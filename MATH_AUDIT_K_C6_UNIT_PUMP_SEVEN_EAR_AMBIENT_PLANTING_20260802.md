# Independent audit of the `C6` unit-pump/seven-ear ambient planting interface

**Date:** 2026-08-02  
**Verdict:** `GO` for deterministic same-cover separation, the exact
residual `b`-factor gate, the private-edge-preserving ternary fusion
interface, and the conditional rooted-host theorem.  `NO-GO` for arbitrary
`S_n` voltage-preserving conjugation, post-hoc union with a completed factor,
use of the small protected-factor theorem, and a transparent two-edge splice.

## 1. Audited sources

The audit used the literal constructions and not only their scalar summaries:

* `MATH_THEOREM_K_TWISTED_THREE_RUN_C6_DYADIC_PUMP_AND_HISTORY_APERTURE_20260802.md`;
* `MATH_THEOREM_A_FIXED_Z_FAR_SOCKET_APERTURE_CYCLE_AND_CORRIDOR_FIBRE_GATE_20260802.md`;
* `MATH_THEOREM_A_ENDPOINT_CONDITIONED_PHASE_COMMON_CORRIDOR_MATERIALIZATION_20260802.md`;
* `MATH_THEOREM_K_DIRECTED_HISTORY_PORT_MONOID_AND_PIVOT_RESET_20260802.md`;
* `MATH_THEOREM_K_TWISTED_C6_PUMP_CORRIDOR_DISTANCE_PLANTING_AND_RESIDUAL_BFACTOR_GATE_20260802.md`;
* `MATH_THEOREM_K_TWISTED_C6_PUMP_CORRIDOR_ENDPOINT_AND_TERNARY_FUSION_GATE_20260802.md`.

The final two source hashes at audit time were respectively

```text
861ee5023d9e70b47ed0358354e0cfc45bada7bce8653967888dd48460490cbc
9bd6ee3468e48eae2d1e344dc4c86ecdbc97e617ae9619d98879d870f6668759
```

The endpoint theorem has its own independent audit, SHA

```text
1995a2ac211e6cd275c7b7c203cb4cd6b08e805b23d9b9049baa3619ba2f7af2
```

## 2. Physical count replay

The twisted pump has `3n` owners and `3n` Johnson edges.  The lower and
immediate-upper edge labels are both squarefree, so their physical counts
are also `3n`.  Its incidence lift therefore has `6n` edges.  Opening one
edge retains all `3n` owners, deletes one projected edge and its lower/upper
labels, and leaves `6n-2` incidences.

The seven-ear local cycle has `28d+35` projected edges.  An exterior ear has
`2d+4` edges and `2d+3` internal owners.  Hence the retained path has

\[
                    26d+31\text{ edges},
                    \qquad26d+32\text{ owners}.
\]

Its physical cap set has size at most `26d+31`; only the occurrence-token
count is automatically exact.  The main theorem deliberately uses the
upper bound rather than asserting cap squarefreeness.

## 3. Cover-preserving scope correction

The first proposed resource proof used uniform `S_n` conjugation.  Its
rank-layer expectation is arithmetically correct but is not a child-voltage
proof: a general `g` replaces the deck generator `tau` by
`g tau g^{-1}`.  Only the affine normalizer preserves the ambient cyclic
cover up to a deck automorphism; it splits each Boolean layer into several
orbits.  Therefore the valid load formula is orbitwise,

\[
              \sum_\alpha
        {m_\alpha|Q\cap\Omega_\alpha|\over|\Omega_\alpha|},
\]

not the aggregate three-layer expression.

This correction is load-bearing.  The main theorem instead fixes the
equivariant pump and chooses the A anchor by Johnson distance.

## 4. Radius and anchor count

Let

\[
 C_0=X-(D^x\cup D^y\cup\{a,b,c\}).
\]

Every central, ray, and connector owner contains `C_0`; since
`|C_0|=r-2d-3`, its Johnson distance from `X` is at most `2d+3`.  A common
lower facet or common immediate-upper cap would put an incident local owner
within one Johnson step of a pump owner.  Thus strict distance `>2d+4`
separates all owners, lower facets, caps, incidences, and occurrence keys
which include an owner/facet.

There are `binom(2r-2,r)` rank-`r` anchors avoiding fixed `z`, while one
radius-`R` Johnson ball has

\[
                         \sum_{j=0}^R{r\choose j}{r-1\choose j}
\]

members.  The pump has `3n` owners.  The strict inequality in the main
theorem is therefore a direct union bound with no independence assumption.

The independent scripts

```text
scratch/audit_k_c6_corridor_radius_and_count_20260802.py
scratch/audit_k_c6_pump_seven_ear_planting_bounds_20260802.py
```

have SHA values

```text
5cf24dc36223ec458790c3a39524ce256b8dc82e1b4e51cbc5db2ed04600d6ee
9f5e518a140f864e0fac8e704d6ad451a4613ec0bd8c5139f1842b6659a9261d
```

and pass.  The latter checks 128 distance regimes.  Its first passing `r`
for `d=1,...,12` is

```text
23, 28, 33, 38, 43, 48, 53, 58, 63, 67, 72, 77.
```

These finite values are an audit only; the proof for `d=O(sqrt(r))` is the
subexponential-ball versus exponential-middle-layer comparison.

## 5. Exact host obstruction

The small protected-factor theorem permits at most `r-2` protected
incidences.  The open pump already has

\[
                    6n-2=12r-8>r-2.
\]

Thus it cannot plant this packet in any dimension.

After deleting the closed pump shores and fixing the disjoint local A bank,
the remaining owner/lower completion is exactly a bipartite `b`-factor.  The
stated Ore--Ryser inequalities are necessary and sufficient.  They are not
automatically implied by Boolean regularity after the `3n` pump vertices
are deleted.

Likewise a completed factor cannot accept the pump by edge-disjoint union:
the first added incidence raises an already saturated degree.  Prospective
completion or an alternating rethread is essential.

## 6. Endpoint and topology audit

The positive connector equations are exactly the directed-history collar
recurrence; exchanging insertions and deletions gives the negative equations.
Both are needed.

A nondegenerate two-edge crossed splice cannot preserve a squarefree lower
palette.  The set identity for the two old and two new intersections forces
the two old facets to agree.  Hence the smallest palette-transparent
private-edge-preserving route in the current catalogue is a ternary Boolean
hex through a pump edge different from the private edge.

For that hex:

* three old components merge to one;
* the typed owner/lower/upper/tail/head inventories agree exactly;
* six collar tests are necessary and sufficient for biresidence; and
* the signed old/new edge sums must agree.

The last equality is automatic only under one coherent physical lift of the
whole hex.  It is not implied by separately valid quotient edges.

The independent endpoint replay script

```text
scratch/audit_k_twisted_c6_pump_corridor_endpoint_20260802.py
```

has SHA

```text
b8a5a3e60d0a0250d6cea071285ad5e5564140254d8f7481e191378896d64d3f
```

and passes 36 pump cases, 21,000 crossed rectangles, and the Boolean-hex
resource/charge identity.

## 7. Absolute versus relative voltage

If `P_P=C_P-e_o`, then

\[
              \lambda(P_P)+\delta(e_o)=\varepsilon.
\]

For a final rooted host the exact identity is

\[
 V_{\rm final}=\varepsilon+sigma_{\rm bg}.
\]

Thus the pump is the sole absolute actuator only when the ambient fragment
and join ledger has `sigma_bg=0`.  A's seven-ear old/new displacement zero
proves that both phases have the same `sigma_bg`; it does not prove that
this common value is zero.

Marking `e_o!=e_*` is the exact private-state correction.  Planting/fusion
uses `e_o`; the recursive private edge `e_*` remains literal and untouched.

## 8. Final scope

The audited milestone closes local same-cover separation and gives the exact
owner/q1, endpoint-history, topology, private-edge, and voltage interfaces.
The first missing theorem is a **prospective pump-aware rooted host**:
simultaneously satisfy the residual `b`-factor/resource rows, expose the two
history-compatible hex partners (or a general ordered corridor), and make
the coherent nonpump background charge zero.

No claim is made for deeper upper shadows, source/envelope binding, exterior
all-width windows, terminal common-cap/compiler matching, or an all-k word.
