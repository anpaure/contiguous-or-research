# Long one-tag port arms give a resident tagged connector chain

**Date:** 2026-08-06  
**Method:** random geodesics in a constant-weight layer, missing-tag
separation, and the exact clipped-age scheduling theorem; no computation or
search  
**Status:** unconditional protected-bank and two-sided distance-aperture
theorem, with a conditional source conclusion.  The `O(sqrt R)` forced PBBS
path components can be extended to pairwise far tagged ports and joined into
one resource-disjoint path.  If the fixed pentagon/collar components have
declared biresident literal histories, the added arms and connectors absorb
every internal positive-run and zero-gap flag at zero positional charge.  The
theorem does not plant those common histories, prove biresidence of the fixed
pentagon halos or unprotected completion, or prove typed-cap suffix rank.

## 1. Every Johnson boundary has unit clipped ages

Let a directed rank-`R` Johnson trace have event notation

\[
 T_{i+1}=T_i-\{D_i\}+\{I_i\}.
\tag{1.1}
\]

At a cut owner `T_0`, let `lambda(x)` be the left clipped age of a present
coordinate, truncated at `delta+1`.  For every `1<=s<=delta`,

\[
 |\{x\in T_0:\lambda(x)\le s\}|\le s.
\tag{1.2}

Indeed every such nonconstant run began at one of the last `s` insertion
events, and there is only one insertion per edge.  The right-age statement
is identical using deletions.  Thus the unit clipped-age premise of the
connector scheduling theorem is automatic at every Johnson cut; it is not
special to the sliding collars.

For an untagged endpoint at which a fresh tag is to be deleted on the first
arm edge, that tag must additionally have clipped positive age `delta+1`.
The inserted non-tag must have clipped zero age `delta+1`.  At most `delta`
present coordinates and at most `delta` absent coordinates fail the two
conditions.  Since the common PBBS reservoir has size `R-O(sqrt R)`, the
outside shore has size `Theta(R)`, and only `O(sqrt R)` ports are required,
distinct eligible tags and non-tags can be assigned greedily.  The right-end
dual chooses a tag of full clipped positive right age and a non-tag of full
clipped zero right age.  Thus the forced whisker event itself can satisfy
both run and gap residence.

## 2. A clean geodesic in one missing-tag layer

Fix a tag set `T` of size `t=O(sqrt R)` in a ground set of size `2R-1`, and
fix one tag `g`.  The rank-`R` owners with tag trace `T-{g}` are naturally
the constant-weight layer

\[
 { [N]\choose s},
 \qquad N=2R-1-t,qquad s=R-t+1.
\tag{2.1}

Both `s` and `N-s=R-2` are `Theta(R)`.

### Lemma 2.1 (clean long one-tag arm)

Let `S` be one owner in (2.1).  Let `F_V,F_E` be forbidden owners and lower
facets of the same one-tag signature, with

\[
 |F_V|+|F_E|=O(R),
\tag{2.2}
\]

and suppose at most `C_0` forbidden facets lie immediately below `S`, for
an absolute constant `C_0`.  Put

\[
 L=\lfloor R/4\rfloor.
\tag{2.3}

For all sufficiently large `R`, there is a shortest length-`L` geodesic
starting at `S` whose internal owners and facets avoid `F_V union F_E`.
Moreover its endpoint can be required to avoid any prescribed union of
`O(sqrt R)` Johnson balls of radius `2delta=O(sqrt R)`.

#### Proof

Choose an ordered `L`-tuple of distinct deletions from `S` and an ordered
`L`-tuple of distinct insertions from its complement, independently and
uniformly.  At step `j`, the owner is uniform on the distance-`j` shell,
whose size is

\[
 {s\choose j}{N-s\choose j}.
\tag{2.4}
\]

The edge facet at step `j` is uniform on the corresponding facet shell of
size

\[
 {s\choose j}{N-s\choose j-1}.
\tag{2.5}
\]

At `j=1`, avoid the at most `C_0` forbidden incident facets directly.
The owner shell has size `Theta(R^2)`, so the `O(R)` forbidden owners cost
`O(1/R)`.  For `j>=2`, (2.5) is at least `Theta(R^3)` and (2.4) at least
`Theta(R^4)`.  These shell sizes increase geometrically for
`j<=R/4`.  A union bound over all `L` steps and the `O(R)` forbidden
resources is therefore `o(1)`.

The terminal shell has size

\[
 {s\choose L}{N-s\choose L}=\exp(\Theta(R)).
\tag{2.6}
\]

A radius-`2delta` Johnson ball has size at most

\[
 (2\delta+1)R^{4\delta}
   =\exp(O(\sqrt R\log R))=\exp(o(R)).
\tag{2.7}
\]

Even `O(sqrt R)` such balls occupy an `o(1)` fraction of the endpoint
shell.  The clean-path event and endpoint-avoidance event therefore have a
common realization. \(\square\)

For the PBBS same-tag start, the required local constant is not an extra
hypothesis: Lemma 4.2 of
`MATH_THEOREM_PBBS_SYNCHRONIZED_INCOMING_COLLAR_CANCELS_COMPLETE_UPPER_CURRENT_20260805.md`
proves that a fixed owner contains at most five lower colours of its collar.
Thus one may take `C_0=5`.

The same proof works after an untagged endpoint `E` takes the initial edge

\[
 E\longrightarrow E-\{g\}+\{z\},
\tag{2.8}

with `z` a non-tag outside `E`: apply Lemma 2.1 for the remaining `L-1`
steps.  If `g` is a prospectively fresh port tag, the whole one-tag
signature is absent from the old bank and no same-signature avoidance is
needed.

## 3. Planting all arms

Let `C_1,...,C_q`, `q=O(sqrt R)`, be the oriented components of the
terminal forced PBBS forest.  Give each of their two free owner endpoints a
distinct tag.

* If the endpoint is already the far end of its synchronized collar, use
  that collar's unique tag.  The only old resources with this signature
  form that one `O(R)` collar, and its endpoint exposure is bounded by the
  collar theorem.  Lemma 2.1 supplies a clean continuation arm.
* If the endpoint contains all global tags, choose a fresh eligible tag as
  in Section 1, take (2.8), and continue by Lemma 2.1.

Choose the arms sequentially.  Different arms have different one-tag
signatures and hence cannot meet.  At each selection, use the final clause
of Lemma 2.1 to keep the new far endpoint at Johnson distance at least
`2delta+1` from every previously chosen far endpoint.  We obtain `2q`
pairwise far ports, each at the end of a length-`L` arm.  Since
`L=floor(R/4)>=2delta+1` for all sufficiently large `R`, both arms and the
shortest connectors between successive far ports have the two-sided
residence aperture.

Every arm is a shortest geodesic.  Consequently a fixed lower facet lies
below at most two arm owners and a fixed owner contains at most two arm
facets.  The complete arm bank therefore has

\[
 e=O(qR)=O(R^{3/2}),
 \qquad
 \alpha,\beta=O(q)=O(\sqrt R).
\tag{3.1}

## 4. Biresidence of a chain of long geodesic segments

### Lemma 4.1 (segmentwise scheduling with biresident fixed blocks)

Concatenate fixed biresident Johnson path blocks with an exit arm and an
entrance arm of length at least `delta+1` at every internal block.  Join
successive far-arm endpoints by shortest connectors of length at least
`2delta+1`.  Then the deletion and insertion orders can be chosen so that
every positive run and every zero gap internal to the concatenation has
length at least `delta+1`.  Only the two exterior ends retain clipped flags.

#### Proof

At every Johnson boundary, both positive and zero clipped ages have the
unit property: in the last `s` steps there are at most `s` insertions and at
most `s` deletions.  We choose the event orders in three stages.

First direct every exit arm from its fixed component toward its far port.
For a coordinate present at the fixed endpoint and deleted on the arm, use
the positive left age as a release condition.  For a coordinate absent at
the endpoint and inserted on the arm, use its zero left age as a release
condition.  Each release list is feasible on an arm of length at least
`delta+1` by the cut argument of Corollary 3.1 in
`MATH_THEOREM_TAGGED_CONNECTOR_ANTECEDENT_SCHEDULING_AND_CAP_OBSTRUCTION_20260806.md`.
There is no imposed condition at the far end; the chosen orders simply
determine its positive and zero left-age profiles.

Second direct every entrance arm from its far port into its fixed component.
Use the component's zero right ages as deadlines for deletions and its
positive right ages as deadlines for insertions.  The dual cut argument
makes both deadline lists feasible on an arm of length at least
`delta+1`.  The chosen orders determine the positive and zero right-age
profiles at the far port.

Now every connector has fixed age profiles on both sides.  The two-sided
interval-Hall theorem (Theorem 3.2 in the same scheduling note) applies
because its length is at least `2delta+1`.  It chooses a deletion
permutation and an insertion permutation simultaneously preserving the
run before/gap after each deletion and the gap before/run after each
insertion.  These two permutations remain independent edge by edge.

For a fresh exit whisker, choose both its deleted tag and inserted non-tag
with full positive and zero left ages as in Section 1; the forced first
event is then feasible.  The entrance-whisker statement is the right dual.
On a pair-tag connector, the first deleted foreign tag was present through
the whole exit arm and absent through the whole entrance arm, while the
last inserted foreign tag has the dual history.  Their two allowed
intervals therefore contain the prescribed extreme slots.

Coordinates common to both ends of a long segment have a positive run
through all its owners, and coordinates absent at both ends have a zero gap
through them.  Coordinates that change state are covered by the release,
deadline, or two-sided interval conditions just imposed.  Runs and gaps
wholly inside fixed blocks were long by hypothesis.  This exhausts the
coordinate types, proving the claim. \(\square\)

## 5. Biresident tagged chain theorem

### Theorem 5.1

For all sufficiently large `R`, with

\[
 q=O(\sqrt R),\qquad \delta=O(\sqrt R),
\]

assume the terminal forced pentagon/collar components have declared literal
histories and are biresident (every internal positive run and zero gap has
length at least `delta+1`).  The positive-run half for the collar interiors
comes from the sliding-window construction; for the pentagon heads it is
Proposition 4.1 of
`MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`
**after** its prospective common-history premise is satisfied.  Those
results do not by themselves establish the zero-gap half, which remains an
explicit local premise here.  Then

the terminal forced PBBS components admit a prospective protected
extension with the following properties.

1. Every component receives two clean length-`floor(R/4)` one-tag arms.
2. The `2q` far ports are pairwise at Johnson distance at least
   `2delta+1`.
3. In any prescribed component order, successive far ports are joined by
   the pair-tag geodesic; all connectors have length at least
   `2delta+1`.
4. The arms and connectors are mutually resource-disjoint, have total
   size `O(R^(3/2))` and exposure `O(sqrt R)`, and form one oriented path.
5. Their event orders can be chosen so every positive run and zero gap
   internal to the forced path has length at least `delta+1`; only its two
   final exterior endpoints retain clipped flags.  On its complete internal
   halo the maximal antecedent is nonempty, and no source position has been
   added.

#### Proof

Sections 1--3 give the clean pairwise-far arms.  A connector between port
tags `a,b` has the exact two-missing-tag signature `{a,b}`, so different
connectors are disjoint from one another, from the one-tag arms, and from
the zero/one-tag forced bank.  The tagged-port theorem gives the edge and
exposure counts and joins the components into one path.  Every arm has
length at least `delta+1` and every connector at least `2delta+1`; apply
Lemma 4.1.  The
maximal-antecedent criterion then gives the final assertion. \(\square\)

## 6. Exact remaining scope

This theorem closes the **forced-bank two-sided distance aperture**
unconditionally and the internal run/gap row conditional on declared
biresident local histories.  It is still not the full literal PBBS lift:

1. the fixed pentagon halos and the unprotected cycles supplied by the
   polynomial two-factor completion are not proved biresident by this
   theorem;
2. a maximal antecedent on the terminal forced path is not yet an
   occurrence-bijective old/new common-history transport;
3. joining the residual factor cycles into one literal source chronology
   remains open; and
4. unique tag signatures supply physical prefix privacy but not the
   all-cut typed suffix rank.  A common unit-capacity suffix bottleneck can
   still leave `Omega(sqrt R)` cap deficiency.

Thus the PBBS source gate has been narrowed from arbitrary long-chain
clipped flags to local fixed-block biresidence, completion/common-history
fusion, and the independent typed-cap router.

## 7. The exact typed-arm density target

The long-arm orbit is large enough for a suffix-router argument, but only
after occurrence-level cap acceptance is proved.  Before typed filtering,
one one-tag port has

\[
 |\mathcal G|=(s)_L(N-s)_L
       =\exp(\Theta(R\log R))
\tag{7.1}
\]

labelled length-`L` geodesics.  Lemma 2.1 deletes only an `o(1)` fraction.

Fix one materialized cap/phase/guard state and let `C_p` be the subset of
these clean arms which carry a complete legal typed suffix for active port
`p`.  The Haxell private-router theorem gives the following exact
sufficient row:

\[
 \min_p|C_p|\ge2\Delta,
\tag{7.2}
\]

where `Delta` is the maximum, over one accepted arm suffix, of the number
of accepted candidates in all other port lists sharing a physical capacity
or sink.  In particular the estimates

\[
 |C_p|\ge\exp(cR\log R),
 \qquad
 \Delta=\exp(o(R\log R))
\tag{7.3}

would prove full typed suffix rank for the connector port bank.

Equation (7.1) proves raw supply, not (7.3): structural zeros may reject
every raw arm, and an external unit suffix bottleneck may give exponential
conflict degree.  Thus the remaining cap theorem has been sharpened to a
positive-density typed lift plus a subexponential conflict-multiplicity
bound.  Neither estimate follows from missing-tag separation alone.

## 8. Long arms decouple distinct history pin blocks

The arms also remove a global correlation which is easy to overlook.  Let
`T` be any completed resident trace with maximal antecedent `P`.  Let
`B_1,...,B_h` be disjoint source-position intervals, each of length at most
`delta`, with at least one unaltered maximal position between consecutive
blocks.  On every `j in union B_i`, choose a nonempty pinned letter `H_j`
satisfying

\[
                         F_j\subseteq H_j\subseteq P_j,
\tag{8.1}
\]

where `F_j` is the exact forced pair of the resident trace.  Replace `P_j`
by `H_j` on all blocks and leave the maximal word elsewhere.

### Lemma 8.1 (separated short-block freedom)

The resulting word is still a depth-`delta` antecedent of `T`.

#### Proof

Work coordinate by coordinate in one maximal carrier interval.  A pin block
can delete that coordinate only from at most `delta` consecutive nonforced
positions; (8.1) retains either forced carrier endpoint if it lies in the
block.  Hence the new support gap made by one block has length at most
`delta+1`.  If the same carrier meets two pin blocks, the unaltered maximal
position between them retains the coordinate and separates the two gaps.
If it does not contain that separator, the carrier interval cannot meet
both blocks.  Thus every support gap satisfies the bounded-gap antecedent
criterion. \(\square\)

The length-`Theta(R)` arms place different pentagon history blocks much
farther apart than one maximal position.  Consequently, **conditional on a
resident global completion**, simultaneous history planting has no
cross-height Hall or flow condition: it reduces to the local containments
(8.1) on each complete pentagon halo.  Those local halo containments are
still premises; owner-level collar planting alone does not verify them.
