# First-eligible \(B_4\) packet choices: an exact triangular capacity Hall obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent packet-selection argument is used.

## 0. Verdict

Fix the first-eligible \(B_4\) packet partition and give every retained
packet one arbitrary relabelled sibling-compatible seed/order whose exact
factor has the proved property that every window of length \(q\le r\)
touches \(q\) distinct four-blocks. Middle ownership remains exact for every
joint packet choice.

There is nevertheless a deterministic target-side Hall obstruction. It is
caused by the first-eligible triangular rule itself.

Take

\[
 r=m^{3/4+o(1)},\qquad h=2r,
 \qquad
 H=\left\lceil\sqrt{\beta m\log m}\right\rceil,
 \quad \frac12<\beta<1,                              \tag{0.1}
\]

with \(r\) dyadic as required by the packet factor, and put

\[
 q=\left\lceil20\sqrt{r\log m}\right\rceil.         \tag{0.2}
\]

Then

\[
 q=o(H),\qquad q=o(r),\qquad q^2/m=o(1).             \tag{0.3}
\]

For either sign, every integral, fractional, adaptive, or globally dependent
choice of one allowed exact factor per retained packet misses

\[
 \boxed{(1-o(1))\binom{2m}{m-q}=(1-o(1))W}          \tag{0.4}
\]

physical targets at this single depth. The exponentially small unpacketized
middle leave changes (0.4) by only \(o(W)\).

Thus aggregate \(o(W)\) holes do not follow. More strongly, the fractional
packet-choice LP itself has a \((1-o(1))W\) hole optimum at depth \(q\).
Conditional expectation, local packet swaps, dependent rounding, and total
unimodularity cannot repair this fixed packetization: every allowed packet
column lies on the wrong side of the same triangular class cut.

The result does not obstruct all first-eligible ideas. It obstructs the
specific architecture in which the first \(r\) eligible blocks are fixed as
one owner packet and every allowed depth-\(q\) window touches each selected
four-block at most once. Escaping it requires a move that changes the
selected-block packet across the chronology, or a window/order primitive
which leaves that distinct-block regime.

## 1. The packet-choice LP and its exact dual

Let \(\mathfrak P\) be the retained first-eligible packet partition. Every
packet has

\[
 s=4^r                                                     \tag{1.1}
\]

middle owners. Let \(\Theta_P\) be any collection of allowed relabelled
seed/order exact factors on packet \(P\). For one sign and one depth \(q\),
write

\[
 \mathcal I_{P,q}(\theta)
 \subseteq \binom{[2m]}{m-q}                             \tag{1.2}
\]

for the set of distinct lower targets emitted by state \(\theta\). There
are \(s\) target occurrences, and packetwise injectivity gives
\(|\mathcal I_{P,q}(\theta)|=s\), although only the upper bound by \(s\)
will be needed.

The fractional one-choice-per-packet hole LP is

\[
 \begin{aligned}
 \eta_q^-:=\min\quad &\sum_Tz_T,\\
 \text{subject to}\quad
 &z_T+\sum_{P,\theta:\,T\in\mathcal I_{P,q}(\theta)}
       x_{P,\theta}\ge1 &&(T),\\
 &\sum_{\theta\in\Theta_P}x_{P,\theta}=1 &&(P),\\
 &x_{P,\theta},z_T\ge0.
 \end{aligned}                                          \tag{1.3}
\]

Its exact dual, after eliminating the free packet variables, is

\[
 \boxed{
 \eta_q^-=max_{0\le y_T\le1}
 \left[
  \sum_Ty_T-
  \sum_{P\in\mathfrak P}
   \max_{\theta\in\Theta_P}
    \sum_{T\in\mathcal I_{P,q}(\theta)}y_T
 \right].}                                             \tag{1.4}
\]

Indeed, the target-cover dual variables satisfy \(0\le y_T\le1\) because
of the singleton columns, while the free multiplier for
\(\sum_\theta x_{P,\theta}=1\) must dominate every packet-state weight.

The integral problem is obtained by requiring
\(x_{P,\theta}\in\{0,1\}\). Hence any lower bound from (1.4) applies to
every correlated or adaptive integral choice as well.

## 2. The exact triangular class invariant

Partition all but at most three coordinates into ordered four-blocks

\[
 B_1<B_2<\cdots<B_b,qquad b=\lfloor m/2\rfloor.    \tag{2.1}
\]

Use the local alphabets

\[
 \mathcal A=\{14,12,23,34\},
 \qquad
 \mathcal L=\binom{B_i}{1}.                          \tag{2.2}
\]

An \(\mathcal A\)-block is eligible. For a retained packet \(P\), let

\[
 a_1(P)<\cdots<a_r(P)                                \tag{2.3}
\]

be its selected first \(r\) eligible positions. The outside context is
fixed throughout \(P\). If it exists, let \(a_{r+1}(P)\) be the next
eligible position in that context and define

\[
 \kappa^-(P)=
 \#\{j<a_{r+1}(P):P|_{B_j}\in\mathcal L\}.          \tag{2.4}
\]

The selected positions themselves are in \(\mathcal A\), so they do not
contribute to (2.4). If there is no \((r+1)\)-st eligible block, put
\(\kappa^-(P)=+\infty\).

For a lower target \(S\) having at least \(r-q+1\) \(\mathcal A\)-blocks,
let \(a_{r-q+1}(S)\) be their \((r-q+1)\)-st position and put

\[
 L_q(S)=
 \#\{j<a_{r-q+1}(S):S|_{B_j}\in\mathcal L\}.        \tag{2.5}
\]

### Lemma 2.1 (triangular transport identity)

For every packet \(P\), every allowed packet state \(\theta\), and every
lower depth-\(q\) target \(S\) emitted from \(P\), if \(S\) has an
\((r-q+1)\)-st \(\mathcal A\)-block, then

\[
 \boxed{L_q(S)=\kappa^-(P)+q.}                       \tag{2.6}
\]

#### Proof

Every allowed \(q\)-window touches \(q\) distinct selected four-blocks.
In an untouched selected block the lower intersection remains in
\(\mathcal A\). In a touched selected block it is the intersection of one
edge of the relabelled local four-cycle and is therefore a singleton in
\(\mathcal L\).

Thus exactly \(q\) of the first \(r\) eligible owner blocks change from
\(\mathcal A\) to \(\mathcal L\). The other \(r-q\) remain in
\(\mathcal A\). No unselected eligible block occurs before
\(a_{r+1}(P)\), by the first-eligible definition. Consequently
\(a_{r+1}(P)\) is exactly the \((r-q+1)\)-st \(\mathcal A\)-block of the
target. Before it, the target has the \(\kappa^-(P)\) frozen singleton
blocks and the \(q\) newly touched singleton blocks. This proves (2.6).
\(\square\)

The identity is statewise. Relabelling the local seed changes which
singleton occurs, and changing the sibling-compatible direction order
changes which selected blocks are touched, but neither changes their number
or the first-eligible boundary.

## 3. An explicit dual target family

Define

\[
 \mathcal Y_q^-=
 \left\{S\in\binom{[2m]}{m-q}:
  a_{r-q+1}(S)\text{ exists and }L_q(S)\le r
 \right\}.                                           \tag{3.1}
\]

By Lemma 2.1, a packet with

\[
 \kappa^-(P)>r-q                                     \tag{3.2}
\]

emits no target in \(\mathcal Y_q^-\), under any allowed state. A packet
with \(\kappa^-(P)\le r-q\) has at most \(s\) emitted targets there. Put

\[
 G_q^-=sum_{P:\,\kappa^-(P)\le r-q}|P|.            \tag{3.3}
\]

Taking \(y_T=1\) on \(\mathcal Y_q^-\) and zero elsewhere in (1.4) gives

\[
 \boxed{\eta_q^-\ge|\mathcal Y_q^-|-G_q^-.}         \tag{3.4}
\]

This is the promised physical-target transversal cut. It applies before
any integrality question: the same inequality holds for fractional mixtures
of all relabelled seeds and orders.

## 4. Exact source census

Count middle owners by first taking independent fair bits and then
conditioning on total rank \(m\). In one four-block,

\[
 \Pr(\mathcal A)=\frac14,qquad
 \Pr(\mathcal L)=\frac14.                            \tag{4.1}
\]

After all other local types are erased, the \(\mathcal A/\mathcal L\)
word is a fair Bernoulli word. The event
\(\kappa^-(P)\le r-q\) says that the \((r+1)\)-st \(\mathcal A\) occurs
after at most \(r-q\) \(\mathcal L\)'s. In the first

\[
 n=(r+1)+(r-q)=2r-q+1                              \tag{4.2}
\]

retained letters, there must therefore be at least \(r+1\)
\(\mathcal A\)'s. The mean is \(n/2\), and the excess is at least \(q/2\).
Hoeffding gives

\[
 \Pr_{1/2}\{\kappa^-(P)\le r-q\}
 \le \exp\left(-\frac{q^2}{4r+2}\right).            \tag{4.3}
\]

The middle-slice event has probability \(\Theta(m^{-1/2})\). Therefore

\[
 \boxed{
 \frac{G_q^-}{W}
 \le C\sqrt m\exp\left(-\frac{q^2}{4r+2}\right).}  \tag{4.4}
\]

There is no packet-selection probability in this argument. Equation (4.4)
is only a census of the deterministic packet classes.

## 5. Exact target census

For lower targets use independent coordinate density

\[
 p_-:=\frac{m-q}{2m}.                                \tag{5.1}
\]

This product law has mean rank exactly \(m-q\). In one block,

\[
 \Pr(\mathcal A)=4p_-^2(1-p_-)^2,
 \qquad
 \Pr(\mathcal L)=4p_-(1-p_-)^3.                    \tag{5.2}
\]

After erasing the other local types, the retained letter is
\(\mathcal A\) with exact probability

\[
 \frac{4p_-^2(1-p_-)^2}
 {4p_-^2(1-p_-)^2+4p_-(1-p_-)^3}
 =p_-.                                               \tag{5.3}
\]

Put \(a=r-q+1\) and \(n=a+r=2r-q+1\). If more than
\(r\) \(\mathcal L\)'s occur before the \(a\)-th
\(\mathcal A\), then among the first \(n\) retained letters there are at
most \(a-1=r-q\) \(\mathcal A\)'s. Their mean is \(np_-\), and

\[
 np_--(r-q)
 =\frac q2+\frac12-rac{q(2r-q+1)}{2m}
 \ge\frac q3                                           \tag{5.4}
\]

for all sufficiently large \(m\), because \(r=o(m)\). Since \(n\le3r\),
Hoeffding gives

\[
 \Pr_{p_-}\{L_q(S)>r\}
 \le \exp\left(-\frac{q^2}{20r}\right)+e^{-c m}.    \tag{5.5}
\]

The final term charges the event that the finite block word has fewer than
\(a\) \(\mathcal A\)-letters at all; its mean number of such letters is
\(\Theta(m)\), while \(a=o(m)\).

By Stirling's formula, the exact-rank event under (5.1) has probability at
least \(c_0m^{-1/2}\), uniformly here. Conditioning (5.5) on that event
therefore gives

\[
 \boxed{
 \frac{|\mathcal Y_q^-|}{N_q}
 \ge1-C\sqrt m
  \left[
   \exp\left(-\frac{q^2}{20r}\right)+e^{-cm}
  \right],
 \qquad N_q=\binom{2m}{m-q}.}                       \tag{5.6}
\]

Again, this is a uniform-slice census, not randomized packet selection.

## 6. The Gaussian-window obstruction

For (0.2),

\[
 \frac{q^2}{r}=400\log m+o(\log m).                 \tag{6.1}
\]

Equations (4.4) and (5.6) imply

\[
 G_q^-=o(W),
 \qquad
 |\mathcal Y_q^-|=N_q-o(W).                         \tag{6.2}
\]

Also \(q=o(m^{2/3})\), and the exact central-layer ratio satisfies

\[
 \log\frac{N_q}{W}
 =-\frac{q^2}{m}
  +O\left(\frac qm+\frac{q^3}{m^2}\right)=o(1).    \tag{6.3}
\]

Thus

\[
 N_q=(1-o(1))W.                                      \tag{6.4}
\]

Substituting (6.2)--(6.4) in the dual cut (3.4) proves

\[
 \boxed{\eta_q^-=(1-o(1))W.}                        \tag{6.5}
\]

The reverse inequality is trivial because the target layer has size
\((1-o(1))W\), so (6.5) is an asymptotic equality.

The upper sign has the identical obstruction. Replace
\(\mathcal L\) by the four local triples \(\mathcal U=\binom{B_i}{3}\).
Under fair middle bits, \(\mathcal A\) and \(\mathcal U\) again have equal
probability. Under upper-target density
\(p_+=(m+q)/(2m)\), the retained \(\mathcal A/\mathcal U\) word has
\(\mathcal U\)-probability exactly \(p_+\). The same calculation gives

\[
 \boxed{\eta_q^+=(1-o(1))W.}                        \tag{6.6}
\]

## 7. Consequences and exact scope

1. **No dependent packet-choice rescue.** The obstruction is a feasible
   dual weight for the fractional packet-choice LP. It therefore survives
   arbitrary dependence, adaptive exposure, conditional expectation, and
   local swaps among the allowed packet states.
2. **No TU rescue.** Total unimodularity could remove an integrality gap,
   but (6.5)--(6.6) already hold in the fractional relaxation. The failure
   is target-side capacity, not rounding.
3. **Candidate support is not capacity.** Almost every target has at least
   one packet-local candidate, as proved by the earlier support theorem.
   Targets in \(\mathcal Y_q^-\) typically have many formal completions, but
   they all draw their one-factor occurrence capacity from the rare source
   packets with \(\kappa^-(P)\le r-q\).
4. **Constant-one relevance.** One lower depth alone has \((1-o(1))W\)
   holes. Adding only \(o(W/h)\) extra strips, the most compatible repair
   with an \(o(W)\) word budget, supplies only \(o(W)\) additional target
   occurrences. Hence this fixed first-eligible exact-factor architecture
   cannot yield coefficient one.
5. **Escape condition.** A positive construction must change the packet
   boundary during the chronology, permit cross-packet owner trades, or use
   a local order in which the protected depth can revisit a selected
   four-block. Merely relabelling the seed, permuting the selected blocks,
   choosing another sibling-compatible recursive order, or correlating
   those choices globally preserves (2.6).

No claim is made against the weaker unrestricted SCI program, which may
recycle middle owners and select arbitrary physical strips not forming one
factor per fixed first-eligible packet.
