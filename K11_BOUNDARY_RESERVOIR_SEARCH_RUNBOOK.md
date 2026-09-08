# Build and run: compressed `k=11` boundary-reservoir search

## Files

* `k11_boundary_reservoir_search.cpp` — row evaluator, exact twelve-cell
  reservoir solver, constructor, internal dual coverage check, and an explicit
  regression of the counting no-go theorem.
* `k11_boundary_reservoir_verify.cpp` — independent certificate parser,
  reconstruction check, all `108345` intervals, and distinct-suffix-OR check.
* `K11_BOUNDARY_RESERVOIR_SEARCH_DESIGN.md` — mathematical specification.

The intended `sigma=369` branch is now proved impossible: `1011` distinct
bulk cores would leave only twelve lower masks, but any such pair/triple-core
family must leave at least 66.  The implementation is frozen as a verifier and
regression harness.  Its heavy `--search` command refuses to launch.  This
no-go result does not exclude unrestricted length `465`.

## Local build-only regression

No long search is needed on the Mac.  The allowed tiny regression is:

```bash
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic \
  k11_boundary_reservoir_search.cpp -o /tmp/k11_boundary_reservoir_search
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic \
  k11_boundary_reservoir_verify.cpp -o /tmp/k11_boundary_reservoir_verify
/tmp/k11_boundary_reservoir_search --self-test
```

Expected output:

```text
PASS geometry=1392 core=1011 reservoir=12 no-go=438>330 run-rule local-pins suffix-OR
```

A useful read-only seed check is:

```bash
/tmp/k11_boundary_reservoir_search --check k11_lower956_upper530.txt
```

## Remote optimized build

No remote search is warranted.  If an independent remote build regression is
desired after copying the two sources into a remote directory, run only:

```bash
mkdir -p /root/k11_boundary_reservoir
cd /root/k11_boundary_reservoir
g++ -std=c++20 -O3 -march=native -flto -fopenmp -DNDEBUG \
  -Wall -Wextra -Wpedantic \
  k11_boundary_reservoir_search.cpp -o k11_boundary_reservoir_search
g++ -std=c++20 -O3 -march=native -flto -DNDEBUG \
  -Wall -Wextra -Wpedantic \
  k11_boundary_reservoir_verify.cpp -o k11_boundary_reservoir_verify
./k11_boundary_reservoir_search --self-test
sha256sum k11_boundary_reservoir_search k11_boundary_reservoir_verify
```

## Why no portfolio should be launched

If `q` lower masks are omitted, at least `462-q` of the `461` adjacent-pair
cores must be rank five.  Hence at most `q-1` pair cores have lower rank.  Of
the `460` triple cores, at least

```text
460 - 2(q-1) = 462 - 2q
```

are then distinct rank-four masks.  Since only `C(11,4)=330` rank-four masks
exist, `q>=66`.  The proposed rainbow bulk has `q=1023-1011=12` and would
force `438>330` distinct rank-four triples.

As a safety guard, any `--search` invocation exits with code 3 before reading
a seed or starting a worker.

## Exact fixed-row commands

Evaluate a row:

```bash
./k11_boundary_reservoir_search --check candidate.row
```

Attempt the exact twelve-cell assignment and write a certificate (retained as
an audit interface, although the no-go theorem proves no row can reach it):

```bash
./k11_boundary_reservoir_search --solve candidate.row candidate.cert
```

Independently verify a produced certificate:

```bash
./k11_boundary_reservoir_verify candidate.cert
```

The required final verifier line is:

```text
PASS k=11 nonzero_length=465 row=462 bulk=1011 reservoir=12 covered=2047/2047 intervals=108345
```

Were such a certificate ever produced, prepending a literal zero to its 465
array entries would give the original all-mask answer of length 466.  Under
the audited no-go theorem, production of one would instead signal an
implementation or theorem error and must be investigated before any claim.
