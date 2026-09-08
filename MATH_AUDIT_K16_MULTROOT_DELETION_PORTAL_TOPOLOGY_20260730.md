# K16 multiroot deletion portal topology and constructive portfolio

Date: 2026-07-30  
Lane: `multiroot_deletion_lns`  
Status: **exact topology census complete; constructive searches live**

## 1. Scope

The frozen source is the independently verified universal word

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

The authenticated deletion census has exactly `191` deletion roots with at
most four holes.  This lane studies all of them rather than only the unique
one-hole deletion at `p=1`.

For each root, each physical position, and each replacement capable of
providing at least one current hole, the O3 C++ census evaluates the exact
interval-OR multiplicity delta.  It records:

- replacements which install every current hole;
- the resulting ejection-debt set;
- the number of physical provider positions;
- multiplicity reserve on every installed hole;
- the resulting number of singleton targets; and
- whether the output debt set is another one of the 191 low-hole roots.

Thus the ranking is not a ranking by hole count alone.

## 2. Exact census result

The output has exactly `191` rows.  The distribution of the minimum hole
count after a full-provider exit is

```text
after holes:     1  2  3  4  5  6  7  8  9 10 11 12  no full provider
roots:           2  2  3  4 55 47 40 14  7  2  2  1  12
```

The two `after=1` roots are precisely the already studied deletions `p=0,1`.
Excluding them, the strongest immediate exits are:

| deletion | source holes | best output holes |
|---:|---|---|
| 2 | `9325,11373,13421,30317` | `5229,21613` |
| 12872 | `52321,52323,52327,52455` | `52833,52835` |
| 3 | `5229,21613` | `9325,13421,30317` |
| 12871 | `35943,36071,48367` | `35938,36070,40166` |
| 6440 | `10365,42093,46189,63085` | `37997,43117,54381` |

The exit geometry is narrow.  Among the 191 roots, the number of physical
positions which can install every current hole begins

```text
positions: 0  1  2  3  4  5  7   10  23  267  284  502  12873
roots:    12 53 42 38  2 35  3    1   1    1    1    1      1
```

Only `11` roots have a full-provider edge to another low-hole deletion root,
with `16` directed edges total.  The only nontrivial strongly connected
components are

```text
{0,1}
{2,3}
{6440,6441}
{6959,6960}
{12871,12872,12873}.
```

This is a useful structural correction: the low-hole deletion landscape is
not one large version of the canonical H/A shuttle.  It consists mostly of
isolated, very narrow portal fibres, plus five small exact shuttles.

The sum of all full-provider replacements is `38,696`.  Independently, the
previous exhaustive delete-plus-one-substitution run retained `installing=`
counts for each deletion.  All 191 counts agree row for row with this new
census.  That independently cross-checks the provider enumeration; the new
data are the per-position topology, debts and reserves.

## 3. Constructive consequences

A deterministic 24-root portfolio takes an equal share from three fronts:

1. smallest output debt;
2. best unique-witness reserve (fewest singleton targets after the exit); and
3. broadest physical portal topology.

Each root receives a 63-position support.  Full-provider positions come
first, then positions which provide only some of the holes.  The latter are
essential: from deletion `p=2`, the reproducible two-edit circuit

```text
position 2: 0x0065 -> 0x004d
position 1: 0x2800 -> 0x2000
```

passes through partial providers and reaches the one-hole state
`{0x2c6d}`.  A search restricted to full-provider-first moves cannot see this
circuit.

The ordinary portfolio has already reproduced three independent funnels:

- deletion `p=3` reaches a new one-hole `0x2c6d` word (SHA-256
  `cc99ae18a961350d7bb06aa6c8de42123f301c82c1fa9c4494031322a1933e80`);
- deletion `p=6440` reaches the two-hole blocker pair
  `{0x4879,0x6879}`; and
- deletion `p=8476` reaches
  `{0x4879,0x6879,0xa0db,0xa0df}`.

The first new H word has an exact unrestricted one-substitution NO_PASS:
`26,968` substitutions install its hole, and its minimum-debt portal again
maps `0x2c6d` to `0xa86d`.  This is a new geometry but the same attractor.

To avoid merely rediscovering that attractor, the ejection engine now has a
separate, optional topology-aware objective.  With

```text
K16_LNS_AVOID_HOLES=11373,43117,18553,26745
```

the four recurrent H/A/P/Q hole masks are penalized strongly enough that a
novel two-hole state outranks a known-attractor one-hole state.  This changes
only search order; every move and every claimed candidate is still evaluated
by the exact interval-OR ledger.

## 4. Exact small-circuit lane

`k16_multiroot_fullprovider_twoedit_20260730.cpp` independently exhausts the
following scoped class for a fixed root:

1. the first substitution installs every source hole, allowing arbitrary new
   debts;
2. the second substitution is an arbitrary one-cell completion.

For deletion `p=2`, all `24` first exits and `2,623,704` exact second provider
values were tested.  There is no completion in this class; the best result has
three holes.  This does not exclude a partial-provider-first circuit (and the
two-edit H circuit above demonstrates why that distinction matters).

## 5. Artifacts and exact boundaries

```text
scratch/k16_multiroot_deletion_portal_rank_20260730.cpp
  SHA-256 7e81c330c7e035bf06592f90bdde7cf10a483dd057f97683b889818df1a643b5
scratch/k16_multiroot_deletion_portal_rank_20260730.tsv
  SHA-256 fe51c4301cab3be93900a9f848082a8fd8a7336bf1d0f9016cb512df2f9a33d2
scratch/materialize_k16_multiroot_deletions_20260730.py
  SHA-256 37ebc81d2a32fece522c5c682b7cd6d95841f74aed2c60acacdbed63058bc59c
scratch/run_k16_multiroot_deletion_lns_20260730.py
  SHA-256 788d703031930aebff619fe2dbc5c171687702dba9796373be34fdc2c65a8c7e
scratch/k16_expanded14_ejection_lns_20260730.cpp
  SHA-256 b2586e9ffc27cd01d249cb105e78a8caa71006cb9ba627240fb8744b97acebee
scratch/k16_multiroot_fullprovider_twoedit_20260730.cpp
  SHA-256 832c1edbf6cbfc7959276d39ce1e0e654f2e3ee772e0e6dd46322f63c159d998
scratch/k16_delete3_multiroot_ejection_h1_20260730.word
  SHA-256 cc99ae18a961350d7bb06aa6c8de42123f301c82c1fa9c4494031322a1933e80
```

The exact topology census is complete for all 191 roots and for one-cell
full-provider exits.  It is not a global two-edit or three-edit no-go.  LNS
timeouts and finite iteration runs are heuristic searches, never UNSAT
claims.  The exact two-edit result is restricted to full-provider-first
circuits and is reported as such.

The remote live package is retained at

```text
/home/amodo/or15/work/multiroot_delete_lns_20260730_7bb6c4f1
```

on the H100 host; only CPU cores are used.
