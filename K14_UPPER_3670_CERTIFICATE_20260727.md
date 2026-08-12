# Certified improvement: `nu(14) <= 3670`

Date: 2026-07-27

The file `scratch/k14_complete_3670_oneedit.word` is an exhaustive
certificate that

\[
                        \boxed{3434\le\nu(14)\le3670}.
\]

It consists of the 3,434-entry compiler-in-the-loop prefix
`scratch/k14_compilable_descent.word` followed by the 236-entry suffix
`scratch/k14_compilable_append236_oneedit.txt`.  Starting from the old
242-entry completion, six successive delete-one/edit-one repairs shortened
the suffix to 236 while retaining complete coverage.

The next repair in this restricted class is exhaustively absent: the
236-to-235 search examined 205 deletions that left exactly one hole and
48,536 exact one-entry repairs, none successful.  This is only a local
no-go for that repair class, not a lower bound on arbitrary completions.

Hashes:

```text
38d6480c4e7de290365b236b8af6b3ea80c2e8537f8a99e0a165fdb6eb9428a0  scratch/k14_complete_3670_oneedit.word
7a0ade7febb95d6be8e8da82932632b0713d62542fd667ef6424eee6da6daced  scratch/k14_compilable_append236_oneedit.txt
```

Run the independent exhaustive verifier with

```text
python3 scratch/verify_k14_completed_3670.py
```

It checks the hash, length, nonzero entry range, all 16,383 target masks, and
recomputes an explicit interval witness for every target.  Independent C++
full-array and suffix verifiers also pass.
