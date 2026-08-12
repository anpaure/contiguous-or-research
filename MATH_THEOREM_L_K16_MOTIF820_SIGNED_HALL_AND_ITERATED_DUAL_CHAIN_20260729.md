# K16 motif 820: signed Hall--Farkas row and the next iterative dual

Date: 2026-07-29  
Status: proved, solver-free Farkas certificate and bounded exact radius-two
audit.  No residence-clean successor factor is claimed.

## 1. Exact successor core

Let `Q2` be the factor obtained from the detector-zero endpoint by applying
both q1-perfect carrier preconditioners, duplicating `U27742` and `L57614`.
Against the same resident factor `R`, write `b_i>=0` for deletion of the
sorted `Q2\R` blue edge and `a_j>=0` for insertion of the sorted `R\Q2`
red edge.  The physical model is Boolean, but every obstruction below uses
only nonnegativity.

The frozen guarded core has ten lower colours

\[
\mathcal C_L=\{36617,39689,43785,49691,53771,
59937,62000,62024,64008,64032\},                            \tag{1.1}
\]

eight upper colours

\[
\mathcal C_U=\{36749,40717,48905,54043,
61967,64328,65060,65072\},                                 \tag{1.2}
\]

and motif 820, the coordinate-five length-two closure

\[
\mathcal M_{820}=\{(64036,64040),(64036,65028),
(64040,64264)\}.                                           \tag{1.3}
\]

Its three deletion variables are `b12455,b12456,b12457`, so residence
requires

\[
                     b_{12455}+b_{12456}+b_{12457}\ge1.     \tag{1.4}
\]

Every one of the eighteen q1 colours has source load one.  The stored core
is assumption-deletion-minimal in the trusted CP-SAT replay: deleting any
one of the nineteen guarded rows is `OPTIMAL`, with zero `UNKNOWN` replay.
Those feasibility witnesses are not serialized, so deletion-minimality is
solver-backed; the Farkas identity below is independently solver-free.

## 2. Exact-degree signed endpoint duality

For a physical Johnson seam `e=uv`, put

\[
 p(e)=1[u\cap v\in\mathcal C_L]+1[u\cup v\in\mathcal C_U]. \tag{2.1}
\]

For each guarded colour `c`, orient its normalized q1 row as

\[
 Q_c:\qquad b_{e(c)}-\sum_{a:\,a\text{ provides }c}a\le0. \tag{2.2}
\]

Orient exact degree balance at a middle vertex `v` as

\[
 D_v:\qquad \sum_{a\ni v}a-\sum_{b\ni v}b=0.              \tag{2.3}
\]

The nonnegative endpoint-capacity Hall theorem uses endpoint prices
`w_v>=0` because it relaxes equality to capacity.  With the exact equalities
(2.3), the endpoint multiplier is instead a free potential
`pi_v in R`.  Summing q1 rows with weights `lambda_c>=0` and degree rows
with potentials `pi_v` gives coefficient

\[
\begin{aligned}
\kappa_R(uv)&=\pi_u+\pi_v-lambda_{u\cap v}-\lambda_{u\cup v}
                 &&\text{on a red insertion},\\
\kappa_B(uv)&=\lambda_{u\cap v}+\lambda_{u\cup v}-\pi_u-\pi_v
                 &&\text{on a blue deletion}.              \tag{2.4}
\end{aligned}
\]

Here a lambda is zero when its rank-seven or rank-nine colour is not
selected.  If all coefficients in (2.4) are nonnegative, their sum is a
valid all-real Farkas inequality.  Negative `pi` is legitimate precisely
because (2.3) is equality; it would not be legitimate in the endpoint-
capacity relaxation.

## 3. Sparse primitive successor row

Take `lambda_c=1` for all eighteen colours in (1.1)--(1.2).  Set

\[
\begin{aligned}
S_+={}&\{36621,40713,47881,53787,61963,64033,64048,64072\},\\
\pi_v={}&1\quad(v\in S_+),\\
\pi_{64009}={}&-1,                                         \tag{3.1}
\end{aligned}
\]

and set every other potential to zero.

### Theorem 3.1 (motif-820 Farkas lock)

The literal row sum

\[
 \sum_{c\in\mathcal C_L\cup\mathcal C_U}Q_c
 +\sum_{v\in S_+}D_v-D_{64009}                             \tag{3.2}
\]

expands exactly to

\[
\boxed{
a_{6484}+a_{7719}+b_{12315}
+b_{12455}+b_{12456}+b_{12457}\le0,}                       \tag{3.3}
\]

where

\[
\begin{aligned}
a_{6484}&=(31267,64033),\\
a_{7719}&=(37435,53787),\\
b_{12315}&=(61977,64009).                                  \tag{3.4}
\end{aligned}
\]

Every displayed coefficient is one.  Of the 12,479 variables on each shore,
the remaining 12,477 red and 12,475 blue coefficients are zero.
Consequently (1.4) contradicts
(3.3) over the nonnegative reals.  The rebuilt exact overlay is LP-
infeasible, not merely integrally infeasible.

#### Proof

Formula (2.4) computes every coefficient in (3.2).  Direct physical replay
gives nonnegative minima zero on both shores and the complete positive
supports

\[
\begin{aligned}
\{e:\kappa_R(e)=1\}&=\{(31267,64033),(37435,53787)\},\\
\{e:\kappa_B(e)=1\}&=\{(61977,64009)\}\cup\mathcal M_{820}.
                                                               \tag{3.5}
\end{aligned}
\]

There are no other nonzero coefficients.  This proves (3.3).  Its left side
is at least the motif sum, which is at least one by (1.4), while (3.3)
requires it to be at most zero.  QED.

The selected q1 rows have 30 physical provider edges on 39 vertices.  Adding
the three non-q1 residual columns in (3.4) gives an effective 33-edge support
on 43 vertices.  If support means every column touched before cancellation,
the nine degree rows and eighteen q1 rows touch 36 edges; the final
nonzero-coefficient support is the six edges in (3.5).  These notions must
not be conflated.

## 4. Why ordinary endpoint capacity stops one step early

If the negative potential at `64009` is omitted, the natural eight-socket
nonnegative row is

\[
\begin{aligned}
a_{6484}+a_{7719}+a_{10022}+a_{12335}
 +b_{12455}+b_{12456}+b_{12457}-b_{12453}\le0,              \tag{4.1}
\end{aligned}
\]

where

\[
\begin{aligned}
a_{10022}&=(47881,64009),&a_{12335}&=(61963,64009),\\
b_{12453}&=(64009,64033).                                  \tag{4.2}
\end{aligned}
\]

Thus nonnegative endpoint capacity proves only that a motif hit must pay by
deleting `b12453`.  Subtracting `D64009` cancels `a10022,a12335,b12453`
and introduces the nonnegative term `b12315`, yielding (3.3).  The negative
potential is essential, not a cosmetic alternate normalization.

This identifies the exact hierarchy needed by the iterative separator:
ordinary capacity Hall first exposes the leak socket; exact-degree signed
Hall closes it.

## 5. Finite-capacity escape price

For an exterior red seam `e=uv`, define its signed escape gain

\[
 g(e)=p(e)-\pi_u-\pi_v.                                    \tag{5.1}
\]

Adding a red variable of gain `g(e)>0` introduces coefficient `-g(e)` in
the extended row.  Therefore, for bounded exterior capacities `0<=z_e<=u_e`,
any fractional augmentation capable of neutralizing this fixed ray must
satisfy

\[
\boxed{
                         \sum_e u_e[g(e)]_+\ge1.}            \tag{5.2}
\]

Below one, the same ray still proves infeasibility.  At or above one, this
ray alone ceases to separate; (5.2) is not sufficient for fractional
feasibility of the augmented overlay.

Every positive-gain seam lies among a guarded-colour provider or an edge
incident with one of the nine nonzero-potential vertices.  Their complete
physical union has 1,030 edges.  Of 994 exterior relevant seams, exactly
530 have positive gain:

\[
\begin{array}{c|rr}
g&1&2\\ \hline
\#&522&8.
\end{array}                                                \tag{5.3}
\]

There is no gain above two.  The eight gain-two seams are

\[
\begin{gathered}
(64009,64010),(64009,64012),(64009,64024),(64009,64040),\\
(64009,64136),(64009,64264),(64009,65032),(64036,65056).
                                                               \tag{5.4}
\end{gathered}
\]

Hence the minimum raw fractional activation mass for this ray is exactly
one half, attained on any seam in (5.4).  With integral unit-capacity
columns, one positive-gain seam is the minimum catalogue escape.  Neither
statement constructs degree-balanced recourse.

The direct proof audit also finds no positive-gain common edge in
`Q2 intersection R`.  A second signed-socket mechanism is possible in
principle: inserting a new Q-only blue seam of negative gain.  The complete
socket audit finds 342 Q-absent negative-gain seams, 340 of them outside
`Q2 union R`; they admit 97 and 96 degree-balanced C4 completions,
respectively, and zero completion preserves both q1 palettes.  Thus neither
common-edge promotion nor a negative-gain blue seam supplies an omitted
radius-two escape.

## 6. Exact minimum literal q1-perfect trades

A nontrivial edit of a simple two-factor cannot have one deletion and one
insertion: degree preservation would force the two endpoint multisets, and
hence the two undirected edges, to be equal.  Thus literal radius is at least
two.  A bounded exhaustive active-provider C4 audit attains this lower bound
in exactly two ways.

### 6.1 Guarded-redundancy escape

\[
\begin{array}{ll}
\text{delete}&(43789,47629),\ (44557,44809),\\
\text{insert}&(43789,44809),\ (44557,47629).
\end{array}                                                \tag{6.1}
\]

Its complete nonzero q1 load changes are

\[
 L_{43785}:1\to2,\quad L_{44553}:2\to1,\quad
 U_{47885}:3\to2,\quad U_{48653}:1\to2.                   \tag{6.2}
\]

It creates a second provider of the source-unique guarded colour `L43785`,
so the normalization (2.2) and the fixed ray must be rebuilt.  It does not
hit motif 820.  It removes one old short motif, creates four, and worsens the
residence count from 2,224 to 2,227; the two component lengths remain 13 and
12,857.

### 6.2 Direct collar slide

\[
\begin{array}{ll}
\text{delete}&(56088,64024),\ (64040,64264),\\
\text{insert}&(56088,64264),\ (64024,64040).
\end{array}                                                \tag{6.3}
\]

Its complete nonzero q1 changes are

\[
 L_{55832}:2\to1,\quad L_{56072}:1\to2,\quad
 U_{64056}:1\to2,\quad U_{64296}:2\to1.                   \tag{6.4}
\]

This deletes the motif edge `(64040,64264)` and replaces its unique
`L64008` occurrence exactly.  Motif 820 disappears, but the same
coordinate-five length-two defect reappears with closure

\[
 \{(64024,64040),(64036,64040),(64036,65028)\}.             \tag{6.5}
\]

The residence count stays 2,224, while the components change from
`(13,12857)` to `(13,2270,10587)`.  This is exact defect transport, not
residence descent.

Both trades delete two `Q2\R` edges and insert two edges outside
`Q2 union R`.  The audit records all 648 abstract guarded-provider slots,
checks up to four neighbour pairings for each provider absent from the
source, and deduplicates to 173 Johnson C4s.  Exactly the
two trades above preserve both complete q1 palettes and break the
certificate, one by changing a guarded source row and one by hitting its
motif.  Every direct motif hit must replace a source-unique guarded provider;
every source-row escape adds such a provider.  Section 5 separately
exhausts both remaining signed-socket mechanisms: there is no positive-gain
common edge, and none of the 97 Q-absent negative-gain socket C4s is q1-
complete.
Thus radius two is the exact literal minimum and (6.1),(6.3) are the complete
minimum C4 list.

Neither trade produces residence progress, and feasibility of either
rebuilt exact overlay remains unproved.

## 7. Exact overlap with the preceding dual

The successor is not a relabelled copy of the preceding 21-colour global
motif-390 row.  The final comparison bullet separately concerns that row's
17-colour internal-edge affine summand.

* The old 21-colour row and the new 18-colour row share exactly one selected
  q1 colour, `U65060`.
* Their nonzero degree-potential supports are disjoint.
* Their motif closures are disjoint in both edges and vertices.
* Their physical selected-provider/effective supports share exactly

  \[
       (64036,64040),\qquad(64036,65028).                    \tag{7.1}
  \]

  The first edge changes selected role from old `U64044` to new `L64032`;
  the second retains `U65060`.
* The corresponding common physical vertices are exactly

  \[
                  \{57871,64036,64040,65028\}.              \tag{7.2}
  \]

* The collapsed positive-coefficient supports of the preceding affine row
  (seven edges) and successor row (six edges) are edge- and vertex-disjoint.

Both shared edges were neutral in the old row because the old endpoint
weight charged `64036`.  The successor potential drops `64036`, turning
them into two of the three positive motif columns.  In particular, an old
charged socket has become an unpriced new motif hub.  This is the concrete
iterative-dual mechanism: a q1-safe escape discharges one certificate but
migrates the obstruction to a nearly disjoint palette/socket block.

Neither minimum successor C4 uses an edge of the two prior q1-safe carrier
preconditioners.

## 8. Proved boundary

Proved:

* all eighteen q1 rows plus nine signed degree multipliers give the exact
  six-term identity (3.3);
* the identity has been checked on all 24,958 overlay columns and proves LP
  infeasibility;
* the negative potential at `64009` is necessary for this displayed
  cancellation; the nonnegative capacity row leaks through `b12453`;
* the fixed-ray exterior escape census is `522` gain-one and `8` gain-two
  seams, so fractional column mass one half and one integral column are
  sharp certificate-neutralization thresholds;
* literal degree/q1-perfect certificate escape has exact minimum radius two;
  the two minimum C4s are (6.1) and (6.3); and
* the exact support-overlap statements in Section 7 hold.

Not proved:

* nine nonzero degree multipliers are globally minimum among all Farkas
  certificates;
* neutralizing this one ray makes the augmented fractional overlay feasible;
* either radius-two escape admits a feasible rebuilt overlay;
* either escape decreases residence; or
* topology, deeper shadows, voltage, or the literal compiler is complete.

## 9. Frozen provenance and replay

```text
successor guarded core
285063a11c1894f3420fe442a7c3d2f6cb16138ab8ff8fbd1b5980569ddad6a6
scratch/k16_mixed_hall_escape_both_guarded_core_20260729.json

twice-preconditioned Q2
b935ee4a4ce3c494e7f2daf2756b3c6aeba2751b39f996082edf16e298642b49
scratch/k16_failedlit0_mixed_hall_escape_u27742_plus_l57614_20260729.json

canonical resident/Q endpoint reconstruction
fbd182aff3117581c7cf5216e33a30db3309da23c8d570275114e5a6165985e9
scratch/k16_resident_resume1_q1_canonical_physical_endpoints_20260729.json

signed Farkas, finite-capacity and overlap replay
00697aeedbee798212eb7e27b86891595b6f76572e631b4bf2db197fe4b281e2
scratch/audit_k16_motif820_sparse_hall_20260729.py

404c2d492983b16e908843ef6d263c8e2e9cdd6176847eea94940d51c29e7949
scratch/k16_motif820_sparse_hall_20260729.audit.json

minimum full-q1 C4 replay
d8ab47dc02d17539d5bd7c04e9306a6f7ecc72ace9cb6f509e0885491b8c3ce3
scratch/audit_k16_motif820_active_colour_c4_20260729.py

527e9fb32b833a5d254817b67a2f07bcf5617b27d7da4771dad42ca5e49fea2b
scratch/k16_motif820_active_colour_c4_20260729.audit.json
```

The signed replay uses only the Python standard library.  The C4 replay is a
bounded 648-provider/four-completion audit using the already frozen literal
factor helpers.  No SAT/CP/LP solve, remote job, sustained local computation,
or process management was used.
