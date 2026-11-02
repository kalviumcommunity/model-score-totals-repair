# Model Exam Question 2: Repair Student Score Totals

**Total: 30 marks | Submit one PDF**

## Problem statement

A small Python utility totals dummy student scores. First student is correct, but later totals wrongly include earlier scores. Reproduce failure, inspect the accumulator, establish a regression check, then fix and submit through a pull request.

Python logic matches practiced score-accumulator debugging. No web framework, database or third-party package. Use supplied inputs and contract, not guesses. Do not replace outputs with hard-coded answers.

## Before starting

Use Git Bash or Bash with Git on macOS/Linux, free GitHub account and a text editor. Sign in, configure Git author name/email and test push authentication before tasks. Do not expose tokens/passwords. No partner, paid tools or cloud services required. GitHub website is sufficient; GitHub CLI output is an accepted optional equivalent for real PR evidence.

Create your own repository with the template link below, then clone YOUR repository and enter its folder. Wait until starter files appear on GitHub before cloning. Do not push to shared instructor starter. Resolve authentication/setup problems before starting. Preparation is not graded. Instructor private reference repositories are not student forks or peer-reviewed production projects.

## Starter and setup

https://github.com/kalviumcommunity/model-score-totals-repair

Select **Use this template > Create a new repository**, choose your account and public visibility. Default branch only is sufficient. Clone your own copy and start on main. Python 3.10+ must already run. Commands below use `python`; if your Python 3 launcher is `python3`, substitute it consistently. Verify `python --version` before tasks. No pip, venv or package install needed because project uses standard library only.

Files: `app.py` (caller), `scores.py` (calculation), `checks.py` (existing checks), `regression_check.py` (assertion skeleton), `README.md` (this question), `RUNBOOK.md` (editable reproduction/check instructions).

## Required behaviour

`total_scores(students)` takes a list of score lists and returns one independent sum for each student, preserving order. Empty student list totals zero; empty outer list returns empty list. Inputs must not be changed. Only supplied integer-score scope required.

| Input | Correct output |
|---|---|
| `[[10, 20], [5, 5]]` | `[30, 10]` |
| `[[7, 3]]` | `[10]` |
| `[]` | `[]` |
| `[[], [4]]` | `[0, 4]` |

## Task 1: Inspect and reproduce

1. On initial main show `pwd`, `python --version`, `ls` and `git status` (clean).
2. Read `RUNBOOK.md`, then run `python app.py` before editing. App prints input, expected and actual totals.
3. In PDF record supplied paired input, expected result and actual observed result. Do not change app.py or expected values.

Evidence: environment/files, clean initial state, original run output and expected-versus-actual record.

## Task 2: Locate and explain

1. Create fix branch now: `git switch -c fix/student-totals`. Keep this branch through Tasks 2-4.
2. Locate relevant code using:
   ```bash
   find . -name '*.py' -not -path './.git/*'
   grep -n 'total_scores' app.py scores.py
   grep -n 'total' scores.py
   ```
   Read scores.py. Equivalent taught editor search accepted if paths/line references shown.
3. Inside outer `for marks in students:` loop, temporarily add this line immediately before inner loop, with same indentation as inner `for`:
   ```python
   print("ENTRY", marks, "total", total)
   ```
4. Run `python app.py` again. Record total entering second student and explain why it should have started at zero. Remove temporary print after screenshot, before regression/final commit. Do not fix accumulation yet.

Evidence: branch, file search/source, diagnostic print/output and one or two sentences connecting misplaced accumulator initialization to wrong second total.

## Task 3: Prove a regression check catches the bug

1. Run `python checks.py` unchanged and record result. These existing checks cover single/empty cases, not multiple students.
2. In `regression_check.py`, replace only `expected = None` with `expected = [30, 10]`, from contract above. Keep assertion and function call intact.
3. Before fixing scores.py run `python regression_check.py`. Capture real `AssertionError` showing observed wrong totals versus expected totals. Do not change expected values to make faulty code pass.

Evidence: unchanged existing-check execution, completed regression source and actual failing regression output. Existing checks may pass while new regression fails; explain this coverage gap in one sentence.

## Task 4: Fix, validate and open a pull request

1. On same fix branch, make focused correction in scores.py: each student must start with fresh total zero. Move existing `total = 0` into outer loop before inner loop; do not rewrite other logic or hard-code answers. Final file must have no temporary diagnostic print.
2. Run `python app.py`, `python checks.py` and `python regression_check.py`. All must now meet expectations. checks.py verifies single student, empty outer list, empty student and input preservation; it checks reversed-order structure but not reversed totals. New regression verifies paired and reversed totals. Keep all checks/expectations unchanged except requested skeleton completion.
3. In RUNBOOK.md replace final TODO line with actual problem, cause, fix, commands you ran and one honest limit (for example, non-integer input not tested). Keep original run/check commands. No need to edit question README.
4. Show `git diff`, stage only scores.py, regression_check.py and RUNBOOK.md, then show `git diff --staged` and `git status`. Commit using meaningful message, show clean status, push `git push -u origin fix/student-totals`.
5. Open PR from fix/student-totals into YOUR main. Description must state reproduction, cause, focused fix, actual check results and testing limit. Capture actual open PR title, description and branch direction. Leave PR open for review; merge and second reviewer not required.

Evidence: focused branch-based patch without diagnostics, actual app/existing/regression outputs, accurate RUNBOOK update, staged diff/status, commit/clean status/push and open PR. Working checks support listed inputs, not a claim of universal correctness.

## Submission

Submit one PDF for this question, with four task headings and labelled genuine screenshots plus requested short answers. Multiple readable screenshots allowed. Capture intermediate states before continuing. No separate URL submission, video, code archive, specific PDF filename or layout required. Evidence must show actual commands/results or actual GitHub states. Never fabricate output. Do not include personal credentials.

Only explicit task work is graded. Give partial credit within criteria, with no duplicate deductions or automatic whole-question zero. No presentation, identity, repository-name, metadata or screenshot-count marks. Equivalent correct commands and ordinary OS/path/hash differences accepted. Exact required file content and branch direction remain technical requirements. No second reviewer or self-approval required.

## Rubric

| Task | Explicit criteria | Marks |
|---|---|---:|
| 1 | Environment/files/clean main inspected (2); genuine original app run (2); correct paired input/expected/observed record (2) | 6 |
| 2 | Fix branch and relevant search/source evidence (2); targeted temporary diagnostic with actual output (2); cause linked to observed incoming second-student total (3) | 7 |
| 3 | Existing checks run unchanged (2); correct executed regression assertion and source (3); real pre-fix failure plus coverage-gap explanation (2) | 7 |
| 4 | Focused branch-based accumulator fix with no diagnostics (3); all specified app/existing/regression checks pass without weakened expectations (3); accurate RUNBOOK with commands and limit (1); staged review/meaningful commit/clean status/push (1); open PR with direction and requested explanation/results/limit (2) | 10 |
| **Total** | | **30** |
