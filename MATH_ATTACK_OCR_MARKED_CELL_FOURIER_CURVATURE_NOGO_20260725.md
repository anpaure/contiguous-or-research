# The marked synchronized cell: exact Fourier spectrum and the renewal-scale curvature wall

Date: 2026-07-25  
Method: pure mathematics only; no computation or search

## 0. Outcome

Let

\[
 a_q={q+1\over q+2},\qquad b_q={1\over q+2},
 \qquad r_q=a_q-b_q={q\over q+2}.                  \tag{0.1}
\]

The critical full-cell transfer from
`MATH_ATTACK_OCR_SYNCHRONIZED_CELL_GREEN_NOGO_20260725.md` is

\[
 P_q=\begin{pmatrix}a_q&b_q\\b_q&a_q\end{pmatrix}.\tag{0.2}
\]

Order the exit states as dual and forward.  Mark every consumed dual
separator by (y), and leave a forward separator unmarked.  The exact
marked cell is

\[
 \boxed{
 P_q(y)=P_q\begin{pmatrix}y&0\\0&1\end{pmatrix}
 =\begin{pmatrix}a_qy&b_q\\b_qy&a_q\end{pmatrix}.}\tag{0.3}
\]

Using the transpose convention gives the same spectrum and singular
values.  For (y=e^{i\theta}), the following statements are exact.

1. The singular values of (P_q(e^{i\theta})) are independent of
   \(\theta\):

   \[
   \boxed{\sigma_1=1,\qquad\sigma_2=r_q.}           \tag{0.4}
   \]

   Thus there is no Fourier contraction at all in the ordinary
   \(\ell^2\) operator norm.

2. Put

   \[
   u=\left|\sin{\theta\over2}\right|,
   \qquad c=\cos{\theta\over2}\ge0
   \quad(-\pi\le\theta\le\pi).
   \]

   The spectral radius is

   \[
   \boxed{
   \rho_q(\theta)=
   \begin{cases}
   a_qc+\sqrt{b_q^2-a_q^2u^2},
     &u\le (q+1)^{-1},\\[3pt]
   \sqrt{r_q},&u\ge(q+1)^{-1}.
   \end{cases}}                                    \tag{0.5}
   \]

3. At the permitted phase zero,

   \[
   \rho_q(\theta)
   =1-{q+1\over8}\theta^2+O(q^3\theta^4)
   \qquad(|\theta|=o(1/q)).                        \tag{0.6}
   \]

   Hence the infinitesimal curvature is order (q), but it persists only
   on a Fourier arc of width order (1/q).

4. Outside that shrinking arc the spectral radius is the constant
   \(\sqrt{r_q}\).  In particular,

   \[
   \rho_q(\pi)=\sqrt{q\over q+2},
   \qquad
   1-\rho_q(\pi)={1\over q}+O(q^{-2}).              \tag{0.7}
   \]

   The best possible global spectral-curvature scale is therefore
   \(\Theta(1/q)\).  More precisely, a bound

   \[
   \rho_q(\theta)\le e^{-c_q\theta^2}
   \qquad(-\pi\le\theta\le\pi)                    \tag{0.8}
   \]

   is available with (c_q\ge c/q), while every such bound has

   \[
   \boxed{
   c_q\le-{1\over2\pi^2}\log r_q
   ={1+o(1)\over\pi^2q}.}                          \tag{0.9}
   \]

Thus for central unmatched height (q\asymp s), the exact synchronized
cell does **not** have curvature (c_s\gg1/s).  It has precisely the
critical scale (c_s=\Theta(1/s)).  No change of norm can evade (0.9),
because every operator norm is bounded below by spectral radius.

The relation with the old one-pair seam renewal is exact.  The symmetric
one-pair critical mass is

\[
 \varrho_q
 :=\left.x^2C_q(x^2)C_{q-1}(x^2)\right|_{x=1/2}
 ={q\over q+2}=r_q.                                \tag{0.10}
\]

Moreover,

\[
 \boxed{
 \det P_q(y)=y\varrho_q,
 \qquad
 \lambda_-(P_q(1))=\varrho_q,
 \qquad
 \rho(P_q(-1))=\sqrt{\varrho_q}.}                 \tag{0.11}
\]

Thus the high-frequency plateau is exactly the square root of the
one-recrossing-pair renewal mass.  The marked cell does not add a new
diffusive gain to that renewal; it is another representation of the same
critical persistence.

Consequently the block-diffusion hypothesis in Section 5 of
`CONSTANT_ONE_FOCUSED_FRONTIER_20260725.md` cannot be proved from the
full-cell transfer alone.  Actual PBBS chronology would have to modify the
marked transfer itself: it must remove the unit singular mode or create a
uniform high-frequency gap not present in (0.5).  No coefficient-one
conclusion is claimed here.

## 1. Exact marking and singular values

In the synchronized parser, exiting through the dual endpoint consumes
one dual-block separator and changes

\[
 (p,j,q)\longmapsto(p,j-1,q-1).
\]

Exiting through the forward endpoint consumes no dual separator and
changes

\[
 (p,j,q)\longmapsto(p-1,j,q+1).
\]

Therefore column marking of the dual exit gives (0.3).  If column vectors
are used instead, the marked matrix is the transpose of (0.3), which does
not affect any calculation below.

For (|y|=1), put (D_y=\operatorname{diag}(y,1)).  Since (D_y) is
unitary,

\[
 P_q(y)^*P_q(y)=D_y^*P_q^2D_y.                     \tag{1.1}
\]

The eigenvalues of the real symmetric matrix (P_q) are (1,r_q).
Hence the eigenvalues of (1.1) are (1,r_q^2), proving (0.4).

This is stronger than the absence of a convenient Euclidean estimate:
the marked operator is obtained from the unmarked stochastic operator by
a unitary column phase, so phase marking cannot decrease its largest
singular value.

## 2. Exact eigenvalues on the unit circle

The marked trace and determinant are

\[
 \operatorname{tr}P_q(y)=a_q(1+y),
 \qquad
 \det P_q(y)=y(a_q^2-b_q^2)=yr_q.                 \tag{2.1}
\]

Write (y=e^{i\theta}) and

\[
 \lambda=e^{i\theta/2}\mu,
 \qquad c=\cos(\theta/2).
\]

The characteristic equation becomes

\[
 \mu^2-2a_qc\mu+r_q=0.                            \tag{2.2}
\]

Since

\[
 a_q^2c^2-r_q
 =b_q^2-a_q^2\sin^2(\theta/2),                    \tag{2.3}
\]

the two eigenvalues are

\[
 \boxed{
 \lambda_\pm(\theta)
 =e^{i\theta/2}
 \left(
 a_qc\pm
 \sqrt{b_q^2-a_q^2\sin^2(\theta/2)}
 \right).}                                        \tag{2.4}
\]

If (u\le b_q/a_q=1/(q+1)), the square root is real and the plus root has
the larger modulus.  If (u>b_q/a_q), the two bracketed roots are complex
conjugates with product (r_q), hence both have modulus (sqrt{r_q}).
This proves (0.5).

At (	heta=\pi), the trace vanishes and

\[
 P_q(-1)	ext{ has eigenvalues }\pm\sqrt{r_q}.     \tag{2.5}
\]

This phase is not a lattice phase for the dual-block count: both zero and
one dual exits occur in the transfer, so the displacement span is one.

## 3. Local and global curvature

For (u<(q+1)^{-1}), expand (0.5):

\[
 \begin{aligned}
 \rho_q(\theta)
 &=a_q\sqrt{1-u^2}+\sqrt{b_q^2-a_q^2u^2}\\
 &=1-{a_q\over2b_q}u^2+O(q^3u^4)\\
 &=1-{q+1\over8}\theta^2+O(q^3\theta^4).
 \end{aligned}                                     \tag{3.1}
\]

This proves (0.6).  The discriminant changes sign when

\[
 |\theta|=2\arcsin{1\over q+1}
 ={2\over q}+O(q^{-2}),                            \tag{3.2}
\]

after which (0.5) is exactly flat.

For a global lower bound on the spectral gap, first suppose
(u\le(q+1)^{-1}).  Then

\[
 \rho_q(\theta)
 \le a_q\sqrt{1-u^2}+b_q
 \le1-{a_q\over2}u^2.                             \tag{3.3}
\]

In the complementary regime,

\[
 1-\rho_q(\theta)=1-\sqrt{r_q}.                    \tag{3.4}
\]

For (q\ge2), one has (1-\sqrt{r_q}\le a_q/2).  Therefore

\[
 1-\rho_q(\theta)
 \ge(1-\sqrt{r_q})\sin^2(\theta/2).               \tag{3.5}
\]

As (sin(|\theta|/2)\ge|\theta|/\pi) on
([-\pi,\pi]),

\[
 \rho_q(\theta)
 \le\exp\left(
 -{1-\sqrt{r_q}\over\pi^2}\theta^2
 \right).                                         \tag{3.6}
\]

This supplies curvature of order (1/q).  Conversely, evaluation at
(	heta=\pi) in (0.8) gives

\[
 \sqrt{r_q}\le e^{-c_q\pi^2},
\]

which is exactly (0.9).  Hence the optimal global scale is
(\Theta(1/q)).

## 4. The signed-displacement convention

Sometimes the unmatched-height displacement is marked rather than the
number of dual exits.  A forward exit contributes (+1) and a dual exit
contributes (-1), giving

\[
 P_q^{\pm}(e^{i\theta})
 =P_q\operatorname{diag}(e^{-i\theta},e^{i\theta}).\tag{4.1}
\]

Its singular values are again (1,r_q).  Its characteristic equation is

\[
 \lambda^2-2a_q\cos\theta\,\lambda+r_q=0.          \tag{4.2}
\]

Thus (0.5) holds with (	heta/2) replaced by (	heta).  The permitted
lattice phases are now (0) and (pi), because every one-step signed
displacement is odd.  Away from those phases, the same plateau
(sqrt{r_q}) and the same global (\Theta(1/q)) curvature scale remain.
For a fixed number (n) of separator exits,

\[
 \Delta q=n-2N_D,
\]

so dual-count and signed-displacement marking are equivalent up to a
deterministic phase and the half-angle change already visible above.

## 5. Exact renewal identity and implication

For a symmetric seam of total height (2q), marked between heights
(q-1,q), the scalar extra-crossing-pair series is

\[
 \varrho_q(x)=x^2C_q(x^2)C_{q-1}(x^2).             \tag{5.1}
\]

At the critical point,

\[
 \begin{aligned}
 \varrho_q(1/2)
 &={1\over4}
   {2(q+1)\over q+2}
   {2q\over q+1}\\
 &=\frac q{q+2}=r_q.                               \tag{5.2}
\end{aligned}
\]

Combining (2.1), (2.5), and (5.2) proves (0.11).  In particular, the
anti-invariant relaxation time

\[
 (1-r_q)^{-1}={q+2\over2}                          \tag{5.3}
\]

is exactly the one-pair renewal scale.  The strong local curvature in
(0.6) is the usual persistent-walk variance accumulated only after this
mixing time.  At frequencies outside the (1/q) central arc, the same
renewal persistence leaves modulus (sqrt{r_q}).

Suppose, as in the natural scalar-renewal model, a one-pair marked
operator has the form

\[
 \mathsf R_q(y)=\eta_qP_q(y),
 \qquad 1-\eta_q=\Theta(1/s).                      \tag{5.4}
\]

Then

\[
 \|\mathsf R_q(e^{i\theta})\|_2=\eta_q             \tag{5.5}
\]

for every \(\theta\), so no Euclidean Fourier curvature exists.  In any
other norm, spectral radius and (0.7) force every uniform estimate

\[
 \|\mathsf R_q(e^{i\theta})\|
 \le\eta_qe^{-c_s\theta^2}                         \tag{5.6}
\]

to have (c_s=O(1/q)).  When (q\asymp s), this is only (O(1/s)),
not the (c_s\gg1/s) needed for the proposed local-limit closure.

The factorization (5.4) is a diagnostic model, not an assertion that the
complete PBBS one-pair operator is scalar times one cell.  Its rigorous
content is the obstruction: an actual operator for which the exact
full-cell sector is invariant (or passes to a genuine quotient/restriction)
inherits the spectral plateau (0.5), unless additional chronology cancels
or kills that sector.  Mere occurrence as a non-invariant matrix subblock
does not by itself give a complex-phase spectral lower bound.

## 6. Exact remaining statement

The marked-cell calculation closes the proposed *automatic diffusion*
lane.  The common carrier does not become sufficiently diffusive merely
because dual-block displacement is marked.  The exact residual theorem
must be stronger:

> **PBBS high-frequency anti-persistence lemma (unproved).**  After the
> four external one-crossing kernels are fixed, the actual literal
> one-pair transfer has a uniform nonlattice spectral gap larger than the
> full-cell value (1-\sqrt{q/(q+2)}=\Theta(1/s)), or its physical source
> and sink vectors have vanishing projection on the plateau modes.

Either alternative must use complete inter-time PBBS chronology.  It is
not a consequence of height caps, separator synchronization, or the
scalar one-pair renewal identity.

No coefficient-one conclusion follows.
