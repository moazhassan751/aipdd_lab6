# Reflection

The app keeps the user interface separate from the model work. The model is
created once when the file starts, and the six FAQ questions are encoded once.
The search function only encodes the new question and returns four simple
values for the interface. This avoids repeating the expensive setup for every
button click. The Blocks version adds a second way to use the same app. Its
Browse FAQs tab reads an answer directly from the FAQ list, so browsing does
not run semantic inference.

The main limitation is the small FAQ list. A cricket question can still look
similar to an academic question because embeddings compare meaning rather than
checking facts. The threshold helps, but it is not a guarantee. Cosine
similarity is not a confidence or probability. The app also cannot know when a
university rule has changed. A better version could use more verified FAQs,
show two close matches when the scores are close, and send uncertain questions
to staff. A separate out-of-scope check could reject topics such as sports
before retrieval. A database and an update process would also keep the answers
current.
