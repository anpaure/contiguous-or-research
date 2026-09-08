# K16 delete-p1 collar594: selected p12826 ghost surgery and exact cube7 CNF

Date: 2026-07-31  
Status: **exact target-complete model audited; solver portfolio staged**

## 1. Scope

Fix the authenticated length-12,873 delete-p1 word

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
SHA256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

and the nineteen editable positions

```text
[0,5) union [6435,6444) union {12826} union [12869,12873).
```

This is a strict enlargement of the solver-free-impossible 18-cell fibre.
It is not a WLOG reduction of an arbitrary length-12,873 word and yields no
unrestricted K16 conclusion.

## 2. Why p12826 is selected

The two fixed first-middle copies of `0xc279` lie on
`[11726,11728]` and `[12826,12828]`.  The complete six-position surgery
census proves that `p12826` is the unique best one-cell ghost surgery under
literal coverage.  Exactly sixteen values remove the later ghost while
preserving every other middle label; each leaves precisely

```text
{0x2c6d, 0xc679}.
```

They form the four-dimensional Boolean cube

```text
p12826 = 0x4001 | a*0x0020 | b*0x0840 | c*0x0200 | d*0x8000.
```

No support of size at most three contained in the six ghost positions closes
the middle layer.  A direct `0xc279 -> 0x2c6d` one-cell exchange is impossible:
the other fixed cells in the triple already contain the unwanted top bit
`0x8000`.

For every one of the sixteen values, the only one-cell common providers for
the exposed pair lie at `p6437`.  Their values form the three-dimensional
cube

```text
p6437 = 0x0408 | e*0x0001 | f*0x0020 | g*0x0040.
```

All `16*8=128` literal pairs leave the invariant six-debt packet

```text
0x2879 0x287d 0xa879 0xa87d 0xc879 0xe879,
```

whose common core is `0x0879`.  The remaining seventeen editable cells must
re-host this packet simultaneously; the cube factorization is a front-end
normal form, not a completion.

## 3. Exact CNF

The complement of the nineteen positions covers 65,462 targets, leaving 73
repair targets.  The independently rebuilt interval atlas has 5,183 raw
terms and 5,131 retained exact physical witness terms over 71 editable
blocks.  Every repair target has a nonempty provider clause.

For the other seventeen cells, arbitrary nonzero values are reduced
feasibility-equisatisfiably to the 333-value target-intersection closure.
The two special cells are not passed through this common closure: doing so
would wrongly discard literal members of the surgery cubes.  Their domains
are encoded directly by 26 unit/equality clauses using the seven existing
cell-bit variables.  The final model has

```text
variables  6,267
clauses   91,512
literals 270,974.
```

The independent audit enumerates both special domains, replays the 16
two-hole states and all 128 six-debt states with exact occurrence deltas,
and reconstructs the complete DIMACS clause multiset.  No solver is used by
that audit.

## 4. Authentication

```text
scratch/k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731/model.cnf
  SHA256 11484aabf0f9da6e50c10f546f1a103a6076458c1b3c097e5e8d92541cf1398c

scratch/build_k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731.py
  SHA256 838dc18457418ba2f03c2587895e79775c0c7137f6f3408638b60d44ef559728

scratch/audit_k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731.py
  SHA256 f7cbef8ea7a252b7f102e4aabecaeb866258cb60d5236b83a0ba810f4654c996

scratch/k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731/independent.audit.json
  SHA256 9053654cc954a5ae7427dfedc28b25a7227fe365fd5970c769c1b2137f94687f
  payload 6c628ab3f6553121c124c533eebf8d640a77f6c673b129d4c30fb6a6321f53be

scratch/k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731/front_end.map.json
  SHA256 78f1bdf6d1cd464775642a311b5bdda2fb2f2847df686f068638f38e4224fdf4

scratch/k16_deletep1_collar594_c279_p12826_cube7_cnf_20260731/model.stats.json
  SHA256 07ebd85f0b0953328720b1184ffb9d52f450eb9aad7a6a104b567d449761be3b
```

The auto-validator is

```text
scratch/decode_verify_k16_deletep1_collar594_c279_p12826_cube7_sat_20260731.py
SHA256 1c49fb183b51a8f0249e78adad1dbae35ccae15fdfe9d4ce1c6449239f76ec9e.
```

It requires a complete satisfying assignment, rechecks every DIMACS clause,
materializes the physical word, and replays all 65,535 nonempty targets.

## 5. Solver protocol

The exact bundle is staged under H100 `/home`, never under the full
`/dev/shm` filesystem.  The authorized portfolio consists of exactly one
Kissat and one CaDiCaL process, each pinned to a genuinely free core at
nice 19, capped at 1,800 seconds and 8 GiB, with proof retention.  SAT is not
accepted without the validator above.  UNSAT is not promoted until its
retained proof passes an independent checker; timeout, signal, resource
failure, or incomplete proof remains UNKNOWN.

The older 18-cell endpoint-Hall CNF is frozen as propagation-only.  Its
interrupted CaDiCaL run is recorded as UNKNOWN with its partial proof
preserved; the 18-cell no-go comes solely from the solver-free immutable
ghost theorem.
