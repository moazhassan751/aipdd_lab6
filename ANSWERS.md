# Answers

## Task A3

The FAQ vectors are precomputed once because the FAQ questions do not change
for each request. Each query then compares one new vector with the saved
vectors. Re-encoding all six FAQs for every question would waste time.

## Task B4

`answer_question` returns the matched FAQ question first, so it goes to
`Matched FAQ`. The answer is second, so it goes to `Suggested answer`. The
rounded similarity is third, so it goes to `Cosine similarity`. The status is
the fourth value and goes to `Status`.

## Task C3

The highest cosine similarity only means that the result is closest among the
six stored questions. It does not prove that the question is in scope or that
the answer is correct. For example, an unrelated question can share words or
general academic meaning with an FAQ. Similarity is not confidence or
probability.

## Task D3

Two tabs are two user interactions, not two AI models. Both tabs use the same
FAQ data and the same app file. The Ask a Question tab calls the embedding
model. The Browse FAQs tab only looks up the selected question in `FAQS` and
does not run semantic inference.

## Viva questions

### 1. Which lines create the GUI, run AI inference, and contain app logic?

In the final `app.py`, the `# AI INFERENCE` section is on lines 19-22 and
contains model creation and the saved FAQ vectors. The `retrieve` function on
lines 25-29 performs query encoding and cosine similarity. The `# APP LOGIC`
section starts on line 32 and contains `answer_question` and `browse_answer`.
The `# GUI` section starts on line 51. `create_interface` creates the
Interface, and `create_blocks` creates the Blocks tabs and events.

### 2. Why is the sentence embedding model initialized outside the request handler?

Model loading is slow and uses memory. Creating it once lets every request
reuse the same model instead of loading it again.

### 3. What data types does your Gradio function receive and return?

It receives a text string from the question box, or `None` for a missing
value. It returns four values: three strings or numbers for the matched FAQ,
answer and similarity, plus a status string.

### 4. How does `gr.Interface` differ from `gr.Blocks` here?

`gr.Interface` quickly connects one function to inputs and outputs. `gr.Blocks`
allows a custom layout, two tabs, a Search button click event and a FAQ
dropdown change event.

### 5. Why does the highest cosine similarity not guarantee a correct answer?

It is only the closest item in this small collection. It is not a calibrated
confidence value, and an unrelated question can still be close to an FAQ.

### 6. How would you adapt the same interface architecture for image classification or ASR?

I would replace the text input with an image or audio input and replace
`retrieve` with a classifier or speech-to-text function. The UI could keep
the same separation: input component, inference function, result outputs and
fallback or validation logic.
