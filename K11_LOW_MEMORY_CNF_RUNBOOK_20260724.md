# Low-memory exact-CNF deployment for the `k=11,n=465` onion split

## Scope

The current integrated executable builds roughly 20.2 million clauses inside
CaDiCaL and simultaneously retains the structural plan clause banks.  Its
observed high-water mark is about 5.14 GiB per process.  The Rose container is
limited to 32,000,000,000 bytes with no swap, so simultaneous formula builds
caused the recorded exit-137 OOM kills.

The safest immediate change is to generate each exhaustive branch CNF once,
hash it, and reuse that immutable CNF for every search seed and for the final
proof-producing run.  This does not weaken or split the formula.

The authoritative source already supports

```text
K11_FOREST_DIMACS=PATH
K11_FOREST_BUILD_ONLY=1
```

but its real-CaDiCaL build still constructs the complete in-memory solver.
The shim

```text
scratch/cadical_dimacs_stream_stub/cadical.hpp
```

implements the same generator-facing API and streams every `solver.add()`
literal verbatim to DIMACS.  It patches a fixed-width header in
`write_dimacs()`.  It performs no simplification and must only be used with
`K11_FOREST_BUILD_ONLY=1`.

This changes the storage mechanism, not the clauses.  A proof checked against
the resulting CNF certifies exactly that raw generated formula.

For the first archival CNF, the zero-code-risk fallback is to run the existing
audited binary once, sequentially, with the two variables above.  It retains
the measured 5.14 GiB generation peak but immediately enables all later seeds
to reuse the resulting CNF.  The streaming shim should be promoted only after
one branch's header/inventory is checked and, ideally, a smaller configuration
is compared clause-for-clause with the existing hook.  The shim's output need
not be byte-identical to CaDiCaL's normalized dump; its claim is that it is the
verbatim raw clause stream accepted by CaDiCaL.

## 1. Compile on RunPod

From a directory containing the audited source of hash

```text
2ab8ce03f844884c1dc6c5b4f742fe6e447680589172610fcd9649906ebdc26c
```

copy the shim and compile without linking CaDiCaL:

```bash
set -euo pipefail
sha256sum k11_forest_sat_newcuts.cpp
g++ -O3 -std=c++20 \
  -I/root/problem/scratch/cadical_dimacs_stream_stub \
  k11_forest_sat_newcuts.cpp -o k11_forest_dimacs_stream
sha256sum k11_forest_dimacs_stream
```

Adjust only the shim include directory to its actual copied location.  Do not
put a large DIMACS in `/dev/shm`: tmpfs pages count against the same 32 GB
cgroup.  First locate and verify a persistent-volume path:

```bash
findmnt -T /workspace || true
findmnt -T /runpod-volume || true
df -h /root /workspace /runpod-volume 2>/dev/null || true
```

Generate one branch at a time, and do not start a generator until

```text
current cgroup usage + 5.2 GiB observed HWM + 5 GiB safety < 32,000,000,000.
```

The streaming build should be substantially smaller, but its first remote
run must still be measured with `/usr/bin/time -v` before changing the
portfolio concurrency.

## 2. Common exact environment

The common exhaustive guards are

```bash
COMMON=(
  K11_FOREST_ADJACENT_SHADOWS=1
  K11_FOREST_RANK3_SHADOWS=1
  K11_FOREST_BAND_CUTS=1
  K11_FOREST_JOINT_BAND_CUTS=1
  K11_FOREST_ENDPOINT_ALIGNMENT_CUTS=1
  K11_FOREST_CANONICAL_RANK6_ENTRY=1
  K11_FOREST_SINGLETON_POOL_CUT=1
  K11_FOREST_RANK6_BOUNDARY_ENTRY=1
  K11_FOREST_LOCAL_DENSITY_PB=1
  K11_FOREST_CONTAINMENT_CAPS=1
  K11_FOREST_SUBCUBE_DEFICIENCY=1
  K11_FOREST_NAMED_CELL_HALL=1
  K11_FOREST_RESIDUAL_COORD_LEX=1
  K11_FOREST_RANK7_TRUNCATED_WIDTH=1
  K11_FOREST_BUILD_ONLY=1
)
```

Type I adds

```bash
TYPE1=(
  K11_FOREST_RANK6_BRANCH=1
  K11_FOREST_RANK_FILTRATION_TYPE1=1
  K11_FOREST_TYPE1_PREFIX_CHAIN=1
  K11_FOREST_TYPE1_FACET_PIN_LOAD=1
  K11_FOREST_TYPE1_RIDGE_PIN_LOAD=1
  K11_FOREST_TYPE1_GLOBAL_PAIR_PROFILE=1
)
```

and Type II adds

```bash
TYPE2=(
  K11_FOREST_RANK6_BRANCH=0
  K11_FOREST_RANK_FILTRATION_TYPE2=1
  K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1
  K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1
  K11_FOREST_TYPE2_COMPANION_PIN_LOAD=1
)
```

## 3. Generate and audit one immutable CNF per branch

After setting `CNF_ROOT` to the verified persistent volume:

```bash
set -euo pipefail
mkdir -p "$CNF_ROOT"
INPUT=/root/k11_onion_20260723/k11_upper549_natural_array.txt
GEN=./k11_forest_dimacs_stream

env "${COMMON[@]}" "${TYPE1[@]}" \
  K11_FOREST_DIMACS="$CNF_ROOT/k11_type1.cnf" \
  /usr/bin/time -v taskset -c 0 "$GEN" "$INPUT" /dev/null 1 \
  >"$CNF_ROOT/k11_type1.build.stdout" \
  2>"$CNF_ROOT/k11_type1.build.log"

env "${COMMON[@]}" "${TYPE2[@]}" \
  K11_FOREST_DIMACS="$CNF_ROOT/k11_type2.cnf" \
  /usr/bin/time -v taskset -c 0 "$GEN" "$INPUT" /dev/null 1 \
  >"$CNF_ROOT/k11_type2.build.stdout" \
  2>"$CNF_ROOT/k11_type2.build.log"
```

Generate the branches sequentially.  Their audited raw inventories must be

```text
Type I:  3,671,659 variables; 20,175,646 clauses.
Type II: 3,686,611 variables; 20,247,467 clauses.
```

Check both the source log and a token-level DIMACS scan:

```bash
for f in "$CNF_ROOT"/k11_type{1,2}.cnf; do
  head -n 1 "$f"
  awk 'NR==1{v=$3;c=$4;next}
       {for(i=1;i<=NF;i++){if($i==0)z++;else{x=$i<0?-$i:$i;if(x>mx)mx=x}}}
       END{print FILENAME,"maxvar="mx,"clauses="z,
                 "header_vars="v,"header_clauses="c;
           exit !(mx<=v && z==c)}' "$f"
  sha256sum "$f"
done | tee "$CNF_ROOT/cnf_inventory_and_hashes.txt"
```

The SAT seed is not part of either CNF: the source uses the third positional
argument only in `solver.set("seed",sat_seed)`.  Every search seed can
therefore reuse the same branch file byte for byte.

## 4. External search portfolio

Benchmark one parser/solver process first and record its maximum RSS.  Only
then choose concurrency from the cgroup limit:

```bash
set +e
/usr/bin/time -v taskset -c 20 /root/kissat/build/kissat --seed=411 \
  "$CNF_ROOT/k11_type2.cnf" \
  >"$CNF_ROOT/type2_seed411.kissat.log" 2>&1
rc=$?
set -e
echo "KISSAT_EXIT=$rc" >>"$CNF_ROOT/type2_seed411.kissat.log"
```

For `rc=10`, decode variables `1,...,5115` (`465*11` array-bit variables)
and independently verify the resulting 465-entry word with both exact OR
verifiers.  For `rc=20`, the no-proof result is only a trigger for the
proof-producing run below.

Reusing DIMACS removes the generator and its plan banks from every search
process.  It also removes the simultaneous formula-construction spike that
caused the OOM kills.  It does not guarantee a particular solver RSS; the
first external run remains the authoritative measurement.

## 5. Proof-producing run

Use the already established Kissat/DRAT workflow, one exhaustive branch at a
time:

```bash
set +e
/usr/bin/time -v taskset -c 20 /root/kissat/build/kissat --seed=411 \
  "$CNF_ROOT/k11_type2.cnf" "$CNF_ROOT/k11_type2.drat" \
  >"$CNF_ROOT/k11_type2.proof.log" 2>&1
rc=$?
set -e
echo "KISSAT_EXIT=$rc" >>"$CNF_ROOT/k11_type2.proof.log"
```

Only exit 20 followed by an independent successful proof check is evidence:

```bash
set +e
/root/drat-trim/drat-trim \
  "$CNF_ROOT/k11_type2.cnf" "$CNF_ROOT/k11_type2.drat" \
  >"$CNF_ROOT/k11_type2.drat-trim.log" 2>&1
rc=$?
set -e
echo "DRAT_TRIM_EXIT=$rc" >>"$CNF_ROOT/k11_type2.drat-trim.log"
test "$rc" -eq 0
grep -F 's VERIFIED' "$CNF_ROOT/k11_type2.drat-trim.log"
sha256sum "$CNF_ROOT/k11_type2.cnf" "$CNF_ROOT/k11_type2.drat" \
  "$CNF_ROOT/k11_type2.drat-trim.log"
```

Repeat independently for Type I.  Both checked branch refutations are needed
to improve the lower bound.  Raw proofs can be far larger than the CNF; check
volume capacity before launch.  If a FIFO-to-`zstd` proof stream is used, it
must first be tested on a small known-UNSAT formula, and the decompressed FIFO
must subsequently be accepted by `drat-trim` with exit zero.  Do not improvise
proof compression during the only archival run.

## 6. Expected memory effect

The current process combines:

1. all structural plan clause banks;
2. the 20-million-clause CaDiCaL database;
3. solver preprocessing/search state.

The streaming generator removes item 2 completely during CNF creation.  Its
largest explicitly reserved bank is the 20,000,000-integer subcube buffer,
about 80 MB, plus the remaining plan vectors.  A sub-gigabyte generation peak
is a reasonable expectation but is **not** asserted until measured remotely.

An external solver then holds item 2/3 but none of the C++ plan banks.  The
saving is expected to be hundreds of MB rather than multiple GiB; its larger
operational benefit is that CNF construction occurs once instead of once per
seed.  Concurrency must still be set from observed external-solver HWM, not
from host-level `free`.

## 7. RunPod validation on 2026-07-24

The shim was copied to Rose and compiled against frozen source hash
`2ab8ce03...c26c` using the host compiler's `-std=c++2a` spelling.  Full
build-only streams to `/dev/null` succeeded under a 3 GiB virtual-memory cap:

| branch | variables | clauses | measured peak RSS |
|---|---:|---:|---:|
| Type I | 3,671,659 | 20,175,646 | 148,472 KiB |
| Type II | 3,686,611 | 20,247,467 | 152,220 KiB |

Both exact CNFs were then written to the Rose overlay and scanned token by
token.  Header counts, maximum variables, clause terminators, and source-log
inventories agree exactly:

```text
79bb1c579bd44e274cf499adcbcb1aef83cf237c0aaac88002dbda09a99cd69e  k11_type1.cnf
508f389e2ad3fff49984a2117a060437fcf3446ccdc96b8b30ac6e69eb039c15  k11_type2.cnf
```

Their sizes are approximately 572 MiB and 574 MiB.  This validates the
streaming path for these exact branch formulas and reduces generation memory
by more than an order of magnitude.  It does not validate any external
solver result; SAT still needs two OR verifiers and UNSAT still needs a
checked proof.

One external Kissat Type-II seed was subsequently started against the frozen
Type-II CNF with a hard 4 GiB virtual-memory limit.  Initial resident memory
was about 1.5--1.8 GiB, far below the integrated process, but concurrency must
continue to use its eventual observed high-water mark.
