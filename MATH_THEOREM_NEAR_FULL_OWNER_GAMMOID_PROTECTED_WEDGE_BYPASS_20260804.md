# Near-full owner gammoids bypass protected-wedge branch activation

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional fixed-state theorem under an occurrence-faithful
owner-port lift.  It replaces direct own-terminal activation of every
selected wedge by one suffix-gammoid basis of small corank.  It does not
prove that the current Pascal/common-cap state supplies that owner-port
lift or rank bound.

## 0. Main result

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},
\]

and fix distinct required lower turns

\[
                         L_1,\ldots,L_p\in\mathcal L.
\]

For each \(i\), let

\[
 N_i=\{U\in\mathcal U:L_i\subset U\},
 \qquad |N_i|=m,
\tag{0.1}
\]

and put

\[
                         P_0=\bigcup_{i=1}^pN_i.
\tag{0.2}
\]

Fix one residual cap/guard/phase/occurrence state after deleting a named
compensation linkage and every protected capacity.  Assume:

1. every Boolean owner value \(U\in P_0\) has one completion-stable
   physical port \(p_U\);
2. whenever \(L_i\subset U\), the literal prefix from the source occurrence
   of \(L_i\) to \(p_U\) is present in this state, has empty interior, and
   is disjoint from the residual suffix network except at \(p_U\);
3. different lower sources and different owner values use different unit
   capacities;
4. linkable owner-port sets form the typed residual strict gammoid
   \(\Gamma\) on \(P_0\); and
5. every suffix linkage supplied by \(\Gamma\) ends at distinct legal typed
   sinks and is disjoint from the fixed compensation linkage.

Write

\[
                         K=|P_0|-r_\Gamma(P_0)
\tag{0.3}
\]

for the owner-port corank.

### Theorem

Assume

\[
                         1\le p\le m-1.
\tag{0.3a}
\]

If

\[
                         \boxed{K\le m-p,}
\tag{0.4}
\]

then one can select one full wedge at every \(L_i\) such that:

* all \(2p\) wedge-owner values are pairwise distinct;
* all \(p\) q1 terminal values are pairwise distinct;
* one owner of every selected wedge belongs to a common independent set of
  \(\Gamma\); and
* the selected independent owner sides give pairwise vertex-disjoint
  literal prefix-plus-suffix routes to distinct typed sinks.

If an incumbent protected bank \(P_*\) is degree-compatible and

\[
                         2p+|P_*|\le m-2,
\tag{0.5}
\]

all selected wedges and \(P_*\) lie in one spanning two-factor of \(ML_m\).

Thus the protected-wedge router does not need a direct active own-q1 branch
on every selected wedge.  A suffix-independent owner basis of corank at
most \(m-p\) is enough.

For \(p=O(d)=O(\sqrt m)\), any bounded owner-port corank satisfies (0.4)
for all sufficiently large \(m\).  More generally, the theorem tolerates
corank almost \(m\).

## 1. A gammoid basis hits every required owner star

Choose a basis \(B\) of the restriction \(\Gamma|P_0\).  Identifying ports
with their owner values,

\[
                         |P_0\setminus B|=K.
\tag{1.1}
\]

### Lemma 1.1

For every required lower turn,

\[
                         |B\cap N_i|\ge m-K.
\tag{1.2}
\]

In particular, under (0.4),

\[
                         |B\cap N_i|\ge p.
\tag{1.3}
\]

#### Proof

The star \(N_i\) has \(m\) owners, and at most all \(K\) members of
\(P_0\setminus B\) can lie in \(N_i\).  Hence

\[
 |B\cap N_i|
 =m-|N_i\setminus B|
 \ge m-K.
\]

Substitute \(K\le m-p\). \(\square\)

No symmetry or random-base distribution is used.

### Corollary 1.2 (exact local-basis form)

The conclusion of the main theorem remains valid under the strictly weaker
premise

\[
 \boxed{
 \text{there is an independent }B\subseteq P_0
 \text{ with }|B\cap N_i|\ge p\quad(1\le i\le p).
 }
\tag{1.4}
\]

The set \(B\) need not span \(P_0\).  Condition (0.4) is merely the weakest
uniform conclusion of this form forced by the single scalar corank \(K\):
every basis then satisfies (1.4).

## 2. Basis-supported wedge menus

At \(L_i\), identify the \(m\) owner extensions with the \(m\) coordinates
outside \(L_i\).  Let \(s_i=|B\cap N_i|\).  Define \(W_i(B)\) to be the
menu of all full wedges at \(L_i\) having at least one owner in \(B\).

### Lemma 2.1

\[
 |W_i(B)|
 ={m\choose2}-{m-s_i\choose2}
 =B_{s_i}(m),
\tag{2.1}
\]

where

\[
 B_q(m)={m\choose2}-{m-q\choose2}.
\]

Under (0.3a)--(0.4),

\[
                         |W_i(B)|\ge B_p(m)>B_{p-1}(m).
\tag{2.2}
\]

#### Proof

The excluded wedges are exactly the pairs whose two owners lie outside
\(B\); there are \({m-s_i\choose2}\) of them.  Lemma 1.1 gives
\(s_i\ge p\), and \(B_q(m)\) is strictly increasing for \(q<m\).
\(\square\)

Apply the purely combinatorial menu-packing proof from the exact cap-aware
protected-wedge theorem to \(W_i(B)\).  That proof uses only menu membership,
not direct own-terminal activation.  It selects wedges \(w_i\) with all
owners and all q1 terminals pairwise distinct.

## 3. Choose the basis side and route

Every selected \(w_i\in W_i(B)\) has at least one owner in \(B\).  Choose
one such owner and call its physical port \(q_i\).  Since all selected
wedge owners are pairwise distinct,

\[
                         Q=\{q_1,\ldots,q_p\}\subseteq B
\tag{3.1}
\]

has size \(p\).

### Lemma 3.1

The selected claims have pairwise vertex-disjoint literal routes to
distinct typed sinks in the fixed residual state.

#### Proof

The set \(B\) is independent in the strict gammoid \(\Gamma\), so by
heredity \(Q\subseteq B\) is independent.  Hence the ports \(q_i\) have
pairwise vertex-disjoint suffixes to distinct legal typed sinks.

Prepend the literal source-to-\(q_i\) prefixes.  Their sources and terminal
owner ports are distinct, their interiors are empty, and by hypothesis they
meet the suffix network only at the intended ports.  They also avoid the
fixed compensation linkage.  The concatenated routes are therefore
pairwise vertex-disjoint and coexist with that linkage. \(\square\)

The q1 terminal value of a selected wedge remains part of the protected
owner/q1 factor structure.  It need not be the terminal sink of the
gammoid route.  If the specification requires that exact own-q1 occurrence
as the sink, it must be encoded in \(\Gamma\)'s terminal type and path
catalogue; the theorem does not silently identify the two roles.

## 4. Factor completion

The selected wedge bank has lower degree two, upper degree one, and
\(2p\) edges.  With (0.5) and the stated degree compatibility, the small
protected-factor theorem extends it together with \(P_*\) to a spanning
two-factor.

Completion-stability is essential: the port \(p_U\), its prefix, and its
suffix-network identity must remain the same physical objects after a
factor completion containing the selected incidence \(L_iU\).  A
prospective Boolean owner name which is rebound to an incompatible
occurrence after completion does not satisfy the hypotheses.

## 5. Exact Rado bypass after a wedge bank is fixed

There is an even weaker exact condition for a particular protected wedge
bank \(D=(w_1,\ldots,w_p)\).  Let

\[
 A_i(D)=\{p_U:U\text{ is one of the two owners of }w_i\}.
\tag{5.1}
\]

The displayed prefix-plus-suffix architecture routes all claims if and
only if

\[
 \boxed{
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)\ge |X|
 \qquad(X\subseteq[p]).
 }
\tag{5.2}
\]

Its exact deficiency is

\[
 \boxed{
 \delta(D,c)=
 \max_{X\subseteq[p]}
 \left(
 |X|-
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)
 \right).
 }
\tag{5.3}
\]

These are Rado's theorem and its rank formula.  They are necessary and
sufficient for the fixed-bank architecture, while (0.4) is a transparent
preselection condition which constructs a bank satisfying them with
deficiency zero.

For additive-constant work, the bounded row

\[
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)\ge |X|-C
\tag{5.4}
\]

leaves at most \(C\) claims.  Thus a proof may bypass active-wedge
abundance entirely by selecting \(D\) jointly with the factor-restricted
Rado cuts.

## 6. The corank threshold is sharp for this implication

For \(p\le m-1\), the inequality \(K\le m-p\) is best possible if the only
information about \(\Gamma\) is its corank on \(P_0\).

### Proposition 6.1

At corank

\[
                         K=m-p+1,
\tag{6.1}
\]

one cannot guarantee that every required owner star contains \(p\)
nonloop, let alone basis, ports.

#### Proof

Choose one required turn \(L_1\) and a set

\[
                         F\subseteq N_1,\qquad |F|=m-p+1.
\]

Let \(\Gamma\) be the direct sum of loops on \(F\) and the free matroid on
\(P_0\setminus F\).  Then \(\Gamma\) is a strict gammoid, for example by
giving every nonloop a private arc to a private sink and giving every loop
no terminal path.  Its corank on \(P_0\) is \(K\), but every basis meets
\(N_1\) in exactly

\[
                         m-K=p-1
\]

owners.  Its basis-supported wedge menu at \(L_1\) has exactly
\(B_{p-1}(m)\) members, not the strict floor required by the cardinality
packing theorem. \(\square\)

This obstruction can be aligned with the attained conflict ledger.  Let
the \(p-1\) nonloop extensions at \(L_1\) be the coordinates
\(c_1,\ldots,c_{p-1}\).  The sharp construction in the exact menu-threshold
theorem supplies a valid prefix of \(p-1\) protected wedges whose conflicts
at \(L_1\) are precisely the union of those \(p-1\) coordinate stars,
namely all \(B_{p-1}(m)\) basis-supported wedges.  No basis-supported final
wedge remains.

Thus neither the corank threshold nor the strict active-menu inequality can
be improved in this sequential cardinality-only argument.

The proposition is scoped.  A different factor bank may satisfy the exact
Rado cuts (5.2) even when (0.4) fails; (0.4) is sufficient, not necessary.

## 7. Two exact ways to prove the residual corank bound

The scalar corank premise follows from a raw full owner linkage plus a
small frozen deletion bank.

### Theorem 7.1 (frozen deletion stability)

Suppose that before the compensation/protection capacities are deleted,
the complete port set \(P_0\) has a full linkage \(\mathcal R\) of pairwise
vertex-disjoint typed suffixes to distinct sinks.  Let the frozen residual
state delete a set \(F\) of physical capacity vertices and terminal slots.
Put

\[
 h_F(\mathcal R)=
 |\{R\in\mathcal R:\operatorname{cap}(R)\cap F\ne\varnothing\}|,
 \qquad f=|F|.
\]

Then

\[
 |P_0|-r_\Gamma(P_0)
 \le h_F(\mathcal R)
 \le f.
\tag{7.1}
\]

Consequently,

\[
 \boxed{
 \text{there is a raw full linkage }\mathcal R
 \text{ with }h_F(\mathcal R)\le m-p
 }
\tag{7.2}
\]

implies the main theorem.

#### Proof

Fix the displayed full linkage of \(P_0\).  Because its paths are pairwise
vertex-disjoint and have distinct sink slots, one deleted physical capacity
or sink slot meets at most one linkage path.  Delete every path meeting
\(F\).  Exactly \(h_F(\mathcal R)\) displayed paths are lost, and the
remaining paths form a residual linkage of at least
\(|P_0|-h_F(\mathcal R)\) ports.  Hence

\[
 r_\Gamma(P_0)\ge |P_0|-h_F(\mathcal R)\ge |P_0|-f.
\]

Now apply (0.4). \(\square\)

The coarser row \(f\le m-p\) is sufficient.  The count \(f\) is the number
of physical capacities and sink slots removed, not the number of logical
compensation claims.  A long frozen path can delete many capacities, so
bounded claim count alone does not imply (7.2).  Conversely, a large
deletion bank can still have small \(h_F(\mathcal R)\) if one can choose a
raw full linkage avoiding almost all of it.

### Theorem 7.2 (adaptive contraction form)

Let \(M=L(D,T)\) be the raw typed suffix gammoid, and let \(C\) be an
independent background entry set of size \(b\), disjoint from \(P_0\).
After adaptive background contraction, put

\[
                         \Gamma=(M/C)|P_0.
\]

Then

\[
 |P_0|-r_\Gamma(P_0)
 =b+|P_0|-r_M(C\cup P_0).
\tag{7.3}
\]

Therefore the joint raw rank condition

\[
 \boxed{
 r_M(C\cup P_0)\ge b+|P_0|-(m-p)
 }
\tag{7.4}
\]

implies the main theorem.

#### Proof

The contraction rank identity gives

\[
 r_\Gamma(P_0)
 =r_{M/C}(P_0)
 =r_M(C\cup P_0)-r_M(C)
 =r_M(C\cup P_0)-b.
\]

Rearrange and apply (0.4). \(\square\)

Thus the frozen model needs one raw full linkage and a deletion count,
whereas the adaptive model needs one joint background-plus-owner rank.
Neither route requires proving all owner ports survive individually.

## 8. Interface with the existing common-cap theorem

The basis-supported wedge construction needs only the **full-set** rank

\[
 r_\Gamma(P_0)\ge |P_0|-(m-p),
\tag{8.1}
\]

not the complete family of Rado inequalities on all owner subsets.
By Menger, (8.1) is equivalent to one all-cut floor:

\[
 \boxed{
 \operatorname{cap}(C)\ge |P_0|-(m-p)
 \quad\text{for every }P_0\text{-to-sink cut }C
 }
\tag{8.2}
\]

in the residual node-split suffix network.

For the frozen common-cap model this is

\[
 \min_C\gamma_C^{\,c,Q}(P_0)
 \ge |P_0|-(m-p),
\tag{8.3}
\]

where the fixed compensation routes, their capacities, and their terminal
slots have already been deleted.  For adaptive background contraction by
an independent entry set of size \(b\), it is

\[
 \min_C\gamma_C^c(B_{\rm bg}\cup P_0)-b
 \ge |P_0|-(m-p).
\tag{8.4}
\]

The literal lower-to-owner prefixes have empty interiors on the serialized
incidence face, so reserving their interiors causes no further rank loss.
If an implementation prices a boundary label or another hidden prefix
resource, that resource must instead be included in the deletion bank \(F\)
of Theorem 7.1.

The regular private-port theorem supplies the conclusion immediately when
its full-port premise

\[
                         r_\Gamma(P_0)=|P_0|
\tag{8.5}
\]

is available.  It does not prove (8.5): its hypotheses separately require
the occurrence-faithful ports, private prefixes, and simultaneous suffix
linkage.  The present theorem weakens only that rank row from zero corank to
corank at most \(m-p\); it likewise does not create the occurrence lift.

The terminal common-cap theorem already uses residual gammoid inequalities

\[
 r_{N^c}(A^c(J))\ge |J|-k
\tag{8.6}
\]

for every ticket subset.  To invoke the present theorem, instantiate one
singleton-menu ticket for every physical owner port in \(P_0\).  Then
(8.6) gives

\[
 r_\Gamma(X)\ge |X|-k
\qquad(X\subseteq P_0),
\tag{8.7}
\]

and in particular \(K\le k\).  Therefore

\[
                         \boxed{k\le m-p}
\tag{8.8}
\]

closes the protected-wedge suffix row.

This is an exact interface, not a proof of its premise.  The current
common-cap theorem states (8.6) as the all-cut hypothesis to be established;
it does not derive it for the owner-port lift.  Moreover, singleton owner
tickets must be genuine completion-stable occurrences in the same cap
state, not value-level placeholders.

## 9. A post-factor bounded-deletion alternative

The preselection basis is unnecessary when bounded residual deficiency is
acceptable and a raw full linkage is available only after the factor has
been completed.

### Theorem 9.1 (paired-port deletion bound)

Fix any protected wedge bank \(D=(w_1,\ldots,w_p)\) with all \(2p\) owner
ports distinct.  Suppose that before the frozen compensation bank is
deleted, those \(2p\) owner ports have pairwise vertex-disjoint typed
suffixes to distinct sinks.  Let \(F\) be the deleted suffix-capacity and
sink-slot bank, and let \(h\) be the number of displayed suffix paths which
meet \(F\).

Then the fixed-bank Rado deficiency after deletion is at most

\[
                         \boxed{\left\lfloor{h\over2}\right\rfloor.}
\tag{9.1}
\]

In particular \(h\le f=|F|\) gives deficiency at most
\(\lfloor f/2\rfloor\).

#### Proof

The two owner ports of claim \(i\) carry two distinct paths in the raw full
linkage.  Delete the \(h\) paths meeting \(F\).  A claim is left without a
surviving displayed suffix only when both of its paths are deleted.  Since
the owner pairs are disjoint, at most \(\lfloor h/2\rfloor\) claims have
this property.

For every other claim choose one surviving owner path.  The chosen paths
remain pairwise vertex-disjoint and end at distinct typed sinks.  Prepend
the selected factor-incidence prefixes, which have distinct sources and
owners and empty interiors.  Thus all but at most
\(\lfloor h/2\rfloor\) claims route.  Rado's deficiency formula gives
(9.1). \(\square\)

The theorem assumes that lower sources and prefix resources themselves
survive.  If a deleted common source or guard kills both alternatives of
\(c\) claims, the bound becomes

\[
                         c+\left\lfloor{h\over2}\right\rfloor,
\tag{9.2}
\]

where \(h\) counts only the remaining side-specific suffix-path losses.

This post-factor route is useful for \(B+O(1)\): a uniformly bounded
physical deletion intersection gives uniformly bounded terminal
deficiency even without completion-stable prospective owner ports.  It
does not give exact equality unless the paired casualties vanish.

## 10. Exact scope

The theorem proves:

* a factor-restricted Rado bypass for a fixed wedge bank;
* a constructive near-full-rank sufficient condition before wedge
  selection;
* tolerance of owner-port corank up to \(m-p\);
* exact compatibility with protected two-factor completion; and
* a sharp quantified obstruction at corank \(m-p+1\).

It does not prove:

1. the occurrence-faithful owner-port lift for the current Pascal child;
2. the owner-port rank or all-cut inequality (8.7);
3. that the q1 terminal occurrence is itself the typed gammoid sink;
4. two-coordinate source/terminal multiplicity or product closure;
5. topology/Hamiltonization, upper decoration, residence, or regeneration.

The remaining cap statement is now one of two alternatives:

\[
 \boxed{
 \text{completion-stable owner-port corank }\le m-p,
 }
\]

or the still weaker jointly selected factor-Rado row (5.2).

## 11. Dependencies

| role | file |
|---|---|
| exact active-menu threshold and automatic routing | MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md |
| protected wedge/factor completion | MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md |
| exact factor-restricted Rado theorem | MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md |
| residual common-cap gammoid cuts | MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md |
