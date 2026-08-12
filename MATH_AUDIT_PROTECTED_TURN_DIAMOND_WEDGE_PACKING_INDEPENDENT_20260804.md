# Independent audit: protected turn-diamond wedge packing

**Date:** 2026-08-04  
**Method:** direct symbolic audit only; no search, finite enumeration, or
computational construction.

**Audited theorem:**
`MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md`, SHA256
`7727963a32eda4aad2b556ec0141dd02ca2c38e80daa563e97e36601cd3332fd`.

## 0. Verdict

PASS.  The per-wedge cross-menu conflict constant is `2m-1`, the strict
greedy threshold is correct, the forbidden-bank ledger is exact, and the
selected `2p`-edge bank satisfies the protected-factor degree conditions.
The distinct-lower hypothesis is necessary for two-factor completion.

## 1. One fixed owner against another lower menu

Fix `L' in binom([2m-1],m-1)` and an owner
`U in binom([2m-1],m)`.  A wedge at `L'` can use `U` only if `L' subset U`.
Then its first extension coordinate is forced to be

\[
                         c=U\setminus L'.
\]

There are exactly `m` coordinates outside `L'`; after `c` is fixed, its
unordered partner has `m-1` choices.  Thus one owner occurs in at most
`m-1` wedges of the other menu.

For a fixed wedge at `L`, its two owners `U_a,U_b` have intersection `L`.
If a wedge at distinct `L'` used both, the intersection of its two owners
would be both `L'` and `L`, impossible.  Therefore the two owner-conflict
families in the `L'` menu are disjoint and have total size at most

\[
                         2(m-1).
\tag{1.1}
\]

## 2. Terminal conflict and total constant

For a fixed rank-`m+1` terminal `Z`, a wedge at `L'` with terminal `Z`
exists only if `L' subset Z`.  Its unordered extension pair is then forced
to be `Z setminus L'`.  Hence there is at most one.

That one wedge can overlap an owner-conflict family, but without assuming
the overlap the union bound gives

\[
                         2(m-1)+1=2m-1.
\tag{2.1}
\]

This proves the claimed uniform conflict load against any restricted menu.
The requirement `L' ne L` is used exactly once: without it, the two
owner-conflict families meet at the original wedge.

## 3. Greedy threshold

After `i-1` wedges have been selected, their union of conflict sets removes
at most

\[
                         (i-1)(2m-1)
\]

candidates from menu `i`.  No disjointness between those conflict sets is
assumed.  Since

\[
 |W_i|\ge Q>(p-1)(2m-1)\ge(i-1)(2m-1),
\]

one candidate remains.  Induction proves the packing.  Because `Q` is an
integer, the equivalent threshold is

\[
                         Q\ge(p-1)(2m-1)+1.
\tag{3.1}
\]

Conflict avoidance makes all `2p` owner values distinct and all `p`
terminal values distinct.  Owners inside one wedge are distinct because
its extension pair has two elements.

## 4. Forbidden-bank ledger

For lower turn `L_i`, a forbidden owner containing `L_i` forbids one
extension coordinate.  If `r_i` such coordinates are forbidden, exactly

\[
 {m\choose2}-{m-r_i\choose2}
 =r_i(m-1)-{r_i\choose2}
\tag{4.1}
\]

full-menu wedges meet a forbidden owner.

After those coordinates are removed, each forbidden terminal containing
`L_i` and using two remaining coordinates deletes one unique remaining
pair.  With `t_i` denoting exactly those terminals, the full retained menu
has size

\[
                         {m-r_i\choose2}-t_i.
\tag{4.2}
\]

For an arbitrary raw sub-menu, (4.1) and `t_i` are upper bounds on how many
of its candidates the two banks can delete, yielding the theorem's coarse
lower bound.  Finally

\[
 r_i\le|F_{\mathcal U}|,
 \qquad t_i\le|F_Z|
\]

gives the global estimate

\[
 |W_i^{\rm retained}|
 \ge Q_0-(m-1)|F_{\mathcal U}|-|F_Z|.
\]

These are value-bank statements.  Whether a same-valued physical occurrence
is independently usable remains, correctly, outside the theorem.

## 5. Protected-factor completion

The selected lower vertices are distinct and each contributes its two
distinct wedge edges, so every selected lower has degree two.  Global owner
disjointness makes every selected upper degree one.  Therefore the new bank
`M` has

\[
                         |E(M)|=2p,\qquad\Delta(M)=2.
\]

If

\[
 \Delta(P_*\cup M)\le2,
 \qquad |E(P_*\cup M)|\le m-2,
\]

the small protected-factor theorem applies literally.  The scalar row

\[
                         2p+|P_*|\le m-2
\]

is sufficient for the edge count because union cardinality is at most the
sum; it does not imply the degree row, which remains an explicit premise.

At a selected lower vertex, the protected pair already has degree two, so
the completing factor cannot add another edge there.  Its q1 upper-turn
value is exactly the union of the two selected owners, namely the chosen
`Z`.  Hence the preselected terminal-value distinctness survives completion.

## 6. Necessity of distinct lower turns

Two distinct unordered extension pairs at the same lower turn share zero or
one owners.  Their edge union consequently has degree four or three at that
lower vertex.  If they share both owners, the unordered pairs are identical.
Thus two distinct full wedges at one lower vertex cannot coexist in a
two-factor.  One wedge must carry both roles there.

## 7. Exact router scope

The theorem closes a support-level packing row:

\[
 \text{distinct lower turns}
 \longmapsto
 \text{owner-disjoint, terminal-value-disjoint complete wedges}.
\]

It does not activate occurrence capacities after compensation or provide
typed terminal tails.  For one ticket choosing one halfport, the canonical
turn-diamond router applies after activation.  For two conjunctive tickets,
the owner values are already disjoint, but both canonical paths meet the
same q1 terminal occurrence at that lower turn.  Source and terminal
multiplicity, phase compatibility, and product closure remain separate.
