# Positive Ferrers boundaries are exponentially thin Wallis residues; one clean collar cannot bundle two flag tasks

**Date:** 2026-08-07  
**Status:** unconditional arithmetic characterization, sparsity theorem,
and local no-bundling theorem.  These results do not prove
\(4h\le m-1\) in every sufficiently large positive-boundary dimension.
They identify that assertion as a sharp exponentially thin residue
problem.

## 1. Parity-unified notation

Put

\[
 C_m=\binom{2m}{m},
 \qquad
 A_m=\frac{4^m}{2C_m}.
\tag{1.1}
\]

For odd and even dimensions use

\[
\begin{array}{c|c|c|c}
 k&W&\eta&x_m\\ \hline
 2m-1&C_m/2&0&A_m\\
 2m&C_m&1/2&A_m-1/2.
\end{array}
\tag{1.2}
\]

The exact scalar identity is

\[
 \Lambda=Wx_m-1.
\tag{1.3}
\]

Since \(Wx_m\) is an integer, define

\[
 j_m:=W\{x_m\}\in\{0,1,\ldots,W-1\},
 \qquad s_m:=\lfloor x_m\rfloor.
\tag{1.4}
\]

Let

\[
 T_d=\binom{d+1}{2},
 \qquad
 h=(\Lambda-dW)_+,
\tag{1.5}
\]

where \(d\) is the optimal deadline.

## 2. Exact positive-boundary window

### Theorem 2.1

For all sufficiently large parameters,

\[
 \boxed{
 h>0
 \iff
 d=s_m\ \text{ and }\ 2\le j_m\le T_d+1.}
\tag{2.1}
\]

On this face,

\[
 \boxed{h=j_m-1,\qquad \sigma=T_d-h=T_d-j_m+1.}
\tag{2.2}
\]

#### Proof

If \(j_m\ge1\), equation (1.3) gives

\[
 \Lambda=s_mW+(j_m-1).
\]

Thus the quotient and remainder are \(q=s_m\) and
\(\rho=j_m-1\).  The optimal deadline equals \(q\) precisely when
\(\rho\le T_q\); its boundary is positive precisely when additionally
\(\rho>0\).  This is (2.1), and (2.2) follows by substitution.

If \(j_m=0\), then

\[
 \Lambda=(s_m-1)W+(W-1).
\]

Since \(T_{s_m-1}<W-1\) eventually, the deadline is \(s_m\) and
\(h=0\). \(\square\)

Equivalently, a positive boundary occurs only when the Wallis phase lies
in the exponentially short interval

\[
 \boxed{
 0<\{x_m\}\le\frac{T_d+1}{W}=\exp(-\Theta(m)).}
\tag{2.3}
\]

The exact clean-path protected-factor condition becomes

\[
 4h\le m-1
 \iff
 \boxed{j_m\le\left\lfloor\frac{m+3}{4}\right\rfloor.}
\tag{2.4}
\]

Therefore a failure of that condition is exactly

\[
 \left\lfloor\frac{m+3}{4}\right\rfloor
 <j_m\le T_d+1.
\tag{2.5}
\]

The interval in (2.5) is nonempty asymptotically because

\[
 T_d=\left(\frac\pi8+o(1)\right)m
 >\frac m4.
\tag{2.6}
\]

Thus scalar size alone cannot prove \(4h\le m-1\).

## 3. Exact modular form

The numerator \(j_m\) is an ordinary least nonnegative residue.  In odd
dimension,

\[
 \boxed{
 j_m^-
 \equiv 4^{m-1}\pmod{C_m/2},
 \qquad 0\le j_m^-<C_m/2.}
\tag{3.1}
\]

In even dimension,

\[
 \boxed{
 j_m^+
 \equiv 2^{2m-1}-\frac{C_m}{2}\pmod{C_m},
 \qquad 0\le j_m^+<C_m.}
\tag{3.2}
\]

Hence an eventual proof of \(4h\le m-1\) on the positive face would be
the residue theorem

\[
 2\le j_m\le T_d+1
 \Longrightarrow
 j_m\le\left\lfloor\frac{m+3}{4}\right\rfloor
\tag{3.3}
\]

for both parities.  Neither uniform distribution of \(\{x_m\}\) nor the
known dyadic congruence decides (3.3): both concern scales much coarser
than the exponentially short window (2.3).

## 4. Positive-boundary dimensions are sparse

Although (3.3) remains open, the positive face itself is sparse without
using equidistribution.

### Theorem 4.1 (at most one positive boundary per depth and parity)

For each sufficiently large integer \(d\), each parity contains at most
one semilength \(m\) with deadline \(d\) and \(h>0\).

#### Proof

The sequence \(x_m=A_m-\eta\) is strictly increasing, and

\[
 x_{m+1}-x_m
 =A_{m+1}-A_m
 =\frac{A_m}{2m+1}
 =\Theta(m^{-1/2}).
\tag{4.1}
\]

If two indices \(m_1<m_2\) had the same positive-boundary depth \(d\),
Theorem 2.1 would put both \(x_{m_i}\) just above the same integer \(d\),
and in particular

\[
 0<x_{m_2}-d\le\frac{T_d+1}{W(m_2)}.
\tag{4.2}
\]

But monotonicity and (4.1) give

\[
 x_{m_2}-d>x_{m_2}-x_{m_1}
 \ge \min_{m_1\le t<m_2}\frac{A_t}{2t+1}
 =\Omega(m_2^{-1/2}),
\]

whereas the right side of (4.2) is exponentially small.  This is
impossible for large \(m_2\). \(\square\)

### Corollary 4.2

For either parity, the number of positive-boundary dimensions up to
semilength \(M\) is

\[
 O(\sqrt M).
\tag{4.3}
\]

Consequently \(h=0\) on a density-one set of dimensions.  This is useful
for architecture selection, but an all-dimensional additive theorem must
still handle the sparse exceptional subsequence.

## 5. One clean collar cannot bundle two target-disjoint boundary flags

In the lag-two model every boundary task is a flag

\[
 M\subset U=M+u,
 \qquad |M|=a,quad |U|=a+1.
\tag{5.1}
\]

Write

\[
 H=Q\cup\{a_0\},\qquad |H|=a-d+1.
\]

Before the \(C_0+z\) letter, the relevant toggle block is

\[
 u,a_1,\ldots,a_{d-1}.
\]

Its unique rank-\((a+1)\) interval using the complete low flag band is

\[
 U=H+u+a_1+\cdots+a_{d-1}.
\tag{5.2}
\]

For \(d\ge3\), it has two adjacent rank-\(a\) subintervals,

\[
 H+u+a_1+\cdots+a_{d-2},
 \qquad
 H+a_1+\cdots+a_{d-1}=M.
\tag{5.3}
\]

(For \(d=2\), only the second has the required rank.)  Thus a collar may
display two abstract rank-\(a\)-to-rank-\((a+1)\) incidences, but they
share the same top target \(U\).

### Theorem 5.1 (no local flag bundling)

One clean lag-two collar can realize at most one member of a boundary task
bank whose rank-\((a+1)\) top targets are distinct.

#### Proof

Every eligible low-band incidence in (5.2)--(5.3) uses the same top
\(U\).  Two tasks with distinct top targets therefore cannot occupy the
same collar. \(\square\)

The shorter suffixes carry additional lower targets at other ranks, and
the alternative bottom in (5.3) may be useful if repeated top targets are
allowed.  It does not bundle two flags in the target-disjoint bank used by
the clean-packet factor.  Multiple such tasks may share one longer
fixed-core rail only as distinct, nonoverlapping collars.

## 6. Consequence for the clean \(B+2\) route

The complete clean bank gives a protected four-edge middle-levels path per
positive boundary task.  The existing small-protected-factor theorem
therefore applies automatically when

\[
 4h\le m-1.
\]

Theorem 2.1 reduces the dimensions not covered by that argument to the
exact residue interval (2.5).  Theorem 4.1 shows that such dimensions are
at most \(O(\sqrt M)\) up to semilength \(M\), while Theorem 5.1 rules out
compressing several of their flag tasks into one clean collar.

Thus the proof-safe alternatives are:

1. prove the residue implication (3.3);
2. strengthen the protected-factor theorem beyond \(m-1\) edges for the
   special disjoint four-edge path bank; or
3. use a different compound packet/factor in the sparse exceptional
   positive-boundary dimensions.

Current scalar and equidistribution theorems do not choose among these
three alternatives.
