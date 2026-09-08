# A factorial-moment hierarchy implies annealed FIFO regeneration

**Date:** 2026-08-21  
**Status:** conditional algebra only; the stated moment hierarchy is false
for this hypergraph and is not a live gate.  The boundary-polymer reduction
supersedes it.

## 1. Setup

Let `H_r` be the directed punctured-configuration hypergraph on the middle
and lower target layers from
`MATH_THEOREM_DIRECT_PUNCTURED_CONFIGURATION_PAIR_PROFILE_AND_CLUSTER_GATE_20260821.md`.
Every configuration has

\[
                         K=4r                                             \tag{1.1}
\]

targets.  Fix a configuration `e`.  For another indexed configuration `F`
put

\[
 t_F=|e\cap F|,
 \qquad N_t(e)=|\{F:t_F=t\}|,
 \qquad M_s(e)=\sum_F {t_F\choose s}.                    \tag{1.2}
\]

Thus `M_s` is the `s`th factorial overlap moment.  Let `D=D_M` be the
middle-target degree.  The lower degree differs from `D` by the factor
`(r+2)/r`, which is harmless in every estimate below.

For reference, the conditional calculation below assumed the following
uniform hierarchy.

> **Factorial-moment gate `FM(C)`.**  There is an absolute constant `C`
> such that, uniformly in `e` and `2<=s<=2r`,
> \[
>                    M_s(e)\le D C^s r^{2-s}.            \tag{1.3}
> \]

For fixed `s=2,3`, the exact calculations give precisely this scale:
`M_2/D=12+O(1/r)` and `M_3/D=44/r+O(1/r^2)`.  However, the explicit
boundary-four-cycle family in
`MATH_OBSTRUCTION_PUNCTURED_BOUNDARY_C4_BREAKS_RAW_FACTORIAL_MOMENT_HIERARCHY_20260821.md`
gives `M_4/D=Omega(1/r)`, contradicting (1.3) at `s=4`.  Thus Theorem 2.1
is a correct implication from a false hypothesis; it must not be used as
evidence for regeneration of the punctured-configuration process.

## 2. Independent two-layer residuals

Suppose, conditionally on keeping every target of `e`, that each other
lower target survives independently with probability `x` and each other
middle target independently with probability

\[
                         y={rx+2\over r+2}.                \tag{2.1}
\]

Write `t_F=t_{F,L}+t_{F,M}` according to the two target layers.  The
expected duplicate conflict excess at `e` is

\[
 {cal E}_{x}(e)
 =\sum_{F:t_F>0}(t_F-1)
        x^{,2r-t_{F,L}}y^{,2r-t_{F,M}}.                 \tag{2.2}
\]

The common residual degree scale is

\[
                         d_x=D x^{2r}y^{2r-1}.             \tag{2.3}
\]

### Theorem 2.1 (moment hierarchy implies annealed regeneration)

Assume `FM(C)`.  For every fixed `alpha<1/2`, uniformly for

\[
                         r^{-\alpha}\le x\le1,             \tag{2.4}
\]

one has

\[
                  \boxed{\quad {\mathcal E_x(e)\over r d_x}=o(1).\quad}  \tag{2.5}
\]

The same conclusion holds for any `x=x(r)` with `rx->infinity` and

\[
 C^{2r}r^{3-2r}x^{-(4r-1)}=o(1).                        \tag{2.6}
\]

#### Proof

Because `y>=x`, (2.2) is at most

\[
 x^{2r}y^{2r}\sum_F(t_F-1)x^{-t_F}.                       \tag{2.7}
\]

Put `a=x^{-1}-1`.  For every integer `t>=2`,

\[
 (t-1)x^{-t}
 \le x^{-2}{t\choose2}(1+a)^{t-2}.                       \tag{2.8}
\]

The elementary binomial identity

\[
 {t\choose2}(1+a)^{t-2}
 =\sum_{j=0}^{t-2}{j+2\choose2}{t\choose j+2}a^j          \tag{2.9}
\]

therefore gives

\[
 {\mathcal E_x(e)\over r d_x}
 \le {y\over rD x^2}
       \sum_{j=0}^{4r-2}{j+2\choose2}a^jM_{j+2}(e).       \tag{2.10}
\]

First take `0<=j<=2r-2`.  By (1.3),

\[
 {M_{j+2}(e)\over D}\le C^{j+2}r^{-j}.                   \tag{2.11}
\]

Since `a<=x^{-1}` and `rx->infinity`, the corresponding part of the sum
in (2.10) is `O_C(D)`.  Also `y/x=1+O(1/(rx))`, so its normalized
contribution is

\[
                         O_C\!\left({1\over rx}\right)=o(1).             \tag{2.12}
\]

It remains to control the factorial orders above `2r`.  For
`2r<k<=4r`, the exact identity

\[
 {t\choose k}{k\choose2r}
 ={t\choose2r}{t-2r\choose k-2r}                         \tag{2.13}
\]

implies

\[
 M_k(e)
 \le M_{2r}(e){{2r}\choose{k-2r}}.                       \tag{2.14}
\]

Using `(j+2 choose 2)<=8r^2`, (2.14), and the binomial theorem, the upper
half of the sum in (2.10) is at most

\[
 8r^2M_{2r}(e)a^{2r-2}(1+a)^{2r}
 \le8r^2M_{2r}(e)x^{-(4r-2)}.                             \tag{2.15}
\]

Now (1.3) at `s=2r` and `y/x=1+o(1)` bound the normalized contribution by

\[
 O\!\left(C^{2r}r^{3-2r}x^{-(4r-1)}\right).              \tag{2.16}
\]

This is `o(1)` under (2.6).  If `x>=r^{-alpha}` with fixed
`alpha<1/2`, the logarithm of (2.16) is

\[
             -(2-4\alpha+o(1))r\log r,
\]

so (2.16) tends to zero uniformly.  Combining (2.12) and (2.16) proves
(2.5).  \(\square\)

## 3. Why only moments through `2r` are needed

The upper-half estimate (2.14) is the useful point of the reduction.
One does **not** need a separate uniform formula for every overlap order
through `4r`, nor does one need to treat each near clone separately in the
regeneration calculation.  Once the single midpoint moment `M_(2r)` has
the scale in (1.3), all larger factorial moments are dominated by it at a
binomial cost which is absorbed by (2.15).

The near-clone classification remains useful for proving (1.3), especially
near `s=2r`, but it is not an additional hypothesis of Theorem 2.1.

## 4. Superseded scope

Theorem 2.1 is retained only because its factorial expansion and midpoint
domination remain useful bookkeeping.  Its hypothesis `FM(C)` is disproved,
so the two-step programme formerly stated here is retired.  The live
replacement is
`MATH_REDUCTION_PUNCTURED_BOUNDARY_POLYMER_TO_ANNEALED_REGENERATION_20260821.md`,
which resums connected boundary cycles before attempting the quenched
trajectory upgrade.
