# A general boundary--seam inequality

## 1. Outcome

This note extends the boundary-reservoir argument from a single atom to an
arbitrary limiting directed-plateau profile.  The extension is quantitative:
plateaux whose lengths lie just above the dangerous threshold are isolated
explicitly, while every longer successor is charged to the first-dangerous
seam functional.

Let

\[
 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
       \Longrightarrow\mu
\]

on `[0,2]`, and, at a continuity point `c` of `mu`, put

\[
 \sigma_c:=\int_{(c,2]}x\,d\mu(x),\qquad
 \nu(c,\eta):=\mu((c,c+\eta]).                    \tag{1.1}
\]

Here `sigma_c` is the normalized edge mass in the `c`-dangerous
plateaux.  Let `H(c)` be the limiting first-dangerous seam mass and let
`r(c)` be the upper density of indices having a valid one-sided length-`L`
window containing no complete `c`-dangerous directed plateau.  Under
`D=o(a^2)`, for every fixed `0<c<2/3` and fixed `0<eta<2-c` for which both
endpoints are continuity points of `mu` and the relevant profile limits
exist,

\[
 \boxed{
  3-\sigma_c
  \le r(c)+{2\over\eta}H(c)+4\nu(c,\eta)
  \le {9\over4}c^2+{2\over\eta}H(c)+4\nu(c,\eta). }
                                                               \tag{1.2}
\]

Equivalently, with

\[
 \tau(c,\eta):=\int_{(c,c+\eta]}x\,d\mu(x),
\]

the last term in (1.2) may be replaced by `4 tau(c,eta)/c`.

The constants in (1.2) come from an exact finite estimate.  In particular,
the seam coefficient is `2/eta`, rather than the `4/eta` obtained by
deleting `L` positions at both ends of every gap.  The improvement uses the
fact that at most `L` positions in one internal gap can lack both a forward
and a backward gap-contained window.

Two consequences are immediate.

1. If `H(c)=0` at a fixed continuity point `0<c<2/3`, then

   \[
                         \sigma_c\ge3-{9\over4}c^2.             \tag{1.3}
   \]

2. If `H(c)->0` as `c downarrow 0` through continuity points, then the
   total plateau edge mass is saturated:

   \[
                    \sigma:=\int_{(0,2]}x\,d\mu(x)=3.           \tag{1.4}
   \]

Thus the boundary invariant excludes every unsaturated general profile
with asymptotically vanishing small-threshold seam mass.  This is not an
atomic assertion.

The corrected mass and weighted-supply laws do not, however, force
`H(c)->0`.  A positive-seam unsaturated variational region remains.  Its
precise necessary inequalities are isolated in Section 7.

## 2. Finite setup

Retain the audited three-box notation

\[
 M_a=3a^2+3a+1,\qquad L=4a+2.                       \tag{2.1}
\]

Fix numerical constants `c>0` and `0<eta<2-c`; neither may depend on `a`.
List the complete directed peak plateaux with

\[
                         \lambda_j>ca
\]

in word order as `P_1,...,P_m`.  Their edge sets are disjoint and
`lambda_j<=2a`.  Let `g_(j-1)` be the number of positions in the complement
of their vertex union between `P_(j-1)` and `P_j`.  Put

\[
 \delta_j=\lambda_j-ca,
 \qquad
 H_a(c)={1\over a^3}\sum_{j=2}^m
       \delta_j\min\{g_{j-1},L-\lambda_j\}.          \tag{2.2}
\]

Let `R_a(c)` be the set of middle-order indices at which at least one valid
forward or backward length-`L` window contains no complete directed plateau
of edge length greater than `ca`.  Finally set

\[
 n_a(c,\eta)=\#\{j:ca<\lambda_j\le(c+\eta)a\}.       \tag{2.3}
\]

The dangerous-free-window lemma supplies a run of cost at most `ca` at
each index of `R_a(c)`.

## 3. Exact loss inside one complement gap

Consider an internal complement gap of `g` positions and number them from
left to right.  A position has a forward length-`L` window wholly inside
the gap if its gap coordinate is at most `g-L`; it has a backward such
window if its coordinate is at least `L+1`.  Hence the number having neither
window is at most

\[
 I_L(g)=
 \begin{cases}
   g,&0\le g\le L,\\
   2L-g,&L<g<2L,\\
   0,&g\ge2L.
 \end{cases}                                        \tag{3.1}
\]

In particular,

\[
                         I_L(g)\le\min\{g,L\}.       \tag{3.2}
\]

For any dangerous successor of length `lambda`, put `b=L-lambda`.  Since
`0<b<=L`,

\[
 \min\{g,L\}
 \le {L\over b}\min\{g,b\}.                        \tag{3.3}
\]

Moreover `lambda<=2a`, so

\[
                         b\ge L-2a=2a+2.             \tag{3.4}
\]

If the successor is not in the short band (2.3), then
`delta>eta a`.  Combining (3.2)--(3.4) gives the exact charge

\[
 I_L(g)
 \le {L\over\eta a(L-2a)}
       \delta\min\{g,L-\lambda\}.                  \tag{3.5}
\]

For a short-band successor the unconditional bound `I_L(g)<=L` is used.
In each of the prefix and suffix complement gaps, all but at most `L`
positions have the one available gap-contained window.  Thus the two word
boundaries cost at most `2L` positions in total.

## 4. Finite general boundary--seam inequality

### Theorem 4.1

For every fixed `c>0` and `0<eta<2-c`,

\[
\boxed{
 M_a-\sum_{j=1}^m\lambda_j
 \le |R_a(c)|
   +{L\over\eta a(L-2a)}a^3H_a(c)
   +L n_a(c,\eta)+2L+m.}                            \tag{4.1}
\]

### Proof

Let `U` be the vertex union of the dangerous plateaux.  Every complement
position except the positions counted by (3.1), and the analogous boundary
exceptions, has a valid one-sided window wholly contained in its complement
gap.  It therefore belongs to `R_a(c)`.

For an internal gap whose successor lies in the short band, charge at most
`L` positions.  For every other internal gap apply (3.5), then sum (2.2).
The two outside gaps cost at most `2L`.  Consequently

\[
 M_a-|U|
 \le |R_a(c)|
   +{L\over\eta a(L-2a)}a^3H_a(c)
   +L n_a(c,\eta)+2L.                               \tag{4.2}
\]

Distinct plateau vertex intervals share at most endpoints.  Therefore

\[
                  0\le |U|-\sum_j\lambda_j\le m,   \tag{4.3}
\]

and (4.1) follows.  No convergence or atomicity assumption is used.
\(\square\)

The finite coefficients in (4.1) are explicit.  After division by `a^2`,

\[
 {L\over L-2a}\longrightarrow2,
 \qquad {L\over a}\longrightarrow4.                \tag{4.4}
\]

The number `m` is `O_c(a)` because the dangerous plateau edges are disjoint
and each plateau has more than `ca` edges.

## 5. Passage to a general profile

Assume, along one subsequence,

\[
 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
       \Longrightarrow\mu.                         \tag{5.1}
\]

Take `c` and `c+eta` to be continuity points of `mu`.  Then

\[
 {1\over a^2}\sum_{\lambda_j>ca}\lambda_j
       \longrightarrow\sigma_c,
 \qquad
 {n_a(c,\eta)\over a}\longrightarrow\nu(c,\eta). \tag{5.2}
\]

Define

\[
 r(c)=\limsup_{a\to\infty}{|R_a(c)|\over a^2},
 \qquad
 H(c)=\limsup_{a\to\infty}H_a(c).                 \tag{5.3}
\]

Divide (4.1) by `a^2`, take `a->infinity` with `c,eta` fixed, and use
(4.4).  This proves the first inequality in (1.2):

\[
                  3-\sigma_c
        \le r(c)+{2\over\eta}H(c)+4\nu(c,\eta).    \tag{5.4}
\]

The audited subset run-spectrum inequality gives, for each fixed
`0<c<2/3` under `D=o(a^2)`,

\[
                              r(c)\le{9\over4}c^2.   \tag{5.5}
\]

Equations (5.4) and (5.5) prove (1.2).  Since every `x` in
`(c,c+eta]` is greater than `c`,

\[
                       \nu(c,\eta)\le{\tau(c,\eta)\over c},     \tag{5.6}
\]

which proves the weighted short-band variant.

The displayed profile form is asserted at continuity endpoints.  At an atom
one should retain the sequence-level statement (4.1), or explicitly define
matching one-sided threshold limits.  All later small-`c` conclusions may be
taken through continuity points, since a finite measure has only countably
many atoms.

## 6. Fixed-parameter limit order and saturation

The prelimit order is essential:

1. fix numerical `c>0` and `eta>0`;
2. let `a->infinity` along the profile subsequence;
3. make any subsequent choice of `eta` inside the already limiting
   inequality;
4. only afterward let `c downarrow 0`.

Neither `c=c(a)` nor `eta=eta(a)` is used.

For fixed `c`, continuity from above gives

\[
                         \nu(c,\eta)\longrightarrow0
                         \quad(\eta\downarrow0).     \tag{6.1}
\]

Thus, if `H(c)=0`, (1.2) yields (1.3).  If this holds for arbitrarily small
continuity points, then `sigma_c<=sigma<=3` and `sigma_c->sigma`, so
`sigma=3`.

More generally suppose only that `H(c)->0` as `c downarrow0`.  After the
`a`-limit has already been taken, choose

\[
                         \eta(c)=c+\sqrt{H(c)}       \tag{6.2}
\]

(with `eta(c)` perturbed, if necessary, so that `c+eta(c)` is a continuity
point while `eta(c)` remains between one half and one times the displayed
value).  Then, with an inessential factor two if a perturbation was needed,

\[
 {H(c)\over\eta(c)}\le2\sqrt{H(c)},
 \qquad
 \nu(c,\eta(c))
 \le\mu((0,2c+\sqrt{H(c)}])\longrightarrow0.        \tag{6.3}
\]

The last limit remains true even if `mu` has an atom at zero, because the
interval excludes zero.  Sending `c downarrow0` in (1.2) proves (1.4).

This proves a broad exclusion theorem:

> Every general limiting profile with `sigma<3` must retain nonvanishing
> first-dangerous seam mass along some sequence of thresholds tending to
> zero.

## 7. The remaining variational problem

Eliminating `r(c)` from (1.2) gives the new necessary seam lower bound

\[
 H(c)\ge {1\over2}
 \sup_{\substack{0<\eta<2-c\\c+\eta\ \text{ a continuity point}}}
 \eta\left[
  3-\sigma_c-{9\over4}c^2-4\mu((c,c+\eta])
 \right]_+
 =:\mathcal B_c(\mu),                              \tag{7.1}
\]

for every continuity point `0<c<2/3`.  The corrected scalar laws therefore
leave the following precise feasibility problem.  Determine whether there
is a finite measure `mu` on `[0,2]` and a seam function `H` such that

\[
\begin{array}{ll}
\text{edge mass:}
 &\displaystyle \sigma=\int x\,d\mu(x)\le3,\\[2mm]
\text{line capacity:}
 &\displaystyle \mu([x,2])\le6(2-x)\quad(x>1),\\[2mm]
\text{mass law:}
 &\displaystyle 2e(c)+H(c)\ge4-3c,\\[1mm]
\text{weighted supply:}
 &\displaystyle S(c):=\int_{(c,2]}(4-x)\,d\mu(x)
       \ge{4-3c\over2-c},\\[2mm]
\text{seam upper bounds:}
 &\displaystyle 0\le H(c)\le
    \min\{(4-c)e(c),(2-c)(3-\sigma)\},\\[2mm]
\text{boundary lower bound:}
 &\displaystyle H(c)\ge\mathcal B_c(\mu)
       \quad(0<c<2/3),
\end{array}                                        \tag{7.2}
\]

where

\[
                         e(c)=\int(x-c)_+\,d\mu(x). \tag{7.3}
\]

The mass and supply inequalities do not close (7.2).  For example, take

\[
                         \mu=2\delta_{4/3},
 \qquad d:=3-\sigma={1\over3}.                      \tag{7.4}
\]

For `0<c<2/3`, set

\[
 H(c)={4/3-c\over2}
       \left[d-{9\over4}c^2\right]_+,              \tag{7.5}
\]

and set `H(c)=0` for `2/3<=c<2`.  If `c+eta<4/3`, the short-band count is
zero and (7.5) is exactly the lower bound (7.1), equivalently the full
inequality (1.2) with the extremal allowed choice `r(c)=9c^2/4`, after
taking `eta up to 4/3-c`; if `c+eta>=4/3`, the term
`4 nu(c,eta)=8` makes (1.2) automatic.  The function (7.5) also obeys both
seam upper bounds.  The corrected mass law has slack

\[
       2e(c)-(4-3c)={4\over3}-c\ge0,
\]

and the weighted supply and line-capacity laws hold exactly as in the
audited scalar profile calculation.

Thus (7.4)--(7.5) is an abstract feasible point of all currently proved
scalar and boundary inequalities.  It is not asserted to be geometrically
realizable.  It proves that the present laws do not force edge saturation
without a small-seam hypothesis.

The remaining problem is consequently not to reprove an edge-mass or
weighted-supply estimate.  It is to rule out the positive-seam feasible
region in (7.2), either by a genuinely stronger lower/upper coupling for
`H`, by a transition/level constraint not encoded by `mu`, or by showing
that equality-compatible seam patterns cannot arise from directed peak
plateaux in one word.

## 8. Ledger

### Proved

* The exact gap-loss formula (3.1).
* The finite boundary--seam inequality (4.1).
* The general profile inequality (1.2), with constants `2/eta`, `4`, and
  `9/4`.
* Edge saturation for every profile with `H(c)->0` as `c downarrow0` in the
  sequential fixed-threshold sense.
* The necessary variational seam lower bound (7.1).

### Not proved

* That the scalar mass and weighted-supply laws force `H(c)->0`.
* Exclusion of positive-seam unsaturated profiles satisfying (7.2).
* Geometric realization of the abstract example (7.4)--(7.5).
* The full three-box obstruction.
