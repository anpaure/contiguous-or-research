# The lexicographic excursion problem after the rotation-system obstruction

## 1. Verdict

Put

\[
 P_m=[0,m]^4,\qquad V_m=\{v:|v|=2m-1\},\qquad
 Z_m=\{z:|z|=2m\}.
\]

For each `z in Z_m`, join the two lower covers obtained by subtracting
from the first two positive coordinates of `z`.  Orient this edge by moving
one unit from the later of those coordinates to the earlier one.  This is
the lexicographic selected-cover graph `G_m`.

There are two conclusions.

1. The within-one-transition-trail **Lexicographic Excursion Lemma is
   false for every `m>=2`**.  Four targets of rank `2m+1`, supported on
   three cubic vertices, force an inconsistent set of local pairings.
2. The obstruction does not cost a long arm.  Cutting `G_m` into its
   maximal degree-two arms and concatenating those arms in arbitrary
   orientations always gives a word of length `|Z_m|+O(m^2)`.  Hence the
   correct remaining statement is a **virtual-seam arm-ordering lemma**,
   not a rotation-system lemma.  It may repeat `O(m^2)` cut vertices but
   uses every long arm only once.

The second statement below is a precise sufficient construction target.
It is still open.  It is strictly weaker than the refuted statement and is
the smallest formulation that retains the width-plus-surface accounting.

## 2. Directed local structure

Let `p<q` be the first two positive coordinates of `v in V_m`.  Every
incident middle colour is `v+e_i`.  Direct inspection of the selected pair
gives

\[
 \operatorname{outdeg}(v)=p-1+\mathbf 1_{v_p<m},\qquad
 \operatorname{indeg}(v)=q-p-1+\mathbf 1_{v_q<m}.       \tag{2.1}
\]

Here coordinates are numbered `1,2,3,4`.  An outgoing move transfers one
unit from a later positive coordinate to a coordinate at or before `p`.
Consequently

\[
                    \Phi(v)=\sum_{i=1}^4 i v_i             \tag{2.2}
\]

strictly decreases along every oriented edge.  Thus every directed
component is a DAG.

The possible directed types, with their exact multiplicities, are

\[
\begin{array}{c|c}
 (\operatorname{outdeg},\operatorname{indeg})&\#\text{ vertices}\\ \hline
 (3,0),(0,3)&1\text{ each}\\
 (2,1),(1,2)&\binom{m+1}{2}\text{ each}\\
 (2,0),(0,2)&m-1\text{ each}\\
 (1,0),(0,1)&\binom m2\text{ each}\\
 (1,1)&\frac23m(m^2-1).
\end{array}                                               \tag{2.3}
\]

This follows by inserting the six possibilities for `(p,q)` into (2.1)
and counting the remaining bounded compositions.  The entries sum to

\[
                   |V_m|={2\over3}m(m+1)(m+2).             \tag{2.4}
\]

In particular, the graph has

\[
 \binom{m+1}{2}\quad\text{directed sources and the same number of sinks},
                                                               \tag{2.5}
\]

and only

\[
 \#\{v:\deg(v)\ne2\}
   =m(m+1)+2+m(m-1)=2m^2+2                         \tag{2.6}
\]

undirected branch or terminal vertices.  All other choices are forced
degree-two continuations.  This is the precise surface-size kernel behind
the earlier `O(m^2)` statement.

The reverse-greedy facet path for an upper target is directed in this DAG.
At a `(2,1)` vertex it may either continue along the boundary or leave into
a forced arm.  Which turn it needs depends on the target.  The next section
shows that these choices cannot be frozen into one transition system.

## 3. An all-dimensional four-target contradiction

For `m>=2`, define the three cubic lower vertices

\[
 A=(0,m-1,0,m),\quad B=(0,m-1,1,m-1),\quad
 C=(0,m,0,m-1).                                      \tag{3.1}
\]

Use the following middle colours:

\[
\begin{array}{lll}
 x=(0,m-1,1,m),&u=(0,m,0,m),&r=(1,m-1,0,m),\\
 s=(0,m-1,2,m-1),&v=(0,m,1,m-1),&t=(1,m-1,1,m-1),\\
 &&w=(1,m,0,m-1).
\end{array}                                          \tag{3.2}
\]

The incident colour triples are exactly

\[
             A:\{x,u,r\},\qquad B:\{s,v,t\},\qquad
             C:\{u,v,w\}.                            \tag{3.3}
\]

Consider

\[
\begin{aligned}
Y_1&=(0,m,1,m),&Y_2&=(0,m,2,m-1),\\
Y_3&=(1,m,0,m),&Y_4&=(1,m,1,m-1).
\end{aligned}                                        \tag{3.4}
\]

All have rank `2m+1`.  Therefore their allowed middle colours are obtained
simply by subtracting one unit in a positive coordinate.  Inspecting their
induced selected graphs gives the four necessary and sufficient clauses

\[
\begin{array}{ll}
Y_1:&(xu)_A\ \lor\ (uv)_C,\\
Y_2:&(sv)_B,\\
Y_3:&(ur)_A\ \lor\ (uw)_C,\\
Y_4:&(vt)_B\ \lor\ (vw)_C.
\end{array}                                          \tag{3.5}
\]

The notation `(ab)_X` means that the two half-edges of colours `a,b` are
paired through `X`.  For example, below `Y_1` the only useful component is
the colour path

\[
                       x\ --_A\ u\ --_C\ v.          \tag{3.6}
\]

The analogous paths establish every row of (3.5), including necessity.

Now `(sv)_B` excludes `(vt)_B`, so `Y_4` forces `(vw)_C`.  This excludes
both `(uv)_C` and `(uw)_C`.  Hence `Y_1` forces `(xu)_A`, while `Y_3`
forces `(ur)_A`.  A cubic transition can pair `u` with only one of `x,r`,
a contradiction.

Thus no transition system works, for any `m>=2`.  The contradiction is
minimal: deleting any one row of (3.5) makes the other three compatible.
In particular, it identifies the exact missing resource: at least one
cubic vertex must make two incompatible turns available, one of them
virtually across a cut or seam.

## 4. Maximal forced arms

Let

\[
                         K_m=\{v\in V_m:\deg(v)\ne2\}.       \tag{4.1}
\]

Cut `G_m` at every vertex of `K_m`.  The remaining edge pieces are maximal
undirected paths whose internal vertices have degree two.  If a component
has degree two everywhere, cut it once as well.  Call the resulting family
`A_m` the **forced arms**.

The degree-one and degree-three rows of (2.3) give

\[
 \sum_{v\in K_m}\deg(v)
 =m(m-1)+3\bigl(m(m+1)+2\bigr)
 =4m^2+2m+6.                                      \tag{4.2}
\]

Hence the arms having two kernel endpoints number `2m^2+m+3`.  A direct
check of the same six `(p,q)` cases shows that exactly one component avoids
`K_m`: it is the all-degree-two component with fourth coordinate zero,
running between the source `(0,m-1,m,0)` and sink `(m,0,m-1,0)`.  Cutting
it once gives

\[
                 |\mathcal A_m|=2m^2+m+4\qquad(m\ge2).       \tag{4.3}
\]

Every selected edge occurs in exactly one arm.  Write each arm as either
of its two vertex sequences and concatenate all arm words in an arbitrary
order.  If an arm has `h` edges, it contributes `h+1` letters.  Hence the
concatenation has length

\[
 \sum_{Q\in\mathcal A_m}(|E(Q)|+1)
       =|Z_m|+2m^2+m+4.                              \tag{4.4}
\]

Repeated arm endpoints are already included in (4.4).  Every lower vertex
appears, up to at most the surface-size isolated set, which can be appended
literally.  Every middle colour appears as the maximum of an internal
adjacent pair.  Arbitrary joins between arms create extra maxima but cannot
destroy these witnesses.

More generally, one may make `O(m^2)` additional cuts at internal arm
vertices.  A cut duplicates only that vertex, so (4.4) remains
`|Z_m|+O(m^2)`.  No long arm is duplicated.

This elementary observation removes the false restriction that the two
arms adjacent in the word must be paired by one rotation system at their
common graph vertex.  They may instead be joined at a **virtual seam**;
their endpoints may even be different vertices.

## 5. Corrected constructive target

The exact replacement for the refuted lemma is the following.

### Virtual-Seam Excursion Lemma (open)

There is a refinement of `A_m` using `O(m^2)` additional cuts, together
with an orientation and a linear ordering of all refined arms, such that
for every `y in P_m` with `|y|>=2m`, the concatenated arm word has a
contiguous interval all of whose letters are at most `y` and whose
coordinatewise maximum is `y`.

Equivalently, every upper target has a facet-spanning maximal `y`-run in
the **concatenated word**, where the run is allowed to cross virtual seams.

This statement is sufficient: (4.4) gives length `|Z_m|+O(m^2)`, internal
arm edges cover `Z_m`, singleton letters cover `V_m`, and the stated runs
cover the whole upper half.

It is also the precise seam-ordering problem for this fixed edge selection.
Any proposed proof must specify only:

1. `O(m^2)` cut locations;
2. one orientation for every resulting forced arm; and
3. one permutation of those `O(m^2)` arm blocks.

There are no remaining edge-selection variables and no long-arm repetition.
The four-target theorem proves that the permission to cross seams cannot be
deleted.

For the intended asymptotic construction, even this statement is stronger
than necessary.  The genuinely minimal sufficient version is:

### Surface-Defect Virtual-Seam Lemma (open)

There is a surface refinement and signed ordering as above for which the
number of upper targets not represented by an interval is `O(m^2)`.

Append those exceptional targets literally.  The central arm word, all
cut-vertex repetitions, and all literal repairs then still have total
length

\[
                         |Z_m|+O(m^2).               \tag{5.1}
\]

Thus a proof need not make the seam order perfect.  It only has to compress
the upper defect from its a priori volume order to the same surface order
as the branch kernel.  This defect form is the smallest compatibility
lemma needed by the four-box reduction.

### Bounded-copy formulation

An equivalent sufficient relaxation is to allow `O(m^2)` repeated lower
vertices but no repeated selected edge and then partition the word at every
adjacency which is not a selected edge.  The selected-edge portions are
exactly a surface refinement of the forced arms.  Conversely, every
surface-refined arm concatenation repeats only one vertex per cut and has
only `O(m^2)` nonedge seams.

Thus the accounting question is closed:

\[
 \boxed{\text{virtual seams and cut-vertex copies cost only }O(m^2).} \tag{5.2}
\]

The sole open issue is their simultaneous order geometry.

## 6. The smallest compatibility lemma still missing

For an oriented arm word `Q` and a target `y`, let its **trace** be the
ordered collection of maximal subintervals of `Q` lying in `[0,y]`, each
decorated by the facets of `y` met on that subinterval.  These traces are
explicit one-dimensional intervals; only the order of arms is unknown.

The Virtual-Seam Excursion Lemma is reduced to the following finite-kernel
statement.

> **Trace stitching lemma.**  The forced arms admit `O(m^2)` cuts and a
> signed permutation such that, for every upper `y`, some consecutive
> suffix--whole-blocks--prefix chain of its arm traces has the union of
> facet decorations `{1,2,3,4}` and contains no letter outside `[0,y]`.

The phrase “suffix--whole-blocks--prefix” is literal: a run crossing block
boundaries starts in a trace suffix, passes through zero or more complete
below-`y` blocks, and ends in a trace prefix.  This formulation exposes the
only global constraint and avoids the invalid inference “connected below
`y` implies consecutive below `y`.”

For the surface-defect version, the same conclusion may fail for
`O(m^2)` values of `y`.  That is the exact relaxed trace-stitching target
needed for asymptotic width-plus-surface length.

The next constructive attack should exploit the directed source/sink order
in (2.1)--(2.5) to sort arm traces recursively by the last two coordinates.
The four clauses (3.5) are the base compatibility gadget that recursion
must route through a virtual seam.  Proving the trace stitching lemma, even
with a larger absolute constant in the `O(m^2)` cuts, settles the entire
upper half for the lexicographic spine.

## 7. Status ledger

Proved here:

* the exact directed degree types and surface-size kernel;
* an all-`m` four-target refutation of the rotation-system lemma;
* the width-plus-surface arm-word accounting with arbitrary virtual seams;
* the exact seam-aware statement sufficient for upper universality.

Not proved:

* the Virtual-Seam Excursion Lemma / Trace Stitching Lemma;
* a recursion choosing the signed arm order;
* the separate deeper lower-factor construction.

The useful correction is therefore constructive rather than merely
negative: the old local-pairing target is impossible, while the new target
has exactly `O(m^2)` objects, permits the locally necessary incompatible
turns, and retains the desired `|Z_m|+O(m^2)` length.
