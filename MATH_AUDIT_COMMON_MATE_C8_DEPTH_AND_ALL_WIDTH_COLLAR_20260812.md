# Audit of the depth and all-width common-mate `C8` collars

**Date:** 2026-08-12
**Audited source:**
`MATH_THEOREM_COMMON_MATE_C8_ONE_STEP_COLLAR_Q2_Q3_ZERO_ODD_SOCKET_20260812.md`,
Sections 6--7
**Verdict:** **PASS after two exact scope clarifications.**  The prefix-union
identities, Johnson simplicity, full-union shield, socket action, and
incidence counts are correct.  At fixed middle-levels parameter `m`, the
depth must satisfy `H<=m-3`; the source formerly said only `H>=1`.  The
original one-step successor is reused as `z_1=z`, rather than consuming an
additional ground coordinate.

## 1. Available labels and the corrected range

The ground set has size `2m-1`.  After the original successor `z` is
reclassified as the first neutral label, the fixed nonneutral labels occupy

\[
 |C|+|\{q_0,q_1,q_2,q_3,c\}|=(m-3)+5=m+2
\]

positions.  Exactly

\[
 (2m-1)-(m+2)=m-3
\]

neutral-label positions remain outside those fixed labels.  One of them is
the already chosen successor `z`.  Therefore the family

\[
 z_0=c,z_1=z,z_2,\ldots,z_H
\]

exists on this ground set precisely in the claimed positive range

\[
 1\le H\le m-3.
\]

The identification `z_1=z` is load-bearing for this exact count: if all
`z_j` were required to be new in addition to the original `z`, the maximum
would instead be `H=m-4`.  The source now explicitly reuses the old
successor, so `H=1` is literally the original collar.  The range restriction
has been inserted into (6.1a) and Theorem 6.1.  It
does not affect the intended deadline choice `H=d(k)=o(m)` or the all-width
choice `H=m-3`.

## 2. Exact audit of Theorem 6.1

Recall

\[
 R_i=C+q_i+q_{i+1}+q_{i+2},\qquad
 U_i=C+c+q_i+q_{i+1},
\]

and

\[
 W_{i,j}=C+q_{i+1}+z_{j-1}+z_j.
\]

Every displayed owner has rank `m`.  The step from `U_i` to `W_(i,1)`
exchanges `q_i` for `z_1`; its lower facet is

\[
 C+c+q_{i+1}.
\]

The step from `W_(i,j)` to `W_(i,j+1)` exchanges `z_(j-1)` for
`z_(j+1)`; its lower facet is

\[
 C+q_{i+1}+z_j.
\]

These facets are distinct because the `z_j` are distinct, and facets on
different rails contain different active labels `q_(i+1)`.

### Prefix identity

For `0<=j<=H`, direct union gives

\[
 R_i\cup U_i\cup W_{i,1}\cup\cdots\cup W_{i,j}
 =C+c+q_i+q_{i+1}+q_{i+2}+\{z_1,\ldots,z_j\}
 =T_i+\{z_1,\ldots,z_j\}.
\]

For the rethreaded output rail,

\[
 R_i\cup U_{i+1}
 =C+c+q_i+q_{i+1}+q_{i+2}=T_i,
\]

and every `W_(i+1,t)` adds only `z_(t-1),z_t` and the already present
active coordinate `q_(i+2)`.  Hence the corresponding prefix has the same
union.  No active or core label is missing from (6.5)--(6.6); in
particular, the first neutral cell uses `z_0=c`.

An owner window of width `w<=H+2` crossing a switched incidence contains
`R_i` followed by at most `H+1` output owners, namely `U` and at most all
`H` neutral owners.  The rest is an unchanged incoming suffix.  The prefix
identity therefore preserves the window union occurrence-by-occurrence.
The output rail is shifted from index `i` to `i+1`, so the endpoint action
is exactly

\[
 R_i\longmapsto W_{i+1,H}.
\]

### Exact incidence count

For one path there are `H+2` upper owners

\[
 R_i,U_i,W_{i,1},\ldots,W_{i,H},
\]

and hence `H+1` Johnson transitions.  Each transition is two selected
middle-levels incidences.  Thus one path uses `2H+2` selected incidences,
and four paths use

\[
 4(2H+2)=8H+8.
\]

Adding four forbidden `C8` incidences and the stated `72`-incidence private
connector allowance gives `8H+84`, exactly as in (6.8).

## 3. Exact audit of Theorem 7.1

Here

\[
 H=m-3,\qquad
 Z=[2m-1]\setminus(C\cup\{q_0,q_1,q_2,q_3,c\}).
\]

The auxiliary choices in (7.3) are possible once `m>=9`: four distinct
`t_i` require `|C|>=4`, while four distinct `d_i` outside
`{z_(H-1),z_H}` require `H-2>=4`.

### Johnson and palette simplicity

Each bridge owner has rank `m`.  The three bridge transitions exchange,
respectively,

\[
 t_i\leftrightarrow d_i,\qquad
 z_{H-1}\leftrightarrow\alpha_i,\qquad
 z_H\leftrightarrow\beta_i.
\]

Their lower facets are exactly the three sets in (7.4).  For fixed `i`
they are distinct by their noncore labels.  For `i!=j`, every facet of
bridge `i` omits `t_i` but contains `t_j`, whereas every facet of bridge
`j` omits `t_j` but contains `t_i`.  A neutral-rail facet contains all of
`C`, so it cannot equal a bridge facet.  The same missing-core signature
separates bridge owners from neutral owners and from bridges with another
index.  This proves both owner and lower-palette simplicity in the old and
rethreaded paths.

### Bridge prefix identity

After the complete neutral rail, the common accumulated union at incoming
socket `R_i` is

\[
 B_i=T_i\cup Z.
\]

The first bridge owner adds no new coordinate: its deleted `t_i` and tag
`d_i` already lie in `C` and `Z`.  The only active coordinate absent from
`B_i` is

\[
 \mu_i=q_{i+3}.
\]

The active pair on output rail `i` is

\[
 \{q_{i+2},q_{i+3}\},
\]

while that on output rail `i+1` is

\[
 \{q_{i+3},q_i\}.
\]

Their common member is `mu_i`.  If its global index is even, it is
`alpha` in both rails and appears at `G_2`; if its index is odd, it is
`beta` in both rails and appears at `F`.  The other active label at each
stage already belongs to `T_i`.  Thus the prefix unions agree after each
of `G_1,G_2,F`, not merely at the end of the bridge.

### Full-union shield and all widths

The outgoing collar on rail `i` contains:

* all of `C` and `c` from `U_i`;
* every label of `Z` from the complete neutral rail;
* `q_i,q_(i+1)` from `U_i`; and
* `q_(i+2),q_(i+3)` from the bridge.

Its union is therefore exactly

\[
 C\cup Z\cup\{q_0,q_1,q_2,q_3,c\}=[2m-1].
\]

A crossing interval ending inside the collar is preserved by the prefix
identity.  A crossing interval extending past the collar contains this
full-union shield and hence has value `[2m-1]` in both phases.  An interval
not crossing a switched incidence is copied literally.  This proves the
all-width claim, including intervals long enough to traverse a later local
cut.

The complete output collar is transported from index `i` to `i+1`, so the
socket action remains the odd cycle

\[
 R_i\longmapsto F_{i+1}.
\]

### Exact `8m+8` count

One complete old path has the upper owners

\[
 R_i,\ U_i,\ W_{i,1},\ldots,W_{i,H},\ G_{i,1},G_{i,2},F_i.
\]

There are `H+5=m+2` owners and therefore `H+4=m+1` Johnson transitions.
Each transition contributes two selected incidences, so one path contributes
`2m+2`, and all four contribute

\[
 4(2m+2)=8m+8.
\]

The outgoing collar alone has

\[
 1+H+3=m+1
\]

owners, agreeing with (7.8).

## 4. Counterexample search and final scope

There is no counterexample within the admissible symbolic range.  The only
small-parameter failure is definitional:

* Section 6 cannot choose more than `m-3` neutral `z` labels, including the
  reused original successor `z_1=z`.
* Section 7 cannot choose the four private `d_i` until `m>=9`.

The first issue and the original-successor identification were genuine
missing scope statements and have been patched.  The second is already
covered by “for all sufficiently large `m`.”  No active, core, neutral,
bridge, or socket label is missing from the identities, and no further
correction is required.
