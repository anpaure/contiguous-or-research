# Thread D: unique-q1 Hall capacity and the r98/r99 row halo

**Date:** 2026-07-29  
**Scope:** solver-free audit of the frozen radius-98 and radius-99 cut fibres.

## 1. Frozen inputs

The source factor is
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`, SHA-256

```text
d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8
```

The palette-safe option certificate has SHA-256
`0df79758045e816e2c4545cd10f99b908309d63dc3e96a43715b370e446eb66e`;
the radius-99 graded cut-space certificate has SHA-256
`b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e`.
The quotient catalogue digest is
`e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

The new replay is
`scratch/audit_threadD_k16_r98_r99_pareto_row_halo_20260729.py`; its output
is `scratch/threadD_k16_r98_r99_pareto_row_halo_20260729.audit.json`.

## 2. Unique-provider Hall inequality

Let \(F\) be the frozen source factor, let \(C\subseteq F\) be the deleted
edge-orbits, and let \(A\) be the inserted loopless seam-orbits.  Put

\[
 |C|=|A|=r.
\]

For a lower q1 colour \(s\) having a unique provider \(e_s\in F\), define
\(s\) to be lost when \(e_s\in C\).  Define lost unique upper colours in the
same way.  Write their sets as \(L(C)\) and \(U(C)\).

**Lemma 2.1 (double-repair inequality).**  If the exchange is q1-complete,
then its inserted seams contain a subfamily \(D\) such that

1. every member of \(D\) covers one colour in \(L(C)\) and one colour in
   \(U(C)\);
2. no two members of \(D\) use the same lost lower colour or the same lost
   upper colour; and
3.

\[
 |D|\ge |L(C)|+|U(C)|-r.                 \tag{2.1}
\]

**Proof.**  Assign every lost lower and upper colour to one inserted seam
that provides it.  A seam receives at most one lower assignment and at most
one upper assignment.  If \(d\) seams receive both kinds of assignment, the
number of assigned colours is at most \(r+d\).  All
\(|L(C)|+|U(C)|\) colours are assigned, proving (2.1).  The doubly assigned
seams have distinct assigned lower and upper colours.  ∎

The scalar form is equivalently the valid weighted inequality

\[
 \sum_{e\in F} w(e)x_e
 \le r+\sum_{a\in E_{LU}}z_a,            \tag{2.2}
\]

where \(w(e)\in\{0,1,2\}\) is the number of palettes for which \(e\) is a
unique source provider, \(x_e\) is the cut indicator, and \(z_a\) marks a
seam assigned simultaneously to its unique-source lower and upper colours.

Degree preservation gives the additional necessary capacities

\[
 \sum_{a\ni v}z_a
 \le \sum_{e\in F:e\ni v}x_e             \tag{2.3}
\]

at every quotient node \(v\).  The colour assignments give

\[
 \sum_{a:\ell(a)=\ell(e)}z_a\le x_e,
 \qquad
 \sum_{a:u(a)=u(e)}z_a\le x_e.           \tag{2.4}
\]

These are Hall/capacity necessities, not a sufficient completion system.

## 3. Exact scalar demands

The existing component DP is exact because the 85 motif-overlap components
have disjoint source-edge supports and the exterior-cut budget is at most
two.  Its results are:

| face | minimum unique losses | required double repairs |
|---|---:|---:|
| r98 anchored internal product | 114 | 16 |
| r99, retain 22511 | 113 | 14 |
| r99, delete/replace 22511 | 111 | 12 |

For r99-retain, the lower/upper Pareto frontier is
((50,63),(51,62),\ldots,(63,50)).  For r99-delete, it contains
((49,62),(50,61),\ldots,(62,49)), together with ((64,48)).

## 4. Endpoint/colour capacity does not close the gate

The row-halo audit chooses, in each face, a canonical cut attaining the
minimum unique-provider loss.  It then greedily constructs and literally
replays inserted seam sets satisfying all of (2.3)--(2.4).  It checks:

- every displayed seam is loopless and off-source;
- both unique source providers of its two assigned colours are cut;
- assigned lower colours and assigned upper colours are separately distinct;
- at every node, displayed seam incidence is at most the cut incidence.

The exact outcomes are:

| face | colour-only maximum matching | replayed endpoint+colour packing | demand |
|---|---:|---:|---:|
| r98 | 38 | 21 | 16 |
| r99 retain | 51 | 21 | 14 |
| r99 delete | 50 | 21 | 12 |

Thus no inequality using only the current cut fibre, distinct lower/upper
unique colours, and aggregate endpoint capacities can upper-bound double
repairs below 16, 14, or 12 respectively.  In particular, optimizing the
current `--solve-capacity` relaxation cannot prove either r99 branch
infeasible: the audit already supplies a feasible objective-21 witness in
each branch.

This does **not** produce a q1 completion.  The missing coupling is that the
remaining 78 seams must simultaneously consume the residual endpoint
deficits and cover every residual q1 row.  That completion coupling is
precisely what the full r99 runs have not resolved.

## 5. Exact raw-row compression for r98 Stage A/B

Raw r98 row IDs below are exactly the Stage-A/B convention: lower then upper
in catalogue insertion order, omitting rows with a provider in the 468-edge
fixed exterior.  There are 649 rows, and row 486 is upper colour `(1,1907)`.

Among all r98 option-product cuts attaining the minimum loss 114:

- 52 unique q1 rows are lost in every such cut;
- 208 unique q1 rows can be lost in at least one such cut;
- the double-seam graph induced by those 208 rows has only 266 seam-orbits;
- the halo incident to the 52 mandatory rows has 104 seams on 117 quotient
  endpoint nodes.

The audit contains the full literal row/colour/provider records and a stable
priority list.  Its first entries are

```text
486, 262, 593, 41, 147, 157, 300, 352, 404, 625,
14, 449, 251, 576, 378, 63, 113, 215, 436, 122, ...
```

The ordering is: the anchor first; then mandatory, canonical, and merely
possible minimum-loss rows; within a class, increasing possible-opposite
double-seam degree, increasing provider count, and raw row ID.  This is a
proof-safe **search/core ordering**, not a replacement for omitted q1 rows.
A cut with loss greater than 114 can leave this 208-row halo.

## 6. Smallest exact remaining capacity subproblem

The smallest useful necessary subproblem has:

- 858 source cut bits \(x_e\), one locked-edge branch, cardinality 99, and
  the 147 current-motif hit rows;
- 20,787 double-seam bits \(z_a\), rather than all 26,570 insertion bits;
- 675 lower-colour and 673 upper-colour capacity rows (2.4);
- 858 endpoint rows (2.3);
- target `sum(z) >= 14` in retain and `sum(z) >= 12` in delete.

This model is sound and complete **as an upper-bound relaxation**: every
actual q1-complete radius-99 exchange induces a feasible \(z\) of at least
the target size.  Its converse is false.  The explicit objective-21
witnesses show that this relaxation is already too weak.

The next exact subproblem must therefore retain residual seam completion.
One minimal formulation keeps the \(z\) variables above and adds residual
insertion variables only in the endpoint/colour halo needed to complete the
remaining endpoint deficits and uncovered q1 rows. Equivalently, after a
candidate \((C,D)\) is fixed, solve the residual 0--1 degree-constrained,
two-palette edge-cover problem

\[
 \deg_{A\setminus D}(v)=\deg_C(v)-\deg_D(v)
\]

together with every still-uncovered lower and upper row.  Failure of that
residual problem yields a genuine endpoint-colour Hall shore; the aggregate
capacity model cannot.

## 7. Audit of the current capacity driver

`scratch/audit_k16_r98_r99_unique_q1_double_repair_20260729.py` (SHA-256
`df1a16bb30f4726312a0cea76debcff3c433979978b27b66fbb13a376eaa8bfa`)
correctly encodes (2.3)--(2.4), the exact branch cut space, and the proved
minimum-loss inequality.  Its negative implication is sound: a proved
optimum below the demand would exclude the branch.  The positive direction
is deliberately only diagnostic.

Before retaining any future optimization transcript as a certificate, the
driver should additionally record:

1. the serialized pre-solve proto and SHA-256;
2. driver, catalogue-module, source, option, and cut-space hashes;
3. OR-Tools version, exact command, host, workers, seed, and time limit;
4. `best_objective_bound` as well as incumbent objective;
5. literal replay of the selected cut, motif hits, branch bit, unique-loss
   weight, distinct colour assignments, and endpoint capacities.

An `UNKNOWN` status is not an exact negative certificate.  Even a numerical
best bound should be described as a trusted-solver bound unless accompanied
by a proof-checkable log.  Here no capacity run is needed because the
solver-free objective-21 witnesses settle the relaxation in the positive
direction.
