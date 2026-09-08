# Legal common-core coefficients have uniformly flat coordinate marginals

Date: 2026-07-27

Method: pure mathematics only.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 N=\binom{2m}{M}=\binom{2m}{m-H},\qquad
 W=\binom{2m}{m},
\]

and retain one common-core cyclic path of length

\[
 d=m-3H+1
\]

on every rank-\(M\) top.  Equivalently, each path is obtained from the
\(M\) middle windows of one cyclic frame by deleting one consecutive block
of

\[
 \kappa=M-d=4H-1
\]

phases.  Let \(L_D\) be the resulting load of the middle target
\(D\in\binom{[2m]}m\), and put

\[
 b_i(L)=\sum_{D\ni i}L_D.
\]

Then every legal one-path-per-top coefficient satisfies, for every
coordinate \(i\),

\[
 \boxed{
 (m-\kappa)\binom{2m-1}{M-1}
 \le b_i(L)\le
 m\binom{2m-1}{M-1}.}
\tag{0.1}
\]

In the calibrated regime

\[
 H=o(m),\qquad dN=(1-o(1))W,
\tag{0.2}
\]

this gives the uniform estimate

\[
 \boxed{b_i(L)=\left(\frac12+o(1)\right)W
        \quad\hbox{for all }i.}
\tag{0.3}
\]

Consequently the high-collision marginal shield \(L^\sharp\) from
`MATH_THEOREM_PSI_MOVING_HOLE_MARGINAL_SHIELD_20260727.md` is not a legal
coefficient of the common-core product polynomial.  Indeed its first two
coordinate marginals are at least \((3/4-o(1))W\).

This removes that particular statewise obstruction.  It does not prove
that the marginal-preserving six-frame exchanges connect every legal
near-flat fibre, nor that every near-flat fibre contains a low-collision
coefficient.

## 1. One frame

Fix an \(M\)-top \(U\) and a cyclic order \(\pi\) of \(U\).  The complete
middle deck consists of the \(M\) cyclic intervals of length \(m\).
Every label \(i\in U\) belongs to exactly \(m\) of these intervals: its
admissible starting positions are the \(m\) positions from \(i-m+1\)
through \(i\), cyclically.

Delete any block of \(\kappa\) phases.  At most \(\kappa\) of the deleted
middle windows contain \(i\).  Therefore the retained path contains \(i\)
between \(m-\kappa\) and \(m\) times:

\[
 m-\kappa\le
 \#\{D\hbox{ in the retained path}:i\in D\}
 \le m.
\tag{1.1}
\]

If \(i\notin U\), the contribution is zero.

## 2. Sum over all tops

The number of rank-\(M\) tops containing a fixed coordinate \(i\) is

\[
 \binom{2m-1}{M-1}=\frac{M}{2m}N.
\tag{2.1}
\]

Summing (1.1) over exactly these tops proves (0.1).  The upper endpoint is

\[
 m\frac{M}{2m}N=\frac{MN}{2},
\tag{2.2}
\]

and the width of the interval in (0.1) is

\[
 \kappa\frac{M}{2m}N.
\tag{2.3}
\]

Since \(M=d+\kappa\), assumption (0.2) and \(\kappa=O(H)=o(m)\) imply

\[
 MN=dN+\kappa N=(1+o(1))W
\tag{2.4}
\]

and

\[
 \kappa\frac{M}{2m}N=O(HW/m)=o(W).
\tag{2.5}
\]

Equations (2.2)--(2.5) prove (0.3).

## 3. Exclusion of the shielded vector

The shielded vector is

\[
 L_D^\sharp={\bf1}_{\{1\in D\}}+{\bf1}_{\{2\in D\}}
              -{\bf1}_{\{D\in\mathcal H\}},
\]

where \(|\mathcal H|=o(W)\).  Hence

\[
\begin{aligned}
 b_1(L^\sharp)
 &=\binom{2m-1}{m-1}+\binom{2m-2}{m-2}
   -|\{D\in\mathcal H:1\in D\}|\\
 &\ge \frac W2+\frac{m-1}{2(2m-1)}W-o(W)
  =\left(\frac34-o(1)\right)W.
\end{aligned}
\tag{3.1}
\]

The same holds for coordinate \(2\).  This contradicts (0.3), proving
that \(L^\sharp\) is not legal.

## 4. Boundary

Proved: every literal common-core coefficient has all coordinate marginals
in one \(o(W)\)-width box about \(W/2\), and the known positive-density
fixed-marginal shield lies outside that box.

Unproved: collision rounding inside the legal near-flat marginal box.
