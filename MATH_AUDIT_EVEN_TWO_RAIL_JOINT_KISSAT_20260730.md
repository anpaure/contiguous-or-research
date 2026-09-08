# Audit and strengthening of the lean joint two-rail DIMACS model

Date: 2026-07-30

Audited implementation:

```text
scratch/solve_even_two_rail_joint_history_kissat_20260730.py
scratch/audit_joint_rail_quotient_history_model_20260730.py
scratch/solve_even_two_rail_joint_history_20260730.py
```

## 1. Exact scope

The model is exact for the following **restricted carrier class** at even
`K=2R`, with `n=K-1` and `M=binom(n,R)/n`:

1. a `Z_n`-equivariant quotient tour through all `M` A-orbits and all `M`
   B-orbits;
2. exactly one A-to-B and one B-to-A transition (one contiguous block on
   each shore);
3. generating quotient voltage, normalized to voltage one;
4. positive coordinate residence at least `d+1`;
5. literal coverage of both lower and upper `q=1` palettes.

It does **not** claim deeper-shadow coverage, negative/gap residence, lower
compiler feasibility, or an optimal word.  `UNSAT_NO_PROOF` is restricted to
this class and is not a statement about `nu(K)`.

## 2. Gate-by-gate correctness audit

### 2.1 Sinz exactly-one

`BodyWriter.exactly_one` is the standard sequential at-most-one encoding plus
one at-least-one clause.  The last literal is paired with the last prefix bit,
and every intermediate literal both advances the prefix and conflicts with a
previous true literal.  Exhaustive existential-extension tests for row sizes
one through six agree exactly with `sum(x)=1`.

The added `at_most_two` strengthening was independently exhaustively tested
for row sizes one through six and agrees exactly with `sum(x)<=2`.

### 2.2 Directed degree rows and seams

Every quotient node has exactly one selected outgoing and incoming option.
Exactly one A-to-B and one B-to-A option is selected.  Consequently each shore
is one directed seam-to-seam path together with zero or more directed cycles.
This observation is used below to replace generic connectivity CEGAR by an
exact path-order certificate.

### 2.3 Moving insertion history

At a quotient occurrence with physical phase `p`, history value `x` denotes
physical old coordinate `p+x`; the sentinel denotes a transition with no old
coordinate inserted.  Across an option of phase increment `delta`, the same
physical coordinate has target-frame name `x-delta mod n`.  Thus the clauses

```text
H[target,0] = inserted-delta
H[target,lag] = H[source,lag-1]-delta
deleted not in H[source,0..d-1]
```

are exactly the last-`d`-insertions automaton in canonical quotient frames.
The sentinel ages the old-coordinate history across the unique deletion-only
seam, as it should.  On a cyclic lift, forbidding deletion of any of the last
`d` inserted coordinates is equivalent to every positive coordinate run
having length at least `d+1`.  The independent materialized audit checks both
descriptions and they agree at K=8 and K=10.

The top coordinate is absent from this history intentionally: exactly two
cross seams make its positive run the entire A block, of length `M>d` in the
instances in scope.  The builder now rejects the exceptional parameter range
`M<=d` rather than silently omitting this check (in particular, the one-block
class at K=4 has a top run of length one and cannot meet depth one).

### 2.4 Voltage BDD

Exactly one outgoing edge at a node implies exactly one selected delta.  The
one-hot automaton starts at residue zero, adds the selected delta at each of
the `2M` quotient nodes in a fixed node order, and ends at residue one.  Since
the sum is commutative, this equals the tour voltage independently of traversal
order.

Fixing voltage one is without loss inside the generating-voltage class, even
for composite `n`: if the voltage is a unit `v`, multiplying every old
coordinate in `Z_n` by `v^{-1}` sends the rotation generator to its
`v^{-1}`-power and sends the voltage to one.  Middle ownership, q1 coverage,
and residence are invariant under this relabeling.  Non-generating voltages
are correctly excluded because their physical lift is disconnected.

### 2.5 Projected q1 rows

The four edge types produce precisely these palettes:

| edge type | lower | upper |
|---|---|---|
| AA | top + rank `R-2` | top + rank `R` |
| BB | rank `R-1` | rank `R+1` |
| AB/BA | rank `R-1` | top + rank `R` |

A selected quotient edge of unit voltage occurs through all `n` physical
rotations, so one canonical provider covers its entire label orbit.  This
remains true for the shorter rank-6/rank-9 orbits at `n=15`: the physical lift
merely repeats labels in a stabilized orbit.  The decoder then independently
materializes all physical edges and checks literal q1 coverage, so the orbit
projection is not trusted as the final certificate.

The rank-`R-1` lower palette and top+rank-`R` upper palette each contain `M`
labels and receive exactly `M+1` selected edge occurrences (`M-1` internal
edges plus the two seams).  Coverage therefore implies multiplicity at most
two in every such row.  `--tight-q1-at-most-two` adds these 858 implied
cardinality constraints at K=16; it is propagation-only and does not narrow
the class.  The sequential counters expose their final "at least two" bits,
and one additional exactly-one row states the implied global fact that each
palette has exactly one duplicated label.

### 2.6 Original connectivity CEGAR

The degree rows make every assignment a directed cycle cover.  For a proper
selected component `S`, the clause

```text
OR { x_(u,v) : u in S, v outside S }
```

is a valid subtour cut.  Identifying `S` with its complement when caching cuts
is sound: in a finite indegree-one/outdegree-one cover, a selected edge crosses
from `S` to its complement iff another selected edge crosses back.  All
components of every incumbent are cut, and timeout/resource termination is
reported only as `UNKNOWN`.

### 2.7 Decoder and independent replay

The decoder follows the selected quotient successor map from A-orbit zero,
accumulates phases, requires return to the root at phase one, lifts the quotient
tour through all `n` rotations, and checks middle distinctness, Johnson
adjacency, residence, and literal q1 coverage.

The standalone auditor reconstructs the physical carrier independently from
the emitted `(c,t)` normal form.  It now accepts both a bare carrier and the
solver's result wrapper and asserts that any emitted physical `cycle` equals
the independently reconstructed lift.

## 3. Exact binary rail-order strengthening

The option `--binary-rail-order` eliminates connectivity CEGAR without an MTZ
unary order or a generic flow encoding.

Let `b=M.bit_length()` and `Q=2^b`, so `Q>M`.  Give each quotient vertex a
`b`-bit position.  A shared ripple circuit computes `position(u)+1 mod Q`.
Every selected same-shore option `u->v` implies

```text
position(v) = position(u)+1 mod Q.
```

Every selected cross seam fixes its target to position zero and its source to
position `M-1`.

**Lemma.** These constraints are equivalent to connectedness in the stated
one-A-block/one-B-block class.

**Proof.** The degree and seam equations make each shore one seam-to-seam path
plus directed cycles.  A directed cycle of length `ell<=M` would imply
`position=position+ell mod Q`.  But `0<ell<=M<Q`, impossible.  Hence no cycle
exists, so the unique path contains all `M` vertices.  Conversely, assign
positions `0,...,M-1` along each Hamilton rail path.  All constraints hold.
Thus no feasible connected carrier is removed.  QED.

At K=8 and K=10 this strengthening produces a connected carrier in the first
SAT call, rather than after six and eight CEGAR rounds respectively.

An additional optional `--static-two-cycles` adds all reciprocal two-cycle
clauses for the CEGAR mode.  There are 28,880 at K=16.  Binary rail order
already excludes cycles of every proper length, so the two options are not
combined.

### 3.1 Exact residual orientation symmetry

`--reverse-negation-symmetry` breaks one remaining involution without assuming
complement residence.  Reverse the physical chronology and simultaneously
relabel every old coordinate `x` as `-x mod n` while fixing the top coordinate.
Reversal negates voltage and coordinate negation negates it again, so unit
voltage is preserved.  Positive run lengths and all q1 colours are preserved,
and AB/BA seams are exchanged.

The implementation reconstructs this map on the full option catalogue and
asserts that it is an involution.  It ranks AB options and maps BA options into
that same ordering.  If `a` is the selected AB rank and `b` the transformed BA
rank, it imposes `a<=b` with exact prefix-OR variables.  The involution swaps
`a,b`, so every orbit retains at least one representative.  This is only a
factor-two symmetry reduction, but it is proof-safe for the positive-residence
class.  Plain complementation was deliberately **not** used: it exchanges
positive runs with gaps and would narrow the model unless negative residence
were also imposed.

## 4. Regression evidence

Fresh, from-scratch DIMACS/Kissat carriers:

```text
scratch/even_two_rail_joint_order_k8_20260730.PASS.json
  sha256 ef201217512dc314a23d86d4833e97fc224c1759bbbb546dfe357a61e12889ba
scratch/even_two_rail_joint_order_k8_20260730.audit.json
  sha256 2b7e2a40a4ad2f5cd1d5ead00eade573e63d726443a9f7e02dbbf0509e47c9e3

scratch/even_two_rail_joint_order_k10_20260730.PASS.json
  sha256 e0e088d93d2265a88add4ae7c68423a39ad2bb32a457de9d08320da10188984f
scratch/even_two_rail_joint_order_k10_20260730.audit.json
  sha256 96ba925ce1dfb8bf5a9a3d2b5c5d609ba9122e49103c8d72fd940ae906d99900
```

Both independent audits report:

```text
middle_distinct = W
johnson_bad = 0
history_violation_count = 0
direct_short_old_run_count = 0
direct_short_top_run_count = 0
lower_q1_missing = 0
upper_q1_missing = 0
one_block_per_shore = true
voltage = 1
emitted_cycle_matches_ct_lift = true
```

The pre-existing compact K=8 artifact also passes the same independent audit.
The pre-existing Waksman K=10 artifact is resident and q1-complete but has six
top-trace transitions, so it correctly lies outside this one-block class; the
fresh K=10 regression above supplies the relevant in-class witness.

## 5. K=16 size and current evidence

Measured under a 4 GiB OS address-space cap on the H100 CPU host:

| encoding | variables | clauses | DIMACS body |
|---|---:|---:|---:|
| base CEGAR | 299,301 | 2,746,474 | 61,395,523 bytes |
| + static reciprocal 2-cycles | 299,301 | 2,775,354 | 61,845,828 bytes |
| + binary rail order | 320,751 | 3,781,072 | 85,050,421 bytes |
| binary order + reversal/negation symmetry | 327,615 | 3,805,094 | 85,493,101 bytes |
| + tight q1 at-most-two | 423,597 | 3,054,210 | 66,965,925 bytes |
| binary order + tight q1 | 445,047 | 4,088,808 | 90,620,823 bytes |

A 120-second low-priority Kissat pilot of binary order + tight q1 remained
`UNKNOWN`; peak displayed memory was about 360 MB.  This is evidence that the
strengthened model is operationally small, not evidence of SAT or UNSAT.

## 6. Verdict

No semantic defect was found in the K=8/K=10/K=16 target range.  One small-
parameter boundary omission was found and fixed: K=4 has `M=1<=d`, so the
unmodeled top-coordinate run violates residence; both builders now reject that
empty one-block class.  The original CEGAR encoding is otherwise sound.  The
binary rail-order formulation is a materially stronger exact CNF: it replaces
an unbounded sequence of solver restarts with one formula and proved path
certificates on both shores.  Small-instance validation is exact; K=16
feasibility of the restricted class remains open.

## 7. Compiler-shadow CEGAR extension

The optional `--deep-cegar` mode now continues after a connected q1/residence
carrier instead of returning immediately.

### 7.1 Exact lower q2/q3 rows

For every missing lower q2 or q3 orbit, the solver enumerates all quotient
option paths that can realize it.

* A q2 provider is a two-option path; its three physical states have the
  requested rank-`R-2` intersection.
* For q3, a three-state prefix must already have rank `R-2` (two Johnson
  deletions cannot lower the intersection further).  The final option must
  delete one element of that intersection.  This gives every q3 provider
  without enumerating the full cubic option-path catalogue.

For a provider path `P`, a fresh variable `y_P` is defined exactly by

```text
y_P <-> AND { x_e : e in P }.
```

The target row is `OR_P y_P`.  Hence the lazy row is a necessary and sufficient
coverage constraint for that orbit, not an incumbent no-good and not a fixed-
width heuristic.  Any later incumbent still missing an installed label causes
an assertion failure rather than being silently accepted.

At K=8, an exhaustive independent enumeration of every distinct-node option
path agrees with the optimized provider catalogue on all q2/q3 labels:

```text
6 orbit rows
10,122 provider paths total
q2 row sizes: 388, 388, 388, 312
q3 row sizes: 8,094, 552
```

### 7.2 Exact arbitrary-width upper audit

For every cyclic start, the audit records the first future occurrence of each
coordinate absent from the start state.  Sorting those events reconstructs
exactly every accumulated union attained by a contiguous segment.  This is
equivalent to a literal width-by-width scan but costs `O(KW log K)` rather than
`O(W^2)`.

There is not yet a compact local DNF for arbitrary widths.  If an incumbent
has an upper hole, the CEGAR therefore adds only

```text
OR { not x_e : e selected in this incumbent }.
```

This excludes exactly that incomplete carrier.  It is weak but completely
sound and does not replace arbitrary-width coverage by fixed q2/q3 coverage.

### 7.3 Independent literal regressions

The independent checker

```text
scratch/audit_even_two_rail_deep_cegar_regression_20260730.py
```

does not import the solver and directly scans every cyclic start and width.
It verifies all middle masks, every Johnson edge, positive residence, lower
q1/q2/q3, and every arbitrary upper target.

```text
scratch/even_two_rail_joint_deep_k8_20260730.PASS.json
  sha256 fc032976ea264fdaabd0f54200b2daade0fc975a2d949a0f3567064d38fcf287
scratch/even_two_rail_joint_deep_k8_20260730.audit.json
  sha256 aa0b7c6c1d8ea071c9c8b0d77052e38883bff57b5e642d8bb288ced45de59fe7

scratch/even_two_rail_joint_deep_k10_20260730.PASS.json
  sha256 fa86522690b60b0e3a22dd061fb2e101ae217c0b6ac96259c5e749c8513c2bc2
scratch/even_two_rail_joint_deep_k10_20260730.audit.json
  sha256 cc92bc98d72645f050b973449e276583f9f3425f68d823d31faf626f76e572d4
```

K=8 passed in the first connected round.  K=10 passed in four rounds: two
arbitrary-upper incumbent no-goods, then one missing q2 orbit (`label 73`)
with 246 exact path providers (246 variables, 739 clauses), then a literal
zero-hole carrier.  Both independent audits report zero lower q1/q2/q3 and
zero arbitrary-upper holes.

No additional K=16 process is launched by this extension.  The existing
base q1/residence pilots remain the front gate; any resulting carrier can be
fed immediately into the audited deep loop.  `--seed-carrier PATH` performs
that handoff directly: it independently replays the selected options, returns
at once if the seed is already compiler-shadow complete, or preinstalls every
missing lower provider row and the exact upper-incomplete incumbent no-good
before the first Kissat round.  Seeded K8 and K10 regressions both converge to
the same literal zero-hole status.

## 8. Live K16 signal and the exceptional q2 orbit

At roughly 1,039 and 772 solver seconds respectively, the two exact live
binary-order pilots had the following Kissat state:

| lane | RSS | conflicts | remaining variables | remaining fraction |
|---|---:|---:|---:|---:|
| plain binary order, seed 20260731 | about 388 MB | 5.6 million | 147,905 | 46% |
| + reversal/negation symmetry, seed 20260732 | about 295 MB | 4.0 million | 152,101 | 46% |

Both sustain approximately 5,000--5,400 conflicts/second and continue normal
clause reduction.  Neither has produced an assignment, a bound, or a monotone
objective: this is healthy search activity but **not** a credible near-SAT
signal.  The symmetry lane leaves slightly more variables after preprocessing
and has not shown a better conflict slope; its only established benefit is the
proof-safe factor-two quotient of solution orientations.

The base CNF is dominated by the moving-history implications: about 1.76
million clauses are the two lag-shift tables alone, and roughly 2.08 million
of the 2.75 million base clauses belong to history.  The voltage automaton is
about 0.32 million clauses.  This explains why a small seam symmetry does not
materially change the live search profile.

An exact streaming census of all two-option lower-q2 providers is recorded in

```text
scratch/k16_joint_q2_orbit_provider_counts_20260730.audit.json
  sha256 28c45cd2e37128d53dc539b2708c452703de003f2a59d173fc89b3882673005e
```

It checks 3,449,552 distinct-node two-option prefixes.  Of these, 3,066,320
give a rank-6 intersection.  The 8,008 physical rank-6 masks form 536 rotation
orbits.  One orbit is uniquely scarce:

```text
label 37449 = {0,3,6,9,12,15}
providers = 920
```

Every ordinary orbit has at least 1,656 providers and most have 5,726--5,760.
The exceptional label is the top coordinate together with the period-three
old-coordinate subgroup.  It is therefore a natural exact non-q1
strengthening.

The solver now accepts

```text
--preinstall-lower-q2-label 37449
```

which adds the exact OR of its 920 two-edge path conjunctions: 920 variables
and 2,761 clauses.  This is a required compiler-shadow condition, not an
implied q1 propagation clause or a sufficient-only fixed-width substitute.
It has been regression-tested at K=8 with the analogous exact orbit row and a
full independent deep replay.  It is prepared for the next K16 seeded/deep
run; the two already-running base pilots were deliberately left untouched.

## 9. Why the exceptional rows are scarce, and what they force

Put

```text
H = 3 Z_15 = {0,3,6,9,12}.
```

The exceptional q2 label is `H + top`.  Every A-shore middle state that
contains it has the unique form

```text
H + top + P,    P in binom(Z_15 \ H, 2).
```

Its uniqueness at this stabilizer size is forced by divisibility.  A subset
fixed by a nontrivial rotation of `Z_15` is a union of cycles of size three or
five.  A top-containing q2 target has five old coordinates, so stabilizer five
forces precisely one coset of `H`; all three cosets are rotations of the same
label.  Likewise, a q3 target without top has five old coordinates and the
only nonfree orbit is a coset of `H`, while a top-containing q3 target has four
old coordinates and cannot be a union of nontrivial rotation cycles.  This is
why the q3 census has exactly one nonfree—and exactly one singular—row.

For a fixed physical copy of `H`, a three-state q2 provider is a Johnson path
of two-subsets

```text
P0={a,u}, P1={a,v}, P2={v,w}.
```

There are exactly

```text
binom(10,2) * (2*8) * 8 = 5,760
```

such physical paths before quotient-node distinctness.  Translation by the
five-element stabilizer `H` identifies them in packets of five.  Of the 5,760,
exactly 1,160 have two of the three middle states in the same necklace node:

```text
repeated pair 02 only: 560
repeated pair 12 only: 280
repeated pair 01 only: 280
all three repeated:     40
```

Thus 4,600 survive, and `4,600/5 = 920`.  This derives the observed minimum;
it is not an accidental catalogue irregularity.

The same calculation exposes a strong order consequence.  Exactly nine
A-shore necklace nodes contain a rotation of `H`.  Every one of the 920
providers consists of three consecutive nodes from this nine-node set, and
both phase increments are `0 mod 3`.  There are 380 possible node triples
(300 with two phase realizations and 80 with four).  Therefore the exact q2
row is much more than 2,761 extra clauses: it forces a length-three cluster
among nine exceptional nodes inside a 429-node A rail.  The weaker redundant
order consequence is that some exceptional middle node has both its selected
predecessor and selected successor in the exceptional set.  The exact provider
DNF additionally enforces the correct phase and deletion pattern.

The exact streaming q3 census is recorded in

```text
scratch/k16_joint_q3_orbit_provider_counts_20260730.audit.json
  sha256 6d48a4c77fd7713ddecb529ea76afe648ee04793b5e88f512f19e22372931c86
```

It counts 146,771,320 compatible three-option paths over all 292 q3 orbits.
Again there is a unique singular row:

```text
label 4681 = H
providers = 88,464
next-smallest row = 480,960
```

All other q3 labels have free old-coordinate orbits.  The singular row has
orbit size three and stabilizer five.  It forces four consecutive quotient
nodes to lie in the 9 A-shore plus 24 B-shore nodes containing a rotation of
`H`, with all three phase increments `0 mod 3`.  In the legal one-A-block,
one-B-block model, 85,728 of its catalogue providers remain compatible with
the global seam constraints.  Their shore patterns are

```text
AAAB 7,360    AABB 7,504    ABBB 6,640
BAAA 7,360    BBAA 7,504    BBBA 6,640
BBBB 42,720
```

so the q3 row forces either four consecutive exceptional B nodes or an
exceptional cluster crossing exactly one seam.  The remaining 2,736 catalogue
paths cross shores more than once and are automatically false under the
one-block constraints.

The independent geometry audit is

```text
scratch/k16_subgroup_shadow_geometry_20260730.audit.json
  sha256 d4887f9bdd15a479c965448ad208d250d87279be9891d30c6cdf92b2c5ac1f4a
```

It checks the fixed-target count, stabilizer quotient, exact node sets, shore
patterns, and phase residues without invoking a solver.  This identifies the
period-three subgroup as the first exact deep-shadow strengthening to install
after a base carrier appears.  No additional heavy K16 solver was launched for
these censuses.

The solver now supports both exact rows directly:

```text
--preinstall-lower-q2-label 37449 \
--preinstall-lower-q3-label 4681
```

With binary rail order, provider paths that cross both seams in three edges
are impossible and are removed exactly.  Q3 paths sharing their first two
options also reuse one exact prefix variable: for each prefix `p`, a second
witness is equivalent to `p selected AND some compatible third edge selected`.
This is an exact factoring of the DNF, not a relaxation.  The K16 singular q3
row has 85,728 paths but only 11,720 prefixes, so it needs 23,440 auxiliary
variables before cross-row reuse.  Exactly 920 of those prefixes are the q2
`H+top` providers, so their already-defined variables are shared with q3.
The q3 row consequently needs 22,520 new variables and 141,569 clauses instead
of one variable and four clauses per path.  Including q2, a zero-round build
gives 23,440 new provider variables and 144,330 exact provider clauses.  The
redundant nine-node q2 cluster
propagation adds 9 witness variables and 19 clauses, for 344,200 variables and
144,349 added clauses total.  The provider enumeration takes about 5--8
seconds on the remote CPU host:

```text
scratch/k16_joint_q23_preinstall_size_20260730.audit.json
  sha256 7b585784ac2cde11d8dc40f1c67041b0ae14ccb123e49fa93a5c81fdd3a4c024
```

Joint q2+q3 preinstallation was regression-tested end to end on the existing
independently verified K8 and K10 carriers.  The exact row sizes were

```text
K8:  q2 label 129 -> 312;   q3 label 128 -> 552
K10: q2 label 73  -> 246;   q3 label 513 -> 31,284
```

and both returned `PASS_COMPILER_SHADOWS` with unchanged literal zero-hole
audits.  A stronger regression enumerated every filtered q2/q3 row (6 rows at
K8 and 19 at K10) and checked that each has an actually selected provider path
in the saved carrier; there were zero row misses.  An exhaustive truth table
over a synthetic overlapping-prefix row also verified that the factored CNF
is satisfiable exactly when its original path DNF is true.  Finally, a fresh
K8 Kissat solve from the factored CNF (not a seed-only replay) returned SAT in
0.032 seconds and its decoded carrier passed the full independent compiler-
shadow audit.

There is no further universal share-or-avoid clause between the two K16
subgroup rows.  An `AAAB` q3 provider can reuse its first two A edges as the
entire q2 provider, whereas a `BBBB` q3 provider can be edge-disjoint from the
q2 A cluster.  Thus both complete overlap and complete separation occur in
the exact catalogue.  The factored encoding reuses the 920 shared-prefix
variables when available without requiring the solver to choose one of them.
The strongest common phase statement is already captured above: every edge in
either exceptional provider has increment zero modulo three.  Any
unconditional clause demanding overlap or disjointness would remove valid
carriers.

## 10. Complete finite H-cluster portfolio

The subgroup rows admit a proof-safe finite split that is much smaller than
branching on all option paths.

* Every q2 `H+top` provider has one middle node among the nine exceptional
  A-nodes.  The provider counts per middle are 80 for four nodes and 120 for
  five nodes.
* Every q3 `H` provider in a connected one-block carrier has exactly one of
  seven shore patterns:

```text
AAAB 7,360    AABB 7,504    ABBB 6,640
BAAA 7,360    BBAA 7,504    BBBA 6,640    BBBB 42,720.
```

Therefore the Cartesian split `(q2 middle node, q3 shore pattern)` has 63
cases and its union contains every carrier satisfying both subgroup rows.  In
each branch the q2 middle is fixed, its selected predecessor and successor are
exceptional, and their phase increments are zero modulo three.  The q3 shore
pattern fixes whether the four-node cluster lies internally in B or at one of
the two unique seams.

The `AAAB` case is stronger: its first two edges are themselves the q2
provider.  Coupling both rows to the same middle node leaves only 640 or 960
q3 paths per branch.  The nine `AAAB` branches add just 161--241 variables and
1,045--1,565 clauses.  The remaining branch ranges are:

| q3 pattern | added variables | added clauses |
|---|---:|---:|
| AABB | 2,257--2,297 | 13,189--13,309 |
| ABBB | 2,065--2,105 | 11,845--11,965 |
| BAAA | 2,257--2,297 | 13,045--13,165 |
| BBAA | 2,065--2,105 | 12,709--12,829 |
| BBBA | 13,361--13,401 | 40,085--40,205 |
| BBBB | 13,361--13,401 | 76,165--76,285 |

This gives a natural sequential portfolio order: the nine coupled `AAAB`
cases first, then `ABBB/BBAA`, `AABB/BAAA`, `BBBA`, and finally `BBBB`.  It is
an exhaustive case split, not a heuristic ordering.

Against the unbranched factored formula (344,200 variables and 3,925,421
clauses), the branches have 320,912--334,152 variables and
3,782,117--3,857,357 clauses.  Thus the split removes 43--99% of the subgroup
auxiliaries (about 3--7% of all variables); more importantly, it turns an
existential cluster hidden behind a large OR into fixed local rail positions
before the 2.08-million-clause history system starts branching.

The generator and audited branch ledger are

```text
scratch/generate_k16_subgroup_cluster_portfolio_20260730.py
scratch/k16_subgroup_cluster_portfolio_20260730.audit.json
  sha256 d763a3dcb059a6f573aae6e55b568c703a5ac92dabb58079d8671b5cc427f71d
```

Each branch is selected with

```text
--preinstall-q2-subgroup-middle-node NODE
--preinstall-lower-q3-shore-pattern PATTERN
```

in addition to the two singular label flags and binary rail order.  Fresh K8
and K10 solves validated the generic shore-pattern branch (`AAAA` for their
top-containing singular q3 rows) and returned literal
`PASS_COMPILER_SHADOWS`:

```text
scratch/even_two_rail_q3pattern_k8_20260730.PASS.json
  sha256 9b9da8a7f821fc815eb77ed3aaa74431fb9aa387425d2c8166a80109ee4db5c3
scratch/even_two_rail_q3pattern_k10_20260730.PASS.json
  sha256 fdaee1c069f002247a29ef62bf4fb7e6ceb9dd838a2628c6062b619369ca0ea7
```

No K16 portfolio branch is launched while the single unbranched strengthened
pilot remains active.  After that pilot returned `UNKNOWN` at 1,800 seconds,
the four smallest `AAAB` branches (middle nodes 380, 384, 395, and 406) were
run for 600 seconds each under the same 8 GiB/low-priority cap.  All four
returned `UNKNOWN`: no carrier and no UNSAT claim.  They nevertheless reduced
to about 146--148 thousand remaining variables (46%), versus about 252
thousand (61%) for the unbranched raw-DNF run, confirming the intended
propagation improvement.  No later portfolio tier is launched in this audit.

## 11. Multiplier quotient and exact q1 saturation

The fixed-voltage 63-case portfolio has a further exact quotient.  The unit
group of `Z_15` acts on old coordinates by `x -> ux`.  The independent
catalogue checker verifies all 438,848 transformed transition options and the
edge identity

```text
delta'(edge) = u delta(edge) + target_gauge - source_gauge  (mod 15).
```

The gauge terms telescope around a selected quotient cycle, so total voltage
is multiplied by `u`.  The two singular target labels `H=3Z_15` and `H+top`
are fixed setwise by every unit.  The nine exceptional A middles split as

```text
{396}, {378,381,383,405}, {380,384,395,406}.
```

Consequently, existence among the four fixed-voltage-one cases in either
size-four orbit is equivalent to existence at one representative middle with
terminal voltage allowed to be any member of
`U(15)={1,2,4,7,8,11,13,14}`.  Any such witness normalizes back to voltage one
by the inverse multiplier.  The singleton case can remain at voltage one.
Thus the existence portfolio has 21 cases rather than 63.  This is an
existence quotient; it does not say that the four old voltage-one CNFs are
pairwise identical.

The checker and ledger are

```text
scratch/audit_k16_unit_voltage_multiplier_equivalence_20260730.py
scratch/k16_unit_voltage_multiplier_equivalence_20260730.audit.json
  sha256 2c48efe2da368e1fc9777e10323698e39263f75d46d2eefe042fa4c0e95dece2
```

The middle stabilizers quotient the terminal voltages once more.  Middle 380
has stabilizer `{1,4}` and needs only voltage representatives `{1,2,7,11}`;
middle 378 has stabilizer `{1,14}` and needs `{1,2,4,7}`.  Middle 396 is fixed
by all eight units and needs only voltage one.  These four/four/one terminal
sets are still complete for the 21 existence cases and have exactly the same
option-level unit-propagation histogram as the all-eight-unit encoding.  The
production interface accepts them through repeated
`--terminal-voltage-residue` flags.

The solver flag `--any-unit-voltage` changes only the accepting row of the
voltage BDD.  Its propagation cost was measured, not guessed.  In compressed
`AAAB_A380`, fixed voltage one causes 99 base variables to be fixed by unit
propagation; arbitrary coprime voltage fixes 70.  The missing 29 are voltage-
BDD auxiliaries.  Under all 640 exact AAAB provider-path assumptions, both
encodings have *identical* option-level propagation: 16 base seam options are
false, the same 10 paths conflict, and every surviving path fixes three
options true and 3,787--3,801 options false.  CaDiCaL preprocessing changes
from 3,757,226 to 3,757,282 clauses, a loss of only 56 clauses.  This is why
the factor-three branch reduction is adopted despite the wider terminal BDD.

There is also an exact q1 conservation cut.  The `top+rank(R)` palette has
429 colours and exactly 430 selected occurrences.  Coverage therefore means
that exactly one colour is repeated.  Among the 640 AAAB terminal providers
through each of the four 80-prefix middles,

```text
480 have three distinct upper labels,
150 have multiplicity shape (2,1),
10  have multiplicity shape (3).
```

The last ten are impossible.  A `(2,1)` path has already consumed the unique
global repeat, so every other provider of either label appearing in the path
is false.  Removing implications already supplied by source degree, target
degree, and the unique A-to-B seam leaves exactly 11,220 sound four-literal
conditional no-goods per 80-prefix AAAB branch.  The 120-prefix branches have
960 paths with histogram `720,224,16` and 17,048 corresponding saturation
clauses.

This sparse encoding is materially better than generic q1 counters.  The
global `--tight-q1-at-most-two` encoding adds 124,216 variables and 307,736
clauses.  The sparse AAAB theorem adds zero variables and 11,220 clauses, yet
an exhaustive unit-propagation audit gives exactly the same option-level
result: all 150 repeat-consuming paths force 61--73 additional options false.
The arbitrary-unit `AAAB_A380` formula is therefore

```text
original:     320,831 variables, 3,792,552 clauses
preprocessed: 320,831 variables, 3,768,519 clauses
```

with 102,642 eliminated variables and only 70 base fixed variables.  The
independent tight-palette Hall relaxation finds no stronger path obstruction:
exactly the same ten `(3)` paths fail; all 630 other upper-palette cases and
all 640 lower-palette cases pass, with minimum residual colour support six
and seven respectively.  Binary implication SCCs after preprocessing are all
singletons in each of the four tested branches, so there is no hidden
equivalence/component cut to extract from the old formulas.

The independent artifacts are

```text
scratch/audit_k16_aaab_tight_palette_hall_20260730.py
scratch/k16_aaab_tight_palette_hall_20260730.audit.json
  sha256 68985f88d003d447e9c36ba646379377df390bcaae8cffab2c803a6fe6043ea7
scratch/cnf_assumption_unit_audit.cpp
scratch/cnf_binary_scc_audit.cpp
scratch/k16_aaab_A380_anyunit_sparseq1_unit_propagation_20260730.audit.json
  sha256 a00e1c395192df9bef4cc3c859481c41086a92f93ef0f4cb366b021c93e6c106
```

The same conservation theorem applies on either tight q1 palette in every q3
shore pattern.  A solver-free all-path census gives the following sparse cut
sizes before middle-orbit branching:

| pattern | q3 paths | impossible paths | conditional saturation clauses |
|---|---:|---:|---:|
| AAAB | 7,360 | 120 | 130,120 |
| AABB | 7,504 | 0 | 42,680 |
| ABBB | 6,640 | 0 | 71,680 |
| BAAA | 7,360 | 120 | 130,120 |
| BBAA | 7,504 | 0 | 42,680 |
| BBBA | 6,640 | 0 | 71,680 |
| BBBB | 42,720 | 0 | 404,800 |

For the five non-BBBB seam patterns this is smaller than the 307,736-clause,
124,216-variable generic counter and uses no new variables.  BBBB has more
clauses but still avoids the counter variables; its preprocessed comparison
is kept as an empirical choice rather than asserted from raw size.  The
production helper now installs these sparse consequences for every explicit
q3 pattern branch.  The independent census is

```text
scratch/audit_k16_q3_tight_palette_saturation_20260730.py
scratch/k16_q3_tight_palette_saturation_20260730.audit.json
  sha256 5cdb0fa44b8574a1554866d565fb5d5ae5ca183b9568203a4d17d5ea7b074c61
```

The overlapping multiplier-orbit branch flag is
`--preinstall-q23-orbit-branch PATTERN_A<node>`.  Unlike the old disjoint
63-case flag, it adds no non-invariant earlier-witness exclusions.  An initial
generic-counter baseline completed 18 cases (all patterns except BBBB) at 120
seconds each; all 18 were `UNKNOWN`, with no SAT or UNSAT claim.  It was then
stopped rather than spending another batch on an encoding already superseded
by the sparse theorem:

```text
scratch/k16_q23_generic_counter_baseline18_stats_20260730.audit.json
  sha256 0e46e9390ea6b98771c5f4414e68152e6d15e60fe87b5a61cb6e3f6ab452335f
```

A replacement seven-case pilot completed: each q3 pattern appeared once,
cycling through middle 380 with voltage set `{1,2,7,11}`, middle 378 with
`{1,2,4,7}`, and singleton 396 with voltage one.  It uses only pattern-
specific sparse saturation.  At most three single-threaded jobs run at once;
every SAT call is capped at 120 seconds and 4 GiB, and timeout/resource
termination is recorded as `UNKNOWN`.  Each case exports hashes of both the
original and CaDiCaL-preprocessed CNFs.  All seven calls timed out or hit the
resource cap and are therefore `UNKNOWN`; there is no SAT or UNSAT claim.
Against matching generic-counter cases, the five comparable non-AAAB formulas
use 72.2--72.9% as many variables and 93.5--95.8% as many original and
preprocessed clauses.  Conflict throughput ratios range from 0.99 to 1.93,
while propagation throughput ratios range from 0.66 to 1.16.  The structural
size reduction is robust, but the 120-second solver comparison is not
uniformly monotone and does not justify expanding the remaining 14 cases.

```text
scratch/k16_q23_stabilizer_sparse_pilot_stats_20260730.audit.json
  sha256 65b01adee467dff73d7f32f22e6dccf3234f81e973c2f653bf9c7ce4cf76e103
```

There is a second exact branch consequence.  Every non-`BBBB` one-block q3
provider contains exactly one cross-shore option.  The global carrier selects
exactly one option of that seam type.  Thus, after fixing a q3 shore-pattern
provider row, the selected seam must occur in the union of that row's provider
paths; every other option of the same seam type is exactly false.  The full
pattern rows allow only 72 of 3,432 seam options and produce 3,360 unit
clauses.  In `AAAB`, fixing the witness middle is stronger: the 80-prefix
middles 380, 384, 395, and 406 allow 48 seams and forbid 3,384; the other five
middles allow 64 and forbid 3,368.  `BBBB` has no cross-shore seam and receives
no such unit clauses.

For compressed `AAAB_A380`, these exact units increase base option variables
fixed false from 16 to 3,392 (all base fixed variables from 70 to 3,446).
Together with the independent one-step colour/order/history successor clauses,
CaDiCaL reduces the branch to 3,586,255 clauses.  The latter successor theorem
adds 22,400 long implications and is logically propagation-redundant; it is
kept distinct from the seam-domain theorem, which adds 3,384 unit clauses.

```text
scratch/audit_k16_q3_pattern_seam_domain_20260730.py
scratch/k16_q3_pattern_seam_domain_20260730.audit.json
  sha256 106d0613b3c3cfb243e5b1e3f7c71b14118628840349e4cb56735182522c716e
```

The fixed singular-q2 middle gives a separate exact binary relation.  A
positive q2 provider has the form

```text
predecessor -> fixed A middle -> successor.
```

Hamilton degree chooses exactly one incoming and one outgoing option at that
middle.  Therefore every option outside the two projections of the q2
provider relation is false, and every projected incoming/outgoing pair absent
from the provider relation is binary-incompatible.  Every exceptional middle
forbids 48 incoming and 48 outgoing options.  The four 80-provider middles
have 14 allowed options on each side and 116 incompatible pairs; the five
120-provider middles have 16 on each side and 136 incompatible pairs.  This
adds 96 units and 116 or 136 binary clauses, with no new variables.

```text
scratch/audit_k16_q2_middle_pair_domain_20260730.py
scratch/k16_q2_middle_pair_domain_20260730.audit.json
  sha256 54d24129b5c412b64de5751aa38ee664a916a1298bfd7c9a0dd1d9f9c9e0b9eb
```

The q3 seam also has an exact conditional neighbour domain.  Given a selected
seam, Hamilton degree uniquely chooses each immediate same-shore q3 neighbour.
If such an option never occurs next to that seam in the positive provider row,
the pair is binary-incompatible.  The whole-pattern counts are 2,880 (`AAAB`
and `BAAA`), 5,896 (`AABB` and `BBAA`), and 3,016 (`ABBB` and `BBBA`).  In a
middle-specific `AAAB` row they are 2,560 for an 80-prefix middle and 3,392
for a 120-prefix middle.  The cut has no variables.

```text
scratch/audit_k16_q3_seam_neighbor_domain_20260730.py
scratch/k16_q3_seam_neighbor_domain_20260730.audit.json
  sha256 9d2c095f4b68b3554af280148be5f81d7726a30ae43f2e85c6abdfe053853184
```

The second seven-pattern pilot used the seam-domain units and the independent
AAAB one-step successor implications, but predates the q2 pair-domain and q3
neighbour-domain clauses.  Again all seven calls were `UNKNOWN` at 120 seconds.
For the six seam patterns, CaDiCaL-preprocessed clauses fell to 94.5--95.2% of
the stabilizer+sparse formulas.  Conflict-throughput ratios were mixed:
`1.45, 1.72, 1.06, 0.63, 1.28, 0.90` in pattern order
`AAAB,AABB,ABBB,BAAA,BBAA,BBBA`.  This is a strong preprocessing improvement
but not a uniform proof-speed result.  The remaining 14 cases are therefore
not launched.

```text
scratch/k16_q23_stabilizer_sparse_seam_pilot_stats_20260730.audit.json
  sha256 1af83453533267d38214e9f2bb53f7f3bc5652d0cc3957d7b2f02ac63bd21754
```

No timeout in either pilot is interpreted as evidence for satisfiability or
unsatisfiability.

A build/preprocessing smoke test of the final local-cut stack (without a long
SAT run) passed for `AAAB_A380`, `AABB_A380`, and `BBBB_A380`.  Relative to the
seam pilot, their preprocessed clause counts fell respectively by 1,486,
8,480, and 18,494.  Since `BBBB` has no seam, its entire reduction from
4,226,706 to 4,208,212 clauses comes from the 212-clause q2 pair relation.
This is the clearest measured evidence that the small exact relation is
exposing consequences that generic DNF preprocessing missed.

Finally, the seam collar gives an exact alternative encoding, not merely
redundant cuts.  Once the unique seam is selected, Hamilton degree determines
the immediate rail neighbour(s), then the next neighbour in an endpoint-seam
pattern.  The positive q3 provider DNF is extensionally equivalent to a
variable-free finite-table encoding: binary projection exclusions followed by
ternary incompatible-pair exclusions.  Exhaustive enumeration verifies exact
equality with the provider set.  The direct clause counts are 13,400 for
`AABB/BBAA`, 51,624 for `ABBB/BBBA`, and 55,552 for `AAAB/BAAA`; `BBBB` has no
seam and is outside this reduction.  This encoding has not replaced the
production DNF yet.  `AABB/BBAA` are the clearest pilots because their direct
table has essentially the same clause count while eliminating 1,984--2,176
q3 auxiliary variables.

```text
scratch/audit_k16_q3_direct_seam_collar_20260730.py
scratch/k16_q3_direct_seam_collar_20260730.audit.json
  sha256 e0cc202211aeb43bf52b12f0e3480f84de9f1dff27bd420d6d124875a0aba87f
```

The replacement is implemented behind
`--replace-q3-seam-dnf-with-collar`; the DNF remains the default.  A remote
`AABB_A380` build/preprocessing smoke gives 320,832 variables and 3,597,602
preprocessed clauses, versus 323,008 and 3,600,531 for the all-local-cut DNF.
Thus the exact table removes all 2,176 q3 auxiliaries, 5,441 raw clauses, and
2,929 post-preprocessing clauses.  This is a formulation comparison only, not
a SAT/UNSAT result.
