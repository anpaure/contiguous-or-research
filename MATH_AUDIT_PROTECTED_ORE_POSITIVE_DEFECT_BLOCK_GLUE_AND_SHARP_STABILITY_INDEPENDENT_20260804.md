# Independent audit: protected Ore positive-defect block gluing and sharp stability

**Date:** 2026-08-04  
**Verdict:** **INDEPENDENT GO.**  Every displayed identity, inequality,
example, and dependency used by
`MATH_THEOREM_PROTECTED_ORE_POSITIVE_DEFECT_BLOCK_GLUE_AND_SHARP_STABILITY_20260804.md`
has been reconstructed independently.  No correction to the theorem is
required.  Its scope is exactly the stated one: it proves sharp metric
scaling, an exact complete-block gluing formula, and the listed positive-
defect reservoir closures, but not arbitrary positive-defect Ore cuts.

No computation, search, or solver result is used in this audit.

## 1. Audited artifact and dependencies

The audited theorem has SHA-256

`b414ed2dea6a3cc7365a054cbea7e664069ae5c9d84e1bdff1c80d79e6ae0980`.

The two cited mathematical dependencies are present with the exact frozen
hashes stated by the theorem:

| role | artifact | independently checked SHA-256 |
|---|---|---|
| exact shadow identity and equality classification | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| constrained reservoir margins and Hamming Lipschitz bound | `MATH_THEOREM_COMMON_CORE_EQUALITY_CUTS_CONSTRAINED_SPREAD_COMPLETE_20260804.md` | `b07682e2aee1b5d3017e96fc1483b17a91be8d249673a2c4b49433610867eb5e` |

The self-audit was read only as an object to check, not as evidence.  Its
SHA-256 before this independent audit was
`770c47e355b2de8a0f4a144ef9cca6e9846ff7adf61283093c710a6fe393bfee`.

Throughout, `k=m-1`, the lower shore is
`L=binom([2m-1],k)`, and `W=|L|`.

## 2. Universal Hamming bound

Both `emptyset` and the full lower shore belong to the zero-defect class,
so

\[
 d_{\mathfrak E}(A)\le t:=\min\{|A|,W-|A|\}.
\]

The frozen weighted-shadow and Johnson spectral inequalities give

\[
 \sigma(A)\ge {2\over m(m-1)}|\partial_JA|
 \ge {2(2m-1)\over m(m-1)}{|A|(W-|A|)\over W}.
\]

Writing the product as `t(W-t)` and using `t<=W/2` gives

\[
 \sigma(A)\ge {2m-1\over m(m-1)}t,
\]

which is exactly Theorem 1.1.  No unstated stability input occurs here.

## 3. Principal-star sharpness

Let `A_c` be the family of lower vertices containing a fixed coordinate
and put `M=binom(2k,k-1)`.  Only owners containing that coordinate meet
the star, and each such owner has `k` selected facets.  Therefore

\[
 \sigma(A_c)=2\binom{2k}{k}-2\binom{2k}{k-1}={2M\over k}.
\]

For a zero-defect support block `S` containing the distinguished
coordinate, put `r=|S|-1`.  Its contribution to the distance gain is

\[
\begin{aligned}
 g(S)
 &=2\binom r{k-1}-\binom{r+1}k\\
 &={2k-r-1\over k}\binom r{k-1}.
\end{aligned}
\]

On the positive range, set `x=r-k+2`; then `1<=x<=k` and

\[
 g(S)={x(k+1-x)\over k(k-1)}\binom r{k-2}
 \le {(k+1)^2\over4k(k-1)}\binom r{k-2}.
\]

After deleting the common distinguished coordinate, distinct equality
supports intersect in at most `k-3` points.  Their `(k-2)`-shadows are
therefore disjoint inside a `2k`-element universe.  Hence

\[
 \sum_i g(S_i)
 \le {(k+1)^2\over4k(k-1)}\binom{2k}{k-2}
 ={(k+1)^2\over4k(k+2)}M.
\]

Blocks not containing the coordinate, and containing blocks with
nonpositive `g`, can only decrease this sum.  The distance lower bound in
Theorem 1.2 follows.  Division by `2M/k` gives asymptotic ratio
`(3/8+o(1))m`, proving that the universal `Theta(m sigma)` scale is sharp.

## 4. Two-block counterexample

For odd `m>=5`, let `H` have size `m-2=k-1` and split its complement into
two `p=(m+1)/2` element sets.  The two complete support layers intersect
in no lower vertex.  They are individually Johnson-connected, and the
edges

\[
 H+x\ \sim\ H+y
 \qquad(x\in P_0,\ y\in Q_0)
\]

join them.  The only owner fibres of size between two and `m-1` are

\[
 U=H\cup\{x,y\},
\]

each with exactly two selected facets.  Thus

\[
 b(A)=(m-2)p^2.
\]

For the distance claim, fix a support `Z` of size `z=k-1+p`.  If no
equality support contains `Z`, then for `Q_i=R_i cap Z` the
`(k-1)`-shadows are disjoint and `|Q_i|<=z-1`; consequently

\[
\begin{aligned}
 |E\cap\binom Zk|
 &=\sum_i\binom{|Q_i|}k\\
 &\le {z-k\over k}\sum_i\binom{|Q_i|}{k-1}\\
 &\le {z-k\over k}\binom z{k-1}
 ={p-1\over p}\binom zk.
\end{aligned}
\]

Therefore distance less than `B/p` forces an equality support containing
each of `S` and `T`.  Two distinct supports cannot do this because their
intersection would contain `H` of size `k-1`; one common support must
contain `S union T=[2m-1]`, and hence the equality family is the full
shore.  Finally

\[
 {W\over B}
 =\prod_{j=1}^{p}{|S|+j\over |S|+j-k}
 \ge\left({2m-1\over m}\right)^p
 >2+{1\over p}
\]

for odd `m>=5` (the smallest case already has `(9/5)^3>7/3`, and both the
base and exponent then increase).  Thus the full shore also has distance
strictly greater than `B/p`.  This verifies Theorem 2.1, including its
Johnson-connected and exponential-versus-polynomial scope.

## 5. Exact local gluing identity

Consider a cross owner meeting `q>=2` complete support blocks in one facet
each.  Write `d` for its protected degree and `t` for the number of its
protected selected facets.  The sum of the separate truncated-shadow
contributions is `q`; the union contribution is `2`.

For one separate block, the selected fibre has size one.  Its protected
loss is zero if `d<=1`; if `d=2`, it is one exactly when that block's
selected facet is not protected.  Hence the summed separate loss is
`0,0,q-t` for `d=0,1,2`.  In the union the selected fibre has size at
least two, so its protected loss is `d-t`.  Therefore the union margin
minus the sum of block margins is

| `d` | shadow change | loss change | margin change |
|---:|---:|---:|---:|
| 0 | `2-q` | `0` | `2-q` |
| 1 | `2-q` | `1-t` | `1-q+t` |
| 2 | `2-q` | `2-q` | `0` |

This is exactly `-psi_P(U)` in (3.4).  All other owners contribute
identically before and after gluing.  Summation proves (3.5) with equality,
not merely a bound.

When two supports meet in `k-1` points, their cross owners are exactly
`H+{x,y}`.  Each has `q=2`, so the only nonzero penalty occurs for
`d=1,t=0`.  There are `pq` possible cross owners and each contributes
`m-2` to `b`; this verifies (3.7)--(3.8).

## 6. Reservoir consequences

The cited constrained-reservoir theorem supplies exactly the one-support
margins (4.1)--(4.2) in their stated ranges and the Hamming estimates

\[
 |\Delta\lambda_P|\le mr,
 \qquad |\Delta\sigma|\le(m+2)r.
\]

Thus the exact two-block gluing identity gives baseline margin at least
`Delta(S)+Delta(T)-pq`, and a Hamming perturbation of radius `r` costs at
most `(2m+2)r`.  This proves (4.3)--(4.4).

For `|S|=|T|=m`, one has `p=q=2`, `u=m-1`, and
`binom(m,m-1)=m`, giving (4.5).  Since
`R_m=ceil(6m/log m)+2=o(m)`, the radius in (4.6) is positive and
`Theta(m)` for all sufficiently large `m`.  The supports in Theorem 2.1
also lie in the broad-margin range for large `m`; their margins are
exponential while `pq=O(m^2)`, so that example is correctly covered by
the gluing theorem.

For the singleton specialization, every singleton has
`sigma=m-2`.  The frozen envelope gives loss at most `R_m+4` outside the
exceptional family, hence margin at least

\[
 D_m=m-R_m-6.
\]

Exceptional singletons have nonnegative margin by the retained exact
common-`G_2` singleton theorem.  Applying the exact gluing identity to the
singleton partition gives (4.9)--(4.10).

If there are no full owners and every multi-facet owner has
`a_U<=r_0<m`, then locally

\[
 \psi_P(U)\le a_U-1
 \le {r_0-1\over m-r_0}(m-a_U).
\]

Summing proves (4.11).  For `r_0=2`, every such owner contributes exactly
`m-2` to `b`, which gives (4.12).  Finally

\[
 2n_2\le\sum_Ua_U=m|A|
\]

proves (4.13).  All asymptotic qualifications in these statements are
needed only to make the cited reservoir margins and `D_m` positive.

## 7. Scope audit

The theorem validly establishes all of the following and no more:

1. universal distance `O(m sigma)` to the zero-defect class, with matching
   order-`m` examples;
2. failure of any polynomial-in-`m` distance bound based only on `b`;
3. exact margin gluing for unions of complete support layers;
4. explicit positive-defect two-block families and their certified Hamming
   neighbourhoods; and
5. an arbitrary-cut low-multiplicity criterion obtained from singleton
   margins.

It does **not** classify or close arbitrary positive-defect cuts, and it
does not prove factor extension, endpoint compatibility, component
placement, or common-cap compatibility.  The stated residual
erosion/partial-component problem is therefore the correct remaining
scope boundary.

## 8. Final verdict

**INDEPENDENT GO.**  The theorem remains unchanged at SHA-256
`b414ed2dea6a3cc7365a054cbea7e664069ae5c9d84e1bdff1c80d79e6ae0980`.
No correction was required.
