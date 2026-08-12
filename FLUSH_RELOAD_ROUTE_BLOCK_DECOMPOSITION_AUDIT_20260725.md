# Flush/reload route blocks: exact trace characterization and decomposition audit

Date: 2026-07-25

## 0. Outcome

Let \(n=2Q\) and

\[
 d=2n+2=4Q+2.
\]

One flush/reload route has \(d-1=4Q+1\) updates and \(d\) state
occurrences.  Its trace has an exact finite fingerprint.

1. There are fixed sets
   \[
   C,\quad P,\quad D,
   \qquad |C|=m-3Q-1,\quad |P|=4Q+2,
   \quad |D|=H-Q-1,
   \]
   which partition the carrier, such that every flag column of the route
   lies in the Boolean interval \([C,C\cup P]\).
2. At upper depth \(Q\), the \(d\) route states are exactly
   \[
   C\cup(P-p),\qquad p\in P,
   \]
   once each.  Thus the route is a complete moving-label facet packet at
   that row.
3. A concatenation of route blocks is characterized by one fixed collar
   label set \(Z\) of size \(2Q\), a Johnson path of boundary cores in
   \(J(M-2Q,m-Q)\), and one ordered \(2Q\)-buffer choice on each skeleton
   edge.  This characterization is necessary and sufficient.
4. If \(t\) such blocks form an \(M\)-state path, then at least
   \[
   m-Q-t(2Q+1)=(1/2-o(1))m
   \]
   elements of the initial core occur in the lower core of **every** state
   of the path.  Also at least \(H-Q-t\) initial tail elements remain
   outside every state flag.  Hence route-block paths are a strict subclass
   of truncated rotor paths with a macroscopic common-core invariant.
5. The route-block versus upper-\(Q\)-target incidence matrix is not totally
   unimodular.  Three actual route blocks and three actual targets give the
   determinant-\(2\) triangle minor.

The uniform route process is nevertheless exactly fractional: a uniform
source state and symmetric route parameters give a uniform state at every
fixed connector phase, and the block-boundary chain has uniform stationary
measure.  Thus there is no fractional or scalar obstruction to selecting
about \(M/(4Q+1)\) blocks per top.  The missing theorem is an integral
route-path selection with balanced global flag and oriented-star loads.
Ordinary network TU cannot supply it, and an arbitrary balanced flag flow
cannot simply be regrouped into these route blocks because of the fixed
interval and boundary-collar invariants.

## 1. Exact moving-label interval of one route

Start from

\[
 \omega=(A;z_1,\ldots,z_n;B),
 \qquad |A|=m-Q,\quad |B|=H-Q.
\]

Choose distinct buffers

\[
 X=\{x_1,\ldots,x_n\}\subset A,
\]

an exchanged core label \(a\in A\setminus X\), and an exchanged tail
label \(b\in B\).  Put

\[
 Z=\{z_1,\ldots,z_n\},                              \tag{1.1}
\]

\[
 C=A\setminus(X\cup\{a\}),
 \qquad D=B\setminus\{b\},                         \tag{1.2}
\]

\[
 P=X\cup\{a,b\}\cup Z.                             \tag{1.3}
\]

Then

\[
 |C|=m-Q-(2Q+1)=m-3Q-1,                            \tag{1.4}
\]

\[
 |D|=H-Q-1,\qquad |P|=2(2Q)+2=4Q+2=d,             \tag{1.5}
\]

and \(U=C\sqcup P\sqcup D\).

No element of \(C\) is ever selected as a core buffer, and no element of
\(D\) is ever selected from the tail.  Therefore, at every state of the
route and every prefix rank \(0\le h\le2Q\),

\[
 \boxed{C\subseteq F_h\subseteq C\cup P.}           \tag{1.6}
\]

Since \(|F_h|=m-Q+h\), its moving part has the fixed size

\[
 |F_h\setminus C|=2Q+1+h.                           \tag{1.7}
\]

Thus a route block is a walk entirely inside one \(d\)-dimensional Boolean
interval, and its full flag trace is obtained by adjoining the fixed core
\(C\) to a reduced rotor trace on \(P\) with unordered block sizes

\[
 2Q+1,\quad 2Q,\quad1.                              \tag{1.8}
\]

## 2. Exact upper-\(Q\) and lower-\(Q\) traces

At upper depth \(Q\), the flag is the carrier minus its tail.  The fixed
tail part is \(D\), and exactly one moving label lies in the tail.

During the \(d\) state occurrences, that moving tail label is, in order,

\[
 b,z_n,z_{n-1},\ldots,z_1,x_1,x_2,\ldots,x_n,a.
 \tag{2.1}
\]

This list contains every element of \(P\) exactly once.  Consequently

\[
 \boxed{
 \{U_Q(\omega_s):0\le s<d\}
 =\{C\cup(P-p):p\in P\}.}                           \tag{2.2}
\]

Every upper-\(Q\) target in the block is distinct.  Their common
intersection is \(C\), and their union is \(C\cup P\).

The lower-\(Q\) moving core is a Johnson path of \((2Q+1)\)-subsets of
\(P\).  Put \(K_s=L_Q(\omega_s)\setminus C\).  Its exact list is

\[
 K_0=X+a,                                            \tag{2.3}
\]

and, for \(1\le s\le n\),

\[
 K_s=
 (X\setminus\{x_1,\ldots,x_s\})
 \cup\{a,b\}
 \cup\{z_{n-s+2},\ldots,z_n\},                    \tag{2.4}
\]

with an empty final set of \(z\)'s when \(s=1\).  At the flush endpoint,

\[
 K_{n+1}=Z+b.                                        \tag{2.5}
\]

If \(z'_1,\ldots,z'_n\) is the target collar order, then for
\(1\le r\le n\),

\[
 K_{n+1+r}
 =\bigl(Z\setminus\{z'_n,\ldots,z'_{n-r+1}\}\bigr)
  \cup\{b,x_1,\ldots,x_r\}.                        \tag{2.6}
\]

In particular

\[
 K_{2n+1}=X+b.                                       \tag{2.7}
\]

Equations (2.1)--(2.7), together with the reduced rotor recurrence, give
an exact ordered characterization of a single connector trace.

## 3. Exact characterization of concatenated route blocks

Consider a sequence of flush/reload blocks with no reset between them.
At the end of one route the collar is a permutation of the same label set
\(Z\) with which that route began.  Hence the collar label set is fixed at
every block boundary throughout the concatenation.

Let the boundary state before block \(j\) be

\[
 \omega_j=(A_j;\pi_j(Z);B_j).                       \tag{3.1}
\]

The block chooses

\[
 a_j\in A_j,\qquad b_j\in B_j,
 \qquad X_j\in\binom{A_j\setminus\{a_j\}}{2Q},    \tag{3.2}
\]

orders \(X_j\), and chooses the target collar permutation \(\pi_{j+1}\).
The next boundary partition is

\[
 A_{j+1}=A_j-a_j+b_j,
 \qquad B_{j+1}=B_j-b_j+a_j.                       \tag{3.3}
\]

Thus \((A_0,A_1,\ldots,A_t)\) is a directed path in the Johnson graph on
the \((m-Q)\)-subsets of \(U\setminus Z\), whose complement has size
\(H-Q\).

### Theorem 3.1 (route-buffer characterization)

A state sequence is a concatenation of \(t\) flush/reload blocks if and
only if there exist data (3.1)--(3.3) such that, inside every block, its
state trace is given by (2.1)--(2.7) after adjoining the fixed sets

\[
 C_j=A_j\setminus(X_j\cup\{a_j\}),
 \qquad D_j=B_j\setminus\{b_j\}.                   \tag{3.4}
\]

Necessity is the routing theorem and Sections 1--2.  Conversely, the data
in (3.1)--(3.4) are exactly the legal choices used by the flush/reload
algorithm, so they compile the stated route sequence.

This is also a characterization of realizable column multisets, provided
one retains a partition into ordered blocks and identifies the common
boundary collar set \(Z\).  If the block order and boundary states are
forgotten, conditions (1.6) and (2.2) remain necessary but are not by
themselves sufficient.

## 4. A macroscopic common-core invariant

One route block selects at most \(2Q+1\) elements from its current core:
the \(2Q\) buffers and the exchanged label.  Therefore after \(t\) blocks,
at least

\[
 \boxed{|A_0|-t(2Q+1)=m-Q-t(2Q+1)}                 \tag{4.1}
\]

elements of the initial core have never been selected.  Every such element
lies in the lower core, and hence in every controlled flag, at every state
of the complete concatenated route.

Likewise each block selects only one element from the current tail for the
boundary exchange.  At least

\[
 \boxed{|B_0|-t=H-Q-t}                              \tag{4.2}
\]

elements of the initial tail remain in the tail throughout every block and
are absent from every controlled flag.

If the complete path has at most \(M\) states, then

\[
 1+t(4Q+1)\le M,
 \qquad
 t\le {M-1\over4Q+1}.                              \tag{4.3}
\]

Substitution in (4.1) gives

\[
\begin{aligned}
 m-Q-t(2Q+1)
 &\ge m-Q-{(M-1)(2Q+1)\over4Q+1}\\
 &=(1/2-o(1))m.                                    \tag{4.4}
\end{aligned}
\]

Also

\[
 H-Q-t=H-Q-O(M/Q)=H-o(H),                          \tag{4.5}
\]

because \(M/Q=o(H)\) in the calibrated regime.

Hence a path made only from these minimal flush/reload connectors is
confined for its entire duration between a fixed common core of size
\((1/2-o(1))m\) and a fixed cap omitting \((1-o(1))H\) carrier labels.
This is a strict structural restriction not present in TRP.

It does not by itself disprove a global construction, because the common
cores and omitted tails may vary with the carrier.  It does show that an
arbitrary balanced state multiset at one top cannot be repartitioned into
minimal route blocks: most such multisets have no macroscopic common
intersection.

## 5. The route-block incidence matrix is not TU

Let

\[
 r=m+Q
\]

be the upper-\(Q\) rank.  A route block with data \((C,P,D)\) contains the
\(d\) targets (2.2).

Choose an \((r-1)\)-set \(R_0\) and three labels \(u,v,w\) outside it.
Put

\[
 S_u=R_0+u,\qquad S_v=R_0+v,\qquad S_w=R_0+w.      \tag{5.1}
\]

Choose a common

\[
 C\in\binom{R_0}{m-3Q-1}.                           \tag{5.2}
\]

There are actual route blocks \(E_{uv},E_{uw},E_{vw}\) whose moving caps
are respectively

\[
 C\cup P_{uv}=R_0+u+v,
 \quad C\cup P_{uw}=R_0+u+w,
 \quad C\cup P_{vw}=R_0+v+w.                       \tag{5.3}
\]

Indeed each right side has size \(r+1=m+Q+1\), its difference from \(C\)
has size \(4Q+2=d\), and it may be extended by an arbitrary
\((H-Q-1)\)-set \(D\) to a carrier.  Choose any source split of \(P\) into
the required \(X,a,b,Z\); the routing theorem supplies the block.

On rows \((S_u,S_v,S_w)\) and columns
\((E_{uv},E_{uw},E_{vw})\), upper-\(Q\) incidence is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},                                    \tag{5.4}
\]

whose determinant is \(-2\).  Therefore the route-block/target matrix is
not totally unimodular, even before middle, lower, other upper, top-demand,
or boundary-linking rows are adjoined.

The half-vector on these three columns gives unit load on the three
displayed targets, whereas no integral choice of just these columns does.
This is a local integrality obstruction, not a proof that the full highly
redundant catalogue lacks an integral balanced solution.  It rules out the
proposed direct network-TU completion.

## 6. Fractional route flow and exact remaining gate

Choose a uniform source state at one top.  Choose \(a,b\), the ordered
buffers, and the target collar order uniformly among their legal values.
The construction is equivariant under every permutation of the carrier.
At each fixed connector phase its state distribution is therefore uniform
on the carrier-state space.  The endpoint distribution is also uniform:
the unordered core/tail exchange is one step of the biregular
Bernoulli--Laplace graph, while the target collar is uniformly reordered.

It follows that a stationary chain of flush/reload blocks has exactly
uniform state marginals at every phase.  Selecting

\[
 t=\left\lfloor{M-1\over4Q+1}\right\rfloor         \tag{6.1}
\]

blocks at every top therefore gives a zero-defect fractional solution for
all flag rows, all oriented candidate-star rows, and every block-boundary
linking constraint.  The unused final padding is \(O(Q)=o(M)\).

The surviving integral theorem can be stated compactly:

> Choose one fixed boundary collar set and one length-\(t\) Johnson
> skeleton path at every top; decorate its edges by ordered buffers and
> target collar permutations; and make the aggregate \(t(4Q+1)+1\) state
> traces satisfy balanced flag loads and the oriented collision energy
> (OB2), up to \(o(W)\) total defect.

If this theorem held, the route traces would already be genuine rotor
paths, Theorem 6.2 of the temporal audit would supply the required
all-round truncated-congestion control, and the remaining \(O(Q)\) padding
per carrier would cost only \(O(QN_H)=o(W)\).

What is proved here is that:

* fractional feasibility is exact;
* the route catalogue has a complete finite characterization;
* arbitrary balanced columns cannot be regrouped freely because route
  blocks have fixed interval and boundary-collar invariants;
* the natural route-block incidence matrix is not TU.

No Hall-type integral selection theorem for the full route catalogue is
proved.

