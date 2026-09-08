# Two-cycle Catalan fusion: exact hybrid clauses, a smallest lock, and the forest escape

Date: 2026-07-31  
Status: general exchange theorem and exact solver-free `m=2,3` audit; sharp
obstruction to degree-preserving fusion inside one two-cycle union; no
all-`m` Catalan Linear Matching theorem is claimed

## 0. Verdict

The lower-tight Hamilton cycle supplied by a tight enumeration and the
upper-tight Hamilton cycle supplied by Middle Levels cannot in general be
combined by merely choosing alternating-circuit states of their union.

There is an exact reason.  Given two oriented Hamilton cycles, their
degree-preserving successor hybrids form a Boolean cube indexed by the
cycles of one permutation.  For a fixed outer-colour perfect matching,
availability of all its diamonds is a signed CNF on that cube.  Thus the
fusion problem is a correlated matching--SAT problem, not an interpolation
between two scalar defect counts.

The obstruction is already sharp at `m=3`.

* A concrete Hamilton cycle `P` of `J(6,3)` obtained from the vendored
  GMM SatCycle implementation, and its complement `Q`, are both
  lower- and upper-complete with exact load profile `1^10 2^5` on both
  shores.
* Nevertheless every one of the `6272` spanning two-factors contained in
  `P union Q` has colour-incidence matching rank at most `14<15`.
  This includes `336` two-sided-rainbow factors and `176` two-sided-rainbow
  Hamilton cycles.
* Yet `P union Q` contains a `Cat_3=5`-path Catalan linear matching.  One
  such forest uses twelve edges of `P` and only three edges of `Q`.

So the failure is not lack of the required diamonds.  It is caused by the
extra requirement that the **unused** edges also complete a spanning
two-factor.  The correct fusion move is forest-first and asymmetric:
select the common outer-colour matching while allowing the complement to
have unmatched physical endpoints.  Full-cycle alternating switches are
strictly too coarse.

For `m=2`, all twelve double-rainbow Hamilton cycles of `J(4,2)` have a
common transversal.  Thus `m=3` is the first possible double-rainbow Hall
failure and the displayed lock is dimension-minimal.

## 1. Setup

Let `|Omega|=2m`, and put

\[
 {\cal L}=\binom\Omega{m-1},\qquad
 {\cal X}=\binom\Omega m,\qquad
 {\cal U}=\binom\Omega{m+1},
\]

\[
 K=\operatorname {Cat}_m,\qquad
 N=|{\cal L}|=|{\cal U}|=mK,\qquad
 M=|{\cal X}|=(m+1)K=N+K.                 \tag{1.1}
\]

Every Johnson edge `e=xy` has its two outer colours

\[
             \ell(e)=x\cap y,\qquad u(e)=x\cup y.   \tag{1.2}
\]

Equivalently it is the unique physical lift of the diamond
`(ell(e),u(e))` in the balanced inclusion graph `B_m` on
`cal L sqcup cal U`.

For a spanning two-factor `C` on `cal X`, let `G(C)` be the
occurrence-labelled bipartite graph with one edge

\[
                       \ell(e)---u(e)                 \tag{1.3}
\]

for every physical occurrence `e in E(C)`.  A perfect matching of `G(C)`
selects one occurrence of every lower and every upper colour.  If `C` is
one Hamilton cycle, the selected `N<M` physical edges form a spanning
linear forest with exactly `M-N=K` components.  This is the cycle-first
form of the Catalan Linear Matching assertion.

The literature gives the two projections separately.

* A GMM tight enumeration of levels `{m-1,m}` projects to a Hamilton cycle
  whose lower colours are complete.
* A Middle Levels Hamilton cycle projects dually to a Hamilton cycle whose
  upper colours are complete.

The question addressed here is what ordinary alternating-circuit fusion of
two such cycles can prove.

## 2. The canonical Boolean hybrid cube

Let `C_0,C_1` be oriented Hamilton cycles on the same vertex set
`cal X`, with successor permutations

\[
                         s_0,s_1\in S_{\cal X}.       \tag{2.1}
\]

We ask for every directed spanning two-factor whose outgoing arc at `x` is
one of

\[
                         x\to s_0(x),\qquad x\to s_1(x).       \tag{2.2}
\]

Put

\[
                         \pi=s_1^{-1}s_0.             \tag{2.3}
\]

### Theorem 2.1 (successor-orbit hybrid theorem)

Let `O_1,...,O_c` be the nontrivial orbits of `pi`; common arcs are regarded
as forced.  Every directed spanning two-factor satisfying (2.2) is obtained
by one binary choice on each orbit:

\[
 s_z(x)=
 \begin{cases}
 s_0(x),&x\in O_j, z_j=0,\\
 s_1(x),&x\in O_j, z_j=1.
 \end{cases}                                         \tag{2.4}
\]

Conversely every `z in {0,1}^c` defines a directed spanning two-factor.
Thus these hybrids form an exact `2^c` Boolean cube.

#### Proof

The two possible arcs entering the head `s_0(x)` are

\[
                  x\to s_0(x),\qquad
                  \pi(x)\to s_1(\pi(x))=s_0(x).     \tag{2.5}
\]

Exactly one must be chosen.  If `x` chooses its `s_0` arc, then `pi(x)`
cannot choose its `s_1` arc and hence also chooses `s_0`.  The same
implication in reverse shows that the choice is constant around every
`pi`-orbit.  Independent orbit choices give one outgoing and one incoming
arc at every vertex, proving the converse. \(\square\)

This is the canonical alternating-circuit decomposition of the two
successor perfect matchings in the tail-copy/head-copy bipartite graph.
It is orientation-sensitive; both orientations of `C_1` must be audited.

## 3. Exact signed availability clauses

Fix an outer diamond `d=(L,U) in E(B_m)`.  For each orbit `O_j`, record
whether the corresponding physical edge occurs among the `C_0` arcs or the
`C_1` arcs with tails in `O_j`.  Then `d` is available in the hybrid `C_z`
exactly when the following signed clause holds:

\[
 A_d(z)=
 \bigvee_{j:\ d\in C_0[O_j]}(z_j=0)
 \ \vee\!
 \bigvee_{j:\ d\in C_1[O_j]}(z_j=1),               \tag{3.1}
\]

with a forced common occurrence making the clause identically true.

### Theorem 3.1 (matching-certified circuit fusion)

Let `M_*` be a perfect matching of the outer diamond graph `B_m`.  A hybrid
`C_z` contains all physical edges of `M_*` if and only if

\[
                         \bigwedge_{d\in M_*}A_d(z)   \tag{3.2}
\]

is true.  Consequently, if (3.2) has a solution for which `C_z` is one
Hamilton cycle, then the edges of `M_*` form a spanning
`Cat_m`-path forest and prove the Catalan Linear Matching assertion.

Conversely every Catalan linear matching contained in a Hamilton hybrid
gives a pair `(M_*,z)` satisfying (3.2).

#### Proof

Equation (3.1) is the literal orbit-by-orbit edge-availability condition.
Taking its conjunction over `M_*` proves the first assertion.  A perfect
outer matching uses every lower and upper colour once.  Since it selects
`N<M` edges of one physical Hamilton cycle, those edges have physical
degree at most two and cannot contain the whole cycle; hence they are a
spanning forest with `M-N=K` components.  The converse reads the same
selected edges back as their unique outer diamonds. \(\square\)

For a fixed `M_*`, if every clause in (3.2) touches at most two exchange
orbits, its feasibility is ordinary `2`-SAT.  If every nontrivial clause is
unit, feasibility is simply the absence of opposite polarity requests on
one orbit.  This is a useful conditional exchange lemma: the two literature
cycles fuse whenever one can choose `M_*` so that its signed availability
clauses are satisfiable and one satisfying state has one-cycle monodromy.

Coverage alone is weaker.  Replacing `d` in (3.1) by one lower or upper
colour gives the clauses for two-sided rainbow coverage, but these do not
impose occurrence Hall.  Section 4 shows that this distinction is
load-bearing even when both endpoints already satisfy every coverage
clause.

If a hybrid is allowed to have several physical cycles, one must add the
exact condition that `M_*` omit at least one edge from every physical
component.  Without it, a selected component can remain cyclic.  Requiring
one-cycle monodromy is the clean sufficient form used in Theorem 3.1.

## 4. A dimension-minimal two-cycle lock

Use bitmasks on `[6]={0,...,5}`.  Start from the following rank-four cyclic
order emitted by the vendored GMM SatCycle implementation:

```text
57 29 53 39 23 27 15 45 43 51 58 46 30 54 60
```

Its cyclic rank-three seam facets omit five masks.  The deterministic
increasing augmenting scan hosts the omitted facets in the blocks

\[
          0\mapsto49,\quad1\mapsto28,\quad
          3\mapsto38,\quad5\mapsto26,\quad7\mapsto44.       \tag{4.1}
\]

Splitting those blocks gives the Hamilton cycle

```text
P = 56 49 25 28 21 37 38 7 19 26
    11 13 44 41 35 50 42 14 22 52 .
```

Let `Q` be its coordinatewise complement:

```text
Q = 7 14 38 35 42 26 25 56 44 37
    52 50 19 22 28 13 21 49 41 11 .
```

Both are Hamilton cycles of `J(6,3)`.  On each cycle the lower and upper
load profiles are exactly

\[
                         1^{10}2^5.                  \tag{4.2}
\]

Thus both cycles are simultaneously lower-tight and upper-tight.  In
particular each one, by itself, realizes the conjunction of the two
published coverage conclusions on the same middle chronology.

Nevertheless

\[
                         \nu(G(P))=\nu(G(Q))=14<15.  \tag{4.3}
\]

For example, `G(P)` has the Hall cut

\[
                       \{12,40\}\longmapsto\{45\},  \tag{4.4}
\]

while `G(Q)` has

\[
                       \{5,12\}\longmapsto\{29\}.   \tag{4.5}
\]

So even a single two-sided-rainbow Hamilton cycle is not enough: the same
occurrence must serve the two palettes.

For the displayed orientations, `pi=s_Q^{-1}s_P` has two orbits of length
ten.  The four hybrid matching ranks are

\[
                             14,10,12,14.             \tag{4.6}
\]

After reversing `Q`, the orbit lengths are `4,4,5,7`; among the sixteen
hybrids, twelve have matching rank twelve and four have rank fourteen.
No directed successor hybrid has a common transversal.

The obstruction is stronger than this canonical cube.

### Theorem 4.1 (complete `P union Q` two-factor lock)

There are exactly `6272` spanning degree-two subgraphs of `P union Q`.
Their colour-incidence matching-rank histogram is

\[
 9^{38}\ 10^{768}\ 11^{2154}\ 12^{2365}\ 13^{820}\ 14^{127}. \tag{4.7}
\]

In particular none has a common transversal.  Among them exactly `336`
are lower- and upper-complete.  Their rank histogram is

\[
 10^6\ 11^{20}\ 12^{125}\ 13^{126}\ 14^{59}.       \tag{4.8}
\]

Exactly `176` of these double-rainbow states are Hamilton cycles, and all
remain Hall-deficient.

#### Finite proof

At every rank-three vertex the union `P union Q` has four incident edges.
The audit branches on one undecided edge and propagates the forced equations
`degree=2`; this enumerates every binary spanning two-factor once.  For
each leaf it reconstructs all occurrence-labelled lower--upper incidences
and runs the ordinary bipartite augmenting-path algorithm.  The displayed
counts sum to `6272` and every matching is replayed from literal bitmasks.
No SAT, MILP, randomization, or symmetry assumption is used.

The theorem closes every degree-preserving alternating-circuit interpolation
whose final edges stay in this two-cycle union.  It does **not** close a
switch using a new Johnson edge or a different starting cycle.

## 5. The forest escape

The same forty-edge union contains the desired Catalan object.  Take the
five paths

```text
7--19--50--42--14--22--52--56
11--13--28
21--37--38
26--25--49
35--41--44
```

Their fifteen edges have lower colours

```text
3 5 6 9 10 12 17 18 20 24 33 34 36 40 48
```

and upper colours

```text
15 23 27 29 30 39 43 45 46 51 53 54 57 58 60
```

each exactly once.  These are the full rank-two and rank-four layers of
`[6]`.  The physical lift is visibly a spanning five-path forest.  Orienting
the five displayed paths gives an ordered four-transversal: all lower
colours, upper colours, tails, and heads are injective, and the directed
trace is acyclic.

Twelve selected edges lie in `P`; only

\[
                  13--28,\qquad25--26,\qquad19--50   \tag{5.1}
\]

come solely from `Q`.  The complete finite census finds exactly four
linear common transversals in `P union Q`, using respectively

\[
                         3,5,10,12                  \tag{5.2}
\]

`Q`-edges.  Thus three is the exact asymmetric repair distance in this
fixture.

This proves a strict separation:

\[
 \begin{array}{c}
 \text{the union contains an ordered four-transversal}\\[1mm]
 \not\Downarrow\\[-1mm]
 \text{the union contains a spanning two-factor whose colour graph}\\
 \text{has a perfect matching.}
 \end{array}                                         \tag{5.3}
\]

The unused-edge chronology is the entire obstruction.  A cycle-first
exchange insists that the five connector edges also be selected from the
same union and balance every physical vertex.  The Catalan theorem needs
only the fifteen forest edges.  In this example those extra degree equations
destroy occurrence Hall in all `6272` cases.

## 6. The corrected literature bridge

The exact sufficient all-dimensional target suggested by the two published
cycles is therefore not “interpolate through Hamilton cycles.”  It is the
following weaker forest-fusion statement.

> **Two-cycle Forest Fusion target.**  Choose a lower-tight Johnson
> Hamilton cycle `C_-` obtained from a GMM tight enumeration and an
> upper-tight Hamilton cycle `C_+` obtained from Middle Levels such that
> `E(C_-) union E(C_+)` contains an ordered four-transversal.

This target implies the Catalan Linear Matching assertion immediately,
because the selected ordered four-transversal is the required spanning
`Cat_m`-path forest.  It does not require either the selected or unselected
edges to form a Hamilton hybrid.  Section 5 is a positive `m=3`
calibration.

Theorem 3.1 remains useful when a Hamilton hybrid does exist: it reduces a
specified pair of literature cycles to a perfect outer matching plus signed
orbit clauses and one-cycle monodromy.  Theorem 4.1 shows why failure of
that restricted system should trigger forest-first selection rather than a
search for more full-cycle switch states.

Nothing here supplies the all-`m` forest-fusion theorem.  In particular,
separate existence of `C_-` and `C_+` gives no theorem about the physical
degree or graphic independence of a matching selected from their union.
Those are exactly the integral correlations retained by the ordered
four-transversal formulation.

## 7. Minimality, replay, and scope

At `m=2`, root a Hamilton cycle of `J(4,2)` at one vertex and quotient only
by reversal.  There are exactly sixteen cycles.  Twelve have both colour
layers complete, and every one has colour-incidence matching rank four.
The remaining four have coverage `(3,3)`.  Hence the explicit `m=3`
cycle is the smallest double-rainbow Hall counterexample.

Run

```text
python3 scratch/audit_catalan_two_cycle_hybrid_lock_m2_m3_20260731.py
```

The script independently rebuilds the GMM-derived fixture, verifies both
orientations of the successor hybrid cube, exhausts all `6272` spanning
two-factors of the forty-edge union, exhausts every linear common
transversal in the same union, and performs the complete `m=2` census.
Its canonical payload SHA-256 is

```text
35efd9f5b8b89d8a7f49f39ce87ef0b865ec40f865ff2a79b73949793f344a9c
```

Proved here:

* the exact Boolean successor-orbit theorem;
* the signed occurrence-clause criterion for a fixed outer matching;
* a dimension-minimal double-rainbow Hall failure;
* a complete two-cycle-union lock at `m=3`; and
* an explicit forest-first escape inside that same locked union.

Not proved here:

* an all-`m` Two-cycle Forest Fusion theorem;
* that the particular published recursive cycles are the right pair in
  every dimension;
* the stronger Regenerative Shadow--Braid theorem; or
* any implication from this central result to residence, deeper shadows,
  or the final compiler.
