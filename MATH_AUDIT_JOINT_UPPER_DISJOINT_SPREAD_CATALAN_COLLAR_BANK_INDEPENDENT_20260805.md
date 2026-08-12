# Independent audit of the joint upper-disjoint spread Catalan collar bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited source:** `MATH_THEOREM_JOINT_UPPER_DISJOINT_SPREAD_CATALAN_COLLAR_BANK_20260805.md`  
**Verdict:** **GO after one exact correction.**  The construction, parity
counts, resource deletion estimates, exact-size thinning, and deadline-scale
union bound are valid.  The original sufficient condition (3.5) omitted the
factor `3/8` from its own Bernstein exponent.  It has been corrected to

\[
 {3pL\over8t}-\log|\mathcal A|\longrightarrow+\infty.
\]

The stronger hypothesis (4.4), which is the hypothesis actually used in the
main theorem and at the deadline scale, already implies this corrected
condition.  Thus the correction changes no conclusion of Theorem 4.1 or
Corollary 4.2.

## 1. Collar resources and parity counts

A balanced collar contains the owner vertices

\[
 E_O=\{P,M_0,\ldots,M_h,N\},\qquad |E_O|=h+3=s+2,
\]

and the distinct new upper vertices

\[
 E_U=\{U_1,\ldots,U_h,U_*\},\qquad |E_U|=h+1=s.
\]

The left seam repeats `U_1`, so it creates no additional upper resource.
The generalized construction with possibly different `q_-`, `q_+` and a
right label `z != lambda_h` preserves these counts and all internal
distinctness assertions.

For `k=2r`,

\[
 c={1\over r+1}{2r\choose r}=\operatorname{Cat}_r.
\]

For `k=2r-1`,

\[
 {1\over2r-1}{2r-1\choose r}
 ={1\over r}{2r-2\choose r-1}=\operatorname{Cat}_{r-1}.
\]

Thus in both parities `b=c-1` is an integer and is exactly the number of
bridges needed to join `c` components in a line.

## 2. Forbidden-bank deletion and residual edge constants

### 2.1 Even case

The owner and upper degrees in the containment graph are `r` and `r+1`,
and the initial edge count is `Wr`.  Deleting the prescribed owner bank
costs at most

\[
 |F|r\le {Wr\over64s}.
\]

One collar deletes at most

\[
 D_e=(s+2)r+s(r+1)=2r(s+1)+s
\]

incidences.  Before the `M`th collar, fewer than `W/(16s)` collars have
been deleted.  Hence the residual edge count is strictly greater than

\[
 W\left({7r\over8}-{9r\over64s}-{1\over16}\right).
\]

At the extremal permitted value `r=32s`, this bracket is at least
`28s-9/2-1/16`, which exceeds `2(s+3)` for every `s>=3`.  The inequality
only strengthens as `r` increases.

### 2.2 Odd case

Here the shore degrees are `r-1` and `r+1`, the initial edge count is
`W(r-1)`, and

\[
 D_o=(s+2)(r-1)+s(r+1)=2r(s+1)-2.
\]

Using the conservative forbidden-bank loss `|F|r` gives residual edge
count strictly greater than

\[
 W\left({7r\over8}-{9r\over64s}-1+{1\over8s}\right).
\]

At `r=32s`, the bracket is greater than `28s-11/2`, again exceeding
`2(s+3)` for `s>=3`.

In either parity the two residual shores have fewer than `2W` vertices.
If iterative deletion of vertices of degree at most `s+3` removed every
vertex, each original residual edge would be charged once, at the first
deleted endpoint, and the total edge count would be less than
`2W(s+3)`.  The preceding strict lower bound excludes this.  Therefore a
nonempty residual subgraph of minimum degree greater than `s+3` exists.

## 3. Use of the balanced-collar construction

The minimum-degree hypothesis is sufficient for every choice in the
generalized collar construction.

* At `M_{j-1}`, only the `j-1` deleted original labels lead back into
  `M_0`; another upper neighbour supplies a fresh `rho_j`.
* At `U_1`, the facet deleting `rho_1` is `M_0`; two further available
  facets supply distinct `q_-` and `lambda_1`.
* At step `j>=2`, the forbidden facet labels consist of the `j` rho labels
  and the protected `q_-`.  Since `j<=h` and the degree is greater than
  `s=h+1`, a remaining original label can be chosen as `lambda_j`.
* At `M_h`, at most the one choice `z=lambda_h` is forbidden.  At `U_*`,
  the `h` rho labels and `z` are the only labels outside `Q`; degree greater
  than `s` leaves a facet deleting some `q_+ in Q`.

All chosen owner and upper vertices lie in the residual graph.  Deleting
them therefore inductively gives pairwise owner/endpoint disjointness and
pairwise new-upper disjointness.  No unpriced resource is used in this
greedy step.

## 4. Exact bank size and the floor inequalities

With

\[
 M=\left\lfloor {W\over16s}\right\rfloor,
\]

the assumption `W/(16s)>=2` gives

\[
 {W\over32s}\le M\le {W\over16s}.
\]

Since `c>=2`, `b=c-1>=c/2`.  Therefore, for `p=b/M` and
`t=s+2<=2s`,

\[
 {p\over t}\ge
 \begin{cases}
 4/(r+1),&k=2r,\\
 4/(2r-1),&k=2r-1.
 \end{cases}
\]

Conversely, `b<c` and the lower bound on `M` give

\[
 p<
 \begin{cases}
 32s/(r+1),&k=2r,\\
 32s/(2r-1),&k=2r-1.
 \end{cases}
\]

The condition `r>=32s` also implies `b<=M` in both parities, so uniform
sampling of exactly `b` collars is well-defined.

## 5. Without-replacement concentration

For a test set `A`, put `w_i=|B_i intersection A|`.  Pairwise disjointness of the
blocks gives

\[
 0\le w_i\le t,\qquad \sum_iw_i\le |A|,
 \qquad \sum_iw_i^2\le t|A|.
\]

The sum from uniform sampling without replacement is smaller in convex
order than the sum of the same number of independent uniform draws with
replacement.  The direction used in the theorem is therefore correct.
In particular its positive exponential moments are no larger.

Both sums have mean

\[
 \mu={b\over M}\sum_iw_i\le p|A|.
\]

For the independent comparison sum the total variance is at most
`pt|A|`, and every centered summand is bounded above by `t`.  Applying the
exponential-moment proof of Bernstein with deviation `p|A|` gives

\[
 \Pr\{X_A>2p|A|\}
 \le \exp\left(-{p^2|A|^2\over
       2(pt|A|+tp|A|/3)}\right)
 =\exp\left(-{3p|A|\over8t}\right).
\]

This also explains the sole correction: a union bound requires

\[
 {3pL\over8t}-\log|\mathcal A|\to+\infty,
\]

not merely the same statement with the coefficient `3/8` omitted.

## 6. Stars, the union bound, and deadline asymptotics

For a lower set of size `ell`, its owner star has size

\[
 {k-\ell\choose r-\ell}={k-\ell\choose k-r}.
\]

This decreases as `ell` increases.  Over `ell<=r-h-1`, its minimum is

\[
 L_*={k-r+h+1\choose h+1}.
\]

At deadline scale `h=d(k)+1`, `s=h+1`, the established deadline
asymptotic gives

\[
 {s^2\over r}\to {\pi\over4}.
\]

Moreover,

\[
 \log L_*=\Theta(s\log(r/s))
             =\Theta(\sqrt r\log r),
 \qquad \log|\mathcal A|\le k\log2=O(r).
\]

Thus

\[
 {L_*/r\over1+\log|\mathcal A|}\to\infty.
\]

Together with the lower bounds on `p/t`, this implies the corrected
union-bound hypothesis with room to spare in both parities.  The upper
bounds on `p` then give exactly

\[
 |V_B\cap\mathcal O(S)|\le
 \begin{cases}
 64s|\mathcal O(S)|/(r+1),&k=2r,\\
 64s|\mathcal O(S)|/(2r-1),&k=2r-1.
 \end{cases}
\]

Since `s^2/r` tends to a positive constant, both coefficients are
`O(1/s)=O(r^(-1/2))`.

An independently prescribed `o(W/s)` owner bank satisfies
`|F|<=W/(64s)` eventually.  Because the chosen collar owners avoid `F`,
the remaining portion of a star is exactly bounded below by subtracting
the separate quantities `|F intersection O(S)|` and the collar-star load.

## 7. Scope audit

The theorem proves, prospectively and for all sufficiently large deadline-
scale middle dimensions, one exact parity-appropriate bank with all four
properties simultaneously:

1. exact `c-1` collar count;
2. pairwise disjoint bridge and endpoint owners;
3. pairwise disjoint new upper-`q1` targets; and
4. `O(1/s)` load in every low owner-containment star.

It does **not** prove natural suffix-deck disjointness, a punctured
ordered-four-transversal, a resident literal trace factor, arbitrary-width
upper coverage, an `O(1)` upper bound, or exact all-dimensional equality.
No such implication is used in the proof.

Subject to the corrected coefficient in (3.5), the audited theorem is
**GO**.
