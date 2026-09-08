# Odd APH audit: frozen odd-pilot candidate and the current proof-safe frontier

**Date:** 2026-08-06  
**Method:** work-level occurrence audit; no computation or search  
**Frozen primary files:**

* `MATH_THEOREM_ODD_APH_CLEAN_ZERO_CHARGE_ORIGIN_CODE_SELECTION_20260806.md`,
  SHA-256
  `f6fd0b05826cba512519aa3961a83f0e8d51a90b1bed0fe2f62d4a94459217f9`;
* `MATH_THEOREM_ODD_APH_ODD_PILOT_TRAIN_AND_RETIREMENT_20260806.md`,
  SHA-256
  `7d1359e6ad8ed6ccd8663f36905258517909fb674884a2c6d27dfb1f3437b879`;
* `MATH_THEOREM_ODD_APH_FARTHEST_FIRST_HH_CARRIER_ESCORT_20260806.md`,
  SHA-256
  `8884652c973c256d28f4a96cc61a1b8b7da7bb2c5ad39a96f41b9684528293ab`;
* `MATH_THEOREM_ODD_APH_G1_VARIABLE_MASS_HH_SUBSTITUTION_20260806.md`,
  SHA-256
  `0f6f3d7e866508e482b92236da8e5df22dd45573ebdbec3e390ab1622c14289e`.

**Verdict:** **FAIL / DO NOT CITE AS APH.**  The old OC18 and two-block
motif-crossing proofs are false.  The frozen odd-pilot files repair those
crossing counterexamples, but the independent audit found that the register
rewrite (1.9) erases the only proved copy of the atom branch.  The
authoritative theorem frontier remains `OC-ACT4` / `ACT4`.

## 1. The two disproved crossing claims

The superseded two-block train has the exact repeated macro vertex

\[
 H|A|B|H|A
   \leadsto B|H|A|H|A
   \leadsto B|H|H|A|A
   \leadsto B|H|A|H|A.                               \tag{1.1}
\]

Thus the word `BHAHA` occurs at two different crossing counts.

The first odd-pilot draft still decomposed the three-block rotation into two
successive swaps.  On the `H|H|P`-through-`B` row, those two swaps both reach

\[
                              H|M|H|P,                \tag{1.2}
\]

with different arrow numbers.  Simplicity of each individual swap does not
separate (1.2).  Neither invalid theorem may be cited.

## 2. Literal repairs in the frozen candidate

The frozen replacement makes five structural changes.

1. The spare mass-four pair is disjoint from the cart atom: it is the second
   `BB` in the `BBBB` branch or the two unused opposite extremes in the
   balanced four-extreme branch.  It is routed to
   `P|D=01|21`, with explicit `BB,AC,CA` paths avoiding `H|H`.
2. `P=01` travels with every carrier.  At macro checkpoints its physical
   position changes by one block, so the commuting recurrence (1.1) is
   impossible.  The source delimiter `D=21` is restored after every visit.
3. One block crossing has exactly two phases.  The explicit paths
   `P|Y -> Y|P` are tail-clean: no strict state has tail `01` and none
   creates an aligned `H`.  The remainder is one simple six-coordinate
   rotation `U|V|Y -> Y|U|V` with tail `P` fixed.  Consequently (1.2) is not
   a legal two-subphase intersection.
4. The only equal-mass ambiguity is `B/M`.  A selected-support `M` holds the
   separate literal tag `D=21 -> bar D=12` throughout the six-coordinate
   path.  A recorded residual ticket holds the already proved nonextreme
   collar tag.  The endpoint train type is supplied by the task ticket, and
   subtracting its mass from the six-coordinate mass determines `Y` outside
   that tagged equality.
5. Setup and task sweeps have different protected register states.  If the
   final atom state is `Q_q`, the ordered collar class `r` is copied at the
   collar to an injective state `widehat Q_(q,r) != Q_q`.  This mandatory
   change prevents the first task from retracing the cart-prepositioning
   path, including the zero-task row.  The carrier endpoint is
   `H|H|P|K`, so `P` separates the temporary cart from a collar record
   `R_0=H|H`.

All five repairs are literal graph-state records, not semantic labels.

## 3. Scalar and resource rows which pass

The following rows are unchanged and proof-safe.

* The sliding four-extreme argument gives a balanced support of span at most
  thirteen unless `BBBB` occurs; the length threshold is `64`.
* The selected source support has zero signed charge, so deleting it before
  cancellation preserves the residual imbalance and gives `t<=3`.
* The pilot/delimiter source has mass four and is disjoint from the cart,
  collar, zipper block, and residual occurrences.
* Every residual substitution preserves mass, leaves `M` at its source
  address, and obeys the farthest-first no-old-ticket invariant.
* The `G_1` return block `Z_d` satisfies
  `mass(X)+2=mass(X')+mass(Z_d)`, and only the two proved extreme-capacity
  rows need one preliminary residual.
* Adding the unchanged pilot mass to each task and collar endpoint changes
  none of those identities.
* The final task collar has mass four.  The candidate explicitly performs
  `K_f -> R_r` before erasing the origin code, rather than treating mass four
  as an order record.
* The protected `Q` register, work suffix, collar, and selected first row are
  on the already audited disjoint supports, and every nonzero work edge lies
  after `p_1`.

## 4. The decisive failed register row

The clean setup proves injectivity using the triple

\[
                 (D,\ Q_q,\ \hbox{source collar}).        \tag{4.1}
\]

It explicitly assigns the atom branch to `Q_q`.  The pilot theorem then
rewrites `Q_q` to `widehat Q_(q,r)` on the assertion that the work/origin
normal form already determines `q`.  No independent one-erasure decoder for
that assertion is proved, and the endpoint table is not injective in `q`.

Even after the later collar record `R_r` is adjoined, the collisions include

\[
\begin{array}{c|c}
r=0&(q,r)=(1,0),(3,0)\longmapsto(R_0,Q_0),\\
r=1&(q,r)=(0,1),(1,1)\longmapsto(R_1,Q_2),\\
r=2&(q,r)=(0,2),(1,2)\longmapsto(R_2,Q_3).
\end{array}                                             \tag{4.2}
\]

The reverse setup paths were permitted to use distinct `Q_q` values to
separate intersecting work projections.  Holding the coincident endpoints
in (4.2) during teardown therefore does not prove source disjointness.  The
claim that `R_r,widehat Q_(q,r)` recovers the atom branch is circular.

The explicit tail-clean rows (2.2) pass their stated local checks.  That
local success cannot repair the earlier loss of `q`.

## 5. Secondary crossing decoder retained for the next repair

For a strict state of the simple six-coordinate rotation, the candidate
decoder proceeds in this order:

1. the literal tail `P` and restored prefix locate the six-coordinate
   window;
2. the task/ticket phase gives the ordered train pair `U,V`;
3. local mass gives `mass(Y)`;
4. `bar D` or the collar tag separates `B` from `M`; and
5. the chosen path is simple, so its state gives the microstep.

This decoder is not reached as a complete APH proof until the atom branch
has a persistent independent copy.  After such a copy is supplied, it must
still be audited simultaneously for all translated source occurrences, the
crossing of `D` itself, successive task visits, the guarded eight-coordinate
collar regeneration, and the reverse private-gap teardown.

## 6. Exact scope and authoritative status

The sufficient length condition is

\[
                         m-3\ge64,
                 \qquad k=2m-1\ge133.                \tag{6.1}
\]

The selection and pilot resource bounds apply to odd `k>=133`; they make no
claim for smaller odd dimensions.  A completion now needs either an
additional persistent atom-branch tag disjoint from the `Q` order record, or
a complete proof that the literal work normal form retains `q` at every
strict reverse-setup state.  The proof-safe ledger is

\[
\boxed{
\begin{array}{l}
\text{clean zero-charge selection and scalar task schedule: proved},\\
\text{old OC18/two-block crossing: disproved},\\
\text{odd-pilot crossing and retirement: failed at the atom-branch copy},\\
\text{odd APH and the full odd package: not yet certified.}
\end{array}}
\]
