# Audit: K17 round047 owner-phase transport on R1921/H1694

**Date:** 2026-08-02  
**Status:** static transport succeeds in both phases; the complete source
projection fails in both phases.  R1921 is retained as a calibration result.

## 1. Input authentication

The authoritative carrier is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/checkpoint_joint_res1921_deep1694
```

Its manifest SHA is
`abb3715e7f70dcfbb8917b061e8e8d591e542712091af944fb332c7a55639304`
and its model SHA is
`353a9e97239666e88f93b3fbf89fdee95240ef1a5099af408b28692f930a6f15`.
An independent `sha256sum -c MANIFEST.sha256` accepted every entry.  The
passive and independent reports give exact q1 coverage, 48,620 selected edges,
one component, best linear residence 1,921, and deeper holes
`(1457,235,2)`, totaling 1,694.  The literal upper-deck containment report
certifies zero losses and eight gains in each opening.

The source table is the independently projection-perfect round047 artifact:

```text
table SHA256             95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
projection audit SHA256  2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a
Hall certificate SHA256  88088c986ade02910cff46fb5bf9b1bdfef76a34331a3e99983f9d92ed9aae87
```

That input audit has matching `16898/16898`, deficiency zero, and zero hard
heads.  The universal incidence map SHA is
`80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a`.

## 2. Carrier and static transport replay

The adapter reconstructs a connected, unicyclic selected factor.  The root
degree histogram is `(1,24308,1)`, every owner has degree two, and leaf peeling
leaves a 43,340-vertex even cycle containing 21,670 roots.  Hence exactly two
perfect owner phases exist; 2,640 off-cycle phase edges are forced.

The adapter emits both phases and a complete rowwise incidence diff.  Phase
zero changes 11,317 owners, phase one changes 12,669, and the phases differ on
21,670 roots.  A separately compiled verifier accepts both tables with:

```text
rows                        24310
selected owner matching     24310
all rank <= 8 targets       65535, exactly once
length histogram (1,2,3)    (0,7395,16915)
minimum long lower bound     16915, attained
```

Thus any later failure is not a malformed payload table, incomplete target
partition, or invalid selected-factor phase.

## 3. Complete projection replay

A separately compiled exhaustive verifier enumerates every long menu and all
nine strict two-transition interval menus, treating short roles as address
reset sockets.  It proves long-transition monotonicity and computes the exact
maximum matching and Hall shore for each transported table:

```text
phase 0: matching 16827/16898, deficiency 71, zero 51,
         Hall heads/neighbors 110/39, graph FNV64 f1fe6a14954c6b5d
phase 1: matching 16828/16898, deficiency 70, zero 55,
         Hall heads/neighbors 102/32, graph FNV64 806ec48a36ea7202
```

Both verifier processes exit negative and emit their full Hall and isolated
head lists.  Therefore a projection-perfect table on the res1972 carrier does
not remain projection-perfect after either licensed R1921 owner rephase.

## 4. Fail-closed boundary

The smallest missing coupling exposed here is owner-phase-dependent supplier
incidence: static roots, targets, and owner matchings all survive, but changing
the owner literals removes the complete hard-head matching.  The exact next
repair must recouple the payload table with the chosen carrier phase (or use a
larger multi-transition macro); it cannot reuse round047 as a carrier-agnostic
table.

Because both literal projections are negative, no same-role state balance,
occurrence-labelled source chronology, residence, deeper upper, DM,
common-cap, compiler, or word is in scope.

Frozen bundle:

```text
scratch/ad_k17_res1921_round047_phase_transport_obstruction_20260802/
```
