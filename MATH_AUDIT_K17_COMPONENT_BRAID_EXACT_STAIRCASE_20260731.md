# K17 component braids: exact staircase replay and two seam no-gos

Date: 2026-07-31  
Status: exact finite audits; no global K17 impossibility claim

## 1. Exact evaluator

`scratch/audit_k17_component_braid_staircase_20260731.py` materializes an
arbitrary cut/orientation/order plan over cyclic carrier components and
audits, independently:

1. the exact terminal-start deadline debt
   \(\mathfrak D_3(T)=\rho_1+\rho_2+\rho_3\), where \(\rho_j\) is the
   final start of an internal positive run of length at most \(j\);
2. the exact arbitrary-start scalar optimum in the no-run-one case, by the
   \(O(\Delta^2)\) \((\delta_1,\delta_2)\) formula;
3. the literal lower-q1 palette; and
4. every upper target realized by a consecutive union in the resulting
   linear chronology.

The implementation reproduces the authenticated K16 carrier value

\[
                    \mathfrak D_3(T_{16})=6384
\]

exactly.  The arbitrary-start optimizer returns the same minimum with
\(\delta=(0,0,0)\), \(\tau=(0,0,6384)\).

Script SHA256:

    cb4f3550b91ef1255f4d44fd4658bc95e97b3de4b22942973246b2a5eb491bb1

## 2. The support-7115 factor

For the protected q1-exact eleven-component factor

    scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
    SHA256 3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e

the cyclic support census is:

\[
 |\operatorname{supp}(R_2\cup R_3)|=7115<7401,
\]

but its minimum per-component cyclic hull sums are

\[
 23525\quad\hbox{for run 2 or 3},\qquad
 23341\quad\hbox{for run 3}.
\]

The corrected audit payload is
`13d842e688fbfb571939bcb2a65cd5e1cc379e0c1a9709ec7569ca6ba816b900`.
Thus support cardinality passes, while one-cut-per-component clustering does
not.

In the stored component concatenation the exact linear replay gives

\[
 \rho=(19305,24285,24288),\qquad \mathfrak D_3=67878.
\]

The five internal singleton runs are seam-created rather than cyclic
factor runs.

## 3. Naive support clustering is false

Cut every cyclic component at every transition between the 7,115 support
vertices and their complement.  This gives 4,643 segments: 2,322 support
segments followed by 2,321 clean segments.

The literal audit gives

\[
 (N_1,N_2,N_3)=(1614,4037,3651),
 \qquad \rho=(24293,24293,24294),
 \qquad \mathfrak D_3=72880.
\]

It also leaves 4,095 lower-q1 holes and 7,119 upper holes.  Thus merely
placing the old short-run support first creates more short runs at the new
seams than it removes.

Artifacts:

    scratch/k17_pbbs_u_support_cluster_braid_20260731.plan.json
      SHA256 4cb652578ee036e232237fff575e67993c710d42e011ecd3c0eb0c52d7122d4e
    scratch/k17_pbbs_u_support_cluster_braid_20260731.audit.json
      SHA256 e2183456a166b8c621c56cd8768977bc8ed122b5e82355a774930d6f50864ead
      payload fed23cefe306e29ea5959f5e5177516ffd9a5aa524370d65d2da69288d4b68d0

## 4. Johnson-compatible seams are still insufficient

A stronger deterministic experiment joins the two segment families through
rank-nine Johnson endpoint arcs whenever possible.  Randomized port matching
found:

* 2,308 of 2,321 support joins Johnson-compatible;
* 2,296 of 2,320 clean joins Johnson-compatible;
* only 37 forced non-Johnson joins, of Hamming distance 4, 6, or 8.

Despite this, the exact replay gives

\[
 (N_1,N_2,N_3)=(833,1538,1623),
 \qquad \rho=(24304,24304,24304),
 \qquad \mathfrak D_3=72912.
\]

There are 3,364 lower-q1 holes and 4,480 upper holes.  Hamming distance two
controls only the number of changed coordinates at one seam.  It does not
control the ages of those coordinates on the two incident segments, and
therefore does not prevent length-one, two, or three runs.

Artifacts:

    scratch/make_k17_johnson_support_cluster_braid_20260731.py
      SHA256 79e75ba0ee6ec3170c16372e35633b19df0b05989c5070d5c291b4c122f65cdf
    scratch/k17_pbbs_u_johnson_support_cluster_braid_20260731.plan.json
      SHA256 7dee2d1dceedfd27235ee99b9b320734480ec83bec5ffc291abdf5119bb5eee3
    scratch/k17_pbbs_u_johnson_support_cluster_braid_20260731.audit.json
      SHA256 d55f4c3c2cf50dde836d6286e4bb5856cade6af030368e247895a4adc26a34ff
      payload 23da0206506e5ccc95ed8f352bb25c48edd0a7f6cbe06d7db5902dcfafefb95c

## 5. Correct reduced gate

The fragment-provider audit shows that all 1,838 deep holes have many
candidate cross-component endpoint pairs.  The experiments above isolate
the remaining constraint: the path-cover catalogue must decorate an endpoint
not just by its mask, but by the capped positive-run ages of all seventeen
coordinates on the incident prefix/suffix.  A seam is acceptable only if it
both supplies its palette obligation and obeys the exact run-state transition.

Consequently the next finite object is a **run-state-decorated seam path
cover**, scored after materialization by the exact deadline functional, not
an unlabelled Johnson path cover.

These audits refute only the two explicit braid rules above.  They do not
exclude another segmentation, protected circuit transport before cutting,
arbitrary-start shielding, or a common-cap solution at K17.
