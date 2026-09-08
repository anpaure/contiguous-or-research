# Audit of the shared-boundary collision theorem

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

The proof in `PBBS_SHARED_BOUNDARY_COLLISION_20260725.md` is valid.  In
particular, the conditional coefficient anti-concentration

\[
 \sup_n\Pr\{X=n\}=O(s^{-2})
\]

survives conditioning on the common balanced boundary word.  There is no
lost normalization factor and no hidden independence assumption.

Consequently the proved coefficient-one advance is genuine:

\[
 \#\{\hbox{zero-winding starts}:s\le A\sqrt r,
       \ 0<\Lambda\le2L\}
 =o_A(B_r/\sqrt r)
\]

whenever

\[
 L\log r=o(r^{1/5}).
\]

The audit also identifies the exact boundary of this argument.  The
shared-word factor \(4^{-\ell}\) is cancelled by the increase
\(4^\ell\) in the capped-array partition function.  The surviving gain is
only polynomial.  The two inactive-core enclosure decks do not supply an
additional local factor: the explicit canonical gap-five component in
`PBBS_BRACKETING_ORDER_LOCAL_OBSTRUCTION_20260725.md` simultaneously
saturates a positive fraction of both decks while their joint endpoint
order is asymptotically FIFO.  Any further gain must use the actual
inter-time \(\tau\)-compatibility of the full forward/dual arrays, or a
global packing/fusion theorem.

## 1. Prefix probability

Let \(e\) be a balanced word of length \(2\ell\), and put

\[
 h=-\min_{0\le t\le2\ell}\operatorname{net}(e[1,t]).
\]

The record-minimum parsing

\[
 e=(0D_1)\cdots(0D_{h-1})0P
\]

is unique.  Under \(3\ell<s-2\), the encountered caps really are

\[
 \ell+1,\ell+2,\ldots,\ell+h.
\]

Indeed the block met at record depth \(i\) is \(S_{s-i}\), whose cap is

\[
 \min\{s-i,i+\ell\}=i+\ell
\]

because \(i\le h\le\ell\) and \(s>3\ell+2\).

For the partial final block, the total fair-walk weight of all Dyck
completions of its prescribed prefix is at most twice the fair-walk weight
of the prefix.  The complete preceding blocks contribute their normalized
Boltzmann weights.  Since

\[
 \sum_i|D_i|+|P|=2\ell-h
\]

and

\[
 \prod_{i=1}^{h-1}C_{\ell+i}(1/4)^{-1}
 =2^{-(h-1)}\frac{\ell+h+1}{\ell+2},
\]

the powers of two cancel to give

\[
 \Pr\{U[1,2\ell]=e\}\le C4^{-\ell}.
\]

Reversing the dual word gives the identical estimate there.  Summing the
product over at most

\[
 \binom{2\ell}{\ell}=O(4^\ell/\sqrt{\ell+1})
\]

balanced words proves the Hadamard collision factor

\[
 O\!\left(4^{-\ell}/\sqrt{\ell+1}\right).
\]

## 2. The truncated product after conditioning

Conditioning on \(E=e\) fixes the complete forward blocks

\[
 S_{s-1},\ldots,S_{s-h+1}
\]

and a prefix of \(S_{s-h}\).  It does not touch

\[
 S_1,\ldots,S_{s-h-1}.
\]

Those blocks remain mutually independent and independent of the partial
completion and of the dual array.  Their partition function is exactly

\[
 P_{s,\ell,h}(z)
 =\prod_{j=1}^{s-h-1}
 C_{\min\{j,s-j+\ell\}}(z).
\]

In the range \(h\le\ell\ll s\), its cap sequence rises to the central
cap and then falls to \(\ell+h+1\).  Direct cancellation of
\(C_j=Q_j/Q_{j+1}\) gives

\[
 P_{s,\ell,h}(z)
 =\frac{Q_{\ell+h+1}(z)}{Q_U(z)Q_V(z)},
 \qquad |U-V|\le1,
 \quad U+V=s+\ell+1.
\]

Thus the numerator index is at most \(2\ell+1=o(s)\), while
\(U,V=\Theta(s)\).

## 3. The \(s^{-2}\) atom bound

At \(z=e^{it}/4\), put

\[
 x=\sqrt{1-e^{it}},\qquad \Re x\ge0.
\]

The exact formula for \(Q_j\) gives

\[
 \frac{|Q_{\ell+h+1}(e^{it}/4)|}
      {Q_{\ell+h+1}(1/4)}
 \le \exp((\ell+h+1)|x|).
\]

After removing a harmless monomial, the reciprocal denominator is either
the path kernel \(H_U=C_U-C_{U-1}\), or that kernel times one normalized
\(C\)-factor of modulus at most one.  Its characteristic function obeys

\[
 |\varphi_{H_U}(t)|\le
 \begin{cases}
 1,&U|x|\le1,\\
 C(U|x|)^2e^{-cU|x|},&U|x|\ge1.
 \end{cases}
\]

Since \(\ell+h+1=o(U)\), the numerator is absorbed in the second
region.  The first region has width \(O(U^{-2})\), because
\(|x|\asymp\sqrt{|t|}\); the integral over the second region is also
\(O(U^{-2})\).  Therefore

\[
 \int_{-\pi}^{\pi}|\varphi_{P_{s,\ell,h}}(t)|^2dt
 =O(s^{-2}).
\]

Fourier inversion gives the claimed largest atom.  Adding the independent
partial-block completion and dual semilength is convolution and cannot
increase that atom.  Finally, mixing over \(e\) preserves the same bound.

## 4. Coefficient ledger

The common-boundary collision probability and the conditional atom bound
give

\[
 z_{r,s,2\ell}
 \le
 C4^{r-s+\ell}s^{-2}
 \frac{4^{-\ell}}{\sqrt{\ell+1}}
 F_{s,\ell}(1/4)^2.
\]

The exact telescope

\[
 4^{-(s-\ell)}F_{s,\ell}(1/4)^2
 \le C\frac{4^\ell(\ell+2)^2}{s^4}
\]

then yields

\[
 \boxed{
 z_{r,s,2\ell}
 \le C4^r\frac{(\ell+2)^2}
 {s^6\sqrt{\ell+1}}.}
\]

Summing above
\(s_0=\lfloor\sqrt{r/(K\log r)}\rfloor\) gives

\[
 C4^r\frac{L^{5/2}(\log r)^{5/2}}{r^{5/2}},
\]

which is \(o(B_r/\sqrt r)\) under
\(L\log r=o(r^{1/5})\).  The spectral low-height deletion below
\(s_0\) is already \(o(B_r/\sqrt r)\).

## 5. Exact remaining issue

The cancellation

\[
 \underbrace{4^{-\ell}}_{\text{literal common word}}
 \times
 \underbrace{4^\ell}_{\text{extra cap entropy}}
 =1
\]

is real.  Merely repeating the same boundary-word argument cannot remove
the residual large-overlap sector.  Moreover, unsigned or endpoint-order
use of the two inactive cores cannot help locally: both core decks can be
simultaneously utilized at positive density with only \(O(r)\) inversions
among \(\Theta(r^2)\) endpoint pairs.

The surviving zero-winding problem is therefore:

> Prove that among pairs of capped arrays satisfying the common-boundary
> condition, only an \(o(1)\) fraction satisfy the complete
> \(\tau\)-chronology linking every \(S_j\), every \(T_j\), and the
> endpoint factorization; or prove an equivalent global trace-clustering
> statement after quotient edge-disjointness is imposed.

This is strictly narrower than the original PBBS packing gate, but it is
not proved here.
