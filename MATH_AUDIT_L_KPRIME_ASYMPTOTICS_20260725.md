# Cross-audit: Lane L constant and asymptotic accounting

Date: 2026-07-25

Target: `MATH_ATTACK_L_GROWING_HARMONIC_ROBUST_CUT_BOUNDARY_20260725.md`.

## 1. Verdict

The constant in (2.10), the growing-degree truncation in (5.9)--(5.10),
and the reduced-cut quantifiers in (6.2)--(6.6) are correct.  No missing
factor of \(2\), \(n\), \(t\), or \(c_q\) was found.

There is one harmless precision point.  The displayed \(K'_m\) is an exact
rational upper bound and equals the parity-sensitive Bhatia--Davis
coefficient when \(t\) is even.  When \(t\) is odd the literal floor
\(\lfloor t/2\rfloor\) gives a slightly smaller parity-sensitive constant.
Thus “exact improvement” is correct if it means an exact uniform bound, but
\(K'_m\) is not the parity-sharp output for odd \(t\).  Also, (2.10) is to be
read for \(m\ge 3\), as already forced by its ambient condition
\(j=2\le r_1=m-1\).

## 2. Independent derivation of \(K'_m\)

Put \(n=2m+1\), \(W=nt\), and let \(h_{ab}\) count factor rows in which
\(a,b\) have cyclic distance \(m\).  Exact middle ownership gives

\[
 G_2=\binom{n-2}{m-2}=\frac{m-1}{2}t.
\]

In any row in which the pair occurs in at least one middle window, the
number of such windows is at most \(m-1\).  Hence the pair occurs in at least

\[
 \left\lceil\frac{G_2}{m-1}\right\rceil
 =\left\lceil\frac t2\right\rceil
\]

rows.  There are \(t\) rows, so

\[
0\le h_{ab}\le t-\left\lceil\frac t2\right\rceil
=\left\lfloor\frac t2\right\rfloor.
\tag{2.1}
\]

Each cyclic row has exactly \(n\) unordered distance-\(m\) pairs.  Since
\(\binom n2=nm\),

\[
 \sum_{a<b}h_{ab}=nt,
 \qquad \overline h=\frac tm.
\tag{2.2}
\]

Bhatia--Davis applied to (2.1)--(2.2) therefore gives the parity-sharp
intermediate estimate

\[
 \sum_{a<b}\left(h_{ab}-\frac tm\right)^2
 \le nt\left(\left\lfloor\frac t2\right\rfloor-\frac tm\right)
 \le \frac{n(m-2)}{2m}t^2.
\tag{2.3}
\]

At \(q=1\), exact total and point margins kill \(E_0,E_1\), and the
unnormalized rank-\((m-1)\)-to-rank-\(2\) inclusion singular value on \(E_2\)
is

\[
 \alpha_{1,2}=\binom{n-4}{m-3}=\binom{2m-3}{m-3}.
\tag{2.4}
\]

Thus no normalization factor is hidden:

\[
 \|P_{E_2}f_1\|_2^2
 =\frac1{\alpha_{1,2}}
 \sum_{a<b}\left(h_{ab}-\frac tm\right)^2.
\tag{2.5}
\]

Direct factorial cancellation gives

\[
 \frac W{\alpha_{1,2}}
 =\frac{4(2m+1)(2m-1)}{(m+1)(m-2)}.
\tag{2.6}
\]

Using \(nt=W\), the second inequality in (2.3) and (2.5)--(2.6) yield

\[
\begin{aligned}
\frac{\|P_{E_2}f_1\|_2^2}{t}
&\le \frac{m-2}{2m}\frac W{\alpha_{1,2}}\\
&=\frac{2(2m+1)(2m-1)}{m(m+1)}=:K'_m.
\end{aligned}
\tag{2.7}
\]

Moreover

\[
 8-K'_m=\frac{8m+2}{m(m+1)}>0.
\tag{2.8}
\]

Keeping the floor in (2.3) gives the slightly sharper exact coefficient

\[
 K'_{m,\mathrm{floor}}
 =\frac W{\alpha_{1,2}}
 \left(\frac{\lfloor t/2\rfloor}{t}-\frac1m\right)
 =
 \begin{cases}
 K'_m,&t\text{ even},\\[2mm]
 K'_m-\dfrac{W}{2t\alpha_{1,2}},&t\text{ odd}.
 \end{cases}
\tag{2.9}
\]

This refinement has no effect on any later asymptotic conclusion.

## 3. Constants preceding the growing-degree truncation

The two fixed-\(A\) constants used later are safe.

First, from

\[
 \lambda_H=\frac{W}{N_H}
 =\prod_{i=1}^H\frac{m+i+1}{m-i+1},
\]

one gets

\[
 \log\lambda_H
 \le\sum_{i=1}^H\frac{2i}{m-i+1}
 \le\frac{H(H+1)}{m-H+1}.
\tag{3.1}
\]

For fixed \(A>0\), \(H=\lceil A\sqrt m\rceil\le(A+1)\sqrt m\), and
eventually \(m-H+1\ge m/2\).  Consequently

\[
 \log\lambda_H\le2(A+1)(A+2),
\]

which proves \(c_H\le M_A=\lceil e^{2(A+1)(A+2)}\rceil\) in (5.4).

Second, with \(r_q=m-q\),

\[
 \frac{W}{\alpha_q}
 =\lambda_q\frac{N_q}{\alpha_q},
 \qquad
 \frac{N_q}{\alpha_q}
 =\frac{(n)_4}{r_q(r_q-1)(n-r_q)(n-r_q-1)}.
\tag{3.2}
\]

Uniformly for \(q\le H=o(m)\), the last fraction is eventually below
\(81\) (in fact it tends uniformly to \(16\)).  For example, eventually
\(q\le m/4\), \(n\le9m/4\), \(r_q\ge3m/4\),
\(r_q-1\ge2m/3\), and both complementary factors are at least \(m\);
these bounds make the fraction at most
\(2(9/4)^4<81\).  Combining this with (3.1)
gives

\[
 \frac W{\alpha_q}
 \le81e^{2(A+3)^2}=\Gamma_A,
\tag{3.3}
\]

so the deliberately loose constant at (5.8) is valid.

Using \(c_q\ge1\), (4.3), and
\(\sum_{q\le H}q^2(q+1)\le2H^4\), (3.3) gives exactly

\[
 \sum_{q\le H}\frac{\|P_{E_2}f_q\|_2^2}{c_q}
 \le\frac{\Gamma_A}{2}H^4t.
\tag{3.4}
\]

## 4. Growing-degree truncation

For \(j\le r_q\), (2.7) of the target report and
\((x-a)(b-x)\le(b-a)^2/4\le q^2t^2/4\) give

\[
 \|P_{E_j}f_q\|_2^2
 \le\frac{\binom njq^2t^2}{4\alpha_{q,j}}.
\tag{4.1}
\]

Because \(\lambda_q>1\),
\(c_q=\lfloor\lambda_q\rfloor\ge\lambda_q/2=W/(2N_q)\).  Also

\[
 \frac{N_q}{\alpha_{q,j}}
 =\frac{(n)_{2j}}{(r_q)_j(n-r_q)_j}.
\tag{4.2}
\]

For \(q\le H\) and
\(j\le J_m^{\rm cell}=\lfloor H/[8\log(108m)]\rfloor\), eventually
\(\binom nj\le(3m)^j\) and the ratio in (4.2) is at most \(36^j\).
Therefore

\[
 \frac1{c_q}\|P_{E_j}f_q\|_2^2
 \le\frac{q^2t}{2n}(108m)^j.
\tag{4.3}
\]

Now \(J_m^{\rm cell}\to\infty\),
\((108m)^{J_m^{\rm cell}}\le e^{H/8}\),
\(\sum_{q\le H}q^2\le H^3\), and, eventually,
\(\sum_{j=2}^{J}(108m)^j\le2(108m)^J\).  This proves (5.9) with its
displayed constant.

Let

\[
 L_m=\frac{t4^H}{1024M_AH^4},
 \qquad
 U_m=\frac{tH^3}{n}e^{H/8}.
\]

The exact comparison needed for (5.10) is

\[
 \frac{U_m}{L_m}
 =\frac{1024M_AH^7}{n}
 \exp\bigl(-H(\log4-1/8)\bigr)\longrightarrow0,
\tag{4.4}
\]

because \(\log4-1/8>0\) and \(H\sim A\sqrt m\).  Hence eventually
\(U_m\le L_m/2\), yielding precisely the denominator \(2048M_AH^4\) in
(5.10).  Its ratio to \(Ht\) is

\[
 \frac{4^H}{2048M_AH^5}\longrightarrow\infty,
\tag{4.5}
\]

so the stated \(\omega_A(Ht)\) conclusion is also correct.

## 5. Reduced-cut asymptotics and quantifiers

Let \(Q_0=\lfloor m^{1/8}\rfloor\).  Since
\(Q_0^4\le\sqrt m\le H/A\), (3.4) with \(H\) replaced by \(Q_0\) proves

\[
 \mathcal S_{Q_0}(G_m)
 \le\frac{\Gamma_A}{2A}Ht.
\tag{5.1}
\]

For one correlated child, (4.4) of the target report bounds each of the two
complete-factor squared displacements by
\(2q^2(q+1)t^2/\alpha_q\).  The energy-change factor \(1/4\) therefore leaves

\[
 \left|\Delta\mathcal S_{Q_0}\right|
 \le\sum_{q\le Q_0}
 \frac{q^2(q+1)t^2}{c_q\alpha_q}.
\tag{5.2}
\]

Using \(c_q\ge1\), \(t^2/\alpha_q=(t/n)(W/\alpha_q)\), and

\[
 \sum_{q=1}^{Q}q^2(q+1)
 =\frac{Q(Q+1)(3Q^2+7Q+2)}{12}\le Q^4
 \qquad(Q\ge2),
\]

equation (5.2) gives exactly

\[
 \left|\Delta\mathcal S_{Q_0}\right|
 \le\frac{\Gamma_AQ_0^4}{n}t
 \le\frac{\Gamma_A}{A}\frac{Ht}{n}.
\tag{5.3}
\]

Thus (6.4)--(6.5) have the correct factor \(1/n\).

Finally fix \(A,B,C>0\).  Combining (6.3) with (5.3), the strict inequality
in (6.6) follows once

\[
 \frac{4^H}{1024M_Am^BH^5}
 -\frac{\Gamma_A}{2A}m^{-B}
 -\frac{C+\Gamma_A/A}{n}>0.
\tag{5.4}
\]

The first term tends to \(+\infty\), because

\[
 \log\frac{4^H}{m^BH^5}
 =H\log4-B\log m-5\log H\longrightarrow+\infty,
\]

whereas the two subtracted terms tend to zero.  This verifies the exact
quantifier order: for every fixed \(A,B,C>0\) and every prescribed
transposition, the conjugated cell minimizer works for all sufficiently
large \(m\), with the threshold allowed to depend on \(A,B,C\).

## 6. Remaining asymptotic substitutions

The asymptotic uses in the scalar construction also check:

* \(D_m^2=2n^3t=2n^2W\), while
  \(t\ge2^n/[n(n+1)]\).  Hence \(t/m\gg D_m\).
* At \(j=m/2-1\), \(G_j\ge\binom{3m/2}{m/2}\), and the binomial mode
  estimate
  \(\binom{3s}{s}\ge(27/4)^s/(3s+1)\) shows \(G_j/m\gg D_m\), since
  \(\sqrt{27/4}>2\).
* For \(j\ge m/2\), \(G_j\le2^{3m/2+1}=o(t)\), proving the asserted
  eventual \(G_j\le t\).
* The error in the three-witness comparison is
  \(O(n^3D_m)=O(n^{9/2}\sqrt t)=o(t)\).
* With \(J_m=\lfloor n/(12\log n)\rfloor\), the low-degree mass is at most
  \(\exp(n/4+O(\log n))=o(t)\).
* The exact formula \(Q_1=(m-2)W/(m+2)\) is indeed \((1-o(1))W\), and
  \(\beta_1<4t\).

Accordingly, this audit finds no correction that changes any theorem or
no-go boundary in the target report.
