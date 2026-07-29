# Audit of the disjoint-surgery set-cover ILP

Date: 2026-07-29

Status: corrected/unsupported verdict.  Claude's current `movecover.py`
`OPTIMUM=0` claim is not a proof-safe no-go.  A corrected high-arity master
remains potentially nonempty.  This audit uses no new heavy solve.

## 1. Audited source and verdict

The live source is

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/movecover.py
SHA-256 9d46ad8f3c0b4fbb8cdd2d280581901212c9854f1c2d31f5bfab64f50e62ef97
```

and the frozen run-transversal seed has SHA-256

```text
7dd31950ffd69eea819d5ea413feb66f1d32bc1d88fe206a2b11faf26c1fd332.
```

The ledger assertion that no pairwise-disjoint family of single surgeries
can improve the `142` missing q2/upper orbits is unsupported for four
independent reasons:

1. arbitrary-width upper load deltas are truncated incorrectly;
2. catalytic moves are pruned before the IP;
3. simultaneous normal-form legality is not imposed; and
4. the active-single catalogue omits primitive moves legal only in
   combination.

No retained solver assignment, optimum proof, or independent replay binds
the old `OPTIMUM=0` line.

## 2. Exact additive theorem

Fix a structurally legal binary trace `c`.  For a proposed surgery `g`, let

* `(u^g,v^g)` be its lifted start/end displacement;
* `delta^g_p=c^g_p-c_p` be its literal bit effect;
* `A_g` be the quotient middle-column support;
* `H_g^(q)=union_(t=0)^q(A_g-t)` be its depth-`q` chronology halo; and
* `Sigma(g)=(Delta M_g,Delta Q_g)` be its signed middle/q1 orbit
  signature.

### Theorem 2.1 (disjoint-halo additivity)

Let `X` be a family of surgeries such that:

1. their literal effects commute and
   `c_X=c+sum_(g in X)delta^g` is binary;
2. their start/end actions are shore-compatible;
3. their combined displacement satisfies

   \[
   \ell_i+\sum_{g\in X}(v^g_i-u^g_i)\ge d+1,                 \tag{2.1}
   \]

   \[
   g_i+\sum_{g\in X}(u^g_{i+1}-v^g_i)\ge1                  \tag{2.2}
   \]

   at every run, together with the exact endpoint-permutation and winding
   equations; and
4. the q1 halos `H_g^(1)` are pairwise disjoint.

Then the final middle/q1 signature is additive:

\[
 \Delta M_X=\sum_{g\in X}\Delta M_g,
 \qquad
 \Delta Q_X=\sum_{g\in X}\Delta Q_g.                        \tag{2.3}
\]

At a middle/q1-perfect seed, the final trace remains perfect if and only if

\[
                         \boxed{\sum_{g\in X}\Sigma(g)=0.}   \tag{2.4}
\]

#### Proof

Disjoint q1 halos ensure that no middle column or adjacent-intersection
position sees two surgeries, so the literal signed differences telescope.
Equations (2.1)--(2.2) and the endpoint equations are exactly the
run-transversal normal form.  Since every initial middle and q1 orbit has
load one, retaining all loads is equivalent to zero signed difference.
`square`

For lower depth `q`, the analogous isolated-load formula requires
pairwise-disjoint `H_g^(q)`, or a direct replay of the combined trace.

## 3. Decisive upper-oracle defect

The source sets

```text
REACH = maximum number of strict union increases from one start + 2.
```

For the frozen `k=15` seed this gives `REACH=10`, but the exact distance to
the first full union is as large as `44`.  Number of newly arriving
coordinates and chronological span are different quantities.

There is a literal witness.  The legal start surgery

```text
S(a=7, delta=3, partner=327)
```

changes quotient columns `127,128,129`.  It also changes the rank-13 upper
flag beginning at start `116` from canonical value

```text
14335 -> 16255.
```

Start `116` is outside the ten-class recomputation window, so the stored
upper delta omits this change.  The source additionally counts `FULL` once
when it is first reached and a second time after the loop.  The latter does
not change Boolean coverage of `FULL`, but it makes the advertised load
vector inexact.

## 4. Why q1-disjointness does not linearize arbitrary upper intervals

Let an upper target have omission size three.  On five consecutive Johnson
columns, take omitted triples

\[
                 abc,\ abd,\ abe,\ abg,\ abf.                \tag{4.1}
\]

Perform two commuting changes:

\[
 abd\mapsto bce,
 \qquad
 abg\mapsto aef.                                            \tag{4.2}
\]

Every old and new adjacent pair shares exactly two omitted coordinates, so
all four traces remain Johnson.  The two changed-column q1 halos are
disjoint.  Nevertheless the intersection of omissions over the displayed
interval is

\[
\begin{array}{c|c}
\text{state}&\text{intersection}\\ \hline
\text{baseline}&\{a,b\}\\
\text{first only}&\{b\}\\
\text{second only}&\{a\}\\
\text{both}&\varnothing.
\end{array}                                                  \tag{4.3}
\]

Thus neither isolated surgery covers the upper target, while the pair does.
Arbitrary-width upper coverage has a genuine mixed term even for commuting,
q1-halo-disjoint Johnson surgeries.  Summing precomputed single-move upper
deltas cannot be exact.

## 5. Other completeness defects

### 5.1 Catalysts are pruned

The code retains only moves which individually gain a currently missing
q2/upper orbit.  This can delete a necessary deck-recycling catalyst.  In
the simplest signed model,

\[
 \Delta g=-e_A+e_B,
 \qquad
 \Delta h=e_A,                                             \tag{5.1}
\]

where `A` is initially covered and `B` is missing.  The pair `g+h` repairs
`B` without losing `A`, but `h` is discarded by the current filter.

### 5.2 Individual legality is not simultaneous legality

A start surgery and an end surgery can each legally shorten opposite ends
of the same run while their sum violates (2.1).  The present IP applies
single-move legality tests but contains no combined run/gap resource rows.

### 5.3 The catalogue is not the full move fibre

The columns are individually legal start/end transpositions.  A balanced
endpoint circulation may be legal only when all of its displacements are
applied together.  Hence an optimum over the active-single catalogue is not
a no-go for the complete normal-form fibre.

## 6. Proof-safe replacement master

Retain every primitive surgery column and use binary variables `x_g`.
Impose:

1. q1-halo packing

   \[
   \sum_{g:j\in H_g^{(1)}}x_g\le1;                          \tag{6.1}
   \]

2. literal support and endpoint compatibility;
3. the combined normal-form rows (2.1)--(2.2), endpoint transversality, and
   winding;
4. exact zero middle/q1 signature

   \[
   \sum_g\Delta M_g(O)x_g=0,
   \qquad
   \sum_g\Delta Q_g(O)x_g=0                                \tag{6.2}
   \]

   for every orbit `O`; and
5. either depth-`q` halo packing or direct combined replay for every lower
   layer.

Upper coverage must be encoded from the final trace, not from isolated
deltas.  Two exact choices are available.

* Use the contained-run recurrence for each target `S`, with

  \[
  b_i=[T_i\subseteq S],
  \qquad
  q_{i,x}=\neg b_i\vee(q_{i-1,x}\wedge\neg[x\in T_i]);       \tag{6.3}
  \]

  coverage is the existence of an `S`-contained run which sees every
  coordinate of `S`.
* Use lazy Benders cuts: after an integral surgery selection misses `S`,
  substitute

  \[
                    c'_p=c_p+\sum_g\delta^g_p x_g           \tag{6.4}
  \]

  into the exact arbitrary-width run-blocker inequality and add the
  resulting valid cut.

Either route is proof-safe.  Neither asserts that the corrected progress
face is nonempty.

## 7. Exact scope of the existing negatives

The following finite facts remain valid.

* All `1,805` legal active singles worsen the frozen exact score, and no
  singleton is middle/q1-perfect.
* Pure start-only or end-only cycles through endpoint arity six do not
  improve the seed.
* All `808,084` combinations of one legal start-pair and one legal end-pair
  fail to improve it.
* The complete same-run-order support-at-most-three atlas has no
  middle/q1-perfect state.  In its additive signature formulation there is
  no zero singleton or opposite pair.
* In the `4,037`-column pure three-run-cycle catalogue, exact
  meet-in-the-middle checks exclude zero-signature bundles of cardinality
  one, two, and three.

These statements do **not** exclude:

* a three-or-more active-surgery bundle;
* a four-or-more bundle from the pure three-cycle catalogue;
* a primitive move legal only simultaneously; or
* an overlapping nonlinear surgery.

Therefore the corrected high-arity master is unresolved, not proved empty.
For the pure three-cycle catalogue, cardinality four is the first unclosed
bundle size.
