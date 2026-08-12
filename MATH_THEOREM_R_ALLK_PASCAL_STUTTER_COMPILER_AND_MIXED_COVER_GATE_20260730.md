# Pascal stutters, curvature cost, and the exact mixed-cover compiler gate

Date: 2026-07-30  
Lane: R  
Status: pure mathematics.  The carrier-stutter theorem, the curvature lower
bound, the one-cell two-fan seam identity, and the bounded common-`Q`
obstruction theorem are proved below.  They give an exact conditional
`B(k)+O(1)` route and quantified finite obstructions to obtaining it by raw
Pascal transport plus owner repetitions.  No all-`k` existence claim or
asymptotic divergence of the repetition cost is proved.

## 0. Result and proof boundary

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad d=d(k),
 \qquad B(k)=W+d,
\]

where `d(k)` is the monotone-deadline value.  The exact carrier/compiler
factorization says that an upper-complete middle chronology `T`, together
with a feasible literal `COMP_d(T)`, gives a word of length `|T|+d`.

This note adds four facts.

1. Repeating selected middle owners consecutively never destroys middle
   ownership or an arbitrary-width upper witness.  The minimum number of
   repetitions needed for depth-`d` residence is exactly one weighted
   interval multicover of the short coordinate runs.
2. Its total curvature defect gives an immediate integral lower bound on
   that repetition cost.  If the authenticated `k=11,13,15` facets are
   required at child depth three, raw stuttering needs at least `29,72,204`
   extra middle states respectively.  The first two numbers concern a
   same-depth use such as the direct odd-to-odd facet sector; they do **not**
   apply to the actual depth-dropping lifts `11->12` and `13->14`, whose
   child deadline is two.  The third is the relevant plateau-depth toll for
   `15->16`.
3. Inserting one physical source position has an exact short-cell exchange:
   it destroys `d-1` crossing length-`d` cells and creates two endpoint fans
   containing `2d-1` cells.  The net band gain is exactly `d`, as required by
   the deadline ledger.
4. After sectorwise transport, every failure of one **fixed** literal pin
   table has a small explicit certificate: either one positive interval is
   covered by at most `d+1` negative pins, or one physical position is
   emptied by at most `r` negative pins.  If the sectors are separately
   feasible, every such certificate is necessarily mixed across sectors or
   uses new seam data.  A single core refutes only that selector; the global
   additive toll is the optimized deletion deficiency `eta`, not the mere
   existence of one core.

Together these give the following exact conditional upper bound.  For an
upper-complete exact-owner chronology `T`, let `tau_d(T)` be its minimum
stutter cost and define

\[
 \eta_d^{\rm opt}(T)=
 \min\{\eta_d({\rm St}_y(T)):c(y)=\tau_d(T),\ y\text{ satisfies (2.2)}\}.
\]

Then

\[
 \boxed{\nu(k)\le B(k)+\tau_d(T)+\eta_d^{\rm opt}(T).}
\tag{0.1}
\]

Consequently a uniform bound

\[
 \tau_d(T)+\eta_d^{\rm opt}(T)=O(1)
\tag{0.2}
\]

for a Pascal-recursive carrier family would prove
`nu(k)<=B(k)+O(1)`.  The two terms in (0.2) are literal and integral.  The
first is an interval multicover; the second is the exact common-`Q` compiler
deficiency.  Neither is implied by owner decks, marginal shadow coverage, or
separate sector compilers.

The independently verified `k=16` word of length `B(16)+1` is consistent
with the target scale, but no audit identifies its third derivative as a
one-stutter Pascal carrier.  It is therefore not used as evidence for the
stutter hypothesis.

## 1. Carrier/compiler notation

Let

\[
 T=(T_0,\ldots,T_{M-1}),\qquad |T_i|=r,
\tag{1.1}
\]

be a linear set chronology on `[k]`.  It is **owner-complete** if every
rank-`r` set occurs at least once, and **upper-complete** if every target of
rank greater than `r` is the union of a contiguous interval of `T`.

For a source word

\[
 A=(A_0,\ldots,A_{M+d-1}),
\]

write `D^d A=T` for

\[
 T_i=\bigcup_{p=i}^{i+d}A_p\qquad(0\le i<M).
\tag{1.2}
\]

Let

\[
 {\cal L}_{<r}=\{S\subseteq[k]:1\le |S|<r\}.
\]

Define the **literal compiler deficiency**

\[
 \eta_d(T)=\min_A
 \left|{\cal L}_{<r}\setminus
   \left\{\bigcup_{p=a}^b A_p:b-a+1\le d\right\}\right|,
\tag{1.3}
\]

where the minimum is over nonzero words satisfying (1.2), and put
`eta_d(T)=infinity` if no such word exists.  Since every interval of at most
`d` source letters is contained in one central window, its union has rank at
most `r`.  Thus (1.3) measures exactly the strict lower targets missing from
the compiler; it does not mix in middle or upper targets.

### Theorem 1.1 (deficiency-to-word theorem)

If `T` is owner-complete and upper-complete and `eta_d(T)<infinity`, then

\[
 \boxed{\nu(k)\le M+d+\eta_d(T).}
\tag{1.4}
\]

#### Proof

Choose `A` attaining (1.3).  Equation (1.2) gives every middle owner.  If
`Y` is an upper target and

\[
 Y=T_a\cup\cdots\cup T_b,
\]

then associativity gives

\[
 Y=A_a\cup\cdots\cup A_{b+d}.
\tag{1.5}
\]

Thus `A` already covers the middle and upper ideals and all but
`eta_d(T)` lower targets.  Append each missing nonempty lower target as one
literal source letter.  Every old interval remains an interval of the
extended word, and each appended singleton supplies its target.  The final
length is (1.4).  \(\square\)

This harmless append step is used only for an upper bound.  It does not
claim that the extended word retains the flat derivative (1.2).

## 2. Exact owner-stutter theorem

For integers `y_i>=0`, let `St_y(T)` be the chronology obtained by replacing
`T_i` by `1+y_i` consecutive copies.  Put

\[
 c(y)=\sum_{i=0}^{M-1}y_i.
\tag{2.1}
\]

For a coordinate `x`, let `R_x(T)` be the family of maximal internal
one-runs in its binary trace on `T`.  A run `R` is an interval of owner
indices, and its old length is denoted `|R|`.

### Theorem 2.1 (exact stutter multicover)

The chronology `St_y(T)` is depth-`d` resident if and only if

\[
 \boxed{
 \sum_{i\in R}y_i\ge(d+1-|R|)^+
 \quad(x\in[k],\ R\in R_x(T)).}
\tag{2.2}
\]

Consequently the minimum stutter cost is the integer interval multicover

\[
 \boxed{
 \tau_d(T)=
 \min\left\{\sum_i y_i:
 y_i\in{\mathbb Z}_{\ge0},\ (2.2)\right\}.}
\tag{2.3}
\]

Stuttering preserves owner-completeness and upper-completeness.

#### Proof

Stuttering changes no zero-to-one or one-to-zero transition of any
coordinate trace.  It therefore preserves the run identities, and a run
`R` acquires exactly

\[
 \sum_{i\in R}y_i
\]

additional one-states.  The binary residence theorem says that a depth-`d`
preimage exists coordinatewise exactly when every internal one-run has
length at least `d+1`.  This is precisely (2.2), proving (2.3).

Every old owner remains present.  If `[a,b]` is an old upper witness, the
interval in the stuttered word from the first copy of `T_a` through the last
copy of `T_b` has the same union.  Hence every old upper witness survives.
\(\square\)

Boundary one-runs are deliberately absent from (2.2): the linear residence
criterion clips them.  For a cyclic carrier all runs are included.  After a
cyclic carrier is opened, a run cut by the opening becomes two one-sided
boundary runs and no longer contributes an internal constraint.

### Corollary 2.2 (an exact conditional `B+c` theorem)

Let `T` be an upper-complete permutation of the rank-`r` layer, let
`d=d(k)<r`, and choose an optimal stutter `T'=St_y(T)`.  Then

\[
 \boxed{
 \nu(k)\le B(k)+\tau_d(T)+\eta_d(T').}
\tag{2.4}
\]

#### Proof

Here `|T'|=W+tau_d(T)`.  Apply Theorem 1.1.  \(\square\)

If the unstuttered transitions are Johnson or equal, (2.2) also makes the
maximal erosion nonempty when `r>d`.  Indeed, among any `d` transitions the
same coordinate cannot be deleted twice: between two deletions it would
have an internal one-run of length at most `d`.  Hence the `d+1` involved
rank-`r` states have intersection rank at least `r-d>0`.  The maximal
erosion is therefore one admissible nonzero preimage, so `eta_d(T')` is
finite.

## 3. Curvature lower bound and Pascal specialization

Define the linear residence deficit

\[
 \Psi_d(T)=
 \sum_{x\in[k]}\sum_{R\in R_x(T)}(d+1-|R|)^+.
\tag{3.1}
\]

For a cyclic chronology this is the event defect
`Phi^-_(d+1)` from the run-curvature theorem.

### Theorem 3.1 (curvature costs physical stutters)

If every owner has rank `r`, then

\[
 \boxed{
 \tau_d(T)\ge
 \left\lceil{\Psi_d(T)\over r}\right\rceil.}
\tag{3.2}
\]

More generally, for a coordinate subset `X`, if every owner contains at
most `s_X` members of `X`, then

\[
 \tau_d(T)\ge
 \left\lceil{
 {\sum_{x\in X}\sum_{R\in R_x(T)}(d+1-|R|)^+
  \over s_X}\right\rceil.
\tag{3.3}
\]

#### Proof

Sum (2.2) over the indicated runs.  At a fixed owner position `i`, the
variable `y_i` is counted once for each deficient run containing `i`.
There is at most one such run per coordinate, and only coordinates present
in `T_i` can count.  Thus its coefficient is at most `r`, or at most `s_X`
after restriction to `X`.  Therefore

\[
 \Psi_d(T)
 \le\sum_i r y_i
 =r c(y),
\]

and similarly for (3.3).  Minimize over feasible `y`.  \(\square\)

The bound is a genuine physical cost: one repeated owner can lengthen at
most one current run for each coordinate it contains.  It is stronger than
the statement that every short run must merely be hit once when deficits
larger than one occur.

### Corollary 3.2 (facet-stutter obstruction)

Let `T` be a rank-`r` strict Johnson chronology with no singleton one-run,
so that `partial T` is again strict.  A parent one-run of length `ell`
becomes an old-coordinate facet run of length `ell-1`.  Therefore the exact old-coordinate stutter
deficit for child depth `e` is

\[
 \Psi^{\partial}_e(T)
 =\sum_{x,R}(e+2-|R|)^+.
\tag{3.4}
\]

Every facet owner contains exactly `r-1` old coordinates.  Any repair which
only repeats facet owners, without changing their order or edges, therefore
uses at least

\[
 \boxed{
 c_{\partial}\ge
 \left\lceil{\Psi^{\partial}_e(T)\over r-1}\right\rceil.}
\tag{3.5}
\]

The same statement applies to the `A={x,y}+partial T` sector of the direct
four-sector odd-to-odd Pascal braid.  New-coordinate residence can impose
additional constraints; ignoring it only weakens the lower bound.

#### Proof

The Pascal event identity sends every run pair `(ell,g)` to
`(ell-1,g+1)` on the facet.  Apply (3.3) to the old-coordinate set.  \(\square\)

There is a dual statement for union sectors.  A zero-gap of length `g`
becomes length `g-1` under `nabla`; repeating a union owner lengthens the
zero-gaps of precisely the old coordinates absent from that owner.  Thus
the analogous zero-gap defect divided by the maximum number of absent old
coordinates per owner is a lower bound for a stutter-only dual-gap repair.

### 3.1 Audit against the authenticated odd bases at a specified child depth

The solver-free Pascal curvature audit records, after the authenticated
openings, respectively

\[
 142,\qquad429,\qquad1424
\tag{3.6}
\]

internal facet runs of length three arising from the `k=11,13,15`
depth-three packages.  If that facet is required to be depth-three resident,
each needs one unit.  The parent middle ranks are `6,7,8`, so the facet
old-coordinate ranks are `5,6,7`.  Formula (3.5) then gives

\[
 \boxed{
 \left\lceil{142\over5}\right\rceil=29,
 \quad
 \left\lceil{429\over6}\right\rceil=72,
 \quad
 \left\lceil{1424\over7}\right\rceil=204.}
\tag{3.7}
\]

Before opening, the corresponding cyclic counts are `143,429,1425` and,
again at child depth three, give the same three rounded bounds.  These
numbers are quoted from the
independently audited run-curvature ledger in
`MATH_THEOREM_K_THREE_SHELL_BRG_TYPED_CONTAINMENT_FLOW_AND_CURVATURE_OBSTRUCTION_20260730.md`;
no new finite enumeration is used here.

The deadline distinction is decisive.  In the actual odd-to-even lifts

\[
 d(12)=d(14)=2,
\]

so a length-three facet run already meets the required threshold and the
first two stutter costs are zero for `11->12` and `13->14`.  The bounds
`29,72` apply only when the same facets are demanded at child depth three,
for example in the direct odd-to-odd `A={x,y}+partial T` sector.  Since
`d(15)=d(16)=3`, the bound `204` does apply to the plateau lift `15->16`.

Equation (3.7) is otherwise scoped exactly.  It excludes a small number of
pure owner repetitions as the same-depth repair of those fixed facet
interiors.  It does not exclude a deadline drop, a different parent, new
cuts which destroy the motifs, edge-changing shadow braids, or a nonzero-
curvature compound trade.

## 4. The exact one-cell two-fan identity

Let `B_(n,d)` be the set of intervals of lengths `1,...,d` on an `n`-point
line.  Insert a new point `*` at an internal cut with at least `d-1` old
points on both sides.

Transport an old interval as follows.

* If it lies on one side of the cut, use the order-preserving copy.
* If it has old points on both sides and length at most `d-1`, use its new
  convex hull, whose length is one larger.
* A crossing old interval of length `d` has no short transported hull.

For `1<=j<=d`, let `L_j` be the length-`j` interval ending at `*`, and let
`R_j` be the length-`j` interval starting at `*`.

### Theorem 4.1 (two-fan seam exchange)

Under the transport above:

1. exactly `d-1` old band cells are lost, namely the crossing length-`d`
   intervals;
2. every new band cell outside the transport image belongs to

   \[
   {\cal F}_*=\{L_1,\ldots,L_d,R_1,\ldots,R_d\},
   \tag{4.1}
   \]

   where `L_1=R_1`, so `|F_*|=2d-1`;
3. consequently

   \[
   |B_(n+1,d)|-|B_(n,d)|=(2d-1)-(d-1)=d.
   \tag{4.2}
   \]

#### Proof

An old length-`j` interval crosses the cut in exactly `j-1` ways.  Its hull
has new length `j+1`, so precisely the `d-1` crossing intervals of old
length `d` leave the band.

A new short interval which avoids `*` is the transport of one old
one-sided interval.  If it contains old points on both sides of `*`, deleting
`*` gives the unique old crossing interval whose hull it is.  The remaining
new intervals have `*` as one endpoint.  These are exactly the two fans in
(4.1), with their singleton shared.  This proves the first two assertions.
The last is subtraction.  \(\square\)

Equation (4.2) is the local form of the global deadline identity

\[
 |B_(W+d+c,d)|
 =dW+{d+1\choose2}+dc.
\tag{4.3}
\]

One extra physical letter contributes `d` net short cells, but locally it
offers `2d-1` fan cells because `d-1` old crossing depth-`d` cells must be
repaid.  Thus the correct seam object is a two-fan exchange, not `d`
independent free slots.

## 5. Exact bounded common-`Q` obstruction for a fixed selector

Fix a proposed carrier `T` of length `M` and deadline `d`.  Its maximal
envelope at source position `p` is

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(p,M-1)}T_i.
\tag{5.1}
\]

Let a pin table assign distinct lower targets `S` to short physical
intervals `I_S` of length at most `d`.  For each coordinate put

\[
 Q_x=\{p:x\in P_p\}
 \setminus\bigcup_{S:x\notin S}I_S.
\tag{5.2}
\]

The central positive requirements are `([i,i+d],x)` for `x in T_i`, with
the usual clipped endpoint convention.  The lower positive requirements
are `(I_S,x)` for `x in S`.

### Theorem 5.1 (small mixed-cover certificate)

The pin table fails the exact common-`Q` test if and only if at least one of
the following occurs.

1. **Positive-cover core.**  There is one central or lower positive
   requirement `(I,x)` such that

   \[
   \{p\in I:x\in P_p\}
   \subseteq\bigcup_{S:x\notin S}I_S.
   \tag{5.3}
   \]

   Whenever (5.3) holds, it already holds using at most `|I|<=d+1`
   negative pins.
2. **Empty-position core.**  There is a source position `p` such that every
   coordinate of `P_p` is deleted there by a negative pin.  Whenever this
   holds with `P_p` nonempty, at most `|P_p|<=r` negative pins certify it.
   If `P_p` is empty, no negative pin is needed.

If sector pin systems are separately common-`Q` feasible, every obstruction
core for their union contains data from at least two sectors or contains a
new seam/boundary positive requirement or negative pin.

#### Proof

The exact common-`Q` theorem says feasibility is equivalent to

\[
 Q_x\cap I\ne\varnothing
\tag{5.4}
\]

for every positive requirement and to

\[
 \{x:p\in Q_x\}\ne\varnothing
\tag{5.5}
\]

at every source position.  Failure of (5.4) is exactly (5.3).  For each
point of its left side choose one negative pin covering that point.  There
are at most `|I|` points, and a central interval has length `d+1` while a
lower interval has length at most `d`.  This gives the stated subcertificate.

Failure of (5.5) says that, for every `x in P_p`, some negative pin omitting
`x` contains `p`.  Choose one such pin per coordinate.  This uses at most
`|P_p|<=r` pins.  The two failure types exhaust the exact theorem.

Finally, a core wholly inside one old sector and using no new requirement or
pin would already contradict the assumed feasibility of that sector's pin
system.
\(\square\)

The positive-cover core is the exact compiler cocycle missed by marginal
Hall.  It is a **cover**, not a capacity overload: several negative pin
intervals can jointly erase the last occurrence of one coordinate even
though every target has a distinct cell and every physical position remains
nonempty.  The resident `k=6` collar

\[
 136,123,124,145
\]

with singleton pins `3` and `2` is the smallest audited instance: the two
negative pins jointly cover the two legal positions of coordinate `1` in
the central `123` window.

This is a certificate for the displayed pin table only.  It may be escaped
by moving one of its pins, choosing a different stutter, or omitting one
target and appending that target literally.  Equivalently, the exact global
compiler cost is the minimum number of target deletions needed to select a
core-free table, which is precisely `eta_d(T)` from (1.3).  The small-core
theorem makes each failed selector locally auditable; it does not assert
that one failed selector forces `eta_d(T)` to grow.

## 6. A reusable one-credit shadow--braid theorem

The preceding facts combine into a precise additive theorem.

### Theorem 6.1 (one-cell seam credit)

Fix `k,r,d`.  Start with an injective pin table assigning every strict lower
target to a short cell on a source line of length `W+d`, and insert one new
physical source position at an internal cut.  Suppose a proposed braid has a
final middle chronology `T'` of length `W+1` with the following properties.

1. Every rank-`r` owner occurs and every upper target is the union of a
   contiguous interval of `T'`.
2. `T'` is assembled from internally valid Pascal pieces on the enlarged
   source line and passes the direct depth-`d` residence/envelope test; all
   carrier changes not already transported are included in its declared
   collar.
3. Every old selected lower pin except those on the `d-1` lost crossing
   length-`d` cells of Theorem 4.1 transports to its new cell.
4. The targets of those lost pins, together with every genuinely new seam
   lower obligation, admit an injective assignment to the `2d-1` fan cells
   (or to other declared free cells).
5. The full transported-and-new pin table has no obstruction of Theorem
   5.1.

Then there is a universal word of length

\[
 W+d+1=B(k)+1.
\tag{6.1}
\]

More generally, `s` pairwise collar-disjoint one-cell seam credits satisfying
the analogous joint pin conditions give length `B(k)+s`.

#### Proof

Theorem 4.1 proves that item 4 uses actual distinct short cells in the final
band.  Items 3--4 therefore give an injective cell for every strict lower
target.  Item 5 is exactly the common-`Q` positive-hit and nonzero test, so
the maximal common-`Q` word is nonzero, has depth-`d` row `T'`, and realizes
every selected lower pin.  Item 1 and the derivative identity (1.5) give all
middle and upper targets.  The word has `|T'|+d=W+d+1` letters.  Disjoint
insertions add their physical positions and fan ledgers, and the one global
common-`Q` test handles any remaining interaction.  \(\square\)

The theorem is deliberately conditional on one **physical** final carrier.
Pascal's facet/union identities supply the intact owner and shadow pieces,
but do not imply items 2, 4, or 5.  Conversely, no other hidden compiler or
integrality condition remains once those items pass.

### Corollary 6.2 (exact bounded-seam route to `B+O(1)`)

Suppose an odd/even Pascal recursion can be chosen so that, uniformly in
`k`,

* at most `s_0` one-cell seam credits are used;
* every residual short run is paid by those inserted carrier states; in the
  owner-stutter specialization this says `tau_d<=s_0`;
* all upper seam signatures survive or are repaired in the same final
  carrier; and
* after optimizing the two-fan assignments, their mixed-cover deletion
  deficiency is at most a constant `h_0`.

Then

\[
 \boxed{\nu(k)\le B(k)+s_0+h_0}
\tag{6.2}
\]

through that recursion.

#### Proof

Delete an optimal family of at most `h_0` lower targets from the residual
pin table.  By definition of the deletion deficiency, the remaining table
passes the one global common-`Q` test.  Apply the multi-credit form of
Theorem 6.1 to obtain a word of length at most `B(k)+s_0` covering every
other target, and append the deleted targets as literal nonzero letters.
This gives (6.2).  \(\square\)

At child depth three, the authenticated raw Pascal facets require the finite
stutter tolls in (3.7).  Only `204` is an odd-to-even plateau toll: a uniform
budget below `204` fails on the listed `15->16` raw facet, whereas the
deadline drops make the corresponding `11->12` and `13->14` tolls zero.
This does not prove that the plateau toll is unbounded with `k`.  A uniform
bounded-overhead proof based on raw plateau Pascal charts must either prove
a global bound on these multicovers, use an edge-changing curvature repair,
choose different parents, or show that a bounded number of cuts destroys a
much larger short-run family before the one-cell credits are installed.

## 7. Relation to the proved Pascal identities

The result uses, without strengthening, the following already proved facts.

1. The monotone-deadline theorem supplies the lower bound `B(k)` and the
   exact short-band count.
2. The residence theorem identifies binary factorability with the internal
   run threshold and gives the forced run-boundary pair in a strict Johnson
   carrier.
3. The architecture-free carrier/compiler factorization says

   \[
   T\text{ upper-complete}+COMP_d(T)\text{ feasible}
   \Longrightarrow \nu(k)\le |T|+d.
   \]

4. Facet and union transport obey

   \[
   L_q(\partial T)=L_{q+1}(T),\qquad
   U_q(\partial T)=\operatorname{shift}U_{q-1}(T),
   \]

   \[
   L_q(\nabla T)=\operatorname{shift}L_{q-1}(T),\qquad
   U_q(\nabla T)=U_{q+1}(T),
   \]

   and transform run pairs by `(ell,g)->(ell-1,g+1)` and
   `(ell,g)->(ell+1,g-1)`.
5. The exact deadline arithmetic is interlaced:

   \[
   d(2r)\in\{d(2r-1)-1,d(2r-1)\},
   \qquad
   d(2r+1)\in\{d(2r-1),d(2r-1)+1\}.
   \]

Thus the only raw event-buffer loss is one Pascal shell, but (3.7) shows
that one shell can contain many physical short-run occurrences.  Scalar
depth interlacing does not make its repair constant-cost.

## 8. Proved and open boundary

Proved here:

1. the exact owner-stutter residence multicover (2.2)--(2.3);
2. preservation of every owner and arbitrary-width upper witness under
   stuttering;
3. the exact conditional upper bound (2.4);
4. the curvature/stutter lower bounds (3.2)--(3.5);
5. the finite calibrated depth-three lower bounds `29,72,204`, with
   `29,72` explicitly inapplicable to the actual depth-two even children and
   `204` applicable to the `15->16` plateau;
6. the exact two-fan short-cell exchange (4.1)--(4.3);
7. the bounded mixed-cover obstruction theorem (5.1); and
8. the one-credit seam theorem and its `B+s` corollary.

Still open:

1. a Pascal-recursive carrier family with uniformly bounded stutter
   multicover;
2. a nonzero-curvature shadow braid which removes the growing raw facet
   defect while preserving owner and upper support;
3. a uniform bound on the optimized mixed-cover deletion deficiency of the
   two-fan residual assignment;
4. a proof that the resulting carrier has `eta_d=O(1)`, let alone zero; and
5. the unconditional bounds `nu(k)<=B(k)+O(1)` and `nu(k)=B(k)`.

The precise optimized obstruction for this lane is therefore not the
existence of one scalar shadow deficit or one failed selector.  It is the
disjunction

\[
 \boxed{
 \text{unbounded optimized stutter multicover}
 \quad\text{or}\quad
 \text{unbounded optimized compiler deletion number }\eta_d.}
\tag{8.1}

Any successful bounded-overhead Pascal induction must keep both optimized
terms bounded in one physical chronology.  The mixed common-`Q` cores of
Theorem 5.1 are the local certificates used to prove a lower bound on the
second term; one core by itself proves no such unbounded lower bound.

## 9. Adversarial proof audit

A separate proof pass checked the decisive implications with the following
conclusions and corrections incorporated above.

1. The stutter multicover is exact only for internal runs in a linear word;
   boundary runs are correctly omitted.  All runs are charged in the cyclic
   version.
2. The facet formula (3.4) assumes no singleton parent one-run.  Otherwise a
   length-one run vanishes under `partial` rather than becoming a repairable
   zero-length run.
3. The authenticated counts `29,72` are not odd-to-even tolls for the actual
   `11->12` and `13->14` lifts, because those deadlines drop from three to
   two.  Only `204` is the displayed plateau `15->16` toll.  The first two
   numbers apply to an `e=3` use such as the direct odd-to-odd facet sector.
4. At one inserted internal point, an old length-`j` interval crosses the
   cut in `j-1`, not `j`, ways.  Hence the lost count is `d-1`, the two-fan
   count is `2d-1`, and the net gain is exactly `d`.
5. A mixed common-`Q` core is a certificate against one fixed pin selector.
   It is not by itself an additive lower bound.  The correct optimized
   quantity is `eta_d`, the minimum target-deletion deficiency over all pin
   choices.
6. Appending the `eta_d` missing lower masks is legitimate because every old
   interval remains contiguous.  No flat-derivative claim is made after the
   append.
7. The `k=16` length-`B+1` certificate is used only as a numerical
   calibration.  No stuttered-middle, Pascal, or compiler-normal-form claim
   is inferred from it.

No finite search, SAT solver, web source, or unaudited numerical experiment
is used in this report.
