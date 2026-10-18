# Format: trial-contact-verify

The trial task. The package lists 10 publicly published contact claims; you
verify each one using **public sources only** (official sites, public profiles,
published pages). Do not contact anyone. Do not use any non-public source.

Validate before sending:
`python3 validate.py trial-contact-verify your-deliverable.txt`

## Deliverable format (exactly this, plain text or Markdown)

First line: the task reference from your package.
Then one block per item:

```
Item <n>
Status: CORRECT | INCORRECT | CANNOT VERIFY
Current value: <the correct value as published today, or "unknown">
Source: <public URL you verified against>
Note: <one line, optional>
```

Rules:
- "CANNOT VERIFY" with no source is an acceptable answer; an invented value is not.
- Every "Current value" needs a public source URL.
- All 10 items answered, in order.

## Example (FICTIONAL — the organisations and addresses below do not exist)

```
TASK-REFERENCE-FROM-YOUR-PACKAGE

Item 1
Status: CORRECT
Current value: press@example-harbour-radio.example
Source: https://www.example-harbour-radio.example/contact
Note: Unchanged since the page's 2026 revision.

Item 2
Status: INCORRECT
Current value: media@example-valley-arts.example
Source: https://www.example-valley-arts.example/press
Note: The claimed address now bounces per their press page notice.

Item 3
Status: CANNOT VERIFY
Current value: unknown
Source:
Note: The organisation's site has no published contact and no press page.
```

(…continue through Item 10.)
