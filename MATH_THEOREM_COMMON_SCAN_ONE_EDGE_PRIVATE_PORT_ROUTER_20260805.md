# A common scan turns rooted receiver squares into a one-edge private port router

**Date:** 2026-08-05  
**Method:** literal capacity-two receiver squares, one-row coordinate scans,
and the regular factor-router flow theorem; no computation  
**Status:** unconditional suffix-router theorem in the compatible even
labelled sector.  It removes the full active-port gammoid premise once the
gain-to-port prefixes have been planted privately.  It does not construct
those prefixes, does not treat the odd hook sector, and does not by itself
plant the receiver bank in the global PBBS parent.

## 1. Literal square convention

Use the direct even receiver bank from
`MATH_THEOREM_COMMON_SCAN_ROOT_CODED_RECEIVER_EXTENSION_AND_ODD_CURRENT_OBSTRUCTION_20260805.md`.
For every task `f`, it gives four distinct capacity-two states

\[
             v^f_{00},\quad v^f_{10},\quad
             v^f_{01},\quad v^f_{11}.                    \tag{1.1}
\]

The first bit is carried by one fixed coordinate pair `p_0`; changing that
bit is the same local edge

\[
                              12\longleftrightarrow21       \tag{1.2}
\]

on `p_0`.  The second bit is carried by a disjoint pair `p_1`.  Fixed-weight
root codes make the squares belonging to different tasks vertex-disjoint.

Define two ports and two terminal states per task by

\[
 p_f^0=v^f_{00},\qquad p_f^1=v^f_{01},\qquad
 t_f^0=v^f_{10},\qquad t_f^1=v^f_{11}.                  \tag{1.3}
\]

Thus

\[
                 p_f^\beta t_f^\beta\qquad(\beta=0,1)    \tag{1.4}
\]

is always one contextual copy of (1.2).

## 2. Simultaneous one-edge suffixes

### Theorem 2.1 (common-scan port router)

All `2q` edges in (1.4), over every task `f`, belong to one perfect
matching of the compatible even labelled capacity-two sector.  In
particular, the directed one-edge paths

\[
                    R_{p_f^\beta}:p_f^\beta\longrightarrow t_f^\beta
                                                                    \tag{2.1}
\]

are pairwise vertex-disjoint and have pairwise distinct sinks.

#### Proof

Put `p_0` first in the coordinate scan.  The endpoints of every edge in
(1.4) agree away from `p_0`, while their restriction to `p_0` is (1.2).
The one-row common-base theorem therefore puts all these edges in one scan
perfect matching.  A matching has disjoint edges, and the literal root
codes already separate distinct contextual squares.  Orient every selected
edge from its `0` endpoint to its `1` endpoint.  This gives (2.1).  \(\square\)

The conclusion is stronger than individual port linkability: it is the
full simultaneous typed suffix linkage required by the private
factor-router theorem, with suffix length one.

## 3. Gain routing with private prefixes

Let `G={g_f:f in F}` be gain claims in one fully materialized cap/guard
state.  Suppose that for every `f` there are directed literal prefixes

\[
 Q_f^0:s_{g_f}\leadsto p_f^0,
 \qquad
 Q_f^1:s_{g_f}\leadsto p_f^1                         \tag{3.1}
\]

satisfying the following exact conditions.

1. Prefix interiors belonging to different `(f,beta)` are physically
   disjoint.  The two prefixes of one claim may share only their claim
   start.
2. No prefix interior meets a port or scan edge in (2.1), except at its
   own terminal port.
3. Prefixes and scan edges avoid the fixed compensation linkage and every
   previously reserved unit capacity.
4. Both `t_f^0,t_f^1` have a terminal type legal for `g_f` in the same
   occurrence state.

### Theorem 3.1 (two-port private routing)

Under these hypotheses all gain claims have pairwise vertex-disjoint
directed paths to distinct legal sinks, simultaneously with the fixed
compensation linkage.

#### Proof

Take the incidence graph with left shore `G`, right shore

\[
                         P=\{p_f^0,p_f^1:f\in F\},        \tag{3.2}
\]

and incidences `g_f p_f^0,g_f p_f^1`.  Every left degree is two and every
right degree is one.  The paths (3.1) are private incidence prefixes and
Theorem 2.1 supplies simultaneous private suffixes.  All state, capacity,
and type hypotheses of the regular factor-router theorem hold with `h=2`.
Its uniform half-flow and integral max-flow rounding give one route for
every gain.  \(\square\)

There is also a direct proof: send one half-unit down each of the two
prefix-plus-scan paths of a claim.  A port and its scan edge carry only one
half-unit because they belong to one task.  Integral max flow rounds this
value-`|G|` flow.

## 4. Relation to the former gammoid gate

Let `Gamma_suf^type` be the active-port strict gammoid from
`MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`.
Theorem 2.1 gives the literal certificate

\[
                      r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|           \tag{4.1}
\]

without checking any cut: the paths (2.1) themselves witness full rank.
Consequently, **for this co-designed even bank**, the old all-cut suffix
router premise is no longer an independent theorem.  It is discharged by
the common scan.

This is a quantifier change.  It does not assert that an arbitrary frozen
port bank has full gammoid rank.  The ports are selected together with the
scan base so that (4.1) is literal.

## 5. Quotient and forbidden-colour scope

The result descends verbatim in an aperiodic background sector.  The
finite merged-colour avoidance theorem may choose that background so that
no scan edge has any colour from a fixed forbidden reset bank, provided
the background mass is sufficiently large.  This removes a fixed family
of colour collisions, but it does not certify disjointness from an
arbitrary adaptive prefix or compensation linkage.  Conditions 1--3 of
Section 3 must still be proved by the parent construction.

## 6. Exact remaining interface

In the compatible even sector the common-cap router has therefore reduced
from

\[
 \text{abstract factor}+\text{all active-port gammoid cuts}
\]

to the following literal planting statement:

> **Private two-prefix planting.**  Plant one root-coded receiver square
> per gain and two private gain-to-square prefixes in the same PBBS/cap
> state, avoiding the fixed compensation linkage and carrying legal
> terminal type.

Once this is done, Theorem 3.1 completes every gain automatically.  The
remaining separate obstruction is the odd hook sector: a fixed receiver
bank and one socket leave the macroscopic wrap-current deficiency
`Delta_(m,R)-O(1)`, so the even common scan cannot be cited there.

## 7. Dependencies and nonclaims

Used:

1. the direct parallel receiver bank and one-row scan theorem in
   `MATH_THEOREM_COMMON_SCAN_ROOT_CODED_RECEIVER_EXTENSION_AND_ODD_CURRENT_OBSTRUCTION_20260805.md`;
2. the private factor-router theorem in
   `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`.

Not proved here:

1. private prefix planting in the global parent;
2. compatibility with an adaptive compensation linkage;
3. the odd wrap/circulation-current construction;
4. regeneration of the aperiodic background and root code through all
   same-parity lifts; or
5. the full `B(k)+O(1)` theorem.
