# The dense three-top reservoir cannot be a one-packet terminal CCTPF absorber

## Saturation caps one block at three new roots and forces a growing exterior-wall scale

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad
 R_H=\frac WN,\qquad
 M=m+H,
\tag{0.1}
\]

and use the calibrated CCTPF parameters

\[
 L=m-3H+1,\qquad
 k=L+2\sum_{q=1}^{H-1}b_q,\qquad
 \varepsilon=kp_*.
\tag{0.2}
\]

At

\[
 H=(1+o(1))\sqrt{m\log m},
\tag{0.3}
\]

assume the audited calibration

\[
 L+c_0H\le R_H\le m+C_0H
\tag{0.3a}
\]

for fixed positive constants \(c_0,C_0\). The audited estimates are

\[
 k=(\sqrt\pi+o(1))m^{3/2},
\qquad
 \log\frac1\varepsilon
 \ge
 \left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m}.
\tag{0.4}
\]

The dense conveyor reservoir has

\[
 K_0=\left\lfloor\frac W{P_H}\right\rfloor,
\qquad
 P_H=
 9M^2+
 \left(9+256\sum_{q=1}^Hq^2\right)R_H
\tag{0.5}
\]

pairwise root-disjoint and middle-owner-disjoint packets.

The exact conclusion is negative for one-packet terminal absorption.

> **Terminal cap.** Suppose the current target set is saturated against
> adding one CCTPF history on any unmatched root. If a block of \(r\)
> ordinary CCTPF histories is removed, then the ordered port-weighted
> block theorem can insert at most \(r\) unmatched roots. In particular,
> even granting the unproved hypothesis that one three-top reservoir
> packet is a target-simple block of three CCTPF histories, it can absorb
> at most three new roots.

Consequently a one-pass use of all \(K_0\) packets can certify an
increase of at most

\[
                              3K_0=o(N/\sqrt m).
\tag{0.6}
\]

The complete trace churn of all such replacements is at most

\[
                              9kK_0=o(W),
\tag{0.7}
\]

and the block theorem keeps all new owner and trace collisions equal to
zero. Thus leakage is not the problem: the gain is asymptotically too
small.

Even best-case monotone reuse of both packet shores changes only the
constant: an absorbed history necessarily meets the shore which was
removed, so that shore cannot be restored while the history is retained.
A two-shore packet therefore supports at most two exact-simple positive
uses, for total gain at most \(6K_0=o(N/\sqrt m)\).

The actual reservoir objects are complete three-frame packets, not
CCTPF history blocks. Even if one grants a mixed installation and
removes every one of their protected typed targets, one packet can put
only

\[
 c_{\rm full}
 :=
 \left\lceil\frac{3M(2H-1)}k\right\rceil
 =
 \left(\frac6{\sqrt\pi}+o(1)\right)\sqrt{\log m}
\tag{0.8}
\]

unmatched roots into the admissible initial positions. Hence a one-pass
use gives

\[
                         K_0c_{\rm full}=o(N/\sqrt m)
\tag{0.9}
\]

as well; monotone use of both shores contributes at most twice this.

More generally, any port-exposure argument using at most \(K_0\)
absorber blocks to repair a critical leave \(cN/\sqrt m\), \(c>0\),
must remove on average at least

\[
 \frac{cP_H}{R_H\sqrt m}-1
 \ge
 \frac{256c}{\sqrt m}\sum_{q=1}^Hq^2-1
 =
 \left(\frac{256c}{3}+o(1)\right)m(\log m)^{3/2}
\tag{0.10}
\]

CCTPF-history equivalents per block. A complete three-top packet has
only \(\Theta(\sqrt{\log m})\) such equivalents. This is the requested
quantitative exterior-wall obstruction.

The next possible absorber must therefore be a genuinely growing block
of average typed mass

\[
 \Omega\!\left(km(\log m)^{3/2}\right),
\tag{0.11}
\]

or it must use signed/cancellative information which is invisible to
the nonnegative exposure \(\omega\). Deleting or replacing one packet
does not close installation.

## 1. The exact saturation inequality

For a root \(U\), a typed target \(T\), and a target family
\(\mathcal B\), retain the CCTPF definitions

\[
 p_U(T)=\frac{|\mathcal C_U(T)|}{s!},
\qquad
 \omega_U(\mathcal B)=\sum_{T\in\mathcal B}p_U(T),
\qquad
 p_U(T)\le p_*.
\tag{1.1}
\]

Every CCTPF history \(F\) contains exactly \(k\) typed targets, so

\[
                         \omega_U(P(F))\le kp_*=\varepsilon
\tag{1.2}
\]

for every root \(U\).

Call an occupied target set \(\mathcal B\) **one-root saturated** if,
for every currently unmatched root \(U\), no CCTPF history on \(U\)
avoids \(\mathcal B\). Any partial installation can be extended greedily
until it is one-root saturated before an absorber is invoked.

### Lemma 1.1 (saturation forces unit additive exposure)

If \(\mathcal B\) is one-root saturated and \(U\) is unmatched, then

\[
                              \omega_U(\mathcal B)\ge1.
\tag{1.3}
\]

#### Proof

Let

\[
 \beta_U(\mathcal B)
 =
 \frac1{s!}\left|
 \bigcup_{T\in\mathcal B}\mathcal C_U(T)
 \right|
\tag{1.4}
\]

be the exact fraction of forbidden tail orders. Saturation says that
every order is forbidden, so \(\beta_U(\mathcal B)=1\). The union bound
gives

\[
                         \beta_U(\mathcal B)
                         \le\min\{1,\omega_U(\mathcal B)\},
\]

and (1.3) follows. \(\square\)

### Lemma 1.2 (exposure after deleting a block)

Let \(\mathcal Q\) be any removed typed target family of cardinality
\(R\), and put

\[
                    \mathcal B_{\rm ext}=\mathcal B\setminus\mathcal Q.
\tag{1.5}
\]

For every unmatched root \(U\),

\[
                 \omega_U(\mathcal B_{\rm ext})
                 \ge1-Rp_*.
\tag{1.6}
\]

If \(\mathcal Q\) is the union of \(r\) CCTPF histories, then

\[
                 \omega_U(\mathcal B_{\rm ext})
                 \ge1-r\varepsilon.
\tag{1.7}
\]

#### Proof

By Lemma 1.1, \(\omega_U(\mathcal B)\ge1\). Additivity and
\(p_U(T)\le p_*\) give

\[
 \omega_U(\mathcal B)-\omega_U(\mathcal B_{\rm ext})
 \le \sum_{T\in\mathcal Q}p_U(T)\le Rp_*.
\]

This proves (1.6). For \(r\) histories use \(R\le rk\). \(\square\)

Thus a three-history deletion leaves every previously unmatched root
behind the near-unit wall

\[
                        \omega_U(\mathcal B_{\rm ext})
                        \ge1-3\varepsilon=1-o(1).
\tag{1.8}
\]

In particular, the fixed half-exposure hypothesis which would allow an
exponentially large block is impossible at a one-root-saturated state.

The exposure recurrence also shows that a replacement cannot amplify
the released slack. If the removed family is \(\mathcal Q\), the newly
inserted target family is \(\mathcal G\), and
\(\mathcal G\cap\mathcal B_{\rm ext}=\varnothing\), then for every
untouched root \(V\),

\[
 \omega_V(\mathcal B_{\rm ext}\cup\mathcal G)
 =
 \omega_V(\mathcal B)
 -h_{\mathcal Q}(V)+g_{\mathcal G}(V),
\tag{1.9}
\]

where

\[
 0\le h_{\mathcal Q}(V)\le Rp_*,
\qquad
 g_{\mathcal G}(V)\ge0.
\tag{1.10}
\]

Here \(h_{\mathcal Q}(V)\) is the exposure of the targets actually
removed from \(\mathcal B\), a subset of \(\mathcal Q\), and
\(g_{\mathcal G}(V)=\omega_V(\mathcal G)\).
For a target-simple \(r\)-history block,
\(h_{\mathcal Q}(V)\le r\varepsilon\). Thus all new histories consume
nonnegative additive exposure; only the deleted block can create slack,
and it creates at most its own port mass.

## 2. The position cap in the ordered block theorem

The CCTPF ordered fill theorem selects roots
\(U_1,\ldots,U_a\) provided

\[
                 \omega_{U_i}(\mathcal B_{\rm ext})
                 +(i-1)\varepsilon<1
                 \qquad(1\le i\le a).
\tag{2.1}
\]

### Theorem 2.1 (general saturation-position cap)

Assume \(\mathcal B\) is one-root saturated, remove a typed family
\(\mathcal Q\) of size \(R\), and attempt to use (2.1). Every root which
was unmatched before the deletion must occur in a position \(i\)
satisfying

\[
                              i-1<\frac Rk.
\tag{2.2}
\]

Consequently the ordered theorem can insert at most

\[
                              \left\lceil\frac Rk\right\rceil
\tag{2.3}
\]

previously unmatched roots.

#### Proof

For a previously unmatched root, combine (1.6) with (2.1):

\[
                1-Rp_*+(i-1)kp_*<1.
\]

Since \(p_*>0\), division by \(kp_*\) gives (2.2). The nonnegative
integers \(i-1<R/k\) number exactly \(\lceil R/k\rceil\). \(\square\)

### Corollary 2.2 (an \(r\)-history block absorbs at most \(r\))

If the removed block consists of \(r\) histories, then the ordered
theorem can insert at most \(r\) previously unmatched roots.

#### Proof

Here \(R\le rk\), so (2.3) is at most \(r\). \(\square\)

For a hypothetical CCTPF-compatible three-top reservoir packet,
\(r=3\). Notice that the three old packet roots must also be filled, but
they can be placed after the unmatched roots. Thus the cap \(u\le3\) is
sharp as a consequence of positions; it does not mistakenly count the
old roots among the first three slots.

This theorem concerns what the current nonnegative port criterion can
certify. It does not assert that an augmentation using cancellations
cannot cross (1.8).

### Lemma 2.3 (a removed shore is spent by positive absorption)

Let the saturated target set have the disjoint form

\[
                         \mathcal B=\mathcal E\mathbin{\dot\cup}Q,
\tag{2.4}
\]

where \(Q\) is the currently installed shore of a packet. Suppose an
augmentation retains a new CCTPF history \(G\) on a previously unmatched
root and \(G\cap\mathcal E=\varnothing\). Then

\[
                                  G\cap Q\ne\varnothing.
\tag{2.5}
\]

Consequently \(Q\) cannot be restored in an exact target-simple table
while \(G\) is retained. A packet with two designated shores can be used
positively at most twice in a monotone exact-simple absorption process.

#### Proof

If \(G\cap Q=\varnothing\), then \(G\) avoids
\(\mathcal E\mathbin{\dot\cup}Q=\mathcal B\), contradicting saturation
at the previously unmatched root. Thus (2.5) holds. Exact target
simplicity forbids the simultaneous presence of \(G\) and \(Q\).

At a positive use, the current shore is therefore spent. In the best
case the other designated shore is installed and remains available for
one later use. That later positive use spends the second shore. \(\square\)

To reuse a spent shore, one must either remove or reconfigure a retained
blocking history \(G\), in which case the removable block has grown
beyond one packet, or accept a trace collision. The latter escape costs
at least one collision per retained blocker. Since a critical root leave
is itself \(o(W)\), this observation does not exclude a deliberately
leakage-tolerant construction; such a construction would additionally
have to prove that all unavoidable hits avoid the middle-owner row.

## 3. The actual complete-frame packet gives only
\(\Theta(\sqrt{\log m})\) positions

There is an additional type mismatch which must not be suppressed. A
CCTPF history has

\[
 L\ \text{middle targets},\qquad
 b_q\ \text{targets on each signed side at depth }q,
\tag{3.1}
\]

whereas a complete cyclic frame has \(M\) targets in each layer. Since

\[
                         M-L=4H-1>0,\qquad b_q<M,
\tag{3.2}
\]

an intact conveyor packet is not a three-edge block in the CCTPF
configuration hypergraph. No existing theorem supplies a simultaneous
target-simple truncation of its two shores.

One can nevertheless grant the most favorable mixed interpretation:
delete every protected target occurrence of the complete packet and
then install ordinary CCTPF histories on its roots and on new roots.
There are \(2H-1\) CCTPF typed layers—the middle and two sides for
\(1\le q<H\)—and three frames with \(M\) occurrences in each. Hence

\[
                             R\le r_{\rm pkt}=3M(2H-1).
\tag{3.3}
\]

Theorem 2.1 gives

\[
                              u\le c_{\rm full}
                              :=
                              \left\lceil\frac{r_{\rm pkt}}k\right\rceil.
\tag{3.4}
\]

Using (0.3)--(0.4),

\[
 \frac{r_{\rm pkt}}k
 =
 \frac{3(m+H)(2H-1)}
      {(\sqrt\pi+o(1))m^{3/2}}
 =
 \left(\frac6{\sqrt\pi}+o(1)\right)\sqrt{\log m},
\tag{3.5}
\]

which proves (0.8).

Deletion itself exposes at most

\[
 r_{\rm pkt}p_*
 =
 \exp\left\{
 -\left(\frac{\log2}{4}-o(1)\right)\sqrt{m\log m}
 \right\}
\tag{3.6}
\]

additive port mass at a root. Indeed,

\[
 \log\frac1{r_{\rm pkt}p_*}
 =
 \log\frac1{kp_*}-\log\frac{r_{\rm pkt}}k,
\]

and the second term is \(O(\log m)\). Thus complete-frame size does not
turn the near-unit wall into fixed positive slack.

## 4. The dense reservoir is too small at the terminal scale

First consider the stronger, hypothetical three-history decoration.
Across a one-pass use of all \(K_0\) packets, Corollary 2.2 gives total
certified gain at most \(3K_0\). Since \(K_0\le W/P_H\),

\[
 \frac{3K_0}{N/\sqrt m}
 \le
 \frac{3R_H\sqrt m}{P_H}
 \le
 \frac{R_H\sqrt m}{3M^2}
 =
 O(m^{-1/2}),
\tag{4.1}
\]

where \(P_H\ge9M^2\) and the calibration gives \(R_H=O(M)\). This proves
(0.6).

Lemma 2.3 permits at most two monotone exact-simple uses of the
two-shore menu. The upper bound becomes \(6K_0\), and the right side of
(4.1) merely doubles; it still tends to zero.

For complete-frame removal, (3.5) similarly gives

\[
 \frac{K_0c_{\rm full}}{N/\sqrt m}
 \le
 \frac{R_H\sqrt m}{P_H}
 \left(
  \left(\frac6{\sqrt\pi}+o(1)\right)\sqrt{\log m}+1
 \right)
 =
 O\left(\sqrt{\frac{\log m}{m}}\right)
 =o(1),
\tag{4.2}
\]

proving (0.9).

Again, using both designated shores only doubles the right side of
(4.2).

Thus the \(W/P_H\) reservoir is exponentially large in an absolute
sense, but polynomially too sparse relative to the critical root leave.
The exponential value of \(1/(kp_*)\) is irrelevant at saturation,
because the deleted block releases only \(R/k\) admissible initial
positions.

## 5. Owner and trace leakage are already negligible

Suppose, under the hypothetical three-history decoration, a packet
absorbs \(u\le3\) roots. It deletes three histories and inserts at most
six. Every history has \(k\) typed targets. Therefore the entire changed
typed-target occurrence set has cardinality at most

\[
                                  9k
\tag{5.1}
\]

per one-pass packet use. Across the reservoir this is at most

\[
 9kK_0
 \le
 \frac{9kW}{P_H}
 \le
 \frac{k}{M^2}W
 =
 O(W/\sqrt m)
 =
 o(W),
\tag{5.2}
\]

using \(P_H\ge9M^2\) and \(k=O(m^{3/2})\).

Using both shores doubles (5.2), which remains \(o(W)\).

Every successful ordered fill avoids the frozen exterior and all
earlier new histories. Hence its middle owners and every protected
target are literally collision-free. Equation (5.2) is only a churn or
worst-case repair bound; no collision is hidden in it.

The same conclusion holds for complete-frame removal. Its changed
occurrence count per packet is at most

\[
 r_{\rm pkt}+(3+c_{\rm full})k=O(MH),
\]

and hence over all packets it is

\[
 O(MHK_0)
 =
 O\left(\frac{MH}{P_H}W\right)
 =
 o(W).
\tag{5.3}
\]

Thus owner collisions and trace leakage do not rescue or obstruct the
lane. The obstruction is exclusively the number of new roots which can
cross the saturated exposure wall.

There is also a literal local owner-volume warning. Replacing a complete
three-frame packet by four CCTPF histories requires at least

\[
                           4L-3M=m-15H+4=\Theta(m)
\tag{5.4}
\]

middle owners outside the packet's old \(3M\)-owner support. Therefore
even one successful augmentation is not a closed local retile; it must
draw on exterior holes.

## 6. Necessary scale of a successor absorber

The position cap has an exact averaged consequence. Suppose an algorithm
works at one-root-saturated states, uses \(J\le K_0\) removed blocks
\(\mathcal Q_1,\ldots,\mathcal Q_J\), and relies on the ordered
nonnegative-exposure theorem. Put

\[
                              R_j=|\mathcal Q_j|.
\tag{6.1}
\]

If it inserts \(\ell\) previously unmatched roots, Theorem 2.1 gives

\[
                    \ell
                    \le
                    \sum_{j=1}^J\left\lceil\frac{R_j}{k}\right\rceil
                    \le
                    J+\frac1k\sum_{j=1}^JR_j.
\tag{6.2}
\]

Consequently

\[
                    \frac1J\sum_{j=1}^J\frac{R_j}{k}
                    \ge\frac{\ell}{J}-1.
\tag{6.3}
\]

Take \(\ell=cN/\sqrt m\), where \(c>0\) is fixed. Since
\(J\le K_0\le W/P_H\),

\[
 \frac{\ell}{J}-1
 \ge
 \frac{cP_H}{R_H\sqrt m}-1.
\tag{6.4}
\]

Now

\[
 \frac{P_H}{R_H}
 =
 \frac{9M^2}{R_H}
 +9
 +256\sum_{q=1}^Hq^2
 \ge
 256\sum_{q=1}^Hq^2.
\tag{6.5}
\]

Since

\[
 \sum_{q=1}^Hq^2
 =
 \frac{H(H+1)(2H+1)}6
 =
 \left(\frac13+o(1)\right)
 m^{3/2}(\log m)^{3/2},
\tag{6.6}
\]

equations (6.3)--(6.6) imply

\[
 \frac1J\sum_{j=1}^J\frac{R_j}{k}
 \ge
 \left(\frac{256c}{3}+o(1)\right)
 m(\log m)^{3/2}.
\tag{6.7}
\]

For \(c=1\), this is (0.10). Multiplication by \(k\) gives the target
mass in (0.11).

If both designated shores are counted as separate one-pass blocks, then
\(J\le2K_0\); the right side of (6.7) is divided by two and remains
\(\Theta(m(\log m)^{3/2})\).

A three-history packet has \(R_j/k\le3\). A complete conveyor packet has
\(R_j/k=O(\sqrt{\log m})\). Both miss (6.7) by a polynomial factor.
Thus a successor on this exposure route must group
\(\Omega(m(\log m)^{3/2})\) ordinary histories into one genuinely
nonlocal removable block, on average, and must control its interaction
with the unchanged exterior. The alternative is a signed augmentation
for which the nonnegative union bound (2.1) is not the governing
criterion.

## 7. Precise proved boundary

Proved:

1. one-root saturation implies \(\omega_U\ge1\) on every unmatched
   root;
2. deleting typed mass \(R\) leaves exposure at least \(1-Rp_*\);
3. the ordered CCTPF fill can then put unmatched roots only in the first
   \(\lceil R/k\rceil\) positions;
4. a three-history packet absorbs at most three new roots;
5. even complete-frame deletion absorbs only
   \((6/\sqrt\pi+o(1))\sqrt{\log m}\) roots by this criterion;
6. each packet shore is spent by a monotone exact-simple positive use,
   so even both shores of the whole \(W/P_H\) reservoir change only
   \(o(N/\sqrt m)\) roots;
7. owner collisions remain zero and total trace churn is \(o(W)\); and
8. a critical-scale terminal absorber needs average block mass
   \(\Omega(km(\log m)^{3/2})\), or a genuinely cancellative principle.

Not proved:

1. a target-simple CCTPF decoration of a complete conveyor packet;
2. a growing block with the scale in (6.7);
3. a signed augmentation crossing the near-unit wall; or
4. coefficient one.

Therefore the proposed iterative one-packet installation is
quantitatively closed. The next exact constructive statement is not
another local packet lemma: it is a growing-block augmentation of the
scale (6.7), or a replacement for additive port exposure.

## 8. Dependency ledger

The ordered port-exposure theorem and the estimate (0.4) are from
MATH_THEOREM_CCTPF_PORT_WEIGHTED_BLOCK_AUGMENTATION_AND_GLOBAL_WALL_20260727.md.
The reservoir size (0.5), its disjoint resources, and its \(o(W)\)
changed-support ledger are from
MATH_THEOREM_THREE_TOP_CONVEYOR_DENSE_ORBIT_PACKING_AND_SIGNING_20260727.md.
The fact that the reservoir objects are complete three-frame packets
with \(3M\) squarefree middle owners is from
MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md.
