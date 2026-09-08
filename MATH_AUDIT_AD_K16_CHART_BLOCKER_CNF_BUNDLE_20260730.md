# K16 chart/blocker CNF bundle audit

Date: 2026-07-30  
Lane: AD  
Status: exact emit/decode bundle generated for all three fixed-gap profiles;
no SAT or UNSAT solver verdict

## 1. Proved semantics

The mathematical source is

~~~text
MATH_THEOREM_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 2f52bc0bbcbc61d7ac0d22113bceb951d46610c0c526c0482160da6785f5a156
~~~

Its chart-intersection theorem says that selected target intervals are
realizable exactly when every used cell has a nonempty active-target
intersection and every target bit missing from the maximal fixed context
has a durable point. The canonical decoded cell is the intersection of all
selected targets whose intervals contain that cell.

The independent audit of the mathematical core is

~~~text
MATH_AUDIT_AD_K16_CHART_INTERSECTION_ELIMINATION_AND_ANCHOR_PRUNING_20260730.md
SHA-256 52ad1912058c0086b9e4a7cfbd6a1203d31939fe372d02fc56587c152c02ee66
~~~

That audit identified two wording qualifications, both incorporated in the
current theorem: maximal contexts are contexts compatible with an exact
target witness, and an ALO-only model unions every true chart occurrence,
not one chart per target. It also requires a decoder to reconstruct active
target intersections rather than treating blocker bits as cell bits.

## 2. Emitter and decoder

~~~text
scratch/build_ad_k16_12873_chart_blocker_cnf_20260730.py
SHA-256 2a3d233c802a255ee97e13d0bf3a3b6e1277b07d28a409c867a1256ed148b7e8

scratch/decode_verify_ad_k16_12873_chart_blocker_cnf_20260730.py
SHA-256 44db9ea1c9345f45fc71d80455e666433fe58361bbd2f3ff40d41bda97240853
~~~

The emitter pins:

* the authenticated length-12,874 answer;
* the theorem note above;
* the solver-free three-profile core source, SHA
  29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2;
* its audit JSON, SHA
  2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892;
  and
* its replayed payload, SHA
  d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47.

The payload replay restores the one integer-keyed Counter serialized by JSON
as string keys. This is the same serialization-type normalization already
needed in earlier audit artifacts; the byte hash remains independently
pinned.

For every target/local interval selector \(x_{T,I}\), every cell
\(p\in I\), and every coordinate \(q\notin T\), the emitter adds

\[
                         \neg x_{T,I}\vee B_{p,q}.
\]

For every \(q\in T\setminus b_T(I)\), it adds

\[
                 \neg x_{T,I}\vee\bigvee_{p\in I}\neg B_{p,q}.
\]

It adds one target ALO row and one common-coordinate row
\(\bigvee_q\neg B_{p,q}\) per cell. No selector AMO and no closure-domain
clauses are needed. Blockers may overstate obstruction but cannot understate
it; extra blocker truth only tightens the formula.

The decoder is fail-closed. It requires a complete SAT assignment, checks
every DIMACS clause, recomputes intersections from every true chart,
verifies every selected maximal-context equation, materializes all 17
nonzero masks, and replays all 65,535 targets literally. Solver blocker bits
are never decoded as word values.

## 3. Forced-anchor completeness

The repair target 0x8000 has maximal context zero in every collar. Any one
of its witnesses consists entirely of cells equal to 0x8000, and therefore
contains a singleton witness. The emitter supports:

* no anchor clause;
* one WLOG ALO over all 17 singleton anchor selectors; or
* a unit clause fixing the singleton anchor to one editable absolute
  position.

The union of the 17 fixed-position branches is equisatisfiable with the
unrestricted profile. A single fixed-position branch is a restriction and
must not be reported as a complete profile solve.

## 4. Frozen generated instances

The three WLOG singleton-anchor instances were emitted on one capped H100
CPU core. No solver was invoked.

| profile | variables | clauses | CNF SHA-256 | map SHA-256 | payload SHA-256 |
|---|---:|---:|---|---|---|
| (4,9,4) | 3,977 | 120,207 | ebf3d8a18eb4b2fef58c8319534a377ed5644b737be91f7ace88fec489a2a4c0 | cac4e803fb12046ce2138a5307403b204506ed643f73cdb86969977734f704fb | 8d94fe795b5c7f4ca1526f5fd4e70aa130cac85ab87c13d11e9b6609c63118d6 |
| (5,8,4) | 3,749 | 104,917 | 34a8e41f685192c30a17ee6d47b204b26d57d1aaa3ee45d1d868eed35c007872 | 3c68df8462beb9b3501dd470b8b16ca4ae444dfd63813640f8e45d3141ce0306 | 64bdcb9538dcecc9a4a18a64c884da95413c73e87869b0649216ec27fc283099 |
| (5,9,3) | 4,034 | 122,850 | c5906661fc0571844ecddb2e6cd8a42932afa7126b0a2a051a1464a96036ee58 | 3424b73da9fcc8aa112f03217ad9823d9001d8457d0e4d2d36acce6488c636ee | 22f921347c7cd867cc7b594aa367baa27d8146baad90a9b76c4d3302078860ea |

The local files are respectively

~~~text
scratch/chart_blocker_4_9_4_anchorany.{cnf,map.json}
scratch/chart_blocker_5_8_4_anchorany.{cnf,map.json}
scratch/chart_blocker_5_9_3_anchorany.{cnf,map.json}
~~~

The extra clause relative to the unanchored theorem counts is exactly the
17-way singleton-anchor ALO.

One fixed-position regression was also emitted:

~~~text
scratch/chart_blocker_4_9_4_anchor0.cnf
SHA-256 434e27e3c9b1b4c87cdc1cfb291c549469aebca8f0bcbff005c982c5e7dc831e

scratch/chart_blocker_4_9_4_anchor0.map.json
SHA-256 4e1330ced30bac1a23c56f648bf604d743a426725d2d6e2b91989e9d7a7c839d
payload SHA-256 4830052251a2ef8b00e948c33d0e2f61cd26687556112db28fc60d092fe40354
~~~

It has 3,977 variables and 120,207 clauses; its last clause is the unit
selector for the singleton 0x8000 chart at absolute shortened-word position
zero. This is an emitter regression, not a solver result.

## 5. Exact scope

A decoded SAT assignment to any anchor-any instance proves a literal
length-12,873 universal word and hence \(\nu(16)=12873\). A proof-checked
UNSAT result closes its full named profile because the singleton-anchor ALO
is WLOG. UNSAT for one fixed-position branch closes only that anchor branch.

No verdict is presently available. The bundle does not address a changed
fixed gap, a moved separator, a nonlocal braid, or an arbitrary word outside
the three fixed-gap shortening profiles.
