# K17 b268 LLR437: parent-valid Hall circuits and root-bank escape

> **Historical incumbent notice.**  The `437/def97` calibration and every
> theorem scoped to that centre remain valid, but it is no longer the active
> incumbent.  The authoritative successor is the `438/def95` table frozen in
> `MATH_THEOREM_K17_B268_LLR438_DEF95_NEXT_EXCHANGE_BENDERS_20260802.md`.

**Date:** 2026-08-02  
**Status:** proof-safe theorem at the authoritative `b268...` static-table,
phasewise marginal-socket, and complete `6/9/4` supplier-projection scopes.
There is no warm47 datum in the theorem.  The result preserves the literal
states of the `7,213` protected rows and uses only transfer modes repriced on
the same parent.  It does not select one common occurrence/state witness and
does not prove residual outer extension, chronology, residence, upper,
compiler, or a K17 word.

## 0. Authoritative binding and corrected verdict

The one parent in this note is

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    private_h_outer_materialized.tsv
```

Its selected private tickets have SHA
`d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1`.
The protected row set `P` has cardinality `7,213`; it is the union, not the
sum, of `1,748` ticket-short rows, `3,496` distinct predecessor/successor
hosts, and `3,495` token rows.

The protected transfer catalogue has `93,234` structural edges.  Native
phase zero and transported phase one price respectively `23,342` and
`25,173` of them positive.  Their intersection

\[
             J^+\subseteq D\times H
\]

has `11,893` edges and matching number `464`.  Every endpoint and every
declared long witness of an edge of `J+` avoids `P`.  The two price tables,
the table, the tickets, and the supplier projection all have the same
literal `b268...` parent.

Write `M` for the supplied size-`464` matching and `F_0` for the final
size-`437` matching.  The audited relation is

\[
                    F_0\subset M,\qquad |M-F_0|=27.          \tag{0.1}
\]

The alleged new-edge file is empty, so (0.1) is literal rather than an
inference from counts.  The calibrated tables are

| transfer set | `(LLR,LMR,LR,MR)` | `p0/p1/both/either` | supplier rank / deficiency | zeros; Hall shore |
|---|---:|---:|---:|---:|
| `empty` | `0,16915,4862,2533` | `2687/1891/1422/3156` | `16796/102` | `94; 109/7` |
| `M` | `464,16451,4398,2997` | `3119/2274/1864/3529` | `16767/131` | `105; 166/35` |
| `F_0` | `437,16478,4425,2970` | `3097/2252/1838/3511` | `16801/97` | `82; 111/14` |

Thus `F_0` strictly Pareto-dominates the empty `b268` transfer table in all
four displayed marginal-socket counts and in supplier rank, but the rank
gain is only five: deficiency `102 -> 97`.  It is still supplier-infeasible.
The larger matching `M` is much worse, with deficiency `131`.  This
nonmonotonicity is load-bearing below.

Phase one is a root-aligned transported phase on this parent.  Its
carrier-opening interpretation is not proved.  “Both positive” means that
each selected edge has a marginal relaxed-nine five-cell witness in each
separately priced phase.  The two witnesses may differ and may compete for
endpoint histories; it is not a simultaneous common-state packing.

## 1. The exact parent-valid transfer face

A transfer edge joins a donor `d=(ell,m,r)` to a host `h=(u,q)` and performs

\[
 (\ell,m,r)+(u,q)\longmapsto(m,r)+(\ell,u,q),
 \qquad \ell\subsetneq u.                                  \tag{1.1}
\]

For `F subseteq J+`, the row-disjointness equations are

\[
 \sum_{e\ni d}z_e\le1\quad(d\in D),\qquad
 \sum_{e\ni h}z_e\le1\quad(h\in H).                       \tag{1.2}
\]

Every integral solution of (1.2) is a static `b268` table which preserves
all named targets, roots, owners, the global row count, and every literal
row state in `P`.  Its type ledger is

\[
 (LLR,LMR,LR,MR)
   =(|F|,16915-|F|,4862-|F|,2533+|F|).                      \tag{1.3}
\]

Every selected edge remains in the supplied two-phase **marginal-positive**
catalogue.  This is the strongest socket assertion inherited merely from
membership in `J+`.

Let `G_F` be the deterministic complete `6/9/4` union-supplier projection
of the materialized table.  Its hard-head census is

\[
                              K=16898.                       \tag{1.4}
\]

The head occurrence displaced by (1.1) is mode-labelled; the source menus
of its two physical rows change `4 -> 9` and `9 -> 4`.  Collapsing those
states to an unlabelled host bit is unsound.

## 2. Exact Hall min--max and the inherited `111/14` cut

Let `A` be one fixed universe of possible mode-labelled head occurrences
and `U` the physical supplier identities.  For an integral parent-valid
assignment `xi`, let

\[
 d_a(\xi)=\mathbf 1[a\text{ is active}],\qquad
 n_u^X(\xi)=\mathbf 1[u\text{ has an active supplier edge into }X]. \tag{2.1}
\]

The second variable is the exact bidirectional OR of complete `b268`
incidence DNFs.  In a literal state-expanded master those DNFs must include
the one selected endpoint/history state; a possible but unselected record
is not a neighbour.

### Theorem 2.1 (parent-valid supplier min--max)

For every fixed integral assignment,

\[
 \boxed{
 \nu(G_\xi)=K-
   \max_{X\subseteq A}
   \left(\sum_{a\in X}d_a(\xi)-\sum_{u\in U}n_u^X(\xi)\right).} \tag{2.2}
\]

Consequently supplier perfection is equivalent to all activated Hall rows

\[
 \boxed{
       \sum_{a\in X}d_a(\xi)\le\sum_un_u^X(\xi)
       \qquad(X\subseteq A).}                              \tag{2.3}
\]

For fixed `xi`, one supplier maximum matching/minimum cut separates (2.3).
Thus (1.2), exact parent-state activations, and lazy rows (2.3) form a
proof-safe branch--Benders formulation.  It is not one weighted transfer
matching.

#### Proof

Equation (2.2) is the deficiency form of Hall's theorem, with the two
cardinalities written using (2.1).  The usual unit-capacity network
`source -> active heads -> suppliers -> sink` supplies the separator.
\(\square\)

For `F_0`, fix the returned maximum-deficiency shore `Q`.  Put

\[
       |Q|=111,\qquad B=N_{F_0}(Q),\qquad |B|=14.            \tag{2.4}
\]

All `82` zero heads lie in `Q`; after deleting them, the remaining `29`
heads still see only `14` suppliers.  Isolated-head repair alone therefore
leaves deficit at least `15` unless it also changes distinct supplier
identities.

Define the exact signed repair of this inherited shore by

\[
\begin{split}
 \Gamma_Q(\xi)
   ={}&\sum_{a\in Q}(1-d_a(\xi))\\
     &+|N_\xi(Q)-B|-|B-N_\xi(Q)|.                           \tag{2.5}
\end{split}
\]

Then

\[
 \boxed{
 \sum_{a\in Q}d_a(\xi)-|N_\xi(Q)|=97-\Gamma_Q(\xi).}       \tag{2.6}
\]

Hence every supplier-perfect continuation on this same parent and
state-expanded catalogue must satisfy

\[
                              \Gamma_Q(\xi)\ge97.            \tag{2.7}
\]

Equation (2.6), including losses of old last neighbours, is exact.  It is
only one necessary Hall row; after repairing it, Theorem 2.1 must separate
the new maximum-deficiency shore.

## 3. Directional circuit radius and the forced escape from `M`

Let `F` be another matching in `J+`.  Relative to `F_0`, put

\[
             r=|F_0-F|,\qquad s=|F-F_0|.                    \tag{3.1}
\]

The audited `Q` contains no selected new-`LLR` head.  Removing one retained
transfer therefore cannot deactivate an incumbent occurrence of `Q`; it
can improve (2.5) only through the two changed source identities.  Adding
one transfer can improve (2.5) through at most those two identities and one
deactivated surviving-`LMR` head.  Lost neighbours have the opposite sign
and only make the bound stronger.

### Theorem 3.1 (sharp inherited-shore directional cut)

Every supplier-perfect matching `F` in the fixed-nontransfer-mode `b268`
face obeys

\[
                         \boxed{2r+3s\ge97.}                 \tag{3.2}
\]

Since `nu(J+)=464`, also `s-r<=27`.  Therefore

\[
                         \boxed{r\ge4,\qquad r+s\ge34.}      \tag{3.3}
\]

At cardinality `437`, (3.2) gives

\[
       \boxed{r=s\ge20,qquad |F\mathbin\triangle F_0|\ge40.} \tag{3.4}
\]

At cardinality `464`, it gives

\[
       \boxed{r\ge4,qquad s\ge31,qquad
              |F\mathbin\triangle F_0|\ge35.}              \tag{3.5}
\]

#### Proof

The per-removal and per-addition upper charges just described sum to an
upper bound `2r+3s` on (2.5), regardless of negative neighbour losses.
Combine with (2.7).  If `r+s<=33`, then `s-r<=27` forces `r>=3`, while
`2r+3s=3(r+s)-r<=96`; hence (3.3).  Equations (3.4)--(3.5) follow by
substituting `s=r` and `s=r+27`.  \(\square\)

There is an independent radius centred at `M`.  Toggling one transfer
changes two supplier-source menus and replaces at most one head occurrence.
Changing the complete adjacency of one bipartite vertex changes matching
rank by at most one.  Removing old edges down to the intersection and then
adding new edges preserves (1.2), so

\[
                    |\nu(G_F)-\nu(G_{F'})|
                    \le3|F\mathbin\triangle F'|.             \tag{3.6}
\]

Since `M` has deficiency `131`, every supplier-perfect `F` satisfies

\[
                       |F\mathbin\triangle M|\ge44.          \tag{3.7}
\]

Put `k=|F|` and `b=|F-M|`, the number of transfer columns outside the
entire supplied `464` matching.  The identity

\[
 |F\mathbin\triangle M|=(464-k+b)+b
                       =464-k+2b                              \tag{3.8}
\]

gives the exact necessary outside-column bound

\[
 \boxed{
       b\ge \max\left\{0,
          \left\lceil\frac{k-420}{2}\right\rceil\right\}.}  \tag{3.9}
\]

In particular:

* every subset of `M` of size `421,...,464` is supplier-infeasible;
* a size-`437` repair requires at least **nine** columns outside `M`, in
  addition to the `20`-for-`20` lower bound (3.4); and
* a size-`464` repair requires at least **twenty-two** columns outside `M`.

For two transfer matchings, the symmetric difference is a disjoint union
of alternating paths and even cycles.  A component with `t` edges uses `t`
physical rows if it is a cycle and `t+1` if it is a path.  The net size
increase is at most the number of path components.  Thus a hypothetical
size-`464` repair relative to `F_0` must touch at least

\[
                       35+27=62                              \tag{3.10}
\]

physical transfer rows.  These are lower bounds, not constructions.

### Corollary 3.2 (the principal downward face)

Let `R=M-F_0`, `|R|=27`, and let

\[
 S=(F_0-U)\cup A,qquad U\subseteq F_0,quad A\subseteq R,
 \quad r=|U|,quad a=|A|.                                  \tag{3.11}
\]

Then the inherited shore requires

\[
                              2r+3a\ge97.                    \tag{3.12}
\]

But (3.7) is stronger globally on this cube: every supplier-perfect
`S subseteq M` must have `|S|<=420`.  In particular there is no exact-size
`437` solution anywhere in the principal downward cube, no matter which of
the deleted `27` edges are restored.  On the narrower descendant face
`S subseteq F_0`, (3.12) gives the sharper requirement

\[
                              r\ge49,qquad |S|\le388.        \tag{3.13}
\]

## 4. What an alternating circuit can and cannot certify

For any two transfer matchings, their symmetric difference consists of
vertex-disjoint alternating paths and even cycles.  Flipping a component is
the exact row-disjoint transfer exchange.  The smallest cardinality-neutral
open exchange is a two-edge alternating path on three rows; the smallest
closed structural circuit is a `C4` on four rows.

Supplier improvement does **not** decompose into fixed component weights.
Several changed heads can share an unchanged supplier identity, and the
neighbour variable in (2.1) is an OR.  Two disjoint components may therefore
be redundant or synergistic.  Searching only individually improving
circuits is incomplete, even though the transfer symmetric difference has
an ordinary alternating decomposition.

The exact minimum-support quantity at transfer cardinality `k` is

\[
 \tau_k=min\left\{|F\mathbin\triangle F_0|:
      F\text{ satisfies (1.2)},\ |F|=k,\ \nu(G_F)=16898\right\}. \tag{4.1}
\]

Equations (1.2), (2.3), and a Hamming objective separate (4.1) exactly by
branching plus supplier min-cuts.  Theorems 3.1 and (3.9) are valid initial
cuts.  There is no general function of the initial deficiency which upper
bounds `tau_k`: an activated supplier path can have deficiency one while
requiring arbitrarily many private, row-disjoint activations before its last
head becomes matchable.

The transfer sets themselves are graph matchings, not a matroid.  On a
three-edge path the two outer edges form a matching of size two, while the
middle edge cannot be augmented by either one.  The supplier rank is not a
matroid rank either, since on one parent

\[
       \nu(G_\varnothing)=16796,qquad
       \nu(G_{F_0})=16801,qquad
       \nu(G_M)=16767,qquad F_0\subset M.                   \tag{4.2}
\]

### Lemma 4.1 (support-sharp first column outside the downward face)

For `e in J+-M`, let

\[
             C_M(e)=\{f\in M:f\text{ shares an endpoint with }e\}. \tag{4.3}
\]

Then `|C_M(e)|` is `0`, `1`, or `2`, and

\[
                  M(e)=(M-C_M(e))\cup\{e\}                 \tag{4.4}
\]

is the unique inclusion-maximal retention of `M` after forcing `e`.  It
changes `1+|C_M(e)|` transfer edges and exactly `2+|C_M(e)|` physical rows.
Because `M` is maximum, the case `|C_M(e)|=0` cannot occur.  Hence the
smallest structural escape from `M` is

* a neutral two-edge alternating path on three rows when `|C_M(e)|=1`; or
* a three-edge descent on four rows when `|C_M(e)|=2`.

This is sharp for forcing that one outside column.  It certifies no supplier
gain.  Relative to the nonmaximum `F_0`, an outside edge whose conflicts all
belong to `M-F_0` can be added on two rows, but (3.4) and (3.9) prove that no
one-column move can finish the supplier projection.

#### Proof

`M` is a matching, so at most one of its edges meets each endpoint of `e`.
Every matching containing `e` must delete precisely those conflicts, while
all other edges of `M` remain mutually disjoint and disjoint from `e`.
The support counts follow by drawing the resulting alternating path.
If there were no conflict, `M+e` would contradict `|M|=nu(J+)=464`.
\(\square\)

### Proposition 4.2 (an exact weighted subface)

On the monotone descendant face `F_0-U`, every occurrence of `Q` remains
active.  For `e in F_0`, let `c_e` be the signed change in the number of
distinct `Q`-neighbour identities contributed by the two physical source
rows of `e` when `e` is undone.  The transfer endpoints are pairwise
disjoint, so those supplier identities are distinct between edges and

\[
 |N_{F_0-U}(Q)|-|N_{F_0}(Q)|=\sum_{e\in U}c_e,qquad c_e\le2. \tag{4.5}
\]

Consequently the inherited shore is repaired to target deficiency at most
`delta` exactly when

\[
                       \sum_{e\in U}c_e\ge97-\delta.         \tag{4.6}
\]

Equation (4.6) is an exact linear shore cut on this one monotone subface.
It does not replace the other Hall cuts, and it does not extend additively
to arbitrary alternating exchanges where head activities and shared
neighbour ORs also change.

## 5. Exact protected root-bank/common-basis augmentation

The current `a=437` table lies outside the older compressed-normal
`a=0` common-basis face on receivers `M(rank7) union R`.  Nevertheless its
**fixed-prefix root layer** has an exact two-matroid formulation.

Pin every protected row and every lower prefix which is not being changed.
Delete every root-assignment arc forbidden by the declared `b268` parent.
Let

* `P_7` be the remaining prefixes whose top target has rank seven;
* `P_L` be the remaining prefixes whose top target has rank at most six;
* `R_0` be the unpinned rank-eight root rows;
* `K_7 subseteq P_7 times R_0` and `K_L subseteq P_L times R_0` be the
  remaining strict-containment assignment graphs.

One may additionally delete arcs failing a **unary, parent-replayed**
marginal-socket mode.  Shared occurrence/history constraints are not unary
and are treated after the theorem.

Let `M_7` and `M_L` be the transversal matroids on ground set `R_0` induced
by `K_7` and `K_L`: a root subset is independent when it can be saturated
by distinct prefixes of the corresponding class.  Assume their full ranks
sum to `|R_0|`, as they do after contracting a represented complete root
assignment.  Let `D` be the roots currently assigned to low-ending prefixes
and `B=R_0-D` the rank-seven receiver bank.

### Theorem 5.1 (protected root-bank common-base theorem)

A root subset `D' subseteq R_0` supports a complete parent-valid
reassignment of the pinned lower prefixes, with low roots `D'` and
rank-seven bank `R_0-D'`, if and only if

\[
              \boxed{D'\text{ is a common basis of }
                     M_L\text{ and }M_7^*.}                 \tag{5.1}

Hence the minimum number of root-bank membership changes, with arbitrary
additive root costs, is an exact weighted matroid-intersection problem.

For `d in D` and `b in B`, the one-out/one-in exchange

\[
              D'=D-d+b,qquad B'=B-b+d                    \tag{5.2}

is legal if and only if

\[
 \boxed{
 d\in C_{M_L}(b,D)quad\text{and}\quad
 b\in C_{M_7}(d,B),}                                      \tag{5.3}

\]

where `C_M(e,B)` is the fundamental circuit of `e` relative to base `B`.
Each membership in (5.3) is certified by an alternating path in the
corresponding bipartite presentation.  Thus (5.3) is the exact
two-sided/fundamental-alternating-path test for a minimum element-support
root-type exchange.  If no pair satisfies (5.3), batch changes require the
ordinary common-base exchange graph; common bases are not being claimed to
form a matroid.

#### Proof

The low prefixes can be matched into `D'` exactly when `D'` is a basis of
`M_L`.  The rank-seven prefixes can be matched into its complement exactly
when `R_0-D'` is a basis of `M_7`.  By the definition of duality, the latter
condition is equivalent to `D'` being a basis of `M_7^*`, proving (5.1).
The fundamental-circuit exchange criterion applied once in each matroid
gives (5.3).  Transversal fundamental circuits are represented by the usual
alternating reachability from the entering root.  \(\square\)

There is a support-two special case.  If the current explicit assignment
contains a rank-seven-ending prefix `P_M -> r` and a low-ending prefix
`P_L -> q`, with top targets `m` and `u`, then swapping the two full prefixes
is valid exactly when

\[
                         u\subsetneq r,qquad m\subsetneq q. \tag{5.4}

This root-type `C4` changes the bank by `B-r+q`, preserves every target,
root, owner, chain type, and pinned row, and touches two root rows.  No
one-row bank change can preserve the root assignment, so support two is
sharp when (5.4) holds.  A closed reassignment entirely inside a fixed
rank-seven/root bank has no `C4`, because two distinct rank-seven sets have
at most one common rank-eight superset; its first possible closed circuit is
`C6`.  A bank-changing fundamental alternating path can be shorter.

### Scope of Theorem 5.1

The theorem is exact for the static, unary-filtered root layer after literal
protected pins.  A common basis `D'` alone does not choose its two
representing prefix matchings.  Supplier incidences, transfer modes, and
socket prices may depend on those representatives.

More importantly, one common endpoint/history state is not generally a
unary root-arc predicate.  For that literal problem, branch on the common
parent state and occurrence choices, form `K_7,K_L` from the active arcs,
apply Theorem 5.1 inside the branch, and separate the supplier child by
Theorem 2.1.  This is a proof-safe common-basis-plus-Benders augmentation;
it is not a claim that the colored/state-expanded system is a matroid or a
single min-cut.

No root-type exchange satisfying (5.3), (5.4), the two-phase socket replay,
and supplier improvement has yet been authenticated for this table.

## 6. Frozen conclusions and open gates

Frozen here:

1. the one-parent `b268` contract and literal protection of the `7,213`
   rows on the declared transfer face;
2. strict Pareto dominance `deficiency 102 -> 97`, together with the fact
   that the `437` table is still obstructed by its exact `111/14` shore;
3. the exact activity-aware Hall min--max and min-cut Benders oracle;
4. the directional cut `2r+3s>=97` and the fixed-size-`437` radius `>=40`;
5. the `M`-centred radius `>=44`, closing every downward layer
   `421,...,464` and forcing at least nine outside-`M` columns at size `437`;
6. the support-sharp first outside-column alternating path/descent;
7. the exact linear inherited-shore cut on monotone descendants; and
8. the protected fixed-prefix root-bank common-base theorem and mutual
   fundamental-circuit criterion.

Not proved:

* that any matching in the full `11,893`-edge face has supplier rank
  `16,898`;
* that the lower bounds `40`, `9`, or `22` are attained;
* that a supplier-improving root-type exchange exists;
* that phasewise marginal-positive tickets admit one common occurrence and
  shared endpoint-history selection;
* that the residual outer matching and long--long arcs complete; or
* carrier-opening phase transport, chronology/Euler connectivity,
  residence, upper, compiler, or a K17 word.

The next proof-safe exact search object is therefore not a scalar transfer
score.  It is either (i) the `J+` matching master with parent-bound state
activations and Hall cuts (2.3), seeded by (3.2) and (3.9), or (ii) the
protected common-base root master of Theorem 5.1 with explicit representing
matchings, the same state activations, and the same supplier separator.

## 7. Load-bearing local hashes

```text
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv
30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.all_edges.tsv
c5c4e00f35e5300e02274142d05252fb122d9e4156e4fdca44b14e887bc08859
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.native_phase0.tsv
637a046bf5ed7552b204e3727b9693ef71442538f39547b51ba7140dba4203fe
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.transported_phase1.tsv
e44a3fdb7b1fd217ef59685c5e505bbf6acfc055022ddc2cb1f89e68af386425
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.common464.matching.audit.json
81c2d9a4e8f0415eaddf12c4555a005ec44651e3b76704bb40e9f87d0ca0a539
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.common464.selected.tsv
94c16918d61ad0945b32bd501a69b528f4c4734800c8f7d61c84eb07e590b361
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.common464.projection.audit.json
869911434312e62743353f6d12bcecf776f5c1ad6a36192f8d5b05b15427958e
  scratch/q1_k17_b268_llr_dm_descent_20260802/audit.json
e9704b820222d93f56bcbf348d202651f2ace1082e1fb65eb6c21fce88d2db25
  scratch/q1_k17_b268_llr_dm_descent_20260802/b268_llr.protected.common464_undo27dm.selected.tsv
b6a51766dd8c7632a79f1f60abea26deced8cc5f40aec952bc8b704a3600c2b6
  scratch/q1_k17_b268_llr_dm_descent_20260802/b268_llr.protected.common464_undo27dm.table.tsv
2a5a5263c41d5b8fada2b26e8a97a6cccc4ae05ce70a579d71ced8e6dd6ef1e4
  scratch/q1_k17_b268_llr_dm_descent_20260802/b268_llr.protected.common464_undo27dm.projection.audit.json
32ef30eebd5113bb2004ecf994da24ce1dd9f704e38e5c16060cac188ba9e194
  scratch/q1_k17_b268_llr_dm_descent_20260802/b268_llr.protected.common464_undo27dm.hall.tsv
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  scratch/q1_k17_b268_llr_dm_descent_20260802/b268_llr.protected.common464_undo27dm.new_dm_transfers.tsv
```
