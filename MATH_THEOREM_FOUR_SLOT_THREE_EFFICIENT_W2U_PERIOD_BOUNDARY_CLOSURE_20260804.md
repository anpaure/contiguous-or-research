# Four-slot three-efficient clocks: complete closure of the `w=2u` face

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It preserves the
adverse far-tail pulse and proves the complete `w=2u` face positive.  In
combination with the other audited `n=4` branches, it leaves only the
second `w=y` boundary `P+u=2y`.  It does not prove that last boundary, the
all-grid Bellman inequality, or an OR-word construction.

Put

\[
 A={\sqrt\pi\over2}.
\]

Consider an internally superadditive four-slot table

\[
 (0,x,y,z,T)
\]

in the three-slot-efficient regime.  Put

\[
 u=T-z,
 \qquad v=\max\{y,u+x\},
\]

and assume the face

\[
 w=\max\{y,2u\}=2u.
\tag{0.1}
\]

The exact normal form is

\[
\begin{aligned}
 \Phi(z;x,y,u)={}&\mathcal L_3(z;u,2u)\\
 &+K(x)-K(u)+K(y)-K(2u)\\
 &+K(z+v)-K(z+2u).
\end{aligned}
\tag{0.2}
\]

The last line is retained throughout; it is generally negative.

## 1. The subcritical parameter domain

Assume first that the endpoint is the first displayed threshold crossing:

\[
 x,y,z<A\le T=z+u.
\tag{1.1}
\]

The inherited constraints give

\[
 0\le x\le u,qquad y\le2u,qquad
 u+y\le z,qquad u\le z/3,qquad u\le v\le2u.
\tag{1.2}
\]

In particular,

\[
 0<u<A/3,qquad z\ge3A/4.
\tag{1.3}
\]

For fixed `x,y,u`, every period between

\[
 z_0:=\max\{3u,A-u\}
\tag{1.4}
\]

and the original `z` remains in the same three-efficient `w=2u` face.
Indeed `z>=3u` dominates `u+y` and `x+y`, while
`z+u>=A`, `z+u>=2y`, and

\[
 {z\over3}\ge {y\over2},
 \qquad {z\over3}\ge {z+u\over4}
\]

follow from `y<=2u` and `z>=3u`.

## 2. Strict period monotonicity with the adverse pulse

### Theorem 2.1

For fixed feasible `x,y,u`, the exact functional (0.2) is strictly
increasing in `z` on

\[
 z_0\le z<A.
\tag{2.1}
\]

#### Proof

The audited three-coset period theorem applies to

\[
 \Psi(z)=\mathcal L_3(z;u,2u).
\]

The elementary minimum

\[
 \max\{3u,A-u\}\ge3A/4
\]

is attained at `u=A/4`, so the whole interval lies in the period theorem's
normalized range.

Its hypotheses are exactly

\[
 {3A\over4}\le z\le A,qquad
 u\le z/3,qquad2u\le2z/3,qquad z+u\ge A,
\]

and it gives

\[
 \Psi'(z)>0.
\tag{2.2}
\]

It remains to price the far-tail pulse rather than discard it.  Since
`v>=u`, both `z+v` and `z+2u` lie in `[A,infinity)`.  On that interval

\[
 K'(t)=2(A+t)e^{-(A+t)^2}.
\]

This derivative is strictly decreasing there, because

\[
 {d\over dt}\bigl((A+t)e^{-(A+t)^2}\bigr)
 =\bigl(1-2(A+t)^2\bigr)e^{-(A+t)^2}<0.
\]

As `v<=2u`,

\[
 {d\over dz}\bigl(K(z+v)-K(z+2u)\bigr)
 =K'(z+v)-K'(z+2u)\ge0.
\tag{2.3}
\]

The two compact transient differences in (0.2) are independent of `z`.
Combining (2.2)--(2.3) proves strict increase of the full functional.
\(\square\)

Thus

\[
 \Phi(z;x,y,u)\ge\Phi(z_0;x,y,u).
\tag{2.4}
\]

The lower boundary has exactly two pieces:

\[
 z_0=
 \begin{cases}
 A-u,&0<u\le A/4,\\
 3u,&A/4\le u<A/3.
 \end{cases}
\tag{2.5}
\]

## 3. The endpoint-`A` boundary

### Lemma 3.1

If `0<u<=A/4` and `z=A-u`, then

\[
 \boxed{\Phi(z;x,y,u)>{1659\over220000}.}
\tag{3.1}
\]

#### Proof

Here the table endpoint is `T=z+u=A`.  The endpoint-period Bellman lower
bound gives

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(A-u).
\tag{3.2}
\]

The parameter bounds are

\[
 x\le u\le A/4,qquad y\le2u\le A/2.
\]

The audited train inequalities therefore give

\[
 C(A)>{1\over25},qquad
 F_A(x)>{1\over25},qquad
 F_A(y)>0.
\]

Reflection and the small-shift upper bound give

\[
 F_A(A-u)>-F_A(u)-{1\over20000}
 >-{1593\over22000}-{1\over20000}.
\]

Consequently

\[
 \Phi>{1\over25}+{1\over25}
       -{1593\over22000}-{1\over20000}
 ={1659\over220000}>0.
\]

Every finite Bellman value, including the adverse pulse in (0.2), is
already present in the endpoint-period lower bound. \(\square\)

## 4. The density-tie boundary

### Lemma 4.1

If `A/4<=u<A/3` and `z=3u`, then

\[
 \boxed{\Phi(z;x,y,u)>{1117\over94500}.}
\tag{4.1}
\]

#### Proof

Now

\[
 T=z+u=4u,qquad {z\over3}={T\over4}=u,
\]

while `y/2<=u`.  Hence the table is on the four-slot-efficient Apéry
boundary with scalar `alpha=u`.  The exact Apéry reduction, including its
delayed finite correction, gives

\[
 \Phi\ge J(u)
 =C(u)+K(4u)-K(5u).
\]

Since `A/4<=u<A/3`, the audited scalar-gate theorem yields

\[
 J(u)>{1117\over94500}.
\]

No tail pulse is omitted in this comparison. \(\square\)

## 5. Complete subcritical and global closure

### Theorem 5.1 (subcritical `w=2u` closure)

Every table satisfying (0.1) and (1.1) has

\[
 \boxed{\Phi>{1659\over220000}>0.}
\tag{5.1}
\]

#### Proof

Apply Theorem 2.1 and the appropriate boundary lemma from (2.5).  Finally,

\[
 {1117\over94500}>{1659\over220000},
\]

so (5.1) is the uniform lower margin. \(\square\)

### Corollary 5.2 (complete `w=2u` face)

Every internally superadditive four-slot table in the three-efficient
`w=2u` face has strictly positive Bellman functional.

#### Proof

Apply the all-grid first-crossing deletion theorem.  If the first displayed
threshold crossing has capacity at most three, the resulting prefix has
strictly positive functional by the complete `n<=3` theorem; deletion only
lowered the functional, so the original table is positive.  Otherwise the
first crossing is the endpoint at capacity four, and Theorem 5.1 applies.
\(\square\)

### Corollary 5.3 (remaining `n=4` Bellman face)

After the proved two-efficient branch, the proved four-efficient branch,
the present complete `w=2u` closure, and the proved threshold surface on
`w=y`, the only unresolved three-efficient `n=4` face is

\[
 \boxed{w=y,\qquad P+u=2y,}
\tag{5.2}
\]

with the boundary overlap `y=2u` already covered by Corollary 5.2.  Thus one
may take `y>2u` on any genuinely unresolved table.

#### Proof

First-crossing deletion removes every earlier-crossing case, so the
large-residue `z>=A` face is not an obstruction.  On the remaining
subcritical `w=y` face, strict period monotonicity reduces to
`P+u=A` or `P+u=2y`; the first surface is the audited threshold-surface
theorem.  The equality case `y=2u` also belongs to `w=2u`. \(\square\)

## 6. Exact scope

The complete `w=2u` five-pulse system is closed without deleting its
adverse far-tail pulse.  The universal four-slot Bellman theorem is now
equivalent to the single remaining surface (5.2).  This note does not sign
that surface, prove the all-grid Bellman inequality, or imply
`nu(k)<=B(k)+O(1)`.
