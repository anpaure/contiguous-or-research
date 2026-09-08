# Protected factors: the two-matching orientation does not follow from sublinear exposure

**Date:** 2026-08-05  
**Method:** pure mathematics; Hall's theorem, one coordinate cut, and the
probabilistic method; no computation or search  
**Status:** unconditional obstruction theorem.  The two local exposure
parameters in the current protected-factor theorem, even together with
pairwise disjoint owner, lower, and upper immediate palettes, do not force a
protected path forest to extend to a spanning two-factor.  Equivalently, no
choice of alternating orientations of the protected paths need make both
partial matchings extendible.

## 0. Setting

Let

\[
 \mathcal L={ [2r-1]\choose r-1},\qquad
 \mathcal U={ [2r-1]\choose r}
\]

be the two shores of the balanced middle-level incidence graph `G_r`.
Thus `G_r` is `r`-regular and its two shores have the same size `W`.

For a protected incidence path forest `P`, put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},\qquad
 X=\mathcal L\setminus Z,
\]

and

\[
 \alpha(P)=\max_{x\in X}
 |\{U\in\mathcal U:x\subset U,\ d_P(U)>0\}|,
 \qquad
 \beta(P)=\max_{U\in\mathcal U}|N(U)\cap Z|.       \tag{0.1}
\]

These are exactly the two exposure parameters used in
`MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`.

## 1. Main theorem

### Theorem 1.1 (sublinear-exposure coordinate-cut obstruction)

For every sufficiently large `r`, there is a protected path forest `P` in
`G_r` with all of the following properties.

1. Every component of `P` has two incidence edges,

   \[
                         U^- - z - U^+ .            \tag{1.1}
   \]

   Consequently every member of `Z` has protected degree two and every
   protected owner has degree one.

2. Different components have disjoint owners and distinct lower and upper
   Johnson colours.  Thus the bank is disjoint in all three immediate
   palettes.

3. The local loads satisfy

   \[
                  \alpha(P),\beta(P)
                    \le \left\lceil {8r\over\log r}\right\rceil
                    =o(r).                           \tag{1.2}
   \]

4. `P` does not extend to a spanning two-factor of `G_r`.

5. More strongly, alternately colour the two edges of every component red
   and blue, with either orientation independently on every component.  If
   `P_0,P_1` are the two resulting partial matchings, then at least one of
   `P_0,P_1` does not extend even to a perfect matching of `G_r`.  Therefore
   the sequential two-perfect-matching strategy cannot repair this bank.

The failed residual shore and its optional complement both have
cardinality `(1/2+o(1))W`.  Hence this is a literal example of the optional
middle core left open by the current two-tail theorem.

## 2. A coordinate decomposition

Fix a distinguished coordinate `infinity` and partition both shores by
whether they contain it:

\[
 \begin{aligned}
  \mathcal L_1&=\{x\in\mathcal L:\infty\in x\},
  &\mathcal L_0&=\mathcal L\setminus\mathcal L_1,\\
  \mathcal U_1&=\{U\in\mathcal U:\infty\in U\},
  &\mathcal U_0&=\mathcal U\setminus\mathcal U_1.
 \end{aligned}                                      \tag{2.1}
\]

Write

\[
 A=|\mathcal U_1|=|\mathcal L_0|
       ={2r-2\choose r-1},
 \qquad
 B=|\mathcal L_1|=|\mathcal U_0|
       ={2r-2\choose r-2}.                          \tag{2.2}
\]

The exact coordinate-cut surplus is

\[
 {B\over A}={r-1\over r},
 \qquad
 \Delta:=A-B={A\over r}.                           \tag{2.3}
\]

### Lemma 2.1 (a full bank of disjoint crossing paths)

There is an injection

\[
 f:\mathcal U_0\longrightarrow\mathcal L_0,
 \qquad f(U)\subset U.                              \tag{2.4}
\]

For every `U in mathcal U_0`, put

\[
 z_U=f(U),\qquad U^+=z_U\cup\{\infty\}.            \tag{2.5}
\]

Then

\[
                         U-z_U-U^+                  \tag{2.6}
\]

is an incidence path, and all paths (2.6) are pairwise vertex-disjoint.
Their Johnson lower colours `z_U` are distinct, and their Johnson upper
colours

\[
                         U\cup U^+=U\cup\{\infty\}  \tag{2.7}
\]

are distinct.

#### Proof

In the inclusion graph on the `(2r-2)` coordinates different from
`infinity`, every `U in mathcal U_0` has `r` rank-`(r-1)` facets, whereas
every member of `mathcal L_0` lies below exactly `r-1` members of
`mathcal U_0`.  Hence, for every `C subseteq mathcal U_0`, double counting
the incidences leaving `C` gives

\[
                         r|C|\le(r-1)|N(C)|.
\]

Hall's theorem gives an injection (2.4).  Injectivity of `f` gives
distinct `z_U` and distinct `U^+`; the zero and one coordinate shores make
the two owner families mutually disjoint.  Equation (2.7) proves upper
colour injectivity. `square`

## 3. A sparse random subbank has the required local loads

Select every path (2.6), independently, with probability

\[
                              p={4\over r}.          \tag{3.1}
\]

Let `P` be the selected incidence forest and let `Z` be its selected lower
shore.  The number `N=|Z|` of selected paths is binomial with mean

\[
              \mu=pB={4B\over r}.                  \tag{3.2}
\]

By (2.3),

\[
 {2\Delta\over\mu}={r\over2(r-1)}\le{2\over3}
 \qquad(r\ge4).                                    \tag{3.3}
\]

The Chernoff lower-tail inequality therefore gives

\[
 \Pr(N\le2\Delta)
   \le \Pr(N\le(2/3)\mu)
 \le \exp(-\mu/18).                              \tag{3.4}
\]

The upper-tail inequality also gives

\[
                         \Pr(N\ge2\mu)\le e^{-\mu/3}.              \tag{3.5}
\]

We next bound the two local loads.

Fix `x in X`.  If `infinity in x`, then no zero-side endpoint contains
`x`, and at most `r` candidate one-side endpoints `U^+` contain it.  If
`infinity notin x`, then at most `r-1` candidate zero-side endpoints
contain it.  The only possible one-side endpoint containing all of `x` is
`x union {infinity}`; if that endpoint belongs to the path whose lower
colour is `x` and the path is selected, then `x in Z`, contrary to
`x in X`.  Thus in either case the protected-owner exposure of `x` is
stochastically dominated by

\[
                              \operatorname{Bin}(r,4/r).             \tag{3.6}
\]

For a fixed owner `V`, its `r` facets contain at most `r` values in the
injective image of `f`.  Hence `|N(V) cap Z|` has the same stochastic
upper bound (3.6).

Put

\[
                         T=\left\lceil{8r\over\log r}\right\rceil.  \tag{3.7}
\]

For all sufficiently large `r`, the standard binomial upper-tail bound
and `E Bin(r,4/r)=4` give

\[
 \Pr(\operatorname{Bin}(r,4/r)\ge T)
 \le\left({4e\over T}\right)^T
 \le e^{-4r}.                                      \tag{3.8}
\]

There are fewer than `2^(2r)` lower- and upper-shore load tests in total.
The union bound makes the probability that any test exceeds `T` at most

\[
                         2^{2r}e^{-4r}=o(1).         \tag{3.9}
\]

The right sides of (3.4)--(3.5) are also `o(1)`, since `mu` is
exponential in `r`.  Therefore some selected bank satisfies simultaneously

\[
                    2\Delta<|Z|<2\mu,
 \qquad             \alpha(P),\beta(P)\le T.       \tag{3.10}
\]

Fix such a bank for the rest of the proof.

## 4. The exact residual two-factor obstruction

Give an owner the usual residual capacity

\[
                         c_U=2-d_P(U).               \tag{4.1}
\]

Take the residual lower shore

\[
                         \mathcal A=\mathcal L_1.    \tag{4.2}
\]

This is a subset of `X`, because every protected lower colour lies in
`mathcal L_0`.  Every neighbour of `mathcal A` lies in `mathcal U_1`.
Conversely, every `U in mathcal U_1` has exactly `r-1` facets in
`mathcal A`.  Since `r-1>=2>=c_U`, the capacitated Hall value is

\[
 \begin{aligned}
 \kappa(\mathcal A)
   &=\sum_{U\in\mathcal U_1}\min\{c_U,|N(U)\cap\mathcal A|\}\\
   &=\sum_{U\in\mathcal U_1}c_U
     =2A-|Z|.                                       \tag{4.3}
 \end{aligned}
\]

The last equality holds because every selected path has exactly one
one-side endpoint, of protected degree one.  Equations (2.2), (2.3), and
(3.10) now give

\[
 \kappa(\mathcal A)
       =2A-|Z|
       <2A-2\Delta
       =2B
       =2|\mathcal A|.                              \tag{4.4}
\]

Thus the exact capacitated Hall criterion fails, and `P` has no spanning
two-factor extension.

Its optional complement is

\[
                   X\setminus\mathcal A=\mathcal L_0\setminus Z.   \tag{4.5}
\]

Because `|Z|=O(W/r)`, both (4.2) and (4.5) have size
`(1/2+o(1))W`.  This locates the obstruction in the unclosed middle
window rather than either tail.

## 5. Why no alternating orientation can work

Alternately colour each two-edge component of `P` red and blue.  The
orientation on every component may be chosen arbitrarily.  Let `P_i` be
the partial matching of colour `i`, and let

\[
 t_i=|\{U\in\mathcal U_1:U\text{ is already matched by }P_i\}|.
                                                               \tag{5.1}
\]

Every protected path assigns its one-side endpoint to exactly one of the
two colours, so

\[
                              t_0+t_1=|Z|.           \tag{5.2}
\]

If `P_i` extended to a perfect matching, every member of
`mathcal A=mathcal L_1` would have to be matched into `mathcal U_1`, and
the `t_i` owners already occupied by `P_i` would be unavailable.  Hall's
necessary inequality is therefore

\[
                       A-t_i\ge B,
 \qquad\text{or equivalently}\qquad t_i\le\Delta.  \tag{5.3}
\]

If both partial matchings extended, (5.2)--(5.3) would imply
`|Z|<=2Delta`, contrary to (3.10).  Hence at least one colour fails before
edge-disjointness of the two completions even becomes an issue.

This proves Theorem 1.1. `square`

## 6. Exact interpretation and scope

Every bipartite spanning two-factor is the union of two edge-disjoint
perfect matchings.  Conversely, alternating the edges of its cycles gives
such a decomposition.  Thus orienting the protected paths and extending
two partial matchings is an exact reformulation, not a relaxation.

The obstruction above says that the two colours possess only

\[
                              2\Delta               \tag{6.1}
\]

units of total coordinate-cut surplus.  Each protected crossing path
consumes one such unit, independently of its orientation.  Once more than
`2Delta` paths are protected, one colour necessarily overloads the cut.

Consequently, none of the following data alone can prove protected-factor
extension:

* `alpha(P)=o(r)`;
* `beta(P)=o(r)`;
* pairwise disjoint owner resources;
* pairwise disjoint lower immediate colours;
* pairwise disjoint upper immediate colours; or
* arbitrary orientation of every protected path before sequential matching.

The theorem does **not** refute extension of the specific deadline-length
balanced collar bank.  Its components have additional geometry absent
from the length-one crossing paths above.  What it proves is that any
successful extension theorem for that bank must use a global balancing
invariant excluding coordinate-cut overloads (or use its detailed collar
geometry); the two local exposure bounds and generic robust matching of
the middle-level graph cannot suffice.

An exact necessary strengthening is the following family of protected-cut
inequalities.  If `mathcal A subseteq X` and every owner in
`N(mathcal A)` has at least its residual capacity many neighbours in
`mathcal A`, then

\[
 \boxed{
 \sum_{U\in N(\mathcal A)} d_P(U)
      \le 2\bigl(|N(\mathcal A)|-|\mathcal A|\bigr).}              \tag{6.2}
\]

Indeed, under that hypothesis the left side subtracted from
`2|N(mathcal A)|` is exactly `kappa(mathcal A)`.  Equation (4.4) is the
strict failure of (6.2) for `mathcal A=mathcal L_1`: its left side is
`|Z|`, whereas its right side is `2Delta`.

The next protected-factor theorem therefore needs at least one genuinely
global condition: coordinate-cut balance, optional-middle-core exclusion,
or a correlated construction which makes those inequalities automatic.

## 7. The audited balanced collars automatically clear every one-coordinate cut

The obstruction is sharp enough to give a useful positive audit of the
actual Catalan collar bank.

For a coordinate `i`, define its protected added-label load

\[
 g_i(P)=|\{(z,U)\in E(P):U\setminus z=\{i\}\}|.     \tag{7.1}
\]

### Lemma 7.1 (exact coordinate charge identity)

Let

\[
 \mathcal A_i=\{x\in X:i\in x\}.
\]

If `beta(P)<=r-3`, then the residual Hall inequality on
`mathcal A_i` is equivalent to

\[
                         g_i(P)\le {2W\over2r-1}.    \tag{7.2}
\]

#### Proof

Put `L_i={x in mathcal L:i in x}` and
`U_i={U in mathcal U:i in U}`.  As in (2.2)--(2.3),

\[
 |U_i|-|L_i|={W\over2r-1}.                          \tag{7.3}
\]

Every owner in `U_i` has `r-1` facets in `L_i`.  At most `beta(P)` of
them lie in `Z`, so it has at least

\[
                         r-1-\beta(P)\ge2
\]

neighbours in `mathcal A_i`.  This is at least its residual capacity.
Therefore

\[
 \kappa(\mathcal A_i)=2|U_i|-\sum_{U\in U_i}d_P(U).                \tag{7.4}
\]

Because every `z in Z` has exactly two protected incidences,

\[
 \begin{aligned}
 \sum_{U\in U_i}d_P(U)-2|Z\cap L_i|
  &=\sum_{(z,U)\in E(P)}
       \bigl({\bf1}_{i\in U}-{\bf1}_{i\in z}\bigr)\\
  &=g_i(P).                                         \tag{7.5}
 \end{aligned}
\]

Substitute (7.5) into
`kappa(mathcal A_i)>=2|mathcal A_i|` and use (7.3).  The result is
exactly (7.2). `square`

### Corollary 7.2 (the Catalan collar bank has coordinate slack two)

Let `P` be the incidence lift of any `b` generalized balanced collars from
`MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md` on
the odd ground set `[2r-1]`, where

\[
                         b={W\over2r-1}-1.           \tag{7.6}
\]

Then every one-coordinate residual Hall cut passes.  More precisely,

\[
                         g_i(P)\le2b
                           ={2W\over2r-1}-2          \tag{7.7}
\]

for every coordinate `i`.

#### Proof

In one generalized balanced collar, the internal geodesic exchanges the
pairwise distinct labels `lambda_j,rho_j`.  The left seam uses
`q_- ,rho_1`, so only `rho_1` can occur for a second time; the right seam
uses `q_+,z`, with `q_+` in the fixed core and `z` fresh.  The two core
labels `q_-` and `q_+` may coincide, but neither is an internal rail
label.  Hence every coordinate is the added label of at most two protected
incidences in one collar.  Summing over (7.6) gives (7.7).

The audited bank has `beta(P)=O(r/log r)<=r-3` for all sufficiently large
`r`, so Lemma 7.1 applies. `square`

Thus the explicit counterexample identifies a real global invariant, while
the detailed collar arithmetic automatically satisfies its entire
one-coordinate subfamily.  The live optional middle core, if it exists for
the Catalan collar bank, must be supported on a genuinely higher-order
family rather than a principal coordinate star.

## 8. The full principal-upset boundary ledger

The coordinate identity has an exact higher-order form.  It gives a
concrete hierarchy of global tests for any future collar selection theorem.

Fix `S subseteq [2r-1]`, `|S|=t`, and put

\[
 \mathcal L_S=\{x\in\mathcal L:S\subseteq x\},
 \qquad
 \mathcal U_S=\{U\in\mathcal U:S\subseteq U\}.      \tag{8.1}
\]

Define the protected incidence boundary entering this principal upset by

\[
 g_S(P)=|\{(z,U)\in E(P):S\subseteq U,\ S\nsubseteq z\}|.           \tag{8.2}
\]

Because `z` is a facet of `U`, an incidence counted in (8.2) is exactly an
incidence whose added label `U setminus z` belongs to `S` and whose other
`t-1` labels of `S` already lie in `z`.

### Lemma 8.1 (principal-upset cut identity)

Assume

\[
                         \beta(P)\le r-t-2.         \tag{8.3}
\]

Then the residual Hall inequality on

\[
                         \mathcal A_S=\mathcal L_S\setminus Z
\]

is equivalent to

\[
 \boxed{
 g_S(P)\le {2t\over r}|\mathcal U_S|.}              \tag{8.4}
\]

#### Proof

The two principal-family sizes satisfy

\[
 |\mathcal U_S|={2r-1-t\choose r-t},
 \qquad
 |\mathcal L_S|={2r-1-t\choose r-1-t}
                  ={r-t\over r}|\mathcal U_S|.      \tag{8.5}
\]

Every owner in `mathcal U_S` has `r-t` facets containing `S`.  By (8.3),
at least two of them remain in `mathcal A_S`, so the owner has at least its
residual capacity many neighbours there.  Hence

\[
 \kappa(\mathcal A_S)
    =2|\mathcal U_S|-\sum_{U\in\mathcal U_S}d_P(U).                \tag{8.6}
\]

As in (7.5), degree two on every protected lower colour gives

\[
 \sum_{U\in\mathcal U_S}d_P(U)-2|Z\cap\mathcal L_S|
   =\sum_{(z,U)\in E(P)}
      \bigl({\bf1}_{S\subseteq U}-{\bf1}_{S\subseteq z}\bigr)
   =g_S(P).                                         \tag{8.7}
\]

Substituting (8.5)--(8.7) in
`kappa(mathcal A_S)>=2|mathcal A_S|` proves (8.4). `square`

For `t=1`, (8.4) is exactly Lemma 7.1.  For larger `t`, the right side
shrinks with the size of the principal owner family, so the per-coordinate
bound (7.7) alone does not imply it.  A complete extension proof for the
collar bank may therefore aim at the explicit boundary-discrepancy system
(8.4), rather than at an unstructured search over all middle optional
cores.  These tests are necessary; no sufficiency claim for arbitrary
residual shores is made.

The low-star spread already proved for the audited collar bank settles a
large interval of these higher-order tests.

### Corollary 8.2 (all sufficiently wide principal upsets pass)

Let `P` be the odd Catalan collar bank of Corollary 7.2, put `s=h+1`, and
retain the notation `beta(P)` from (0.1).  If

\[
 \left\lceil {256sr\over2r-1}\right\rceil
       \le t\le \min\{r-\beta(P)-2,r-h-1\},         \tag{8.8}
\]

then every rank-`t` principal-upset cut (8.1) passes.

#### Proof

Item 4 of the three-palette collar-bank theorem gives, for every such `S`
(and in its stated range `t<=r-h-1`),

\[
 |V_P\cap\mathcal U_S|
       \le {256s\over2r-1}|\mathcal U_S|.           \tag{8.9}
\]

Every selected owner has protected degree at most two.  Therefore

\[
 g_S(P)le\sum_{U\in\mathcal U_S}d_P(U)
      \le {512s\over2r-1}|\mathcal U_S|.            \tag{8.10}
\]

The lower bound in (8.8) makes the last quantity at most
`(2t/r)|mathcal U_S|`; the upper bound in (8.8) supplies (8.3).  Lemma 8.1
finishes the proof. `square`

At deadline scale, the lower threshold in (8.8) is
`128s+O(1)=Theta(sqrt r)`, while the upper threshold is
`r-O(r/log r)`.  Together with Corollary 7.2, the presently unpriced
principal-upset orders are confined to the short interval
`2<=t<128s+O(1)` and the near-top interval where the crude global `beta`
bound no longer guarantees two residual facets.  This still does not
exclude nonprincipal optional middle cores.
