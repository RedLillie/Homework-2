# Report — Process Improvement Suggester

## Business Use Case
Many organizations struggle to consistently analyze and improve internal workflows. Managers often lack time to conduct structured process reviews. This tool allows any employee to submit a plain-text description of a process and receive structured, prioritized improvement suggestions instantly — reducing the barrier to continuous improvement.

## Model Choice
**Model used**: claude-sonnet-4-6

Claude Sonnet 4.6 was chosen for its strong instruction-following, consistent structured output, and cost efficiency for a prototype. It reliably follows formatting instructions and handles both simple and nuanced process descriptions well.

## Baseline vs. Final Design

| Aspect | Baseline (v1) | Final (v3) |
|---|---|---|
| Output format | Unstructured prose | Structured sections with priorities |
| Role framing | Generic assistant | Business process consultant |
| Edge case handling | None | Flags human review conditions |
| Consistency | Variable | Repeatable across test cases |

The most impactful change was adding structured output requirements. The addition of a "Human Review Recommended If" section in v3 significantly improved the tool's reliability for sensitive or ambiguous cases.

## Where the Prototype Still Fails
The system struggles with vague inputs — when a user provides minimal context, the model sometimes fills in process details that were never mentioned (hallucination). It also cannot access real organizational data, so suggestions are generic rather than tailored to company-specific constraints. Human review is essential before acting on any output.

## Deployment Recommendation
This prototype is suitable for **internal use with human review**, not autonomous deployment. It works best as a first-pass tool that surfaces ideas for a manager or process owner to evaluate. It should not be used in high-stakes domains (healthcare, finance, legal) without domain expert review of every output. A deployment-ready version would require output validation, user feedback loops, and guardrails against hallucinated specifics.
