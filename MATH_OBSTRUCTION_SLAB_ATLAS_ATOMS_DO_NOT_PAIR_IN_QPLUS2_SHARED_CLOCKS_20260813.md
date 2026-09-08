# Slab-atlas atoms do not pair into period-`q+2` shared clocks

**Date:** 2026-08-13  
**Audited clock source:**
`MATH_THEOREM_CLOCKED_SINGLETON_ARM_PRODUCT_CELL_COMPILER_AND_ATOM_COUNT_GATE_20260813.md`  
**Source SHA-256:**
`ac8e7e56b578353eb0fbc3cbf0e1a683c4dfaea1b9946fb5fbd89e5dd38f5b16`  
**Verifier:** `analyze_slab_atom_arm_lengths_and_pairing.py`  
**Verifier SHA-256:**
`f995e03d8f65ca2fff773282c9b7f954cdf228f99e7a65750caa814c2ab06d61`  
**Method:** literal replay of the corrected slab recurrence, exact directed
arm-superstring compatibility, shared-core rank, and coordinatewise
schedule avoidance.  The nontrivial census was run on `h100`.  
**Status:** unconditional obstruction to the proposed intact-atom shared-
rail compiler.  It does not obstruct splitting or redesigning the long fan
atoms.

## 1. Proposed shared-clock model

Put

\[
                         q=d+1,qquad N=q+2.                         \tag{1.1}
\]

A replacement atom rooted at product-grid cell `(x,y)` has base

\[
                         K(x,y)=C_x\cup D_y                          \tag{1.2}
\]

and directed arm sequence

\[
 X_{x+A-1},X_{x+A-2},\ldots,X_{x+1},
 Y_{y+1},Y_{y+2},\ldots,Y_{y+B-1}.                                 \tag{1.3}
\]

Here an `X_i` or `Y_j` denotes the corresponding singleton chain
increment.  Its arm length is

\[
                         L=A+B-2.                                   \tag{1.4}
\]

The proposed pairing places two such arm sequences, allowing reversal of
either, as directed contiguous arcs of one cyclic order on at most `N`
distinct toggle labels.

For a product-grid type `(u,v)` the required shared core has size

\[
                         c=R-q,                                     \tag{1.5}
\]

while

\[
 |K(x_1,y_1)\cup K(x_2,y_2)|
 =u+v+\max(x_1,x_2)+\max(y_1,y_2).                                  \tag{1.6}
\]

Thus core feasibility requires the right side of (1.6) to be at most
`c`; equality leaves no filler coordinates.

Finally, every arm position is assigned as a literal singleton target.
If a shared-core coordinate `f` is absent from an atom base, its emission
schedule must avoid that entire arm arc.  A legal schedule preserving the
immediate-lower row must meet every cyclic `(q-1)`-interval.  Therefore its
negative arc cannot contain `q-1` consecutive cycle positions.

## 2. First obstruction: corrected terminal fans can be too long

The full slab rectangles satisfy

\[
                         L=d=q-1.                                   \tag{2.1}
\]

The corrected terminal diagonal fans do **not** satisfy this bound.  Their
two arms may never attain their maxima simultaneously on a marked target,
so their physical arm length may be as large as

\[
                         2d-1=2q-3.                                 \tag{2.2}
\]

This is allowed by the diagonal-fan theorem but makes the intact arm
impossible to embed in an `N=q+2` cycle once `L>N`.

The exact `h100` replay at `k=201`, where `q=10,N=12`, found

\[
 {\#\text{atoms}\over W}=0.100692999533,                            \tag{2.3}
\]

\[
 {\#\{\text{atoms with }L>q-1\}\over W}=0.033281571900,             \tag{2.4}
\]

with maximum `L=17=2d-1`.  Hence one third of the weighted atoms already
violate the premise `L<=q-1` used by the shared-clock proposal.

## 3. Exact compatibility hierarchy on the short subfamily

Restrict temporarily to atoms with `L<=q-1`.  In each literal product-grid
copy form four graphs, successively imposing:

1. **cyclic:** the two directed arm words, under optional reversal, are
   consistent arcs of one cycle on at most `N` distinct labels;
2. **core<=:** cyclic compatibility plus (1.6) at most `c`;
3. **core=:** cyclic compatibility plus (1.6) equal to `c`;
4. **core/toggle-disjoint:** core feasibility plus the requirement that no
   proposed arm toggle already lies in the shared core;
5. **exact:** core feasibility, toggle/core disjointness, and for every
   coordinate missing from one or both bases a `(q-1)`-hitting schedule
   avoiding the union of its negative arm arcs.

The directed-word test is exact: each arm contributes successor equations;
shared labels must have the same predecessor and successor, the resulting
components must be directed paths or one complete directed cycle, and the
remaining labels are inserted as guards.

For the schedule test, an avoided union of path components can be placed
in the gaps between guard hits if and only if its component lengths pack
into the available guard gaps of capacity `q-2`.  This is an exact finite
bin-packing test because the guard labels themselves form a legal hitting
schedule.

### Theorem 3.1 (intact shared-clock failure at `k=201`)

For the corrected minimum-cost slab orientation at `k=201`, the weighted
maximum matching sizes, normalized by `W`, are

\[
\begin{array}{c|c|c}
\text{compatibility level}&\text{matching}/W&
 N(\#\text{short atoms}-\text{matching})/W\\ \hline
\text{cyclic}&0.005094457153&0.747803645765\\
\text{core at most}&0.004868974331&0.750509439632\\
\text{core equality}&0.002734816863&0.776119329246\\
\text{core/toggle disjoint}&0&0.808937131603\\
\text{exact}&0&0.808937131603
\end{array}                                                        \tag{3.1}
\]

Moreover, the short atoms which cannot run singly because their required
filler would have to avoid a full `(q-1)` arm have weighted count

\[
                         0.012871472752,W,                          \tag{3.2}
\]

and product-grid copies of total normalized weight

\[
                         0.010291538801                             \tag{3.3}
\]

contain such a mandatory vertex but no exact compatible matching.

#### Proof

The atom list is generated literally by equations (4.1)--(4.11) of the
corrected slab-fan theorem, using the orientation which minimizes source
cost and then atom count.  Equations (1.3)--(1.6) implement the first three
graphs.  The fourth graph is already empty: every surviving proposed pair
uses some chain increment both as one atom's toggle and as an element of
the other atom's base, hence of the shared core.  This violates the
disjoint `F dotcup X` hypothesis of the clock and destroys toggle privacy
and owner rank.

For completeness, in the exact graph a base-difference coordinate imposes the
other atom's arm as a negative arc, and a filler coordinate imposes both
arms.  The path-component gap-packing criterion above is then necessary
and sufficient for an avoiding `(q-1)`-hitting schedule.  Exact maximum
weight matching was computed independently inside every grid-copy type and
weighted by the product-SCD chain multiplicity.  The resulting exact graph
remains empty.  \(\square\)

The last column of (3.1) is explicitly conditional on discarding the long
unembeddable atoms.  It is not a complete compiler charge.

## 4. Consequence

The proposed intact-atom pairing does not produce a coefficient-one
carrier:

* many terminal fans do not fit in one `q+2` cycle;
* even among the short atoms, common-core and cyclic-order constraints
  leave very few pairs; and
* imposing arm-toggle/shared-core disjointness already removes every pair;
  the later singleton-target schedule constraints cannot restore one.

This failure is stronger than a bad numerical coefficient: some weighted
grid copies have no feasible exact packet assignment at all.

The viable escape is to change the objects before matching—split a long
terminal fan into shorter carrier atoms while preserving its mixed target
hull, replace the singleton assignment by safe masked positions, or use a
different pair-cell clock whose source letters already contain the required
core masks.  Marginal unused positions cannot repair the failed
coordinatewise schedule inequalities.

## 5. Verification artifact

`analyze_slab_atom_arm_lengths_and_pairing.py` contains the exact recurrence
replay, arm extraction, cyclic-superstring test, common-core filters,
schedule-avoidance test, and NetworkX exact matching call.  The substantial
run was performed only on `h100`.  Further requested parameter runs were
stopped after the exact obstruction was established.
