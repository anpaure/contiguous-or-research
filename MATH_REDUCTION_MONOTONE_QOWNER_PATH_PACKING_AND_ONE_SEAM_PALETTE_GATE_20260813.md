# Monotone `q`-owner paths reduce the middle/lower/residence problem to one seam colour per block

**Date:** 2026-08-13  
**Status:** unconditional exact local theorem and global packing reduction.  A monotone
exchange block with `q` owners has only boundary-clipped nonconstant coordinate runs,
uses `q-1` distinct immediate-lower colours, and, after placement in a globally
`q`-positive-resident chronology, inherits the literal maximal-antecedent erosion
identity.  A partition of the owner layer into such blocks would therefore leave
exactly one lower colour per block to be supplied at the joins.  Existence of the
required owner partition, a bijection
of joins to omitted lower colours, and the full compiler are not proved here.

## 1. The monotone exchange block

Fix `2<=q<=R`, a rank-`R` owner `A`, pairwise distinct labels

\[
 x_1,\ldots,x_{q-1}\in A,
 \qquad y_1,\ldots,y_{q-1}\in[k]\setminus A,              \tag{1.1}
\]

and put

\[
 T_i=A-\{x_1,\ldots,x_i\}+\{y_1,\ldots,y_i\}
 \qquad(0\le i\le q-1).                                  \tag{1.2}
\]

Thus `(T_0,...,T_(q-1))` is a simple Johnson path on `q` owners.  Its
internal immediate-lower colours are

\[
 L_i=T_{i-1}\cap T_i
 =A-\{x_1,\ldots,x_i\}+\{y_1,\ldots,y_{i-1}\}
 \qquad(1\le i\le q-1).                                 \tag{1.3}
\]

### Theorem 1.1 (exact local ledger)

The block has the following properties.

1. The displayed owners induce exactly a path `P_q` in the Johnson graph.  Hence the
   unordered support recovers its monotone order up to reversal.  In particular, the
   `q` owners and the `q-1` lower colours are separately pairwise distinct.
2. Every nonconstant coordinate word on the owner block is one of
   `1^a0^(q-a)` or `0^a1^(q-a)`; hence no positive or zero run is trapped
   internally.  Every nonconstant run reaches one of the two block boundaries.
3. Its owner intersection is
   \[
   S_A=A-\{x_1,\ldots,x_{q-1}\},\qquad |S_A|=R-q+1.       \tag{1.4}
   \]
4. If this block occurs consecutively in any globally `q`-positive-resident owner
   chronology and `P` is the maximal `q`-antecedent, then the complete consecutive
   intersection fan inside the block is materialized by literal source intervals:
   \[
   \bigcap_{j=a}^{b}T_j
     =\bigcup_{u=b}^{a+q-1}P_u,                            \tag{1.5}
   \]
   for `0<=a<=b<=q-1`, with indices inherited from the ambient cyclic chronology.

#### Proof

For `i<j`, the Johnson distance between `T_i` and `T_j` is exactly `j-i`, because
their symmetric difference consists of the `j-i` deleted labels and the `j-i`
inserted labels with indices in `(i,j]`.  Thus two displayed owners are adjacent
exactly when their indices are consecutive.  The induced graph on the support is
`P_q`, proving the rigidity statement and owner distinctness.  Every internal edge
then recovers its step index, so the lower colours are also distinct.
An old coordinate `x_i` is present up to its deletion and absent afterwards; a new
coordinate `y_i` is absent up to its insertion and present afterwards.  Untouched
coordinates are constant.  This gives Item 2, and intersecting all owners gives
(1.4).

For Item 4, use the ambient definition

\[
                         P_t=\bigcap_{v=0}^{q-1}T_{t-v}.  \tag{1.6}
\]

A coordinate belongs to `P_u` exactly when its positive owner run contains
`[u-q+1,u]`.  If it belongs to every owner in `[a,b]`, global `q`-positive residence
extends that interval inside its positive run to some length-`q` interval whose right
endpoint lies in `[b,a+q-1]`; hence it belongs to the right side of (1.5).  Conversely,
for every `u` in that range, `[a,b] subseteq [u-q+1,u]`, so `P_u` is contained in the
left side.  This proves (1.5).  \(\square\)

## 2. Exact global deficit ledger

Assume from now on that `k=2R-1`, and assume for the moment that the owner layer

\[
                         \mathcal O={ [k]\choose R}       \tag{2.1}
\]

is partitioned into `b` disjoint monotone blocks of `q` owners.  Then necessarily

\[
                         b={W\over q},\qquad W=|\mathcal O|. \tag{2.2}
\]

so this pure form requires `q|W`.  Open each block as a directed path.

### Proposition 2.1 (one lower ticket per block)

The internal edges use exactly

\[
                         b(q-1)=W-b                       \tag{2.3}
\]

distinct lower occurrences if their values are globally collision-free.  An exact
lower factor on the cyclically joined owner chronology has `W` edges and must use all
`W` rank-`(R-1)` lower colours.  Therefore the joins must supply exactly `b` further
lower colours: one omitted colour per block.

More precisely, if `\mathcal I` is the set of internal colours, then a cyclic joining
is lower-exact if and only if its `b` seam intersections form the set complement

\[
 { [k]\choose R-1}\setminus\mathcal I.                    \tag{2.4}
\]

#### Proof

There are `q-1` internal edges in every block and one seam after every block.  The
rank-`(R-1)` layer has the same size `W` as the rank-`R` owner layer when
`k=2R-1`.  Counting and value exactness give (2.3)--(2.4).  \(\square\)

Thus the lower palette is not an `O(W)` free decoration after block packing: it is an
exact one-ticket-per-block boundary matching.

## 3. Exact seam state

Assume from now on that the internal lower colours of different selected blocks are
globally distinct.  Then `|\mathcal I|=W-b`, so its complement (2.4) has exactly `b`
members.

For an oriented block `B`, record its first and last owners, its ordered transition
word of length `q-1`, and its internal lower-colour set.  A seam from block `B` to
block `B'` is legal when:

1. the terminal and initial owners are Johnson adjacent;
2. their intersection is an unused member of (2.4); and
3. the concatenated endpoint transition collars contain no repeated physical
   coordinate in any `q` consecutive transitions.

### Proposition 3.1

A cyclic ordering and orientation of the blocks is a `q`-biresident exact owner/lower
factor if and only if every seam is legal in the above sense and the seam intersections
are all distinct.  The global distinctness premise on the internal colours is
essential.

#### Proof

Owner exactness is the assumed vertex partition.  Theorem 1.1 does **not** by itself
give internal or global residence: it says only that a short nonconstant run cannot
have both endpoints inside one block.  Every run length is controlled by the cyclic
distance between consecutive transitions of the same physical coordinate.  Thus every
violation uses a `q`-edge transition window; since one block has only `q-1` internal
edges, that window meets a seam.  Condition 3 checks exactly all such windows and is
therefore precisely the global `q`-biresidence criterion.  Proposition 2.1 gives lower
exactness.  \(\square\)

## 4. Hypergraph formulation

Let `\mathcal H_q` be the `q`-uniform hypergraph on `\mathcal O` whose edges are the
unordered owner supports of all monotone exchange blocks (1.2).  A perfect matching in
`\mathcal H_q` is exactly an owner partition into monotone path supports.  By Theorem
1.1, a support already determines its internal edges and its two possible orientations;
there are no further hidden monotone orders.

### Proposition 4.1 (exact owner orbit degrees)

Put `ell=q-1`.  The simple support hypergraph `\mathcal H_q` is regular of degree

\[
 \boxed{D_q={q\over2}(R)_{\underline\ell}
                    (R-1)_{\underline\ell}.}             \tag{4.1}
\]

If two owners have Johnson distance `d`, their codegree is zero for `d>ell`, while

\[
 \boxed{\lambda_{q,d}=(q-d)(d!)^2
 (R-d)_{\underline{\ell-d}}
 (R-1-d)_{\underline{\ell-d}}}                           \tag{4.2}
\]

for `1<=d<=ell`.  Equivalently,

\[
 {\lambda_{q,d}\over D_q}
 ={2(q-d)\over q}\,{(d!)^2\over
 (R)_{\underline d}(R-1)_{\underline d}}.               \tag{4.3}
\]

When `2<=q<=(R+1)/2`, the maximum pair codegree occurs at `d=1` and

\[
 \boxed{{\Delta_2(\mathcal H_q)\over D_q}
 ={2(q-1)\over qR(R-1)}.}                                \tag{4.4}
\]

#### Proof

Fix an owner `T` and a prospective position `r in {0,...,ell}`.  Relative to `T`, the
`r` earlier exchanges choose ordered inserted coordinates in `T` and deleted
coordinates outside `T`; the `ell-r` later exchanges choose the remaining ordered
deleted coordinates in `T` and inserted coordinates outside `T`.  Altogether there
are `(R)_ell(R-1)_ell` oriented paths through `T` at position `r`.  Sum over the `q`
positions and divide by the two orientations recovered in Theorem 1.1.  This proves
(4.1).

Now fix `U,V` at Johnson distance `d`.  In any common support their positions differ
by exactly `d`.  Orient the recovered path so that `U` precedes `V`; there are `q-d`
choices for the position of `U`.  The `d` central deletions and insertions may be
ordered in `(d!)^2` ways.  The other `ell-d` exchanges choose, in order, disjoint
coordinates from `U\cap V` and from the complement of `U\cup V`, giving the last two
falling factorials in (4.2).  This orientation is unique for each support, so there is
no further factor two.  Division gives (4.3).

The ratio of consecutive right sides of (4.3) is

\[
 {q-d-1\over q-d}\,{(d+1)^2\over(R-d)(R-1-d)}.           \tag{4.5}
\]

It is less than one throughout `1<=d<=q-2` under `q<=(R+1)/2`, proving (4.4).
\(\square\)

The owner-support hypergraph alone does not impose global internal-palette
distinctness.  The exact smaller host is obtained by adding those resources.  Let

\[
 \mathcal L={ [k]\choose R-1}                             \tag{4.6}
\]

be a disjoint lower-colour shore, and let `\mathcal G_q` have one edge

\[
 \{T_0,\ldots,T_{q-1}\}\mathbin{\dot\cup}
 \{L_1,\ldots,L_{q-1}\}                                  \tag{4.7}
\]

for every monotone support.  It is `(2q-1)`-uniform.  Its owner degree is `D_q`; by
double counting, every lower vertex has degree

\[
                         {q-1\over q}D_q.                 \tag{4.8}
\]

### Theorem 4.2 (smallest exact packing/fusion target)

Assume `q|W`.  A `q`-biresident exact owner/lower factor whose marked internal blocks
are monotone paths of size `q` exists if and only if both of the following hold.

1. `\mathcal G_q` has an `\mathcal O`-perfect matching `\mathcal M`.  It contains
   `b=W/q` path blocks and leaves exactly a set `\mathcal C\subseteq\mathcal L` of
   `b` unused lower colours.
2. One can orient and cyclically order the blocks of `\mathcal M` so that every seam
   passes the transition-collar test and the `b` seam intersections are distinct
   members of `\mathcal C`.

Under Item 1, the last clause of Item 2 automatically makes the seam intersections
equal `\mathcal C`.  Equivalently, after `\mathcal M` is selected, the only remaining
middle/lower/residence problem is a rainbow directed Hamilton cycle through the
two-state port graph of its blocks, using the missing-colour set `\mathcal C`.

#### Proof

A matching in `\mathcal G_q` makes both the owner supports and all internal lower
colours disjoint.  If it is `\mathcal O`-perfect, it has `b` edges, uses `W-b` lower
resources, and leaves `b`; this is Item 1.  Proposition 3.1 proves that Item 2 completes
it to the desired factor.

Conversely, mark the internal path edges of such a factor.  Their owner and lower
values are exact and hence distinct, so their resource sets form an
`\mathcal O`-perfect matching in `\mathcal G_q`.  The remaining cycle edges are
exactly its legal seams and supply precisely the unused lower colours.  \(\square\)

This is an occurrence-labelled matching-plus-rainbow-Hamilton problem, but its host
uniformity is only `2q-1=Theta(sqrt k)`, not the exponential `2^m` of whole pair
cells.  The specific `2^M` whole-cube divisibility obstruction therefore disappears.
In the pure form `q|W` is a necessary scalar condition.  Allowing consecutive block
sizes removes this one scalar obstruction whenever `W=aq+b(q+1)` with nonnegative
integers `a,b`; it does not by itself prove a mixed monotone packing or remove any
further incidence-lattice obstruction.

## 5. Relation to modern forbidden-submatching nibbles

Proposition 4.1 computes the owner-only degrees.  The natural next step is to compute
all mixed owner/lower codegrees of `\mathcal G_q` and encode short transition
collisions as forbidden submatchings.  Lower-colour repetition is already a host
resource collision in `\mathcal G_q`.  Quantitative theorems for almost-perfect
matchings avoiding forbidden configurations apply only after checking their
uniformity quantifiers and the exact owner/lower degree imbalance (4.8).  In
particular, fixed-uniformity asymptotic notation cannot simply be used with
`q->infinity`.

The reduction here makes that literature interface precise.  A near-perfect matching
is useful only if its leave is compatible with a residue-carrying mixed-block absorber;
small relative leave alone is insufficient for the additive `B(k)+O(1)` target.

## 6. Scope

This theorem proves the exact local path ledger, its conditional erosion identity,
the owner-only pair codegrees, and the exact boundary deficit.  It does not
prove:

* a perfect or near-perfect matching in `\mathcal H_q`;
* global distinctness of internal lower colours;
* a seam-colour transversal;
* upper target coverage;
* the low-rank compiler; or
* a one-cycle terminal cap.

Its purpose is to replace the impossible intact-pair-cell selector by the smallest
natural residue-carrying path blocks and to expose the one-ticket-per-block coupling
that any successful packing must satisfy.
