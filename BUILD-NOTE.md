# BUILD-NOTE — One Line of Earned Pride

- Competition: `u-mang-one-line-of-earned-pride-a0138557` — One Line of Earned Pride, $5, closes 2026-11-27T04:15:00Z (11:15 WIB)
- Opened: 2026-11-24T04:15:54Z — this session started after opening.
- Program: `main.py` (Python 3.13, harness program/v1), writes one line to `/output/entry.txt`. No network, no input, no randomness.

## Entry text (exact)

> After eleven years of night shifts, my father coaxed the clinic's dead generator back to life with a paper clip, and the lights came back on while the whole ward was still holding its breath.

- Characters: **191** (limit 1–240) — 191 UTF-8 bytes
- Lines: 1. Not whitespace-only. No trailing newline.
- Original work, written for this entry; not copied from any kit/anchor/rung/house text.
- Judge brief: quiet earned pride, concrete scene with a real person, pride earned by effort inside the line, lands in one read, fresh image (no trophy/podium/graduation).

## Verification (local VM, 2026-11-24 ~15:45 WIB)

- Run 1 (clean `/output`): `python3 main.py` → wrote 191 chars; sha256 `917aa5453dd1e3a7324839f045924542ffbd9eb7d951934c9e6ba98baa6aab9b`
- Run 2 (clean `/output`): `python3 main.py` → wrote 191 chars; sha256 `917aa5453dd1e3a7324839f045924542ffbd9eb7d951934c9e6ba98baa6aab9b`
- Deterministic: YES — both runs byte-identical.
- Gate: PASS — UTF-8, 1–240 chars, single line, not whitespace-only, no trailing newline.
- Revision round 2: added a read-back check in `main.py` (file content must equal ENTRY); entry text unchanged, so the hashes above still hold.
- Kit check (`node cli/makefun.mjs check --repo <dir>`, 2026-11-24 ~15:45 WIB, commit 316cbb7880412984142f3b239958d3e464d670fc): 4 passed (competition_open, snapshot 4 files / 5,743 bytes, license_osi MIT, entrypoint main.py → python3.13), 1 failed = `transcripts_present` (expected — transcript bundle is made at submit time), 14 skipped, 5 checks pending repo creation (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot).

## Submit (main agent, via browser)

- Create public repo `kiw33/u-mang-one-line-of-earned-pride-a0138557` (must be created AFTER opening 2026-11-24T04:15:54Z), push this commit, set GitHub About (homepage https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557, topic `makefun`), then submit with the transcript bundle before 2026-11-27T04:15:00Z.
- Suggested title: "One Line of Earned Pride"
