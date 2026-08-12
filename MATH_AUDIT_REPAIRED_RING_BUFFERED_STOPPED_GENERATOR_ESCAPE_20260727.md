# Repaired promotion rings: the buffered stopped-generator audit

Date: 2026-07-27

Scope: constant-one owner packing only.

## 0. Verdict

The claimed buffered slow-bite theorem is not proved. The finite buffer

\[
 J=\Theta(\log m),\qquad L=\Theta((\log m)^2)
\]

does repair the formal defect that an order-\(J-1\) term can leave an
order-\(J\) hierarchy in one step. It does not control the top input strip
during a checkpoint of length \(\Theta(m)\).

For a protected path cluster \(C\), let \(A_C\) be its current size,
\(A_C(g)\) the number of its paths hit by an edge event \(g\), and
\(P_C(y)\) the number containing a vertex killed by a compensation coin
at \(y\). The exact square generator contains

\[
 \boxed{
 \mathsf D_2(C)
 =
 \nu_t\sum_g A_C(g)^2
 +\sum_y\chi_t(y)P_C(y)^2.}
\tag{0.1}
\]

The first term is the repeated-next-edge diagonal. The second is the
compensation-coin diagonal. At the moving top of a finite hierarchy,
(0.1) is unrecorded. The universal bounds

\[
 A_C(g)\le A_C,\qquad P_C(y)\le A_C
\]

permit

\[
 \mathsf D_2(C)=A_C\,\mathsf D_1(C),
\tag{0.2}
\]

where \(\mathsf D_1(C)\) is the first-moment loss. Then \(A_C^2\)
decays at only half its reference logarithmic rate. During a checkpoint
of length \(K/40=\Theta(m)\), its normalized value can grow by
\(\exp(\Theta(m))\). A \(J=\Theta(\log m)\) path buffer attenuates an
error by at best

\[
 \varepsilon^{J/2}
 =\exp[-\Theta((\log m)^2)],
\qquad \varepsilon=m^{-2+o(1)},
\tag{0.3}
\]

which does not absorb \(\exp(\Theta(m))\).

Thus the decreasing-order assertion
\(L_i\mapsto L_i-J\) is not a stopped induction: it assumes that the
unproved top strip remains valid throughout the checkpoint. The
unconditional conclusion in
MATH_THEOREM_REPAIRED_RING_GROWING_UNIFORMITY_SLOW_BITE_TRAJECTORY_20260726.md
is retracted.

The exact surviving gate is the mixed diagonal link-energy condition
MDLE in Section 6. Conditional on MDLE, the compensation, cumulative
drift, martingale, matching, and weighted-quarantine ledgers all close.

## 1. A compensated continuous process

This formulation puts compensation coins and the matching in one exact
generator.

Let \(\mathcal H_t\) be the active repaired-ring hypergraph. Every edge
contains one root and \(r\sim m\) owners. After suppressing quarantined
incidences, put

\[
 \Delta_t=\max_{v\in V(\mathcal H_t)}d_t(v),
 \qquad
 \nu_t={1\over r\Delta_t}.
\tag{1.1}
\]

Every active edge has an exponential clock of rate \(\nu_t\). When its
clock rings, put the edge in the matching and delete all its vertices.
Because clocks ring one at a time, selected edges form an integral
matching.

Independently, give every active vertex \(y\) a compensation clock of
rate

\[
 \chi_t(y)={\Delta_t-d_t(y)\over r\Delta_t}\ge0.
\tag{1.2}
\]

When it rings, delete \(y\) as waste. The total marginal deletion hazard
of every active vertex is exactly

\[
                 \nu_td_t(y)+\chi_t(y)={1\over r}.
\tag{1.3}
\]

Thus the common reference vertex density is

\[
                 x(t)=e^{-t/r}.
\tag{1.4}
\]

To reach \(z=m^{-1/20}\), run until

\[
                 T=r\log(1/z)={r\over20}\log m.
\tag{1.5}
\]

### Exact joint hazard

For a finite active vertex set \(S\), let

\[
 J_t(S)=
 \sum_{y\in S}d_t(y)
 -
 \left|\bigcup_{y\in S}\mathcal E_t(y)\right|.
\tag{1.6}
\]

The total rate of an event deleting at least one member of \(S\) is

\[
\begin{aligned}
 \Lambda_t(S)
 &=
 \nu_t\left|\bigcup_{y\in S}\mathcal E_t(y)\right|
 +\sum_{y\in S}\chi_t(y)\\
 &={|S|\over r}-\nu_tJ_t(S).
\end{aligned}
\tag{1.7}
\]

Equation (1.7) is the continuous compensation-coin analogue of the
exact compensated survivor law. Compensation removes every marginal
degree disparity. The only drift away from product thinning is the
edge-multiplicity excess \(J_t(S)\).

## 2. Protected clusters and diagonal multiplicities

Fix a live center \(X\) and a family of protected external edges and
vertices. Let \(\mathcal F_C\) be the active repaired paths satisfying
those conditions and put

\[
                 A_C=|\mathcal F_C|.
\tag{2.1}
\]

For an edge \(g\) disjoint from the protected resources, put

\[
 A_C(g)
 =
 |\{f\in\mathcal F_C:f\cap g\ne\varnothing\}|.
\tag{2.2}
\]

For a compensation vertex \(y\), put

\[
 P_C(y)
 =
 |\{f\in\mathcal F_C:y\in f\}|.
\tag{2.3}
\]

An edge can meet one path several times. The correct witness counts are

\[
 B_C^{(c)}(g)
 =
 \sum_{f\in\mathcal F_C}\binom{|f\cap g|}{c},
\tag{2.4}
\]

and exact binomial inversion gives

\[
                 A_C(g)=
 \sum_{c\ge1}(-1)^{c+1}B_C^{(c)}(g).
\tag{2.5}
\]

The power \(A_C(g)^\ell\) repeats the same next edge \(g\), rather than
using \(\ell\) disjoint next edges. Expanding (2.5) before taking this
power is the required diagonal-multiplicity bookkeeping. Replacing it by
a distinct-edge mesh is invalid.

## 3. The exact stopped generator

Stop a protected cluster when its center or any protected resource is
deleted. Such a terminal event only removes the cluster energy, so it
has a nonpositive contribution to every upper-bound calculation.

If an unprotected edge \(g\) rings, then

\[
                 A_C\longmapsto A_C-A_C(g).
\]

If a compensation clock at \(y\) rings, then

\[
                 A_C\longmapsto A_C-P_C(y).
\]

Define the diagonal loss moments

\[
\begin{aligned}
 \mathsf D_\ell^E(C)
 &=\nu_t\sum_g A_C(g)^\ell,\\
 \mathsf D_\ell^\circ(C)
 &=\sum_y\chi_t(y)P_C(y)^\ell,\\
 \mathsf D_\ell(C)
 &=\mathsf D_\ell^E(C)+\mathsf D_\ell^\circ(C).
\end{aligned}
\tag{3.1}
\]

For every integer \(h\ge1\), the stopped generator is exactly

\[
 \boxed{
 \mathcal L_t A_C^h
 =
 \sum_{\ell=1}^h
 (-1)^\ell\binom h\ell
 A_C^{h-\ell}\mathsf D_\ell(C)
 +\mathsf K_C,
 }
\tag{3.2}
\]

where \(\mathsf K_C\le0\) is the contribution from events killing a
protected resource.

In particular,

\[
 \mathcal L_tA_C=-\mathsf D_1(C)+\mathsf K_C
\tag{3.3}
\]

and

\[
 \boxed{
 \mathcal L_tA_C^2
 =-2A_C\mathsf D_1(C)+\mathsf D_2(C)+\mathsf K_C.}
\tag{3.4}
\]

Equations (3.1)--(3.4) include both requested diagonals: same-edge powers
through (2.5), and compensation-coin powers through \(P_C(y)^\ell\).

## 4. First-moment drift does close

For \(f\in\mathcal F_C\), let \(S_C(f)\) be its unprotected vertices.
Summing (1.7) over \(f\) gives

\[
 \mathsf D_1(C)
 =
 \sum_{f\in\mathcal F_C}
 \left(
 {|S_C(f)|\over r}
 -\nu_tJ_t(S_C(f))
 \right).
\tag{4.1}
\]

The repaired-path internal overlap estimate and its multiplicity
extension through witness order \(L\) give, while the corresponding
first-moment hierarchy is valid,

\[
 {1\over A_C}
 \sum_{f\in\mathcal F_C}J_t(S_C(f))
 \le {CL^2\Delta_t\over m}.
\tag{4.2}
\]

Using \(\nu_t=(r\Delta_t)^{-1}\), the relative drift error per unit time
is at most

\[
                 {CL^2\over rm}.
\tag{4.3}
\]

For \(L=O((\log m)^2)\) and the total time (1.5), its cumulative value is

\[
 T\,{CL^2\over rm}
 =O\left({L^2\log m\over m}\right)
 =O\left({\log^5m\over m}\right)=o(1).
\tag{4.4}
\]

Thus compensation coins cause no first-order bias: their rates make
(1.7) exact, and the only cumulative degree drift is the audited overlap
term (4.4).

## 5. Why the finite buffer fails

### 5.1 The top square

Suppose a cluster at the recorded top has reference first-moment loss

\[
                 \mathsf D_1(C)=\lambda_CA_C,
\qquad \lambda_C=\Theta(1).
\tag{5.1}
\]

Since every decrement is at most \(A_C\),

\[
                 \mathsf D_2(C)\le A_C\mathsf D_1(C).
\tag{5.2}
\]

Nothing in a hierarchy ending at \(C\) improves (5.2). Equality occurs
if every effective event deletes either none or all of \(\mathcal F_C\).
It can be realized by an unrecorded child cluster:

* all paths in \(\mathcal F_C\) meet the same unprotected edge event
  \(g\), so \(A_C(g)=A_C\); or
* all paths contain one unprotected compensation vertex \(y\), so
  \(P_C(y)=A_C\).

These are exactly the next-edge and coin extensions lying above the
recorded top.

Substituting (5.1)--(5.2) into (3.4) permits

\[
                 \mathcal L_tA_C^2=-\lambda_CA_C^2.
\tag{5.3}
\]

The square of the reference first moment decays at rate
\(-2\lambda_C\). Hence the normalized top square can grow at rate
\(\lambda_C=\Theta(1)\).

### 5.2 The checkpoint mismatch

The claimed checkpoint length was

\[
                 \tau={K\over40}=\Theta(m).
\tag{5.4}
\]

Equation (5.3) permits normalized top growth

\[
                 \exp(\Theta(\tau))=\exp(\Theta(m)).
\tag{5.5}
\]

The quadratic diagonal raises witness order by two. To transport a top
error through a buffer of width \(J=\Theta(\log m)\) requires at most
\(J/2\) such steps. Even granting the ideal static path cost
\(\varepsilon=m^{-2+o(1)}\) at every step, the attenuation is only

\[
                 \varepsilon^{J/2}
 =\exp[-\Theta((\log m)^2)].
\tag{5.6}
\]

Combining (5.5)--(5.6) leaves

\[
 \exp\{\Theta(m)-\Theta((\log m)^2)\}\longrightarrow\infty.
\tag{5.7}
\]

Therefore the assertion

\[
       \text{input order }L_i
       \quad\Longrightarrow\quad
       \text{output order }L_i-J
\]

does not follow merely by declining to assert the top strip. The
generator for the core uses that strip throughout the checkpoint, and
the strip has no stopped estimate.

### 5.3 Micro-checkpoints do not repair it

One could shorten a checkpoint until the crude top growth in (5.5) is
bounded. This requires \(\tau=O(1)\). Reaching time
\(T=\Theta(m\log m)\) would then require
\(\Theta(m\log m)\) checkpoints. Spending \(J=\Theta(\log m)\) witness
levels per checkpoint would require

\[
                 L=\Omega(m(\log m)^2),
\tag{5.8}
\]

far beyond the proved \(L=O((\log m)^2)\) path-mesh catalogue and beyond
the close-witness range used in its proof.

This rules out both advertised finite-buffer implementations.

## 6. The exact surviving mixed-diagonal gate

A sufficient condition is the following incidence-weighted statement.
Let \(\mathcal C_t\) be any monitored cluster class and \(w_C\) its
natural base-incidence weight.

### MDLE\((z,J)\)

Uniformly while \(x(t)\ge z\), outside cluster mass whose centered owner
incidence is \(o(E_t)\), for every \(2\le\ell\le h\le J\),

\[
                 \varepsilon_h={Ch^4\over m^2z^2},
\qquad
                 \varepsilon_*=\varepsilon_J.
\tag{6.1}
\]

\[
 \boxed{
 \sum_{C\in\mathcal C_t}w_C
 A_C^{h-\ell}\mathsf D_\ell(C)
 \le
 C
 \varepsilon_h^{\,\ell-1}
 \sum_{C\in\mathcal C_t}w_CA_C^h,
 }
\tag{6.2}
\]

The \(\ell=1\) term is supplied separately by the exact drift identity
(4.1). The edge part of (6.2) must be interpreted using the
multiplicity expansion (2.5). The coin part is the literal term
\(\sum_y\chi_t(y)P_C(y)^\ell\).

Condition (6.2), rather than a distinct-edge mesh, is exactly what the
generator (3.2) requires. A pointwise sufficient version is

\[
\begin{aligned}
 \nu_t\sum_gA_C(g)^\ell
 &\le CA_C^\ell\varepsilon_h^{\ell-1},\\
 \sum_y\chi_t(y)P_C(y)^\ell
 &\le CA_C^\ell\varepsilon_h^{\ell-1}.
\end{aligned}
\tag{6.3}
\]

The weighted version (6.2) is strictly weaker and is the natural target
for quarantine.

## 7. What closes conditional on MDLE

This section audits the remaining requested ledgers; none repairs the
failure in Section 5.

### 7.1 Stopped generator and martingale

Insert (6.2) into (3.2). For \(h\le J\), all nonlinear terms have total
absolute contribution at most

\[
 C
 \sum_{\ell=2}^h\binom h\ell
 \varepsilon_h^{\ell-1}
 \sum_Cw_CA_C^h
 =
 O\left(h^2\varepsilon_h\right)
 \sum_Cw_CA_C^h.
\tag{7.1}
\]

Since \(h=O(\log m)\) and \(\varepsilon_*=m^{-2+o(1)}z^{-2}\), this is
smaller than the first-moment drift. The predictable normalized
quadratic variation through time \(T\) is

\[
 O(T\varepsilon_*)
 =
 O\left({rJ^4\log m\over m^2z^2}\right)
 =
 O(m^{-9/10}\log^5m)
\tag{7.2}
\]

for \(z=m^{-1/20}\). This is the conservative normalization: the
first-moment loss rate of a whole path is \(\Theta(1)\), since it has
\(r\) vertices of hazard \(1/r\).

Taking \(h=c\log m\) in the stopped moment inequality gives bad-resource
probability

\[
                 \beta_m\le\exp[-c'(\log m)^2].
\tag{7.3}
\]

### 7.2 Cumulative degree drift

Equation (4.4) gives the complete deterministic bias from nonproduct
survival:

\[
                 O(\log^5m/m)=o(1).
\tag{7.4}
\]

The compensation clocks create no further bias because (1.3) is exact.
Their diagonal noise is already included in MDLE.

### 7.3 Weighted quarantine

Let \(E_t=|\mathcal E_t|\). The owner incidence is
\(I_t^O=rE_t\). Weighted Markov applied to (7.3) gives

\[
 \sum_{X\ {\rm bad}}d_t(X)
 \le\beta_m I_t^O
 =\beta_m rE_t=o(E_t).
\tag{7.5}
\]

Suppressing every edge incident with a bad owner therefore removes only
\(o(E_t)\) active edges, regardless of how many static root
neighborhoods those owners meet. The root calculation is normalized by
\(I_t^R=E_t\); a second weighted cleaning leaves only \(o(N)\) bad
roots.

### 7.4 Compensation waste

For nonexceptional roots, degree error \(o(1)\) makes the aggregate root
compensation rate \(O(\eta Nx(t)/r)\), with
\(\eta=m^{-1/10}\). Since

\[
                 \int_0^T{x(t)\over r}\,dt=1-z,
\]

this deletes \(O(\eta N)=o(N)\) roots as waste.

Owner degrees have the unavoidable ratio
\(\rho=1-O((H+\kappa)/m)\). Compensation therefore deletes at most

\[
 \int_0^T{(1-\rho)Wx(t)\over r}\,dt+o(W)
 =
 O\left((1-\rho)W\right)+o(W)=o(W)
\tag{7.6}
\]

owners. This is compatible with the exact packing defect
\(W-rN=o(W)\).

### 7.5 Integral matching ledger

Every edge-clock event enters the matching, and clocks are sequential.
At time \(T\), the unmatched roots consist of active roots, compensation
waste, and quarantined roots. Conditional on MDLE their total is

\[
                 (z+o(1))N=o(N).
\tag{7.7}
\]

Hence the integral matching \(Q\) satisfies

\[
\begin{aligned}
 W-r|Q|
 &\le W-rN+r(z+o(1))N\\
 &=O\left(\left({H+\kappa\over m}+z\right)W\right)
 =o(W).
\end{aligned}
\tag{7.8}
\]

No fractional rounding remains; only MDLE remains unproved.

## 8. Infinite factorial generating functions

The finite-buffer failure suggests summing all multiplicity orders.
Sections 8.1--8.2 below audit positive majorants which retain a \(+1\)
order shift.  They do **not** rule out the exactly compensated hierarchy,
whose positive Taylor remainder starts at \(+2\).  The corrected
calculation in
`MATH_AUDIT_WEIGHTED_RPRN_BUFFERED_DIAGONAL_GENERATOR_20260727.md`,
Proposition 8.1, shows that \(a=0\) and
\(\theta\asymp\sqrt{\mathcal T}\) absorb every compensated
\(+\ell\), \(\ell\ge2\), without a finite boundary.  What remains
unproved is the initial physical exponential-overlap estimate IEGF and
its hereditary form EMDLE.  Thus the infinite norm removes the formal
boundary but does not close from the available catalogue bounds.

### 8.0 Initial all-order audit

The multiplicity-aware close-witness estimate

\[
                 \left({Cs^4\over m^2}\right)^s
\]

was proved only for \(s=O((\log m)^2)=o(H)\). It cannot be
extrapolated to all \(s\le r\). The audited all-order codegree statement
is only

\[
 \left({D\over\Delta_{s+1}}\right)^{1/s}
 \ge c{m\over H},
\qquad
 {\Delta_{s+1}\over D}
 \le\left({CH\over m}\right)^s,
\tag{8.1}
\]

together with the exact consecutive spine in (8.11)--(8.14) below and
the terminal full-edge codegree one. Thus an infinite generating
function must control a genuine change of regime at \(s\asymp H\); the
local \(s^4/m^2\) coefficient is not an all-order input.

### 8.1 The shift has the wrong sign for inverse factorial weights

Let \(E_s\ge0\) denote any normalized witness-order-\(s\) energy. The
available path estimate has the schematic order-raising coefficient

\[
                 c_s\le {Cs^4\over m^2}
\tag{8.2}
\]

in the close-witness range, with the trivial cap \(c_s\le1\) afterwards.
Suppose the upper generator contains

\[
                 \dot E_s\le c_sE_{s+1}+\cdots.
\tag{8.3}
\]

For

\[
                 \Phi_a=\sum_{s\ge0}{E_s\over(s!)^a},
\tag{8.4}
\]

the raised term contributes

\[
\begin{aligned}
 \sum_{s\ge0}{c_sE_{s+1}\over(s!)^a}
 &=
 \sum_{t\ge1}
 c_{t-1}t^a\,{E_t\over(t!)^a}.
\end{aligned}
\tag{8.5}
\]

Thus the proposed inverse factorial weight multiplies, rather than
divides, the raising coefficient by \(t^a\). In the close-witness range
the effective coefficient is

\[
                 {Ct^{a+4}\over m^2},
\tag{8.6}
\]

and beyond that range the available capped majorant contributes the
shifted factor \(t^a\). Over \(T=\Theta(m\log m)\) time, (8.5) supplies
no uniform Gronwall bound from the known estimates.

Nor can one simply discard the large-\(t\) tail using its inverse
factorial weight. At the intermediate physical order
\(t\asymp H\), the concentrated diagonal in Section 5 permits normalized
square growth

\[
                 \exp(\Theta(T))
 =\exp(\Theta(m\log m)).
\tag{8.7}
\]

For every fixed \(a\),

\[
 {1\over(H!)^a}
 =
 \exp[-O_a(\sqrt m(\log m)^{3/2})],
\tag{8.8}
\]

which is far too weak to absorb (8.7). Thus the failure is not merely
the use of a supremum in (8.5).

Allowing \(a=a(m)\) does not reconcile the two effects. Absorbing
(8.7) at order \(H\) requires

\[
                 a\gtrsim {m\over H}
                 \asymp\sqrt{m/\log m}.
\]

But then the shift multiplier in (8.5) contains

\[
                 H^a
 =\exp[\Theta(\sqrt{m\log m})],
\]

so the generator majorant is even less summable.

### 8.2 The opposite weights conflict with the initial spine

To make a shift favorable one would instead try

\[
                 \Psi_a=\sum_{s\ge0}(s!)^aE_s.
\tag{8.9}
\]

Then the shifted coefficient is \(c_{t-1}t^{-a}\). Near

\[
                 t\asymp H\asymp\sqrt{m\log m},
\]

the available bound (8.2), capped at one, requires \(a>2\) to make

\[
                 T\sup_t c_{t-1}t^{-a}=o(1).
\tag{8.10}
\]

But the exact consecutive-path spine rules out such an initial norm.
Let \(\Gamma_s\) be the normalized number of repaired paths through a
fixed owner and \(s\) further consecutive owners. The exact catalogue
formulas give

\[
 \Gamma_s
 ={2(r-s)\over r}
 \left({(m-s)!\over m!}\right)^2
 \qquad(1\le s\le H),
 \tag{8.11}
\]

and

\[
 \Gamma_s
 ={2(r-s)(m-s)!(m-H)!\over r(m!)^2}
 \qquad(H\le s\le\min\{m,r-1\}).
 \tag{8.12}
\]

Put

\[
                 s_*=\min\{m,r-1\}=m-o(m).
\]

At this last universally available spine order,

\[
 \Gamma_{s_*}
 =
 {2(r-s_*)(m-s_*)!(m-H)!\over r(m!)^2}.
 \tag{8.13}
\]

Consequently

\[
\begin{aligned}
 \log\big((s_*!)^a\Gamma_{s_*}\big)
 &=(a-1+o(1))m\log m.
\end{aligned}
 \tag{8.14}
\]

For every \(a>1\), and hence for every \(a\) allowed by (8.10), the
single \(s=s_*\) spine term makes the initial weighted norm
exponentially large. The requirements

\[
                 a>2\quad\text{from propagation},
\qquad
                 a\le1\quad\text{from initialization}
 \tag{8.15}
\]

are incompatible.

This is an audit of the available \(s^4/m^2\) hierarchy. A sharper
large-\(s\) conditional theorem might change (8.10), but it would already
be a new form of MDLE.

### 8.3 Exact exponential sum of the diagonals

Factorial weights in the power \(h\), rather than the witness order,
do sum the repeated-event diagonal exactly. From (3.2),

\[
\boxed{
 \mathcal L_te^{\theta A_C}
 =
 e^{\theta A_C}
 \left[
 \nu_t\sum_g\big(e^{-\theta A_C(g)}-1\big)
 +
 \sum_y\chi_t(y)\big(e^{-\theta P_C(y)}-1\big)
 \right]
 +\mathsf K_C(\theta),
}
\tag{8.16}
\]

where \(\mathsf K_C(\theta)\le0\) for \(\theta\ge0\). Thus no diagonal
is lost in an infinite exponential generating function.

However, (8.16) exposes rather than removes the obstruction. After
subtracting the first-moment drift, the required remainder is

\[
\begin{aligned}
 \mathsf R_\theta(C)
 &=
 \nu_t\sum_g
 \left(e^{-\theta A_C(g)}-1+\theta A_C(g)\right)\\
 &\quad+
 \sum_y\chi_t(y)
 \left(e^{-\theta P_C(y)}-1+\theta P_C(y)\right).
\end{aligned}
\tag{8.17}
\]

If one effective event has \(A_C(g)=A_C\), or one compensation vertex
has \(P_C(y)=A_C\), then at the concentration scale
\(\theta A_C=\Theta(1)\), the corresponding term in (8.17) is a
positive constant times its event rate. It is not
\(O(\varepsilon_*)\).

The infinite-series condition needed to close (8.16) is precisely the
exponential MDLE bound

\[
 \mathsf R_{\vartheta/A_C}(C)
 \le C\vartheta^2\varepsilon_*
 \qquad(0\le\vartheta\le c\log m),
\tag{8.18}
\]

in incidence-weighted form. Expanding (8.18) in \(\vartheta\) recovers
all the mixed diagonal inequalities (6.2).

Therefore neither the uncompensated inverse-factorial majorant nor the
exact exponential power generating function closes the trajectory from
the current static catalogue.  The compensated geometric norm removes
the finite boundary, but its initialization and hereditary propagation
reduce to IEGF/EMDLE.

## 9. Final status

The following parts are proved:

1. the exact compensated process and joint hazard (1.7);
2. the stopped generator (3.2), including same-edge multiplicities and
   compensation-coin powers;
3. the stopped cumulative first-moment drift
   \(O(\log^5m/m)\) while the first-moment hierarchy is valid;
4. the finite-buffer escape (5.3)--(5.7);
5. the failure of all-order weights for the uncompensated \(+1\)
   majorant, including the exact spine calculation (8.11)--(8.15), and
   the boundary-free compensated \(+2\) correction cited above;
6. the exact repeated-edge/coin exponential generator (8.16);
7. weighted quarantine and compensation-waste ledgers conditional on
   MDLE; and
8. MDLE implies an integral matching missing \(o(N_H)\) roots.

What is not proved is MDLE itself. Therefore the owner-only near-factor
and the \(o(W)\) owner leave are not unconditional consequences of the
current path-mesh catalogue. The exact escaping term is (0.1), and the
unconditional slow-bite claim is retracted.
