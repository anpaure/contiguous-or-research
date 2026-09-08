# Audit of the compensated \(+2\) cutoff: the repeated-child \(+1\) diagonal

Date: 2026-07-27

Scope: `MATH_REDUCTION_COMPENSATED_PLUS_TWO_LOGSQUARED_CUTOFF_20260727.md`.

## 0. Verdict

The finite-cutoff arithmetic is viable, but the displayed hypothesis
\((\mathrm{CG}_J)\) is not the exact compensated generator.  Exact
physical compensation removes the *linear* one-child mean.  It does not
remove the quadratic variation of a jump supported on one new physical
resource.

The missing orbit is elementary.  A compensation coin at \(a\notin S\)
deletes

\[
                         B_a=d_t(S\cup\{a\})             \tag{0.1}
\]

rows from the \(S\)-link.  In any quadratic/exponential Taylor energy,
the positive remainder contains

\[
                         \chi_t(a)B_a^2.                 \tag{0.2}
\]

The same term is produced by a selected external edge which meets the
displayed link through the single resource \(a\).  Algebraically \(a\)
occurs twice, but the physical support is only \(S\cup\{a\}\).  Equality
resolution cannot turn it into two distinct resources.

Therefore the correct generator has the form

\[
 (\mathcal G\mathscr E)_s^+
 \le \delta_{s+1}\mathscr E_{s+1}
 +\sum_{\substack{\ell\ge2\\s+\ell\le J}}
 A^\ell\kappa_{s+\ell}^{\ell-1}\mathscr E_{s+\ell}
 +\mathscr B_s^{(J)},                                   \tag{CG'\(_J\)}
\]

where \(\delta_{s+1}\) is an \(L^2\), repeated-child diagonal
coefficient.  It is not the raw \(L^1\) coefficient from the consecutive
spine.  The proposed cutoff still closes if

\[
 \boxed{
 \mathcal T\max_{t\le J}\delta_t/\theta=o(1).}          \tag{0.3}
\]

For example, either
\(\delta_t\le C t^4/m^2\) or even
\(\delta_t\le C t^4/m\) suffices when
\(J=(\log m)^2\) and
\(\theta=\Theta(\sqrt{m\log m})\).

Thus the note does not yet prove a compensated finite cutoff, but its
architecture survives a precise repair.  The new exact gate is the
equality-resolved repeated-child diagonal bound (0.3), plus the already
stated distinct-child \(+2\) estimates.

## 1. The explicit \(+1\) physical orbit

Let \(A=d_t(S)\) be a displayed link count, and let an event supported on
one new resource \(a\) change it by \(A\mapsto A-B_a\).  For the square
energy,

\[
 (A-B_a)^2-A^2=-2AB_a+B_a^2.                            \tag{1.1}
\]

Compensation calibrates the aggregate first-order term \(-2AB_a\) against
the survival reference.  The term \(B_a^2\) is nonnegative and belongs to
the predictable bracket.  Independent compensation clocks cannot supply
a negative quadratic variation with which to cancel it.

Expanding the square does not increase physical support:

\[
 B_a^2=B_a(B_a-1)+B_a.                                  \tag{1.2}
\]

The first term counts ordered pairs of distinct rows, both containing
the same protected set \(S\cup\{a\}\); the second is the row diagonal.
Both have physical profile order \(|S|+1\).  Consequently neither
falling-factorial expansion nor equality resolution places (1.2) in an
\(s+2\) profile.

In carré-du-champ notation, for any normalized observable \(X_S\),

\[
 \boldsymbol\Gamma_t(X_S)
 =\sum_e\lambda_e(\Delta_eX_S)^2
  +\sum_a\chi_t(a)(\Delta_aX_S)^2.                       \tag{1.3}
\]

Every summand is nonnegative.  The one-resource summands in the second
sum are precisely the orbit omitted from \((\mathrm{CG}_J)\).

## 2. Relation to exact child centering

The repeated-child diagonal does not restore the scalar no-go.  With

\[
 p_{S,a}={q_{s+1}(S\cup\{a\})
                \over(r-s)q_s(S)},
 \qquad
 X_S={d_t(S)\over d_0(S)u^{r-s}},                        \tag{2.1}
\]

one has pathwise

\[
 \sum_a p_{S,a}X_{S\cup\{a\}}=uX_S.                    \tag{2.2}
\]

Thus the raw \(L^1\) one-child mean is exactly canceled.  The residual
quantity is the conditional variance

\[
 V_S=\sum_a p_{S,a}
        (X_{S\cup\{a\}}-uX_S)^2.                        \tag{2.3}
\]

Equation (0.2) is an unnormalized version of the diagonal part of (2.3).
It is governed by squared child weights, not by their sum.

For the post-\(H\) consecutive spine, writing
\(R=r-s\), \(g=m-s\), each of the \(g\) regular continuations has
probability

\[
                         {R-1\over R^2g},                \tag{2.4}
\]

and their total probability is \((R-1)/R^2\le1/R\).
Hence this particular repeated-child diagonal is contracting; it does
not have the raw order-one coefficient of the scalar spine note.

The danger in \((\mathrm{CG}'_J)\) can only come from a different
equality-resolved child orbit or from a broad event column.  This is a
finite, polylogarithmic-order census problem.

### 2.1 The compensation-coin diagonal is directly bounded

The coin orbit itself is not the hard part once static normalization is
kept.  Write

\[
 \rho_{S,a}={q_{s+1}(S\cup\{a\})\over q_s(S)}
            =(r-s)p_{S,a},
 \qquad \rho_* =\max_a\rho_{S,a}.                        \tag{2.5}
\]

A coin at \(a\) changes the normalized parent profile by

\[
 |\Delta_aX_S|
 ={\rho_{S,a}\over u}X_{S\cup\{a\}}.                   \tag{2.6}
\]

Since \(\chi_t(a)\le1/r\), its complete pointwise bracket is bounded by

\[
\begin{aligned}
 \sum_a\chi_t(a)(\Delta_aX_S)^2
 &\le {1\over r u^2}
       \sum_a\rho_{S,a}^2X_{S\cup\{a\}}^2\\
 &\le {\rho_*\over r u^2}
       \sum_a\rho_{S,a}X_{S\cup\{a\}}^2.               \tag{2.7}
\end{aligned}
\]

Thus the coin diagonal has the required \(+1\) form with coefficient
\(\rho_*/(ru^2)\) against the natural child square score.  Even after a
polylogarithmic parent-multiplicity loss, the static higher-codegree
bound \(\rho_*\le Ct^4/m^2\), \(t\le J\), makes it summable.

Indeed, using \(dt=-r\,du/u\), its weighted integrated coefficient is at
most

\[
 {1\over\theta}\int_0^T {\rho_*\over u^2}\,dt
 \le {\rho_* r\over2\theta z^2}
 =m^{-1/2+o(1)}                                          \tag{2.8}
\]

for \(z=m^{-1/2}(\log m)^{B_0}\), uniformly through
\(t\le(\log m)^2\).  (Keeping the extra \(1/r\) in (2.7) only improves
this estimate; (2.8) deliberately allows the losses from reversing the
aggregate parent-child sum.)

The unresolved repeated-child orbit is therefore the **selected-edge
column diagonal**: one selected edge can meet many different rows of the
same \((S,a)\)-link.  Bounding

\[
 {1\over r\Delta_t}\sum_g B_{S,a}(g)^2                 \tag{2.9}
\]

requires the actual equality-resolved whole-arm/column breadth estimate.
It is not supplied by marginal compensation or by (2.7).

## 3. The corrected cutoff arithmetic

Multiply order \(s\) by \(\theta^s\) and integrate for time
\(\mathcal T\).  The repeated-child term entering the coefficient of
\(\theta^{s+1}\mathscr E_{s+1}\) is

\[
                         \mathcal T\delta_{s+1}/\theta.  \tag{3.1}
\]

This proves the sufficient condition (0.3).  If

\[
                         \delta_t\le {Ct^4\over m^2},    \tag{3.2}
\]

then, uniformly for \(t\le J=(\log m)^2\),

\[
 {\mathcal T\delta_t\over\theta}
 \le {C(\log m)^8\sqrt{m\log m}\over m^2}
 =m^{-3/2+o(1)}.                                        \tag{3.3}
\]

Even the weaker bound \(\delta_t\le Ct^4/m\) gives

\[
                         {\mathcal T\delta_t\over\theta}
                         =m^{-1/2+o(1)}.                 \tag{3.4}
\]

Thus the diagonal orbit falsifies the literal \(+2\)-only statement but
does not threaten the numerical cutoff if its natural squared-codegree
bound is proved dynamically.

The internal \(\ell\ge2\) absorption in the original note is otherwise
correct: with \(\theta=2A\sqrt{\mathcal T}\),

\[
 \mathcal T A^\ell\theta^{-\ell}
 =2^{-\ell}\mathcal T^{1-\ell/2}.                       \tag{3.5}
\]

## 4. Terminal arithmetic corrections

Two typographical/arithmetic corrections do not alter the leading
terminal exponent.

First,

\[
 {\theta J^2\over m}
 =m^{-1/2}(\log m)^{9/2+o(1)},                           \tag{4.1}
\]

not \(m^{-1/2}(\log m)^{5/2+o(1)}\).  Nevertheless,

\[
 J\log\!\left({C\theta J^2\over m}\right)
 =-\left({1\over2}-o(1)\right)(\log m)^3,               \tag{4.2}
\]

so the claimed leading exponent remains valid.

Second, the terminal union cannot merely be asserted to have
``polynomially many marked types.''  Equality partitions and ordered
histories on \(J\) labels contribute at most
\(\exp[O(J\log J)]\), which is harmless compared with (4.2).  If the
chosen diagram grammar permits arbitrary graphs on the \(J\) labels,
however, it can have \(\exp[\Theta(J^2)]\) types and the displayed
terminal estimate does not pay that union.  The final cutoff theorem
must either:

1. sum terminal profiles directly in one aggregate energy; or
2. prove the relevant type count is \(\exp[O(J\log J)]\).

This is a secondary audit item, independent of the repeated-child
diagonal.

## 5. Corrected boundary

The exact finite theorem still needed is

\[
 \boxed{
 \begin{array}{l}
 \text{For every equality-resolved column--row and compensation orbit}\
 \text{of total order }t\le(\log m)^2,\text{ the repeated-child}\
 \text{diagonal obeys }\delta_t\le m^{-1+o(1)},\text{ and the}\
 \text{distinct-child terms obey the stated }\kappa_t\text{ hierarchy.}
 \end{array}}                                           \tag{5.1}
\]

Under (5.1), the geometric cutoff works with room.  Without the first
clause, \((\mathrm{CG}_J)\) is false even in the one-resource
compensation orbit.
