# K16 L57614-only successor: exact signed dual and radius-two continuation

Date: 2026-07-29  
Status: proved by solver-free all-column algebra and bounded literal C4
replay.  Two successor factors are materialized.  No rebuilt-overlay
feasibility or residence descent is claimed.

## 1. Branch comparison and the primary endpoint for this dual gate

Let `Q0` be the detector-zero q1-perfect endpoint.  The two previously
audited radius-two carrier preconditioners duplicate `U27742` and `L57614`.
The three relevant guarded extractions are:

\[
\begin{array}{c|c|c|c}
\text{carrier}&\text{core size}&\text{q1 rows}&\text{motifs}\\ \hline
U27742\text{ only}&23&8L+13U&2\\
L57614\text{ only}&19&10L+8U&1\\
U27742+L57614&19&10L+8U&1.
\end{array}                                                \tag{1.1}
\]

The L-only and composed 19-row cores have identical physical q1 rows,
provider indices, and closure

\[
\mathcal M=\{(64036,64040),(64036,65028),(64040,64264)\}.   \tag{1.2}
\]

Only the stored cyclic occurrence label differs: motif `790`, start `5535`
for L-only versus motif `820`, start `7706` for the composed endpoint.

The L-only endpoint has two components `(13,12857)`, complete lower and
upper q1 palettes, and 2,222 short-residence violations.  The composed
endpoint has the same component lengths and same successor core but 2,224
violations.  Thus the extra `U27742` preconditioner gives no successor-dual
benefit and costs two residence violations.  The L-only endpoint is strictly
better for this fixed dual gate and the scalar residence count; no global
topology dominance is claimed.

By contrast, the U-only 23-row core still contains the original
coordinate-two length-two motif 390 and a coordinate-nine length-three
motif.  The `U27742` escape alone therefore does not reach the successor
socket.

Frozen guarded-core hashes are

```text
L57614 only
60c01989449f066e5daa943fda7282e637a5bfba3250d89b174918455692bf96
scratch/k16_mixed_hall_escape_l57614_guarded_core_20260729.json

U27742+L57614
285063a11c1894f3420fe442a7c3d2f6cb16138ab8ff8fbd1b5980569ddad6a6
scratch/k16_mixed_hall_escape_both_guarded_core_20260729.json

U27742 only
996514c394b46c7ae6a81df49b1821a473a97efe79b3ee6552148a183f0d519b
scratch/k16_mixed_hall_escape_u27742_guarded_core_20260729.json
```

## 2. Exact signed Hall--Farkas row on the L-only shore

The successor colour sets are

\[
\begin{aligned}
C_L={}&\{36617,39689,43785,49691,53771,
59937,62000,62024,64008,64032\},\\
C_U={}&\{36749,40717,48905,54043,
61967,64328,65060,65072\}.                                \tag{2.1}
\end{aligned}
\]

For a physical edge `e=uv`, let

\[
p(e)=1[u\cap v\in C_L]+1[u\cup v\in C_U].                 \tag{2.2}
\]

Put endpoint potential one on

\[
S_+=\{36621,40713,47881,53787,61963,64033,64048,64072\},   \tag{2.3}
\]

put `pi_64009=-1`, and put zero elsewhere.  Give all eighteen
source-unique q1 rows weight one.  If

\[
D_v=\sum_{a\ni v}a-\sum_{b\ni v}b=0,                       \tag{2.4}
\]

then the literal sum of all eighteen q1 inequalities with

\[
                     \sum_{v\in S_+}D_v-D_{64009}           \tag{2.5}
\]

is exactly

\[
\boxed{
a_{6484}+a_{7719}+b_{12315}
+b_{12455}+b_{12456}+b_{12457}\le0.}                       \tag{2.6}
\]

The non-motif residual edges are

\[
a_{6484}=(31267,64033),\quad
a_{7719}=(37435,53787),\quad
b_{12315}=(61977,64009).                                   \tag{2.7}
\]

Every displayed coefficient in (2.6) is one.  Of the 12,479 variables on
each shore, the remaining 12,477 red and 12,475 blue coefficients are zero.
Since residence requires

\[
b_{12455}+b_{12456}+b_{12457}\ge1,                         \tag{2.8}
\]

the L-only exact overlay is infeasible already over the nonnegative reals.

The negative potential is essential.  Using only the eight positive sockets
gives the leaking capacity row

\[
a_{6484}+a_{7719}+a_{10022}+a_{12335}
+b_{12455}+b_{12456}+b_{12457}-b_{12453}\le0,              \tag{2.9}
\]

with `b12453=(64009,64033)`.  Subtracting `D64009` cancels the
leak and replaces it by the nonnegative term `b12315`.  This successor is
therefore an exact-degree signed-potential obstruction, not an ordinary
nonnegative endpoint-cover row.

The U-only carrier trade changes four physical edges of signed gain zero,
uses no colour in (2.1), and touches no vertex in the support of `pi`.
Consequently (2.6) is coefficientwise identical on the L-only and composed
overlays, not merely isomorphic.

Relative to the preceding motif-390 mixed row, the successor shares exactly
one selected colour, `U65060`, no nonzero potential vertex, two effective
physical edges `(64036,64040)` and `(64036,65028)`, and four effective-support
vertices lying in both support vertex sets: `57871,64036,64040,65028`.
Thus it is a nearly disjoint successor
block rather than a rescaling of the preceding dual.

## 3. Exact finite-capacity escape price

For an exterior red seam define

\[
                       g(e)=p(e)-\pi_u-\pi_v.                \tag{3.1}
\]

Any bounded augmentation neutralizing this fixed ray must satisfy

\[
\boxed{\sum_e u_e[g(e)]_+\ge1.}                            \tag{3.2}
\]

The complete relevant physical universe has 1,030 seams.  Of 994 exterior
seams, exactly 530 have positive gain:

\[
\begin{array}{c|rr}
g&1&2\\ \hline
\#&522&8.
\end{array}                                                \tag{3.3}
\]

The eight gain-two seams are

\[
\begin{gathered}
(64009,64010),(64009,64012),(64009,64024),(64009,64040),\\
(64009,64136),(64009,64264),(64009,65032),(64036,65056).
                                                               \tag{3.4}
\end{gathered}
\]

Hence the sharp raw fractional activation mass for this ray is one half;
one unit-capacity seam is the minimum integral catalogue escape.  These are
certificate thresholds, not degree-balanced recourse.  There is no
positive-gain common edge in the L-only `Q intersection R`.  The companion
negative-gain socket census checks 342 Q-absent seams, 340 exterior seams,
97/96 degree-balanced completions, and zero full-q1 completion.  Together
these close both possible signed-socket escape modes at radius two.

Equation (3.2) is scoped to exterior red-column augmentation with this
carrier, row normalization, and potential fixed.  Arbitrary carrier/blue
augmentation has the complementary donor price `[-g(e)]_+`, which is why
the negative-gain C4 census is separately necessary.

## 4. Exact minimum literal q1-perfect continuation

A nontrivial edit of a simple two-factor needs at least two deletions and
two insertions.  The complete active-provider audit records 648 abstract
provider slots, checks up to four local completions for each absent provider,
and deduplicates to 173 distinct Johnson C4s.  Exactly two C4s preserve both
full q1 palettes and break the successor certificate.

### 4.1 Redundancy branch

\[
\begin{array}{ll}
\text{delete}&(43789,47629),\ (44557,44809),\\
\text{insert}&(43789,44809),\ (44557,47629).
\end{array}                                                \tag{4.1}
\]

It duplicates `L43785`; the complete q1 changes are

\[
L_{43785}:1\to2,\ L_{44553}:2\to1,\
U_{47885}:3\to2,\ U_{48653}:1\to2.                        \tag{4.2}
\]

It leaves the motif closure intact, increases residence violations
`2222 -> 2225`, and changes the components to `(13,5576,7281)`.  Its
materialized factor is

```text
cd379fd288d515fd58c96d71e8034c96a9114165ba7447bb8c4cdd8be73a8590
scratch/k16_l57614_motif820_escape_redundancy_l43785_20260729.json
```

### 4.2 Direct collar slide

\[
\begin{array}{ll}
\text{delete}&(56088,64024),\ (64040,64264),\\
\text{insert}&(56088,64264),\ (64024,64040).
\end{array}                                                \tag{4.3}
\]

Its complete q1 changes are

\[
L_{55832}:2\to1,\ L_{56072}:1\to2,\
U_{64056}:1\to2,\ U_{64296}:2\to1.                        \tag{4.4}
\]

It removes `(64040,64264)` from (1.2), but creates the new coordinate-five
length-two closure

\[
\{(64024,64040),(64036,64040),(64036,65028)\}.             \tag{4.5}
\]

Thus residence remains exactly `2222`, while components become
`(13,2270,10587)`.  Its materialized factor is

```text
c47a7f231496414a9bfad028bd5f0816e85e53fccae7d657a919a183ffd49e74
scratch/k16_l57614_motif820_escape_direct_slide_20260729.json
```

Both moves delete two L-only `Q\R` edges and insert two seams outside
`Q union R`.  Every direct motif hit must replace one of the guarded unique
providers; every row-normalization escape creates a guarded provider; and
the signed-socket census excludes the remaining mechanisms.  Hence radius
two is the exact minimum and (4.1),(4.3) are the complete minimum list.

## 5. Does the two-edge chain strictly continue?

Yes for literal carrier mobility and certificate escape:

\[
Q_0\xrightarrow[\text{q1-perfect}]{\text{radius }2\;L57614}
Q_L\xrightarrow[\text{q1-perfect}]{\text{radius }2\;\text{(4.3)}}
Q_{L,\mathrm{slide}}.                                      \tag{5.1}
\]

The two move supports are edge- and vertex-disjoint, so the composition is
literal.  Every factor in (5.1) is materialized, spanning, degree two, and
complete in both q1 palettes.  Thus the first q1-safe escape did not exhaust
radius-two mobility.

It does **not** strictly continue a residence descent.  The preferred direct
move only transports the same length-two collar and leaves the residence
count unchanged.  The alternative redundancy move is worse by three.  The
red/blue overlay has not been rebuilt after either new C4, so no third
Farkas core, overlay feasibility, or termination statement follows.

The composed U+L branch has exactly the same two local continuations but
starts two residence violations higher.  The L-only chain is therefore
better for this fixed dual gate and residence scalar.  After the redundancy
move it has three components while the composed branch retains two, so no
joint residence/topology dominance is asserted.

## 6. Exact boundary

Proved:

* the L-only 19-row core has the signed six-term all-real certificate (2.6);
* it is coefficientwise identical to the composed endpoint certificate;
* the finite-capacity census and sharp fixed-ray thresholds are (3.2)--(3.4);
* literal q1-perfect certificate escape has exact radius two and exactly the
  two C4s (4.1),(4.3);
* both successor factors are materialized and deterministically replayed; and
* the L-only direct slide gives a second composable radius-two step.

Not proved:

* either materialized successor has a feasible exact overlay with `R`;
* either move reduces residence;
* a third bounded C4 continues the chain after the slide;
* any deeper shadow, topology, voltage, or compiler condition.

## 7. Permanent replay

```text
L-only source
167aa8534d0fc3b1483c2e60d965faf94bfea1f233a5f4cb593c620191e00651
scratch/k16_failedlit0_mixed_hall_escape_l57614_20260729.json

signed Hall/Farkas verifier
00697aeedbee798212eb7e27b86891595b6f76572e631b4bf2db197fe4b281e2
scratch/audit_k16_motif820_sparse_hall_20260729.py

aec277604f3f6749e4dcfa79b534653fecee4bf965ae8080e9ad3ae5c1e73cfe
scratch/audit_k16_motif820_l57614_sparse_hall_20260729.py

983c5f573889cf8ba7cb836b6b53968b0e5b0505143433e306ff00bcf4a6c17b
scratch/k16_motif820_l57614_sparse_hall_20260729.audit.json

minimum C4 verifier
d8ab47dc02d17539d5bd7c04e9306a6f7ecc72ace9cb6f509e0885491b8c3ce3
scratch/audit_k16_motif820_active_colour_c4_20260729.py

d979c7c2a8cfd0e47e09e667d898759c262f91ca26c4378b8885755860907241
scratch/audit_k16_motif820_l57614_active_colour_c4_20260729.py

a7f67624d3b0c196e465df0b0ddb5bfe1db09480e2090cd54b46c5c0c699d070
scratch/k16_motif820_l57614_active_colour_c4_20260729.audit.json

materializer
cc648d24900725e1b57d047d4d2de19daeb874be8ac2b1e7685c31921f7d9958
scratch/materialize_k16_motif820_l57614_c4_escapes_20260729.py

da10a5e3552cb35090f43d72b6b7919b04495e13a5c3b05a7fe109b60df58758
scratch/k16_l57614_motif820_c4_materialization_20260729.audit.json
```

All work was bounded deterministic replay.  No SAT, CP, LP, remote job,
sustained local computation, or process management was used.
