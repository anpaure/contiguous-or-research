# Central two-interval-bank reduction and the Engel-range gate

**Date:** 2026-08-02  
**Status:** exact reduction and literature-scope audit.  This note does not
prove the required central packings, a Catalan linear forest, a universal
word, or any new value of `nu(k)`.

## 1. Central Boolean diamonds

Let

\[
 \mathcal L={ [2m]\choose m-1},\qquad
 \mathcal M={ [2m]\choose m},\qquad
 \mathcal U={ [2m]\choose m+1}.
\]

A maximal interval of the three-level poset
`P_(2m;m-1,m+1)` has the form

\[
 I(L,U)=[L,U]=\{L,L+a,L+b,U\},
 \qquad U=L\cup\{a,b\}.                         \tag{1.1}
\]

It therefore determines the Johnson edge

\[
                  (L+a)(L+b)                       \tag{1.2}
\]

on `mathcal M`, coloured at its two outer shores by `L` and `U`.
An interval packing is exactly a family of such edges with pairwise
distinct lower colours, upper colours, and middle endpoints.

Put

\[
       N=|\mathcal L|=|\mathcal U|={2m\choose m-1},
       \qquad W=|\mathcal M|={2m\choose m}.
                                                               \tag{1.3}
\]

Then

\[
                         {N\over W}={m\over m+1}.     \tag{1.4}
\]

## 2. The two-bank reduction

### Theorem 2.1 (two interval banks give the four resource rows)

Suppose there are two interval packings `I_0,I_1` in
`P_(2m;m-1,m+1)` such that

1. their lower-endpoint palettes partition `mathcal L`; and
2. their upper-endpoint palettes partition `mathcal U`.

Then the union of their Johnson edges can be oriented so that

* every lower colour occurs exactly once;
* every upper colour occurs exactly once;
* every middle set occurs at most once as a tail; and
* every middle set occurs at most once as a head.

Thus the union satisfies the four partition/resource rows of an ordered
Boolean-diamond transversal. Under the established terminology in which an
`ordered four-transversal` also includes graphic independence, this is
not yet an ordered four-transversal: the graphic row is exactly the
acyclicity condition below.

If the union graph on `mathcal M` is acyclic, the oriented union is an
ordered four-transversal and is already the Catalan linear forest required
by the central owner construction. More generally, if it has `c` cycle
components, deleting one interval from each cycle leaves a linear forest
with total defect exactly `c` in each outer palette.

#### Proof

Within each `I_epsilon`, interval disjointness says that its Johnson edges
form a matching.  Hence their union is a graph of maximum degree two whose
components are paths and even cycles (the edge colours alternate between
the two matchings on every nontrivial component).

Orient every path consistently from one end to the other and every cycle
cyclically.  Each middle vertex then has indegree and outdegree at most one.
The palette-partition hypotheses give every lower and upper colour exactly
once across the union.  These are precisely the four ordered-transversal
conditions.

If the union has no cycle it is a linear forest.  Otherwise delete one edge
from each cycle.  The remaining maximum-degree-two graph is acyclic, and
exactly the two outer colours of each deleted interval are lost.  \(\square\)

### Corollary 2.2 (the remaining topological defect is transparent)

Under the two palette-partition hypotheses, the central correlation problem
separates into:

1. constructing the two interval banks; and
2. absorbing the alternating cycles of their union.

No further tail/head matching is required. In particular, a construction
with `O(1)` alternating cycles gives an `O(1)`-defect central forest before
the residence, upper-shadow, and compiler guards are imposed.

Conversely, every Catalan linear forest with the exact two outer palettes
splits into two such interval packings: alternately colour the edges on
each path. Each colour class is a matching on the middle layer, hence an
interval packing, and the two outer palettes still partition their full
levels. Therefore the zero-cycle complementary bi-packing statement is
equivalent to the central ordered-four-transversal/linear-forest gate.

Only a four-resource transversal *without* the graphic row can fail to
split: its maximum-degree-two graph may contain an odd cycle.

## 3. Exact relation to the 2026 interval-packing theorem

Dong and Mao prove that the maximum number of pairwise disjoint maximal
intervals in `P_(n;ell,ell+r)` equals `{n choose ell}` whenever

\[
                         n\ge (\ell+1)r+\ell.         \tag{3.1}
\]

Their construction is explicit and uses a cycle-lemma rule in the critical
case, followed by a coordinate recursion.  See:

* Yuxian Dong and Jianxi Mao, *Engel's Interval Packing Problem in the
  Boolean Lattice*, arXiv:2607.04794 (2026),
  <https://arxiv.org/abs/2607.04794>.

For the central diamonds here, `n=2m`, `ell=m-1`, and `r=2`.  Condition
(3.1) becomes

\[
                         2m\ge 3m-1,                 \tag{3.2}
\]

which fails for every `m>=2`.  Complementation gives the same central
failure.  Their Section 4 explicitly leaves the central three-level range
open.  Thus their theorem cannot be cited as an existence proof for either
bank in Theorem 2.1.

There is also an elementary capacity distinction. Every interval consumes
two middle vertices, so a central interval packing has size at most
`W/2`. Write `b_e=|\mathcal I_e|`. The palette partitions imply

\[
                 N=W-{W\over m+1}                   \tag{3.3}
\]

intervals, while the individual middle ceilings give the exact window

\[
 {W\over2}-{W\over m+1}\le b_e\le {W\over2}
 \qquad(e=0,1).                                      \tag{3.4}
\]

This is a necessary capacity window, not a feasibility characterization.

Equivalently, the two unused-middle-vertex counts
\(\Delta_e=W-2b_e\) are nonnegative and satisfy

\[
                 \Delta_0+\Delta_1={2W\over m+1}
                 =2\operatorname {Cat}_m.            \tag{3.5}
\]

Hence the two-bank problem asks for two correlated almost-perfect central
matchings, not for the noncentral full packing proved by Dong--Mao.

## 4. Precise surviving lemma

The literature reduction leaves the following self-contained target.

### **UNPROVED** central complementary bi-packing lemma

For every sufficiently large `m`, there are two central interval packings
`I_0,I_1` whose lower palettes and upper palettes separately partition the
two outer levels, and whose union has `O(1)` alternating cycles.

Before cycle deletion this lemma supplies all four resource rows; after
deleting one interval per cycle it supplies a central linear forest with
`O(1)` missing lower and upper colours. A zero-cycle version supplies
the exact Catalan linear forest and, by Corollary 2.2, is equivalent to the
central ordered-four-transversal gate.

The lemma does not require either bank to be maximum.  In fact, requiring
both to have the conjectural central maximum `W/2` would be incompatible
with `b_0+b_1=N<W`.  Its content is instead stronger than two unrelated
large packings: the two outer palettes must be complementary
simultaneously.  It is also only the central gate.  A contiguous-OR
construction must still correlate the result with residence,
arbitrary-width upper witnesses, physical chronology, and the lower common
cap.

## 5. Consequence for the current programme

The Dong--Mao theorem is useful as a construction language and as a warning
about the exact frontier, but it does not close the programme. Its
cycle-lemma map can be used as a prospective first bank only after an
explicit decomposition into noncentral fibres satisfying (3.1); no such
decomposition of the central palettes is proved here. Conditional on such a
first bank, the second bank may be sought by alternating-circuit exchange.
The exact acceptance rows are:

1. complementary lower and upper palettes;
2. matching capacity inside each bank;
3. bounded cycle count in the union; and
4. preservation of any protected pivot/collar resources.

Failure of the canonical first bank would be a scoped fibre obstruction,
not a no-go for the central complementary bi-packing lemma.

Nor does the cycle lemma provide the cycle absorber in Corollary 2.2.
Swapping the two bank colours on an alternating cycle, or reversing its
orientation, leaves the uncoloured Johnson union and hence its cycle count
unchanged.  Removing that cycle while retaining both outer palettes and the
middle capacities requires an additional interval-replacement circuit (or
a connected exchange theorem) not present in Dong--Mao.

## 6. A tempting parity construction is impossible

One might try to force the union graph to be bipartite in advance.  Split
the ground set as `[2m]=A dotcup B` and allow only intervals for which the
two new elements `U-L` consist of one element of `A` and one of `B`.  The
two middle endpoints then have opposite parity of `|M cap A|`, so every
selected Johnson edge crosses a fixed bipartition.

This restriction cannot cover every lower colour.

### Proposition 6.1 (fixed coordinate-bipartition overload)

For `m>=3`, no ordered four-transversal can use only intervals whose two
new elements cross one fixed ground-set bipartition.

#### Proof

If `|A|<=m-1`, choose an `(m-1)`-set `L` containing all of `A`.  No element
of `A-L` is available, so `L` has no permitted interval.  Similarly, if
`|B|<=m-1`, a lower set containing all of `B` has no permitted interval.
Hence covering all lower colours forces

\[
                         |A|=|B|=m.                  \tag{6.1}
\]

Now consider the `m` lower sets `L=A-{a}`, one for each `a in A`.  Every
permitted interval from such an `L` must add the missing `a` and one element
of `B`.  One of its two middle endpoints is therefore the same set `A`.
Consequently the middle vertex `A` has degree at least `m` in the selected
Johnson graph.  An ordered four-transversal has tail and head capacity one,
and hence total physical degree at most two.  This is impossible for
`m>=3`.  \(\square\)

Thus bipartiteness must be obtained from the selected union graph itself
(or by a state-dependent parity), not by requiring every diamond to cross
one fixed coordinate cut.  This also explains why the two banks must be
chosen in correlation: a globally convenient parity restriction can destroy
local middle capacity at a single extreme vertex.

## 7. Common-base insertion

On the ground set of ordered central diamonds, the four resource rows are
the lower-, upper-, tail-, and head-partition matroids; the physical
Johnson edges supply the graphic matroid. Theorem 2.1 says that a
complementary pair of interval banks automatically satisfies the first four
rows. The zero-cycle condition is exactly independence in the fifth,
graphic row. Thus the complementary bi-packing lemma is an exact structured
common-base target, not a replacement for the common-base condition.

Dong--Mao supplies neither a central bank nor the joint common base. The
remaining compatibility is simultaneous: complementary lower and upper
palettes, middle matching inside each bank, and acyclicity (or a bounded
cycle defect) of their union, all on the same protected host.
