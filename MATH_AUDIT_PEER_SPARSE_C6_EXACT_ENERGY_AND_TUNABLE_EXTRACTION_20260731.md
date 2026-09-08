# Peer audit of sparse C6 row energy and tunable extraction

Date: 2026-07-31  
Status: **GO** for the raw local C6 catalogue and the stated conditional
buffered extension.  No guarded packet, prescribed-task, cap, topology, or
`B(k)+O(1)` existence claim is made.

## 1. Audited verdict

The original large-family theorem and the independent exact-energy theorem
are both correct and complementary:

| extraction | retained anchors | average external conflict | raw Haxell |
|---|---:|---:|---:|
| large family, `p=m^-2` | `>=3I/(4m^2)` | `<=72m+216` | `m>=579` |
| endpoint-disjoint, `p=(16m^2)^-1` | `>=W/(32m)` | `<=16m` | `m>=128` |

Here

\[
 W={2m+1\choose m},\qquad I=W(m+1),\qquad L=m^2.
\]

The first keeps a much larger constant fraction of the Catalan-scale
anchor supply.  The second explicitly removes shared anchor endpoints and
has better conflict constants.  Neither chooses anchors prescribed by an
external repair bank.

There is a third, stronger raw existence consequence.  Tunable density
`p=Theta(1/m)` with a sufficiently small constant yields
`Theta(W)` pairwise-compatible raw C6 packets.  This does not contradict
the cubic full-atlas obstruction: average conflict falls linearly with `p`,
and high-degree packet choices are pruned inside each retained list.

## 2. Independent derivation of the exact row

For anchors `e,f`, let

\[
 K(e,f)={1\over L}\sum_r a_e(r)a_f(r),
\]

where `a_e(r)` is the multiplicity of typed token `r` in list `e`.  This
counts shared-token witnesses and therefore upper-bounds actual packet
conflict.

On either vertex shore, global token load, local total multiplicity, and
local square sum are

\[
 3(m+1)m^2,\qquad3m^2,\qquad m^4+m^3+m^2.
\]

The two shores contribute

\[
 2{3m^2\,3(m+1)m^2-(m^4+m^3+m^2)\over m^2}
 =18m^3+16m^2-2m-2.
\]

For incidence tokens the corresponding values are

\[
 6m^2,\qquad6m^2,\qquad m^4+2m^3+3m^2,
\]

and the contribution is `35m^2-2m-3`.  Hence, independently,

\[
 \boxed{R_m:=\sum_{f\ne e}K(e,f)
       =18m^3+51m^2-4m-5<44m^3\quad(m\ge2).}
\]

The companion literal enumerator obtains the same value at every anchor for
`m=2,3,4,5`.

## 3. Endpoint alteration constants

Each anchor has exactly `2m` endpoint-neighbours, so there are exactly `Im`
unordered endpoint-sharing pairs.  With

\[
                         p={1\over16m^2},
\]

the expected selected-anchor count, endpoint-pair count, and unordered
weighted energy are at most

\[
 pI,\qquad p^2Im,\qquad {p^2IR_m\over2}.
\]

Deleting one anchor per endpoint collision and then every vertex of
weighted degree above `16m` leaves in expectation at least

\[
 pI-p^2Im-{p^2IR_m\over16m}
 >pI\left(1-{1\over32}-{11\over64}\right)>{pI\over2}.
\]

Thus at least `W/(32m)` endpoint-disjoint anchors remain.  Per-list Markov
pruning at degree `32m` retains `L/2`; Haxell requires

\[
 {m^2\over2}\ge2(32m),
\]

whose first integer solution is exactly `m=128`.

The endpoint alteration is not a maximum-load theorem.  An endpoint-
disjoint owner-star may still have one token of total load `m^2`, while its
average contribution to one list is only `m-1`.

## 4. Tunable density

For any row-energy bound `R` and `0<p<=1`, Bernoulli sampling followed by
deletion above `4pR` leaves some family of size at least

\[
                         {3pI\over4}
\]

with per-list average at most `4pR`.  Prune packet vertices above degree
`8pR`.  Half of each list remains, so Haxell's sufficient condition is

\[
                         L_{min}\ge32pR.                         \tag{4.1}
\]

For the raw row, `L_min=m^2`, `R=R_m<44m^3`.  The safe universal choice

\[
                         p={1\over1408m}
\]

satisfies both `32pR<m^2` and `4pR<m^2` for every `m>=2`.  The latter
inequality automatically removes endpoint-sharing raw anchors, since their
mutual row contribution is `m^2`.  The compatible reservoir has size

\[
 {3pI\over4}
 = {3W(m+1)\over5632m}
 \ge {3W\over5632}.
\]

Using the sharp leading term `R_m~18m^3`, any fixed
`p=c/m` with `c<1/576` works asymptotically.

## 5. Buffered scope

Suppose, as an additional theorem, complete guarded lists have size at
least `alpha m^2` and complete-ticket row energy at most

\[
                         R_{full}\le K D_m m^3.                    \tag{5.1}
\]

Taking, in the asymptotically nontrivial branch,

\[
                         p={\alpha\over64K D_m m}
\]

gives `32pR_full<=alpha m^2/2` and extracts

\[
                         \Omega(W/D_m)
\]

compatible packets.  Thus even `D_m=Theta(m)` would give a Catalan-scale
dispersed reservoir.  This improves the fixed-density reading, which asked
for `D_m=o(m)`.

Equation (5.1) is not currently proved.  It must count protected
replacement rays, complete common-cap paths and sinks, and graphic/topology
tickets.  Raw C6 token loads do not control those resources.

The theorem also chooses a convenient anchor family.  It does not map a
specified Catalan leave or reachable task bank into that family.  A spread
task-to-anchor matching, or freedom to choose the defect bank after the
extraction, remains essential.  Ordinary Hall existence provides neither
the required pair marginals nor packet compatibility.

## 6. Frozen audits

The producer's direct token enumerator is

```text
scratch/audit_dispersed_catalan_average_conflict_20260731.py
```

and the independent constant/scope audit is

```text
scratch/peer_audit_sparse_c6_average_load_extraction_20260731.py
scratch/peer_sparse_c6_average_load_extraction_20260731.audit.json
```

Frozen hashes at this audit point are

```text
MATH_THEOREM_SPARSE_C6_AVERAGE_LOAD_EXTRACTION_20260731.md
  f82e1dfea59b96a3e95bd9ee829312a0ad5501f6263af956da06d8ce24329905
scratch/audit_dispersed_catalan_average_conflict_20260731.py
  10c098edcda056f11eb62a1beab0b303760bfbc3e979b056017908e786bf3055
scratch/dispersed_catalan_average_conflict_20260731.audit.json
  e5cc2876b5d532bcf22d7d122457e35af5e908f95ce858bb750372b040587792
  payload 03766531a0d246bdb5c141de35a81ae7ad6bbcd14dfea838dda5141dd1df0183
scratch/peer_audit_sparse_c6_average_load_extraction_20260731.py
  49b8042277dc2e991e22a8ea3074350d291ac607acfabef6ffb81cf2dd9f85ad
scratch/peer_sparse_c6_average_load_extraction_20260731.audit.json
  02e092fcc8b070942c844c5b87d7fa2a3d9c6397b020352204687914e8d3675b
  payload 6101fe42def292d2edf37e0a2bb79f644822a00b8bd85cd0be93697761697409
```
