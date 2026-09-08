# Five-slot size-four-efficient clocks: exact three-face boundary reduction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It reduces the whole
five-slot size-four-efficient branch to three explicit endpoint faces and
gives a literal endpoint-period lower bound on each face.  It retains the
complete availability-filtered Apéry head.  It does **not** prove the three
remaining train inequalities positive.

Put

\[
 A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Consider a nonnegative
internally superadditive first-crossing table

\[
 (c_0,c_1,c_2,c_3,c_4,c_5)=(0,x,y,z,P,T),
 \qquad x,y,z,P<A\le T,
\tag{0.1}
\]

and suppose the size-four generator has maximal efficiency:

\[
 {P\over4}\ge {x\over1},\quad
 {P\over4}\ge {y\over2},\quad
 {P\over4}\ge {z\over3},\quad
 {P\over4}\ge {T\over5}.
\tag{0.2}
\]

The elementary constraints include

\[
\begin{gathered}
 0\le x\le P/4,
 \qquad2x\le y\le P/2,
 \qquad x+y\le z\le3P/4,\\
 P\ge x+z,
 \qquad P\ge2y,
 \qquad T\ge P+x,
 \qquad T\ge y+z,
 \qquad T\le5P/4.
\end{gathered}
\tag{0.3}
\]

Since `T>=A`, one also has

\[
                         {4A\over5}\le P<A.
\tag{0.4}
\]

## 1. Exact endpoint boundary

Define

\[
 R=\max\{P+x,y+z\},
 \qquad
 T_*=\max\{A,R\}.
\tag{1.1}
\]

### Theorem 1.1 (monotone endpoint reduction)

The table `(0,x,y,z,P,T_*)` is nonnegative, internally superadditive,
first-crossing at size five, and still size-four-efficient.  Moreover

\[
                         \boxed{\Phi(x,y,z,P,T)
                         \ge\Phi(x,y,z,P,T_*).}
\tag{1.2}
\]

#### Proof

The only internal inequalities involving the size-five endpoint are
`c_5>=c_1+c_4` and `c_5>=c_2+c_3`; every other exact-capacity-five
partition is dominated by one of those two through the prefix
superadditivity relations.  Hence `T_*` is the least endpoint at least `A`
that keeps the table internally superadditive.

One has `T_*<=T<=5P/4`, so size four remains maximally efficient.  The
prefix values remain below `A`, while `T_*>=A`, proving first crossing.

Now vary only the endpoint from `T_*` to `T`.  Bellman values below capacity
five do not change.  At every capacity `m>=5`, the endpoint generator gives
`V_m>=T_*>=A`; increasing its value can only increase `V_m`.  The kernel is
increasing on `[A,infinity)`, so every changed summand is nondecreasing.
Summation proves (1.2). \(\square\)

Thus the least endpoint belongs to exactly the following three closed faces,
with overlaps allowed:

\[
\begin{array}{ll}
\mathfrak F_A:&T_*=A,\quad A\ge P+x,\quad A\ge y+z,\\
\mathfrak F_{14}:&T_*=P+x,\quad P+x\ge A,\quad P+x\ge y+z,\\
\mathfrak F_{23}:&T_*=y+z,\quad y+z\ge A,\quad y+z\ge P+x.
\end{array}
\tag{1.3}
\]

This union is exact because it is simply the active-maximum decomposition
of (1.1).

## 2. Endpoint-period Bellman lower bound

For `tau>=A` and `0<=v<A`, write

\[
 F_\tau(v)=\sum_{q\ge0}K(q\tau+v),
 \qquad
 \mathscr B_\tau(x,y,z,P)
 =F_\tau(0)+F_\tau(x)+F_\tau(y)+F_\tau(z)+F_\tau(P).
\tag{2.1}
\]

### Theorem 2.1 (literal five-residue lower bound)

For the boundary table with endpoint `T_*`,

\[
                         \boxed{
 \Phi(x,y,z,P,T_*)\ge
 \mathscr B_{T_*}(x,y,z,P).}
\tag{2.2}
\]

Consequently, every table in the original branch obeys

\[
                         \boxed{
 \Phi(x,y,z,P,T)\ge
 \mathscr B_{T_*}(x,y,z,P).}
\tag{2.3}
\]

#### Proof

Let `V` be the Bellman clock of the boundary table.  For `m=5q+r`,
`0<=r<5`, the configuration with `q` endpoint generators and one size-`r`
generator gives

\[
                         V_{5q+r}\ge qT_*+c_r.
\tag{2.4}
\]

At `q=0`, prefix superadditivity gives equality `V_r=c_r`.  At `q>=1`,
both sides of (2.4) lie in `[A,infinity)`, where `K` is increasing.  Sum
over all five residues and all `q`.  This proves (2.2), and Theorem 1.1
then gives (2.3). \(\square\)

For fixed shifts below `A`, increasing the train period from `A` to `tau`
only increases its terms with `q>=1`.  Hence another exact lower bound is

\[
 \mathscr B_\tau(x,y,z,P)
 \ge C(A)+F_A(x)+F_A(y)+F_A(z)+F_A(P),
\tag{2.5}
\]

where `C(A)=F_A(0)`.  Inequality (2.5) is sometimes weaker because the
pairing constraints on the nonthreshold faces are naturally expressed
relative to `tau`, not to `A`; no sign is asserted here.

## 3. Exact Apéry head remains present

Put

\[
 e_*=T_*-P,
 \qquad
 d_1=e_*-P/4,
 \qquad d_2=y-P/2,
 \qquad d_3=z-3P/4.
\tag{3.1}
\]

All three reduced weights are nonpositive.  The exact eventual residue
weights are

\[
\begin{aligned}
 \beta_1&=\max\{d_1,d_2+d_3,d_1+2d_2,3d_3\},\\
 \beta_2&=\max\{d_2,2d_1,2d_3,d_1+d_2+d_3\},\\
 \beta_3&=\max\{d_3,d_1+d_2,3d_1,2d_2+d_3\},
\end{aligned}
\tag{3.2}
\]

with shifts `s_r=rP/4+beta_r`.  If `V_m^*` is the literal Bellman clock of
the boundary table and

\[
 \widehat V_{4q+r}=qP+s_r,
\]

then the availability-filtered identity is

\[
 \boxed{
 \Phi(x,y,z,P,T_*)
 =\mathcal L_4(P;s_1,s_2,s_3)
 +\sum_{m=0}^{14}\bigl(K(V_m^*)-K(\widehat V_m)\bigr).
 }
\tag{3.3}
\]

The early size-one representative is retained until the better congruent
size-five representative becomes available, and three size-five steps may
first be needed at capacity fifteen.  Thus (3.3) retains all fifteen head
entries.  The lower bound (2.2) was derived from the same literal Bellman
clock rather than by deleting or assigning a sign to any term of this head.

## 4. The two inert faces

### Proposition 4.1

On `mathfrak F_(14)`, the size-five generator is Bellman-inert, because

\[
                         T_*=P+x
\]

is exactly the value of a size-four plus size-one partition.  On
`mathfrak F_(23)`, it is Bellman-inert because

\[
                         T_*=y+z
\]

is exactly the value of a size-two plus size-three partition.

#### Proof

In either case, replace every occurrence of a size-five generator in an
arbitrary Bellman configuration by the displayed lower-denomination pair.
Capacity and value are unchanged.  Hence deleting the size-five generator
does not change any Bellman maximum. \(\square\)

The genuinely active size-five endpoint can therefore occur only on the
part of the threshold face `mathfrak F_A` not covered by either inert face.
On the other two faces the remaining problem is the four-denomination clock
generated by `(x,y,z,P)`, whose displayed denominations all lie below `A`
even though their combinations cross it.

## 5. Sharp remaining boundary statement

The entire size-four-efficient five-slot branch is positive if the following
three finite-dimensional train inequalities hold on their stated faces:

\[
 \mathscr B_A(x,y,z,P)>0
 \qquad\text{on }\mathfrak F_A,
\tag{5.1}
\]

\[
 \mathscr B_{P+x}(x,y,z,P)>0
 \qquad\text{on }\mathfrak F_{14},
\tag{5.2}
\]

and

\[
 \mathscr B_{y+z}(x,y,z,P)>0
 \qquad\text{on }\mathfrak F_{23}.
\tag{5.3}
\]

Conversely, if a nonpositive table exists in this branch, then its boundary
reduction has `mathscr B_(T_*)<=0` on at least one of these faces.  Thus
(5.1)--(5.3) are a proof-safe sufficient target and a necessary obstruction
for a counterexample to survive the endpoint-period lower bound.

The reduction is sharp at the endpoint level: lowering `T_*` further would
either pass below the Gaussian threshold `A` or violate one of the two exact
capacity-five superadditivity constraints.

## 6. Scope

This theorem proves no new Gaussian train sign.  It replaces the interior
endpoint parameter and fifteen potentially adverse head corrections by
three explicit boundary train problems, without assuming any head correction
is nonnegative.  It does not close the size-four-efficient branch, the
size-three- or size-five-efficient branches, the all-slot Bellman inequality,
or an OR-word upper bound.
