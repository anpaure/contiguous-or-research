# K17 OPTIMAL28: exact compatible pure-hex master semantics

Date: 2026-07-31  
Status: exact reduction and schema audit; no pure-hex feasible selection or
K17 word is claimed

## 1. Frozen column system

Let `G=(C,O;E_0)` be the rank-eight/rank-nine incidence factor reconstructed
from

`scratch/k17_opt28_connected_owner_cycle_20260731.word`.

Every vertex of `C union O` has degree two in `E_0`.  The frozen catalogue

`scratch/threadD_k17_opt28_hex_variant_catalogue_20260731.audit.json`

contains `5433` columns.  For a column `h`, write

* `M_h subset E_0` for its three `removed_incidences`;
* `A_h subset (E(G)\E_0)` for its three `added_incidences`;
* `O_h` for its three owner vertices;
* `C_h` for its three colour vertices; and
* `R_h subset [724]` for its `hit_rows`.

For every `h`, the signed vector `1_(A_h)-1_(M_h)` has zero degree at each
owner and each colour.  All three removed incidences belong to `E_0`, and all
three added incidences lie outside `E_0`.

The catalogue is therefore complete for the smallest nonzero
degree-neutral incidence moves, but it contains neither an `R_3` transfer
table nor an upper-provider bank.  Those data must be reconstructed from the
literal factor; `hit_rows` alone is not a residence certificate.

## 2. Exact incidence-compatible master

Use one binary variable `y_h` per catalogue column and put, for every
rank-eight/rank-nine incidence `e`,

\[
 x_e={\bf1}_{e\in E_0}
      -\sum_{h:e\in M_h}y_h
      +\sum_{h:e\in A_h}y_h.                 \tag{2.1}
\]

### Theorem 2.1 (binary incidence bounds are necessary and sufficient)

The selected columns compose to a simple degree-two incidence factor if and
only if

\[
                         0\le x_e\le1                 \tag{2.2}
\]

for every incidence occurring in a column.  No additional owner-degree,
colour-degree, or lower-palette row is necessary.

#### Proof

Necessity is immediate.  Conversely, (2.2) makes the affine vector (2.1)
binary.  Summing (2.1) at any owner or colour cancels every selected
column's one positive and one negative incidence at that vertex.  Its degree
therefore remains two.  In particular, every rank-eight colour occurs once
as a projected factor edge and the complete lower palette is retained.
\(\square\)

Because `M_h subset E_0` and `A_h cap E_0=empty`, (2.2) is equivalently the
two families of clique rows

\[
 \sum_{h:e\in M_h}y_h\le1\quad(e\in E_0),\qquad
 \sum_{h:e\in A_h}y_h\le1\quad(e\notin E_0).         \tag{2.3}
\]

The frozen degrees of these resource cliques are:

```text
removed-incidence resources  10,931, column degree 1..7
added-incidence resources    13,341, column degree 1..4
```

The phrase **resource-disjoint** must not be used ambiguously.  There are
three distinct faces.

1. `(2.3)` is the largest exact incidence-compatible pure-hex face.
2. Requiring `sum_(h:v in O_h)y_h<=1` and
   `sum_(h:c in C_h)y_h<=1` is the strictly smaller changed-vertex-disjoint
   face.  The catalogue uses `8522` changed owners and `8392` colours, each
   of column degree `1..12`.
3. Requiring disjoint physical collars must also include each
   `fixed_other_owner` and its requested collar.  This is smaller again.

Only the third face makes precomputed local residence or provider deltas
automatically additive.  Neither owner/colour disjointness nor collar
disjointness is required for exact factor feasibility if literal replay is
used.

## 3. Marked packet and old-hazard rows

The protected set is the union of `106` `path_raw_components` and `28`
`optional_components`.  It contains every owner in those component words
and the `133` internal connector owners, for `4108` marked owners in total.
The literal component signature used by the source audit is

\[
              (\hbox{ordered port tuple},\hbox{ordered macro-block tuple}).
                                                               \tag{3.1}
\]

Every catalogue column avoids all `4108` marked owners.  Moreover, direct
replay finds zero catalogue columns whose recorded `fixed_other_owner` is
marked.  Hence both
incidences at each marked owner remain unchanged under (2.2).  All internal
marked adjacencies, all `133` marked connector turns, and the boundary port
incidences on the marked side are therefore fixed.  Thus all `134`
signatures and the literal marked packet path are preserved automatically;
there is no additional packet row for this frozen catalogue.  A future
catalogue may allow an exterior endpoint attached to a marked boundary
colour to change; it would then need the explicit strong packet guard rather
than owner avoidance alone.

Every inherited bad run `r` must lose at least one of its supporting old
incidences.  Since the catalogue only records columns which do so, the exact
old-hazard rows are

\[
                     \sum_{h:r\in R_h}y_h\ge1
             \qquad(r=0,\ldots,723).                 \tag{3.2}
\]

These rows are necessary, not sufficient: they destroy every old bad path
but do not exclude a new bad path.

Let `P` be the frozen packing of `452` pairwise edge-disjoint bad-run
intervals.  A removed old factor incidence destroys one old owner edge and
can meet at most one member of `P`; one hex removes three such incidences.
Consequently

\[
 \sum_h |R_h\cap P|y_h\ge452,
 \qquad |R_h\cap P|\le3,
 \qquad \sum_hy_h\ge151.                              \tag{3.3}
\]

Equation (3.3), and its restriction to every subpacking of `P`, is the
sharp currently certified Hall-type deletion-capacity row.  The weaker
`ceil(724/5)=145` bound should not be used in the master.

## 4. Exact lazy `R_3` separation

Project a feasible incidence vector to owner edges.  For a colour `c` and
two owners `u,v` introduce, only when needed,

\[
 b_{cuv}=x_{cu}\wedge x_{cv}                          \tag{4.1}
\]

with the three standard AND inequalities.  Since `c` has degree two,
`b_{cuv}=1` says exactly that the projected factor uses the owner edge
`u--v` with lower colour `c`.

Delete the fixed marked path interiors and read every resulting complement
path/cycle literally.  Suppose a candidate contains a strict owner run

\[
 q_0,q_1,\ldots,q_\ell,q_{\ell+1},\qquad
 1\le\ell\le3,                                      \tag{4.2}
\]

for some coordinate, with the coordinate absent from `q_0,q_(ell+1)` and
present in the `ell` internal owners.  If `e_i` is the coloured factor edge
between `q_i,q_(i+1)`, install the exact lazy motif cut

\[
                         \sum_{i=0}^{\ell} b_{e_i}\le\ell.  \tag{4.3}
\]

All `ell+1` edges would force (4.2) as a contiguous factor path because the
factor is degree two; conversely removing any one destroys that occurrence.
Thus (4.3) is an exact minimal path-edge cut.  It remains valid when a later
column repairs the candidate by deleting a formerly retained baseline edge.

This qualification matters.  The unguarded incumbent cut

\[
                 \sum_{h\in S}y_h\le |S|-1
\]

is generally **unsound** for an `R_3` defect: a compatible extra hex can
destroy one of the retained baseline edges of the bad path.  Use final-edge
variables as in (4.3), or emit the equivalent guarded clause containing
both the selected edge creators and every currently false edge-destroyer.

For facet-mode physicalization, (4.2) is exactly the owner-side form of a
strict facet run below three after the one-unit diamond erosion.  Endpoint
runs are not rejected before the residual connector solve; they are exported
in the left/right `R_3` collar and may be merged at a later seam.  In
addition to (4.3), the separator must reject a literal internally empty
maximal-envelope letter or an internal three-window replay failure.  Such a
failure is again supported on a concrete final factor path and receives the
same guarded edge-path cut.  Exact `D2` replay makes a separate `D3` row
redundant, though `D3` remains a useful independent audit.

## 5. Protected rank-ten--twelve objective

There are two different quantities which must not be conflated.

### 5.1 Exact static bank loss

Enumerate every baseline interval occurrence `p` of every protected target
of ranks `10,11,12` inside the frozen complement component words.  Let
`E(p)` be its coloured factor-edge path, and introduce

\[
                 s_p=\bigwedge_{e\in E(p)}b_e.          \tag{5.1}
\]

Then

\[
 L_{occ}=\sum_p w_p(1-s_p)                              \tag{5.2}
\]

is the exact loss of banked physical provider occurrences.  One useful
lexicographic objective is:

1. minimize destroyed unique-provider targets;
2. minimize targets for which every banked occurrence is destroyed; and
3. minimize the remaining weighted occurrence loss (5.2).

The ANDs in (5.1) retain all cross-column interactions.  Summing independent
per-hex deltas is unsound outside the collar-disjoint face.

### 5.2 Exact final target coverage

Loss of every baseline occurrence is not the same as a final target hole:
new factor paths can create a new provider.  Conversely, separately good
column deltas can cancel after composition.  Exact target preservation is

\[
                  \mu'_T\ge1                            \tag{5.3}
\]

for every protected target `T`, where `mu'_T` is obtained by literal
component replay or by the target-labelled accumulated-union monoid
`U_12`.  The safe workflow is therefore to optimize (5.2), reconstruct the
candidate factor, replay all rank-ten--twelve targets, and lazily install
the exact target automaton/guarded provider row for every missed target.
A baseline-only constraint `sum_(p for T)s_p>=1` is sufficient but not
necessary and would wrongly exclude solutions relying on gained providers.

Ranks `13,...,17` are currently complete but are not protected by an
`h=12` state.  They require literal replay, `U_17`, or explicit immutable
witness tickets before any final physicalization claim.

## 6. Hall/conflict cores and exact scope

For the LP relaxation of (2.3),(3.2), an exact Farkas/Hall certificate is a
pair of nonnegative multiplier families `alpha_r` on hazard rows and
`beta_q` on resource-capacity rows such that

\[
 \sum_{r\in R_h}\alpha_r
       \le \sum_{q:h\text{ consumes }q}\beta_q
 \quad\hbox{for every column }h,
 \qquad
 \sum_r\alpha_r>\sum_q\beta_q.                         \tag{6.1}
\]

This proves fractional, hence integral, infeasibility of the displayed
core.  In the integral problem the columns form a set-cover/packing system,
not a bipartite matching; there is no ordinary Hall iff theorem.  For a
hazard subset `A`, the exact integral deficiency is

\[
 \delta(A)=|A|-\max\{|A\cap\bigcup_{h\in J}R_h|:
             J\text{ satisfies the installed resource and }R_3\text{ rows}\}.
                                                               \tag{6.2}
\]

A positive `delta(A)` with the induced columns, resource rows, installed
guarded motifs, and a replayable integer proof is the appropriate exact
conflict core.  A solver timeout or a failure of a heuristic cover is not
such a core.

Thus the minimum proof-safe pipeline is:

1. eager (2.3), (3.2), and (3.3);
2. exact factor reconstruction;
3. guarded internal `R_3`/envelope cuts (4.3);
4. static provider-bank objective (5.2) followed by exact `U_12` and
   ranks `13+` replay;
5. a fresh residual owner/socket `b`-flow with all selected physical
   incidences guarded; and
6. literal two-bank/common-cap replay.

Feasibility through step 4 is only a repaired skeleton, not a K17 word.
Infeasibility justifies escalation to arity-two split/merge packets only for
the components appearing in a replayed positive core such as (6.2), not for
all `257` components indiscriminately.

## 7. Two exact outer faces

The same hex variables support two different exact searches.  Their results
must be labelled separately.

### 7.1 Full cycle-preserving face

Keep every final incidence in (2.1).  The projected owner graph is a
two-factor.  Add ordinary subtour cuts until it is one cycle, anchor its
orientation on the unchanged marked interval, materialize the unique
two-bank row, and apply Sections 4--5 literally.  No residual pairing is
released.  This is the smaller **full-cycle face**.

### 7.2 Forest-first asymmetric face

Compose the selected hexes, but freeze only:

1. every final incidence at a tagged owner and every packet-side incidence;
2. both final incidences of each selected-touched colour; and
3. no other incidence.

Thus an active pure owner automatically has both changed incidences frozen,
while a pure `fixed_other_owner` has only its incidence at the touched colour
frozen.  Its unrelated colour remains free and contributes residual owner
demand one.  Freezing that second incidence would define a smaller sufficient
face, not the exact maximally released forest-first face.

Contract the resulting frozen paths.  A frozen zero-socket cycle is an
immediate obstruction.  Release all other pure-`U` incidences and solve a
fresh owner-to-port `b`-flow before topology and literal replay.  Internal
`R_3` failures of a frozen path are fatal; endpoint run state is exported to
the flow.  This is the larger **forest-first asymmetric face**.  It preserves
each selected hex on one side while allowing the untouched pure-owner side
to be regenerated, so it must not be audited as the full composed cycle.

For a fixed frozen graph, let `d(p)=2-deg_F(p)` be the residual demand of old
port `p`, let `b(u)=2-deg_F(u)` be the residual demand of pure owner `u`, and
let `N(u)` be its allowed residual ports after all pinned and forbidden
incidences are applied.  The degree completion is feasible if and only if
the two total demands agree and, for every port set `S`,

\[
 \sum_{p\in S}d(p)
 \le
 \sum_{u}\min\{b(u),|N(u)\cap S|\}.                 \tag{7.1}
\]

This is the exact capacitated Hall/min-cut criterion: give the source-to-owner
arc capacity `b(u)`, every owner-port incidence capacity one, and the
port-to-sink arc capacity `d(p)`.  A violated `S` and the reachable owner side
are a replayable residual-flow certificate.  Quotient connectivity remains a
separate subtour condition.

## 8. Certified arity-two escalation signature

Suppose an exact pure-hex core identifies a component family `K`.  An
arity-two option may be admitted only with the following lossless signature:

\[
 \Xi(e)=(B_e;\mathcal O_e,\mathcal C_e,\mathcal I_e^-,\mathcal I_e^+;
          \partial e;H_e;F_e;\mathsf R_3(e);
          \mathsf U_{12}^-(e),\mathsf U_{12}^+(e)).             \tag{8.1}
\]

Here:

* `B_e` is the one- or two-component input packet, including provenance and
  the oriented output path forest;
* `O_e,C_e` are the exact owner and lower-colour resources, and
  `I_e^-,I_e^+` are its removed/added incidences;
* `partial e` is the signed, occurrence-labelled socket current together
  with the pairing of trail endpoints;
* `H_e` is the set of inherited hazard rows killed;
* `F_e` is the set of forbidden incidences and required fixed-incidence
  guards relative to the retained pure-hex selection;
* `R_3(e)` is the internal defect set plus both endpoint collars; and
* `U_12^-,U_12^+` are target-labelled lost and gained provider occurrences,
  not merely target counts.

An option is **closed guarded** only if its interior owner/colour resource
delta is zero, all nonzero current occurs at its advertised sockets, it has
no internal `R_3` defect, every forbidden-incidence guard is false, and its
joint protected-provider ledger is compatible with the other selected
options.  Marginal provider safety is insufficient.

There is a genuine Rado theorem only after physical installability has been
proved to be a matroid.  The useful sufficient interface is a common directed
unit-capacity socket/resource network `N`: each closed option is represented
by a source vertex with its allowed source-to-sink routes, and a set of
options is installable exactly when routes can be chosen vertex-disjoint.
These installable sets form the strict gammoid `M(N)`.  If `A_i` is the
guarded option set serving core
obligation `i`, then a simultaneous escalation exists if and only if

\[
 r_{M(N)}\left(\bigcup_{i\in X}A_i\right)\ge |X|
       \quad\text{for every }X.                     \tag{8.2}
\]

The rank in (8.2) is an exact max-flow value.  A failed set `X` together
with a minimum vertex cut of capacity below `|X|` is the certified Rado
core to freeze and escalate.  The exact deficiency is

\[
 \max_X\left(|X|-r_{M(N)}(\bigcup_{i\in X}A_i)\right).          \tag{8.3}
\]

Two qualifications prevent circular use of (8.2).

1. An arity-two option services two components.  To use Rado, the obligation
   packets (or a target-plus-helper convention) must be fixed first; allowing
   the same option to choose its pairing and represent two independent
   obligations introduces a hypergraph consistency constraint, not a Rado
   transversal.
2. Arbitrary multi-resource set packing and joint provider guards are not
   matroids.  If the routes in `N` are only sufficient, a min-cut excludes
   only that routed atlas.  If no exact gammoid/laminar representation has
   been proved, retain the integral option master and call its proof a
   conflict core, not a Rado core.

After an arity-two selection, its socket current feeds the residual
capacitated Hall system (7.1).  Thus a proof-carrying escalation consists of
the signature (8.1), a Rado cut when (8.2) applies, and the separate residual
port min-cut from (7.1).

## 9. Audited catalogue statistics

The following counts were obtained by a lightweight direct parse of the
frozen JSON; no optimization was run.

```text
columns                                              5,433
changed owners used                                  8,522, degree 1..12
lower colours used                                   8,392, degree 1..12
removed incidences                                  10,931, degree 1..7
added incidences                                    13,341, degree 1..4
hazard rows of catalogue degree exactly two              6
```

These figures are model-size diagnostics, not feasibility evidence.
