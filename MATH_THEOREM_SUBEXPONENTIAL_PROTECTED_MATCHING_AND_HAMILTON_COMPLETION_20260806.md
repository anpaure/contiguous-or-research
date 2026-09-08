# Subexponential protected matchings extend, and Hamilton anchoring leaves only a subexponential component bank

**Date:** 2026-08-06  
**Method:** Johnson spectral localization, the sharp balanced and
strict-imbalance partial-shadow thresholds, and alternating-cycle insertion;
no computation or search  
**Status:** unconditional asymptotic strengthening of the polynomial
protected-matching and Hamilton-anchored completion theorems.  Their proofs
do not require polynomial protected size.  They work whenever the protected
size is negligible compared with the appropriate sharp shadow threshold;
in particular they work for every `2^{o(r)}` protected bank with a fixed
sub-half exposure margin.  This theorem controls the residual component
count.  It does not itself pack the protected bank, remove common coloured
edges, or install the PBBS payload.

## 1. Setting and the sharp scale

Put

\[
 \mathcal L={ [2r-1]\choose r-1},\qquad
 \mathcal U={ [2r-1]\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|,
\tag{1.1}
\]

and let `G` be their `r`-regular incidence graph.  Let `F` be a matching,
with lower and upper endpoint sets `Z,Y` and size

\[
                         f=|F|=|Z|=|Y|.             \tag{1.2}
\]

Use the all-occurrence exposure parameters

\[
 \widehat\alpha(F)=
   \max_{x\in\mathcal L}|N_G(x)\cap Y|,
 \qquad
 \widehat\beta(F)=
   \max_{U\in\mathcal U}|N_G(U)\cap Z|.             \tag{1.3}
\]

For an ordinary residual matching problem one may replace
`widehat alpha` by the maximum over the residual lower shore.  The stronger
form (1.3) is used below because every prefix of an arbitrary ordering of
`F` then inherits the same bounds.

Put

\[
 D_\alpha=r-\widehat\alpha(F),\qquad
 D_\beta=r-\widehat\beta(F),\qquad
 K(D)={2D-1\choose D}.                               \tag{1.4}
\]

The exact scale condition is

\[
              rf=o\bigl(\min\{K(D_\alpha),K(D_\beta)\}\bigr).
                                                               \tag{1.5}
\]

If, for a fixed `epsilon>0`,

\[
 \widehat\alpha(F),\widehat\beta(F)
       \le(1/2-\epsilon)r                              \tag{1.6}
\]

and `f=2^{o(r)}`, then (1.5) holds because

\[
 K(D_\alpha),K(D_\beta)
       \ge 2^{(1+2\epsilon)r-O(\log r)}.              \tag{1.7}
\]

## 2. Subexponential extension theorem

### Theorem 2.1 (sharp-scale protected matching extension)

If (1.5) holds, then `F` extends to a perfect matching of `G` for all
sufficiently large `r`.

In particular, every matching of size `2^{o(r)}` satisfying (1.6) extends
to a perfect matching.

#### Proof

Delete `Z,Y` and suppose a residual lower shore `A` fails Hall.  The
Johnson spectral-surplus inequality gives

\[
 |N_G(A)|-|A|
 \ge {2r-1\over r^2}{|A|(W-|A|)\over W}.             \tag{2.1}
\]

Hall failure can lose at most the `f` deleted upper vertices.  Therefore,
with `q=min(|A|,W-|A|)`,

\[
                         q<{2r^2\over2r-1}f<2rf.       \tag{2.2}
\]

If the small side is `A`, take an inclusion-minimal failed shore.  Every
member of `A` retains at least `D_alpha` upper neighbours.  The sharp
balanced partial-shadow theorem then gives

\[
                         |A|\ge K(D_\alpha).           \tag{2.3}
\]

Equations (2.2)--(2.3) contradict (1.5).

If the small side is the complement, put

\[
 B=(\mathcal L\setminus Z)\setminus A,
\]

and let `Q` be the residual upper vertices missed by `A`.  Residual-shore
balance gives `|Q|>|B|`.  Each `U in Q` has at least `D_beta` lower facets
in `B`, so the sharp strict-imbalance partial-shadow theorem gives

\[
                         |B|\ge K(D_\beta)+1.          \tag{2.4}
\]

Again (2.2), with the harmless deletion of `f` vertices absorbed into its
right side, says more explicitly

\[
 |B|=W-f-|A|<2rf.                                    \tag{2.5}
\]

This contradicts (1.5).  Thus no residual Hall shore fails, and a
perfect residual matching together with `F` is the required extension.
\(\square\)

The proof is exactly the proof of the polynomial theorem with `r^C`
replaced by `f`.  Polynomiality was used only to make the right side of
(2.2) smaller than the exponential quantities in (2.3)--(2.4); condition
(1.5) is the actual hypothesis.

## 3. Every protected prefix remains elementary

Fix any ordering of the edges of `F`, and let `F_j` be its first `j`
edges.  Delete their endpoints and call the residual graph `B_j`.

### Lemma 3.1 (connected and elementary residuals)

Assume (1.5).  Every `B_j`, `0<=j<=f`, is connected, and every edge of
`B_j` belongs to a perfect matching of `B_j`.

#### Proof

Theorem 2.1 applies to every prefix because its endpoint sets are subsets
of those in (1.3), and `j<=f`.

If `B_j` were disconnected, choose a component with equal lower and upper
shore size `a<=W/2`.  All old neighbours of its lower shore lie in that
component together with the `j` deleted upper vertices.  Applying (2.1)
gives

\[
                         a<2rj\le2rf.               \tag{3.1}
\]

Every lower vertex of the component has at least `D_alpha` neighbours in
its upper shore.  The balanced partial-shadow theorem gives

\[
                         a\ge K(D_\alpha),           \tag{3.2}
\]

contradicting (1.5).  Thus `B_j` is connected.

For an edge `e in E(B_j)`, the protected matching `F_j+e` has size at most
`f+1`; its two exposures increase by at most one.  Replacing `D_alpha` and
`D_beta` by one less changes each `K(D)` by only a bounded adjacent-binomial
factor, so (1.5) remains true.  Theorem 2.1 extends `F_j+e`, proving that
`e` belongs to a perfect matching of `B_j`. \(\square\)

Fix a perfect matching `N` of `B_j`, contract its edges, and orient an arc
`x->z` whenever `xN(z)` is an incidence of `B_j`.  As in the polynomial
proof, connectedness plus the fact that every residual edge is allowed
implies that this exchange digraph is strongly connected.

### Lemma 3.2 (subexponential alternating diameter)

Every such exchange digraph has directed diameter at most

\[
                         8rj+32r^2+4.               \tag{3.3}
\]

#### Proof

For a forward set `S` of size at most `W/2`, spectral surplus gives

\[
 |\Gamma^+(S)|-|S|\ge {|S|\over2r}-j.               \tag{3.4}
\]

Strong connectivity grows a forward ball at least one vertex per step
until size `4rj`; afterward (3.4) multiplies it by at least
`1+1/(4r)` until it exceeds `W/2`.  This costs at most

\[
                         4rj+8r\log W+2             \tag{3.5}
\]

steps.  The complemented backward argument has the same bound.  The two
majority balls meet, and `log W<2r`, proving (3.3). \(\square\)

## 4. Hamilton-anchored completion

Fix a Hamilton cycle of `G` and write its two alternating perfect
matchings as `H_0,H_1`.

### Theorem 4.1 (subexponential-damage insertion)

Let `H` be either Hamilton half.  Under (1.5), there is a perfect matching
`M` containing `F` such that

\[
 |M\triangle H|
 \le 8rf^2+64r^2f+10f.                              \tag{4.1}
\]

Consequently, when `f=2^{o(r)}` and (1.6) holds,

\[
                         |M\triangle H|=2^{o(r)}.     \tag{4.2}
\]

#### Proof

Insert the edges of `F` in the fixed order.  At prefix `j`, if the next
edge is absent, Lemma 3.2 supplies a return path in the exchange digraph.
Together with the desired arc it is an alternating cycle; switching on it
inserts the edge without changing `F_j`.  Twice the cycle length bounds
the matching symmetric difference spent at that step.  Summing (3.3) for
`0<=j<f` gives (4.1).  Equation (4.2) is immediate. \(\square\)

Now let `P` be an oriented protected owner-path forest.  Alternately colour
its incidence edges and call the two matching classes `F_0,F_1`.  Assume
both satisfy (1.5), with sizes `f_0,f_1`.

### Theorem 4.2 (subexponential-component directed completion)

There are perfect matchings `M_i\supseteq F_i` such that the coloured
cycle cover

\[
                         \mathcal K=M_0\uplus_{\rm col}M_1   \tag{4.3}
\]

contains every oriented protected path and has

\[
 c(\mathcal K)
 \le1+{1\over2}\sum_{i=0}^1
       (8rf_i^2+64r^2f_i+10f_i).                    \tag{4.4}
\]

The number of coloured common edges has the same upper bound without the
leading one.  In particular, if `f_0,f_1=2^{o(r)}` and both have a fixed
sub-half exposure margin, then

\[
 c(\mathcal K)=2^{o(r)},\qquad
 |M_0\cap M_1|=2^{o(r)}.                             \tag{4.5}
\]

#### Proof

Apply Theorem 4.1 to `(H_i,F_i)`.  The original coloured union
`H_0\uplus_{\rm col}H_1` is one Hamilton cycle.  Unless the new union equals
that cycle, take one proper component `C` of the new cover.  The Hamilton
cycle has a nonempty even edge cut across `V(C)`, hence at least two of its
coloured edges leave `V(C)`.  Neither can remain in the corresponding
`M_i`, because every `M_i`-edge at a vertex of `C` stays inside the new
component.  Thus every proper new component consumes at least two distinct
edges from

\[
                         (H_0\setminus M_0)\uplus_{\rm col}
                         (H_1\setminus M_1).          \tag{4.6}
\]

The cuts of distinct components are edge-disjoint.  Also, for two
equal-size matchings,

\[
 |H_i\setminus M_i|=|M_i\setminus H_i|
                   ={1\over2}|M_i\triangle H_i|.     \tag{4.7}
\]

Charging the two cut edges proves (4.4).  Since the Hamilton halves are
disjoint, every common coloured edge of `M_0,M_1` is added relative to at
least one corresponding half and is counted in the right side of (4.7).
This proves the common-edge bound and (4.5). \(\square\)

## 5. Consequence for the current tail programme

The complete tail witness family and its seasoning-buffer splices have
`2^{o(r)}` incidences.  Once their owner/lower/upper Ore halos are packed
with a fixed sub-half exposure margin, alternate colouring gives two
matchings satisfying (1.5).  Theorem 4.2 then extends them to a directed
spanning cycle cover with only `2^{o(r)}` components and only `2^{o(r)}`
common-edge debt.

Thus the tail bank cannot create an uncontrolled exponential completion
defect.  The remaining tail statements are:

1. the resource-disjoint Ore-halo packing itself;
2. physical fusion of the `2^{o(r)}` residual components/common edges; and
3. compatibility with the PBBS all-width and payload rows.

## 6. Dependencies and scope

Used as inputs:

* the Johnson spectral-surplus inequality;
* the sharp balanced and strict-imbalance partial-shadow thresholds;
* existence of a middle-levels Hamilton cycle; and
* the alternating-cycle insertion argument.

No new finite computation, solver, or probabilistic matching theorem is
used.  The theorem is a quantitative strengthening of
`MATH_THEOREM_POLYNOMIAL_PARTIAL_MATCHING_EXTENSION_AND_DIRECTED_FOREST_COVER_20260806.md`
and
`MATH_THEOREM_HAMILTON_ANCHORED_POLYNOMIAL_DAMAGE_CYCLE_COUNT_FOR_PBBS_20260806.md`.
