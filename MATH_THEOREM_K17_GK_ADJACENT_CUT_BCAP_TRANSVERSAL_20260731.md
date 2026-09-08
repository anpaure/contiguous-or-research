# The adjacent-cut GK supported-provider b-capacity transversal

Date: 2026-07-31  
Status: exact positive finite theorem for the first correlated physical
provider gate at cyclic cuts `s=1,16`.  This is not an ear packing or a
`K17` word.

## 0. Result

Let `F_1` be the rank-seven Greene--Kleitman forest obtained from cyclic cut
starts `(0,1)`, and let `R_1` be its frozen greatest-supported relation from
missing rank-six colours to fresh rank-eight unions.  If `(D,Q) in R_1`, the
pair determines one Johnson edge, with endpoints

\[
       D+a,\quad D+b,\qquad Q\setminus D=\{a,b\}.       \tag{0.1}
\]

Give each vertex of `F_1` capacity one and each unused rank-seven vertex
capacity two.  There is an explicit set of `8736` supported provider edges
which

* contains exactly one edge for every missing rank-six colour;
* has `8736` pairwise-distinct rank-eight unions;
* uses every base vertex at most once; and
* uses every unused vertex at most twice.

The exact selected type histogram is

\[
            (EE,EU,UU)=(572,3065,5099).                \tag{0.2}
\]

The coordinate rotation `i -> i-1 mod 17`, followed by swapping the two
undirected GK rails, transports the same certificate to cuts `(0,16)`.

## 1. Authenticated adjacent-cut fixture

The all-shift theorem proves that the adjacent forests are matchings:

\[
 |E(F_1)|=3640,qquad |V(F_1)|=7280,qquad c(F_1)=3640. \tag{1.1}
\]

There are `12168` unused rank-seven vertices and `8736` missing rank-six
colours.  Since every component has two vertices, width two is the complete
nontrivial internal-width range.  Literal replay gives `3640` width-two
occurrences, each of rank eight, with `3640` distinct unions.  The same
statement holds for `F_16` under rotation.

The independently materialized supported-edge/wedge fixed point has

\[
454930\text{ edges},\qquad 20772564\text{ wedges}.    \tag{1.2}
\]

Its projected provider relation has

\[
 |L|=8736,quad |R|=13817,quad |I|=272992,            \tag{1.3}
\]

ordinary matching rank `8736`, and no zero row.  The complete provider type
census is

\[
       EE^{20655}EU^{66574}UU^{185763}.                \tag{1.4}
\]

These upstream claims are replayed again by the independent certificate
auditor; the positive capacity result does not infer them from scalar counts.

## 2. Exact b-capacity system

For each `(D,Q) in R_1`, introduce `x_{D,Q} in {0,1}` and reconstruct its
two endpoints `u(D,Q),v(D,Q)` by (0.1).  Put

\[
 b(w)=\begin{cases}
 1,&w\in V(F_1),\\
 2,&w\notin V(F_1).
 \end{cases}                                           \tag{2.1}
\]

The first physical provider gate is exactly

\[
\begin{aligned}
 \sum_{Q:(D,Q)\in R_1}x_{D,Q}&=1 &&(D\in L),\\
 \sum_{D:(D,Q)\in R_1}x_{D,Q}&\le1 &&(Q\in R),\\
 \sum_{(D,Q):w\in\{u(D,Q),v(D,Q)\}}x_{D,Q}&\le b(w)
                                                    &&(w\in { [17]\choose7}).
\end{aligned}                                         \tag{2.2}
\]

The equivalence is literal: the first row covers every missing lower colour,
the second makes the new rank-eight colours injective, and the third is
precisely the rank-seven incidence capacity.  Conversely, any physical
provider transversal gives the incidence vector in (2.2).  This is a
four-resource column system, not an ordinary bipartite Hall problem.

The frozen uncapacitated matching is not a solution: it has `1356` excess
endpoint units.  Thus the positive theorem requires correlated reselection.

## 3. Sufficient forced-core face

Exactly `572` provider rows have no `EU` or `UU` option.  An authenticated
direct core selects one `EE` provider on each of these rows with

\[
572\text{ distinct }Q,quad
1144\text{ distinct base endpoints},quad
1144\text{ distinct boundary rank-nine turns}.        \tag{3.1}
\]

After contracting the base dimers, these `572` edges are vertex-disjoint in
the component quotient, hence acyclic, and leave `3068` quotient components.
The four-column and six-column frozen versions encode the same literal edge
family; the latter additionally records both boundary turns.

Fix this core and forbid `EE` on every other provider row.  Before the
optional boundary-turn filter, the residual face has

\[
8164\text{ rows},quad11947\text{ rank-eight resources},quad
249477\text{ incidences},                              \tag{3.2}
\]

and ordinary rank-eight matching rank `8164`.  This is a **sufficient face**
of (2.2), not a completeness reduction for arbitrary b-capacity solutions.

For the stronger solve, also delete a residual `EU` option when its forced
boundary rank-nine turn collides with the direct core.  The resulting exact
model has

\[
 242771\text{ binary columns}=
 57008\ (EU)+185763\ (UU).                             \tag{3.3}
\]

It retains all `8164` rows.  A one-run H100 CP-SAT solve returned a feasible
(reported `OPTIMAL` for the satisfaction model) selection in
`53.113112142` seconds.  The selected residual histogram is

\[
                    EU^{3065}UU^{5099}.                \tag{3.4}
\]

Solver status is provenance only.  The theorem rests on the stored integral
certificate and the independent literal replays below.

## 4. Literal certificate theorem

Combine the `572` direct rows with the `8164` residual rows and rewrite each
record as `(D,Q,u,v)`.  Direct replay gives

\[
\begin{array}{c|cc}
 &0&1\\\hline
\text{base-vertex load}&3071&4209
\end{array}                                            \tag{4.1}
\]

and

\[
\begin{array}{c|ccc}
 &0&1&2\\\hline
\text{unused-vertex load}&4416&2241&5511.
\end{array}                                            \tag{4.2}
\]

Hence the maximum loads are exactly one and two.  The certificate has
`8736` distinct lower colours and `8736` distinct rank-eight unions, and
every selected pair belongs to the complete frozen menu.  This proves
feasibility of (2.2).

The construction additionally has `4209` distinct **forced boundary**
rank-nine turns: two for every selected `EE` edge and one for every selected
`EU` edge.  This does not assert compatibility or injectivity of the central
turns created when selected edges are paired at unused vertices.

An independent diagnostic makes that exclusion literal.  Exactly `5511`
unused vertices currently have selected degree two, so their provider--
provider pairing is forced.  Of these, `5494` are locally legal wedges and
`17` are locally illegal.  Among the legal central turns there are `1503`
repetition units and `261` collisions with selected boundary turns, for
`1764` central rank-nine collision units.  Thus the certificate is not itself
a wedge packing: its exact current turn-defect potential is

\[
                    17+1503+261=1781.                 \tag{4.3}
\]

These are diagnostics of this witness, not an obstruction to the b-capacity
system (2.2), which the witness already satisfies.

The fail-closed verifier independently reconstructs `F_1`, checks all
internal widths, authenticates the complete provider relation, reconstructs
every selected Johnson edge, and replays every row, union, and vertex load.
It then rotates the actual selected family to `F_16` and repeats the union
and capacity checks.  Its exact verdict is

```text
PASS_EXACT_ADJACENT_B_CAPACITY_TRANSVERSAL
s=1:  rank8 distinct 8736, base max load 1, unused max load 2
s=16: rank8 distinct 8736, base max load 1, unused max load 2
```

## 5. Exact next gate

The certificate selects only the `8736` first-provider edges among the
`13270` new tail edges.  The remaining `4534` repeat-payload edges have not
been chosen.  On this particular certificate, completing the base incidence
ledger with two global terminals requires

\[
               3069\ (EU)+1465\ (UU)=4534             \tag{5.1}
\]

additional edges.  Currently `7752=2241+5511` unused vertices are touched;
an exact `9631`-owner tail must additionally activate `1879` of the `4416`
zero-load unused vertices.  The residual unused incidence demand is

\[
                2241+2\cdot1879=5999
                =3069+2\cdot1465.                     \tag{5.2}
\]

Thus the next literal gate is to choose and pair the filler edges so that
all used unused vertices have degree two, central wedges and rank-nine turns
are compatible, and the component quotient becomes one path.  Nothing in
the present theorem proves that gate.  In particular, the `17` saturated
illegal centres cannot simply receive filler edges; at least their provider
choices must be reselected.  The `1764` turn-collision units show that fixing
only those `17` local rows is not by itself a certified completion.

## 6. Scope exclusions

This theorem proves only the adjacent-cut supported-provider b-capacity
transversal, plus injectivity of its already-forced boundary turns.  It does
not prove

* compatible pairing of selected provider edges at unused vertices;
* central rank-nine injectivity;
* the `4534` repeat-payload filler edges;
* a component-spanning ear path;
* prefix or higher-upper coverage;
* residence, a common compiler cap, or a `K17` word.

## 7. Frozen artifacts

```text
complete provider relation
scratch/k17_gk_cyclic_cut_s1_supported_provider_matching_20260731.tsv
SHA-256 6b2d9802d028cca79064278a65020d8ec28e3cc1b04d59c518d29b66b1a68e97

direct 572-row core with boundary turns
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d

residual solver
scratch/solve_independent_k17_gk_shift1_residual_cap_20260731.py
SHA-256 5f73de6ceaccf7d3165ccb51112bfe57e273a34a30d7b9508f25dfce65dacfce

residual 8164-row witness
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
SHA-256 7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff

residual solver audit
scratch/independent_k17_gk_shift1_residual_cap_solver_20260731.audit.json
SHA-256 7e98c74b8606171d10f2d712b2d107c59e5859e83b52474327dc1a793076e095

combined canonical certificate
scratch/k17_gk_adjacent_cut_bcap_certificate_20260731.tsv
SHA-256 68fb5b172ac90c89aa7f590da2f24e9e118aea0a14ef4793e77409b8b79d30aa

combination replay
scratch/audit_k17_gk_adjacent_cut_bcap_combined_20260731.py
SHA-256 4f79ebc63eec0cfa40165d47729262364b27e422196275da746f53845a23fbbf

scratch/k17_gk_adjacent_cut_bcap_combined_20260731.audit.json
SHA-256 cfd173b2c0b8ea63c80a736d5bd63ad0e57236028956d837099fd9b4a2110fe3
canonical payload 58f9f3c135d76180dff347f39291175dd1797ee147d239eba4047ecb9451e3c1

independent all-width/provider/symmetry/certificate replay
scratch/audit_k17_gk_adjacent_cut_bcap_certificate_20260731.py
SHA-256 314273f620259295f4dc20c3ba97195479b732cb0a7e59add475b0ba00411d22

scratch/k17_gk_adjacent_cut_bcap_certificate_20260731.independent.audit.json
SHA-256 5e44a83c0f8b80f4cd6c545e4cca2dda6fc4e579f458a7e204e2d460d567d276
canonical payload 43e39a99c6ee34f5ea52dfa4d7f6a25ad39b8b8f655f46e0661e2a89e6099f6c

second independent split/core/certificate/s16 verifier
scratch/verify_k17_gk_adjacent_cut_bcap_candidate_20260731.py
SHA-256 70cc3f3d0644bbf7ad66fe2dcd3ae1172e8e48c85ecc8e8ce9a6b916fb260842

scratch/k17_gk_adjacent_cut_bcap_candidate_independent_20260731.audit.json
SHA-256 f1a7bc5fdeeb66eac8615510068ea762c8d0fbe77aa51e8bcbdbd47ec9ff9a88
canonical payload 6090e65dc6adf8c6a984542ce2efd3e9ffb4bdc77a6a52f69c09ad304e8386d8

independent residual wedge/turn diagnostic
scratch/audit_independent_k17_gk_shift1_residual_cap_20260731.py
SHA-256 f2ddfdd0d9017189a59e0c5e1c3accf39ce5a6a69165539731a15d5ce1afad47

scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json
SHA-256 6b9f5389e59d086cadda4be9e7bd146991c050fa1231513097bed7f30b6157cc
canonical payload 952b19f4df8b8a920107448a9b66bc4e1c4d2ee6b5760538933222d23c538ff5
```
