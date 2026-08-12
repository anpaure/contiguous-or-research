# FRR versus IRRC16: exact sparse history-lift criterion and the frozen-sign obstruction

Date: 2026-07-29  
Lane: A  
Status: theorem and counteraudit.  No unrestricted `K=16` factor is claimed.

## 0. Verdict

The source-relative equations (4.10)--(4.11) in
`MATH_THEOREM_K16_BIRESIDENT_COMPLEMENT_DOUBLE_AND_TURN_SELECTOR_20260729.md`
are correct as, respectively, the rank-seven degree equation and the lower
palette-survival inequalities for a facet-rail repair.  Upper colours are
preserved automatically because the replacement still chooses exactly one
edge indexed by each cut upper set `U`.

There are, however, two important scope corrections.

1. The number `60` is the minimum number of `Z_15` edge orbits needed to
   **cut** all 95 positive-run collar orbits.  Neither (4.7) nor (4.12)
   constructs replacement pairs `p(U)`, solves (4.10), or supplies a
   rethread.  Thus the phrase “60-orbit rethread” is presently shorthand
   for a hypothetical rethread at the minimum cut scale, not a proved
   circulation.
2. Even a solution of (4.10)--(4.11) and of the positive seam clauses does
   not embed in the IRRC16 legal-history graph.  IRRC16 imposes both signs
   of residence.  The unchanged rank-eight source rail has 2,010 short
   zero-gaps, so the advertised source-relative repair, which changes only
   the rank-seven rail, leaves illegal memory-three windows frozen.

This note proves the exact necessary-and-sufficient history-lift theorem.
For an orientation-coherent cut-and-rethread it reduces to nine swap-label
disjointness tests at each new seam.  A `60`-orbit (`900`-edge) rethread
which passed those tests on a previously legal factor would induce a signed
history circulation supported on at most `7,200` state arcs, or at most
`480` translation orbits.  The current FRR source is not such a previously
legal factor.

## 1. Canonical lift of a physical factor

Let `J=J(16,8)`.  Orient every component of a spanning two-factor `F` and
write its successor permutation as `s`.  For a physical transition `XY`,
put

\[
 \sigma(XY)=X\triangle Y.
\tag{1.1}
\]

Let `H_3` be the legal history graph of
`THREAD_A_K16_UNRESTRICTED_RAINBOW_BIRESIDENT_FACTOR_NORMAL_FORM_20260729.md`:
its vertices are directed three-edge histories whose three swap labels are
pairwise disjoint, and an arc appends a fourth transition precisely when its
label is disjoint from the preceding three.

For an oriented factor `F`, define its canonical order-three lift by

\[
 a_X:
 (s^{-3}X,s^{-2}X,s^{-1}X,X)
 \longrightarrow
 (s^{-2}X,s^{-1}X,X,sX)
\tag{1.2}
\]

for every owner `X`, whenever (1.2) is an arc of `H_3`.

### Theorem 1.1 (canonical history-lift theorem)

For an oriented spanning two-factor `F`, the following are equivalent.

1. Every one-run and every zero-run of every coordinate on every component
   has length at least four.
2. Formula (1.2) is defined for every owner and its indicators form a binary
   circulation on `H_3` with one selected outgoing arc in every terminal-
   owner fibre.

When these conditions hold, the lift is unique for the chosen component
orientations.  Reversing an entire component replaces its lift by the
reversed history cycle and changes no physical edge or colour.

#### Proof

The full residence condition is equivalent to disjointness of the labels
of any two transitions at cyclic distance one, two, or three.  Hence each
four-transition window in (1.2) is legal, and successive windows overlap in
their last three vertices.  They therefore form directed cycles in `H_3`,
one arc over every physical owner.

Conversely, the overlap rule in `H_3` forces every four consecutive
transitions in every projected cycle to have pairwise disjoint labels.
Thus repeated changes of a coordinate have cyclic separation at least four,
which is exactly the two-sign residence condition.  Once `s` and the
orientation are fixed, the preceding three owners of `X` are fixed, so
(1.2) is the only possible lift.  QED.

In particular, a positive-resident factor with a short zero-gap is not a
partial point of IRRC16.  Its offending four-window is not a vertex/arc of
`H_3` at all.

## 2. Exact sparse correction theorem

Suppose `F_0` and `F_1` are fully resident spanning two-factors.  Choose
component orientations, and let `y_0,y_1` be their canonical lifts.  Put

\[
 z=y_1-y_0.
\tag{2.1}
\]

Let `A` be the directed incidence matrix of `H_3`, let `B` sum outgoing
history arcs by terminal physical owner, and let `P^-,P^+` project history
arcs to their lower and upper physical colours.

### Theorem 2.1 (signed history correction)

The correction (2.1) satisfies

\[
 Az=0,\qquad Bz=0,
\tag{2.2}
\]

\[
 P^-z=\ell(F_1)-\ell(F_0),\qquad
 P^+z=u(F_1)-u(F_0),
\tag{2.3}
\]

and

\[
 -y_0\le z\le1-y_0.
\tag{2.4}
\]

Conversely, any integral `z` satisfying (2.2), (2.4), and such that
`y_0+z` is binary projects to a fully resident spanning directed
two-factor; the palette requirements are exactly the corresponding lower
bounds on `P^-(y_0+z)` and `P^+(y_0+z)`.

#### Proof

Both `y_0` and `y_1` are circulations with one unit in every owner fibre,
so subtraction gives (2.2).  Projection gives (2.3), and binary incidence
gives (2.4).  Conversely, Theorem 5.2 of the IRRC16 note applies directly
to `y_0+z`.  QED.

Thus the exact algebraic trade lattice is

\[
 \ker_{\mathbb Z}\!\begin{pmatrix}A\\B\end{pmatrix},
\tag{2.5}
\]

with the binary box and palette inequalities retained.  Degree balance in
the physical graph is only the projection of (2.2); it is not sufficient
for a history lift.

## 3. The nine seam inequalities

There is a useful physical form of the history condition for collar
rethreading.  Cut `h` directed edges of an oriented factor.  Assume that
every four-transition window lying wholly in a retained piece is legal and
that the retained pieces are directed paths with at least three retained
edges each.  Join their tails to heads by `h` new Johnson edges, without
reversing any retained path.  Around a new seam write the transition labels
as

\[
 \alpha_3,\alpha_2,\alpha_1, c,
 \beta_1,\beta_2,\beta_3,
\tag{3.1}
\]

where `c` is the new seam, `alpha_1` and `beta_1` are its immediate old
neighbours, and subscripts record distance from the seam.

### Theorem 3.1 (exact seam-history criterion)

The rethreaded factor is fully resident if and only if every new seam
satisfies the following nine disjointness tests:

\[
 c\cap\alpha_i=c\cap\beta_i=\varnothing
 \quad(1\le i\le3),
\tag{3.2}
\]

and

\[
 \alpha_1\cap\beta_1=alpha_1\cap\beta_2
 =\alpha_2\cap\beta_1=\varnothing.
\tag{3.3}
\]

Here labels are regarded as two-element coordinate sets.  If, in addition,
the factor before cutting was itself fully resident, then (3.2)--(3.3)
induce a signed history correction supported on at most `8h` arcs.

#### Proof

All pairs of transitions at cyclic distance at most three which lie wholly
inside a retained path were already legal.  A pair crossing the new seam
either contains `c`, giving the six tests (3.2), or has one old edge on each
side.  Its distance is at most three exactly for the index pairs
`(1,1),(1,2),(2,1)`, giving (3.3).  The lower bound of three retained edges
between consecutive seams ensures that two seam edges are at distance at
least four.  This proves necessity and sufficiency.

If the old factor was fully resident, it has a canonical history lift.  A
canonical history arc projected on an unchanged transition is unchanged
whenever its preceding three transitions contain no seam.  Hence at most
the seam arc and the next three lifted arcs change per old seam, and the
same bound holds per new seam.  There are `h` of each, so at most `8h`
signed state arcs occur.  QED.

If an endpoint matching reverses a retained path, the physical edge support
can still be small but the history support generally contains the whole
reversed path.  Direction coherence is therefore necessary for the stated
`8h` sparse bound, though not for physical feasibility.

For a translation-equivariant minimum FRR cut, `h=60*15=900`.  A
direction-coherent fully legal rethread would consequently give

\[
 |\operatorname{supp}z|\le7200,
\tag{3.4}
\]

and, equivariantly, at most `8*60=480` history-arc orbits.  This is a
conditional embedding bound, not an existence statement.

## 4. Audit of the source-relative equations

For `U` of rank eight in `[15]`, the old selector
`p_0(U)={a_U^0,b_U^0}` chooses the edge with endpoints
`U-a_U^0,U-b_U^0`; a replacement selector `p(U)={a_U,b_U}` does the same.
Changing selectors only on `H` changes the degree of a rank-seven owner by

\[
 \sum_{U\in H}
 \bigl({\bf1}_{U-a_U}+{\bf1}_{U-b_U}
       -{\bf1}_{U-a_U^0}-{\bf1}_{U-b_U^0}\bigr).
\tag{4.1}
\]

Thus equation (4.10) is exactly degree preservation.  The lower colour of
the selected edge at `U` is `U-p(U)`, so equation (4.11) is exactly lower
palette survival.  Since the edge at `U` continues to have union `U`, every
upper colour remains present exactly once.

At the incidence-graph level, the signed change is balanced at rank eight
(two old and two new incidences at every changed `U`) and (4.10) balances it
at rank seven.  It therefore decomposes into alternating even circuits.
This verifies the alternating-circuit statement following (4.11).
However, that decomposition does not choose a successor orientation and
does not imply (3.2)--(3.3).  The missing data are precisely a coherent
ordering of the circuit pieces and the legal order-three boundary states.

### Proposition 4.1 (what the 60-orbit certificate proves)

In the stated `Z_15`-equivariant quotient class, the certified value `60`
proves only that every selector repair of the facet derivative must change
at least 60 upper-colour orbits, and that a cut set of 60 orbits exists
which meets all 95 short-positive-run collar orbits.  It does not prove any
of the following:

* a choice of new pairs `p(U)` satisfying (4.10);
* the lower inequalities (4.11);
* an endpoint matching or direction-coherent rethread;
* the nine seam inequalities; or
* any condition on short zero-gaps.

#### Proof

The certificate is a transversal calculation on old collar intervals.  Its
variables say only whether an old edge orbit is cut.  Replacement pairs and
new incidences do not occur in that optimization.  QED.

## 5. Exact obstruction to embedding the advertised FRR move in IRRC16

The source-relative construction retains the certified rank-eight source
rail `F^+` unchanged and attempts to repair only its rank-seven facet
derivative.  The unchanged source has the audited short zero-gap census

\[
 1^{330}2^{585}3^{1095},
\qquad 330+585+1095=2010.
\tag{5.1}
\]

### Theorem 5.1 (frozen-shore obstruction)

No modification confined to the rank-seven facet rail, including any
solution of FRR(7,4) and any hypothetical 60-orbit solution of
(4.10)--(4.11), is a sparse correction from the advertised no-cross source
factor to an IRRC16 circulation.

#### Proof

Every gap in (5.1) gives two transitions of the unchanged rank-eight rail
whose labels share its coordinate and whose cyclic distance is one, two,
or three.  Hence the associated four-transition window violates the legal
history condition.  A repair confined to the other shore changes neither
transition nor its successor relation.  By Theorem 1.1 the final no-cross
factor therefore has no binary lift to `H_3`.  QED.

There is a second, independent warning on the facet rail itself.  For a
binary source trace `t_i`, the facet trace is

\[
 x_i=t_i t_{i+1}.
\tag{5.2}
\]

A bounded zero-gap of length `g` in `t` becomes a zero-gap of length
`g+1` in `x`.  Since every positive source run has length at least four,
distinct zero-gaps do not merge under (5.2).  Therefore the facet derivative
has exactly

\[
 330+585=915
\tag{5.3}
\]

short zero-gaps, in addition to its 1,425 short positive runs.  The
60-orbit transversal was optimized only against the latter collars.  It
may intersect some dual collars, but no simultaneous dual-transversal
claim has been proved.

## 6. Exact surviving conditional theorem

The FRR architecture can feed IRRC16 only after the following strengthening.

### Corollary 6.1 (bi-FRR physical history embedding)

Suppose that:

1. the unchanged rank-eight rail is fully biresident;
2. a cut set `H` meets every positive- and zero-run illegal window of the
   old rank-seven facet factor;
3. replacement selectors satisfy (4.10), and (4.11) preserves every lower
   colour;
4. the exposed paths admit a direction-coherent endpoint matching;
5. every retained path has at least three edges; and
6. all nine inequalities (3.2)--(3.3) hold at every new seam.

Then the two no-cross rails have a binary IRRC16 lift.

If, in a different application, the factor before cutting is already fully
biresident, then a `60`-orbit edit has a signed history correction supported
on at most `480` history-arc orbits.  The actual FRR source is not in that
situation, so its final lift (if one is found) cannot be expressed as a
sparse difference from an integral source lift.

Conversely, under the no-cross, retained-path, and direction-coherent
hypotheses, every final IRRC16 lift yields selectors satisfying
(4.10)--(4.11) and the nine seam inequalities.

#### Proof

Condition 3 restores the physical degree and palette constraints; upper
colours are fixed by their `U` indices.  Conditions 1, 2, 4--6 and Theorem
3.1 give full residence on both rails.  Theorem 1.1 gives the binary IRRC16
circulation.  When the source is itself legal, Theorem 2.1 and the support
part of Theorem 3.1 give the stated sparse difference.  Projection proves
the converse.  QED.

Thus the smallest source-relative missing statement compatible with
IRRC16 is not the one-sign `FRR(7,4)`.  It is a **bi-FRR** endpoint
rethread satisfying the nine seam tests, together with a fully legal
opposite rail.  Alternatively one must abandon sparse source-relative
repair and alter the opposite rail as well.

## 7. Adversarial audit

1. The obstruction in Theorem 5.1 is not a claim that no unrestricted
   `K=16` factor exists.  It rejects only the proposed embedding of a
   one-shore FRR edit into the full two-sign IRRC16 graph.
2. The support bound `8h` requires orientation coherence.  An undirected
   endpoint matching which reverses long retained paths may have small
   physical symmetric difference but large history-coordinate support.
3. Equations (4.10)--(4.11) remain valid and useful for the one-sided target;
   the gap is chronology, not an algebraic error in those equations.
4. The 915 dual defects in (5.3) are a census of initial facet defects, not a
   lower bound on the number of additional cuts.  One cut can meet collars
   of both signs.  No union-transversal number is asserted here.
5. A correction of the dense symmetric fractional point is never sparse in
   the same sense: that point spreads its owner unit over all legal outgoing
   history arcs, whereas a binary solution selects one.  The sparse theorem
   applies to differences of two integral legal lifts.

## 8. Precise remaining lemma

The first theorem not supplied by the existing FRR certificate is:

> **Legal bi-FRR circulation.**  Find a cut set and replacement selectors
> satisfying (4.10)--(4.11), a direction-coherent endpoint rethread, and the
> nine seam inequalities for both signs, while simultaneously providing a
> fully biresident opposite rail; or prove that the corresponding signed
> kernel system (2.2)--(2.4) has an integral separating cut.

The minimum positive-collar value `60` is input to that problem, not its
solution.
