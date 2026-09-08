# Crossing-core bridge to pointed factor selection

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Result

This note does not prove the remaining exact-factor inequality in
`MATH_ATTACK_H_POINTED_CYCLIC_FLAG_EXTRACTION_20260725.md`.  It proves the
exact implication available from the audited crossing structure.

For one exact factor \(F\), suppose one common balanced nested resolution
can be obtained after releasing a single exceptional owner family \(E\)
and freezing every canonical path outside \(E\).  Then at every controlled
depth

\[
 O_q(F)\le |E|.
\]

More sharply, only exceptional owners whose canonical depth-\(q\) target
lies in an overloaded fibre are charged at depth \(q\).  If the sum of
these charged owner-depth incidences is below half the audited shoulder
supply by \(\Omega(HW)\), the pointed factor-selection inequality follows.
A common cover of sufficiently small cardinality is a transparent
corollary.  It proves exactly the literal pointed extraction conclusion of
the cited report, not by itself a complete multiscale fusion or
constant-one theorem.

The crossing inequalities do not themselves decrease the overload.  Their
role is to certify that the **same** exceptional owners support one integral
completion at all depths.  The overload estimate uses the survival part of
that common certificate.  At depth at least two, target deficit can be
inherited from a parent neighborhood and need not activate a crossing
packet.  This exact inheritance is the obstruction to turning the audited
crossing theorem into an unconditional factor-selection theorem.

## 1. Common alignment number

Put

\[
 n=2m+1,
 \qquad W=\binom nm,
 \qquad H=\lceil A\sqrt m\rceil\le m-1.
\]

Let \(F\) be one oriented exact wreath factor and let

\[
 \Gamma_0(X)\supset\Gamma_1(X)\supset\cdots\supset\Gamma_H(X)
\]

be its canonical paths, one for each middle owner
\(X\in\binom{[n]}m\).  Write

\[
 \ell_q(S)=|\{X:\Gamma_q(X)=S\}|.
\]

Fix one common balanced integral nested load vector \(b=(b_q)_{q=0}^H\),
so

\[
 b_q(S)\in\{c_q,c_q+1\},
 \qquad
 c_q=\left\lfloor\frac W{\binom n{m-q}}\right\rfloor,
\]

and \(b\) is realized by one integral family of nested paths.  Define the
fixed-quota overload

\[
 O_q^b(F)=\sum_S(\ell_q(S)-b_q(S))_+.
\tag{1.1}
\]

The overload used in the pointed extraction report is

\[
 O_q(F)=\min_{\beta_q\text{ balanced}}
          \sum_S(\ell_q(S)-\beta_q(S))_+,
\tag{1.2}
\]

and therefore

\[
 O_q(F)\le O_q^b(F).
\tag{1.3}
\]

Let \(\chi_H(F;b)\) be the minimum \(|E|\) over owner sets
\(E\subseteq\binom{[n]}m\) for which every canonical path outside \(E\)
extends, together with rerouted paths rooted at \(E\), to one common
integral nested resolution having load vector \(b\).  By the audited
owner-cover theorem, this is equivalently the minimum size of one owner set
meeting every survival packet and every directed crossing packet for
\((F,b)\).  Since \(b\) itself is a common resolution, releasing all
owners is feasible and \(\chi_H(F;b)\le W\).

For a feasible \(E\), define its overload-fibre incidence at depth \(q\) by

\[
 J_q(F,b;E)
 =\sum_{\substack{S:\ \ell_q(S)>b_q(S)}}a_q^E(S)
 =|\{X\in E:\ell_q(\Gamma_q(X))>b_q(\Gamma_q(X))\}|,
\tag{1.4}
\]

and put

\[
 J_H(F,b;E)=\sum_{q=1}^HJ_q(F,b;E).
\tag{1.5}
\]

Let \(\jmath_H(F;b)\) be the minimum of (1.5) over all feasible common
exceptional sets \(E\).  The same owner set is used at every depth; this is
not a sum of independently minimized rankwise costs.

## 2. Exact crossing-core bridge

### Theorem 2.1 — weighted common completion bounds every overload

For every exact factor \(F\), every common balanced load vector \(b\), and
every feasible common exceptional set \(E\),

\[
\boxed{
 O_q(F)\le O_q^b(F)\le J_q(F,b;E)\le |E|
 \qquad(1\le q\le H).}
\tag{2.1}
\]

In particular,

\[
\boxed{
 2\sum_{q=1}^H O_q(F)
 \le2\jmath_H(F;b)
 \le 2H\chi_H(F;b).}
\tag{2.2}
\]

#### Proof

Take any feasible common exceptional set \(E\), and put

\[
 a_q^E(S)=|\{X\in E:\Gamma_q(X)=S\}|.
\]

The frozen load is \(f_q^E=\ell_q-a_q^E\).  Feasibility of the residual
completion makes every residual demand nonnegative:

\[
 r_q^E(S)=b_q(S)-f_q^E(S)
 =b_q(S)-\ell_q(S)+a_q^E(S)\ge0.
\]

Thus, for every overloaded target \(S\),

\[
 (\ell_q(S)-b_q(S))_+\le a_q^E(S).
\]

Summing only over the overloaded fibres, and then using the fact that every
exceptional owner has exactly one depth-\(q\) target, gives

\[
 O_q^b(F)
 \le\sum_{\ell_q(S)>b_q(S)}a_q^E(S)
 =J_q(F,b;E)\le |E|.
\]

Use (1.3) to obtain (2.1).  Sum in \(q\) and minimize over feasible
\(E\).  Finally, an \(E\) of minimum cardinality has
\(J_H(F,b;E)\le H|E|=H\chi_H(F;b)\), proving (2.2). \(\square\)

### Corollary 2.2 — exact weighted bridge to pointed extraction

If one feasible triple \((F,b,E)\) satisfies

\[
\boxed{
 2J_H(F,b;E)
 \le S_{\mathcal T}-\varepsilon_AHW}
\tag{2.3}
\]

for a fixed \(\varepsilon_A>0\), then

\[
 S_{\mathcal T}-2\sum_{q=1}^HO_q(F)
 \ge\varepsilon_AHW.
\tag{2.4}
\]

Hence the pointed extraction theorem applies to the unchanged literal word
of \(F\).

#### Proof

Before minimizing over \(E\), the proof of (2.2) gives
\(2\sum_qO_q(F)\le2J_H(F,b;E)\).  Apply (2.3). \(\square\)

### Corollary 2.3 — a constant-density common cover is sufficient

Let \(S_{\mathcal T}\) be the audited floor-weighted shoulder supply from
the pointed extraction theorem, and suppose

\[
 S_{\mathcal T}\ge\gamma_AHW
\tag{2.5}
\]

for a fixed \(\gamma_A>0\).  If, for some exact factor \(F\), common
balanced load vector \(b\), and fixed \(0<\eta<\gamma_A/2\),

\[
\boxed{
 \chi_H(F;b)
 \le\left(\frac{\gamma_A}{2}-\eta\right)W,}
\tag{2.6}
\]

then

\[
\boxed{
 S_{\mathcal T}-2\sum_{q=1}^HO_q(F)
 \ge2\eta HW.}
\tag{2.7}
\]

Hence Corollary 4.1 of the pointed extraction report applies with
\(\varepsilon_A=2\eta\), preserving the original exact factor and literal
contiguous-OR witnesses.

#### Proof

Combine (2.2), (2.5), and (2.6):

\[
 S_{\mathcal T}-2\sum_{q=1}^HO_q(F)
 \ge\gamma_AHW-2H
 \left(\frac{\gamma_A}{2}-\eta\right)W
 =2\eta HW.
\]

\(\square\)

In particular, \(\chi_H(F;b)=o(W)\) suffices.  If exceptions must be whole
wreath rows, \(E\) is the union of \(n|\mathcal B|\) owners and
\(W=n\operatorname{Cat}_m\).  Condition (2.6) becomes

\[
 |\mathcal B|
 \le\left(\frac{\gamma_A}{2}-\eta\right)
       \operatorname{Cat}_m.
\tag{2.8}
\]

Thus the fixed-window row-cover target
\(o(\operatorname{Cat}_m/\sqrt m)\) would be far more than sufficient.

## 3. Exact discrepancy inheritance across a crossing

The bridge above does not construct the common exceptional set.  The next
identity isolates why the large singleton packets do not do so
automatically.

For a fixed common quota flow \(b\), put

\[
 g_q(S)=b_q(S)-\ell_q(S),
 \qquad
 g_{q-1}(N_q(\mathcal A))
 =\sum_{R\in N_q(\mathcal A)}g_{q-1}(R).
\]

### Lemma 3.1 — exact crossing-defect identity

For every \(q\ge1\) and \(\mathcal A\subseteq V_q\),

\[
\boxed{
 |\mathcal C_q(\mathcal A)|-\kappa_q^b(\mathcal A)
 =g_q(\mathcal A)-g_{q-1}(N_q(\mathcal A)).}
\tag{3.1}
\]

In particular, a singleton crossing packet at \(S\in V_q\) is active
exactly when

\[
 g_q(S)>g_{q-1}(N_q(S)).
\tag{3.2}
\]

At depth one the rightmost term is zero, so every positive target deficit
is active.  At every later depth, a positive deficit can be completely
screened by aggregate deficit in its parent neighborhood.

#### Proof

The two definitions give

\[
 |\mathcal C_q(\mathcal A)|
 =\ell_{q-1}(N_q(\mathcal A))-\ell_q(\mathcal A)
\]

and

\[
 \kappa_q^b(\mathcal A)
 =b_{q-1}(N_q(\mathcal A))-b_q(\mathcal A).
\]

Subtracting proves (3.1).  At depth zero \(b_0=\ell_0=1\), so
\(g_0=0\), proving the final assertions. \(\square\)

The direct positive-part charging estimate obtained from (3.1) loses a
linear factor.  Indeed, using
\((\sum x_i)_+\le\sum(x_i)_+\),

\[
 \sum_{S\in V_q}
   \bigl(g_{q-1}(N_q(S))\bigr)_+
 \le (m-q+1)
      \sum_{R\in V_{q-1}}(g_{q-1}(R))_+,
\tag{3.3}
\]

because a parent \(R\) has exactly \(m-q+1\) children in \(V_q\).
The multiplicity factor is \(\Theta(m)\) in the fixed window.  Thus a
proof which simply charges every inactive child deficit to all of its
positive parent deficits loses a linear factor.  No claim is made that
equality in (3.3) is realized by canonical wreath loads; the point is that
the audited crossing identities themselves provide no better multiplicity
bound.  Formula (3.3) does not rule out a sharper estimate that exploits
additional structure of realizable cyclic load vectors.

## 4. What failure of factor selection forces

The following elementary consequence records the scale at which any
counterexample must operate.  It is diagnostic, not a replacement for
common ownership.

### Lemma 4.1 — overload proliferation

Suppose

\[
 \sum_{q=1}^H O_q(F)\ge aHW
\tag{4.1}
\]

for some \(0<a<1\).  For every \(0<\theta<a\), at least

\[
\boxed{
 \frac{a-\theta}{1-\theta}H}
\tag{4.2}
\]

depths satisfy \(O_q(F)\ge\theta W\).  At each such depth, for any
balanced quota attaining \(O_q(F)\), at least

\[
\boxed{
 \frac{\theta W}{\Delta_A}}
\tag{4.3}
\]

targets have positive deficit, where
\(\Delta_A=\max_{q\le H}(c_q+1)=O_A(1)\).

#### Proof

Let \(r\) be the number of depths with overload at least \(\theta W\).
Since \(O_q(F)\le W\),

\[
 aHW\le\sum_qO_q(F)
 \le rW+(H-r)\theta W.
\]

Rearrangement gives (4.2).  For an attaining balanced quota, total positive
deficit equals \(O_q(F)\), while each target deficit is at most its quota
and hence at most \(\Delta_A\).  This proves (4.3). \(\square\)

More precisely, let \((F_m)\) be a sequence of exact factors such that,
for every fixed \(C,\delta>0\), all sufficiently large indices admit no
pointed extraction on at most \(CW/H\) starts carrying at least \(\delta W\)
globally distinct prescribed targets with the required parent-rainbow
property.  If (2.5) holds, the exact contrapositive in the pointed report
then gives

\[
 \sum_{q=1}^H O_q(F)
 \ge\left(\frac{\gamma_A}{2}-o(1)\right)HW.
\]

Lemma 4.1 therefore forces positive-density overload on a positive fraction
of the depths and positive deficit on \(\Omega_A(W)\) targets at each of
those depths.  Lemma 3.1 shows the unresolved point: beyond depth one those
deficits need not be active crossing demands, and the parent-neighborhood
screening can be counted with linear multiplicity.

## 5. Exact proved and unproved boundary

### Proved

1. Survival plus all crossing-cover inequalities are exactly equivalent to
   one integral common residual completion.
2. Any such completion with exceptional owner set \(E\) gives
   \(O_q(F)\le J_q(F,b;E)\le|E|\) simultaneously at all controlled
   depths.
3. The weighted common-owner condition
   \(2J_H\le S_{\mathcal T}-\varepsilon_AHW\) proves the exact pointed
   factor-selection inequality.  A common cover of size
   \((\gamma_A/2-\eta)W\) proves the exact pointed factor-selection
   inequality with margin \(2\eta HW\) as a coarser corollary.
4. Crossing activity is the inter-depth discrepancy increment (3.1), not
   the child deficit alone.  Parent-neighborhood inheritance is absent only
   at depth one.
5. Failure of factor selection forces positive-density overload at a
   positive fraction of Gaussian depths, but this does not select a common
   exceptional owner set.

### Sufficient unproved weighted crossing-based replacement lemma

For every fixed \(A\) and all sufficiently large \(m\), prove that there
are one exact factor \(F_m\), one common balanced integral nested load
vector \(b\), and one owner family \(E_m\) satisfying **all** survival and
directed crossing-cover inequalities through depth
\(H=\lceil A\sqrt m\rceil\), such that

\[
\boxed{
 2J_H(F_m,b;E_m)
 \le S_{\mathcal T}-\varepsilon_AHW
}
\tag{5.1}
\]

for some fixed \(\varepsilon_A>0\).  A more transparent but stronger
cardinality sufficient form is

\[
 |E_m|
 <\frac{S_{\mathcal T}}{2H}-\frac{\varepsilon_A}{2}W.
\tag{5.2}
\]

Under (2.5), an even simpler constant-density version, for fixed
\(0<\eta_A<\gamma_A/2\), is

\[
 |E_m|\le
 \left(\frac{\gamma_A}{2}-\eta_A\right)W.
\tag{5.3}
\]

The cardinality forms are weaker targets than fixed-window alignment
\(|E|=o(W/\sqrt m)\), but even they are not proved by the three audited A
reports.  The weighted condition (5.1) is the exact sufficient threshold
furnished by this bridge.  It is not claimed necessary for factor
selection, because the independently minimizing overloads in (1.2) can be
strictly smaller than the fixed-\(b\) overloads.

### Adversarial audit

1. **The crossing half is not used to prove the numeric overload bound.**
   The inequalities \(O_q^b(F)\le J_q(F,b;E)\le|E|\) follow from residual
   node nonnegativity, equivalently the survival constraints.  The crossing
   half is indispensable only for certifying one realizable common nested
   completion.  It would be incorrect to advertise (2.1) as a new
   quantitative consequence of large crossing-packet rank.
2. **The implication is one-way.**  Small \(\sum_qO_q(F)\) need not furnish
   one common \(E\) or satisfy crossing Hall cuts.  The depth-one potential
   theorem already shows an additional labelled compatibility cost.
3. **Linear rank is not linear cover cost.**  A depth-one singleton deficit
   requires only one or two exceptional owners from a packet of
   \(m+O(1)\) distinct rows.  No packet-disjointness estimate is available.
4. **No separate factors or quotas.**  Theorem 2.1 fixes one \(F\), one
   common \(b\), and one \(E\) through all depths.  Lemma 4.1 may inspect
   rankwise minimizing quotas only as a diagnostic and is not used as a
   common completion.
5. **Literal realizability is preserved.**  The residual flow is auxiliary.
   Once (2.4) or (2.7) holds, the pointed extraction theorem selects
   intervals from the unchanged literal word of the same exact factor
   \(F\); no reset or seam is appended.
6. **No complete fusion or constant-one claim.**  Corollary 2.2 proves only
   the cited pointed extraction conclusion.  The unproved factor/core
   selection in (5.1), and the remaining fusion steps outside this note,
   are not discharged.
