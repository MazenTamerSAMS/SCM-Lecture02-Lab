# Software Configuration Management — Lab Report

**Student:** Mazen Tamer  
**Repository:** SCM-Lecture02-Lab  
**Project:** Inventory Management System

## Task 1 — Repository inspection

The starter repository was on `main` and contained two feature branches: `feature-search` and `feature-stock-validation`. The latest initial commit on main was `Add project changelog`.

1. A centralized VCS stores the authoritative history on a central server, while a distributed VCS gives each clone its own repository history.
2. A distributed VCS allows local commits, history inspection, and branching without a live connection to the remote. Network access is needed to exchange changes.
3. A feature branch isolates work so a feature can be developed and tested without immediately changing the main line.

## Task 2 — Branching, merging, and conflict resolution

The search branch was merged first. Merging the stock-validation branch then produced a conflict in `version.txt`, because each branch changed the same line to a different version label. Git could not infer which value represented the intended release. The conflict was resolved as:

```text
Version: 2.0
```

Both feature files, `src/search.py` and `src/stock_validation.py`, are included in the completed project. The supplied starter repository archive contains the original local Git history; captured conflict evidence is also recorded under `evidence/` in this GitHub repository.

## Task 3 — Defect investigation

- **File/function:** `src/inventory.py`, `stock_is_valid(quantity)`
- **Introducing commit:** `d1d5c34` — `Adjust stock validation behavior`
- **Defect:** Negative quantities were incorrectly accepted.
- **Expected behavior:** Zero and positive quantities are valid; negative quantities are rejected.
- **Fix:** Removed the erroneous special case and kept `return quantity >= 0`.
- **Verification:** `python test_inventory.py` passes for positive, zero, and negative stock.

The original defective commit is preserved in history; the correction is a new commit.

## Task 4 — Diff algorithms

The supplied v1/v2 samples were compared using Myers, Minimal, Patience, and Histogram. For these short examples, all four outputs show the same essential changes: adding `validateUser()`, changing `stock == 0` to `stock <= 0`, and adding `logTransaction()`. Therefore, no meaningful readability ranking can be inferred from these particular outputs alone. In a larger file with repeated lines, Patience and Histogram can sometimes produce easier-to-follow alignments, while Minimal may spend more effort finding a smaller diff.

## Task 5 — Distributed collaboration

Developer A added a short note to `README.md` and committed it locally. Developer B did not see that change before the push. After Developer A pushed to the shared remote and Developer B pulled, the new line appeared in B. A local commit updates only that clone; push publishes commits to the remote, and pull fetches and integrates remote changes.

## Task 6 — Hashing and SSH

1. A commit's short hash is the abbreviated form of its object ID. A new commit normally has a different hash because its content and/or metadata and parent reference differ.
2. One hexadecimal digit represents four bits. Thus 160 bits / 4 = 40 hexadecimal digits.
3. Git hashes identify objects and help detect content changes; commit IDs also connect the history graph.
4. The public SSH key may be shared with a hosting service.
5. The private key must remain secret because possession of it can allow an attacker to authenticate as its owner.

## Task 7 — Reflection (171 words)

Software configuration management helps a team control how software changes over time. Git history records what changed and when, so developers can investigate defects and understand why a behavior appeared. Commits provide small, identifiable checkpoints that can be reviewed or compared with earlier versions. Branches allow different features to be developed independently, reducing the chance that unfinished work disrupts the main version. Merging brings completed changes together, while conflict resolution requires the team to make an explicit decision when two edits cannot safely be combined automatically. A distributed repository makes local work possible even when the remote server is unavailable; developers can inspect history, create branches, and commit changes locally. Push and pull then synchronize work through a shared remote repository. Hashing gives Git identifiers for repository objects and helps reveal when content changes. SSH keys support secure authentication to remote services: the public key can be registered with the service, while the private key stays secret. Together, these practices improve traceability, collaboration, integrity, and confidence that the project being tested and delivered matches the intended configuration.

## Evidence and reproducibility

Command output is stored under `evidence/`, and the original Git repository is included in `SCM_Lab_Completed_Files.zip`. The assignment requests screenshots from the student's own working copy; use the included command outputs as a checklist and capture genuine local screenshots before submission.
