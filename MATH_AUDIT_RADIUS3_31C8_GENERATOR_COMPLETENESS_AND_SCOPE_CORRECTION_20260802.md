# Audit of the `k=17` radius-three / `3+1`-`C8` generator

**Date:** 2026-08-02  
**Status:** independent pure-mathematical audit.  The anchored enumeration is
sound within its declared move classes, but two statements in the current
notes need correction before a finite launch: the three-way mechanism
classification is not exhaustive, and a syntactically missing guarded-minor
leaf is not by itself a semantic non-entailment certificate.

## 1. Audited scope

This audit reads the proposed generator and D handoff against the frozen
round-02 Hamming-two ledger and the one-copy octagon theorem.  It makes no
SAT, rank-ten, residence, topology, upper-shadow, or compiler claim.

The authenticated inputs quoted by the D specification replay exactly:

* the occurrence-delta audit has `3664` input rows, `3664` complete keys, and
  largest equality class one;
* the six quoted SHA-256 hashes for the delta and anchored-pair artifacts
  match the files on disk; and
* the anchored two-recut audit has `16667` recuts, `21` anchors, `349642`
  compatible distinct banks, and `169426` joint-zero-265-clean banks.

The `3664` rows are therefore a collision-free residual **support-two test
set**.  They are not a generating basis for support three.

## 2. Parts of the generator that are correct

### 2.1 Causal residues

For a compatible set `S` of at most three baseline one-for-one recuts, every
final occurrence-labelled q1 datum has a minimal subset of `S` on which its
final value first differs from baseline.  Consequently a literal truth table
on all subsets of `S`, together with final deletion/role/capacity data,
recovers every unary, binary, and ternary change.  This is an exact finite
identity; it is not a compression theorem.

In particular, dirty singleton and pair states must remain in the truth
table.  Applying a zero-row filter before forming the ternary residue is
unsound.

### 2.2 Critical-anchor necessity

Let `D(K)` contain every load-bearing occurrence, provider footprint,
capacity, guard, blocker, and transported embedding used by a stored
certificate `K`.  If the occurrence-labelled trace of `K` fails in `B[S]`,
some inclusion-minimal subset of `S` changes a datum of `D(K)`.  Hence the
critical-anchor hitting condition is necessary.

For the original `114930` dual fan, the sharper `A21` statement is also
valid on the declared one-for-one, distinct-base face.  With the two central
roles fixed, a new arm has at most one endpoint-creator recut.  Selected
colour multiplicity is additive.  If the creator child has multiplicity
zero and the triple has positive multiplicity, one of the other two recuts
is already a positive supplier, producing a creator--supplier pair.  The
frozen empty nonanchor join then forces one member into `A21`.

Thus

\[
  21 {16666\choose 2}=2,916,258,345
\]

is a safe raw upper bound before base compatibility, deduplication, and the
other core-anchor intersections.  It is far too large to be a sensible raw
launch; the causal tables and library hitting conditions must be
materialized first.

### 2.3 Simple Boolean `C8` count and canonical form

A simple incidence `C8` projects to a Johnson four-cycle and has exactly one
of two forms:

* star: a common rank-seven core and four singleton petals;
* octahedral: a common rank-six core and the four consecutive two-petal
  sets of a four-cycle.

The core and petal four-set are uniquely recovered in their respective
families.  Modulo cyclic rotation and reversal a four-set has three cyclic
orders, and the alternating cycle has two phases.  Therefore the raw counts
are indeed

\[
 {17\choose7}{10\choose4}\,3\,2
 = {17\choose6}{11\choose4}\,3\,2
 =24,504,480.
\]

Both families are needed for a complete simple-`C8` catalogue.  A physical
canonical key must additionally retain the eight immutable incidence ids,
the active phase, and the directed order of the three removed incidences on
the repeated component.  The mask/core/petal key alone is not an
occurrence-labelled key.

### 2.4 Relative successor-cover logic

If an authenticated unsatisfiable core trace persists before conditioning,
then conditioning on any compatible footprint remains unsatisfiable.  For a
resource-support core this follows by adjoining the footprint seams to any
hypothetical residual saturating family; for a literal core it is ordinary
restriction of an unsatisfiable formula.  Hence a footprint open against
every stored core necessarily disturbs every stored trace, and anchor
enumeration causes no false omission relative to the declared library.

This remains a one-sided proof system.  A library-open packet need not be
q1-feasible.

## 3. Correction: the three listed radius-three mechanisms are not exhaustive

Corollary 5.2 of the generator note lists pair extension, distributed core
cover, and primitive ternary construction.  These do not exhaust the
possible triples because the predicate being classified is a conjunction of
two logically independent parts:

1. final zero-265 cleanliness; and
2. successor-library openness.

For example, a proper subset `A` may already disturb every stored core while
failing one local zero row.  The remaining recut or recuts may repair only
that local debt.  Then the full triple is clean and library-open, but:

* no proper pair satisfies both final predicates, so it is not a pair
  extension as defined;
* one unary or binary disturbance may already defeat every core, so it need
  not be a distributed cover of different cores; and
* no datum need have minimal activation support three.

This possibility is not hypothetical in the move language: the frozen
two-recut census already demonstrates exact dirty-single compensation.

An exhaustive first-applicable taxonomy is instead:

1. **clean proper-subset extension:** some proper subset is both clean and
   library-open;
2. **local-debt completion:** some proper subset is library-open on its
   formal bank but locally dirty, and the remaining edits repair its zero
   rows;
3. **distributed certificate cover:** no proper subset is library-open, no
   load-bearing datum has ternary support, and unary/binary changes on
   different subsets jointly defeat the last closures; or
4. **primitive ternary constructor:** some load-bearing final datum has
   minimal support three.

The error affects only the descriptive classification and the corresponding
handoff/index sentence.  It does **not** invalidate the full anchored-triple
enumerator, which retains dirty proper subsets and evaluates the final bank.

## 4. Correction: `OPEN` for a guarded minor needs a precise proof-system scope

For a resource-support entry, a compatible seam family saturating the
residual demand is an exact certificate that its resource deficiency is
zero.

For a guarded CNF minor or implication bicycle, however, the absence of one
stored clause or one direct implication arc does not prove semantic
non-entailment.  The residual formula may derive the same leaf by another
path.  Thus the proposed `OPEN` row is proof-safe in either of only two
forms:

* **derivation-relative form:** `K does not close` means that none of the
  finitely declared authenticated embeddings/derivations survives.  A named
  missing provenance leaf is then enough, and `SURVIVOR` means only “not
  rejected by this derivation manifest”; or
* **semantic form:** closure means entailment by the full residual formula.
  Then an `OPEN` certificate must include an exact countermodel to the
  required leaf/arc, or the output of a complete entailment procedure.  A
  syntactically missing clause is insufficient.

The rejection side remains sound provided every `CLOSE` row carries an
authenticated final proof.  The safest implementation is fail-closed for
rejection and fail-open for promotion: if no closure proof is available,
promote the packet without claiming semantic non-entailment.

## 5. Additional launch gates for the `3+1`-`C8` face

The raw `49,008,960` count is a count of Boolean simple-cycle keys, not of
active physical `3+1` packets.  Before a row is called an atomic aligned
role-relocating `3+1` `C8`, the independent verifier must establish:

1. all four removed incidences are selected in the current factor and the
   four inserted incidences are the opposite matching;
2. the current occurrence-labelled factor remains within the declared
   degree/owner class after the atomic toggle;
3. the old component pattern is literally `3+1`, and the three cuts on the
   repeated component occur in the aligned directed cyclic order relative
   to the toggle phase;
4. role relocation is measured from immutable occurrence/endpoint
   fingerprints, not a changed numeric component id; and
5. if the catalogue is called *literal* rather than merely a formal q1
   incidence catalogue, all four new turns satisfy the literal age
   recurrence and all protected successor incidences are respected.

The five zero-265 coordinates are downstream necessary rows; by themselves
they do not certify items 1--5.  The reverse-dependency anchor also has to
retain its joint context.  For a tail--head--colour or remote role event, a
bare changed-slot id is not a certificate: store the circuit key, the other
participating slots, and the changed load-bearing datum.  A unary slot set
computed by forgetting this hyperedge context is not an exact reverse cone.

## 6. Exact relation to the `3664` Hamming-two shell

If all `3664` exact jobs are proof-closed, the existing manifests jointly
close the declared support-two one-for-one face.  This licenses calling
support three the next **independent-recut radius**.

It does not license the generator

```text
for pair in 3664:
    append one recut
```

as exhaustive.  A clean triple may have every proper pair locally dirty,
may distribute unary/binary core disturbances across different pairs, or
may contain a primitive ternary activation.  The proof-complete support-
three generator must start from the `A21` anchored triples and intersect the
full causal-anchor conditions, exactly as the main theorem specifies.

The `C8` face is incomparable with Hamming radius: it is one correlated
four-incidence circuit, not four independent recuts.

## 7. Move classes still outside the proposed launch

Even after both declared tables are complete, no general “next-move” no-go
follows.  The following primitive or compound classes remain outside scope:

* simple `C8`s with component patterns other than aligned `3+1`;
* aligned `3+1` `C8`s which change providers but do not relocate the chosen
  forced role;
* a `C6` or `C8` composed with one or more independent recuts;
* two correlated circuits, or `C6`--`C8` composites;
* simple alternating `C10` and longer circuits;
* overlapping/same-base multi-cut edits; and
* segment rethreads or added-cut moves not representable by the frozen
  one-for-one catalogue.

The earlier single-`C6` no-go closes only the authenticated single-circuit
face; it does not close these compositions.

## 8. Launch verdict

The radius-three anchor theorem and the two-family raw `C8` canonicalization
are suitable foundations for a finite generator.  Before launch:

1. replace the three-mechanism sentence by the four cases in Section 3;
2. declare whether guarded-minor `OPEN` is derivation-relative or provide
   semantic non-entailment certificates;
3. add the five physical `C8` validation rows of Section 5; and
4. materialize enough causal/library anchor intersections to avoid the raw
   `2.916`-billion anchored-triple loop.

With these corrections, a negative table is exact only for support-three
distinct-base one-for-one recuts and atomic aligned role-relocating `3+1`
simple `C8`s, relative to the declared successor library.  It is not a q1
feasibility theorem and not a closure of the broader move space.
