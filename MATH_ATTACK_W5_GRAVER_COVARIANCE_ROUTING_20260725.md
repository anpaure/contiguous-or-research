# Fifth-wave W: exact mixed-sign covariance routing on Graver cubes

## Verdict

Standard negative dependence is neither available nor needed.  Given any two
exact wreath factors, the connected components of their middle-owner overlap
graph form a genuine cube of exact factors.  On this cube, the optimum among
**all** probability laws preserving the midpoint wreath marginals is attained
by the uniform law on one antipodal pair of exact hybrid factors.  Its
covariance is rank one and has mixed signs chosen by a simultaneous
multidepth vector-discrepancy problem.

The optimum has an exact decomposition into two nonnegative terms:

1. an immutable pair-sum profile floor; and
2. a parity-corrected Graver signing slack.

This gives a complete covariance-routing theorem on every fixed Graver face.
It also gives an exact obstruction: if either term is large, no
midpoint-preserving dependent law on that face can have low pair-collision
excess.

The asymptotic wreath theorem remains open.  No argument below proves that a
useful pair of factors has a small pair-sum floor or admits a parity-sharp
common signing through all depths \(q\le A\sqrt m\).  The surviving positive
statement is a precise averaged Graver-discrepancy lemma.  A scale
\(o(W/\sqrt m)\) bound on its parity slack would imply the required
\(o(W)\) fixed-window excess.  Connected overlays, shadow-orthogonal
components, and invariant trade subspaces are exact obstructions to broader
versions.

Everything below remains integral inside one exact middle factor.  Ordinary
cycles of the owner-overlap graph are not declared to be physical trades;
the primitive exact moves are its whole connected components.

## 1. Exact setup and normalization

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
B=\frac Wn=\operatorname{Cat}_m.
\]

Let \(M=A_m\) be the middle-set versus unoriented-wreath incidence matrix.
An exact factor is an indicator vector

\[
x_F\in\{0,1\}^{\mathscr W_m},\qquad Mx_F=\mathbf1.
\]

For \(1\le q<m\), let \(A_q\) denote incidence of wreaths with their cyclic
\((m-q)\)-intervals, and put

\[
N_q=\binom n{m-q},\qquad
\lambda_q=\frac W{N_q}=a_q+\theta_q,
\]

where \(a_q=\lfloor\lambda_q\rfloor\) and
\(0\le\theta_q<1\).  The depth-\(q\) load vector of \(F\) is

\[
\mu_q^F=A_qx_F.
\]

Every exact factor has total load

\[
\sum_S\mu_q^F(S)=W=N_q\lambda_q.
\]

Use the undoubled pair-collision excess

\[
R_q(F)
=\frac12\sum_S
(\mu_q^F(S)-a_q)(\mu_q^F(S)-a_q-1).
\tag{1.1}
\]

Thus \(R_q=P_q-P_q^{\min}\ge0\).  The full floor-energy convention in
several earlier reports is \(Q_q=2R_q\).

Fix arbitrary weights \(\omega_q>0\) and a depth cutoff \(H<m\).  Define

\[
\Phi_H(F)=\sum_{q\le H}\omega_qR_q(F),
\tag{1.2}
\]

\[
Tx=(\sqrt{\omega_q}A_qx)_{q\le H},\qquad
u=(\sqrt{\omega_q}\lambda_q\mathbf1)_{q\le H},
\tag{1.3}
\]

and the integer quantization floor

\[
J_H=\sum_{q\le H}\omega_qN_q\theta_q(1-\theta_q).
\tag{1.4}
\]

Using the fixed total-load identity to cancel the linear term gives

\[
\boxed{
\Phi_H(F)=\frac12\bigl(\|Tx_F-u\|_2^2-J_H\bigr).
}
\tag{1.5}
\]

For fixed-window MWB, take

\[
H=H_A=\lceil A\sqrt m\rceil,
\qquad \omega_q=\frac1{a_q}.
\tag{1.6}
\]

Then \(a_q=O_A(1)\), and \(\Phi_H=o(W)\) is sufficient for fixed-window
unlabelled MWB.  The sharper factor scale is

\[
O_A(HB)=O_A(W/\sqrt m).
\tag{1.7}
\]

## 2. Ownership components are precisely the squarefree Graver moves

Let \(F,G\) be exact factors.  Cancel their common wreaths and form the
bipartite owner-overlap multigraph \(\mathcal O(F,G)\):

- the left vertices are \(F\setminus G\);
- the right vertices are \(G\setminus F\);
- every middle set joins its unique owner in \(F\) to its unique owner in
  \(G\).

Every vertex has degree \(n\).  In particular, every connected component has
the same number of left and right wreaths.

For a component \(K_i\), write its sides as \(F_i,G_i\), and define

\[
g_i=\mathbf1_{G_i}-\mathbf1_{F_i}.
\tag{2.1}
\]

### Theorem 2.1 — exact Graver cube

The following statements hold.

1. \(Mg_i=0\).
2. Every choice of one complete side in every component is an exact factor.
3. These are all exact factors whose support is contained in \(F\cup G\).
4. Every \(g_i\) is conformally indecomposable in \(\ker_{\mathbb Z}M\),
   hence is a squarefree Graver element.
5. The component decomposition is the unique conformal Graver decomposition
   of \(x_G-x_F\).

#### Proof

Inside one component, its two sides own exactly the same set of middle
vertices, proving \(Mg_i=0\).  Choosing either side therefore preserves
every middle equation, and independent choices across components give an
exact factor.

Conversely, on every overlap edge the two incident wreath indicators must
sum to one.  Along a connected bipartite component this forces one constant
choice on the left and the complementary choice on the right.  Hence there
are exactly two choices per component.

If \(0\ne h\sqsubseteq g_i\) and \(Mh=0\), the row equation at each overlap
edge forces its two incident coefficients to occur together.  Connectedness
propagates this through all of \(K_i\), so \(h=g_i\).  The same propagation
shows uniqueness of the conformal decomposition. \(\square\)

Put

\[
\bar x=\frac{x_F+x_G}{2}.
\]

With a fixed orientation of every component, all cube corners are

\[
x(s)=\bar x+\frac12\sum_{i=1}^r s_i g_i,
\qquad s\in\{-1,1\}^r.
\tag{2.2}
\]

The owner-overlap graph is an \(n\)-regular bipartite multigraph and hence
can be decomposed into graph-theoretic alternating cycles.  Those cycles are
not, in general, separately flippable physical trades: selecting one wreath
forces all its other ownership incidences, and the move propagates through
the whole connected component.  The component, not an arbitrary graph
cycle, is the primitive exact move.

## 3. Exact diamond identity

Put

\[
V_i=Tg_i.
\tag{3.1}
\]

For \(I\subseteq[r]\), let \(H_I,H_{I^c}\) be the complementary hybrid
factors obtained by reversing the component signs on \(I\).  Then

\[
x_F+x_G=x_{H_I}+x_{H_{I^c}}.
\tag{3.2}
\]

### Theorem 3.1 — exact target-weighted diamond law

\[
\boxed{
\Phi_H(F)+\Phi_H(G)
-\Phi_H(H_I)-\Phi_H(H_{I^c})
=
\left\langle
\sum_{i\in I}V_i,
\sum_{j\notin I}V_j
\right\rangle.
}
\tag{3.3}
\]

#### Proof

Let \(V_I=\sum_{i\in I}V_i\) and
\(V_{I^c}=\sum_{i\notin I}V_i\).  The two endpoint deviations from the
common midpoint are
\(\pm(V_I+V_{I^c})/2\); the hybrid deviations are
\(\pm(V_I-V_{I^c})/2\).  The common midpoint term, linear term, and integer
floor cancel between the two pairs.  Finally,

\[
\frac14\bigl(\|V_I+V_{I^c}\|^2
-\|V_I-V_{I^c}\|^2\bigr)
=\langle V_I,V_{I^c}\rangle.
\]

This is (3.3). \(\square\)

Thus a positive cross inner product is cancelled exactly by replacing the
endpoint coin with the hybrid coin.  Expected undoubled excess drops by

\[
\frac12\langle V_I,V_{I^c}\rangle.
\tag{3.4}
\]

The replacement preserves every wreath marginal, not merely the middle
equations.  If the cross inner product is nonnegative separately at every
depth, it weakly improves every depth simultaneously.  Positivity only after
weighted summation proves improvement of the aggregate objective, not
coordinatewise improvement at every rank.

## 4. Complete covariance optimization on one Graver cube

Let \(s\) be a random sign vector on the cube.  Preserving the midpoint
wreath marginals is equivalent to

\[
\mathbb Es_i=0\qquad(1\le i\le r).
\tag{4.1}
\]

Put

\[
v=T\bar x-u,\qquad G_{ij}=\langle V_i,V_j\rangle,
\qquad \mathcal R=\mathbb E[ss^{\mathsf T}].
\]

Expansion of (1.5) gives

\[
\boxed{
\mathbb E\Phi_H(x(s))
=\frac12(\|v\|^2-J_H)
+\frac18\operatorname{tr}(G\mathcal R).
}
\tag{4.2}
\]

### Theorem 4.1 — antipodal optimality

\[
\boxed{
\inf_{\mathbb Es=0}\mathbb E\Phi_H(x(s))
=\frac12(\|v\|^2-J_H)
+\frac18\min_{\varepsilon\in\{\pm1\}^r}
\left\|\sum_i\varepsilon_iV_i\right\|^2.
}
\tag{4.3}
\]

The optimum is attained by the uniform law on the two antipodal exact
factors \(x(\varepsilon),x(-\varepsilon)\).

#### Proof

Any sign law can be symmetrized under \(s\mapsto-s\).  This makes every
sign mean zero and leaves \(ss^{\mathsf T}\) unchanged.  Consequently the
possible second-moment matrices are exactly

\[
\operatorname{conv}\{\varepsilon\varepsilon^{\mathsf T}:
\varepsilon\in\{\pm1\}^r\}.
\]

The objective in (4.2) is linear in that matrix, so a minimum occurs at one
rank-one extreme point. \(\square\)

For the optimizing law, if

\[
h=\sum_i\varepsilon_i g_i,
\]

then the wreath-indicator covariance is

\[
\boxed{\operatorname{Cov}(x)=\frac14hh^{\mathsf T}.}
\tag{4.4}
\]

This covariance has both signs: wreaths with equal signs in \(h\) are
positively correlated, and opposite signs are negatively correlated.  It is
the exact target-specific covariance selected by the common multidepth
signing.  Higher entropy or higher support cannot improve the quadratic
objective on this fixed face.

If uniform global wreath marginals are desired, average this antipodal law
over all coordinate relabelings.  The resulting law is still supported on
exact factors, has marginal \(B/|\mathscr W_m|=1/D\) on every wreath, and
has the same expected \(\Phi_H\), since the objective is
\(S_n\)-invariant.

For two components, writing

\[
c=\langle V_1,V_2\rangle,
\]

the optimum discrepancy is

\[
\|V_1\|^2+\|V_2\|^2-2|c|.
\tag{4.5}
\]

Relative to independent fair component coins, the exact expected gain is
\(|c|/4\).  Relative to the original endpoint coin, the hybrid coin improves
exactly when \(c>0\), with expected gain \(c/2\).  These constants use
\(R_q\); they double under the convention \(Q_q=2R_q\).

## 5. Immutable pair-sum floor and parity restitution

For an integer \(z\), define

\[
e_a(z)=\frac12(z-a)(z-a-1).
\]

For a fixed nonnegative integer pair sum \(t\), put

\[
b_a(t)=\min_{r+s=t}\bigl(e_a(r)+e_a(s)\bigr),
\tag{5.1}
\]

where \(r,s\) range over nonnegative integers.

### Lemma 5.1 — exact scalar pair floor

\[
\boxed{
b_a(t)
=e_a(\lfloor t/2\rfloor)+e_a(\lceil t/2\rceil)
=\left\lfloor\frac{(t-2a-1)^2}{4}\right\rfloor.
}
\tag{5.2}
\]

If \(t-2a=2k\), then \(b_a(t)=k(k-1)\); if
\(t-2a=2k+1\), then \(b_a(t)=k^2\).

#### Proof

If \(r\ge s+2\), moving one unit from \(r\) to \(s\) changes the sum in
(5.1) by \(-(r-s-1)<0\).  Thus every minimizer is the balanced split.
Substitution gives (5.2). \(\square\)

For any antipodal cube pair, put

\[
t_{q,S}=\mu_q^{x(\varepsilon)}(S)+
\mu_q^{x(-\varepsilon)}(S)
=\mu_q^F(S)+\mu_q^G(S),
\tag{5.3}
\]

and

\[
d_{q,S}(\varepsilon)=
\mu_q^{x(\varepsilon)}(S)-
\mu_q^{x(-\varepsilon)}(S)
=\sum_i\varepsilon_i(A_qg_i)(S).
\tag{5.4}
\]

The pair sums are invariant over the whole cube, and

\[
d_{q,S}(\varepsilon)\equiv t_{q,S}\pmod2.
\tag{5.5}
\]

Let \(\epsilon(t)=\mathbf1_{\{t\text{ odd}\}}\).  Direct substitution gives

\[
e_a\left(\frac{t+d}{2}\right)
+e_a\left(\frac{t-d}{2}\right)
=b_a(t)+\frac14(d^2-\epsilon(t)).
\tag{5.6}
\]

### Theorem 5.2 — floor plus restitution decomposition

For every common signing \(\varepsilon\),

\[
\boxed{
\frac{\Phi_H(x(\varepsilon))+\Phi_H(x(-\varepsilon))}{2}
=\mathfrak B_H(F,G)+\mathfrak C_H(F,G;\varepsilon),
}
\tag{5.7}
\]

where

\[
\mathfrak B_H(F,G)
=\frac12\sum_{q\le H}\omega_q\sum_S b_{a_q}(t_{q,S})\ge0,
\tag{5.8}
\]

and

\[
\mathfrak C_H(F,G;\varepsilon)
=\frac18\sum_{q\le H}\omega_q\sum_S
\bigl(d_{q,S}(\varepsilon)^2-\epsilon(t_{q,S})\bigr)\ge0.
\tag{5.9}
\]

Therefore the exact midpoint-preserving optimum is

\[
\boxed{
\Theta_H(F,G)
=\mathfrak B_H(F,G)
+\frac18\bigl(\Delta_H(F,G)-O_H(F,G)\bigr),
}
\tag{5.10}
\]

with

\[
\Delta_H(F,G)
=\min_{\varepsilon\in\{\pm1\}^r}
\sum_{q\le H}\omega_q
\left\|A_q\sum_i\varepsilon_i g_i\right\|^2,
\tag{5.11}
\]

and

\[
O_H(F,G)
=\sum_{q\le H}\omega_q
|\{S:t_{q,S}\text{ is odd}\}|.
\tag{5.12}
\]

In particular,

\[
\boxed{\Delta_H(F,G)\ge O_H(F,G).}
\tag{5.13}
\]

The invariant floor vanishes exactly when every pair sum lies in

\[
t_{q,S}\in\{2a_q,2a_q+1,2a_q+2\}.
\tag{5.14}
\]

The restitution term vanishes exactly when one common signing satisfies

\[
|d_{q,S}|=
\begin{cases}
0,&t_{q,S}\text{ even},\\
1,&t_{q,S}\text{ odd},
\end{cases}
\tag{5.15}
\]

simultaneously for every \(q,S\).  Both terms vanish precisely when the
two antipodal exact factors are floor/ceiling balanced at every target and
depth.

For every midpoint-preserving law, not just an antipodal law, the expected
contribution at \((q,S)\) is at least \(b_{a_q}(t_{q,S})/2\).  This follows
from the minimum integer variance at mean \(t_{q,S}/2\).  Thus
\(\mathfrak B_H\) is a genuine covariance invariant of the face.

## 6. Orbit averages and exact parity descent

Fix a factor \(F\), let \(\pi\) be uniform in \(S_n\), and set

\[
\rho_q=\frac1{N_q}
|\{S:\mu_q^F(S)\text{ is odd}\}|.
\tag{6.1}
\]

Transitivity on the rank-\((m-q)\) targets gives

\[
\boxed{
\mathbb E_\pi\mathfrak B_q(F,\pi F)
=\frac12R_q(F)
+\frac{N_q}{4}
\bigl[\rho_q(1-\rho_q)-\theta_q(1-\theta_q)\bigr].
}
\tag{6.2}
\]

This is exact.  To prove it, average over \((S,\pi^{-1}S)\), which is a
uniform ordered pair of rank targets.  Equivalently, use

\[
\mathfrak B_q(F,G)
=\frac18\|\mu_q^F+\mu_q^G-2\lambda_q\mathbf1\|^2
+\frac18O_q(F,G)
-\frac{N_q}{2}\theta_q(1-\theta_q).
\tag{6.3}
\]

The linear term in the scalar identity with \(\lambda_q\) cancels only
after summing all targets and using total load \(W\); it does not vanish
coordinatewise.

Define

\[
L_q(F)
=2R_q(F)
-N_q\bigl[\rho_q(1-\rho_q)-\theta_q(1-\theta_q)\bigr].
\tag{6.4}
\]

Then

\[
\mathbb E_\pi\mathfrak B_q(F,\pi F)
=R_q(F)-\frac14L_q(F).
\tag{6.5}
\]

### Lemma 6.1 — quantitative parity gap

\[
L_q(F)\ge0,
\]

with equality exactly when \(R_q(F)=0\).  Writing
\(e_q=R_q(F)/N_q\),

\[
\boxed{
\frac{L_q(F)}{N_q}\ge
\begin{cases}
4e_q^2,&e_q\le1/4,\\
2e_q-1/4,&e_q\ge1/4.
\end{cases}}
\tag{6.6}
\]

#### Proof

Let \(k_S=\mu_q^F(S)-a_q\), and let \(o_q\) count the odd \(k_S\).
Since \(\sum_Sk_S=N_q\theta_q\),

\[
|o_q-N_q\theta_q|
\le\sum_S|\mathbf1_{\{k_S\text{ odd}\}}-k_S|
\le\sum_Sk_S(k_S-1)=2R_q(F).
\tag{6.7}
\]

The actual odd-load fraction is either \(o_q/N_q\) or its complement, so
its product with its complement is unchanged.  If
\(f(t)=t(1-t)\), (6.7) says that its argument differs from \(\theta_q\) by
at most \(2e_q\).  For \(e\le1/4\), the largest possible increase of
\(f\) is \(2e(1-2e)\); for \(e\ge1/4\), it is at most \(1/4\).
Substitution in (6.4) gives (6.6).  Equality in \(L_q\ge0\) forces
\(e_q=0\). \(\square\)

Thus the ideal coordinatewise pair split against a random relabel strictly
improves every nonbalanced load profile.  The only counterterm is realizing
that split through one common Graver signing.

Summing with the weights, let

\[
L_H(F)=\sum_{q\le H}\omega_qL_q(F).
\tag{6.8}
\]

Combining (5.10) and (6.5) yields

\[
\boxed{
\mathbb E_\pi\Theta_H(F,\pi F)
=\Phi_H(F)-\frac14L_H(F)
+\frac18\mathbb E_\pi
\bigl(\Delta_H(F,\pi F)-O_H(F,\pi F)\bigr).
}
\tag{6.9}
\]

This is the exact fifth-wave covariance-routing identity.

## 7. Exact descent, switch-stable obstruction, and sufficient scale

Equation (6.9) gives a strict exact-factor descent whenever

\[
\mathbb E_\pi(\Delta_H-O_H)<2L_H(F).
\tag{7.1}
\]

Indeed, some \(\pi\) then has an antipodal hybrid pair with average energy
below \(\Phi_H(F)\), and at least one of its two exact factors is better.

Consequently every factor stable under all orbit-overlay Graver cubes—and
in particular every global minimizer—obeys the exact obstruction

\[
\boxed{
\mathbb E_\pi
\bigl(\Delta_H(F,\pi F)-O_H(F,\pi F)\bigr)
\ge2L_H(F).
}
\tag{7.2}
\]

The parity gap controls the original energy.  From (6.6),

\[
\boxed{
\Phi_H(F)
\le L_H(F)
+\frac12\sqrt{
\left(\sum_{q\le H}\omega_qN_q\right)L_H(F)}.
}
\tag{7.3}
\]

For \(H=H_A\) and \(\omega_q=1/a_q\),

\[
\sum_{q\le H}\omega_qN_q=\Theta_A(WH).
\tag{7.4}
\]

Therefore the following theorem would close fixed-window unlabelled MWB.

> **UNPROVED parity-Graver routing theorem \(\mathrm{PGR}_A\).**  For a
> global minimizer of \(\Phi_{H_A}\), or uniformly for every exact factor,
> \[
> \mathbb E_\pi
> [\Delta_{H_A}(F,\pi F)-O_{H_A}(F,\pi F)]
> =o(W/H_A).
> \tag{7.5}
> \]

At a global minimizer, (7.2) gives \(L_H=o(W/H)\).  Equations
(7.3)--(7.4) then give

\[
\Phi_H=o(W).
\]

The scale in (7.5) matters.  A mere \(o(W)\) bound on the Graver slack does
not imply \(o(W)\) collision excess in the worst case.  The sharper
factor-scale conclusion \(\Phi_H=O_A(HB)=O_A(W/H)\) would require a
correspondingly stronger quantitative version; (7.3) alone would ask for
slack on the order of \(W/H^3\).

There is a second, stronger but simpler sufficient gate.  Put

\[
\ell_H(F,G)=\|T(x_G-x_F)\|^2.
\]

Because \(\Phi_H(\pi F)=\Phi_H(F)\), the optimal cube-pair average is

\[
\Phi_H(F)+\frac18[\Delta_H(F,\pi F)-\ell_H(F,\pi F)].
\tag{7.6}
\]

The all-plus signing shows \(\Delta_H\le\ell_H\).  If \(F\) is a global
minimizer, strict inequality would make the average in (7.6) smaller than
\(\Phi_H(F)\), and one antipodal corner would contradict minimality.
Therefore

\[
\boxed{\Delta_H(F,\pi F)=\ell_H(F,\pi F)
\quad\text{for every }\pi}
\tag{7.6a}
\]

at every global minimizer.  Equivalently, every component cut has
nonpositive cross inner product.

Uniform permutation averaging gives

\[
\boxed{
\mathbb E_\pi\ell_H(F,\pi F)=4\Phi_H(F)+2J_H.
}
\tag{7.7}
\]

Hence an upper bound

\[
\mathbb E_\pi\Delta_H(F,\pi F)
\le2J_H+\eta_m
\tag{7.8}
\]

at a global minimizer gives exactly

\[
\Phi_H(F)\le\eta_m/4.
\tag{7.9}
\]

This is the averaged Graver-discrepancy formulation.  It is unproved and,
at a global minimizer, is algebraically equivalent to the desired bound
once cube rigidity is used.  The parity-slack formulation (7.5) isolates
more sharply what must be controlled.

## 8. Exact invariant obstructions

### 8.1 Pair-sum profile obstruction

The quantity \(\mathfrak B_H(F,G)\) is unchanged by every covariance choice
on the \(F/G\) face.  If it is \(\Omega(W)\), no midpoint-preserving law on
that face can give \(o(W)\) excess.  Since every positive
\(b_a(t)\) is at least one, a linear number of pair sums outside
(5.14) already gives this obstruction.

### 8.2 Connected-overlay obstruction

If \(\mathcal O(F,G)\) is connected, the face contains only \(F,G\).  There
is one sign, so

\[
\Delta_H(F,G)=\ell_H(F,G).
\]

No mixed-sign component routing exists.

### 8.3 Shadow-orthogonal obstruction

If

\[
\langle V_i,V_j\rangle=0\qquad(i\ne j),
\]

then every sign vector has the same discrepancy

\[
\left\|\sum_i s_iV_i\right\|^2=\sum_i\|V_i\|^2.
\]

All midpoint-preserving covariance laws have the same quadratic action.

More generally,

\[
\Delta_H(F,G)
\ge\max\left\{0,
\sum_i\|V_i\|^2-2\sum_{i<j}|\langle V_i,V_j\rangle|
\right\}.
\tag{8.1}
\]

This gives an exact diagonally-dominant obstruction.

### 8.4 Restricted trade-span obstruction

Let \(\mathcal T\) be any allowed family of exact trades and put

\[
U=\operatorname{span}\{Tg:g\in\mathcal T\}.
\]

Inside a reachability class generated by \(\mathcal T\),

\[
z_\perp=P_{U^\perp}(Tx_F-u)
\tag{8.2}
\]

is invariant.  Writing the remaining, random part as \(Z_U\), every law on
the class satisfies

\[
\boxed{
\mathbb E\Phi_H
=\frac12\left[
\|z_\perp\|^2+\|\mathbb EZ_U\|^2
+\operatorname{tr}\operatorname{Cov}(Z_U)-J_H
\right].
}
\tag{8.3}
\]

Thus covariance cannot repair the component of the defect outside the
shadow span of the allowed trades.

### 8.5 Whole coordinate orbits do not descend

For every coordinate permutation \(\pi\),

\[
\mu_q^{\pi F}=P_{\pi,q}\mu_q^F,
\qquad \Phi_H(\pi F)=\Phi_H(F).
\]

An orbit law only converts deterministic defect into covariance:

\[
\|\mathbb EZ\|^2+\operatorname{tr}\operatorname{Cov}(Z)
=\|Tx_F-u\|^2,
\]

where \(Z=Tx_{\pi F}-u\).  Genuine descent requires the hybrid Graver
corners, not whole relabelings alone.

## 9. Nontrivial classes on which the theorem closes

The theorem is exact on every physical Graver cube.  In particular, suppose
a cube has

\[
\mathfrak B_H(F,G)=0,
\qquad
\Delta_H(F,G)=O_H(F,G).
\tag{9.1}
\]

Then the optimizing antipodal pair consists of two distinct exact factors
with

\[
R_q=0\qquad(1\le q\le H).
\tag{9.2}
\]

Here “distinct” assumes that the cube has at least one nontrivial component.

More generally, pair some component indices and use independent fair coins
between pairs, with the optimal correlation inside each pair.  Put

\[
T_{\mathcal P}
=\sum_i\|V_i\|^2
-2\sum_{\{i,j\}\in\mathcal P}|\langle V_i,V_j\rangle|.
\tag{9.3}
\]

Then

\[
\mathbb E\Phi_H
=\mathfrak B_H(F,G)
+\frac18(T_{\mathcal P}-O_H).
\tag{9.4}
\]

This supplies a genuine mixed-sign law on any such nontrivial factor class.
What is unproved is the existence, in the physical wreath fibre for growing
\(m\), of a useful cube satisfying (9.1) or its \(o(W)\) weakening.  Ambient
signed-lattice selectors do not suffice because their positive and negative
sides need not extend to exact factors.

There is also a classwise form with exact quantifiers.  Let
\(\mathscr C\) be a nonempty family of exact factors which is
\(S_n\)-invariant and is closed under every ownership-component hybrid
between \(F\in\mathscr C\) and \(\pi F\).  Choose a minimizer of
\(\Phi_H\) inside \(\mathscr C\).  All rigidity, orbit, parity, and descent
identities in Sections 6--7 remain internal to \(\mathscr C\).  Hence
\(\mathrm{PGR}_A\) for that class implies that \(\mathscr C\) contains a
factor with \(\Phi_H=o(W)\).  No natural asymptotic class satisfying the
required Graver-slack estimate is presently proved.

## 10. Final implication scope

The proved conclusions are:

1. exact ownership-component trades give the complete supported Graver cube;
2. every positive component cut gives a literal exact-factor covariance
   improvement with the exact constant (3.3);
3. the optimal midpoint-preserving law on a fixed cube is an antipodal
   mixed-sign law;
4. its optimum is exactly the immutable pair-sum floor plus the
   parity-restoring signing slack;
5. random coordinate pairing gives the exact parity-descent identity (6.9);
6. connected faces, orthogonal component effects, and invariant trade spans
   give exact covariance obstructions.

The unproved physical theorem is \(\mathrm{PGR}_A\), or a direct construction
of a face with

\[
\mathfrak B_H=o(W),\qquad
\Delta_H-O_H=o(W).
\]

Either statement would produce a low-collision exact factor.  No such bound
is proved here.  Consequently this report proves neither fixed-window MWB,
labelled common-owner synchronization, nor the contiguous-OR conjecture.
