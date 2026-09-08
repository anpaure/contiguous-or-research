# Audit of quartet-resolution trades and the structured `CPM` gate

Date: 2026-07-26

Source audited:
`MATH_THEOREM_QUARTET_RESOLUTION_TRADES_AND_STRUCTURED_CPM_GATE_20260726.md`.

## 0. Verdict

The finite carrier factorizations, packet-mass counts, deterministic
near-tiling count, option-union coverage theorem, quadratic derivative,
and conditional reductions

\[
                         \mathrm{HCRT}\Longrightarrow
                         \mathrm{CPM}\Longrightarrow
                         \mathrm{EMSF}
\]

are correct.

The source also correctly labels the multiscale anticorrelation statement
`HCRT` as open.  Four qualifications are needed.

1. The imported Gaussian ratio `R_q(g,u)` is exact for the earlier,
   restricted `Q_4` mosaic, not for the enlarged internal atlas built in
   Sections 1--6 of the source.  The enlarged atlas activates
   `J(4,1)`, every one-factor of `J(4,2)`, and `J(4,3)`.  It therefore has
   compatible sources omitted from the old ratio.  No Gaussian Hall
   deficit uniform over this larger block-internal atlas is proved.
2. The `7/16` calculation is the density of the local owner sector for
   **one fixed pair of quartets**.  Trades attached to several disjoint
   coordinate pairs still overlap as owner sets because their reservoirs
   range over all other coordinates.  A simultaneous “round” over a
   matching of quartet indices needs an additional canonical owner
   assignment or scheduling theorem.
3. Even if a new uniform block-internal Hall cut makes cross-quartet
   transport necessary, one cross-quartet packet has only one
   profile-crossing axis.  At depth `q<r`, only a `q/r` fraction of its
   start windows contain that axis.  Therefore the `7/16` owner supply
   gives only

   \[
                         O\!\left({q\over r}W\right)=o(W)
   \]

   genuinely profile-crossing Gaussian windows when `q<=H=o(r)`.  The
   fixed-mosaic Hall deficit requires `Omega_A(W)` such windows.  A valid
   hierarchy must accumulate `Omega_A(r/q)` cross axes in a typical
   packet, not merely apply one or any bounded number of the displayed
   rounds.
4. `HCRT` is a valid sufficient statement, but not a logically smaller
   reformulation of `CPM`: the condition `Q=o(W)` controls balanced
   multiplicity and is strictly stronger than target coverage alone.
   Moreover a linear owner round contains `Theta(W/R)` local trades, so
   the displayed per-trade quadratic bound permits total positive
   collateral `O(HW)`.  The missing anticorrelation theorem must overcome
   this growing factor `H`; bounded local trade size does not make the
   descent automatic.

The last point is not a refutation of `HCRT`; `HCRT` explicitly demands
linear cross-profile occurrence mass.  It is a missing quantitative
bridge from Theorem 4A.2 to that demand.  The statement that the elementary
atom already has “the correct scale” is false if scale is measured in
depth-`q` occurrences rather than owners.  Before that bridge is even
needed, however, a Hall theorem for the full block-internal atlas must
show that internal resolutions alone still fail.

## 1. Checked local counts

### 1.1 The three `B_4` factorizations

* `J(4,1)=K_4` has the three one-factors in (1.1).
* `J(4,2)=K_6` minus the three complementary pairs.  The four rows in
  (1.3) are perfect matchings, are pairwise edge-disjoint, and exhaust its
  twelve edges.
* Complementation gives the three factors of `J(4,3)`.

Thus the factor count `k(4-k)` is exact.

Tensoring a carrier edge with `Q_(r-1)` gives `Q_r`.  Two distinct
one-factors have:

* a four-cycle union at occupancies one and three, hence owner mass
  `4*2^(r-1)=2R`;
* a six-cycle union at occupancy two, hence owner mass
  `6*2^(r-1)=3R`.

The carrier-exchange square has local owner set
`e times f times Q_(r-1)`, of size

\[
                         4\,2^{r-1}=2R.
\]

All these trades are exact whole-packet replacements.  No seam term is
missing.

### 1.2 The six-packet adapter

On `J(4,2) times Q_r`, the old shore has

* two singleton-carrier copies of `Q_r`; and
* four copies of `Q_2 times Q_(r-2)` on the cross states.

It therefore consists of six `Q_r` packets and covers `6R` owners.  A
factor of `J(4,2)` has three edges; tensoring each with the two
`Q_(r-1)` halves of `Q_r` gives six packets and the same owner set.
Theorem 4.1 is exact.

### 1.3 Cross-quartet factors

For

\[
 V_k^+=\binom Ak\times\binom B{k-1},
 \qquad
 V_k^-=\binom A{k-1}\times\binom Bk,
\]

both shores have size

\[
                         \binom4k\binom4{k-1}.
\]

A plus owner has `k` deletions in `A` and `5-k` insertions in `B`, so
the crossing graph is exactly `k(5-k)`-regular bipartite.  It has a
one-factorization by repeated Hall matchings.

The internal factor exists on both shores; at `k=4` it uses the
occupancy-three layer in the opposite quartet.  Tensoring with
`Q_(r-1)` gives equal packet tilings.  The owner mass is

\[
 \binom4k\binom4{k-1}R\le24R.
\]

Finally,

\[
 2\sum_{k=1}^4\binom4k\binom4{k-1}
 =2(4+24+24+4)=112,
\]

and `112/256=7/16`.  Under rank displacement `o(m)`, a fixed
eight-coordinate restriction is asymptotically uniform, so the local
sector density is indeed `7/16+o(1)`.

The qualification is that sectors for different quartet pairs overlap
as global owner families.  Coordinate-disjointness of the carrier pairs
does not make the associated owner trades disjoint.

## 2. Checked owner near-tiling count

There are `c=floor(m/2)` quartets and at most two residual coordinates.
A quartet has fourteen eligible states of local sizes one, two, or three,
and two ineligible states.  Ignoring the global rank constraint gives

\[
 L_r\le
 4\sum_{e<r}\binom ce14^e2^{c-e}
 =4\,2^c\sum_{e<r}\binom ce7^e.
\]

For `r=o(c)`,

\[
 \log_2\sum_{e<r}\binom ce7^e=o(m),
\]

so

\[
 L_r=2^{m/2+o(m)},
 \qquad
 {L_r\over\binom{2m}m}=2^{-3m/2+o(m)}.
\]

Thus `L_r=o(W/H)` for `H<=m` is correct.

For a fixed occupancy sector, taking one one-factor in every active local
layer and tensoring the edges partitions the sector into `Q_r` packets.
Changing an active carrier must be applied after grouping all tags of the
new carrier into its one-factor edges; with this sector-level grouping,
Theorem 3.1 implements the Johnson-graph exchange of active sets.  Hence
Theorem 5.2 is valid as a statement about the whole occupancy sector, not
about one individually frozen inactive-tag block.

## 3. Checked option-union coverage

Lemma 6.1 is valid: axis permutations prescribe any ordered list of
distinct next directions, and an endpoint translation sends the chosen
start to any specified packet owner.

For a lower target `T` of size `m-q`, at least

\[
 c-|T|/3=m/6+q/3+O(1)
\]

quartets have local occupancy at most two.  Each supplies two absent
coordinates.  Adding one and reserving the other gives `q` desired local
Johnson exchanges and does not destroy eligibility.  The resulting
middle owner is good whenever `T` is quartet-typical.

For an upper target `U`, if `b` quartets have occupancy at least two, then
`|U|<=c+3b`, giving

\[
 b\ge(|U|-c)/3=m/6+q/3+O(1).
\]

Deleting one of two selected occupied coordinates again gives a good
middle owner and the desired upper trace.  Thus Theorem 6.2 is correct.

The non-typical target count is bounded by the same unrestricted count as
the owner leave, and multiplying by `2H<=2m` remains `o(W)`.  This proves
only union reachability.  It gives no simultaneous source assignment,
exactly as the source file warns.

The imported compatible-source ratio

\[
 R_q(g,u)={2^q\binom gq\over\binom{u+q}q}
\]

and its central Gaussian limit `e^(-6A^2)` are correct for the earlier
fixed `Q_4` mosaic.  They do **not** enumerate every source available in
the present resolution atlas.

The discrepancy is visible locally.  In the old mosaic a lower window
can use only a prescribed occupancy-two edge, taking a good singleton
target block to a two-set source block.  In the enlarged atlas:

* an empty target block can be supplied from a singleton source through
  an edge of `J(4,1)`;
* a singleton target has all incident occupancy-two Johnson edges
  available across the four factors, not only the old prescribed edge;
* a two-set target can be supplied from a triple source through an edge
  of `J(4,3)`.

Indeed, these extra cases are used explicitly in the proof of Theorem
6.2, which selects any target quartet of occupancy at most two.  Therefore
the old source family of type `(g-q,h,u+q,...)` is a strict subset of the
new compatible-source family.  Preserving the quartet occupancy vector
of each **owner** does not force the old target-to-source type map.

Consequently the source file has not proved that all trades confined to
Sections 2--3 retain a linear Gaussian Hall deficit.  A new capacity
calculation for the full block-internal compatibility graph is required.
It may produce another deficit, or it may show that the internal atlas
already escapes the old cut.

That graph has a simple exact description at one lower depth, after
restricting the source shore to the retained good owners.  Join
`T in binom([2m],m-q)` to a good `X in binom([2m],m)` precisely when

\[
 T\subseteq X,qquad |X\setminus T|=q,                 \tag{3.1}
\]

the `q` added elements lie in distinct quartets, and every selected
quartet has `|T cap C_i|<=2`.  The last condition is exactly what allows
the added endpoint to lie in a nontrivial Johnson edge.  Every internal
packet window gives an edge of this graph, and the factorization argument
in Theorem 6.2 realizes every such edge in the option union.  The upper
graph is its complement.

Thus the correct fixed-quartet capacity question is a Hall theorem for
this larger graph (and then a simultaneous all-depth selection theorem),
not the old two-parameter ratio `R_q(g,u)`.

## 4. Checked floor energy and reductions

For one target part of size `N`, total mass `S`, and
`c=floor(S/N)`, put

\[
                         Q=\sum_T(Z_T-c)(Z_T-c-1).
\]

If `c>=1`, every hole contributes at least two to `Q`.  If `c=0`, write
the hole count as

\[
 N-|\operatorname{supp}Z|
 =(N-S)+\sum_T(Z_T-1)_+
 \le(N-S)+Q/2.
\]

This proves Proposition 7.1 and, after summing the `2H` parts,

\[
                         \operatorname{Hol}
                         \le2HL_r+Q/2.
\]

The identity

\[
 f(z+d)-f(z)=2(z-c-1/2)d+d^2,
 \qquad f(z)=(z-c)(z-c-1),
\]

proves (7.6).  The norm constants are also correct:

* at most three packets per elementary shore gives `36HR` over `2H`
  signed parts;
* six packets gives `144HR`;
* at most twenty-four packets gives `2304HR`.

The literal-hole derivative `D_tau-G_tau` and its averaging consequence
are exact.

Consequently `Q=o(W)`, together with `L_r=o(W/H)`, implies the aggregate
literal target-hole bound required by `CPM`.  Since every option retains
one common all-depth compiler, the conditional implications to `CPM` and
then `EMSF` are valid.

The converse is false in this level of generality.  Coverage can hold
while the forced excess mass is concentrated on a small target family,
giving large quadratic energy.  Thus `HCRT` is a stronger structured
sufficient gate, not an equivalent reduction of `CPM`.

There is also a useful scale warning.  A disjoint round acting on
`Theta(W)` owners uses `Theta(W/R)` bounded packet trades.  Summing the
upper bounds from Theorem 7.2 gives

\[
                         O(HR)\,{W\over R}=O(HW).       \tag{4.1}
\]

Since `H` grows, the positive square term is not an `o(W)` perturbation.
Any descent proof must obtain a comparably large negative linear term and
then continue until the residual energy is `o(W)`; independent or
sign-blind trade choices do not suffice.

## 5. A conditional occurrence-scale toll

Fix the original quartet decomposition.  Call an active packet axis
*crossing* if its two physical endpoints lie in different quartets.

### Lemma 5.1 (cross-axis dilution)

Let a physical `Q_r` packet be factored into isometric `C_(2r)` cycles,
and suppose it has `s` crossing axes.  At signed depth `q<r`, the number
of its `R=2^r` start occurrences whose `q`-window contains at least one
crossing axis is at most

\[
                         {sq\over r}R.                 \tag{5.1}
\]

#### Proof

Every isometric `C_(2r)` has direction word `pi pi`; each axis occurs
twice.  One occurrence of a direction edge lies in exactly `q` cyclic
windows of length `q`.  Since `q<r`, the two collections of starts for
the two antipodal occurrences are disjoint.  Thus one axis belongs to
exactly a `q/r` fraction of all starts in every cycle.  Sum over the `s`
crossing axes and use the union bound. \(\square\)

A lower or upper trace can move a direction across two quartet blocks
only if its window contains a crossing axis.  Lemma 5.1 therefore gives
an exact count of physically cross-quartet windows.  The later theorem
`MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`,
independently checked in
`MATH_AUDIT_FULL_INTERNAL_QUARTET_HALL_AND_DENSE_CROSS_AXIS_SCHEDULING_20260726.md`,
now proves that such windows are necessary on \(\Omega_A(W)\) based
occurrences at every fixed nonzero Gaussian depth.

The cross shore of Theorem 4A.2 has `s=1`.  Even if it is installed on
`(7/16+o(1))W` owners, one round supplies at most

\[
 \left({7\over16}+o(1)\right){q\over r}W             \tag{5.2}
\]

profile-crossing depth-`q` occurrences.  At
`q=floor(A sqrt(m))` and under the source assumptions

\[
                         q\le H=o(r),
\]

this is `o(W)`, while the fixed-mosaic Hall deficit is
`(delta_A-o(1))W`.

The full internal-atlas Hall theorem proves that a successful endpoint of
the hierarchy must satisfy, in weighted owner average,

\[
                         s=\Omega_A(r/q)               \tag{5.3}

\]

crossing axes per typical packet, or obtain the same occurrence mass by
an equivalent exterior-moving mechanism.  In particular, a bounded number
of elementary cross-quartet rounds cannot suffice.

The earlier baseline argument in Theorem 8.1 was insufficient by itself,
because disagreement with the old mosaic need not cross a quartet.  The new
theorem repairs this exact gap using the invariant number of full quartets,
which is preserved by the **complete** internal atlas.  The second warning
remains: owner mass \(\Theta(W)\) is not by itself crossing-occurrence mass
\(\Theta(W)\); the marked axes must be accumulated and dispersed in the
final packet direction words.

## 6. Proved versus proposed

### Proved

1. All one-carrier, active-carrier, adapter, and one-cross-axis packet
   trades are exact.
2. Their owner masses and target-derivative norm bounds are correct.
3. The deterministic quartet resolution gives an exponentially accurate
   owner near-factor.
4. The union of its internal option atlas has exponentially few immutable
   target holes.
5. The complete block-internal `J(4,k)` atlas has a linear Gaussian Hall
   deficit, through the preserved full-quartet profile.
6. `Q=o(W)` is sufficient for `CPM`, and hence for `EMSF`.
7. Every successful construction needs \(\Omega_A(W)\) physically
   cross-quartet depth-\(q\) occurrences and weighted average
   \(\Omega_A(r/q)\) crossing axes under the isometric packet model.

### Open

1. A disjoint scheduling of cross-quartet trades over changing matchings
   of the quartet index set.
2. Closure of the packet class while accumulating many crossing axes.
3. The quantitative build-up and direction-word dispersion required by
   (5.3) at every protected Gaussian depth.
4. Negative target covariance after those profile moves.
5. The hierarchical descent/circulation assertion `HCRT` itself.

Accordingly, the source gives a valid and useful local trade atlas, but
does not yet reduce the global difficulty to a routine bounded-trade
matching theorem.  Its remaining gate still contains the Gaussian Hall
capacity problem in occurrence-scale form.
