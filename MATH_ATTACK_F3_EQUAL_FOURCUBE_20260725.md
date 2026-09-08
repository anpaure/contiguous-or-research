# Fifth-wave F: the equal four-cube

Date: 2026-07-25

## 0. Verdict

Let

\[
Q_t=[0,t]^4,
\qquad
M_t=w_4(t,t,t,t)
=\frac{2t^3+6t^2+7t+3}{3}.
\tag{0.1}
\]

This attack does **not** prove

\[
g_4(t,t,t,t)=M_t+o(t^3),
\tag{0.2}
\]

and it does not produce an unrestricted interior dual with positive cubic
excess.  It does, however, leave a substantially smaller exact construction
gate and a sharp obstruction to the dual route tried here.

1. Every target at rank distance \(d\) from the middle is the literal join,
   or literal meet, of a **depth-\((d+1)\) L-portal** of middle points.  If
   both arms are nonempty, the portal seam can be chosen on a coordinate
   facet.  Thus the earlier selectable rectangle of
   \((\alpha+1)(\beta+1)\) middle labels may be replaced by only
   \(\alpha+\beta+1=d+1\) labels.

2. There is an exact carrier theorem converting a near-width packing of
   those portals into one literal max-word.  The only unproved positive
   statement left by this route is the adaptive portal-carrier lemma in
   Section 8.

3. A natural nonadaptive substitute is impossible: a middle-layer row
   which tabulates every side-anchored rectangle support-exactly has length

   \[
   M_t+\left(\frac19+o(1)\right)t^3.
   \tag{0.3}
   \]

   This is an architecture-specific obstruction; it does not apply after
   adaptive portal selection.

4. Every ordinary-rank-band endpoint dual obtained from one or several
   coordinate-color potentials has leading coefficient at most \(2/3\),
   exactly the width coefficient.  This includes asymmetric bands and all
   nonnegative combinations of the displayed inequalities.

5. The failure of cover-edge duals is structural.  The equal four-cube has
   two \(M_t\)-chain partitions whose target-cover edge sets are disjoint.
   Consequently an interior dual must use common **non-cover** comparable
   pairs, endpoint pairing/acyclicity, or coordinate pins; cover-edge
   disjointness alone cannot prove even \(g_4>M_t\).

6. A small unconditional improvement over width survives those
   obstructions:

   \[
   \boxed{
   g_4(t,t,t,t)
   \ge M_t+
   \left\lceil
   \frac{((t+1)^4-M_t)/2-1}{M_t+2t-1}
   \right\rceil
   =M_t+\left(\frac34+o(1)\right)t.}
   \tag{0.4}
   \]

This report uses arbitrary selected literal witnesses throughout.  No
canonical endpoint choice, single physical pin, web search, finite search,
or computational search is used.

---

## 1. Conventions

A word is a finite sequence of nonzero points of \(Q_t\).  It represents a
nonzero target \(x\) if the coordinatewise maximum of some nonempty
contiguous factor is \(x\).  The minimum universal word length is denoted
by \(g_4(t,t,t,t)\).

The middle layer is

\[
H_t=\{x\in Q_t:|x|=2t\}.
\]

Inclusion-exclusion gives

\[
|H_t|
=\binom{2t+3}{3}-4\binom{t+2}{3}
=M_t.
\tag{1.1}
\]

For a family of points, \(\bigvee\) and \(\bigwedge\) denote coordinatewise
join and meet.  Coordinate unit vectors are \(e_1,\ldots,e_4\).

---

## 2. A depth-plus-one facet portal

The local selectable-rectangle problem has an exact one-dimensional
replacement.

### Theorem 2.1 (upper and lower L-portals)

Partition the four coordinates into two ordered pairs

\[
(a,a'),\qquad(b,b').
\]

#### Upper portal

Let \(x\in Q_t\) have \(|x|=2t+d\).  Choose nonnegative integers
\(\alpha,\beta\) such that

\[
\alpha+\beta=d,
\qquad
\alpha\le\min(x_a,x_{a'}),
\qquad
\beta\le\min(x_b,x_{b'}).
\tag{2.1}
\]

Put

\[
v=x-\alpha e_a-\beta e_b,
\tag{2.2}
\]

\[
L_u=v+u e_a-u e_{a'}\quad(0\le u\le\alpha),
\qquad
R_z=v+z e_b-z e_{b'}\quad(0\le z\le\beta).
\tag{2.3}
\]

Then the \(d+1\) distinct middle points in the literal order

\[
L_\alpha,L_{\alpha-1},\ldots,L_0=v,R_1,\ldots,R_\beta
\tag{2.4}
\]

have join exactly \(x\).

#### Lower portal

Let \(|x|=2t-d\).  Choose

\[
\alpha+\beta=d,
\qquad
\alpha\le t-\max(x_a,x_{a'}),
\qquad
\beta\le t-\max(x_b,x_{b'}).
\tag{2.5}
\]

Put

\[
v=x+\alpha e_a+\beta e_b,
\tag{2.6}
\]

\[
L_u=v-u e_a+u e_{a'}\quad(0\le u\le\alpha),
\qquad
R_z=v-z e_b+z e_{b'}\quad(0\le z\le\beta).
\tag{2.7}
\]

The order (2.4) now consists of \(d+1\) distinct middle points and has
meet exactly \(x\).

In either case a legal split exists.  Moreover, one may choose the split
so that either \(\beta=0\), or the seam \(v\) lies on a coordinate facet:

\[
v_a=0\quad\hbox{above the middle},
\qquad
v_a=t\quad\hbox{below the middle}.
\tag{2.8}
\]

#### Proof

For the upper case, put

\[
A=\min(x_a,x_{a'}),\qquad B=\min(x_b,x_{b'}).
\]

For two coordinates in \([0,t]\), their sum is at most \(t\) plus their
minimum.  Hence

\[
A+B\ge |x|-2t=d.
\]

Thus (2.1) is feasible.  Every point in (2.3) has rank \(2t\).  The
inequalities in (2.1) show that every coordinate remains in \([0,t]\), and
every displayed point is coordinatewise at most \(x\).  The four required
maxima occur as follows:

\[
x_a\text{ at }L_\alpha,qquad
x_{a'}\text{ at }v,qquad
x_b\text{ at }R_\beta,qquad
x_{b'}\text{ at }v.
\]

Therefore the join is \(x\).  The two arms vary disjoint coordinate pairs,
so their only common point is \(L_0=R_0=v\); the length is
\(\alpha+\beta+1=d+1\).

For the lower case, put

\[
A=t-\max(x_a,x_{a'}),\qquad
B=t-\max(x_b,x_{b'}).
\]

Since the sum of the two pairwise maxima is at most \(|x|\),

\[
A+B\ge2t-|x|=d.
\]

The same legality and rank check applies to (2.6)--(2.7), now with every
portal point at least \(x\).  The four minima are attained at
\(L_\alpha,v,R_\beta,v\), respectively, so the meet is \(x\).

Finally choose \(\alpha=\min(A,d)\).  If \(\alpha=d\), then \(\beta=0\).
Otherwise \(\alpha=A\); orient \(a\) as a coordinate attaining the upper
minimum or lower maximum.  Equations (2.2) and (2.6) then give (2.8).
\(\square\)

### Example 2.2

The word

\[
(t,0,0,t),(t-1,1,0,t),\ldots,(0,t,0,t),
(0,t,1,t-1),\ldots,(0,t,t,0)
\tag{2.9}
\]

has length \(2t+1\).  Its seam intervals represent all \((t+1)^2\)
targets

\[
(k,t,\ell,t),\qquad0\le k,\ell\le t.
\]

This is the elementary literal model for the global portal packing still
needed below.

---

## 3. Exact portal-carrier theorem

The following factor construction explicitly records every contamination
condition.

Let \(T_1,\ldots,T_L\in H_t\) be indexed middle-label occurrences, and let
each occurrence have an integer carrier interval

\[
J_i\subseteq[N].
\]

At physical position \(k\), define

\[
A_k=\bigwedge_{i:k\in J_i}T_i,
\tag{3.1}
\]

with \(A_k=0\) if no carrier is active.

### Theorem 3.1 (portal-carrier sufficiency)

Assume:

1. every middle label occurs among the \(T_i\), and every indexed
   occurrence is recovered by its carrier:

   \[
   \bigvee_{k\in J_i}A_k=T_i;
   \tag{3.2}
   \]

2. every upper target \(x\) is assigned an upper portal from Theorem 2.1,
   together with indexed occurrences of all its portal labels, such that

   \[
   U_x=\bigcup_{i\text{ in the portal}}J_i
   \tag{3.3}
   \]

   is one physical interval;

3. every lower target \(x\) is assigned a lower portal and indexed
   occurrences whose carriers have a nonempty common physical interval

   \[
   K_x\subseteq\bigcap_{i\text{ in the portal}}J_i;
   \tag{3.4}
   \]

4. for every positive coordinate \(c\) of a lower target, some
   \(k\in K_x\) is a literal pin:

   \[
   \min_{i:k\in J_i}(T_i)_c=x_c.
   \tag{3.5}
   \]

Then \(A_1,\ldots,A_N\), after deleting zero letters, is a universal
range-maximum word for \(Q_t\).  In particular, if

\[
L=M_t+o(t^3),\qquad N=M_t+o(t^3),
\tag{3.6}
\]

then (0.2) holds.

#### Proof

Equation (3.2) represents every middle label on its own carrier interval.

Fix an upper target \(x\).  If \(k\in U_x\), at least one selected portal
carrier contains \(k\).  Its label is at most \(x\), so (3.1) gives
\(A_k\le x\).  Conversely, (3.2) and \(J_i\subseteq U_x\) give

\[
\bigvee_{k\in U_x}A_k\ge T_i
\]

for every selected portal label.  The join of those labels is \(x\) by
Theorem 2.1.  Hence the maximum on the literal interval \(U_x\) is exactly
\(x\).

For a lower target and \(k\in K_x\), every selected portal carrier is
active.  Consequently

\[
A_k\le\bigwedge_{i\text{ in the portal}}T_i=x.
\]

Condition (3.5) supplies equality in every positive coordinate somewhere
inside the same physical interval \(K_x\); zero coordinates are automatic.
Thus \(\bigvee_{k\in K_x}A_k=x\).

Deleting zero letters compresses every selected interval to a contiguous
interval and preserves all positive coordinate pins. \(\square\)

The theorem is strictly weaker than a full selectable-rectangle braid:
only the \(d+1\) portal labels, rather than all
\((\alpha+1)(\beta+1)\) rectangle labels, need compatible carriers.

---

## 4. Two scoped construction obstructions

### 4.1 Universal side-anchored rectangle tables cost cubic excess

This subsection rules out one nonadaptive way of satisfying Theorem 3.1.
It does not rule out adaptive portal choices.

Let

\[
F_a=\{P_{ij}:0\le i,j\le a\}.
\]

A word over \(F_a\) realizes

\[
R(r;c_0,c_1)=[0,r]\times[c_0,c_1]
\]

**support-exactly** if a contiguous factor contains every label of that
rectangle and no label outside it.  Repetitions inside the factor are
allowed.

### Theorem 4.1 (star obstruction)

If a word support-exactly realizes every side-anchored rectangle
\(R(r;c_0,c_1)\), then

\[
|W|-(a+1)^2
\ge
s_a:=
\left\lceil\frac a2\right\rceil
\left\lfloor\frac{a+1}{3}\right\rfloor.
\tag{4.1}
\]

#### Proof

Take

\[
r=0,2,4,\ldots<a,
\qquad
c=1,4,7,\ldots\le a-1,
\]

and form the pairwise label-disjoint stars

\[
Q_{r,c}=
\{P_{r,c-1},P_{r,c},P_{r,c+1},P_{r+1,c}\}.
\tag{4.2}
\]

Suppose all four labels of one star occurred globally exactly once.
Restrict the whole word to these four labels.  The support-exact factors
for

\[
[0,r]\times[c-1,c],
\quad
[0,r]\times[c,c+1],
\quad
[0,r+1]\times\{c\}
\tag{4.3}
\]

would make the unique occurrence of \(P_{r,c}\) adjacent in the restricted
linear order to each of the other three star labels.  A vertex in a linear
order has degree at most two, a contradiction.  Hence every star contains
some repeated label.  The stars are disjoint, and their number is exactly
the right side of (4.1). \(\square\)

The middle layer splits into disjoint square fibers of side parameter

\[
a_u=t-|t-u|,
\qquad0\le u\le2t,
\tag{4.4}
\]

by fixing the first pair sum \(u\).  Thus a row which universally tabulates
every side-anchored rectangle in every fiber pays

\[
\begin{aligned}
\sum_{u=0}^{2t}s_{a_u}
&=2\sum_{a=0}^{t-1}s_a+s_t\\
&=\frac19t^3+O(t^2).
\end{aligned}
\tag{4.5}
\]

Since the fiber alphabets partition \(H_t\), this proves (0.3).

The scope is important.  Actual maximum witnesses may contain additional
dominated labels, and Theorem 3.1 chooses only one portal per target.
Neither freedom is covered by Theorem 4.1.

### 4.2 A full fixed delay forces only quadratic excess

For a middle point \(z\), call each condition \(z_c\ge h\),
\(1\le h\le t\), a positive coordinate-threshold atom.  Every middle point
has exactly \(2t\) positive atoms.

### Proposition 4.2 (atom-run ledger)

Let \(T_1,\ldots,T_N\in H_t\) contain every middle label.  Suppose every
internal positive run of every threshold atom has length at least \(q+1\).
Then

\[
\boxed{
2tN\ge(q+1)\max\{0,M_t-1-2t\}.}
\tag{4.6}
\]

#### Proof

After suppressing consecutive repetitions, a sequence visiting \(M_t\)
distinct labels has at least \(M_t-1\) nontrivial transitions.  At a
transition between two distinct labels of the same rank, at least one
threshold atom changes from absent to present.  Each such change begins a
positive run.  At most \(2t\) of these runs are suffix runs, because the
final middle label contains exactly \(2t\) atoms.  Hence there are at least
\(M_t-1-2t\) internal positive runs.

Their total length is at most the total atom incidence \(2tN\), proving
(4.6). \(\square\)

For the full-depth fixed delay \(q=2t\), (4.6) gives

\[
N\ge
\left\lceil
M_t+\frac{t^2}{3}-t-\frac56
\right\rceil.
\tag{4.7}
\]

Thus, for \(t\ge4\), a width-exact common-delay erosion is impossible.  The
argument does not give cubic excess and does not obstruct (0.2).

---

## 5. Exact ordinary-rank-band endpoint dual

We next state the strongest coordinate-color band inequality obtained in
this attack and then prove that it never beats width cubically.

Retain all targets in ranks

\[
u,u+1,\ldots,v,
\qquad1\le u\le v\le4t,
\]

and put

\[
J=v-u,
\quad
T=\sum_{j=u}^v|Q_{t,j}|,
\quad
B_-=|Q_{t,u}|,
\quad
B_+=|Q_{t,v}|.
\tag{5.1}
\]

Let \(C_0\) be the number of lines parallel to one fixed coordinate axis
which meet the band.  By symmetry this is independent of the axis.

### Theorem 5.1 (finite subset-color band inequality)

For \(k\in\{1,2,3\}\), put \(m=4-k\) and

\[
K_m=
2T-B_--B_+
-\frac m4(vB_+-uB_-)
+mtB_+.
\tag{5.2}
\]

Then

\[
\boxed{
g_4(t,t,t,t)
\ge
\left\lceil
\frac{K_m-\frac{k}{2}(T-C_0)}{J+mt}
\right\rceil.}
\tag{5.3}
\]

#### Proof

Choose one arbitrary literal witness for every target in the band.  Use
that same witness to form the left- and right-endpoint partitions.  In
either partition, targets with one endpoint in common form a chain.  If
the partition has \(C\) nonempty classes, the class sets meeting adjacent
ranks force at least

\[
U(C)=2T-B_--B_+-JC
\tag{5.4}
\]

target-poset cover edges.

Fix a \(k\)-set \(S\) of coordinate colors, and use the complementary
potential

\[
\phi_{S^c}(x)=\sum_{i\notin S}x_i,
\qquad0\le\phi_{S^c}\le mt.
\tag{5.5}
\]

Every used cover whose color is outside \(S\) consumes one unit of this
potential.  Telescoping over the endpoint chains gives the upper bound

\[
\frac m4(vB_+-uB_-)+mt(C-B_+).
\tag{5.6}
\]

Indeed, coordinate symmetry makes the potential mass of a rank-\(r\)
layer equal to \((m/4)r\) times its size.  Chains missing the top boundary
have terminal potential at most \(mt\), while internal initial potentials
may only decrease the total rise.

Subtracting (5.6) from (5.4), the partition uses at least

\[
K_m-(J+mt)C
\tag{5.7}
\]

covers whose color lies in \(S\).

Sum (5.7) over all \(\binom4k\) choices of \(S\).  Each used cover is
counted \(\binom3{k-1}\) times.  The two endpoint partitions cannot share
a target cover edge: its two distinct endpoints would then lie in one
common left class and one common right class, giving the same selected
interval twice.  The total number of band cover edges is

\[
A=4(T-C_0),
\tag{5.8}
\]

because each active coordinate line contributes one fewer edge than
vertices.  Both chain counts are at most the physical word length \(n\).
Therefore

\[
2\binom4k\bigl(K_m-(J+mt)n\bigr)
\le
\binom3{k-1}A.
\]

Using

\[
\frac{\binom3{k-1}}{2\binom4k}=\frac{k}{8}
\]

and taking the integer ceiling proves (5.3). \(\square\)

### Theorem 5.2 (complete cubic collapse of this band family)

Let

\[
u=(2+x)t+O(1),
\qquad
v=(2+y)t+O(1),
\qquad
-2\le x\le y\le2.
\]

The leading coefficient supplied by (5.3) is

\[
L_m(x,y)=\frac{mQ(x,y)}{m+y-x},
\tag{5.9}
\]

where

\[
\rho(z)=
\begin{cases}
\displaystyle\frac23-z^2+\frac{|z|^3}{2},&|z|\le1,\\[1ex]
\displaystyle\frac{(2-|z|)^3}{6},&1\le|z|\le2,
\end{cases}
\tag{5.10}
\]

and

\[
Q(x,y)=
\frac12\int_x^y\rho(z)\,dz
+\frac{(2+x)\rho(x)+(2-y)\rho(y)}4.
\tag{5.11}
\]

For every allowed \(x,y\) and \(m=1,2,3\),

\[
\boxed{L_m(x,y)\le\frac23.}
\tag{5.12}
\]

Consequently no nonnegative combination of ordinary-rank-band inequalities
of the form (5.3) proves positive cubic excess.

#### Proof

The rank layer at \((2+z)t+O(1)\) has size
\(\rho(z)t^3+O(t^2)\).  Hence \(T\) has leading term
\(t^4\int_x^y\rho\), while \(C_0=O(t^3)\) is one order smaller.  Substitution
in (5.3) gives (5.9)--(5.11).

For fixed \(x,y\), the right side of (5.9) increases with \(m\), so it is
enough to take \(m=3\).  We prove

\[
3Q(x,y)\le2+\frac23(y-x),
\tag{5.13}
\]

which is equivalent to (5.12) for \(m=3\).

First suppose \(x=-a\le0\le b=y\).  Define

\[
F(a)=\frac12\int_0^a\rho(z)\,dz
+\frac{(2-a)\rho(a)}4.
\tag{5.14}
\]

Then \(Q(-a,b)=F(a)+F(b)\), and direct integration gives

\[
F(a)=
\begin{cases}
\displaystyle
\frac13+\frac a6-\frac{a^2}{2}+\frac{a^3}{3}-\frac{a^4}{16},
&0\le a\le1,\\[1.5ex]
\displaystyle
\frac14+\frac{(2-a)^4}{48},
&1\le a\le2.
\end{cases}
\tag{5.15}
\]

In both ranges,

\[
3F(a)\le1+\frac{2a}{3}.
\tag{5.16}
\]

For \(0\le a\le1\), the difference is

\[
\frac a6+\frac{3a^2}{2}-a^3+\frac{3a^4}{16}\ge0;
\]

for \(1\le a\le2\), (5.16) is immediate from the second line of
(5.15).  Adding (5.16) for \(a,b\) proves (5.13).

Now suppose \(x\le y\le0\), and put

\[
D(x,y)=2+\frac23(y-x)-3Q(x,y).
\]

Writing \(a=-x\), differentiation gives

\[
\partial_xD=
\begin{cases}
\displaystyle-\frac16-3a+3a^2-\frac34a^3,&0\le a\le1,\\[1ex]
\displaystyle-\frac23-\frac{(2-a)^3}{4},&1\le a\le2.
\end{cases}
\tag{5.17}
\]

Both expressions are negative.  Therefore

\[
D(x,y)\ge D(y,y)=2-3\rho(y)\ge0.
\]

Intervals above the middle follow by the complement symmetry
\(Q(x,y)=Q(-y,-x)\).  This proves (5.13).

Finally, a nonnegative sum of valid inequalities has normalized right side
equal to a weighted average of their individual normalized right sides, so
it also cannot exceed \(2/3\). \(\square\)

### Audit correction: the false \(d=t/4\) excess

For the symmetric band \(2t-d\le|x|\le2t+d\), a valid specialization of
Theorem 5.1 is

\[
n\ge
\left\lceil
\frac{3T+C_0+(6t-3d-4)B}{2(3t+2d)}
\right\rceil,
\tag{5.18}
\]

where \(B\) is one boundary size.  At \(d=\lfloor t/4\rfloor\),

\[
B\sim\frac{235}{384}t^3,
\quad
T\sim\frac{995}{3072}t^4,
\quad
C_0\sim\frac{55}{64}t^3.
\]

The coordinate-line term \(C_0\) is only cubic before division by a linear
denominator, so it contributes only \(O(t^2)\) to the word bound.  The
correct leading coefficient is

\[
\frac{4285}{7168}<\frac23,
\tag{5.19}
\]

not \(5165/7168\).  The latter number results from incorrectly promoting
\(C_0\) by one power of \(t\).

---

## 6. Structural saturation: two edge-disjoint chain partitions

The preceding collapse is not an accident of the chosen linear
potentials.

### Theorem 6.1 (edge-disjoint product SCDs)

The poset \([0,t]^4\) has two symmetric chain decompositions, each with
exactly \(M_t\) chains, whose target-poset cover-edge sets are disjoint.
After deletion of the global zero, they give two edge-disjoint
\(M_t\)-chain partitions of the nonzero poset.

#### Proof

In \([0,t]^2\), for \(0\le k\le t\), define

\[
C_k=(k,0),(k,1),\ldots,(k,t-k),
(k+1,t-k),\ldots,(t,t-k).
\tag{6.1}
\]

These chains partition the square and run from rank \(k\) to rank
\(2t-k\).  Let \(D_k\) be their coordinate swaps.

A vertical \(C\)-edge has lower endpoint \((x,y)\) with \(x+y<t\), while a
horizontal \(C\)-edge has lower endpoint with \(x+y\ge t\).  For the
\(D\)-decomposition the two roles are reversed.  Hence the \(C\)- and
\(D\)-edge sets are disjoint, including the rank-\(t\) boundary.

Now partition the first and second coordinate squares by the \(C\)-chains.
Each product \(C_i\times C_j\) is a rectangle of two chains.  For
completeness, if their edge lengths are \(p\le q\), the required rectangle
decomposition consists, for \(0\le h\le p\), of the hook

\[
(h,0),(h,1),\ldots,(h,q-h),
(h+1,q-h),\ldots,(p,q-h).
\tag{6.2}
\]

(Interchange the two factors when \(q<p\).)

The hooks are disjoint and cover \([0,p]\times[0,q]\): a point \((i,j)\)
with \(i+j\le q\) lies on the vertical part of hook \(h=i\), while a point
with \(i+j\ge q\) lies on the horizontal part of hook \(h=q-j\), with the
common corner counted only once.  Hook \(h\) runs from local rank \(h\) to
local rank \(p+q-h\), so it is symmetric.

Apply (6.2) in every \(C_i\times C_j\).  Every resulting
four-dimensional cover edge projects to a \(C\)-edge in the changing square
factor.  Doing the same with \(D_i\times D_j\) uses only \(D\)-edges, so the
two resulting four-cube decompositions are edge-disjoint.

Every chain is symmetric about rank \(2t\), hence meets \(H_t\) exactly
once.  Each decomposition therefore has exactly \(|H_t|=M_t\) chains.
\(\square\)

### Consequence 6.2

No lower-bound argument whose only coupling between the two endpoint-chain
partitions is disjointness of target **cover edges** can prove
\(g_4(t,t,t,t)>M_t\).  The two decompositions in Theorem 6.1 are an exact
feasible certificate for that relaxation.

They are not endpoint schemes for a word.  In particular, a \(C\)-product
chain and a \(D\)-product chain may share two nonconsecutive targets.
Thus edge-disjointness does not imply the required orthogonality

\[
|L\cap R|\le1,
\]

and Theorem 6.1 supplies no endpoint matching, acyclic physical order, or
coordinate pins.  Those are precisely the resources a successful interior
dual may still exploit.

---

## 7. An unconditional physical-endpoint lower bound

Cover edges saturate, but physical endpoint displacement still gives a
strict lower bound.

### Theorem 7.1 (middle-interval displacement)

For \(t\ge1\), put

\[
L_-:=\frac{(t+1)^4-M_t}{2}-1.
\tag{7.1}
\]

Then (0.4) holds.

#### Proof

Let a universal word have length

\[
N=M_t+D.
\]

Choose one arbitrary literal witness

\[
I_x=[\ell_x,r_x]
\]

for every middle target \(x\in H_t\), and choose an arbitrary witness for
every lower target as well.  Fixed-left-endpoint target families
are chains, and so are fixed-right-endpoint families.  Middle targets are
an antichain.  Therefore the \(M_t\) starts \(\ell_x\) are distinct, and
the \(M_t\) ends \(r_x\) are distinct.

Group the selected witnesses of all nonzero targets below the middle by
their left endpoint.  If such a target shares the start \(\ell_x\) of a
middle witness, its end must be strictly before \(r_x\); otherwise its
interval contains \(I_x\), and its maximum cannot have rank below \(2t\).
Distinct targets in the same fixed-start class have distinct ends.  Hence
that class contains at most \(r_x-\ell_x\) lower targets.

There are at most \(D\) remaining start positions.  Each supports a chain
and hence at most one nonzero target in each lower rank
\(1,\ldots,2t-1\), for at most \(2t-1\) lower targets.

If \(R=\{r_x:x\in H_t\}\) and \(L=\{\ell_x:x\in H_t\}\), both are
\(M_t\)-subsets of \([M_t+D]\).  Therefore

\[
\sum_{x\in H_t}(r_x-\ell_x)
=\sum R-\sum L
\le M_tD,
\tag{7.2}
\]

the extremal difference between the last and first \(M_t\) positions.

By rank-complement symmetry, the number of nonzero targets below the
middle is exactly \(L_-\).  The preceding bounds give

\[
L_-\le M_tD+(2t-1)D=(M_t+2t-1)D.
\]

Taking the integer ceiling proves (0.4).  Since
\(L_-=(1/2+o(1))t^4\) and \(M_t=(2/3+o(1))t^3\), the excess is
\((3/4+o(1))t\). \(\square\)

This proof uses non-cover endpoint information, but its scale is linear,
not cubic.

---

## 8. Exact smallest unproved lemma

The surviving construction statement is the following.

> **Adaptive facet-portal carrier braid (APCB) — UNPROVED.**  For every
> \(t\), construct indexed middle labels
> \(T_1,\ldots,T_L\), carrier intervals \(J_i\subseteq[N]\), and an
> adaptive choice of coordinate pairing, orientation, and facet-anchored
> portal from Theorem 2.1 for every off-middle target, such that all four
> hypotheses of Theorem 3.1 hold and
> \[
> L=M_t+o(t^3),
> \qquad
> N=M_t+o(t^3).
> \tag{APCB}
> \]

APCB immediately implies (0.2) by Theorem 3.1.  It is smaller than the
former selectable-rectangle lemma in two literal senses:

1. a rank-distance-\(d\) target asks for only \(d+1\) middle labels, not a
   quadratic rectangle of labels;
2. unless the portal is one-armed, its seam lies on one of the eight
   coordinate facets of \(H_t\).

Theorem 4.1 shows why APCB must be adaptive: tabulating all side-anchored
rectangles pays a positive cubic toll.  Proposition 4.2 shows that a single
full-depth delay is not itself ruled out at cubic scale, but it still needs
a global ordering with the required short portal unions and pinned common
cores.

On the negative side, Theorem 6.1 shows that any replacement lemma must
quantify a resource absent from cover-edge ledgers: repeated non-cover
intersections of a left/right chain pair, the acyclic endpoint matching, or
coordinate-pin contamination.  No theorem converting any of those three
resources into cubic excess is proved here.  Cover-edge collisions cannot
substitute for it.

---

## 9. Adversarial audit

The decisive claims were independently reconstructed and attacked.

1. **Portal signs and legality.**  The upper portal subtracts at the seam
   and transfers outward; the lower portal adds at the seam and transfers
   inward.  All points remain in \([0,t]^4\), have rank \(2t\), and are
   distinct except for the common seam.  The four extrema in the proof of
   Theorem 2.1 were checked separately, including \(d=0\) and \(d=2t\).

2. **Carrier contamination.**  For an upper target, an extra active label
   can only lower \(A_k\), while recovery of every selected portal label
   prevents undershoot on the union.  For a lower target, the entire portal
   is active on the common core, so extra labels again only lower the meet;
   the explicit coordinate pins are therefore necessary and sufficient.
   Indexed repeated labels, rather than unlabelled values, are used.

3. **False dual coefficient.**  The initially proposed positive coefficient
   at \(d=t/4\) was rejected.  The exact inequality was sound, but the line
   count \(C_0=\Theta(t^3)\) had been treated as \(\Theta(t^4)\).  Equations
   (5.18)--(5.19) are the corrected normalization.

4. **Band endpoint choice.**  Both endpoint partitions always use the same
   arbitrarily selected witness for each target.  Cover-edge disjointness
   follows from full left/right orthogonality of those selected intervals;
   no shortest or canonical witness is assumed.

5. **Product-SCD scope.**  The square \(C/D\) edge split and its product
   lift were independently verified.  The result is deliberately called an
   edge-disjoint relaxation certificate, not a word construction.  The
   product chains can share nonconsecutive vertices, so orthogonality,
   acyclicity, and pins remain open.

6. **Star charge.**  The star argument charges one repeated label somewhere
   in each disjoint four-label star; it does not assume that the center
   itself repeats.  Its conclusion requires support-exact realization of
   every listed rectangle and does not apply to adaptive portals or factors
   containing extra dominated labels.

7. **Endpoint displacement.**  The \(-1\) in (7.1) removes the global zero.
   A lower target sharing a middle start must end before the middle end;
   this is interval containment, not cover adjacency.  The ceiling in
   (0.4) is therefore exact.

### Final status

The equal cube remains unresolved.  The strongest constructive advance is
the exact reduction from selectable rectangles to facet-anchored
depth-plus-one portals.  The strongest negative advance is structural:
two edge-disjoint minimum chain partitions eliminate the entire
cover-edge-only interior-dual route.  APCB is the smallest precise positive
lemma left by this attack.
