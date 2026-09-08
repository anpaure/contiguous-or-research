# Common-core reservoir: a hybrid clipped-resident witness packing

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical construction.  It
repairs the local residence defect in the full-size common-core upper
witness reservoir.  Small external traces use shortened sliding-window
paths whose internal positive runs have length at least `d+1`; the
subexponential high tail uses greedily packed random monotone Johnson
geodesics.  The resulting paths are pairwise disjoint in owners, immediate
lower colours, and immediate upper colours, and avoid the protected hinge
bank.  No search, solver, or sampled computation is used.

## 0. Setup and clipped residence

Let

\[
 K\sqcup E=[2m-1],
 \qquad |K|=m-1,
 \qquad |E|=m,
\tag{0.1}
\]

and let `mathcal D` be the full-size common-core damage family

\[
 \mathcal D={K\cup T:\varnothing\ne T\subsetneq E,
 \ T\text{ contains a cyclic hinge edge}\}.
\tag{0.2}
\]

Owners have rank `m`.  A Johnson path is called **`d`-clipped resident**
if, for every coordinate, every positive occurrence run which meets neither
endpoint of the path has length at least `d+1`.  Endpoint runs are exported
as boundary collars; no global cyclic-residence assertion is made here.

Assume

\[
                         1\le d=d(m)=O(\sqrt m).
\tag{0.3}
\]

Precisely, for every fixed constant `C>0`, all conclusions below hold for
all sufficiently large `m` whenever `1<=d<=C sqrt(m)`.  The threshold in
`m` is allowed to depend on `C`.

## 1. The low-trace shortening

Retain the monotone top paths for cyclic-interval traces from the frozen
common-core reservoir.  Along each such path, a `K`-coordinate occurs in
an initial run and an `E`-coordinate in a terminal run.  Hence every top
path is `d`-clipped resident for every `d`.

Now fix a noninterval trace `T` of size

\[
                         3\le q=|T|\le m-d-1
\tag{1.1}
\]

and put

\[
                         h=m-q\ge d+1,
 \qquad n=|K|=m-1.
\tag{1.2}
\]

Choose a linear presentation

\[
                         K=(k_0,k_1,\ldots,k_{n-1})
\]

and, for `0<=j<=q-1`, define the consecutive `h`-window

\[
 W_{T,j}={k_j,k_{j+1},\ldots,k_{j+h-1}}.
\tag{1.3}
\]

There is no wrap in (1.3), because

\[
                         (q-1)+(h-1)=m-2=n-1.
\]

Put

\[
                         V_{T,j}=T\cup W_{T,j}
\tag{1.4}
\]

and take

\[
 \mathcal Q_T^{\rm low}
 =(V_{T,0},V_{T,1},\ldots,V_{T,q-1}).
\tag{1.5}
\]

### Lemma 1.1

The path `mathcal Q_T^low` is a simple Johnson path with union `K union T`.
Its owners, immediate lower colours, and immediate upper colours are all
distinct.  It is `d`-clipped resident.

### Proof

Every owner has size `q+h=m`.  Consecutive owners delete `k_j` and insert
`k_(j+h)`.  Their lower and upper colours are respectively

\[
 T\cup{k_{j+1},\ldots,k_{j+h-1}},
\tag{1.6}
\]

and

\[
 T\cup{k_j,\ldots,k_{j+h}}.
\tag{1.7}
\]

The starting positions distinguish all owners and both palettes.  Also,
the union of the `q` consecutive `h`-windows is all of `K`, since their
total spanned interval has length

\[
                         h+q-1=m-1=|K|.
\]

Thus the full path union is `K union T`.

Every coordinate of `T` occurs throughout.  For `k_s in K`, the set of
owner indices containing it is

\[
 [s-h+1,s]\cap[0,q-1],
\tag{1.8}
\]

an interval.  If this interval meets neither endpoint `0` nor `q-1`, its
length is exactly `h>=d+1`.  Hence the path is `d`-clipped resident.
\(\square\)

The harmless two-owner construction for `q=2` is also clipped resident,
because every positive coordinate run meets a path endpoint.  (For the
full-size damage family this case is actually vacuous among noninterval
traces: a two-element trace containing a cyclic hinge edge is itself a
cyclic interval.)  Different
low targets have different exact external traces `T`; a low noninterval
trace is also distinct from every cyclic-interval trace in the top bank.
Consequently the complete top-plus-low bank is globally disjoint in all
three resource ranks.

## 2. High traces and monotone geodesics

It remains to treat a noninterval target

\[
 Z=K\cup T,
 \qquad q=|T|=m-h,
 \qquad 1\le h\le d.
\tag{2.1}
\]

Its ground set has size

\[
                         N=|Z|=2m-h-1.
\tag{2.2}
\]

Choose a partition

\[
 Z=C\sqcup X\sqcup Y,
 \qquad |C|=h+1,
 \qquad |X|=|Y|=q-1,
\tag{2.3}
\]

and orders

\[
 X=(x_1,\ldots,x_{q-1}),
 \qquad Y=(y_1,\ldots,y_{q-1}).
\]

Define

\[
 A_t=C\cup{x_{t+1},\ldots,x_{q-1}}
       \cup{y_1,\ldots,y_t},
 \qquad 0\le t\le q-1.
\tag{2.4}
\]

Then `(A_0,...,A_(q-1))` is a monotone Johnson geodesic: at step `t`, it
deletes `x_(t+1)` and inserts `y_(t+1)`.  Its endpoint union is

\[
                         A_0\cup A_{q-1}=Z.
\tag{2.5}
\]

Every `x`-coordinate occurs in an initial run, every `y`-coordinate in a
terminal run, and every core coordinate throughout.  Thus this path has no
internal positive run at all and is `d`-clipped resident for every `d`.

## 3. Exact symmetric hitting probabilities

Choose the data in (2.3)--(2.4) uniformly and symmetrically: choose `C`
uniformly, then choose a uniformly random ordering of `Z setminus C`, using
its first `q-1` entries as the ordered list `X` and its remaining entries
as the ordered list `Y`.

### Lemma 3.1

For a fixed resource contained in `Z`, the probabilities that the random
geodesic uses it are exactly

\[
 \boxed{
 \Pr(O\text{ is an owner})={q\over {N\choose m}},}
\tag{3.1}
\]

for `O in binom(Z,m)`,

\[
 \boxed{
 \Pr(L\text{ is an immediate lower colour})
 ={q-1\over {N\choose m-1}},}
\tag{3.2}
\]

for `L in binom(Z,m-1)`, and

\[
 \boxed{
 \Pr(U\text{ is an immediate upper colour})
 ={q-1\over {N\choose m+1}}.}
\tag{3.3}
\]

A resource not contained in `Z` has probability zero.

### Proof

The distribution is invariant under the full symmetric group of `Z`.
Every owner position therefore has the uniform rank-`m` marginal.  The
owners are distinct because `|A_t cap Y|=t`.  Summing the disjoint position
events proves (3.1).

On edge `t`, the lower colour is `A_t cap A_(t+1)` and has exactly `t`
coordinates of `Y`; the upper colour is `A_t union A_(t+1)` and has exactly
`t+1` coordinates of `Y`.  Thus each palette is simple.  Symmetry and the
same disjoint-position argument prove (3.2)--(3.3). \(\square\)

## 4. Uniform binomial supply

Let

\[
 H_d=\sum_{j=1}^{d}{m\choose j}.
\tag{4.1}
\]

This upper-bounds the number of high targets, because such a target omits
`h<=d` elements of `E`.  Since `d=O(sqrt m)`,

\[
 H_d\le(d+1)\left({em\over d}\right)^d=2^{o(m)}.
\tag{4.2}
\]

We need a simultaneous lower bound on the three binomial denominators in
Lemma 3.1, uniform also over the target parameter `1<=h<=d`.  For fixed
`h` and `r in {m-1,m,m+1}`, put `N_h=2m-h-1` and `p=r/N_h`.  The `r`-th term is a
mode of the binomial distribution with parameter `p`, so

\[
 {N_h\choose r}p^r(1-p)^{N_h-r}\ge{1\over N_h+1}.
\tag{4.3}
\]

Equivalently,

\[
 {N_h\choose r}\ge {2^{N_hH_2(p)}\over N_h+1}.
\tag{4.4}
\]

If `p=1/2+t` and `|t|<=1/4`, the elementary entropy estimate

\[
                         H_2(1/2+t)\ge1-6t^2
\tag{4.5}
\]

follows by expanding the binary relative entropy, or by differentiating
its two sides.  Here

\[
 |t|\le {h+3\over2N_h}.
\]

Consequently, uniformly for `h<=d`,

\[
\boxed{
 \underline B_m:=
 \min_{1\le h\le d}\ \min_{r\in\{m-1,m,m+1\}}
 {N_h\choose r}
 \ge
 {1\over2m}
 2^{\,2m-d-1-
 {3(d+3)^2\over2(2m-d-1)}}
 =2^{\,2m-o(m)}.}
\tag{4.6}
\]

## 5. Greedy disjoint packing

Order the high targets arbitrarily.  Before selecting the geodesic for one
of them, forbid every owner, lower colour, and upper colour already used by:

1. the top cyclic-interval bank;
2. all shortened low-trace paths;
3. the protected hinge bank;
4. every earlier high-trace geodesic.

For each of the three resource ranks, the number of forbidden resources is
at most

\[
 R_m:=4m(2^m+H_d).
\tag{5.1}
\]

Indeed, there are at most `2^m` low targets and `H_d` high targets, every
path uses at most `m` resources of each rank, the top bank uses fewer than
`m^2`, and the hinge bank uses only `O(m)` resources.  Formula (5.1) is a
uniform overcount for sufficiently large `m`.

By Lemma 3.1 and the union bound, the probability that a random geodesic
hits any forbidden resource is at most

\[
 {qR_m\over{N\choose m}}
 +{(q-1)R_m\over{N\choose m-1}}
 +{(q-1)R_m\over{N\choose m+1}}
 \le {3mR_m\over \underline B_m}.
\tag{5.2}
\]

Equations (4.2), (4.6), and (5.1) give

\[
 {3mR_m\over \underline B_m}
 \le {12m^2(2^m+H_d)\over2^{\,2m-o(m)}}
 =2^{-m+o(m)}<1
\tag{5.3}
\]

for all sufficiently large `m`.  Thus at every greedy step a legal
geodesic exists.  Induction packs all high targets simultaneously.

### Theorem 5.1 (hybrid resident reservoir)

For every `d=O(sqrt m)` and all sufficiently large `m`, the full-size
common-core damage family has a simultaneous path bank with the following
properties:

1. every target `Z in mathcal D` is the union of one contiguous Johnson
   path in the bank;
2. all owners are distinct;
3. all immediate lower colours are distinct;
4. all immediate upper colours are distinct;
5. every path is `d`-clipped resident;
6. the bank avoids any separately listed `O(m)` hinge resources; in the
   canonical full-size realization, the hinge bank may instead be retained
   as the first edges of the top paths.

The construction is explicit for cyclic-interval and low noninterval
traces, and existential by the symmetric probabilistic method for the high
tail.

In the canonical full-size ring coinstantiation, the cyclic rethread also
preserves clipped residence on every transported top path.  The new path
beginning with `L_i,R_(i+1)` and continuing along the old `(i+1)`-suffix
has `b` only in its first owner, every other `K`-coordinate in an initial
run, `a_i` throughout, and every remaining external coordinate in a
terminal run.  It therefore has no internal positive run.  Every private
low or high path is disjoint from the top bank and is untouched by the
rethread.

## 6. Exact scope

This theorem repairs **internal residence inside the protected common-core
reservoir**.  It does not prove global cyclic residence after factor
completion, prescribe the endpoint collars, prove the weighted Ore--Ryser
extension inequalities, place the distinguished hinges on separate factor
components, or solve the common cap.  Those remain genuinely separate
global rows.

## 7. Frozen dependency

| role | file | SHA-256 |
|---|---|---|
| common-core damage compression, top paths, and hinge coinstantiation | `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md` | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |
