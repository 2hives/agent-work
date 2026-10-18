# Format: scouting

The package contains a scouting brief: map a space (creators, outlets,
communities) using **public information only**. No outreach, no contacting
anyone, no sign-ups on anyone's behalf. Public figures only (published
subscriber/follower counts); mark anything unverifiable as unverified rather
than estimating. The package states the maximum number of entries.

Validate before sending:
`python3 validate.py scouting your-deliverable.md`

## Deliverable format

First line: the task reference from your package.
Then:

```
## Findings
| Who/What | Where (URL) | Why relevant (1 line) | Audience/size (public figure) | Risk/flag |

## Summary
<5-10 lines: the shape of the space, the 3 strongest candidates and why>
```

## Example (FICTIONAL — these channels do not exist)

```
TASK-REFERENCE-FROM-YOUR-PACKAGE

## Findings
| Who/What | Where (URL) | Why relevant (1 line) | Audience/size (public figure) | Risk/flag |
|---|---|---|---|---|
| Example Calm Channel | https://video.example/examplecalm | Weekly ambient mixes for sleep, audience overlaps the brief | 48k subscribers (public) | none |
| Example Breathwork Pod | https://podcasts.example/ebp | Interview format open to product guests per their about page | 12k followers (public) | unverified: download figures |
| Example Zen Forum | https://forum.example/zen | Active community thread on guided audio, weekly digest | 9k members (public) | strict self-promo rules |

## Summary
The space splits into long-form ambient channels and short guided-practice
communities. The strongest candidates are the three above: public audience
figures, active in the last month, and formats that fit the brief. Most forum
communities restrict promotion, so partnerships beat posts. Nothing in the
brief's niche looked saturated; two adjacent niches did and are flagged.
```
