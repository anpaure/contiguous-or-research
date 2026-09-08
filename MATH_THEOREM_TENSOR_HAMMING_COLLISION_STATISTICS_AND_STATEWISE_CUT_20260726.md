# Tensor-associator/Hamming collision statistics and the statewise support cut

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Consider physical packets whose internal state may choose:

1. tensor-associator shores;
2. local \(Q_2\)-cell resolutions;
3. an affine/Hamming resolution class; and
4. a cyclic direction order.

Assume every realized global state has exact middle ownership.  There are
three rigorous conclusions.

**Independent packet randomization fails.**  Let
\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q=\frac W{N_q}.                                  \tag{0.1}
\]
If the packet choices are independent, a target \(T\) with packet hit
probabilities \(p_{P,T}\) has
\[
 \Pr(T\text{ is missed})=\prod_P(1-p_{P,T}).              \tag{0.2}
\]
For diffuse symmetric marginals,
\[
 \max_Pp_{P,T}=o(1),\qquad
 \sum_Pp_{P,T}^2=o(1),\qquad
 \sum_Pp_{P,T}=\lambda_q+o(1),                            \tag{0.3}
\]
and therefore
\[
 \Pr(T\text{ is missed})
   =e^{-\lambda_q+o(1)}.                                  \tag{0.4}
\]
At \(q=A\sqrt m+o(\sqrt m)\),
\[
 \lambda_q\longrightarrow e^{A^2},
\]
so independent randomization leaves
\[
                    (e^{-e^{A^2}}+o(1))N_q=\Theta_A(W)    \tag{0.5}
\]
expected holes.  Arbitrary dependence among the four choices *inside*
one packet does not change this conclusion; only independence between
different packets is used.

**The exact dependent second-moment gate is explicit.**  If \(Z_{P,q}(T)\)
is packet \(P\)'s target multiplicity and
\(\mu_q(T)=\sum_PZ_{P,q}(T)\), put
\[
 c_q=\lfloor\lambda_q\rfloor,\qquad
 \theta_q=\lambda_q-c_q.
\]
The balanced factorial excess satisfies
\[
\begin{aligned}
2\mathbb E\Delta_q
={}&\|\mathbb E\mu_q-\lambda_q\mathbf1\|_2^2\\
 &+\sum_P V_{P,q}
   +2\sum_{P<P'}C_{P,P',q}
   -N_q\theta_q(1-\theta_q),                            \tag{0.6}
\end{aligned}
\]
where
\[
 V_{P,q}=\mathbb E\|Z_{P,q}-\mathbb EZ_{P,q}\|_2^2,\qquad
 C_{P,P',q}
   =\mathbb E\langle Z_{P,q}-\mathbb EZ_{P,q},
                    Z_{P',q}-\mathbb EZ_{P',q}\rangle.   \tag{0.7}
\]
Since
\[
 |\{T:\mu_q(T)=0\}|\binom{c_q+1}{2}\le\Delta_q,          \tag{0.8}
\]
an expectation/second-moment proof of \(o(W)\) aggregate holes follows
if the right side of (0.6), summed over the required depths and both
signs, is \(o(W)\).  For diffuse packets
\(\sum_PV_{P,q}=\Theta(W)\).  Thus a successful dependent law must create
negative cross-packet covariance of order \(W\); ordinary independent
shore, phase, factor, or order choices give \(C_{P,P',q}=0\) and cannot
work.

**There is a statewise support obstruction inside one balanced tensor
sector.**  Take \(r\) eight-coordinate associator blocks and depth
\(2\le q=o(r)\).  Every associator shore and every local \(Q_2\)-cell
state preserves the macroprofile.  One cyclic order on the \(2r\)
directions exposes at most \(2r\) of the
\[
                              \binom rq                  \tag{0.9}
\]
profiles having occupancy three in \(q\) blocks and four in the others.
If \(K\) effective direction orders are used, then, statewise and under
arbitrary dependence,
\[
 \boxed{
 H^{\mathrm{sector}}_q
 \ge
 \left(\binom rq-2rK\right)_+
       \binom83^q\binom84^{r-q}.}                       \tag{0.10}
\]
For opposite-pair direction words, replace \(2rK\) by \(rK\).
Consequently \(K=o(\binom rq/r)\) misses \(1-o(1)\) of the literal
targets in that sector.  The \(2^r\) associator shore corners and all
affine Hamming phase choices do not enlarge the directional support.

Bound (0.10) is conditional on sectorwise supply.  Cross-sector
macroprofile transport has a balanced integral marginal flow, so no
statewise lower bound of this form is currently proved for the fully
mixed cross-sector reservoir.  There the exact remaining theorem is the
negative-covariance condition (0.6), together with physical bundled
completion.

## 1. Exact middle ownership and the true random variables

Let \(\mathcal P\) be a collection of packets.  Packet \(P\) has a finite
state space \(\Omega_P\).  Every \(\omega\in\Omega_P\) is a physical
collection of cube cycles and has a middle-owner incidence vector
\[
                         M_P^\omega\in\{0,1\}^{\binom{[2m]}m}.       \tag{1.1}
\]

The clean randomization regime fixes pairwise disjoint cells
\[
                         \mathcal M=\bigsqcup_{P\in\mathcal P}V_P \tag{1.2}
\]
and requires
\[
                         M_P^\omega=\mathbf1_{V_P}
                         \qquad(\omega\in\Omega_P).       \tag{1.3}
\]
Then every joint state choice has exact middle ownership automatically,
regardless of dependence.

This is not merely a convenient sufficient condition for independent
packets.

### Proposition 1.1 (independent ownership rigidity)

Suppose the packet states are independent and their nonnegative integral
middle incidences sum to one almost surely at every middle owner.  Then
each packet's incidence at every owner is deterministic.  Hence the
packets have fixed disjoint owner cells as in (1.2)--(1.3).

#### Proof

For a fixed middle owner \(X\), let \(Y_{P,X}\) be its multiplicity in
packet \(P\).  The independent nonnegative integer variables \(Y_{P,X}\)
sum to one almost surely.  Thus
\[
                0=\operatorname{Var}\sum_PY_{P,X}
                  =\sum_P\operatorname{Var}Y_{P,X}.
\]
Every \(Y_{P,X}\) is deterministic, and exactly one equals one.
\(\square\)

### Proposition 1.2 (the local \(Q_2\)-cells are not independent bits)

In the 24-owner pair-frame associator, the overlap graph between the six
old \(Q_2\)-cells and the six new \(Q_2\)-cells is connected.  Therefore
any exact middle cover made from cells on the two shores chooses all six
cells of one shore and none of the other.

#### Proof

Give every old cell \(L\) and new cell \(R\) a binary selection variable.
Every middle owner in \(L\cap R\) imposes
\[
                              x_L+x_R=1.                \tag{1.4}
\]
Connectedness forces one common value on all old variables and its
complement on all new variables. \(\square\)

Thus one local associator supplies one shore bit, not six independent
\(Q_2\)-cell bits.  Tensoring \(r\) disjoint blocks supplies the genuine
\(2^r\) shore corners, all with exact ownership.

## 2. Target loads and the balanced collision potential

Fix one depth \(q\) and one sign.  For a packet state \(\omega_P\), let
\[
 Z_{P,q}^{\omega_P}(T)\in\mathbb Z_{\ge0}              \tag{2.1}
\]
be the number of its literal consecutive windows with target \(T\).
Write
\[
 Z_{P,q}(T)=Z_{P,q}^{\omega_P}(T),\qquad
 \mu_q(T)=\sum_PZ_{P,q}(T).                             \tag{2.2}
\]
For a full middle-owner factor,
\[
                         \sum_T\mu_q(T)=W.              \tag{2.3}
\]

Put \(W=c_qN_q+\rho_q\), with
\[
 c_q=\lfloor W/N_q\rfloor,\qquad
 \theta_q=\rho_q/N_q.                                   \tag{2.4}
\]
Define
\[
 \Delta_q
  =\sum_T\frac{(\mu_q(T)-c_q)(\mu_q(T)-c_q-1)}2.         \tag{2.5}
\]
The exact centered identity is
\[
 2\Delta_q
   =\|\mu_q-\lambda_q\mathbf1\|_2^2
       -N_q\theta_q(1-\theta_q).                         \tag{2.6}
\]

Taking expectation and expanding the variance of
\(\sum_PZ_{P,q}\) gives (0.6)--(0.7).

### Lemma 2.1 (hole conversion)

For \(c_q\ge1\),
\[
                         H_q\binom{c_q+1}{2}\le\Delta_q,
 \qquad H_q=|\{T:\mu_q(T)=0\}|.                          \tag{2.7}
\]

#### Proof

For a hole, the summand in (2.5) is
\(c_q(c_q+1)/2\).  All summands are nonnegative on integral loads.
\(\square\)

Therefore a sufficient all-depth second-moment condition is
\[
 \sum_{q\le Q}\frac{\mathbb E\Delta_q^-+
                         \mathbb E\Delta_q^+}
                        {\binom{c_q+1}{2}}
                    =o(W).                               \tag{2.8}
\]
It implies that some joint outcome has \(o(W)\) aggregate missing lower
and upper targets.

## 3. Independent packet choices: exact miss expectation

Let
\[
                  I_{P,T}=\mathbf1_{\{Z_{P,q}(T)>0\}},
 \qquad p_{P,T}=\Pr(I_{P,T}=1).                          \tag{3.1}
\]
If packet choices are independent, then
\[
 \boxed{
 \mathbb EH_q
   =\sum_T\prod_P(1-p_{P,T}).}                           \tag{3.2}
\]

Suppose that on a target family \(\mathcal T_q\) of size
\(N_q-o(W)\),
\[
 \max_Pp_{P,T}=o(1),\qquad
 \sum_Pp_{P,T}^2=o(1),\qquad
 \mu_T:=\sum_Pp_{P,T}=O(1).                              \tag{3.3}
\]
Then
\[
 \log\prod_P(1-p_{P,T})
   =-\mu_T+O\left(\sum_Pp_{P,T}^2+
                  \max_Pp_{P,T}\sum_Pp_{P,T}^2\right),   \tag{3.4}
\]
and hence
\[
 \mathbb EH_q
   =\sum_{T\in\mathcal T_q}e^{-\mu_T+o(1)}+o(W).         \tag{3.5}
\]

For the complete affine-symmetric reservoir, \(\mu_T=\lambda_q+o(1)\).
At \(q=A\sqrt m+o(\sqrt m)\),
\[
 \log\lambda_q=A^2+o(1),                                \tag{3.6}
\]
which proves (0.5).

The fixed-pair Hamming selection is an exact special case.  For a target
of pair type \((f,q)\),
\[
 L_q(T)\sim\operatorname{Bin}\left(
             \binom{f+q}{q},
             \frac{2^q}{\binom{m-2f}{q}}\right),         \tag{3.7}
\]
so its miss probability is
\[
 \left(1-\frac{2^q}{\binom{m-2f}{q}}\right)^{
             \binom{f+q}{q}}.                            \tag{3.8}
\]
This remains of constant order at the central types.  The deterministic
fixed-frame capacity cut is stronger in under-capacity types.

## 4. Fine affine-phase and direction-order correlations

Inside one Hamming/linear-code fibre, let \(A_0\) be the allowed shore of
phase labels.  At a face-simple depth, a physical affine face \(F\) whose
direction set is cyclically available has an allowed-label set
\[
                              S_F\subseteq A_0,\qquad
 |S_F|=2^{q-1}.                                         \tag{4.1}
\]
Since \(|A_0|=\ell/2\), a uniform phase choice gives
\[
                         \Pr(F\text{ is hit}\mid
                                  D_F\text{ available})
                         =\frac{2^q}{\ell}.              \tag{4.2}
\]

For two faces \(F,G\) in the same fibre,
\[
 \boxed{
 \Pr(F,G\text{ both hit}\mid\sigma)
 =\mathbf1_{\{D_F,D_G\text{ are intervals of }\sigma\}}
      \frac{|S_F^\sigma\cap S_G^\sigma|}{|A_0|}.}        \tag{4.3}
\]
The intersection is either empty or an affine flat of power-of-two size.
It is generally not
\(|S_F||S_G|/|A_0|^2\).  Thus affine phase choices are correlated block
choices, not independent face coins.

Averaging also over a uniform cyclic direction order makes a fixed
\(q\)-set available with probability
\[
                              \frac{\ell}{\binom hq}      \tag{4.4}
\]
when the active set has size \(\ell=h\).  Combining (4.2) and (4.4)
gives the exact one-face marginal
\[
                              \frac{2^q}{\binom hq}.      \tag{4.5}
\]
For pair statistics one must average (4.3), not multiply (4.5).

Tensor-associator shore choices may change the labelled target inside an
available macroprofile, but they do not change which macroprofile is
available.  The local \(Q_2\) choice is already absorbed into the one
shore bit of Proposition 1.2.

## 5. What dependence must accomplish

For face-simple packets with deterministic target-set size \(s_{P,q}\)
and a uniform marginal on the target layer,
\[
 V_{P,q}
   =s_{P,q}-\frac{s_{P,q}^2}{N_q}.                     \tag{5.1}
\]
Hence a diffuse packet family, \(s_{P,q}=o(N_q)\), has
\[
                         \sum_PV_{P,q}=W-o(W).          \tag{5.2}
\]

If the mean histogram is balanced, (0.6) reduces to
\[
 2\mathbb E\Delta_q
 =W-o(W)
   +2\sum_{P<P'}C_{P,P',q}
   -N_q\theta_q(1-\theta_q).                            \tag{5.3}
\]
Therefore (2.8) requires
\[
 \boxed{
 2\sum_{P<P'}C_{P,P',q}
 =-W+N_q\theta_q(1-\theta_q)+o(W)}                     \tag{5.4}
\]
at each Gaussian-scale depth, up to the permitted weighted aggregation.

This is the precise negative-correlation demand.  Independent packets have
zero left side.  Pairwise-independent shore bits, phase labels, Hamming
factors, or direction orders also have zero left side across owner cells.
The required cancellation must be imposed by a global dependent
assignment, comparable to a target-balancing matching or design.

Equation (5.4) is not by itself impossible.  A random translate of a
deterministic balanced design has exactly the necessary dependence while
retaining symmetric one-packet marginals.  Consequently no universal
statewise no-go follows merely from exact middle ownership and symmetric
marginals.

## 6. The balanced tensor-sector support cut

Consider \(r\) disjoint eight-coordinate associator blocks
\[
                              B_1,\ldots,B_r.             \tag{6.1}
\]
In the balanced tensor sector every middle owner has four coordinates in
each \(B_i\).  A geodesic depth-\(q\) window which touches \(q\) distinct
blocks has lower macroprofile
\[
 \kappa^J_i=
 \begin{cases}
 3,&i\in J,\\
 4,&i\notin J,
 \end{cases}
 \qquad J\in\binom{[r]}q.                                \tag{6.2}
\]
There are
\[
                              M_{r,q}=\binom rq           \tag{6.3}
\]
such cells, each containing
\[
                              C_{r,q}=\binom83^q
                                          \binom84^{r-q} \tag{6.4}
\]
literal lower targets.

Every local associator shore preserves \(|T\cap B_i|\) pointwise.  An
affine Hamming phase changes which affine faces are hit but not the
direction sets of the fixed cyclic order.  Finally one order on \(2r\)
labelled directions has only \(2r\) cyclic starts and therefore exposes
at most \(2r\) sets \(J\).

### Theorem 6.1 (statewise order-support bound)

Suppose targets in the balanced sector (6.2) must be supplied from
balanced-sector packets using \(K\) effective cyclic direction orders.
Then every joint choice of associator shores, \(Q_2\)-cells, Hamming
factors, affine phases, and the \(K\) orders satisfies
\[
 H_q^{\mathrm{sector}}
 \ge(M_{r,q}-2rK)_+C_{r,q}.                             \tag{6.5}
\]
If the two directions of every \(B_i\) are opposite in each order, then
one order exposes only \(r\) cells and
\[
 H_q^{\mathrm{sector}}
 \ge(M_{r,q}-rK)_+C_{r,q}.                              \tag{6.6}
\]

#### Proof

The union of \(K\) directional supports has size at most \(2rK\), or
\(rK\) in the opposite-pair case.  Every unsupported cell \(J\) contains
the \(C_{r,q}\) distinct literal targets counted in (6.4), and none can be
hit by the permitted packets.  All other choices act inside the supported
cells and cannot alter this conclusion. \(\square\)

For \(2\le q=o(r)\), any
\[
                              K=o\left(\frac1r\binom rq\right)       \tag{6.7}
\]
therefore misses \(1-o(1)\) of these sector targets.

The hypothesis of Theorem 6.1 is essential.  In the full construction a
target macroprofile may be fed from many different source macroprofiles.
The quotient inclusion network has a perfectly balanced fractional flow
and an integral floor/ceiling marginal flow.  Thus (6.5) is a statewise
no-go for sectorwise tensor routing, not for a globally coupled
cross-sector assignment.

There is a second, independent statewise cut when no associator changes the
underlying unordered coordinate pairing.  If \(T_{f,q}\) is the number of
rank-\((m-q)\) targets with \(f\) full pairs and \(V_f\) the number of
middle starts of that preserved type, then
\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q},\qquad
 V_f
 =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f},                    \tag{6.8}
\]
and every realization obeys
\[
                         H_q\ge
                    \sum_f(T_{f,q}-V_f)_+.              \tag{6.9}
\]
At \(q=A\sqrt m+o(\sqrt m)\), the right side is a positive constant
multiple of \(W\).  Hamming factors, phases, and direction orders do not
alter (6.9).  The tensor associator escapes its hypothesis precisely
because one shore recouples coordinate pairs locally; after that escape,
the macroprofile cut (6.5), rather than the fixed-pair type cut, is the
remaining statewise statement.

## 7. Exact remaining gate

The four randomization layers now have a complete audit.

1. Local \(Q_2\)-cell choices collapse to one associator shore bit under
   exact ownership.
2. Tensor shore bits change fine target labels and pair types but preserve
   macroprofiles.
3. Affine Hamming phases have the exact block correlations (4.3).
4. Cyclic direction orders control directional support; polynomially few
   orders fail the sectorwise cut (6.5).
5. Independent packet choices leave Poisson-scale \(\Theta(W)\) holes.
6. A dependent expectation proof is possible only by verifying the
   covariance cancellation (5.4), or equivalently
   \[
    \sum_{q\le Q}
      \frac{\mathbb E\Delta_q^-+\mathbb E\Delta_q^+}
           {\binom{c_q+1}{2}}=o(W).                     \tag{7.1}
   \]

No such dependent physical selection is presently constructed.  Nor is
there a universal no-go for the full mixed cross-sector reservoir:
exact middle ownership permits globally dependent component choices, and
the macroprofile quotient has no Hall deficit.  The proved statewise
lower bounds are precisely the fixed-pair type cut and the sectorwise
order-support cut (6.5).
