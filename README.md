# SCM Lecture 02 Lab

Software Configuration Management assignment covering Git inspection, branching and merging, conflict resolution, defect investigation, diff algorithms, distributed collaboration, hashing, and SSH.

## Repository contents

- [REPORT.md](REPORT.md) — complete written report and 171-word reflection.
- `student-repo/` — inventory project source, tests, diff samples, and resolved version file.
- `evidence/` — captured command outputs for conflict resolution, tests, diff comparisons, and collaboration.
- `collaboration/` — notes describing the Developer A / Developer B exercise.

## Verify the fix

From the repository root:

```bash
cd student-repo
python test_inventory.py
```

Expected output:

```text
PASS: positive stock is valid
PASS: zero stock is valid
PASS: negative stock must be rejected
```

## Important submission note

The original starter archives contain the full local Git history and the actual `collaboration/remote.git` bare repository. The text evidence and completed source are also represented here, but the assignment asks for genuine screenshots from the student's own local working copy. Capture those screenshots before submitting.
