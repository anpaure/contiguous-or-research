# Independent audit: PBBS plane-tree rerooting obstruction and Pascal-saddle gate

Date: 2026-07-25

Audited source:
`MATH_ATTACK_K_RPA_PLANE_TREE_REROOTING_OBSTRUCTION_20260725.md`.

Method: pure mathematics only. No web search, computation, finite search, or
solver is used.

## 0. Verdict

**PASS after the four corrections now incorporated in the source.**

The report's proved claims, constants, and implication scopes are correct:

1. the first-deepest-spine sector formula for \(\tau=\phi^2\) and its
   physical cocycle;
2. the ordinary, planted, canonical-corner, and Stanley--Kreweras
   rerooting obstructions;
3. the predecessor-particle/final-root-slot iff criterion;
4. the exact inverse-pruning capacities and capacitated mass transport;
5. the gap-seven normalized congestion constant \(1/18\), including the
   full edge/corner pigeonhole constants \(1/(18d)\) and \(1/(36d)\);
6. the genuine level-three component packing density \(2/9\);
7. the two-dimensional Pascal-saddle Gaussian normalization and the
   coefficient

   \[
      \frac{27\sqrt2}{16\pi A\,4^{z_0}};
   \]

8. the all-slot extension with weight \(4^{-z}\) for
   \(0\le z\le\lceil3\log r\rceil\); and
9. the exact one-way implication from \(\mathrm{RP}_A\) to the averaged
   saddle sparsity conditions.

The report does not prove or disprove \(\mathrm{RP}_A\). It rigorously
closes the natural local unrooted-rerooting charge and identifies the
remaining global, slot-sensitive passage-packing theorem.

The incorporated corrections were:

* the descending \(B\)-range in the spine formula is explicitly empty for
  \(h=1\), preventing a literal duplicate \(B_0\);
* the gap-seven congestion theorem assumes \(H\ge4\), so every five-edge
  interval on a cycle longer than \(H+1\) is nonwrapping;
* the explicit level-three step-two intervals use the corrected edge sets
  \(\{2,4,6,8\}+9j\) and \(\{3,5,7,9\}+9j\); and
* the saddle theorem now states the pointwise asymptotic lower bound, not
  only its liminf consequence. This is what implies the full limit
  \(S_r\to0\), rather than merely \(\liminf S_r=0\).

## 1. Dyck and plane-tree action

Write the first-maximum decomposition as

\[
 D=P1R0S.
\]

The one-step formula gives

\[
 \phi D=\overline R\,1\,\overline S\,0\,\overline P,
\]

whose displayed one is again the first maximum-reaching step. A second
application therefore gives

\[
 \boxed{\tau D=S1P0R.}
\]

The two one-step displacements add to

\[
 |P|+1+|R|+1=N-(|S|+1),
\]

so the physical two-step displacement is exactly \(-(|S|+1)\pmod N\).

For the contour tree, let \(v_0,\ldots,v_h\) be the path to the first
deepest leaf, and let \(A_i,B_i\) be the forests before and after the
spine child at \(v_i\). Then

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1\,
   0B_{h-1}0\cdots0B_1\,0B_0.
\]

The first-deepest condition forces \(A_{h-1}=\varnothing\): every child
of \(v_{h-1}\) is already at maximum depth and is therefore a leaf. The
substitution above yields the displayed sector-transport formula in the
source. Thus each \(A_i\) moves one level away from the root, each
\(B_i\), \(i\ge1\), moves one level toward it, and \(B_0\) crosses the
root seam. Since \(|B_0|=2|E(\mathcal B_0)|\), the cocycle is

\[
 d_0(D)=2|E(\mathcal B_0)|+1.
\]

Finally,

\[
 |P|+1=h+2\sum_{i=0}^{h-1}|E(\mathcal A_i)|,
\]

so the accumulated sector return equation in the report follows directly
from the skew product. The integer winding is nonnegative: the difference
between the positive left side and the final displacement cannot be a
negative multiple of \(N\) of magnitude less than \(N\).

## 2. Shape-change and rerooting obstructions

For

\[
 E_d=(10)^{d-2}1100,
\]

the defect-one affine rule

\[
 \phi E(a,b,c)=E(b-1,c+1,a),
 \qquad
 \tau E(a,b,c)=E(c,a+1,b-1)
\]

gives

\[
 \tau E_d=1(10)^{d-1}0.
\]

The ordinary contour-tree degree multisets are exactly

\[
 \{d-1,2,1^{d-1}\},
 \qquad
 \{d,1^d\}.
\]

Both contain \(d+1\) vertices and have degree sum \(2d\), and they differ
for every \(d\ge3\).

For the all-rank family

\[
 D_r^\star=110100(10)^{r-3},
 \qquad
 \tau D_r^\star=(10)^{r-3}110010,
\]

the degree multisets are

\[
 \{r-2,3,1^{r-1}\},
 \qquad
 \{r-1,2,1^{r-1}\}.
\]

They differ for \(r=3\) and every \(r\ge5\); the exceptional equality of
degree multisets at \(r=4\) is correctly not used. The separate planted
example has degree multisets

\[
 \{4,2,1,1,1,1\},
 \qquad
 \{3,3,1,1,1,1\}.
\]

The explicit \(r=4\) quotient three-cycle also rules out conjugacy to the
canonical next-corner action, whose order divides \(2r=8\), or
\(2(r+1)=10\) after planting.

For the Stanley--Kreweras incidence tree, the maximal-descent convention
indeed gives

\[
 \pi(E(a,b,c))=(a+1,a+b+1)
\]

with all remaining points fixed. If the transposition has cyclic
separation \(s\), direct multiplication gives complementary cycle sizes
\(s,d-s\). Hence the family \(E(0,2,d-3)\) and its \(\tau\)-image have
white-degree multisets

\[
 \{2,d-2\},
 \qquad
 \{1,d-1\},
\]

while their black degrees agree. At \(d=4\) the complete uncolored
degree multisets are

\[
 \{2,2,2,1,1\},
 \qquad
 \{3,2,1,1,1\};
\]

for \(d\ge5\), their maximum degrees differ. The opposite Kreweras
convention merely conjugates the complementary permutation and does not
alter these cycle sizes.

## 3. Predecessor-slot iff and capacities

For \(E=\partial D\in\mathcal D_d\) with \(k\) peaks, inverse leaf
expansion has \(2d+1\) ordered child slots. After removing the one
mandatory new leaf at each old leaf, the free occupancies satisfy

\[
 n_0+\cdots+n_{2d}=r-d-k.
\]

Therefore

\[
 P_r(E)=\binom{r+d-k}{2d}.
\]

The final root slot \(n_0=z\) makes the initial predecessor separation
exactly \(2z+1\). Before \(N\) updates, no particle can make a full
circuit and cyclic particle order cannot change. Thus the next entry into
the initially selected physical edge can only be made by the immediate
predecessor. The three conditions

\[
 \kappa_g=-1,
 \qquad
 \kappa_h=0\text{ for some }0<h<g,
 \qquad
 C_{-1}(g)=2z+1
\]

are consequently necessary and sufficient for the next occurrence at
time \(g\). Fixing \(z\) leaves \(2d\) slots with total
\(r-d-k-z\), giving

\[
 K_r(E,z)=\binom{r+d-k-z-1}{2d-1}.
\]

No earlier-return or completion assumption is hidden in this argument.

Peak deletion semiconjugates \(\tau\), so a parent quotient edge above a
fixed reduced edge is uniquely the reduced edge together with its slot
vector. Edge-disjoint parent intervals therefore use distinct vectors
above every reduced occurrence. This proves

\[
 L_e(\mathcal P)\le P_r(e),
 \qquad
 \sum_eL_e(\mathcal P)=\sum_{I\in\mathcal P}|I|,
 \qquad
 \sum_eP_r(e)=B_r.
\]

Repeated occurrences of a reduced edge cause no problem: multiplicity is
retained, while distinct parent occurrences carry distinct transported
slot vectors.

## 4. Local congestion and component constants

For the gap-seven core \(E_d\),

\[
 P_r(E_d)=\binom{r+1}{2d},
 \qquad
 K_r(E_d,0)=\binom r{2d-1},
\]

so

\[
 \frac{K_r(E_d,0)}{P_r(E_d)}=\frac{2d}{r+1}.
\]

When \(2d-1=r/2+O(1)\), this tends to \(1/2\). A gap-seven interval has
five quotient edges, so its closed conflict neighborhood has at most nine
candidate starts. With \(H\ge4\), every such interval on a cycle longer
than \(H+1\) is nonwrapping. Removing the single global short-cycle set
\(Z_H=\exp(o(r))\) and applying greedy selection gives

\[
 \frac{|\mathcal P_{r,d}|}{P_r(E_d)}
 \ge\frac19\left(\frac12-o(1)\right)
 =\frac1{18}-o(1).
\]

Pigeonhole over the \(d\) edges or \(2d\) corners of the fixed core gives
the exact lower loads

\[
 \left(\frac1{18}-o(1)\right)\frac{P_r(E_d)}d,
 \qquad
 \left(\frac1{36}-o(1)\right)\frac{P_r(E_d)}d.
\]

These are local obstructions only: the fibre has exponential rate
\(\log2\), while \(B_r/N\) has rate \(\log4\).

For the level-three component, the displayed quotient cycle has voltages
\(2,N-3,2\), total \(N+1\). Its lift is one \(3N\)-component, and the
omitted-label formula shows that phases zero and one have gap five. The
chosen interval sets

\[
 \{2,4,6,8\}+9j,
 \qquad
 \{3,5,7,9\}+9j
\]

are pairwise disjoint for
\(0\le j<\lfloor(3N-1)/9\rfloor\). Thus the exact lower count is

\[
 2\left\lfloor\frac{3N-1}{9}\right\rfloor,
\]

whose density among the \(3N\) step-two edges tends to \(2/9\). This
component lies over a short quotient cycle and is correctly excluded from
any claimed global counterexample.

## 5. Two-dimensional Pascal saddle

The exact cell mass is

\[
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
  \binom{r+d-k}{2d}.
\]

Its entropy saddle is \((k/r,d/r)=(1/6,1/2)\). In the Gaussian variables

\[
 u=\frac{k-r/6}{\sqrt r},
 \qquad
 v=\frac{d-r/2}{\sqrt r},
\]

the negative Hessian is

\[
 Q_0=\frac14
 \begin{pmatrix}81&-9\\-9&33\end{pmatrix},
 \qquad
 \det Q_0=162.
\]

The lattice Gaussian prefactor is
\(\sqrt{162}/(2\pi)=9\sqrt2/(2\pi)\), proving

\[
 \frac{\mathsf M_r(d,k)}{B_r}
 =\frac{9\sqrt2}{2\pi r}
   e^{-(81u^2-18uv+33v^2)/8}(1+o(1))
\]

uniformly in every fixed saddle tube.

The exact slot ratio is

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\frac{2d}{r+d-k}
  \prod_{j=0}^{z-1}
   \frac{r-d-k-j}{r+d-k-1-j}.
\]

At the saddle it tends to \((3/4)4^{-z}\). Multiplying the cell
prefactor by \(3/(4\cdot4^{z_0})\), then dividing the variable-length
candidate family by
\(2H+1=(2A+o(1))\sqrt r\), gives exactly

\[
 \frac{27\sqrt2}{16\pi A\,4^{z_0}}.
\]

The global greedy step is valid even when the selected passage varies by
core. Each parent root supplies at most one chosen interval, every interval
has at most \(H+1\) edges, and on a directed cycle it can meet candidates
starting at only \(H\) preceding positions, its own position, and \(H\)
following positions. Different cores have disjoint inverse fibres.
All short parent cycles are removed once, at total cost \(Z_H\), not once
per cell. After multiplication by \(r/[B_r(2H+1)]\), this subtraction is
\(o(1)\).

The corrected pointwise estimate is therefore

\[
 \frac{r\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A\,4^{z_0}}+o(1)\right)
 S_r(a,z_0)-o(1).
\]

This pointwise form, unlike a liminf-only statement, proves the full
necessary limit \(S_r(a,z_0)\to0\) from
\(\overline\nu_H=o(B_r/N)\).

## 6. All-slot extension

For one reduced core, two distinct predecessor passages cannot prescribe
the same exact slot \(z\): Theorem 4.1 would otherwise make every parent
root in that nonempty hyperplane have two different next-return times.
Different exact slots are disjoint coordinate hyperplanes. Hence selecting
one passage for every admissible \((E,z)\) does not double-count parent
starts.

For \(z\le L_r=\lceil3\log r\rceil\), every factor in the exact slot
product is

\[
 \frac14+O\left(r^{-1/2}+\frac{z+1}{r}\right)
\]

uniformly in a fixed saddle tube. Since there are only \(O(\log r)\)
factors, the accumulated relative error is \(1+o(1)\), uniformly over all
these slots. Therefore

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\left(\frac34+o(1)\right)4^{-z}.
\]

The weighted inner sum is bounded by
\(\sum_{z\ge0}4^{-z}=4/3\), so uniform errors remain harmless after
summing. Candidate hyperplanes are disjoint, the global short-cycle set is
again subtracted only once, and the same variable-length greedy argument
applies. This verifies

\[
 \frac{r\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A}+o(1)\right)
 S_r^\ast(a)-o(1).
\]

Thus \(\mathrm{RP}_A\) necessarily forces
\(S_r^\ast(a)\to0\) for every fixed \(a\).

## 7. Final implication scope

The deck inequality is one-way:

\[
 N\overline\nu_H\le\nu_H(P_r).
\]

Therefore physical \(\mathrm{RP}_A\) implies the quotient target
\(\overline\nu_H=o(B_r/N)\), which in turn implies the fixed-slot and
all-slot saddle sparsity conditions. The converse is not claimed.

The gap-seven and level-three examples disprove only uniform local or
hereditary orbitwise charges. Their total Catalan mass is negligible. The
ordinary and incidence-tree examples rule out those natural encodings,
not every artificially decorated object containing the full slot dynamics.
The remaining theorem is genuinely global: it must control the exact
peak- and slot-weighted predecessor-passage packing across different long
parent-rank quotient cycles.
