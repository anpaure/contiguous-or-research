# K17 LLR470 common-parent supplier cut and support-sharp escape circuits

**Date:** 2026-08-02  
**Status:** proof-safe theorem at the explicitly stated parent, projection,
and static-chain scopes.  The warm47 `470` table is rejected as a literal
carrier of the independently materialized `b268...` private bank.  No global
selected-state, private-bank, chronology, residence, upper, compiler, or word
claim is made.

## 0. Corrected verdict

The authenticated warm47-derived calibration is

```text
warm47 protected-address-ID-safe, both-phase marginal
new-MR transfer edges                                      4,803
maximum transfer matching                                    470
final short marginal positives phase0 / phase1 / both
                                                      1,770 / 1,781 / 1,437
complete 6/9/4 supplier union projection            16,872 / 16,898
supplier deficiency                                             26
zero hard heads                                                  23
maximum-deficiency shore                              36 heads / 10 suppliers
```

The shore contains all `23` zero heads.  Deactivating those heads leaves `13`
heads with only `10` suppliers, a Hall deficit of three.  Merely making every
zero head nonisolated is insufficient unless those repairs also add enough
distinct supplier identities.  The shore splits into `18` new `LLR` and
`18` surviving `LMR` heads; its zeros split `16/7`.

These facts prove that this one warm47 table is supplier-infeasible even in
the generous union projection.  They do **not** prove that every size-`470`
transfer matching is supplier-infeasible.

Nor is the table literally full-private.  The `7,213` filter excludes
transfer endpoints whose row IDs occur as protected shorts, hosts, or
tokens, but the tickets were materialized on a different parent.  The
common-parent preflight reports

```text
warm47-candidate versus b268 parent row differences        16,034
protected unique rows                                        7,213
protected unique-row mismatches                              6,479
protected occurrence mismatches                              7,437
short / host / token mismatches                       1,564 / 2,946 / 2,927
```

Thus `4,803/470` is a warm47 footprint-safe transfer result.  The `1,437`
count is per-row marginal existence in both repriced phases; the two phase
witnesses may differ, and it is not a simultaneous ticket packing.  None of
these counts certifies that the `b268...` tickets, incidence values, or
placements survive.

## 1. Literal common-parent contract

Let `P` be a labelled parent materialization.  Write

* `T_P` for its complete table and transported owner phases;
* `B_P` for its literal private tickets, host/token placements, flags, and
  structural presentation edges;
* `J_P` for its edge-labelled LLR transfer catalogue and all transported
  `MR`/`LLR` modes; and
* `S_P` for the supplier records derived from selected row states,
  occurrences, and long transitions on that parent.

### Theorem 1.1 (common-parent contract)

An exact transfer/supplier Benders branch is semantically defined only for
one tuple

\[
                         (T_P,B_P,J_P,S_P).                 \tag{1.1}
\]

If several prospective parents are present, introduce one-hot guards `b_P`.
Every selected table mode, ticket incidence, transfer, occurrence, long arc,
and supplier record must imply the same `b_P`.  Every Hall or rank cut
separated on `P` is installed as

\[
             b_P=1\quad\Longrightarrow\quad
             \text{the cut evaluated on literal `P` activations}.          \tag{1.2}
\]

Agreement of row IDs, roots, or endpoint avoidance is not a substitute for
(1.1).  Together with exact one-hot state selection and bidirectional
within-parent AND/OR activations, the contract is fail-closed sufficient for
globally valid guarded matching cuts.  It is also necessary unless an
explicit incidence-preserving common-materialization/equivalence theorem
transports every listed object.  It is not itself a feasibility theorem.

#### Proof

Hall separation counts literal active neighbors.  Under (1.1), every edge
activation is an exact AND/OR of facts belonging to one materialization, so
its neighborhood has that meaning.  Conversely, mixing a ticket incidence
from one parent with a row mode or supplier record from another can count an
edge which exists in neither completed object.  An unguarded cut from that
mixed graph is then invalid on both branches.  Parent guards make the cut
active exactly where every one of its incidence definitions is true.
\(\square\)

For the present data, Theorem 1.1 rejects the combined warm47/`b268...`
branch before supplier optimization.  A valid continuation must regenerate
`J_P,S_P` on `b268...`, regenerate a complete private bank on the warm47
candidate, or select a prospective common materialization and rebuild every
object in (1.1) from it.

## 2. Exact parent-indexed transfer and supplier min--max

Fix one parent `P`.  Let `D_P` be its `LMR` donors, `H_P` its direct `LR`
hosts, and

\[
                         J_P\subseteq D_P\times H_P             \tag{2.1}
\]

its private-safe, mode-labelled, both-phase transfer graph.  A column
`e=(d,h)`, where

\[
 d=(\ell,m,r),\qquad h=(u,q),qquad \ell\subsetneq u,
\]

performs

\[
       (\ell,m,r)+(u,q)\longmapsto(m,r)+(\ell,u,q).              \tag{2.2}
\]

The exact size-`k` transfer master is

\[
 \sum_{e\ni d}z_e\le1,qquad
 \sum_{e\ni h}z_e\le1,qquad
 \sum_ez_e=k.                                                   \tag{2.3}
\]

The final `LLR` state at `h` is edge-labelled because it contains the donor
bottom `ell`; a host-only state bit is insufficient.

Let `A_P` be the universe of mode-labelled hard-head occurrences and `U_P`
the physical supplier identities.  For an integral master assignment `xi`,
let

\[
 d_a(\xi)=\mathbf1[a\text{ is an active hard head}],            \tag{2.4}
\]

and let `I_ua(xi)` be the exact activation of supplier identity `u` at head
occurrence `a`.  It is the OR of complete signed **common-parent** DNFs,
including the selected transfer mode, actual flags/history, ticket or
long-arc parent, and placements.  For `X subset A_P`, put

\[
                   n_u^X(\xi)=\bigvee_{a\in X}I_{ua}(\xi).       \tag{2.5}
\]

The OR must be bidirectionally encoded: a stale possible-but-unselected
record is not a neighbor.  Let `Xi_P` denote the complete integral
common-parent master: it contains exact one-hot row/head modes, transfer
matching, protected tickets, presentation/placement literals, flags,
selected occurrences and long arcs, and all resource constraints.

### Theorem 2.1 (weighted transfer / supplier Hall--Benders theorem)

Put `K(xi)=sum_a d_a(xi)`.  For every fixed integral assignment,

\[
 \boxed{
 \nu(G_\xi)=
 \min_{X\subseteq A_P}
 \left(K(\xi)-\sum_{a\in X}d_a(\xi)+\sum_{u\in U_P}n_u^X(\xi)\right),}
                                                                  \tag{2.6}
\]

and

\[
 \boxed{
 \delta(G_\xi)=
 \max_{X\subseteq A_P}
 \left(\sum_{a\in X}d_a(\xi)-\sum_{u\in U_P}n_u^X(\xi)\right).}
                                                                  \tag{2.7}
\]

Consequently the exact weighted full-rank problem is

\[
 \max_{\xi\in\Xi_P}\left\{\sum_e w_ez_e(\xi):
       z(\xi)\text{ satisfies (2.3)},\quad
       \sum_{a\in X}d_a(\xi)\le\sum_u n_u^X(\xi)
       \quad( X\subseteq A_P)\right\}.                           \tag{2.8}
\]

Equivalently, maximize a rank variable `Theta` with the lazy optimality cuts

\[
\boxed{
 \Theta\le K(\xi)-\sum_{a\in X}d_a(\xi)+\sum_u n_u^X(\xi).}     \tag{2.9}
\]

Here `0 <= Theta <= K(xi)`, and `Theta` equals supplier rank only when it is
maximized or given lexicographic priority over secondary objectives.

For fixed `xi`, one supplier maximum matching/min-cut separates the most
violated member of (2.9).  In the network `s -> active heads -> supplier
identities -> t`, head and supplier arcs have capacity one and compatibility
arcs have infinite capacity.  A minimum cut returns `X`.

#### Proof

The deficiency form of Hall's theorem gives

\[
 K-\nu(G_\xi)=
 \max_X\left(|X\cap A(\xi)|-|N_\xi(X)|\right).
\]

Equations (2.4)--(2.5) are exactly the two cardinalities on the right.
Rearranging proves (2.6)--(2.9), and the standard matching network gives the
separation oracle.  \(\square\)

This is an exact matching/min-cut theorem for **fixed** `xi` and an exact
branch--Benders formulation for optimizing `xi`.  It is not one weighted
matching in the transfer graph: the neighborhood OR has redundancy, and a
supplier edge may be activated only by two compatible row modes.

## 3. The exact `36 -> 10` obstruction cut

Let `Q` be the current set of `36` mode-labelled projected hard heads and let

\[
                         B=N_0(Q),\qquad |B|=10.                 \tag{3.1}
\]

At the warm47 calibration all `36` head occurrences are active, so its cut
value is `36-10=26`.  The exact activity-aware cut is

\[
             \boxed{\sum_{a\in Q}d_a(\xi)\le
                    \sum_u n_u^Q(\xi).}                         \tag{3.2}
\]

For any assignment on the **same parent and the same state-expanded
catalogue**, define the repair gain

\[
\begin{aligned}
 \Gamma_Q(\xi)
   &=\sum_{a\in Q}(1-d_a(\xi))
     +|N_\xi(Q)\setminus B|-|B\setminus N_\xi(Q)|.              \tag{3.3}
\end{aligned}
\]

Then the signed Hall excess of this inherited shore is exactly

\[
 \boxed{
 \sum_{a\in Q}d_a(\xi)-|N_\xi(Q)|=26-\Gamma_Q(\xi).}            \tag{3.4}
\]

The actual residual deficiency contributed by this shore is
`[26-Gamma_Q(xi)]_+`.  Hence every full supplier solution must satisfy

\[
                         \Gamma_Q(\xi)\ge26.                    \tag{3.5}
\]

#### Proof

Expand the right side of (3.4):

\[
 26-\Gamma_Q
 =(36-|B|)-(36-\sum_Qd_a)-(|N_\xi(Q)|-|B|)
 =\sum_Qd_a-|N_\xi(Q)|.
\]

\(\square\)

Formula (3.3) is the precise meaning of “hit the 26 missing supplier units.”
A repair can deactivate or change a deficient head occurrence, add a new
distinct supplier identity, or lose an old one.  Counting positive transfer
edges or zero heads does not compute (3.3).  Even (3.5) repairs only the
inherited shore; all other Hall cuts in (2.8) remain necessary.

The reported `16,872` rank is a union over possible `6/9/4` flag pairs.  Any
literal common-state graph is a subgraph of that union projection.  Thus the
current table's literal supplier rank is at most `16,872`; projection
deficiency `26` is already a valid no-go for that table, not a positive
common-state certificate.

## 4. Alternating transfer circuits and a valid radius cut

Continue on one fixed parent and freeze every nontransfer state used by the
deterministic complete-row-pair supplier projection.  Let `F_0` be the saved
size-`470` transfer matching and `F` another size-`470` matching in `J_P`.

### Lemma 4.1 (transfer-circuit decomposition)

`F triangle F_0` is a vertex-disjoint union of alternating even cycles and
alternating paths.  Flipping any collection of its components preserves
row-disjointness; the total cardinality is preserved when the chosen
components contain equally many old and new edges.

The smallest cardinality-preserving open exchange is a two-edge alternating
path on three physical rows.  The smallest closed transfer circuit is a
four-edge `C4`.

#### Proof

Every vertex has degree at most two in the union of two matchings, with edges
alternating by membership.  Its components are therefore alternating paths,
even cycles, and common edges.  Flipping interchanges the two matchings on a
component.  The size statements follow by inspection.  \(\square\)

### Lemma 4.2 (three-Lipschitz projection rank)

For the deterministic row-pair supplier projection,

\[
                  |\nu(G_F)-\nu(G_{F_0})|
                     \le 3|F\triangle F_0|.                     \tag{4.1}
\]

Indeed, toggling one transfer changes two supplier-source menus and replaces
at most one hard-head mode.  The hard-head census remains `16,898` throughout
the transfer face: the identical bottom `ell_d` moves from the donor LMR row
to the host LLR row, so the predicate `rank(ell_d)>1` is unchanged.  Changing
the adjacency of one left vertex or replacing one right vertex changes
bipartite matching rank by at most one.  Remove old transfers first and then
add new transfers; all intermediate transfer sets remain row-disjoint.  The
triangle inequality proves (4.1).

Since the current projection needs a rank gain of `26`, every supplier-
perfect size-`470` matching in this deterministic face must obey

\[
             |F\triangle F_0|\ge\left\lceil{26\over3}\right\rceil.
\]

Equal-cardinality matchings have even symmetric difference, so the valid
integer radius-10 cut is

\[
 \boxed{
 \sum_{e\in F_0}(1-z_e)+\sum_{e\notin F_0}z_e\ge10.}            \tag{4.2}
\]

Thus at least five saved transfers must be removed and five new transfers
added.  Bound (4.2) is a lower-bound Benders cut, not an existence theorem.
It is valid only under the common-parent and fixed-nontransfer-mode hypotheses
of this section.  If tickets, flags, long arcs, or the parent can change
supplier incidences independently of `z`, (4.2) is not valid.

## 5. No general bounded-support repair; the exact Rado special case

### Theorem 5.1 (no support bound depending only on deficiency)

In the general activated-edge model, no function of supplier deficiency
alone bounds the number of private-safe row-disjoint transfer activations
needed for repair.

#### Proof

For arbitrary `k`, take supplier identities `s_0,...,s_(k-1)` and hard heads
`h_0,...,h_(k-1)`.  The baseline has the edges

\[
                         s_i h_i\qquad(1\le i<k),                \tag{5.1}
\]

so its deficiency is one.  For `1<=i<k`, column `c_i` activates
`s_i h_(i-1)`, and `c_k` activates `s_0 h_(k-1)`.  Give the columns disjoint
private transfer row pairs.  Realize each mandatory neutral head swap by old
and new right states having identical adjacency to a unique always-available
dummy supplier, so it does not alter the displayed deficiency.  All `k` columns
give the shifted perfect matching.  If any `c_i` is absent, following the
forced chain from `h_0` leaves one head unmatched.  Thus all `k` activations
are necessary although the original deficiency is one.  \(\square\)

Therefore no claim such as “deficiency 26 has a repair on at most 26 (or
`O(26)`) transfers” is proof-safe for the actual LLR activation system.

There is a sharp positive theorem under stronger hypotheses.

### Theorem 5.2 (fixed-transversal `d`-exchange/Rado lemma)

Assume one common parent, invariant supplier menus, and transfers which only
replace hard-head elements of one fixed transversal matroid `M_sup`.  Let
`H` have size `n` and rank `n-d`.  Fix a basis `I subset H`, put
`D=H minus I`, and for each `x in D` let `A_x` be the private-safe new-head
elements obtainable by deleting `x`.  Candidate element identity must
already include its unique physical host.

A repair which retains this fixed basis `I` and replaces precisely
`D=H minus I` by one candidate from each `A_x` exists if and only if

\[
 \boxed{
 r_{M_{sup}/I}\!\left(\bigcup_{x\in X}A_x\right)\ge|X|
 \qquad(X\subseteq D).}                                      \tag{5.2}
\]

#### Proof

A repaired basis of this declared form consists of `I` plus one candidate for every deleted
element in `D`, and the candidates must be independent after contracting
`I`.  Rado's independent-transversal theorem gives exactly (5.2).  A global
`d`-replacement statement is existential over the choice of retained basis
`I`.  Necessity
of `d` replacements follows because rank can increase by at most one per new
matroid element, and examples with `d` independent private candidates attain
the bound.  \(\square\)

The weighted version is weighted independent transversal/matroid
intersection.  The candidate ground-element identity in the theorem includes
its unique physical host and is not donor-labelled.  If several donor states
of one host are distinct elements, an additional host partition constraint
is required and Rado alone no longer suffices.  Actual LLR transfers do not
satisfy this theorem's premises:
they change two supplier menus (`4 -> 9` and `9 -> 4`), their new head is
donor-labelled, and distinct choices can activate a supplier edge only
jointly.  The warm47 deficit `26` therefore cannot be promoted to a
26-transfer Rado claim.

## 6. Why the joint master is not a matroid or one TU flow

Row-disjoint transfer sets are graph matchings, not a matroid.  On a
three-edge path, the two outer edges form a matching of size two, while the
middle edge alone cannot be augmented by either outer edge.

Supplier gain over transfer bundles need not be submodular: two disjoint row
state changes can each have gain zero but jointly activate one compatible
supplier/head edge.  The natural activation matrix already contains

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&-1\\
 0&1&-1
 \end{pmatrix},
 \qquad |\det|=2.                                             \tag{6.1}
\]

More strongly, the arbitrary mode-labelled occurrence-column problem
contains rainbow bipartite matching and hence perfect three-dimensional
matching.  Given `|D|=|H|=|C|=n` and allowed triples
`T subset D times H times C`, create one distinct parallel edge-labelled
transfer column on row pair `(d,h)` for each `(d,h,c)`, and give it a distinct
private supplier identity adjacent only to color-head `c`.  Selecting `n`
row-disjoint transfers and saturating all color heads is exactly perfect 3DM.
This is a hardness theorem for arbitrary occurrence catalogues, not for pure
structural LLR containment.

Lemma 4.1 and the structural circuits below use the simple row-pair graph.
In an occurrence multigraph, two parallel modes can instead form a
two-column alternating cycle; that does not contradict the structural `C4`
statement.

Thus only the **fixed-master** supplier child is ordinary matching/min-cut.
Joint transfer/state/supplier selection is an occurrence hypermatching or an
exact branch--Benders problem.  This is consistent with the earlier
three-index warning and makes no false matroid claim.

## 7. Support-sharp structural escape lemmas

The current data do not prove that the entire size-`470` transfer face is
impossible.  If it is later closed by parent-guarded Hall cuts, the following
are the first exact structural extensions.

### Lemma 7.1 (downward cardinality escape)

Undoing one transfer changes exactly its donor and host rows and moves from
`a=470` to `a=469`.  Within the declared inverse-transfer grammar and exact
target-partition tables, this is the smallest downward escape.  Its four type
counts change by

\[
                         (-1,+1,+1,-1)                         \tag{7.1}
\]

in `(LLR,LMR,LR,MR)` order.  Every resulting chain is still a strict chain
of length at most three and is marginally legal in the depth-three derivative
grammar.  Common-parent tickets, sockets, and supplier incidences must be
regenerated.

### Lemma 7.2 (two-long-row lower-prefix `C4`)

Let two long rows be

\[
                (\ell_1,u_1,r_1),\qquad(\ell_2,u_2,r_2),        \tag{7.2}
\]

where each `u_i` may be a rank-seven `LMR` middle or a low `LLR` middle.  The
support-two exchange

\[
 (\ell_1,u_1,r_1)+(\ell_2,u_2,r_2)
 \longmapsto
 (\ell_2,u_1,r_1)+(\ell_1,u_2,r_2)                             \tag{7.3}
\]

is a valid target/root/owner table exchange if and only if

\[
                         \ell_2\subsetneq u_1,qquad
                         \ell_1\subsetneq u_2.                 \tag{7.4}
\]

It preserves every target, root, owner, row length, and the individual
`LLR/LMR` middle types.  If `rank(ell_1),rank(ell_2)>1`, it changes exactly
two hard-head requirements; without that hypothesis it changes two long-row
payloads but zero, one, or two hard-head occurrences.
No one-row exchange can preserve the target partition, so support two is
sharp whenever (7.4) holds.

#### Proof

All unchanged containments are inherited and (7.4) is exactly the pair of
new containments.  The two bottom targets are transposed, so the target
multiset is unchanged; roots, owners, and middles remain on their rows.  A
one-row change would duplicate one bottom and omit the other.  \(\square\)

### Lemma 7.3 (support-two receiver-basis/root-type `C4`)

Let `P_M` be an `LMR` or `MR` prefix ending in a rank-seven target `m`, and
let `P_L` be an `LLR` or `LR` prefix ending in a low target `u`.  Suppose the
current root assignment is

\[
                         (P_M,r)+(P_L,q).                       \tag{7.5}
\]

It can be changed to

\[
                         (P_L,r)+(P_M,q)                        \tag{7.6}
\]

on exactly two root rows if and only if

\[
                              u\subsetneq r,qquad m\subsetneq q.             \tag{7.7}
\]

This is the alternating `C4` in the full prefix--root matching.  It changes
which root belongs to the rank-seven receiver basis, preserves every target,
root, owner, and global `LLR/LMR/LR/MR` count, and has structurally minimum
support: a one-row receiver change cannot preserve a perfect root assignment.

If no cross-compatible pair (7.7) exists, the minimum support among
receiver-basis changes in this fixed full prefix--root perfect-matching
presentation is the shortest common-parent-admissible alternating cycle.
In the contracted rank-seven transversal-matroid view, the same
receiver-basis change appears as a fundamental alternating path to an
outside root; its low-side completion closes that path in the full
presentation.  Other simultaneous prefix recouplings are outside this
minimum statement.  A closed reassignment entirely inside the fixed
rank-seven/root bank has no `C4`: two distinct rank-seven sets have at most
one common rank-eight superset.  Hence its first possible closed circuit is
`C6`.  Changing the receiver basis may use the shorter fundamental path, so
root-bank change does not generally require `C6`.

Lemmas 7.2--7.3 are static and marginal.  Their use on the current supplier
shore requires a common-parent occurrence catalogue, protected presentation
extension, socket replay, and supplier cut separation.  No such improving
circuit has been authenticated for the current `36 -> 10` shore.

## 8. What is proved and what remains

Frozen here:

1. the literal common-parent contract;
2. the exact weighted transfer/supplier Hall--Benders min--max;
3. the activity-aware `36 -> 10` cut and repair identity;
4. the same-parent projection Hamming-radius cut `>=10`;
5. nonexistence of a general support bound depending only on deficiency;
6. the conditional fixed-transversal Rado theorem;
7. the nonmatroid/3DM boundary; and
8. the support-two lower-prefix and receiver-basis extension lemmas.

Not proved:

* that any literal `b268...` transfer face has `4,803` edges or rank `470`;
* that every warm47 size-`470` transfer matching is supplier-deficient;
* that the `1,437` marginal short positives admit one simultaneous ticket
  selection;
* that a current-shore support-two escape exists; or
* any selected-state, global chronology, residence, upper, compiler, or word
  completion.

The proof-safe next row is to regenerate `(T_P,B_P,J_P,S_P)` under one parent
and run Theorem 2.1.  Only a parent-guarded exhaustive Hall closure can turn
the present calibration into a face no-go.  If that closure occurs, search
the support-two circuits of Lemmas 7.2--7.3, followed by the shortest
parent-valid alternating circuit or completed receiver-basis exchange
path—not an unguarded additive supplier score.

## 9. Frozen input hashes

```text
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
  scratch/ad_k17_round047_relay_lineage_independent_20260802/seed4015.relay_cegar.round047.table.tsv
34838ee1e8d2149feaa5254bcd51fb02f4659c6a35bb77b4938bf2d73f9e674e
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.table.tsv
e3e14e5831553465148ca87a81aa86bc680fe0ea340591bcf1384c717a67f650
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate_socket_matching.audit.json
66f62610f685418e61f46e17bc9b9b19019500f2a9e5ee3ac5eb75a6301b9911
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate_socket_matching.selected.tsv
c83bcc44195bf5c3e9032ba19252025e12a50135af3fc2cdff539051eb99daff
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.phase0.tsv
ec7b77163c71d7527ae2bdb37f714815ee1f972519d42fcf6717a32c226c395b
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.phase1.tsv
92b8c0062aa68516a0666813dc4fb76541eb0f375524c8c68751cd0346d06da2
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.independent.audit.json
b52184e189fac458bcadc1dd2761dc256654570cdc57c671ce1b4aa2d83508eb
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.projection.audit.json
f284d8246b67d1d823408753dde8fea61729283a87bdf77214d129554bc9afcb
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.hall.tsv
639166c51af3f37d540ed145525133a3b721c85ed742443945d9fac828dd561c
  scratch/q1_k17_llr_socket_matching_20260802/llr_fullprivate470.hall_heads_classified.tsv
479fd8333c07952c65fcaf15db488cf300c191335e30e64c73184f38f00d5761
  scratch/k_llr470_selector_20260802/fullprivate470_bankbound.preflight.audit.json
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv
```
