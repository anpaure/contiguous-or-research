# `k=17` round-02 escape children: physical dual-fan normal forms and the exact second-recut separator

Date: 2026-08-02  
Lane: R2, read-only core classification and theorem-first separator  
Status: exact for the named retained cores and for one further one-for-one
recut conditioned on a literal final rebuild.  No search, pricing, SAT run,
or remote write is part of this note.

This note classifies the promoted retained cores at

```text
/home/amodo/or15/work/root_k17_round02_dualfan_socket_escape_20260801/q1_tests
```

and gives a proof-safe scan for the next recut.  It does not assert that
breaking a retained core makes the complete q1 formula satisfiable.  It
does not prove selected rank-ten packing, topology, exact assembled
residence, deeper upper ranks, or a terminal compiler.

## 1. Extraction hygiene

Every promoted `escapeXX.core.orientations.tsv` begins with one spurious
triple obtained by parsing the DIMACS header as data.  Its first entry is
the number of core clauses and it has zero occurrences in the core body.
It must be discarded.  Forced physical roles below use only orientation
variables that actually occur in clauses.

Directed seam literals are quotiented by physical socket occurrences, not
by owner masks and not by mutable rebuilt piece numbers.  If the forward
orientation of a physical piece has endpoints `L(P),R(P)`, a directed seam

```text
P,orientation 0  -> Q,orientation 1
```

uses physical sockets `R(P),R(Q)`; its reversed directed occurrence uses
the same two physical sockets.  A singleton piece can have two distinct
socket occurrences with the same owner mask.  This distinction is
load-bearing in classes C and D below.

The odd extra literal in `escape05` also shows why a trimmed DRAT seam list
must not be treated as a complete reverse-paired atlas.  Classification may
use a sufficient retained subcore, but a breaker scan must reconstruct the
full literal atlas of the final bank.

## 2. Exact physical normal forms

After resolving the retained forced orientation rows, every promoted core
contains a two-required-socket, one-colour **dual fan**.  None of the twelve
promoted cores is a primal fan.

Write `Y={s,t}` for the two mandatory physical socket occurrences and `c`
for the primary lower colour.  In each row below there is no physical
`s--t` seam in the retained core, every retained seam meeting `Y` has
colour `c`, and both members of `Y` are forced.  Thus

\[
       |Y|=2,\qquad |\Gamma(Y)|+\nu(E[Y])=1+0<2.
       \tag{2.1}
\]

| class | children | primary colour | directed seams | forced physical shore | physical occurrence graph |
|:---:|:---|---:|---:|:---|:---|
| A | `e00` | `118996` | 6 | `R(1507)=127188`, `L(2078)=119028` | path `119508--127188--119004--119028` |
| B | `e06` | `14820` | 6 | `R(3505)=14821`, `R(3789)=14828` | path `15844--14821--15332--14828` |
| C | `e11` | `87145` | 36 | `L(1790)=87147`, `R(6616)=119913` | `K_{2,9}` on socket occurrences |
| D | `e01,e02,e03,e04,e07,e08,e09,e10` | `115308` | 28 | `L(3924)=115310`, `L(7179)=119404` | `K_{2,7}` on socket occurrences |
| D+pendant | `e05` | `115308` | `28+1` | same as D | same `K_{2,7}`; one off-shore `117348` pendant |

The first-child recuts are:

| child | base | old cut | new cut | class |
|---:|---:|---:|---:|:---:|
| `e00` | 540 | 2838 | 2842 | A |
| `e01` | 3680 | 19815 | 19818 | D |
| `e02` | 1284 | 6831 | 6832 | D |
| `e03` | 3613 | 19443 | 19445 | D |
| `e04` | 1379 | 7364 | 7380 | D |
| `e05` | 1801 | 9773 | 9771 | D+pendant |
| `e06` | 3254 | 17426 | 17428 | B |
| `e07` | 1532 | 8180 | 8181 | D |
| `e08` | 2251 | 12065 | 12067 | D |
| `e09` | 3029 | 16232 | 16234 | D |
| `e10` | 3344 | 17953 | 17957 | D |
| `e11` | 2251 | 12065 | 12066 | C |

The formal pair `e08,e11` is not a two-recut bank: the two moves are
alternative choices in the same base.  A second-recut scan either excludes
that pair or canonicalizes the overwrite as a single child.

### Lemma 2.1 (forced-shore decoding)

After the spurious header row is removed, the retained orientation clauses
force the same physical endpoint in both signs of the relevant piece:

```text
A: piece 1507 forces R(1507), piece 2078 forces L(2078)
B: piece 3505 forces R(3505), piece 3789 forces R(3789)
C: piece 1790 forces L(1790), piece 6616 forces R(6616)
D: piece 3924 forces L(3924), piece 7179 forces L(7179).
```

The corresponding retained seam implications contain only the primary
colour at those two sockets and contain no direct shore-to-shore physical
edge.  Hence each displayed row contains the dual-fan inequality (2.1).

#### Proof

For either orientation sign of the first named piece, its retained
incoming/outgoing clause requires one seam at the displayed physical
endpoint; the same holds for the second piece.  Reverse directed literals
pair to the occurrence graphs displayed above.  Inspection of their lower
columns gives the single primary colour, while their physical endpoint
pairs give no edge joining the two forced occurrences.  This is exactly
(2.1).  QED.

### 2.1 Occurrence-level leaf banks

Class A has core-colour arms

\[
  127188\!-!119508,\quad127188\!-!119004,
  \quad119028\!-!119004.                                  \tag{2.2}
\]

Class B has core-colour arms

\[
  14821\!-!15844,\quad14821\!-!15332,
  \quad14828\!-!15332.                                    \tag{2.3}
\]

For class C, both forced sockets meet the following nine physical leaf
occurrences:

\[
\begin{array}{c|c}
\text{physical socket}&\text{owner mask}\\ \hline
R(640)&87657\\
L(2714),R(2714)&95337,95337\\
L(2949)&89193\\
L(3950),R(3950)&87161,87161\\
L(3952),R(3952)&87273,87273\\
R(6124)&87149.
\end{array}                                                 \tag{2.4}
\]

The owner-mask quotient is only `K_{2,6}`; the exact resource graph is
`K_{2,9}`.

For class D, both forced sockets meet the following seven physical leaf
occurrences:

\[
\begin{array}{c|c}
\text{physical socket}&\text{owner mask}\\ \hline
R(704)&115436\\
L(3923),R(3923)&116332,116332\\
L(4066)&117356\\
R(6223)&115309\\
L(6972),R(6972)&123500,123500.
\end{array}                                                 \tag{2.5}
\]

The owner-mask quotient is only `K_{2,5}`; the exact resource graph is
`K_{2,7}`.  In `e05` the additional retained edge has colour `117348` and
physical endpoints

\[
                 L(4066)=117356,\qquad R(1262)=125540.      \tag{2.6}
\]

It misses both forced shore sockets in (2.5), so it does not break the
`115308` dual fan.  It remains a side guard in any replay of the full core.

## 3. Exact two-socket separator

Fix a child `C_i` and one allowed second recut `h` in a different base.
Build the final bank `D=C_i\oplus h` literally from the frozen round-02
assignment.  Reconstruct pieces, endpoint ages, the selected lower palette,
and all resource rows from `D`; do not add unary deltas.

After the same forced contraction used by the exact q1 formula, let
`A_D(s)` and `A_D(t)` be the available resident crossing arms at the two
forced socket occurrences.  An arm records its outside **physical socket
occurrence**, selected lower colour, upper mask, and every already consumed
resource.  Let `I_D(s,t)` be the available direct physical seams between
the two forced sockets.

Make a bipartite compatibility graph `B_D` with shores `A_D(s),A_D(t)`.
For an arm `e`, let `p(e)` be its outside physical piece, `sigma(e)` its
outside `L/R` occurrence, `d(e)` its incoming/outgoing slot at that piece,
and `o(e)` the path orientation it demands.  Join arms `e=su` and `f=tv`
exactly when their colours differ and

\[
 \gamma(e)\ne\gamma(f),\qquad
 p(e)\ne p(f)\quad\hbox{or}\quad
 \bigl(\sigma(e)\ne\sigma(f),\ d(e)\ne d(f),\ o(e)=o(f)\bigr),
                                                               \tag{3.1}
\]

and neither arm uses a socket, colour, or forced resource already consumed
by the contraction.

### Theorem 3.1 (necessary and sufficient retained-core breaker)

Suppose the literal rebuild leaves the same two physical occurrences as
mandatory residual sockets.  Then the residual two-socket row has rainbow
rank two if and only if

\[
       I_D(s,t)\ne\varnothing
       \quad\text{or}\quad E(B_D)\ne\varnothing.           \tag{3.2}
\]

If a forced role is genuinely relocated, the old retained certificate is
also inapplicable, but the new forced shore must be extracted and tested
before any q1 claim.

#### Proof

A local matching which covers both required sockets either uses one direct
`s--t` seam or two crossing arms.  Rainbow exactness forces distinct
colours.  Arms on different outside pieces have independent orientation and
functional resources.  If they meet the same outside piece, they must use
different endpoint occurrences and different incoming/outgoing slots under
one common path orientation; these conditions are also sufficient.  This is
exactly (3.1).  Conversely either a direct seam or one edge of `B_D` is an
explicit resource-disjoint local matching covering both required sockets.
A genuine role relocation removes a premise of the old certificate.  QED.

An isolated new off-core arm is therefore not enough.  It must have a
compatible opposite arm.  Conversely, it is unsafe to require that the
opposite arm be newly created: a surviving old core-colour arm may supply
it.  Classes A and B make the outside-occurrence check particularly
important because the two forced sockets share one leaf.

### Corollary 3.2 (exact prune)

If the roles persist, `I_D(s,t)` is empty, and `B_D` has no edge, the named
core remains a valid local obstruction.  The final full q1 formula is UNSAT
without a new SAT call.  The contrapositive is proof-safe because every
global q1 model restricts to a local matching covering the two forced
sockets.

Passing (3.2), or relocating a role, is only a promotion condition.  It is
not a q1 model and it need not eliminate another retained Hall core.

## 4. Four activation channels that the scan must retain

For each second recut, classify a promotion witness only after the final
literal rebuild.

1. **Direct shared seam.**  A selected, resident `s--t` physical seam of
   any available lower colour.
2. **Off-core arm.**  A seam meeting exactly one member of `Y` which forms
   a compatible pair in (3.1).  This includes a new non-primary-colour arm
   paired with a surviving primary-colour arm.
3. **Role relocation.**  The exact forced residual socket changes.  Merely
   touching or renumbering the old piece is not a role relocation.
4. **Multi-colour/cross activation.**  A raw arm may have legal endpoint
   geometry in `C_i` while its lower colour is unselected there; the second
   recut can select that colour.  Conversely the first recut can already
   supply the colour used by geometry created by the second.  Palette and
   geometry provenance must therefore be recorded separately.

For a raw seam `e`, the exact activation identity is

\[
  a_e(D)=G_e(D)\,
         {\bf1}\{\gamma(e)\in K(D)\}\,
         R_e(D),                                           \tag{4.1}
\]

where `G_e` is literal endpoint/Johnson geometry, `K(D)` is the final
selected lower palette, and `R_e` is residence plus residual-resource
availability.  Neither a raw geometric arm nor a supplied colour alone is
an active seam.

Removing the primary colour also does not count as a repair by itself.  It
deletes old arms and can leave a zero socket row.  Only Theorem 3.1 or a
genuine role relocation promotes the rebuilt bank.

## 5. Proof-safe one-hot selector and Benders row

Let `H_i` be the allowed second recuts for child `i`, after removing the
same-base overwrite.  For every `h in H_i`, the literal oracle returns

\[
 g_{ih}={\bf1}\{\text{all five scoped zero-265 ledgers pass}\},
 \qquad
 b_{ih}={\bf1}\{\text{role relocation or (3.2)}\}.          \tag{5.1}
\]

Here the five ledgers are lower colour, physical tail, physical head,
coherent orientation, and raw rank-ten-provider support.  They are
evaluated on the joint bank, not on either prefix.

With one-hot selector variables `z_h`, the exact retained-core master is

\[
 \sum_{h\in H_i}z_h=1,
 \qquad z_h\le g_{ih},
 \qquad \sum_{h\in H_i}b_{ih}z_h\ge1.                      \tag{5.2}
\]

Thus

\[
             B_i=\{h:g_{ih}=b_{ih}=1\}                    \tag{5.3}
\]

is the exact second-recut breaker bank for the named core.  `B_i` empty is
a scoped no-go for one further one-for-one recut from child `i`; it is not a
no-go for added cuts or circuits.

For a symbolic rather than precomputed atlas, introduce availability
variables `u_e` and pair variables `w_{ef}` for the compatible pairs in
(3.1):

\[
\begin{aligned}
 w_{ef}&\le u_e,&w_{ef}&\le u_f,&
 w_{ef}&\ge u_e+u_f-1,\\
 r+\sum_{e\in I(s,t)}u_e+
   \sum_{(e,f)\in E(B)}w_{ef}&\ge1.                       \tag{5.4}
\end{aligned}
\]

`r` is the exact role-relocation indicator.  Equation (5.4) is a complete
two-socket Benders separator.  An infeasible local incumbent has a finite
certificate: no direct edge is active and every cross pair conflicts in
outside occurrence, colour, or a consumed resource.

Because general coloured socket matching is not an ordinary flow problem,
one must not replace (5.4) by separate colour and endpoint projection
matchings.  On this two-demand row the explicit compatibility graph is the
smallest exact separator.

## 6. Required literal scan rows

A fail-closed second-recut table needs the following fields.  Counts without
the corresponding occurrence-labelled witnesses are not sufficient.

### Bank and final local ledger

```text
child, first_base, first_old, first_new,
second_base, second_old, second_new, final_bank_sha256,
zero_lower, zero_tail, zero_head, zero_coherent_orientation, zero_rank10
```

### Forced-role replay

```text
core_class, primary_colour,
old_socket_0_fingerprint, old_socket_1_fingerprint,
new_forced_socket_0_fingerprint, new_forced_socket_1_fingerprint,
role_relocation
```

A fingerprint contains the source base and side, `L/R` endpoint role,
owner mask, and the ordered owner sequence of the physical path.  Numeric
piece ids alone are rejected.

### Raw and selected seam rows

```text
socket_index, direction,
central_occurrence_fingerprint, outside_occurrence_fingerprint,
lower_colour, upper_mask,
geometry_legal, colour_selected, residence_legal, residual_resource_free,
geometry_source, colour_source, direct
```

`geometry_source` and `colour_source` distinguish incumbent, first-recut,
second-recut, and cross-activated support.  Every prospective unary seam is
retested in the final bank; it cannot rely on an intact counterpart block
which the other recut splits.

### Exact breaker witness

```text
local_rainbow_rank,
breaker_mode = NONE | DIRECT | TWO_ARM | ROLE,
direct_edge_witness,
arm_0_witness, arm_1_witness,
outside_occurrences_distinct, colours_distinct,
outside_pieces_distinct, outside_slots_distinct,
outside_orientation_compatible,
core_colour_still_selected, pendant_e05_status
```

For `DIRECT` the physical edge and colour are printed.  For `TWO_ARM`, both
full seam rows are printed.  For `ROLE`, the old and new forced-clause/path
fingerprints are printed.  A core-mask count, degree delta, or owner-mask
projection is not an admissible witness.

## 7. Frozen read-only core identities

### 7.1 Final physical-label replay

The final label audit used the literal state convention: orientation zero
has `first=L,last=R`, orientation one reverses them, and a directed seam
uses `tail.last` and `head.first`.  Canonicalizing each retained directed
row by its two physical `(piece,L/R)` occurrences gives:

| children | directed rows | physical edges | non-reverse-paired edges |
|:---|---:|---:|---:|
| `e00` | 6 | 3 | 0 |
| `e01,e02,e03,e04,e07,e08,e09,e10` | 28 each | 14 each | 0 |
| `e05` | 29 | 15 | 1, exactly the `117348` pendant |
| `e06` | 6 | 3 | 0 |
| `e11` | 36 | 18 | 0 |

All eight class-D children have byte-identical canonical physical
edge/colour/upper lists, with SHA-256

```text
412f5a23cf3cb1541acd03d268cd926d37d87e6a4ce62e4e3ad7ea9e54fd21b2
```

when the unique rows are sorted and serialized as
`socket_0 socket_1 lower upper`.  This independently confirms the `K_{2,7}`
class collapse.  The corresponding explicit edge lists confirm the L/R
labels in (2.2)--(2.6), the `K_{2,9}` size in class C, and the path sizes in
classes A and B.

### 7.2 Bundle and proof authentication

The canonical remote bundle contains 72 files matching
`escape*.core.*`.  With paths relative to `q1_tests`, its sorted digest is

```text
sha256sum escape*.core.* | LC_ALL=C sort | sha256sum
  b1ce92ae40bd3a1d526f1ec9a5a6258f80ae33c5960ab5c75ebe865a56716159
```

The corresponding CNF-plus-lemma and physical-map digests are

```text
escape*.core.cnf + escape*.core.lemmas
  1270b854567cb9e74453412a189ebb92022142de730699c12c4f97d515d83a53
escape*.core.lower_masks + orientations.tsv + seams.tsv
  f64e3ab36476195e5a6685bfc985cc98893a1468a47bb3e9540bd6b69704dedd
```

An independent read-only `drat-trim` replay against the exact retained
`core.cnf/core.lemmas` pairs accepted all 12.  The tuples below are
`child : clauses retained by backward checking / core lemmas / resolution
steps`:

```text
e00 22/22/49     e01 143/38/1607   e02 143/38/1607
e03 143/38/1607 e04 143/38/1607   e05 142/41/1680
e06 26/26/66    e07 165/44/1650   e08 156/41/1765
e09 143/38/1607 e10 143/38/1607   e11 179/32/1825
```

The checker binary had SHA-256
`92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a`.
Every real core clause was also checked as an unordered-literal subset of
its full q1 CNF, and every non-header orientation/seam map row as an exact
subset of the full maps.  The compact independent classification ledger is

```text
scratch/r2_k17_round02_root_12_escape_core_classification_20260802.tsv
  SHA-256 917c98a35e7b0b7a9523764eb10138926566765cef0fa85447a02ecc9990370a
```

### 7.3 Core formula identities

The promoted core CNF SHA-256 values observed read-only are:

| child | core CNF SHA-256 |
|:---:|:---|
| `e00` | `3ac26da7e6c011cb0a79afca71ad2876bf739bd69fa438f770f2e0b20529c493` |
| `e01` | `f8f6709d20ab158fd72135cf3d72f0faad1947cb61dca1f4350f5c14891b5325` |
| `e02` | `0d22eb5d186bb33ee819584ebfaa495d3d017011adc97e41ffaea9306e288037` |
| `e03` | `b41f5e3e84070fed4a08b20a995eb137558f88e7f679e5e7ea238766889989a9` |
| `e04` | `9ae6b04ff811230a91ceb362467cab26db30982f223248ae248ba52e38d35891` |
| `e05` | `b3e13736fa6e6fc36f0d43b2f3aa2192299093750e4a8203514f7d224556dc2c` |
| `e06` | `06c9649675b08936484aef1eb844ca0396eec0c712e3f743bb9288cc2bd14225` |
| `e07` | `3a84fdb2e08ea677174db885537e1466f01b90705da7ef9fd8f3bf9f0e2fb6f3` |
| `e08` | `4b69bb1c7cf6c263f0969e5172f40df4e8c5ee335ff21e44d70a6d4c30559883` |
| `e09` | `0dd94be3df57b64b795763a1cba48353d9182085c99cebb892ffb67d02905e3c` |
| `e10` | `f004f566727699bb0fac65ba8dbd44d0b6292e3c223c3bc337026704e0e44a0e` |
| `e11` | `469aebc98c42ee799813cc95c6e5d220d9e5d2000f19ee6c0b5b4b0faf9cb466` |

This note classifies those authenticated formulas physically; it does not
replace their DRAT manifests.  In particular, the older Thread-D core
classification for children `e06,e07,e08,e11` must not be substituted for
this later promoted bundle.

## 8. Sharp scope

Proved here:

* the twelve promoted cores have the four primary dual-fan normal forms
  A--D, with the stated occurrence-level shores and leaf banks;
* the `e05` second colour is an off-shore pendant, not a primal-fan repair;
* Theorem 3.1 is necessary and sufficient for breaking each named residual
  two-socket row while its roles persist; and
* (5.2) is an exact Benders selector for one further one-for-one recut once
  its constants are obtained by literal final rebuild.

Not proved here:

* that any second-recut breaker exists;
* that a breaker extends to a complete q1 rainbow matching;
* a no-go for dirty-prefix pairs, added cuts, C6/C8 circuits, or larger
  final-net moves; or
* topology, selected rank-ten packing, exact assembled residence, deeper
  upper rows, exterior windows, or compiler feasibility.
