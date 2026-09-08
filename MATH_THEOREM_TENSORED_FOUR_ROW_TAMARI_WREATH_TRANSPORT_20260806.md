# The four-row Tamari associator tensors to every wreath dimension

## Status

The port-restored four-row packet at semilength four preserves its complete
state and adjacent-union ledgers while moving one nonleaf Tamari target.
This note proves that the packet extends, without additional ledger debt, to
every semilength `r>=4`: append any common complement geodesic on fresh
coordinates to all four rows.

The result is an exact, fixed-endpoint, four-wreath trade in every dimension.
Every phase consists of shortest wreaths.  In the cyclic-window ordering
of the *complemented owner support* these are automatically biresident.
Unlike the two-row inverse-pair move, the tensor changes a nonleaf
first-return/long-window target.  Turning that local marked change into a
usable partner or slot transport still requires a compatible global
occurrence/collar embedding.

This does not assert that the four negative rows occur in one prescribed
factor, that the packet preserves every deeper interval palette, or that it
changes the number of components.

No computation or search is used beyond the already proved finite packet
identities quoted below.

## 1. The port-restored base packet

Let

\[
 \mathcal P^-=(A^-,L^-,C^-,D^-),\qquad
 \mathcal P^*=(A^*,L^*,C^*,D^*)                    \tag{1.1}
\]

be the two four-row packets in
`MATH_ATTACK_E_FOUR_ROW_TAMARI_ASSOCIATOR_20260726.md`, Sections 1 and 7.
Each row is a length-four Johnson geodesic on `[8]`,

\[
                         P_0,P_1,\ldots,P_4,          \tag{1.2}
\]

from a four-set to its complement.  The cited theorem proves:

1. the aggregate multisets of all twenty states `P_i` agree in the two
   phases;
2. the aggregate multisets of all sixteen adjacent unions
   `P_i union P_(i+1)` agree;
3. every state and every adjacent union is simple within each phase;
4. the first and last state of each named row agree between the two phases;
5. in the distinguished `L` row, the marked suffix intersection moves from
   `{8}` to `{6}`.

The fourth item is the port-restoration property and is load-bearing below.

## 2. Common complement-geodesic extension

Fix `r>=4`.  On a fresh set `E` of size `2(r-4)`, choose an `(r-4)`-set
`S_0` and a Johnson geodesic

\[
                         S_0,S_1,\ldots,S_{r-4}=E-S_0 \tag{2.1}
\]

of length `r-4`.  Equivalently, every step removes one previously
unremoved point of `S_0` and inserts one previously uninserted point of
`E-S_0`.

For a base row `P=(P_0,...,P_4)`, define its extension

\[
 \widehat P=
 (P_0+S_0,P_1+S_0,\ldots,P_4+S_0,
  P_4+S_1,\ldots,P_4+S_{r-4}).                       \tag{2.2}
\]

This is a length-`r` path of rank-`r` sets on `[8] dotcup E`.

### Lemma 2.1 (extended rows are complement geodesics)

Every row (2.2) is a simple Johnson geodesic from

\[
                         P_0+S_0
 \quad\hbox{to}\quad
                         ([8]-P_0)+(E-S_0).           \tag{2.3}
\]

#### Proof

The first four steps exchange the four points of `P_0` for the four points
of `[8]-P_0`; the remaining `r-4` steps exchange the points of `S_0` for
those of `E-S_0`.  The two coordinate banks are disjoint, no coordinate is
exchanged twice, and the endpoint is the full complement of the start.
Thus every step is Johnson and the path has the minimum possible length
`r`. \(\square\)

## 3. Exact tensor theorem

Extend all four rows of both phases using the same path (2.1).  Write the
resulting packets as `widehat P^-` and `widehat P^*`.

### Theorem 3.1 (all-dimensional four-row associator)

For every `r>=4`, the two extended packets have identical aggregate
rank-`r` state multisets and identical aggregate adjacent-union multisets.
Every state and adjacent union remains simple in each phase.  The initial
and terminal state of every named row is fixed by the trade.

Consequently their odd-graph lifts are two exact support-matched families
of four shortest wreaths on `2r+1` coordinates.  Replacing one phase by the
other preserves both central shores, uses no extra source position, and is
biresident at every deadline at most `r-1`.

#### Proof

On the first five states of each row, adjoining the common set `S_0`
preserves the two base multiset equalities and simplicity.

For a fixed named row, the base theorem gives the same terminal set `P_4`
in both phases.  Hence every tail state

\[
                         P_4+S_j\qquad(1<=j<=r-4)    \tag{3.1}
\]

is literally the same in both phases.  The junction union

\[
                         P_4+S_0+S_1                \tag{3.2}
\]

and all later tail unions

\[
                         P_4+S_j+S_{j+1}             \tag{3.3}
\]

are likewise identical row by row.  This proves both aggregate ledger
equalities.

Different named rows have different base projections in every state and
union where the base packet asserts simplicity.  On the common tail, their
fixed `P_4` projections are distinct.  Within one tail, the geodesic
states `S_j` are distinct, and its adjacent unions `S_j union S_(j+1)`
are distinct: they record respectively the unremoved suffix of `S_0` and
the inserted prefix of `E-S_0`, with the current exchanged pair at the
boundary.  Finally a base-part union has `[8]`-projection of size five,
whereas a junction or tail union has `[8]`-projection `P_4` of size four.
Thus no base/tail collision is possible, and projection to the two
coordinate banks proves simplicity after extension.

By Lemma 2.1, every row is a complement geodesic.  Inserting between
successive states `X_i,X_(i+1)` the odd-graph set

\[
 \{\infty\}\cup
       \bigl(([8]\dot\cup E)-(X_i\cup X_{i+1})\bigr) \tag{3.4}
\]

and then using the closing edge from the complementary endpoint to the
start gives a shortest `(2r+1)`-wreath.  Equality of state and
adjacent-union palettes is exactly equality of the two shores of these
lifts.

For residence, write the deletion order of the complement geodesic as
`d_1,...,d_r` and its insertion order as `e_1,...,e_r`.  The `2r+1`
rank-`r` vertices of the lift are precisely the cyclic `r`-intervals of

\[
                 d_1,d_2,\ldots,d_r,
                 e_1,e_2,\ldots,e_r,\infty.           \tag{3.4a}
\]

(the `X_i` give the intervals crossing the `d/e` boundary, and the
inserted odd vertices give the intervals crossing `infty`).  Hence their
rank-`(r+1)` complements, in cyclic-window order, have for every
coordinate one run of length `r+1` and one gap of length `r`.  This is the
owner chronology in which the wreath is biresident at every deadline at
most `r-1`.  No such run claim is made about the alternating odd-cycle
traversal itself. \(\square\)

### Corollary 3.2 (nonleaf transport survives tensoring)

In the distinguished row, the base marked intersection still changes from

\[
                         \{8\}+S_0
 \quad\hbox{to}\quad
                         \{6\}+S_0.                  \tag{3.5}
\]

The four named endpoint pairs remain fixed.  Thus the tensor is a literal
local nonleaf first-return/long-window transport with no central or
endpoint debt.  The statement does not identify this marked occurrence
with a free partner or compiler slot in an exterior factor.

#### Proof

The relevant four base states all acquire the same set `S_0`, so their
intersection acquires exactly `S_0`.  Endpoint preservation was used in
Theorem 3.1. \(\square\)

## 4. Relation to inverse-pair rigidity

A fixed-slot inverse-pair move is an involution and cannot transport three
distinct active endpoints.  Theorem 3.1 uses four rows and changes the
internal pairing of the same fixed ports.  It therefore lies outside that
two-row rigidity and is a valid candidate for changing-slot rail transport.

The exact next question is whether a component-spanning family of these
four-row tensors can be planted with common tail geodesics so that:

1. their exposed inverse-pair rails concatenate;
2. their deeper-width exterior currents telescope; and
3. the remaining component and compiler sockets have bounded deficiency.

The theorem supplies the required all-dimensional local associator.  It
does not supply that global packing.
