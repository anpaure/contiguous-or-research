# Weighted quotient lift: exact dual and a Gaussian cross-profile obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 q=A\sqrt m+O(1),\quad A>0,
\tag{0.1}
\]

and let the core be split into blocks

\[
 B_j=A_j\mathbin{\dot\cup}C_j,qquad |A_j|=|C_j|=d,qquad
 b=m/d+O(1),
\tag{0.2}
\]

where

\[
 d\longrightarrow\infty,qquad d^2=o(\sqrt m),qquad
 (m/d)e^{-c_0d}=o(1).
\tag{0.3}
\]

Thus a sufficiently large constant multiple of \(\log m\) is
admissible.  Use arbitrary rank-dependent perfect matchings
\(\pi_{j,k}:A_j\to C_j\).

The weighted source-capacity LP left open in
`MATH_THEOREM_ORDERED_PROFILE_QRE_AND_WEIGHTED_LIFT_GATE_20260726.md`
has the following exact dual.  If

\[
 A_{\tau\kappa}(y)
 =\sum_{T\in\tau}y_T R_{\tau\kappa}(T),
\tag{0.4}
\]

then capacities \(c_{\tau\kappa}\ge0\) satisfying

\[
 \sum_\tau c_{\tau\kappa}\le1,qquad
 \sum_\kappa c_{\tau\kappa}R_{\tau\kappa}(T)\ge1
\tag{0.5}
\]

exist if and only if, for every \(y_T\ge0\),

\[
 \boxed{
 \sum_Ty_T\le
 \sum_\kappa\max_\tau A_{\tau\kappa}(y).}
\tag{0.6}
\]

Here \(R_{\tau\kappa}=R_\lambda\), because for fixed \(\tau\) the
source profile \(\kappa\) determines the allocation \(\lambda\).
Equation (0.6), not an average score estimate, is the exact remaining
cross-profile theorem.

The exact quotient flow does **not** satisfy the desired pointwise lift,
even after all of its constant owner slack is used.  Let \(F_{\tau\kappa}\)
be the ordinary-inclusion quotient flow restricted to allocations with
at most two promotions in a block, and scale it to full source capacity:

\[
 c^F_{\tau\kappa}
 ={1-\varepsilon_m\over\rho_q}
 {F_{\tau\kappa}\over|\kappa|},qquad
 \rho_q={N_q\over W}=e^{-A^2+o(1)},qquad
 \varepsilon_m=O_A(d^2/\sqrt m)=o(1).
\tag{0.7}
\]

Then \(\sum_\tau c^F_{\tau\kappa}\le1\).  Nevertheless, on all but
\(o(N_q)\) lower targets, conditional on any typical ordered profile,

\[
 \boxed{
 \log\!\left(\sum_\kappa
       c^F_{\tau\kappa}R^-_{\tau\kappa}(T)\right)
 =2A Z_\tau^-(T)-A^2+o_{\mathbb P}(1),}
\tag{0.8}
\]

where \(Z_\tau^-\Rightarrow N(0,1)\).  The upper formula is identical.
Consequently

\[
 {1\over N_q}\#\left\{T:
   \sum_\kappa c^F_{\tau(T)\kappa}R^-_{\tau(T)\kappa}(T)<1
                  \right\}
 \longrightarrow \Phi(A/2)>0,
\tag{0.9}
\]

and likewise above.  Thus the quotient flow leaves a **linear**, not
quarantine-sized, pointwise deficit.  Its mean score is
\(e^{A^2+o(1)}\); the mean is carried by the lognormal upper tail.

There is also a quantitative stability obstruction.  Put

\[
 \Delta_A
 =\mathbb E(1-e^{2AZ-A^2})_+
 =\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0,
 \qquad Z\sim N(0,1).
\tag{0.10}
\]

If another capacity system \(c\) satisfies the pointwise inequality in
(0.5) outside \(o(N_q)\) targets, then

\[
 \boxed{
 \sum_{\tau,\kappa}|c_{\tau\kappa}-c^F_{\tau\kappa}|\,|\kappa|
 \ge (\Delta_A-o(1))N_q
 = (e^{-A^2}\Delta_A-o(1))W.}
\tag{0.11}
\]

Hence no \(o(W)\) repair, bounded tail correction, or perturbative
rounding of the quotient flow can prove the weighted theorem.  A positive
solution of (0.6), if one exists, must reroute a positive fraction of all
source-profile capacity.  The exponential unweighted one-hit reservoir
does not prevent (0.8), because the quotient weights normalize that
reservoir by the equally exponential number of competing allocations.

This is an explicit cross-profile obstruction to the proposed quotient
lift.  It is not yet a Farkas counterexample to the unrestricted LP:
the maximum over \(\tau\) in (0.6) may exploit a macroscopic rerouting
which \(c^F\) does not.  Therefore the maximal raw injection is neither
proved nor disproved here.

## 1. Exact weighted LP dual

Discard a fixed quarantine \(E\) and write \({\cal T}\) for the retained
targets.  For each ordered target profile \(\tau\), source profile
\(\kappa\), and \(T\in\tau\), let \(R_{\tau\kappa}(T)\ge0\) be the exact
status-stratum source/target ratio.  The primal feasibility system is

\[
\begin{aligned}
 &c_{\tau\kappa}\ge0,\\
 &\sum_\tau c_{\tau\kappa}\le1 &&(\kappa\text{ fixed}),\\
 &\sum_\kappa c_{\tau\kappa}R_{\tau\kappa}(T)\ge1
       &&(T\in\tau\cap{\cal T}).
\end{aligned}
\tag{1.1}
\]

### Theorem 1.1 (exact support-function dual)

System (1.1) is feasible if and only if

\[
 \sum_{T\in{\cal T}}y_T
 \le\sum_\kappa\max_\tau
       \sum_{T\in\tau\cap{\cal T}}
                y_TR_{\tau\kappa}(T)
\tag{1.2}
\]

for every nonnegative vector \(y\).

#### Proof

For fixed \(y\ge0\), the largest weighted target score obtainable under
the source-profile capacity constraints is

\[
\begin{aligned}
 \sup_c\sum_Ty_T\sum_\kappa
             c_{\tau(T)\kappa}R_{\tau(T)\kappa}(T)
 &=\sum_\kappa\sup_{\substack{c_{\tau\kappa}\ge0\\
                         \sum_\tau c_{\tau\kappa}\le1}}
       \sum_\tau c_{\tau\kappa}A_{\tau\kappa}(y)\\
 &=\sum_\kappa\max_\tau A_{\tau\kappa}(y).
\end{aligned}
\tag{1.3}
\]

Thus (1.2) is necessary.  Conversely, if the convex down-set of score
vectors generated by the source-capacity simplices does not contain a
vector which is at least one in every coordinate, finite-dimensional
separation supplies a nonnegative separating normal \(y\).  Its support
function is (1.3), contradicting (1.2).  This is precisely the usual
Farkas argument. \(\square\)

The maximum in (1.2) is the point missed by an averaged quotient-flow
argument.  The ordered-profile theorem controls a sum over \(\kappa\)
for one fixed \(\tau\), whereas (1.2) lets each source profile choose the
best competing target profile.

## 2. The quotient capacities and their exact local polynomial

Fix a lower ordered target profile

\[
 \tau=((a_j,c_j))_{j\le b}.
\tag{2.1}
\]

For an allocation
\(\lambda=((\alpha_j,\gamma_j))\), put

\[
 \kappa(\lambda)=((a_j+\alpha_j,c_j+\gamma_j))_{j\le b}.
\tag{2.2}
\]

Let

\[
 B_{\kappa\tau}
 =\prod_j\binom{a_j+\alpha_j}{\alpha_j}
             \binom{c_j+\gamma_j}{\gamma_j}.
\tag{2.3}
\]

This is the number of ordinary rank-\((m-q)\) members of profile \(\tau\)
contained in one fixed middle set of profile \(\kappa\).  Hence

\[
 {J_{\tau\kappa}\over|\kappa|}=B_{\kappa\tau}.
\tag{2.4}
\]

For the untruncated ordinary inclusion flow,

\[
 \sum_\tau B_{\kappa\tau}=\binom mq.
\tag{2.5}
\]

Equation (2.5) explains the full-capacity normalization in (0.7).  The
restriction \(\alpha_j+\gamma_j\le2\) loses only
\(\varepsilon_m=O_A(d^2/\sqrt m)\) of a target row and can only decrease
a source column.

For one block, let \(t=a+c\).  Relative to the rank-\((t+1)\) matching,
write the target statuses as

\[
 (f,p,s,e)=(f,a-f,c-f,d-a-c+f).
\tag{2.6}
\]

Multiplying the one-hit status ratios by the reverse ordinary counts in
(2.3) gives the exact first coefficient

\[
 \boxed{
 u_j(T)=e_j\left(
 {a_j+1\over p_j+1}+{c_j+1\over s_j+1}
                 \right).}
\tag{2.7}
\]

For the rank-\((t+2)\) matching, use its statuses
\((f^{(2)},p^{(2)},s^{(2)},e^{(2)})\).  The exact two-hit coefficient is

\[
\begin{aligned}
 v_j(T)={}&
 \binom{a_j+2}{2}{\binom{e^{(2)}}2\over
                         \binom{p^{(2)}+2}2}\\
 &+(a_j+1)(c_j+1)
 {e^{(2)}(e^{(2)}-1)\over
       (p^{(2)}+1)(s^{(2)}+1)}\\
 &+\binom{c_j+2}{2}{\binom{e^{(2)}}2\over
                         \binom{s^{(2)}+2}2}.
\end{aligned}
\tag{2.8}
\]

Terms with an impossible denominator are interpreted as zero; on the
safe core every displayed denominator is positive.

By (2.3), (2.7), (2.8), and the exact stratum formula for
\(R_\lambda^-\),

\[
 \sum_{\substack{\lambda:\ \sum(\alpha_j+\gamma_j)=q\\
                    \alpha_j+\gamma_j\le2}}
 B_{\kappa(\lambda)\tau}R^-_\lambda(T)
 =[z^q]\prod_{j=1}^b(1+u_j(T)z+v_j(T)z^2).
\tag{2.9}
\]

Consequently, uniformly on typical safe profiles,

\[
 \boxed{
 S_F^-(T):=\sum_\kappa c^F_{\tau\kappa}
                         R^-_{\tau\kappa}(T)
 =(1+o(1)){[z^q]\prod_j(1+u_jz+v_jz^2)\over\binom mq}.}
\tag{2.10}
\]

The \(o(1)\) in (2.10) is deterministic at the profile scale: it is the
product of the row renormalization, the source-load scaling, and the
residual-coordinate correction.

## 3. The first coefficient carries an unavoidable Gaussian

Put

\[
 x_j=a_j/d,qquad y_j=c_j/d,qquad
 \bar f_j=x_jy_jd.
\tag{3.1}
\]

Conditional on \(\tau\), the variables \(f_j\) measured by the
rank-\((t_j+1)\) matchings are independent and

\[
 f_j\sim\operatorname{Hyp}(d,c_j,a_j),qquad
 \operatorname{Var}f_j
 ={a_jc_j(d-a_j)(d-c_j)\over d^2(d-1)}.
\tag{3.2}
\]

No cross-rank independence is needed for the leading term.  After an
ordered profile is fixed, the local target choices are independent across
blocks.  Within one block, \(u_j\) and \(v_j\) may be correlated through
the two rank matchings, but both are bounded by \(O(d)\) and \(O(d^2)\),
respectively.  This is enough to make every centered quadratic-saddle
contribution negligible.

Regard the right side of (2.7) as a smooth function \(u_j(f)\).  On a
fixed safe compact set,

\[
 u_j(f_j)-\mathbb Eu_j(f_j)
 =\beta_j(f_j-\bar f_j)+\xi_j,
\tag{3.3}
\]

where

\[
 \beta_j={1\over x_j(1-y_j)}+{1\over y_j(1-x_j)}+O(d^{-1})
\tag{3.4}
\]

and

\[
 {A\over\sqrt m}\sum_j\xi_j=o_{\mathbb P}(1).
\tag{3.5}
\]

Indeed, Taylor's formula gives
\(|\xi_j|\le C((f_j-\bar f_j)^2/d+1)\) after subtracting its mean.
The centered sum has standard deviation \(O(\sqrt b)\), and
\(\sqrt b/\sqrt m=O(d^{-1/2})\).

Typical ordered profiles satisfy

\[
 {1\over b}\sum_j
 \left((x_j-1/2)^2+(y_j-1/2)^2\right)=O(d^{-1})
\tag{3.6}
\]

and have all but \(o(b)\) blocks in a fixed safe compact set.  These
profiles carry \(1-o(1)\) of the target layer.  On them, (3.2)--(3.4)
give

\[
 {1\over m}\sum_j\beta_j^2\operatorname{Var}f_j=4+o(1).
\tag{3.7}
\]

The Lindeberg condition follows from \(d=o(\sqrt m)\).  Therefore

\[
 {A\over\sqrt m}\sum_j
       (u_j-\mathbb Eu_j)\Longrightarrow N(0,4A^2).
\tag{3.8}
\]

### Lemma 3.1 (coefficient saddle)

For every typical profile there is a deterministic \(C_\tau\) such that

\[
 \log S_F^-(T)
 =C_\tau+{A\over\sqrt m}\sum_j
            (u_j(T)-\mathbb Eu_j)+o_{\mathbb P}(1).
\tag{3.9}
\]

The error in (3.9) also tends to zero in exponential mean on every fixed
compact interval of moment parameters.

#### Proof

The saddle for \([z^q](1+z)^m\) is

\[
 z_0={q\over m-q}={A\over\sqrt m}(1+o(1)).
\tag{3.10}
\]

Since \(dz_0=o(1)\),

\[
 \sum_j\log(1+u_jz+v_jz^2)
 =z\sum_ju_j+z^2\sum_j(v_j-u_j^2/2)+O(bd^3z^3).
\tag{3.11}
\]

At \(z=z_0\), the last term is
\(O(d^2/\sqrt m)=o(1)\).  Since one centered quadratic block term is
\(O(d^2)\), block independence gives the sufficient uniform bound

\[
 z_0^2 O_{\mathbb P}(d^2\sqrt b)
 =O_{\mathbb P}(d^{3/2}/\sqrt m)=o(1).
\]

The standard one-dimensional saddle
estimate, or equivalently exponential tilting followed by the local
central limit theorem for a sum of independent \(\{0,1,2\}\)-valued
variables, now gives (3.9).  Bernstein's exponential-moment bound for
the linear sum and the same estimates on the quadratic remainder give
the last assertion. \(\square\)

## 4. Determining the constant from exact mass conservation

There is a small exactness point suppressed in the preceding note.
For an arc \((\tau,\kappa)\),

\[
 \sum_{T\in\tau}R_{\tau\kappa}(T)=E_{\tau\kappa}\le|\kappa|,
\tag{4.1}
\]

where \(E_{\tau\kappa}\) is the number of source sets in \(\kappa\)
having enough correctly oriented singleton edges to reverse the prescribed
allocation.  Equality with \(|\kappa|\) need not hold on an unsafe arc.

On a safe arc with at most two promotions in a block, a fixed touched
block is ineligible with probability \(e^{-\Omega(d)}\).  A union bound
over at most \(q\) touched blocks gives, uniformly,

\[
 E_{\tau\kappa}=(1-o(1))|\kappa|.
\tag{4.2}
\]

It follows from (0.7), the exact target-row identity for \(F\), and
(4.2) that

\[
\begin{aligned}
 {1\over|\tau|}\sum_{T\in\tau}S_F^-(T)
 &= {1\over|\tau|}\sum_\kappa
             c^F_{\tau\kappa}E_{\tau\kappa}\\
 &=(1-o(1)){1-\varepsilon_m\over\rho_q}
   {1\over|\tau|}\sum_\kappa F_{\tau\kappa}\\
 &=e^{A^2+o(1)}.
\end{aligned}
\tag{4.3}
\]

By Lemma 3.1 and (3.8), the random part in (3.9) converges to
\(N(0,4A^2)\), with exponential moments converging.  Taking expectations
in (3.9) and using (4.3) gives

\[
 e^{C_\tau}\,e^{(4A^2)/2}=e^{A^2+o(1)},
\]

and hence

\[
                         C_\tau=-A^2+o(1).
\tag{4.4}
\]

Equations (3.8), (3.9), and (4.4) prove (0.8).  Complementation gives the
upper statement, with full edges replacing empty edges and the same
variance and constant.

The failure probability is now exact:

\[
 \Pr\{S_F^-(T)<1\mid\tau\}
 \longrightarrow
 \Pr\{2AZ-A^2<0\}=\Phi(A/2).
\tag{4.5}
\]

Since typical profiles have total mass \(1-o(1)\), (4.5) proves (0.9)
globally.  No \(o(N_q)\) quarantine can remove this set.

## 5. Macroscopic distance from every successful repair

For arbitrary capacities \(c\), write

\[
 S_c(T)=\sum_\kappa
          c_{\tau(T)\kappa}R_{\tau(T)\kappa}(T).
\tag{5.1}
\]

From (4.1),

\[
\begin{aligned}
 \sum_T|S_c(T)-S_F(T)|
 &\le\sum_{\tau,\kappa}
      |c_{\tau\kappa}-c^F_{\tau\kappa}|
      \sum_{T\in\tau}R_{\tau\kappa}(T)\\
 &\le\sum_{\tau,\kappa}
      |c_{\tau\kappa}-c^F_{\tau\kappa}|\,|\kappa|.
\end{aligned}
\tag{5.2}
\]

Suppose \(S_c(T)\ge1\) outside \(E\), where \(|E|=o(N_q)\).  On
\(\{S_F<1\}\setminus E\),

\[
 |S_c-S_F|\ge1-S_F.
\]

The lognormal convergence in (0.8), with uniform integrability, yields

\[
 {1\over N_q}\sum_T(1-S_F(T))_+
 \longrightarrow
 \int_{-\infty}^{A/2}(1-e^{2Az-A^2})\phi(z)\,dz.
\tag{5.3}
\]

Exponential tilting gives

\[
 \int_{-\infty}^{A/2}e^{2Az-A^2}\phi(z)\,dz
 =e^{A^2}\Phi(-3A/2),
\tag{5.4}
\]

so (5.3) equals \(\Delta_A\) from (0.10).  Equations (5.2)--(5.4)
prove (0.11).

This shows exactly why the exponential one-hit reservoir is
scalar-insufficient after quotient normalization.  It proves enormous
unweighted \(\sum_\lambda R_\lambda(T)\), but the source capacities
assign weights of reciprocal exponential scale.  The surviving
first-order matching-overlap fluctuation is \(2AZ\), while the entire
Gaussian owner surplus supplies only the deterministic shift \(-A^2\).

## 6. What is and is not settled

Proved:

1. the exact LP dual (1.2);
2. the exact coefficient polynomial (2.9) for the quotient-flow lift;
3. the Gaussian law \(2AZ-A^2\) for its full-capacity pointwise score;
4. a linear \(\Phi(A/2)+o(1)\) family of failed targets on both signs;
5. the explicit deficit constant \(\Delta_A\); and
6. the \(\Omega(W)\) weighted distance of every successful capacity
   system from the quotient flow.

Not proved:

1. a violating vector \(y\) for the unrestricted dual (1.2);
2. infeasibility of a genuinely macroscopic, atlas-dependent rerouting;
3. the maximal raw injection; or
4. selected-axis, packet, or chronological grouping.

The decisive correction is therefore negative for the proposed
**fixed-frame** lift: the exact quotient flow cannot be rounded or locally
repaired into the weighted pointwise theorem.  Inside that fixed frame,
the only remaining positive possibility is a cross-profile transport
macroscopically different from \(F_{\tau\kappa}\) which directly verifies
the max-dual (1.2).  Section 7 audits the distinct moving-frame escape.

## 7. Cross-audit of full local conjugacy-orbit averaging

There is an important escape which does not contradict Sections 2--5.
Those sections fix one rank-matching array.  Now let

\[
 \Gamma_\tau=\prod_j
       \bigl(\mathfrak S(A_j)\times\mathfrak S(C_j)\bigr).
\tag{7.1}
\]

This group acts transitively on the raw targets in every ordered profile
\(\tau\).  Conjugate every local rank matching by \(g\in\Gamma_\tau\),
and denote the resulting ratio by \(R_{\tau\kappa}^g(T)\).  Equivariance
gives

\[
 R_{\tau\kappa}^g(T)
 =R_{\tau\kappa}^{1}(g^{-1}T).
\tag{7.2}
\]

### Proposition 7.1 (exact orbit flattening)

For every fixed arc \((\tau,\kappa)\),

\[
 \boxed{
 {1\over|\Gamma_\tau|}\sum_{g\in\Gamma_\tau}
        R_{\tau\kappa}^g(T)
 ={1\over|\tau|}\sum_{T'\in\tau}
        R_{\tau\kappa}^{1}(T')
 ={E_{\tau\kappa}\over|\tau|},}
\tag{7.3}
\]

independently of \(T\in\tau\).

#### Proof

Transitivity makes the multiset
\(\{g^{-1}T:g\in\Gamma_\tau\}\) uniform on \(\tau\), with every point
appearing \(|\operatorname{Stab}(T)|\) times.  The first equality follows
from (7.2).  The second is (4.1). \(\square\)

Consequently the full-capacity quotient coefficients do satisfy the
annealed pointwise inequality:

\[
\begin{aligned}
 \sum_\kappa c^F_{\tau\kappa}
 {1\over|\Gamma_\tau|}\sum_gR_{\tau\kappa}^g(T)
 &= {1\over|\tau|}\sum_\kappa
          c^F_{\tau\kappa}E_{\tau\kappa}\\
 &=e^{A^2+o(1)}>1
\end{aligned}
\tag{7.4}
\]

on every typical safe profile, for both signs.  Thus the orbit claim is
mathematically correct.

There are two distinct capacity interpretations.

1. **Normalized common-state averaging is legal.**  If \(g\) is one
   common legal matching-array state and is sampled with total probability
   one, then every state separately obeys
   \(\sum_\tau c^F_{\tau\kappa}\le1\).  Averaging preserves the same
   inequality.  No source profile is reused.  In this interpretation the
   orbit does not move the coefficients \(c^F\) at all; it moves a positive
   fraction of the raw incidence inside each shared source profile by
   changing the legal frame.  This is exactly how it evades (0.11), whose
   hypothesis fixes the ratios \(R_{\tau\kappa}\).

2. **Separate full capacity for every conjugate is illegal.**  If a proof
   gives every pair \((\tau,g)\) its own copy of the source shore, the
   exact time-sharing constraint requires probabilities \(p_g\ge0\) with
   \(\sum_gp_g=1\) such that

   \[
      \boxed{
      \sum_\tau c_{\tau\kappa g}\le p_g
      \quad(\kappa,g),
      \qquad \sum_gp_g=1.}
   \tag{7.5}
   \]

   In particular \(\sum_{\tau,g}c_{\tau\kappa g}\le1\), not
   \(\sum_\tau c_{\tau\kappa g}\le1\) separately for each \(g\).
   The conjugates relabel the same raw owners in \(\kappa\); they are not
   disjoint physical copies.  Omitting the factor
   \(|\Gamma_\tau|^{-1}\), or choosing an independently full conjugate
   budget for every target profile, multiplies the owner load by the orbit
   multiplicity.  This is the exact reuse error.

The normalized construction (7.4) therefore closes the **annealed
one-point weighted Hall inequality** over the moving-frame convex hull.
It does not produce a raw injection in one fixed frame.  A fractional
flow may saturate a target only after summing fractions carried by several
different global states; this need not decompose into injections which
each saturate every target in one state.

## 8. Alignment with CPCR

`MATH_EXACT_REMAINING_CROSS_PARENT_COMPILER_RESOLUTION_20260726.md`
defines CPCR, a strong sufficient target,

\[
 \Phi_m=\sum_{q\le H,\epsilon,T}
 (L_q^\epsilon(T)-c_q)(L_q^\epsilon(T)-c_q-1)=o(W).
\tag{8.1}
\]

The later audit
`MATH_AUDIT_CPCR_ONE_SIDED_L1_WEAKENING_20260726.md` proves that the exact
constant-one residual is the strictly weaker L1 missing-shadow/repeat-
excess condition.  The present results sit at the shared source-profile
allocation layer preceding either target.  Their exact relationship is
as follows.

* The fixed-frame quotient **certificate** fails before compiler
  realization.  By (0.9), its canonical uniform status-stratum marginal
  is below one on a linear family at one Gaussian depth, and (0.11) says
  that repairing this pointwise certificate costs \(\Omega(W)\)
  profile-weighted capacity.  This is not, by itself, a universal Hall
  cut or a proof that every fixed-frame state has linearly many holes.
  Its exact L1 interpretation is developed in
  `MATH_THEOREM_L1_MISSING_SHADOW_QUOTIENT_AND_ORBIT_ROUNDING_OBSTRUCTION_20260726.md`.
* Full normalized frame-orbit averaging genuinely supplies the missing
  one-point zero mode with slack, without violating shared
  source-profile capacity.  It is a macroscopic moving-frame operation,
  exactly of the size forced by (0.11).
* CPCR is quadratic and integral.  Equation (7.4) controls only
  \(\mathbb E L_q^\epsilon(T)\).  It gives no bound on
  \(\mathbb E[(L_q^\epsilon(T)-c_q)
                 (L_q^\epsilon(T)-c_q-1)]\), no compiler-image bundle,
  and no simultaneous all-depth slab circulation.  Independent or
  merely annealed conjugates can therefore retain \(\Omega(W)\) floor
  covariance even though every one-point marginal is exact.

Indeed, if the orbit average gives
\(\mathbb E L_T=\lambda=c+\alpha\), then exactly

\[
 \mathbb E[(L_T-c)(L_T-c-1)]
 =\operatorname{Var}(L_T)-\alpha(1-\alpha).
\tag{8.2}
\]

Thus CPCR needs the extremal two-point variance
\(\alpha(1-\alpha)+o(1)\), equivalently concentration on
\(\{c,c+1\}\), not merely the correct mean.  Independent rare orbit
occurrences have Poisson-scale variance \(\lambda+o(1)\), leaving a
positive constant in (8.2) per target and hence \(\Omega(W)\) total
floor covariance at one Gaussian depth.

Accordingly neither (0.8) nor Proposition 7.1 is a counterexample to
CPCR or to the weaker L1 theorem.  The orbit theorem removes the
first-moment Hall deficit.  For CPCR the remaining issue is factorial
covariance; for coefficient one itself the irreducible issue is only the
product-uncovered/L1 homing functional.  Neither formulation reopens a
common-order syndrome, within-packet injectivity gate, or packet-local
chronology problem.
