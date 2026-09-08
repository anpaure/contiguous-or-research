# A three-palette-disjoint Catalan collar bank from a dense coloured Johnson core

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, finite search, or solver  
**Status:** unconditional prospective bank theorem for all sufficiently
large middle dimensions.  It strengthens the earlier joint collar-bank
theorem by making the lower immediate colours disjoint as well as the owner
and upper immediate colours.  It still does not extend the protected bank
to a complete ordered four-transversal, a resident literal trace factor, or
an all-width upper carrier.

## 0. Statement and notation

Let

\[
 k\in\{2r,2r-1\},\qquad q=k-r\in\{r,r-1\},
 \qquad W={k\choose r},                              \tag{0.1}
\]

and let `h>=2`, `s=h+1`.  A generalized balanced pivot collar has

* `s+2` distinct rank-`r` owner resources;
* `s+1` distinct rank-`(r-1)` lower-`q1` resources; and
* `s` distinct rank-`(r+1)` upper-`q1` resources.

There are `s+1` transitions: the left seam deliberately repeats the first
internal upper colour, while every lower colour is new.  These are the
literal collars of
`MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`,
including the generalized right endpoint.

Put

\[
 c=\begin{cases}
       W/(r+1),&k=2r,\\
       W/(2r-1),&k=2r-1,
    \end{cases}
 \qquad b=c-1.                                      \tag{0.2}
\]

The main result is the following.

### Theorem 0.1 (three-palette Catalan bank)

At deadline scale `h=d(k)+1`, for every sufficiently large `k` there are
exactly `b` generalized balanced collars such that

1. all owner resources of different collars are distinct;
2. all lower-`q1` resources of different collars are distinct;
3. all distinct upper-`q1` resources of different collars are distinct;
4. for every `S subseteq [k]` with `|S|<=r-h-1`, the union `V_B` of the
   protected owner resources satisfies

   \[
    |V_B\cap\mathcal O(S)|
       \le {256s\over D_k}|\mathcal O(S)|,
    \qquad
    \mathcal O(S)=\{T\in\tbinom{[k]}r:S\subseteq T\},                 \tag{0.3}
   \]

   where `D_k=r+1` for `k=2r` and `D_k=2r-1` for
   `k=2r-1`.
5. uniformly for every lower colour `L in binom([k],r-1)` and every owner
   `T in binom([k],r)`,

   \[
   |V_B\cap\{R:L\subset R\}|=O(r/\log r),           \tag{0.4}
   \]

   and the number of selected collar lower colours contained in `T` is
   `O(r/log r)`.

In particular the protected bank occupies only `O(r^(-1/2))` of every
such low containment star.

The proof has two stages.  First a deterministic greedy argument builds
`Theta(W/s)` collars disjoint in all three palettes.  Then exact-size
hypergeometric thinning retains `b=Theta(W/r)` collars and installs the
simultaneous low-star spread.

## 1. The coloured Johnson graph

Let `J=J(k,r)` be the Johnson graph on `binom([k],r)`.  For an edge `AB`
write

\[
             \ell(AB)=A\cap B\in{[k]\choose r-1},
 \qquad
             u(AB)=A\cup B\in{[k]\choose r+1}.       \tag{1.1}
\]

Every owner has degree

\[
                         \Delta=rq,                  \tag{1.2}
\]

and hence

\[
                         |E(J)|={W\Delta\over2}.      \tag{1.3}
\]

A fixed lower colour lies under `q+1` owners.  Its colour class is the
clique on those owners and therefore contains

\[
                         {q+1\choose2}                \tag{1.4}
\]

Johnson edges.  A fixed upper colour contains `r+1` owner facets and its
colour class contains

\[
                         {r+1\choose2}                \tag{1.5}
\]

edges.

### Lemma 1.1 (a dense residual coloured core)

Suppose fewer than

\[
                         M=\left\lfloor{W\over64s}\right\rfloor       \tag{1.6}
\]

balanced collars have already been selected, with all three resource
families pairwise disjoint.  Delete their owner vertices and delete every
remaining Johnson edge whose lower or upper colour has already been used.
If `r>=16s` and `W/(64s)>=2`, the residual graph has a nonempty subgraph of
minimum degree at least `Delta/4`.

#### Proof

After `t<M` collars, the numbers of deleted resources are at most

\[
 t(s+2),\qquad t(s+1),\qquad ts                         \tag{1.7}
\]

in the owner, lower, and upper shores.  Equations (1.2), (1.4), and (1.5)
give the union-bound estimate

\[
 \begin{aligned}
 |E_{\rm res}|
 \ge {W\Delta\over2}
 &-t(s+2)\Delta\\
 &-t(s+1){q+1\choose2}
 -ts{r+1\choose2}.                                  \tag{1.8}
 \end{aligned}
\]

Divide the three losses by `W Delta/2`.  Using `t<W/(64s)` gives,
respectively,

\[
 {s+2\over32s},\qquad
 {s+1\over64s}{q+1\over r},\qquad
 {1\over64}{r+1\over q}.                            \tag{1.9}
\]

Here `q in {r,r-1}`, `s>=3`, and `r>=16s`.  Their sum is less than
`1/2` (in fact it is less than `1/10` in the stated range).  Hence

\[
                         |E_{\rm res}|>{W\Delta\over4}.               \tag{1.10}
\]

Repeatedly remove residual vertices of degree less than `Delta/4`.  If
every vertex disappeared, charging an edge when its first endpoint is
removed would give fewer than `W Delta/4` residual edges, contradicting
(1.10).  The surviving core has the asserted minimum degree. `square`

## 2. A collar inside every dense coloured core

### Lemma 2.1 (dense-core collar lemma)

Let `H` be a subgraph of `J(k,r)` of minimum degree at least `Delta/4`,
where `q in {r,r-1}`, `h>=2`, and `r>=16(h+1)`.  Then `H` contains all
owner edges of one generalized balanced collar.  Its owner resources are
distinct, its lower colours are distinct, and its upper colours are
distinct apart from the prescribed repetition of the first internal upper
colour at the left seam.

#### Proof

Choose any `M_0 in V(H)`.  Partition its incident edges according to the
entering label `rho notin M_0`.  There are `q` classes, so one label
`rho_1` has at least

\[
                 {\deg_H(M_0)\over q}\ge {r\over4}                    \tag{2.1}
\]

possible deleted labels.  Let `S subseteq M_0` be that set of deleted
labels.  Choose `lambda_1 in S` and put

\[
                 M_1=M_0-\{\lambda_1\}+\{\rho_1\}.                   \tag{2.2}
\]

Inductively suppose that `M_(j-1)` has been reached, for `2<=j<=h`, by
distinct exchanges

\[
 \lambda_i\longmapsto\rho_i\qquad(1\le i<j),         \tag{2.3}
\]

where all `lambda_i` belonged to `M_0` and all `rho_i` lay outside
`M_0`.  At `M_(j-1)`, forbid an edge if it removes one of the `j-1`
inserted rho labels or inserts one of the `j-1` deleted lambda labels.
For each fixed removed label there are at most `q` incident edges, and for
each fixed entering label at most `r`.  Thus fewer than

\[
                         (j-1)(r+q)                  \tag{2.4}
\]

edges are forbidden.  Since

\[
 {rq\over4}>h(r+q)                                  \tag{2.5}
\]

under the stated hypotheses, an allowed edge remains.  It supplies new
labels `lambda_j,rho_j`.  Continuing gives the Johnson geodesic

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_j\},
 \quad
 Q=M_0\setminus\{\lambda_1,\ldots,\lambda_h\}.       \tag{2.6}
\]

The first entering-label class `S` has size at least `r/4`.  Since only
`h` lambda labels were deleted and `r/4>h`, choose

\[
                         q_-\in S\cap Q.              \tag{2.7}
\]

Then

\[
                         P=M_0-\{q_-\}+\{\rho_1\}     \tag{2.8}
\]

is a vertex of `H`, and `PM_0` is an edge of `H`.  Its upper colour is
the first internal upper colour `M_0 union {rho_1}` and is the unique
declared repetition.

At `M_h`, forbid every edge which removes one of the `h` rho labels or
inserts one of the `h` lambda labels.  Again at most `h(r+q)` edges are
forbidden, so (2.5) leaves an edge

\[
                         M_hN,qquad
 N=M_h-\{q_+\}+\{z\},                                \tag{2.9}
\]

with `q_+ in Q` and a new label `z notin M_0 union
{rho_1,...,rho_h}`.  This is the generalized trace-compatible right
endpoint.

The standard collar identities now finish the resource audit.  Every
internal lower colour contains `Q`; the left and right seam lower colours
omit `q_-` and `q_+`, respectively, and the two seam values contain the
opposite complete rails, so all `s+1` lower values are distinct.  The
rho-prefix length distinguishes the `h` internal upper values, the left
seam repeats only the first one, and the right upper value contains `z`,
so the `s` distinct upper resources are different.  The owner values are
distinct by (2.6)--(2.9).  Every edge used belongs to `H`, so every one of
these colours was allowed. `square`

### Remark 2.2 (why Johnson density, rather than owner density, is enough)

At one owner, a fixed lower colour accounts for at most `q` incident
edges and a fixed upper colour for at most `r`.  The local exclusions in
the collar construction price only `O(h)` such colour or coordinate
classes.  Their total cost is `O(hr)=o(rq)`, while the dense core retains
`Omega(rq)` degree.  This is the exact aperture behind Lemma 2.1.

## 3. A large three-palette-disjoint bank

### Theorem 3.1

Under the hypotheses of Lemma 1.1 there are `M` generalized balanced
collars whose owner sets are pairwise disjoint, whose lower resource sets
are pairwise disjoint, and whose distinct upper resource sets are pairwise
disjoint.

#### Proof

Start with the full coloured Johnson graph.  Before the `t`th choice,
apply Lemma 1.1 to the resources of the previously chosen collars.  Apply
Lemma 2.1 inside the resulting dense core.  Delete the new collar's owner
vertices and every edge carrying one of its lower or distinct upper
colours.  The induction continues through `t=M`. `square`

## 4. Exact Catalan thinning and star spread

For a lower set `S` of rank at most `r-h-1`, let `O(S)` be its owner star.
The smallest test has size

\[
                         L_*={k-r+h+1\choose h+1}.    \tag{4.1}
\]

Choose exactly `b` of the `M` collars uniformly.  This is possible for all
sufficiently large deadline-scale dimensions because

\[
                         {M\over b}=\Theta(r/s)\to\infty.              \tag{4.2}
\]

Put `p=b/M` and let one block be the `s+2` owner resources of a collar.
The blocks are disjoint.  The weighted exact-size thinning lemma gives,
for every fixed star,

\[
 \Pr\{ |V_B\cap O(S)|>2p|O(S)|\}
 \le \exp\left(-{3p|O(S)|\over8(s+2)}\right).        \tag{4.3}
\]

When `c>=2`, `b>=c/2`; and when `W/(64s)>=2`,

\[
 {W\over128s}\le M\le {W\over64s}.                 \tag{4.4}
\]

Consequently

\[
 {p\over s+2}\ge {16\over D_k},
 \qquad
 p<{128s\over D_k}.                                 \tag{4.5}
\]

At deadline scale `s=Theta(sqrt(r))`,

\[
 \log L_*=\Theta(\sqrt r\log r),
 \qquad
 \log|\{S:|S|\le r-h-1\}|=O(r).                   \tag{4.6}
\]

Thus the exponent in (4.3), evaluated at the smallest star, dominates the
logarithm of the number of tests.  A union bound gives one exact `b`-collar
subfamily satisfying

\[
 |V_B\cap O(S)|\le2p|O(S)|
       <{256s\over D_k}|O(S)|                       \tag{4.7}
\]

simultaneously for every test.  All three disjointness properties are
inherited from the large bank.

It remains to prove the two small-star assertions in Item 5.  We first use
the geometry of one collar.

### Lemma 4.1 (two-per-small-star geometry)

For one generalized collar:

1. any fixed rank-`(r-1)` set is contained in at most two of its owner
   resources; and
2. any fixed rank-`r` set contains at most two of its lower-`q1`
   resources.

#### Proof

For central owners `M_i,M_j`,

\[
                         |M_i\cap M_j|=r-|i-j|.       \tag{4.8}
\]

Thus a rank-`(r-1)` set cannot lie in two nonconsecutive central owners.
The left endpoint `P` has rank-`(r-1)` intersection only with `M_0` and
possibly `M_1`; their triple intersection has rank at most `r-2`.  The
right endpoint is analogous, and the two endpoint collars have no common
rank-`(r-1)` subset when `h>=2`.  This proves Item 1.

The internal lower colours are

\[
 I_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
          \cup\{\rho_1,\ldots,\rho_{j-1}\}.          \tag{4.9}
\]

For `i<j`,

\[
                         |I_i\cup I_j|=r+j-i-1.       \tag{4.10}
\]

So a rank-`r` owner can contain at most two consecutive internal lower
colours.  The left seam lower colour can coexist inside a rank-`r` set only
with the first internal lower colour, and the right seam value only with
the last one; the two seam values cannot coexist.  This proves Item 2.
`square`

### Lemma 4.2 (simultaneous sublinear small-star load)

The exact `b`-collar thinning may be chosen so that both quantities in
(0.4) are `O(r/log r)` uniformly over all lower colours and owners.

#### Proof

Fix a lower colour `L`.  Because the `M` owner blocks are disjoint, at most
`q+1` blocks contain an owner above `L`.  If `Z_L` is the number of those
blocks selected in the exact `b`-sample, Lemma 4.1 bounds the protected
owner load above `L` by `2Z_L`.  Sampling without replacement is dominated
in positive exponential moments by independent sampling, so

\[
 \Pr\{Z_L\ge t\}
 \le\left({e\mu\over t}\right)^t,
 \qquad
 \mu\le p(q+1)=O(s).                                \tag{4.11}
\]

The same argument applies to a fixed owner `T`: lower-resource blocks are
pairwise disjoint, at most `r` of them meet the facet set of `T`, and each
selected block contributes at most two facets by Lemma 4.1.

Take `t=K r/log r`, where `K` is a sufficiently large absolute constant.
Since `s=Theta(sqrt r)`,

\[
 t\log{t\over e\mu}=\left({K\over2}+o(1)\right)r.    \tag{4.12}
\]

There are fewer than `2W<2\cdot4^r` small-star tests.  Choosing, for
example, any fixed `K>4 log 4`, equations (4.11)--(4.12) and a union bound
show that none of the tests exceeds `2t`.  Intersect this event with the
large-star event from (4.3); the latter has failure probability tending to
zero superexponentially on the `r` scale.  Hence one exact sample satisfies
both families of conclusions. `square`

This proves Theorem 0.1. `square`

## 5. What this closes and what remains

The theorem supplies one exact Catalan-scale protected bank with the
simultaneous local data

\[
 \boxed{
 \text{owners} + \text{lower }q1 + \text{upper }q1
 \text{ disjoint} + \text{low-star spread}.}
\tag{5.1}
\]

It therefore removes the possibility that the three immediate palettes
fail merely because their prospective collar banks do not intersect.

It does **not** prove any of the following.

1. The complementary owners admit an ordered four-transversal with the
   prescribed collar endpoints.
2. The remaining immediate colours can be assigned with their exact global
   multiplicities and one path topology.
3. The collar suffix targets are disjoint at every lower depth.
4. One literal factorization supplies residence and the selected endpoint
   source letters.
5. Arbitrary-width upper witnesses or the terminal common-cap compiler
   survive.

Those are correlated extension gates, not consequences of palette
disjointness or star spread alone.
