# Preselect, protect, complete: a Middle-Levels-to-Boolean router theorem

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical composition theorem.  It first
chooses the logical gain-to-port incidences by a small Boolean-shadow Hall
argument, protects those exact edges inside a Middle Levels factor, and
only then applies the matched-port Boolean suffix theorem.  It does not
construct the required physical occurrence lift or a globally guarded
carrier.

## 0. Setup and main inequalities

Let `ML_m` be the containment graph between

\[
 \mathcal L={ [2m-1]\choose m-1},
 \qquad
 \mathcal U={ [2m-1]\choose m},
\]

and assume `m>=2`.  Let `I` be a set of logical gains, `p=|I|`, and fix an
injection

\[
                         \iota:I\hookrightarrow\mathcal L.
\tag{0.1}
\]

Let `F_0 subseteq mathcal U` be a forbidden abstract port bank, with
`f_0=|F_0|`.

For one occurrence coordinate, every gain `i` has an eligible port menu

\[
 A_i^0\subseteq N_{ML_m}(\iota(i)),
 \qquad |A_i^0|\ge L_0.
\tag{0.2}
\]

The exact concavity-endpoint sufficient conditions used below are

\[
 \boxed{
 f_0\le L_0-1,
 \qquad
 p(L_0-1)-\binom p2-f_0\ge0.}
\tag{P0}
\]

The simpler sufficient conditions

\[
                         p\le L_0,
 \qquad                  f_0\le L_0-1
\tag{P0'}
\]

imply `(P0)`.

For two occurrence coordinates, suppose there are menus

\[
 A_i^q\subseteq N_{ML_m}(\iota(i)),
 \qquad |A_i^q|\ge L_q,
 \qquad q\in\{0,1\}.
\tag{0.3}
\]

After the phase-0 edge at gain `i` is selected, delete only that one port
from its phase-1 menu.  The second menu then has size at least `L_1-1`.
The exact concavity-endpoint sufficient conditions for the second
coordinate are

\[
 \boxed{
 f_0\le L_1-2,
 \qquad
 p(L_1-2)-\binom p2-f_0\ge0.}
\tag{P1}
\]

If `L_0=L_1=L`, the simple joint conditions

\[
                         p\le L-1,
 \qquad                  f_0\le L-2
\tag{P01'}
\]

imply both `(P0)` and `(P1)`.

Let `P_*` be any previously protected Middle Levels edge bank.  The
factor-completion conditions are

\[
 \boxed{
 \Delta(P_*\cup M_0)\le2,
 \qquad |E(P_*\cup M_0)|\le m-2}
\tag{F0}
\]

for one coordinate, and

\[
 \boxed{
 \Delta(P_*\cup M_0\cup M_1)\le2,
 \qquad |E(P_*\cup M_0\cup M_1)|\le m-2}
\tag{F01}
\]

for two.  Here `M_0,M_1` are the matchings constructed below.  A convenient
scalar sufficient bound is respectively

\[
 |E(P_*)|+p\le m-2,
 \qquad\text{or}\qquad
 |E(P_*)|+2p\le m-2,
\tag{0.4}
\]

together with the displayed degree-two condition.

## 1. Preselecting one eligible port per gain

### Lemma 1.1 (Middle Levels eligible-port Hall)

Under `(P0)`, there is a matching

\[
 \mu_0:I\longrightarrow\mathcal U\setminus F_0,
 \qquad \mu_0(i)\in A_i^0.
\tag{1.1}
\]

Equivalently,

\[
 M_0=\{\iota(i)\mu_0(i):i\in I\}
\tag{1.2}
\]

is an eligible matching of `p` literal Middle Levels incidences.

#### Proof

If `I` is empty there is nothing to prove.  For a nonempty `X subseteq I`,
put `x=|X|`.  The injected left vertices are distinct rank-`(m-1)` sets.
Two such sets have at most one common rank-`m` upper neighbour: if a common
neighbour exists it must be their union.  Thus

\[
 \left|\bigcup_{i\in X}A_i^0\right|
 \ge xL_0-\binom x2.
\tag{1.3}
\]

After deleting `F_0`, Hall follows from

\[
 q_0(x)=x(L_0-1)-\binom x2-f_0\ge0.
\tag{1.4}
\]

This quadratic is concave on `[1,p]`.  Its first endpoint is nonnegative
by `f_0<=L_0-1`, and its second endpoint is `(P0)`.  Hall proves (1.1).

Under `(P0')`, the second endpoint has the lower bound

\[
 q_0(p)\ge(p-1)\left(L_0-1-{p\over2}\right)\ge0,
\]

with `p=1` immediate and `p>=2` following from `p<=L_0`.  Hence `(P0')`
implies `(P0)`. \(\square\)

The result is deliberately **preselection**: the exact logical port edge is
chosen before the arbitrary two-factor completion is allowed to add other
edges.

## 2. Two coordinate matchings with a 2-bounded union

### Lemma 2.1 (sequential distinct-edge selection)

Assume `(P0)` and `(P1)`.  There are two matchings

\[
 \mu_q:I\longrightarrow\mathcal U\setminus F_0,
 \qquad \mu_q(i)\in A_i^q,
 \qquad q\in\{0,1\},
\tag{2.1}
\]

such that

\[
                         \mu_1(i)\ne\mu_0(i)
 \qquad(i\in I).
\tag{2.2}
\]

Consequently the simple edge union

\[
 M_{01}=M_0\cup M_1,
 \qquad
 M_q=\{\iota(i)\mu_q(i):i\in I\},
\tag{2.3}
\]

satisfies

\[
                         \Delta(M_{01})\le2,
 \qquad                  |E(M_{01})|=2p.
\tag{2.4}
\]

#### Proof

Choose `mu_0` by Lemma 1.1.  For each gain define

\[
 \widetilde A_i^1=A_i^1\setminus\{\mu_0(i)\}.
\]

Then `|widetilde A_i^1|>=L_1-1`.  Apply Lemma 1.1 with `L_1-1` in place
of `L_0`.  Its two endpoint conditions are exactly `(P1)`, so it gives a
matching `mu_1` outside `F_0`.  The deletion makes (2.2) literal.

At a left vertex `i`, the union has the two distinct selected edges.  At a
right vertex, each matching contributes at most one edge, so the union has
degree at most two.  No edge is repeated because a repeated edge would
have the same left endpoint and violate (2.2).  Therefore its maximum
degree is at most two and its size is `2p`. \(\square\)

It is essential that only `mu_0(i)` is removed from the phase-1 menu of
the **same** gain.  The phase-1 matching may use `mu_0(j)` for another gain
`j`; this creates right degree two, which the protected-factor theorem
allows.  Deleting the whole phase-0 port bank would unnecessarily lose
`p` choices per menu.

## 3. Protecting the selection and completing the owner/q1 factor

### Theorem 3.1 (preselect-then-complete factor)

Under `(F0)`, `ML_m` has a spanning two-factor `Phi` containing

\[
                         P_*\cup M_0.
\tag{3.1}
\]

Under `(F01)`, it has a spanning two-factor containing

\[
                         P_*\cup M_0\cup M_1.
\tag{3.2}
\]

#### Proof

The protected graph in either line has maximum degree at most two and at
most `m-2` edges.  Apply the small protected-factor theorem. \(\square\)

If `P_*` is empty, `(F0)` is automatic once `p<=m-2`, and `(F01)` is
automatic once `2p<=m-2`.  With an additional protected bank, maximum
degree two is a real compatibility condition: the scalar edge count alone
does not prevent a degree-three collision.

The arbitrary completion cannot change or delete the selected incidences.
It may, however, have many cycle components and need not be upper-surjective,
resident, or compatible with a compiler.  The theorem closes only the
abstract unoriented owner/q1 degree row.

## 4. Literal port lift and the suffix inequalities

The preceding sections are abstract.  To route literal claims, assume the
following additional data are fixed in one cap/guard/phase/occurrence
state.

1. Every selected abstract incidence `i--mu_q(i)` has a physical
   occurrence-labelled prefix from its allocated unit source to a physical
   port occurrence.
2. The selected prefixes are jointly capacity-disjoint, avoid the fixed
   compensation linkage and protected banks, and preserve the coordinate
   and terminal type of the selected incidence.
3. Every selected physical port carries a rank-`s` Boolean base value.  In
   one coordinate these values are pairwise distinct.  In two coordinates
   they are pairwise distinct inside each coordinate; hence their union has
   value multiplicity at most two.
4. Every selected occurrence ticket `u` has an incidence-typed one-step
   suffix menu

   \[
    N_u\subseteq\{p(u)\cup\{a\}:a\notin p(u)\},
    \qquad |N_u|\ge L_{\rm suf}.
   \tag{4.1}
   \]

5. There is a forbidden upper-value bank `F_1`, `f_1=|F_1|`.  For every
   retained upper value `Y`, one physical sink occurrence `r(Y)` is fixed,
   is legal for every selected ticket whose menu contains `Y`, and lies in
   the same materialized state.  Distinct retained values use distinct
   unit-capacity occurrences.
6. `F_1` removes every chosen sink occurrence used by a selected prefix,
   the compensation linkage, or a protected bank.  After node splitting,
   the one-step suffix arcs have no other shared unit-capacity interior.

For one coordinate, the exact concavity-endpoint suffix conditions are

\[
 \boxed{
 f_1\le L_{\rm suf}-1,
 \qquad
 p(L_{\rm suf}-1)-\binom p2-f_1\ge0.}
\tag{S0}
\]

The simpler conditions

\[
                         p\le L_{\rm suf},
 \qquad                  f_1\le L_{\rm suf}-1
\tag{S0'}
\]

imply `(S0)`.

For two coordinates, let `T` be the number of distinct Boolean base values
among the `2p` selected occurrence tickets.  The exact grouped conditions
are

\[
 \boxed{
 f_1\le L_{\rm suf}-2,
 \qquad
 T(L_{\rm suf}-2)-\binom T2-f_1\ge0.}
\tag{S01}
\]

The simpler conditions

\[
                         T\le L_{\rm suf}-2,
 \qquad                  f_1\le L_{\rm suf}-2
\tag{S01'}
\]

imply `(S01)`.

### Theorem 4.1 (literal preselect-complete-route composition)

Assume `(P0)`, `(F0)`, and `(S0)`, together with literal conditions 1--6.
Then:

1. `M_0` is contained in a spanning owner/q1 two-factor of `ML_m`; and
2. every logical gain has a pairwise vertex-disjoint literal route through
   its preselected port to a distinct typed sink, simultaneously with the
   fixed compensation linkage.

Assume instead `(P0)`, `(P1)`, `(F01)`, and `(S01)`.  Allocate one unit
source to each of the two occurrence tickets of every logical gain.  Then:

1. `M_0 union M_1` is contained in one spanning owner/q1 two-factor; and
2. all `2p` occurrence tickets have pairwise vertex-disjoint literal routes
   to distinct typed sinks in one shared-capacity Hall instance.

#### Proof

Lemmas 1.1 and 2.1 preselect the required incidence matching bank(s).
Theorem 3.1 protects them inside one spanning two-factor.  For one
coordinate, the pair-overlap Hall proof applied to the `p` selected
distinct values and `(S0)` chooses distinct upper values outside `F_1`.
For two coordinates, the selected value multiplicity is at most two, so
the bounded-multiplicity grouped Boolean Hall theorem and `(S01)` choose
distinct upper values for all `2p` tickets at once.  Literal conditions
1--6 turn those values into distinct physical sink occurrences and make
the prefix-plus-one-step concatenations capacity-disjoint and typed legal.
\(\square\)

The suffix step is deliberately performed only on the preselected ports.
No suffix rank or terminal-type coherence is required for the unused
right-shore vertices added by the two-factor completion.

## 5. Central Boolean specialization and asymptotic bank size

If the selected port values are the rank-`m` right-shore sets of `ML_m`
itself, then each has `m-1` one-coordinate upper extensions inside
`[2m-1]`.  If typing forbids at most `c` extension labels, one may take

\[
                         L_{\rm suf}=m-1-c.
\tag{5.1}
\]

Thus the simple two-coordinate suffix conditions become

\[
                         T\le m-3-c,
 \qquad                  f_1\le m-3-c.
\tag{5.2}
\]

Likewise every injected left vertex has `m` incident Middle Levels ports.
If phase typing, before deletion of the separate global bank `F_0`, leaves
at least `L` raw eligible edges in both coordinates, the simple preselection
conditions are

\[
                         p\le L-1,
 \qquad                  f_0\le L-2.
\tag{5.3}
\]

With no additional protected edges, the factor condition is

\[
                         2p\le m-2.
\tag{5.4}
\]

Consequently, if

\[
 p=O(d(m)),\qquad f_0=O(d(m)),\qquad
 T=O(d(m)),\qquad f_1=O(d(m)),
 \qquad d(m)=\Theta(\sqrt m),
\tag{5.5}
\]

and typing removes only `O(1)` incident/extension labels, then all scalar
inequalities `(P01')`, `(F01)`, and `(S01')` hold for sufficiently large
`m`.  The physical coexistence premises of Section 4 do not follow from
these asymptotics.

## 6. Exact scope and remaining physical rows

The theorem proves the following mathematical order of operations:

\[
 \boxed{
 \text{preselect eligible ports}
 \ \Longrightarrow\ 
 \text{protect those exact edges in a two-factor}
 \ \Longrightarrow\ 
 \text{route only those ports to sinks}.}
\]

It does **not** prove any of the following.

1. The logical injection `iota`, phase menus, and previously protected bank
   coexist in a carrier satisfying upper palettes and residence.
2. An abstract Middle Levels edge has the required physical occurrence,
   literal prefix, common-cap state, or transported phase-1 realization.
3. The two coordinate prefix families are jointly private or have their
   required two units of source capacity.
4. The common sink occurrences survive the background compiler,
   compensation linkage, and all structural zeros.
5. Separate coordinate choices have any nonseparable product compatibility
   beyond what is encoded in the joint suffix menus.
6. The arbitrary completing two-factor has few components, complete
   immediate-upper colours, arbitrary-width upper witnesses, or global
   residence.
7. The completing cycles admit orientations simultaneously compatible with
   every selected coordinate/role label.
8. The construction regenerates with bounded state in the next dimension.

Thus this theorem closes the **abstract preselection plus factor-extension
plus conditional suffix-Hall composition**.  It does not close the physical
common-cap/router premise and has no standalone implication
`nu(k)<=B(k)+O(1)`.

## 7. Dependencies

| role | file |
|---|---|
| protected Middle Levels factor completion | `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md` |
| matched-port and bounded-multiplicity Boolean suffix Hall | `MATH_THEOREM_MATCHED_PORT_BOOLEAN_ROUTER_REDUCTION_20260804.md` |
| exact factor-restricted router boundary | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` |
