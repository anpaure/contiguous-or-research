# AD audit: portal-complete radius-99 Benders/CEGAR normal form

Date: 2026-07-29

## 1. Frozen scope

Let `F` be the quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`, SHA-256
`d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8`.
Its source edge set `E_0` has 858 loopless edge orbits.  The complete loopless
off-source seam set `A` has 26,570 edge orbits.  A radius-99 rethread chooses
`C subset E_0` and `Z subset A` with

`|C|=|Z|=99`,

and replaces `C` by `Z`.  The exhaustive branch split is
`22511 notin C` (retain) or `22511 in C` (delete).  Every admissible cut must
hit each of the 147 frozen residence motifs.

The frozen cut-space audit is
`scratch/threadD_k16_r99_cutspace_scope_20260729.audit.json`, SHA-256
`b1b069fe61a871fea0c6929cd44dc88bbde0d5f68de77a6b1a7d22a82c6c642e`.
The portal audit is
`scratch/ad_k16_r99_unique_colour_portal_rows_20260729.audit.json`, SHA-256
`37ff50044cd1b844060d95c3d4c1e3c41a0dc53285affbe2ea02660e7487b7cc`.
It fixes 1,328 portal rows, split as 667 lower and 661 upper, and 20 separately
skipped parallel-provider cases.  The complete portal-row-key hash is
`5b94a68de77a1a230dd345b8803baf32c633483b18e266cd4c9e4ff8ea546335`.

All statements below concern exact quotient degree and both q1 palettes for
this frozen source and radius.  Connectivity, voltage, fresh residence after
the rethread, and deeper shadows are later gates.

## 2. The cut-only portal theorem

### Theorem 2.1 (unique-colour endpoint portal)

Let a lower or upper q1 colour have sole source provider `e=uv`.  Suppose no
loopless off-source provider of that colour is parallel on the quotient-node
pair `{u,v}`.  Let `Q_e` be the set of endpoints outside `{u,v}` appearing on
off-source providers of the colour, and let

`H_e={h in E_0 : h has an endpoint in Q_e}`.

Every integral degree-balanced q1 completion satisfies

`sum_{h in H_e} c_h >= c_e`.                                      (2.1)

#### Proof

If `c_e=0`, (2.1) is automatic.  Suppose `c_e=1`.  Covering the colour requires
an added provider `a`.  By the nonparallel hypothesis, `a` has an endpoint
`q in Q_e` outside `{u,v}`.  The added degree at `q` is therefore positive.
Exact degree restitution says that added degree at every quotient node equals
cut source degree there.  Hence some cut source edge is incident with `q`, and
that edge belongs to `H_e`.  Thus the left side of (2.1) is at least one.  The
argument is integral and uses no relaxation variable.  QED.

The 1,328 rows in the frozen audit are exactly the instances of (2.1) after
the 20 parallel-provider cases are omitted.

## 3. Exact diagnosis of the two obsolete max-slack cuts

The old dynamic-capacity optimizer, before portal rows were imposed, produced
the following cuts.

| branch | cut-value SHA-256 | active portal rows | violated rows |
|---|---|---:|---:|
| retain | `4190aac9363d88fbb327bec88340e1ea9ed9e5dbd517dd12d0b77afaedd27b38` | 121 | 7 = 6 lower + 1 upper |
| delete | `41202dbc0b2932965f996558974c6d0a53980516570b16f2d6601924ac2560dc` | 119 | 6 = 5 lower + 1 upper |

The retain failures have sole providers
`9215,3782,10492,21021,19213,20402,3536`.  The delete failures have sole
providers `9215,3782,9539,10492,20402,22511`.

Both cuts fail the same single lower-colour row.  For colour `(0,995)`, the
sole source provider is 9215 and

`H_9215={1240,1689,1720,1737,1808,1815,2632,5497,5503,5719,5726,9086,18893,18903}`.

Each cut contains 9215 and contains no edge of `H_9215`; (2.1) evaluates to
`0>=1`.  Thus each fixed full-seam instance is infeasible from its cut
equalities and one portal row alone.  Its dynamic matching witness is
irrelevant.  In particular, the reported 0.02-second presolve times do not
measure the difficulty of a portal-admissible seam subproblem.

The solver-free reproducer is
`scratch/audit_ad_maxslack_portal_witnesses_20260729.py`, SHA-256
`9ae4f5620da9031ee7cb0de312335f6f31dc22de400f9d54a59e32e5ca31a8b1`.
Its output is
`scratch/ad_maxslack_portal_witnesses_20260729.audit.json`, SHA-256
`7a574bf5578bc1768a3eabb5f9ab6d12200ea17157c7204f0d463786aaefdfb1`.

## 4. Same-palette portal-Hall hierarchy

### Theorem 4.1 (endpoint-union Hall row)

Fix one palette and a family `T` of source-unique colours having no parallel
off-source provider.  For `c in T`, let `e(c)` be its sole source provider and
let `P_c` be its audited alternate-portal set.  Put `P=union_{c in T} P_c`.
Every exact degree-balanced q1 completion satisfies

`sum_{c in T} x[e(c)] <= sum_h |ends(h) intersect P| x[h]`.          (4.1)

#### Proof

Every lost colour in `T` requires an added replacement seam.  Distinct
colours in one palette require distinct seams, and every such seam has an
endpoint in its `P_c`, hence in `P`.  Therefore the number of lost colours is
at most total added endpoint incidence on `P`.  Exact degree restitution
changes this to total cut-source endpoint incidence on `P`, which is the
right side of (4.1).  A source edge internal to `P` has coefficient two;
this is required by the endpoint identity, not a relaxation artifact.  QED.

The exact hierarchy audit gives two radius-99 cuts satisfying all 1,328
first-order portal rows but violating (4.1):

* retain cut SHA
  `fe480b32f526e8ed428fd389b7fbd89191dcc669353956b21fee957238555ad2`
  has a lower demand/capacity pair `5/3` and an upper pair `8/4`;
* delete cut SHA
  `396a105d8413d9d7835620d3db8f6864675d2bd839a3f629061a6949b6c1457d`
  has the same pairs `5/3` and `8/4`.

The lower target-provider set is shared:
`{764,1559,9750,21323,24374}`.  The retain upper provider set is
`{652,764,1406,2169,7445,12575,16767,24697}`; the delete upper set is
`{1406,2169,7445,12575,16767,20660,22501,24697}`.  Thus four branch-labelled
certificates deduplicate to three exact linear rows.  The full rows, including
portal unions and every coefficient-one/two source edge, are in
`scratch/k16_r99_portal_hall_strictness_20260729.audit.json`, SHA-256
`685a6e080a27822a5142382062dd1b6470bf77de4631b2a55dbb00f2d95b6e0e`.
The solver-free generator has SHA-256
`4a766217bf8f2d20e8204f0d4e14e7f0cf592f1dfb966871dfc623dea50f7fab`.

### Theorem 4.2 (exact max-closure separator)

Let `x_h>=0` be any integral or fractional source-cut vector.  For each
nonparallel source-unique colour `c`, give its colour vertex profit
`p_c=x[e(c)]`; give portal node `v` cost
`d_x(v)=sum_{h incident v} x_h`.  In the directed graph

`source -> colour(c) -> every v in P_c -> sink`,

use capacities `p_c`, `INF`, and `d_x(v)` respectively, with
`INF>sum_c p_c+sum_v d_x(v)`.  If `T` is the set of colour vertices on the
source side of a minimum cut, then

`sum_{c in T}p_c-sum_{v in union P_c}d_x(v)`

is the maximum violation of (4.1) over all `T`.

#### Proof

No minimum cut crosses an `INF` arc, because cutting every source-colour arc
costs only `sum p_c<INF`.  Hence its source side is a closure: selecting a
colour forces all nodes in its portal set.  The cut capacity is precisely
the profit of unselected colours plus the node cost of the selected closure.
Subtracting from total profit yields the displayed violation.  Conversely
every `T` and its forced portal union define such a closure cut.  QED.

The production separator is exact for integer CP-SAT candidates and for
exact rational test weights.  It excludes 8 lower and 12 upper unique colours
having a parallel replacement, because their external portal sets do not hit
all replacements; no inequality for those colours is inferred.  The three
audited rows are eager master rows.  Every later master candidate is separated
in both palettes before any seam subproblem call; a newly violated full Hall
row is added, while the candidate-specific signed no-good is omitted as
redundant.

The standalone certificate emitter is
`scratch/analyse_k16_portal_hall_model_20260729.py`, SHA-256
`b39bd3cd0b11c481137f9483f4f1f2e47299816ee83e8e2bd0db77b00964288a`.

### Theorem 4.3 (joint lower--upper--endpoint cover row)

Let `R_L` and `R_U` be the source-unique lower and upper q1 colours, with
sole source providers `e(l)` and `e(u)`.  Let `D` be the 20,787 loopless
off-source seams whose two colours lie in `R_L x R_U`.  For `a in D`, write

`H_a={l(a),u(a),p(a),q(a)}`,

where `p(a),q(a)` are its quotient endpoints.  Fix any integral cover
`K=(K_L,K_U,K_N)` of these hyperedges: every `H_a` meets at least one chosen
lower colour, upper colour, or endpoint.  For a source-cut vector `x`, put

`d_x(v)=sum_{h in E_0} |ends(h) cap {v}| x_h`

and

`cost_K(x)=sum_{l in K_L}x[e(l)] + sum_{u in K_U}x[e(u)]`
`            + sum_{v in K_N}d_x(v)`.

Every endpoint-capacitated two-palette matching `y` satisfies

`|y| <= cost_K(x)`.                                             (4.2)

Consequently every radius-99 both-q1 completion, and every feasible point of
the implemented matching master, satisfies the exact projected row

`cost_K(x) >= L(x)+U(x)-99`.                                  (4.3)

#### Proof

Sum the lower-colour capacity rows indexed by `K_L`, the upper-colour rows
indexed by `K_U`, and the endpoint-capacity rows indexed by `K_N`.  Every
selected `y_a` occurs on the summed left side at least once because `K` covers
`H_a`; repeated coverage only increases its coefficient.  The summed right
side is exactly `cost_K(x)`, with an internal source edge counted twice when
both endpoints lie in `K_N`.  This proves (4.2).  The dynamic matching theorem
gives `|y|>=L(x)+U(x)-99`, proving (4.3).  Parallel seam IDs cause no problem:
they are separate `y` columns and every one of the 20,787 IDs is covered.
QED.

The frozen joint audit supplies two explicit global covers.  On the final
same-palette-Hall-feasible retain cut (SHA `061d8f5904...`) the cover costs 30
against demand 44, giving deficit 14.  On the delete cut (SHA
`8cf56bd32251...`) it costs 39 against 42, giving deficit 3.  The replay checks
all 20,787 hyperedges, including 16 repeated four-resource tuples arising
from parallel edge-orbit variants, and reconstructs every signed source-cut
coefficient.  Its artifact is
`scratch/k16_r99_joint_double_hypergraph_cover_20260729.audit.json`, file
SHA-256 `26501347140f717d9aa16b2c6cff967448867f3482aaa568560bd38910e8424e`
and payload SHA-256
`9eea835b356b080b00cfa1f2c8c1e1e37e6fadd70715bd70d61a4be821c43661`.

The audit proves that these are covers and hence proves their rows; it does
not prove either cover is minimum.  Minimum weighted cover of this
four-partite four-resource hypergraph is not the max-closure/min-cut problem
of Theorem 4.2.  More importantly, every such row is already implied by the
explicit `y` matching layer: the selected colour and endpoint capacity rows
give `cost_K(x)>=|y|`, while the dynamic demand row gives
`|y|>=L+U-99`.  The production driver therefore installs **no** joint-cover
row and runs no per-candidate joint-cover ILP.  The frozen covers remain useful
dual explanations of two rejected cuts, but duplicating them would not
strengthen the lifted master feasible set.  Same-palette Hall remains an
independent secondary filter because it also governs one-sided replacement
seams outside `D`.

### Theorem 4.4 (the `6c98` four-colour endpoint-cover cut)

Let

`T={(1,1883),(1,1907),(1,3255),(1,5939)}`

be four upper colours with respective sole source providers

`e(T)={4742,22511,23229,24034}`.

Let

`P={97,208,403,485,502,521,541,546,576,581,600,606,611,615,617,`
`   619,620,623,667,751,757,758,759,761,832,852}`.

Every loopless off-source provider of every colour in `T` has at least one
endpoint in `P`.  Consequently every exact degree-restoring upper-q1
completion satisfies

`sum_h |ends(h) intersect P| x_h`
`    >= x_4742+x_22511+x_23229+x_24034`.                 (4.4)

#### Proof

For each lost colour in `T`, upper-q1 completeness requires a selected added
provider of that colour.  One seam carries exactly one upper colour, so these
providers are distinct.  By the displayed cover property each contributes at
least one added endpoint incidence in `P`.  Their number is therefore at most
total added endpoint incidence on `P`.  Exact nodewise degree restitution
identifies that quantity with total cut-source endpoint incidence on `P`,
which is the left side of (4.4).  A source edge internal to `P` correctly has
coefficient two.  QED.

At the frozen cut with digest `6c98aa96...`, the two sides of (4.4) are 3 and
4.  Thus (4.4) gives a solver-free proof of fixed-add infeasibility and a
global cut-space separator, rather than merely a 99-edge candidate no-good.
The audit checks all 140 loopless off-source providers, all 49 nonzero LHS
source coefficients (46 of value one and 3 of value two), and the 52-term
signed form.  This audit needs no minimality claim; the separate
`MATH_THEOREM_L_K16_R99_6C98_ENDPOINT_COVER_BENDERS_20260729.md` proves that
26 is minimum for this provider union.
Its frozen artifact is
`scratch/k16_r99_6c98_fourcolour_endpoint_cover_cut_20260729.audit.json`,
SHA-256
`aacf3b7960201815404596a4fc124e99173d38b757b347ede0b240142ecbbd3d`.

## 5. Portal-complete cut master

There are 675 source-unique lower colours and 673 source-unique upper colours.
Among the off-source seams, 20,787 have both a source-unique lower colour and
a source-unique upper colour.  Introduce 858 cut bits `c_e` and 20,787
auxiliary double-repair bits `y_a`.

The master contains:

1. `sum c=99`, the fixed branch value of `c_22511`, and all 147 motif rows;
2. lower- and upper-colour matching rows for `y` (675 and 673 rows);
3. 858 endpoint-capacity rows
   `sum_{a incident v} y_a <= sum_{e incident v} c_e`;
4. the dynamic demand row
   `sum y >= L(c)+U(c)-99`;
5. all 1,328 portal rows (2.1);
6. the three deduplicated eager Hall rows (4.1), followed by exact dynamic
   max-closure separation;
7. the single four-colour endpoint-cover row (4.4); no joint-cover projection
   row is duplicated;
8. the audited Pareto facets: retain has `L>=50`, `U>=50`, `L+U>=113`;
   delete has `L>=49`, `U>=48`, `L+U>=111`, `L+2U>=160`.

Hence the exact master census is

| branch | variables | constraints |
|---|---:|---:|
| retain | 21,645 | 3,691 |
| delete | 21,645 | 3,692 |

### Theorem 5.1 (master necessity)

Every exact 99-cut/99-seam degree-balanced both-q1 completion projects to a
feasible master point.

#### Proof

The cut, branch, motif, portal, and Pareto conditions are necessary by their
defining audits and Theorem 2.1.  Consider the bipartite graph whose left
vertices are the `L(c)` lost source-unique lower colours, whose right vertices
are the `U(c)` lost source-unique upper colours, and whose edges are selected
added seams carrying both kinds of lost colour.  The 99 selected additions,
together with one-sided additions if present, give an edge cover of all
`L(c)+U(c)` lost-colour vertices using at most 99 tokens.  The bipartite
edge-cover identity gives a matching of size at least `L(c)+U(c)-99`.  Choose
that matching as `y`.  Its colour rows hold by matching, its activation rows
hold because its colours were lost, and its endpoint usage is at most the
total selected added degree.  Exact degree restitution bounds the latter by
cut degree at every node.  Thus all master rows hold.  QED.

The master is necessary only; a feasible `(c,y)` does not itself supply the
remaining seams or exact degree/q1 completion.

## 6. Branch-free exact seam recourse

The production recourse now keeps all 858 cut bits symbolic and all 26,570
loopless off-source add bits, but deliberately removes every master-only
antecedent.  It contains only `sum cut=99`, 858 exact degree equalities, and
all 764 lower plus 764 upper q1 provider rows.  Thus its exact census is

| variables | constraints |
|---:|---:|
| 27,428 | 2,387 |

No branch lock, motif, Pareto, portal, Hall, joint-cover, or aggregate repair
row occurs in this oracle.  The explicit equation `sum add=99` is redundant:
summing the loopless degree equalities counts every cut and add seam twice and
gives `2 sum add=2 sum cut=198`.

For a fixed cut `C`, the 99 positive assumptions `c_e=1` for `e in C` fix the
entire cut vector because the model also contains `sum c=99`.  Thus recourse
SAT is equivalent to the existence of exactly 99 loopless off-source seams
restoring every quotient degree and both complete q1 palettes for that cut.
No seam filtering or cut-dependent numeric substitution occurs: the same
branch-free model is used for every candidate in both masters.

### Theorem 6.1 (positive assumption-core cut)

Let `K subset E_0`.  If the branch-free recourse is infeasible under the
positive assumptions `c_e=1` for all `e in K`, then every radius-99 exact
completion in either branch satisfies

`sum_{e in K} c_e <= |K|-1`.                                      (5.1)

#### Proof

If an exact completion violated (5.1), its cut would contain every edge of
`K`, and its seam set would satisfy the branch-free degree/q1 recourse under
those assumptions, contradicting infeasibility.  QED.

For a master candidate `C`, the full 99 positive assumptions fix `C`; no
negative assumptions are needed.  A solver-returned subcore can therefore be
strictly smaller than 99 and yields the genuinely generalized cut (5.1).
This specialization depends essentially on the exact cardinality equation.

The implementation learns (5.1) only after an independent replay of the
assumption-bearing universal proto returns `INFEASIBLE`.  `UNKNOWN` never
learns a row.  Each replay proto, its SHA-256, the literal-index registry, and
the normalized cut are persisted.  An empty returned core is not converted
into an illegal no-good; after replay it says that the entire radius-99
degree-plus-both-q1 recourse is infeasible, independent of branch.  Imported
resume cores are checked against the new branch-free scope digest and replayed
before reuse; old branch-scoped resumes fail that digest.

CP-SAT `INFEASIBLE` is an exact solver transcript, not a DRAT-style formal
proof log; the report scope states this explicitly.

### Theorem 6.2 (compact four-colour recourse projection)

Keep all 858 symbolic cut bits and all 26,570 loopless off-source add bits,
but retain only `sum x=99`, the 858 exact node-degree equations, and the four
guarded upper rows in `T`.  This branch-free relaxation has 27,428 Boolean
variables and exactly

`1+858+4=863`

native constraints.  Every full both-q1 recourse projects into it.  Hence any
assumption set whose replay makes this relaxation infeasible yields a valid
global no-good, independent of branch, motifs, Pareto rows, portal rows, and
all other master strengthenings.

For the four colours alone there is a smaller necessary projection.  Use one
witness bit for each of their 140 loopless off-source provider seams.  Impose
four activation equations

`sum_{a provider of c} z_a = x[e(c)]`

and, at each of the 33 provider endpoints,

`sum_{c,a incident v} z_a <= sum_{h in E_0 incident v} x_h`.       (6.1)

This has 140 witness bits, 59 relevant source-cut bits, and 37 rows.  It is
exact for simultaneous selection of one provider for each lost colour under
the available endpoint capacities, and is a necessary projection of full
recourse.  Projecting the endpoint-cover inequality for `P` from (6.1)
recovers (4.4).  A SAT point of this compact oracle is not a complete add set;
an UNSAT replay is a sound recourse obstruction.

Because each of the four complete provider graphs is `K_9` with only its
unique source edge removed, the same projection has an even smaller exact
endpoint formulation.  Introduce 36 bits `u_(c,v)`, require

`sum_{v in V_c}u_(c,v)=2x[e(c)]`,

forbid choosing both endpoints of the removed source pair, and impose the 33
shared endpoint-capacity rows.  This uses 36 new bits and 41 rows (95 total
variables including the 59 relevant cut bits).  It is equivalent to the
140-provider projection for this four-colour `K_9-e` family and strictly
stronger than the single endpoint row (4.4).  The independent dominance audit
also proves that (4.4) strictly dominates both previously proposed 51-term
forcing-chain clauses, so those clauses are not installed.

The generic 199-variable artifact and its independent replay are
`scratch/k16_r99_6c98_fourcolour_compact_recourse_20260729.model.json` and
`scratch/k16_r99_6c98_fourcolour_compact_recourse_20260729.audit.json`.
The exact dominance comparison is
`MATH_AUDIT_AD_K16_R99_6C98_CUT_DOMINANCE_20260729.md` with replay
`scratch/ad_k16_r99_6c98_cut_dominance_20260729.audit.json`.

More generally, full q1 recourse depends on a cut only through its endpoint
demand vector

`d_v(x)=sum_{h incident v}x_h`

and its lower/upper lost-colour bits.  Guarding these state values permits a
conflict clause of the form

`OR_{(v,t) in G_d}[d_v(x) != t] OR OR_{c in G_l}[lost_c(x)=0]`.    (6.2)

Both directions of every lost-colour equivalence are required before such a
clause is translated back to the master.  The persisted four-row q1 shrink is
deletion-minimal relative to the fixed `6c98` degree system, but it is not by
itself a cut-assumption core.  Equation (4.4), not the unsupported inequality
`x_4742+x_22511+x_23229+x_24034<=3`, is the present unconditional cut-space
consequence.

## 7. Implemented artifacts and lightweight audits

The proof-carrying driver is
`scratch/solve_k16_r99_cut_add_benders_cegar_20260729.py`, SHA-256
`5f700eeca6b36385378c5a6595ab7838b67606e1cdf2215dcc46c0c1b02c4e84`.
It rejects the two obsolete max-slack artifacts as portal-infeasible hints,
audits every decoded master candidate before recourse, stores distinct initial
and final master protos, freezes source hashes at process start, and fails if
the driver or catalogue module changes during a run.

The portal-complete stand-alone dynamic master is
`scratch/solve_k16_r99_cut_double_capacity_relaxation_20260729.py`, SHA-256
`2e43939ab1288c3cc2d308d315e29d45f57f0d2e8f1dc2faa60cb495a553630d`.
It reconstructs and hash-checks all 1,328 portal rows and uses the same Pareto
facets, the three eager Hall rows, and the 3,690/3,691 master census.

The independent result auditor is
`scratch/audit_threadD_k16_r99_cut_add_benders_20260729.py`, SHA-256
`0cb576e930ff1a9603ce1b8e1af3a23807e8ec01ab202a7ce641297b766772bc`.
Its solver-free self-test passes.  All sixteen positive-core/portal/endpoint
regressions in `scratch/test_threadD_k16_r99_benders_core_logic_20260729.py`,
SHA-256 `340a5cf2992859619d29eaa206657ff8d41a7d3369c30ce46356e08dd97a44d2`,
also pass, including exact-rational closure separation, complete replay of the
140 four-colour providers, absence of the redundant joint-cover layer, and
the exact branch-free 2,387-row recourse scope.

## 8. Exact current boundary

No level-2-separated Benders master/recourse run is claimed here.  H100 memory
and swap were under severe pressure, and the user explicitly froze new
launches and retries until headroom is confirmed.  The preserved commands are in
`scratch/K16_R99_RECOVERY_COMMANDS_20260729.md`.
The older frozen directory
`scratch/threadD_k16_r99_benders_lowmem_launch_20260729/` is explicitly
pre-pivot and must not be launched: it still carries the redundant joint rows
and obsolete master/recourse censuses.  Its manifest must be rebuilt from the
current endpoint-row driver before it can again serve as an authorized
low-memory bundle.

Consequently:

* the two old max-slack cuts are rigorously closed at the cut-master layer;
* first-order portal feasibility is rigorously separated from level-2 Hall,
  and the two embedded portal-feasible cuts are closed by three eager rows;
* an exact polynomial separator for the canonical portal-union subfamily now
  screens every later master candidate before seam recourse; the later
  fractional endpoint-cover LP in
  `MATH_THEOREM_L_K16_R99_6C98_ENDPOINT_COVER_BENDERS_20260729.md` separates
  a dominating broader family but is not yet in this production loop;
* the joint-cover rows are retained only as dual explanations and are not
  duplicated in the lifted matching master;
* the first joint-matching-admissible delete cut, `6c98`, is rigorously closed
  by the solver-free four-colour endpoint row (4.4); the saved fixed-CNF UNSAT
  transcript is no longer needed for that conclusion;
* the compact 863-row first tier and the 199-variable/37-row generic
  four-colour projection (equivalently 95 variables/41 rows in the exact
  `K_9-e` endpoint encoding) give portable local assumption-core interfaces;
* the corrected master and the branch-free exact 2,387-row full recourse are
  implemented and independently audited without launching a new heavy job;
* no SAT radius-99 q1 factor and no branch/global UNSAT certificate has yet
  been obtained from this CEGAR loop.
