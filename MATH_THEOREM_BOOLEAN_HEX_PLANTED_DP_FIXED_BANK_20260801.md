# A bounded ternary-hex bank can be planted before the Delcourt--Postle forest

Date: 2026-08-01  
Status: exact fixed-bank extension theorem for the valid ordered-diamond
`N-o(N)` Delcourt--Postle construction.  It installs any fixed typed-resource
disjoint target bank in graphically safe gain packets.  It does **not**
prescribe the `o(N)` leave of the bulk matching, and it does not absorb the
bulk's unbounded number of long cycles.

## 0. Statement and consequence

Let

\[
 {cal L}={ [2m]\choose m-1},\qquad
 {cal U}={ [2m]\choose m+1},\qquad
 {cal M}={ [2m]\choose m},\qquad
 N=|{cal L}|,
\]

and let `H_m` be the ordered-diamond four-graph whose atoms are

\[
       e(L;a,b)=(L,L+a+b,(L+a)_{\rm tail},(L+b)_{\rm head}).
\tag{0.1}
\]

The tail and head copies of `M` are distinct resource classes, although
their physical projections are the same middle vertices.

### Theorem 0.1 (planted fixed bank)

Let `e_1,...,e_H` be ordered diamonds which are pairwise disjoint in all
four **typed** resource classes.  If

\[
                         m-1>12H-10,                 \tag{0.2}
\]

then one can choose one ternary-hex packet through each `e_i` so that:

1. the complete three-atom phases of the packets are pairwise
   four-resource disjoint;
2. the four auxiliary physical middle vertices of distinct packets are
   all different and avoid every physical endpoint of every `e_i`;
3. the union `B^-` of the two-atom off phases is a four-resource matching
   whose physical projection is `2H` isolated edges; and
4. replacing every off phase by its three-atom new phase gives a
   four-resource matching `B^+` of size `3H` whose physical projection is a
   linear forest.

Fix any cycle cutoff `g`.  For all sufficiently large `m`, there is in
addition a four-resource matching `F` in the remaining host such that

\[
        F\cup B^-\quad\hbox{and}\quad F\cup B^+
\]

are physical linear forests, and

\[
 |F|\ge N-ND^{-\alpha_g}-{N\over g+1}-18H,
 \qquad D=m(m+1),                                  \tag{0.3}
\]

for the positive constant `alpha_g` in the valid Delcourt--Postle
short-cycle colouring theorem.

Consequently a bounded regenerative target bank may be fixed **before**
the asymptotic bulk is selected.  The bulk can later be toggled from
`B^-` to `B^+`, gaining all `H` target tuples, without a new resource or
graphic check.

The same proof permits `H=H(m)` subject to (0.2).  Since then `H=O(m)=o(N)`,
a slow diagonal choice `g=g(m)->infinity` still gives an `N-o(N)` forest.

## 1. Packing the packet menus

Orient one target atom as

\[
 e=(L,U,E,F),\qquad E=L+d,\quad F=L+a,\quad U=L+a+d.
\tag{1.1}
\]

For every `b in L` and `c notin U`, the ternary-hex construction in
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`
has four auxiliary physical middle vertices

\[
\begin{array}{ll}
 A=U-b,                 &B=L-b+a+c,\\
 C=L-b+c+d,             &D=L+c,
\end{array}                                                \tag{1.2}
\]

two non-target lower colours

\[
                         L-b+a,\qquad L-b+c,           \tag{1.3}
\]

and two non-target upper colours

\[
                         U-b+c,\qquad U-a+c.           \tag{1.4}
\]

There are `(m-1)^2` choices `(b,c)`.

### Lemma 1.1 (one forbidden unit has linear menu load)

In the menu of a fixed target, each fixed non-target lower or upper colour
occurs in at most `m-1` options.  Each fixed physical middle vertex occurs
among `A,B,C,D` in at most `m-1` options.

#### Proof

The outer-colour assertion is the menu-load computation in the ternary-hex
theorem.  For the physical assertion, membership in the two distinguished
coordinates `a,d` identifies the role in (1.2): `A` contains both, `B`
contains only `a`, `C` contains only `d`, and `D` contains neither.  In the
`A` role the vertex determines `b` and leaves `c` free; in the `D` role it
determines `c` and leaves `b` free.  The `B` and `C` roles determine both.
Thus the maximum load is `m-1`.  `square`

### Lemma 1.2 (simultaneous clean menu selection)

Under (0.2), options can be chosen so that all non-target lower and upper
colours are distinct, all auxiliary physical vertices are distinct, and
no auxiliary physical vertex is a physical endpoint of a target atom.

#### Proof

Choose the options greedily.  In one current menu, forbid:

* the lower and upper resources of the other targets: at most `2(H-1)`
  fixed outer units;
* every target physical endpoint: at most `2H` fixed physical units; and
* the four non-target outer units and four auxiliary physical units of
  each previously chosen option: at most `8(i-1)` fixed units before the
  `i`th choice.

By Lemma 1.1, each unit deletes at most `m-1` of the `(m-1)^2` options.
Before the last choice, the number deleted is at most

\[
 [,2(H-1)+2H+8(H-1),](m-1)
       =(12H-10)(m-1)<(m-1)^2.                       \tag{1.5}
\]

An option remains.  `square`

The typed-resource disjointness in Theorem 0.1 now follows immediately.
The target tuples were typed-resource disjoint; (1.3)--(1.4) avoid every
other target outer resource; and auxiliary vertices are disjoint even
after forgetting their tail/head roles.

## 2. Both packet phases are forests

For packet `i`, write its six physical vertices as

\[
                    A_i,B_i,C_i,D_i,E_i,F_i,
\]

where `E_i,F_i` are the fixed target tail and head.  Its off and new
physical phases are

\[
 \partial O_i^- =\{A_iB_i,C_iD_i\},\qquad
 \partial N_i   =\{A_iF_i,C_iB_i,E_iD_i\}.           \tag{2.1}
\]

The off union is visibly a matching of isolated physical edges.  In the
new union, all `A_i,B_i,C_i,D_i` are private.  Typed target disjointness
implies that a physical middle vertex can occur as at most one `E_i` and at
most one `F_j`.  Therefore every component involving target endpoints is
one of

\[
 A_i-F_i,\qquad E_j-D_j,\qquad A_i-F_i(=E_j)-D_j,     \tag{2.2}
\]

and every `C_iB_i` is an isolated edge.  Hence the new union is a linear
forest.  This proves assertions 1--4 of Theorem 0.1.

Notice why typed disjointness is enough: equality `E_j=F_i` across the two
roles merely creates the length-two path in (2.2); it cannot create a
cycle because both auxiliary neighbours are private.

## 3. Delete a closed packet support and run Delcourt--Postle

Let `Z` consist of

* the three lower and three upper colours of every complete packet phase;
  and
* **both** the tail and head copy of each of its six physical middle
  vertices.

Then

\[
                              |Z|\le18H.              \tag{3.1}
\]

Every atom of `H_m-Z` is four-resource disjoint from both packet phases and
is physically vertex-disjoint from their projections.

The full host has `ND` atoms, maximum degree `D=m(m+1)`, pair-codegree at
most `m`, and the fixed-`g` physical-cycle configuration bounds audited in
`MATH_AUDIT_JMS_ORDERED_DIAMOND_DEFINITIVE_AND_DP_FALLBACK_20260801.md`.
Deleting `Z` removes at most `D|Z|` atoms and cannot increase any degree,
codegree, cycle-configuration degree, or mixed codegree.  The same
Delcourt--Postle corollary therefore colours the residual host with at most

\[
                         D(1+D^{-\alpha_g})           \tag{3.2}
\]

short-cycle-free matchings.  Its largest colour class `K` has size

\[
 |K|\ge {ND-D|Z|\over D(1+D^{-\alpha_g})}
       \ge N-ND^{-\alpha_g}-18H.                     \tag{3.3}
\]

Its physical graph has no cycle of length at most `g`.  Delete one atom
from each remaining physical cycle.  There are at most `N/(g+1)` such
cycles, so the resulting matching `F` is a physical linear forest and
satisfies (0.3).

Since `F` avoids both physical role copies of every packet vertex, it is
physically vertex-disjoint from `B^-` and `B^+`.  The two unions in Theorem
0.1 are therefore forests.  Resource disjointness follows from the other
parts of `Z`.  This completes the proof.  `square`

## 4. Exact scope

This proves the weakest useful finite-extension theorem:

> Any fixed typed-resource-disjoint family of desired central atoms has a
> graphically safe ternary-hex absorber bank, and the valid asymptotic
> Delcourt--Postle forest can be rebuilt around that bank.

It is stronger than merely saying that finite conditioning does not alter
the asymptotic count: the old phases are physically isolated, so every
gain has the exact contracted graphic position required by the five-edge
ear theorem.

It does **not** prove any of the following.

1. The `o(N)` leave of `F` can be paired into prescribed legal target
   atoms.
2. A bank of size larger than the elementary `Theta(m)` range can be
   planted by this greedy argument.
3. The long cycles of the Delcourt--Postle colour can be absorbed by this
   isolated bank.  The cycle-mode packet needs its target edge on the
   cycle, whereas the present construction reserves all packet vertices
   away from the bulk.
4. A central gain automatically lifts to a one-cell OR-word repair.  The
   star-hidden fan identity still couples its fan and lost-crossing traces.

Thus the bounded **central** regenerative bank needed in an `O(1)` proof is
now unconditional.  What remains is to make the other guarded tasks expose
their bounded central targets before this bank is planted, or to prove a
growing prescribed-leave/cycle-routing theorem.
