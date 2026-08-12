# Audit of the two-dimensional renewal local-CLT gate

Date: 2026-07-25

Audited report:
PBBS_TWO_DIMENSIONAL_RENEWAL_LOCAL_CLT_GATE_20260725.md.

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

The scalar renewal lemma, the abstract matrix Fourier theorem, the
Gaussian-band arithmetic, the curvature threshold, and the record-depth
moment estimate are correct after minor typographical repairs.

The claimed reduction of the remaining PBBS problem to one Fourier
contraction is **conditional, not established**.  Four logically
independent physical statements are still missing:

1. a coefficientwise, length-preserving factorization separating the
   external four one-crossing kernels from one copy of the outer carrier;
2. a homogeneous additive one-pair operator
   \(\mathsf R_s(y)\), despite the actual synchronized cells depending on
   the changing state \((j,q)\);
3. uniformly bounded **aggregate** source and sink norms after summing
   over the \(\Theta(s)\) possible source blocks;
4. either one prescribed block displacement \(d\), or a proved weighted
   summation over all physically possible \(d\)'s.

Consequently the report proves a useful sufficient Fourier theorem and a
precise conditional route.  It does not prove that the PBBS block-diffusion
lemma is the sole remaining assertion, and it does not yet imply the
zero-winding contribution to \(QST_A\).

## 1. Scalar renewal lemma

Let

\[
 \rho_s(y)=r_s\sum_jp_s(j)y^j,
 \qquad \sum_jp_s(j)=1,
\]

with nonnegative coefficients and

\[
 {c_0\over s}\le1-r_s\le{C_0\over s}.
 \tag{1.1}
\]

For all sufficiently large \(s\), this implies \(0\le r_s<1\).
The displacement coefficient in the renewal resolvent is

\[
 G_s(d)=\sum_{k\ge0}r_s^kp_s^{*k}(d).
\]

Under

\[
 \sup_d p_s^{*k}(d)\le {C\over\sqrt{k+1}},
 \tag{1.2}
\]

one has

\[
 \begin{aligned}
 G_s(d)
 &\le C\sum_{k\ge0}{e^{-c_0k/s}\over\sqrt{k+1}}\\
 &\le C'\left(1+\int_0^\infty
 e^{-c_0x/s}x^{-1/2}\,dx\right)
 =O(\sqrt s).
 \end{aligned}
\]

This proof is exact.  Periodicity causes no problem if (1.2) is assumed;
it merely changes the constant on the permitted lattice.

The displayed assumption (1.4) in the source is missing a TeX backslash
before \(\le\); this is only a typographical error.

## 2. Abstract matrix Fourier theorem

Assume throughout that the norm is an induced Hilbert-space operator norm.
The hypotheses

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_se^{-c_1\theta^2}
 \quad(|\theta|\le\theta_0)
 \tag{2.1}
\]

and

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_s(1-c_2)
 \quad(\theta_0\le|\theta|\le\pi)
 \tag{2.2}
\]

imply \(\|\mathsf R_s(e^{i\theta})\|<1\) uniformly on the unit circle.
Thus the Neumann series for

\[
 (I-\mathsf R_s(e^{i\theta}))^{-1}
\]

converges uniformly, and its Fourier coefficients agree with the
Laurent coefficients of the resolvent.  Fourier inversion is therefore
legitimate.

For \(|\theta|\le\theta_0\),

\[
 \begin{aligned}
 1-r_se^{-c_1\theta^2}
 &=(1-r_s)+r_s(1-e^{-c_1\theta^2})\\
 &\ge c\bigl(s^{-1}+\theta^2\bigr),
 \end{aligned}
\]

after reducing \(\theta_0\) if necessary.  Hence

\[
 \|(I-\mathsf R_s(e^{i\theta}))^{-1}\|
 \le {C\over s^{-1}+\theta^2}.
 \tag{2.3}
\]

The exact integral is

\[
 \int_{-\theta_0}^{\theta_0}
 {d\theta\over s^{-1}+\theta^2}
 =2\sqrt s\,\arctan(\theta_0\sqrt s)
 =O(\sqrt s).
 \tag{2.4}
\]

On the complementary arc, (2.2) gives a uniform \(O(1)\) resolvent.
Therefore

\[
 \left|[y^d]\langle u,(I-\mathsf R_s(y))^{-1}v\rangle\right|
 \le C\sqrt s\,\|u\|\|v\|.
 \tag{2.5}
\]

Theorem 2.1 is correct.

The proper-lattice sentence following the theorem needs its usual
uniformity clause: the number of peripheral phases must be bounded
independently of \(s\), with the same quadratic curvature and a uniform
gap off fixed neighbourhoods of those phases.  If the number of phases
grows, their \(O(\sqrt s)\) contributions must also be counted.

### 2.1 The norm hypothesis is not the natural PBBS Fourier hypothesis

The exact synchronized full-cell transition is

\[
 \mathbf P_q={1\over q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix}.
 \tag{2.6}
\]

Order the endpoints as dual and forward.  A dual exit decreases the
dual-block index by one, while a forward exit leaves that index fixed.
Marking the block displacement therefore gives, up to replacing \(y\)
by \(y^{-1}\),

\[
 \mathbf P_q(y)
 =\mathbf P_q
 \begin{pmatrix}y&0\\0&1\end{pmatrix}.
 \tag{2.7}
\]

For \(|y|=1\), the diagonal matrix in (2.7) is unitary.  Since
\(\mathbf P_q\) is symmetric stochastic,

\[
 \boxed{\|\mathbf P_q(e^{i\theta})\|_2
 =\|\mathbf P_q\|_2=1}
 \tag{2.8}
\]

for every \(\theta\).  After a scalar renewal attenuation \(r_s\), the
norm is identically \(r_s\).  Hence neither

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_se^{-c_1\theta^2}
\]

nor the uniform high-frequency norm gap can hold for this natural
one-cell tilt in the reversible Euclidean norm.

This does not rule out Fourier diffusion.  The spectral radius of the
tilted matrix can curve below one even though its largest singular value
does not.  It shows that the PBBS Fourier statement must instead control
the leading analytic eigenvalue and its spectral projection, a suitable
multi-step product, or the resolvent directly:

\[
 \|(I-\mathsf R_s(e^{i\theta}))^{-1}\|
 \le {C\over s^{-1}+c_s\theta^2}.
 \tag{2.9}
\]

Thus (2.1)--(2.2) are a correct sufficient assumption, but they are not
the natural “exact remaining PBBS assertion” claimed in Section 4 of the
source.

## 3. Weaker curvature and the exact threshold

Suppose (2.1) is replaced near zero by

\[
 \|\mathsf R_s(e^{i\theta})\|
 \le r_se^{-c_s\theta^2},
 \tag{3.1}
\]

while the high-frequency gap remains uniform.  Then

\[
 \int_{-\theta_0}^{\theta_0}
 {d\theta\over s^{-1}+c_s\theta^2}
 =O\!\left(\min\left\{s,\sqrt{s/c_s}\right\}\right).
 \tag{3.2}
\]

With uniformly bounded source and sink norms, this is \(o(s)\) exactly
when

\[
 sc_s\longrightarrow\infty,
\]

that is, \(c_s\gg s^{-1}\).  The threshold in the source report is
correct.

If the product of the source and sink norms is \(M_s\), the actual
condition becomes

\[
 M_s\sqrt{s/c_s}=o(s),
\qquad\text{equivalently}\qquad
 {M_s^2\over sc_s}\longrightarrow0.
 \tag{3.3}
\]

Thus the stated \(c_s\gg s^{-1}\) threshold cannot be used before the
uniform boundary-norm hypothesis is proved.

## 4. Gaussian-band arithmetic

The audited one-crossing kernel obeys

\[
 \sup_n2^{-n}[x^n]K^\times_{s,t,u}(x)=O(s^{-6})
\]

for deterministic central \(t,u\).  If a nonnegative synchronized
transfer series for one prescribed displacement has critical mass
\(O(\sqrt s)\), convolution gives the fixed-height bound

\[
 O(4^m s^{-6}\sqrt s)
 =O(4^m s^{-11/2}).
 \tag{4.1}
\]

On a fixed Gaussian band there are \(O(\sqrt m)\) choices of \(s\), and
\(s\asymp\sqrt m\).  Therefore

\[
 \sum_sO(4^m s^{-11/2})
 =O(4^m m^{1/2}m^{-11/4})
 =O(4^m m^{-9/4}).
 \tag{4.2}
\]

Since

\[
 B_m\asymp4^m m^{-3/2},
\]

the last expression is

\[
 O(B_m/m^{3/4})
 =o(B_m/\sqrt m).
 \tag{4.3}
\]

All exponents in Section 3 of the source are correct.

This arithmetic applies only after one has a nonnegative,
coefficientwise factorization whose length variable \(x\) counts every
physical bit once.  A Fourier estimate at \(x=1/2\) does not construct
that factorization.

## 5. Why the actual PBBS implication does not yet follow

### 5.1 The exact carrier is inhomogeneous

In the audited synchronized-cell description, a full cell has state
\((j,q)\), and its critical transition is

\[
 \mathbf P_q
 ={1\over q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix}.
 \tag{5.1}
\]

A forward separator sends \(q\) to \(q+1\); a dual separator sends \(q\)
to \(q-1\), and in the latter case \(j\) also changes.  The caps and the
available interval depend on the current \(j,q\).

This is a finite inhomogeneous acyclic automaton, not a power of one
translation-invariant matrix Laurent polynomial
\(\mathsf R_s(y)\).  A homogeneous one-pair representation may exist
after enlarging the state space, but it is not supplied in the source
report.  If the enlarged state includes \(j\), marking \(j\) again by a
Laurent exponent is redundant unless the additive decomposition is
defined explicitly.

Even after such a representation is supplied, subsection 2.1 shows that
one-step operator-norm curvature is generally the wrong target.  The
leading Perron eigenvalue or a block product must be analyzed.

### 5.2 The displacement is not globally fixed

Theorem 2.1 bounds one coefficient \(d\).  A physical boundary word has a
well-defined record depth or terminal block index, but the set of all
roots contains many possible values of that index.  The endpoint
identities do not presently prescribe one common \(d\) for the entire
enumerated class.

Summing the uniform estimate (2.5) over \(D_s\) possible displacements
costs a factor \(D_s\).  If \(D_s=\Theta(s)\), the resulting bound is
\(O(s^{3/2})\), not \(o(s)\).  Therefore one must prove either:

\[
 \text{one fixed displacement after conditioning on the external data},
\]

or a weighted estimate

\[
 \sum_d w_{s,d}
 \left|[y^d]\langle u,\mathsf G_s(y)v\rangle\right|
 =o(s)
\]

with the actual PBBS weights \(w_{s,d}\).

### 5.3 Aggregate boundary norms are not known to be bounded

For one source block \(h\), the exact internal endpoint vector has
order-one norm.  But the synchronized capped relaxation has
\(\Theta(s)\) possible central source blocks.  In their natural direct
sum, a vector carrying order-one amplitude on each orthogonal source
state has norm \(\Theta(\sqrt s)\), not \(O(1)\).

The exact external normalization does not automatically remove this
issue.  The high-dual prefix product is

\[
 {1\over s-h},
\]

which is a bounded nonzero multiple of the ordinary external
first-passage mass \(A_{s-h-1}(1/2)=1/(s-h)\).  After that ordinary
kernel is factored out, the synchronized source still has order-one
coupling to the invariant mode.

Likewise, for the physical sink with \(p=s-L\),
\[
 \mathsf K_{p,L}^{\rm sink}(1/2)
 ={4(p-L+1)\over(p+1)(p+2)}
\]

has a ratio bounded above and below by positive constants relative to
the ordinary \(G_{s-1}(1/2)\) factor on the central corner range.
Therefore the external kernels do not provide an unrecorded vanishing
boundary norm.

A special weighted Hilbert norm might normalize the aggregate boundary
vectors, but the Fourier operator inequalities (2.1)--(2.2) must then be
proved in that same norm.  Rescaling the norm is not free.

### 5.4 Disjoint rank reconstruction remains open

The identity

\[
 |\mathcal A R_0|=2m-1
\]

does count the common carrier \(O\) once.  It does not yet split the
remaining \(2m-|O|\) bits into the four independent one-crossing kernels
and a synchronized transfer series.  Without such an injection, the
product

\[
 K^\times_{s,t,u}(x)\Psi_s(x)
\]

can duplicate \(O\) or omit external constraints.

These four points show that the PBBS application in Section 3 is a valid
conditional implication under its bullet assumptions, but Section 4
cannot call Fourier curvature the sole remaining assertion.

## 6. Record-depth moment and Hadamard weighting

For a balanced word \(e\) of length \(2\ell\), let

\[
 h(e)=-\min_{0\le j\le2\ell}\operatorname{net}(e[1,j]).
\]

Layer cake and reflection give

\[
 \begin{aligned}
 \sum_eh(e)
 &=\sum_{a\ge1}\#\{e:h(e)\ge a\}\\
 &=\sum_{a=1}^{\ell}\binom{2\ell}{\ell+a}\\
 &={4^\ell-\binom{2\ell}{\ell}\over2}
 <4^\ell.
 \end{aligned}
 \tag{6.1}
\]

Thus Lemma 5.1 is correct; in fact the reflection count is an equality
before endpoint restrictions.

If each of the two point probabilities is at most \(C4^{-\ell}\), then

\[
 \begin{aligned}
 &\sum_{e\ {\rm balanced}}h(e)
 \Pr(U[1,2\ell]=e)
 \Pr(V[|V|-2\ell+1,|V|]=e)\\
 &\qquad\le C^2\,16^{-\ell}\sum_eh(e)
 \le C'4^{-\ell}.
 \end{aligned}
 \tag{6.2}
\]

The weighted Hadamard estimate is correct.  The double
\(\boxed{\boxed{\cdot}}\) and malformed \({\rm balanced}\) text in the
source display (5.3) are typographical errors.

This estimate alone does not sum the Fourier coefficients over physical
displacements.  It weights record depth under the **boundary collision
law**, while Theorem 2.1 controls a coefficient of a proposed renewal
operator.  A theorem identifying these two distributions, with all
external conditioning retained, is still required.

## 7. Corrected theorem boundary

The following statement is proved:

> If actual PBBS roots admit a length-preserving coefficientwise
> factorization into the central four-kernel chart and a homogeneous
> additive matrix renewal; if the external data fix one displacement (or
> supply a controlled displacement sum); if the aggregate boundary
> vectors have uniformly bounded norm; and if the renewal operator has
> quadratic Fourier curvature \(c_s\gg s^{-1}\) with a uniform
> high-frequency gap, then the zero-winding Gaussian-band contribution is
> \(o(B_m/\sqrt m)\).

What is not proved is that actual PBBS roots satisfy those structural
hypotheses.  The exact next theorem must combine the physical
inhomogeneous \((j,q)\) automaton, its boundary vectors, and the
record-depth collision law in one coefficientwise estimate.

No coefficient-one conclusion follows from the present local-CLT gate.
