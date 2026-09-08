# Audit of Claude's late c-space update and the `k=15` nine-cycle pivot

Date: 2026-07-29

Audited mutable source:

```text
/Users/amir.nuriyev/Downloads/opusproblem/work
```

Frozen source hashes at the audit time:

```text
a548ed88f5249296a3a7e46483951cb76f9a33c7b93ce874c8bbc54d46282a84  LEDGER.md
c904137c6b0d07407f9df768e59eb02109215b825ec8ddd6fd5a84712af12890  GENERAL_CONSTRUCTION.md
006fe8ef2600491518b82a075a5d9c27e751f73b0bc30af1c0c1dd611256b452  cword.py
977854c6a5dc7ae81574915eb8e2cd81336548adf1fb594dcc635dbeace50dfa  sandwich2.py
```

## What is genuinely reusable

Claude's strongest new contribution is the **single-trace c-space reduction**
for a connected strict unit-voltage spiral.  In that chart the physical
carrier is determined by one cyclic binary trace `c`; class sums fix the
rank, run-start and run-end transversals encode Johnson seams, cyclic
one-runs encode residence, and middle/q1 orbit collisions are relational
inequalities between quotient columns.  The associated gap algebra reduces
the deeper decorations to consecutive end-drops and prefix start-unions.

This is a real collapse of the strict-spiral search to a pair of
permutations plus run lengths.  The `k=7` census and the independently
verified `k=9` and `k=11` regressions are useful positive calibrations.
Positive `PASS` outputs of the current capped-selector CEGAR remain sound;
capped-cover `UNSAT` is correctly treated as inconclusive and covers are
dropped before any sound-cut-only infeasibility claim.

The scope must remain explicit: c-space parametrizes **strict connected
spirals**, not all optimal carriers.  In particular, the known `k=13`
optimum arose from a multi-cycle factor followed by a splice.

## Corrections to the headline

1. The rigorous numerical frontier is

   ```text
   6438 <= nu(15) <= 6458,
   ```

   not the `6459` recorded in Claude's ledger.

2. `sandwich2.py` is an exact SAT formulation and a powerful tested
   compiler.  The successful finite regressions do not prove that every
   decorated carrier compiles.  A fixed carrier still needs an exact core,
   Hall feasibility, a safe opening, word emission, and literal verification.

3. A voltage spiral is without loss only **inside the strict-spiral chart**.
   It is not WLOG for the original word problem or for multi-cycle factors.

4. Claude's latest `k=15` round is not globally closer than its seed.  The
   seed has `(mid,q1,q2,upper)=(0,0,47,95)`.  The newest recorded round has
   `(34,42,44,85)`: it improves the last two decks while breaking 76 formerly
   exact central orbits.  The window LNS stayed at score `142` through 375
   iterations.  No `k=15` `PASS` artifact exists in the audited folder.

5. At audit time none of Claude's `cword.py`/`cpsat.py` lanes was still an
   active H100 process.  The latest files are useful search states, not an
   overnight convergence certificate.  The `k=13` lane likewise has no
   `PASS` or sound-cut-only `UNSAT` conclusion.

The probability estimates in `LEDGER.md` are judgments, not mathematical
outputs.

## Stronger repository result found during this audit

The fixed-`M0` PBBS fibre now contains an independently verified resident,
all-depth-complete `k=15` factor:

```text
physical cycles        9
cycle lengths          1890, 774^5, 555, 75, 45
minimum run            4
residence defects      0
lower/upper holes      0 at every audited depth
```

The candidate and audit are

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.engine.json
scratch/k15_fixed_matching_pbbs_resident_20260729/u2u3l3_s801.audit.json
```

with SHA-256 values

```text
886877094a3eaba8950136728d131782141a4b6f882d570ecb3791827da98f83
f2ab5b997199e788c1f18d2de2579020751020a35d8ef1394cb0b06a40494bd7
```

Fresh independent replay reproduced the audit byte for byte.  This result is
strictly stronger for the finite `k=15` endgame than Claude's current strict
spiral seed: all residence and shadow gates are already closed, at the price
of nine components rather than one.

The exact remaining problem is to open and concatenate the nine cycles using
eight seams and then pass the exact lower compiler.  The scalar lower-bound
slack is

```text
3*6435 + binom(4,2) - 16383 = 2928,
```

not `369`; affordability is ample, but it is not a Hall or shadow-safe-splice
proof.  The independent audit deliberately reports `compiler_eligible=false`
until a linear carrier is emitted.

## Integration decision

Keep Claude's c-space theorem, gap algebra, sound relational cuts, and small
`k` census as the best **connected strict-spiral** lane and as a candidate
general-theorem language.  For the immediate `k=15` proof, pivot priority to
the exact nine-cycle factor and the finite eight-seam/compiler problem.

No length-6438 word has yet been emitted, so the bound remains unchanged.
