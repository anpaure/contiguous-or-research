# Full-history collision excess: exact duality, dependent colouring, and the global blocker obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Outcome

Use the fixed good common cores and one fixed admissible nested tag
profile in every root. Put

\[
 W=\binom{2m}{m},\qquad N=N_H,\qquad M=m+H,\qquad
 s=m-H,\qquad L=m-3H+1,
\tag{0.1}
\]

and let

\[
 k=L+2\sum_{q=1}^{H-1}b_q=\Theta(m^{3/2})
\tag{0.2}
\]

be the number of protected physical targets in one literal all-depth
history. The protected target universe is denoted by \(\mathcal T\).
For one chosen history \(e_U\) in every root, write

\[
 \lambda_v=|\{U:v\in e_U\}|,
 \qquad
 K(e)=\sum_{v\in\mathcal T}(\lambda_v-1)_+.
\tag{0.3}
\]

Equivalently,

\[
 K(e)=\sum_{v:\lambda_v>0}(\lambda_v-1).
\tag{0.4}
\]

The unsigned sum over all \(v\), without the positive part or the
restriction \(\lambda_v>0\), is fixed by the occurrence census and is
not an optimization objective. The exact constant-one target is

\[
 K^*:=\min_e K(e)=o(W).
\tag{0.5}
\]

It is strictly weaker than a target-simple CCTPF matching.

This note does not prove (0.5). It proves the following exact reduction
and obstruction.

1. \(K^*\) is a pure minimax/purification gap. Its natural fractional
   collision LP and every additive target dual have value zero.
2. A root-Latin colouring of all history columns is an exact dependent
   rounding formulation. Total monochromatic excess \(o(DW)\), where
   \(D=s!\), proves (0.5). Independent root permutations instead have
   asymptotic collision \(D|\mathcal T|/e\).
3. At a global \(K\)-minimizer, put

   \[
   c_U=|\{v\in e_U:\lambda_v\ge2\}|.
   \tag{0.6}
   \]

   The other selected histories form an exact \(c_U\)-fold blocker of
   the complete literal fibre of \(U\). If \(p_*\) is the maximum
   single-port exposure, at least

   \[
   {c_U\over kp_*}
   \tag{0.7}
   \]

   distinct selected roots have positive physical blocking exposure
   toward \(U\).
4. Let \(\iota(V)\) be the total incoming blocker exposure of a selected
   history and put \(\iota_{\max}=\max_V\iota(V)\). Then

   \[
   \boxed{K^*\le N\iota_{\max}.}
   \tag{0.8a}
   \]

   Hence \(\iota_{\max}=o(m)\) proves \(K^*=o(W)\). If the directed
   blocker graph has maximum indegree \(\Delta_{\rm in}\), then

   \[
   \boxed{K^*\le N\,\Delta_{\rm in}\,k p_*.}
   \tag{0.8}
   \]

   In particular,

   \[
   \Delta_{\rm in}k p_*=o(m)
   \quad\Longrightarrow\quad K^*=o(W).
   \tag{0.9}
   \]

5. The proved full-history port estimate gives

   \[
   kp_*\le
   \exp\left\{-\left({\log2\over4}-o(1)\right)
                         \sqrt{m\log m}\right\}.
   \tag{0.10}
   \]

   Thus every polynomial, or more generally \(\exp(o(H))\), blocker
   indegree proves coefficient one through the collision ledger.
6. Conversely, \(K^*\ge\varepsilon W\) forces one selected literal
   history to have incoming blocker exposure \(\Omega(m)\), and to
   participate physically in blocking alternatives in at least

   \[
   \boxed{
   {\varepsilon m\over kp_*}
   =\exp(\Omega(H))}
   \tag{0.11}
   \]

   collided roots.

Finally, every disjoint union of inclusion-minimal closed odd-port
subsystems has total collision \(o(W)\). Thus repairability of
subcritical local odd ports is sufficient for the weaker objective
whenever those ports do not share exterior blockers. The surviving
physical obstruction is a globally shared, exponentially
high-indegree all-depth blocker.

## 1. Exact collision and hole ledger

Every history contains \(k\) distinct protected targets, so every
one-history-per-root selection has

\[
 \sum_{v\in\mathcal T}\lambda_v=kN
\tag{1.1}
\]

occurrences. Put

\[
 B=|\mathcal T|
   =W+2\sum_{q=1}^{H-1}N_q
\tag{1.2}
\]

and

\[
 \Delta=B-kN
 = (W-LN)+2\sum_{q=1}^{H-1}(N_q-b_qN)=o(W).
\tag{1.3}
\]

### Proposition 1.1 (collision equals additional holes)

For every selection \(e\), the number \(Z(e)\) of unrepresented
protected targets is

\[
 \boxed{Z(e)=\Delta+K(e).}
\tag{1.4}
\]

#### Proof

The number of represented targets is
\(|\{v:\lambda_v>0\}|\), and

\[
 kN=\sum_v\lambda_v
 =|\{v:\lambda_v>0\}|+K(e).
\tag{1.5}
\]

Subtract from \(B\) and use (1.3). \(\square\)

Thus \(K^*=o(W)\) is exactly the collision-excess target needed by the
append-the-holes compiler. Perfect matching is unnecessary.

## 2. The exact collision LP and its dual

Let \(\Omega_U\) be the \(D=s!\) literal tail histories in root \(U\),
with the fixed nested tag profile. Introduce

\[
 x_{U,e}\ge0\quad(e\in\Omega_U),\qquad
 z_v\ge0\quad(v\in\mathcal T).
\]

Consider

\[
 \min\sum_v z_v,
\tag{2.1}
\]

\[
 \sum_{e\in\Omega_U}x_{U,e}=1
 \qquad(U),
\tag{2.2}
\]

\[
 \sum_U\sum_{\substack{e\in\Omega_U\\v\in e}}x_{U,e}-z_v\le1
 \qquad(v\in\mathcal T).
\tag{2.3}
\]

For integral \(x\), the optimum is
\(z_v=(\lambda_v-1)_+\), so (2.1) is exactly \(K(e)\).

### Theorem 2.1 (additive collision dual)

The dual of (2.1)--(2.3) is

\[
 \max\left\{\sum_U\alpha_U-\sum_v y_v\right\},
\tag{2.4}
\]

subject to

\[
 0\le y_v\le1,
\tag{2.5}
\]

\[
 \alpha_U\le\sum_{v\in e}y_v
 \qquad(U,\ e\in\Omega_U).
\tag{2.6}
\]

Equivalently, its value is

\[
 \max_{0\le y\le1}
 \left[
 \sum_U\min_{e\in\Omega_U}\sum_{v\in e}y_v
 -\sum_v y_v
 \right].
\tag{2.7}
\]

For the fixed good cores this value is exactly zero.

#### Proof

Attach a nonnegative multiplier \(y_v\) to (2.3) and a free multiplier
\(\alpha_U\) to (2.2), written as
\(1-\sum_e x_{U,e}=0\). The Lagrangian coefficients of \(z_v\) and
\(x_{U,e}\) are

\[
 1-y_v,\qquad \sum_{v\in e}y_v-\alpha_U.
\]

Their infimum over nonnegative variables is finite exactly under
(2.5)--(2.6), and the remaining constant is (2.4).

The common-core fractional history distribution has every root mass one
and every target load at most one. Taking \(z=0\) gives primal value
zero. The objective is nonnegative, so primal and dual values are both
zero. \(\square\)

Since

\[
 (\lambda-1)_+=\max_{0\le y\le1}y(\lambda-1),
\tag{2.8}
\]

one also has the exact minimax identity

\[
 \boxed{
 K^*=\min_{e_U\in\Omega_U}\ 
       \max_{0\le y\le1}
 \left[
  \sum_U\sum_{v\in e_U}y_v-\sum_vy_v
 \right].}
\tag{2.9}
\]

Interchanging min and max gives zero by (2.7). Hence \(K^*\) is exactly
the pure-strategy minimax gap. A positive proof may be stated as an
approximate purification theorem with error \(o(W)\).

## 3. Exact dependent-colouring formulation

Give the \(D\) histories of every root the colours
\([D]=\{1,\ldots,D\}\), bijectively within that root. Call this a
root-Latin colouring \(\chi\). For colour \(a\), let \(e^a_U\) be the
unique history of root \(U\) with colour \(a\), and put

\[
 K_a(\chi)=\sum_v
 \left(|\{U:v\in e^a_U\}|-1\right)_+.
\tag{3.1}
\]

Define

\[
 \mathscr C(\chi)=\sum_{a=1}^D K_a(\chi).
\tag{3.2}
\]

### Theorem 3.1 (colouring equivalence)

\[
 \boxed{
 K^*=\min_{\chi}\min_{a\in[D]}K_a(\chi).}
\tag{3.3}
\]

Consequently,

\[
 \mathscr C(\chi)=o(DW)
 \quad\Longrightarrow\quad K^*=o(W).
\tag{3.4}
\]

#### Proof

Every colour class contains one history from every root, so
\(K_a(\chi)\ge K^*\). Conversely, give an optimal selection colour
\(1\), and extend independently to a bijection on every remaining root
fibre. Then \(K_1=K^*\). Averaging (3.2) proves (3.4). \(\square\)

For a target \(v\), put

\[
 a_{U,v}=|\{e\in\Omega_U:v\in e\}|,\qquad
 p_{U,v}={a_{U,v}\over D},\qquad
 \rho_v=\sum_U p_{U,v}\le1.
\tag{3.5}
\]

### Proposition 3.2 (exact independent-colouring loss)

If every root uses an independent uniform random bijection between its
histories and \([D]\), then the expected contribution of target \(v\)
to \(\mathscr C\) is

\[
 \boxed{
 a_v-D\left(1-\prod_U(1-p_{U,v})\right),}
\qquad a_v:=\sum_Ua_{U,v}=D\rho_v.
\tag{3.6}
\]

Moreover,

\[
 \mathbb E\mathscr C
   =\left(e^{-1}+o(1)\right)D B.
\tag{3.7}
\]

#### Proof

Within root \(U\), the \(a_{U,v}\) histories containing \(v\) receive a
uniform \(a_{U,v}\)-subset of the colours. A fixed colour is unused by
\(U\) with probability \(1-p_{U,v}\). Root bijections are independent,
so the probability that the colour is unused by every root is the
product in (3.6).

Across all colours, target \(v\) has \(a_v\) occurrences. Its collision
excess is occurrences minus occupied colours, proving (3.6).

The exact port count gives
\(\max_{U,v}p_{U,v}\le p_*=e^{-\Omega(H)}\). Therefore

\[
 \prod_U(1-p_{U,v})
 =\exp\{-\rho_v+O(p_*\rho_v)\}.
\tag{3.8}
\]

Also

\[
 \sum_v(1-\rho_v)=B-kN=\Delta=o(W)=o(B).
\tag{3.9}
\]

The function \(g(\rho)=\rho-1+e^{-\rho}\) is Lipschitz on
\([0,1]\), and \(g(1)=e^{-1}\). Sum (3.6), and use
(3.8)--(3.9) and \(p_*B=o(B)\), to obtain (3.7). \(\square\)

Thus useful rounding must correlate colours across root fibres so that
target-colour subsets nearly partition \([D]\). Rootwise dependence
alone leaves a Poisson collision floor on almost every target.

## 4. Exact one-switch blocker theorem

Fix a global minimizer \(e=(e_U)_U\) of \(K\). Put

\[
 S_{-U}=\bigcup_{V\ne U}e_V
\tag{4.1}
\]

and

\[
 c_U=|\{v\in e_U:\lambda_v\ge2\}|.
\tag{4.2}
\]

For a target family \(\mathcal A\), define its exact exposure to root
\(U\) by

\[
 \omega_U(\mathcal A)
 ={1\over D}\sum_{f\in\Omega_U}|f\cap\mathcal A|
 =\sum_{v\in\mathcal A}p_{U,v}.
\tag{4.3}
\]

### Theorem 4.1 (physical blocker identity)

For every root \(U\),

\[
 \boxed{
 c_U=\min_{f\in\Omega_U}|f\cap S_{-U}|.}
\tag{4.4}
\]

Consequently,

\[
 c_U\le\omega_U(S_{-U})
 \le\sum_{V\ne U}\omega_U(e_V).
\tag{4.5}
\]

#### Proof

Removing \(e_U\) decreases collision excess by exactly \(c_U\). Adding
\(f\) increases it by exactly \(|f\cap S_{-U}|\), because a target
creates one unit of excess precisely when its residual load is positive.
Thus

\[
 K(e-e_U+f)-K(e)=|f\cap S_{-U}|-c_U.
\tag{4.6}
\]

Minimality makes this nonnegative for every \(f\), while \(f=e_U\)
gives equality. This proves (4.4). Average over \(f\), then replace the
exposure of a union by the sum of exposures, to get (4.5).
\(\square\)

The identity uses the collision objective essentially. Perfect
target-disjointness would demand the stronger value \(c_U=0\) for every
root.

## 5. The directed global blocker graph

For the minimizing selection, form a directed graph \(\mathcal B(e)\)
on the roots by putting

\[
 U\longrightarrow V
 \quad\Longleftrightarrow\quad
 c_U>0\ \hbox{ and }\ \omega_U(e_V)>0.
\tag{5.1}
\]

Thus \(U\) is a collided root and some physical target used by the
selected all-depth history of \(V\) occurs in at least one literal
history of \(U\). Every history
has \(k\) targets and every target exposure is at most \(p_*\), so

\[
 \omega_U(e_V)\le kp_*.
\tag{5.2}
\]

Define the incoming blocker exposure

\[
 \iota(V)=\sum_{\substack{U:c_U>0\\U\ne V}}\omega_U(e_V),
 \qquad
 \iota_{\max}=\max_V\iota(V).
\tag{5.2a}
\]

### Theorem 5.1 (blocker degree theorem)

For every root \(U\),

\[
 d^+_{\mathcal B(e)}(U)
 \ge {c_U\over kp_*}.
\tag{5.3}
\]

Also

\[
 \sum_U c_U
 =\sum_{v:\lambda_v\ge2}\lambda_v
 =K(e)+|\{v:\lambda_v\ge2\}|,
\tag{5.4}
\]

and hence

\[
 K(e)\le\sum_Uc_U\le2K(e).
\tag{5.5}
\]

If \(\Delta_{\rm in}\) is the maximum indegree of
\(\mathcal B(e)\), then

\[
 \boxed{
 K(e)\le N\iota_{\max}
 \le N\,\Delta_{\rm in}\,kp_*.}
\tag{5.6}
\]

#### Proof

Equations (4.5) and (5.2) give
\(c_U\le d^+(U)kp_*\), proving (5.3). Summing \(c_U\) by target gives
(5.4). Every overloaded target contributes at least one to \(K\), so
their number is at most \(K\), proving (5.5). Summing (4.5) over the
collided roots gives

\[
 K(e)\le\sum_Uc_U
 \le\sum_V\iota(V)
 \le N\iota_{\max}.
\tag{5.6a}
\]

Also \(\iota_{\max}\le\Delta_{\rm in}kp_*\) by (5.2). This proves the
boxed inequalities. Equivalently, the unweighted calculation is

\[
 {K(e)\over kp_*}
 \le\sum_Ud^+(U)
 =\sum_Vd^-(V)
 \le N\Delta_{\rm in}.
\]

as asserted. \(\square\)

### Corollary 5.2 (sufficient congestion theorem)

If some global minimizer has either

\[
 \iota_{\max}=o(m),
\tag{5.7a}
\]

or the stronger checkable condition

\[
 \Delta_{\rm in}kp_*=o(m),
\tag{5.7}
\]

then

\[
 K^*=o(W).
\tag{5.8}
\]

In particular, \(\Delta_{\rm in}=\exp(o(H))\) is sufficient.

#### Proof

Use \(N=(1+o(1))W/m\), Theorem 5.1, and (0.10). \(\square\)

### Corollary 5.3 (obstruction forced by linear collision)

If \(K^*\ge\varepsilon W\) for fixed \(\varepsilon>0\), every global
minimizer contains a selected history \(e_V\) with

\[
 \iota(V)\ge{\varepsilon m\over1+o(1)}
\tag{5.8a}
\]

and

\[
 d^-_{\mathcal B(e)}(V)
 \ge {\varepsilon m\over(1+o(1))kp_*}
 =\exp(\Omega(H)).
\tag{5.9}
\]

Moreover, at least

\[
 {K^*\over k}
\tag{5.10}
\]

roots have \(c_U>0\).

#### Proof

Rearrange both inequalities in (5.6) and use
\(N=(1+o(1))W/m\). Since \(c_U\le k\),
(5.5) gives (5.10). \(\square\)

This is a physical all-depth obstruction, not an entropy count. Failure
of coefficient one forces one selected literal history whose actual
target ports participate in the blocking sets of exponentially many
other complete fibres.

## 6. Why isolated local odd ports are harmless for \(K\)

Call a root subsystem closed if its complete physical target support is
disjoint from the complete support of every root outside it. Closed
subsystems can be optimized independently. Call it inclusion-minimal
infeasible if it has no target-simple transversal but every proper root
subset does.

Let

\[
 R_*={1\over kp_*}.
\tag{6.1}
\]

The full-history forbidden-port theorem shows that every
inclusion-minimal infeasible subsystem has at least \(1+R_*\) roots.

### Theorem 6.1 (collision cost of isolated minimal ports)

Suppose the roots are a disjoint union of closed subsystems, each either
target-simple or inclusion-minimal infeasible. Then

\[
 \boxed{K^*\le {kN\over R_*}=k^2p_*N=o(W).}
\tag{6.2}
\]

#### Proof

A target-simple subsystem costs zero. In an inclusion-minimal infeasible
subsystem, remove one root. The others have a target-simple selection.
Reinsert the removed root with any literal history. It contains \(k\)
distinct targets and creates at most \(k\) units of collision excess.

Each bad subsystem has at least \(1+R_*\) roots, so there are at most
\(N/R_*\) of them. Closedness makes collision costs additive. Finally,

\[
 {k^2p_*N\over W}
 =(1+o(1)){k^2p_*\over m}=o(1)
\]

by (0.10) and the polynomial size of \(k\). \(\square\)

Thus bounded triangles, prisms, and every disjoint collection of
inclusion-minimal local odd meshes are harmless for the exact
coefficient-one objective. Exterior sharing, not local parity, is the
remaining danger.

## 7. The globally correlated gate

At a minimizer, every collided root is blocked by at least
\(1/(kp_*)=\exp(\Omega(H))\) selected exterior histories. If those
blocking families have subexponential overlap, Corollary 5.2 proves
\(K^*=o(W)\). A linear collision obstruction must instead reuse some
selected history as a blocker for exponentially many collided roots.

The existing common-core degree caps do not exclude this. At one target
row they permit as many as

\[
 {d_r\over b_{|r|}}={1\over p_r}
\tag{7.1}
\]

compatible roots, where \(p_r=b_{|r|}/d_r\) is that rank's exact port
exposure. For middle and shallow active ranks this may be
\(\exp(\Theta(H\log(m/H)))\), much larger than (5.9). A proof of
(0.5) therefore needs a genuinely multi-target fact: one selected
whole history cannot simultaneously realize enough rowwise compatible
incidences to have blocker indegree \(\Omega(m/(kp_*))\).

The fractional capacity rows give only the following bound:

\[
 \iota(V)
 \le\sum_U\omega_U(e_V)
 =\sum_{v\in e_V}\rho_v
 \le k=\Theta(m^{3/2}).
\tag{7.2}
\]

The blocker-congestion theorem needs \(o(m)\), so a positive proof must
save a factor \(\omega(\sqrt m)\) beyond separate target capacities.
This identifies exactly why the already proved rowwise caps do not close
the weaker collision objective.

Either of the following would close the lane.

1. **Dependent-colouring theorem.** Construct a root-Latin colouring
   with \(\mathscr C=o(DW)\).
2. **Blocker-congestion theorem.** Prove that some \(K\)-minimizer has
   \(\iota_{\max}=o(m)\); the stronger unweighted condition
   \(\Delta_{\rm in}kp_*=o(m)\) suffices.

The second is strictly tailored to collision excess and need not produce
a near-perfect CCTPF matching.

## 8. Final theorem-grade decision

### Theorem 8.1 (exact globally correlated collision obstruction)

For the physical all-depth common-core history catalogue:

1. the collision LP and every additive target dual have value zero;
2. \(K^*\) is the pure minimax gap (2.9);
3. a root-Latin colouring with average collision \(o(W)\) is an exact
   dependent-rounding certificate;
4. independent root-Latin rounding has Poisson-scale collision
   \((e^{-1}+o(1))D|\mathcal T|\);
5. every global minimizer obeys the physical blocker identity (4.4);
6. every collided root has at least \(c_U/(kp_*)\) distinct blocker
   histories;
7. every disjoint family of isolated minimal odd-port obstructions has
   total collision \(o(W)\); and
8. failure of \(K^*=o(W)\) forces one selected full history to have
   incoming blocker exposure \(\Omega(m)\) and blocker indegree at least
   \(\Omega(m/(kp_*))=\exp(\Omega(H))\).

Thus all subcritical local odd-port obstructions are harmless for the
weaker collision objective. The exact unresolved issue is global reuse
of one physical all-depth history as a blocker across exponentially many
root fibres. This is a concrete multi-target incidence problem, not an
entropy-only no-go and not the stronger perfect-matching gate.

## 9. Dependency ledger

This note uses:

- MATH_AUDIT_AND_THEOREM_COMMON_CORE_TIGHT_PATH_FUSION_20260726.md for
  the definition of \(K^*\), the hole identity, and fixed-core
  fractional feasibility;
- MATH_ATTACK_O_CCTPF_FULL_HISTORY_ODD_PORT_AND_REPAIR_20260726.md for
  the exact port exposure \(p_*\), forbidden-port repair, and (0.10);
- MATH_THEOREM_CCTPF_FULL_HISTORY_ODD_PORT_OBSTRUCTION_20260726.md for
  the physical all-depth odd-port prism and failure of total
  unimodularity.

No perfect-matching conclusion, entropy obstruction, or unproved
rounding theorem is used.
