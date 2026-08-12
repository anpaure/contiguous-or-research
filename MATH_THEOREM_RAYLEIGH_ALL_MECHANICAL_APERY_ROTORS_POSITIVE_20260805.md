# Every rational mechanical Apéry rotor has positive Rayleigh phase

**Date:** 2026-08-05  
**Method:** pure mathematics; Euclidean multiplicity descent, exact
Beatty-cell moments, and Fourier--Parseval domination; no computation,
search, or solver  
**Status:** unconditional.  Every lower mechanical/Christoffel Apéry clock
whose fundamental endpoint period is at most the Rayleigh minimum has
strictly positive complete formal phase functional.  This includes all
primitive binary balanced rotors, at every residue period.  The theorem
does not assert that every extreme ray of the cyclic-superadditive cone is
mechanical.

## 1. Mechanical clocks

Fix integers

\[
 g\ge2,
 \qquad1\le h<g,
\]

and a scale `eta>0`.  Put

\[
 s_r=\eta\left\lfloor{rh\over g}\right\rfloor
 \quad(0\le r\le g),
 \qquad
 P=s_g=h\eta.
\tag{1.1}
\]

The resulting infinite formal clock is

\[
 \boxed{
 U_m=\eta\left\lfloor{mh\over g}\right\rfloor
 \qquad(m\ge0).}
\tag{1.2}
\]

Indeed, for `m=qg+r`,

\[
 qP+s_r
 =\eta\left(qh+\left\lfloor{rh\over g}\right\rfloor\right)
 =\eta\left\lfloor{mh\over g}\right\rfloor.
\]

### Lemma 1.1

The table (1.1) is nonnegative and cyclically superadditive.  Its endpoint
has maximum density `h eta/g`.  It is primitive exactly when
`gcd(g,h)=1`.

#### Proof

For `i+j<=g`, floor superadditivity gives

\[
 \left\lfloor{(i+j)h\over g}\right\rfloor
 \ge
 \left\lfloor{ih\over g}\right\rfloor
 +\left\lfloor{jh\over g}\right\rfloor.
\]

For `i+j>=g`, subtracting the integer `h` gives the carry version of the
same inequality.  Also

\[
 {s_r\over r}
 \le {h\eta\over g}.
\]

Equality at a proper residue occurs exactly when `g` divides `rh`, which
happens for no proper `r` exactly when `gcd(g,h)=1`. \(\square\)

If `d=gcd(g,h)`, then (1.2) is unchanged after replacing `(g,h)` by
`(g/d,h/d)`.  This is the exact fundamental-period collapse.  It is
therefore enough to treat the coprime case.

## 2. Exact Euclidean multiplicity descent

Assume now that `gcd(g,h)=1`, and write

\[
 g=ah+b,
 \qquad a\ge1,
 \qquad0\le b<h.
\tag{2.1}
\]

Let

\[
 \Phi_{g,h}(\eta)
 =\sum_{m\ge0}K\left(\eta\left\lfloor{mh\over g}\right\rfloor\right).
\tag{2.2}
\]

For each output integer `n>=0`, its multiplicity is

\[
\begin{aligned}
 c_n
 &=\#\left\{m\ge0:
 n\le{mh\over g}<n+1\right\}\\
 &=\left\lceil{(n+1)g\over h}\right\rceil
   -\left\lceil{ng\over h}\right\rceil\\
 &=a+delta_n,
\end{aligned}
\tag{2.3}
\]

where

\[
 \delta_n=left\lceil{(n+1)b\over h}\right\rceil
          -\left\lceil{nb\over h}\right\rceil.
\tag{2.4}
\]

If `b=0`, coprimality forces `h=1`, and `delta_n=0`.  If `b>0`, then
`gcd(b,h)=1`, every `delta_n` is zero or one, and

\[
 \boxed{
 \{n:\delta_n=1\}
 =\left\{\left\lfloor{\ell h\over b}\right\rfloor:
            \ell\ge0\right\}.}
\tag{2.5}
\]

To verify (2.5), observe that `delta_n` counts integers `ell` in the
half-open interval

\[
 \left[{nb\over h},{(n+1)b\over h}ight),
\]

whose length is less than one.  Such an integer exists exactly when
`n=floor(ell h/b)`; coprimality removes every nonzero boundary ambiguity.

Consequently

\[
 \boxed{
 \Phi_{g,h}(\eta)
 =aC(\eta)+R_{h,b}(\eta),}
\tag{2.6}
\]

where `R_(h,0)=0`, and for `1<=b<h`,

\[
 R_{h,b}(\eta)
 =\sum_{\ell\ge0}
 K\left(\eta\left\lfloor{\ell h\over b}\right\rfloor\right).
\tag{2.7}
\]

Thus all repeated output levels have been peeled off as `a` complete
arithmetic combs.  The sole residual is a sparse Beatty rotor.

## 3. Exact moments of the sparse Beatty discrepancy

Fix coprime integers `1<=b<p` and put

\[
 P=p\eta,
 \qquad
 R_{p,b}(\eta)
 =\sum_{\ell\ge0}K\left(\eta\left\lfloor{\ell p\over b}\right\rfloor\right).
\tag{3.1}
\]

Let `H(x)` count the clock points in (3.1) below `x`, and define the
equal-work discrepancy

\[
 D(x)=H(x)-{bx\over P}.
\tag{3.2}
\]

The clock satisfies `U_(ell+b)=U_ell+P`, so `D` is `P`-periodic.  Tail
integration and equal work give

\[
 R_{p,b}(\eta)=\int_0^\infty D(x)q(x)dx,
 \qquad q=-K'.
\tag{3.3}
\]

Put

\[
 \rho={b\over p},
 \qquad t={1\over p}.
\tag{3.4}
\]

### Lemma 3.1 (exact Beatty-cell law)

On a uniformly sampled point of one period, `D` has the same distribution
as

\[
 A_p+\rho V,
\tag{3.5}
\]

where `A_p` is uniform on

\[
 \left\{0,{1\over p},\ldots,{p-1\over p}\right\},
\]

`V` is uniform on `(0,1)`, and the two are independent.  Consequently

\[
 \boxed{
 \widehat D_0
 ={1+\rho-t\over2},}
\tag{3.6}
\]

and

\[
 \boxed{
 {1\over P}\int_0^P(D-\widehat D_0)^2
 ={1+\rho^2-t^2\over12}.}
\tag{3.7}
\]

#### Proof

For

\[
 x=\eta(n+u),
 \qquad0\le n<p,
 \qquad0<u<1,
\]

one has

\[
 H(x)=\left\lceil{b(n+1)\over p}\right\rceil.
\]

Hence

\[
 D(x)=
 \left(\left\lceil{b(n+1)\over p}\right\rceil
       -{b(n+1)\over p}\right)
 +\rho(1-u).
\tag{3.8}
\]

As `n+1` runs through a complete residue system modulo `p`, coprimality
makes the first parenthesis a permutation of

\[
 0,{1\over p},\ldots,{p-1\over p}.
\]

The cell index and the within-cell coordinate are independent under
uniform measure.  The two elementary means and variances are

\[
 \mathbb EA_p={p-1\over2p},
 \qquad
 \operatorname {Var}(A_p)={p^2-1\over12p^2},
\]

and

\[
 \mathbb E(\rho V)={\rho\over2},
 \qquad
 \operatorname {Var}(\rho V)={\rho^2\over12}.
\]

Equations (3.6)--(3.7) follow. \(\square\)

## 4. Fourier--Parseval positivity of every sparse rotor

Let

\[
 B={5324\over875}.
\]

The all-period transform theorem gives, for every nonzero integer `n`,

\[
 \left|\int_0^\infty q(x)e^{2\pi i n x/P}dx\right|
 <{BP^2\over4\pi^2n^2}.
\tag{4.1}
\]

Write `Dhat_n` for the normalized Fourier coefficients of `D`.  Parseval
and (3.7) give

\[
 \sum_{n\ge1}|\widehat D_n|^2
 ={1+\rho^2-t^2\over24}.
\tag{4.2}
\]

The Fourier products are absolutely summable by Cauchy--Schwarz.  Pairing
positive and negative frequencies, then using
`zeta(4)=pi^4/90`, gives

\[
\begin{aligned}
 |\text{nonzero modes}|
 &<{BP^2\over2\pi^2}
   \sum_{n\ge1}{|\widehat D_n|\over n^2}\\
 &\le {BP^2\over2\sqrt{90}}
 \left({1+\rho^2-t^2\over24}\right)^{1/2}\\
 &=\boxed{
 {BP^2\over24\sqrt{15}}
 \sqrt{1+\rho^2-t^2}.}
\end{aligned}
\tag{4.3}
\]

The zeroth mode is

\[
 {M\over2}(1+\rho-t).
\tag{4.4}
\]

For `P<=zeta`, the complete duty-cycle Fourier theorem proved the strict
coefficient inequality

\[
 BP^2<12\sqrt{15}M.
\tag{4.5}
\]

Moreover

\[
\begin{aligned}
 (1+\rho-t)^2-(1+\rho^2-t^2)
 &=2(\rho-t)(1-t)\\
 &\ge0,
\end{aligned}
\tag{4.6}
\]

because `rho=b/p>=1/p=t`.  Equations (4.3)--(4.6) show that the zeroth
mode strictly dominates all nonzero modes, even in the equality case
`b=1` of (4.6).  Therefore

\[
 \boxed{
 R_{p,b}(\eta)>0
 \qquad(1\le b<p,\ p\eta\le\zeta).}
\tag{4.7}
\]

## 5. Main theorem

### Theorem 5.1 (all mechanical rotors are positive)

For every mechanical table (1.1), reduce `(g,h)` by their gcd and let
`P_f` be its fundamental endpoint period.  If

\[
 0<P_f\le\zeta,
\]

then

\[
 \boxed{
 \sum_{m\ge0}
 K\left(\eta\left\lfloor{mh\over g}\right\rfloor\right)>0.}
\tag{5.1}
\]

In the coprime case `g=ah+b`, its exact decomposition is

\[
 \Phi_{g,h}(\eta)=aC(\eta)+R_{h,b}(\eta).
\tag{5.2}
\]

If `b=0`, the second term is absent; otherwise it is strictly positive by
(4.7).  Since `C(eta)>377/108000`, one always has at least the explicit
arithmetic reserve

\[
 \Phi_{g,h}(\eta)>a{377\over108000}>0.
\tag{5.3}
\]

#### Proof

Fundamental-period collapse reduces to coprime `(g,h)`.  Apply the exact
Euclidean multiplicity identity (2.6).  The arithmetic part is positive
by the all-mesh comb theorem, and the residual is positive by (4.7).  This
proves (5.1)--(5.3). \(\square\)

## 6. Consequence and exact frontier

Every primitive lower Christoffel/Sturmian increment word is covered,
with no restriction on its residue period or continued-fraction depth.
The period-five rotor `01011` is the first example and is recovered by
`(g,h)=(5,3)`.

The proof does not require iterative Euclidean descent: one quotient
peels all repeated levels into arithmetic combs, and an exact second-moment
law signs the remaining sparse Beatty rotor at once.

This still does not classify all extreme rays of the cyclic-block cone.
In particular, a proof of complete formal Apéry positivity must either
show that a minimizing profile is mechanical, or control the genuinely
nonmechanical extremes and interpolation between them.  The finite
availability shoulder and the occurrence-faithful Boolean theorem remain
separate.

## 7. Dependencies

1. `MATH_THEOREM_RAYLEIGH_DUTY_CYCLE_ALL_APERY_PERIOD_FOURIER_POSITIVITY_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_APERY_FUNDAMENTAL_PERIOD_COLLAPSE_AND_ONE_KINK_COMB_RESERVE_20260805.md`.
