# Audit of Claude's recent equivariant-construction update

Date: 2026-07-29  
Audited source: `/Users/amir.nuriyev/Downloads/opusproblem/work`  
Newest source mtime in the snapshot: 2026-07-29 03:01:01 (`punchdeep.py`)

## Bottom line

The update contains real theorem-level and computational progress, but it does
not solve `k=15`, and its headline that only decorated-carrier existence
remains is too strong.

The reusable advances are:

1. the central rotation action is free for every odd `k=2m+1`, including
   composite `k=15`;
2. Merino--Micka--Mutze supplies an undecorated strict voltage spiral with a
   perfect first lower shadow for every odd `k` and every unit voltage;
3. the corrected lower-`q2`, upper-`q2`, and singleton motif catalogues agree
   with brute-force enumeration at small `k`;
4. the quotient CEGAR pipeline independently regenerates an optimal `k=11`
   carrier and, after the repository's exact compiler, a fully verified
   length-465 word.

The missing theorem is stronger than decoration.  It is the existence of a
**compiler-ready decorated pair** `(T,C)` consisting of

- a resident, shadow-complete strict spiral `T`;
- an exact one-core `C <= P(T)` satisfying `DC=DP`;
- exact weighted quotient Hall, followed by a physical matching; and
- a safe linear cut.

Decoration alone does not imply the one-core/Hall conditions.

The rigorous numerical frontier remains

```text
6438 <= nu(15) <= 6458.
```

No recent Claude run has emitted a new `k=15` carrier or word.

## Frozen snapshot

Important source hashes:

```text
6d63a707...  GENERAL_CONSTRUCTION.md
f469cd579...  LEDGER.md
fed3719c5...  cpsat.py
5f5813cd8...  ready15.py
738df9dee...  punchdeep.py
dc47e46ab...  construct.py
22c1358b0...  k11_final.word
011a32e8b...  k13_flat.word
```

The upstream directory is not version-controlled, so claims should be tied to
these hashes rather than mutable filenames.

## What verifies positively

### 1. Odd-composite quotient freeness

For odd `k=2m+1`, a nontrivial stabilizer orbit length `t | k` fixing a set of
rank `m` or `m+1` would force `t` to divide `2 rank-k`, which is `-1` or `1`.
Thus both central layers are free under rotation, even when `k` is composite.
Consequently

```text
W = k Catalan(m)
```

and the `k=15` central quotient really has `429` vertices in each layer.  The
old prime-only restriction was artificial.

### 2. The MMM undecorated strict spiral

The Merino--Micka--Mutze rotational middle-levels theorem projects to a
Johnson Hamilton cycle with perfect lower-`q1` rainbow and prescribed unit
voltage.  This closes the undecorated quotient base for every odd `k`.

It does **not** supply residence, deeper lower shadows, upper shadows, a
one-core, or Hall compatibility.

The exact canonical `k=15` audit gives, for shifts 1 and 4 alike,

```text
minimum cyclic run       2       (need 4)
missing lower q2       550
missing lower q3       528
missing upper masks   1338
```

so changing the unit shift does not decorate the canonical spiral.

There is also a direct conjugacy explanation.  For every unit
`a in Z_k^*`, the coordinate multiplier `phi_a(x)=a x` satisfies

```text
phi_a rho = rho^a phi_a.
```

Thus applying `phi_a` to any voltage-one spiral produces a voltage-`a`
spiral with exactly the same residence and shadow statistics.  Exploring
unit voltage by coordinate relabelling alone is therefore redundant.  This
does not say that every independently chosen MMM gluing tree of voltage `a`
is isomorphic; it scopes the redundancy to the multiplier-conjugate family.

### 3. Independent `k=11` calibration

Claude's fresh quotient route produced `k11_final.word`, and the repository's
literal verifier reports

```text
length                 465
covered masks         2047/2047
middle row exact       true
status                 VERIFIED_OPTIMAL
SHA-256                22c1358b0cb82d86cd13d0877cdfc4c847be14bc27c0ee5c2866ed35f6237688
```

The repository's independent exact compiler applied to Claude's fresh carrier
also gives a distinct verified optimum,
`scratch/claude_k11_cpsat3_repo_compile.word`, with SHA-256
`317db8aec07b190f5b0c31536abb705139e56b0d262c755698dda1534341d80f`.

This is strong validation of the compact quotient search model at `d=3`.

## The decisive compiler error

`ready15.py` lines 165--203 defines

```python
M_i = (P_i \ P_{i-1}) union (P_i \ P_{i+1})
```

and tests Hall using `M_i <= S <= P_i`.  But the graded compiler theorem
requires a fixed one-core `C` with

```text
C <= P,    DC = DP.
```

The forced-port mask `M` need not satisfy `DM=DP`.  On Claude's own fresh
`k=11` carrier, `ready15.py` prints `READY`, yet an independent audit finds

```text
DM != DP on 330 of 462 cyclic edges.
```

Artifact:
`scratch/claude_k11_ready15_forced_ports.audit.json`.

Therefore `READY` is only a relaxed positive-degree/Hall screen.  It is not a
sufficient compiler certificate.  This invalidates the claim in
`GENERAL_CONSTRUCTION.md` that decorated-carrier existence is the only open
odd-`k` statement.

The repository-owned exact boundary is
`scratch/graded_quotient_pipeline.py::make_equivariant_core`, followed by
weighted quotient Hall, a physical matching, literal word emission, and full
interval-OR verification.

## Other corrections

1. `GENERAL_CONSTRUCTION.md` and `LEDGER.md` state `nu(15) <= 6459`.  The
   current verified bound is `nu(15) <= 6458`.
2. The stored `k13_flat.word` has an exact rank-seven `D^3` row, but its
   cyclic closure has one non-Johnson seam of symmetric-difference size four.
   It does not prove a strict decorated `k=13` voltage spiral.
3. `construct.py` is not a proved deterministic polynomial-time algorithm:
   its fallback is unrestricted recursive backtracking, and no theorem says
   every decorated carrier passes its matching.
4. `punchdeep.py` describes iterative CEGAR but performs one solve and one
   final verification.  On the motivating saved `k=9` carrier it returns
   `deep CSP: UNSAT`; it does not reproduce the known optimum.
5. Several drivers are specialized to depth three despite general-`k`
   wording.  Their `q2/q3` dispatch should not be treated as an all-`d`
   theorem.
6. In the Claude logs, `PASS`/`FULLPASS` means the requested shadow gates
   passed.  It does not mean a word was compiled and exhaustively verified.
7. A cyclic quotient compiler has `W` distinct physical positions.  The
   appended `d` letters in a linear word duplicate the opening cells; they do
   not create `W+d` independent cyclic assignment positions.

## Live-search status at audit time

The H100 CPU currently runs:

- seeded `k=15` quotient CP-SAT (`cpsat.py 15 ...`), still before its first
  reported feasible round;
- `k=13` quotient CP-SAT, likewise with no result yet;
- a `k=13` Kissat portfolio; and
- independent exact `k=15` compiler-plus-19-suffix jobs from the main
  repository.

None has yet changed the rigorous bound.

## Integration decision

Adopt immediately:

- odd-composite central freeness;
- the MMM strict-spiral base theorem;
- the corrected motif generators;
- the compact quotient CP-SAT/CEGAR carrier search; and
- the independently verified `k=11` regression.

Do not adopt as theorem or certificate:

- `ready15.py`'s `READY` result;
- the claim that decoration is the sole remaining gate;
- `punchdeep.py` as a finished deep-punch compiler;
- a strict decorated `k=13` claim; or
- `PASS/FULLPASS` as a word-level success.

The right unified search target is a compiler-ready decorated pair `(T,C)`,
or a Benders loop that alternates compact carrier selection with exact
one-core/Hall counterexamples.  That is the strongest useful synthesis of
Claude's quotient work and the repository's exact compiler theory.
