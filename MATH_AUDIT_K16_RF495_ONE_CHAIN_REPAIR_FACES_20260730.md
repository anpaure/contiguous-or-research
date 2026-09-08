# Exact one- and two-chain repair faces for the repeat-free RF495 collar

Date: 2026-07-30  
Status: the `left4`, `right5`, and `middle9+right5` proper faces are proved
`UNSAT`; the remaining proper faces are exact generated subinstances.  These
face theorems are not a global `K=16` decision and are not the unrestricted
RF495 decision.

## Geometry

The 18 editable cells in the frozen seed-5/self collar split into three
disjoint linear interval chains:

\[
  \{0,1,2,3\},\qquad \{4,\ldots,12\},\qquad \{13,\ldots,17\},
\]

of lengths `4`, `9`, and `5`.  The authenticated maximal-provider table has
exactly the 70 nonempty intervals of these chains:

\[
 \binom{4+1}{2}+\binom{9+1}{2}+\binom{5+1}{2}=10+45+15=70.
\]

Thus every residual physical witness uses editable cells from exactly one
chain.  The chains interact only because their covered-target sets must have
union equal to the 70-target residual family.

## Exact faces

Starting from the unrestricted exact-one formula

`scratch/k16_rf495_exactone_maximal_cnf_20260730/rf495_exactone_4900.cnf`

with SHA-256

`0d0adb8078b412ee4602382222bdbb907f2bf6274f5fc2715578fe07079038f8`,

pin every bit outside a chosen one- or two-chain union to the independently
replayed three-hole lead and leave the chosen chains unrestricted.  This adds
only unit clauses; all original provider, nonzero-cell, and exact-one clauses
remain byte-for-byte unchanged.

| free chain | SHA-256 |
|---|---|
| left 4 | `af30ad0ca992a7802e7545ca019b71957259a99dc532972a9e394d6c6c5ea2f5` |
| middle 9 | `8361246f241974be41a928d887ce1887e713e54e2af1ad06cd8ac2a1a25f8842` |
| right 5 | `b26c96aaabee69120fa072dd54a017e16f35557f90f1481357c01fd32d8d565d` |
| left 4 + middle 9 | `4cf8f91e6492a72650ebb9b6beed1c0edfb5bdc6d0cbba606ea86ee830bb73b1` |
| left 4 + right 5 | `dd7f6c8ed7a840c0b6ac79612f71f2377a2d56175b9943ce627b6ea1d8e59b52` |
| middle 9 + right 5 | `7d7434d21e30705544a59c6b999cca28b6415f896f50b10897d4e6adb000b9d7` |

Generator:
`scratch/build_k16_rf495_chain_repair_branches_20260730.py`, SHA-256
`0f951e2ad9365674698ac538fc3a387a120691516a1baeb9356fbe841f949ffe`.

Audit:
`scratch/k16_rf495_chain_repair_branches_20260730/chain_repair_faces.audit.json`,
SHA-256
`6fb5a74fe84a40d3d121af4aac53975fa73abd139511966900f99fd5f9c06092`,
payload
`50209758fc6dfdbf7cb16d6cfff336455eebeeba4174bee57c70e22e88699873`.

## Scope of a verdict

- `SAT` on any face is a model of the unrestricted base formula.  It must
  still be decoded into the 12,873-cell word and independently replayed over
  all 65,535 nonzero masks; after that replay it proves
  `nu(16)=12,873`.
- `UNSAT` on all three one-chain faces proves that no repair of the current
  lead can be confined to one collar chain.  At least two chains must change
  together.
- `UNSAT` on all six faces proves that every repair of the lead must move all
  three chains.  This is still strictly weaker than unrestricted RF495
  `UNSAT`, because the free chains are not required to remain near the lead.
- Even six `UNSAT` verdicts do **not** refute the unrestricted RF495 fibre,
  another seed pairing, another collar layout, or the global lower-bound
  equality conjecture.

This decomposition is useful because it distinguishes a local one-chain
wrinkle from the genuinely coupled multi-chain defect that the unrestricted
solver is deciding.

## Independent replay

An independently written parser checked all six headers, the untouched
175,462-clause base prefix, every appended unit literal, and its claimed lead
cell bit.  It reports `PASS`:

- checker SHA-256:
  `7cd0c1884e4f71242da1f7acb227816c2df87fd42084b841af444fa3ea3524e5`,
- audit SHA-256:
  `a9d0145ff3f84b306ea29d0d4b4c1413b99ba77387d3e2da5b22ae1a37dec2a3`,
- audit payload:
  `65aa0a0e000b43ea3cfed3ffb87ee32cb27a15e7b450a2a5cc23fe6a968c38b0`.

No target is locally dead on any face.  The exact fallback order by remaining
provider-domain mass is `left4`, `right5`, `left4+right5`, `middle9`,
`left4+middle9`, `middle9+right5`.  The faces are queued but deliberately not
launched while the unrestricted core-47 run is active.

## Left-chain face: solver-free closure

The `left4` face is now closed without SAT.  Let `R` be the 17 residual
targets not covered by the two frozen lead chains.  For a nonzero candidate
cell value `v`, define

\[
 \operatorname{cl}_R(v)=\bigcap\{T\in R:v\subseteq T\},
\]

using the full mask when the indexing family is empty.  If an interval
delivers `T`, every participating `v` is contained in `T`, and therefore

\[
             v\subseteq\operatorname{cl}_R(v)\subseteq T.
\]

Replacing every cell by its closure cannot destroy that delivery and never
creates a forbidden bit inside it.  Consequently closure normalization is
without loss.  The 65,535 nonzero values collapse to exactly 30 closures.
Exhaustive replay of all

\[
                         30^4=810,000
\]

normalized left words against all 38 raw `(Q,fixed-OR)` providers finds no
word covering the 17 mandatory targets.  A separately implemented replay
using the maximal-provider quotient agrees.

- census source SHA-256:
  `ba56824154ee2ecdf545673f7cc9849a33d6cdaea7ea6873e0b90f76eb622bca`,
- frozen result SHA-256:
  `1dc342e495ee08bac5e0497d671627b470da5b23e7c8275ae41aa37d48f91dcf`.

Thus the lead cannot be repaired by changing only its four-cell left chain.
The `left4` CNF need not be run.  This remains a face theorem: two-chain,
three-chain, and other-parent repairs are untouched.

## Right-chain face: exact closure meet-in-the-middle

The five-cell `right5` face is also closed without SAT.  Freezing the left
and middle chains leaves nineteen mandatory residual targets.  The same
closure-normalization lemma is without loss and collapses the nonzero cell
alphabet to seventy-three masks.

Write the right chain as

```text
(x0,x1) | (x2,x3,x4).
```

Internal left coverage depends only on `(x0|x1,x1)`, and internal right
coverage only on `(x2,x2|x3,x2|x3|x4)`.  For a fixed key, any coverage set
contained in another is dominated.  Crossing outputs are constant on a pair
of keys because the six crossing intervals are exactly a left suffix OR a
right prefix OR their fixed halo.

The exact census is

```text
left keys / antichain states:    2,270 /  2,531   (maximum 11)
right keys / antichain states:  41,865 / 59,267   (maximum 157)
key pairs:                      95,033,550
prefilter survivors:               214,561
tested antichain-state pairs:    4,616,608
completions:                             0
```

The optimized C++ decision took under one CPU second on the shared H100
host.  An independent NumPy implementation rebuilt all `73^2+73^3`
assignments before dominance, reproduced the retained-state and per-left-key
trace files byte for byte, and replayed all key/state pairs.  It reports
`PASS_UNSAT`.

Artifacts:

```text
scratch/decide_k16_rf495_right5_closure_mitm_20260730.cpp
scratch/audit_k16_rf495_right5_closure_mitm_20260730.py
scratch/k16_rf495_right5_closure_mitm_20260730/
  result.json
  states.tsv
  trace.tsv
  right5_mitm.independent.audit.json
```

Therefore neither outer one-chain face can repair the incumbent lead by
itself.  This still does not decide a two-chain face, the unrestricted RF495
fibre, another parent/layout, or `nu(16)`.

## Middle-plus-right face: endpoint-Hall contradiction

The strongest queued proper face closes without a SAT verdict.  Freeze the
four-cell left chain to the authenticated incumbent and allow all middle-nine
and right-five cell values to vary arbitrarily.  Exactly fifty-six targets
are then mandatory.  Seventeen of them have rank eight.

Independent replay of all 6,081 raw physical-provider rows shows that every
active provider of any of those seventeen targets has right endpoint in

```text
6434..6444  or  12868..12872,
```

only sixteen physical endpoints in total.  Intervals with the same right
endpoint are nested.  Their OR masks are therefore nested as sets, whereas
distinct rank-eight targets are incomparable.  Consequently at most one of
the seventeen mandatory rank-eight targets can be assigned to each endpoint.
This would require an injection of seventeen targets into sixteen endpoints,
which is impossible.

Thus the arbitrary `middle9+right5` face is `UNSAT`, with Hall deficiency one.
This proof does not assume maximal providers, exact-one ownership, a finite
cell alphabet, or proximity to the incumbent values.  It decides precisely
the left-four-frozen face and nothing broader.

Artifacts:

```text
scratch/audit_k16_rf495_middle9_right5_endpoint_hall_20260730.py
scratch/k16_rf495_middle9_right5_endpoint_hall_20260730/
  endpoint_hall.independent.audit.json
  rank8_endpoint_domains.tsv
  rank8_active_raw_providers.tsv
```

The audit reports `PASS_UNSAT`; its payload SHA-256 is
`7e1ea37f73720a033276dc284450792c7e25e6fa4201af8db8276964600fa5e8`.

## Superseded compact exact coupled-face reduction

For the strongest two-chain face in the queue—arbitrary `middle9+right5`
cells with `left4` frozen—the provider-selector base model can be replaced by
a much smaller exact CNF:

```text
224  physical cell bits
736  nonsingleton interval-OR bits
3360 target/Q provider selectors
----
4320 variables, 54,450 clauses.
```

Every nonsingleton interval bit is defined by the exact three-clause
recurrence `y <=> a OR b`.  A provider selector implies exactly the needed and
forbidden interval bits from the authenticated greatest `(target,Q)` row.
There is one coverage ALO for each of the fifty-six mandatory targets.  No
AMO is required: selecting multiple literal providers for one target does not
change the cell projection.

An independent implementation reconstructed the 4,900-row rectangle, the
fourteen targets already served by the frozen left chain, all sixty active
intervals, every variable, and all 54,450 clauses in exact order; it also
truth-tabled the OR recurrence.  Status is `PASS_FROZEN_NOT_SOLVED`.

```text
scratch/build_k16_rf495_middle9_right5_compact_cnf_20260730.py
scratch/audit_k16_rf495_middle9_right5_compact_cnf_20260730.py
scratch/k16_rf495_middle9_right5_compact_cnf_20260730/
  middle9_right5_compact.cnf
  middle9_right5_compact.map.json
  middle9_right5_compact.independent.audit.json
  MANIFEST.json
```

The compact formula was independently audited and then launched once on the
shared H100 host under a retained-proof contract.  After the endpoint-Hall
contradiction above was found, that run was deliberately terminated and
marked `SUPERSEDED_BY_ENDPOINT_HALL_THEOREM`.  Its partial proof is incomplete
and carries no SAT/UNSAT claim.  The exact formula remains useful only as an
independent encoding cross-check of the now-solved face.
