# Audit and hardening of Claude's composite-​`k=15` quotient pipeline

Date: 2026-07-29 (Asia/Almaty)

## 1. Verdict

The current Claude quotient search has a sound central mathematical core for
`k=15`: ranks 7 and 8 are free under cyclic rotation, the CP-SAT circuit model
uses one rank-seven colour per orbit, and its coprime-voltage constraint is the
right exact condition for one physical 6,435-cycle.  The live pipeline was not
safe as a reproducible constructor because it lost arc directions and voltage,
mixed incompatible selector catalogues, counted periodic target orbits as if
they all had size 15, required cyclic lower `q=3` at the wrong stage, and sent
an inadequately checked graph into the compiler.

The repo-owned hardening package is

- `scratch/claude_quotient_hardened_20260729/quotient_certificate.py`;
- `scratch/claude_quotient_hardened_20260729/migrate_legacy_selector.py`;
- `scratch/claude_quotient_hardened_20260729/guarded_compile.py`;
- `scratch/claude_quotient_hardened_20260729/test_hardened_pipeline.py`;
- `scratch/claude_quotient_hardened_20260729/RUNBOOK.md`; and
- `scratch/claude_quotient_hardened_20260729/UPSTREAM_PROVENANCE_20260729.json`.

It is self-contained for quotient mathematics, rejects bare or ambiguous IDs,
uses distinct physical rotations rather than nominal multiplicity, recomputes
the unit voltage, makes lower `q=3` diagnostic only, and proves the complete
physical carrier before any compiler import or SAT invocation.  The guarded
compiler then replays the certified cut and independently verifies the final
literal contiguous-OR word.

No `k=15` search, SAT run, exhaustive enumeration, or other heavy local job was
launched.  All executed regressions were small, solver-free `k=9/k=11` audits.

## 2. Upstream provenance is mutable, not a frozen run

`/Users/amir.nuriyev/Downloads/opusproblem/work` is not a Git repository and
changed while it was being audited.  `LEDGER.md` was first observed with
SHA-256

`427d0eaa1c2dd65a4afd8246c5bb26c57e834fc9622294acabcab274665d19c3`

and later, at 2026-07-29 00:33 local time, with

`e1ad3a0b82e353d8c656d896bc50d7b9e0b66c7b5c860feb7d857998c2388a4a`.

The current decisive source hashes at that snapshot were:

| artifact | SHA-256 |
|---|---|
| `cpsat.py` | `aa4e56dbf7b8773fff65f6432857ec8d5123434de8ea0f207b828de55df7aeaf` |
| `equi2.py` | `d939b89386a313ff306c659f18813c582e3f0cb822c731b44aab7f16776093ff` |
| `equi3.py` | `54c9dd30d14dacf9e0e41b374e69dbb64849068b2bcf2055acbb1d90dcd316bd` |
| `equi15.py` | `03394c2233ce77e2092f33cb8588ec4f4a7d1946cfd7243e0bc71a398f4f72fd` |
| `compile15.py` | `b288dc1d23898ee9a7bd4e18fd25d8ff8651cc130dd8c3ccc3ec9fa7e22bad8b` |
| `cutcompile.py` | `ae61b7a333a450a4dc13216349e0ab2ddbb2104e5685be3b698ce12816a58a13` |
| `gates.py` | `7d237cc60748e786b84f0235b07b5b2e7b658990f6ca3c69132073aea16f7b63` |
| `lib.py` | `a744bfcedd5786b73a6cbc54d62e9b056f188084a768fbcaf3459726b6b72845` |
| `carrier.cpp` | `b4fb6947b96670c9990a7823a5605af0806a24b9986e022e2521f73684e3495e` |
| `strictdfs.py` | `625e924041bff140cb469450116db8b128279bdcf770a16ec223ce1b7da13dff` |

The current `carrier` binary has SHA-256
`7a689d3767b6372857f72101759f371c187cd9419aa196e2411d3b28879b95a1`
and timestamp 00:06:47, whereas `carrier.cpp` has timestamp 00:10:02.  The
binary therefore cannot have been built from the current source.  The file
`k15_cegar.log` is empty (the SHA-256 of the empty string) and supplies no run
evidence.  The exact size, timestamp, and hash ledger is frozen in the
repo-owned upstream-provenance JSON.

Consequently, names such as `carrier`, `PASS.json`, or `latest` are not
provenance.  Future claims must be attached to hashes and to a persistent
remote run directory.

## 3. Exact mathematical audit

### Theorem 3.1 (unit-voltage lift)

Let a cyclic group of order `k` act freely on the selected middle vertices.
Let a directed quotient Hamilton cycle have `N` vertices and directed arc
phase increments `t_0,...,t_{N-1}`.  Put

`v = sum_i t_i (mod k)`.

Its physical lift has exactly `gcd(v,k)` directed cycles, each of length
`Nk/gcd(v,k)`.  In particular, it is one physical `Nk`-cycle if and only if
`gcd(v,k)=1`.

Proof.  Label a lifted state by `(i,s)`, where `i` is the quotient position and
`s` is its phase.  One quotient revolution maps `(0,s)` to `(0,s+v)`.  The
translation `s -> s+v` on `Z/kZ` has `gcd(v,k)` orbits, each of length
`k/gcd(v,k)`.  Expanding each quotient revolution by `N` gives the stated
cycle count and lengths.  This also proves both implications.  QED.

At `k=15`, both central ranks are free: rank 7 and rank 8 each consist of 429
orbits of size 15.  Thus the CP-SAT constraints in `cpsat.py:148-179` use the
correct theorem.  The model's explicit allowed voltages at `cpsat.py:173-179`
are sound.  The upper bound at line 174 should nevertheless be
`(K-1)*N`, not the unrelated hard-coded `14*2*len(choices)`.

The hardened verifier does not merely trust this quotient proof.  It expands
each selected directed edge orbit as a set, proves the full physical degree
and colour identities, walks the unique physical directed cycle, recomputes
`v`, requires `gcd(v,k)=1`, and checks that shifting by `N` positions equals
rotation by `v` at every physical position.

### Theorem 3.2 (actual equivariant multiplicities)

For an edge orbit `E` and a target orbit `Lbar`, the correct lower incidence
multiplicity is

`mu(E,Lbar) = |{e in E : intersection(e) in Lbar}| / |Lbar|`.

For a directed edge orbit and a middle orbit `Vbar`, the corresponding tail or
head coefficient is the number of directed tails or heads in `Vbar`, divided
by `|Vbar|`.  These quotients are integers because the group acts transitively
on each denominator orbit and equivariantly on the incidence relation.

Therefore neither an edge orbit nor a missing target orbit may be assigned
nominal multiplicity `k` without first proving it free.  Direct physical
expansion, as used in the hardened verifier, automatically implements these
coefficients and is safe even when target ranks are periodic.

The complete `k=15` orbit profile is:

| rank | orbit-size histogram |
|---:|---:|
| 1 | `1 x 15` |
| 2 | `7 x 15` |
| 3 | `1 x 5 + 30 x 15` |
| 4 | `91 x 15` |
| 5 | `1 x 3 + 200 x 15` |
| 6 | `2 x 5 + 333 x 15` |
| 7 | `429 x 15` |
| 8 | `429 x 15` |
| 9 | `2 x 5 + 333 x 15` |
| 10 | `1 x 3 + 200 x 15` |
| 11 | `91 x 15` |
| 12 | `1 x 5 + 30 x 15` |
| 13 | `7 x 15` |
| 14 | `1 x 15` |
| 15 | `1 x 1` |

In particular, lower `q=3` (rank 5), lower `q=2` (rank 6), and their upper
duals contain short orbits.  Boolean zero/nonzero coverage by canonical
representatives in the old code remains positive-sound, but an unweighted
missing count is not physical missing mass.  The hardened audit records
`orbit_size`, `stabilizer_size`, and weighted missing mass for every defect.

### Proposition 3.3 (scope of cyclic lower `q=3`)

For `k=15` the compiler depth is `D=3`.  The four-middle-window intersections
at lower `q=3` lie in the terminal rank-five erosion row assigned by the exact
linear lower compiler.  Hence cyclic lower `q=3` is a sufficient precondition
but is not a necessary carrier gate.  Residence, all upper masks, and cyclic
lower `q=2` remain required here; after a safe cut the literal compiler must
still cover every lower target, including rank five.

This proposition does not claim that a q3-defective carrier is already a word.
It only assigns the rank-five obligation to the exact compiler.  The final
guard checks literal coverage of every nonempty mask, so no q3 hole can escape
the proof boundary.

The old code violates this scope at `cpsat.py:467,475,483-484`,
`equi2.py:544,554,561-563`, `equi3.py:93,111-113`, and
`carrier.cpp:74-88`.  The hardened verifier reports q3 diagnostics but excludes
them from `cyclic_pass`.

## 4. Exact source and interface defects

### 4.1 Actual orbit size

- `cpsat.py:41-42` and `equi2.py:48-49` assert all low and middle orbits are
  free.  This happens to be true at the `k=15` central ranks but is not a
  general composite-dimension rule.
- `cpsat.py:249-276` and analogous walkers append exactly `K` rotations rather
  than deduplicating.  This is safe for the selected central edge orbits at
  `k=15`, but target defect ledgers at ranks 5, 6, 9, 10, and 12 need actual
  sizes.
- The hardened verifier constructs every orbit as a set of distinct rotations
  and emits the full all-rank profile.

### 4.2 Catalogue mismatch

- `equi2.py:95-100`, `equi3.py`, and `equi15.py:55-68` retain quotient
  self-loop choices.
- `cpsat.py:90-95` removes them.
- `cutcompile.py:57-61` always decodes integer IDs through the equi2 catalogue.
- `compile15.py:290-312` always decodes integer IDs through the CP-SAT
  no-self-loop catalogue.

The ordered catalogue sizes and hashes are:

| `k` | catalogue | entries | SHA-256 of compact `[[L,a,b],...]` |
|---:|---|---:|---|
| 9 | equi2 all | 140 | `1b78ed29576741103bb0dda3b64bcd11c722743e260ff99b29098f3019c2783c` |
| 9 | CP no loops | 135 | `fd0a5fc8b5ddaab9e01e8a2d6899e3f5018b7d5f3f7bae87c9888002d83d1f36` |
| 11 | equi2 all | 630 | `6f4f40e013f7ce690e165c98492d6d096a1543e4c949c857748bae646b8924aa` |
| 11 | CP no loops | 625 | `74ab216905b709645e33cfce2c435c54b3258e096c46b1f05e77698aea1fc652` |
| 15 | equi2 all | 12,012 | `883a657f2f08cf45c8ed3e692197c2a811a7dd3ecdb65e1dbf810a233e1b6dbe` |
| 15 | CP no loops | 11,998 | `8d09676a3c073c5bb688c6ea61d8561087f560ebcc1fac775b9a97d33b1cf08a` |

The first integer-ID divergence occurs at ID 3, 4, and 6 for `k=9,11,15`,
respectively.  Bare IDs are therefore not portable data.  The new v2 schema
requires an explicit canonical lower mask, `a<b`, and direction on every
choice.  If legacy IDs are retained for provenance, their catalogue kind,
entry count, digest, and exact ordered decoding must equal the explicit tuple
list.  Orphan or inconsistent legacy metadata is rejected before graph
construction.

### 4.3 Direction and voltage loss

- `cpsat.py:241-243` returns selected undirected choices but discards selected
  directed arcs and the solved voltage.
- `cpsat.py:471-478` writes only integer choice IDs.
- `equi3.py:61-62,98-105` similarly loses directions.
- `equi15.py:369` can overwrite a bare-ID selection before upper-gate success.
- `equi2.py:549-552` saves directions keyed by mutable integer IDs rather than
  binding them to explicit choice tuples.

The migrator hash-locks the raw selector and declared catalogue, proves its
entire undirected factor, chooses a deterministic orientation of the unique
cycle, and writes explicit per-choice directions.  The verifier derives and
records each directed quotient arc `(source_rep,target_rep,phase_shift)` and
independently recomputes the net coprime voltage.

### 4.4 Incomplete lower-q2 lazy template

`equi2.py:432-434` and `cpsat.py:361-363` discard `q2==p`.  These are legal
same-insertion triples.  This is not merely a hypothetical omission:

- for the final `k=9` factor, target orbit 37 has 9 valid occurrences but none
  of the 180 groups emitted by the old builder is satisfied;
- for the final `k=11` factor, target orbit 201 has 11 valid occurrences but
  none of the 420 emitted groups is satisfied.

Positive certificates remain sound because physical coverage is audited
directly.  An UNSAT conclusion from the old accumulated lazy model is not
complete even within its nominal equivariant/rainbow class.  The runbook
requires deleting that exclusion in a frozen source copy before future search.

### 4.5 Physical carrier was not validated before compilation

- `cutcompile.py:27-45` and `compile15.py:44-66` follow the first available
  neighbour without first proving degree two or uniqueness.
- `cutcompile.py:63` and `compile15.py:315-316` only assert the reconstructed
  length.
- They do not first prove the complete rank layer, unique edges, Johnson
  legality, physical degree, connectedness, q1 colours, directed incidence,
  or voltage.
- `gates.py:18-32` checks only a subset of residence/upper/permutation
  conditions and is not an adequate standalone carrier certificate.
- `compile15.py:342-343` stops after 40 gate-passing cuts; a negative result is
  not an all-cut theorem.
- `compile15.py:94-177` is an envelope-overcount precheck, not the exact SAT
  Hall theorem.

The new `export-path` refuses any carrier that fails its physical or required
cyclic gates.  Its output includes hashes of the certificate, physical cycle,
and exact middle path.  `verify-path` recomputes the path from the carrier and
cut and compares canonical JSON types, so altered masks, hashes, Boolean cuts,
or float/int substitutions fail.  `guarded_compile.py` calls this verification
before importing the compiler; it never invokes the unsafe selector decoder or
cycle walker in `compile15.py`.

The guard passes separate copies of an immutable certified middle tuple to
the historical Hall/compiler functions, protecting against input mutation.
It makes private hash-locked copies of the compiler and solver, rejects output
aliasing or overwrites, checks all protected inputs again after compilation,
requires the Hall ledger's target count to equal the independently recomputed
number of lower masks, and independently requires:

1. word length `W+D`;
2. every letter a nonzero genuine `k`-bit integer;
3. `D^D(word)` equal to the pristine certified middle path; and
4. every nonempty mask occur as a literal contiguous OR.

The word and audit are read back after individual atomic replacement.

## 5. Hardened certificate theorem

### Theorem 5.1

If `quotient_certificate.py verify` returns `PASS` on a v2 certificate, then
the certificate describes a literal directed Johnson cycle on exactly the
whole rank-`r` layer, uses every rank-`r-1` q1 colour exactly once, has one
incoming and outgoing selected edge at each physical vertex, has one physical
cycle, and its quotient voltage is coprime to `k`.  It also satisfies cyclic
residence, all upper trace coverage, and lower q2 coverage.  Every reported
orbit mass is its actual number of distinct rotations.

Proof.  `parse_choice` enforces canonical rank-`r-1` ownership and genuine
outside coordinates.  Each directed orbit is expanded as a set.  The verifier
then compares the vertex set with the exact combinatorial rank layer, checks
all symmetric differences have size two, all undirected edges are distinct,
all degrees are two, all directed indegrees/outdegrees are one, and the
intersection colour counter equals one copy of every rank-`r-1` mask.  Walking
the directed successor for exactly `W` steps proves one cycle.  The quotient
transversal, phase sum, physical shift identity, and gcd test prove the voltage
claim.  Residence and trace gates are recomputed from that physical cycle.
Orbit sizes are cardinalities of rotation sets, not nominal multipliers.  QED.

### Corollary 5.2

If `guarded_compile.py` returns `PASS`, its emitted word is a literal
contiguous-OR covering word whose depth derivative is exactly the certified
middle path.

Proof.  The guard first applies Theorem 5.1 and exact path replay.  After the
compiler returns, it checks the stated derivative equality and enumerates all
nonempty masks, marking only actual interval ORs of the emitted word.  Success
requires no missing mask.  Neither the SAT solver nor the historical compiler
is trusted for the final positive claim.  QED.

## 6. Exact `k=9/k=11` regressions

The hermetic command

```sh
python3 -m unittest -v scratch/claude_quotient_hardened_20260729/test_hardened_pipeline.py
```

passes 21 tests.  It performs no solver call and no search.

### `k=9` final factor

- legacy selection SHA-256:
  `81b11db074ee29ed0d9ea537d49ac01bde7f212b106bc3a6c7871a5d5be878ad`;
- 14 explicit choices and 126 physical vertices/edges;
- one directed 126-cycle;
- recomputed voltage `4 mod 9`, gcd 1;
- residence defects 0, upper holes 0, lower-q2 holes 0;
- 54 safe linear cuts;
- literal test word length 128 and SHA-256
  `0f282a2c5bb61c0ea48d49c5966eafba3ceb8a30cc40150a92764c1321c21b7c`.

The guarded-compiler test exports certified cut 29, supplies the exact literal
word through a fake non-solving compiler that deliberately mutates both input
lists, and still proves against the untouched certified tuple.  It also tests
output/input alias rejection.

### `k=11` final factor

- legacy selection SHA-256:
  `05832de6a2aa7191dc99dc7133b67b852539278a930cf717bb12ed9a301616e7`;
- 42 explicit choices and 462 physical vertices/edges;
- one directed 462-cycle;
- recomputed voltage `2 mod 11`, gcd 1;
- residence defects 0, upper holes 0, lower-q2 holes 0;
- 242 safe linear cuts;
- historical literal word length 465 and SHA-256
  `0dee7330a1c912f3b568dd0a669fbc823cf79e68b76f32ef37bb7afed6ebe77a`.

Cut indices depend on the chosen directed start/orientation; the invariant
regressions are the cycle/choice hashes, gate counts, and number of safe cuts.

### Exact lower-q3 skip control

Raw `cpsat_k11_rnd1.json` has SHA-256
`61b11e618650609d341cd4f4e4eaef51ea4ab1244a9e539396922e34092f3fa3`.
Under the CP no-self-loop catalogue it reconstructs as one 462-cycle with no
residence, upper, or lower-q2 defect.  Its lower-q3 diagnostic misses exactly
one orbit, representative 81, of physical mass 11.  The migrated deterministic
orientation has voltage 6 and gcd 1.  The hardened carrier correctly returns
`PASS` while retaining this q3 defect in its audit.

This is the direct regression proving that lower q3 is no longer silently
wired into carrier acceptance.

### Negative controls

The suite also proves rejection of:

- CP selector IDs decoded through the equi2 catalogue;
- catalogue metadata correctly rehashed but not matching explicit tuples;
- bare IDs and directionless tuples;
- direction and voltage tampering;
- duplicate JSON object keys;
- floats, strings, or Booleans masquerading as integers;
- orphan legacy metadata;
- `python -O`, which would otherwise erase assertions;
- altered exported middle paths and Boolean-valued cuts;
- invalid paths and wrong compiler hashes before compiler import;
- output/input aliases at compiler handoff; and
- changed or missing provenance artifacts.

As an independent wrong-catalogue control, decoding `cpsat_k11_rnd0.json`
through its correct CP table gives a connected degree-two graph on 462
vertices.  Decoding the same IDs through equi2 instead gives 418 vertices,
degree histogram `{1:143,2:154,3:33,4:66,5:22}`, and largest component 363.
All 42 tuples differ.  The hardened schema rejects this before any graph walk.

## 7. Exact proved/conditional boundary

Proved:

- the `k=15` central rotation actions used by the quotient model are free;
- coprime voltage is exactly the one-lifted-cycle criterion;
- the actual composite orbit profiles above;
- the old catalogue mismatch, q2-template omission, q3-scope error, and
  precompiler validation gaps;
- the k9/k11 positive carrier regressions and q3-skip regression;
- the fail-closed certificate, path, and guarded positive-word boundary.

Not proved or not reproduced:

- no passing `k=15` carrier or literal word was produced in this audit;
- no historical `k=15` solver run is reproducible from the live Downloads
  directory;
- no old UNSAT claim is complete while the same-insertion q2 templates are
  omitted;
- the frozen `compile15.py` deletes its temporary CNF and discards its solver
  model/stdout.  The guarded wrapper proves any positive word independently,
  but execution-level replay requires a further compiler-API patch that
  retains those artifacts;
- lower-q3 being nonbinding at carrier time does not remove its literal final
  obligation.

The exact future production procedure is the repo-owned runbook.  All heavy
`k=15` work belongs on the `h100` CPU; none was run locally here.
