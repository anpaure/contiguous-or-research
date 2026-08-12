# Lane C: endpoint-stable three-reflection iteration with the exact floor

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

This note closes the iteration and floor-accounting part of a prospective
common-base three-reflection chart theorem.  It proves the following exact
implication.

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  Suppose a class of literal exact factors containing
the K10 \(1/16\)-prepared factor is closed under three chart kernels based on
the fixed reflections \(s,r,t\) of the audited three-reflection frame.  At
every current factor whose floor energy exceeds

\[
 T_A=C_AHB\qquad(C_A>0\text{ fixed}),
 \tag{0.1}
\]

suppose each kernel preserves its reflection-invariant load part exactly and
contracts its anti-invariant part in conditional mean square by a common
factor \(\delta_m\le 1/2\).  Suppose also that every nontrivial kernel outcome
is reached by at most \(L\) nonempty proper freshly recomputed
complete-component cuts.

Then a deterministic sequence of at most

\[
 L\left\lceil 600n^6
   \log^+\!\left(\frac{nW}{C_A}\right)\right\rceil
 \tag{0.2}
\]

proper cuts reaches a factor \(F_{\rm stop}\) satisfying

\[
 \boxed{\mathcal Q_H(F_{\rm stop})\le 2C_AHB=o_A(W).}
 \tag{0.3}
\]

For a two-cut reflected chart one may take \(L=2\); (0.2) is then
\(O_A(n^7)\) cuts.  The integer floors introduce no accumulated error.

There is a second, more flexible version.  Exact preservation of a reflection
projection may be replaced by a **charged chart-frame inequality** for the
actual Haar signals and variances at every endpoint.  This is stated in
Theorem 4.1 and is the form that accommodates simultaneous even and odd chart
modes.

The state-independent harmonic frame is therefore sufficient for iteration
*after* endpoint-stable physical chart kernels have been constructed.  A
three-chart construction only at the initial common base is not sufficient:
common base does not imply endpoint closure.  Also, a state-independent
additive variance bound \(O_A(HB)\) per kernel, combined only with the audited
\(1/(100n^6)\) frame, stops at \(O_A(n^6HB)\), not at \(O_A(HB)\).  Thus the
needed quantitative statement is multiplicative chart contraction above
(0.1), or equivalently the charged inequality (4.2) below.

## 1. The exact floor is a factor-independent translate

For \(1\le q\le H\), write

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad 0\le\rho_q<N_q.
 \tag{1.1}
\]

For an exact factor \(F\), let \(\mu_q^F(S)\) be its load on the
\((m-q)\)-set \(S\).  Then

\[
 \sum_{|S|=m-q}\mu_q^F(S)=W.
 \tag{1.2}
\]

Use the unhalved weighted floor energy

\[
 \mathcal Q_H(F)=
 \sum_{q=1}^H\frac1{c_q}
 \sum_{|S|=m-q}
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1).
 \tag{1.3}
\]

Put

\[
 f_q^F=\mu_q^F-\frac W{N_q}{\bf1},\qquad
 \|f^F\|_H^2=\sum_{q=1}^H\frac{\|f_q^F\|_2^2}{c_q}.
 \tag{1.4}
\]

### Lemma 1.1 (exact floor translation)

For every exact factor,

\[
 \boxed{
 \mathcal Q_H(F)=\|f^F\|_H^2-\beta_H^{\rm fl},\qquad
 \beta_H^{\rm fl}=\sum_{q=1}^H
 \frac{\rho_q(N_q-\rho_q)}{c_qN_q}.}
 \tag{1.5}
\]

In particular \(\beta_H^{\rm fl}\) is independent of \(F\), and

\[
 0\le\beta_H^{\rm fl}\le\frac{HW}{4},
 \qquad 0\le \mathcal Q_H(F)\le HW^2.
 \tag{1.6}
\]

#### Proof

Fix \(q\), put \(a_q=W/N_q=c_q+\theta_q\), where
\(\theta_q=\rho_q/N_q\), and write \(x_S=\mu_q^F(S)-a_q\).
By (1.2), \(\sum_Sx_S=0\).  Therefore

\[
 \begin{aligned}
 \sum_S(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
 &=\sum_S(x_S+\theta_q)(x_S+\theta_q-1)\\
 &=\sum_Sx_S^2-N_q\theta_q(1-\theta_q).
 \end{aligned}
\]

Division by \(c_q\) and summation proves (1.5).  Each summand in
(1.3) is nonnegative, because \(\mu_q^F(S)-c_q\) is an integer; hence the
lower bound in (1.6).

Also \(\rho_q(N_q-\rho_q)/N_q\le N_q/4\), while
\(c_qN_q\le W\) and \(c_q\ge1\).  Thus each floor-baseline summand is at
most \(N_q/(4c_q)\le W/4\), proving the first upper bound in (1.6).

For the upper bound, direct expansion and (1.1) give

\[
 Q_q(F)=\frac1{c_q}
 \left(\sum_S\mu_q^F(S)^2-N_qc_q^2-(2c_q+1)\rho_q\right)
 \le\frac1{c_q}\sum_S\mu_q^F(S)^2\le W^2.
\]

Here \(c_q\ge1\), and the last inequality follows from nonnegativity and
(1.2).  Sum over \(q\). \(\square\)

The identity (1.5) is the reason no floor error accumulates under an
arbitrarily long sequence of cuts: every energy difference is exactly the
corresponding squared-norm difference.

## 2. Endpoint-stable reflection kernels

Let \(s,r,t\) be the three fixed-point involutions in Section 4 of
`MATH_AUDIT_C_REFLECTED_CHART_HAAR_AND_THREE_REFLECTION_FRAME_20260725.md`,
and put

\[
 P_a=\frac{I+a}{2}\qquad(a\in\{s,r,t\}).
\]

They act orthogonally on every subset layer and on the weighted direct sum
(1.4).  The audited frame theorem says that every stacked vector having
zero sum on each layer satisfies

\[
 \sum_{a\in\{s,r,t\}}\|(I-P_a)v\|_H^2
 \ge \alpha_n\|v\|_H^2,
 \qquad \alpha_n=\frac1{100n^6}.
 \tag{2.1}
\]

Let \(\Omega_m\) be a set of literal exact factors.  A family
\(\{K_a:a=s,r,t\}\) is called an endpoint-stable chart menu above \(T_A\)
if, for every \(F\in\Omega_m\) with \(\mathcal Q_H(F)>T_A\):

1. \(K_a(F)\) is a finite distribution on factors in \(\Omega_m\);
2. every outcome \(F'\ne F\) in its support has a certified path from \(F\)
   of at most \(L\) nonempty proper fresh complete-component cuts;
3. with \(v=f^F\) and \(v'=f^{F'}\), every outcome obeys
   \[
   P_av'=P_av;
   \tag{2.2}
   \]
4. conditionally on the current factor,
   \[
   \mathbb E_{K_a(F)}\|(I-P_a)v'\|_H^2
   \le\delta_m\|(I-P_a)v\|_H^2.
   \tag{2.3}
   \]

The quantifier \(F'\in\Omega_m\) in item 1 is the physical closure
condition.  It cannot be replaced by availability only at one initial base.

The same definition and every proof below allow the triple itself to depend
on \(F\), provided its three projections satisfy (2.1) with the same
\(\alpha_n\).  In particular, an arbitrary coordinate conjugate of the
audited triple has exactly the same frame constant.  Thus state-adaptive
renewal is fully compatible with the iteration; what must be uniform is the
frame and contraction estimate, not the literal coordinate names.

### Lemma 2.1 (one-round drift with exact floors)

Choose \(a\) uniformly from \(\{s,r,t\}\), then apply \(K_a(F)\).  If
\(F\in\Omega_m\) and \(\mathcal Q_H(F)>T_A\), then

\[
 \boxed{
 \mathbb E[\mathcal Q_H(F')\mid F]
 \le(1-\lambda_m)\mathcal Q_H(F),\qquad
 \lambda_m=\frac{1-\delta_m}{300n^6}.}
 \tag{2.4}
\]

#### Proof

For a fixed \(a\), (2.2), orthogonality, and (2.3) give

\[
 \mathbb E\|v'\|_H^2
 \le\|v\|_H^2-(1-\delta_m)\|(I-P_a)v\|_H^2.
\]

Average over \(a\), use (2.1), and then use (1.5):

\[
 \begin{aligned}
 \mathbb E\mathcal Q_H(F')
 &\le \mathcal Q_H(F)
 -\frac{1-\delta_m}{3}\alpha_n\|v\|_H^2\\
 &=\mathcal Q_H(F)-\lambda_m(\mathcal Q_H(F)+\beta_H^{\rm fl})\\
 &\le(1-\lambda_m)\mathcal Q_H(F).
 \end{aligned}
\]

Thus the floor constant helps rather than hurts the drift. \(\square\)

Notice that (2.4) is asserted only above \(T_A\).  There is therefore no
contradiction with the existence of floor-perfect factors of energy zero.

## 3. Deterministic descent and exact cut count

### Theorem 3.1 (proper-cut iteration)

Assume the endpoint-stable chart menu of Section 2, let
\(F_0\in\Omega_m\), and suppose \(0<\lambda_m\le1\).  There is a
deterministically selected sequence of literal factors, every transition
using at most \(L\) nonempty proper fresh cuts, which reaches

\[
 \mathcal Q_H(F_R)\le2T_A
 \tag{3.1}
\]

in at most

\[
 R=\left\lceil
 \lambda_m^{-1}\log^+\!\left(
 \frac{\mathcal Q_H(F_0)-T_A}{T_A}
 \right)\right\rceil
 \tag{3.2}
\]

rounds.  Here \(\log^+x=\max\{0,\log x\}\), with the displayed fraction
interpreted as zero when \(\mathcal Q_H(F_0)\le T_A\).

#### Proof

If the current energy is at most \(2T_A\), stop.  Otherwise Lemma 2.1
shows that some pair consisting of a reflection and a kernel outcome obeys

\[
 \mathcal Q_H(F_{j+1})
 \le(1-\lambda_m)\mathcal Q_H(F_j)
 \le T_A+(1-\lambda_m)
       (\mathcal Q_H(F_j)-T_A).
 \tag{3.3}
\]

It has strictly smaller energy, hence is not the identity outcome.  Item 2
of the endpoint-stable definition supplies its proper-cut path, and item 1
keeps the next factor in \(\Omega_m\).

As long as the process has not stopped, iteration of the second inequality
in (3.3) gives

\[
 \mathcal Q_H(F_j)-T_A
 \le(1-\lambda_m)^j(\mathcal Q_H(F_0)-T_A)
 \le e^{-\lambda_mj}(\mathcal Q_H(F_0)-T_A).
\]

At the value in (3.2) the right side is at most \(T_A\), so (3.1) holds.
There are at most \(L\) proper cuts per round. \(\square\)

The theorem asserts monotonicity at completed chart-block endpoints.  An
intermediate cut inside a two-cut block may increase \(\mathcal Q_H\); this
does not affect either freshness of the second overlay or the telescoping
bound.  Every individual physical operation is nevertheless nonempty and
proper.

The available single-state reflected block has the numerical ratio

\[
 \delta_m\le\frac{4096M_AH^5}{4^H}=o_A(1).
 \tag{3.4}
\]

Consequently, if the missing endpoint-stable construction retains this
already proved ratio at every high-energy endpoint, then for all sufficiently
large \(m\), \(\delta_m\le1/2\) and

\[
 \lambda_m\ge\frac1{600n^6}.
 \tag{3.5}
\]

By Lemma 1.1, \(\mathcal Q_H(F_0)\le HW^2\).  Since
\(T_A=C_AHB\) and \(B=W/n\),

\[
 \frac{HW^2}{T_A}=\frac{nW}{C_A}.
 \tag{3.6}
\]

Equations (3.2), (3.5), and (3.6) prove (0.2).  Since \(W\le2^n\), this
is \(O_A(Ln^7)\) proper cuts.  Finally

\[
 \frac{2T_A}{W}=\frac{2C_AH}{n}
 \le\frac{2C_A(A+1)\sqrt m}{2m+1}=O_A(m^{-1/2})=o_A(1),
 \tag{3.7}
\]

which proves (0.3).

## 4. Charged mode-frame form

The preceding theorem is deliberately stronger than necessary: an actual
common-base construction may combine a reflection-odd Haar block with a
reflection-even companion, so that no single projection is preserved.
Only the exact expected floor drift is needed.

At a current factor \(F\), let chart \(i\in\{1,2,3\}\) have a finite Haar
cube of literal endpoints, all remaining in \(\Omega_m\).  Suppose its exact
Haar identity is

\[
 \mathbb E_i\mathcal Q_H(F')
 =\mathcal Q_H(F)-\frac{A_i(F)-V_i(F)}4.
 \tag{4.1}
\]

Here \(A_i\) is the squared coherent signal and \(V_i\) the sum of the
individual bundle variances, with all \(1/c_q\) weights included.  Identity
(1.5) shows that (4.1) already has the exact integer floor.

### Theorem 4.1 (charged chart-frame iteration)

Suppose that for every \(F\in\Omega_m\) with \(\mathcal Q_H(F)>T_A\),
the three endpoint-stable Haar cubes satisfy

\[
 \boxed{
 \sum_{i=1}^3\bigl(A_i(F)-V_i(F)\bigr)
 \ge12\lambda_m\bigl(\mathcal Q_H(F)-T_A\bigr).}
 \tag{4.2}
\]

Then a deterministic sequence of at most

\[
 L\left\lceil\lambda_m^{-1}
 \log^+\!\left(\frac{HW^2}{T_A}\right)\right\rceil
 \tag{4.3}
\]

proper cuts reaches energy at most \(2T_A=o_A(W)\).

#### Proof

Choose a chart uniformly, then a fair Haar corner.  Averaging (4.1) and
using (4.2) gives

\[
 \mathbb E\mathcal Q_H(F')
 \le \mathcal Q_H(F)-\lambda_m
       (\mathcal Q_H(F)-T_A).
 \tag{4.4}
\]

Some nonidentity endpoint attains the right side whenever
\(\mathcal Q_H(F)>T_A\).  Endpoint stability allows repetition.  The proof
of Theorem 3.1, now using (4.4) directly, gives (4.3). \(\square\)

Equation (4.2) is the exact theorem-level target for the missing physical
construction.  It says that the three even/odd chart modes span all energy
above the admissible floor \(T_A\), after paying their actual variances.  No
separate additive-error bookkeeping is needed.

## 5. Why an additive \(O(HB)\) variance is quantitatively insufficient

This point is important for selecting the correct common-base statement.
Suppose only that each reflection kernel satisfies

\[
 P_av'=P_av,
 \qquad
 \mathbb E\|(I-P_a)v'\|_H^2
 \le\delta\|(I-P_a)v\|_H^2+R_AHB,
 \tag{5.1}
\]

where \(R_A\) is independent of \(m\).  The same calculation as in Lemma
2.1 gives merely

\[
 \mathbb E\mathcal Q_H(F')
 \le(1-\lambda_m)\mathcal Q_H(F)+R_AHB,
 \qquad
 \lambda_m=\frac{1-\delta}{300n^6}.
 \tag{5.2}
\]

The equilibrium scale certified by (5.2) is

\[
 \frac{R_AHB}{\lambda_m}
 =\frac{300R_A}{1-\delta}\,n^6HB,
 \tag{5.3}
\]

not \(O_A(HB)\).  Indeed \(n^6HB/W=n^5H\to\infty\), so (5.3) does not
even imply \(o(W)\).  To use the polynomial frame while retaining the
desired stopping scale, one needs either:

* multiplicative variance \(V_i\le\delta A_i\) throughout the high-energy
  region, as in Section 2; or
* aggregate additive variance at most \(O(\lambda_mHB)\); or
* the stronger charged mode coverage (4.2).

This is an exact scaling statement, not a heuristic loss.

## 6. State-independent frame versus physical endpoint closure

The fixed frame (2.1) itself survives every endpoint, deterministic or
random.  Conditional on any realized current factor \(F\), its centered load
has zero coordinate sum on every layer, so (2.1) applies without any
invariance assumption on the distribution of \(F\).  Thus the reflections
need not be changed during iteration.

What does not survive automatically is the factor geometry.  Conjugating one
reflected-chart construction changes its base factor; and performing a cut in
one chart can merge or split the fresh ownership components required by the
other charts.  Therefore a common-base theorem at \(F_0\) must certify at
least one of the following stronger properties:

1. **closed corner space:** every chart endpoint lies in one set \(\Omega_m\)
   on which all three fresh chart kernels and their estimates remain valid;
2. **commuting reservoirs:** cuts in any reservoir leave the complete
   components of the other two reservoirs intact; or
3. **adaptive renewal:** after every endpoint, new charts satisfying the same
   uniform estimates can be constructed from that endpoint.

Without one of these quantified statements, a common initial base permits
one averaging step but not Theorem 3.1.

There is a simple properness reserve in the K10 density.  Let \(x_m\) be the
number of selected K10 packets.  The laminar half-signing gives

\[
 x_m\le\frac{\operatorname{Cat}_{m-2}+1}{2},\qquad
 \frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}\longrightarrow\frac1{16}.
 \tag{6.1}
\]

One packet occupies exactly \(2n\) middle roots.  Hence even six disjoint
copies of this selected packet family occupy at most

\[
 12nx_m\le6n(\operatorname{Cat}_{m-2}+1)<n\operatorname{Cat}_m=W
 \tag{6.2}
\]

for all sufficiently large \(m\); the ratio of the middle expression to
\(W\) tends to \(3/8\).  Therefore a construction using at most the six root
families naturally arising from three reflected chart pairs has a nonempty
immutable root complement.  Whenever the selected root union for a physical
transposition is invariant, this complement is invariant as well and contains
an unselected fresh component.  Thus every nonempty chart cut is proper.

This reserve settles the numerical properness issue.  It does not settle
cross-chart persistence: that remains part of endpoint closure.

## 7. Exact boundary delivered to the common-base construction

To obtain \(\mathcal Q_H=o(W)\) from the K10 prepared factor, it is enough to
prove either of the following literal statements for all sufficiently large
\(m\):

1. an endpoint-stable three-reflection menu above \(C_AHB\) satisfying
   (2.2)--(2.3) with \(\delta_m\le1/2\); or
2. an endpoint-stable three-chart even/odd Haar menu satisfying the charged
   inequality (4.2) with \(\lambda_m^{-1}=m^{O(1)}\).

The first statement composes with the already audited fixed frame and gives
the explicit bound (0.2).  The second allows the common-base construction to
use its invariant companions and gives (4.3).  In either case, the exact
floor baseline is harmless, the deterministic selection uses only proper
cuts, and the stopping energy is \(O_A(H\operatorname{Cat}_m)=o(W)\).
