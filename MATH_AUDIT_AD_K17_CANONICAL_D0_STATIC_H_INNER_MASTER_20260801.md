# Audit: canonical-`D0` static-`H` inner master

Date: 2026-08-01

## 1. Verdict

The frozen canonical-`D0` static-`H` instance is **PASS** as an exact
age-relaxed inner master.

For the three hashes in Section 3, the formula is satisfiable if and only if
there is a nonloop perfect matching `H` from the 1,430 rank-8 facet orbits to
the 1,430 rank-9 owner orbits whose `D0`--`H` turns hit every one of the 1,144
rank-10 orbits.  It imposes no age or direct-rank-7 condition.

Consequently:

- a replayed SAT assignment is only a static upper-`q1` candidate for the
  age/rank-7 subproblem;
- proof-verified UNSAT excludes this entire fixed `D0` from every solution of
  the fuller age/rank-7/upper-`q1` projection; and
- solver timeout, resource exhaustion, an unverified proof, or failed replay
  proves nothing.

## 2. Exact encoding proof

Fix the authenticated perfect matching `D0`.  Let `E(D0)` contain every
quotient incidence `e=(f,o,s)` at facet `f` except those whose owner `o` is
the `D0` owner at `f`.  The exclusion is exactly the quotient-owner loop
condition used by the compact base.

Introduce one Boolean `x_e` for every `e in E(D0)`.  The CNF contains:

1. pairwise exactly-one clauses on the candidates incident with each facet;
2. pairwise exactly-one clauses on the candidates incident with each owner;
3. one at-least-one clause for each rank-10 orbit colour of the physical
   union of the fixed `D0` tail and candidate `H` head.

The first two families are equivalent to `H` being a perfect matching.  The
third is equivalent to upper-`q1` orbit surjectivity.  Since 17 is prime and
rank 10 is neither 0 nor 17, every rank-10 orbit has length 17, and

```text
binom(17,10)/17 = 19448/17 = 1144.
```

Thus quotient-orbit surjectivity is exactly literal physical rank-10
coverage under the equivariant lift.

At a fixed facet at least the selected `D0` owner incidence is excluded, so
the facet degree is at most 8.  The owner degree is at most 9.  Therefore the
generic bounds are

```text
|E(D0)| <= 1430*8 = 11440,

clauses <= 1430*(1+C(8,2))
         + 1430*(1+C(9,2))
         + 1144
         = 95524.
```

The frozen instance is smaller: 11,438 variables and 84,056 clauses.

## 3. Independent frozen-artifact replay

The checker

```text
scratch/audit_ad_k17_canonical_D0_static_H_semantics_20260801.cpp
SHA-256 849bcfc1202b5488271daea23f12faa32586c4d0c1644fef7c4c9074142c0fac
```

independently performs all of the following:

1. reconstructs the 1,430 rank-9 owner orbits, 1,430 rank-8 facet orbits, and
   all 12,870 owner--facet incidences of the `Z_17` quotient;
2. checks that the 1,430 frozen `D0` rows form a perfect matching and that
   every incidence ID, owner, facet, shift, and original variable ID is exact;
3. independently enumerates every and only nonloop `H` incidence against
   `D0`;
4. recomputes the aligned physical tail/head, rank-10 union, canonical orbit
   representative, and phase of every candidate;
5. checks the layer map and compact static map row-for-row against that
   reconstruction; and
6. reconstructs every exact-one and colour clause and compares the whole CNF
   clause-for-clause, in addition to checking all three SHA-256 hashes.

Frozen inputs:

```text
952786fd3f20263757289029e966594953a7cf420993f360072f51090b275deb
  fixed_D.layer.map.tsv

9b5f1ab6b513cedab1f0e690ea273495b35998f1c4f9c38af871b8d2c97437e2
  static_H.map.tsv

65104be271c225d0b94b65c3b6489101bbbd92f31e63fc48f67797d848bdd6cb
  static_H.cnf
```

The independent replay returned

```text
PASS_CANONICAL_D0_STATIC_H_EXACT_REPLAY
owner orbits        1430
facet orbits        1430
rank-10 orbits      1144
fixed D edges       1430
candidate H edges  11438
present colours     1144
empty colours       0
CNF variables       11438
CNF clauses         84056
max facet degree    8
max owner degree    8
max colour degree   10
```

Audit artifact:

```text
scratch/ad_k17_canonical_D0_static_H_semantic_audit_20260801/semantic.audit.json
SHA-256 e43d127de2871699323536a297efd283da6edbb3b5cbfd95a1036620764c76e7
```

This closes the provenance caveat for the three frozen hashes.  The generic
builder still relies on an authenticated layer map when used on a different
`D`; this frozen checker is not a blanket audit of arbitrary future maps.

## 4. Builder source audit

The formula builder is

```text
scratch/build_ad_k17_fixed_D_static_q1_H_cnf_20260801.cpp
SHA-256 e881e797025afa198155263befcd85a39b3919287b8e1b1b1eefbe5242966c04
```

Its exact-one encoding, sequential variable allocation, clause count, and
degree bounds are correct.  Its source-level limitation is that it trusts
the supplied layer map for incidence geometry, candidate completeness, and
canonical colour labels.  In particular, it counts absent colours as
`1144 - number_of_observed_keys` rather than reconstructing the target set.
That is sound for an authenticated layer map but not for an arbitrary or
truncated map.  Section 3 supplies the missing independent authentication
for canonical `D0`.

## 5. Worker audit

Worker:

```text
scratch/run_ad_k17_fixed_D_static_H_worker_20260801.sh
SHA-256 bab067f5261106e5e4f01cbb8d4e92bc86c44b6510b833036f60a12b33b1c211
```

The worker is **PASS** for the frozen instance:

- it pins the exact static CNF/map, Kissat, assignment verifier, and
  `drat-trim` hashes;
- it requires exit 10 plus exactly one exact `s SATISFIABLE` line and no
  UNSAT line before SAT replay;
- it replays every declared variable and every DIMACS clause independently;
- it requires exit 20 plus exactly one exact `s UNSATISFIABLE` line before
  proof checking;
- it promotes UNSAT only after `drat-trim` returns successfully with exactly
  one `s VERIFIED` and no `s NOT VERIFIED`; and
- every timeout, malformed status, incomplete model, failed replay, or failed
  proof becomes `UNKNOWN` or leaves no authenticated status.

The semantic meaning of the two positive terminal statuses is exactly:

```text
SAT_STATIC_H_REPLAYED_AGE_PENDING
UNSAT_VERIFIED_STATIC_H_FIXED_D0
```

The first does not certify ages.  The second certifies only the fixed-`D0`
no-good, not failure of every outer `D`.

Minor operational limitations do not create a false theorem result in the
intended single-worker use: the proof checker has no separate memory/resource
ledger, and two processes pointed at the same initially empty output
directory could race.  Use a unique output directory and preserve the input
hash ledger.

## 6. Gates deliberately omitted

Neither SAT of this inner face nor its replay proves:

- age compatibility or direct rank-7 coverage;
- quotient connectivity or nonzero voltage;
- cyclic depth-3 residence;
- lower ranks 2 through 6;
- upper ranks 11 through 16 or source-3-trimmed safe opening;
- opened lower-`q1` boundary restitution;
- generalized lower compiler/common-cap compatibility; or
- a literal contiguous-OR word.

These omissions make the static face a sound relaxation for fixed-`D`
exclusion and a lightweight candidate generator, not a complete K17 model.
