# Hostile audit of the rigid-GK five-hinge common-history lift

**Date:** 2026-08-13  
**Audited file:**
`MATH_THEOREM_GK_RIGID_C10_FIVE_HINGE_COMMON_HISTORY_LIFT_20260813.md`  
**Audited SHA256:**
`3166734d4c2d89caa274a13e72cd77bd644f3fd921a04b413219c406c2543e7b`  
**Verdict:** **PASS after four scope/rigour corrections incorporated in the
audited bytes.**  The direct compound lift is valid for every `m>=5` and
`1<=d<=m-2`.  Its selected PBBS q2 conclusion is valid for `m>=6` only
when the audited unchanged companion edges are retained.  No global source
planting, zero-gap guard, or arbitrary exterior-upper theorem follows.

## 1. Common-core and screen audit

Put

\[
 p=m-1,\quad q=2m-2,\quad s=2m-1,\quad t=2m,
 \qquad H=\{m,\ldots,2m-3\}.
\tag{1.1}
\]

Reading the ten binary owners coordinate by coordinate gives

\[
\begin{array}{c|c|c}
i&A_i\setminus H&B_i\setminus H\\ \hline
0&\{p,q,s\}&\{q,s,t\}\\
1&\{0,p,q\}&\{0,q,s\}\\
2&\{0,1,p\}&\{0,1,q\}\\
3&\{0,p,s\}&\{0,1,s\}\\
4&\{p,s,t\}&\{0,s,t\}.
\end{array}
\tag{1.2}
\]

This table proves, without cardinality inference, that `H` is contained in
all ten owners and that every screen `X_i,Y_i` is a nonempty three-set.
The ten rows in `(1.2)` are distinct.  Since `|H|=m-2`, any
`1<=d<=m-2` admits the required ordered partition into nonempty letters.

The two identities required by the cyclic head shift are, for every
`i in Z_5`,

\[
 X_i\cap Y_{i+1}=X_i\cap Y_i,
 \qquad
 X_i\cup Y_{i+1}=X_{i+1}\cup Y_{i+1}.
\tag{1.3}
\]

They follow immediately from the ten triples in `(1.2)`.  Adding the
disjoint common set `H` proves that the hinge
`A_iB_{i+1}=B_{i+1}A_i=n_{i+1}` has the old lower colour of `e_i` and the
old upper colour of `e_{i+1}`.  Hence the head shift is exactly the net
palette-neutral `C10`, with no intermediate chord.

As a corroborating check, I independently generated the displayed owners
for `m=5,...,20` and verified common-core containment, ten distinct
three-set screens, and both identities in `(1.3)` exactly.  The symbolic
table, not this finite replay, is the proof for all `m`.

## 2. Arbitrary-context lower transport

The potentially delicate case is that `e_1` and `e_4` lie on the same old
PBBS component.  Treating five independently chosen overlapping “right
contexts” would not define a source rethread.  The audited theorem now uses
the correct global formulation: cut immediately before all five tagged
`Y_i` occurrences.  The affected cycles split into five disjoint residual
paths, two of them coming from the twice-cut component, and the complete
paths beginning with `Y_i` are permuted.

An interval internal to a residual path is literal.  At a reattached seam,
an interval extending left through `X_iC_1...C_d` contains

\[
 H\cup X_i=A_i,
\tag{2.1}
\]

so it cannot have rank below `m+1`.  Every strict-lower seam interval is
therefore a suffix of the common history followed by a prefix of one tagged
right path.  Move that occurrence to the old seam preceding the same right
path; the common suffix is identical, so occurrence width and OR value are
unchanged.  A strict-lower interval cannot cross two reattached seams,
because it would traverse a terminal block `X_hC_1...C_d` and contain
`A_h`.  The reverse rethread gives the inverse map.

This proves a genuine occurrence bijection for compatible arbitrary
contexts, not merely equality of projected supports.  It transports every
cell-based strict-lower compiler assignment.  It does not automatically
transport independent phase, socket, cap, or route tickets.

## 3. Internal deck and positive residence

For internal fragment widths `ell<=d`, no interval meets both screens, so
the left/right bank bijection applies.  At width `d+1`, the two values are
the owner bank `A_i,B_i`, whose multiset is unchanged.  At width `d+2`, the
only old and new values are respectively

\[
 A_i\cup B_i,
 \qquad
 A_i\cup B_{i+1}=A_{i+1}\cup B_{i+1},
\tag{3.1}
\]

so those five values rotate.  This exhausts every internal width and proves
the complete internal-deck assertion.

For residence, a source occurrence of a coordinate belongs to `d+1`
consecutive cyclic length-`d+1` owner windows.  The union of several such
blocks has either become constant on a component or has every positive run
of length at least `d+1`; overlaps cannot shorten a connected run.  The
head rethread permutes source occurrences and adds no positions.  Thus the
positive-residence and zero-length-charge claims are correct.  This does
not bound the intervening zero run, which depends on exterior contexts.

## 4. q2 and topology scope

The selected PBBS q2 row is not identified here with the literal source
derivative intervals.  It depends on the changed diamond together with the
other, unchanged factor diamond at each affected owner.  The audited source
now states the correct separation:

* literal interval rows (q3 and deeper in the current bookkeeping) follow
  from the strict-lower occurrence bijection for `m>=5`;
* selected q2 follows from the independent owner-level audit for `m>=6`,
  conditional on retaining those five unchanged PBBS companion edges.

Under that same planting hypothesis, the source move changes exactly the
five owner hinges of the audited `C10`.  Its old return involution is
`(0)(1\ 4)(2)(3)`; composing with the five-cycle of new heads gives two
return orbits.  Hence the four affected PBBS owner components become two.

## 5. Corrections incorporated and exact boundary

The hostile audit required four genuine clarifications, all incorporated
before freezing the SHA above:

1. “local/source theorem” was qualified as **prospective**; it does not
   assert that the canonical PBBS chronology already exposes the five
   literal common histories.
2. Arbitrary contexts were formulated as a disjoint global cut-path
   decomposition, which covers the component containing two hinges.
3. Literal q3/deeper transport was separated from selected owner-level q2,
   whose `m>=6` proof requires the unchanged PBBS companions.
4. Compiler transport was restricted to cell-based data; extra frozen
   socket/cap/route state requires its own equivariance proof.

No defect was found in the common-core identities, the direct `C10`
indexing, the complete internal deck, positive residence, or four-to-two
owner topology.

The first context-dependent upper width remains `d+3`: a private exterior
letter attached to one side distinguishes the old pair `(X_i,Y_i)` from
the new pair `(X_i,Y_{i+1})`.  Therefore the exact remaining gates are:

\[
\boxed{
\text{protected global source planting}
\; + \;
\text{zero-gap/q-safe exterior control}
\; + \;
\text{replacement witnesses for exterior upper fans}.}
\]

The direct five-hinge theorem closes the local compound converter and
eliminates the serial shared-chord obstruction; it does not close these
three global gates.
