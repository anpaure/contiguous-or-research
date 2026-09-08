# K17 OPTIMAL28 port-circuit invariant and occurrence296+C6 defect vector

Date: 2026-07-31  
Status: solver-free fixed-skeleton theorem plus two independent literal replays;
source-relative only; no common-cap compiler or K17 word is claimed

## 0. Verdict

Residual pure-`U` incidence circuits and occurrence regeneration act on
different coordinates.

* On a fixed occurrence/macro skeleton, a residual port circuit cannot change
  a macro-interior residence packet and cannot create a provider for a target
  absent from the union of the entire residual provider atlas.
* Occurrence regeneration can change both invariant floors.  In the frozen
  `occurrence_greedy296` skeleton they fall from `724` to `296` internal
  residence packets and from `218` to `177` unsupported rank-ten targets.
* Starting from that regenerated skeleton, the authenticated `1160`-move C6
  fibre reaches the exact bounded-regeneration vector

  \[
       (c_{\rm cent},u,w_{q1:q3},V_*)=(0,776,2525,\bot),
  \]

  where `u` is the unpacketized missing row-bit host weight, `w` counts one
  unit per distinct missing literal target, and `V_*` is undefined (equivalently
  `+infinity` in the lexicographic gate) because upstream replay, residence,
  and upper service still fail.

The combined child strictly improves residence relative to both structural
parent branches, but it is **not** an all-coordinate contraction: its upper
weight `2525` is better than occurrence-only `2986` and worse than the current
pure-C6 comparator `2467`.

## 1. Fixed-skeleton port-circuit theorem

Fix:

1. every occurrence-selected macro word and all adjacencies internal to it;
2. the marked packet and its literal path;
3. the complementary component endpoint-demand multiset;
4. the residual `U` owner set; and
5. the complete allowed residual owner--port incidence atlas.

A **residual port circuit** changes only selected incidences in item 5, has
zero owner and port boundary, and retains every row in items 1--4.  The C6
move is the minimum example, but the conclusion does not depend on its
length.

### Theorem 1.1 (interior and provider-union invariance)

Under any sequence of residual port circuits:

1. every strict run wholly internal to one fixed macro word is unchanged;
2. the set of all providers available in the union of the fixed residual
   atlas is unchanged; and therefore
3. if a target has neither a fixed provider nor an incidence in that atlas,
   it remains unsupported under every residual assignment and every circuit
   sequence.

#### Proof

A residual port circuit replaces only edges between residual owners and
component ports.  It neither deletes nor inserts a vertex or adjacency inside
a fixed macro word, proving item 1.  It selects a different balanced subset of
one fixed incidence atlas; it does not enlarge the atlas, proving item 2.
Every realized residual provider is an atlas incidence, while every
nonresidual provider is fixed.  A target absent from both unions cannot be
realized, proving item 3.  The argument is independent of connectivity and of
the number or support of the circuits.  \(\square\)

For the original OPTIMAL28 skeleton the two exact floors are `724` internal
run packets and `218` rank-ten targets.  For `occurrence_greedy296` they are
`296` and `177`.  The latter pair is invariant only inside the regenerated
residual fibre.  Occurrence replacement, macro splitting, additive hex
columns, or a nonflat actuator may leave that fibre and are not excluded.

The theorem does not say that global residence is fixed.  Circuits can change
cross-component seams, and the child below lowers the full strict-D2 count
from `1875` to `503` while the component-interior floor remains `296`.

## 2. Authenticated combined checkpoint

The child uses the authenticated occurrence selection
`k17_opt28_occurrence_greedy296_verified_20260731.flow.json`, the corrected
connected residual base `connected_bflow_v2`, and the saved `1160`-move C6
ledger.

Two independent checkers reconstruct the occurrence macros from the K15
parent, replay all `1160` moves sequentially, and verify at every prefix:

* exact oriented-C6 incidence replacement;
* residual owner and port degree two;
* one `6435`-object cycle; and
* the unchanged literal marked path.

The final assignment has `4872` residual owners and `9744` distinct
owner--port incidences.  Materializing the fixed macros plus this assignment
gives one cycle on `24310` distinct rank-nine owners whose `24310` consecutive
rank-eight intersections are all distinct.  Hence central ownership and the
lower-`q1` palette are exact.

The two independent replays agree on:

```text
marked owners / D2 / D3              4108 / 0 / 0
complement owners / D2 / D3         20202 / 230 / 94
nonflat strict D2 / D3                         503 / 503
maximal-envelope empty / minimum size             0 / 6
replay mismatching rows / missing row bits       748 / 776
upper holes ranks 10..17          1585,824,116,0,0,0,0,0
lower cyclic q1..q9 holes          0,1441,770,147,2,0,0,0,0
```

## 3. Exact bounded-regeneration comparison

The central coordinate is the exact owner/palette matching deficiency.  The
residence coordinate `u` is the unpacketized count of missing `(row,bit)`
hosts; replay-row and strict-run counts are separately displayed diagnostics.
Upper literal weight is one per distinct rank-ten, eleven, or twelve target.

| state | central | `u` | replay rows | strict D2/D3 | upper q1/q2/q3 | upper unit weight | exact common-cap Hall `V_*` |
|---|---:|---:|---:|---:|---:|---:|---|
| fixed OPTIMAL28 | 0 | 3759 | 3568 | 2392/2392 | 1900/911/128 | 2939 | undefined |
| occurrence296 parent | 0 | 2901 | 2769 | 1875/1874 | 1908/929/149 | 2986 | undefined |
| pure-C6 `escape8` parent | 0 | 1651 | 1571 | 1029/1029 | 1576/775/116 | 2467 | undefined |
| occurrence296 + C6 child | 0 | **776** | **748** | **503/503** | 1585/824/116 | 2525 | undefined |

Thus, relative to both parent branches:

* `u`, replay rows, and both strict residence counts contract strictly;
* central defect remains exactly zero, so it is preserved but not strictly
  contracted;
* upper unit weight is not contracted against the pure-C6 parent (`+58`);
* common-cap Hall has no finite value to compare.

For completeness, the child upper `q`-depth weight is
`1585+2*824+3*116=3581`, and its rank-bit mass is
`10*1585+11*824+12*116=26306`.  These alternative weights have the same
noncontraction verdict against the pure-C6 parent.

## 4. Why common-cap is undefined

The exact compiler defect is

\[
 V_*(Z)=\min_Q\bigl(|\mathcal T|-\nu(H_Q)\bigr),
\]

where `Q` ranges over literal middle-realizing common guards.  It is defined
only after literal replay, residence, declared upper rows, sockets, and prepins
pass.  The child still has `776` missing row-bit hosts, `503` strict D2
packets, and `2525` upper `q1..q3` holes.  Therefore no legal `H_Q` instance
exists yet and `V_*` is `undefined` (or `+infinity` for logical ordering).

The scoped `177` zero-residual-provider targets are a valid marginal Hall
lower bound inside the occurrence296 fibre.  They are **not** the common-cap
Hall deficit and are not reported as such.

### 4.1 Exact common-cap precursor rows

Although Hall is not instantiated, every earlier Benders row is exact.  The
child has `a=4108` distinct rank-nine rows, `d8=20203` distinct direct
rank-eight rows, and minimum adjacent-row union rank nine.  Therefore every
lower target not among those `d8` direct rows must use a singleton or adjacent
pair cell.  With no auxiliary prepin charged, the ledger is

```text
physical word positions L                         24313
singleton + adjacent-pair cells       L+(L-1) =   48625
direct rank-eight rows                            20203
residual lower short targets          65535-d8 =  45332
lower-only scalar slack                           3293
upper no-long-provider targets q1..q3             2525
combined short targets                            47857
conditional scalar reserve                          768
```

Equivalently, the two-bank scalar cut is

\[
       a+|H^+|+s_{\rm aux}=4108+2525+0=6633
       \le 7401,
\]

with reserve `7401-6633=768`.  Thus the scalar precursor passes.  It does
not repair the earlier failures.  In fail-closed order the child has:

```text
central owner/lower-q1                         PASS
maximal-envelope nonemptiness                  PASS
literal D2 replay                              FAIL (748 rows, 776 bits)
strict D2 residence                            FAIL (503 packets)
long upper providers q1..q3                    FAIL (2525 targets)
q4 and deeper upper providers                  PASS
scalar combined short-cell cut                 PASS (reserve 768)
marginal target--cell Hall graph               NOT BUILT
rank-three common-cap Hall/clutter              NOT INSTANTIABLE
```

The conditional scalar overflow is zero, but the theorem-level `omega` and
`kappa` coordinates remain `+infinity` until hard host feasibility.  This
distinguishes a valid precursor capacity row from a compiler certificate.

## 5. Frozen provenance

Primary inputs:

```text
occurrence flow                         SHA 079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f
connected_bflow_v2                     SHA 63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0
C6 candidate                           SHA 960ca8df23e7c4ea28c6381e6642b4ec1ab86288a57329115d72182e56be949c
canonical final residual               SHA 6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4
canonical final residual payload           c92b72db852a8362a2f99c8091dec072ef42af831e1ef83af5381375d6d2a6e4
```

Independent H2 replay:

```text
scratch/h2_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py
  SHA 04e0148f4005f96c64df3f88d80628ffc8172e3c7fce67bf8f60e3c3fb1a1b29
scratch/h2_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
  SHA fc6716d285f774c246e22b7cbfd9a29f69391ace9f7d8089061d2fed57f38be7
  payload caef94767d76ef5fab84aa1bba454740c6fcca4e98914ac74ed0615d777a278d
```

Independent H4 replay:

```text
scratch/h4_independent_audit_k17_opt28_occ296_c6_localmin_20260731.py
  SHA 0be596135bffc24bafcbfb8363559670c67965976e27acf0f8901b4ee7371218
scratch/h4_k17_opt28_occ296_c6_localmin_independent_20260731.audit.json
  SHA 0bca08d71f42db8fc97ff599328fd725c32abb0de2c30396ce72bf70374d32a4
  payload 1466d61c961b3343151fa0e84fea2b6a9edce6d8b4bbf498ce751041eef1cc91
```

Common-cap precursor replay:

```text
scratch/h2_audit_k17_opt28_occ296_c6_commoncap_precursor_20260731.py
  SHA 9714fe95df38439f6585ea2053cf7069fa10069feb63715e9014a02279f846f4
scratch/h2_k17_opt28_occ296_c6_commoncap_precursor_20260731.audit.json
  SHA b0d1f6a8dbc92089d93cd8ec2a1b6031ff4b25c55194c4d3207e65108553865b
  payload 5b9e6c416d6b54a0c98abf3d2d7bf0a90e3a1d958ff6c4ece8c77c90c4904020
```

The H2 and H4 serializers differ, but their semantic owner cycle, envelopes,
run ledgers, and upper-hole sets agree exactly.  The H4 owner word is
byte-identical to the separately frozen materialization, SHA
`a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49`.

## 6. Scope

This proves an exact fixed-skeleton invariant and authenticates one
source-relative K17 checkpoint.  It does not prove that the remaining
residence or upper defects are jointly repairable, does not instantiate a
common-cap Hall problem, and makes no claim about a K17 universal word,
`nu(17)`, or an all-dimension recurrence.
