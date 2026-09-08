# Audit of the dynamic geodesic-orbit TRP step

Date: 2026-07-25

Pure mathematics only.  No computation, web input, or fixed-rank matching
theorem is used.

## 0. Verdict

The geodesic-orbit calculation in
`MATH_ATTACK_GEODESIC_ORBIT_TRP_OVERLAP_PRUNING_20260725.md` proves a
strong **initial static** overlap census.  It does not prove hereditary
control through a wasteful nibble.

There are two precise failures.

1. The exact covariance multiplier in one bite is

   \[
    (1-p)^{-|\Gamma(e)\cap\Gamma(f)|},               \tag{0.1}
   \]

   where \(\Gamma(e)\) is the conflict neighbourhood of \(e\).  It is not
   obtained by simply substituting the current density into the initial
   owner-intersection series.

2. Even under ideal independent vertex thinning, geodesic endpoint links
   do not all concentrate multiplicatively.  A distance-two endpoint link
   splits into four equal blocks, one for each geodesic midpoint.  At
   density \(z=o(1)\), with probability \((1-z)^4=1-o(1)\) every midpoint
   is absent and the whole residual link is zero.  Conditional on a
   midpoint surviving, the expected block is larger than its unconditional
   trajectory by scale \(1/z\).  Thus no product-residual theorem asserting
   simultaneous relative concentration of all links can hold, and the
   static moments alone cannot imply such concentration for the nibble.

This does not refute an owner near-factor.  The bad distance-two link has
only \(O(D/m^4)\) initial mass, versus \(O(D/m^2)\) for a distance-one
link.  A one-sided, distance-stratified **aggregate energy** argument may
still close.  Such an argument is not present in the manuscript.

Consequently the owner matching and coefficient-one conclusion remain
conditional.  The flag step cannot yet be invoked.  Moreover, its
depth-one part is not a free hidden decoration: it is already forced by
the selected geodesic support.

## 1. Exact one-bite covariance

Regard each carrier-copy tag as a vertex, so a chunk edge has one tag and
\(\ell\) owners.  In a current residual hypergraph \(G\), mark every edge
independently with probability

\[
 p={h\over rD},\qquad r=\ell+1.                     \tag{1.1}
\]

Put

\[
 \Gamma(A)=\{g\in G:g\cap A\ne\varnothing\}.
\]

Let \(I_e\) be the event that no marked edge meets \(e\).  Directly from
independence of the edge marks,

\[
 \Pr(I_e=1)=(1-p)^{|\Gamma(e)|},                     \tag{1.2}
\]

and

\[
 \boxed{
 {\Pr(I_e=I_f=1)\over\Pr(I_e=1)\Pr(I_f=1)}
 =(1-p)^{-|\Gamma(e)\cap\Gamma(f)|}.}                \tag{1.3}
\]

If current degrees are at most \((1+\epsilon)D\) and current pair
codegrees are at most \(\Delta _2\), then

\[
 \begin{aligned}
 |\Gamma(e)\cap\Gamma(f)|
 &\le\sum_{x\in e}\sum_{y\in f}d(x,y)\\
 &\le(1+\epsilon)|e\cap f|D+r^2\Delta _2.           \tag{1.4}
 \end{aligned}
\]

Here \(d(x,x)=d(x)\).  Therefore, writing
\(\Delta _2=\delta D\),

\[
 (1-p)^{-|\Gamma(e)\cap\Gamma(f)|}
 \le
 \exp\left\{(1+o(1)){h\over r}|e\cap f|
                  +O(hr\delta)\right\}.             \tag{1.5}
\]

The geodesic static hierarchy controls the first term at time zero.  To
reuse (1.5) at the next bite one must already know current degree and
pair-link bounds.  This is the circular step omitted between Sections 7
and 9 of the attacked note.

## 2. Static moments acquire an extra density factor

The failure is visible even in independent vertex thinning.  Retain every
tag and owner independently with probability \(z\), and condition on one
edge \(P\) being retained.  If another edge \(F\) shares \(k\) owners with
\(P\) and has a different tag, then \(F\) has \(r-k\) vertices outside
\(P\).  Hence

\[
 \Pr(F\text{ retained}\mid P\text{ retained})=z^{r-k}.  \tag{2.1}
\]

A one-vertex residual degree has trajectory \(Dz^{r-1}\).  Thus the
normalized contribution of this pair is inflated by

\[
 z^{r-k}/z^{r-1}=z^{-(k-1)}.                         \tag{2.2}
\]

In particular, a residual edgewise overlap enumerator is not bounded by
the initial \(\mathcal K_z\) with no further work.  Even at the level of
expectations there is a common extra factor \(z^{-1}\) relative to a
series whose weights begin with \(z^{-(k-2)}\).

At the proposed terminal density \(z=1/\log m\), this missing factor is
only \(\log m\), and the geodesic numerical ledger still has ample room:

\[
 {\ell^2\log m\log\log m\over m^2}=o(1).             \tag{2.3}
\]

So (2.2) is a proof defect, not a numerical obstruction.  Concentration
and propagation remain to be established.

## 3. Exact four-midpoint failure of link concentration

Choose distance-two owners

\[
 X_2=X_0-\{a_1,a_2\}+\{b_1,b_2\}.
\]

There are exactly four Johnson-geodesic midpoints

\[
 Z_{ij}=X_0-a_i+b_j,\qquad i,j\in\{1,2\}.            \tag{3.1}
\]

Every monotone geodesic support containing \(X_0,X_2\) two phases apart
contains exactly one \(Z_{ij}\).  The four choices have equal link size:

\[
 d(X_0,X_2,Z_{ij})={1\over4}d(X_0,X_2).              \tag{3.2}
\]

This follows either by the two orders of the departing coordinates and
the two orders of the arriving coordinates, or directly from the
coordinate stabilizer of \((X_0,X_2)\).

Now independently retain vertices at density \(z\), conditioning on
\(X_0,X_2\) being retained.  Let \(Y_z\) be their residual link degree.
If all four vertices in (3.1) are absent, then

\[
 Y_z=0.                                               \tag{3.3}
\]

Consequently

\[
 \Pr(Y_z=0\mid X_0,X_2\text{ retained})
 \ge(1-z)^4.                                         \tag{3.4}
\]

For \(z=1/\log m\), the right side tends to one.  On the other hand,

\[
 \mathbb EY_z=d(X_0,X_2)z^{r-2},                    \tag{3.5}
\]

which is enormous on the scalar entropy ledger.  Hence

\[
 {Y_z\over\mathbb EY_z}\not\longrightarrow1
\]

even in probability.  Uniform multiplicative concentration of all pair
links is therefore false in the friendlier independent-thinning model,
and cannot be used as an unproved property of the wasteful nibble.

The same calculation appears in the conditional overlap second moment.
For the endpoint core \(A=\{X_0,X_2\}\), two uniformly chosen edges of
its link use the same midpoint with probability \(1/4\).  Thus

\[
 {1\over d(A)^2}
 \sum_{e,f\supset A}
 \left(z^{-| (e\cap f)\setminus A|}-1\right)
 \ge {1\over4}(z^{-1}-1).                            \tag{3.6}
\]

This diverges at the proposed terminal density.  Equation (3.6) is the
precise conditional hierarchy which the static edgewise estimate does not
control.

## 4. Why the example does not yet kill the owner lane

The endpoint link in Section 3 is far below the maximum pair scale.  The
geodesic endpoint identity gives

\[
 {d(X_0,X_s)\over D}
 ={2(\ell-s)\over\ell\binom ms^2}.                   \tag{4.1}
\]

Thus distance one has scale \(D/m^2\), while distance two has scale
\(D/m^4\).  Losing a constant fraction of a distance-two link, or
inflating it by \(1/z\), still leaves it below the distance-one scale for
\(z\ge1/\log m\).

This shows exactly why the missing theorem must be one-sided and
distance-sensitive.  It is unnecessary, and impossible, to keep every
small link close to its mean.  What is needed is an aggregate statement
which permits the four-midpoint fluctuation but keeps its total mass
negligible.

One possible sufficient gate is the following.  For every bite, after
discarding \(o(|R_t|)\) exceptional owners:

1. surviving owner and tag degrees are \((1+o(1))D_t\);
2. distance-one pair links are at most
   \((1+o(1))D_t/(z_tm^2)\);
3. for every \(s\ge2\), the total squared mass of distance-\(s\) links is
   bounded by its thinned orbit trajectory, with the allowed factors
   \(z_t^{-O(s)}\); and
4. the analogous exponentially weighted **aggregate** common-core energy
   is \(o(1/(r\log\log m))\).

The natural energy for item 3 is

\[
 \mathcal E_{s,t}
 ={1\over |R_t|D_t^2}
   \sum_{d_J(X,Y)=s}d_t(X,Y)^2.                       \tag{4.2}
\]

Initially, the number of distance-\(s\) neighbours of one owner is
\(\binom ms^2\), while (4.1) has the reciprocal squared denominator.
Therefore

\[
 \mathcal E_{s,0}
 =O\left({1\over\binom ms^2}\right),                 \tag{4.3}
\]

up to the harmless rank normalization.  The four-midpoint instability at
\(s=2\) is multiplied by the already small factor \(m^{-4}\).

No recurrence proving (4.2)--(4.3) after
\(\Theta((r/h)\log\log m)\) adaptive bites is supplied in the attacked
note.  Proving it requires a three-edge orbit census: for a fixed core
\(A\), one must count pairs \((e,f)\) in its link according to
\(|(e\cap f)\setminus A|\).  The two-edge moments \(\Psi_j(P)\) do not
contain this information.

## 5. Exact status of the owner conclusion

The following parts of the geodesic construction survive the audit:

* rotor realizability of every monotone geodesic support;
* exact tag and owner regularity at time zero;
* exact endpoint codegrees;
* the static overlap hierarchy;
* scalar entropy after geodesic pruning; and
* the reset and remainder ledgers.

The implication

\[
 \text{static hierarchy}\Longrightarrow
 \text{hereditary residual hierarchy}               \tag{5.1}
\]

is not proved and is false if “hierarchy” includes multiplicative
concentration of every link.  Hence an owner matching with \(o(W)\) leave
is not yet established.  It remains plausible only through the aggregate
energy route in Section 4.

## 6. The hidden flag decoration cannot yet be pushed

Even if the owner energy theorem were proved, a selected geodesic support
does not leave all flag rows free for postprocessing.  Its depth-one bridge
flags are forced.

For the geodesic transition

\[
 X_{t+1}=X_t-a_{t+1}+b_{t+1},                        \tag{6.1}
\]

every rotor realization has the rank-\((m-1)\) and rank-\((m+1)\) bridge
masks

\[
 L_{1,t}=X_t\cap X_{t+1}=X_t-\{a_{t+1}\},            \tag{6.2}
\]

\[
 U_{1,t+1}=X_t\cup X_{t+1}=X_t+\{b_{t+1}\}.          \tag{6.3}
\]

The choices of the initial upper queue in \(R\) and of the last delayed
departures in \(C\) cannot change (6.2)--(6.3).  Therefore an owner-only
matching can select two disjoint owner chunks whose transitions reuse the
same facet or cofacet, and no later hidden-state decoration can repair that
duplication.  Only the \(O(1)\) flags at a reset boundary retain extra
initial-state freedom; the \(\ell-1\) interior depth-one bridges are fixed
by the owner path.

By coordinate symmetry, for a fixed middle owner \(X\) and a prescribed
facet \(S\subset X\) or cofacet \(T\supset X\), the depth-one vertical
ratios retain the scale

\[
 {d(X,S)\over d(X)}={1+o(1)\over m},
 \qquad
 {d(X,T)\over d(X)}={1+o(1)\over m}.                 \tag{6.4}
\]

Under the calibrated priority load, a decorated chunk has mean protected
rank

\[
 k_\ell=(\sqrt\pi+o(1))\ell\sqrt m.                 \tag{6.5}
\]

Thus an ordinary decorated-edge nibble has

\[
 k_\ell^2{\Delta _2^{\rm aug}\over D}
 \ge(\pi+o(1))\ell^2,                                \tag{6.6}
\]

and an owner-scale bite sees flag-conflict load

\[
 {k_\ell\over\ell}=(\sqrt\pi+o(1))\sqrt m.          \tag{6.7}
\]

The geodesic restriction does not alter these scales.  It also does not
remove the upper-star concentration caused by the common arrival
coordinate.  Hence the flag problem must be incorporated into the support
selection itself, at least for depth one; it cannot be postponed to a
hidden decoration after an owner matching.

## 7. Correct frontier

The geodesic orbit is a strong static pruning, but the current proof stops
at the following two gates.

1. **Owner gate:** prove a distance-stratified aggregate link-energy
   recurrence through the adaptive wasteful nibble.  Uniform relative
   concentration of all links is impossible by (3.4)--(3.6).
2. **Flag gate:** select geodesic supports while simultaneously controlling
   the forced depth-one facets/cofacets and the higher upper-star fibres.
   Hidden rotor choices can address only the genuinely unforced higher
   decorations.

Until the first gate is proved there is no owner near-factor theorem to
decorate.  Even after it is proved, the second gate is a joint selection
problem rather than a post hoc decoration problem.
