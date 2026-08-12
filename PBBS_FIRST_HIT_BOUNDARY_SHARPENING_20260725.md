# RETRACTED: first-hit sharpening of the shared-boundary collision theorem

Date: 2026-07-25

## Retraction

The argument below is **invalid**. It assumes that the mandatory copied
word (0S_s0) is contained in one complemented dual block
(\overline T_h0). Proposition 4.2 of
`MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md` gives a genuine
first zero-winding PBBS return for which this copied word crosses the
(T_1/T_0) separator. Therefore the factorization (1.1), the claimed
first-passage factor (1/(h+3)), and Theorem 3.1 do not hold in general.

The earlier theorem in `PBBS_SHARED_BOUNDARY_COLLISION_20260725.md` is
unaffected: it uses the complete shared boundary word and record-minimum
parsing, not a one-block localization. Its verified frontier remains

\[
 \Lambda=o(r^{1/5}/\log r).
\]

The text below is retained only as an audit trail of the rejected
one-block idea and must not be cited as a theorem.

This note strengthens `PBBS_SHARED_BOUNDARY_COLLISION_20260725.md` by
using one piece of genuine PBBS geometry not present in the capped-array
relaxation: the overlap begins after two consecutive first hits in one
dual block.

Put

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil .
\]

## 1. The physical first-hit factor

For a positive-overlap zero-winding return, retain

\[
 O=(0S_s)E,
 \qquad |E|=2\ell,
\]

and let (h) be the dual block in which (O) begins.  Literal matching
inside that block gives the unique factorization

\[
 T_h=X1\overline{S_s}1Y,                           \tag{1.1}
\]

where the displayed up-steps are the first hits of heights (h+1) and
(h+2).  Complementing inside

\[
 \overline T_h0=\overline X,0S_s0\overline Y0
\]

shows

\[
 E=0\overline Y0
   (\overline T_{h-1}0)\cdots(\overline T_00).     \tag{1.2}
\]

Hence (h+1) is the record depth of (operatorname{rev}E).  Since
(E) is balanced, it is also the maximum prefix height of (E):

\[
 h+1=\max_{0\le j\le2\ell}\operatorname{net}(E[1,j]).
 \tag{1.3}
\]

Under the critical Boltzmann law, the unobserved prefix

\[
 X1\overline{S_s}1
\]

is a first-passage word from zero to (h+2).  Its exact total critical
weight is

\[
 A_{h+2}(1/2)=\frac1{h+3}.                         \tag{1.4}
\]

### Lemma 1.1 (physical dual-boundary probability)

There is an absolute (C) such that, if (3\ell<s-2), then every
balanced word (e) of length (2\ell) which can occur as the common
overlap boundary satisfies

\[
 \boxed{
 \Pr(\text{the dual boundary is }e
      \text{ and satisfies the two-first-hit rule})
 \le C\frac{4^{-\ell}}{h(e)+3}.}                  \tag{1.5}
\]

#### Proof

Equation (1.2) fixes (Y,T_0,\ldots,T_{h-1}).  Their total bit length is

\[
 |Y|+\sum_{i<h}|T_i|=2\ell-h-2.                  \tag{1.6}
\]

The shifted caps of (T_0,\ldots,T_h) are, respectively,

\[
 \ell+1,\ell+2,\ldots,\ell+h+1.                  \tag{1.7}
\]

Thus (1.4), the fixed-bit weights, and the block normalizations give

\[
 \begin{aligned}
 p_T(e)
 &\le 2^{-(2\ell-h-2)}\frac1{h+3}
      \prod_{i=0}^{h}\frac1{C_{\ell+i+1}(1/4)}\\
 &=2^{1-2\ell}\frac{\ell+h+3}{(\ell+2)(h+3)}
 \le C\frac{4^{-\ell}}{h+3}.
 \end{aligned}                                    \tag{1.8}
\]

Here

\[
 C_a(1/4)=\frac{2(a+1)}{a+2}
\]

makes the product telescope.  \(\square\)

## 2. The weighted bridge sum

### Lemma 2.1

For balanced binary words (e) of length (2\ell), put

\[
 M(e)=\max_j\operatorname{net}(e[1,j]).
\]

Then

\[
 \boxed{
 \sum_{e:\,\operatorname{net}(e)=0}\frac1{M(e)+2}
 \le C\frac{4^\ell}{\ell+1}.}                    \tag{2.1}
\]

#### Proof

Let (Z_\ell=\binom{2\ell}{\ell}\).  Reflection at the first hit of
height (a) gives

\[
 \#\{e:M(e)<a\}
 =Z_\ell-\binom{2\ell}{\ell+a}.                  \tag{2.2}
\]

For (1\le a\le\sqrt\ell), the product formula for the ratio of the
two binomial coefficients yields

\[
 \#\{e:M(e)<a\}
 \le C Z_\ell\frac{a^2}{\ell}.                   \tag{2.3}
\]

Split (M) into dyadic intervals below (sqrt\ell).  The contribution
of (2^j\le M+1<2^{j+1}) is, by (2.3), at most

\[
 C\frac1{2^j}Z_\ell\frac{2^{2j}}\ell.
\]

Summing to (2^j\le\sqrt\ell) gives

\[
 C\frac{Z_\ell}{\sqrt\ell}.
\]

The range (M+1\ge\sqrt\ell) has the same bound trivially.  Finally
(Z_\ell\le C4^\ell/\sqrt{\ell+1}), proving (2.1).  \(\square\)

### Corollary 2.2 (first-hit Hadamard collision)

Let the forward and dual capped arrays be independent under their
critical laws, but impose the genuine two-first-hit rule on the dual
array.  Then

\[
 \boxed{
 \Pr(\text{their length-}2\ell\text{ boundary words agree})
 \le C\frac{4^{-\ell}}{\ell+1}.}                 \tag{2.4}
\]

#### Proof

The forward pointwise boundary estimate from the shared-boundary theorem
is (C4^{-\ell}).  Multiply it by (1.5), sum over common (e), and use
(1.3) and (2.1).  \(\square\)

## 3. Improved coefficient and aggregate bounds

Conditioning on (E) and on the first-hit prefix does not touch the free
forward blocks

\[
 S_1,\ldots,S_{s-h'-1},
\]

where (h'\le\ell) is the forward record depth.  Their cap product is

\[
 \frac{Q_{\ell+h'+1}}{Q_UQ_V},
 \qquad |U-V|\le1,\quad U+V=s+\ell+1.
\]

Therefore the conditional largest coefficient remains (O(s^{-2})), by
the already audited (H_U) characteristic-function estimate.

Let (z_{r,s,2\ell}^{\rm phys}) count genuine roots.  Combining this
anti-concentration, Corollary 2.2, and the exact cap telescope gives

\[
 \boxed{
 z_{r,s,2\ell}^{\rm phys}
 \le C4^r\frac{(\ell+2)^2}{s^6(\ell+1)}.}         \tag{3.1}
\]

### Theorem 3.1

Fix (A>0).  Let (Z_r^{\rm phys}(A,L)) count genuine zero-winding
starts with

\[
 s\le A\sqrt r,
 \qquad0<\Lambda\le2L.
\]

If

\[
 \boxed{L^2(\log r)^{5/2}=o(\sqrt r),}            \tag{3.2}
\]

equivalently if, for example,

\[
 L=o\!\left(\frac{r^{1/4}}{(\log r)^{5/4}}\right),
\]

then

\[
 \boxed{Z_r^{\rm phys}(A,L)=o_A(B_r/\sqrt r).}    \tag{3.3}
\]

#### Proof

Below

\[
 s_0=\left\lfloor\sqrt{r/(K\log r)}\right\rfloor
\]

the path-spectrum bound is already (o(B_r/\sqrt r)).  Condition (3.2)
implies (L=o(s_0)), so (3.1) applies above (s_0).  Hence

\[
 \begin{aligned}
 \sum_{\ell\le L}\sum_{s\ge s_0}z_{r,s,2\ell}^{\rm phys}
 &\le C4^r
 \left(\sum_{\ell\le L}\frac{(\ell+2)^2}{\ell+1}\right)
 \left(\sum_{s\ge s_0}s^{-6}\right)\\
 &\le C4^r\frac{L^2(\log r)^{5/2}}{r^{5/2}}.
 \end{aligned}
\]

Since (B_r/\sqrt r\asymp4^r/r^2), (3.2) proves (3.3).  \(\square\)

This still does not settle the large-overlap zero-winding sector.  It
does, however, replace the former (r^{1/5}) overlap frontier by the
strictly larger (r^{1/4}) frontier using literal PBBS first-hit geometry.
