# Constant clustered origins already have `o(W)` pooled profile deficit

**Status (2026-08-21).**  Every assertion below is proved.  In the two-block
clustered product palette, discard every counter origin whose next `H` type
steps cross an `A/B` run boundary.  Every retained origin then generates one
common all-`A` or all-`B` extension chain through the whole upper band.  The
resulting endpoint-only split-profile capacities still have aggregate
deficit

\[
 O\!\left(W_b b^{-1/4}\log^{7/4}b\right)=o(W_b).
\]

The same endpoint flow lifts to the 3-uniform token/source/target
hypergraph; quantitative small-codegree rounding gives separate integral
matchings at every offset with total deficit `o(W_b)`, still using only
these band-constant endpoint tokens.

Thus the moving phase boundary and the interior phase types are not needed
for scalar band capacity.  This is a simultaneous-phase simplification, not
a labelled construction: common cyclic orders, tight-cycle factors, target
integrality, and the coupling of the two endpoint families remain open.

## 1. The common-origin endpoint capacity

Let `b` tend through odd primes, let `A,B` be disjoint `b`-sets, and put

\[
 W_b={2b\choose b},\qquad H=\Theta(\sqrt{b\log b}).  \tag{1.1}
\]

For a payload split `r`, the clustered type word is the cyclic word
`A^rB^(b-r)`.  Exactly

\[
 (r-H+1)_+\quad\hbox{origins have their next `H` types all `A`,}
\]
\[
 (b-r-H+1)_+\quad\hbox{origins have their next `H` types all `B`.} \tag{1.2}
\]

These origins are independent of the offset `q<=H`: one retained origin
specifies one constant-type chain simultaneously at every `q`.

At upper offset `q`, a target profile is indexed by

\[
 s=|V\cap A|,\qquad
 P_{q,s}={b\choose s}{b\choose s-q}.                \tag{1.3}
\]

An all-`B` extension comes from payload `r=s`; an all-`A` extension comes
from payload `r=s-q`.  Their pooled formal capacity is therefore

\[
 E_{q,s}={1\over b}\left[
 (b-s-H+1){b\choose s}^{\!2}
 +(s-q-H+1){b\choose s-q}^{\!2}\right],             \tag{1.4}
\]

whenever both coefficients and both payload ranks are admissible.  Outside
the central quarter

\[
 s,\ s-q\in[b/4,3b/4]                               \tag{1.5}
\]

set `E_(q,s)=0` and charge the target profile in full.  The omitted tails,
summed over `q<=H`, have mass `e^(-Omega(b))W_b`.

## 2. Exact localization of a deficient profile

Fix a central profile and write

\[
 s={b+q\over2}+x,\qquad
 a={b-q\over2}-H+1,\qquad
 R={{b\choose s}\over {b\choose s-q}},\qquad
 u=\log R.                                          \tag{2.1}
\]

Then (1.4) gives the exact ratio

\[
 {E_{q,s}\over P_{q,s}}
 ={(a-x)R+(a+x)R^{-1}\over b}
 ={2a\over b}\cosh u-{2x\over b}\sinh u.            \tag{2.2}
\]

The sign of `u` is opposite the sign of `x`, so the last term in (2.2) is
nonnegative.  Put

\[
 \delta_q={q+2H-2\over b},\qquad {2a\over b}=1-\delta_q. \tag{2.3}
\]

For all large `b`, `delta_q<1/2`; hence

\[
 {E_{q,s}\over P_{q,s}}
 \ge(1-\delta_q)\cosh u
 \ge(1-\delta_q)(1+u^2/2).                          \tag{2.4}
\]

Consequently

\[
 [P_{q,s}-E_{q,s}]_+\le\delta_qP_{q,s},             \tag{2.5}
\]

and a positive deficit is possible only if

\[
 |u|<2\sqrt{\delta_q}.                              \tag{2.6}
\]

The binomial ratio supplies the required spatial localization.  With
`d=(b+1)/2` and `theta_j=j-(q-1)/2`,

\[
 u(x)=\sum_{j=0}^{q-1}
 \log {d-(x+\theta_j)\over d+(x+\theta_j)}.         \tag{2.7}
\]

The offsets are symmetric, so `u(0)=0`, while every summand has derivative

\[
 {-2d\over d^2-y^2}\le-{4\over b+1}.                \tag{2.8}
\]

Integration gives

\[
 |u(x)|\ge {4q|x|\over b+1}.                        \tag{2.9}
\]

Combining (2.6) and (2.9), every deficient profile lies in

\[
 |x|\le L_q:={b+1\over2q}\sqrt{\delta_q}
 =O\!\left({\sqrt{b(q+H)}\over q}\right).           \tag{2.10}
\]

## 3. Aggregate deficit

The standard central-binomial bounds give, uniformly in `q,s`,

\[
 {P_{q,s}\over W_b}
 \le {C\over\sqrt b}
 \exp\!\left[-c{q^2+x^2\over b}\right]              \tag{3.1}
\]

for absolute positive constants `c,C`.  Indeed, apply

\[
 {b\choose b/2+y}\le {C2^b\over\sqrt b}e^{-c y^2/b}
\]

to the two factors in (1.3), whose centered displacements are
`x+q/2` and `x-q/2`, and divide by
`W_b>=c4^b/sqrt(b)`.

Let

\[
 D_q=\sum_s[P_{q,s}-E_{q,s}]_+.                    \tag{3.2}
\]

Equations (2.5), (2.10), and (3.1) imply

\[
 {D_q\over W_b}
 \le C e^{-cq^2/b}\left[
 {q+H\over b\sqrt b}
 +{(q+H)^{3/2}\over bq}\right].                    \tag{3.3}
\]

The first term in (3.3), summed over `q<=H`, is `o(1)`.  For the second,
`q+H<=2H` and

\[
 \sum_{q=1}^H{e^{-cq^2/b}\over q}=O(\log b).        \tag{3.4}
\]

Therefore

\[
 \sum_{q=1}^H D_q
 \le O\!\left({H^{3/2}\log b\over b}\right)W_b
 +o(W_b)
 =O\!\left(W_b b^{-1/4}\log^{7/4}b\right)
 =o(W_b).                                           \tag{3.5}
\]

Adding the exponentially small profiles excluded in (1.5) does not change
(3.5).  Complementation gives the identical lower-band statement.

## 4. Separate-offset integral endpoint rounding

The scalar statement also survives the token/source/target integrality
constraints.  For a source `U` of split `r`, give an all-`B` containment
`U subset V` at offset `q` the weight

\[
 f_q^\circ(U,V)=
 \rho_{q,r}{b-r-H+1\over b{r\choose q}},            \tag{4.1}
\]

and give an all-`A` containment, whose target split is `r+q`, the weight

\[
 f_q^\circ(U,V)=
 \rho_{q,r+q}{r-H+1\over b{b-r\choose q}},          \tag{4.2}
\]

where

\[
 \rho_{q,s}=\min(1,P_{q,s}/E_{q,s})                \tag{4.3}
\]

with the usual zero convention.  The total load at `U` is at most

\[
 {b-r-H+1+r-H+1\over b}\le1.                       \tag{4.4}
\]

The same choose-in-either-order identity used for the full fractional
transport shows that every target in profile `s` has load
`min(1,E_(q,s)/P_(q,s))`.  Thus (4.1)--(4.2) have total mass

\[
 F_q^\circ=\sum_s\min(P_{q,s},E_{q,s}).             \tag{4.5}
\]

Split each phase type into its actual
`(r-H+1)L_r/b` or `(b-r-H+1)L_r/b` occurrence-token vertices and divide
the corresponding edge weights uniformly among them.  This produces a
3-uniform token/source/target fractional matching.  After the central-quarter
truncation its maximum fractional pair load is at most

\[
 {1\over{\lfloor b/4\rfloor\choose q}}+e^{-\Omega(b)}. \tag{4.6}
\]

The quantitative Molloy--Reed small-codegree rounding argument, stated and
derived in
`MATH_THEOREM_ALL_OFFSET_TOKEN_ORBIT_SMALL_CODEGREE_ROUNDING_20260821.md`,
therefore gives integral matchings `\mathcal M_q^\circ` using only these
band-constant endpoint tokens.  Its relative loss is
`O(beta_q^(1/3)log^4(1/beta_q))`, where
`beta_q=binom(floor(b/4),q)^(-1)`.  Hence

\[
 \sum_{q=1}^H\left[{2b\choose b+q}
                 -|\mathcal M_q^\circ|\right]
 =o(W_b):                                           \tag{4.7}
\]

the scalar part is (3.5), the `q=1` rounding loss is
`O(W_b b^(-1/3)log^4 b)`, and the sum for `q>=2` is
`O(HW_b b^(-2/3)log^4 b)=o(W_b)`.

Equation (4.7) treats offsets separately.  The selected sources and token
identities may depend on `q`, and the chosen targets need not be nested.
It is therefore an integral endpoint-orbit theorem, not yet one family of
physical chains.

## 5. Exact consequence and surviving gate

The capacities (1.4) use one fixed set of origins through the entire band:
there is no rankwise re-selection and no Ferrers-origin reconciliation.
Moreover every retained chain has a constant side type, so the interior
phase classes `1<=z<=q-1` disappear completely.

What (3.5) proves is only that these common origins are numerically
sufficient after pooling neighboring payload ranks.  It does not assign
actual labelled targets to origins.  An all-`A` chain needs successive
labels from one cyclic order on `A`, an all-`B` chain needs one order on
`B`, and many middle targets must share each order through a tight-cycle
factor.  The remaining problem is therefore a two-endpoint labelled
order-bank transport/absorption theorem, now with phase consistency already
built in.
