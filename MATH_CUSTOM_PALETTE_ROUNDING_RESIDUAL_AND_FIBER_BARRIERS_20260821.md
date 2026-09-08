# Custom palette rounding: residual and trace-fiber barriers

**Date:** 2026-08-21  
**Status:** proved method barriers.  Nothing below disproves an integral
near-factor.  The results rule out a cardinality-only one-pass greedy
extension theorem and a postprocessing scheme that first fixes one ordered
central trace and then tries to round the other ranks inside its fiber.

## 1. Setup

Let

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 H=\lceil\sqrt{n\log n}\rceil,
\]

\[
 K=\{m-H,\ldots,m+1+H\},\qquad
 f=m+H+2,\qquad d=n-f+1=m-H.
\]

A free core of length `a` starts from an arbitrary permutation and makes at
each step one of the `d` legal tail-to-front moves.  At rank `k<f`, its
post-move observations are the top-`k` sets.  A core is **band-simple** when
its `a` observations are distinct at every rank in `K`.  There are at most

\[
 n!d^a                                                     \tag{1.1}
\]

seed-labelled free cores, and hence at most this many band-simple cores.

For a fixed slot, let `r_k` be the number of real rank-`k` resources that
the selected decorated edge must claim.  The other `a-r_k` observations may
be ignored or charged to distinct dummies.  Thus the argument below counts
actual real claims, not padded edge size.

## 2. An adversarial-residual killing lemma

For `0<=delta<=1` and integers `0<=r<=a<=M`, define

\[
 \mathsf H(M,a,\delta,r)
 =\Pr\{X\ge r\},                                      \tag{2.1}
\]

where `X` is hypergeometric with population size `M`, exactly
`floor(delta M)` marked elements, and sample size `a`.

### Theorem 2.1 (exact residual killing)

Put `M_k=binom(n,k)` and assume `a<=min_(k in K) M_k`.  If numbers
`delta_k in [0,1]` and integer real
quotas `r_k` satisfy

\[
 n!d^a\prod_{k\in K}
 \mathsf H(M_k,a,\delta_k,r_k)<1,                       \tag{2.2}
\]

then there are residual real-target families

\[
 U_k\subseteq { [n]\choose k},\qquad
 |U_k|=\lfloor\delta_kM_k\rfloor,                      \tag{2.3}
\]

such that **no** band-simple length-`a` core can claim `r_k` distinct
members of `U_k` simultaneously for every `k in K`.

#### Proof

Choose the `U_k` independently and uniformly among the subsets of the sizes
in (2.3).  Fix a band-simple core.  Its rank-`k` trace is an `a`-set, so its
number of observations in `U_k` has exactly the hypergeometric law in (2.1).
The choices of the residual families are independent between ranks.
Consequently the probability that this core meets every real quota is the
product in (2.2).  Union-bound over the at most `n!d^a` cores in (1.1).
The expected number of feasible cores is below one, and therefore some
choice of the residual families has none.  \(\square\)

This statement already permits the best decoration after the core is known:
the core survives precisely when it contains at least `r_k` residual real
targets at every rank.  Dummy labels add no further way to meet a real
quota.

For `p=r/a>delta'=floor(delta M)/M`, the standard sampling-without-
replacement Chernoff bound gives

\[
 \mathsf H(M,a,\delta,r)
 \le \exp\{-aD(p\|\delta')\},                          \tag{2.4}
\]

where

\[
 D(p\|q)=p\log{p\over q}+(1-p)\log{1-p\over1-q}.       \tag{2.5}
\]

It follows that a sufficient asymptotic condition for (2.2) is

\[
 \sum_{k:r_k/a>\delta_k'}D(r_k/a\|\delta_k')
 >\log d+{\log(n!)\over a},                            \tag{2.6}
\]

with enough strict margin to absorb harmless floors.

### Corollary 2.2 (the full band can block a balanced greedy very early)

Assume

\[
 n^3=o(a),\qquad a\le e^{n/5},\qquad
 N=sa\le W,\qquad N=(1-o(1/n))W.                       \tag{2.7}
\]

Use balanced outer quotas

\[
 {r_k\over a}={{n\choose k}\over N}+O(1/a),            \tag{2.8}
\]

and quota `a` at both middle ranks.  There is an absolute constant `C`
such that, for

\[
 x=Cn^{-1/3}(\log n)^{2/3},\qquad \delta_k=1-x,         \tag{2.9}
\]

one can choose residual families of density `1-x+o(1)` at every rank for
which a prescribed balanced-quota slot has no feasible core.

#### Proof

For `j>=1`, symmetry gives

\[
 p_j:={{n\choose m-j}\over W}
 =\prod_{h=0}^{j-1}{m-h\over m+2+h}.                  \tag{2.10}
\]

For `j=o(n)`, the elementary bounds `1-y<=-log y` and
`log(1+u)<=u` give

\[
 1-p_j\le-\log p_j
 \le\sum_{h=0}^{j-1}{2h+2\over m-h}
 \le {8j(j+1)\over n}                                 \tag{2.11}
\]

for all sufficiently large `n` in the range used below.  Therefore, for

\[
 1\le j\le J:=\left\lfloor{\sqrt{nx}\over16}\right\rfloor,
\]

the two symmetric rank quotas at distance `j` from the middle obey
`r_k/a>=1-x/4` for large `n`; the replacement of `W` by `N` only increases
the ratio, and the `O(1/a)` rounding error is negligible.

For `0<x<=1/4`, monotonicity of `D(p||1-x)` in `p>1-x` and
`log(1+u)>=u/(1+u)` give

\[
\begin{aligned}
 D(1-x/4\|1-x)
 &=(1-x/4)\log{1-x/4\over1-x}+{x\over4}\log{1\over4}\\
 &\ge {3x\over4}-{x\log4\over4}
 =c_0x,
\end{aligned}                                         \tag{2.12}
\]

where `c_0=(3-log 4)/4>0`.  The `2J` ranks just selected hence contribute

\[
 \sum_{k\in K}D(r_k/a\|1-x)
 \ge 2Jc_0x=\Omega(\sqrt n\,x^{3/2}).                 \tag{2.13}
\]

For these ranks,
`delta'_k=floor((1-x)M_k)/M_k<=1-x<r_k/a`.  At fixed
`p=r_k/a`, the quantity `D(p||q)` decreases as `q` increases through
`q<p`; hence
`D(r_k/a||delta'_k)>=D(r_k/a||1-x)`.  Thus (2.13) is also a lower bound
for the actual sum in (2.6).

With (2.9), the last expression is
`Omega(C^(3/2) log n)`.  Choose `C` large.  Since `d=Theta(n)` and
`log(n!)/a=o(1)` under (2.7), inequality (2.6) holds.  Theorem 2.1 finishes
the proof.  \(\square\)

The scope is important.  The residual families in Corollary 2.2 need not be
the residual of a partial palette matching.  Thus the corollary does not
rule out a global matching, a pseudorandom invariant tailored to reachable
residuals, or augmenting rearrangements of previously chosen cores.  It does
rule out a theorem asserting that residual cardinalities alone always allow
the next balanced block.  Its threshold is independent of whether `a` is
polynomial or exponential: after division by `a`, path entropy contributes
`log d`, quota large deviations contribute the sum in (2.6), and the seed
term `log(n!)/a` vanishes for every `a>>n^3`.

## 3. One ordered central trace has an asymptotically rigid fiber

Write `C_k(t)` for the top-`k` set after core move `t`.

### Theorem 3.1 (trace reconstruction)

Fix `k<f` and let a legal core have length `b>=k+1`.  Its ordered set trace

\[
 C_k(1),C_k(2),\ldots,C_k(b)                            \tag{3.1}
\]

determines:

1. every accessed letter at core times `2,...,b`;
2. the complete order of the top `k` letters at time `1`;
3. every rank-`ell` trace with `ell<=k`; and
4. `C_ell(t)` for `k<ell<f` whenever `t>=ell-k+1`.

Consequently, two legal cores with the same ordered rank-`k` trace can differ
inside a band `K=[k_-,k_+]` with `k_+<f` in at most

\[
 \sum_{\ell=k+1}^{k_+}(\ell-k)
 ={(k_+-k)(k_+-k+1)\over2}                             \tag{3.2}
\]

target observations.

#### Proof

Because the recurrence gap is at least `f>k`, the newly accessed letter at
time `t` is outside `C_k(t-1)`.  Moving it to the front deletes exactly the
old position-`k` letter.  Hence, for every `2<=t<=b`,

\[
 x_t\text{ is the unique member of }C_k(t)\setminus C_k(t-1),\qquad
 y_t\text{ is the unique member of }C_k(t-1)\setminus C_k(t). \tag{3.3}
\]

The deleted letters `y_2,y_3,...,y_(k+1)` are the time-1 top-`k` order read
from oldest to newest; explicitly, the newest-to-oldest order is
`(y_(k+1),y_k,...,y_2)`, and `y_(k+1)=x_1`.  This proves the first two
claims.  Lower prefixes are then known.  At a higher rank `k<ell<f`, after
`t-1>=ell-k` further moves its
top `ell` consists only of known accessed letters and a prefix of the known
time-1 top-`k` order; the unknown deeper seed tail has been shifted below
position `ell`.  This proves the remaining claims and (3.2).  \(\square\)

For the DCC band, take `k=m`.  Then (3.2) is `O(H^2)=O(n log n)` per core.
If `s=(1+o(1))W/a` cores are used and `a>>n^3`, the entire fiber left after
all ordered rank-`m` traces have been fixed contains only

\[
 O\left({W H^2\over a}\right)=o(W)                    \tag{3.4}
\]

potentially changeable band observations.  Thus a two-stage procedure that
first fixes the actual ordered paths (or their ordered trace at one middle
rank) has only `o(W)` core observations with which to repair a `Theta(W)`
coverage defect in the other rank parity.  If the fixed-endpoint bridges are
also allowed to vary, their observations add at most

\[
 O(|K|sR)=O\left({W|K|R\over a}\right).               \tag{3.4a}
\]

Thus the same full-word conclusion holds when `a>>|K|R`, in particular for
the canonical choice `a=floor(e^(n/5))`; under only `a>>n^3`, (3.4) is a
core-ledger statement.  A viable parity-first argument must retain
unordered/common-path lift freedom or use augmenting changes that revise the
first-stage traces themselves.

### Proposition 3.2 (a typical unordered trace also fixes the order)

Under the uniform-seed, uniform-generator band-simple core law with
`a<=e^(n/5)`, fix `k in {m,m+1}`.  With probability `1-o(1)`, the graph
on the `a` observed rank-`k` targets, joining Johnson-adjacent pairs, is
exactly the trace path.  Hence its unordered target set determines the
ordered trace up to reversal.

#### Proof

Consecutive observations are Johnson-adjacent.  A nonconsecutive chord at a
gap `2<=g<k` would match `g-1` of the `g` exiting occurrences to `g-1` of
the `g` entering occurrences.  If exit position `i` matches entry position
`j`, the recurrence floor gives `k+j-i>=f`.  Writing `i_0,j_0` for the
unmatched positions and summing gives

\[
 (g-1)(f-k)\le\sum_{\rm matched}(j-i)=i_0-j_0\le g-1.
\]

It would follow that `k=f-1`, impossible for `k=m,m+1<=f-2`.  At a gap
`g>=k`, the history-free endpoint bound is at most `d!/d^d` for each
specified target.  A fixed `k`-set has
`k(n-k)` Johnson neighbours.  A union bound over time pairs therefore gives

\[
 \Pr\{\text{a nonconsecutive Johnson chord}\}
 \le a^2k(n-k){d!\over d^d}=e^{-n/10+o(n)}.            \tag{3.5}
\]

Conditioning on band-simplicity changes this by a factor `1+o(1)`.  With no
chord, the induced graph is the displayed path, whose only two linear orders
are reversals.  \(\square\)

Proposition 3.2 concerns the canonical fractional law, not the entire
palette: an integral construction is allowed to concentrate on exceptional
chorded cores.  It therefore strengthens the diagnosis of naive randomized
two-stage rounding but is not an impossibility theorem.

## 4. What remains live

The same-rank normalized codegree `O(n^(-2))` is useful for controlling
fluctuations inside a rank, but it does not contradict Theorem 2.1: the
latter is an all-rank, all-candidate entropy bound and already lets the edge
choose its best real claims after seeing the residual sets.  Nor does making
`a` polynomial change its leading inequality.

An integral near-factor can still exist.  It must use at least one feature
excluded by the two barriers above: a globally coordinated construction, a
proved invariant restricting residuals far beyond their sizes, or
augmenting/common-path moves that revise already fixed central traces.  The
fractional palette theorem supplies none of these by itself.
