# K16 delete-p1 collar `(5,9,4)`: target-closure normal form

## Frozen scope

The source is the length-12,873 word obtained by deleting zero-based position
`1`, whose value is `0x2800`, from the verified length-12,874 upper word:

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
SHA256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

Its sole missing target is `0x2c6d`.  Permit arbitrary nonzero replacements
only at

```text
[0,5) union [6435,6444) union [12869,12873),
```

and freeze the complement.  This is an 18-cell fibre, not the set of all
length-12,873 words.

## Normal-form theorem

The frozen runs witness 65,474 targets and leave a residual set `R` of 61.
For a nonzero editable value `v`, define

```text
N(v) = intersection {t in R : v subset t}
```

when the displayed family is nonempty.  If it is empty, `v` belongs to no
residual witness and is redirected to the live sentinel `N(1)=1`.

For every residual witness target `t` containing `v`,

```text
v subset N(v) subset t.
```

Thus normalizing all editable cells preserves the exact OR of every chosen
residual interval: added bits already occurred somewhere in that interval,
and no bit outside `t` is introduced.  Dead values occur in no residual
witness.  The remaining 65,474 targets retain fixed-run witnesses.  Hence
the unrestricted 18-cell fibre is equisatisfiable with the nonzero fixed
points of `N`.

## Exhaustive audit

The independent audit gives:

```text
10,015 live nonzero masks
55,520 dead nonzero masks
30,525 live value-target containments checked
245 nonzero closure-fixed masks
```

Direct scanning of all 65,536 masks and independent closure of the 61 targets
under pairwise bitwise intersection produce the same fixed-point family.
The 257 emitted domain clauses per cell have exactly those 245 models under
an exhaustive 16-bit truth table.

The interval decomposition is also reconstructed independently: 491 fixed
bases produce 4,270 dominated-minimal terms on 70 active blocks.  The 52
non-singleton terms for the single-bit target `0x8000` are redundant because
nonzero cells in such an interval must each equal `0x8000`; 4,218 terms
remain.  An independent Python reconstruction matches the complete DIMACS
clause multiset exactly.

## Strengthened CNF

```text
5,338 variables
76,653 clauses
226,792 literals
832 interval-OR variables
4,218 deterministic witness variables
```

The normalization preserves feasibility, not exact Hamming distance from the
incumbent.  It is therefore valid for this unbounded fibre but cannot be
inserted into an exact-change-count face without a separate argument.

## Solver disposition

Exactly one strengthened-form solver was run on H100 CPU core 28:

```text
Kissat 4.0.4, seed 16703
nice 19
1,800-second wall cap
8 GiB address-space cap
```

It reached the cap with exit `124` after `30:00.01` wall time and 1,346.97
user seconds.  Peak RSS was 115,992 KiB.  It emitted no SAT model and no
UNSAT conclusion.  The exact disposition is therefore `UNKNOWN`.

The 2,251,292,672-byte DRAT stream was interrupted with the solver.  Its hash
is retained only for run identity; it is incomplete, was not passed to
`drat-trim`, and is not a certificate or mathematical evidence.  No SAT or
UNSAT claim follows from this run.

## Artifacts

```text
scratch/k16_upper12874_delete_p1_collar_5_9_4.positions.txt
  SHA256 5cd610ff6fd904cbca92e74217f942e43ed7caa4136aa73c2c6a0c8db2931032
scratch/k16_append0200_collar473_closure_strengthened_cnf_20260730.cpp
  SHA256 1a98c4a85145d6dd7dee3647b575cf5d6fb92dc6160c2ec71425ee1f4ddee29c
scratch/audit_k16_upper12874_delete_p1_collar594_closure_cnf_20260730.py
  SHA256 24e326c84057d067c663f9278aa8437a9e5da61864fce027ea449b31fcdec5a5
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/audit.json
  SHA256 efc2096c1e8994228c096581de21f5fcf5dadc2cc0dcc4d9c42bd6c92f71988f
  payload 6459146484d1494413a8aeed6a69796f5fafe3a518f90bbed89b97c8228ce05e
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/model.cnf
  SHA256 cc73d7bf680d2698fd05f34bee74e1eb10427c95d2323013b4f8d5e387b948f2
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/model.map
  SHA256 b557c13272198a2338ce1f0718c24a0a1692cd8c8e3b40b2071a125402b3c55a
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/model.stats.json
  SHA256 d9a456532881d51e58ce481ae0bfc8ffda23990f29490f126d6c55c06bdbd72b
scratch/decode_verify_k16_deletep1_collar594_closure_sat_20260730.py
  SHA256 586ad17240b32a19573d04fe160ed6aab95a4efff6bfab62ce6eaf58ffcfdd8e
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/solve.stdout
  SHA256 6093b8cc46b6988bafb4710d3363307cca33a18ea45f503ef806bc993adeb303
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/solve.stderr
  SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/solve.resource
  SHA256 97f19a91762025d2c8af36274ed0f746bdb347aa9c482a113be107ab53d7e40a
scratch/k16_upper12874_delete_p1_collar594_closure_normalform_20260730/solve.exit
  SHA256 ca2ebdf97d7469496b1f4b78958f9dc8447efdcb623953fee7b6996b762f6fff
remote retained partial model.drat.bin (2,251,292,672 bytes)
  SHA256 767b8fdbbfaf0825a2a5c39162db1493b4ac6c8c4feeb8bc757e43ccee31dc56
H100 /home/amodo/or15/kissat/build/kissat, version 4.0.4
  SHA256 3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d
```

The complete remote run remains under
`/home/amodo/or15/work/k16_deletep1_collar594_closurelane_20260730`.
