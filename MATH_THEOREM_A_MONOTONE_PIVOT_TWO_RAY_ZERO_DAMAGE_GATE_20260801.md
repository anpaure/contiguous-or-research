# Monotone pivot insertion: exact two-ray compiler and the pivot-rich owner gate

Date: 2026-08-01  
Lane: A, additive-constant common cap  
Status: exact positive compiler theorem and sharp physical obstruction for
the two canonical source catalogues.  No all-dimension carrier construction
is claimed.

## 0. Outcome

Insert one nonempty source letter `X` at a cut.  Every old contiguous-OR
witness survives, with the same value, if and only if

\[
                         X\subseteq A_{-1}\cup A_1.       \tag{0.1}
\]

Inside the width-`h` compiler band, the only old cells which fail to
transport are the `h-1` crossing cells of old width `h`.  The only genuinely
new cells are the singleton `X` and two rays of `h-1` cells each.

This yields a positive zero-damage theorem.  Suppose the inserted word has
a flat rank-`m` depth-`h` derivative.  By (0.1), every lost crossing cell is
itself one of the new rank-`m` middle rows.  It therefore carries no edge of
the strict-lower compiler graph.  Every edge of a reference lower matching
transports injectively.  If the singleton and two rays equal one task and
the packet's two damaged target chains, release the old edges of those
`2h-2` chain targets; the remaining transported matching plus the `2h-1`
new edges is a complete lower compiler with **zero** old-target deficiency.
The displayed inserted source word is a common-`Q` witness, so the
maximal-word criterion adds no hidden cap obstruction.

The ray equalities are exact.  With

\[
 B_i^- =\bigcup_{t=1}^iA_{-t},\qquad
 B_i^+ =\bigcup_{t=1}^iA_t,                              \tag{0.2}
\]

the new cells have values

\[
                         X,\quad X\cup B_i^-,\quad
                         X\cup B_i^+\qquad(1\le i<h).     \tag{0.3}
\]

Thus a prescribed occurrence-labelled chain pair is realized exactly when
it equals (0.3).  If `X` is not prescribed in advance, this is the interval
condition

\[
 \bigcup_{\sigma\in\{-,+\}}\bigcup_{i=1}^{h-1}
       (T_i^\sigma\setminus B_i^\sigma)
 \ \subseteq X\subseteq\
 (A_{-1}\cup A_1)\cap P_0\cap
 \bigcap_{\sigma,i}T_i^\sigma,                           \tag{0.4}
\]

together with `B_i^sigma subseteq T_i^sigma` for every row and nonemptiness
of `X`.  For a typed task, `X` is fixed and (0.3) is the simpler exact test.

There are two sharp physical warnings.

1. In the canonical shortest rotating-hole erosion source, every crossing
   old width-`h` union has rank `m-1`.  Monotonicity makes `X` redundant, so
   the new middle row still has rank `m-1`.  No monotone pivot can be inserted
   into that canonical source while retaining a flat rank-`m` carrier.
2. The canonical complementary coatom chains do give rank `m`, and hence a
   zero-damage compiler, but all `h-1` mixed middle rows are the same owner.
   For an owner-simple carrier this is unacceptable once `h>=3`.

The exact remaining internal physical object is therefore a **pivot-rich
chain pair**: the `h-1` joins

\[
                         T_i^-\cup T_{h-i}^+             \tag{0.5}
\]

must all have rank `m` and must satisfy the required owner multiplicity.
The two endpoint joins must also be allowed rank-`m` owners, and all `h+1`
new rows must have the prescribed Johnson adjacency to one another and to
the exterior chronology, while (0.3) and the final caps hold.  The compiler
part is closed; constructing such a pair in every Pascal child is not.

## 1. Exact monotone insertion algebra

Let an old nonzero source word have an internal cut with at least `h` old
source positions on each side,

\[
 \cdots,A_{-2},A_{-1}\mid A_1,A_2,\cdots.                \tag{1.1}
\]

Insert a new nonzero letter `A_0=X`.  Transport an old interval by keeping
its old endpoints in the enlarged line.

### Theorem 1.1 (monotone-pivot equivalence)

Every old interval has the same OR as its transported interval if and only
if (0.1) holds.

#### Proof

An interval on one side of the cut is unchanged.  An old interval crossing
the cut contains both adjacent letters `A_(-1),A_1`; after insertion its OR
only gains `X`.  Hence (0.1) is sufficient.  Conversely, apply preservation
to the old two-letter interval `A_(-1),A_1`.  Its transported interval adds
`X`, so equality forces (0.1).  \(\square\)

This is equality of literal witnesses, not merely inclusion of OR decks.
It applies at every width and in every exterior context.

Now restrict cells to intervals of length at most `h`.  The standard
transport keeps every one-sided old cell and every crossing old cell of
length at most `h-1`.  A crossing old cell of length `h` acquires length
`h+1` and leaves the band.

### Proposition 1.2 (exact band exchange)

Exactly `h-1` old cells leave the band.  They are

\[
 I_i^\times=[-i,-1]\cup[1,h-i],qquad 1\le i<h,          \tag{1.2}
\]

with values

\[
                         C_i=B_i^-\cup B_{h-i}^+.         \tag{1.3}
\]

The cells outside the transport image are exactly

\[
 [0,0],\quad[-i,0],\quad[0,i]qquad(1\le i<h),           \tag{1.4}
\]

and have the values (0.3).  Thus there are `2h-1` new cells and net band
gain `h`.

#### Proof

Deleting the inserted position from a new mixed interval gives the unique
old interval transported to it.  The new intervals with no old points on
one side are exactly the two rays (1.4).  An old crossing interval leaves
the band precisely when its old length was `h`; there are `h-1` choices for
its left count.  The value formulas are direct unions.  \(\square\)

Under (0.1), `X subseteq C_i` for all `i`, because every crossing cell
contains `A_(-1) union A_1`.  Therefore the new depth-`h` middle row on the
hull of `I_i^times` has value

\[
                         X\cup C_i=C_i.                  \tag{1.5}
\]

This observation is the source of both the positive compiler theorem and
the physical rank obstruction.

## 2. Exact two-ray target criterion

Let `T_i^-` and `T_i^+` (`1<=i<h`) be prescribed occurrence-labelled
targets for the left and right new rays, and let the singleton task be
`T_0=X`.

### Theorem 2.1 (fixed-source ray criterion)

For the fixed adjacent source letters, the two ray banks realize the
prescribed targets if and only if

\[
                         T_i^-=X\cup B_i^-,\qquad
                         T_i^+=X\cup B_i^+               \tag{2.1}
\]

for every `1<=i<h`.  If `X` is variable subject to cap `P_0`, an admissible
nonempty `X` exists if and only if `B_i^sigma subseteq T_i^sigma` for all
rows and the set interval (0.4) contains a nonempty member.

#### Proof

The first statement is Proposition 1.2.  The equality

\[
                         X\cup B=T                         \tag{2.2}
\]

is equivalent to

\[
                         B\subseteq T,qquad
                         T\setminus B\subseteq X\subseteq T.             \tag{2.3}
\]

Intersect the upper bounds and unite the lower bounds over all rows, then
add the monotonicity bound `X subseteq A_(-1) union A_1`, cap legality
`X subseteq P_0`, and nonemptiness.  This is exactly (0.4).  \(\square\)

### Corollary 2.2 (constructing arbitrary strict ray chains)

Suppose

\[
 X\subsetneq T_1^-\subsetneq\cdots\subsetneq T_{h-1}^-,
 \qquad
 X\subsetneq T_1^+\subsetneq\cdots\subsetneq T_{h-1}^+. \tag{2.4}
\]

Define

\[
\begin{aligned}
 A_{-1}&=T_1^-,&
 A_{-i}&=T_i^-\setminus T_{i-1}^- &&(2\le i<h),\\
 A_1&=T_1^+,&
 A_i&=T_i^+\setminus T_{i-1}^+ &&(2\le i<h).
\end{aligned}                                             \tag{2.5}
\]

Then every source letter is nonempty, (0.1) holds, and insertion of `X`
realizes the two chains.  The destroyed crossing values are forced to be

\[
                         C_i=T_i^-\cup T_{h-i}^+.         \tag{2.6}
\]

#### Proof

The differences telescope to the chains.  Both adjacent letters contain
`X`, proving monotonicity, and (2.6) is (1.3).  \(\square\)

Thus the two ray chains are freely constructible as compiler data, but their
crossed joins (2.6) are not free.  They are exactly the middle-owner state
which must be checked physically.

## 3. Zero residual compiler damage

Let `T=D^hA` denote the final depth-`h` chronology after insertion.  Assume
all of its rows have rank `m`.  Let `M_0` saturate the entire declared old
strict-lower target bank by old width-at-most-`h` cells.

### Theorem 3.1 (flat monotone pivot gives zero old damage)

Under (0.1), every edge of `M_0` transports injectively to a final compiler
cell with the same literal value.  In particular its exact failure set is
empty; equivalently, one may take a complete plus-state damage set with

\[
                         D\cap C(\phi(M_0))=\varnothing.  \tag{3.1}
\]

If, in addition,

1. the task `X` is a strict-lower target outside the old target bank, while the `2h-2` distinct
   ray targets in (2.1) form a set `R` of old targets saturated by `M_0`;
2. the old `M_0` edges of `R` are released and those targets are assigned to
   the non-singleton cells in (1.4), with `X` assigned to the singleton; and
3. the displayed inserted source letters lie in their final caps,

then the transported matching on `M_0\setminus R` plus the ray edges is a
complete literal matching for every old target and the new task.  The exact
common-`Q` maximal word exists.  Hence one inserted letter has zero residual
compiler deficiency for `H=1`.

#### Proof

By Proposition 1.2, the only old cells which do not transport are the
crossing cells `I_i^times`.  Their old values are `C_i`.  Their new hulls are
depth-`h` middle rows with the same values by (1.5).  Flatness gives
`|C_i|=m`.  A strict-lower target has rank less than `m`, so no edge of
`M_0` uses any `I_i^times`.  Every `M_0` edge therefore transports, and
Theorem 1.1 preserves its exact OR.  Transport is injective on cells, proving
(3.1).

Delete the `M_0` edges incident with the targets in `R`.  Every remaining
edge transports by the preceding paragraph.  The cells in (1.4) are exactly
those outside the transport image.  The displayed task/ray edges are
therefore pairwise cell-disjoint and disjoint from the transported matching;
target distinctness gives a matching which covers all old targets and `X`.

Finally, the inserted source word itself is nonzero, cap-legal, realizes
all final middle rows, every transported old pin row (including the released
rows of `R` as protected duplicate witnesses), and every task/ray row.
It is a feasible word for the joint common-`Q` system.  The exact
maximal-letter theorem then gives a componentwise maximal feasible word as
well.  No remote cap casualty is hidden.  \(\square\)

The flatness assumption is load-bearing.  Monotonicity preserves an old
crossing OR as an unrestricted interval, but if its rank is below `m`, its
lost short cell may carry an edge of `M_0`.

### Corollary 3.2 (exact fixed-outside nonflat residual matching)

Without flatness, let `R` be the set of distinct strict-lower targets which
`M_0` matches to the lost cells (1.2), after removing any target already
assigned to a ray cell.  Freeze the transported edges of `M_0` outside `R`
and the prescribed ray edges.  Let `G_ext` be the incidence graph from `R`
to all remaining final cells, including unused cells in the transport image.
Within this fixed-outside architecture, the pivot has zero residual
old-target damage if and only if

\[
                         |N_{G_{ext}}(Y)|\ge |Y|
                         \qquad(Y\subseteq R),            \tag{3.2}
\]

and the resulting complete pin table passes the common-`Q` test.

#### Proof

Every frozen old matching edge outside the lost cells transports.  The
remaining targets must, and by Hall can, be assigned exactly through
`G_ext`.  Literal simultaneous realizability is then precisely the
common-`Q` maximal-letter criterion.  \(\square\)

If the outside edges may also move, the exact matching condition is ordinary
Hall in the full final target--cell graph, followed by the one joint
common-`Q` test.  The smaller condition (3.2) is then sufficient, not
necessary.

## 4. The complementary coatom packet

Let `G={g_1,...,g_h}` be disjoint from nonempty `X` and from `a,b`.  Define

\[
\begin{aligned}
 T_i^-&=X\cup\{b,g_1,\ldots,g_i\},\\
 T_i^+&=X\cup\{a,g_{h-i+1},\ldots,g_h\},
                         &&1\le i<h.                    \tag{4.1}
\end{aligned}
\]

These are the canonical prefix/suffix target chains of the mixed-coatom
packet.  Corollary 2.2 realizes them by a monotone pivot.  Their crossed
joins are independent of `i`:

\[
                         C_i=X\cup\{a,b\}\cup G=:C.      \tag{4.2}
\]

### Corollary 4.1 (compiler-positive canonical pivot)

Assume `|C|=m`, the two endpoint star-containing middle rows are allowed
rank-`m` owners with the required exterior Johnson adjacencies, and the
task/ray/cap hypotheses of Theorem 3.1 hold.  Then the canonical
complementary-chain pivot satisfies Theorem 3.1.  It gives one task, both
complete damaged target chains, and zero residual strict-lower compiler
damage from one added letter.

#### Proof

Every mixed new middle row is `C` by (4.2), hence has rank `m`.  The two
one-sided endpoint middle rows must still be checked in the exterior
carrier; once they also have rank `m`, Theorem 3.1 applies.  \(\square\)

The conclusion is exactly about the lower compiler.  The `h-1` internal
middle rows are all the same owner `C`.  For `h>=3` this creates duplicate
owner excess at least `h-2`; a simple owner chronology cannot use the packet
without an additional rethread.  This is the first sharp incompatibility.

## 5. Failure in the canonical shortest-rail source

Assume `h>=2`.  For the frozen shortest rotating-hole rail, the canonical erosion letters
are

\[
                         W_j=K\cup\{z_j\},               \tag{5.1}
\]

where `|K|=m-h-1` and the active labels are distinct around the relevant
cycle.  Every old crossing interval of length `h` has union

\[
                         K\cup\{h\text{ active labels}\}, \tag{5.2}
\]

of rank `m-1`.

### Proposition 5.1 (canonical-rail monotone-pivot no-go)

No insertion satisfying (0.1) can turn the canonical source (5.1) into a
flat rank-`m` depth-`h` source at that cut.

#### Proof

For each of the `h-1` internal new middle windows, (1.5) says its union is
the corresponding old crossing value.  Equation (5.2) gives rank `m-1`,
not `m`.  \(\square\)

This obstruction already occurs at `h=2`.  It concerns the canonical
erosion preimage, not the physical rail owner cycle: a different, pivot-rich
preimage may exist.

## 6. Exact proved boundary

The monotone-pivot compiler question is closed.

* Old arbitrary-width OR witnesses survive exactly under (0.1).
* The task and damaged chain cells are exactly (0.3), with feasibility
  characterized by (0.4).
* On a flat final carrier, all old strict-lower matching edges transport and
  the new ray assignment gives a complete common cap with zero residual
  damage for `H=1`.
* Off the flat face, (3.2) plus common-`Q` is necessary and sufficient with
  the outside transported edges frozen; arbitrary rematching uses full Hall.

The remaining construction theorem is physical rather than compiler
algebra: produce a pivot-rich source for which the joins (0.5), including
the two endpoint middle rows, form the required owner-simple Johnson
chronology and satisfy the residence/q1/upper packet interface.  The two
canonical catalogues fail this in complementary ways: the shortest-rail
source is rank-deficient, while the complementary coatom source is
owner-degenerate.

## 7. Adversarial audit

1. Full-word OR preservation does not by itself preserve `COMP_h`: crossing
   width-`h` cells become width `h+1`.  Theorem 3.1 uses flatness to prove
   those cells were unavailable to the strict-lower matching.
2. The `2h-1` new fan cells are not `2h-1` free cells in an arbitrary
   insertion.  Here they are free because the transported matching avoids
   the lost cells and transport covers every other old/new correspondence.
3. Equality (0.4) includes cap legality, monotonicity and every ray target;
   marginal chain cardinalities are insufficient.
4. A displayed feasible source word is enough for common-`Q`, because the
   maximal-word theorem is an equivalence.  No product-like or Hall
   assumption is used.
5. Corollary 4.1 does not claim owner legality: its repeated middle row is
   explicitly the remaining obstruction.
6. Proposition 5.1 is scoped to the canonical erosion source.  It does not
   exclude a noncanonical preimage of the same physical rotating-hole rail.
