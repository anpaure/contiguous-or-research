# Audit of the repeated-child \(1/r\) theorem: normalization and higher powers

Date: 2026-07-27

Scope: MATH_THEOREM_REPEATED_CHILD_DIAGONAL_ONE_OVER_R_20260727.md.

## 0. Verdict

The raw reverse-sum inequality (0.4) is correct for the displayed
diagonal proxy.  It does **not** imply a normalization-free coefficient
\(\delta_{k+1}\le2/r\).

For the natural static-incidence and survival-normalized profile energy,
the exact coefficient contributed by child \(a\) is

\[
                 {2\over r u^2}\,\rho_{S,a},\qquad
 \rho_{S,a}={q_{k+1}(S\cup\{a\})\over q_k(S)}.            \tag{0.1}
\]

Thus the theorem as stated—every profile order, every induced residual,
no codegree input—is false.  A child with \(\rho_{S,a}=1\) at density
\(u\ll1\) has coefficient \(2/(ru^2)\), not \(2/r\).

The intended polylogarithmic cutoff can nevertheless be repaired
**conditional on a child-ratio or aggregate diagonal estimate**.  If,
for the equality-resolved profiles being monitored,

\[
                         \rho_{S,a}\le {CJ^4\over m^2}.  \tag{0.2}
\]

then at \(u\ge z=m^{-1/2}(\log m)^{B_0}\), (0.2) makes
\(\rho_{S,a}/u^2=m^{-1+o(1)}\).  Hence the corrected diagonal is no larger
than \(m^{-1+o(1)}/r\), and its integrated geometric-weight coefficient
is \(o(1)\).

Crucially, (0.2) is **not** a consequence of the existing maximum
higher-codegree table.  Upper bounds on \(d_0(S)\) and
\(d_0(S\cup\{a\})\) cannot be divided: a low-degree profile can have a
forced child and \(\rho_{S,a}=1\).  The exact consecutive profiles do
satisfy the required ratio through the cutoff \(J=o(H)\), but all
equality-resolved profiles have not been proved to do so.  Therefore the
general cutoff conclusion still needs an aggregate \(L^2\) child-ratio
theorem; it is not currently repaired merely by the static codegree
maximum.

There is a second, independent gap in the higher repeated-power paragraph.
The current relative decrement is

\[
 {A_a\over A}
 ={\rho_{S,a}\over u}{X_{S\cup\{a\}}\over X_S}.          \tag{0.3}
\]

Upper profile stops control \(X_{S\cup\{a\}}\), but do not give a positive
lower bound on \(X_S\).  Therefore they do not imply
\(A_a/A=m^{-1+o(1)}u^{-1}=o(1)\).  A depleted link can have
\(A=A_a=1\), so the ratio is one while all absolute upper profile stops
hold.  Higher powers require either a lower corridor for every monitored
parent, or a cemetery/large-jump treatment when \(A_a/A\) is not small.

## 1. What the raw reverse sum proves

Fix a current raw link \(A=d_t(S)\), and put
\(A_a=d_t(S\cup\{a\})\).  For the diagonal term in which a selected edge
contains the exposed resource \(a\), its decrement is at most \(A_a\).
Therefore

\[
\begin{aligned}
 \nu_t\sum_g\sum_{a\in g}A_a^2
 &=\nu_t\sum_a d_t(a)A_a^2\\
 &\le {1\over r}\sum_aA_a^2.                             \tag{1.1}
\end{aligned}
\]

The same bound holds for compensation coins because
\(\chi_t(a)\le1/r\).  Thus

\[
 \text{raw diagonal}\le{2\over r}\sum_aA_a^2.            \tag{1.2}
\]

This is a useful hereditary inequality.  Its right side, however, has
the **parent** normalization.  A profile energy at order \(k+1\) normally
uses the child normalization.  Passing from one to the other produces
(0.1).

## 2. Exact conversion between parent and child energy

Let \(R=r-k\), and use

\[
 X_S={d_t(S)\over d_0(S)u^R},\qquad
 X_{S,a}={d_t(S\cup\{a\})\over d_0(S\cup\{a\})u^{R-1}}. \tag{2.1}
\]

Then

\[
 {A_a\over d_0(S)u^R}
 ={\rho_{S,a}\over u}X_{S,a}.                            \tag{2.2}
\]

Weight the parent square by its static incidence
\(q_k(S)=d_0(S)/D_0\).  The contribution of the \(a\)-diagonal from
(1.2), in parent units, is

\[
 {2\over r}\,q_k(S){\rho_{S,a}^2\over u^2}X_{S,a}^2.    \tag{2.3}
\]

The natural child square is

\[
 q_{k+1}(S\cup\{a\})X_{S,a}^2
 =q_k(S)\rho_{S,a}X_{S,a}^2.                            \tag{2.4}
\]

Dividing (2.3) by (2.4) gives exactly (0.1).  No stochastic or
asymptotic estimate is involved.

If an aggregate reversal of the parent-child sum counts a child through
at most \(P_k\) parents, the corrected coefficient is

\[
                         \delta_{k+1}(t)\le
 {2P_k\rho_k^*\over r u^2},                              \tag{2.5}
\]

where \(\rho_k^*=\max_{S,a}\rho_{S,a}\).  The factor \(P_k\) must be
recorded explicitly.  It is often polynomial in \(k\), but it is not
automatically one.

## 3. The cutoff arithmetic still works

Assume \(P_k\le J^{O(1)}\) and the additional bound (0.2).  Then

\[
 {1\over\theta}\int_0^T\delta_{k+1}(t)\,dt
 \le {2P_k\rho_k^*\over r\theta}\int_0^T u^{-2}\,dt.     \tag{3.1}
\]

Since \(dt=-r\,du/u\),

\[
 \int_0^T u^{-2}\,dt={r\over2}(z^{-2}-1),               \tag{3.2}
\]

and therefore

\[
 {1\over\theta}\int_0^T\delta_{k+1}(t)\,dt
 \le {P_k\rho_k^*z^{-2}\over\theta}
 =m^{-3/2+o(1)}.                                        \tag{3.3}
\]

Here \(z^{-2}=m(\log m)^{-2B_0}\),
\(\theta=\Theta(\sqrt{m\log m})\), and all powers of \(J\) are absorbed
in \(m^{o(1)}\).  Even one additional reversal factor \(r\) leaves
\(m^{-1/2+o(1)}\), still summable.

Thus the normalization correction is conceptually essential but
numerically favorable in the finite cutoff range whenever the required
conditional ratio bound is available.  For arbitrary equality-resolved
profiles, availability of that bound is itself part of the dynamic/static
diagonal gate.

## 4. A literal counterexample to the higher-power claim

The source note asserts that the existing child-profile stop gives

\[
                         b_*=\max_a{A_a\over A}=o(1).    \tag{4.1}
\]

This does not follow from upper stops.  Consider any active induced
residual in which the current \(S\)-link consists of one row \(f\), and
choose \(a\in f\setminus S\).  Then

\[
                         A=d_t(S)=1,\qquad A_a=1.        \tag{4.2}
\]

Both normalized profiles can lie far below every polylogarithmic upper
threshold, yet \(A_a/A=1\).  More generally, (0.3) shows that a small
\(X_S\) invalidates the claimed estimate even when \(X_{S,a}\) is under
its stop.

This arbitrary induced state is not asserted to occur before the actual
degree/whole-arm stops.  It is enough to refute the theorem's stated
pathwise, every-residual deduction.  To recover the intended trajectory
claim one must prove one of:

1. a lower profile corridor \(X_S\ge m^{-o(1)}\) whenever its powers are
   expanded;
2. an incidence-weighted quarantine of depleted parents before expansion;
3. a cemetery convention under which an event with \(A_a/A\) above a
   small threshold contributes only favorable terminal killing; or
4. a direct exponential diagonal moment bound which does not reduce all
   powers to the square by \(b_*=o(1)\).

## 5. Corrected theorem available now

The defensible replacement is:

> For profile orders \(k\le(\log m)^2\), under the conditional extension-ratio
> bound (0.2) and a polynomial parent-reversal multiplicity, the
> **quadratic** repeated-child diagonal has integrated geometric-weight
> coefficient \(o(1)\), uniformly down to the square-root density.

This discharges the square diagonal needed by a quadratic cutoff for
profile classes satisfying (0.2), including the exact low-order
consecutive spine.  It does not prove (0.2) for every equality-resolved
profile and does not discharge every higher repeated power in an
exponential Taylor majorant.  Those two issues retain the explicit
conditional-ratio and large-relative-jump gates.
