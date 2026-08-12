# Fixed-bank resource bounds and the schedule-free repeat-path contraction

Date: 2026-07-31  
Status: exact degree/codegree theorem and exact contraction theorem for the
authenticated adjacent-cut `s=1` GK seed after fixing the displayed
`572`-edge direct bank.  A bounded alternating descent gives an independently
replayed positive wedge fixture but leaves rank-nine and topology debt.  The
decisive unconditioned `13270`-edge joint master is not closed here.

## 1. Scope and outcome

This note supplements
`MATH_THEOREM_H2_K17_GK_CYCLIC_SECOND_CUT_PROVIDER_GATE_20260731.md`.
Fix its direct bank of SHA-256 `7abcbd84...`.  The residual relation has one
row for each of the remaining `8164` missing rank-six colours.  An option is
a supported Johnson edge, and consumes its rank-eight union, its two
rank-seven endpoints, and, for endpoint--unused (`EU`) edges, its forced
boundary rank-nine turn.

Three conclusions are rigorous.

1. The residual option hypergraph has exact small degrees but a genuine
   sparse left core: `165` rows have only two options.  Uniform
   high-degree/codegree nibble or independent-transversal hypotheses do not
   apply to this fixed bank.
2. For every clean acyclic provider selection, the repeat stage contracts to
   exactly `4535` nodes and `4534` edges, independently of the provider
   `EU` count and independently of any length-`4/5` segmentation.
3. A `900`-second one-core alternating descent preserves every marginal hard
   resource, removes all `17` illegal selected wedges, and reduces central
   rank-nine collision debt from `1764` to `628`.  The checkpoint still has
   one carrier cycle and is not a completion.  The run proves neither local
   optimality nor infeasibility.

## 2. Exact residual degree and codegree bounds

After deleting the fixed direct rows and their rank-eight, endpoint and
boundary-turn resources, the residual relation has

\[
  8164\text{ rows},\qquad 242771\text{ options}
   =57008\ (EU)+185763\ (UU).                       \tag{2.1}
\]

The row types are

\[
  3640\ UU\text{-only},\qquad1001\ EU\text{-only},\qquad
  3523\text{ mixed}.                                \tag{2.2}
\]

Hence every residual selection has

\[
                         1001\le b_{EU}\le4524.      \tag{2.3}
\]

Filler nonnegativity strengthens the lower bound to `b_EU>=1600`; see
Section 3.  The exact option-row degrees range from two to `55`, and exactly
`165` rows have degree two.

The maximum resource degrees are

\[
       \Delta(q_8)=28,\qquad\Delta(v_7)=70,
       \qquad\Delta(h_9^{\rm boundary})=25.          \tag{2.4}
\]

The first two ceilings are symbolic.  A rank-eight mask contains at most
`binom(8,6)=28` possible lower colours.  For a fixed rank-seven vertex, an
option chooses one of its seven coordinates to delete and one of the ten
outside coordinates to add, giving at most `7*10=70` carriers.  The boundary
maximum `25` is an exact literal census after the fixed reservations.

Three exact pair-codegree maxima are

\[
 \Delta_2(\text{row},v_7)=10,\qquad
 \Delta_2(q_8,v_7)=7,\qquad
 \Delta_2(v_7,v_7)=1.                               \tag{2.5}
\]

Indeed, after fixing a lower row and one intermediate vertex, only the ten
outside additions remain.  After fixing a rank-eight union and one of its
rank-seven subsets, only the seven possible deleted coordinates remain.
Two distinct intermediate vertices determine both their intersection and
union, hence determine the option.

These favourable codegrees do not by themselves imply a transversal.  The
minimum row degree is two, while options conflict simultaneously through a
rank-eight resource, two rank-seven resources and possibly a boundary turn.
Thus neither a uniform Pippenger--Spencer-type nibble nor the standard
`|list|>=2 Delta` independent-transversal bound applies.  Ordinary Hall on
only the rank-eight shore is also strictly weaker than this multi-resource
selection problem.

## 3. Schedule-free path-contraction theorem

Let `S` be any residual choice of one `EU` or `UU` provider for every one of
the `8164` rows, satisfying rank-eight injectivity, old-endpoint capacity one
and unused-vertex capacity two.  Include the `3640` seed edges and the `572`
fixed direct edges.  Put

* `b` = the number of selected residual `EU` edges;
* `n_i` = the number of the `12168` unused rank-seven vertices having
  selected degree `i`, for `i=0,1,2`;
* `t=n_1+n_2`, the number of unused vertices touched by `S`.

### Theorem 3.1

If the resulting provider carrier is acyclic, it is a forest of exactly

\[
                              t-5096                 \tag{3.1}
\]

paths.  To reach the exact owner budget, adjoin `9631-t` currently untouched
unused vertices as singleton contracted nodes.  The repeat edge counts are
forced to be

\[
          r_{EU}=6134-b,\qquad r_{UU}=b-1600.        \tag{3.2}
\]

They are nonnegative exactly when `1600<=b<=6134`; in the conditioned bank,
(2.3) sharpens the upper endpoint to `4524`.  After contracting every
provider path, the repeat problem always has

\[
                         4535\text{ nodes and }4534\text{ edges}. \tag{3.3}
\]

If those repeat edges form a connected graph while respecting final degree
at most two, the literal carrier is one path and has exactly two old
endpoints.

### Proof

The residual selected edges have unused-vertex incidence count

\[
                  n_1+2n_2=b+2(8164-b)=16328-b.     \tag{3.4}
\]

The provider carrier has `7280+t` vertices and

\[
                        3640+572+8164=12376          \tag{3.5}
\]

edges.  Under acyclicity, its component count is therefore
`7280+t-12376=t-5096`.  Maximum degree two makes every component a path.

After the direct bank, `6136` old endpoints remain.  The residual `EU` edges
consume `b` of them, and the final path must leave exactly two.  This forces
`r_EU=6136-b-2=6134-b`.  Since there are `4534` repeat edges in total,
`r_UU=4534-r_EU=b-1600`.

The unused-side incidence demanded by these repeat edges is

\[
 r_{EU}+2r_{UU}=2934+b.                             \tag{3.6}
\]

The existing degree-one unused vertices need one incidence each, while the
`9631-t` new singleton vertices need two each.  By (3.4),

\[
 n_1+2(9631-t)=2934+b,                              \tag{3.7}
\]

so the incidence ledger is exact.  Finally, contracting the provider paths
and adding the singleton unused vertices gives

\[
 (t-5096)+(9631-t)=4535                             \tag{3.8}
\]

nodes.  A connected graph on these nodes with `4534` edges is a tree; a tree
of maximum degree two is a path.  Equation (3.2) leaves precisely two old
endpoints.  This proves every claim. \(\square\)

The hypothesis that the provider carrier is acyclic is load-bearing.  A
cycle cannot be destroyed by adding repeat edges.

## 4. Exact Rado and Hall interfaces after topology is exposed

There are two useful exact reductions, neither of which alone proves the
repeat path.

First, ignore the degree-two requirement and expose a candidate multigraph
on the `4535` contracted nodes whose edges carry rank-five labels.  A
rainbow spanning tree exists if and only if every partition `Pi` of the
contracted nodes satisfies

\[
 \#\{\text{distinct labels on edges crossing }\Pi\}\ge |\Pi|-1. \tag{4.1}
\]

This is the graphic-matroid/partition-matroid intersection criterion.  It is
the proof-producing Rado cut for the repeat stage.  The final degree-two row
is an additional Hamilton-path condition and is not supplied by (4.1).

Second, suppose a fixed topology skeleton gives every new two-edge unused
centre all `20` ordered pairs of distinct labels from one five-label menu,
and gives every remaining singleton connector its label menu.  Duplicate
each two-edge centre into two identical demand slots.  A globally distinct
label assignment exists if and only if, for every collection `X` of
two-demand centres and `Y` of singleton connectors,

\[
                    2|X|+|Y|\le |N(X\cup Y)|.        \tag{4.2}
\]

This is ordinary capacitated Hall.  It is sufficient because the two clones
of a centre have identical neighbourhoods; any violating partial-clone set
can be enlarged to both clones without changing its neighbourhood.  The
availability of both orders then assigns the two chosen labels to the two
physical edges.  If a centre lacks the full ordered-pair menu, (4.2) is no
longer sufficient and the correlated pair gadget must be kept explicitly.

## 5. Bounded alternating-descent checkpoint

The authenticated starting residual witness has

\[
 (EU,UU)=(3065,5099),\quad17\text{ illegal wedges},\quad
 1764\text{ central-turn collision units},           \tag{5.1}
\]

and four carrier cycles.  A distinct one-worker descent preserves the fixed
direct bank, one choice per residual row, rank-eight injectivity, endpoint
capacity one, unused capacity two, boundary-turn injectivity and
`1600<=EU<=4524`.  Every move is an alternating row--rank-eight path or
cycle.  With seed `170155`, depth at most eight and an exact `900`-second
H100 cap, its best stored checkpoint has

\[
 (EU,UU)=(3252,4912),\quad0\text{ illegal wedges},\quad
 628\text{ central-turn collision units}.            \tag{5.2}
\]

The `628` units split into `571` repeated central labels and `57` central
labels colliding with the boundary bank.  The provider carrier has `15255`
vertices, `12376` edges, `2879` path components and one cyclic component.
The recomputed repeat ledger is

\[
 1656\text{ new unused vertices},\qquad
 (r_{EU},r_{UU})=(2882,1652).                         \tag{5.3}
\]

Independent replay verifies every number in (5.2)--(5.3) directly from the
provider table and the selected TSV.  The search result string
`UNKNOWN_LOCAL_MINIMUM` is only a program status label: no exhaustive
neighbourhood audit was run, so this note claims a bounded checkpoint, not a
local minimum.  It is positive evidence that wedge legality is compatible
with all marginal capacities in this fixed bank, but it leaves substantial
global rank-nine and topology debt.

## 6. Exact limitations

Everything here is conditioned on one displayed `572`-edge direct bank.
The decisive raw-edge master chooses all `13270` new edges jointly, may use a
different direct palette and does not preserve the scalar `x_1/x_4/x_5`
segmentation.  Therefore:

* the remaining `628` units and one cycle are not an obstruction to the
  joint master;
* the fixed-length Stage-B UNSAT result cannot be transferred to this
  schedule-free contraction, or conversely;
* no prefix, higher-shadow, residence, common-cap, compiler or `K17` word is
  proved.

## 7. Artifacts

Quantitative resource audit:

```text
scratch/audit_h2_k17_shift1_residual_resource_bounds_20260731.py
SHA-256 da6317efdb0e8dac645bc8443102a2d58599622f6e4e2a3f7f9a649349a7816c

scratch/h2_k17_shift1_residual_resource_bounds_20260731.audit.json
SHA-256 d712b8ac20e95e955867d9eb74a0f93f1c5985acbfb86d8de8a0e3512354df2f
canonical payload 3661227d71da70451f7eebcf76e1898bb83d473623cc72e7fa582c41f165fe82
```

Bounded descent and independent replay:

```text
scratch/search_h2_k17_shift1_wedge_h9_descent_20260731.cpp
SHA-256 2d0371fc68c961ea2b7c4dc27614fc9bba527c3b9438cd179bd8faaad0553637

scratch/h2_k17_shift1_wedge_h9_descent_20260731.best.tsv
SHA-256 b4aebce29421407d4cb111c95b55c1eed34a92423a0084c0fbbfb650085b7c3a

scratch/h2_k17_shift1_wedge_h9_descent_20260731.result.json
SHA-256 7e5a8dbe70a5bdd7912b2a0e790b463b39552510175923b591c2633c96dceb85

scratch/audit_h2_k17_shift1_wedge_h9_descent_20260731.py
SHA-256 02c18698414db18510cf6ab95c0b4aef664ff71673cf47483bbd682050c28d30

scratch/h2_k17_shift1_wedge_h9_descent_20260731.audit.json
SHA-256 e84d1eae795af73435f87d88e039a4243b1003b48fa3fa03823e8b58087c597d
canonical payload 97fbaab5faa3b28247eca6ab3afb0b360820d46af05edda017aac2a27fd73b2e
```

The direct and starting residual inputs have SHAs
`7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d`
and
`7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff`.
