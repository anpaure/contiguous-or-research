# Exact Gaussian quantifier for the factor-blind product-SCD tail

Date: 2026-07-26

## 0. Verdict

Let

\[
 W_m={2m\choose m}
\]

and let `L_m(m-H-1)` be the exact even-dimensional product-SCD exterior
word from
`MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`.
The construction covers the two exterior rank intervals for every
`0<=H<=m-1`, but its asymptotic length has the sharp quantifier

\[
 \boxed{
 {L_m(m-H-1)\over W_m}=o(1)
 \quad\Longleftrightarrow\quad
 {H\over\sqrt m}\longrightarrow\infty.}
 \tag{0.1}
\]

The forward implication was already proved uniformly by

\[
 {L_m(m-H-1)\over W_m}
 \le C_0\exp\!\left(-{H^2\over8m}\right).
 \tag{0.2}
\]

The converse below is for the exact constructed length, not merely for an
older binomial-tail envelope.  In particular:

* if `H=A sqrt(m)+o(sqrt(m))` for fixed finite `A`, the normalized cost
  tends to a strictly positive function `F(A)`;
* if `H=o(sqrt(m))`, the normalized cost tends to `2 sqrt(2)`;
* the trimmed odd lift has the same normalized limit.

Thus the product-SCD tail cannot be joined directly to a central compiler
known only through `H=o(sqrt(m))`.  The cutoffs do not overlap.  A new
annulus construction or the fixed-window little-oh theorem `(ST_A)` is
still necessary.

## 1. Exact fixed-Gaussian limit

Use the notation of the factor-blind tail theorem:

\[
 h=\lfloor m/2\rfloor,\qquad
 \epsilon=m-2h,\qquad
 x=h-a,\qquad
 d=H+1-\epsilon,
\]

and

\[
 B_{m,x}=A_m(h-x)w_m(h-x).
\]

The exact parity-uniform formula is

\[
 L_m(m-H-1)
 =2\sum_{x=0}^{h}B_{m,x}
 {m\choose h-(d-x)_+},
 \tag{1.1}
\]

with

\[
 \sum_{x=0}^{h}B_{m,x}=2^m-1.
 \tag{1.2}
\]

Define a probability distribution

\[
 p_m(x)={B_{m,x}\over2^m-1}.
 \tag{1.3}
\]

The local central-binomial estimate, uniformly on compact subsets of
`x/sqrt(m)`, gives the weak limit

\[
 {x\over\sqrt m}\Longrightarrow Y,
 \qquad
 f_Y(y)=8\sqrt{2\over\pi}\,y^2e^{-2y^2},\qquad y\ge0.
 \tag{1.4}
\]

Indeed, for `x=y sqrt(m)+o(sqrt(m))`,

\[
 B_{m,x}
 ={2^m\over\sqrt m}
 \left(8\sqrt{2\over\pi}\,y^2e^{-2y^2}+o(1)\right),
 \tag{1.5}
\]

and the density in (1.4) integrates to one.  Also, if
`z=u sqrt(m)+o(sqrt(m))`, then

\[
 {{m\choose h-z}\over {m\choose h}}
 \longrightarrow e^{-2u^2},
 \tag{1.6}
\]

while Wallis/Stirling gives

\[
 {2(2^m-1){m\choose h}\over {2m\choose m}}
 \longrightarrow2\sqrt2.
 \tag{1.7}
\]

Suppose `H/sqrt(m)->c` with `0<=c<infinity`.  Equations
(1.1)--(1.7), with standard Gaussian domination outside compact sets,
give

\[
 \boxed{
 {L_m(m-H-1)\over W_m}\longrightarrow F(c),}
 \tag{1.8}
\]

where

\[
 F(c)=2\sqrt2\int_0^\infty
 8\sqrt{2\over\pi}\,y^2e^{-2y^2}
 e^{-2(c-y)_+^2}\,dy.
 \tag{1.9}
\]

This is strictly positive for every finite `c`; for example,

\[
 F(c)\ge2\sqrt2\int_c^\infty
 8\sqrt{2\over\pi}\,y^2e^{-2y^2}\,dy>0.
 \tag{1.10}
\]

Moreover `F(0)=2 sqrt(2)`.  Hence every bounded subsequence of
`H/sqrt(m)` has a further subsequence on which the product-SCD exterior
cost is bounded below by a positive multiple of `W_m`.  Together with
(0.2), this proves (0.1).

For the odd lift the exterior length is `2L_m`, whereas

\[
 {2m+1\choose m}\sim2{2m\choose m}.
\]

Therefore its normalized limit is again `F(c)`.

## 2. What the current PBBS critical bound does prove

Let

\[
 B_m=\operatorname{Cat}_m={W\over2m+1}
\]

in the odd PBBS compiler, and let `nu_H(P_m)` be the full-deck residence
packing number.  The audited central ledger is

\[
 L_H^{\rm cen}
 \le W+2HB_m+2(5H-1)\nu_H(P_m).
 \tag{2.1}
\]

The height-gap theorem gives, at `H_0=ceil(sqrt(m))`,

\[
 \nu_{H_0}(P_m)=O(B_m\sqrt m).
 \tag{2.2}
\]

Since `nu_H` is monotone in `H`, for every `h_m=o(sqrt(m))`,

\[
 \nu_{h_m}(P_m)\le\nu_{H_0}(P_m)=O(B_m\sqrt m).
 \tag{2.3}
\]

Substitution into (2.1) yields

\[
 {L_{h_m}^{\rm cen}-W\over W}
 =O\!\left({h_m\over m}+{h_m\over\sqrt m}\right)=o(1).
 \tag{2.4}
\]

Thus the existing PBBS compiler does unconditionally give a
`W+o(W)` literal word for every central half-width

\[
 \boxed{h_m=o(\sqrt m).}
 \tag{2.5}
\]

This is a genuine central-band theorem, far beyond logarithmic width.
It does not prove the full constant-one theorem, because (0.1) puts the
factor-blind tail on the opposite side of the Gaussian scale.

## 3. Why fixed `A` does not create an overlap

There are two separate issues.

1. At cutoff `H=A sqrt(m)`, the product-SCD tail has length
   `(F(A)+o(1))W`, not `o(W)`.  Choosing a large fixed `A` makes this
   coefficient small but not asymptotically zero.
2. A central word through `h=o(sqrt(m))` and an exterior word beginning at
   `A sqrt(m)` leave the annulus

\[
 h<q\le A\sqrt m
 \tag{3.1}
\]

uncovered.  The two cutoffs cannot simply be chosen independently.

The standard fixed-window diagonal argument works only if, for every fixed
`A`, the central compiler itself reaches `H=A sqrt(m)` with excess
`o_A(W)`.  The current critical estimate gives only `O_A(W)` there.  The
missing improvement is exactly

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)
 =o_A(B_m\sqrt m),
 \tag{ST_A}
\]

or an independent construction of the intermediate annulus.

## 4. Decisive answer to the quantifier question

\[
\begin{array}{c|c|c}
\text{cutoff}&\text{product-SCD coverage}&\text{normalized length}\\ \hline
H=o(\sqrt m)&\text{yes}&2\sqrt2+o(1)\\
H=A\sqrt m,\ A<\infty&\text{yes}&F(A)+o(1)>0\\
H/\sqrt m\to\infty&\text{yes}&o(1)
\end{array}
\]

So the exact answer is: **coverage works at every cutoff, economical tail
completion works only beyond every fixed Gaussian window**.  There is no
hidden fixed-`A` or sub-Gaussian overlap in the existing product-SCD word.
