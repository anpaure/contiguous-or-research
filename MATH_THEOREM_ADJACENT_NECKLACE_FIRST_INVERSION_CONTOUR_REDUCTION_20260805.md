# Adjacent necklace matching reduces to a first-inversion contour recurrence

**Date:** 2026-08-05  
**Method:** binary run encoding, the first-inversion necklace tree, and
rooted-block matching transfer; no search  
**Status:** unconditional reduction.  It proves that every edge used below
is the required adjacent transfer `01 <-> 10`, and it gives an exact
one-dimensional criterion for the canonical recursive spanning graph.  It
does **not** prove that the criterion holds in every recursive call, nor
does it claim simultaneous q2-halo separation.

## 1. Weak-composition necklaces are strict adjacent-swap necklaces

For integers `q,b>=1`, put

\[
 \mathcal N_{q,b}
 =\{x=(x_0,\ldots,x_{q-1})\in\mathbb Z_{\ge0}^q:|x|=b\}/C_q.
\]

Define

\[
 \Phi(x)=0\,1^{x_0}0\,1^{x_1}\cdots0\,1^{x_{q-1}}.
 \tag{1.1}
\]

### Theorem 1.1 (strict binary encoding)

The map `Phi` induces a bijection from `N_(q,b)` to binary necklaces of
length `q+b` with exactly `q` zeroes and `b` ones.  Moreover,

\[
 x\longmapsto x-e_j+e_{j+1}\qquad(x_j>0)
 \tag{1.2}
\]

is carried to one cyclically adjacent interchange

\[
                         10\longleftrightarrow01.
 \tag{1.3}
\]

#### Proof

The zeroes in (1.1) are separators, so their intervening one-run lengths
recover `x`.  Moving the final one in the `j`-th run through its following
separator changes

\[
             0\,1^{x_j}0\,1^{x_{j+1}}
 \quad\hbox{to}\quad
             0\,1^{x_j-1}0\,1^{x_{j+1}+1},
\]

which is exactly the swap of the displayed `10` to `01`.  Both
constructions commute with cyclic rotation.  `square`

Thus the hook graph `G_(q,b)` is not merely a subgraph of a usual
fixed-density necklace flip graph: it is exactly the graph whose allowed
operation is a **neighbor swap**.  A Gray code using an arbitrary
transposition of a zero and a one does not establish an edge of
`G_(q,b)`.

## 2. A canonical adjacent-swap spanning tree

Represent every binary necklace by its lexicographically least rotation,
using `0<1`.  Its unique nondecreasing representative is

\[
                         R_{q,b}=0^q1^b.
 \tag{2.1}
\]

For every other representative `w`, let `10` be its leftmost inversion
and replace it by `01`.  Sawada--Williams' first-inversion lemma says that
the resulting word is again the lexicographically least representative of
a necklace.  For completeness, the point is that the prefix before the
chosen `10` is nondecreasing.  A rotation beginning inside that prefix is
larger after the swap, while a later rotation smaller than the new word
would already have been smaller than `w`.  Hence no rotation beats the
new word.

The swap decreases the ordinary inversion number by one.  Iteration must
therefore terminate at (2.1), and every nonroot word has one prescribed
parent.

### Theorem 2.1 (first-inversion tree)

The first-inversion edges form a spanning tree

\[
                         T_{q,b}\subseteq G_{q,b}
 \tag{2.2}
\]

rooted at the concentrated hook necklace.  Every edge of this tree is a
literal adjacent unit transfer, not a general transposition.

This is the strict part of the published first-inversion tree used by
Sawada and Williams in their fixed-content universal-cycle construction.
Their cool-lex successor order itself may use a longer substring shift;
only the parent edge (2.2) is invoked here.

## 3. The recursive calls have an adjacent root contour

Use the standard binary bubble-language recursion.  A nonempty recursive
call is denoted

\[
                         \mathcal C(s,t;\gamma),
\]

where the movable prefix has `s` zeroes and `t` ones and `gamma` is the
fixed suffix.  Its distinguished root is

\[
                         r_t=0^s1^t\gamma.
 \tag{3.1}
\]

The binary necklace recursion has a contiguous interval of valid child
calls.  For a suitable least index `j`, it is the disjoint union

\[
 \mathcal C(s,t;\gamma)
 =\{r_t\}\ \dot\cup\!
   \bigdotcup_{i=j}^{t-1}
   \mathcal C(s-1,t-i;0\,1^i\gamma).
 \tag{3.2}
\]

The distinguished root of child `i` is

\[
                         r_i
 =0^{s-1}1^{t-i}0\,1^i\gamma.
 \tag{3.3}
\]

The validity interval and partition (3.2) are the fixed-density binary
specialization of the proved necklace recurrence: once a tested child
root ceases to be a necklace, every subsequent forbidden shift is also
forbidden.

### Theorem 3.1 (root-contour path)

The roots in every call satisfy

\[
                         r_j-r_{j+1}-\cdots-r_t
 \tag{3.4}
\]

inside `G_(q,b)`.  In particular, (3.2) is a disjoint sequence of rooted
blocks whose roots are joined by a path of strict adjacent swaps.

#### Proof

For `j<=i<t`, the relevant factors are

\[
 r_i=\cdots 1\,0\,1^i\gamma,
 \qquad
 r_{i+1}=\cdots 0\,1^{i+1}\gamma.
\]

They differ by the single adjacent swap of the displayed `10`.  Both are
necklace representatives by membership in the valid recursion.  `square`

Starting from the top call `C(q,b;epsilon)` and recursively retaining the
child graphs together with all contour edges (3.4) gives a canonical
spanning subgraph

\[
                         K_{q,b}\subseteq G_{q,b}.
 \tag{3.5}
\]

It generally contains more edges than the first-inversion tree, but all
of them are still strict neighbor swaps.

## 4. Exact rooted-block matching transfer

The matching question on (3.5) is one-dimensional.

Let `B_0,...,B_l` be pairwise vertex-disjoint rooted graphs with roots
`rho_0,...,rho_l`, and add only the path edges

\[
                         \rho_0\rho_1,\ldots,
                         \rho_{\ell-1}\rho_\ell.
 \tag{4.1}
\]

Write

\[
 P_i=1\iff B_i\text{ has a perfect matching},
 \qquad
 D_i=1\iff B_i-\rho_i\text{ has a perfect matching}.
 \tag{4.2}
\]

Let `F_i` say that the union of the first `i+1` blocks and their path
edges has a perfect matching.  Put `F_(-1)=1` and `F_(-2)=0`.

### Theorem 4.1 (monomer--dimer recurrence)

For every `i>=0`,

\[
 \boxed{
 F_i=(P_i\wedge F_{i-1})
 \ \vee\ 
 (D_{i-1}\wedge D_i\wedge F_{i-2}).
 }
 \tag{4.3}
\]

For `i=0`, the second term is omitted.

#### Proof

In a perfect matching, the final root `rho_i` is either matched inside
`B_i`, which requires `P_i` and a perfect matching of the preceding
prefix, or it is matched across the final path edge to `rho_(i-1)`.  The
latter removes both roots, requiring `D_(i-1),D_i` and a perfect matching
through block `i-2`.  These cases are disjoint and exhaustive.  `square`

Apply this to (3.2), treating the terminal root `r_t` as a singleton
block, for which

\[
                         (P_t,D_t)=(0,1).
 \tag{4.4}
\]

Then:

* `F_t=1` is an exact certificate for a perfect matching of the whole
  contour call;
* `F_(t-1)=1` is an exact certificate for a matching of the call after
  deleting its distinguished root.

No general graph matching or exponentially large Tutte family remains in
this canonical spanning subgraph: only the two Boolean boundary states of
each child enter (4.3).

There is also an exact quantitative version which does not assume that
either Boolean state exists.  Put

\[
 a_i=\operatorname{def}(B_i),\qquad
 e_i=\operatorname{def}(B_i-\rho_i),
 \tag{4.5}
\]

where \(\operatorname{def}\) is the minimum number of unmatched
vertices.  Let \(C_i\) be the minimum deficiency through block \(i\)
with no root reserved for the next contour edge, and let \(U_i\) be the
minimum deficiency when \(\rho_i\) is deleted internally and reserved
for the next contour edge.

### Theorem 4.2 (two-state min-plus transfer)

\[
\begin{aligned}
 C_0&=a_0,& U_0&=e_0,\\
 U_i&=C_{i-1}+e_i,&
 C_i&=\min\{C_{i-1}+a_i,\ U_{i-1}+e_i\}.
\end{aligned}
\tag{4.6}
\]

In particular, \(C_\ell\) is the exact matching deficiency of the
path-of-blocks graph.

#### Proof

To export \(\rho_i\), the preceding prefix must already be closed and the
interior \(B_i-\rho_i\) contributes \(e_i\).  To close at \(i\), either
no final contour edge is used, giving \(C_{i-1}+a_i\), or
\(\rho_{i-1}\rho_i\) is used, closing the previously exported root and
deleting \(\rho_i\) internally, giving \(U_{i-1}+e_i\).  These are
exhaustive.  Also \(a_i\le e_i+1\), because a matching of
\(B_i-\rho_i\) may simply leave \(\rho_i\) unmatched, so abandoning an
exported final root cannot improve on \(C_\ell\).  This proves the
recurrence.

This is the requested two-boundary state: \(C\) is a closed call and
\(U\) is a call exporting one parent-facing monomer.  It identifies an
exact minimal obstruction even when a child is not parity-complete.

## 5. The parity-run form and exact socket count

Call a rooted block **parity-complete** when

\[
 P_i=1\iff |B_i|\text{ is even},
 \qquad
 D_i=1\iff |B_i|\text{ is odd}.
 \tag{5.1}
\]

The reverse implications are forced by parity; the content is existence
in the permitted parity.

### Corollary 5.1 (odd-block tiling)

If all child blocks in a call are parity-complete, then a prefix has a
perfect matching precisely when every maximal run of odd-cardinality
blocks has even length.

#### Proof

An even block is closed by its internal perfect matching.  An odd block
must expose its root, and two exposed roots can be covered precisely when
they are consecutive on (3.4).  Thus the odd positions must tile by
adjacent dimers.  This is exactly the stated run condition and is also
the specialization of (4.3).  `square`

More generally, the minimum number of exposed roots in the path
composition equals the number of odd-length maximal runs of odd blocks.
Choose alternating contour edges in every run; each even run closes and
each odd run leaves exactly one root.  No matching can do better within
the contour graph because an even block cannot expose its root while
remaining internally saturated, so distinct odd runs cannot communicate
through it.

Consequently the desired hook statement follows from the following much
narrower parity assertion.

> **Contour parity lemma.**  In every binary necklace call belonging to
> the top content `(q,b)` with odd `q`, the odd-cardinality child calls are
> consecutive-pairable, except for the one terminal parity socket chosen
> on the recursion branch leading to `0^q1^b`.

Under this lemma, induction on `s` using (4.3) gives a matching of
`K_(q,b)`, and hence of `G_(q,b)`, that is perfect when its order is even
and otherwise misses only the prescribed concentrated necklace.

The reduction is exact but the contour parity lemma is **not proved in
this note**.  A failure has an equally exact form: the first bad call has
an internal odd-length run of parity-complete odd child blocks.  That run
is the minimal canonical parity socket that must be crossed by a
noncontour adjacent swap or exported to the neighboring chip level.  This
is substantially smaller than an arbitrary Tutte obstruction.

## 6. Marked promoted ports along the contour

Every contour edge is a sibling edge

\[
                         [y+e_a]-[y+e_{a+1}]
 \tag{6.1}
\]

for a unique rooted deletion datum `(y,a)`.  The promoted-hook port is
obtained by inserting a distinguished `00` at that cut.

### Theorem 6.1 (abstract port injectivity is automatic)

Distinct edges selected by a contour matching use distinct marked
promoted ports, including when their unmarked promoted parent necklaces
coincide.

#### Proof

Deleting the distinguished `00` pair recovers `(y,a)`.  Hence equality of
marked ports would force equality of rooted deletion data and therefore
of the child edge.  `square`

Thus no additional parent-*port* matching is required after solving the
child matching.  What remains is metric rather than combinatorial
injectivity: the constant six-owner supports and their q2 halos around
different marked ports must be placed disjointly on every repeated parent
cycle.

A proof-safe sufficient condition is the following list-packing row.  Give
each selected child edge `e` a list `L_e` of aligned pairs of disjoint
physical C6 lifts at its marked port.  If the packets are ordered so that
each candidate pair in `L_e` is forbidden by at most `kappa` choices of
each earlier packet sharing a component, and

\[
                         |L_e|>\kappa d_e,
 \tag{6.2}
\]

where `d_e` is the number of earlier packets sharing one of its three
components, then greedy selection gives globally disjoint halos.  The
existing individual two-rotation theorem proves only `|L_e|>=1`; it does
not yet prove (6.2) at the high-degree promoted parents.

## 7. Literature boundary and exact remaining theorem

The cyclic fixed-density Gray codes of Wang--Savage and Ueda use one
transposition of a zero and a one, with no adjacency guarantee.  The
cool-lex necklace order uses substring shifts, amounting to one or two
transpositions.  Neither result by itself supplies edges of `G_(q,b)`.

The first-inversion parent theorem is different: it swaps a literal
neighboring `10`, and therefore is valid here.  Together with the contour
recurrence, it leaves exactly two proof obligations for the hook sector:

1. prove the contour parity lemma above, or exhibit bounded parity sockets
   and a literal adjacent-swap route exporting them between chip levels;
2. prove a simultaneous marked-port list bound such as (6.2).

No claim about non-hook PBBS sectors, q3, residence, arbitrary-width upper
witnesses, common-cap regeneration, or `nu(k)<=B(k)+O(1)` is made.
