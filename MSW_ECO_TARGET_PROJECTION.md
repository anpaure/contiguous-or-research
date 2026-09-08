# Exact target projection for MSW peak-insertion children

## 1. Outcome

The path-dependent coordinates in the MSW peak-insertion theorem do not
destroy all shadow provenance.  After passing from the flip order to the
ordinary wreath order, every peak-insertion child is obtained from its
parent wreath by inserting the two new coordinates in two antipodal gaps.
Deleting those coordinates recovers the parent cyclic order exactly.

This gives a complete occurrence-level projection table at every depth.
For a lower child shadow at depth `j>=1`:

* a window containing one inserted coordinate projects to a parent shadow
  at the same depth `j`;
* a window containing no inserted coordinate projects to a parent shadow at
  depth `j-1`;
* no covered lower window contains both inserted coordinates.

The upper table is the complement of this one.

This is the exact local algebra needed by the critical Catalan lift.  It
does **not** by itself prove the defect recurrence.  A missing target has no
owner path, hence no canonical local inserted pair.  Turning the many
possible path-dependent deletions into a bounded-load assignment to old
missing targets is an additional Hall/flow theorem.  Sections 5--7 below
state that theorem precisely and prove that only masks with linearly many
coordinate runs can matter asymptotically.

## 2. Contracting an adjacent pair in an odd flip cycle

Let

\[
 Q=(q_0,q_1,\ldots,q_{N-1}),\qquad N=2m+1,          \tag{2.1}
\]

be a cyclic word of distinct labels.  Its tight wreath order is the
step-two order

\[
 \mathsf T(Q)=(q_0,q_2,q_4,\ldots)                  \tag{2.2}
\]

with indices modulo `N`.  Since `N` is odd, this is one cyclic permutation
of all labels.

Insert two new adjacent labels `p,q` at any cut of `Q`, obtaining a cycle
`Q'` of length `N+2=2m+3`.

### Lemma 1 (step-two contraction)

Deleting `p,q` from `mathsf T(Q')` recovers `mathsf T(Q)`, up to cyclic
rotation.  In `mathsf T(Q')`, the two new labels separate the old labels
into arcs of lengths `m` and `m+1`.

### Proof

Relabel the cut so that `p,q` occupy consecutive cyclic indices `a,a+1`.
Following indices by `+2 modulo N+2`, deleting the two exceptional indices
contracts the two exceptional jumps to the `+2 modulo N` jumps on the old
indices.  Thus the induced cyclic order is (2.2).

The inverse of `2 modulo 2m+3` is `m+2`.  Therefore two consecutive indices
of `Q'` are separated in the step-two order by `m+2` steps in one direction
and `m+1` in the other.  Removing the two endpoints leaves respectively
`m+1` and `m` old labels on the two arcs.  \(\square\)

## 3. Application to every MSW peak insertion

Let `w` be a Dyck word of semilength `m`, and insert a peak `10` at an
arbitrary word gap `g`.  Denote the child by `c=I_g(w)`, the two inserted
coordinate labels by `p_g,q_g`, and the increasing old-coordinate injection
by `iota_g`.

The peak-insertion theorem in `MSW_ECO_INSERTION_AUDIT.md` gives

\[
 \rho(c)=
  (\iota_g(r_1),\ldots,\iota_g(r_a),
    p_g,q_g,
    \iota_g(r_{a+1}),\ldots,\iota_g(r_{2m}))         \tag{3.1}
\]

or the same formula with `p_g,q_g` reversed.  Appending the distinguished
closing coordinate turns the flip words into odd omitted-label cycles.
Lemma 1 therefore proves:

### Theorem 2 (exact wreath-order projection)

For every parent `w` and every insertion gap `g`, deleting the locally
inserted coordinates from the child wreath order gives the parent wreath
order, after the natural injection and a cyclic rotation.  The inserted
coordinates occupy two gaps whose complementary old arcs have lengths `m`
and `m+1`.

The insertion gap need not be the canonical ECO-parent site.  Inserting a
peak at any gap still gives a Dyck child, hence a wreath which occurs in the
MSW factor in dimension `2m+3`.  Different `(w,g)` may produce the same
child root; this causes no problem for a coverage argument, which needs only
one witnessing occurrence.

This theorem also resolves an apparent conflict between the terminal and
primitive root formulas.  The word `1u0` is generally not the literal
endpoint insertion child of the root indexed by `u`; its unique canonical
ECO parent is obtained by deleting its rightmost peak.  Projection must use
that actual parent presentation, not the convenient first-return index `u`.

There is a useful strengthening of the insertion theorem.

### Lemma 2.1 (gap--cut permutation)

Fix `w`.  As the word gap `g` runs through its `2m+1` possible values, the
cut `a` at which the adjacent block is inserted in (3.1) runs through every
one of the `2m+1` cuts of `rho(w)` exactly once.

### Proof

Induct through the first-return decomposition `w=1u0v` used in the proof of
the peak-insertion theorem.  The gaps lying inside the `v` part map, by
induction, bijectively to the cuts of the final block
`|u|+2+rho(v)`.  The gaps between the opening and closing letters around
`u` map, after reverse-complement, bijectively and in reverse order to the
cuts of the block `|u|+2-rho(mu(u))`.  The one remaining gap, before the
first letter of `w`, maps to the cut adjacent to the two outer entries
`|u|+2,1` in the recursion for `rho(w)`.  These three cut families are
disjoint and have respective sizes `|v|+1`, `|u|+1`, and `1`, whose sum is
`2m+1`.  The empty-word basis is immediate.  \(\square\)

Combining Lemmas 1 and 2.1 gives an exact slot-reproduction count.  Fix one
parent interval occurrence of length `m-j`.  Among all gap insertions into
its owner root, it has exactly

\[
                         2(m+1-j)                    \tag{3.2}
\]

one-tag child lifts at depth `j`.  Similarly, a fixed parent occurrence at
depth `j-1` has exactly `2j+1` zero-tag seam lifts at child depth `j`.
These counts are with insertion-presentation multiplicity.  A child root
may have several peak-deletion presentations; passing to the unique
rightmost-peak ECO parent is precisely where the full Catalan ratio replaces
the much larger `2m+1` presentation count.

## 4. The complete interval projection table

Fix a child of a parent on `2m+1` coordinates.  At lower depth `j>=1`, put

\[
                         \ell=m+1-j.                 \tag{4.1}
\]

A child lower shadow is a cyclic interval of length `ell` in the child
wreath order.  Since `ell<=m`, it cannot contain both inserted labels.

### Theorem 3 (local lower table)

The `2m+3` child lower occurrences at depth `j` split as follows.

\[
\begin{array}{c|c|c|c}
\text{tag count}&\text{number}&\text{after deleting }p_g,q_g
  &\text{parent depth}\\ \hline
1&2\ell=2(m+1-j)&\text{interval of length }\ell-1=m-j&j\\
0&2j+1&\text{interval of length }\ell=m+1-j&j-1.
\end{array}                                         \tag{4.2}
\]

More precisely, the one-tag windows are exactly those crossing one of the
two insertion gaps; deleting their tag closes that gap.  The zero-tag
windows are exactly the intervals contained in one of the two old arcs.

### Proof

There are `ell` cyclic length-`ell` intervals containing either fixed tag.
The two families are disjoint because no such interval contains both tags.
This gives the first line of (4.2).

The old arcs have lengths `m` and `m+1`.  Their numbers of contained
length-`ell` intervals are

\[
 (m-\ell+1)+(m+1-\ell+1)=j+(j+1)=2j+1.             \tag{4.3}
\]

Deleting a tag from a crossing interval, or simply deleting the absent tags
from an arc interval, gives the stated parent lengths.  \(\square\)

Complementation gives the upper table.  A child upper occurrence at depth
`j` contains one tag and projects to parent upper depth `j`, or contains both
tags and projects to parent upper depth `j-1`; the respective counts are the
same two lines of (4.2).

In particular, every zero-tag lower seam and every two-tag upper seam in
(4.2) is an **already covered** value.  It must not be charged to the
exceptional term `B_(m,H)`.  At `j=1`, the `3 Cat_m` distinct terminal-child
examples in `CRITICAL_ECO_SEAM_DISTINCTNESS_NO_GO.md` are instances of the
second line.

## 5. Why occurrence projection is not yet defect projection

Let

\[
 \mathcal M_{m,j}^{-},\qquad \mathcal M_{m,j}^{+}    \tag{5.1}
\]

denote the actual missing lower and upper targets at depth `j` of the MSW
factor.  Theorems 2--3 project every **covered occurrence**.  A member of
`mathcal M_(m+1,j)^-` has no owner child and therefore has no distinguished
pair `p_g,q_g`.  It has many possible presentations obtained by deleting
two adjacent word coordinates and closing the coordinate gap.

This is the exact point where a path-local proof can make an invalid jump:

\[
 \text{every child occurrence has an old projection}
 \quad\not\Longrightarrow\quad
 \text{every missing child target has one canonical old hole}.  \tag{5.2}

The required global object is a capacitated deletion graph.

For a fixed band `1<=j<=H`, form a bipartite graph `G_(m,H)` as follows.

* The left vertices are all actual missing child targets
  `M_(m+1,j)^pm`.
* The right vertices are all actual old missing targets
  `M_(m,r)^pm`, with `|r-j|<=1`.
* Join a child target `S` to an old target `T` when some peak-insertion
  presentation deletes its local adjacent pair from `S`, order-preservingly
  relabels the old coordinates, and gives `T`.  The depth shift is determined
  by whether `S` contains zero, one, or two members of the pair, exactly as
  in (4.2) and by complementation.

### Proposition 4 (exact charging-flow reduction)

If all but `B_(m,H)` left vertices can be fractionally assigned to adjacent
right vertices so that every right vertex receives load at most

\[
                         A_m={C_{m+1}\over C_m},      \tag{5.3}
\]

then

\[
 E_{m+1,H}\le A_m E_{m,H}+B_{m,H}.                  \tag{5.4}

Conversely, a targetwise proof of (5.4) by local ECO deletion is precisely
such a flow after its exceptional targets are removed.

This is ordinary capacitated Hall.  For every family `X` of nonexceptional
left vertices it asks for

\[
                         |X|\le A_m|N(X)|.            \tag{5.5}

Thus the critical ECO lemma is not a new factor-construction problem.  It is
an expansion theorem for the actual recursively defined missing-target
families.

## 6. Exact collision of deletion presentations

A one-tag presentation is available at every adjacent coordinate pair on
which the incidence word of a target changes value.  Raw presentations are
not the same as distinct neighbours in the Hall graph: several deletions
can give the same old target.  The collision has an exact form.

For a binary word `u=u_1...u_L`, let `delta_i(u)` delete positions `i,i+1`.

### Lemma 5 (period-two collision law)

For `i<j`,

\[
 \delta_i(u)=\delta_j(u)
 \quad\Longleftrightarrow\quad
 u_t=u_{t+2}\quad(i\le t\le j-1).                  \tag{6.1}
\]

Thus, among one-tag positions, equal deleted parents are exactly the
positions lying in one maximal alternating block.  If

\[
 d_t=u_t\mathbin{\mathsf{xor}}u_{t+1},              \tag{6.2}
\]

then the number of distinct one-tag deleted parents is the number of runs
of ones in `d`.

### Proof

The two deleted words already have the same prefix before `i` and suffix
after `j+1`.  Their middle factors agree exactly when

\[
                     u_{i+2}\cdots u_{j+1}
                     =u_i\cdots u_{j-1},             \tag{6.3}
\]

which is (6.1).  If both deleted pairs are unequal, period two is the same
as alternation throughout the intervening factor.  \(\square\)

### Lemma 6 (few distinct parents are negligible)

For every fixed `eta<1/2`, the number of length-`2m+O(1)` masks with at
most `eta m` distinct one-tag deleted parents is

\[
 2\sum_{s\le\eta m}{2m+O(1)\choose 2s}
 =2^{(2m+O(1))H_2(\eta)+o(m)}=o(C_m).               \tag{6.4}
\]

### Proof

The transition word `d`, together with the first bit of `u`, determines
`u`.  A binary word of length `L-1` having exactly `s` runs of ones is
specified by its `2s` run endpoints, giving `binom(L,2s)` choices.  Sum
over `s`.  Since `eta<1/2`, `H_2(eta)<1`, whereas
`C_m=2^{2m-o(m)}`.  \(\square\)

Consequently a sub-Catalan exceptional family may discard all targets with
sublinear distinct ambient deletion degree.  Every remaining target has
linearly many distinct possible old projections.  This does not prove Hall
expansion: the actual missing-target graph retains only projections landing
in an old missing family, and its cardinality obstruction is recorded in
`MSW_CRITICAL_CARDINALITY_AUDIT.md`.

## 7. The exact remaining mathematical lemma

The remaining assertion is now sharply separated from the seam algebra.

> **Targetwise ECO expansion lemma.**  For
> `H=o(m)`, after deleting `o(C_m)` low-run or boundary targets, the
> capacitated deletion graph `G_(m,H)` satisfies (5.5), with capacity
> `A_m=C_(m+1)/C_m`, on average in `m` if necessary.

The coefficient is critical.  A crude degree argument gives only a constant
near four: an old word has `O(m)` adjacent-pair insertions and a typical new
word has `Theta(m)` deletions.  The exact deficit

\[
                         4-A_m={6\over m+2}           \tag{7.1}
\]

cannot be lost at every dimension, because an `Omega(C_m)` loss would
invalidate the critical theorem.  A successful proof must use the exact
Catalan distribution of insertion sites, not merely maximum degree.

Tiny independent reconstruction through `m=8` suggests that the deletion
graph is extremely redundant at lower depth one: apart from at most two
small-dimensional exceptions, every missing child target has an adjacent
deletion which is an old missing target at depth one or two, and most have
linearly many.  This is evidence only, not an all-dimensional theorem.

The next proof target is therefore (5.5), not another audit of raw seams.
Theorems 2--3 have already removed the seam values themselves from the
exceptional budget.
