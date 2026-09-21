# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

Retrieval is not always perfect, even when the answer exists somewhere in the corpus, because the embedding search may not always return the correct chunk among the top results. I allow one retrieval miss, but if the system misses two or more of the five questions, I would consider the retrieval too unreliable.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

The goal of this system is to produce answers that are grounded in the provided documents. Therefore, every generated answer should identify its source, and if the documents do not contain enough information, the system should say that instead of producing an unsupported answer. Because grounding is a core requirement of the system, my target is 100%.


---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

Questions that are not covered by the corpus should be stopped before they reach the model because unrelated retrieved chunks could lead to unsupported answers. Semantic similarity is not a perfect classifier, so I allow one false positive, but if two or more unrelated questions pass the gate, I would consider the relevance gate too unreliable.

---

## 4. Something about your chunks

I will inspect 5 sampled chunks. 5 of them should keep a selected sentence together with its surrounding sentences when those sentences exist, so the chunk preserves enough context to be understood on its own.



**Why this target:**

I want every sampled chunk to preserve the context around its main sentence rather than cutting an idea into isolated pieces. I chose 5 out of 5 because preserving surrounding context is part of my chunking strategy, so each sampled chunk should follow that rule.




---

## 5. Your choice


For Every test questions, the answer should not include factual claims that are unsupported by the retrieved documents.

**Why this target:**

The purpose of the RAG system is to answer questions using the retrieved documents rather than adding information from the model’s existing knowledge. Because an unsupported factual claim would violate that goal and could mislead the user, I expect all 5 test answers to remain grounded in the retrieved evidence.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
