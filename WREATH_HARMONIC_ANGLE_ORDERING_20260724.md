# Harmonic-angle ordering for cross-rank cyclic-interval incidence

## 1. Result and limitation

Let \(n=2m+1\), and let \(\theta_{m,m-q;j}\) be the angle between the
copies of (S^{(n-j,j)}) selected in the common cyclic-order column space
by the all-start matrices (A_m) and (A_{m-q}).  The normalization is the
one in `WREATH_CROSS_RANK_SPECTRAL_20260724.md`, so

\[
 \cos ^2\theta_{s,t;j}=
 {\beta_{s,t,j}^2\|f_{s,j}\|_2^2
  \over \lambda_{s,j}\lambda_{t,j}\|f_{t,j}\|_2^2}.
 \tag{1.1}
\]

This note proves the complete adjacent-rank ordering:

\[
 \boxed{
 \sin ^2\theta_{m,m-1;2}
 <\sin ^2\theta_{m,m-1;j}
 \quad(3\le j\le m-1).}
 \tag{1.2}
\]

Thus degree two is exactly the thinnest harmonic for the first shadow, not
merely asymptotically.  It also gives the fixed-((q,j)) asymptotics at
every depth and computes the Gaussian aggregate of the exact degree-two
leakage:

\[
 \sum_{q\le H}{\binom{2m+1}{m-q}\over\binom{2m+1}{m}}
 \sin ^2\theta_{m,m-q;2}
 ={2+o(1)\over m}
 \quad\left({H\over\sqrt m}\longrightarrow\infty, H=o(m)\right).
 \tag{1.3}
\]

The natural all-depth conjecture is that degree two minimizes leakage for
every \(q\).  Exact rational computation finds no counterexample through
all \(m\le50\), all feasible \(q\), and all \(j\), but this note does not
claim that conjecture.  Proving it would promote (1.3) to a uniform
Gaussian frame-gap theorem on every nontrivial Johnson harmonic.

## 2. Exact adjacent-rank formula

Put

\[
 \ell_{m,j}=\sin ^2\theta_{m,m-1;j}.
\]

### Theorem 2.1 -- every adjacent harmonic

For (m\ge3) and (2\le j\le m-1), the following formulas hold.  If
(j) is even, then

\[
 \boxed{
 \ell_{m,j}=
 {j(j^2-1)(2m-j+2)\over D^{\rm ev}_{m,j}},}
 \tag{2.1}
\]

where

\[
\begin{aligned}
D^{\rm ev}_{m,j}={}&m^4+4m^3-(2j^2-5)m^2\\
 &+(2j^3-4j^2-4j+2)m+2j(j-2)(j+1).
\end{aligned}
\tag{2.2}
\]

If (j) is odd, then

\[
 \boxed{
 \ell_{m,j}={j(2m-j+3)(2m-j+2)(2m-j+1)
 \over D^{\rm odd}_{m,j}},}
 \tag{2.3}
\]

where

\[
\begin{aligned}
D^{\rm odd}_{m,j}={}&9m^4+(36-16j)m^3
 +(10j^2-48j+45)m^2\\
 &+(-2j^3+20j^2-44j+18)m
 -2j(j-2)(j-3).
\end{aligned}
\tag{2.4}
\]

For (j=2), (2.1) cancels a factor (m) and becomes

\[
 \ell_{m,2}={12\over m^3+4m^2-3m-6}.
 \tag{2.5}
\]

#### Derivation

For reference, define the Hahn coefficient

\[
h^{s,t}_j(u)=
\sum_{k=0}^j(-1)^k\binom jk
 \binom{s-j}{u-j+k}
 \binom{n-s-j}{t-u-k}.
\tag{2.6}
\]

Grouping (7.8) of the cross-rank spectral note by (u=|S\cap T|)
gives

\[
 \beta_{s,t,j}=D_s\sum_u h^{s,t}_j(u)p_{s,t}(u).
 \tag{2.7}
\]

Set (s=m,t=m-1,n=2m+1).  Substitute the five cases of
(p_{s,t}(u)) from (7.5), apply Vandermonde's identity to the two proper
overlap ranges, and use

\[
 {\|f_{m,j}\|_2^2\over\|f_{m-1,j}\|_2^2}
 ={\binom{2m+1-2j}{m-j}\over
   \binom{2m+1-2j}{m-1-j}}
 ={m+2-j\over m-j}.
\tag{2.8}
\]

After putting the resulting \(\beta_{m,m-1,j}\),
\(\beta_{m,m,j}\), and \(\beta_{m-1,m-1,j}\) into (1.1), the even and odd
parts reduce respectively to (2.1) and (2.3).  No asymptotic estimate is
used here.  The calculation uses only (2.6), Vandermonde, and cancellation
of falling factorials.  The exact-rational implementation is
`scratch/wreath_cross_rank_spectrum.py`, function
`adjacent_harmonic_leakage_closed_form`.

The parity split has a geometric source.  Complementing a slice harmonic
changes it by ((-1)^j).  The two almost-complementary ranks therefore
have a first-order cancellation for even (j), but not for odd (j).

## 3. Degree two is the exact adjacent minimum

### Theorem 3.1 -- adjacent ordering

For every (m\ge3), degree two is the unique minimum in (1.2).

#### Proof for even (j)

Write (x=m-j-1\ge0).  On taking the difference of (2.1) and (2.5),
the numerator over the positive common denominator is

\[
 (j-2)P_{\rm ev}(j,x),
\tag{3.1}
\]

where

\[
 P_{\rm ev}(j,x)=\sum_{b=0}^4p_b(j)x^b
\]

and

\[
\begin{array}{c|l}
b&p_b(j)\\ \hline
0&72+148j+154j^2+127j^3+61j^4+13j^5+j^6\\
1&168+348j+310j^2+175j^3+50j^4+5j^5\\
2&138+235j+165j^2+65j^3+9j^4\\
3&48+57j+32j^2+7j^3\\
4&6+4j+2j^2.
\end{array}
\tag{3.2}
\]

Every coefficient is positive.  Equality occurs only at (j=2).

#### Proof for odd (j)

Put (y=j-3\ge0), again with (x=m-j-1\ge0).  The numerator of
(ell_{m,j}-ell_{m,2}) over the positive common denominator is

\[
 P_{\rm odd}(y,x)=\sum_{b=0}^6q_b(y)x^b,
\tag{3.3}
\]

where

\[
\begin{array}{c|l}
b&q_b(y)\\ \hline
0&93600+151740y+96064y^2+31837y^3+6064y^4+670y^5+40y^6+y^7\\
1&153960+209882y+109593y^2+28880y^3+4110y^4+302y^5+9y^6\\
2&102768+115340y+47956y^2+9465y^3+898y^4+33y^5\\
3&35484+31898y+9993y^2+1322y^3+63y^4\\
4&6648+4604y+982y^2+66y^3\\
5&636+320y+36y^2\\
6&24+8y.
\end{array}
\tag{3.4}
\]

This is strictly positive.  Equations (3.1)--(3.4) prove the theorem.
\(\square\)

In particular, for fixed (j),

\[
\ell_{m,j}=
\begin{cases}
\displaystyle {2j(j^2-1)\over m^3}+O_j(m^{-4}),&j\text{ even},\\[2mm]
\displaystyle {8j\over9m}+O_j(m^{-2}),&j\text{ odd}.
\end{cases}
\tag{3.5}
\]

The degree-two coefficient is (12); the next even coefficient is (120).

## 4. Fixed-depth asymptotics

The same Hahn calculation gives a useful all-depth expansion.

### Proposition 4.1

For every fixed (j\ge2), uniformly along integer sequences
(1\le q=o(m)), as (m\to\infty),

\[
\boxed{
\sin ^2\theta_{m,m-q;j}=
\begin{cases}
\displaystyle
 \binom{j+1}{3}{2q(q+1)(2q+1)\over m^3}
 \displaystyle\times
 \left(1+O_j\left({q+1\over m}\right)\right),&j\text{ even},\\[3mm]
\displaystyle
 {4j q(q+1)\over3(2q+1)m}
 \displaystyle\times
 \left(1+O_j\left({q+1\over m}\right)\right),&j\text{ odd}.
\end{cases}}
\tag{4.1}
\]

#### Proof

Use (2.7) with (s=m,t=m-q).  After the two Vandermonde sums, divide
the three scalars in (1.1) by their common factorial factor.  For fixed
(j), every remaining term is a product of a bounded number of ratios of
falling factorials whose arguments differ by (O_j(q+1)).  On
(q=o(m)), expand those ratios uniformly; their relative remainders are
(O_j((q+1)/m)).  The constant, first, and second determinant
coefficients cancel for even (j); the first nonzero coefficient is

\[
 2\binom{j+1}{3}q(q+1)(2q+1).
\]

For odd (j), the first determinant coefficient is

\[
 {4j q(q+1)\over3(2q+1)}.
\]

The displayed leading polynomials are positive for every (q\ge1), so
the same relative error remains valid uniformly, including bounded (q).
\(\square\)

Consequently, for every fixed (J), degree two is asymptotically the
unique minimum among (2\le j\le J), uniformly at every depth
(q=o(m)).  For even (j\ge4), the ratio to degree two tends to
\(\binom{j+1}{3}\ge10\).  For odd \(j\), the ratio is asymptotic to

\[
 {2jm^2\over3(2q+1)^2}\longrightarrow\infty.
\]

Formula (4.1) does **not** by itself establish uniformity when (j) grows
with (m).

### Theorem 4.2 -- exact all-depth ordering in degrees three, four, and six

For every feasible (m,q),

\[
 \boxed{
 \sin^2\theta_{m,m-q;3}>\sin^2\theta_{m,m-q;2},}
 \tag{4.2}
\]

and, whenever \(j\in\{4,6\}\) and \(m-q\ge j\),

\[
 \boxed{
 \sin^2\theta_{m,m-q;j}>\sin^2\theta_{m,m-q;2}.}
 \tag{4.3}
\]

These assertions are uniform over the entire depth range, not only fixed
or Gaussian (q).

#### Degree three

Write (ell_{3}=P_3/D_3), where

\[
 P_3=\sum_{i=0}^4p_i(q)m^i
\tag{4.4}
\]

with

\[
\begin{aligned}
p_0={}&2q-q^2-3q^3+q^4+q^5,\\
p_1={}&q^2-8q^3-13q^4-4q^5,\\
p_2={}&-8q+14q^2+46q^3+28q^4+4q^5,\\
p_3={}&-2q-30q^2-40q^3-12q^4,\\
p_4={}&4q+12q^2+8q^3,
\end{aligned}
\tag{4.5}
\]

and

\[
\begin{aligned}
D_3=(2q+1)\big[&(2q+1)m^5-(2q^2+7q+1)m^4\\
 &+(4q^2+4q-3)m^3+(2q^2+7q+1)m^2\\
 &-(4q^2+6q-2)m\big].
\end{aligned}
\tag{4.6}
\]

These expressions follow directly from the Hahn sum (2.7); apparent lower
degrees at (q=1,2) are common-factor cancellations.

Let (N_2,D_2) be the numerator and denominator in the exact degree-two
formula (5.1), and set (x=m-q-3\ge0).  Expanding

\[
 P_3D_2-N_2D_3=\sum_{b=0}^8r_b(q)x^b
\tag{4.7}
\]

gives the following coefficient arrays.  Row (b) lists the coefficients
of (q,q^2,\ldots); omitted entries are zero.

\[
\begin{array}{c|l}
b&[q^1,q^2,\ldots]\\ \hline
0&[18432,84288,160176,163416,96312,32664,5880,432]\\
1&[55296,238624,422212,394558,208840,62122,9532,576]\\
2&[70912,289572,475830,403123,187510,47057,5752,252]\\
3&[50816,196816,298800,225755,89204,17745,1532,36]\\
4&[22280,81989,113916,74721,23690,3328,152]\\
5&[6128,21447,26818,14575,3324,248]\\
6&[1034,3442,3760,1544,192]\\
7&[98,310,280,68]\\
8&[4,12,8].
\end{array}
\tag{4.8}
\]

Every entry is positive, proving (4.2).

#### Degree four

Similarly, (ell_4=P_4/D_4), where the coefficients of (P_4), from
constant through cubic in (m), are

\[
\begin{aligned}
&-36q+16q^2-40q^3-180q^4-104q^5-16q^6,\\
&-76q+120q^2+440q^3+300q^4+56q^5,\\
&-20q-220q^2-280q^3-80q^4,\\
&20q+60q^2+40q^3,
\end{aligned}
\tag{4.9}
\]

and the coefficients of (D_4), from constant through degree six in
(m), are

\[
\begin{aligned}
(&-30q+75q^2+150q^3+45q^4,\\
&-6-134q-100q^2+40q^3+30q^4,\\
&-1-95q^2-90q^3-15q^4,\\
&10+70q+70q^2+20q^3,\\
&-30q-10q^2, -4+4q, 1).
\end{aligned}
\tag{4.10}
\]

Put (x=m-q-4\ge0).  The coefficient arrays of

\[
 P_4D_2-N_2D_4
\tag{4.11}
\]

as a polynomial in (x), again starting at (q^1), are

\[
\begin{array}{c|l}
b&[q^1,q^2,\ldots]\\ \hline
0&[180000,658800,956160,702720,276480,55440,4320]\\
1&[384000,1324620,1772112,1165920,397080,66900,4248]\\
2&[328950,1085892,1350876,792960,227910,30252,1368]\\
3&[149610,477234,551190,282750,65112,6072,144]\\
4&[39468,122604,130050,55680,9222,456]\\
5&[6084,18540,17670,5730,516]\\
6&[510,1536,1266,240]\\
7&[18,54,36].
\end{array}
\tag{4.12}
\]

This proves (4.3).  The coefficientwise positivity suggests a possible
route to all even (j): derive (P_j,D_j) before specializing (j), then
show positivity after (m=q+j+x).  At present the degree of those
polynomials grows with (j), and no uniform factorization has been found.

#### Degree six

One further even harmonic can be completed exactly.  Write
\(\ell_6=P_6/D_6\).  The coefficients of \(P_6\), from constant through
degree five in \(m\), are

\[
\begin{aligned}
(&-400q+176q^2-3738q^3-9674q^4-7910q^5-3066q^6-552q^7-36q^8,\\
&104q+4200q^2+18886q^3+24990q^4+12726q^5+2730q^6+204q^7,\\
&1498q-11046q^2-26320q^3-18480q^4-5208q^5-504q^6,\\
&434q+8330q^2+12180q^3+4900q^4+616q^5,\\
&-490q-2310q^2-2240q^3-420q^4,\\
&70q+210q^2+140q^3).
\end{aligned}
\tag{4.13}
\]

The coefficients of \(D_6\), from constant through degree eight in \(m\),
are

\[
\begin{aligned}
(&-280q+1890q^2+4095q^3+2975q^4+1225q^5+175q^6,\\
&-120-1644q-5383q^2-5544q^3-595q^4+630q^5+140q^6,\\
&34+3045q-224q^2-4305q^3-2450q^4-525q^5-35q^6,\\
&203+1484q+4445q^2+4200q^3+1015q^4+70q^5,\\
&-91-2100q-2205q^2-1050q^3-105q^4,\\
&-70+714q+378q^2+84q^3,\quad
56-105q-21q^2,\quad -13+6q,\quad1).
\end{aligned}
\tag{4.14}
\]

After \(x=m-q-6\), direct expansion of
\(P_6D_2-N_2D_6\) has 69 nonzero monomials \(q^ax^b\); every coefficient
is positive.  Its \(x\)-degrees run from zero through nine and every row
has a factor \(q\).  This proves the \(j=6\) instance of (4.3).  The exact
coefficient expansion and equality with the Hahn formula are audited by
the checker function degree_six_leakage_closed_form.

## 5. Exact degree-two Gaussian aggregate

The all-depth degree-two formula is

\[
\ell_{m,q;2}=
{2q(q+1)((2q+1)m-(2q^2+2q-1))
\over
(m^2-1)(m^2+(2q+1)m-3q(q+1))}.
\tag{5.1}
\]

For (m\ge8) and (1\le q\le m/4), direct comparison of the two
factors gives absolute constants (c,C>0) such that

\[
 c{q^3\over m^3}\le\ell_{m,q;2}
 \le C{q^3\over m^3}.
\tag{5.2}
\]

More precisely, for (q=x\sqrt m) with (x) in a fixed compact subset
of ((0,\infty)),

\[
 m^{3/2}\ell_{m,q;2}\longrightarrow4x^3.
\tag{5.3}
\]

Also

\[
 {N_q\over W}={\binom{2m+1}{m-q}\over\binom{2m+1}{m}}
 \longrightarrow e^{-x^2}.
\tag{5.4}
\]

### Proposition 5.1 -- Gaussian frame mass

If (H/\sqrt m\to\infty) and (H=o(m)), then

\[
 \boxed{
 \sum_{q=1}^{H}{N_q\over W}\ell_{m,q;2}
 ={2+o(1)\over m}.}
\tag{5.5}
\]

#### Proof

Equations (5.2) and the elementary ratio bound
(N_q/W\le\exp(-c_0q^2/m)) give an integrable dominating function after
the scaling (q=x\sqrt m).  Equations (5.3)--(5.4) therefore turn the
sum into a Riemann integral:

\[
\begin{aligned}
m\sum_{q\le H}{N_q\over W}\ell_{m,q;2}
&\longrightarrow
4\int_0^\infty x^3e^{-x^2}\,dx\\
&=2.
\end{aligned}
\]

The range (q>m/4) is exponentially negligible, and the hypothesis on
\(H\) makes the upper limit tend to infinity after scaling. \(\square\)

Thus the worst known single-depth conditioning (m^{3/2}) is not the
conditioning of the whole Gaussian-weighted band: degree two carries total
relative frame mass \(\Theta(m^{-1})\), corresponding to a
\(\Theta(\sqrt m)\) norm penalty.

If the all-depth ordering

\[
 \sin ^2\theta_{m,m-q;j}\ge
 \sin ^2\theta_{m,m-q;2}
 \qquad(2\le j\le m-q)
\tag{5.6}
\]

is proved, (5.5) immediately gives the same (2/m) lower frame gap on
every nontrivial harmonic.  This is the precise remaining spectral lemma.
It is substantially sharper than treating the ranks independently.

There is also an exact limit for the integer capacity weight used in the
weighted-overload transfer.  Put

\[
 d_q=\left\lfloor {W\over N_q}\right\rfloor.
\tag{5.7}
\]

### Proposition 5.2 -- floor-capacity frame mass

Under the same hypotheses on \(H\),

\[
 \boxed{
 \sum_{q=1}^{H}{\ell_{m,q;2}\over d_q}
 ={C_{\rm cap}+o(1)\over m},}
\tag{5.8}
\]

where

\[
\begin{aligned}
C_{\rm cap}
&=4\int_0^\infty{x^3\,dx\over\lfloor e^{x^2}\rfloor}\\
&=\sum_{k=2}^{\infty}{(\log k)^2\over k(k-1)}
=2.336313176\ldots .
\end{aligned}
\tag{5.9}
\]

#### Proof

For \(q=x\sqrt m\), one has \(W/N_q\to e^{x^2}\), away from the
measure-zero threshold set \(e^{x^2}\in\mathbb Z\), while (5.3) still
holds.  Also, for every \(\lambda\ge1\),

\[
 {1\over\lfloor\lambda\rfloor}\le {2\over\lambda}.
\]

Thus Proposition 5.1 supplies an integrable dominating function and the
Riemann limit is the first integral in (5.9).  Setting \(y=x^2\) and
partitioning the integral over
\([\log k,\log(k+1))\) gives

\[
 2\sum_{k\ge1}{1\over k}
 \int_{\log k}^{\log(k+1)}y\,dy
 =\sum_{k\ge2}{(\log k)^2\over k(k-1)}.
\]

The series converges absolutely. \(\square\)

Hence the actual floor-capacity Hessian, not only its smooth Gaussian
surrogate, has degree-two frame mass \(\Theta(m^{-1})\).

## 6. A rank-two semiseparable clue

Fix \(m,j\), and form the Gram matrix of all rank copies

\[
 G^{(j)}_{r,s}
 =\left\langle A_r^{\mathsf T}f_{r,j},
 A_s^{\mathsf T}f_{s,j}\right\rangle,
 \qquad j\le r,s\le m.
\tag{6.1}
\]

Exact rational computation gives the striking identity

\[
 \left(G^{(j)}\right)^{-1}_{r,s}=0
 \qquad\text{whenever }|r-s|>2
\tag{6.2}
\]

for every \(m\le12\) and every feasible \(j\).  Equivalently, every
strictly off-diagonal block of \(G^{(j)}\) has rank at most two.  This is
exactly the precision pattern of a second-order Gaussian Markov chain.

For \(j=2\), every interior precision row, after normalization by its
diagonal, is

\[
 \left({1\over6},-{2\over3},1,-{2\over3},{1\over6}\right),
\tag{6.3}
\]

the discrete biharmonic stencil.  This explains both the cubic
\(q^3/m^3\) leakage and the integrated \(m^{-1}\) Gaussian frame mass.
For larger \(j\), the five coefficients vary with the rank but retain the
same sign pattern in every exact instance checked.

The two-arc formula strongly suggests a proof of (6.2): after the Hahn
transform, the proper-overlap kernel should be a rank-two semiseparable
Green kernel, with the disjointness and containment cases supplying its
two boundary conditions.  Establishing this symbolically would reduce the
all-\(j\) ordering to comparison of a pentadiagonal precision recurrence,
rather than comparison of the growing rational expressions \(P_j/D_j\).

At present (6.2) is a verified structural conjecture, not used in any
theorem above.  The exact audit is the checker option
--verify-precision-band 12.

## 7. Computation

`scratch/wreath_cross_rank_spectrum.py` now contains:

* the exact formula `adjacent_harmonic_leakage_closed_form`;
* an exact verification of (2.1)--(2.5) and (1.2) through (m=50);
* exact all-depth degree-\(3,4,6\) formulas and ordering through \(m=50\);
* an exact all-\((m,q,j)\) counterexample search through \(m=50\);
* the precision-band audit through \(m=12\).

The command

```text
python3 scratch/wreath_cross_rank_spectrum.py \
  --m 8 --q 2 --verify-adjacent-grid 50 \
  --verify-low-harmonics 50 --search-ordering-grid 50 \
  --verify-precision-band 12
```

ends with

```text
ADJACENT ALL-HARMONIC FORMULA AND ORDERING VERIFIED THROUGH m=50
ALL-DEPTH DEGREE-3/4/6 FORMULAS AND ORDERING VERIFIED THROUGH m=50
NO DEGREE-TWO ORDERING COUNTEREXAMPLE THROUGH m=50
RANK-COPY GRAM INVERSE BANDWIDTH TWO VERIFIED THROUGH m=12
```

The unrestricted finite search is evidence only for (5.6); Theorems 3.1
and 4.2 are exact proofs in their stated ranges.
