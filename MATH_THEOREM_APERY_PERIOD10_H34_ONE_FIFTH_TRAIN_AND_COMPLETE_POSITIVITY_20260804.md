# Period-ten Apéry clocks: one-fifth train bounds and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period ten has strictly
positive formal Bellman functional.  This includes the first possible
overlap-depth-four chamber.  No computation, search, or functional
compression is used.  The theorem does not address periods at least eleven,
threshold overshoot, later first crossing, or finite physical shoulders.

Put

\[
 A={\sqrt\pi\over2},\qquad
 F_A(w)=\sum_{q\ge0}K(qA+w),\qquad
 f(u)=F_A(Au),
\tag{0.1}
\]

and

\[
                         h(x)=xe^{-\pi x^2/4}.
\tag{0.2}
\]

## 1. The one-fifth monotonicity interval

### Lemma 1.1

\[
                         \boxed{
 f'(u)<0\qquad(1/5\le u\le1/2).}
\tag{1.1}
\]

#### Proof

Termwise differentiation gives

\[
 f'(u)={\pi\over2}
 \left(\sum_{q\ge0}h(1+u+q)-h(1-u)\right).
\tag{1.2}
\]

At \(u=1/5\), divide by \(h(4/5)\).  The first ratio is

\[
 {h(6/5)\over h(4/5)}
 ={3\over2}e^{-\pi/5}<{5\over6}.
\tag{1.3}
\]

Indeed \(\pi>3\), and

\[
 e^{3/5}>
 1+{3\over5}+{9\over50}+{9\over250}+{27\over5000}
 >{9\over5}.
\]

The second ratio is

\[
 {h(11/5)\over h(4/5)}
 ={11\over4}e^{-21\pi/20}<{1\over8}.
\tag{1.4}
\]

Here \(21\pi/20>63/20=3+3/20\), while
\(e^3>20\) and \(e^{3/20}>1+3/20\), so
\(e^{21\pi/20}>23>22\).

For every later positive term, beginning with \(z=11/5\),

\[
 {h(z+1)\over h(z)}
 \le {16\over11}e^{-27\pi/20}
 <{1\over30}.
\tag{1.5}
\]

The final inequality follows from \(27\pi/20>4\) and
\((19/7)^4>480/11\).  Hence the complete positive/adverse ratio is less
than

\[
 {5\over6}+{1/8\over1-1/30}
 ={5\over6}+{15\over116}
 ={335\over348}<1.
\tag{1.6}
\]

For

\[
 R_q(u)={h(1+u+q)\over h(1-u)},
\]

one has

\[
 {d\over du}\log R_q(u)
 ={1\over1+u+q}+{1\over1-u}
 -{\pi\over2}(q+2).
\tag{1.7}
\]

For \(q=0\), the first two terms are at most \(8/3<\pi\).  For
\(q\ge1\), they are at most \(5/11+2<9/2<3\pi/2\).
Thus every \(R_q\) decreases on \([1/5,1/2]\), and (1.6) propagates the
strict derivative sign throughout the interval. \(\square\)

## 2. The one-fifth value and a global compact bound

For later use, define the factorial-tail majorant

\[
 U_m(x)=\sum_{j=0}^{m-1}{x^j\over j!}
       +{x^m\over m!\,(1-x/(m+1))}
 \qquad(0<x<m+1).
\tag{2.1}
\]

Since the ratio of consecutive exponential terms from degree \(m\)
onward is at most \(x/(m+1)\),

\[
                         e^x<U_m(x).
\tag{2.2}
\]

### Lemma 2.1 (one-fifth value)

\[
                         \boxed{f(1/5)<{101\over2000}.}
\tag{2.3}
\]

#### Proof

The literal train gives

\[
\begin{aligned}
 f(1/5)
 <{}&1-e^{-4\pi/25}
       -e^{-9\pi/25}
       -e^{-121\pi/100}
       -e^{-64\pi/25}.
\end{aligned}
\tag{2.4}
\]

Using \(\pi<22/7\), equation (2.2), and \(e<87/32\), direct rational
substitution gives

\[
\begin{array}{c|c|c}
\text{term}&\text{exponent upper bound}&\text{lower bound}\\ \hline
e^{-4\pi/25}&88/175&1209/2000\\
e^{-9\pi/25}&198/175&129/400\\
e^{-121\pi/100}&1331/350&111/5000\\
e^{-64\pi/25}&1408/175&3/10000
\end{array}
\tag{2.5}
\]

For the first row use \(U_3(88/175)\), for the second use
\(U_5(198/175)\), for the third split off \(e^3\) and use
\((87/32)^3U_3(281/350)\), and for the fourth split off \(e^8\) and use
\((87/32)^8U_2(8/175)\).  Each resulting rational upper bound is smaller
than the reciprocal displayed in the last column.

The four lower bounds sum to

\[
 {1209\over2000}+{129\over400}
 +{111\over5000}+{3\over10000}
 ={9495\over10000}.
\]

Equation (2.4) proves (2.3). \(\square\)

We next sharpen the global bound \(f<61/1000\).

### Lemma 2.2 (global compact bound)

\[
                         \boxed{
 f(u)<{27\over500}\qquad(0\le u\le1/2).}
\tag{2.6}
\]

#### Proof

For \(0\le u\le1/5\), use the Jacobi completion

\[
 f(u)=1-\Theta(u)+e^{-\pi u^2/4}
      +\sum_{j\ge2}e^{-\pi(j-u)^2/4},
\tag{2.7}
\]

where

\[
                         |\Theta(u)-2|<{1\over20000}.
\tag{2.8}
\]

Put

\[
 H(u)=e^{-\pi u^2/4}+e^{-\pi(2-u)^2/4}.
\tag{2.9}
\]

The standard derivative calculation shows that \(H\) has one interior
maximum \(t_*\), characterized by

\[
 \log{2-t_*\over t_*}=\pi(1-t_*).
\tag{2.10}
\]

In fact

\[
                         t_*<{119\over1000}.
\tag{2.11}
\]

To prove this, put \(t_0=119/1000\).  Since

\[
 \pi(1-t_0)>{138317\over50000},
\]

the degree-four positive Taylor polynomial, together with
\(e^2>369/50\), gives

\[
 e^{\pi(1-t_0)}>{1881\over119}={2-t_0\over t_0}.
\]

Thus the left side of (2.10) is already smaller than the right side at
\(t_0\).

At the maximum,

\[
 H(t_*)={2\over2-t_*}e^{-\pi t_*^2/4}.
\tag{2.12}
\]

The right side is increasing for \(0\le t\le119/1000\).  Hence, using
\(\pi>157/50\) and \(e^{-x}<1/(1+x)\),

\[
\begin{aligned}
 H(t_*)
 &<{2000\over1881}
   e^{-14161\pi/4000000}\\
 &<{400000000000\over380381984037}
 <{10517\over10000}.
\end{aligned}
\tag{2.13}
\]

For the residual tail

\[
 R(u)=\sum_{j\ge3}e^{-\pi(j-u)^2/4},
\]

every term increases with \(u\) on \([0,1/5]\).  Its first term at
\(u=1/5\) satisfies

\[
 e^{-49\pi/25}<{43\over20000}.
\tag{2.14}
\]

Indeed \(49\pi/25>7693/1250=6+193/1250\),
\(e^6>400\), and

\[
 e^{193/1250}>1+{193\over1250}
                  +{37249\over3125000},
\]

whose product with \(400\) exceeds \(20000/43\).

Every successive tail ratio is less than \(1/100\), because its exponent
increment is at least \(33\pi/20>99/20\), while

\[
 e^{99/20}>e^4(1+19/20)>100.
\]

Therefore

\[
                         R(u)<{43/20000\over1-1/100}
                         ={43\over19800}
                         <{11\over5000}.
\tag{2.15}
\]

Equations (2.7)--(2.8), (2.13), and (2.15) give

\[
 f(u)
 <{10517\over10000}-1
   +{11\over5000}+{1\over20000}
 ={1079\over20000}
 <{27\over500}
\tag{2.16}
\]

for \(0\le u\le1/5\).  For \(1/5\le u\le1/2\), Lemmas 1.1 and 2.1 give

\[
 f(u)\le f(1/5)<{101\over2000}<{27\over500}.
\]

This proves (2.6). \(\square\)

## 3. Period-ten ray classification

Let

\[
 0=s_0<s_1<\cdots<s_9<P,
 \qquad
 P+s_1=A,
\tag{3.1}
\]

be an honest period-ten cyclic Apéry table.  Put

\[
 a=s_1,\qquad \alpha={a\over A}.
\]

The disjoint-ray inequality gives

\[
                         u+1<10-u,
\]

so

\[
                         \boxed{u\le4,\qquad H\le4.}
\tag{3.2}
\]

The already proved depth theorem closes \(H\le2\).  The only new
possibilities are

\[
\boxed{
(u,H)=(3,3),\ (4,3),\ (4,4).}
\tag{3.3}
\]

For \(1\le i\le u\), put

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{10-i}\over A}.
\tag{3.4}
\]

Then \(0<X_i\le Y_i<1/2\).  Terminal-suffix maximality gives

\[
 Y_i\ge{\displaystyle a+{iP\over10}\over A}
 >{i\over10}.
\tag{3.5}
\]

In particular,

\[
 \boxed{
 Y_2>{1\over5},\qquad
 Y_3>{3\over10}>{1\over4},\qquad
 Y_4>{2\over5}>{1\over4}.}
\tag{3.6}
\]

The exact endpoint comparison is

\[
\boxed{
\begin{aligned}
 E(s)
 ={}&C+g(\alpha)
 +\sum_{i=1}^u
   \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr)\\
 &+\sum_{r=u+2}^{9-u}f(s_r/A),
\end{aligned}}
\tag{3.7}
\]

with \(\Phi(W)\ge E(s)\).  For \(u=3\), the last sum is exactly

\[
                         f(s_5/A)+f(s_6/A)>0.
\tag{3.8}
\]

For \(u=4\), it is empty.

## 4. Pair estimates

Retain the frozen bounds

\[
 C>{57\over1400},\qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),
\tag{4.1}
\]

\[
 f(1/4)<{293\over6000},\qquad
 f\text{ decreases on }[1/4,1/2],
\tag{4.2}
\]

\[
 |g(x)|<{1\over20000},\qquad
 g(x)>0\quad(1/4\le x\le1/2).
\tag{4.3}
\]

The first pair is bounded globally by Lemma 2.2:

\[
\boxed{
 f(X_1)-f(Y_1)+g(Y_1)
 >{57\over1400}-{27\over500}-{1\over20000}.}
\tag{4.4}
\]

Indeed, if \(X_1<1/4\), use (4.1), Lemma 2.2, and the theta bound.  If
\(X_1\ge1/4\), monotone decrease makes the compact difference
nonnegative and \(g(Y_1)>0\), which is stronger.

For pair two, \(Y_2>1/5\).  Lemmas 1.1 and 2.1 give

\[
\boxed{
 f(X_2)-f(Y_2)+g(Y_2)
 >{57\over1400}-{101\over2000}-{1\over20000}.}
\tag{4.5}
\]

If \(X_2\ge1/5\), monotone decrease leaves only the theta charge.  If
\(X_2<1/5\), use \(f(X_2)>57/1400\) and
\(f(Y_2)<f(1/5)<101/2000\).

For every remaining pair \(i=3,4\), equation (3.6) and the quarter
bounds give

\[
\boxed{
 f(X_i)-f(Y_i)+g(Y_i)
 >{57\over1400}-{293\over6000}.}
\tag{4.6}
\]

## 5. Complete period-ten closure

The minimum-gap theorem gives \(P\ge10a\), hence

\[
                         0<\alpha={a\over P+a}\le{1\over11}<1/2,
\]

so \(g(\alpha)>-1/20000\).

### Theorem 5.1 (\(u=3,H=3\))

Every table in the \((u,H)=(3,3)\) chamber satisfies

\[
                         \boxed{
 \Phi(W)\ge E(s)>{3937\over420000}>0.}
\tag{5.1}
\]

#### Proof

Retain the two positive middle terms in (3.8), then discard them only in
the final lower bound.  Equations (3.7) and (4.4)--(4.6) give

\[
\begin{aligned}
 E(s)
 &>{4\cdot57\over1400}
   -{27\over500}
   -{101\over2000}
   -{293\over6000}
   -{3\over20000}\\
 &={3937\over420000}>0.
\end{aligned}
\]

This proves (5.1). \(\square\)

### Theorem 5.2 (\(u=4,H=3\) or \(4\))

Every table with \(u=4\) and \(H\in\{3,4\}\) satisfies

\[
                         \boxed{
 \Phi(W)\ge E(s)>{527\over420000}>0.}
\tag{5.2}
\]

#### Proof

There are four ray pairs and no middle term.  Equations
(3.7) and (4.4)--(4.6) give

\[
\begin{aligned}
 E(s)
 &>{5\cdot57\over1400}
   -{27\over500}
   -{101\over2000}
   -2{293\over6000}
   -{3\over20000}\\
 &={527\over420000}>0.
\end{aligned}
\]

This proves (5.2). \(\square\)

### Corollary 5.3

Every honest exact-first-carry period-ten cyclic Apéry clock has

\[
                         \boxed{\Phi(W)>0.}
\tag{5.3}
\]

#### Proof

Theorems 5.1--5.2 close all cases in (3.3).  If \(H\le2\), then
\(u\le4\), \(\tau\le u+1\le5\), and

\[
                         360H+\tau\le725<860.
\]

The general reflected-ray depth theorem closes those cases. \(\square\)

## 6. Scope and frozen dependencies

This theorem closes the complete exact-first-carry formal period-ten
branch, including the first possible \(H=4\) clock.  It does not address
overshoot, later crossing, physical shoulders, or the corresponding
all-period problem.

| role | file | SHA-256 |
|---|---|---|
| prefix-minimum, ray identity, and depth theorem | MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md | 28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e |
| compact quarter bounds | MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
| theta completion and positivity | MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |
| complete period-nine closure | MATH_THEOREM_APERY_PERIOD9_H3_TWO_NINTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md | 65dddbe77a805cfa5b0308f3e555801234437a383ca18ce9bbb92d5ec5b716d7 |
