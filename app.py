import argparse

import gradio as gr
from sentence_transformers import SentenceTransformer, util


FAQS = [
    ("How do I register my final year project?", "Contact the FYP office and follow the published registration procedure."),
    ("How can I withdraw from a course?", "Consult the academic office about course withdrawal deadlines and approval."),
    ("How can I reserve laboratory equipment?", "Submit a lab equipment booking request to the laboratory staff."),
    ("Where can I find internship application guidance?", "Consult the career office and internship notices."),
    ("How can I request my academic transcript?", "Apply through the registrar's published transcript procedure."),
    ("How can I reset my student portal password?", "Use the official portal recovery process or contact IT support."),
]

THRESHOLD = 0.35
FALLBACK_TEXT = "No sufficiently relevant FAQ found"

# AI INFERENCE
model = SentenceTransformer("all-MiniLM-L6-v2")
faq_questions = [q for q, a in FAQS]
faq_vectors = model.encode(faq_questions, convert_to_tensor=True)


def retrieve(question):
    query_vector = model.encode(question, convert_to_tensor=True)
    similarities = util.cos_sim(query_vector, faq_vectors)[0]
    idx = int(similarities.argmax().item())
    return FAQS[idx][0], FAQS[idx][1], float(similarities[idx].item())


# APP LOGIC
def answer_question(question):
    if question is None or not isinstance(question, str) or not question.strip():
        return "", "Please enter a question.", 0.0, "Needs clarification"

    matched, answer, similarity = retrieve(question)
    rounded_similarity = round(similarity, 3)
    if similarity < THRESHOLD:
        return matched, FALLBACK_TEXT, rounded_similarity, "Needs clarification"
    return matched, answer, rounded_similarity, "Matched"


def browse_answer(question):
    for faq_question, answer in FAQS:
        if faq_question == question:
            return answer
    return ""


# GUI
def create_interface():
    return gr.Interface(
        fn=answer_question,
        inputs=gr.Textbox(label="Your academic question", lines=2),
        outputs=[
            gr.Textbox(label="Matched FAQ"),
            gr.Textbox(label="Suggested answer"),
            gr.Number(label="Cosine similarity"),
            gr.Textbox(label="Status"),
        ],
        examples=[
            ["I need to sign up for my final year project"],
            ["What is the process to leave a course?"],
            ["Where do I book lab equipment?"],
            ["I forgot my student portal password"],
        ],
        title="University Academic Helpdesk",
        description=(
            "Ask an academic question in everyday language. Answers are illustrative "
            "and are not official university policy. Cosine similarity is not a confidence score."
        ),
    )


def create_blocks():
    with gr.Blocks() as demo:
        gr.Markdown("# University Academic Helpdesk")
        gr.Markdown(
            "Answers are illustrative. Cosine similarity is not a confidence or probability."
        )

        with gr.Tab("Ask a Question"):
            question = gr.Textbox(label="Question", lines=2)
            search_btn = gr.Button("Search")
            matched = gr.Textbox(label="Matched FAQ")
            answer = gr.Textbox(label="Suggested answer")
            similarity = gr.Number(label="Similarity")
            status = gr.Textbox(label="Status")
            search_btn.click(
                fn=answer_question,
                inputs=question,
                outputs=[matched, answer, similarity, status],
            )

        with gr.Tab("Browse FAQs"):
            faq_dropdown = gr.Dropdown(
                choices=faq_questions,
                label="FAQ topic",
                value=faq_questions[0],
            )
            faq_answer = gr.Textbox(label="FAQ answer")
            faq_dropdown.change(fn=browse_answer, inputs=faq_dropdown, outputs=faq_answer)

    return demo


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--interface", action="store_true")
    args = parser.parse_args()
    demo = create_interface() if args.interface else create_blocks()
    demo.launch()
