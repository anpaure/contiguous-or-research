# K17 complement-dual zero-rectangle certificate and singleton topology LNS

Date: 2026-08-01  
Lane: K / exact complement-dual topology  
Status: the literal support-four faces are closed exactly for one authenticated
seed.  Radius-two fixed-exterior topology LNS is DRAT-verified UNSAT.
Radius three is `UNKNOWN` after the declared cap.  No statement here is a
global K17 impossibility result.

## 1. Authenticated seed and corrected topology

The input matching is

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/best.tsv
SHA256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

It chooses one incidence perfect matching `D`; the other matching is
`H=C(D)`.  Independent literal reconstruction gives:

* two `A=C D` cycles of lengths `1429,1`;
* two `A^2=H^{-1}D` factor components of lengths `1429,1`;
* `A^2` component voltages `4,9` modulo 17;
* all 1,144 rank-ten and all 1,144 rank-seven quotient colours covered;
* 286 repeat units on each immediate palette.

Thus the earlier `715+715` parity picture does **not** describe this seed.
That picture applies only after `A` itself is Hamilton.

## 2. Exact two catalogues

Let `s` be the singleton `A` owner.  There are 1,429 possible pairs
consisting of one matching edge on the singleton component and one on the
large component.

### 2.1 Dual-preserving `D` rectangles

For old edges

```text
d0=(x0,f0), d1=(x1,f1),
```

a two-edge assignment switch would require literal crossed incidences

```text
c0=(x0,f1), c1=(x1,f0).
```

If they existed and `D'` contained no complementary edge pair, then swapping
the two `A` heads would join the two odd `A` cycles into one Hamilton cycle.
The new `A` voltage would be

\[
 v(A')=v(A)-v(d_0)-v(d_1)+v(c_0)+v(c_1)\pmod {17}.
\]

The exact incidence atlas contains **zero** such crossed pairs among all
1,429 choices.  Hence no support-four, complement-dual, two-edge switch can
join this seed's `A` cycles.  Palette constraints are never reached.

### 2.2 Non-dual `H` rectangles

Keep `D`, remove one `H` edge from each factor component, and cross their
facet ends.  Again the complete physical incidence atlas contains **zero**
crossed pairs among all 1,429 choices.  Hence the direct non-dual two-edge
splice is also absent before voltage or palette screening.

This is stronger than a palette failure and weaker than a general splice
no-go.  In either matching fibre, a successful alternating change must use at
least three old and three new incidence edges, or must first change the seed.

The catalogue replays the two shore-tagged provider ledgers separately.
This is important: an upper loss and its complementary lower loss are two
coverage inequalities, not one untagged multiplicity subtraction.

Frozen remote output:

```text
/home/amodo/or15/work/laneK_dual_rectangle_20260801/seed.audit.json
SHA256 dabd166abab176b3b921cec95f4cf7f8d66671cfc509cd1ba14bfa602f0717b1
```

## 3. Matching-contracted singleton halo

Write the seed permutation as a perfect assignment from tail owners to head
owners.  Contract each selected seed arc.  A candidate odd-graph arc
`u -> h` becomes an edge from root `u` to root `A^{-1}(h)`.  Forgetting its
orientation gives the **incidence-alternating root graph**.

For radius `r`, let `R_r` be the roots at graph distance at most `r` from
the singleton root.  The exact LNS face leaves an `A`-arc variable free iff
both its tail root and its contracted head root lie in `R_r`.  Every other
arc is pinned to its authenticated seed value.  Therefore every allowed
symmetric-difference assignment circuit is wholly contained in `R_r`, and
every such circuit is retained.

The base model is the direct-`A` exact-cycle master, not the matching master
with a `D<->H` orientation symmetry break.  It retains exactly:

1. one incoming and one outgoing arc at every owner;
2. distinct incoming/outgoing labels, equivalently `D cap C(D)=empty`;
3. every rank-ten quotient row (rank seven follows by complement);
4. one Hamilton `A` cycle.

There is consequently no invalid global orientation-breaking clause in the
fixed-exterior face.

Exact halo sizes are:

| radius | released roots | free `A` arcs | boundary arcs | CNF clauses |
|---:|---:|---:|---:|---:|
| 2 | 146 | 612 | 1,404 | 937,649 |
| 3 | 771 | 4,976 | 3,926 | 933,285 |

The nonmonotone clause counts are correct: the larger halo needs fewer unit
pins.

An independently written scope auditor reconstructs the seed, contracted
root graph, BFS balls, and every free/pinned variable.  It returns `PASS` with
the same counts.  Its hashes are

```text
source       d9650e0482fca52efe1858928763f80298fab7c931915b98b25d5578ad9cd944
radius 2     409e2ac84a871dca38c30b41e1efb20f89a42d00aed6ea072c46920553f82806
radius 3     dd4b07140c446e6b8b1f46d56c80ac5f904e33bc6b85b406337469584e35e9cf
```

The radius-two ball contains every single seed-relative exchange cycle
through the singleton using at most five changed roots; radius three contains
every such cycle using at most seven.  Neither ball contains an exchange that
leaves the ball and is balanced by a disjoint remote circuit.

## 4. Radius-two exact result

The radius-two CNF is UNSAT.  A second Kissat run emitted a DRAT proof, and
`drat-trim` independently returned `s VERIFIED`:

```text
CNF    8604ff265946fbaf4601572a854a6a6d1a3df4c6f7d7098714a50c3e1ae9f923
proof  16d7bfd326a4378a2a7eded90a59099fab5d1118075e83226b456a17cdc40054
verify 3ca7b7ea3c74b37801535bd5bbf2d94f5d1538c6118a4e7ab00142032edb69aa
```

The verified core has 7,270 original clauses, 2,071 lemmas, and 25,040
resolution steps.  The conclusion is precisely:

> No rank-ten-surjective, complement-dual Hamilton `A` is obtainable while
> fixing every assignment arc outside the radius-two singleton halo.

It says nothing about radius three, another seed, a non-complement-dual
factor, residence, deletion spines, deeper upper shadows, or the compiler.

## 5. Radius-three status

The exact-order radius-three formula ran for 600 seconds with one CPU,
`nice 15`, and a 4 GiB virtual-memory cap.  It exited `124` without a model or
an UNSAT line.  Therefore its status is exactly `UNKNOWN`.

```text
CNF 0645c22a42c55d3f015d7597603411b5e29785c8aecdcceae37af2639b8a2356
build audit f79a13b97d9ca840d622f46acb1dbd4ac56365613ce42489fca979b09f93b183
scope audit dd4b07140c446e6b8b1f46d56c80ac5f904e33bc6b85b406337469584e35e9cf
```

Kissat wrote a 2,645,557,248-byte partial DRAT stream before timeout.  It was
incomplete, was never passed to a verifier, and is not evidence of UNSAT.
On the user's later resource-cleanup instruction it was deleted, while its
CNF, halo, build/scope audits, stdout/stderr, exit code, and lazy-probe logs
were retained.  Its former path was

```text
/home/amodo/or15/work/laneK_dual_rectangle_20260801/radius3.proof.drat
```

A smaller lazy-subtour formulation was also given one 90-second first-round
probe.  It likewise exited `124` before producing a cycle cover.  No further
solve was launched.

## 6. Artifacts

Local sources:

```text
scratch/catalogue_k17_direct_A_nondual_splices_20260801.cpp
scratch/audit_k17_direct_A_nondual_splice_factor_20260801.cpp
scratch/build_k17_direct_A_topology_lns_20260801.cpp
scratch/audit_k17_direct_A_topology_lns_scope_20260801.cpp
scratch/audit_dimacs_complete_model_20260801.cpp
```

Current source hashes are, in the same order,

```text
2c0dbb5b729d809438c4ef97ca4bdef4330772638c143c12a645cdf852a6d87a
da2f3a9cef363e22e9a83088887d63757e368b7c1b364376aee36f43678d2195
6835a6c22487555fa33484adcccc394bb5289b7731e37f4a92051e3d3dc0c51d
d9650e0482fca52efe1858928763f80298fab7c931915b98b25d5578ad9cd944
99cbe61c98c1a1b31429d7c11c8db7bb21e8f91b784a33ba2a32806b77960ea3
```

Remote run directory:

```text
/home/amodo/or15/work/laneK_dual_rectangle_20260801/
```

The small build, scope, solver-status, and DRAT-verification logs are frozen
locally under

```text
scratch/k17_dual_rectangle_singleton_lns_20260801/
```

`SHA256SUMS.txt` in that directory verifies all local files; remote-only
large-object hashes and the explicit incomplete-proof warning are in
`REMOTE_OBJECTS.txt`.

The standalone factor auditor rebuilds all selected turns and the physical
17-fold cycle for a future non-dual survivor.  It was not invoked on this seed
because both rectangle catalogues are empty.

## 7. Remaining exact gate

The first open topology face for this seed is a longer alternating assignment
circuit through the singleton.  Radius three is the next complete induced
halo, not a claim that support six suffices.  A SAT model must be replayed
against the full CNF, decoded as a literal Hamilton `A`, checked for nonzero
voltage, and only then passed to residence/deletion-spine/deeper-opening
audits.

## 8. Candidate-B fixed-`D`, `H`-only provider halo

The later connected candidate-B factor is

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/dual_splice_dev5_20260801/seed17931.minimum_debt_assignment_cycle.factor.tsv
SHA256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

It has one quotient factor cycle, voltage 9, all 1,144 upper colours, and
exactly the two missing lower colours `0x00e0f,0x01547`.  Fix `D`.  For each
admissible non-`D` incidence `e`, let

* `u(e)` be the `D`-root of the facet of `e`;
* `h(e)` be the owner of `e`;
* `v(e)` be the seed predecessor of `h(e)`.

Thus `e` is the relative-assignment arc `u(e)->v(e)`.  There are exactly 20
arcs whose fixed-`D` lower label is one of the two missing colours.  Their
tail and displaced-predecessor endpoints comprise 34 distinct roots.

The exact radius-`r` provider halo is the ball around those 34 roots in the
undirected graph of **non-`D`** relative-assignment arcs.  An `H` incidence
is free exactly when both of its relative endpoints lie in the ball; every
other non-`D` incidence is pinned to its seed value.  The master then imposes

1. one selected `H` incidence at every owner and every facet;
2. all fixed `D` incidences false;
3. all 1,144 lower and all 1,144 upper palette ALO rows;
4. a guarded binary MTZ ordering making `H^{-1}D` one quotient Hamilton
   cycle.

This is exact for the stated induced halo.  Voltage, residence, deeper
shadows, openings, and the compiler are deliberately absent, so UNSAT is a
valid local no-go while SAT would only be a topology/palette candidate.

An initial implementation accidentally allowed the forbidden `D` incidences
as BFS links.  That safe over-approximation released 351 roots.  It was not
used as the canonical statement.  The corrected builder asserts the literal
hole identities and excludes every `D` incidence from the provider graph,
free-variable counts, boundary counts, and exterior-pin counts; the original
global unit clauses still forbid all `D` variables.  Its SHA256 is

```text
475a9542cf9f71311ac48bf7287d3374a14d69b627a0af6718e6e48f865ff7ed
```

Independent reconstruction gives:

| radius | starts | released roots | feasible free `H` edges | boundary edges | variables | clauses |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 34 | 332 | 1,356 | 2,600 | 44,330 | 659,786 |
| 2 | 34 | 1,266 | 9,246 | 1,764 | 44,330 | 651,896 |

The exact radius-one formula is UNSAT.  A second run emitted an ASCII DRAT
proof and `drat-trim` returned `s VERIFIED`.  In fact the contradiction is
unit-propagational after fixing the exterior: the extracted core has 686
original clauses and one core lemma, with 686 resolution steps.

```text
radius-1 CNF       014b7d3d6fd96ef887d38af1a8645bb20d4f10f0357e497cd6b7fe80575f1a1a
radius-1 proof     8290784b5cca107fb283bf438da494492265b73e56da5ae93e1f1a256435740f
verification log  f7c64b407a3e67ca96629fe9b2ec09acc87fe64a12a4fa23d95ae03f3b883858
core CNF           10e2647bb518ce69e800880b3b932d8c394e948c576337977e62447ccc90a08b
```

Therefore no fixed-`D`, `H`-only repair lying in the exact radius-one
provider halo can simultaneously fill both lower holes, retain every upper
colour, and remain a single quotient factor cycle.  This does not rule out
radius two, a disconnected relative change followed by another circuit,
changing `D`, or a mixed `D/H` packet.

The 686-clause core contains no MTZ/order variable: its maximum variable is
12,869, within the incidence block.  It consists only of fixed-exterior or
`D` units, owner/facet matching rows, 34 lower-palette rows, and 27
upper-palette rows.  The missing-lower row `0x00e0f` occurs in the core but
`0x01547` does not.  Unit propagation ultimately forces two different
incidences, variables 3,516 and 3,831, into facet 315 (physical facet mask
3,975), contradicting that facet's AMO row.  Thus Hamiltonicity is not the
radius-one obstruction, and the same core remains UNSAT even if the
`0x01547` coverage demand is removed.  The independently replayable semantic
classification is deliberately scoped to this extracted core; DRAT remains
the proof authority.

The exact radius-two model was given one 300-second, single-core, `nice 15`,
8-GiB-address-space run.  It exited 124 with empty stdout/stderr, no model,
no UNSAT line, and no proof.  Its status is exactly `UNKNOWN`; no further
solve was launched.

The canonical remote directory is

```text
/home/amodo/or15/work/laneK_dual_rectangle_20260801/
```

The first safe over-approximation and its complete proof were retained under
`allincidence_overapprox/`; only the unrelated incomplete radius-three proof
described in Section 5 was deleted.

The new local sources and frozen small package are

```text
scratch/build_k17_fixed_D_H_palette_halo_master_20260801.cpp
  475a9542cf9f71311ac48bf7287d3374a14d69b627a0af6718e6e48f865ff7ed
scratch/audit_k17_fixed_D_H_palette_halo_scope_20260801.cpp
  949260250cc84d3335878b09325f7cc6f5cfb1b5471c165f759298189b013c25
scratch/audit_k17_fixed_D_H_provider_core_semantics_20260801.py
  5f67ff30c7297649c1866e289a2c9984a19ef59e871a2dedc8472340a2c4ee89
scratch/k17_fixedD_H_provider_halo_20260801/
```

The independent scope-audit payload hashes are
`053ea4b2f7e90ea524168d9d8f583a5fb94abc45ae6cbd70f079178602144d74`
for radius one and
`6d7be29d4a0461a19b748ae69190c06f5e82042377253a929a3f1770301640f8`
for radius two.  They reconstruct all atlas labels, palette groups, provider
starts, non-`D` BFS distances, free/boundary/pin sets, map and halo rows, and
the DIMACS envelope from the authenticated factor before returning `PASS`.
