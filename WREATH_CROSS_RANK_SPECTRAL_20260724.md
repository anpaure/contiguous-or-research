# Cross-rank cyclic-interval incidence and the exact middle kernel

## 1. Verdict

Let \(n=2m+1\). Put all cyclic-interval ranks on one common column space:
the oriented cyclic orders of \([n]\), modulo rotation. If \(A_r\) is the
incidence matrix of all \(n\) cyclic \(r\)-intervals, then an exact middle
factor is a Boolean vector \(x\) with

\[
A_mx={\bf1}.                                         \tag{1.1}
\]

The capacity energy at rank \(r\) is exactly the integer-floor excess of
\(\|A_rx\|_2^2\). The real-linear action of the middle kernel is completely
determined:

\[
\boxed{A_r(\ker A_m)=\ker U_r\qquad(2\le r<m),}      \tag{1.2}
\]

where \(U_r\) is the point-versus-\(r\)-set incidence matrix. More strongly,

\[
\boxed{
\ker A_m\longrightarrow\bigoplus_{r=2}^{m-1}\ker U_r,
\qquad y\longmapsto(A_2y,\ldots,A_{m-1}y)
\text{ is surjective}.}                              \tag{1.3}
\]

Thus there is no real cross-rank spectral obstruction: every discrepancy
with zero point margins can be changed inside the exact-middle affine space,
and the ranks can be changed independently by signed vectors.

The tempting row-space inclusion is false. For distinct
\(1\le r,s\le m\),

\[
\boxed{
\operatorname{im}A_r^{\mathsf T}\cap
\operatorname{im}A_s^{\mathsf T}
=\operatorname{span}\{{\bf1}\}.}                    \tag{1.4}
\]

In particular, for \(2\le r<m\),

\[
\operatorname{im}A_r^{\mathsf T}\not\subseteq
\operatorname{im}A_m^{\mathsf T},
\qquad
\ker A_m\not\subseteq\ker A_r.                     \tag{1.5}
\]

The apparent contradiction with the Petr--Turek wreath matrix comes from a
column-space mismatch. If \(g=\gcd(n,r)\), one all-start column of \(A_r\)
is the sum of \(g\) phase wreaths in the Petr--Turek \((n,r)\) sense. At the
middle rank \(g=1\), but generally \(g>1\). Moreover oriented reversals are
duplicate columns. Standalone rank-\(r\) wreath-matrix eigenvalues therefore
cannot be transferred to \(A_r\) without the phase-aggregation map.

This is an exact continuous theorem, not an integral rounding theorem. The
rank-selecting kernel vectors have overlapping positive and negative wreaths
and need not be differences of Boolean exact factors. Quantitative CRP still
requires support-feasible circuits or balanced switches.

## 2. The common all-start matrices

Let \(\Omega^+\) be the set of oriented cyclic orders of \([n]\), modulo
cyclic rotation. Reversal is retained for the moment as a second copy. For
\(C=(c_0,\ldots,c_{n-1})\in\Omega^+\), write

\[
I_C(j,r)=\{c_j,c_{j+1},\ldots,c_{j+r-1}\}.
\]

For \(1\le r\le n-1\), define

\[
A_r:\mathbb R^{\Omega^+}\longrightarrow
\mathbb R^{\binom{[n]}r},
\qquad
(A_rx)_S=
\sum_{C\in\Omega^+}x_C
{\bf1}\{S=I_C(j,r)\text{ for some }j\}.             \tag{2.1}
\]

Each column contains exactly \(n\) ones. Reversing \(C\) does not change
its interval family, so

\[
A_re_C=A_re_{C^{\rm rev}}.                           \tag{2.2}
\]

The reversal-antisymmetric copy is consequently contained in
\(\bigcap_r\ker A_r\). Quotienting it gives the unoriented cyclic-order
space used in `WREATH_MATRIX_VERTICAL_AUDIT.md`; every theorem below is
unchanged by that quotient.

For \(r=m\), the \(n\) intervals determine the unoriented cyclic order, and
\(\gcd(n,m)=1\). Thus the quotient of \(A_m\) is exactly the incidence
matrix whose Gram matrix is the Petr--Turek middle wreath matrix.

If \(x\in\{0,1\}^{\Omega^+}\) satisfies (1.1), then summing all middle rows
gives

\[
n{\bf1}^{\mathsf T}x=W,
\qquad {\bf1}^{\mathsf T}x=B=W/n.                    \tag{2.3}
\]

Its rank-\(r\) load vector is \(\mu_r=A_rx\), of total mass \(W\).

## 3. Capacity energy is a squared-norm excess

Write

\[
N_r=\binom nr,
\qquad W=c_rN_r+a_r,
\qquad 0\le a_r<N_r.                                 \tag{3.1}
\]

Among integer vectors of length \(N_r\) and total mass \(W\), the minimum
squared norm is

\[
L_r^{\min}=(N_r-a_r)c_r^2+a_r(c_r+1)^2.              \tag{3.2}
\]

It is attained precisely by the floor/ceiling vectors. Therefore the
quadratic capacity energy is

\[
\boxed{
Q_r(x)=\frac12\left(\|A_rx\|_2^2-L_r^{\min}\right).} \tag{3.3}
\]

Equivalently,

\[
Q_r(x)=
\sum_S\binom{(A_rx)_S}{2}
-\left[(N_r-a_r)\binom{c_r}{2}
      +a_r\binom{c_r+1}{2}\right].                  \tag{3.4}
\]

Thus, on the affine fibre \(A_mx={\bf1}\), multidepth energy is the
quadratic form

\[
\frac12x^{\mathsf T}
\left(\sum_rw_rA_r^{\mathsf T}A_r\right)x
\]

minus a constant.

There is a sharper middle-kernel form.  The uniform fractional exact factor
is

\[
 x_0={1\over D_m}{\bf1}_{\Omega^+},
 \qquad D_m=m!(m+1)!,                              \tag{3.5}
\]

because \(A_mx_0={\bf1}\).  If \(A_mx={\bf1}\) and \(y=x-x_0\), then

\[
 y\in\ker A_m,
 \qquad
 A_ry=A_rx-{W\over N_r}{\bf1}.                    \tag{3.6}
\]

The balanced integer norm (3.2) differs from the squared norm of the
constant real vector by exactly

\[
 L_r^{\min}-{W^2\over N_r}
 ={a_r(N_r-a_r)\over N_r}.                        \tag{3.7}
\]

Consequently

\[
\boxed{
 Q_r(x)={1\over2}\|A_ry\|_2^2
 -{a_r(N_r-a_r)\over2N_r}.}
\tag{3.8}
\]

The subtracted quantity is the fixed integer quantization floor.  Hence the
pair-collision capacity energy is exactly the middle-kernel harmonic norm,
up to a factor-independent constant.  By (4.2), \(A_ry\) has zero total and
zero point margins, so only the constituents \(E_2,\ldots,E_r\) occur.

## 4. The point-margin constraint

Let

\[
U_r:\mathbb R^{\binom{[n]}r}\longrightarrow\mathbb R^n,
\qquad
(U_rf)_i=\sum_{S\ni i}f_S.                           \tag{4.1}
\]

Every coordinate occurs in exactly \(r\) cyclic \(r\)-intervals of one
order. Hence the exact matrix identity is

\[
\boxed{U_rA_r=r\,{\bf1}_n{\bf1}_{\Omega^+}^{\mathsf T}.} \tag{4.2}
\]

The rows of \(U_r\) are linearly independent for \(1\le r<n\): its row
Gram matrix has diagonal \(\binom{n-1}{r-1}\), off-diagonal
\(\binom{n-2}{r-2}\), and positive eigenvalues on both the constant and
standard subspaces. Thus

\[
\dim\ker U_r=N_r-n.                                  \tag{4.3}
\]

If \(A_sy=0\) for any \(s\), then the column-sum identity gives
\({\bf1}^{\mathsf T}y=0\). Equation (4.2) consequently implies

\[
A_r(\ker A_s)\subseteq\ker U_r
\qquad(r\ne s).                                      \tag{4.4}
\]

## 5. Petr--Turek selectors give the reverse inclusion

Fix a base order \(C=(1,2,\ldots,n)\). For \(2\le r\le m\), put

\[
\tau=(1\ 2),\qquad \sigma=(r+1\ r+2),
\]

and define the signed four-order vector

\[
z_r=e_C-e_{\tau C}-e_{\sigma C}+e_{\tau\sigma C}.   \tag{5.1}
\]

This is the adjacent-pair kernel vector used by Petr and Turek. The direct
all-start calculation gives

\[
A_sz_r=0\quad(1\le s\le m,\ s\ne r),                \tag{5.2}
\]

while, with \(K=\{3,\ldots,r\}\),

\[
\begin{aligned}
A_rz_r={}&e_{K\cup\{2,r+1\}}-e_{K\cup\{1,r+1\}}\\
         &-e_{K\cup\{2,r+2\}}+e_{K\cup\{1,r+2\}}.
                                                               \tag{5.3}
\end{aligned}
\]

Indeed, a target coefficient can survive the alternating sum only if the
target contains exactly one element from each swapped adjacent pair.  If it
is an interval, its two boundary cuts must therefore separate both pairs.
The two arcs between those cuts have lengths \(r\) and \(n-r\); for an
interval length \(s\le m<n-r\), this forces \(s=r\).  The four choices at
that rank give (5.3).  This proof uses all starts and does not assume
\(\gcd(n,r)=1\).

All relabelings of (5.3) span \(\ker U_r\). One proof is to take a vector
orthogonal to every displayed square: its exchange differences depend only
on the exchanged coordinates, so it is a sum of point weights, hence lies in
\(\operatorname{im}U_r^{\mathsf T}\). Taking orthogonal complements proves
the spanning assertion.

### Theorem 5.1 -- exact cross-rank kernel image

For distinct \(r,s\in\{1,\ldots,m\}\), with \(r\ge2\),

\[
\boxed{A_r(\ker A_s)=\ker U_r.}                      \tag{5.4}
\]

For \(s=m\), the relabelings of \(z_r\), rank by rank, give an explicit
right inverse simultaneously. Hence (1.3) holds.

The constant target vector also belongs to \(\operatorname{im}A_r\), by
averaging all columns and using transitivity. Therefore

\[
\boxed{
\operatorname{im}A_r
=\operatorname{span}\{{\bf1}\}\oplus\ker U_r,
\qquad
\operatorname{rank}A_r=N_r-n+1.}                    \tag{5.5}
\]

This recovers the Petr--Turek rank \(\binom nr-n+1\) directly for the
all-start incidence matrix.

## 6. Exact row-space separation

### Theorem 6.1 -- different ranks meet only in the constant line

For distinct \(1\le r,s\le m\),

\[
\operatorname{im}A_r^{\mathsf T}\cap
\operatorname{im}A_s^{\mathsf T}
=\operatorname{span}\{{\bf1}_{\Omega^+}\}.           \tag{6.1}
\]

#### Proof

The case \(r=1\) is immediate because every singleton is an interval in
every order, so \(\operatorname{im}A_1^{\mathsf T}\) is the constant line.
Assume \(r\ge2\), and let

\[
v=A_r^{\mathsf T}f=A_s^{\mathsf T}g.
\]

For every \(y\in\ker A_s\),

\[
0=\langle v,y\rangle=\langle f,A_ry\rangle.
\]

By Theorem 5.1, \(A_r(\ker A_s)=\ker U_r\). Hence
\(f\perp\ker U_r\), so \(f=U_r^{\mathsf T}h\) for some \(h\). Transposing
(4.2) now gives

\[
v=A_r^{\mathsf T}U_r^{\mathsf T}h
 =r({\bf1}^{\mathsf T}h){\bf1}_{\Omega^+}.
\]

Conversely, \(A_r^{\mathsf T}{\bf1}=n{\bf1}\) for every \(r\), so the
constant line is contained in both row spaces. \(\square\)

The same selectors prove the stronger direct-sum statement

\[
\sum_{r=2}^m A_r^{\mathsf T}(\ker U_r)
=\bigoplus_{r=2}^m A_r^{\mathsf T}(\ker U_r).         \tag{6.2}
\]

Indeed, pair a putative dependence with relabelings of \(z_a\); all ranks
except \(a\) vanish, while the rank-\(a\) images span \(\ker U_a\).

Equation (6.1) resolves the proposed inclusion test. Inclusion would imply
\(A_r(\ker A_m)=0\), whereas the exact answer is the largest image allowed
by point margins, namely \(\ker U_r\).

## 7. The \(S_n\)-module and compressed spectral form

Over \(\mathbb C\), the target permutation module is multiplicity-free:

\[
\mathbb C^{\binom{[n]}r}
=E_0\oplus E_1\oplus\cdots\oplus E_r,
\qquad E_j\cong S^{(n-j,j)}.                         \tag{7.1}
\]

Here

\[
\operatorname{im}U_r^{\mathsf T}=E_0\oplus E_1,
\qquad
\ker U_r=E_2\oplus\cdots\oplus E_r.                \tag{7.2}
\]

Equations (5.5) and (7.2) show that \(A_r^{\mathsf T}\) annihilates the
target standard module \(E_1\), is nonzero on \(E_0\), and embeds exactly
one copy of every \(E_j\), \(2\le j\le r\), into the common order module.
This is the module content behind the positive Petr--Turek eigenvalues.

There is also an exact Schur-complement description of the spectrum seen
inside the middle kernel. Fix \(2\le j\le r<m\). Let

* \(\lambda_{r,j}\) be the eigenvalue of \(A_rA_r^{\mathsf T}\) on \(E_j\);
* \(\lambda_{m,j}\) be the corresponding middle eigenvalue; and
* \(\tau_{r,m,j}\) be the scalar of the equivariant cross operator
  \(A_rA_m^{\mathsf T}:E_j^{(m)}\to E_j^{(r)}\), after fixed unitary
  identifications.

If \(P_m\) is orthogonal projection onto \(\ker A_m\), then the compressed
Hessian

\[
P_mA_r^{\mathsf T}A_rP_m                              \tag{7.3}
\]

has, on its \(E_j\)-copy, the nonzero eigenvalue

\[
\boxed{
\kappa_{r,j}
=\lambda_{r,j}-\frac{|\tau_{r,m,j}|^2}{\lambda_{m,j}}>0.} \tag{7.4}
\]

The formula is the squared norm of the rank-\(r\) multiplicity vector after
orthogonal projection away from the middle multiplicity line. Strict
positivity follows from Theorem 6.1: equality would mean that the rank-\(r\)
and middle copies of \(E_j\) coincide.

Thus every nontrivial target module \(E_2,\ldots,E_r\) is visible to a
middle-kernel direction. What remains quantitatively unknown are the cross
scalars \(\tau_{r,m,j}\), or equivalently the angles between these distinct
copies. They can be computed by the same Johnson-scheme transform used by
Petr--Turek, since an entry of \(A_rA_m^{\mathsf T}\) depends only on
\(|R\cap M|\).

### 7.1 An exact two-arc cross-scalar formula

The cross scalars admit a direct finite sum. For \(s,t\le m\), let
\(D_s=s!(n-s)!\), the number of oriented cyclic orders modulo rotation in
which a prescribed \(s\)-set is an interval. Conditional on that event, a
prescribed \(t\)-set with intersection size \(u\) is an interval with
probability

\[
p_{s,t}(u)=
\begin{cases}
1,&s=t=u,\\
\dfrac{n-s-t+1}{\binom{n-s}{t}},&u=0,\\
\dfrac{s-t+1}{\binom{s}{t}},&u=t<s,\\
\dfrac{t-s+1}{\binom{n-s}{t-s}},&u=s<t,\\
\dfrac{2}{\binom{s}{u}\binom{n-s}{t-u}},
   &0<u<\min(s,t).
\end{cases}                                         \tag{7.5}
\]

The cases are the two boundary-crossing arcs, together with containment and
disjointness. Put

\[
f_{s,j}(S)=\prod_{i=0}^{j-1}
\left({\bf1}_{\{2i\in S\}}-{\bf1}_{\{2i+1\in S\}}\right).
                                                               \tag{7.6}
\]

This is a standard vector in \(E_j\), with

\[
\|f_{s,j}\|_2^2=2^j\binom{n-2j}{s-j}.              \tag{7.7}
\]

If

\[
A_sA_t^{\mathsf T}f_{t,j}=\beta_{s,t,j}f_{s,j},
\]

then evaluating at an \(s\)-set on which \(f_{s,j}=1\) and grouping by the
number of odd choices among the \(j\) distinguished pairs gives

\[
\boxed{
\begin{aligned}
\beta_{s,t,j}=D_s
\sum_{k=0}^j(-1)^k\binom jk
\sum_{\ell=0}^{t-j}
&\binom{s-j}{\ell}
 \binom{n-s-j}{t-j-\ell}\\
&\cdot p_{s,t}(j-k+\ell).
\end{aligned}}                                      \tag{7.8}
\]

The unit-vector cross scalar used in (7.4) is

\[
|\tau_{s,t,j}|^2
=\beta_{s,t,j}^2
 \frac{\|f_{s,j}\|_2^2}{\|f_{t,j}\|_2^2}.          \tag{7.9}
\]

This calculation uses the common oriented-order columns, so it already has
the correct copy multiplicity for \(A_sA_t^{\mathsf T}\).

### 7.2 Exact adjacent-rank leakage in degree two

Take \(n=2m+1\), \(s=m\), \(t=m-1\), \(j=2\), and \(m\ge3\). Evaluating
(7.8) gives

\[
\lambda_{m,2}=D_m\frac{2m-1}{3},                    \tag{7.10}
\]

\[
\beta_{m,m-1,2}
=\lambda_{m,2}\frac{(m-2)(m+3)}{m(m+1)},            \tag{7.11}
\]

and

\[
\lambda_{m-1,2}
=D_{m-1}\frac{(2m-1)(m^3+4m^2-3m-6)}
 {3(m+2)(m+1)^2}.                                   \tag{7.12}
\]

Consequently the squared angle between the middle and first-lower copies of
\(E_2\) is

\[
\boxed{
\cos^2\theta_2
=\frac{(m-2)(m+3)^2}{m^3+4m^2-3m-6}
=1-\frac{12}{m^3+4m^2-3m-6}.}                      \tag{7.13}
\]

The compressed lower-rank Hessian eigenvalue is therefore

\[
\boxed{
\kappa_{m-1,2}
=\lambda_{m-1,2}\sin^2\theta_2
=\frac{4D_{m-1}(2m-1)}{(m+2)(m+1)^2}.}              \tag{7.14}
\]

Although positive, its relative leakage is only

\[
\frac{\kappa_{m-1,2}}{\lambda_{m-1,2}}
=\frac{12}{m^3+4m^2-3m-6}=\Theta(m^{-3}).           \tag{7.15}
\]

Thus continuous correction of a degree-two first-shadow discrepancy through
the middle kernel incurs norm inflation

\[
\frac1{\sin\theta_2}
=\sqrt{\frac{m^3+4m^2-3m-6}{12}}
=(1+o(1))\frac{m^{3/2}}{\sqrt{12}}.                 \tag{7.16}
\]

The degree-two angle also has a closed form at every lower depth.  For
\(1\le q\le m-2\), substituting \(s=m,t=m-q,j=2\) in (7.8) and simplifying
gives

\[
\boxed{
\begin{aligned}
 \sin^2\theta_{m,m-q;2}
 ={}&\frac{2q(q+1)
 \bigl((2q+1)m-(2q^2+2q-1)\bigr)}
 {(m^2-1)
 \bigl(m^2+(2q+1)m-3q(q+1)\bigr)}.
\end{aligned}}
\tag{7.17}
\]

Uniformly for \(q=o(m)\),

\[
 \sin^2\theta_{m,m-q;2}
 =\frac{2q(q+1)(2q+1)}{m^3}
 \left(1+O\!\left(\frac qm\right)\right).          \tag{7.18}
\]

Thus the degree-two middle-kernel frame remains thin throughout every
shallow band: its condition-number penalty is
\(\Theta((m/q)^{3/2})\).  The exact-rational checker asserts (7.17) at every
requested \((m,q)\), and a complete exact grid through \(m=30\) has been
verified.

This is a genuine quantitative spectral obstruction to a well-conditioned
projection argument, even though exact surjectivity holds. It does not
obstruct an integral nonlinear switching proof, but it explains why merely
projecting a lower-rank correction into \(\ker A_m\) can amplify coefficients
by a polynomial factor.

The normalizations in (7.10)--(7.14) are for oriented orders modulo rotation.
After quotienting each reversal pair, \(D_s\), every \(\lambda\), every
\(\beta\), and every compressed eigenvalue are divided by two.  The angle,
relative leakage (7.15), and conditioning factor (7.16) are unchanged.  This
is the only copy correction at the coprime middle rank.

### 7.3 Harmonic ordering and Gaussian aggregation

The harmonic-angle calculation is continued in
`WREATH_HARMONIC_ANGLE_ORDERING_20260724.md`.  It proves the exact
all-harmonic adjacent-rank formulas and, in particular,

\[
 \sin^2\theta_{m,m-1;2}
 <\sin^2\theta_{m,m-1;j}\qquad(3\le j\le m-1).
\tag{7.19}
\]

For fixed \(q,j\), the leading terms are

\[
 \sin^2\theta_{m,m-q;j}\sim
 \begin{cases}
 \displaystyle\binom{j+1}{3}{2q(q+1)(2q+1)\over m^3},
      &j\text{ even},\\[2mm]
 \displaystyle{4jq(q+1)\over3(2q+1)m},
      &j\text{ odd}.
 \end{cases}
\tag{7.20}
\]

Moreover the exact degree-two leakage has Gaussian aggregate

\[
 \sum_{q\le H}{\binom{2m+1}{m-q}\over\binom{2m+1}{m}}
 \sin^2\theta_{m,m-q;2}
 ={2+o(1)\over m}
\tag{7.21}
\]

whenever \(H/\sqrt m\to\infty\) and \(H=o(m)\).  Thus the whole-band
degree-two norm penalty is only \(\Theta(\sqrt m)\), rather than the
\(\Theta(m^{3/2})\) penalty of the first shadow alone.

For the actual integer capacity weight
\(d_q=\lfloor W/N_q\rfloor\), the corresponding exact limit is

\[
 \sum_{q\le H}{\sin^2\theta_{m,m-q;2}\over d_q}
 ={C_{\rm cap}+o(1)\over m},
 \qquad
 C_{\rm cap}=\sum_{k\ge2}{(\log k)^2\over k(k-1)}
 =2.336313176\ldots .
\tag{7.22}
\]

It remains open to prove that degree two minimizes leakage for every
growing depth \(q\).  Exact rational computation finds no counterexample
through \(m=50\).  Beyond (7.19), the continuation proves the all-depth
comparison with degree two exactly for \(j=3,4,6\); a formula
uniform in growing \(j\) is the remaining gap.

## 8. The phase-copy correction

The standalone Petr--Turek \((n,r)\)-wreath does not contain all \(n\)
coordinate starts when \(g=\gcd(n,r)>1\). For a pointed representative
\(C=(c_0,\ldots,c_{n-1})\), define its phase-\(t\) family

\[
\mathcal F_{C,t}^{(r)}
=\{I_C(t+jr,r):0\le j<n/g\},
\qquad 0\le t<g.                                     \tag{8.1}
\]

The starts \(t+jr\) run through all positions congruent to \(t\pmod g\), so

\[
\boxed{
\{I_C(j,r):j\in\mathbb Z_n\}
=\mathop{\dot\bigcup}_{t=0}^{g-1}
 \mathcal F_{C,t}^{(r)}.}                            \tag{8.2}
\]

Each family in (8.1) is a Petr--Turek \((n,r)\)-wreath. Changing the pointed
representative permutes the phases, so their sum is intrinsic to the
unpointed cyclic order.

Let \(P_r\) denote the incidence matrix whose distinct columns are the
Petr--Turek rank-\(r\) wreaths. There is a phase-aggregation map \(J_r\),
combining repeated physical phase wreaths when necessary, such that

\[
\boxed{A_r=P_rJ_r.}                                  \tag{8.3}
\]

Consequently the all-start Gram operator relevant to vertical energy is

\[
A_r^{\mathsf T}A_r
=J_r^{\mathsf T}(P_r^{\mathsf T}P_r)J_r,             \tag{8.4}
\]

not the standalone Petr--Turek rank-\(r\) wreath matrix. At the middle rank
\(g=\gcd(2m+1,m)=1\), there is one phase, and after quotienting reversal
copies the distinction disappears. This is the precise multiplicity/copy
resolution needed before comparing ranks.

## 9. Consequence and remaining obstruction

The exact spectral answer is favourable:

* all allowable rank-\(r\) discrepancy directions occur in \(\ker A_m\);
* different ranks have independent signed selectors;
* the compressed Hessian is strictly positive on every target module
  \(E_j\), \(2\le j\le r\);
* row-space containment does not obstruct varying shadows.

But this is also a limit theorem for the spectral route. The vectors
\(z_r\) have four highly overlapping wreaths; neither sign can occur inside
an exact factor. Surjectivity of (1.3) says nothing about the tangent cone of
the Boolean polytope

\[
\{x\in[0,1]^{\Omega^+}:A_mx={\bf1}\}.                \tag{9.1}
\]

The next useful theorem must therefore be integral: compare the legal
balanced-eight-switch span, or a larger support-feasible circuit span, with
the positive compressed modules in (7.4). A quantitative lower bound on
their projection to each \(E_j\), together with control of the quadratic
switch toll, would turn the continuous spectrum into a CRP descent theorem.

The real-linear Petr--Turek spectrum itself presents no obstruction; support
feasibility and conditioning of the legal circuit subspace are the remaining
gates.

## Reference

J. Petr and P. Turek,
[*The wreath matrix*](https://arxiv.org/abs/2501.07269), especially the
rank computation, the \(S_n\)-module decomposition, and the adjacent-pair
kernel vectors in Section 5.
