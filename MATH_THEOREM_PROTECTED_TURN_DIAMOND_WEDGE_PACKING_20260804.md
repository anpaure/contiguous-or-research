# Protected turn-diamond wedge packing in the Middle Levels graph

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical packing and factor-completion
theorem.  No search or computational construction is used.  It selects one
full two-incidence wedge at each of several distinct lower turns while making
all selected owners and q1 upper-turn values distinct.  It does not activate
those occurrences in a common cap, supply source or terminal multiplicity,
or solve phase/product closure.

## 0. Setup and conclusion

Let `m>=2`, and let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m}
\]

be the shores of `ML_m`.  Fix distinct lower turns

\[
                         L_1,\ldots,L_p\in\mathcal L.
\tag{0.1}
\]

A **full wedge** at `L_i` is an unordered pair

\[
                         w=(L_i;\{a,b\}),
 \qquad a,b\in[2m-1]\setminus L_i,quad a\ne b.
\tag{0.2}
\]

It protects the two incidences

\[
 L_i--(L_i\cup\{a\}),
 \qquad
 L_i--(L_i\cup\{b\}),
\tag{0.3}
\]

and declares the q1 upper-turn value

\[
                         Z(w)=L_i\cup\{a,b\}.
\tag{0.4}
\]

Let `W_i` be any menu of candidate wedges at `L_i`, and assume

\[
                         |W_i|\ge Q
 \qquad(1\le i\le p).
\tag{0.5}
\]

Two wedges conflict when they share an owner in `mathcal U` or have the
same terminal value in `binom([2m-1],m+1)`.

### Main theorem

If

\[
                         \boxed{Q>(p-1)(2m-1),}
\tag{0.6}
\]

then one can choose `w_i in W_i` so that all `2p` owners and all `p`
terminal values are pairwise distinct.  The protected incidence bank has
`2p` edges, lower degree two, and upper degree one.

Consequently, if an incumbent protected bank `P_*` is degree-compatible and

\[
                         2p+|P_*|\le m-2,
\tag{0.7}
\]

the small protected-factor theorem embeds every selected wedge and every
edge of `P_*` in one spanning two-factor of `ML_m`.

## 1. Exact pairwise conflict load

Fix a wedge

\[
 w=(L;\{a,b\}),qquad
 U_a=L\cup\{a\},\quad U_b=L\cup\{b\},\quad
 Z=L\cup\{a,b\},
\tag{1.1}
\]

and another lower turn `L' ne L`.

### Lemma 1.1 (owner conflicts)

For a fixed rank-`m` owner `U`, at most `m-1` wedges at `L'` use `U`.
Hence at most `2(m-1)` wedges at `L'` use either `U_a` or `U_b`.

#### Proof

If `L'` is not contained in `U`, no wedge at `L'` uses `U`.  If
`L' subset U`, the extension coordinate

\[
                         c=U\setminus L'
\]

is forced.  A wedge using `U` is then `{c,d}`, where `d` is any of the
other `m-1` coordinates outside `L'`.

For `U_a` and `U_b`, the two resulting wedge families are disjoint when
`L' ne L`: a wedge in their intersection would have the two owners
`U_a,U_b`, whose intersection is `L`, forcing `L'=L`.  Thus the total is
at most `2(m-1)`. \(\square\)

### Lemma 1.2 (terminal conflict)

At most one wedge at `L'` has terminal value `Z`.

#### Proof

Such a wedge can exist only when `L' subset Z`.  In that case its unordered
extension pair is forced to be

\[
                         Z\setminus L',
\]

which has size two. \(\square\)

The terminal-conflicting wedge may already be among the owner-conflicting
ones.  Without assuming that overlap, Lemmas 1.1--1.2 give the uniform
bound

\[
 \boxed{
 \#\{w'\in W(L'):w'\text{ conflicts with }w\}
 \le2(m-1)+1=2m-1.
 }
\tag{1.2}
\]

Restricting to an arbitrary menu `W_i` cannot increase this load.

## 2. Greedy wedge packing

### Theorem 2.1

Under (0.5)--(0.6), there are wedges

\[
                         w_i\in W_i\qquad(1\le i\le p)
\]

with no pairwise conflict.

#### Proof

Process the distinct lower menus in any order.  After `i-1` choices, each
chosen wedge excludes at most `2m-1` candidates in `W_i` by (1.2).  Hence
at most

\[
                         (i-1)(2m-1)
 \le(p-1)(2m-1)
\]

candidates are excluded.  Since `|W_i|>=Q` and (0.6) is strict, at least
one candidate remains.  Choose it and continue. \(\square\)

Because conflict includes every owner equality and every terminal equality,
the selected family has `2p` distinct owners and `p` distinct terminals.
Within one wedge its two owners are already distinct because `a ne b`.

## 3. Forbidden owner and terminal banks

Let

\[
 F_{\mathcal U}\subseteq\mathcal U,
 \qquad
 F_Z\subseteq{[2m-1]\choose m+1}
\tag{3.1}
\]

be fixed forbidden owner and terminal-value banks.

The cleanest formulation is to delete every wedge meeting either bank and
apply Theorem 2.1 to the retained menus.  Thus if every retained menu has
size at least `Q` satisfying (0.6), the conclusion is unchanged.

There is also an exact full-menu ledger.  For lower turn `L_i`, let

\[
 B_i=\{c\in[2m-1]\setminus L_i:
             L_i\cup\{c\}\in F_{\mathcal U}\},
 \qquad r_i=|B_i|.
\tag{3.2}
\]

After forbidden owners are removed, the available extension pairs are the
`binom(m-r_i,2)` pairs inside the remaining coordinate set.  Put

\[
 t_i=\#\{Z\in F_Z:L_i\subset Z,
                    (Z\setminus L_i)\cap B_i=\varnothing\}.
\tag{3.3}
\]

Distinct rank-`m+1` values containing `L_i` give distinct extension pairs,
so the exact retained size of the full wedge menu is

\[
                         \boxed{{m-r_i\choose2}-t_i.}
\tag{3.4}
\]

For arbitrary raw menus of size at least `Q_0`, the coarser uniform bound

\[
 |W_i^{\rm retained}|
 \ge Q_0-
 \left[r_i(m-1)-{r_i\choose2}\right]-t_i
\tag{3.5}
\]

is valid: the bracket is the exact number of full-menu pairs meeting
`B_i`, and at most `t_i` further allowed-owner pairs have forbidden
terminals.  In particular one may use the still coarser bank-size estimate

\[
 |W_i^{\rm retained}|
 \ge Q_0-(m-1)|F_{\mathcal U}|-|F_Z|.
\tag{3.6}
\]

Any of (3.4)--(3.6) may be combined with the strict greedy threshold (0.6).

## 4. Protected-factor completion

Let `M` be the union of the two incidence edges from every selected wedge.
The lower turns are distinct, so every selected lower has degree exactly
two.  Pairwise owner disjointness gives upper degree at most one.  Hence

\[
                         |E(M)|=2p,qquad \Delta(M)=2.
\tag{4.1}
\]

Assume an incumbent protected edge bank `P_*` satisfies

\[
 \Delta(P_*\cup M)\le2,
 \qquad
 |E(P_*\cup M)|\le m-2.
\tag{4.2}
\]

Then the small protected-factor theorem extends `P_* union M` to a spanning
two-factor.  The scalar condition (0.7) implies the edge-count half of (4.2)
because

\[
 |E(P_*\cup M)|\le |P_*|+2p.
\]

Degree compatibility remains essential: a pre-existing edge at a selected
lower can create degree three, and two pre-existing edges at a selected
owner can do the same.

In the completed factor, the two selected incidences exhaust the degree of
each `L_i`.  Thus they are exactly the two halfports of one q1 turn, and its
upper-turn value is the preselected `Z(w_i)`.  Those q1 terminal values are
pairwise distinct by construction.

## 5. Why the lower turns must be distinct

Two distinct wedges at the same lower turn cannot both lie in one simple
two-factor.  Each wedge specifies two incidence edges at that lower vertex.
If the wedges share one owner, their union has three distinct incident
edges; if they share none, it has four.  Sharing both owners makes the
unordered wedges identical.  Thus every pair of distinct wedges violates
the factor degree two condition.

Accordingly the theorem selects one wedge per distinct `L_i`.  Multiple
logical roles at one lower turn must be carried by the two incidences of
that one wedge, not by independently selected wedges.

## 6. Exact scope

The theorem proves a correlated protected bank with:

* one complete two-incidence turn at every selected lower occurrence;
* pairwise distinct selected owner values, hence no owner-cell alias within
  the new bank;
* pairwise distinct selected q1 upper-turn values; and
* exact eligibility for protected two-factor completion under (4.2).

It does not prove:

1. that the selected lower, owner, or q1 upper-turn occurrences are active
   and unused after a fixed compensation linkage;
2. that equal values and physical occurrences have the same capacity model;
3. two physical source units or two terminal units when both wedge
   incidences are conjunctively routed;
4. a typed suffix when the q1 upper-turn occurrence is not itself a legal
   sink;
5. componentwise phase/role compatibility, opening, upper decoration,
   residence, or common-state product closure.

For one claim choosing one wedge halfport, the turn-diamond router applies
after activation.  For two simultaneous occurrence-coordinate tickets, the
owners are already distinct, but both canonical branches meet the same
q1 terminal occurrence; terminal multiplicity or different typed sinks are
still required.

## 7. Dependencies

| role | file |
|---|---|
| small protected-factor completion | `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md` |
| factor occurrence lift and collision ledger | `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md` |
| canonical turn-diamond router | `MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md` |
