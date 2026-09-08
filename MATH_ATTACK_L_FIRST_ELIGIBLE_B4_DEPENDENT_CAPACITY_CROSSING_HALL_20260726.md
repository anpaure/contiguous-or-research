# The first-eligible \(B_4\) atlas under exact dependent packet choices: labelled Hall cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent packet sampling is used.

## 0. Verdict

Put

\[
 W=W_m=\binom{2m}{m}.
\]

Fix the ordered four-block atlas and the first-\(r\)-eligible packetization
from `MATH_THEOREM_FIRST_ELIGIBLE_B4_SCD_PACKET_FACTOR_20260726.md`.  Exact
middle ownership does not make a strongly dependent packet choice possible:
it supplies only one depth-\(q\) occurrence per middle owner, and a labelled
Hall cut can ask where those occurrences are allowed to go.

Two statements are proved below.

### Theorem A (robust frozen-suffix Hall obstruction)

Assume

\[
 r\longrightarrow\infty,\qquad r=o(m),
 \qquad q=\lfloor A\sqrt m\rfloor\le \min\{H,r\},
 \qquad A>0\text{ fixed}.                         \tag{0.1}
\]

Allow an arbitrary integral or fractional exact-owner resolution by literal
components contained in the active coordinates of the first-eligible
packets.  This includes arbitrary global dependence, arbitrary packetwise
physical cube automorphisms in
\(\mathbb F_2^{2r}\rtimes S_{2r}\), arbitrary recursive direction orders,
repeated use of the two directions of one original \(B_4\)-block, and
arbitrary mixing of whole components, provided every retained owner has its
exact unit phase-incidence weight and no physical middle owner used by the
mixture has weight exceeding one.

For the fixed canonical support, the branch
\(U_{\mathrm{eff}}=U_m\) is available only when every phase vertex lies in
its raw packet.  Any component which merely shares the packet exterior but
imports other local owner states must use the appropriate owner-importing
branch of (3.7c), whether or not it comes from an adaptive scan.  If one
extends the statement to an adaptive mixed-seed first-eligible scan, the
requested seed at a fresh block must additionally be measurable from the
anchor and previously exposed scan data before that block is exposed.

Then there is an explicit labelled lower target family
\(\mathcal Z_{q,A}^-\subseteq\binom{[2m]}{m-q}\), and by complementation an
upper family \(\mathcal Z_{q,A}^+\), for which every integral resolution
misses

\[
 \boxed{(\kappa_A-o(1))W}                           \tag{0.2}
\]

targets of each sign.  Every fractional resolution has fractional uncovered
mass at least the same quantity.  Here \(\kappa_A>0\) is made explicit in
(4.12) below.

Thus no chronology-preserving capacity process confined to the fixed
first-eligible packets has aggregate holes \(o(W)\).  The conclusion is at
one depth and precedes every rounding question.

### Theorem B (sharper triangular crossing cut in the one-touch fibre)

Suppose additionally that the packet chronology is sibling-compatible: every
protected window of length \(q\le r\) changes \(q\) distinct original
four-blocks, once each.  Take

\[
 r=m^{3/4+o(1)}\text{ dyadic},\qquad h=2r,
 \qquad H=\left\lceil\sqrt{\beta m\log m}\right\rceil,
 \quad \frac12<\beta<1,                            \tag{0.3}
\]

and

\[
 q=\left\lceil20\sqrt{r\log m}\right\rceil.       \tag{0.4}
\]

For every arbitrarily correlated choice of one support-preserving relabelled
seed/order per packet, an integral choice misses

\[
 \boxed{(1-o(1))\binom{2m}{m-q}=(1-o(1))W}          \tag{0.5}
\]

targets of each sign.  The packet-choice LP has fractional uncovered mass
\((1-o(1))W\) as well.

The exact obstruction is the labelled triangular identity

\[
 L_q^-(T)=\kappa^-(P)+q,                            \tag{0.6}
\]

which places every candidate transversal in one source/target stratum.  This
is stronger than a probabilistic collision estimate.

Theorem A covers the full physical cube-automorphism/revisiting menu.  The
sharper Theorem B is deliberately restricted to the one-touch fibre.
Neither theorem rules out a
new atlas which transports coordinates through every positive-density
suffix, a nonlocal cross-packet owner trade, or unrestricted SCI owner
recycling.

## 1. What is a legal relabelled packet state?

On a four-block \(B=\{1,2,3,4\}\), the canonical owner support is

\[
 \mathcal A=\{14,12,23,34\}
 =\binom B2\setminus\{13,24\}.                     \tag{1.1}
\]

Its four owners form the physical square

\[
 14\longrightarrow12\longrightarrow23
 \longrightarrow34\longrightarrow14.             \tag{1.2}
\]

A coordinate relabelling is an owner-preserving state of this fixed square
if and only if it stabilizes the omitted perfect matching \(\{13,24\}\).
The legal local relabelling group therefore has order

\[
 |\operatorname {Stab}_{S_4}\{13,24\}|=8.          \tag{1.3}
\]

These eight labels change phase, orientation, and the names of the two cube
directions, but not the four middle owners.

The other sixteen labels move (1.1) to one of the other two four-state
supports.  They are not independent states of the same exact packet.  If
\(P_1,P_2,P_3\) are the three omitted perfect matchings and \(z_i\) is the
weight of the seed omitting \(P_i\), exact local ownership would require

\[
 z_2+z_3=1,\qquad z_1+z_3=1,\qquad z_1+z_2=1.      \tag{1.4}
\]

The unique solution is

\[
 z_1=z_2=z_3=\frac12.                              \tag{1.5}
\]

Hence there is no integral independent three-seed choice.  Using all three
supports requires a genuine repacketization or the completed common-owner
carrier.  Theorem A still applies to such a construction whenever its
components remain localized in the same early active blocks; Theorem B uses
the raw fixed support (1.1).

Inside a fixed packet \(P\cong Q_{2r}\), the physical cube automorphism
group

\[
 \operatorname {Aut}(Q_{2r})=
 \mathbb F_2^{2r}\rtimes S_{2r}                    \tag{1.6}
\]

is a legal owner-preserving menu.  This is not the full linear group
\(\operatorname {GL}(2r,2)\), whose general elements do not preserve cube
edges.  A cube automorphism can place both directions of one physical
four-block in the same protected window.  This is why Theorem B is not
claimed for the full cube-automorphism menu.  Theorem A has no one-touch
assumption and does cover it.

## 2. Exact dependent packet-choice dual

Let \(\mathfrak P\) be the retained packet partition, let \(\Theta_P\) be
any legal set of exact factor states on packet \(P\), and let
\(\mathcal I_{P,q}^-(\theta)\) be the set of distinct lower depth-\(q\)
targets emitted by state \(\theta\).  The fractional one-state-per-packet
hole programme is

\[
\begin{aligned}
 \eta_q^-:=\min\quad &\sum_T z_T,\\
 z_T+\sum_{P,\theta:\,T\in\mathcal I_{P,q}^-(\theta)}
       x_{P,\theta}&\ge1 &&(T),\\
 \sum_{\theta\in\Theta_P}x_{P,\theta}&=1 &&(P),\\
 x_{P,\theta},z_T&\ge0.
\end{aligned}                                      \tag{2.1}
\]

Linear-programming duality gives exactly

\[
 \boxed{
 \eta_q^-=
 \max_{0\le y_T\le1}
 \left\{
  \sum_Ty_T-
  \sum_{P\in\mathfrak P}
   \max_{\theta\in\Theta_P}
    \sum_{T\in\mathcal I_{P,q}^-(\theta)}y_T
 \right\}.}                                       \tag{2.2}
\]

The inequalities \(y_T\le1\) are supplied by the unit singleton-repair
columns.  Formula (2.2) already permits arbitrary fractional mixing inside
each packet; correlations between integral packet choices do not change any
deterministic value of its objective.

There is a still larger component relaxation.  Let \(\Pi(C)\) be the phase
set of a literal component, let \(o_C(\alpha)\) be the middle owner at phase
\(\alpha\), and put

\[
 \mu_C(X)=|\{\alpha\in\Pi(C):o_C(\alpha)=X\}|.
\]

Give every component \(C\) a weight \(x_C\ge0\) and require

\[
 \boxed{
 \sum_C\mu_C(X)x_C\le1
 \quad\left(X\in\binom{[2m]}m\right).}             \tag{2.3}
\]

An exact factor has equality at every owner it covers and has
\(\mu_C(X)\in\{0,1\}\); the at-most-one relaxation is only stronger for an
upper-capacity argument.  Crucially, (2.3) is imposed on every physical
middle owner which any component uses, including an owner imported from a
canonical leave or from another seed support.  For any target family
\(\mathcal Z\), the weighted number of phase occurrences which can land in
\(\mathcal Z\) is an upper bound on its covered mass.  Theorem A proves that
this capacity is smaller than \(|\mathcal Z|\) by \(\Omega(W)\), even under
(2.3).

Here a component is *contained in the packet's active coordinates* when all
of its phase vertices have one common restriction outside those coordinates.
Each weighted phase incidence contributes exactly one signed depth-\(q\)
occurrence, with cyclic phase indices and

\[
 \tau_{q,C}^-(\alpha)=\bigcap_{j=0}^q o_C(\alpha+j),
 \qquad
 \tau_{q,C}^+(\alpha)=\bigcup_{j=0}^q o_C(\alpha+j).             \tag{2.4}
\]

If \(\ell_q^\pm(T)\) is the resulting fractional target load,
its fractional uncovered mass is, throughout,

\[
 D_q^\pm=\sum_T(1-\ell_q^\pm(T))_+.                \tag{2.5}
\]

This is not a count of targets having literally zero fractional load.

## 3. Localization and suffix conservation

Partition all but at most three coordinates into ordered four-blocks

\[
 B_1<B_2<\cdots<B_b,\qquad b=\lfloor m/2\rfloor.   \tag{3.1}
\]

Put

\[
 j=\lfloor b/4\rfloor,\qquad
 R=\bigcup_{i=b-j+1}^{b}B_i,\qquad s=|R|.          \tag{3.2}
\]

Then

\[
 \frac{s}{2m}\longrightarrow\frac14.              \tag{3.3}
\]

Call a packet normal if its first \(r\) eligible blocks all precede \(R\).

### Lemma 3.1 (exponentially small exceptional owner mass)

For the canonical first-eligible atlas, if either \(r=o(m)\), or more
generally \(r\le m/16\), the number \(U_m\) of middle owners outside the
retained packet cover or in nonnormal packets satisfies

\[
 U_m\le e^{-c m}W                                  \tag{3.4}
\]

for some absolute \(c>0\) and all sufficiently large \(m\).

#### Proof

Before conditioning on rank, eligibility in each block has probability
\(4/16=1/4\).  The number of eligible blocks before \(R\) is

\[
 \operatorname {Bin}(b-j,1/4),
\]

whose mean is

\[
 \frac{b-j}{4}=\frac{3m}{32}+O(1).                 \tag{3.5}
\]

For \(r\le m/16\), failure to see \(r\) successes is a fixed lower-tail
deviation, so Chernoff gives probability \(e^{-\Omega(m)}\).  Failure of the
whole packet scan is smaller.  Conditioning on \(|X|=m\) multiplies this by
at most

\[
 \frac{2^{2m}}{\binom{2m}{m}}=O(\sqrt m),          \tag{3.6}
\]

which is absorbed in the exponential.  Context stability makes normality
constant on every packet.  This proves (3.4). \(\square\)

For a causal context-stable three-seed scan, packet stability forces the
requested support at a fresh block to be determined before that block is
exposed; its success probability is still \(1/4\).  The same proof applies.

If components indexed by canonical bad packets import owners, one must bound
the whole imported union.  Write \(U_m^{\mathrm{leave}}\) for the owner mass
outside the retained cover and \(U_m^{\mathrm{bad}}\) for the owner mass in
nonnormal retained packets, so
\(U_m=U_m^{\mathrm{leave}}+U_m^{\mathrm{bad}}\).  There are
\(U_m^{\mathrm{bad}}/4^r\) bad
canonical packets.  If every local imported state lies in the union of the
three rank-two \(B_4\) supports, one packet generates at most \(6^r\) owners,
so the envelope is

\[
 \left(\frac32\right)^rU_m^{\mathrm{bad}}.          \tag{3.7a}
\]

For completely arbitrary literal middle vertices on the same \(4r\) active
physical coordinates, one packet generates at most \(16^r\) local states,
giving the robust envelope

\[
 4^rU_m^{\mathrm{bad}}.                             \tag{3.7b}
\]

In what follows, write

\[
 U_{\mathrm{eff}}=
 \begin{cases}
 U_m,&\text{for the fixed canonical packet support},\\
 U_m^{\mathrm{leave}}+(3/2)^rU_m^{\mathrm{bad}},
   &\text{for the three-support rank-two union},\\
 U_m^{\mathrm{leave}}+4^rU_m^{\mathrm{bad}},
   &\text{for arbitrary states on the same active coordinates}.
 \end{cases}                                      \tag{3.7c}
\]

In every case \(U_{\mathrm{eff}}=e^{-\Omega(m)}W\), because \(r=o(m)\).
No raw-\(U_m\) claim is used for owner-importing menus.

### Lemma 3.2 (suffix conservation)

Let \(C\) be any literal component contained in the active coordinates of a
normal packet.  For every phase \(\alpha\in\Pi(C)\), with
\(X=o_C(\alpha)\), every depth \(q\), and both signs,

\[
 \tau_{q,C}^-(\alpha)\cap R=X\cap R,
 \qquad
 \tau_{q,C}^+(\alpha)\cap R=X\cap R.              \tag{3.8}
\]

#### Proof

All vertices of \(C\) agree outside the selected active blocks, and those
blocks are disjoint from \(R\).  Intersections and unions of consecutive
vertices therefore retain the common restriction to \(R\). \(\square\)

No common direction word, one-touch property, or intrapacket injectivity is
used in Lemma 3.2.

## 4. The robust labelled suffix Hall cut

For an integer \(a\), define

\[
\begin{aligned}
 \mathcal Z_{q,a}^-&=
 \left\{T\in\binom{[2m]}{m-q}:|T\cap R|\le a\right\},\\
 \mathcal Z_{q,a}^+&=
 \left\{T\in\binom{[2m]}{m+q}:|T\cap R|\ge s-a\right\},       \tag{4.1}
\end{aligned}
\]

and

\[
 B_a=\left|\left\{X\in\binom{[2m]}m:|X\cap R|\le a\right\}\right|.
                                                               \tag{4.2}
\]

By middle-layer complementation, \(B_a\) also counts middle owners with
\(|X\cap R|\ge s-a\).

### Proposition 4.1 (exact component Hall inequality)

Under the fractional exact-owner constraint (2.3), the total lower
phase-occurrence capacity in \(\mathcal Z_{q,a}^-\) is at most

\[
 B_a+U_{\mathrm{eff}},                              \tag{4.3}
\]

and the same bound holds above.  Consequently every integral exact-owner
resolution leaves at least

\[
 |\mathcal Z_{q,a}^{\pm}|-B_a-U_{\mathrm{eff}}    \tag{4.4}
\]

distinct signed targets uncovered.  For a fractional resolution, (4.4) is
a lower bound on fractional uncovered mass.

#### Proof

For a good component whose active coordinates avoid \(R\), Lemma 3.2 says
that a lower occurrence can lie in \(\mathcal Z_{q,a}^-\) only when its
owner satisfies \(|X\cap R|\le a\).  Therefore

\[
 \sum_{C\text{ good}}x_C
 \sum_{\alpha\in\Pi(C)}
 \mathbf 1_{\{\tau_{q,C}^-(\alpha)\in\mathcal Z_{q,a}^-\}}
 \le
 \sum_X\mathbf 1_{\{|X\cap R|\le a\}}
       \sum_{C\text{ good}}\mu_C(X)x_C
 \le B_a.                                         \tag{4.5}
\]

by (2.3).  Give every occurrence belonging to a bad/exceptional component
the most favorable possible target; the audited total weight of those
occurrences is at most \(U_{\mathrm{eff}}\).  Repeated
occurrences of one target cannot increase the number of distinct targets
hit.  Fractionally, if \(\ell(T)\) is the resulting target load, then

\[
 \sum_{T\in\mathcal Z_{q,a}^-}(1-\ell(T))_+
 \ge |\mathcal Z_{q,a}^-|-
     \sum_{T\in\mathcal Z_{q,a}^-}\ell(T),          \tag{4.5a}
\]

so the same capacity bound gives fractional uncovered mass (4.4).  The
upper proof is the complemented statement. \(\square\)

Now fix \(A>0\), put \(q=\lfloor A\sqrt m\rfloor\), and write

\[
 v=\frac{3}{32},\qquad d=A\sqrt{\frac23}.           \tag{4.6}
\]

For \(x>0\), let

\[
 a_m=\left\lfloor\frac{s}{2}-x\sqrt{vm}\right\rfloor.         \tag{4.7}
\]

The exact counts are

\[
\begin{aligned}
 B_{a_m}
 &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-t},\\
 |\mathcal Z_{q,a_m}^-|
 &=\sum_{t\le a_m}\binom st\binom{2m-s}{m-q-t}.    \tag{4.8}
\end{aligned}
\]

Stirling's formula applied uniformly for
\(t=s/2+O(\sqrt m)\) gives the hypergeometric limits

\[
 \frac{B_{a_m}}W\longrightarrow\Phi(-x),
 \qquad
 \frac{|\mathcal Z_{q,a_m}^{\pm}|}{W}
 \longrightarrow e^{-A^2}\Phi(d-x).               \tag{4.9}
\]

Here the suffix count has middle mean \(s/2\), lower-layer mean
\(s/2-(A/4+o(1))\sqrt m\), and variance \((v+o(1))m\); the upper statement
follows by complementation.  Also

\[
 \frac{\binom{2m}{m-q}}W\longrightarrow e^{-A^2}.  \tag{4.10}
\]

For a completely explicit positive choice, put

\[
 u_A=\max\left\{1,\frac{A^2+\log2+1}{d}\right\},
 \qquad x_A=d+u_A.                                  \tag{4.11}
\]

Writing \(\phi\) for the standard normal density, the standard Mills bounds

\[
 \frac{u}{u^2+1}\phi(u)\le\Phi(-u)\le\frac{\phi(u)}u
 \qquad(u>0)
\]

give

\[
 \frac{\Phi(d-x_A)}{\Phi(-x_A)}
 =\frac{\Phi(-u_A)}{\Phi(-(u_A+d))}
 \ge\frac{u_A(u_A+d)}{u_A^2+1}
       e^{u_Ad+d^2/2}
 >e^{A^2}.
\]

Define

\[
 \boxed{
 \kappa_A=e^{-A^2}\Phi(d-x_A)-\Phi(-x_A)>0.}       \tag{4.12}
\]

Equations (3.4), (4.4), (4.9), and (4.12) prove Theorem A.

## 5. The one-touch triangular crossing grid

Return to the fixed support \(\mathcal A\), and assume every protected
\(q\)-window touches \(q\) distinct selected four-blocks.  This property is
preserved by support-preserving local square automorphisms, phase and
orientation changes, arbitrary packetwise permutations of the selected
blocks, and recursive orders which keep the two directions of every original
block \(q\)-separated.

For a retained packet \(P\), let

\[
 a_1(P)<\cdots<a_r(P)<a_{r+1}(P)                   \tag{5.1}
\]

be its first \(r+1\) eligible \(\mathcal A\)-blocks, when the last exists,
and define

\[
 \kappa^-(P)=
 \#\left\{j<a_{r+1}(P):|P\cap B_j|=1\right\}.      \tag{5.2}
\]

If the \((r+1)\)-st eligible block does not exist, set
\(\kappa^-(P)=+\infty\).

For a lower target \(T\) having at least \(r-q+1\) eligible blocks, let
\(a_{r-q+1}(T)\) be its \((r-q+1)\)-st eligible position and put

\[
 L_q^-(T)=
 \#\left\{j<a_{r-q+1}(T):|T\cap B_j|=1\right\}.    \tag{5.3}
\]

### Lemma 5.1 (exact chronology transport)

For every packet state in the one-touch menu and every emitted lower
depth-\(q\) target \(T\),

\[
 \boxed{L_q^-(T)=\kappa^-(P)+q.}                   \tag{5.4}
\]

#### Proof

Exactly \(q\) of the first \(r\) eligible owner blocks are touched.  In an
untouched block the trace remains in \(\mathcal A\); in a touched block the
intersection of one local square edge is a singleton.  Thus \(r-q\) of the
first \(r\) eligible blocks remain eligible, and the next frozen eligible
block \(a_{r+1}(P)\) becomes exactly the \((r-q+1)\)-st eligible block of
the target.  Before it lie the \(\kappa^-(P)\) frozen singletons and the
\(q\) newly created singletons. \(\square\)

This is the labelled crossing-grid invariant: packet row \(c\) has support
only on target column \(c+q\).

There is an exact geometric-face census.  Let \(\mathfrak P_c\) be the
packets with \(\kappa^-=c\), and let \(\mathcal T_{q,c}\) be the lower
targets with \(L_q^-=c+q\).  In the full one-touch affine-face catalogue,
each target in \(\mathcal T_{q,c}\) has exactly

\[
 \binom{c+q}{q}                                     \tag{5.5}
\]

geometric face-candidate packets: choose the \(q\) singleton blocks to lift
to their unique local edges.  A restricted factor-state menu may realize
only a subset of these candidates, which can only strengthen the Hall
defect.  A packet has

\[
 \binom rq4^r                                       \tag{5.6}
\]

one-touch affine \(q\)-faces in the full geometric catalogue: choose the
\(q\) local blocks, one of their
two directions, and the fixed values of all inactive directions.  The local
edge trace identifies the face.  Hence double counting candidate
packet/face pairs gives

\[
 \boxed{
 |\mathcal T_{q,c}|\binom{c+q}{q}
 =|\mathfrak P_c|\binom rq4^r.}                    \tag{5.7}
\]

One exact factor state in a packet emits at most \(4^r\) distinct targets.
Consequently every integral or fractional packet choice has stratum defect
at least

\[
 \boxed{
 |\mathfrak P_c|4^r
 \left(\frac{\binom rq}{\binom{c+q}{q}}-1\right)_+.}            \tag{5.8}
\]

Equation (5.8) is the exact critical-transversal Hall inequality.  It is not
a statement about independent packet sampling.

## 6. Near-total failure at a protected sub-Gaussian depth

Define

\[
 \mathcal Y_q^-=
 \left\{T\in\binom{[2m]}{m-q}:
 a_{r-q+1}(T)\text{ exists and }L_q^-(T)\le r\right\}.           \tag{6.1}
\]

By Lemma 5.1, only packets satisfying

\[
 \kappa^-(P)\le r-q                              \tag{6.2}
\]

can emit a target in \(\mathcal Y_q^-\).  Since each such packet has
\(4^r\) owners and hence at most \(4^r\) depth-\(q\) occurrences, (2.2)
with \(y=\mathbf1_{\mathcal Y_q^-}\) gives

\[
 \eta_q^-
 \ge |\mathcal Y_q^-|-G_q^-,
 \qquad
 G_q^-=
 \sum_{P:\,\kappa^-(P)\le r-q}|P|.                \tag{6.3}
\]

We now evaluate both terms without any packet-selection probability.

Under independent fair middle bits, a block is in \(\mathcal A\) with
probability \(1/4\) and is a singleton with probability \(1/4\).  Suppress
all other blocks.  The resulting \(\mathcal A\)/singleton word is fair.
The event in (6.2) requires at least \(r+1\) \(\mathcal A\)-letters among
the first \(2r-q+1\) retained letters.  Hoeffding and conditioning on the
middle slice give

\[
 \boxed{
 \frac{G_q^-}{W}
 \le C\sqrt m
 \exp\left(-\frac{q^2}{4r+2}\right).}              \tag{6.4}
\]

For target counting use independent coordinate density

\[
 p_-=\frac{m-q}{2m}.                                \tag{6.5}
\]

In one block,

\[
 \Pr(\mathcal A)=4p_-^2(1-p_-)^2,
 \qquad
 \Pr(\text{singleton})=4p_-(1-p_-)^3.             \tag{6.6}
\]

After the other types are suppressed, the retained letter is
\(\mathcal A\) with exact probability \(p_-\).  If
\(L_q^-(T)>r\), then among the first \(2r-q+1\) retained letters there are
at most \(r-q\) \(\mathcal A\)-letters.  Their mean exceeds \(r-q\) by at
least \(q/3\) for all large \(m\), because \(r=o(m)\).  Hoeffding, the
exponentially unlikely failure to see \(r-q+1\) eligible blocks, and
conditioning on the exact target rank give

\[
 \boxed{
 \frac{|\mathcal Y_q^-|}{N_q}
 \ge1-C\sqrt m
 \left[
  \exp\left(-\frac{q^2}{20r}\right)+e^{-cm}
 \right],
 \qquad N_q=\binom{2m}{m-q}.}                      \tag{6.7}
\]

Take (0.4).  Then

\[
 \frac{q^2}{r}=400\log m+o(\log m),               \tag{6.8}
\]

so (6.4)--(6.7) yield

\[
 G_q^-=o(W),\qquad |\mathcal Y_q^-|=N_q-o(W).      \tag{6.9}
\]

Moreover

\[
 q=o(H),\qquad q=o(r),\qquad \frac{q^2}{m}=o(1),  \tag{6.10}
\]

and the exact layer ratio

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
 =\exp\left(-\frac{q^2}{m}+o(1)\right)             \tag{6.11}
\]

tends to one.  Substitution in (6.3) proves

\[
 \eta_q^-=(1-o(1))W.                               \tag{6.12}
\]

Full ground-set complementation acts blockwise, preserves \(\mathcal A\),
exchanges singletons with triples, and also complements the at most three
remainder coordinates.  It gives the identical upper statement

\[
 \eta_q^+=(1-o(1))W.                               \tag{6.13}
\]

For integral packet choices, (6.12)--(6.13) count literally missed physical
targets.  For fractional choices they count fractional uncovered mass.

The same calculation quantifies how much chronology breaking would be
needed to evade the sharper cut.  For a fixed integral or fractional
resolution, let \(B_q^\pm\) be the total mass of signed depth-\(q\)
occurrences which do not satisfy all hypotheses of Lemma 5.1.  Thus an
occurrence is exceptional if, for example, it leaves or changes its fixed
packet/support, changes the first-eligible boundary, or touches some selected
four-block at least twice.  Let \(D_q^\pm\) be the resolution's uncovered
mass.  Include the exponentially small unpacketized-owner mass in
\(B_q^\pm\), or absorb it in the displayed \(o(W)\).  Delete those
occurrences before applying Lemma 5.1, and then restore them with maximally
favorable targets.  This gives

\[
 \boxed{
 D_q^\pm\ge(1-o(1))W-B_q^\pm.}                    \tag{6.14}
\]

Thus sparse exceptions cannot clear the triangular cut.  An \(o(W)\)-hole
outcome requires

\[
 B_q^\pm\ge(1-o(1))W.                              \tag{6.15}
\]

Under the unit exact-owner normalization, the total phase-occurrence mass is
at most \(W+o(W)\), so (6.15) becomes
\(B_q^\pm=(1-o(1))W\): almost every occurrence at this depth must genuinely
break the original one-touch chronology.  Since one literal \(C_{2h}\)
supplies \(2h\) starts at a fixed depth, an additive \(o(W/h)\) family of
exceptional strips supplies only \(o(W)\) such occurrences and cannot repair
(6.12).

## 7. Independent audit and exact boundary

The decisive steps were audited independently.

1. The packet-choice dual (2.2) has no missing factor of \(2h\): a packet
   has \(4^r\) phase owners and hence at most \(4^r\) occurrences at one
   signed depth.
2. The source exponent in (6.4) is at least
   \(q^2/(4r+2)=100\log m+o(\log m)\); the middle-slice factor
   \(O(\sqrt m)\) is harmless.
3. The target exponent in (6.7) is
   \(q^2/(20r)=20\log m+o(\log m)\); exact-rank conditioning is again
   harmless.
4. The one-touch transport identity has the correct first-eligible boundary:
   the frozen \((r+1)\)-st owner-eligible block is precisely the target's
   \((r-q+1)\)-st eligible block.
5. Theorem B must not be extended to a full cube-direction permutation
   which revisits one physical \(B_4\)-block.  Theorem A is the audited
   obstruction for that larger menu.
6. Cross-support local relabellings are not independent states of the raw
   packet.  If they are made legal through a common-owner completion, the
   suffix proof uses the exceptional envelope (3.7c).

The constructive implication is therefore negative but sharp in scope:

\[
 \boxed{
 \begin{array}{c}
 \text{fixed first-eligible atlas + exact middle ownership}\\
 \text{+ components confined to its active coordinates}
 \end{array}
 \Longrightarrow
 \text{a labelled }\Omega(W)\text{ Hall defect}.}  \tag{7.1}
\]

The defect survives arbitrary dependence, adaptive packet exposure,
conditional expectation, local packet swaps, fractional mixtures, and total
unimodularity.  A coefficient-one construction must therefore perform at
least one operation absent from this atlas:

* change the ambient block order/support along the construction so that no
  common positive-density suffix remains frozen;
* splice or trade owners across packets with different suffix restrictions;
* use components which physically move suffix coordinates; or
* leave the exact-factor specialization and prove unrestricted SCI with
  controlled owner recycling.

No claim is made that unrestricted SCI is false.
