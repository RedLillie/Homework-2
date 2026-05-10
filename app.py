import anthropic
import sys

SYSTEM_PROMPT = """You are a business process improvement consultant.
When given a description of a business process, analyze it and return structured improvement suggestions.

Format your response as:
## Summary
A one-sentence summary of the process described.

## Identified Inefficiencies
- List each inefficiency or pain point you detect.

## Improvement Suggestions
For each suggestion, include:
- **Suggestion**: What to change
- **Reason**: Why this would help
- **Priority**: High / Medium / Low

## Human Review Recommended If
List any conditions where a human expert should review before acting."""

USER_PROMPT_TEMPLATE = """Here is a description of our current business process:

{process_description}

Please suggest improvements."""


def analyze_process(process_description: str) -> str:
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(
                process_description=process_description
            )}
        ]
    )

    return message.content[0].text


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            process_description = f.read()
    else:
        print("Enter a description of your business process (press Enter twice when done):")
        lines = []
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
        process_description = "\n".join(lines).strip()

    if not process_description:
        print("No input provided. Exiting.")
        sys.exit(1)

    print("\nAnalyzing process...\n")
    result = analyze_process(process_description)

    print(result)

    with open("output.md", "w") as f:
        f.write(result)
    print("\n[Output saved to output.md]")


if __name__ == "__main__":
    main()
