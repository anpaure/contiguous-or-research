# Promotion-ring entrance: exact degree-two character and its subcritical integral energy

Date: 2026-07-26

Method: pure mathematics only.  Every column below is an actual cyclic
frame.  No slot relaxation, computation, search, or generic rounding
theorem is used.

## 0. Result

Use the notation of
`MATH_THEOREM_PROMOTION_RING_ENTRANCE_COUPLED_LP_DUAL_20260726.md`:

\[
 n=2m,\qquad q_0=\lceil m^{1/4}\rceil,\qquad
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad M=m+H,
\tag{0.1}
\]

\[
 r=m-q_0,\qquad W=\binom{2m}m,\qquad
 N=\binom{2m}r,\qquad R=\binom{2m}M,\qquad T=MR.
\tag{0.2}
\]

For an integral selection (F=(\pi_U)_U) of one oriented cyclic frame
on every (M)-top, let (a(F)) and (b(F)) be its middle and entrance
load vectors.  Write \(\Pi_2^{(k)}\) for orthogonal projection onto the
degree-two Johnson module on \(\binom{[2m]}k\).

Define, for (2\ell<M),

\[
 \Xi(M,\ell)
 ={M\ell(\ell-1)(2\ell-1)\over6}
 -{M\ell^2(\ell-1)^2\over2(M-1)}.
\tag{0.3}
\]

Then there is an integral actual-frame selection (F) for which

\[
\boxed{
\begin{aligned}
 &\left\|\Pi_2^{(m)}
       \left(a(F)-{T\over W}\mathbf1\right)\right\|_2^2
 +\left\|\Pi_2^{(r)}
       \left(b(F)-{T\over N}\mathbf1\right)\right\|_2^2\\
 &\qquad\le
 R\left{
 {\Xi(M,H)\over\binom{2m-4}{m-2}}
 +{\Xi(M,H+q_0)\over\binom{2m-4}{r-2}}
 \right}\\
 &\qquad=
 \left({32\over3}+o(1)\right)H^3=o(W).
\end{aligned}}
\tag{0.4}
\]

The estimate is simultaneous over the entire degree-two module, whose
dimension is \(\binom{2m}2-2m\).  Consequently, for every pair of
degree-two Johnson characters \(f,g\) satisfying

\[
 \|f\|_\infty\le1,\qquad \|g\|_\infty\le1,
\tag{0.5}
\]

the same integral selection satisfies

\[
\boxed{
 \left|
 \langle a(F)-T\mathbf1/W,f\rangle
 +\langle b(F)-T\mathbf1/N,g\rangle
 \right|
 =O(H^{3/2}\sqrt W)=o(W).}
\tag{0.6}
\]

The local cyclic chronology is not zero.  If
\(\omega=e^{2\pi i/M}\), its exact nonconstant Fourier eigenvalues are

\[
 \boxed{
 \rho_{\ell,s}
 =\left|{1-\omega^{s\ell}\over1-\omega^s}\right|^2
   -\ell+{\ell(\ell-1)\over M-1},
 \qquad 1\le s<M.}
\tag{0.7}
\]

In particular \(\rho_{\ell,1}=\Theta(\ell^2)\) for
\(\ell\in\{H,H+q_0\}\).  Thus a genuine first cyclic mode is present in
every frame column.  Formula (0.4) proves that its label-conjugates, and
indeed all cyclic pair modes together, can nevertheless be balanced
integrally at total Johnson energy (o(W)).

The first character which directly compares the two coupled rows is the
distance shell

\[
 \chi_{H,q_0}(d)=\kappa_{H+q_0}(d)-\kappa_H(d).
\tag{0.8}
\]

Its exact one-top variance is

\[
\boxed{
 \tau_{H,q_0}^2=
 {2Hq_0^2+q_0(q_0-1)(2q_0-1)/3\over M-1}
 -\left({q_0(2H+q_0-1)\over M-1}\right)^2
 =(2+o(1)){Hq_0^2\over m}.}
\tag{0.9}
\]

If (G_m,G_r) are the pair compressions of the two centered load rows,
there is an integral frame selection for which

\[
 \boxed{
 {\|G_r-G_m\|_2^2\over\binom{2m-4}{m-2}}
 \le(16+o(1))Hq_0^2=o(W).}
\tag{0.10}
\]

Thus the literal coupled entrance chronology shell is not conserved and
also has only subcritical integral energy.

Therefore neither a bounded linear degree-two character nor a bounded
positive quadratic form supported on the degree-two projections can be
an \(\Omega(W)\) invariant obstruction to entrance rounding.  This does
not construct a low-defect entrance packing: it closes only the proposed
degree-two/one-pair chronology obstruction.  Any surviving integral cut
must couple degree at least three, or couple coverage support to chronology
nonlinearly rather than merely charging the degree-two load projection.

There is also a direct conditional separation audit.  If a selection has
\(\Delta(F)=T-W+o(W)\), then both complete load vectors are
\(o(W)\)-close in \(\ell^1\) to load one.  Hence every bounded
nonconstant Johnson character, degree two included, has value (o(W)) on
that selection, while it has value zero at the uniform fractional point.
Thus a linear \(\Omega(W)\) separator of the good-selection hull cannot
live in this sector either.

## 1. Degree-two Johnson coordinates

Let \(\mathcal P=\binom{[2m]}2\).  The degree-two pair space is

\[
 \mathcal H_2=
 \left\{w\in\mathbb R^{\mathcal P}:
     \sum_{j\ne i}w_{\{i,j\}}=0\text{ for every }i\right\}.
\tag{1.1}
\]

The row equations imply \(\sum_{e\in\mathcal P}w_e=0\).  For
\(2\le k\le2m-2\), define

\[
 (J_kw)(S)=\sum_{e\in\binom S2}w_e,
 \qquad S\in\binom{[2m]}k.
\tag{1.2}
\]

The image \(J_k\mathcal H_2\) is the degree-two Johnson module.

### Lemma 1.1 (exact inclusion normalization)

For every \(w\in\mathcal H_2\),

\[
 \boxed{
 \|J_kw\|_2^2=\Lambda_k\|w\|_2^2,
 \qquad \Lambda_k=\binom{2m-4}{k-2}.}
\tag{1.3}
\]

#### Proof

Let \(D_k\) be the adjoint pair-sum operator.  The coefficient of
\(w_f\) in \((D_kJ_kw)_e\) is

\[
 \binom{2m-|e\cup f|}{k-|e\cup f|}.
\]

For fixed (e), the sum of (w_f) over pairs (f\ne e) sharing one
endpoint with (e) is \(-2w_e\), by the row equations.  The sum over
pairs disjoint from (e) is (w_e), because the total pair sum is zero.
Therefore

\[
 D_kJ_kw=
 \left[
 \binom{2m-2}{k-2}
 -2\binom{2m-3}{k-3}
 +\binom{2m-4}{k-4}
 \right]w.
\]

Two applications of Pascal's identity reduce the bracket to
\(\binom{2m-4}{k-2}\).  Taking the inner product with (w) proves
(1.3). \(\square\)

For a target vector (y), put

\[
 (D_ky)_e=\sum_{S\supset e}y_S.
\tag{1.4}
\]

If (y) has zero total and zero coordinate-star sums and
\(z=D_ky\in\mathcal H_2\), then Lemma 1.1 and adjointness give

\[
 \boxed{
 \Pi_2^{(k)}y=J_k(z/\Lambda_k),\qquad
 \|\Pi_2^{(k)}y\|_2^2={\|z\|_2^2\over\Lambda_k}.}
\tag{1.5}
\]

Indeed the right side has the same inner product as (y) against every
vector (J_kw) in the degree-two module.

## 2. The exact pair character of one cyclic frame

Fix an (M)-top (U), an oriented cyclic frame \(\pi\), and a length
\(k=M-\ell\), where (2\ell<M).  Let \(v_{U,k}^{\pi}\) be the zero-one
incidence vector of its (M) cyclic (k)-intervals, embedded in
\(\binom{[2m]}k\).  Let

\[
 \bar v_{U,k}=\mathbb E_\pi v_{U,k}^{\pi}
\tag{2.1}
\]

under the uniform cyclic frame on (U), and put
\(y_{U,k}^{\pi}=v_{U,k}^{\pi}-\bar v_{U,k}\).

Every coordinate of (U) belongs to exactly (k) cyclic (k)-intervals,
both before and after averaging.  Hence (y_{U,k}^{\pi}) has zero total
and zero coordinate-star sums.

For two positions at cyclic distance (d), the number of cyclic
\(\ell\)-intervals containing both is

\[
 \kappa_\ell(d)=
 \begin{cases}
  \ell-d,&1\le d\le\ell-1,\\
  0,&\ell\le d\le M/2,
 \end{cases}
\tag{2.2}
\]

with the symmetric interpretation (d=\min(t,M-t)).  Its pair average is

\[
 \mu_\ell={\ell(\ell-1)\over M-1}.
\tag{2.3}
\]

Complementing intervals inside (U) gives the exact identity

\[
 \kappa_{M-\ell}(d)-\mu_{M-\ell}
 =\kappa_\ell(d)-\mu_\ell.
\tag{2.4}
\]

Thus the pair moment \(z_{U,k}^{\pi}=D_ky_{U,k}^{\pi}\) is supported on
pairs in (U) and equals

\[
 z_{U,k}^{\pi}(\{x,x'\})
 =\kappa_\ell(d_\pi(x,x'))-\mu_\ell.
\tag{2.5}
\]

For every (x\in U), summing (2.5) over (x'\ne x) gives zero:
both the actual and averaged pair counts equal (k(k-1)).  Hence
\(z_{U,k}^{\pi}\in\mathcal H_2\).

### Lemma 2.1 (exact one-frame norm)

For every frame \(\pi\),

\[
 \boxed{\|z_{U,k}^{\pi}\|_2^2=\Xi(M,\ell).}
\tag{2.6}
\]

#### Proof

Because \(\ell<M/2\), there are exactly (M) unordered position pairs
at each distance (1\le d\le\ell-1\).  Therefore

\[
 \sum_{\{x,x'\}\subset U}\kappa_\ell(d_\pi(x,x'))^2
 =M\sum_{j=1}^{\ell-1}j^2
 ={M\ell(\ell-1)(2\ell-1)\over6}.
\tag{2.7}
\]

Also

\[
 \sum_{\{x,x'\}\subset U}\kappa_\ell(d_\pi(x,x'))
 =M\binom\ell2
 =\binom M2\mu_\ell.
\tag{2.8}
\]

Subtracting the constant mean in (2.5) gives

\[
 \sum(\kappa_\ell-\mu_\ell)^2
 =\sum\kappa_\ell^2-\binom M2\mu_\ell^2,
\]

which is exactly (0.3). \(\square\)

Combining (1.5) and (2.6) yields the exact local projection energy

\[
 \left\|\Pi_2^{(k)}y_{U,k}^{\pi}\right\|_2^2
 ={\Xi(M,\ell)\over\Lambda_k}.
\tag{2.9}

### Lemma 2.2 (the local cyclic spectrum)

In the cyclic position basis, the centered pair matrix (2.5) has zero
constant eigenvalue and, on the Fourier vector
\((1,\omega^s,\ldots,\omega^{s(M-1)})\), (1\le s<M\), eigenvalue
\(\rho_{\ell,s}\) from (0.7).

#### Proof

Let (B_\ell) be the cyclic interval-position incidence matrix.  Its
Fourier eigenvalues are

\[
 \widehat B_\ell(s)={1-\omega^{s\ell}\over1-\omega^s}.
\]

The matrix (B_\ell^*B_\ell) counts interval cooccurrences and has
eigenvalues \(|\widehat B_\ell(s)|^2\).  Its diagonal is \(\ell\).
Removing the diagonal and then subtracting the off-diagonal mean
\(\mu_\ell\) gives

\[
 B_\ell^*B_\ell-(\ell-\mu_\ell)I-\mu_\ell J.
\]

The constant eigenvalue is zero by (2.3).  On every nonconstant Fourier
vector, (J) vanishes, giving (0.7). \(\square\)

For (s=1) and \(\ell=o(M)), the sine form gives

\[
 \left|{1-\omega^{\ell}\over1-\omega}\right|^2
 =\left({\sin(\pi\ell/M)\over\sin(\pi/M)}\right)^2
 =(1+o(1))\ell^2,
\tag{2.10}
\]

so \(\rho_{\ell,1}=\Theta(\ell^2)\).  This verifies that the first
chronology character is real and nontrivial; it is not an artefact of
averaging away the cyclic order.

### Lemma 2.3 (exact coupled distance shell)

Let (q=q_0) and put

\[
 \chi_{H,q}(d)=\kappa_{H+q}(d)-\kappa_H(d).
\tag{2.11}
\]

For either orientation of the shorter cyclic arc, its nonzero values are

\[
 \underbrace{q,\ldots,q}_{H\ {m times}},q-1,q-2,\ldots,1.
\tag{2.12}
\]

Consequently its mean over the (M-1) oriented separations is

\[
 \overline\chi={q(2H+q-1)\over M-1},
\tag{2.13}
\]

and its variance is exactly (0.9).

#### Proof

For distances (1\le d\le H), enlarging an interval from (H) to
(H+q) adds (q) common starts.  For (d=H+j),
(1\le j<q), it adds (q-j); after that it adds none.  The same list
occurs in the reverse orientation.  Hence

\[
 \sum_d\chi_{H,q}(d)=2Hq+q(q-1),
\]

and

\[
 \sum_d\chi_{H,q}(d)^2
 =2Hq^2+{q(q-1)(2q-1)\over3}.
\]

Divide by (M-1) and subtract the square of the mean. \(\square\)

## 3. Integral simultaneous balancing over all tops

Choose the frame on every top independently and uniformly.  For fixed
layer (k), the pair defects \(z_{U,k}^{\pi_U}\) are independent,
have coordinatewise mean zero, and have the deterministic squared norm
(2.6).  Hence

\[
 \mathbb E\left\|\sum_Uz_{U,k}^{\pi_U}\right\|_2^2
 =R\Xi(M,\ell).
\tag{3.1}
\]

The uniform frame mean summed over all tops is constant on the target
layer.  Thus

\[
 a(F)-{T\over W}\mathbf1
 =\sum_Uy_{U,m}^{\pi_U},
 \qquad
 b(F)-{T\over N}\mathbf1
 =\sum_Uy_{U,r}^{\pi_U}.
\tag{3.2}
\]

Equations (1.5) and (3.1) now give the exact expectations

\[
 \mathbb E\left\|\Pi_2^{(m)}
       (a(F)-T\mathbf1/W)\right\|_2^2
 ={R\Xi(M,H)\over\binom{2m-4}{m-2}},
\tag{3.3}
\]

\[
 \mathbb E\left\|\Pi_2^{(r)}
       (b(F)-T\mathbf1/N)\right\|_2^2
 ={R\Xi(M,H+q_0)\over\binom{2m-4}{r-2}}.
\tag{3.4}
\]

Some integral outcome is no larger than the expectation of their sum,
proving the first inequality in (0.4).

There is an equally literal coupled calculation.  Regard the pair
compressions

\[
 G_m=D_m(a-T\mathbf1/W),\qquad
 G_r=D_r(b-T\mathbf1/N)
\tag{3.4a}
\]

as vectors on the same ground-coordinate pair set.  For a fixed pair,
the constant term (-2q_0) in the difference between its large-interval
counts cancels after centering.  Its one-top contribution is exactly

\[
 \chi_{H,q_0}(d_{\pi_U})-\overline\chi.
\]

Independence and Lemma 2.3 therefore give

\[
 \mathbb E\|G_r-G_m\|_2^2
 =R\binom M2\tau_{H,q_0}^2.
\tag{3.4b}
\]

Using (R=(1+o(1))W/m),
\(\binom M2=(1+o(1))m^2/2\),
\(\binom{2m-4}{m-2}=(1/16+o(1))W\), and (0.9), the normalized
expectation is ((16+o(1))Hq_0^2).  Some integral outcome attains at
most this expectation, proving (0.10).

It remains to evaluate it.  Uniformly for
\(\ell\in\{H,H+q_0\}\),

\[
 \Xi(M,\ell)=\left({1\over3}+o(1)\right)M\ell^3,
\tag{3.5}
\]

because \(\ell/M=o(1)\).  Also

\[
 R=(1+o(1)){W\over m},
\tag{3.6}
\]

and, since (q_0=o(\sqrt m)),

\[
 \binom{2m-4}{m-2}=\left({1\over16}+o(1)\right)W,
 \qquad
 \binom{2m-4}{r-2}=\left({1\over16}+o(1)\right)W.
\tag{3.7}
\]

Since (M/m\to1) and \((H+q_0)/H\to1\), substitution gives
\((32/3+o(1))H^3\).  Finally

\[
 H^3=(m\log m)^{3/2}=o(W),
\]

which completes (0.4).

For (0.6), the selected (F) from (0.4) satisfies

\[
\begin{aligned}
 &|\langle a(F)-T\mathbf1/W,f\rangle
   +\langle b(F)-T\mathbf1/N,g\rangle|\\
 &\quad\le
 \left(\|\Pi_2^{(m)}(a-T\mathbf1/W)\|_2^2
       +\|\Pi_2^{(r)}(b-T\mathbf1/N)\|_2^2\right)^{1/2}
 (\|f\|_2^2+\|g\|_2^2)^{1/2}\\
 &\quad=O(H^{3/2}\sqrt W)=o(W),
\end{aligned}
\]

because \(N\le W\) and (0.5) gives
\(\|f\|_2^2+\|g\|_2^2\le W+N\le2W\).

### Proposition 3.1 (a good selection has no bounded linear character gap)

Let (h_m=|\{X:a_X(F)=0\}|) and
(h_r=|\{S:b_S(F)=0\}|).  Then

\[
 \Delta(F)=T-W+h_m+h_r,
\tag{3.8}
\]

and

\[
 \|a(F)-\mathbf1\|_1=T-W+2h_m,
 \qquad
 \|b(F)-\mathbf1\|_1=T-N+2h_r.
\tag{3.9}
\]

#### Proof

For any nonnegative integral load vector (L) on (K) targets with
total mass (S\ge K), occurrence conservation gives

\[
 \sum_x(L_x-1)_+=S-K+|\{x:L_x=0\}|.
\tag{3.10}
\]

Apply this to the middle layer.  Its collision term is
(T-W+h_m), while the entrance term in the objective is (h_r),
proving (3.8).  Adding positive and negative deviations from one proves
(3.9), first with (K=W) and then with (K=N). \(\square\)

If \(\Delta(F)=T-W+o(W)\), then (h_m+h_r=o(W)).  Since
\(T-W=o(W)\) and (T-N=o(W)), (3.9) gives both \(\ell^1\) bounds
(o(W)).  Every nonconstant Johnson character has coordinate sum zero,
so for bounded (f,g)

\[
 |\langle a(F)-T\mathbf1/W,f\rangle|
 =|\langle a(F)-\mathbf1,f\rangle|=o(W),
\]

and likewise at the entrance.  This proves the conditional claim in the
outcome without assuming the existence of such an (F).

## 4. Exact boundary

Proved here:

1. the exact degree-two Johnson character of every actual middle and
   entrance cyclic-frame column;
2. the exact local cyclic Fourier spectrum, including the nonzero first
   chronology mode;
3. the exact coupled middle--entrance distance-shell variance and its
   subcritical integral energy;
4. the exact expectation (3.3)--(3.4) for an integral one-frame-per-top
   selection; and
5. an integral selection whose complete two-layer degree-two energy is
   \((32/3+o(1))H^3=o(W)\).

Consequently the first nonconstant pair/chronology sector has no forced
\(\Omega(W)\) energy and no bounded linear character gap.  In particular,
the nonzero local Fourier mode does not align coherently across the top
fibres.

Not proved here:

1. the integral selection furnished by expectation need not have
   \(o(W)\) coverage deficiency;
2. a character inequality which couples degree-two phase with the support
   indicators \(\mathbf1_{\{a_X>0\}}\) or
   \(\mathbf1_{\{b_S>0\}}\) is not reduced to the quadratic energy above;
3. degree at least three, parity/odd-set constraints, and nonlinear
   chronology--coverage coupling remain open.

Thus this is a rigorous no-go for the isolated degree-two obstruction,
not a proof of entrance rounding and not a coefficient-one conclusion.
