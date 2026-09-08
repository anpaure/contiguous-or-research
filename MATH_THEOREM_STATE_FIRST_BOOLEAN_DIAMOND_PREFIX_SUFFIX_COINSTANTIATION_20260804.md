# State-first Boolean diamonds coinstantiate private prefixes and one-step suffixes

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional fixed-state routing theorem and sharp reduction of
the remaining common-cap premise.  It proves that a sufficiently large bank
of already active Boolean diamonds simultaneously materializes the private
gain-to-port prefixes and the one-step typed suffix router.  It does not prove
that the current Pascal/common-cap construction exposes such a bank.

## 0. Main result

Fix one complete cap/guard/phase/occurrence state after deleting a named
compensation linkage and every protected capacity.  Let `G` be `p` gain
claims, where `p>=1`, with pairwise distinct rank-`s` Boolean source values
`X_g`.

For each gain, suppose there are at least `L_0` rank-`(s+1)` port values
`U` such that, in this same state,

1. the source occurrence of `X_g` and one unit port occurrence of `U` are
   active;
2. `X_g` is contained in `U` and the direct occurrence arc `X_g -> U` is
   active;
3. the arc has no interior capacity; and
4. the selected incidence `(g,U)` has at least `L_1` active, correctly
   typed rank-`(s+2)` sink values `Y superset U`, each joined to `U` by a
   direct no-interior arc in the same state.

Call these the **good diamonds** of `g`.  Let `F_0,F_1` be forbidden port
and sink value banks, of sizes `f_0,f_1`, containing every value whose fixed
physical occurrence is inactive, occupied, aliased to a deleted capacity, or
otherwise unavailable.  Retain one unit occurrence per eligible port value
and one unit occurrence per eligible sink value; distinct retained values
must use distinct physical capacities.  A retained sink occurrence must have
a type legal for every incidence whose displayed menu contains its value.

If

\[
 \boxed{
 f_0\le L_0-1,\qquad
 p(L_0-1)-{p\choose2}-f_0\ge0,}
\tag{P}
\]

and

\[
 \boxed{
 f_1\le L_1-1,\qquad
 p(L_1-1)-{p\choose2}-f_1\ge0,}
\tag{S}
\]

then every gain has a pairwise vertex-disjoint literal path

\[
                         X_g\longrightarrow U_g\longrightarrow Y_g
\tag{0.1}
\]

to a distinct typed sink, simultaneously with the deleted fixed linkage.

The simpler conditions

\[
 p\le\min\{L_0,L_1\},
 \qquad f_i\le L_i-1\quad(i=0,1)
\tag{0.2}
\]

imply `(P)` and `(S)`.

The point is the quantifier order.  The cap state and the complete good-
diamond menus are fixed first.  Port Hall then chooses the prefixes, and
sink Hall chooses suffixes for precisely those selected incidences.  No
post-selection activation premise remains.

## 1. Fixed-state occurrence model

For each Boolean port value `U` occurring in a good-diamond menu, fix one
physical occurrence `u(U)`.  For each retained sink value `Y`, fix one
physical occurrence `z(Y)`.  Assume the source, port, and sink occurrence
layers are disjoint unit-capacity layers.  Equal values at different
addresses may instead be retained as separate typed values, but then the
pair-overlap argument below must be applied after that occurrence refinement;
the theorem uses the simpler value-injective face.

For `g in G`, write

\[
 \mathcal U_g\subseteq
 \{U\in{[k]\choose s+1}:X_g\subset U\},
 \qquad |\mathcal U_g|\ge L_0,
\tag{1.1}
\]

for its raw good-port menu.  For every `U` in `mathcal U_g`, write

\[
 \mathcal Y_{g,U}\subseteq
 \{Y\in{[k]\choose s+2}:U\subset Y\},
 \qquad |\mathcal Y_{g,U}|\ge L_1
\tag{1.2}
\]

for its incidence-typed sink menu.  Every displayed arc

\[
 x_g\longrightarrow u(U),\qquad
 u(U)\longrightarrow z(Y)\quad(Y\in\mathcal Y_{g,U})
\tag{1.3}
\]

is already present in the one fixed residual state and has empty interior.

This is stronger than saying separately that `g` has many prefixes and
that many ports have suffixes.  The suffix menu in (1.2) is attached to
each candidate prefix incidence before either Hall selection.

## 2. Two consecutive Hall selections

### Lemma 2.1 (good-port matching)

Under `(P)`, there is an injection

\[
 \mu:G\longrightarrow {[k]\choose s+1}\setminus F_0,
 \qquad \mu(g)\in\mathcal U_g.
\tag{2.1}
\]

#### Proof

Two distinct rank-`s` source values have at most one common rank-`(s+1)`
superset: if it exists, it is their union.  Hence, for nonempty `H` contained
in `G`, with `x=|H|`,

\[
 \left|\bigcup_{g\in H}\mathcal U_g\right|
 \ge xL_0-{x\choose2}.
\]

After deleting `F_0`, Hall follows if

\[
 x(L_0-1)-{x\choose2}-f_0\ge0
 \qquad(1\le x\le p).
\]

The left side is concave in `x`; its endpoint conditions are exactly `(P)`.
\(\square\)

Put `U_g=mu(g)`.  These port values, and therefore their fixed physical
occurrences, are pairwise distinct.

### Lemma 2.2 (incidence-typed sink matching)

Under `(S)`, there is an injection

\[
 \phi:G\longrightarrow {[k]\choose s+2}\setminus F_1,
 \qquad \phi(g)\in\mathcal Y_{g,U_g}.
\tag{2.2}
\]

#### Proof

The selected `U_g` are distinct rank-`(s+1)` values.  Two such values have
at most one common rank-`(s+2)` superset.  The same pair-overlap and
concavity argument as Lemma 2.1, with `L_1,F_1`, proves Hall. \(\square\)

### Theorem 2.3 (state-first Boolean diamond router)

Under Sections 0--1 and `(P)`, `(S)`, the paths

\[
 x_g\longrightarrow u(\mu(g))
     \longrightarrow z(\phi(g))
\tag{2.3}
\]

are pairwise vertex-disjoint and typed legal.

#### Proof

The source occurrences are distinct by hypothesis.  Lemma 2.1 makes the
port occurrences distinct, and Lemma 2.2 makes the sink occurrences
distinct.  The three rank/occurrence layers are disjoint.  Every path has
no further vertex because both arcs have empty interior.  All nodes and
arcs were fixed in the same residual state before either matching, and
the forbidden banks removed every collision with the compensation linkage
and protected capacities.  Terminal legality is part of the good-diamond
definition. \(\square\)

## 3. Protected Middle-Levels factor consequence

Take `s=m-1` on a `(2m-1)`-element ground set.  The selected prefix edges

\[
 M=\{X_gU_g:g\in G\}\subseteq ML_m
\tag{3.1}
\]

form a matching.  Let `P_*` be any previously protected incidence bank.

### Corollary 3.1 (state first, then protect and complete)

If

\[
 \Delta(P_*\cup M)\le2,
 \qquad |E(P_*\cup M)|\le m-2,
\tag{3.2}
\]

then `ML_m` has a spanning two-factor containing every selected literal
prefix edge.

#### Proof

The small protected-factor theorem extends `P_* union M`.
\(\square\)

Thus an abstract two-factor need not be asked to create the prefixes.  The
prefixes should be selected from one fixed cap first and protected as exact
incidences afterward.  Theorem 2.3 already proves that the selected router
paths are mutually private inside the fixed residual state.  Corollary 3.1
does **not** assert that arbitrary additional incidences supplied by factor
completion are active in that state or avoid the reserved router capacities;
that stronger simultaneous physical lift requires the usual separate
capacity-separation premise.

## 4. Two occurrence coordinates

Suppose each logical gain has two physically distinct source occurrences
`x_g^0,x_g^1`.  For `q=0,1`, let the good-port menu of coordinate `q` have
size at least `L_0^q`.  Select coordinate zero by Lemma 2.1.  When selecting
coordinate one, forbid the `p` already selected port values as well as
`F_0`.

If

\[
 \begin{aligned}
 f_0&\le L_0^0-1,&
 p(L_0^0-1)-{p\choose2}-f_0&\ge0,\\
 f_0+p&\le L_0^1-1,&
 p(L_0^1-1)-{p\choose2}-f_0-p&\ge0,
 \end{aligned}
\tag{4.1}
\]

there are `2p` globally distinct selected port values.  If every selected
incidence has at least `L_1` good sinks and

\[
 f_1\le L_1-1,
 \qquad
 2p(L_1-1)-{2p\choose2}-f_1\ge0,
\tag{4.2}
\]

one common sink Hall instance gives distinct typed sinks to all `2p`
occurrence claims.  The resulting paths are jointly private because both
source and port layers were made globally disjoint.

The simple sufficient rows are

\[
 p\le L_0^0,qquad
 2p\le L_0^1,qquad
 2p\le L_1,qquad
 f_0\le\min(L_0^0-1,L_0^1-p-1),qquad
 f_1\le L_1-1.
\tag{4.3}
\]

This two-coordinate conclusion requires two source capacities per logical
gain.  With one shared unit source, the source shore is a cut of capacity
`p` for `2p` demands, so no routing theorem can supply both occurrences.

## 5. Asymptotic corollary and the exact remaining lemma

Suppose

\[
 p,f_0,f_1=O(d(m)),\qquad d(m)=\Theta(\sqrt m),
\]

and one fixed cap state supplies

\[
 L_0,L_1=\Theta(m)
\]

good diamond menus as in Section 1.  Then `(P)`, `(S)`, and the two-
coordinate analogues hold for all sufficiently large `m`.  The factor edge
budget also holds for `p=O(d(m))` when the rest of the protected bank leaves
the corresponding `O(m)` capacity.

Therefore the former private-prefix plus suffix-router gate reduces to one
statewise abundance statement.

> **Static good-diamond abundance lemma.**  There is one complete residual
> cap/guard/phase/occurrence state in which every exposed gain occurrence has
> `Theta(m)` active direct owner ports, every such incidence has `Theta(m)`
> active correctly typed direct sinks, the globally forbidden port and sink
> banks have size `O(d(m))`, and the selected coordinate source layers have
> the required physical multiplicity.

Once this lemma holds, Theorem 2.3 (or Section 4), followed by Corollary
3.1, supplies the private prefixes and one-step suffixes simultaneously.
No independent prefix gammoid, suffix gammoid, or post-selection activation
theorem remains on this face.

A useful sufficient input to the lemma is a bad-port bound.  If one state
gives every gain `D` direct active prefix ports and at most `b` of those
ports have fewer than `L_1` typed active sinks, then

\[
                         L_0\ge D-b.
\tag{5.1}
\]

Thus `D=Theta(m)` and `b=O(d(m))` already give the required good-port
abundance.

## 6. Sharp marginal obstruction

Separate prefix and suffix abundance does not imply the static good-diamond
lemma.  Assume `2L<=k-s` and `L<=k-s-1`.  Fix one source `X` and partition
`2L` of its rank-`(s+1)` supersets into disjoint banks `A,B`, each of size
`L`.  In one fixed occurrence state,
activate the direct prefixes `X -> U` only for `U in A`.  Give every port
in `B` at least `L` active typed one-step sinks, but give every port in `A`
no legal sink.  Then:

* the gain has `L` active private prefix candidates;
* there are `L` suffix-rich active ports;
* all displayed paths are individually literal and in one state; but
* no gain-to-sink path exists, because no port is both prefix-reachable and
  suffix-rich.

The same obstruction can be split between two cap states, making the
common-state failure even more explicit.  Consequently no theorem based
only on marginal prefix degree, marginal suffix degree, an abstract factor,
or separate cap states can prove coinstantiation.  The incidencewise
good-diamond menu in (1.1)--(1.2), or an equivalent joint relation, is
necessary.

## 7. Scope

The theorem closes the combinatorics and privacy of the prefix/suffix
composition once a single fixed state exposes static good diamonds.  It
does not prove the static good-diamond abundance lemma for the current
Pascal child, does not authenticate transported phase one, and does not
establish upper-deck, residence, component, common-cap regeneration, or
cross-ticket product constraints hidden outside the displayed unit
occurrence network.
