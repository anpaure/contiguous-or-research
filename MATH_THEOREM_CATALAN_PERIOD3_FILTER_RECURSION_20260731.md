# Period-three outer colours form a smaller Catalan filter problem

Date: 2026-07-31  
Status: exact exceptional-bank bijection and orbit-filter lower bounds;
complement-paired local sharpness when \(v_3(q)=1\), while global extension
remains open

## 1. Exceptional colours are smaller Catalan necklaces

Assume

\[
q=2m-1\equiv0\pmod3.
\]

Since \(q\) is odd, write

\[
q=6a+3=3(2a+1),\qquad m=3a+2.
\]

Identify the ground set with
\(\Omega=\mathbb Z_q\sqcup\{\infty\}\), and let \(K_3\) be the unique
order-three subgroup of \(\mathbb Z_q\).  Its finite-coordinate cosets are
naturally indexed by

\[
\mathbb Z_q/K_3\cong\mathbb Z_{2a+1}.
\]

### Theorem 1 (Catalan exceptional-bank recursion)

The shortened rank-\((m-1)\) colour states are exactly

\[
L_A=\{\infty\}\cup\pi^{-1}(A),
\qquad A\in\binom{\mathbb Z_{2a+1}}a,                    \tag{1}
\]

and the shortened rank-\((m+1)\) states are exactly

\[
U_B=\pi^{-1}(B),
\qquad B\in\binom{\mathbb Z_{2a+1}}{a+1}.                \tag{2}
\]

Complementation \(B\mapsto\mathbb Z_{2a+1}\setminus B\) identifies the
upper bank with a second copy of the lower bank.  Translation orbits in
either bank are free orbits of \(\mathbb Z_{2a+1}\), and the number of
physical full-rotation orbits on each side is

\[
\frac1{2a+1}\binom{2a+1}a
  =\frac1{a+1}\binom{2a}a
  =\operatorname{Cat}_a.                                \tag{3}
\]

#### Proof

The period-three classification in
`MATH_APPENDIX_CATALAN_FULL_ROTATION_STABILIZERS_AND_VOLTAGE_20260731.md`
says that a shortened lower state contains \(\infty\) and its finite part
is a union of \((m-2)/3=a\) cosets of \(K_3\).  This is exactly (1).
The complementary statement gives (2).  Translation descends to the
regular translation action on \(\mathbb Z_{2a+1}\).  Its action on
\(a\)-sets is free because \(\gcd(a,2a+1)=1\), so orbit division gives
(3). \(\square\)

Thus the obstruction at parameter \(m=3a+2\) is indexed by the same
Catalan necklace set that governs the smaller odd ground set \(2a+1\).

## 2. Exact exceptional-bank contribution to broken edge-orbits

Let \(\mathcal J\) be the Johnson graph on rank-\(m\) subsets of \(\Omega\).
For an edge \(e=XY\), write

\[
\ell(e)=X\cap Y,\qquad u(e)=X\cup Y
\]

for its lower and upper colours.  Every Johnson-edge orbit under
\(\mathbb Z_q\) is free.  Indeed, each rank-\(m\) endpoint is free because
its finite part has size \(m\) or \(m-1\), both coprime to \(q\).  An element
stabilizing an unordered edge cannot swap its endpoints, since
\(\mathbb Z_q\) has odd order, and hence must fix both.

Call a physical edge orbit *partial* in an edge set \(F\) when

\[
0<|F\cap\operatorname{Orb}(e)|<q.
\]

### Theorem 2 (two-sided filter lower bound)

If \(F\) hits every rank-\((m-1)\) lower colour exactly once and every
rank-\((m+1)\) upper colour exactly once, then \(F\) contains at least

\[
2\operatorname{Cat}_a                                  \tag{4}
\]

partial \(\mathbb Z_q\)-edge orbits:

* at least \(\operatorname{Cat}_a\) whose lower-colour orbit is shortened;
* at least \(\operatorname{Cat}_a\) whose upper-colour orbit is shortened.

No one edge orbit can count toward both families.

#### Proof

Fix one shortened lower-colour orbit \(\mathcal C\).  It has \(q/3\)
physical colours.  A free edge orbit mapping to \(\mathcal C\) has \(q\)
edges, and the colour map is three-to-one.  If every contributing edge
orbit were either wholly selected or wholly absent, every colour of
\(\mathcal C\) would have selected load divisible by three, not one.
At least one contributing edge orbit is partial.  Different colour orbits
require different edge orbits.  Theorem 1 gives
\(\operatorname{Cat}_a\) shortened lower orbits, proving the first bound.
The upper bound is identical.

A shortened lower colour contains \(\infty\), while a shortened upper
colour avoids \(\infty\).  Since \(\ell(e)\subset u(e)\), no Johnson edge
can have both kinds of exceptional colour.  Hence the two collections of
partial edge orbits are disjoint, and their bounds add. \(\square\)

The bound is an exact symmetry-breaking requirement.  It does not assume
that the remainder of \(F\) is invariant, only that full versus partial
orbit occupancy is measured under the full rotation action.  It is not in
general the exact global minimum, because the nonexceptional edges can force
additional partial orbits.

### Corollary 2.1 (global orbit-size congruence)

Put

\[
E=\binom{2a+1}a=\frac q3\operatorname{Cat}_a,
\qquad
R=\binom{2m}{m-1}.
\]

If \(3\nmid\operatorname{Cat}_a\), then every \(F\) in Theorem 2 has at
least

\[
2\operatorname{Cat}_a+1.                               \tag{5}
\]

partial full-rotation edge-orbits.  Moreover, at least one of the additional
partial orbits has neither a shortened lower-colour orbit nor a shortened
upper-colour orbit.

Indeed, there are \(E\) exceptional physical colours on either shore.  All
other lower colours lie in free \(q\)-orbits, so

\[
q\mid R-E.                                              \tag{6}
\]

Suppose there were exactly \(2\operatorname{Cat}_a\) partial edge-orbits.
Theorem 2 then forces exactly one above each exceptional colour orbit.  Such
an orbit contains exactly \(q/3\) selected edges, one over each physical
colour, so the exceptional lower and upper families together contain exactly
\(2E\) selected edges.  Every remaining selected edge-orbit would be full;
since \(|F|=R\), this would give

\[
q\mid R-2E.                                             \tag{7}
\]

Subtracting (7) from (6) gives \(q\mid E\), equivalently
\(3\mid\operatorname{Cat}_a\), a contradiction.  Thus an additional
partial orbit is necessary.  In fact, if no partial orbit had both colour
orbits nonexceptional, all \(R-2E\) remaining selected edges would again be
a union of full edge-orbits, giving the same contradiction (7).  No
attainment claim is made when \(3\mid\operatorname{Cat}_a\).

## 3. Exact section counts at the clean symmetry scale

For a fixed exceptional colour orbit \(\mathcal C\), any incident free edge
orbit projects three-to-one onto \(\mathcal C\).  Selecting exactly one edge
above each of its \(q/3\) physical colours is therefore a section of a
three-sheeted map.  Inside one fixed free edge orbit there are

\[
3^{q/3}                                                  \tag{8}
\]

arbitrary sections; without an equivariance hypothesis they are not just
three global phases.

Now write

\[
s=3^{v_3(q)},\qquad h=q/s,\qquad
H=\langle s\rangle\cong\mathbb Z_h.
\]

Since \(H\cap K_3=1\), \(H\) acts freely on \(\mathcal C\).  The free full
edge orbit splits into \(s\) \(H\)-edge-orbits, while \(\mathcal C\) splits
into \(s/3\) \(H\)-colour-orbits.  Each \(H\)-edge-orbit maps bijectively
to one \(H\)-colour-orbit, and exactly three \(H\)-edge-orbits map to each
one.  Consequently the number of \(H\)-invariant sections inside the fixed
full edge orbit is exactly

\[
3^{s/3}.                                                 \tag{9}
\]

The residual group \(\mathbb Z_q/H\cong\mathbb Z_s\) acts freely on these
sections.  To see this, identify a section with a transversal of the cosets
of the unique order-three subgroup in \(\mathbb Z_s\).  Every nontrivial
subgroup of the cyclic \(3\)-group contains that order-three subgroup, but
invariance under it would make the transversal a union of three-element
fibres.  Hence there are

\[
\frac{3^{s/3}}s                                          \tag{10}
\]

residual cyclic orbits of \(H\)-invariant sections.

When \(v_3(q)=1\), \(s=3\) and the cyclic group splits as

\[
\mathbb Z_q\cong K_3\times\mathbb Z_{2a+1}.
\]

The free edge orbit decomposes into three
\(\mathbb Z_{2a+1}\)-edge-orbits, and each one separately covers every
colour of \(\mathcal C\) once.  Thus an
\(H=\mathbb Z_{2a+1}\)-invariant minimal filter is exactly one of three
constant phases.  When \(v_3(q)>1\), an \(H\)-invariant filter is instead a
phase word of length \(s/3\), with three choices at every position.  The
\(s\) sectors are the \(H\)-edge-orbits carrying that word; they are not a
proved iteration of one constant phase down the three-primary tower.

## 4. A sharp complement-paired filter construction

The lower bound of Theorem 2 is attained at the exceptional-palette and
middle-vertex-matching level.

### Theorem 3 (sharp paired filters when \(v_3(q)=1\))

Assume \(a\ge1\) and \(v_3(q)=1\).  Identify

\[
\mathbb Z_q\cong\mathbb Z_{2a+1}\times\mathbb Z_3
\]

by the Chinese remainder theorem.  There is a
\(\mathbb Z_{2a+1}\)-invariant matching of Johnson edges consisting of
exactly \(2\operatorname{Cat}_a\) clean-subgroup edge-orbits such that:

1. every exceptional lower colour occurs exactly once;
2. every exceptional upper colour occurs exactly once;
3. all lower colours and all upper colours of the selected edges are
   separately distinct, so the edges form a partial matching in the
   lower--upper diamond containment graph;
4. all middle endpoints of all selected edges are distinct;
5. the upper-filter edge paired with a lower-filter edge is its setwise
   complement; and
6. each clean-subgroup orbit occupies one third of one free full-rotation
   edge orbit.

Thus the \(2\operatorname{Cat}_a\) partial-orbit floor is sharp before the
nonexceptional palettes and global topology are imposed.

#### Construction and proof

For each translation orbit of
\(A\in\binom{\mathbb Z_{2a+1}}a\), choose one representative \(A\).  Put
\(B=\mathbb Z_{2a+1}\setminus A\), and choose distinct \(b,c\in B\).  Let

\[
\begin{aligned}
L_A&=\{\infty\}\cup(A\times\mathbb Z_3),\\
U_B&=B\times\mathbb Z_3,\\
x&=(b,0),\qquad y=(c,0).
\end{aligned}
\]

Select the lower-filter edge

\[
e_A^-=\{L_A\cup\{x\},\,L_A\cup\{y\}\}                 \tag{11}
\]

and the complementary upper-filter edge

\[
e_A^+=\{U_B\setminus\{x\},\,U_B\setminus\{y\}\}.       \tag{12}
\]

The intersection colour of (11) is \(L_A\), while the union colour of (12)
is \(U_B\).  Moreover the two endpoints in (12) are precisely the
complements of the two endpoints in (11).

Take the complete \(\mathbb Z_{2a+1}\)-translation orbits of (11) and (12).
The \(A\)-action is free, so (11) covers every lower colour in its exceptional
full-rotation orbit exactly once; (12) does the same for the complementary
upper orbit.  Varying the \(\operatorname{Cat}_a\) necklace representatives
covers both exceptional banks exactly.

The nonexceptional upper colour of (11) consists of the full \(A\)-cosets,
\(\infty\), and one point in each of two outside cosets; this data recovers
the translated \(A,b,c\).  Dually, the nonexceptional lower colour of (12)
recovers \(B,b,c\).  Hence these opposite-shore colours are also distinct.
Together with the disjoint exceptional banks, the chosen diamonds form a
partial matching in the lower--upper containment graph.

It remains to check middle-endpoint collisions.  From an endpoint containing
\(\infty\), recover \(A\) as the set of finite cosets appearing with all
three phases; the endpoint has exactly one additional point outside those
cosets.  Hence two lower-filter endpoints agree only when their necklace,
translation and choice \(x\) versus \(y\) agree.  Upper-filter endpoints are
their distinct complements, and no lower endpoint equals an upper endpoint
because only the former contains \(\infty\).  All endpoints are therefore
distinct.

Finally, translating by the order-three factor changes the common phase of
\(x,y\) and produces the other two clean-subgroup edge-orbits above the same
exceptional colour orbit.  Selecting phase zero occupies exactly one of
the three, proving Item 6. \(\square\)

For \(a=0\), the same statement is a direct finite base case: choose two of
the three finite phases outside \(\{\infty\}\), together with the
complementary edge.

When \(v_3(q)>1\), Section 3 still gives the exact \(H\)-invariant phase-word
space, but the CRT construction above does not recurse verbatim: the quotient
still has nontrivial three-primary part.  Constructing complement-paired
phase words with the same collision-free properties is an additional
coupling theorem not claimed here.

## 5. Calibration

The first values are:

\[
\begin{array}{c|c|c|c|c|c}
m&q&a&\text{exceptional orbits per side}&
  \text{exceptional-bank floor}&\text{global lower bound}\\ \hline
2&3&0&1&2&3\\
5&9&1&1&2&3\\
8&15&2&2&4&5\\
11&21&3&5&10&11\\
14&27&4&14&28&29.
\end{array}
\]

At \(m=8\), the numbers \(4\) and \(5\) in the table are strictly
palette-level lower bounds for an edge set \(F\) satisfying Theorem 2.  They
do not identify literal carrier seams or defects in the authenticated
\(k=16\) lineage, and they do not assert that its compiler realizes
\(H\)-invariant phase filters.  In that lineage only one changed lower colour
is shortened and no changed upper colour is shortened; the residual sectors
interlace within each strict spiral, and the compiler itself breaks \(H\).
Thus no “four-filter” physical interpretation follows from this theorem.

## 6. Construction target

The composite-order gate is no longer an unspecified failure of
equivariance.  It is:

1. install the complement-paired exceptional matching of Theorem 3 when
   \(v_3(q)=1\), and construct compatible phase-word filters otherwise;
2. extend its used middle endpoints through the nonexceptional
   \(\mathbb Z_h\)-quotient matching;
3. couple the \(s/3\)-position phase words to all ordinary partial orbits;
4. retain path-forest topology and unit voltage.

Proving that extension theorem, recursively in \(a\), would close the
3-primary sector braid.  The current note solves the exceptional palettes
with collision-free middle endpoints, but not their simultaneous extension
to a spanning two-sided-rainbow forest.
