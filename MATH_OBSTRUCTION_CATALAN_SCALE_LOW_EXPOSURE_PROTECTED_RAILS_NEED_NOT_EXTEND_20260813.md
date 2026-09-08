# Catalan-scale low-exposure protected rails need not extend

**Date:** 2026-08-13  
**Status:** unconditional analytic obstruction; no computation or search.

## 0. Result

Let `ML_r` be the balanced incidence graph between

\[
 \mathcal L={ [2r-1]\choose r-1},\qquad
 \mathcal U={ [2r-1]\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|.
\]

For all sufficiently large `r` there is a vertex-disjoint incidence path
forest `P` such that

1. every component has two edges;
2. its owner, lower-colour, and immediate-upper-colour resources are
   pairwise distinct;
3. its two **all-occurrence** exposures are at most `8 sqrt(r)`;
4. `|E(P)|=Theta(W/sqrt(r))`; but
5. no spanning two-factor of `ML_r` contains `P`.

Consequently a Catalan-scale backup bank cannot be inserted merely from

\[
 |E(P)|=O(W/\sqrt r),\qquad
 \widehat\alpha(P),\widehat\beta(P)=O(\sqrt r).
\]

Any positive theorem for the tensorized `T2` backup rails must use an
additional global cut-balancing invariant, their exact tensor geometry, or
a conformal alternating replacement of an existing factor.

## 1. The full crossing-path catalogue

Fix a coordinate `infinity` and split both shores according to whether it
is present.  Put

\[
 A=|\mathcal U_1|=|\mathcal L_0|
   ={2r-2\choose r-1},\qquad
 B=|\mathcal L_1|=|\mathcal U_0|
   ={2r-2\choose r-2}.
\]

Then

\[
 {B\over A}={r-1\over r},\qquad
 \Delta=A-B={A\over r}.                              \tag{1.1}
\]

The incidence graph between `mathcal U_0` and `mathcal L_0` has left
degree `r` and right degree `r-1`.  Hall therefore gives an injection

\[
 f:\mathcal U_0\longrightarrow\mathcal L_0,
 \qquad f(U)\subset U.                               \tag{1.2}
\]

For each `U in mathcal U_0`, put

\[
 z_U=f(U),\qquad U^+=z_U\cup\{\mathord\infty\},
\]

and take the two-edge incidence path

\[
                         U-z_U-U^+.                   \tag{1.3}
\]

All zero-side owners `U`, all lower vertices `z_U`, and all one-side
owners `U^+` are distinct.  The immediate-upper colour is
`U union {infinity}`, so those colours are distinct as well.

For a subfamily `Q` of these paths define the stronger exposures

\[
 \widehat\alpha(Q)=
 \max_{x\in\mathcal L}
 |\{Y\in V(Q)\cap\mathcal U:x\subset Y\}|,           \tag{1.4}
\]

\[
 \widehat\beta(Q)=
 \max_{Y\in\mathcal U}
 |\{z\in V(Q)\cap\mathcal L:z\subset Y\}|.          \tag{1.5}
\]

In the complete catalogue, every row in `(1.4)` and `(1.5)` has total
load at most `r`.  Indeed, a lower vertex lies below at most `r` displayed
endpoint owners, counting the possible path whose two endpoints both
contain its central facet; and an owner has only `r` facets, while `f` is
injective.

## 2. A balanced colouring of the catalogue

Put

\[
                         t=\lceil\sqrt r\rceil.
\]

Colour every path in the complete catalogue independently and uniformly
with one of `t` colours.  For every exposure row and every colour, declare
the event that its monochromatic load exceeds `8 sqrt(r)` to be bad.

One exposure row depends on at most `r` path variables, with individual
weights at most two and total weight at most `r`.  Its mean in one colour
is at most `sqrt(r)`.  Bernstein's inequality therefore gives, for an
absolute `c>0`,

\[
 \Pr(\text{one bad event})\le \exp(-c\sqrt r).       \tag{2.1}
\]

One path variable occurs in at most `2r` lower-exposure rows, one for each
facet of either endpoint owner, and in at most `r` upper-exposure rows,
one for each owner above its central facet.  After the colour is specified,
a bad event is consequently dependent on at most

\[
                         3r^2t=O(r^{5/2})             \tag{2.2}
\]

other bad events.  Equations `(2.1)--(2.2)` satisfy the symmetric Lovasz
local lemma for all sufficiently large `r`.  Hence the complete catalogue
has a `t`-colouring in which every colour class `Q_j` obeys

\[
 \widehat\alpha(Q_j),\widehat\beta(Q_j)le8\sqrt r. \tag{2.3}
\]

Some colour class contains at least `B/t` paths.  Retain exactly

\[
                         N=\lfloor B/t\rfloor         \tag{2.4}
\]

of them and call their union `P`.  The exposure bounds persist, and

\[
                         |E(P)|=2N=\Theta(W/\sqrt r).\tag{2.5}
\]

## 3. The exact failed coordinate cut

Take the residual lower shore

\[
                         \mathcal A=\mathcal L_1.    \tag{3.1}
\]

Every protected lower vertex lies in `mathcal L_0`, so `(3.1)` is an
allowed residual shore.  Its neighbourhood is `mathcal U_1`.  Every
selected path has exactly one protected owner endpoint in `mathcal U_1`,
of protected degree one.  Since every owner in `mathcal U_1` has `r-1`
neighbours in `mathcal A`, at least its residual capacity, the exact
capacitated Hall value is

\[
 \kappa(\mathcal A)
   =\sum_{Y\in\mathcal U_1}(2-d_P(Y))
   =2A-N.                                             \tag{3.2}
\]

On the other hand `|mathcal A|=B`.  By `(1.1)` and `(2.4)`,

\[
 {B/t\over2\Delta}={r-1\over2t}>1                  \tag{3.3}
\]

for all sufficiently large `r`; the floor is harmless.  Thus `N>2Delta`
and

\[
 \kappa(\mathcal A)=2A-N
       <2A-2\Delta=2B=2|\mathcal A|.                \tag{3.4}
\]

The residual Hall inequality fails, proving that no spanning two-factor
contains `P`.

## 4. Consequence for the `T2` backup lane

The private `B/C/H` staircase rails have the promising local scale

\[
 O(h)\operatorname {Cat}_{m-6}
      =O(W/\sqrt m)
\]

when `h=Theta(sqrt(m))`, and their local exposure can be `O(h)`.  The
present theorem shows that these two numerical facts do not constitute a
factor-extension theorem.  A proof must additionally establish the exact
protected Ore cuts for that specific tensor bank, or realize the rails as
a degree-preserving alternating trade in an already spanning factor.

