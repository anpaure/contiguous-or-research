# Audit of the exact-`B` / `B+1` zero-charge synthesis

**Date:** 2026-08-03  
**Audited file:**
`MATH_SYNTHESIS_EXACT_B_BPLUS1_ZERO_CHARGE_COINSTANTIATION_20260803.md`  
**Method:** theorem-by-theorem scope and quantifier audit; no computation.

## 0. Audit verdict

**PASS as a conditional synthesis.**

The synthesis proves only implication theorems.  It does not claim that
`PPC(1)` or `PCC(0)` exists, and it does not promote a bounded-defect router
to a sharp `B` or `B+1` result.

The central terminal-charge identity is exact:

\[
                         \tau=c+R(H).
\]

The following deductions are valid.

* `tau=0` plus the general lower bound gives exact `B`.
* `tau<=1` gives `B+1`.
* a uniform terminal bound gives `B+O(1)`.
* on the pivot branch `c=1`, so `B+1` forces `R(H)=0`.

## 1. Lower-side scope

### Verified

The antitone coupling theorem proves exact anonymous row balancing for an
arbitrary residual degree sequence and arbitrary collar columns, including
the displayed Gale min-max value.  The rank-separated named-target theorem
proves an equitable integral containment assignment.

The cross-SCD sparse-top theorem is also incorporated with its exact scope:
on its `2r`-coordinate model it gives named owner flags when the residual
top-density cut holds, including the complete central `d`-rank band, but not
the full strict lower ideal or the other parity.  Its file hash at the time
of this audit is
`a4d954e2d35e6a17e24099a3b6d28b9731f6f7d47d5a14533dad9e29ca62359e`.

### Not inferred

The synthesis correctly does not infer that these two integral points are
compatible.  Neither source proves that the named targets assigned to one
owner form an inclusion flag, nor that the flags appear as suffix unions in
one literal source word.

The fractional configuration theorem supplies a canonical fractional point,
not an integral matching.  Its one-SCD obstruction also prevents citing a
fixed symmetric-chain partition as the missing rounding.

## 2. Selector and topology scope

### Verified

The protected simple Catalan theorem gives the abstract target
`1+1_D` and row-fixed Ryser reachability.  The component-port theorem gives
the exact path-count identity, ordinary Hall criterion for one path plus
cycles, and ordered Hall criterion for a direct Hamilton path.

The fixed-factor completion theorem is used only as an exact reduction to
a rainbow base, a head-colour master, and predecessor-fibre Hall.  It is not
used as an all-parameter existence theorem.

The protected forward-atlas theorem is also correctly scoped.  Strong
connectivity and bidirectional occurrence of every upper colour prove full
graphic rank and raw forward supply, but a fixed strict order leaves only
the consecutive Hamilton path as a `W-1` edge tail/head-injective choice.
The synthesis therefore leaves the Hamilton order/selector open.

### Not inferred

The synthesis correctly separates:

* an abstract colour-margin selector from literal tail/head occurrences;
* one-path-plus-cycles from a Hamilton path;
* palette-preserving switches from a change in path-component count; and
* prospective octagon supply from serial pivot-disjoint accessibility.

No claim is made that row-fixed Ryser switches are automatically Boolean
hexagons.

## 3. All-width scope

The all-width file proves the retained-witness equivalence, forced-cut-core
criterion, rainbow witness-bank equivalence, component-omission Hall
criterion, and monotone-pivot transparency.  The synthesis uses each only
in its stated direction.

In particular, it does not use the `2 Cat_m` duplicated q1 occurrences as
an all-width safe-opening theorem.  It retains the additional forced-core
or rainbow-bank condition.

The rooted-forest chain is explicitly scoped to the strategy in which each
higher witness is already carried by `Q_0`.  The synthesis does not claim
that this condition is necessary for every possible final Hamilton path.

## 4. Pivot scope

The pivot implication is used only after assuming:

1. a literal pre-insertion source;
2. the containment `X subseteq A_-1 union A_1`;
3. the flat owner-window and residence conditions;
4. a transported background compiler fixed away from the pivot cells; and
5. literal assignments for the singleton and two rays.

Under those assumptions, old interval ORs survive exactly and the local ray
compiler has no residual loss.  The synthesis does not infer a source
antecedent from the owner path alone.

The one-token overlay theorem is incorporated with its updated exact scope
(theorem SHA
`2635e32142db89714177e0b017a5f98d2e20fb91e11864cf22905b4ec40efcdd`,
audit SHA
`2717301fd4129cfe539d3b0adcdd16a89ba529398c325ef88460a697fe18b926`).
The exact transition sphere is `|H cap J|=R-D`; its graph is connected; and
the fixed-bank avoidance criterion is

\[
 |F\cap H|\le D-1,
 \qquad |F\setminus H|\le R-D+1.
\]

The synthesis uses this only to remove a token-coordinate orbit/avoidance
obstruction.  It does not infer fresh-host, cap, all-width, or occurrence
acceptance from token reachability.

## 5. Common-cap and router scope

### Fixed-state quantifier

The common-cap graph is formed only after one complete cap/guard/occurrence
state is fixed.  The synthesis preserves the valid quantifier

\[
             \exists c\ \forall U,
\]

and rejects `forall U exists c_U` and different states in the two
coordinates.

### Coordinate semantics

The audit confirms that the two Rado coordinates are the two physical
occurrence coordinates required by every ticket in the union of the two
cross-ray matchings.  They are not the two ray matchings themselves.  The
synthesis states this explicitly.

### Background semantics

Frozen named background routes and adaptive matroid contraction are kept
separate.  Deleting one chosen route is not identified with contraction.

### Product closure

The synthesis correctly requires allocation of shared capacities and global
product closure.  Two marginal full-rank Rado systems are not promoted to a
common compiler in the presence of correlated representative pairs or
cross-ticket constraints.

### Abstract factor versus physical router

The regular-factor theorem is used only conditionally on private literal
claim-to-port prefixes and one simultaneous typed suffix linkage.  The
balanced-factor theorem itself says dense Ferrers load is orthogonal to
suffix rank; the synthesis does not derive one from the other.

The frozen common-cap/private-router inputs are bound to theorem hashes
`108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc`
and
`2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0`,
with audit hash
`0f4211dd6a3dd79d7e50669285baeb12dd3f45ab1957a2094ef1306a7338d67a`.
In particular, the `h=2` protected middle-levels factor supplies only an
abstract incidence factor.  It does not supply capacity-faithful physical
ports, private literal prefixes, or a typed full-rank suffix router.

## 6. Diagonal-router capacity audit

The two seemingly conflicting diagonal statements refer to different
capacity models.

1. In the native interval-address model, overlapping intervals are distinct
   cells and boundary letters are semantic incidence labels.  The interval
   diamond gives a full source-free dual-role linkage.
2. In the stronger source-node-priced model, every route uses two source
   capacities, yielding the `W/2` cut unless capacities are doubled or the
   upper attachment is private.

The synthesis does not combine the positive theorem from Model 1 with a
capacity assertion from Model 2.  It also preserves the condition that the
common cap must allow the upper-turn occurrence to serve both roles.

## 7. Type audit

The native diagonal pair and the q1/q2 ladder are nested upper Hasse types.
The canonical folded ticket is an incomparable opposite-ray type.  The
first-exit converter file proves:

* exact native conversion only for `d=2,j=1`;
* a lower bound of `d` Hasse edges and `d+1` Boolean values for a general
  cap-preserving folded fan; and
* longest branch `max(j,d-j)`.

The synthesis therefore correctly leaves a full-depth converter in
`PCC(0)` and does not require it in `PPC(1)`.

## 8. Sharp-charge audit

This is the most important scope correction.

* A common-cap theorem with deficiency `O(1)` proves only an additive
  constant after terminal repair.
* Exact `B` requires scaffold excess zero and terminal repair zero.
* The pivot `B+1` scaffold has excess one, so any nonempty repair pushes the
  conclusion to at least `B+2`.

The synthesis keeps these three levels separate.

## 9. Parity and regeneration audit

The odd equal-shore diagonal theorem is not cited as an even construction.
The even bilayer theorem is treated as exact accounting conditional on an
even chronology, not as existence of that chronology.

The direct per-dimension implication and the inductive spine implication are
also separated correctly:

* direct certificates need not form a spine;
* an inductive proof needs one compatible infinite sequence, not merely one
  good child in each dimension;
* parent-local occurrence menus cannot be reused without child-local
  authentication.

## 10. Exact status of the two named missing theorems

### `PPC(1)`

This is a single co-instantiation theorem, not a proved lemma.  Its known
projections are anonymous lower balance, rank-separated containment,
component-port Hall, all-width retained-channel criteria, and local pivot
transparency/compiler closure.  Their intersection and regeneration remain
open.

### `PCC(0)`

This is also unproved.  In addition to the common lower and all-width rows,
it requires a literal cap-two occurrence selector, one component, full-depth
folded type conversion, exact two-coordinate routing, and global product
closure in one state.

The synthesis correctly scopes `PCC(0)` to the current diagonal/folded
architecture; it is not asserted necessary for every conceivable exact
construction.

## 11. Final proof-status ledger

| Statement | Status |
|---|---|
| terminal-charge implication | proved |
| exact anonymous lower balance | proved |
| equitable rank-separated named containment | proved |
| cross-SCD sparse-top / central-band named flags | proved on its density face |
| balanced named owner flags in one chronology | open |
| abstract protected cap-two target | proved |
| protected rooted atlas full graphic rank / raw forward colour supply | proved |
| literal cap-two selector and one-component chronology | open |
| component-port Hall criteria | proved |
| rainbow witness/omission Hall criteria | proved |
| protected Catalan path satisfying them | open |
| pivot upper transparency and local ray compilation | proved conditionally on the source/collar |
| one-token transition sphere, connectivity, fixed-bank avoidance | proved |
| native one-coordinate dual-role router | proved on its exact interval-address face |
| canonical two-coordinate common compiler | conditional on lifting, state, and product closure |
| `PPC(1)` | open |
| `PCC(0)` | open |
| `nu(k)<=B(k)+O(1)` | open |
| `nu(k)<=B(k)+1` for all `k` | open |
| `nu(k)=B(k)` for all `k` | open |

## 12. Audit conclusion

The synthesis is proof-safe.  Its main mathematical contribution is the
sharp separation by terminal charge and the identification of one
co-instantiated missing theorem for each branch.  No hidden marginal
existence, capacity reuse, type conversion, or per-dimension quantifier is
treated as a global construction.
