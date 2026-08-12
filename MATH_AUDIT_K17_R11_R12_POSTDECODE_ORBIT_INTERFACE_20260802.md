# K17 rank-11/rank-12 postdecode orbit interface

Date: 2026-08-02  
Status: exact scoped decoder/audit utility.  It prepares the deep-upper target
interface for the first compact-Horn v3 model.  It does not assert residence,
a source factor, a compiler, or a universal word.

## Construction

The cyclic rotation action of `Z_17` is free on ranks 11 and 12.  Hence the
literal target sets split into

```text
rank 11: C(17,11)/17 = 728 orbits
rank 12: C(17,12)/17 = 364 orbits
total:                    1092 orbits
```

After the quotient model is decoded to a 24,310-edge physical factor, the
auditor:

1. verifies every rank-eight facet, rank-nine endpoint and rank-ten cap;
2. reconstructs the unique physical owner cycle fail-closed;
3. enumerates every cyclic consecutive-owner union until its rank exceeds 12;
4. compresses rank-11/rank-12 targets to canonical rotation representatives;
5. checks that coverage is all-or-none on every 17-element orbit and that
   every witness multiplicity is divisible by 17;
6. emits a complete target table and a separate missing-orbit list.

The target table fields are

```text
rank
orbit_rep
orbit_size
covered_translates
witness_intervals
orbit_witness_multiplicity
min_owner_width
first_start
first_width
first_literal_target
```

This is an interface rather than an eager SAT encoding.  The intended first
resident-model pipeline is

```text
compact Horn v3 model
 -> fail-closed quotient/factor export
 -> literal residence/connectivity/voltage replay
 -> rank11/rank12 orbit interface
 -> deep-upper CEGAR or exact repair
```

Source:

```text
scratch/audit_k17_rank11_rank12_orbit_interface_20260802.cpp
SHA e3274d4ef2a4c3bbaed3e7f5704269e2f75bc1853451e47bea0e629bd0e32c80
```

Retained H100 root:

```text
/home/amodo/or15/work/qa_k17_r11_r12_orbit_interface_20260802_quotientaudit
```

## Exact controls

| factor | rank-11 missing orbits | rank-12 missing orbits | rank-11 witness intervals | rank-12 witness intervals |
|---|---:|---:|---:|---:|
| clean floor1955 | 105 | 21 | 33,184 | 37,927 |
| clean floor1989 C14 | 101 | 21 | 33,711 | 38,981 |
| dirty floor1938 | 101 | 25 | 33,490 | 38,862 |

Multiplying missing-orbit counts by 17 recovers the independently audited
literal holes exactly:

```text
clean1955: 1785 / 357
clean1989: 1717 / 357
dirty1938: 1717 / 425
```

The dirty floor1938 factor also has one missing rank-thirteen orbit; that row
is intentionally outside this rank-11/rank-12 interface and remains a
separate decoder gate.
