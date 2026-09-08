# Audit: generalized defect screens and consecutive rotor rail

**Date:** 2026-08-05  
**Method:** independent set, index, rank, and serial-order replay; no
computation or search

## Verdict

**PASS at the stated conditional physical scope.**

## 1. Generalized local packet

The history contributes `H=K\D` and both screens contribute `D`, so the
owner core remains `K`.  The active screen pairs give exactly `Q_i` and
`P_(i-1)` (or `P_i` after rethread).  Any interval meeting both screens
contains a rank-`r` owner, so the all-strict-lower occurrence proof is
unchanged.  Disjoint history letters are not needed.

## 2. Sliding equations

At transition `t`, source positions `t`, `t+1,...,t+d`, `t+d+1` are
respectively left screen, history, and right screen.  Therefore (2.2)--(2.4)
are definitionally necessary and sufficient for the generalized ansatz.
Comparing the same source letter at `t` with the right screen of
`t-d-1` gives (2.5), with no index shift.

## 3. Rotor replay

Because phase advances modulo `d+1`, the `d` internal source letters meet
every age block except `G_p` exactly once.  Their clock labels are exactly
`x_(t+1),...,x_(t+d)`.  This proves (3.10).  The clean core size is

\[
 (|G|-1)+d=(|G|+d+1)-2=r-2.
\]

The left/right sources use the same age block and clock labels `x_t` and
`x_(t+d+1)`.  Their owner windows are (3.4), and local distinctness makes
the transition Johnson.  The two-set obstruction is genuinely escaped
because a screen now has size `|G_p|+1`, while the defects over one age
period are disjoint.

## 4. Serial-order replay

Packet `u>t` begins changing its right body no earlier than source position
`u+d+1>=t+d+2`, strictly after packet `t`'s complete fragment.  Descending
order therefore preserves the next fragment literally.  Arbitrary changed
right contexts are admitted by the local theorem.  This proves serial lower
transport, conditional on the stated privacy of all other roles and the
chosen source orientation.

## 5. Scope

The theorem constructs a source-compatible rotor corridor; it does not
identify it inside the canonical PBBS word.  It also does not protect long
upper intervals or non-functorial common-cap routes.  Those exclusions are
explicit and necessary.
