# Composite-odd quotient factor master

Date: 2026-07-29

Status: exact reduction and implementation audit, with unconditional raw
factor existence now supplied by the PBBS two-matching theorem.  Connectivity,
residence, safe opening, and compiler compatibility remain separate; no
`k=15` word is claimed.

## 1. Central freeness does not require primality

Let `k=2m+1` be any odd integer and let the cyclic group `Z_k` act by
translation on subsets of `Z_k`.

**Lemma.**  The action is free on ranks `m` and `m+1`.

**Proof.**  If a nonidentity translation fixes a subset, that subset is a
union of orbits of a subgroup of some order `t>1` dividing `k`.  Its size is
therefore divisible by `t`.  But

\[
 \gcd(k,m)=\gcd(2m+1,m)=1,
 \qquad
 \gcd(k,m+1)=1.
\]

No such `t` divides either central rank.  \(\square\)

Consequently each central layer has exactly

\[
 N={1\over k}\binom{k}{m}=\operatorname{Cat}(m)
\]

rotation orbits even when `k` is composite.  The old prime guard in
`scratch/sigma_sat_solver.py` was therefore stronger than the quotient
degree argument requires.

Shadow ranks need not be free.  At `k=15`, ranks six and nine have short
orbits.  This does not invalidate orbit-*coverage*: selecting one equivariant
witness covers the whole target orbit.  It only forbids treating an
unweighted quotient load at those ranks as a physical multiplicity.  The
master below uses central freeness for degrees and representative coverage
for shadows; `--no-cap2` avoids imposing a spurious shadow-load cap.

## 2. Exact factor master

Use the middle-levels incidence graph between rank `m` vertices `X` and rank
`m+1` vertices `T`.  At each `X`, choosing two of its `m+1` supersets is
equivalent to choosing a rank-`m+2` set

\[
 \sigma(X)=X\cup\{a,b\}.
\]

After quotienting by `Z_k`, introduce one Boolean variable for each pair

\[
 ([X],\{a,b\}).
\]

The exact constraints are:

1. choose exactly one pair at every rank-`m` orbit;
2. give every rank-`m+1` orbit weighted quotient degree exactly two (a
   quotient loop contributes twice);
3. cover every rank-`m+2` orbit by some selected `sigma(X)`;
4. for lower `q2`, cover every rank-`m-1` orbit by the intersection of the
   two selected rank-`m` neighbours at some middle vertex.

Binary solutions lift to equivariant physical 2-factors.  They have perfect
middle ownership and perfect lower `q1` automatically.  Conditions 3 and 4
are respectively complete upper `q1` and lower `q2`.  Connectivity, voltage,
residence, a safe opening, and the lower compiler remain separate audits; a
disconnected solution is still a valid decorated factor and becomes input to
the separate audited splice/fusion problem.  Section 4 gives one PBBS point
with complete deeper support as well, but arbitrary switches away from it
must re-audit those deeper shadows.

For `k=15`, the exact quotient sizes are

```text
central orbits per shore: 429
pair choices per lower orbit: C(8,2)=28
choice variables: 12,012
rank-9 target orbits: 335
rank-6 target orbits: 335
```

The current disconnected-factor CNF uses the exact grouped-neighbour
lower-q2 encoding audited below.  It has 36,465 variables, 243,913 clauses,
and is 3.9 MB in DIMACS form; it builds in about 0.25 seconds on the local
audit host.  The earlier expanded witness model had 670,511 variables and
2,067,129 clauses.  Quotient loops are legitimate weighted-degree-two factor
components and are now retained unless connectivity is explicitly encoded;
the default iterative driver removes them by lazy component cuts.

For a connected quotient cycle, the one-physical-cycle condition is
`gcd(voltage,k)=1`.  The former `voltage != 0` test was prime-specific and is
now corrected.  Full details, including physical multiplicities at the short
shadow orbits, are in
`AUDIT_SIGMA_COMPOSITE_QUOTIENT_SOUNDNESS_20260729.md`.

## 3. Composite calibration

The grouped-neighbour model was run at composite `k=9` with both upper `q1`
and lower `q2` required.  After one quotient subtour round it found a connected
coprime-voltage lift in 0.082 seconds total.  The literal decoded cycle has

```text
unique middle       126 / 126
unique lower q1     126 / 126
unique upper q1      84 / 84
unique lower q2      84 / 84
lift length         126
quotient voltage      4 mod 9
```

This is a positive end-to-end calibration of the composite quotient logic,
not a proof by testing.  The proof obligation is the freeness/coverage
separation in Sections 1--2; the calibration catches implementation errors.

The retained source is

```text
scratch/sigma_sat_solver.py
```

and the heavy `k=15` search runs only on the H100 host CPU.  Any positive
candidate must be copied back and independently replayed through the
repository factor auditor before it is used.

## 4. Unconditional PBBS solution of the raw master

Let `f` be the canonical PBBS permutation of the rank-`m` sets.  The two
incidence maps

\[
 M_+(A)=f(A)^c,\qquad M_-(A)=f^{-1}(A)^c
\]

are edge-disjoint perfect matchings between ranks `m` and `m+1`.  Put

\[
 \theta(A)=f^{-1}(A)\cap f(A).
\]

Their union is a spanning degree-two factor.  At a lower vertex `A`, its
upper-`q1` pair colour is `theta(A)^c`; at the upper vertex `A^c`, its two
lower neighbours intersect in `theta(A)`.  The audited PBBS first-shadow
theorem gives

\[
 1\le |\theta^{-1}(S)|\le3
 \qquad\left(S\in\binom{[k]}{m-1}\right).
\]

Thus both target shores are physically complete.  PBBS is rotation-
equivariant, so central freeness descends this factor to a binary solution of
constraints 1--4 for every odd `k`; short shadow orbits retain their actual
physical multiplicities.  At `k=15` the two quotient target histograms are
both

```text
load 1: 244 orbits
load 2:  88 orbits
load 3:   3 orbits
```

and the explicit factor selects two legitimate quotient-loop choices.  It is
therefore excluded by a loop-free model but satisfies the full loop-allowing
raw master.

More strongly, the audited all-depth PBBS path theorem and complementation
give complete correct-window support at every lower and upper depth of this
same factor.  The proof, exact indexing, component bound, and adversarial
scope audit are in

`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`.

Consequently the remaining `k=15` optimization is the intersection with
connectivity, coprime voltage, residence, safe opening, and the compiler—not
raw upper-`q1`/lower-`q2` feasibility.
