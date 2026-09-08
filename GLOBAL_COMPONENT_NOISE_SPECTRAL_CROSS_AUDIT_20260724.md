# Spectral cross-audit of `GLOBAL_COMPONENT_NOISE_MINIMIZER_RAW_20260724.md`

## 1. Verdict

The switching identities (3)--(5), the quadratic floor, and the global
minimizer argument are correct.  The transposition spectral constant in
(6) is not sharp after the exact zero point margins are used.

For every covered nontrivial rank,

\[
\boxed{
\sum_{\tau\ {\rm transposition}}
\|f-\tau f\|_2^2
\ge 4(n-1)\|f\|_2^2.
}
\tag{S}
\]

The coefficient \(4(n-1)\) is sharp on the ambient zero-point-margin
Johnson module.  The report's \(2n\) is the coefficient obtained when only
the constant component is removed and degree one is still allowed.  Exact
wreath-factor loads have no degree-one component.

Put

\[
B_H:=\sum_{q=1}^H\frac{V_q^{\min}}{c_q},
\qquad
\Phi_H(F):=\sum_{q=1}^H
\frac{V_q(F)-V_q^{\min}}{c_q},
\]

and

\[
\mathcal O_H(F):=\sum_{q=1}^H\frac{O_q(F)}{c_q}.
\]

At a global minimizer \(F\), the corrected exact consequence is

\[
\boxed{
\mathcal O_H(F)
\le
\frac{R_H(F)}{8(n-1)}
-\frac12B_H.
}
\tag{28 corrected}
\]

Consequently the corrected sufficient criterion is

\[
\boxed{
R_{H_m}(F_m)
\le
4(n-1)B_{H_m}+o(nW).
}
\tag{29 corrected}
\]

It yields \(\mathcal O_{H_m}(F_m)=o(W)\).

The proposed \(2nB_H\) is not the exact baseline.  Indeed the same proof
gives the universal minimizer lower bound

\[
\boxed{
R_H(F)\ge4(n-1)\bigl(B_H+\Phi_H(F)\bigr)
\ge4(n-1)B_H.
}
\tag{F}
\]

Thus an exact upper bound \(R_H\le2nB_H\) is impossible whenever
\(B_H>0\) and \(n>2\).  With an added \(o(nW)\) error it can be formally
compatible only when \(B_H=o(W)\), in which case the error term is absorbing
the missing

\[
\bigl(4(n-1)-2n\bigr)B_H=2(n-2)B_H.
\]

That does not make \(2nB_H\) the spectral floor.  The forced sharp spectral
baseline is \(4(n-1)B_H\).

Attainment inside the exact-factor fibre is a separate, unproved issue.
Equality at \(4(n-1)B_H\) requires simultaneous floor-balanced rank loads,
pure Johnson degree two, and equality in every component-switching
minimality comparison.  The spectrum shows that the coefficient cannot be
improved using only zero point margins; it does not produce an exact factor
attaining all equality conditions.

No search, numerical experiment, or solver output is used in this audit.

## 2. Exact zero point margins

Fix \(q\), write

\[
r=m-q,\qquad
\Omega_r=\binom{[n]}r,\qquad
g_q=\mu_q(F)-a_q\mathbf1.
\]

An exact factor has \(W/n\) wreaths.  In one wreath, exactly \(r\) cyclic
rank-\(r\) intervals contain a fixed coordinate \(x\).  Therefore

\[
\sum_{\substack{S\in\Omega_r\\x\in S}}\mu_q(F)(S)
=\frac{rW}{n}.
\tag{2.1}
\]

The constant profile has the same point margin:

\[
a_q\binom{n-1}{r-1}
=\frac{W}{N_q}\frac{rN_q}{n}
=\frac{rW}{n}.
\tag{2.2}
\]

Subtracting gives

\[
\sum_{S\ni x}g_q(S)=0
\qquad(x\in[n]).
\tag{2.3}
\]

For \(r>0\), summing (2.3) over \(x\) also gives

\[
\sum_S g_q(S)=0.
\]

Let \(U_r\) be the point-incidence map

\[
(U_rf)(x)=\sum_{S\ni x}f(S).
\]

The image of \(U_r^\ast\) consists of the constant and degree-one
functions

\[
S\longmapsto c+\sum_{x\in S}b_x.
\]

Equivalently, it is the Johnson subspace \(E_0\oplus E_1\).  Equation
(2.3) says \(U_rg_q=0\), so

\[
\boxed{
g_q\in\bigoplus_{j\ge2}E_j.
}
\tag{2.4}
\]

This is the extra information omitted in the use of (6).  Zero total alone
would remove only \(E_0\) and leave the degree-one eigenvalue \(n\).

When \(r=1\), (2.3) forces \(g_q=0\) outright.  Thus the endpoint rank does
not create an exception to the corrected inequality.

## 3. The transposition Dirichlet form

Let

\[
L_r=\sum_{\tau\ {\rm transposition}}(I-T_\tau)
\]

on functions on \(\Omega_r\).  At a set \(S\), transpositions with both
points in \(S\) or both outside \(S\) act trivially.  The remaining
transpositions replace one point of \(S\) by one point outside it.  Hence
\(L_r\) is exactly the combinatorial Laplacian of the Johnson graph
\(J(n,r)\):

\[
(L_rf)(S)
=\sum_{\substack{x\in S\\y\notin S}}
\bigl(f(S)-f(S-\{x\}+\{y\})\bigr).
\tag{3.1}
\]

The Johnson Laplacian eigenvalue on \(E_j\) is

\[
\lambda_j=j(n-j+1),
\qquad 0\le j\le r.
\tag{3.2}
\]

Because \(r\le m=(n-1)/2\), the eigenvalues are increasing over the
relevant range:

\[
\lambda_{j+1}-\lambda_j=n-2j>0
\qquad(j<r).
\]

After (2.4), the first allowed eigenvalue is therefore

\[
\lambda_2=2(n-1).
\tag{3.3}
\]

For an orthogonal transposition action,

\[
\begin{aligned}
\sum_\tau\|f-\tau f\|_2^2
&=2\sum_\tau\langle f,(I-T_\tau)f\rangle\\
&=2\langle f,L_rf\rangle.
\end{aligned}
\tag{3.4}
\]

Combining (2.4), (3.3), and (3.4) gives

\[
\sum_\tau\|g_q-\tau g_q\|_2^2
\ge 2\lambda_2\|g_q\|_2^2
=4(n-1)V_q(F).
\tag{3.5}
\]

This proves (S).  Equality in (3.5) holds exactly when the nonzero vector
lies in \(E_2\).  Since \(E_2\) exists for \(2\le r\le n-2\), the
coefficient \(4(n-1)\) is sharp on the ambient zero-margin space.

### Consistency with the audited heat multiplier

There are \(\binom n2=n(n-1)/2\) transpositions.  Dividing (3.5) by this
number gives

\[
\mathbb E_\tau\|g_q-\tau g_q\|_2^2
\ge\frac8n\|g_q\|_2^2.
\tag{3.6}
\]

For the heat projection \(P_\tau=(I+T_\tau)/2\),

\[
\|P_\tau g_q\|_2^2
=\|g_q\|_2^2-\frac14\|g_q-\tau g_q\|_2^2.
\]

Thus

\[
\mathbb E_\tau\|P_\tau g_q\|_2^2
\le\left(1-\frac2n\right)\|g_q\|_2^2.
\tag{3.7}
\]

This is exactly the degree-two contraction used in the audited RFEN
analysis.  The raw coefficient \(2n\) would instead give only
\(1-1/(n-1)\), revealing the same missing degree-one cancellation.

## 4. Propagation through global minimality

For one transposition \(\tau\), define

\[
A_{\tau,H}(F)
:=\sum_{q=1}^H
\frac{\|\mu_q(F)-\tau\mu_q(F)\|_2^2}{c_q},
\]

\[
N_{\tau,H}(F)
:=\sum_{C\in\mathcal C_\tau(F)}
\sum_{q=1}^H
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\]

The fair switching identity is exact.  Every component-side choice is an
integral exact factor, so global minimality implies

\[
A_{\tau,H}(F)\le N_{\tau,H}(F)
\qquad\text{for every transposition }\tau.
\tag{4.1}
\]

Summing (4.1) gives

\[
R_H(F)\ge\sum_\tau A_{\tau,H}(F).
\tag{4.2}
\]

The constant vector cancels under a permutation, so (3.5) applies rank by
rank:

\[
\begin{aligned}
\sum_\tau A_{\tau,H}(F)
&=\sum_{q=1}^H\frac1{c_q}
\sum_\tau\|g_q-\tau g_q\|_2^2\\
&\ge4(n-1)\sum_{q=1}^H\frac{V_q(F)}{c_q}.
\end{aligned}
\tag{4.3}
\]

Since

\[
\sum_q\frac{V_q(F)}{c_q}=B_H+\Phi_H(F),
\]

(4.2)--(4.3) prove the floor inequality (F):

\[
R_H(F)\ge4(n-1)\bigl(B_H+\Phi_H(F)\bigr).
\tag{4.4}
\]

This is stronger than merely changing a coefficient in the upper bound:
it identifies the unavoidable component-noise floor at every global
minimizer.

The rankwise quadratic floor gives

\[
2O_q(F)\le V_q(F)-V_q^{\min}.
\]

After division by \(c_q\) and summation,

\[
2\mathcal O_H(F)\le\Phi_H(F).
\tag{4.5}
\]

Rearranging (4.4) gives

\[
\Phi_H(F)
\le\frac{R_H(F)}{4(n-1)}-B_H.
\tag{4.6}
\]

Combining (4.5) and (4.6) proves the sharp corrected form of (28):

\[
\boxed{
\mathcal O_H(F)
\le
\frac{R_H(F)-4(n-1)B_H}{8(n-1)}
=\frac{R_H(F)}{8(n-1)}-\frac12B_H.
}
\tag{4.7}
\]

The right side is automatically nonnegative by (4.4).

If, for a sequence of minimizers \(F_m\),

\[
R_{H_m}(F_m)
\le4(n-1)B_{H_m}+\varepsilon_m,
\qquad
\varepsilon_m=o(nW),
\tag{4.8}
\]

then

\[
\mathcal O_{H_m}(F_m)
\le\frac{\varepsilon_m}{8(n-1)}
=o(W).
\]

Equation (4.8) is the sharp corrected form of (29).

## 5. Baseline and attainability

The phrase “baseline” has two distinct meanings which should not be
conflated.

### 5.1 Forced spectral baseline

From (4.4),

\[
R_H(F)\ge4(n-1)B_H
\]

for every global minimizer.  This is an exact theorem.  Therefore
\(2nB_H\) lies below the forced floor by

\[
2(n-2)B_H.
\]

If \(B_H>0\), the exact value \(2nB_H\) is unattainable for \(n>2\).
If \(B_H=0\), both formal baselines vanish.

An estimate

\[
R_H(F)\le2nB_H+o(nW)
\]

is not automatically contradictory because its unspecified error may
dominate \(2(n-2)B_H\).  Combining it with the lower bound forces
\(B_H=o(W)\).  In that regime the statement has merely hidden the missing
spectral floor in its error term and is not the sharp cancellation
criterion needed in (28).

### 5.2 Actual equality in the exact-factor fibre

The coefficient in (S) is spectrally sharp, but equality in the full floor
\(R_H=4(n-1)B_H\) requires all of the following:

1. \(V_q(F)=V_q^{\min}\) at every weighted rank;
2. every nonzero centered load \(g_q\) lies entirely in \(E_2\);
3. equality holds after summing every minimizer switching inequality
   \(A_{\tau,H}\le N_{\tau,H}\).

The first condition is already simultaneous positive floor/ceiling
feasibility across the window.  The second is not automatic for a balanced
integer profile, and the third is a component-geometry condition.  No
result in the raw note proves that an exact factor satisfies them.

Thus \(4(n-1)B_H\) is the sharp baseline forced by the available invariants,
but actual attainment in the exact-factor fibre remains open and may fail.
For the sufficient criterion, one only needs component noise within
\(o(nW)\) above that floor.

## 6. Scope relative to RFEN

The corrected minimizer criterion and RFEN use the same degree-two
transposition spectrum, but they control different objects and have
different quantifiers.

RFEN\(_A\), in its all-factor form, says that for every exact factor the
expected accumulated rankwise remainder along an iid-uniform transposition
word of length

\[
T_0=\lceil n\log2\rceil
\]

is bounded by a multiple of the current collision energy plus a
Catalan-scale error.  It is annealed over the random word; after freezing a
good word, an integral leaf is selected and the estimate can be iterated.

The present criterion:

* is imposed only at one global minimizer for the chosen window;
* sums the one-step component noise over every transposition at that same
  factor;
* uses no random word, accumulated remainder, or iterative contraction; and
* concludes directly from the minimum principle.

A minimizer-only RFEN hypothesis is also sufficient, but it remains a
different inequality: RFEN bounds a sequential remainder relative to the
current excess energy, whereas (29 corrected) bounds an absolute
one-step-all-transpositions noise sum relative to the floor \(B_H\).
Component decompositions change along an RFEN word, so neither bound is a
formal consequence of the other.

The common multiplier \(1-2/n\) in RFEN is precisely equivalent to the
\(4(n-1)\) Dirichlet constant through (3.6)--(3.7).  This agreement is an
independent normalization check on the correction.

## 7. Scope relative to \(HG_L\)

For one overlay \(F,\sigma F\), \(HG_L\) compares coherent displacement
\(A_H(F,\sigma)\) with component noise \(V_H(F,\sigma)\) and asks, for every
factor, for some permutation satisfying

\[
A_H(F,\sigma)-V_H(F,\sigma)
\ge\eta_L\Psi_H(F)-C_LH\operatorname{Cat}_m.
\]

That is an all-factor positive heat-gap statement.  It yields a legal
one-step contraction and can be iterated.  The permutation may be nonlocal;
it is not restricted to one transposition.

At a global minimizer, the fair component switch gives the opposite
one-transposition inequality

\[
A_{\tau,H}(F)\le N_{\tau,H}(F)
\]

for every transposition.  The corrected global criterion does not seek a
positive one-step heat gap there.  It sums these nonpositive gaps and asks
that the total component-noise side be only \(o(nW)\) above its unavoidable
degree-two spectral floor.

Therefore:

* all-factor \(HG_L\) is stronger in its factor quantifier and supplies a
  descent mechanism away from a minimizer;
* the corrected global criterion is minimizer-only and supplies no
  contraction for arbitrary factors;
* \(HG_L\) may use one general permutation, while the corrected criterion
  averages every coordinate transposition; and
* no implication between their unproved structural estimates is currently
  established.

Both are sufficient routes to the same fixed-window overload conclusion
once their respective imported diagonalization steps are supplied.  Neither
is proved by continuous smoothing alone, and neither is a necessary
characterization of MWB.

## 8. Final ledger

- **Exact component switching:** accepted.
- **Quadratic floor \(2O_q\le V_q-V_q^{\min}\):** accepted.
- **One-switch expectations (3)--(4):** accepted.
- **Minimizer inequality (5):** accepted.
- **Raw spectral coefficient \(2n\):** valid without point-margin
  cancellation but nonsharp and inappropriate here.
- **Correct coefficient:** \(4(n-1)\), sharp on the zero-point-margin
  Johnson space.
- **Proposed baseline \(2nB_H\):** below the forced spectral floor whenever
  \(B_H>0\).
- **Correct forced baseline:** \(4(n-1)B_H\); exact-factor attainment is not
  proved.
- **Corrected (28):**
  \[
  \mathcal O_H(F)\le
  \frac{R_H(F)}{8(n-1)}-\frac12B_H.
  \]
- **Corrected (29):**
  \[
  R_{H_m}(F_m)\le4(n-1)B_{H_m}+o(nW).
  \]
- **RFEN comparison:** same degree-two spectral normalization, different
  sequential remainder and word quantifiers.
- **\(HG_L\) comparison:** different all-factor heat-gap criterion; no
  proved implication in either direction.
- **Global scope:** the component-noise excess estimate remains unproved,
  and no new proof of MWB is obtained.
