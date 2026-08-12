# Parity-complete local trace codes do not solve the two-sign outer packet Hall problem

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent packet sampling is used.

## 0. Verdict

Grant the parity-complete local trace-code gate in full: every retained
first-eligible packet may choose an arbitrary physical parity mapping,
seed, affine phase, factor resolution, and direction order, and its lower
and upper trace codes may be exactly injective at every protected depth.
Allow the packet choices to be arbitrarily dependent.

This still does not give aggregate \(o(W)\) holes for the fixed ordered
first-eligible atlas. The parity gate changes the target labels emitted
inside a packet, but it does not move a physical coordinate of the common
frozen suffix.

Fix \(A>0\), let

\[
 q=\lfloor A\sqrt m\rfloor\le\min\{H,r\},
 \qquad r=o(m),                                     \tag{0.1}
\]

and put \(W=\binom{2m}{m}\). There is an explicit constant
\(\kappa_A>0\) and explicit labelled target families

\[
 \mathcal Z_{q,A}^-subseteq\binom{[2m]}{m-q},
 \qquad
 \mathcal Z_{q,A}^+\subseteq\binom{[2m]}{m+q}       \tag{0.2}
\]

such that every integral packetwise choice has

\[
 M_q^-\ge(\kappa_A-o(1))W,
 \qquad
 M_q^+\ge(\kappa_A-o(1))W.                          \tag{0.3}
\]

The exact coupled two-sign packet LP has fractional singleton deficit at
least

\[
 \boxed{(2\kappa_A-o(1))W}                          \tag{0.4}
\]

at this one depth. Hence no dependent packetwise mapping/seed/order choice
confined to the fixed first-eligible supports can prove coefficient one.

The result permits completed-pair windows, repeated visits to one active
block, arbitrary physical cube automorphisms, and arbitrary trace-code
quality. It fails to apply only if the new construction physically changes
the suffix support, changes the ambient atlas, trades owners between
different suffix fibres, or leaves the exact-owner packet specialization.

## 1. Exact coupled two-sign packet LP

Let \(\mathfrak P\) be the retained owner-disjoint packet partition. For a
packet \(P\), let \(\Theta_P\) be the complete allowed menu of physical
parity-complete factor states. A state \(\theta\) determines, simultaneously
for every \(1\le q\le H\) and both signs, physical target sets

\[
 \mathcal I_{P,q}^\epsilon(\theta),
 \qquad \epsilon\in\{-,+\}.                         \tag{1.1}
\]

The exact fractional all-depth, two-sign singleton-repair programme is

\[
\begin{aligned}
 \eta^{\pm}:=\min\quad
 &\sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
   \sum_{T\in V_q^\epsilon}z_{q,T}^\epsilon,\\
 z_{q,T}^\epsilon+
 &\sum_{P,\theta:\,T\in\mathcal I_{P,q}^\epsilon(\theta)}
 x_{P,\theta}\ge1
 &&(q,\epsilon,T),\\
 &\sum_{\theta\in\Theta_P}x_{P,\theta}=1
 &&(P),\\
 &x_{P,\theta},z_{q,T}^\epsilon\ge0,
\end{aligned}                                       \tag{1.2}
\]

where

\[
 V_q^-:=\binom{[2m]}{m-q},
 \qquad
 V_q^+:=\binom{[2m]}{m+q}.                          \tag{1.3}
\]

The same state variable appears at every sign and depth; no separate
rankwise choice has been introduced.

Linear-programming duality gives

\[
\boxed{
 \eta^{\pm}=
 \max_{0\le y_{q,T}^\epsilon\le1}
 \left[
  \sum_{q,\epsilon,T}y_{q,T}^\epsilon
  -\sum_{P\in\mathfrak P}
   \max_{\theta\in\Theta_P}
   \sum_{q,\epsilon}
   \sum_{T\in\mathcal I_{P,q}^\epsilon(\theta)}
      y_{q,T}^\epsilon
 \right].}                                         \tag{1.4}
\]

The caps \(y\le1\) are exactly the dual constraints from the singleton
columns. Any globally correlated random choice is a distribution on integral
joint states. Since the cut below holds for every outcome and for the larger
fractional relaxation (1.2), dependence cannot evade it.

For clarity, if \(\ell_{q}^\epsilon(T)\) is a fractional target load, its
uncovered mass is

\[
 D_q^\epsilon=
 \sum_{T\in V_q^\epsilon}(1-\ell_q^\epsilon(T))_+.  \tag{1.5}
\]

For integral loads, (1.5) is exactly the number of missed targets.

## 2. What the parity-complete gate does and does not change

The parity lift pairs local directions and may use a context-dependent
coarse order. Its local trace-code gate can, in principle, recover all
parity information erased by completed pairs. None of those operations
changes the following support fact.

Reserve the terminal quarter of the ordered four-block atlas:

\[
 R=\bigcup_{i=b-j+1}^bB_i,
 \qquad b=\lfloor m/2\rfloor,
 \qquad j=\lfloor b/4\rfloor,
 \qquad s=|R|.                                      \tag{2.1}
\]

Then

\[
 \frac{s}{2m}\longrightarrow\frac14.              \tag{2.2}
\]

All but \(e^{-\Omega(m)}W\) middle owner mass reaches its first \(r=o(m)\)
eligible blocks before \(R\). On every such normal packet, every physical
component supported on its selected active coordinates has one common
restriction to \(R\). Therefore, for every phase owner \(X\), every order,
every number of repeated active-block visits, and both signs,

\[
 \tau_{q,C}^-(X)\cap R=X\cap R,
 \qquad
 \tau_{q,C}^+(X)\cap R=X\cap R.                    \tag{2.3}
\]

The proof is literal: all vertices in the component agree on \(R\), so their
intersection and union agree there as well.

If an enlarged mixed-seed menu imports owners from the other local supports,
use the effective exceptional occurrence mass

\[
 U_{\mathrm{eff}}
 =U_m^{\mathrm{leave}}+(3/2)^rU_m^{\mathrm{bad}}
 =e^{-\Omega(m)}W.                                  \tag{2.4}
\]

For a causal packet-stable mixed-seed scan, the requested seed is predictable
before a fresh block is exposed, so its success probability remains \(1/4\)
and the same localization estimate holds. No independent packet choice is
used.

## 3. A coupled two-sign literal occurrence cut

For an integer \(a<s/2\), define

\[
\begin{aligned}
 \mathcal Z_{q,a}^-&=
  \{T\in V_q^-:|T\cap R|\le a\},\\
 \mathcal Z_{q,a}^+&=
  \{T\in V_q^+:|T\cap R|\ge s-a\},                \tag{3.1}
\end{aligned}
\]

and

\[
 B_a=\left|\left\{X\in\binom{[2m]}m:
                   |X\cap R|\le a\right\}\right|. \tag{3.2}
\]

Middle complementation gives the same number \(B_a\) of owners with
\(|X\cap R|\ge s-a\). Since \(a<s/2\), the two owner events are disjoint.

### Lemma 3.1 (two-sign occurrence capacity)

For every integral or fractional exact-owner packet resolution, the total
target-load capacity in the two labelled families satisfies

\[
 \boxed{
 \sum_{T\in\mathcal Z_{q,a}^-}\ell_q^-(T)
 +\sum_{T\in\mathcal Z_{q,a}^+}\ell_q^+(T)
 \le2B_a+2U_{\mathrm{eff}}.}                        \tag{3.3}
\]

#### Proof

For a good component, (2.3) says that a lower occurrence belongs to
\(\mathcal Z_{q,a}^-\) exactly when its starting owner lies in the lower
owner event of size \(B_a\). The upper statement is the complementary owner
event, also of size \(B_a\). Summing component weights first at each owner
and using exact middle ownership gives total good occurrence weight at most
\(2B_a\).

An exceptional weighted phase owner can contribute at most one lower and one
upper occurrence, so all exceptional components add at most
\(2U_{\mathrm{eff}}\). This proves (3.3). \(\square\)

Consequently

\[
 \boxed{
 D_q^-+D_q^+
 \ge|mathcal Z_{q,a}^-|+|mathcal Z_{q,a}^+|
      -2B_a-2U_{\mathrm{eff}}.}                     \tag{3.4}
\]

This is also obtained directly from (1.4) by setting the two dual target
weights equal to one on (3.1), zero elsewhere, and using (3.3) to bound the
packet maxima. Notice that local trace injectivity can only make each packet
use its allowed capacity efficiently; it cannot increase that capacity.

## 4. Exact Gaussian evaluation and explicit constant

Put

\[
 q=\lfloor A\sqrt m\rfloor,
 \qquad
 v=\frac3{32},
 \qquad
 d=A\sqrt{\frac23}.                                \tag{4.1}
\]

For \(x>0\), let

\[
 a_m=\left\lfloor\frac s2-x\sqrt{vm}\right\rfloor. \tag{4.2}
\]

The exact hypergeometric counts satisfy

\[
 \frac{B_{a_m}}W\longrightarrow\Phi(-x),
 \qquad
 \frac{|\mathcal Z_{q,a_m}^-|}W
 =\frac{|\mathcal Z_{q,a_m}^+|}W
 \longrightarrow e^{-A^2}\Phi(d-x).               \tag{4.3}
\]

For a fully explicit positive choice, put

\[
 u_A=\max\left\{1,\frac{A^2+\log2+1}{d}\right\},
 \qquad
 x_A=d+u_A,                                         \tag{4.4}
\]

and define

\[
 \boxed{
 \kappa_A=
 e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0.}                \tag{4.5}
\]

The positivity follows from the Mills bounds:

\[
 \frac{\Phi(-u_A)}{\Phi(-(u_A+d))}
 \ge
 \frac{u_A(u_A+d)}{u_A^2+1}
 e^{u_Ad+d^2/2}
 >e^{A^2}.                                         \tag{4.6}
\]

Substitute (4.3)--(4.5) into (3.4). Since
\(U_{\mathrm{eff}}=o(W)\),

\[
 \boxed{D_q^-+D_q^+\ge(2\kappa_A-o(1))W.}          \tag{4.7}
\]

Using only one of the two dual families gives separately

\[
 \boxed{
 D_q^-\ge(\kappa_A-o(1))W,
 \qquad
 D_q^+\ge(\kappa_A-o(1))W.}                        \tag{4.8}
\]

This proves (0.3)--(0.4).

## 5. Constant-one implication and exact escape boundary

The obstruction occurs at one protected Gaussian depth. Thus an aggregate
\(o(W)\) target deficit is impossible inside this architecture, even after
the local parity-complete trace-code theorem is granted exactly.

Adding \(o(W/h)\) extra physical strips cannot repair the cut: each strip
supplies only \(2h\) lower and \(2h\) upper occurrences at the fixed depth,
so the total additional two-sign capacity is \(o(W)\). Literal singleton
repair of the remaining deficit costs \(\Omega_A(W)\) output positions.

The theorem does not say that parity-complete trace codes are useless. They
solve a genuine intrapacket problem: completed-pair transport and recovery of
the erased local parity context. They simply do not solve the independent
outer occurrence-capacity problem.

To evade the dual cut, a positive construction must perform at least one of
the following:

1. use enough ambient block atlases that no common positive-density suffix is
   frozen;
2. move physical coordinates into and out of \(R\) along the components;
3. trade or splice owners across different suffix fibres; or
4. leave the exact-owner packet architecture and solve unrestricted SCI with
   controlled owner recycling.

These are necessary escape categories, not sufficient constructions. No
claim is made against unrestricted SCI.
