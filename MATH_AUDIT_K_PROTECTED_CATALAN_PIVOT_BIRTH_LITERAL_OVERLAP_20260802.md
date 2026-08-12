# Audit of the protected Catalan--pivot birth and literal-overlap reductions

**Date:** 2026-08-02  
**Scope:** independent audit of
`MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_CONNECTOR_BIRTH_AND_PREPARED_SCAFFOLD_GATE_20260802.md`
and
`MATH_THEOREM_K_PROTECTED_CATALAN_PIVOT_LITERAL_CONNECTOR_AND_EXACT_REMAINING_GATE_20260802.md`.

## 0. Verdict

The local size/rank ledger, the protected predecessor-matching extension,
the rooted-link path calculation, the upper-provider selection inside an
already existing rooted Hamilton path, and exact literal `d`-overlap
concatenation are proof-safe.

Two corrections were necessary and are now present in the theorem notes.

1. The unrooted closed-shore formulation is missing an endpoint-aperture
   condition.  If `o` is the one omitted lower root and `s,t` are the two
   final owner endpoints, then one must require
   
   \[
                      o\subseteq s\quad\hbox{or}\quad o\subseteq t.
   \]
   
   Without this, the resulting rainbow Johnson Hamilton path need not lift
   to a perfect rooted phase `M_0`.  The corrected unrooted theorem states
   this endpoint aperture explicitly.
2. The literal-overlap proof says that nonadjacent component blocks are not
   identified.  This is false whenever an intervening owner component has
   fewer than `d` vertices (in particular for isolates).  Pairwise overlap
   equalities are therefore only local constraints: source letters and caps,
   physical pin injectivity, owner-history acceptance, and every other
   address resource must be checked in one global quotient.  The corrected
   literal theorem now imposes that quotient.

There is also an important scope correction.  The born-connector theorem is
an exact **decomposition of an already selected upper-surjective rooted
Hamilton path**.  It is not an existence reduction for that path: its
hypothesis already contains the tail partition, head partition, upper
surjection, and graphic spanning-tree correlation.  Likewise `PCPS` is a
valid sufficient package, but it retains nearly every global construction
gate.  The owner-layer equivalence is genuine; the claimed constructive
gain is only the removal of a separate *post-hoc* connector choice.

## 1. Size and rank ledger: PASS

In the odd host `[2m-1]`, the sharp collar uses

\[
                         m+3d
\]

distinct coordinates.  Hence it embeds exactly under

\[
                 m+3d\le 2m-1\iff m\ge3d+1.
\]

Its owner path has `3d+1` rank-`m` vertices and `3d` Johnson transitions.
The predecessor incidences use `3d` distinct lower roots and `3d` distinct
owners, so they form a matching.  The same inequality gives
`3d<=m-1`, exactly the range of the protected small-matching extension
theorem.  Thus the extension to a perfect `M_0` is valid.

For the literal component accounting, a component with `n_K` owner cells
and charge `epsilon(K)` has source length

\[
                         n_K+d+\epsilon(K),
\]

and therefore `n_K+epsilon(K)` depth-`d` cells.  Gluing two blocks along
exactly `d` source letters gives source length

\[
 n_K+n_{K'}+d+\epsilon(K)+\epsilon(K'),
\]

so their depth rows concatenate with no extra cell.  Iterating over all
components gives length

\[
       \sum_K n_K+d+\sum_K\epsilon(K)=W+d+1
\]

under the stated hypotheses.  This part of the `B+1` accounting is exact.

## 2. Rooted pivot path and upper-provider selection: PASS

If `M_0(I_i)=V_i`, then the successor incidence `I_i V_(i+1)` contracts to

\[
 I_i\longrightarrow M_0^{-1}(V_{i+1})=I_{i+1}
\]

for every nonterminal edge.  The terminal head
`M_0^{-1}(V_(3d))` is new by injectivity of `M_0`.  Hence the successor
shore is one simple rooted directed path, and its upper labels are the
distinct sets `V_i union V_(i+1)`.

Now suppose `Q` is already a matching of size `W-1`, its rooted links are
graphic-independent, and its upper labels cover every rank-`m+1` colour.
Its rooted graph is a spanning tree of maximum indegree and outdegree one,
hence a directed Hamilton path.  Choosing one occurrence of every upper
colour, with the distinct protected occurrences forced, gives `U` edges.
As a subset of a path this is a forest with

\[
                         W-U=C
\]

components.  The complementary `C-1` path edges necessarily join those
components in their linear order through their unique free ports.  This
proves the born-connector decomposition.

For the converse statement, the words “free-port path” must formally
include that `Q_0 dotcup Q_1` is a matching outside `M_0` and that every
tail and head port is used at most once.  Items 2--5 alone, read literally
without that convention, do not state all hypotheses needed for (2.2).

## 3. Missing endpoint aperture in the unrooted formulation

The exact missing condition has a short proof.

### Lemma 3.1 (endpoint aperture for rooting a rainbow owner path)

Let

\[
 V_0,L_0,V_1,L_1,\ldots,L_{W-2},V_{W-1}
\]

be the incidence lift of a Johnson Hamilton path on all `W` rank-`m`
owners, with distinct rank-`m-1` transition roots.  Let `o` be the unique
unused lower root.

There is a perfect matching `M_0` containing the predecessor phase
`L_i V_i` if and only if `o subseteq V_(W-1)`.  There is one containing the
successor phase `L_i V_(i+1)` if and only if `o subseteq V_0`.

#### Proof

In the predecessor phase, the `W-1` used roots are matched to exactly the
first `W-1` owners.  The only unmatched lower vertex is `o` and the only
unmatched owner is `V_(W-1)`.  A perfect extension therefore exists exactly
when their incidence is legal.  The reverse phase is identical.  \(\square\)

Consequently Theorem 2.3 of the birth note correctly includes

\[
                         o\subseteq s\text{ or }o\subseteq t
\]

in addition to the closed-shore degree and graphic-rank conditions.  The
flow criterion (2.9) does not mention `o`, so it cannot imply this aperture
by itself.  With this extra condition, orientation toward the incident
endpoint recovers the perfect rooted phase and the equivalence is valid.

This is not only a formal omission.  An exhaustive `m=3` replay gives the
upper-surjective rainbow-root owner path (masks are on `[5]`)

\[
 7,11,13,21,19,26,14,22,28,25,                       \tag{3.1}
\]

whose transition roots are

\[
 3,9,5,17,18,10,6,20,24.
\]

The omitted root is `o=12`, while the endpoints are `7` and `25`; `12` is
contained in neither endpoint.  The transition upper colours cover all
five rank-four masks.  Taking edges `1,2,3,4,6` (zero-based) as `F_0`
uses the five upper colours

\[
                         15,29,23,27,30
\]

exactly once.  The remaining edges `0,5,7,8` use precisely the four roots
in `A`, meet the endpoint degree vector, and have contracted graphic rank
four.  Thus the closed-shore and connector hypotheses hold, but no perfect
rooted phase can be recovered.  The replay source and output are

* `scratch/audit_m3_rainbow_path_omitted_root_endpoint_20260802.cpp`,
  SHA-256 `eb6bb167b6344333c7c339dc7d5f7c9a1b1bae7c3c9fa56acf602147a965a170`;
* `scratch/audit_m3_rainbow_path_omitted_root_endpoint_20260802.out`,
  SHA-256 `bef58dd5d1962f6a331dbf00af4f2ba7e9a88dcf8b22f5dd6212cb00bf583f4e`.

## 4. Literal overlap: local lemma PASS, iteration sentence corrected

For two blocks, literal equality of the last and first `d` source letters
proves the depth-row concatenation and preserves every old interval
occurrence.  The two-block Lemma 3.1 is correct.

For several components, let block `i` have owner count `n_i` and charge
`epsilon_i`.  Its start position advances by `n_i+epsilon_i`, not by its
whole source length.  Thus blocks `i` and `i+2` overlap in

\[
              \max\{0,d-(n_{i+1}+\epsilon_{i+1})\}
\]

source positions.  An isolated uncharged middle component gives an overlap
of `d-1`.  Hence the sentence “No nonadjacent blocks are identified” is
false.

This does not invalidate source concatenation: the middle block fixes both
overlaps, so adjacent literal equalities are transitively consistent.  It
does mean that the following resources cannot be certified solely by
pairwise port arcs:

* equality or collision of physical interval addresses;
* pin injectivity between nonadjacent component states; and
* any exported resource whose address support crosses more than one seam.

Theorem 4.1 now requires a globally consistent address quotient in item 1
and an address-disjoint pin union in item 4.  Those global guards, rather
than the erroneous no-nonadjacent-overlap sentence, make its source and pin
conclusions valid.  Any algorithmic
`GOP(m,d)` statement must retain this higher-order compatibility condition;
ordinary Hall in the pairwise port graph alone does not enforce it.

## 5. Residence-history scope

The history state must be declared to refer to the coordinate traces of the
**depth row / owner chronology**, since that is the residence condition used
by the carrier theory.  Histories of the source letters are a different
object and do not directly state owner residence.

If owner components can have fewer than `d+1` vertices, merely checking the
two original endpoint states on each adjacent arc is not, by itself, a
generic finite-automaton composition proof: one short run can pass through
several all-one owner fragments.  One must either propagate the aggregate
automaton state along the chosen path or check the final concatenated owner
trace.  (For source fragments of length at least `d+1`, the analogous
pairwise clipped-run argument does not have this short-fragment issue.)

For positive residence, a globally literal factor actually gives a shorter
proof: every source occurrence creates `d+1` consecutive occurrences in
the depth row, so every internal positive run in that row has length at
least `d+1`.  The finite boundary automaton remains useful for prospective
state selection, for a controlled nonowner convention, or when simultaneous
zero-run residence is required.  The corrected literal note accordingly
keeps the ordered source `d`-rails separate from the clipped coordinate
histories of the owner chronology.

## 6. Upper tower and lower pins: proof-safe only with the stated global guards

The upper-provider selection inside `Q` proves only the immediate rank
`m+1` palette.  The separate occurrence atlas is genuinely necessary for
deeper targets.  If every selected witness is wholly contained in one
component block, literal overlap preserves it.  This is a valid sufficient
condition, but not a necessary characterization: a valid final word may use
upper witnesses crossing connector seams.

Likewise, the pivot singleton and two rays close the **local** pivot
compiler ledger.  A universal-word conclusion requires that the declared
pin bank in Theorem 4.1 be the complete strict-lower target bank and pass
one terminal common-cap check.  If “declared bank” is smaller, the theorem
proves only the corresponding partial compiler statement.

## 7. Exact logical status of the born-connector reduction

At the owner/immediate-upper layer there is a genuine equivalence:

\[
 \begin{array}{c}
 \text{upper-surjective rooted Hamilton path}\
 \text{containing the protected pivot}
 \end{array}
 \quad\Longleftrightarrow\quad
 \begin{array}{c}
 \text{upper-exact rooted Catalan forest}\
 +\text{ compatible free-port component path}.
 \end{array}
\]

But the forward direction starts with the hard correlated path already in
hand.  Therefore “the connector is born” correctly eliminates a separate
post-hoc connector search; it does **not** prove or materially relax the
four-resource existence problem.

The literal `PCPS` hypothesis is similarly sufficient but close to a
restatement of the desired construction: it assumes an all-width-complete
preword, the final protected Hamilton owner row, residence interfaces, and
the terminal common cap.  The `PCF+GOP+CAP` split is useful bookkeeping, but
`PCF`'s component-internal witness-atlas condition is stronger than general
existence and hence the split is not an equivalence to all possible `B+1`
words.

### 7.1 Recheck of the cycle-cover escape under the corrected guards

The rooted factor-first escape remains correct, but only on its explicitly
source-lifted face.  Here `M_0` is fixed before the connector cycle cover is
chosen.  If the final connector incidence `e=oV` is opened and
`S=M_0(o)`, its owner endpoints are `S,V`, so `o subset S` and `o subset V`
hold automatically.  The omitted-root defect of Section 3 therefore does
not recur on this rooted face.

What does recur is the global physical state.  A perfect free-port matching
gives only a component cycle cover.  A protected merger incidence tree and
an opening prove the desired linear chronology only if all of the following
are carried through the actual sequence of source words:

1. merger supports are closed under the global address quotient, or remain
   hereditarily literal after every earlier merger;
2. all-width witness multiplicities are computed sequentially and the final
   signed opening increment leaves each required target positive;
3. the composed owner-coordinate residence history accepts;
4. the source surplus is exactly one, with full `d`-overlap at every internal
   Catalan join and the unique nonowner at a global boundary; and
5. the opened rank-`m-1` root is literally one maximal pivot-ray target (or
   another explicit rank-`m-1` cell) in the common cap.

Under these guards the incidence-tree argument really does reduce the cycle
cover to one cycle, and the typed opening gives one physical Hamilton path.
Without them ordinary free-port Hall, contracted topology, or pairwise seam
legality proves only an owner-layer factor.

## 8. Proof-safe synthesis

After the corrections above, the valid conclusion is:

> For `m>=3d+1`, the sharp pivot supplies an unconditional protected rooted
> seed.  If one can construct a globally compatible family of literal
> component antecedents whose rooted Catalan forest is immediate-upper
> exact, whose overlap ports form a Hamilton path, whose *global* physical
> addresses are injective, whose internal/cross-seam atlas covers the upper
> tower, and whose pins pass one complete common cap, then exact `d`-overlap
> concatenation gives a length `B+1` word.  In the alternative unrooted
> formulation, the omitted lower root must additionally be incident with a
> chosen final owner endpoint.

This is a sound sufficient route.  It is not yet an unconditional
`B+O(1)` theorem and it does not improve the authenticated finite bound for
`k=17`.
