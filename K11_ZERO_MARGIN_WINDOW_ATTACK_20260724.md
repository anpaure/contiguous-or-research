# A window-and-run attack on the zero-margin \(k=11\) templates

## 1. Outcome

This note attacks the zero-Hall-margin templates in
`K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md` using only exact window
ranks, coordinatewise binary runs, Johnson adjacency, endpoint identities,
and the finite point degrees of the \(11\)-coordinate subset layers.

No contradiction is obtained.  The attack does produce a stronger exact
normal form.

Let

\[
A_0,A_1,\ldots,A_{m-1}\subseteq[11]
\]

be the central rank-at-most-three segment called \(D_3\) at \(n_5=133\)
and \(M_3\) at \(n_5=132\).  Put

\[
\begin{aligned}
B_i&=A_i\cup A_{i+1},\\
C_i&=A_i\cup A_{i+1}\cup A_{i+2},\\
T_i&=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\end{aligned}
\]

There is one seam triple \(H=C_s\) of rank
\(\rho\in\{3,4\}\).  Every other triple has rank five, and all four-windows
\(T_i\) are distinct six-sets.

The new conclusions are:

1. The sequence \(T_0,T_1,\ldots,T_{m-4}\) is a simple Johnson path in
   \(J(11,6)\), except for at most one jump at the seam.  If the seam is
   internal to the transition sequence and that jump has Johnson distance
   \(1+\eta\), then
   \[
   0\le\eta\le5-\rho.
   \]
   Every ordinary five-window has rank exactly seven, while the one
   seam-centered five-window has rank \(7+\eta\).

2. The number of coordinate zero runs of length exactly three is not merely
   bounded:
   \[
   \boxed{
   E_3=7-\rho-\eta.
   }
   \]
   If the seam is at one end, set \(\eta=0\).  The same formula holds, with
   the seam contribution absorbed by that boundary.

3. Every length-two zero run is localized to an endpoint, a low pair under
   \(H\), or, only in mode C0 at \(n_5=132\), the one extra low pair.
   No ordinary rank-four pair can support a length-two zero run.

4. At \(n_5=133\), let \(\lambda_x\) be the number of distinct literal
   rank-four boundary values containing coordinate \(x\), let \(r_x\) be
   the incidence of \(x\) in repeated rank-at-most-three entries of \(D_3\),
   and let \(Z_x\) be the number of zero runs of \(x\) in \(D_3\).  If
   \(I\) is the intersection of the two seam-pair colors, then
   \[
   \boxed{
   Z_x+\lambda_x+r_x
   =65+\mathbf1_{x\in H}+2\mathbf1_{x\in I}.
   }
   \]
   This is an exact eleven-coordinate incidence budget, not an average
   inequality.

5. In mode D at \(n_5=132\), an internal seam has the exact form
   \[
   L,\{a\},\{b\},\{c\},R,
   \qquad H=\{a,b,c\},
   \]
   where \(L,R\) are three-sets disjoint from \(H\) and
   \[
   |L\cap R|=2-\eta.
   \]
   In mode C0, an internal extra low pair has an explicit four-entry
   normal form recorded in Section 8.

6. Once the selected witness families are fixed, equality at the external
   endpoints canonically pairs the complete rank-five and rank-six layers
   by inclusion.  In the resulting perfect matching, every coordinate is
   the unique added coordinate exactly
   \(42\) times.  Ordered by physical endpoints, the rank-six witnesses
   have offset schedule
   \[
   01^*\,02^*\,03^*\,13^*\,23^*,
   \]
   and every central four-window belongs to the \(03\) block.

7. In endpoint order, the complete rank-five layer is a spanning linear
   forest in \(J(11,5)\) with at most six components.  At least \(456\) of
   the rank-six targets are its distinct edge-union colors.  With the
   matching orientation fixed by the endpoint states, every coordinate
   labels between \(36\) and \(42\) forest edges.  Equivalently, all 924
   middle-level vertices split into at most six alternating paths.

These refinements reduce the remaining problem to a one-jump flag path
through the \(4\)-, \(5\)-, and \(6\)-subset Johnson layers with exact
coordinate-run budgets.  They do not make that path impossible.  The
parity, endpoint, and layer-capacity attacks below all close as identities
or retain substantial slack.

No solver, finite search, random experiment, or computer enumeration is
used.

## 2. Exact central templates used

### 2.1 The \(n_5=133\) slice

The source proves

\[
C=P_4\ \Vert\ D_3\ \Vert\ Q_4,
\qquad
m:=|D_3|=332-n_4.
\]

Every entry of \(D_3\) has rank at most three.  Inside \(D_3\):

* exactly two consecutive pairs, the pairs under \(H\), have rank below
  four;
* the other \(m-3=329-n_4\) pairs are distinct rank-four targets;
* \(H\) has rank four;
* the other \(m-3\) triples are distinct rank-five targets; and
* all \(m-3\) four-windows are distinct rank-six targets.

There are two seam types.

* Type \((2,3)\), including its reversal:
  \[
  |B_s|+|B_{s+1}|=5,
  \quad
  (z_1,z_2,z_3)=(11,54,164).
  \]
* Type \((3,3)\):
  \[
  |B_s|+|B_{s+1}|=6,
  \quad
  (z_1,z_2,z_3)=(11,55,163).
  \]

Put

\[
r=103-n_4=m-229
\]

for the number of repeated lower entries, and let \(r_j\) be the number of
those repetitions having rank \(j\).  Thus

\[
r_1+r_2+r_3=r.
\]

### 2.2 The \(n_5=132\) modes

The five exact modes are:

\[
\begin{array}{c|c}
\text{mode}&(x_4,s_3,\rho,t_\ast,g)\\ \hline
A&(1,1,4,2,0)\\
B&(0,2,4,2,0)\\
C0&(0,1,4,3,0)\\
C1&(0,1,4,3,1)\\
D&(0,1,3,3,0).
\end{array}
\]

The central segment \(M_3\) has length

\[
m=
\begin{cases}
333-n_4,&A,C0,D,\\
332-n_4,&B,C1.
\end{cases}
\]

Every triple except \(H\) has rank five and every four-window has rank six
and a distinct target value.

Modes A, B, and C1 have exactly the two seam pairs below rank four.  Mode C0
has those two and one additional low pair.  Mode D has two rank-two seam
pairs and a rank-three seam triple.

## 3. The one-jump Johnson normal form

There are \(m-3\) four-windows

\[
T_0,\ldots,T_{m-4}.
\]

They are distinct six-sets.  Consecutive four-windows satisfy

\[
C_{i+1}\subseteq T_i\cap T_{i+1}.
\tag{3.1}
\]

If \(C_{i+1}\ne H\), then \(|C_{i+1}|=5\).  Since \(T_i,T_{i+1}\) are
distinct six-sets, their intersection cannot have rank six.  Hence

\[
T_i\cap T_{i+1}=C_{i+1},
\qquad
|T_i\cup T_{i+1}|=7.
\tag{3.2}
\]

Thus every ordinary transition is one Johnson swap.

Suppose \(H=C_s\) is internal to the transition sequence:

\[
1\le s\le m-4.
\]

Define

\[
d_J:=6-|T_{s-1}\cap T_s|,
\qquad
\eta:=d_J-1.
\tag{3.3}
\]

The two six-sets are distinct, so \(d_J\ge1\).  Their intersection contains
\(H\), so

\[
6-d_J\ge\rho.
\]

Therefore

\[
\boxed{
0\le\eta\le5-\rho.
}
\tag{3.4}
\]

Moreover

\[
|T_{s-1}\cup T_s|
=12-|T_{s-1}\cap T_s|
=7+\eta.
\tag{3.5}
\]

If \(H\) is the first or last triple, it is not centered on a five-window
transition.  In that case set \(\eta=0\).

It follows that the sum \(U_5\) of all five-window ranks is exactly

\[
\boxed{
U_5=7(m-4)+\eta.
}
\tag{3.6}
\]

For \(\rho=4\), the exceptional five-window has rank seven or eight.  For
\(\rho=3\), it has rank seven, eight, or nine.

### 3.1 The full three-level flag path away from defects

Whenever \(B_i,B_{i+1}\) are ordinary rank-four pair colors and
\(C_i\) is ordinary,

\[
B_i\cup B_{i+1}=C_i,
\qquad
|B_i\cap B_{i+1}|=3.
\tag{3.7}
\]

Thus the ordinary rank-four pair colors form Johnson paths in \(J(11,4)\).
Their edge-union labels are the distinct rank-five triple targets.

Likewise, consecutive ordinary rank-five triple colors are Johnson-adjacent:

\[
C_i\cup C_{i+1}=T_i,
\qquad
C_i\cap C_{i+1}=B_{i+1}
\tag{3.8}
\]

whenever the middle pair is ordinary.  Finally, (3.2) makes the distinct
rank-six four-window colors a Johnson path whose edge intersections are the
triple colors.

Equivalently, away from the finite defect cells,

\[
\text{rank-4 path vertex}
\subset
\text{rank-5 edge union}
\subset
\text{rank-6 next edge union}
\]

is an exact sliding flag path.  Three consecutive ordinary pair colors have
union \(T_i\), and those unions are globally distinct.

### 3.2 Equality in the rank-six endpoint charge

The endpoint argument forcing the four-windows has a further equality
consequence.  Let the central segment occupy physical positions
\([L,R]\), so \(m=R-L+1\).  Let \(X\) be the selected rank-six intervals
whose left endpoint is before \(L\), and let \(Y\) be those whose right
endpoint is after \(R\).

First choose every central four-window as the witness for its rank-six
value.  The 462 selected rank-six intervals have distinct left and right
endpoints in 465 positions, so each has physical length at most four.
Every interval of length at most three inside the central segment has rank
at most five.  Thus its only selected rank-six intervals are precisely the
\(m-3\) four-windows, and all other selected rank-six intervals lie
outside the segment.

Distinct endpoint order gives

\[
|X|\le L,
\qquad
|Y|\le464-R,
\]

while every selected rank-six interval outside the central segment belongs
to \(X\cup Y\).  There are exactly

\[
462-(m-3)=465-m=L+(464-R)
\]

such outside intervals.  Therefore equality holds in the union bound:

\[
\boxed{
|X|=L,\qquad |Y|=464-R,\qquad X\cap Y=\varnothing.
}
\tag{3.9}
\]

Consequently:

* every physical position before \(L\) is the left endpoint of exactly one
  selected rank-six interval;
* every physical position after \(R\) is the right endpoint of exactly one;
* no selected rank-six interval starts before the central segment and ends
  after it; and
* the \(m-3\) central four-windows form one consecutive block in the global
  rank-six endpoint order.

Indeed, the central block uses every left endpoint \(L,\ldots,R-3\) and
every right endpoint \(L+3,\ldots,R\).  A suffix interval in \(Y\) therefore
has left endpoint at least \(R-2\), while a prefix interval in \(X\) has
right endpoint at most \(L+2\).

This is a genuine endpoint saturation theorem.  It does not determine the
rank-six target values outside the segment, so it does not close the
point-degree attack in Section 11.

The rank-five family satisfies the same external-endpoint equality.  Inside
the central segment, every cell of length at most two has rank at most four,
and exactly the \(m-3\) triples other than \(H\) are the selected rank-five
witnesses.  Hence exactly \(465-m\) selected rank-five intervals lie
outside.  Distinct endpoint order again forces all left slots before \(L\)
and all right slots after \(R\) to be saturated, with no rank-five witness
crossing the whole segment.  The selected central triples form one
consecutive block in rank-five endpoint order, with the physical seam cell
\(H\) as the sole missing triple.

### 3.3 A perfect rank-five/rank-six inclusion matching

For the fixed selected witness families, the two endpoint saturations
canonically match every selected rank-five target to a selected rank-six
target containing it.

* Before the central segment, match the unique rank-five and rank-six
  witnesses having the same saturated left endpoint.  The rank-six interval
  must end later, so the rank-five target is a proper subset of it.
* After the central segment, match the two witnesses having the same
  saturated right endpoint.  The rank-six interval must start earlier.
* For central triples before the seam, match
  \[
  C_i\longmapsto T_i
  \qquad(i<s);
  \]
  these intervals have the same left endpoint.
* For central triples after the seam, match
  \[
  C_i\longmapsto T_{i-1}
  \qquad(i>s);
  \]
  these intervals have the same right endpoint.

The central rule uses every four-window exactly once:

\[
\{T_i:i<s\}\ \sqcup\ \{T_{i-1}:i>s\}
=\{T_0,\ldots,T_{m-4}\}.
\]

The external rule uses \(465-m\) pairs and the central rule uses \(m-3\),
for a total of 462.  Since the selected target values at each rank are the
complete layers, this is a perfect inclusion matching

\[
\binom{[11]}5\longrightarrow\binom{[11]}6.
\tag{3.10}
\]

Every matched edge adds one coordinate.  For a fixed coordinate \(x\), the
number of edges adding \(x\) is forced by the point degrees of the two full
layers:

\[
\binom{10}{5}-\binom{10}{4}=252-210=42.
\]

Hence

\[
\boxed{
\text{each coordinate is the unique rank-five-to-rank-six extension
exactly 42 times.}
}
\tag{3.11}
\]

For the central matches these extension labels are literal window data:
\[
T_i\setminus C_i\subseteq A_{i+3}\quad(i<s),
\qquad
T_{i-1}\setminus C_i\subseteq A_{i-1}\quad(i>s).
\]
The remaining labels come from the matched external witnesses.  Equation
(3.11) is exact, but the present template does not separately fix the
central and external shares, so it does not yet contradict a survivor.

### 3.4 The ordered endpoint schedule

The matching in Section 3.3 is also order preserving.  To make this
precise, list the selected rank-five and rank-six intervals by increasing
left endpoint:

\[
I_j=[\ell_j,r_j],
\qquad
J_j=[u_j,v_j],
\qquad 0\le j<462.
\]

For either family, strict increase of both endpoint sequences in a word of
length \(465\) gives

\[
0\le \ell_j-j\le r_j-j\le3,
\qquad
0\le u_j-j\le v_j-j\le3.
\tag{3.12}
\]

Write an interval's *offset state* as the two-digit word formed by these
endpoint offsets.  All five classified \(n_5=132\) modes, as well as the
\(n_5=133\) slice, lie in the one-component rank-five chain-A branch.
Denote its six successive cutpoints by
\(h_1,\ldots,h_6\); the carrier condition is \(h_3=h_4\):

\[
00^*\,01^*\,02^*\,13^*\,23^*\,33^*.
\tag{3.13}
\]

The rank-six intervals cannot be singletons, because every word entry has
rank at most five.  Moreover the central four-windows have physical form
\([p,p+3]\).  Endpoint saturation says that the four-window starting at
\(p\) has global index \(j=p\), so its rank-six offset state is \(03\).
Monotonicity of both offsets then leaves only

\[
\boxed{
01^*\,02^*\,03^*\,13^*\,23^*
}
\tag{3.14}
\]

for the full rank-six schedule.  Before the central \(03\) block the left
offset must be zero; after it the right offset must be three.

The canonical matching is in fact

\[
I_j\longmapsto J_j.
\tag{3.15}
\]

For the prefix this follows because the two matched witnesses share their
left endpoint, which is the \(j\)-th occupied left endpoint in both
families.  For the suffix use the common right endpoint.  In the middle,
the index shift caused by omitting \(H\) is exactly the shift in the rule
\(C_i\mapsto T_i\) before the seam and
\(C_i\mapsto T_{i-1}\) after it.

Physical containment \(I_j\subsetneq J_j\) gives the following complete
compatibility table for chain A:

\[
\begin{array}{c|c}
\text{rank-five state}&\text{allowed rank-six state}\\ \hline
00&01,02,03\\
01&02,03\\
02&03\\
13&03\\
23&03,13\\
33&03,13,23.
\end{array}
\tag{3.16}
\]

If the five rank-six blocks in (3.14) have cutpoints

\[
0\le g_1\le g_2\le g_3\le g_4\le462,
\]

then comparison with the chain-A cutpoints gives

\[
g_1\le h_1,
\qquad
g_2\le h_2,
\qquad
g_3\ge h_5,
\qquad
g_4\ge h_6.
\tag{3.16A}
\]

Indeed, rank-six state \(01\) can match only rank-five state \(00\), state
\(02\) can occur only before the rank-five \(02\) block begins, state
\(13\) only after the rank-five \(13\) block ends, and state \(23\) only
inside the final \(33\) block.  Thus the central index interval
\([h_2,h_5)\) is contained in the rank-six \(03\) block.

Concretely, a central triple before \(H\) has state \(02\), while a central
triple after \(H\) has state \(13\): before
the missing triple its global index equals its physical left endpoint, and
after it the index is one smaller.  Both kinds are rigidly matched to
state \(03\).

If
\(e_x^{\mathrm{cen}}\) is the number of central matching edges whose added
coordinate is \(x\), then (3.11) also gives the individual bound

\[
0\le e_x^{\mathrm{cen}}\le42,
\qquad
e_x^{\mathrm{ext}}=42-e_x^{\mathrm{cen}}.
\tag{3.17}
\]

This ordered symmetric-layer matching is stronger than either endpoint
saturation separately.  It still leaves freedom in the external extension
labels, so (3.17) does not force a collision.

### 3.5 A six-component spanning Johnson forest

Put

\[
S_j=\operatorname{OR}(I_j),
\qquad
U_j=\operatorname{OR}(J_j).
\]

The \(S_j\) list every five-set exactly once and the \(U_j\) list every
six-set exactly once.  Inside any one of the three left-oriented chain-A
state blocks \(00,01,02\), the physical containment table gives

\[
I_j\cup I_{j+1}\subseteq J_j.
\]

Inside any one of the three right-oriented blocks \(13,23,33\), it gives

\[
I_j\cup I_{j+1}\subseteq J_{j+1}.
\]

The two five-set targets are distinct.  Since they lie in a common
six-set, they intersect in four coordinates and are Johnson adjacent.
Moreover their union is exactly the displayed six-set target:

\[
\begin{aligned}
U_j&=S_j\cup S_{j+1}
&&\text{in states }00,01,02,\\
U_{j+1}&=S_j\cup S_{j+1}
&&\text{in states }13,23,33.
\end{aligned}
\tag{3.18}
\]

Delete only the transitions between distinct nonempty state blocks.  The
remaining edges form a spanning linear forest \(F\) in \(J(11,5)\).  If
\(c\) is the number of nonempty chain-A state blocks, then

\[
1\le c\le6,
\qquad
|E(F)|=462-c\ge456.
\tag{3.19}
\]

All edge-union colors in (3.18) are distinct, because they are distinct
members of the selected rank-six family.  Thus \(F\) is rainbow and misses
exactly \(c\) of the 462 rank-six colors.

The omitted matching edge is explicit in each component.  In a
left-oriented state block it is the edge matched from the block's final
five-set; in a right-oriented block it is the edge matched from the block's
first five-set.  Direct every forest edge from the endpoint matched to its
rank-six union color toward the other endpoint.  Each component is then a
directed path pointing toward precisely that unmatched-source vertex.

There is also an exact coordinate label law.  Orient each forest edge in
increasing endpoint index.  On a left-oriented state block label
\(S_jS_{j+1}\) by the entering coordinate
\(S_{j+1}\setminus S_j\).  On a right-oriented block label it by the
leaving coordinate \(S_j\setminus S_{j+1}\).  By (3.18), these are exactly
the added-coordinate labels of the matching edges used by the forest.  In
the matching direction just defined, the label is always the coordinate
gained on moving toward the root.

Let \(f_x\) count forest edges labeled \(x\), and let \(d_x\) count the
unused matching edges whose added coordinate is \(x\).  The 42-extension
law gives eleven separate equations

\[
\boxed{
f_x+d_x=42,
\qquad
d_x\ge0,
\qquad
\sum_{x=1}^{11}d_x=c.
}
\tag{3.20}
\]

In particular

\[
\boxed{42-c\le f_x\le42,\quad\text{so }36\le f_x\le42.}
\tag{3.21}
\]

The same forest has a second coordinatewise run fingerprint.  Let
\(Z_x^F\) be the total number of zero runs in the incidence words of
coordinate \(x\), treating the \(c\) path components separately.  Let
\(\mu_x\) be the number of the \(c\) unused rank-six colors containing
\(x\).  The forest contains all 462 five-set vertices, so coordinate \(x\)
has 210 vertex occurrences.  The binary pair-window identity on \(c\)
components gives

\[
252-\mu_x=210+Z_x^F-c.
\]

Consequently

\[
\boxed{
Z_x^F=42+c-\mu_x,
\qquad
42\le Z_x^F\le42+c,
\qquad
\sum_x Z_x^F=462+5c.
}
\tag{3.22}
\]

Here \(\sum_x\mu_x=6c\), since every omitted color is a six-set.  Finally,
let \(\sigma_x\) count the unused matching sources containing \(x\).
For an unused matching edge its six-set is the disjoint union of its
five-set source and its added coordinate, so

\[
\mu_x=\sigma_x+d_x,
\qquad
\sum_x\sigma_x=5c.
\]

Combining this with (3.20) gives the exact bridge

\[
\boxed{Z_x^F=f_x+c-\sigma_x.}
\tag{3.23}
\]

Here the unused sources are exactly the \(c\) directed roots described
above.  Equation (3.23) can also be read directly on each binary path: the
number of zero runs equals the number of rootward \(0\)-to-\(1\)
transitions, plus one unless the root contains \(x\).

Equivalently, expand every forest edge through its rank-six union color,
and append the unused matching edge at the root.  This produces \(c\)
vertex-disjoint alternating paths in the middle-level graph

\[
\binom{[11]}5\ \cup\ \binom{[11]}6
\]

which together cover all \(924\) vertices.  Each path begins at a five-set
and ends at a six-set.  Let \(\tau_x\) count the initial five-set endpoints
containing \(x\), and let \(g_x\) count the nonmatching inclusion edges
whose deleted coordinate is \(x\).  Coordinate balance from the initial to
the final endpoints gives

\[
\boxed{
g_x=42-\mu_x+\tau_x,
\qquad
\sum_x\tau_x=5c,
\qquad
\sum_xg_x=462-c.
}
\tag{3.24}
\]

Thus every classified survivor induces a spanning path cover of the entire
middle-level graph by at most six paths, with both inclusion-edge label
vectors fixed up to the \(c\) endpoint pairs.

This is a finite eleven-coordinate constraint on the almost-Hamilton
rainbow forest, but it is not inconsistent: the missing \(c\) matching
edges can absorb the entire coordinatewise deficit.

## 4. Window sums and exact zero-run identities

For a coordinate \(x\), write its incidence on \(A_0,\ldots,A_{m-1}\) as a
binary word.  Let \(R^{(\ell)}\) be the total, over all eleven coordinates,
of zero runs of length at least \(\ell\).  Let \(E_\ell\) be the number of
zero runs of length exactly \(\ell\).

If \(U_\ell\) is the sum of the ranks of all length-\(\ell\) windows, then

\[
U_{\ell+1}-U_\ell=R^{(\ell)}-11.
\tag{4.1}
\]

Consequently

\[
E_\ell
=R^{(\ell)}-R^{(\ell+1)}
=2U_{\ell+1}-U_\ell-U_{\ell+2}.
\tag{4.2}
\]

The exact central ranks give

\[
U_3=5(m-3)+\rho,
\qquad
U_4=6(m-3).
\tag{4.3}
\]

Using (3.6),

\[
\begin{aligned}
R^{(3)}
&=U_4-U_3+11
=m+8-\rho,\\
R^{(4)}
&=U_5-U_4+11
=m+1+\eta.
\end{aligned}
\tag{4.4}
\]

Therefore

\[
\boxed{
E_3=R^{(3)}-R^{(4)}
=7-\rho-\eta.
}
\tag{4.5}
\]

This sharpens the source's upper bound.

At a rank-four seam,

\[
E_3=3-\eta\in\{3,2\}.
\]

At a rank-three seam,

\[
E_3=4-\eta\in\{4,3,2\}.
\]

## 5. Complete localization of length-two and length-three zero runs

The global identities have exact local forms.

### 5.1 Length two

Write

\[
b_i=|B_i|,
\qquad
c_i=|C_i|.
\]

A left-boundary zero run of length exactly two is a coordinate absent from
\(A_0\cup A_1\) and present in \(A_2\).  Its multiplicity is

\[
c_0-b_0.
\tag{5.1}
\]

The right-boundary multiplicity is

\[
c_{m-3}-b_{m-2}.
\tag{5.2}
\]

For an internal pair \(B_i\), \(1\le i\le m-3\), the coordinates whose
zero run is exactly the two positions \(i,i+1\) are

\[
\bigl(A_{i-1}\cap A_{i+2}\bigr)\setminus B_i.
\]

Since

\[
C_{i-1}\cup C_i=T_{i-1},
\]

their number is exactly

\[
\boxed{
c_{i-1}+c_i-6-b_i.
}
\tag{5.3}
\]

For an ordinary pair between two ordinary triples, this is

\[
5+5-6-4=0.
\]

Thus an ordinary rank-four pair cannot support a length-two zero run.
Every such run is forced to a boundary or a listed low pair.

### 5.2 Length three

A left-boundary zero run of length exactly three has multiplicity

\[
|T_0|-|C_0|=6-c_0,
\tag{5.4}
\]

and similarly at the right boundary.

For an internal triple \(C_i\), \(1\le i\le m-4\), a length-three zero run
is a coordinate in

\[
\bigl(A_{i-1}\cap A_{i+3}\bigr)\setminus C_i.
\]

Its exact multiplicity is

\[
\boxed{
12-|T_{i-1}\cup T_i|-c_i.
}
\tag{5.5}
\]

At an ordinary triple, (3.2) gives

\[
12-7-5=0.
\]

If the seam is internal, (3.5) gives seam contribution

\[
5-\rho-\eta.
\tag{5.6}
\]

The two ordinary boundaries contribute one each, so

\[
1+1+(5-\rho-\eta)=7-\rho-\eta,
\]

in agreement with (4.5).

If the seam is at the left boundary, that boundary contributes
\[
6-\rho
\]
and the ordinary right boundary contributes one.  This again gives
\(7-\rho\), which is (4.5) with \(\eta=0\).  The right-boundary case is
symmetric.

Thus every exact length-three zero run is completely localized: it is a
boundary entry/exit or one of the coordinates in

\[
(T_{s-1}\cap T_s)\setminus H
\]

at an internal seam.

## 6. Consequences for \(n_5=133\)

### 6.1 Exact short-run counts

Let

\[
s_0=|B_s|+|B_{s+1}|.
\]

The pair-rank sum is

\[
U_2=4(m-3)+s_0.
\tag{6.1}
\]

Using (4.2)--(4.3),

\[
E_2=2U_3-U_2-U_4=8-s_0.
\tag{6.2}
\]

Hence:

\[
\begin{array}{c|c|c}
\text{seam type}&E_2&E_3\\ \hline
(2,3)\text{ or }(3,2)&3&3-\eta\\
(3,3)&2&3-\eta.
\end{array}
\tag{6.3}
\]

For an internal seam, the two ordinary boundaries contribute one
length-two zero run each.  Formula (5.3) contributes one more at the
rank-two seam pair in type \((2,3)\), and zero at either rank-three seam
pair.  This accounts for every length-two run.

If the seam lies at a boundary, (5.1) or (5.2) absorbs the same count.  For
example, a left-boundary type-\((2,3)\) seam contributes

\[
\rho-|B_s|=4-2=2
\]

at that boundary, and the ordinary opposite boundary contributes the third
unit.  No unnamed length-two run remains.

### 6.2 Exact number of length-one zero runs

Let \(r_j\) be the repeated-entry counts from Section 2.1.  In the
\((2,3)\) seam type,

\[
U_1=611+r_1+2r_2+3r_3.
\]

In the \((3,3)\) seam type,

\[
U_1=610+r_1+2r_2+3r_3.
\]

Since

\[
E_1=2U_2-U_1-U_3,
\]

direct substitution gives

\[
\boxed{
\begin{aligned}
(2,3):\quad E_1&=73+2r_1+r_2,\\
(3,3):\quad E_1&=76+2r_1+r_2.
\end{aligned}
}
\tag{6.4}
\]

Thus all repetition at rank one creates two additional isolated
coordinate-zero holes, repetition at rank two creates one, and rank-three
repetition creates none at this level.

### 6.3 Local form of a type-\((2,3)\) seam with neighbors

Use the orientation

\[
A_s=\{x\},\qquad
A_{s+1}=\{y\},\qquad
A_{s+2}=\{c,d\}.
\tag{6.5}
\]

Assume the seam is internal and put

\[
L=A_{s-1},\qquad R=A_{s+3}.
\]

The ordinary triple before \(H\) has rank five:

\[
|L\cup\{x,y\}|=5.
\]

Since \(|L|\le3\), this forces \(L\) to be a three-set disjoint from
\(\{x,y\}\).  The four-window \(L\cup H\) has rank six, so

\[
|L\cap H|=1.
\]

Thus \(L\) contains exactly one of \(c,d\) and two coordinates outside
\(H\).  Write

\[
P=L\setminus H,
\qquad |P|=2.
\]

On the right, \(R\) adds exactly two coordinates outside \(H\); call that
two-set \(Q\).  The ordinary pair \(\{c,d\}\cup R\) has rank four, so
\[
R=Q
\quad\text{or}\quad
R=Q\cup\{c\}
\quad\text{or}\quad
R=Q\cup\{d\}.
\tag{6.6}
\]

The exceptional five-window has rank \(7+\eta\), while its union is
\[
H\cup P\cup Q.
\]
Consequently
\[
\boxed{
|P\cap Q|=1-\eta.
}
\tag{6.7}
\]

If \(\eta=0\), the unique common coordinate of \(P,Q\) is the one internal
length-three zero run.  If \(\eta=1\), the two outside pairs are disjoint
and there is no seam-local length-three zero run.

## 7. The exact eleven-coordinate rank-four budget at \(n_5=133\)

For a coordinate \(x\), define:

* \(o_x\): number of entries of \(D_3\) containing \(x\);
* \(Z_x\): number of zero runs of \(x\) in the binary incidence word of
  \(D_3\);
* \(\lambda_x\): number of the \(n_4\) distinct literal rank-four boundary
  values in \(P_4,Q_4\) containing \(x\);
* \(r_x\): incidence of \(x\) among the \(r=103-n_4\) repeated lower
  entries beyond the first copy of every distinct literal value;
* \(h_x=\mathbf1_{x\in H}\); and
* \(i_x=\mathbf1_{x\in I}\), where
  \[
  I=B_s\cap B_{s+1}.
  \]

The number \(q_x\) of pair windows in \(D_3\) whose OR contains \(x\)
satisfies the binary identity

\[
q_x=o_x+Z_x-1.
\tag{7.1}
\]

The complete rank-four layer has point degree

\[
\binom{10}{3}=120.
\]

It is partitioned into:

* the \(n_4\) distinct literal rank-four values;
* the nonliteral rank-four value \(H\); and
* the \(m-3=329-n_4\) selected rank-four pair colors.

Therefore the selected rank-four pair colors containing \(x\) number

\[
120-\lambda_x-h_x.
\]

The two remaining pair windows are the seam colors.  Their incidence sum is

\[
\mathbf1_{x\in B_s}+\mathbf1_{x\in B_{s+1}}
=h_x+i_x,
\]

because their union is \(H\) and their intersection is \(I\).  Hence

\[
\boxed{
q_x=120-\lambda_x+i_x.
}
\tag{7.2}
\]

All 231 masks of ranks one through three except the two seam-pair values
occur literally in \(D_3\).  The full lower ideal has point degree

\[
1+10+45=56.
\]

The two missing values have coordinate incidence \(h_x+i_x\), and the
repeated entries add \(r_x\).  Thus

\[
o_x=56-h_x-i_x+r_x.
\tag{7.3}
\]

Combining (7.1)--(7.3) gives the promised coordinatewise identity

\[
\boxed{
Z_x+\lambda_x+r_x
=65+h_x+2i_x.
}
\tag{7.4}
\]

The sums of its non-run terms are

\[
\sum_x\lambda_x=4n_4,
\qquad
\sum_xr_x=r_1+2r_2+3r_3,
\qquad
\sum_xh_x=4,
\]

and

\[
\sum_xi_x=
\begin{cases}
1,&(2,3),\\
2,&(3,3).
\end{cases}
\]

Summing (7.4) recovers the global \(R^{(1)}\) identity, but (7.4) is
strictly more informative because it fixes each coordinate separately.

The full core occurrence count of \(x\) is

\[
\lambda_x+o_x.
\]

Equations (7.1)--(7.2) also give

\[
\boxed{
\lambda_x+o_x=121+i_x-Z_x.
}
\tag{7.5}
\]

Thus the distribution of literal rank-four boundary incidence disappears
from the total core occurrence count after the complete rank-four layer is
used.

As one weak consequence, the binary inequality \(Z_x\le o_x+1\) gives

\[
\lambda_x+2r_x
\ge8+2h_x+3i_x.
\tag{7.6}
\]

This leaves ample total incidence and does not contradict either seam type.
The importance of (7.4) is therefore structural rather than eliminative.

## 8. Consequences for the five \(n_5=132\) modes

### 8.1 Exact short-run table

For a rank-four seam put

\[
s_0=|B_s|+|B_{s+1}|\in\{5,6\}.
\]

Modes A, B, and C1 have only these two low pairs.  Therefore

\[
E_2=8-s_0
\]

and

\[
E_3=3-\eta.
\]

Mode C0 has one further low pair of rank \(r_e\in\{2,3\}\).  Its pair-rank
sum is
\[
U_2=4(m-4)+s_0+r_e,
\]
so
\[
\boxed{
E_2=12-s_0-r_e.
}
\tag{8.1}
\]

Mode D has two rank-two seam pairs and \(\rho=3\).  It satisfies

\[
\boxed{
E_2=2,\qquad E_3=4-\eta,\qquad0\le\eta\le2.
}
\tag{8.2}
\]

Thus:

\[
\begin{array}{c|c}
\text{mode/seam}&E_2\\ \hline
A,B,C1\text{ with }(2,3)&3\\
A,B,C1\text{ with }(3,3)&2\\
C0\text{ with }(2,3)&7-r_e\\
C0\text{ with }(3,3)&6-r_e\\
D&2.
\end{array}
\tag{8.3}
\]

Every unit in this table is localized by (5.1)--(5.3).

### 8.2 Coordinatewise budget for all five modes

Let:

* \(\lambda_x\) count distinct literal rank-four target values containing
  \(x\);
* \(\ell_x\) count the low pair colors in \(M_3\) containing \(x\);
* \(k_x\) count the missing literal rank-at-most-three target values
  containing \(x\);
* \(r_x\) count incidence of repeated rank-at-most-three entries;
* \(X_x\) be the incidence vector of the one lower vertex outside \(M_3\)
  in modes B and C1, and zero in A, C0, D;
* \(h_x=\mathbf1_{x\in H}\); and
* \(\delta_4=1\) when \(\rho=4\), zero when \(\rho=3\).

The complete rank-four layer gives the number of selected rank-four pair
colors containing \(x\):

\[
120-\lambda_x-\delta_4h_x.
\]

All of those pair cells lie in \(M_3\).  Adding the low pair cells gives

\[
q_x=120-\lambda_x-\delta_4h_x+\ell_x.
\tag{8.4}
\]

The literal rank-at-most-three entries over all lower components have
incidence

\[
56-k_x+r_x.
\]

After removing the possible outside vertex \(X\), the occurrence count in
\(M_3\) is

\[
o_x=56-k_x+r_x-X_x.
\tag{8.5}
\]

Using \(q_x=o_x+Z_x-1\), one obtains

\[
\boxed{
Z_x
=65-\lambda_x-\delta_4h_x
+\ell_x+k_x-r_x+X_x.
}
\tag{8.6}
\]

In the rank-four carrier modes, the missing lower targets are exactly the
low pair colors, so \(k_x=\ell_x\).  Hence

\[
Z_x
=65-\lambda_x-h_x+2\ell_x-r_x+X_x.
\tag{8.7}
\]

In mode D, the missing lower targets are the two seam-pair colors and
\(H\), so

\[
k_x=\ell_x+h_x
\]

and

\[
Z_x
=65-\lambda_x+2\ell_x+h_x-r_x.
\tag{8.8}
\]

These are exact coordinatewise normal forms for all five modes.

### 8.3 The extra low pair in C0

Let an internal extra low pair be

\[
B=A_i\cup A_{i+1},
\qquad |B|=r_e\in\{2,3\},
\]

away from \(H\).  Its neighboring triples \(C_{i-1},C_i\) are distinct
five-sets and their union \(T_{i-1}\) is a six-set.  Therefore

\[
K:=C_{i-1}\cap C_i
\]

is a four-set containing \(B\).  Write

\[
C_{i-1}=K\cup\{a\},
\qquad
C_i=K\cup\{b\},
\]

where \(a,b\) are distinct and outside \(K\).

If \(|B|=2\), write \(K=B\sqcup J\) with \(|J|=2\).  The outer entries
must contain \(J\cup\{a\}\) and \(J\cup\{b\}\), respectively.  Since their
ranks are at most three, they are exactly those three-sets.  The two middle
entries are nonempty proper subsets whose union is the nonliteral two-set
\(B=\{x,y\}\); hence they are \(\{x\},\{y\}\) in one order.  The exact local
word is

\[
\boxed{
J\cup\{a\},\quad\{x\},\quad\{y\},\quad J\cup\{b\}.
}
\tag{8.9}
\]

The two coordinates of \(J\) are exactly the two length-two zero runs
charged by \(4-r_e=2\).

If \(|B|=3\), then \(K=B\cup\{j\}\).  The outer entries contain
\(\{j,a\}\) and \(\{j,b\}\), with at most one additional coordinate from
\(B\).  The middle entries are nonempty proper subsets of \(B\) whose union
is \(B\).  The coordinate \(j\) is the unique length-two zero run.

If the extra pair is the first or last pair of \(M_3\), the corresponding
boundary formula (5.1) or (5.2) replaces this four-entry form.  The total
count (8.1) is unchanged.

### 8.4 Mode D around an internal seam

The source already forces the seam entries to be three distinct singletons:

\[
A_s=\{a\},\qquad
A_{s+1}=\{b\},\qquad
A_{s+2}=\{c\},
\qquad
H=\{a,b,c\}.
\tag{8.10}
\]

Put

\[
L=A_{s-1},\qquad R=A_{s+3}.
\]

The two neighboring ordinary triples have rank five:

\[
|L\cup\{a,b\}|=5,
\qquad
|\{b,c\}\cup R|=5.
\]

Thus \(L,R\) are three-sets disjoint from the indicated pairs.  The two
four-windows have rank six and contain \(H\), which forces

\[
L\cap H=R\cap H=\varnothing.
\]

Finally,

\[
T_{s-1}\cap T_s
=H\cup(L\cap R)
\]

has rank \(5-\eta\).  Hence

\[
\boxed{
|L\cap R|=2-\eta.
}
\tag{8.11}
\]

Those common coordinates are precisely the \(2-\eta\) seam-local
length-three zero runs.  Together with the two boundary runs, this gives
\(E_3=4-\eta\).

## 9. Birth/death labels forced by the four-window path

The one-jump Johnson path can be read directly on the entry word.

Consider an index \(i\) with

\[
4\le i\le m-5
\]

such that neither transition adjacent to the birth or death of \(A_i\) is
the exceptional seam jump.

The transition

\[
T_{i-4}\longrightarrow T_{i-3}
\]

removes one coordinate from \(A_{i-4}\) and introduces exactly one
coordinate from \(A_i\).  Therefore \(A_i\) contains a unique coordinate
\(b_i\) absent from

\[
A_{i-4}\cup A_{i-3}\cup A_{i-2}\cup A_{i-1}.
\tag{9.1}
\]

Similarly, the transition

\[
T_i\longrightarrow T_{i+1}
\]

removes a unique coordinate \(d_i\in A_i\) which is absent from

\[
A_{i+1}\cup A_{i+2}\cup A_{i+3}\cup A_{i+4}.
\tag{9.2}
\]

The birth and death labels may coincide.

In particular, if \(A_i=\{x\}\) is an ordinary singleton entry in this safe
range, then

\[
b_i=d_i=x.
\]

The coordinate \(x\) is absent from the four entries on either side of its
singleton occurrence.  Thus every safe singleton literal is an isolated
one-run with adjacent zero runs of length at least four.

For a safe rank-two entry, its birth and death labels orient an ordered pair
inside that two-set, possibly a loop if the labels coincide.  Since all
rank-two literal values except the listed missing masks occur, this gives
an orientation decoration of almost the complete graph on eleven
coordinates.  The decoration has no forced balance: rank-three entries and
repetitions contribute additional births and deaths, and the endpoint
difference absorbs the remaining imbalance.  No parity contradiction
follows from this orientation alone.

## 10. Parity and endpoint attacks

For a coordinate \(x\), the membership word

\[
\mathbf1_{x\in T_0},\ldots,\mathbf1_{x\in T_{m-4}}
\]

changes value precisely when a length-at-least-four zero run of \(x\) in
the entry word begins or ends.

Let \(R_x^{(4)}\) be the number of such zero runs, and let

\[
\epsilon_x^L=\mathbf1_{x\notin T_0},
\qquad
\epsilon_x^R=\mathbf1_{x\notin T_{m-4}}.
\]

Then the number \(\deg_x\) of \(T\)-path transitions changing coordinate
\(x\) is

\[
\boxed{
\deg_x=2R_x^{(4)}-\epsilon_x^L-\epsilon_x^R.
}
\tag{10.1}
\]

Since the first and last four-window colors are six-sets,

\[
\sum_x\epsilon_x^L=\sum_x\epsilon_x^R=5.
\]

Summing (10.1) and using \(R^{(4)}=m+1+\eta\) gives

\[
\sum_x\deg_x
=2(m+1+\eta)-10
=2(m-4+\eta).
\tag{10.2}
\]

The Johnson path has \(m-4\) transitions of distance one with one extra
distance \(\eta\) at the seam, so its total coordinate-change count is also

\[
2(m-4+\eta).
\]

Thus the global parity/transition attack closes as an identity.

Coordinatewise, (10.1) implies

\[
\deg_x\equiv
\epsilon_x^L+\epsilon_x^R
\pmod2,
\]

which is exactly the parity of the membership difference between the two
endpoint six-sets.  Without a further theorem fixing those endpoint sets or
the point degrees of the central rank-six subfamily, this supplies no
contradiction.

## 11. Why the present attacks stop

### 11.1 Johnson-layer capacity

The rank-four ordinary colors form at most three simple path pieces after
the low-pair defects are deleted (at most two except in mode C0, whose
additional low pair can split one piece once more).  Their vertices are distinct, their
rank-five edge unions are distinct, and their three-vertex unions are the
distinct rank-six colors.  This is strong, but the relevant layers have

\[
\binom{11}{4}=330,\qquad
\binom{11}{5}=462,\qquad
\binom{11}{6}=462
\]

available labels.  The surviving path lengths in the \(n_5=133,132\)
slices do not exceed these capacities.

Almost every literal three-set occurs as an entry.  At an ordinary
rank-three entry it equals the intersection of its two neighboring
rank-four pair colors.  A fixed three-set has eight rank-four supersets,
so the local Johnson clique has enough room to supply such a transition.
Layer cardinality and this local degree alone do not force a collision.

Globally, Section 3.5 upgrades the complete rank-five endpoint list to a
rainbow spanning Johnson forest with at most six components.  Equations
(3.20)--(3.24) fix its oriented coordinate labels and zero-run counts almost
completely.  Those equations are mutually consistent: the incidences of
the at most six unused matching edges supply exactly the residual terms.

### 11.2 Short zero runs are fully explained

The small values of \(E_2\) and \(E_3\) initially look contradictory to the
large literal lower ideal.  Sections 5--8 show instead that they are exactly
the boundary and seam defects forced by the window ranks.  Ordinary cells
contribute none.  After this localization, no uncharged short run remains
to contradict the eleven-coordinate budget.

### 11.3 The point-degree budget retains slack

Equation (7.4) is exact, but the weak binary bound \(Z_x\le o_x+1\) yields
only (7.6).  Summed over eleven coordinates, the available literal
rank-four incidence and repeated-entry incidence are more than sufficient.
No contradiction follows without an additional restriction on the
distribution of \(\lambda_x\), \(r_x\), or the endpoint six-sets.
The perfect-matching law fixes the *total* extension degree at \(42\) for
each coordinate, but its central/external split in (3.17) remains free.

### 11.4 What would finish this route

Any one of the following would materially strengthen the attack:

1. a theorem fixing or sharply bounding the point-degree vector of the
   central rank-six path \(T_i\);
2. an endpoint theorem linking \(T_0,T_{m-4}\) to the literal rank-four
   boundary families \(P_4,Q_4\);
3. a restriction on how often one three-set can label intersections along
   the rainbow rank-four path;
4. a coupling between the repeat-incidence vector \(r_x\) and the
   birth/death labels in Section 9; or
5. a rank-seven distinctness or congestion theorem for the ordinary
   five-window unions.

None of these is supplied by the present zero-margin classification.

## 12. Final normal form

Every zero-margin \(n_5=133\) or \(132\) survivor therefore has the following
additional exact structure.

1. Its central four-window colors form a simple path of distinct six-sets
   with one possible seam jump of distance \(1+\eta\).
2. Those four-windows form a consecutive, endpoint-saturated block in the
   global rank-six witness order, and no outside rank-six witness crosses
   the whole central segment.
3. The complete rank-five and rank-six layers are paired, in endpoint
   order, by a perfect inclusion matching.  The rank-six endpoint states
   are \(01^*02^*03^*13^*23^*\), the central block is \(03\), and each
   coordinate is the matching extension label exactly \(42\) times.
4. The rank-five endpoint list is a rainbow spanning linear forest in
   \(J(11,5)\) with at most six components and at least 456 distinct
   rank-six edge-union colors.  Equivalently, the 924 middle-level vertices
   admit the induced alternating path cover of (3.24).  Its coordinate
   labels and componentwise zero runs obey (3.20)--(3.24).
5. If the seam triple is internal, all five-windows have rank seven except
   its unique seam-centered window, whose rank is \(7+\eta\). If the seam
   triple is at an endpoint, set \(\eta=0\); there is no seam-centered
   five-window and every five-window has rank seven.
6. The exact number of length-three coordinate zero runs is
   \(7-\rho-\eta\), and every one is boundary- or seam-local.
7. Every length-two coordinate zero run is supported by a boundary or a
   classified low pair.
8. The rank-four, rank-five, and rank-six window colors form a sliding
   Johnson flag path away from those cells.
9. The \(n_5=133\) coordinate runs obey the eleven separate equations
   \[
   Z_x+\lambda_x+r_x=65+h_x+2i_x.
   \]
10. The \(n_5=132\) coordinate runs obey the mode-uniform equation (8.6).
11. Safe singleton entries are isolated coordinate one-runs with four zeros
   on both sides.

This is a genuine strengthening of the classified templates, but it is not
a contradiction.  The remaining construction gate is now a finite-layer
rainbow flag-path problem with exact coordinate-run and endpoint data,
rather than an unconstrained bit assignment.
