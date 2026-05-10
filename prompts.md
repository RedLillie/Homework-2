# Prompt Iterations

## Version 1 — Initial Prompt

**System:**
> You are a helpful assistant. When given a business process description, suggest improvements.

**What changed**: Too vague. The model gave unstructured, conversational responses with no consistent format.

---

## Version 2 — Added Structure

**System:**
> You are a business process improvement consultant.
> When given a description of a business process, analyze it and return structured improvement suggestions.
>
> Format your response as:
> - Summary
> - Identified Inefficiencies
> - Improvement Suggestions (with reason and priority)

**What changed**: Added role framing and required output structure.
**What improved**: Responses became consistent and easier to parse. Priority labels helped distinguish critical changes from nice-to-haves.
**What stayed the same**: The model still sometimes over-suggested changes for simple processes.

---

## Version 3 — Added Human Review Guidance

**System:**
> (Same as Version 2, plus:)
> ## Human Review Recommended If
> List any conditions where a human expert should review before acting.

**What changed**: Added a section prompting the model to flag uncertainty.
**What improved**: The model now surfaces edge cases and high-risk suggestions for human review rather than presenting everything with equal confidence.
**What got worse**: Slightly longer outputs; not ideal for very simple process descriptions.
