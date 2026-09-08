# Endpoint criticality reduces to a first-physical-row two-block inverse covariance

**Date:** 2026-08-07  
**Method:** pure mathematics; max-plus first-row retention, generalized
inverses, and Stieltjes integration  
**Status:** unconditional exact lower bound and structural reduction.  The
complete endpoint-critical Bellman functional is bounded below by a
functional involving only the displayed head and the first physical carry
row.  That lower bound is exactly a two-block inverse covariance.  The
two inverse blocks satisfy the honest half-line sumset inequalities, so
the remaining sufficient lemma is stated without any Apéry conductor or
abstract shoulder profile.  Positivity of that covariance is not proved.

## 1. Endpoint-critical clock and its first physical row

Put

\[
 A={\sqrt\pi\over2},\qquad a=A^2={\pi\over4},
\tag{1.1}
\]

and write

\[
 f(x)=e^{-ax^2}.
\tag{1.2}
\]

The normalized Rayleigh kernel is

\[
 \kappa(y):=K(Ay)=
 \begin{cases}
  1-f(1-y)-f(1+y),&0\le y\le1,\\
  -f(1+y),&y\ge1.
 \end{cases}
\tag{1.3}
\]

Let

\[
 0=v_0\le v_1\le\cdots\le v_n=1
\tag{1.4}
\]

be internally superadditive, and suppose

\[
 {v_j\over j}<{1\over n}\qquad(1\le j<n).
\tag{1.5}
\]

Let \(L\) be its max-plus Bellman closure.  Then \(L(r)=v_r\) for
\(0\le r\le n\), \(L\) is nondecreasing and superadditive, and

\[
 L(m)\le {m\over n}.
\tag{1.6}
\]

Retain the complete first physical carry row by putting

\[
 \boxed{p_r=L(n+r)-1\qquad(0\le r\le n).}
\tag{1.7}
\]

Thus

\[
 p_0=0,\qquad p_n=1,
 \qquad v_r\le p_r\le {r\over n},
\tag{1.8}
\]

and \(p_0\le p_1\le\cdots\le p_n\).

The inequality \(p_r\ge v_r\) follows by using one endpoint part and
the direct residue part.  The upper bound follows from (1.6), and
monotonicity follows from that of \(L\).

## 2. The first row controls every later Gaussian tail

Define

\[
 B(y)=f(1-y)+f(1+y),
 \qquad
 H_2(y)=\sum_{\ell\ge2}f(\ell+y)
 \quad(0\le y\le1).
\tag{2.1}
\]

### Theorem 2.1 (first-physical-row lower bound)

The complete physical Bellman functional satisfies

\[
 \boxed{
 \sum_{m\ge0}K(AL(m))
 \ge
 n-\sum_{r=0}^{n-1}\{B(v_r)+H_2(p_r)\}.}
\tag{2.2}
\]

#### Proof

For every \(q\ge1\), endpoint superadditivity gives

\[
 L(qn+r)
 \ge (q-1)L(n)+L(n+r)
 =q+p_r.
\tag{2.3}
\]

Both sides are at least one.  The outer branch of \(\kappa\) is
increasing, so

\[
 \kappa(L(qn+r))\ge\kappa(q+p_r)=-f(q+1+p_r).
\tag{2.4}
\]

The head term is exact:

\[
 \kappa(L(r))=\kappa(v_r)=1-B(v_r).
\tag{2.5}
\]

Sum (2.4) over \(q\ge1\), use (2.1), and then sum over residues.
This gives (2.2). \(\square\)

This strengthens the binary first-wrap bound.  Indeed, if

\[
 w_r=\max\left\{v_r,
   \max_{i+j=n+r}(v_i+v_j-1)\right\},
\tag{2.6}
\]

then Bellman superadditivity gives \(p_r\ge w_r\).  Since \(H_2\) is
decreasing, (2.2) is at least as strong as the lower bound obtained by
replacing \(p_r\) with \(w_r\).

## 3. Exact inverse profiles

For \(0<z<1\), define the two generalized inverses

\[
 C_0(z)=\min\{0\le r\le n:v_r\ge z\},
 \qquad
 C_1(z)=\min\{0\le r\le n:p_r\ge z\},
\tag{3.1}
\]

and their equal-work discrepancies

\[
 U_0(z)=C_0(z)-nz,
 \qquad
 U_1(z)=C_1(z)-nz.
\tag{3.2}
\]

The phase bounds in (1.8) give

\[
 \boxed{0\le U_1(z)\le U_0(z).}
\tag{3.3}
\]

Let

\[
 C(t)=\min\{m\ge0:L(m)\ge t\},
 \qquad u(t)=C(t)-nt.
\tag{3.4}
\]

Then, away from the irrelevant clock atoms,

\[
 \boxed{
 u(z)=U_0(z),\qquad
 u(1+z)=U_1(z)
 \quad(0<z<1).}
\tag{3.5}
\]

Indeed, no index below \(n\) reaches level one, and the points in the
next index block are exactly

\[
 L(n+r)=1+p_r\qquad(0\le r\le n).
\tag{3.6}
\]

## 4. Honest two-block half-line subadditivity

The inverse \(C\), and therefore \(u\), is subadditive on the
nonnegative half-line.  Equations (3.5) immediately give the following
complete two-block inequalities.

### Theorem 4.1 (two-block inverse law)

For \(x,y\in(0,1)\),

\[
 \boxed{
 U_0(x+y)\le U_0(x)+U_0(y)
 \quad\hbox{if }x+y<1,}
\tag{4.1}
\]

and

\[
 \boxed{
 U_1(x+y-1)\le U_0(x)+U_0(y)
 \quad\hbox{if }x+y>1.}
\tag{4.2}
\]

Consequently, if

\[
 A_i(t)=\{z\in(0,1):U_i(z)\le t\},
 \qquad F_i(t)=|A_i(t)|,
\tag{4.3}
\]

then the one-dimensional sumset inequality gives

\[
 \boxed{
 F_0(a)+F_0(b)
 \le F_0(a+b)+F_1(a+b)}
\tag{4.4}
\]

whenever both input sublevel sets have positive measure.

#### Proof

Equations (4.1)--(4.2) are just

\[
 u(x+y)\le u(x)+u(y)
\tag{4.5}
\]

with the output read in the appropriate unit block.  Moreover,
\(A_0(a)+A_0(b)\subset(0,2)\) lies inside the union of the two output
sublevel sets, in their respective unit blocks.  The real-line
Brunn--Minkowski inequality gives

\[
 |A_0(a)+A_0(b)|\ge F_0(a)+F_0(b),
\tag{4.6}
\]

which proves (4.4). \(\square\)

The converse implication is false: the distributional inequality (4.4)
does not by itself recover the pointwise laws (4.1)--(4.2).  Thus the
first-row lower bound retains the first nontrivial expanding-horizon
sumset constraint together with its stronger pointwise Bellman origin.
No artificial periodization of the physical head has been used.

## 5. Exact two-block covariance

For any nondecreasing phase list

\[
 0=x_0\le x_1\le\cdots\le x_n=1
\tag{5.1}
\]

and its discrepancy

\[
 U_x(z)=\#\{0\le r<n:x_r<z\}-nz,
\tag{5.2}
\]

Stieltjes integration by parts gives, for every \(C^1\) function
\(\phi\),

\[
 \int_0^1U_x(z)\phi'(z)\,dz
 =n\int_0^1\phi(z)\,dz-
   \sum_{r=0}^{n-1}\phi(x_r).
\tag{5.3}
\]

Since

\[
 B(y)+H_2(y)
 =e^{-a(1-y)^2}+\sum_{q\ge1}e^{-a(q+y)^2}
\tag{5.4}
\]

and the intervals in (5.4) tile the positive half-line,

\[
 \int_0^1\{B(y)+H_2(y)\}\,dy=1.
\tag{5.5}
\]

Apply (5.3) separately to the phase lists \(v\) and \(p\).  The lower
bound in Theorem 2.1 becomes the exact identity

\[
 \boxed{
 n-\sum_{r<n}\{B(v_r)+H_2(p_r)\}
 =\int_0^1\bigl[U_0(z)B'(z)+U_1(z)H_2'(z)\bigr],dz.}
\tag{5.6}
\]

The derivative weights are explicit:

\[
 B'(z)=2a\{(1-z)f(1-z)-(1+z)f(1+z)\},
\tag{5.7}
\]

\[
 H_2'(z)=-2a\sum_{\ell\ge2}(\ell+z)f(\ell+z)<0.
\tag{5.8}
\]

Consequently the following is a sufficient endpoint-critical closure
lemma:

> **Two-block inverse covariance target.**  Every pair of staircase
> profiles \((U_0,U_1)\) arising from (1.4)--(1.7), and hence satisfying
> (3.3) and (4.1)--(4.4), obeys
> \[
>  \int_0^1\{U_0B'+U_1H_2'\}\,dz\ge0.
> \tag{5.9}
> \]

If (5.9) holds, then (2.2) proves positivity of the complete physical
Bellman functional.  A counterexample to (5.9) would only refute this
first-row lower bound; higher physical rows could still supply additional
positive tail gain.

## 6. Exact scope

This theorem proves neither (5.9) nor the complete endpoint inequality.
It does prove that the whole-tail bonus can be retained without the full
conductor:

1. the actual first carry row controls every later outer-Gaussian row;
2. the resulting scalar is an exact two-block inverse covariance;
3. its two profiles satisfy honest half-line subadditivity and the exact
   two-block connected-sumset inequality;
4. the already-refuted separate shoulder sign is not used.

The remaining sufficient statement is therefore a signed two-block
sumset/covariance theorem, rather than an unsigned shoulder-area bound or
a residuewise derivative-prefix sign.

## 7. Dependencies

1. the half-line generalized-inverse theorem;
2. the endpoint missing-tail identity and first-wrap lower bound;
3. only elementary Stieltjes integration and the real-line
   Brunn--Minkowski inequality beyond those results.
