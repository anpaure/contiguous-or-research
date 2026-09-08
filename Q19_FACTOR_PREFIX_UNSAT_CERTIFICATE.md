# Certified UNSAT result for the `k=11`, `q19_factor_prefix` branch

## Verdict and exact scope

The exact all-target SAT formula obtained with

```text
K11_FOREST_ADJACENT_SHADOWS=1
K11_FOREST_RANK3_SHADOWS=1
K11_FOREST_CONTAINMENT_CAPS=1
K11_FOREST_PORTAL_BRANCH=q19_factor_prefix
```

is **UNSAT**.  This was certified by a stock CaDiCaL binary-LRAT trace and
two separate successful standalone `lrat-trim` runs, including strict-chain
mode.

This conclusion is deliberately branch-specific.  It rules out the one
fixed 22-entry `q=19` factor prefix encoded by `q19_factor_prefix`; it does
not rule out the weaker `q19_fixed_row` branch, another mixed-delay prefix,
or an unrestricted 465-entry array.  In particular, it does **not** prove
`nu(11) > 465`.

The logical encoding and this scope were independently audited in
`K11_PORTAL_BRANCH_IMPLEMENTATION_AUDIT.md`.  In this mode the formula has
2,882,282 variables and 14,460,196 clauses; the portal restriction itself
adds 704 unit clauses and allocates no variable.

## Exact unsimplified formula

The first proof attempt used `CaDiCaL::Solver::write_dimacs`, which emitted a
root-simplified 12,265,047-clause formula.  That file is not the initial
14,460,196-clause stream used by the original solver run, so it was rejected
as proof-certificate input.

For a clean reconstruction, the frozen proof source was copied to
`scratch/k11_forest_sat_proof_raw.cpp` and changed only to:

1. mirror every literal passed by `add` and `add_vector` to a raw DIMACS
   stream before CaDiCaL can simplify it;
2. expose optional proof-format and internal-check switches.

The complete instrumentation diff is
`scratch/k11_forest_sat_proof_raw.patch`.  It does not add, remove, reorder,
or change a SAT clause.

Two independent build-only runs emitted byte-identical files:

```text
p cnf 2882282 00000000000014460196
```

The file has exactly 14,460,197 lines including the header.  Its SHA-256 is

```text
17b6cc9c4780340bbc9cfce549e381b03e0945d775775f881bf8d9d78de6e464
  q19_factor_prefix_original.cnf
```

The reproducible second full copy was removed after `cmp` returned zero; its
build log was retained.

## Proof generation

Generating LRAT through the custom `solver.add()` API is not suitable here:
derived clauses can be introduced before all original clauses are known, so
their identifiers are not those of a standard final-CNF LRAT proof.  The
invalid API trace was discarded.

Instead, the stock CaDiCaL CLI parsed the exact raw DIMACS.  Its parser calls
`reserve_ids(14460196)` before adding clauses, which gives the standard LRAT
identifier convention.  The command was

```bash
/root/cadical/build/cadical \
  --lrat=true --seed=1901 \
  q19_factor_prefix_original.cnf \
  q19_factor_prefix_cli.lrat
```

CaDiCaL reported `s UNSATISFIABLE` and exited with status 20.  The run took
409.50 seconds real time and at most 3563.79 MB RSS.  The exact solver was
CaDiCaL 3.0.0 at commit
`7b99c07f0bcab5824a5a3ce62c7066554017f641`.

The binary proof has 378,785,357 bytes and SHA-256

```text
5c8d4d16ac78e6a0d2cb6d1a9bc94904bc8072bc7dd7569833d53b9b30a8ab94
  q19_factor_prefix_cli.lrat
```

## Independent proof checks

The checker was `lrat-trim` 0.2.1-dev from the same CaDiCaL source tree,
compiled independently as a standalone executable.  Source and executable
hashes are

```text
1f2cfe4e2bd33f83933fa85ce7548cab69838d865983e1382660ea8c0b4f4330
  lrat-trim.c
19807513afb0e1faf1544890df19a8b9a59628922f0721c79e11573d14ccde2e
  lrat-trim
```

The ordinary forward/eager check was

```bash
./lrat-trim --no-trim \
  q19_factor_prefix_original.cnf \
  q19_factor_prefix_cli.lrat
```

It returned

```text
s VERIFIED
c checked 3235021 clauses 645643 per second
c resolved 51751384 clauses 16.00 per checked clause
c assigned 82673138 literals 25.56 per checked clause
c maximum memory usage of 1429 MB
c total time of 5.01 seconds
EXIT:20
```

The stricter rerun was

```bash
./lrat-trim --strict --no-trim \
  q19_factor_prefix_original.cnf \
  q19_factor_prefix_cli.lrat
```

and independently returned

```text
s VERIFIED
c checked 3235021 clauses 673319 per second
c resolved 48516363 clauses 15.00 per checked clause
c marked 0 literals 0.00 per checked clause
c maximum memory usage of 1429 MB
c total time of 4.80 seconds
EXIT:20
```

Thus the UNSAT result no longer rests on a solver status line, a mismatched
simplified formula, or an unchecked DRAT trace.

## Artifact hashes

The large artifacts remain on the rose pod under `/root/portal_branch`.
Compressed copies were tested with `zstd -t`; decompression reproduces the
raw hashes above.

The two small checker logs were copied into
`scratch/certificates/q19_factor_prefix_unsat/`.  The solver and
formula-reproduction logs remain on the rose pod and are identified by hash
below.

```text
c186bf2a804704ffe7e2f7b2af2eec0cfea935d9482b986fd7f6832662cb255e
  q19_factor_prefix_cli.lrat.zst
e31d15a4378ba90a08c135bfe28754595257ef68534408f682109a7c287611b8
  q19_factor_prefix_original.cnf.zst
c0c54358d38fb307e008ce5ff089a1d8f80f62ba2500f270ea8456a1411895b5
  q19_factor_prefix_cli_lrat_check.log
1a5a3960b2619d145f9375bc691ddc780f08363d788aa27de4dda1354cbbda21
  q19_factor_prefix_cli_lrat_check_strict.log
2e6ee106202cff2b47f2ab9cb193b471e1da65655426b0da0e2f854216cced6c
  q19_factor_prefix_cli_lrat_solve.log
8d4e0a942e97b817f7942e98d0e26766cdd9e0e15ec56ea250181f466225ec04
  q19_factor_prefix_original_build.log
58239a026e7bb99a7bf3697c9593d01e97ca2894fe835037aff23a8f8f38aa0e
  q19_factor_prefix_original_rebuild.log
```

Local provenance files:

```text
d513ff6218879b3bd0786c08c4b200e85c731a0170f904acae39149db46e4ec1
  scratch/k11_forest_sat_proof_frozen.cpp
650b8b42d06cd3b7621fafd9dc33e304d0047bd673d38cc2dc6b6eef85bf4947
  scratch/k11_forest_sat_proof_raw.cpp
22214388695626a4c06f1a3b4a129742fa456b7b769c6200a9cc31f854e05d4f
  scratch/k11_forest_sat_proof_raw.patch
```

## Superseded DRAT attempt

For completeness, the earlier binary DRAT file was not used in this
certificate.  It was initially paired with the simplified DIMACS, and its
tail becomes malformed after byte 359,256,064.  Although a valid-looking
empty-clause addition occurs earlier, at byte 358,117,377, neither fact is
needed now: the fresh stock-CLI LRAT proof above starts from the exact
unsimplified formula and passes two independent checks.
