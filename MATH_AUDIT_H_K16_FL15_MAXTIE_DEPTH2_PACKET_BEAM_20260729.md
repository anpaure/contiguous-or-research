# Lane H audit: the Hamilton `FL15` maximum-tie depth-two packet beam

Date: 2026-07-29  
Status: exact search specification, locally replayed plan, and a certified
depth-two path `15 -> 12 -> 9`; the exhaustive all-tie beam has not been
launched under the active H100 memory freeze.

## 1. Frozen input

Let `R` be the fixed resident factor reconstructed from the three PBBS
artifacts, and let `Q_15` be

```text
scratch/k16_q1_endpoint_resume1_failedlit15_20260729.json
SHA-256 80d79467973fa724a938f0c7ab7d0df4c9ce81dfcb16a04fb3a85c42da2c7819.
```

Direct factor replay gives one physical cycle of length `12870`, zero lower
or upper `q1` holes, and `2233` short old-coordinate runs, with histogram

```text
length 1: 132,   length 2: 906,   length 3: 1195.
```

The complete scoped failed-literal bank is

```text
scratch/k16_failedlit15_fullbank_20260729.audit.json
SHA-256 a769feaddb08104e55993d27d773048a967cd824a1728ac8e90bc133dbf8ff00.
```

It has `503` unhit two-live-variable motif rows, `956` distinct candidate
variables, all `956` probed, and exactly `15` variables for which both
Boolean assumptions give a recursively certified unit-propagation
contradiction.  Write this count as `Phi(Q_15)=15`.  This is an exact
infeasibility certificate when positive.  It is not a complete feasibility
test: `Phi=0` would only mean that this particular complete 956-variable
bank has no double failure.

## 2. Maximum-incidence focus

For a double-failed variable `v`, let `K_v` be the union of the deterministic
recursive core rows returned for assumptions `v=0` and `v=1`.  A current
blue edge is counted once for `v` when it occurs in any row of `K_v`.
Let `w_Q(e)` be the resulting number of failed variables using `e`.

For `Q_15`,

```text
max_e w_Q(e) = 4,
```

and exactly the following 30 edges attain the maximum:

```text
(15032,47288) (18558,26718) (19644,22716) (22716,30876)
(26718,27678) (31524,64260) (36021,44197) (36021,51381)
(39100,40116) (39100,47260) (40085,40116) (40120,47288)
(45734,61990) (45838,58126) (47878,47884) (47884,63756)
(51358,59422) (55846,59942) (56084,64260) (57902,57998)
(57902,61994) (57998,58250) (58022,59942) (58126,58638)
(59422,59478) (59918,59948) (59918,63502) (61990,62052)
(64036,64040) (64036,65028).
```

Thus a `top 9` rule is mathematically arbitrary at this state.  The new
driver retains the entire maximum tie.  At every retained child it
recomputes the complete failed-literal bank and again uses every edge at the
new maximum, whatever the new maximum or tie size may be.

## 3. Exact packet enumeration lemma

**Lemma 3.1 (focused closed-trail completeness).**  Fix a physical Johnson
2-factor `Q`, an edge `e` of `Q`, and `r` in `{2,3,4}`.  The routine
`connected_alternating_trades(e,r,...)` enumerates every connected,
edge-simple alternating closed-trail switch containing `e` that deletes
exactly `r` edges of `Q` and adds exactly `r` non-`Q` Johnson edges.
Conversely every returned pair has equal deleted and added incidence at
every vertex, so switching preserves the spanning degree-two equations.

**Proof.**  Orient an eligible alternating closed trail in either direction
from `e`.  After deleting the oriented copy of `e`, the trail alternates

```text
new Johnson edge, old Q edge, ..., new Johnson edge, old Q edge,
```

for `r-1` pairs and then closes by one new Johnson edge to the initial
vertex.  The recursion tries both orientations of `e`, every Johnson
neighbour at each new-edge step, and both current `Q` neighbours at each
old-edge step.  Its edge-disjointness tests are exactly the edge-simple
condition, and the final test is exactly Johnson closure.  Hence it reaches
the oriented presentation of every eligible trail.  Conversely, along a
returned closed alternating trail each visit contributes one deleted and
one added incidence, including at a repeated support vertex.  Therefore the
two incidence vectors agree.  QED.

The family contains every simple alternating `C4`, `C6`, and `C8`.  It also
contains valid repeated-vertex packets, such as an alternating bow-tie; the
report does not mislabel those as simple graph cycles.  Disconnected unions
and radii outside `{2,3,4}` are not enumerated.

**Lemma 3.2 (hard immediate-shadow preservation).**  A returned packet is
accepted only if the switched factor has every lower and every upper `q1`
colour.  Thus every scored beam state is an exact q1-complete physical
2-factor.

**Proof.**  For each colour used by a deleted edge, the filter subtracts the
deleted multiplicity from its current load and adds the new multiplicity,
requiring the result to be at least one.  Colours not used by a deleted edge
retain their positive old load.  A subsequent independent compact factor
audit rejects any state with a lower or upper hole.  QED.

Here “preserves q1 exactly” means the two complete physical colour supports
are hard constraints.  It does not mean that every colour multiplicity is
unchanged.

## 4. Depth-two retention rule

For every live scored state define the coordinatewise-minimized vector

```text
(Phi, residence violations).
```

Component count is excluded from Pareto dominance and used only as a
secondary deterministic display tie-break; q1 completeness is not an
objective but a hard admissibility condition.  The unhit-two-choice count
and candidate-bank size are reported as diagnostics, not minimized: making
the state-dependent candidate universe smaller is not a proved improvement.

At depth one the driver retains

every live state with `Phi <= 17`, including neutral `15` states and mildly
uphill `16,17` states.  No state above this hard ceiling is rescued merely
by residence or component count.  The coordinatewise Pareto subset of the
retained band is recorded, but the whole band is expanded.

Every retained state is expanded once using its own newly recomputed
maximum-incidence tie.  A strict success is any evaluated live state at
depth one or two with `Phi<15`.  The report preserves all strict-improvement
move sequences, the physical edge set of the best one, and the Pareto set
over every evaluated live state at depths zero through two.

This is deliberately a beam, not an exhaustive two-move theorem.  A
depth-one state with `Phi>=18` is not expanded, and there is
no proved continuation monotonicity of the displayed vector.  The search
also omits packets avoiding the current maximum-incidence tie.  Therefore a
negative beam result would be a no-go only for this serialized adaptive
family and retention rule.

## 5. Certified in-beam path `15 -> 12 -> 9`

Two already frozen simple alternating `C8` packets form a literal path in
the new beam.

The first packet is

```text
delete (7350,7860), (7356,15420), (15414,15540), (39100,40116)
add    (7350,15414), (7356,39100), (7860,40116), (15420,15540).
```

It hits the FL15 maximum-tie edge `(39100,40116)`, preserves both q1
supports, changes the component census `1 -> 2`, improves residence
`2233 -> 2231`, and gives `Phi: 15 -> 12`.  Since `12<=17`, the hard band
retains this child.

At FL12 the maximum proof incidence is again four, now attained by 21
edges.  The second packet is

```text
delete (43813,47877), (47629,64012), (47653,64005), (47878,47884)
add    (43813,47653), (47629,47884), (47877,47878), (64005,64012).
```

It hits the FL12 maximum-tie edge `(47878,47884)`, preserves both q1
supports, keeps two components, improves residence `2231 -> 2230`, and gives
`Phi: 12 -> 9`.  Both packet supports have eight distinct vertices, so they
are genuine simple `C8` switches, not repeated-vertex trails.

The independent solver-free replay checks literal edge-set equality with the
frozen FL12 and FL9 endpoints, degree balance, connectedness, Johnson
adjacency, q1 completeness, fullbank bindings, and both maximum-tie
memberships:

```text
scratch/audit_k16_fl15_to9_maxtie_depth2_path_20260729.py
SHA-256 ef5f26d371a34da98f8ff4cddc8d20df275c018f7b53d3892b74501ec022746b
scratch/k16_fl15_to9_maxtie_depth2_path_20260729.audit.json
SHA-256 8f490b922657dc4484531a880422fc6e16f7e021876f0fc8653dc42cae683dee.
```

Thus the requested beam has a proved strict depth-two outcome, `Phi=9`,
even without running the exhaustive 30-way catalogue.  This remains a
failed-literal-census descent, not a resident completion or feasibility
proof.

## 6. Proof-safe replay provisions

The full run, before enumerating a packet, independently reconstructs `R`
and `Q_15` and checks:

- the endpoint, resident-selection, catalogue, and all three reconstruction
  input hashes;
- the complete-bank schema, `956=956` probe census, and uniqueness of probe
  variables;
- the exact 15 failed-variable identities;
- a canonical SHA-256 of both deterministic branch-core row sets for all 15
  failures; and
- the complete 30-edge maximum-incidence tie above.

The report hashes the driver and six critical direct/transitive helper
modules.  At each layer it also emits a canonical transition-manifest hash
and a scored-candidate-manifest hash.  These hashes make a later independent
replay sensitive to omitted or altered transitions, scores, or helper code.

The locally audited plan is

```text
scratch/k16_fl15_depth2_pareto_packet_beam_20260729.plan.json
SHA-256 c417752fb335d698c1c7cbfca6a8aaeac29ac63bf41c4f6a07da1ef679d5547b.
```

The driver is

```text
scratch/search_k16_fl15_depth2_pareto_packet_beam_20260729.py
SHA-256 ef906af32791793a2d58041a39a7fd5bbe90304742ff79c534e12b1e1b50395d.
```

The driver compiles, and local `--plan-only` replay reproduces
`Phi=15`, Hamiltonicity, q1 completeness, residence `2233`, and the exact
30-way count-four tie.  Non-plan execution is guarded to the H100 CPU host.
It has not been launched because the explicit H100 memory/swap freeze remains
active, and the full candidate/propagation beam would violate the prohibition
on heavy local work.

The full driver contains the certified FL12 and FL9 state digests as mandatory
regressions: a full run aborts if either leaves its corresponding layer or if
its exact score changes.

## 7. Exact execution command after recovery

```text
python3 scratch/search_k16_fl15_depth2_pareto_packet_beam_20260729.py \
  --resident scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json \
  --q1 scratch/k16_q1_endpoint_resume1_failedlit15_20260729.json \
  --fullbank scratch/k16_failedlit15_fullbank_20260729.audit.json \
  --base scratch/k15_pbbs_trade_baseline.json \
  --b-certificate scratch/k16_pbbs_component_trade_27_factor_20260729.json \
  --a-cycles scratch/k15_two_component_a_cycles_20260729.json \
  --output scratch/k16_fl15_depth2_pareto_packet_beam_20260729.json \
  --first-step-slack 2 --workers 4
```

No optimal `k=16` word, resident completion, compiler, or constant-one
theorem follows from the plan alone.
