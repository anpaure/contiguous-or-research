# Lane W audit: CAA deployment, soft homotopy, and exact branch scope

Date: 2026-07-28

## 0. Audited verdict

No CAA solve should be launched through the old adaptive-motif route.
The deployment-correct route has the following frozen interface.

1. In the relabel catalogue
   
   ```text
   TRANSPOSITIONS = ((1,12),(3,4),(10,11),(3,13))
   ```
   
   every entry is a **zero-based bit index** in `{0,...,14}`.  The one-based
   mathematical pairs are `(2,13),(4,5),(11,12),(4,14)`.
2. On the H100 host the synchronized repository is
   `/dev/shm/k15_rotation`, and OR-Tools is imported only after
   
   ```bash
   export PYTHONPATH=/dev/shm/orlib
   ```
   
   The old `/workspace/problem` default is wrong for this deployment.
3. A measured five-parent shore has about 11.8 million centered motifs and a
   474 MB serialized file.  Iterative motif Benders is therefore disabled by
   default.  Accumulated shores are encoded over the exact 19,311 physical
   positions instead.
4. The old hard `--maximize-fixed-min-slack` mode is not erroneous: each row
   is already hard constrained, so its nonnegative margin merely optimizes
   surplus inside the hard-feasible region.  A distinct
   `--soft-fixed-homotopy` mode suppresses those hard rows, optimizes a signed
   margin in `[-W,W]`, writes the incumbent path, restores the unchanged hard
   rows, and uses the path only as a hint.  Accumulated moving-DM rows remain
   hard in both phases.
5. Two-parent fixed-DM motif tables are not globally exact on the five-parent
   consumer.  Their producer arc catalogue is smaller, and pair-only endpoint
   maxima optimize over the wrong collar language.  They yield pair-escape
   consequences for a terminal Hall-perfect carrier, but they are not five
   globally exact shore predicates.  The solver now rejects a purported
   fixed exact/projected table unless its directed edge table equals the
   consumer table.

No Hall-perfect carrier and no five-parent no-go is claimed here.  The safe
next action is a one-cut position-channel smoke run.

## 1. Exact position-shore theorem

Let the selected chronology be

\[
 P=(P_0,\ldots,P_{W-1}),\qquad W=6435,
\]

and set, for `0 <= j <= W+2`,

\[
 Q_j=\bigcap_{i=\max(0,j-3)}^{\min(j,W-1)}P_i.
\]

For `h in {0,1,2}` and `0 <= b <= W+2-h`, define

\[
 E_{b,h}=\bigcup_{j=b}^{b+h}Q_j
\]

and

\[
 M_{b,h}=\begin{cases}
 E_{b,h}\setminus Q_{b+h+1},&b+h<3,\\
 E_{b,h}\setminus Q_{b-1},&b\ge W,\\
 E_{b,h}\setminus(Q_{b-1}\cap Q_{b+h+1}),&\text{otherwise}.
 \end{cases}
\]

A lower target `T` fits cell `(b,h)` exactly when

\[
 M_{b,h}\subseteq T\subseteq E_{b,h},\qquad
 T\cap Q_j\ne\varnothing\quad(b\le j\le b+h).       \tag{1.1}
\]

There are

\[
 (W+3)+(W+2)+(W+1)=19311                         \tag{1.2}
\]

physical cells.

### Theorem 1.1 (position-indexed Hall equivalence)

Fix a nonempty lower-target shore `A` and integer allowance `a` with
`0 <= a < |A|`.  For each physical cell `c`, introduce one claim bit `z_c`,
one selected target `T_c in A`, and one selected coordinate in every required
intersection in (1.1).  Condition all fit constraints on `z_c=1` and impose

\[
                 \sum_c z_c\ge |A|-a.              \tag{1.3}
\]

For a fixed chronology, these auxiliary constraints are feasible if and only
if

\[
                 |N_P(A)|\ge |A|-a.                 \tag{1.4}
\]

#### Proof

Every true claim supplies a target satisfying (1.1), hence a genuine cell in
`N_P(A)`.  There is one claim per physical cell, so (1.3) counts distinct
right vertices.  Conversely, choose `|A|-a` fitting cells, choose one fitting
target for each, and choose one coordinate from each nonempty intersection
in (1.1).  Set precisely those claims to one.  This satisfies the encoding.
\(\square\)

The implementation also evaluates `M_{b,h}` by an independent complete-
carrier construction.  A persisted shore is accepted only in the versioned
format carrying its hashed source candidate and native `dm_cell_indices`.
Before installing the row, the loader reconstructs that source chronology and
reruns the native maximum-matching auditor.  It requires exact equality of the
rerun native target/cell lists, the saved lists, the formula cell list, and the
complete-carrier cell list.  This check occurs even if the next hard model is
immediately `INFEASIBLE`.  On each later feasible incumbent, the fixed-
shore native interface returns only its total, so the additional mandatory
post-solve check is equality of the position score and native total.  A
freshly returned DM shore also receives direct formula/carrier/native cell-
list equality before it is serialized.

## 2. Exact scale ledger

The shared order/compiler channel contributes 787,005 Boolean and 19,305
integer variables.  For one shore,

\[
 \sum_c(h(c)+1)=6438+2(6437)+3(6436)=38620.
\]

Consequently one hard shore contributes exactly

\[
 \begin{aligned}
 \text{Booleans}&=19311+15(19311)+2(38620)=386216,\\
 \text{integers}&=2(19311)+38620=77242,\\
 \text{constraints}&=32(19311)+4(38620)+1=772433.
 \end{aligned}                                      \tag{2.1}
\]

This is roughly 25 times fewer primary variables than 11.8 million motif
indicators, but repeated target arrays remain material.  A shore of size
1,524 places 29,429,964 constants into the 19,311 target-selection `Element`
constraints.  Therefore the position representation makes a first exact cut
plausible; it does not prove that hundreds of simultaneous cuts fit in
memory.  A one-cut resource smoke is mandatory before a long Benders run.

## 3. Hard mode versus soft homotopy

Let the fixed scored rows be `s_i(x)` with thresholds `t_i`.

### Hard mode

The original builders impose

\[
 s_i(x)\ge t_i\qquad\text{for every }i.
\]

The variable used by `--maximize-fixed-min-slack` obeys

\[
 0\le z\le W,\qquad z\le s_i(x)-t_i.
\]

Its lower bound is redundant with the already hard rows.  Hence existing hard
pair-UNSAT results are unaffected; `[0,W]` was not a soundness bug in that
mode.

### Soft mode

The distinct `--soft-fixed-homotopy --hint-path FILE` phase instead omits the
rows `s_i>=t_i`, uses

\[
 -W\le z\le W,\qquad z\le s_i(x)-t_i,
\]

and maximizes `z`.  If it obtains an incumbent, it writes the complete middle
path to `FILE`.  It then clears the soft objective, installs every original
hard row, replaces all earlier hints by that full path, and runs the same hard
model.  A negative or positive soft margin is never an acceptance
certificate.  Only the hard solve and independent literal Hall audit count.

The implementation rejects simultaneous objective modes so a later
parent-overlap or balanced-window objective cannot silently overwrite the
min-margin objective.

Persisted `--global-exact-dm-shore` rows are deliberately outside this soft
family: they are installed as hard constraints before either phase and stay
hard.

## 4. Exact producer/consumer boundary

Let `E_prod` be the directed edge table serialized in a fixed motif file and
`E_cons` the directed arc table loaded by the CP-SAT consumer.  Exactness of a
full fixed-DM motif sum requires

\[
                         E_{prod}=E_{cons}.             \tag{4.1}
\]

Containment is insufficient.  If `E_prod` is a two-parent face and `E_cons`
is the 23,628-arc five-parent union, mixed-parent positive local words are
absent from the file.  Moreover, endpoint-upper values generated on the pair
maximize over pair collars, not over five-parent collars.  Thus neither the
interior total nor its endpoint completion is globally exact.

The fixed exact, projected fixed, multi-fixed, adaptive exact, and
required-target consumers now assert (4.1) before adding a row.  For a branch
represented by fixing full-catalogue variables to zero, the safe moving-shore
route remains the position channel on that actual selected chronology; a
smaller pair table is not reused as a full-branch scorer.

The option `--exact-fixed-interior-only` deliberately deletes valid endpoint
credit and is therefore a strengthening, not a necessary Hall relaxation.
An `INFEASIBLE` result obtained with it is now labelled
`EXPLORATORY_INFEASIBLE`, returned as inconclusive by the outer driver, and
never promoted to a Hall no-go.

## 5. Canonical branch cover and its scope

For the canonical parents `P_0,...,P_4`, let `src(e)` be the complete set of
parents supplying augmented arc `e`, including dummy-to-start and
end-to-dummy arcs.  For a proposed minimal cover `S`, impose

\[
 x_e=0\quad\text{when }src(e)\cap S=\varnothing,       \tag{5.1}
\]

and, for every `p in S`,

\[
 \bigvee_{p\in src(e),\ src(e)\cap(S\setminus\{p\})=\varnothing}x_e.
                                                               \tag{5.2}
\]

The ten certified pair no-gos imply only the terminal escape clauses

\[
 \bigvee_{src(e)\cap\{i,j\}=\varnothing}x_e,
 \qquad0\le i<j<5.                                   \tag{5.3}
\]

Every Hall-perfect canonical carrier has a minimal cover of size at least
three.  Hence the ten triples, five quadruples, and one full set give an
exhaustive 16-branch terminal search.  All clauses use augmented parent
support, ordinary parent orientations, parent-only dummy endpoints, and the
resident legal-state model.

The premise is frozen to these ordered SHA-256 hashes:

```text
5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c
6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
6d7cee2418f10dbd02076971fdd119d7bc7c35d154430522a70c06f953687ea7
8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd
2b25279185b50a9485c65cbc727a08d95b71a1d310332cbdcb23dd6b0b3d2cb7
```

It does **not** apply to the base-plus-four-relabels CAA catalogue.  The
canonical branch launcher refuses `--pair-escape-cuts` unless all five hashes
match.  The ordinary CAA launcher applies no pair escapes and omits no small
support faces.

Finally, (5.3) is the only global consequence imported from the pair no-gos.
The five pair-local fixed-DM face predicates are not installed in the
five-parent branch model.  Every moving shore is scored on the full/branch
chronology by Theorem 1.1; feasible incumbents receive the native total/list
checks just distinguished above.

## 6. Deployment commands and exact stopping rule

The ordinary relabel-catalogue smoke run is

```bash
cd /dev/shm/k15_rotation
export PYTHONPATH=/dev/shm/orlib
scratch/launch_k15_caa29_h100_cpu.sh \
  /dev/shm/caa29_position \
  /dev/shm/k15_rotation \
  smoke
```

The canonical branch smoke for, for example, branch `013` is

```bash
cd /dev/shm/k15_rotation
export PYTHONPATH=/dev/shm/orlib
scratch/launch_k15_canonical_branch_benders_h100_cpu.sh \
  /dev/shm/caa29_canonical_branches \
  013 \
  /dev/shm/k15_rotation \
  smoke
```

Both launchers default to a two-round smoke, so the second outer round builds
at most the first persisted position shore.  `full` is an explicit opt-in and
defaults to 16 outer rounds; environment variables may change the limits.

At every outer round, the native Hall auditor computes a maximum matching.
If its size is below 16,383, its current DM shore is saved with allowance zero
and becomes a hard position row on the next invocation.  A relocated defect
is therefore separated again.  Terminal success requires a 16,383-edge
matching and equal Koenig cover emitted by the native auditor and checked by
the independent verifier.

`TIMEOUT`, `UNKNOWN`, a smoke limit, or a Benders round limit is
inconclusive.  `INFEASIBLE` proves a no-go only for the exact catalogue,
support branch, residence/upper model, and accumulated literal shores in that
run; absent a separately checkable proof log, this remains a trusted-solver
computational certificate rather than a solver-independent derivation.  A
global canonical-five no-go requires exact `INFEASIBLE` completion of all 16
branches.  No such completion has been run here.

## 7. Files audited or changed

* `scratch/search_k15_directed_parent_union_cpsat.py`: separate soft
  homotopy, augmented support branching, exact producer/consumer assertions,
  repeatable hard position shores, native post-solve equality checks.
* `scratch/search_k15_caa29_five_parent_benders.py`: zero-based metadata,
  position-shore persistence by default, explicit legacy motif opt-in,
  optional canonical branch arguments and hash guard.
* `scratch/launch_k15_caa29_h100_cpu.sh`: correct H100 repository and
  `PYTHONPATH`; position smoke by default.
* `scratch/launch_k15_canonical_branch_benders_h100_cpu.sh`: the guarded
  10+5+1 canonical terminal branch portfolio.
* `MATH_AUDIT_W_CAA29_POSITION_LITERAL_HALL_SCALE_AND_BRANCH_SCOPE_20260728.md`:
  independent position-channel theorem and exact variable/constraint census.
