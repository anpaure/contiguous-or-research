# Thread D: executable phase-free compiler CEGAR for the joint two-rail class

Date: 2026-07-30

Status: exact model and exact separation theorem implemented; `K=8` and the
new global `K=10` carrier pass; the new `K=10` carrier compiles to an
independently verified optimal 254-letter word.  The retained `K=16` runs
are **UNKNOWN**: two CP-SAT launches stopped on memory before producing an
incumbent, and one lean Kissat launch stopped after 300 seconds before
producing an incumbent.  Neither result is UNSAT evidence.

## 1. Result and scope

Let `K=2R`, `n=K-1`, and let rotation act on the first `n` coordinates while
fixing the top coordinate.  The executable searches the complete
phase-free quotient-option atlas for the following normalized class:

1. one ordered A-shore block and one ordered B-shore block;
2. exactly one `A -> B` and one `B -> A` crossing;
3. unit total voltage modulo `n`;
4. exact middle ownership after physical lifting;
5. positive residence at least `d+1`, where `d` is the compiler depth;
6. both lower and upper q1 palettes complete;
7. lower q2 and q3 complete; and
8. every strict upper target covered by an interval of arbitrary width.

The master is **global and source-independent**.  It has no source carrier,
edit-radius, Hamming-distance, or fixed selected-option constraint.  At
`K=16` it selects from all 54,856 eligible quotient options on all 858
owners.  Consequently the source-relative `Exact66` infeasibility does not
cut this model and gives no negative information about it.  A satisfying
carrier here must be a genuinely new global selection, not a local repair
of the 93-hole source.

The scope remains the one-block-per-shore, unit-voltage equivariant class.
The report does not claim that every possible `K=16` carrier has this normal
form.

## 2. Exact base encoding

For each eligible quotient transition option `a`, let `x_a` be its selection
literal.  The CP model in

```text
scratch/threadD_solve_even_two_rail_compiler_cegar_20260730.py
SHA-256 4540852168012658dac2bbcffd5f774e7035c1d016098599cc4657f622b3ac61
```

uses the following constraints.

### 2.1 Ownership and block topology

Every quotient owner has exactly one selected outgoing and incoming option.
Exactly one selected option crosses in each direction.  For each owner `u`,
compact integer variables record its selected successor, voltage increment,
deleted coordinate, inserted coordinate, and whether its outgoing option is
a crossing.

The block order uses one position in `{0,...,M-1}` per owner and one
successor-position `Element` row per owner.  A same-shore successor increases
position by one; a crossing must leave position `M-1` and enter position
zero.  Hence each shore is one Hamilton path and the two crossings join the
paths into one quotient circuit.  This replaces option-pair order
auxiliaries by `O(N)` integers and is exact, not a subtour relaxation.

The voltage constraint is

\[
       \sum_u \delta(u)=1+n z
\]

for an integer `z`.  A quotient circuit with unit voltage lifts to one
physical middle Hamilton cycle of length `W=Nn`.

### 2.2 Residence and q1

For each owner, the last `d` insertion labels are transported through the
selected successor and voltage by exact `Element` and allowed-assignment
rows.  Every deletion is forbidden from these `d` labels.  This is exactly
the positive-run lower bound `d+1` in the scoped transition atlas.

The four q1 palettes are orbit-compressed but literal-exact.  At `K=16`
their sizes are

```text
rank(R+1)       335
rank(R-1)       429
top+rank(R)     429
top+rank(R-2)   335
total          1528
```

and one positive provider row is installed for every one of these 1,528
orbit colours.

### 2.3 Optional eager lower controller

For `q <= d`, residence implies that the next `q` deletion labels are
distinct coordinates of the starting middle state.  Transporting future
deletions back to the starting frame therefore gives exactly

\[
   T_u\cap T_{s(u)}\cap\cdots\cap T_{s^q(u)}
      =T_u\setminus\{f_1(u),\ldots,f_q(u)\}.
\]

Thus lower q2/q3 may be imposed eagerly by label tables and witness-owner
`Element` rows.  At `K=16`, adding both depths has the exact semantic cost
5,976 variables and 5,976 constraints.  The retained low-memory `K=16` CP
attempt deliberately omitted these eager rows and used exact lazy
separation instead; this changes performance, not the accepted carrier
class.

## 3. Exact deep-shadow separation

The lower and upper separators are

```text
scratch/threadD_lower_fixed_depth_labelled_boundary_20260730.py
SHA-256 a705f62dc3bb92f404f51e6bb998ee672e8da08e2702e29dc906e043d09b7c92

scratch/threadD_upper_accumulated_union_separator_20260730.py
SHA-256 6130ed3c6380c4a62dc82547a05d2513adf4d03f57de21abdb67603ff035940f
```

### Theorem 3.1 (exact labelled-frontier row)

Fix a target automaton whose transition labels are quotient option IDs.  For
an incumbent selected set `X`, let `Reach_X` be the closure of all starts
under selected transitions.  If no accepting state is reachable, let

\[
 B_X=\{a:\text{ some transition labelled }a
               \text{ leaves }Reach_X\}.
\]

Then

\[
                  \bigvee_{a\in B_X}x_a                         \tag{3.1}
\]

is valid for every future carrier covering the target and is violated by
the incumbent.  Repeated physical copies with the same quotient option are
deduplicated.  If `B_X` is empty, the target is unreachable in the complete
option atlas.

Proof.  Any accepting path starts in `Reach_X` and ends outside it, so its
first exit has a selected label in `B_X`.  Conversely, an incumbent-selected
exit label would activate the particular physical copy leaving a reachable
state, contradicting closure.  QED.

For a lower target `L` at depth `q`, the automaton state records the current
middle state and running intersection for exactly `q` transitions; it
accepts iff the intersection is `L`.  This is the literal consecutive
`(q+1)`-state definition and requires no residence assumption.

For an upper target `U`, the automaton state records the current middle state
and accumulated union.  All middle states contained in `U` are starts, and
the automaton accepts exactly when the union reaches `U`.  The event-stream
oracle enumerates first insertions over a doubled cyclic chronology.  It
therefore covers arbitrary interval width, cyclic wrap, and tied insertions;
it is not a fixed-q witness approximation.

Rotation maps the complete automaton and its labelled boundary to those of
the translated target.  Hence one row per missing target orbit is exact,
including non-free orbits.

### Corollary 3.2 (finite CEGAR correctness)

At every integral incumbent, physical replay either finds no hole or emits
a valid row (3.1) for each missing lower-q2/q3 or upper orbit.  Since the
option set is finite and each emitted row excludes the incumbent, exhaustive
iteration is complete for these target families.  If it terminates with
`PASS_CYCLIC_COMPILER_SHADOW_CARRIER`, the materialized cycle has exact
middle ownership, the residence and q1 properties of the base model, no
lower-q2/q3 holes, and no arbitrary-width upper hole.

This is a mathematical completeness statement about the encoding and
separator.  A time or memory stop before termination is still UNKNOWN.

### Component rows

The default CP and lean models encode the two shore paths eagerly.  The lean
executable also supports a cycle-cover reduction.  If a decoded selected
component is `C`, the clause

\[
  \bigvee_{a:\,tail(a)\in C,\ head(a)\notin C}x_a
\]

is necessary for every connected completion.  Under unit indegree and
outdegree this is a sound directed component cut.  It is not needed in the
reported default binary-order runs.

## 4. Fail-closed promotion pipeline

Every q1/residence incumbent is promoted immediately through the following
pipeline.

1. Decode exactly one selected option per quotient owner.
2. Reconstruct the quotient block order and check its crossings and voltage.
3. Lift every selected option through all rotations and require `W` distinct
   middle owners and only Johnson transitions.
4. Replay residence and both literal q1 palettes.
5. Audit lower q2 and q3 exactly; install labelled lower frontier rows for
   every missing orbit.
6. Run the all-width accumulated-union oracle; install labelled upper
   frontier rows for every missing orbit.
7. Only after all cyclic shadow rows pass, enumerate linear cuts and
   orientations with
   `scratch/threadD_phasefree_comp3_adapter_20260730.py` (SHA-256
   `a6f2e3a014f07282530f168a6b4ef1ea9a5dc4e7705aade3edf126c5a5f13ae0`).
8. Re-audit the literal linear lower and upper witnesses, verify the maximal
   erosion core, solve the exact compiler/source model, and accept only
   after the generated word derives the proposed chronology and covers every
   nonempty mask.

At `K=16`, the final step must cover all 65,535 nonempty masks.  The cyclic
carrier status is therefore necessary but not itself a word claim.

## 5. Exact `K=8` and `K=10` regressions

### 5.1 Master results

| case | options | initial vars/constraints | final constraints | CP rounds | learned deep rows | carrier length | external wall | peak RSS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `K=8` | 148 | 293 / 223 | 223 | 1 | 0 | 70 | 0.73 s | 105,316 KiB |
| `K=10` v2 | 680 | 1,087 / 625 | 637 | 6 | 12 | 252 | 13.65 s | 130,448 KiB |

Both runs used one CP-SAT worker.  The final exact physical cycle hashes are

```text
K8   6cbe3d6b3ea2bd9f223b1ea01b7eb7fc63da0f43f2ab8f3b8b0762213fa0e876
K10  0dcc8e281d529fa2efd4048330db546c373ea94bed8994960a1a6241bcfa8def
```

The K8 result passes lower q2/q3 and all 93 strict upper targets without a
learned row.

The K10 v2 run first produced five failing incumbents and installed 12 exact
upper frontier rows.  Its sixth incumbent has zero lower-q2 holes, zero
lower-q3 holes, and all 386 strict upper targets covered.  Its physical
replay also has 252 distinct middle owners, no non-Johnson transition, no q1
hole, and minimum positive run three.

### 5.2 Generation distinction

The earlier q1-only fresh K10 carrier is not this result.  It had the lower
q2 orbit represented by `73` and the upper-rank7 orbit represented by `687`,
and therefore did not compile.  The new v2 carrier was regenerated by the
global CEGAR master; it shares **0 of 28** selected quotient options with the
earlier carrier (symmetric difference 56).  This is direct evidence that the
implemented lane is not making a local repair of the old source.

### 5.3 Exact K10 compilation

The new v2 carrier compiles at cut zero.  The retained exact compiler reports

```text
OPTIMAL WORD len 254 (cut 0)
```

and the independent solver-free audit verifies:

```text
word length                         254
middle owners                       252 distinct / 252
Johnson defects                     0
lower q1/q2/q3 holes                0 / 0 / 0
arbitrary-upper holes               0
covered nonempty masks              1023 / 1023
missing nonempty masks              0
word SHA-256                         6e7adf1b03655124c310029232215638552936a2674625722aeddd12b47951c3
```

Compilation used 0.45 seconds wall time and 107,700 KiB peak RSS.  Thus the
answer to “do fresh K10 candidates compile?” is generation-sensitive:
the earlier q1-only carrier does not, while the new global v2 CEGAR carrier
does, with a literal verified word certificate.

## 6. Exact `K=16` status

At `K=16`,

```text
R=8, n=15, M=429 owners per shore, N=858 quotient owners, W=12870,
raw options=54912, eligible non-self-loop options=54856.
```

### 6.1 CP-SAT low-memory attempt

The lazy, no-presolve CP model had

```text
variables       66,011
constraints     18,691
q1 rows          1,528
learned rows         0
workers              1
```

It was run twice and raised `std::bad_alloc` before producing its first
incumbent in both attempts:

| launch | internal memory parameter | producer elapsed | external wall | peak RSS | status |
|---|---:|---:|---:|---:|---|
| initial bounded run | 1,536 MiB | 6.47 s | 7.05 s | 1,904,588 KiB | `UNKNOWN_RESOURCE_MEMORY` |
| 4-GiB outer-envelope retry | 2,048 MiB | 19.29 s | 20.17 s | 3,738,644 KiB | `UNKNOWN_RESOURCE_MEMORY` |

The second result has embedded payload SHA-256
`1720c75c1d92acd049a12ac2399255b64cba44fbb8e0b0b8c8814a302a6dee7c`.
There is no carrier, no deep row, and no feasibility conclusion from either
attempt.  This is why the lean DIMACS model, rather than a larger CP-SAT
retry, is the current `K=16` executable path.

### 6.2 Lean DIMACS attempt

The retained lean base was built from the exact binary rail-order encoder:

```text
base variables       445,047
base clauses       4,088,808
DIMACS body bytes  90,620,823
q1 rows                 1,528
tight q1 rows              858
binary rail bits              9
```

Base construction took 4.61 seconds and 39,936 KiB peak RSS.  Kissat was
then allowed one 300-second round.  It produced no SAT assignment and no
UNSAT result; the wrapper recorded `UNKNOWN_RESOURCE_OR_TIME`, zero learned
rows, and no carrier.  The exact solver interval was 300.03 seconds; total
external wall time was 304.76 seconds and peak RSS was 381,808 KiB.

The executed lean source is retained verbatim as

```text
scratch/threadD_solve_even_two_rail_compiler_cegar_kissat_prebatch_20260730.py
SHA-256 f152a569f15c46a54529929de6416f9f9b3a9d5abb096569b1d385a20e39da34
```

The maintained successor is

```text
scratch/threadD_solve_even_two_rail_compiler_cegar_kissat_20260730.py
SHA-256 00ce5e8708f2d7a42f65e682a4e4362ad1c646b19ae35bf02a6c05e6ac399f68
```

It has not been used to reinterpret the retained run.  It adds fair
round-robin frontier batching across lower q2, lower q3, and arbitrary upper
families (so batch size one cannot starve a family), exact option/DIMACS and
CNF/output ledgers, and separate timeout/round-limit/resource `UNKNOWN`
statuses.  Five lightweight regressions, including exact replay of a K10
prebatch frontier, pass; their audit is
`scratch/threadD_kissat_frontier_batching_audit_20260730.json`.

The Kissat binary hash in the result is
`3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d`.
No scoped UNSAT, formal or otherwise, follows from this bounded run.

## 7. Reproducible artifacts

| artifact | file SHA-256 | embedded payload/status |
|---|---|---|
| K8 v2 result | `72e96bc52d490ba3a19a3b8e0285a1b16454a3c439aa023105cf4a29c2b91fe6` | payload `8e4ea6c39f2...`, PASS |
| K10 v2 result | `0a58c1821eb5c0d73c13f79fc91c340acecd7723afc5db0fafac0414abce3deb` | payload `460f922d4d1...`, PASS |
| K16 CP result | `1875e282485aa4b36ec63a00dc5900c199d8a9b9bde0e6dfa2ca608cf871b3cc` | payload `7633d6e4610...`, UNKNOWN memory |
| K16 CP 4-GiB retry | `4f595d8bf4057271c55bf2c2c76a86c5893f401bd6d3655d9a93a675de322df6` | payload `1720c75c1d9...`, UNKNOWN memory |
| K16 lean build | `f78504d3f16881f236018ee60023ac7d5be43a802e568fcd872fe1cd6c890d94` | payload `4ebf4e2b605...`, model built |
| K16 lean solve | `2648b339bcfd2972e9923041af9052326034ce019ee2c29bc376a36997556297` | payload `1dc1711c33b...`, UNKNOWN time/resource |
| K10 cycle input | `3b8de0f0f546a25efda21ae5c8e7713f316df2aea09495c5bbfa1287fb7931ae` | physical cycle `0dcc8e281d...` |
| K10 word | `6e7adf1b03655124c310029232215638552936a2674625722aeddd12b47951c3` | exact length 254 |
| K10 word audit | `96eafbabc9844ba25d5686bd2ac8199c0dc7fa471abaa14bcf1e7b0e6f378c7e` | payload `ce5c9231f8b...`, PASS |
| deep-row audit | `e600a1f86da85ee394a2352416ad170a933e865e253e749eac8af17165bb0a82` | payload `ed0f3836b2c...`, PASS |
| lower-separator audit | `de945d2aa85bd8ab8f4210ad91d736d73a325c88ececd18a5d01ec11a5b537c3` | payload `5cf023475720...` |
| upper-separator audit | `f8f8463ed7d5768be0b5c41be346be18ac76a67edef898ea332525ddf899a186` | payload `d62fd13e338e...` |
| complete result replay | `e07b46b387436e814117a2f4537552d0d64acb60f142129e3d4f06f1c5f4b45f` | payload `85eac681fbf...`, PASS |
| lean batching audit | `792ad7c5f8a0eff0ec8e537cf0588b29ca049193fb3c0aebfc0529f60bf6356e` | 5/5 PASS |

The corresponding files are, in order:

```text
scratch/k8.compiler_cegar.v2.json
scratch/k10.compiler_cegar.v2.json
scratch/k16.compiler_cegar.lazy.nopresolve.solve.json
scratch/k16.compiler_cegar.lazy.nopresolve.4g.solve.json
scratch/k16.kissat.compiler_cegar.build.json
scratch/k16.kissat.compiler_cegar.solve.json
scratch/k10.compiler_cegar.cycle.json
scratch/k10.compiler_cegar.word
scratch/threadD_k10_compiler_cegar_word_20260730.audit.json
scratch/threadD_deep_shadow_component_rows_20260730.audit.json
scratch/threadD_lower_fixed_depth_labelled_boundary_k8_k10_20260730.audit.json
scratch/threadD_upper_accumulated_union_separator_k8_k10_20260730.audit.json
scratch/threadD_even_two_rail_compiler_cegar_results_20260730.audit.json
scratch/threadD_kissat_frontier_batching_audit_20260730.json
```

## 8. Reproduction commands and claim discipline

Small regressions may be rerun with one worker.  `K=16` solving is H100 CPU
only and must be wrapped in an external `prlimit`/timeout appropriate to
current server headroom.

```bash
PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_solve_even_two_rail_compiler_cegar_20260730.py 8 \
  --output /tmp/k8.json --checkpoint /tmp/k8.checkpoint.json \
  --model /tmp/k8.pbtxt --rounds 20 --seconds-per-round 120 \
  --workers 1 --max-memory-mb 1536

PYTHONPATH=/dev/shm/orlib python3 \
  scratch/threadD_solve_even_two_rail_compiler_cegar_20260730.py 10 \
  --output /tmp/k10.json --checkpoint /tmp/k10.checkpoint.json \
  --model /tmp/k10.pbtxt --rounds 20 --seconds-per-round 60 \
  --workers 1 --max-memory-mb 1536

python3 scratch/audit_threadD_k10_compiler_cegar_word_20260730.py
```

For a new `K=16` launch, any SAT q1/residence incumbent must go directly
through the exact lower-q2/q3 and arbitrary-upper separators and physical
replay.  It must not be scored as progress merely for resembling the old
source.  Only an all-shadow carrier may enter the exact cut/compiler stage,
and only a 65,535-mask literal replay may be called a `K=16` word.

The current exact frontier is therefore:

> Find one integral assignment in the global 54,856-option master, or prove
> the scoped one-block class infeasible.  The retained bounded attempts do
> neither.  Exact66 and the 93-hole source-relative local-repair lane are no
> longer relevant to this search.
