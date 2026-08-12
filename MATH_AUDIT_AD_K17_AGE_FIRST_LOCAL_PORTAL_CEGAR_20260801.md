# Independent scope audit: K17 age-first local-portal CEGAR

Date: 2026-08-01  
Lane: AD  
Status: **PASS for the theorem, ordered companion, exact-z local cuts, and
H100 structural generation; UNKNOWN for a real age-first SAT incumbent.**

## 1. Audited claim

The audited package turns a connected primitive, lower-rainbow,
depth-3-resident SAT assignment of the age-first `D/H` master into one of two
outputs:

* `PASS_TRIM3_HIGHER_UPPERS`, meaning that the chosen normalized opening has
  no rank-11 through rank-16 strict-upper hole (rank 10 is eager and rank 17
  is automatic); or
* `CUT_LOCAL_HIGHER_UPPERS`, accompanied by incumbent-violated semantic CNF
  rows over exact ordered-turn atoms.

This is not a K17 construction.  No authenticated SAT assignment of the
full age-first master with these properties is currently frozen.

## 2. Exact host separation

The correct host is

```text
scratch/build_k17_incidence_bimatching_age_skeleton_20260801.cpp
```

and not the older unordered 51,480-turn host.  The age direction makes a
same-facet turn `(D_e,H_f)` ordered.  The companion reconstructs all 102,944
allowed nonloop ordered turns and defines

\[
 z_{e,f}\leftrightarrow(D_e\wedge H_f).
\]

Its count proof independently gives 308,831 variables and 824,693 clauses:
102,944 `z` atoms, 102,944 roots, 102,943 Sinz auxiliaries; three clauses per
conjunction, 1,144 eager rank-10 rows, two root rows per atom, and `3n-3`
exact-one-root rows.

The root is the common-facet-phase-zero physical copy, with endpoint phases
`-s_D,-s_H`.  It is not tail-owner phase zero in general.  Root restitution
requires a distinct selected `z` atom of the same rank-10 rotation orbit.

## 3. Mathematical cut audit

For a target `U`, let `V_U` be all rank-9 owners contained in `U`.  A target
is present in an opened owner path exactly when one component of the path
induced by `V_U` has owner union `U`.  Hence a missing target forces any
repair retaining the root to select an ordered turn crossing two incumbent
induced components.

The emitted row is

\[
 \bigvee_{a\in B_U}z_a
\]

for a cyclic hole, or

\[
 \neg o_*\vee\bigvee_{a\in B_U}z_a
\]

for an opening-only hole.  `B_U` is the complete set of allowed quotient
turn atoms with a nonroot physical copy crossing two old components.

The following adversarial corrections were incorporated.

1. Replacing each conjunction by one currently false `D/H` role is sound
   only as a weaker projection.  The frozen clauses use exact `z` atoms.
2. An opening-only row without `-o_*` is false: moving the root can repair a
   target without changing its provider turns.
3. Relative phase modulo 17 cannot be discarded after opening.  Cyclic
   holes compress to one rotation-orbit row, while opening holes remain
   physical-phase-specific.
4. The root deletes one physical copy, not all 17 copies of its turn orbit.
5. Johnson edges whose two endpoints lie in one quotient owner orbit are
   forbidden self-loop turns in this master.  The final separator skips
   exactly these; the superseded pre-patch source could fail during portal
   lookup.
6. The cover-separator converse and prime-implicate statement is exact only
   in the undirected monotone label-reachability relaxation.  Weak
   connectivity is an over-approximation of directed chronology.  The
   forward validity of the emitted rows is unaffected.

If `Q` is the opened rank-10 edge colour, every opening-only target contains
`Q`.  Thus there are at most

\[
 7,21,35,35,21,7
\]

such targets at ranks 11 through 16, or 126 total.  The separator checks
this containment and bound fail-closed.  Cyclic holes need at most 1,281
orbit rows.  Therefore the old candidate-1911 deficit of 1,989 physical
holes cannot be interpreted as 1,989 opening-only obligations; its stored
98 rank-11 plus 19 rank-12 orbit rows are a compression calibration only.

## 4. Fail-closed implementation audit

Before producing any upper row the separator:

1. replays every clause of the composed CNF;
2. authenticates the age and ordered-layer maps;
3. checks `z <-> D&H`, 1,430 selected atoms, one root, all 1,144 eager
   rank-10 groups, and a distinct selected root-colour provider;
4. checks both perfect matchings, one quotient component, and nonzero
   voltage;
5. expands all 24,310 physical owners and requires a bijection;
6. requires all 24,310 adjacent rank-8 intersections to be distinct; and
7. requires every cyclic positive coordinate run to have length at least
   four.

`DEFER_TO_TOPOLOGY_OR_VOLTAGE_SEPARATOR`, lower-rainbow rejection, and
residence rejection produce no upper cuts and return exit 3.  A driver must
branch on the JSON status; it must not blindly append a zero-row cut file and
retry.  An empty cyclic portal bank is different: it is an exact empty CNF
clause and the dedicated composer preserves it.

The implementation emits the full cross bank `B_U`.  It does not yet run
the optional greedy prime minimizer, serialize positive witnesses on PASS,
or separate cyclic holes while the quotient factor is disconnected.  These
are strength/certificate omissions, not soundness defects.

## 5. H100 structural regression

Only deterministic generation and compilation were run; there was no SAT
solve.  The unique directory was

```text
/home/amodo/or15/work/ad_k17_age_local_portal_a296f14c_84cb8ffe_20260801
```

The staged-rank7 age host generated

```text
2,655,796 variables
12,882,305 clauses
```

in 2.28 seconds at 6,784 KiB maximum RSS.  The ordered companion generated

```text
102,944 ordered atoms
308,831 added variables
824,693 added clauses
maximum variable 2,964,627
```

in 0.59 seconds at 9,728 KiB maximum RSS.  Exact composition produced
2,964,627 variables and 13,706,998 clauses in 7.16 seconds at 5,632 KiB
maximum RSS.  The final separator compiled with O3, `-Wall -Wextra
-pedantic`, and zero warnings.

This run pins only the staged-rank7 structural face.  A future PASS has full
lower-suffix scope only if the default full-lower base CNF/map/stats are
separately pinned.  The upper separator itself is valid for either base
because it authenticates and replays the CNF supplied to it.

## 6. Exact boundary

A future positive separator result proves a connected primitive resident
owner carrier, cyclic lower-q1 rainbow, complete cyclic upper q1, and a
strict-upper-safe trim-3 opening.  The opening still deletes one lower-q1
facet address.  Generalized lower compilation, suffix restitution,
common-cap matching, and literal all-mask OR replay remain outside.

Candidate 1911 is intentionally excluded as a master seed: it is
nonresident and has two lower palette holes.  Its negative trim-3 report is
only a regression statistic.

The independent verifier is

```text
scratch/verify_ad_k17_age_bimatching_trim3_local_orbit_cuts_20260801.cpp
SHA 79edf4c4f83f33757b043bd93c79aa411a75c018b8121dbaa1bd45cf7afe64aa
```

It reconstructs target components as literal runs rather than reusing the
separator's DSU and checks complete row coverage, exact cross banks, the cut
CNF and the separator JSON.  It compiled on H100 with zero warnings; runtime
verification is necessarily pending the first authenticated SAT incumbent.
Its complete scan is `O(2^17 W)` and must remain an H100-CPU step.

The final source hashes are

```text
ordered layer  a296f14c346ca72ddc2aef0dde064427de478f217afa2c68d17530e08b92e44d
separator      84cb8ffe52419d16a502e470f1a9a2ac6bf88d14277249ded1a02f17a74722d4
verifier       79edf4c4f83f33757b043bd93c79aa411a75c018b8121dbaa1bd45cf7afe64aa
composer       32db7b04ab6cb83cd91a2b33c1122fc6ab7fc047c8aabae664ad788b91a4c246
```

The exact run hashes and resource figures are in
`scratch/ad_k17_age_bimatching_local_portal_cegar_20260801/run_manifest.json`.
