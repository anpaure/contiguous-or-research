# Independent punctured residual degrees have vanishing relative variance

**Date:** 2026-08-21  
**Status:** analytic annealed variance theorem; no uniform or adaptive
trajectory concentration is claimed

## 1. Setup

Let `\mathcal C_r` be the directed punctured-configuration hypergraph,
let `D=D_M`, and retain lower and middle targets independently with
probabilities

\[
                         x,\qquad y={rx+2\over r+2}.             \tag{1.1}
\]

Fix a target `v` and condition on retaining it.  Let `X_v` be its degree in
the independently thinned residual and let `\mu_v=\mathbb E X_v`.  Thus
`\mu_v` is exactly the appropriate expression

\[
 D_Lx^{2r-1}y^{2r}\quad(v\in L),
 \qquad
 D_Mx^{2r}y^{2r-1}\quad(v\in M).                       \tag{1.2}
\]

We use the proved boundary-codegree inequality: for every target family
`T` inside one configuration, with `t=|T|` and `q=|V(B(T))|`,

\[
                         {\deg(T)\over D}\le C^t r^{2-q}.       \tag{1.3}
\]

### Theorem 1.1

For every fixed `alpha<1/3`, uniformly for `r^{-alpha}<=x<=1` and both
target layers,

\[
 \boxed{\qquad
 {\operatorname {Var}X_v\over\mu_v^2}
       \le {1\over\mu_v}+O_C\!\left({1\over r x^3}\right)
       =o(1).
 \qquad}                                               \tag{1.4}
\]

The last equality uses the exponential size of (1.2) in this density
range.

## 2. Exact covariance expansion

Write

\[
                         X_v=\sum_{F\ni v}I_F,                   \tag{2.1}
\]

where `I_F` says that every target of `F-v` survives.  All configurations
through a fixed layer-tagged `v` have the same monomial probability, say
`w_v=\mathbb E I_F`, and `\mu_v=d(v)w_v`.

For two configurations `F,G` through `v`, put `t=|F\cap G|`.  Every shared
target other than `v` has retention probability at least `x`, so

\[
 {\mathbb E(I_FI_G)\over\mathbb E I_F\,\mathbb E I_G}
       \le x^{-(t-1)}.                                  \tag{2.2}
\]

Put `a=x^{-1}-1`.  Then

\[
 x^{-(t-1)}-1
   =(1+a)^{t-1}-1
   =\sum_{\varnothing\ne S\subseteq(F\cap G)-\{v\}}a^{|S|}.   \tag{2.3}
\]

Fixing `F` and summing first over `G`, (2.3) gives

\[
 \sum_{G\ni v}\bigl(x^{-(|F\cap G|-1)}-1\bigr)
 \le
 \sum_{\varnothing\ne S\subseteq F-\{v\}}
      a^{|S|}\deg(\{v\}\cup S).                       \tag{2.4}
\]

The right side includes `G=F`, which is harmless for an upper bound.
Separating the diagonal variances in (2.1), using
`\operatorname {Var}I_F<=\mathbb E I_F`, and then dividing by
`\mu_v^2`, yields

\[
 {\operatorname {Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}
 +{1\over d(v)}
   \sum_{\varnothing\ne S\subseteq F-\{v\}}
       a^{|S|}\deg(\{v\}\cup S).                       \tag{2.5}
\]

## 3. A rooted boundary-polymer estimate

Let `R` be the boundary edge representing `v` inside `B(F)`, and put
`z=Ca`.  Since `d(v)>=D`, (1.3) bounds the second term of (2.5), up to one
factor `C`, by

\[
 \sum_{\varnothing\ne S\subseteq E(B_r)-\{R\}}
           z^{|S|}r^{2-|V(R\cup S)|}.                  \tag{3.1}
\]

We record the elementary rooted estimate used here.

### Lemma 3.1

For `0<=z<=c\sqrt r`, with `c>0` a sufficiently small absolute constant,

\[
 \sum_{\varnothing\ne S}
           z^{|S|}r^{2-|V(R\cup S)|}
   =O\!\left({z\over r}+{z^3\over r}+{z^4\over r^2}\right).   \tag{3.2}
\]

#### Proof

Decompose `R\cup S` into its connected component containing `R` and its
other connected components.  In the maximum-degree-four boundary graph,
the number of connected `m`-edge subgraphs containing a prescribed edge or
vertex is at most `A^m` for an absolute `A`.

The unrooted component activity is

\[
                         \eta_0=O(z/r+z^4/r^2),          \tag{3.3}
\]

by the bounded-degree boundary-polymer estimate.  Dropping mutual
vertex-disjointness multiplies the rooted sum by at most `exp(eta_0)`.

For completeness, the arboricity assertion used below follows directly
from cuts.  Multiplication by two identifies the boundary graph with
`Cay(Z_b,{\pm1,\pm3})` after deleting the two edges `{0,-1}` and `{0,-3}`.
For a nonempty proper vertex set `U`, the step-one Hamilton cycle has at
least two crossing edges.  The step-three subgraph has either at least two
crossing edges, or `3` divides `b` and `U` is a union of its full residue
cycles; in the latter case the step-one cut already has at least four
edges.  Hence the full circulant induces at most `2(|U|-1)` edges on `U`,
and deleting two edges cannot increase this number.  On the full vertex
set the punctured graph has exactly `2b-2=2(b-1)` edges.  The
Nash--Williams density criterion therefore gives arboricity at most two.

For the root component, one edge gives the root alone.  A second edge adds
at least one vertex and contributes `O(z/r)`.  Three edges span at least
four vertices when `b>=11`, because the step-`{1,3}` graph has no triangle;
their contribution is `O(z^2/r^2)`.  For `m>=4` total edges, arboricity at
most two gives

\[
                         |V|\ge m/2+1.                  \tag{3.4}
\]

The remaining rooted activity is therefore bounded by the geometric tail

\[
 \sum_{m\ge4}A^m z^{m-1}r^{1-m/2}
                         =O(z^3/r).                     \tag{3.5}
\]

Components disjoint from the root but with no nontrivial root component
contribute `exp(eta_0)-1`.  Equations (3.3)--(3.5) prove (3.2).  The
finitely many `b<11` are absorbed by the constant. `square`

## 4. Completion and scope

For `x>=r^{-alpha}`, fixed `alpha<1/3`, one has
`z=O_C(x^{-1})=o(r^{1/3})`, so Lemma 3.1 applies and `eta_0=o(1)`.  Equations
(2.5) and (3.2) give

\[
 {\operatorname {Var}X_v\over\mu_v^2}
 \le {1\over\mu_v}
 +O_C\!\left({a\over r}+{a^3\over r}+{a^4\over r^2}\right)
 \le {1\over\mu_v}+O_C\!\left({1\over r x^3}\right),  \tag{4.1}
\]

because `rx>=1` in this range.  This proves Theorem 1.1.

Chebyshev's inequality now gives fixed-target annealed concentration.  It
does not give the exponentially small failure probabilities needed to
union-bound over all targets, and it does not survive conditioning on an
adaptive nibble history.  Those tasks require high connected cumulants (or
an equivalent switching martingale) for multi-root overlap clusters; they
are not consequences of (1.4) alone.
