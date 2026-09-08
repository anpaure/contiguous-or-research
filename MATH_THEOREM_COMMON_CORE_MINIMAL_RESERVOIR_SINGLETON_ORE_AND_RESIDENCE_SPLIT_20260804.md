# Minimal common-core rays, exact singleton Ore closure, and the residence split

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical strengthening and scope audit of
`MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md`.
It shortens every private witness to its geodesic minimum, proves every
singleton protected Ore--Ryser cut, and proves all cuts whose complementary
lower shore has size at most `m-2`.  It also shows that the random-geodesic
packing of the resident high-trace tail can be performed while preserving
all singleton inequalities.  It does not prove the remaining multi-vertex
Ore cuts.  The residence audit records the exact split: fixed-trace rays
work below the top `d` ranks, while the top tail needs monotone geodesics.

## 0. Setting

Use the notation of the common-core reservoir.  Thus `m>=4` and

\[
 |K|=m-1,\qquad |E|=m,
\]

and write

\[
 W=\left|{[2m-1]\choose m-1}\right|
  =\left|{[2m-1]\choose m}\right|.
\]

and every possible damaged target has the unique form `K union T`.  Fix
cyclic orders

\[
 K=(k_1,k_2,\ldots,k_{m-1}),\qquad
 E=(e_0,e_1,\ldots,e_{m-1}),
\]

with `k_1=b`.  In the full ring specialization `c=m`, the top path starting
with external label `a_i` has first two owners

\[
 K+a_i,qquad (K-b)+a_i+a_{i-1}.
\]

These are literally the ring owners `L_i,R_i`; their common lower colour is
`B+a_i`.  Thus the hinge is identified with, rather than added to, the first
top-path edge.

For `p<=m-3`, write

\[
 D_s^{(p)}=\{k_s,k_{s+1},\ldots,k_{s+p-1}\}
 \quad(s\in\mathbb Z/(m-1)\mathbb Z)
\tag{0.1}
\]

for a cyclic `p`-window of `K`.

## 1. Every private ray has a geodesic truncation

Fix a noninterval external trace `T`, put

\[
 q=|T|,\qquad p=q-1,
\]

and assume `3<=q<=m-2`.  Choose an arbitrary start `s(T)` and define

\[
 V_{T,j}=(K\setminus D_{s(T)+j}^{(p)})\cup T,
 \qquad 0\le j\le p.
\tag{1.1}
\]

Let

\[
 \mathcal G_T=(V_{T,0},V_{T,1},\ldots,V_{T,p}).
\tag{1.2}
\]

For `q=2`, instead choose distinct `u_T,v_T in K` and use the one-edge
path

\[
 (K-u_T)+T,\quad(K-v_T)+T.
\tag{1.3}
\]

### Theorem 1.1 (minimal private geodesic)

The path `mathcal G_T` has exactly `q` owners and `q-1` Johnson edges.  Its
owner, immediate-lower, and immediate-upper colours are simple.  Its union
is exactly

\[
                         K\cup T.
\tag{1.4}
\]

Paths belonging to different external traces have disjoint owner and q1
colour sets.  They are also disjoint from the cyclic-interval top bank.

#### Proof

Successive deletion windows in (1.1) differ by one leaving and one entering
coordinate.  Thus successive owners are Johnson adjacent.  Their omission
union and intersection are respectively cyclic windows of lengths `p+1`
and `p-1`; because `p+1<=m-2`, all such windows occurring in the displayed
linear segment are distinct.  This proves both q1 simplicities.

The `p+1` consecutive `p`-windows have empty total intersection.  Indeed,
every member of the first window leaves during the next `p` shifts, while a
coordinate outside the first window is absent there already.  Hence every
coordinate of `K` occurs in some owner.  Every owner contains `T`, proving
(1.4).

Every owner and q1 colour in this path has external trace exactly `T`.
Different noninterval traces are therefore disjoint, and no such trace is
a cyclic interval.  Formula (1.3) proves the `q=2` case and, importantly,
uses only one occurrence of its immediate-upper colour `K union T`.
\(\square\)

The length `q` is minimal: a Johnson path beginning at rank `m` can raise
the rank of its cumulative union by at most one per edge, while
`|K union T|-m=q-1`.

The starts `s(T)` are free balancing variables.  Changing a start changes
which two deletion-window owners are endpoints, without changing any
target or palette statement.

## 2. A choice closing every singleton Ore cut

Let

\[
 F_j=\{k_1,\ldots,k_j\}
\tag{2.1}
\]

be the deletion prefix on every top path.  Choose one cyclic two-window

\[
 G_2\ne F_2,\qquad k_1=b\notin G_2.
\tag{2.2}

For every noninterval triple `T`, choose `s(T)` so that the unique internal
deletion window of its three-owner geodesic is `G_2`.  Starts for all other
private traces are arbitrary.

Let `P` be the incidence lift of the full cyclic-interval top bank together
with these minimal private geodesics.  In the `c=m` ring, identify each
hinge with the first top edge as above; do not count it twice.

### Lemma 2.1 (two deletion candidates away from the full cycle)

If `D` is a subset of a cyclically ordered `n`-set and
`2<=|D|<=n-1`, then at most two elements `x in D` have the property that
`D-x` is a proper cyclic interval.  Likewise, if
`1<=|R|<=n-2`, then at most two elements `e` outside `R` make `R+e` a
proper cyclic interval.

#### Proof

View `D` as a union of components in the ambient cycle.  If it has at least
three components, deleting one point cannot leave one nonempty component.
If it has two components, the deleted point must be the sole member of one
of them, giving at most two choices.  If it has one component, only one of
its two endpoints can be deleted, again giving at most two choices.  The
hypotheses exclude the full cycle, for which every co-singleton is a cyclic
interval and the unqualified statement would be false.

For the addition assertion apply the deletion assertion to the complement
`D` of `R`: the complement of `R+e` is `D-e`, and complements of nonempty
proper cyclic intervals are nonempty proper cyclic intervals. \(\square\)

### Theorem 2.2 (all singleton cuts pass)

For every lower vertex `x`, the exact protected loss satisfies

\[
                         \lambda_P(\{x\})\le m-2
                         =\sigma(\{x\}).
\tag{2.3}
\]

#### Proof

Put

\[
 R=x\cap E,qquad D=K\setminus x,qquad |R|=|D|=s.
\]

The `m` owner-neighbours of `x` split into

* `K`-additions, with external trace `R` and deletion set `D-k`; and
* `E`-additions, with trace `R+e` and deletion set `D`.

An owner contributes to the singleton loss only when both protected
incidences at that owner go to lower vertices other than `x`.  In
particular it must be an internal owner of one protected path.  Counting
all internal protected owner-neighbours therefore gives an upper bound.

If `s=0`, every protected neighbour is the first endpoint of a top path,
so the count is zero.  If `s=1`, noninterval pair paths have no internal
owner, while at most the two cyclic-pair completions are internal top
owners.  The count is at most `2<=m-2`.

Let `s=2`.  A `K`-addition contributes at most one top internal owner and
none from a private pair path.  An `E`-addition can be internal in the top
bank only when `D=F_2`, and can be internal in a private triple path only
when `D=G_2`.  If `D=F_2`, there are at most two top additions and no
private ones; together with the possible `K`-addition this is at most
three, which is at most `m-2` for `m>=5`.  If `D=G_2`, there is no top or
`K` contribution because `b notin G_2`, and there are at most `m-2`
external additions.  Every other `D` gives at most one contribution.  For
`m=4`, a length-three top owner is an endpoint, and the same bound follows
directly.

Let `s=3`.  There are at most `m-3` external additions.  If `R` is a cyclic
interval, at most one `K`-addition is a top internal owner.  If `R` is
noninterval, its three-owner private path has only one internal owner, so
again at most one `K`-addition contributes.  The total is at most `m-2`.

Finally let `4<=s<=m-2`.  There are at most `m-s` external additions.  By
Lemma 2.1, at most two `K`-additions can lie on the appropriate top or
private path.  Hence the total is at most

\[
                         m-s+2\le m-2.
\]

If `s=m-1`, then `R` is an external co-singleton and hence a cyclic
interval.  Its unique top owner is the last endpoint of its top path, so
no `K`-addition contributes.  The sole external addition produces the
full external trace `E`, whose full-ground target is absent from the
proper damage bank.  Thus the contribution is zero.

The singleton value `sigma({x})=m-2` is the sharp weighted-boundary
identity.  This proves (2.3). \(\square\)

The proof deliberately overcounts internal neighbours for which one of the
two path incidences actually lands at `x`; such an owner has protected loss
zero, so the bound remains valid.

## 3. Every small complementary cut is automatic

### Theorem 3.1 (co-small Ore closure)

Let `X` be any lower-vertex set with `|X|<=m-2`, and put

\[
                         A=\mathcal L\setminus X.
\]

Then every maximum-degree-two protected bank `P`—not only the reservoir—
satisfies

\[
                         \lambda_P(A)\le\sigma(A).
\tag{3.1}
\]

#### Proof

Every owner has at least `m-|X|>=2` lower neighbours in `A`.  Hence

\[
 \sum_U\min\{2,d_A(U)\}=2|\mathcal U|,
\]

and, since the two shores have the same size,

\[
 \sigma(A)=2|\mathcal U|-2|A|=2|X|.
\]

For `d_A(U)>=2`, the owner contribution to protected loss is exactly the
number of protected incidences from `U` into `X`.  Therefore

\[
 \lambda_P(A)=e_P(\mathcal U,X)
              \le\sum_{x\in X}d_P(x)
              \le2|X|=\sigma(A).
\]

\(\square\)

Combining Theorems 2.2 and 3.1, the unresolved protected-factor cuts may be
restricted exactly to

\[
 2\le |A|,qquad
 |\mathcal L\setminus A|\ge m-1.
\tag{3.2}

This is still an exponential cut family; no extension claim is made.

For this particular bank the remaining inequality has a simpler exact
form.  Let `L_2` be the selected immediate-lower colours, let `U_2` be the
internal path owners, and let `U_1` be the path endpoints.  All vertices of
`L_2` and `U_2` already have protected degree two, while an owner in `U_1`
has residual capacity one and every unused owner has capacity two.

### Theorem 3.2 (exact residual path-forest Hall)

The protected path bank extends to a spanning two-factor if and only if,
for every

\[
                         X\subseteq\mathcal L\setminus L_2,
\]

one has

\[
 \boxed{
  2|X|\le
  \sum_{U\notin U_1\cup U_2}\min\{2,|N(U)\cap X|\}
  +|\{U\in U_1:N(U)\cap X\ne\varnothing\}|.}
\tag{3.3}
\]

#### Proof

Delete the already saturated shores `L_2,U_2`.  Give every remaining lower
vertex demand two.  An unused owner has capacity two and an endpoint owner
capacity one.  The capacitated bipartite Hall theorem is exactly (3.3).
If `J=|L_2|` is the number of Johnson edges in the protected paths, then
the protected incidence bank has `2J` edges, and

\[
 2|U_2|+|U_1|=2J.
\]

Hence the total residual upper capacity and total residual lower demand
are both `2W-2J`.  Consequently an integral flow satisfying all lower
demands also saturates every residual upper capacity and completes the
protected bank to degree two on both shores. \(\square\)

Thus the final factor gate is no longer an opaque weighted inequality: it
is one ordinary capacity-two Hall system in the Middle-Levels graph after
the explicit witness paths are contracted.  Theorem 2.2 verifies all
one-vertex rows of (3.3); Theorem 3.1 verifies the corresponding near-full
rows.

There is also an exact identity showing what is missing beyond the
singleton rows.  Put

\[
 \ell_P(x)=\lambda_P(\{x\}),
 \qquad a_U=|N(U)\cap A|,
 \qquad t_U=e_P(U,A).
\]

Define

\[
 C_{\le1}(A)=
   \sum_{U:d_P(U)\le1}(a_U-2)_+,
\tag{3.4}
\]

and

\[
 E_1(A)=
 |\{U:d_P(U)=1, a_U\ge2, t_U=0\}|.
\tag{3.5}
\]

### Theorem 3.3 (singleton slack pays unsaturated clique overlap)

For every lower cut `A`,

\[
 \boxed{
 \sigma(A)-\lambda_P(A)=
 \sum_{x\in A}(m-2-\ell_P(x))
 -C_{\le1}(A)-E_1(A).}
\tag{3.6}
\]

Hence, after all singleton rows have been proved, the complete factor gate
is exactly

\[
 \boxed{
 \sum_{x\in A}(m-2-\ell_P(x))
 \ge C_{\le1}(A)+E_1(A)
 \quad(A\subseteq\mathcal L).}
\tag{3.7}

#### Proof

For one owner of protected degree two, summing its contributions to the
singleton losses over its `a_U` facets in `A` gives `a_U-t_U`.  Its direct
contribution to `lambda_P(A)` is the same when `a_U<=1`, and is `2-t_U`
when `a_U>=2`; their difference is `(a_U-2)_+`.

An owner of protected degree zero contributes to neither loss.  An endpoint
owner contributes one to `lambda_P(A)` precisely when `a_U>=2,t_U=0`, and
nothing to any singleton loss.  Therefore

\[
 \lambda_P(A)=
 \sum_{x\in A}\ell_P(x)
 -\sum_{U:d_P(U)=2}(a_U-2)_+
 +E_1(A).
\]

Finally

\[
 \sigma(A)=(m-2)|A|-\sum_U(a_U-2)_+,
\]

which follows from `sum_U a_U=m|A|` and
`min(2,a)=a-(a-2)_+`.  Subtraction gives (3.6)--(3.7).
\(\square\)

Formula (3.7) is the sharp obstruction left by the singleton theorem:
unused and endpoint owners lying over several members of `A` create a
clique-overlap debt, and only unused singleton capacity can pay it.

### Corollary 3.4 (exact frozen near-shadow scope)

The frozen near-shadow localization theorem further restricts every
failed cut.  Put

\[
 s_A=|N(A)|-|A|,
 \qquad
 b_A=\sum_{U:2\le a_U\le m-1}(m-a_U),
 \qquad e=|E(P)|.
\]

If `lambda_P(A)>sigma(A)`, then necessarily

\[
 \boxed{(m-2)s_A+b_A\le(m-1)\lambda_P(A)-1,}
\tag{3.8}
\]

\[
 |\mathcal L\setminus A|\ge m-1,
 \qquad s_A\ge m-1,
 \qquad \lambda_P(A)\ge m-1,
\tag{3.9}
\]

and

\[
 \boxed{
 \min\{|A|,W-|A|\}
 <{m(m-1)\over2m-1}\lambda_P(A)
 \le {m(m-1)\over2m-1}e.}
\tag{3.10}
\]

It must also satisfy the exact Kruskal--Katona restriction

\[
 \partial_m(|A|)-|A|
 \le e+\left\lfloor{e-1\over m-2}\right\rfloor.
\tag{3.11}
\]

where `partial_m(a)` is the minimum lower-shadow size of an `a`-member
family of rank-`m` sets.

Hence the open family is not all of (3.2), but only its multi-vertex,
non-co-small, near-tight upper-shadow subfamily satisfying
(3.8)--(3.11).  These are necessary conditions for failure, not a factor
extension theorem.

## 4. Residence audit and the necessary hybrid

The geodesic truncation is an upper-witness theorem, not by itself an
unqualified resident-host theorem.

For the asymptotic packing statements in this section, fix `C>0` and
assume `1<=d<=C sqrt(m)` with `m` sufficiently large as a function of
`C`, exactly as in the frozen hybrid-reservoir theorem.  Put

\[
 H_d=\sum_{h=1}^d {m\choose h}=2^{o(m)}.
\]

Along the full cyclic-deletion path for trace size `q`, every external
coordinate has a run of length `m-1`, while an internal positive run of a
`K` coordinate has length

\[
                         m-q.
\tag{4.1}

Thus the full fixed-trace path is internally positive-resident at depth
`d` only for

\[
                         q\le m-d-1.
\tag{4.2}

On a minimal `q`-owner geodesic, the external trace has run length `q`.
For `q<d+1` this run requires an endpoint collar.  For
`q>=m-d`, equation (4.1) shows that the cyclic fixed-trace geometry creates
a short internal `K` run and cannot be repaired merely by extending the
two endpoints.

The top band has only

\[
 \sum_{t=2}^{d}{m\choose t}=2^{o(m)}
\tag{4.3}

targets, since there `q=m-t`.  Its appropriate replacement is a monotone
geodesic.  For `Z=K union T` of rank `2m-t-1`, choose rank-`m` endpoints
`A_Z,B_Z subseteq Z` with

\[
 A_Z\cup B_Z=Z,qquad |A_Z\cap B_Z|=t+1,
\tag{4.4}

and monotonically exchange the `m-t-1` elements of `A_Z-B_Z` for those of
`B_Z-A_Z`.  Every coordinate run in this geodesic is a prefix, a suffix,
or the whole path.  It therefore has no internal short positive run and is
`d`-clipped resident.  Endpoint runs are exported; the existence of
compatible physical endpoint collars is not asserted here.

The frozen hybrid-reservoir theorem supplies the occurrence-level greedy
packing of these `2^{o(m)}` clipped geodesics, disjoint in owner and q1
resources from the fixed-trace bank.  Its greedy choice can be strengthened
to retain Theorem 2.2.  Two global rows still remain:

1. select mutually compatible endpoint collars in the ambient carrier;
   and
2. prove the joint protected bank satisfies the residual cuts
   (3.2), equivalently only the localized subfamily (3.8)--(3.11).

### Lemma 4.1 (one monotone path costs at most one per singleton)

Let `G=(A_0,...,A_s)` be a monotone Johnson geodesic.  For every lower
vertex `x`, adjoining the incidence lift of `G` increases
`lambda({x})` by at most one.

#### Proof

If `A_i` and `A_j`, `i<j`, both contain `x`, then their intersection has
rank at least `m-1`.  Monotonicity gives

\[
                         |A_i\mathbin\triangle A_j|=2(j-i),
\]

so `j-i<=1`.  If two consecutive owners contain `x`, their intersection is
exactly `x`; the protected incidence between them lands at `x`, and neither
owner has two protected incidences going outside the singleton cut.
Endpoints also have protected degree at most one.  Thus only one internal
owner can contribute a new unit. \(\square\)

### Theorem 4.2 (adaptive high-tail packing preserves singleton Ore)

Assume the top-plus-low bank has been oriented as in Section 2, so every
singleton cut is safe.  The high-trace monotone geodesics in the hybrid
resident reservoir can be greedily selected so that every singleton cut
remains safe.

#### Proof

At one greedy stage call a lower vertex `x` critical when

\[
                         \lambda_P(\{x\})=m-2.
\]

For sufficiently large `m`, every trace of size three lies in the low
range (4.2), so the common `G_2` orientation used in Theorem 2.2 is
retained.  Deleting the as-yet unchosen high paths cannot increase any
singleton loss, hence the initial top-plus-low bank is safe.

An internal owner of one protected path contributes singleton loss for
exactly its `m-2` lower facets other than the two path incidences.  Hence,
if `N_int` is the current number of internal protected owners,

\[
 \sum_x\lambda_P(\{x\})=(m-2)N_{\rm int},
 \qquad |X_{\rm crit}|\le N_{\rm int}.
\tag{4.5}
\]

Forbid every owner containing a critical lower vertex.  This adds at most

\[
                         mN_{\rm int}
\tag{4.6}

owner resources to the greedy forbidden bank.  Throughout the hybrid
construction,

\[
 N_{\rm int}=O\bigl(m(2^m+H_d)\bigr),
\]

so (4.6) is `O(m^2(2^m+H_d))`.  Replacing the resource bound `R_m` in the
hybrid theorem by this extra polynomial factor leaves its collision
probability

\[
 {O(m^3(2^m+H_d))\over 2^{2m-o(m)}}
 =2^{-m+o(m)}<1.
\]

Therefore a collision-free high geodesic avoiding all critical stars still
exists at each step.  Critical singleton losses do not increase.  Every
noncritical loss is at most `m-3` and rises by at most one by Lemma 4.1.
Induction proves the theorem. \(\square\)

This adaptive restriction preserves owner/q1 disjointness and clipped
residence, because it only enlarges the forbidden owner set in the same
symmetric greedy argument.

## 5. Exact frontier

The common-core ring now has an explicit all-width upper reservoir, and its
private pieces can be chosen at geodesic-minimum length.  The full-size
ring covariantly redelivers all cyclic-interval traces; only noninterval
traces require retained private paths.  After the balancing choice (2.2),
all singleton Ore cuts pass.  The resident high tail can be packed without
reopening them.  All cuts with complementary shore at most `m-2` pass for
every two-bounded bank.

The smallest exact unproved factor statement is therefore:

> choose the remaining path starts and the collared high-trace monotone
> geodesics so that the weighted protected Ore inequality holds for every
> localized cut in (3.8)--(3.11).

Arbitrary-width upper coverage itself is no longer an open row once that
factor contains the bank.  Internal positive residence is solved, while
compatible endpoint-collar selection remains open.  Component distribution
and the common cap remain separate.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| common-core damage family, top bank, and hinge coinstantiation | `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md` | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |
| exact protected weighted boundary | `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md` | `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891` |
| near-shadow localization used in Corollary 3.4 | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| hybrid clipped-resident packing | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
