# `k=17`: proof-safe D certificate for radius-three and role-relocating `C8` survivors

**Date:** 2026-08-02  
**Status:** exact specification relative to the frozen round-02 primitive
catalogues and a finite authenticated successor-core library.  It performs
no q1 solve.  `SURVIVOR` below means only that the declared successor proof
system did not reject the packet.

## 1. Frozen finite input

The current exact-build input has `3,664` rows and `3,664` distinct complete
occurrence-labelled q1 delta keys; the largest equality class has size one.
This is a statement about complete anchor-relative deltas, not about exterior
boundary types and not about q1 feasibility.

The next generator uses the following immutable inputs.

1. The authenticated round-02 bank `B0`, its occurrence map, and the complete
   one-for-one recut catalogue.  A primitive recut key contains its base,
   old cut and new cut.  Two or three recuts are compatible only when their
   final cut data define one literal bank; in the present one-for-one shell
   this includes the distinct-base condition.
2. The full zero-265 row ledger.  Its five reported failure coordinates are
   `zero_lower`, `zero_out`, `zero_in`, `zero_orientation`, and
   `zero_rank10`.  A packet is joint-clean only when every one is zero after
   all packet edits are applied simultaneously.
3. An authenticated q1 library partitioned into unconditional contradictions
   `L0` and pivot-conditional successor certificates `Lsucc`.  Each entry
   contains its immutable occurrences, demanded physical resources, complete
   effective provider rows and footprints, capacities/conflicts, guards or
   blocker proofs, and either a resource-deficiency certificate, guarded
   minor, or implication bicycle.  Every permitted occurrence transport and
   every stored embedding is included in the library manifest.  A member of
   `Lsucc` is never used for unconditional anchor rejection.
4. For the circuit face, the authenticated selected incidence factor and the
   complete Boolean rank-8/rank-9 incidence graph.  A circuit key uses
   occurrence-labelled incidences, never owner masks or mutable piece ids.

Closure of all `3,664` Hamming-two rows is a separate prospective input.  A
radius-three output may be called the *first independent-recut shell* only
after a proof manifest authenticates that closure.  The generator itself
does not assume it.

## 2. The exact causal-anchor table

For every unconditional core `K in L0`, retain its complete dependency cone
`D(K)`.
For each compatible set `A` of at most three primitive recuts, construct the
formal bank `B[A]` before imposing zero-265.  A **causal anchor record** is an
inclusion-minimal `A` for which some load-bearing datum of `D(K)` changes.
Its serialized record contains

* `core_id`, `datum_id`, event type and `|A|`;
* the immutable recut keys in `A`;
* for an atom event, its tail occurrence, head occurrence, lower colour and
  complete resource footprint;
* the complete truth table on all subsets of `A`; and
* the old and new value of the changed row, role, capacity, guard or blocker.

The truth table is load-bearing.  It retains a provider which appears only
after two endpoint changes and a palette change, and it also retains
nonmonotone palette compensation.  It is not enough to union unary or binary
provider lists.

The possible q1 events may be indexed as follows:

* direct occurrence, role, resource, capacity, old-atom or blocker change;
* geometry--palette or two-endpoint activation on two recuts; and
* a genuinely ternary provider activation, most visibly
  tail--head--selected-colour activation, or any other ternary truth-table
  residue of the declared primitive bank.

This classification is descriptive.  Completeness is supplied by literal
subset truth tables, not by assuming a unique colour supplier.  The ternary
class is needed for successor cores and other changed rows.  It does not
enlarge the exact anchor set for the *original* round-02 dual fan; the
special one-fixed-central-endpoint geometry gives the sharper corollary in
Section 3.1.

## 3. Candidate packets

### 3.1 Three-recut packets

A radius-three key is the sorted triple of compatible immutable recut keys.
All three edits are applied before any local test.  In particular, a dirty
singleton or dirty pair is not discarded: its debt can be repaired only by
the full triple.

Let `A_3(K)` be the causal-anchor family for `K`.  A triple `S` can disturb
every unconditional stored trace only if

\[
  \forall K\in L0\quad\exists A\in A_3(K)\quad A\subseteq S. \tag{3.1}
\]

There is a sharper authenticated reference-core statement here.  Let
`A21` be the twelve selected-colour socket escapes and all nine alternatives
in the two central bases from the frozen anchor theorem.  Every
radius-three bank which destroys the original `114930` dual fan satisfies

\[
                         S\cap A21\ne\varnothing.             \tag{3.2}
\]

Indeed, a central-base change belongs to `A21`.  Without one, the direct
central seam remains illegal.  A final noncore arm has one fixed central
endpoint and at most one recut-created outside endpoint.  If it is already
selected in that singleton child, its creator is one of the twelve visible
anchors.  Otherwise use the exact one-for-one multiplicity law

\[
 m_S(c)=m_0(c)+\sum_{a\in S}
   \bigl({\bf1}_{\mathrm{new}(a)=c}
        -{\bf1}_{\mathrm{old}(a)=c}\bigr).                 \tag{3.2a}
\]

If the arm colour `c` has multiplicity zero in its creator child and positive
multiplicity in the triple, some other recut `h` has positive contribution
in (3.2a), and the creator--supplier pair already has positive multiplicity.
A nonanchor such pair would occur in the authenticated raw inverse join,
whose complete nonanchor output is empty.  The third recut can repair other
rows but cannot undo this containment conclusion.  Hence (3.2) follows.
This proof uses the literal round-02 arm geometry, one-for-one palette law,
and empty raw join; it is not a generic statement about arbitrary dual fans.

Thus D starts with `anchor in A21`, chooses two further compatible recuts,
applies all three simultaneously, and deduplicates the sorted triples.  It
then intersects (3.1) for the rest of the library.  In particular, with
`N=16667`, a safe pre-deduplication bound is

\[
                         21{N-1\choose2}.                      \tag{3.3}
\]

Same-base exclusions and repeated generation by two anchors only decrease
this number.  More generally, if a different reference family contains
`a_i` anchors of size `i`, then before deduplication the number is at most

\[
 a_1{N-1\choose2}+a_2(N-2)+a_3.                            \tag{3.4}
\]

These are exact finite anchor bounds, not survivor-count bounds.  Ternary
provider residues still have to be reconstructed after generation: they can
disturb a successor core even though (3.2) already anchors destruction of
the original dual fan.

### 3.2 Atomic aligned `3+1` `C8` packets

A proof-complete simple-`C8` catalogue must contain both Boolean incidence
families:

* star keys `C_i=S union {a_i}`, `|S|=7`; and
* octahedral keys `C_i=S union {a_i,a_(i+1)}`, `|S|=6`.

The three cyclic orders modulo reversal and two toggle phases give
`24504480` canonical oriented keys in each family, hence `49008960` before
activity and dependency-cone filtering.  Reusing the old star-only
catalogue would make the next generator incomplete.

A circuit key records the four removed and four inserted incidences of one
simple alternating `C8`, its family and core/petal data, its orientation,
the old component ids, and the cyclic order of the three old incidences on
the repeated component.  It is in the declared `3+1` role-relocation face
exactly when

1. the removed-incidence component pattern is aligned `3+1`; and
2. the final immutable forced-role key differs from the old one.

The `C8` is toggled atomically.  Its four-edge subsets are not independent
recuts and are not screened as intermediate banks.  To enumerate the class
without a broad circuit scan, anchor one changed incidence slot in the
reverse dependency cone of a reference core, complete the literal
alternating-cycle equations, and then intersect the analogous dependency
condition for every other unconditional core.  A packet whose changed slots
avoid an unconditional core dependency cone leaves that core trace
unchanged.

Here the reverse cone is computed on the complete joint `C8` hypergraph: a
slot is included when it participates with other changed slots in a new
endpoint--endpoint, endpoint--colour, or tail--head--colour atom incident
with the core.  It is not the union of four singleton-delta cones.

The `C8` shell and the radius-three shell are incomparable.  A `C8` is one
correlated degree-preserving packet, while a three-recut bank need not be an
alternating circuit.

## 4. Exact survivor test

For either packet type, D first builds the complete final occurrence-labelled
bank and requires all five zero-265 coordinates to be zero.  It then rejects
every entailed member of `L0` and rebuilds the exact footprint family
`Sigma_B(U0)` at the chosen pivot resources.

For a footprint `P`, contract every resource in its complete footprint and
all incident seam atoms.  The packet is a **library-open survivor** exactly
when no unconditional core is entailed and

\[
 \exists P\in\Sigma_B(U_0)\quad
 \forall K\in Lsucc\quad K\text{ does not close }B/P.       \tag{4.1}
\]

Equation (4.1) is the exact negation of the successor-cover refutation
`for every P, some K closes P`.  Merely changing every old trace is weaker
than (4.1).

A proof-safe open-footprint certificate consists of:

* the selected seam ids in `P`, their pairwise-disjoint resource footprints,
  and the complete footprint-family hash;
* for every `Lsucc` resource-support entry which does not close, a compatible
  seam family saturating its residual demand after `P` is contracted;
* for every `Lsucc` guarded-minor or bicycle embedding, a named missing
  clause, entailed leaf, blocker, vertex or implication arc; and
* the complete-embedding manifest proving that all stored transports and
  embeddings were checked.

These are `OPEN_MANIFEST` witnesses only for the finite declared library.  A
syntactically missing guarded-minor leaf or bicycle arc proves that the named
stored derivation does not close; it does not prove semantic non-entailment
by every possible derivation.  A semantic `OPEN` claim requires either a
countermodel for the asserted entailment or a separately complete entailment
replay.  An incomplete embedding/derivation manifest is `UNKNOWN`, not open.
None of these witnesses proves the absence of a new core.

## 5. Required D artifacts

The generator should emit the following logically separate artifacts.

1. `inputs.sha256`: hashes of the baseline bank, primitive catalogues,
   occurrence map, zero-265 ledger and successor library.
2. `causal_anchors.tsv`: the records of Section 2, including subset truth
   tables and full resource footprints.
3. `packets.tsv`: canonical packet key, packet type, primitive support,
   final-bank hash, and (for `C8`) `STAR|OCTAHEDRAL`, the core/petal/order/
   phase key, all eight incidence ids, the `3+1` order and old/new role keys.
4. `zero265.tsv`: the five exact final failure coordinates, with a row-ledger
   hash.  A summed objective is insufficient.
5. `provider_delta.tsv`: every added, removed or relabelled final q1 atom,
   its occurrence endpoints, colour and full resource footprint.
6. `footprints.tsv`: every exact pivot signature, its selected seams and
   contraction footprint.
7. `core_scan.tsv`: unconditional rows `(packet,L0-core,embedding)` and
   conditional rows `(packet,footprint,Lsucc-core,embedding)`, recording
   `CLOSE` with its authenticated certificate, `OPEN_MANIFEST` with the
   witness specified in Section 4, or `UNKNOWN`.
8. `survivors.tsv`: precisely the packets satisfying joint zero-265 and
   (4.1), together with one named open footprint.
9. `audit.json`: counts before and after anchor generation, deduplication,
   zero-265, trace persistence and successor cover; plus the exact theorem
   scope.  Resource or execution exits are not positive verdicts.

An independent verifier rebuilds every packet from `B0`, checks immutable
keys and compatibility, recomputes its final provider atlas and all five
local rows, reconstructs every footprint, and replays every core status.
It must not trust displayed hashes as semantic equality.

## 6. Completeness theorem for the emitted survivor table

Assume the primitive recut and literal `3+1`-`C8` catalogues are complete,
the causal-anchor and stored-embedding manifests are independently replayed,
and every packet is reconstructed as above.  Then:

1. every support-three one-for-one recut bank which is joint zero-265 and
   satisfies (4.1) occurs in `survivors.tsv`;
2. every atomic aligned role-relocating `3+1` `C8` which is joint zero-265
   and satisfies (4.1) occurs there; and
3. every omitted packet either lies outside those two declared move classes,
   fails an exact local row, or is refuted by an authenticated unconditional
   or successor-cover certificate.

### Proof

If a packet changes an unconditional stored trace, an inclusion-minimal
subset of its at most three primitive recuts changes a load-bearing datum,
so it contains a causal anchor.  Intersecting this condition over `L0`
therefore omits no packet which breaks every unconditional trace.  Literal
subset truth tables
recover every unary, binary and ternary atom and every destruction or role
change.  For a role-relocating `C8`, some changed slot lies in the reverse
dependency cone of each disturbed unconditional core; completing all
anchored simple alternating octagons is therefore exhaustive in the declared
circuit class.  Conditional successor entries are applied only after a
footprint is chosen.  The remaining filters are the literal zero-265 test,
the unconditional semantic scan, and the exact logical condition (4.1).
This proves all three statements.  \(\square\)

## 7. Scope boundary

`SURVIVOR` is not `SAT`.  The table can contain a bank refuted by a new Hall
shore, a larger resource support, or an unrecorded implication core.  No
rank-11-or-deeper shadow, residence, component, opening, common-cap or
compiler statement is made.  Four independent recuts, overlapping same-base
edits, segment rethreads, nonliteral circuits, and a `C8` composed with
additional recuts are outside the declared generator.  Equality of masks,
provider degrees, delta counts, or the earlier 3,664 anchor-relative keys is
never used as a proof shortcut.

## 8. Authenticated finite references

* `scratch/threadD_k17_round02_delta_signatures_20260802/audit.json`  
  SHA `ddcd28ff60094b96426ac617a63b9e93aee0ab7c4e4c3aff0056ab8dc441bae4`.
* `scratch/threadD_k17_round02_delta_signatures_20260802/map.tsv`  
  SHA `07497e807b6897f8ac8c85cf6cb65a017ef0c1ab0ffa8bf6299f9378bd31236a`.
* `scratch/threadD_k17_round02_delta_signatures_20260802/groups.tsv`  
  SHA `fb0c6567b1f9f186508cfc53d214666fc6accf34fc6248249eef48f8cf7772f0`.
* `scratch/threadD_k17_round02_delta_signatures_20260802/counts_union.tsv`  
  SHA `f184ade82dc8f63ac5bd74bf2d89aed25a9d57f05dcc830782480e6bbf3c8fa0`.
* `scratch/threadD_k17_round02_anchored_two_recuts_20260802/clean.tsv`  
  SHA `9c4ecd1541a945bfae2be6d6534b28543a9c5c87745bdb8a47100dda274fb589`.
* `scratch/threadD_k17_round02_anchored_two_recuts_20260802/audit.json`  
  SHA `12ee6bff96d4ab42b0f4c92ef642aedd4b4849f7cdd0632f8b2466d6275ea4df`.
