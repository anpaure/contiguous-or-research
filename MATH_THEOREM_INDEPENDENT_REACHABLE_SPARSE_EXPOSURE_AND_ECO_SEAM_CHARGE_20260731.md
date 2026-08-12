# Reachable sparse exposure: the exact ECO seam charge and the weakest bounded-state theorem

Date: 2026-07-31  
Status: proved implication, explicit `24`-seam coefficient on the prepared
all-six ECO face, and exact counterexamples to the unqualified statement.
Existence of the required protected Pascal/ECO lift in every dimension is
open.  No unconditional `B(k)+O(1)` theorem is claimed.

## 0. Verdict

The statement

\[
                 s\le a\Phi+s_0                                      \tag{0.1}
\]

is false when `Phi` is only the number of terminal holes or the Hall defect
of the current compiler.  A disjoint union of arbitrarily many internally
perfect guarded path blocks has zero such defect and needs arbitrarily many
physical joins.

There is, however, an exact positive form which is already supported by the
repository's physical ECO theorem.  Make every nonterminal obstruction a
named **carried repair token**, including topology/component debt and
minimum-run compensation debt.  Suppose that a two-coordinate Pascal lift
creates at most one child task in each of the four phases of every token,
plus an absolute birth bank.  If every child task is realized by one
prepared all-six coherent ECO packet, all packets lie in one common-
connector, halo-separated cube, and there are only absolutely many
structural seams, then

\[
                 \boxed{s\le24\Phi+s_0}.                              \tag{0.2}
\]

The coefficient is literal:

\[
       4\ \hbox{child phases per token}
       \quad\times\quad
       6\ \hbox{changed physical seams per ECO packet}.
\]

The AD seam theorem then groups every row of a **declared maximum dependency
span** `D_m` into one compound task per seam.  This is an `O(d)` collar only
after a separate protected-upper compression/tail-regeneration theorem has
reduced all carried upper information to `D_m=O(d)`.  Literal all-width
upper replay can have `D_m=Theta(m)` and does not receive this reduction for
free.  On a bounded sublevel `Phi<=E`, the
selector therefore sees only absolutely many tasks.  Quadratic packet
lists and the stated `O(mD)` pairwise exclusion hypothesis are
then enough for deterministic greedy selection when `D=o(m)`.

Equation (0.2) is a theorem **conditional on the prepared Pascal/ECO
lift**.  Current results prove the six-seam atom and the compound-collar
partition, but do not construct the required common-connector,
residence-safe, upper-bank-preserving, common-cap packet cube uniformly in
the dimension.  This is the remaining construction, not a missing counting
argument.

Finally, a linear bound such as (0.1) is stronger than the additive-
constant induction actually needs.  It is enough that one bounded
reachable sublevel, or even one infinite compatible spine, have a uniform
absolute seam bound.  This gives the weakest exact target in Section 6.

## 1. The carried defect potential

A recursive auxiliary state `g` contains a finite set `D(g)` of named
carried repair tokens.  The bank must include every nonterminal obstruction
which can force a physical change at the next step.  In particular it has
typed subbanks for

1. unmatched compiler/common-cap sources;
2. missing protected upper providers or central owner occurrences;
3. minimum-run packets which require compensation rather than passive
   residence transport; and
4. component/connector debt not already contained in a protected baseline
   chronology.

Terminal holes which are appended and forgotten are not carried tokens.
Define

\[
                         \Phi(g):=|D(g)|.                             \tag{1.1}
\]

Weights may be used instead, provided every token has weight at least one
and the child-task multiplicity below is changed accordingly.

This definition is intentionally occurrence-labelled.  Two defects with
the same target mask but requiring different physical occurrences are two
tokens.  Conversely, an entire `O(d)` seam collar is one token only if one
whole packet choice certifies every residence, shadow, erosion, topology
and cap row in that collar.

### Definition 1.1 (four-phase protected Pascal exposure)

A provisional two-coordinate lift of `g` has four-phase exposure when its
nonstructural child task bank `U` admits an injection

\[
 U\setminus U_0\longrightarrow D(g)\times\{00,01,10,11\},             \tag{1.2}
\]

where `|U_0|<=b` for one absolute birth constant `b`.  Consequently

\[
                         |U|\le4\Phi(g)+b.                            \tag{1.3}
\]

Passive descendants of a declared upper hole satisfy this four-phase
count.  Existing Pascal identities do **not** prove (1.2) automatically for
residence, topology or the child compiler.  Those rows must either be
included in `D(g)`, reset inside the protected lift, or charged to `U_0` by
an independently proved absolute birth theorem.

Thus Definition 1.1 is a named construction property, not a consequence of
calling `D(g)` a token bank.  Proving it for every row of one reachable
Pascal state is part of the missing exposure theorem.

## 2. The explicit ECO seam theorem

Fix a provisional protected child chronology `T_*`.  Let `J_str` be an
absolute structural boundary/opening bank with

\[
                         |J_{str}|\le s_{str}.                         \tag{2.1}
\]

For each task `u in U`, choose one prepared all-six coherent ECO atom.  We
assume exactly the hypotheses under which the repository's six-edge theorem
is compositional:

* the atom supports are pairwise physical-port-disjoint;
* the atoms form a literal common cube with one fixed decoration;
* every cube state has the same legal connector set; and
* the dependency halos needed below are separated, or their full joint
  table is included in the packet.

Let `T` be the chronology obtained by toggling the chosen atoms and applying
the fixed structural opening.

### Theorem 2.1 (explicit reachable seam charge)

Under the preceding hypotheses, the one-sided changed-seam count between
`T_*` and `T` satisfies

\[
 \begin{aligned}
 s&\le s_{str}+6|U|\\
  &\le24\Phi(g)+(s_{str}+6b).                         \tag{2.2}
 \end{aligned}
\]

Thus (0.1) holds with

\[
                         a=24,\qquad s_0=s_{str}+6b.                 \tag{2.3}
\]

If one task needs at most `h` all-six atoms rather than one, the same proof
gives `a=24h` and `s_0=s_str+6hb`.

#### Proof

The exact decorated ECO lift replaces six old Johnson edges by six new
Johnson edges.  Under the common connector, these are exactly six old-only
and six new-only chronology seams.  Pairwise support disjointness and the
common-cube hypothesis make the symmetric differences additive; without
disjointness the union bound still gives at most six seams per composable
atom.  The structural bank contributes at most `s_str`.  Substitute (1.3).
\(\square\)

The theorem compares two complete child chronologies.  Seams already
present in the protected baseline are not charged again.  If the baseline
is only a path forest and must first be linearized, its connector edges
belong either to `J_str` or to topology tokens in `D(g)`; silently omitting
them invalidates (2.2).

## 3. One compound task per physical seam

Let `D_m` be the largest owner dependency span of every row which must be
preserved: upper-shadow windows, residence walls, erosion envelopes and
compiler cells.  For old-only and new-only seam sets of common size `s`,
delete the old-only seams.  The common graph is a path-fragment system.

For a span `ell`, the AD seam identity gives exactly

\[
 b_\ell=\sum_P\min\{\ell,|V(P)|\}\le \ell s                          \tag{3.1}
\]

old boundary windows and the same number of new boundary windows.  Assign
each changed window to the least indexed changed seam in its span.

### Theorem 3.1 (compound-collar partition)

All changed rows through owner span `D_m` are the disjoint union of at most
`s` compound seam tasks.  One such task contains at most `ell` old and
`ell` new windows at span `ell`, and its physical support lies in the union
of the old and new radius-`D_m` collars of its seam.  Hence its physical
support has size at most

\[
                         4D_m+O(1).                                  \tag{3.2}
\]

#### Proof

Every changed window contains a changed seam, so least-index assignment is
defined and unique.  A fixed cyclic seam lies in exactly `ell` based
`ell`-edge windows.  Every assigned window is contained in the radius-
`ell` collar of the seam.  Take the union over the two chronologies and
over `ell<=D_m`.  Equation (3.1) proves that no other changed window exists.
\(\square\)

The number of row labels inside a compound task may be `Theta(D_m^2)`.
Only the number of independently selected packets has been compressed.  A
candidate is valid only if it repairs the entire signed collar.

Combining Theorems 2.1 and 3.1 gives at most

\[
                  24\Phi(g)+s_0                                    \tag{3.3}

compound seam tasks.  A conservative selector which also keeps the
original child-source tasks separately sees at most

\[
                  H(g)\le28\Phi(g)+(7b+s_{str}+e_0),                \tag{3.4}
\]

where `e_0` is an absolute terminal/boundary task bank.  If each ECO choice
is already a whole packet containing all six of its seam collars, the six
collars need not be selected again and the sharper bound

\[
                  H(g)\le4\Phi(g)+b+s_{str}+e_0                     \tag{3.5}

holds.  Equations (3.4)--(3.5) are two encodings of the same physical
obligations, not two independent repair charges.

## 4. Bounded-bank selection

For each of the `H` compound tasks let `P_i` be its list of complete
guarded packets.  A packet includes the physical replacement, every
protected witness, its residence certificate, all topology resources and
its complete common-cap path ticket.  Assume absolute `alpha,beta>0` with

\[
       |P_i|\ge\alpha m^2,\qquad
       \#\{q\in P_j:q\hbox{ conflicts with }p\}\le\beta mD_m          \tag{4.1}
\]

for every `i!=j` and every fixed `p in P_i`.  Source-fixed quadratic-load
tokens must be private; (4.1) must include complete cap and topology
tickets, not only the six local hexagon ports.

### Theorem 4.1 (deterministic bounded-bank reset)

If

\[
                         \alpha m^2>(H-1)\beta mD_m,                 \tag{4.2}

\]

one can choose one mutually compatible packet from every list.

#### Proof

Choose lists in any order.  After `j` choices, at most `j beta mD_m`
candidates are forbidden in the next list.  Inequality (4.2) leaves a
candidate.  Induction gives the transversal.  Since complete tickets were
included in the conflict relation, the resulting repair composes
literally. \(\square\)

If a separate protected-upper compression theorem gives
`D_m=Theta(sqrt(m))`, then for an absolute `H`, (4.2) holds for all
sufficiently large `m`.  More generally the conclusion holds whenever
`D_m=o(m)`.  For literal all-width upper replay one may have
`D_m=Theta(m)`; then (4.2) is a nontrivial constant inequality and sparse
task count alone does not close it.  This is the precise scope in which
sparse reachable exposure avoids the cubic-load obstruction of the full
hexagon atlas.

## 5. Exact refutations of stronger readings

### Proposition 5.1 (compiler-only defect cannot bound seams)

For every `t`, there is an abstract protected sidecar with zero terminal
holes, zero compiler Hall defect, and `t` pairwise resource-private guarded
path blocks, for which every interior-preserving single chronology needs at
least `t-1` cross-block seams.

#### Proof

Give every block its own exact owner, witness and common-cap data.  The
disjoint union has no local defect.  Contract every protected block to one
vertex.  A single chronology induces a connected graph on the `t`
contracted vertices, which has at least `t-1` edges.  Each such edge is a
cross-block physical seam. \(\square\)

Thus (0.1) is false unless `Phi` charges component debt or the protected
baseline already contains the global connectors.

### Proposition 5.2 (ordinary residence defect cannot bound seams)

Let `R_1,...,R_t` be pairwise collar-separated minimum-run packets, each of
which becomes one unit too short under the Pascal residence identity.
Suppose one seam collar can meet at most `c` of them.  Any seam-only repair
uses at least `ceil(t/c)` seams, even if the current-depth residence defect
is zero.

#### Proof

Every packet must meet a repair collar; otherwise its run shortens below
the child threshold.  A union of `s` collars hits at most `cs` packets.
Hence `cs>=t`. \(\square\)

The potential must charge a minimum-run hitting/transversal bank or export
one extra unit of run margin.

### Proposition 5.3 (sparse exposure is not packet compatibility)

Two tasks can have distinct private source anchors and arbitrarily many
otherwise private packet choices while admitting no simultaneous choice.

#### Proof

Force every complete common-cap ticket for both lists through one cap-one
vertex `z`; duplicate all other resources privately.  Each task separately
has valid packets, but the two-source strict-gammoid rank is one. \(\square\)

Thus (2.2) and a bounded task count do not replace the whole-ticket
exclusion hypothesis (4.1) or a common-guard Rado/gammoid theorem.

### Proposition 5.4 (one reachable upper task can destroy quadratic supply)

At a standard Pascal incidence anchor, let the two hexagon parameters be
`b in B,c in C`, with `|B|=|C|=m`.  Let a two-tag child target have the
form

\[
              Y=P\cup E\cup\{x,y\},\qquad |E|=q-1.                 \tag{5.1}
\]

Suppose every old occurrence of `Y` is cut and every available replacement
interval for `(b,c)` contains a `c`-bearing packet atom, with no alternative
private witness.  Then safety forces `c in E`.  At least

\[
                         m(m-q+1)                                  \tag{5.2}
\]

of the `m^2` choices are bad, and the bad-pair graph contains
`K_(m,m-q+1)`.

#### Proof

The `c`-bearing atom puts coordinate `c` into the replacement union.  Since
the outside-anchor coordinates allowed by `Y` are exactly `E`, no-spill
forces `c in E`.  Every `c` outside `E` is therefore bad for all `m`
choices of `b`.  There are `m-q+1` such values. \(\square\)

For `q<=d=o(m)`, only `O(md)` choices may survive.  Thus bounded task count,
four-phase reachability and constant atom support do not imply the
quadratic-list row in Section 4.  One still needs an occurrence-private old
witness, a packet-private replacement ray, or the global Pascal exposed-ray
star-cover (`PERSC`) certificate.  Proposition 5.4 is conditional on its
explicit last-witness hypotheses; it is a no-deduction theorem, not a claim
that every reachable state contains such a target.

## 6. The weakest theorem actually sufficient for `B(k)+O(1)`

The global linear estimate (0.1) is convenient but unnecessary.  Fix an
invariant bound `E`.  It is enough to prove the following **bounded-sublevel
exposure statement**:

> There are absolute `E,S,B` and a finite authenticated base such that every
> recursively selected state with `Phi<=E` has one protected odd successor
> with at most `S` changed physical seams, at most `B` nonseam child tasks,
> a declared span `D_m=o(m)` (or directly (4.2) eventually), exact
> compound-collar packet lists satisfying (4.1), and regenerated
> state `Phi'<=E`.  The same state has odd and even terminal
> physicalizations of length `B(k)+O(1)` with `O(1)` terminal repair
> complexity.

### Theorem 6.1 (bounded-sublevel induction)

The bounded-sublevel exposure statement implies

\[
                            \nu(k)\le B(k)+O(1).                     \tag{6.1}

\]

#### Proof

On the sublevel, Theorem 3.1 gives at most `S` seam tasks, so the complete
selector has at most `H=4E+B+S+O(1)` lists.  Since `H` is absolute and
`D_m=o(m)`, Theorem 4.1 supplies a simultaneous repair above a finite
threshold.  By hypothesis the successor again has `Phi'<=E`; induction
gives one infinite odd spine.  The terminal repair theorem pays each
dimension's bounded terminal charge once rather than exporting it, yielding
(6.1). \(\square\)

It is weaker still to require the displayed property only along one
compatible infinite spine instead of left-totality over the whole
sublevel.  This is logically sufficient but less convenient to prove.

The explicit ECO estimate (2.2) is one certificate for the bounded-sublevel
seam row: on `Phi<=E`, take

\[
                         S=24E+s_0.                                \tag{6.2}

\]

## 7. What is proved and what remains conditional

Unconditional from current repository theorems:

1. one all-six coherent ECO toggle changes exactly six physical seams under
   a common connector;
2. a prepared separated common cube has additive seam symmetric
   differences;
3. `s` changed seams expose at most `ell s` old and `ell s` new windows at
   span `ell`, and these form at most `s` compound collars;
4. the deterministic finite-bank selector, once (4.1) is supplied; and
5. the four counterexamples/no-deduction theorems in Section 5.

Conditional/open:

1. a uniform protected Pascal baseline whose uncharged structural seam bank
   is absolute;
2. the four-phase bound (1.2) for topology, residence and compiler tasks,
   rather than passive upper holes alone;
3. a task-private, common-connector, residence-safe, upper-bank-preserving
   all-six ECO packet for every reachable task;
4. halo separation or an exact interacting collar table;
5. protected-upper compression/tail regeneration giving `D_m=o(m)`, or a
   stronger packet supply/exclusion inequality that handles `D_m=Theta(m)`;
6. a PERSC/private-replacement certificate retaining quadratic per-task
   upper-safe supply;
7. the `O(mD_m)` cross-list load including full common-cap and topology
   tickets; and
8. regeneration to one bounded exported state family.

Therefore the unqualified reachable-state sparse-exposure lemma is
refuted, while its exact prepared-ECO version is proved with coefficient
`24`.  The all-dimensional problem is now concentrated in constructing the
prepared packetized Pascal lift and showing that it regenerates a bounded
token bank.

## 8. Dependencies

* `MATH_THEOREM_AD_REPAIRED_ECO_SIX_SEAM_RSB_EXPORT_AND_CUBE_GUARDS_20260731.md`;
* `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`;
* `MATH_THEOREM_R_REACHABLE_COMPOUND_SEAM_COLLAR_GREEDY_INDUCTION_20260731.md`;
* `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md`;
* `MATH_THEOREM_K_ABSOLUTE_SPARSE_EXPOSURE_AND_COMPOUND_COLLAR_RESET_20260731.md`;
* `MATH_THEOREM_A_PASCAL_REACHABLE_UPPER_TASK_STAR_COVER_TEST_20260731.md`;
* `MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`.
