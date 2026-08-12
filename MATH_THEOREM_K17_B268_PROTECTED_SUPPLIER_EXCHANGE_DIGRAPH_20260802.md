# K17 `b268` protected supplier exchange digraph and nested-Hall ladder

**Date:** 2026-08-02  
**Status:** exact finite audit of the authoritative protected 438-transfer
prefix from supplier deficiency `96` through `90`, the strict-Pareto
`def85 -> def84` release/compensation exchange, and a general fixed-table
exchange theorem.  The authoritative analysis parent is now `def84`, table
SHA-256 `3171bf38...`.  No radius search or solver was launched in this lane.
The independently materialized `def91` and `def90` artifacts are byte-equal
to their root-owned H100 counterparts.

## 1. Frozen scope and literal evidence

The parent is the materialized `b268` table

```text
b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    private_h_outer_materialized.tsv
```

The protected transfer catalogue and ticket ledger are

```text
30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
  scratch/q1_k17_b268_llr_common464_20260802/
    b268_llr.protected.all_edges.tsv

d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/
    selected_tickets.tsv
```

The union of its `short_row`, `pred_host`, `pred_token`, `succ_host`, and
`succ_token` addresses, excluding the sentinel `-1`, has exactly `7,213`
physical rows.  Every table in the audited chain agrees byte-for-byte with
`b268` on all of them.

The two socket columns have different semantics:

* phase 0 is the literal `b268` owner phase;
* phase 1 is the root-aligned transported `round047.s7` owner marginal.

The latter is not an authenticated carrier history.  All socket statements
below are complete rowwise marginal DNF replays at those two declared phases.

## 2. Exact seven-state ledger

All states contain exactly `438` row-disjoint protected transfers and have
the invariant table histogram `[0,7395,16915]`.  The four socket coordinates
are `(p0,p1,both,either)`.

| state | table SHA-256 | supplier edges | rank / 16898 | deficiency | zero heads | Hall `Q/B` | sockets |
|---|---|---:|---:|---:|---:|---:|---:|
| `def96` | `7206ab1c9f3763aa0cfad7e88516753142d2bbbb858627b45fa3f49dee514655` | 74121 | 16802 | 96 | 81 | 110/14 | 3098/2253/1839/3512 |
| `def95` | `ae44aebdae38c0ca5cb5d76ab2a6a305a67b52f17b4e395a3aedbd3d97300374` | 74129 | 16803 | 95 | 80 | 109/14 | 3098/2253/1839/3512 |
| `def94` | `2372971ac55737a5df73d3f6f2e2548a6da8d1e7500eda26412f41d32e8658f9` | 74135 | 16804 | 94 | 79 | 108/14 | 3099/2254/1840/3513 |
| `def93` | `eaa079432173f87803992bd47d97a67533f93f18ffc89fb779920f2f0a390329` | 74146 | 16805 | 93 | 78 | 107/14 | 3099/2255/1840/3514 |
| `def92` | `6892f589839d076bdca8dd2aaf789f5169cc09083455fe6fc4e9c8eb136ef3d0` | 74152 | 16806 | 92 | 77 | 106/14 | 3099/2255/1840/3514 |
| `def91` | `cc1be2af0ca1ebd800ad5e15cabcdb52d27e1dd99c2ba7711c02f751e29d6478` | 74162 | 16807 | 91 | 76 | 105/14 | 3099/2255/1840/3514 |
| `def90` | `20087349f4f47183f6dd1ab810041635d02d9f6b0f6f51c97221d026276a5bc6` | 74174 | 16808 | 90 | 76 | 104/14 | 3099/2255/1840/3514 |

Thus all four socket coordinates are weakly nondecreasing.  Notice that the
last supplier improvement does **not** reduce the zero-head count.

The root-owned terminal paths, hashes, and local byte-equal names are frozen
in

```text
scratch/audit_k17_b268_supplier_exchange_theorem_20260802/
  root_terminal_bindings.tsv.
```

### Authoritative rebase: strict `def85 -> def84`

The later strict-Pareto predecessor and current parent are

| state | selected SHA-256 | table SHA-256 | projection SHA-256 | edges | rank / 16898 | zero | Hall `Q/B` | sockets |
|---|---|---|---|---:|---:|---:|---:|---:|
| `def85` | `0fb9a812e0afd7e9590d6ba690d2c3d7bee3f15a9462e3236b784a17de48b59f` | `ea0e8803b666dd51e4e5b073e50938ca5c508f3c2d7066f04ec2a0bd9f083aa8` | `038739aa6dad705ce48ac0aee0fba80d3eacd858dcf9c7de8a255e44a4460637` | 74195 | 16813 | 72 | 98/13 | 3102/2259/1843/3518 |
| `def84` | `c490cc49aef575caae9f72d478ff08320f24a3625593f2465f9b94fb7d8ce979` | `3171bf380c3a139313f1304bb1d821810cb7402c20aa99f01ab8ccdc189854f1` | `7f2dc7ae146ae6a706a2399326b293809f7ae62d34a89ac393a2301a357dab05` | 74200 | 16814 | 71 | 98/14 | 3102/2260/1844/3518 |

The deterministic exchange is `remove 32175 / add 36629`.  It preserves
`p0` and `either`, raises `p1`, `both`, and supplier rank by one, and leaves
all `7,213` protected rows unchanged.  It supersedes the earlier generic
deficiency-84 branch whose socket tuple regressed.  Every next-step oracle or
candidate claim must now be hash-bound to table `3171bf38...`; results tied
to another deficiency-84 table are not evidence about this parent.

The root freeze and its byte-identical local mirror are

```text
/home/amodo/or15/work/root_k17_b268_llr_release_oracle_20260802/
  def84_pareto_remove32175_add36629/

scratch/q1_k17_b268_llr_release_theorem_20260802/
  def84_pareto_remove32175_add36629/
```

The older files `b268_llr_def84_release_oracle.*` and
`predicted_def83_from84_remove32175_add8443.*` in the parent release-theorem
directory belong to the superseded deficiency-84 branch.  They attempt to
release edge `32175`, whereas canonical selection `c490cc49...` already
removed that edge and instead contains `36629`.  They are historical
artifacts, not current-parent continuation certificates.

## 3. Literal action of a one-for-one transfer exchange

A protected catalogue edge has a current LR host `a`, an LMR donor `d`, and
a lower target `ell`.  Selecting it performs

\[
 a:(u<q)\longmapsto(\ell<u<q),\qquad
 d:(\ell<m<r)\longmapsto(m<r).                         \tag{3.1}
\]

For a selected set `F`, a replacement `F-f+e` is structurally admissible
exactly when the added edge `e` is disjoint from `F-{f}`.  In all seven
audited steps the dropped and added edges have four distinct endpoints.  Hence their
transfer-graph symmetric difference is two disconnected singleton edges,
while the materialized table changes exactly four rows:

1. the dropped edge's LLR host returns to its parent LR short state;
2. its MR donor returns to its parent LMR head state;
3. the added edge's LMR donor becomes a new MR short row; and
4. its LR host becomes a new LLR head.

The exact row supports of the earlier six-step prefix are

| move | restored LR | reactivated LMR | new MR short | new LLR head |
|---|---:|---:|---:|---:|
| `41 -> 89826` | 49 | 136 | 9998 | 23929 |
| `311 -> 89202` | 293 | 627 | 19468 | 23849 |
| `659 -> 88917` | 501 | 554 | 627 | 23805 |
| `756 -> 88472` | 512 | 13720 | 136 | 23725 |
| `1792 -> 88113` | 1041 | 4045 | 23287 | 23665 |
| `1952 -> 81624` | 1301 | 2048 | 13333 | 22687 |

This is the first important separation: the transfer replacement is not the
supplier augmenting path.  The latter lives in a different bipartite graph.

## 4. The literal supplier graph

For a materialized table `T_F`, let

\[
 G_F=(U,A_F;E_F)                                           \tag{4.1}
\]

be the complete generalized `6/9/4` row-pair projection.

* `U` consists of all `24,310` physical rows in their current table states.
* `A_F` consists of length-three rows whose first target has rank greater
  than one.
* `(u,a)` lies in `E_F` precisely when the complete flag compatibility
  predicate returns a nonzero `flag_pair_mask`.

Every transfer relocates one lower target from one length-three row to one
length-two row.  Consequently

\[
                         |A_F|=K=16898                     \tag{4.2}
\]

throughout this face.  Hall's deficiency theorem gives

\[
 \delta(F)=K-\nu(G_F)
   =\max_{X\subseteq A_F}\bigl(|X|-|N_F(X)|\bigr).         \tag{4.3}
\]

## 5. Exchange-surplus theorem

Let `M` be any maximum matching of `G_F`, and materialize one structurally
admissible successor `F'`.  Delete from `M` every pair whose head is no
longer active or whose literal compatibility mask is zero in `G_{F'}`.  Put

\[
 M^\circ=M\cap E_{F'},\qquad
 \ell=|M|-|M^\circ|.                                      \tag{5.1}
\]

Let `alpha` be the maximum number of additional integral matching edges
obtainable by augmenting \(M^\circ\) in \(G_{F'}\).  Equivalently,

\[
 \alpha=\nu(G_{F'})-|M^\circ|.                            \tag{5.2}
\]

### Theorem 5.1 (exact rank-update invariant)

\[
 \boxed{\delta(F')=\delta(F)+\ell-\alpha.}                \tag{5.3}
\]

Therefore a swap is strictly supplier-improving if and only if
`alpha >= ell+1`; it improves by exactly one if and only if
`alpha = ell+1`.

#### Proof

The surviving set \(M^\circ\) is a matching of \(G_{F'}\) of size
\(\nu(G_F)-\ell\).  Berge augmentation from it gives

\[
 \nu(G_{F'})=|M^\circ|+\alpha
             =\nu(G_F)-\ell+\alpha.
\]

Subtract from the invariant head census \(K\).  This proves (5.3).  The
individual numbers \(\ell\) and \(\alpha\) may depend on the chosen old
maximum matching, but their difference is the invariant rank change.
\(\square\)

The successor supplier exchange digraph orients

* every nonmatching incidence `head -> supplier`; and
* every edge of the current matching `supplier -> head`.

A directed path from an unmatched head to an unmatched supplier is an
augmenting path.  After each flip the orientations are updated.  Counting
these flips until no path remains computes `alpha`.

## 6. The six restored-row certificates

The row restored by deleting the old transfer supplies the peeled Hall head
in every step.  It is never the new MR short donor created by the added
transfer.

| step | restored short row and state change | former deficient head | head degree | new mask | `(ell,alpha)` |
|---|---|---:|---:|---:|---:|
| `96 -> 95` | `49: [1,1139,1271] -> [1139,1271]` | 6579 | 0 -> 1 | 136 | (2,3) |
| `95 -> 94` | `293: [1030,3111,3247] -> [3111,3247]` | 305 | 0 -> 1 | 136 | (2,3) |
| `94 -> 93` | `501: [4149,4157,4349] -> [4157,4349]` | 519 | 0 -> 1 | 50 | (4,5) |
| `93 -> 92` | `512: [4259,4275,4535] -> [4275,4535]` | 540 | 0 -> 1 | 16908800 | (3,4) |
| `92 -> 91` | `1041: [5185,5191,7247] -> [5191,7247]` | 1046 | 0 -> 1 | 263168 | (3,4) |
| `91 -> 90` | `1301: [8204,8478,8574] -> [8478,8574]` | 1316 | 1 -> 2 | 1073741892 | (3,4) |

For the first five rows, the displayed restored row is the head's sole
successor supplier.  For the sixth, head `1316` already had sole supplier
`1307`; its successor supplier set is `{1307,1301}`.  Head `1386` also had
sole old supplier `1307`.  The distinguished augmentation is therefore

```text
H1386 -new- S1307 -old- H1316 -new- S1301,
```

which assigns `1307 -> 1386` and the restored row `1301 -> 1316`.  Neither
head was isolated, so a zero-head-only release oracle misses this valid
improvement.

The old matching is not generally a successor matching.  The six swaps
invalidate respectively `2,2,4,3,3,3` old pairs.  The complete successor
certificates contain `3,3,5,4,4,4` augmenting components relative to the
surviving old submatching.  Thus every step repairs every loss and has one
augmentation left over:

\[
                         \alpha-\ell=1.                    \tag{6.1}
\]

The exact invalid pairs, all augmenting components, and every literal flag
mask are frozen in `exchange_chain.matching_losses.tsv` and
`exchange_chain.augmenting_components.tsv`.

## 7. Hall-shore motifs

### 7.1 The earlier head-peeling prefix

The canonical neighbour set is identical in all seven Hall certificates:

\[
\begin{split}
B=\{&1307,2562,5895,6063,6448,6560,8183,9945,12973,\\
    &13581,14128,14639,16803,20737\}.                      \tag{7.1}
\end{split}
\]

If `Q_d` denotes the displayed deficiency-`d` Hall head set, then

\[
 Q_{d-1}=Q_d\setminus\{q_d\},\qquad
 N(Q_{d-1})=B,                                             \tag{7.2}
\]

where

```text
q_96=6579, q_95=305, q_94=519,
q_93=540,  q_92=1046, q_91=1316.
```

The restored row `r_d` is outside `B` and becomes a new neighbour of
`q_d`.  Hence the old shore has successor neighbourhood
\(B\cup\{r_d\}\)
and signed Hall repair one, while the peeled shore still witnesses
deficiency `d-1`.

### Proposition 7.1 (certified one-unit Hall peel)

Suppose a deficiency-`d` state has a maximum shore `(Q,B)`.  A successor is
an exact one-unit improvement if it has

\[
 Q'=Q\setminus\{q\},\quad N_{F'}(Q')=B,\quad
 r\notin B,\quad (r,q)\in E_{F'},                          \tag{7.3}
\]

and contains at least `ell+1` augmentations from the surviving old matching.

#### Proof

The `ell+1` augmentations and Theorem 5.1 give
`delta(F') <= d-1`.  The shore `Q'` has
`|Q'|-|B|=d-1`, so Hall gives `delta(F') >= d-1`.  Equality follows.
\(\square\)

This proposition captures both motifs in the table: singleton zero-head
activation and release of a nonzero head from a shared-neighbour bottleneck.

### 7.2 The authoritative `def85 -> def84` bank expansion

The current rebase is not a head peel.  Its four literal row changes are

```text
12586  LLR(29697,62465,62475) -> LR(62465,62475)
24210  MR(95235,128003)       -> LMR(29697,95235,128003)
13716  LR(69795,70055)        -> LLR(4259,69795,70055)
13720  LMR(4259,69811,70067)  -> MR(69811,70067).
```

The Hall head set remains the same `98` rows.  Its supplier bank changes from

\[
 B_{85}=\{1307,5895,6063,6448,6560,8183,9945,12973,13581,
          14128,14639,16803,20737\}                       \tag{7.4}
\]

to

\[
                         B_{84}=B_{85}\cup\{12586\}.       \tag{7.5}
\]

Restored LR row `12586` creates two incidences into the old shore:

| head | old suppliers | successor suppliers | new mask | role in certificate |
|---:|---|---|---:|---|
| 9327 | `{5895}` | `{5895,12586}` | 136 | matched to restored row |
| 12592 | empty | `{12586}` | 16908800 | ceases to be zero but remains unmatched |

Thus the zero set loses `12592`, but the actual net augmenting component is

```text
H9327 -new(136)- S12586.
```

The old maximum matching loses exactly

```text
S9333  -> H12586
S13672 -> H13720,
```

because both old heads become short.  Relative to the surviving old
matching, the successor has three positive augmenting components:

```text
H9327  -N136- S12586

H13716 -N136- S13692 -O536870963- H13706 -N136- S506
       -O50- H570 -N8- S534 -O2- H84 -N8- S716

H24210 -N64- S12605.
```

Therefore \(\ell=2\), \(\alpha=3\), and

\[
 \delta_{84}=85+2-3=84.                                  \tag{7.6}
\]

The restored row adds two shore edges but only one new supplier identity.
Hall accounting must count the OR-neighbour bank, not raw incidences.

### Proposition 7.2 (unified nested-shore certificate)

Let `(Q,B)` be an old maximum shore of deficiency `d`.  Suppose a successor
has a Hall witness `(Q',B')` with

\[
 Q'\subseteq Q,\qquad B\subseteq B',\qquad
 \rho=(|Q|-|Q'|)+(|B'|-|B|).                              \tag{7.7}
\]

If its exchange surplus satisfies

\[
                         \alpha-\ell\ge\rho,               \tag{7.8}
\]

then its deficiency is exactly `d-rho`.

#### Proof

Theorem 5.1 gives \(\delta'\le d-\rho\).  The successor shore has

\[
 |Q'|-|B'|=|Q|-|B|-\rho=d-\rho,
\]

so Hall gives the reverse inequality.  \(\square\)

The six earlier swaps have `(head loss, bank gain)=(1,0)`.  The current
`def85 -> def84` rebase has `(0,1)`.  Both are exact one-unit instances of
Proposition 7.2, certified independently by `alpha-ell=1`.

## 8. Radius-one algorithm and continuation criterion

There are two graphs and they must not be conflated.

1. **Transfer exchange graph.**  Its left vertices are selected drops
   `f in F`, its right vertices are unselected additions `e`, and an arc
   `f -> e` exists when `e` is disjoint from `F-{f}`.
2. **Supplier alternating digraph.**  It is constructed only after the
   candidate table is materialized.  Its augmenting surplus is
   `sigma(f,e)=alpha-ell`.

Protection and socket conditions are separate exchange-arc filters.  The
exact radius-one audit is:

```text
for every structurally admissible drop/add arc:
    materialize the four changed table rows
    validate the target partition and all 7,213 protected rows
    replay the complete phasewise DNF socket sets if socket floors are imposed
    keep the literally surviving part M° of the incumbent maximum matching
    augment M° to maximum in the successor supplier graph
    accept exactly when alpha - ell >= 1
    rebuild a maximum Hall shore before the next step
```

For the live continuation, `F`, `M`, the Hall shore, socket baseline, and
selected-transfer membership in this algorithm are those of authoritative
`def84` (`3171bf38...`, `9c8d62b...`, `2661fbee...`,
`3102/2260/1844/3518`, `c490cc49...`).  They must not be inherited from the
superseded generic deficiency-84 branch.

Equivalently, every candidate arc has exact weight

\[
                         \sigma(f,e)=\alpha-\ell.           \tag{8.1}
\]

Positive arcs are precisely the supplier-rank-improving radius-one
exchanges.  A cheap necessary filter is that every incumbent
maximum-deficiency Hall shore receives signed repair at least one.  One
shore is not sufficient: another shore may retain deficiency `d`, and
changed source/head modes may destroy old matching edges.  The complete
augmentation or min-cut replay remains necessary.

### Corollary 8.1 (sufficient continuation to deficiency zero)

Let the admissible state space consist of protected 438-transfer tables
satisfying the requested socket constraints.  If every reachable state with
positive supplier deficiency has a radius-one exchange arc with

\[
                         \sigma(f,e)\ge1,                  \tag{8.2}
\]

then repeated exact acceptance reaches deficiency zero in at most the
current deficiency many steps.

This is the sharp monotone radius-one accessibility condition.  This note
verifies it on the six-step prefix `96 -> ... -> 90` and independently on the
current `85 -> 84` rebase.  It does **not** infer the intervening root descent
or prove that a positive arc exists at every state below `84`.  Failure at
one state would rule out only monotone radius-one continuation from that
state, not a plateau, temporarily worsening move, or balanced multi-swap
path.

## 9. Projection closure is not occurrence or chronology closure

The exact statements above stop at the static complete `6/9/4` projection.
A nonzero `flag_pair_mask` is an existential OR over compatible source/head
flag pairs.  Even deficiency zero would prove only that every hard head can
be assigned a distinct physical supplier identity in this union graph.

It would not prove any of the following:

* one common occurrence-labelled flag/history selection;
* that the phase-0 and transported-phase-1 socket witnesses are the same
  occurrence;
* that transported phase 1 belongs to the same authenticated carrier;
* a residual private outer matching or state-balanced circulation;
* residence, endpoint/demand disjointness, upper containment, or common cap;
* chronology, cyclic-cell replay, compiler closure, or a K17 word.

Likewise, byte identity of the `7,213` protected table rows is a physical
footprint theorem.  It does not assert simultaneous realization of their
ticket witnesses.  The augmenting paths in this note are matching
reassignment certificates, not temporal paths.

## 10. Reproducible artifacts

All lane-owned outputs are under

```text
scratch/audit_k17_b268_supplier_exchange_theorem_20260802/
```

The load-bearing files are

```text
materialize_reported_chain.cpp         deterministic def91/def90 materializer
audit_exchange_chain.cpp               literal matching/Hall exchange auditor
chain_inputs.tsv                        seven-state input/provenance ledger
def85_def84_inputs.tsv                  authoritative current-rebase ledger
def84_rebase_quarantine.tsv             superseded-parent artifact quarantine
root_terminal_bindings.tsv              root/local terminal hash bindings
reported_terminal_materialization.tsv   four-row and 7,213-row checks
exchange_chain.steps.tsv                 rank-update and Hall-difference ledger
exchange_chain.restored_incidences.tsv   restored row/head degree census
exchange_chain.matching_losses.tsv       invalidated old matching pairs
exchange_chain.augmenting_components.tsv all positive alternating components
def85_def84_exchange.steps.tsv           current rebase rank/Hall ledger
def85_def84_exchange.restored_incidences.tsv current restored-row incidences
def85_def84_exchange.matching_losses.tsv current invalidated matching pairs
def85_def84_exchange.augmenting_components.tsv current augmenting components
```

The source auditors materialize fixed reported tables and audit fixed
supplier graphs.  They do not enumerate radius candidates, launch SAT/CP,
or write into any root-owned radius path.
