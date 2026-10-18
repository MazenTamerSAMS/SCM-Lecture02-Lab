# Developer A / Developer B collaboration exercise

The original package contains the actual local bare remote and both working copies under `collaboration/`. Run the task from those local folders to reproduce the push/pull workflow. Captured command outputs are in `../evidence/`.

Expected flow:
1. Add a note to Developer A's README.
2. Commit locally in A.
3. Verify the line is not yet present in B.
4. Push A's main branch to origin.
5. Pull origin/main in B.
6. Verify the line is now present in B.

A commit alone changes only the local repository. Push transfers the commit to the remote; pull fetches and integrates it into the other clone.
