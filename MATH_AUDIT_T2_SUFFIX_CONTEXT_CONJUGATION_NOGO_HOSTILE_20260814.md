# Hostile audit of the `T2` suffix context-conjugation no-go

**Date:** 2026-08-14

**Object audited:**
`MATH_OBSTRUCTION_T2_SUFFIX_CONTEXT_COORDINATE_CONJUGATION_AND_ANCHOR_TOPOLOGY_20260814.md`

**Verdict:** **PASS** for the coordinate-injection obstruction, the finite
anchor-repair/topology failures, and the `D_5` fresh-reset census.  **OPEN**
for a split-aware non-conjugate reset-template SDR at all suffix
semilengths.  This is a hostile self-audit, not an independent audit.

## 1. Quantifier audit

The main no-go is not an impossibility theorem for every finite symbolic
grammar.  It rules out:

1. literal context insertion of one of the seventeen frozen circuits;
2. every Boolean coordinate-injection image mapping its two named endpoints
   to the requested context edge in any of the six target `T2` phases;
3. the narrower repair scheme that keeps all transported owners in cyclic
   order and replaces only failed directed arcs;
4. a whole-word topology recurrence consisting only of the two unary images.

A fresh circuit may discard all old anchors, and a recursive first-return
grammar may place templates inside nontrivial contexts.  Both remain open.

## 2. MSW-law audit

Substitution in

```text
rho(1u0v)=(d,d-rho(mu u),1,d+rho(v))
```

with `u` empty gives `rho(10X)=(2,1,2+rho(X))`.  Taking `v` empty and
`u=X` gives `rho(1X0)=(2s+2,2s+2-rho(mu X),1)`.  Splitting odd/even
positions reproduces the four displayed insertion/deletion formulas.  No
empirical inference is used in these equations.

## 3. Connected-phase lemma audit

The lemma assumes a coordinate injection and rank increase one.  Each
resource must therefore acquire exactly one coordinate outside the old
image.  On an incidence `O subset Q`, choosing different new coordinates
makes the owner image fail containment in the colour image.  Connectivity
then forces one choice globally.  The proof does not apply to an arbitrary
partial resource bijection that is not induced by Boolean coordinates; the
theorem does not claim that it does.

## 4. Signature-quotient completeness

For every circuit resource, a coordinate is completely characterized by its
membership column across the ordered resource list.  Swapping equal columns
changes no mapped owner or colour.  Conversely, placing the multiset of
columns on target coordinates reconstructs the image of every resource.

The frontier audit adds the all-one column for the new fixed up coordinate
and the all-zero column for the unused down coordinate, then partitions
columns by endpoint membership.  It exhausts `56,448` `D_3` images and
`141,708` `D_4` images, with zero selection-valid image.

The stronger full-ground audit permits arbitrary reassignment of every old
suffix coordinate as well.  Columns are partitioned by their ordered pair of
memberships in the two named endpoint owners.  This condition is necessary
and sufficient for those endpoints to map exactly.  The `D_3` run exhausts
`1,034,208` distinct full coordinate images and the partitioned `D_4` run
exhausts `44,334,000`, again with zero selection-valid image.  Rejection
precedes q2 and topology.

Potential pitfall checked: equal membership signatures may arise from a new
fixed coordinate and an old common-core coordinate.  Quotienting them is
still exact because their action on the finite circuit resource set is
identical.  The audit claims no distinction invisible to that resource set.

## 5. Anchor-repair scope

The repair search computes reverse directed distances in the exact
internal-owner exchange graph.  For a fixed cyclic anchor order, path
lengths below the sum of those distances are impossible.  At each total
length it exhausts every length composition and every simple directed path,
then checks global owner/colour simplicity and exact q2 support.  Hence each
reported first solution is minimum in this anchor class.

The `D_3 -> D_4` verifier independently reconstructs all eight circuits.  It
confirms individual q2 safety and one-output component action.  It also
confirms that the `10` bank is resource-disjoint but has three simultaneous
outputs, while the wrap bank has one shared owner and one shared colour.

At `D_4 -> D_5`, one wrap image has no solution through the declared `C36`
bound; no claim is made beyond that bound.  The 25 available circuits are
all independently valid and q2-safe.  Four have two individual component
outputs, and both context banks contain resource conflicts.

## 6. Fresh-reset census audit

For each of the 26 `D_4` context-image suffix edges, the reset search runs
all six prefix channels from the minimum directed-distance sum upward.  All
shorter owner/colour-simple cycles are exhausted before the first q2-safe
witness is accepted.  The resulting minima lie in `C18`--`C24` with the
histograms stated in the theorem.

The conflict verifier checks only the first frozen witness on each edge.  Its
large conflict counts therefore prove that this witness choice is not an
SDR; they do not prove that no choice from all minimum candidates is an SDR.
An exact reset-template theorem must enumerate candidate signatures and solve
that global selection problem.

## 7. Topology and residence boundary

The count `2 Cat_s < Cat_(s+1)` applies to the two whole-word images only.
It does not count templates inserted inside every first-return context or
right-tail tensor copies.  Such placements are exactly the open split-aware
recurrence.

No context result supplies residence, a source planting, or common-history
turn fidelity.  Those gates remain downstream even if the reset SDR is
solved.

## 8. Final gate

The audited conclusion is therefore sharp:

\[
 \boxed{\text{coordinate conjugation is closed; the live route is a fresh,
 split-aware reset-template SDR with verified component action.}}
\]
