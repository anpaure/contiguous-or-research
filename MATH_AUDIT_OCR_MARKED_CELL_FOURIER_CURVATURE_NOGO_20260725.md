# Audit of the marked-cell Fourier-curvature no-go

Date: 2026-07-25

Audited report:
MATH_ATTACK_OCR_MARKED_CELL_FOURIER_CURVATURE_NOGO_20260725.md.

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

**Pass, with minor typographical repairs and one invariant-sector scope
qualification.**

The following formulas are exact:

\[
 P_q(y)=P_q\operatorname {diag}(y,1),
\]

\[
 \sigma(P_q(e^{i\theta}))=\left\{1,{q\over q+2}\right\},
\]

the piecewise spectral-radius formula (0.5), the local coefficient
\((q+1)/8\), the global curvature scale \(\Theta(1/q)\), and the identity

\[
 x^2C_q(x^2)C_{q-1}(x^2)\big|_{x=1/2}
 ={q\over q+2}.
\]

Thus the natural one-cell marking has no operator-norm contraction and
only critical \(1/q\)-scale global spectral curvature.

The scope qualification is this: the exact full-cell plateau obstructs an
actual marked PBBS operator if that cell sector is retained as an
invariant restriction, or if its source/sink compression is proved to
preserve the corresponding eigenmode.  Mere appearance as a
non-invariant subblock of a larger complex matrix does not by itself give
a spectral-radius lower bound, because complex off-block couplings can
alter eigenvalues.  The report's final “unless chronology cancels or
kills that sector” wording is consistent with this qualification.

## 1. Marking convention and singular values

Write

\[
 a={q+1\over q+2},\qquad
 b={1\over q+2},\qquad
 r=a-b={q\over q+2}.
\]

With rows indexed by the incoming endpoint and columns by the exit
endpoint, a dual exit consumes one dual separator and a forward exit
does not.  Marking the dual column gives

\[
 \boxed{
 P_q(y)
 =\begin{pmatrix}a&b\\b&a\end{pmatrix}
  \begin{pmatrix}y&0\\0&1\end{pmatrix}
 =\begin{pmatrix}ay&b\\by&a\end{pmatrix}.}
 \tag{1.1}
\]

For the column-vector convention the matrix is
\(\operatorname {diag}(y,1)P_q=P_q(y)^{\mathsf T}\), so its spectrum and
singular values agree with (1.1).

For \(|y|=1\), put \(D_y=\operatorname {diag}(y,1)\).  Then

\[
 P_q(y)^*P_q(y)=D_y^*P_q^2D_y.
\]

The eigenvalues of the symmetric matrix \(P_q\) are \(1,r\).  Hence

\[
 \boxed{\sigma_1(P_q(y))=1,\qquad
 \sigma_2(P_q(y))=r.}
 \tag{1.2}
\]

The singular values are independent of the Fourier phase.  In
particular, multiplying by a scalar attenuation \(\eta_q\) leaves

\[
 \|\eta_qP_q(e^{i\theta})\|_2=\eta_q
\]

for every \(\theta\).

## 2. Exact eigenvalues and spectral radius

For \(y=e^{i\theta}\),

\[
 \operatorname {tr}P_q(y)=a(1+y),\qquad
 \det P_q(y)=yr.
\]

Write

\[
 \lambda=e^{i\theta/2}\mu,\qquad
 c=\cos(\theta/2),\qquad
 u=|\sin(\theta/2)|.
\]

Since \(c\ge0\) on \([-\pi,\pi]\), the characteristic equation is

\[
 \mu^2-2ac\,\mu+r=0.
 \tag{2.1}
\]

Moreover

\[
 a^2c^2-r=b^2-a^2u^2.
\]

Therefore

\[
 \lambda_\pm(\theta)
 =e^{i\theta/2}
 \left(ac\pm\sqrt{b^2-a^2u^2}\right).
 \tag{2.2}
\]

If \(u\le b/a=1/(q+1)\), both bracketed roots are real and nonnegative,
and the plus root has the larger modulus.  If \(u>1/(q+1)\), they are
complex conjugates with product \(r\), so both have modulus \(\sqrt r\).
Consequently

\[
 \boxed{
 \rho_q(\theta)=
 \begin{cases}
 ac+\sqrt{b^2-a^2u^2},
 &u\le(q+1)^{-1},\\[2mm]
 \sqrt r,&u\ge(q+1)^{-1}.
 \end{cases}}
 \tag{2.3}
\]

At \(\theta=\pi\), the trace is zero and the eigenvalues are
\(\pm\sqrt r\).  Since the possible dual-exit increments are zero and
one, their span is one; \(\pi\) is not a lattice phase for this marking.

## 3. Local curvature

In the real-discriminant regime,

\[
 \begin{aligned}
 \rho_q(\theta)
 &=a\sqrt{1-u^2}+\sqrt{b^2-a^2u^2}\\
 &=1-\left({a\over2}+{a^2\over2b}\right)u^2
   +O\!\left({a^4\over b^3}u^4\right)\\
 &=1-{a\over2b}u^2+O(q^3u^4).
 \end{aligned}
\]

Because \(a/b=q+1\) and

\[
 u^2={\theta^2\over4}+O(\theta^4),
\]

one obtains

\[
 \boxed{
 \rho_q(\theta)
 =1-{q+1\over8}\theta^2+O(q^3\theta^4)}
 \tag{3.1}
\]

uniformly when \(|\theta|=o(1/q)\).  The coefficient and the error scale
in the source report are correct.

The discriminant vanishes at

\[
 |\theta|=2\arcsin{1\over q+1}
 ={2\over q}+O(q^{-2}),
\]

so the order-\(q\) infinitesimal curvature persists only on an
order-\(1/q\) arc.

## 4. Global curvature

When \(u\le1/(q+1)\),

\[
 \rho_q(\theta)
 \le a\sqrt{1-u^2}+b
 \le1-{a\over2}u^2.
\]

In the complementary regime,

\[
 1-\rho_q(\theta)=1-\sqrt r.
\]

For \(q\ge2\),

\[
 1-\sqrt r\le {a\over2}.
\]

It follows in both regimes that

\[
 1-\rho_q(\theta)
 \ge(1-\sqrt r)\sin^2(\theta/2).
\]

Since

\[
 \sin(|\theta|/2)\ge {|\theta|\over\pi}
 \qquad(-\pi\le\theta\le\pi),
\]

\[
 \boxed{
 \rho_q(\theta)
 \le\exp\left(
 -{1-\sqrt r\over\pi^2}\theta^2
 \right).}
 \tag{4.1}
\]

This provides \(c_q\ge c/q\).  Conversely, any estimate

\[
 \rho_q(\theta)\le e^{-c_q\theta^2}
\]

evaluated at \(\theta=\pi\) gives

\[
 \sqrt r\le e^{-c_q\pi^2},
\qquad
 \boxed{
 c_q\le-{1\over2\pi^2}\log r
 ={1+o(1)\over\pi^2q}.}
 \tag{4.2}
\]

Thus the optimal global scale is exactly \(\Theta(1/q)\).

For the finitely many cases \(q<2\), constants can be adjusted
separately; they do not affect the central \(q\asymp s\) statement.

## 5. Signed displacement

If a dual exit is marked by \(e^{-i\theta}\) and a forward exit by
\(e^{i\theta}\), then

\[
 P_q^\pm(e^{i\theta})
 =P_q\operatorname {diag}(e^{-i\theta},e^{i\theta}).
 \tag{5.1}
\]

Its singular values remain \(1,r\), and its characteristic equation is

\[
 \lambda^2-2a\cos\theta\,\lambda+r=0.
\]

This is the preceding calculation with \(\theta/2\) replaced by
\(\theta\), with one important lattice qualification: the permitted
phases are now both \(0\) and \(\pi\), because every one-step signed
increment is odd.  At \(\theta=\pi\), the spectral radius is one again,
not \(\sqrt r\).  The plateau \(\sqrt r\) holds away from neighbourhoods
of both permitted phases.

For \(n\) exits and \(N_D\) dual exits,

\[
 \Delta q=n-2N_D.
\]

Thus the dual-count and signed-displacement markings differ by a
deterministic phase and the stated half-angle change.

The source display (4.1) repeats the symbol
\(P_q^\pm(e^{i\theta})\); one copy should be deleted.

## 6. Renewal identity

The symmetric one-pair seam series is

\[
 \varrho_q(x)=x^2C_q(x^2)C_{q-1}(x^2).
\]

At \(x=1/2\),

\[
 \begin{aligned}
 \varrho_q(1/2)
 &={1\over4}
 {2(q+1)\over q+2}
 {2q\over q+1}\\
 &={q\over q+2}=r.
 \end{aligned}
\]

Also

\[
 \det P_q(y)=yr,\qquad
 \lambda_-(P_q(1))=r,\qquad
 \rho(P_q(-1))=\sqrt r.
\]

The high-frequency plateau is therefore exactly the square root of the
one-pair renewal mass, and

\[
 (1-r)^{-1}={q+2\over2}
\]

is both the anti-invariant relaxation scale and the scalar one-pair
renewal scale.  All identities in Section 5 of the source report pass.

## 7. Exact no-go scope

For the diagnostic operator

\[
 \mathsf R_q(y)=\eta_qP_q(y),
\qquad 1-\eta_q=\Theta(1/s),
\]

one has

\[
 \|\mathsf R_q(e^{i\theta})\|_2=\eta_q
\]

at every phase.  In any norm, the spectral-radius value at \(\pi\)
forces every global Gaussian estimate to have

\[
 c_s=O(1/q).
\]

For \(q\asymp s\), this is only the critical \(O(1/s)\) scale, not
\(c_s\gg1/s\).  Hence the automatic one-cell diffusion hypothesis from
the local-CLT route is rigorously unavailable.

This conclusion applies directly to the exact full-cell operator and to
any actual marked operator for which that sector survives as an
invariant restriction or has a source/sink compression retaining the
plateau mode.  For a larger non-invariant complex operator, an additional
argument is needed to transfer the two-state spectral lower bound to the
full spectrum.

The malformed tab characters in \(\theta\) and \(\text{ has
eigenvalues}\) in Section 2 are typographical only.

No coefficient-one conclusion follows from this audit.
