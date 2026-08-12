# Catalan forest supports, Rado reduction, and the ordered-diamond gate

Date: 2026-07-31  
Status: exact reductions and solver-free `m=2,3` calibration; no all-`m`
existence claim

## 0. Verdict

There is a strict simplification of the proposed fusion of a lower-tight
GMM cycle `P` and an upper-tight Middle Levels cycle `Q`.

It is unnecessary to hybridize them into a spanning two-factor before
choosing the Catalan diamonds.  It is enough to find **one spanning physical
linear forest** `R` inside `P union Q` whose lower/upper colour-incidence
graph satisfies Hall.  Once `R` is fixed, the remaining selection is an
ordinary bipartite perfect matching; integrality is automatic, and every
selected edge is already physically acyclic.

This relaxation is genuinely stronger at the first nontrivial case.  For
the explicit `m=3` cycles audited in
`MATH_THEOREM_CATALAN_TWO_CYCLE_HYBRID_LOCK_AND_FOREST_ESCAPE_20260731.md`,
no spanning two-factor in `P union Q` satisfies occurrence Hall.  In
contrast, the same union contains 28 unoriented spanning Hamilton paths
whose colour-incidence graph has a perfect matching.  One explicit path is

```text
7 19 26 42 14 38 37 21 49 25 28 22 52 50 35 41 11 13 44 56.
```

Its support colour loads are `lower=upper=1^11 2^4`; its colour-incidence
graph has a unique perfect matching, and the selected physical edges form
five paths on four vertices each.  This is exactly `Cat_3=5` components.

Thus the strongest currently calibrated two-cycle target is:

> Choose a lower-tight cycle `P` and an upper-tight cycle `Q` such that
> `P union Q` contains a spanning linear forest `R` satisfying colour Hall.

This is a central Catalan Linear Matching target only.  It does not by
itself prove residence, deeper shadows, the lower compiler, or the full
word formula.

## 1. Setup

Let `|Omega|=2m` and

\[
 {\cal L}=\binom\Omega{m-1},\quad
 {\cal X}=\binom\Omega m,\quad
 {\cal U}=\binom\Omega{m+1}.
\]

Put

\[
 K=\operatorname{Cat}_m,\qquad
 N=|{\cal L}|=|{\cal U}|=mK,\qquad
 M=|{\cal X}|=(m+1)K=N+K.
\]

For a Johnson edge `e=TH` define

\[
             \ell(e)=T\cap H,\qquad u(e)=T\cup H.
\]

For any physical support `R subseteq E(J(2m,m))`, define its
colour-incidence multigraph `G_R` with shores `cal L,cal U` and one
occurrence edge `ell(e)--u(e)` for each `e in R`.

## 2. Forest-support Rado theorem

### Theorem 2.1

Let `R` be a spanning physical linear forest on `cal X`.  The following are
equivalent.

1. `R` contains a Catalan linear matching (an ordered four-transversal).
2. `G_R` has a perfect matching.
3. For every `S subseteq cal L`,

   \[
                     |N_{G_R}(S)|\ge |S|.
   \]

4. The occurrence families

   \[
       E_L=\{e\in R:\ell(e)=L\}\qquad(L\in{\cal L})
   \]

   have a transversal independent in the partition matroid whose parts are
   the upper colours.

Every such transversal has `N` physical edges and is a spanning linear
forest with exactly `M-N=K` components.  Orienting its components gives
injective tail and head maps and hence an ordered four-transversal.

#### Proof

Statements 2 and 3 are Hall's theorem.  Statement 4 is Rado's theorem for
the upper-colour partition matroid: the rank of a union of occurrence
families is exactly the number of distinct upper neighbours, so Rado's rank
inequalities are precisely Hall's inequalities.

A perfect matching selects each lower and upper colour exactly once.  Its
physical edge set is a subset of the spanning linear forest `R`, hence is
acyclic and has physical degree at most two.  All `M` middle vertices occur
as vertices of `R`; isolated vertices are allowed components of the
selected forest.  With `N` selected edges, the component count is `M-N=K`.
Each nontrivial path has two orientations; tails and heads are automatically
injective because physical degree is at most two.  Reading every edge as
`(L,U,T,H)` gives the ordered four-transversal.  The converse is immediate.
`square`

### Corollary 2.2 (Hamilton-path support)

If `P union Q` contains a spanning Hamilton path `R` for which `G_R`
satisfies Hall, then `P union Q` contains a Catalan linear matching.

This absorbs all physical degree and graphic constraints before invoking
matching theory.  The last gate is a single ordinary bipartite matching.

## 3. Exact extension to degree-two supports

Let `R` be any spanning physical graph of maximum degree two and let
`C(R)` denote its cycle components.

### Theorem 3.1 (break--Hall criterion)

`R` contains a Catalan linear matching if and only if there is a breaker set
`D subseteq E(R)` containing at least one edge from every member of `C(R)`
such that `G_{R-D}` has a perfect matching.

#### Proof

If `G_{R-D}` has a perfect matching, its selected physical support lies in
the linear forest `R-D`; Theorem 2.1 applies.  Conversely, any Catalan linear
matching contained in `R` omits an edge from every physical cycle (its
selected support is acyclic).  Choose one omitted edge from each cycle to
form `D`; the matching survives in `G_{R-D}`.  `square`

For one Hamilton cycle, no explicit breaker search is needed: any outer
perfect matching has only `N<M` edges and therefore omits at least one cycle
edge.  This recovers the usual cycle-first Hall criterion.  For several
cycles, however, the omitted edges must hit every component; merely having
an outer perfect matching is insufficient.

## 4. Why the direct problem is not ordinary matroid intersection

On an arbitrary supply `E` (for example `P union Q`) the exact direct model
is

\[
 \begin{aligned}
 x(\delta_L)&=1 &&(L\in{\cal L}),\\
 x(\delta_U)&=1 &&(U\in{\cal U}),\\
 x(\delta_T)&\le2 &&(T\in{\cal X}),\\
 x(E(S))&\le |S|-1 &&(\varnothing\ne S\subseteq{\cal X}).
 \end{aligned}
\tag{4.1}
\]

The first two rows are the two colour-partition constraints; the last two
say that the physical lift is a linear forest.

The linear forests of a graph do not form a matroid.  On vertices
`{c,1,2,3}`, let

```text
A = {c1,c2},       B = {c1,c3,12}.
```

Both are linear forests and `|A|<|B|`, but adding `c3` to `A` creates
degree three and adding `12` creates a triangle.  Thus the augmentation
axiom fails.  Consequently (4.1) is not reduced to two-matroid intersection
by naming the graphic row.

The raw Boolean-local incidence also contains the triangle minor

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
\]

whose determinant is `-2`; total unimodularity is unavailable in this
form.  The support-first theorem is effective precisely because it makes
the nonmatroid degree/acyclicity row true before Rado is applied.

## 5. Fractional versus integral obstruction

For a fixed forest support `R`, `G_R` is bipartite.  Its perfect-matching
polytope is integral, so there is no fractional gap after the support is
chosen: Hall is the complete obstruction.

Requiring the selected forest to extend to a full physical two-factor adds
an unnecessary endpoint-completion problem.  Degree equations alone do not
make that completion integral: two disjoint triangles with weight `1/2` on
every edge satisfy every degree-one equation but have no perfect matching.
The omitted blossom/odd-set rows are exactly the sort of global constraint
that the forest-first route avoids.

The `m=3` audit makes this distinction literal.  No two-factor support in
the displayed `P union Q` passes occurrence Hall, whereas 28 Hamilton-path
supports do.  The earlier two-factor lock was therefore a lock of the
unused edges, not of the required Catalan diamonds.

## 6. Direct ordered-diamond hypergraph

The entire central problem can also be written as a four-partite
four-uniform hypergraph.  An ordered atom is

\[
             (L,U,T,H),\qquad
 L=T\cap H,\quad U=T\cup H,quad T\ne H,
\]

on the parts `cal L,cal U,cal X_tail,cal X_head`.  Its exact parameters are:

\[
 \deg(L)=\deg(U)=m(m+1),\qquad
 \deg(T)=\deg(H)=m^2.
\tag{6.1}
\]

The nonzero pair codegrees are

\[
 \deg(L,U)=2,\quad
 \deg(L,T)=\deg(L,H)=m,\quad
 \deg(U,T)=\deg(U,H)=m,\quad
 \deg(T,H)=1,
\tag{6.2}
\]

whenever the corresponding containment/Johnson-adjacency relation holds.
Thus maximum codegree divided by minimum degree is `1/m`.

A matching saturating `cal L` and `cal U` has exactly `N` atoms and leaves
exactly

\[
                      M-N=K
\]

unused vertices on each middle shore.  Its directed physical lift has
indegree and outdegree at most one, hence is a disjoint union of directed
paths and directed cycles.  It is an ordered four-transversal exactly when
the directed cycles are absent.

There is a canonical fractional solution: put weight

\[
                     1/[m(m+1)]
\]

on every atom.  Every outer vertex has load one and every middle vertex has
load `m/(m+1)<1`.  Hence fractional feasibility, including the correct
total middle leave, is automatic.

The fixed uniformity and normalized codegree `1/m` put the hypergraph in
the range where sparse-hypergraph nibble methods plausibly give an
almost-perfect matching.  They do **not**, without an additional theorem,
give the property needed here:

* exact saturation of both outer shores;
* optionally prescribed `K`-sets of unused tails and heads; and
* absence (or repair) of every directed physical cycle.

No off-the-shelf sparse matching theorem is invoked here.  The exact missing
ingredient in this language is a robust outer absorber together with a
cycle-switch theorem.  A random partial-permutation heuristic predicts only
`Theta(log m)` physical cycles and no-cycle probability `Theta(1/m)`, so
acyclicity looks like a polynomial rather than exponential tax; this is
calibration, not proof.

## 7. Small-case audit

The solver-free script

```text
scratch/audit_catalan_forest_support_rado_m2_m3_20260731.py
```

checks the explicit `m=3` path, all colour incidences, the unique perfect
matching, and the selected physical component orders.  With `--full` it
exhausts all Hamilton paths in the displayed `P union Q` and obtains the
following unoriented matching-rank histogram:

```text
rank 8:      26
rank 9:    2588
rank 10:  31556
rank 11:  89086
rank 12:  79960
rank 13:  23990
rank 14:   2066
rank 15:     28
```

There are `229300` unoriented spanning Hamilton paths in total and exactly
`28` Hall-successful ones.  The selected perfect matching for the displayed
path uses ten `P` edges and five `Q` edges and has physical component orders

```text
4 4 4 4 4.
```

At `m=2`, the audit checks all rooted Hamilton cycles up to reversal and
recovers the already-known positive common-transversal census.  Thus the
support-first theorem is consistent in both smallest dimensions and first
separates from two-factor hybridization at `m=3`.

## 8. Honest frontier

The cleanest two-cycle sufficient theorem now is:

> **Path-Support Forest Fusion.**  For every `m`, some lower-tight GMM cycle
> `P` and upper-tight Middle Levels cycle `Q` have a union containing a
> spanning Hamilton path `R` whose colour-incidence graph satisfies Hall.

The weaker logically exact version allows any spanning linear forest `R`.
Proving either gives the central Catalan Linear Matching theorem.  The
four-partite formulation suggests a different route: exact outer
absorption followed by cycle elimination.

Neither statement is presently proved uniformly.  Even if one is proved,
the full identity `nu(k)=B(k)` still additionally needs the residence,
deeper-shadow, seam and lower-compiler rows of the Regenerative
Shadow--Braid theorem.  This note sharpens the central gate; it does not
collapse those downstream rows.

