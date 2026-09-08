# K17 LLR escape: exact fixed-head flow, switch matching, and the state-hypermatching gate

**Date:** 2026-08-02  
**Status:** proof-safe static theorem and scoped replay audit.  The literal
`a=1` target/root counterexample is frozen.  No positive claim is made here
for the new socket DNFs, supplier rank, a common endpoint/state assignment,
or global chronology.

## 0. Verdict

The compressed-normal common-basis face is not the full no-singleton
depth-three face.  On the authenticated round-47 table, rows `8` and `172`
give the literal switch

\[
 (62,254,510)+(2110,2302)
 \longmapsto
 (254,510)+(62,2110,2302).                         \tag{0.1}
\]

It changes

\[
 (LLR,LMR,LR,MR)=(0,16915,4862,2533)
\]

to

\[
 (1,16914,4861,2534)                               \tag{0.2}
\]

without changing a target, row root, row owner, or the long/short
histogram.  This is an exact static counterexample to any unqualified claim
that the two-matroid common-basis representation covers all no-singleton
tables.

There are three different combinatorial scopes.

1. The bare-containment face with a fixed set of upper-low `LLR` targets is
   one integral bipartite flow and has a one-min-cut oracle.
2. Around a fixed compressed table, row-disjoint two-row switches of the
   form (0.1) are exactly a bipartite matching face, even after any
   **edge-local** socket filter.
3. A joint occurrence predicate on `(lower, upper-low, root, owner/state)` is
   a three-index column.  The generalized-size class of explicitly listed
   state-expanded catalogues contains perfect three-dimensional matching and
   is NP-hard.  This is not a complexity claim about the one fixed finite K17
   instance.  Shared endpoint histories, supplier tokens, or state cells
   therefore cannot in general be discarded as marginal edge labels.

For the particular switch (0.1), the repository contains no rank-generic
socket/supplier replay.  The current production pricers reject the table
before pricing because they require every length-three middle to have rank
seven.  The phase-0 private ticket bank is nevertheless preserved at the
static ticket/host layer and, after transporting the hard/fixed-short ground
sets, by one unforced outer-matching edge replacement.

## 1. The exact four-type path-cover formulation

Let

\[
 |L|=21777,\qquad |M|=19448,\qquad |R|=24310,
\]

where `L` contains the targets of ranks one through six, `M` the rank-seven
targets, and `R` the rank-eight receiver roots.  On strict-containment arcs,
write

\[
 g_{\ell u}\;(L\!\to L),\quad
 y_{\ell m}\;(L\!\to M),\quad
 d_{\ell r}\;(L\!\to R),\quad
 x_{mr}\;(M\!\to R).
\]

All four variable families are binary.

Require

\[
\begin{aligned}
 \sum_u g_{\ell u}+\sum_m y_{\ell m}+\sum_r d_{\ell r}&=1
       &&(\ell\in L),\\
 \sum_r x_{mr}&=1 &&(m\in M),\\
 \sum_\ell g_{\ell u}&\le 1 &&(u\in L),\\
 \sum_\ell y_{\ell m}&\le 1 &&(m\in M),\\
 \sum_\ell d_{\ell r}+\sum_m x_{mr}&=1 &&(r\in R),             \tag{1.1}
\end{aligned}
\]

and the length-three gate

\[
 \boxed{
 \sum_\ell g_{\ell u}
 +\sum_v g_{uv}+\sum_m y_{um}\le1
 }
 \qquad(u\in L).                                      \tag{1.2}
\]

### Theorem 1.1 (exactness)

Integral solutions of (1.1)--(1.2) are in bijection with target partitions
whose chain types are exactly `LLR`, `LMR`, `LR`, and `MR`.  If

\[
                         a=\sum_{\ell,u}g_{\ell u},             \tag{1.3}
\]

then the type counts are forced to be

\[
 \boxed{(a,16915-a,4862-a,2533+a).}                    \tag{1.4}
\]

In particular the arithmetic range is `0 <= a <= 4862`; existence for every
value in that range is not asserted.

#### Proof

Strict containment makes the selected directed graph acyclic.  Equations
(1.1) give each `L` and `M` target one successor, each root one predecessor,
and each possible internal receiver at most one predecessor.  If `u` has an
incoming `L-L` arc, (1.2) forbids an outgoing `L-L` or `L-M` arc, so its
unique successor is a root.  Thus no `L-L-M-R`, `L-L-L-R`, or longer chain
can occur.  Conversely each of the four declared chain types obeys
(1.1)--(1.2).

Every `M` has one root arc, so there are `19448` selected `M-R` arcs.
Consequently exactly `24310-19448=4862` selected arcs enter roots from `L`.
Each selected `L-L` arc creates one `LLR` head, hence there are `a` `LLR`
chains and `4862-a` direct `LR` chains.  Counting the `21777` outgoing `L`
arcs leaves

\[
 21777-a-4862=16915-a
\]

`L-M` arcs.  These are the `LMR` chains; the unused `M` receivers give
`19448-(16915-a)=2533+a` `MR` chains.  This proves (1.4).  The reverse map
selects the arcs of the chains.  \(\square\)

### Proposition 1.2 (the natural exact matrix is not TU)

The ungated path-cover constraints are bipartite flow constraints.  The
length gate (1.2) is load-bearing and destroys total unimodularity in the
natural formulation.  For

\[
 \ell_0\subsetneq\ell_1\subsetneq\ell_2
\]

take the columns `g01`, `g12`, and `g02` and the three rows (1.2).  Their
submatrix is

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},
 \qquad |\det|=2.                                      \tag{1.5}
\]

This proves only that the natural formulation is non-TU.  It does not prove
that bare Boolean-containment feasibility is NP-hard or rule out a larger
extended formulation.

## 2. Fixed upper-low heads give one exact flow and min-cut oracle

Fix `U subset L`, `|U|=a`, intended to be exactly the upper-low targets of
the `LLR` chains.  Split targets into source and receiver copies.  Let

\[
 S=L_{out}\mathbin{\dot\cup}M_{out},\qquad
 T=U_{in}\mathbin{\dot\cup}M_{in}\mathbin{\dot\cup}R.            \tag{2.1}
\]

Retain the following strict-containment arcs:

* `u_out -> R` for `u in U`;
* `l_out -> U_in union M_in union R` for `l in L minus U`;
* `m_out -> R` for `m in M`.

Every source, every receiver in `U`, and every root must be saturated;
receivers in `M` have capacity one.

### Theorem 2.1 (fixed-head flow equivalence)

This bipartite flow is feasible if and only if there is an exact four-type
table whose set of `LLR` heads is `U`.

#### Proof

A saturated `U` receiver has one lower predecessor and its source copy can
only enter a root, so it gives an `LLR` chain.  A source in `L minus U`
selects exactly one of an `LLR` head, an `M` receiver, or a root.  Every `M`
source enters a root.  Saturation and capacity therefore give precisely the
four chain types without target reuse.  Conversely, split the arcs of any
table having head set `U`; they satisfy these conditions.  \(\square\)

Add

\[
 q=|T|-|S|=2533+a                                      \tag{2.2}
\]

dummy sources, each adjacent to every `M_in` receiver.  The problem becomes
ordinary perfect bipartite matching.  The dummies occupy exactly the unused
`M` receivers.

### Corollary 2.2 (exact Hall/min-cut oracle)

For every `X subset S`, fixed-`U` feasibility is equivalent to

\[
 \boxed{
 |N_T(X)|\ge |X|,
 \qquad
 |N_{U\cup R}(X)|\ge |X|-(16915-a).
 }                                                       \tag{2.3}
\]

Equivalently, one max-flow/min-cut computation on the dummy-augmented
bipartite network decides the face and returns a deficient Hall set when it
fails.  Thus a proof-safe exact global architecture is:

1. branch on `U` (or generate head-set columns), and
2. use the integral fixed-`U` flow as recourse and (2.3) as the separation
   certificate.

Deleting pairwise arcs for a marginal socket predicate preserves this TU
recourse.  A joint predicate on both arcs of an `LLR` chain is not represented
by independent arc deletion and need not preserve this TU recourse.

## 3. The baseline-local switch face is bipartite matching

Fix a compressed-normal table.  Let `D` be its `LMR` rows

\[
 d=(\ell_d,m_d,r_d)
\]

and let `H` be its direct `LR` rows

\[
 h=(u_h,s_h).
\]

Build the bipartite switch graph `J subset D times H` with

\[
 d\sim h\quad\Longleftrightarrow\quad
                         \ell_d\subsetneq u_h.           \tag{3.1}
\]

Optionally retain an edge only if the complete two-row replacement has an
edge-local witness in every required transported phase.

### Theorem 3.1 (switch-matching theorem)

For an edge `dh`, replace

\[
 (\ell_d,m_d,r_d)+(u_h,s_h)
 \longmapsto
 (m_d,r_d)+(\ell_d,u_h,s_h).                             \tag{3.2}
\]

Simultaneously applicable row-disjoint switches of the declared form are in
exact bijection with matchings in `J`.  A matching of size `k` changes the
type ledger by

\[
                 k(+1,-1,-1,+1).                         \tag{3.3}
\]

Therefore maximum harvest, a prescribed value of `a`, additive switch
weights, Hall deficiency, and the Dulmage--Mendelsohn decomposition of this
baseline-local face are ordinary bipartite-matching questions.

#### Proof

All old containments in (3.2) are inherited; the only new containment is
(3.1).  The target multiset is preserved; the two roots and their owners
remain on their original rows.
Two switches can coexist precisely when they share neither donor row nor host
row, which is the matching condition.  Conversely every table produced by
this declared grammar identifies its used donor and host rows and hence the
corresponding matching.  \(\square\)

The existing static transfer audit reports `34,757` structural edges on the
`1,018` union-zero `LR` hosts and a matching saturating all `1,018`.  This is
calibration only: that audit explicitly excludes sockets, owners, supplier,
the protected bank, chronology, and the word.  Its audit hash is

```text
75596d0b1d4e45ce1efaaf4978c0f2d45f32e3dbade7ed721c0e63660d7df946
  scratch/root_k17_llr_short_transfer_matching_20260802/llr_short_transfer.audit.json
```

## 4. Why a one-shot matching gadget does not cover the full face

At one low target, collapse the relevant port classes to

* `p`: incoming `L-L`;
* `q`: outgoing internal `L-L` or `L-M`;
* `r`: outgoing root.

The exact local feasible sets are

\[
                \mathcal F=\{\{r\},\{q\},\{p,r\}\}.       \tag{4.1}
\]

They encode, respectively, a direct `LR` row, a lower tail, and an `LLR`
head.

### Proposition 4.1 (local delta-matroid obstruction)

`F` is not a delta-matroid.  Take `X={q}`, `Y={p,r}`, and `e=p`.  For every
`f in X triangle Y`, the candidate exchange is one of

\[
                 \{p,q\},\qquad\{p\},\qquad\{p,q,r\},
\]

none of which belongs to `F`.  Thus symmetric exchange fails.

Under the standard perfect-matching boundary semantics—every internal vertex
and every terminal not exposed externally must be covered—the feasible
exposed-terminal sets of a local matching gadget form, up to
complement/twist and minors, a graph matching delta-matroid.  Hence the exact
three-bit signature (4.1) has no such gadget.  This rules out the direct
strategy “replace every low target by this standard local gadget and run one
matching.”  It does not rule out nonlocal extensions, a projection using a
different boundary semantics, the fixed-head branching of Section 2, or
another polynomial algorithm.

## 5. The exact state-expanded complexity split

Suppose an `LLR` occurrence is admitted by a joint predicate

\[
             Q(\ell,u,r,\omega),                         \tag{5.1}
\]

where `omega` includes the owner, long flag, endpoint histories, common
phase, or supplier state.  Then choosing the incoming `L-L` edge and the
outgoing `L-R` edge independently is invalid.

### Theorem 5.1 (generalized explicit occurrence catalogues contain 3DM)

The generalized-size decision problem for exact cover by an explicitly
listed, polynomially verifiable catalogue of state-expanded `LLR` columns is
NP-complete, even with the remaining chain types forced through disjoint
private gadgets.

#### Proof

Given a three-dimensional matching instance

\[
                     \mathcal T\subseteq X\times Y\times Z,
 \qquad |X|=|Y|=|Z|=n,
\]

use `X` as lower-low tails, `Y` as upper-low heads, and `Z` as roots.  Take a
height-three containment instance in which every structural relation
`x<y<z` is present.  Give each allowed triple one fixed/private occurrence
state `omega`, and let the joint predicate `Q` retain exactly the columns
`(x,y,z)` in `T`.  Require `a=n`.  An exact chain cover is then exactly a
perfect three-dimensional matching.  For any fixed or explicitly padded
polynomially bounded nonnegative auxiliary counts `b,c,d`, add `b` isolated
one-column `LMR` gadgets, `c` isolated `LR` gadgets, and `d` isolated `MR`
gadgets, with no cross-catalogue columns.  Membership in NP follows from the
explicit polynomial catalogue and the assumed polynomial witness check.
\(\square\)

The usual four-column fractional obstruction is already present: the
columns `111`, `122`, `212`, and `221`, each at value one half, cover all six
endpoints fractionally, while no integral perfect cover exists.

This hardness theorem is deliberately scoped to an unbounded family of
arbitrary joint occurrence catalogues.  It is not a hardness theorem for
pure Boolean containment or for the one fixed K17 catalogue, and it does not
make Section 3's row-disjoint switch packing hard.  With fixed shores and a
factorized catalogue `E_XY` joined with `E_YZ`, an all-`LLR` perfect cover is
just one perfect matching on `X-Y` and one on `Y-Z`; the reduction needs
genuinely joint triple admissibility.  For Section 3, prepricing an entire
two-row switch merely deletes edges of `J`; matching remains exact as long as
the chosen witness uses no resource outside its two rows.  Shared endpoint
hosts, state cells, supplier tokens, or chronology footprints add further
resource incidences and lift the selection problem to set
packing/hypermatching or to a branch--Benders master with exact recourse.

## 6. Literal `a=1` switch on the transported phases

The authenticated transported rows are

| phase | row | owner | root | old targets | new targets |
|---|---:|---:|---:|---|---|
| 0 | 8 | 1022 | 510 | `62,254,510` | `254,510` |
| 0 | 172 | 18686 | 2302 | `2110,2302` | `62,2110,2302` |
| 1 | 8 | 1022 | 510 | `62,254,510` | `254,510` |
| 1 | 172 | 67838 | 2302 | `2110,2302` | `62,2110,2302` |

The exact masks obey

\[
 62\subsetneq2110\subsetneq2302,qquad
 254\subsetneq510,                                      \tag{6.1}
\]

and the unchanged owner increments are

\[
 1022\mathbin\triangle510=512,qquad
 18686\mathbin\triangle2302=16384,qquad
 67838\mathbin\triangle2302=65536.                      \tag{6.2}
\]

Thus target, root, and owner compatibility passes statically in both phases.
The phase-0 generalized table is frozen as

```text
e3956ccc091280b9091960adcc3f1d990606ed7bcf8c5b5a13078373ef16bda0
  scratch/audit_k17_corrected_recoupling_common_basis_agent_20260802/generalized_a1_LLR.table.tsv
```

The phase-1 row replacement follows identically from the transported table,
but no generalized phase-1 TSV has been materialized locally.

The switch preserves `16,915` long roles, `7,395` short roles, and `16,898`
hard long roles: old hard long row `8` is replaced by new hard long row `172`,
both with bottom `62` of rank five.

### 6.1 Exact socket/menu audit

The new `MR` short is row `8`, with bottom/root/owner

\[
                         (254,510,1022).                  \tag{6.3}
\]

It has two canonical `P1-P2` addresses and nine relaxed-nine addresses.  The
new `LLR` long is row `172`, with the four rank-generic long flags built from

\[
              (62,\;2110\setminus62,\;2302\setminus2110). \tag{6.4}
\]

This proves that both new rows have the expected marginal menus.  It does
**not** prove a common five-cell socket with predecessor and successor long
histories.

The old row `172` short had a positive relaxed-nine DNF in both transported
phases:

```text
phase 0: q=1, predecessor flag=0, successor flag=0,
         predecessor row=3339, successor row=194, owner=18686
phase 1: q=1, predecessor flag=0, successor flag=0,
         predecessor row=13206, successor row=194, owner=67838
```

Those records are stale after (0.1), because row `172` is now long and row
`8` is the new short.  Neither `all7395` DNF file contains a record for new
short row `8`, and no local artifact supplies a long-occurrence record for
the new `LLR` row.

The rank-generic independent coordinate-DP parser can represent (6.3)--(6.4)
and its five-cell feasibility test is rank-generic.  It is a verifier of
supplied summaries and role edges, however; the old summaries and edge files
are invalid after the long/short swap.  A rank-generic generator must first
rebuild the candidate predecessor/successor edges and then the verifier must
be run on each transported phase.

### 6.2 Supplier and common-state audit

The present production table reader and potential-socket pricer both throw
when a length-three middle is not rank seven.  The independent supplier
projection verifier likewise throws `bad long ranks` on (6.4).  Therefore:

\[
 \boxed{\text{supplier-rank survival is not replayed and is not frozen.}}
                                                               \tag{6.5}
\]

Equations (6.1)--(6.4) prove row-local owner/root and menu compatibility only.
They do not prove that row `8` has one exact common-phase socket, that row
`172` can occupy a required long history, or that their selected states agree
with shared neighboring endpoints.

### 6.3 Protected phase-0 private bank

The authenticated phase-0 bank contains `1,748` selected tickets and `3,496`
mutually distinct protected endpoint hosts.  In the role fields
`short_row`, `pred_host`, `pred_token`, `succ_host`, and `succ_token`, neither
row `8` nor row `172` occurs.  The physical-cell witness rows have the same
property.  Hence every selected private ticket and protected endpoint host
is literally untouched by (0.1).

The switch transports the outer-matching ground-set classes: row `8` leaves
the hard token and `H`-receiver copies, row `172` enters those copies, and the
fixed-short identity changes from row `172` to row `8`.  After this class
transport, the complete outer matching has exactly one affected key-field
edge, and it is unforced:

```text
8    62    H    8      254     0
```

Replace it by

```text
172  62    H    172    2110    0.                        (6.6)
```

No other matching edge uses token row or receiver row `172`, and
`62 subsetneq 2110`.  Thus, on the transported hard/fixed-short ground sets,
(6.6) gives an exact new outer matching by one edge replacement and leaves
all forced ticket edges and protected hosts unchanged.  The frozen verifier
for the old ground sets would not accept (6.6) without that class transport.
This freezes phase-0 private-bank survival at the ticket/host plus transported
static outer-matching layers.  It does not freeze a new physical socket,
supplier rank, or a phase-1 private bank; no transported phase-1 private-bank
artifact exists.

## 7. Physical derivative schedule

There is no marginal chronology prohibition against `LLR`.  The general
depth-`d` trace theorem permits every strict chain of length at most `d`, with
fixed ranks explicitly identified as an additional construction choice.  At
depth three, for `x in 62`, the new row `172` has the admissible trace

\[
\begin{aligned}
 B_3&=62,\\
 B_2&=2110\setminus62,\\
 B_1&=2302\setminus2110,\\
 B_0&=(O\setminus2302)\cup\{x\},                        \tag{7.1}
\end{aligned}
\]

where `O` is `18686` in phase zero and `67838` in phase one.  The last one,
two, and three cells have suffix unions `62`, `2110`, and `2302`.

What excludes this row today is compressed-normal software, not the physical
depth-three derivative grammar.  That software declares all ranks one
through six to be one antichain level and requires the middle of every long
row to be rank seven.  Global word chronology remains a separate Euler-trace
condition: one trace per row must share endpoints, balance, and form the
required connected trail.  Marginal trace (7.1) does not establish it.

## 8. Frozen claims and remaining exact test

The following are frozen.

1. The literal static `a=1` counterexample (0.1), including the transported
   phase-1 owner/root audit.
2. The exact four-type integer model (1.1)--(1.2) and forced ledger (1.4).
3. The fixed-head TU flow and Hall/min-cut oracle (2.3).
4. The baseline-local switch-matching theorem.
5. The local delta-matroid obstruction and the generic occurrence-catalogue
   3DM hardness theorem.
6. Phase-0 private ticket/host survival plus the one-edge static outer
   extension (6.6) on the transported ground sets.
7. Marginal physical depth-three legality of `LLR`.

The next proof-safe test is not a reuse of the old row-`172` DNF.  It is a
rank-generic two-phase rebuild with exactly these gates:

1. price new short row `8=(254,510)` against all admissible predecessor and
   successor long histories in each transported phase;
2. generate the four long flags for row `172=(62,2110,2302)` and rebuild all
   of its exact incident state arcs: four-cell long--long arcs and five-cell
   long--short incidences wherever applicable;
3. choose a socket occurrence for new short row `8` and a globally consistent
   incident state/arc for new long row `172`, respecting shared role addresses
   and protected endpoint exclusions;
4. replay the supplier projection/rank with rank-generic long intervals;
5. replay the private bank and (6.6), then the global Euler/chronology gate.

Until those five steps pass, the exact `a=1` object is a positive static
column and a valid physical chain type, but not a certified socket/supplier
solution.

## 9. Audited local inputs

```text
ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
  scratch/ad_k17_s7_carrier_adapter_20260802/out/round047.s7.phase0.tsv
736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
  scratch/ad_k17_s7_carrier_adapter_20260802/out/round047.s7.phase1.tsv
21d14d1c86b76a9ab2c45ea15c963ae9f113f8acd3563fcc7f2623f27cfba5a7
  scratch/k17_global_chain_recoupling_20260802/all7395.phase0.dnf.tsv
c83e24810027c4a3ebf3e0414522c6ca73e8431157c16726009ac5d305d6bda3
  scratch/k17_global_chain_recoupling_20260802/all7395.phase1.dnf.tsv
d02e01d0e56beec82633b280bf9011760c273a31994431bd62db52c3662d0ef1
  scratch/k17_phase0_retained_witness_private_basis_20260802/selected_tickets.tsv
465d8813600ffc12ba3383a86f7cddf07dcaa6cc7af19d23172825a0a8247062
  scratch/k17_phase0_retained_witness_private_basis_20260802/physical_cells.tsv
179270d1d01f6c14a7b47b5eb390e634aca33ac16e5ec82d54a93b589b8d850e
  scratch/k17_phase0_retained_witness_private_basis_20260802/complete_outer_matching.tsv
```
