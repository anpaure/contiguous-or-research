# Mesoscopic defect-to-buffer Hall: exact dispersal criterion and dense-cluster reduction

## Status

The aggregate-linear packet reservoir does **not** by itself absorb an
arbitrary `W/sqrt(r)` leave.  A linear `rho`-regular `h`-graph can fail the
defect-to-buffer Hall condition by the factor `h/rho`.

There is, however, an exact sufficient invariant.  If no reservoir packet
contains more defect objects than the minimum reservoir degree, the
incidence graph has a matching saturating every defect.  Every defect set
admits a canonical decomposition into such a Hall-matchable dispersed part
and at most `|X|/(rho+1)` dense packet clusters.

For the pull-ring parameters `h=Theta(sqrt r)`, `rho=r^(1/4)`, and
`|X|=O(W/sqrt r)`, the number of dense clusters is only
`O(W/r^(3/4))`.  Thus the mesoscopic absorber problem reduces exactly to
absorbing those packet-supported clusters and forcing the main cover-down
leave to avoid the exceptional low-degree reservoir resources.

## 1. The defect-buffer incidence graph

Let `R` be a linear `h`-uniform hypergraph.  Its vertices are physical
owner/root resources and its edges are available buffer packets.  For a
defect set `X subset V(R)`, define the bipartite incidence graph

\[
 G_X=(X,R;\{ve:v\in X\cap e\}).                            \tag{1.1}
\]

A matching in `G_X` saturating `X` assigns a distinct packet socket to
every defect.  This is only the combinatorial socket assignment; each
assigned incidence must still carry the required literal two-phase
switch.

### Theorem 1.1 (dispersed-leave Hall lemma)

Suppose `delta` is a positive integer and

\[
 d_R(v)\ge\delta\quad(v\in X),
 \qquad
 |e\cap X|\le\delta\quad(e\in R).                         \tag{1.2}
\]

Then `G_X` has a matching saturating `X`.

#### Proof

Let `Y subset X`.  Count incidences between `Y` and its packet
neighbourhood:

\[
 \delta|Y|
 \le\sum_{v\in Y}d_R(v)
 =\sum_{e\in N(Y)}|e\cap Y|
 \le\delta|N(Y)|.                                         \tag{1.3}
\]

Thus `|N(Y)|>=|Y|` for every `Y subset X`.  Hall's theorem applies.
`square`

The same proof works with unequal bounds: minimum defect degree `delta_0`
and maximum packet load `ell` give

\[
                         |N(Y)|\ge {\delta_0\over\ell}|Y|.\tag{1.4}
\]

## 2. Linearity and near-regularity alone are insufficient

Theorem 1.1 needs its packet-load hypothesis.  It does not follow from
linearity.

### Proposition 2.1 (affine-plane cut obstruction)

Let `q` be a prime power and choose `rho<q` parallel classes of lines in
the affine plane of order `q`.  The resulting hypergraph has

\[
 N=q^2,qquad h=q,qquad d(v)=\rho,                         \tag{2.1}
\]

and is linear.  For `X=V`, its defect-buffer incidence graph has only

\[
                         |R|=\rho q={\rho\over h}|X|<|X|  \tag{2.2}
\]

packet vertices, so no matching can saturate `X`.

Disjoint unions of this construction give the same obstruction at any
larger scale.  Hence a theorem using only

\[
 \text{linearity},\qquad d(v)=(1+o(1))\rho,qquad
 \rho=o(h)                                                 \tag{2.3}
\]

cannot prove mesoscopic Hall expansion.

#### Proof

Two affine lines from different parallel classes meet once, and lines in
one class are disjoint, so the hypergraph is linear.  Every point lies on
one selected line from every class, giving degree `rho`.  There are `q`
lines per selected class, which proves (2.2).  `square`

This does not construct an obstruction inside the pull-ring orbit.  It
proves that the aggregate-linear reservoir theorem, considered only
through its stated output parameters, is logically insufficient.

## 3. Canonical dense-cluster peeling

The failure in Proposition 2.1 has a precise form: too many defects are
concentrated in one packet.  Every defect set splits into this dense part
and a Hall part.

### Theorem 3.1 (dense-or-Hall decomposition)

Let `delta` be a positive integer.  Let `R` be any hypergraph and let
`X subset V(R)` consist of vertices of degree at least `delta`.  There are
pairwise disjoint subsets

\[
                         C_1,\ldots,C_t,X_0               \tag{3.1}
\]

which partition `X`, and packets `e_1,...,e_t`, such that

\[
 C_i\subseteq e_i,qquad |C_i|\ge\delta+1,qquad
 t\le {|X|\over\delta+1},                                 \tag{3.2}
\]

while

\[
                         |e\cap X_0|\le\delta
                         \quad(e\in R).                    \tag{3.3}
\]

Consequently the incidence graph `G_(X_0)` has a matching saturating
`X_0`.

#### Proof

Start with `X^(0)=X`.  While some packet `e_i` satisfies
`|e_i cap X^(i-1)|>=delta+1`, put

\[
 C_i=e_i\cap X^{(i-1)},\qquad
 X^{(i)}=X^{(i-1)}-C_i.                                   \tag{3.4}
\]

The `C_i` are disjoint and each has size at least `delta+1`, so the
process stops after at most `|X|/(delta+1)` steps.  At termination put
`X_0=X^(t)`.  Equation (3.3) holds by construction, and Theorem 1.1 gives
the final assertion.  `square`

The supporting packets `e_i` need not be resource-disjoint; only their
captured defect subsets are disjoint.  Nor does (3.2) say that a partial
set `C_i subsetneq e_i` is absorbable by the known whole-packet trade.
Those are the two exact physical rows left by the reduction.

## 4. Pull-ring scale

For Hall assignment alone, it is better not to delete multiply
intersecting packets.  A much thinner raw sample has an exceptional set
smaller than the target leave.

### Theorem 4.1 (logarithmic raw packet reservoir)

Let `H` be an `h`-uniform, `D`-regular hypergraph on `N` vertices, and let
`8<=rho<=D`.  There is a packet subfamily `S` with

\[
                         |S|\le {4N\rho\over h}            \tag{4.1}
\]

such that all but at most

\[
                         4N\exp(-\rho/8)                  \tag{4.2}
\]

vertices have degree at least `rho/2` in `S`.

#### Proof

Select each packet independently with probability `p=rho/D`.  The
expected packet count is `Nrho/h`.  A fixed vertex has selected degree
`Bin(D,p)`, so its probability of degree below `rho/2` is at most
`exp(-rho/8)`.  Markov's inequality, with factor four for both random
variables, gives an outcome satisfying (4.1)--(4.2) simultaneously.
`square`

For the pull-ring system take

\[
                         \rho=A\log r                      \tag{4.3}
\]

with any fixed `A>4`.  Then

\[
 |S|=O(W\log r/\sqrt r),
 \qquad |Z|=O(Wr^{-A/8})=o(W/\sqrt r).                    \tag{4.4}
\]

For every leave `X subset V-Z` of size `O(W/sqrt r)`, Theorem 3.1 with
`delta=floor(rho/2)` leaves only

\[
                         O\!\left({W\over\sqrt r\log r}\right)\tag{4.5}
\]

dense packet-supported clusters; its dispersed remainder has a Hall
assignment to distinct packets of `S`.

The logarithmic reservoir is not linear.  Thus (4.5) solves packet
identity Hall and the exceptional-set scale, but not resource-disjointness
of the literal buffer gadgets.

### A linear alternative

Use the linear reservoir from
`MATH_THEOREM_AGGREGATE_LINEAR_PACKET_RESERVOIR_AND_ANCHORED_FAN_20260806.md`
with

\[
 h=2L=\Theta(\sqrt r),\qquad
 \rho=r^{1/4},\qquad
 \varepsilon=r^{-1/16},qquad
 \delta=\lfloor(1-2\varepsilon)\rho\rfloor.               \tag{4.6}
\]

Let `Z` be its exceptional low-degree resource set.  For every defect set

\[
                         X\subseteq V(R)-Z,qquad
                         |X|\le c{W\over\sqrt r},          \tag{4.7}
\]

Theorem 3.1 gives

\[
                         t=O\!\left({W\over r^{3/4}}\right)\tag{4.8}
\]

dense packet-supported clusters and a remainder `X_0` with an injective
defect-to-packet assignment.

The reservoir has

\[
                         |R|=\Omega(W/r^{1/4}),            \tag{4.9}
\]

so its packet count exceeds both the number of singleton defects and the
dense-cluster count by polynomial factors at the relevant scales.  The
remaining issue is not scalar capacity.

## 5. Exact sufficient mesoscopic absorber interface

The following three properties would turn the decomposition into a full
absorption theorem.

1. **Exceptional-set protection.**  The main cover-down covers every
   resource of `Z`, so its terminal leave lies in `V(R)-Z`.
2. **Singleton incidence tickets.**  Every edge of the Hall matching for
   `X_0` lifts to a literal two-phase packet/C14 buffer, and distinct
   assigned reservoir packets give resource-disjoint buffers.
3. **Dense packet clusters.**  Every pair `(C,e)` with
   `C subset e`, `|C|>delta`, has an accepting whole-packet trade, or the
   peeling can be chosen so that `C=e`; the `t` resulting trades admit a
   resource-disjoint selection.

Under these three properties, every leave satisfying (4.7) is absorbed:
use the dense trades on the `C_i` and the Hall matching on `X_0`.

The current theorems prove neither property 1 nor properties 2--3 at the
mesoscopic scale.  The deterministic anchored-fan theorem proves property
2 only for `O(sqrt r)` prescribed anchors.  The complete-bipartite owner
absorber handles a whole owner block but not an arbitrary partial cluster
and is not automatically q1/named-target neutral.

For pure pull decorations, property 3 is now known to be false for an
arbitrary named-occurrence cluster.  The pull-run toggle theorem proves
that one omitted coordinate run `I` changes exactly the principal interval
ideal

\[
                         \mathcal T(I)=\{J:J\subseteq I\}. \tag{5.1}
\]

Its exact Mobius inverse forces every one-phase Boolean support to be a
downset in the cyclic-interval containment poset.  Even the set of all
proper intervals except one singleton is not toggleable.  Thus “dense” is
not the right physical invariant: dense clusters must be refined into
ideal-shaped pull clusters, or handled by a richer non-pull actuator.

Thus the decisive scale bridge is now an exact, checkable statement:

> construct a cover-down whose leave avoids `Z` and whose dense clusters
> are unions of legal pull ideals, or build a richer chain-contracted
> absorber for the `O(W/r^(3/4))` nonideal clusters.

Arbitrary mesoscopic Hall is false from aggregate near-linearity alone;
the dispersed-leave invariant plus dense-cluster absorption is the
strongest conclusion supported by the present packet reservoir.
