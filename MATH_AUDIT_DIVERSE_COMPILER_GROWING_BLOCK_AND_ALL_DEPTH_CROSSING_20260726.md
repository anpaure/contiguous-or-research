# Diverse compiler: growing-block threshold and all-depth crossing audit

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Audited conclusion

Let

\[
 D_{m,b,q}=\sum_k
 \left(
   \#\{T\in\tbinom{[2m]}{m-q}:F_b(T)=k\}
  -\#\{X\in\tbinom{[2m]}m:F_b(X)=k\}
 \right)_+ ,
\]

where \(F_b\) counts full blocks in a fixed partition into \(b\)-sets.
Put

\[
                         \Lambda_b={2^b\over b}.
\]

The uniform saddle theorem in
MATH_THEOREM_GROWING_BLOCK_PROFILE_SADDLE_THRESHOLD_20260726.md
is correct. In particular:

\[
 {D_{m,b,A\sqrt m}\over W}
 =\exp\left[-\left({A^2\over4}+o(1)\right)\Lambda_b\right]
\tag{0.1}
\]

when \(b\to\infty\) and \(2^b=o(\sqrt m)\), while the deficient
depth-\(A\sqrt m\) profiles disappear exactly when

\[
                         2^b>(2/A+o(1))\sqrt m.
\tag{0.2}
\]

For the simultaneous band, whenever
\(b\to\infty\) and \(2^b=o(\sqrt{bm})\) (a range containing the sharp
transition),

\[
 \boxed{
 {1\over W}\sum_{q\le A\sqrt m}D_{m,b,q}
 =\left({2\over3\sqrt\pi}+o(1)\right)
 { \sqrt m\over\Lambda_b^{3/2}}.}
\tag{0.3}
\]

The complementary sparse-full-block range has \(o(W)\) aggregate deficit
by the coupling bound proved in Section 3. Thus the sharp no-crossing
escape for the whole band is

\[
 \boxed{\Lambda_b\gg m^{1/3},}
\tag{0.4}
\]

not merely \(b\to\infty\). The critical block size is

\[
 b={1\over3}\log_2m+\log_2\log_2m+O(1).
\tag{0.5}
\]

In the rank-twisted construction, the coordinate-union components are
the macroblocks \(B_j=A_j\dot\cup C_j\), of size

\[
                         b=2d.
\tag{0.6}
\]

They are not the \(Q_R\)-packet supports. Therefore the exact all-depth
condition is

\[
 \boxed{
 {2^{2d}\over2d}\gg m^{1/3}
 \quad\Longleftrightarrow\quad
 d>{1\over6}\log_2m+{1\over2}\log_2\log_2m+\omega(1).}
\tag{0.7}
\]

The standard \(d=10\log_2m\) construction satisfies (0.7) with enormous
slack. The compiler scale

\[
 R\asymp\sqrt{mH}\asymp m^{3/4}
\]

does not enter the full-block invariant. It controls trace diversity and
cycle length only.

## 1. Why \(b=2d\), not \(R\)

In one rank-twisted macroblock,

\[
 B_j=A_j\dot\cup C_j,\qquad |A_j|=|C_j|=d,
\]

the local rank-\(k\) frame is a perfect matching
\(M_{j,k}\subseteq A_j\times C_j\). For the cyclic twist,

\[
                         \bigcup_kM_{j,k}=K_{d,d}.
\tag{1.1}
\]

Hence the graph formed by every physical Johnson axis which can occur in
any rank layer has connected components exactly \(B_j\), each of size
\(2d\).

A retained \(Q_R\) packet selects \(R\) pairwise disjoint split edges,
usually from many different \(B_j\)'s. Its active coordinate support has
size \(2R\), but two owner-disjoint packets need not have disjoint
coordinate supports. Consequently those supports are not a partition of
\([2m]\), and no \(F_R\) invariant is defined by them.

The diverse compiler then applies a bijection from its abstract
directions to the already selected physical edges. It creates no new
physical edge. Thus it neither joins two macroblocks nor changes (1.1).
This proves (0.6).

Relative to any fixed bounded quartet refinement whose parts lie inside
the two halves, every edge of \(A_j\times C_j\) is cross-quartet. Hence
every nonempty compiler window pays the old bounded-block crossing toll.
Relative to the macroblock partition, every edge is internal. The two
statements are consistent because the relevant block scales differ.

## 2. The one-depth threshold

Let

\[
 A(r,k)=\#\{Y\in\tbinom{[2m]}r:F_b(Y)=k\}.
\]

The one-block rank/full-indicator array is TP\(_2\), and convolution
preserves TP\(_2\). Therefore

\[
                         {A(m,k)\over A(m-q,k)}
\tag{2.1}
\]

is nondecreasing in \(k\). The deficient profiles are an initial
interval.

With

\[
 h_b(z)=(1+z)^b-z^b,\qquad
 a_b={b2^{b-1}\over2^b-1},
\]

the exact profile counts are

\[
 A(r,k)=\binom{2m/b}{k}[z^{r-bk}]h_b(z)^{2m/b-k}.
\tag{2.2}
\]

If

\[
 \delta_{b,k}={m\over2^b-1}-a_bk,
\]

then the two coefficient indices in (2.2) are displaced from their
common mean by \(\delta_{b,k}\) and \(\delta_{b,k}-q\). The uniform
central saddle gives

\[
 \log{A(m,k)\over A(m-q,k)}
 ={q^2-2q\delta_{b,k}\over m+o(m)}+o(1).
\tag{2.3}
\]

Thus the real likelihood crossing is

\[
 \kappa_{m,b,q}
 ={m/(2^b-1)-q/2\over a_b}.
\tag{2.4}
\]

At \(q=A\sqrt m\), the target full-block count must fall by
\((A+o(1))\sqrt m/b\) below its mean to reach (2.4). Its conditional
variance is

\[
                         {2m\over b2^b}(1+o(1)).
\]

The resulting moderate-deviation cost is

\[
 {1\over2}
 {A^2m/b^2\over2m/(b2^b)}
 = {A^2\over4}\Lambda_b,
\]

which proves (0.1). At \(k=0\), equation (2.3) changes sign at
\(2^b=2\sqrt m/A\). Exact monotonicity then proves (0.2).

## 3. Why the all-depth threshold is \(m^{1/3}\)

Set

\[
 \varepsilon_b={2b\over2^b}={2\over\Lambda_b},
 \qquad
 z_q={q\over\sqrt{\varepsilon_bm}}.
\tag{3.1}
\]

The source and target full-block means differ by

\[
                         {2q\over2^b}(1+o(1)),
\]

and their common conditional variance is

\[
                         {2m\over b2^b}(1+o(1)).
\]

Therefore the standardized mean difference is
\(\varepsilon_bz_q(1+o(1))\), while

\[
                         \log{W\over N_q}
 =\varepsilon_bz_q^2+o(\varepsilon_b).
\]

For a target standardized profile \(x\), the exact coefficient saddle,
after subtracting the two neighboring rank coefficients, gives the
local asymptotic-normal likelihood

\[
 \log{A(m,k)\over A(m-q,k)}
 =\varepsilon_bz_q(z_q+x)+o(\varepsilon_b).
\tag{3.2}
\]

TP\(_2\) says the negative-likelihood set is \(x<-z_q+o(1)\).
Integrating \(1-\exp(\varepsilon_bz_q(z_q+x))\) over this normal tail
gives

\[
 {D_{m,b,q}\over W}
 =\varepsilon_bz_q
 \{\phi(z_q)-z_q\Phi(-z_q)\}
 +o(\varepsilon_b).
\tag{3.3}
\]

The exponential tilt also gives an integrable envelope
\[
 {D_{m,b,q}\over W}
 \le C\varepsilon_bz_q(1+z_q)e^{-cz_q^2}.
\]

The \(z_q\)-mesh is \(1/\sqrt{\varepsilon_bm}\), and
\(z_{A\sqrt m}\to\infty\). Hence

\[
 {1\over W}\sum_{q\le A\sqrt m}D_{m,b,q}
 =(1+o(1))\sqrt{\varepsilon_bm}\,\varepsilon_b
 \int_0^\infty z\{\phi(z)-z\Phi(-z)\}\,dz.
\tag{3.4}
\]

Now

\[
 \int_0^\infty z\phi(z)\,dz={1\over\sqrt{2\pi}},
\qquad
 \int_0^\infty z^2\Phi(-z)\,dz
 ={2\over3\sqrt{2\pi}}.
\]

The integral in (3.4) is \(1/(3\sqrt{2\pi})\), which proves (0.3).
Equation (0.4) follows immediately.

The LAN proof applies throughout the transition range. If the expected
full-block count no longer diverges, couple a uniform target to a uniform
middle extension. Then

\[
 {D_{m,b,q}\over N_q}
 \le d_{\rm TV}(F_b(T),F_b(X))
 \le Cq2^{-b}.
\]

Deficient profiles can occur only for \(q=O(m/2^b)\), by (2.4).
Summation gives

\[
 {1\over W}\sum_qD_{m,b,q}
 \le C{m^2\over b^3\Lambda_b^3}=o(1)
\]

in the complementary sparse-full-block regime. Thus no unexamined large
\(b=o(m)\) interval remains.

## 4. Exact named scales

Let \(b=c\log_2m\).

* At the single depth \(q=A\sqrt m\), the deficit is
  \[
  {D_{m,b,q}\over W}
  =\exp\left[-\left({A^2\over4c}+o(1)\right)
                   {m^c\over\log_2m}\right]
  \]
  for \(c<1/2\), and it is exactly zero eventually for \(c>1/2\).
* Across all \(q\le A\sqrt m\),
  \[
  {1\over W}\sum_qD_{m,b,q}
  =\left({2\over3\sqrt\pi}+o(1)\right)
    (c\log_2m)^{3/2}m^{(1-3c)/2}.
  \]
  Hence the all-depth transition is \(c=1/3\), with the logarithmic
  correction in (0.5).
* For \(b=m^\alpha\), \(0<\alpha<1\), the full-block deficit is exactly
  zero eventually at every Gaussian depth.
* A hypothetical disjoint partition into
  \(b=R\asymp m^{3/4}\) blocks is also far beyond the zero-deficit
  threshold. Actual packet supports do not form such a partition, so this
  observation cannot itself be used as a physical invariant.

For the actual \(b=2d\) macroblocks:

* \(d=C\log_2m\) passes the all-depth test iff \(C>1/6\);
* the depth-\(H\) deficit is exactly absent iff \(C>1/4\); and
* \(d=10\log_2m\) passes both.

## 5. Transverse moves: exact necessary density

Let \(E_q^\pm\) count signed depth-\(q\) window occurrences containing
at least one move between two prescribed \(b\)-blocks, and let
\(M_q^\pm\) be the signed target holes.

An internal move preserves every block rank. A lower intersection can
lose a full block only at the first cross-block move removing one of its
coordinates; complementation gives the upper statement. Therefore,
outcome by outcome,

\[
 \boxed{
 E_q^\pm+M_q^\pm\ge D_{m,b,q}.}
\tag{5.1}
\]

Summing and using (0.3),

\[
 {1\over W}\sum_{q\le A\sqrt m}E_q^\pm
 \ge
 \left({2\over3\sqrt\pi}+o(1)\right)
 { \sqrt m\over\Lambda_b^{3/2}}-o(1)
\tag{5.2}
\]

whenever the total signed hole budget is \(o(W)\).

One physical cross transition belongs to at most \(q\) cyclic
depth-\(q\) windows. Let \(C\) be the number of cross transitions. For

\[
 q\asymp\sqrt{m/\Lambda_b},
\]

equation (3.3) gives \(D_{m,b,q}\asymp W/\Lambda_b\). On a fixed
constant-factor interval of such depths, \(E_q^\pm\le qC\).
Consequently, whenever \(\Lambda_b=O(m^{1/3})\) and the total hole budget
is \(o(W)\),

\[
 \boxed{
 {C\over W}=\Omega\left({1\over\sqrt{m\Lambda_b}}\right).}
\tag{5.3}
\]

At the critical all-depth scale this is
\(\Omega(W/m^{2/3})\) physical cross transitions and
\(\Omega(W)\) total exceptional signed window occurrences.

For fixed \(b\), (5.1) at \(q=A\sqrt m\) instead requires
\(\Omega_{A,b}(W)\) exceptional windows. For
\(\Lambda_b\gg m^{1/3}\), the full-block dual requires no asymptotically
nonzero all-depth crossing budget.

## 6. Exact boundary for the diverse compiler

The rank-twisted construction with \(d=10\log_2m\) genuinely escapes
every full-macroblock Farkas deficit, both signs and all
\(q\le A\sqrt m\). This is a proved positive statement about that exact
dual.

It does not prove coefficient one. If the \(R\) selected axes are
localized in a physical carrier \(E\) of size \(\Theta(R)\), the separate
target/source capacity ratio is

\[
 \exp(-\Theta(q^2/R))
 =\exp(-\Theta(m^{1/4}))
\]

at \(q=A\sqrt m\). Thus the surviving exact construction gate is a
dispersed selected-axis Hall theorem followed by one common all-depth,
both-sign integral covariance choice. Increasing \(R\) alone does not
address either gate.
