# K17 planted `B_5`: inverse outer parent and regenerated ticket ledger

**Date:** 2026-08-02
**Status:** exact finite theorem.  The planted compressed-normal table has an
explicit origin-form inverse parent, and both local `B_5` modes are exact
outer materializations of that same parent.  A regenerated `1,748`-ticket
ledger has `3,495` common real outer edges and passes every canonical physical
five-cell replay in both local modes.  The fixed regenerated ledger is
**not** common to the two s7 owner phases: it replays on only `520/501`
records.  A phase-specific s7 reselection, aggregate history, reset,
residence, selected-state supplier, compiler, selected `z=6` occurrence
closure, chronology, a clone-good bank, and every bound on `nu(k)` remain
**UNPROVED**.

## 0. Outcome and quantifier boundary

Let `T^0` be the planted table

```text
scratch/k17_common_basis_b5_protected_host_20260802/
  constructed_common_basis_b5_host.tsv
SHA-256 d00a9138e211c49071c5a8848d433850764461a5d8e3bc8e8c359840e6bec78f
```

Its exact type census is

\[
 \begin{array}{c|rrrr}
  \text{type}&\text{hard LMR}&\text{singleton-soft LMR}&LR&MR\\ \hline
  \text{rows}&16898&17&4862&2533.
 \end{array}                                                   \tag{0.1}
\]

The static inverse-parent gate is now closed, in a stronger form than an
arbitrary choice of short shore:

1. the same `1,748` rows used as shorts by the frozen private ticket bank are
   retained as the unoccupied hard shore;
2. an explicit containment matching assigns them `1,748` distinct bottoms
   from `LR` rows;
3. the resulting origin-form table `P*` has census

   \[
       (\text{free},\text{fixed length two},\text{singleton-soft},
         \text{hard})=(1748,3899,17,18646);                    \tag{0.2}
   \]
4. exact outer matchings `mu^0,mu^1` rematerialize the two planted `B_5`
   modes, with `mu^1=kappa mu^0`; and
5. after changing only the real source-token labels in the old ticket list,
   all `1,748` tickets and all `3,495` real forced edges are literal in both
   local modes.
6. Substituting the two s7 owner maps into that one fixed regenerated ledger
   gives exact pass counts `520` and `501`, so fixed-ledger owner-phase
   transport is refuted.

Here **mode zero/one** means the two local bottom assignments of the planted
`B_5` actuator on one fixed owner table.  It does not mean the two s7 owner
phases.  No s7 phase-common state is inferred below.

## 1. Exact inverse-materialization criterion

Consider any target-partition table `T` with the census (0.1).  Let

* `Q` be its 17 singleton-soft `LMR` rows;
* `H` be its 16,898 other `LMR` rows;
* `A` be its 4,862 `LR` rows; and
* `B` be its 2,533 `MR` rows.

For `v in H union A`, write `ell_v` for the lower target.  For
`u in H union B`, write `m_u subset r_u` for the middle/root suffix.

Choose

\[
                 F\subseteq A,\qquad S\subseteq B,
                 \qquad |F|=|S|=1748.                         \tag{1.1}
\]

The candidate receiver-bottom shore and hard-source-ceiling shore are

\[
 D(F)=\{\ell_v:v\in H\cup F\},\qquad
 C(S)=\{m_u:u\in H\cup S\}.                                  \tag{1.2}
\]

Both have size `18,646`.  Put an edge `ell_v -- u` exactly when
`ell_v proper-subset m_u`.

### Theorem 1.1 (inverse outer materialization)

`T` is the exact outer materialization of an origin-form parent with free
shore `F` and unoccupied-hard shore `S` if and only if the graph (1.2) has a
perfect matching.  Equivalently, for the fixed choice `(F,S)`,

\[
        |N(X)|\ge |X|\qquad\text{for every }X\subseteq D(F).   \tag{1.3}
\]

Given a perfect matching `sigma:D(F)->H union S`, the parent and outer
matching are canonical up to the choice of `sigma`:

* if `sigma(ell_v)=u`, put native bottom `ell_v` below `m_u subset r_u` at
  source row `u`;
* strip every `f in F` to the singleton root `r_f`;
* leave every row in `Q`, `A-F`, and `B-S` unchanged; and
* send source row `u=sigma(ell_v)` to receiver `v`, of kind `H` for `v in H`
  and kind `F` for `v in F`.

#### Proof

The lower targets in `D(F)` become the 18,646 native hard tokens.  The other
lower targets occur exactly once on the fixed rows `Q union (A-F)`.
Every middle and root is retained on its original row.  Thus the construction
is still an exact partition of all 65,535 nonempty rank-at-most-eight targets.
Containment on the matching edges makes its 18,646 source rows valid hard
chains.  The row counts are

\[
 \begin{split}
  \text{free}&=|F|=1748,\\
  \text{fixed length two}&=|A-F|+|B-S|=3114+785=3899,\\
  \text{singleton-soft}&=|Q|=17,\\
  \text{hard}&=|H|+|S|=16898+1748=18646.
 \end{split}                                                  \tag{1.4}
\]

Materialization puts each matched native bottom back at its row `v`, fills
all free receivers and exactly the hard receivers `H`, and leaves exactly
`S` unoccupied.  This reconstructs `T` row by row.

Conversely, take any origin-form parent and outer matching materializing
`T`.  Its singleton rows determine `F subseteq A`; its unoccupied hard rows
determine `S subseteq B`.  The 18,646 native hard bottoms are exactly
`D(F)`, and assigning each native token to its source row gives a bijection
to the hard source ceilings `H union S`.  Parent-chain containment gives
every edge of the required perfect matching.  Hall's theorem gives (1.3).
\(\square\)

### Corollary 1.2 (identity-core reduction)

There is a sufficient matching with no 18,646-row search.  Assign every
`ell_h`, `h in H`, to its own ceiling `m_h`; these 16,898 edges are legal
because `T` is a chain table.  It remains only to find a matching of size
1,748 in

\[
       G_{LR,MR}=(A,B;\ \ell_f\mathbin{\subsetneq}m_s).        \tag{1.5}
\]

For a prescribed short shore `S`, the exact reduced condition is

\[
  |N_A(X)|\ge |X|\qquad\text{for every }X\subseteq S.          \tag{1.6}
\]

If (1.6) holds and `F` is the set of matched `LR` rows, the identity edges
on `H` plus the reduced matching give the parent in Theorem 1.1.

This is sufficient, not necessary: a general perfect matching in (1.2) may
use nonidentity edges inside the 16,898-row core.

## 2. The selected-short reduced matching and `P*`

Let `S` be the 1,748 distinct `short_row` values of the frozen private
ticket list.  Every member of `S` is an `MR` row of `T^0`.  The exact reduced
graph from `S` to the 4,862 `LR` bottoms has

```text
vertices on selected short shore     1748
vertices on LR shore                  4862
containment edges                    75670
explicit matching                    1748
```

The explicit matching, not the matching algorithm, is the proof-bearing
certificate:

```text
scratch/k17_planted_b5_inverse_outer_parent_20260802/
  lr_to_selected_short_matching.tsv
SHA-256 09be3564882af8ffc7ae90f7f1b5ba0aaa9a7afc7bfb8a2e7e92b6aa71cfe1c1
```

It has 1,748 distinct rows on each shore, uses every member of `S`, and
checks `ell_f proper-subset m_s` edge by edge.  Therefore (1.6) holds by the
matching itself.

### Theorem 2.1 (exact new static parent)

Applying Corollary 1.2 gives the origin-form parent

```text
scratch/k17_planted_b5_inverse_outer_parent_20260802/inverse_parent.tsv
SHA-256 a146debfe42ef678b3ea64666f219504f8b26f77aec169724b3d8f3b5f268a12
```

with the census (0.2).  Its phase-zero outer matching is

```text
phase0_outer_matching.tsv
SHA-256 68a257ad1079e9e38bf3e3a0516056670d38d12a5332e73553c808c063babe7f
```

and has exactly

\[
     18646\text{ source tokens},\quad1748\ F\text{ receivers},
     \quad16898\ H\text{ receivers}.                          \tag{2.1}
\]

Materializing it reconstructs `T^0` byte for byte.

#### Proof

For each `h in H`, the parent retains native bottom `ell_h` at source row
`h` and the outer edge is the identity `h->h`.  For each reduced edge
`f--s`, the parent installs native bottom `ell_f` below the source ceiling
`m_s`, strips `f` to a free root, and uses the outer edge `s->f`.  Theorem
1.1 proves the construction.  The independent verifier reparses all targets,
checks the parent census, every containment edge, source/receiver uniqueness,
and exact rowwise rematerialization.  \(\square\)

This parent is new.  It is not `P1972`, and it does not reverse the proved
`P1972`-fibre exclusion.

## 3. One parent for both local `B_5` modes

Let `kappa` be the lower-location permutation

```text
(15351 16083 16227 15411 16087)
(2849 16218 16232).
```

Thus the phase-zero bottom at receiver `v` is at receiver `kappa(v)` in the
alternate local mode.  Its support consists of the eight moving hard `LMR`
rows.  It fixes `F`, `S`, every selected short, every selected endpoint host,
and every fixed soft endpoint.

### Theorem 3.1 (common-parent mode lift)

Put

\[
                            \mu^1=\kappa\mu^0.                 \tag{3.1}
\]

Then `mu^1` is a legal complete outer matching of the same parent `P*`, and
its exact materialization is the alternate planted table `T^1`.

```text
phase1_outer_matching.tsv
SHA-256 7087251433be0bf98766e3bc7212dcb00650ffbdd306a8dc0126914725ab246d

phase1_child.tsv
SHA-256 00f0dbe08f0229f135b5fb10109ba580f2d35c0cba584c5342a12923f56a381d
```

#### Proof

The source token and its bottom are unchanged.  If `mu^0(u)=v`, the
definition of `kappa` says that the same bottom is the phase-one lower at
`kappa(v)`.  Every moved receiver remains in the hard occupied shore, while
all free receivers are fixed.  The fixed middle/root suffix at `kappa(v)`
contains that phase-one bottom.  Hence (3.1) is a legal complete outer
matching.  Rowwise rematerialization gives `T^1`; the independent verifier
checks all 24,310 rows.  \(\square\)

This theorem closes the local outer-parent transport.  It says nothing about
changing the owner map to the other s7 phase.

## 4. Regenerated selected tickets

Keep from each old selected record

```text
short_row, q, alpha, beta, pred_host, succ_host
```

and keep the unique fixed-soft token `-1`.  At a real endpoint host `h`,
replace the old token label by the unique source token

\[
                         u^*(h)=(\mu^0)^{-1}(h).               \tag{4.1}
\]

In the identity-core construction every selected real endpoint belongs to
`H`, so

\[
                              u^*(h)=h.                        \tag{4.2}
\]

The regenerated ledger is

```text
regenerated_selected_tickets.tsv
SHA-256 cb2b0660c2d42f2351ef884ecf3148d7feac57214b311c3109886aeb563fdc2e
```

### Theorem 4.1 (two-mode static selected ledger)

The regenerated ledger has the following exact properties.

1. It contains 1,748 tickets, 1,748 distinct shorts, 3,496 distinct endpoint
   hosts, 3,495 distinct real source tokens, and one fixed-soft endpoint.
2. Every real token has its parent payload exactly at its named receiver,
   and all 3,495 edges are marked forced in both complete outer matchings.
3. All 1,748 tickets pass the canonical physical `P1--P2` five-cell replay
   on `P*`.  Their exact histograms are

   \[
   q7/q8=1365/383,
   \quad R=(498,0,104),                                \tag{4.3}
   \]

   with flag-pair counts

   ```text
   0/0 424, 1/0 498, 1/1 443, 2/2 150, 3/2 104, 3/3 129.
   ```
4. The same token labels, receiver rows, and physical ticket records are
   valid in `T^1`.  No phase-specific ticket ledger is required for the two
   local B5 modes.

#### Proof

The six non-token ticket fields are unchanged, so all short/host privacy
rows remain true.  Equation (4.1), source uniqueness of the outer matching,
and endpoint-host privacy give 3,495 distinct real tokens.  By construction,
the native bottom at `u^*(h)` equals the child lower at `h`, proving every
forced edge.

The independent physical verifier reconstructs the predecessor family, the
short physical family, the successor family, and five nonempty literal cells
for every ticket; all 1,748 replays pass and give (4.3).  Finally `kappa`
fixes every selected endpoint host.  Equation (3.1) therefore gives

\[
        (\mu^1)^{-1}(h)=(\mu^0)^{-1}(h)=u^*(h)                 \tag{4.4}
\]

for all 3,495 real endpoints.  The selected short and endpoint target rows
are also fixed between `T^0,T^1`, so the same five-cell records replay.
\(\square\)

The physical certificate is

```text
regenerated_physical_cells.tsv
SHA-256 0b4d5b1d48f85762c5aea7fe816ecc55208a37b976130d27910d04134e1a2185

regenerated_physical.audit.json
SHA-256 1dd0d9d1c4e6a9690bc84bf00b0bd938403335c5ec659cde7a1acca814389b48
```

This five-cell audit checks the five local boxes and exact inner/total covers
ticket by ticket.  It does not check global capacity-one cell or address
injectivity between different tickets, nor any propagated history.

### Corollary 4.2 (selected lower/source/address boundary is pointwise closed)

For every regenerated real ticket endpoint, the source label equals the
receiver row `h`, and

\[
 P^*[h].\operatorname{bottom}
   =T^0[h].\operatorname{bottom}
   =T^1[h].\operatorname{bottom}.                             \tag{4.5}
\]

Moreover the complete materialized row at `h` is fixed between the two local
modes.  Thus the optional same-number `Src` relation which caused the old
ten-row ambiguity is pointwise closed on this regenerated selected bank; it
carries no 109-row ambient sidecar.

This corollary is confined to the 3,495 selected ticket endpoints.  It does
not close module-internal lower/tail addresses or an aggregate history that
depends on other rows.

### Old and new ledgers must not be conflated

Only `572/3,495` old real token labels already equal the source selected by
this canonical new-parent matching.  The other `2,923` labels are genuinely
regenerated.  Therefore Theorem 4.1 is not a transport of the old retained
ticket TSV and makes no claim of membership in its old summary catalogue.
Its positivity comes from the fresh exact five-cell replay and forced outer
edges on `P*`.

## 5. What may now be called a regenerated parent

The tuple

\[
       (P^*,T^0,T^1,\mu^0,\mu^1,\mathcal T^*)                 \tag{5.1}
\]

is an unconditionally authenticated **static selected outer parent** for the
following represented rows:

* the complete 65,535-target partition and all 24,310 root/owner rows;
* the exact origin census (0.2);
* both 18,646-edge outer matchings and both exact child tables;
* all 1,748 local canonical ticket witnesses;
* all 3,495 real ticket token/source/receiver edges and the fixed-soft edge;
* all selected short/endpoint row privacy; and
* the local B5 equation `mu^1=kappa mu^0`.

Calling (5.1) a full selected-state or regenerative parent would assume the
remaining conclusion and is not justified.  The following rows remain
**UNPROVED** on (5.1).

1. A phase-specific reselection/rethreading of tickets under the two s7 owner
   maps.  The fixed regenerated ledger has the exact obstruction

   \[
   \begin{array}{c|rrrrrr}
   &\text{phase 0}&\text{phase 1}&\text{both}&\text{only 0}&
      \text{only 1}&\text{neither}\\ \hline
   \text{records}&520&501&332&188&169&1059.
   \end{array}                                                \tag{5.2}
   \]

   Thus that one ledger is not phase-common.  Equation (5.2) does not refute
   different witnesses in the two phases on one common structural host.
2. A selected `z=6` occurrence witness on the eight moving module slots,
   including the marked mutable topology and the full lower/tail actual-
   address transport.
3. Aggregate history, reset and directed chronology, residence, upper/source
   and common-cap rows, selected-state supplier rank `16898`, and every
   non-evicted compiler dependency.
4. A phase-common clone-good B5 bank, protected cross-core planting, and the
   all-depth regenerative recurrence.

The separately proved bare s7 endpoint aperture and the typed physical-root
seed may be composed with (5.1) only after items 1--3 are supplied on one
common dependency closure.  Hence this note proves no `B+1`, no
`B(k)+O(1)`, and no new bound on `nu(k)`.

## 6. Reproducible evidence

Constructor, exact matching, parent construction, two rematerializations,
ticket regeneration, and pin audit:

```text
scratch/audit_k17_planted_b5_inverse_outer_materialization_20260802.cpp
SHA-256 dc1d432c5b0291dcee1470e08b53fe10fdb576935b39913c204af5b781d839a2

scratch/k17_planted_b5_inverse_outer_parent_20260802/audit.json
SHA-256 91301356134f604634d7eff428d040c8470b004537cdb73c4cb30fe9b0af769f
```

Independent target-partition, reduced-matching, parent-census, outer-edge,
two-child, `kappa`, and regenerated-ticket replay:

```text
scratch/verify_k17_planted_b5_inverse_outer_materialization_independent_20260802.py
SHA-256 8e3905d97e62c22fb07725514a6ea27671b05753695d4d1d7dae111587ea6c27

scratch/k17_planted_b5_inverse_outer_parent_20260802/independent.audit.json
SHA-256 52b60ca8b3b15b24483ced8242cbf79b3f0b62a5100b193a82c308f22911adc2
```

Independent canonical five-cell replay source:

```text
scratch/k17_phase0_retained_witness_private_basis_20260802/
  verify_k17_phase0_private_bank_physical_p1p2_20260802.cpp
SHA-256 7947c32afc8609cd4da7de9759f79cd3aaf1c15b8d629f407a66971add5d9287
```

Independent regenerated-ledger replay under the two s7 owner maps, including
the overlap decomposition (5.2):

```text
scratch/audit_k17_planted_b5_regenerated_ticket_s7_owner_replay_20260802.py
SHA-256 7833b2bb82650bbd1cd223d05ae61a634e88f8181873df2dc80b85bcce1b0df7

scratch/k17_planted_b5_inverse_outer_parent_20260802/
  regenerated_s7_owner_phase_replay.independent.audit.json
SHA-256 04bb5a1e37acc647accaa71f452d74d3dbb176101b01e07b950b96e3fad8a29a
```

The earlier independently implemented owner replay gives the same marginal
counts `520/501`:

```text
scratch/audit_root_k17_constructed_common_basis_b5_host_independent_20260802.py
SHA-256 235a52f3ee0cd9783f91a3ca481eb2b02fd09f1f53186e686e21eb6a1b4ef28b
```

The all-`LR`/all-`MR` maximum-rank diagnostic printed by the constructor is
not used in any theorem above.  The proof-bearing positive is the explicit
1,748-edge selected-short matching and its independent edge-by-edge replay.
