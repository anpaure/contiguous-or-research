# Global-owner-disjoint multicoordinate preselection in the Middle Levels graph

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It strengthens the
preselect--protect--complete construction by making all selected upper
owners distinct across the occurrence coordinates.  Consequently the
protected-factor occurrence lift has no owner-cell alias on the selected
bank.  The theorem does not construct a common-cap activation, distinct
source capacities, typed suffixes, product closure, or a globally decorated
carrier.

## 0. Setup

Let

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal U={ [2m-1]\choose m}
\]

be the shores of the Middle Levels containment graph.  Let `I` be a set of
`p` logical gains and fix an injection

\[
                         \iota:I\hookrightarrow\mathcal L.       \tag{0.1}
\]

For occurrence coordinate `q=0,...,c-1`, let

\[
 A_i^q\subseteq N(\iota(i)),\qquad |A_i^q|\ge L_q              \tag{0.2}
\]

be its eligible upper-owner menu.  Let `F subseteq mathcal U` be a fixed
forbidden owner bank of size `f`.

For each `q`, assume

\[
 \boxed{
 f+qp\le L_q-1,
 \qquad
 p(L_q-1)-{p\choose2}-f-qp\ge0.}                              \tag{H_q}
\]

The simpler rows

\[
                         p\le L_q,
 \qquad                  f+qp\le L_q-1                         \tag{H'_q}
\]

imply `(H_q)`.

## 1. The simultaneous owner-disjoint theorem

### Theorem 1.1

Under `(H_q)` for `q=0,...,c-1`, there are injections

\[
 \mu_q:I\longrightarrow\mathcal U\setminus F,
 \qquad \mu_q(i)\in A_i^q,                                    \tag{1.1}
\]

such that all `cp` values

\[
                         \{\mu_q(i):q<c, i\in I\}              \tag{1.2}
\]

are pairwise distinct.

#### Proof

Proceed by induction on `q`.  Suppose coordinates below `q` have been
selected and put

\[
 R_q=\{\mu_t(i):t<q, i\in I\}.
\]

The induction hypothesis gives `|R_q|=qp` and `R_q cap F=emptyset`.

For a nonempty `X subseteq I`, put `x=|X|`.  Distinct lower vertices of
`ML_m` have at most one common upper neighbour: a common rank-`m` set, if it
exists, must be their union.  Inclusion--exclusion truncated after pairs
therefore gives

\[
 \left|\bigcup_{i\in X}A_i^q\right|
 \ge xL_q-{x\choose2}.                                       \tag{1.3}
\]

After deleting `F union R_q`,

\[
 \left|\bigcup_{i\in X}(A_i^q\setminus(F\cup R_q))\right|
 \ge xL_q-{x\choose2}-f-qp.                                  \tag{1.4}
\]

Thus Hall follows if

\[
 Q_q(x):=x(L_q-1)-{x\choose2}-f-qp\ge0
 \qquad(1\le x\le p).                                      \tag{1.5}
\]

The quadratic `Q_q` is concave, so its minimum on `[1,p]` is attained at
an endpoint.  The two endpoint inequalities are exactly `(H_q)`.  Hence
there is a matching `mu_q` avoiding `F union R_q`.  This both preserves all
earlier choices and makes the new bank disjoint from them.  Induction proves
(1.1)--(1.2). \(\square\)

For `(H'_q)`, the endpoint at one is immediate.  At `p`, writing
`F_q=f+qp`, one has

\[
 p(L_q-1)-{p\choose2}-F_q
 \ge (p-1)\left(L_q-1-{p\over2}\right)\ge0,
\]

with `p=1` immediate.  Thus `(H'_q)` implies `(H_q)`.

## 2. Two-coordinate protected factor consequence

Take `c=2` and define

\[
 M_q=\{\iota(i)\mu_q(i):i\in I\},\qquad M=M_0\cup M_1.        \tag{2.1}
\]

### Corollary 2.1

The selected graph `M` has

\[
 |E(M)|=2p,qquad
 d_M(\iota(i))=2,qquad
 d_M(U)\le1\quad(U\in\mathcal U).                            \tag{2.2}
\]

In particular `Delta(M)<=2`.  If an additional protected bank `P_*`
satisfies

\[
 \Delta(P_*\cup M)\le2,qquad |E(P_*\cup M)|\le m-2,          \tag{2.3}
\]

then the small protected-factor theorem extends `P_* union M` to a spanning
two-factor of `ML_m`.

After orienting and serializing that factor, the exact occurrence-lift
ledger on `M` is

\[
 \begin{array}{c|c}
 \text{resource}&\text{selected-bank load}\\ \hline
 \text{logical lower turn }\iota(i)&2\\
 \text{upper owner cell }U&\le1\\
 \text{edge halfport}&1.
 \end{array}                                                 \tag{2.4}
\]

Hence **upper-owner aliases are absent** on the complete two-coordinate
selected bank.

#### Proof

Each `mu_q` is a matching, the two selected owners for the same `i` are
distinct, and Theorem 1.1 makes owners distinct even across different
coordinates.  This proves (2.2).  Equation (2.3) is exactly the hypothesis
of the small protected-factor theorem.  The loads in (2.4) are then the
collision identities of the protected-factor occurrence lift. \(\square\)

## 3. Asymptotic regime and exact scope

For any fixed number `c` of occurrence coordinates, if

\[
 p,f=O(d(k)),\qquad d(k)=\Theta(\sqrt k),\qquad L_q=\Theta(k), \tag{3.1}
\]

then `(H'_q)` holds for every `q<c` and all sufficiently large `k`.
Therefore owner-cell aliasing is not an asymptotic obstruction to choosing
a fixed number of protected occurrence-coordinate banks.

This theorem deliberately leaves the following literal rows open:

1. the two selected edges at `iota(i)` still share the same abstract lower
   turn; a physical construction must provide two occurrence-coordinate
   source units or an explicitly capacity-two source gadget;
2. a factor halfport must still be activated as a unit common-cap port in
   the same materialized state;
3. every activated port still needs a jointly capacity-disjoint typed
   suffix to an unused sink;
4. phase/role parity, product closure, opening, component joining, upper
   decoration, residence, and regeneration remain separate;
5. if an incumbent protected bank meets a selected upper owner, condition
   (2.3) must price that collision; global disjointness of the new banks
   alone does not protect against `P_*`.

Thus the theorem removes precisely the **new-bank upper-owner alias** from
the common-cap premise.  It does not turn an abstract factor into a
literal common-cap router.

## 4. Dependencies

| role | file |
|---|---|
| eligible-port Hall and protected completion | `MATH_THEOREM_PRESELECT_THEN_COMPLETE_MIDDLE_LEVELS_BOOLEAN_ROUTER_20260804.md` |
| exact halfport/owner collision ledger | `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md` |

