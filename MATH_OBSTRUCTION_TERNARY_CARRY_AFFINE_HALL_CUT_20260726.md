# The ternary-carry affine Hall cut: whole-component shore freedom does not balance consecutive traces

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Verdict

The phase-dense ternary-carry factor removes the local ownership obstruction,
but it does **not** compose with the affine trace theorem in its present form.
The reason is an explicit all-target Hall cut for the actual consecutive
traces.

Write

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\tag{0.1}
\]

In the carry construction, \(t\) is a power of two, \(h=2t=o(m)\), and the
good middle owners are partitioned into canonical macrocells of size
\(24^t\). A static shore factor on one macrocell is the disjoint union of
\(6^t\) parallel one-order Hamming factors on \(Q_h\). The ternary carry
changes exactly

\[
 E_{\rm cell}
 =\frac{3(1-3^{-t})}{4h}\,24^t
\tag{0.2}
\]

outgoing edges of that static factor.

For either sign and every \(1\le q<h\), the number of distinct physical
depth-\(q\) targets hit by the carry factor in one macrocell is at most

\[
 \boxed{
 24^t\left(\frac{h}{2^q}
       +\frac{3q(1-3^{-t})}{4h}\right).}
\tag{0.3}
\]

The first term is the physical basepoint plateau of the common-order
Hamming factors. The second term is the maximum number of new targets
created by carry-changed edges.

Take

\[
 q_*:=\left\lceil2\log _2 h\right\rceil.
\tag{0.4}
\]

In the phase-dense choice \(t\ge H\), \(t<2H\), one has \(h<4H\), so
\(q_*\le H\) for all sufficiently large \(h\). Moreover

\[
 \frac{h}{2^{q_*}}+\frac{3q_*}{4h}=o(1),
 \qquad
 \frac{N_{q_*}}W=1-o(1).
\tag{0.5}
\]

Consequently, after summing over all macrocells and even after allowing the
exponentially small bad-owner set to hit a new target at this depth, one has

\[
 \boxed{M_{q_*}^-=W-o(W),\qquad M_{q_*}^+=W-o(W).}
\tag{0.6}
\]

In particular

\[
 \sum_{q\le H}(M_q^-+M_q^+)\ge2W-o(W),
\tag{0.7}
\]

so the SCI signed-band-hole condition fails at a single logarithmic depth.
The failure is stronger than the Gaussian collision obstruction and occurs
well before the Gaussian window.

The same cut rules out fractional mixing among whole-macrocell affine
conjugates of the present carry factor. Affine conjugacy relabels the trace
image but does not enlarge (0.3). Thus component-constant shore freedom is
not the missing component-dependent affine Hall theorem: the carry variables
choose phase-aligned shore matchings, not independent trace-rainbow affine
factors.

The obstruction does **not** rule out a new carry built on the recursive
trace-rainbow factor. Such a construction would have to reprove the
six-fibre port alignment and ternary holonomy after independent affine
refreshing. That compatibility theorem is presently absent.

## 1. A common-order image bound

Let \(P\) be a finite owner set and let \(F_0:P\to P\) be a permutation.
Suppose \(P\) is partitioned into \(L\) physical orientation cubes

\[
 P=P_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_L,
 \qquad P_a\cong Q_h,
\tag{1.1}
\]

and, in each \(P_a\), every cycle of \(F_0\) has one common cyclic order of
the \(h\) cube directions. Coordinate permutations and a common affine
translation are allowed separately in the different cells.

For a start \(x\), let \(T_{q,F_0}^-(x)\) be the intersection of the first
\(q+1\) middle states on its forward orbit, and let \(T_{q,F_0}^+(x)\) be
their union.

### Lemma 1.1 (parallel physical support)

For either sign and every \(1\le q<h\),

\[
 \left|\{T_{q,F_0}^{\pm}(x):x\in P\}\right|
 \le Lh2^{h-q}.
\tag{1.2}
\]

#### Proof

Inside one \(Q_h\)-cell, the \(q\) directions of a forward window form one
of the \(h\) cyclic \(q\)-intervals of the common direction order. Once
that direction set is fixed, an affine \(q\)-face has at most \(2^{h-q}\)
outside orientations. Hence at most \(h2^{h-q}\) affine faces occur.

Both the lower intersection and upper union are functions of the affine
face: active pairs are respectively emptied or filled, while every inactive
pair retains its outside orientation. Thus neither signed physical image
is larger than the affine-face image. Sum the bound over the \(L\) cells.
Overlaps between cells only decrease the union size. \(\square\)

No direction-set balance can repair (1.2). The lost information is the
affine basepoint outside the consecutive direction set.

## 2. Stability under a sparse permutation switch

The carry factor and its static reference are permutations of the same
owner support. The following elementary comparison is the exact bridge
from their edge ledger to physical traces.

### Lemma 2.1 (changed-edge support bound)

Let \(F,F_0:P\to P\) be permutations and put

\[
 D=\{x\in P:F(x)\ne F_0(x)\},\qquad e=|D|.
\tag{2.1}
\]

For either sign and every \(q\ge1\),

\[
 \left|\operatorname {im}T_{q,F}^{\pm}\right|
 \le
 \left|\operatorname {im}T_{q,F_0}^{\pm}\right|+qe.
\tag{2.2}
\]

#### Proof

Let \(A_q\) be the starts whose first \(q\) outgoing \(F\)-edges contain a
tail in \(D\). For a fixed \(y\in D\) and a fixed lag
\(j\in\{0,\ldots,q-1\}\), there is exactly one start \(F^{-j}(y)\).
Therefore

\[
 |A_q|\le qe.
\tag{2.3}
\]

If \(x\notin A_q\), induction along the first \(q\) steps gives
\(F^j(x)=F_0^j(x)\) for \(0\le j\le q\). Its lower and upper targets are
therefore targets already present in the \(F_0\)-image. Starts in \(A_q\)
can add at most one new target each, proving (2.2). \(\square\)

This is a support statement, not a perturbative estimate on multiplicity.
It is consequently exactly the statistic needed for the all-target Hall
cut.

## 3. Application to one ternary-carry macrocell

The common owner support of one local associator has \(24\) states. On
\(t\) selected blocks, one canonical macrocell therefore has

\[
 |P|=24^t=6^t2^h,
 \qquad h=2t.
\tag{3.1}
\]

Fix the all-new static shore factor \(F_0\). It partitions \(P\) into
\(L=6^t\) physical \(Q_h\)-cells, each carrying the parallel Hamming factor
with the opposite-axis order

\[
 (\alpha _1,\ldots,\alpha _t,
   \beta _1,\ldots,\beta _t)
\tag{3.2}
\]

twice around a \(C_{2h}\).

Let \(F_{\rm car}\) be the ternary-carry successor. Its exact edge-change
ledger is (0.2). Lemmas 1.1 and 2.1 give

\[
\begin{aligned}
 |\operatorname {im}T_{q,F_{\rm car}}^{\pm}|
 &\le 6^th2^{h-q}+qE_{\rm cell}\\
 &=24^t\left(
       h2^{-q}+\frac{3q(1-3^{-t})}{4h}
       \right),
\end{aligned}
\tag{3.3}
\]

which is (0.3).

The proof uses no relation between different macrocells. Therefore any
separate coordinate relabelling or affine conjugacy in every macrocell
leaves the same cardinality bound. It also permits different conjugacies
in different macrocells: summing their image sizes is still an upper bound
on the size of the global image.

## 4. The explicit component-dependent Hall cut

Let the good owner mass be

\[
 G=W-u,
 \qquad u\le e^{-\Omega(m)}W,
\tag{4.1}
\]

and partition it into canonical \(24^t\)-owner macrocells. For a macrocell
\(P\), let \(\mathfrak G_P\) be any menu consisting of physical affine
conjugates of the ternary-carry factor, including arbitrary conjugacies
chosen separately in different macrocells. Write

\[
 \mathcal S_q^\epsilon(P,g)
 =\{T_{q,g}^\epsilon(x):x\in P\}
\tag{4.2}
\]

for its set of distinct actual consecutive targets.

Put

\[
 \eta_{h,q}=h2^{-q}+\frac{3q(1-3^{-t})}{4h}.
\tag{4.3}
\]

Equation (3.3) says

\[
 \max_{g\in\mathfrak G_P}|\mathcal S_q^\epsilon(P,g)|
 \le |P|\eta_{h,q}.
\tag{4.4}
\]

Consider the component-choice covering LP at one signed depth: one state
must be selected fractionally from every macrocell menu and every physical
target has unit demand. Its dual, with weight one on every target, gives
the deficiency lower bound

\[
\begin{aligned}
 D_{q,\epsilon}
 &\ge N_q-
   \sum_P\max_{g\in\mathfrak G_P}
                    |\mathcal S_q^\epsilon(P,g)|-u\\
 &\ge N_q-G\eta_{h,q}-u.
\end{aligned}
\tag{4.5}
\]

Thus (4.5) is an explicit violated weighted Hall cut. It applies to
integral choice, fractional choice, random choice, and every correlation
among different macrocell choices.

The term \(u\) is deliberately generous: every bad owner is allowed to
create a distinct target at the chosen signed depth.

## 5. Evaluation at logarithmic depth and SCI

Take \(q_*\) as in (0.4). Then

\[
 h2^{-q_*}\le h^{-1},
 \qquad
 \frac{3q_*(1-3^{-t})}{4h}
 =O\!\left(\frac{\log h}{h}\right),
\tag{5.1}
\]

so \(\eta_{h,q_*}=o(1)\).

For the canonical phase-dense parameter choice, \(t\) is the least power
of two at least \(H\). Hence

\[
 H\le t<2H,
 \qquad 2H\le h<4H.
\tag{5.2}
\]

It follows that \(q_*\le H\) for sufficiently large \(h\). Also
\(q_*=O(\log h)=o(\sqrt m)\), because \(h=o(m)\). The exact layer ratio is

\[
 \frac{N_q}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}.
\tag{5.3}
\]

Taking logarithms in (5.3) gives, uniformly for \(q=o(\sqrt m)\),

\[
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}+O\!\left(\frac{q^3}{m^2}\right),
\tag{5.4}
\]

and hence \(N_{q_*}=W-o(W)\).

Substituting (5.1) and (4.1) into (4.5) yields

\[
 D_{q_*,\epsilon}=W-o(W)
\tag{5.5}
\]

for each sign. For an actual selected factor the owner-to-target graph is
functional, so its target-side Hall deficiency is exactly its hole count.
This proves (0.6)--(0.7).

The middle condition is not the issue: the good macrocells are exact owner
factors and \(u=o(W)\). The SCI failure is entirely in the labelled
consecutive shadows.

## 6. Why the two existing theorems do not compose

The full-activity affine theorem and the ternary-carry theorem solve
different incidence equations.

1. The full-activity theorem installs a recursive trace-rainbow factor in
   each \(Q_h\)-cell. Independent affine conjugates make the actual trace
   maps injective within every cell, and local activity signatures separate
   different cells.

2. The ternary carry starts from the parallel Hamming factor. Its common
   phase \(j\) and syndrome \(k=x+p_j\) are the data which identify the two
   shore matchings at a port. Whole six-point fibres may choose either
   shore matching, and the base-three predicate fuses the components.

The second freedom is genuine whole-component ownership freedom, but it is
not independent affine trace freedom. Replacing the parallel factors by
unrelated affine recursive factors destroys the common phase/syndrome
identification used to define the six-point fibres. Conversely, keeping
that identification leaves the common-order support bound (1.2), and the
carry changes too few edges to remove it.

Therefore the inference

\[
 \text{whole-component shore choices}
 +\text{affine trace balance}
 \Longrightarrow\text{component-dependent affine Hall}
\tag{6.1}
\]

is invalid. The two choices are not simultaneously available in the
current physical factor.

## 7. Smallest surviving replacement theorem

The cut identifies the exact necessary repair.

> **Trace-rainbow ternary fusion theorem — unproved.** On every canonical
> \(24^t\)-owner macrocell, construct an exact factor which:
>
> 1. uses whole overlay fibres, so every owner is covered once;
> 2. has \(o(24^t/H)\) components after fusion;
> 3. is cyclically \(H\)-geodesic;
> 4. satisfies
>    \[
>    \sum_{q\le H,\epsilon=\pm}
>    \left(24^t-
>      |\operatorname {im}T_{q}^{\epsilon}|
>    \right)=o(24^t)
>    \]
>    after the appropriate ambient layer normalization; and
> 5. admits component-dependent affine menus whose actual consecutive
>    target sets pass every weighted outer Hall cut.

A sufficient route would replace the parallel Hamming factors by the
recursive trace-rainbow factor and prove a new port theorem showing that
the two shore copies retain a common fibre coordinate under the required
independent affine refreshes. Neither the full-activity theorem nor the
present carry theorem proves that compatibility.

The logarithmic cut shows that changing only \(o(W/\log h)\) outgoing
edges over all good owners can never suffice: at depth \(q_*\), each
changed edge can rescue at most \(q_*\) starts. In particular, any repair
of the present factor must refresh

\[
 \Omega(W/\log h)
\tag{7.1}
\]

edges in total. Equivalently, its average refresh over the canonical
macrocells is \(\Omega(24^t/\log h)\). It may distribute those changes
nonuniformly among macrocells, but it cannot evade the total bound without
abandoning the common-order reference altogether.

## 8. Audit checklist

1. The support bound counts distinct physical targets, not merely
   direction sets.
2. The factor \(q\), not \(2q\), in Lemma 2.1 is exact: a changed outgoing
   edge has \(q\) possible positions in a length-\(q\) transition window.
3. Cross-macrocell overlaps can only reduce the global hit set, so summing
   macrocell image sizes is a valid upper bound.
4. The all-target dual cut is unaffected by correlations among macrocell
   choices.
5. Both signs use the same affine-face support and the same changed-start
   set, so the argument applies separately below and above.
6. The selected depth \(q_*\) lies in the hard band and satisfies
   \(N_{q_*}=W-o(W)\).
7. The argument does not claim that arbitrary, non-phase-aligned
   six-fibre switches remain sparse or legal. It refutes the present
   ternary-carry factor and its affine conjugacy menu; enlarging that menu
   requires a new physical factor theorem.
