# A universal `d`-step seasoning buffer joins arbitrary clipped tail paths

**Date:** 2026-08-06  
**Method:** Johnson-ball counting plus the exact clipped-connector interval
matching theorem; no computation or search  
**Status:** unconditional asymptotic residence and topology theorem.  Any
subexponential family of internally clipped rank-`m` paths can be joined in
an arbitrary cyclic order after giving each short path two explicit
`d`-step endpoint collars.  A fresh central `d`-step buffer at every seam
removes the false requirement that the two original endpoints themselves
be antipodal.  The theorem does not yet pack the new physical resources
against the fixed central bank.

## 1. A central owner far from two prescribed ports

Work in the Johnson graph

\[
                         J(2m-1,m).                 \tag{1.1}
\]

For a fixed owner `A`, the number of owners at Johnson distance at most
`rho m` is

\[
              \sum_{j\le \rho m}\binom mj\binom{m-1}j.       \tag{1.2}
\]

At `rho=1/3`, the logarithm of `(1.2)` is at most

\[
              2mH_2(1/3)+o(m)<2m-o(m),             \tag{1.3}
\]

whereas

\[
              \binom{2m-1}m=2^{2m-o(m)}.           \tag{1.4}
\]

### Lemma 1.1 (two-port far centre)

For every two rank-`m` owners `A,B` and all sufficiently large `m`, there
is a rank-`m` owner `C_0` such that

\[
                 d_J(A,C_0)>{m\over3},\qquad
                 d_J(B,C_0)>{m\over3}.             \tag{1.5}
\]

Moreover a uniformly random owner has this property with probability
`1-2^{-Omega(m)}`.

#### Proof

The union of the two radius-`m/3` balls has size at most twice `(1.2)`.
Equations `(1.3)`--`(1.4)` prove both assertions. \(\square\)

Choose arbitrary disjoint sets

\[
             D_C\subset C_0,qquad
             I_C\subset[2m-1]\setminus C_0,qquad
             |D_C|=|I_C|=d,                       \tag{1.6}
\]

and put

\[
                         C_d=C_0-D_C+I_C.           \tag{1.7}
\]

Order the two banks and swap them coordinatewise.  This gives a monotone
buffer

\[
                         H=(C_0,C_1,\ldots,C_d)      \tag{1.8}
\]

of exactly `d` transitions.  The triangle inequality gives

\[
 d_J(C_d,B)\ge d_J(C_0,B)-d>{m\over3}-d.          \tag{1.9}
\]

In particular, at the deadline scale `d=o(m)`, both distances

\[
                         d_J(A,C_0),\quad d_J(C_d,B)             \tag{1.10}
\]

are at least `3d`.

## 2. Universal seasoning-buffer connector

Let `P` be a rank-`m` path ending at `A`, and let `Q` be one beginning at
`B`.  Assume:

1. every positive run and zero gap wholly internal to `P` or `Q` has
   length at least `d+1`; and
2. `P` supplies at least `d` transitions before `A`, while `Q` supplies at
   least `d` transitions after `B`.

### Theorem 2.1 (two connectors plus one seasoning buffer)

For all sufficiently large `m`, there are monotone geodesics

\[
                         G^-:A\longrightarrow C_0,
 \qquad                  G^+:C_d\longrightarrow B                 \tag{2.1}
\]

such that

\[
                         P\,G^-\,H\,G^+\,Q          \tag{2.2}
\]

is positive- and zero-resident with deadline `d`.  The deletion and
insertion orders of `G^-` and `G^+` may be selected independently after
`P,Q,H` are fixed.

#### Proof

At seam `A -> C_0`, the left context is the final `d` transitions of `P`
and the right context is the complete `d`-transition buffer `H`.  By
Corollary 3.5 of
`MATH_THEOREM_CLIPPED_RESIDENCE_CONNECTOR_INTERVAL_MATCHING_20260806.md`,
each shore has at most `d` short histories at either endpoint.  Lemma 1.1
gives connector distance at least `3d`.  The sparse clipped-flag theorem
therefore supplies both interval SDRs and hence `G^-`.

At seam `C_d -> B`, use the same argument with `H` as the left context
and `Q` as the right context.  Equation `(1.9)` gives distance at least
`3d`, so it supplies `G^+`.  The two interval systems use disjoint
connectors and fixed contexts, proving independence of their choices.

A monotone path changes a coordinate at most once, so it has no run or gap
wholly internal to it.  A component meeting the `P/G^-` or `G^-/H` seam is
priced by the first interval theorem; one meeting `H/G^+` or `G^+/Q` is
priced by the second.  If a component crosses all of `H` without changing
there, it contains its `d+1` owners and is safe automatically.  These cases
exhaust `(2.2)`. \(\square\)

The role of `H` is not to carry a target.  It is a finite state reset: it
supplies `d` literal transitions of future context to the left connector
and `d` transitions of past context to the right connector.

## 3. Short paths always admit literal endpoint contexts

Let

\[
                         Q=(Q_0,\ldots,Q_\ell)       \tag{3.1}
\]

be a one-pass path whose transition support is disjoint from sets

\[
 D^-,D^+\subseteq Q_0\cap Q_\ell,
 \qquad
 I^-,I^+\subseteq[2m-1]\setminus(Q_0\cup Q_\ell), \tag{3.2}
\]

with all four sets pairwise disjoint and of size `d`.  Prepend the
monotone path

\[
                         Q_0-D^-+I^-\longrightarrow Q_0       \tag{3.3}
\]

and append

\[
                         Q_\ell\longrightarrow Q_\ell-D^++I^+. \tag{3.4}
\]

Exactly the same active-bank argument as in the rolling-collar theorem
shows that the thickened path is simple, has `d` transitions of context at
both endpoints, and has no short internal component.  Its original target
interval remains literally intact.

For the shortened low trace path with `|T|<=2d`,

\[
 |Q_0\cap Q_\ell|=m-\ell,
 \qquad
 |[2m-1]\setminus(Q_0\cup Q_\ell)|=m-1-\ell,      \tag{3.5}
\]

and `ell<=2d-1`.  Thus `(3.2)` exists once `m>=4d`.  This includes the
singleton auxiliary path (`ell=0`).

All remaining tail paths in the hybrid common-core reservoir already have
at least `d` monotone transitions at both ends and no short internal
component: shortened large-trace paths use one-pass consecutive windows,
and the extreme high paths are monotone geodesics.  They need no added
collar.

## 4. Tail chronology without complement pairing

Let `R_tail^o` be the `2^{o(m)}` family of paths `Q_T` with tail trace
`T` from
`MATH_THEOREM_ANTIPODAL_RESERVOIR_SUBSTITUTION_AND_TAIL_ONLY_LEAVE_20260806.md`.
The separate fixed hinge incidences `H` are not put into this cycle; they
remain in the protected hinge bank.
Replace every short member by its thickening from Section 3.  Order the
resulting paths arbitrarily and insert one seasoning-buffer connector from
Theorem 2.1 at every cyclic seam.

### Corollary 4.1 (abstract resident tail cycle)

For all sufficiently large `m`, the tail witness paths lie on one abstract
cyclic chronology in which every positive run and zero gap has
length at least `d+1`.  Every old tail target occurrence remains a
contiguous internal interval.  The added role count is

\[
                         O(m)|R_{tail}^{\circ}|=2^{o(m)}.    \tag{4.1}
\]

#### Proof

Apply Theorem 2.1 independently at every seam.  Each of its two monotone
connectors and its buffer is simple separately.  At this stage neither
cross-piece repetitions inside one seam macro nor collisions between
different seams are excluded; the full resource packing is the next gate.
Residence is seam-local and therefore holds around the entire
cycle.  Each old target interval lies strictly inside its retained path.
There are `2^{o(m)}` paths and every new connector has at most `m`
transitions. \(\square\)

The qualifier "abstract" is essential in Corollary 4.1: different local
macros can still collide in owners or immediate palettes.  The theorem
closes the endpoint-distance and residence quantifiers without making a
premature packing claim.

## 5. Linear free aperture

Use the explicit three-zone orders of Theorem 3.6 in the clipped-connector
note.  On each of `G^-` and `G^+`, at most `3d` positions on either shore
are fixed.  Since the connector distances in `(1.10)` are at least
`m/3-d`, each connector retains

\[
                         q_0\ge {m\over3}-4d=\Omega(m)          \tag{5.1}
\]

independently permutable deletion labels and the same number of insertion
labels.  Conditional owner and immediate-palette point probabilities in
that free block are exactly

\[
 {1\over\binom{q_0}s^2},
 \qquad
 {1\over\binom{q_0}s\binom{q_0}{s+1}},            \tag{5.2}
\]

as in the central antipodal aperture theorem.

The remaining resource statement is now sharply separated:

> **Subexponential buffer packing.**  Choose the `C_0`, the `d`-step
> buffers, and the two free connector orders at all tail seams so their
> owner/lower/upper Ore halos avoid the fixed central bank and one another.

The tail family has `2^{o(m)}` macros, and every connector has a linear
free middle.  What is not automatic is the endpoint star: a fixed tail
port may have every first palette ticket blocked by only `O(m)` fixed
roles.  The fixed protected construction must therefore reserve one full
first-step star at each tail port, or the port itself must remain a packing
variable.

## 6. Scope

Proved:

1. arbitrary clipped tail paths can be connected without complement
   pairing;
2. every seam has an explicit finite seasoning buffer and two legal
   interval-SDR connectors;
3. global positive/zero residence and one abstract tail cycle;
4. only `2^{o(m)}` added roles; and
5. a linear conditional random aperture in every long connector.

Not proved:

1. physical owner/lower/upper or Ore-halo privacy across tail macros;
2. attachment of the tail cycle to the central protected chronology;
3. PBBS all-width occurrence preservation; or
4. terminal common-cap transport and `nu(k)<=B(k)+O(1)`.
