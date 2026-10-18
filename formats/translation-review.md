# Format: translation-review

The package contains a machine-translated DRAFT excerpt of content destined for
publication, and names the target language. Review it as a native speaker.

Rules (as stated in every package):
- Correct the draft; do not rewrite it into your own text.
- Flag anything culturally off or unintentionally funny/offensive.
- Do not add content. Do not translate beyond the excerpt.

Validate before sending:
`python3 validate.py translation-review your-deliverable.txt`

## Deliverable format

First line: the task reference from your package.
Then:

```
Overall: PUBLISHABLE AS-IS | PUBLISHABLE WITH FIXES | NEEDS RETRANSLATION
Fixes (one per line):
<line/segment reference>: <original> -> <your correction> — <why, briefly>
Tone note: <2-3 sentences on register/naturalness for this audience>
```

## Example (FICTIONAL draft and fixes)

```
TASK-REFERENCE-FROM-YOUR-PACKAGE

Overall: PUBLISHABLE WITH FIXES
Fixes (one per line):
line 2: "relaxing sound bath" -> "soothing sound journey" — literal rendering reads clinical in this register
line 5: "press start for calm" -> "begin whenever you are ready" — imperative feels abrupt to native ears
line 9: "deep rest state" -> "state of deep rest" — word order
Tone note: The draft is understandable throughout but leans formal for a
wellbeing audience; the fixes soften it to the conversational register native
speakers expect from this kind of product copy.
```
