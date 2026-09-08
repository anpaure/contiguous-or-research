# Gate C: an adjacent-rank transition skeleton

**Status (2026-09-05).**  The three central Boolean layers admit a set of
`W-o(W)` directed Johnson transitions which is simultaneously almost
injective on lower targets, upper targets, tails, and heads.  This follows
from a fixed-rank four-partite matching theorem, so there is no abstract
adjacent-layer matching obstruction.

The selected transitions are not asserted to obey the FIFO recurrence or
to group into completed coherent tours.  The theorem therefore isolates
the surviving obstruction as chronological factorization, rather than
lower/upper target compatibility.

Let `|Omega|=2b` and put

\[
 \mathcal L={\Omega\choose b-1},\qquad
 \mathcal M={\Omega\choose b},\qquad
 \mathcal U={\Omega\choose b+1},                    \tag{0.1}
\]

\[
 W=|\mathcal M|={2b\choose b},\qquad
 W_1=|\mathcal L|=|\mathcal U|={b\over b+1}W.       \tag{0.2}
\]

Use two labelled copies `mathcal M_out,mathcal M_in` of the middle layer.

## 1. The four-partite transition hypergraph

For every ordered pair `A,B in mathcal M` at Johnson distance one, form
the four-edge

\[
 e(A,B)=\bigl(A\cap B,\ A_{\rm out},\ B_{\rm in},\ A\cup B\bigr)    \tag{1.1}
\]

on

\[
 \mathcal L\mathbin{\dot\cup}\mathcal M_{\rm out}
 \mathbin{\dot\cup}\mathcal M_{\rm in}\mathbin{\dot\cup}\mathcal U.
                                                                  \tag{1.2}
\]

Call the resulting `4`-uniform hypergraph `mathcal Q_b`.

### Lemma 1.1 (degrees and codegrees)

Every lower or upper vertex has degree `b(b+1)`, every middle-copy vertex
has degree `b^2`, and

\[
                         \Delta_2(\mathcal Q_b)=b.    \tag{1.3}
\]

#### Proof

For fixed `L in mathcal L`, choose the two elements of `U setminus L` and
one of the two orientations of the resulting middle pair.  This gives

\[
                         2{b+1\choose2}=b(b+1)       \tag{1.4}
\]

edges.  The upper count is identical.  For fixed `A_out`, choose the
removed member of `A` and the entering member of `Omega setminus A`, giving
`b^2`; the incoming count is symmetric.

Two vertices from the same part have codegree zero.  A compatible pair
`(L,U)` lies in its two oriented middle transitions.  A compatible pair
`(A_out,B_in)` determines at most one transition.  Given `L subset A`, the
other middle endpoint is `L union {y}` with `y in Omega setminus A`, giving
`b` choices.  The three symmetric lower/upper--middle cases have the same
count.  Thus the maximum is exactly `b`. \(\square\)

## 2. A near-perfect transition matching

We use the standard fixed-uniformity almost-regular matching theorem: if a
sequence of `k`-uniform hypergraphs, for fixed `k`, has all degrees
`(1+o(1))D` with `D->infinity` and maximum pair-codegree `o(D)`, then it has
a matching leaving `o(|V|)` vertices uncovered.  This is the usual
Pippenger--Spencer nibble theorem; its fixed `k=4` hypothesis is literal
here.

Lemma 1.1 has

\[
 {b(b+1)\over b^2}=1+{1\over b},\qquad
 {\Delta_2\over b^2}={1\over b}.                    \tag{2.1}
\]

It therefore gives a matching `mathcal N` in `mathcal Q_b` with

\[
                         |\mathcal N|=W-o(W).         \tag{2.2}
\]

Because the lower and upper shores each have only `W_1=W-o(W)` vertices,
(2.2) is equivalently `W_1-o(W)`: the matching misses only `o(W)` lower
targets and `o(W)` upper targets.  It also uses distinct tails in
`mathcal M_out` and distinct heads in `mathcal M_in`.

### Corollary 2.1 (an almost two-regular directed Johnson skeleton)

Regard every selected `e(A,B)` as the directed Johnson edge `A->B` on the
single middle layer.  Then

* every middle vertex has outdegree at most one and indegree at most one;
* all but `o(W)` middle vertices have both indegree and outdegree one; and
* the intersection and union labels of the selected edges miss only
  `o(W)` members of `mathcal L` and `mathcal U`, respectively.

#### Proof

The first and third claims are the four matching constraints.  The sets of
tails and heads both have size `W-o(W)`.  Their intersection therefore has
size at least `W-o(W)`, proving the second claim. \(\square\)

The directed skeleton is a disjoint union of cycles and paths, with only
`o(W)` vertices outside its degree-two core.  The number of cycles need not
be small.

## 3. Exact scope

A sequence of Johnson transitions `A_i->A_(i+1)` is a sequence of literal
sliding windows only when its swaps obey the FIFO recurrence: after the
initial queue is fixed, the element removed at time `i+b` must be the
element inserted at time `i`.  Nothing in the four-partite matching enforces
that long recurrence.  Nor does it bound the number of cycle components.

Thus the theorem proves that the adjacent targets, considered with both
middle endpoints, possess the desired near-integral incidence skeleton.
The completed coherent-tour selector asks for a much stronger
factorization of such a skeleton into `Theta(W/b^2)` clean FIFO cycles.
The antipodal-bank theorem supplies locally compatible FIFO cycles, but a
global orbit matching of those cycles remains necessary.
