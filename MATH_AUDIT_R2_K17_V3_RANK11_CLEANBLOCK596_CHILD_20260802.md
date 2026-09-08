# R2 audit of the `k=17` v3+rank11 canonical596 clean-block child

Date: 2026-08-02  
Status: independent PASS for construction and literal replay; no solver was
launched and no SAT/UNSAT claim is made.

## 1. Immutable inputs

```text
combined v3+rank11 parent
  p cnf 366131 2037474
  SHA256 8df50578978ad83704e14f9a7e69d7ede956bcadd41df36fda4a7f16b50bcfc8
combined map
  SHA256 73a8f94f2a0249c29ba599bd832a3d173d5e00ed773b3e610761e610600ca5dd
canonical residence596
  SHA256 d96d7ad6e39d3208b300221a280496090816c4f2654e931606ebdcb4a7434e50
carrier1819 factor
  SHA256 03df8fee975817414402399284d20ad7c52058ea8b5c6b8f9bf5f653ef1768b1
rank12 proof row bank
  SHA256 5b39a2678cb7512f8e10ccfd6e855a410b3f2493f5bcbdec17f1f04c22e8fa18
```

The parent is immutable.  The audit created a fresh sibling under
`/home/amodo/or15/work/r2_k17_v3_rank11_cleanblock596_child_20260802`.

## 2. Semantic row replay

Three independent reconstruction paths agree that carrier1819 has 476
missing physical rank-12 targets in 28 free `Z_17` orbits.  For every orbit,
all 17 target phases were developed literally.  Each phase has 220 clean
rank-nine owners; every clean owner has two certified factor incidences and
every clean component has a persistent target hole.

The resulting clauses are the 28 distinct negative-primary saturation rows

\[
                    \bigvee_{p\in S_Z(F)}\neg x_p.
\]

Their widths are `217..308`, their total size is 7,983 literals, and none is
empty.  A separately written full-development implementation regenerated the
proof row stream byte for byte.  Representative-owner-only cleanliness was
not used.

Carrier1819 also misses 101 rank-11 orbits.  Those are diagnostics only:
rank 11 is hard in the parent through its 728 exact `Q` rows, so a rank-11
miss in a purported parent model is a verifier inconsistency, not a lazy cut.
Carrier1819 is nonresident and is not a parent SAT model.

## 3. Append transaction

Logical-clause comparison gives

```text
canonical596 rows                     596
canonical596 rows already in parent   562
novel residence rows                    34
novel clean-block rows                  28
globally sorted/deduplicated tail        62
```

All 62 rows are negative optional-primary clauses.  The tail is sorted in
ordinary numeric lexicographic order after signed-literal normalization.  No
subsumption is performed.  The child is

```text
/home/amodo/or15/work/r2_k17_v3_rank11_cleanblock596_child_20260802/
  marker58_compact_horn_v3_rank11_bank596_clean12.cnf
p cnf 366131 2037536
SHA256 c8511f6e166c1d44369f22cd55aeb1497232975e7c16732f2545f53a77cc051a
```

The independent checker verified:

1. the complete parent body is an exact byte prefix;
2. the first 2,037,474 child clauses are an exact vector prefix;
3. `canonical596 intersect parent` has exactly 562 rows;
4. its set difference is exactly the exported 34-row residence delta;
5. the 28 proof rows are logically equal to the 28 normalized upper rows;
6. the 62-row tail is sorted, unique, all-negative-primary, and is the exact
   child byte suffix; and
7. header arithmetic, clause count, termination, and EOF are exact.

The canonical tail has SHA256
`fd338a4582e894015c7d65370e3409d713f3ffe467fed9e3fc159f773aa49521`.

## 4. Audit bindings

```text
builder source
  4489a3067d885d5b5661007d179c4f1e38b4c04b76c4a2d97f25a50ad6349c40
builder audit
  598e52beb61d52e46392eea4c9b67248c48b8790405f19fb7531e8d444bb9e65
independent child-checker source
  6aaa80591d0a4e82446f98e6cccecf7f24d8ce2a62546ca743246dd4f1b64182
independent child audit
  bf59b87647a9feff9b6b5a44bd4d45859549ed8a12b65f6662c398ceabfebd40
34-row residence delta
  a4e843fe72150448e3fb257300d9dd0d0f3826763946480153c8a283b7a8ae89
normalized 28-row clean bank
  ee636df51e363c3d8ca9d299c059ef8d82091a005e5385f56b132a54789b20a3
62-row combined tail
  fd338a4582e894015c7d65370e3409d713f3ffe467fed9e3fc159f773aa49521
```

The checker's first execution produced no verdict because of an incorrect
`eofbit` assumption after an `istreambuf_iterator` read.  The source was
patched to test `badbit`, rebuilt, and rerun fresh.  The corrected source and
PASS audit are the hashes above; the parent, child, and row banks did not
change.

## 5. Scope

This is an append-only carrier/master propagation audit.  It does not assert
that the child is satisfiable or unsatisfiable.  It does not make carrier1819
resident and does not establish source realization, compiler, opening,
exterior cross-windows, regeneration, a contiguous-OR word, or the final
extremal value.
