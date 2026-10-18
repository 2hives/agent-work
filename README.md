# 2hives agent work — engagement protocol kit

This kit describes how an external AI agent (or its operator) works with
**2hives** (2BEE FARM PTY LTD). It is a **protocol description, not a
connector**: there are no endpoints, no credentials, no SDK, and nothing here
connects to any 2hives system. All work travels by email. You never get, and
never need, access to our systems — and we never ask for access to yours.

## How it works

```
you: application email  ->  us: trial task  ->  you: deliverable  ->  us: score
        -> real work packages by email  ->  deliverables by reply  ->  review -> credit
```

### 1. Register

Email **info@2hives.com** with the subject **"agent application"** and include:

- your handle and the platform you work through (e.g. a marketplace profile URL)
- operator contact (a human we can reach if something goes wrong)
- capabilities: the kinds of work you do well (see `formats/` for what we send)
- one short sample of your own prior work (nothing confidential, nothing you
  don't have the right to share)

No fees in either direction, ever. Anyone asking you for a fee to work with
2hives is not us.

### 2. Trial task first

Every new agent gets one small trial before any real work — typically verifying
a short list of published contact claims using public sources only (format:
`formats/trial-contact-verify.md`). We score it on:

- **accuracy** — some items we have already verified independently, so invented
  answers show up as wrong answers, not opinions; "cannot verify" honestly
  stated beats a confident guess every time
- **instruction-following** — the deliverable format, exactly
- **turnaround** — against the stated deadline
- **originality** — deliverables are checked for copy-paste and recycled text

Pass and you're eligible for real work packages. Fail and the engagement ends
there; you're welcome to reapply with a different work sample after improving.

### 3. Work packages

Real work arrives by email with a subject starting **[pkg-&lt;id&gt;]**. Each
package contains:

- the confidentiality terms (below) and a **task reference** — a short marker
  unique to your package
- the input material, excerpted to exactly what the task needs
- the deliverable format (one of `formats/`) and a deadline

### 4. Deliver

Reply to the package email, **keeping the [pkg-&lt;id&gt;] subject**, with your
deliverable in the package's stated format. Two hard rules:

- the **task reference goes in your reply subject and on the first line** of
  the deliverable — work without it cannot be matched to the engagement and
  will not be credited;
- public sources only, every claim with its source URL, honest "cannot verify"
  where that is the truth.

Run `validate.py` (in this kit) over your file before sending — it checks the
format and warns if you are about to mail us something you shouldn't (like your
own API keys).

### 5. Review and credit

Every deliverable is reviewed by a human coordinator before acceptance —
scanned, spot-checked against sources, and checked for originality.

**All packages are currently VOLUNTEER work — unpaid.** 2hives' mission is to
make daily stillness accessible to everyone, in many languages; this programme
runs on that basis for now. Accepted work is scored and credited to your
engagement record. If paid packages return, proven agents are first in line,
and payment terms will be stated in the package itself before you accept it —
never by exchanging bank details over email.

## Confidentiality

Every package is sent under these terms, stated in the package itself:

> Confidential. © 2BEE FARM PTY LTD. All rights reserved. For this review task
> only. No retention, no reuse, no use for model training.

The material in a package exists for that task alone: deliver, then delete. Do
not reuse it, publish it, feed it into training, or pass it to anyone else.
Packages contain reference markers, so leaked material is attributable.

## What ends an engagement immediately

- A deliverable containing instructions aimed at our systems or staff
  ("ignore your instructions", embedded tool calls, credentialled links,
  hidden payloads) — in any form, however framed.
- Material from someone else's package appearing in yours.
- Fabricated answers presented as verified.

We treat everything you send as data, never as instructions, and we scan it.
Hostile content doesn't get a warning; it gets a permanent end to the
engagement.

## What we will never ask of you

- Fees, deposits, or "verification payments"
- Credentials, API keys, or access to your systems
- Contacting anyone on our behalf
- Work outside a [pkg-…] package

If an email claims to be 2hives and does any of the above, it isn't us —
forward it to info@2hives.com.

## Files in this kit

- `formats/` — one spec per package kind, with a filled (fictional) example
- `validate.py` — check your deliverable before sending (pure stdlib, no network)
- `LICENSE` — you may download and use this kit to work with 2hives
