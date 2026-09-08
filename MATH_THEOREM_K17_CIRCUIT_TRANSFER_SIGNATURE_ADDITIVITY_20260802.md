# Exact circuit-transfer signatures and the guarded additivity theorem

## Status

This note defines the transfer artifact used by the `k=17` c68b residence
lane and proves the exact conditions under which several circuit signatures
may be added without enumerating their full Cartesian product.

It is a **packet-search reduction**, not a residence construction.  Cap
coverage and the residence-blocker current become additive under the guards
below.  Final physical connectivity and every accepted candidate are still
replayed literally.  Deeper upper shadows, a depth-three antecedent, and the
lower compiler remain separate.

## 1. Literal state and defect orbits

Let `F` be a `Z_17`-equivariant rank-eight/rank-nine factor.  Every selected
quotient option develops to 17 physical edges.  Protected marker edges are
fixed.  A positive coordinate run of length two or three has a boundary
segment consisting of its entering edge, its internal edges, and its leaving
edge.

Delete protected edges from that segment and record the sorted list of
selected quotient variables on the remaining edges.  Call this list the
**blocker key** of the run.  The exact blocker audit proves that every current
physical short run occurs in a translation orbit of size 17, so a blocker
key is counted with its orbit multiplicity.

Write `B(F)` for the resulting blocker-key multiset.  Then

```text
short positive runs(F) = 17 |B(F)|
```

whenever there is no all-protected (`FIXED`) short run.  The implementation
retains `FIXED` as an explicit key, so the multiset identity remains valid
without silently discarding that obstruction.

For one quotient circuit `C`, let `F+C` be the degree-two factor obtained by
replacing its old option on each supported facet orbit by its new option.
Its blocker current is

```text
partial_B(C) = B(F+C) - B(F).
```

The transfer row writes the negative and positive parts separately as
`removed_blockers` and `created_blockers`.

## 2. Complete transfer row

For every individually cap-safe simple endpoint-retaining circuit, the exact
artifact records:

```text
id, length, exact_cap,
physical component count and component sizes,
run2, run3, short-run delta,
frozen-bank score,
rank-11/12/13 holes when connected,
removed and created blocker keys,
rank-ten cap current,
facet support, old->new primary variables,
old quotient edges, new quotient edges.
```

An old or new quotient edge is the tuple

```text
(facet representative, owner-a representative,
 owner-b representative, voltage).
```

Thus the row retains enough information to reconstruct the exact changed
factor.  It is not only an aggregate score.

## 3. Resource-current additivity

Let `C_1,...,C_t` be circuits whose facet supports are pairwise disjoint.
Let `Delta_i(e)` be `+1` for a new quotient edge of `C_i`, `-1` for an old
edge, and zero otherwise.  Let `gamma_i(U)` be the analogous rank-ten cap
current.

### Theorem 1 — exact edge and cap current

The simultaneous packet is well-defined and

```text
E(F + C_1 + ... + C_t)
  = E(F) + sum_i Delta_i.
```

Every owner still has degree two.  If `ell_F(U)` is the old cap load, the
packet covers every rank-ten cap exactly when

```text
ell_F(U) + sum_i gamma_i(U) >= 1
```

for every cap `U`.  It preserves the entire cap multiset exactly when every
summed current is zero.

#### Proof

Facet-support disjointness means no old selected option is deleted twice and
no facet is assigned two new options.  Each directed circuit has zero owner
boundary: at every quotient owner it deletes and inserts equally many
incident edges.  Summing zero boundaries gives zero boundary, hence degree
two is preserved.  Cap multiplicity is a linear count of selected edges, so
its final load is the displayed sum.  The two cap assertions follow. ∎

This theorem permits temporary cap debt in a sequential realization as long
as the final displayed inequalities hold.  The production search currently
uses the stronger individually-cap-safe face for its mixed products.

## 4. Blocker additivity

For a circuit `C`, define its **short-run halo** `H(C)` to be all physical
edges at cyclic factor distance at most four from a changed edge, measured in
every component of `F+C`.  A length-two or length-three run can change only
if its boundary segment meets this halo.

The following is the precise disjointness condition needed by the hyperedge
model.

### Definition — blocker-separable packet

A packet `P={C_1,...,C_t}` is blocker-separable relative to `F` if:

1. its facet supports are pairwise disjoint;
2. its short-run halos are pairwise edge-disjoint; and
3. no final length-two or length-three run has a boundary segment meeting
   two different halos.

Condition 3 is retained explicitly because two distant cut sets in the old
cycle can become adjacent after a topology rethread.

### Theorem 2 — exact blocker-current additivity

For every blocker-separable packet,

```text
B(F + C_1 + ... + C_t)
  = B(F) + sum_i partial_B(C_i).
```

Consequently,

```text
short positive runs(final) - short positive runs(F)
  = 17 sum_i (|created_i| - |removed_i|),
```

with multiplicities and the `FIXED` key included.

#### Proof

A short run whose boundary segment avoids all packet halos has exactly the
same incident selected variables before and after the packet, so it cancels
from both sides.  By conditions 2 and 3, every remaining old or final short
run belongs to one unique halo.  Inside that halo all other circuits leave
the factor unchanged, hence its blocker-key change is exactly the one-circuit
current `partial_B(C_i)`.  Summing over the disjoint partition of affected
runs proves the multiset identity.  Multiplying orbit multiplicity by 17
gives the physical count. ∎

### Controlled overlap

For `I subseteq [t]`, let

```text
Delta(I) = B(F + sum_(i in I) C_i) - B(F),   Delta(empty)=0,
```

and define the interaction current by the Boolean-lattice Möbius transform

```text
kappa(I) = sum_(J subseteq I) (-1)^(|I|-|J|) Delta(J).
```

Möbius inversion gives the exact identity

```text
Delta([t]) = sum_(empty!=I subseteq [t]) kappa(I).
```

Here `kappa({i})=partial_B(C_i)`.  Thus additivity with overlap is still sound
if every nonzero higher interaction is explicitly catalogued.  The simplest
controlled-overlap face stores every pair correction `kappa({i,j})` and
additionally proves that all interactions of order at least three vanish;
one sufficient local guard is that no old or final short-run boundary meets
three halos and that pairwise halo intersections do not change when a third
circuit is applied.  Without such a guard or the full interaction catalogue,
base-relative blocker signatures are not composable.

## 5. Topology qualification

Zero owner boundary gives a two-factor, not necessarily one cycle.  Let
`T(C)` be the old/new quotient edge pairing and voltage data retained in the
signature.  A proposed packet must satisfy one of:

1. exact quotient-component and voltage replay followed by literal
   development; or
2. a proved endpoint-pairing theorem implying one nonzero-voltage quotient
   component.

The current implementation always uses item 1.  Component counts of the
individual circuits are diagnostic only; they are not additive scalars.

## 6. Augmenting-chain formulation

Make one vertex for every blocker key.  A transfer signature is a directed
hyperedge

```text
removed blocker multiset  --->  created blocker multiset
```

with side resources consisting of facet occupancy, cap current, and the
old/new topology tuple.  Give it cost

```text
17 (|created| - |removed|).
```

A path or circulation may cancel a created blocker against the same key
removed by a later hyperedge.  Internal keys disappear, leaving only the
boundary current.  A negative-cost packet is therefore a predicted
residence improvement.

For pairwise blocker-separable circuits this prediction is a theorem by
Theorems 1 and 2.  For controlled overlaps, include the certified correction
hyperedges.  In either case the proposed negative-cost chain is accepted only
after exact cap, topology, residence, deep-upper, and blocker replay.

This replaces cubic enumeration of all triples by a sparse augmenting search.
It does not assert that every useful packet is blocker-separable, nor that a
shortest augmenting chain preserves the upper deck.

## 7. Validation artifact

The O3 C++ emitter is

```text
scratch/extract_k17_circuit_transfer_signatures_20260802.cpp
```

and was first validated on the authenticated residence-1,547 factor with
rank-11/12/13 holes `1,513/238/0`.  Its complete `C6` census reports:

```text
1,884 simple C6 circuits
80 individually cap-safe signatures
91 baseline blocker orbits
28 individually connected candidates.
```

The remote validation files are

```text
/home/amodo/or15/work/root_k17_c68b_c6xc6_20260802/
  greedy_residence/after_c16_clean1547_deep1513_238/
    c6.transfer.tsv
    c6.transfer.audit.json
```

The emitter source and validation binary are hashed in the final audit after
rebasing to the final C18-pair leader.

### Successive authenticated descent

The transfer catalogue exposed an objective-ordering bug in the earlier
promotion policy: a connected `C14` row reduced residence while leaving the
rank-11/12 deck unchanged, but was skipped because another row was better in
the deep-lex ordering.  Literal replay promoted that row from `1513` to
`1496` short positive runs.  A subsequent connected `C16` replay reduced the
count to `1479`.  The independent `C18` quotient phase then produced the
first simultaneous three-gate actuator:

```text
positive residence: 1479 -> 1462,
rank-11 holes:       1479 -> 1428,
rank-12 holes:        238 ->  204.
```

The final state in this sequence has `86` positive blocker orbits and keeps
the rank-13 through rank-17 upper deck complete.  This remains a carrier
state, not a depth-three antecedent or a universal word.

## 8. Fail-closed alternating driver

The observed search alternates two exact phases:

1. endpoint-retaining `C6`--`C16` residence/deep rethreads;
2. independently enumerated `C18` quotient rethreads.

The production residence phase is now orchestrated by

```text
scratch/run_k17_alternating_descent_failclosed_20260802.sh
```

with deterministic row selection by

```text
scratch/select_k17_transfer_promotion_20260802.cpp.
```

For an authenticated input model, factor, blocker bank, and expected metric
tuple, the driver:

- acquires one file lock;
- independently exports and verifies the input factor;
- enumerates every cap-safe `C6`--`C16` direct signature;
- runs the reduced `C6+C6/C8`, `C6+(C10/C14)`, and
  `C12+(C6--C14)` exact products;
- literally replays every proposed promotion through cap, topology,
  residence, deep-upper, and blocker audits;
- promotes only a strict residence improvement or a componentwise upper
  Pareto improvement at nonincreasing residence; and
- writes an immutable hashed root with next phase `quotient_c18_import`, or
  declares a scoped plateau and hands off to blocker-graph search.

`C18` enumeration is deliberately absent from this driver and remains owned
by the independent quotient lane.  Thus the two phases do not duplicate
heavy work, and no partially written state can become a search base.

## 9. Exact scope

The theorem proves edge, cap, and guarded blocker-current additivity.  It
does not prove:

- existence of a negative-cost chain;
- connectivity from component-count marginals;
- arbitrary-width upper preservation;
- depth-three residence;
- a source antecedent;
- a lower common-cap compiler; or
- a `k=17` universal word.

Every claimed winner remains subject to literal end-to-end replay.
