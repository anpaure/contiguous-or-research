# The post-collar gap matrix: a surviving constant mode and the exact limit of compensation

Date: 2026-07-27

Scope: the equality-resolved consecutive-profile boundary in the
vertex-compensated promotion-frame process. All statements are exact
finite combinatorics. No probabilistic independence, computation, or
scalar all-order ansatz is used.

## 0. Verdict

Refining profile order by the unresolved base gap, the exposed shore,
the ordered endpoint string, and arbitrary further finite state does not
repair the post-collar positive \(+1\) profile shift.

For \(H\le k<m\), put \(g=m-k\). The exact ordered-continuation
operator on the one-shore consecutive face is

\[
 \boxed{
 (\mathsf K_g f)(\omega)
 =\alpha_g{1\over g}\sum_{x\in G(\omega)}
       f(\omega\mathbin{\frown}x),
 \qquad
 \alpha_g={r-m+g-1\over r-m+g}.}
 \tag{0.1}
\]

Here \(G(\omega)\) is the unresolved base gap, of size \(g\), and
\(\omega\mathbin{\frown}x\) is the child obtained by exposing \(x\) at
the active endpoint. Thus

\[
                         \mathsf K_g\mathbf 1
                         =\alpha_g\mathbf 1.             \tag{0.2}
\]

The normalized operator \(\alpha_g^{-1}\mathsf K_g\) is literally the
sampling-without-replacement Markov kernel. In particular, the
post-collar transition has a positive constant mode. Its cumulative
attenuation is only

\[
 \boxed{
 \prod_{g=1}^{m-H}\alpha_g={r-m\over r-H},}              \tag{0.3}
\]

which is polynomial, not exponential, in the promotion-frame regime.

Let a positive gap/two-shore energy use arbitrary state-dependent
weights and suppose it is required to absorb this upward boundary over
a time horizon \({\cal T}\) with contraction factor \(\rho<1\). The
mean weights on the consecutive face necessarily satisfy

\[
 \bar w_{g-1}\ge{{\cal T}\alpha_g\over\rho}\bar w_g.
 \tag{0.4}
\]

Consequently

\[
 \bar w_0\ge \bar w_{m-H}
 \left({{\cal T}\over\rho}\right)^{m-H}{r-m\over r-H}.
 \tag{0.5}
\]

For

\[
 {\cal T}=(1/2+o(1))m\log m
 \tag{0.6}
\]

and the exact terminal consecutive-profile mass

\[
                         \log\Gamma_m=-m\log m+O(m),     \tag{0.7}
\]

equation (0.5) gives

\[
 \log(\bar w_0\Gamma_m)
 \ge \log\bar w_{m-H}+(1+o(1))m\log\log m.              \tag{0.8}
\]

Thus no positive diagonal matrix energy, and more generally no positive
Banach-lattice norm whose state refinement retains (0.1), can absorb the
post-\(H\) \(+1\) shift and have finite physical initialization. The
obstruction is not caused by forgetting the gap or the two shores: it is
the invariant constant mode on the one-shore face. Adding other shore
states or other positive transitions cannot remove it.

Vertex compensation does not automatically cancel this mode. For every
live physical resource set \(S\), the exact compensated hazard is

\[
 \Lambda_t(S)={|S|\over r}-\nu_tJ_t(S),\qquad
 J_t(S)=\sum_e(|e\cap S|-1)_+.                             \tag{0.9}
\]

Hence the product-density-normalized survivor has drift

\[
 \boxed{
 \mathcal L_t\bigl(I_Su_t^{-|S|}\bigr)
 =\nu_tJ_t(S)I_Su_t^{-|S|}\ge0.}                          \tag{0.10}
\]

The compensation coins cancel the one-vertex marginals exactly, but
they leave the common-edge correction with positive sign. Therefore a
successful post-collar argument must prove an additional signed
edge-event coboundary, or must terminate and quarantine before entering
the post-\(H\) face. There is no remaining positive-weight choice to
try.

## 1. Ordered continuation states

Fix a root owner \(X\) and one of the two orientations. A rooted frame
has the form

\[
 x_1x_2\cdots x_m a_1a_2\cdots a_H.                      \tag{1.1}
\]

After the first \(H\) consecutive shifts, the collar
\(A=\{a_1,\ldots,a_H\}\), with its relevant endpoint order, is fully
exposed. Every further consecutive owner identifies one new base
coordinate at the active endpoint. At profile order \(k\ge H\), the
state may therefore be written

\[
 \omega=(X,A,\sigma;\,x_1,\ldots,x_k;\,G),
 \qquad |G|=m-k=g,                                       \tag{1.2}
\]

where \(\sigma\in\{+,-\}\) is the shore and \(G\) is the unresolved
base gap. We allow \(\omega\) to carry any additional equality type,
row type, or history label. Those labels play no role below because we
restrict to one fixed compatible fibre.

The \(g\) legal ordered continuations are

\[
 \omega\mathbin{\frown}x
 =(X,A,\sigma;x_1,\ldots,x_k,x;G\setminus\{x\}),
 \qquad x\in G.                                          \tag{1.3}
\]

Let \(\Omega_g\) be the orbit of these states under coordinate
relabeling, with the uniform invariant probability \(\pi_g\). More
generally, after a compatible equivariant state refinement, define
\(\pi_{g-1}\) to be the push-forward of \(\pi_g\) under one uniform
continuation. Define

\[
 (\mathsf P_gf)(\omega)
 ={1\over g}\sum_{x\in G(\omega)}f(\omega\mathbin{\frown}x).
 \tag{1.4}
\]

### Lemma 1.1 (Markov consistency)

For every \(g\ge1\),

\[
 \mathsf P_g\mathbf1=\mathbf1,
 \qquad
 \int_{\Omega_g}\mathsf P_gf\,d\pi_g
 =\int_{\Omega_{g-1}}f\,d\pi_{g-1}.                     \tag{1.5}
\]

#### Proof

The first identity is immediate. A uniform ordered partial exposure,
followed by a uniform choice from its unresolved gap, is a uniform
ordered partial exposure one step longer. Equivalently, before further
refinement the incidence graph between \(\Omega_g\) and
\(\Omega_{g-1}\) is biregular under the coordinate-relabeling action,
so double counting its directed incidences proves the second identity.
After an equivariant refinement the second identity holds by the
push-forward definition of \(\pi_{g-1}\); on each transitive child orbit
this push-forward is uniform. \(\square\)

There is a stronger identity which is important below. Every ordered
child has a unique parent. Let

\[
 p_g:\Omega_{g-1}\longrightarrow\Omega_g
 \tag{1.6}
\]

delete its last exposed coordinate, and define the pullback

\[
 (\mathsf U_gh)(\eta)=h(p_g(\eta)).
 \tag{1.7}
\]

Then

\[
 \boxed{\mathsf P_g\mathsf U_g=I.}                       \tag{1.8}
\]

Thus \(\mathsf P_g\) preserves not only constants but every
parent-measurable function. In particular, if \(h\) has global mean
zero, then \(f=\mathsf U_gh\) also has global mean zero while
\(\mathsf P_gf=h\) with no contraction. The operator

\[
 \mathsf Q_g:=\mathsf U_g\mathsf P_g                     \tag{1.9}
\]

is a projection on functions on \(\Omega_{g-1}\), and

\[
 f=\mathsf Q_gf+(I-\mathsf Q_g)f,\qquad
 \mathsf P_g(I-\mathsf Q_g)f=0.                          \tag{1.10}
\]

Only the fibre-centred second summand is killed by one continuation
step.

## 2. The exact physical multiplier

Let \(\Gamma_k\) denote the normalized physical mass of one prescribed
consecutive profile at order \(k\). The audited exact formula for
\(H\le k\le m\) is

\[
 \Gamma_k
 ={2(r-k)(m-k)!(m-H)!\over r(m!)^2}.                     \tag{2.1}
\]

Therefore, for one prescribed child,

\[
 {\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over m-k}
 ={\alpha_g\over g}.                                     \tag{2.2}
\]

There are exactly \(g=m-k\) coordinate continuations (1.3). Reversing
the child sum therefore gives (0.1):

\[
                         \mathsf K_g=\alpha_g\mathsf P_g.
 \tag{2.3}
\]

This calculation is the promised gap-indexed transition matrix. It is
not an order-only estimate: every matrix entry is the prescribed-child
factor in (2.2), and the row is indexed by the actual unresolved gap.

Before collar saturation the corresponding prescribed-child ratio has
two factorial denominators:

\[
 {\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over(m-k)^2},\qquad k<H.             \tag{2.4}
\]

Since there are \(m-k\) admissible continuations, its constant-mode
multiplier is

\[
 {r-k-1\over r-k}{1\over m-k}=\Theta(1/m)                \tag{2.5}
\]

through the collar range. At \(k=H\), one factorial denominator
disappears because the \(A\)-shore is fully exposed. Equations
(2.3)--(2.5) give an exact matrix explanation of the crossover.

Finally, (0.3) follows by telescoping:

\[
 \prod_{g=1}^{m-H}{r-m+g-1\over r-m+g}
 ={r-m\over r-H}.                                        \tag{2.6}
\]

## 3. Positive matrix energies cannot remove the constant mode

We formulate the result in the dual form actually used by a positive
energy argument. Let \(w_g:\Omega_g\to(0,\infty)\) be arbitrary. A
time-integrated absorption of the positive boundary generated by
\(\mathsf K_g\) requires

\[
 {\cal T}\mathsf K_g^*w_g\le\rho w_{g-1},
 \qquad0<\rho<1,                                         \tag{3.1}
\]

where the adjoint is taken with respect to \(\pi_g,\pi_{g-1}\). This is
the coefficientwise condition ensuring that the contribution entering
every child state is paid by at most a \(\rho\)-fraction of that child's
energy. It allows completely nonuniform, gap-dependent, shore-dependent,
and history-dependent weights.

### Theorem 3.1 (mean-weight recurrence)

Put

\[
 \bar w_g=\int_{\Omega_g}w_g\,d\pi_g.
 \tag{3.2}
\]

Then (3.1) implies (0.4), and hence (0.5).

#### Proof

Integrate (3.1) against \(\pi_{g-1}\). By adjointness, (1.5), and
(2.3),

\[
 \begin{aligned}
 \int_{\Omega_{g-1}}\mathsf K_g^*w_g\,d\pi_{g-1}
 &=\int_{\Omega_g}w_g\mathsf K_g\mathbf1\,d\pi_g\\
 &=\alpha_g\bar w_g.
 \end{aligned}                                           \tag{3.3}
\]

Thus \({\cal T}\alpha_g\bar w_g\le\rho\bar w_{g-1}\),
which is (0.4). Iteration and (2.6) prove (0.5). \(\square\)

This proof also shows why breaking coordinate symmetry in the weights
does not help. Averaging any feasible system over the relabeling group
preserves (3.1), preserves its initialized physical mean, and produces
the scalar means in (3.2). Equivalently, the constant mode is a
positive left and right Perron mode of the invariant continuation
kernel. Identity (1.8) is stronger: ordered continuation has a full
inherited, noncontracting parent-measurable subspace.

### Corollary 3.2 (positive Banach-lattice form)

Let \(\|\cdot\|_g\) be any family of Banach-lattice norms on functions on
\(\Omega_g\). Then

\[
 \|\mathsf K_g\|_{g-1\to g}
 \ge\alpha_g{\|\mathbf1\|_g\over\|\mathbf1\|_{g-1}},      \tag{3.4}
\]

with the quotient reversed if the operator convention is reversed.
Consequently a product of the post-collar operators has lower norm at
least the telescoping constant-mode factor (2.6), times the endpoint
normalization of \(\mathbf1\).

#### Proof

Apply the operator to the positive constant vector and use (0.2). The
product assertion follows by iteration. \(\square\)

The statement remains true in a full two-shore/gap state space. Its
positive operator dominates the restriction to the one-shore face
\(q=0\) used above. A positive operator cannot cancel an invariant
positive subkernel. This is the precise scope in which the scalar
obstruction survives every multidimensional positive refinement.

## 4. Initialization divergence

At \(k=m\), (2.1) and Stirling give

\[
                         \log\Gamma_m=-m\log m+O(m).      \tag{4.1}
\]

Combining Theorem 3.1 with (4.1) yields

\[
\begin{aligned}
 \log(\bar w_0\Gamma_m)
 &\ge \log\bar w_{m-H}
 +(m-H)\log({\cal T}/\rho)
 +\log{r-m\over r-H}
 -m\log m+O(m).
\end{aligned}                                            \tag{4.2}
\]

For (0.6), \(H=o(m)\), and the promotion-frame values of \(r\), the
right side is

\[
 \log\bar w_{m-H}+(1+o(1))m\log\log m.                   \tag{4.3}
\]

Any energy retaining the pair/triple levels has
\(\log\bar w_{m-H}=-o(m\log\log m)\). More strongly, applying the
audited pre-collar recurrence (2.5) from any fixed normalized low order
forces

\[
 \log\bar w_{m-H}\ge\Omega(H\log\log m).                 \tag{4.4}
\]

Thus (4.3) diverges. Notice that this proof used the full gap matrix
and only then projected onto its invariant mean; it did not assume at
the outset that weights depend on order alone.

## 5. What compensation cancels, exactly

In the compensated process, every active edge rings at rate
\(\nu_t=(r\Delta_t)^{-1}\), and the independent compensation clock at
an active vertex \(y\) has rate

\[
 \chi_t(y)={\Delta_t-d_t(y)\over r\Delta_t}.
 \tag{5.1}
\]

For a live finite resource set \(S\), the rate of an event deleting at
least one member of \(S\) is

\[
\begin{aligned}
 \Lambda_t(S)
 &=\nu_t\left|\bigcup_{y\in S}\mathcal E_t(y)\right|
   +\sum_{y\in S}\chi_t(y)\\
 &={|S|\over r}-\nu_t
 \left(\sum_{y\in S}d_t(y)
 -\left|\bigcup_{y\in S}\mathcal E_t(y)\right|\right).
\end{aligned}                                            \tag{5.2}
\]

The parenthesis equals

\[
 J_t(S)=\sum_e(|e\cap S|-1)_+.                            \tag{5.3}
\]

Let \(I_S\) be the indicator that every member of \(S\) is alive and
let \(u_t=e^{-t/r}\). While \(S\) is live,

\[
 \mathcal L_tI_S=-\Lambda_t(S)I_S,
 \qquad {d\over dt}u_t^{-|S|}={|S|\over r}u_t^{-|S|}.
 \tag{5.4}
\]

Equations (5.2)--(5.4) prove (0.10).

In particular, for every live \(S\), each of the \(d_t(S)\) edges in
its common link contributes \(|S|-1\), and hence

\[
                         J_t(S)\ge(|S|-1)d_t(S).          \tag{5.5}
\]

There is no negative coin term available to cancel (5.5): the coin
rates have already been used exactly in obtaining the marginal term
\(|S|/r\).

There is a signed identity inside the edge correction:

\[
 \boxed{
 J_t(S)=
 \sum_{\ell=2}^{|S|}(-1)^\ell
 \sum_{T\in\binom S\ell}d_t(T).}                         \tag{5.6}
\]

Indeed,

\[
 (j-1)_+=\sum_{\ell=2}^{j}(-1)^\ell\binom j\ell
 \qquad(j\ge0),                                         \tag{5.7}
\]

and summing (5.7) over active edges gives (5.6). Therefore cancellation
of the post-collar mode is possible only through a genuinely signed
Möbius/coboundary argument which keeps the full intersection state.
Replacing (5.6) by a positive child majorant restores (0.1) and is
subject to Theorem 3.1.

## 6. Exact proved boundary and smallest replacement lemma

Proved here:

1. the exact gap-indexed post-collar matrix (0.1);
2. its invariant Markov constant mode (0.2);
3. the telescoping survival factor (0.3);
4. the mean-weight obstruction for arbitrary positive state-dependent
   gap/two-shore weights;
5. the corresponding positive Banach-lattice obstruction; and
6. the exact statement that compensation cancels marginal hazards but
   not common-edge overlap.

Not proved here:

1. a signed trajectory estimate exploiting (5.6);
2. a dynamic terminal quarantine at \(k=H\); or
3. coefficient one.

The smallest exact post-collar replacement is fibrewise, not a global
mean condition. Let \(B_{g-1}(t,\eta)\) be the signed,
equality-resolved source on \(\Omega_{g-1}\) left after the first-order
reference drift is subtracted. Its inherited part is determined by

\[
 \boxed{
 R_g(t,\omega):=(\mathsf P_gB_{g-1})(t,\omega)
 ={1\over g}\sum_{x\in G(\omega)}
 B_{g-1}(t,\omega\mathbin{\frown}x).}                    \tag{6.1}
\]

The strong fibrewise coboundary statement

\[
 \boxed{R_g(t,\omega)=0
 \quad\hbox{for every }g,t,\omega}                       \tag{FCB}
\]

annihilates every \(+1\) continuation exactly. Equivalently,

\[
 B_{g-1}=(I-\mathsf Q_g)C_{g-1}                          \tag{6.2}
\]

for some fibre function \(C_{g-1}\). A global mean-zero condition is
insufficient: if \(B_{g-1}=\mathsf U_gh\) with
\(\int h\,d\pi_g=0\), then its global mean vanishes but \(R_g=h\).

For an approximate statement, one must pay the complete chronological
propagation of the residuals, not merely their global means. In the
static kernel majorant define

\[
 \mathsf P_{g:j}
 :=\mathsf P_g\mathsf P_{g-1}\cdots
   \mathsf P_{g-j+1},
 \qquad
 A_{g:j}:=\prod_{i=0}^{j-1}\alpha_{g-i}.                 \tag{6.3}
\]

An exact sufficient quantitative replacement for FCB is

\[
\boxed{
 \int_0^{\cal T}
 \sum_{g=1}^{m-H}\sum_{j=1}^{g}
 {({\cal T}-t)^j\over j!}\,
 A_{g:j}\,
 \bigl\|\mathsf P_{g:j}B_{g-j}(t)\bigr\|_{L^1(\pi_g)}
 \,dt=o(1)}
 \tag{FCM}
\]

in marked-incidence normalization. This is precisely the
time-ordered Duhamel mass of all propagated signed sources for the
triangular kernel \(\mathsf K_g=\alpha_g\mathsf P_g\). For a
time-dependent equality-resolved kernel, the displayed powers are
replaced by the corresponding chronological integrals. The simpler
one-step bound

\[
 \int_0^{\cal T}\sum_g
 \|\mathsf P_gB_{g-1}(t)\|_{L^1(\pi_g)}\,dt=o(1)          \tag{6.4}
\]

is necessary to control immediate inheritance but is not, by itself,
sufficient over the long horizon unless its error is small enough to
absorb the remaining Duhamel amplification.

If no signed statement such as FCB or FCM is available, the sharp
positive alternative is to stop at \(k=H\) and pay the terminal
profiles from their time-zero physical mass. Propagating any positive
hierarchy past that boundary re-enters the obstruction proved above.

## 7. Adversarial scope audit

Three limitations are essential.

First, Theorem 3.1 applies only when the equality-resolved generator
contains the post-collar continuations with nonnegative coefficients,
or is upper-bounded by a positive operator which contains them. It does
not rule out a signed generator identity which cancels their constant
projection—and, more generally, their full parent-measurable
projection—before positive parts are taken.

Second, the proof does not assume that every refined child orbit is
uniform. The measure used in (1.5) is the actual push-forward of a
uniform parent and a uniform legal coordinate continuation. Thus
splitting states by histories cannot evade (3.3); it merely splits the
same conserved mass among child fibres.

Third, (0.10) rules out cancellation supplied automatically by the
independent compensation clocks. It does not rule out cancellation
between different edge-event terms. Such a cancellation would have to
use the alternating identity (5.6), and proving the fibrewise
coboundary FCB, or the propagated residual estimate FCM, is the exact
unproved replacement.

Finally, no claim is made that globally mean-zero modes contract.
Identity (1.8) gives explicit mean-zero modes which are transported
isometrically. All contraction claims in this note are restricted to
the fibre-centred kernel of \(\mathsf P_g\).
