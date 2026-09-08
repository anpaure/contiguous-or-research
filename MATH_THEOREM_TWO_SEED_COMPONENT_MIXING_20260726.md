# Two-seed exact-factor component mixing

## Status

This note audits the proposal to overlay two genuinely unrelated exact
middle wreath factors and to choose one complete side of every ownership
component.  The switching operation is exact and integral.  The main
conclusion is that unrelated seeds remove the special equal-energy symmetry
of a relabeling overlay, but they do not by themselves give smoothing.

For fair component coins there are **two** gates:

1. the centered energy of the midpoint of the two seed load vectors;
2. the component variance.

For deterministic component choices, component variance is not the sharp
gate.  The sharp quantity is an affine vector-discrepancy problem for the
component effects.  This can be strictly smaller than fair variance, but no
uniform improvement is possible without additional geometry.

All statements below concern genuine exact wreath factors.  No fractional
factor or incomplete matching is used.

---

## 1. Notation and the weighted energy

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 \mathcal X_q=\binom{[n]}{m-q},\qquad
 N_q=|\mathcal X_q|.
\]

An exact middle wreath factor contains

\[
 t=\frac Wn
\]

wreaths.  At depth \(q\), let \(\mu_q^F\in\mathbb Z^{\mathcal X_q}\)
be the cyclic-interval load vector of an exact factor \(F\).  Every wreath
contributes \(n\) distinct intervals at that depth, so

\[
 \sum_{S\in\mathcal X_q}\mu_q^F(S)=W.
\]

Write

\[
 \lambda_q=\frac W{N_q},\qquad
 f_q^F=\mu_q^F-\lambda_q\mathbf1.
\]

Fix a depth window \(1\le q\le H\) and nonnegative weights \(w_q\).
The intended weights are \(w_q=1/c_q\), where
\(c_q=\lfloor\lambda_q\rfloor\).  Work in the Hilbert direct sum

\[
 \mathscr H_H=\bigoplus_{q=1}^H\mathbb R^{\mathcal X_q},\qquad
 \|z\|_H^2=\sum_{q=1}^Hw_q\|z_q\|_2^2.
\]

Define the centered energy

\[
 \mathcal E_H(F)=\|f^F\|_H^2.
\tag{1.1}
\]

If \(\lambda_q=c_q+\theta_q\), \(0\le\theta_q<1\), the unavoidable
integer floor at depth \(q\) is

\[
 b_q=N_q\theta_q(1-\theta_q).
\]

Thus

\[
 \mathcal Q_H(F)=\mathcal E_H(F)-B_H,
 \qquad B_H=\sum_{q=1}^Hw_qb_q,
\tag{1.2}
\]

is nonnegative.  The established scalar floor identity gives

\[
 2\sum_{q=1}^Hw_qO_q(F)\le \mathcal Q_H(F).
\tag{1.3}
\]

The constant \(B_H\) is factor-independent, so every energy-difference
identity below is valid verbatim for \(\mathcal Q_H\).

---

## 2. Overlaying two unrelated exact factors

Let \(F\) and \(G\) be arbitrary exact middle wreath factors.  Form their
bipartite ownership graph: the left vertices are the wreaths of \(F\), the
right vertices are the wreaths of \(G\), and every middle \(m\)-set joins
its unique owner in \(F\) to its unique owner in \(G\).

Every graph vertex has degree \(n\).  Hence, in every connected component
\(K\), the two sides contain the same number \(s_K\) of wreaths.  Moreover,
the two sides partition the same set of middle \(m\)-sets.  It follows that
choosing, independently in every component, either its complete \(F\)-side
or its complete \(G\)-side always gives another exact middle factor.

For each component and depth, let

\[
 u_{K,q}=\text{load contributed by the \(F\)-side of \(K\)},
\]

\[
 v_{K,q}=\text{load contributed by the \(G\)-side of \(K\)},
\qquad
 \delta_{K,q}=v_{K,q}-u_{K,q}.
\tag{2.1}
\]

Regard \(\delta_K=(\delta_{K,q})_{q\le H}\) as a vector in
\(\mathscr H_H\).  Then

\[
 \sum_K\delta_K=f^G-f^F.
\tag{2.2}
\]

Every \(\delta_{K,q}\) has zero total mass.  It also has zero point
margins: a cyclic order has exactly \(m-q\) depth-\(q\) intervals
containing each coordinate, and the two component sides have equally many
rows.  Thus component effects lie in Johnson degrees at least two, although
no relabeling relation between the two sides is assumed.

For signs \(\varepsilon_K\in\{-1,+1\}\), let \(F_\varepsilon\) choose the
\(G\)-side of \(K\) when \(\varepsilon_K=+1\) and its \(F\)-side when
\(\varepsilon_K=-1\).  Put

\[
 a=\frac{f^F+f^G}{2},\qquad
 D_\varepsilon=\sum_K\varepsilon_K\delta_K.
\tag{2.3}
\]

Then the exact centered load is

\[
 \boxed{
 f^{F_\varepsilon}=a+\frac12D_\varepsilon.}
\tag{2.4}
\]

---

## 3. Exact fair-coin identity

Define

\[
 A(F,G)=\|f^G-f^F\|_H^2,
\tag{3.1}
\]

\[
 V(F,G)=\sum_K\|\delta_K\|_H^2,
\tag{3.2}
\]

and the midpoint energy

\[
 M(F,G)=\left\|\frac{f^F+f^G}{2}\right\|_H^2.
\tag{3.3}
\]

### Theorem 3.1 -- two-seed heat identity

If the component signs are independent fair signs, then

\[
 \boxed{
 \mathbb E_\varepsilon\mathcal E_H(F_\varepsilon)
 =M(F,G)+\frac14V(F,G).}
\tag{3.4}
\]

Equivalently,

\[
 \boxed{
 \mathbb E_\varepsilon\mathcal E_H(F_\varepsilon)
 =\frac{\mathcal E_H(F)+\mathcal E_H(G)}2
  -\frac14\bigl(A(F,G)-V(F,G)\bigr).}
\tag{3.5}
\]

For the floor-corrected energy, the exact forms are

\[
 \mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
 =M(F,G)+\frac14V(F,G)-B_H,
\tag{3.6}
\]

and

\[
 \mathbb E_\varepsilon\mathcal Q_H(F_\varepsilon)
 =\frac{\mathcal Q_H(F)+\mathcal Q_H(G)}2
  -\frac14\bigl(A(F,G)-V(F,G)\bigr).
\tag{3.7}
\]

#### Proof

From (2.4), independence and zero sign means give

\[
 \mathbb E\left\|a+\frac12\sum_K\varepsilon_K\delta_K\right\|_H^2
 =\|a\|_H^2+\frac14\sum_K\|\delta_K\|_H^2,
\]

which is (3.4).  The parallelogram identity gives

\[
 \frac{\|f^F\|_H^2+\|f^G\|_H^2}{2}
 =\left\|\frac{f^F+f^G}{2}\right\|_H^2
  +\frac14\|f^G-f^F\|_H^2,
\]

proving (3.5).  Subtracting the same constant \(B_H\) from both sides
proves the floor-corrected version. \(\square\)

### Interpretation

For a relabeling overlay \(G=\sigma F\), the endpoint energies are equal
and group averaging can control the coherent term \(A\).  With unrelated
seeds there is no equal-energy or mean-zero identity.  Formula (3.4) shows
the two separate tasks:

* construct two seeds whose midpoint \((f^F+f^G)/2\) is already small;
* control the component variance \(V(F,G)\).

Thus component variance is the only *rounding* gate after a counterbalanced
pair has been supplied, but it is not the only gate in the two-seed theorem.

---

## 4. A concrete quadratic-component criterion

The preceding variance has a simple upper bound in terms of overlay
component sizes.

### Lemma 4.1 -- component second-moment bound

For every component \(K\) and every depth \(q\),

\[
 \boxed{
 \|\delta_{K,q}\|_2^2\le 2ns_K^2.}
\tag{4.1}
\]

Consequently,

\[
 \boxed{
 \sum_K\|\delta_{K,q}\|_2^2
 \le 2n\sum_Ks_K^2.}
\tag{4.2}
\]

#### Proof

At a fixed depth, one wreath contains any target at most once.  Hence each
coordinate of \(u_{K,q}\) and \(v_{K,q}\) lies between zero and \(s_K\),
so

\[
 \|\delta_{K,q}\|_\infty\le s_K.
\]

Each component side contributes exactly \(ns_K\) occurrences, whence

\[
 \|\delta_{K,q}\|_1
 \le \|u_{K,q}\|_1+\|v_{K,q}\|_1=2ns_K.
\]

The inequality \(\|z\|_2^2\le\|z\|_\infty\|z\|_1\) proves (4.1), and
summing proves (4.2). \(\square\)

Define the size-biased component parameter

\[
 \chi(F,G)=\frac nW\sum_Ks_K^2.
\tag{4.3}
\]

Since \(\sum_Ks_K=t=W/n\), one has \(\chi\le\max_Ks_K\).  Lemma 4.1
becomes

\[
 \sum_K\|\delta_{K,q}\|_2^2\le2\chi(F,G)W.
\tag{4.4}
\]

### Corollary 4.2 -- bounded-component, counterbiased seeds

Suppose

\[
 \chi(F,G)\le L
\tag{4.5}
\]

and, for every controlled depth,

\[
 \|f_q^F+f_q^G\|_2^2\le C W.
\tag{4.6}
\]

Then fair component switching satisfies

\[
 \mathbb E\|f_q^{F_\varepsilon}\|_2^2
 \le\left(\frac C4+\frac L2\right)W.
\tag{4.7}
\]

For one common sign vector through all depths,

\[
 \boxed{
 \mathbb E\mathcal E_H(F_\varepsilon)
 \le\left(\frac C4+\frac L2\right)
 W\sum_{q=1}^Hw_q.}
\tag{4.8}
\]

In particular, with \(w_q=1/c_q\le1\) and
\(H\le A\sqrt m\), some exact switched factor has aggregate centered
energy \(O_{A,C,L}(W\sqrt m)\).  If (4.6) and (4.5) hold uniformly at one
specified depth, some switch has depthwise energy \(O(W)\).

The same conclusion holds under the weaker direct hypothesis

\[
 \sum_{q\le H}w_q\|f_q^F+f_q^G\|_2^2=O(W\sqrt m),
 \qquad
 n\sum_Ks_K^2=O(W).
\tag{4.9}
\]

The component-size condition is sufficient, not necessary.  Large
components can still have small lower-rank effect vectors.

### Proposition 4.3 -- centered two-seed ensembles

Let \(\mathscr D\) be a probability distribution on exact factors such
that

\[
 \mathbb E_{F\sim\mathscr D} f^F=0
\tag{4.10}
\]

in \(\mathscr H_H\).  Draw \(F,G\) independently from \(\mathscr D\),
overlay them, and then use fair component signs.  If

\[
 \overline E=\mathbb E_{F\sim\mathscr D}\mathcal E_H(F),
 \qquad
 \overline V=\mathbb E_{F,G\sim\mathscr D}V(F,G),
\]

then the output is an exact-factor-valued distribution with centered mean
zero and

\[
 \boxed{
 \mathbb E\mathcal E_H(F_\varepsilon)
 =\frac12\overline E+\frac14\overline V.}
\tag{4.11}
\]

In particular, the ensemble contracts whenever

\[
 \overline V\le(2-\eta)\overline E+CT_m,
\tag{4.12}
\]

because then

\[
 \mathbb E\mathcal E_H(F_\varepsilon)
 \le\left(1-\frac\eta4\right)\overline E+\frac C4T_m.
\tag{4.13}
\]

#### Proof

Independence and (4.10) give

\[
 \mathbb E\left\|\frac{f^F+f^G}{2}\right\|_H^2
 =\frac12\overline E.
\]

Average (3.4).  The output mean is zero by averaging (2.4). \(\square\)

This is the cleanest ensemble version of the two-seed proposal.  It uses no
relation \(G=\sigma F\).  If the direct overlay is connected almost surely,
then \(V=A\), while independence and centering give
\(\mathbb E A=2\overline E\); equation (4.11) has no contraction.  Thus
fragmentation or genuine signed discrepancy is still necessary.

---

## 5. The exact deterministic discrepancy gate

Fair coins are only one way to select a vertex of the exact switching cube.
Equation (2.4) gives the exact optimum.

Define the affine component discrepancy

\[
 \operatorname{ADisc}_H(F,G)
 =\min_{\varepsilon\in\{\pm1\}^{\mathcal K}}
 \left\|f^F+f^G+\sum_K\varepsilon_K\delta_K\right\|_H^2.
\tag{5.1}
\]

### Theorem 5.1 -- exact affine-discrepancy formula

\[
 \boxed{
 \min_\varepsilon\mathcal E_H(F_\varepsilon)
 =\frac14\operatorname{ADisc}_H(F,G).}
\tag{5.2}
\]

Thus affine discrepancy, rather than fair component variance, is the sharp
deterministic gate.

There is also a useful symmetric discrepancy

\[
 \beta_H(F,G)=\min_\varepsilon
 \left\|\sum_K\varepsilon_K\delta_K\right\|_H^2.
\tag{5.3}
\]

It satisfies

\[
 \boxed{
 \beta_H(F,G)\le\min\{A(F,G),V(F,G)\}.}
\tag{5.4}
\]

Moreover, some exact child obeys

\[
 \boxed{
 \mathcal E_H(F_\varepsilon)
 \le M(F,G)+\frac14\beta_H(F,G).}
\tag{5.5}
\]

#### Proof

Formula (5.2) is (2.4) multiplied by four.  The all-plus signing in (5.3)
has signed sum \(f^G-f^F\), proving \(\beta_H\le A\).  Averaging over fair
signs gives expected squared signed sum \(V\), proving \(\beta_H\le V\).

Choose a signing attaining \(\beta_H\).  The two antipodal children have
centered vectors \(a+D_\varepsilon/2\) and
\(a-D_\varepsilon/2\).  Their average energy is

\[
 \|a\|_H^2+\frac14\|D_\varepsilon\|_H^2.
\]

The better antipode proves (5.5). \(\square\)

Hence deterministic discrepancy can beat fair coins whenever
\(\beta_H\ll V\).  It can also fail to improve them: if the component
effect vectors are mutually orthogonal, every signing has squared norm
\(V\), so \(\beta_H=V\).  In the extreme genuine case of a connected
overlay, there is one component and the switching cube contains only the
two original factors; no new factor can be produced.

Conditional expectation derandomizes (3.4), yielding a deterministic child
no worse than the fair expectation, but conditional expectation alone gives
no strict improvement over \(V\).  A strict improvement requires a theorem
about the component Gram matrix or the affine target in (5.1).

---

## 6. Biased independent component choices

There is an intermediate criterion between fair coins and solving the exact
discrepancy problem.  Choose independent signs with

\[
 \mathbb E\varepsilon_K=t_K,\qquad -1\le t_K\le1.
\]

### Proposition 6.1 -- biased rounding identity

\[
 \boxed{
 \begin{aligned}
 \mathbb E\mathcal E_H(F_\varepsilon)
 ={}&\frac14\left\|f^F+f^G+\sum_Kt_K\delta_K\right\|_H^2\\
 &+\frac14\sum_K(1-t_K^2)\|\delta_K\|_H^2.
 \end{aligned}}
\tag{6.1}
\]

Consequently, if some fractional component vector \(t\in[-1,1]^{\mathcal K}\)
makes the right side at most \(T\), then some genuine exact switched factor
has centered energy at most \(T\).

#### Proof

The mean of the numerator in (5.2) is

\[
 f^F+f^G+\sum_Kt_K\delta_K.
\]

Independence makes the covariance trace

\[
 \sum_K(1-t_K^2)\|\delta_K\|_H^2.
\]

The mean-square decomposition proves (6.1), and some integral outcome is no
larger than its expectation. \(\square\)

This criterion shows exactly how biased choices may improve fair coins:
they may move the mean toward the affine target
\(-f^F-f^G\), while paying only the residual Bernoulli variance.  It also
shows why a fractional cancellation alone is insufficient; components with
\(|t_K|\ll1\) retain nearly their full variance.

---

## 7. A two-seed descent criterion

The unrelated endpoint \(G\) may have a different energy from \(F\).  From
(3.5),

\[
 \boxed{
 \mathbb E\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F)
 =\frac{\mathcal Q_H(G)-\mathcal Q_H(F)}2
  -\frac{A(F,G)-V(F,G)}4.}
\tag{7.1}
\]

Thus coherent separation must pay both the component variance and the
energy price of importing the second seed.

### Theorem 7.1 -- sufficient unrelated-seed heat gap

Let \(T_m\ge0\).  Suppose there are constants \(\eta>0,C<\infty\) such
that every exact factor \(F\) admits an exact factor \(G\) with

\[
 \boxed{
 A(F,G)-V(F,G)
 \ge
 2\bigl(\mathcal Q_H(G)-\mathcal Q_H(F)\bigr)
 +\eta\mathcal Q_H(F)-CT_m.}
\tag{7.2}
\]

Then there exists an exact factor \(F_*\) with

\[
 \boxed{
 \mathcal Q_H(F_*)\le\frac C\eta T_m.}
\tag{7.3}
\]

#### Proof

Let \(F_*\) minimize \(\mathcal Q_H\) over the finite exact-factor fibre.
Every switched child is an exact factor, so its expected energy is at least
\(\mathcal Q_H(F_*)\).  Apply (7.1) and (7.2) at \(F_*\):

\[
 0\le
 \frac{\mathcal Q_H(G)-\mathcal Q_H(F_*)}{2}
 -\frac{A-V}{4}
 \le -\frac\eta4\mathcal Q_H(F_*)+\frac C4T_m.
\]

This proves (7.3). \(\square\)

Equivalently, one may iterate the fair switch: (7.2) gives a child with

\[
 \mathcal Q_H(F_\varepsilon)
 \le\left(1-\frac\eta4\right)\mathcal Q_H(F)+\frac C4T_m.
\]

For the modest target requested in the two-seed proposal, one may take
\(T_m=W\) at one depth or \(T_m=HW=O(W\sqrt m)\) on a fixed Gaussian
window.  A constant-one proof would require the correspondingly sharper
target dictated by its final transfer ledger.

At a global minimizer \(F_*\), every unrelated seed \(G\) necessarily
obeys the exact reverse inequality

\[
 \boxed{
 A(F_*,G)-V(F_*,G)
 \le2\bigl(\mathcal Q_H(G)-\mathcal Q_H(F_*)\bigr).}
\tag{7.4}
\]

Indeed, otherwise the fair expectation in (7.1) would lie below the global
minimum.  Likewise, Theorem 5.1 gives

\[
 \operatorname{ADisc}_H(F_*,G)\ge4\mathcal E_H(F_*).
\tag{7.5}
\]

Thus a successful two-seed theorem must use special wreath geometry to
force (7.2) whenever the global minimum is still large; abstract component
switching alone cannot do so.

---

## 8. What the proposal does and does not remove

The exact audit is:

1. **Exact ownership and completion are solved.**  Every component signing
   is already one exact integral factor.
2. **Unrelated seeds can create genuine midpoint cancellation.**  This is
   absent from a comparison whose two endpoints are forced to have the same
   structured bias.
3. **Midpoint cancellation is a new hypothesis, not an automatic fact.**
   Taking \(F=G\) gives \(V=0\) while preserving any arbitrarily large
   seed energy.  Thus component variance is not the only two-seed gate.
4. **For fair coins, variance remains the complete rounding loss.**  Once
   the midpoint is controlled, (3.4) has no other error term.
5. **Deterministic signs may beat fair variance.**  The sharp gate is
   affine discrepancy (5.1), with biased relaxation (6.1).  They give no
   universal improvement: connected overlays and orthogonal component
   effects attain the fair obstruction.
6. **A concrete sufficient structural target is now available.**  It is
   enough to construct counterbiased factors satisfying (4.6) whose direct
   overlay has bounded size-biased component size (4.5).  More generally,
   one may replace bounded components by an affine-discrepancy theorem.
7. **The required pair is not supplied by the canonical MSW factor.**
   Repointing, reversing, or coordinate-relabeling one MSW factor gives a
   highly related endpoint and returns to the previously audited
   relabeling/component-variance setting.  This note does not construct,
   uniformly for all \(m\), two genuinely unrelated exact factors with the
   counterbias and overlay geometry required by (4.5)--(4.6).

Therefore the two-seed proposal is a legitimate new escape from the
relabeling zero-drift symmetry, but it is not yet a proof.  Its exact missing
object is a pair of counterbiased exact factors with either small component
second moment or small affine component discrepancy.
