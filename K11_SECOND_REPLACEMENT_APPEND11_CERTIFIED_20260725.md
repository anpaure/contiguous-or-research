# $K=11$: certified second-replacement plus eleven-entry closure

Date: 2026-07-25

## 1. Scope and conclusion

Let $P$ be the certified 465-entry partial word
`k11_upper549_natural_array.txt`.  The preceding one-replacement theorem
proved that, among all $465\cdot2047$ replacements of one entry of $P$,
only

```text
position 159: 288 -> 800
position 159: 288 -> 808
```

leave a missing-mask poset of width at most eleven.  Call the resulting
words $P_{800}$ and $P_{808}$.

This report closes the next rooted neighbourhood.

### Theorem

Start from either $P_{800}$ or $P_{808}$, replace one entry by an
arbitrary nonzero 11-bit mask, and then append eleven arbitrary nonzero
entries.  No resulting 476-entry word is universal.

The theorem includes no-op and first-edit-reverting replacements.  It is
not the full two-replacement theorem around $P$: two edits that jointly
reduce the missing-poset width can exist even when neither intermediate
one-edit word is one of $P_{800},P_{808}$.  Consequently the certified
global interval remains

\[
465\le \nu(11)\le477.
\]

## 2. Independent second-replacement enumeration

For each root, every one of the

\[
465\cdot2047=951{,}855
\]

second replacements was screened.  A completion by eleven new entries is
possible only if the missing-mask inclusion poset has width at most eleven,
because suffix ORs ending at one new endpoint form one chain.

The primary incremental-coverage implementation and an independent direct
interval implementation agree exactly.  For each root they find 1,610
width-feasible replacements.  The width distributions are

```text
root 800:
11:1610 12:12717 13:52594 14:292091 15:574217 16:18626

root 808:
11:1610 12:12725 13:52602 14:292114 15:574178 16:18626
```

The two 1,610-element replacement lists were sorted and compared byte for
byte after normalization.  An independent C++ reconstruction then encoded
each 465-entry word itself and found

```text
PASS first=1610 second=1610 listed=3220 unique=2290
```

Thus there are exactly 2,290 distinct prefix words requiring an exact
completion decision.

## 3. Exact completion and proof checking

For every distinct candidate, the audited last-occurrence recency encoder
`scratch/append_completion_recency_sat.py` generated the exact
eleven-entry completion CNF, including the full missing family and the
sound inclusion-poset endpoint cuts.  Its source hash is unchanged from
`APPEND_RECENCY_CIRCUIT_AUDIT.md`, whose independent audit proves the
recency recurrence, capped suffix-OR equivalence, and agreement with the
separate interval-selector encoding.

Kissat returned UNSAT for all 2,290 CNFs.  A DRAT proof was generated for
each individual CNF and checked immediately by the local `drat-trim`
binary.  A candidate was counted as closed only when the checker exited
zero and printed `s VERIFIED`.  Proofs were transient; the retained
manifest records the SHA-256 of every candidate word, its missing count,
and canonical provenance.  The batch output was

```text
listed=3220 unique=2290 solving=2290 jobs=8
progress unsat=2290/2290
UNSAT all_unique_candidates=2290 certified=1
manifest=scratch/k11_second_replace_append11_certified.tsv
```

The manifest contains one header and 2,290 candidate rows.

## 4. Reproduction

The principal commands are:

```text
c++ -O3 -std=c++20 scratch/k11_prefix_replace_append11_screen.cpp -o screen
./screen scratch/k11_prefix_replace_p159_x800.word \
  > scratch/k11_second_replace_from800_screen.out
./screen scratch/k11_prefix_replace_p159_x808.word \
  > scratch/k11_second_replace_from808_screen.out

c++ -O3 -std=c++20 scratch/audit_k11_prefix_replace_append11.cpp \
  -o screen_audit
./screen_audit scratch/k11_prefix_replace_p159_x800.word \
  > scratch/k11_second_replace_from800_independent.out
./screen_audit scratch/k11_prefix_replace_p159_x808.word \
  > scratch/k11_second_replace_from808_independent.out

c++ -O3 -std=c++20 scratch/audit_k11_second_replace_candidate_set.cpp \
  -o candidate_audit
./candidate_audit \
  scratch/k11_prefix_replace_p159_x800.word \
  scratch/k11_second_replace_from800_screen.out \
  scratch/k11_prefix_replace_p159_x808.word \
  scratch/k11_second_replace_from808_screen.out

python3 scratch/k11_second_replace_append11_sat.py --jobs 8 --certify
```

Current authoritative hashes are:

```text
da5773dca37fcf9f0851762d721e370bd40d77b59867412495e1ca3f951057a0  scratch/k11_prefix_replace_p159_x800.word
f8ed827b6e411ea72c2e4abb2600173b94c7526f0a080af7b45a00ae9975905c  scratch/k11_prefix_replace_p159_x808.word
1c3f94060091f9dc6d7d1197bb2d4a25f469a453b27adb96a69b0d9dc81a3792  scratch/k11_prefix_replace_append11_screen.cpp
1131e17e49a40c9ed10e2f3e253e943cf060d69c18b69f000e4c2842d1a93ba2  scratch/audit_k11_prefix_replace_append11.cpp
a1debe747842bb831ab579318e17c0674dfe04368b97e26473c1ea1a3f6f096f  scratch/audit_k11_second_replace_candidate_set.cpp
d93d842bd14d4fc9350f7d5f2610847270237a57bb96a2a885433083980c662a  scratch/k11_second_replace_append11_sat.py
4b32cbbf68490a969191a46bdbe737e3cec87437cd65bcfcd87957a5f11c65cd  scratch/k11_second_replace_append11_certified.tsv
441f2065e5e13c1c8f7fa68c0e4a9c8ec11e71a7aa24b14b3f7c0dea5ac82b80  scratch/append_completion_recency_sat.py
ebf53476748574a057367ff7c199002ce0d54e457a37044118d545495c641f54  scratch/drat_trim_local/drat-trim
```

## 5. Exact status

This is a strict enlargement of the previously certified rooted
construction exclusion: even after taking either of the only two
width-feasible first edits, no further arbitrary replacement can make an
eleven-entry completion possible.  It gives no global lower-bound increase
and no shorter upper construction.  The unrestricted $K=11$ problem is
still the physical synchronization problem described in
`CURRENT_EXACT_K_LT20_FRONTIER_20260725.md`.
