# Exact Hamming-two anchor and latent-palette completeness at round02

Date: 2026-08-02  
Lane: Thread D, `k=17` dense refinement  
Frozen face: two distinct-base, one-for-one substitutions of selected extra
cuts in the round02 7,612-piece bank.

This note proves completeness of a finite candidate generator for breaking
the original `114930` dual-fan certificate.  It does **not** say that any
generated child is q1-feasible, resident, connected, upper-complete, or
compiler-ready.

## 1. Frozen local certificate

The two forced socket owners are

\[
 s=115442,qquad t=115186,qquad s\cap t=114930.
 \tag{1.1}
\]

The direct seam is residence-illegal and both socket colour neighbourhoods
are the singleton `{114930}`.  Thus any q1-feasible child must destroy this
occurrence-labelled dual fan.

Let `M` be the complete set of `16,667` one-for-one recuts.  A pair is
compatible when its two recuts act on different base pieces.

Define the anchor set `A` to consist of:

* the 12 exact selected-colour socket escapes from the complete radius-one
  census; and
* all 9 alternatives in the two central bases `1834,1835`, including the
  seven locally failing `s`-side recuts and the locally failing colour/role
  move `1835:9933->9932`.

Hence `|A|=21` on 13 distinct bases.

## 2. Raw-atlas trichotomy

For a noncentral recut `g`, form the child `C_g` but ignore the selected
lower-colour filter.  Let `Raw(g)` be every seam incident with `s` or `t`
whose endpoint owners are Johnson adjacent and whose two path states pass
the exact relaxed residence predicate.  Write `colour(e)` for its rank-eight
intersection.

> **Theorem 2.1 (complete Hamming-two trichotomy).**
> Let `g,h` be compatible recuts.  If their final-net child destroys the
> original dual fan, then at least one of the following holds:
>
> 1. `g` or `h` is one of the nine central recuts;
> 2. a one-recut child already contains a selected legal noncore socket seam;
> 3. after interchanging `g,h` if necessary, there is an
>    `e in Raw(g)` such that `colour(e)` is absent in `C_g` and is selected
>    by `h` in `C_{gh}`.

### Proof

If a central base changes, case 1 holds.  Otherwise the two central path
states and their direct seam predicate are fixed.  The direct seam remains
illegal, so a certificate breaker contains a noncore arm at `s` or `t`.

Its outside endpoint is either unchanged or belongs to exactly one of the
two changed bases.  In the latter case call that recut `g`; then the arm is
already a member of `Raw(g)`.  In the former case assign it to either recut
which changes its colour status.  If its colour is selected in the assigned
one-child, case 2 holds.  Otherwise the other recut supplies that colour,
which is case 3.  These alternatives exhaust endpoint creation, residence,
and palette activation.  \(\square\)

The theorem is a final-net statement.  It permits a locally bad central
child to be repaired by the partner.  It also includes the joint-only
endpoint-plus-palette mechanism that is invisible in every
selected-colour single-recut atlas.

## 3. Exact unfiltered projection

The complete unfiltered audit rebuilds all `16,667` one-recut children and
constructs `Raw(g)` before selected-colour or zero-row pruning.  It gives:

| quantity | exact value |
|:---|---:|
| zero-265-clean recuts | 13,043 |
| clean selected-colour escapes | 12 |
| all selected-colour escapes, clean or dirty | 12 |
| dirty noncentral selected-colour escapes | **0** |
| recuts creating a new raw unselected seam | 67 |
| new raw unselected seam occurrences | 154 |

Thus no dirty noncentral escape was omitted by the 12 clean anchors.
However, the 67/154 line proves that latent endpoint creation is real and
cannot be dropped merely from the one-child counts.

The projection ran in `72.79 s` wall time with `37,424 KiB` maximum RSS.

## 4. Exact latent supplier join

For every unselected raw seam in every noncentral child, the second audit
joins its lower colour to the complete inverse index of recuts selecting
that colour, excludes same-base pairs, and removes pairs already containing
one of the 21 anchors.  Every remaining pair is then rebuilt at final net
state and checked against the complete zero-265 and socket ledgers.

The exact result is:

| quantity | exact value |
|:---|---:|
| summed raw seam rows over all children | 733,024 |
| summed unselected raw seam rows | 732,950 |
| nonanchor dirty selected escapes | 0 |
| nonanchor creator-supplier pairs | **0** |
| nonanchor joint zero-265 pairs | 0 |
| nonanchor joint socket escapes | 0 |

The large first two counts include the same baseline latent seams in many
children; they are not numbers of distinct new seams.  The decisive count
is the empty nonanchor join.  Equivalently, every one of the 154 newly raw
unselected occurrences either has no compatible selector recut or can only
be activated in a bank already containing an anchor.

The join ran in `9:53.85` wall time (`593.76 s` user) with `36,404 KiB`
maximum RSS.

## 5. Complete generator corollary

> **Corollary 5.1 (21-anchor completeness).**
> On the frozen round02 Hamming-two face, every child which destroys the
> original `114930` dual fan contains at least one of the 21 anchors.

This follows from Theorem 2.1, the absence of dirty selected escapes, and
the empty nonanchor latent join.

Therefore the smallest proof-complete generator is

```text
for anchor a in A:
    for recut g in M:
        if base(a) != base(g):
            emit unordered final bank {a,g}
deduplicate identical unordered banks
```

The exact combinatorial sizes are:

| generator count | exact value |
|:---|---:|
| compatible ordered `anchor x second` rows | 349,823 |
| distinct-base anchor-anchor double generations | 181 |
| unique two-recut banks | **349,642** |

For every emitted bank the implementation must apply both substitutions
before any acceptance test, then rebuild the complete path states, selected
lower bank, residence-tested seam atlas, zero-265 rows, and original socket
rank.  Prefix feasibility is not required.

## 6. Core-guided pruning after generation

The twelve single-anchor q1 children are all DRAT-UNSAT and have several
proof-dependent occurrence-labelled cores.  The independently decoded
owner-graph classes include:

* the one-colour fan `F_118996`;
* the recurring one-colour fan `F_115308` (also with one pendant
  `117348` seam in one proof);
* the two-colour bow tie `B_(35275,35786)`; and
* the two-colour bow tie `B_(31844,32352)`.

These give a sound pruning rule: if a final pair leaves any verified core's
orientation/seam resource clauses literally unchanged after owner-occurrence
reconstruction, the pair remains UNSAT.  The converse is false.  Cores are
proof-specific, so a candidate must not be rejected merely because it fails
to hit one preferred owner-graph representation; pruning requires an actual
unchanged verified core.

This is the correct role of the residual classification in the 349,642-bank
sweep.  It is a prioritization and exact unchanged-core certificate, not an
extra completeness assumption.

## 7. Reproducible artifacts

Sources:

* `scratch/audit_threadA_k17_round02_dualfan_hamming2_projection_20260802.cpp`;
* `scratch/audit_threadA_k17_round02_hamming2_anchor_completeness_20260802.cpp`;
* `scratch/audit_threadD_k17_round02_dualfan_socket_escape_20260801.cpp`;
* `scratch/run_threadD_k17_round02_hamming2_projection_h100_20260802.sh`;
* `scratch/run_threadD_k17_round02_hamming2_latent_join_h100_20260802.sh`.

Frozen outputs in
`scratch/threadD_k17_round02_hamming2_anchor_20260802/`:

| file | SHA-256 |
|:---|:---|
| `projection.tsv` | `bcaa7f353d00504edb954d448d7537f7f4d2c851d929be89df98e1c66be373f8` |
| `projection.audit.json` | `3bb51a527904b36e20e62e9020e11a9becbc0591c67ab678c5d728783d821955` |
| `projection.resource.txt` | `35790c4547c91a9d38b39c4ce2f548ac4725f239e6d1f61c65a43c0ec51daf45` |
| `latent_recuts.tsv` | `8b8769f4d333a0b3fcdf6fb292c1a9af715e390e1ad310070e3914071fb65f69` |
| `latent_pairs.tsv` | `9c80a03c0beabc704bd18ecd2d16a02f7511ff22bdd95ea4ebc0f04a300d447e` |
| `latent_join.audit.json` | `0ee2c01a938b58eec8cb9b26161fcf3defbaf92a8f0ab4211b6c0b97bb09e284` |
| `latent_join.resource.txt` | `79ddb3db1357554fbe6093a0f655e7bea0b1238718494308cb5856f51da9f488` |

The H100 execution root is
`/home/amodo/or15/work/threadD_k17_round02_hamming2_anchor_20260802`.

## 8. Complete anchored two-recut census

The proof-complete generator of Corollary 5.1 has now been evaluated in
full.  The adopted run applies both recuts before testing any row; it uses
no unary-cleanliness pruning.  Its exact counts are:

| quantity | exact value |
|:---|---:|
| complete recut catalogue | 16,667 |
| anchors | 21 |
| raw `anchor x second` jobs | 350,007 |
| incompatible same-base jobs | 184 |
| duplicate anchor--anchor jobs skipped | 181 |
| unique compatible two-recut banks evaluated | **349,642** |
| banks passing every local zero-265 row | **169,426** |

The twelve visible anchors and the sole clean central anchor
`1834:9924->9923` each have about 13,000 clean partners.  More sharply, the
seven individually dirty central alternatives
`1834:9924->9925,...,9931` each have exactly the same seven compensating
partners:

```text
recut 51     base 10    64    -> 63
recut 9674   base 2221  11898 -> 11897
recut 10130  base 2328  12461 -> 12462
recut 10131  base 2328  12461 -> 12463
recut 13210  base 3031  16253 -> 16248
recut 16309  base 3725  20042 -> 20040
recut 16310  base 3725  20042 -> 20041
```

Thus dirty-single compensation is real but extremely rigid on this face.
In contrast, the role/colour-removing central recut
`1835:9933->9932` has **zero** jointly clean partners in the complete
catalogue.

The adopted H100 run is frozen in
`scratch/threadD_k17_round02_anchored_two_recuts_20260802/`.  Its primary
outputs and independent structural audit are:

| file | SHA-256 |
|:---|:---|
| `audit.json` | `12ee6bff96d4ab42b0f4c92ef642aedd4b4849f7cdd0632f8b2466d6275ea4df` |
| `clean.tsv` | `9c4ecd1541a945bfae2be6d6534b28543a9c5c87745bdb8a47100dda274fb589` |
| `anchors.tsv` | `eedf932033280d3bef390e49929400ea5612097fbafbf0b6ca78db709b6834c9` |
| `independent.audit.json` | `f5d902547a07ed272de901125c77c5e436547966b197f2cc0afd2fefcd01dce7` |
| `preflight.sha256` | `52b2e2a99cbb3a1abb1576def8516f04892c52e1cd811e200241791fc4bb1f6a` |
| `runtime.note.json` | `0cfaedd60142d2fe54270baa30862e35db57cf49e98c883ecd399e6efb57cd3b` |

The independent checker reconstructs the catalogue, anchors, compatible
job set, deduplication and output ledger.  It verifies all 169,426 output
rows structurally; the C++ sweep remains the source of the local score
values.  The adopted run used 12 worker threads.  Its timestamp-inferred
wall time is `1004.06 s`, and a near-final snapshot saw `66,768 KiB` RSS;
neither is a guaranteed maximum because the adopted run was not wrapped in
`/usr/bin/time`.

A separate duplicate Thread D launch was terminated by signal 15 after the
adopted output was available.  It has status **UNKNOWN** and supports no
mathematical inference; none of its partial state is used here.

## 9. Scope boundary of the generator census

Corollary 5.1 closes the generator for original-dual-fan destruction only
on the fixed two-recut face.  The complete census additionally classifies
which generated banks pass the local zero-265 ledger.  At the time this
generator census was frozen, it had not solved the q1 formula on any of the
169,426 surviving banks.  The later audit in Section 10 supersedes that
chronological statement for exactly 49 dirty-central banks and nothing
else.  The generator theorem itself does not close the fixed-face
Hamming-two q1 problem.  Added-cut refinements,
alternative base cuts, C6/C8 rethreads, residence outside the local pair
predicate, topology, deeper shadows, and the terminal compiler also remain
outside the theorem.

## 10. Later exact closure of the dirty-central slice

The seven locally dirty central anchors

```text
1834:9924 -> 9925,...,9931
```

have exactly seven locally compensating partners each.  These produce 49
distinct joint-zero-265-clean banks.  A later canonical replay regenerates
all 49 complete bank/CNF/map triples byte for byte, obtains exact q1 UNSAT on
all 49, and independently verifies all 49 DRAT proofs.  Hence dirty-single
compensation is closed on this fixed Hamming-two face.

The remaining count is

\[
                         169426-49=169377.                \tag{10.1}
\]

Every remaining bank contains at least one individually clean anchor
(`0,...,12`).  This does not close any of those 169,377 banks and gives no
Hamming-three, circuit, deep-shadow, topology or compiler conclusion.

The proof-grade compact artifacts are

| file | SHA-256 |
|:---|:---|
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/proof_manifest.tsv` | `7959c9ce00d855cd187fe24e770e785f908dee5106cef8daf75480a75d55c0b6` |
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/theorem.audit.json` | `bf468abc0fd076613c81b21468f23e8e947e153eeff3d85e4bb52b15705e32f9` |
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/THEOREM_SCOPE.txt` | `bcda315af6bff664e7cb4a29df52479af4218e0008423a2a537bfa12316ca81d` |

The full remote `artifacts.sha256` has SHA-256
`52eba4e2c2869b5b04324062f3959f733e464338d6ce8de577aaaf5b25d89ca9`.
