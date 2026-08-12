# Post-$H$ profile propagation: the exact Perron mode, the surviving $+1$ child, and the finite two-shore gate

Date: 2026-07-27

Scope: the equality-resolved compensated promotion-frame process.  This is
an audit of

* `MATH_NOGO_ALL_ORDER_PROFILE_ENERGY_CONSECUTIVE_SPINE_20260727.md`,
* `MATH_REDUCTION_FINITE_H_PROFILE_CUTOFF_AND_NO_POST_H_BOUNDARY_20260727.md`,
* `MATH_THEOREM_PAIR_PROFILE_STOP_UNDER_TRIPLE_FIBRE_AND_NEXT_BOUNDARY_20260727.md`, and
* `MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md`.

No probabilistic or matching conclusion is asserted beyond the hypotheses
stated below.

## 0. Audited verdict

There are three separate facts.

1.  The post-$H$ consecutive child tree has an exact levelwise constant
    Perron mode.  If $K_k$ is its prescribed-child transfer, then

    \[
    K_k\mathbf 1=c_k\mathbf 1,
    \qquad
    c_k={r-k-1\over r-k},
    \qquad H\le k<m.                                      \tag{0.1}
    \]

    In particular,

    \[
    \prod_{k=H}^{\ell-1}c_k={r-\ell\over r-H}.             \tag{0.2}
    \]

    A refinement by gap, shore, or coordinate labels does not remove this
    invariant positive mode.  Any positive coercive argument which is
    permutation-equivariant on the consecutive orbit can be symmetrized
    losslessly back to the scalar recurrence.  Thus such a refinement does
    not evade the audited scalar no-go.

2.  Compensation does **not** cancel the profile-order $+1$ shift.  For a
    live physical resource set $S$, its exact joint deletion hazard is

    \[
    \Lambda_t(S)={|S|\over r}-\nu_tJ_t(S),
    \qquad
    J_t(S)=\sum_g(|g\cap S|-1)_+.                           \tag{0.3}
    \]

    Hence normalization by independent marginal survival leaves the
    positive term $+\nu_tJ_t(S)$.  An event meeting two displayed
    resources contributes a literal first-new-resource child, hence a
    $+1$ profile shift.  Compensation coins are singleton events and
    provide no term of the opposite sign.

    The fact that the centered power generator of one decrement starts at
    Taylor order $2$ is different: it concerns powers
    $A_C(g)^\ell$, not the number of physical resources in a profile.
    The compensated $+2$ power-diagonal EGF therefore does not establish
    cancellation of the profile $+1$ term.

3.  Propagation beyond $H$ is nevertheless unnecessary in the existing
    finite-cutoff reduction.  It is eliminated **conditionally**, not
    unconditionally.  The exact remaining theorem lives only at
    $2\le k<H$: one needs a uniform gap/equality-resolved child kernel and
    its theta quadratic estimate, followed by the already audited one-step
    stopped argument.  At order $H$, direct incidence-weighted terminal
    quarantine is sufficient.  Therefore a new post-$H$ multidimensional
    norm would duplicate a boundary which the finite reduction has already
    removed.

## 1. The exact geometric state cannot be only $k$ or $(p,q)$

Root a frame at an owner $X$.  For each additional owner $Y$, its
leaving and entering sets lie on the positive or negative shore.  On the
two shores, list the positive successive distance gaps as

\[
 \mathbf g^+=(g_1^+,\ldots,g_a^+),\qquad
 \mathbf g^-=(g_1^-,\ldots,g_b^-),                          \tag{1.1}
\]

and put

\[
 p=\sum_i g_i^+,qquad q=\sum_jg_j^-.                       \tag{1.2}
\]

The state also contains the actual nested label sets on both shores and
the physical equality partition of displayed row, column, and
compensation resources.  After quotienting by coordinate permutations,
the smallest lossless static parameter is therefore

\[
 \boxed{(\mathbf g^+,\mathbf g^-,\eta)},                    \tag{1.3}
\]

where $\eta$ is the physical equality/type data.  The totals $p,q$
alone are not lossless.  For one admissible signing with $p+q\le H$, the
exact rooted mass is

\[
 q(\mathbf g^+,\mathbf g^-)
 =\left[
 { (m-p-q)!\prod_i g_i^+!\prod_jg_j^-!\over m!}
 \right]^2.                                                \tag{1.4}
\]

For example, on one shore at total span $p$, the one-gap state
$(p)$ and the fully refined state $(1,\ldots,1)$ have masses in ratio

\[
                         (p!)^2.                            \tag{1.5}
\]

Thus neither order nor the two shore totals determine the physical base
or the child ratios.  Any proposed multidimensional energy which forgets
the two ordered gap compositions has already replaced the exact catalogue
by an uncontrolled majorant.

## 2. Exact post-$H$ child tree

Let $\Omega_k$ be the labelled consecutive-spine states at order $k$.
Every state in $\Omega_k$ has exactly

\[
                         d_k=m-k                           \tag{2.1}
\]

admissible next coordinate continuations.  For one prescribed child, the
exact mass ratio is

\[
 \rho_k={\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over m-k},
 \qquad H\le k<m.                                        \tag{2.2}
\]

Define the positive child operator by

\[
 (K_kf)(\sigma)
 =\rho_k\sum_{\tau\in\operatorname{Ch}(\sigma)}f(\tau).
                                                               \tag{2.3}
\]

Equations (2.1)--(2.3) give (0.1).  Moreover, a fixed order-(k)
spine state has ((m-k)_{\ell-k}) labelled order-(\ell) descendants,
and therefore

\[
 (m-k)_{\ell-k}{\Gamma_\ell\over\Gamma_k}
 ={r-\ell\over r-k},
 \qquad H\le k<\ell\le m.                                \tag{2.4}
\]

Thus the entire aggregate descendant mass loses only the telescoping
factor in (2.4).  At (\ell=m), this is

\[
 {r-m\over r-H}=(1+o(1)){H\over m},                        \tag{2.5}
\]

not an exponential or factorial attenuation.

The same conclusion is independent of the particular positive norm.
If $\|\cdot\|_k$ is any monotone homogeneous norm on nonnegative
functions on $\Omega_k$, then

\[
 \|K_k\|_{k+1\to k}
 \ge c_k{\|\mathbf1\|_k\over\|\mathbf1\|_{k+1}},          \tag{2.5a}
\]

because it may be tested on the constant function.  Consequently

\[
 \|K_HK_{H+1}\cdots K_{\ell-1}\|_{\ell\to H}
 \ge {r-\ell\over r-H}
      {\|\mathbf1\|_H\over\|\mathbf1\|_\ell}.             \tag{2.5b}
\]

Changing the level normalizations $\|\mathbf1\|_k$ is exactly a
one-index scalar reweighting.  The audited initialization-versus-
propagation contradiction applies to that reweighting.  Thus a nonlinear
choice of norm does not evade the constant mode unless it ceases to be
coercive on some spine states or uses signed cancellation.

Before (H), the corresponding row sum is

\[
 c_k={r-k-1\over r-k}{1\over m-k},
 \qquad k<H,                                              \tag{2.6}
\]

which is (\Theta(m^{-1})).  This is the exact reason that (H) is a
valid terminal geometric scale and not merely an arbitrary truncation.

### Proposition 2.1 (lossless symmetrization on the spine)

Consider a positive linear Lyapunov or majorant construction on a state
refinement of the post-(H) tree.  Assume:

1. its coefficient inequalities are convex and invariant under
   permutations of the unused coordinates;
2. it majorizes the positive child operator (2.3); and
3. it is coercive on every physical consecutive-spine state which it is
   supposed to charge.

Then averaging all coefficients over the unused-coordinate permutation
group preserves feasibility, initial invariant mass, and coercivity.  The
averaged coefficients are constant on every (\Omega_k), and the
restriction of the averaged construction to the spine is exactly the
one-index recurrence with coefficient (c_k).

#### Proof

The permutation group acts transitively on (\Omega_k), preserves the
child relation, and commutes with (K_k).  Apply every group element to a
feasible coefficient family and average.  Convexity preserves every
coefficient inequality; positivity and coercivity are preserved; every
invariant initial or charging functional is unchanged.  Transitivity
makes the averaged coefficient constant on (\Omega_k).  Equation
(0.1) then identifies the restricted transfer coefficient as (c_k).
(\square)

Consequently the scalar consecutive-spine obstruction applies to every
such positive refinement.  The genuine loopholes are exactly:

* terminate and quarantine at (H);
* use a noncoercive energy and separately prove that its low-weight states
  carry negligible incidence;
* prove an exact signed coboundary cancellation rather than a positive
  majorant; or
* use a trajectory theorem which never enters the post-(H) transfer.

Merely recording ((p,q)), or even the complete compositions in (1.1),
does not by itself provide one of these loopholes.

## 3. Compensation leaves the (+1) child exactly

Every active selected edge (g) rings at rate (\nu_t), and every active
resource (y) has compensation rate

\[
 \chi_t(y)={1\over r}-\nu_td_t(y).                         \tag{3.1}
\]

For a finite live set (S), the rate of an event deleting at least one
member of (S) is

\[
\begin{aligned}
 \Lambda_t(S)
 &=\nu_t\left|\bigcup_{y\in S}\mathcal E_t(y)\right|
   +\sum_{y\in S}\chi_t(y)\\
 &={|S|\over r}
   -\nu_t\left(
       \sum_{y\in S}d_t(y)
       -\left|\bigcup_{y\in S}\mathcal E_t(y)\right|
     \right).
                                                               \tag{3.2}
\end{aligned}
\]

Reversing the edge sum proves

\[
 J_t(S)
 =\sum_g(|g\cap S|-1)_+.                                  \tag{3.3}
\]

If (I_S) is the indicator that every member of (S) is live and
(u_t=e^{-t/r}), then, before a protected-resource death,

\[
 (\partial_t+\mathcal L_t){I_S\over u_t^{|S|}}
 =\nu_tJ_t(S){I_S\over u_t^{|S|}}\ge0.                    \tag{3.4}
\]

In particular, for (S=\{x,y\}),

\[
                         J_t(S)=d_t(x,y).                  \tag{3.5}
\]

This is the order-(3) fibre which enters the pair-profile calculation.
No coin clock deletes both (x) and (y), so no compensation term cancels
(3.5).

For a cluster count (A_C), centering the decrement identity

\[
 \mathcal L A_C^h
 =\sum_{\ell=1}^h(-1)^\ell\binom h\ell
 A_C^{h-\ell}\mathsf D_\ell(C)+\mathsf K_C              \tag{3.6}
\]

removes the (\ell=1) Taylor term and leaves (\ell\ge2).  But
(\mathsf D_1(C)) itself contains the common-event correction (3.3).
Thus “Taylor order (2)” in (3.6) cannot be reinterpreted as “profile
order (+2).”

## 4. What the finite-(H) reduction actually proves

The finite-cutoff note is a conditional consumer theorem.  It assumes,
for every equality-resolved physical child orbit and every
(2\le k<H),

\[
 \sum_{T\in\mathscr C(S)}q_{k+1}(T)
 \le {C\over m}q_k(S),                                   \tag{4.1}
\]

with ordered physical multiplicities, and a uniform stopped one-step
estimate whose failure fraction (\varepsilon_m) obeys

\[
                         H\varepsilon_m=o(1).             \tag{4.2}
\]

Iteration of (4.1) gives

\[
 \sum_{S_2\leadsto S_H}q_H(S_H)
 \le(C/m)^{H-2}q_2(S_2).                                 \tag{4.3}
\]

Direct maximal control of each order-(H) normalized link and
incidence weighting then quarantine the terminal family at the cost in
(4.3).  No profile of order (H+1) is introduced.  Summing the disjoint
first-violated levels below (H) costs (H\varepsilon_m).

Therefore the post-(H) Perron mode is not the remaining gate.  What is
unproved is (4.1)--(4.2), uniformly over the full physical gap/equality
state.  In particular, the order-two instance proved before the
triple-profile stop does not itself provide uniformity up to (H).

## 5. Smallest presently legitimate multidimensional theorem

The order-two proof shows exactly which local estimates are needed.  The
following is a state-resolved finite theorem; it makes no assertion at or
above (H).

### FTSK (finite two-shore kernel)

There are a fixed exponent $C_0$ and an absolute $C$ such that, with

\[
                         \Lambda_m=(\log m)^{C_0},
\]

for every sufficiently large (m),
every (2\le k<H), every reachable equality-resolved physical
(k)-profile (S) with full state (1.3), every external physical
resource (a), and every active event row (G) disjoint from the protected
prefix, the following hold with all physical equality multiplicities:

\[
 q_{k+1}(S\cup\{a\})
 \le {C\Lambda_m\over m^2}q_k(S),                         \tag{FTSK1}
\]

\[
 \sum_{a\in V(G)\setminus S}^{\rm phys}
 q_{k+1}(S\cup\{a\})
 \le {C\Lambda_m\over m}q_k(S),                          \tag{FTSK2}
\]

and

\[
 \sum_{a\ne b}^{\rm phys}
 q_2(a,b)
 q_{k+1}(S\cup\{a\})q_{k+1}(S\cup\{b\})
 \le {C\Lambda_m\over m^2}q_k(S)^2.                      \tag{FTSK3}
\]

The corresponding edge-column and compensation-child versions are
included.  Equivalently, one may replace (m) by the exact free-gap
dimension in each state; throughout the finite range that dimension is
((1+o(1))m).

### Proposition 5.1 (FTSK is sufficient for the finite cutoff)

Assume FTSK, the ordinary degree corridor, the already proved pair stop,
and the whole-arm equality-resolution stop.  Use a common
polylogarithmic profile threshold (A).  Then the order-(k) normalized
link, stopped at its order-(k+1) children, has

\[
 b_*\le {C\Lambda_mA\over mz_*},                          \tag{5.1}
\]

and predictable quadratic variation

\[
 V_*\le C\left(
 {\Lambda_mA^2\over mz_*}
 +{\Lambda_mA_2A^2\over m^2z_*^3}
 \right).                                                 \tag{5.2}
\]

For

\[
 z_*=m^{-1/2}(\log m)^B                                  \tag{5.3}
\]

with (B) sufficiently large relative to the fixed threshold powers,
(b_*=o(1)), (V_*=o(1)), and the one-step crossing fraction can be
chosen (\varepsilon_m) with (H\varepsilon_m=o(1)).  Hence (4.3)
and the finite-cutoff argument give (o(W)) total profile-stopped marked
incidence.

#### Proof

Put

\[
 \mu_S=q_k(S)D_0u_t^{r-k},
 \qquad A_a(t)=d_t(S\cup\{a\}).                           \tag{5.4}
\]

Before the child stop, FTSK1 gives

\[
 \max_a{A_a\over\mu_S}
 \le {C\Lambda_mA\over m^2u_t}.                           \tag{5.5}
\]

FTSK2 gives, for one selected event row,

\[
 {1\over\mu_S}\sum_{a\in V(G)}A_a
 \le {C\Lambda_mA\over m u_t},                           \tag{5.6}
\]

which is (5.1).  The diagonal selected-edge and coin terms obey

\[
 {1\over r\mu_S^2}\sum_aA_a^2
 \le {C\Lambda_m A^2\over m^2u_t},                       \tag{5.7}
\]

using (\sum_aA_a=(r-k)d_t(S)).  For the off-diagonal selected-edge
term, reverse the event sum exactly as in the pair-profile proof.  The
pair stop and FTSK3 give rate

\[
 {1\over r\Delta_t\mu_S^2}
 \sum_{a\ne b}d_t(a,b)A_aA_b
 \le {C\Lambda_mA_2A^2\over rm^2u_t^3}.                  \tag{5.8}
\]

Integrating (5.7)--(5.8) with $dt=-r\,du/u$ gives (5.2).
The one-sided Freedman estimate from the order-two proof now applies
with constants independent of (k).  A sufficiently large
polylogarithmic (A) makes its marked crossing fraction smaller than
(o(1/H)).  FTSK2 iterates to (4.3), completing the finite-cutoff
consumer argument. (\square)

FTSK1--FTSK3, with a fixed polylogarithmic loss of this form, are already
proved at the pair-to-triple step.  Their uniform
gap/equality-resolved extension through (k<H) is unproved.  This is the
narrowest theorem supported by the existing stochastic calculation.  It
retains exactly the geometry which scalar order weighting discards, but it
does not attempt to cross the audited Perron sector.

## 6. Final boundary and adversarial audit

Unconditional conclusions of this note are:

1. the exact constant-mode identities (0.1)--(0.2) and (2.4);
2. lossless symmetrization for positive permutation-equivariant coercive
   refinements of that spine;
3. the exact surviving compensation term (3.4); and
4. the distinction between power-diagonal Taylor order and physical
   profile order.

Conditional conclusions are:

1. the finite-(H) removal of the post-(H) boundary, conditional on
   (4.1)--(4.2); and
2. the (o(W)) stopped-incidence conclusion, conditional on FTSK and
   the previously stated degree/whole-arm stops.

The Perron argument does not exclude signed energies, a proved
state-dependent coboundary, or noncoercive incidence quarantine.  It also
does not construct an adverse vertex-induced trajectory.  Conversely,
the finite cutoff does not prove FTSK: static fixed-order codegrees and the
order-two theta identity do not automatically give uniform current-state
control through (H).  These are the exact proved/conditional boundaries.
