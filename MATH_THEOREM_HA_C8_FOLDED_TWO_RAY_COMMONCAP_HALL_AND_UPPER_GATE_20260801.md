# Folded C8 two-ray common caps close the local Hall row, but not the upper-exact selector

Date: 2026-08-01  
Lane: H/A, quotient-fold common-cap and terminal compiler  
Status: exact local source/cap/Hall theorem, exact finite cut tradeoff, and
an exact upper-partition obstruction.  No Catalan placement or
`B(k)+O(1)` conclusion is claimed.

## 0. Verdict

Suppress a fixed core `K`.  The quotient-folded pair has directed source
support differences

\[
\begin{aligned}
 \mathcal P_0&=\{K+za_3+F[1,j]:1\le j<d\},&
 \mathcal S_0&=\{K+za_1+F[j,d]:1<j\le d\},\\
 \mathcal P_1&=\{K+za_1+F[1,j]:1\le j<d\},&
 \mathcal S_1&=\{K+za_3+F[j,d]:1<j\le d\}.
\end{aligned}                                                \tag{0.1}
\]

There are two exact local closures.

* One binary host carries both rays with one phase-common cap and cost one,
  but only as a nonflat, deadline-`+1` interface.  An internal flat split is
  impossible for every `d`.
* Two one-sided hosts on one common filler rail have a literal common cap
  and `2d-2` pairwise distinct ray cells.  Those cells give a diagonal
  perfect matching, so the typed local Hall deficiency is exactly zero.

This does **not** place the folded path in an upper-exact Catalan forest.
For the upper-support-safe Hamilton opening, the `8d+23` forced edges have
only sixteen upper labels, with load profile

\[
                         1^8(d+1)^1(d+2)^7.              \tag{0.2}
\]

Hence their rank in the upper partition matroid is `16` and their nullity
is `8d+7`.  A residual selector cannot repair dependence already present in
the forced bank.  The local compiler theorem and the strict upper-selector
row are therefore genuinely different statements.

## 1. The exact one- and two-host packets

### 1.1 One host

Put

\[
 X=K+za_1a_3,
 \quad (Z^0,T^0)=(K+za_3,K+za_1),
 \quad (Z^1,T^1)=(T^0,Z^0).                              \tag{1.1}
\]

Between the two decreasing filler rails, replace `X` by
`Z^epsilon,T^epsilon`.  The left exclusive intervals are `P_epsilon` and
the right exclusive intervals are `S_epsilon`; all have width at most `d`.
Both halves lie in the common cap `X`, and contracting them preserves every
old interval OR.

If this split is made internally in a flat depth-`d` rank-`r` source, the
`d` new natural windows containing both halves lie in intersections of
adjacent distinct rank-`r` owners.  Each therefore has rank at most `r-1`.
Thus the one-host packet is an exact nonflat interface and an all-`d` flat
no-go.

### 1.2 Two hosts

Define

\[
\begin{array}{ll}
L_0=K+za_3f_1,&L_1=K+za_1f_1,\\
R_0=K+za_1f_d,&R_1=K+za_3f_d,
\end{array}
\]

and

\[
 X_L=L_0\cup L_1,
 \qquad X_R=R_0\cup R_1.                               \tag{1.2}
\]

Starting with

\[
                    X_L,f_2,\ldots,f_{d-1},X_R,         \tag{1.3}
\]

use

\[
 X_L\mapsto(X_L,L_\epsilon),
 \qquad X_R\mapsto(R_\epsilon,X_R).                    \tag{1.4}
\]

The common cap word is

\[
                    X_L,X_L,f_2,\ldots,f_{d-1},X_R,X_R. \tag{1.5}
\]

Every old interval has an injective full-block lift.  The new left and
right side cells are exactly `P_epsilon` and `S_epsilon`.  A cell trimming
both blocks is phase common because

\[
                       L_0\cup R_0=L_1\cup R_1.         \tag{1.6}
\]

Consequently the local packet has no unlisted phase-exclusive set value.
Its `2d-2` typed ray targets have pairwise distinct literal cells, giving a
diagonal matching.

## 2. Reconciliation with antitone birail Hall

For the canonical two-ray task bank the two threshold marginals are

\[
       \{0^{d-1},1,\ldots,d-1\}
       \quad\hbox{on each shore}.                         \tag{2.1}
\]

Thus

\[
 N=2d-2,qquad E_L=E_R=d-1,qquad
                 (E_L+E_R-N)_+=0.                       \tag{2.2}
\]

The antitone-birail theorem proves that the abstract freely pairable
threshold system has optimum deficiency zero.  The two-host packet is
stronger locally: its occurrence labels already exhibit one integral
zero-defect matching.  No threshold-pairing existence assumption is needed
for these `2d-2` cells.

This diagonal does not by itself close an ambient compiler.  Fix a shared
cap/boundary state `theta`.  Let `M_(P,epsilon)^theta` be the transversal
matroid on the full target bank `L` induced by the packet cells, and let
`M_(B,epsilon)^theta` be the transversal matroid induced by all remaining
legal cells.  Exact phase-`epsilon` completion is equivalent to

\[
 r_{M_{P,\epsilon}^\theta}(Y)+r_{M_{B,\epsilon}^\theta}(Y)
                         \ge |Y|\qquad(Y\subseteq L).    \tag{2.3}
\]

For a terminal state required to support both phases, the exact joint
condition is that one compatible common boundary state `theta` satisfy
(2.3) for both `epsilon=0,1`.

If the diagonal ray edges are fixed and their target set is
`R_epsilon=P_epsilon dotcup S_epsilon`, (2.3) reduces to ordinary residual
Hall:

\[
 |N_{B,\epsilon}^\theta(Y)|\ge |Y|
        \qquad(Y\subseteq L\setminus R_\epsilon).       \tag{2.4}
\]

Equations (2.3)--(2.4) are necessary and sufficient.  They include cap,
deadline and cell-competition effects through the literal legal cell bank;
the scalar equality (2.2) does not.

## 3. The upper-exact obstruction

The upper-support-safe folded opening has `8d+23` physical Johnson edges.
Its upper-union counter is (0.2), so

\[
 r_{\mathrm{upper}}(P)=16,
 \qquad |P|-r_{\mathrm{upper}}(P)=8d+7.                 \tag{3.1}
\]

Therefore no exact upper-rainbow Catalan forest can contain this whole
path.  Contracting `P` in the upper partition matroid is illegal.  On the
aligned ray-address face the cut retains only fifteen upper labels, giving
rank `15` and nullity `8d+8`.

The load formula is not inferred from the total alone.  At `d=2`, direct
classification gives eight singleton upper classes and eight classes of
load four.  Increasing `d` by one extends each filler rail by exactly one
edge in each of the latter eight classes; it does not change the sixteen
binary decisions or the singleton classes.  Hence a complete folded cycle
has `1^8(d+2)^8`, and deleting a support-safe edge gives (0.2), for every
depth for which this folded signature is used.  The independent replay
below reconstructs the choice problem without importing the primary folded
enumerator and verifies the classification through `d=12`.

At the `m=9,d=6` calibration the path has 71 edges but upper-partition rank
16, so at least 55 packet edges must be replaced before it can lie in an
upper-exact forest.

Support-only upper coverage is not logically impossible for the original
contiguous-OR problem: repeated immediate upper witnesses can coexist with
other, longer witnesses.  But that route has left the upper-exact forest
polytope.  It must add every missing global upper obligation to the literal
target--cell graph and prove (2.3) for that enlarged target bank.  Neither
the typed ray diagonal nor the antitone lower Hall theorem supplies this
upper matching.

## 4. Exact finite cut and source-host audit

For every `2<=d<=12`, exhaustive enumeration of the folded catalogue gives
three distinct faces.

\[
\begin{array}{c|c|c|c}
\text{face}&\text{graded }L^1&\text{upper support}&
 \text{phase ray addresses}\\ \hline
\text{global minimum}&6d+4&15&\text{displaced by }4d+12\\
\text{aligned}&10d+12&15&\text{aligned}\\
\text{upper safe}&10d+20&16&\text{displaced by }4d+12.
\end{array}                                               \tag{4.1}
\]

Thus the summary value `6d+4` belongs to the nonaligned global minimum; it
is not the aligned-row value.  On all three faces, no maximal-inverse source
letter contains `X_L`, `X_R`, or their merged one-host union.  The hosts are
genuinely planted, not native source letters.

For the aligned pair, adjoining the opposite two-host packet closes the
set-valued source support, but not the graded occurrence history.  The
remaining graded `L1` distance is

\[
                             6d+16,                     \tag{4.2}
\]

with one positive and one negative unit at each width
`2d+5,...,5d+12`.  Common boundary screens equalize complete prefix and
suffix unions but do not remove (4.2).  Hence support equality cannot be
used as a matching-closed common-cap certificate; the residual
occurrence-labelled rows must pass (2.3).

## 5. Scope and provenance

Proved here, using independently replayed frozen artifacts:

* exact one-host contraction/rays and the all-`d` internal-flat no-go;
* exact two-host support/common-cap/diagonal-Hall closure;
* reconciliation with the zero antitone-birail optimum;
* exact matroid-union and forced-diagonal residual-Hall criteria;
* exact upper partition rank/nullity obstruction; and
* the finite `2<=d<=12` cut/host tradeoff.

Not proved: owner-legal host planting, a common deadline realization,
global upper completion outside the exact-forest face, regenerative
contraction, or `nu(k)<=B(k)+O(1)`.

Primary replays and payloads:

```text
scratch/audit_ad_octagon_folded_two_ray_twohost_closure_20260801.py
  replay PASS_AD_OCTAGON_FOLDED_TWO_RAY_TWOHOST_CLOSURE
  payload 21133ca4560fb7da32822b7795e471e7a44ad09282e5951e65504d348850f872

scratch/audit_ad_quotient_fold_two_ray_deadline_gate_20260801.py
  replay PASS_AD_QUOTIENT_FOLD_TWO_RAY_COMMON_HOST_DEADLINE_GATE
  payload 3b98567d8f5276b59339e96c1d83975397fdb822fc59dd8f6deb54e3421623f3

scratch/audit_h2_c8_folded_two_ray_graded_context_gate_20260801.py
  replay PASS_H2_C8_FOLDED_TWO_RAY_GRADED_CONTEXT_GATE
  payload acd6af741dfebbfc1d20f102a4506bf77bbf4e08157249bf89ff6352e36d6ce2

scratch/audit_ha_c8_folded_commoncap_upper_gate_20260801.py
  replay PASS_HA_C8_FOLDED_COMMONCAP_UPPER_GATE
  payload f7ded23a4891abca86212daba56b8ada3499b5e22bc18f1f6aecf87b6a6f0820

scratch/audit_ha_c8_folded_upper_partition_20260801.py
  replay PASS_HA_C8_FOLDED_UPPER_PARTITION_SCOPE
  payload a72be931e66163b5def00d9f2a793fc74257be890a95ebabef3c445c4b571b77
```

The common-cap/cut-tradeoff replay's script and JSON SHA-256 values are
`3db6fc3c6d2b452d162d05d64059a430df2267d93a009fb6b1c7dcdd6cbf58fc`
and
`17eb24239e21dcb61633a7410d93b0dd3a670f0e9163f0fc3ade34a0254d592a`.

The last replay is the independent upper-row audit.  Its frozen script and
JSON SHA-256 values are respectively
`b5970fa69ac753c7ca1385420fcf835a512b9ef6cc9466d24284dea6e4e6e402`
and
`cae98936e9c5548c9a5abe528d5f9758052756441e126e28c928f88d73da9e3f`.
