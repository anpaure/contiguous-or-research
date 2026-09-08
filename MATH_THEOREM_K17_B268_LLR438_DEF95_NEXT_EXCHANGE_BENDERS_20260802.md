# K17 b268 LLR438-def95: exact next-exchange Benders theorem

**Date:** 2026-08-02  
**Status:** proof-safe at the authoritative `b268...` static-table,
phasewise relaxed-nine marginal-socket, and complete `6/9/4`
supplier-projection scopes.  This note supersedes `def96` and the earlier
`454/def96` incumbent.  It contains no warm47 table mixing.  Transported
phase one remains root-aligned; carrier-opening transport is not proved.

> **Successor notice.**  After this centre was frozen, the root-owned clean
> radius chain was verified through `def94` and `def93`.  The min--max and
> next-target theorem below apply verbatim with the current deficiency in
> place of `95`.  The concurrently written shared target-`92` directory is
> explicitly UNKNOWN and is not evidence for this note.  Only a clean,
> hash-bound successor may supersede the `def93` centre.

## 0. New authoritative incumbent

Let `F_*` be the selected transfer set with SHA

```text
d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
```

and let `T_*` be its table, SHA

```text
ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374.
```

Both derive literally from the parent

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc.
```

The exact ledger is

\[
 |F_*|=438,\qquad
 (LLR,LMR,LR,MR)=(438,16477,4424,2971).                     \tag{0.1}
\]

All `7,213` protected ticket rows are byte-identical to the `b268` parent.
The marginal socket tuple is

\[
 (p0,p1,both,either)=(3098,2253,1839,3512).                 \tag{0.2}
\]

The independently replayed supplier projection is

\[
 \nu(G_{F_*})=16803,\qquad \delta(F_*)=95,\qquad
 Z(F_*)=80,                                                  \tag{0.3}
\]

with a maximum-deficiency shore

\[
                |Q_*|=109,\qquad |N_{F_*}(Q_*)|=14.         \tag{0.4}
\]

All `80` isolated heads lie in `Q_*`; the other `29` shore heads still have
only `14` supplier identities.  Repairing isolated heads alone therefore
leaves a deficit of `15` unless it simultaneously expands the distinct
neighbour bank.

Relative to the former `def96` size-`438` table, `F_*` is exactly

\[
 F_* = F_{96}-\{41\}+\{89826\}.                             \tag{0.5}
\]

The removed and added edges have endpoints

```text
edge 41:    LR 49,    LMR 136
edge 89826: LR 23929, LMR 9998.
```

All four rows are distinct and avoid the protected set.  Thus (0.5) is two
disconnected one-edge alternating-path components, balanced only by the
fixed-cardinality equation.  It changes four physical rows.  The socket
tuple (0.2) is unchanged from `F_96`, but supplier rank rises
`16802 -> 16803`, zero heads fall `81 -> 80`, and the shore changes
`110/14 -> 109/14`.

This authenticates a literal parent-valid supplier-improving coupled
exchange.  In particular, supplier rank is not determined by transfer
cardinality or by the four marginal socket totals.

Relative to the earlier `F_437` and supplied `M_464`, the direct lineage is

\[
 F_*=(F_{437}-\{41\})\cup\{57336,89826\},\qquad
 F_*\cap M=F_{437}-\{41\}.                                 \tag{0.6}
\]

Thus `|F_*-M|=2`, `|M-F_*|=28`, and
\( |F_*\mathbin\triangle M|=30 \).

## 1. One-parent Hall min--max

Let `J+` be the `11,893`-edge protected, two-phase marginal-positive
transfer graph on this same parent.  Its matching number is `464`.  For a
matching `F subseteq J+`, let `G_F` be the deterministic complete union
supplier projection.  In a state-expanded version, replace each marginal
record below by its exact active occurrence/history DNF.

Every transfer moves the identical bottom label `ell` from its `LMR` donor
to its new `LLR` host.  Therefore the predicate `rank(ell)>1`, and hence the
hard-head census `K=16898`, is invariant on the whole transfer face.

For a fixed universe of mode-labelled hard-head occurrences `A` and
physical supplier identities `U`, write

\[
 d_a(F)=\mathbf1[a\text{ is active}],\qquad
 n_u^X(F)=\mathbf1[u\text{ has an active edge into }X].     \tag{1.1}
\]

The neighbour variable is a bidirectional OR of literal records; possible
but unselected records do not count.

### Theorem 1.1 (exact parent-valid supplier separator)

For every integral parent-valid table state,

\[
 \boxed{
 \nu(G_F)=16898-
    \max_{X\subseteq A}
       \left(\sum_{a\in X}d_a(F)-\sum_{u\in U}n_u^X(F)\right).} \tag{1.2}
\]

Target deficiency at most `Delta` is equivalent to

\[
 \boxed{
   \sum_{a\in X}d_a(F)-\sum_u n_u^X(F)\le\Delta
   \qquad(X\subseteq A).}                                  \tag{1.3}
\]

One supplier maximum matching/minimum cut separates (1.3) for a fixed
candidate.  Hence transfer branching plus the exact active rows (1.3) is a
finite proof-safe Benders formulation.

#### Proof

This is Hall's deficiency theorem with head activities and distinct
supplier-neighbour ORs written explicitly.  The standard unit-capacity
supplier matching network yields the minimum-cut separator.  \(\square\)

### Corollary 1.2 (exact one-step radius ladder)

Let `F^(d)` be any clean, one-parent incumbent with supplier deficiency
`d`, and define

\[
 h_F(X)=\sum_{a\in X}d_a(F)-|N_F(X)|,
 \qquad
 \Gamma_X^{(d)}(F)=h_{F^{(d)}}(X)-h_F(X).                  \tag{1.3a}
\]

Then a candidate has deficiency at most `d-1` if and only if

\[
 \boxed{
 \Gamma_X^{(d)}(F)\ge h_{F^{(d)}}(X)-(d-1)
 \qquad(X\subseteq A).}                                   \tag{1.3b}
\]

In particular every maximum-deficiency incumbent shore requires at least
one net signed unit.  One maximum matching/min-cut on the candidate verifies
all of (1.3b) at once.  This is the exact theorem for the verified
`def93 -> target92` step once the clean `def93` parent artifacts are bound.
No numerical `Q_93` size, zero count, or directional `2/3` coefficient is
assumed here.  Those quantities must be replayed from that clean incumbent;
they cannot be inherited from `def95` or from the UNKNOWN shared target-`92`
directory.

For a candidate `F`, define the signed repair of the incumbent shore by

\[
\begin{split}
 \Gamma_*(F)={}&\sum_{a\in Q_*}\bigl(d_a(F_*)-d_a(F)\bigr)\\
 &+|N_F(Q_*)-N_{F_*}(Q_*)|
  -|N_{F_*}(Q_*)-N_F(Q_*)|.                                \tag{1.4}
\end{split}
\]

Then the identity

\[
 \boxed{
 \sum_{a\in Q_*}d_a(F)-|N_F(Q_*)|=95-\Gamma_*(F)}          \tag{1.5}
\]

is exact.  Therefore

* supplier perfection requires `Gamma_*(F)>=95`; and
* the next target `deficiency <=94` requires

\[
                         \boxed{\Gamma_*(F)\ge1.}            \tag{1.6}
\]

The loss term in (1.4) is essential.  Passing (1.6) repairs the inherited
shore only; (1.3) must still be separated because another shore may exceed
`94`.

Concretely, (1.6) demands at least one net unit from deactivating an
incumbent `Q_*` occurrence or adding a genuinely new distinct `Q_*`
supplier, after subtracting reactivated heads and lost last neighbours.
Giving an isolated head a supplier identity already counted among the old
`14` does not by itself pass the cut.

## 2. Exact one-for-one theorem for the `def94` target

For `f in F_*` and `e in J+-F_*`, put

\[
                         F_{f\to e}=F_*-f+e.                 \tag{2.1}
\]

Call `(f,e)` structurally admissible when `e` meets no edge of
`F_*-f`.  Equivalently,

\[
              C_{F_*}(e):=\{g\in F_*:g\cap e\ne\varnothing\}
              \subseteq\{f\}.                              \tag{2.2}
\]

There are three exact literal-support types.

* If `e` and `f` share their donor, the donor remains in the same `MR` mode;
  only the old and new hosts change.  This is a two-row table move and is the
  true minimum-support fixed-cardinality successor.
* If they share their host, the old donor, new donor, and common host change,
  so the literal support is three rows.
* If `C_{F_*}(e)` is empty, removal and addition are two disconnected
  one-edge alternating paths and four table rows change.

In graph-endpoint language either shared-endpoint case is a two-edge
alternating path on three vertices.  Literal table support is smaller in the
shared-donor case because the common donor's resulting `MR` payload is
donor-independent.

### Theorem 2.1 (exact radius-one acceptance criterion)

A one-for-one successor of `F_*` with deficiency at most `94` exists if and
only if there is a structurally admissible pair `(f,e)` such that

\[
 \boxed{
 \sum_{a\in X}d_a(F_{f\to e})-
       \sum_u n_u^X(F_{f\to e})\le94
       \qquad(X\subseteq A).}                              \tag{2.3}
\]

Every such pair necessarily satisfies the cheap incumbent-shore filter

\[
                         \Gamma_*(F_{f\to e})\ge1.           \tag{2.4}
\]

Conversely, (2.4) plus one exact min-cut verification of (2.3) is sufficient.
Thus the complete radius-one oracle is an on-demand bipartite graph whose
left vertices are removable selected edges, whose right vertices are
unselected `J+` edges, and whose structural arcs satisfy (2.2); candidate
arcs are accepted only after the coupled table materialization and supplier
min-cut.

For the three support types above, the cheap incumbent-shore charge is at
most respectively `2`, `4`, and `5`; the complete supplier-rank change is
at most respectively `3`, `5`, and `6`.  These are upper bounds only.  In
particular, a support-two successor exists exactly when a selected donor has
an admissible `J+` edge to a currently unmatched host; it reaches `def94`
exactly when it passes (2.3).

#### Proof

Condition (2.2) is exactly the matching condition for (2.1).  Membership of
`e` in `J+` and removal of `f` preserve the literal protected rows and the
declared phasewise marginal-positive transfer face.  Theorem 1.1 with
`Delta=94` proves (2.3), while (1.5) proves (2.4).  \(\square\)

There is no proof-safe decomposition

\[
            \Gamma_*(F_{f\to e})=w^-(f)+w^+(e)              \tag{2.5}
\]

with fixed scalar edge weights in general.  Removing `f` changes two source
menus and possibly head activity; adding `e` changes two more.  Their
head-neighbour incidences meet through shared supplier ORs.  The successful
exchange (0.5), with unchanged socket totals, is a concrete warning that
socket-count pricing is insufficient.  Exact pricing is on the coupled
pair followed by the min-cut, not on its two columns independently.

Define the fixed-size next-target radius

\[
 \tau_{94}=\min\{|F\mathbin\triangle F_*|:
      F\subseteq J^+\text{ is a matching},\ |F|=438,
      \delta(F)\le94\}.                                    \tag{2.6}
\]

Equal-cardinality matchings have even symmetric difference, so

\[
             \tau_{94}\ge2.                                \tag{2.7}
\]

Theorem 2.1 decides exactly whether equality holds.  If every admissible
pair fails (2.3), then `tau_94>=4` and the next master must select a balanced
collection of alternating path/cycle components.  No such radius-one no-go
is asserted here.

## 3. Full-rank radius from the new incumbent

A direct ID intersection of the `109` incumbent head rows with the `438`
selected new-`LLR` host rows is empty.  This is a direct classified
intersection replay of the frozen `iter1.hall.tsv`, `iter1.selected.tsv`,
and protected edge catalogue; it is not merely inferred from the scalar
audit JSON.  Hence deleting a selected transfer
cannot deactivate an incumbent occurrence of `Q_*`; its positive charge in
(1.4) is at most the two changed supplier identities.  Adding a transfer can
deactivate at most one incumbent surviving-`LMR` head and changes at most two
supplier identities.

Let

\[
                 r=|F_*-F|,\qquad s=|F-F_*|.                \tag{3.1}
\]

### Theorem 3.1 (new directional perfect-rank cut)

Every supplier-perfect matching in the same fixed-mode `b268` transfer face
satisfies

\[
                         \boxed{2r+3s\ge95.}                 \tag{3.2}
\]

Because `|F|<=464`, also `s-r<=26`, and therefore

\[
                         \boxed{r\ge4,\qquad r+s\ge33.}    \tag{3.3}
\]

At the incumbent cardinality `438`,

\[
       \boxed{r=s\ge19,\qquad |F\mathbin\triangle F_*|\ge38.} \tag{3.4}
\]

At cardinality `464`,

\[
       \boxed{r\ge4,\qquad s\ge30,\qquad
              |F\mathbin\triangle F_*|\ge34.}              \tag{3.5}
\]

These are necessary projection bounds, not existence statements.

The two one-sided specializations are also exact necessary bounds:

\[
 \boxed{\text{removal only: }r\ge48,\qquad
        \text{addition only: }s\ge32.}                     \tag{3.5a}
\]

The latter cannot occur before the matching cap, because only `26` net
augmentations are available from cardinality `438`.

#### Proof

As in (1.4), neighbour losses count negatively.  Each removal can therefore
contribute at most two positive units and each addition at most three.
Combine with the perfection threshold `Gamma_*>=95`.  Substitution of
`s-r<=26`, `s=r`, and `s=r+26` gives (3.3)--(3.5).  \(\square\)

The older size-`464` matching `M` still has supplier rank `16767` and
deficiency `131`.  One transfer toggle changes the adjacency of at most two
supplier vertices and one head vertex, so supplier rank is three-Lipschitz:

\[
                    |\nu(G_F)-\nu(G_{F'})|
                    \le3|F\mathbin\triangle F'|.             \tag{3.6}
\]

Every supplier-perfect `F` therefore satisfies

\[
                       |F\mathbin\triangle M|\ge44.          \tag{3.7}
\]

If `k=|F|` and `b=|F-M|`, then

\[
 |F\mathbin\triangle M|=464-k+2b,\qquad
 b\ge\max\left\{0,\left\lceil\frac{k-420}{2}\right\rceil\right\}. \tag{3.8}
\]

The new incumbent has exactly two columns outside `M`, namely `57336` and
`89826`, and omits `28` columns of `M`; hence

\[
                         |F_*\mathbin\triangle M|=30.        \tag{3.9}
\]

A supplier-perfect size-`438` table needs at least nine outside-`M` columns.
Thus any full-rank continuation from `F_*` must introduce at least seven
additional outside-`M` columns net.  This full-rank statement is separate
from the next `def94` target, for which the `M`-centred radius is already
satisfied and gives no additional local restriction.

The distance from `F_*` to the principal downward cube `D(M)` is exactly
two: delete its two outside columns, reaching cardinality `436`.  At fixed
cardinality `438`, re-entering `D(M)` requires at least four toggles, because
both outside columns must be deleted and two `M` columns restored.  A single
one-for-one successor changes the outside count by at most one, so it cannot
re-enter `D(M)`.  Returning all the way to `M` requires the exact `30`
toggles in (3.9).

## 4. Balanced alternating components, not matroid circuits

For any two transfer matchings, their symmetric difference is a disjoint
union of alternating paths and even cycles.  A fixed-cardinality exchange
is any collection of those components for which the total number of entering
and leaving edges balances.  Individual components need not be balanced:
the authenticated move (0.5) is exactly one leaving singleton path plus one
entering singleton path.

This is the correct branch-flow abstraction for the next search:

1. select a balanced, row-disjoint collection of alternating components;
2. activate the exact resulting `b268` row modes and phasewise socket DNFs;
3. apply the signed shore filter (1.6); and
4. separate all supplier cuts (1.3) by a min-cut.

Transfer matchings are not a matroid, and supplier rank is not a matroid rank.
The latter is already witnessed on one parent by

\[
 \nu(G_\varnothing)=16796,
 \quad\nu(G_{F_{437}})=16801,
 \quad\nu(G_M)=16767,
 \quad F_{437}\subset M.                                  \tag{4.1}
\]

Nor is a connected-circuit-only search complete: (0.5) improves rank using
two disconnected alternating components.  The exact child is Hall matching;
the exact master is branch--Benders, not a generic matroid exchange oracle.

## 5. Root-type/common-basis augmentation remains available

The new transfer incumbent does not alter the static root-layer theorem.
After pinning the `7,213` protected rows and every fixed lower prefix, split
the remaining prefixes into rank-seven-ending `P_7` and low-ending `P_L`.
On the unpinned root ground `R_0`, let `M_7` and `M_L` be the transversal
matroids induced by their parent-valid strict-containment assignment graphs.
Unary parent-replayed marginal-socket failures may be deleted as arcs.

If `D` is the low-root set and `B=R_0-D` the rank-seven bank, then a new
root set `D'` supports both root matchings exactly when

\[
                    \boxed{D'\text{ is a common basis of }
                           M_L\text{ and }M_7^*.}            \tag{5.1}
\]

A one-root-type exchange `D'=D-d+b`, `B'=B-b+d` is legal exactly when

\[
 \boxed{
 d\in C_{M_L}(b,D),\qquad b\in C_{M_7}(d,B).}              \tag{5.2}
\]

Each test is an alternating-path test in its transversal presentation.
This is an exact static/common-parent augmentation lemma, not a claim that
common bases form a matroid.  Shared endpoint histories, representative-
matching-dependent supplier incidences, and nonunary socket states still
require explicit branching and Theorem 1.1.  No supplier-improving root-type
exchange is authenticated here; the new `def95` gain was achieved wholly
inside the transfer face.

## 6. Frozen result and remaining work

Frozen here:

1. the literal `b268` one-for-one exchange `remove 41 / add 89826`;
2. byte identity of all `7,213` protected rows;
3. unchanged marginal socket tuple `3098/2253/1839/3512` across the
   `def96 -> def95` swap;
4. supplier rank `16803/16898`, deficiency `95`, `80` zeros, and the exact
   `109/14` obstruction;
5. the exact target-`94` signed acceptance cut and radius-one min-cut oracle;
6. the full-rank directional radius `38` at fixed size `438`; and
7. the unchanged outside-`M` and protected root-bank augmentation theorems.

Still open:

* whether any one-for-one successor of `F_*` reaches deficiency `94`;
* if not, the minimum balanced multi-component support;
* supplier perfection anywhere in the `11,893`-edge transfer face;
* one simultaneous occurrence-labelled socket/history selection;
* residual outer completion and long--long chronology; and
* transported-phase-one carrier opening, residence, upper, compiler, and a
  K17 word.

## 7. Load-bearing hashes

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/private_h_outer_materialized.tsv
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv
30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
  scratch/q1_k17_b268_llr_common464_20260802/b268_llr.protected.all_edges.tsv
d6dca87229b542481f4f686f851c15700939db9b952cd26ce9df3b47d19bb8f0
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.selected.tsv
ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.table.tsv
09e3c0303134781c985be87221749a2c520e39702df36731e0f213c2d2542874
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.native_phase0.dnf.tsv
343c0c7b25ed4da8e94458ef98594926db3552401c9fce31613b7d3a81d364f8
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.transported_phase1.dnf.tsv
54ec235f807cdc73ce09f1b42fa8639b1f10820f0c9aea5e2f54fbf164d733ae
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.projection.audit.json
23225a9b98a8a3cebf1a22ae468d43e56e2cbd56f9cc506b0b1c8d1426d5029f
  scratch/q1_k17_b268_llr_radius_def95_20260802/iter1.hall.tsv
50dccba751fab5264023d8e08f8e8b628b7919154107b5a80fa8cf419f0dddb5
  scratch/q1_k17_b268_llr_radius_def95_20260802/audit.json
1d7bdfdbbaea9636b22d9792214a88c14f48232854ecbb35f21b54bd5ceaec84
  scratch/audit_k17_b268_def95_lineage_agent_20260802/independent.audit.json
daf7b4ee1d968d7ecc536e2ae4ace8b7f5cd6e1780ce6e1d614fe58a6b2ee12d
  scratch/audit_k17_b268_def95_price_agent_20260802/def95.independent.audit.json
```
