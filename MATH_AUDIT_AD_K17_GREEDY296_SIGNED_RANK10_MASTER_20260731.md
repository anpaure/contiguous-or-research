# Independent audit: greedy296 marked-preserving signed-rank10 master

Date: 2026-07-31  
Status: **PASS for the stated rank10/factor scope; no feasibility result**

## 1. Scope

This note audits the frozen greedy296 exchange master without invoking
OR-Tools or a solver.  It independently parses the exported binary
`CpModelProto`, reconstructs every exchange column from the literal owner
cycle, checks every coefficient in every hard row, checks the objective and
partial hint, and replays the post-connectivity chronology evaluator on the
frozen base.

The proved scope is the marked/cross-frozen, complement-rethreaded,
lower-rainbow factor with complete **linear-zipper rank10** coverage and lazy
one-cycle cuts.  Residence, ranks 11 and 12, maximal-envelope inversion, and
common-cap Hall are not hard rows of the exported proto.  They are separate
literal post-materialization tests.  In particular, this audit is not a K17
word certificate and does not assert that this master is feasible.

## 2. Authenticated greedy296 base

The audited inputs are:

| artifact | SHA-256 |
|---|---|
| frozen generic core | `6ecf1cf02cb3791333816b058ceb1e415331274d8bc4e2dcde93ea4e87c89a1e` |
| greedy296 wrapper | `a5ce3d8437fd1c4e6babf33aa72bfb0ed1273b89a2116632d0d193973a744b02` |
| build result | `4c992430ce8fad42d3f0ef412a021a8dbc35de8fcfb343eb8f4848e91f1e2516` |
| binary proto | `9ffdf790808361d0d84a1c0428958610a0e75da56d833eb0359b0534de7697be` |
| greedy296 occurrence flow | `079f5cd96f713ef2d72dd43acff10f84416acdb670aeff96f61a3cb97f29c25f` |
| corrected residual bflow v2 | `63b49db80ad983bcd440aba3ac4b449888e30dea2d3c83e140e15b07082f69d0` |
| literal owner cycle | `801896cd15cc6b0b202db75421b93c1dc0e13a33b67fbc902ce283e242c381a6` |
| compact exchange catalogue | `c31071269fb709d28887e5d3590be15d5af727560809c8476dd2981ef546ea2a` |

The corrected v2 residual has 4,872 assignment rows, assignment payload
`327d60f1f1d072b3bcb60e84404e52f346e25a98499fcf688fde842cddf67a8c`,
flow value and demand both 9,744, and one residual cycle.  Its assignment rows
and switch rows are byte-semantically identical to the earlier residual with
SHA `c32349f7...`; v2 corrects the flow provenance pin to `079f5cd...`.

The owner-cycle replay gives 24,310 distinct rank9 owners and every rank8
intersection exactly once.  The two bank-crossing edges delimit one frozen
4,108-owner marked path and a 20,202-owner complement.  There are exactly
4,107 marked-internal, 20,201 complement-internal, and two cross edges.  The
linear closing edge is

`{7418,71930}`

and is the unique physical owner edge omitted from the linear zipper.

### Provenance qualification

The compact catalogue's historical metadata names the old residual SHA
`c32349f7...`, but its actual semantic base is the newly frozen owner-cycle
SHA `801896cd...`; all groups are reconstructed from that cycle.  The old and
v2 residual assignment rows are identical, and the wrapper separately checks
the v2 SHA and its current flow pin.  Therefore no stale exchange delta enters
the model.  For cleaner future provenance, the build JSON should echo the v2
residual SHA explicitly rather than relying on the wrapper hash and cycle
hash.

## 3. Exact exchange equations

For each mutable complement-internal rank8 colour `c`, let `e_c={a_c,b_c}`
be its incumbent owner edge and let

`V_c={v in complement : c subset v}`.

For every unordered pair `f={u,v}` from `V_c` other than `e_c`, introduce
`x_(c,f)`.  Introduce `y_c` to say that `e_c` is replaced.  The exported hard
system is exactly

`sum_(f != e_c) x_(c,f) - y_c = 0`                                            (C)

for each mutable colour,

`sum_(c,f : w in f) x_(c,f) - sum_(c : w in e_c) y_c = 0`                     (D_w)

for each complement owner `w`, and

`b_T + sum_(c,f : union(f)=T) x_(c,f)
     - sum_(c : union(e_c)=T) y_c >= 1`                                        (U_T)

for every rank10 target `T`.  Here `b_T` is the number of exposed incumbent
owner edges with union `T` after omitting the frozen closing edge.

There are exactly 20,201 equations (C), 20,202 equations (D_w), and 19,448
inequalities (U_T).  The complete exchange universe has 545,721 `x` columns;
its reconstructed stream hash is

`ab27e28d780ab036669ae8d1fc058b150d585343b684ed4426e6411442b835af`.

### Theorem 3.1 (factor exactness)

For Boolean variables, equations (C) choose either the incumbent edge or one
alternative edge for every mutable lower colour.  Equations (D_w) are
necessary and sufficient for every complement owner to retain degree two.
Together with the 4,109 frozen marked/cross edges, every solution is therefore
a spanning lower-rainbow 2-factor, and every marked-preserving lower-rainbow
2-factor occurs in this system.

**Proof.**  Any two distinct rank9 supersets of rank8 `c` have intersection
exactly `c`; hence the catalogue lists every and only possible replacement of
`e_c`.  Equation (C), with Boolean `y_c`, allows at most one.  The incumbent
already has degree two.  Equation (D_w) is precisely new incidence minus
deleted incidence at `w`, so it preserves degree two.  The marked and cross
edges cannot change.  Conversely, any factor in the stated face chooses one
listed pair for each changed colour and satisfies these incidence equations.
∎

### Theorem 3.2 (boundary-correct rank10 identity)

Let the decoded linear row be

`Z = P_1,...,P_a,F_0,...,F_b`,

where the `P` are the marked rank9 path and the `F` are the distinct rank8
edge facets along the complement rail, including its two boundary facets.
Then the rank10 interval set of `Z` is exactly the set of unions of the owner
edges in the final cycle other than the closing edge `Q_b P_1`.

**Proof.**  A marked internal edge is exposed by its two adjacent `P` tokens.
The outgoing marked-to-complement edge is exposed by `P_a,F_0,F_1`.
Every complement-internal edge is exposed by the three consecutive facets
around it.  Consecutive facets are distinct lower colours and unite to their
shared rank9 owner, so the corresponding triple unites to the rank10 union of
the intervening owner edge.  The closing edge would require cyclic wrap and
is not exposed in the linear row.

Conversely, any interval whose union first reaches rank10 either contains two
consecutive marked owners or contains a three-facet local witness (with the
same boundary interpretation).  That local owner-edge union is a rank10
subset of the interval union and hence equals it.  ∎

Thus all 19,448 signed rows (U_T), including supported targets whose incumbent
witness may be deleted, are necessary and sufficient for rank10 coverage.
The frozen base has 1,908 such holes.

## 4. Serialized-proto audit

The binary proto was parsed directly at protobuf wire level, without
OR-Tools.  It contains:

| item | exact count |
|---|---:|
| exchange Boolean variables | 545,721 |
| changed-colour Boolean variables | 20,201 |
| total Boolean variables | 565,922 |
| colour-choice rows | 20,201 |
| owner-degree rows | 20,202 |
| rank10 rows | 19,448 |
| total constraints | 59,851 |

Every variable domain is exactly `[0,1]`.  Every constraint is linear.  For
each of the 59,851 constraints, the independent parser checks every literal
index, sign, target/owner incidence, domain endpoint, and completeness count.
The objective has exactly the 20,201 `y_c` variables with coefficient one and
scaling factor one.  It therefore minimizes the literal number of changed
complement colours, not the number of components or a shadow proxy.

The build-only proto contains no component cuts.  This is expected: component
cuts are generated after disconnected incumbents are returned.

## 5. Direct hint audit

The hint contains 1,908 exchange variables and their 1,908 corresponding
changed-colour variables, all hinted true; all other variables are left
unhinted.  The exchange groups and targets are distinct.  Replaying the
signed deltas leaves every one of the 19,448 rank10 rows positive.

It is not a physical factor: its endpoint imbalance is nonzero at 4,195
owners with `L1=4,536`.  Accordingly, the 1,908-row object is only a partial
rank10 hint and supplies no feasible objective upper bound.  The frozen
wrapper labels it that way.

## 6. Connectivity and exact-choice CEGAR

For any returned degree-two incumbent and any one of its components `S`, the
core adds the exact signed cut

`|delta_base(S)| + gains_x(S) - losses_y(S) >= 2`.

It includes frozen, deleted, and added edges with their literal signs.  Every
connected factor satisfies it, while the current disconnected component has
cut zero.  Iterating these ordinary component cuts is therefore sound and is
complete for one-cycle connectivity if allowed to continue.

The final-choice no-good also has exact semantics.  It contributes one
literal per mutable colour: `not x_(c,f)` for the selected replacement, or
`y_c` if the incumbent was kept.  It excludes exactly that colour-choice
assignment.  In the present unsplit model there is no additional split
literal.  I find no duplicated selected-exchange literal in the frozen source;
even if a Boolean disjunction contained a duplicate, it would be logically
idempotent.

## 7. Literal chronology replay

After a connected factor is decoded with the frozen marked orientation, the
core reconstructs the literal nonflat row, then independently performs:

1. strict D2 run audit at threshold three;
2. D3 adjacent-union audit at threshold four;
3. maximal three-window erosion envelopes with both suffix corrections;
4. exact row-by-row inverse replay;
5. exhaustive monotone interval scans through ranks 10, 11, and 12; and
6. scalar common-cap diagnostics.

On the frozen greedy296 base, the independent replay exactly returns:

| metric | value |
|---|---:|
| empty maximal envelopes | 0 |
| inverse replay mismatching rows | 2,769 |
| inverse replay missing bits | 2,901 |
| strict D2 short runs | 1,875 |
| strict D3 short runs | 1,874 |
| rank10 holes | 1,908 |
| rank11 holes | 929 |
| rank12 holes | 149 |
| host redundancy | 256,785 |
| envelope volume | 150,843 |
| minimum envelope size | 6 |

The hard model does **not** linearize ranks 11/12 or residence.  A connected
candidate failing any literal gate receives an exact whole-assignment no-good;
this is an exact but potentially weak CEGAR scheme.  The heuristic frontier
orders D2 short runs but not the separately reported D3 count.  Sound final
acceptance is unaffected: zero D2 inversion triggers an independent assertion
that D3 is also zero.

The common-cap object is not solved.  For the base it reports only scalar
values: 7,401 available cells, 4,108 fixed marked cells, slack 3,293, total
rank10--12 hole demand 2,986, and scalar remainder 307.  No matching or Hall
claim follows from these numbers.

## 8. Execution status

A capped H100 execution of this frozen build completed one 300.27-second
round with status **UNKNOWN**, zero incumbent, and therefore zero generated
component cuts.  Maximum RSS was 2,378,720 KiB.  Reported hashes are:

- result `c64c62369b5d7693b577d660b6d3de09a4d56db40fba38eeab1f12e3e5bacca6`;
- stdout `f7958864...`;
- resource log `b27c687b...`.

These execution hashes were reported by the coordinating root lane and were
not local inputs to the solver-free artifact below.  `UNKNOWN` proves neither
feasibility nor infeasibility and does not weaken the structural audit.

## 9. Exact proved/conditional boundary

The frozen system is exact and complete for:

- all greedy296-relative marked-preserving same-lower-colour exchanges;
- owner degree and exact lower-q1 palette;
- boundary-correct rank10 interval coverage; and
- lazy one-cycle connectivity.

It is only an exact evaluator/CEGAR wrapper, not an integrated sparse hard
master, for:

- strict D2/D3 residence;
- rank11 and rank12 interval coverage;
- maximal-envelope inverse replay; and
- common-cap Hall.

Those are the precise remaining rows a compound-column or finite-state
chronology model must strengthen.  No stale fixed-base delta and no fixed-pair
fibre assumption survives in the audited rank10 equations.

## 10. Independent artifacts

- verifier:
  `scratch/audit_ad_k17_opt28_greedy296_signed_rank10_master_20260731.py`  
  SHA-256 `a162e569a1c087227986bfbde945e6d1f248cb60cd500c0c61969f839c06892f`;
- audit JSON:
  `scratch/ad_k17_opt28_greedy296_signed_rank10_master_20260731.independent.audit.json`  
  SHA-256 `efc327a23689cf718e8e7317718feea732021a59285e768d5ca3978dd670dabf`,  
  payload `c4f5ffbda6729968cc2fed7805fbea47543904fd38ef395da668188692dd488d`.

