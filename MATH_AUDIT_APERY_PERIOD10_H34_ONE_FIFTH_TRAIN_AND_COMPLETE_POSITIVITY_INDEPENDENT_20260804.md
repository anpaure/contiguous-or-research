# Independent audit: period-ten one-fifth train and complete positivity

**Date:** 2026-08-04  
**Audited theorem:**  
MATH_THEOREM_APERY_PERIOD10_H34_ONE_FIFTH_TRAIN_AND_COMPLETE_POSITIVITY_20260804.md  
**Audited SHA-256:**  
1697def0ed72f30c6972a706a968a3efed68e470ebe511b813c7eedc7259095e  
**Verdict:** **GO.**  The one-fifth monotonicity lemma, value anchor,
global compact bound, period-ten chamber classification, and both final
margins are exact.  No computation or search is used.

## 1. One-fifth derivative sign

For

\[
 h(x)=xe^{-\pi x^2/4},
\]

the exact derivative is

\[
 f'(u)={\pi\over2}
 \left(\sum_{q\ge0}h(1+u+q)-h(1-u)\right).
\tag{1.1}
\]

At \(u=1/5\), divide by \(h(4/5)\).  The first ratio is

\[
 {3\over2}e^{-\pi/5}.
\]

The positive Taylor sum

\[
 1+{3\over5}+{9\over50}+{9\over250}+{27\over5000}
 ={9107\over5000}>{9\over5}
\]

and \(\pi>3\) make this ratio less than \(5/6\).

The second ratio is

\[
 {11\over4}e^{-21\pi/20}.
\]

Since \(21\pi/20>3+3/20\), \(e^3>20\), and
\(e^{3/20}>23/20\), it is less than \(1/8\).

Starting at \(z=11/5\), every successive positive-term ratio is at most

\[
 {16\over11}e^{-27\pi/20}<{1\over30}.
\]

Indeed \(27\pi/20>4\), while

\[
 \left({19\over7}\right)^4
 ={130321\over2401}>{480\over11}.
\]

Consequently the complete positive/adverse ratio is below

\[
 {5\over6}+{1/8\over1-1/30}
 ={335\over348}<1.
\tag{1.2}
\]

For

\[
 R_q(u)={h(1+u+q)\over h(1-u)},
\]

\[
 {d\over du}\log R_q(u)
 ={1\over1+u+q}+{1\over1-u}
 -{\pi\over2}(q+2).
\]

On \(1/5\le u\le1/2\), the first two terms are at most \(8/3\) for
\(q=0\), and at most \(5/11+2\) for \(q\ge1\).  Both are strictly below
the corresponding last term.  Thus all \(R_q\) decrease, and (1.2)
proves

\[
                         f'(u)<0
 \qquad(1/5\le u\le1/2).
\tag{1.3}
\]

## 2. One-fifth endpoint

The theorem uses

\[
 U_m(x)=\sum_{j=0}^{m-1}{x^j\over j!}
       +{x^m\over m!\,(1-x/(m+1))},
\]

which is an upper bound for \(e^x\).  The four rational checks behind its
table are exactly

\[
\begin{aligned}
 U_3(88/175)&<{2000\over1209},\\
 U_5(198/175)&<{400\over129},\\
 \left({87\over32}\right)^3U_3(281/350)
   &<{5000\over111},\\
 \left({87\over32}\right)^8U_2(8/175)
   &<{10000\over3}.
\end{aligned}
\tag{2.1}
\]

Each follows by clearing positive denominators.  Together with
\(\pi<22/7\), they give

\[
\begin{aligned}
 e^{-4\pi/25}&>{1209\over2000},&
 e^{-9\pi/25}&>{129\over400},\\
 e^{-121\pi/100}&>{111\over5000},&
 e^{-64\pi/25}&>{3\over10000}.
\end{aligned}
\tag{2.2}
\]

The four right sides sum to \(9495/10000\).  Retaining these four adverse
terms in the literal train therefore gives

\[
                         f(1/5)<1-{9495\over10000}
                         ={101\over2000}.
\tag{2.3}
\]

This independently verifies the endpoint anchor.

## 3. Global compact bound

For \(0\le u\le1/5\), Jacobi completion gives

\[
 f(u)=1-\Theta(u)+H(u)+R(u),
\tag{3.1}
\]

where

\[
 H(u)=e^{-\pi u^2/4}+e^{-\pi(2-u)^2/4},
\]

\[
 R(u)=\sum_{j\ge3}e^{-\pi(j-u)^2/4},
\qquad
 |\Theta(u)-2|<{1\over20000}.
\tag{3.2}
\]

The derivative of \(H\) vanishes exactly when

\[
 G(u):=\log{2-u\over u}-\pi(1-u)=0.
\]

On \(0<u\le1/5\),

\[
 G'(u)=\pi-{2\over u(2-u)}<0,
\]

so there is at most one critical point.  The derivative of \(H\) is
positive near zero.  At \(t_0=119/1000\),

\[
 e^{\pi(1-t_0)}
 >e^{138317/50000}
 >{1881\over119},
\tag{3.3}
\]

where the last inequality follows from \(e^2>369/50\) and the
degree-four positive Taylor sum at \(38317/50000\).  Thus \(G(t_0)<0\),
and the unique maximum obeys \(t_*<t_0\).

At that maximum,

\[
 H(t_*)={2\over2-t_*}e^{-\pi t_*^2/4}.
\]

This right side increases up to \(t_0\).  Using
\(\pi>157/50\) and \(e^{-x}<1/(1+x)\) gives

\[
 H(t_*)
 <{400000000000\over380381984037}
 <{10517\over10000}.
\tag{3.4}
\]

For the tail, every term increases with \(u\).  At \(u=1/5\), its first
term satisfies

\[
 e^{-49\pi/25}<{43\over20000}.
\tag{3.5}
\]

Indeed \(49\pi/25>6+193/1250\), \(e^6>400\), and the quadratic positive
Taylor sum at \(193/1250\), multiplied by \(400\), exceeds \(20000/43\).

Every subsequent ratio is less than \(1/100\), because the exponent
increment is at least \(33\pi/20>99/20\), and

\[
 e^{99/20}>e^4(1+19/20)>100.
\]

Hence

\[
                         R(u)<{43\over19800}
                         <{11\over5000}.
\tag{3.6}
\]

Equations (3.1)--(3.6) give

\[
 f(u)
 <{10517\over10000}-1
  +{11\over5000}+{1\over20000}
 ={1079\over20000}
 <{27\over500}
\]

on \([0,1/5]\).  On \([1/5,1/2]\), monotonicity and (2.3) give the
stronger \(f(u)<101/2000\).  Therefore

\[
                         \sup_{0\le u\le1/2}f(u)
                         <{27\over500}.
\tag{3.7}
\]

## 4. Period-ten geometry

The disjoint-ray inequality gives \(u+1<10-u\), hence \(u\le4\) and
\(H\le4\).  After the already closed \(H\le2\) branch, the exhaustive new
list is

\[
                         (u,H)=(3,3),(4,3),(4,4).
\tag{4.1}
\]

Terminal-suffix maximality yields

\[
 Y_i\ge{a+iP/10\over P+a}>{i\over10}.
\]

Thus

\[
                         Y_2>{1\over5},
\qquad
                         Y_3>{3\over10},
\qquad
                         Y_4>{2\over5}.
\tag{4.2}
\]

For \(u=3\), the reflected identity contains exactly the two middle terms
\[
                         f(s_5/A)+f(s_6/A)>0.
\]
For \(u=4\), it contains no middle term.  This confirms that no positive
middle contribution was silently discarded before classification.

## 5. Pair ledgers

Let

\[
 m_0={57\over1400},\quad
 U_0={27\over500},\quad
 U_1={101\over2000},\quad
 U_q={293\over6000},\quad
 \varepsilon={1\over20000}.
\]

The first pair has the uniform lower bound

\[
                         m_0-U_0-\varepsilon.
\tag{5.1}
\]

This follows from the global bound if \(X_1<1/4\), while quarter
monotonicity and positive theta give a stronger result if \(X_1\ge1/4\).

The second pair has lower bound

\[
                         m_0-U_1-\varepsilon.
\tag{5.2}
\]

If \(X_2\ge1/5\), one-fifth monotonicity leaves only the theta charge.  If
\(X_2<1/5\), use \(f(X_2)>m_0\) and
\(f(Y_2)<f(1/5)<U_1\).

Every remaining pair has lower bound

\[
                         m_0-U_q,
\tag{5.3}
\]

because its reflected endpoint is beyond the quarter and its theta term
is positive.

Finally \(P\ge10a\) gives \(\alpha\le1/11\), so
\(g(\alpha)>-\varepsilon\).  Exactly three possible theta losses have
therefore been charged.

For \(u=3\), after retaining and then harmlessly discarding the two
positive middle terms,

\[
\begin{aligned}
 E(s)
 &>4m_0-U_0-U_1-U_q-3\varepsilon\\
 &={3937\over420000}>0.
\end{aligned}
\tag{5.4}
\]

For \(u=4\),

\[
\begin{aligned}
 E(s)
 &>5m_0-U_0-U_1-2U_q-3\varepsilon\\
 &={527\over420000}>0.
\end{aligned}
\tag{5.5}
\]

These arithmetic ledgers are exact.

## 6. Scope verdict

The proof closes every honest exact-first-carry period-ten formal clock,
including \(H=4\).  The \(H\le2\) cases satisfy
\(360H+\tau\le725<860\); equations (5.4)--(5.5) close all remaining
cases.  Threshold overshoot, later first crossing, finite shoulders, and
periods at least eleven remain outside scope.

**Audit verdict:** **PASS.**
