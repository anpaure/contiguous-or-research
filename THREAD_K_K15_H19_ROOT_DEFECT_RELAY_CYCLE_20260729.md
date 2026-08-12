# Thread K: exact H19 root-defect relay, inverse cycle, and commuting split

Date: 2026-07-29  
Status: theorem-level exact audit; no Hall-18 carrier is claimed

## 1. Scope

This note audits the selected continuation of the H19 profile route.  It
contains no search performed on the local machine.  The direct-description
enumerations and the 695-state neutral census were run on the H100 CPU; the
local audit is a search-free recomputation on five frozen carriers.

Write

\[
 A=\operatorname{FR}(3814,4556,5539),\qquad
 B=\operatorname{RF}(688,2636,2650),\qquad
 C=\operatorname{RF}(3176,4522,5948).
\]

The starting state in this note is `c0440=A(X19)`.  Its critical DM shore is
`380/361` and includes the component rooted at 9104 of type `25/24`.

## 2. Exact defect-relay theorem

**Theorem 2.1 (disjoint root-defect relay).**  The braid

\[
   c0440\xrightarrow{C}c0668                                      \tag{2.1}
\]

is deck-exact, Johnson, resident, upper-complete through depth seven, and has
Hall deficiency 19 and zero count six.  On positive DM components it replaces
exactly

\[
       (r,L,R)=(9104,25,24)\quad\hbox{by}\quad(952,6,5),           \tag{2.2}
\]

and this is the only replacement of a target shore/root.  The two target
shores are disjoint.  Every shared component retains its root, type, target
shore, and native-trace multiset, but the physical right-cell sets are not all
fixed: roots 1103, 2420, 2575, 2676, 4213, 7504, 8216, 9524, 17683, 18970,
and 19568 are re-addressed.  Consequently the total critical shore changes
from `380/361` to `361/342`, but its total defect remains 19.

On the fixed old 25-target shore, the matching rank changes `24 -> 25`; on
the fixed new six-target shore, it changes `6 -> 5`.  Thus (2.1) closes the
old defect and opens a new one.  It is a genuine defect relocation and not a
same-shore refinement.

The lower-hole vectors are

\[
 (4,18,13,1,0,0,0)\quad\longrightarrow\quad
 (4,19,13,1,0,0,0),                                               \tag{2.3}
\]

and every upper hole count remains zero.

**Proof.**  Literal block materialization gives (2.1).  The exact compiler
graphs have maximum matching 16364.  Their target-component differences have
old root set `{9104}`, new root set `{952}`, types (2.2), and empty
target-shore intersection.  The auditor separately compares target shores,
native traces, and physical right cells on every shared root.  Induced
matching recomputation on each fixed shore gives the two rank transitions
above.  The all-depth ledgers give (2.3).  These facts are asserted and
independently recomputed by the frozen auditor in Section 6.
\(\square\)

## 3. Exact inverse and complete one-step canonical target-shore obstruction

Define

\[
 C^{-}=\operatorname{FR}(3176,4603,5948).
\]

Here *neutral* means emitted Hall-19/zero-six carriers with lower-q1 hole count
four.  The c0668 emission contains 7130 raw move descriptions and 695 distinct
middle paths after deduplication.

**Theorem 3.1 (unique one-step canonical closure is the inverse).**  Among all
695 deduplicated neutral, resident, upper-complete one-braid successors of c0668,
exactly one saturates the fixed root-952 shore, and exactly one changes the
canonical target component containing that shore, allowing both root-changing
and same-root target-shore migrations.  They are the same carrier, `c0450`,
obtained by `C^-`.  Its middle path is entrywise equal to the c0440 middle
path.  Pure physical right-cell readdressings with the same target shore are
not called target-component changes here.

More explicitly, the root-952 target shore is

\[
             \{952,956,1976,5048,9144,17336\}.                    \tag{3.1}
\]

The unique canonical migration removes this `6/5` target component and
recreates the disjoint root-9104 `25/24` target component.  Thus `C` and
`C^-` give the certified inverse two-cycle

\[
             9104:25/24\ \xrightleftharpoons[C^-]{C}\ 952:6/5.   \tag{3.2}
\]

**Proof.**  The source census has status PASS, 695 entries, 695 passing
entries, and manifest SHA-256

```text
356796f72a3a1b492bbff79a75fca4e6be1824d2eac895716e18d1ec10f6e8b4
```

Filtering all entries by fixed-shore saturation at root 952 returns only
manifest index 450.  Filtering every canonical target-shore migration group
whose old-root list contains 952, including same-root target-shore changes,
also returns only index 450.  Its move and state hash are

```text
FR(3176,4603,5948)
648ad9d3112908dbfff22ba9a95c81b7db3591154bc9594a09874a4e0030f608
```

Literal materialization followed by entrywise comparison of the middle path
with c0440 gives equality.  The compact exhaustive certificate is frozen in
Section 6.  \(\square\)

The theorem is deliberately one-step, one-sided, and target-shore-specific.
It proves uniqueness of the closure from c0668 in this census, not uniqueness
of outgoing root-9104 relays from c0440 and not uniqueness under pure physical
right-cell readdressings.  It does not rule out a longer route that first
changes unrelated components and only later returns to this shore.

## 4. Physical readiness obstruction over the whole neutral beam

**Theorem 4.1 (no native duplicate opening).**  Every one of the 695 neutral
c0668 successors has Hall deficiency 19 and zero count six.  Every final DM
component admits a native basis.  Nevertheless, across the whole beam:

- no final-component native child target has a surplus occurrence;
- no exact all-reserve-preserving single-root rebase exists in the canonical
  native mechanism;
- no exact all-reserve-preserving full rebase exists within one component in
  that mechanism;
- no gap-two root-8216 component is partially or fully discharged.

The root-8216 `321/319` component survives in 669 states; none of those states
has a one-root or two-root readiness witness.  The physical-census SHA-256 is

```text
bee279b28f3aa7ca88758025ce2998f59c781e2cad6f7bcdd91b6cabf325794c
```

and the compact physical ranking has SHA-256

```text
f292bf648c32a6e70ecd8ce0600005196e99611c94cb830a5d87a978edfa1878
```

This is stronger than a Hall-profile statement: it reserves one native pin
on every final positive-DM right cell and checks all central windows after a
prospective shrink.  Its exact scope is one component at a time using native
child occurrences.  It does not assert simultaneous ears across distinct
components, does not reserve a full 16364-pin global compiler, and is not an
impossibility theorem for nonnative pin assignments.

## 5. Commuting compression-plus-split and q1-cap-four direct scan

The support of `B` ends at 2650 and the support of `C` begins at 3176.  Direct
materialization therefore gives the literal commuting square

\[
 B(C(c0440))=C(B(c0440))=c0526.                                  \tag{5.1}
\]

At c0526 the DM shore is `330/311`.  The root-952 target shore, type `6/5`, and
native-trace multiset are unchanged, although its physical right-cell set is
re-addressed.  The root-8216 `321/319` target component is replaced by

\[
                8217:129/128,
                \qquad 8218:161/160.                             \tag{5.2}
\]

This is a compression-plus-split rather than a partition: old left mass 321
becomes new left mass 290, with 36 old-only and five new-only targets.  Move
`B` preserves the support set of every lower and upper shadow ledger at depths
one through seven, but not all multiplicities (the depth-six and depth-seven
counters change).  All 19 final components have a native basis, but there are
again zero duplicate native children and zero exact componentwise single or
full rebases under the canonical native reserve.

The direct scanner computes Hall only after imposing lower-q1 holes at most
four.  Therefore the exact conclusion is: among all Hall-evaluated move
descriptions satisfying this cap, no Hall-18 child exists.  Upper-safe
descriptions failing the cap are counted but not Hall-evaluated, and the counts
below are move descriptions rather than deduplicated states.

| parent | Johnson | resident | upper-safe | Hall-evaluated | best Hall | `.out` SHA-256 | `.err` SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| c0668 | 549092 | 12000 | 9229 | 7316 | 19 | `f50c5718c702df3525043f4ced4513c745d73649fc0db668caa3c6b858c9fd67` | `4dcd5994334af45098d9a9c6bc99915bb4fdfb30a7bfcfe0053734d64d942e3e` |
| c0526 | 549079 | 12001 | 9230 | 7317 | 19 | `b850ad2d555e24f8438f2ed4cf3b997d75a94d58c0fe4e9c3c96f8eaef54c4da` | `1d34d6fd1cb77f05fbd493f998ef23327785ddeff1696852ed015e7028179f43` |
| c0450=c0440 | 549329 | 12021 | 9202 | 7301 | 19 | `4ed7e47eedb13cd56c1e1f562df7bc0808f89d7e79685bbaf5d38b24dfd09f0d` | `b24f60b64fe9963aac60edf10830f53ab5304764de52b42d1913131f084b17dd` |

For comparison, the same-root extension

\[
 c0440\xrightarrow{\operatorname{FR}(3100,4117,4961)}c0434
\]

enlarges root 9104 from `25/24` to `27/26` and saturates the original fixed
25-target shore.  Its direct scan has 547383 Johnson, 11935 resident, 9177
upper-safe, and 7302 Hall-evaluated descriptions; their best Hall is 19.  The
output and diagnostic SHA-256 values are

```text
3f8ef8084d65873a1dd3c839be3f14f2c7dd014cbcc60077f2f72078d30eea53
eae11d12020379c98db55d7d36a95dbe77718620c54d56258fe3ddbdfc669a8a
```

Thus neither same-root extension, disjoint defect relay, nor the
disjoint-support commuting split exposes Hall 18 in the Hall-evaluated,
lower-q1-cap-four portions of the audited direct neighbourhoods.

## 6. Frozen artifacts

The search-free auditor is

```text
scratch/audit_k15_h19_root_defect_relay_cycle.py
a0385a8461582cd8ca6372f8990ca2311b237cd9b6ec9bbe958ff9d42f493f8c
```

and its PASS output is

```text
scratch/k15_h19_relay_20260729/audit_k15_h19_root_defect_relay_cycle.json
bfe6a627def60876512ccf9b018f96fb13af7147b94bb7cbe0d2b4a24c494deb
```

The exhaustive root-952 filter is

```text
scratch/k15_h19_relay_20260729/root952_neutral_uniqueness_certificate.json
3d9882c54ba9eeaac111b59dc8c7e524586a7dc4e982f05f68c46f7f5ab9862a
```

The principal frozen carrier hashes are

```text
c0668  2c024151a93eb5f2e36cd113b90d38b89685a14026d66b03788c5a683f83913f
c0450  648ad9d3112908dbfff22ba9a95c81b7db3591154bc9594a09874a4e0030f608
c0526  2a266531b92aeed3cf662d556699ff102f83b331e53655923af42c25373e1d7c
c0434  8e894909a2c83cdc5449bcf03d092c841cffb82e026ab8ef3568cc03b5bc2012
```

The complete c0668 profile-census SHA-256, retained on H100, is

```text
a2ba2b057be9598265d1152219723dbbdaf13d450689d90a2f8715185a018af2
```

All locally frozen relay artifacts are covered by
`scratch/k15_h19_relay_20260729/CANONICAL_SHA256SUMS_20260729.txt`; a fresh
`shasum -a 256 -c` check passes every entry.

## 7. Sharp boundary

The proved obstruction is architectural, not global:

1. the audited braid `C` moves a unit DM defect from target mass 25 to mass 6,
   but does not remove it;
2. the complete neutral one-step beam has no alternative canonical
   target-shore migration of root 952;
3. its unique canonical closure from c0668 is the literal inverse;
4. every neutral successor lacks the duplicate native occurrence needed by
   the audited common-`Q` shrink mechanism;
5. after the disjoint-support root-8216 split, c0526 still has Hall 19, the
   same abstract root-952 target shore, zero canonical-native readiness, and no
   Hall 18 among lower-q1-cap-four Hall-evaluated descriptions.  No 695-state
   uniqueness or inverse theorem is asserted for the c0526 beam.

The next viable move must therefore do at least one thing absent from this
native, one-component library: create a surplus native child occurrence,
provide a certified nonnative common-`Q` reassignment, coordinate ears across
components, temporarily leave the protected lower-q1-hole cap four, or use a
longer coupled braid whose intermediate state changes the root-952 occurrence
geometry before attempting the split.  The present audit does not exclude such
a higher-order route and does not claim Hall 18 is impossible.
