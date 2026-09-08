# The consecutive-gap Hilbert trace and the fibrewise-mean gate

Date: 2026-07-27

Scope: the equality-resolved consecutive-profile face in the compensated
promotion-frame process.  All calculations below are finite and exact.  The
result is a theorem about the candidate multidimensional propagation
operator, not a proof of coefficient one.

## 0. Outcome

The positive one-index obstruction does not say that every genuinely
multidimensional calculation diverges.  On the fully labelled consecutive
tree, the unnormalised counting-space Hilbert kernel is exactly

\[
 \lambda_k:=\|K_k\|_{2\to2}^2
 =\begin{cases}
 \displaystyle
 {\alpha_k^2\over(m-k)^3},&2\le k<H,\\[2mm]
 \displaystyle
 {\alpha_k^2\over m-k},&H\le k<m,
 \end{cases}
 \qquad
 \alpha_k={r-k-1\over r-k}.
 \tag{0.1}
\]

Consequently, if \({\cal T}\le C m\log m\), then the complete
time-ordered squared-kernel series satisfies

\[
 \boxed{
 \sum_{\ell=2}^{m}{\mathcal T^{\ell-2}\over(\ell-2)!}
 \bigl\|K_2K_3\cdots K_{\ell-1}\bigr\|_{2\to2}^2
 =1+o(1).}
 \tag{0.2}
\]

Thus the exact consecutive spine is not, by itself, an
initialization/trace obstruction to a history-resolved *quadratic* Duhamel
energy whose generator really closes with the squared kernel in (0.1).
That dynamic closure is not proved here.  This does not contradict the
positive Perron no-go: (0.2) uses the growth in the number of labelled gap
states and time ordering, whereas coefficientwise positive absorption asks
each level separately to pay a factor \({\cal T}\).

The missing point is also exact.  Marginal compensation leaves a linear
protected-common-event source.  Before any Hilbert estimate can apply, that
source must have negligible conditional mean on every child fibre.  Global
mean zero is insufficient.  The smallest post-collar gate is therefore a
fibrewise common-event-column cancellation, stated in Section 4.

## 1. The labelled continuation tree

Let \(\Omega_k\) be the labelled one-shore consecutive states of profile
order \(k\).  A state \(\omega\in\Omega_k\) has exactly

\[
 b_k=m-k
 \tag{1.1}
\]

children, obtained by exposing one of its unresolved coordinate labels.
Every child has a unique parent after the complete ordered history is
retained.

Let \(\Gamma_k\) be the normalized mass of one prescribed consecutive
profile.  The audited exact ratios are

\[
 \rho_k:={\Gamma_{k+1}\over\Gamma_k}
 =\begin{cases}
 \displaystyle {\alpha_k\over(m-k)^2},&k<H,\\[2mm]
 \displaystyle {\alpha_k\over m-k},&H\le k<m.
 \end{cases}
 \tag{1.2}
\]

Define

\[
 (K_kf)(\omega)
 =\rho_k\sum_{\eta\in\operatorname{Ch}(\omega)}f(\eta),
 \qquad f:\Omega_{k+1}\to\mathbb R.
 \tag{1.3}
\]

Both shore orientations give a direct sum of two copies of (1.3), so all
norm identities below remain unchanged.

## 2. Exact Hilbert singular values

### Theorem 2.1 (one-step and multistep norm)

Equip every \(\Omega_k\) with unnormalised counting measure.  Then

\[
 \boxed{K_kK_k^*=b_k\rho_k^2 I,}
 \tag{2.1}
\]

and hence (0.1) holds.  More generally, for \(2\le k<\ell\le m\),

\[
 \boxed{
 \bigl\|K_kK_{k+1}\cdots K_{\ell-1}\bigr\|_{2\to2}^2
 = (m-k)_{\ell-k}
   \left({\Gamma_\ell\over\Gamma_k}\right)^2
 =\prod_{j=k}^{\ell-1}\lambda_j.}
 \tag{2.2}
\]

#### Proof

The child sets of two distinct labelled parents are disjoint.  Every row of
\(K_k\) has exactly \(b_k\) entries, all equal to \(\rho_k\).  Its distinct
rows are orthogonal, proving (2.1).  Substitution of (1.2) gives (0.1).

A level-\(k\) state has exactly \((m-k)_{\ell-k}\) labelled descendants at
level \(\ell\), and every descendant coefficient in the product is
\(\Gamma_\ell/\Gamma_k\).  Descendant sets of distinct initial states are
again disjoint.  The same row-orthogonality argument proves the first
equality in (2.2); the second is the telescoping product of (2.1). \(\square\)

With uniform probability measures, write

\[
 K_k=b_k\rho_kP_k,
\]

where \(P_k\) is conditional expectation along one child fibre and
\(\|P_k\|_{2\to2}=1\).  Thus the probability-space norm of \(K_k\) is
\(b_k\rho_k\), whereas its counting-space norm is
\(\sqrt{b_k}\rho_k\).  The difference in (0.1) is dimension growth, not a
spectral gap: the Markov part \(P_k\) has a large norm-one inherited
subspace.

## 3. The full time-ordered trace is summable

### Theorem 3.1 (quadratic spine summability)

Suppose

\[
 H=(1+o(1))\sqrt{m\log m},
 \qquad r\ge m+1,
 \qquad {\cal T}\le C m\log m
 \tag{3.1}
\]

for fixed \(C\).  Then (0.2) holds.  More precisely, the contribution from
\(\ell\ge H\) is at most

\[
 \exp[-(5/2-o(1))H\log m].
 \tag{3.2}
\]

#### Proof

For \(2\le k<H\),

\[
 \lambda_k\le(m-H)^{-3}.
 \tag{3.3}
\]

Thus the terms with \(2\le\ell\le H\), excluding the initial term, sum to
at most

\[
 \exp\!\left({\mathcal T\over(m-H)^3}\right)-1=o(1).
 \tag{3.4}
\]

Put \(h=m-H\).  For \(j\ge0\), the post-collar part of the product ending
at \(\ell=H+j\) is at most

\[
 {1\over(h)_j},
 \tag{3.5}
\]

because every \(\alpha_k\le1\).  Also

\[
 (H-2+j)!\ge(H-2)!j!,
 \qquad (h)_j\ge j!.
 \tag{3.6}
\]

It follows that the whole tail is at most

\[
 (m-H)^{-3(H-2)}
 {\mathcal T^{H-2}\over(H-2)!}
 \sum_{j=0}^{h}{\mathcal T^j\over j!(h)_j}
 \le
 (m-H)^{-3(H-2)}
 {\mathcal T^{H-2}\over(H-2)!}e^{2\sqrt{\mathcal T}}.
 \tag{3.7}
\]

For the last inequality, use

\[
 \sum_{j\ge0}{x^j\over(j!)^2}\le e^{2\sqrt x},
 \tag{3.8}
\]

which follows by retaining the diagonal terms in
\(e^{\sqrt x}e^{\sqrt x}\).  Stirling's formula and (3.1) make the logarithm
of (3.7)

\[
 -3H\log m+H\log({\cal T}/H)+O(H)+2\sqrt{\cal T}
 =-(5/2-o(1))H\log m.
 \tag{3.9}
\]

Equations (3.4) and (3.7) prove (0.2). \(\square\)

## 4. Why compensation does not yet feed this Hilbert trace

For a protected resource profile \(S\), marginal compensation leaves the
exact normalized source

\[
 \nu J(S),
 \qquad
 J(S)=\sum_e(|e\cap S|-1)_+.
 \tag{4.1}
\]

For a protected link and one row remainder, the one-new-resource part is

\[
 \mathcal B_1(S)
 =\sum_{y\notin S}a_S(y)d(S\cup\{y\}),
 \qquad
 a_S(y)=|\{e:y\in e,\ e\cap S\ne\varnothing\}|.
 \tag{4.2}
\]

Every coefficient in (4.2) is nonnegative.  Thus neither shore reversal nor
the compensation coins turn (4.2) into the squared kernel (0.1).

To avoid changing the earlier order indexing silently, put
\(\widetilde\Omega_g:=\Omega_{m-g}\) for \(0\le g\le m-H\).  Let
\(p_g:\widetilde\Omega_{g-1}\to\widetilde\Omega_g\) delete the last
exposed label, let

\[
 (P_gf)(\omega)={1\over g}\sum_{x\in G(\omega)}
 f(\omega\mathbin{\frown}x),
 \tag{4.3}
\]

and let \(U_gh=h\circ p_g\).  Then

\[
 P_gU_g=I.
 \tag{4.4}
\]

Hence even a globally mean-zero child source can pass without attenuation
when it is inherited from its parent.

The raw source (4.2) cannot itself satisfy a zero-mean statement: on a
one-sided spine every summand is nonnegative, and the diagonal
\(e=f\) gives a genuine positive example.  Thus the smallest exact
cancellation statement must include a physical terminal/common-event credit,
not merely a relabelling of (4.2).

> **Augmented fibrewise common-event coboundary (unproved).**  After retaining
> the common-event column and all equality types, construct a predictable
> signed credit \(C_{g-1}\), supported on literal terminal kills or selected
> common-event incidences, such that its initial, final, and discarded
> boundary ledger is \(o(W)\).  The adjusted source
> \[
> B_{g-1}:=\mathcal B_{1,g-1}
>       +(\partial_t+\mathcal L_t)C_{g-1}
> \]
> satisfies, for every \(1\le g\le m-H\),
> \[
> {1\over g}\sum_{x\in G(\omega)}
> B_{g-1}(t,\omega\mathbin{\frown}x)=0
> \tag{FCC}
> \]
> for every live parent \(\omega\) and every \(t\).  Every physical child
> incidence, including equality/common-event multiplicity, is replicated
> before this uniform average is taken.  Without that replication,
> \(g^{-1}\sum_x\) is replaced by the exact weighted transition kernel.

Under exact (FCC), the credit telescopes and the linear \(+1\) source is
killed before a positive part is taken.  The remaining quadratic fluctuation
is the natural place where Theorem 3.1 could apply.  No such physical credit,
and no dynamic covariance inequality reducing the full catalogue to (0.1),
is currently known.

A strictly weaker approximate alternative would have to bound the complete
chronological propagation of the nonzero conditional means, summed over both
shores, all orders, parents, and replicated incidences, by \(o(W)\).  A
one-step or global-mean estimate is not sufficient over the full time
horizon; no such normalized Duhamel bound is asserted here.

## 5. Adversarial audit

Theorem 3.1 is unconditional but concerns only the labelled consecutive
face.  It does not control nonconsecutive gap compositions, repeated
physical equalities, or different histories ending at the same physical
profile.  Those effects may increase both row and column norms.

The positive Perron obstruction remains valid for every coefficientwise
positive level-by-level absorption.  The Hilbert calculation avoids that
hypothesis, so it does not refute the obstruction.

Finally, marginal compensation does not prove (FCC); raw (FCC) is false.
Equation (4.2) has strictly positive one-sided examples, and the
common/difference shore decomposition only transfers their variance into the
symmetric mode.  A proof of the *augmented* FCC would have to use cancellation
between distinct common-event-column terms or a global terminal-kill
telescope, with its boundary ledger proved to be \(o(W)\).  Without such an
identity, the rigorous alternative remains a trajectory-specific cutoff
before order \(H\).
