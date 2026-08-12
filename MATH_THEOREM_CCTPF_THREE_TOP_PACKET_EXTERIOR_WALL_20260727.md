# The dense three-top reservoir is a subcritical CCTPF absorber

## Exact cyclic-incidence wall, multi-packet threshold, and trace-cost boundary

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad L=m-3H+1,
 \qquad W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H}.
\tag{0.1}
\]

Assume the calibrated CCTPF regime

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>16H,
\tag{0.2}
\]

and let a **reservoir packet** mean one of the mutually top-disjoint and
middle-disjoint three-top promotion conveyors from the dense orbit
packing theorem.

There are two different objects at the proposed interface.

* A reservoir packet contains three complete cyclic frames and has a
  common, squarefree middle support of size \(3M\).
* A CCTPF history on one top retains only \(L\) middle masks, together
  with its coupled lower and upper traces.

Even granting the strongest favorable interface--namely, that deleting
one packet makes all \(3M\) of its middle owners available to the CCTPF
augmentation--one packet cannot absorb a fourth, previously unpacketized
top **from that exposed owner support alone**.

The obstruction is not just the global inequality \(4L>3M\).  If \(U\)
is a rank-\(M\) top distinct from the three packet tops, then \(U\) is
compatible with at most

\[
                         3H                                      \tag{0.3}
\]

of the packet's \(3M\) middle owners.  A CCTPF history on \(U\) requires
\(L\) distinct middle owners.  Hence it must import at least

\[
                  L-3H=m-6H+1=(1-o(1))m                         \tag{0.4}
\]

middle targets from outside the deleted packet.  At depth one, where
\(b_1=L-1\), the two signed rows require respectively at least

\[
                  m-6H-3\quad\hbox{and}\quad m-6H+3             \tag{0.5}
\]

outside targets.  Thus the same wall is already present simultaneously
in the first lower and upper trace rows.

More generally, deleting \(r\) packets cannot supply one new top from
their exposed middle rows unless

\[
                 r\ge \left\lceil\frac{L}{3H}\right\rceil
                  =\left(\frac13+o(1)\right)\frac mH.           \tag{0.6}
\]

There is also a global net-capacity inequality.  If the \(3r\) old
packet tops and \(u\) additional tops are replaced by CCTPF histories,
and only \(F\) middle targets are imported from outside the deleted
packet supports, then necessarily

\[
 F\ge uL-3r(M-L)=uL-3r(4H-1).                                  \tag{0.7}
\]

In particular, one packet and one new top require

\[
                         F\ge m-15H+4.                          \tag{0.8}
\]

A closed \(K\)-packet reservoir can therefore increase the number of
covered tops by at most

\[
       \left\lfloor\frac{3K(4H-1)}L\right\rfloor
        =O(KH/m).                                               \tag{0.9}
\]

For the signed dense bank

\[
 K=\left\lfloor\frac{W}{2P_H}\right\rfloor,
 \qquad P_H=m^{5/2+o(1)},                                      \tag{0.10}
\]

this is \(Wm^{-3+o(1)}\), whereas the critical CCTPF leave
\(N/\sqrt m\) is \(Wm^{-3/2+o(1)}\).  The reservoir's closed absorption
capacity is smaller by a factor \(m^{3/2-o(1)}\).

The port-weighted block theorem leads to the same verdict in its own
metric.  Removing the three CCTPF histories associated with one packet
can uncover at most a \(3kp_*\) fraction of the tail orders at any root.
Since

\[
 kp_*\le
 \exp\left\{-\left(\frac{\log2}{4}-o(1)\right)
                   \sqrt{m\log m}\right\},                    \tag{0.11}
\]

this supplies exponentially small, not fixed, exterior slack.  It does
not trigger iterative block growth across an order-one exterior wall.

Consequently the dense packet bank is a valid switching and signing
reservoir, but not a self-contained CCTPF absorber.  A positive
installation theorem must import a chain-aligned exterior reserve of
\((1-o(1))m\) compatible targets for each newly attached top, or must
use a genuinely multi-packet transverse construction involving
\(\Omega(m/H)\) packets at its first step.  No coefficient-one
conclusion follows here.

## 1. Cyclic rows visible from a second top

Let \(V\) be an \(M\)-set with a cyclic order \(\pi\).  For
\(1\le t<M\), let

\[
 \mathcal R_t(V,\pi)
   =\{V\setminus J:J\text{ is a cyclic interval of length }t
                         \text{ in }\pi\}.                    \tag{1.1}
\]

Thus \(\mathcal R_H(V,\pi)\) is the complete middle row of the
promotion frame, because its members have size \(M-H=m\).  The direct
rank-\((m-q)\) row is \(\mathcal R_{H+q}(V,\pi)\), and the direct
rank-\((m+q)\) row is \(\mathcal R_{H-q}(V,\pi)\).

### Lemma 1.1 (exact second-top interval bound)

Let \(U,V\) be \(M\)-sets, let \(d=|V\setminus U|\), and assume
\(t<M/2\).  Then

\[
 \left|\{X\in\mathcal R_t(V,\pi):X\subseteq U\}\right|
 \le
 \begin{cases}
 M,&d=0,\\
 t-d+1,&1\le d\le t,\\
 0,&d>t.
 \end{cases}                                                   \tag{1.2}
\]

In particular, if \(U\ne V\), the left side is at most \(t\).

#### Proof

Write \(D=V\setminus U\).  For a cyclic \(t\)-interval \(J\),

\[
                  V\setminus J\subseteq U
             \quad\Longleftrightarrow\quad D\subseteq J.      \tag{1.3}
\]

If \(d=0\), all \(M\) intervals work.  If \(d>t\), none works.
Suppose \(1\le d\le t\) and at least one interval works.  Cut the
cycle immediately outside a working interval.  In this linear
representation, let \(a\) and \(b\) be the first and last positions
of \(D\).  A length-\(t\) interval containing \(D\) has its initial
position in an interval of exactly \(t-(b-a+1)+1\) possible positions.
Since \(b-a+1\ge d\), this number is at most \(t-d+1\).  The hypothesis
\(t<M/2\) prevents a second family wrapping around the opposite side of
the chosen cut.  This proves (1.2). \(\square\)

The last appeal to \(t<M/2\) can also be phrased intrinsically: the
starting positions of all length-\(t\) intervals containing one fixed
nonempty set form one cyclic interval, because two disjoint wrapping
arcs would have total length at least \(M\).

## 2. The one-packet compatibility wall

Let \(P\) be a three-top packet.  Write its three top-frame pairs as

\[
                       (V_i,\pi_i),\qquad 0\le i\le2,          \tag{2.1}
\]

on either shore.  The middle-squarefree theorem says that

\[
 \mathcal O(P)=\bigcup_{i=0}^2\mathcal R_H(V_i,\pi_i),
 \qquad |\mathcal O(P)|=3M,                                   \tag{2.2}
\]

and the two shores have the same set \(\mathcal O(P)\).

### Theorem 2.1 (one packet cannot supply a fourth CCTPF root)

If \(U\) is an \(M\)-top distinct from \(V_0,V_1,V_2\), then

\[
             |\mathcal O(P)\cap\tbinom Um|\le3H.              \tag{2.3}
\]

Consequently no CCTPF history on \(U\) can take all of its \(L\)
middle masks from \(\mathcal O(P)\).  It must take at least \(L-3H\)
of them from the exterior.

#### Proof

For each \(i\), the sets in
\(\mathcal R_H(V_i,\pi_i)\cap\binom Um\) are precisely the members of
the middle row contained in \(U\).  Since \(U\ne V_i\), Lemma 1.1 with
\(t=H\) bounds their number by \(H\).  Sum over the three frames.
Possible cross-frame coincidences only decrease the union size.

A CCTPF history has exactly \(L\) pairwise distinct middle masks, all
contained in its top \(U\).  At most \(3H\) can belong to
\(\mathcal O(P)\), proving the final assertion. \(\square\)

This theorem uses the whole complete packet row, not merely the
\(L\) phases which would survive a CCTPF truncation.  It is therefore
an obstruction under the most generous possible packet-to-CCTPF
interface.

### Corollary 2.2 (the depth-one wall)

Under the CCTPF calibration, for all sufficiently large \(m\),

\[
                              b_1=L-1.                         \tag{2.4}
\]

For a fourth top \(U\), the complete packet rows contain at most
\(3(H+1)\) compatible direct lower targets at depth one and at most
\(3(H-1)\) compatible direct upper targets.  Thus a CCTPF history on
\(U\) imports at least the two quantities in (0.5).

#### Proof

Let \(\Lambda=W/N\).  The calibration gives
\(\Lambda\ge L+c_0H\) for a fixed \(c_0>0\).  Since

\[
 \frac{N_1}{N}=\frac{m}{m+1}\Lambda\ge L                    \tag{2.5}
\]

for all sufficiently large \(m\), the definition

\[
 b_1=\min\left\{L-1,
          \left\lfloor\frac{N_1}{N}\right\rfloor-1\right\}
\tag{2.6}
\]

gives (2.4).

Apply Lemma 1.1 to the three frames with \(t=H+1\) and \(t=H-1\).
Subtract the resulting bounds from \(b_1=L-1\):

\[
 \begin{aligned}
 (L-1)-3(H+1)&=m-6H-3,\\
 (L-1)-3(H-1)&=m-6H+3.
 \end{aligned}                                                \tag{2.7}
\]

These are positive under (0.2). \(\square\)

Global complementation carries the corresponding direct statement to
the physical root-form row, so the obstruction is not an artefact of
choosing one of the two equivalent descriptions.

## 3. Multi-packet thresholds

Let \(P_1,\ldots,P_r\) be reservoir packets.  Their complete middle
supports are pairwise disjoint.  Let \(U\) be a top not among their
\(3r\) packet tops.

### Theorem 3.1 (local compatibility threshold)

If a CCTPF history on \(U\) imports at most \(f\) middle targets from
outside \(\bigcup_{j=1}^r\mathcal O(P_j)\), then

\[
                         L\le3rH+f.                            \tag{3.1}
\]

In particular, a closed construction with \(f=0\) requires (0.6).

#### Proof

Apply Theorem 2.1 to every packet and sum.  At most \(3rH\) compatible
middle masks lie in the deleted packet union.  The history needs \(L\)
distinct middle masks, giving (3.1). \(\square\)

The estimate is local to the new top.  It is stronger by a factor four
than the aggregate capacity threshold below, because most owners of a
deleted packet are not visible from one fixed exterior top.

### Theorem 3.2 (global net-capacity inequality)

Delete \(r\) pairwise middle-disjoint full packets.  Suppose they are
replaced by CCTPF histories on their \(3r\) old tops and on \(u\)
additional tops.  Assume all new histories are middle-target-simple,
and let \(F\) be the number of their middle targets lying outside the
deleted union

\[
                    \bigcup_{j=1}^r\mathcal O(P_j).            \tag{3.2}
\]

Then (0.7) holds.

#### Proof

The deleted union has exactly \(3rM\) targets.  The \(3r+u\) new
CCTPF histories together require exactly \((3r+u)L\) distinct middle
targets.  At most \(3rM\) of them lie in (3.2), and exactly \(F\) lie
outside it.  Hence

\[
                     (3r+u)L\le3rM+F.                         \tag{3.3}
\]

Rearranging and using \(M-L=4H-1\) proves (0.7). \(\square\)

For \(r=u=1\), (0.7) is (0.8).  If \(F=0\), it gives

\[
 u\le\left\lfloor\frac{3r(4H-1)}L\right\rfloor.              \tag{3.4}
\]

Summing (3.4) over arbitrary disjoint absorber blocks proves (0.9).
There is no hidden gain from iterating: once a full packet has been
replaced by ordinary CCTPF histories, its excess \(3(M-L)\) owner slots
has been spent and does not regenerate.

### Corollary 3.3 (the dense reservoir is far below the critical leave)

At the calibration \(W/N=R_H=m^{1+o(1)}\), the signed dense reservoir
has

\[
 K=\frac{W}{2P_H}+O(1),\qquad P_H=m^{5/2+o(1)}.                \tag{3.5}
\]

Its closed growth capacity is

\[
 O(KH/m)=Wm^{-3+o(1)}.                                       \tag{3.6}
\]

On the other hand,

\[
                    \frac{N}{\sqrt m}=Wm^{-3/2+o(1)}.         \tag{3.7}
\]

Thus (3.6) is \(o(N/\sqrt m)\).

#### Proof

The dense-packing formula is

\[
 P_H=9M^2+
   \left(9+256\sum_{q=1}^Hq^2\right)\frac{W}{N}.              \tag{3.8}
\]

Here \(M=m^{1+o(1)}\), \(H=m^{1/2+o(1)}\), and \(W/N=m^{1+o(1)}\),
so (3.5) follows.  Substitute it into (0.9) to get (3.6).  Equation
(3.7) follows from \(N=Wm^{-1+o(1)}\). \(\square\)

## 4. What one packet does in the port metric

This section grants an additional interface hypothesis: the three
packet frames have been turned into three literal CCTPF histories
\(F_0,F_1,F_2\), each with a protected target set of cardinality

\[
                       k=L+2\sum_{q=1}^{H-1}b_q.               \tag{4.1}
\]

This hypothesis is not automatic.  The dense packet theorem supplies
complete cyclic frames, whereas CCTPF also prescribes fixed cores and a
nested tag history.  Granting the interface only strengthens the
putative absorber.

For a root \(U\), let \(\omega_U\) and \(\beta_U\) be respectively
the additive port exposure and the exact union-cylinder coverage from
the CCTPF block-augmentation theorem.  Let \(p_*\) be its largest
single-target port probability.

### Theorem 4.1 (one packet uncovers only an exponentially thin set)

Let \(\mathcal B\) be the protected target union of a target-simple
CCTPF matching containing \(F_0,F_1,F_2\), and put

\[
 \mathcal B_{\rm ext}
   =\mathcal B\setminus
       \bigl(P(F_0)\cup P(F_1)\cup P(F_2)\bigr).              \tag{4.2}
\]

Then, for every root \(U\),

\[
 \begin{aligned}
  0&\le\beta_U(\mathcal B)-\beta_U(\mathcal B_{\rm ext})
       \le3kp_*,\\
  \omega_U(\mathcal B_{\rm ext})
       &\ge\omega_U(\mathcal B)-3kp_*.
 \end{aligned}                                                \tag{4.3}
\]

If \(U\) was blocked before deletion, meaning
\(\beta_U(\mathcal B)=1\), then the fraction of its tail orders made
available by deleting the packet is at most

\[
                         3kp_*.                               \tag{4.4}
\]

At the calibration, (0.11) holds.

#### Proof

The cylinder union lost when passing from \(\mathcal B\) to
\(\mathcal B_{\rm ext}\) is contained in the union of the cylinders of
the three deleted histories.  Its normalized size is at most their
additive exposure.  The one-history port lemma bounds each exposure by
\(kp_*\), proving the first line of (4.3).

Additivity of \(\omega_U\), and target simplicity of the matching, give
the second line.  If \(\beta_U(\mathcal B)=1\), then

\[
 1-\beta_U(\mathcal B_{\rm ext})
   =\beta_U(\mathcal B)-\beta_U(\mathcal B_{\rm ext})
   \le3kp_*,                                                   \tag{4.5}
\]

which is (4.4).  Finally the calibrated CCTPF estimate is

\[
 \frac1{kp_*}\ge
 \exp\left\{\left(\frac{\log2}{4}-o(1)\right)
                  \sqrt{m\log m}\right\},                    \tag{4.6}
\]

equivalent to (0.11). \(\square\)

### Corollary 4.2 (necessary exposure window for ordered augmentation)

Consider the ordered block theorem after deleting one packet, so the
block consists of its three old roots and one blocked root \(U\).  If
\(U\) occupies position \(i\in\{1,2,3,4\}\) in the greedy order, a
necessary condition for the port estimate itself to certify that step
is

\[
             \omega_U(\mathcal B)<1+(4-i)kp_*.                \tag{4.7}
\]

In particular a blocked root, for which \(\omega_U(\mathcal B)\ge1\),
cannot be placed fourth.  Even in the first position its exposure must
lie in an interval of width only \(3kp_*\) above the critical value one.

#### Proof

At position \(i\), the ordered theorem requires

\[
 \omega_U(\mathcal B_{\rm ext})+(i-1)kp_*<1.                  \tag{4.8}
\]

Combine (4.8) with the second inequality in (4.3) and rearrange.  If
\(U\) is blocked, exact cylinder coverage one implies additive exposure
at least one. \(\square\)

Thus the block theorem and the packet reservoir do not concatenate into
a robust one-packet growth rule.  They concatenate only under a new,
exponentially precise hypothesis that the selected blocked root lies
within \(O(kp_*)\) of the additive exposure threshold.

### Corollary 4.3 (exact port saturation: one packet certifies at most
three blocked roots)

Delete one packet and adjoin \(u\) roots which were all blocked before
deletion.  If the ordered block-augmentation theorem certifies the
resulting block, then

\[
                              u\le3.                           \tag{4.9}
\]

More generally, deleting \(r\) packets permits that theorem to certify
at most \(3r\) previously blocked roots.

#### Proof

Deleting \(r\) packets removes \(3r\) histories and lowers the additive
exposure of any root by at most \(3rkp_*\).  If a previously blocked
root \(U\) occurs in position \(i\) of the ordered construction, then
\(\omega_U(\mathcal B)\ge1\), while the ordered hypothesis and the
exposure lower bound require

\[
 1-3rkp_*+(i-1)kp_*<1.                                       \tag{4.10}
\]

Thus \(i\le3r\).  Every previously blocked root must occupy one of the
first \(3r\) positions, proving that there are at most \(3r\) of them.
Set \(r=1\) for (4.9). \(\square\)

This is a limitation of the exact nonnegative-exposure certificate,
not a claim that a signed or cancellative augmentation cannot cross the
wall.  In particular it complements, rather than replaces, the stronger
literal-owner conclusion that a closed one-packet block cannot absorb
even one fourth top.

## 5. The optimistic shore-switch trace ledger

The preceding obstruction already closes self-contained one-packet
absorption.  For completeness, suppose a proposed absorber uses the
opposite shore of every consumed packet, because this is the only
currently audited way to retain the packet's all-depth floor control.
The dense packing has disjoint changed-target supports.  Therefore
switching \(r\) packets changes exactly

\[
                     8H(H+1)r                                \tag{5.1}
\]

targets in one nonzero physical description, and twice this number if
both complementary descriptions are counted.

### Proposition 5.1 (conditional closed-growth versus trace cost)

Suppose a proposed compiler consumes \(r\) reservoir packets and has
both of the following properties:

1. it is closed at the middle row, so all replacement middle targets
   lie in the deleted packet union; and
2. on every consumed packet it retains the audited opposite-shore
   derivative, so the packet's disjoint changed-target support is part
   of the compiler boundary.

If this compiler grows by \(u\) roots, then

\[
 r\ge\frac{uL}{3(4H-1)},                                     \tag{5.2}
\]

and hence its changed support in one physical description is at least

\[
 \frac{8H(H+1)uL}{3(4H-1)}
       =\left(\frac23+o(1)\right)umH.                         \tag{5.3}
\]

At \(u=N/\sqrt m\), this lower bound is

\[
       \left(\frac23+o(1)\right)\frac{NHm}{\sqrt m}
       =\left(\frac23+o(1)\right)W\frac H{\sqrt m},           \tag{5.4}
\]

which is \(W(\log m)^{1/2+o(1)}\) at (0.2), not \(o(W)\).

#### Proof

Equation (5.2) is (0.7) with \(F=0\).  Property 2 and the disjointness
of the reservoir derivatives make (5.1) an exact part of the boundary.
Multiply (5.2) by that exact per-packet support, and use
\(L=m(1-o(1))\) and
\(4H-1=4H(1+o(1))\), to obtain (5.3).  Finally
the calibrated identity \(W/N=m+O(H)\) gives (5.4). \(\square\)

This proposition is deliberately conditional.  A complete opposite
shore still occupies all \(3M\) packet owners, whereas owner slack is
obtained only after truncation or replacement.  No existing theorem
proves that these two operations can be combined while preserving the
full derivative.  An unknown replacement compiler could also have a
different trace boundary.  What the proposition proves is that any
interface retaining both already audited ledgers--closed maximal packet
slack and disjoint shore-switch traces--cannot repair the critical leave
with \(o(W)\) leakage.

## 6. Exact boundary

Proved:

1. the exact cyclic-incidence bound (1.2) between a packet frame and a
   second rank-\(M\) top;
2. the \(3H\) one-packet ceiling for compatible middle targets;
3. simultaneous middle and depth-one exterior imports of
   \((1-o(1))m\) for every fourth top;
4. the \(\Omega(m/H)\) multi-packet threshold for a closed local
   absorber;
5. the exact global net-capacity inequality (0.7), including the
   nonregeneration of packet slack;
6. the fact that the entire \(W/P_H\) reservoir has
   \(o(N/\sqrt m)\) closed growth capacity;
7. the exponentially thin \(3kp_*\) tail-order exposure created by one
   packet deletion;
8. the exact \(u\le3\) port saturation of the one-packet ordered
   certificate; and
9. the non-\(o(W)\) trace cost of scaling the presently audited
   shore-switch implementation to the critical leave.

Not proved:

1. impossibility of an absorber which imports a globally coordinated
   exterior owner reserve;
2. impossibility of a transverse block using \(\Omega(m/H)\) packets
   with nonlocal trace cancellation;
3. compatibility of the dense packet frames with the prescribed CCTPF
   fixed cores and nested tag histories; or
4. coefficient one.

The surviving positive statement is now exact.  One needs a
**chain-aligned exterior-reserve lemma**: for each new top, it must
supply \(L-3rH\) compatible middle targets and the corresponding
depth-one lower and upper targets, while preserving target simplicity,
for blocks of at least \(r\asymp m/H\) packet seeds.  A one-packet
absorber-growth lemma is false at the level of literal cyclic incidence,
even before the harder CCTPF chronology constraints are imposed.

## 7. Dependency ledger

The three-top packet identities and complete cyclic rows are in
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
The dense middle- and changed-target-disjoint reservoir and the definition
of \(P_H\) are in
`MATH_THEOREM_THREE_TOP_CONVEYOR_DENSE_ORBIT_PACKING_AND_SIGNING_20260727.md`.
The CCTPF quotas are in
`MATH_THEOREM_COMMON_CORE_TIGHT_PATH_FUSION_SUFFICES_20260726.md`.
The literal formula showing that every signed CCTPF target is a subset
of its rank-\(M\) root is (1.11), and its exact root--target incidence is
Theorem 2.1, of
`MATH_THEOREM_COMMON_CORE_TIGHT_PATH_CONFIGURATION_HYPERGRAPH_20260726.md`.
The additive port exposure, exact cylinder coverage, and ordered block
augmentation are in
`MATH_THEOREM_CCTPF_PORT_WEIGHTED_BLOCK_AUGMENTATION_AND_GLOBAL_WALL_20260727.md`.
