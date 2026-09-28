from generate import generate


SCORER_INSTRUCTION = """
You are an evaluation grader.

Your job is to determine whether a generated answer is semantically correct
according to the expected answer.

Rules:
- Judge meaning, not exact wording.
- Paraphrases are allowed.
- The generated answer may contain additional explanation or source names.
- Numbers, dates, times, quantities, and yes/no facts must agree with the
  expected answer.
- Do not require the exact expected phrase to appear.
- Ignore differences in capitalization and formatting.
- Return exactly PASS or FAIL.
"""


def judge(question, expects, answer, results) -> bool:
    prompt = f"""
Question:
{question}

Expected answer:
{expects}

Generated answer:
{answer}

Does the generated answer correctly express the expected answer?
"""

    verdict = generate(
        prompt,
        system=SCORER_INSTRUCTION,
        cache=True,
    )

    verdict = verdict.strip().upper()

    print(
        f"LLM judge: {verdict} | "
        f"expected={expects!r}"
    )

    return verdict == "PASS"
