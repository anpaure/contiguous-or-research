# `k=17`: chronology-first flag exchange and the fixed-`B`-orbit Hall obstruction

Date: 2026-08-01  
Lane: R / chronology-first OFHT  
Status: exact exchange theorem, exact finite obstruction for the authenticated
rooted factor, and independently replayed positive one-row repair.  This is a
packet-support theorem, not an owner-state cycle cover or a `k=17` word.

## 0. Verdict

For a depth-three rooted row write

\[
                 A=C_0\subset B=C_0\dot\cup C_1\subset Q,
                 \qquad C_2=Q-B.                    \tag{0.1}
\]

There are two sharply different exchange faces.

1. If `Q`, the type, and the **assigned necklace orbit of `B`** are fixed
   packetwise, but every literal phase of that `B` orbit inside `Q` and the
   residual `A` assignment are free, the exact static fibre is a product of
   labelled bipartite perfect-matching fibres.  Its complete moves are
   alternating even cycles, including parallel two-cycles which change only
   phases, together with independent one-row pivots in the slack rank-one
   packets.
2. This integral static fibre does not by itself make the chronology layer
   integral.  The general coupling schema between one selected flag and its
   incoming/outgoing literal turns is non-TU; no special integrality theorem
   is known for the present Boolean instance.

More decisively, take the exact residual `A`-orbit pool but relax both its
global one-use constraint and the requirement that a packet use one common
menu choice on its incoming and outgoing turns.  Union every literal turn
available from those independent endpoint menus, retaining quotient loops.
For the authenticated rooted certificate

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

the frozen chronology has 912 distinct root turns and 7,296
occurrence-/phase-labelled state arcs.  These are different projections:
all support matchings below are on packet roots, whereas the exact joint
model in Section 6 retains the labelled incidences.

The permissive union graph has

```text
literal root turns                       7512
quotient packet loops                       0
zero-out / zero-in packet roots         15 / 90
packet-support maximum matching            1304
Hall witness                          1206 / 1080
deficiency                                126.
```

Only six packets have two admissible literal phases of their fixed `B`
orbit; the other 1,424 have one.  Thus neither exact low-target alternating
cycles nor phase freedom of the fixed `B` orbit can raise the packet-support
matching to 1,430.  Any successful repair must change the assigned `B`
orbit or the type on at least 32 packet rows.  If the repair preserves the
old division of target resources between the `A` and `B` stages, the
stronger lower bound is 63 rows.

There is nevertheless an exact first positive move.  Moving only the slack
singleton in row 331 creates turns `0 -> 331` and `331 -> 409`, removes no
turn, and changes

```text
turns / zero-out / zero-in / matching
912 / 761 / 848 / 530
  ->
914 / 759 / 847 / 531.
```

Therefore root 0 is rigid when its **own** row alone changes, but its dead
successor cut is remotely repairable by one other row.  Any claim that two
changed rows are globally necessary to remove that cut is false.

## 1. Exact resource and circuit language in every depth

For an order-`d` rooted flag `f`, let `Q(f)` be its root, `t(f)` its type,
and let

\[
 S_1(f)\subset S_2(f)\subset\cdots\subset S_d(f)=Q(f) \tag{1.1}
\]

be its recorded prefix/suffix targets.  For every tight target row use one
common resource coordinate `(rank, necklace orbit)`, independent of the
stage at which that target occurs.  Put

\[
 r(f)=e_{Q(f)}+e_{t(f)}+
      \sum_{j:\,S_j\text{ tight}}e_{(|S_j(f)|,[S_j(f)])}.       \tag{1.2}
\]

Rank-one slack occurrences are omitted from the last sum.

### Theorem 1.1 (all-depth exact flag circuits)

Let `F` be a literal exact flag factor.  Replacing distinct rows
`f_1,...,f_h` by literal rows `g_1,...,g_h` on the same root set preserves
all roots, type masses, and every tight lower target if and only if

\[
                    \sum_i r(f_i)=\sum_i r(g_i).                \tag{1.3}
\]

Moreover, between any two zero-one factors in the same resource fibre,
their signed difference is a sign-compatible sum of primitive integer
kernel moves.  Applying those moves in any order gives a sequence of
literal resource-exact factors.

#### Proof

Every coordinate in (1.2) is one defining equality of the static factor,
so (1.3) is necessary.  Literal containment of every inserted column plus
equality in every defining row is sufficient.

For the last assertion, let `z=x'-x` be the difference of two zero-one
factors.  It is an integer kernel vector with entries in `{-1,0,1}`.  Choose
a nonzero conformal kernel vector of inclusion-minimal support, subtract it,
and iterate.  Conformality implies that no coordinate can be used twice:
every summand has entries in `{-1,0,1}` with the sign of `z`.  Consequently
every partial sum remains between `x` and `x'` coordinatewise and is again
zero-one.  Resource equality is preserved at every step.  These
support-minimal conformal vectors are the primitive flag circuits.  `square`

This is an exact exchange theorem, but it is not a claim that bounded
support or `2 x 2` moves generate the fibre.  Structural zeros can force
long circuits.

## 2. The fixed-`B`-orbit fibre is exactly alternating cycles

Specialize to depth three.  Fix packetwise:

* the root `Q_p`;
* the type, hence `a_p=|A_p|` and `b_p=|B_p|`; and
* the assigned necklace orbit `beta_p=[B_p]`.

The literal phase of `B_p` is **not** fixed.  Let

\[
 \mathcal B_p=\{\rho^jB_p:\rho^jB_p\subset Q_p\}.             \tag{2.1}
\]

Since the `B` orbits remain assigned injectively, choosing any member of
`cal B_p` cannot damage the `B`-palette row.

For each rank `s>=2`, let `P_s={p:a_p=s}` and let `R_s` be the residual
rank-`s` target-orbit bank after the already assigned `B` resources at that
rank are removed.  The certified scalar equalities give
`|P_s|=|R_s|`.  Form a labelled bipartite multigraph `G_s` from `P_s` to
`R_s`: an edge is a tuple

\[
       (p,R;\widehat B,\widehat A),\qquad
       \widehat B\in\mathcal B_p,\quad
       \widehat A\in[R],\quad
       \widehat A\subset\widehat B.                \tag{2.2}
\]

Parallel choices are retained.  Rank-one packets have only local choices
\(\{x\}\subset\widehat B\), because their target orbit is slack/repeated.

### Theorem 2.1 (phase-free fixed-orbit matching theorem)

The exact static flag factors with the above fixed data are in bijection
with

\[
                \prod_{s\ge2}\{\text{perfect matchings of }G_s\}
       \quad\times\quad
                \prod_{p:a_p=1}\{\text{local labelled choices at }p\}.
                                                               \tag{2.3}
\]

In particular this static polytope is integral.  Any two factors in it are
connected by alternating even-cycle switches in the `G_s` on tight ranks,
together with independent one-row pivots in the slack rank-one packets; a
change between parallel labelled edges is an alternating two-cycle.

#### Proof

A factor selects one literal row at every packet, hence one labelled edge
at every left vertex.  Exact use of every residual `A` target gives one edge
at every right vertex.  Conversely a perfect matching supplies one
`A subset B subset Q` row per packet, while the frozen `B`-orbit assignment
and roots supply their exact rows.  Different ranks have disjoint slots and
resources.  This proves (2.3).  Bipartite perfect-matching matrices are
totally unimodular.  Finally, the symmetric difference of two perfect
matchings in a bipartite multigraph is a disjoint union of alternating even
cycles, with parallel-edge differences giving length two.  `square`

### Corollary 2.2 (exact forced-option oracle)

Prescribe any mutually consistent set of labelled options (2.2), with no
packet or target used twice.  It extends to a complete static factor if and
only if, in every rank, the graph obtained by deleting the prescribed
packet and target endpoints has a perfect matching.  Equivalently, every
residual Hall inequality holds.

Given a current factor, the minimum number of changed packet rows in such
an extension is an ordinary min-cost perfect matching: cost zero is put on
the incumbent labelled edge and cost one on every other edge.  Thus pricing
one proposed literal turn is proof-safe: enumerate its compatible endpoint
option pairs and run the residual min-cost matching oracle for each pair.

## 3. Eliminating the arbitrary inner flags

For a prospective aligned root turn write

\[
 Q_q=Q_p-\{x\}+\{y\}.                               \tag{3.1}
\]

Choose literal middle suffixes `B_p in cal B_p` and
`B_q in cal B_q` in this common gauge, and put

\[
              C_{2,q}=Q_q-B_q,\qquad
              \ell_p=|A_p|,\quad \ell_q=|A_q|.      \tag{3.2}
\]

### Lemma 3.1 (arbitrary-`A` turn criterion)

There exist subsets \(A_p\subset B_p\), \(A_q\subset B_q\) of sizes
\(\ell_p,\ell_q\) making the depth-three turn literal if and only if

\[
\begin{aligned}
 x&\notin B_p,\\
 C_{2,q}&\subseteq B_p,\\
 \ell_p&\le |B_p-C_{2,q}|,\\
 |B_q|-\ell_q
   &\le \min\{\ell_p,\ |B_q\cap(B_p-C_{2,q})|\}.     \tag{3.3}
\end{aligned}
\]

#### Proof

The literal survivor rows are

\[
 x\in C_{2,p}=Q_p-B_p,\qquad
 C_{2,q}\subseteq B_p-A_p,\qquad
 B_q-A_q\subseteq A_p.                              \tag{3.4}
\]

The first three rows of (3.3) are immediate.  Subject to
\(A_p\subset B_p-C_{2,q}\) and \(|A_p|=\ell_p\), the largest possible
intersection with `B_q` is

\[
       \min\{\ell_p,|B_q\cap(B_p-C_{2,q})|\}.        \tag{3.5}
\]

The last inclusion in (3.4) can hold precisely when this is at least
\(|B_q|-\ell_q\); then choose `A_q` to contain `B_q-A_p` and fill it to size
\(\ell_q\).  Conversely every legal pair has this many elements of `B_q` in
`A_p`.  Finally `y` lies outside `Q_p`, whereas both survivor cells in
(3.4) lie in `Q_p`; hence \(y\in A_q\) and the refresh identity follows from
the complete target partition.  `square`

Lemma 3.1 gives a useful geometry-only diagnostic after the inner target
colours are forgotten.  It is not used for the global obstruction below,
because a loop-free diagnostic would omit potentially legal nonzero-phase
quotient self-loops.  For the proof-safe obstruction let `U` instead be the
packet digraph obtained as follows: at every root use every labelled option
from the exact residual banks in Theorem 2.1, independently at the two ends
of a prospective turn, and retain every literal turn, including a quotient
self-loop whenever its physical entering and deleted coordinates differ.
Global target one-use and one-common-menu consistency are relaxed.  Hence
the packet support of every exact factor in Theorem 2.1 is a subgraph of
`U`.

## 4. Exact finite Hall obstruction

As a nested calibration, keep each packet's two incumbent target orbits and
open only their literal phases.  There are 3,987 row menus.  Even the
menu-inconsistent union has only 2,306 packet arcs, 410 zero-out roots, 570
zero-in roots, and maximum matching 811.  Thus phase choice alone cannot
repair the 530 baseline matching.

The exact audit first reconstructs the residual target banks

\[
 |R_2|,|R_3|,|R_4|,|R_5|,|R_6|
       =8,40,140,364,442.                            \tag{4.1}
\]

It then materializes every labelled option (2.2), every one of the
`1430*9*8=102960` physical changing-owner root geometries, and the complete
refresh identity before taking the permissive endpoint-menu union.  The
fixed-`B`-orbit phase multiplicities are

```text
one phase : 1424 packets
two phases:    6 packets, IDs 7,85,695,1130,1364,1417.
```

There are 16,859 row menus.  Their independent endpoint union has 7,533
working physical geometries and 7,512 packet arcs.  The audit retains
quotient self-loops; the resulting count happens to be zero.  A deterministic
maximum matching yields a literal Hall set `S` and its exact neighbourhood
`H` with

\[
                       |S|=1206,\qquad |H|=1080.      \tag{4.2}
\]

All IDs themselves are recorded in the audit JSON.  Hence Hall gives
`nu(U)<=1430-126=1304`; the displayed matching has size 1,304, proving
equality.  There are 15 zero tails.  Root 201 is an explicit singleton cut:

```text
Q=3045, type=8, assigned B-orbit representative=2981,
possible source C1 masks={4,128,512}.
```

For every menu and physical successor geometry the forced target `C2` is
not contained in the source singleton `C1`; the exhaustive literal replay
therefore gives outdegree zero.  The full Hall witness gives the stronger
edit lower bound.

### Corollary 4.1 (outer/type edit floor, with and without stage migration)

Suppose a repaired factor has a packet-support perfect matching and differs
from the authenticated factor in its assigned `B` orbit or type on the
packet set `R`.  Arbitrary inner flags and `B` phases are free everywhere.
Then

\[
                              |R|\ge32.              \tag{4.3}
\]

If, in addition, every tight `A` target in the repaired factor belongs to
the old residual `A` bank (equivalently, no target resource migrates from
the old `B` stage into the new `A` stage), then

\[
                              |R|\ge63.              \tag{4.4}
\]

#### Proof

At most `|H|=1080` matched edges out of `S` can end in `H`, so at least 126
end outside `H`.  Let `K` be the set of packets whose repaired tight `A`
target does not belong to the old residual `A` bank.  Every target used at
such a packet was an old `B`-stage target.  Because target resources are
exact and the old `B` assignments are injective, that target's old `B`
packet must lie in `R`; assigning each member of `K` its old `B` packet is
injective.  Hence

\[
                              |K|\le |R|.             \tag{4.5}
\]

If an escaping matched edge has neither endpoint in `R union K`, then both
endpoint types and assigned `B` orbits are unchanged and both of its actual
`A` targets lie in the old residual bank.  Its two endpoint menus therefore
occur in the union defining `U`, so the edge would lie in `U`, contradicting
`H=N_U(S)`.  Every one of the 126 escaping edges is consequently incident
with `R union K`.  A packet occurs at most once as a matching tail and at
most once as a matching head, and hence covers at most two escaping edges.
Therefore

\[
       126\le2|R\cup K|\le2(|R|+|K|)\le4|R|,
\]

which proves (4.3).  Under the extra no-stage-migration hypothesis `K` is
empty, so `126<=2|R|`, proving (4.4).  `square`

These are row-count lower bounds, not claims that 32 or 63 changes suffice.
The distinction is essential: target resources are common across stages,
so an outer edit can free an old `B` target for use as `A` at a different,
otherwise unchanged packet.

## 5. A remote support-one repair and the corrected local scope

The original rows needed here are

```text
row 0:   Q=0x000ff, type8,
         (C0,C1,C2)=(0x0009f,0x00040,0x00020)
row 331: Q=0x010df, type1,
         (C0,C1,C2)=(0x00001,0x0109e,0x00040).
```

Keep row 0 fixed and replace only row 331 by

```text
(C0,C1,C2)=(0x01000,0x0009f,0x00040).
```

Its type, root, and middle suffix `B=0x0109f` are unchanged.  The changed
`C0` is still a singleton, so every resource coordinate (1.2) is unchanged.
Moreover

\[
 Q_{331}=Q_0-\{0x20\}+\{0x1000\},\qquad
 C_{1,331}=C_{0,0},\qquad C_{2,331}=C_{1,0}.          \tag{5.1}
\]

Thus `0 -> 331` is a literal turn, with the entering singleton `0x1000` as
the new `C0`.  Direct full replay adds exactly

```text
(0,331), (331,409)
```

and removes no root turn.  Hopcroft--Karp gives the exact matching increase
`530 -> 531` and the zero counts stated in Section 0.

The separately frozen two-row type-transfer on rows 0 and 330 also has
matching 531.  It adds

```text
(0,3),(330,0),(333,330),(343,330),(345,330)
```

and removes

```text
(13,0),(294,0),(328,0).
```

Therefore that two-row switch is a valid positive circuit, but is not
support-minimal for remotely eliminating root 0's dead row.

## 6. Why chronology is not the same flow

Let `Omega(p)` be the complete labelled flag options at packet `p`, and let
`T` be the complete phase- and owner-labelled directed turn multiset between
options.  Parallel turns remain distinct.  The exact cycle-cover master has
variables `x_u` and `y_tau` with

\[
\begin{aligned}
 \sum_{u\in\Omega(p)}x_u&=1 &&(p),\\
 \sum_{u:\,[A(u)]=R}x_u&=1 &&(R\text{ tight target}),\\
 \sum_{\tau:\operatorname{tail}(\tau)=u}y_\tau&=x_u &&(u),\\
 \sum_{\tau:\operatorname{head}(\tau)=u}y_\tau&=x_u &&(u),\\
 \sum_{\tau:\operatorname{owner}(\tau)=O}y_\tau&=1 &&(O).    \tag{6.1}
\end{aligned}
\]

One-cycle topology and voltage are later rows.  Equations (6.1) are compact
and exact, but not TU.

There is a smaller factorized owner-exact version on the fixed-`B`-orbit
face.  Let `I` be the 9-regular aligned root/owner incidence multigraph.
Use two incidence perfect matchings `D,H`.  For every owner `O` and every
ordered pair `i,j in I(O)`, use `w_(i,j)` to pair an outgoing `H` incidence
from a source root with an incoming `D` incidence at the next root.  Impose

\[
\begin{aligned}
 D(I(p))=D(I(O))&=1, & H(I(p))=H(I(O))&=1,\\
 \sum_jw_{ij}&=H_i, & \sum_iw_{ij}&=D_j.             \tag{6.2}
\end{aligned}
\]

The 1,430 owner fibres contribute exactly `81*1430=115830` pair variables.
For a selected row option define its coordinate-membership bits

\[
 a_{p,u}={\mathbf 1}_{u\in A_p},\qquad
 b_{p,u}={\mathbf 1}_{u\in B_p};                    \tag{6.3}
\]

these are linear sums of the option variables because exactly one option is
selected at `p`.  For `w_(i,j)`, align the head root and its row in the
physical gauge of the outgoing incidence.  If `gamma` is the head's oldest
singleton, literal compatibility is exactly

\[
 \gamma\in Q_p-B_p,\qquad
 \widehat Q_q-\widehat B_q\subseteq B_p-A_p,
 \qquad \widehat B_q-\widehat A_q\subseteq A_p.     \tag{6.4}
\]

Each membership implication in (6.4) is a three-term zero-one inequality.
For example, for \(u\in\widehat Q_q\),

\[
\begin{aligned}
 w-\widehat b_{q,u}&\le b_{p,u},\\
 w+a_{p,u}&\le1+\widehat b_{q,u},\\
 w+\widehat b_{q,u}-\widehat a_{q,u}&\le1+a_{p,u}.
                                                               \tag{6.5}
\end{aligned}
\]

The first two rows enforce the middle inclusion when `u` is in the target
`C2`; the third enforces the last inclusion when `u` is in target `C1`.
The singleton row is option-dependent: set `w=0` only when
`gamma notin Q_p`, and otherwise impose

\[
                         w+b_{p,\gamma}\le1.         \tag{6.6}
\]

Also impose `D_i+H_i<=1` for the same aligned incidence so the entering and
deleted physical coordinates differ.  Equations (6.2)--(6.6), together with
the static matching rows, are necessary and sufficient for a literal
owner-exact quotient cycle cover on this face.  They use at most

\[
 17914+2(12870)+115830=159484                      \tag{6.7}
\]

binary variables; the actual residual menu has 16,859 rather than 17,914
row columns.  Thus this is a compact exact integer formulation, not an
ownerwise nibble.

Equivalently, after complete state columns `z_sigma` are introduced, the
successor variables project out by the exact Hall family

\[
 z(X)\le z(\Gamma^+(X))\qquad(X\subseteq\Omega).     \tag{6.8}
\]

For binary `z`, taking `X` inside the selected states gives ordinary Hall,
and arbitrary `X` follows from its selected subset.  A violated row is a
maximum-closure/min-cut: give a selected tail weight `+z_sigma`, a selected
head weight `-z_tau`, and infinite implication arcs for literal successors.
This supplies a polynomial separation oracle, while leaving the outer
zero-one correlation explicit.

The obstruction is to a **generic** matching/TU reduction.  First delete the
owner rows, which can only take a row submatrix of the general schema.
Take two packets and two target colours `a,b`.  Give each packet one state
of each colour, and retain only the two directed 2-cycles using equal
colours.  No integral solution can both choose each colour once and close a
cycle: either cycle repeats `a` or repeats `b`.  Assigning one half to every
state and to every one of the four directed arcs satisfies all remaining
rows of (6.1).  Hence that row submatrix has an integer right-hand side and a
fractional feasible point but no integral point, so the general schema is
not totally unimodular.  This abstract minor is not asserted to be a literal
four-column minor of the fixed certificate; the exact finite obstruction for
that certificate is instead the Hall cut in Section 4.

Thus alternating cycles solve the **static fixed-`B`-orbit fibre**, and the
residual matching oracle exactly prices any fully decorated forced turn.
They do not turn the joint flag-and-successor selection into one ordinary
flow.  The chronology-first gate must either use the integer master (6.1),
or enlarge the packet circuits so a compound move carries one common flag
choice through both its incoming and outgoing turns.

## 7. Frozen audits

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

The first JSON stores the complete Hall tail/head ID lists.  The edge file
is the complete sorted packet graph used by the matching replay.  Both
audits are lightweight exact replays.  Neither uses a SAT solver.

## 8. Exact remaining gate

For this authenticated rooted table, the weakest surviving static
augmentation must open the packetwise assigned middle-suffix orbit or the
type on at least 32 rows while keeping the common lower resource coordinates
exact; the floor is 63 if the old `A`/`B` target-bank division is retained.
In the general circuit language this is a compound zero-sum move of (1.2),
not merely a low-target matching cycle.  Once such columns exist, they must
still be selected jointly with one common incoming/outgoing flag, one owner
attachment per orbit, and the state-level Hall rows.  Packet matching 1,430
would remain only a necessary relaxation of OFHT.
