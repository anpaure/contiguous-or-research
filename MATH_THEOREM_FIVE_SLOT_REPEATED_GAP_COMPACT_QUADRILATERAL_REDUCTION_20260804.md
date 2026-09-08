# Five-slot repeated-gap trains: exact compact quadrilateral reduction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It uses the valid
composite-endpoint descent and reflection identities to remove every
subthreshold period from the two remaining five-slot gates.  The result is
two compact finite inequalities for the single threshold-period train
`F_A`.  Their signs are not proved here.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F(v)=F_A(v)=\sum_{q\ge0}K(qA+v),
 \qquad
 C=F(0),
\tag{0.1}
\]

and

\[
 \varepsilon=4\sum_{m\ge1}e^{-4\pi m^2}<{1\over20000}.
\tag{0.2}
\]

The exact reflected-train estimate is

\[
 F(A-w)>-F(w)-\varepsilon
 \qquad(0\le w\le A).
\tag{0.3}
\]

The two remaining scalar trains are

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta)
\tag{0.4}
\]

on

\[
 0\le a\le\beta,
 \qquad 2a+2\beta<A<2a+3\beta,
\tag{0.5}
\]

and

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a)
\tag{0.6}
\]

on

\[
 0<a<{A\over4},
 \qquad \max\{3a,A-2a\}<p<A-a.
\tag{0.7}
\]

## 1. Short-singleton quadrilateral

For the `mathcal R` gate put

\[
 y=a+\beta,
 \qquad
 v=A-2y,
 \qquad
 u=A-(2y-a)=v+a.
\tag{1.1}
\]

The parameter domain is equivalently

\[
 0<v<{A\over3},
 \qquad
 0\le a\le {A-v\over4},
 \qquad
 2a+3v<A.
\tag{1.2}
\]

Define

\[
\boxed{
 Q_R(a,v)
 =C+F(a)+F\!\left({A-v\over2}\right)
   -F(v)-F(v+a)-2\varepsilon .}
\tag{1.3}
\]

### Theorem 1.1

On (0.5), with coordinates (1.1),

\[
                         \boxed{\mathcal R(a,\beta)>Q_R(a,v).}
\tag{1.4}
\]

Consequently, positivity of `Q_R` on (1.2) proves the complete
short-singleton gate.

### Proof

The exact clock begins

\[
 0,a,y,2y-a,2y,3y-a.
\]

Condition (0.5) says exactly that its first five values are below `A` and
the sixth value is above `A`.  Composite-endpoint descent therefore gives

\[
 \mathcal R(a,\beta)
 \ge C+F(a)+F(y)+F(2y-a)+F(2y).
\tag{1.5}
\]

Now `2y-a=A-u` and `2y=A-v`.  Apply (0.3) twice and use
`y=(A-v)/2`, `u=v+a`; this gives (1.4).

It remains only to check the domain.  The inequality `2y<A` is `v>0`,
while `A<3y-a` is `2a+3v<A`.  Finally `a<=beta=y-a` is
`a<=(A-v)/4`.  These implications reverse, so (1.2) is exact. \(\square\)

## 2. Long-singleton quadrilateral

For the `mathcal P` gate put

\[
 t=A-p-a.
\tag{2.1}
\]

The unresolved interior has the exact domain

\[
 0<t<a<{A\over4},
 \qquad
 4a+t<A.
\tag{2.2}
\]

For the compact sufficient gate below we adjoin the boundary
`4a+t=A`.  It is already positive: there `p=3a` and
`mathcal P(3a,a)=C(a)>0`.

Define

\[
\boxed{
 Q_P(a,t)
 =C+F(a)+F(2a)-F(t)-F(a+t)-2\varepsilon .}
\tag{2.3}
\]

### Theorem 2.1

On (0.7), with coordinate (2.1),

\[
                         \boxed{\mathcal P(p,a)>Q_P(a,t).}
\tag{2.4}
\]

Consequently, positivity of `Q_P` on (2.2) proves the complete
long-singleton gate.

### Proof

The exact clock begins

\[
 0,a,2a,p,p+a,p+2a.
\]

The first five values are below `A`, while `p+2a>A`.  Composite-endpoint
descent gives

\[
 \mathcal P(p,a)
 \ge C+F(a)+F(2a)+F(p)+F(p+a).
\tag{2.5}
\]

By (2.1), `p+a=A-t` and `p=A-(a+t)`.  Two applications of (0.3) give
(2.4).

The inequalities `p<A-a` and `p>A-2a` are respectively `t>0` and
`t<a`.  The strict unresolved density condition `p>3a` is `4a+t<A`;
equality is the just-described positive boundary.  Together with
`a<A/4`, these give (2.2) and its stated closed enlargement. \(\square\)

## 3. Consequence and scope

The already-audited five-slot classification is therefore reduced to the
two compact threshold-period inequalities

\[
 Q_R(a,v)>0\quad\hbox{on (1.2)},
 \qquad
 Q_P(a,t)>0\quad\hbox{on the closure of (2.2)}.
\tag{3.1}
\]

The first statement remains a possible uniform target.  The second is a
useful sufficient bound only on subranges, not a viable full-domain target:
at the excluded limiting corner `(a,t)=(A/4,0)` its right side is strictly
negative even though the actual train equals the positive arithmetic clock
`C(A/4)`.  The exact theta-coefficient obstruction is recorded separately.
Thus a proof on the remaining large-`a` part of `mathcal P` must retain more
of the original subthreshold-period train.

Unlike the retracted reverse-monotonicity argument, (1.3) and (2.3) retain
the potentially adverse differences in their correct order.  No
no-interior-minimum comparison is used.  This note does not assert (3.1),
and the full-domain `Q_P` assertion is in fact false by the preceding
boundary obstruction.  No claim is made of five-slot positivity, the
all-grid Bellman inequality, or an OR-word upper bound.
