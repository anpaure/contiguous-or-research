# Overlap tag current and the zero-drift star normal form

**Date:** 2026-08-07  
**Method:** suffix containment and telescoping tag rank  
**Status:** unconditional local reduction.  It identifies the exact history
interface which can evade the bounded-tag monotonicity obstruction: a dense
component must use zero-current swaps or explicitly priced negative-current
reset events.

## 1. Event current

Let (A=(A_1,\ldots,A_L)) be a cyclic word, fix a coordinate bank
(D\subseteq[n]), and fix a depth (d).  A chart event terminating at
position (e) has

\[
 F_e=\left(\bigcup_{p=e-d}^{e-1}A_p\right)\cap D,
 \qquad
 G_e=A_e\cap D.                                          \tag{1.1}
\]

Thus (F_e) is the tag signature of the first rail's deepest target and
(G_e) is the tag signature of the second rail's bottom target.  Define
the event's **tag current** by

\[
                         \delta_e=|G_e|-|F_e|.             \tag{1.2}
\]

No fixed-signature hypothesis is imposed.

## 2. The telescoping law

### Theorem 2.1 (overlap tag current)

Let (e_1<e_2<\cdots<e_h) be chart terminals in one linearized portion of
the word, and suppose

\[
                         1\le e_{i+1}-e_i\le d             \tag{2.1}
\]

for every (i<h).  Then

\[
                         G_{e_i}\subseteq F_{e_{i+1}}      \tag{2.2}
\]

and

\[
 \boxed{
   \sum_{i=1}^{h-1}\delta_{e_i}
       \le |F_{e_h}|-|F_{e_1}|\le |D|.}                   \tag{2.3}
\]

#### Proof

Condition (2.1) puts the terminal letter (A_{e_i}) inside the (d)-letter
window (A_{e_{i+1}-d},\ldots,A_{e_{i+1}-1}).  Intersecting with (D)
gives (2.2).  Hence

\[
 |F_{e_{i+1}}|\ge |G_{e_i}|
                  =|F_{e_i}|+\delta_{e_i}.
\]

Sum these inequalities over (i).  The (F)-terms telescope, and both
endpoint ranks lie between (0) and (|D|). \(\square\)

### Corollary 2.2 (reset accounting)

Let (P) be the number of events among (e_1,\ldots,e_{h-1}) with
(\delta_e\ge1), and put

\[
 R=-\sum_{i=1}^{h-1}\min\{\delta_{e_i},0\}.
\]

Then

\[
                         \boxed{P\le |D|+R.}              \tag{2.4}
\]

In particular, if every event has current at least one, one overlap
component contains at most (|D|+1) events.  More generally, every positive-
current birth beyond the bounded initial bank must be paid by negative
current somewhere in the same component.

The fixed-separator two-rail packet has

\[
 F=E,\qquad G=E\cup\{b\},\qquad\delta=1,                 \tag{2.5}
\]

which recovers the monotone-signature mechanism behind the bounded-tag
no-go.

## 3. A literal zero-current chart

Let the source core be (K=E\mathbin{\dot\cup}Q), where
(E\subseteq D) and (Q\cap D=\varnothing).  Choose distinct

\[
 a,b\in D\setminus E,
 \qquad c_1,\ldots,c_{d-1}\notin D\cup Q,
\]

and use the (d+1) common-core letters

\[
 K\cup\{c_{d-1}\},\ldots,K\cup\{c_1\},
 K\cup\{a\},K\cup\{b\}.                               \tag{3.1}
\]

The last two endpoints are full.  Their depth-(j) targets are

\[
 \begin{aligned}
 T_{0,j}&=K\cup\{a,c_1,\ldots,c_{j-1}\},\\
 T_{1,1}&=K\cup\{b\},\\
 T_{1,j}&=K\cup\{b,a,c_1,\ldots,c_{j-2}\}
                         \qquad(2\le j\le d).
 \end{aligned}                                           \tag{3.2}
\]

Every row is a saturated chain of ranks (|K|+j).  In the notation of
(1.1),

\[
                         F=E\cup\{a\},
 \qquad G=E\cup\{b\},
 \qquad\boxed{\delta=0}.                                 \tag{3.3}
\]

Thus replacing (a) by (b), rather than inserting (b) above a fixed
signature, is the smallest literal interface which evades strict tag-rank
growth.

## 4. Equality forces a tag-state walk

### Corollary 4.1 (zero-current overlap normal form)

Suppose consecutive overlapping events all satisfy

\[
                         |F_e|=|G_e|=h.                    \tag{4.1}
\]

Then

\[
                         \boxed{G_{e_i}=F_{e_{i+1}}}       \tag{4.2}
\]

for every adjacent pair of events.

#### Proof

Equation (2.2) is an inclusion between two (h)-sets, so it is equality.
\(\square\)

Consequently a dense zero-current component is not a collection of
independent separator insertions.  Its tag signatures form a directed walk

\[
                         F_1\longrightarrow F_2\longrightarrow\cdots,
 \qquad G_i=F_{i+1},                                      \tag{4.3}
\]

and a one-swap chart such as (3.1) makes this a Johnson walk on a fixed tag
layer.  The required all-depth condition is precisely the residence rule
that every (j)-event suffix gains one fresh coordinate for
(1\le j\le d).

## 5. Consequence for the general programme

The multiseparator hypercube construction solves static target packing but
uses only (+1)-current events.  Theorem 2.1 proves that adding further
bounded separator shores cannot fix its history problem.  A successful
physical replacement must provide one of the following, explicitly:

1. a zero-current resident tag-state walk with a simultaneous all-depth
   target factor;
2. negative-current reset events whose total current pays every positive
   birth, with their physical cells and target casualties included; or
3. a packet whose distinguishing state is not represented by persistent OR
   coordinates in the overlapping (d)-history.

This is a reduction, not a proof of the resettable packet theorem or of
(\nu(k)\le B(k)+O(1)).

