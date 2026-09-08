# Two-hole packet upper defects obey an exact conservation law

## Status

Every two-hole packet uses the same number of owners, immediate-lower
roots, and immediate-upper occurrences.  The owner and lower shores have
size `W`, while the upper shore is smaller.  This gives an exact identity
between owner leave, missing upper targets, and repeated upper occurrences.

The identity identifies the sharp mesoscopic scale

\[
                         u_0={2W\over r+1}=\Theta(W/r).
\]

In particular, a complete owner/lower factor is *supposed* to have exactly
`u_0` units of upper repetition when it covers the upper shore.  Those
repetitions are not defects to be eliminated.  The genuine upper defect is
failure to cover a target.

## 1. The ledger

Put

\[
 W=\binom{2r-1}r=\binom{2r-1}{r-1},\qquad
 U=\binom{2r-1}{r+1}={r-1\over r+1}W.                     \tag{1.1}
\]

Let `mathcal M` be any matching of one-step upper-rich ring packets on the
owner and immediate-lower shores.  Packet `P` may have its own period
`L_P`, but it has exactly `L_P` owners, lower roots, and upper occurrences.
Write

\[
              M=\sum_{P\in\mathcal M}L_P,\qquad u=W-M.     \tag{1.2}
\]

Thus exactly `u` owners and `u` lower roots remain uncovered.  Upper
occurrences are not required to be disjoint.  For each upper target `X`,
let `mu_X` be its occurrence multiplicity, and put

\[
 h=|\{X:\mu_X=0\}|,
 \qquad
 e=\sum_X(\mu_X-1)_+.                                     \tag{1.3}
\]

Here `h` is the number of genuine upper holes and `e` is the total excess
multiplicity above first coverage.

### Theorem 1.1 (upper-defect conservation)

Every owner/lower packet matching satisfies

\[
 \boxed{
 e-h=u_0-u,
 \qquad
 u_0=W-U={2W\over r+1}.}                                  \tag{1.4}
\]

#### Proof

The packets contribute exactly

\[
                         \sum_X\mu_X=M=W-u               \tag{1.5}
\]

upper occurrences.  The number of distinct upper targets used is `U-h`,
so by the definition of excess,

\[
                         W-u=(U-h)+e.                       \tag{1.6}
\]

Rearrange and use (1.1).  \(\square\)

## 2. Sharp consequences

### Corollary 2.1 (simple-upper threshold)

If no upper target is repeated, then

\[
                         u\ge u_0,\qquad h=u-u_0.           \tag{2.1}
\]

Thus an upper-simple packet packing cannot cover more than `U` owners.
It covers the entire upper shore exactly once if and only if

\[
                         u=u_0.                             \tag{2.2}
\]

If all packets have one common period `L`, the matching also requires
`u congruent W (mod L)`.  In that fixed-period subfamily, exact one-copy
coverage of all three shores is arithmetically possible only when

\[
                         L\mid U.                           \tag{2.3}
\]

If (2.3) fails, the nearest fixed-period admissible owner leave differs
from `u_0` by less than `L`, and (1.4) prices the resulting `O(L)` net upper
defect.  Mixed periods remove this particular congruence condition without
changing the conservation law.

### Corollary 2.2 (complete owner/lower factor)

If the packet factor covers every owner and every lower root, then

\[
                         e-h=u_0.                           \tag{2.4}
\]

If it is upper-complete as required by the OR construction, then `h=0`
and therefore

\[
 \boxed{
                         e=u_0={2W\over r+1}.}              \tag{2.5}
\]

This is the integral meaning of the fractional upper load

\[
                         {r+1\over r-1}=1+{2\over r-1}.     \tag{2.6}
\]

The repeated upper occurrences in (2.5) are unavoidable inventory, not a
failure of the construction.

### Corollary 2.3 (bulk leave and unavoidable holes)

For a bulk packet packing with owner/lower leave `u`,

\[
 h\ge(u-u_0)_+,
 \qquad
 e\ge(u_0-u)_+.                                           \tag{2.7}
\]

Both bounds are sharp at the level of scalar multiplicity.  In particular,
a bulk cover-down leaving `Theta(W/sqrt(r))` resources necessarily leaves
the same order of upper holes, because

\[
                         W/\sqrt r\gg u_0=\Theta(W/r).      \tag{2.8}
\]

The mesoscopic reservoir must therefore repair owner, lower-root, and upper
holes jointly; upper completion cannot be postponed to a bounded terminal
gadget after such a bulk leave.

## 3. Exact reservoir state

Suppose a bulk packing leaves `u` owners and lower roots and has upper
defects `(h,e)`.  A completion bank using the remaining owner/lower
resources contributes exactly `u` further upper occurrences.  At the end,
upper completeness is equivalent to routing at least one of those
occurrences to each of the `h` missing targets.  In particular, extendability
requires

\[
                         h\le u,
 \qquad\text{equivalently by (1.4)}\qquad e\le u_0.         \tag{3.1}
\]

When this holds, the remaining

\[
                         u-h                               \tag{3.2}
\]

occurrences may land on already covered targets.  Equation (1.4) guarantees
that after successful routing the final excess is exactly `u_0`.

Thus the proof-safe mesoscopic state is not a symmetric three-shore leave.
It is

\[
 \boxed{
   (\text{owner leave }u,\ \text{lower leave }u,\
    \text{named upper-hole set of size }h),}               \tag{3.3}
\]

with the exact scalar invariant `e-h=u_0-u`.  A cover-down theorem must
retain literal incidence information from the remaining packets to the
named upper-hole set; aggregate packet counts alone do not suffice.

Combined with top simplicity and the q1-intersection classification, the
remaining integral target is now precise:

> Find a top-simple owner/lower packet packing with a mesoscopic leave,
> together with an all-cut reservoir assignment that covers every named
> upper hole while completing the equal owner/lower leaves.

The natural forced repetition scale is `u_0=Theta(W/r)`.  Any larger bulk
leave is acceptable only if the same reservoir is already equipped to
repair its `Theta(u)` upper holes.
