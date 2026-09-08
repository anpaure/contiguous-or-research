# `k=17`: exact rooted-flag palette-switch basis and support-one/support-two repairs of the first dead root

Date: 2026-08-01  
Lane: A / residence-first rooted age partitions  
Status: exact general switch formulation and independently replayed local
repairs of the explicit root-0 singleton obstruction; no global
1,430-state transversal claim

## 1. Verdict

The correct palette-preserving local object is a circuit of one resource
incidence matrix.  In particular, rank-six targets emitted as `C0` and as
`C0 union C1` must use the **same** resource coordinates; treating the two
stages as different palettes would admit false switches.

For the frozen rooted certificate of SHA `ad9e15...`, root 0 is rigid when
its own row is the only changed row.  This does **not** make its zero-out
obstruction globally support-two-minimal.  The remote one-row phase pivot

```text
row 331, Q=0x010df, fixed type1 and B=0x0109f:
  old (C0,C1,C2)=(0x00001,0x0109e,0x00040)
  new (C0,C1,C2)=(0x01000,0x0009f,0x00040)
```

preserves every resource row, adds exactly the turns `0->331` and
`331->409`, removes none, and changes

```text
root turns / zero-out / zero-in / support matching
  912 / 761 / 848 / 530
to
  914 / 759 / 847 / 531.
```

There is also the following exact two-row switch, which preserves all
roots, all lower target orbits, and all nine type masses:

```text
row 0,   Q=0x000ff:
  old type8 (C0,C1,C2)=(0x0009f,0x00040,0x00020)
  new type1 (C0,C1,C2)=(0x00040,0x0009f,0x00020)

row 330, Q=0x010bf:
  old type1 (C0,C1,C2)=(0x00001,0x000be,0x01000)
  new type8 (C0,C1,C2)=(0x0009f,0x00020,0x01000).
```

It changes the fixed-table transition census from

```text
root turns / zero-out / zero-in = 912 / 761 / 848
```

to

```text
root turns / zero-out / zero-in = 914 / 757 / 847.
```

Root 0 changes from out/in degree `0/3` to `1/1`; row 330 has degree
`1/3` afterward.  The root-support maximum matching also rises from
`530` to `531`.  This is a genuine positive compound repair witness, not a
cycle cover and not a global support-minimality claim.

## 2. The exact resource matrix

Write a rooted literal flag as

\[
             f=(Q,t,A,B),\qquad A=C_0\subset B=C_0\cup C_1\subset Q.
\]

For each root `Q`, type `t`, and tight necklace target `(s,[S])`, introduce
one resource coordinate.  Define

\[
 r(f)=e_Q+e_t+e_{(|B|,[B])}
       +{\mathbf 1}_{|A|\ge2}e_{(|A|,[A])}.              \tag{2.1}
\]

There is no rank-one resource: the singleton suffixes of types 0 and 1 are
slack.  Crucially, (2.1) has only one coordinate for a given pair
`(s,[S])`; it does not remember whether that target occurred as `A` or
`B`.

### Theorem 2.1 (switch iff)

Let `F` be a feasible rooted certificate.  Delete flags
`f_1,...,f_k` on distinct roots and put flags `g_1,...,g_k` on exactly
those roots.  The replacement preserves every root, every type mass, and
one occurrence of every tight lower target if and only if

\[
                 \sum_{i=1}^k r(f_i)=\sum_{i=1}^k r(g_i).       \tag{2.2}
\]

Every primitive palette-preserving move is therefore a circuit of the
integer matrix whose columns are the vectors `r(f)`.  Conversely every
applicable signed circuit is a literal palette-preserving switch.

#### Proof

Every coordinate of (2.1) is exactly one defining equality of the static
factor: one flag per root, the nine type totals, and exact cover of every
tight target.  Equality (2.2) is consequently necessary.  If (2.2) holds,
the deleted and inserted multisets have identical load in every defining
row; literal containment of each inserted column makes the replacement a
valid partition.  Hence it is sufficient.  Minimal nonzero kernel vectors
are precisely the circuits.  \(\square\)

This is the exact pre-SAT formulation.  A search may enumerate literal flag
columns, bucket them by `r(f)-r(f_Q^0)`, and pair opposite buckets for all
support-two moves.  Larger switches are zero-sum circuit combinations.
There is no claim that two-by-two moves connect the whole fibre: containment
structural zeros can force longer circuits.

The raw matrix is not totally unimodular.  Restrict its rows to the root
`Q=0x000ff`, rank-two orbit `[A]` with `A=0x00003`, and rank-seven orbit
`[B]` with `B=0x0007f`.  The three valid type-2 columns

```text
A  subset 0x000bf subset Q,
0x00005 subset B  subset Q,
A  subset B       subset Q'=0x0017f
```

restrict respectively to

\[
                  (1,1,0)^T,\quad(1,0,1)^T,\quad(0,1,1)^T.
\]

Their determinant is `-2`.  Thus ordinary exact-cover LP integrality cannot
replace the circuit or extended matching formulation.

## 3. Two useful matching subfibres

Fix the type and inner set `A_i` at every root.  For `b=6,7`, form a
bipartite multigraph between the roots having an outer rank-`b` slot and the
rank-`b` necklace targets.  An edge is a literal occurrence

\[
                 A_i\subset \rho^sB\subset Q_i.                 \tag{3.1}
\]

An exact outer assignment is a perfect matching in this multigraph.
Therefore the symmetric difference of any two assignments is a disjoint
union of alternating even cycles.  Switching one alternating cycle is an
exact palette move, and these cycles generate this fixed-inner/type
subfibre.  With outer `B_i` and types fixed, the identical statement holds
for every inner rank separately.  Rank-one choices are local phase choices.

These matching cycles are a useful small basis, but not a basis for the
full matrix (2.1): type changes and rank-six transfers between the inner and
outer stages require compound circuits.

## 4. Exact finite audit at root 0

For each incumbent row, retain its root, type, and target resources and
enumerate every literal phase embedding.  The exact menu histogram is

```text
menu size : number of roots
1 : 942
2 : 42
3 : 6
4 : 3
5 : 1
6 : 138
7 : 296
12: 1
14: 1
```

Thus 488 roots have a support-one phase move and 942 are rigid.  Root 0 has
menu size one: the only copies of its rank-six target `0x0009f` and
rank-seven target `0x000df` nested inside `Q=0x000ff` are the displayed
copies.  Hence no support-one move at root 0 can change that row.  The
row-331 pivot in Section 1 shows that a turn out of root 0 can nevertheless
be created remotely by changing its prospective target row.

The complete support-two fibre which genuinely changes root 0 contains 22
literal moves, on only four partner rows:

```text
partner row : literal moves
15          : 1
330         : 7
331         : 7
412         : 7
```

All 22 retain root 0's outer set `B=0x000df` and `C2=0x00020`; the sevenfold
multiplicity is the rank-one slack singleton.  Exactly six of the 22 give
root 0 positive outdegree.  Optimizing first the number of zero-out roots,
then zero-in roots, selects the row-330 switch displayed in Section 1 and
gives `757/847`.  This proves feasibility and minimality among switches
required to change row 0 itself; it does not prove global support-two
minimality of repairing the root-0 cut.

The resource equality is transparent.  Before the switch the two rows use

```text
types                 {8,1}
rank-6 target orbits  {[0x0009f]}
rank-7 target orbits  {[0x000df],[0x000bf]}.
```

Afterward they use exactly the same multisets: type 1 moves to root 0,
type 8 moves to root 330, `0x0009f` remains the type-8 inner target, and
the two outer targets remain at their respective roots.  Only the literal
age classes and the slack singleton change.

## 5. The shortest outer-only cycle through root 0

If types and inner sets are frozen, root 0 has exactly one nonincumbent
outer option, the target of row 330.  Row 330 cannot accept root 0's outer
target, so no outer two-cycle contains root 0.  The shortest outer cycle is

```text
rows     [0,330,331]
old B    [0x000df,0x000bf,0x0109f]
new B    [0x000bf,0x0109f,0x000df].
```

It preserves types, inner targets, and all outer target orbits.  It is a
valid support-three alternating matching cycle.  However, it changes the
transition census to `910/761/848` and leaves root 0 with zero outdegree.
So changing the outer matching alone is not the needed first repair; the
successful support-two move uses a compound type/inner transfer.

## 6. Scope and next exact model

The audit is complete only for

* all support-one menus of the frozen table;
* every support-two move that changes root 0; and
* the shortest fixed-inner/type outer cycle through root 0.

It does not enumerate all support-two moves on all 1,430 roots and does not
claim the displayed move belongs to a sequence reaching a state
transversal.  The correct next exact layer is to enumerate zero-sum columns
of (2.1), update transition degrees incrementally, and optimize the
zero-out/zero-in objective before imposing the owner/root/H transversal.
Upper rows remain deliberately absent.

The exact matching and min-cut formulation for those two optimization
layers is given separately in
`MATH_THEOREM_A_K17_ROOTED_FLAG_SWITCH_FACTOR_AND_STATE_TRANSVERSAL_BENDERS_20260801.md`.
The present two-row move keeps the rank-six role set `S` fixed but swaps the
predecessor-rank colours (and hence types) of two rank-seven middle
vertices.  It therefore lies outside that note's fixed `(S,\kappa)`
totally-unimodular face and is a literal example of why the outer integer
master is necessary.

## 7. Frozen artifacts

```text
scratch/audit_threadA_k17_rooted_flag_palette_switch_basis_20260801.py
  SHA256 e5073d6ae7091ff4833594f0e79277d9eb170e53b6e0dc524b7a28d70d8c6b4b

scratch/threadA_k17_rooted_flag_palette_switch_basis_20260801.audit.json
  SHA256 44851b88701993ec86e5367bca5c490091525a41b71ac5815e4e429d80011939

scratch/verify_threadA_k17_root0_support2_witness_20260801.py
  SHA256 1a225758794d862389bf2d1de9278d909435bd07c5960f26f5a85472fdc56236

scratch/threadA_k17_root0_support2_witness_independent_20260801.audit.json
  SHA256 ef3c34a23125132331e12724edc4b41e6ebfaf29d931b2f58ccb60f8eb8fa608

scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
  SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab

scratch/audit_r_k17_root0_support2_matching_gain_20260801.py
  SHA256 a0e487efe73c332b98b6adb5cd154ebec4343555d0c40dc5c4aacbf7fd13e8db

scratch/k17_root0_support2_matching_gain_20260801.audit.json
  SHA256 47766d4e2514ff2d1197e924c0c6dc068a9eee55d88e51cfa2efaa00f7d5e843

scratch/verify_threadA_k17_ad9e_support2_root0_330_20260801.cpp
  SHA256 43d5978b3ebfaf03752b582c7ae457593e21772fd178dfd615e6435138c8533d

scratch/threadA_k17_rooted_support2_h100_20260801/
  support2_root0_330.audit.json
  SHA256 81dd97fbce6d66c7a4a5ddc208f5f3c28a68468da551e777257b65169c311483

  support2_root0_330.candidate.tsv
  SHA256 c75e807c11ec44241902d509e20a2ce84894a52601b7dd2faff755efdd81129a

  support2_root0_330.transition_delta.tsv
  SHA256 1d29b0b9de0102cfa37da1670e2c5d4d07ee861d88dd698608e58461d78e68ee

  run.stdout / run.stderr / compile.stderr
  SHA256 880564729673251e8b0331f531d86e23d0b7c7066803266147bb2ca91d31ef47
         113f7cb29c0391b6dd7129dc65f2f2f2c1f9208efe54b6684dd9e2ea9315bafb
         4fe55382f26508a50f029ec389373b9e6f4200a53fc1248fa40e0be69e4844bb
```

The deterministic enumerator reconstructs all displayed menus and switches
from the certificate.  The small Python verifier independently hard-codes
only the two-row witness and replays every transition containment.  The
separate C++ verifier consumes neither catalogue nor JSON: it hard-codes
the same witness, rechecks the entire lower/type ledger, rebuilds every
rooted transition and state arc, and reruns the root-support matching.  It
was compiled with `g++ -std=c++20 -O3 -DNDEBUG` and replayed on the H100
CPU; the frozen log records exit status zero and peak run RSS 5,120 KiB.
The final audit independently replays both the row-331 remote pivot and the
row-0/330 compound switch, recomputes their exact root-arc deltas,
Hopcroft--Karp values, and canonical Hall witnesses.
