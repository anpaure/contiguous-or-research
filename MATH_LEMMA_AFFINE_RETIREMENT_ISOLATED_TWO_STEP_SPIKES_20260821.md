# The half-step affine retirement ratios have isolated two-step spikes on the Gaussian bulk

**Status (2026-08-21).**  The finite deterministic lemma below is proved.  It
closes the local-return hypothesis in Proposition 2.2 of
`MATH_LEMMA_RETIREMENT_PREFIX_ENVELOPE_POSITIVE_VARIATION_20260821.md` after
discarding a Gaussian tail of `o(W_b)` total retirement mass.  It does **not**
by itself estimate the remaining one-step ledger `A_1` or the sizes of the
two-step positive jumps.

## 1. Statement

Write

\[
 b=2h+1,\qquad m=h,\qquad
 P_r=\{x\in\mathbb Z_b:mx\bmod b<r\},                       \tag{1.1}
\]

and retain

\[
 J=\{\lfloor b/4\rfloor,\ldots,b-\lfloor b/4\rfloor\}.
\]

For a phase path `i=(r,p)` put

\[
 s_i(q)=r+|P_r\cap\{p+1,\ldots,p+q\}|,
 \quad
 a_i={1\over b}{b\choose r}^{\!2},                          \tag{1.2}
\]

\[
 T_{q,s}=\sum_{i:s_i(q)=s}a_i,
 \quad
 Q_{q,s}={b\choose s}{b\choose{s-q}},
 \quad
 \rho_{q,s}=\min\left(1,{Q_{q,s}\over T_{q,s}}\right),      \tag{1.3}
\]

with `rho=0` off the support, and let `u_i(q)=rho_(q,s_i(q))`.

### Theorem 1.1 (finite bulk local return)

Let `G,H` be positive integers satisfying

\[
                 G+H+4\le {h\over16}.                       \tag{1.4}
\]

If

\[
 |r-b/2|\le G+1,                                             \tag{1.5}
\]

then, whenever `q,q+2,q+4<=H`,

\[
 \boxed{
 u_i(q+2)>u_i(q)\quad\Longrightarrow\quad
 u_i(q+4)\le u_i(q).}                                       \tag{1.6}
\]

More precisely, after complement symmetry it is enough to take
`r=h+1+k`, `0<=k<=G`.  A strict two-step increase can then occur only when

* `q=2u+1>=3` is odd;
* the two newly appended bits are both `1`; and
* the upper profile parameter `K` defined below satisfies `2<=K<=2u`.

Thus every positive move is one isolated visit to the unique nonalternating
run of the half-step word.

### Corollary 1.2 (the tails cost `o(W_b)`)

Let

\[
 W_b={2b\choose b},\qquad
 \pi_b(r)={{b\choose r}^2\over W_b}.
\]

For every `G`,

\[
 \sum_{|r-b/2|>G}\pi_b(r)\le2e^{-2G^2/b}.                   \tag{1.7}
\]

Consequently discarding all tail paths at all `H` layers costs at most

\[
             2H e^{-2G^2/b}W_b.                             \tag{1.8}
\]

For example, if `H=O(sqrt(b log b))` and
`G=sqrt(b log b)`, then (1.4) holds eventually and (1.8) is `o(W_b)`.
For the surviving paths Proposition 2.2 of the prefix-envelope note is
therefore available with no factor `H` on the two-step variation:

\[
 \mathfrak D_{\rm ret}
 \le \mathfrak D_{\rm sep}+\mathcal A_{1,\rm bulk}
       +2\mathcal A_{2,\rm bulk}
       +2H e^{-2G^2/b}W_b.                                  \tag{1.9}
\]

Here the ratios in (1.3) are still the **full** profile ratios.  Tail paths
are set to zero only in the explicit retirement witness, so (1.9) does not
silently replace `T_(q,s)` by a truncated load.

## 2. Exact central profile formulae

Put

\[
 C_j={b\choose{h+1+j}},\qquad L_j=C_j^2,
 \qquad
 \lambda_j={C_{j+1}\over C_j}={h-j\over h+j+2}.             \tag{2.1}
\]

The ratios are strictly decreasing and satisfy

\[
 {\lambda_j\over\lambda_{j+1}}
 =1+{2(h+1)\over(h+j+2)(h-j-1)}
 \ge1+{2\over h}                                            \tag{2.2}
\]

for `-h-1<=j<=h-2`.  (The denominator in (2.2) is maximized at
`j=-1`, where equality holds.)  Also

\[
                  \lambda_{-j-2}=\lambda_j^{-1}.            \tag{2.3}
\]

For an upper profile write

\[
 s=h+1+u+K                                                     \tag{2.4}
\]

at both `q=2u` and `q=2u+1`, and set `F=bT_(q,s)`.  Condition
(1.4) keeps all the following source indices strictly inside `J`, so there
is no hidden truncation.

For odd `q=2u+1`, `u>=1`,

\[
 F_o(u,0)=2(h-u)L_0,
 \quad
 F_o(u,1)=(h-u-1)L_1+(h+u+1)L_0.                            \tag{2.5}
\]

For `K>=2`, put `A=h-u-K`.  If `K=2v<=2u`,

\[
 F_o(u,K)=A L_K+(A+4)L_{K-1}
              +4\sum_{j=v}^{K-2}L_j;                       \tag{2.6}
\]

if `K=2v+1<=2u`,

\[
 F_o(u,K)=A L_K+(A+4)L_{K-1}
 +4\sum_{j=v+1}^{K-2}L_j+2(u-v+1)L_v;                      \tag{2.7}
\]

and if `K>=2u+1`,

\[
 F_o(u,K)=A L_K+(A+4)L_{K-1}
 +4\sum_{j=K-u}^{K-2}L_j+2(K-2u)L_{K-u-1}.                 \tag{2.8}
\]

At `q=1`, the endpoint and the `d=1` term coincide, and the correct separate
formula is

\[
 F_o(0,0)=2hL_0,\qquad
 F_o(0,K)=(h-K)L_K+(h+K)L_{K-1}\quad(K>=1).                 \tag{2.9}
\]

For even `q=2u`,

\[
 F_e(u,0)=(2h+1-u)L_0.                                      \tag{2.10}
\]

For `K>=1`, put `A=h+1-u-K`.  If `K=2v<=2u`,

\[
 F_e(u,K)=2A L_K+4\sum_{j=v+1}^{K-1}L_j+(u-v+3)L_v;         \tag{2.11}
\]

if `K=2v+1<=2u`,

\[
 F_e(u,K)=2A L_K+4\sum_{j=v+1}^{K-1}L_j+(u-v)L_v;           \tag{2.12}
\]

and if `K>=2u+1`,

\[
 F_e(u,K)=2A L_K+4\sum_{j=K-u+1}^{K-1}L_j
                    +[2(K-2u)+3]L_{K-u}.                   \tag{2.13}
\]

To derive these displays, observe directly from (1.1) that for
`r=h+1+k` the physical bit word has `1` at `0`, at every odd position, and
at the final `k` even positions.  It is alternating except for the cyclic
`1`-run `[-2k,1]`.  Counting an even or odd window by its overlap with that
run gives (2.5)--(2.13).  This is also a literal proof that every omitted
coefficient is zero.

## 3. Coefficient maps for two-step moves

It is enough to compare the uncapped load ratio `F/(bQ)`: increasing that
ratio can only decrease `rho`.

Let `x=u+K`.  An odd or even two-step extension by `11` sends
`(u,K)` to `(u+1,K+1)` and has

\[
 {Q'\over Q}=\lambda_x\lambda_{x+1}.                        \tag{3.1}
\]

In every bulk profile `x<=G+H`, so all top coefficients called `A` below
satisfy

\[
                         A\ge {15h\over16}.                  \tag{3.2}
\]

For an even layer, map the old top source `K` to `K+1`, every interior
source `j` to `j+1`, and use the new endpoint plus the one unused interior
term for the old endpoint.  The only coefficient loss is at most
`(A-2)/A`.  By (2.2),

\[
 {\lambda_K^2\over\lambda_x\lambda_{x+1}}
 \ge(1+2/h)^{2u+1}\ge(1+2/h)^3,                             \tag{3.3}
\]

and (3.2) makes `(1-2/A)(1+2/h)^3>=1`.  Hence every even-layer
`11` move decreases `rho`.

For an odd layer with `K>=2u+1`, the same map works.  If
`c=2(K-2u)` and `j=K-u-1`, its only endpoint comparison is

\[
 cL_j\longmapsto(c-2)L_j+4L_{j+1}.                          \tag{3.4}
\]

Writing `R=Q'/Q`, the new side minus `R` times the old side is

\[
 (c-2)(1-R)L_j+(4\lambda_j^2-2R)L_j\ge0,                    \tag{3.5}
\]

because `R<=lambda_j^2<=1`.  The boundary `K=2u+1` uses
`2L_u -> 4L_(u+1)` and is easier.  Direct substitution of (2.5) and (2.9)
handles `K=0,1` and `q=1`.  Therefore a strict two-step increase is possible
only on an odd `11` move with

\[
                         2\le K\le2u.                        \tag{3.6}
\]

For completeness, a normal appended pair sends `(u,K)` to `(u+1,K)`.
Its quota ratios satisfy the exact identities

\[
 1-{Q'_o\over Q_o}
 ={4(u+1)(h+1)\over (h+u+2)^2-K^2},                         \tag{3.7}
\]

\[
 1-{Q'_e\over Q_e}
 ={2(h+1)(2u+1)\over
   (h+u+K+2)(h-K+u+1)}.                                     \tag{3.8}
\]

Under (1.4), each right side is larger than `1/A`.  In
(2.5)--(2.13) only the top coefficient(s) fall, by the relative factor at
most `1-1/A`; a moving endpoint is replaced by four copies at the old
source and the remaining copies one source closer to the centre.  Thus
`F'/F>=Q'/Q`, so normal pairs also decrease `rho`.  This proves the complete
classification (3.6).

## 4. Return after the exceptional move

Suppose first that the pair after the exceptional `11` pair is again
`11`.  The four-step move is

\[
                    (u,K)\longmapsto(u+2,K+2),               \tag{4.1}
\]

and

\[
 {Q''\over Q}=\prod_{t=0}^3\lambda_{u+K+t}.                 \tag{4.2}
\]

In (2.6)--(2.7), map the top source `K` to `K+2`, the second
source `K-1` to `K+1`, and every short-sum source `j` to `j+1`.
For odd `K`, map the endpoint `v` to `v+1`; its coefficient increases by
two.  The worst top loss is `(A-4)/A`, while

\[
 {\lambda_K^2\lambda_{K+1}^2
  \over\prod_{t=0}^3\lambda_{u+K+t}}
 \ge(1+2/h)^{4u+4}\ge(1+2/h)^8.                             \tag{4.3}
\]

Equations (3.2)--(4.3) give `F''/F>=Q''/Q`, and hence
`rho''<=rho`.

It remains to treat exit from the run.  Parametrize the current `11` start
as

\[
                    x=-2k+j,\qquad0\le j\le2k.               \tag{4.4}
\]

Literal counting in the preceding odd window gives

\[
 K=k+\min\left(u+1,\left\lceil{j\over2}\right\rceil\right).\tag{4.5}
\]

The next pair is normal exactly for `j=2k-1,2k`; in both cases

\[
                         K=k+\min(u+1,k).                    \tag{4.6}
\]

Together with (3.6), (4.6) forces `k<=u` and `K=2k`.  The
four-step move is now

\[
                    (u,K)\longmapsto(u+2,K+1).               \tag{4.7}
\]

Its quota ratio is

\[
 {Q''\over Q}
 ={\lambda_{K+u}\lambda_{K+u+1}\lambda_{K+u+2}
   \over\lambda_{K-u-2}}.                                   \tag{4.8}
\]

Map the top, second, and every short-sum source in (2.6) one place to the
right.  The new endpoint is unused positive mass.  Since every short source
`j>=K/2=k`, while `K-u-2<=k-2`, monotonicity of `lambda` gives

\[
                         \lambda_j^2\ge {Q''\over Q}.         \tag{4.9}
\]

For the top term, the total `lambda` spacing in (4.8) is `4u+5>=9`,
which pays the coefficient loss `(A-3)/A` by (2.2) and (3.2).
Thus once again `F''/F>=Q''/Q`.  Equations (4.1)--(4.9) prove
(1.6) for the upper word.  Replacing a word by its complemented cyclic
translate sends `r` to `b-r` and `s` to `b+q-s`, while preserving both
`T` and `Q`; this proves the lower half.

## 5. Tail proof, audit, and scope

The law `pi_b` is the hypergeometric law obtained by sampling `b` objects
without replacement from `b` marked and `b` unmarked objects.  Hoeffding's
sampling-without-replacement bound gives (1.7).  A rank-`r` source has total
phase capacity `binom(b,r)^2`; setting all its `H` retirement variables to
zero costs at most `H` times that capacity.  Summing proves (1.8) and (1.9).

The exact checker
`scratch/audit_affine_isolated_spike_coefficient_maps_20260821.py`:

1. compares (2.5)--(2.13) to literal cyclic-word enumeration;
2. checks the rational coefficient inequalities in (3.3), (4.3), and
   (4.8)--(4.9);
3. checks (1.6) with exact integer profile loads on more than 160,000 finite
   paths; and
4. checks the run-exit formula (4.5)--(4.6) literally.

The theorem is only about the scalar fractional phase/profile retirement
LP.  It does not provide integral token rounding or common labelled factor,
order, origin, or physical-atom coinstantiation.
