# Week 06 University Academic Helpdesk

This project is a small semantic FAQ search prototype. It uses the fixed FAQ
list from the lab manual. The answers are illustrative and are not official
university policy.

## Setup

Create and activate the virtual environment on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The first run downloads the `all-MiniLM-L6-v2` sentence embedding model. Later
runs can use the cached model.

## Run

The default command starts the Blocks application:

```powershell
python app.py
```

The Phase B and C interface can be started with:

```powershell
python app.py --interface
```

The default threshold is `0.35`. It is defined as `THRESHOLD` near the top of
`app.py`. Change that value, then repeat the threshold tests before relying on
the result.

Cosine similarity measures how close two embeddings are. It is not a
confidence score and it is not a probability that the answer is correct.

## Limitations

The system only knows six FAQs. A question outside this set can still be close
to an FAQ in embedding space and may get a high score. A threshold alone
cannot guarantee that a result is correct. A larger verified FAQ set, a
separate out-of-scope classifier, and human review for low-margin matches
would improve it. The model also does not check current university policy.
