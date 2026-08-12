# A clean `C6` repairs one rigid PBBS edge without changing q1, upper-q1, or q2 palettes

**Date:** 2026-08-05  
**Method:** explicit common-core set algebra and cyclic-parenthesis matching;
no computation or search  
**Status:** unconditional local gadget for every `m>=4`.  It cuts the rigid
single-soliton PBBS cycle and preserves the full local q1 intersection,
q1 union, and q2 turn multisets.  Its global acyclicity is equivalent to
one explicit three-edge component-forest test; that test is not proved for
the canonical PBBS exterior in this note.

## 1. The six owners and three q1 rows

Work on the cyclic ground set

\[
 \Gamma=\mathbb Z/(2m+1),\qquad m\ge4.
\]

Put

\[
 C=\{1,2,\ldots,m-2\},
\quad a_0=m-1,\quad a_1=m,\quad a_2=m+1,\quad c=0,
\tag{1.1}
\]

with subscripts on the `a_i` read modulo three.  Define rank-`(m-1)` rows

\[
 R_i=C+\{a_i\},                                     \tag{1.2}
\]

and rank-`m` owners

\[
 P_i=C+\{a_i,a_{i+1}\},
 \qquad
 Q_i=C+\{a_i,c\}.                                  \tag{1.3}
\]

All six owners are distinct.  The three old Johnson edges are

\[
 E_i=P_iQ_i,qquad P_i\cap Q_i=R_i,                 \tag{1.4}
\]

and the clean `C6` replacement is

\[
 E_i'=P_iQ_{i+1},qquad P_i\cap Q_{i+1}=R_{i+1}.   \tag{1.5}
\]

At the incidence level, the common incidences `R_i--Q_i` remain fixed and
the alternating six-cycle

\[
 R_0-P_0-R_1-P_1-R_2-P_2-R_0                     \tag{1.6}
\]

switches its three old `R_i--P_i` edges to the three new
`R_(i+1)--P_i` edges.

## 2. All three old rows are literal max-height PBBS occurrences

For `R_0={1,...,m-1}`, its deficit-three word has one nonempty block

\[
 1^{m-1}0^{m-1}
\]

and two empty blocks.  The unique max-height occurrence is

\[
 P_0=C+\{m-1,m\}=\{1,\ldots,m\},
 \qquad
 Q_0=C+\{m-1,0\}=\{0,\ldots,m-1\}.                \tag{2.1}
\]

This is an edge of the rigid single-soliton component.

For `R_1=C+{m}`, forward cancellation leaves the three zeros

\[
 0,\ 2m-1,\ 2m.
\]

The block after `0` occupies positions `1,...,2m-2`.  It has maximum
height `m-2`, last attained after the up-step `m`; its rightmost-maximum
down-step is `m+1`.  Hence its unique max-height PBBS edge is

\[
 R_1+\{m+1\}=P_1,qquad R_1+\{0\}=Q_1.             \tag{2.2}
\]

For `R_2=C+{m+1}`, forward cancellation again leaves
`0,2m-1,2m`.  Its unique nonempty block starts with `m-2` consecutive
up-steps; the rightmost maximum is followed by the down-step `m-1`.
Thus its max-height PBBS edge is

\[
 R_2+\{m-1\}=P_2,qquad R_2+\{0\}=Q_2.             \tag{2.3}
\]

The assumption `m>=4` ensures that the displayed interior cancellation
and strict maximum statements have the indicated form.

## 3. Exact q1 and upper-q1 preservation

The old q1 intersection rows are `R_0,R_1,R_2`.  By (1.5), the new rows
are `R_1,R_2,R_0`; hence their multiset is unchanged.

More strongly, the upper union colour is preserved edge by edge:

\[
\begin{aligned}
 P_i\cup Q_i
 &=C+\{a_i,a_{i+1},c\}\\
 &=P_i\cup Q_{i+1}.
\end{aligned}                                      \tag{3.1}
\]

Thus the switch creates no immediate lower or upper palette defect.

## 4. The exterior selected rows at the three `P_i`

At `P_i`, the other PBBS turn row is

\[
 L_i=P_i\setminus\{1\}.                            \tag{4.1}
\]

Explicitly,

\[
\begin{aligned}
 L_0&=\{2,3,\ldots,m\},\\
 L_1&=\{2,\ldots,m-2,m,m+1\},\\
 L_2&=\{2,\ldots,m-1,m+1\}.                       \tag{4.2}
\end{aligned}
\]

These are literal selected max-height rows.  For `L_0` this is another
rotation of the rigid consecutive colour.  For `L_1` and `L_2`, cut the
deficit-three word at the unmatched zero `1`; the other two unmatched
zeros are consecutive at the far end, and the intervening block is the
unique nonempty block.  Its distinguished rightmost-maximum down-step
gives the incoming PBBS edge at `P_i`.

The clean `C6` does not change any `L_i` incidence.

## 5. Exact q2 palette preservation

Put

\[
 C'=C\setminus\{1\}=\{2,\ldots,m-2\}.              \tag{5.1}
\]

Before the switch, the q2 turns at the three owners `P_i` are

\[
 R_i\cap L_i=C'+\{a_i\}.                           \tag{5.2}
\]

After the switch, the row incident with `P_i` is `R_(i+1)`, so the new
turn is

\[
 R_{i+1}\cap L_i=C'+\{a_{i+1}\}.                  \tag{5.3}
\]

Consequently the three old q2 colours

\[
 C'+a_0,\quad C'+a_1,\quad C'+a_2
\]

are merely cyclically permuted.  At every `Q_i`, the incident q1 row
remains `R_i`, so its q2 turn with the unchanged exterior row is literally
unchanged.  All other owners are untouched.

### Theorem 5.1 (clean local repair)

Replacing the three selected PBBS edges `E_i` by `E_i'`:

1. preserves every owner degree;
2. preserves the q1 intersection multiset exactly;
3. preserves every q1 union colour edge by edge;
4. preserves the q2 turn multiset exactly; and
5. removes the rigid edge `P_0Q_0` and replaces both of its incidences by
   edges leaving the single-soliton owner set.

In particular the original rigid single-soliton cycle is no longer a
component.

#### Proof

Items 1--4 are Sections 1 and 3--5.  Among the six owners, only `P_0,Q_0`
are consecutive cyclic `m`-intervals: the other four have an internal hole
or separated final point when `m>=4`.  The new neighbours of `P_0,Q_0`
are respectively `Q_1,P_2`, outside the single-soliton owner set.  Hence
the old rigid cycle is cut and spliced outward.  `square`

## 6. Exact remaining topology test

Let `F` be the selected q1 graph before the switch and put

\[
 H=F-\{E_0,E_1,E_2\}.                              \tag{6.1}
\]

Assume the components of `H` meeting the gadget are paths (isolated
vertices allowed).  Contract every such path component to one vertex and
let `J_H` be the multigraph formed by the three new links

\[
 P_iQ_{i+1}.                                       \tag{6.2}
\]

### Proposition 6.1 (component-forest criterion)

The repaired selected graph is acyclic on the union of the affected
components if and only if `J_H` is a forest.  In particular, the local
palette repair becomes a complete graphic repair whenever the six exposed
endpoint roles of (6.1) lie in components for which the three links (6.2)
have no contracted cycle.

#### Proof

Adding edges between components of a forest creates a cycle exactly when
their images create a cycle after each old tree component is contracted.
Apply this elementary criterion to `H` and the three new edges.  `square`

The present note does not prove this endpoint-component condition for the
canonical PBBS exterior.  It is now the only missing row for this explicit
gadget; all colour and q2 conditions are identities.

## 7. Scope and the `m=3` boundary

This `C6` is an ambient Johnson/incidence surgery.  Its new edges need not
be PBBS edges, which is necessary because the rigid q1 colours have no
alternate occurrence inside the PBBS factor.

The displayed construction is stated for `m>=4`.  At `m=3` some interior
blocks collapse and the exact support-minimal local repair is the separate
common-core `C8` normal form; no `m=3` conclusion is inferred here.

No residence, q3, or all-width upper claim is made.  The theorem proves
exact preservation through q2 and isolates global acyclicity as the sole
remaining local-integration gate.
