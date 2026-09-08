# Edge-transitive reduction for one augmented geodesic template

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Coordinate symmetrization has one exact use in the coefficient-one problem.
For a **fixed augmented multirank template**, every weighted residual cut in
its coordinate orbit is equivalent, with no extra loss, to the single
unweighted matching ratio of the full orbit.

This does not make the matching ratio automatic.  For the middle-only
wreath template it is already one, because an exact middle wreath factor is
known.  For an augmented geodesic template, lower and upper protected
targets are additional vertices, and the corresponding full-orbit packing
is precisely an unproved multirank design theorem.

## 1. General orbit hypergraph

Let a finite group `G` act on a finite vertex set

\[
 V=V_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}V_s
\]

and transitively on every `V_i`.  Fix one template edge `F subset V`, put

\[
 k_i=|F\cap V_i|,
\]

and let `E=G F` be its orbit, with coincident labelled copies retained if
desired.  The group acts transitively on `E`.

### Proposition 1.1 (exact stratum degrees and fractional capacity)

Every vertex of `V_i` has degree

\[
 \boxed{D_i=\frac{|E|k_i}{|V_i|}.}
 \tag{1.1}
\]

Put

\[
 D=\max_iD_i,
 \qquad
 T_*=\min_i\frac{|V_i|}{k_i}=\frac{|E|}{D},
 \tag{1.2}
\]

where empty strata are omitted.  Then `x_e=1/D` is a fractional matching
of value `T_*`, and every integral matching has size at most `T_*`.

#### Proof

Double count incidences between `E` and `V_i`.  Edge transitivity gives
`|E|k_i` incidences, and vertex transitivity distributes them uniformly,
proving (1.1).  Since `D_i<=D`, the constant edge weight `1/D` is a
fractional matching.  Any integral matching uses `k_i` distinct vertices
of `V_i` per edge, so it has size at most `|V_i|/k_i` for every `i`.
Taking the minimum proves (1.2).  \(\square\)

### Proposition 1.2 (lossless residual symmetrization)

Let `nu(H)` be the maximum matching size of the full orbit hypergraph.
For every labelled subcatalogue `E' subset E` and every nonnegative edge
weight `w`,

\[
 \boxed{
 \nu_w(E')\ge\frac{\nu(H)}{|E|}\,w(E').}
 \tag{1.3}
\]

Consequently, if

\[
 \nu(H)\ge(1-\delta)T_*=(1-\delta)\frac{|E|}{D},
 \tag{1.4}
\]

then every weighted residual satisfies

\[
 \boxed{
 \nu_w(E')\ge(1-\delta)\frac{w(E')}{D}.}
 \tag{1.5}
\]

#### Proof

Fix a maximum matching `M_0` of the full orbit and extend `w` by zero
outside `E'`.  For uniform `g in G`, every fixed member of `M_0` is sent
uniformly over the labelled edge orbit.  Therefore

\[
 \mathbb E_g w(gM_0)
 =\frac{|M_0|}{|E|}w(E').
\]

Some `g` attains at least this value.  Intersecting `gM_0` with `E'`
gives the required residual matching.  Substitute (1.4) to obtain (1.5).
\(\square\)

The converse is immediate from `w=1` and `E'=E`.  Thus within one edge
orbit, the all-weights/all-residuals statement and the unweighted full
matching ratio are exactly equivalent.

Equivalently, the fractional chromatic index of an edge-transitive
multihypergraph has the exact closed form

\[
 \boxed{
 \chi_f'(H)
 =\sup_{w\ge0}{w(E)\over\nu_w(H)}
 ={|E|\over\nu(H)}.}
 \tag{1.5a}
\]

The first equality is the standard matching-cover LP dual, while the
second follows from (1.3) and is attained by the constant weight.

### Proposition 1.3 (exact pair-orbit codegrees)

Let `R` be one orbit of ordered pairs of distinct vertices under `G`, and
let

\[
 j_R(F)=|\{(x,y)\in F^2:(x,y)\in R\}|.
\]

Then every ordered pair `(x,y) in R` has codegree

\[
 \boxed{\operatorname {codeg}(x,y)
       ={ |E|j_R(F)\over |R|}.}
 \tag{1.6}
\]

The same statement holds for ordered `a`-tuples, with the number of
template `a`-tuples in the numerator and the ambient tuple-orbit size in
the denominator.

#### Proof

Count pairs consisting of an orbit edge and an ordered vertex pair from
`R` contained in that edge.  Edge transitivity gives `|E|j_R(F)` such
incidences.  Pair-orbit transitivity distributes them uniformly over
`R`.  The tuple statement is identical. \(\square\)

For the full symmetric group on Boolean ranks, an ordered pair consisting
of an `r`-set and an `s`-set is determined by

\[
 t=|S\cap T|.
\]

Its orbit has size

\[
 \binom nr\binom rt\binom{n-r}{s-t}.
 \tag{1.7}
\]

If `J_{r,s,t}(F)` is the number of ordered protected pairs of this profile
inside the template, then

\[
 \boxed{
 \operatorname {codeg}(S,T)
 ={ |E|J_{r,s,t}(F)\over
    \binom nr\binom rt\binom{n-r}{s-t}}.}
 \tag{1.8}
\]

Relative to the degree of an `r`-target this is

\[
 \boxed{
 {\operatorname {codeg}(S,T)\over D_r}
 ={J_{r,s,t}(F)\over
   k_r\binom rt\binom{n-r}{s-t}}.}
 \tag{1.9}
\]

These formulas include stabilizers automatically; no freeness assumption
on the template is needed.

### Proposition 1.4 (root--target and rooted tuple codegrees)

Suppose the tag is a rooted carrier `(U,j)`, with `|U|=M`, and every
Boolean target in the template lies inside `U`.  For a compatible
`r`-target `S subset U`,

\[
 \boxed{
 \operatorname {codeg}((U,j),S)
 =D_{\rm tag}{k_r\over\binom Mr}.}
 \tag{1.10}
\]

More generally, if `S,T subset U` have ranks `r,s` and intersection `t`,
then

\[
 \boxed{
 \operatorname {codeg}((U,j),S,T)
 =D_{\rm tag}{J_{r,s,t}(F)\over
  \binom Mr\binom rt\binom{M-r}{s-t}}.}
 \tag{1.11}
\]

#### Proof

There are `T_tag binom(M,r)` compatible ordered tag--target pairs and
`|E|k_r` incidences with orbit edges.  This proves (1.10).  For (1.11),
replace the compatible-pair count by

\[
 T_{\rm tag}\binom Mr\binom rt\binom{M-r}{s-t}
\]

and the incidence count by `|E|J_{r,s,t}(F)`. \(\square\)

## 2. Middle wreaths versus augmented geodesic templates

For `n=2m+1`, take the middle-wreath template consisting of the `n` cyclic
`m`-intervals of one coordinate order.  There is only one vertex stratum,
`|V_0|=binom(n,m)`, and `k_0=n`.  The Mütze--Standke--Wiechert odd-graph
cycle factor gives an exact matching of size

\[
 T_*=\frac1n\binom nm.
\]

The conversion from their cycle factor to wreaths is worth recording
explicitly.  Let

\[
 A_0,A_1,\ldots,A_{n-1},\qquad n=2m+1,
\]

be one \(n\)-cycle in \(KG(n,m)\).  Consecutive sets are disjoint.  For
each \(i\), let \(u_i\) be the unique coordinate outside
\(A_i\cup A_{i+1}\).  For a coordinate \(x\), the index set

\[
 J_x=\{i:x\in A_i\}
\]

is independent in the odd cycle, so \(|J_x|\le m\).  But

\[
 \sum_x|J_x|=\sum_i|A_i|=nm,
\]

and there are \(n\) coordinates.  Hence every \(|J_x|=m\).  The
complement of a maximum independent set in \(C_{2m+1}\) contains exactly
one edge with both endpoints outside the independent set.  Consequently
there is a unique \(i\) with \(x\notin A_i\cup A_{i+1}\), and therefore
\(x=u_i\).  Thus \(i\mapsto u_i\) is a bijection.

Away from its unique consecutive pair of zeroes, the membership word of
\(u_j\) around the cycle alternates.  Therefore

\[
 A_i=\{u_{i-2},u_{i-4},\ldots,u_{i-2m}\}.
\]

Since multiplication by \(-2\) is invertible modulo \(2m+1\), putting
\(\pi_t=u_{-2t}\) shows that the \(A_i\)'s are exactly the cyclic
length-\(m\) intervals of \(\pi\).  Hence every \((2m+1)\)-cycle in the
odd graph is a wreath.  The MSW \(C_{2m+1}\)-factor is therefore an exact
wreath decomposition, not merely an approximate packing.

Hence `delta=0` in (1.4), and (1.5) is unconditional for every residual
of the **middle-only** wreath orbit.  This is useful but does not cover a
lower or upper Boolean rank.

Here are the exact orientation constants.  If directed cyclic orders are
considered modulo rotation and retained as labelled parallel edges, then

\[
 |E^{\to}|=(n-1)!,\qquad
 D^{\to}={n!\over W}=m!(m+1)!,\qquad
 \nu(E^{\to})={W\over n}.
 \tag{2.0a}
\]

The action of `S_n` is transitive on these labelled directed orders.  The
MSW factor is a matching of wreath supports; orienting every selected
wreath arbitrarily gives the last equality in (2.0a), while the middle
capacity bound gives the reverse inequality.

If reversal is also identified, the support orbit has

\[
 |E|={(n-1)!\over2},\qquad
 D={m!(m+1)!\over2},\qquad
 \nu(E)={W\over n}.
 \tag{2.0b}
\]

Thus in either convention

\[
 {\nu(E)\over|E|}={1\over D},
\]

and Proposition 1.2 gives the exact residual constant, with no hidden
factor two.  Using the labelled directed multihypergraph is the safest
way to avoid any support-automorphism ambiguity.

For completeness, when `m>=2` the wreath support determines its cyclic
order up to rotation and reversal.  Indeed, two distinct coordinates at
cyclic distance `d<=m` lie together in exactly `m-d` of the `m`-windows.
Hence the pairs of maximum co-occurrence `m-1` are precisely the adjacent
pairs of the underlying cycle.  This reconstructs the undirected cyclic
order and justifies the first count in (2.0b).  The case `m=1,n=3` is
immediate.

Consequently the following weighted statement is already unconditional.
For every labelled residual family `C` of directed cyclic orders and every
nonnegative weight `w`, there is a subfamily whose middle wreaths are
pairwise disjoint and whose weight is at least

\[
 \boxed{
 {1\over m!(m+1)!}\sum_{\pi\in C}w_\pi.}
 \tag{2.0c}
\]

For unoriented wreath supports the exact coefficient is
`2/[m!(m+1)!]`.  This is the middle-only weighted residual hypothesis in
closed form; it ceases to be known after protected lower and upper targets
are included in the edge intersections.

Now fix one legal bounded-displacement geodesic chunk template, including:

1. its carrier/tag vertex;
2. its `g` middle owners;
3. its calibrated protected lower and upper targets in every signed depth
   through `Q`.

Take all coordinate relabellings.  The resulting augmented orbit has one
vertex stratum for the tag type and one for each protected Boolean rank.
The calibration chooses the numbers `k_i` so that every active capacity
ratio `|V_i|/k_i` is at least the tag count `T`.  Equivalently every
target degree is at most the tag degree.  The aggregate floor, cap, and
deadline deficits are `o(W)`, but this does **not** imply the stronger
pointwise estimate `D_i=(1+o(1/Q))D`; for the middle-owner row its relative
deficit is only audited as `O((H+g)/m)`.

Therefore the single orbit-level theorem

\[
 \boxed{
 \nu(H_{\rm geo})\ge T-o(T/Q)}
 \tag{2.1}
\]

would imply every weighted residual cut for that orbit with the original
design denominator, and in particular gives one coefficient-safe
geodesic near-factor.

### The exact augmented geodesic ledger

For the audited even-dimensional chunk construction put

\[
 n=2m,\qquad M=m+H,\qquad
 N=\binom{2m}{M},\qquad
 J=\left\lfloor{M\over g}\right\rfloor,
 \qquad T=JN.
 \tag{2.2}
\]

An augmented edge contains one carrier-copy tag, `g` middle owners, and
`\widetilde c_q` protected targets in each of the two signed depth-`q`
rows.  Thus

\[
 k_{\rm tag}=1,\qquad k_m=g,\qquad
 k_{m-q}=k_{m+q}=\widetilde c_q.
 \tag{2.3}
\]

If `D_0` is the tag degree, Proposition 1.1 gives the exact ratios

\[
 \boxed{{D_m\over D_0}={Tg\over W}\le1,\qquad
 {D_{m\pm q}\over D_0}
 ={T\widetilde c_q\over R_q}\le1,}
 \tag{2.4}
\]

where

\[
 W=\binom{2m}{m},\qquad R_q=\binom{2m}{m-q}.
\]

The inequalities are exactly the owner and signed-row calibration.  In
particular

\[
 T_*=\min\left\{T,{W\over g},
       \min_q{R_q\over\widetilde c_q}\right\}=T,
 \tag{2.5}
\]

so the uniform full-orbit fractional matching saturates every tag.

There is a small but essential orbit convention here.  Coordinate
relabeling by `S_n` preserves the formal copy index `j`; it therefore
produces `J` separate edge orbits, each on only `N` tags.  Because the
candidate fibre is identical at every formal copy, one may enlarge the
action to

\[
 S_n\times S_J,
 \tag{2.6}
\]

where `S_J` permutes the copy labels and acts trivially on Boolean
targets.  Only under this enlarged action is the full `T`-tag catalogue a
single edge orbit.  Alternatively, one must keep the `J` coordinate
orbits separate and supply an additional cross-orbit packing argument.

If the abstract protected template on its `M` carrier positions has
automorphism group of order `a`, then the enlarged labelled orbit has

\[
 \boxed{|E|={J(n)_M\over a},\qquad
 D_0={M!\over a}.}
 \tag{2.6a}
\]

When every carrier labelling is deliberately retained as a separate
catalogue occurrence, take `a=1`.  Formula (2.6a) is consistent with all
ratios in (2.4), and makes clear that stabilizers do not create an
additional divisibility loss.

For a fixed template, (1.8)--(1.11) now compute every codegree exactly.
Two important special scales are:

* a same-phase nested adjacent pair has
  `J_{r,r+1,r}<=min(k_r,k_{r+1})`, and hence relative codegree at most
  `1/(n-r)=Theta(1/m)`;
* in a bounded-displacement template, the number of same-rank Johnson
  neighbours of a fixed protected member inside the template is
  `O(1)`, so (1.9) gives relative codegree `O(1/m^2)`.

Thus the full orbit has the same audited hierarchy as the raw catalogue:
the owner--facet correlation is genuinely of order `1/m`; orbit
symmetrization does not remove it.

### Proposition 2.1 (all one-row rooted Hall cuts pass)

Let `A` be any family of carrier-copy tags and let `C` be its family of
distinct carriers.  For every active rank `r`, the union of rank-`r`
targets appearing in orbit edges above `A` has size at least

\[
 k_r|A|.
 \tag{2.7}
\]

Consequently no individual Boolean row supplies a Hall obstruction to a
tag-saturating matching.

#### Proof

Full relabeling implies that every `r`-subset of a carrier occurs in some
orbit edge above that carrier.  Hence the available target union is the
rank-`r` shadow

\[
 \partial_r C=\bigcup_{U\in C}\binom Ur.
\]

Double-counting containments gives

\[
 |\partial_r C|\ge {\binom nr\over\binom nM}|C|.
 \tag{2.8}
\]

There are at most `J` tags above each carrier, so `|A|<=J|C|`.  The
calibration says

\[
 Jk_r\le {\binom nr\over\binom nM}
 \tag{2.9}
\]

for the middle row and for every protected signed row.  Combining
(2.8)--(2.9) proves (2.7). \(\square\)

Proposition 2.1 is deliberately one-row.  Independently chosen row
matchings need not be realizable by one common geodesic trajectory.  The
remaining obstruction is therefore a simultaneous multirank one, not a
scalar capacity or separate-shadow Hall defect.

## 3. What (2.1) does and does not remove

Equation (2.1) is an unweighted packing theorem for copies of one growing
multirank set-system template.  Edge transitivity proves its exact
fractional relaxation but not its integrality.  The abstract random linear
counterexamples show that regularity, `D>>K^2`, consecutive chain
structure, and width-three intersections cannot prove (2.1) without the
common Johnson-geodesic root schedule.

There is also a distinction between one orbit and a union of orbits.
Symmetrization applies losslessly inside each fixed template orbit.  A
catalogue mixing different gap schedules or priority profiles is generally
not edge-transitive; one must either find one orbit satisfying (2.1), or
combine orbit matchings by a separate convex/integral argument.

Finally, (1.5) uses the original full-orbit degree `D`.  It does not replace
`D` by a smaller density-scaled residual degree.  Such a replacement is a
strictly stronger hereditary assertion and is not supplied by symmetry.

No coefficient-one conclusion is claimed: (2.1) remains unproved.

## 4. Final audited verdict

For the middle-only odd wreath orbit, the unweighted matching number is
known exactly and orbit symmetrization therefore solves every weighted
residual cut.

For the augmented geodesic orbit, the exact degrees, all pair codegrees,
the uniform fractional matching, and every separate-rank rooted Hall cut
are now explicit.  None yields a nontrivial obstruction to a matching of
size `T-o(T/Q)`.  Conversely, no theorem currently proves such a matching:
it is exactly the common-trajectory multirank packing gate.  Therefore the
honest conclusion is

\[
 \boxed{
 \text{orbit symmetry removes the weighted-cut quantifier, but it does
 not determine the augmented orbit matching number.}}
 \tag{4.1}
\]

The exact remaining scalar is

\[
 \boxed{\operatorname {gap}(F)=T-\nu(GF).}
 \tag{4.2}
\]

Literal coefficient-safe repair requires `gap(F)=o(T/Q)` for at least one
legal fixed template (or an equally strong structured reserve theorem).
The middle-only MSW theorem proves the analogue with gap zero only after
all protected multirank vertices have been deleted.
