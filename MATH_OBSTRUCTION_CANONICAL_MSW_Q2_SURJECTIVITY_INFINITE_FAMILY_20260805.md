# The canonical MSW upper-`q2` projection is not surjective

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, enumeration, or solver  
**Status:** unconditional infinite-family obstruction.  It concerns the
canonical MSW complementary-geodesic factor only; it is not a no-go for a
rethreaded upper-exact forest.

## 0. Outcome

Let `P_r` be the canonical Mütze--Standke--Wiechert family of
complementary Johnson geodesics on the rank-`r` subsets of `[2r]`.  Its
edges enumerate all rank-`(r+1)` upper colours exactly once.  At an
internal owner, the union of its two incident selected edges is a
rank-`(r+2)` upper-`q2` target.

The resulting upper-`q2` map is **not** surjective.  For every even

\[
                         r=2K+2\ge6
\]

the rank-`(r+2)` target represented by the endpoint-height-four word

\[
                         T_K=(1100)^K1111                         \tag{0.1}
\]

has no canonical two-edge witness.  For every odd

\[
                         r=2K+3\ge7
\]

the same is true of

\[
                         T'_K=(1100)^K10\,1111.                    \tag{0.2}
\]

Consequently

\[
 \boxed{
   L^{(2)}(\mathcal P_r)\ne { [2r]\choose r+2}
   \quad\text{for every }r\ge6. }
                                                                    \tag{0.3}
\]

In fact the defect is Catalan-scale.  Put

\[
                         T_0=(1100)^2 1111.
\]

For every `r>=6` and every Dyck word `V` of semilength `r-6`, the
concatenated endpoint-height-four word

\[
                         T_0V                                      \tag{0.4}
\]

is also missing.  Hence the canonical upper-`q2` defect is at least

\[
                         \operatorname {Cat}_{r-6},                 \tag{0.5}
\]

which is asymptotic to `4^(-6) Cat_r`.  Thus a bounded repair bank cannot
fix the canonical factor: any repair operation changing at most `b`
internal turn values requires at least `Cat_(r-6)/b` operations.

Equivalently, in the directed two-out facet graph on `T_K` or `T'_K`,
there is no pair of facet vertices selecting one another.  Thus the
canonical MSW Hamilton half-projection closes the owner and upper-`q1`
gates but cannot, without rethreading or an additional upper repair,
close the next upper row required by the direct `B+1` route.

## 1. The exact canonical inverse test

Write a rank-`(r+2)` set as a binary path `T` of length `2r` ending at
height four.  For an up-step position `u`, let `H_T(u)` be its starting
height, and write

\[
 U_i(T;I)=\#\{u\in I:T_u=1,\ H_T(u)=i\}.
\]

The exact MSW inverse theorem says that `T` is the union of the two
selected upper facets incident with one internal canonical owner if and
only if there are up-step positions `p<q` such that

\[
\begin{array}{ll}
\text{(a)}&H_T(p)\in\{0,1\},\\
\text{(b)}&H_T(q)\in\{2,3\},\\
\text{(c)}&\text{there is no down-step starting at height `2` or `3`
strictly between `p` and `q`,}\\
\text{(d)}&U_0(T;[1,p))=U_3(T;(q,2r]).
\end{array}                                                     \tag{1.1}
\]

This is Lemma 3.1 of
`MATH_THEOREM_MSW_Q1_INVERSE_AND_SQRT_BOUND_20260725.md`.  In that
notation the upper-`q2` map is `Gamma`: if `x` is the internal owner
state, the two consecutive selected facets have union

\[
             \Gamma(x)=g'(x)\cup g(x).                           \tag{1.2}
\]

Hence it is enough to show that (1.1) has no solution for (0.1)--(0.2).

For completeness, the owner/facet formulation is identical.  If
`T` has rank `r+2`, give each facet `T-{a}` the selected endpoint pair of
its unique MSW edge and draw arcs from `a` to those two deleted endpoint
labels.  A mutual pair `a<->b` says that the two facets
`T-{a}` and `T-{b}` use the common owner `T-{a,b}`.  That is precisely a
preimage in (1.2).

## 2. Even semilength

Let `r=2K+2`, `K>=2`, and take `T=T_K` from (0.1).  Each block `1100`
starts and ends at height zero and has height trace

\[
                         0,1,2,1,0.                              \tag{2.1}
\]

Thus it contains up-steps starting at heights zero and one, but no
up-step starting at height two or three.  The terminal `1111` is the only
part of the word containing possible `q` positions from (1.1b).  They are

\[
 q_2:\ 2\longrightarrow3,
 \qquad
 q_3:\ 3\longrightarrow4.                                      \tag{2.2}
\]

Every possible `p` lying before the final `1100` block has, strictly
between it and either position in (2.2), the down-step

\[
                         2\longrightarrow1                       \tag{2.3}
\]

of that last block.  It therefore violates (1.1c).  The only surviving
`p` positions are the first two up-steps of the terminal `1111`.

For the first of these, exactly the `K` previous `1100` blocks have
contributed a height-zero up-step, so

\[
                         U_0(T;[1,p))=K.                           \tag{2.4}
\]

For the second, the first step of `1111` contributes one more, so the
left side is `K+1`.  On the other hand, the two possible right sides are

\[
 U_3(T;(q_2,2r])=1,
 \qquad
 U_3(T;(q_3,2r])=0.                                  \tag{2.5}
\]

Since `K>=2`, neither `K` nor `K+1` equals zero or one.  Condition (1.1d)
fails for every surviving pair.  Hence `T_K` has no preimage.

## 3. Odd semilength

Let `r=2K+3`, `K>=2`, and take `T=T'_K` from (0.2).  Again the only
possible `q` positions are the height-two and height-three up-steps of the
terminal `1111`, with right counts one and zero as in (2.5).

Every `p` before the last `1100` block is excluded by its final
height-two down-step.  After that down-step there are exactly three
eligible `p` positions:

1. the up-step of the intervening `10`, whose left count is `K`;
2. the height-zero up-step of the final `1111`, whose left count is
   `K+1`;
3. the height-one up-step of that `1111`, whose left count is `K+2`.

The down-step in the intervening `10` starts at height one, so it is not
forbidden by (1.1c); the list above is complete.  Because `K>=2`, none of
`K,K+1,K+2` equals either right count zero or one.  Condition (1.1d)
again fails in every case.  Thus `T'_K` has no preimage.

## 4. Dyck-suffix closure and Catalan defect

### Theorem 4.1

If an endpoint-height-four word `T` has no solution of (1.1), and every
eligible `p,q` of `T` occurs before its final visit to height four, then
`TV` also has no solution for every Dyck suffix `V`.

In particular all words (0.4) are absent from the canonical upper-`q2`
image, and they are pairwise distinct.  Therefore the number of missing
targets is at least (0.5).

#### Proof

Read `V` from initial height four.  Since every prefix height of a Dyck
word is nonnegative, every step of the suffix starts at height at least
four.  The suffix consequently contributes

* no eligible `p` at height zero or one;
* no eligible `q` at height two or three;
* no `U_3` term to the right side of (1.1d); and
* no down-step at height two or three.

Thus the complete candidate list and every value in (1.1) are unchanged
when `V` is appended.  The base word `T_0` is the case `K=2` of Section 2,
so it has no candidate pair.  This proves absence of every `T_0V`.
Distinct suffixes give distinct words, and there are `Cat_(r-6)` Dyck
suffixes of semilength `r-6`.  Finally the Catalan asymptotic gives

\[
 {\operatorname {Cat}_{r-6}\over\operatorname {Cat}_r}
                            \longrightarrow4^{-6}.                 \tag{4.1}
\]

\(\square\)

### Corollary 4.2 (bounded local repair is impossible)

An alternating incidence hexagon changes the selected incident pair at
exactly its three rank-`r` vertices, so it changes at most three values of
the upper-`q2` turn map.  Starting from the canonical MSW factor, any
sequence of incidence-hexagon switches reaching upper-`q2` surjectivity
therefore has length at least

\[
                    {1\over3}\operatorname {Cat}_{r-6}.            \tag{4.2}
\]

The same counting statement holds with `3` replaced by `b` for any local
packet that changes at most `b` turn values.

#### Proof

Changing one turn value can introduce at most one target that was absent
before the change.  There are at least `Cat_(r-6)` initially absent
targets by Theorem 4.1.  Telescoping along the repair sequence proves the
claim.  \(\square\)

## 5. Exact boundary of the obstruction

The path count leaves scalar room for upper-`q2` surjectivity.  There are

\[
  (r-1)\operatorname{Cat}_r
\]

internal canonical owners, while

\[
 {2r\choose r+2}
   ={r\over r+2}(r-1)\operatorname{Cat}_r.           \tag{5.1}
\]

So the failure is not a count obstruction; it is a literal chronology
obstruction detected by the ordinal equality (1.1d).

Nor does (0.3) contradict canonical upper-`q1` exactness.  Every
rank-`(r+1)` target still labels exactly one selected Johnson edge.  The
missing `T_K,T'_K` assert only that no two of those selected edges meet at
one owner in the required pair of facets.

The theorem is deliberately scoped to the fixed canonical MSW half.  A
palette-preserving rethread can change the pairing of facets and may create
the missing mutual pairs.  Corollary 4.2 shows that this cannot be a bounded
postprocessing of the canonical half: it must be a Catalan-scale coherent
rethread (or a different upper-exact protected forest) selected together
with the collar bank.  Any direct `B+1` proof using the MSW protected-stem
theorem must therefore supply that global repair theorem.
