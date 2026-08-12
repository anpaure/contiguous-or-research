# Replicated \(Q_4\) braid bits: the exact occurrence LP and a logarithmic-depth dual cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The independent braid bank from
`MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md` gives a
literal binary multiple-choice system, but it cannot round the protected
multi-depth target cover.

The decisive quantity is not the number of targets on two context shores.
It is the number of directed phase occurrences which a braid bit can move.
One replicated \(Q_4\) component consists of two \(C_{2h}\)'s, hence has
\(4h\) phase owners, but its two states differ at exactly eight outgoing
tails.  Therefore at a fixed signed depth \(q\), switching the bit can
change at most

\[
                              8q                             \tag{0.1}
\]

actual target occurrences.  There are

\[
                         K={G\over4h}                         \tag{0.2}
\]

owner-disjoint braid components in a union of \(Q_h\)-cells containing
\(G\) middle owners.  Thus the whole bank can create at most

\[
                         8qK={2qG\over h}                     \tag{0.3}
\]

new occurrences in any prescribed signed target family.

This finite edit budget gives an explicit occurrence-capacity dual cut.
Fix any reference syndrome factor and its cellwise direction relabellings,
and let \(Z_q^\epsilon\) be the targets absent from that reference at one
signed depth.  Every fractional or integral selection of the independent
braid bits has uncovered mass at least

\[
 \boxed{
 |Z_q^\epsilon|-{2qG\over h}-E,}                    \tag{0.4}
\]

where \(E=W-G\) is granted arbitrary completion capacity.

The reference factor has one common cyclic direction order inside each
\(Q_h\)-cell, so its depth-\(q\) image has size at most

\[
                         {Gh\over2^q}.                       \tag{0.5}
\]

At

\[
                         q_* =\lceil2\log_2h\rceil,           \tag{0.6}
\]

provided \(q_*\le H\), equations (0.3)--(0.5) give

\[
 \boxed{
 D_{q_*}^\epsilon
 \ge N_{q_*}-{Gh\over2^{q_*}}-{2q_*G\over h}-E
 =W-o(W).}                                             \tag{0.7}
\]

This holds separately for lower and upper targets.  It is an occurrence
cut: every directed start is counted with its full multiplicity, and only
the eight-tail edit bound is used.  It is unrelated to the retracted raw
side-size comparison.

The exact occurrence matrix is not totally unimodular.  Already at depth
three it has a coefficient two, forced by the translate pairing
\(v=e_2+e_4\) of the replicated braid components.  Consequently fractional
edge-cover feasibility would not imply integral bit selection even without
the cut (0.7).

The surviving use of the braid is only as a final sparse absorber.  After
a different primary construction, its residual must satisfy every weighted
Hall cut and, necessarily, have scale at most \(O(qW/h)\) at depth \(q\)
and \(O(H^2W/h)\) across the whole signed tower.  The common-order syndrome
factor is far outside that regime.

## 1. The replicated component bank

Let \(h=2^t\ge8\).  In one standard syndrome factor of \(Q_h\), the number
of cycles is

\[
                         {2^h\over2h}.
\]

Translation by

\[
                         v=e_2+e_4                         \tag{1.1}
\]

pairs these cycles without fixed points.  Hence the cell contains

\[
                         M={2^h\over4h}                     \tag{1.2}
\]

owner-disjoint braid components.  Each component is the union of two
cycles and has \(4h\) owners.  State zero has direction word

\[
             1,2,3,4,5,\ldots,h, 1,2,3,4,5,\ldots,h,
                                                                  \tag{1.3}
\]

and state one has

\[
             1,4,3,2,5,\ldots,h, 1,4,3,2,5,\ldots,h.             \tag{1.4}
\]

Both states partition the same \(4h\) owners into two physical
\(C_{2h}\)'s.  Different components have disjoint owner supports, so their
bits commute exactly.

### Lemma 1.1 (eight changed successor tails)

If \(F_i^0,F_i^1\) are the successor maps of the two states of component
\(i\), then

\[
             D_i=\{X:F_i^0(X)\ne F_i^1(X)\},
             \qquad |D_i|=8.                              \tag{1.5}
\]

#### Proof

In each half of (1.3)--(1.4), the outgoing directions differ at the two
phase positions occupied by directions two and four.  There are two cycles,
so one half has four changed tails.  The antipodal half repeats the same
exchange, giving eight.  At every other tail the old and new rows use the
same physical edge. \(\square\)

### Lemma 1.2 (depth-\(q\) occurrence stability)

For either sign, the target traces of states zero and one differ at no more
than \(8q\) phase starts of one component.

#### Proof

A state-one start can differ from its state-zero trace only if one of its
first \(q\) outgoing tails belongs to \(D_i\).  For a fixed tail
\(Y\in D_i\) and a fixed lag \(j\in\{0,\ldots,q-1\}\), the permutation
\(F_i^1\) has at most one start \((F_i^1)^{-j}(Y)\).  Thus at most
\(q|D_i|=8q\) starts are affected. \(\square\)

This proof counts directed occurrences.  It neither assumes target
injectivity nor replaces a repeated target by one unit prematurely.

## 2. Exact multiple-choice occurrence edge cover

Let

\[
 \mathcal J=
 \{(q,\epsilon,T):1\le q\le H,\ \epsilon\in\{-1,+1\},\
              T\in\tbinom{[2m]}{m+\epsilon q}\}       \tag{2.1}
\]

be the tagged target tower.  For component \(i\), state
\(e\in\{0,1\}\), and tagged target \(t=(q,\epsilon,T)\), define the exact
occurrence coefficient

\[
 a_{i,e,t}=
 \bigl|\{X\in V_i:\tau_{q,F_i^e}^{\epsilon}(X)=T\}\bigr|.    \tag{2.2}
\]

The coefficients are nonnegative integers and retain all multiplicities.
At every fixed tagged rank,

\[
                         \sum_Ta_{i,e,(q,\epsilon,T)}=4h.     \tag{2.3}
\]

For unit target demand, the fractional hole programme is

\[
\begin{aligned}
 \eta=\min\quad&\sum_{t\in\mathcal J}z_t,\\
 z_t+\sum_i\sum_{e=0}^1a_{i,e,t}x_{i,e}&\ge1
                                      &&(t\in\mathcal J),\\
 x_{i,0}+x_{i,1}&=1                  &&(i),\\
 x_{i,e},z_t&\ge0.                                      \tag{2.4}
\end{aligned}
\]

The integral problem adds \(x_{i,e}\in\{0,1\}\).  Prescribed demands
\(d_t\) replace the right side one by \(d_t\).  Thus (2.4) is a binary
multiple-choice multihypergraph edge cover: a left component chooses one
of two target-occurrence multisets, and the same choice is used at every
depth and both signs.

### Theorem 2.1 (exact weighted dual)

The value of (2.4) is

\[
 \boxed{
 \eta=
 \max_{0\le y_t\le1}
 \left\{
  \sum_ty_t-
  \sum_i\max_{e\in\{0,1\}}
           \sum_ta_{i,e,t}y_t
 \right\}.}                                           \tag{2.5}
\]

For demand \(d_t\), the first sum is \(\sum_td_ty_t\).

#### Proof

This is linear-programming duality after minimizing independently over the
two-choice simplex of every component.  The upper bounds \(y_t\le1\) are
dual to the unit-cost hole variables \(z_t\). \(\square\)

Write \(\Delta_{i,t}=a_{i,1,t}-a_{i,0,t}\).  Since the bits are genuinely
independent, the support function in (2.5) has the exact additive form

\[
 \sum_i\max_e a_{i,e}\cdot y
 =\sum_i\left(a_{i,0}\cdot y+(\Delta_i\cdot y)_+\right).       \tag{2.6}
\]

This equality is the principal algebraic gain supplied by replication.
It does not imply integrality.

### Joint reference-order choices

If cell \(c\) may first choose a reference conjugate \(g\in\Gamma_c\),
let \(u_{c,g}\) be its weight and let \(w_{c,g,i}\) be the weight of bit
one in component \(i\), conditional on \(g\).  The exact extended
fractional formulation is

\[
 \sum_gu_{c,g}=1,qquad
 0\le w_{c,g,i}\le u_{c,g},                          \tag{2.7}
\]

with target load

\[
 \sum_{c,g}\left(
  u_{c,g}a^0_{c,g,t}+
  \sum_iw_{c,g,i}\Delta_{c,g,i,t}
 \right).                                             \tag{2.8}
\]

Indeed, conditional bit marginals in \([0,1]^M\) are realizable by a
distribution on \(\{0,1\}^M\), and the occurrence vector is affine in the
bits.  Integrally, exactly one \(u_{c,g}\) is one and every corresponding
\(w_{c,g,i}\) is binary.

## 3. Total unimodularity fails in the literal matrix

### Proposition 3.1 (a coefficient-two minor)

If \(H\ge3\), the occurrence matrix in (2.4) is not totally unimodular.

#### Proof

Consider one base braid component.  Its two syndrome cycles are translates
by \(v=e_2+e_4\).  At the phase whose next three base directions are

\[
                              D=\{2,3,4\},             \tag{3.1}
\]

the two phase starts differ by \(v\in V_D\).  Hence they define the same
affine three-face:

\[
                         x+V_D=(x+v)+V_D.              \tag{3.2}
\]

Their lower traces are equal, and their upper traces are equal.  Therefore
for the corresponding tagged target \(t\),

\[
                              a_{i,0,t}\ge2.           \tag{3.3}
\]

This coefficient is a \(1\times1\) minor of the literal constraint matrix.
A totally unimodular matrix has every entry in \(\{0,1,-1\}\), so (2.4)
is not TU. \(\square\)

Clipping (3.3) to one produces a different support LP and discards the
occurrence capacities required in the audited formulation.  It cannot be
used to infer integrality of (2.4).

## 4. Exact absorber budget

Fix a reference state zero in every component.  For a signed target family
\(Z\) at depth \(q\), let

\[
 L_0(Z)=\sum_i\sum_{T\in Z}a_{i,0,(q,\epsilon,T)}              \tag{4.1}
\]

be its reference occurrence capacity.

### Theorem 4.1 (one-depth braid capacity)

Every fractional or integral braid-bit selection satisfies

\[
 \sum_{T\in Z}L(T)\le L_0(Z)+8qK.                    \tag{4.2}
\]

Consequently its fractional uncovered mass in \(Z\) is at least

\[
 \boxed{
 \sum_{T\in Z}(1-L(T))_+
 \ge |Z|-L_0(Z)-8qK.}                                \tag{4.3}
\]

#### Proof

For one component, Lemma 1.2 says that state one can add at most \(8q\)
occurrences to \(Z\) beyond state zero.  Sum this inequality over the
\(K\) component simplexes.  Then use \((1-u)_+\ge1-u\) target by target.
Equivalently, (4.3) is (2.5) with \(y\) the indicator of \(Z\). \(\square\)

For a general tower weight \(0\le y_t\le1\), Lemma 1.2 gives, per
component,

\[
 |a_{i,1}\cdot y-a_{i,0}\cdot y|
 \le2\sum_{q=1}^H8q=8H(H+1).                        \tag{4.4}
\]

Therefore the whole braid bank can improve the support function of a fixed
reference factor by at most

\[
 \boxed{
 8H(H+1)K={2G H(H+1)\over h}.}                       \tag{4.5}
\]

Equations (4.3)--(4.5) give the weakest possible residual scale for a
future absorber theorem.  They are necessary, not sufficient: non-TU shows
that all weighted fractional cuts still would not automatically provide an
integral bit choice.

## 5. The explicit logarithmic-depth dual cut

In one reference \(Q_h\)-cell, every cycle has one common cyclic direction
order.  A depth-\(q\) trace is determined by

1. one of at most \(h\) cyclic direction intervals, and
2. one of \(2^{h-q}\) orientations outside that interval.

Thus the number of distinct reference targets of either sign is at most

\[
                              h2^{h-q}.               \tag{5.1}
\]

Let the good owner support consist of \(G/2^h\) cells, with arbitrary
cellwise translations and direction relabellings of the reference syndrome
factor.  Their combined reference image has size at most

\[
                              {Gh\over2^q}.           \tag{5.2}
\]

Let \(Z_q^\epsilon\) be the complement of this reference image in the
signed rank-\(q\) target layer.  Then

\[
                    |Z_q^\epsilon|\ge N_q-{Gh\over2^q},
 \qquad L_0(Z_q^\epsilon)=0.                         \tag{5.3}
\]

Give the \(E=W-G\) outside owners arbitrary favorable occurrences.  Theorem
4.1 yields the literal occurrence-dual inequality

\[
 D_q^\epsilon
 \ge N_q-{Gh\over2^q}-{2qG\over h}-E.               \tag{5.4}
\]

Now take \(q_*\) from (0.6).  Since \(h\le2m\),
\(q_*=O(\log m)=o(\sqrt m)\), and hence

\[
                              N_{q_*}=W-o(W).          \tag{5.5}
\]

Moreover,

\[
 {Gh\over2^{q_*}}\le{G\over h},
 \qquad
 {2q_*G\over h}=O\left({G\log h\over h}\right)=o(W). \tag{5.6}
\]

If \(G=W-o(W)\) and \(h\to\infty\), substitution in (5.4) proves (0.7).
The dual weight is supported at one tagged depth and one sign, so sharing
the same bits across all other depths cannot weaken the obstruction.

There is also a deterministic column form of the same conclusion.  In one
cell, an arbitrary braid state differs from its reference on at most
\(8M=2^{h+1}/h\) tails, and therefore has signed depth-\(q\) image at most

\[
 2^h\left({h\over2^q}+{2q\over h}\right).            \tag{5.7}
\]

At \(q_*\), this is \(O((\log h)/h)2^h\).  Thus even if the reference
direction order is chosen separately in every cell, every deterministic
one-state-per-cell field hits only \(o(W)\) targets at this depth.  A joint
fractional mixture of many reference orders can spread its occurrence mass
more widely, but (5.7) shows that the replicated braid bank cannot round
such a mixture to one integral cell state.

## 6. Precise boundary

Proved here:

* the exact two-choice occurrence coefficients, including multiplicity;
* the exact multiple-choice edge-cover LP and weighted dual;
* a compact extended LP when reference conjugates are also variables;
* failure of total unimodularity in the literal occurrence matrix;
* the sharp \(8q\)-per-bit and \(O(H^2)\)-per-bit absorber ledgers; and
* a \(W-o(W)\) occurrence-capacity cut at one logarithmic depth for every
  fixed reference order field.

Not ruled out is a construction with \(\Omega(h/q)\) overlapping braid
layers, or another dense exterior-moving generator, for which a typical
depth-\(q\) occurrence meets a switched tail with probability bounded away
from zero.  Such layers cannot be selected independently on the same owner
support by Theorem 5.1 alone; they require a new braid-network ownership
theorem.  The present single replicated bank is a sparse final absorber,
not a rounding mechanism for the central cover.
