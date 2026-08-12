# Independent audit: `k=17` chronology-first fixed-`B`-orbit Hall obstruction

Date: 2026-08-01  
Lane: R / OFHT chronology  
Verdict: **PASS after four corrections**

The audited theorem is

```text
MATH_THEOREM_R_K17_CHRONOLOGY_FIRST_FLAG_EXCHANGE_AND_FIXED_BORBIT_HALL_OBSTRUCTION_20260801.md
```

The four necessary corrections were:

1. the earlier loop-free arbitrary-`A` graph cannot by itself obstruct an
   unrestricted quotient cycle cover, because a nonzero-phase quotient
   self-loop can be physically legal; and
2. the row-0/330 two-row switch is not globally support-minimal, because a
   one-row phase pivot at row 331 already creates an outgoing turn from row
   0; and
3. the 126-edge Hall cut gives a 63-row edit floor only if the old division
   of target resources between the `A` and `B` stages is preserved.  With
   arbitrary exact cross-stage migration, the unconditional floor is 32;
   and
4. in the compact owner-exact formulation, the oldest-singleton condition
   is option-dependent and must be encoded by
   `w+b_(p,gamma)<=1`, not by a static prefilter from the incumbent row.

The corrected theorem uses the exact residual-`A` menu union, explicitly
retains all physical changing-owner quotient loops, and states the one-row
counterexample.

## 1. Static exchange fibre

For a rooted depth-three row write

\[
             A=C_0\subset B=C_0\cup C_1\subset Q,
             \qquad C_2=Q-B.
\]

Fix at each packet its root, type, and assigned necklace orbit of `B`, but
allow every literal copy of that orbit contained in the root.  At rank
`s>=2`, join a packet whose `A`-rank is `s` to a residual rank-`s` target
orbit once for every literal nested realization `A subset B subset Q`.
The right-bank sizes are

\[
                    8,40,140,364,442
\]

at ranks two through six.  They equal the packet counts at the respective
`A`-ranks.  Hence a static factor on this face is exactly one perfect
matching in each of these labelled bipartite multigraphs, plus independent
rank-one choices.  This proves both directions of the claimed bijection.
The symmetric difference theorem for bipartite perfect matchings proves
that alternating even cycles, including parallel-edge two-cycles, generate
the tight-rank matching factors; independent one-row slack pivots generate
the rank-one factors.  With that wording, this part is valid and integral.

It does **not** imply a generic integrality theorem after successor variables
are coupled to the same selected row.  After deleting owner rows, the
two-packet/two-colour half-integral example in the theorem satisfies every
remaining schema row but has no integral cycle cover.  This refutes a
generic TU reduction; it is not claimed as a literal minor of the fixed
certificate.

## 2. Literal turn test

For a physical root step

\[
                      Q_q=Q_p-\{x\}+\{y\},
\]

the three survivor requirements are exactly

\[
 x\in Q_p-B_p,
 \qquad Q_q-B_q\subseteq B_p-A_p,
 \qquad B_q-A_q\subseteq A_p.                       \tag{2.1}
\]

The audit program checks (2.1) and the complete age-zero refresh identity
for every labelled endpoint-menu pair.  The entering and deleted
coordinates are required to differ.  A target root in the same necklace
orbit as the source is retained; thus a physical nontrivial quotient loop
is not accidentally removed.

The separate arbitrary-inner-set criterion in the theorem is also correct.
After eliminating `A_p,A_q`, (2.1) is feasible iff

\[
\begin{aligned}
 x&\notin B_p,\\
 Q_q-B_q&\subseteq B_p,\\
 |A_p|&\le |B_p-(Q_q-B_q)|,\\
 |B_q|-|A_q|&\le
 \min\{|A_p|,|B_q\cap(B_p-(Q_q-B_q))|\}.
\end{aligned}
\]

Necessity follows by intersection counting.  For sufficiency, choose the
new `C1_q` inside
`B_q cap (B_p-(Q_q-B_q))`, extend it to `A_p` of the prescribed size, and
put `A_q=B_q-C1_q`.  Completeness of the target partition forces `y` into
`A_q`.  This criterion is diagnostic only; the global proof uses the exact
residual target menus.

In the factorized owner-exact master, the first row of (2.1) depends on the
selected source menu.  Its exact linear form is

\[
                         w+b_{p,\gamma}\le1
\]

when `gamma in Q_p`, and `w=0` only when `gamma notin Q_p`.  The two survivor
inclusions are the coordinatewise implications displayed in the theorem.
With this option-dependent singleton row, the compact formulation is exact;
predeleting `w` from the incumbent `B_p` alone would be an unsound freeze.

## 3. Exact finite replay and Hall cut

The authenticated certificate has SHA

```text
ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

The independent local replay compiled the C++ checker with `-O3` and
completed in under two seconds.  It obtained

```text
row menus                              16859
raw nonbacktracking root geometries   102960
working geometries                      7533
packet arcs                             7512
quotient loops                             0
zero-out / zero-in roots               15 / 90
maximum matching                         1304
Hall tail / neighbourhood             1206 / 1080
Hall deficiency                           126.
```

The smaller same-target phase-menu audit is consistent: 3,987 menus give a
menu-inconsistent union matching of only 811, with 410 zero-out roots.  It
is a nested obstruction, not a globally compatible phase selection.

The stored Hall neighbourhood was reconstructed directly from all outgoing
arcs of the stored tail set and agrees exactly.  Since endpoint menu choices
and residual-target one-use are relaxed, this graph is a supergraph of every
globally consistent exact factor with the fixed root/type/`B`-orbit
assignment.  Its matching deficiency therefore proves the scoped no-go.

The edit lower bound needs one further resource-bank distinction.  In any
perfect packet matching, at least 126 matching edges leave the old Hall
neighbourhood.  Let `R` be the packets whose type or assigned `B` orbit
changes, and let `K` be the packets whose repaired tight `A` target lies
outside the old residual `A` bank.  Every member of `K` consumes a distinct
old `B` target, so its old `B` owner lies in `R`; hence `|K|<=|R|`.  An
escaping edge with neither endpoint in `R union K` belongs to the permissive
old menu union, a contradiction.  Since a packet meets at most two matching
edges,

\[
             126\le2|R\cup K|\le4|R|,
\]

and therefore `|R|>=32` unconditionally.  If cross-stage target migration is
forbidden, `K` is empty and the stronger `|R|>=63` follows.  Both are only
necessary row counts, not constructions.

Root 201 supplies a smaller explicit obstruction.  Its possible source
`C1` masks are `{4,128,512}`; direct replay of all successor menus finds no
target `C2` contained in one of those singleton cells.  Thus its outdegree
is zero even in the endpoint-menu union.

## 4. Positive one-row calibration

At row 331, replacing

```text
(C0,C1,C2)=(0x00001,0x0109e,0x00040)
```

by

```text
(C0,C1,C2)=(0x01000,0x0009f,0x00040)
```

keeps its root, type, and `B=0x0109f`.  Since `C0` has rank one in both
rows, every tight resource coordinate is unchanged.  The literal identities

\[
 Q_{331}=Q_0-\{0x20\}+\{0x1000\},\quad
 C_{1,331}=C_{0,0},\quad C_{2,331}=C_{1,0}
\]

prove the new turn `0->331`.  Independent full replay adds exactly
`(0,331),(331,409)`, removes no root arc, and changes the maximum matching
from 530 to 531.  Hence the correction of the old global support-two
minimality claim is mandatory.

## 5. Exact boundary

Proved:

* the fixed-`B`-orbit static fibre is a product of labelled matching fibres;
* all its tight-rank palette-preserving static moves are alternating cycles,
  with independent one-row pivots on rank-one slack;
* even its menu-inconsistent packet union has matching only 1,304;
* any full-support repair of this certificate changes type or assigned
  `B` orbit on at least 32 packets, strengthened to 63 when the old
  `A`/`B` target-bank division is preserved; and
* one exact remote phase pivot raises the baseline support matching by one.

Not proved:

* existence after opening the outer `B`-to-root matching or type roles;
* a common owner-state transversal, quotient connectedness, or nonzero
  voltage;
* upper shadows, an opening, residence beyond the local age recurrence; or
* compiler/common-cap feasibility and a literal `k=17` word.

The next proof-safe layer is therefore the full lower factorization: outer
`B`-to-root alternating cycles together with synchronized role/type resource
circuits, selected jointly with the successor Hall rows.  Independent
ownerwise or rowwise nibbling remains invalid.

## 6. Frozen artifacts

```text
scratch/audit_threadA_k17_ad9e_phase_menu_union_20260801.cpp
  SHA256 215f12760ba5c8ddb63e375a05a1a82a3ea2a4c2ec552d825810e9759a05c30c
scratch/threadA_k17_rank8_rooted_nine_attachment_transition_20260801/phase_menu_union.audit.json
  SHA256 6d28fef2d3bb659964537c03704de4b6c1e558358986e97c2d7ff67cc911edb6

scratch/audit_r_k17_ofht_fixed_Borbit_global_A_union_20260801.cpp
  SHA256 17574853a12caa9b188a6d5dfcbc6d2d1080ef5a54e61fc9722210d70804cbda
scratch/k17_ofht_fixed_Borbit_global_A_union_20260801.audit.json
  SHA256 81f091ac662ddd39e2ffe76762aa1083f1a5d91d6c7295735766533cc0561c04
scratch/k17_ofht_fixed_Borbit_global_A_union_20260801.edges.tsv
  SHA256 4e086a5435653ac63513c4466d195c776412be2c52f70c3bd27f9be7a71c392b

scratch/audit_r_k17_root0_support2_matching_gain_20260801.py
  SHA256 a0e487efe73c332b98b6adb5cd154ebec4343555d0c40dc5c4aacbf7fd13e8db
scratch/k17_root0_support2_matching_gain_20260801.audit.json
  SHA256 47766d4e2514ff2d1197e924c0c6dc068a9eee55d88e51cfa2efaa00f7d5e843
```
