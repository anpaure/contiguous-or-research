# Random relabelling of repaired twelve-top packets: exact owner collisions and the colour-capacity gate

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\]

and

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},\qquad
 \lambda=\frac WN.
\]

Consider a fixed near-perfect matching of the repaired twelve-top
packets. Randomize different packets independently by uniformly
permuting their common-core roles; this is a physical relabelling which
preserves all twelve tops and the repaired recharge identity.

The exact conclusions are as follows.

1. Every repaired packet shore has

   \[
   12H
   \]

   middle owners retaining one outside label and

   \[
   12(d-H)
   \]

   middle owners retaining two outside labels. Each of the six outside
   labels occurs in exactly \(2H\) owners of the first kind.

2. For an arbitrary fixed top-packet matching, the expected pair
   collision mass and expected collision excess have exact formulas in
   terms of the packetwise one-owner probabilities; see (3.2) and
   (3.4). In particular they are not determined by \(m,H,N,W\) alone:
   they retain the cross-incidence profile of the fixed packet cores and
   outside six-sets.

3. Nevertheless, in the calibrated regime

   \[
   H=o(m),\qquad \lambda=M+O(H),\qquad \lambda\ge M,
   \]

   every near-perfect layer satisfies the universal lower bounds

   \[
   \mathbb E\,\operatorname{Pair}
      \ge \left(\frac12-o(1)\right)W,
   \qquad
   \mathbb E\,\operatorname{Excess}
      \ge (e^{-1}-o(1))W.
   \]

   Thus independent packetwise relabelling produces linear collisions
   with probability \(1-\exp[-\Omega(W/m)]\) even in one layer. This
   does not exclude an exponentially rare deterministic good
   assignment. Across \(L=\Theta(m)\) preassigned layers its expected
   collision excess is \(\Theta(mW)\).

4. There is, however, a different positive multilevel statement. Pool
   \(L=(1+o(1))m\) top-disjoint layers and randomize every packet
   independently. Let \(D_X\) be the total number of packet shores in
   the pool containing the middle owner \(X\). At the calibrated height,

   \[
   \mathbb E\sum_X(D_X-L)_+\le Wm^{-4+o(1)}.
   \]

   Hence one realization, after deleting at most
   \(Wm^{-4+o(1)}\) packets and only \(Wm^{-3+o(1)}=o(W)\)
   owner incidences, has owner degree at most \(L\) and top degree at
   most \(L\). This is an exact capacity statement for an
   \(L\)-colour resolution. It does not colour the packets.

5. The remaining deterministic gate is therefore a near-class-one
   edge-colouring theorem for the top-plus-owner packet resource
   hypergraph. The elementary packet-pair Lovasz-local-lemma calculation
   misses by a factor \(\Theta(m)\). A successful argument must correlate
   colours globally; the ordinary independent-relabel plus
   variable-LLL certificate is unavailable.

6. There is no need to pay owner collisions afresh at every chronological
   layer. Every repaired packet has identical old- and new-shore owner
   incidence vectors. Hence a genuinely source-compatible chronology
   preserves the complete owner load vector exactly. The multilevel gate
   is therefore a common-support word handoff, not \(\Theta(m)\)
   independent owner roundings.

## 1. The repaired one-/two-outside census

A simple packet is specified by

\[
 |C|=M-2,\qquad |S|=6,
\]

and a perfect matching \(J\) on \(S\). Its twelve tops are

\[
 C\cup e,\qquad e\in E:=\binom S2\setminus J.
\]

Fix either shore of the repaired packet. The squarefreeness proof in the
recharge theorem gives the exact local census. In an unrotated row, the
middle windows meeting an outside placeholder consist of one pure
context and \(H-1\) mixed contexts. In a rotated row there are \(H\)
mixed contexts. Thus every one of the twelve top paths has exactly
\(H\) owners which retain one outside label. Its other \(d-H\) owners
retain both outside labels.

Orient the two six-cycles as in the repaired construction. At an outside
label \(x\), the unrotated cycle contributes \(1+(H-1)=H\) occurrences
retaining \(x\), while the rotated cycle contributes \(H+0=H\).
Therefore every \(x\in S\) occurs in exactly \(2H\) one-outside owners.
Consequently the packet totals are

\[
 6(2H)=12H,
 \qquad
 12(d-H).
\tag{1.1}
\]

## 2. Exact marginal law under legal relabelling

Let

\[
 B_1=\binom{M-2}{m-1}=\binom{m+H-2}{H-1},
 \qquad
 B_2=\binom{M-2}{m-2}=\binom{m+H-2}{H}.
\tag{2.1}
\]

For a packet \(P=(C,S,E)\), define its two potential owner families

\[
 \begin{aligned}
 \mathcal A_1(P)
   &=\{A\cup\{x\}:A\in\tbinom C{m-1},\ x\in S\},\\
 \mathcal A_2(P)
   &=\{A\cup e:A\in\tbinom C{m-2},\ e\in E\}.
 \end{aligned}
\tag{2.2}
\]

They are disjoint because their members meet \(S\) in respectively one
and two labels. Uniformly permute the core roles of the repaired template
over the fixed set \(C\). Every fixed core role-subset of the required
size is then uniform among the corresponding subsets of \(C\). By the
census (1.1), the probability that the randomized packet contains a
fixed middle owner \(X\) is exactly

\[
 \boxed{
 p_P(X)=
 \frac{2H}{B_1}\,1_{\mathcal A_1(P)}(X)
 +\frac{d-H}{B_2}\,1_{\mathcal A_2(P)}(X).}
\tag{2.3}
\]

This formula uses only a simultaneous permutation of the core roles, so
it preserves the fixed physical twelve-top support. The squarefreeness
of a packet shore says that the event counted by \(p_P(X)\) is a
Bernoulli event, not an occurrence multiplicity.

The identities

\[
 |\mathcal A_1(P)|=6B_1,
 \qquad
 |\mathcal A_2(P)|=12B_2
\]

give

\[
 \sum_Xp_P(X)=12d
\tag{2.4}
\]

and

\[
 \boxed{
 \sum_Xp_P(X)^2
 =\sigma:=\frac{24H^2}{B_1}
             +\frac{12(d-H)^2}{B_2}.}
\tag{2.5}
\]

## 3. Exact conditional collision formulas

Let \(\mathcal P\) be any fixed matching of \(K\) twelve-top packets,
and randomize its packets independently as above. Write \(I_P(X)\) for
the indicator that packet \(P\) uses owner \(X\), and put

\[
 Z_X=\sum_{P\in\mathcal P}I_P(X),
 \qquad
 \Lambda_X=\sum_{P\in\mathcal P}p_P(X),
 \qquad
 R=12dK.
\tag{3.1}
\]

The cross-packet equal-owner pair mass is

\[
 \operatorname{Pair}=\sum_X\binom{Z_X}{2}.
\]

Independence between distinct packets gives the exact identity

\[
 \boxed{
 \mathbb E\operatorname{Pair}
 =\frac12\sum_X
    \left(\Lambda_X^2-\sum_{P\in\mathcal P}p_P(X)^2\right)
 =\frac12\left(\sum_X\Lambda_X^2-K\sigma\right).}
\tag{3.2}
\]

Equivalently, for two specified packets \(P,Q\), let

\[
 K_{ij}(P,Q)=|\mathcal A_i(P)\cap\mathcal A_j(Q)|.
\]

Then their expected collision-pair mass is exactly

\[
 \begin{aligned}
 \mathbb E\operatorname{Pair}(P,Q)
 ={}&\frac{4H^2}{B_1^2}K_{11}(P,Q)\\
 &+\frac{2H(d-H)}{B_1B_2}
       \bigl(K_{12}(P,Q)+K_{21}(P,Q)\bigr)\\
 &+\frac{(d-H)^2}{B_2^2}K_{22}(P,Q).
 \end{aligned}
\tag{3.3}
\]

This is the requested exact dependence on the fixed packet geometry.

It can be written without the shorthand \(K_{ij}\). Put

\[
 \mathcal E_1(P)=\binom{S_P}{1},\qquad
 \mathcal E_2(P)=\binom{S_P}{2}\setminus J_P,
\]

and similarly for \(Q\). If \(c=|C_P\cap C_Q|\), then

\[
 \boxed{
 K_{ij}(P,Q)=
 \sum_{T\in\mathcal E_i(P)}
 \sum_{U\in\mathcal E_j(Q)}
 \mathbf1_{\mathsf{comp}(T,U)}
 \binom{c}{m-|T\cup U|},}
\tag{3.3a}
\]

where

\[
 \mathsf{comp}(T,U):\quad
 T\cap S_Q=U\cap S_P,\qquad
 T\setminus U\subseteq C_Q,\qquad
 U\setminus T\subseteq C_P,
\tag{3.3b}
\]

and an out-of-range binomial coefficient is zero. Indeed an owner in
both potential families has the uniquely prescribed outside traces
\(T=X\cap S_P\) and \(U=X\cap S_Q\). Conditions (3.3b) are exactly the
consistency conditions on those traces; every remaining owner element
must then be chosen from \(C_P\cap C_Q\). Thus (3.3a) is an exact
closed coefficient formula for every fixed packet pair.

The collision excess is

\[
 \operatorname{Excess}
   =\sum_X(Z_X-1)_+.
\]

For a fixed \(X\), the variables \(I_P(X)\) are independent Bernoulli
variables. Therefore

\[
 \boxed{
 \mathbb E\operatorname{Excess}
 =\sum_X\left(
       \Lambda_X-1+\prod_{P\in\mathcal P}(1-p_P(X))
             \right).}
\tag{3.4}
\]

Pair mass and collision excess are different: (3.2) is quadratic,
whereas (3.4) retains every higher overlap.

### Fully symmetrized benchmark

If one additionally averages every packet over an independent full
ambient \(S_{2m}\)-orbit, then

\[
 p_P(X)=\frac{12d}{W}
\]

for every \(P,X\). This extra averaging does not preserve a fixed
physical top matching, so it is only an annealed benchmark. With

\[
 \rho=\frac{12dK}{W},
\]

it gives the exact formulas

\[
 \mathbb E\operatorname{Pair}
 =\binom K2\frac{(12d)^2}{W}
 =\frac{\rho^2W}{2}-6d\rho,
\tag{3.5}
\]

The three marked contributions to (3.5) are, respectively,

\[
 \begin{aligned}
 \mathbb E\operatorname{Pair}_{11}
   &=\binom K2\frac{(12H)^2}{W},\\
 \mathbb E\operatorname{Pair}_{12}
   &=\binom K2\frac{2(12H)\,12(d-H)}{W},\\
 \mathbb E\operatorname{Pair}_{22}
   &=\binom K2\frac{(12(d-H))^2}{W}.
 \end{aligned}
\tag{3.5a}
\]

Thus their proportions are

\[
 \frac{H^2}{d^2},\qquad
 \frac{2H(d-H)}{d^2},\qquad
 \frac{(d-H)^2}{d^2}.
\tag{3.5b}
\]

In particular the two-outside/two-outside term is
\((1-o(1))\) of the random pair mass.

and

\[
 \mathbb E\operatorname{Excess}
 =W\left[\rho-1+\left(1-\frac{12d}{W}\right)^K\right].
\tag{3.6}
\]

At \(\rho=1-o(1)\), these are respectively
\((1/2-o(1))W\) and \((e^{-1}-o(1))W\).
For \(L\) independently randomized preassigned layers, both expectations
sum over the layers: they are

\[
 \left(\frac12-o(1)\right)LW,
 \qquad
 \left(e^{-1}-o(1)\right)LW.
\tag{3.7}
\]

This is distinct from pooling the owner degrees and subsequently
recolouring the packet edges, which is the subject of Section 5.

## 4. Universal critical lower bounds for a fixed matching

Assume the matching leaves \(\ell=o(N)\) tops, so

\[
 12K=N-\ell,
 \qquad
 R=d(N-\ell),
 \qquad
 \rho=\frac RW.
\tag{4.1}
\]

By Cauchy--Schwarz and (3.2),

\[
 \mathbb E\operatorname{Pair}
 \ge \frac{R^2}{2W}-\frac{K\sigma}{2}.
\tag{4.2}
\]

In the calibrated regime, \(K\le W/(12\lambda)\), while (2.5) and
\(H=o(m)\) give \(\sigma=o(\lambda)\). Hence

\[
 K\sigma=o(W).
\tag{4.3}
\]

Here is the promised elementary estimate. The packet size hypothesis
gives \(3\le H<(M-2)/2\). Therefore

\[
 B_1\ge\binom{m}{2},\qquad B_2\ge\binom{m}{3}.
\]

It follows that

\[
 \frac{H^2}{B_1}=O\!\left(\frac{H^2}{m^2}\right)=o(1),
 \qquad
 \frac{(d-H)^2}{B_2}=O(m^{-1}).
\]

Thus in fact \(\sigma=o(1)\), which is stronger than the estimate used
in (4.3).

Also

\[
 \rho=\frac d\lambda\left(1-\frac\ell N\right)=1-o(1),
\tag{4.4}
\]

because \(d=M-4H+1\), \(\lambda=M+O(H)\), and \(H=o(m)\).
Equations (4.2)--(4.4) prove

\[
 \boxed{
 \mathbb E\operatorname{Pair}
 \ge(1/2-o(1))W.}
\tag{4.5}
\]

For the excess, put

\[
 u=\max_{P,X}p_P(X)=\frac{2H}{B_1}=o(1).
\tag{4.6}
\]

The equality in (4.6) follows from

\[
 \frac{2H/B_1}{(d-H)/B_2}
 =\frac{2(m-1)}{d-H}>1.
\]

For \(0\le p\le u\),

\[
 \log(1-p)\ge-\frac{p}{1-u}.
\]

Therefore

\[
 \prod_P(1-p_P(X))
 \ge \exp\left(-\frac{\Lambda_X}{1-u}\right).
\]

The function

\[
 x\longmapsto x-1+e^{-x/(1-u)}
\]

is convex. Applying Jensen to (3.4), and using
\(\sum_X\Lambda_X=R\), gives

\[
 \boxed{
 \mathbb E\operatorname{Excess}
 \ge W\left[\rho-1+\exp\left(-\frac\rho{1-u}\right)\right]
 =(e^{-1}-o(1))W.}
\tag{4.7}
\]

Thus the linear first-moment loss is intrinsic to independent
packetwise choices and does not come from an uneven fixed packet
matching.

The failure is overwhelmingly typical, rather than merely an expectation
calculation. Changing the decoration of one packet changes
\(\operatorname{Excess}=R-|\{X:Z_X>0\}|\) by at most \(2(12d)\).
McDiarmid's inequality therefore gives, for every fixed
\(\varepsilon>0\),

\[
 \Pr\!\left(
 \operatorname{Excess}<(e^{-1}-\varepsilon)W
 \right)
 \le
 \exp\!\left[-\Omega_\varepsilon(W/m)\right].
\tag{4.8}
\]

Indeed the number of packet variables is
\((1-o(1))N/12=\Theta(W/m)\), so the denominator in the bounded-
difference exponent is
\(\Theta((W/m)m^2)=\Theta(Wm)\), whereas the squared deviation is
\(\Theta_\varepsilon(W^2)\).

### Theorem 4.1 (exact carrier-respecting bulk Hall factor)

Fix any top-disjoint repaired-packet layer. For every covered top
\(U=C\cup e_U\), retain its designated two-label carrier edge \(e_U\).
There are pairwise distinct owners \(X_{U,j}\),
\(1\le j\le d-H\), such that

\[
                         e_U\subset X_{U,j}\subset U.
\tag{4.9}
\]

Consequently the entire bulk mass

\[
 (d-H)(N-o(N))=W-o(W)
\tag{4.10}
\]

has a collision-free assignment respecting the exact two-outside owner
type of the repaired packet. Only the \(HN=o(W)\) singleton-endpoint
occurrences remain outside this Hall factor.

#### Proof

Join a covered top \(U\) to the rank-\(m\) sets \(X\) satisfying
\(e_U\subset X\subset U\). Its degree is

\[
 A_2=\binom{M-2}{m-2}=\binom{M-2}{H}.
\]

Every owner has degree at most
\(B=\binom mH\), since this is the number of all rank-\(M\) tops which
contain it. Hence for every set \(\mathcal A\) of left vertices,

\[
 |\Gamma(\mathcal A)|\ge {A_2\over B}|\mathcal A|.
\]

Using
\(\lambda=W/N=\binom MH/\binom mH\ge M\),

\[
 {A_2\over B}
 =\lambda {m(m-1)\over M(M-1)}
 \ge {m(m-1)\over M-1}
 \ge m-4H+1=d-H.
\tag{4.11}
\]

For the last inequality, multiplication by \(M-1=m+H-1\) leaves the
positive difference

\[
 3mH+4H^2-m-5H+1.
\]

Clone each top \(d-H\) times and apply Hall's theorem. This proves
(4.9). Finally \((d-H)N=W-O(HN)=W-o(W)\) in the calibrated regime,
and deleting the top leave changes this by only \(o(W)\). \(\square\)

Theorem 4.1 is deliberately unbundled. It does not say that the
assigned complements \(U\setminus X_{U,j}\) occur as the
\(d-H\) core-only consecutive \(H\)-windows of one word, nor that the
twelve words share the repaired palettes and filler columns. This is
the exact remaining physical lift.

## 5. Pooled colour capacity across \(L\) layers

The same two-type census gives a favorable statement after the layers
are pooled.

Fix an owner \(X\). Let

\[
 T=\binom mH
\tag{5.1}
\]

be the number of rank-\(M\) tops containing \(X\). In one top-disjoint
packet layer, let \(a_X\) be the number of packets for which
\(X\in\mathcal A_1(P)\), and let \(b_X\) be the corresponding number
for \(\mathcal A_2(P)\).

If \(X\in\mathcal A_1(P)\), exactly four of the packet's twelve tops
contain \(X\), because \(\binom S2\setminus J\) is four-regular. If
\(X\in\mathcal A_2(P)\), exactly one packet top contains \(X\). The
layer is top-disjoint, so

\[
                         4a_X+b_X\le T.
\tag{5.2}
\]

The standing size assumption implies

\[
 d-H=m-4H+1\ge\frac{m-1}{2},
\]

and hence

\[
 \frac14\frac{2H}{B_1}
 \le\frac{d-H}{B_2}.
\tag{5.3}
\]

Using (2.3), (5.2), and (5.3), the expected load of any owner in one
layer is at most

\[
 \Lambda_X\le
 \alpha:=\frac{(d-H)T}{B_2}.
\tag{5.4}
\]

The binomial ratios have the exact identity

\[
 \frac{B_2}{T}
 =\lambda\frac{m(m-1)}{(m+H)(m+H-1)}.
\tag{5.5}
\]

Consequently

\[
 \boxed{
 \alpha=
 \frac{(d-H)(m+H)(m+H-1)}{m(m-1)\lambda}.}
\tag{5.6}
\]

Since \(\lambda\ge M=m+H\),

\[
 \alpha
 \le\frac{(m-4H+1)(m+H-1)}{m(m-1)},
\]

and therefore

\[
 \boxed{
 1-\alpha\ge
 \frac{3mH+4H^2-m-5H+1}{m(m-1)}
 =\left(3+o(1)\right)\frac Hm.}
\tag{5.7}
\]

Already for one fixed layer, the uniform legal core-relabel
distributions therefore constitute a fractional rainbow factor: every
packet part has total weight one, while every owner has load at most
\(\alpha<1\). Thus no fractional owner cut survives the repaired
twelve-row groupability constraints.

Now pool \(L=(1+o(1))m\) top-disjoint layers and independently
randomize every packet. Let \(D_X\) be the total number of selected
packet shores containing \(X\). It is a Poisson-binomial variable with
mean

\[
 \mu_X\le L\alpha=L-\Delta,
 \qquad
 \Delta\ge(3-o(1))H.
\tag{5.8}
\]

For any Poisson-binomial variable of mean \(\mu<L\), the exponential
moment bound, with \(\theta=\log(L/\mu)\), gives

\[
 \mathbb E(D-L)_+
 \le\frac{L}{L-\mu}
      \exp\left(-\frac{(L-\mu)^2}{2L}\right).
\tag{5.9}
\]

Indeed,

\[
 (D-L)_+\le\frac{e^{\theta(D-L)}}{e^\theta-1},
 \qquad
 \mathbb Ee^{\theta D}\le e^{\mu(e^\theta-1)},
\]

and \(x+\log(1-x)\le-x^2/2\).

At the calibrated height,

\[
 \log\lambda
 =\sum_{j=1}^H
   \log\frac{m+j}{m-j+1}
 =\frac{H^2}{m}
   +O\!\left(\frac{H^2}{m^2}+\frac{H^4}{m^3}\right).
\tag{5.10}
\]

To justify the range of this expansion without circularity, each
summand is at least \((2j-1)/(m+H)\). Hence

\[
 \frac{H^2}{m+H}\le\log\lambda=O(\log m),
\]

so \(H=O(\sqrt{m\log m})\). The error in (5.10) is consequently
\(o(1)\).

Since \(\lambda=M+O(H)=(1+o(1))m\), this yields

\[
 \frac{H^2}{m}=(1+o(1))\log m.
\tag{5.11}
\]

Equations (5.8)--(5.11) show, uniformly in \(X\),

\[
 \mathbb E(D_X-L)_+
 \le m^{-4+o(1)}=o(1).
\tag{5.12}
\]

Summing over the \(W\) owners proves

\[
 \boxed{
 \mathbb E\sum_X(D_X-L)_+
 \le Wm^{-4+o(1)}=o(W).}
\tag{5.13}
\]

Therefore some physical simultaneous relabelling has the property in
(5.13). Iteratively delete one packet incident with an overloaded owner.
Every deletion decreases the total overload by at least one and cannot
increase it elsewhere. After at most \(Wm^{-4+o(1)}\) deletions, every
owner has degree at most \(L\). Every top already has degree at most
\(L\). Since one deleted packet contains \(12d=O(m)\) owner
incidences, the total deleted owner mass is at most

\[
                         Wm^{-3+o(1)}=o(W).
\tag{5.14}
\]

This proves a near-spanning pooled top-and-owner degree-capacity theorem.
It does not assign layer colours.

## 6. The exact colouring gate and the elementary LLL wall

For every retained packet \(P\), form the resource edge

\[
 \mathcal R(P)=
 \{\text{its twelve tops}\}
 \ \dot\cup\ 
 \{\text{its }12d\text{ middle owners}\}.
\tag{6.1}
\]

After Section 5, this resource hypergraph has maximum degree at most
\(L\), after loss of only \(o(W)\) packet edges. An \(L\)-edge-colouring
of it would partition the packets into \(L\) layers, each top-disjoint
and owner-disjoint. More generally, an \(L\)-colouring with only
\(o(W)\) monochromatic owner excess is sufficient for the present owner
gate.

This conclusion does not follow from a generic maximum-degree theorem:
the resource rank is

\[
                         12+12d=\Theta(m).
\]

The atomic local-lemma wall can be stated without a homogeneous-model
approximation. For distinct packets \(P,Q\) and an owner \(X\), let

\[
 A_{P,Q,X}=\{X\in\mathcal O(P)\cap\mathcal O(Q)\}.
\]

Its probability is \(p_P(X)p_Q(X)\). All such events involving one
fixed packet \(P\) form a clique in the ordinary variable-dependency
graph. Put

\[
 S_P=\sum_{Q\ne P}\sum_Xp_P(X)p_Q(X).
\tag{6.2}
\]

Then

\[
 \sum_P S_P
 =2\mathbb E\operatorname{Pair}
 \ge(1-o(1))W.
\tag{6.3}
\]

There are \((1-o(1))N/12\) packets, so the average \(S_P\) is
\((12-o(1))W/N=\Theta(m)\). In particular one packet-star clique has
probability sum greater than one.

For completeness, any standard asymmetric-LLL witness
\(0\le x_A<1\) on a clique \(\mathcal C\) would imply

\[
 \sum_{A\in\mathcal C}\Pr(A)
 \le
 \sum_{A\in\mathcal C}
 x_A\prod_{B\in\mathcal C\setminus\{A\}}(1-x_B)
 \le1,
\tag{6.4}
\]

because the last sum is the probability that exactly one of independent
Bernoulli variables of parameters \(x_A\) succeeds. Equation (6.3)
contradicts this necessary clique inequality. Thus the canonical
atomic-event asymmetric LLL fails by a factor \(\Theta(m)\). This does
not rule out a new lopsided resampling oracle whose dependence relation
already encodes global owner exclusion.

There is an equivalent full-catalogue colour formulation. Let
\(D_T,D_X\) be the top and owner degrees in the complete orbit of
role-labelled repaired decorations, and let \(E\) be its number of
columns. Incidence counting gives

\[
 ND_T=12E,\qquad WD_X=12dE,\qquad
 {D_X\over D_T}={dN\over W}=1-o(1)<1.
\tag{6.5}
\]

Therefore a proper \((1+o(1))D_T\)-edge-colouring of this decorated
resource hypergraph would have almost all colour classes of size
\((1-o(1))N/12\), and each such class would be both top-disjoint and
owner-disjoint. Its resource rank is \(12+12d=\Theta(m)\), so the
fixed-uniformity edge-colouring theorem used for the undecorated
twelve-top catalogue does not prove this resolution.

The smallest missing statement is consequently:

> **Correlated repaired-packet colour-resolution lemma (unproved).**  
> For the randomizable twelve-top packet pool of Section 5, after
> deleting \(o(W)\) edges, choose the relabellings and an \(L\)-colouring
> so that every top and all but \(o(W)\) middle-owner incidences are
> colour-simple.

The capacity side of this lemma is proved by (5.13). The unresolved part
is integrality of the simultaneous top/owner colour resolution, followed
by the already-separate chronology compatibility.

There is an exact reason not to add the defects of genuinely applicable
chronological layers. If \(\mu_t\) is the complete middle-owner load
vector and \(\mathcal A_t\) is any collection of repaired moves whose
source shores occur in the current table, then

\[
 \mu_{t+1}-\mu_t
 =\sum_{P\in\mathcal A_t}
 \left(
 1_{\mathcal O(P,\mathrm{new})}
 -1_{\mathcal O(P,\mathrm{old})}
 \right)=0.
\tag{6.6}
\]

Thus one squarefree source-compatible owner factor stays squarefree
through all \(\Theta(m)\) layers. The independent-layer experiment
measures the cost of ignoring this handoff; it is not an unavoidable
chronological toll.

## 7. Exact boundary

Proved:

1. the exact one-/two-outside owner census of a repaired twelve-top
   shore;
2. the exact legal-relabel marginal (2.3);
3. exact conditional pair and excess identities (3.2)--(3.4);
4. a universal \((1/2-o(1))W\) expected pair mass and
   \((e^{-1}-o(1))W\) expected excess in every near-perfect layer;
5. the sharp distinction between this quenched fixed-support model and
   full ambient annealed symmetrization;
6. an \(o(W)\) pooled degree-overload theorem across
   \(L=(1+o(1))m\) layers;
7. the exact carrier-respecting bulk Hall factor;
8. the packet-star \(\Theta(m)\) asymmetric-LLL wall; and
9. exact owner-vector conservation along every genuinely applicable
   repaired chronology.

Not proved:

1. an \(L\)-edge-colouring of the pooled top-plus-owner packet resource
   hypergraph;
2. \(o(W)\) collision excess inside the original preassigned layers;
3. source-to-target chronology between the resulting layers; or
4. the constant-one theorem.
