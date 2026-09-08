# Collar-neutral re-rooting gives linear local rectangle reuse

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\) and \(m\ge6H+4\). For a top \(U\) and a full
injective word \(p=(p_1,\ldots,p_M)\), let

\[
 \mathcal D_h(U,p)=
 \sum_{i=1}^{d}
 e_{\,U\setminus\{p_i,\ldots,p_{i+h-1}\}}
 \qquad(0\le h\le2H).
\tag{0.2}
\]

The fixed-root rectangle option graph is a union of \(K_2\)'s, so it
has only one net unit of middle action per top. Allowing literal
re-rooting changes the answer at the **local capacity** level.

### Theorem A (exact four-top recharge)

For every top \(U\) and every current word \(p\) on \(U\), there are
three further tops \(U_1,U_2,U_3\) and source words on them such that
simultaneously replacing all four words by their one-step left cyclic
rotations has

\[
 \boxed{
 \sum_{i=0}^{3}
 \bigl(\mathcal D_h(U_i,rp_i)-\mathcal D_h(U_i,p_i)\bigr)=0
 \quad(0\le h\le2H),}
\tag{0.3}
\]

where \(U_0=U\). Thus the recharge changes the intrinsic boundary orbit
on every participating top while preserving **every** protected trace
in aggregate, including the middle trace. It is an open four-top move,
not a closed one-top conjugation. The endpoint words generally have
different invisible final \(2H\)-sets, so this is an all-core or
dynamic-core move rather than a fixed-core-preserving one.

### Theorem B (exact cyclic-root direction rank)

Let \(s\) swap the first two letters and let \(r\) be left cyclic
rotation. On one fixed top put \(T=rs\). The \(T\)-orbit of a word has
length \(M-1\). At its \(M-1\) successive states, the focal middle
derivatives of the boundary swaps are pairwise support-disjoint and
hence linearly independent. Therefore

\[
 \boxed{\operatorname{rank}_{\rm cyclic}(U)=M-1=\Theta(m).}
\tag{0.4}
\]

This is the maximum possible rank inside this particular cyclic-tail
orbit because the orbit contains exactly \(M-1\) rooted states.
Across all arbitrary root and tail choices, the abstract directional
rank is much larger and is exactly \(\binom MH-1\); this latter count
does not by itself give a literal chronology.

### Theorem C (literal constant-fraction installation)

Let

\[
 r_*=\left\lfloor {m-H-6\over8}\right\rfloor.
\tag{0.5}
\]

Starting from an arbitrary word on one focal top \(U\), one can execute
\(r_*\) collar-neutral two-top rectangles on \(U\), inserting after each
one a four-top recharge from Theorem A, such that

1. the \(r_*\) focal middle unit directions are linearly independent;
2. every intermediate state has exactly one literal word at every top;
3. the aggregate derivative at every nonmiddle protected length is zero;
4. every rectangle and every recharge is chronologically applicable;
   and
5. all auxiliary tops can be chosen fresh.

Hence the re-rooted literal option system has

\[
                       \boxed{\Theta(m)}
\tag{0.6}
\]

sequentially installable independent rectangle directions per chosen
focal top. Chronology does **not** impose an \(O(H)\), \(O(1)\), or
\(K_2\) local ceiling after open collar-neutral re-rooting is admitted.

There is still a global resource gate. The construction of Theorem C
uses four fresh auxiliary tops per focal rectangle: one rectangle
companion and three recharge helpers. Applied independently to many
focal tops, it therefore has only constant average reuse over all used
tops. It does not yet supply the required \(\Theta(m)\) average reuse
over the \(N\sim W/m\) available tops. The exact remaining problem is
to pack the four-top recharges so that their helper tops are themselves
reused as focal tops in later rounds.

The note also proves a complementary rigidity statement: a re-rooting
cannot be collar-neutral on one top by itself. Equality of just the
length-\(1\) and length-\(2H\) decks already forces equality of the
entire visible word and hence of the middle deck. Aggregate multi-top
cancellation in (0.3) is essential.

## 1. One-top collar neutrality cannot recharge a root

Let

\[
                         L=d+2H-1=m-H.
\tag{1.1}
\]

Only the visible prefix \(p_1,\ldots,p_L\) occurs in a protected deleted
interval. The final \(M-L=2H\) word positions are invisible to every
deck in (0.2).

### Lemma 1.1 (two nonmiddle decks determine the visible word)

If two words \(p,q\) on the same top satisfy

\[
                 \mathcal D_1(U,p)=\mathcal D_1(U,q),
 \qquad
                 \mathcal D_{2H}(U,p)=\mathcal D_{2H}(U,q),
\tag{1.2}
\]

then

\[
                         p_i=q_i\qquad(1\le i\le L).
\tag{1.3}
\]

Consequently

\[
                         \mathcal D_H(U,p)=\mathcal D_H(U,q).
\tag{1.4}
\]

#### Proof

Complementing inside \(U\), the length-\(2H\) deck is the unordered
family

\[
 J_i(p)=\{p_i,\ldots,p_{i+2H-1}\},
 \qquad1\le i\le d.
\tag{1.5}
\]

Its intrinsic intersection-\((2H-1)\) graph is \(P_d\). Indeed

\[
 |J_i(p)\cap J_j(p)|=\max\{0,2H-|i-j|\}.
\tag{1.6}
\]

Thus equality of the decks aligns their windows either in the same
order or in reverse order. Consecutive differences recover

\[
 \{p_t\}=J_t\setminus J_{t+1},\qquad
 \{p_{t+2H}\}=J_{t+1}\setminus J_t
 \quad(1\le t\le d-1).
\tag{1.7}
\]

Since \(d\ge2H+3\), the position ranges

\[
 [1,d-1]\quad\hbox{and}\quad[2H+1,d+2H-1]
\tag{1.8}
\]

cover \([1,L]\). Hence the visible word is determined up to reversal.

The length-\(1\) deck identifies the unordered set
\(\{p_1,\ldots,p_d\}\). Under reversal of the visible word, the first
\(d\) positions would instead be the old positions

\[
                         L-d+1,\ldots,L=2H,\ldots,L.
\tag{1.9}
\]

The index sets \([1,d]\) and \([2H,L]\) are different. Since all word
labels are distinct, their label sets are different. Equality of the
length-\(1\) decks therefore excludes reversal and proves (1.3).
Every length-\(H\) retained interval lies in the visible prefix, giving
(1.4). \(\square\)

### Corollary 1.2 (no top-local recharge)

If a one-top path replacement preserves every nonmiddle protected deck,
then it preserves the middle deck as well. Its only remaining freedom is
to reorder the invisible final \(2H\) letters, which changes no
protected deck.

Thus any useful collar-neutral root change must be open across at least
two tops. The construction below uses four.

## 2. The derivative of a one-step re-rooting

Let

\[
                         rp=(p_2,\ldots,p_M,p_1).
\tag{2.1}
\]

For \(h\ge1\), put

\[
 A_h(p)=\{p_1,\ldots,p_h\},\qquad
 B_h(p)=\{p_{d+1},\ldots,p_{d+h}\}.
\tag{2.2}
\]

The largest index in (2.2) is \(d+2H=m-H+1<M\), so no wrap occurs.

### Lemma 2.1 (endpoint telescoping)

For every \(1\le h\le2H\),

\[
 \boxed{
 \mathcal D_h(U,rp)-\mathcal D_h(U,p)
 =e_{U\setminus B_h(p)}-e_{U\setminus A_h(p)}.}
\tag{2.3}
\]

For \(h=0\), the derivative is zero.

#### Proof

The new interval at retained phase \(i\) is the old interval at phase
\(i+1\). All phases \(2,\ldots,d\) cancel telescopically. The only
survivors are the new interval with old start \(d+1\) and the old
interval with start \(1\), with the signs in (2.3). At \(h=0\), both
decks equal \(d e_U\). \(\square\)

## 3. Universal four-top full-trace recharge

We prove Theorem A in a form which accepts an arbitrary prescribed word
on one of the four tops.

### Theorem 3.1 (arbitrary-word four-cycle recharge)

Let \(p_0\) be any word on a top \(U_0\). There are distinct tops
\(U_1,U_2,U_3\) and words \(p_1,p_2,p_3\) for which (0.3) holds.

#### Proof

Write

\[
 \begin{aligned}
 v_3&=(p_0)_1,&
 A&=((p_0)_2,\ldots,(p_0)_{2H}),\\
 v_0&=(p_0)_{d+1},&
 B&=((p_0)_{d+2},\ldots,(p_0)_{d+2H}).
 \end{aligned}
\tag{3.1}
\]

The two displayed position blocks are disjoint, so the ordered
\((2H-1)\)-sets \(A,B\) are disjoint. Put

\[
                         C=U_0\setminus\{v_3,v_0\},
 \qquad |C|=M-2.
\tag{3.2}
\]

Choose two distinct labels

\[
                         v_1,v_2\notin C\cup\{v_3,v_0\}.
\tag{3.3}
\]

For indices modulo four, define

\[
                         U_i=C\cup\{v_{i-1},v_i\}.
\tag{3.4}
\]

Put

\[
                         F_0=F_2=A,\qquad F_1=F_3=B.
\tag{3.5}
\]

For \(i=1,2,3\), choose \(p_i\) so that its positions
\(1,\ldots,2H\) and \(d+1,\ldots,d+2H\) are respectively

\[
                         (v_{i-1},F_i),
 \qquad
                         (v_i,F_{i-1}).
\tag{3.6}
\]

Fill all remaining positions by an arbitrary order of
\(C\setminus(A\cup B)\). There are exactly

\[
 |C|-|A|-|B|=M-4H=d-1
\tag{3.7}
\]

remaining labels and the same number of remaining positions. Equations
(3.1) and (3.6) also describe the two relevant blocks of the prescribed
word \(p_0\); its other positions need not agree with the arbitrary
orders chosen on the helper tops.

Let \(F_i^{h-1}\) be the first \(h-1\) labels of \(F_i\). Lemma 2.1
gives the derivative on \(U_i\) as

\[
 e_{(C\setminus F_{i-1}^{h-1})\cup\{v_{i-1}\}}
 -
 e_{(C\setminus F_i^{h-1})\cup\{v_i\}}.
\tag{3.8}
\]

The positive term at \(i\) is the negative term at \(i-1\). Summing
cyclically proves zero for every \(1\le h\le2H\). The \(h=0\) case is
zero top by top. This proves (0.3). \(\square\)

### Remark 3.2 (why this escapes the closed chronology obstruction)

All four endpoint paths change. No helper is restored around a sole
unit transfer. The macro is therefore an open circulation of endpoint
flags, precisely the case not covered by the closed-companion theorem.

## 4. Linear independent rank along one re-root orbit

Fix a word

\[
                         p=(a,q_0,q_1,\ldots,q_{M-2})
\tag{4.1}
\]

on \(U\), with the \(q\)-indices read modulo \(M-1\). Let \(s\) swap
the first two positions and let \(T=rs\). Directly,

\[
 T^kp=(a,q_k,q_{k+1},\ldots,q_{k-1})
 \qquad(0\le k\le M-2).
\tag{4.2}
\]

Thus \(T\) fixes \(a\), cyclically rotates the other \(M-1\) labels,
and has orbit length \(M-1\).

At state \(T^kp\), the focal middle derivative of \(s\) is

\[
 g_k=
 e_{U\setminus B_k}-e_{U\setminus A_k},
\tag{4.3}
\]

where

\[
 A_k=\{q_k,q_{k+1},\ldots,q_{k+H-1}\},
\qquad
 B_k=\{a,q_{k+1},\ldots,q_{k+H-1}\}.
\tag{4.4}
\]

### Theorem 4.1 (support-disjoint cyclic directions)

The \(2(M-1)\) owner coordinates appearing in (4.3) are all distinct.
Consequently \(g_0,\ldots,g_{M-2}\) are linearly independent.

#### Proof

The \(A_k\) are the distinct cyclic \(H\)-arcs of the
\((M-1)\)-cycle \(q_0,\ldots,q_{M-2}\). The sets \(B_k\setminus\{a\}\)
are its distinct cyclic \((H-1)\)-arcs. Hence the \(A_k\)'s are
pairwise distinct and the \(B_k\)'s are pairwise distinct. No \(A_k\)
equals a \(B_l\), because \(a\notin A_k\) and \(a\in B_l\).
Complementation inside \(U\) preserves distinctness.

Each vector \(g_k\) therefore has two coordinates which occur in no
other \(g_l\). The vectors are support-disjoint and linearly
independent. \(\square\)

### Proposition 4.2 (full rooted-tail direction rank)

Let

\[
                         \Omega_U=\binom Um.
\tag{4.5}
\]

If arbitrary rooted words and tail orders on \(U\) are admitted, their
boundary-swap middle directions span exactly

\[
 \left\{z\in\mathbb Z^{\Omega_U}:\sum_{X\in\Omega_U}z_X=0\right\}.
\tag{4.6}
\]

Consequently the maximum abstract linear rank of all rooted-tail
boundary directions on one top is

\[
                         \boxed{\binom MH-1.}
\tag{4.7}
\]

#### Proof

Let \(X,Y\in\Omega_U\) be Johnson-adjacent. Their complementary
\(H\)-sets have the form

\[
                         U\setminus X=C\cup\{v\},
 \qquad
                         U\setminus Y=C\cup\{u\},
\tag{4.8}
\]

where \(|C|=H-1\). Choose a rooted word whose first \(H+1\) positions
are

\[
                         (u,v,C)
\tag{4.9}
\]

in any order on \(C\). Its phase-two deleted \(H\)-set is
\(C\cup\{v\}\); after the first-two swap it is
\(C\cup\{u\}\). The middle derivative is therefore \(e_Y-e_X\).

Every Johnson edge is realizable. Since the Johnson graph on
\(\Omega_U\) is connected, its oriented edge differences span the
complete zero-total lattice, whose rank is
\(|\Omega_U|-1=\binom MH-1\). \(\square\)

Proposition 4.2 is only a signed catalogue-rank statement. Theorem 5.2
below is the conformal chronological result: it certifies a linear,
not exponential, number of these directions in one literal route.

This proves Theorem B. Notice that the focal word returns after \(M-1\)
swap--re-root rounds. There is no contradiction with the independent
focal ledger: the intervening re-rootings have nonzero one-top middle
derivatives whose compensating derivatives are carried by the helper
tops, even though every recharge has zero aggregate trace.

## 5. Literal installation of a linear number of rounds

We use two facts.

First, every current word \(w=(u,v,x,\ldots)\) supports a literal
two-top collar-neutral rectangle. Choose any \(y\notin U\), put
\(V=U-\{x\}+\{y\}\), and use the companion word from the exact two-top
construction. The focal action is \(w\to sw\).

Second, Theorem 3.1 re-roots the resulting word \(sw\) to \(rsw=Tw\)
using three helper tops.

It remains only to ensure that the auxiliary tops can be chosen fresh.

### Lemma 5.1 (fresh helper choice)

Suppose at most \(4k\) auxiliary tops have previously been used and

\[
                         8k+7<m-H+2.
\tag{5.1}
\]

Then round \(k\) can choose one new rectangle companion and three new
recharge helpers, all distinct from the focal top and all earlier
auxiliaries.

#### Proof

For the rectangle, the position-\(3\) label \(x\in U\) is fixed. There
are

\[
                         2m-M=m-H
\tag{5.2}
\]

choices of \(y\notin U\), producing distinct tops
\(U-\{x\}+\{y\}\). Since \(4k<m-H\) under (5.1), one is fresh.

For the recharge, use the notation of Theorem 3.1 and put

\[
                         Q=[2m]\setminus C,\qquad
                         |Q|=m-H+2.
\tag{5.3}
\]

A top containing \(C\) is an edge of the complete graph on \(Q\).
Mark as forbidden the focal top, the new rectangle companion if it
contains \(C\), and every earlier auxiliary top which contains \(C\).
There are at most

\[
                         F\le4k+2
\tag{5.4}
\]

forbidden edges.

The recharge helpers must be the three edges of a path

\[
                         v_0-v_1-v_2-v_3
\tag{5.5}
\]

with fixed distinct endpoints \(v_0,v_3\). Choose \(v_1\) so that
\(v_0v_1\) is not forbidden. Then choose \(v_2\), distinct from the
other vertices, so that neither \(v_1v_2\) nor \(v_2v_3\) is forbidden.
The number of excluded choices for \(v_2\) is at most

\[
                         2F+3\le8k+7<|Q|.
\tag{5.6}
\]

The same inequality also leaves a choice of \(v_1\). The three helper
tops are therefore fresh. \(\square\)

### Theorem 5.2 (linear fresh-helper chronology)

There is a literal chronology of \(r_*\) rectangle rounds satisfying
all five conclusions of Theorem C.

#### Proof

At round \(k\), the focal word is \(T^kp\). Apply its two-top boundary
rectangle, then apply Theorem 3.1 to the resulting focal word
\(sT^kp\). The focal endpoint is

\[
                         rsT^kp=T^{k+1}p.
\tag{5.7}
\]

Choose every auxiliary top fresh using Lemma 5.1. For
\(0\le k<r_*\), definition (0.5) gives (5.1). Thus every advertised
source word can be installed initially on its unique auxiliary top and
remains untouched until its move. Each step is chronologically
applicable and maintains one word per top.

Every rectangle has zero aggregate derivative at \(h\ne H\). Every
recharge has zero aggregate derivative at all \(h\), by Theorem 3.1.
The entire chronology therefore preserves every nonmiddle trace in
aggregate. Its focal rectangle directions are
\(g_0,\ldots,g_{r_*-1}\), which are independent by Theorem 4.1.
\(\square\)

The construction uses exactly \(4r_*\) auxiliary tops in addition to
the focal top.

## 6. Independent audit of the decisive identities

There are three places where a false cancellation could enter.

### 6.1 Re-rooting signs

Under left rotation, new retained phase \(i\) is old phase \(i+1\).
Hence the new far-end window has sign \(+\), while the removed first
window has sign \(-\). In the four-cycle construction this gives

\[
 +(C\setminus F_{i-1}^{h-1})\cup\{v_{i-1}\},
 \qquad
 -(C\setminus F_i^{h-1})\cup\{v_i\}.
\tag{6.1}
\]

The positive coordinate at \(i\) is literally the negative coordinate
at \(i-1\), including the vertex label and the ordered filler prefix.
Thus cancellation is coefficientwise, not merely marginal.

### 6.2 Literal label count

On every recharge top the two protected endpoint blocks use

\[
                         2+2(2H-1)=4H
\tag{6.2}
\]

distinct labels. The top has \(M=m+H\) labels, so \(M-4H=m-3H=d-1\)
labels remain, exactly matching the unused word positions. No label is
repeated and no placeholder column is being counted twice.

### 6.3 Independence

For every \(k\), the negative owner in \(g_k\) contains the fixed label
\(a\), whereas the positive owner omits \(a\). Within either class the
deleted cyclic arcs have different starting points. Therefore no
coordinate can occur in two focal directions. This is stronger than a
rank computation and rules out cancellation among the advertised local
directions.

The fresh-helper argument is deliberately conservative. It proves only
a fixed positive fraction of the full \(M-1\) cyclic rank, but that is
already the required \(\Theta(m)\) local scale.

## 7. Exact boundary

Proved:

1. top-local preservation of the nonmiddle decks forces preservation of
   the middle deck;
2. an arbitrary current word admits a four-top, one-step, full-trace
   neutral re-rooting;
3. cyclic re-rooting enlarges the focal rectangle direction rank from
   one to exactly \(M-1\);
4. arbitrary rooted-tail directions have exact abstract rank
   \(\binom MH-1\);
5. a literal chronology installs at least
   \(\lfloor(m-H-6)/8\rfloor=\Theta(m)\) independent rectangle
   directions on one focal top;
6. every nonmiddle protected trace is preserved in aggregate throughout
   the construction; and
7. the decisive signs, label counts, support independence, and fresh-top
   inequalities have been audited separately.

Not proved:

1. simultaneous \(\Theta(m)\) average reuse over all
   \(N\sim W/m\) tops;
2. recycling the four-top helper paths so that helpers later become
   focal paths rather than fresh consumables;
3. a fixed-\(2H\)-core-preserving version of the re-root recharge;
4. a synchronized global schedule with \(o(W)\) owner-repeat excess;
5. squarefree middle ownership at every intermediate table; or
6. coefficient one.

Therefore the direct \(K_2\) option graph is not a local rank
obstruction once open re-rooting is admitted. The remaining obstruction
is global amortization of the exact four-top recharge, not the number of
independent rectangle directions available at one top.

## 8. Dependencies

The fixed-root \(K_2\) theorem and exact chronological option-flow
criterion are in
MATH_THEOREM_COLLAR_NEUTRAL_RECTANGLE_BANK_LITERAL_SPLICE_AND_INSTALLABILITY_20260727.md.

The two-top all-length rectangle identity is in
MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md
and independently in
MATH_THEOREM_TWO_TOP_BOUNDARY_RECTANGLE_AND_ORBIT_PARITY_NOGO_20260727.md.

The closed-companion chronology obstruction is in
MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md.
