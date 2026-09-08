# Independent-style audit: syndrome-quotient resident cube cycle

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_SYNDROME_QUOTIENT_SWITCH_TREE_RESIDENT_CUBE_20260804.md`

## 1. Resolution audit

The partial sums of the standard `1,...,h,1,...,h` cycle map to
`U` and `v+U`, respectively.  They are a transversal of `ker(phi)`, so the
kernel translates partition all cube vertices.  No edge-decomposition or
Hamming-code property is used.

The `v`-coordinate forces every kernel vector to have zero `e_h`
coefficient.  Independence of the `b_j` then forces even parity separately
inside every equal-column class `I_j`.  The tree differences in those
classes are therefore a basis of the whole kernel, not merely a subspace.

## 2. Safe-basis audit

For a binary reflected Gray ordering, `I_j` is an equally spaced cyclic set
of size `h/2^j`.  At size two its unique pair has distance `h/2`.  At size at
least four, the step `c/2-1` is odd and hence coprime to the power of two
`c`; it gives a spanning cycle.  Its minimum coordinate distance is `h/4`.
Thus every selected weight-two kernel generator has the advertised
`D`-separation under `h>=4D`.

The factor `1/4` is exact for this method.  The four-point equal-column
class has even-parity dimension three, but above distance `h/4` its legal
weight-two graph is only two disjoint antipodal edges and has incidence
rank two.

## 3. Square orientation and parity twist

For a kernel generator `e_p+e_q`, corresponding `q`-edges in equally
oriented translated cycles point from opposite corners of their square.
The two `p` cross edges therefore give the directed merge.

For a bare inactive translation `e_t`, corresponding `q`-edges are parallel.
Reversing one old cycle would reflect, rather than complement, the two
collars and is not a safe argument.  The theorem does not make that mistake.
It translates the active resolution by `e_(q_0)` on the odd inactive shore.
Every inactive adjacency then has total translation `e_t+e_(q_0)`, so the
same directed square template applies with cross direction `t`.  This is the
essential parity-twist correction.

## 4. Port and global-residence audit

Every cut direction has two antipodal occurrences.  Given a previously
fixed occurrence, one of the two occurrences of the next cut is at cyclic
distance at least `h/2`; recursive choices are valid because the quotient
switch graph is a path, not a cycle.  Thus an old component carrying two
switches leaves at least `D-1` internal transitions in each retained segment.

At a kernel seam, the cross direction `p` is outside the full
`(D-1)`-collar of the deleted `q` edge.  At an inactive seam the cross
direction was absent from the old cycle.  For every other direction, the
two equally oriented collars form a punctured interval of length `2D-2<h`
in one `h`-periodic permutation, so they contain no repeated direction.
A final interval shorter than `D` crosses at most one seam, so these local
checks and old residence exhaust all cases.

All components use translates of one equally oriented cycle.  Therefore
the antipodal occurrence bit is transported identically across each square.
The recursive port choice is a flat gauge on the quotient path; it does not
hide a reflection or a cycle-holonomy assumption.

The quotient basis graph is a cube and has a Hamilton path.  Switches along
that spanning path merge all old cycles, one component at a time.  No
unproved Hamiltonicity of a general Cayley graph is invoked.

## 5. Scope verdict

**PASS.**  Subject only to the elementary binary reflected Gray identities
spelled out in the theorem, the construction proves a `D`-resident Hamilton
cycle of `Q_m` whenever `m` is at least a power of two `h>=4D`.

It correctly does not prove:

* a selector among overlapping good cells from different pairings;
* a repair of low-dimensional cells in one fixed pairing;
* a middle-owner palette or all-width upper deck;
* a lower compiler or common-cap router; or
* an additive-constant OR-word theorem.

The gain is an explicit local resident Hamilton chronology with a priced,
globally separated switch-tree origin.  The remaining residence obstruction
is the global owner/cell selector, not construction inside a sufficiently
large cell.

The theorem does not claim equal-support `D-1` endpoint collars at the
critical dimension `m=D+O(log r)`.  It bypasses that critical collar gate by
using an active power-of-two block of size at least `4D`; the factor four is
sharp for its chosen equal-column weight-two switch basis.
