# Period-nine depth-three Apéry clocks: the two-ninth train and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period nine is strictly
positive.  The only new chamber is \(H=3\).  Terminal-suffix maximality
places its second reflected endpoint beyond \(2/9\) and its third beyond
\(1/3\); a new exact train estimate proves monotone decrease from \(2/9\)
and \(f(2/9)<13/250\).  No computation, search, or functional compression
is used.  The theorem does not address periods at least ten, threshold
overshoot, later first crossing, or finite physical shoulders.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_A(w)=\sum_{q\ge0}K(qA+w),
 \qquad
 f(u)=F_A(Au).
\tag{0.1}
\]

Also put

\[
                         h(x)=xe^{-\pi x^2/4}.
\tag{0.2}
\]

## 1. A new compact-train interval

### Lemma 1.1 (two-ninth train lemma)

The threshold-period train satisfies

\[
 \boxed{
 f'(u)<0\quad(2/9\le u\le1/2),
 \qquad
 f(2/9)<{13\over250}.}
\tag{1.1}
\]

#### Proof of monotonicity

For \(0<u<1\), termwise differentiation of the Gaussian train gives the
exact identity

\[
 f'(u)={\pi\over2}
 \left(\sum_{q\ge0}h(1+u+q)-h(1-u)\right).
\tag{1.2}
\]

At \(u=2/9\), divide every positive term by \(h(7/9)\).  The first ratio
is

\[
 R_0={h(11/9)\over h(7/9)}
 ={11\over7}e^{-2\pi/9}<{4\over5}.
\tag{1.3}
\]

Indeed \(\pi>157/50>621/200\), so \(2\pi/9>69/100\), and the cubic
positive Taylor sum gives

\[
 e^{2\pi/9}>e^{69/100}
 >1+{69\over100}+{4761\over20000}
    +{328509\over6000000}
 >{55\over28}.
\]

The second ratio is

\[
 R_1={h(20/9)\over h(7/9)}
 ={20\over7}e^{-13\pi/12}<{1\over10}.
\tag{1.4}
\]

Here \(13\pi/12>17/5\), while

\[
 e^{17/5}=e^3e^{2/5}
 >\left({19\over7}\right)^3{37\over25}
 >{200\over7}.
\]

The elementary bound \(e>19/7\) follows already from the positive Taylor
sum through degree five.

For every later positive term, beginning with \(z=20/9\),

\[
 {h(z+1)\over h(z)}
 ={z+1\over z}e^{-\pi(2z+1)/4}
 \le {29\over20}e^{-49\pi/36}
 <{1\over30}.
\tag{1.5}
\]

The last inequality follows from \(\pi>3\) and
\((19/7)^4>87/2\).  Therefore the complete positive/adverse ratio at
\(u=2/9\) is less than

\[
 {4\over5}+{1/10\over1-1/30}
 ={4\over5}+{3\over29}
 ={131\over145}<1.
\tag{1.6}
\]

It remains to propagate the derivative sign.  For \(q\ge0\), let

\[
 R_q(u)={h(1+u+q)\over h(1-u)}.
\]

Then

\[
 {d\over du}\log R_q(u)
 ={1\over1+u+q}+{1\over1-u}-{\pi\over2}(q+2).
\tag{1.7}
\]

For \(q=0\) and \(2/9\le u\le1/2\), the first two terms equal
\(2/(1-u^2)\le8/3<\pi\).  For \(q\ge1\), they are at most

\[
 {9\over20}+2={49\over20}
 <{9\over2}< {3\pi\over2}
 \le{\pi\over2}(q+2).
\]

Thus every \(R_q(u)\) strictly decreases on the interval.  Equation
(1.6) consequently proves \(f'(u)<0\) throughout
\([2/9,1/2]\).

#### Proof of the endpoint bound

For \(0<u<1\), the literal threshold train is

\[
 f(u)
 =1-e^{-\pi(1-u)^2/4}
   -\sum_{n\ge1}e^{-\pi(n+u)^2/4}.
\tag{1.8}
\]

At \(u=2/9\), retain the first three adverse exponentials:

\[
 f(2/9)
 <1-e^{-49\pi/324}
    -e^{-121\pi/324}
    -e^{-100\pi/81}.
\tag{1.9}
\]

We prove

\[
 e^{-49\pi/324}>{621\over1000},
 \qquad
 e^{-121\pi/324}>{307\over1000},
 \qquad
 e^{-100\pi/81}>{1\over50}.
\tag{1.10}
\]

Use the elementary upper estimate

\[
 e^x
 <1+x+{x^2\over2(1-x/3)}
 \qquad(0<x<3),
\tag{1.11}
\]

which follows from \(n!\ge2\cdot3^{n-2}\) for \(n\ge2\).  Also

\[
                         e<{87\over32},
\tag{1.12}
\]

obtained by summing through degree three and bounding the remaining
factorial tail geometrically.

Since \(\pi<22/7\),

\[
 {49\pi\over324}<{539\over1134}.
\]

Substitution in (1.11) gives

\[
 e^{539/1134}
 <{10451161\over6493284}
 <{1000\over621},
\tag{1.13}
\]

proving the first inequality in (1.10).

Similarly,

\[
 {121\pi\over324}
 <{1331\over1134}
 =1+{197\over1134}.
\]

Equations (1.11)--(1.12) give

\[
 e^{1331/1134}
 <{87\over32}\,
   {8648137\over7268940}
 <{1000\over307},
\tag{1.14}
\]

which proves the second inequality.

Finally,

\[
 {100\pi\over81}
 <{2200\over567}<{39\over10}.
\]

Using (1.11) at \(9/10\) and (1.12),

\[
 e^{100\pi/81}
 <e^{39/10}
 <\left({87\over32}\right)^3{347\over140}
 <50.
\tag{1.15}
\]

This proves the third inequality in (1.10).  Their sum is

\[
 {621\over1000}+{307\over1000}+{1\over50}
 ={237\over250}.
\]

Equation (1.9) now gives \(f(2/9)<13/250\), completing the proof.
\(\square\)

## 2. Period-nine ray geometry

Let

\[
 0=s_0<s_1<\cdots<s_8<P,
 \qquad
 P+s_1=A,
\tag{2.1}
\]

be an honest cyclic Apéry table of period nine.  Put

\[
 a=s_1,\qquad \alpha={a\over A}.
\]

The disjoint-ray inequality

\[
                         u+1<9-u
\]

gives \(u\le3\).  Hence every \(H=3\) table has \(u=3\).

Define

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{9-i}\over A},
 \qquad 1\le i\le3,
\tag{2.2}
\]

and the one middle point

\[
                         M={s_5\over A}.
\tag{2.3}
\]

Then

\[
 0<X_i\le Y_i<1/2,
 \qquad
 0<M\le1/2.
\tag{2.4}
\]

The exact reflected-ray identity is

\[
\boxed{
 E(s)=C+g(\alpha)+f(M)
 +\sum_{i=1}^3
  \bigl(f(X_i)-f(Y_i)+g(Y_i)\bigr),
}
\tag{2.5}
\]

and \(\Phi(W)\ge E(s)\).

Let \(R_i=P-s_{9-i}\) be the terminal \(i\)-gap suffix.  Prefix-minimum
duality makes \(R_i\) a maximum cyclic \(i\)-block, so

\[
                         R_i\ge{iP\over9}.
\tag{2.6}
\]

Since \(Y_i=(a+R_i)/A\) and \(A=P+a\),

\[
 Y_i\ge{\displaystyle a+{iP\over9}\over A}.
\tag{2.7}
\]

In particular,

\[
\boxed{
 Y_2>{2\over9},
 \qquad
 Y_3>{1\over3}>{1\over4}.}
\tag{2.8}
\]

The strict differences are respectively

\[
 a+{2P\over9}-{2(P+a)\over9}={7a\over9}>0,
\]

and

\[
 a+{P\over3}-{P+a\over3}={2a\over3}>0.
\]

## 3. The three pair bounds

We use the frozen estimates

\[
 C>{57\over1400},
 \qquad
 f(x)>{57\over1400}\quad(0\le x\le1/4),
\tag{3.1}
\]

\[
 f(x)<{61\over1000}\quad(0\le x\le1/2),
\tag{3.2}
\]

\[
 f(1/4)<{293\over6000},
 \qquad
 f\text{ decreases on }[1/4,1/2],
\tag{3.3}
\]

and

\[
 |g(x)|<{1\over20000},
 \qquad
 g(x)>0\quad(1/4\le x\le1/2).
\tag{3.4}
\]

The unrestricted first-pair estimate is

\[
 f(X_1)-f(Y_1)+g(Y_1)
 >{57\over1400}-{61\over1000}-{1\over20000}.
\tag{3.5}
\]

For the second pair, equation (2.8) and Lemma 1.1 give

\[
\boxed{
 f(X_2)-f(Y_2)+g(Y_2)
 >{57\over1400}-{13\over250}-{1\over20000}.}
\tag{3.6}
\]

Indeed, if \(X_2\ge2/9\), monotone decrease gives
\(f(X_2)\ge f(Y_2)\), and (3.6) is weaker than the theta bound alone.
If \(X_2<2/9\), then (3.1) gives the lower bound on \(f(X_2)\), while
Lemma 1.1 and \(Y_2>2/9\) give \(f(Y_2)<13/250\).

For the third pair, \(Y_3>1/3>1/4\).  If \(X_3\ge1/4\), quarter-interval
decrease makes the compact difference nonnegative and \(g(Y_3)>0\).
If \(X_3<1/4\), equations (3.1), (3.3), and (3.4) give

\[
\boxed{
 f(X_3)-f(Y_3)+g(Y_3)
 >{57\over1400}-{293\over6000}.}
\tag{3.7}
\]

Thus (3.7) is a valid uniform third-pair bound.

## 4. Complete period-nine closure

### Theorem 4.1

Every honest exact-first-carry period-nine cyclic Apéry clock with
\(H=3\) satisfies

\[
 \boxed{
 \Phi(W)\ge E(s)>{367\over420000}>0.}
\tag{4.1}
\]

#### Proof

The minimum-gap theorem gives \(P\ge9a\), hence

\[
                         0<\alpha={a\over P+a}\le{1\over10}<1/2
\]

and therefore \(g(\alpha)>-1/20000\).  Also \(f(M)>0\), so it may be
discarded from a strict lower bound.

Insert (3.1) and the three pair estimates (3.5)--(3.7) into (2.5):

\[
\begin{aligned}
 E(s)
 &>{4\cdot57\over1400}
   -{61\over1000}
   -{13\over250}
   -{293\over6000}
   -{3\over20000}\\
 &={367\over420000}>0.
\end{aligned}
\tag{4.2}
\]

The endpoint comparison \(\Phi(W)\ge E(s)\) proves (4.1). \(\square\)

### Corollary 4.2

Every honest exact-first-carry period-nine cyclic Apéry clock has

\[
                         \boxed{\Phi(W)>0.}
\tag{4.3}
\]

#### Proof

The disjoint-ray inequality gives \(u\le3\), hence \(H\le3\).  Theorem
4.1 closes \(H=3\).  If \(H\le2\), then
\(\tau\le u+1\le4\), so

\[
                         360H+\tau\le724<860.
\]

The general reflected-ray depth theorem therefore gives strict
positivity. \(\square\)

## 5. Scope and dependencies

The theorem closes the complete exact-first-carry period-nine formal
branch.  It does not prove positivity under threshold overshoot or a later
first crossing, does not control finite physical shoulders, and does not
imply a universal Bellman or OR-word theorem.

| role | file | SHA-256 |
|---|---|---|
| prefix-minimum and reflected-ray identity | MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md | 28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e |
| compact train and quarter bounds | MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
| theta monotonicity and positivity | MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |
| complete period-eight direct closure | MATH_THEOREM_APERY_PERIOD8_ALL_H3_DIRECT_QUARTER_CLOSURE_20260804.md | 93f40df626f7356ccb5dd890818fd9214f3db3f65cce9f649ca1db4270603815 |
