# K16 O5 service paths: exact component-crosspair exclusion

Date: 2026-07-30

Status: **exact scoped negative census; unrestricted K16 remains open**.

## 1. Frozen family

The source is the authenticated O5 near-carrier

```text
SHA-256 94ce24bb6dd4f8236f8565941d3aeea55caec0d1a3abb31b0419c8cd78282516
```

with four middle-replay errors and three upper holes.  The finite family does
the following, occurrence by occurrence:

1. choose one of the 74 phase-compatible three-row pre-flat service paths;
2. choose one of the two phase-compatible two-row post-flat service paths;
3. delete the five chosen rows' old incident edges and the two defective
   destination edges;
4. install the two forced service paths; and
5. reconnect all remaining loose component endpoints in every perfect
   matching, choose both final path endpoints, and test both orientations.

This is an arbitrary component cross-pairing inside that fixed service-path
family.  It is strictly wider than closing each donor vacancy in place, but
does not vary the O5 service paths or introduce a new donor macro.

## 2. Exact eight-shard result

The 74 pre choices are partitioned by residue modulo eight.  The aggregate is

```text
pre/post choices                         148
balanced component instances             148
connected endpoint reconnections   3,198,720
oriented literal carrier audits     6,397,440
capacity-sufficient exact carriers          22
arbitrary-upper-complete carriers             0
```

The per-shard exact-carrier counts are

```text
0, 0, 2, 0, 0, 10, 2, 8.
```

Among exact carriers the best upper-hole count is seven.  The retained
capacity-qualified shard minimizers independently replay with the reported
flat schedule, zero-envelope count, middle-row defect count, and upper-hole
spectrum.  No Hall/compiler conclusion is inferred from the 22 rows because
none reaches the prerequisite arbitrary-upper gate.  Three retained exact
minimizers were additionally Hall-audited and have large deficiencies
1818, 2029, and 2367; these samples are diagnostic, not part of the no-go.

## 3. Consequence and scope

Exact residence and adequate scalar lower capacity are compatible with the
component reconnection: 22 examples prove that.  What fails throughout this
family is simultaneous preservation of the upper spectrum.  Thus the next
move must change at least one of:

- the fixed O5 service paths;
- the selected row domain;
- the component macro/endpoint signature; or
- the source chronology itself.

This theorem does **not** exclude the 57,396 alternative local Hall collars,
the BDR four-token shell, another parent, or an unrestricted length-12,873
word.  The exact bracket remains

```text
12873 <= nu(16) <= 12874.
```

## 4. Authenticated artifacts

```text
scratch/search_k16_o5_service5_crosspair_reconnection_20260730.cpp

scratch/audit_root_k16_o5_crosspair_sharded_20260730.py
  SHA-256 233e52a76d01eaa8c3de1e7ef98028cbbe5cdb5df249cc358a0cb68cb888e0f0

scratch/root_k16_o5_crosspair_sharded_20260730/audit.json
  SHA-256 a19d7c95aa2362e1dca69f7cd0f57f6c9a08ae57b4c59e9f31e432e44bd644b6
  payload e6d22bf924a37c9f555219c4302187c77ac8e99fde3d9aaabd12757b743c6b9a

scratch/root_k16_o5_crosspair_sharded_20260730/frozen/
```

The independent auditor authenticates the eight-way partition and counter
sum, verifies occurrence-multiset equality for every retained minimizer, and
recomputes its variable-depth maximal envelopes and complete upper spectrum.

