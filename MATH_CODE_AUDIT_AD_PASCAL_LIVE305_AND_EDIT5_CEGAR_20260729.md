# Frozen 305-segment Pascal run and the exact edit-five successor

Date: 2026-07-29  
Lane: AD  
Status: original 305-segment run terminated `UNKNOWN` and was copied and
independently audited; new solver-free radius-five obstruction and exact
edit-five CEGAR implemented and adversarially audited; the authorized
16-worker disjoint edit-five run also terminated `UNKNOWN` and was audited

## 1. Verdict

The 305-segment H100 job was an exact satisfaction model for its declared
304-cut/305-segment chronology palette.  It jointly enforces

* a literal same-endpoint Hamilton path through the complete rank-seven
  deck of `[14]`;
* one AA edge of every rank-six intersection colour;
* hard distinguished-coordinate residence, meaning every AA path has at
  least four vertices;
* the common cross/BB controller;
* both complete upper-`q1` sectors.

It terminated raw `UNKNOWN` after 7,214.8 solver seconds.  It found no
positive witness and proved no infeasibility; its `certificate_status` is
null.  The independent terminal verifier passes the frozen provenance and
correctly labels the result as carrying no mathematical certificate.

The main new mathematical conclusion is stronger than the previous
three-edge support bound:

\[
 \boxed{|E(P)\setminus E(P')|\ge5}
\]

for every same-endpoint chronology `P'` on the frozen rank-seven deck that
admits an exact-lower AA forest with all components of length at least four.
This is independent of either upper channel.  The proof has two parts:

1. four disjoint exact colour/owner closures force at least four deleted
   base edges;
2. every one of the 900 possible support-compatible four-cut sets has only
   its original forward Johnson route, which restores all four cuts.  Thus
   no nontrivial exact-distance-four Hamilton path exists.

The exact next chronology shell is therefore edit distance five.  A new
full-Johnson-graph model represents this shell without a heuristic cut
palette and enforces connectivity by valid finite CEGAR cuts.  After the
resource restriction was relaxed, one `outside-live` run was launched; its
feasible chronology set was disjoint from the 305-segment palette.  It also
terminated `UNKNOWN`, without producing a first master incumbent.

## 2. Frozen live run

The frozen remote directory is

```text
/home/amodo/or15/k15_pascal_segment_lns_20260729
```

and the completed process was PID `3123570`, parent PID `1`.  Its exact
command was

```text
python3 -u input/solve_k15_generalized_pascal_segment_lns_ad.py \
  --path input/k14_common_colour_3opt_best_20260729.json \
  --hint-factor input/minz_base.json \
  --output segment_fullq1_hardres_s15107.json \
  --timeout 7200 --workers 20 --seed 15107 \
  --z-upper --noz-upper --hard-residence \
  --require-motif-change --overwrite
```

Frozen hashes are

```text
source  5c2ec7f8189717a4b2e86fc546ef0c3b0965636d20c49a3a002b0f8ab6031767
path    eeccbd6be6edeba88a5d953a1f543c8f77895bbbec0e6ab0fd4eadb9e05af546
hint    dd2a8eeda0aa996fed43a9bb92eb823cfa57d0d00f1f3e9492dcc4235f115363
input manifest 53c036c956410c6b8e640710127bcb3ad4fa5ae7ca100fdeb9cbcfdc1eb23207
```

The exact initial model census is `116,240` variables and `92,717`
constraints.  It uses OR-Tools `9.15.6755`, initial CP-SAT fingerprint
`0xdc7e3b021edf44a8`, and presolved fingerprint `0xdc05ccbfb9a45d5`.
The terminal CP-SAT response is

```text
status       UNKNOWN
objective    NA
best_bound   NA
walltime     7214.796416519001 seconds
```

The final JSON has `solver_status=UNKNOWN`, `certificate_status=null`, no
decoded path or selected factor, and the same 116,240/92,717 model census.
The final hashes are

```text
result JSON  962be430f617ac8fe1c5fa5cbddabc4bb92a382def3543884e04ca5c61f2aa85
solver log   abcf3a2b5e3cd027001f7556ef092a8a9d300e01f52575a816d8806a014db032
model proto  f0eaf89a883823db5fd4a116b891d36ccdf1c57e8066a812ea84ea0d77b3c7a5
```

The proto digest was independently reproduced on H100 from the staged
source and inputs with zero search time; the rebuild again had 116,240
variables and 92,717 constraints.  The copied artifacts and solver-free
audit are under

```text
scratch/k15_pascal_segment_lns_20260729/
```

with audit SHA-256

```text
43e9f7d1b0a91a0f06e7053a64a6901dd48666ff185997b174066e26f45b43e2.
```

Ordinary and `python -O` verification both pass.  Because the raw status is
`UNKNOWN`, the exact conclusion is only that this bounded run was
inconclusive.

## 2A. Fixed-path full-`q1` minimization harvest

The separate fixed-chronology minimization artifacts are

```text
scratch/k15_generalized_pascal_fixedpath_minz_s15106_20260729.json
SHA-256 2248e5ff1fb95ce5c2c4990f5c652a2cc30f65514ee2e50f173cfdb4c21148cf

scratch/k15_generalized_pascal_fixedpath_minz_s15106_20260729.log
SHA-256 d8e96c9c8e403061fde11f952d732e2ee3fdb42797580dd8259bb1fd0e7761cc
```

The raw CP-SAT response is

```text
status       FEASIBLE
objective    29
best_bound   17
walltime     3600.17 seconds
```

under seed `15106`, eight workers, OR-Tools `9.15.6755`, initial model
fingerprint `0x589c12603953fe36`, 106,388 variables, and 48,745
constraints.  The presolved and solution fingerprints are respectively
`0x2a8dd7833241bf3a` and `0x33ddeb07be11effc`.  The JSON's status string
`FEASIBLE_VERIFIED_FACTOR` is the old
source's postverification wrapper; it must not be mistaken for raw
`OPTIMAL`.  In particular, 29 is an incumbent and 17 is only the retained
lower bound.

The paired dependency hashes are

```text
fixed-path solver  ac53e0611cfbadd3e2e21db7a5a5473e79b4d3a98a464505261e850ce88bcf70
full-q1 hint       e8092469c88b0a224bf0b11ed2661e06b5de260cc349717ea704732f47e00f29
```

The old flag name `no_z_residence=true` is misleading: in that source it
means hard residence is **off**, while `minimize_z_defects=true` activates
the short-run objective.  Both upper constraint families are active.

Independent literal replay of all 3,003 AA, 858 cross, and 2,574 BB
selections gives

```text
lower q1                         exact (6,435/6,435)
physical upper q1 holes          0 (5,005/5,005 present)
z-upper sector holes             0
no-z upper sector holes          0
physical factor components       8
component lengths                3831,1010,820,618,136,11,5,4
distinguished-z short AA paths   29 = 18 of length 2 + 11 of length 3
all-coordinate residence defects 1415
  histogram                        578 of length 2 + 837 of length 3
  distinguished z contribution    29
  old-coordinate contribution     1386
```

The two residence numbers are different statistics.  The optimized
objective counts only short paths in the distinguished-`z` AA forest.
The value 1,415 counts every length-two or length-three coordinate run on
every physical factor cycle.  The latter was recomputed from the literal
cycles, not inferred from the objective.

This improves the fixed-path full-`q1` bracket only to

\[
 17\le D_{\mathrm{fixed\ path,full}\ q1}\le29.          \tag{2A.1}
\]

It neither proves 29 optimal nor weakens the solver-free fact that exact
distinguished-`z` residence is impossible on the frozen path.  It has no
negative implication for the variable-path 305-segment job.  The eight
components are a degree-two factor, not one Hamilton cycle; upper `q1` is
coverage with multiplicities, not exact-one upper ownership, and the saved
deeper `q` audit remains holey.

The reproducer

```text
scratch/audit_k15_generalized_pascal_fixedpath_minz_s15106_20260729.py
SHA-256 67e991fc488b3e5155a0621f071332bc6e3bec95f578f0c7474ca0fe2d2df1ac
```

checks the frozen JSON/log/path hashes, raw response and fingerprint,
reconstructs the physical factor from the selected AA/cross/BB rows, checks
the saved cycles edge-for-edge, and independently recomputes all 1,415
coordinate/run triples.  Ordinary and `python -O` executions agree.  This
literal replay closes the positive witness despite the historical source's
use of removable Python `assert`; the JSON itself does not embed the source,
path, hint, raw status, bound, or solver fingerprints, so provenance depends
on the frozen sidecar pairing above.

## 3. Exact scope of the live model

Cutting the parent path at the 304 palette positions produces 305 intact
segments.  Exactly one orientation is chosen for every segment.  Selected
state arcs give one predecessor and successor except at the frozen source
and sink.  All-different order variables and

\[
 \pi_{\rm target}=\pi_{\rm source}+1
\]

on every selected arc exclude all subtours and force one order through all
segments.  Every allowed join is tested directly in `J(14,7)`.  Thus the
decoded sequence is a literal Hamilton path, not a fractional or projected
chronology.

For every candidate path edge `e`, the AA variable satisfies `a_e<=h_e`.
The equations

\[
 \sum_{e:\,\cap e=X}a_e=1
 \qquad\left(X\in\binom{[14]}6\right)
\]

and

\[
 \sum_{e\ni T}a_e=1+p_T,
 \qquad p_T\in\{0,1\},
\]

make the AA graph a spanning path forest with 3,003 edges, 858 degree-one
vertices, 2,574 degree-two vertices, and 429 components.

The hard-residence edge and wedge inequalities are exact.  A two-vertex
component is exactly an AA edge whose two ends have AA degree one.  A
three-vertex component is exactly an AA wedge whose outer ends have degree
one.  Excluding both is equivalent to all AA components having at least
four vertices.

The cross/BB equations then give exactly 858 cross edges and 2,574 BB edges,
degree two at every rank-eight child vertex, exact lower `q1`, and the two
separate upper requirements

\[
 \{\text{AA unions}\}\cup\{\text{cross uppers}\}
   =\binom{[14]}8,
\]

\[
 \{\text{BB unions}\}=\binom{[14]}9.
\]

Therefore a final `VERIFIED_FACTOR` JSON is a literal positive certificate.
An `INFEASIBLE` status would be a CP-SAT conclusion only for this frozen
palette and these flags; CP-SAT emits no independently checkable DRAT proof.
`UNKNOWN` has no negative content.

Two provenance qualifications remain:

1. the version-robust fallback hashes `str(model.Proto())`; that digest is
   provenance metadata, not a canonical cross-version proof hash;
2. the source hashes its inputs again after solving, so the staged pre-run
   `input.sha256` manifest is needed to close the mutation race.

## 4. Four forced deletion closures

Let

\[
 P=(T_0,\ldots,T_{3431}),\qquad
 e_i=T_iT_{i+1},\qquad
 \gamma_i=T_i\cap T_{i+1}.
\]

For a new same-endpoint Hamilton chronology `P'`, say that old edge `e_i`
*survives* if it belongs to `E(P')`.  Let `x_i` indicate that a surviving
old edge is chosen in the new AA forest.

If two consecutive old edges survive, they are still the two path edges at
their common old vertex.  Since every AA degree is at least one,

\[
 x_i\lor x_{i+1}.                                      \tag{4.1}
\]

Exact lower colour gives at most one selected occurrence of each
intersection colour, even if new seams create additional occurrences.
This observation is what makes the following closures stable under an
arbitrary global block permutation.

Define the pairwise-disjoint position sets

\[
\begin{aligned}
G_1&=\{708,709,710,711\},\\
G_2&=\{1940,1941,1942\},\\
G_3&=\{2219,2220,2221,2521,2522\},\\
G_4&=\{179,180,181,1364,1365,1773,1774,1775,\\
&\qquad 1836,1837,1838,2723,2724,2725,2726\}.
\end{aligned}                                           \tag{4.2}
\]

### Theorem 4.1 (four-closure deletion theorem)

If `P'` admits an exact-lower AA forest with no component of two or three
vertices, then at least one old edge in every `G_j` is absent from `P'`.
Consequently

\[
 |E(P)\setminus E(P')|\ge4.                            \tag{4.3}
\]

#### Proof

Assume all edges of one displayed group survive.

For `G_1`, the complete old fibres are

\[
 F_{14374}=\{708,709\},\qquad
 F_{12390}=\{710,711\}.
\]

Equation (4.1) and colour at-most-one force exactly one selected edge in
each adjacent pair.  The two unselected edges cannot be `709,710` by
(4.1); every other possible pair is at edge-position distance two or three,
so it brackets a forbidden short AA component.

For `G_2`,

\[
 F_{10318}=\{1940,1941,1942\}.
\]

The two adjacent owner clauses and colour at-most-one force only edge 1941
selected.  The cuts at 1940 and 1942 bracket a two-vertex component.

For `G_3`,

\[
 F_{5149}=\{2219,2220\},\qquad
 F_{5273}=\{2221,2521,2522\}.
\]

The surviving adjacent pair `2521,2522` forces one selected occurrence of
colour 5273, so `2221` is unselected.  The owner clause at the surviving
`2220,2221` pair then forces `2220` selected, hence `2219` unselected.
The cuts 2219 and 2221 bracket a two-vertex component.

For `G_4`, use the complete fibres

\[
\begin{aligned}
F_{7697}&=\{179,1775\},&
F_{3858}&=\{181,1838\},\\
F_{16128}&=\{1364,1365,1773\},&
F_{3792}&=\{1836,2723\},\\
F_{2761}&=\{2725,2726\}.&&
\end{aligned}
\]

Suppose no short component occurs.  The adjacent pair `2725,2726` forces
one selected occurrence of colour 2761.  Its other edge is an AA cut.  A
cut at 2723 would then lie at distance two or three, so 2723 is selected
and 1836 is cut.  The cut at 1836 forces 1838 selected and 181 cut; the cut
at 181 forces 179 selected and 1775 cut.  Finally the adjacent occurrences
1364,1365 force one of them selected and therefore 1773 cut.  The cuts
1773 and 1775 now bracket a two-vertex component, a contradiction.

At every step, an added seam of the same colour cannot be selected: a
surviving adjacent old pair already forces an old occurrence selected, or
the no-short assumption forces the stated old occurrence selected.  Thus
the argument is stable under arbitrary added colour multiplicity.  The
four groups are disjoint, proving (4.3).  ∎

## 5. The entire four-edit shell is empty

At edit distance exactly four, Theorem 4.1 forces exactly one deletion from
each `G_j`.  Hence there are exactly

\[
 4\cdot3\cdot5\cdot15=900                              \tag{5.1}
\]

possible cut quadruples.

Fix one sorted quadruple `c_1<...<c_4`.  Deleting these edges makes five
intact old intervals `B_0,...,B_4`.  The frozen endpoints force `B_0` first
and forward and `B_4` last and forward.  The three internal intervals have
at most

\[
 3!2^3=48                                               \tag{5.2}
\]

orders/orientations.  This list is exhaustive: every connected graph that
retains all other old edges must contract to such a five-block path.

### Theorem 5.1 (solver-free empty four-cut shell)

For every one of the 900 cut quadruples, exactly one of the at most 48
same-endpoint block routes is Johnson-legal.  It is the original forward
order

\[
 B_0|B_1|B_2|B_3|B_4
\]

and its four joins are precisely the four deleted base edges.  It therefore
restores all four cuts and has actual edit distance zero.  In particular,
there is no same-endpoint Johnson Hamilton path at edit distance four that
can satisfy hard AA residence.

#### Exact audit

The primary route generator tests the Cartesian list (5.2).  An independent
solver-free audit instead constructs the directed compatibility graph of
the ten possible oriented internal blocks and uses DFS from the frozen
source block to the frozen sink block.  Both give the same census:

```text
cut quadruples                       900
compatible Johnson routes            900
profile new0, four distinct joins     900
exact-distance-four routes              0
```

The independent per-quadruple ledger SHA-256 is

```text
ceedb84102052749d902cc3ff3fb72905a0c10add812d9af9861da70f72b1801
```

It also rechecks the complete fibre-position lists used in Theorem 4.1 and
mechanically checks the added-occurrence loophole.  For each relevant colour
it allows either one selected old occurrence or one abstract selected new
occurrence, then tests every assignment against the surviving connector
blocks.  The exact assignment counts for `G_1,...,G_4` are respectively
`9,4,12,324`, with zero no-short assignment in every case.  It passes
identically under ordinary Python and `python -O`.  This is a finite literal
proof for the frozen path, not an asymptotic statement.

The route catalogue hash is

```text
ffc29a2d5cc667136b5bd332190f90fd59bfa57c0463e718369316283b68c463
```

over canonical sorted compact JSON including its explicit hash-domain
string and excluding only the `catalogue_sha256` field.

Combining Theorems 4.1 and 5.1 gives

\[
 \boxed{|E(P)\setminus E(P')|\ge5,
 \qquad |E(P)\triangle E(P')|\ge10.}                  \tag{5.3}
\]

## 6. Interaction with the live palette

Let `P_0` be the frozen 304-cut palette.  Exact reconstruction gives

\[
 G_1\cup G_2\cup G_3\subseteq P_0,
\]

\[
 G_4\cap P_0=\{179,180,181,1775,1838,2725\},
\]

\[
 G_4\setminus P_0=
 \{1364,1365,1773,1774,1836,1837,2723,2724,2726\}.
\]

Retaining every nonpalette base edge is equivalent to keeping each of the
305 old segments intact, so the live chronology model is exactly the
`eta=0` class, where `eta` is the number of deleted nonpalette base edges.
All positions in `G_1` and `G_2` are among the 55 motif cuts, so the live
`--require-motif-change` flag excludes no hard-resident path in this class.

The empty four-cut theorem is global and does not depend on the live result.
At edit distance five the useful disjoint scope is `eta>=1`; the complete
scope also includes `eta=0` in case the live run is only `UNKNOWN`.

## 7. Exact edit-five CEGAR

Let `J=J(14,7)`, with

\[
 |V(J)|=3432,\qquad |E(J)|=84084.
\]

The frozen path has 3,431 edges, leaving 80,653 nonbase Johnson edges.

### Theorem 7.1 (degree master)

For each `e in E(J)`, let `h_e` indicate a selected chronology edge.  Impose

\[
 \sum_{e\ni v}h_e=
 \begin{cases}
 1,&v\in\{T_0,T_{3431}\},\\
 2,&\text{otherwise},
 \end{cases}                                           \tag{7.1}
\]

and

\[
 \sum_{e\notin E(P)}h_e=5.                            \tag{7.2}
\]

Then the selected graph has 3,431 edges, deletes exactly five base edges,
and consists of one source-sink path component plus zero or more cycles.
It is a same-endpoint Hamilton path at edit distance five if and only if it
is connected.

#### Proof

Summing (7.1) gives `2|E(h)|=2(3432)-2`, so `|E(h)|=3431`.
Equation (7.2) then forces exactly `3431-5` selected base edges and hence
five deletions.  Every component has an even number of odd-degree vertices.
The only odd-degree vertices are the frozen endpoints, so they lie in the
same component; every other component is a cycle.  Connectedness is
therefore equivalent to one spanning source-sink path.  ∎

The four closure inequalities are added directly:

\[
 \sum_{i\in G_j}(1-h_{e_i})\ge1\qquad(j=1,2,3,4).      \tag{7.3}
\]

They are redundant mathematically but strong and independently proved.

### Theorem 7.2 (compact hard-residence constraints)

Select AA variables `a_e<=h_e` with one edge per rank-six colour and

\[
 \sum_{e\ni v}a_e=1+p_v,qquad p_v\in\{0,1\}.          \tag{7.4}
\]

For every edge `e=uv`, impose

\[
 a_{uv}\le p_u+p_v.                                   \tag{7.5}
\]

Introduce a witness `q_uv` allowed to be one only if

\[
 q_{uv}\le a_{uv},\qquad q_{uv}\le p_u,qquad
 q_{uv}\le p_v,                                       \tag{7.6}
\]

and impose

\[
 \sum_{e\ni v}q_e\ge p_v.                            \tag{7.7}
\]

For a spanning AA subgraph of a Hamilton path, (7.5)--(7.7) hold if and
only if every AA component has at least four vertices.

#### Proof

Equation (7.5) excludes a two-vertex component, whose unique edge has two
degree-one ends.  A three-vertex component has one degree-two centre and
two degree-one ends; no incident edge can satisfy (7.6), contradicting
(7.7) at the centre.  Conversely, in every path of at least four vertices,
each degree-two vertex is adjacent to another degree-two vertex.  Set one
or more corresponding `q` witnesses to one.  ∎

The unchanged cross/BB equations impose the common controller, exact lower
`q1`, and both upper sectors.  Before connectivity cuts, the full scope has
exactly

```text
351,780 Boolean variables
448,596 constraints
```

under the source-level count.  `outside-live` adds one constraint requiring
at least one of the 3,127 nonpalette base edges to be deleted.  Every
connectivity cut adds one further constraint.

### Theorem 7.3 (exact connectivity CEGAR)

If an integral incumbent of (7.1) is disconnected, let `S` be the vertex
set of one cycle component.  Add

\[
 \sum_{e\in\delta_J(S)}h_e\ge2.                       \tag{7.8}
\]

This cut is valid for every connected feasible chronology.  Repeatedly
separating all incumbent cycle components terminates after finitely many
distinct shores; it accepts exactly the connected edit-five chronologies.

#### Proof

The shore `S` contains neither frozen endpoint, so its selected boundary
has even cardinality by the degree-sum identity.  A connected graph has a
nonempty boundary, hence at least two edges.  The current cycle component
has boundary zero and is removed.  There are finitely many vertex shores.
When no cycle component remains, Theorem 7.1 gives one Hamilton path.  ∎

An `INFEASIBLE` terminal status after any collection of (7.8) is therefore
sound for the declared edit-five scope.  It remains solver-certified rather
than proof-certificate-certified.  A positive result is decoded and checked
as a literal Hamilton path and complete physical factor before being marked
`VERIFIED_FACTOR`.

For provenance, every future run serializes the exact argv, resolved input
and output paths, source/input hashes, OR-Tools version, raw integer status,
`ResponseStats()`, total elapsed time, and a per-iteration status/time/
component ledger, as well as every connectivity shore and its boundary
size.  These data make the solver claim reproducible but still do not turn
CP-SAT `INFEASIBLE` into an independently checkable proof certificate.

## 8. Terminal verifier

The independent no-OR-Tools verifier is

```text
scratch/verify_ad_k15_pascal_segment_lns_terminal_20260729.py
SHA-256 297430460c1ced57945abaf017969e9d8154edcf6d49cf422303a7ef9e5a1997
```

For a positive live result it independently rebuilds the catalogue and
checks:

1. the complete 3,432-mask Johnson path, frozen endpoints, all 305 segments,
   orientations, and selected joins;
2. 3,003 distinct path-supported AA edges, every rank-six colour once,
   degree histogram `858 x 1 + 2574 x 2`, 429 components, and minimum
   component length four;
3. 858 legal cross edges and 2,574 legal BB edges with every A/B controller
   equation;
4. 6,435 unique physical edges, degree two on the full rank-eight child
   deck, exact lower `q1`, complete upper `q1`, and the two upper sectors
   separately;
5. motif change and all four support-closure hits.

For `INFEASIBLE` or `UNKNOWN`, it additionally requires the exact pre-run
manifest and an independently rebuilt same-version proto hash.  It labels
the former only as a frozen-scope solver status and the latter as no
mathematical certificate.

## 9. New artifacts

```text
scratch/solve_k15_pascal_fourcut_shell_ad_20260729.py
scratch/audit_k15_pascal_fourcut_empty_shell_ad_20260729.py
scratch/solve_k15_pascal_edit5_connectivity_cegar_ad_20260729.py
scratch/verify_ad_k15_pascal_segment_lns_terminal_20260729.py
scratch/audit_k15_generalized_pascal_fixedpath_minz_s15106_20260729.py
scratch/audit_k15_pascal_edit5_s15501_terminal_20260729.py
```

Current source hashes after adversarial hardening are

```text
edit-five CEGAR       803593f675ac7c7c575ae4674bb3a60e5921498cad431a147b4c1355442f6e79
four-cut generator    f9b5ca96d8b7e4b3f249a7ca36b8147cf4eaa1bdaf69d63cdfc8f070959a40f6
four-cut audit        13e1a8b9f35d1a1a9c4f51cb8e0e5158935ccfd2116f9857d6f7a771295eaff9
live terminal verifier 297430460c1ced57945abaf017969e9d8154edcf6d49cf422303a7ef9e5a1997
fixed-path s15106 audit 67e991fc488b3e5155a0621f071332bc6e3bec95f578f0c7474ca0fe2d2df1ac
edit-five terminal audit 968ff6a7d7e642dcd2018c05b8e134dbd8b27e7b86a97fe0a981e8cc5df61829
```

The independent adversarial proof/source audit is

```text
MATH_CODE_AUDIT_AD_EDIT5_CEGAR_FOURCUT_ADVERSARIAL_20260729.md
```

After explicit authorization, one CPU-only disjoint run was launched at

```text
/home/amodo/or15/k15_pascal_edit5_cegar_20260729
```

with command

```text
python3 -u scratch/solve_k15_pascal_edit5_connectivity_cegar_ad_20260729.py \
  --path input/k14_common_colour_3opt_best_20260729.json \
  --hint-factor input/minz_base.json \
  --output edit5_outside_live_s15501.json \
  --scope outside-live --timeout 7200 --workers 16 --seed 15501 \
  --max-iterations 1000 --overwrite
```

The Python PID is `3141966` under launch-wrapper PID `3141965`.  The frozen
input manifest SHA-256 is

```text
0d87e4fabb395be862a2a92e84db413c66f66a6b5320bc877bcf1b5ce6cbe14f.
```

Initial CP-SAT census and fingerprint are

```text
variables       351,780
constraints     448,597
fingerprint     0xf10b26eabe3b817
presolved       351,540 variables / 304,139 constraints
presolved fp    0x84a5d9a3c110776b
OR-Tools        9.15.6755
```

The extra constraint is exactly `eta>=1`, requiring at least one deleted
nonpalette base edge.  The existing segment model has `eta=0`, so the two
chronology domains are disjoint.  The terminal response was

```text
status                 UNKNOWN
master iterations       1
decoded incumbents       0
connectivity cuts        0
solver walltime          7201.786005734 seconds
certificate_status       null
```

Thus even the initial relaxed degree master was inconclusive; the CEGAR
separator was never reached.  Final frozen hashes are

```text
result JSON  eda3638eaadd059bb3c5d229d59fbc2be515508cc701003f3829b994a4b2d00e
solver log   0201389758eb475142bd22eca23c51a7751e121841c16c626885259eea397fb8
model proto  f81051310ddc474025dd46fae050fe87db9fafb5cf02ac1fffb08df06c396a51
```

The proto was independently rebuilt with 0.001 seconds of search and exactly
reproduced the digest and 351,780/448,597 census.  The copied bundle is

```text
scratch/k15_pascal_edit5_cegar_20260729/
```

and the solver-free audit

```text
scratch/audit_k15_pascal_edit5_s15501_terminal_20260729.py
SHA-256 968ff6a7d7e642dcd2018c05b8e134dbd8b27e7b86a97fe0a981e8cc5df61829
```

passes under ordinary Python and `python -O`.  Its frozen output SHA-256 is
`d156e99d7c38690383b761cc69c3197334105a37ca322f4d293536de0139d3cd`.
The `0/0` objective/bound text in `ResponseStats()` is a satisfaction-API
default; the canonical solver log records `NA/NA`, so no bound exists.  No
third worker was launched.

The copied directory is self-contained: it includes the two frozen inputs,
both source files needed for the proto rebuild, the terminal result and log,
the rebuild artifacts, and the independent audit.  Their relative paths and
SHA-256 digests are bound by

```text
scratch/k15_pascal_edit5_cegar_20260729/bundle.sha256
SHA-256 9e5bd2a19b72e7fd48f99560f39c4a4b0c45b0fe64bd76b99cc753e6aa236dde
```

## 10. Exact remaining boundary

The 305-segment result is `UNKNOWN`.  Therefore:

* no hard-resident full-`q1` path in that palette was found;
* no path in that palette was ruled out;
* its `eta=0` chronology class remains open;
* the disjoint edit-five `eta>=1` run cannot, by itself, close the missing
  `eta=0` class even if it eventually returns `INFEASIBLE`.

The complete radius-five question is the union of the still-open palette
part and the still-open `outside-live` part.  Both disjoint runs terminated
`UNKNOWN`, so neither half is closed and no radius-five existence or
infeasibility conclusion follows.

The edit-five artifact contains no candidate factor and no connectivity
shore.  Its exact conclusion is only that the bounded first master solve was
inconclusive.

Independently of that status, Theorems 4.1 and 5.1 prove that edit radii at
most four cannot solve even the lower exact-rainbow/hard-residence gate on
this frozen parent path.
