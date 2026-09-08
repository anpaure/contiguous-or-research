# Audit of the 24-owner two-seed Q2 common-carrier obstruction

Date: 2026-07-26

Audited file:
MATH_OBSTRUCTION_K_TWO_SEED_Q2_COMMON_CARRIER_20260726.md.

Method: pure mathematics only.

## 0. Verdict

The local classification and the eight-edge invariant are correct.  A static
exact factor menu on the same 24 owners has net lower type drift at most
\(8/24=1/3\) from the old canonical shore.  It therefore cannot supply the
\(12/24=1/2+o(1)\) displacement required by the three-halves visibility
schedule, and a fortiori cannot supply two full independent
Bernoulli-\(1/3\) erasures.

Terminology should distinguish these last two quantities.  Two simultaneously
visible canonical erasures have drift \(2/3=16/24\); \(1/2=12/24\) is the
time-averaged demand obtained from \(3/2\) visible layers per physical depth.

The implication must retain one chronology qualifier: the invariant compares
the old factor with one final factor on the same carrier.  It does not bound
the sum of absolute signed changes along an oscillating sequence of
intermediate factors.  Such intermediate states matter to a contiguous
window only if they are physically laid out at different times and the
window traverses their interfaces.  That requires context states or vertical
connectors and is a larger joint carrier, such as
\(\mathcal V\square Z\), rather than another factor on \(\mathcal V\).

## 1. Co-degree and canonical-state classification

For
\[
 \mathcal V=
 \{X\cup Y:X\in\binom A2,\ |Y\cap R_1|=|Y\cap R_2|=1\},
\]
the coordinate co-degrees are exactly
\[
 c(i,j)=
 \begin{cases}
 0,&\{i,j\}=R_1\text{ or }R_2,\\
 4,&i,j\in A,\\
 6,&\text{otherwise}.
 \end{cases}
\]
Indeed an \(A\)-pair fixes \(X\) and leaves four reservoir orientations;
an \(A\)-reservoir pair leaves three choices for the other point of \(X\)
and two for the other reservoir orientation; a cross-reservoir pair leaves
all six choices of \(X\).

Hence \(R_1,R_2\) are the unique zero-co-degree pairs and \(A\) is their
intrinsic complement.  A canonical factor is therefore indexed by one of
the three perfect matchings of \(A\).  The canonical state set has size
three, and two distinct nonidentity involutions on it cannot commute:
distinct transpositions in \(S_3\) do not commute.  The no-faithful-\(V_4\)
conclusion is valid.

This classifies canonical pair-frame factors, not every physical
\(Q_2\)-tiling of the carrier.

## 2. Explicit noncanonical tilings

The vertical factor
\[
                         \{X\cup Q_R:X\in\binom A2\}
\]
is an exact six-\(Q_2\) partition.

For the mixed factor, the three special Johnson edges
\[
 \{ab,ac\},\quad\{ad,bd\},\quad\{bc,cd\}
\]
partition \(\binom A2\), and the two reservoir edges
\[
                         \{uw,vw\},\quad\{vx,ux\}
\]
partition the reservoir four-cycle.  Their six Cartesian products are
pairwise disjoint physical \(Q_2\)'s and cover all 24 owners.

Relative to \(P_0=ab\mid cd\mid uv\mid wx\), the four displayed factors
\[
 \mathscr D_{P_0},\quad\mathscr D_{P_1},\quad
 \mathscr D_V,\quad\mathscr D_M
\]
have lower type-one edge counts
\[
                         8,\quad0,\quad8,\quad4.
\]
For \(\mathscr D_M\), all 12 special-direction edges have type zero.
Exactly the two special vertices \(ab,cd\), each appearing over the two
reservoir edges, provide the four type-one reservoir-direction edges.
The table is correct.

## 3. The eight-edge invariant

Let
\[
 S=\{Z\in\mathcal V:ab\subseteq Z\text{ or }cd\subseteq Z\}.
\]
There are exactly eight such owners.  A lower physical edge has one full
\(P_0\)-pair if and only if both endpoints lie in \(S\).  In any cycle
factor, the owner graph is 2-regular, so the total degree incident with
\(S\) is \(16\).  Every internal edge consumes two units of this degree.
Consequently
\[
                         e_{\mathscr F}(S)\le8.
\]

Thus every final factor has at most eight type-one lower edge occurrences.
The old canonical factor attains eight, so for every final factor
\(\mathscr F\),
\[
 \sum_e f_{P_0}(\cap e;\mathscr D_{P_0})
 -\sum_e f_{P_0}(\cap e;\mathscr F)\le8.
\]
After adjoining a frozen exterior core, its constant contribution cancels
from this difference.  Complementation gives the identical upper-excess
bound.

## 4. Relation to the three-halves schedule

One effective reciprocal \(Q_2\) layer has ledger
\[
                         16f_0+8f_1\longrightarrow24f_0,
\]
so it erases a Bernoulli-\(1/3\) contribution.  Matching a Gaussian target
at one new physical depth requires average visible-layer increment
\[
                         {3\over2}+o(1),
\]
or mean type displacement \(1/2+o(1)\).  On 24 owners that is 12 units.
The common-carrier invariant permits only eight.  Therefore:
\[
\boxed{\text{one static 24-owner carrier cannot realize the required
simultaneous two-seed visibility.}}
\]

The invariant does not say that every intermediate switch in a formal
sequence is trivial.  A sequence can oscillate, for example
\(8\to0\to8\to0\), and have large total absolute variation while its
old-to-final decrease remains eight.  Formal intermediate switches are
irrelevant to one final depth-one edge.  They become physically relevant
only if a long row visits the different states successively.  Building
that row requires additional owner/context coordinates and a new exact
joint tiling; it is not contradicted by the 24-owner theorem.

The same qualifier applies to disjoint packets.  Two owner-disjoint packets
commute in one additive factor corner, but no owner sees both switches in
that corner.  Successive global repartitions could expose an owner to
different packets at different times, but literal fusion of those times is
new work and is not ruled out by the additive multiplicity lemma.

## 5. Corrections

Three wording corrections are needed.

1. In the carrier definition, “left brace” should be written as
   \(\left\{\); this is typographical.
2. Phrases saying that intermediate layers have no capacity should be read
   as statements about their old-to-final net depth-one ledger on the same
   static carrier.  They are not a no-go for factor monodromy on an enlarged
   contextual carrier.
3. “Two-exposure demand \(1/2\)” should be split into the exact double-corner
   demand \(2/3\) and the averaged three-halves-schedule demand \(1/2\).
   Likewise the surviving larger-carrier condition should be stated using
   multiplicity-weighted bit incidence, not the union density of eligible
   families.  The necessary average is
   \[
      {|U|}^{-1}\sum_{x\in U}
      \#\{\text{visible removable contributions at }x\}
      \ge {1\over2}-o(1)
   \]
   for the averaged schedule, and \(2/3-o(1)\) for a canonical two-layer
   corner.  Union density at least \(1/2\) is not necessary when two
   contributions can coexist on one occurrence.

With this scope, the obstruction is theorem-level correct.
