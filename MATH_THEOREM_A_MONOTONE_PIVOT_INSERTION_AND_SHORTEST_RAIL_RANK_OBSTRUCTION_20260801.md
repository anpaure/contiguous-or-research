# Monotone pivot insertion: exact compiler transport and the shortest-rail rank obstruction

Date: 2026-08-01  
Lane: A, additive-constant terminal compiler  
Status: exact local theorem.  A monotone inserted source gives a genuine
zero-loss transport of the unrestricted interval deck and, under an exact
matching-alignment condition, zero residual `COMP_h` damage.  However it
cannot be inserted into the canonical shortest rotating-hole erosion when
`h>=2`: an internal new owner has rank one too small.  No obstruction to a
noncanonical pivot-rich Pascal source is claimed.

## 0. Outcome

Insert a nonempty source letter `X` at an internal cut of a source word.
If

\[
                         X\subseteq A_{-1}\cup A_1,       \tag{0.1}
\]

then every old interval has a canonically enlarged interval with exactly
the same OR.  The cells not used by this transport are precisely the two
new rays ending at the inserted letter, with their singleton shared.
Consequently prescribed left and right target chains admit an exact
one-letter common cap if and only if they are the literal prefix unions on
those rays.  This has a one-row/one-coordinate maximal-word formulation.

There are two qualifications.

1. In the width-`h` compiler, an old crossing cell of width exactly `h`
   is transported to width `h+1`, hence outside `COMP_h`.  A fixed
   reference matching has zero residual loss under the canonical transport
   exactly when every such matched target is among the targets rehosted on
   the two new rays (or is otherwise explicitly rematched).
2. The new depth-`h` middle owners through the inserted letter are the
   complementary joins of the two ray chains.  They must have the middle
   rank and must be distinct when the carrier is simple.  In the canonical
   shortest-rail erosion `W_j=K+z_j`, every internal complementary join has
   rank `m-1`, not `m`.  Thus the proposed monotone pivot fails before the
   compiler matching is considered.

This separates the three ledgers exactly:

\[
\begin{array}{c|c}
\text{unrestricted old OR deck}&\text{zero loss under (0.1)}\\
\text{width-}h\text{ matching}&\text{one }(h-1)\text{-cell boundary face}\\
\text{flat middle carrier}&\text{complementary-join rank/distinctness}.
\end{array}                                                \tag{0.2}
\]

## 1. Exact interval transport

Let a nonzero word be indexed near an internal cut by

\[
       \ldots,A_{-2},A_{-1}\mid A_1,A_2,\ldots .          \tag{1.1}
\]

Insert `A_0=X`.  For an old interval `I`, let `phi(I)` be the interval in
the new word obtained by preserving its old endpoints: intervals on the
right are shifted by one, and an interval crossing the cut is enlarged to
include position zero.

### Theorem 1.1 (monotone insertion transport)

Every old interval keeps its OR under `phi` if and only if (0.1) holds.
Moreover, the intervals of the new word outside the image of `phi` are
exactly

\[
 [-t,0]\quad(t\ge0),\qquad [0,t]\quad(t\ge0),             \tag{1.2}
\]

where the two lists share `[0,0]`.

#### Proof

An old interval not crossing the cut has the same letters after the index
shift.  A crossing interval gains only `X`; hence its new OR is its old OR
union `X`.  Every crossing interval contains both adjacent letters, so
(0.1) is sufficient.  Applying the claimed equality to the minimal
crossing interval `{A_{-1},A_1}` proves necessity.

An interval containing zero and letters on both sides is the image of the
old interval obtained by deleting zero.  An interval avoiding zero is the
image of a one-sided old interval.  The remaining intervals contain zero
and use at most one side, which are exactly (1.2).  \(\square\)

For `t>=0`, put

\[
 B^-_t=\bigcup_{s=1}^tA_{-s},\qquad
 B^+_t=\bigcup_{s=1}^tA_s,\qquad B^-_0=B^+_0=\varnothing . \tag{1.3}
\]

The two new ray values are

\[
                    L_t=X\cup B^-_t,\qquad
                    R_t=X\cup B^+_t.                     \tag{1.4}
\]

### Corollary 1.2 (exact one-letter ray/common-cap criterion)

Let `T^-_t,T^+_t` be prescribed values on selected left and right ray
cells, and let `P_0` be the cap at the inserted position.  A nonempty `X`
satisfying (0.1) and all prescribed ray equalities exists if and only if

\[
 B^\sigma_t\subseteq T^\sigma_t\quad(\sigma\in\{-,+\}),  \tag{1.5}
\]

and there is a nonempty set in the interval

\[
 \boxed{
 \bigcup_{\sigma,t}(T^\sigma_t-B^\sigma_t)
 \ \subseteq X\subseteq\
 P_0\cap(A_{-1}\cup A_1)\cap
             \bigcap_{\sigma,t}T^\sigma_t .}             \tag{1.6}
\]

If the singleton is a typed task, `X=S_tau`, the criterion is simply

\[
 S_\tau\ne\varnothing,\quad S_\tau\subseteq P_0\cap
 (A_{-1}\cup A_1),\quad
                  S_\tau\cup B^\sigma_t=T^\sigma_t       \tag{1.7}
\]

for every prescribed ray.

#### Proof

The equality `X union B=T` is equivalent to the three inclusions
`B subseteq T`, `T-B subseteq X`, and `X subseteq T`.  Intersecting them
over all rows and adjoining the cap, monotonicity and nonemptiness gives
(1.5)--(1.6).  The typed case fixes `X` and gives (1.7).  \(\square\)

This is exactly the one-live-position specialization of the fixed-`H`
common-`Q` theorem.  If the old letters are also live under larger caps,
one appends all transported old equalities and ray equalities to that
theorem.  The displayed inserted word is a feasible witness, so the
componentwise maximal word is feasible as well.  Thus no additional signed
or subset-Hall condition is hidden here.

## 2. The precise `COMP_h` matching boundary

Restrict cells to intervals of at most `h` source positions.  Under `phi`,
a crossing interval of old width `ell` has new width `ell+1`.  Hence the
only old cells not canonically transported inside `COMP_h` are the

\[
                             h-1                            \tag{2.1}
\]

crossing cells of width exactly `h`.  The new width-`h` cells outside the
old image are the `2h-1` ray cells

\[
 [0,0],\quad[-t,0],[0,t]\quad(1\le t\le h-1).             \tag{2.2}
\]

Thus the band count changes by `(2h-1)-(h-1)=h`, as it must.

### Theorem 2.1 (zero-residual direct matching criterion)

Let `M_0` be a matching from a target set `S` to old `COMP_h` cells.  Let
`R subseteq S` be a family of pairwise distinct targets prescribed
bijectively on non-singleton cells in (2.2), and prescribe a new target
`tau notin S` at `[0,0]`.  Assume (0.1), the literal ray equalities, and
that

\[
 \boxed{\text{every target whose }M_0\text{-cell crosses the cut with
 width }h\text{ belongs to }R.}                            \tag{2.3}
\]

Then the plus word has a matching saturating `S union {tau}`: remove the
`M_0` edges of targets in `R`, put those targets on their prescribed ray
cells, transport every other `M_0` cell by `phi`, and put `tau` at the
singleton.  In particular the residual compiler damage is zero.

Within this fixed architecture (canonical transport plus the prescribed
ray rehosting), condition (2.3) is also necessary.

#### Proof

After removing the edges indexed by `R`, condition (2.3) says that every
remaining crossing cell has old width at most `h-1`; its image therefore
lies in `COMP_h`.  Theorem 1.1 preserves its target.  Transported cells are
pairwise distinct.  They either avoid zero or use both sides of zero,
whereas the cells (2.2) use at most one side; hence the two cell families
are disjoint.  Distinctness of the prescribed target family and
`tau notin S` gives target disjointness.  The displayed union is therefore
a matching saturating all claimed targets.

Conversely, a retained width-`h` crossing edge has no canonical image in
`COMP_h`, so this architecture must remove and rehost its target.  This is
(2.3).  \(\square\)

The theorem is deliberately not a claim that an arbitrary width-`h`
crossing target has no other plus witness.  Allowing arbitrary rematching
replaces (2.3) by the literal Hall condition in the final plus incidence
graph.  The point is that monotonicity alone gives no such alternate
witness.

## 3. The exact middle-owner condition

The new depth-`h` windows containing zero are indexed by the number `i` of
old positions taken on the left:

\[
 O_i=X\cup B^-_i\cup B^+_{h-i},\qquad0\le i\le h.          \tag{3.1}
\]

Equivalently, extending (1.4) to `t=h`,

\[
                         O_i=L_i\cup R_{h-i}.              \tag{3.2}
\]

### Theorem 3.1 (complementary-join carrier criterion)

Keeping every old source letter fixed, the monotone insertion extends an
old depth-`h` carrier to a prescribed new carrier if and only if its
`h+1` new owners at the cut are the sets (3.1).  A flat rank-`m` carrier
therefore requires

\[
                         |O_i|=m\quad(0\le i\le h),         \tag{3.3}
\]

and a simple chronology also requires these owner occurrences to be
pairwise distinct from each other and from the retained owners.

For `1<=i<=h-1`, monotonicity makes `X` redundant in (3.1), so

\[
                 O_i=B^-_i\cup B^+_{h-i}.                 \tag{3.4}
\]

#### Proof

Formula (3.1) lists exactly the `h+1` consecutive letters of each new
window meeting zero.  Windows avoiding zero are unchanged, up to the index
shift.  This proves necessity and sufficiency.  An internal window contains
both adjacent old letters, so (0.1) implies (3.4).  Rank and simplicity are
then immediate.  \(\square\)

This condition is separate from Corollary 1.2.  Two perfectly legal
compiler rays need not have legal complementary middle joins.

### Corollary 3.2 (complementary coatom chains repeat the middle owner)

Suppose the ray targets are the complementary flag chains

\[
 L_i=J\cup\{a\}\cup\{g_1,\ldots,g_i\},\qquad
 R_j=J\cup\{b\}\cup\{g_{h-j+1},\ldots,g_h\}.             \tag{3.5}
\]

Then for every `1<=i<=h-1`,

\[
                         O_i=J\cup\{a,b\}\cup G.          \tag{3.6}
\]

Hence for `h>=3` the local owner chronology repeats an owner.  The ray
common-cap equalities may all be feasible, but a simple flat carrier is
not.

#### Proof

The prefix of length `i` and suffix of length `h-i` partition `G`.
Substitute (3.5) in (3.2).  \(\square\)

## 4. The canonical shortest rail forbids a monotone pivot

Use the exact erosion of the shortest rotating-hole rail.  Thus

\[
 W_j=K\cup\{z_j\},\qquad |K|=m-h-1,                       \tag{4.1}
\]

where the active labels have cyclic period `h+3`, and every depth-`h`
owner is the union of `h+1` consecutive `W_j`.

### Theorem 4.1 (rank-one-short obstruction)

Let `h>=2`, cut a linear unrolling of (4.1) between two consecutive source
positions, and insert a nonempty `X` satisfying the monotone condition
(0.1).  Then every internal new depth-`h` window through zero has rank

\[
                              m-1,                          \tag{4.2}
\]

so the inserted word is not a flat rank-`m` preimage.  This holds for every
choice of the rail parameters and every typed task contained in `X`.

#### Proof

For `1<=i<=h-1`, the old part of the corresponding window consists of `h`
distinct source positions from a cyclic word of period `h+3`.  Its union
is `K` plus `h` distinct active labels and therefore has size

\[
                         |K|+h=(m-h-1)+h=m-1.              \tag{4.3}
\]

It contains both source letters adjacent to the cut.  By (0.1), adding
`X` changes no coordinate of that union.  Formula (3.4) therefore gives
(4.2).  Since `h>=2`, at least one internal index exists.  \(\square\)

The smallest case is `h=2`: if the adjacent erosion letters are
`K+u,K+v`, every monotone `X subseteq K+u+v` leaves the new three-letter
window equal to `K+u+v`, of rank `m-1`.

### Corollary 4.2 (sharp scope of the monotone-pivot proposal)

One inserted monotone letter can give a complete cap with zero residual
compiler damage only after an additional **pivot-richness** hypothesis:
all complementary joins (3.1) must be the prescribed rank-`m` owners, and
condition (2.3) (or the exact residual Hall replacement for it) must hold.
The canonical shortest-rail erosion violates pivot-richness for every
`h>=2`.

Thus monotone insertion is a valid positive compiler lemma, but it is not
the missing bridge for the frozen shortest rail.  A successful rail
construction must do at least one of the following:

* use a noncanonical source whose `h`-letter complementary joins already
  have rank `m` and the required distinctness;
* let `X` introduce a genuinely new coordinate, abandoning monotonicity
  and paying/repairing the affected old crossing witnesses; or
* combine several insertions/rethreads so the middle-rank gain and the
  compiler return occur in different local faces.

## 5. Scope audit

1. Theorem 1.1 concerns interval-OR coverage, not residence, owner degree,
   q1 palettes or upper chronology.
2. Theorem 2.1 is an exact matching construction, but its necessity is only
   for the stated canonical-transport architecture.  Arbitrary residual
   rematching is governed by Hall.
3. Theorem 4.1 uses the explicit canonical erosion (4.1), not every possible
   common-`Q` source for the same middle rail.
4. No asymptotic or all-`k` impossibility is claimed.  Historically the
   surviving local gate was a pivot-rich noncanonical source plus cap
   satisfying (1.6), (2.3) and (3.1) simultaneously.  The noncanonical
   pivot-rich geodesic packet has since been constructed in
   `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`.
   Only its ambient protected-host/common-cap integration remains open;
   the local packet itself is no longer a missing lemma.
