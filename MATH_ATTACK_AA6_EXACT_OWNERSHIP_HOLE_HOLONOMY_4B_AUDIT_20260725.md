# AA6 Section 4B audit: optimized doubled-\(K_n\) ownership gap

Date: 2026-07-25

Method: pure mathematics only. No search, computation, or solver is used.

## Outcome

The optimized construction in Section 4B of
`MATH_ATTACK_AA6_EXACT_OWNERSHIP_HOLE_HOLONOMY_NOGO_20260725.md`
is correct.  In particular, its row inventory, rectangle supply, neutral
completion, exact point margins, and hole constant all check exactly.  The
source now also displays the neutral-slot identity and scopes the final
\(1/4\) ceiling explicitly to the doubled-edge template.

Throughout,

\[
n=2m+1,\qquad W=nB,\qquad
N_1=\binom n{m-1},\qquad D=W-N_1,
\]

and \(Q=W/4+O(W/n)\) is the number of rank-\((m-1)\) rectangles left
after deleting those which meet the regular family \(\mathcal U\).

## 1. Exact capacities

One active block has \(n\) components and two rows per component on either
source side.  It therefore consumes \(2n\) rows and has \(2n^2\) target
slots per source side.

There are two gadgets on each edge of \(K_n\).  At an endpoint of an edge,
each gadget uses one target occurrence on either source side.  Thus a
component uses

\[
2\deg_{K_n}(v)=2(n-1)
\]

constraint slots, leaving exactly two of its \(2n\) slots neutral.  Splitting
the constraint labels as \(n-1\) in each row leaves one neutral slot in each
row.  Globally, a block uses

\[
4\binom n2=2n(n-1)
\]

constraint occurrences and leaves \(2n\) neutral occurrences, as required.

The choice

\[
J_*=\min\left\{
\left\lfloor\frac{B}{2n}\right\rfloor,
\left\lfloor\frac{Q}{\binom n2}\right\rfloor
\right\}
\]

gives both exact capacity inequalities

\[
2nJ_*\le B,
\qquad
J_*\binom n2\le Q.
\]

Hence there are enough source rows and enough pairwise disjoint rectangles.
The unused source rows are common fixed rows.

Across all rows, the number of neutral slots is exactly

\[
\begin{aligned}
&2nJ_*+n(B-2nJ_*)\\
&\hspace{1cm}=W-2n(n-1)J_*\\
&\hspace{1cm}=W-4J_*\binom n2.
\end{aligned}
\tag{1}
\]

The constraint rectangles contain exactly
\(4J_*\binom n2\) distinct targets and avoid \(\mathcal U\).  Consequently
the prescribed neutral multiset has size

\[
\left(N_1-4J_*\binom n2\right)+D
=W-4J_*\binom n2,
\tag{2}
\]

which agrees with (1).

## 2. Neutral Hall completion

Place one copy of every target outside the constraint rectangles in distinct
neutral slots.  Exactly \(D\) slots remain, to receive the second copies of
the \(D\) members of \(\mathcal U\).  A second copy is forbidden only from
the row containing its first copy.

Every first-copy row class has size at most \(n\), and every remaining-slot
row class has size at most \(n\).  For a set \(X\) of second copies whose
first copies all lie in one row,

\[
|X|\le n,
\qquad
|N(X)|\ge D-n\ge n\ge |X|
\]

for all sufficiently large \(m\), because \(D>2n\).  If the first copies
of \(X\) lie in at least two rows, every remaining slot is allowed for at
least one member of \(X\), so \(|N(X)|=D\ge |X|\).  Hall's condition holds.

The same assignment can be used on corresponding rows of the two source
sides.  Since rectangles avoid \(\mathcal U\), and all rectangles are
disjoint, no row acquires a repeated target label.

## 3. Exact point margins

Write one rectangle as

\[
x^+=C_0\cup\{x\},\quad y^+=C_0\cup\{y\},\quad
x^-=C_1\cup\{x\},\quad y^-=C_1\cup\{y\}.
\]

Then

\[
\mathbf1_{x^+}-\mathbf1_{y^+}
=\mathbf1_{x^-}-\mathbf1_{y^-}=e_x-e_y.
\tag{3}
\]

At either endpoint component, the \(+\)-gadget and \(-\)-gadget have
opposite side orientations.  Thus the left-minus-right point-incidence
change is

\[
(e_x-e_y)-(e_x-e_y)=0.
\]

Every component switch therefore preserves every coordinate degree.

At the all-left corner, the two endpoints together contribute
\(2\mathbf1_{x^+}+2\mathbf1_{y^-}\).  Its difference from one copy of
each rectangle target is

\[
(\mathbf1_{x^+}-\mathbf1_{y^+})
+(\mathbf1_{y^-}-\mathbf1_{x^-})=0
\]

by (3).  Adding the neutral labels shows that the all-left degree vector is
that of the complete rank-\((m-1)\) layer plus one extra copy of
\(\mathcal U\).  Regularity of \(\mathcal U\) makes this degree

\[
\binom{n-1}{m-2}+\frac{(m-1)D}{n}=(m-1)B
\]

at every coordinate.  All integral children have this same exact point
margin.

## 4. Hole count and asymptotic

For a two-colouring of \(K_{2m+1}\), the largest cut has size

\[
\left\lfloor\frac{n^2}{4}\right\rfloor=m(m+1).
\]

Since

\[
\binom n2=m(2m+1),
\]

the number of monochromatic edges is at least exactly

\[
m(2m+1)-m(m+1)=m^2.
\]

Each monochromatic edge has two gadgets, and each gadget creates exactly one
hole.  Hence every signing has at least \(2m^2J_*\) holes.

Finally,

\[
\begin{aligned}
\frac{Q}{\binom n2}
&=\frac{nB/4+O(B)}{n(n-1)/2}\\
&=\frac{B}{2(n-1)}+O\left(\frac{B}{n^2}\right)\\
&=\left(1+O(n^{-1})\right)\frac{B}{2n}.
\end{aligned}
\]

The floor errors are negligible relative to \(B/(2n)\), so

\[
J_*=\left(1+O(n^{-1})\right)\frac{B}{2n}.
\]

Using \(W=nB\),

\[
\frac{2m^2J_*}{W}
=\left(1+O(n^{-1})\right)\frac{m^2}{n^2}
=\frac14+O(n^{-1}).
\]

This proves the claimed \((1/4-o(1))W\) lower bound.

## 5. The ceiling statement

Within this doubled-edge template, one doubled edge consumes four target
slots on either source side.  Under independent fair component signs, its
two gadgets create one hole in expectation.  Therefore some signing has at
most one hole per doubled edge, and the number of doubled edges is at most
one quarter of total row capacity.  Thus no construction in this template
can force more than \(W/4\) holes.  The complete graph attains this ceiling
asymptotically.
