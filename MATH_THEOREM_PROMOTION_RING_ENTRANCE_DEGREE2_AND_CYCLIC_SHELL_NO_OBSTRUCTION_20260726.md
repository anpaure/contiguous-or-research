# Promotion-ring entrance coupling: exact degree-two action and cyclic-shell no-obstruction theorem

Date: 2026-07-26

Method: pure mathematics.  All columns below are literal cyclic frames, and
all selections are integral (one frame for every top).

## 0. Outcome

Put

\[
 n=2m,\qquad q=\lceil m^{1/4}\rceil,\qquad
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad M=m+H,
\]

and let

\[
 W=\binom{n}{m},\qquad N=\binom{n}{m-q},\qquad
 R=\binom{n}{M},\qquad T=MR.
\tag{0.1}
\]

We use the tuned regime from
`MATH_THEOREM_PROMOTION_RING_ENTRANCE_COUPLED_LP_DUAL_20260726.md`:

\[
 T=(1+o(1))W,\qquad N=(1+o(1))W.
\tag{0.2}
\]

For a cyclic frame \(\pi\) on a top \(U\), the middle and entrance rows
are respectively the cyclic intervals of lengths \(m\) and \(m-q\).
The first nonconstant choice-dependent pair kernel of a length-
\(k=M-L\) row is exactly

\[
 \boxed{\tau_L(d)=
 (L-d)_+ +(L-M+d)_+-\frac{L(L-1)}{M-1}}
 \qquad(1\le d<M).
\tag{0.3}
\]

Thus the middle kernel is \(\tau_H\), the entrance kernel is
\(\tau_{H+q}\), and their genuinely chronology-sensitive difference is

\[
 \eta_{H,q}=\tau_{H+q}-\tau_H.
\tag{0.4}
\]

The note proves the following exact statements.

1. Every four-point Johnson degree-two character has, on an actual frame
   column, the alternating-pair value of (0.3).  Formula (3.6) below is
   the exact action, including top-containment indicators.

2. If \(P_{k,2}\) denotes orthogonal projection onto Johnson degree two
   on \(\binom{[n]}k\), then independent uniform integral frames satisfy

   \[
   \mathbb E\|P_{k,2}z_k\|_2^2
   =\frac{RM}{2\binom{n-4}{k-2}}
    \left[
      \frac{L(L-1)(2L-1)}3
      -\frac{L^2(L-1)^2}{M-1}
    \right],
   \tag{0.5}
   \]

   where \(z_k\) is the centered aggregate load and \(L=M-k\).
   Consequently the two expectations for \(k=m,m-q\) sum to

   \[
     \left(\frac{32}{3}+o(1)\right)H^3.
   \tag{0.6}
   \]

3. There is therefore a literal integral one-frame-per-top selection
   \(F\) such that

   \[
   \boxed{
   \|P_{m,2}z_m(F)\|_2^2+
   \|P_{m-q,2}z_{m-q}(F)\|_2^2=O(H^3).}
   \tag{0.7}
   \]

   For every pair of degree-two test functions with
   \(\|w_k\|_\infty\le m^C\), where \(C\) is fixed,

   \[
   |\langle w_m,z_m(F)\rangle|
    +|\langle w_{m-q},z_{m-q}(F)\rangle|=o(W).
   \tag{0.8}
   \]

4. The same selection may be chosen so that its raw two-rank chronology
   shell \(D_{m-q}-D_m\) obeys

   \[
   \|D_{m-q}-D_m\|_2^2=O(WHq^2).
   \tag{0.9}
   \]

   Hence every polynomially bounded integral pair-character evaluates to
   \(o(W)\) on this shell.

5. Averaging the coordinate-relabelling orbit of this one selection gives
   the uniform fractional frame point.  Every orbit member retains
   (0.7) and (0.9).  Therefore **the complete Johnson degree-two sector,
   including the first middle--entrance cyclic shell, cannot supply an
   \(\Omega(W)\) integral separating inequality under any fixed
   polynomial coefficient normalization.**

This does not prove the desired \(o(W)\) collision/hole rounding.  It
proves that an obstruction must use Johnson degree at least three, or a
nonlinear coverage/odd-set condition which is not determined by the
degree-two loads.  In particular, quadratic energy of the *whole* load
is not being claimed small.

## 1. Frames, loads, and pair incidence

For \(1\le k<M\), write a cyclic frame as

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

with indices modulo \(M\), and put

\[
 I_t^{(k)}(\pi)=\{u_t,u_{t+1},\ldots,u_{t+k-1}\}.
\tag{1.1}
\]

Its rank-\(k\) column vector is

\[
 f_{U,\pi}^{(k)}=\sum_{t=0}^{M-1}\mathbf 1_{I_t^{(k)}(\pi)}
 \in\mathbb R^{\binom{[n]}k}.
\tag{1.2}
\]

An integral selection \(F\) chooses one \(\pi_U\) for each of the \(R\)
tops, and its load and centered load are

\[
 \ell_k(F)=\sum_U f_{U,\pi_U}^{(k)},\qquad
 z_k(F)=\ell_k(F)-\frac{T}{\binom nk}\mathbf1.
\tag{1.3}
\]

For a vector \(g\) on the rank-\(k\) layer, define its pair-incidence
vector

\[
 (I_kg)_{xy}=\sum_{S\supseteq\{x,y\}}g(S)
 \qquad(x<y).
\tag{1.4}
\]

We abbreviate

\[
 D_k(F)=I_kz_k(F).
\tag{1.5}
\]

The total and every coordinate degree of \(z_k(F)\) are zero.  Indeed
every frame contains \(M\) intervals, and each coordinate of its top lies
in exactly \(k\) of them.  It follows also that

\[
 \sum_{y\ne x}D_k(F)_{xy}=0
 \qquad(x\in[n]).
\tag{1.6}
\]

Thus \(D_k(F)\) lies in the degree-two pair module.

## 2. Exact Johnson degree-two normalization

Let \(E_{k,2}\) be the second Johnson module on \(\binom{[n]}k\), and
let \(P_{k,2}\) be its orthogonal projection in counting measure.  The
degree-two pair module is

\[
 E_{2,2}=\left\{
   a\in\mathbb R^{\binom{[n]}2}:
   \sum_{y\ne x}a_{xy}=0\quad\hbox{for every }x
 \right\}.
\tag{2.1}
\]

Its dimension is

\[
 d_2=\binom n2-n=\frac{n(n-3)}2.
\tag{2.2}
\]

### Lemma 2.1 (exact singular value of pair incidence)

On \(E_{2,2}\),

\[
 I_kI_k^*=\Lambda_k\,\mathrm{Id},\qquad
 \boxed{\Lambda_k=\binom{n-4}{k-2}}.
\tag{2.3}
\]

Consequently, whenever \(g\) has zero degree-zero and degree-one parts,

\[
 \boxed{
 \|P_{k,2}g\|_2^2
 =\frac{\|I_kg\|_2^2}{\binom{n-4}{k-2}}.}
\tag{2.4}
\]

#### Proof

Let \(a\in E_{2,2}\) and fix a pair \(P\).  In
\((I_kI_k^*a)_P\), a pair \(Q\) has coefficient
\(\binom{n-|P\cup Q|}{k-|P\cup Q|}\).  The zero-star equations give

\[
 \sum_{|P\cap Q|=1}a_Q=-2a_P,
 \qquad
 \sum_{P\cap Q=\varnothing}a_Q=a_P.
\tag{2.5}
\]

Therefore

\[
\begin{aligned}
 (I_kI_k^*a)_P
 &=\left[
 \binom{n-2}{k-2}-2\binom{n-3}{k-3}
 +\binom{n-4}{k-4}
 \right]a_P\\
 &=\binom{n-4}{k-2}a_P.
\end{aligned}
\]

The range of \(I_k^*\) consists of Johnson degrees at most two, so
\(I_k\) kills every degree above two.  It also preserves the orthogonal
decomposition into the three lower modules.  If \(g\) has no degree zero
or one, then \(I_kg=I_kP_{k,2}g\), and (2.4) follows from (2.3). \(\square\)

For four distinct coordinates \(a,b,c,d\), define the standard
four-point character

\[
 \chi_{ab\mid cd}^{(k)}(S)
 =\bigl(\mathbf1_{a\in S}-\mathbf1_{b\in S}\bigr)
  \bigl(\mathbf1_{c\in S}-\mathbf1_{d\in S}\bigr).
\tag{2.6}
\]

It belongs to \(E_{k,2}\), these characters span \(E_{k,2}\), and its
exact norm is

\[
 \|\chi_{ab\mid cd}^{(k)}\|_2^2
 =4\binom{n-4}{k-2}=4\Lambda_k.
\tag{2.7}
\]

The last identity follows because the character is nonzero precisely
when the set contains one of \(a,b\) and one of \(c,d\).

## 3. Exact action of one actual cyclic-frame column

For distinct \(x,y\in U\), let \(d_\pi(x,y)\in\{1,\ldots,M-1\}\) be the
directed distance from \(x\) to \(y\) in \(\pi\).  Let

\[
 w_{M,k}(d)=(k-d)_++(k-M+d)_+.
\tag{3.1}
\]

### Lemma 3.1 (pair count)

The number of cyclic rank-\(k\) intervals containing both \(x\) and \(y\)
is \(w_{M,k}(d_\pi(x,y))\).  If \(L=M-k<M/2\), then

\[
 w_{M,k}(d)=2k-M+(L-d)_++(L-M+d)_+.
\tag{3.2}
\]

#### Proof

There are \((k-d)_+\) starts whose forward interval meets \(x\) before
\(y\), and \((k-(M-d))_+\) starts which meet them in the other order.
This gives (3.1).  Substitute \(k=M-L\) and check separately
\(d<L\), \(L\le d\le M-L\), and \(d>M-L\) to obtain (3.2). \(\square\)

Averaging over uniform cyclic frames of a fixed top makes the relative
distance uniform on \(\{1,\ldots,M-1\}\).  Since

\[
 \sum_{d=1}^{M-1}\bigl((L-d)_++(L-M+d)_+\bigr)=L(L-1),
\tag{3.3}
\]

the choice-dependent centered pair count is exactly (0.3).  Let

\[
 \bar f_U^{(k)}=\mathbb E_\pi f_{U,\pi}^{(k)},\qquad
 \widehat f_{U,\pi}^{(k)}=f_{U,\pi}^{(k)}-\bar f_U^{(k)}.
\tag{3.4}
\]

Then

\[
 \boxed{
 (I_k\widehat f_{U,\pi}^{(k)})_{xy}
 =\mathbf1_{\{x,y\}\subseteq U}\,
   \tau_{M-k}(d_\pi(x,y)).}
\tag{3.5}
\]

Before centering, the exact actual-column action is

\[
\begin{aligned}
 \langle f_{U,\pi}^{(k)},\chi_{ab\mid cd}^{(k)}\rangle
 ={}&\mathbf1_{\{a,c\}\subseteq U}w_{M,k}(d_\pi(a,c))
    -\mathbf1_{\{a,d\}\subseteq U}w_{M,k}(d_\pi(a,d))\\
   &-\mathbf1_{\{b,c\}\subseteq U}w_{M,k}(d_\pi(b,c))
    +\mathbf1_{\{b,d\}\subseteq U}w_{M,k}(d_\pi(b,d)).
\end{aligned}
\tag{3.6a}
\]

After centering, with the convention that a term is zero when its pair is
not contained in \(U\), the action is

\[
\boxed{
\begin{aligned}
 \langle\widehat f_{U,\pi}^{(k)},\chi_{ab\mid cd}^{(k)}\rangle
 ={}&\tau_{M-k}(d_\pi(a,c))
    -\tau_{M-k}(d_\pi(a,d))\\
   &-\tau_{M-k}(d_\pi(b,c))
    +\tau_{M-k}(d_\pi(b,d)).
\end{aligned}}
\tag{3.6}
\]

This is the requested actual-column formula.  Notice that the large
constant \(2k-M\) in (3.2) is fixed by the top and disappears under frame
choice; globally its pair counts are coordinate-uniform because every top
is used once.

For every \(x\in U\), the other points of \(U\) occupy the distances
\(1,\ldots,M-1\) once each.  Equation (3.3) therefore gives

\[
 \sum_{y\in U\setminus\{x\}}
 \tau_L(d_\pi(x,y))=0.
\tag{3.7}
\]

Thus the pair vector in (3.5) already lies exactly in \(E_{2,2}\), not
merely after a further projection.

## 4. Exact cyclic chronology shell

Put \(\rho(d)=\min(d,M-d)\).  Since \(H+q<M/2\) for large \(m\), define

\[
 \delta_{H,q}=\frac{2Hq+q^2-q}{M-1}.
\tag{4.1}
\]

Then (0.4) is exactly

\[
 \boxed{
 \eta_{H,q}(d)=
 \begin{cases}
 q-\delta_{H,q},&1\le\rho(d)\le H,\\
 H+q-\rho(d)-\delta_{H,q},&H<\rho(d)<H+q,\\
 -\delta_{H,q},&\rho(d)\ge H+q.
 \end{cases}}
\tag{4.2}
\]

Here

\[
 \delta_{H,q}=O(m^{-1/4}\sqrt{\log m})=o(1).
\tag{4.3}
\]

For the same frame on the two rows, subtraction of (3.5) gives

\[
 \boxed{
 I_{m-q}\widehat f_{U,\pi}^{(m-q)}
 -I_m\widehat f_{U,\pi}^{(m)}
 =\left(
 \mathbf1_{\{x,y\}\subseteq U}\eta_{H,q}(d_\pi(x,y))
 \right)_{xy}.}
\tag{4.4}
\]

This is the first nontrivial cyclic entrance chronology character.  It is
a thin distance shell, not an additional coordinate-degree constraint.

For completeness, let \(\omega=e^{2\pi i/M}\).  Extend the uncentered
triangular kernel to the diagonal by \(a_L(0)=L\).  Its usual
autocorrelation transform is

\[
 \sum_{d=0}^{M-1}a_L(d)\omega^{td}
 =\left|\sum_{j=0}^{L-1}\omega^{tj}\right|^2
 =\frac{\sin^2(\pi tL/M)}{\sin^2(\pi t/M)}.
\tag{4.5}
\]

The degree-two pair kernel, however, has zero diagonal and the centering
in (0.3).  Its correct nonzero-frequency symbol is

\[
 \boxed{
 \widehat\tau_L(t)=
 \frac{\sin^2(\pi tL/M)}{\sin^2(\pi t/M)}
 -L+\frac{L(L-1)}{M-1}}
 \qquad(1\le t<M),
\tag{4.6}
\]

while \(\widehat\tau_L(0)=0\).  The circulant has zero diagonal and is
nonzero, so the sum of its eigenvalues is zero and it has both positive
and negative eigenvalues.  The same statement holds for the nonzero
shell (4.2).  Hence positivity of the full interval autocorrelation in
(4.5) is a diagonal/degree-one baseline and is not a one-sided
degree-two invariant.

## 5. Exact second moment under integral random frames

Define

\[
 V_{M,L}=
 \frac{L(L-1)(2L-1)}3
 -\frac{L^2(L-1)^2}{M-1}.
\tag{5.1}
\]

### Lemma 5.1 (one-column degree-two norm)

For every top and every cyclic frame,

\[
 \|I_k\widehat f_{U,\pi}^{(k)}\|_2^2
 =\frac M2V_{M,L},\qquad L=M-k,
\tag{5.2}
\]

and

\[
 \|P_{k,2}\widehat f_{U,\pi}^{(k)}\|_2^2
 =\frac{M}{2\Lambda_k}V_{M,L}.
\tag{5.3}
\]

#### Proof

Every directed distance occurs \(M\) times, so every unordered pair is
counted twice in the directed sum.  Also

\[
 \sum_{d=1}^{M-1}
 \bigl((L-d)_++(L-M+d)_+\bigr)^2
 =2\sum_{j=1}^{L-1}j^2
 =\frac{L(L-1)(2L-1)}3.
\]

Subtracting the square of the mean in (3.3) gives (5.2).  Equations
(3.7) and (2.4) give (5.3). \(\square\)

Choose independently and uniformly one frame on every top.  The vectors
\(\widehat f_{U,\pi_U}^{(k)}\) are independent and mean zero.  Moreover

\[
 \sum_U\bar f_U^{(k)}=\frac{T}{\binom nk}\mathbf1
\tag{5.4}
\]

by coordinate transitivity and total mass.  Therefore

\[
 z_k=\sum_U\widehat f_{U,\pi_U}^{(k)}.
\tag{5.5}
\]

Orthogonality of independent mean-zero summands and (5.3) prove the exact
identity

\[
 \boxed{
 \mathbb E\|P_{k,2}z_k\|_2^2
 =\frac{RM}{2\Lambda_k}V_{M,M-k}.}
\tag{5.6}
\]

Since

\[
 \frac{\Lambda_k}{\binom nk}
 =\frac{k(k-1)(n-k)(n-k-1)}
 {n(n-1)(n-2)(n-3)}
 =\frac1{16}+o(1)
\tag{5.7}
\]

for \(k=m,m-q\), while \(RM=(1+o(1))W\), and

\[
 V_{M,L}=\left(\frac23+o(1)\right)L^3
\tag{5.8}
\]

uniformly for \(L=H,H+q\), equation (0.5) and then (0.6) follow.

### Lemma 5.2 (exact shell second moment)

Let

\[
 V^{\rm sh}_{M,H,q}
 =2Hq^2+\frac{(q-1)q(2q-1)}3
 -\frac{(2Hq+q^2-q)^2}{M-1}.
\tag{5.9}
\]

For independent uniform integral frames,

\[
 \boxed{
 \mathbb E\|D_{m-q}-D_m\|_2^2
 =\frac{RM}{2}V^{\rm sh}_{M,H,q}
 =O(WHq^2).}
\tag{5.10}
\]

#### Proof

For one top, (4.4) is conditionally mean zero.  Before subtracting its
mean, the shell has value \(q\) at each distance
\(1,\ldots,H\), and values \(q-1,\ldots,1\) at the next \(q-1\)
distances, on both sides of the cycle.  Thus its directed square sum is

\[
 2Hq^2+2\sum_{j=1}^{q-1}j^2.
\]

Subtracting the squared mean gives (5.9).  Multiply the unordered pair
sum by \(M/2\), then sum variances over the \(R\) independent tops. \(\square\)

## 6. Integral annihilation of the entire degree-two sector

### Theorem 6.1 (one integral selection balances both degree-two rows and
the chronology shell)

There is an integral one-frame-per-top selection \(F\) for which

\[
 \|P_{m,2}z_m(F)\|_2^2=O(H^3),\qquad
 \|P_{m-q,2}z_{m-q}(F)\|_2^2=O(H^3),
\tag{6.1}
\]

and

\[
 \|D_{m-q}(F)-D_m(F)\|_2^2=O(WHq^2).
\tag{6.2}
\]

#### Proof

Normalize each of the three nonnegative random variables in (5.6) and
(5.10) by its positive expectation and add them.  The expectation of the
sum is three, so some integral outcome has normalized sum at most three.
Each summand is then at most three.  Equations (5.6)--(5.10) give
(6.1)--(6.2). \(\square\)

### Corollary 6.2 (no bounded integral degree-two separator)

Fix \(C<\infty\).  Let

\[
 w_m\in E_{m,2},\qquad w_{m-q}\in E_{m-q,2},\qquad
 \alpha\in\mathbb R^{\binom{[n]}2}
\]

have all coefficients bounded in absolute value by \(m^C\).  For the
selection in Theorem 6.1,

\[
\begin{aligned}
 &|\langle w_m,z_m(F)\rangle|
 +|\langle w_{m-q},z_{m-q}(F)\rangle|\\
 &\hspace{28mm}
 +|\langle\alpha,D_{m-q}(F)-D_m(F)\rangle|=o(W).
\end{aligned}
\tag{6.3}
\]

#### Proof

Cauchy--Schwarz and (6.1) give, for either target layer,

\[
 |\langle w_k,z_k(F)\rangle|
 \le m^C\sqrt{\binom nk}\,O(H^{3/2})
 =m^{O(1)}\sqrt W=o(W).
\tag{6.4}
\]

Similarly (6.2) gives

\[
 |\langle\alpha,D_{m-q}-D_m\rangle|
 \le m^C\sqrt{\binom n2}\,O(\sqrt{WH}\,q)
 =m^{O(1)}\sqrt W=o(W).
\tag{6.5}
\]

The last asymptotic uses \(W=\binom{2m}{m}\), which dominates every
fixed polynomial in \(m\). \(\square\)

Let \(\mathfrak B_2\) be the set of integral selections satisfying
(6.1)--(6.2) with sufficiently large absolute constants.  It is invariant
under coordinate relabelling and is nonempty by Theorem 6.1.

### Corollary 6.3 (degree-two convex-hull inclusion)

The uniform fractional frame point \(\bar x\) belongs to

\[
 \boxed{\bar x\in\operatorname{conv}(\mathfrak B_2).}
\tag{6.6}
\]

#### Proof

Take \(F\in\mathfrak B_2\).  Every coordinate relabelling of \(F\) stays
in \(\mathfrak B_2\), because all three norms are invariant.  The average
of the \(S_n\)-orbit of \(F\) is \(\bar x\): the group is transitive on
all formal cyclic-frame columns, and every integral selection contains
exactly one column over each top.  Hence the orbit average proves (6.6).
\(\square\)

## 7. Exact boundary

Equations (3.6) and (4.2) completely identify the first nontrivial
Johnson/cyclic chronology characters of the actual coupled columns.
They are real and nonzero, but they are neither one-sided invariants nor
macroscopic integral discrepancies.  The integral selection in Theorem
6.1 makes their entire polynomial-dimensional sector negligible on the
\(W\)-scale, and (6.6) rules out a convex separation of the uniform frame
point from such degree-two-balanced integral selections.

What remains possible is narrower and genuinely nonlinear: an inequality
may couple collision/hole indicators to higher chronology, or impose an
odd-set condition invisible to the two load vectors and their pair
moments.  This theorem does not put the low-defect selections themselves
in the convex hull.  It does prove that no \(\Omega(W)\) obstruction can
come from a linearly normalized degree-two Johnson character or from the
first middle--entrance cyclic shell alone.
