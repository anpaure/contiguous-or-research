# K17 recoupled ROTS: exact-minimum-long frontier and one-short projection launch specification

**Date:** 2026-08-02  
**Status:** reconstruction and proof-safe model specification.  The frozen
positive statements below are independently replayed static/projection
facts.  The proposed `1S-ROTS` master has not been run and has no SAT or
UNSAT verdict.  It is a sufficient projection, not a physical chronology.
No residence, upper-shadow, source, topology, common-cap, compiler, or word
claim is made.

## 1. Live recoupled-table frontier

The authoritative input table has `24,310` owner/root rows and chain-length
histogram

\[
                    (x_1,x_2,x_3)=(1748,3899,18663).
\]

There are `18,646` eligible length-three donors.  A recoupling chooses, for
each singleton row `f`, a distinct donor `d` whose old bottom target is
contained in the root of `f`.  There are exactly `401,754` such pairs.  It
replaces

```text
f : (R_f)                 by (B_d,R_f),
d : (B_d,M_d,R_d)         by (M_d,R_d).
```

Thus every old target remains present exactly once.  Matching all `1,748`
singletons gives

\[
                    (x_1,x_2,x_3)=(0,7395,16915).
\]

This attains the counting minimum `x_3=16,915`, because
`x_3-x_1=16,915` for every depth-three partition of the fixed lower deck.
It also raises the potential short-role bank from `5,647` to `7,395`.

The best locally mirrored, independently replayed table is the builder
phase of `cegar2`.  Its exact hard-head projection is

```text
hard length-three heads                 16,898
long supplier--head pairs               42,216
length-two supplier--head pairs         29,229
total pairs                              71,445
zero hard heads                              77
maximum matching                        16,809
deficiency                                  89
canonical Hall shore                102 heads / 13 neighbours
```

The alternate owner phase has matching `16,734`, deficiency `164`, and
`141` zero heads.  A later remote generation-3 portfolio reached only
deficiency `92`, zero `78`; it is not an improvement over the independently
mirrored `cegar2` builder table.  Its exact scoped entry is

```text
/home/amodo/or15/work/ad_v5r_chain_recouple_019fc04bf4d7_20260802/
  out/portfolio_g3/seed0.builder.tsv
table SHA-256             393cccc1b662b038b3d89e2223de976840b92da0480e11026dd53ad5019c12b6
projection-audit SHA-256  4e0d6a0b71166374a9e01e847d7420e86137ac3962f0a5309d857491c30f47c7
Hall SHA-256              29ec23436f6c1df0973e8595d64e3c7250defd97f1c6bdc9ec2e1fa00faf9c90
```

The generation-3 result is an independently enumerated projection result,
not a separately mirrored full static-table replay.

These are union-over-address projections.  They do not choose one common
address/state per role and do not contain a cycle cover or typed reset
assignment.

## 2. Exact recoupling variables

Let `F` be the `1,748` old singleton rows, `D` the `18,646` eligible hard
donors, and `E_R` the `401,754` containment pairs.  The static choice is the
bipartite matching

\[
 x_{fd}\in\{0,1\},\qquad
 \sum_{d:fd\in E_R}x_{fd}=1\quad(f\in F),\qquad
 \sum_{f:fd\in E_R}x_{fd}\leq1\quad(d\in D).       \tag{2.1}
\]

Put `u_d=sum_f x_fd`.  A donor is long exactly when `u_d=0`; when
`u_d=1` it is a length-two short role.  Every `f` and every one of the
`3,899` old length-two rows is short.  The seventeen rank-one-bottom
length-three rows remain long but are not hard heads.

Equation (2.1), rather than a fixed reroute table, is the chain-allocation
part of the proposed joint master.  The first launch fixes the builder owner
phase, because it is the stronger authenticated projection.  An UNSAT result
there would not close the alternate phase; the two phases can be decided by
two separately scoped runs or by adding one global phase bit in a later
master.

## 3. The smallest typed-reset projection

The first useful exact target is the following deliberately restricted
projection, denoted `1S-ROTS(17)`.

1. Choose `x` satisfying (2.1).
2. Give each resulting long role one of the four literal long address flags

   \[
       12/1,\ 12/2,\ 23/2,\ 23/3,
   \]

   and each resulting length-two role one of its nine strict nested
   contiguous address flags.
3. A long--long arc is allowed only when the exact three-cell interval
   oracle accepts the selected two flags and the frozen owner.  Pointwise
   address drift then gives `alpha <= beta`.
4. A socket hyperarc

   \[
        (j,\alpha)\longrightarrow(s,q)\longrightarrow(i,\beta) \tag{3.1}
   \]

   is present only if **one common literal state of the short role** `s`, at
   address `q`, supports both transitions.  This is stronger than intersecting
   separate incoming and outgoing projections.  In the first master retain
   only downward/neutral sockets `beta <= alpha`.
5. Every long role has exactly one incoming and one outgoing contracted arc.
   Every one of the `7,395` short roles is used in exactly one hyperarc
   (3.1).  Consequently there are exactly `9,520` selected long--long arcs
   and `7,395` selected socket hyperarcs.
6. Every selected incidence at a role uses that role's single selected
   address flag.  Thus address flags cannot differ between its incoming and
   outgoing sides.

After contracting each short role, these equations give a directed cycle
cover on the `16,915` long roles.  Connectivity is intentionally omitted.
Long-only components, if any, are constant-flag.

The reset ledger needs no additional scalar relaxation.  On every directed
cycle, flag balance says that the upward cut load of selected long--long
arcs equals the cut load of the selected downward sockets.  Hence the three
threshold equations and `rho(D)<=7395` hold identically for every solution.
The model retains the physical socket type, rather than merely imposing
that scalar inequality.

This is the smallest projection which simultaneously tests all three new
rows:

* static chain recoupling;
* one address flag shared by both sides of each role; and
* a correlated, typed reset socket rather than separate endpoint marginals.

It is still only a projection.  A flag does not determine all overlap
letters of a long state.  A SAT result must therefore be followed by a
literal cyclic cell replay; failure of that replay is a valid CEGAR cut, not
a contradiction of the flag projection.

## 4. Exact equations for a fixed recoupling

For a frozen table, let `A_LL` be the accepted flag-labelled long--long
arcs and `A_S` the common-state socket records (3.1).  With binary variables
`e_a` and `r_b`, impose for every long role `v`

\[
 \sum_{a\in\delta^-_{LL}(v)}e_a+
 \sum_{b\in\delta^-_S(v)}r_b=1,
 \qquad
 \sum_{a\in\delta^+_{LL}(v)}e_a+
 \sum_{b\in\delta^+_S(v)}r_b=1,                    \tag{4.1}
\]

and for every short role `s`

\[
                         \sum_{b\ni s}r_b=1.          \tag{4.2}
\]

Standard implication clauses link each selected `e_a` or `r_b` to the
corresponding one-hot address variables.  Equations (4.1)--(4.2) are the
complete fixed-table `1S-ROTS` cycle-cover projection.

For a joint master, long--long records are disabled by `u_d` when either
endpoint donor was shortened; donor-short records are enabled by `u_d`;
and a free-row socket record carrying bottom `B_d` is enabled by `x_fd`.
The latter option family is the potentially large part and should be
generated lazily, not expanded as `9*401,754` state variables.

## 5. Size and exact CEGAR organization

The static outer layer has exactly

```text
recoupling choice bits              401,754
free-row exact-one rows               1,748
donor at-most-one rows                18,646
```

For one fixed table the address layer needs at most

```text
four-way long address literals       67,660
nine-way short address literals      66,555
total address literals              134,215
```

and the current fixed-table union projection has only `71,445` supplier--
hard-head row pairs.  The exact number of common-state socket triples is
not yet known for the recoupled table and must be the first fail-closed
census.  No estimate should be promoted as a theorem.

The proof-safe global organization is finite CEGAR:

1. the outer exact matching (2.1) proposes a recoupling table, seeded by
   `cegar2`;
2. the exact fixed-table oracle builds `A_LL,A_S` and decides
   (4.1)--(4.2);
3. on oracle UNSAT, the always-valid no-good

   \[
        \sum_{f\in F}x_{f,d_f^{\rm current}}\leq1747       \tag{5.1}
   \]

   excludes exactly that recoupling table;
4. smaller Hall/core cuts may replace (5.1) only after an independent
   dependency replay proves that changing rows outside the advertised halo
   cannot change the core;
5. on projection SAT, replay the emitted table, all selected flag masks,
   every common short state, degree equations, and the three reset cuts;
   then solve/replay the literal cyclic cell constraints.  Only the former
   earns `PASS_1S_ROTS_FLAG_PROJECTION`; the latter is needed for a physical
   nested-address chronology.

The no-good (5.1) makes the CEGAR logically complete, though not necessarily
fast.  A run stopped by time or memory is `UNKNOWN`.  An UNSAT verdict from
a released Hall halo is scoped to that halo unless a checkable proof covers
all `401,754` recoupling choices.

## 6. One-process H100 launch discipline

Use the unique persistent root

```text
/home/amodo/or15/work/k_rots_k17_joint_1s_20260802
```

and no `/dev/shm` output.  Before solving, the O3 C++ driver must:

1. authenticate every input hash listed below;
2. reconstruct the `401,754` recoupling pairs;
3. reproduce the frozen `cegar2` table and its `89`-defect projection;
4. census the exact common-state socket records and independently replay a
   deterministic sample with a per-coordinate oracle;
5. print variable/constraint counts and estimated memory, then fail closed
   if the configured cap would be exceeded.

Run one pinned CPU lane, `OMP_NUM_THREADS=1`, `nice -n 15`, with an explicit
wall timeout and an 8-GiB address-space cap.  Do not run a portfolio.  The
driver should keep outer matching, oracle, decode, and ledger in one serial
job.  The first job is explicitly the builder-owner phase.  Any timeout,
signal, malformed output, or resource failure is `UNKNOWN`.

No relevant recoupled/four-flag/ROTS process was active on H100 at the audit
poll.  The existing roots

```text
/home/amodo/or15/work/ad_v5r_chain_recouple_019fc04bf4d7_20260802
/home/amodo/or15/work/a_k17_fourflag_projection_20260802
/home/amodo/or15/work/k_fourflag_audit_20260802
```

are frozen/idle and must not be overwritten.

## 7. Frozen artifacts and hashes

The independently mirrored frontier is

```text
scratch/ad_k17_h1_res1972_minlong_recoupling_20260802/
```

with principal SHA-256 values

```text
original res1972 table
db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185

owner phase-pair table
fed8919d461ae2e4344ce6d4c8b05df1c4c1c7c7551d4d4b6638f3a02f23dd6b

cegar2 builder table
62d711033eabeaa3ab60da93327a0bc6181cc6ac80dbf11b6ce997e616780ad6

cegar2 reroutes
42009cc19bb3cf00fc74a0c008d96c40c435e4dc93a55765723c1585a3cd1082

cegar2 builder audit
f91b15aa83c4f19194322096243bec0756406e6d559e5e337151761c6f6f3342

independent static-table replay
1f0b2a9876b2fc6160efb59564a5a887d8931fe2bf5e1373f326ca30d1d4719d

independent dynamic projection source
56bbdfdbb6eff7a8680b877898ae2ba68f1ebe6d4856a963f0b17c337d3cd5a2

independent dynamic projection output
6aa2fd135371d7b9d3d7b47719cc2e47f39804d9c687822d35f29dd3e88f302c

Hall shore
e55b88af317f3241912a96ef08ff3397dd2cc0693c3dca460b01dd30043b5892

reference matching witness
029c9ce55c09d6784d8f246436da8a52899d1f8b58a782ef6efc7bae3b3c0575
```

The static builder source and the independent dynamic projection source are
different implementations.  Their scopes are also different: the builder
proves exact target preservation and minimum long count; the dynamic audit
proves only the union hard-head projection and its Hall shore.

## 8. Exact remaining finite row

The next certified milestone is not another random recoupling table.  It is
one of:

* `PASS_1S_ROTS_FLAG_PROJECTION` for a jointly selected recoupling/address/
  socket cycle cover, followed by literal cell replay; or
* a checkable UNSAT proof for a precisely declared recoupling fibre.

Even a literal `1S-ROTS` PASS would leave connectivity, residence, upper
decks, source chronology, common-cap, compiler, and the final word open.
