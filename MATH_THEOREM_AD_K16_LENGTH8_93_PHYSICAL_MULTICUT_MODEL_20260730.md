# The `K=16` length-eight source: exact 93-row physical multi-cut model

Date: 2026-07-30  
Lane: AD  
Status: an exact source-relative `WIDTH45` cut/seam model, a stronger physical
set-cover lower bound, an H100-capped CP-SAT build, and a complete full-edge
fallback are proved.  The model was built and audited but not solved.  The
frozen driver is exact for model construction; Section 7 records the
additional fail-closed replay requirements before a future solve may be
reported as a certificate.  No repaired carrier or length-`12873` word is
claimed.

**Implementation-scope correction (2026-07-30).**  The current live driver
named in this note has since been narrowed to the four-separated additive
`q<=3`/upper-width-four catalogue; width-five occurrences are now checked
only by literal CEGAR.  In that narrowed catalogue the independently replayed
scale-140 target/potential theorem gives `c>=101`.  The `WIDTH45` dimensions
and floor statements below document the earlier frozen build and must not be
used to describe the current driver.  The current theorem is
`MATH_THEOREM_K16_RATIONAL_TARGET_POTENTIAL_FLOOR101_20260730.md`; the direct
AD audit is `MATH_AUDIT_AD_K16_SECOND_STAGE_PORT_DUAL_FLOOR101_20260730.md`.

## 0. Verdict

The authoritative source is now

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
SHA-256 3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87
```

Its canonical deficit is seven physical phase-vector blocks:

\[
\begin{aligned}
\mathcal H^-&=\mathcal O(33337)\sqcup\mathcal O(33609)
                    \sqcup\mathcal O(34069),&|\mathcal H^-|&=45,\\
\mathcal H^+&=\mathcal O(36343)\sqcup\mathcal O(36599)
                    \sqcup\mathcal O(39791)\sqcup\mathcal O(46811),
                    &|\mathcal H^+|&=48.
\end{aligned}                                                   \tag{0.1}
\]

The first six orbits have size 15 and `O(46811)` has size three.  Thus

\[
                            6\cdot15+3=93                         \tag{0.2}
\]

literal target rows are required.  No scalar orbit row and no coefficient
five is used for a noninvariant seam.

The smallest executable exact model constructed here keeps the displayed
source directions and requires four-vertex retained packets.  It has

```text
12,870 cut bits
211,604 physical directed seam bits
1 cut-count integer
224,475 variables total
86,251 constraints
```

and enforces:

* exact endpoint permutation and cut separation;
* exact local positive residence;
* all 22,880 signed literal q1 inequalities;
* all fixed lower-q2 and upper-q2 rows;
* all fixed lower-q3 rows;
* all rank-eleven union rows using widths four and five; and
* seven exact provider/component strengthening rows; and
* literal physical replay of every remaining lower and arbitrary-upper gate
  through exact CEGAR no-goods.

The source-specific catalogue has the exact defect-hit histogram

\[
\begin{array}{c|rrr}
\text{distinct members of }\mathcal H^-\cup\mathcal H^+
   \text{ hit by one seam}&0&1&2\\ \hline
\text{seams}&206029&5382&193.
\end{array}                                                     \tag{0.3}
\]

Every physical phase has a provider.  Across the 45 lower phases the
provider counts range from 17 to 64 and sum to 2,127; across the 48 upper
phases they range from 65 to 94 and sum to 3,641.

The elementary column-capacity bound is only

\[
                         c\ge\left\lceil{93\over2}\right\rceil=47. \tag{0.4}
\]

It is not sharp.  The exact double-provider graph has 119 distinct edges,
193 physical double columns, 18 isolated defects, and matching number 37.
Consequently the exact provider-only floor, and hence the physical-master
floor, is

\[
                              c\ge93-37=56.                    \tag{0.5}
\]

All radius-47 pattern conclusions in the first build are superseded.  The
old model's feasible set remains sound because its 93 literal rows already
imply (0.5), but the strengthened build exposes the floor and its component
cuts explicitly.  A physically `C_15`-invariant rethread satisfying this
catalogue has the stronger componentwise floor `c>=75` (Corollary 5.3).

A later, separately scoped endpoint-path audit strengthens the fixed
q<=3/upper-width-four catalogue to

\[
                              c\ge73.                           \tag{0.6}
\]

It uses a 33-target, capacity-two provider-path cut and is proved in
`MATH_AUDIT_AD_K16_Q3_PROVIDER_PATH_FLOOR73_20260730.md`.  It does not
automatically transfer to this report's combined `WIDTH45` catalogue, whose
150 additional width-five-only singleton providers change the provider
digraph.  Thus (0.5) remains the proved unconditional floor for the frozen
combined-width model described here.

## 1. Frozen source and the meaning of 93

The source has 12,870 distinct rank-eight owners and 29 cyclic components,
of lengths

```text
6540,2070,1245,390,390,390,345,330,255,255,255,75,45,45,16x15.
```

It has no bad Johnson edge, minimum positive run four, and complete lower
and upper q1 palettes.  Its edge-type census is

\[
                |E_{AA}|=6420,\qquad |E_{AB}|=30,
                \qquad |E_{BB}|=6420.                            \tag{1.1}
\]

Here `B` denotes a middle owner containing the fixed coordinate 15 and `A`
one omitting it.

The fixed lower-q2 holes are the 45 masks in `H^-`.  The fixed upper-q3
holes and the arbitrary-width rank-eleven holes are the same 48 masks in
`H^+`.  A size-15 fixed upper-q4 orbit represented by `40443` is also absent,
but each of its masks retains a width-six union witness.  It is therefore not
part of the canonical arbitrary-upper deficit.  Fixed-window hole mass is
108; objective mass is 93.

The exact q1 load histogram on each shore is

\[
                         1^{10110}2^{1230}3^{100}.                \tag{1.2}
\]

For a source edge, the pair of its lower and upper source loads has histogram

\[
(1,1)^{7365}(1,2)^{2445}(1,3)^{300}
(2,1)^{2445}(2,2)^{15}(3,1)^{300}.                              \tag{1.3}
\]

Thus the old statement that every source edge is unique on at least one q1
shore no longer holds: precisely 15 source edges have slack on both shores.
The correct model must use the signed literal ledger.

## 2. New endpoint-minimal replay

The old endpoint-minimal audit was hash-pinned to an earlier carrier and
could not be imported.  The same independent enumeration was therefore
rerun against the source in Section 1 on one representative of every
residual upper orbit, through the unconditional width range `4,...,11`.

### Proposition 2.1 (frozen cross-component endpoint support)

On the independently oriented cross-component one-seam arms of this source,
raw rank-eleven target occurrences have widths four through seven, while the
endpoint-minimal and positive-safe endpoint-minimal supports are both

\[
                              \{4,5\}.                            \tag{2.1}
\]

The exact counts on orbit representatives are

\[
\begin{array}{c|rr|rr}
T&\text{minimal }w=4&\text{minimal }w=5
 &\text{safe minimal }w=4&\text{safe minimal }w=5\\ \hline
36343&950&56&164&8\\
36599&802&40&172&8\\
39791&1202&90&264&20\\
46811&1230&100&300&30.
\end{array}                                                     \tag{2.2}
\]

#### Proof/certificate

The replay tests every cross-component seam, both independent source
orientations, every split, and every width four through eleven.  A raw
occurrence is retained as endpoint-minimal only when deleting either endpoint
changes its union.  The output support and counts are (2.1)--(2.2).  Rotation
transports the statement to every literal member of each target orbit.  The
hash-pinned replay is listed in Section 9.  QED.

This proposition is not a WLOG theorem for arbitrary same-source or
multi-seam rethreads.  It justifies the concrete short catalogue; an UNSAT
result from that catalogue would remain `WIDTH45`-scoped.

## 3. Direction-coherent multi-cut decoder

Orient the 29 source cycles as displayed.  Index their 12,870 directed
transitions by `i`.  Write

\[
                       t_i\longrightarrow h_i                 \tag{3.1}
\]

for the old tail and head.  Let `c_i` be the bit which cuts transition `i`.

A directed seam record `a=(i,j)` replaces the old outgoing transition at
`t_i` by

\[
                         t_i\longrightarrow h_j.               \tag{3.2}
\]

It is retained in the catalogue exactly when (3.2) is a nontrivial Johnson
edge, the two source collars pass the exact positive-run test, and, if the
two cuts lie on one source cycle, their cyclic transition distance is at
least four.  There are exactly 211,604 such records.  Let `y_ij` select one.

Impose

\[
 \sum_jy_{ij}=c_i,
 \qquad
 \sum_i y_{ij}=c_j                                      \tag{3.3}
\]

for every transition, and for every cyclic block of four consecutive source
transitions impose

\[
                    c_i+c_{i+1}+c_{i+2}+c_{i+3}\le1.           \tag{3.4}
\]

### Theorem 3.1 (exact decoder)

The binary solutions of (3.3)--(3.4) are in bijection with the
direction-coherent source rethreads whose retained packets have at least four
vertices and whose seams belong to the positive-compatible catalogue.
Every decoded object is a literal spanning two-factor of `J(16,8)`.

#### Proof

The first equation in (3.3) gives every cut tail exactly one new successor;
an uncut tail retains its old successor.  The second gives every cut head
exactly one new predecessor, while an uncut head retains its old predecessor.
Thus the decoded successor is a permutation of all 12,870 owners.  Every arc
is a Johnson arc by construction.  A directed two-cycle would require either
two consecutive exposed source ports or two new seams whose exposed head and
tail ports are consecutive; both contradict (3.4).  Hence the underlying
edges form a simple literal spanning two-factor.  Conversely a
direction-coherent rethread has exactly one outgoing
seam at every cut tail and one incoming seam at every cut head and therefore
defines a unique binary solution.  Equation (3.4) is equivalent to four
retained vertices between consecutive cuts.  QED.

This formulation has one tail/head orientation per displayed source cycle.
An undirected socket model would allow each packet to reverse independently
but has up to 1,647,360 socket-mode seam variables.  The complete arbitrary
factor alternative in Section 8 uses 411,840 physical edge variables.

## 4. Exact literal loss/gain ledgers

A width-three window uses two transitions, a width-four window three, and a
width-five window four.  By (3.4), each such old window contains at most one
cut and each corresponding new window crosses at most one seam.  Danger from
double cuts begins at width six, not width five.

For a target `T`, let `m_T^0` be its source multiplicity in the row under
consideration.  Let `d_T(i)` be the number of its width-specific old
occurrences destroyed by cut `i`, and let `g_T(a)` be the multiplicity among
the crossing windows created by seam `a`.

### Theorem 4.1 (additive width-3/4/5 identity)

For every q1 target, every natural width-three q2 target, every natural
width-four q3 target, and every rank-eleven target counted over widths four
and five, the final multiplicity is exactly

\[
              m_T=m_T^0-\sum_i d_T(i)c_i+\sum_a g_T(a)y_a.      \tag{4.1}
\]

#### Proof

An old occurrence survives exactly when none of its transitions is selected;
(3.4) guarantees that at most one can be selected.  Every occurrence not
wholly inside a retained packet
crosses exactly one selected seam and is one of that seam's enumerated split
windows.  The two classes are disjoint and exhaustive.  Multiplicity is kept
when two splits give the same target.  QED.

The model installs (4.1) with right-hand side at least one for:

\[
\begin{array}{c|r}
\text{family}&\text{literal rows}\\ \hline
\text{lower q1}&11440\\
\text{upper q1}&11440\\
\text{lower q2}&8008\\
\text{upper q2 preservation}&8008\\
\text{lower q3 preservation}&4368\\
\text{rank-eleven union, widths 4 or 5}&4368.
\end{array}                                                     \tag{4.2}
\]

The 45 lower and 48 upper zero-baseline rows in (0.1) occur inside the
corresponding complete physical families in (4.2).  They are not replaced by
seven quotient totals.

### Corollary 4.2 (signed q1 rows)

For every literal lower rank-seven or upper rank-nine colour `C`, the exact
condition is

\[
 m_C^0-\sum_{i:\,c(i)=C}c_i+\sum_{a:\,c(a)=C}y_a\ge1.         \tag{4.3}
\]

In particular, a source load two or three permits negative change one or two;
equality in every row is an overconstraint.  Sector totals cannot replace
(4.3).

## 5. Exact lower bounds

### Theorem 5.1 (exact provider-edge-cover floor)

For a seam `a`, let

\[
 H(a)=\{T\in\mathcal H^-\sqcup\mathcal H^+:a\text{ creates }T\}, \tag{5.1}
\]

with repeated occurrences of one target counted once.  Form the simple graph
`G` on the 93 defects by placing an edge `ST` whenever some seam has
`H(a)={S,T}`.  Then:

* `|H(a)|<=2` for every seam;
* 193 physical seams give 119 distinct edges: 90 physical/75 distinct `LU`,
  103 physical/44 distinct `UU`, and no `LL` edge;
* `G` has one 75-vertex component and 18 isolated vertices; and
* `nu(G)=37`.

The provider-only minimum is exactly 56.  Therefore every solution of the
physical master has at least 56 cuts and seams.

#### Proof

The 18 isolates leave only 75 vertices eligible for an ordinary matching, so
`nu(G)<=floor(75/2)=37`.  The pinned certificate contains 37 pairwise
vertex-disjoint double-provider seams, proving equality.  Every isolated
vertex has a singleton provider, and completing that matching with 19
verified singleton columns covers all 93 vertices with 56 seams.  Conversely,
from any provider cover choose its double columns as graph edges and its
single columns as loops.  Replacing a cover by the standard matching-plus-one
edge/loop construction gives the edge-cover bound

\[
                       |S|\ge |V(G)|-\nu(G)=93-37=56.          \tag{5.2}
\]

Endpoint permutation, q1, collateral shadows, and residence only remove
provider covers, so they cannot lower (5.2).  QED.

The combined-width `WIDTH45` graph is exactly the fixed-width-four graph:
both contain the same 193 directed double columns and the same hit sets.
Width five adds 150 singleton-only columns.  Thus (5.2), not merely its
numerical value, transfers to the frozen master.

### Proposition 5.2 (zero-variable master strengthening)

Let `h` count selected hitful seams, `d` selected double-provider seams,
`L` lower incidences, `U` upper incidences (so a `UU` column has weight two),
`X` selected `LU` columns, and `h_G` selected providers in the 75-vertex
component.  The strengthened build installs the seven valid rows

\[
\begin{gathered}
h\ge56,\qquad h_G\ge38,\qquad L\ge45,\qquad U\ge48,\\
h+d\ge93,\qquad 2h+X\ge138,\qquad 2h_G+X\ge105.               \tag{5.3}
\end{gathered}
\]

The first two are the global and giant-component edge-cover floors.  The next
two sum the literal lower and upper rows.  A singleton has one service slot
and a double has two, giving `h+d>=93`.  Weighting lower targets twice and
upper targets once gives `2h+X>=2*45+48`; restricting the same argument to
the giant component gives `2h_G+X>=2*30+45`.  Hence every row in (5.3) is
implied by the 93 integral literal rows and changes no feasible solution.

At radius 56 every selected seam is hitful, the 18 isolates consume 18
single services, and the giant component uses 38 seams.  Writing its type
counts as `(d,X,s_L,s_U,u)` for doubles, `LU`, lower singletons, upper
singletons, and `UU`, the only capacity patterns are

\[
(37,29,1,0,8),\ (37,30,0,1,7),\
(38,30,0,0,8),\ (38,31,0,0,7).                                \tag{5.4}
\]

In the last two cases the 76 service slots duplicate exactly one upper or
lower target respectively.  This is a provider-capacity classification only;
none of the four patterns is asserted endpoint-, q1-, or residence-feasible.

### Corollary 5.3 (invariant and connected bounds)

Every physical middle edge has a free `C_15` orbit.  Indeed, if a nonidentity
rotation fixed an unordered edge, its odd order would prevent it from
swapping the two endpoints, so it would fix each rank-eight endpoint.  Its
cycles on the first 15 coordinates have length 3, 5, or 15.  An invariant
endpoint would therefore contain a multiple of that length among those
coordinates, whereas a rank-eight endpoint contains either seven or eight
of them according as coordinate 15 is present or absent.  This is impossible.
The component structure sharpens the symmetry consequence.  Let `I_-` be the
15 isolated lower targets, `I_+` the three isolated upper targets, and `G`
the remaining 75 targets.  These are three rotation-invariant service blocks,
and no provider serves two blocks.  For a physically `C_15`-invariant
rethread/factor, the added-edge operations are free 15-orbits and their
service blocks rotate equivariantly.  Therefore the selected hitful counts in
the three blocks are separately multiples of 15.  Rounding their respective
floors `15,3,38` gives `15,15,45`, hence

\[
                              c\ge75.                           \tag{5.5}
\]

This is a physical-invariance theorem, not a symmetry reduction of the raw
directed-column model.  The frozen displayed chronology is not itself
`C_15`-equivariant, so one must not assume its 211,604 directed columns form
rotation orbits.

If the final factor is required to be one cycle, every one of the 29 source
components must be cut, giving the independent but weaker bound `c>=29`.
In particular, cutting every source component only once cannot cover the 93
literal targets in this catalogue.

### Proposition 5.4 (architecture-free lower and q1 debt)

Every residual lower target contains coordinate 15, so every new width-three
provider is a `BBB` path.  A new `BB` edge lies in at most two such windows.
Therefore every physical repair, without the directed-catalogue restriction,
satisfies

\[
                              Y_{BB}\ge23.                      \tag{5.6}
\]

Only 15 source edges have q1 load pair `(2,2)`.  Hence a catalogue solution
at the radius floor 56 cuts at least 41 edges which are the unique source
provider of some literal q1 colour.  Those colour debts must be restored by
the positive terms in (4.3).

The upper bank alone gives only `ceil(48/7)=7`, since one seam belongs to
three width-four and four width-five crossing slots.  The source-specific
two-hit theorem is much stronger because most slots do not land in the 93
target bank.

### Theorem 5.5 (separately scoped q<=3 endpoint-path floor)

In the authenticated 211,604-seam q<=3/upper-width-four ledger, let `p` count
selected seams supplying at least one of the 93 original defects and let `z`
count the remaining selected seams.  Then

\[
                     p\ge56,\qquad z\ge17,
                     \qquad c=p+z\ge73.                       \tag{5.7}
\]

Indeed, the 33-target bank

\[
T=\mathcal O_{15}(33609)\sqcup\mathcal O_{15}(34069)
  \sqcup\mathcal O_3(46811)
\]

is missed by every provider-only cycle, and an exact SCC-condensation
union-mask audit proves that one provider path hits at most two distinct
members of `T`.  Deleting `z` zero-hit seams from the endpoint-balanced
selected cycles leaves at most `z` provider paths, so `33<=2z`.  Combining
`z>=17` with Theorem 5.1 gives (5.7).

This proof uses only endpoint balance and the 93 service rows.  It does not
use four-separation, reverse-edge, q1, nondefect survivor, residence, or CEGAR
rows.  The exact proof, equality-at-73 ledger, audit corrections, and hashes
are in `MATH_AUDIT_AD_K16_Q3_PROVIDER_PATH_FLOOR73_20260730.md`.  Because the
combined `WIDTH45` graph contains 150 extra provider arcs, (5.7) must not be
quoted for that older graph without a separate replay.

## 6. Why matching alone is insufficient

The defect-graph matching in Theorem 5.1 is exact only for provider
cardinality.  It does not solve the independent endpoint-assignment problem.
With a fixed cut set and without coloured quotas, (3.3) is an ordinary
bipartite perfect matching.  The signed q1 and deep rows destroy total
unimodularity.  For example, let terminals be `a,b`, initials `x,y`, and let

```text
ax, by have red service;
ay, bx have blue service.
```

The two integral perfect matchings use two red or two blue edges, while
assigning one half to all four edges satisfies endpoint balance and the
fractional equations “one red, one blue.”  Thus an ordinary flow relaxation
is not exact.

The present formulation is a binary CP-SAT/ILP.  A Benders decomposition may
choose cuts, literal service columns, and colour assignments in the master;
after those choices, the remaining uncoloured endpoint completion is a Hall
flow.  Without the assignments, the joint problem is a quota-constrained
matching problem.

## 7. All-depth CEGAR and exact status meanings

Rows (4.2) include the opposite q2/q3 preservation gates which reject the
known length-nine false descents.  They do not directly encode fixed lower
depths four through seven or arbitrary upper ranks twelve through sixteen.
Every incumbent is therefore materialized as a literal successor factor and
audited for:

1. positive residence four;
2. every fixed lower rank; and
3. every arbitrary upper interval rank.

If an incumbent fails, the implementation adds the exact full seam-assignment
no-good

\[
 \sum_{a\in Y}(1-y_a)+\sum_{a\notin Y}y_a\ge1,                 \tag{7.1}
\]

which excludes that factor and no strict subset, superset, or compensating
packet.  The finite loop is therefore exact, although (7.1) can be weak.

The objective variable is bounded by

\[
                         56\le c\le R,                         \tag{7.2}
\]

where `R=--radius-max` (default `256`).  Consequently, status scopes must be:

* `PASS_MINIMUM_WIDTH45_CARRIER`: a physically replayed carrier and a proved
  minimum inside this source-relative class (an optimum below `R` is globally
  minimum in the class because every smaller cardinality lies in the model);
* `PASS_WIDTH45_CARRIER_MINIMUM_UNKNOWN`: a physically replayed carrier, but
  no minimum proof;
* `WIDTH45_INFEASIBLE_ON_[56,R]_TRUSTED_CP`: trusted CP-SAT infeasibility only
  through radius `R` in this direction-coherent width-4/5 class; this becomes
  full separated-class infeasibility only when `R=12870`; and
* `UNKNOWN`/time or round limit: no mathematical conclusion.

No solve was launched in this work, so the frozen status is only
`MODEL_BUILT`.

For the later q<=3/upper-width-four live master, Theorem 5.5 replaces the
lower endpoint 56 by 73.  Persisted exact-count-70 infeasibility is therefore
subsumed by a solver-free endpoint-service theorem and supplies no additional
q1 obstruction.

The frozen `d8b5...` driver constructs the audited master exactly, but its
future-solve certificate path still requires the following fail-closed
hardening.  These items do not alter the built model:

1. rename and record infeasibility with the interval in (7.2);
2. require the already computed fixed upper-q1 and upper-q2 hole rows to be
   empty in final replay;
3. persist the selected cut and seam identifiers, assert that their left and
   right port sets are both exactly the cut set, and independently replay
   indegrees, Johnson adjacency, distinct rank-eight owners, and the component
   partition;
4. preserve separate pre-CEGAR and post-CEGAR model artifacts, so learned
   assignment no-goods are reproducible; and
5. gate objective fields on a feasible solver status and record the OR-Tools
   version, hostname, response statistics, and artifact hashes.

Thus the present executable package is a fail-closed **build certificate**.
No future SAT or UNSAT output from the frozen solve loop should be promoted
without the preceding replay layer.

## 8. Complete arbitrary-factor fallback

The direction-coherent model is a sufficient source-relative class, not WLOG
for all physical repairs.  A complete topology model uses one final-edge bit
for every edge of `J(16,8)`:

\[
                    |E(J(16,8))|={12870\cdot64\over2}=411840.  \tag{8.1}
\]

Equivalently, use 12,870 cut bits on source edges and 398,970 addition bits
on non-source edges.  At every owner `v`, impose

\[
 \sum_{e\in E_0:e\ni v}h_e
   =\sum_{f\notin E_0:f\ni v}a_f.                              \tag{8.2}
\]

### Theorem 8.1 (full physical edit decoder)

The binary solutions of (8.2) are exactly the spanning simple two-factors of
`J(16,8)`, written as symmetric-difference edits of the source.  Their edit
edges decompose into alternating old/new circuits.

#### Proof

After cancelling common edges, (8.2) says that the old and new degrees agree
at every owner.  Pair old and new incidences locally and trace alternating
circuits.  Conversely every new two-factor has degree two at each owner, so
its deleted and added degrees relative to the source agree.  QED.

Literal width-three and width-four/five witness flows can be attached to
(8.2), and the same signed q1 rows apply.  This model admits packet reversal,
close cuts, and multi-seam witnesses.  For an unrestricted rank-eleven UNSAT
claim one must enlarge the upper automaton to the theorem-complete width
range `4,...,11`; width `4,5` is a sound but potentially incomplete
restriction outside the audited short-arm class.

Thus “smallest” here means the smallest executable exact source-relative
model we constructed, not an information-theoretic lower bound on all SAT
encodings.

## 9. Frozen executable package

### Endpoint-minimal replay

```text
scratch/run_ad_k16_len8_endpoint_minimal_20260730.py
SHA-256 75d6f449fd87d1442c345af202c377fc64e3e31fcabb1137947956f1b88e5fd9

scratch/ad_k16_len8_endpoint_minimal_20260730.audit.json
SHA-256 6be2bbbf3f8c6532c34a0aaef7188c22d1d8e364b368e5fa1cd1f14c4e494959

scratch/ad_k16_len8_endpoint_minimal_20260730.resource.txt
SHA-256 e4b0fe9642585545f9def6847eff36700d6253398e67baa48f15eb29c7bcbecd
```

The frozen resource transcript records 3.83 wall seconds and 20,992 KiB
maximum RSS.  It does not itself certify the hostname or an address-space
cap, so neither is asserted for this replay.

### Exact model driver and catalogue audit

The live development filename was concurrently edited after the build.  In
particular, that edit replaced the combined width-4/5 bank by width four
alone and is not the model proved here.  The byte-exact source used for the
frozen artifacts is therefore preserved under a new immutable name:

```text
scratch/solve_k16_len8_physical_93_multicut_cegar_frozen_20260730.py
SHA-256 d8b5e39042234a8c7246139942e35891ae4db489a65bd3e26280c32615025dc0

scratch/k16_len8_physical_93_multicut_catalogue_v3_20260730.audit.json
SHA-256 b0800c94dd6d6f9418532501d84fa5c6ca8d5745a0481db22edaaf37f483144b

scratch/k16_len8_physical_93_multicut_catalogue_v3_20260730.resource.txt
SHA-256 2f1d05b05ade5c80a2e400b51f11ed552173eafea24c3e1ed2a3700567fbfa8f
```

The catalogue replay used one H100 CPU, a 1 GiB cap, 6.18 wall seconds, and
206,296 KiB maximum RSS.

### Built CP-SAT model

```text
scratch/k16_len8_physical_93_multicut_build_20260730.result.json
SHA-256 41916aceaad4649bbe272fd088f62e47e4ff5eae37af15f7ed1a9bfb98bd37d0

scratch/k16_len8_physical_93_multicut_build_20260730.checkpoint.json
SHA-256 1057ed9cbaebb8a1dc145099ed1c4ee60b1faa0b1a5d71a3c9e2b0a6571c42b8

scratch/k16_len8_physical_93_multicut_build_20260730.pbtxt.gz
SHA-256 7adbe17379f259863dc3b7b62dd766150c1b93ff78f1b1ae6ffd4f491b8278c4
uncompressed model SHA-256
ce45fe3bf01627d155f6a3ba6ebcdc6037e85e5d701c35abe8db909a22a06b9f

scratch/k16_len8_physical_93_multicut_build_20260730.resource.txt
SHA-256 6537257f95b7d11a3a990c458f6c9899161653eed9f83ad80d80187c76e09956
```

The build ran on the host enforced by the driver with a 4 GiB address-space
cap and `--workers 1` configured, but build-only mode never invokes CP-SAT and
therefore does not consume that worker setting.  The frozen transcript records
14.96 wall seconds and 587,908 KiB maximum RSS.  It performed no solve.

### Independent package audit

```text
scratch/audit_ad_k16_len8_physical_93_multicut_package_20260730.py
SHA-256 d271613325b5a4d003d201f35187875df34662b2d8eac7d8510702d202e04055

scratch/ad_k16_len8_physical_93_multicut_package_20260730.audit.json
SHA-256 5be169b44691370bad9d2033ab609770fa83564cbe44aa4d5cd0ef802fa12a8d
```

The package audit checks the pinned input hashes; the catalogue, result, and
checkpoint self-hashes; the endpoint-minimal counts; the seam/hit/row/model
censuses; and the compressed and uncompressed model digests.  The phase-block
sizes in its output are a reported constant rather than an independently
derived check, and the auditor cannot authenticate its own displayed
script/output hashes.  Subject to that explicit scope, it returns `PASS`.

### Later q<=3 provider-path certificate

```text
MATH_AUDIT_AD_K16_Q3_PROVIDER_PATH_FLOOR73_20260730.md

scratch/audit_ad_k16_provider_path_subset_floor73_20260730.py
SHA-256 fc7413559ee1de8653eccb49c86a2f41b7e3fb5f39d077d1cd7fa451221b13e5

scratch/ad_k16_provider_path_subset_floor73_v3_20260730.audit.json
SHA-256 00404a022a84cefc4249930726775ccb57a57cc75a2be0098a4499dca2fe24fd
```

This later certificate is authoritative only for the fixed q<=3 /
upper-width-four ledger, as stated in Theorem 5.5.

## 10. Proved/conditional boundary

Proved:

* the new source has seven phase blocks and 93 literal obligations;
* its cross-component endpoint-minimal upper support is exactly `4,5`;
* the 211,604-column direction-coherent catalogue and exact decoder;
* the signed q1 and width-3/4/5 loss/gain identities;
* the weak column bound `c>=47`, the exact provider floor `c>=56`, and the
  four exact provider-capacity patterns at radius 56;
* the separately scoped q<=3 endpoint-service floor `c>=73`;
* the conditional physical-`C_15` invariant floor `c>=75`;
* the exact CP-SAT model size and H100-capped build; and
* the complete 411,840-edge arbitrary-factor fallback theorem.

Not proved:

* feasibility of the 224,475-variable model;
* infeasibility of any width range;
* existence of a globally all-depth repaired carrier;
* connectivity of a model solution (arbitrary final components are allowed);
* compiler Hall after carrier repair; or
* `nu(16)=12873`.
