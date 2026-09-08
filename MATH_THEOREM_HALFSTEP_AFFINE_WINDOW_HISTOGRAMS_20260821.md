# Exact half-step affine window histograms and adjacent-transition counts

**Status (2026-08-21).** Every assertion below is proved.  The formulas
replace the `b`-phase enumeration in the affine retirement problem by a
short triangular kernel.  In particular, they give exact `O(q)` formulas
for every profile capacity in the natural upper-band range.  They also give
adjacent-layer transition masses without origin enumeration whenever both
neighboring histograms lie in their stated separation domains.
They do not by themselves prove the weighted positive-variation estimates.

## 1. Setup and the triangular overlap kernel

Let

\[
 b=2m+1,
 \qquad R(x)=mx\pmod b,
 \qquad P_r=\{x\in\mathbb Z_b:R(x)<r\}.             \tag{1.1}
\]

Primality of `b` is not needed here.  For a window of length `q`, define

\[
 z_{r,p}(q)=|P_r\cap\{p+1,\ldots,p+q\}|,
 \qquad
 n_{r,q}(z)=|\{p:z_{r,p}(q)=z\}|.                  \tag{1.2}
\]

For nonnegative integers `u,l,j`, put

\[
 h(u,l;j)=
 \begin{cases}
  2,&1\le j<\min(u,l),\\
  |u-l|+1,&j=\min(u,l)\ge1,\\
  0,&\text{otherwise}.
 \end{cases}                                      \tag{1.3}
\]

This is the exact number of translates of a length-`u` interval whose
intersection with a fixed length-`l` interval has size `j`, provided the
two intervals live in a larger arc and do not meet a second copy of the
fixed interval.  The hypotheses below guarantee precisely that separation.

## 2. The exact even-window histogram

### Theorem 2.1

Let `q=2u` and assume

\[
                         u\le\min(r,b-r).           \tag{2.1}
\]

Write

\[
 |2r-b|=2k+1,
 \qquad \epsilon=\operatorname {sgn}(2r-b).        \tag{2.2}
\]

Then, for every `j>=1`,

\[
 \boxed{
 n_{r,2u}(u+\epsilon j)
   =h(u,k;j)+h(u,k+1;j),}                          \tag{2.3}
\]

and all remaining phases have the central count:

\[
 n_{r,2u}(u)
 =b-\sum_{j\ge1}\{h(u,k;j)+h(u,k+1;j)\}.          \tag{2.4}
\]

All other multiplicities vanish.

#### Proof

Since `2m=-1 mod b`, consecutive physical pairs have affine ranks

\[
                 y,\qquad y+m+1.                  \tag{2.5}
\]

For `A_r={0,...,r-1}`, set

\[
 g_r(y)=1_{A_r}(y)+1_{A_r}(y+m+1).                 \tag{2.6}
\]

If `r<=m`, the two arcs in (2.6) are disjoint and `g_r=1` except on two
zero arcs of lengths `k` and `k+1`, where `g_r=0`.  If `r>=m+1`, their
union is the circle and `g_r=1` except on two overlap arcs of those same
lengths, where `g_r=2`.  A `2u`-window is the sum of `g_r` over a
length-`u` affine-rank interval.  Under (2.1), that interval cannot meet
both exceptional arcs.  Formula (1.3), applied to the two arc lengths,
therefore gives (2.3); subtraction from the `b` possible origins gives
(2.4).  \(\square\)

## 3. The exact odd-window histogram

### Theorem 3.1

For `q=1`,

\[
                   n_{r,1}(0)=b-r,
 \qquad            n_{r,1}(1)=r.                  \tag{3.1}
\]

Now let `q=2u+1>=3` and assume

\[
                         u\le\min(r,b-r).           \tag{3.2}
\]

Put

\[
 r_0=\min(r,b-r)=m-k.                              \tag{3.3}
\]

First suppose `r<=m`.  If `k=0`, the only nonzero multiplicities are

\[
 n_{m,2u+1}(u)=m+1+u,
 \qquad
 n_{m,2u+1}(u+1)=m-u.                              \tag{3.4}
\]

If `k>=1`, then

\[
 \boxed{
 \begin{aligned}
 n_{r,2u+1}(u-j)&=2h(u,k;j) &&(j\ge1),\\
 n_{r,2u+1}(u)&=r+3-u,\\
 n_{r,2u+1}(u+1)&=r-u.
 \end{aligned}}                                   \tag{3.5}
\]

All other multiplicities vanish.  For `r>=m+1`, complementation gives

\[
               n_{r,2u+1}(z)=n_{b-r,2u+1}(2u+1-z).\tag{3.6}
\]

#### Proof

For `r=m-k<=m`, inversion of the affine order gives the literal cyclic
word

\[
 P_r=\{0,2k+3,2k+5,\ldots,2m-1\}.                \tag{3.7}
\]

Thus all `r` ones are isolated.  One intervening zero run has length
`2k+2`; every other zero run has length one.  A length-`2u+1` interval
which loses `j>=1` ones at the long run can cross it from either end.  The
alternating sites on either side compress to a translated length-`u`
interval meeting a fixed length-`k` interval in exactly `j` sites; the two
boundary orientations stay disjoint because `u<=r`.  They therefore give
exactly `2h(u,k;j)` intervals.  The intervals with
`u+1` ones are the `r-u` alternating intervals which do not encounter the
long run.  For `k>=1`, subtracting these and the

\[
             2\sum_{j\ge1}h(u,k;j)=2(u+k-1)       \tag{3.8}
\]

long-run intervals from `b` gives `r+3-u` intervals with `u` ones.
When `k=0`, the two boundary neighborhoods coalesce; direct alternation
around the unique defect gives (3.4).  Finally, the half-step words at
payloads `r` and `b-r` are complements up to a cyclic reflection, proving
(3.6).  \(\square\)

## 4. Exact adjacent-transition counts

For `epsilon in {0,1}`, let

\[
 N_{r,q}(z,\epsilon)
 =|\{p:z_{r,p}(q)=z,
          1_{P_r}(p+q+1)=\epsilon\}|.              \tag{4.1}
\]

### Corollary 4.1

With `F_(r,q)(z)=sum_(t<=z)n_(r,q)(t)`, one has

\[
 \boxed{
 \begin{aligned}
 N_{r,q}(z,0)&=F_{r,q+1}(z)-F_{r,q}(z-1),\\
 N_{r,q}(z,1)&=n_{r,q}(z)-N_{r,q}(z,0).
 \end{aligned}}                                   \tag{4.2}
\]

#### Proof

A length-`q+1` window of weight `w` arises either from a length-`q`
window of weight `w` followed by zero, or from one of weight `w-1`
followed by one.  Hence

\[
 n_{r,q+1}(w)=N_{r,q}(w,0)+N_{r,q}(w-1,1).         \tag{4.3}
\]

Summing (4.3) over `w<=z` and using
`N(z,0)+N(z,1)=n_q(z)` proves (4.2).  \(\square\)

Thus the adjacent positive-variation ledger has the exact finite form

\[
 \mathcal A_{1,q+1}
 ={1\over b}\sum_r{b\choose r}^{\!2}
 \sum_{z,\epsilon}N_{r,q}(z,\epsilon)
 \left[
  \rho_{q+1,r+z+\epsilon}-\rho_{q,r+z}
 \right]_+.                                      \tag{4.4}
\]

Here `rho_(q,s)` is any prescribed profile table (in the retirement
application it is the quota-to-capacity thinning factor), the physical
payload sum is over `1<=r<=b-1`, and the left side defines the layer-`q+1`
contribution to `mathcal A_1`.  Formula (4.2) itself is unconditional.
When

\[
 \left\lceil{q\over2}\right\rceil\le\min(r,b-r),            \tag{4.5}
\]

Theorems 2.1 and 3.1 evaluate both histograms in (4.2) in `O(q)` time, so
there is no remaining enumeration over the `b` origins for that payload.

## 5. Exact short profile-capacity sums

Throughout this section assume only the natural upper-band domain

\[
                         1\le q\le b,qquad q\le s\le b.       \tag{5.0}
\]

Every payload which actually contributes to the upper-half formulas below
automatically satisfies the separation hypotheses of Theorems 2.1 and
3.1.  A lower-half half-step word has isolated ones, so a `2u` window has
at most `u` ones and a `2u+1` window has at most `u+1` ones.  The
complementary upper-half word has the reverse bounds.  Hence an
upper-profile contributor has `r=m+1+k` with `0<=k<=K`, apart from the
single `K=0` boundary case.  Since `s<=b` gives `K<=m-u`, one has
`u<=b-r`; the other separation inequality is immediate.

Define the physical profile capacity by

\[
 T_{q,s}={1\over b}\sum_{r=1}^{b-1}
          n_{r,q}(s-r){b\choose r}^{\!2}.          \tag{5.0a}
\]

Put

\[
 B_j={b\choose {m-j}}^{\!2}.                       \tag{5.1}
\]

For an upper-half profile at even offset, write

\[
 q=2u,
 \qquad s=m+u+1+K,
 \qquad K\ge0.                                    \tag{5.2}
\]

Let `M(u,l)=0` for `l=0` and `M(u,l)=u+l-1` for `l>=1`.  Then the
unnormalized capacity `bT_(q,s)` is exactly

\[
 \boxed{
 \begin{aligned}
 bT_{2u,s}
  ={}&[b-M(u,K)-M(u,K+1)]B_K\\
   &+\sum_{j=1}^K
    [h(u,K-j;j)+h(u,K-j+1;j)]B_{K-j}.
 \end{aligned}}                                   \tag{5.3}
\]

At `q=1`, Theorem 3.1 gives the separate exact identity

\[
 bT_{1,s}=(b-s){b\choose s}^{\!2}
          +(s-1){b\choose{s-1}}^{\!2}.            \tag{5.3a}
\]

At odd offset `q>=3`, write

\[
 q=2u+1,
 \qquad s=m+u+1+K.
\]

For `K=0`,

\[
                     bT_{2u+1,s}=2(m-u)B_0.        \tag{5.4}
\]

For `K>=1`, put

\[
 d_{u,K}=\begin{cases}
  m+1+u,&K=1,\\
  m-K+4-u,&K\ge2.
 \end{cases}                                      \tag{5.5}
\]

Then

\[
 \boxed{
 \begin{aligned}
 bT_{2u+1,s}
  ={}&(m-K-u)B_K+d_{u,K}B_{K-1}\\
    &+\sum_{j=1}^{K-1}2h(u,K-j-1;j)B_{K-j-1}.
 \end{aligned}}                                   \tag{5.6}
\]

The lower-half capacities follow from

\[
                         T_{q,s}=T_{q,b+q-s}.       \tag{5.7}
\]

Equations (5.3), (5.3a), and (5.6) are just Theorems 2.1 and 3.1 with
`r=s-z`; each contains at most `q+1` nonzero terms.  They are the exact
finite sums whose binomial variation must be controlled to prove
`A_1+A_2=o(W_b)` in the retirement problem.

## 6. H100 verification and scope

The checker
`scratch/audit_halfstep_window_histogram_formula_20260821.py` exhaustively
compares (2.3)--(3.6), including the endpoint `q=b`, with literal cyclic
windows for every odd `b<80` in their stated ranges.  It compares
(5.3)--(5.7) with direct profile sums throughout (5.0), and checks the
transition reconstruction (4.2).

This theorem is an exact enumerative reduction.  It does not assert the
analytic positive-variation bound, the local parity-return property, or
integral labelled/order-bank coinstantiation.
