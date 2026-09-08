# The generalized defect-screen rotor does not fit the rigid full-rotation rail

**Date:** 2026-08-05  
**Method:** exact colored sliding-window equations; no computation or search  
**Status:** unconditional obstruction for the canonical rigid full-rotation
rail when `m>=4` and `1<=d<=m-2`.  Enlarging the common-history screens by
arbitrary defect subsets removes the scalar `r-2<=2d` obstruction in an
abstract rotor corridor, but it cannot satisfy the literal screen-consistency
equation on the consecutive single-soliton PBBS rail.

## 1. The source orientation of the rigid rail

Work on `Z_n`, `n=2m+1`.  At spatial phase `t`, the rigid clean `C6` has

\[
 K_t=\rho^t\{1,\ldots,m-2\},
\]

and its old `E_0(t)` hinge is represented by the common-history fragment

\[
                         \widehat W_0(t)
   =(X_0(t),\mathcal C_t,Y_1(t)).                 \tag{1.1}
\]

The two active screen pairs are

\[
 \ell_t=X_0(t)=\{t,t+m-1\},
 \qquad
 r_t=Y_1(t)=\{t+m-1,t+m\}.                       \tag{1.2}
\]

Its owner transition in source order is

\[
 Q_0(t)=K_t\cup\ell_t
     \longrightarrow
 P_0(t)=K_t\cup r_t.                              \tag{1.3}
\]

Since

\[
                         P_0(t)=Q_0(t+1),          \tag{1.4}
\]

the complete rotation family is one consecutive source rail indexed by
increasing `t`.  Applying the graph switches in decreasing `t` is exactly the
reverse serial order required by the generalized rotor theorem.

## 2. The payload equation has no solution

Allow the full generalized ansatz.  Thus at role `t` choose an arbitrary

\[
                         D_t\subseteq K_t,          \tag{2.1}
\]

put the defect into both screens, and allow arbitrary nonempty overlapping
history letters whose union is `K_t-D_t`.

The necessary screen-consistency equation is

\[
 D_t\cup\ell_t
   =D_{t-d-1}\cup r_{t-d-1}.                     \tag{2.2}
\]

### Theorem 2.1 (rigid-rail payload obstruction)

Equation (2.2) fails for every choice of the defect sets `D_t`.  Hence the
canonical full rigid rotation rail has no simultaneous generalized
defect-screen common-history decoration.

#### Proof

Fix `t` and consider

\[
                         z=t+m-1.                  \tag{2.3}
\]

By (1.2), `z` lies in the left side of (2.2).  On the right, the active pair
is

\[
 r_{t-d-1}
   =\{t+m-d-2,t+m-d-1\},                         \tag{2.4}
\]

which does not contain `z` because the two differences are `d+1` and `d`.

The earlier core is the cyclic interval

\[
 K_{t-d-1}
   =\{t-d,t-d+1,\ldots,t+m-d-3\}.                \tag{2.5}
\]

Relative to its first coordinate `t-d`, the residue of `z` is

\[
                         m+d-1.                   \tag{2.6}
\]

For `1<=d<=m-2`, this lies between `m` and `2m-3`, strictly below
`n=2m+1`.  Membership in (2.5) would require a residue in
`{0,...,m-3}`.  Therefore `z` is not in `K_(t-d-1)`, and hence not in
`D_(t-d-1)`.

Thus `z` belongs to the left side of (2.2) and not the right side, a
contradiction.  `square`

Reversing the source orientation swaps the two screens and reverses the
cyclic rail indices.  The sliding equations are invariant under that joint
operation, so the obstruction is not an artefact of orientation.

## 3. Interpretation

The abstract rotating-defect corridor has owners

\[
                         G\cup\{x_t,\ldots,x_{t+d}\}, \tag{3.1}
\]

with one fixed core `G` of size `r-d-1`.  The rigid single-soliton owners are
all cyclic translates of an `m`-interval and have empty total intersection.
Theorem 2.1 is the exact colored version of that mismatch: the active label
`t+m-1` is required again in one source position after `d+1` roles, but the
earlier clean core and active pair have already rotated past it.

This is stronger than the old scalar screen-size no-go.  Arbitrarily large
defect screens and arbitrarily overlapping history letters cannot repair the
missing payload coordinate.

## 4. What the generalized theorem would have supplied

Had (2.2) and the history-union equation held, descending serial composition
would have given, at zero source-length charge:

1. exact owner, q1, upper-q1 and selected-q2 rows;
2. zero complete strict-lower occurrence current at every depth;
3. exact transport of every occurrence-labelled strict-lower compiler
   matching; and
4. positive cyclic residence at least `d+1`.

Theorem 2.1 shows that none of these global-rail consequences may be imported
for the canonical full rotation braid.  Isolated packets and abstract fixed-
core rotor corridors retain the generalized theorem.

Even in a valid generalized corridor, arbitrary-width upper protection would
remain separate.  The first context-dependent casualty may occur at source
width `d+3`, rank `r+2`, and the rigid private-prefix example has nonzero
binary-necklace current.

## 5. Constant component count is not yet constant opening charge

The full rigid graph orbit has

\[
                         C=1+\gcd(2m+1,3)\in\{2,4\} \tag{5.1}
\]

components.  This is a constant number of topological pieces.  It does not
by itself imply an `O(1)` literal sidecar.

For depth-`d` trace states `u,v`, any literal join has chronology cost at
least

\[
 \delta_d(u,v)=d-
 \max\{q:\text{the length-}q\text{ suffix of }u
                \text{ equals the length-}q\text{ prefix of }v\}. \tag{5.2}
\]

Two chosen ports with no overlap cost `d` new source letters.  Thus even two
components can cost `Theta(d)=Theta(sqrt k)` unless compatible ports are
prepared.

The exact conditional conclusion is:

> If the repaired named target bank also supplies one all-width-safe cut on
> each of the `C` components and a component ordering whose total literal
> overlap-routing cost is `O(1)`, then the final `2` or `4` components can be
> opened and joined at `O(1)` charge.

All-width safety requires the cuts to avoid every forced witness core, and
the trace-overlap condition is additional to target-bank repair.  Without
those two port properties, constant component count alone gives no additive-
constant theorem.

## 6. Exact frontier

For the rigid full orbit:

| gate | status |
|---|---|
| serial graph switches | exact |
| q1 / upper-q1 / selected q2 | exact throughout |
| generalized defect-screen rail | impossible by (2.2) |
| complete strict-lower/compiler rail | therefore not obtained |
| arbitrary upper bank | requires protected alternatives |
| component count | constant `2` or `4`, but never fused |
| `O(1)` opening | conditional on safe high-overlap ports |

The next viable source object must change the owner rail itself, use a
compound packet whose payload is not governed by (2.2), or decorate only a
sparse subfamily and protect the remaining lower/upper witnesses elsewhere.

## 7. Dependencies

This note applies the exact screen equations from

`MATH_THEOREM_GENERALIZED_COMMON_HISTORY_DEFECT_SCREENS_AND_CONSECUTIVE_ROTOR_RAIL_20260805.md`

to the rigid packet and serial topology in

`MATH_THEOREM_PBBS_RIGID_C6_SERIAL_ROTATION_ORBIT_TOPOLOGY_NOGO_20260805.md`.

The opening qualification uses the exact overlap lower bound in

`MATH_THEOREM_A_UNSATURATED_HINGE_SKELETON_DAMAGE_AND_TWO_SWITCH_EXPANSION_20260802.md`

and the all-width forced-cut criterion in

`MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`.
