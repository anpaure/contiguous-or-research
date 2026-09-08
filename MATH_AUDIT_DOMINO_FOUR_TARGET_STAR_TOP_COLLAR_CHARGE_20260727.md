# Four-target star--top coincidences: exact normal form, collar charge, and the whole-domino residual

Date: 2026-07-27

## 0. Outcome

Fix a domino-twin packet (F) at odd entrance length

\[
 n=2m,\qquad R=2r+1<m.
\]

The local four-target geometry can be classified completely.

1. A star cell and a top cell share at most two targets.  They share two
   precisely when they share one Johnson edge.
2. There are four realizable shore signatures, according as the two labels
   of that edge lie in one or two boundary dominoes of the star and in one
   or two endpoint dominoes of the top.
3. A purely cellwise charge is false.  A fixed shared edge has
   \(\Theta(n^2)\) top-cell continuations with two noncommon targets, and
   \(\Theta(n)\) continuations with one noncommon target.  Thus no claim of
   three, or even two, missing targets per freely chosen label follows from
   one cell.
4. The first collar repairs the one-free-label case.  A one-label deviation
   from a native top carrier forces at least two further noncommon targets
   in the other top cell incident with the nonnative endpoint domino.  Its
   collar charge is therefore at least (1+2=3).
5. A two-label reconnection has collar charge at least (2+2=4), and at
   least (2+2+2=6) when its two labels leave through distinct endpoint
   dominoes.  The sole exception is that the two labels themselves form one
   intact domino of (F).  This is a whole-domino transport, not a free
   pair reconnection.
6. In the cross-shore case the same (4/6) alternatives hold.  The only
   low-collar exception is again an intact old domino; the edge made from
   the two split boundary labels is fixed and carries no free label.

Consequently the requested charge (3) or (4) is valid for
**collar-disjoint, genuinely non-domino label reconnections**.  It is not
valid cell by cell.  The exact residual in a global close-neighbour proof is
a chain or cycle which transports intact (F)-dominoes between native top
carriers.  A global proof must also prevent double charging when first
collars meet.  Neither issue is resolved here, so this note does not claim
the bound

\[
 \#\{G:|F\cap G|\ge 4m-s\}
 \le \exp(O(m))n^{cs},\qquad c<\tfrac12.
\]

It does remove arbitrary star--top coincidences from the gate and replaces
them by one explicit block-transport residual.

**Subsequent same-date counteraudit.**  The later claimed paired-window
zipper treated every two-point anchor as releasing no labels.  Section 4
already shows why this is not a valid local inference.  The explicit
extendable corridor and its sharp two-star charge are recorded in
`MATH_COUNTERAUDIT_DOMINO_ZIPPER_TWO_POINT_ANCHOR_20260727.md`.
That counteraudit also fixes the interpretation of the displayed
\(3/4/6\) charges here: they are charges per selected endpoint event with
the stated top-cell collars, not unconditional charges per free label.
A same-shore mate hinge has two free endpoint labels but only four
noncommon targets in its immediate two-star collar.  Thus a per-label
charge \(3\) is valid for the genuine top-only split, and false without
that qualification.

## 1. The two canonical four-target partitions

Write the domino cycle of (F) as

\[
 B_i=\{x_i,y_i\},\qquad i\in\mathbb Z_m,
\]

and put

\[
 A_i=\bigcup_{h=0}^{r-1}B_{i+h}.
\]

The star cells are

\[
 \mathcal S_i
 =\{A_i\cup\{z\}:z\in B_{i-1}\cup B_{i+r}\}.       \tag{1.1}
\]

They are disjoint and partition (F).  There is a second, top-cell
partition.  Put

\[
 U_i=\bigcup_{h=0}^{r}B_{i+h}=A_i\cup B_{i+r},
 \qquad
 D_i=B_i\cup B_{i+r},                                  \tag{1.2}
\]

and

\[
 \mathcal T_i=\{U_i\setminus\{z\}:z\in D_i\}.          \tag{1.3}
\]

Indeed, deleting a member of (B_{i+r}) gives one of the two right-shore
targets of (mathcal S_i), while deleting a member of (B_i) gives one of
the two left-shore targets of (mathcal S_{i+1}).  Thus the
(mathcal T_i) are also disjoint and partition (F).

It is convenient to use the abstract notation

\[
 \mathcal S(A,C)=\{A\cup\{c\}:c\in C\},                \tag{1.4}
\]

where (|A|=R-1), (C\cap A=\varnothing), (|C|=4), and

\[
 \mathcal T(U,D)=\{U\setminus\{d\}:d\in D\},          \tag{1.5}
\]

where (|U|=R+1), (D\subseteq U), (|D|=4).

## 2. Complete intersection classification

### Lemma 2.1 (star--star)

Let (mathcal S(A,C)) and (mathcal S(A',C')) be star cells.

* If (A=A'), then
  \[
   |\mathcal S(A,C)\cap\mathcal S(A,C')|=|C\cap C'|.
  \]
* If (A\ne A'), the intersection is nonempty only when
  \[
   A=K\cup\{a\},\qquad A'=K\cup\{b\}
  \]
  for distinct (a,b).  In that case it consists of the single target
  (K\cup\{a,b\}), and this target occurs exactly when
  (b\in C) and (a\in C').

#### Proof

If (A\cup\{c\}=A'\cup\{c'\}), then (A,A') are two
((R-1))-subsets of one (R)-set.  They are equal or differ by one
exchange.  In the latter case their union is the only possible common
target.  The displayed membership conditions are then necessary and
sufficient.  \(\square\)

### Lemma 2.2 (top--top)

Let (mathcal T(U,D)) and (mathcal T(U',D')) be top cells.

* If (U=U'), their intersection has size (|D\cap D'|).
* If (U\ne U'), the intersection is nonempty only when
  (U=K\cup\{a\}), (U'=K\cup\{b\}).  It then consists of the single
  target (K), provided (a\in D) and (b\in D').

#### Proof

Apply Lemma 2.1 after taking complements inside the two carriers, or argue
directly from (U\setminus\{d\}=U'\setminus\{d'\}).  \(\square\)

### Lemma 2.3 (star--top shared-edge normal form)

For a star (mathcal S(A,C)) and a top (mathcal T(U,D)),

\[
 |\mathcal S(A,C)\cap\mathcal T(U,D)|\le2.              \tag{2.1}
\]

The intersection is nonempty only if (A\subset U).  In that case write

\[
 U\setminus A=\{u,v\}.
\]

Then

\[
 |\mathcal S(A,C)\cap\mathcal T(U,D)|
 =\mathbf1_{\{u\in C,\ v\in D\}}
  +\mathbf1_{\{v\in C,\ u\in D\}}.                   \tag{2.2}
\]

In particular, equality holds in (2.1) precisely when

\[
 \{u,v\}\subseteq C\cap D.                             \tag{2.3}
\]

The common targets are then

\[
 A\cup\{u\}=U\setminus\{v\},
 \qquad
 A\cup\{v\}=U\setminus\{u\}.                         \tag{2.4}
\]

They form the shared Johnson edge.

#### Proof

An equality (A\cup\{c\}=U\setminus\{d\}) implies
(A\subset U), (d\notin A), and (c\ne d).  As
(|U\setminus A|=2), the ordered pair ((c,d)) is either ((u,v)) or
((v,u)).  Formula (2.2) follows.  \(\square\)

Lemmas 2.1--2.3 give every possible intersection of two canonical
four-target cells, including all one-target degeneracies.

## 3. Four shore signatures and realizability

In a twin packet, the four-set (C) in a star cell is the disjoint union
of two (F)-dominoes, and the four-set (D) in a top cell is the disjoint
union of two endpoint dominoes of the second packet.  When (2.3) holds,
the pair (E=\{u,v\}) can therefore be

* in one (F)-shore or split between the two (F)-shores; and
* in one top endpoint domino or split between the two endpoint dominoes.

Thus there are four signatures

\[
 (\mathrm{same},\mathrm{same}),\quad
 (\mathrm{same},\mathrm{split}),\quad
 (\mathrm{split},\mathrm{same}),\quad
 (\mathrm{split},\mathrm{split}).                       \tag{3.1}
\]

### Lemma 3.1

All four signatures in (3.1) occur in completed twin packets whenever
(r\ge2) and there are at least two blocks outside the displayed carrier.

#### Proof

Choose a set (A) of size (2r) and pair it into the (r) core
dominoes of (F).  For the same-shore case pair (u,v) together as one
boundary domino; for the split case use boundary dominoes
({u,w\},\{v,x\}), with (w,x\notin A\cup\{u,v\}).

For the second packet put (U=A\cup\{u,v\}).  Choose distinct
(a,b\in A).  Its endpoint four-set is
(D=\{u,v,a,b\}).  Pair (u,v) together to obtain the same-endpoint
signature, or pair them as ({u,a\},\{v,b\}) to obtain the split
signature.  Pair the remaining elements of (U\setminus D) arbitrarily
into the internal dominoes.  Finally pair and order all labels outside
the displayed carriers arbitrarily.  This completes both cyclic domino
orders.  \(\square\)

Thus none of the four signatures can be discarded as a formal but
physically unrealizable corner.

## 4. Exact local target charge

Fix a star cell (mathcal S_i) of (F) and a shared edge
(E=\{u,v\}\subseteq B_{i-1}\cup B_{i+r}).  Let
(mathcal T(U,D)) be a top cell of a second packet which shares this
edge, so

\[
 U=A_i\cup E,\qquad E\subseteq D.                       \tag{4.1}
\]

Write

\[
 \mu_F(\mathcal T)=|\mathcal T\setminus F|.             \tag{4.2}
\]

### Lemma 4.1 (cross-shore case)

If (u,v) lie in different (F)-boundary dominoes, then

\[
 |\mathcal T(U,D)\cap F|=2,
 \qquad
 \mu_F(\mathcal T)=2.                                  \tag{4.3}
\]

#### Proof

The occupancy of (U) in the (F)-dominoes is: (r) consecutive full
blocks, and one singleton in each adjacent boundary block.  Deleting one
of those two boundary singletons leaves (r) consecutive full blocks and
one adjacent singleton, hence gives the two shared targets.  Deleting any
element of (A_i) leaves only (r-1) full blocks and three singleton
blocks.  Such a set has neither form (1.1) nor membership in (F).
\(\square\)

### Lemma 4.2 (same-shore case)

Suppose (E) is a whole (F)-boundary domino.  Then (U) is a native
(F)-top carrier.  Let (O) be its opposite endpoint (F)-domino, so
the native endpoint four-set is (D_F=E\cup O).  Put

\[
 L=D\setminus E,\qquad |L|=2,
 \qquad t=|L\cap O|.
\]

Then

\[
 |\mathcal T(U,D)\cap F|=2+t,
 \qquad
 \mu_F(\mathcal T)=2-t.                                \tag{4.4}
\]

#### Proof

The carrier (U) is a union of (r+1) consecutive full (F)-dominoes.
An (R)-subset (U\setminus\{z\}) belongs to (F) exactly when (z)
lies in one of the two endpoint dominoes: deleting an internal label
splits the (r) remaining full blocks into two nonempty runs.  Therefore
the targets of (mathcal T(U,D)) which lie in (F) are exactly those
indexed by (D\cap(E\cup O)).  This gives (4.4).  \(\square\)

For a fixed shared edge (E), Lemma 4.2 gives the exact list sizes

\[
\begin{array}{c|c|c|c}
t&\mu_F&\text{choices of }L&\text{pairings of }D\\ \hline
2&0&1&3\\
1&1&2(R-3)&3\\
0&2&\binom{R-3}{2}&3.
\end{array}                                             \tag{4.5}
\]

If endpoint blocks are ordered, the last column is multiplied by two.
In the cross-shore case there are

\[
 \binom{R-1}{2}
\]

choices for (L=D\setminus E), again with three pairings, and every one
has (mu_F=2).

### Corollary 4.3 (cellwise charge is false)

A prescribed shared edge has (Theta(n)) top-cell continuations with one
noncommon target and (Theta(n^2)) continuations with two noncommon
targets.  Moreover, the (t=2) row has two nonnative endpoint pairings
with no noncommon target in the cell.  Therefore no cellwise injection can
charge three or four missing targets to every free label or local
reconnection.

The (t=2) degeneracy has only constant branching: all four endpoint
labels are already fixed.  The dangerous (n)-entropy lies in the
(t=1,0) rows and in their cross-shore analogue.

## 5. Low-defect carriers and the first collar

We now use the fact that a top endpoint domino is shared by two top
carriers of the same packet.

### Lemma 5.1 (three targets force a native carrier)

If a top cell (mathcal T(U,D)) satisfies

\[
 \mu_F(\mathcal T)\le1,
\]

then (U=U_i) for one of the native carriers (1.2).  For this (i),

\[
 \mu_F(\mathcal T)=|D\setminus D_i|.                   \tag{5.1}
\]

#### Proof

At least three targets of the top cell lie in (F).  Three distinct
members of a top cell form a Johnson triangle with union (U).  The
triangle classification in the domino normal form says that every
triangle of (F) lies in one of its canonical star or top cells.  It
cannot lie in a star cell, by Lemma 2.3.  Hence it lies in a canonical top
cell, whose carrier, being the union of the triangle, is (U).  Therefore
(U=U_i).  Lemma 4.2, with no need to prescribe a shared edge, says that
the members of (F) inside this carrier are exactly
(U_i\setminus\{d\}), (d\in D_i), proving (5.1).

For completeness, the triangle classification itself follows directly
from (1.1): three pairwise adjacent targets either have their common
((R-1))-core, which fixes one star cell, or have common
((R+1))-union, in which case their three occupancy vectors force one
run of (r+1) full dominoes and hence one top cell.  \(\square\)

Let the second packet have dominoes (C_j).  Its top carriers are

\[
 V_j=\bigcup_{h=0}^{r}C_{j+h}.
\]

The endpoint domino (C_j) belongs to the two top cells with carriers
(V_j) and (V_{j-r}).

### Lemma 5.2 (opposite-carrier intersection)

\[
 V_j\cap V_{j-r}=C_j.                                   \tag{5.2}
\]

#### Proof

The block-index intervals ([j,j+r]) and ([j-r,j]) intersect only in
(j), because (2r+1=R<m).  The dominoes of a packet are disjoint, so
their carrier sets intersect exactly in (C_j).  \(\square\)

### Lemma 5.3 (nonnative endpoint between native carriers is impossible)

Suppose both (V_j) and (V_{j-r}) are native (F)-top carriers.  Then
(C_j) is one of the original dominoes (B_i).

#### Proof

Native carriers are unions of (F)-dominoes.  Their intersection is
therefore a union of (F)-dominoes.  By (5.2) it has size two, so it is
one (F)-domino.  \(\square\)

This elementary intersection observation supplies the missing collar
charge.

## 6. The (3/4/6) collar theorem

Call an endpoint domino of the second packet **split** if it is not one of
the (B_i).

### Theorem 6.1 (native central carrier)

Let (mathcal T) be a top cell of the second packet whose carrier is a
native (F)-carrier, and put (mu=mu_F(\mathcal T)le2).

1. If (mu=1), the endpoint domino containing the unique foreign label
   is split.  If (mathcal T^*) is the other top cell incident with that
   domino, then
   \[
    mu_F(\mathcal T)+\mu_F(\mathcal T^*)\ge3.           \tag{6.1}
   \]
2. If (mu=2) and the two foreign labels lie in one split endpoint
   domino, then
   \[
    mu_F(\mathcal T)+\mu_F(\mathcal T^*)\ge4.           \tag{6.2}
   \]
3. If (mu=2) and the two foreign labels lie in distinct endpoint
   dominoes, the two opposite cells (mathcal T_1^*,mathcal T_2^*)
   are distinct and
   \[
    mu_F(\mathcal T)+
    \mu_F(\mathcal T_1^*)+
    \mu_F(\mathcal T_2^*)\ge6.                          \tag{6.3}
   \]
4. The only case not covered by (2) is that the two foreign labels form
   one intact (F)-domino.  This is the whole-domino transport residual.

#### Proof

In case (1), the foreign label lies in an internal (F)-domino of the
native carrier.  If its endpoint domino in the second packet were that
intact (F)-domino, both labels of this domino would be foreign, contrary
to (mu=1).  Thus this endpoint domino is split.

For any split endpoint (C), if its opposite cell had missing count at
most one, Lemma 5.1 would make its carrier native.  The central carrier is
native as well, and Lemma 5.3 would then make (C) an (F)-domino, a
contradiction.  Hence every opposite cell reached through a split endpoint
has missing count at least two.  This proves (6.1) and (6.2).

In case (3), both endpoint dominoes are split by the same argument.  Their
opposite cells have indices (j-r) and (j+r), which are distinct because
(2r<m).  Each has missing count at least two, proving (6.3).

If the two foreign labels occupy one endpoint and that endpoint is not
split, they form an intact (F)-domino.  This is exactly (4).  \(\square\)

The fully common but cross-paired row (mu=0) also has a collar cost:
each of its two cross-paired endpoint dominoes is split, so their two
distinct opposite cells have missing count at least two.  Thus the two
nonnative pairings of the four fixed endpoint labels cost at least four
targets in the first collar, although their branching was already only
constant.

### Theorem 6.2 (cross-shore central carrier)

Suppose a top cell shares a cross-shore edge with a star cell of (F).
Its central missing count is two.

1. If the two edge labels are split between the two endpoint dominoes,
   both opposite cells have missing count at least two, and the central
   cell together with its collars has charge at least six.
2. If the two edge labels form one endpoint domino, write (L) for the
   other endpoint domino.  If (L) is split, its opposite cell has missing
   count at least two, giving charge at least four.
3. The only uncharged alternatives are the fixed edge domino itself and
   the case in which (L) is an intact (F)-domino.

#### Proof

Use the notation of Lemma 4.1.  The carrier (U) has (r) full
(F)-dominoes and one singleton in each adjacent boundary domino.

Suppose an opposite cell through an endpoint (C) has missing count at
most one.  Its carrier (W) is native by Lemma 5.1, and Lemma 5.2 gives
(U\cap W=C).  Since (W) is a union of whole (F)-dominoes, an
intersection of size two can only be

* one whole (F)-domino contained in the core (A_i); or
* the pair consisting of the two boundary singletons.

Indeed, if (W) contains one boundary singleton and one label of a full
core domino, it also contains the mate of the latter, making the
intersection at least three.  If it contains labels from two full core
dominoes, the intersection has size at least four.

When the edge labels are split, each endpoint contains one boundary
singleton and one core label, so neither exceptional intersection is
possible.  Both opposite cells therefore have missing count at least two,
proving (1).  When the edge labels are paired, that fixed endpoint is the
second exceptional intersection.  The other endpoint (L\subset A_i)
can be a low-collar intersection only if it is one whole (F)-domino.
This proves (2)--(3).  \(\square\)

## 7. Exact boundary for the close-neighbour count

Theorems 6.1 and 6.2 prove the desired local charges with the correct
qualification.

* one genuinely free label in a native carrier: at least three missing
  targets in its central cell and first collar;
* one genuinely split two-label reconnection: at least four missing
  targets, or six when its two outputs separate;
* cross-shore shared edge: charge four or six after ignoring the fixed
  edge endpoint;
* zero-target local degeneracy: constant branching only, and first-collar
  charge four if cross-paired.

For a family whose displayed central and collar cells are pairwise
disjoint, these charges add literally because the top cells of the second
packet partition its targets.  Hence such a family contributes at most a
constant-to-the-(m) factor times (n^{s/3}), and the split two-label
subfamily has the stronger (n^{s/4}) scale when one already exposed
label is reconnected to one new partner.

Two issues prevent a global list-decoding theorem from being asserted.

1. First collars of different events can be the same top cell.  The
   degree-two carrier graph limits this overlap but does not by itself
   preserve the (3/4) charge after division by the overlap multiplicity.
2. An intact (F)-domino can pass between two native carriers without
   invoking Lemma 5.3.  Repeated exceptions form a block-transport chain
   or cycle.  The remaining exact statement is therefore a one-dimensional
   inverse theorem for this chain: either its block choices have only
   \(\exp(O(m))\) entropy, or every new block reconnection must create
   enough additional nonnative carriers to restore a strict exponent below
   (1/2).

Thus the star--top cell itself is no longer mysterious.  The surviving
annular gate is the global packing of its intact-domino exceptions and of
overlapping first collars.
