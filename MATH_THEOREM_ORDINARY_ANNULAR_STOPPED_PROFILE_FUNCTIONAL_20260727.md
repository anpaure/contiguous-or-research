# Ordinary annular frames: the exact stopped-profile functional for one correlated leave

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 r=m-q_0,\qquad J=H-q_0,
\]

where

\[
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
 \qquad 0<a<b,
\]

and write

\[
 V_d=\binom{[n]}{r-d},\qquad N_d=|V_d|
 \qquad(0\le d\le J).
\]

This note uses only ordinary cyclic packets. There are no paired or
domino-twin columns.

For one entrance matching of ordinary packets, with common occurrence
mass \(G\) at every depth, the exact identity is

\[
 H_d=(N_d-G)_++\widetilde E_d,
 \qquad
 \widetilde E_d=\min\{G,N_d\}-|S_d|.
\tag{0.1}
\]

Thus the unique correlated-leave target is

\[
 \boxed{
 \mathfrak C=\sum_{d=0}^{J}\widetilde E_d=o(W).}
\tag{0.2}
\]

The main result is an exact reduction of (0.2) to a stopped residual
profile.

1. For any stopped process which selects legal **bites** of ordinary
   packets, let \(c_{d,j}\) be the increase of the scalar support capacity
   at bite \(j\), and let \(Z_{d,j}\) be the number of previously missing
   depth-\(d\) targets hit by the union of that bite. Pathwise,

   \[
   \boxed{
   \mathfrak C_\tau
    =\sum_{j<\tau}\sum_{d=0}^{J}(c_{d,j}-Z_{d,j}).}
   \tag{0.3}
   \]

   This is an equality; no rankwise leaves occur.

2. For a conditional bite law, let \(K_{d,j}(T)\) be the number of
   selected packets in the bite which contain \(T\), and put

   \[
   a_{d,j}(T)=\mathbb E[K_{d,j}(T)\mid\mathcal F_j],
   \qquad
   \chi_{d,j}(T)=
   \mathbb E[(K_{d,j}(T)-1)_+\mid\mathcal F_j].
   \]

   The exact conditional stopped-profile drift is

   \[
   \boxed{
   \mathscr P_j=
   \sum_dc_{d,j}
   -\sum_d\sum_{T\in\mathcal H_{d,j}}a_{d,j}(T)
   +\sum_d\sum_{T\in\mathcal H_{d,j}}\chi_{d,j}(T),}
   \tag{0.4}
   \]

   where \(\mathcal H_{d,j}\) is the current hole set. Moreover,

   \[
   \boxed{
   \mathbb E\mathfrak C_\tau
      =\mathbb E\sum_{j<\tau}\mathscr P_j.}
   \tag{0.5}
   \]

   Hence the weakest stochastic stopped-profile theorem is exactly

   \[
   \boxed{
   \mathbb E\sum_{j<\tau}\mathscr P_j=o(W).}
   \tag{SP}
   \]

   Under (SP), some realized ordinary entrance matching has
   \(\mathfrak C=o(W)\).

3. In a one-packet process the coalescence term \(\chi\) vanishes. If
   \(\mathcal L_j\) is a weighted catalogue of safe legal next packets,
   \(D_j\) is its total weight, and \(D_{d,j}(T)\) is the weight of its
   packets containing \(T\) at depth \(d\), then

   \[
   \boxed{
   \mathscr P_j
    =\sum_dc_{d,j}
      -\frac1{D_j}
       \sum_d\sum_{T\in\mathcal H_{d,j}}D_{d,j}(T).}
   \tag{0.6}
   \]

   Thus a concrete sufficient residual inequality is

   \[
   \boxed{
   \sum_d\sum_{T\in\mathcal H_{d,j}}D_{d,j}(T)
   \ge D_j\left(\sum_dc_{d,j}-\varepsilon_j\right),
   \qquad
   \mathbb E\sum_{j<\tau}\varepsilon_j=o(W).}
   \tag{SD}
   \]

4. The signed form of (0.6) is the sharp profile interpretation. At
   unsaturated depths, exposure to already covered targets is a debit;
   at saturated depths, exposure to holes is a credit. There is at most
   one boundary depth. The exact inequality is displayed in (5.8).

5. Ordinary entrance degree, codegree, and time-zero overlap estimates do
   not prove (SP) or (SD). A target-blind packet law has the wrong drift
   even at a floor-perfect state: at an unsaturated depth its expected
   one-step deficit is \(nG_j/N_d=\Theta(n)\). The required average total
   deficit is \(o(n)\) per selected packet. The missing theorem is
   therefore an explicitly state-dependent, hole-biased profile theorem,
   including the union/coalescence term for whole bites.

If the stopped process also has scalar leave
\(L=N_0-G_\tau=O(N_0/\sqrt m)\), then the common scalar bill is \(o(W)\).
Together with (SP), complement symmetry, and an
\(O(W/m)\)-path compiler, the deterministic annulus interface has total
cost \(o(W)\).

## 1. Ordinary cyclic histories and the terminal objective

For a directed cyclic order \(e=(z_i)_{i\in\mathbb Z_n}\), let

\[
 e_d=\{I_e(i,r-d):i\in\mathbb Z_n\}\subseteq V_d,
 \qquad
 I_e(i,k)=\{z_i,\ldots,z_{i+k-1}\}.
\tag{1.1}
\]

Every \(e_d\) has exactly \(n\) members. Let \(\mathcal M\) be an
entrance matching, meaning

\[
 e_0\cap f_0=\varnothing
 \qquad(e\ne f\in\mathcal M).
\tag{1.2}
\]

Write

\[
 s=|\mathcal M|,\qquad G=ns,
\]

and define the depth loads and supports by

\[
 \mu_d(T)=|\{e\in\mathcal M:T\in e_d\}|,
 \qquad
 S_d=\{T:\mu_d(T)>0\}.
\tag{1.3}
\]

Since every packet contributes \(n\) occurrences,

\[
 \sum_{T\in V_d}\mu_d(T)=G.
\tag{1.4}
\]

Therefore

\[
 \sum_T(\mu_d(T)-1)_+=G-|S_d|.
\tag{1.5}
\]

After subtracting the forced repeat floor,

\[
 \begin{aligned}
 \widetilde E_d
 &=G-|S_d|-(G-N_d)_+\\
 &=\min\{G,N_d\}-|S_d|.
 \end{aligned}
\tag{1.6}
\]

The actual hole count is \(H_d=N_d-|S_d|\), so (0.1) follows.
Complementing a lower cyclic interval gives an upper cyclic interval in
the same order. Thus the upper load vector is a relabelled copy of the
lower one, and it is enough to prove (0.2).

## 2. Stopped ordinary bites

Consider a filtration \((\mathcal F_j)\). At time \(j\), let
\(\mathcal M_j\) be the already selected ordinary entrance matching and
put

\[
 G_j=n|\mathcal M_j|,
 \qquad
 S_{d,j}=\bigcup_{e\in\mathcal M_j}e_d,
 \qquad
 \mathcal H_{d,j}=V_d\setminus S_{d,j}.
\tag{2.1}
\]

The next bite \(\mathcal B_j\) is a random finite family of ordinary
packets such that, conditionally on \(\mathcal F_j\),

\[
 \mathcal M_j\cup\mathcal B_j
\]

is again an entrance matching. Put \(b_j=|\mathcal B_j|\), allowing
\(b_j\) to be \(\mathcal F_j\)-measurable. The new occurrence mass is
\(G_j+nb_j\).

Define the exact scalar support-capacity increment

\[
 c_{d,j}
 =\min\{G_j+nb_j,N_d\}-\min\{G_j,N_d\},
\tag{2.2}
\]

and the fresh union score

\[
 Z_{d,j}
 =\left|
   \left(\bigcup_{e\in\mathcal B_j}e_d\right)
       \cap\mathcal H_{d,j}
  \right|.
\tag{2.3}
\]

Let

\[
 \mathfrak C_j
 =\sum_{d=0}^{J}
   \left(\min\{G_j,N_d\}-|S_{d,j}|\right).
\tag{2.4}
\]

### Theorem 2.1 (pathwise stopped-bite identity)

For every bite,

\[
 \boxed{
 \mathfrak C_{j+1}-\mathfrak C_j
   =\sum_{d=0}^{J}(c_{d,j}-Z_{d,j}).}
\tag{2.5}
\]

Consequently, for every bounded stopping time \(\tau\),

\[
 \boxed{
 \mathfrak C_\tau
 =\sum_{j<\tau}\sum_{d=0}^{J}(c_{d,j}-Z_{d,j}).}
\tag{2.6}
\]

#### Proof

At depth \(d\), adding the bite raises
\(\min\{G_j,N_d\}\) by (2.2). It raises the support size by exactly the
number (2.3) of old holes hit by the union of the bite. Their difference
is the change of the depth-\(d\) summand in (2.4). Sum over \(d\), then
telescope over \(j<\tau\). Initially \(G_0=0\), \(S_{d,0}=\varnothing\),
and \(\mathfrak C_0=0\). \(\square\)

The union in (2.3) is essential. Summing the fresh scores of the packets
in a bite would count a target repeatedly when two same-bite packets hit
it. That is precisely the error which a first-moment bite analysis must
control.

## 3. The exact conditional stopped profile

For \(T\in V_d\), define the bite multiplicity

\[
 K_{d,j}(T)=|\{e\in\mathcal B_j:T\in e_d\}|.
\tag{3.1}
\]

Conditionally on \(\mathcal F_j\), put

\[
 a_{d,j}(T)=\mathbb E[K_{d,j}(T)\mid\mathcal F_j],
\tag{3.2}
\]

\[
 \chi_{d,j}(T)
 =\mathbb E[(K_{d,j}(T)-1)_+\mid\mathcal F_j],
\tag{3.3}
\]

and

\[
 u_{d,j}(T)
 =\Pr(K_{d,j}(T)>0\mid\mathcal F_j).
\tag{3.4}
\]

For every nonnegative integer \(k\),

\[
 \mathbf1_{\{k>0\}}=k-(k-1)_+.
\]

Taking conditional expectations gives the exact relation

\[
 \boxed{u_{d,j}(T)=a_{d,j}(T)-\chi_{d,j}(T).}
\tag{3.5}
\]

Since a current hole is fresh precisely when the bite hits it at least
once,

\[
 \mathbb E[Z_{d,j}\mid\mathcal F_j]
 =\sum_{T\in\mathcal H_{d,j}}u_{d,j}(T).
\tag{3.6}
\]

Define the ordinary stopped-profile functional by

\[
 \begin{aligned}
 \mathscr P_j
 &:=\mathbb E[\mathfrak C_{j+1}-\mathfrak C_j
                  \mid\mathcal F_j]\\
 &=\sum_dc_{d,j}
   -\sum_d\sum_{T\in\mathcal H_{d,j}}a_{d,j}(T)
   +\sum_d\sum_{T\in\mathcal H_{d,j}}\chi_{d,j}(T).
 \end{aligned}
\tag{3.7}
\]

### Theorem 3.1 (stopped-profile martingale)

The process

\[
 M_k=\mathfrak C_{k\wedge\tau}
      -\sum_{j<k\wedge\tau}\mathscr P_j
\tag{3.8}
\]

is a martingale. In particular,

\[
 \boxed{
 \mathbb E\mathfrak C_\tau
 =\mathbb E\sum_{j<\tau}\mathscr P_j.}
\tag{3.9}
\]

#### Proof

Equation (3.7) says exactly that the conditional mean of the next
increment of \(M\) is zero. The stopping time is bounded by the number of
available entrance targets divided by \(n\), so all variables are
integrable. Take expectations at the terminal time. \(\square\)

### Corollary 3.2 (weakest stochastic correlated-leave theorem)

If a stopped ordinary-packet process satisfies

\[
 \mathbb E\sum_{j<\tau}\mathscr P_j=o(W),
\tag{3.10}
\]

then some realization of its terminal entrance matching satisfies

\[
 \mathfrak C_\tau=o(W).
\tag{3.11}
\]

Conversely, (3.10) is equivalent to
\(\mathbb E\mathfrak C_\tau=o(W)\) for that process law.

#### Proof

Equation (3.9) gives the equivalence. Since
\(\mathfrak C_\tau\ge0\), an expectation \(o(W)\) implies the existence
of a realization with value \(o(W)\). \(\square\)

A stronger but often easier sufficient condition is

\[
 \mathbb E\sum_{j<\tau}(\mathscr P_j)_+=o(W).
\tag{3.12}
\]

Unlike (3.10), condition (3.12) discards cancellation between early
positive drift and later negative drift. The exact weakest functional is
the signed expression (3.10).

## 4. The single-packet residual degree functional

Suppose every bite consists of one packet. Let \(\mathcal L_j\) be a
catalogue of legal next packets, each assigned a nonnegative
\(\mathcal F_j\)-measurable weight \(w_j(e)\). The catalogue may already
include every safety, extendibility, compiler, or protected-target
restriction required by the construction. Put

\[
 D_j=\sum_{e\in\mathcal L_j}w_j(e),
\tag{4.1}
\]

\[
 D_{d,j}(T)
 =\sum_{\substack{e\in\mathcal L_j\\T\in e_d}}w_j(e).
\tag{4.2}
\]

For the raw ordinary entrance process there is no ambiguity in this
catalogue. If

\[
 R_{0,j}=V_0\setminus S_{0,j},
\]

then

\[
 \mathcal L_j^{\rm ord}
 =\{e:e_0\subseteq R_{0,j}\}.
\tag{4.2a}
\]

Indeed, \(e_0\subseteq R_{0,j}\) says exactly that every entrance target
of \(e\) is disjoint from the already used entrance support. Taking
\(w_j\equiv1\) in (4.1)--(4.2) makes the functional below a literal
function of the stopped ordinary residual. Other weights represent an
explicit biased scheduler on the same legal catalogue.

Choose the next packet with probability \(w_j(e)/D_j\). Then

\[
 u_{d,j}(T)=a_{d,j}(T)=\frac{D_{d,j}(T)}{D_j},
 \qquad \chi_{d,j}(T)=0.
\tag{4.3}
\]

The scalar increment is

\[
 c_{d,j}
 =(N_d-G_j)_+-(N_d-G_j-n)_+.
\tag{4.4}
\]

Substitution in (3.7) proves the exact residual formula

\[
 \boxed{
 \mathscr P_j
 =\sum_{d=0}^{J}c_{d,j}
  -\frac1{D_j}
    \sum_{d=0}^{J}
    \sum_{T\in\mathcal H_{d,j}}D_{d,j}(T).}
\tag{4.5}
\]

Accordingly define

\[
 \operatorname{SPF}(\mathcal M_j,w_j)
 :=\sum_dc_{d,j}
  -\frac{
    \sum_d\sum_{T\in\mathcal H_{d,j}}D_{d,j}(T)}{D_j}.
\tag{4.5a}
\]

Equation (4.5) states
\(\operatorname{SPF}(\mathcal M_j,w_j)=\mathscr P_j\) exactly.

### Theorem 4.1 (weighted stopped-degree criterion)

Assume the weighted legal catalogue is nonempty until the desired stop
and, along the process,

\[
 \sum_d\sum_{T\in\mathcal H_{d,j}}D_{d,j}(T)
 \ge D_j\left(\sum_dc_{d,j}-\varepsilon_j\right)
\tag{4.6}
\]

for nonnegative \(\varepsilon_j\) satisfying

\[
 \mathbb E\sum_{j<\tau}\varepsilon_j=o(W).
\tag{4.7}
\]

Then some terminal ordinary entrance matching has
\(\mathfrak C=o(W)\).

#### Proof

Equations (4.5)--(4.6) give
\(\mathscr P_j\le\varepsilon_j\). Apply (3.9), (4.7), and the
nonnegativity of \(\mathfrak C\). \(\square\)

This is a target-labelled residual statement. It cannot be replaced by
the unlabelled assertion that most residual packet degrees are near their
mean: the sum in (4.6) is taken over the actual hole sets created by the
same earlier trajectory.

## 5. Exact collision-to-hole compensation

For one-packet steps, define the normalized exposure of the next-packet
law to the covered and uncovered parts of depth \(d\):

\[
 \alpha_{d,j}
 =\frac1{D_j}\sum_{T\in S_{d,j}}D_{d,j}(T),
 \qquad
 \beta_{d,j}
 =\frac1{D_j}\sum_{T\in\mathcal H_{d,j}}D_{d,j}(T).
\tag{5.1}
\]

Every candidate packet has \(n\) depth-\(d\) targets, so

\[
 \alpha_{d,j}+\beta_{d,j}=n.
\tag{5.2}
\]

Partition the depths into

\[
 \mathcal U_j=\{d:G_j+n\le N_d\},
\tag{5.3}
\]

\[
 \mathcal S_j=\{d:N_d\le G_j\},
\tag{5.4}
\]

and

\[
 \mathcal B_j=\{d:G_j<N_d<G_j+n\}.
\tag{5.5}
\]

Since \(N_d\) decreases strictly in \(d\), these are an initial interval,
at most one boundary depth for all sufficiently large \(m\), and a final
interval. Indeed,

\[
 N_d-N_{d+1}
 =N_d\frac{n-2(r-d)+1}{n-r+d+1}
 =\Theta_{a,b}(W/\sqrt m)\gg n
\tag{5.6}
\]

through the fixed Gaussian annulus.

For \(d\in\mathcal U_j\), \(c_{d,j}=n\), so the depth drift is
\(n-\beta_{d,j}=\alpha_{d,j}\). For
\(d\in\mathcal S_j\), \(c_{d,j}=0\), so it is
\(-\beta_{d,j}\). At the boundary it is

\[
 N_d-G_j-\beta_{d,j}
 =\alpha_{d,j}-(G_j+n-N_d).
\tag{5.7}
\]

Therefore

\[
 \boxed{
 \mathscr P_j
 =\sum_{d\in\mathcal U_j}\alpha_{d,j}
  +\sum_{d\in\mathcal B_j}
    \bigl(\alpha_{d,j}-(G_j+n-N_d)\bigr)
  -\sum_{d\in\mathcal S_j}\beta_{d,j}.}
\tag{5.8}
\]

Equivalently, after multiplying by \(D_j\), the concrete stopped-profile
cut is

\[
 \begin{aligned}
 &\sum_{d\in\mathcal U_j}\sum_{T\in S_{d,j}}D_{d,j}(T)\\
 &\quad+
 \sum_{d\in\mathcal B_j}
 \left[
   \sum_{T\in S_{d,j}}D_{d,j}(T)
   -D_j(G_j+n-N_d)
 \right]\\
 &\quad-
 \sum_{d\in\mathcal S_j}
   \sum_{T\in\mathcal H_{d,j}}D_{d,j}(T)
 \le \varepsilon_jD_j.
 \end{aligned}
\tag{5.9}
\]

Formula (5.9) is the precise multi-depth statement to prove for an
ordinary stopped process. It permits a packet to collide at a shallow,
unsaturated depth provided the same packet fills enough holes at deeper,
saturated depths. It is strictly weaker than demanding small repeat
excess, or a near-factor, at every depth separately.

## 6. Whole-bite coalescence is a separate profile term

For a general bite, define the expected fresh occurrence mass

\[
 A_j=\sum_d\sum_{T\in\mathcal H_{d,j}}a_{d,j}(T)
\tag{6.1}
\]

and its hole-restricted coalescence mass

\[
 X_j=\sum_d\sum_{T\in\mathcal H_{d,j}}\chi_{d,j}(T).
\tag{6.2}
\]

Then (3.7) is

\[
 \boxed{
 \mathscr P_j=\sum_dc_{d,j}-A_j+X_j.}
\tag{6.3}
\]

Thus the literal bite condition is

\[
 \boxed{
 A_j-X_j\ge\sum_dc_{d,j}-\varepsilon_j.}
\tag{6.4}
\]

The first moment \(A_j\) alone is insufficient. Two selected packets in
the same bite may both hit the same current hole, contributing two to
\(A_j\) but only one to fresh support. The exact correction is \(X_j\),
not a generic pair-codegree bound.

There is a useful sufficient estimate in terms of the second falling
moment. Since

\[
 (k-1)_+\le\binom{k}{2}
 \qquad(k\in\mathbb Z_{\ge0}),
\]

one has

\[
 X_j\le
 \sum_d\sum_{T\in\mathcal H_{d,j}}
 \mathbb E\left[\binom{K_{d,j}(T)}2\,\middle|\,\mathcal F_j\right].
\tag{6.5}
\]

Consequently a checkable, slightly stronger bite criterion is

\[
 \begin{aligned}
 &\sum_d\sum_{T\in\mathcal H_{d,j}}
   \mathbb E[K_{d,j}(T)\mid\mathcal F_j]\\
 &\quad-
 \sum_d\sum_{T\in\mathcal H_{d,j}}
   \mathbb E\left[\binom{K_{d,j}(T)}2\,\middle|\,\mathcal F_j\right]
 \ge\sum_dc_{d,j}-\varepsilon_j.
 \end{aligned}
\tag{6.6}
\]

Unlike a global packet-pair energy, (6.5)--(6.6) are restricted to the
current holes. This target restriction is indispensable: collisions on
already covered targets do not reduce the fresh union a second time.

## 7. Scale and the failure of target-blind ordinary profiles

At critical entrance mass,

\[
 G_\tau=N_0-O(N_0/\sqrt m),
 \qquad
 |\mathcal M_\tau|=\Theta(W/n).
\tag{7.1}
\]

Thus an error budget \(o(W)\) permits average stopped-profile drift only

\[
 o(W)/(W/n)=o(n)
\tag{7.2}
\]

per selected packet. When \(\Theta(\sqrt m)\) depths are unsaturated,
the raw support-capacity increment is \(\Theta(n\sqrt m)\), so the needed
relative aggregate accuracy is \(o(m^{-1/2})\).

The complete ordinary packet catalogue is target-regular. If a packet is
chosen uniformly without using the current state, then for every
\(T\in V_d\),

\[
 \Pr(T\in e_d)=\frac n{N_d}.
\tag{7.3}
\]

At a floor-perfect strictly unsaturated state, with
\(G_j+n\le N_d\),

\[
 |\mathcal H_{d,j}|=N_d-G_j,
 \qquad c_{d,j}=n.
\]

The expected fresh score and drift at that depth are therefore

\[
 \mathbb E Z_{d,j}
 =n\frac{N_d-G_j}{N_d},
\tag{7.4}
\]

\[
 \boxed{
 c_{d,j}-\mathbb E Z_{d,j}
 =\frac{nG_j}{N_d}.}
\tag{7.5}
\]

At a macroscopic stage \(G_j=\Theta(N_d)\), this is \(\Theta(n)\) at
one depth. Without a correlated credit from saturated depths, that one
debit already exceeds the allowed total average (7.2). Target regularity
alone supplies no such signed correlation.

The terminal target-blind calculation is also exact. For \(s\)
independent uniform ordinary packets, temporarily ignoring entrance
conflicts,

\[
 \mathbb E|S_d|
 =N_d\left[1-\left(1-\frac n{N_d}\right)^s\right].
\tag{7.6}
\]

If \(G=ns\) and \(G/N_d\to\lambda\in(0,\infty)\), then

\[
 \frac{\mathbb E\widetilde E_d}{N_d}
 \longrightarrow
 \begin{cases}
   e^{-\lambda}-1+\lambda,&0<\lambda\le1,\\
   e^{-\lambda},&\lambda\ge1.
 \end{cases}
\tag{7.7}
\]

Both quantities are positive for fixed \(\lambda>0\). Thus the
unconditioned target-blind law has linear excess at every macroscopic
annular depth. This is not a counterexample inside an entrance matching;
it identifies exactly what the state-dependent legal scheduler must
change.

Entrance legality changes the residual catalogue, but no sign follows
from that fact. The exact missing claim is that the **state-dependent**
legal degrees satisfy (5.9), or that a whole-bite law satisfies (6.4),
with cumulative expected error \(o(W)\). Static ordinary pair codegrees,
unweighted residual degrees, or separate estimates at each rank do not
contain this hole-labelled information.

## 8. Scalar leave and deterministic compiler implication

Let the terminal entrance leave be

\[
 L_\tau=N_0-G_\tau.
\]

The common scalar annular bill is

\[
 B(L_\tau)=\sum_{d=0}^{J}(N_d-G_\tau)_+.
\tag{8.1}
\]

Uniformly in the fixed Gaussian annulus,

\[
 B(L)=O_a\left(L+\frac{L^2\sqrt m}{N_0}\right).
\tag{8.2}
\]

Indeed,

\[
 \frac{N_d}{N_0}
 =\prod_{h=0}^{d-1}\frac{r-h}{n-r+h+1}
 =\exp\left(
   -\frac{2q_0d+d^2}{m}
   +O_a(m^{-1/2}+d/m)
   \right).
\tag{8.2a}
\]

Writing \(\delta=L/N_0\), the summand
\((N_d-N_0+L)_+\) can be positive for only
\(O_a(1+\delta\sqrt m)\) depths, and every such summand is at most
\(L\). This proves (8.2).

In particular,

\[
 L_\tau=O(N_0/\sqrt m)
 \quad\Longrightarrow\quad
 B(L_\tau)=o(W).
\tag{8.3}
\]

Combining (0.1) over all depths gives the exact lower-hole ledger

\[
 \sum_{d=0}^{J}H_d=B(L_\tau)+\mathfrak C_\tau.
\tag{8.4}
\]

The upper ledger is identical by complementation. Therefore a stopped
ordinary-packet law satisfying

\[
 \boxed{
 \mathbb E\left[
 B(L_\tau)+\sum_{j<\tau}\mathscr P_j
 \right]=o(W)}
\tag{8.5}
\]

has a realization with \(o(W)\) total annular holes on both shores.
If the selected ordinary cycles are cut once each, their number of paths
is

\[
 p=|\mathcal M_\tau|=O(W/m).
\]

The Gaussian-width reset toll is

\[
 2Hp=O(W/\sqrt m)=o(W).
\tag{8.6}
\]

Thus (8.5) supplies every deterministic annulus-to-compiler implication.
It uses one common entrance leave, one common ordinary history family,
and one signed stopped-profile sum. It never introduces independent
rank leaves.

## 9. Exact remaining theorem

The ordinary entrance-frame route is reduced to the following statement.

> **Ordinary stopped-profile theorem.** Construct a stopped matching
> process in the ordinary cyclic-packet catalogue such that
> \[
> L_\tau=O(N_0/\sqrt m)
> \]
> and either
> \[
> \mathbb E\sum_{j<\tau}\mathscr P_j=o(W)
> \]
> with \(\mathscr P_j\) given exactly by (3.7), or, in a one-packet
> implementation, prove the weighted hole-degree inequality (5.9) with
> cumulative expected error \(o(W)\).

For a whole-bite implementation the selected-incidence term and the
same-bite coalescence term must both be retained, as in (6.4). Proving
only entrance degree regeneration or an unconditioned factorial-overlap
hierarchy does not establish this theorem.

This is strictly weaker than near-perfect coverage independently at every
annular rank. It asks only that shallow collision debits and deep
hole-filling credits balance in one common stopped trajectory up to
\(o(W)\). By Theorem 3.1 it is also exact: no further probabilistic or
compiler loss remains after this functional is controlled.
