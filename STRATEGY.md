# STRATEGY — "One Word From Your Ex"

## Exact deliverable

- `/output/entry.txt` must contain **exactly one word**, encoded as UTF-8,
  **1–24 characters**, not whitespace-only, with **no trailing newline**.
- The grader refuses a mode-600 file (`tempfile.mkstemp` creates 0600): the
  temp file must be `os.chmod(0o644)` **before** `os.replace`, and the final
  mode must be verified as `0644`.
- `/output` must hold **only** `entry.txt`.
- Entrypoint: `main.py` at the repository root (python3.13 runtime, stdlib
  only, no network, well under the 60 s wall budget). It writes the artifact
  atomically (temp in `/output` → `os.replace`) and verifies bytes, UTF-8,
  char count, single-token shape and mode.
- Keep the makefun root freshness commit and the LICENSE commit intact;
  commit all work after the second write to `main.py`.

## Scoring and judge criteria, in the rubric's order

The house judge (GLM-5.3-flash), reads two entries at a time, both orders,
and picks the funnier / more painfully honest word with a margin 1–5.
Games are scored 0.6–1.0 for the winner; a Bradley-Terry fit gives the
published Judge win rate. Top 500 on the dev board reach the final heat;
top 3 play a playoff; **1st place takes $2**.

The criteria are applied **in this order**, first difference deciding:

1. **Exactly one word an ex would use about a partner** — a real, natural
   word; any phrase, sentence or off-topic text loses to any single word.
2. **Makes me laugh out loud** — surprise, a sharp turn, a word that lands
   harder than expected.
3. **Stings with recognition** — painfully true, and the entrant plainly
   knows it. A true sting beats a plain insult; meanness for its own sake
   does not count.
4. **Lands instantly** — needs no explanation and cannot be swapped for a
   near synonym without losing its edge.
5. **Feels relatable** — the kind of word people repeat because it names
   something they lived through too.

## Hard caps

- 1–24 characters; UTF-8; one non-whitespace token; no trailing newline.
- Final file mode 0644; `/output` containing only the artifact.
- Program: 1 CPU, 512 MB, 64 PIDs, 60 s, no network, everything it runs in
  the repository at the submitted commit.
- Self-deprecation required; judge-directed text would violate criterion 1
  (highest priority), so the artifact is a bare word.
- 500-contender cut; byte-identical entries share a rate and earlier receipt
  wins an exact tie, so an original word with few bytes is safest.

## Plan to maximize the score

1. **Word choice: `Placeholder`** (11 bytes). It clears criterion 1 as a
   single, real word people actually use about a former partner ("I was just
   a placeholder"). It wins criterion 2 by the sharp, almost clinical turn:
   a whole person reduced to a temporary blank to be filled. It wins
   criterion 3 because the sting is true and self-owned: *I was never
   actually chosen*. It wins criterion 4 because "stand-in", "backup" or
   "interim" lose the cold, modern edge. It wins criterion 5 because nearly
   everyone recognises being someone's temporary option. Generic insults
   ("needy", "clingy", "dramatic") pass criterion 1 but lose on 2 and 4.
2. **Freshness.** The public feed at
   `https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2`
   was read; blind rounds are active (`judged: 0`, hidden board, no texts
   published). With no rival wording available, the word was chosen from the
   rubric alone and does not copy or duplicate any rival entry or house text.
3. **Rule-compliant writer.** `main.py` validates the word before writing,
   writes via a temp file in `/output`, chmods to 0644 before `os.replace`,
   removes stray files from `/output`, and verifies the exact bytes and mode.
4. **Transcript discipline.** Quote the exact `makefun anchor ... round ...`
   line before the first counted write; write `main.py`, then in a separate
   later step rewrite that same entrypoint with a stronger rule-compliant
   version, so the transcript shows two distinct writes to the final
   entrypoint. Validate locally, then commit everything with git.
