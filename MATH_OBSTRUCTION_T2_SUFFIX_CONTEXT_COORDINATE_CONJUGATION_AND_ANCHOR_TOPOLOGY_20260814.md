# The finite `T2` suffix atlas has no coordinate-conjugation insertion grammar

**Date:** 2026-08-14

**Status:** unconditional exact obstruction to transporting any of the
seventeen frozen `D_3/D_4` actuators by a Boolean coordinate injection under
`X -> 10X` or `X -> 1X0`, even after an arbitrary permutation of the complete
old ground set and a transition to any of the six `T2` prefix channels.
Exact directed-path
repairs exist, but they leave the `C14`--`C24` atlas, lose resource or
component-topology compatibility, and do not furnish an insertion-closed
spanning recurrence.  This does not rule out a genuinely new reset-template
grammar.

## 0. Outcome

The frozen finite atlas in
`MATH_THEOREM_T2_DYCK_D3_D4_SPANNING_ACTUATOR_ATLAS_AND_CONTEXT_GATE_20260813.md`
does not conjugate through either Catalan insertion.

1. Literal endpoint-correct transport fails for all `34` pairs consisting
   of one of the `17` frozen circuits and one of the two context moves.  All
   mapped owners remain internal and all mapped incidences remain
   Boolean-legal, but `37` transported old incidences fail selection for
   `10`, and `51` fail for primitive wrapping.
2. This is not repaired by changing one of the six prefix phases or by a
   coordinate relabelling.  A frontier-local audit checks `198,156` distinct
   images.  The stronger all-ground audit checks `1,034,208` endpoint-correct
   images of the `D_3` bank and `44,334,000` images of the `D_4` bank:
   `45,368,208` in total.  **Zero preserve the selected incidences**, before
   q2 support or topology is even imposed.
3. Keeping the transported owners as cyclic anchors and replacing failed
   arcs by shortest directed exchange paths does give q2-safe circuits.  For
   `D_3 -> D_4`, their exact anchor-preserving lengths are

   ```text
   10:    C22,C22,C26,C20
   wrap:  C28,C24,C24,C24.
   ```

   Thus the `C14`--`C24` class is already not anchor-closed.
4. The repaired `10` bank is pairwise owner/colour-disjoint and aggregate
   q2-safe, but its simultaneous toggle meets `39` old lifted components and
   leaves **three** outputs of shore-owner lengths `230,253,756`; its
   reduction is `36`, not the `38` required for one output.  The repaired
   wrap bank is not even resource-compatible: two circuits share one owner
   and one q1 colour.
5. On the thirteen `D_4` circuits, exact anchor repair gives all thirteen
   `10` images at lengths `C18`--`C28`.  Primitive wrapping requires lengths
   through `C36`; twelve images are repaired through that bound, while one
   has no q2-safe simple anchor repair through `C36`.
6. Even an ideal whole-word recurrence using only `10D_s` and `1D_s0` sees
   only `2 Cat_s` of the `Cat_(s+1)` roots.  For `s>=2`,

   \[
      \operatorname{Cat}_{s+1}-2\operatorname{Cat}_s
       ={2(s-1)\over s+2}\operatorname{Cat}_s>0.       \tag{0.1}
   \]

   Hence these two unary images cannot themselves be a spanning suffix
   recurrence, independently of factor legality.

The exact escape is consequently narrower than “add a prefix correction”:

\[
 \boxed{\text{one needs non-conjugate reset circuits, fresh global resource
 selection, and a first-return-split topology recurrence.}}       \tag{0.2}
\]

## 1. Exact MSW context phases

Let `rho(X)` be the MSW flip-coordinate word, let `mu` be reverse complement,
and let `X` have semilength `s`.  Direct substitution in the first-return
recursion gives

\[
 \rho(10X)=(2,1,2+\rho(X)),                           \tag{1.1}
\]

and therefore

\[
 \mathsf I(10X)=(2,2+\mathsf I(X)),\qquad
 \mathsf D(10X)=(1,2+\mathsf D(X)).                  \tag{1.2}
\]

For primitive wrapping,

\[
 \rho(1X0)=
 (2s+2,,2s+2-\rho(\mu X),,1),                       \tag{1.3}
\]

so

\[
\begin{aligned}
 \mathsf I(1X0)&=(2s+2,,2s+2-\mathsf D(\mu X)),\\
 \mathsf D(1X0)&=(2s+2-\mathsf I(\mu X),,1).
                                                               \tag{1.4}
\end{aligned}
\]

Equation `(1.1)` exposes the two insertion phases.  At the root endpoint the
new pair is `10`.  After its first two flips it is `01`, and only then does
the embedded `X` path run.  Equation `(1.4)` shows the stronger wrap effect:
insertion and deletion phases are exchanged and the entire interior is
mirrored.  Right Dyck-tail concatenation had neither effect, which is why it
was a literal tensor operation while these two moves are not.

## 2. The connected-incidence phase lemma

Let a source alternating circuit use rank-`m` owners and rank-`m+1`
colours.  A context insertion injects the old coordinates into a ground set
with two new coordinates and raises both resource ranks by one.

### Lemma 2.1 (one phase on a connected circuit)

Fix the injection of old coordinates.  Suppose every circuit resource is
mapped by adjoining exactly one of the two new coordinates.  If every old
owner--colour containment remains a containment, then the same new
coordinate is adjoined to every resource of the circuit.

#### Proof

For an incident source pair `O subset Q`, write the two images as

\[
                 j(O)\cup\{a\},\qquad j(Q)\cup\{b\}.
\]

The new coordinates are outside `j([n])`.  If `a != b`, the first set is not
contained in the second.  Thus `a=b` on every incidence.  The incidence
graph of an alternating circuit is connected, so equality propagates to all
resources. \(\square\)

For `10`, the endpoint-correct phase is the coordinate carrying the `1` in
`10`; the other global phase lands on `01X`, not on a Dyck `T2` endpoint.
Literal H100 replay finds that the endpoint-correct phase preserves no
frozen circuit.  The `01` phase preserves exactly one frozen `C14`, but at
the wrong `01X` endpoints, and fails on the other sixteen circuits.

Lemma 2.1 alone fixes the new-coordinate phase.  The next section allows a
strictly stronger correction: arbitrary mixing of the old prefix coordinates
with both new frontier positions.

## 3. Exhaustive frontier-signature obstruction

Take one frozen circuit with `k` rows and list its `3k` displayed resources
in row order: owner, removed colour, inserted colour.  Give each old prefix
coordinate its complete membership signature in `{0,1}^{3k}`.  Add one
all-one signature for the fixed new up coordinate and one all-zero signature
for the unused new down coordinate.

An endpoint-correct context coordinate injection is now exactly a placement
of this fourteen-signature multiset on the fourteen target frontier
positions:

* seven signatures whose endpoint bit is one occupy the seven up positions
  of `P'10` or `P'1...0`;
* the other seven occupy the seven down positions;
* `P'` may be any of the six changed `T2` prefix owners;
* old suffix coordinates retain their literal context order.

Coordinates with the same complete signature act identically on every
circuit resource.  Quotienting their permutations therefore loses no
coordinate image.  Conversely every signature placement lifts to the
corresponding family of coordinate injections.  The finite enumeration is
thus exhaustive, not a sampling or canonical-form heuristic.

### Theorem 3.1 (no coordinate-conjugation transition)

For each of the four frozen `D_3` circuits, thirteen frozen `D_4` circuits,
both context moves, and all six target prefix phases, no endpoint-correct
frontier-signature placement preserves every old selected incidence and new
unselected incidence.

The exact census is

| source bank | phase pairs | distinct coordinate images | selection-valid |
|---|---:|---:|---:|
| `D_3` | `48` | `56,448` | `0` |
| `D_4` | `156` | `141,708` | `0` |
| total | `204` | `198,156` | `0` |

Because rejection occurs in the post-`T2` factor row, q2 support, component
action, residence, and common-history requirements cannot rescue any such
image. \(\square\)

This theorem covers arbitrary permutations of the old twelve-coordinate
prefix, phase changes among the six `T2` channels, and even moving an old
prefix coordinate into a new context position while the fixed new up
coordinate moves into the target prefix.  It is the complete Boolean
coordinate-injection meaning of a bounded prefix correction.

There is a stronger all-ground replay.  Instead of fixing the literal suffix
injection, give every old ground coordinate its complete resource-membership
signature and add the all-one/all-zero new-coordinate signatures.  Partition
these signatures by their ordered pair of memberships in the two named
endpoint owners.  Placing each signature multiset on the target coordinates
with the same endpoint-membership pair is necessary and sufficient for an
arbitrary coordinate injection to map both endpoints exactly.  Exhaustive
placement gives:

| source bank | phase pairs | all-ground images | selection-valid |
|---|---:|---:|---:|
| `D_3` | `48` | `1,034,208` | `0` |
| `D_4` | `156` | `44,334,000` | `0` |
| total | `204` | `45,368,208` | `0` |

Thus the no-go is not an artefact of keeping suffix coordinate names fixed:
no Boolean coordinate injection carrying the named endpoint pair to either
context edge preserves any frozen circuit.

## 4. Exact anchor repair and why it is not a recurrence

Write the transported circuit as a directed cyclic owner list

\[
 O_0\mathrel{\mathop\longrightarrow^{Q_0}}O_1
 \longrightarrow\cdots\longrightarrow O_0.           \tag{4.1}
\]

A raw arc fails when `(O_i,Q_i)` is not the required unselected incidence or
`(O_(i+1),Q_i)` is not selected.  Retain every `O_i` in cyclic order and
replace each failed arc by a directed exchange path with the same endpoints.
Breadth-first reverse distances give an additive lower bound.  The H100
search exhausts every path-length composition upward, imposes global
owner/colour simplicity, and evaluates the complete q2 current.

For the four `D_3` circuits the exact results are:

| source edge | raw | `10` repair | wrap repair |
|---|---:|---:|---:|
| `111000--101100` | `C16` | `C22` | `C28` |
| `111000--101010` | `C16` | `C22` | `C24` |
| `110100--110010` | `C18` | `C26` | `C24` |
| `110100--101100` | `C16` | `C20` | `C24` |

Every repaired circuit is individually q2-safe and merges all of its touched
post-`T2` lifted components into one.  Their component arities in the `10`
column are `11,11,13,10`; in the wrap column they are `14,11,11,12`.

Individually correct circuits do not compose into the inherited suffix tree:

* the four `10` repairs commute and lose no q2 support, but their simultaneous
  endpoint permutation has three orbits on the touched set;
* the wrap repairs for `111000--101010` and `110100--101100` share one owner
  and one q1 colour, so their toggles do not commute.

For the `D_4 -> D_5` anchor audit, the `10` repair histogram is

```text
C18:1,C20:3,C22:3,C24:1,C26:3,C28:2.
```

For wrapping, the twelve solutions through `C36` have histogram

```text
C24:3,C28:1,C30:2,C32:1,C34:3,C36:2,
```

and the image of `11100100--10101100` has no q2-safe simple
anchor-preserving solution through `C36` (its exact directed-distance lower
bound is already `C36`).

Compatibility and component action also deteriorate at this next level.
The thirteen `10` repairs have two owner-conflict resources and two
colour-conflict resources, producing two conflicting cycle pairs.  The
twelve available wrap repairs have the same resource-conflict counts, again
on two cycle pairs.  Moreover four individually q2-safe repairs split their
touched component support into two outputs:

```text
wrap  11101000--10101010   C34   shore lengths 23,483
10    11010010--11001010   C28   shore lengths 139,344
10    11001010--10101010   C18   shore lengths 183,185
wrap  11001010--10101010   C32   shore lengths 160,461.
```

These are exact finite anchor-class facts.  They do not prove that minimum
unrestricted circuits grow without bound.  They prove the claim actually
needed here: preserving the frozen resources plus bounded directed repairs
does not close the finite `C14`--`C24` atlas and does not preserve its
compatible component action.

## 5. Independent topology obstruction to the two unary images

The two whole-word maps have disjoint images

\[
             10\mathcal D_s,\qquad 1\mathcal D_s0,              \tag{5.1}
\]

each of size `Cat_s`.  Formula `(0.1)` shows that their union omits roots as
soon as `s>=2`.  The omitted words have a nontrivial first primitive factor
and a nonempty tail.  Therefore, even if both context transports were
perfect, copying one spanning tree into the two unary images would not span
`D_(s+1)`.

Right-tail tensoring supplies valid copies inside first-return blocks, but it
does not connect those blocks.  A genuine Catalan recurrence must be indexed
by the first-return split `1A0B` and include compatible bridge templates
between different `(A,B)` blocks.  The finite `D_3/D_4` label trees do not
provide that recurrence.

## 6. Exact scope and remaining gate

The obstruction does **not** say that the image suffix edges lack short
q2-safe circuits.  An exhaustive all-six-prefix `D_4 -> D_5` reset search
finds exact internal-owner minima on all 26 context-image edges:

```text
10:    C18:3,C20:8,C22:2
wrap:  C18:2,C20:3,C22:6,C24:2.
```

Thus local shortness survives perfectly after discarding the transported
anchors.  The first exact witnesses all occur in prefix channel
`101001010101`, however, and are grossly incompatible: the thirteen `10`
witnesses have `40` shared-owner resources, `35` shared-colour resources,
and `14` conflicting cycle pairs; the wrap witnesses have respectively
`43,37,35`.  This is a frozen-witness obstruction, not an UNSAT theorem over
all minimum candidates.  It identifies the reset problem as a global SDR
problem rather than a local-circuit-existence problem.

Nor does the theorem rule out a larger symbolic template set whose
transition deliberately discards the old resources.

It rules out three precise shortcuts:

1. literal context tensoring of the frozen circuits;
2. any Boolean coordinate-injection conjugation with a bounded prefix-phase
   correction;
3. anchor-preserving local repair as a compatible spanning-topology
   recurrence.

The sharp next theorem is therefore:

> **Split-aware reset-template theorem.**  For every first-return block in a
> recursive Catalan spanning tree, choose a fresh q2-safe alternating circuit
> from finitely many symbolic reset schemas, with a global owner/colour
> resource SDR and an actual one-orbit simultaneous component action.

Only after that factor theorem is proved can the residence-dilated,
turn-faithful common-history lift be attempted.

## 7. H100 certificates

All substantive execution and all hashes were run via `ssh h100`.

| object | SHA-256 |
|---|---|
| `scratch/audit_t2_suffix_context_raw_transport_20260814.py` | `6b94ff786897263aac5c9da22642b30b774e8919f4596c4a9dc850a415c06c20` |
| `scratch/audit_t2_suffix_context_raw_transport_phase_20260814.h100.out` | `b6e5e170217814c091327289266ccf29a29db1276a303ad5b0896bee9eb7908a` |
| `scratch/search_t2_suffix_context_frontier_signature_conjugations_20260814.py` | `b71ff2528e1edbd4b037d52f10614fdfdddcc2acedf4b8c1f124fd44228ed37e` |
| frontier outputs `D_3`,`D_4` | `cf3250c7ce33b06a5801912ff9088a6c7085d112345bd9ed7916d5edc06b38b4`, `00c18e7bd52391e95ae9bc0f97efc3c54337fcd495a4c43ced964c143b7f9710` |
| `scratch/search_t2_suffix_context_full_signature_conjugations_20260814.py` | `f90e74cf0cf1cbc94bb55c7974610efd87698c720a432b1d34ef5a2c55380ffb` |
| full outputs `D_3`,`D_4` | `dd983b4fd769a6691872d972e5aaa9f256f909555f4ad256bf16269c72b7c366`, `93ffeb6214ddd5524046425d40af09e48e3480a1b8200cb2cdf2fbd927e58074` |
| `scratch/combine_t2_suffix_context_full_signature_conjugations_20260814.py` | `02dbd3a216c8fd7d94d31597b860d3967ed9ae90d16a228fd2f7f42daf034195` |
| `scratch/search_t2_suffix_context_anchor_repairs_20260814.py` | `10378fbd8ef1cbe276db4c86efb56baec300d598b3bfb8355cfcf7efe9531b55` |
| anchor outputs `D_3`,`D_4` | `e9ef320222f2664dd39b01f1174233dbe0b26bcc531bd6a7f8c09301fb163e21`, `e0a0d1705f3140b4200dd8737d07a532b6036d1a3ae18ddf3c1fa952af5d2e1b` |
| `scratch/verify_t2_suffix_context_anchor_repair_bank_20260814.py` | `916ff83c31fd710c9e668abb9ff3617c0ac7cc5f3a726d8bf4092c33bce3e14e` |
| anchor verification outputs `D_3`,`D_4` | `6c99e8fd5f7d0032b1d5cf8e6dd9b9b20361f73df4ee397e28a150f7d34d1cca`, `3f45b951be3b632b85e92b7fc46b47b4bf87f2984ea422ec58d819691d099591` |
| `scratch/search_t2_suffix_context_image_minima_20260814.py` | `269c9a02b12ce6488a80f0b47b3a500bcda72000831cdaec8c6b68fa5e1b33c7` |
| fresh `D_5` minima output | `6dbe57b3e6ca6bd3a12dc898728191a0cc37ca869b4a4d47dc84857c34c2787c` |
| `scratch/verify_t2_suffix_context_image_minimum_bank_20260814.py` | `5686343e407e840a507e4b8047e67ad50eecf9129071af8f68090db8d5f9e1fc` |
| fresh-witness conflict output | `27a2179292f12e2681fcdaa41e244bac0fdab89b822d99e0e69c13999d65989a` |

The full `D_4` coordinate census was partitioned by frozen actuator/target
phase and recombined by the listed standard-library combiner.  Every part is
represented exactly once in the combined output.
