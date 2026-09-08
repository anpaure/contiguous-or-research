# Lane R: edge-coherent Catalan C8 selections versus the tuned promotion-ring middle normal form

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or probabilistic existence theorem is used.

## 0. Outcome

Put

\[
 V=[2m],\qquad W=\binom{2m}{m},\qquad B=\operatorname{Cat}_m={W\over m+1}.
\tag{0.1}
\]

For the tuned promotion-ring normal form, let

\[
 H=o(m),\qquad M=m+H,qquad R=N_H=\binom{2m}{m-H},
\tag{0.2}
\]

at the covering-side critical height, so that

\[
 T:=MR=W+o(W),\qquad {R\over B}=1+o(1).
\tag{0.3}
\]

Every promotion root

\[
 A\in\binom{V}{m-H}
\tag{0.4}
\]

has top (U=V\setminus A), of size (M). Choosing a cyclic frame

\[
 \gamma_A=(u_0,ldots,u_{M-1})
\tag{0.5}
\]

on (U) gives the middle-owner packet

\[
 \mathcal R_A(\gamma_A)
 =\{U\setminus I_{\gamma_A}(j,H):j\in\mathbb Z_M\},
\tag{0.6}
\]

equivalently the (M) cyclic length-(m) windows of (gamma_A).
The tuned middle gate is to choose one frame for every (A) so that the
union of these (T=W+o(W)) occurrences has only (o(W)) collisions.

This note compares that gate with the extensive reciprocal-(C_8) bank
on (D_m), using

\[
 u=\lfloor\alpha m\rfloor,qquad 0<\alpha<\frac12,
\tag{0.7}
\]

pairwise disjoint four-coordinate slots.

There is a substantial positive algebraic theorem which is stronger than
the previously used global-mask cube.

* For every elementary reciprocal rectangle (e), choose one bit (b_e),
  and give that same bit to the two Dyck rows at the ends of (e). These
  choices are mutually independent over all rectangles. They produce an
  exact anchored factor, preserving the complete (X/Y) ownership ledger,
  not merely its middle projection.
* Conversely, every rowwise C8 choice which preserves the complete factor
  ledger has equal bits at the two ends of every rectangle.
* Hence the extensive bank contains exactly

  \[
  \boxed{2^{uC_{m-2}}
  =2^{(\alpha/16+o(1))W}}
  \tag{0.8}
  \]

  edge-coherent exact factors. The old (2^u) global-mask cube is only a
  tiny diagonal subcube.

Thus there is no ambient middle-owner obstruction forcing one common slot
mask. This is a genuine integral selection theorem.

However, the theorem does not descend to the promotion rings by assigning
one C8 row to each root (A) and restricting its order to (U=A^c).
There are two exact reasons.

1. **Boundary-degree-two and frozen-mass barrier.** After restriction to a
   top, a C8 transposition either disappears or remains one adjacent
   transposition. A cyclic (H)-window sees only the possible swaps at
   its two boundary cuts. For the whole extensive bank, even after
   enlarging the coupled C8 bits to independent adjacent-swap bits,

   \[
   \boxed{	ext{at least }
   (1-\alpha/2-o(1))W> (3/4-o(1))W
   \text{ middle occurrences are frozen}.}
   \tag{0.9}
   \]

   At least ((1-\alpha-o(1))W) directed (H)-window-cycle arcs are
   frozen. The total root-labelled potential middle menu has size at most

   \[
   \boxed{(1+3\alpha/4+o(1))W<(11/8+o(1))W.}
   \tag{0.10}
   \]

   Therefore near-disjointness after C8 selection is possible only if the
   frozen occurrences already form a near-packing. The C8 choices cannot
   manufacture the main packing from the tuned fractional point.

2. **Exact-factor projection barrier.** For any cyclic order (pi) on
   (V) and any (M)-top (U), at most (H+1) middle windows of the
   restricted promotion frame (pi|_U) are also ambient middle windows
   of (pi):

   \[
   \boxed{|E_m(\pi|_U)\cap E_m(\pi)|\le H+1.}
   \tag{0.11}
   \]

   Consequently the ambient C8 exact-factor ownership partition certifies
   at most

   \[
   (H+1)R=O(WH/m)=o(W)
   \tag{0.12}
   \]

   of the promotion middle occurrences. Certifying one complete ring from
   ambient owner rows would require at least

   \[
   \boxed{\left\lceil{M\over H+1}\right\rceil
          =\Omega(m/H)}
   \tag{0.13}
   \]

   different ambient rows, rather than one.

There is a third, useful incompatibility. The four-term middle derivative
of a nontrivial adjacent swap in a promotion top determines that top: the
union of its four support targets is exactly (U). Hence two opposite
swap derivatives must belong to the same top. The two endpoints of an
ambient C8 rectangle, when assigned to distinct promotion roots, no
longer cancel after restriction. Any cancellation which survives must be
a new longer cross-top circuit, not the certified two-row C8 identity.

The requested explicit algebraic selection therefore exists at the
ambient Catalan-factor level but does **not** give the tuned promotion-ring
selection. The direct one-C8-row-per-promotion-root composition is closed
as an ownership-inheritance argument. What remains possible is a
top-native Latin system, or a multirow braid using
\(\Omega(m/H)\) ambient owner rows per promotion top, whose cross-top
derivatives cancel in longer circuits. No such system is constructed
here, and no universal obstruction is claimed against arbitrary
nonlocal top-native frames.

## 1. The extensive C8 root graph

Choose disjoint four-coordinate slots

\[
 I_1,\ldots,I_u
\tag{1.1}
\]

in a Dyck word of semilength (m). At slot (j), the two eligible local
fillings are

\[
 1100\longleftrightarrow1010.
\tag{1.2}
\]

Let (	au_j) be this partial involution on (D_m). Its eligibility graph

\[
 \mathcal M_j
 =\bigl\{\{P,\tau_jP\}:P|_{I_j}=1100\bigr\}
\tag{1.3}
\]

is a matching with exactly

\[
 |\mathcal M_j|=C_{m-2}
\tag{1.4}
\]

edges. The matchings for different (j) may share vertices but not
edges. Put

\[
 \mathcal E=\bigsqcup_{j=1}^u\mathcal M_j,
 \qquad |\mathcal E|=uC_{m-2}.
\tag{1.5}
\]

For a root (P), write (J(P)) for its eligible slots. A rowwise mask is
a family

\[
 \varepsilon_j(P)\in\{0,1\},\qquad j\in J(P).
\tag{1.6}
\]

The row selected at (P) is the simultaneous local C8 variant with those
bits. Disjoint slots occupy disjoint chronology slabs, so this row is a
literal path for every choice of its local mask.

Let

\[
 \mathbf a_P(\varepsilon(P))
\tag{1.7}
\]

be its complete state-and-colour incidence column, including every (X)
state, every (Y) colour, and the fixed ports.

### Lemma 1.1 (rowwise affine cube)

For every root (P), there are integral incidence columns

\[
 d_{P,j},\qquad j\in J(P),
\tag{1.8}
\]

such that

\[
 \boxed{
 \mathbf a_P(\varepsilon(P))
 =\mathbf a_P(0)+
   \sum_{j\in J(P)}\varepsilon_j(P)d_{P,j}.}
\tag{1.9}
\]

If (e=\{P,Q\}\in\mathcal M_j), then

\[
 \boxed{d_{P,j}+d_{Q,j}=0.}
\tag{1.10}
\]

#### Proof

For two distinct eligible slots (i,j), disjoint chronology slabs and
fixed gluing states give the exact cubical identity

\[
 \mathbf a_P(11)+\mathbf a_P(00)
 =\mathbf a_P(10)+\mathbf a_P(01).
\tag{1.11}
\]

Thus every mixed discrete second derivative vanishes. Induction on the
number of eligible bits gives the affine expansion (1.9), with

\[
 d_{P,j}=\mathbf a_P(e_j)-\mathbf a_P(0).
\]

For an elementary reciprocal rectangle, its two old rows and two new
rows have exactly the same complete state-and-colour ledger. Therefore

\[
 \mathbf a_P(e_j)+\mathbf a_Q(e_j)
 =\mathbf a_P(0)+\mathbf a_Q(0),
\]

which is (1.10). \(\square\)

## 2. An explicit edge-coherent exact-factor family

### Theorem 2.1 (edge-coherent Latin section)

A rowwise mask (arepsilon) gives a complete anchored exact factor if
and only if

\[
 \boxed{
 \varepsilon_j(P)=\varepsilon_j(Q)
 \quad\text{for every }e=\{P,Q\}\in\mathcal M_j.}
\tag{2.1}
\]

Consequently the edge-coherent exact factors are parametrized by arbitrary
bits

\[
 b_e\in\{0,1\},\qquad e\in\mathcal E,
\tag{2.2}
\]

and their number is exactly

\[
 \boxed{2^{uC_{m-2}}.}
\tag{2.3}
\]

#### Proof: sufficiency

Sum (1.9) over all roots and group derivatives by elementary rectangle:

\[
\begin{aligned}
 \sum_P\mathbf a_P(\varepsilon(P))-
 \sum_P\mathbf a_P(0)
 &=\sum_{j=1}^u
   \sum_{e=\{P,Q\}\in\mathcal M_j}
   \bigl(\varepsilon_j(P)d_{P,j}
          +\varepsilon_j(Q)d_{Q,j}\bigr)\\
 &=\sum_{j=1}^u
   \sum_{e=\{P,Q\}\in\mathcal M_j}
   \bigl(\varepsilon_j(P)-\varepsilon_j(Q)\bigr)d_{P,j}.
\end{aligned}
\tag{2.4}
\]

Condition (2.1) makes every summand zero. The complete incidence column
therefore equals the canonical exact-factor column. Every selected row is
literal and has the same ports, so this is a completed anchored exact
factor, not merely an ownership ledger.

#### Proof: necessity

Each elementary rectangle exchanges two unique internal primary
(X)-tokens. Those two token positions lie in its own chronology slab.
Disjoint slabs do not reuse them, and canonical exactness prevents a
token belonging to two different root rectangles.

If the two endpoint bits of (e) disagree, one of the exchanged tokens
has load two and the other load zero. No derivative belonging to another
rectangle contains either token, so this defect cannot cancel. Exactness
therefore forces (2.1) edge by edge.

There is one independent choice for each of the (|\mathcal E|) edges,
which proves (2.3). \(\square\)

Using

\[
 {C_{m-2}\over C_m}
 ={m(m+1)\over4(2m-1)(2m-3)}
 ={1\over16}+O(m^{-1}),
\tag{2.5}
\]

and (mB=(1+o(1))W), equation (2.3) becomes (0.8).

### Corollary 2.2 (exact defect of arbitrary rowwise bits)

Put

\[
 D(\varepsilon)=
 \sum_{j=1}^u\sum_{e=\{P,Q\}\in\mathcal M_j}
 \mathbf1_{\{\varepsilon_j(P)\ne\varepsilon_j(Q)\}}.
\tag{2.6}
\]

For the complete primary middle-owner histogram (mu),

\[
 \boxed{
 \sum_X(\mu(X)-1)_+
 =|\{X:\mu(X)=0\}|
 ={1\over2}\|\mu-\mathbf1\|_1
 =D(\varepsilon).}
\tag{2.7}
\]

In particular, independent fair row bits have

\[
 \mathbb E D={uC_{m-2}\over2}
 =\left({\alpha\over32}+o(1)\right)W.
\tag{2.8}
\]

#### Proof

On one mismatched rectangle, its two rows place both occurrences on one
of the two exchanged unique tokens and none on the other. This contributes
one collision, one hole, and total (ell^1)-error two. Matched endpoint
bits contribute neither. The exchanged token pairs are disjoint over
all elementary rectangles, so the contributions add exactly. Equation
(2.8) follows because an edge is mismatched with probability (1/2).
\(\square\)

This corollary identifies the correct dependency schedule. Independent
root signs fail linearly, but one common bit per reciprocal rectangle
preserves middle ownership exactly.

## 3. Exact cut-packet middle selection inside an edge-coherent factor

The preceding theorem concerns all anchored primary owners. If one cuts
at infinity and selects only a row shore (S\subseteq D_m), the ordinary
cyclic packets also contain the complementary nonport windows. Their
middle collision gate has the following exact Boolean form.

Fix an edge-coherent factor (F^b). For every nonport primary token (Q),
let (o_b(Q)) be its owner row and put

\[
 \ell_Q(b)=\mathbf1_{\{o_b(Q)\in S\}}.
\tag{3.1}
\]

If (Q) is untouched by the C8 bank, (ell_Q) is a constant. If it is
the token of a rectangle (e), then

\[
 \ell_Q(b)\in\{0,1,b_e,1-b_e\}.
\tag{3.2}
\]

The two nonconstant cases occur precisely when (e)'s root pair is split
by (S).

### Proposition 3.1 (exact complement 2-CNF)

The ordinary cut-packet middle collision is

\[
 \boxed{
 C_0(S,b)=
 2\sum_{\{Q,Q^c\}}ell_Q(b)\ell_{Q^c}(b),}
\tag{3.3}
\]

where every complementary nonport pair is taken once. Consequently:

1. (C_0(S,b)=0) if and only if the explicit clauses
   
   \[
   \neg\ell_Q\vee\neg\ell_{Q^c}
   \tag{3.4}
   \]
   
   form a satisfiable 2-CNF in the rectangle variables (b_e);
2. minimizing (C_0/2) is exactly the corresponding weighted
   Max-2SAT problem; and
3. complementary pairs whose two possible owner pairs both lie inside
   (S) are immutable violated clauses.

#### Proof

The primary owners themselves are distinct. For a complementary nonport
pair ({Q,Q^c}), the two ordinary cut packets duplicate both targets
exactly when both primary owner rows are selected. This is the event

\[
 \ell_Q(b)=\ell_{Q^c}(b)=1.
\]

It contributes exactly two to the ordinary middle collision excess.
Different complementary pairs use disjoint target pairs, so summing gives
(3.3). Equations (3.2)--(3.4) give the stated Boolean classification.
\(\square\)

This is an explicit algebraic selection gate, not an action estimate. It
does not solve the all-depth annulus clauses, but it replaces the vague
middle optimization by a signed implication-cycle problem.

## 4. Promotion rings and the boundary-degree-two normal form

Fix a promotion top (U), (|U|=M=m+H), with base cyclic frame

\[
 \gamma=(a_0,a_1,\ldots,a_{M-1}).
\tag{4.1}
\]

Let (mathcal C) be any matching of adjacent cuts of this frame. We
temporarily allow one independent bit at every cut in (mathcal C). This
enlarges the actual C8 menu, because one C8 rectangle may couple two
different adjacent transpositions.

For (j\in\mathbb Z_M), put

\[
 Y_j^0=\{a_j,a_{j+1},\ldots,a_{j+H-1}\},
 \qquad X_j^0=U\setminus Y_j^0.
\tag{4.2}
\]

The (Y_j)'s are the cyclic (H)-windows and the (X_j)'s are the
promotion middle owners.

### Lemma 4.1 (two-boundary formula)

The target (Y_j) depends only on the swap bits at the two cuts

\[
 j-1\mid j,qquad j+H-1\mid j+H.
\tag{4.3}
\]

If the corresponding bits are (s_j,t_j\in\{0,1\}), with a missing cut
interpreted as bit zero, then

\[
\begin{aligned}
 Y_j(s_j,t_j)
 ={}&Y_j^0
 -s_j\{a_j\}+s_j\{a_{j-1}\}\\
 &-t_j\{a_{j+H-1}\}+t_j\{a_{j+H}\}.
\end{aligned}
\tag{4.4}
\]

Every other adjacent swap is either wholly inside or wholly outside the
indexed window and hence does not change its underlying set.

#### Proof

An adjacent transposition changes the set in an indexed interval exactly
when the interval contains one of its two positions and not the other.
Those are precisely the two boundary cuts in (4.3). At the entrance cut,
(a_j) is replaced by (a_{j-1}); at the exit cut,
(a_{j+H-1}) is replaced by (a_{j+H}). This is (4.4). \(\square\)

Write

\[
 c(U)=|\mathcal C|,
\tag{4.5}
\]

and let (k_j\in\{0,1,2}) be the number of active cuts among the two
boundaries of start (j). Every cut is a boundary of exactly two
(H)-windows, so

\[
 \sum_{j\in\mathbb Z_M}k_j=2c(U).
\tag{4.6}
\]

### Corollary 4.2 (frozen starts and total potential menu)

For one top:

\[
 \boxed{#\{j:X_j\text{ is frozen under every variant}\}
 \ge M-2c(U),}
\tag{4.7}
\]

and, if (mathscr S_U) is the union of all middle targets obtainable
from all enlarged independent-cut variants,

\[
 \boxed{|\mathscr S_U|\le M+3c(U).}
\tag{4.8}
\]

At least (M-4c(U)) directed arcs of the cyclic (H)-window successor
cycle are unchanged under every variant.

#### Proof

Only a start with (k_j>0) can move. Equation (4.6) gives at most
(2c(U)) such starts, proving (4.7).

For a fixed start, (4.4) gives at most (2^{k_j}) target sets. Hence

\[
 |\mathscr S_U|
 \le\sum_j2^{k_j}
 =M+\sum_j(2^{k_j}-1).
\]

For (k\in\{0,1,2}),

\[
 2^k-1\le{3\over2}k.
\]

Together with (4.6), this proves (4.8). Finally, changing at most
(2c(U)) vertices can affect at most (4c(U)) incident directed cycle
arcs. \(\square\)

The result is deterministic and holds before any owner collisions are
considered. Exponentially many C8 row variants do not give an
exponentially large promotion-target menu; every indexed phase has at
most four possible middle owners.

## 5. A swap derivative remembers its promotion top

Let one effective adjacent swap exchange consecutive labels (p,q) in
a top (U). Exactly two length-(m) owner windows change. There are
((m-1))-sets (R_-,R_+\subset U\setminus\{p,q\}) such that, up to
overall sign, the incidence derivative is

\[
 \boxed{
 d_{U,pq}
 =e_{R_-\cup\{q\}}+e_{R_+\cup\{p\}}
  -e_{R_-\cup\{p\}}-e_{R_+\cup\{q\}}.}
\tag{5.1}
\]

### Lemma 5.1 (top recovery)

Assume (2\le H<m). The four targets in (5.1) are distinct and

\[
 \boxed{
 \bigcup_{X\in\operatorname{supp}d_{U,pq}}X=U.}
\tag{5.2}
\]

If (D) is the common inner core left after deleting the two
((H-1))-boundary blocks and (p,q), then also

\[
 \boxed{
 \bigcap_{X\in\operatorname{supp}d_{U,pq}}X=D,
 \qquad |D|=m-H.}
\tag{5.2a}
\]

Consequently, if two nonzero adjacent-swap derivatives satisfy

\[
 d_{U,pq}=-d_{U',p'q'},
\tag{5.3}
\]

then

\[
 \boxed{U=U'.}
\tag{5.4}
\]

#### Proof

Rotate the frame so that (p) is at position (0) and (q) at position
(1). The two affected length-(m) windows are the one ending at
position (0) and the one beginning at position (1). Their two
\((m-1))-cores occupy, respectively,

\[
 M-m+1,\ldots,M-1
 \quad\text{and}\quad
 2,\ldots,m
\tag{5.5}
\]

in cyclic position notation. Since (M=m+H) and (H<m), these two
blocks together with positions (0,1) cover every position of the top.
This proves (5.2). Equivalently, if (B,C) are the two disjoint
((H-1))-boundary blocks immediately before (p) and after (q), then

\[
 U=D\mathbin{\dot\cup}B\mathbin{\dot\cup}C
     \mathbin{\dot\cup}\{p,q\},
\]

and the four targets all contain (D), while each element outside (D)
is omitted by at least one of them. This proves (5.2a). The condition
(H\ge2) makes the four old/new windows distinct.

Equality (5.3) gives equality of the two four-target supports. Taking
their unions and applying (5.2) gives (U=U'). \(\square\)

Thus the opposite-derivative cancellation in an ambient reciprocal
rectangle is not preserved when its two endpoint rows are assigned to
distinct promotion tops. If both swaps survive restriction, their
four-term columns cannot be negatives. If one swap disappears, there is
nothing for the surviving column to cancel against. Longer dependencies
among several tops are not ruled out, but they are new circuits not
certified by the elementary C8 identity.

There is an exact minimum-cycle consequence in the one-derivative-per-top
regime. Consider a zero sum containing one nonzero adjacent-swap
derivative on each of a family of pairwise distinct tops. Form the
support-overlap graph on those tops, joining two when their derivative
supports share a middle target. A vertex cannot have degree one: then all
four signed coordinates of its derivative would have to cancel against
its sole neighbor, forcing equality of the two four-target supports and
hence, by (5.2), equality of the tops. Therefore every nonempty such
cancellation has minimum degree at least two and contains a cycle.
Moreover a shared middle target (X) satisfies (X\subseteq U\cap U'), so

\[
 d_J(U,U')=M-|U\cap U'|\le M-m=H.
\tag{5.5}
\]

Thus every surviving cross-top cancellation contains a genuine cycle in
the distance-(H) top graph, together with compatible signs on all four
coordinates of every local derivative. Pairwise ambient C8 coherence is
strictly too short. If several derivatives from one top are combined,
their internal cancellations must first be analyzed; no minimum-degree
claim for that more general compressed column is asserted here.

## 6. Aggregate frozen mass in the extensive bank

An eligible C8 slot changes one row order by two disjoint adjacent
transpositions. Put

\[
 c_x=2|J(x)|
\tag{6.1}
\]

for the ambient row (x\). Restriction to a promotion top can only delete
effective transpositions, so its effective cut count is at most (c_x).
The exact Catalan census gives

\[
 \sum_{x\in D_m}|J(x)|=2uC_{m-2},
\tag{6.2}
\]

and therefore

\[
 \boxed{
 \sum_{x\in D_m}c_x=4uC_{m-2}
 =\left({\alpha\over4}+o(1)\right)W.}
\tag{6.3}
\]

At the tuned height, (R/B=1+o(1)). Hence the promotion roots and Dyck
roots can be paired one-to-one after discarding or repeating only (o(B))
roots. All exceptional promotion rings together contain (o(W)) middle
occurrences. Even granting arbitrary frames on those exceptional rings,
the paired C8-rooted rings have total effective cut count at most

\[
 C_{\rm eff}\le4uC_{m-2}+o(W)
 =\left({\alpha\over4}+o(1)\right)W.
\tag{6.4}
\]

Summing Corollary 4.2 and using (T=W+o(W)) proves:

### Theorem 6.1 (extensive promotion-menu ceiling)

For every one-C8-row-per-promotion-root assignment and every choice of
local variants,

\[
 \boxed{F_{\rm vert}\ge
 T-2C_{\rm eff}
 =\left(1-{\alpha\over2}-o(1)\right)W,}
\tag{6.5}
\]

where (F_{\rm vert}) is the number of middle occurrences fixed under
every allowed variant. The number of directed (H)-window-cycle arcs
fixed under every variant is at least

\[
 \boxed{left(1-\alpha-o(1)\right)W.}
\tag{6.6}
\]

The sum, over promotion roots, of the sizes of their complete potential
middle-target menus is at most

\[
 \boxed{left(1+{3\alpha\over4}+o(1)\right)W.}
\tag{6.7}
\]

The bounds remain valid for the actual coupled C8 bits, since independent
effective-cut bits only enlarge the variant library.

Let (f_X) be the multiplicity of target (X) among the frozen
occurrences. Every final selection obeys the statewise obstruction

\[
 \boxed{
 C_{\rm mid}\ge\sum_{X\in\binom Vm}(f_X-1)_+.}
\tag{6.8}

Thus (C_{\rm mid}=o(W)) requires

\[
 \boxed{sum_X(f_X-1)_+=o(W).}
\tag{6.9}

#### Proof

Equations (6.5)--(6.7) are the sums of (4.7), the fixed-arc conclusion,
and (4.8), with the (o(W)) exceptional roots included. Frozen target
occurrences remain in every final packet. If (f_X\ge1), at least
(f_X-1) of them are collisions whatever the movable occurrences do.
Summing gives (6.8), and (6.9) follows. \(\square\)

For the maximal allowed density (alpha<1/2), equation (6.5) leaves
more than three quarters of the (W)-scale middle ledger frozen. The
extensive C8 bank can therefore be an absorber only after a
positive-density frozen near-packing already exists. This is stronger
than saying that its action capacity is large.

## 7. The ambient-to-top projection ceiling

### Theorem 7.1 (at most (H+1) inherited owner windows)

Let (pi) be any cyclic order of (V=[2m]), and let
(U\subseteq V) have size (M=m+H<2m). Delete (V\setminus U) from
(pi), retaining the induced cyclic order (pi|_U). Then

\[
 \boxed{|E_m(\pi|_U)\cap E_m(\pi)|\le H+1.}
\tag{7.1}
\]

#### Proof

Write the cyclic binary indicator of (U) in the order (pi). If an
(m)-set (X\) is both a length-(m) window of (pi|_U) and a
length-(m) window of (pi), then the latter ambient block consists
entirely of (U)-labels. Thus every target in the intersection comes
from a length-(m) all-one window in the binary indicator.

Let the cyclic one-run lengths be (r_1,\ldots,r_s). Since
(V\setminus U) is nonempty, these are ordinary separated runs and

\[
 \sum_i r_i=M.
\]

The number of length-(m) all-one windows is

\[
 \sum_i(r_i-m+1)_+.
\]

If (k) runs contribute positively, this sum is at most

\[
 M-k(m-1)\le M-m+1=H+1.
\]

This proves (7.1). \(\square\)

### Corollary 7.2 (one-row inheritance is negligible)

Suppose every promotion frame is obtained by restricting one ambient C8
row. Even if every ambient row family is one common exact factor, its
exact ambient middle-owner partition certifies at most

\[
 \boxed{(H+1)R=O(WH/m)=o(W)}
\tag{7.2}
\]

promotion occurrences. Moreover, a single promotion ring has (M)
owners, while one ambient row can contribute at most (H+1) of them.
Therefore a construction which populates a ring entirely from
ambient-factor-certified owners needs at least

\[
 \boxed{\left\lceil{M\over H+1}\right\rceil}
\tag{7.3}
\]

ambient rows for that top.

#### Proof

Apply Theorem 7.1 to every ring. Equation (0.3) gives

\[
 (H+1)R=(H+1){T\over M}=O(WH/m)=o(W).
\]

The pigeonhole bound (7.3) is immediate. \(\square\)

The corollary is deliberately about **inheritance of the exact owner
ledger**. It does not prove that the remaining, uncertified promotion
owners must collide. It proves that ambient C8 exactness supplies no
reason for them not to collide.

There are only two natural interpretations of a C8-derived frame:

1. Restrict a common ambient exact-factor row. Then (7.2) applies.
2. Relabel a C8 order template independently inside each top. Every ring
   remains literal, but the ambient cross-root ownership identity is lost;
   one is back at the original tuned promotion selection, now with the
   thin menu described by Theorem 6.1.

## 8. Exact surviving algebraic gate

For each promotion root (A), let (mathscr C_A) be its C8-derived
frame menu, and for (gamma\inmathscr C_A) let

\[
 v_A(\gamma)\in\{0,1\}^{\binom Vm}
\tag{8.1}
\]

be the incidence vector of its (M) middle owners. The tuned middle
condition is exactly

\[
 \boxed{
 \sum_A v_A(\gamma_A)=\mathbf1+z,
 \qquad
 \sum_X(z_X)_+=o(W),}
\tag{8.2}
\]

because the total left side has mass (T=W+o(W)). Formula (4.4) makes
every indexed coordinate of (v_A) depend on at most two local cut bits.
Equation (6.9) is a necessary frozen-core condition for (8.2).

The ambient edge-coherent choice (2.1) does not solve (8.2). Its
cancellation pairs derivatives belonging to the two roots of one
reciprocal rectangle. After those roots are assigned to distinct
promotion tops, Lemma 5.1 shows that their nonzero derivatives cannot be
opposites. A valid top selection therefore needs one of the following
new objects.

1. A base family whose frozen (>(3/4-o(1))W) occurrences already has
   collision (o(W)), followed by C8 absorption of the movable residue.
2. A top-native Latin/cocycle system producing longer cross-top
   derivative circuits whose complete signed sum is zero.
3. A multirow rethreading which uses (Omega(m/H)) ambient C8 owner rows
   inside each promotion top and simultaneously closes the cyclic
   chronology.

The annular version must impose the analogous equation at every signed
rank with one common choice of the same variables. Neither the ambient
edge-coherent theorem nor marginal action capacity supplies this
all-depth alignment.

## 9. Audited boundary

Proved here:

1. the rowwise affine C8 identity (1.9);
2. the necessary-and-sufficient edge-coherence theorem (2.1);
3. the exact family count (2^{uC_{m-2}});
4. the exact primary middle defect (D(\varepsilon));
5. the ordinary cut-packet complement 2-CNF (3.3)--(3.4);
6. the two-boundary promotion formula (4.4);
7. the frozen occurrence, frozen strong-cycle, and potential-menu bounds
   (6.5)--(6.7), with constants;
8. the top-recovery invariant for one swap derivative; and
9. the (H+1) ambient-to-top projection ceiling (7.1).

Not proved:

1. an explicit choice satisfying the tuned promotion equation (8.2);
2. that every possible C8-derived base violates the frozen near-packing
   condition (6.9);
3. a longer cross-top derivative circuit with positive-density coverage;
4. the simultaneous all-depth promotion-ring selection; or
5. coefficient one.

The precise answer to the question is therefore two-sided. C8 variants
do admit an explicit, enormous, integral algebraic selection preserving
the ambient exact factor. But the direct one-row-per-promotion-root
transport loses that cancellation and inherits only (o(W)) certified
owners. The promotion problem is not solved by choosing C8 variants; it
requires a new cross-top Latin braid or a pre-existing frozen
positive-density near-packing.
