# Rooted rotor openings require, and admit, a sharp depth-sized residence collar

**Date:** 2026-08-05  
**Method:** exact run-fragment calculus and explicit safe-coordinate Johnson
geodesics; no computation or search  
**Status:** unconditional local opening theorem and sharp collar-length
obstruction.  No edge of the cyclic-window shield rotor is intrinsically
safe to open at growing depth.  A `d`-owner collar on each exposed side is
necessary and an explicit doubly-rainbow collar exists when `m>=2d+1`.
The collar transports all rotor residence debt to one nested external state
interface.  Matching that interface to four named PBBS bodies and the typed
common cap remains open.

## 1. Opening the rotor

Use the cyclic-window rotor on

\[
 \Omega=\{z_0,\ldots,z_{2m-2}\},
 \qquad
 T_i=\{z_i,\ldots,z_{i+m-1}\},                            \tag{1.1}
\]

with indices modulo `2m-1`.  Open the owner edge

\[
                         T_{2m-2}T_0.                       \tag{1.2}
\]

Every other opening is a coordinate rotation of this one.

For `0<=a<=m-2`, coordinate `z_a` has a positive rotor run crossing
(1.2).  In the resulting linear path its left and right fragments have
lengths

\[
                         a+1,\qquad m-1-a.                 \tag{1.3}
\]

Coordinates `z_m,...,z_(2m-2)` have the complementary zero-gap fragments.

### Theorem 1.1 (no bare residence-safe opening)

For every rotor edge and every `d>=1`, opening that edge without controlling
external owner positions creates both a positive fragment and a zero
fragment of length one.  More precisely, at the left endpoint `T_0` the
vulnerable banks are

\[
 P_L=\{z_0,\ldots,z_{d-1}\},
 \qquad
 Q_L=\{z_m,\ldots,z_{m+d-1}\},                            \tag{1.4}
\]

where the coordinates in `P_L` must remain present and those in `Q_L` must
remain absent in a nested collection of preceding positions.  At the right
endpoint `T_(2m-2)` they are

\[
 P_R=\{z_{m-1-d},\ldots,z_{m-2}\},
 \qquad
 Q_R=\{z_{2m-2-d},\ldots,z_{2m-3}\}.                      \tag{1.5}
\]

Any universally residence-safe interface must control at least `d` owner
positions on each exposed side.

#### Proof

Formula (1.3) follows by cutting the cyclic positive run
`a-m+1,...,a`.  At the left endpoint, the positive fragment of `z_a` has
length `a+1`, so for `a<d` it needs `d-a` preceding owners which also
contain `z_a`.  The zero prefix of `z_(m+b)` has length `b+1`, so for
`b<d` it needs `d-b` preceding owners omitting that coordinate.  This gives
(1.4).  Reversing the calculation at the right endpoint gives (1.5).

In particular `z_0` has positive left fragment length one.  Reaching the
floor `d+1` requires the `d` immediately preceding owners to contain it.
The corresponding first zero fragment gives the dual assertion.  Thus no
collar controlling fewer than `d` external owner positions can be safe for
all attachments.  Rotation gives the statement at every rotor edge.
\(\square\)

The exact nested left requirements are: at the `t`th owner before `T_0`,
`1<=t<=d`, contain `z_0,...,z_(d-t)` and omit
`z_m,...,z_(m+d-t)`.  The displayed full banks (1.4) are a stronger
time-independent sufficient interface.  The right requirements are the
reversed analogues.

## 2. A sharp incoming collar

Put `E=T_0`.  Assume

\[
                              m\ge2d+1.                     \tag{2.1}
\]

Choose distinct

\[
 u_1,\ldots,u_d\in E\setminus P_L,
 \qquad
 v_1,\ldots,v_d\in\Omega\setminus(E\cup Q_L).             \tag{2.2}
\]

The supply sizes are `m-d` and `m-1-d`, so (2.1) suffices.  Define

\[
 S_j=E-\{u_{j+1},\ldots,u_d\}
        +\{v_{j+1},\ldots,v_d\},
 \qquad0\le j\le d.                                      \tag{2.3}
\]

Thus `S_d=E`, and transition `j` replaces `v_(j+1)` by `u_(j+1)`.

### Theorem 2.1 (sharp left residence collar)

The owner path

\[
                         S_0,S_1,\ldots,S_d=T_0            \tag{2.4}
\]

is simple and doubly q1-rainbow.  Every collar owner contains `P_L` and
omits `Q_L`; consequently every positive and zero rotor fragment clipped at
the left opening reaches length at least `d+1` after (2.4) is attached.

The only residence obligations exported at the outer endpoint `S_0` are
the ordered pairs `(u_i,v_i)`: the preceding body must omit `u_i` and
contain `v_i` for at least `d+1-i` further owner positions.

#### Proof

Equation (2.3) gives rank `m` and one Johnson exchange at every step.
The lower colour at step `j` is obtained by deleting both active elements
`u_(j+1),v_(j+1)` from the corresponding union, and the upper colour by
including both.  The prefix/suffix index recovers `j`, so both palettes are
simple.  Different owners are immediate from the strictly increasing set of
restored `u` coordinates.

The choices (2.2) leave every member of `P_L` fixed present and every member
of `Q_L` fixed absent for all `d` collar positions preceding `T_0`.
Theorem 1.1 then proves the rotor-fragment claim.

Coordinate `u_i` is absent in `S_0,...,S_(i-1)` and enters at `S_i`;
coordinate `v_i` is present in those same owners and leaves at `S_i`.
Their inner runs continue safely into the rotor because the `u_i` are chosen
outside the vulnerable prefix bank and the `v_i` outside the vulnerable
zero bank.  At the outer boundary, their length-`i` zero and positive
fragments require exactly `d+1-i` further matching states.  No other new
collar transition is exposed there.  \(\square\)

## 3. The right collar

The reversed construction is literal.  Put `E'=T_(2m-2)`, choose

\[
 u'_1,\ldots,u'_d\in E'\setminus P_R,
 \qquad
 v'_1,\ldots,v'_d\in\Omega\setminus(E'\cup Q_R),          \tag{3.1}
\]

and set

\[
 R_j=E'-\{u'_1,\ldots,u'_j\}
          +\{v'_1,\ldots,v'_j\},
 \qquad0\le j\le d.                                      \tag{3.2}
\]

Then `E'=R_0,...,R_d` is a simple doubly-rainbow outgoing collar.  It keeps
`P_R` present and `Q_R` absent through the next `d` owners.  At `R_d` it
exports the reversed nested interface: the following body must keep
`u'_i` absent and `v'_i` present for the remaining number of positions
required by the run beginning at step `i`.

Together, Sections 2--3 prove that the sharp lower bound of `d` controlled
owner positions per exposed side is attained for repairing all fragments
inherited from the rotor.  The newly created geodesic transitions are
exported in the explicit nested outer interface rather than silently closed.

## 4. Resource planting

One shield together with one depth-sized seam collar has `O(m+d)=O(m)`
owner/incidence length.  A fixed lower facet lies under at most two owners
of each geodesic segment, and a fixed owner contains at most two lower
colours from each segment.  Thus a fixed bank of shield--collar interfaces
has constant lower-star and forced-facet exposure and total protected size
`O(m)`.

The proof of

`MATH_THEOREM_FIXED_SHARP_SHIELD_BANK_EXTENDS_TO_MIDDLE_LEVELS_TWO_FACTOR_20260805.md`

therefore applies with a larger constant depending only on the number of
segments.  For all sufficiently large `m`, any fixed prospective bank of
pairwise resource-disjoint shield--collar paths extends to one unrooted
spanning owner/lower-q1 two-factor.

This statement selects the paths prospectively.  It does not force their
outer exported states to occur at prescribed PBBS endpoints.

## 5. Combination with the adaptive `C8`

Suppose four PBBS continuation arcs are supplied with the following rooted
data.

1. Each oriented cut side contains a sharp full-union shield.
2. Each exposed shield endpoint has the depth-`d` collar above.
3. The named PBBS body realizes the collar's exported nested pair state.
4. The two protected opposite-role paths are attached to the two intended
   bodies.

Then:

* the full-union localization theorem reduces every exterior upper casualty
  to the finite quadratic cut collars;
* Sections 1--3 preserve positive and zero residence through every opened
  rotor seam;
* Section 4 supplies owner-once and lower-q1-exact unrooted completion; and
* the adaptive-phase theorem for the common-history `C8` chooses the old
  phase if the two protected paths already share a component and the toggled
  phase otherwise, fusing them with zero positional charge.

The remaining theorem is now precisely the **rooted state realization** in
item 3, together with simultaneous packing of the localized upper backups
and the typed common-cap/lower-compiler routes.  The shield, collar length,
local residence, q1 resources, and adaptive local topology introduce no
further obstruction.

## 6. Scope

Proved:

1. every bare rotor opening has a short-run defect;
2. `d` controlled owner positions per side are necessary;
3. an explicit `d`-step doubly-rainbow collar attains that bound and exports
   one nested state interface; and
4. fixed many prospectively chosen shield--collar paths are compatible with
   unrooted q1 factor extension.

Open:

1. occurrence of the exported nested state at named PBBS body endpoints;
2. one literal source chronology through all rooted joins;
3. the localized exterior backup bank in the same factor; and
4. the terminal typed common cap and lower compiler.
