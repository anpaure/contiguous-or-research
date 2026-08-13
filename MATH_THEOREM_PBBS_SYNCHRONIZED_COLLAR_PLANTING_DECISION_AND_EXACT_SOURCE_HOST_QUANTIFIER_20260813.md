# Synchronized PBBS collars: graph planting is decided, and source planting is an exact pinned-erosion fibre

**Date:** 2026-08-13  
**Status:** unconditional decision theorem obtained by combining the audited
height-pentagon endpoint identities, global missing-tag construction,
protected-factor extension, and the exact pinned-antecedent criterion.  The
endpoint-corrected collar bank has a collision-free simple directed graph
host.  The literal all-five incoming-collar bank used for zero complete
upper current cannot be such a host because it has forced owner degree
three.  Moreover, the endpoint-corrected graph face retains the direct
height spine and therefore has forced positive runs shorter than the target
aperture in the intended range; it is **not** a resident source host.  The
pinned-erosion criterion below remains the exact general source test, but
the current corrected face fails its preliminary residence row.  No
typed-cap claim is made.

## 0. Verdict

Let the PBBS height-pentagon ladder use heights `4<=h<H`, with

\[
                     H=O(\sqrt r),\qquad
                     \delta=O(\sqrt r).               \tag{0.1}
\]

There are three different assertions which must not be conflated.

1. The **interiors** of all synchronized collars can be selected with no
   owner or lower-colour collision.  The common missing-tag reservoir proves
   this directly.
2. The independent **all-five incoming-collar** bank cannot be an incidence
   path forest: adjacent heights force a third protected edge at one owner.
   Consequently neither a halo-disjoint packing theorem nor a protected
   Ore extension theorem can plant that bank as stated.
3. After the endpoint correction (four incoming collars and one outgoing
   role-zero collar per height), the complete graph-level bank, its
   rank-stratified upper backups, and its oriented component connectors can
   be planted in one simple directed spanning two-factor.  This corrected
   face is nevertheless not a source candidate when `d>=4,H>=9`: its
   retained height spine already contains a protected positive run of
   length four.  A resident architecture must delete or dilate those spine
   edges before applying the exact erosion test in Section 4.

Thus the strongest exact-current route and the strongest presently proved
graph-host route are different faces.  A shared adjacent-height collar or
an alternating lift of the three-edge zero-seam ear would be needed to make
them the same face.

## 1. The forced endpoint collision

Use the standard high-pentagon notation

\[
 P_{h,i}Q_{h,i}\longleftrightarrow P_{h,i}Q_{h,i+1}
 \qquad(i\in\mathbb Z_5),                           \tag{1.1}
\]

and put

\[
 A_h=0\,1^h0^h(10)^{r-h},\qquad U_h=A_h^c.          \tag{1.2}
\]

The literal PBBS successor calculation gives, for adjacent high heights,

\[
                 \boxed{P_{h,0}=Q_{h-1,1}=U_h.}     \tag{1.3}
\]

After the simultaneous head shifts, the role-zero return edges form the
height spine

\[
                 \cdots-U_{h-1}-U_h-U_{h+1}-\cdots.\tag{1.4}
\]

Hence the two protected factor degrees at `U_h` are already occupied.
The explicit incoming synchronized collar at role zero ends at
`P_(h,0)=U_h` and has a first interior owner with its private missing-tag
signature.  Its incident edge is therefore different from both all-tag
spine edges.

### Theorem 1.1 (all-five degree-three obstruction)

For every internal adjacent-height seam, the independent all-five
incoming-collar bank has protected owner degree at least three at `U_h`.
It is not an incidence path forest and is contained in no simple spanning
two-factor.

#### Proof

Equation (1.4) contributes two distinct protected edges at `U_h`.  The
role-zero incoming collar contributes a third distinct edge by its
missing-tag signature.  A simple two-factor has owner degree two, giving
the contradiction.  \(\square\)

This theorem does not rule out a **fused** collar which reuses or replaces
one spine incidence.  It rules out treating the displayed independent
collars as disjoint packets.

## 2. Why generic halo packing and Ore extension do not fix (1.3)

The subexponential halo-packing theorem assumes that every named role of a
packet ranges uniformly over a stabilizer orbit of size

\[
                         2^{n-o(n)}.                 \tag{2.1}
\]

For a collar required to end at the literal PBBS owner `P_(h,i)`, the
endpoint role is fixed.  Its admissible orbit in this embedding problem has
size one.  More decisively, (1.3) says that the endpoint halos of two
adjacent-height packets have a mandatory common resource in every allowed
embedding which preserves the ladder.  Therefore the pairwise halo-disjoint
conclusion is false for the complete all-five halos, independently of any
probability estimate.

The polynomial protected-forest theorem begins with a vertex-disjoint
owner-path forest of maximum protected degree two.  It proves that such a
forest extends after its size and two exposures are bounded.  It does not
choose packet embeddings and cannot lower the degree three in Theorem 1.1.
Thus its use in the complete-current collar theorem is logically
conditional on a planting premise which the literal all-five bank fails.

The global missing-tag theorem does close the part that is actually a
packing problem.  With

\[
 \mathcal P=\{(h,i):4\le h<H,\ i\in\mathbb Z_5\},
 \qquad |\mathcal P|=5(H-4),                         \tag{2.2}
\]

the common reservoir has size `r-H`.  Under (0.1), it supplies one private
tag per collar.  Every positive collar owner and every collar lower colour
then omits exactly its own tag, so all collar interiors are mutually
resource-disjoint and avoid the all-tag pentagon bank.  The only failure is
the forced endpoint incidence (1.3).

## 3. The graph-level endpoint-corrected theorem

At each high height, retain incoming collars at roles `1,2,3,4`, omit the
incoming role-zero collar, and put one full-union collar after the free old
head `Q_(h,0)`.  The endpoint audit proves that this is a protected incidence
path forest before and after the head shifts.  Its high bank has

\[
 e=10(H-4)(r+4)+O(1)=O(r^{3/2}),                   \tag{3.1}
\]

and the proof-safe exposure bounds

\[
 \alpha\le85(H-4)+O(1),\qquad
 \beta\le30(H-4)+O(1).                              \tag{3.2}
\]

The missing role-zero incoming profile leaves a prospectively fixed upper
target bank.  At every excess rank its size is

\[
                         O(Hr)=O(r^{3/2}).           \tag{3.3}
\]

The rank-stratified backup theorem selects mutually resource-disjoint
owner-path witnesses for all those targets, keeps the aggregate exposures
below a fixed half-degree margin, and uses only polynomially many
incidences.  The global tagged-port construction joins every forced
oriented component into one protected path.  The polynomial protected-
forest theorem then supplies a simple spanning two-factor, which can be
oriented consistently on that path.

### Theorem 3.1 (graph planting is closed on the corrected high face)

For all sufficiently large `r` under (0.1), there is a simple directed
owner/lower-`q1` spanning two-factor containing simultaneously:

1. the endpoint-corrected high-height pentagon collar forest for
   `4<=h<H`;
2. one protected alternative owner-path witness for every target in the
   rank-stratified residual upper bank; and
3. all forced pentagon pieces in one consistently oriented protected
   component.

The bounded heights `2,3` may be omitted and paid as a bounded terminal
bank.  They may be included only after a separately checked compatible
bounded planting; the common high tag reservoir does not automatically
separate an arbitrarily frozen low-height realization.

#### Proof

The missing-tag construction gives the incidence path forest and
(3.1)--(3.2).  Enlarge the common high reservoir before selecting the
collar deletion sets by one fresh tag for every otherwise untagged free
component endpoint.  One-tag whiskers and pair-tag geodesics then join the
`O(H)` forced components without resource collisions and add only `O(Hr)`
incidences and `O(H)` exposure.  Treat this enlarged forced path as the
forbidden base in the rank-stratified backup theorem.  It gives item 2,
keeps the union an incidence path forest, and leaves a fixed sub-half
aggregate exposure.  The polynomial protected-forest theorem extends the
resulting forest to a simple spanning two-factor.  Orient the factor cycle
containing the one forced path in its prescribed direction and orient all
other cycles arbitrarily.  Since the backup paths were not pre-oriented,
they impose no conflicting cycle orientation.  \(\square\)

Theorem 3.1 is a graph theorem.  It replaces exact zero exterior current by
explicit alternative witnesses.  It neither gives a source antecedent nor
implies that the unprotected completion is resident.

There is in fact an exact residence obstruction on this graph face.  The
retained role-zero edge is

\[
 e_h=U_hU_{h+1},
 \qquad U_{h+1}=U_h-\{h+1\}+\{2h+1\}.
\tag{3.4}
\]

For every `h>=4`, coordinate `2h+1` is absent from `U_h`, present exactly
on `U_(h+1),...,U_(2h)`, and absent from `U_(2h+1)`.  If `2h<H`, both
boundary edges are protected and this is a maximal positive run of length
`h`.  Hence whenever `4<=h<=d` and `2h<H`, the required aperture
`q=d+1` is impossible.  In particular `d>=4,H>=9` already fails at `h=4`.
No choice of completion, long arms, or source pins changes that protected
membership trace.  See
`MATH_OBSTRUCTION_PBBS_ENDPOINT_CORRECTED_SPINE_HAS_FORCED_SHORT_RUNS_20260813.md`.

## 4. Exact source-host criterion

The remaining quantifier can be written with no hidden source-word search.
Let `T=(T_i)` be any cyclic oriented owner trace and let `q>=1` be the owner
window width (`q=delta+1` in the collar application).  Define the safe
emission envelope

\[
 K_j=\bigcap_{a=0}^{q-1}T_{j-a}.                    \tag{4.1}
\]

Let `D` be a set of source positions and prescribe an exact nonempty source
letter `W_j` at every `j in D`.  For a coordinate `x`, put

\[
 E_x=\{j:x\in K_j\},\qquad
 Z_x=\{j\in D:x\notin W_j\}.                       \tag{4.2}
\]

### Theorem 4.1 (pinned-erosion equivalence)

There is a cyclic word of nonempty source letters `(A_j)` satisfying

\[
 A_j=W_j\quad(j\in D),\qquad
 T_i=\bigcup_{j=i}^{i+q-1}A_j\quad(i\in\mathbb Z_W) \tag{4.3}
\]

if and only if all three conditions hold:

\[
                         W_j\subseteq K_j
                         \qquad(j\in D),             \tag{4.4}
\]

\[
 [i,i+q-1]\cap(E_x\setminus Z_x)\ne\varnothing
 \qquad(i\in\mathbb Z_W,\ x\in T_i),               \tag{4.5}
\]

and

\[
                         K_j\ne\varnothing
                         \qquad(j\notin D).          \tag{4.6}
\]

When these conditions hold, the coordinatewise maximal completion

\[
 A_j=\begin{cases}
       W_j,&j\in D,\\
       K_j,&j\notin D
     \end{cases}                                      \tag{4.7}
\]

is a solution.

#### Proof

If `x in A_j`, every owner window containing source position `j` must
contain `x`, so `A_j subseteq K_j`; this gives (4.4), and nonempty unpinned
letters give (4.6).  If `x in T_i`, some source position
`j in [i,i+q-1]` must emit it.  That position is safe (`j in E_x`) and,
when pinned, cannot forbid `x` (`j notin Z_x`).  This proves (4.5).

Conversely use (4.7).  Equations (4.4) and (4.1) ensure that no selected
source occurrence introduces a coordinate into a forbidden owner.  Equation
(4.5) covers every positive owner incidence.  Equations (4.4), (4.6), and
the nonemptiness of the prescribed letters make every source letter
nonempty.  Therefore all equalities in (4.3) hold.  \(\square\)

For a `q`-resident rank-`R` Johnson trace with `R>=q`, the unpinned envelopes
are nonempty and cover every owner.  Pins can still violate (4.4) or (4.5).
Those two rows are exactly the anticipatory source-history constraint which
owner-level packet planting does not see.

## 5. Applying the criterion to the pentagon bank

For every common-history pentagon fragment, the prescribed pin block is

\[
                 (X_i,C_1,\ldots,C_\delta,Y_i).     \tag{5.1}
\]

The synchronized collars, stretched half-edges, and clipped boundary
adapters contribute their own exact source letters.  Put all of these
positions in `D`.  Then:

* (4.4) says that every screen/history letter survives throughout its full
  incoming owner-of-source halo;
* (4.5) says that the combined pins do not erase the last safe emission of
  any owner incidence; and
* cut separation says that the complete right paths can be permuted without
  interleaving displayed left blocks.

These are literal occurrence conditions, not marginal owner, palette, or
exposure conditions.

Long one-tag arms can place distinct local pin blocks more than `q` source
positions apart.  In that case no length-`q` source window meets two local
pin blocks, so every *owner window and envelope containment* test is local
to one complete `q-1` halo.  The coordinate-coverage tests (4.5) are also
closed by the separated-short-block freedom lemma **provided** every pin
block has length at most `q-1`, every prescribed letter lies between its
forced set and maximal envelope, and at least one unaltered maximal source
position separates consecutive blocks.  Indeed the maximal source support
of one coordinate is a carrier interval; one legal block can erase at most
`q-1` consecutive nonforced support positions, and the retained maximal
separator prevents erasures in two blocks from joining into a support gap
longer than `q`.  Thus under these local containments and separators,
(4.5) follows automatically.

This removes a cross-height Hall condition; it does **not** prove the local
containments.  In particular a complete pentagon pin fragment has length
`q+1`, not at most `q-1`, and must be decomposed into legal short blocks or
checked directly on its full halo.  Nor does the graph-level completion
theorem make its owner trace resident or supply maximal separators.

### Corollary 5.1 (the exact surviving source-host assertion)

To lift Theorem 3.1 to the literal synchronized-collar source face, it is
necessary and sufficient to choose its simple directed factor and the
occurrence positions of all declared pin blocks so that:

1. every positive owner run has length at least `q` (and every zero run has
   length at least `q` when biresidence is required);
2. the pin blocks are cut-separated and satisfy (4.4)--(4.6); and
3. the required factor components are ordered through the declared long
   arms, so the local pin halos are the ones used in those tests.

Under these conditions, (4.7) gives a literal antecedent on every completed
factor cycle, and the protected cycle carries all declared pins; the
common-history occurrence bijections transport every strict-lower cell on
that protected chronology.  Turning the componentwise antecedents into one
global cyclic source word still requires common-history fusion of the
unprotected factor cycles (or a completion theorem producing one cycle).

#### Proof

Positive residence gives the unpinned antecedent row cycle by cycle;
Theorem 4.1 is the exact extension test for all prescribed letters.  Cut
separation permits the common-history path permutations on the protected
cycle, and their strict-lower occurrence bijections then apply.  Necessity
follows from the same facts in reverse.  Fusion into one source chronology
is an additional topology/history condition, not part of the
coordinatewise erosion equivalence.  \(\square\)

The polynomial protected-factor theorem supplies none of items 1--3: its
unprotected cycles and edges have unrestricted chronology.  The
subexponential halo theorem likewise controls set-resource collisions, not
the safe-emission sets (4.2).  This is the precise source-host quantifier
which remains open.

## 6. Boundary after this decision

The graph layer is now proof-safe:

\[
\boxed{
\text{endpoint-corrected protected bank}
\;\Longrightarrow\;
\text{simple directed two-factor with all named upper backups}.}
\]

The exact-current all-five face is blocked at (1.3), before Ore extension.
The literal-source face is blocked earlier by the protected short-run
obstruction after graph extension; Corollary 5.1 becomes operative only on
an architecture which deletes or dilates those spine edges.
Even if Corollary 5.1 is solved, the occurrence-labelled typed suffix cap
still requires its own common Rado/gammoid rank theorem; missing-tag privacy
does not imply that rank.

The two constructive ways past the endpoint obstruction which remain
compatible with the current algebra are:

1. a shared adjacent-height collar which reuses a spine incidence while
   retaining the common cumulative-union profile; or
2. an alternating physical lift of the minimal three-edge zero-seam repair
   ear, followed by the long synchronized collar.

Neither follows from halo packing or protected Ore extension.
