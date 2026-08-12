# A private-phase stationary trace cone and the exact two-guard root address

Date: 2026-08-01  
Status: unconditional sufficient construction, unconditional necessary
concavity and bridge-threshold cuts, and an exact rooted obstruction.  The
unrooted inclusion of the triangular binomial vector in this cone for
arbitrary `d` is open.  Its proposed simultaneous ordered-singleton root is
impossible for every odd `k>=7`.  Small remote probes are evidence only and
are explicitly separated from the theorems.

## 0. Motivation

Let `n=d+1`.  A stationary trace with almost `d` marked proper suffixes per
owner must cover its owner in `n` letters while keeping almost every
shorter suffix proper.  The following model enforces this literally and
turns the marked-trace question into a finite cyclic set-pattern polytope.

It also explains the occurrence semantics of the two folded-C8
antidiagonals: one antidiagonal is a two-sided visit to the
ordered-singleton de Bruijn state.  Two distinct equal-rank guards cannot
both be supplied at one occurrence.  The obstruction is not merely the two
immediate letters: it follows from the inclusion chain of all interval
unions with one fixed endpoint, and therefore also covers longer exterior
collars realizing the same exact target banks.

## 1. Private-phase cyclic words

Fix a rank-`r` owner `T`, put `n=d+1`, and assume `r>=n`.  Choose distinct
private coordinates

\[
                         p_0,\ldots,p_{n-1}\in T.     \tag{1.1}
\]

For every remaining coordinate `x`, choose a nonempty phase pattern

\[
                         P_x\subseteq\mathbb Z_n.     \tag{1.2}
\]

Define the cyclic word

\[
 B_i=\{p_i\}\cup
       \{x\in T\setminus\{p_0,\ldots,p_{n-1}\}:i\in P_x\}
       \qquad(i\in\mathbb Z_n).                       \tag{1.3}
\]

For a cyclic interval `I subset Z_n`, write

\[
                         U(I)=\bigcup_{i\in I}B_i.    \tag{1.4}
\]

### Theorem 1.1 (private-phase trace circulation)

Every `n`-window of (1.3) has union `T`.  Every proper cyclic interval has
union strictly below `T`; moreover, along any growing interval its union
rank increases strictly at every step.

Choose a phase `i` uniformly and use

\[
                 e_i=(B_i,B_{i+1},\ldots,B_{i+d})
                 \qquad(\text{indices modulo }n)     \tag{1.7}
\]

as an order-`d` trace edge.  Mark any chosen subset of its `d` proper
suffix unions.  This is an owner-local marked-trace circulation.

After averaging over all bijections of `T` and all rank-`r` owners, its
rank histogram belongs to `ST_(k,r,d)`.

#### Proof

Every extra coordinate has a nonempty phase pattern, so it occurs in the
full cycle; every private coordinate occurs in its own phase.  Hence the
full union is `T`.

A proper phase interval omits some phase `i` and therefore omits the private
coordinate `p_i`.  It is proper.  When a phase `i` is added to a growing
interval, the new coordinate `p_i` was absent before, so the union grows
strictly.

The tail of the phase-`i` trace is the head of the phase-`i-1` trace.
Uniform phase is consequently a directed cycle measure and has zero
literal de Bruijn boundary.  Coordinate and owner averaging gives the
required invariant circulation. \(\square\)

### The private-pattern cone

For a fixed pattern configuration `P=(P_x)`, define

\[
 g_s(P)=\frac1n
 \#\{(i,j):i\in\mathbb Z_n,\ 1\leq j<n,
        |U([i-j+1,i])|=s\}.                           \tag{1.5}
\]

All suffixes can be marked, so `sum_s g_s(P)=d`.  Given a desired vector
below a convex combination of these profiles, independently retain each
marked rank-`s` suffix with the appropriate rank-dependent probability
(with probability zero if its available mass is zero).  This selective
marking shows that the coordinatewise downward closure of

\[
 \operatorname{conv}\{g(P):P\text{ satisfies (1.2)}\}                \tag{1.6}
\]

is contained in `ST_(k,r,d)`.  Thus proving that the triangular vector `q`
lies in (1.6), or below a point of (1.6), is a concrete sufficient
all-`k` theorem.  It is stronger than general `ST` membership because it
uses one fixed owner and a period exactly `d+1`.

The model has only `2^(d+1)-1` possible extra-coordinate types.  A type is
an occurrence pattern, not a trace edge; arbitrary multiplicities with
total `r-d-1` are allowed.

## 2. Missing-set and graph coordinates

For a suffix interval `I`, a coordinate is missing from `U(I)` precisely
when its pattern is disjoint from `I`.  Hence

\[
 r-|U(I)|
 =|\mathbb Z_n\setminus I|
  +\#\{x:P_x\cap I=\varnothing\}.                    \tag{2.1}
\]

The first term consists of the omitted private coordinates.

A useful quadratic submodel assigns every extra coordinate either to all
phases or to an unordered phase pair, identified with an edge of a graph
`G` on `Z_n`.  If the omitted complement interval is `J`, then

\[
                         r-|U(I)|=|J|+e_G(J).          \tag{2.2}
\]

Thus its deficiency histogram is the cyclic induced-edge profile

\[
 \frac1n\#\{(i,m):m+e_G([i,i+m-1])=t\}.              \tag{2.3}
\]

Pair patterns alone are not universal: exact remote LP probes find this
subcone sufficient for the first `d=3` cases `k=11,13`, but not from
`k=15` onward.  Allowing all nonempty patterns of size at least two restores
feasibility in the same probe for every actual `d=3` instance
`11<=k<=22`.  These finite floating-point probes are not proofs and are not
used elsewhere in this note.  Their only safe conclusion is architectural:
higher occurrence patterns are load-bearing, while the full
private-pattern cone remains a plausible strict sufficient class.

### The bridge-threshold cuts

Put `n=d+1`, write `h_t(P)=g_(r-t)(P)`, and, for a cyclic complement
interval `J`, put

\[
 N_P(J)=\#\{x:P_x\subseteq J\},\qquad
 D_P(J)=|J|+N_P(J).
\]

For `1<=a<=d`, define

\[
 Z_a(P)=\#\{J:1\le |J|\le a,\ D_P(J)>a\}.
\]

There are `na` cyclic intervals of lengths at most `a`, and every interval
of deficiency at most `a` is among them.  Therefore

\[
 \boxed{a-\sum_{t=1}^a h_t(P)=\frac{Z_a(P)}n.}       \tag{2.4}
\]

If a distribution on configurations has mean profile dominating the
triangular vector, bridge reflection gives the necessary cuts

\[
 \boxed{
 \mathbb E Z_a\le n\left(\mathbb E(a-M)_+
              +\frac1W\sum_{t=1}^a b_{r-t}\right),} \tag{2.5}
\]

where `M` is the maximum of the length-`k` bridge ending at `k mod 2`.
Indeed `q_(r-t)=Pr(M>=t)-b_(r-t)/W`, and the sum of the first `a`
survival probabilities is `E min(M,a)`.  These cuts are exact necessary
consequences of the bridge marginal; they do not construct the joint cyclic
patterns.

At `a=1`, if `c_1(P)` counts phases carrying at least one singleton extra
pattern, (2.4) becomes

\[
                 g_{r-1}(P)=1-\frac{c_1(P)}n.        \tag{2.6}
\]

For odd `k=2r-1` with `d<r-1`, the boundary board does not puncture this
rank and `q_(r-1)=1`.  Hence every configuration in a dominating measure
has `c_1(P)=0`.  This top-face equality will obstruct the singleton root in
Section 5.

## 3. A necessary stationary concavity law

The following applies to every stationary trace law, not only (1.3).

Let

\[
 R_j=\left|\bigcup_{h=0}^{j-1}B_{-h}\right|,
 \qquad R_0=0,
 \qquad \Delta_j=\mathbb E(R_j-R_{j-1}).             \tag{3.1}
\]

### Theorem 3.1 (mean first-occurrence concavity)

For every stationary cyclic set process,

\[
                 \Delta_1\geq\Delta_2\geq\cdots.    \tag{3.2}
\]

In particular, if every `(d+1)`-window has rank `r`, then

\[
 \mathbb E R_j\geq\frac{jr}{d+1},
 \qquad
 \sum_{j=1}^d\mathbb E R_j\geq\frac{rd}{2}.          \tag{3.3}
\]

#### Proof

Fix a coordinate and inspect its cyclic binary incidence word.  It is
newly discovered when the window is extended from length `j-1` to `j`
exactly when the new endpoint is a `1` preceded toward the present endpoint
by at least `j-1` zeros.  Equivalently, each zero gap of length `ell`
contributes one discovery at every distance `1,...,ell+1`.  The number of
gaps of length at least `j-1` is nonincreasing in `j`.  Sum this statement
over coordinates and average the root phase to obtain (3.2).

The increments sum to `r` through time `d+1`.  A nonincreasing nonnegative
sequence with this sum majorizes the constant sequence
`r/(d+1)`, proving the first inequality in (3.3).  Summing it over `j`
proves the second. \(\square\)

If all `d` suffixes are marked, their aggregate first rank moment must
therefore obey

\[
                         \sum_s s q_s\geq rd/2.       \tag{3.4}
\]

With unmarked mass `epsilon=d-sum_s q_s`, one only obtains the robust
interval

\[
 \sum_s s q_s+\varepsilon
 \leq \sum_{j=1}^d\mathbb E R_j
 \leq \sum_s s q_s+r\varepsilon.                    \tag{3.5}
\]

The triangular binomial profile is on the permitted high-rank side of
(3.3); this is not a refutation.  The theorem is nevertheless a sharp
warning that `ST_(k,r,d)` is strictly smaller than the uniform-matroid rank
polytope: arbitrary depthwise rank marginals need not have a stationary
trace lift.

## 4. Exact singleton-root and cross-bank addresses

Let

\[
 v=(\{f_1\},\ldots,\{f_d\})                           \tag{4.1}
\]

be an ordered-singleton de Bruijn state and put `F={f_1,...,f_d}`.  Let
`G` be a nonempty guard disjoint from `F`, with `|G|=r-d` when the two
incident trace edges are required to have owner rank `r`.  A two-sided
traversal

\[
                    G,\{f_1\},\ldots,\{f_d\},G       \tag{4.2}
\]

through `v` exposes, for every `1<=j<d`, two disjoint physical interval
cells

\[
 P_G(j)=G\cup F[1,j],
 \qquad
 S_G(j+1)=G\cup F[j+1,d].                            \tag{4.3}
\]

They satisfy

\[
 P_G(j)\cap S_G(j+1)=G,
 \qquad
 P_G(j)\cup S_G(j+1)=G\cup F                         \tag{4.4}
\]

independently of `j`.  Thus (4.2) is a literal occurrence-level realization
of one constant-cap antidiagonal, not merely a target-value identity.

### Proposition 4.1 (two equal-rank guards require two root visits)

A single occurrence of the state `v` cannot supply two exact antidiagonal
banks (4.3) with distinct equal-rank constant intersections
`G_1!=G_3`.

They are supplied by two visits

\[
 G_1,v,G_1,
 \qquad
 G_3,v,G_3.                                          \tag{4.5}
\]

In a fractional circulation these may be two directed branches through the
same literal state `v`; after denominator clearing, an Euler circuit visits
`v` twice.  Hence **positive two-guard throughput at the same
ordered-singleton state** is the correct strengthening of the boundary-root
criterion for these exact banks.

#### Proof

Equations (4.3)--(4.4) are direct interval unions.  Suppose one occurrence
supplied the two exact banks for `G_1` and `G_3`.  At `j=1`, their prefix
cells would be

\[
                     G_1\cup\{f_1\},\qquad
                     G_3\cup\{f_1\}.                 \tag{4.6}
\]

Both are interval unions ending at the same physical occurrence
`{f_1}`.  All interval unions with a fixed right endpoint form an inclusion
chain as their left endpoint moves left.  The two sets in (4.6) have the
same rank and are distinct, because the guards are equal-rank, distinct and
disjoint from `F`.  Two such sets cannot lie in one inclusion chain.  This
contradiction proves that the banks require distinct visits.  The same
argument could instead use the two suffix cells with fixed left endpoint
`{f_d}`.  Conversely, each visit in (4.5) supplies its bank by (4.4).
\(\square\)

For fixed `F` and fixed rank-`r` owner `T`, the guard is uniquely
`T\setminus F`.  Thus distinct `G_1,G_3` belong to distinct owner fibres
sharing the same literal state `v`.

There is also a small Euler qualification.  Let a rational balanced
circulation have weakly connected positive support and positive weight on
the incoming and outgoing edge for each guard.  Clear denominators and
multiply further so that, after reserving one copy of each of the four
guard edges, one untouched copy of every support edge remains.  Contract
each prescribed incoming--outgoing guard pair to one macroedge.  The
contracted multigraph is balanced and remains weakly connected, hence has
an Euler circuit.  Expanding the macroedges gives both same-guard visits.
Thus connected positive two-sided throughput is sufficient at repeated
fractional scale.  At minimum multiplicity a figure eight may force the
two guards to be cross-paired, so this argument does not imply one-copy
coloured rounding.

There is a categorical literal one-copy obstruction.  The incoming and
outgoing trace edges of `G,v,G` are distinct, but both have owner
`F\cup G`.  An integral owner-perfect trace selects exactly one edge of
that owner and therefore cannot retain even one complete immediate
same-guard passage.  For two guards the duplication occurs independently
in the two owners.  The repeated fractional bank can enter a physical
construction only through an auxiliary boundary/uncoloured layer, an owner
puncture, or a different address geometry.

This resolves the address semantics but not the common-cap compiler:
the two visits consume distinct physical cells, must coexist with the
background occurrence matching, and cannot survive literal
one-owner-per-colour rounding in this geometry.  A generic connected
circulation meeting `v` once does not imply the two-guard condition.

## 5. The root-enhanced target is false on the odd top face

The order-one theorem settles `q in ST_(k,r,1)` completely.  In general,
the unrooted private-pattern question remains:

> Find a probability distribution on `r-d-1` nonempty occurrence patterns
> in `Z_(d+1)` such that the expected cyclic interval-union histogram
> dominates the triangular vector `q`.

This is a finite convex-hull problem with exact integer generators (1.5).
Bridge reflection supplies the cuts (2.5), but not their sufficiency.

The earlier proposal to append positive ordered-singleton root mass to this
same distribution is false throughout the odd family.  Suppose
`R=r-d-1>0` and a private period-`d+1` configuration contains

\[
                         G,\{f_1\},\ldots,\{f_d\},G. \tag{5.1}
\]

The `d` singleton letters occupy all but the guard phase.  Every extra
coordinate must therefore have the singleton pattern consisting of that
guard phase.  Thus `c_1(P)=1` and

\[
                         g_{r-1}(P)=\frac d{d+1}<1.  \tag{5.2}
\]

For odd `k=2r-1`, `q_(r-1)=1` whenever `d<r-1`, so (5.2) cannot occur with
positive probability in a dominating measure.  Every actual odd `k>=7`
has `d<=r-2`: for `r=4`, `Lambda/W=63/35<2`, while for `r>=5`

\[
 \frac\Lambda W
 \le 1+(r-2)\frac{r-1}{r+1}\le r-2,
\]

and `d<=ceil(Lambda/W)`.

The obstruction is stronger than the private model.  In the full marked
trace LP, one atom has at most one marked rank-`(r-1)` suffix because its
marked suffix sets are nested and distinct.  When `q_(r-1)=1`, every
positive atom must attain that cap.  An edge entering the singleton state
`v` has proper suffix ranks only `1,...,d`, so for `d<r-1` its weight is
zero; literal balance also makes every outgoing weight at `v` zero.

For even `k=2r` with `b_(r-1)=0`, `q_(r-1)=r/(r+1)`.  The same calculation
only bounds the total private root-configuration mass by
`(d+1)/(r+1)`; it does not exclude positive mass.

Thus unrooted cone membership remains open, but the joint all-`k`
singleton-root/two-guard target is exactly refuted.  One must puncture the
top face, decouple the absorber, or replace `v` by a root state already
exposing a rank-`(r-1)` suffix.  Connected unrooted support, common-cap
compatibility, and a different one-copy root/address realization remain
logically distinct.
