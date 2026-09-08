# The paired GK `C10` phases satisfy the resident clean-`C6` interface

**Date:** 2026-08-13  
**Status:** exact proof-only compatibility audit.  Each of the two
hexagonal phases of the rigid-cycle `C10` is a clean common-core `C6`, so
the existing prospective resident hybrid theorem applies phase by phase.
The first unresolved condition is not the local packet algebra; it is the
existence of one jointly planted serial resident occurrence state with a
legal intermediate chord and protected exterior.

## 1. Input

Use the exact endpoints `A_i,B_i` and the old/new edges

\[
 e_i=A_iB_i,\qquad n_i=B_iA_{i-1}
\]

from
`MATH_THEOREM_GK_RIGID_PALETTE_NEUTRAL_C10_FUSION_20260813.md`.
The two phases are

\[
 F:\{e_1,e_2,e_3\}\longmapsto\{n_2,n_3,c_*\},
 \qquad c_*=A_3B_1,                                  \tag{1.1}
\]

and

\[
 G:\{e_0,e_4,c_*\}\longmapsto\{n_0,n_1,n_4\}.       \tag{1.2}
\]

All owners have rank `m+1` on `2m+1` coordinates.

## 2. Both phases are literally clean common-core `C6`s

For phase `F`, put

\[
 K_F=\{0\}\cup\{m,m+1,\ldots,2m-3\},                \tag{2.1}
\]

and choose active labels

\[
 (a_0,a_1,a_2,c)=(1,,2m-2,,2m-1,,m-1).           \tag{2.2}
\]

For phase `G`, put

\[
 K_G=\{m,m+1,\ldots,2m-3\}\cup\{2m-1\},            \tag{2.3}
\]

and choose

\[
 (a_0,a_1,a_2,c)=(0,,2m-2,,2m,,m-1).             \tag{2.4}
\]

In both cases `|K|=m-1`.  This is exactly `r-2` with the resident theorem's
owner-rank parameter `r=m+1`.

Define, cyclically,

\[
 P_i=K+a_i+a_{i+1},\qquad Q_i=K+a_i+c.              \tag{2.5}
\]

Substitution of `(2.1)`--`(2.4)` into the binary endpoint formulas gives

\[
 \{P_iQ_i:i\in\mathbb Z_3\}=\text{old phase},
 \qquad
 \{P_iQ_{i+1}:i\in\mathbb Z_3\}=\text{new phase},  \tag{2.6}
\]

for `F` and `G`, respectively.  Thus both phases meet the literal clean
Boolean-diamond hypothesis of the resident theorem, not merely its palette
projection.

The q2 calculation in the `C10` theorem separately verifies the required
PBBS common-deletion condition for `m>=6`: phase `F` cycles
`X_1,X_2,X_3`, while phase `G` cycles `X_0,X_1,X_4`.  Hence both are
simultaneously clean-common-core and q2-transparent.

## 3. What the existing resident theorem supplies

Fix source depth `d`.  The resident clean-`C6` theorem requires

\[
                         r=m+1\ge d+3,               \tag{3.1}
\]

and enough fresh rail coordinates.  Its generic statement writes this as
ambient size at least `r+d+2`; on the literal odd ground of size `2m+1`
this again reduces to `(3.1)`.

Under `(3.1)`, choose `d` rail-deletion coordinates in `K_F` (or `K_G`),
retain one anchor, and use `d` fresh labels in the complement of the direct
active support.  The theorem prospectively replaces each direct phase by
three resident return rails on `6d+6` owner positions.  For each of `F,G`
separately it gives:

1. the same owner/lower-q1/upper-q1/tail/head signature before and after;
2. exact transport of every strict-lower occurrence and lower compiler
   assignment at every depth;
3. positive residence at least `d+1`;
4. fusion of the three declared old port cycles to one; and
5. inclusion of the complete internal cyclic upper deck at every width.

Thus there is **no local normal-form mismatch** between the new `C10` and
the resident hybrid theorem.

## 4. The first actual mismatch is joint serial planting

The resident theorem is prospective and one-packet-at-a-time.  It does not
state that two lifts sharing the intermediate direct chord `c_*` coexist in
one simple occurrence-labelled factor.

More concretely, the native `C10` history is

\[
                 \text{old}\xrightarrow{F}
                 \text{intermediate containing }c_*
                 \xrightarrow{G}\text{new}.         \tag{4.1}
\]

A literal resident lift of `F` replaces its three direct port cycles by
one long resident fused cycle.  The generic output is not automatically a
fresh three-port input state for `G`; this is precisely the regeneration
qualification in the resident hybrid theorem.  Conversely, planting
independent resident lifts for `F` and `G` duplicates the owner occurrence
of the shared chord endpoints `A_3,B_1` and need not preserve simplicity,
history tags, or the intermediate companion rows.

The exact missing assertion is therefore:

> **Paired resident handoff lemma.**  There is one prospective source bank
> on a common owner occurrence set whose first rethread realizes resident
> `F`, whose authenticated intermediate state exposes `c_*=A_3B_1` with
> the companion/history tickets required by resident `G`, and whose second
> rethread realizes `G`, without duplicating owners or exact resources.

Even such a lemma would initially prove only internal cyclic upper
monotonicity.  Intervals crossing from the packet into an arbitrary fixed
exterior, the final linear opening, zero-gap residence, and typed common-cap
routes remain outside the resident theorem.

## 5. Verdict

The new `C10` clears the algebraic gate more strongly than expected:

\[
 \boxed{\text{each phase is an authenticated clean common-core `C6`.}}
\]

The existing resident theorem can lift either phase separately with exact
lower transport, residence, and all-width **internal** upper monotonicity.
The first unresolved row is the same-object serial handoff across the
cancelling chord, followed by protection of the packet/exterior boundary.
