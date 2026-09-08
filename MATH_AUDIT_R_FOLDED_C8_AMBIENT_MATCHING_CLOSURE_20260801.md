# Independent audit: folded-C8 ambient matching closure

Date: 2026-08-01  
Audited file:
`MATH_THEOREM_R_FOLDED_C8_ADDRESSED_TRANSPORT_FORCED_EDGE_HALL_AND_COMMON_CAP_GATE_20260801.md`  
Verdict: **PASS**, with all corrections from the adversarial audit incorporated.

The audited theorem SHA-256 is

```text
f5beeb3401aee98f15522bd41bfa8105f84b9b31dc8d5f105c594660f5118185
```

## 1. Address fibres and compiler graphs

Equal cardinalities of every complete cell-type fibre, together with an
injective type-preserving partial address map, are necessary and sufficient
for extending that map to a global cell bijection: complete each finite
fibre independently.  The complete type must contain the actual OR core,
the interval cap, width/grade, and an extensional guard type determining the
entire permitted target neighbourhood.

Such a global bijection is an isomorphism of the one-core compiler graphs.
It transports graph matchings and strict-core assignments edge by edge.
It does not, by itself, prove one simultaneous common-`Q` word; the maximal
source intersection/reconstruction test remains necessary.

The frozen finite audit verifies exactly the unguarded
`(width,OR-core,interval-cap)` fibres for both screens and every
`2<=d<=12`.  Its hashes are:

```text
script   247e4aa93100dd6d7d4c282daf6e2183e4ca95c70049aa0cefc807d72bf24dcc
JSON     c7c99e1cf57ec490bd3a7136349d047a06fa6af249c1a65363cb639a26bf4cd3
payload  8ee79f497d8ae1951dd28d16b61dfa0d7a4b5fa15e9cae455dd28df5ddf21368
```

It does not certify address-dependent guards, owner legality, `q1`, or
complete-cap existence.

## 2. Source-cap gluing

For a fixed combined row family, every feasible source letter lies below
the intersection `K_p` of its upper cap with every incident target.  The
joint system is feasible exactly when:

1. every required lower bound lies in nonempty `K_p`; and
2. every row is reconstructed by its frozen exterior together with the
   incident `K_p`.

The proof uses both containments: feasibility gives
`Q_p subseteq K_p`, while every `K_p` incident with a row lies in that row's
target.  Choosing `Q_p=K_p` proves sufficiency.

Two row systems may be glued only under one common upper cap and the union
of their lower bounds.  The one-source three-row example in the theorem
correctly violates matroid exchange, so cap choices cannot be unioned before
Hall is evaluated.

For zero-charge screen recycling, the actual immediate-left ambient letter
`H` remains unchanged.  In the exact frozen form its lower and upper bounds
are both `H`; every crossing assigned target must contain all of `H`, not
only the smaller abstract screen.

## 3. Forced edges and alternating linkage

After a mandatory new return bank is pulled back through a global type
bijection, it extends to a complete matching exactly when the residual old
graph, after deleting the forced targets and forced cells, satisfies Hall.
This is the standard forced-edge matching theorem.

Relative to a named old matching, deleting its conflicts leaves a partial
matching `M_0`.  The exact rank gain is the maximum number of vertex-disjoint
`M_0`-alternating paths from its unmatched targets to its unmatched cells.
The symmetric difference with a maximum matching proves equality; every
net unit of gain is one augmenting component.  Thus the stated linkage
deficiency and Hall deficiency coincide.

The corrected two-target example lies inside a genuine global type
isomorphism and shows that a legal forced return can destroy the unique
complete matching.  It therefore proves that forced-edge Hall is necessary
for nonprivate placements.

## 4. Preferred full-block refinement

The theorem correctly demotes forced-edge Hall to a fallback.  Under a
genuine source-block refinement:

* every old matched interval has an injective full-block lift;
* every mandatory ray assignment is a certified side cell outside that
  image; and
* all lifted incidence data, including width/grade and guards, are assumed
  admissible.

The transported and packet cell banks are therefore disjoint.

At the cap level, every transported background row contains either a whole
refined block or none of it, so it contains the old block union and does not
shrink any piece cap.  Background reconstruction is automatic once every
block touched by a background row—including one-piece unrefined blocks—has
maximal-piece union equal to its old letter.  The theorem's small
non-contraction example shows this union condition is load-bearing.

For the canonical two-host splits

```text
X_L -> (X_L,L_e),    X_R -> (R_e,X_R),
```

the contraction equations are immediate.  Conditional on actual
owner-legal placement and admissible widths/guards, there is no separate
ambient compiler Hall or cap-conflict gate.

## 5. `q1` and exact remaining scope

The lower and upper `q1` ledgers are coupled because one physical owner edge
simultaneously supplies its intersection and union colours.  The corrected
criterion compares the complete old/even and new/odd edge-occurrence banks
on both shores and requires a type-preserving bijection of the complete
occurrence shores.  The cited alternating `C8` supplies the algebraic maps,
but all old transition occurrences and all new seams still need physical
residence/source-cap placement.

Accordingly the proved boundary is:

* addressed compiler transport and background cap closure are automatic in
  a contraction-exact full-block realization;
* forced-edge Hall/linkage is exact for any nonprivate fallback; and
* owner/residence placement, the physical `q1` sidecar halos, address guards,
  the recycled-screen halo, and regenerative return remain unproved.

No equality theorem or `B(k)+O(1)` conclusion follows from this audit.
