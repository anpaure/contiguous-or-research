# Gaussian-annulus multi-seed overlays: exact floor variance, diffuse heat, and the carrier-local statewise obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
 \qquad 0<a<b<\infty.
\tag{0.1}
\]

This note tests exact two- and multi-seed component switching directly on
the two signed Gaussian annulus.  The conclusions are as follows.

1. There is an exact baseline-corrected component formula.  For an
   independent physical component choice with exact uniform first
   marginals, the expected floor excess at a target is

   \[
   \boxed{
   \sum_K \mathbb E Y_K(Y_K-1)
   +c_q+\tau_q^2-\sum_Kp_K^2,}
   \tag{0.2}
   \]

   where \(Y_K\) is the number of copies of that target contributed by
   component \(K\), \(p_K=\mathbb EY_K\), and

   \[
   \lambda_q={W\over \binom{2m}{m-q}}=c_q+\tau_q,
   \qquad c_q=\lfloor\lambda_q\rfloor.
   \tag{0.3}
   \]

   Thus ordinary component variance is the wrong scale: it must equal the
   integer floor variance to additive \(o(W)\) after summing
   \(\Theta(\sqrt m)\) depths.

2. Formula (0.2) is rigid.  Its value is zero exactly when the total load
   is always \(c_q\) or \(c_q+1\).  Under independent component choices,
   at most one component may then be nonconstant at that target.  Hence a
   successful product heat bath must provide \(c_q\) deterministic units
   and at most one residual floor coin at almost every target-depth cell.

   For fair binary component choices this has a sharper exact form.  If
   \(a_{K,\alpha}\) is the difference between the two component-side
   contributions at target cell \(\alpha\), then the rounding excess above
   the convex floor envelope is

   \[
   \boxed{
    {1\over4}\left(
       \sum_Ka_{K,\alpha}^2
       -\mathbf1_{\{\sum_Ka_{K,\alpha}\ \mathrm{odd}\}}
    \right).}
   \tag{0.3a}
   \]

   It vanishes only when every \(a_K=0\), or exactly one \(a_K=\pm1\).
   Together with the convex mean-transport term, this is a positive,
   checkable physical contraction theorem.

3. Diffuse component heat is quantitatively impossible even when the
   components are genuine exact-factor trades and change orbit masses.  If
   the mean is uniform and

   \[
                 \max_K\mathbb EY_K=\rho_m=o(1)
   \tag{0.4}
   \]

   at every signed annular target, then

   \[
   \boxed{
   \mathbb E\mathcal Q_{a,b}
   \ge \bigl(2(b-a)e^{-b^2}+o_{a,b}(1)\bigr)W\sqrt m.}
   \tag{0.5}
   \]

   This is an excess above the exact integer floor, not raw centered
   energy.

4. The complete coordinate-orbit fractional braid of
   `MATH_THEOREM_GAUSSIAN_SHARED_PREFIX_PACKET_FRACTIONAL_BRAID_20260726.md`
   has precisely this diffuse pathology under independent packet rounding.
   Its expected floor excess has the exact expression

   \[
   \boxed{
   2\sum_{q=q_0}^{H}{N_q\over c_q}
      \bigl(c_q+\tau_q^2-\vartheta_m\lambda_q\bigr),
   \qquad
   \vartheta_m={W\over (2m)!\,2m},}
   \tag{0.6}
   \]

   and is \(\Theta_{a,b}(W\sqrt m)\).  Thus exact fractional first
   marginals do not supply the floor covariance needed for rounding.

5. There is also a genuinely statewise obstruction.  In any row-matched
   multi-seed overlay in which every alternative row differs from a fixed
   row only by reordering one common carrier block of width \(s_m\), every
   integral component child satisfies

   \[
   \boxed{
   \left|\mathcal D_{a,b}(F')-\mathcal D_{a,b}(F_0)\right|
   \le {2s_m(H-q_0+1)\over m}\,W.}
   \tag{0.7}
   \]

   Here \(\mathcal D_{a,b}\) is the raw two-sign floor deficiency.  Hence
   every \(s_m=o(\sqrt m)\) carrier-local cube is statewise incapable of
   repairing an \(\Omega(W)\) annular defect.  This applies to the audited
   orbit-mass-changing suspended-pentagon bank, whose active carrier width
   is nine.  It is unrelated-seed and non-relabeling, so (0.7) is not the
   old single-relabeling heat obstruction.

The shared-prefix braid escapes (0.7) because its moving frame is nonlocal
on the full packet.  What it does not yet supply is an exact owner-component
resolution with the strong negative cross-component covariance forced by
(0.2)--(0.5).  That is the precise surviving physical condition.

## 1. The exact annular floor polynomial

For a signed depth \((q,\sigma)\), where \(\sigma\in\{-,+\}\), put

\[
 \mathcal X_q^- =\binom{[2m]}{m-q},\qquad
 \mathcal X_q^+ =\binom{[2m]}{m+q},\qquad
 N_q=|\mathcal X_q^-|=|\mathcal X_q^+|.
\tag{1.1}
\]

An exact owner-cycle factor partitions all \(W\) middle owners into safe
cyclic routes.  Let \(\mu_{q,T}^{\sigma}\) be the number of signed
depth-\(q\) route windows with target \(T\).  Then

\[
 \sum_{T\in\mathcal X_q^\sigma}\mu_{q,T}^{\sigma}=W.
\tag{1.2}
\]

Write \(\lambda_q=c_q+\tau_q\) as in (0.3), with
\(0\le\tau_q<1\), and use \(w_q=1/c_q\).  Define the two-sign
floor-correct annular energy

\[
 \mathcal Q_{a,b}(F)
 =\sum_{q=q_0}^{H}\sum_{\sigma=\pm}w_q
   \left(
    \sum_T(\mu_{q,T}^{\sigma}-\lambda_q)^2
    -N_q\tau_q(1-\tau_q)
   \right).
\tag{1.3}
\]

The mass identity (1.2) gives the exact integer polynomial

\[
 \boxed{
 \mathcal Q_{a,b}(F)
 =\sum_{q=q_0}^{H}\sum_{\sigma=\pm}{1\over c_q}
   \sum_T
   (\mu_{q,T}^{\sigma}-c_q)
   (\mu_{q,T}^{\sigma}-c_q-1).}
\tag{1.4}
\]

Every summand in (1.4) is a nonnegative even integer before multiplication
by \(1/c_q\).  The raw two-sign floor deficiency is

\[
 \mathcal D_{a,b}(F)
 =\sum_{q=q_0}^{H}\sum_{\sigma=\pm}\sum_T
       (c_q-\mu_{q,T}^{\sigma})_+.
\tag{1.5}
\]

If \(d=(c_q-\mu)_+\), then

\[
 (\mu-c_q)(\mu-c_q-1)=d(d+1)\ge2d.
\]

Consequently

\[
 2\sum_{q,\sigma}{1\over c_q}
       \sum_T(c_q-\mu_{q,T}^{\sigma})_+
 \le \mathcal Q_{a,b}(F).
\tag{1.6}
\]

Uniformly on the fixed annulus,

\[
 \lambda_q
 =\prod_{j=1}^{q}{m+j\over m-j+1},
 \qquad
 \log\lambda_q={q^2\over m}+O_b(m^{-1/2}).
\tag{1.7}
\]

Thus \(c_q=O_b(1)\), and (1.6) shows

\[
                 \mathcal Q_{a,b}=o(W)
       \quad\Longrightarrow\quad
                 \mathcal D_{a,b}=o(W).
\tag{1.8}
\]

The subtraction in (1.3) is large.  Riemann summation in (1.7) gives

\[
\begin{aligned}
 {1\over W\sqrt m}
 \sum_{q=q_0}^{H}\sum_{\sigma=\pm}
 {N_q\tau_q(1-\tau_q)\over c_q}
 \longrightarrow{}&
 2\int_a^b e^{-x^2}
 {\{e^{x^2}\}(1-\{e^{x^2}\})
  \over\lfloor e^{x^2}\rfloor}\,dx.
\end{aligned}
\tag{1.9}
\]

The integral is positive: its integrand vanishes only at the finitely many
points in \([a,b]\) for which \(e^{x^2}\) is an integer.  Therefore the
unavoidable centered floor variance is \(\Theta_{a,b}(W\sqrt m)\), while
the allowed excess in (1.8) is only \(o(W)\).

There is an equivalent collision interpretation.  Put

\[
 C_{q}^{\sigma}(F)=\sum_T
          \mu_{q,T}^{\sigma}(\mu_{q,T}^{\sigma}-1).
\tag{1.10}
\]

Then

\[
 \sum_T(\mu-c_q)(\mu-c_q-1)
 =C_q^\sigma(F)-2c_qW+N_qc_q(c_q+1).
\tag{1.11}
\]

Hence floor-energy contraction is exactly the removal of excess ordered
target collisions.  For a shared-prefix braid packet, its \(2m\) targets
at each fixed signed depth \(q<m\) are distinct, so all collisions in a
packet factor are interpacket collisions.

To verify the last assertion, the lower target records the cyclic block of
\(q\) empty coordinate pairs.  Equality of two such targets forces their
starts to agree modulo \(m\).  Starts separated by \(m\) have complementary
orientations on each of the \(m-q>0\) surviving pairs, so their targets are
different.  The upper assertion follows by complement-antipodality.

## 2. Physical multi-seed owner components

Let \(F^{(1)},\ldots,F^{(r)}\) be arbitrary exact owner-cycle factors on
the same middle-owner set.  Form the owner incidence hypergraph whose
vertices are all routes, tagged by their seed, and whose hyperedge at an
owner \(X\) joins the unique route of each seed containing \(X\).

For a connected component \(K\), let \(\Omega_K\) be its owner set.  For
every seed \(i\), the seed-\(i\) routes in \(K\) partition exactly
\(\Omega_K\).  Thus selecting one complete seed side \(i_K\) in every
component gives another exact integral owner factor.  This is a physical
multi-seed component overlay; no fractional row is selected.

Choose the labels \(i_K\) independently, with arbitrary component-dependent
probabilities.  For a target cell

\[
                         \alpha=(q,\sigma,T),
\]

let \(Y_{K,\alpha}\) be the nonnegative integer number of occurrences of
\(T\) contributed by the selected side of \(K\), and put

\[
 p_{K,\alpha}=\mathbb EY_{K,\alpha},\qquad
 \bar\mu_\alpha=\sum_Kp_{K,\alpha}.
\tag{2.1}
\]

Every realization is exact.  Independence is used only to evaluate its
floor energy.

### Theorem 2.1 (exact baseline-corrected multi-seed drift)

For the random exact child \(F_{\bf i}\),

\[
\boxed{
 \mathbb E\mathcal Q_{a,b}(F_{\bf i})
 =\sum_{\alpha}{1\over c_{q(\alpha)}}
 \left[
  (\bar\mu_\alpha-\lambda_{q(\alpha)})^2
  +\sum_K\operatorname {Var}(Y_{K,\alpha})
  -\tau_{q(\alpha)}(1-\tau_{q(\alpha)})
 \right].}
\tag{2.2}
\]

For any fixed reference child \(F_0\), the exact drift is

\[
\boxed{
\begin{aligned}
 \mathbb E\mathcal Q_{a,b}(F_{\bf i})-
 \mathcal Q_{a,b}(F_0)
 =\sum_\alpha{1\over c_{q(\alpha)}}
 \bigg[&
  (\bar\mu_\alpha-\lambda_{q(\alpha)})^2
  -(\mu_\alpha^{F_0}-\lambda_{q(\alpha)})^2\\
 &+\sum_K\operatorname {Var}(Y_{K,\alpha})
 \bigg].
\end{aligned}}
\tag{2.3}
\]

In particular, if the right side of (2.2) is \(R_m\), some physical
integral component child satisfies

\[
                         \mathcal Q_{a,b}\le R_m.
\tag{2.4}
\]

Thus (2.2) is a positive baseline-corrected rounding theorem whenever
\(R_m=o(W)\).

#### Proof

For every cell,

\[
 \mathbb E(\mu_\alpha-\lambda_q)^2
 =(\bar\mu_\alpha-\lambda_q)^2
   +\sum_K\operatorname {Var}(Y_{K,\alpha}),
\]

because the component labels are independent.  Substitute this in (1.3)
to obtain (2.2).  Subtract the deterministic instance of (1.3) for
\(F_0\) to obtain (2.3).  Finally, at least one realization is no larger
than its expectation. \(\square\)

No relabeling assumption appears in Theorem 2.1.  In particular, the
component profiles may have nonzero projection on every chosen target-orbit
census.

## 2A. Convex floor transport plus the binary rounding reservoir

The preceding identity has a useful decomposition which separates the
quality of the mean profile from the cost of rounding that mean.  For a
real number \(x\), let

\[
 \Phi_q(x)=(x-\lambda_q)^2+\{x\}(1-\{x\}).
\tag{2A.1}
\]

On every interval \([j,j+1]\), this is the affine interpolation of
\((j-\lambda_q)^2\) and \((j+1-\lambda_q)^2\).  Hence \(\Phi_q\) is
convex, and

\[
                         \Phi_q(\lambda_q)=\tau_q(1-\tau_q).
\tag{2A.2}
\]

For the mean load vector \(\bar\mu\), define

\[
 \mathcal T_{a,b}(\bar\mu)
 =\sum_\alpha {1\over c_{q(\alpha)}}
   \left(\Phi_{q(\alpha)}(\bar\mu_\alpha)
              -\Phi_{q(\alpha)}(\lambda_{q(\alpha)})\right).
\tag{2A.3}
\]

Although an individual summand can be negative, the total at each fixed
sign and depth is nonnegative.  Indeed, every child has total target mass
\(W\), so

\[
                         \sum_T\bar\mu_{q,T}^\sigma=N_q\lambda_q,
\]

and Jensen's inequality gives

\[
                         \mathcal T_{a,b}(\bar\mu)\ge0.
\tag{2A.4}
\]

For an integer-valued random variable \(Z\) of mean \(x\), one has

\[
                         \operatorname {Var}Z
                         \ge\{x\}(1-\{x\}),
\tag{2A.5}
\]

because the minimum second moment at fixed mean is attained on the two
adjacent integers bracketing \(x\).  Define the rounding reservoir

\[
 \mathcal R_{a,b}
 =\sum_\alpha {1\over c_{q(\alpha)}}
  \left(
    \operatorname {Var}\mu_\alpha
    -\{\bar\mu_\alpha\}(1-\{\bar\mu_\alpha\})
  \right)\ge0.
\tag{2A.6}
\]

### Theorem 2A.1 (exact convex-envelope floor decomposition)

For any random exact-factor-valued law, with no independence assumption,

\[
 \boxed{
                 \mathbb E\mathcal Q_{a,b}
                 =\mathcal T_{a,b}(\bar\mu)
                  +\mathcal R_{a,b}.}
\tag{2A.7}
\]

Consequently, if a physical component law satisfies

\[
                         \mathcal T_{a,b}=o(W),
                         \qquad
                         \mathcal R_{a,b}=o(W),
\tag{2A.8}
\]

then some exact integral child has

\[
                         \mathcal Q_{a,b}=o(W),
                         \qquad
                         \mathcal D_{a,b}=o(W).
\tag{2A.9}
\]

#### Proof

At one cell,

\[
\begin{aligned}
 \mathbb E(\mu-\lambda_q)^2-\tau_q(1-\tau_q)
 ={}&\Phi_q(\bar\mu)-\Phi_q(\lambda_q)\\
 &+\operatorname {Var}\mu
   -\{\bar\mu\}(1-\{\bar\mu\}).
\end{aligned}
\]

Sum this identity.  Equations (2A.4)--(2A.6) prove nonnegativity, and
(1.6) proves the deficiency conclusion. \(\square\)

The equality case in the transport term is also exact.  If
\(0<\tau_q<1\), equality in Jensen at a fixed sign and depth holds exactly
when every \(\bar\mu_{q,T}^\sigma\) lies in the one affine segment
\([c_q,c_q+1]\).  If \(\tau_q=0\), it holds exactly when every mean is
\(c_q\).

Now specialize to a fair binary physical overlay.  At a target cell write

\[
 Y_{K,\alpha}
 ={y_{K,\alpha}^-+y_{K,\alpha}^+\over2}
  +{\varepsilon_K\over2}a_{K,\alpha},
 \qquad
 a_{K,\alpha}=y_{K,\alpha}^+-y_{K,\alpha}^-,
\tag{2A.10}
\]

where the component signs are independent and fair.  Then

\[
 \operatorname {Var}\mu_\alpha={1\over4}\sum_Ka_{K,\alpha}^2,
\tag{2A.11}
\]

while \(\bar\mu_\alpha\) is integral or half-integral according as
\(\sum_Ka_{K,\alpha}\) is even or odd.  Therefore the cellwise summand of
the rounding reservoir is exactly (0.3a).

The parity identity

\[
                         \sum_Ka_K^2\equiv\sum_Ka_K\pmod2
\]

shows that a nonzero value in (0.3a) is at least \(1/2\).  It is zero
exactly in the following two cases:

\[
 \begin{array}{ll}
 \text{even case:}& a_K=0\quad\text{for every }K,\\[2mm]
 \text{odd case:}& \text{one }a_K=+1\text{ or }-1,
                   \text{ and all other }a_L=0.
 \end{array}
\tag{2A.12}
\]

We obtain a concrete positive theorem.

### Corollary 2A.2 (binary one-unit contraction theorem)

Suppose a fair two-seed or binary multi-seed physical overlay has

\[
                         \mathcal T_{a,b}(\bar\mu)=o(W),
\tag{2A.13}
\]

and (2A.12) fails on only \(o(W)\) signed target-depth cells, with the sum
of \(\sum_Ka_{K,\alpha}^2\) over those exceptional cells equal to
\(o(W)\).  Then some exact component child satisfies (2A.9).

Conversely, for fair binary independent choices,
\(\mathbb E\mathcal Q_{a,b}=o(W)\) forces
\(\mathcal T_{a,b}=o(W)\), and (2A.12) fails on only \(o(W)\) cells.

#### Proof

Equations (0.3a) and (2A.12) give
\(\mathcal R_{a,b}=o(W)\); apply Theorem 2A.1.  Conversely both terms in
(2A.7) are nonnegative, and every failed cell costs at least
\(1/(2c_q)=\Omega_b(1)\) in \(\mathcal R_{a,b}\). \(\square\)

Thus a binary component bank may change orbit masses on many components,
but it contracts to the floor only if each literal target sees essentially
no switch or one unit switch.  Several small switches at the same target
are already a positive floor-reservoir loss; their signs do not cancel in
fair heat.

## 3. Exact floor rigidity and the diffuse-product obstruction

Assume now that the first marginal is exactly uniform at a cell:

\[
                         \bar\mu_\alpha=\lambda_q.
\tag{3.1}
\]

Since an integer-valued nonnegative variable satisfies

\[
 \operatorname {Var}Y
 =\mathbb EY(Y-1)+\mathbb EY-(\mathbb EY)^2,
\tag{3.2}
\]

equation (2.2) gives the promised per-cell identity

\[
\boxed{
 \mathbb E[(\mu_\alpha-c_q)(\mu_\alpha-c_q-1)]
 =\sum_K\mathbb EY_{K,\alpha}(Y_{K,\alpha}-1)
  +c_q+\tau_q^2-\sum_Kp_{K,\alpha}^2.}
\tag{3.3}
\]

### Proposition 3.1 (one-residual-component rigidity)

The quantity in (3.3) is zero if and only if

\[
                       \mu_\alpha\in\{c_q,c_q+1\}
                       \quad\hbox{almost surely}.
\tag{3.4}
\]

Under independent component choices, (3.4) implies that at most one
\(Y_{K,\alpha}\) is nonconstant.  The sum of all deterministic component
contributions and the smaller value of the possible nonconstant component
is exactly \(c_q\); that component's two possible values are consecutive.

If every component contributes either zero or one copy, this says exactly:
there are \(c_q\) deterministic carriers, at most one residual Bernoulli
carrier of mean \(\tau_q\), and no other carrier.

#### Proof

The polynomial \((z-c_q)(z-c_q-1)\) is nonnegative on the integers and
vanishes exactly at \(z=c_q,c_q+1\).  This proves the first assertion.

For the second, the support of a sum of independent finite integer-valued
variables is the Minkowski sum of their supports.  If two summands were
nonconstant, the total support would have diameter at least two, contrary
to (3.4).  The unique possible nonconstant summand must itself have support
inside two consecutive integers.  The remaining statements follow by
matching the two possible total values. \(\square\)

The same argument is quantitatively stable at the output level:

\[
 \mathbb P\{\mu_\alpha\notin\{c_q,c_q+1\}\}
 \le {1\over2}
 \mathbb E[(\mu_\alpha-c_q)(\mu_\alpha-c_q-1)].
\tag{3.5}
\]

Thus an \(o(W)\) expected aggregate floor energy forces floor/ceiling loads
outside only \(o(W)\) weighted target-depth cells.

### Theorem 3.2 (diffuse exact-component heat no-go)

Suppose (3.1) holds for every signed annular target and

\[
                 p_{K,\alpha}\le\rho_m=o(1)
                 \quad\hbox{for all }K,\alpha.
\tag{3.6}
\]

Then (0.5) holds.

#### Proof

The factorial term in (3.3) is nonnegative, while

\[
 \sum_Kp_{K,\alpha}^2
 \le\rho_m\sum_Kp_{K,\alpha}
 =\rho_m\lambda_q.
\tag{3.7}
\]

Consequently the weighted expected excess at one target is at least

\[
 {c_q+\tau_q^2-\rho_m\lambda_q\over c_q}=1-o_{a,b}(1),
\tag{3.8}
\]

uniformly on the annulus, because \(1\le c_q\le O_b(1)\) and
\(\lambda_q\le e^{b^2}+o_b(1)\).  Also

\[
 N_q={W\over\lambda_q}
 \ge(e^{-b^2}-o_b(1))W.
\tag{3.9}
\]

There are two signs and

\[
 H-q_0+1=(b-a)\sqrt m+O(1)
\]

depths.  Summing (3.8)--(3.9) proves (0.5). \(\square\)

The theorem is about genuine integral outputs: every realization is an
exact component child.  It does not say that every child has large energy;
it says that diffuse independent heat cannot be the baseline-corrected
rounding argument.  A rare globally coordinated child is not excluded.

## 4. Exact application to the shared-prefix fractional braid

Let \(\mathscr O=\{P_g:g\in S_{2m}\}\) be the complete labelled orbit of
the explicit shared-prefix packet and put

\[
                         \vartheta_m={W\over(2m)!\,2m}.
\tag{4.1}
\]

The fractional theorem assigns weight \(\vartheta_m\) to every labelled
packet.  Its most direct product rounding selects each \(P_g\)
independently with Bernoulli probability \(\vartheta_m\).  This rounding
does not enforce owner disjointness; the point here is that it already
fails the annular floor test before owner conflicts are repaired.

By the packet-distinctness proved after (1.11), a fixed packet contains a
fixed signed depth-\(q\) target at most once.  The exact orbit count is

\[
 \sum_{g\in S_{2m}} b_{q,T}^{\sigma}(P_g)
 =2m\,{(2m)!\over N_q}.
\tag{4.2}
\]

Hence the rounded load at \(T\) has

\[
 \sum_gp_g=\lambda_q,qquad
 \sum_gp_g^2=\vartheta_m\lambda_q,qquad
 \sum_g\mathbb EY_g(Y_g-1)=0.
\tag{4.3}
\]

Substitution in (3.3), followed by summation over the two signs, gives
the exact formula (0.6).

Moreover, uniformly for \(q=x\sqrt m+O(1)\), (1.7) gives

\[
 {N_q\over W}=e^{-x^2}+O_{a,b}(m^{-1/2}).
\tag{4.4}
\]

Since \(\vartheta_m\to0\), Riemann summation yields

\[
\boxed{
 {\mathbb E\mathcal Q_{a,b}^{\rm ind}\over W\sqrt m}
 \longrightarrow
 2\int_a^b e^{-x^2}
 \left(
  1+{\{e^{x^2}\}^2\over\lfloor e^{x^2}\rfloor}
 \right)dx.}
\tag{4.5}
\]

The constant in (4.5) is strictly positive and is at least
\(2(b-a)e^{-b^2}\).  Thus the exact fractional braid solves first
marginals and collar sharing, but its independent packet heat has
Poisson-scale target collisions rather than floor-scale collisions.

Conditioning on exact owner disjointness is not analyzed by (4.5), because
that conditioning creates long-range dependence.  Precisely such dependence
would have to provide the negative covariance described in Section 6.

## 5. A statewise carrier-local obstruction for arbitrary many seeds

We now give a different obstruction which applies to every component
signing, not merely its product average.

Consider exact packet factors whose rows have cyclic length \(2m\).  Fix a
reference factor \(F_0\), and assume all seeds have a common row indexing
compatible with ownership components.  Say that the overlay is
*row-matched \(s_m\)-carrier-local* if, for every indexed row and every
seed option, its cyclic coordinate word agrees with the reference outside
one common cyclic interval of at most \(s_m\) positions and uses the same
coordinate set inside that interval.  The order inside may be arbitrary.

Every component may choose any of the seed sides.  The definition ensures
that the resulting row is still compared row by row with its reference;
the component sizes and the number of seeds are unrestricted.

### Lemma 5.1 (two-boundary count)

For one row and one fixed depth, at most \(2s_m\) cyclic lower windows
change their target, and at most \(2s_m\) cyclic upper windows change their
target.

#### Proof

A cyclic interval has two boundary cuts.  If neither cut lies in the
carrier block, it contains either the whole block or none of it.  Its set
is then unchanged because the exterior order and the set of carrier
coordinates are fixed.  Each boundary lies in the block for at most
\(s_m\) starts.  The same argument applies to lower intersections and,
by complementing, to upper unions. \(\square\)

### Theorem 5.2 (statewise multi-seed annular locality bound)

Every integral component child \(F'\) of a row-matched
\(s_m\)-carrier-local overlay satisfies (0.7).

#### Proof

Changing one target occurrence deletes one histogram unit and inserts one,
so Lemma 5.1 gives

\[
 {1\over2}\|\mu_{q}^{\sigma,F'}-\mu_q^{\sigma,F_0}\|_1
 \le2s_m\,{W\over2m}={s_mW\over m}
\tag{5.1}
\]

for each sign and depth.  If integer vectors \(x,y\) have the same total
mass, then

\[
 \left|\sum_T(c-x_T)_+-\sum_T(c-y_T)_+\right|
 \le {1\over2}\|x-y\|_1.
\tag{5.2}
\]

Indeed,

\[
 \sum_T(c-x_T)_+
 ={1\over2}\left(\sum_T|x_T-c|+Nc-\sum_Tx_T\right),
\]

and the equal-mass terms cancel.  Sum (5.1)--(5.2) over the two signs and
\(H-q_0+1\) depths to obtain (0.7). \(\square\)

In particular,

\[
 s_m=o(\sqrt m)
 \quad\Longrightarrow\quad
 \sup_{F'}
 |\mathcal D_{a,b}(F')-\mathcal D_{a,b}(F_0)|=o(W).
\tag{5.3}
\]

The same conclusion holds after pushing every load vector to any fixed
target-orbit partition, because push-forward is an \(\ell^1\) contraction.
Thus changing orbit masses does not defeat (5.3).

The suspended-pentagon two-seed bank audited in
`MATH_ATTACK_K_TWO_SEED_GROWING_FRINGE_TRADE_20260726.md` is a literal
example.  Its five-row components change a complete shadow histogram and
an automorphism-orbit census, so it is genuinely unrelated-seed and
orbit-mass-changing.  Its active carrier nevertheless has width nine,
independent of the formal fringe scale.  Therefore all states of that
component cube change the Gaussian-annular floor deficiency by only

\[
                         O_{a,b}(W/\sqrt m)=o(W).
\tag{5.4}
\]

The same proof in the odd wreath normalization replaces \(2m\) by
\(2m+1\) and is unchanged asymptotically.

The shared-prefix braid is qualitatively different: its successive product
atoms may use unrelated frames, and comparison of two transverse packets
need not be supported on an \(o(\sqrt m)\) carrier.  Thus Theorem 5.2 does
not close that nonlocal route.

## 6. The exact surviving covariance condition

Allow the component choices to be correlated.  The exact analogue of
(2.2) is

\[
\begin{aligned}
 \mathbb E\mathcal Q_{a,b}
 =\sum_\alpha{1\over c_q}\bigg[&
  (\bar\mu_\alpha-\lambda_q)^2
  +\sum_K\operatorname {Var}(Y_{K,\alpha})\\
 &+2\sum_{K<L}\operatorname {Cov}
       (Y_{K,\alpha},Y_{L,\alpha})
  -\tau_q(1-\tau_q)
 \bigg].
\end{aligned}
\tag{6.1}
\]

This is the required joined-owner cross-component condition.  In the
diffuse regime (3.6), integer-valuedness gives

\[
 \sum_K\operatorname {Var}(Y_{K,\alpha})
 \ge\sum_K(p_{K,\alpha}-p_{K,\alpha}^2)
 \ge(1-\rho_m)\lambda_q.
\tag{6.2}
\]

Therefore a correlated diffuse rounding with exact uniform mean and
\(o(W)\) total floor excess must provide, in weighted aggregate,

\[
\boxed{
 2\sum_{q,\sigma,T}{1\over c_q}
   \sum_{K<L}\operatorname {Cov}(Y_{K,q,T}^{\sigma},Y_{L,q,T}^{\sigma})
 =-\Theta_{a,b}(W\sqrt m),}
\tag{6.3}
\]

with the more precise target value obtained by replacing the right side
cellwise by

\[
 \tau_q(1-\tau_q)-\sum_K\operatorname {Var}(Y_{K,q,T}^{\sigma}).
\tag{6.4}
\]

Equivalently, a product component law may avoid (6.3) only through the
one-residual-component floor skeleton of Proposition 3.1.  Ordinary small
component size, orbit-mass motion, and uniform first marginals imply none
of these properties.

This identifies the next exact constructive statement:

> Construct two or more exact nonlocal shared-prefix packet factors and a
> common owner-component resolution such that either (i) almost every
> signed annular target has the one-residual-component floor skeleton, or
> (ii) an integral correlated component transversal realizes (6.3)--(6.4)
> while leaving only \(o(W)\) owners.

The correlation must act on literal targets, not merely on packet frames or
projected orbit masses.

## 7. Proved boundary

Proved here:

1. the exact two-sign Gaussian floor polynomial and collision form;
2. the exact physical multi-seed component drift (2.2)--(2.3);
3. the one-residual-component equality classification;
4. the quantitative \(\Theta(W\sqrt m)\) diffuse-component heat no-go;
5. the exact \(\Theta(W\sqrt m)\) independent-rounding calculation for the
   shared-prefix fractional braid;
6. the statewise \(s_m=o(\sqrt m)\) carrier-local obstruction for arbitrary
   many unrelated seeds; and
7. the exact negative covariance required of a nonlocal correlated
   resolution.

Not proved:

1. no exact integral shared-prefix packet factor or owner-disjoint near
   resolution is constructed;
2. deterministic discrepancy could in principle find an exceptionally
   good child hidden inside a diffuse product distribution;
3. no correlated integral component law satisfying (6.3) is constructed;
4. the theorem does not close the nonlocal braid route; and
5. coefficient one is not claimed.

The lane is therefore sharply divided.  Orbit-changing local exact trades
are statewise too weak, while nonlocal diffuse heat pays Poisson rather than
floor variance.  The surviving object is a nonlocal exact owner resolution
with literal-target floor covariance.
