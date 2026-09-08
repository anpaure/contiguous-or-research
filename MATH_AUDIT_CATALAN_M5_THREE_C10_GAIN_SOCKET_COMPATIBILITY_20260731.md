# Compatibility audit for the repaired `m=5` Catalan state

Date: 2026-07-31  
Status: exact finite central/socket/all-depth certificate; strict-run and
fixed two-label alignment fail; intact-path residence is impossible

## 0. Verdict

The synchronized three-\(C_{10}\) packet repairs the standard `m=5`
turn/decoration failure, and the repaired final decoration now also has an
explicit physical endpoint closure.

The proved chain is

\[
 \boxed{
 \text{palette }84/84
 \to \text{joint occurrence matching }210/210
 \to \text{gap forest + trace forest}
 \to \text{42-path }J(10,5)\text{ forest}
 \to \text{one literal 252-cycle}
 \to \text{complete flag tower at 46 cuts}.}
\]

The clean rotation group has order \(h=1\), so primitive voltage is vacuous
after the one-cycle topology has been proved.  This is a positive physical
`m=5` Catalan-linear-matching base.

Two qualifications remain essential.

1. The two disjoint private objects proved by the repair audit are
   **lower gap-owner paths**, not physical endpoint sockets.  The final
   42-connector closure is proved separately; its transport through the
   four-state glue cube and its ownership by a recursive parent are not.
2. The packet is not a monotone component-tree operation.  It temporarily
   merges and splits factor components.  The complete two-glue cube is a
   valid decorated physical rethread cube, but not the original aligned
   two-edge component tree.

The final full two-glue closure does have complete all-depth flag support.
It is nevertheless not compiler-ready: the 42 path interiors contain 31
bounded length-two positive runs, so depth-two residence fails under every
intact-path ordering, reversal and socket choice.  An interior rethread is
necessary before any chain-aligned envelope or lower compiler can exist.

## 1. Coordinate-by-coordinate status

| Coordinate | Verdict | Exact certificate |
|---|---:|---|
| Turn palettes | PASS | All 84 lower and all 84 upper turn colours occur. |
| Joint alternating SDR | PASS | Augmented graph matching `210/210`, with all 12 standard ports forced selected. |
| Gap state | PASS | In all four two-glue states the occurrence-named gap graph is a forest and its perfect matching is unique. |
| Private gap ownership | PASS | Disjoint paths `[82]-g-[84]-g-[88]` and `[50]-g-[52]-g-[56]`. |
| Root/final linkage | PASS | Common-core rank `197`; deficiency 13 is routed by 13 vertex-disjoint augmenting paths, plus four alternating 4-cycles. |
| Binary trace | PASS | The exact forest predicate passes in all four cube states. |
| Strict run/protected breaker | FAIL | Every cube state violates the strict run rule; one of the two preglue components lacks a protected `0^4` breaker. |
| Fixed aligned one-effective-edge face | FAIL for both labels together | Component counts are `(2,1,1,1)` for `(none,g0,g1,both)`; either singleton is an aligned salvage, but the two labels are not one fixed graphic tree image. |
| Physical Catalan forest | PASS | 252 vertices, 210 Johnson edges, exactly 42 paths. |
| Endpoint socket topology | PASS at final state | 84 formal ports, 297 legal formal connector pairs; one colour-injective 42-edge connector set gives one 252-cycle. |
| Final all-depth flag tower | PASS on the full two-glue closure | All ranks \(5\pm q\), \(q=1,\ldots,5\), occur; 46 cuts retain the tower, including 39 connector cuts with all 42 paths intact. |
| Intact-path depth-two residence | FAIL | 31 internal `0-11-0` collars on 18 paths survive every path permutation/reversal/socket choice. |
| Interior rethread | REQUIRED on this source, but solved by item 2188 on another matching | Defect collars have old-edge hitting number 29; after one possible opening-cut credit, any rethread deletes at least 28 old forest edges. No pairing-private all-depth single connected \(C_4/C_6/C_8/C_{10}\) move improves the short-run score; one nonprivate \(C_6\) improves three length-two runs. A separate 119-partner rethread is internally residence-clean. |
| Primitive voltage | VACUOUS | \(q=9\), \(s=3^{v_3(9)}=9\), hence \(h=q/s=1\). |
| Pairing transport/private physical ownership | OPEN | No common connector/pairing transport across all four glue states is certified. |
| Lower compiler | BLOCKED on intact paths | Residence fails before schedule/envelope/Hall/common-cap; a successful interior rethread must be re-audited through all of those rows. |

The endpoint graph has 81 distinct endpoint vertices, 273 distinct physical
Johnson seams and no zero-degree formal port.  The explicit closure uses 42
distinct connector edges and 42 distinct connector colours on each shore.
In the closed outer-incidence profile, each shore has 168 colours of
multiplicity one and 42 colours of multiplicity two.  Thus the final
connector is cap-two exact; no repeated connector colour is being excused
by the retained forest.

## 2. The component-alignment correction

Commuting the repair packet before the two standard glues changes component
orders as follows:

\[
 [36,72,144]\longrightarrow[36,216]
 \longrightarrow[36,48,168]\longrightarrow[120,132]. \tag{2.1}
\]

In particular the second \(C_{10}\) splits a component after the first has
merged components.  Therefore the packet is a valid correlated physical
rethread, not a sequence of monotone edges in the original three-component
tree.

There is a genuine aligned singleton salvage.  From the repaired preglue
state \([120,132]\), either `g0` alone or `g1` alone gives a Hamilton factor,
an augmented-perfect decoration, a unique gap forest and a trace forest.
Choosing one glue therefore gives a one-edge component-tree face with one
of the two private lower-owner paths.  Choosing both also gives a valid
Hamilton/decorated state, but is not a two-edge aligned spanning-tree face.

This distinction is exactly why gap ownership, common-core linkage and
physical socket pairing remain separate coordinates.

It also separates two notions of binary acceptance.  The mark trace is a
forest in all four states, but every state has cyclic zero-runs of length
two and odd one-runs, so the stronger rule

\[
  \text{zero-run length}\ge4,
  \qquad \text{one-run length even}
\]

fails everywhere.  One preglue component has no protected `0^4` block;
after either glue, the Hamilton component has two.  Hence this finite packet
cannot be inserted unchanged into a recursion that requires the strict-run
state at every boundary.

The packet is also not a sequence of fixed-decoration transparent moves.
Its exact `(lower palette, upper palette, augmented occurrence)` deficit
triple is

\[
 (3,3,3)\to(2,2,2)\to(1,1,1)\to(0,0,0),
\]

so no exact decoration exists at the input or first two intermediate
stages.  The 13-path common-core linkage is an end-to-end macro certificate;
it is not a claim that each `C10` preserves one SDR.  The standard `g0/g1`
glues are tested only after the output decoration has been installed.  In
the terminology of
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`,
those later glues lie on a fixed-decoration transfer face, whereas the
three-`C10` packet is an atomic repair router carrying temporary matching
debt.  Interleaving a recursive glue inside the packet would require the
full intermediate feasible relation and is not certified here.

## 3. Exact physical closure

The independently reconstructed final forest has path-length histogram

```text
1:3, 2:2, 3:11, 4:8, 5:2, 6:1, 7:4, 8:3,
9:2, 11:1, 12:1, 13:2, 16:1, 29:1.
```

These 42 lengths sum to 252.  The endpoint catalogue has formal-port degree
between 4 and 13 and connected component projection.  The frozen endpoint
audit supplies the literal connector list and canonical 252-cycle and checks:

* every forest and connector edge is Johnson;
* forest and connector sets are disjoint;
* every vertex has final degree two;
* every formal endpoint occurrence is used once;
* the 42 connector colours are injective separately on both shores, giving
  the exact cap-two outer profile; and
* the final graph is one cycle on all 252 middle vertices.

Thus the socket/topology gate is genuinely positive for this final state;
it is not inferred from socket multiplicity.

## 4. What remains for the `k=10` exact word

For the corresponding even problem,

\[
 W=\binom{10}{5}=252,qquad d(10)=2,qquad B(10)=254,
\]

and the lower compiler has

\[
 \sum_{r=1}^{4}\binom{10}{r}=385
\]

targets.  The auxiliary `ML(9)` cycle itself is not the required upper
carrier: each consecutive pair crosses the two rails, so every rank-six
union contains \(\infty\), missing exactly the \(\binom96=84\) rank-six
targets avoiding \(\infty\).

The exact next pipeline is therefore:

1. rethread the path interiors.  Every final word must omit an old edge from
   all 31 immutable three-edge defect collars.  Their transversal number is
   29; after crediting one possible opening cut, the rethread itself must
   delete at least 28 old forest edges;
2. replay both immediate palettes, the final decoration, linear-forest
   physicality, the entire flag tower, the depth-two run row, directed
   boundary reachability and the gain--Brauer socket/voltage root;
3. only after those rows pass, enumerate legal length-254 chain-aligned
   two-hole schedules and audit maximal envelopes and middle-row ORs;
4. build the complete 385-target lower-cell atlas, run ordinary Hall, and
   then enforce the maximal-common-cap equations; and
5. decode and replay all \(2^{10}-1=1023\) targets.

The first exact fixed-connector actuator census closes single connected palette cycles
\(C_4,C_6,C_8,C_{10}\): no pairing-private all-depth row improves the run
score.  A nonprivate \(C_6\) three-path braid does reduce the best all-depth
short-run count from 74 to 71 while leaving 47 valid cuts, so interior
rethreading is compatible with palettes and full-shadow support in a
nontrivial finite case.  It is not residence-complete and, because \(h=1\),
does not test nontrivial voltage.  The larger residence-clean matching of
item 2188 changes 119 partners and removes every internal defect.  Its
unjoined fragments still miss 21 deeper targets.  The exact pair-safe socket
audit then closes endpoint-only joining of those fixed paths: both sockets of
one component have safe degree zero, and one opening cannot destroy the two
forced disjoint short-run collars.  Thus the current finite gate is a further
interior/socket-trace actuator coupled to all-depth chronology, rather than
the existence of an interior rethread or a marginal endpoint matching.

Marginal Hall is not a substitute for the final common-cap row.

## 5. Scope of the reported frontier counts

The reported `585` palette-perfect and `452` matching-perfect outputs arise
from a scoped candidate-pool search built from 281 first-switch candidates
and 182 two-switch deficit-`(1,1)` states.  They are not an unrestricted
three-switch census.  The literal three-\(C_{10}\) witness and the frozen
central/endpoint audits do not depend on promoting that scoped census.

## 6. Audit artifacts

The central repair is frozen in
`MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`
and its deterministic audit.  The independent physical reconstruction is

```text
scratch/audit_catalan_m5_three_c10_endpoint_socket_20260731.py
scratch/catalan_m5_three_c10_endpoint_socket_20260731.audit.json
```

The current endpoint script SHA-256 is
`95fee800565d6f412a46c31f46dd426253a765ac35821ff8d5677040a0e7b22b`;
the current JSON SHA-256 is
`3af1f9d4e2875b5896d8db355d6ed8f7d72f592f57e634f9d25125f5413b53a4`;
its canonical payload is
`4596f812a44a7b1edf0c1ff4acbadcf9a5f4a252c06ba7c7c86226f235c3efa4`.
It authenticates the current central theorem SHA-256
`1be05f74fbbc0f050117d3d04e9720bc972d5838c623af2636b838a4884dbd66`.

The authoritative downstream all-depth/residence audit is

```text
THREAD_A_M5_THREE_C10_DOWNSTREAM_COMPATIBILITY_AUDIT_20260731.md
scratch/audit_thread_a_m5_three_c10_downstream_state_20260731.py
scratch/thread_a_m5_three_c10_downstream_state_20260731.audit.json
```

with SHAs respectively
`bd3cc11ac3682c5d7a244099e736f5a707884edac5d1554dde7ada0805f20c60`,
`f97eaa7d8457f619e06fa91a501142a5b9fb0af0818fc0b31ae10ef318778041`
and `91201d7281bde581ef01a58778b6e8edbea8dcb7da37d185c76f1771b91b2a5e`;
its canonical payload is
`19752a1d1ec5d02ad5ab18479228a85d6128caa8b1bc51cc0226e509c8f31549`.
That frozen JSON pins the earlier central/endpoint snapshots `78c207...` and
`1bc199...`; the mathematical replay is unchanged, but byte-authenticated
lineage must not conflate those snapshots with the current files above.

The interior-rethread theorem and exact finite census are

```text
MATH_THEOREM_CATALAN_INTERIOR_RETHREAD_GAIN_BRAUER_ACTUATOR_20260731.md
scratch/audit_catalan_m5_interior_rethread_actuator_20260731.py
scratch/catalan_m5_interior_rethread_actuator_20260731.audit.json
```

Their SHAs are respectively
`37667dd88c3d204843c058d72d228d8f2190d0a426776799d5ecc425ae23dd54`,
`ac54bd368866f0b96de791404a20608961a001d760689b1c29f23b4d8c7a8131`
and `d26e0d91d3fcbaef6f279ffe15c1f9d92b7a32611d9ebd54b2ca58e7cec22f04`;
the canonical payload is
`3be077f86990753a2f9c2ca57ca420fc165fc5ea78135c6985e7e5798507e107`.

The item 2188 endpoint-only obstruction is frozen in

```text
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_SOCKET_DEAD_COMPONENT_NOGO_20260731.md
scratch/audit_catalan_m5_residence_clean_socket_dead_component_h2_20260731.py
scratch/catalan_m5_residence_clean_socket_dead_component_h2_20260731.audit.json
```

with SHAs respectively
`083dcb456e629a1fa8abb47797ba2ade17ce8fe108d007bc444a4e80b3093cfc`,
`19873b98966cb67e95ec31d23593d54f47ed3f32a76e02d44aeb25659bbd6ed1`
and `28fc239f52fef28715f0bf986a56ca7f53ffb138cd007cba3f76debfb3bcfe3a`;
its canonical payload is
`2f6692b8b3e884dd715167f9d763b884c7dc7d693066e5adf44d07de6d314b16`.

The transparent-microstep side of the comparison is frozen in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`, SHA
`3c5007b3759e94a635593eaf83980dd93819c7f3d9bf8e280ab50fa46678b6e2`.
Its audit script/JSON SHAs are
`5c5a697cf8a6183391d14b11c2b6c334f342c5eb1d0d0789b77b2e915d22d2d9`
and `966b182cf4c830d7b3e1ed9ede74d5e157afe31014abe12ba2f41c033d7cfcbc`;
the canonical payload is
`9dc85bd68adce34377e25927be6e9d59c159f6e36ae92168012518709834e07d`.

The independent fail-closed correlated-state replay is

```text
MATH_AUDIT_THREAD_D_M5_THREE_C10_CORRELATED_STATE_COMPATIBILITY_20260731.md
scratch/threadD_audit_m5_three_c10_state_compatibility_20260731.py
scratch/threadD_m5_three_c10_state_compatibility_20260731.audit.json
```

with SHAs respectively
`a15c6aa078e1c9478d5e2c366389ea3489b5d7e9ecc1941a3ef06dec15509f50`,
`4f347dda4eade9a92f657f09abf106f14674b9af338798bfaea4793df9894e02`
and `bd163ba4d64eae54fba479328870497912aa1da2c4f30cedcf963a92fa8bb480`;
its canonical payload is
`49474c9c07e0e07568cdf023ae68f8fd2108ca4d8ce72f22be5ddaf8089f0290`.

The algebraic need for deficient parent rails and a directed reachability
state is proved in
`MATH_THEOREM_CATALAN_PASCAL_SECTOR_DETERMINANT_AND_TWO_COPY_NOGO_20260731.md`,
SHA `a4c89a962b59eac35556e7c4c1fab42bf24757ec86029e4d691bfd43a9380659`.
Its replay script/JSON SHAs are
`fb4580b511fa8ba10e5aa9758f3a947cd9c698f6f3feca21716991ed463691a7`
and `133c4d1410c9b9b7fce174d50b03d6dc2cff657ddc90a94cb680679209877ac3`.
