# Guard intervals, global residence cuts, and the exact lower-q1 credit ledger

Date: 2026-08-01  
Status: unconditional abstract theorems.  Their application to a socket bank
still requires a sufficiently spread menu of literal packet completions.
They do not construct the upper-decorated Catalan host or a `k=17` word.

## 1. Residence defects as interval transversals

Fix one owner-path component.  Its possible cuts are the gaps
`1,...,n-1`.  Every internal positive coordinate run of length at most the
depth `h` gives a closed defect interval

\[
                         D=[a,b]                       \tag{1.1}
\]

of gaps: at least one gap of `D` must be cut.  This is the exact interval
stabbing formulation proved in
`MATH_THEOREM_K17_MINIMUM_RESIDENCE_CUT_COLORED_INTERVAL_STABBING_20260801.md`.

An exposed guard segment on owners `[l,r)` forces its two boundary gaps
`l,r` when they are internal to the component, and forbids every gap in its
open interior

\[
                         (l,r)=\{l+1,\ldots,r-1\}.      \tag{1.2}
\]

Call the guard **defect-transparent** when no defect interval is contained
in `(l,r)`.

### Theorem 1.1 (transparent-guard cut completion)

Let `mathcal G` be a collection of defect-transparent guards.  Suppose the
open interiors of any two guards are disjoint, except that identical guards
may be repeated.  Then there is a cut set which:

1. contains every internal guard boundary;
2. contains no point in any guard interior;
3. hits every residence-defect interval.

Identical guards may in particular be shared by one left role and one right
role when their orientations agree.

#### Proof

Let `A` be the set of allowed gaps after deleting all guard interiors, and
include every guard boundary in the provisional cut set.

Suppose a defect interval `D` had no point in `A`.  Since `D` is itself an
interval and the forbidden guard interiors are pairwise disjoint open
intervals, `D` would have to lie inside one connected forbidden interior.
Otherwise it would contain the allowed boundary gap separating two such
interiors.  This contradicts transparency of that guard.

Thus every still-unhit defect interval has an allowed point.  Choose one
such point for each interval, or apply the ordinary rightmost-allowed greedy
algorithm.  The resulting cut set has all three properties. `square`

### Corollary 1.2 (cut-count bound)

Let `tau` be the unrestricted minimum residence-cut number, let `g` be the
number of distinct selected guard intervals, and let `F` be any additional
forced-cut bank disjoint from all guard interiors.  Under the hypotheses of
Theorem 1.1 there is a valid cut set of size at most

\[
                         \tau+2g+|F|.                  \tag{1.3}
\]

#### Proof

Start with a minimum transversal `H` of size `tau`.  For each guard, delete
the points of `H` in its interior and add its at most two internal boundary
gaps.  Any defect interval formerly hit at a deleted point either contains
the left boundary or the right boundary: otherwise it would be contained
in the guard interior, contrary to transparency.  Finally add `F`. `square`

The bound is deliberately crude.  Coincident boundaries, already-present
cuts, and opposite-role sharing only reduce it.

## 2. A global guard-packet allocation theorem

Facet abundance alone does not choose physical guards.  The appropriate
global object is a list of complete packets.

For each task `t`, let `mathcal L_t` be a list of packets.  A packet contains
its already-disjoint facet owners, its oriented left and right guard
intervals, and every forced cut.  Declare two packets to conflict whenever
their simultaneous use would violate any of:

* facet-owner capacity;
* nonidentical guard-interior disjointness;
* a facet or forced cut lying in another guard interior;
* same-role guard endpoint capacity;
* orientation agreement for an identical opposite-role guard;
* any other explicitly typed unit-capacity resource.

### Theorem 2.1 (list-versus-conflict selection)

Suppose every task list has at least `L` packets and every packet conflicts
with at most `Delta` packets belonging to other task lists.  If

\[
                 e\,\frac{2L\Delta+1}{L^2}<1,          \tag{2.1}
\]

then one may choose one packet from every list with no conflict.  The simpler
condition

\[
                         L>3e\Delta                    \tag{2.2}
\]

is sufficient.

#### Proof

Restrict every list to exactly `L` entries and choose one entry uniformly
and independently from each list.  For every conflicting pair of packets in
two different lists, let the bad event be that both are selected.  Its
probability is `1/L^2`.

A bad event involving lists `s,t` is independent of every bad event using
neither list.  The `L` packets in one list have at most `L Delta` conflict
incidences, so the dependency degree is at most `2L Delta`.  The symmetric
Lovasz local lemma gives (2.1), and (2.2) implies it. `square`

### Corollary 2.2 (resource-load form)

Suppose each packet mentions at most `s` typed resources and each such
resource occurs in at most `mu` packets outside a fixed task list.  If every
conflict is witnessed by a common typed resource, then

\[
                         \Delta\le s\mu.               \tag{2.3}
\]

Hence `L>3 e s mu` guarantees a simultaneous packet selection.

For guard intervals of length at most `h`, one may put every owner/gap in the
interval into the packet's resource support.  Then `s=O(h+b+f)`, where `b`
is the number of socket facets and `f` the number of explicit forced cuts.

Combining this with
`MATH_THEOREM_FORBIDDEN_BANK_ROBUST_FACET_SOCKET_ALLOCATION_20260801.md`
gives a clean two-stage sufficient route:

1. allocate disjoint facets while avoiding an independently fixed protected
   owner bank;
2. prove a spread bound `L>3 e s mu` for the remaining literal guard/cut
   completions.

Theorem 1.1 then supplies the global residence cut set automatically.

## 3. A necessary obstruction not seen by facet Hall

No unconditional guard theorem follows from facet abundance alone.  Take two
tasks with disjoint facet blocks, but suppose every legal left-guard
completion for both tasks uses the same oriented physical segment.  That
segment has outgoing capacity one, so the two tasks cannot coexist.

More generally, for any family `X` of guard roles, the union of their legal
role-compatible guard ports must contain at least `|X|` units of capacity.
This is an ordinary Hall obstruction before upper-deck or compiler issues
enter.  The finite `k=17` catalogues exhibit exactly this phenomenon: huge
facet menus can collapse after conditioning on incumbent cuts and guards.

Thus the genuinely missing all-dimensional statement is a **guard-spread
theorem**, not another facet-count theorem.  The list/load hypothesis in
Theorem 2.1 is one quantitative form of that statement.

## 4. Exact lower-q1 cut/credit conservation

The scalar effect of arbitrary refinement cuts and socket seams has a simple
exact form.

Let a rank-`r` owner forest have `W` owners and `E` internal edges.  Assume
the `E` old rank-`r-1` intersection colours are distinct.  Let `K` be a set
of `c` old edges that are cut.  Let `mathcal J` be any bank of new physical
socket/guard seams.  Define `R` to be the number of distinct intersection
colours supplied by `mathcal J` which are not among the retained old
intersection colours.

### Theorem 4.1 (q1 credit ledger)

The number of rank-`r-1` colours not supplied by the retained old edges or
the new seam bank is exactly

\[
                  \boxed{W-E+c-R}.                    \tag{4.1}
\]

#### Proof

The retained old edges supply exactly `E-c` distinct colours.  By definition,
the new seam bank enlarges that colour set by exactly `R`.  Subtracting from
the `W` possible rank-`r-1` colours gives (4.1). `square`

Every distinct cut therefore costs one unit, while every distinct useful new
seam intersection earns one unit.  A repeated new intersection, or one
already present on an uncut old edge, earns no credit.

For a socket with ordered facets `F_1,...,F_L`, its internal bank contains
the `L-1` colours

\[
                  F_1\cap F_2,\ldots,F_{L-1}\cap F_L. \tag{4.2}
\]

Its two guard seams may add two more.  Internal and guard credits must be
deduplicated against each other and against the retained palette before
being inserted into `R`; one may not simply count physical edges.

## 5. The exact k=17 scalar budget

For the authenticated `k=17` SCD forest,

\[
 W=24310,\qquad E=19448,\qquad W-E=4862.              \tag{5.1}
\]

The depth-three lower-cell defect allowance is

\[
 \Delta_{17}=3W+\binom42-\sum_{j=1}^{8}\binom{17}j
            =7401.                                    \tag{5.2}
\]

Consequently, a refined cut/socket bank passes the exact lower-q1 scalar
gate if and only if

\[
              4862+c-R\le7401,
 \qquad\text{equivalently}\qquad
              \boxed{c-R\le2539}.                     \tag{5.3}
\]

The minimum residence refinement has `c=1419` and no socket credit yet, so
its omission bank is `6281` and its remaining scalar reserve is

\[
                       7401-6281=1120.                 \tag{5.4}
\]

For any proposed generalized-cut SAT witness, the proof-safe audit is now
unambiguous:

1. count the distinct selected old gaps `c`;
2. materialize every socket internal and guard seam;
3. form the set of genuinely new rank-eight intersections and count `R`;
4. test (5.3).

This scalar test is necessary for the lower compiler but not sufficient.
The occurrence-labelled common-cap matching, all upper casualties, residence
after the final ordering, and one physical path remain separate gates.
