# Independent audit: period-nine two-ninth train and complete positivity

**Date:** 2026-08-04  
**Audited theorem:**  
MATH_THEOREM_APERY_PERIOD9_H3_TWO_NINTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md  
**Audited SHA-256:**  
65dddbe77a805cfa5b0308f3e555801234437a383ca18ce9bbb92d5ec5b716d7  
**Verdict:** **GO.**  The new train lemma, terminal-suffix geometry, pair
ledger, and final margin are all exact.  No computation or search is used.

## 1. Derivative identity and the point \(2/9\)

With

\[
 h(x)=xe^{-\pi x^2/4},
\]

direct differentiation of the compact term and every Gaussian tail gives

\[
 f'(u)={\pi\over2}
 \left(\sum_{q\ge0}h(1+u+q)-h(1-u)\right).
\tag{1.1}
\]

At \(u=2/9\), the adverse term is \(h(7/9)\).  The first positive ratio is

\[
 {h(11/9)\over h(7/9)}
 ={11\over7}e^{-2\pi/9}.
\]

Since \(2\pi/9>69/100\), the cubic Taylor lower bound is

\[
 e^{2\pi/9}>
 {11896809\over6000000}>{55\over28},
\]

where the last comparison is

\[
 11896809\cdot28=333110652>330000000.
\]

Thus this ratio is less than \(4/5\).

The second ratio is

\[
 {h(20/9)\over h(7/9)}
 ={20\over7}e^{-13\pi/12}.
\]

The theorem uses \(13\pi/12>17/5\) and

\[
 e^{17/5}>
 \left({19\over7}\right)^3{37\over25}
 ={253783\over8575}>{200\over7}.
\]

The final inequality is
\[
 253783\cdot7=1776481>1715000.
\]
Hence the second ratio is less than \(1/10\).

For \(z\ge20/9\),

\[
 {h(z+1)\over h(z)}
 \le {29\over20}e^{-49\pi/36}.
\]

Since \(49\pi/36>4\) and

\[
 \left({19\over7}\right)^4
 ={130321\over2401}>{87\over2},
\]

this ratio is less than \(1/30\).  Therefore all positive terms divided
by the adverse term sum to less than

\[
 {4\over5}+{1/10\over1-1/30}
 ={131\over145}<1.
\tag{1.2}
\]

This proves \(f'(2/9)<0\).

## 2. Propagation of monotonicity

For

\[
 R_q(u)={h(1+u+q)\over h(1-u)},
\]

one has

\[
 {d\over du}\log R_q(u)
 ={1\over1+u+q}+{1\over1-u}
 -{\pi\over2}(q+2).
\tag{2.1}
\]

If \(q=0\) and \(2/9\le u\le1/2\), the two rational terms equal
\(2/(1-u^2)\le8/3<\pi\).  If \(q\ge1\), they are at most

\[
 {9\over20}+2={49\over20},
\]

while the last term is at least \(3\pi/2>9/2\).  Thus every \(R_q\)
strictly decreases.  Their sum remains below one by (1.2), proving

\[
                         f'(u)<0
 \qquad(2/9\le u\le1/2).
\tag{2.2}
\]

No interchange of conditionally convergent series occurs: all derivative
trains converge absolutely and uniformly on this compact interval.

## 3. Exact endpoint certificate

At \(u=2/9\), the first three adverse exponentials give

\[
 f(2/9)
 <1-e^{-49\pi/324}
    -e^{-121\pi/324}
    -e^{-100\pi/81}.
\tag{3.1}
\]

For \(0<x<3\),

\[
 e^x<1+x+{x^2\over2(1-x/3)}
\tag{3.2}
\]

because \(n!\ge2\cdot3^{n-2}\) for \(n\ge2\).  Also
\(e<87/32\).

Using \(\pi<22/7\), the first exponent obeys

\[
 {49\pi\over324}<{539\over1134}.
\]

Substitution in (3.2) gives

\[
 e^{539/1134}
 <{10451161\over6493284}
 <{1000\over621}.
\]

The final cross multiplication is

\[
 10451161\cdot621=6490170981<6493284000.
\]

Hence

\[
                         e^{-49\pi/324}>{621\over1000}.
\tag{3.3}
\]

For the second exponent,

\[
 {121\pi\over324}
 <{1331\over1134}
 =1+{197\over1134}.
\]

Equations (3.2) and \(e<87/32\) give

\[
 e^{1331/1134}
 <{87\over32}{8648137\over7268940}
 <{1000\over307}.
\]

The last comparison is

\[
 87\cdot8648137\cdot307
 =230983091133
 <232606080000
 =32\cdot7268940\cdot1000.
\]

Therefore

\[
                         e^{-121\pi/324}>{307\over1000}.
\tag{3.4}
\]

Finally,

\[
 {100\pi\over81}
 <{2200\over567}<{39\over10}.
\]

Applying (3.2) at \(9/10\),

\[
 e^{100\pi/81}
 <\left({87\over32}\right)^3{347\over140}
 <50,
\]

because

\[
 87^3\cdot347=228500541
 <229376000=50\cdot32^3\cdot140.
\]

Thus

\[
                         e^{-100\pi/81}>{1\over50}.
\tag{3.5}
\]

The three lower bounds sum to \(237/250\).  Equation (3.1) proves

\[
                         f(2/9)<{13\over250}.
\tag{3.6}
\]

This independently verifies the full two-ninth train lemma.

## 4. Period-nine ray geometry

The disjoint-ray inequality \(u+1<9-u\) gives \(u\le3\).  Hence
\(H=3\) forces \(u=3\).  The reflected identity then contains exactly one
unpaired middle term:

\[
 E(s)=C+g(\alpha)+f(M)
 +\sum_{i=1}^3
 \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr),
\tag{4.1}
\]

where \(M=s_5/A\in(0,1/2]\).  The frozen train theorem gives \(f(M)>0\).

For the terminal \(i\)-gap suffix \(R_i=P-s_{9-i}\), prefix-minimum
duality gives

\[
                         R_i\ge{iP\over9}.
\]

Since \(Y_i=(a+R_i)/(P+a)\),

\[
\begin{aligned}
 Y_2-{2\over9}
 &\ge {7a\over9(P+a)}>0,\\
 Y_3-{1\over3}
 &\ge {2a\over3(P+a)}>0.
\end{aligned}
\tag{4.2}
\]

Thus \(Y_2>2/9\) and \(Y_3>1/3>1/4\), exactly the domains required by
the new and old train estimates.

## 5. Pair ledger

Write

\[
 m_0={57\over1400},
 \qquad U_1={61\over1000},
 \qquad U_2={13\over250},
 \qquad U_3={293\over6000},
 \qquad \varepsilon_\theta={1\over20000}.
\]

The first pair is unrestricted.  Splitting at the quarter as in the
period-eight audit gives

\[
 f(X_1)-f(Y_1)+g(Y_1)>m_0-U_1-\varepsilon_\theta.
\tag{5.1}
\]

For pair two:

* if \(X_2\ge2/9\), monotone decrease gives
  \(f(X_2)\ge f(Y_2)\), leaving only a theta charge;
* if \(X_2<2/9\), then \(f(X_2)>m_0\), while
  \(f(Y_2)<f(2/9)<U_2\).

Hence uniformly

\[
 f(X_2)-f(Y_2)+g(Y_2)>m_0-U_2-\varepsilon_\theta.
\tag{5.2}
\]

For pair three, \(Y_3>1/4\).  Quarter-interval decrease if
\(X_3\ge1/4\), and the quarter bounds otherwise, give

\[
 f(X_3)-f(Y_3)+g(Y_3)>m_0-U_3.
\tag{5.3}
\]

The minimum-gap theorem gives \(P\ge9a\), so
\(\alpha=a/(P+a)\le1/10\), and

\[
                         g(\alpha)>-\varepsilon_\theta.
\tag{5.4}
\]

Thus exactly three possible theta charges are priced: \(g(Y_1)\),
\(g(Y_2)\), and \(g(\alpha)\).  The \(Y_3\) theta term is positive.

## 6. Exact margin and scope

Discarding only the positive middle term and inserting (5.1)--(5.4) into
(4.1) gives

\[
\begin{aligned}
 E(s)
 &>4m_0-U_1-U_2-U_3-3\varepsilon_\theta\\
 &={68400-25620-21840-20510-63\over420000}\\
 &={367\over420000}>0.
\end{aligned}
\]

Therefore

\[
                         \Phi(W)\ge E(s)>
                         {367\over420000}>0.
\]

This closes every period-nine \(H=3\) exact-first-carry formal clock.
For \(H\le2\), one has \(u\le3\), \(\tau\le4\), and
\(360H+\tau\le724<860\), so the prior reflected-depth theorem applies.
Consequently every honest exact-first-carry period-nine formal clock is
positive.

The result does not cover period at least ten, threshold overshoot, later
first crossing, or finite physical shoulders.

**Audit verdict:** **PASS.**
