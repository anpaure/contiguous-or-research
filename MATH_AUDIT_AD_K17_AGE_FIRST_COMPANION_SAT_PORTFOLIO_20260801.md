# Audit: K17 age-first ordered-companion SAT portfolio

Date: 2026-08-01

Status at freeze: **ROUND 0 TERMINATED EXACT UNKNOWN / NO SAT OR UNSAT
CERTIFICATE / GLOBAL SCOPE UNKNOWN**.

This note records the exact logical scope, launch package, fail-closed
postprocessing contract, and terminal runtime telemetry for the 2,964,627-
variable age-first companion CNF.  Both 1,800-second workers ended without a
SAT or UNSAT line.  The result is therefore exact `UNKNOWN`: it has no
feasibility or infeasibility implication.

## 1. Decision status of the composition

The composed formula

```text
p cnf 2964627 13706998
```

is a self-contained SAT instance.  It does not require a previously supplied
incumbent.  It is, however, only a necessary relaxation for the loopless,
`Z_17`-equivariant, fixed-type-MASS age-bimatching subclass.  Thus:

- an independently proof-verified UNSAT result excludes that subclass;
- a SAT result is only a CEGAR incumbent and is not a K17 word;
- neither outcome alone decides arbitrary K17 carriers.

The formula eagerly contains the type/age skeleton, the `D` and `H` perfect
incidence matchings, the exact age bridge, the staged rank-7 lower suffix
rows, all 102,944 allowed nonloop ordered conjunctions
`z_(d,h) <-> D_d and H_h`, all 1,144 cyclic
rank-10 orbit ALOs, one normalized opening root, and a distinct provider for
the root edge's rank-10 union colour.

The following remain lazy or absent: quotient connectivity and nonzero
voltage; lower suffix ranks 2 through 6; trim-3 upper ranks 11 through 16;
the opened lower-q1 boundary restitution; generalized lower compiler/common
cap; and literal OR-word compilation.

## 2. Exact CEGAR contract

For every reported SAT assignment the pipeline performs, in order:

1. complete assignment census for every variable `1..2964627` and literal
   replay of all 13,706,998 clauses;
2. independent age/rank-7 reconstruction, with flag and incidence exports;
3. quotient topology and voltage separation;
4. semantic identity comparison between the topology separator's headered
   cut bank and the independently reconstructed headerless bank;
5. if connected and primitive, require the literal physical lower rainbow
   and cyclic minimum positive run four, then perform exact trim-3
   ranks-11-through-16 separation;
6. independent reconstruction of every local portal row, candidate bank,
   incumbent violation, cut CNF, and separator audit;
7. fail-closed composition of a verified nonempty cut bank into the next CNF.

`DEFER_*` and `REJECT_*` local states are not treated as cuts.  A zero-row cut
file is never appended merely because the separator returned nonzero.

The complete-assignment condition is essential.  The semantic readers treat
omitted variables as false, so a partial but clause-satisfying witness is
rejected before any topology or portal inference.

If a connected primitive incumbent is reached, the age verifier also
reconstructs the 24,310-owner physical lift and literally checks its `D^3`
source, rank-8 lower rainbow, and staged rank-7 suffix.  It exports sufficient
flags/incidences to reconstruct the carrier.  No compiler-ready source-word
serializer is claimed in this package.

## 3. Authenticated inputs

Remote source directory:

```text
/home/amodo/or15/work/ad_k17_age_local_portal_a296f14c_84cb8ffe_20260801
```

Inputs:

```text
b6efe31e0582fe106793a865ab44048f49a3f71b6a1a6dfda4d57b6cf71365f8  composed.rank7_ordered.cnf
82bb0802f07776a78dd156e21693dcb60006beecc9e4325e6256dccebd6e0db4  base.rank7.map.tsv
5a65f5d8a761251a2b5c898851ef60b8df9f8e54be9bd101f45f0e3ea8721eb1  ordered.layer.map.tsv
```

Unique round directory:

```text
/home/amodo/or15/work/ad_k17_age_local_portal_a296f14c_84cb8ffe_20260801/portfolio_round0_20260801T1255Z
```

Pinned solver binaries:

```text
aeae2850e0491ace333f8cba8958be165dd24ba7a3dea130a39507c8bbd8fe6e  Kissat 4.0.4
49c86c5f8447d768906dcd12d62fb4752e80a48a0d52bbc633929f32eec00b3d  CaDiCaL 3.0.1
```

## 4. Portfolio

The two nonduplicate workers were launched at approximately
`2026-08-01T12:55Z` on H100 CPU only:

| solver | mode/seed | core | limits |
|---|---:|---:|---|
| Kissat | `--sat`, 1702528 | 24 | 1 CPU, nice 15, 24 GiB AS, 32 GiB file, 1800 s solver / 1830 s hard wall |
| CaDiCaL | `--sat`, 1702529, text DRAT | 25 | same |

All new solver output and any proof are written under `/home`, not
`/dev/shm`.  `SAT` is accepted only with exit code 10 plus exactly one
`s SATISFIABLE`; this is only a **raw solver SAT** until postprocess exit zero
and all applicable audit JSONs pass.  `UNSAT` is accepted only with exit code
20 plus exactly one `s UNSATISFIABLE` and an independently checked proof.
The round-0 worker preserves CaDiCaL's text proof as a partial artifact but
does not itself run `drat-trim`; proof verification is a separate mandatory
post-result step.  Timeout, OOM, ENOSPC, signal termination,
malformed/partial model, or replay failure is `UNKNOWN`.  In particular, the
worker's raw `status.json=SAT` is never by itself an authenticated incumbent;
`postprocess.exit_code=0` and the exact replay/result files are also required.

## 5. Local sources frozen for reproduction

```text
57d798ed6fbb2c047a267146d813f0936a24c42fb38c0412c9c3216678117e7a  scratch/launch_ad_k17_age_bimatching_portfolio_round0_20260801.sh
6ae1e287dfa5bdf538a978615bf7ac59754b997d66bc2f06ce0cb3b6e2c9de26  scratch/run_ad_k17_age_bimatching_portfolio_worker_20260801.sh
c20ad7479a851839f47d6c370d98c48edd2132eb6de79c5193b89ec2e23d1967  scratch/postprocess_ad_k17_age_bimatching_sat_20260801.sh
fdc888d947984729e4168b264e6e931cbe1a0aa7e30dd2ad5bdf1b48972bea17  scratch/verify_ad_k17_age_bimatching_sat_assignment_20260801.cpp
7a061f1c442417b871eae95634e9f5c721b3aa2e93e73000f527128b89e91dba  scratch/compare_ad_k17_topology_cut_banks_20260801.cpp
```

The existing ordered-layer, local separator, independent local verifier, and
fail-closed composer retain the hashes recorded in handoff item 2528AD.

## 6. Terminal telemetry

The exact terminal statuses were:

```text
Kissat: UNKNOWN; conflicts 3,207,291; decisions 193,761,884;
propagations 13.60 billion; remaining variables 1,051,276;
irredundant clauses 11,192,607; search/simplify 1216.5/579.0 s;
peak RSS 3.39 GB.
Status SHA d5202761b8b2d175ea8b09fde783bb75e3dd44f4538e21f071f0850b2c64ac5f.

CaDiCaL: UNKNOWN; conflicts 2,201,817; decisions 69,251,034;
propagations 7.35 billion; remaining variables 951,722;
irredundant clauses 17,028,807; search/simplify 1345.9/449.3 s;
peak RSS 3.70 GB.
Status SHA d913d551dd7b055c652172e21588d482501f35e1fa9c495fc7cbab4c21c57a60f.
```

The partial CaDiCaL DRAT is 3,366,250,228 bytes with SHA
`bbce0baf...`.  It is noncertifying and carries no UNSAT implication.

The telemetry points to search/simplification cost in the deterministic
cardinality skeleton rather than a memory or output failure.  In particular,
it does not justify a larger duplicate portfolio on the same formula.

## 7. Exact boundary

Had a SAT assignment survived all postprocessing, the strongest possible
positive round result would have been:

> a connected primitive physical age lift with cyclic rank-8 lower rainbow
> and minimum positive coordinate run four, satisfying the staged rank-7
> lower rows, eager rank-10 rows, and the exact source-3-trimmed/opening upper
> rows at ranks 11 through 16.

It still is not a literal OR word.  The one opened lower-q1 boundary address,
lower ranks 2 through 6, generalized lower compiler, suffix/common-cap, and
final literal interval realization remain independent gates.

No such assignment was obtained in round 0.
