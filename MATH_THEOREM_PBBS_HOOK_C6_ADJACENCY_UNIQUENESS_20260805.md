# A clean repeated-hook PBBS C6 can move only one adjacent angle chip

**Date:** 2026-08-05  
**Method:** deficit-three sibling-profile algebra and the hook peak-deletion
coordinates; no search  
**Status:** unconditional.  This is a sharp no-go for replacing the
adjacent-chip hook connector by a one-C6 arbitrary-transposition connector.
It does not exclude a compound excursion through promoted action levels or
a higher circuit.

## 1. Deficit-three sibling profiles

Let a clean PBBS C6 arise from a rank-`(m-1)` center with its three
forward-unmatched zeros displayed as

\[
            0_{a_0}D_0\,0_{a_1}D_1\,0_{a_2}D_2,
\tag{1.1}
\]

where the `D_i` are Dyck words.  Put

\[
 B=\beta(D_0)+\beta(D_1)+\beta(D_2),
 \qquad h_i=\operatorname{ht}(D_i).
\tag{1.2}
\]

The exact peak-pruning sibling formula says that the three middle-state
profiles are

\[
                         B+e_{h_i+1},
                         \qquad i=0,1,2.
\tag{1.3}

Suppose two shores have hook action

\[
                         (h,1^b)
\tag{1.4}

and the third has the leaf-promoted hook action

\[
                         (h+1,1^{b-1}).
\tag{1.5}

Their peak profiles are, respectively,

\[
 P=(b+1,1^{h-1}),
 \qquad
 P^+=(b,1^h).
\tag{1.6}

## 2. The two repeated blocks are forced empty

The two profiles in (1.6) have the unique common predecessor of size
`m-1`

\[
                         B=(b,1^{h-1}).
\tag{2.1}

Indeed the hook child is obtained from (2.1) by adding one unit in pruning
row one, while the promoted child is obtained by adding one unit in row
`h+1`.  Equation (1.3) therefore forces, after relabeling,

\[
                         h_0=h_1=0,
                  \qquad h_2=h.
\tag{2.2}

A Dyck word has height zero if and only if it is empty.  Hence

\[
                         D_0=D_1=\varnothing.
\tag{2.3}

The remaining block `D=D_2` has profile (2.1), equivalently action
`(h,1^(b-1))`.  Thus every clean C6 with the prescribed repeated-hook and
promoted-hook shores has, up to cyclic relabeling and reversal, the unique
shape

\[
                         0\,0\,0\,D.
\tag{2.4}

Its three normalized middle words are

\[
                         D10,
                         \qquad 10D,
                         \qquad 1D0.
\tag{2.5}

No PBBS direction, selection, or q2 hypothesis can create another block
shape: (2.2)--(2.4) follow already from the action profiles.

## 3. Exact angle consequence

Apply one simultaneous peak deletion to `D`.  It leaves the mountain
`1^(h-1)0^(h-1)`, whose `q=2h-1` insertion gaps carry the hook angle
composition `y` of mass `b-1`.

The appended peak in `D10` occupies the final gap, and the prepended peak
in `10D` occupies the initial gap.  These two gaps are consecutive after
cyclic closure.  Therefore the repeated hook angles are necessarily

\[
                         [y+e_j],
                  \qquad [y+e_{j+1}]
\tag{3.1}

for consecutive indices modulo `q`.  Conversely the literal hook-angle
connector theorem realizes every pair (3.1) with one common q2 deletion.

### Theorem 3.1 (adjacency uniqueness)

Every clean deficit-three PBBS C6 having two shores of action `(h,1^b)`
and one shore of action `(h+1,1^(b-1))` changes the hook angle by exactly
one adjacent unit transfer.  In particular, no one-C6 common-pivot
leaf-plucking gadget realizes a nonadjacent chip transfer.

## 4. Metric lower bound for aligned chains

On labeled vacancy vectors, give a unit transfer across one vacancy edge
cost one and let `dist_cyc` be the resulting earthmover metric on the
cycle.  Equation (3.1) implies that a chain of `t` repeated-hook clean C6s
can connect only pairs with

\[
                         \operatorname{dist}_{cyc}\le t.
\tag{4.1}

The quotient distance between necklace classes is the minimum of this
quantity over cyclic representatives, so (4.1) remains valid after
passing to angles.  Therefore two aligned C6s cannot simulate a hook-angle
transposition of cyclic transport distance greater than two while staying
inside the repeated-hook face.

This last clause is important.  A two-C6 excursion may delete two marked
zero slots at one promoted-parent port and reinsert them at another port;
that operation leaves the fixed hook face between the two steps.  The
theorem does not classify or rule out such a promoted-parent excursion.

## 5. Scope

The result closes one tempting shortcut: an arbitrary-transposition Gray
code on hook necklaces cannot be lifted edge-for-edge by single clean
C6s.  The physically available one-C6 graph is exactly the adjacent-chip
graph already identified in the all-angle theorem.  A proof using an
arbitrary-transposition necklace code must first construct a genuine
compound ear or a higher q2-neutral circuit.

