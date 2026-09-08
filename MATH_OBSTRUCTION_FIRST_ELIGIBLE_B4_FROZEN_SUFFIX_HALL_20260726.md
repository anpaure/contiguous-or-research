# The frozen-suffix Hall obstruction for first-eligible \(B_4\) packets

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Fix one ordered four-block atlas and form packets from the first \(r\)
eligible \(B_4\)-blocks, as in
`MATH_THEOREM_FIRST_ELIGIBLE_B4_SCD_PACKET_FACTOR_20260726.md`, with

\[
             r\le m/16,\qquad r\to\infty .                 \tag{0.1}
\]

Allow the strongest cycle-first mixed menu naturally supported by these
packets:

* every selected block may use any relabelled cyclic \(B_4\) seed;
* every packet may use any recursive direction order;
* instead of taking one entire menu factor, cycles from different menu
  factors may be mixed arbitrarily, provided that the chosen whole cycles
  partition the middle owners exactly; and
* the same relaxation may be made fractionally, with total component weight
  one at every owner.

Even this enlarged menu cannot cover the signed Gaussian band.  For every
fixed \(A>0\), at

\[
                         q=\lfloor A\sqrt m\rfloor          \tag{0.2}
\]

(whenever \(q\le\min\{H,r\}\)), there is an explicit lower target set
\(\mathcal Z_q^-\subseteq\binom{[2m]}{m-q}\) and an explicit upper target
set \(\mathcal Z_q^+\subseteq\binom{[2m]}{m+q}\) such that every integral
mixed-component factor misses

\[
              \boxed{\kappa_A W-o(W)}                       \tag{0.3}
\]

members of each set, where \(W=\binom{2m}{m}\) and \(\kappa_A>0\).
The same sets violate the fractional capacitated Hall inequality by
\(\kappa_AW-o(W)\).

The obstruction is not caused by a common recursive direction word.  It is
caused earlier, by first-eligible localization.  For all but
\(e^{-\Omega(m)}W\) owners, the first \(r\) eligible blocks avoid a fixed
quarter of the block positions.  Every legal packet component consequently
freezes all coordinates in that suffix.  A rank displacement of
\(A\sqrt m\), however, changes the hypergeometric law on that suffix by a
constant likelihood ratio.  A one-sided suffix-count event is therefore a
positive-density Hall cut.

Thus choosing relabelled seeds or recursive orders inside the fixed
first-eligible atlas cannot prove coefficient one.  A viable mixed-frame
construction must change the ordered block atlas itself, or use components
whose physical edges move coordinates outside the packet's first-eligible
blocks.

## 1. Packets and the enlarged component menu

Put

\[
 b=\lfloor m/2\rfloor
\]

and let \(B_1<\cdots<B_b\) be disjoint four-coordinate blocks.  In a
middle owner \(X\), a block is eligible when its restriction belongs to

\[
                         \mathcal A=\{14,12,23,34\}.         \tag{1.1}
\]

When at least \(r\) blocks are eligible, let \(I(X)\) be the ordered set
of the first \(r\) eligible indices.  Context stability makes the packet
\(P(X)\) and its index set \(I(P)=I(X)\) constant as \(X\) ranges over
the packet.

For a packet \(P\), let \(\mathfrak C(P)\) be the union of all oriented
physical \(C_{4r}\)-components obtained from all permitted relabellings of
the local \(B_4\) cycles and all permitted recursive orders.  The only
property used below is

\[
 C\in\mathfrak C(P),\ X,Y\in V(C)
 \quad\Longrightarrow\quad
 X\triangle Y\subseteq\bigcup_{i\in I(P)}B_i .       \tag{1.2}
\]

Thus the proof also covers any future recoupling of cycles which retains
(1.2).

An **integral mixed-component factor** is a collection \(\mathcal F\) of
whole members of \(\bigcup_P\mathfrak C(P)\) whose vertex sets partition
the retained middle owners.  This is a strict relaxation of choosing one
seed and one recursive factor for each whole packet: components belonging
to different packet-menu states may be mixed.

The fractional relaxation assigns \(x_C\ge0\) to components and imposes

\[
                         \sum_{C\ni X}x_C=1                 \tag{1.3}
\]

at every retained owner.  Consequently any obstruction valid under (1.3)
also applies to every integral packet-state selection.

For a phase start \(X\in V(C)\), write

\[
 \tau_{q,C}^-(X)=\bigcap_{j=0}^qF_C^j(X),\qquad
 \tau_{q,C}^+(X)=\bigcup_{j=0}^qF_C^j(X).             \tag{1.4}
\]

No injectivity of these maps is needed for the upper bound on the number
of targets hit: the number of distinct targets in a set is at most the
number of phase occurrences landing there.

## 2. An exponentially dominant frozen suffix

Let

\[
 j=\lfloor b/4\rfloor,\qquad
 R=\bigcup_{i=b-j+1}^bB_i,\qquad s=|R|=4j.            \tag{2.1}
\]

Then

\[
                  \gamma_m:={s\over2m}\longrightarrow {1\over4}. \tag{2.2}
\]

Call a packet normal if \(I(P)\cap\{b-j+1,\ldots,b\}=\varnothing\), and
let \(U_m\) be the number of middle owners which are either outside the
first-eligible packet cover or belong to a nonnormal packet.

### Lemma 2.1 (exceptional owner bound)

There is an absolute \(c>0\) such that

\[
                              U_m\le e^{-cm}W.        \tag{2.3}
\]

#### Proof

Before conditioning on middle rank, the eligibility indicators of the
first \(b-j\) blocks are independent Bernoulli variables of mean \(1/4\).
Their sum has mean

\[
 {b-j\over4}={3b\over16}+O(1).
\]

On the other hand, (0.1) gives

\[
 r\le {m\over16}={b\over8}+O(1).
\]

Thus, for all large \(m\), the event that fewer than \(r\) eligible
blocks occur before the suffix is a fixed lower-tail deviation.  Chernoff's
inequality bounds its unconditioned probability by \(e^{-\Omega(m)}\).
The event of having fewer than \(r\) eligible blocks in the entire atlas is
smaller still.  Conditioning on \(|X|=m\) costs only
\(\Theta(\sqrt m)\), since

\[
                         2^{-2m}\binom{2m}{m}=\Theta(m^{-1/2}).
\]

Finally, context stability makes normality constant on a packet.  This
proves (2.3). \(\square\)

### Lemma 2.2 (componentwise suffix conservation)

If \(C\) lies in a normal packet, then for every phase start \(X\in V(C)\),
every \(q\ge0\), and both signs,

\[
                 \tau_{q,C}^\pm(X)\cap R=X\cap R.    \tag{2.4}
\]

#### Proof

All vertices of \(C\) agree outside the selected blocks by (1.2), and the
selected blocks of a normal packet are disjoint from \(R\).  Intersection
and union of any consecutive vertices therefore retain exactly the common
restriction to \(R\). \(\square\)

This is the point at which tracking whole components matters.  A chosen
component uses every one of its phase owners, and (2.4) holds at every
phase simultaneously; there is no ownerwise flag choice capable of
changing the suffix projection.

## 3. Exact component Hall identity

For an integer \(a\), define

\[
 \begin{aligned}
 \mathcal Z_{q,a}^-&=
   \{T\in\tbinom{[2m]}{m-q}:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+&=
   \{T\in\tbinom{[2m]}{m+q}:|T\cap R|\ge s-a\},      \tag{3.1}
 \end{aligned}
\]

and put

\[
                 B_a=\bigl|\{X\in\tbinom{[2m]}m:|X\cap R|\le a\}\bigr|.
                                                                    \tag{3.2}
\]

Middle-layer complementation gives the same number \(B_a\) for the event
\(|X\cap R|\ge s-a\).

### Proposition 3.1 (mixed-component Hall bound)

For either an integral mixed-component factor or a fractional exact owner
cover satisfying (1.3), the total phase-occurrence capacity in
\(\mathcal Z_{q,a}^-\) is at most

\[
                              B_a+U_m,                \tag{3.3}
\]

and the same bound holds for \(\mathcal Z_{q,a}^+\).  Hence an integral
factor leaves at least

\[
             |\mathcal Z_{q,a}^\pm|-B_a-U_m          \tag{3.4}
\]

distinct targets uncovered.

#### Proof

For every normal component, Lemma 2.2 says that a lower phase occurrence
lands in \(\mathcal Z_{q,a}^-\) exactly when its owner has
\(|X\cap R|\le a\).  Therefore (1.3) gives the exact identity

\[
 \sum_{C\ \mathrm{normal}}x_C
  \sum_{X\in V(C)}
   \mathbf1_{\{\tau_{q,C}^-(X)\in\mathcal Z_{q,a}^-\}}
 =\sum_{X\ \mathrm{normal}}
   \mathbf1_{\{|X\cap R|\le a\}}.                  \tag{3.5}
\]

The right side is at most \(B_a\).  Give every exceptional owner the
most favorable possible completion; its one phase occurrence can add at
most one unit, so the additional capacity is at most \(U_m\).  This proves
(3.3).  Repeated occurrences of one target cannot increase the number of
distinct targets hit, giving (3.4).  The upper proof uses the complementary
event in (3.1). \(\square\)

Equivalently, assign weight one to the targets in \(\mathcal Z_{q,a}^\pm\)
and zero to all other targets.  Proposition 3.1 is the exact target-side
support function of every legal component mixture on this weight.  Thus
(3.4) is a literal capacitated Hall cut, not a collision-moment estimate.

## 4. The Gaussian cut has positive density

Fix \(A>0\) and take \(q=\lfloor A\sqrt m\rfloor\).  Let

\[
                 v={1\over2}\,{1\over4}\,{3\over4}={3\over32}. \tag{4.1}
\]

Choose a constant \(c>0\), to be fixed below, and put

\[
                         a_m=\left\lfloor{s\over2}-c\sqrt m\right\rfloor.
                                                                    \tag{4.2}
\]

The exact cardinalities entering Proposition 3.1 are

\[
 \begin{aligned}
 B_{a_m}
  &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-t},\\
 |\mathcal Z_{q,a_m}^-|
  &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-q-t}.     \tag{4.3}
 \end{aligned}
\]

Complementation gives

\[
                         |\mathcal Z_{q,a_m}^+|
                         =|\mathcal Z_{q,a_m}^-|.     \tag{4.4}
\]

Also

\[
 {N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}
 \longrightarrow e^{-A^2}.                          \tag{4.5}
\]

The standard hypergeometric central limit theorem, applied to (4.3), now
gives

\[
 \begin{aligned}
 {B_{a_m}\over W}
   &\longrightarrow
     \Phi\left(-{c\over\sqrt v}\right),\\
 {|\mathcal Z_{q,a_m}^-|\over W}
   &\longrightarrow
     e^{-A^2}
     \Phi\left({A/4-c\over\sqrt v}\right).          \tag{4.6}
 \end{aligned}
\]

Indeed, the suffix count has middle mean \(s/2\), lower-layer mean
\(s/2-(s/(2m))q=s/2-(A/4+o(1))\sqrt m\), and variance
\((v+o(1))m\) in both layers.

Put

\[
                d={A/4\over\sqrt v}=A\sqrt{2/3}.      \tag{4.7}
\]

Writing \(x=c/\sqrt v\), the desired strict Hall gap is

\[
                         e^{-A^2}\Phi(d-x)>\Phi(-x). \tag{4.8}
\]

Such an \(x\) always exists.  For \(x>d\), Mills' asymptotic gives

\[
 {\Phi(d-x)\over\Phi(-x)}
 ={x\over x-d}\exp\left(xd-{d^2\over2}+o(1)\right)
 \longrightarrow\infty                              \tag{4.9}
\]

as \(x\to\infty\).  Fix an \(x=x_A\) for which (4.8) is strict, set
\(c=x_A\sqrt v\), and define

\[
 \kappa_A=
 e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0.                  \tag{4.10}
\]

Equations (4.3)--(4.10) yield

\[
             |\mathcal Z_{q,a_m}^\pm|-B_{a_m}
             =(\kappa_A+o(1))W.                     \tag{4.11}
\]

Combining (2.3), (3.4), and (4.11) proves (0.3) for both signs.

## 5. Consequences and exact surviving gate

The obstruction is insensitive to all of the internal choices proposed in
the mixed-seed programme:

1. no common direction order was assumed;
2. local \(B_4\) seeds may be relabelled independently;
3. recursive orders may vary from packet to packet;
4. cycles from incompatible packet states were allowed to mix under the
   sole exact-owner constraint (1.3); and
5. neither packetwise shadow injectivity nor integrality was used.

The fixed ordered first-eligible atlas is therefore closed at Gaussian
depth.  Its candidate-support theorem remains correct owner by owner, but
candidate paths for suffix-atypical targets draw on the same insufficient
set of suffix-atypical middle owners.  Pointwise existence does not imply
the component Hall inequalities.

The precise escape is a **suffix-transport theorem**.  A future
cycle-first construction must mix genuinely different coordinate
matchings/block orders, or use exterior-moving components, so that for
every positive-density coordinate set \(R\) and every Gaussian threshold
event the selected components transport enough middle owners across the
corresponding hypergeometric cut.  Relabelling a cyclic seed inside already
selected blocks has zero transport across (3.1), and hence cannot meet this
gate.
