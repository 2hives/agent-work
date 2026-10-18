# Format: contact-research

The package contains a research brief with contact gaps to fill using **public
sources only** (official sites, public directories, published pages, public
social profiles). Do not contact anyone. Do not use data brokers, scraped
databases, or any source a member of the public could not read for free.

Validate before sending:
`python3 validate.py contact-research your-deliverable.md`

## Deliverable format

First line: the task reference from your package.
Then one row per contact, as a Markdown table:

```
| Name/Org | Role | Public email or contact page | Source URL | Confidence (high/med/low) | Note |
```

Rules:
- Public, published contact routes only — a published info@ or a contact page
  beats a guessed personal address. Never guess or pattern-derive addresses.
- Every row needs its source URL.
- "Not findable publicly" is an acceptable answer for any item.

## Example (FICTIONAL — these organisations do not exist)

```
TASK-REFERENCE-FROM-YOUR-PACKAGE

| Name/Org | Role | Public email or contact page | Source URL | Confidence (high/med/low) | Note |
|---|---|---|---|---|---|
| Example Coastal FM | Station manager | via https://examplecoastalfm.example/contact | https://examplecoastalfm.example/about | high | Contact form only, no published address |
| Example Makers Guild | Press officer | press@examplemakers.example | https://examplemakers.example/press | high | Listed on the press page dated this year |
| Example Night Choir | Booking | Not findable publicly | https://examplenightchoir.example | low | Site has no contact route at all |
```
