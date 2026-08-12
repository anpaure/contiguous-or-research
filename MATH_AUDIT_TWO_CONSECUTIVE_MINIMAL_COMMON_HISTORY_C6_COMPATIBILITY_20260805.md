# Audit: two consecutive minimal common-history C6 packets

**Date:** 2026-08-05  
**Method:** direct source-position and set-difference replay; no computation

## Verdict

**PASS.**

The overlap positions are exact: `A_1` is simultaneously first-history
letter of packet zero and left screen of packet one; `A_(d+1)` is
right screen of packet zero and last-history letter of packet one.  The
middle letters `A_2,...,A_d` are common to both histories.

Minimality makes every history a disjoint core partition and every active
screen disjoint from its own packet core.  Hence

\[
 K_0=A_1\dot\cup M,
 \qquad K_1=M\dot\cup A_{d+1},
\]

which proves the directed-difference criterion.  Conversely those
differences plus any nonempty partition of the intersection reconstruct the
two fragments.  At the shared owner `V`, the criterion reduces exactly to
disjointness of the two prescribed screen pairs.

The theorem correctly distinguishes a two-packet shared child from a run of
`d+1` packets on one physical source rail.

## PBBS label replay

For orientation `P_i->Q_i`, role `E_2` has right screen
`{c_A,a_2^A}` and role `E_1` has left screen `{a_1^B,a_2^B}`.  Equality of
the incoming companion q1 row gives `c_A=d_B in K_B`, excluding the first
coordinate.

For the second, write the first center as `0 10D`.  One PBBS step gives
`0 01 bar(D)`.  Its forward survivor is the complemented last up-step into
the rightmost maximum of `D`; complementing again yields `110 D^(down)`.
The old `a_2` zero retains a one as its cyclic successor, so it cannot be
the terminal zero `a_1^B` before B's zero root.  Cutting after it would give
`D^(down)11`, whose prefix `D^(down)` has height `-2`, so it cannot be B's
root `a_2^B` either.  The screens are disjoint and Corollary 2.2 applies.
