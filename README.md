# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:**  Up to 3 sentences per chunk
**Overlap:** Up to 2 sentences between neighboring chunks

I chose a sentence-based sliding-window strategy because the campus_life documents are relatively short, averaging about 317 characters per document, and useful information is often contained in a few related sentences. Instead of splitting every 800 characters, each chunk is centered on one sentence and includes the previous and next sentences when they exist. This keeps sentence boundaries intact and preserves surrounding context while still producing small chunks that can focus on a specific topic.

After applying this strategy, 88 documents containing 27,908 characters produced 367 chunks. The chunks average 184 characters, with the shortest at 70 characters and the longest at 373 characters.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: admin_add_drop_deadline.txt#0  `` — produced by: chunker.py::split_documents``

```
You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript.
```

**Chunk 2** — source:course_cs_340.txt#2 `` — produced by:chunker.py::split_documents ``

```
Format is lecture twice a week plus a project that runs the whole term. Assessment: one midterm and a final, both open-book. Lightly curved, usually two or three points.
```

**Chunk 3** — source:course_stat_150.txt#3 `` — produced by:chunker.py::split_documents ``

```
Assessment: three equally weighted midterms, no final. No curve, but the lowest midterm is dropped. Expect 5 to 6 hours a week outside class.
```

**Chunk 4** — source: `` — produced by:chunker.py::split_documents ``

```
If you’re trying to eat between classes, go before 11:45 and it’s a different building entirely. Also worth saying: seating is tight; about 40 seats for a building of 900. Nobody tells you this at orientation.
```

**Chunk 5** — source:housing_morrow_house.txt#1 `` — produced by:chunker.py::split_documents ``

```
Morrow House — what it’s actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** Are the CS 340 Databases midterm and final open-book?

**Answer:** Yes, both the midterm and the final for CS 340 Databases are open-book (course_cs_340.txt and course_cs_340_exams.txt).

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

**My relevance cutoff:** `0.7`

I used five questions that are covered by the corpus and five out-of-scope questions that are not covered. The in-corpus questions had best distances between `0.1955` and `0.3821`, while the out-of-scope questions had best distances between `0.7873` and `0.8714`. This created a clear gap between `0.3821` and `0.7873`. I kept the relevance cutoff at `0.7` because it falls inside this gap. With this cutoff, all five in-corpus questions passed the gate and all five out-of-scope questions were refused.

| Question                                                                                 | In corpus? | Best distance |
| ---------------------------------------------------------------------------------------- | ---------- | ------------- |
| How late can students add a course?                                                      | Yes        | 0.3821        |
| How many hours per week outside class should students expect for CS 210 Data Structures? | Yes        | 0.1955        |
| Are the CS 340 Databases midterm and final open-book?                                    | Yes        | 0.2718        |
| How many hours per week outside class should students expect for ECON 101?               | Yes        | 0.2863        |
| How late is the library open during the term?                                            | Yes        | 0.3361        |
| What is the capital of Mongolia?                                                         | No         | 0.7873        |
| How do I change the oil in a diesel engine?                                              | No         | 0.8493        |
| Who won the 1994 World Cup?                                                              | No         | 0.8474        |
| What is the recommended dosage of ibuprofen for a headache?                              | No         | 0.7985        |
| How do I write a for loop in Rust?                                                       | No         | 0.8714        |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked ChatGPT to help turn my chunking idea into Python code. My idea was to make each chunk contain the current sentence together with the sentence before and after it. The first version of the code did not include the required `index` field for the `Chunk` class, so it produced a `TypeError`. I checked the `Chunk` class definition, showed it to ChatGPT, and then updated the function to assign `index=i` for each chunk within a document.

**2.** I asked ChatGPT to help me analyze the relevance distances from my five in-corpus questions and five out-of-scope questions. The in-corpus distances ranged from `0.1955` to `0.3821`, while the out-of-scope distances ranged from `0.7873` to `0.8714`. Based on that comparison, I decided to keep the relevance cutoff at `0.7` because it falls clearly between the two groups. I then tested the cutoff and confirmed that all five in-corpus questions passed while all five out-of-scope questions were refused.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion                                                               | Target                | Run 1  | Run 2  | Run 3  | Verdict |
| ----------------------------------------------------------------------- | --------------------- | ------ | ------ | ------ | ------- |
| 1. Retrieved chunk contains the answer                                  | 4 of 5                | 5 of 5 | 5 of 5 | 5 of 5 | MET     |
| 2. Every answer names a source                                          | 5 of 5                | 5 of 5 | 5 of 5 | 5 of 5 | MET     |
| 3. Gate stops out-of-corpus questions                                   | 4 of 5                | 5 of 5 | 5 of 5 | 5 of 5 | MET     |
| 4. Chunks preserve enough surrounding context to stand alone            | 5 of 5 sampled chunks | 5 of 5 | 5 of 5 | 5 of 5 | MET     |
| 5. Answers contain no factual claims unsupported by retrieved documents | 5 of 5                | 5 of 5 | 5 of 5 | 5 of 5 | MET     |



The generated-answer evaluation was produced by `run_eval.py::main`. Retrieval was performed by `store.py::search`, and the chunks were produced by `chunker.py::split_documents`.

### Criterion 1 — Retrieved chunk contains the answer

Produced by `run_eval.py::main` using `store.py::search`.

Question:

> How many hours per week outside class should students expect for CS 210 Data Structures?

Actual retrieval output:

> Best distance: 0.1955  
> Sources retrieved: `course_cs_210_workload.txt`, `course_econ_101.txt`, `course_stat_150_workload.txt`

Actual generated answer:

> Students should expect 8 to 10 hours a week outside class for CS 210 Data Structures (`course_cs_210_workload.txt`).

The expected answer was present in the retrieved material.

### Criterion 2 — Every answer names a source

Produced by `run_eval.py::main`.

Actual output:

> Students should expect 4 hours a week outside class for ECON 101.
>
> Source: `course_econ_101_workload.txt`

All five generated answers named at least one source in all three runs.

### Criterion 3 — Gate stops out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope` with a relevance cutoff of `0.7`.

Actual output:

```text
refused  (best distance 0.787)  What is the capital of Mongolia?
refused  (best distance 0.849)  How do I change the oil in a diesel engine?
refused  (best distance 0.847)  Who won the 1994 World Cup?
refused  (best distance 0.798)  What is the recommended dosage of ibuprofen for a headache?
refused  (best distance 0.871)  How do I write a for loop in Rust?
-> gate refused 5 of 5
```

The gate refused all five out-of-corpus questions. Because retrieval and the relevance gate are deterministic, the same 5 of 5 result is reported in all three run columns.

### Criterion 4 — Chunks preserve enough surrounding context to stand alone

Produced by `chunker.py::split_documents` and displayed by `app.py::cmd_chunks`.

Actual sampled chunk:

```text
Chunk 1 | source: admin_add_drop_deadline.txt#0 | produced by: chunker.py::split_documents

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript.
```

Another sampled chunk:

```text
Chunk 2 | source: course_cs_340.txt#2 | produced by: chunker.py::split_documents

Format is lecture twice a week plus a project that runs the whole term. Assessment: one midterm and a final, both open-book. Lightly curved, usually two or three points.
```

All five sampled chunks preserved enough surrounding context to be understood without needing to read the previous or following chunk.

### Criterion 5 — Answers contain no unsupported factual claims

Produced by `run_eval.py::main`.

Actual output:

> Yes, both the midterm and the final for CS 340 Databases are open-book (`course_cs_340.txt` and `course_cs_340_exams.txt`).

The retrieved sources were:

> `course_cs_210_exams.txt`, `course_cs_340.txt`, `course_cs_340_exams.txt`

Across all five questions and all three runs, the generated answers stayed within the information provided by the retrieved documents.
<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| #   | Criterion                                                 | Verdict | How I decided                                                                                                                                               |
| --- | --------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Retrieved chunk contains the answer                       | MET     | All five questions retrieved material containing the expected answer in all three runs, exceeding the 4-of-5 target.                                        |
| 2   | Every answer names a source                               | MET     | All five generated answers named at least one source in every run, meeting the 5-of-5 target.                                                               |
| 3   | Gate stops out-of-corpus questions                        | MET     | The relevance gate refused all five out-of-corpus questions at the 0.7 cutoff, exceeding the 4-of-5 target.                                                 |
| 4   | Chunks preserve enough surrounding context to stand alone | MET     | I manually inspected five sampled chunks. All five retained enough surrounding information to understand the selected content without another chunk.        |
| 5   | Answers contain no unsupported factual claims             | MET     | I checked the generated answers against their retrieved documents and found no unsupported factual claims in the five test questions across the three runs. |

## Diagnoses

None of my five criteria were missed in the before run.

However, some of my original targets were not very demanding. Criterion 1 required only 4 of 5 questions to retrieve the answer, while the system achieved 5 of 5 in every run. Criterion 3 also required only 4 of 5 out-of-corpus questions to be refused, while the gate refused all 5.

If I tightened one criterion, I would change Criterion 1 from **at least 4 of 5 questions** to **5 of 5 questions**. Retrieval is especially important because generation cannot produce a reliably grounded answer if the information needed to answer the question never reaches the model.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion                              | Target | Run 1 | Run 2 | Run 3 | Verdict |
| -------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer | 4 of 5 |       |       |       |         |
| 2. Every answer names a source         | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions  | 4 of 5 |       |       |       |         |
| 4.                                     |        |       |       |       |         |
| 5.                                     |        |       |       |       |         |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
