# Audit of paired turn-diamond deletion and the minimal occurrence lift

**Date:** 2026-08-04  
**Method:** independent pure-mathematical replay; no computation, search,
or solver  
**Audited theorem:** MATH_THEOREM_PAIRED_TURN_DIAMOND_DELETION_AND_MINIMAL_OCCURRENCE_LIFT_20260804.md  
**Audited SHA-256:** b1852de086db9846d6f4748e7200fe4757d31036e5a50673a68dac78d6262110

## 0. Verdict

**GO at the stated paired-support and occurrence-lift scope.**

The casualty formula is exact, the Middle-Levels specialization correctly
uses the protected wedge owner/terminal ledger, and the hidden-common-
capacity counterexample proves that cross-claim support privacy is
load-bearing.

## 1. Paired deletion replay

For one claim \(i\), write

\[
 P_i^\epsilon=C_i\cup E_i^\epsilon,
 \qquad E_i^0\cap E_i^1=\varnothing.
\]

A deletion kills both alternatives exactly in either of two cases:

1. it meets \(C_i\); or
2. it avoids \(C_i\) and meets both \(E_i^0,E_i^1\).

This is exactly the set \(D_F\) in (1.1).  Every dead claim of the second
kind contributes two distinct side-hit records, so their count is at most
\(\lfloor s_F/2\rfloor\).  The common-hit claims contribute \(c_F\).

Condition (0.1) says total paired supports of different claims are
disjoint.  Hence choosing either surviving alternative independently for
each live claim preserves pairwise vertex-disjointness.

The construction deleting one common resource in \(c\) pairs and one
exclusive resource on each side of \(t\) other pairs attains
\(c+\lfloor2t/2\rfloor=c+t\).  Thus the bound is sharp.

## 2. Physical-resource replay

Under pairwise support disjointness, common cores are disjoint over claims,
and all side-exclusive sets are disjoint over ordered claim sides.
Therefore one deleted physical resource contributes to at most one
common-hit claim or one ordered side-hit record.  This proves

\[
 c_F\le f_C,\qquad s_F\le f_E
\]

and the resource bound

\[
 |D_F|\le f_C+\left\lfloor{f_E\over2}\right\rfloor.
\]

If common cores are protected, each dead claim requires two side-exclusive
losses, giving \(\lfloor|F|/2\rfloor\).

## 3. Turn-diamond specialization replay

A protected wedge at \(L_i\) has the two canonical paths

\[
 x_i-u_i^0-z_i,\qquad x_i-u_i^1-z_i.
\]

Within a pair, source and terminal are common and the two owners are
exclusive.  The protected packing theorem makes:

* lower sources distinct;
* all \(2p\) owner values distinct; and
* all \(p\) q1 terminal values distinct.

On the theorem's value-injective occurrence face, these facts give
cross-claim support disjointness.  Definition 3.1 explicitly prices every
additional flag, guard, continuation, and capacity quotient, so no hidden
resource is omitted from the hypothesis.

The only-owner-deletion corollary is correct: two distinct selected owners
must be deleted to kill one claim, and owner sets of claims are disjoint.

## 4. Minimal occurrence-lift boundary

The existing factor occurrence theorem provides values, addresses,
containment arcs, and empty prefix interiors.  It does not prove cap
activation, post-compensation survival, typed terminal acceptance, private
continuations, or hidden-capacity identities.  Definition 3.1 adds exactly
those rows.

The regular private-port theorem does not derive them.  It also views
listed ports as simultaneous demands, whereas the two branches of one
wedge are alternatives sharing source and terminal.  Applying a
simultaneous two-port router to both would overprice the physical claim.

## 5. Fixed-bank Rado equality

On the exact direct paired face, every live claim has at least one private
route and every dead claim has none.  Thus the serviceable claim system is
the free matroid on the live claims plus loops on the dead claims.  Its
deficiency is exactly \(|D_F|\), agreeing with the displayed
factor-restricted Rado max formula.

## 6. Hidden-capacity obstruction

If one hidden unit capacity \(g\) belongs to both alternatives of every
claim, deleting \(g\) kills all \(p\) claims while \(|F|=1\).  This violates
cross-claim support disjointness and proves that no deletion-cardinality
bound is valid before shared hidden capacities are represented and priced.

## 7. Scope confirmed

The theorem does not supply the raw dual-branch lift or bound its
intersection with the frozen background.  It also does not establish
two-coordinate product closure or any topology, upper, residence, compiler,
or regeneration theorem.

Its exact new target is:

\[
 \text{one raw protected-wedge dual-branch lift}
 \quad+\quad
 c_F+\left\lfloor{s_F\over2}\right\rfloor=O(1).
\]

That condition closes this one-coordinate cap row with bounded deficiency,
but the full \(B(k)+O(1)\) implication remains conditional on the other
regenerative gates.
