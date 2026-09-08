# Independent cross-audit of the stationary component-heat report

Audited source: `MATH_ATTACK_Y_STATIONARY_HEAT_REPORT_RAW_20260724.md`.

## Overall verdict

The report's main finite-state identities are mathematically sound for
\(m\ge 2\), after several necessary definitions and scope repairs. In
particular, the intrinsic cell theorem, projection/idempotence, uniform
stationary laws, exact variance formula, covariance/noise formulas (including
the coefficient \(\kappa_j\)), cell-floor decomposition, and Poisson duality
all survive independent derivation.

The audit found no unconditional proof of the open stationary selection
statement \(SCOV_A\), and no counterexample to it. Three broad conclusions in
the source must be weakened:

1. **CORRECTED.** A communicating class need not be a single \(S_n\)-orbit.
   The load-mean conclusion uses class invariance under \(S_n\), together with
   transitivity of \(S_n\) on the target layer, not "class transitivity."
2. **UNSUPPORTED AS STATED.** The fixed indicator-noise trace shows that cube
   entropy or component count does not determine harmonic placement. It does
   not prove that entropy combined with additional exact-factor structure can
   never control lower-shadow alignment.
3. **UNSUPPORTED AS STATED.** The low-stationary-class statement and the
   positive-cut/local-minimum lemma are not known to imply one another. They
   are distinct sufficient routes, not proved to be ordered by strength.

Also, every phrase calling \(SCOV_A\) "the exact remaining statement" or a
covariance theorem "necessary" must be read as restricted to the stationary
class route. It is not known to be necessary for fixed-window overload, MWB,
or the contiguous-OR conjecture.

## 0. Necessary standalone setup and notation repairs

The source is not standalone. Its claims should be read with

\[
n=2m+1,\quad W=\binom nm,\quad N_q=\binom n{m-q},\quad
H_A=\lceil A\sqrt m\rceil,\quad
\operatorname{Cat}_m=\frac Wn,
\]

\[
W=c_qN_q+b_q,\qquad 0\le b_q<N_q,\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,\qquad
\theta_q=\frac{b_q}{N_q},
\]

and

\[
Q_q(F)=\sum_{S\in\binom{[n]}{m-q}}
 (\mu_q(F,S)-c_q)(\mu_q(F,S)-c_q-1),
\qquad
\mathcal Q_A(F)=\sum_{q\le H_A}\frac{Q_q(F)}{c_q}.
\]

For fixed \(A\), all Gaussian-window assertions are asymptotic assertions for
\(m\ge m_0(A)\), so that the listed ranks are admissible. Alternatively, every
finite statement should explicitly restrict to \(0\le q\le
\min(H_A,m-1)\). The intrinsic-cell and pointwise noise-trace statements need
\(m\ge2\); \(m=1\) is a genuine exception.

The incidence operator \(A_r\) maps a wreath-coordinate vector to its cyclic
rank-\(r\) interval histogram. The omitted floor constant is

\[
\boxed{\beta_q=N_q\theta_q(1-\theta_q)
=\frac{b_q(N_q-b_q)}{N_q}.}
\]

In both the covariance and floor sections, the symbol indexing a component
must mean its **left side** \(L_i\subset F\), not the whole ownership
component. The whole component is \(\tau\)-stable, so writing
\(\mathbf1_{\tau K}-\mathbf1_K\) with \(K\) literally the whole component
would give zero.

## 1. Disjointness, intrinsic cells, and projections

### 1.1 A fixed middle interval

**VALID, with the compressed proof expanded.** Let \(C\) be an unoriented
cyclic order and \(\tau=(ab)\). Put the two labels at shorter cyclic distance
\(d\), where \(1\le d\le m\). The complementary open arc has
\(2m-d\ge m\) vertices, so it contains a consecutive \(m\)-set \(X\) avoiding
both \(a\) and \(b\). Hence \(\tau X=X\). Thus \(X\) is a middle interval of
both \(C\) and \(\tau C\).

No transposition stabilizes an unoriented cyclic order when \(m\ge2\). Indeed,
the stabilizer of an unoriented labelled \(n\)-cycle is a conjugate of the
dihedral group \(D_n\). A nontrivial rotation has no cycle type equal to a
single transposition, while for odd \(n=2m+1\) every reflection has cycle type
\(1^1 2^m\). This is not the transposition type \(1^{2m-1}2\) when \(m\ge2\).

Now suppose \(C\in F\cap\tau F\). Then \(C=\tau D\) for some \(D\in F\).
The wreaths \(D\) and \(\tau D\) share the fixed middle interval just found.
Exactness of \(F\) forces them to be the same wreath, but that would make
\(D\) transposition-stable, a contradiction. Therefore

\[
\boxed{F\cap\tau F=\varnothing\qquad(m\ge2).}
\]

For \(m=1\), there is only one unoriented cyclic order, it is fixed by every
coordinate permutation, and this conclusion fails. The source excludes
\(m=1\) in its disjointness line but must carry that qualifier into later
trace claims.

### 1.2 The intrinsic \(\tau\)-cell

**VALID.** Form the edge-labelled bipartite ownership overlay: its left
vertices are the wreaths of \(F\), its right vertices those of \(\tau F\), and
each middle set is an edge between its unique owners. For every left wreath
\(C\), the fixed interval above supplies an edge from \(C\) to \(\tau C\).
Consequently \(\tau\) preserves each connected component and exchanges its
two sides. Write those sides as \(L_i\) and \(\tau L_i\).

Selecting independently either \(L_i\) or \(\tau L_i\) in each component
covers every middle-set edge exactly once, hence gives an exact factor.
Disjointness of \(F\) and \(\tau F\) makes the \(2^k\) choices distinct.

If \(G\) is any such choice, then in the overlay of \(G\) with \(\tau G\) the
same edge-labelled components reappear; only the names of the two sides are
reversed in components switched when passing from \(F\) to \(G\). Therefore
the set of \(2^k\) factors depends only on the cell, not on the chosen base
factor. The \(\tau\)-cells partition the state space.

### 1.3 Projection and stationary classes

**VALID.** On each intrinsic cell, \(K_\tau\) is the all-ones averaging matrix
divided by the cell size. Hence, for the counting inner product,

\[
\boxed{K_\tau^2=K_\tau,\qquad K_\tau^*=K_\tau.}
\]

The support graph of
\(K=\binom n2^{-1}\sum_\tau K_\tau\) is the union of the complete cell graphs
and is undirected. Thus every communicating class \(\mathscr C\) is a union of
whole \(\tau\)-cells for every fixed \(\tau\). Uniform measure on
\(\mathscr C\) is preserved by every block average \(K_\tau\), and therefore
by \(K\). Irreducibility on the class makes this stationary law unique.
Globally, stationary laws are mixtures of these class-uniform laws.

Choosing the opposite side in every component gives \(\tau F\), so every
transposition preserves each communicating class. Since transpositions
generate \(S_n\), every class is \(S_n\)-stable.

Finally, because every \(K_\tau\) is an orthogonal projection,

\[
\left\langle f,(I-K)f\right\rangle
=\binom n2^{-1}\sum_\tau
 \|(I-K_\tau)f\|_2^2.
\]

It follows in both directions that

\[
\boxed{\ker(I-K)=\bigcap_\tau\operatorname{Fix}(K_\tau)
=\bigcap_\tau\operatorname{Ran}(K_\tau).}
\]

This is an exact characterization of the invariant functions, not an
explicit classification of the classes.

## 2. Stationary mean and exact integer variance

### 2.1 Mean load

**CORRECTED WORDING; CONCLUSION VALID.** The sentence "Class transitivity
gives" the mean is too strong: a communicating class need not be a single
\(S_n\)-orbit. What is proved is enough. Its uniform law is \(S_n\)-invariant,
and \(S_n\) is transitive on the rank-\((m-q)\) targets. Thus the expected load
is the same at every target. Every exact factor has \(W\) pointed
rank-\((m-q)\) occurrences, so

\[
\boxed{\mathbb E_{\pi_{\mathscr C}}Z_q=\frac W{N_q}=\lambda_q.}
\]

### 2.2 Variance/floor identity

**VALID, including endpoints and constants.** For any integer-valued \(Z\)
with \(\mathbb EZ=c+\theta\),

\[
\begin{aligned}
\mathbb E[(Z-c)(Z-c-1)]
&=\operatorname{Var}Z+(c+\theta-c)(c+\theta-c-1)\\
&=\operatorname{Var}Z-\theta(1-\theta).
\end{aligned}
\]

Applying this to each target, whose stationary laws are identical, gives

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}Q_q
=N_q\bigl(\operatorname{Var}_{\pi_{\mathscr C}}Z_q
-\theta_q(1-\theta_q)\bigr).}
\]

The formula is still exact at \(\theta_q=0\). Moreover,
\((z-c)(z-c-1)\ge0\) for every integer \(z\), proving directly that
\(\theta(1-\theta)\) is the minimum variance of an integer random variable
with mean \(c+\theta\).

The weighted identity for \(\mathcal Q_A\) follows immediately and is valid.

## 3. Covariance and component noise

Let \(M=(n-1)!/2\) be the number of unoriented wreath coordinates,
\(B=\operatorname{Cat}_m\), \(p=B/M\),
\(y_F=x_F-p\mathbf1\), and
\(\Sigma_{\mathscr C}=\mathbb E_{\pi_{\mathscr C}}y_Fy_F^{\mathsf T}\).

### 3.1 Centering, trace, and the middle kernel

**VALID.** Class invariance and transitivity on wreath coordinates give
\(\mathbb E x_F=p\mathbf1\), so \(\Sigma_{\mathscr C}\) is the actual
covariance. Pointwise,

\[
\|x_F-p\mathbf1\|^2=B-2pB+p^2M=B(1-p),
\]

and hence

\[
\boxed{\operatorname{Tr}\Sigma_{\mathscr C}=B(1-p).}
\]

Also \(A_mx_F=\mathbf1\). Incidence counting gives
\(A_m\mathbf1=(M/B)\mathbf1\), so \(A_my_F=0\) pointwise. Therefore

\[
\boxed{A_m\Sigma_{\mathscr C}=0,\qquad
\Sigma_{\mathscr C}A_m^{\mathsf T}=0.}
\]

### 3.2 Correct component-side notation and covariance identity

**VALID AFTER NOTATIONAL CORRECTION.** For the \(i\)-th overlay component,
let \(L_i\subset F\) denote its left side and set

\[
z_{F,\tau,i}=\mathbf1_{\tau L_i}-\mathbf1_{L_i}.
\]

Writing just \(z_K=\mathbf1_{\tau K}-\mathbf1_K\) is misleading if \(K\)
means the whole component, because then \(\tau K=K\). The effect also depends
on \((F,\tau)\).

A uniform child in the cell has, for independent fair signs \(\varepsilon_i\),

\[
y'=P_\tau y_F+\frac12\sum_i\varepsilon_i z_{F,\tau,i},
\qquad P_\tau=\frac{I+\tau}{2}.
\]

Thus

\[
\mathbb E[y'y'^{\mathsf T}\mid F]
=P_\tau y_Fy_F^{\mathsf T}P_\tau
+\frac14\sum_i z_{F,\tau,i}z_{F,\tau,i}^{\mathsf T}.
\]

Stationarity under the fixed kernel \(K_\tau\) proves

\[
\boxed{
\Sigma_{\mathscr C}
=P_\tau\Sigma_{\mathscr C}P_\tau
+\mathbb E_{\pi_{\mathscr C}}\frac14\sum_i z_i z_i^{\mathsf T}.}
\]

Because \(\Sigma_{\mathscr C}\) is \(S_n\)-equivariant, it commutes with
\(P_\tau\). Hence

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\frac14\sum_i z_i z_i^{\mathsf T}
=(I-P_\tau)\Sigma_{\mathscr C}.}
\]

No factor is missing.

### 3.3 Pointwise trace

**VALID FOR \(m\ge2\).** Disjointness gives
\(\|z_i\|^2=2|L_i|\), while \(\sum_i|L_i|=B\). Therefore, pointwise,

\[
\boxed{
\operatorname{Tr}\left(\frac14\sum_i z_i z_i^{\mathsf T}\right)
=\frac B2.}
\]

For \(m=1\), the unique wreath is fixed, the noise is zero, and the displayed
value \(B/2\) is false. This is why the standing qualifier matters.

**UNSUPPORTED OVERREACH.** The identity proves that the component count
\(k\), hence the conditional cube entropy \(k\log2\), does not determine the
total indicator-noise trace. It does not rule out a theorem using entropy
together with component geometry to control the distribution of that trace
among lower-shadow harmonics. The safe conclusion is that entropy or
component count **alone** supplies no such bound.

### 3.4 Johnson harmonic coefficient

**VALID AFTER DEFINING THE OMITTED SYMBOLS.** Put \(r=m-q\), let \(E_j\) be
the degree-\(j\) Johnson projector on rank-\(r\) functions, and define

\[
f_{q,j}=E_jA_ry_F,\qquad
\Delta_{i,q,j}=E_jA_rz_i,
\]

for \(0\le j\le\min(r,n-r)\). For the exact-factor component effects the
degrees \(0\) and \(1\) vanish: a component switch compares two exact
factors, and their rank-\(r\) histograms both have total mass \(W\) and point
margins \(rB\mathbf1\). The displayed equality is therefore harmless in
those degrees.

Push the covariance-noise identity through \(A_r\) and \(E_j\). The resulting
degree-\(j\) covariance is an \(S_n\)-equivariant endomorphism of the
multiplicity-one module \(S^{(n-j,j)}\), hence is scalar on that module. The
ratio of the two traces is

\[
\frac{\operatorname{Tr}((I-P_\tau)E_j)}{\dim E_j}
=\frac12\left(1-
\frac{\chi^{(n-j,j)}(\tau)}{\dim S^{(n-j,j)}}\right).
\]

The transposition character ratio is

\[
\frac{\chi^{(n-j,j)}(\tau)}{\dim S^{(n-j,j)}}
=\frac{\binom{n-j}{2}+\binom j2-j}{\binom n2}
=1-\frac{2j(n-j+1)}{n(n-1)}.
\]

Consequently

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\frac14\sum_i
 \|\Delta_{i,q,j}\|_2^2
=\frac{j(n-j+1)}{n(n-1)}
 \mathbb E_{\pi_{\mathscr C}}\|f_{q,j}\|_2^2.}
\]

The coefficient in the source is exact. The prose "component noise tracks
harmonic energy" must retain all its quantifiers: this is a stationary-class
expectation for a fixed transposition and a fixed Johnson degree, not a
pointwise or conditional identity.

### 3.5 Weighted covariance formula

**VALID AFTER DEFINING \(\beta_q\).** Incidence counting gives
\(A_r(p\mathbf1)=\lambda_q\mathbf1\), and therefore

\[
A_ry_F=\mu_q(F)-\lambda_q\mathbf1,
\qquad
Q_q(F)=\|A_ry_F\|_2^2-\beta_q.
\]

With

\[
T_A=\sum_{q\le H_A}\frac{A_{m-q}^{\mathsf T}A_{m-q}}{c_q},
\qquad
\beta_A=\sum_{q\le H_A}\frac{\beta_q}{c_q},
\]

one gets exactly

\[
\boxed{
\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A
=\operatorname{Tr}(T_A\Sigma_{\mathscr C})-\beta_A.}
\]

The source uses \(\beta_q\) without defining it; that is a formal but
necessary repair.

**OPEN / UNSUPPORTED AS A THEOREM.** The displayed \(SCOV_A\) statement is
properly labelled unproved. It is exactly equivalent to finding a class with
stationary mean \(O_A(H_A\operatorname{Cat}_m)\), but it is only a sufficient
stationary route to fixed-window overload. It is not an equivalent
reformulation of the existence of one good exact factor, MWB, or OR.

## 4. Exact cell-floor decomposition

Fix a target orbit \(p=\{S,\tau S\}\) with \(\tau S\ne S\). The sum over
\(p\) below is over one representative of each unordered moved orbit. For
each component side \(L_i\subset F\), define

\[
a_i(S)=\text{the number of occurrences of }S\text{ contributed by }L_i,
\qquad
d_{i,p}=a_i(S)-a_i(\tau S).
\]

This definition of \(a_i\), omitted in the source, is essential. Put

\[
\ell_p=\sum_i(a_i(S)+a_i(\tau S))
=\mu_q(S)+\mu_q(\tau S).
\]

The pair sum \(\ell_p\) is invariant throughout the cell, while for a child
with signs \(\varepsilon_i\) its load difference is, up to the immaterial
global sign convention,

\[
D_p(\varepsilon)=\sum_i\varepsilon_i d_{i,p}.
\]

### 4.1 Pair-floor identity

**VALID.** Let \(h(z)=(z-c_q)(z-c_q-1)\), let \(a+b=\ell\),
\(D=a-b\), and let \(\epsilon(\ell)\in\{0,1\}\) be the parity residue of
\(\ell\). Direct expansion gives

\[
\boxed{
h(a)+h(b)
=h(\lfloor\ell/2\rfloor)+h(\lceil\ell/2\rceil)
+\frac12\bigl(D^2-\epsilon(\ell)\bigr).}
\]

Applying this once to every moved target pair and treating fixed targets
separately proves exactly

\[
Q_q=J_{q,\tau}+G_{q,\tau}
\]

with the formulas in the source. The factor \(1/2\) is correct.

### 4.2 Nonnegativity and cell invariance

**VALID.** For every integer \(z\), \(h(z)\ge0\), so \(J_{q,\tau}\ge0\).
For an actual pair of integer loads, \(D_p\equiv\ell_p\pmod2\), whence
\(D_p^2\ge\epsilon(\ell_p)\), so \(G_{q,\tau}\ge0\).

For the component term,

\[
\sum_i d_{i,p}^2\equiv\sum_i d_{i,p}
\equiv\sum_i(a_i(S)+a_i(\tau S))
=\ell_p\pmod2.
\]

If \(\ell_p\) is odd, at least one \(d_{i,p}\) is odd and the sum of squares
is at least one; if \(\ell_p\) is even, nothing is subtracted. Hence
\(C_{q,\tau}\ge0\).

Fixed targets are frozen componentwise because
\(a_i(S)=a_i(\tau S)\) when \(\tau S=S\). The quantities \(\ell_p\), the
fixed-target loads, and the squares \(d_{i,p}^2\) do not change when the cell
is rebased; a rebase can only reverse signs of selected \(d_{i,p}\). Therefore
\(J_{q,\tau}\) and \(C_{q,\tau}\) are constant throughout the intrinsic cell.

### 4.3 Fair averaging and stationarity

**VALID.** Independent fair signs give

\[
\mathbb E_\varepsilon D_p(\varepsilon)^2=\sum_i d_{i,p}^2.
\]

Thus, pointwise as a function of the base factor,

\[
\boxed{(K_\tau Q_q)(F)=J_{q,\tau}(F)+C_{q,\tau}(F).}
\]

Stationarity under every fixed \(K_\tau\) then yields

\[
\boxed{
\mathbb E Q_q=\mathbb E J_{q,\tau}+\mathbb E C_{q,\tau},
\qquad
\mathbb E G_{q,\tau}=\mathbb E C_{q,\tau}.}
\]

These identities expose two nonnegative class parameters but do not bound
them. Calling them an "obstruction" is acceptable as route terminology, not
as an independently proved lower bound on every class.

## 5. Finite-state variational characterization

### 5.1 Exact duality

**VALID.** Here \(h\) ranges over all real functions on the finite state
space and \(\pi\) over probability laws. Since the kernel is symmetric, its
stationary laws are precisely mixtures of uniform laws on communicating
classes. Hence

\[
\inf_{\pi K=\pi}\mathbb E_\pi\mathcal Q_A
=\min_{\mathscr C}\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A
=\Theta_A.
\]

For any stationary \(\pi\) and any \(h\),

\[
\min_F[\mathcal Q_A(F)+(I-K)h(F)]
\le \mathbb E_\pi\mathcal Q_A,
\]

which gives weak duality. On each class, the right side of

\[
(I-K)h=\mathbb E_{\pi_{\mathscr C}}\mathcal Q_A-\mathcal Q_A
\]

has class mean zero. Self-adjointness and irreducibility imply that it lies
in the range of \(I-K\). Solve separately on every class, with arbitrary
additive constants. Then the bracket is the class mean at every state, giving
the reverse inequality. Therefore

\[
\boxed{
\Theta_A
=\inf_{\pi K=\pi}\mathbb E_\pi\mathcal Q_A
=\sup_h\min_F[\mathcal Q_A(F)+(I-K)h(F)].}
\]

The sign convention is correct; replacing \(h\) by \(-h\) would give the
equivalent convention with \(K-I\).

For a fixed numerical bound \(R_m\), this says

\[
\Theta_A\le R_m
\quad\Longleftrightarrow\quad
\text{for every }h\text{ there exists }F=F(h,m)
\text{ with }
\mathcal Q_A(F)+(I-K)h(F)\le R_m.
\]

The same constant, fixed \(A\), and sufficiently-large-\(m\) quantifiers must
be retained when \(R_m=O_A(H_A\operatorname{Cat}_m)\).

### 5.2 Comparison with existence and local minima

Let

- \(S_A\): some communicating class has uniform mean at most \(R_m\);
- \(E_A\): some exact factor has energy at most \(R_m\);
- \(LM_A\): every transposition-component-cut local minimum has energy at
  most \(R_m\).

Then

\[
S_A\Longrightarrow E_A,
\qquad
LM_A\Longrightarrow E_A.
\]

The first implication takes a point no larger than its class average. For the
second, strict descent stays inside a finite communicating class and
terminates at a local minimum.

**CORRECTED SCOPE.** Thus the stationary condition is stronger than
one-good-factor existence in the one-way implication sense. No converse is
proved for exact wreath factors, and strict non-equivalence inside the exact
system has not been exhibited. The one-cell cost pattern \((0,L)\), with
\(L>2R_m\), already shows that the converse does not follow from finite-state
cell formalism alone: it has a zero-cost state but stationary mean
\(L/2>R_m\).

**UNSUPPORTED / CORRECTED.** No implication \(S_A\Rightarrow LM_A\) or
\(LM_A\Rightarrow S_A\) has been proved for exact wreath factors. The source's
claim that the stationary criterion is "strictly stronger" than the
positive-cut/local-minimum lemma should be deleted.

Even the abstract cell formalism separates them. Two disconnected uniform
two-point cells with costs \((0,0)\) and \((L,L)\), where \(L>R_m\), satisfy
\(S_A\) but fail \(LM_A\) in the high cell. One uniform two-point cell with
costs \((0,L)\), where \(L>2R_m\), satisfies \(LM_A\), while its only
stationary mean is \(L/2>R_m\) and violates \(S_A\). These examples are not claimed
to be realizable by exact wreath factors; they prove that no comparison follows
from finite-state projection/duality alone.

The safe scope statement is: \(SCOV_A\) implies existence of a low exact
factor, while \(SCOV_A\) and \(LM_A\) are presently incomparable sufficient
routes.

## 6. Linear invariants, parity, and congruence floors

### 6.1 Signed-lattice statement

**VALID WITH SCOPE.** The cited signed-lattice surjectivity says that a linear
additive (including modular) functional annihilating the unrestricted signed
middle-preserving shadow image factors through the point-margin quotients.
Every exact factor has the same rank-\(r\) point margins,
\(r\operatorname{Cat}_m\mathbf1\). Thus such a functional cannot separate
exact factors.

This only concerns additive functionals on the unrestricted signed lattice.
It says nothing about nonlinear invariants or invariants surviving only on
the support-feasible graph of legal component switches. The source states
this limitation correctly.

### 6.2 The \(m=4\) parity-flip certificate

**VALID, conditional on the displayed rows belonging to the archived exact
factor as stated.** For \(n=9\), rotate an order to begin with \(1\). Reversal
reverses eight symbols and has sign \((-1)^{\binom82}=+1\), so permutation
parity is well-defined on an unoriented wreath. Define factor parity by

\[
\Xi(F)=\sum_{C\in F}\chi(C)\pmod2.
\]

For \(\tau=(3\,9)\), applying \(\tau\) to the three old rows gives the three
new rows (the second and third after reversal). Independently listing the
nine middle windows of each old row gives

\[
\begin{array}{c|lllllllll}
O_1&1247&2467&4679&3679&3689&3589&1358&1258&1245\\
O_2&1379&2379&2679&2569&2568&4568&1458&1348&1347\\
O_3&1467&3467&2367&2356&2358&2589&1589&1489&1479.
\end{array}
\]

These 27 sets are distinct. Applying \(\tau\) shows that their union is
\(\tau\)-invariant. The nonfixed pairings are

\[
\begin{gathered}
4679\leftrightarrow3467,\quad
1358\leftrightarrow1589,\quad
2679\leftrightarrow2367,\quad
2569\leftrightarrow2356,\\
1348\leftrightarrow1489,\quad
1347\leftrightarrow1479,\quad
2358\leftrightarrow2589,
\end{gathered}
\]

and all remaining listed windows are fixed. Hence this is a closed
three-by-three block of the overlay.

The numbers of fixed middle windows in the three old rows are respectively
\(7,5,1\). A one-by-one overlay component would force equality of the entire
middle supports of an old row and a member of
\(\{\tau O_1,\tau O_2,\tau O_3\}\). The distinct fixed-window counts first
force the corresponding progenitor indices to agree, while each old row has
an explicit moved window whose image lies in another row, so no row support is
itself \(\tau\)-invariant. Thus there is no one-by-one component. Since every
component is balanced and the two sides have size three, the closed overlay is
connected.

A coordinate transposition reverses wreath parity, so switching this
size-three component changes \(\Xi(F)\) by \(3=1\pmod2\). Independently, the
three displayed old representatives have inversion counts \(10,14,10\), so
the source's assertion that they are even (and their transposition images
odd) is correct. Cyclic-order parity is therefore not a heat-class invariant.

### 6.3 Coset variance and parity endpoints

**VALID AFTER CHANGING EQUALITY LANGUAGE TO A SHARP LOWER BOUND.** Suppose a
fixed-target load throughout a class lies in \(a+d\mathbb Z\), and let \(u<v\)
be consecutive allowed values with \(u\le\lambda_q\le v\). Every allowed
value \(z\) satisfies \((z-u)(z-v)\ge0\), so expectation gives

\[
\boxed{\operatorname{Var}Z_q
\ge(\lambda_q-u)(v-\lambda_q).}
\]

Equality holds exactly when the law is supported on the bracketing pair
\(\{u,v\}\) (apart from a degenerate endpoint).

For a parity coset, if \(c_q\) is allowed, the sharp forced variance excess
above \(\theta_q(1-\theta_q)\) is **at least** \(\theta_q\); if \(c_q\) is
forbidden, it is **at least** \(1-\theta_q\). The source's word "is" is only
correct for the extremal two-point law. At \(\theta_q=0\), the two cases give
respectively zero and one per target, so the endpoint is consistent.

If \(\min(\theta_q,1-\theta_q)\ge\delta>0\) and \(q\le A\sqrt m\), then
\(N_q=\Theta_A(W)\), and the forced rank energy is
\(\Omega_{A,\delta}(W)\), whereas

\[
H_A\operatorname{Cat}_m=O_A(W/\sqrt m).
\]

**SCOPE CORRECTION.** A congruence producing one high-energy class is not
decisive against \(SCOV_A\), whose quantifier asks for *some* low class, and
does not refute MWB or OR. It would refute an every-class drift theorem. To
refute \(SCOV_A\), the obstruction would have to force the minimum class mean,
equivalently every candidate class, above the target scale.

## 7. Conditional rigid-orbit theorem

**VALID FOR \(m\ge2\), WITH ITS HYPOTHESIS STILL UNPROVED.** Suppose the
ownership overlay of \(F\) and \(\tau F\) is connected for every
transposition \(\tau\). Then every \(\tau\)-cell at \(F\) is exactly
\(\{F,\tau F\}\).

At an orbit point \(\sigma F\), the overlay for \(\tau\) is the \(\sigma\)-image
of the overlay of \(F\) with
\((\sigma^{-1}\tau\sigma)F\). The conjugate is again a transposition, so this
overlay is connected too. Therefore no heat step from the orbit \(S_nF\)
leaves that orbit. Conversely, opposite-side choices along transposition
words reach every orbit element. The orbit is exactly one communicating
class (with repetitions removed if \(F\) has a nontrivial coordinate
stabilizer).

Since \(\mathcal Q_A\) is invariant under coordinate relabelling,

\[
\boxed{
\mathbb E_{\pi_{S_nF}}\mathcal Q_A=\mathcal Q_A(F).}
\]

A fixed-\(A\) asymptotic family of such factors with energy above the claimed
scale would refute every-class drift and would supply high cut-local minima.
As the source correctly notes, it would not disprove the existence of a
different low class. Neither existence nor high energy of such a rigid family
is proved.

## 8. Final classification and implication scope

The decisive claims classify as follows.

1. **VALID:** \(F\cap\tau F=\varnothing\) for \(m\ge2\), with the fixed-window
   and dihedral-stabilizer proof above.
2. **VALID:** intrinsic \(\tau\)-cells, exactly \(2^k\) children,
   \(K_\tau^2=K_\tau=K_\tau^*\).
3. **VALID:** each communicating class is a union of complete cells, its
   unique stationary law is uniform and invariant under every \(K_\tau\), and
   the invariant-algebra intersection formula holds.
4. **CORRECTED:** replace "class transitivity" by class \(S_n\)-invariance plus
   target transitivity.
5. **VALID:** exact variance/floor formula, including \(\theta_q=0\).
6. **VALID AFTER NOTATION REPAIR:** covariance decomposition and fixed trace;
   use component sides \(L_i\), define \(A_r\), and retain \(m\ge2\).
7. **VALID AFTER DEFINITION:** the harmonic coefficient
   \(\kappa_j=j(n-j+1)/(n(n-1))\) has no missing factor.
8. **VALID AFTER DEFINITION:** weighted covariance energy; define
   \(\beta_q=N_q\theta_q(1-\theta_q)\).
9. **VALID AFTER DEFINITION:** \(J/C/G\) cell floors and all factors of
   \(1/2\); define \(a_i\), moved unordered pairs, and component sides.
10. **VALID:** finite-state stationary/Poisson duality, with \(h\) ranging over
    all real state functions and the same asymptotic constants preserved.
11. **UNSUPPORTED:** \(SCOV_A\) itself; the source correctly labels it
    unproved.
12. **UNSUPPORTED AS STATED:** entropy can never control alignment. Only the
    insufficiency of entropy/component count alone is proved.
13. **UNSUPPORTED AS STATED:** \(SCOV_A\) is strictly stronger than \(LM_A\).
    No implication either way is proved for exact factors.
14. **CORRECTED:** \(SCOV_A\) implies one-good-factor existence, but the
    converse and strict separation within the exact system are unproved.
15. **VALID WITH CORRECTION:** congruence variance is a lower bound, with the
    endpoint and fractional-part qualifications above.
16. **VALID:** the displayed \(m=4\) component flips factor parity, so parity is
    not a heat invariant.
17. **VALID CONDITIONALLY:** the rigid-orbit theorem; the required asymptotic
    family remains unproved.
18. **CORRECTED SCOPE:** \(SCOV_A\) is exact for the proposed stationary-class
    selection route and sufficient for fixed-window overload. It is not known
    necessary for fixed-window overload, MWB, or OR. A single high class only
    refutes universal every-class assertions.

Thus the source's mathematical core is retained, but its final conclusion
must read: the stationary route ends at the open class-covariance selection
problem \(SCOV_A\); the identities in the report do not solve it, and they do
not establish that no entropy-based or other structurally enriched argument
could solve it.
