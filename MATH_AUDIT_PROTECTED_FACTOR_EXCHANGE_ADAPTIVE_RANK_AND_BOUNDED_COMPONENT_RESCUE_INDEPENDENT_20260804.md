# Independent audit: protected factor exchange and bounded-component rescue

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_PROTECTED_FACTOR_EXCHANGE_ADAPTIVE_RANK_AND_BOUNDED_COMPONENT_RESCUE_20260804.md`  
**Audited theorem SHA256:**
`f553f85672445da0fe3ef71c10557eaa72b3c96042b13fcca83c7be5dd6c2b1e`  
**Verdict:** **GO**, with the stated scopes.  The alternating-circuit
exchange theorem, exact adaptive graphic-rank formula, static-host
component bound, and mobile-turn packing theorem all check.  The note
correctly does not infer an additive-constant OR word from bounded factor
components alone.

No finite search, solver, or computational enumeration is used in this
audit.

## 1. Protected alternating-circuit exchange

For two two-factors `F,F'`, colour `F-F'` red and `F'-F` blue.  At every
vertex,

\[
 d_{F-F'}(v)=2-d_{F\cap F'}(v)=d_{F'-F}(v).
\]

Thus red and blue incidences can be paired locally.  The resulting
edge-pairing decomposes the symmetric difference into edge-disjoint closed
alternating trails.  A trail may revisit a vertex; this is harmless because
it then removes and adds the same number of incidences there.

Sequential toggling is valid even when distinct trails share vertices:
their edge sets are disjoint, so every untoggled red edge is still present
and every untoggled blue edge is still absent.  Degree two is retained
after every toggle.

All protected edges lie in `F cap F'` and therefore outside the symmetric
difference.  Every switched edge lies in `F union F'`, which avoids the
fixed forbidden set `Z`.  Theorem 1.1 and Corollary 1.2 follow.

The theorem uses arbitrary alternating closed trails, not a bounded local
pull catalogue.  It proves exchange-class connectivity but no monotone
component descent; the theorem records both limitations.

## 2. Adaptive graphic-rank formula

Let `N` be the number of vertices of the Middle-Levels graph.  A spanning
two-factor `F` with `c(F)` cycles has

\[
                         r_{\rm gr}(F)=N-c(F).
\]

For a component-minimizing protected completion `F_*`, taking one spanning
tree in every factor cycle gives a forest of size `N-c(F_*)`.  Its union
with `D` remains a degree-at-most-two subgraph of `F_*`, and `F_*` certifies
the exact guarded Ore--Ryser condition.  Hence

\[
                         \rho(D,Z)\ge N-c(F_*).
\]

Conversely, every forest counted by `rho(D,Z)` extends, by definition and
the exact Ore--Ryser theorem, to a protected factor `F`.  Since `F` contains
that forest,

\[
                         c(F)=N-r_{\rm gr}(F)
                              \le N-\rho(D,Z).
\]

The inequalities face in opposite directions and give equality.  This
checks Theorem 2.1 and both rows of Corollary 2.2.

Allowing `R` to overlap `D` is sound: `D union R` is a simple edge union,
while `|R|` is the rank contribution of the forest.  The assumptions
`R subset E-Z`, `D cap Z=emptyset`, and `Delta(D union R)<=2` are exactly
what the guarded extension theorem requires.

The family of extendable forests is not shown to satisfy matroid exchange;
the theorem correctly presents (0.2) as a correlated maximum, not a matroid
intersection formula.

## 3. Static protected partition deficiency

Let `q=c(H_D)`.  If a partition `Pi` meets one connected component of
`H_D` in `s` blocks, at least `s-1` edges of that component cross between
the blocks.  Summing over the `q` components gives

\[
                         |E_{H_D}(\Pi)|\ge|\Pi|-q.
\]

Therefore every partition-deficiency value is at most `q-1`.  Partitioning
into the connected components of `H_D` attains `q-1`.  Since `H` is
connected,

\[
 r_H(E(H))-r_H(E(H_D))
 =(|V(H)|-1)-(|V(H)|-q)=q-1.
\]

This verifies Lemma 3.1, including the exact rank identity.

A maximal forest of `H_D` contains one tree in each of its connected
components.  Tree compatibility contracts each such tree to one factor
component and no edge between distinct `H_D` components is used.  Thus the
result has exactly `q`, not merely at most `q`, factor components and
retains `D`.  Graphic basis extension proves the prescribed-forest clause.

Deleting one edge from a connected graph raises its component count by at
most one.  Also

\[
 |B_D|
 \le\sum_{d\in D}|\{e:d\in O_e\}|
 \le|D|\lambda.
\]

This proves Corollary 3.3 and the wedge specialization
`c<=1+2p lambda`.  A tree with `b` deleted edges attains `b+1`, so no better
bound follows from only `|B_D|`.

## 4. Mobile-turn supported wedge packing

At a fixed lower root `L`, a factor chooses exactly two upper owners and
hence one supported wedge.

Fix its terminal `(m+1)`-set `Z`.  Any other supported wedge with the same
terminal is rooted at an `(m-1)`-subset of `Z`; there are

\[
                         \binom{m+1}{m-1}=\binom{m+1}{2}
\]

possible roots, including `L`.  Each of the two chosen upper owners has
factor degree two and therefore meets at most one other lower root.  Hence
at most two additional roots can create an owner collision.  The union of
the two conflict families has size at most

\[
                         \Delta_m=\binom{m+1}{2}+2.
\]

The greedy threshold `(p-1)Delta_m` is consequently valid.  Root equality
is already included in the terminal-conflict family, so distinctness does
not need a separate unit in the bound.

Every factor edge has one lower endpoint.  Removing all lower endpoints of
a forbidden factor-edge bank `R` deletes at most `|R|` candidates, and a
retained root's two supported edges avoid `R`.  This verifies (4.3) and all
claims of Theorem 4.1.

This theorem changes the quantifier: roles choose their roots from large
menus.  It does not solve the problem with prescribed roots or prescribed
wedge values, exactly as stated.

## 5. Relation to additive-constant topology

For absolute `p` and bounded `lambda`, the theorem gives `O(1)` factor
components.  For `p=O(d)` it gives only `O(d)`, so it cannot by itself
support a dimension-independent additive constant.

More importantly, the cited overlap theorem gives the exact chronology
lower bound

\[
                         \delta_d(u,v)=d-\operatorname{ov}(u,v).
\]

Two residual component ports can therefore cost `d` even when there are
only two components.  This confirms that the theorem must not conclude
`B(k)+O(1)` from (0.6).

The stated downstream interface is accurate:

1. completed-hinge cyclic head compatibility gives zero-sidecar component
   fusion while preserving the compiled payload;
2. otherwise one needs an accepted port tour of total overlap/guard cost
   `O(1)`; and
3. immediate-upper extraction still has the bounded component-omission Hall
   cuts, which are finite in number but not automatic.

Thus the bounded-component rescue is a genuine topology advance and a
bounded-state reduction, not a completed OR-word theorem.

## 6. Final verdict

The exact adaptive replacement for fixed-host connectivity is

\[
                         \rho(D,Z)\ge N-c.
\]

The exact static-host residual is

\[
 \operatorname{ppd}(F,D,H)=c(H_D)-1,
\]

and its unconditional bounded consequence is

\[
                         c(H_D)\le1+|D|\lambda.
\]

All three formulas and their quantifiers check.  The remaining open work is
to obtain large adaptive rank for prescribed wedges, improve the
`O(d)` deletion loss when task birth is not bounded, and provide the
completed literal fusion interface.
