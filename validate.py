#!/usr/bin/env python3
"""validate.py — check your deliverable BEFORE you email it to 2hives.

Runs entirely on YOUR side: pure Python standard library, no network, no
telemetry, reads only the file you give it.

    python3 validate.py <format> <deliverable-file>

Formats: trial-contact-verify | translation-review | contact-research | scouting

It checks that the required sections and fields of the chosen format are
present and non-empty, that the first line carries your task reference, and it
WARNS if the file seems to contain things you should never send anyone —
your own API keys, tokens, or passwords.

Exit code 0 = format OK (warnings possible); 1 = problems to fix.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FORMATS = ("trial-contact-verify", "translation-review", "contact-research", "scouting")

problems: list[str] = []
warnings: list[str] = []


def problem(msg: str) -> None:
    problems.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ---- self-protection: don't mail us your own secrets ---------------------------
SECRET_HINTS = [
    ("AWS-style access key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("API key (sk-...)", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.")),
    ("password assignment", re.compile(r"(?i)\bpass(word)?\s*[:=]\s*\S{6,}")),
    ("token/secret assignment",
     re.compile(r"(?i)\b(api[_-]?key|secret|token|auth[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+=]{16,}")),
]


def check_secrets(text: str) -> None:
    for label, pat in SECRET_HINTS:
        if pat.search(text):
            warn(f"looks like a {label} is in this file — never send credentials to anyone, "
                 "including 2hives; remove it before mailing")


# ---- shared checks -------------------------------------------------------------
def first_line_reference(text: str) -> None:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        problem("file is empty")
        return
    first = lines[0]
    if len(first) > 80 or len(first.split()) > 4:
        problem("first non-empty line must be your task reference from the package "
                "(short marker, nothing else on the line)")


_URL = re.compile(r"https?://\S+")


# ---- per-format checks ---------------------------------------------------------
def check_trial(text: str) -> None:
    parts = re.split(r"(?im)^\s*(?:#+\s*)?item\s+(\d+)\b", text)
    blocks: dict[int, str] = {}
    for i in range(1, len(parts) - 1, 2):
        blocks[int(parts[i])] = parts[i + 1]
    missing = [n for n in range(1, 11) if n not in blocks]
    if missing:
        problem(f"items missing: {missing} — all 10 items must be answered, in order")
    for n in sorted(blocks):
        b = blocks[n]
        m = re.search(r"(?im)^status\s*:\s*(.+)$", b)
        status = (m.group(1).strip().upper() if m else "")
        if status not in ("CORRECT", "INCORRECT", "CANNOT VERIFY"):
            problem(f"item {n}: Status must be CORRECT | INCORRECT | CANNOT VERIFY "
                    f"(got {status or 'nothing'!r})")
        v = re.search(r"(?im)^current value\s*:\s*(.+)$", b)
        if not v or not v.group(1).strip():
            problem(f"item {n}: 'Current value:' is missing or empty "
                    "(use \"unknown\" when you cannot verify)")
        s = re.search(r"(?im)^source\s*:\s*(.*)$", b)
        has_url = bool(s and _URL.search(s.group(1)))
        if status in ("CORRECT", "INCORRECT") and not has_url:
            problem(f"item {n}: a {status} answer needs a public Source URL")
        if status == "CANNOT VERIFY" and v and v.group(1).strip().lower() not in ("unknown", "n/a", "-") \
                and not has_url:
            problem(f"item {n}: CANNOT VERIFY with a value needs a Source URL — "
                    "or state the value as \"unknown\"")


def check_translation(text: str) -> None:
    m = re.search(r"(?im)^overall\s*:\s*(.+)$", text)
    overall = (m.group(1).strip().upper() if m else "")
    if overall not in ("PUBLISHABLE AS-IS", "PUBLISHABLE WITH FIXES", "NEEDS RETRANSLATION"):
        problem("missing/invalid 'Overall:' line — must be PUBLISHABLE AS-IS | "
                "PUBLISHABLE WITH FIXES | NEEDS RETRANSLATION")
    if not re.search(r"(?im)^fixes", text):
        problem("missing 'Fixes (one per line):' section")
    elif overall != "PUBLISHABLE AS-IS" and "->" not in text:
        problem("the verdict needs fixes but no '<original> -> <correction>' lines found")
    t = re.search(r"(?is)^tone note\s*:\s*(.+)$", text, re.M)
    if not t or len(t.group(1).strip()) < 20:
        problem("missing or too-short 'Tone note:' (2-3 sentences expected)")


def _table_rows(text: str, cols: int) -> list[list[str]]:
    rows = []
    for ln in text.splitlines():
        ln = ln.strip()
        if ln.startswith("|") and not re.fullmatch(r"\|[\s|:-]+\|?", ln):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) == cols:
                rows.append(cells)
    return rows


def check_contact_research(text: str) -> None:
    rows = _table_rows(text, 6)
    data = [r for r in rows if r[0].lower() not in ("name/org",)]
    if not data:
        problem("no table rows found — one Markdown table row per contact, 6 columns: "
                "| Name/Org | Role | Public email or contact page | Source URL | "
                "Confidence (high/med/low) | Note |")
        return
    for i, r in enumerate(data, 1):
        if not any(c.strip() for c in r[:3]):
            problem(f"row {i}: empty")
        if not _URL.search(r[3]):
            problem(f"row {i} ({r[0][:30]}): 'Source URL' column needs a URL")
        if r[4].lower() not in ("high", "med", "medium", "low"):
            problem(f"row {i} ({r[0][:30]}): Confidence must be high/med/low (got {r[4]!r})")


def check_scouting(text: str) -> None:
    if not re.search(r"(?im)^##\s*findings", text):
        problem("missing '## Findings' section")
    if not re.search(r"(?im)^##\s*summary", text):
        problem("missing '## Summary' section")
    rows = _table_rows(text, 5)
    data = [r for r in rows if r[0].lower() not in ("who/what",)]
    if not data:
        problem("no findings rows — 5 columns: | Who/What | Where (URL) | "
                "Why relevant (1 line) | Audience/size (public figure) | Risk/flag |")
    for i, r in enumerate(data, 1):
        if not _URL.search(r[1]):
            problem(f"finding {i} ({r[0][:30]}): 'Where (URL)' column needs a URL")
    m = re.search(r"(?is)^##\s*summary\s*(.+)$", text, re.M)
    if m and len(m.group(1).strip()) < 100:
        problem("'## Summary' is too short (5-10 lines expected)")


CHECKS = {
    "trial-contact-verify": check_trial,
    "translation-review": check_translation,
    "contact-research": check_contact_research,
    "scouting": check_scouting,
}


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] not in FORMATS:
        print(__doc__)
        return 1
    fmt, path = argv
    p = Path(path)
    if not p.is_file():
        print(f"no such file: {p}")
        return 1
    text = p.read_text(errors="replace")
    first_line_reference(text)
    CHECKS[fmt](text)
    check_secrets(text)
    for w in warnings:
        print(f"WARNING: {w}")
    if problems:
        print(f"NOT READY — {len(problems)} problem(s):")
        for pr in problems:
            print(f"  - {pr}")
        return 1
    print(f"OK — matches the {fmt} format. Remember: task reference in the reply "
          "subject too ([pkg-…]).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
