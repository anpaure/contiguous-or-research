# Gate C: the all-pairing coherent-tour orbit

**Status (2026-08-22).**  All enumerative assertions and implications below
are proved.  The all-pairing construction gives an exact regular fractional
factor by FIFO-closed tours and its complete pair-codegree profile can be
computed.  Its maximum normalized codegree is

\[
 {b^2-5\over 2b^2(b-1)}\sim {1\over2b}.
\]

This does **not** prove an integral near-factor: the tour size is
\(b(b-1)\), so the fixed-uniformity Pippenger--Spencer theorem is not
uniformly applicable.  The growing-uniformity counterexample recalled in
Section 5 shows that regularity and this codegree estimate alone cannot
justify the desired matching.  The positive result nevertheless removes
all ambiguity about the proposed hypergraph and isolates the remaining
task as a structured orbit-packing theorem rather than a FIFO seam problem.

Throughout, \(b\ge5\) is odd,

\[
 \Omega=\mathbb Z_b\times\mathbb F_2,
 \qquad P_h=\{h^0,h^1\},
 \qquad \mathcal V={\Omega\choose b},
 \qquad W=|\mathcal V|={2b\choose b}.
\]

## 1. One coherent tour and its distinct internal targets

Take the directed cyclic coordinate order
\(0,1,\ldots,b-1\), and initially select \(h^0\) from every pair
\(P_h\).  At stage \(t\), the pair \(P_t\) is special.  The FIFO packet
keeps its selected member, flips the selected member of every nonspecial
pair in cyclic order, and rotates the coordinate queue by one place.  After
all \(b\) stages, every coordinate has been nonspecial \(b-1\) times.
Because \(b-1\) is even, both the ordered queue and all bits return to their
initial values.  Thus this is a closed FIFO cycle of \(b\) packets.

For distinct \(t,i\in\mathbb Z_b\), let \(T_{t,i}\) be the internal
middle window at the stage with empty pair \(P_t\) and doubled pair
\(P_i\).  Regard \(0,\ldots,b-1\) as integer representatives.  A direct
record of the queue gives

\[
 T_{t,i}=P_i\cup
 \{h^{\chi_{t,i}(h)}:h\notin\{t,i\}\},                 \tag{1.1}
\]
\[
 \boxed{\quad
 \chi_{t,i}(h)=t+\mathbf1_{(h-i)(t-i)>0}\pmod2.
 \quad}                                                  \tag{1.2}
\]

Indeed, before stage \(t\) the selected bit at coordinate \(h\) is

\[
 s_t(h)=t+\mathbf1_{h<t}\pmod2,                           \tag{1.3}
\]

since each of the first \(t\) packets flips \(h\), except the packet at
which \(h\) itself was special.  Before doubling \(P_i\), precisely the
coordinates in the open directed arc from \(t\) to \(i\) have been
flipped once more.  Combining that arc indicator with (1.3) gives (1.2).

Each \(T_{t,i}\) has exactly one empty pair, namely \(P_t\), and exactly
one doubled pair, namely \(P_i\).  Therefore the ordered pair \((t,i)\)
is recoverable from the set, and

\[
 K:=\{T_{t,i}:t\ne i\},\qquad |K|=q:=b(b-1),              \tag{1.4}
\]

has no repeated vertex.  This verifies the first point that is easy to
miss in the all-pairing proposal.

Every perfect pairing of \(\Omega\), rooted directed cyclic listing
\((p_0,\ldots,p_{b-1})\) of its pairs, and initial transversal state
produces a permutation image of \(K\), and every permutation image occurs.
A tour label is the equivalence class under the \(b\) phase shifts: move
the root from \(p_0\) to \(p_s\) and transport the bit state through the
first \(s\) packets.  This action is free because the rooted pair listing
changes.  Hence the number of parameter labels is

\[
 |\mathcal E_{\rm lab}|
 ={(2b)!\over2^b b!}{b!2^b\over b}
 ={(2b)!\over b}.                                         \tag{1.5}
\]

We initially retain these parameter labels, so
\(\mathcal H_b^{\rm lab}=(\mathcal V,\mathcal E_{\rm lab})\) is an
edge-labelled hypergraph and may have parallel supports.  Section 4 treats
that issue exactly.

## 2. Complete internal Johnson-distance census

For \(0\le d\le b\), put

\[
 M_d=|\{(A,B)\in K^2:|A\setminus B|=d\}|.                 \tag{2.1}
\]

The following table is a complete audit of the ordered pairs in (2.1).
In it the labels of the two targets are \((t,i)\) and \((u,j)\); entries
not displayed contribute zero.

\[
\begin{array}{c|c|c}
\text{relation of the labels}&\text{distance }d&
 \text{number of ordered target pairs}\ \\ \hline
(t,i)=(u,j)&0&b(b-1)\\
t=u,\ i\ne j&1\le d\le b-2&2b(b-1-d)\\
i=j,\ t\ne u&1&b(b-1)(b-3)/2\\
i=j,\ t\ne u&b-2&b(b-1)^2/2\\
(u,j)=(i,t)&d\in\{2,4,\ldots,b-1\}&2b\\
\text{exactly one of }t=j,\ i=u&2\le d\le b-1&2b(b-1)\\
|\{t,i,u,j\}|=4&2\le d\le b-2&
b\{b^2-4b+3+4\lfloor d/2\rfloor\}.
\end{array}                                                \tag{2.2}
\]

Here is a self-contained verification of the table.  At a coordinate
which is split in both targets, its contribution to twice the Johnson
distance is zero or two according as the two values of \(\chi\) agree or
disagree.  An empty--split or doubled--split comparison contributes one;
an empty--doubled comparison contributes two.  Substitute (1.2), fix the
first empty coordinate using the cyclic phase automorphism (coordinate
translation together with its forced within-pair bit relabellings), and
list the cyclic gaps between the exceptional coordinates.

For a common empty coordinate, the two doubled coordinates occupy positions
\(r,s\in\{1,\ldots,b-1\}\) in the resulting linear order and the distance
is \(|r-s|\).  This gives \(2b(b-1-d)\).  For a common doubled coordinate,
the parity in (1.2) leaves only distances \(1\) and \(b-2\); respectively
\((b-1)(b-3)/2\) and \((b-1)^2/2\) ordered choices remain after the
doubled coordinate is fixed.  A reversed ordered pair has every even
distance from \(2\) through \(b-1\), with two choices per fixed first
empty coordinate.  With exactly one crossed role, every distance from
\(2\) through \(b-1\) has \(2(b-1)\) choices per fixed first empty.
Finally suppose the four exceptional coordinates are distinct.  Fix the
first empty coordinate at \(t=0\), write their other three integer
positions as \(1\le x<y<z\le b-1\), and use \(I,U,J\) for the roles
first-double, second-empty, second-double.  Substitution in (1.2) gives
the following six-case audit; the two entries are for \(U\) even and \(U\)
odd, respectively:

\[
\begin{array}{c|c}
\text{role word at }x,y,z&d(U\text{ even})\,/\,d(U\text{ odd})\\ \hline
IUJ&z-x\,/\,(b+x-z)\\
IJU&(b+x-y-1)\,/\,(1-x+y)\\
UIJ&(1-y+z)\,/\,(b-1+y-z)\\
UJI&(1-y+z)\,/\,(b-1+y-z)\\
JIU&(b+x-y-1)\,/\,(1-x+y)\\
JUI&(b+x-z)\,/\,(z-x).
\end{array}                                                \tag{2.3}
\]

For a fixed \(d\), solve the displayed linear difference in each row,
sum the remaining free position over its integer interval, and retain the
required parity of the position carrying \(U\).  Pairing the first and
last rows, the second and fifth, and the third and fourth cancels the
endpoint floors.  The resulting number for fixed \(t=0\) is

\[
 b^2-4b+3+4\lfloor d/2\rfloor .                           \tag{2.4}
\]

Restoring the \(b\) choices of the first empty coordinate gives

\[
 b\{b^2-4b+3+4\lfloor d/2\rfloor\}                       \tag{2.5}
\]

for each \(2\le d\le b-2\).

As independent exhaustion checks, the five nonidentity relation classes
in (2.2) have
row sums

\[
 q(b-2),\quad q(b-2),\quad q,\quad2q(b-2),\quad
 q(b-2)(b-3),                                             \tag{2.6}
\]

where the two common-double entries form one row.  Their sum is
\(q(q-1)\), so no ordered pair is omitted or counted twice.  Summing the
columns of (2.2) gives

\[
\boxed{
\begin{aligned}
 M_0&=b(b-1),\\
 M_1&={b(b^2-5)\over2},\\
 M_d&=b(b^2+1),&&2\le d\le b-3,\ d\text{ even},\\
 M_d&=b(b^2-3),&&3\le d\le b-4,\ d\text{ odd},\\
 M_{b-2}&={b(b+1)(3b-5)\over2},\\
 M_{b-1}&=2b^2,\\
 M_b&=0.
\end{aligned}}                                             \tag{2.7}
\]

Empty index ranges in (2.7) are simply omitted.  The formulas sum to
\(q^2\), as they must.

## 3. Exact regularity and maximum pair-codegree

The symmetric group on \(\Omega\) is transitive on middle vertices and on
ordered pairs of middle vertices at every Johnson distance.  Double-counting
edge--vertex incidences in (1.5) gives the exact labelled degree

\[
 \boxed{D_{\rm lab}
 ={ |\mathcal E_{\rm lab}|q\over W}
 =(b-1)(b!)^2.}                                           \tag{3.1}
\]

There are \(W{b\choose d}^2\) ordered ambient vertex pairs at distance
\(d\).  Counting a label together with an ordered internal pair in its
support therefore gives

\[
 \lambda_d^{\rm lab}W{b\choose d}^2
 =|\mathcal E_{\rm lab}|M_d.
\]

After division by (3.1),

\[
 \boxed{
 {\lambda_d^{\rm lab}\over D_{\rm lab}}
 ={M_d\over b(b-1){b\choose d}^2}.}                        \tag{3.2}
\]

For \(2\le d\le b-2\), (2.7) gives
\(M_d\le M_{b-2}\), while
\({b\choose d}\ge {b\choose2}\).  Hence the corresponding value in
(3.2) is at most

\[
 {2(b+1)(3b-5)\over b^2(b-1)^3}
 <{b^2-5\over2b^2(b-1)},                                  \tag{3.2a}
\]

where the strict inequality is equivalent to
\(4(b+1)(3b-5)< (b^2-5)(b-1)^2\).  The right side minus the
left side is
\(b^4-2b^3-16b^2+18b+15\), which is positive at \(b=5\) and
has positive derivative for every \(b\ge5\).  At \(d=b-1\), the value
is \(2/[b(b-1)]\), which ties the
\(d=1\) value when \(b=5\) and is smaller for \(b\ge7\).  Thus

\[
 \boxed{
 {\Delta_2(\mathcal H_b^{\rm lab})\over D_{\rm lab}}
 ={b^2-5\over2b^2(b-1)}
 ={1\over2b}+O(b^{-2}).}                                  \tag{3.3}
\]

This is the strongest possible maximum-codegree estimate for this orbit:
it is an equality, not only an upper bound.

## 4. Parallel parameterizations and the simple orbit

Reversing the entire cyclic FIFO word preserves its collection of
length-\(b\) windows as sets.  It reverses the cyclic pair order and changes
the displayed initial state.  Consequently the two directed orientations
give the same support; the parameter-labelled hypergraph is not simple.

There is no ambiguity in the enumerative conclusion.  All supports form
one \(S_{2b}\)-orbit.  If \(\mu_b\) is their common label multiplicity,
then collapsing parallel labels divides every degree and every codegree by
the same \(\mu_b\).  Hence the simple orbit is exactly regular with

\[
 D_{\rm simp}={(b-1)(b!)^2\over\mu_b},\qquad
 \lambda_{d,\rm simp}={\lambda_d^{\rm lab}\over\mu_b},     \tag{4.1}
\]

and (3.2)--(3.3) remain unchanged.  In particular, matching questions are
identical for the labelled and simple versions: parallel copies can never
both occur in a matching.

The phase rotations have already been quotiented in (1.5), while reversal
shows \(\mu_b\ge2\).  Finite exhaustive checks for \(b=3,5\) show that
reversal is the only duplication among orders and states which retain the
same pairing.  This does not exclude a support representation through a
different pairing, and no use of the unproved all-\(b\) equality
\(\mu_b=2\) is made anywhere in this note.

## 5. Why this is not yet a Pippenger--Spencer matching theorem

The edge size is

\[
 q=b(b-1)\longrightarrow\infty.                            \tag{5.1}
\]

Pippenger--Spencer gives a near-perfect matching from asymptotic regularity
and vanishing normalized codegree when the uniformity is fixed.  Its error
parameters are not uniform in an edge size tending to infinity.  Thus
(3.3) cannot be inserted into that theorem while simultaneously taking
\(b\to\infty\).

This is not a technical quibble.  For growing \(k\), take \(k\) independent
equipartitions of a set of size \(LD\) into \(L\) blocks of size \(D\).
Make the blocks the hypergraph vertices and, for each ground point, take the
\(k\)-edge consisting of its containing blocks.  The hypergraph is exactly
\(D\)-regular.  With positive probability, different partitions have
block intersections at most two, so \(\Delta_2\le2\).  On the other hand,
when

\[
 k\ge64\log(2eDk),
\]

a first-moment calculation for common partial transversals shows that every
matching covers only
\(O(\log(Dk)/k)=o(1)\) of the vertices.  Indeed, for
\(s=\lceil16L\log(2eDk)/k\rceil\), the probability that a fixed \(s\)-set
meets distinct blocks in one partition is at most
\(\exp\{-s(s-1)/(4L)\}\); raising this to the \(k\)-th power and union
bounding over the \({LD\choose s}\) choices tends to zero.

For the present parameters, \(k\asymp b^2\) and
\(\log D_{\rm lab}=\Theta(b\log b)=o(k)\), exactly the range in which this
generic obstruction exists.  It does not disprove a matching in the
coherent-tour orbit.  It proves that the orbit geometry, not the scalar
statistics (3.1) and (3.3), must supply the missing argument.

## 6. Exact fractional consequences and adjacent-rank extension

Giving every labelled tour weight \(1/D_{\rm lab}\) is an exact fractional
perfect matching of the middle layer.  Thus the fractional obstruction is
completely closed.

Write the consecutive middle windows of one packet as
\(C_0,C_1,\ldots,C_b\), with \(C_0,C_b\) its boundaries.  For the
ordered internal window \(C_i\), define its designated adjacent tokens by

\[
 L_i=C_{i-1}\cap C_i,\qquad U_i=C_i\cup C_{i+1}
 \qquad(1\le i\le b-1).                                  \tag{6.0}
\]

These are exactly the literal length-\((b-1)\) and length-\((b+1)\)
windows at the same start.  Within one coherent tour, the \(q\) lower windows
are distinct: the empty pair determines the packet, and within that packet
they are the distinct vertices of an antipodal cube path.  The \(q\) upper
windows are also distinct: an internal upper window is identified by its
empty pair and two consecutive doubled pairs, while the packet-end upper
window has no empty pair and one doubled pair.  These signatures separate
all cases.

Let \(D_-\) and \(D_+\) denote labelled occurrence-degrees on the ranks
\(b-1\) and \(b+1\).  Orbit symmetry and incidence counting give exactly

\[
 D_-=D_+
 ={ |\mathcal E_{\rm lab}|q\over{2b\choose b-1}}
 =(b-1)(b-1)!(b+1)!.                                    \tag{6.1}
\]

Under the middle-normalized fractional weight \(1/D_{\rm lab}\), every
adjacent target therefore has load

\[
 {D_-\over D_{\rm lab}}={D_+\over D_{\rm lab}}
 ={b+1\over b}=1+O(b^{-1}).                              \tag{6.2}
\]

This is an exact simultaneous fractional middle/lower/upper **load
profile**, with only the asymptotically negligible adjacent excess forced
by the different layer sizes.  If instead every tour has weight
\(1/D_-\), it is an exact fractional factor on both adjacent ranks and
has middle load \(b/(b+1)\).  Equivalently, one may form a three-partite
augmented tour hypergraph whose edge contains the \(q\) distinct tokens in
each of these three ranks.  A matching in that augmented hypergraph which
saturates the smaller adjacent layers would cover a
\(b/(b+1)=1-O(1/b)\) fraction of the middle layer and would settle the
adjacent literal-coverage interface.  No such integral matching is proved
here; middle-disjoint tours can still collide at lower or upper tokens.

There is no hereditary extension to arbitrary residual middle families.
For a fixed ground point \(a\), the star

\[
 \mathcal U_a=\{C\in\mathcal V:a\in C\},\qquad
 |\mathcal U_a|=W/2,                                      \tag{6.3}
\]

contains no tour edge: at the packet whose special pair contains \(a\),
all \(b-1\) internal targets omit that entire pair.  Its complementary
half also contains no tour edge: at any stage whose special pair differs
from the pair containing \(a\), the unique target which doubles the latter
pair contains \(a\).
Thus even a density-\(1/2\) residual can have induced tour degree zero.
Any recursive use must prove structural pseudorandomness of the reachable
residuals; density alone is insufficient.

Finally, adding the \(b\) packet-boundary transversals to \(K\) gives a
full closed-cycle support \(K^+\) of \(b^2\) distinct middle windows.  Two
different boundary states cannot agree: between their stages, coordinates
which have and have not yet been special have respectively been flipped
numbers of opposite parity.  A boundary is a transversal, whereas an
internal target has an empty and a doubled pair, so the two classes are
disjoint.  The labelled orbit of \(K^+\) has degree \(b(b!)^2\).

For completeness, the ordered boundary--boundary census is \(2b\) at
every even distance \(d=2,4,\ldots,b-1\), zero at positive odd distance,
and \(b\) at distance zero.  In one direction, boundary--internal pairs
number \(b(b+1)\) at every odd \(1\le d\le b-2\), and \(b(b-1)\) at
every even \(2\le d\le b-1\).  These statements follow by fixing the
boundary stage in (1.3): the internal empty coordinate and the two
parities of its directed separation give the displayed two constant
counts.  Adding both cross directions and the boundary--boundary census
to (2.7) gives

\[
\begin{aligned}
 M^+_0&=b^2,\\
 M^+_1&={b(b^2+4b-1)\over2},\\
 M^+_d&=b(b+1)^2 &&(2\le d\le b-3,\ d\text{ even}),\\
 M^+_d&=b(b^2+2b-1)&&(3\le d\le b-4,\ d\text{ odd}),\\
 M^+_{b-2}&={b(b+1)(3b-1)\over2},\\
 M^+_{b-1}&=4b^2,\qquad M^+_b=0.                         \tag{6.4}
\end{aligned}
\]

Consequently its maximum normalized pair-codegree is still attained at
distance one and equals

\[
 {b^2+4b-1\over2b^3}= {1\over2b}+O(b^{-2}).               \tag{6.5}
\]

This removes the negligible boundary-occurrence bookkeeping if a matching
can be proved, but it does not improve the growing-rank matching issue.

## 7. Exact implication for Gate C

Assume, as an additional theorem not proved here, that the simple tour
orbit has a matching covering \((1-o(1))W\) middle vertices.  It uses at
most

\[
 {W\over b(b-1)}                                         \tag{7.1}
\]

closed coherent tours.  There are no FIFO seams inside a tour.  Linearize
each cyclic word at one point, concatenate the resulting words, and mark
unusable every start whose length lies in \([b-H,b+H]\) and whose window
crosses a join.  There are fewer than \(2(b+H)\) such starts per join, so
this operation costs \(O(b+H)\) positions per tour.  The \(b\) packet
boundaries per tour contribute at most

\[
 O\!\left({(b+H)W\over b(b-1)}\right)=o(W),
 \qquad H=o(b).                                           \tag{7.2}
\]

Thus such a matching would close the middle-coverage and seam-cost parts
of Gate C.

It would **not** by itself close adjacent literal coverage, because tokens
from different middle-disjoint tours may coincide.  Section 6 gives the
exact augmented formulation needed for that.  Nor does it give clean,
near-surjective literal windows at every offset \(1\le h\le H\); those
colored/off-middle quotas remain open.  The present theorem therefore
closes exact regularity, fractional feasibility, duplicate bookkeeping,
the complete pair-codegree calculation, and the FIFO seam implication,
but not the structured integral matching or the all-offset compiler.

## 8. Finite audit

The companion checker

`scratch/verify_gate_c_all_pairing_coherent_tour_orbit_20260822.py`

constructs (1.1) directly for every odd \(5\le b\le31\), verifies target
distinctness, the full relation-class table (2.2), the distance census
(2.7), the maximum in (3.3), distinct adjacent tokens and their incidence
counts, and the full-cycle census (6.4)--(6.5).  It also exhausts all cyclic
orders and states for fixed pairings at \(b=3,5\), confirming twofold
reversal duplication within those fixed pairings.  The checker is confirmatory; the
proofs are contained above.
