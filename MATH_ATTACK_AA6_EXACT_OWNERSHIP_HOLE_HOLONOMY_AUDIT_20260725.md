# Independent audit of exact-middle hole holonomy

Date: 2026-07-25

Audited source:
MATH_ATTACK_AA6_EXACT_OWNERSHIP_HOLE_HOLONOMY_NOGO_20260725.md.

Method: pure mathematics only.

## Verdict

The exact signed-NAE identity, the abstract exact-middle cube, the doubled
\(K_4\) constant, and the target-compression argument are correct.  The
base construction in Sections 2--4 really has literal integral middle ownership for every
component signing and a \((1/6-o(1))W\) hole lower bound after compression
to exactly \(N_1\) targets.

The later Sections 4A--4B refine the target labels, point margins, and
constant to \(1/4-o(1)\).  They have now been checked separately in
Sections 7--8 below and are certified there.

An earlier draft had one ambiguous quantifier in \(\mathrm{CLH}_A\): the
signing which controls NAE violations must be the **same** signing whose
selected atoms admit \(o(W)\) chronology/reset toll.  Small minimum
frustration and existence of a separately low-toll signing do not compose.
The source now fixes this by its joint statement \(\mathrm{JCLH}_A\), and
also states the joint normalization and one-color extraction for a rotor
multicover.

Subject to that correction, the claimed conditional implication is sound:
append each of the \(o(W)\) missing masks as a one-letter repair, then use
the audited outer-tail bound and let the fixed window grow.

## 1. Component connectivity and middle counts

For one active component, the four left-right ownership cells have sizes

\[
\begin{pmatrix}m+1&m\\m&m+1\end{pmatrix}.
\]

Every row and column sum is \(2m+1=n\), the total is \(2n\), and all four
cells are nonempty.  Hence the overlay is exactly a connected \(K_{2,2}\).
Different components have disjoint middle symbols.

One block contains four components and therefore \(8\) rows and \(8n\)
middle symbols on either side.  With
\(J=\lfloor B/8\rfloor\), the residual \(B-8J\) common rows contribute
\(n(B-8J)\) further symbols.  Thus each side has \(B\) rows and partitions

\[
8nJ+n(B-8J)=nB=W
\]

middle symbols.  Choosing either complete side in every component preserves
exact middle ownership.  Common rows cause no ambiguity: their two colored
copies have identical incidence and contribute the same uncolored row to
each child.

## 2. Target incidence inventory

At one component vertex, the three \(K_4\) neighbours, two gadget signs,
and \(t\) copies give \(6t\) target occurrences on each side.  Since

\[
f=2n-6t\in\{0,2,4\},
\]

the \(f\) neutral targets bring the side total to \(2n\), which splits into
two rows of \(n\) distinct targets.

One block has

\[
6\cdot 2t\cdot2+4f=24t+4f=8n
\]

distinct targets.  Residual rows supply private neutral targets, so the
uncompressed target universe has size \(W\).  Every constraint target
occurs in exactly two rows on one source side, and every neutral target
occurs once on each side.  Thus the maximum number of source rows
containing one target is two, as used in the compression proof.

Uniform independent component signs give expected load one to every
uncompressed target: a neutral target has deterministic load one and a
constraint target is the sum of two independent Bernoulli-\(1/2\)
ownership indicators.

## 3. Exact \(K_4\) hole constant

For either gadget on \(\{u,v\}\), opposite endpoint signs cover its two
targets once each.  Equal signs give loads \((2,0)\) or \((0,2)\), hence
one hole.  Every two-colouring of \(K_4\) has at least two monochromatic
edges, with equality for a \(2+2\) split.  There are \(2t\) gadgets per
edge, so the sharp block minimum is \(4t\), and the global minimum before
compression is \(4tJ\).

Since \(t=n/3+O(1)\), \(J=B/8+O(1)\), and \(nB=W\),

\[
4tJ=\frac16W+O(B+n).
\]

The constant \(1/6\) is correct.

## 4. Target compression

The conflict graph degree is at most \(2(n-1)\): a target lies in at most
two source rows, each containing \(n-1\) other targets.  At greedy step
\(j<D\), a permissible partner exists whenever

\[
W-2j>2n-1.
\]

At the last step this follows from

\[
W-2D+2
=W\left(1-\frac4{m+2}\right)+2>2n-1
\]

for all sufficiently large \(m\).  The chosen pairs are disjoint and no
row contains both members, so quotienting preserves \(n\) distinct target
symbols in every row.

There are exactly

\[
D=W-N_1=\frac{2W}{m+2}
\]

merged targets of fractional load two; all others have fractional load
one.  This is the exact balanced depth-one floor/ceiling vector.  Merging
one pair reduces holes by at most one, so

\[
M\ge4tJ-D
=\left(\frac16-o(1)\right)W.
\]

## 5. Hole identity

Theorem 1.1 is exact.  A target owned on both sides of one component covers
both antipodal children.  With no active component it contributes two
holes; with one it contributes one.  With at least two one-sided active
components, the two hole events are exactly the two monochromatic signed
patterns.  Summation gives

\[
\min_\varepsilon(M(F_\varepsilon)+M(F_{-\varepsilon}))
=\iota+\operatorname{fr}_{\rm NAE}.
\]

Multiplicities on one side do not affect this positivity identity.

## 6. Joint-quantifier audit

The safe quantified version, now adopted in the source, is:

> There exist one actual support-feasible overlay and one signing
> \(\varepsilon\) such that
> \[
> \iota_H+
> \#\{\text{signed target hyperedges violated by }\varepsilon\}=o(W),
> \]
> and the **same** selected child \(F_\varepsilon\) has a literal
> realization of length \(W+o(W)\) before repairs.

Equivalently, one may require that an NAE-minimizing signing has
\(o(W)\) chronology toll.  Merely asserting

\[
\iota_H+\operatorname{fr}_{\rm NAE}=o(W)
\]

and that some unspecified signing has low chronology toll is insufficient.

The target hypergraph must include the total resource set over all
controlled depths, so the displayed \(o(W)\) is a total hole count rather
than a per-rank bound.  For a \(Q_m\)-fold rotor master, replace \(W\) by
\(Q_mW\) throughout the multicover ledger and state the averaging/extraction
step which gives one color with both properties; separate averages for
holes and resets do not guarantee the same color.

With these quantifiers fixed, append one entry equal to each missing mask.
This costs at most the total hole count and cannot destroy previous
witnesses.  Hence the fixed-window word has length \(W+o(W)\), and the
already audited outer-tail/diagonal argument yields coefficient one.

The sentence about antipodal children being relabelings is unnecessary for
the hole conclusion, because a nonnegative combined hole count \(o(W)\)
already makes each child \(o(W)\).  If retained, “transposition-symmetric”
should mean that the transposition fixes every ownership component
setwise; otherwise it can permute component indices and the literal
identity \(F_{-\varepsilon}=\tau F_\varepsilon\) need not hold for an
arbitrary signing.

## 7. Audit of the actual-label refinement

Section 4A also passes.  The regular upper family exists because

\[
\frac{(m-1)(W-N_1)}{n}
=(m-1)B-\binom{n-1}{m-2}\in\mathbb Z,
\]

and the degree-square exchange forces every coordinate degree to equal
this integer.  The first-unequal-pair involutions leave at most
\(2^{m+1}+2m=o(W/n)\) rank targets unpacked.  Deleting the disjoint
rectangles meeting the upper family loses at most \(D=O(W/n)\) more, so
\(Q=W/4+O(W/n)\).

The neutral-slot identity is exact, and Hall's condition is valid: a set
of second copies forbidden from one row has size at most \(n\) and sees at
least \(D-n\ge n\) slots, while a set using two forbidden rows sees all
\(D\) remaining slots.  Finally the two directions of every rectangle have
opposite component effects, so switching preserves the point vector.  At
the all-left corner the rectangle contribution equals its four target
labels once each; adding the regular upper family gives point degree

\[
\binom{n-1}{m-2}+\frac{(m-1)D}{n}=(m-1)B.
\]

Thus the actual labels, row distinctness, balanced \(\{1,2\}\) loads, and
one-design margins are literal, not formal marginals.

## 8. Audit of the optimized doubled-\(K_n\) block

Section 4B's optimized constant is correct.  A block has \(n\) components,
\(2n\) rows, and \(2n^2\) target slots on either source side.  Its two
gadgets on each edge use

\[
4\binom n2=2n(n-1)
\]

constraint occurrences, leaving exactly \(2n\) neutral slots.  The two
defining bounds on \(J_*\) enforce both row capacity and availability of
disjoint actual-target rectangles.  Since

\[
\frac{Q}{\binom n2}
=\frac{B}{2(n-1)}+O(B/n^2)
=\left(1+O(n^{-1})\right)\frac{B}{2n},
\]

floors give
\(J_*=(1+O(n^{-1}))B/(2n)\).

For \(n=2m+1\), every two-colouring of \(K_n\) has at least

\[
\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor=m^2
\]

monochromatic edges.  Both gadgets on such an edge contribute a hole.
Consequently every signing has at least

\[
2m^2J_*
=\left(1+O(n^{-1})\right)\frac{m^2}{n^2}W
=\left(\frac14-o(1)\right)W
\]

holes.  The residual fixed rows, neutral Hall assignment, and point-margin
cancellation are unchanged from Section 4A.  Hence the optimized theorem
retains literal exact middle ownership and every advertised target
property.
