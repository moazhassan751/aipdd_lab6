# Test Table

The final threshold is `0.35`. Each result below was produced by
`answer_question` after the model loaded.

| Test input | Expected behavior | Actual result | Pass/Fail |
|---|---|---|---|
| How do I register my FYP? | Relevant FYP answer | Matched `How do I register my final year project?`; score `0.484`; status `Matched` | Pass |
| I want to drop a subject | Course withdrawal FAQ | Matched `How can I withdraw from a course?`; score `0.391`; status `Matched` | Pass |
| How can I book lab equipment? | Lab booking FAQ | Matched `How can I reserve laboratory equipment?`; score `0.722`; status `Matched` | Pass |
| (empty input) | Helpful validation response | Answer `Please enter a question.`; score `0.0`; status `Needs clarification` | Pass |
| Tell me the cricket score | Fallback / out-of-scope | Top match was the password FAQ, but answer was `No sufficiently relevant FAQ found`; score `0.101`; status `Needs clarification` | Pass |
| asdf qwer zxcv | Graceful handling | Top match was the internship FAQ, but answer was `No sufficiently relevant FAQ found`; score `0.072`; status `Needs clarification` | Pass |
| What is campus life? | Graceful handling of an ambiguous question | Top match was the course withdrawal FAQ, but answer was `No sufficiently relevant FAQ found`; score `0.231`; status `Needs clarification` | Pass |
| Where can I find internship help? | Relevant internship answer | Matched `Where can I find internship application guidance?`; score `0.821`; status `Matched` | Pass |
| I forgot my student portal password | Relevant password answer | Matched `How can I reset my student portal password?`; score `0.908`; status `Matched` | Pass |

## Threshold comparison

| Input | Score | Result at 0.50 | Result at 0.35 |
|---|---:|---|---|
| How do I register my FYP? | 0.484 | Needs clarification | Matched |
| I want to drop a subject | 0.391 | Needs clarification | Matched |
| How can I book lab equipment? | 0.722 | Matched | Matched |
| Tell me the cricket score | 0.101 | Needs clarification | Needs clarification |
| asdf qwer zxcv | 0.072 | Needs clarification | Needs clarification |

The `0.35` threshold was selected from these tests because it keeps the two
required paraphrases while rejecting the unrelated and gibberish inputs.

## Borderline or false match

The cricket question's top-ranked FAQ was the password FAQ even though the
question is unrelated. Its score was only `0.101`, so the final threshold
rejected it. This is still a false top match. A larger verified FAQ set and a
separate out-of-scope classifier would be safer than relying on the threshold
alone.

## Robustness checks

`None`, an empty string, spaces only, numbers, symbols and a 10,000-character
string were tested. They did not crash the app. Empty values returned
`Please enter a question.`. The number, symbol and long-string checks returned
`No sufficiently relevant FAQ found` with status `Needs clarification`.
