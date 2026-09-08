# Zero-defect coatom templates: exact local regeneration and the fixed-slot menu quantifier

Date: 2026-08-01  
Lane: L, additive-constant coatom packet  
Status: exact local same-parity template recurrence and exact fixed-incumbent
menu obstruction.  Global Pascal placement, a phase-common compiler bank,
and U5 remain open.  No unconditional additive-constant theorem is claimed.

## 0. Outcome

The mixed coatom-screen tensor has no owner sidecar.  Its local U1--U4
template also regenerates exactly under both possible same-parity deadline
transitions.

Let the parent packet have middle rank `r`, deadline `d`, filler size
`n=d+2`, and

\[
                         |K|=r-d-4.                              \tag{0.1}
\]

At a same-parity step the child rank is `r+1` and
`d' in {d,d+1}`.

* If `d'=d`, put one fresh coordinate into `K`.  Every child owner is the
  cone of its parent owner.
* If `d'=d+1`, put one fresh coordinate into the filler order at an interior
  coatom position.  Every old owner is coned and one new owner is inserted
  into each of the twelve coatom blocks.

Both operations produce the same zero-defect mixed-screen template at the
child parameters.  Thus local owner, immediate-palette, upper-deck,
residence and path-topology state maps exactly to itself.  Only one of the
two new ambient coordinates is used.

This is **template regeneration**, not yet a literal regenerative Pascal
child.  A global proof must still expose a prepared slot in the child
chronology and solve U5 on that same chronology.

The task/menu quantifier has an exact obstruction and a corrected positive
planting row.  After the endpoints, core and filler are fixed, varying the
two remaining active labels gives a quadratic formal catalogue.  But the
incumbent old word itself recovers those two labels, so only one catalogue
member equals one fixed incumbent slot.  The quadratic count is an inventory
of possible planted anchors, not an option list at one anchor.  For the
endpoint-preserving coatom planting, the formerly stated eight screen
schedules are not all palette exact: an exact rotation with transition zero
upper leaves exactly four fully guarded schedules.

## 1. The mixed tensor notation

Use the authoritative active paths `P,Q` and crossed-screen set

\[
                              E=\{1,3,5,7\}.                     \tag{1.1}
\]

For a filler order `F=(f_0,...,f_(n-1))`, every active triple `V` has block

\[
 B_F(V)=\bigl(K\cup V\cup(F-\{f_i\}):0\le i<n\bigr).           \tag{1.2}
\]

At a transition `V->W`, use

\[
 \begin{aligned}
  S^\cap_F(V,W)&=K\cup(V\cap W)\cup F, &&j\notin E,\\
  S^\cup_F(V,W)&=K\cup(V\cup W)\cup(F-\{f_0,f_{n-1}\}),
                                               &&j\in E.
 \end{aligned}                                                  \tag{1.3}
\]

The zero-defect tensor theorem proves that the two phase words are simple,
owner-current, immediate-palette exact, prefix/suffix-OR exact,
internal-deck exact as distinct support, and resident at threshold `d+1`.

## 2. Exact no-jump lift

Let `z` be one of the two fresh child coordinates and suppose `d'=d`.  Put

\[
                          K'=K\cup\{z\},\qquad F'=F.             \tag{2.1}
\]

### Theorem 2.1 (cone lift)

The child phase words are obtained by replacing every parent owner `A` by
`A union {z}`.  They are the mixed coatom tensor at parameters `(r+1,d)`;
all U1--U4 equalities are the cones of the parent equalities.  The new
coordinate is present on the whole fragment, so its clipped residence state
is saturated in both phases.

#### Proof

Equation (2.1) adds `z` to every block and both screen types in (1.2)--(1.3).
Coning preserves symmetric differences, intersections, unions, prefix and
suffix chains, interval-OR support equality, owner distinctness and owner
current.  It raises every owner rank by one.  The trace of `z` is constant
one.  \(\square\)

The second new ambient coordinate is untouched and remains available to the
global Pascal embedding.

## 3. Exact deadline-jump lift

Suppose `d'=d+1`.  Keep `K'=K` and insert one fresh coordinate `z` at the
second filler position:

\[
                  F'=(f_0,z,f_1,\ldots,f_{n-1}).                 \tag{3.1}
\]

The endpoint fillers remain `f_0,f_(n-1)`, so every old screen in (1.3) is
simply coned by `z`.

### Theorem 3.1 (one-coatom insertion lift)

In every active block, cone the old `n` owners by `z` and insert

\[
                             K\cup V\cup F                       \tag{3.2}
\]

after the first coned owner.  Cone every old screen by `z`.  The resulting
word is exactly the mixed tensor at `(r+1,d+1)` with filler order (3.1).
It has all U1--U4 properties and common endpoints equal to the cones of the
parent endpoints.

#### Proof

For an old filler `f_i`, the new coatom is
`(F-{f_i}) union {z}`, hence gives the coned old owner.  The coatom missing
`z` is exactly `F`, giving (3.2).  Around the insertion,

\[
 (F-\{f_0\})+z\ \longleftrightarrow\ F\
 \longleftrightarrow\ (F-\{f_1\})+z
\]

are Johnson steps.  Because `z` is not an endpoint filler, both screen
formulas in (1.3) are coned.  This proves the literal word identity and the
rank/topology claims.  Owner current and all palette/deck equalities follow
from the child tensor theorem (or directly by applying the same insertion
to both phase block sets).

Every internal old active-coordinate run contains a complete active block
and gains the inserted owner there.  An old filler run between consecutive
missing-coatom positions consists of a suffix of one block and a prefix of
the next; the new coatom lies in exactly one of those pieces (the left one
when `p>i`, the right one when `p<=i`), so that run also gains exactly one
positive owner.  Thus every old internal run reaches the child threshold.
The new coordinate is absent once in every block.  Its internal positive
runs have length at least `n`, the child threshold.  At the two fragment
boundaries its clipped state is

\[
                         (\text{leading},\text{trailing})
                              =(1,n-1),                           \tag{3.3}
\]

in both phases.  This is a deterministic structured boundary profile, not
an owner or compiler defect.  It is nevertheless a real placement demand:
to make the two boundary runs globally resident, the exterior must continue
`z` for at least `n-1` positions on the left and one position on the right.
More generally, inserting `z` at coatom position `p` exports the exact
profile `(p,n-p)` and demands complementary continuations `(n-p,p)`.
\(\square\)

There is an additional exact staircase row when one tries to reuse a tight
parent exterior.  Put `D=d+1`, so the parent filler indices are `0<=i<=D`
and their boundary profiles are

\[
                              \beta_i=(i,D-i,0).                  \tag{3.4}
\]

The child threshold is `D'=D+1=n`.  Insertion at position `p` sends old
index `i` to

\[
                 j=i+\mathbf 1_{i\ge p},\qquad
                 \beta'_i=(j,D'-j,0),                            \tag{3.5}
\]

and gives `z` the profile `(p,D'-p,0)`.  Hence an inherited exterior which
was exactly tight must add one left continuation unit for old fillers
`i<p`, and one right continuation unit for old fillers `i>=p`, whenever the
corresponding boundary run is nonempty.  At the canonical `p=1`, all
nonendpoint old fillers need one extra right unit; one exterior owner
containing all of them could discharge this jointly, but its existence is
not a local tensor theorem.

Thus the jump closes phase-neutral U3 and internal residence exactly, while
global regenerative placement must realize the enlarged boundary staircase
(3.4)--(3.5), not merely the fresh-`z` continuation.

Iterating Theorems 2.1 and 3.1 gives a zero-owner-defect local template in
every later same-parity dimension.  It does not show that the global Pascal
construction transports a prescribed task into this slot.

## 4. Exact endpoint-fixed catalogue

Suppress `K,F` and write the active endpoints as

\[
                    V_{\rm left}=\{\infty,a,b\},\qquad
                    V_{\rm right}=\{e,a,b\}.                     \tag{4.1}
\]

The ordered endpoints recover `e`, `infinity`, and the unordered pair
`{a,b}`.  Fix an orientation of `a,b`, and let `R` be the remaining active
label bank, of size `q`.  If the ambient ground set is `Omega`, then

\[
                         q=|\Omega|-r-2,                         \tag{4.2}
\]

because `K union F union {e,a,b,infinity}` has size `r+2`.  Every ordered
pair of distinct labels

\[
                            (c,d)\in R^2,\qquad c\ne d            \tag{4.3}
\]

gives a formally valid active tensor with the same endpoints.  Hence the
formal endpoint-fixed catalogue has size

\[
                              q(q-1).                            \tag{4.4}
\]

This count is genuinely quadratic but has the wrong quantifier for a fixed
incumbent replacement.

### Theorem 4.1 (fixed-incumbent uniqueness)

For fixed `K,F,e,a,b,infinity`, one incumbent old phase word belongs to
exactly one member of (4.4).

#### Proof

In the contracted old active word, the owner at address two is

\[
                              bc=\{e,b,c\},
\]

so it recovers `c`.  The next owner is

\[
                              Cd=\{e,c,d\},
\]

and then recovers `d`.  Expanded coatom blocks recover their active triple
by removing the known `K` and filler coatom.  Thus equality with a fixed
incumbent word forces the same ordered pair `(c,d)`.  \(\square\)

More quantitatively, changing `c` removes the three old active triples
`Ic,Ibc,Ica`; with `c` fixed, changing `d` removes `Ad,Bd,Cd`.  Hence two
distinct formal choices differ in at least three whole coatom blocks, or
`3(d+2)` physical owner positions.  Exchanging `a,b` merely exchanges the
two phases and supplies no additional reversible packet.

Consequently the large planting count in the independent tensor theorem is
an inventory of distinct potential slots.  To become a task list it needs
an actual prepared-slot bank and a task-to-slot matching; abstract
relabelling cannot be used as if all candidates replaced one fixed word.

### Theorem 4.2 (correct endpoint-preserving planting)

Let `G` be the planted common core of size `r-3`.  Choose

\[
 F_0=\{g_0,\ldots,g_d\}\subseteq G,\qquad K=G-F_0,
 \qquad F=F_0\cup\{p\},                                      \tag{4.5}
\]

with fresh `p`.  In blocks two through twelve use missing-filler order

\[
                         (g_0,g_1,\ldots,g_d,p),                 \tag{4.6}
\]

and in the first block use

\[
                         (p,g_1,\ldots,g_d,g_0).                 \tag{4.7}
\]

Thus the first and last tensor owners are the literal original endpoint
owners.  Make transition zero an upper screen (with filler part
`F-{p,g_0}`).  Among all sixteen owner-simple screen schedules, exactly the
following four preserve the owner set, both immediate palettes, the OR
signatures/deck, topology, boundary state and residence:

\[
\begin{split}
 &\{0,2,4,6,8,10\},\\
 &\{0,2,3,4,6,8,10\},\\
 &\{0,2,4,5,6,8,10\},\\
 &\{0,2,3,4,5,6,8,10\}.                                    \tag{4.8}
\end{split}
\]

Consequently a fixed active atom with `P` allowed fresh coordinates has
exactly

\[
                         4P{r-3\choose d+1}                     \tag{4.9}
\]

certified endpoint-preserving planted parameter choices of this form.  For
each planted parameter `(F_0,p)`, let `R_p` be its allowed active-label bank
and put `q_p=|R_p|`.  The exact combined active-label count is

\[
             4{r-3\choose d+1}\sum_p q_p(q_p-1).                \tag{4.10}
\]

It factors as `4P binom(r-3,d+1)q(q-1)` only when all `P` allowed banks have
the same size `q`.  Formula (4.2) is the unrestricted fixed-`p` special
case, not a licence to multiply overlapping marginal reservoirs.

#### Proof

The first owner in (4.7) omits `p`, so it is `G union V_left`; the last
standard block owner also omits `p`, so it is `G union V_right`.  At
transition zero the adjacent block endpoints both omit `g_0`, while the
upper screen omits `g_0,p`; it is one Johnson step from each endpoint.  At
all later transitions (4.6) gives the standard lower/upper bridges.

The finite active/screen table leaves exactly the four schedules (4.8).
For residence, `p` has `d+1` positives between its first-block zero and the
upper screen; `g_0` has consecutive zeros at the last first-block coatom,
the upper screen and the first next-block coatom; all subsequent filler gaps
have the original lower bound `d+1=n-1`.

For the deck row, any interval meeting two screens crosses a complete
`n>=2` coatom block and therefore has filler union `F`; likewise any interval
using at least two cells of one block fills `F`.  Every non-full-`F`
exception is consequently a block singleton, a lower-screen singleton, or
one upper screen with at most one adjacent boundary coatom on each side.
Those values are classified solely by the selected active edge-union and
the common endpoint-missing labels.  This also covers the consecutive upper
screens in two schedules of (4.8).  These statements are replayed
independently for `0<=d<=12`.  \(\square\)

The earlier first-block order `(p,g_0,...,g_d)` with transition zero lower
preserves owner/OR/topology rows but fails the lower immediate palette for
all eight schedules that were claimed compatible.  Thus the factor eight
is valid only for a U1--U4 parameter count with q1 omitted; it is not the
fully guarded planting count.

### Theorem 4.3 (the corrected planted template also regenerates)

The endpoint-preserving template of Theorem 4.2 is closed under both
same-parity transitions.

* If `d'=d`, put fresh `z` into `K` (and hence into `G`).  The child is the
  cone of the entire planted word.
* If `d'=d+1`, put `G'=G union {z}`, `F'_0=F_0 union {z}` and keep `K,p`.
  Use first-block order

  \[
                    (p,g_1,\ldots,g_d,z,g_0)                    \tag{4.11}
  \]

  and standard order `(g_0,...,g_d,z,p)` in the other blocks.  Cone every
  old owner and screen by `z`, and insert the coatom missing `z` at the same
  penultimate address in every block.

The four screen schedules (4.8), the literal original endpoints and every
U1--U4 equality are preserved.  Thus regeneration does not force a return
to the non-planted canonical ordering.

#### Proof

In the no-jump case `z` belongs to every displayed set.  In the jump case
`z` is neither `p` nor `g_0`, the two filler labels omitted by every upper
screen, so all old screens cone.  Both orders in (4.11) are obtained by
inserting the new missing-coatom address immediately before their final
distinguished label.  Hence every old block owner cones and the one new
coatom missing `z` is inserted.  This is the literal child planted tensor,
so Theorem 4.2 applies.  \(\square\)

The exact boundary ledger explains why this is still only local
regeneration.  Put `D=d+1`.  In the parent planted word,

\[
 \beta(p)=(0,0,0),\quad \beta(g_0)=(D,D,0),\quad
 \beta(g_i)=(i,D-i,0)\quad(1\le i\le d).                       \tag{4.12}
\]

At the child threshold `D'=D+1`, the old coordinates have profiles

\[
 \beta'(p)=(0,0,0),\quad \beta'(g_0)=(D',D',0),\quad
 \beta'(g_i)=(i,D'-i,0),                                      \tag{4.13}
\]

and the new coordinate has

\[
                              \beta'(z)=(D,1,0).                \tag{4.14}
\]

Relative to an exactly tight parent exterior, every `g_i`, `1<=i<=d`,
therefore needs one additional left continuation cell; `z` needs one left
and `D` right continuation cells.  The left demands can be shared by one
exterior owner containing all those coordinates, but neither that owner nor
the right `z` collar is supplied by the local theorem.

### Corollary 4.4 (exact prepared-anchor row)

Suppose a physical scaffold contains a family `A` of planted tensor slots
whose complete physical, boundary-capacity and compiler halos are pairwise
disjoint.  Join task `i` to slot `alpha` exactly when switching that literal
slot repairs `i` and passes every declared guard.  Then simultaneous task
embedding is feasible exactly when this task--anchor graph has a
task-saturating matching, equivalently

\[
                       |N(X)|\ge |X|\qquad(X\subseteq T).        \tag{4.15}
\]

Here tasks are unit demands and the interface requires one distinct slot
per task; one switch is not credited against several task vertices.  Under
that injective convention this is ordinary Hall because private atomic
switches commute.  Without
private halos, formal `(c,d)` choices consume multi-owner hyperedges and
ordinary candidate-count Hall is not sufficient.  The exact replacement is
the 0--1 packing system with one selected option per task and capacity one
on every shared halo token.  Already two tasks with two formal candidates
each can fail when all four candidates share one capacity-one owner.  Thus
(4.15) is an exact theorem for actual private slots, not for the raw formal
catalogue (4.4).

## 5. Relation to U5 and global regeneration

The current artifacts still export no physical compiler cell.  Under the
fail-closed convention of the augmented-Hall theorem, their certified
packet list is empty and the isolated packet row has deficiency one.  The
local recurrence above neither worsens nor repairs that row.

The exact remaining all-dimensional statement can now be phrased without
an owner sidecar:

1. prepare a task-Hall-sufficient bank of literal tensor slots in the
   Pascal child;
2. on the same chronology construct the phase-common guarded compiler bank
   and a nonempty certified packet-cell list (or solve the joint augmented
   matching); and
3. ensure that the selected child slots lie in the same template class, so
   Theorem 4.3 remains available at the next step.

The local template satisfies item 3 algebraically.  What remains open is
**physical reachability** of that template through the globally assembled
Pascal chronology, including the complementary fresh-coordinate boundary
continuations and the inherited filler staircase (3.4)--(3.5), together
with items 1--2.  This is the precise difference between template
regeneration and the still-missing regenerative induction.

## 6. Audit

Run

```text
python3 scratch/audit_o1_zero_defect_coatom_template_regeneration_20260801.py
```

The first audit checks all three authenticated active rows for `1<=d<=24`.  It
replays the cone and one-coatom insertion identities literally, then checks
ranks, Johnson adjacency, simple/equal owner sets, endpoints, both immediate
palette multisets, pointwise prefix/suffix OR signatures, complete internal
OR support, residence, the exact new-coordinate boundary state and the full
inherited filler staircase.  It also
enumerates endpoint-fixed active catalogues with `2<=q<=10` and verifies
that every incumbent word recovers its unique ordered `(c,d)` labels.

The independent endpoint audit
`scratch/audit_coatom_endpoint_planting_fixed_slot_hall_20260801.py`
exhausts all screen schedules, checks the four corrected planted patterns,
and replays the planted no-jump/jump recurrence and profiles (4.12)--(4.14)
for `0<=d<=12`.

No staircase placement, task-anchor bank, compiler cell, phase-common
target--cell graph, or U5 certificate is claimed.
