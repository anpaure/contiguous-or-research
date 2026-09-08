# K16 WIDTH45: complete safe-cycle classification raises the source-relative floor to 104

Date: 2026-07-30  
Lane: R / native safe-cycle pricing  
Status: **exact theorem in the frozen WIDTH45/global-Sep5 model**

## 1. The result

For the frozen K16 length-eight source, its complete direction-coherent seam
catalogue, the authenticated WIDTH45 isolated-seam service interface, Boolean
endpoint balance/capacity and cyclic global Sep5, every circulation servicing
all 93 residual targets has at least

\[
                              \boxed{104}
\]

selected nonold seams/cuts.

This strengthens the earlier scale-four/GF(2) floor 103 by completely
classifying the safe simple cycles on all three `C=103` ledgers.  It remains
source-relative and does not claim a global K16 lower bound.

## 2. Exhaustive C=103 ledgers

The exact scale-four identity is

\[
4C=408+R+S,
\]

where `R` is weighted repeated service and `S` is total seam slack.  At
`C=103`, positivity and the available prices leave exactly

| branch | target multiplicity | total slack |
|---|---|---:|
| A | every target exactly once | 4 |
| B | one price-three target twice, all others once | 1 |
| C | one price-four target twice, all others once | 0 |

The three cases are exhaustive.

Every balanced capacity-one binary support is a vertex-disjoint union of
directed simple cycles.  Global Sep5 passes to every component cycle.  Since
the total selected length is 103, every cycle has length at most 103.

## 3. Branch C: complete tight-cycle absence

Branch C uses only tight seams.  An independent enumeration over all 7,742
tight seams finds exactly

```text
Sep5-safe tight simple cycles                 56
cycles with branch-C-valid target repeats    52
mandatory targets with no compatible provider 33
```

Thus branch C is impossible before any packing or conflict row is needed.
This independently confirms the earlier tight GF(2) exclusion.

See
`MATH_THEOREM_R_K16_WIDTH45_C103_BRANCH_C_SAFE_TIGHT_CYCLE_EXCLUSION_20260730.md`.

## 4. Branch B: every safe slack cycle has forbidden repeats

Total slack one gives one slack-one seam and a tight return.  Exactly 43 of
the 9,484 slack-one seams admit such a return.  Exhaustion finds exactly 43
Sep5-safe cycles containing one of them.  Their repeat signatures are

| number | repeated-target signature `(price,load)` |
|---:|---|
| 15 | `(3,2),(4,2)` |
| 15 | `(4,2)^4,(6,2)` |
| 13 | `(8,2)^2` |

None has only the unique permitted price-three repeat, so branch B is
impossible.

See
`MATH_THEOREM_R_K16_WIDTH45_C103_BRANCH_B_SAFE_CYCLE_EXCLUSION_20260730.md`.

## 5. Branch A: complete slack-at-most-four cycle classification

Every selected edge has slack at most four.  The complete graph has

```text
slack 0      7,742 seams
slack 1      9,484 seams
slack 2     10,003 seams
slack 3     19,880 seams
slack 4    124,707 seams
total      171,816 seams
```

The O3 native generator uses two exact canonicalizations:

* a tight cycle is rooted at its least vertex;
* a positive-slack cycle is rooted at its least positive seam id.

DFS enforces physical cyclic Sep5, vertex simplicity, target simplicity,
length at most 103 and total slack at most four.  It terminates without a
time or column cutoff after 1,640,500 states and returns the complete pool

| total cycle slack | 0 | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|
| cycles | 22 | **0** | 15 | 50 | 298 |

An independent Python implementation reads the compact graph, uses a global
bitset Sep5 test and separate canonical DFS, and obtains exactly the same 385
ordered seam cycles.  It then enumerates 884,763 mutually compatible subsets
of the 22 tight cycles and every positive seed (all 298 slack-four cycles and
all compatible pairs among the 15 slack-two cycles).  No positive seed has an
exact target-complement among the tight subsets; hence no exact cover exists.

The 22 tight cycles collectively service only 60 of the 93 targets.  Call the
remaining 33 targets mandatory-positive.  With no slack-one cycle, a union of
cycles having total slack four can have only one of the following positive
parts:

1. one slack-four cycle; or
2. two slack-two cycles.

The complete census checks

```text
maximum mandatory-positive targets hit by one slack-4 cycle   3
maximum mandatory-positive targets hit by two slack-2 cycles  4
mandatory-positive targets required                           33
```

Tight cycles hit none of these 33 by definition.  Therefore neither slack
partition can cover the target bank, and branch A is impossible.

This last argument is purely combinatorial once the complete safe-cycle
census is established; the accompanying CP-SAT master also dies in presolve
but is not used as proof.

### The obstruction is genuinely integral

The complete branch-A capacity/Sep5 linear relaxation is feasible.  GLOP
finds a 647-seam point, which decomposes into 101 positive simple-cycle
columns.  Solving its 101-by-101 active-row system over the rationals and then
running the independent physical point checker gives exactly

```text
seam mass             103
target service        exactly one on all 93 targets
effective slack       4
positive seams        647
cycle columns         101
capacity              <= 1
cyclic Sep5            <= 1
WIDTH5 activators      all 150 rows, w=x
```

Thus neither a linear dual nor the scale-four identity can strengthen the
floor.  The complete safe-cycle classification detects an integrality gap:
the fractional decomposition uses cycles that are not individually physical
Sep5/target-simple columns, while every binary circulation decomposes into
physical columns and is excluded above.

## 6. Independent audit artifacts

```text
scratch/export_r_k16_width45_branchA_cycle_graph_20260730.py
  SHA-256 a77a249a8ac802b386d8e56d0d5261333313494d00a36012227e58dc447140c1

complete branch-A compact graph
  SHA-256 25a4d4ed48386ad88f95e8a2a470018779ffc2a1e8c6f79327058cdee959d0aa

scratch/audit_r_k16_width45_c103_branchA_complete_safe_cycles_20260730.py
  SHA-256 1fd4f4af5eef16725cc80f698f58a5514eae71cdc80a7479da5519ced60fb135

scratch/k16_width45_c103_branchA_complete_safe_cycle_exact_cover_exhaustion_20260730.audit.json
  SHA-256 abde424b5385a29004155672b1b11302dcfdf8b3f6eb412d4102c4b546c3e206
  payload bd643b695a449460093ef4bf291727171d15f5bcd121b1966da3f7e014cf9926

scratch/branchA_mixed_cycles_smoke.json
  SHA-256 87d84518310e34ab454f216c6eac9cd0caeac1470707d5657a5831188da9d860

scratch/branchA_complete385_master.audit.json
  SHA-256 1640abbc624dbd1fad2d405b8fe68c4a1859020063b7d8fb6e815482e3839784

scratch/exactify_k16_width45_c103_branchA_fractional_20260730.py
  SHA-256 c5d4f98dcbf889b1816fc23c0c84cc8be4a5d9713264796079f48f314271e5db

scratch/k16_width45_c103_branchA_exact_fractional_point_20260730.json
  SHA-256 9599b42f5271a27a5d597fc5bf801082df9a9c9c61251e7a4b09b30732c6e81a

scratch/k16_width45_c103_branchA_exactification_20260730.audit.json
  SHA-256 172e9048b1c0a7c48e14c0e28e65580f8c40cf7c79927204d0088c84325229da
  payload 59cf68f9c579a3739fc1d0cdc377b36f8c92f53e20e687fe492ed16012d95380

scratch/k16_width45_c103_branchA_exact_fractional_point_replay_20260730.audit.json
  SHA-256 2aaf81e4888179ea3f7b45afffc297ef5fc709109613b3c2c280eef55b15f4e4
  payload 077ccd8986152964c77256e02ccc81dc6cc012a890644c4cefda6ec17b720ee3
```

The master artifact remains honestly labelled as a restricted-column result.
Its pool is nevertheless proved complete by the separate native/Python
enumeration equality, and the theorem uses the explicit 33-versus-4 coverage
argument rather than trusting the solver status.

## 7. Scope

The floor 104 is exact only for:

* the frozen asymmetric K16 length-eight source;
* the complete 211,604 direction-coherent seam catalogue;
* the authenticated 150 isolated WIDTH45 occurrences;
* Boolean seam/cut support, endpoint balance/capacity and cyclic global Sep5;
* complete service of the frozen 93-target bank.

It does not cover reverse edges, close-cut compound width-five occurrences,
another carrier, or unrestricted rethreading.  Additional q1, survivor,
residence, compiler, connectivity and literal-word rows can only strengthen
the source-relative bound.
