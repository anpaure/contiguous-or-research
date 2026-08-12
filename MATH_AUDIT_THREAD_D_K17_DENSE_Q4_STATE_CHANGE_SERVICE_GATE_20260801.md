# Dense k=17 refinement: the exact q4 state-change service gate

Date: 2026-08-01  
Lane: Thread D, independent mathematical/source audit  
Status: fixed-endpoint no-go proved; exact live q4 class and replay test stated

## 1. Frozen dense bank and its two defect families

Let `F` be the authenticated degree-two rank-8/rank-9 incidence factor and
let `C` be the 7,612 selected cut-lower set from

`scratch/k17_joint_extra_cut_support_sat_20260801.selected_cuts.tsv`.

Deleting the lower vertices in `C` and their incident factor edges gives
7,612 owner paths.  Their two orientations give 15,224 endpoint states.
For an oriented state `s`, the stored endpoint summary is

`(first,last,length,all[17],prefix[17],suffix[17])`,

where prefix and suffix lengths are truncated at four.

The complete relaxed atomic atlas consists of every triple `(s,t,c)` such
that

1. `s` and `t` are orientations of different physical pieces;
2. `last(s) != first(t)`;
3. `last(s) & first(t) = c`, with `c in C`;
4. the exact two-block necessary predicate `relaxed_pair_resident(s,t)`
   holds.

It has 243,424 triples.  There are two exact defect families:

- 78 rank-10 masks have neither an internal provider nor any relaxed seam
  provider;
- 187 physical pieces have no orientation with both nonempty relaxed
  outgoing and incoming menus.

The latter count follows from the printed state census, not an additional
search.  Reversal sends every atlas triple `(s,t,c)` to
`(rev(t),rev(s),c)`, so a tail-dead state is paired with a head-dead opposite
orientation.  There are 187 tail-dead and 187 head-dead states, while no
physical piece is tail-dead or head-dead in both orientations.  Hence the
dead states lie on 187 distinct pieces and each such piece has one
tail-dead orientation and the opposite head-dead orientation.

Thus the immediate local objective has 265 rows: 187 common-orientation
rows plus 78 rank-10 rows.

## 2. Endpoint-preserving switches cannot serve either family

### Lemma 2.1 (complete-atlas monotonicity)

Let `A` be the complete relaxed endpoint-state atlas above.  Replacing one
selected seam matching by another matching contained in `A` cannot give a
provider to a zero row of `A`.

This is tautological but decisive: a seam C8/q4 switch merely replaces four
chosen triples by four other triples from the same complete atlas.  It does
not create a new endpoint state or a new atom.

Consequently:

1. all 78 rank-10 zero-provider rows remain zero; and
2. all 187 common-orientation rows remain impossible.

This rules out **every endpoint-preserving seam switch**, not merely the
currently selected matching or one orientation convention.

## 3. The exact underlying-factor q4

Let `K` be a rank-7 core and let `p_0,p_1,p_2,p_3` be four distinct
coordinates outside `K`, cyclically ordered.  Put, modulo four,

`L_i = K + p_i`,

`O_i = K + p_i + p_(i+1)`.

The two incidence-C8 phases are

`M_old = {(L_i,O_i): i=0,1,2,3}`

and

`M_new = {(L_i,O_(i-1)): i=0,1,2,3}`.

A legal factor toggle requires:

- all four old incidences are selected in `F`;
- all four new incidences are absent;
- no removed old incidence is protected.

Then

`F' = F - M_old + M_new`

is again a simple degree-two Boolean incidence factor.  Unlike the earlier
component-fusion census, a dense-service q4 must **not** require the four old
edges to lie on four distinct factor components.  Its purpose is state
change, not necessarily component fusion.

## 4. Exact cut-pattern criterion

Write `chi_i=1` when `L_i in C`, and let `P(F,C)` be the owner-path graph
obtained by deleting every lower vertex in `C` and all its incidences.
Restriction of the q4 identity to this graph gives

`E(P(F',C)) triangle E(P(F,C))`

equal to the old/new q4 incidences at exactly those indices with `chi_i=0`.
Therefore:

### Theorem 4.1 (state-change criterion)

`P(F',C)=P(F,C)` if and only if `chi=(1,1,1,1)`.

If all four q4 lowers are cut, the factor toggle changes only incidences
which are deleted before pieces are formed.  The owner words, endpoint
states, internal upper deck, complete relaxed atlas, 187 availability
defects, and 78 rank-10 defects are all literally unchanged.

If at least one q4 lower is internal, the path graph changes because its old
and new owner endpoints are distinct.  Physical owner words must then be
rebuilt.  Their coarse endpoint summaries may occasionally coincide, but
they may not be reused without replay.

Thus an underlying factor C8 with at least one internal lower is the
smallest live class **within q4**.  This statement does not exclude a C6,
balanced cut relocation, or larger packet in a different class.

### 4.1 Cut pattern does not determine rank-10 current

Let `A_i` be the unchanged other owner incident with `L_i`.  For every
internal q4 lower, the old and new internal rank-10 colours are

`U_i=A_i union O_i`,

`V_i=A_i union O_(i-1)`.

Hence the exact internal current is

`Delta_chi = sum_(i:chi_i=0) (e_(V_i)-e_(U_i))`.             (4.1)

It vanishes if and only if the two multisets

`{V_i:chi_i=0}` and `{U_i:chi_i=0}`

are equal, with multiplicity.  The constant pattern `1111` is trivially
neutral because the sum is empty.  The constant pattern `0000` is **not**
neutral in general: it requires an additional alignment/collision identity
among the four other owners `A_i`.  Nor does a nonconstant pattern alone
prove nonneutrality; cross-index colour collisions must be checked exactly.

The repository's complete generic C8 census is a direct finite warning
against a pattern-only shortcut: in the unsplit factor all four q4 lowers
are internal, yet the 17 protected four-component candidates have rank-10
hole histogram `1^4,2^5,3^7,4^1` and zero rank-10-safe candidates.

Therefore every dense q4 implementation must calculate (4.1) literally.
If it restricts to current-neutral single macros, it may retain only exact
multiset-zero rows; otherwise it must carry the signed current into a
compound-macro master.

For pruning, `U_i != V_i` for every live index: equality would force the
unchanged other owner at `L_i` to be one of the old or absent-new q4 owners.
Thus a one-index internal support cannot be neutral.  On two indices the
only neutral possibility is the crossed pair

`V_i=U_j` and `V_j=U_i`.

On three indices the equality must be a three-cycle of colours, and on four
indices it is an exact multiplicity-preserving derangement (allowing colour
collisions).  Sorting the old and new mask lists is a complete test; symbolic
cut-pattern rejection is not.

## 5. Exact legality and service replay

For every candidate live q4, the proof-safe test is as follows.

### 5.1 Factor and protected resources

1. Verify the four old incidences, four absent new incidences, Boolean
   containment, and preservation of all 52 protected incidences.
2. Apply the toggle and verify degree two and simplicity on both shores.

### 5.2 Fixed-cut physical bank

3. Keep the same 7,612-element set `C`.
4. Delete `C` from `F'` and reject if any cut-free cycle remains.
5. Verify that the result is 7,612 paths partitioning all 24,310 owners
   exactly once.

The lower-q1 palette is then structurally exact before seam selection:
every lower outside `C` occurs once internally and every lower in `C` is one
named seam obligation.  Distinctness of the selected lower colours is
automatic because `C` itself is unchanged, but every colour still needs a
literal seam in the final matching.

### 5.3 Internal and relaxed residence

6. For every rebuilt owner word and coordinate, reject a positive run of
   length at most three which is bounded by zeros strictly inside the word.
   Such a run cannot be repaired at a seam.
7. Recompute both orientation states and the complete relaxed atomic atlas.
   The relaxed predicate remains only a necessary two-block condition; it
   is not a full chronology certificate.

### 5.4 Projection and orientation rows

8. Recompute zero lower-colour, tail-piece, and head-piece rows.
9. Recompute the three physical projection matchings

   `tail-piece <-> head-piece`,
   `tail-piece <-> cut-colour`,
   `cut-colour <-> head-piece`.

   Preservation means all three matching numbers remain 7,612.
10. For every piece `p`, compute

   `G_p={sigma: Out(p,sigma) nonempty and In(p,sigma) nonempty}`.

   The desired q4 service must reduce the 187 empty `G_p` rows, ideally to
   zero.  Pairwise perfect projections do not imply these rows.

### 5.5 Rank-10 service

11. Recompute every internal consecutive-owner union of rank ten.
12. For each remaining rank-10 target, test the complete relaxed seam atlas.

A candidate serves an old zero target `R` exactly when `R` becomes internal
or is the endpoint union of a new relaxed atom.  It is not enough to cover
the old list of 78: the full replay must have zero rank-10 rows, since a q4
may destroy a former internal or seam provider.

Only after these tests is it meaningful to impose a common orientation,
tail/head/colour matching, topology, exact residence automaton, deeper deck,
or compiler.

## 6. Balanced four-cut relocation is a different operation

A literal balanced relocation keeps `F` fixed and replaces

`C` by `C'=(C-R) union A`, with `|R|=|A|=4`.

It is legal only if `C'` is protected-avoiding, has 7,612 distinct lowers,
hits every old short-run interval, and leaves no cut-free factor cycle.
One then performs the same complete rebuild in Section 5.  This operation
changes which lower colours are internal versus seam obligations; global
lower exactness can still hold, but the selected cut-lower set is not fixed.

No existing fixed-C incidence-C8 result proves legality or completeness of
this balanced-relocation class, and conversely a balanced relocation is not
an underlying-factor C8.

## 7. Implementation audit requirements

A proof-safe dense-q4 implementation must therefore expose:

- the q4 key `(K,p_0,p_1,p_2,p_3,phase)` and cut pattern `chi`;
- the eight incidence deltas and protected-edge audit;
- a full rebuilt piece inventory, not patched old endpoint summaries;
- the internal short-run audit;
- the complete relaxed atom atlas;
- all three projection matching ranks and all `G_p` rows;
- full rank-10 zero rows, with old gains and new losses separated.

The existing component-fusion q4 source is not by itself such an auditor:
it enforces four distinct components and evaluates q1 current on the
unsplit factor, whereas the dense-service problem needs arbitrary component
signature and literal reconstruction of the 7,612-piece bank.

## 8. Scope

This note proves the fixed-endpoint obstruction and the exact boundary
between dead and live q4 classes.  It does not assert that any live q4
passes the replay, that 265 rows admit a simultaneous cover, or that a
locally passing q4 extends to a global chronology or compiler.
