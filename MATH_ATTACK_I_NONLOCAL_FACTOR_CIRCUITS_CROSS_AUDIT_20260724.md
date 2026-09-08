# Cross-audit of the nonlocal exact-factor circuit attack

## 1. Verdict

This is an independent audit of
MATH_ATTACK_I_NONLOCAL_FACTOR_CIRCUITS_20260724.md.

The central exact algebra is sound:

1. the group-component product in Theorem 3.1 always produces an exact
   middle factor;
2. the group-Haar identities (4.1)--(4.7), including all factors of
   \(1/2\) and the one-transposition specialization, are exact;
3. the static two-transposition rectangle collapses to a
   one-transposition partial-support trade for \(n\ge5\);
4. the circuit identities (6.1)--(6.5) depend only on the net endpoint
   effect and are exact; and
5. \((\mathrm{CHF}_A)\), as stated, is a sufficient exact-factor descent
   theorem for the fixed \(A\)-window.

Four corrections or qualifications are required.

* The rectangle theorem and whole-factor no-go need the hypothesis
  \(n\ge5\).  They are false at \(n=3\).
* Enlarging a coordinate group coarsens the component partition and hence
  reduces the number of independently selectable component blocks.  It
  need not reduce the total number of distinct product factors, because
  the larger group also supplies more translations.
* Only centered conditional heat innovations are martingale differences.
  There is no general nonnegative-covariance theorem for the actual
  increments; independent-innovation contraction chains can have negative
  cross-time covariance.  Consequently the report does not prove that
  independent or recomputed exact-factor heat can never realize useful
  packet cancellation.
* \((\mathrm{CHF}_A)\) is one strong sufficient uniform descent lemma.  It
  is not proved necessary, equivalent to MWB, or minimal.  One fixed value
  of \(A\) gives only one fixed-window result.  The final OR bound requires
  the statement for every fixed \(A\), or at least for an unbounded
  sequence of fixed windows, followed by diagonalization.

The corrected conditional implication to the OR bound remains valid.
The route preserves one exact middle factor and one common set of
component choices at every depth, but it proves only unlabelled histogram
overload.  It does not produce the stronger common labelled nested
resolution \((\mathrm{CA}_A)\).

No computation or finite search is used below.

---

## 2. Exact group-component product

Let \(F\) be an exact middle factor, let \(\Gamma\le S_n\), and denote by
\(o_F(M)\) the unique owner in \(F\) of a middle mask \(M\).  The graph
\(\mathcal G_\Gamma(F)\) joins

\[
o_F(M)\quad\hbox{to}\quad o_F(gM)
\qquad(M\in\binom{[n]}m,\ g\in\Gamma).
\tag{2.1}
\]

For a component \(K\), put

\[
\mathcal M(K)=\bigcup_{C\in K}\mathcal W_m(C).
\]

### Theorem 2.1

For every component \(K\):

\[
g\mathcal M(K)=\mathcal M(K)\qquad(g\in\Gamma).
\tag{2.2}
\]

For every \(h\in\Gamma\), the family \(hK\) covers
\(\mathcal M(K)\) exactly once.  Therefore every independent component
choice \(\mathbf h=(h_K)_K\) produces an exact factor

\[
F_{\mathbf h}=\bigcup_K h_KK.
\tag{2.3}
\]

#### Proof

If \(M\in\mathcal M(K)\), then \(o_F(M)\in K\).  By the definition of the
graph, \(o_F(gM)\) is in the same component, so
\(gM\in\mathcal M(K)\).  This gives
\(g\mathcal M(K)\subseteq\mathcal M(K)\); applying the same argument to
\(g^{-1}\) gives equality.

Coordinate relabelling is bijective on wreaths and masks, and

\[
\mathcal W_m(hC)=h\mathcal W_m(C).
\]

Thus \(hK\) covers

\[
h\mathcal M(K)=\mathcal M(K)
\]

exactly once.  The sets \(\mathcal M(K)\) for distinct components
partition the middle layer, because \(F\) is exact.  Hence (2.3) covers
every middle mask exactly once.

It remains only to exclude a repeated wreath in the union.  If a wreath
\(C\) belonged to both \(h_KK\) and \(h_LL\), where \(K\ne L\), every
middle mask of \(C\) would belong to both \(\mathcal M(K)\) and
\(\mathcal M(L)\), contradicting their disjointness.  Thus (2.3) is a
set-valued exact factor. \(\square\)

Stabilizers cause no exception: uniform choices below are uniform in group
elements, not necessarily uniform in distinct translated factors.

If \(\Gamma_1\le\Gamma_2\), every \(\Gamma_2\)-component is a union of
\(\Gamma_1\)-components.  This proves monotonicity only for the number of
independently selectable component blocks.  There is no proved
monotonicity for the cardinality of

\[
\{F_{\mathbf h}:\mathbf h\in\Gamma^{\mathcal K}\},
\]

because passing to a larger group simultaneously creates more possible
translations of each coarser block.

If \(\Gamma\) is transitive on middle masks, the component graph is
connected.  Indeed, for \(C,D\in F\), choose
\(M\in\mathcal W_m(C)\), \(M'\in\mathcal W_m(D)\), and \(g\in\Gamma\)
with \(gM=M'\).  Equation (2.1) directly joins \(C\) and \(D\).
The product construction then has one component and yields only the
global relabellings \(gF\).

---

## 3. Exact group-Haar identity

The coordinate action on a rank-\(r\) vector is

\[
(gu)(S)=u(g^{-1}S).
\tag{3.1}
\]

It is unitary for counting measure at every rank, hence for the weighted
multidepth inner product \(\langle\ ,\ \rangle_H\).  The shadow maps are
equivariant:

\[
\mathcal A_{m-q}\mathbf1_{gK}
=g\mathcal A_{m-q}\mathbf1_K.
\tag{3.2}
\]

For a component \(K\), write

\[
a_K=(\mathcal A_{m-q}\mathbf1_K)_{q\le H},
\qquad
P_\Gamma=\frac1{|\Gamma|}\sum_{g\in\Gamma}g.
\]

Since \(\Gamma\) is finite and acts unitarily, \(P_\Gamma\) is the
orthogonal projection onto the invariant subspace.

### Theorem 3.1

For every group-component product,

\[
f(F_{\mathbf h})
=P_\Gamma f(F)+
\sum_K(h_Ka_K-P_\Gamma a_K),
\tag{3.3}
\]

and the two terms on the right are orthogonal.  Consequently

\[
\Psi_H(F_{\mathbf h})+\frac12B_H
=\frac12\|P_\Gamma f(F)\|_H^2
+\frac12\left\|
\sum_K(h_Ka_K-P_\Gamma a_K)
\right\|_H^2.
\tag{3.4}
\]

If

\[
A_\Gamma(F)=\|(I-P_\Gamma)f(F)\|_H^2
\]

and

\[
R_\Gamma(F)=
\min_{\mathbf h}
\left\|\sum_K(h_Ka_K-P_\Gamma a_K)\right\|_H^2,
\]

then

\[
\boxed{
\Psi_H(F)-\min_{\mathbf h}\Psi_H(F_{\mathbf h})
=\frac12\bigl(A_\Gamma(F)-R_\Gamma(F)\bigr).}
\tag{3.5}
\]

#### Proof

Equivariance and Theorem 2.1 give

\[
f(F_{\mathbf h})=\sum_Kh_Ka_K-\lambda\mathbf1.
\]

Because the rankwise constant vector is invariant,

\[
P_\Gamma f(F)=\sum_KP_\Gamma a_K-\lambda\mathbf1.
\]

Their difference is the residual in (3.3).  Moreover

\[
P_\Gamma(h_Ka_K-P_\Gamma a_K)=0
\]

for every \(K\), so the residual lies in \(\ker P_\Gamma\) and is
orthogonal to \(P_\Gamma f(F)\).  Using

\[
\Psi_H(G)+\frac12B_H=\frac12\|f(G)\|_H^2
\]

proves (3.4).

For the identity component choice, the residual is

\[
\sum_K(a_K-P_\Gamma a_K)=(I-P_\Gamma)f(F),
\]

whose squared norm is \(A_\Gamma(F)\).  Minimizing the second term in
(3.4) proves (3.5). \(\square\)

At a global minimizer \(F_*\) of this same fixed-\(H\) objective, every
group child is exact.  The identity is an admissible choice, so
\(R_\Gamma\le A_\Gamma\), while global minimality and (3.5) give the
reverse inequality.  Hence

\[
\boxed{R_\Gamma(F_*)=A_\Gamma(F_*)}
\tag{3.6}
\]

for every \(\Gamma\).  This equality is not asserted at an arbitrary
factor or at a minimizer of a different depth window.

For independent uniform \(h_K\), set

\[
X_K=h_Ka_K-P_\Gamma a_K.
\]

Then \(\mathbb EX_K=0\), even in the presence of stabilizers, and the
\(X_K\)'s are independent.  Therefore

\[
\mathbb E\left\|\sum_KX_K\right\|_H^2
=\sum_K\mathbb E\|X_K\|_H^2
=V_\Gamma.
\]

Subtracting the identity-choice residual in (3.4) yields exactly

\[
\mathbb E[\Psi_H(F_{\mathbf h})-\Psi_H(F)]
=\frac12(V_\Gamma-A_\Gamma).
\tag{3.7}
\]

For \(\Gamma=\{1,\tau\}\),

\[
P_\Gamma=\frac{I+\tau}{2},\qquad
A_\Gamma=\frac14A_{\tau,H},\qquad
V_\Gamma=\frac14N_{\tau,H}.
\]

Thus (3.7) is precisely

\[
\frac18(N_{\tau,H}-A_{\tau,H}).
\]

For two disjoint transpositions, the four operators

\[
P_{\varepsilon\eta}
=\frac14(I+\varepsilon\tau)(I+\eta\sigma)
\]

are mutually orthogonal character projections.  Expanding every residual
in these four sectors gives (4.7) of the audited report.  Each component
choice supplies two independent character signs, and the third
nontrivial sign is their product.  Hence the \(V_4\) identity is exact,
but it does not authorize three independent Fourier signs.

---

## 4. Static two-transposition rectangles

The required dimension hypothesis must be made explicit.

### Lemma 4.1

Assume \(n=2m+1\ge5\).  If \(U\) is a partial middle factor and
\(\pi\) is a coordinate transposition, then

\[
U\cap\pi U=\varnothing.
\tag{4.1}
\]

#### Proof

Fix a wreath \(C\), and let \(\pi=(u\,v)\).  Across the \(n\) cyclic
middle intervals of \(C\), the total number of incidences of \(u\) and
\(v\) is

\[
2m=n-1.
\]

If every interval contained exactly one of \(u,v\), this total would be
\(n\).  Thus some middle interval contains both or neither and is fixed
as a mask by \(\pi\).  Consequently \(C\) and \(\pi C\) share a middle
mask.

For odd \(n\ge5\), \(C\ne\pi C\).  A nonidentity automorphism of an odd
cycle is either a rotation or a reflection; a reflection fixes one vertex
and transposes \(m\ge2\) pairs.  No automorphism induces just one label
transposition.  A partial factor cannot contain two distinct wreaths
sharing a middle mask, proving (4.1). \(\square\)

At \(n=3\), the unique unoriented cyclic order is stabilized by every
coordinate transposition.  Thus Lemma 4.1 is false, and a whole-factor
rectangle can be the zero vector and hence support-feasible.  This does
not affect the asymptotic application, but it invalidates the unqualified
finite statement.

### Theorem 4.2

Assume \(n\ge5\).  Let \(U\) be a partial factor and let
\(\tau,\sigma\) be distinct coordinate transpositions, with no
commutativity assumption.  Set

\[
z=(I-\tau)(I-\sigma)\mathbf1_U.
\tag{4.2}
\]

Then \(z\) is support-feasible if and only if

\[
P=U\mathbin{\dot\cup}\tau\sigma U
\tag{4.3}
\]

is a partial factor and

\[
\mathcal A_m\mathbf1_P
=\tau\mathcal A_m\mathbf1_P.
\tag{4.4}
\]

In that case

\[
z=\mathbf1_P-\mathbf1_{\tau P},
\qquad
\tau P=\tau U\mathbin{\dot\cup}\sigma U.
\tag{4.5}
\]

#### Proof

The nominal positive families are \(U,\tau\sigma U\), and the nominal
negative families are \(\tau U,\sigma U\).  Every positive-negative
intersection is empty by Lemma 4.1, after applying a coordinate
permutation when needed.  For example,

\[
\tau\sigma U\cap\sigma U\ne\varnothing
\]

would, after applying \((\tau\sigma)^{-1}\), give

\[
U\cap(\sigma\tau\sigma)U\ne\varnothing,
\]

where \(\sigma\tau\sigma\) is a transposition.

Moreover, \(\tau\) maps

\[
U\cap\tau\sigma U
\quad\hbox{bijectively to}\quad
\tau U\cap\sigma U.
\]

Hence either both same-sign intersections are empty, or coefficients
\(+2\) and \(-2\) occur.  No cross-sign cancellation is available.  In
the support-feasible case the same-sign families must therefore be
disjoint, the positive side is \(P\), and the negative side is
\(\tau P\).  The remaining support-feasibility conditions are exactly
that \(P\) is a partial factor and that the two sides cover the same
middle masks, which is (4.4).  This proves (4.5). \(\square\)

If \(P\) and \(\tau P\) have a common exact-factor completion \(R\), the
claim about ordinary ownership components is also valid.  Let
\(\mathscr S\) be the middle support of \(P\).  Equation (4.4) and
partial-factor integrality imply

\[
\tau\mathscr S=\mathscr S.
\]

In the ordinary \(F=P\cup R\) versus \(\tau F\) ownership graph, an edge
whose mask lies in \(\mathscr S\) stays inside \(P\), while an edge whose
mask lies in \(\mathscr S^c\) stays inside \(R\).  Hence \(P\) is a union
of ordinary \(\tau\)-components, and switching those components replaces
\(P\) by \(\tau P\) while leaving \(R\) fixed.

For an exact factor \(F\), the whole-factor rectangle is not
support-feasible when \(n\ge5\).  If either same-sign intersection is
nonempty, a coefficient of magnitude two occurs.  Otherwise each sign is
the disjoint union of two exact factors and covers every middle mask
twice, so it is not a partial factor.  Thus the corrected rectangle
collapse and whole-factor no-go are unconditional for the asymptotic
range \(n\ge5\).

---

## 5. Circuit composition and the heat-increment correction

Let

\[
F_0\to F_1\to\cdots\to F_t
\]

be a legal path of exact factors, and put

\[
\delta_i=f(F_i)-f(F_{i-1}),\qquad
D=\sum_i\delta_i=f(F_t)-f(F_0).
\]

### Theorem 5.1

The endpoint identities

\[
\boxed{
\Psi_H(F_t)-\Psi_H(F_0)
=\langle f(F_0),D\rangle_H+\frac12\|D\|_H^2}
\tag{5.1}
\]

and

\[
\boxed{
\begin{aligned}
\Psi_H(F_t)-\Psi_H(F_0)
={}&\sum_i\left(
\langle f(F_0),\delta_i\rangle_H
+\frac12\|\delta_i\|_H^2\right)\\
&+\sum_{i<j}\langle\delta_i,\delta_j\rangle_H
\end{aligned}}
\tag{5.2}
\]

are exact.

#### Proof

The floor term \(B_H/2\) is factor-independent, so

\[
\Psi_H(F_i)-\Psi_H(F_{i-1})
=\langle f(F_{i-1}),\delta_i\rangle_H
+\frac12\|\delta_i\|_H^2.
\]

Insert

\[
f(F_{i-1})=f(F_0)+\sum_{j<i}\delta_j
\]

and sum.  This gives (5.2).  Expanding
\(\|\sum_i\delta_i\|_H^2\) gives (5.1). \(\square\)

At one depth \(q\),

\[
D_q=0
\quad\Longleftrightarrow\quad
\sum_{i<j}\langle\delta_{i,q},\delta_{j,q}\rangle_2
=-\frac12\sum_i\|\delta_{i,q}\|_2^2.
\tag{5.3}
\]

This is simply the expansion of \(\|D_q\|_2^2=0\).  A closed factor path
has \(D=0\), so its energy change is zero.  If the endpoint is a global
coordinate relabelling \(\pi F_0\), unitary invariance gives

\[
\langle f,(\pi-I)f\rangle_H
=-\frac12\|(\pi-I)f\|_H^2,
\]

so a global coordinate word, including a coordinate commutator, also has
zero energy descent.  Formula (6.5) for four corners follows by expanding

\[
f_{11}=f_{00}+a+b+h
\]

and is correct.

There is, however, no valid inference that the actual increments of an
independent heat chain have nonnegative cross-time covariance.  If
\(\mathcal F_{i-1}\) is the past, only

\[
\xi_i=\delta_i-\mathbb E(\delta_i\mid\mathcal F_{i-1})
\tag{5.4}
\]

is a martingale difference.  The centered innovations are orthogonal in
\(L^2\), but the increments \(\delta_i\) include state-dependent drift.
They need not be orthogonal and may have negative covariance.

A scalar contraction already demonstrates the logical point.  Let
\(\varepsilon_1,\varepsilon_2\) be independent centered variables,
\(0<\rho<1\), and define

\[
X_0=0,\qquad X_1=\varepsilon_1,\qquad
X_2=\rho X_1+\varepsilon_2.
\]

Then

\[
\delta_1=\varepsilon_1,\qquad
\delta_2=(\rho-1)\varepsilon_1+\varepsilon_2,
\]

and

\[
\mathbb E[\delta_1\delta_2]
=(\rho-1)\mathbb E[\varepsilon_1^2]<0.
\tag{5.5}
\]

This example does not prove that an exact-factor heat chain attains the
needed packet estimate.  It proves that martingale variance additivity
does not rule it out.  Accordingly, the following statements in the
audited report require qualification:

* consequence 3 after Theorem 6.1 is valid only for the centered
  innovations (5.4), not for the raw increments;
* the assertion that independent heat cannot supply packet cancellation
  is not established by Theorem 6.1; and
* the final phrase that independent dynamic heat merely adds
  nonnegative noise must not be read as a theorem about its net endpoint
  effect.

The report's more cautious statement in Section 8 is correct: an additive
upper bound on step curvatures gives no packet improvement, while negative
cross terms remain a possible source of improvement.

---

## 6. Exact scope of \((\mathrm{CHF}_A)\)

Fix \(A>0\), let \(H=\lceil A\sqrt m\rceil\), and define

\[
\Delta_A(F)=
\max_{\Gamma\in\mathfrak G_m}
\bigl(A_\Gamma(F)-R_\Gamma(F)\bigr).
\tag{6.1}
\]

Equation (3.5) gives the exact reformulation

\[
\boxed{
\Delta_A(F)
=2\left(
\Psi_H(F)-
\min_{\substack{\Gamma\in\mathfrak G_m\\\mathbf h}}
\Psi_H(F_{\Gamma,\mathbf h})
\right).}
\tag{6.2}
\]

Every child in (6.2) is an exact factor, and the same component choice
\(\mathbf h\) is used simultaneously at every depth.

The proposed statement \((\mathrm{CHF}_A)\) is

\[
\Delta_A(F)
\ge\eta_A\Psi_H(F)-C_AH\operatorname{Cat}_m
\tag{6.3}
\]

for every exact factor \(F\), with constants independent of \(m,F\).

### Theorem 6.1

For a fixed \(A\), \((\mathrm{CHF}_A)\) implies the existence of an exact
factor \(F_*\) satisfying

\[
\Psi_H(F_*)
\le\frac{C_A}{\eta_A}H\operatorname{Cat}_m
=O_A(W/\sqrt m)=o(W),
\tag{6.4}
\]

and hence

\[
P_H(F_*)=o(W).
\tag{6.5}
\]

#### Proof

Choose a global minimizer of \(\Psi_H\) on the finite exact-factor fibre.
Every child in (6.2) is exact, so \(\Delta_A(F_*)=0\).  Equation (6.3)
then gives the first inequality in (6.4).  Since

\[
\operatorname{Cat}_m
=\frac{W}{2m+1}
\]

and \(H=O_A(\sqrt m)\), the right side is
\(O_A(W/\sqrt m)\).  Finally, the exact overload ledger gives
\(P_H\le\Psi_H\). \(\square\)

Equivalently, after replacing \(\eta_A\) by
\(\min(\eta_A,1)\), a minimizing child in (6.2) obeys

\[
\Psi_H(F_{\rm next})
\le\left(1-\frac{\eta_A}{2}\right)\Psi_H(F)
+\frac{C_A}{2}H\operatorname{Cat}_m.
\tag{6.6}
\]

Thus \((\mathrm{CHF}_A)\) is a genuine uniform exact-factor descent
statement, not merely a fractional averaging assertion.

Its logical scope is nevertheless narrower than some wording in the
audited report suggests.

1. It is sufficient, not necessary, for fixed-window overload, MWB, or the
   final OR conjecture.
2. It is stronger than the existence of an exact factor with
   \(\Psi_H=o(W)\), because it imposes an affine descent gap at every exact
   factor.
3. The energy conclusion \(\Psi_H=o(W)\) is itself stronger than the
   overload conclusion \(P_H=o(W)\).  Only the one-way inequality
   \(P_H\le\Psi_H\) is proved.
4. Restricting (6.3) to global minimizers is enough for the displayed
   proof, but then it is essentially the desired energy bound in disguise,
   since \(\Delta_A(F_*)=0\).
5. Nothing in the report proves that \((\mathrm{CHF}_A)\) is equivalent to
   the dynamic residual-packet criterion.

Consequently the label “smallest quantitative replacement lemma” is not
justified.  A strictly weaker route-local sufficient condition is the
following.

> **Strict Haar descent \((\mathrm{SHD}_A)\) — UNPROVED.**  There is
> \(\varepsilon_A(m)=o(W)\) such that every exact factor satisfies
> \[
> \Psi_H(F)>\varepsilon_A(m)
> \quad\Longrightarrow\quad
> \Delta_A(F)>0.
> \tag{6.7}
> \]

Indeed, repeatedly choose a strict group child whenever (6.7) applies.
The exact-factor fibre is finite and the energy strictly decreases, so
the process terminates.  It can terminate only at a factor with
\(\Psi_H\le\varepsilon_A(m)\).  Thus \((\mathrm{SHD}_A)\) already proves
fixed-window overload \(o(W)\).  The proposed \((\mathrm{CHF}_A)\) implies
\((\mathrm{SHD}_A)\) with

\[
\varepsilon_A(m)=\frac{C_A}{\eta_A}
H\operatorname{Cat}_m.
\]

This does not make \((\mathrm{SHD}_A)\) necessary or absolutely minimal;
it is simply a clean, strictly weaker group-descent target.

---

## 7. The fractional spectral benchmark is not static CHF

For a vector with zero Johnson degrees \(0\) and \(1\), the report
correctly proves

\[
\mathbb E\|P_{\tau_T}\cdots P_{\tau_1}f\|_H^2
\le\left(1-\frac2n\right)^T\|f\|_H^2
\tag{7.1}
\]

for independent uniform transpositions, where
\(P_\tau=(I+\tau)/2\).

This is a fractional sequential benchmark.  It does not prove the
spectral part of static \((\mathrm{CHF}_A)\):

* the transpositions in (7.1) may overlap and fail to commute;
* the product \(P_{\tau_T}\cdots P_{\tau_1}\) is generally not the group
  average \(P_\Gamma\) for any
  \(\Gamma\in\mathfrak G_m\), whose generators are required to be
  disjoint; and
* the intermediate vectors are fractional projections, not histograms of
  exact factors.

Thus “the spectral part alone is adequate” is correct only as a statement
about the fractional sequential model.  It supplies no theorem controlling
\(A_\Gamma-R_\Gamma\) for the static exact groups.

Moreover, \(T=\Theta(n)\) in (7.1) certifies only a constant-factor
contraction, since

\[
\left(1-\frac2n\right)^T\le e^{-2T/n}.
\]

To use (7.1) as a worst-start guarantee down to the floor/seam scale, one
needs a polynomial-in-\(W\) reduction of the crude initial norm bound.
The displayed estimate certifies such a reduction after

\[
T=\Theta(n\log W)=\Theta(n^2)
\tag{7.2}
\]

steps, since \(\log W=\Theta(n)\).  Equation (7.2) is the scale required
by this particular worst-case contraction certificate, not a lower bound
on every possible coherent procedure.

---

## 8. Fixed windows and the final OR bound

A single fixed instance \((\mathrm{CHF}_A)\) gives (6.4)--(6.5) only for

\[
H=\lceil A\sqrt m\rceil
\]

with that fixed \(A\).  It does not by itself imply the final OR bound,
because the SCD-product tail used in the report requires

\[
\frac H{\sqrt m}\longrightarrow\infty.
\]

The conditional final implication is valid under the family of
hypotheses

\[
(\mathrm{CHF}_A)\quad\text{for every fixed }A>0
\tag{8.1}
\]

or under the corresponding statements for an unbounded sequence of fixed
values of \(A\).

For integers \(j\), choose \(M_j\) so that, once \(m\ge M_j\), an exact
factor has \(j\)-window overload at most \(W/j\).  Define

\[
A(m)=\max\{j\le m^{1/4}:M_j\le m\}.
\]

Then

\[
A(m)\to\infty,\qquad
H=\lceil A(m)\sqrt m\rceil=o(m),\qquad
\frac H{\sqrt m}\to\infty,
\]

and a factor selected for the diagonal window satisfies

\[
\frac{P_H(F)}W\le\frac1{A(m)}\to0.
\]

The audited SCD-product estimate

\[
\nu(2m+1)
\le W+\frac{2H+1}{2m+1}W
+2P_H(F)+2L_m(m-H-1)
\]

then has three \(o(W)\) error terms.  This proves the conditional odd
dimensional OR bound, and the established trimmed one-bit lift gives the
even-dimensional leading constant.

This diagonalization uses only unlabelled overload.  It does not infer a
nearby common labelled owner flow and therefore does not establish
\((\mathrm{CA}_A)\).

---

## 9. Corrected theorem-level summary

### Unconditional results

For every finite coordinate group, the component product (2.3) is an
exact factor.  Its optimal correlated energy descent is exactly

\[
\frac12(A_\Gamma-R_\Gamma).
\]

For \(n\ge5\), every support-feasible static two-transposition rectangle
is a one-transposition partial-support trade.  With a common exact
completion, it is a union of ordinary one-transposition ownership
components.  A whole-factor rectangle is not support-feasible.

Every legal exact-factor circuit satisfies the endpoint quadratic law
(5.1)--(5.3).  Closed circuits and global coordinate relabellings have
zero energy descent.

### Corrected obstruction

The report does not prove a no-go theorem for independent dynamic heat:
only centered innovations have additive variance, while the actual
increments may have negative cross-time covariance.  Static rectangle
collapse remains a valid no-go theorem.

The exact unresolved group quantity is

\[
\Delta_A(F)
=\max_{\Gamma\in\mathfrak G_m}(A_\Gamma-R_\Gamma).
\]

No theorem in the report controls it at the required scale.  The proposed
\((\mathrm{CHF}_A)\) is a strong sufficient uniform bound; the weaker
\((\mathrm{SHD}_A)\) is already sufficient for this group-descent route.
Both remain unproved.

### Conditional result

If \((\mathrm{CHF}_A)\), or any other sufficient fixed-window statement,
holds for every fixed \(A\), then diagonalization yields

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}=o(W)
\]

for some \(H/\sqrt m\to\infty\), \(H=o(m)\), and hence the final OR bound.
A single fixed \(A\) does not suffice for that last implication.
