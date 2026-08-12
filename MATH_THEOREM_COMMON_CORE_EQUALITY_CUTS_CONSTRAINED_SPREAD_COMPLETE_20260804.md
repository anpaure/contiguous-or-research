# Common-core reservoir: complete protected Ore closure on every equality cut

**Date:** 2026-08-04  
**Status:** unconditional asymptotic pure-mathematical theorem.  It keeps
the authenticated common internal deletion window for every three-trace
path, randomizes only the remaining low-trace paths, and adaptively packs
the resident high tail.  For this one reservoir all protected Ore--Ryser
cuts with zero clique-closure defect pass.  It does not prove the
positive-defect cuts, endpoint-collar compatibility, component placement,
or the common-cap gate.

## 0. Setting and the cut family

Fix `C>0`.  Let `m` be sufficiently large as a function of `C`, and let

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1,\quad |E|=m,
 \qquad 1\le d\le C\sqrt m.
\tag{0.1}
\]

Use the full common-core hinge ring and its hybrid clipped-resident upper
witness reservoir.  The protected incidence bank is denoted by `P`.  For
`A\subseteq\binom{[2m-1]}{m-1}`, write

\[
 \lambda_P(A)=
 \sum_U\bigl(\min\{2,a_U\}-\min\{2-p_U,a_U\}\bigr),
 \qquad
 \sigma(A)=\sum_U\min\{2,a_U\}-2|A|,
\tag{0.2}
\]

where `a_U=|\binom{U}{m-1}\cap A|` and
`p_U=e_P(U,\mathcal L\setminus A)`.  The protected Ore criterion is

\[
                         \lambda_P(A)\le\sigma(A).
\tag{0.3}
\]

The frozen equality classification says that the clique-closure defect
`b(A)` is zero exactly for

\[
 A=\mathop{\dot\bigcup}_{i}{S_i\choose m-1},
 \qquad |S_i\cap S_j|\le m-3\quad(i\ne j).
\tag{0.4}
\]

We prove (0.3) for every family (0.4).

## 1. The constrained reservoir choice

Fix the top-bank deletion prefix `F_2`.  Choose a two-set

\[
                         G_2\subset K,\qquad G_2\ne F_2,
 \qquad b\notin G_2,
\tag{1.1}
\]

as in the frozen singleton theorem.  For every noninterval damaged trace
`T\subset E` of size three, orient its three-owner geodesic so that its
unique internal deletion window is the same set `G_2`.

For every low noninterval trace of size

\[
                         4\le q\le m-d-1,
\tag{1.2}
\]

choose independently a uniformly random linear ordering of `K`, and use
the `q` consecutive windows of size `m-q`.  Top paths and the harmless
two-trace paths remain fixed.  High traces `q>=m-d` are subsequently
packed by the symmetric monotone-geodesic construction.

This retains the exact `G_2` choice used to prove all singleton cuts.  In
particular it is not the incompatible model in which the three-trace
paths are independently uniform.

For a lower vertex `x`, let

\[
                         \ell_P(x)=\lambda_P(\{x\}).
\tag{1.3}
\]

Split this load into the fixed top/three-trace contribution and the
random contribution from (1.2) and the high tail.

## 2. Uniform spread outside the fixed three-trace face

Write

\[
 x\cap E=R,\qquad K\setminus x=D,
 \qquad |R|=|D|=s.
\tag{2.1}
\]

### Lemma 2.1 (one random fixed-trace path)

For a fixed trace `T` in (1.2), the random path contributes at most one
unit to `ell_P(x)`.  If `T=R\cup\{z\}` for one
`z\in E\setminus R`, the
probability of such a contribution is at most

\[
                         {s+1\over {m-1\choose s}}.
\tag{2.2}
\]

All other traces except the possible own trace `T=R` contribute zero;
the own trace contributes at most one deterministically.

#### Proof

Every owner of the path has external trace exactly `T`.  An owner over
`x` therefore has trace `R` or `R\cup\{z\}`.  In the latter case its
`K`-part must be the fixed set `K\setminus D`, of size `m-s-1`.

The random order is invariant under `Sym(K)`.  Each of the `q=s+1`
owner positions is therefore a uniform rank-`m-s-1` subset of `K`, and
the owner positions are distinct.  This gives (2.2).  Two nonconsecutive
owners of the shortened path differ in at least two Johnson exchanges.
Since two rank-`m` supersets of the same rank-`m-1` vertex differ in at
most one exchange, `x` lies in at most two consecutive owners.  When it
lies in two, their protected intersection is `x`, so neither owner loses
the singleton cut.  Hence the path contributes at most one. \(\square\)

For `s>=3`, summing (2.2) over `z` gives

\[
 (m-s){s+1\over {m-1\choose s}}\le2.
\tag{2.3}
\]

The cases `s<3` do not occur in the randomized range (1.2).  Thus the
random low contribution at any fixed star is bounded by one deterministic
unit plus a sum of independent Bernoulli variables of total mean at most
two.

Put

\[
                         R_m=\left\lceil {6m\over\log m}\right\rceil+2.
\tag{2.4}
\]

### Lemma 2.2 (simultaneous random-star spread)

The orders in (1.2) can be chosen so that their total singleton loss is at
most `R_m` at every lower vertex.

#### Proof

For a Bernoulli sum of mean at most two,

\[
                         \Pr(X\ge r)\le(2e/r)^r.
\tag{2.5}
\]

Take `r=R_m-1`.  Then the logarithm of the right side is
`-6m+o(m)`.  There are fewer than `4^m` lower vertices.  Since
`log 4<6`, the union bound is less than one for all sufficiently large
`m`.  The extra unit in (2.4) pays the possible own-trace path. \(\square\)

### Lemma 2.3 (spread-preserving resident high tail)

The high monotone geodesics can be packed, disjointly in owner and both
immediate palettes, so that the combined random contribution from (1.2)
and the high tail is still at most `R_m` at every lower vertex.

#### Proof

One monotone Johnson geodesic increases a fixed singleton loss by at most
one: if two of its owners contain the lower vertex, they are consecutive
and their protected intersection is that vertex.

The frozen singleton proof says that the top-plus-low bank has total
singleton loss at most `m-2` at every vertex; the random choices in
(1.2) are among the arbitrary starts allowed by that proof.  During the
greedy high-tail packing, forbid both kinds of critical vertices:

* those whose current random contribution equals `R_m`; and
* those whose current total singleton loss equals `m-2`.

If `N_int` internal owners have already been chosen, then

\[
 \sum_x\ell_{\rm random}(x)=(m-2)N_{\rm int},
 \qquad
 |X_{\rm random\ crit}|\le{(m-2)N_{\rm int}\over R_m},
 \qquad
 |X_{\rm total\ crit}|\le N_{\rm int}.
\tag{2.6}
\]

Forbid every owner containing either kind of critical lower vertex.  This
adds `2^{m+o(m)}` owner resources to the existing greedy forbidden
bank.  The symmetric high-geodesic denominators are
`2^{2m-o(m)}`, whereas the number of high targets is `2^{o(m)}`.
The same union bound as in the hybrid packing theorem is therefore still
strictly below one.  A legal geodesic avoiding every critical star exists
at each step.  Induction simultaneously preserves the exact singleton
bound and the random-load bound. \(\square\)

## 3. Exact price of the fixed `q=3` concentration

Put

\[
 H=K\setminus G_2,
 \qquad
 \mathcal B=\{H\cup R:R\in{E\choose2}\}.
\tag{3.1}
\]

### Lemma 3.1 (fixed-bank singleton envelope)

The top paths contribute at most three to `ell_P(x)`.  The fixed
three-trace paths contribute at most

\[
                         1+(m-3)\mathbf1_{\{x\in\mathcal B\}}.
\tag{3.2}
\]

Consequently the complete constrained reservoir satisfies

\[
 \boxed{
 \ell_P(x)\le R_m+4+(m-3)\mathbf1_{\{x\in\mathcal B\}}.}
\tag{3.3}
\]

#### Proof

A top-path owner over `x` has external trace `R` or `R\cup\{e\}`.
There is at most one owner of the first kind.  By the cyclic-interval
deletion lemma, at most two values of `e` make the second trace a proper
cyclic interval.  Hence the top contribution is at most three.  When
`R` is empty the addition lemma has `m` exceptional singleton traces, but
all of their owners are first endpoints of top paths and contribute zero
to singleton loss; thus the same bound holds.

A three-trace path has one internal owner, namely

\[
                         (K\setminus G_2)\cup T=H\cup T.
\tag{3.4}
\]

If `|R|=2` and `D=G_2`, every possible contribution arises by adding one
external element to `R`; there are at most `m-2` such traces.  These are
exactly the vertices in `mathcal B`.  Otherwise, at most the own trace
`T=R` can contribute, and it contributes at most one.  Combining this
with Lemmas 2.2--2.3 gives (3.3). \(\square\)

The envelope is deliberately one-sided: some protected intersections
make the displayed possible contributions vanish, which only improves the
cut inequality.

## 4. One complete-support cut

Fix `S\subseteq[2m-1]`, put

\[
 t=|S|,\qquad u=2m-1-t,
 \qquad A_S={S\choose m-1}.
\tag{4.1}
\]

A rank-`m` owner meeting `A_S` either lies inside `S`, in which case all
its `m` facets lie in `A_S`, or has exactly one facet in `A_S`, in which
case it has one point outside `S`.

Let `theta_P(S)` count boundary owners of protected degree two for which
neither protected lower incidence is the unique `S`-facet.

### Lemma 4.1 (exact support formula)

For every `t>=m-1`,

\[
 \boxed{
 \lambda_P(A_S)=\theta_P(S),
 \qquad
 \sigma(A_S)={u(m-2)\over m}{t\choose m-1}.}
\tag{4.2}
\]

Moreover,

\[
                         \theta_P(S)\le
                         \sum_{x\in A_S}\ell_P(x).
\tag{4.3}
\]

#### Proof

An owner inside `S` has `a_U=m`; all of its protected facets also lie in
`A_S`, so its loss is zero.  A boundary owner has `a_U=1`; its loss is one
exactly when its protected degree is two and neither protected incidence
is its unique selected facet.  This proves the first identity.  Every
such owner also contributes one to the singleton loss of that unique
facet, proving (4.3).

There are `{t choose m}` internal owners and
`u{t choose m-1}` boundary owners.  Hence

\[
\begin{aligned}
 \sigma(A_S)
 &=2{t\choose m}+u{t\choose m-1}
   -2{t\choose m-1}\\
 &={u(m-2)\over m}{t\choose m-1},
\end{aligned}
\]

using `t=2m-1-u`. \(\square\)

### Lemma 4.2 (the exceptional family has density at most `3/m`)

If `t>=m`, then

\[
 \boxed{
 {|A_S\cap\mathcal B|\over |A_S|}\le {3\over m}.}
\tag{4.4}
\]

#### Proof

If `H` is not contained in `S`, the numerator is zero.  Otherwise write
`c=t-(m-1)>=1`.  Since `|H|=m-3`, at most `c+2` external coordinates can
belong to `S`, and therefore

\[
 |A_S\cap\mathcal B|\le {c+2\choose2},
 \qquad
 |A_S|={m-1+c\choose c}.
\tag{4.5}
\]

At `c=1` their ratio is `3/m`.  The ratio of the left side of (4.5) at
`c+1` to its value at `c` is at most

\[
                         {c+3\over m+c}\le1
\tag{4.6}
\]

for `m>=3`.  This proves (4.4). \(\square\)

### Theorem 4.3 (every one-support equality cut passes)

For all sufficiently large `m`,

\[
                         \lambda_P(A_S)\le\sigma(A_S)
\tag{4.7}
\]

for every `S` with `|S|>=m-1`.

#### Proof

If `t=m-1`, then `A_S` is a singleton and (4.7) is the frozen singleton
theorem; this is exactly where the common `G_2` orientation is used.  If
`u=0`, then `A_S=mathcal L` and both sides are zero.

Assume `t>=m` and `u>=1`.  By (3.3), (4.3), and Lemma 4.2,

\[
 \theta_P(S)\le(R_m+7){t\choose m-1}.
\tag{4.8}
\]

Thus (4.7) holds whenever

\[
                         {u(m-2)\over m}\ge R_m+7.
\tag{4.9}
\]

It remains to consider

\[
 1\le u<{m(R_m+7)\over m-2}=o(m).
\tag{4.10}
\]

The complete protected reservoir has at most

\[
                         M_P\le m(2^m+m)=2^{m+O(\log m)}
\tag{4.11}
\]

internal owners, so `theta_P(S)<=M_P`.  On the other hand, uniformly in
(4.10),

\[
 {t\choose m-1}={2m-1-u\choose m-1}=2^{2m-o(m)}.
\tag{4.12}
\]

Indeed, start from the largest binomial coefficient on `2m-1` points and
remove the `u=o(m)` points one at a time; the ratio stays at least `1/3`,
giving only the factor `3^{-u}=2^{-o(m)}`.  Equations (4.2), (4.11), and
(4.12) imply `sigma(A_S)>M_P>=theta_P(S)` for all sufficiently large `m`.
This closes the remaining range. \(\square\)

## 5. Additivity and complete zero-defect closure

### Theorem 5.1 (all `b(A)=0` cuts pass)

For the constrained resident reservoir above and all sufficiently large
`m`, every protected Ore cut with `b(A)=0` satisfies

\[
                         \boxed{\lambda_P(A)\le\sigma(A).}
\tag{5.1}
\]

#### Proof

Write `A` as in (0.4).  No rank-`m` owner can meet two distinct component
families: two different rank-`m-1` facets of one owner intersect in
`m-2` points, contradicting `|S_i\cap S_j|\le m-3`.  Hence the upper shadows
of the component families are disjoint.  Both `lambda_P` and `sigma`
therefore split additively over the supports `S_i`.  Apply Theorem 4.3 to
every summand. \(\square\)

## 6. A quantitative positive-defect neighbourhood

The equality theorem also closes an explicit family of positive-defect
cuts around every equality cut with positive certified margin.

### Lemma 6.1 (Hamming Lipschitz bound)

For arbitrary lower families `A,A'`, put

\[
                         r=|A\mathbin\triangle A'|.
\]

Then

\[
 |\lambda_P(A)-\lambda_P(A')|\le mr,
 \qquad
 |\sigma(A)-\sigma(A')|\le(m+2)r.
\tag{6.1}
\]

Consequently, if

\[
 \sigma(A')-\lambda_P(A')\ge(2m+2)r,
\tag{6.2}
\]

then `A` is safe.

#### Proof

Toggle the vertices of `A\mathbin\triangle A'` one at a time.  Toggling one lower
vertex changes `a_U` at exactly its `m` owner-neighbours.  At a neighbour
whose toggled incidence is protected, `p_U` changes in the opposite
direction at the same time.  Directly from

\[
 f(a,p)=\min\{2,a\}-\min\{2-p,a\},
 \qquad 0\le p\le2,
\]

the combined change of `f` is at most one.  Thus `lambda_P` changes by at
most `m`.  The sum of the truncated owner counts in `sigma` changes by at
most `m`, while `-2|A|` changes by two.  This proves (6.1), and (6.2)
follows by subtraction. \(\square\)

For a one-support equality cut in the broad range (4.9), the proof gives
the explicit certified margin

\[
 \Delta(S)=
 \left({u(m-2)\over m}-(R_m+7)\right){t\choose m-1}.
\tag{6.3}
\]

In the near-full range (4.10), it gives

\[
 \Delta(S)={u(m-2)\over m}{t\choose m-1}-M_P.
\tag{6.4}
\]

Hence every lower family within Hamming distance at most

\[
 \left\lfloor{\Delta(S)\over2m+2}\right\rfloor
\tag{6.5}
\]

of that support clique is also safe.  Apart from the zero-margin endpoint
cases, this includes many families with `b(A)>0`.  It is a genuine
stability neighbourhood, but not a classification of every small-positive
`b(A)` cut: clique closure can propagate over much larger Hamming distance.

## 7. Exact frontier

The proof closes all equality cases of the shadow-slack inequality while
simultaneously retaining:

1. the common `G_2` orientation used by the exact singleton theorem;
2. clipped residence of every low and high witness path;
3. owner, immediate-lower, and immediate-upper resource disjointness; and
4. the complete common-core upper witness deck.

It does not use or require the endpoint-exposure estimate from the earlier
random-spread draft.  That estimate is false for the fixed top bank: the
lower vertex `K` lies in all `m` first top-path endpoints.

Every still-unproved protected Ore cut has positive clique-closure defect
`b(A)>0`.  Closing those cuts requires a stability theorem relating this
positive defect to protected loss; the exact equality family no longer
contributes an obstruction.

## 8. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| equality-cut classification and exact slack | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| fixed `G_2` singleton theorem | `MATH_THEOREM_COMMON_CORE_MINIMAL_RESERVOIR_SINGLETON_ORE_AND_RESIDENCE_SPLIT_20260804.md` | `bfc9b6cc16c19e06ea8c455d688099e90fd8c80bd476b71fdbbbff1c1f91ae87` |
| hybrid clipped-resident high-tail packing | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| upper-damage family and common-core witness deck | `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md` | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |
