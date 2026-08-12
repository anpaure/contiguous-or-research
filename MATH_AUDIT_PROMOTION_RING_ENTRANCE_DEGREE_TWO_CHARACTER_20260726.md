# Degree-two audit of the promotion-ring entrance LP

Date: 2026-07-26

Method: pure mathematics.  All columns below are actual cyclic frames.  No
replacement of a frame by an arbitrary pair of target tables is made.

## 0. Outcome

Put

\[
 n=2m,\qquad q=\lceil m^{1/4}\rceil,\qquad
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad M=m+H,
 \qquad r=m-q,
\]

and retain the tuned relations

\[
 R=\binom nM,\qquad T=MR=W+o(W),\qquad
 W=\binom nm,\qquad \binom nr=(1+o(1))W.
\tag{0.1}
\]

The primal and dual in
`MATH_THEOREM_PROMOTION_RING_ENTRANCE_COUPLED_LP_DUAL_20260726.md`
are correct.  Degree zero is exactly the scalar surplus, and degree one is
exactly frozen by the top equations.

The first nonconstant sector can also be disposed of as a possible
macroscopic **linear or lattice obstruction**.  More precisely, there is an
integral choice of one genuine cyclic frame on every top for which

\[
 \boxed{
 \|P^{(m)}_2(a-TW^{-1}{\bf1})\|_2^2+
 \|P^{(r)}_2(b-T\tbinom nr^{-1}{\bf1})\|_2^2
 \le \left({32\over3}+o(1)\right)H^3.}
\tag{0.2}
\]

Consequently, for this one integral selection, every pair
\(\alpha\in E_2(J(n,m))\), \(\beta\in E_2(J(n,r))\) with
\(\|\alpha\|_\infty,\|\beta\|_\infty\le B_m\) satisfies

\[
 \left|
 \langle\alpha,a-TW^{-1}{\bf1}\rangle+
 \langle\beta,b-T\tbinom nr^{-1}{\bf1}\rangle
 \right|
 \le
 \left(\sqrt{64/3}+o(1)\right)B_m\sqrt{WH^3}.
\tag{0.3}
\]

Thus the right side is \(o(W)\) whenever

\[
 B_m=o\!\left(\sqrt{W/H^3}\right),
\tag{0.4}
\]

in particular for every polynomially bounded integral character.  Hence no
bounded-coefficient degree-two Johnson character, nor any polynomially
bounded integral combination of pair characters, gives an
\(\Omega(W)\) separating inequality between the uniform fractional load and
all integral frame selections.  Equation (0.2) also rules out a universal
\(\Omega(W)\) lower bound from any positive-semidefinite degree-two
quadratic form dominated by a polynomial multiple of the standard
degree-two norm.

The actual coupled chronology character is also explicit.  The middle and
entrance pair counts differ only in the shell of cyclic distances from
\(H\) through \(H+q\).  Its one-top variance is

\[
 \boxed{
 \tau_{H,q}^2=
 {2Hq^2+q(q-1)(2q-1)/3\over M-1}
 -\left({q(2H+q-1)\over M-1}\right)^2
 =(2+o(1)){Hq^2\over m}.}
\tag{0.5}
\]

It is therefore not an invariant.  After the natural Johnson
normalization, an integral selection exists with shell energy
\((16+o(1))Hq^2\), again polynomial and hence negligible at scale \(W\).

This does **not** prove the desired small collision/hole objective.  It proves
the exact narrower statement that the first higher Johnson sector has no
macroscopic integrality gap.  A surviving obstruction must couple the
nonlinear support indicators in the objective, use higher chronology, or
have coefficients exponentially larger than the objective normalization.

## 1. Audit of the primal and dual

For a top \(U\in\binom{[n]}M\) and an oriented cyclic frame \(\pi\) of
\(U\), let \(I_k(\pi)\) be its \(M\) cyclic intervals of length \(k\).
The integer variables obey

\[
 \sum_{\pi}x_{U,\pi}=1,
\tag{1.1}
\]

and the two loads are

\[
 a_X=\sum_{U,\pi}{\bf1}_{\{X\in I_m(\pi)\}}x_{U,\pi},
 \qquad
 b_S=\sum_{U,\pi}{\bf1}_{\{S\in I_r(\pi)\}}x_{U,\pi}.
\tag{1.2}
\]

With \(c_X,h_S\ge0\), the relaxation is

\[
 a_X-c_X\le1,\qquad b_S+h_S\ge1,
 \qquad x_{U,\pi}\ge0,
\tag{1.3}
\]

minimizing \(\sum_Xc_X+\sum_Sh_S\).  Dual variables
\(0\le u_X,v_S\le1\) and free variables \(z_U\) give

\[
 z_U\le
 \sum_{X\in I_m(\pi)}u_X-
 \sum_{S\in I_r(\pi)}v_S.
\tag{1.4}
\]

Eliminating \(z_U\) gives exactly

\[
 \max_{0\le u,v\le1}
 \left\{
 \sum_Sv_S-\sum_Xu_X+
 \sum_U\min_\pi
 \left(\sum_{X\in I_m(\pi)}u_X-
       \sum_{S\in I_r(\pi)}v_S\right)
 \right\}.
\tag{1.5}
\]

Uniform frame weights give loads \(T/W\) and
\(T/\binom nr\).  The dual choice \(u\equiv1,v\equiv0\) gives
\(T-W\).  Hence both primal and dual values are \(T-W\).  The averaging
argument in the source report also correctly shows that every fractional
dual weighting is bounded by this scalar value.

For every feasible integral or fractional selection,

\[
 \sum_{X\ni i}a_X=m\binom{n-1}{M-1},\qquad
 \sum_{S\ni i}b_S=r\binom{n-1}{M-1}.
\tag{1.6}
\]

Thus the centered load vectors have zero degree-zero and degree-one
projections.  This verifies the claimed clearing of the first two sectors.

## 2. Exact pair count in one actual frame

Fix two coordinates of a top.  In a uniformly chosen cyclic frame, their
oriented separation \(d\) is uniform on \(\{1,\ldots,M-1\}\).  For
\(1\le \ell<M/2\), define

\[
 \rho_\ell(d)=(\ell-d)_++(\ell-(M-d))_+.
\tag{2.1}
\]

### Lemma 2.1 (literal cyclic pair count)

If \(k=M-\ell>M/2\), the number \(D_k(d)\) of cyclic \(k\)-intervals
containing the fixed pair is

\[
 \boxed{D_k(d)=M-2\ell+\rho_\ell(d).}
\tag{2.2}
\]

Moreover

\[
 \mathbb E D_k={k(k-1)\over M-1}
\tag{2.3}
\]

and

\[
 \boxed{
 \operatorname {Var}(D_k)=\sigma_\ell^2:=
 {\ell(\ell-1)(2\ell-1)\over3(M-1)}
 -\left({\ell(\ell-1)\over M-1}\right)^2.}
\tag{2.4}
\]

#### Proof

A cyclic \(k\)-interval is the complement of a cyclic \(\ell\)-interval.
There are \(M-2\ell\) complement intervals avoiding the two coordinates
before accounting for overlap between the two length-\(\ell\) incidence
arcs.  That overlap has size \(\rho_\ell(d)\), proving (2.2).

For each \(j=1,\ldots,\ell-1\), the value \(j\) of \(\rho_\ell\)
occurs twice, and it is zero at every other separation.  Therefore

\[
 \mathbb E\rho_\ell={2\over M-1}\sum_{j=1}^{\ell-1}j
 ={\ell(\ell-1)\over M-1},
\]

\[
 \mathbb E\rho_\ell^2={2\over M-1}\sum_{j=1}^{\ell-1}j^2
 ={\ell(\ell-1)(2\ell-1)\over3(M-1)}.
\]

Together with \(k=M-\ell\), the first identity simplifies to (2.3),
and subtraction of the squared mean gives (2.4).  \(\square\)

For the two rows in the entrance problem, the complementary lengths are

\[
 \ell_m=H,\qquad \ell_r=H+q.
\tag{2.5}
\]

Thus this lemma computes the actual frame columns, not merely their
containment averages.

## 3. The exact Johnson degree-two norm

For a function \(f\) on the rank-\(k\) layer, define its pair compression

\[
 (\mathcal I_kf)(e)=\sum_{Q\supset e}f(Q),
 \qquad e\in\binom{[n]}2.
\tag{3.1}
\]

### Lemma 3.1 (degree-two singular value)

If the degree-zero and degree-one projections of \(f\) vanish, then

\[
 \boxed{
 \|\mathcal I_kf\|_2^2
 =\Lambda_k\|P_2^{(k)}f\|_2^2,
 \qquad
 \Lambda_k=\binom{n-4}{k-2}.}
\tag{3.2}
\]

#### Proof

The adjoint of \(\mathcal I_k\) has image in Johnson degrees at most two,
so \(\mathcal I_k\) annihilates all degrees greater than two.  On the
pair layer, the entries of \(\mathcal I_k\mathcal I_k^*\) are

\[
 A=\binom{n-2}{k-2},\quad
 B=\binom{n-3}{k-3},\quad
 C=\binom{n-4}{k-4}
\]

according as two pairs are equal, meet in one point, or are disjoint.
If \(y\) is in pair degree two, its sum on all pairs and on every
coordinate star is zero.  Hence the sums of \(y\) over pairs meeting a
fixed pair in one point and in zero points are respectively \(-2y_e\)
and \(y_e\).  Thus the eigenvalue is

\[
 A-2B+C=\binom{n-4}{k-2}.
\]

The hypotheses remove the two lower eigenspaces, proving (3.2).
\(\square\)

Choose independently and uniformly one actual cyclic frame on every top.
Put

\[
 f_m=a-{T\over W}{\bf1},\qquad
 f_r=b-{T\over\binom nr}{\bf1},
\tag{3.3}
\]

and let

\[
 R_2=\binom{n-2}{M-2}.
\tag{3.4}
\]

For a fixed pair \(e\), exact double counting and (2.3) give

\[
 (\mathcal I_kf_k)(e)
 =\sum_{U\supset e}
 \left(D_k^{\pi_U}(e)-{k(k-1)\over M-1}\right).
\tag{3.5}
\]

The summands are independent over the \(R_2\) tops containing \(e\).
Using (1.6), Lemma 3.1, and then summing the variances in (3.5), we obtain
the exact identity

\[
 \boxed{
 \mathbb E\|P_2^{(k)}f_k\|_2^2
 ={\binom n2R_2\over\Lambda_k}\sigma_{M-k}^2
 ={R\binom M2\over\Lambda_k}\sigma_{M-k}^2.}
\tag{3.6}
\]

Here the second equality is the flag identity
\(\binom n2R_2=R\binom M2\).

Now

\[
 R=(1+o(1)){W\over m},\qquad
 \Lambda_m=(1/16+o(1))W,\qquad
 \Lambda_r=(1/16+o(1))W,
\tag{3.7}
\]

and, uniformly for \(\ell\in\{H,H+q\}\),

\[
 \sigma_\ell^2=(2/3+o(1)){H^3\over m}.
\tag{3.8}
\]

Therefore (3.6) equals \((16/3+o(1))H^3\) for either rank.  Averaging
over the integral random selections proves the existence of a selection
satisfying (0.2).

Finally, Cauchy--Schwarz and
\(\|\alpha\|_2^2+\|\beta\|_2^2\le B_m^2(W+\binom nr)\) prove
(0.3)--(0.4).  Notice that the one integral selection supplied by the
averaging argument works simultaneously for every normalized degree-two
character.

## 4. The first coupled chronology shell

Define

\[
 \chi_{H,q}(d)=\rho_{H+q}(d)-\rho_H(d).
\tag{4.1}
\]

By (2.2), the centered difference between the entrance and middle pair
counts is exactly the centered version of \(\chi_{H,q}\); the constant
\(-2q\) cancels.  On either orientation of the shorter arc,
\(\chi_{H,q}\) takes the values

\[
 \underbrace{q,\ldots,q}_{H\ {m times}},q-1,q-2,\ldots,1,
\tag{4.2}
\]

and is zero elsewhere.  Consequently

\[
 \mathbb E\chi_{H,q}={q(2H+q-1)\over M-1},
\tag{4.3}
\]

and direct summation gives exactly (0.5).

Let \(G_k=\mathcal I_kf_k\), both regarded as functions on coordinate
pairs.  More explicitly, for every pair \(e\),

\[
 (G_r-G_m)(e)=\sum_{U\supset e}
 \left(\chi_{H,q}(d_{\pi_U}(e))-\mathbb E\chi_{H,q}\right).
\tag{4.4}
\]

Independence over tops now gives

\[
 \mathbb E\|G_r-G_m\|_2^2
 =R\binom M2\tau_{H,q}^2.
\tag{4.5}
\]

Using the middle-rank normalization \(\Lambda_m\),

\[
 \boxed{
 \mathbb E\,{\|G_r-G_m\|_2^2\over\Lambda_m}
 =(16+o(1))Hq^2.}
\tag{4.6}
\]

Thus the first genuinely coupled cyclic chronology mode is a thin distance
shell, not a hidden conserved character.  Equation (4.6) supplies an
integral selection with only polynomial shell discrepancy.

## 5. Exact boundary of the no-go

The theorem rules out the following proposed obstruction:

*project the two actual load rows to Johnson degree two, apply a bounded
linear functional (including a pair-distance shell functional), and obtain
a one-sided gap of order \(W\) for every integral frame selection.*

Indeed (0.3) gives one integral selection whose discrepancy against every
such normalized functional is \(o(W)\).

It does not rule out:

1. a valid inequality involving the nonlinear variables
   \((a_X-1)_+\) and \({\bf1}_{\{b_S=0\}}\);
2. a higher Johnson or genuinely long cyclic-word character;
3. an integral cut whose normalized coefficients grow as fast as
   \(\sqrt{W/H^3}\).

Accordingly the degree-two entrance sector cannot be the missing
\(\Omega(W)\) obstruction.  The next exact target is a nonlinear
support-sensitive chronology inequality or a degree growing with \(m\).
