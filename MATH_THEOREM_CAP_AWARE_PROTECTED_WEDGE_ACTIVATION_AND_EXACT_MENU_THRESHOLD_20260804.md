# Cap-aware protected-wedge activation and the exact retained-menu threshold

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional packing/routing theorem in one already
materialized cap state, followed by an exact separation from the presently
proved gammoid premises.  It does not prove that the Pascal child exposes
the required active menus in one cap state.

## 0. Main conclusion

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m},
\]

and let (L_1,\ldots,L_p\in\mathcal L) be distinct lower turns.  Fix one
complete residual cap/guard/phase/occurrence state after deleting a named
compensation linkage and every protected capacity.

At (L_i), a wedge is an unordered pair

\[
 w=(L_i;\{a,b\}),\qquad a,b\notin L_i,\quad a\ne b.
\tag{0.1}
\]

It has owner values

\[
 U_a=L_i\cup\{a\},\qquad U_b=L_i\cup\{b\},
\]

and terminal value

\[
 Z(w)=L_i\cup\{a,b\}.
\]

Call (w) **active** in the fixed state if at least one of its two direct
canonical branches

\[
 x_i\longrightarrow u_i(a)\longrightarrow z_i(a,b),
 \qquad
 x_i\longrightarrow u_i(b)\longrightarrow z_i(a,b)
\tag{0.2}
\]

is present, correctly typed, and disjoint from the deleted bank.  The
source, owner, and terminal occurrence layers are unit-capacity and
disjoint.  Distinct retained owner values and distinct retained terminal
values use distinct physical capacities.  Both arcs in (0.2) have empty
interior.

Let (W_i^c) be any menu of active wedges at (L_i) in this same state.
Put

\[
 B_q(m):={m\choose2}-{m-q\choose2}
        ={q(2m-q-1)\over2}.
\tag{0.3}
\]

### Main theorem

Assume (p-1\le m-1) and

\[
 \boxed{|W_i^c|>B_{p-1}(m)\qquad(1\le i\le p).}
\tag{0.4}
\]

Then one can select (w_i\in W_i^c) so that all (2p) owner values and
all (p) terminal values are pairwise distinct.

If an incumbent protected incidence bank (P_*) is degree-compatible and

\[
                    2p+|P_*|\le m-2,
\tag{0.5}
\]

the selected wedges and (P_*) extend to a spanning two-factor of
(ML_m).  In every such completion the selected turns are pairwise
nonconsecutive.  Choosing any active side of every selected wedge gives
pairwise vertex-disjoint literal routes (0.2).

Thus protected wedge packing plus **one active branch per selected wedge**
already gives the private one-coordinate router.  No subsequent suffix
gammoid matching, monotone-side choice, or comparator transport is needed.

The threshold in (0.4) is

\[
 \boxed{
 B_{p-1}(m)
 ={(p-1)(2m-p)\over2},
 }
\tag{0.6}
\]

which sharpens the former sufficient row
((p-1)(2m-1)).  It is the exact maximum number of candidates in one full
wedge menu that a valid prefix of (p-1) protected wedges can forbid.

## 1. Exact cross-menu conflict profile

Fix

\[
 w=(L;\{a,b\}),\qquad Z=L\cup\{a,b\},
\]

and another lower turn (L'\ne L).  A wedge at (L') conflicts with (w)
when it shares one of the owner values (L+a,L+b), or has terminal value
(Z).

### Lemma 1.1 (one star or one singleton)

Exactly one of the following occurs.

1. If

   \[
   L'=L-\{x\}+\{a\}
   \quad\hbox{or}\quad
   L'=L-\{x\}+\{b\}
   \tag{1.1}
   \]

   for some (x\in L), the conflicting wedges at (L') form the complete
   coordinate star consisting of all (m-1) extension pairs containing
   (x).  The unique terminal-conflicting pair is already in this star.

2. If

   \[
                         L'=L-\{x,y\}+\{a,b\}
   \tag{1.2}
   \]

   for distinct (x,y\in L), the only conflict is the terminal pair
   ({x,y}).

3. In every other case there is no conflict.

Consequently a fixed wedge conflicts with at most

\[
                         \boxed{m-1}
\tag{1.3}
\]

wedges in any other full menu.

#### Proof

A rank-(m) owner (U) can be used by a wedge at (L') precisely when
(L'\subset U).  Since (L'\ne L), the owner (L+a) contains (L')
precisely in the first case of (1.1), and then the forced extension back to
that owner is (x).  All pairs ({x,d}), with (d) any of the other
(m-1) coordinates outside (L'), use that owner.  The owner (L+b) is
analogous.  The two alternatives in (1.1) cannot both hold for the same
(L').

A terminal conflict requires (L'\subset Z).  Since (Z) has rank
(m+1), (L') is obtained by deleting two elements from (Z).  Deleting
({a,b}) gives the excluded turn (L'=L).  Deleting one element of
({a,b}) and one (x\in L) gives (1.1); the terminal pair uses the
already shared owner.  Deleting two elements (x,y\in L) gives (1.2) and
the unique pair ({x,y}).  These exhaust the possibilities. \(\square\)

The earlier (2m-1) estimate counted the two owner stars independently.
For distinct lower turns, at most one of those owner stars can exist.

## 2. Exact union of conflicts from a protected prefix

Identify the full wedge menu at one lower turn with the edge set of
(K_m) on its (m) extension coordinates.  By Lemma 1.1, every previously
selected wedge forbids either one vertex star, one singleton edge, or
nothing.

### Lemma 2.1 (exact (q)-wedge deletion bound)

Let (q\le m-1).  The union of the conflicts caused in one full wedge menu
by any (q) previously selected wedges has size at most

\[
                         B_q(m)
 ={m\choose2}-{m-q\choose2}.
\tag{2.1}
\]

This bound is attained by a pairwise conflict-free bank of (q) protected
wedges.

#### Proof

Suppose (t) of the (q) conflict sets are vertex stars.  Their union has
size at most

\[
 {m\choose2}-{m-t\choose2}=B_t(m).
\]

The other (q-t) sets contribute at most one edge each, so the union has
size at most (B_t(m)+q-t).  Since

\[
 B_{s+1}(m)-B_s(m)=m-s-1\ge1
 \qquad(s\le q-1\le m-2),
\]

we have (B_t(m)+q-t\le B_q(m)).

For equality, fix a current turn (L_0).  Choose distinct
(x_1,\ldots,x_q\in L_0), distinct
(c_1,\ldots,c_q,e\notin L_0), and put

\[
 L_j=L_0-\{x_j\}+\{c_j\},\qquad
 w_j=(L_j;\{x_j,e\}).
\tag{2.2}
\]

The owners of (w_j) are

\[
 L_0\cup\{c_j\},
 \qquad
 L_0-\{x_j\}+\{c_j,e\},
\]

and its terminal is (L_0\cup\{c_j,e\}).  These values are pairwise
distinct over (j), so the (w_j) form a valid conflict-free protected
bank.  At (L_0), wedge (w_j) forbids exactly the star at extension
coordinate (c_j).  The union of these (q) stars has size (B_q(m)).
\(\square\)

Thus (2.1) is sharp as a one-step adversarial deletion bound.  In
particular the strict inequality in (0.4) cannot be weakened at the final
greedy step using only the cardinality of the retained menu.

## 3. Cap-aware packing and automatic private routing

### Theorem 3.1 (active-wedge packing)

More generally than (0.4), order the gains so that

\[
                         |W_i^c|>B_{i-1}(m)
                         \qquad(1\le i\le p).
\tag{3.1}
\]

Then there is a conflict-free selection (w_i\in W_i^c).

#### Proof

After (i-1) choices, Lemma 2.1 says that at most (B_{i-1}(m))
candidates in (W_i^c) conflict with the selected prefix.  Condition
(3.1) leaves an active candidate.  Choose it and continue. \(\square\)

The uniform row (0.4) implies (3.1).

### Theorem 3.2 (selected owners force nonconsecutive turns)

Complete the selected wedge bank to a spanning two-factor.  No two selected
turns are consecutive in any oriented factor component.

#### Proof

Two consecutive lower turns of a Middle-Levels factor share the intervening
rank-(m) owner.  The selected wedges have all (2p) owner values distinct,
so no two selected turns can share such an owner. \(\square\)

### Corollary 3.3 (one active branch per wedge is enough)

Under the physical hypotheses in Section 0, choose either active side of
every selected wedge.  The resulting routes are pairwise vertex-disjoint.

#### Proof

The lower source occurrences are distinct.  Every route uses one of the
globally distinct selected owner values and one of the globally distinct
terminal values.  The source, owner, and terminal layers are disjoint, and
the direct arcs have no interior.  Hence no two routes meet.

Equivalently, Theorem 3.2 makes the selected turns an independent set in
every factor cycle, so the exact selected-turn side criterion permits every
active side independently. \(\square\)

This is the promised automatic privacy statement.  It is stronger than
merely saying that each selected route exists separately: the value and
occurrence-capacity hypotheses in Section 0 make the displayed direct
routes coexist in one state.

## 4. Weak active-side counts which imply the menu bound

For (L_i), let (C_i=[2m-1]\setminus L_i), so (|C_i|=m).  Define the
directed active-side graph (D_i^c) on (C_i) by

\[
 a\longrightarrow b
 \quad\Longleftrightarrow\quad
 x_i\longrightarrow u_i(a)\longrightarrow z_i(a,b)
 \text{ is an active typed branch in the fixed state}.
\tag{4.1}
\]

Let (e_i=|E(D_i^c)|), and let (b_i) be the number of unordered pairs
({a,b}) for which both orientations occur.  Then the active wedge menu
is precisely the undirected support of (D_i^c), so

\[
                         \boxed{|W_i^c|=e_i-b_i\ge\lceil e_i/2\rceil.}
\tag{4.2}
\]

Consequently each of the following is sufficient for (0.4):

\[
 e_i-b_i>B_{p-1}(m),
\tag{4.3}
\]

or the coarser branch-count row

\[
                         e_i>2B_{p-1}(m).
\tag{4.4}
\]

If (L_{0,i}) owner coordinates each have at least (L_{1,i}) active
typed terminal partners in (4.1), then

\[
 e_i\ge L_{0,i}L_{1,i}.
\]

Hence the product condition

\[
 \boxed{
 L_{0,i}L_{1,i}>2B_{p-1}(m)
 =(p-1)(2m-p)
 }
\tag{4.5}
\]

is sufficient.

This is much weaker than requiring both (L_0) and (L_1) to be linear.
For example, if all (m) prefix owners are active, only

\[
 L_1>{(p-1)(2m-p)\over m}<2(p-1)
\tag{4.6}
\]

typed terminal partners per owner are needed.  In the intended
(p=O(d)=O(\sqrt m)) regime this is an (O(\sqrt m)), not
(\Theta(m)), terminal fan.

All counts in this section are **after** deleting forbidden capacities,
typing failures, aliases, and the fixed compensation linkage.  Marginal
counts obtained in different states cannot be multiplied.

## 5. What the present gammoid theory does and does not imply

Let (Gamma) be the typed strict gammoid of a residual suffix network on
a physical owner-port set.  A rank inequality for (Gamma) controls
simultaneous suffix linkability of already specified ports.  It does not
count the direct own-terminal incidences (4.1), and therefore does not by
itself imply (0.4), (4.3), or (4.5).

There is a valid conditional bridge.  If a set of (R_i) distinct
nonloop ports in one state each has at least (S_i) direct canonical typed
terminal partners, then (e_i\ge R_iS_i), and

\[
                         R_iS_i>2B_{p-1}(m)
\tag{5.1}
\]

implies active-wedge packing.  The rank premise can certify the existence
of (R_i) nonloop ports; the direct fan premise remains additional.

### Proposition 5.1 (sharp common-owner star obstruction)

Individual active branches, even (m-1) active wedges per source, do not
imply a joint selection.

#### Proof

Fix one rank-(m) owner (U) and distinct (x_1,\ldots,x_p\in U).  Put

\[
                         L_i=U-\{x_i\}.
\]

For every (b\notin U), activate only the branch

\[
 L_i\longrightarrow U\longrightarrow U\cup\{b\}.
\tag{5.2}
\]

At source (L_i), the active wedge menu is

\[
 W_i^c=\{\{x_i,b\}:b\notin U\},
 \qquad |W_i^c|=m-1.
\]

Every selected branch from every menu uses the same unit owner (U).
Thus no two gains can be routed and no two selected wedges can belong to a
protected bank with pairwise distinct owners.  For (p=2), the exact
threshold is (B_1(m)=m-1), so this also proves the sharpness of the strict
inequality in (0.4).

The suffix gammoid of the displayed physical port bank has rank one, and
the factor-restricted Rado cut detects the obstruction exactly. \(\square\)

There is also no converse implication from large gammoid rank to the menu
bound.  A full-rank set of (m) ports may have only one private direct
typed terminal per port, hence at most (m) active wedges.  For (p\ge3),
(m\le B_{p-1}(m)) for all (m\ge3).  Gammoid independence would route a
suitably chosen port bank, but it does not manufacture the additional
partner incidence needed to protect a full factor wedge.

Therefore the current cap/gammoid results do not prove the active-wedge
menu hypothesis.  They offer two alternative exits:

1. prove the statewise directed branch support (4.3), or the weaker product
   certificate (4.5), before factor completion; or
2. bypass wedge abundance by proving the exact factor-restricted Rado cuts
   for a jointly selected factor-compatible port bank.

The first is the narrower target for the protected-wedge architecture.

## 6. Completion-stability and exact scope

The active menus in this theorem must be **completion-stable**: either the
factor and cap state are chosen jointly, or every candidate branch carries
a certificate that survives any protected-factor completion containing its
two wedge incidences.  A prospective Boolean branch that disappears after
the factor occurrence addresses or cap flags are fixed is not a member of
(W_i^c).

The theorem proves:

* the exact cross-menu conflict profile (m-1);
* the exact (q)-prefix deletion number (B_q(m));
* a sharper cap-aware active-menu packing theorem;
* automatic private routing from one active branch per selected wedge;
* the product fan condition (4.5); and
* a sharp obstruction showing that individual activation and present
  gammoid marginals do not supply the missing menu theorem.

It does not prove:

1. that one Pascal/common-cap state exposes (4.3) or (4.5);
2. completion-stability of the current prospective wedge catalogue;
3. two physical source units or two terminal units for a two-coordinate
   claim;
4. topology/Hamiltonization, upper decoration, residence, or regeneration;
5. transported phase-one authenticity or common product closure.

## 7. Dependencies

| role | file |
|---|---|
| protected wedge packing and factor completion | `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md` |
| exact fixed-factor turn collision law | `MATH_THEOREM_FACTOR_STATE_STATIC_DIAMOND_NO_GO_AND_SPARSE_TURN_ACTIVATION_20260804.md` |
| rich-state direct Boolean diamond router | `MATH_THEOREM_STATE_FIRST_BOOLEAN_DIAMOND_PREFIX_SUFFIX_COINSTANTIATION_20260804.md` |
| private factor router and strict-gammoid premise | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` |
| factor-restricted Rado cuts | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` |
