# A root-coded three-bit cube is a complete private common-cap router

**Date:** 2026-08-05  
**Method:** an explicit Boolean cube inside one even-coordinate,
odd-mass capacity-two sector; no computation  
**Status:** unconditional literal prefix-and-suffix router in every labelled
cycle with room for the displayed disjoint pairs, and in rooted quotient
sectors.  One cube gives one unit gain
two private ports and two parallel one-edge terminal suffixes.  A fixed
bank of cubes is mutually private.  This closes the physical router itself
once the global construction identifies its gain sources and terminal
type with these cube roles.  In an even-coordinate odd-mass sector the
suffix bank additionally lies in one scan perfect matching.  The router
does not require that completion.  The theorem does not prove a guarded
PBBS planting or regenerative role identification.

## 1. The cube bank

Let a capacity-two coordinate cycle contain `s+3` pairwise disjoint
adjacent coordinate pairs.  Reserve three of them as

\[
                              p_0,p_1,p_2.                \tag{1.1}
\]

On any active pair encode a bit by

\[
                     0\longleftrightarrow12,
                     \qquad 1\longleftrightarrow21.       \tag{1.2}
\]

Both states have local mass three, and changing the bit is one legal
adjacent-transfer edge.

Use the other `s` pairs as code pairs.  Choose fixed-weight codewords

\[
 c_f\in\{0,1\}^s,qquad |c_f|=w,qquad
                    f\in F,\quad |F|\le {s\choose w}.     \tag{1.3}
\]

On code pair `j` put `22` if `c_f(j)=1` and `00` otherwise.  Put one common
fixed even-mass filler on every unused pair.  For every
`(a,b,c) in {0,1}^3`, let `v^f_(abc)` be the state using bits `a,b,c` on
`p_0,p_1,p_2` and code `c_f`.

Every vertex in every cube has the same odd mass

\[
                             R=9+4w+R_0,                 \tag{1.4}
\]

where `R_0` is the common filler mass.  Distinct codewords give disjoint
literal cubes.  The construction itself does not depend on the parity of
the coordinate-cycle length.  When the cycle length is even and the desired
sector mass is odd, choose `R_0` even.

## 2. Source, ports, and sinks

For task `f` define

\[
\begin{aligned}
 s_f&=v^f_{000},\\
 p_f^0&=v^f_{100},& p_f^1&=v^f_{010},\\
 t_f^0&=v^f_{101},& t_f^1&=v^f_{011}.
\end{aligned}                                            \tag{2.1}
\]

There are two one-edge prefixes

\[
 Q_f^0:s_f\longrightarrow p_f^0\quad(p_0\text{ flip}),
 \qquad
 Q_f^1:s_f\longrightarrow p_f^1\quad(p_1\text{ flip}), \tag{2.2}
\]

and two one-edge suffixes

\[
 R_f^0:p_f^0\longrightarrow t_f^0,
 \qquad
 R_f^1:p_f^1\longrightarrow t_f^1,                      \tag{2.3}
\]

both of which flip `p_2`.

### Theorem 2.1 (literal complete private router)

The paths (2.2)--(2.3), over all tasks `f`, have the following properties.

1. Prefixes of different tasks are vertex-disjoint.  The two prefixes of
   one task share only their allowed unit source `s_f`.
2. All ports and sinks are distinct.
3. Prefix interiors are empty and meet no suffix except at their own port.
4. The `2|F|` suffix edges are a simultaneous literal linkage.  If the
   coordinate length is even and the total mass is odd, they additionally
   lie in one coordinate-scan perfect matching of the complete sector.

Consequently, if the two sinks of task `f` have a common terminal type
legal for the claim placed at `s_f`, every claim is simultaneously
routable to a distinct legal sink.

#### Proof

Inside one cube the five displayed vertices in (2.1) are distinct.
Different cubes have different fixed code-pair restrictions, so all their
vertices are disjoint.  This proves the first three assertions directly.

Every suffix changes only `p_2`, and on that pair is the identical local
edge `12-21`.  Literal cube disjointness already proves that all suffixes
are pairwise vertex-disjoint.  In the even-coordinate odd-mass case, put
`p_2` first in the coordinate scan.  The one-row scan theorem additionally
contains every contextual copy (2.3) in one perfect matching.

Finally, send one half-unit from `s_f` along each concatenation
`Q_f^beta R_f^beta`.  The source has total load one.  Every other physical
vertex lies in only one displayed concatenation and has load at most one
half.  Thus the network has a feasible flow of value `|F|`.  Integral
max-flow rounds it to one path from every source and to distinct sinks.
The terminal-type hypothesis makes every rounded choice legal.  \(\square\)

Because every prefix and suffix is one edge, there is no hidden interior
capacity and no full-port gammoid cut to check.

## 3. Fixed protected banks

Let `Z` be a fixed bank of forbidden literal vertices or unit edges in the
same labelled sector.  A forbidden literal vertex belongs to at most one
code cube, since its code-pair restriction determines `c_f`.  A forbidden
edge can meet at most two code cubes, and in the present edge-disjoint
family in fact at most one unless only its Boolean value, rather than its
physical address, is being forbidden.

Hence, after discarding at most `O(|Z|)` codewords, the construction still
contains any prescribed fixed number `q` of private cubes whenever

\[
                       {s\choose w}\ge q+O(|Z|).          \tag{3.1}
\]

For forbidden **merged colours** rather than literal capacities, this
count is not sufficient: different child backgrounds may merge to one
parent colour.  The finite merged-colour avoidance theorem for the common
scan supplies the needed aperiodic background when its explicit
composition inequality holds.

## 4. Quotient descent

Choose an aperiodic fixed background.  Its cyclic stabilizer is trivial,
so literal cube vertices and edges remain distinct in the necklace
quotient.  Therefore Theorem 2.1 descends verbatim.  A fixed-weight code is
not itself enough to prove aperiodicity; the background choice is part of
the theorem.

## 5. Fixed-bank owner/q1 planting

For one task the four router edges form the simple owner path

\[
 t_f^0-p_f^0-s_f-p_f^1-t_f^1.                           \tag{5.1}
\]

Each adjacent-transfer edge has one deleted-cut hub.  Suppose the four
hubs of every cube are distinct, and hubs belonging to different cubes are
also distinct.  Then replacing each owner edge in (5.1) by its two
owner--hub incidences gives a protected Middle-Levels subgraph `H_F` with

\[
                  \Delta(H_F)\le2,
                  \qquad |E(H_F)|=8|F|.                 \tag{5.2}
\]

The hub-separation hypothesis can be enforced directly for a fixed bank.
Choose `A>2|F|` and give cube `f`, after numbering the tasks
`1,...,|F|`, the background

\[
                       a^{(f)}=(A-f,f,0,\ldots,0).        \tag{5.3}
\]

Place all three active pairs away from the first two background positions.
The unique maximum `A-f` roots every child and every displayed parent hub;
the following entry `f` identifies the task.  Hence hubs from different
cubes cannot be rotations of one another.  Within one cube the rooted
rotation is the identity.  The two suffix hubs have the same deleted
boundary but different surviving `(p_0,p_1)` contexts, while any prefix hub
has a different rooted deleted boundary.  Thus the four hubs are distinct.
This is stronger here than generic aperiodicity, which by itself need not
survive a merge.

### Theorem 5.1 (fixed cube-bank factor planting)

For every fixed `q`, and all sufficiently large `m`, a bank of `q` complete
private router cubes can be chosen so that its owner--hub incidence graph
is contained in a spanning two-factor of `ML_m`.

#### Proof

Choose the backgrounds (5.3), giving literal owner and hub separation.
Equation (5.1) then proves (5.2).  For sufficiently large
`m`,

\[
                              8q\le m-2.                 \tag{5.4}
\]

The small protected-factor theorem for `ML_m` says that every protected
subgraph of maximum degree at most two and with at most `m-2` incidences
extends to a spanning two-factor.  Apply it to `H_F`.  \(\square\)

The theorem plants only the exact owner/q1 incidences.  An arbitrary
two-factor completion need not be connected, upper-surjective, resident,
or compatible with the terminal compiler.  Those properties remain part
of the global protected extension.

## 6. What gate this removes

The former common-cap interface asked for:

\[
 \text{private gain-to-port prefixes}
 \quad+\quad
 r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.                \tag{6.1}
\]

The cube supplies both pieces literally.  Its two source edges are the
private prefixes, and its two `p_2` edges are a displayed full suffix
linkage.  Thus (6.1) is automatic **for gains co-designed as cube sources**.

The exact remaining global interface is smaller:

> **Cube-role planting and regeneration.**  Realize every bounded gain as
> one `s_f` role in an aperiodic even sector, identify the `c=1` endpoints
> with legal terminal cells in the same cap/guard state, keep the cube bank
> disjoint from the compensation linkage, and export the same bounded role
> interface after the next lift.

This is a parent/carrier statement, not a suffix-router Hall statement.

## 7. Odd-sector boundary

The cube router itself works in an odd coordinate cycle: its displayed
prefix and suffix paths are already disjoint and need not extend to a
perfect matching of the whole token sector.  Therefore the following
obstruction does **not** invalidate Theorem 2.1.

If, however, one asks to delete a receiver bank from a pre-existing rooted
odd-sector factor and complete every remaining ordinary vertex using one
nonwrap scan and one socket, the rooted shore imbalance is

\[
              \Delta_{m,R}=[z^{R-1}](1+z^2+z^4)^m,        \tag{7.1}
\]

and a fixed bank plus one socket leaves
`Delta_(m,R)-O(1)` unmatched vertices.  Thus a macroscopic
wrap/circulation current remains necessary for that **residual perfect-
matching architecture**.  Co-designing the bounded cube path inside a new
protected factor avoids the suffix-router part of this obstruction, but it
still has to preserve q2, all deeper upper witnesses, residence, and the
terminal compiler.

## 8. Dependencies and nonclaims

Used:

1. the one-row coordinate-scan matching theorem (for the optional even
   perfect-matching completion) and aperiodic-background descent in
   `MATH_THEOREM_COMMON_SCAN_ROOT_CODED_RECEIVER_EXTENSION_AND_ODD_CURRENT_OBSTRUCTION_20260805.md`;
2. integral max flow, in the elementary form used by
   `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`;
3. the explicit aperiodic background-sector separation from the
   common-scan theorem; and
4. the small protected-factor theorem for `ML_m`.

Not proved:

1. that the PBBS/Pascal parent exposes the cube-source roles;
2. terminal-type legality in the global compiler state;
3. disjointness from an adaptively chosen compensation linkage;
4. guarded q2/all-width planting in either parity;
5. regeneration across every dimension; or
6. `nu(k)=B(k)+O(1)`.
