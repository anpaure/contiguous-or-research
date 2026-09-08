# Reciprocal-height saturation forces linearly many canonical PBBS reframings

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2m+1,
 \qquad B_m=\operatorname {Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  Let \(\tau=\phi^2\) be the normalized
step-two PBBS permutation on semilength-\(m\) Dyck roots.

This note proves a strict version of the reciprocal-height packing bound
for every family whose canonical first-deepest frame changes sublinearly
often along its return traces.

For a Dyck root \(D\) of height \(h\), transport its canonical first
deepest spine through one application of the literal sector formula.  Call
the transition \(D\mapsto\tau D\) a **frame change** if that transported
spine is not the canonical first deepest spine of \(\tau D\).  For a
return interval \(I\), let \(s(I)\) be its step-two core duration, let
\(h(I)\) be its invariant Dyck height, and let \(R(I)\) be the number of
frame changes among the first \(s(I)-1\) core transitions.

The main quantitative theorem is the following.  For every fixed
\(0<a<A\), every integer

\[
 1\le q\le
 \left\lfloor{\lceil a\sqrt m\rceil\over4}\right\rfloor,
\]

and every pairwise quotient-edge-disjoint family \(\mathcal P\) of
nonwrapping PBBS returns with \(s(I)\le H_A\),

\[
 \boxed{
 \#\left\{I\in\mathcal P:
    a\sqrt m\le h(I)\le A\sqrt m,
    \ R(I)\le {s(I)\over4q}
 \right\}
 \le C_{a,A}\,2^{-q}{B_m\over\sqrt m}.}
 \tag{0.1}
\]

All floors can be inserted in the displayed height bounds without changing
the proof; Section 4 states the integer form used in the counting.

Consequently, if \(q_m\to\infty\) and \(q_m=o(\sqrt m)\), returns with

\[
 R(I)\le {s(I)\over4q_m}
\]

contribute \(o_{a,A}(B_m/\sqrt m)\) on every fixed Gaussian height band.
Equivalently, for fixed \(0<a<A\),

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}\limsup_{m\to\infty}
 {\sqrt m\over B_m}
 \#\left\{I\in\mathcal P:
 a\sqrt m\le h(I)\le A\sqrt m,
 R(I)\le\varepsilon s(I)
 \right\}=0.}
 \tag{0.2}
\]

The small-height reciprocal trace has a uniformly vanishing coefficient:
there is a function \(\eta(a)\downarrow0\) such that

\[
 \limsup_{m\to\infty}{\sqrt m\over B_m}
 \sum_{h<a\sqrt m}{b_{m,h}\over h+2}
 \le \eta(a).
 \tag{0.3}
\]

Thus any packing which saturates a positive fraction of the critical scale
\(B_m/\sqrt m\) must, after discarding a vanishing small-height part,
contain a positive fraction of intervals with a **linear density of genuine
canonical frame changes**.  The unchanged-spine protected cone, boundedly
many changes, and every sublinear-change extension are all too small.

This is a chronology-sensitive vanishing improvement, but not yet the full
coefficient-one gate.  The exact residual is the linearly reframing class.
No genuine PBBS family of mass \(\Theta(B_m/\sqrt m)\) in that class is
constructed here, and no claim that the full packing is little-oh is made.
The false implication from \(d(D)=1\) to a height return is nowhere used.

## 1. Literal frames and the partial-horizon atlas

Let \(D\) have height \(h\).  Along its canonical first deepest spine,
write its contour as

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1
     0B_{h-1}0\cdots0B_1\,0B_0.                 \tag{1.1}
\]

Here \(A_k\) and \(B_k\) are the ordered forests before and after the
spine child at depth \(k\).  The literal block rotation gives

\[
 \tau D=B_0\,1A_0\,1A_1\cdots1A_{h-1}\,0
              0B_{h-1}0\cdots0B_1.              \tag{1.2}
\]

If the displayed transported spine stays canonical, the sector update is

\[
 A'_0=B_0,
 \qquad A'_i=A_{i-1}\ (1\le i<h),                \tag{1.3}
\]

\[
 B'_i=B_{i+1}\ (0\le i<h-1),
 \qquad B'_{h-1}=\varnothing.                    \tag{1.4}
\]

Call \(D\) **\(q\)-stable** if this same displayed spine remains the
canonical first deepest spine through rounds \(0,1,\ldots,q\).  Thus
\(0\)-stability is vacuous, while \(q\)-stability asserts that the next
\(q\) transitions are frame-preserving.

Let \(C_j(z)\) count ordered Dyck forests of height at most \(j\), with

\[
 C_0(z)=1,
 \qquad C_j(z)={1\over1-zC_{j-1}(z)}\quad(j\ge1). \tag{1.5}
\]

We use the convention that a forest of height zero is empty.  Define

\[
 F_0(z)=F_1(z)=1,
 \qquad F_{j+1}(z)=F_j(z)-zF_{j-1}(z).            \tag{1.6}
\]

Then

\[
 C_j(z)={F_j(z)\over F_{j+1}(z)}.                \tag{1.7}
\]

Let \(c_{m,h}^{(q)}\) be the number of semilength-\(m\), height-\(h\),
\(q\)-stable roots.

### Lemma 1.1 (exact partial-horizon sector count)

For \(0\le q\le h\),

\[
 c_{m,h}^{(q)}=[z^{m-h}]
 \prod_{k=0}^{h-1}
 C_{\max\{h-k-q-1,0\}}(z)
 C_{h-\max\{k,q-k\}}(z).                         \tag{1.8}
\]

In particular, coefficientwise,

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(q)}z^m
 \preceq {z^h\over F_{h-q}(z)F_{h+1}(z)}.}
 \tag{1.9}
\]

#### Proof

Under the formal update, an original \(A_k\) is at earlier depth \(k+j\)
at round \(j\), until it reaches the bottom.  It must stay strictly below
height \(h\).  The strongest restriction over \(0\le j\le q\) is

\[
 \operatorname {ht}(A_k)
 \le\max\{h-k-q-1,0\}.                            \tag{1.10}
\]

An original \(B_k\) remains after the spine while \(j\le k\), where the
original cap is \(h-k\).  For \(j>k\), it lies before the spine at depth
\(j-1-k\); the strongest strict cap occurs at \(j=q\).  Hence

\[
 \operatorname {ht}(B_k)
 \le\min\{h-k,h-q+k\}
 =h-\max\{k,q-k\}.                                \tag{1.11}
\]

These conditions are also sufficient: every earlier forest stays strictly
below height \(h\), every later forest stays at or below height \(h\), and
the displayed spine reaches height \(h\).  The forests are independent
once the spine is fixed, so (1.8) follows.

For (1.9), relax the \(B_k\)-cap in (1.11) to its original value \(h-k\).
All coefficients are nonnegative, and therefore the resulting product is

\[
 \begin{aligned}
 &z^h
 \prod_{k=0}^{h-1}C_{\max\{h-k-q-1,0\}}(z)
 \prod_{k=0}^{h-1}C_{h-k}(z)\\
 &\qquad =z^h
 \left(\prod_{j=1}^{h-q-1}C_j(z)\right)
 \left(\prod_{j=1}^{h}C_j(z)\right)
 ={z^h\over F_{h-q}(z)F_{h+1}(z)},
 \end{aligned}                                    \tag{1.12}
\]

by telescoping (1.7).  Empty products cover \(q=h-1,h\).  This proves
(1.9).  \(\square\)

The point of (1.9) is that a chronology condition extending over \(q\)
actual PBBS transitions becomes a product of only two finite-strip
kernels, with an exact displacement \(q\).

In fact the product in (1.8) telescopes completely.  This refinement is
useful because it shows that the factor \(2^{-q}\) below is intrinsic to
the partial atlas, rather than a loss in the relaxation (1.9).

### Corollary 1.2 (closed partial-atlas kernel)

If \(q=2r\), then

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(2r)}z^m
 ={z^h\over F_{h-r}(z)F_{h-r+1}(z)}.}
 \tag{1.13}
\]

If \(q=2r+1\), then

\[
 \boxed{
 \sum_{m\ge h}c_{m,h}^{(2r+1)}z^m
 ={z^h\over F_{h-r}(z)^2}.}
 \tag{1.14}
\]

#### Proof

Suppose first that \(q=2r\).  The \(A\)-factor in (1.8) is

\[
 \prod_{j=1}^{h-2r-1}C_j={1\over F_{h-2r}}.       \tag{1.15}
\]

For \(k<r\), the \(B_k\)-cap runs through
\(h-2r,h-2r+1,\ldots,h-r-1\).  For \(k\ge r\), it runs through
\(h-r,h-r-1,\ldots,1\).  Therefore the \(B\)-factor is

\[
 \left(\prod_{j=1}^{h-r}C_j\right)
 \left(\prod_{j=h-2r}^{h-r-1}C_j\right)
 ={1\over F_{h-r+1}}{F_{h-2r}\over F_{h-r}}.     \tag{1.16}
\]

Multiplication by (1.15) proves (1.13).  Empty products and \(F_0=1\)
cover the endpoint \(2r=h\).

If \(q=2r+1\), the \(A\)-factor is \(1/F_{h-2r-1}\).  The two parts of
the \(B\)-factor are

\[
 \prod_{j=1}^{h-r-1}C_j
 \quad\hbox{and}\quad
 \prod_{j=h-2r-1}^{h-r-1}C_j,
\]

whose product is

\[
 {1\over F_{h-r}}{F_{h-2r-1}\over F_{h-r}}.      \tag{1.17}
\]

The \(A\)-factor cancels the numerator, proving (1.14).  \(\square\)

At \(z=1/4\), (2.5) below gives the exact retention relative to the full
height-\(h\) class.  With \(w=h-r\), both parities give

\[
 {\sum_m c_{m,h}^{(q)}4^{-m}
  \over
  \sum_m c_{m,h}^{(0)}4^{-m}}
 =2^{-q}\,{(h+1)(h+2)\over
 (w+1)(w+2-\mathbf 1_{\{q\text{ odd}\}})}.
 \tag{1.18}
\]

For \(q=o(h)\), this is \((1+o(1))2^{-q}\).  Thus the exponential in
\(q\) used below is coefficient-exact at the critical Boltzmann point.

## 2. Gaussian coefficient of the partial atlas

Put

\[
 A_j(x)={x^j\over F_j(x^2)},
 \qquad
 G_j(x)={x^j\over F_{j+1}(x^2)}.                  \tag{2.1}
\]

For their normalized coefficients write

\[
 u_j(n)=2^{-n}[x^n]A_j(x),
 \qquad
 v_j(n)=2^{-n}[x^n]G_j(x).                        \tag{2.2}
\]

The finite path-graph expansion gives absolute constants \(c,C>0\) such
that

\[
 \|u_j\|_1={1\over j+1},
 \qquad
 \|v_j\|_1={2\over j+2},                         \tag{2.3}
\]

and

\[
 u_j(n)\le {C\over(j+1)^3}
       \exp\!\left(-{cn\over(j+1)^2}\right),
 \qquad
 v_j(n)\le {C\over(j+2)^3}
       \exp\!\left(-{cn\over(j+2)^2}\right).    \tag{2.4}
\]

For completeness, (2.3) follows by evaluating at \(x=1/2\) and using

\[
 F_j(1/4)={j+1\over2^j}.                           \tag{2.5}
\]

For times at least the square of the strip width, (2.4) follows by pairing
the two endpoint modes in the path-graph diagonalization and using the
spectral gap \(1-\cos(\pi/(j+2))\asymp j^{-2}\).  Below that time,
two-barrier reflection gives

\[
 C(n+1)^{-3/2}
 \exp\!\left(-c{(j+1)^2\over n+1}\right)
 \le C'(j+1)^{-3},                                \tag{2.6}
\]

and the same estimate for the terminal corridor.  Combining the two time
ranges proves (2.4).  No termwise absolute-value bound at short time is
used.

### Lemma 2.1 (the \(2^{-q}\) Gaussian contraction)

Fix \(0<a<A\).  There is \(C_{a,A}<\infty\) such that, whenever

\[
 \lceil a\sqrt m\rceil\le h\le\lfloor A\sqrt m\rfloor,
 \qquad 0\le q\le h/2,
\]

one has

\[
 \boxed{
 c_{m,h}^{(q)}
 \le C_{a,A}4^m2^{-q}h^{-4}.}                    \tag{2.7}
\]

Consequently

\[
 \boxed{
 \sum_{\lceil a\sqrt m\rceil
       \le h\le\lfloor A\sqrt m\rfloor}
 c_{m,h}^{(q)}
 \le C_{a,A}2^{-q}B_m.}                          \tag{2.8}
\]

#### Proof

Write \(q=2r\) or \(q=2r+1\), and put \(w=h-r\).  Corollary 1.2 and
the substitution \(z=x^2\) give, respectively,

\[
 x^qA_w(x)G_w(x)
 \quad\hbox{or}\quad
 x^{q-1}A_w(x)^2.                                 \tag{2.9}
\]

Thus the normalized convolution is multiplied by \(2^{-q}\) in the even
case and by \(2^{-(q-1)}\le2^{1-q}\) in the odd case.  Since
\(q\le h/2\), both strip widths in (2.9) are between a positive
multiple of \(\sqrt m\) and a fixed multiple of \(\sqrt m\).  Also
the remaining coefficient index is at least \(m\) for all sufficiently
large \(m\).  In each convolution
term, one of the two times is at least \((2m-q)/2\).  Apply (2.4) to that
factor and sum the other factor with (2.3).  In either case this gives

\[
 (u_w*v_w)(2m-q)\le C_{a,A}h^{-4},
 \qquad
 (u_w*u_w)(2m-q+1)\le C_{a,A}h^{-4}.              \tag{2.10}
\]

Equations (1.13)--(1.14), (2.9), and (2.10) prove (2.7).  Finally,

\[
 \sum_{h\ge a\sqrt m}h^{-4}\le C_a m^{-3/2},
 \qquad
 B_m\asymp4^m m^{-3/2},                           \tag{2.11}
\]

which proves (2.8), after enlarging the constant to cover finitely many
small \(m\).  \(\square\)

## 3. Stable-window witnesses inside an edge-disjoint return packing

Consider a return interval \(I\) with step-two core roots

\[
 D_0(I),D_1(I),\ldots,D_{s(I)-1}(I).              \tag{3.1}
\]

Dyck height is invariant under \(\tau\), so all roots in (3.1) have the
same height \(h(I)\).  The exact peak-deletion height-gap theorem gives

\[
 s(I)\ge h(I).                                    \tag{3.2}
\]

This statement is valid for every winding.  In the zero-winding equality
case one has \(s(I)=h(I)\), but equality is not assumed below.

There are \(s-q\) possible length-\(q\) transition windows wholly inside
(3.1), starting at \(0\le t\le s-q-1\).  One frame change invalidates at
most \(q\) of these starts.  Therefore the number of \(q\)-stable roots
among (3.1) is at least

\[
 s-q-qR(I).                                       \tag{3.3}
\]

In particular, if

\[
 q\le s/4,
 \qquad R(I)\le{s\over4q},                        \tag{3.4}
\]

then (3.3) is at least \(s/2\).

If the return intervals form a pairwise quotient-edge-disjoint nonwrapping
packing, all core roots (3.1), over all selected intervals, are distinct.
Thus the stable roots furnished by (3.3) are also distinct globally.
This is the step which couples the chronology factor to the edge-volume
factor; no independence of two marginal counts is asserted.

### Theorem 3.1 (slow-reframing packing contraction)

Fix \(0<a<A\).  For all sufficiently large \(m\), every integer

\[
 1\le q\le {a\sqrt m\over4},                      \tag{3.5}
\]

and every pairwise quotient-edge-disjoint nonwrapping family \(\mathcal P\)
of returns with \(s(I)\le H_A\), inequality (0.1) holds.

#### Proof

For every interval counted on the left side of (0.1), (3.2) and (3.5)
give \(q\le s(I)/4\).  Equations (3.3)--(3.4) therefore furnish at least

\[
 {s(I)\over2}\ge{h(I)\over2}\ge {a\sqrt m\over2} \tag{3.6}
\]

distinct \(q\)-stable core roots.  Global edge-disjointness and (2.8)
give

\[
 {a\sqrt m\over2}\,|\mathcal P_{\mathrm{slow}}|
 \le
 \sum_{\lceil a\sqrt m\rceil
       \le h\le\lfloor A\sqrt m\rfloor}
 c_{m,h}^{(q)}
 \le C_{a,A}2^{-q}B_m.                            \tag{3.7}
\]

Absorb \(2/a\) into the constant.  This proves (0.1).  \(\square\)

This proof uses the actual sequence of canonical frames along each return.
It neither replaces the sequence by a prescribed static overlay nor treats
the necessary condition \(d(D)=1\) as sufficient.

## 4. Floors, small heights, and the saturation consequence

For literal integer bounds, define

\[
 h_-(m)=\lceil a\sqrt m\rceil,
 \qquad h_+(m)=\lfloor A\sqrt m\rfloor.
 \tag{4.1}
\]

If \(h_->h_+\), the family in (0.1) is empty.  Otherwise use

\[
 1\le q\le\left\lfloor{h_-(m)\over4}\right\rfloor,
 \qquad
 R(I)\le\left\lfloor{s(I)\over4q}\right\rfloor. \tag{4.2}
\]

Then (3.6)--(3.7) apply verbatim.  Thus no rounding error is hidden in
(0.1).  If one instead parametrizes a residence bound by the convention
that the final odd edge is included, so that \(s(I)+1\le H_A\), one may
replace \(h_+(m)\) by

\[
 \min\{\lfloor A\sqrt m\rfloor,H_A-1\}.
\]

The two conventions differ only at the displayed endpoint, but they must
not be interchanged inside an exact floor statement.

For the small-height contribution, let \(b_{m,h}\) be the number of
semilength-\(m\) Dyck roots of height \(h\).  The spectral path-graph
bound gives, for \(h\le\sqrt m\),

\[
 \#\{D:\operatorname {ht}(D)\le h\}
 \le C B_m\left({\sqrt m\over h}\right)^3
          \exp\!\left(-c{m\over h^2}\right).     \tag{4.3}
\]

Split \(h<a\sqrt m\) into dyadic bands

\[
 2^{-j-1}\sqrt m<h\le2^{-j}\sqrt m.
\]

On such a band its contribution to the reciprocal-height trace is at most

\[
 C{B_m\over\sqrt m}\,2^{4j}e^{-c4^j}.           \tag{4.4}
\]

The tail of this summable series tends to zero as its first index tends to
infinity.  This proves (0.3), with for example

\[
 \eta(a)=C\sum_{2^{-j}\le2a}2^{4j}e^{-c4^j}.      \tag{4.5}
\]

Now fix \(0<a<A\).  If \(q_m\to\infty\) and
\(q_m=o(\sqrt m)\), Theorem 3.1 gives

\[
 \#\{I:a\sqrt m\le h(I)\le A\sqrt m,
 R(I)\le s(I)/(4q_m)\}
 =o_{a,A}(B_m/\sqrt m).                            \tag{4.6}
\]

To obtain (0.2), for sufficiently small \(\varepsilon>0\) choose

\[
 q=\left\lfloor{1\over8\varepsilon}\right\rfloor.
\]

Then \(\varepsilon s\le s/(4q)\) for all sufficiently small
\(\varepsilon\), while (0.1) bounds the normalized limsup by

\[
 C_{a,A}2^{-q}
 \le C_{a,A}2^{-1/(8\varepsilon)+1},              \tag{4.7}
\]

which tends to zero with \(\varepsilon\).  This proves (0.2).

Finally suppose a sequence of packings has

\[
 \limsup_{m\to\infty}{\sqrt m\,|\mathcal P_m|\over B_m}>0. \tag{4.8}
\]

First choose \(a>0\) so that (0.3) removes less than half of this limsup.
Then (0.2) shows that, for some \(\varepsilon>0\), a positive normalized
subfamily satisfies

\[
 R(I)>\varepsilon s(I).                            \tag{4.9}
\]

Thus linear-density reframing is a necessary condition for critical
reciprocal-height saturation.

## 5. Exact boundary

The following statements are proved.

1. A \(q\)-step chronology-preserving canonical frame has the exact
   partial-sector count (1.8) and the two-strip majorant (1.9).
2. On every fixed Gaussian height band, the total mass of such roots is
   at most \(C_{a,A}2^{-q}B_m\), with the full displacement factor and no
   missing floor.
3. Edge-disjoint return traces convert this root-mass contraction into the
   packing contraction (0.1).
4. Every sublinearly reframed return family, of arbitrary winding, is
   \(o_{a,A}(B_m/\sqrt m)\).
5. Small heights have a uniformly vanishing reciprocal-height coefficient,
   so any critical near-saturator must be Gaussian and linearly reframing.

What remains unproved is an estimate for return intervals which change
their canonical first-deepest frame on a positive fraction of their
step-two transitions.  The one-step frame-change condition is not itself
rare: a pre-spine forest one level below the maximum can become first
deepest after transport.  Therefore the present theorem cannot be extended
by charging frame changes only through their one-time marginal count.
The missing statement must use compatibility among a linear number of
successive reframings, or construct a genuine exact PBBS near-saturator
realizing that compatibility.

The companion report
`MATH_ATTACK_GAUSSIAN_STAR_COMB_LINEAR_REFRAMING_20260725.md` proves that
this residual is nonempty with the strongest pointwise quantifiers: it
constructs Gaussian, zero-winding, endpoint-overlap-zero returns with
\(R=s-1\), all caused by relative height-one stars.  That family has only
\(\exp(o(m))\) roots, so it closes deterministic frame-change charges but
does not close or refute the aggregate packing theorem.

The primitive height converse remains retracted throughout.  In
particular, this report proves no unconditional coefficient-one theorem.
