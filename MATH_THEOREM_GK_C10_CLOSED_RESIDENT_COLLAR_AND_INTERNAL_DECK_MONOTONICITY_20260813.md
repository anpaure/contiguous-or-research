# A closed resident collar makes the rigid GK `C10` internally all-width monotone

**Date:** 2026-08-13  
**Status:** unconditional local/prospective theorem.  A common doubled
history turns the five old hinges of the explicit rigid odd-GK `C10` into
five disjoint depth-`d` resident source cycles and realizes the net decagon
as one source rethread.  The rethread fuses those five collar cycles into
one, preserves all exact immediate resources and every strict-lower
occurrence, and deletes no value from the complete cyclic owner-interval
deck of the closed collars.  Attaching the collars to the four named GK
components, protecting arbitrary exterior intervals, and zero-gap
residence remain global interfaces.

## 1. Screens and the decisive identities

Let `m>=5`.  Use the owners `A_i,B_i`, `i in Z_5`, of
`MATH_THEOREM_GK_RIGID_PALETTE_NEUTRAL_C10_FUSION_20260813.md`, with old
edges `A_iB_i` and new edges `A_iB_(i+1)` (the latter are the same
undirected edges as `B_jA_(j-1)`).  Put

\[
 H=\{m,m+1,\ldots,2m-3\},\qquad |H|=m-2.             \tag{1.1}
\]

Write

\[
 \alpha=0,\quad\beta=1,\quad z=m-1,\quad
 u=2m-2,\quad v=2m-1,\quad w=2m.                     \tag{1.2}
\]

The ten rank-three screens `X_i=A_i\setminus H` and
`Y_i=B_i\setminus H` are

\[
\begin{array}{c|c|c}
i&X_i&Y_i\\ \hline
0&zuv&uvw\\
1&\alpha zu&\alpha uv\\
2&\alpha\beta z&\alpha\beta u\\
3&\alpha zv&\alpha\beta v\\
4&zvw&\alpha vw.
\end{array}                                             \tag{1.3}
\]

All ten screens are distinct.  Direct inspection of `(1.3)` gives, for
every `i` modulo five,

\[
 X_{i-1}\cup Y_i=X_i\cup Y_i,                          \tag{1.4}
\]

\[
 X_i\cap Y_{i+1}=X_i\cap Y_i.                          \tag{1.5}
\]

Equation `(1.4)` is pointwise immediate-upper restoration at head `Y_i`;
equation `(1.5)` is pointwise immediate-lower restoration at tail `X_i`.
They are the complete active-coordinate content of the palette-neutral
decagon.

## 2. The doubled common-history collars

Fix

\[
                         1\le d\le m-3.                   \tag{2.1}
\]

Partition `H` into nonempty sets

\[
                         H=C_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}C_d,       \tag{2.2}
\]

choose `x_j in C_j`, and choose distinct fresh labels

\[
                         y_1,\ldots,y_d\in\{2,\ldots,m-2\}.
                                                               \tag{2.3}
\]

Put

\[
                         C'_j=(C_j-\{x_j\})+\{y_j\},       \tag{2.4}
\]

and write `mathcal C=(C_1,...,C_d)` and
`mathcal C'=(C'_1,...,C'_d)`.

For every port define the cyclic source word

\[
             P_i=(Y_i,\mathcal C',X_i,\mathcal C),         \tag{2.5}
\]

of length

\[
                              L=2d+2.                      \tag{2.6}
\]

The five `P_i` are the old state.  The new state is the one cyclic word

\[
                              P_0P_1P_2P_3P_4.             \tag{2.7}
\]

Equivalently, cut every old cycle after its final common-history letter and
reattach its tagged continuation `(Y_i,mathcal C',X_i,mathcal C)` in cyclic
order.  At the owner row the only changed seams are

\[
                              A_i\longrightarrow B_{i+1}.  \tag{2.8}
\]

Thus `(2.7)` is the net `C10` in one operation; the incompatible
intermediate chord `A_3B_1` never occurs.

## 3. Exact resources, topology, and residence

### Theorem 3.1 (closed resident decagon collar)

The old and new states above have the following properties.

1. Both use exactly `5(2d+2)=10d+10` source positions and have the same
   rank-`m+1` owner multiset.
2. Every owner, immediate-lower colour, and immediate-upper colour occurs
   at most once in either state, and the two states have identical complete
   multisets of all three resources.
3. The old state has five source/owner cycles; the new state has one.
4. Every nonconstant positive owner run in either state has length at least
   `d+1`.
5. There is an occurrence-, width-, and value-preserving bijection on every
   source interval whose OR has rank below `m+1`; hence every strict-lower
   derivative row and every occurrence-labelled strict-lower compiler
   assignment transports exactly.

#### Proof

Every length-`d+1` source window contains exactly one rank-three screen and
one version of every core block.  Its union therefore has rank
`(m-2)+3=m+1`.  Sliding inside `mathcal C` or `mathcal C'` performs one
fresh swap `x_j<->y_j`; crossing a screen seam performs the Johnson swap
recorded by the adjacent screens.  The changed seam is legal by `(1.4)`--
`(1.5)`.

An owner is determined by its active screen and its prefix/suffix profile
in the fresh `y` bank.  Since the ten active screens are distinct, all
owners are distinct.  The same profile distinguishes every core-swap
lower/upper colour; a screen-swap colour is distinguished by its active
intersection/union.  Equations `(1.4)`--`(1.5)` show that precisely the
five seam colours are permuted.  This proves items 1--2.

Each `P_i` is a closed source cycle before the move, whereas `(2.7)` is
their literal cyclic concatenation, proving item 3.

Every occurrence of a source coordinate belongs to `d+1` consecutive
owner windows.  Occurrences at distance at most `d+1` merge their positive
runs; occurrences farther apart give disjoint runs, each of length
`d+1`.  This proves item 4.

Finally, an interval meeting both screens surrounding a common history
contains `H` and one complete rank-three screen, hence already contains a
rank-`m+1` owner.  A strict-lower interval is therefore one-sided.  Left
intervals remain literal and right intervals move with their complete
tagged continuation.  The inverse cyclic rethread gives the inverse
occurrence map.  This proves item 5. `square`

## 4. Complete cyclic upper-deck monotonicity

Let `Deck_cyc(F)` be the set of unions of all nonempty cyclic intervals of
owner vertices over all components of a state `F`.

### Theorem 4.1 (no internal upper casualty at any width)

If `F_old` is the five-cycle state `(P_i)_i` and `F_new` is the one-cycle
state `(2.7)`, then

\[
                         \boxed{
 Deck_{\rm cyc}(F_{\rm old})
       \subseteq Deck_{\rm cyc}(F_{\rm new}).}             \tag{4.1}
\]

#### Proof

Fix an old owner interval in the component `P_i`, and let `t` be its owner
width.

If `t<=d+1`, its supporting source interval has length `d+t<L`.  If it
does not cross the cut before `Y_i`, it survives literally.  If it crosses
that cut, split it into a suffix ending in `(X_i,mathcal C)` and a prefix
beginning in `(Y_i,mathcal C')`.  In the new word, use the identical prefix
and the corresponding suffix from `P_(i-1)`.  The core/fresh coordinates
are identical.  The only possible active change is `X_i` to `X_(i-1)`, but
the prefix contains `Y_i`; equation `(1.4)` therefore makes the two unions
equal.

If `t>=d+2`, the resident port is already saturated: the old interval has
the constant value

\[
              T_i=H\cup\{y_1,\ldots,y_d\}
                    \cup X_i\cup Y_i.                      \tag{4.2}
\]

Indeed `d+2` consecutive owner windows cover all `L=2d+2` source positions
of `P_i`.  In the new word, the `L` consecutive source positions

\[
              (X_{i-1},\mathcal C,Y_i,\mathcal C')         \tag{4.3}
\]

give an owner interval of width `d+2` whose union is

\[
 H\cup\{y_1,\ldots,y_d\}\cup X_{i-1}\cup Y_i=T_i
\]

by `(1.4)`.  Hence every saturated old value also has a new witness.  These
two cases exhaust all old intervals and prove `(4.1)`. `square`

The statement is support monotonicity, not equality of graded
multiplicities.  The fused cycle also creates cross-port values.

## 5. Exact scope and consequence

The theorem solves the local problem asked of the serial two-`C6` lift:
there is one equal-support source history which is owner/q1 exact,
strict-lower exact, positively resident, and internally upper-monotone at
all widths.  The conflict `B_1 leadsto A_1` versus `B_1 leadsto A_3` was
an artifact of insisting on the intermediate chord.

The closed collar has topology `5 -> 1`, not the literal old GK return
geometry `4 -> 2`.  To perform the audited GK switch, open the five collar
cycles and graft their sockets into the four named GK components with
return involution `(0)(1 4)(2)(3)`.  The theorem does not provide that
rooted graft.  Nor does it protect intervals which enter arbitrary exterior
GK bodies, a final linear cut, typed cap routes, or minimum zero gaps.  Its
global interface is therefore:

> plant the five doubled-history port paths as a protected rooted bank,
> graft them to the named GK returns, and furnish alternative witnesses for
> exterior intervals crossing a changed seam.

The substantive gain is that no resident regeneration gadget between two
hexagons is needed.  The remaining problem is a protected host/exterior
problem, not a local common-history compatibility problem.

## 6. Independent finite audit

The script

`scratch/audit_gk_c10_closed_resident_collar_20260813.py`

was copied to and run on `h100` (no substantive Mac enumeration).  It
checks all `104` pairs

\[
                         5\le m\le17,
                  \qquad 1\le d\le m-3,
\]

including every screen identity, owner/q1 simplicity, resource equality,
positive residence, component count, and the complete set inclusion
`(4.1)`.  The frozen output is

```text
PASS_GK_C10_CLOSED_RESIDENT_COLLAR cases=104 m=5..17 d=1..m-3
max_atoms=150 owners=q1=simple residence>=d+1 topology=5_to_1
Deck_cyc(old)<=Deck_cyc(new)
```

