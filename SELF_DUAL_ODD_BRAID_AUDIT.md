# Audit: the proposed self-dual odd-graph braid for `k=11`

## Verdict

The odd-graph quotient and its complement duality are correct and potentially
useful.  The claimed complete `O_6` skeleton is not currently certified: no
cycle artifact exists in the workspace or on either RunPod.  The proposed
mixed-width completion therefore remains a conditional construction ansatz,
not a new upper bound or proof of `nu(11)=465`.

## 1. Correct algebraic core

Let `C_i` be a Hamilton cycle in `O_6=KG(11,5)` and let `z_i` be the unique
coordinate outside `C_i union C_{i+1}`.  Then

\[
C_{i+1}=C_i^c\setminus\{z_i\},
\qquad
C_{i+2}=C_i-\{z_{i+1}\}+\{z_i\}.
\]

Thus each parity subsequence is a Johnson cycle.  The transition color

\[
R_i=C_{i-1}\cap C_{i+1}
   =C_i^c\setminus\{z_{i-1},z_i\}
\]

has rank four.

For either parity, put

\[
L_j=C_{2j+p},\qquad U_j=C_{2j+p+1}^c.
\]

Then `L_j,L_{j+1} subset U_j`, and

\[
U_{j-1}\cap U_j=L_j,
\qquad
U_{j-1}\cup U_j=R_{2j+p}^c.
\]

Consequently complete rank-four transition colors would simultaneously give
complete rank-seven union colors.  This is a genuine self-duality gain.

The two parity lifts form a `231+231` cycle cover of the two middle layers.
They are not yet the `369+93` pair of paths used by the current mixed-width
search.  A color-safe switch joining/splitting the components, plus compatible
linear cuts, is still required.

## 2. Edge-label run interpretation

The recurrence shows that a coordinate inserted by one parity transition is
removed at a later transition bearing the same omitted label.  In particular,
an internal singleton run corresponds to a return at cyclic label distance
three, and a two-vertex run to the relevant next return at distance five.
This gives a compact local language for pair/triple factorability.

Boundary runs, intervening returns, the two cuts, and the mixed-width seam must
still be handled explicitly.  Merely forbidding equal labels at distances
three and five on the whole cyclic word is stronger than some linear boundary
conditions and weaker than a complete pinning proof.

## 3. Unsupported certificate claims

The supplied text claims an explicit `462`-vertex cycle with all `330`
transition colors, and another representative with complete deeper rank-three
and rank-two intersections.  Exhaustive filename/content scans found no such
artifact locally or on either configured RunPod.  Existing middle-level and
rank-six cycle files are not rank-five Hamilton cycles in `KG(11,5)`.

`verify_o6_cycle.cpp` has been added as a strict checker for any future
candidate.  Its exit status verifies the rank-five permutation, all disjoint
cyclic edges, the number of transition colors, both parity Johnson lifts, and
all rank-five edge colors.  It reports deeper intersection counts for audit,
and `--require-deep` additionally gates complete rank-three, rank-two, and
rank-one parity-lift intersections.  The distance-three label defect is not
yet an acceptance gate because the mixed linear boundary condition has not
been specified precisely enough.

Until the 462 masks and verifier output are supplied, the claimed skeleton is
**unverified**, not inherited fact.

## 4. The short-band count is an ansatz, not a necessity

At `k=11,n=465`, after reserving one short witness for every mask of ranks at
most five, `369` short cells remain.  These cells need not have distinct ORs
and need not all represent rank-six masks.  Therefore the statement that
equality *forces* exactly

\[
561\text{ masks of ranks }1\!:\!4,
\quad462\text{ rank-five masks},
\quad369\text{ rank-six masks}
\]

among the short-window values is false.

Requiring that collision-free saturation is a legitimate stronger
construction target.  Under that target, the arithmetic split

\[
369=231+138,
\qquad231-138=93
\]

is natural because the odd-graph quotient has two parity components of size
231.  It is not forced by the lower bound alone.

## 5. What would make it decisive

A valid certificate route needs all of the following:

1. a checked `O_6` Hamilton cycle with all 330 transition colors;
2. a checked color-safe switch/cut producing the required `369+93` linear
   middle schedule;
3. the exact mixed pair/triple run conditions, including seams and boundaries;
4. a bijective short-band labeling of the lower masks;
5. coordinatewise pin survival; and
6. checked longer upper unions through rank eleven.

If these pass, the resulting 465-entry array would prove `nu(11)=465` by the
existing lower bound.  At present the idea is a promising self-dual search
coordinate system, not a solved case and not yet an all-dimensional principle.
