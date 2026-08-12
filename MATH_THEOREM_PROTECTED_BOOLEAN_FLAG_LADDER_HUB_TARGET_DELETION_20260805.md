# Protected Boolean flag ladders: exact extension of the hub target bank

**Date:** 2026-08-05  
**Method:** Kruskal--Katona shadow surplus and Hall's theorem; no computation  
**Status:** unconditional integral named-target theorem.  Every
\(O(d)\)-sized protected family of disjoint saturated chains in a band below
the Boolean middle extends to a chain decomposition of the complete band.
In particular, the coloured hub necklace causes zero residual named-target
deficiency in its high band.  Functional predecessor serialization of the
resulting chains remains open.

## 0. Outcome

Let

\[
                         r=\lceil k/2\rceil,
\]

and let

\[
 {\cal B}_s={[k]\choose s}.
\]

Suppose \(L\) pairwise target-disjoint saturated chains have been prescribed
through a consecutive band

\[
 {\cal B}_a,{\cal B}_{a+1},\ldots,{\cal B}_r,         \tag{0.1}
\]

so that at every interface \(s\to s+1\) their prescribed edges form a
matching \(P_s\) of size \(L\).  If

\[
                         L\le k-r,                    \tag{0.2}
\]

then every \(P_s\) extends to a matching \(M_s\) which saturates the entire
rank-\(s\) layer.

The union of the \(M_s\)'s is therefore a saturated-chain decomposition of
the complete band, containing every prescribed chain.  Deleting the
protected chains leaves an exact chain decomposition of every remaining
named target in the band.

For the hub necklace, \(a=r-d\) and \(L=O(d)\).  Since
\(d=O(\sqrt k)\) while \(k-r=\lfloor k/2\rfloor\), (0.2) holds for all
sufficiently large \(k\).  Hence the hub's \(Ld\) named targets may be
reserved integrally with no target-deletion sidecar.

## 1. Strong Boolean shadow surplus

For a family \({\cal A}\subseteq{\cal B}_s\), write

\[
 \nabla{\cal A}
 =\{T\in{\cal B}_{s+1}:\text{some }S\in{\cal A}
                                  \text{ satisfies }S\subset T\}. \tag{1.1}
\]

### Lemma 1.1 (coarse Kruskal--Katona surplus)

Let \(0\le s<r\), and let \(\varnothing\ne{\cal A}\subseteq{\cal B}_s\).

If \(k\ne2s+1\), then

\[
                         |\nabla{\cal A}|-|{\cal A}|
                         \ge k-s-1.                  \tag{1.2}
\]

If \(k=2s+1\), put \(W={k\choose s}={k\choose s+1}\).  Then

\[
 |\nabla{\cal A}|-|{\cal A}|
 \ge
 \min\{\,s,\ W-|{\cal A}|\,\}.                       \tag{1.3}
\]

#### Proof

Complementation turns \({\cal A}\) into a family of

\[
                         p=k-s
\]

element sets and turns its upper shadow into the lower shadow of that
family.  Since \(s<\lceil k/2\rceil\), we have \(p>k/2\).

We use the following numerical consequence of Kruskal--Katona:

\[
 1\le t\le {2p-2\choose p}
 \quad\Longrightarrow\quad
 \partial_p(t)-t\ge p-1.                            \tag{1.4}
\]

For completeness, write the first term of the canonical binomial expansion
as

\[
 t={x\choose p}+b,
 \qquad p\le x\le2p-3,
 \qquad 0\le b<{x\choose p-1}.
\]

The remainder shadow satisfies
\(\partial_{p-1}(b)\ge b\), because it lives on at most \(2p-3\) points,
where ranks \(p-1\) and \(p-2\) have normalized expansion at least one.
Also

\[
 {x\choose p-1}-{x\choose p}
\]

is nondecreasing for \(p\le x\le2p-2\) and starts at \(p-1\).
The Kruskal--Katona formula proves (1.4), including its endpoint.

If \(k\le2p-2\), then

\[
 |{\cal A}|\le{k\choose p}\le{2p-2\choose p},
\]

so (1.4) gives

\[
 |\nabla{\cal A}|-|{\cal A}|\ge p-1=k-s-1,
\]

which is (1.2).

The only remaining case is \(k=2p-1\), equivalently \(k=2s+1\) and
\(p=s+1\).  The sharp middle-shadow continuation of (1.4) is

\[
 \partial_p(t)-t
 \ge\min\{p-1,{2p-1\choose p}-t\}.                  \tag{1.5}
\]

It follows by applying (1.4) to the initial colex segment up to
\({2p-2\choose p}\), and to the complemented missing lower shadow above
that breakpoint.  Substituting \(p-1=s\) gives (1.3). \(\square\)

The constants are sharp: a singleton family has surplus \(k-s-1\), while
in the balanced middle case a family missing \(c\) sets can have surplus
only \(c\).

## 2. Protected matching extension at one interface

### Theorem 2.1 (every small protected matching extends)

Let \(P_s\) be any matching of \(L\) inclusion edges between
\({\cal B}_s\) and \({\cal B}_{s+1}\), where \(s<r\).  If

\[
                         L\le k-r,                    \tag{2.1}
\]

then \(P_s\) is contained in a matching which saturates all of
\({\cal B}_s\).

#### Proof

Delete the \(L\) lower and \(L\) upper endpoints of \(P_s\).  Let
\({\cal A}\) be any family of surviving lower vertices.

First suppose \(k\ne2s+1\).  By Lemma 1.1,

\[
 |\nabla{\cal A}|\ge|{\cal A}|+k-s-1.
\]

At most \(L\) of these neighbours were deleted, and

\[
                         L\le k-r\le k-s-1.
\]

Thus the residual neighborhood has size at least \(|{\cal A}|\).

Now suppose \(k=2s+1\).  Then \(s=r-1\) and \(k-r=s\).  Since
\({\cal A}\) avoids the \(L\) deleted lower vertices,

\[
                         |{\cal A}|\le W-L.
\]

Lemma 1.1 therefore gives

\[
 |\nabla{\cal A}|-|{\cal A}|
 \ge\min\{s,W-|{\cal A}|\}\ge L.
\]

Again deletion of the \(L\) protected upper endpoints leaves at least
\(|{\cal A}|\) neighbours.

Hall's theorem supplies a matching of all residual lower vertices into the
residual upper layer.  Adjoining \(P_s\) gives the required saturating
matching. \(\square\)

This theorem is stronger than the ordinary normalized-matching statement:
the protected incidences are fixed in advance.

## 3. Simultaneous protected flag extension

### Theorem 3.1 (protected Boolean flag ladder)

Fix \(a<r\).  For each \(t\in[L]\), let

\[
 S_{t,a}\subset S_{t,a+1}\subset\cdots\subset S_{t,r} \tag{3.1}
\]

be a saturated Boolean chain, and assume all displayed sets are distinct
across \(t\) at every rank.  If \(L\le k-r\), then the complete band

\[
                         \bigcup_{s=a}^r{\cal B}_s
\]

has a partition into saturated chains which contains every chain (3.1) as
a consecutive protected segment.

#### Proof

For each \(s=a,\ldots,r-1\), the prescribed edges

\[
                         P_s=\{S_{t,s}S_{t,s+1}:t\in[L]\}
\]

form a matching.  Apply Theorem 2.1 independently to obtain a matching
\(M_s\supseteq P_s\) saturating \({\cal B}_s\).

Orient every \(M_s\) upward.  Every non-top vertex has outdegree one, and
matching injectivity gives every vertex indegree at most one.  Rank strictly
increases along every edge, so the components are disjoint saturated paths.
They cover every vertex of the band and contain each prescribed chain
because all of its interface edges were protected. \(\square\)

### Corollary 3.2 (exact hub-target deletion)

Take the \(L\) literal hub chains

\[
 S_{t,r-d}\subset S_{t,r-d+1}\subset\cdots
             \subset S_{t,r-1}\subset T_t
\]

from
MATH_THEOREM_COLOURED_HUB_NECKLACE_AND_PROTECTED_OWNER_MATCHING_20260805.md.
If \(L\le k-r\), they extend to a saturated-chain decomposition of the
complete band of ranks \(r-d,\ldots,r\).

Removing those \(L\) protected paths leaves a literal nested-chain
decomposition of every nonhub target in ranks \(r-d,\ldots,r-1\), ending
at the nonhub rank-\(r\) owners.  Therefore the protected hub creates:

\[
                         \boxed{\text{zero named-target deficiency
                         throughout the high band}.} \tag{3.2}
\]

This is integral, not merely fractional.

## 4. Relation to the stationary rotor gate

Theorem 3.1 supplies exact named payload chains and exact distinct owners.
It does not choose predecessor arcs between the resulting age states.
Equivalently, it fixes the head/payload shore of the functional rainbow
cycle-cover system but not its tail permutation.

Combining this note with the hub circulation-graft theorem yields:

* the protected hub component is already a balanced literal state cycle;
* every high-band named target outside it lies in one exact residual chain;
* every high-band chain has a distinct rank-\(r\) owner; and
* the residual rank profile remains fractionally clockable.

The remaining lower-side statement is now the functional predecessor
matching for these residual chains, together with fusion to one Euler
component.  There is no longer a high-band target-deletion or
coatom--owner matching defect.

