# Shielded opposed hinges: owner-wide two-cell rectangles with one protected exception

**Date:** 2026-08-02  
**Lane:** ROOT, exact-`d` macro-Euler / regenerative pull-cell  
**Status:** unconditional two-cell literal construction, exact convex-row
filtering theorem, and an owner-wide bounded-exception factor.  The global
Hoffman expansion, protected spanning skeleton, residence chronology, and
compiler completion remain unproved.

## 0. Outcome

The raw unsaturated hinge is necessarily one-sided: fixing its depth-one
suffix payload fixes its last source letter and therefore its complete head.
Moreover, raw one-sided menus can have an arbitrarily large predecessor Hall
deficit.  Thus they cannot themselves give a dimension-uniform sidecar.

There is nevertheless an unconditional multi-edge replacement.  If two
rank-`r` owners are Johnson adjacent,

\[
                  T^-=R\cup\{a\},\qquad T^+=R\cup\{b\},
                  \qquad |R|=r-1,                         \tag{0.1}
\]

then a forward full-depth unsaturated hinge for `T^-` and the reverse of a
second full-depth unsaturated hinge for `T^+` can be glued at the fixed
coatom state `R`.  The resulting two-cell word has independently variable
left and right literal `d`-rails.  Both endpoint states and the middle state
are proper in their adjacent owners, so no owner is forced twice.

The important extra fact is **shielding**.  The only two variable source
letters lie at the ends of the block, and every optional coordinate in
either one is repeated in the fixed middle core.  Consequently every
contiguous-interval OR predicate, in an already fixed global placement, is
left-only, right-only, or independent of both ends.  Point caps and pins are
also one-sided, while physical address collisions are fixed before the set
choice.  Therefore arbitrary PCPS Boolean/erosion filtering preserves a
Cartesian product.  The rooted graphic-Rado choice is independent because
the owner chronology and incidence occurrence do not change.

This closes a genuine ambient supply clause.  For the triangular odd problem
at every owner rank `r>=5`, the actual depth satisfies `r>=d+3`.  A Middle
Levels Hamilton cycle partitions all rank-`r` owners into adjacent pairs,
except for at most one prescribed aperture owner when the owner count is
odd.  The shared rank-`r-1` roots of the pairs are automatically distinct,
and the corresponding incidences form a matching in one global predecessor
phase.  Every pair supports a nontrivial two-sided shielded rectangle; the
single exceptional owner has the already proved fixed unsaturated hinge and
may be put in the protected bank.  Thus the **nonrectangular owner casualty
is at most one**, uniformly in the dimension, and deleting the transition
through the omitted root gives a correctly phased connected spanning
aperture path in the owner/lower-root projection.

This is not yet `B+O(1)`.  Complete-state balance between different pair
macros can still have the disjoint-copy Hall obstruction, and a literal
continuation of a pair must retain its newly entered coordinate for the next
`d` owner cells.  PCPS factorization checks a chronology after it has been
chosen; it does not construct a resident chronology or prove the macro
Hoffman cuts.  The exact surviving global hypothesis is recorded in Section
7 rather than hidden in the local theorem.

## 1. Complete-state scope

Fix a global source line and a placement of one local block in that line.
The placement includes the exact global address quotient; in particular,
all identifications caused by intervening components shorter than `d` have
already been made.  A **convex-row guard family** consists of:

1. prescribed OR values on occurrence-labelled contiguous source intervals;
2. pointwise lower pins and upper caps on source letters;
3. capacity-one conditions on the resulting global interval addresses; and
4. a fixed input state of every owner-history automaton, propagated through
   the displayed fixed owner row.

The capacity-one conditions in item 3 depend on physical addresses, not on
the optional endpoint subsets.  The history state in item 4 may be the full
clipped signed history.  It is fixed as an input/output **action**, not
reconstructed from the two endpoint masks.

This is the local data used by the complete-state macro-Euler theorem.  It
does not assert that independently chosen local placements have one
globally consistent quotient.  That path-level condition remains explicit
in Section 7.

## 2. The opposed-hinge word

Assume `d>=2`.  Let (0.1) hold and choose an ordered partition

\[
                         R=D_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}D_d              \tag{2.1}
\]

into nonempty sets.  Choose guards `y in D_1` and `z in D_d`.  For

\[
             A\subseteq D_1-\{y\},\qquad
             A'\subseteq D_d-\{z\},                    \tag{2.2}
\]

put

\[
 X(A,A')=\bigl(\{a\}\cup A,
        D_d,D_{d-1},\ldots,D_1,
        \{b\}\cup A'\bigr).                            \tag{2.3}
\]

This word has `d+2` nonempty letters and therefore two depth-`d` cells.
Write

\[
\begin{aligned}
 p(A)&=(\{a\}\cup A,D_d,\ldots,D_2),\\
 h&=(D_d,D_{d-1},\ldots,D_1),\\
 q(A')&=(D_{d-1},\ldots,D_1,\{b\}\cup A').            \tag{2.4}
\end{aligned}
\]

### Theorem 2.1 (shielded opposed-hinge rectangle)

Every cross-pair `(A,A')` in (2.2) gives a literal two-edge macro

\[
                         p(A)\longrightarrow h\longrightarrow q(A')
                                                               \tag{2.5}
\]

with the following properties.

1. Its two owner windows are exactly `T^-` and `T^+`, in that order.
2. The three state unions are proper in every adjacent owner.  More
   precisely, the tail misses `y`, the head misses `z`, and the middle has
   union `R`.
3. The left cell carries the fixed suffix chain

   \[
                         S_q=D_1\cup\cdots\cup D_q
                         \quad(1\le q\le d),             \tag{2.6}
   \]

   while the right cell carries, in reverse orientation, the fixed prefix
   chain

   \[
                         S'_q=D_d\cup\cdots\cup D_{d-q+1}.
                                                               \tag{2.7}
   \]
4. The literal macro relation contains the Cartesian product

   \[
       \{p(A):A\subseteq D_1-\{y\}\}
       \times
       \{q(A'):A'\subseteq D_d-\{z\}\},               \tag{2.8}
   \]

   of respective sizes `2^(|D_1|-1)` and `2^(|D_d|-1)`.
5. The complete owner row, its immediate-lower occurrence `R`, and its
   immediate-upper occurrence `R union {a,b}` are invariant throughout
   (2.8).

#### Proof

The first length-`d+1` union in (2.3) is

\[
              \{a\}\cup A\cup D_d\cup\cdots\cup D_1
                         =R\cup\{a\}=T^-.
\]

The second is `R union {b}=T^+`.  The tail omits the last fixed letter
`D_1`; its only possible replacement from that layer is `A`, which omits
`y`.  Dually, the head omits `D_d` and its endpoint subset `A'` omits `z`.
The middle union is `R`.  This proves items 1--2 and the one-copy
unsaturation claim.

The last `q` fixed letters in the first cell have union (2.6).  For the
right cell, start with the ordinary forward unsaturated word

\[
        (\{b\}\cup A',D_1,D_2,\ldots,D_d)
\]

for the reversed layer chain and reverse the whole trace.  It becomes the
second half of (2.3), proving (2.7).  Only the first letter depends on `A`
and only the last depends on `A'`; both maps are injective.  Every
cross-pair is the displayed physical word, giving (2.8).  The owner and
incidence statements follow from the two fixed windows.  \(\square\)

### Corollary 2.2 (nontrivial menus)

If

\[
                              r\ge d+3,                 \tag{2.9}
\]

then (2.1) may be chosen with `|D_1|,|D_d|>=2`.  Both shores of (2.8) then
have at least two literal states.

#### Proof

Use two elements in each endpoint layer and one in every intermediate
layer.  This consumes `d+2` elements of `R`, whose size is `r-1`; distribute
any remainder arbitrarily.  \(\square\)

## 3. Exact convex-row shielding

Let `u` and `v=u+d+1` be the two variable positions of (2.3) in its fixed
global placement.  All source letters outside these positions are frozen.

### Theorem 3.1 (arbitrary-width interval filtering stays Cartesian)

Impose any convex-row guard family from Section 1.  Let `F` be the set of
endpoint pairs `(A,A')` from (2.2) which pass all set-valued interval, pin,
and cap rows.  Then there are subfamilies

\[
                  \mathcal A\subseteq2^{D_1-\{y\}},\qquad
                  \mathcal H\subseteq2^{D_d-\{z\}}              \tag{3.1}
\]

such that

                              F=\mathcal A\times\mathcal H.      \tag{3.2}

In particular, if one guarded realization exists, the projections of the
guarded relation form a genuine nonempty Cartesian complete-state
rectangle.  No arbitrary-width contiguous-OR row creates an `A`--`A'`
correlation.

#### Proof

Consider one prescribed contiguous interval `I`.  If `I` contains neither
`u` nor `v`, its OR is fixed.  If it contains exactly one of them, its OR
depends only on the corresponding endpoint subset.  If it contains both,
convexity forces it to contain every position between them, whose fixed
letters have union `R`.  Since `A,A' subseteq R`, both optional subsets are
then redundant and the interval OR is again fixed.

Thus every interval equality is left-only, right-only, or constant.  A
point pin or cap has the same trichotomy.  Conjoining all left predicates
defines `mathcal A`, conjoining all right predicates defines `mathcal H`,
and the constant predicates either reject every pair or accept every pair.
If the full system is nonempty the latter all accept, which proves (3.2).
Global address distinctness was frozen with the placement and hence cannot
couple the two set choices.  \(\square\)

### Corollary 3.2 (PCPS Rado--erosion compatibility)

Fix the complete prospective chronology, global address quotient, pins,
caps, interval rows, predecessor phase, incidence support, and forced
protected forest as in the PCPS Rado--erosion theorem.  Force the interior
letters of (2.3) by equal pin and cap, and give its two endpoint letters the
pins/caps

\[
 \{a\}\subseteq X_u\subseteq\{a\}\cup(D_1-\{y\}),\qquad
 \{b\}\subseteq X_v\subseteq\{b\}\cup(D_d-\{z\}).     \tag{3.3}
\]

If the Boolean closure rows pass, the set of feasible endpoint rails is the
nonempty rectangle (3.2).  If in addition the contracted graphic-Rado
deficiency is zero, one upper-exact rooted representative set can be chosen
independently and used for every cross-pair in that rectangle.

For a fixed accepting input owner-history state, propagation across the
fixed two-owner row gives one fixed output history state for every
cross-pair.  Therefore (3.2), with these history states and the fixed rooted
incidence data appended to its two shores, is a literal rectangle in the
frozen PCPS rail--owner-history state space.

#### Proof

The Boolean half is Theorem 3.1 together with the exact maximal-envelope
criterion of PCPS.  The pins/caps (3.3) make every feasible endpoint letter
have precisely the form used in (2.3).  The owner windows, transition root,
upper colour, support occurrence, and forced forest are independent of
`A,A'`; hence the Rado variables share no endpoint decision variable and
the PCPS product theorem applies.

Finally, the exact owner-history automaton reads only the fixed owner row
`(T^-,T^+)`.  Fixing one accepted input state fixes its output state, so
history propagation does not shrink (3.2).  \(\square\)

The word *fixed* is load-bearing in this corollary.  Choosing a different
chronology, occurrence address, or forced history state after seeing the
endpoint subsets lies outside the factorization.  Likewise, an additional
non-set automaton whose output genuinely depends jointly on `A` and `A'`
is not covered by Theorem 3.1.  Before applying the full macro-Hoffman
theorem, every reset, common-cap, or other aggregate coordinate must be
proved fixed or left/right separable on this rectangle.  The present result
proves that property for contiguous-OR rows, point caps/pins, fixed physical
addresses, rooted incidence/Rado data, and the fixed owner-history action;
it does not silently assert it for an arbitrary extra automaton.

## 4. Owner-wide bounded-exception factor

Let

\[
                         \mathcal O={ [2r-1]\choose r},
                         \qquad W=|\mathcal O|.          \tag{4.1}
\]

Fix an omitted lower root `o` and choose a desired aperture owner
`T_* in mathcal O` with `o subset T_*`.

### Theorem 4.1 (root-distinct adjacent-pair factor with one exception)

There are a perfect predecessor phase `M_0` and an alternating Middle Levels
Hamilton cycle containing the prescribed incidence `o subset T_*` such that,
after the owner transition through `o` is opened, the owner bank has a
decomposition with the following form.

* If `W` is even, all owners split into Johnson-adjacent unordered pairs,
  and the pair containing `T_*` may be oriented with `T_*` second.
* If `W` is odd, `T_*` is the sole singleton and every other owner splits
  into Johnson-adjacent pairs.

The rank-`r-1` intersections of all paired owners are distinct.  In the
phase `M_0`, one supporting incidence for every pair is outside `M_0`, and
these supporting incidences form an incidence matching.  The paired blocks
and the unused transition roots occur in one connected projected Hamilton
path whose omitted root is exactly `o` and whose terminal owner is `T_*`.

Consequently, under `r>=d+3`, every pair has a nontrivial shielded
two-sided macro rectangle from Corollary 2.2.  In the odd case the sole
nonrectangular owner may use any one fixed unsaturated hinge and be placed
in the protected terminal bank.  The endpoint aperture `o subset T_*` is
then literal.  Thus the number of nonrectangular owner roles is at most one.

#### Proof

The symmetric group is transitive on the incidences between ranks `r-1`
and `r`.  Applying a coordinate permutation to any Middle Levels Hamilton
cycle therefore gives one containing the prescribed edge `oT_*`.  Index it
as

\[
 o=L_0,T_0=T_*,L_1,T_1,\ldots,L_{W-1},T_{W-1},L_0.    \tag{4.2}
\]

where `|L_i|=r-1`, `|T_i|=r`, and every displayed consecutive pair is
incident.  Put `M_0(L_i)=T_i`.  Then consecutive owners `T_i,T_(i+1)` are
distinct supersets of `L_(i+1)`, and hence

\[
                         T_i\cap T_{i+1}=L_{i+1}.       \tag{4.3}
\]

Delete the owner transition through `L_0=o` and orient the remaining owner
path as

\[
                         T_{W-1},T_{W-2},\ldots,T_0.    \tag{4.4}
\]

Its transition from `T_i` to `T_(i-1)` has root `L_i`.  The phase
`M_0(L_i)=T_i`, together with `M_0(o)=T_0`, is exactly the corrected
terminal endpoint phase: the omitted root lies in the terminal owner
`T_0=T_*`.

Pair consecutive vertices of (4.4) starting at its left end.  If `W` is
even this pairs every owner and ends with `(T_1,T_0)`.  If `W` is odd it
pairs through `(T_2,T_1)` and leaves `T_0` as the sole singleton.  The
paired roots `L_i` have different indices and are therefore distinct.  For
a pair `(T_i,T_(i-1))`, the incidence `L_iT_(i-1)` lies outside `M_0`; the
chosen incidences have distinct lower endpoints and distinct owner
endpoints, so they form an incidence matching.

Contracting the paired two-edge paths in (4.4) preserves its connected path
order and its terminal aperture.  Every paired owner edge has the form
(0.1), so
Corollary 2.2 applies.  For the singleton, the unsaturated nonempty-chain
hinge applies to any assigned strict chain at rank at least three; the
empty-chain formula applies when its payload is empty.  Its owner is `T_*`,
so the corrected endpoint aperture holds.  \(\square\)

The theorem partitions the owner **resource bank** and makes the paired
immediate-lower roots distinct.  It does not assert that the two fixed
chains (2.6)--(2.7) over all pairs partition the complete strict-lower target
bank, nor that the paired immediate-upper colours are distinct or cover the
whole upper shore.  On the support-first PCPS route those questions are
tested after the chronology; on a preassigned triangular chain table they
remain additional common-table constraints.

## 5. The triangular depth is in range

For the odd triangular problem put

\[
 \Lambda=\sum_{s=1}^{r-1}{2r-1\choose s}=4^{r-1}-1,
 \qquad W={2r-1\choose r},                              \tag{5.1}
\]

and let `d` be the least nonnegative integer satisfying

\[
                         dW+{d+1\choose2}\ge\Lambda.    \tag{5.2}
\]

### Lemma 5.1 (uniform room for two-sided layers)

For every `r>=5`, the depth (5.2) satisfies

                              d\le r-3.                 \tag{5.3}

Hence every such triangular instance satisfies the rank hypothesis of
Corollary 2.2.

#### Proof

For `r=5`, `Lambda=255`, `W=126`, and `d=2=r-3`.  For `r=6`,
`Lambda=1023`, `W=462`, and `3W>Lambda`.

For `r>=7`, Vandermonde and Cauchy--Schwarz give

\[
 {2r\choose r}=\sum_{j=0}^r{r\choose j}^2
       \ge {\left(\sum_j{r\choose j}\right)^2\over r+1}
       ={4^r\over r+1}.                                \tag{5.4}
\]

Since `W=(1/2) binom(2r,r)`,

\[
                         {\Lambda\over W}<{r+1\over2}\le r-3. \tag{5.5}
\]

Thus `q=r-3` is already admissible in (5.2), even without its triangular
term.  \(\square\)

## 6. A sharp persistence obstruction

The owner-wide factor of Section 4 must not be mistaken for a spanning
literal chronology.

### Proposition 6.1 (the entering coordinate cannot leave at the next seam)

In the macro (2.3), the coordinate `b` occurs in source position `d+1`.
In any full-`d` continuation of this same literal word, each of the next
`d` owner windows after `T^+` also contains `b`.  In particular, if a
proposed next owner omits `b`, then the macro has no exact-`d` literal port
to that continuation, regardless of the choices `A,A'`.

#### Proof

The owner `T^+` is the window with start one.  Source position `d+1`
belongs to every window whose start lies in `1,2,...,d+1`.  These are
`T^+` and the next `d` owner cells.  Since its letter contains `b`, all
those owners contain `b`.  \(\square\)

This is the local form of the full-row residence condition in PCPS.  An
arbitrary Johnson Hamilton order can violate it at linearly many pair
boundaries.  Pairing owners and constructing rectangles therefore does not
bound the number or total width of deficient intermacro overlaps.

There is a second independent obstruction.  The four-role raw-menu example
in
`MATH_THEOREM_A_UNSATURATED_HINGE_PREDECESSOR_HALL_AND_BOOLEAN_INTERVAL_OBSTRUCTION_20260802.md`
has locally nonempty accepted menus but Hall deficit one; disjoint copies
force arbitrarily many casualties.  Making all owner histories fixed and
all upper-Rado tasks vacuous does not change that predecessor cut.  Thus
zero Boolean/Rado deficiency on each already chosen local block does not
imply global macro balance.

## 7. Exact remaining hypothesis and scope ledger

The construction above closes the following clause unconditionally:

> **Bounded-exception rectangle supply.**  For every odd triangular owner
> bank with `r>=5`, all but at most one prescribed aperture owner can be
> packed into owner-disjoint, root-distinct, two-cell, unsaturated,
> nontrivial two-sided literal rectangles in one Middle Levels predecessor
> phase.  Their owner/lower projection is connected.  After one global
> placement is frozen, arbitrary contiguous-interval PCPS filtering
> preserves Cartesianity, and rooted graphic-Rado selection remains
> independent.

What remains **unproved** is the ambient expansion clause:

1. choose one common owner/target table or one resident PCPS chronology;
2. choose one globally consistent address quotient and propagated aggregate
   history, including all identifications through components shorter than
   `d`;
3. retain nonempty rectangles after every cap, pin, and upper row;
4. reserve a distinct-role connected complete-state skeleton; and
5. make the residual shifted Hoffman deficit nonpositive, or show that the
   total overlap/casualty cost is `O(1)`.

Theorem 4.1 proves that failure of this list cannot be blamed on a lack of
owner-disjoint multi-edge rectangles or on owner parity.  Proposition 6.1
and the predecessor Hall example show that Steps 1--5 do not follow from
that supply.  In particular, no `B+O(1)`, `B+1`, regenerative reset, or
all-dimensional bound for `nu(k)` is claimed here.

## 8. Independent audit target

The companion verifier

`scratch/audit_root_shielded_opposed_hinge_macro_20260802.py`

independently exhausts endpoint cross-products for small ranks and depths,
checks every owner/state/suffix formula, verifies the forward-plus-reversed
hinge identity, checks the left/right/constant classification for every
contiguous interval in padded blocks, replays a fixed signed-history slice,
and checks Lemma 5.1 through rank 100.  Its result and hashes are recorded in
the companion audit note after execution.
