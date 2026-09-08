# Conflict-union compression and the initial off-star collision bound

**Date:** 2026-08-22  
**Status:** exact for every current hypergraph; initial punctured estimate
proved; the adaptive row-cap persistence remains open

This note compresses the union-exposure scalars which occur in the
factorial-moment microbite hierarchy.  The compression has two logically
different inputs.  An exact Bonferroni identity is valid in every current
residual hypergraph.  In the initial punctured configuration hypergraph,
the complete pair profile then makes its quadratic defect smaller by
`O_ell(1/r)`.  The scalar pair mass `S(e)` fixes the leading scale, while
the localization of that mass is what bounds the quadratic defect.  The
scalar `S(e)` alone is not enough for the latter conclusion.

## 1. Exact compression in an arbitrary hypergraph

Let `H` be a finite simple hypergraph with edge set `mathcal E`, and let
`V_sigma` be one of its shores.  Write

\[
 d_v=|\{F\in\mathcal E:v\in F\}|,
 \qquad
 \Gamma(F)=\{G\in\mathcal E:G\cap F\ne\varnothing\}.
                                                               \tag{1.1}
\]

For `G in mathcal E` and a target `v`, define the external conflict-row
entry

\[
 a_G(v)=|\{F\in\mathcal E:v\in F,\ F\cap G\ne\varnothing\}|.
                                                               \tag{1.2}
\]

Thus `0<=a_G(v)<=d_v`, and `a_G(v)=d_v` whenever `G` contains `v`.
For `d_v>0`, put

\[
 E_v={1\over d_v}\sum_{F\ni v}(|\Gamma(F)|-d_v).
                                                               \tag{1.3}
\]

Set `E_v=0` when `d_v=0`.

For an integer `ell>=1`, let `mathcal T_(ell,v)` be the ordered distinct
`ell`-tuples of edges through `v`, and put

\[
 G_{\ell,\sigma}=
 \sum_{v\in V_\sigma}
 \sum_{(F_1,\ldots,F_\ell)\in\mathcal T_{\ell,v}}
 \left|\bigcup_{i=1}^\ell\Gamma(F_i)\right|.          \tag{1.4}
\]

We use the combinatorial falling-factorial convention `(n)_j=0` whenever
`n<j` and `j>=1`, and `(n)_0=1`.  All nonzero applications have
nonnegative `n`; the extension only makes zero factors at small degrees
literal.

### Theorem 1.1 (exact conflict-row formula)

For every `ell>=1`,

\[
 \boxed{
 G_{\ell,\sigma}
 =\sum_{G\in\mathcal E}\sum_{v\in V_\sigma}
 \bigl[(d_v)_\ell-(d_v-a_G(v))_\ell\bigr].}
                                                               \tag{1.5}
\]

Define its linearized value

\[
 L_{\ell,\sigma}=
 \sum_{v\in V_\sigma}(d_v)_\ell[d_v+\ell E_v].       \tag{1.6}
\]

For `ell=1`, `G_(1,sigma)=L_(1,sigma)`.  For `ell>=2`,

\[
 \boxed{
 \begin{aligned}
 0\le L_{\ell,\sigma}-G_{\ell,\sigma}
 &\le {\ell\choose2}
 \sum_{v\in V_\sigma}\sum_{G\not\ni v}
 (a_G(v))_2(d_v-2)_{\ell-2}.
 \end{aligned}}                                      \tag{1.7}
\]

#### Proof

For fixed `G,v`, the total number of ordered distinct `ell`-tuples through
`v` is `(d_v)_ell`; exactly `(d_v-a_G(v))_ell` of them have no member
which meets `G`.  Therefore
their difference counts the tuples for which `G` lies in at least one of
the conflict neighbourhoods.  Summing first over `G` proves (1.5).

For later use, let a distinguished `a`-set lie inside a `d`-set.  Among
ordered distinct `ell`-tuples, write `m` for the number of selected entries
which lie in the distinguished set.  The union indicator is
`1_(m>=1)`, while the sum of its `ell` singleton indicators is `m`.
Consequently

\[
 \begin{aligned}
 0&\le \ell a(d-1)_{\ell-1}
       -[(d)_\ell-(d-a)_\ell]\\
  &\le {\ell\choose2}(a)_2(d-2)_{\ell-2},            \tag{1.8}
 \end{aligned}
\]

because `0<=m-1_(m>=1)<=binom(m,2)`.  If `G` contains `v`, then
`a_G(v)=d_v`, so its exact contribution to (1.5) is `(d_v)_ell`; there
are `d_v` such `G`.  On the other hand, double counting `(F,G)` gives

\[
 \sum_{G\not\ni v}a_G(v)
 =\sum_{F\ni v}(|\Gamma(F)|-d_v)=d_vE_v.              \tag{1.9}
\]

Apply (1.8) to every `G notni v`.  Its singleton term sums to

\[
 \ell(d_v-1)_{\ell-1}d_vE_v
 =\ell(d_v)_\ell E_v.
\]

Adding the `d_v(d_v)_ell` on-star contribution proves (1.6)--(1.7).
For `ell=1`, (1.8) is equality.  \(\square\)

### Corollary 1.2 (regular external-row criterion)

Suppose all targets of `V_sigma` have the same positive degree `d_sigma`,
and define

\[
 B_\sigma=\max\{a_G(v):v\in V_\sigma,\ G\not\ni v\}. \tag{1.10}
\]

Then, for `ell>=2` and `d_sigma>=ell`,

\[
 0\le {L_{\ell,\sigma}-G_{\ell,\sigma}
              \over L_{\ell,\sigma}}
 \le {\ell-1\over2}{B_\sigma\over d_\sigma-1}.       \tag{1.11}
\]

Indeed, `(a)_2<=B_sigma a`, (1.9) sums the remaining first moments, and

\[
 { {\ell\choose2}(d-2)_{\ell-2}B\,dE
       \over (d)_\ell(d+\ell E)}
 ={ {\ell\choose2}BE\over(d-1)(d+\ell E)}
 \le {\ell-1\over2}{B\over d-1}.                    \tag{1.12}
\]

## 2. The initial directed punctured hypergraph

Put `b=2r+1`, with `r>=3`.  For a cyclic word
`w=(w_0,...,w_(b-1))`, let `I_k^w(s)` be its cyclic interval of length
`k` beginning at `s`, and define

\[
 E(w)=\{(\mathcal M,I_r^w(s)):s\ne0\}
 \mathbin{\dot\cup}
 \{(\mathcal L,I_{r-1}^w(s)):s\ne0\}.                \tag{2.1}
\]

The alternating containment path between the retained `(r-1)`- and
`r`-windows reconstructs the missing window and then the directed cyclic
word, so `w mapsto E(w)` is injective.  Let `mathcal C_r` contain all
these `b!` edges.  Every edge has `2r` targets on each shore.  Prescribing
the retained start of a target gives

\[
 D_M=2r\,r!(r+1)!,\qquad
 D_L=2(r+2)r!(r+1)!={r+2\over r}D_M.                 \tag{2.2}
\]

We abbreviate `D=D_M`.

### Lemma 2.1 (the pair profile needed below)

Let `A,B` be distinct targets, of cardinalities `k,h in {r,r-1}`, and
put `a=|A cap B|`.  Their codegree is

\[
 d_{k,h}(a)=
 \bigl((b-2)m_{k,h}(a)+\mathbf1_{a=\min(k,h)}\bigr)
 a!(k-a)!(h-a)!(b-k-h+a)!,                           \tag{2.3}
\]

where

\[
 m_{k,h}(a)=
 \begin{cases}
 b-k-h+1,&a=0,\\
 2,&0<a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h).
 \end{cases}                                         \tag{2.4}
\]

In particular, the two high-codegree types are

\[
 \begin{aligned}
 d_{r,r}(0)&=(4r-2)(r!)^2\le {2D\over r},\\
 d_{r,r-1}(r-1)&=(4r-1)(r-1)!(r+1)!\le {2D\over r}.
 \end{aligned}                                       \tag{2.5}
\]

Every other distinct pair has codegree at most

\[
                         {6D\over r^2}.               \tag{2.6}
\]

#### Proof

Fixing the two positional cyclic arcs leaves four Venn cells, which can be
labelled in the factorial number appearing in (2.3).  With the first start
fixed, (2.4) is the number of relative starts giving intersection `a`.
There are `b m_(k,h)(a)` full-cycle start pairs.  Deleting the two fibres
whose first or second start is zero, and restoring `(0,0)` exactly in the
containment case, leaves the prefactor in (2.3).

Equations (2.5) follow by substitution and (2.2).  In the `MM`, `LL`, and
proper-`ML` rows, successive factorial ratios are respectively

\[
 { (a+1)(a+2)\over(r-a)^2},\quad
 { (a+1)(a+4)\over(r-1-a)^2},\quad
 { (a+1)(a+3)\over(r-a)(r-1-a)}.                     \tag{2.7}
\]

They increase with `a`, so after removing the two types in (2.5), each
row is maximized at an endpoint.  Direct substitution at those endpoints
gives (2.6); the largest normalized endpoint is the disjoint `ML` value

\[
 {d_{r,r-1}(0)\over D}={6r-3\over r^2(r+1)}<{6\over r^2}.
\]
This proves the lemma.  \(\square\)

### Lemma 2.2 (uniform external conflict-row cap)

For every initial configuration `G=E(w)` and every target `v notin G`,

\[
 \boxed{a_G(v)\le {32D\over r}.}                     \tag{2.8}
\]

#### Proof

Every configuration through `v` which meets `G` contains `v` together
with at least one target of `G`.  Hence the union bound

\[
 a_G(v)\le\sum_{u\in G}d(u,v).                       \tag{2.9}
\]

Among the cyclic windows of `G`, an arbitrary middle target is disjoint
from at most two middle windows: three distinct cyclic `r`-intervals have
union at least `r+2`, while its complement has size only `r+1`.
Three distinct cyclic `(r-1)`-intervals have union at least `r+1`, so an
`r`-set contains at most two of them.  Dually, the intersection of three
distinct cyclic `r`-intervals has size at most `r-2`, so an `(r-1)`-set is
contained in at most two of them.  Thus a middle `v` has at most four partners of
the two high types in (2.5), and a lower `v` has at most two.  Their total
contribution is at most `8D/r`.  The remaining at most `4r` targets each
contribute at most `6D/r^2` by (2.6).  This proves (2.8).
\(\square\)

## 3. Initial collision error

For a fixed initial edge `e`, write `t_F=|e cap F|` and

\[
                         S(e)=\sum_F{t_F\choose2}.     \tag{3.1}
\]

Substitution of (2.3) into the cyclic-window pair inventory gives

\[
 \begin{aligned}
 {S_{MM}\over D}&=4-{4\over r}+{9\over r^2}+O(r^{-3}),\\
 {S_{ML}\over D}&=8+{32\over r}-{111\over2r^2}+O(r^{-3}),\\
 {S_{LL}\over D}&={4\over r}+{96\over r^2}+O(r^{-3}).
 \end{aligned}                                       \tag{3.2}
\]

For completeness, these are finite factorial sums, not a probabilistic
estimate.  Put

\[
 n_{ML}(a)=
 \begin{cases}
 3(2r-1),&a=0,\\
 2(2r-1),&1\le a\le r-2,\\
 4r-1,&a=r-1,
 \end{cases}
 \qquad
 n_{LL}(a)=
 \begin{cases}
 4(2r-1),&a=0,\\
 2(2r-1),&1\le a\le r-2.
 \end{cases}                                         \tag{3.3}
\]

Direct substitution in (2.3), with division by two for equal-shore
unordered pairs, gives

\[
 {S_{MM}\over D}={ (2r-1)^2\over r}
 \sum_{a=0}^{r-1}{1\over {r\choose a}{r+1\choose a+1}},             \tag{3.4}
\]

\[
 {S_{ML}\over D}={1\over2r}\sum_{a=0}^{r-1}
 {n_{ML}(a)^2\over {r\choose a}{r+1\choose a+2}},                    \tag{3.5}
\]

\[
 {S_{LL}\over D}={r+2\over4r^2}\sum_{a=0}^{r-2}
 {n_{LL}(a)^2\over {r-1\choose a}{r+2\choose a+3}}.                 \tag{3.6}
\]

In (3.4), the endpoint expansion is
`4-4/r+9/r^2+O(r^-3)`.  In (3.5), the containment, disjoint, and
`a=r-2` terms are respectively

\[
 8-{4\over r}+{1\over2r^2},\qquad
 {36\over r}-{72\over r^2}+O(r^{-3}),\qquad
 {16\over r^2}+O(r^{-3}).                            \tag{3.7}
\]

In (3.6), the `a=r-2` and `a=0` terms are

\[
 {4\over r}+O(r^{-3}),\qquad {96\over r^2}+O(r^{-3}).               \tag{3.8}
\]

After these displayed endpoints, the common prefactor is `O(r)` and the
two binomial factors have product `Omega(r^5)`; the remaining `O(r)` terms
therefore total `O(r^-3)`.  The analogous middle remainder in (3.4) is
smaller.  This proves (3.2), and hence

\[
 \boxed{{S(e)\over D}=12+{32\over r}+{99\over2r^2}+O(r^{-3}).}       \tag{3.9}
\]

Let `C=|Gamma(e)|`, which is independent of `e`.  Since

\[
 \sum_{u\in e}d_u=2r(D_M+D_L)=4(r+1)D                         \tag{3.10}
\]

and

\[
 \sum_{u\in e}d_u-C
 =\sum_{F:t_F>0}(t_F-1)\le S(e),                              \tag{3.11}
\]

we have

\[
 C=4rD+O(D),\qquad E_v=C-d_v=(4r+O(1))D                       \tag{3.12}
\]

on either shore.  Notice the division of labour: (3.9) supplies (3.12),
whereas the localized pair bounds (2.5)--(2.6), not the scalar (3.9),
supply (2.8).

### Theorem 3.1 (initial relative collision defect)

For either shore `sigma` and every fixed `ell>=1`, once `r` is large
enough that `ell<=D_M` (in particular for `1<=ell<=6` and `r>=3`),

\[
 \boxed{
 G_{\ell,\sigma}
 =L_{\ell,\sigma}\bigl(1-O_\ell(r^{-1})\bigr),
 \qquad
 L_{\ell,\sigma}
 =\sum_{v\in V_\sigma}(d_v)_\ell[d_v+\ell E_v].}     \tag{3.13}
\]

The error is one-sided.  More explicitly, for `ell>=2`,

\[
 0\le {L_{\ell,\sigma}-G_{\ell,\sigma}\over L_{\ell,\sigma}}
 \le {\ell-1\over2}{32D/r\over d_\sigma-1}
 \le {32(\ell-1)\over r}.                            \tag{3.14}
\]

The last inequality uses `d_sigma>=D>=2`.  Equations (3.12)--(3.13) also
show that

\[
 L_{\ell,\sigma}
 =(4\ell r+O_\ell(1))|V_\sigma|(d_\sigma)_\ell D.     \tag{3.15}
\]

#### Proof

Apply Corollary 1.2 with Lemma 2.2.  Equation (3.15) follows from (3.12).
\(\square\)

## 4. What this does and does not reduce adaptively

For a current residual define

\[
 B_\sigma(H)=\max_{v\in V_\sigma,\,G\not\ni v}a_G(v).          \tag{4.1}
\]

Theorem 1.1 says exactly that the order-`ell` union exposure is its linear
first-exposure term, minus a nonnegative multiple-collision correction.
Consequently, on roots with `B_sigma(H)=o(d_v)`, all six orders needed by
the purge are uniformly determined to relative `o(1)` by the weighted
first-exposure statistics

\[
                 \sum_v(d_v)_\ell E_v,\qquad1\le\ell\le6.      \tag{4.2}
\]

This is a genuinely smaller sufficient interface than retaining every
rooted union profile: it involves one-edge conflict rows and first
exposures only.  It is not yet an unconditional reduction for the stopped
adaptive process.  The initial absolute estimate
`B_sigma(mathcal C_r)=O(D_M/r)` does not imply
`B_sigma(H_j)=o(bar d_(j,sigma))` after the average degree has fallen by
many orders of magnitude.  Nor does the maximum/average degree cap imply
such a row cap; a clique component can have `a_G(v)=d_v` for external
roots while remaining perfectly regular.

Thus the exact smaller adaptive gate is conditional:

1. control the stopped weighted first-exposure sums (4.2); and
2. prove a stopped external-row cap at the *current* degree scale on the
   roots which contribute to the bad-incidence moment.

Without item 2, (1.5) is an exact reparametrization rather than a closure
of Gate A.  No fixed-time pair-mass statement, by itself, proves its
adaptive persistence.
