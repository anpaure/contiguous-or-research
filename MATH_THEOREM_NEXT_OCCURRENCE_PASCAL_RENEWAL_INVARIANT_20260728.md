# A next-occurrence Pascal--renewal invariant for the exact bound `B(k)`

Date: 2026-07-28

Status: exact fixed-dimension equivalence and exact conditional induction
invariant.  This note does **not** prove that the invariant exists in every
dimension.  It identifies a literal, non-rankwise object whose existence
would prove `nu(k)=B(k)`, proves that its lower pins automatically satisfy
the common-`Q` compiler, and gives the exact way in which the Pascal
odd/even sectors and the forced run-boundary ports must be included.  It also
proves why a static finite-radius version cannot be inductive.

The useful advance over a separate carrier-plus-Hall package is that the
physical word is encoded once, by future-hit ordered partitions.  Every
lower pin is then a marked prefix of the same table.  There is no subsequent
owner synchronization to guess.

## 1. Exact target and cell ledger

Put

\[
 r=\left\lceil\frac k2\right\rceil,
 \qquad
 W=W_k={k\choose r},
 \qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},                           \tag{1.1}
\]

and let `d=d(k)` be the least nonnegative integer for which

\[
             dW+{d+1\choose2}\ge\Lambda.                        \tag{1.2}
\]

The conjectured optimum is

\[
                         B(k)=W+d.                               \tag{1.3}
\]

Write

\[
                         N=W+d.                                  \tag{1.4}
\]

There are exactly

\[
 \sum_{q=0}^{d-1}(N-q)
   =d(W+d)-{d\choose2}
   =\boxed{dW+{d+1\choose2}}                                    \tag{1.5}
\]

physical intervals of lengths `1,...,d`.  Thus (1.2) is exactly the
capacity inequality for placing every target below rank `r` into a short
cell.  It is not yet a containment, chronology, or common-word theorem.

## 2. Timed next-occurrence partitions

Let

\[
                         A=(A_0,\ldots,A_{N-1})                  \tag{2.1}
\]

be a word of nonempty subsets of `[k]`.  For `0<=i<=N` and `x in [k]`, put

\[
 n_i(x)=\min\{p\ge i:x\in A_p\},                                \tag{2.2}
\]

with value `infinity` when the set is empty.  Put

\[
 B_i(t)=\{x:n_i(x)=i+t\}\quad(0\le t<N-i),
 \qquad
 B_i(\infty)=\{x:n_i(x)=\infty\}.                              \tag{2.3}
\]

The **timed future partition** is the deadline-labelled array

\[
 \Pi_i=(B_i(0),B_i(1),\ldots,B_i(N-i-1),B_i(\infty)).           \tag{2.3a}
\]

Empty finite time slots are retained.  This is essential: the ordinary
ordered partition obtained by suppressing empty blocks does not determine
which prefix is reached after a prescribed physical length.

For a set `X`, define the backward timed move-to-front operation by

\[
\begin{aligned}
 (M_X\Pi_{i+1})(0)&=X,\\
 (M_X\Pi_{i+1})(t+1)&=B_{i+1}(t)\setminus X,\\
 (M_X\Pi_{i+1})(\infty)&=B_{i+1}(\infty)\setminus X.
\end{aligned}                                                    \tag{2.3b}
\]

Thus `move-to-front' here includes the one-unit shift of every labelled
future slot; it is not the unlabelled MTF operation.

### Theorem 2.1 (future-table/word equivalence)

The future partitions of a nonzero word satisfy

\[
 \Pi_N=([k]_\infty),
 \qquad
 \boxed{\Pi_i=M_{A_i}(\Pi_{i+1})}
       \quad(0\le i<N).                                         \tag{2.4}
\]

Conversely, suppose deadline-labelled arrays `Pi_0,...,Pi_N` and nonempty masks
`A_i` satisfy (2.4).  Then they are exactly the next-occurrence partitions
of the word `(A_i)`.  In particular, `A_i` is the first finite block of
`Pi_i`.

#### Proof

Prepending `A_i` to the suffix beginning at `i+1` makes time `i` the next
occurrence of every coordinate of `A_i`.  Every other coordinate keeps its
old absolute next-occurrence time, shifted one relative slot, and all later
copies of coordinates in `A_i` cease to be next occurrences.  This is
precisely (2.3)--(2.4).

Conversely, induct backwards from `Pi_N`.  The same description shows at
each step that the blocks of `Pi_i` are the level sets of the minimum in
(2.2).  \(\square\)

Passing from start `i` to `i+1` gives the equivalent forward description:
remove the zero-time block and reinsert its coordinates at their next
absolute occurrence times.  The timed form is important: empty time slots
are allowed and determine which prefix is reached by a fixed physical
length.

For `0<=q<N-i`, define the threshold prefix

\[
 C_{i,q}=\{x:n_i(x)\le i+q\}.                                   \tag{2.5}
\]

### Lemma 2.2 (intervals are timed prefixes)

For every `i,q`,

\[
                         \boxed{C_{i,q}=\bigcup_{p=i}^{i+q}A_p.} \tag{2.6}
\]

#### Proof

A coordinate belongs to the right-hand side exactly when its first
occurrence at or after `i` is at most `i+q`.  \(\square\)

Thus a single future table simultaneously specifies every contiguous-OR
cell.  Separate choices at different depths are not present in this model.

## 3. Middle deadlines, countdown clocks, and forced ports

Assume now that \(d\ge1\) and

\[
                         T_i=C_{i,d}\qquad(0\le i<W).             \tag{3.1}
\]

For `x in T_i`, define its arrival clock

\[
                         a_i(x)=n_i(x)-i\in\{0,\ldots,d\}.       \tag{3.2}
\]

Then

\[
                         C_{i,q}=\{x\in T_i:a_i(x)\le q\}
                  \qquad(0\le q\le d).                          \tag{3.3}
\]

### Theorem 3.1 (countdown and Johnson boundary ports)

Suppose consecutive middle states are Johnson-adjacent,

\[
                  T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.         \tag{3.4}
\]

Then:

1. for \(x\in T_i\cap T_{i+1}\) with \(a_i(x)>0\),

   \[
                         a_{i+1}(x)=a_i(x)-1;                    \tag{3.5}
   \]

2. the deleted coordinate is a zero-time occurrence,

   \[
                         \boxed{\alpha_i\in A_i;}                \tag{3.6}
   \]

3. the inserted coordinate enters at the maximum deadline and occurs at
   the far end of its first middle window,

   \[
     \boxed{a_{i+1}(\beta_i)=d,qquad
            \beta_i\in A_{i+d+1}.}                              \tag{3.7}
   \]

#### Proof

If the next occurrence of a common coordinate is after `i`, shifting the
start one step toward that same occurrence decreases its distance by one,
which is (3.5).

If `alpha_i` did not occur at `i`, its occurrence witnessing membership in
`T_i` would lie in `[i+1,i+d]`, and hence also in the next middle window
`[i+1,i+d+1]`, contrary to `alpha_i notin T_(i+1)`.  This proves (3.6).

The coordinate `beta_i` has no occurrence in `[i,i+d]`, because it is absent
from `T_i`, but it has one in `[i+1,i+d+1]`, because it is present in
`T_(i+1)`.  The only possible position is `i+d+1`, proving (3.7).
\(\square\)

For a relative deadline `t`, write

\[
                         B_i(t)=\{x:n_i(x)=i+t\}.                 \tag{3.7a}
\]

### Lemma 3.2 (horizon-crossing Johnson criterion)

For every central transition,

\[
 T_{i+1}\setminus T_i=B_i(d+1),                                 \tag{3.7b}
\]

and

\[
 T_i\setminus T_{i+1}
 =\{x\in A_i:n_{i+1}(x)>i+d+1\}.                                \tag{3.7c}
\]

Consequently the transition is a Johnson edge if and only if the
beyond-horizon block `B_i(d+1)` is one singleton `\{beta_i\}`, and exactly
one coordinate `alpha_i` of the zero-time block has its next occurrence
beyond the next deadline.

#### Proof

A coordinate absent from `[i,i+d]` but present in `[i+1,i+d+1]` can first
occur only at `i+d+1`, proving (3.7b).  A coordinate present in the first
window but absent from the second must occur at `i` and have no later
occurrence through `i+d+1`, proving (3.7c).  Equal rank and singleton
differences are precisely Johnson adjacency.  \(\square\)

This is the clean local port test for a sector interface.  Under
lower-`d`-freshness it also recovers the Pascal flag formula

\[
 L_i^{(q)}
 =T_i\setminus\{\alpha_i,\ldots,\alpha_{i+q-1}\}.                \tag{3.7d}
\]

Thus `L^(1)` is the adjacent threshold face obtained by deleting the unique
zero-time coordinate whose reinsertion lies beyond the deadline.  The
odd-to-even tagged lower shore must retain this reinsertion class, not only
the unordered middle labels.

Let `P` be the maximal erosion controller

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,W-1)}T_i,
 \qquad 0\le p<N.                                                \tag{3.8}
\]

Every physical letter satisfies $A_p\subseteq P_p$, because every central
window containing position `p` must contain `A_p`.  At a fully interior
position, the erosion identities give

\[
 P_p\setminus P_{p+1}=\{\alpha_p\},
 \qquad
 P_p\setminus P_{p-1}=\{\beta_{p-d-1}\}.                        \tag{3.9}
\]

Equations (3.6)--(3.7) therefore yield the exact forced-port inclusion

\[
 \boxed{
 (P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1})
                 \subseteq A_p\subseteq P_p.}                   \tag{3.10}
\]

This derives the two controller ports from next-occurrence consistency; it
does not add them as an independent local rule.

### Corollary 3.3 (run pinning)

Let `[u,v]` be an internal maximal run of coordinate `x` in `P`, and put

\[
                         H_x=\{p:x\in A_p\}.                     \tag{3.11}
\]

Then

\[
 u,v\in H_x,
 \qquad
 h_{j+1}-h_j\le d+1                                             \tag{3.12}
\]

for consecutive points of $H_x\cap[u,v]$.  Conversely, (3.12), with the
one-sided boundary versions, is sufficient coordinatewise for
`D^dA=T`.

#### Proof

The controller run `[u,v]` is the erosion of the corresponding internal
middle run `[u-d,v]`.  The leftmost middle window can be hit only at or after
`u` and ends at `u`, forcing `u`; the rightmost can be hit only at or before
`v` and begins at `v`, forcing `v`.  A gap of at least `d+2` would leave a
length-`d+1` central window unhit.  The same window-cover argument proves
the converse.  \(\square\)

In arrival-clock language, an internal new-coordinate middle run `[u,v]`
must begin with

\[
                         a_u(x)=d                                \tag{3.13}
\]

and end with `a_v(x)=0`.  Its first physical occurrence is at `u+d`, not at
`u`.  This `d`-position offset is the exact port collar which a bare Pascal
label lift forgets.

## 4. The literal renewal compiler invariant

### Definition 4.1 (renewal compiler frame)

A **renewal compiler frame** `RCF(k)` is a timed future table of length
`N=W+d(k)` satisfying:

1. **Nonzero recurrence.**  Equations (2.4) hold and every first block
   `A_i` is nonempty.
2. **Exact middle deck.**  The `W` sets

   \[
                         T_i=C_{i,d}\quad(0\le i<W)               \tag{4.1}
   \]

   are the members of `binom([k],r)` exactly once, in Johnson order.
3. **Lower prefix completeness.**

   \[
   \{C_{i,q}:0\le q<d,\ 0\le i<N-q\}
       \supseteq\{S:1\le|S|<r\}.                               \tag{4.2}
   \]

4. **Upper prefix completeness.**

   \[
   \left\{\bigcup_{h=0}^{s}T_{i+h}:
          s\ge1,\ 0\le i<W-s\right\}
       \supseteq\{S:r<|S|\le k\}.                              \tag{4.3}
   \]

### Theorem 4.2 (frame sufficiency and exact common-`Q`)

If `RCF(k)` exists, then its first blocks form a nonzero universal word of
length `B(k)`.  Consequently

\[
                         \boxed{\nu(k)=B(k).}                    \tag{4.4}
\]

Moreover, choose one witnessing cell for every target in (4.2), every
middle target in (4.1), and every target in (4.3).  This complete
selected pin family satisfies the exact common-`Q` criterion for the one
physical word.  No separate rankwise synchronization hypothesis is needed.

#### Proof

Theorem 2.1 produces the word `(A_i)`, and Lemma 2.2 identifies every marked
prefix with its literal interval union.  Conditions 2--4 cover respectively
the middle, lower, and upper ideals.  For the upper identity, note that

\[
 \bigcup_{h=0}^{s}T_{i+h}
 =\bigcup_{p=i}^{i+d+s}A_p=C_{i,d+s}.                            \tag{4.5}
\]

The word has length `N=W+d=B(k)`.  The known deadline lower bound gives the
reverse inequality in (4.4).

For common-`Q`, let `I_S` be a selected interval with union `S`, and let
`P` be (3.8).  Put

\[
 K_x=\{p:x\in P_p\}\setminus
       \bigcup_{S:x\notin S}I_S.                                \tag{4.6}
\]

The actual occurrence set `H_x` from (3.11) is contained in `K_x`: it lies
in the controller, and if $x\notin S$, no position of the exact interval
`I_S` contains `x`.  If $x\in S$, exactness of the interval supplies a point
of $H_x\cap I_S$.  Every central positive coordinate is similarly hit, and
every physical point contains a member of some `H_x`.  Hence all central
hits, pin-positive hits, and point nonemptiness conditions of the maximal
common-`Q` theorem hold.  \(\square\)

### Corollary 4.3 (exact flat-form equivalence)

Within the flat-middle architecture, a length-`B(k)` universal word whose
`W` length-`d+1` cells are the middle deck is equivalent to an `RCF(k)`.

#### Proof

One direction is Theorem 4.2.  In the other direction, take the word's exact
future partitions.  The middle condition is (4.1); every lower target must
use a cell of length at most `d`, since a longer cell contains a rank-`r`
middle window; and (4.5) gives (4.3).  \(\square\)

The equivalence is deliberately architecture-scoped.  It does not assert
that every hypothetical optimum has already been normalized to a flat
middle row.

### Theorem 4.4 (canonical maximal-\(Q\) renewal table)

The frame can be specified without first guessing its physical letters.
Fix:

1. the central marks \(([i,i+d],T_i)\);
2. an injective assignment of every lower target \(S\) to a short interval
   \(I_S\).

For each coordinate define

\[
 Q_x=\{p:x\in P_p\}\setminus
       \bigcup_{S:x\notin S}I_S,
 \qquad
 A_p^{\max}=\{x:p\in Q_x\}.                                    \tag{4.7}
\]

Let

\[
 n_i^Q(x)=\min\bigl(Q_x\cap[i,N-1]\bigr)                        \tag{4.8}
\]

with the usual infinity convention, and put

\[
 \Theta_{i,q}^Q=\{x:n_i^Q(x)\le i+q\}.                          \tag{4.9}
\]

Then the marked system has one nonzero common-\(Q\) compiler if and only if

\[
 A_p^{\max}\ne\varnothing\quad(0\le p<N),                       \tag{4.10}
\]

\[
 \Theta_{i,d}^Q=T_i\quad(0\le i<W),                             \tag{4.11}
\]

and

\[
 \Theta_{i,q}^Q=S
 \quad\text{for every assigned }I_S=[i,i+q].                    \tag{4.12}
\]

When these conditions hold, the future partitions defined by \(n_i^Q\)
satisfy (2.4), and \(A^{\max}\) is the canonical realizing word.

#### Proof

Equation (4.7) is exactly the maximal common-\(Q\) word: the controller
enforces all central negative constraints and the deleted intervals enforce
all lower negative constraints.  Condition (4.10) is point nonemptiness.
By Lemma 2.2 applied to \(A^{\max}\), equations (4.11)--(4.12) are exactly
the central and lower pin equalities, including all positive hits.  These
three requirements are necessary and sufficient by the exact common-\(Q\)
criterion.  Theorem 2.1 gives the final assertion.  \(\square\)

In relative-deadline block notation the recurrence is

\[
\begin{aligned}
 B_i(0)&=A_i^{\max},\\
 B_i(t+1)&=B_{i+1}(t)\setminus A_i^{\max},\\
 B_i(\infty)&=B_{i+1}(\infty)\setminus A_i^{\max}.
\end{aligned}                                                    \tag{4.13}
\]

Thus Theorem 4.4 is a finite system of exact threshold identities on one
backward-MTF table.  It is strictly stronger than separate rankwise Hall,
but it contains no hidden owner choice.

## 5. Exact coordinate and Pascal lifts

The correct lift object is not just a set label.  It is a coordinate's whole
future-hit trajectory.

### Theorem 5.1 (ported coordinate insertion)

Let a timed table on `[k]` be fixed, adjoin a coordinate `z`, and choose a
physical support $H_z\subseteq[0,N-1]$.  Define

\[
 n_i'(z)=\min(H_z\cap[i,N-1]),
 \qquad n_i'(x)=n_i(x)\quad(x\in[k]).                            \tag{5.1}
\]

Inserting `z` into the timed block labelled `n_i'(z)` (or the infinity
block) at every state gives a valid future table.  Its physical letters are

\[
                         A_i'=A_i\cup(\{z\}\mathbf1_{i\in H_z}).\tag{5.2}
\]

For a prescribed binary middle tag word `tau_i`, this insertion realizes

\[
                         z\in T_i'\iff\tau_i=1                  \tag{5.3}
\]

if and only if

\[
                  \tau_i=\mathbf1[H_z\cap[i,i+d']\ne\varnothing]\tag{5.4}
\]

at the child deadline `d'`.  Equivalently, every internal one-run of `tau`
has length at least `d'+1`; the support is contained in the maximal eroded
tag controller; and on each internal eroded run it contains both forced
endpoints and has gaps at most `d'+1`, with the exact one-sided boundary
convention.

#### Proof

The new coordinate is independent of all old next-occurrence minima, so
(5.1) satisfies the recurrence of Theorem 2.1 coordinatewise.  Equations
(5.2)--(5.4) are definitions.  The final equivalence is Corollary 3.3 applied
to the binary coordinate row.  \(\square\)

Two coordinate insertions commute.  Thus the two new tags in a `k -> k+2`
Pascal lift can be pinned independently at the coordinate level; their
interaction occurs only through nonempty letters, the old-coordinate
ordered partitions, and seam placement.

Three useful special partition operations are:

\[
\begin{aligned}
 \mathsf L_z(\Pi)&=\Pi\text{ with }z\text{ in the infinity block},\\
 \mathsf U_z(\Pi)&=\Pi\text{ with }z\text{ in its first block},\\
 \mathsf V_z(\Pi)&=\{z\}|\Pi.
\end{aligned}                                                     \tag{5.5}
\]

They correspond respectively to no future `z`, a `z` occurrence now, and a
single prepended seam occurrence.  If `Pi_i=M_(A_i)Pi_(i+1)`, then

\[
\boxed{
 \mathsf L_z(\Pi_i)=M_{A_i}\mathsf L_z(\Pi_{i+1}),
 \qquad
 \mathsf U_z(\Pi_i)=M_{A_i\cup\{z\}}\mathsf U_z(\Pi_{i+1}).}    \tag{5.6}
\]

Also

\[
                         \mathsf V_z(\Pi)=M_{\{z\}}\mathsf L_z(\Pi).
                                                                    \tag{5.7}
\]

These are the ordered-partition forms of the lower, upper, and bridge
copies.  On a finite tagged middle run, `U_z` applies only after the forced
left countdown collar in (3.13); using it from the first tagged middle state
would place `z` too early.

### Theorem 5.2 (Pascal sector identities with renewal decorations)

Let `k=2r-1` and adjoin `z`.  If `T` lists the parent rank-`r` row and
`widehat L^(1)` is a completed parent rank-`r-1` row, then the even child
middle deck is the disjoint label union

\[
 \boxed{
 \binom{[k]\cup\{z\}}r
 =T\ \sqcup\
   \bigl(\{z\}+\widehat L^{(1)}\bigr).}                          \tag{5.8}
\]

If two coordinates `x,y` are adjoined, and `U_*` contains one selected copy
of every parent rank-`r+1` label, then the odd child deck is

\[
\boxed{
 \binom{[k]\cup\{x,y\}}{r+1}
 = (\{x,y\}+\widehat L^{(1)})
   \sqcup(\{x\}+T)\sqcup(\{y\}+T)\sqcup U_*.}                   \tag{5.9}
\]

Inside each uncut sector, any timed renewal path for the old row transports
by Theorem 5.1.  New-coordinate runs transport precisely when their ported
supports satisfy (5.4).  Therefore the only additional literal gates are:

1. ordering/completing `widehat L^(1)` and `U_*` as timed renewal paths;
2. satisfying the backward MTF equation at every cross-sector seam;
3. replacing every marked prefix occurrence destroyed by the cuts; and
4. regenerating the same data for the next lift.

#### Proof

The label identities partition a child set by its intersection with the new
coordinate set.  The renewal statement is Theorem 5.1 applied sectorwise.
An internal table equation remains unchanged under fixed tags by (5.6), so
only the listed interfaces can fail.  \(\square\)

This theorem is the exact reconciliation: Pascal supplies the child labels;
the renewal table supplies the one physical chronology.  Neither statement
substitutes for the other.

## 6. Exact seam and safe-cut criteria

A **renewal port** at a proposed seam records:

1. the two timed ordered partitions on the seam sides;
2. the physical first block used at the join;
3. the complete child central collar through its declared radius;
4. every marked threshold-prefix occurrence meeting that collar; and
5. the new-coordinate support bits and forced endpoints from (3.12).

### Lemma 6.1 (literal seam criterion)

Suppose two oriented timed paths are internally valid.  Their concatenation
is one future table if and only if, at each join position `p`,

\[
                         \boxed{\Pi_p=M_{A_p}(\Pi_{p+1}).}       \tag{6.1}
\]

If (6.1) holds at all joins, all uncut interval prefixes remain literal in
one word.  The central deck, residence, and marked prefixes need be checked
only in the declared seam collars.

#### Proof

Internal equations already give (2.4) away from joins.  Adding (6.1) gives
(2.4) everywhere, so Theorem 2.1 produces one global word.  Any interval not
meeting a changed boundary has the same ordered physical letters.  The
remaining assertions are therefore collar-local, although the availability
of replacement addresses is a global matching question.  \(\square\)

The last clause matters: exact ordered-partition stitching pays common-`Q`,
but it does not by itself prevent two targets from claiming the same cell.

Let `D` be the family of marked targets whose chosen prefix cells are
destroyed by a proposed cut/selector, after every unaffected assigned cell
has been reserved.  For `S in D`, let `A(S)` be the set of unreserved final
threshold cells, including seam cells, whose literal value is `S`.

### Lemma 6.2 (marked-prefix replacement Hall)

The cut preserves an injective marked occurrence of every target in `D` if
and only if

\[
 \boxed{
 \left|\bigcup_{S\in X}\mathcal A(S)\right|\ge|X|
 \quad\text{for every }X\subseteq D.}                           \tag{6.2}
\]

When (6.1) also holds, every replacement selected by (6.2) is automatically
compatible with the same common-`Q` word.

#### Proof

Equation (6.2) is Hall's theorem for the target/final-cell incidence graph.
Every incident cell is an actual prefix in the final future table, so
Theorem 4.2 applies to their union with the unaffected pins.  \(\square\)

This is the relational safe-cut invariant.  A scalar multiplicity reserve
does not imply (6.2), and the standard Catalan `A` forest has no uniform
one-occurrence surplus after its `b-1` cuts.

### Theorem 6.3 (adjacent-face canonical gluing)

Let a child have deadline \(e\), and partition its central chronology into
Pascal sectors.  In sector \(\sigma\), suppose the ordinary labels, before
orientation, are

\[
 Z_\sigma\cup\iota_\sigma\!\left(L_T^{(a_\sigma)}(i)\right),     \tag{6.3}
\]

where \(Z_\sigma\) is a fixed tag set and \(\iota_\sigma\) is a coordinate
embedding.  Let \(c\) range over the central cuts between sectors.  The
controller positions whose defining \(e+1\) central states meet both sides
of the cut are exactly

\[
                         E_c=[c,c+e-1].                          \tag{6.4}
\]

Put \(E=\bigcup_cE_c\).  Declare a marked cell exceptional if it is not the
transport of one parent-face mark or if its physical interval meets \(E\),
and put

\[
 \mathcal C=E\cup
       \bigcup_{\mu\ {\rm exceptional}} I_\mu.                   \tag{6.5}
\]

Assume:

1. off \(E\), the child controller is the transported face controller; in a
   forward sector,

   \[
   P^+_{i+e}
      =Z_\sigma\cup
        \iota_\sigma\!\left(L_T^{(a_\sigma+e)}(i)\right),         \tag{6.6}
   \]

   with the reflected formula in a reversed sector;
2. all nonexceptional marks are distinct transported parent marks, and for
   every coordinate the eligible forbidden-position profile off
   \(\mathcal C\) is exactly transported from the corresponding parent
   partial chart;
3. the **one global** child \(Q_x\), computed from all sector marks
   simultaneously, satisfies every affected central and pin-positive hit
   on \(\mathcal C\), and every point of \(\mathcal C\) has a nonempty
   \(Q\)-core;
4. the child central transitions are Johnson/resident and the separate
   upper-support ledger is complete.

Then the global child marks and controller form the canonical maximal-\(Q\)
renewal table of Theorem 4.4.  In particular, the child has one literal
common-\(Q\) compiler; no extra inter-sector owner choice remains.

#### Proof

A controller position \(p\) is defined by the central indices
\([p-e,p]\).  This interval crosses the cut at \(c\) exactly when
\(c\le p\le c+e-1\), proving (6.4).  Away from those positions,
intersection commutes with the fixed tag and embedding:

\[
\begin{aligned}
\bigcap_{h=0}^{e}
 \left(Z_\sigma\cup\iota_\sigma(L_T^{(a_\sigma)}(i+h))\right)
 &=Z_\sigma\cup\iota_\sigma
      \left(\bigcap_{h=0}^{e}L_T^{(a_\sigma)}(i+h)\right)\\
 &=Z_\sigma\cup
      \iota_\sigma(L_T^{(a_\sigma+e)}(i)),
\end{aligned}                                                     \tag{6.7}
\]

which is (6.6).

Hypotheses 1--2 transport the canonical \(Q\)-table and every ordinary mark
away from \(\mathcal C\).  Hypothesis 3 checks exactly the central hits, pin
hits, and nonzero points not covered by that transport.  Theorem 4.4
therefore gives the global word.  Hypothesis 4 pays the remaining
middle/upper carrier requirements.  \(\square\)

For one interior cut, every threshold cell of depth at most \(e\) affected
by (6.4) lies in the physical collar

\[
                         [c-e,c+2e-1],                           \tag{6.8}
\]

and their total number is at most

\[
                         \sum_{q=0}^{e}(e+q)
                         =\frac32e(e+1).                         \tag{6.9}
\]

This is a bounded audit once the exceptional marks are named.  It is not a
proof that their simultaneous global \(Q\)-cores exist.

There is also an orientation caveat.  Reversing a physical sector exchanges
future and past occurrence data.  A reversed future partition is not the
old future partition read backwards.  One must store both oriented germs or
recompute the reversed states from the transported \(Q_x\).

### Corollary 6.4 (exact Pascal depth demand)

In the odd-to-even decomposition (5.8), the untagged \(T\) sector has
\(a_\sigma=0\) and needs the parent face \(L^{(e)}\), while the
\(\{z\}+L^{(1)}\) sector has \(a_\sigma=1\) and needs
\(\{z\}+L^{(e+1)}\).  Hence:

- if \(e=d_{\rm parent}-1\), the existing parent depth-\(d_{\rm parent}\)
  stack is exactly sufficient;
- if \(e=d_{\rm parent}\), one genuinely new face
  \(L^{(d_{\rm parent}+1)}\) is required.

For the two-coordinate lift (5.9), the \(xy+L^{(1)}\) sector needs face
depth \(e+1\), the \(x+T\) and \(y+T\) sectors need depth \(e\), and the
selected \(U_*\) sector is not a transported lower face at all: it must
carry its own partial renewal chart.

#### Proof

Substitute \(a_\sigma=0,1\) into (6.6).  The \(U_*\) statement follows
because choosing one occurrence of every upper label does not preserve the
natural order of \(U^{(1)}\).  \(\square\)

### Lemma 6.5 (exact tag-omission resource)

Fix a new coordinate \(z\) and one maximal internal run

\[
                         R=[u,v]                                 \tag{6.10}
\]

of \(z\) in the child controller.  Let

\[
 Z_0=\bigcup_{\mu:\ z\notin S_\mu}I_\mu                         \tag{6.11}
\]

be the union of all marked intervals whose labels omit \(z\).  Then

\[
                         Q_z\cap R=R\setminus Z_0.               \tag{6.12}
\]

Central feasibility on this run is equivalent to:

1. \(u,v\notin Z_0\);
2. every connected component of \(Z_0\cap R\) has at most \(e\) positions.

Every marked target containing \(z\) must additionally have its interval
meet \(R\setminus Z_0\).  A marked target omitting \(z\) imposes only its
negative deletion on that interval.

#### Proof

Equation (6.12) is the definition of the maximal common-\(Q\) support on the
tag controller.  The controller endpoint/gap theorem says precisely that
the first and last \(Q_z\) pins survive and consecutive pins have gap at most
\(e+1\).  Deleting a consecutive block of \(\ell\) positions creates a pin
gap \(\ell+1\), giving conditions 1--2.  The last assertion is the positive
pin condition.  \(\square\)

Thus a nominal tagged sector need not put \(z\) in every physical letter.
It can host targets omitting \(z\) in gaps of length at most \(e\) between
the forced tag pins.  This is the exact one-dimensional signature-braid
resource.

The face charts in this corollary are only partial transport charts.  The
lower marked assignment must remain global across sectors.  Indeed, in the
depth-drop case \(e=d_{\rm parent}-1\), minimality of the parent deadline
gives

\[
 \Lambda_{\rm parent}>
 eW+\binom{e+1}{2},                                             \tag{6.13}
\]

the entire short-cell capacity of one length-\(W+e\) face.  Thus lower
targets of one signature cannot all be confined to that nominal face;
cross-face physical intervals are arithmetically necessary.

## 7. One precise inductive invariant

The fixed-dimension frame of Definition 4.1 is enough for the formula but is
not closed under Pascal lifting.  The following strengthened object records
exactly the missing interfaces.

### Definition 7.1 (regenerative Pascal--renewal frame)

At an odd dimension `k=2r-1`, a **regenerative Pascal--renewal frame**
`RPRF(k)` consists of:

1. **A literal parent frame.**  An `RCF(k)` with its chosen injective marked
   lower prefixes and upper witnesses.
2. **A coherent adjacent-face stack.**  Partial timed renewal charts for the
   completed first lower row `widehat L^(1)`, the middle row `T`, and every
   lower face required by Corollary 6.4, plus an independent partial chart
   for a selected complete upper row `U_*`.  Every protected all-depth
   occurrence is recorded by its full source support; lower target marks are
   not assigned separately by face.
3. **Exact Pascal sector data.**  Specified cuts, orientations, and sector
   orders for (5.8) and (5.9), together with supports for the new coordinates
   satisfying (5.4).
4. **Full renewal ports.**  Every sector join satisfies (6.1), every
   exceptional collar passes Theorem 6.3 using one global common-`Q` table,
   every child central collar has the required rank and residence, and its
   zero-time first blocks contain the forced pair (3.10).
5. **A marked safe-cut matching.**  After the Catalan deletions, `X/Y` cuts,
   and `U` selection, every destroyed protected occurrence passes the exact
   replacement Hall system (6.2).  The final child threshold cells cover its
   whole lower ideal, and its consecutive middle unions cover its upper
   ideal.
6. **Declared absolute radius.**  Residence, completed endpoint flags, timed
   renewal ports, and marked prefix data are carried through an absolute
   radius `R>=d(k)`; all one-sided boundary data are included.
7. **Regeneration.**  The odd child produced by (5.9) contains another
   adjacent-face stack, safe-cut matching atlas, full renewal-port atlas, and
   declared radius satisfying items 1--6 for the next lift.

Items 1--6 are a one-step certificate.  Item 7 is the genuine inductive
content.  In particular, “the child happens to be universal” is not accepted
as regeneration unless the named future cut/selector and port data are also
present.

### Theorem 7.2 (exact conditional Pascal induction)

Suppose there is an odd base dimension `k_0` with an `RPRF(k_0)`, and suppose
the specified constructions have the following hereditary property for
every reachable odd frame:

1. (5.8) produces an `RCF(k+1)` at deadline `d(k+1)` and length `B(k+1)`;
2. (5.9) produces an `RPRF(k+2)` at deadline `d(k+2)` and length `B(k+2)`.

Then

\[
                         \boxed{\nu(j)=B(j)}                    \tag{7.1}
\]

for every `j>=k_0`.

#### Proof

Induct through the odd dimensions using item 2.  At each odd frame, item 1
supplies the intervening even frame.  Definition 7.1, Lemmas 6.1--6.2, and
Theorem 4.2 give one literal common-`Q` word of the exact claimed length at
each stage.  The deadline lower bound supplies equality.  \(\square\)

The theorem is not circular: the output must be obtained by the explicit
sector functors, renewal-port equations, and marked replacement matching.
What remains open is the existence of that hereditary construction.

## 8. Why a static Pascal buffer is not this invariant

Let an odd parent have deadline `d` and absolute declared radius

\[
                         R=d+\beta.                              \tag{8.1}
\]

Passing from a row to its natural first lower row consumes one absolute
renewal/flag/port level:

\[
                         R\longmapsto R-1.                       \tag{8.2}
\]

Indeed, a child depth-`q` lower flag of `L^(1)(T)` is the parent depth-`q+1`
flag, and a parent coordinate run loses one position under first-shadow
erosion.  The loss is sharp on a minimum-length run.

For the odd-to-even step, write

\[
 e=d(2r)=d-\delta,
 \qquad \delta\in\{0,1\}.                                      \tag{8.3}
\]

Raw transport through the lower shore gives

\[
                         \boxed{\beta_e^{\rm tr}=\beta+\delta-1.}\tag{8.4}
\]

For the odd `k -> k+2` step, write

\[
 d^+=d+\epsilon,
 \qquad \epsilon\in\{0,1\}.                                   \tag{8.5}
\]

The `A={x,y}+L^(1)` sector is the bottleneck and gives

\[
                         \boxed{\beta_+^{\rm tr}=\beta-1-\epsilon.}\tag{8.6}
\]

After `n` raw two-coordinate lifts,

\[
 \beta_n\le\beta_0-n-(d_n-d_0).                                \tag{8.7}
\]

Thus no finite collection of finite scalar-buffer bases supports all
dimensions by raw adjacent-row transport.

There is an independent occurrence obstruction.  In the standard odd
`k -> k+2` lift, the Catalan `A` sector has

\[
                         b=C_r                                  \tag{8.8}
\]

components after deleting exactly `b-1` repeat edges.  Every retained
both-new first-shadow target then has one internal occurrence, and the
cross-sector seams have the wrong tag to duplicate it.  Hence no invariant
requiring a uniform spare occurrence is closed even for one lift.

Equations (8.6)--(8.8) explain clauses 5--7 of `RPRF`: a successful lift must
create

\[
                         1+\epsilon                              \tag{8.9}
\]

new radius units, use a cut-specific replacement matching rather than a
minimum multiplicity, and regenerate another aligned atlas.  Those are
theorems forced by the lift, not optional strengthening.

## 9. The exact remaining construction theorem

The general formula is reduced, within this architecture, to the following
single statement.

> **Aligned regenerative renewal theorem (open).**  For every reachable odd
> `RPRF(k)`, choose the `b-1` Catalan `A` deletions, the `X/Y` cuts, the `b`
> omitted `U` indices, the sector order, and the new-coordinate renewal
> supports so that:
>
> 1. the assembled child has exactly `W_child+d_child` physical positions,
>    and every join satisfies the full timed equation (6.1);
> 2. every new-coordinate tag run satisfies the forced endpoint and gap
>    conditions (3.12)--(3.13) and the omission criterion of Lemma 6.5;
> 3. every destroyed marked lower or upper occurrence has an injective final
>    replacement satisfying (6.2);
> 4. one global marked-threshold assignment across all sectors passes
>    Theorems 4.4 and 6.3; the child central cells are exactly the Pascal deck,
>    and its consecutive middle unions cover the upper ideal;
> 5. the odd child contains another atlas with the same clauses at its new
>    deadline.

If this theorem is proved from a finite odd base family, Theorem 7.2 proves
`nu(k)=B(k)` in every subsequent dimension.  It is stronger than separate
Pascal label transport, separate Hall matchings, or separate coordinate
pinning, but it is precisely strong enough to produce the common physical
compiler.

## 10. Proved/conditional boundary

Proved here:

1. timed next-occurrence partitions are exactly backward MTF trajectories;
2. their threshold prefixes are exactly the contiguous-OR cells;
3. middle Johnson transitions force both run-boundary ports with the exact
   `d`-offset;
4. `RCF(k)` is equivalent to a literal optimum inside the flat architecture;
5. every marked prefix family in one future table automatically passes the
   exact common-`Q` criterion;
6. new-coordinate Pascal tags lift by coordinate renewal supports, with the
   forced collar stated exactly;
7. full ordered-partition seam equations plus marked replacement Hall are
   sufficient for literal composition;
8. `RPRF` is an exact hereditary invariant implying the formula;
9. raw finite-radius or uniform-occurrence buffers cannot be that invariant.

Unproved:

1. the aligned regenerative renewal theorem of Section 9;
2. existence of `RPRF(k)` for an unbounded sequence of odd dimensions;
3. an unconditional length-`6438` word for `k=15`;
4. the all-`k` equality `nu(k)=B(k)`.

The invariant is intentionally literal.  Any weaker proposal which forgets
the timed seam state, replaces (6.2) by a scalar reserve, or chooses lower
rows independently no longer implies common-`Q`.
