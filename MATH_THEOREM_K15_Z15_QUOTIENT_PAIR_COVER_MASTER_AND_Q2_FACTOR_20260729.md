# The exact `Z_15` quotient pair-cover master and a complete-`q2` rainbow factor

Date: 2026-07-29

Status: exact reduction, independently cross-audited catalogue and pair maps,
and two independently replayed positive factor certificates.  The stronger
certificate has perfect middle and lower-`q1` palettes and complete lower
`q2` and upper `q1` simultaneously.  It is not resident, not connected,
not collision-floor optimal, and not deeper-shadow complete.  This note does
not claim a `k=15` word.

## 1. Quotient incidence data

Let `rho` be coordinate rotation on `Z_15`, and let `B` be the bipartite
inclusion graph between rank-seven sets and rank-eight sets.  The action of
`<rho>` is free on both central ranks.  Indeed, if `rho^t`, with
`t!=0 mod 15`, fixes a set, then its coordinate cycles all have length

\[
 d={15\over\gcd(15,t)}\in\{3,5,15\}.
\]

The fixed set is a union of these cycles, so its rank is divisible by `d`,
whereas

\[
 \gcd(15,7)=\gcd(15,8)=1.
\]

Consequently the quotient multigraph

\[
 Q=B/\langle\rho\rangle
\]

has exactly

\[
 |L(Q)|=|U(Q)|={1\over15}{15\choose7}=429
\]

vertices on each shore.  Every quotient vertex has degree eight, counting
voltage-labelled parallel edges, so

\[
 |E(Q)|=429\cdot8=3432.                         \tag{1.1}
\]

Choose canonical representatives.  Write an edge orbit as

\[
 e=(L_e,a_e,U_e,\lambda_e),
 \qquad L_e\cup\{a_e\}=\rho^{\lambda_e}U_e.     \tag{1.2}
\]

Thus, at sheet `s`, the lift of `e` joins

\[
 \rho^sL_e\quad\hbox{to}\quad\rho^{s+\lambda_e}U_e. \tag{1.3}
\]

### Theorem 1.1 (complete quotient catalogue)

The `k=15` quotient has 3,418 unordered endpoint pairs.  Of these, 3,404
support one edge orbit and exactly 14 support two voltage-distinct parallel
edge orbits.  No endpoint pair has larger multiplicity.

There are no bipartite loops, because the shores have different ranks.
Nevertheless, the pair of parallel edges at a rank-seven quotient vertex
projects to a Johnson quotient loop on rank eight.  There are exactly 14 such
rank-seven pair choices.  Dually, there are 14 parallel pair choices at the
rank-eight shore.

#### Audit

Three independently written catalogues agree edge-for-edge on the four
stored fields

\[
 (L_e,a_e,U_e,\lambda_e)
\]

for all 3,432 edge IDs; the normalized lower endpoint
`rho^(-lambda_e)L_e` is then derived identically in all three implementations.
The stable four-field edge-table SHA-256 is

```text
8b3d5054edd286c03092089c9e3e198b5f482f1d70d5539746c7ed608197899d
```

The old `graded_quotient_pipeline.py` Johnson choice table has only 11,998
choices, namely

\[
 11998=429{8\choose2}-14.
\]

It deliberately omits the 14 projected loops and therefore is not a complete
edge/pair catalogue for the present bipartite master.

## 2. Exact pair linearization

For every edge orbit `e`, introduce `x_e in {0,1}`.  For every quotient
vertex `v` and unordered pair

\[
 p\in {\delta(v)\choose2},
\]

introduce `y_(v,p) in {0,1}`.  Since every vertex has eight incident edge
IDs, there are exactly

\[
 2\cdot429{8\choose2}=24024                    \tag{2.1}
\]

pair variables, 12,012 on each shore.  Impose

\[
 \sum_{p\in{\delta(v)\choose2}}y_{v,p}=1
 \qquad(v\in V(Q)),                              \tag{2.2}
\]

and, for every incidence `e in delta(v)`,

\[
 x_e=\sum_{\substack{p\in{\delta(v)\choose2}\\e\in p}}y_{v,p}. \tag{2.3}
\]

### Theorem 2.1 (necessary and sufficient factor equations)

The binary solutions of (2.2)--(2.3) are in bijection with the
`rho`-invariant spanning physical `2`-factors of `B`.

For every solution:

1. exactly 858 quotient edge orbits are selected;
2. every physical rank-eight state has degree two;
3. every physical rank-seven state has degree two;
4. the projected rank-eight Johnson factor contains every middle owner once;
5. its rank-seven edge-intersection palette contains every rank-seven colour
   once.

Thus middle ownership and lower `q1` are squarefree by construction, even if
the selected factor is disconnected.

#### Proof

At a fixed vertex `v`, (2.2) chooses one pair of distinct incident edge IDs.
Equation (2.3) says that `x` is exactly the incidence vector of this pair.
The equation at the other endpoint of every edge forces the two local pair
systems to select the same global edge set.  Hence every quotient vertex has
degree two.  Lifting equivariantly gives degree two at every physical vertex.

Conversely, a rotation-invariant spanning physical `2`-factor descends to a
degree-two quotient factor with voltage-labelled parallel edges retained.
Its two selected incident edges give the unique pair variable equal to one at
each quotient vertex, and (2.2)--(2.3) follow.  The middle and lower-`q1`
claims follow because every rank-eight and rank-seven physical vertex occurs
exactly once in the bipartite factor.  \(\square\)

The `x` variables may be eliminated: for each quotient edge, equate the sum
of lower-shore pair variables containing it with the corresponding
upper-shore sum.  This gives exactly the same binary feasible set with only
the 24,024 pair variables.

## 3. The two local shadow maps

For an edge incident with a canonical upper vertex `U`, put

\[
 L_e^U=\rho^{-\lambda_e}L_e\subset U.            \tag{3.1}
\]

For an upper-shore pair `p={e,f}` define

\[
 \kappa_-(U,p)
 =\operatorname{can}(L_e^U\cap L_f^U)
 \in {[15]\choose6}/\langle\rho\rangle.          \tag{3.2}
\]

For a lower representative `L`, its two incident upper neighbours in the
`L` frame are `L union {a_e}` and `L union {a_f}`.  Define

\[
 \kappa_+(L,p)
 =\operatorname{can}(L\cup\{a_e,a_f\})
 \in {[15]\choose9}/\langle\rho\rangle.          \tag{3.3}
\]

### Theorem 3.1 (pair colours are the exact shadows)

In the projected rank-eight factor, `kappa_-` is exactly the lower-`q2`
triple-intersection colour at the middle state `U`, while `kappa_+` is
exactly the upper-`q1` union colour on the Johnson edge represented by `L`.

Consequently complete lower `q2` and upper `q1` are respectively equivalent
to the ordinary covering rows

\[
 \sum_{\kappa_-(U,p)=C}y_{U,p}\ge1
 \quad\hbox{for every rank-six orbit }C,          \tag{3.4}
\]

\[
 \sum_{\kappa_+(L,p)=D}y_{L,p}\ge1
 \quad\hbox{for every rank-nine orbit }D.         \tag{3.5}
\]

No fixed chronological suffix automaton is needed for these two gates.

#### Proof

Let the two rank-seven neighbours of a physical middle state `T_i` be

\[
 X_{i-1}=T_{i-1}\cap T_i,
 \qquad X_i=T_i\cap T_{i+1}.
\]

Then

\[
 T_{i-1}\cap T_i\cap T_{i+1}=X_{i-1}\cap X_i,
\]

which is (3.2) after putting both incidences in the same upper frame.  At a
rank-seven state `X_i`, its two upper neighbours are `T_i,T_(i+1)`, and

\[
 T_i\cup T_{i+1}=X_i\cup\{a_e,a_f\},
\]

which is (3.3).  Rotation-equivariance shows that one representative witness
covers the whole physical target orbit.  \(\square\)

There are 335 target orbits on each side.  Exactly 333 have orbit size 15 and
each has 36 candidate pair variables.  Two on each side have orbit size five
and each has 12 candidate pairs.  The short representatives are

```text
rank 6: 3171, 5285
rank 9: 7399, 11627.
```

Orbit coverage remains exact at composite `15`.  Soft physical-hole and
physical-collision objectives must, however, use the actual orbit size.  An
unweighted quotient load is not a literal physical multiplicity on a short
orbit.

### Theorem 3.2 (complement-symmetric submaster)

Complement swaps the two shores of `B`.  On voltage-labelled quotient edges
it induces a fixed-point-free involution

\[
 e\longmapsto\bar e.                              \tag{3.6}
\]

The 3,432 edge orbits split into exactly 1,716 complement pairs.  It also
induces a bijection from lower-shore pairs to upper-shore pairs, with 12,012
pair-pairs, satisfying

\[
 \kappa_+(\bar U,\bar p)
 =\operatorname{can}([15]\setminus\kappa_-(U,p)). \tag{3.7}
\]

Therefore, in the restricted submaster

\[
 x_e=x_{\bar e}\qquad(e\in E(Q)),                 \tag{3.8}
\]

complete lower `q2` is equivalent to complete upper `q1`.  The same statement
holds for the load cap at two.

#### Proof

A physical incidence `L subset U` complements to `U^c subset L^c`, so
complement exchanges the shores and preserves incidence.  Applying it twice
returns the original voltage-labelled edge orbit.  Direct canonicalization
of all edge records gives no fixed orbit and 1,716 two-cycles.

At an upper turn, complement changes the intersection of its two lower
neighbours into the union of the two complementary upper neighbours.  This
is (3.7).  If (3.8) holds, the unique local pair chosen at a vertex is sent
to the unique chosen pair at the complementary vertex, so the two colour
load vectors are complementary copies.  Coverage and the cap at two are
therefore equivalent.  \(\square\)

This is a sufficient restricted model, not a without-loss-of-generality
reduction.  Averaging a factor with its complement gives a fractional or
four-regular object, not automatically a complement-invariant binary
`2`-factor.

## 4. Exact collision-zero refinement

For each rank-six target orbit `C`, let

\[
 n_C=\sum_{\kappa_-(U,p)=C}y_{U,p}.               \tag{4.1}
\]

There are 429 selected upper-shore pairs, so

\[
 \sum_C n_C=429.                                  \tag{4.2}
\]

On the factor face of Theorem 2.1 the middle collision contribution is zero
identically.  Define

\[
 P_\Psi=\sum_C{n_C\choose2},
 \qquad \Xi_Q=P_\Psi-94.                          \tag{4.3}
\]

### Theorem 4.1 (linear form of `Xi_Q=0`)

Under complete `q2` coverage (3.4),

\[
 \Xi_Q=0
 \quad\Longleftrightarrow\quad
 1\le n_C\le2\quad\hbox{for every }C.             \tag{4.4}
\]

In that case exactly 241 colours have load one and 94 have load two.

#### Proof

All 335 loads are positive and sum to 429.  Convexity of `binom(n,2)` gives
the unique minimum distribution `1^241 2^94`, with collision sum 94.  Any
load at least three can be reduced, and a load-one bin increased, lowering
the collision sum.  Conversely the cap `n_C<=2`, positivity, and (4.2) force
the displayed minimum distribution.  \(\square\)

Thus the exact quotient-normalized collision-zero target is linear: append

\[
 \sum_{\kappa_-(U,p)=C}y_{U,p}\le2               \tag{4.5}
\]

for all 335 rank-six orbits.  Mere `q2` OR coverage is weaker.  Literal
physical collision counts require the short-orbit weights and are reported
separately.

## 5. Components and voltage

Orient a quotient factor component `C`.  Add `lambda_e` when traversing an
edge from rank seven to rank eight and subtract it in the reverse direction.
Let the resulting net voltage be `gamma(C) in Z_15`.

### Theorem 5.1 (exact lift-component formula)

The physical lift of `C` has

\[
 \gcd(15,\gamma(C))                               \tag{5.1}
\]

components.  Hence a quotient solution gives one strict physical Hamilton
cycle exactly when the quotient factor is one component and its voltage is a
unit modulo 15.

#### Proof

One quotient traversal translates the sheet by `gamma(C)`.  Its orbit on
`Z_15` has length `15/gcd(15,gamma(C))`, leaving exactly the stated number of
sheet orbits.  Summing over quotient components gives the total physical
component count.  \(\square\)

Connectivity may be imposed by subtour cuts.  Unit voltage and residence may
be audited lazily.  A post-hoc splice is not automatically safe: it changes
the selected local pairs at its seams and can erase the last `q2` or upper
`q1` witness.  Any splice theorem used here must preserve the pair-cover rows
and the residence collars explicitly.

## 6. Two seed interfaces

### 6.1 The strict resident factor

The retained strict factor

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
SHA-256 4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
```

is a genuine full assignment of (2.2)--(2.3).  Independent replay gives

```text
selected edge orbits       858
quotient components          1
quotient voltage              1 mod 15
physical upper cycles         1 of length 6435
minimum residence run         4
middle / lower q1       6435 / 6435, squarefree
q2 orbits                 288 / 335  (47 holes)
upper-q1 orbits            268 / 335  (67 holes)
```

Its rank-six quotient-load histogram is

\[
 1^{165}2^{105}3^{18},
\]

so its quotient collision value is `P_Psi=159`, `Xi_Q=65`.

### 6.2 The NAND complete-`q2` trace

The independently audited NAND word

```text
scratch/k15_nand_euler_mixed_psi.cw
SHA-256 de3786f9b6b3f3b211e991fbf9f38a2f0a5026b6d63eee07810439c2746d3936
```

visits all 335 rank-six turn-colour orbits, but only 367 of the 429 rank-eight
orbits and only 367 of the 429 rank-seven orbits in one quotient period.
Therefore it is not a feasible `x,y` assignment: (2.2) requires one pair at
every one of the 858 quotient vertices.

It is nevertheless a sound soft seed.  Each actual occurrence supplies pair
data on both shores.  The implementation uses the modal pair at every seen
vertex only as a CP-SAT hint, and uses the complete occurrence-frequency
vector when the NAND-overlap objective is selected.  Neither the modal pairs
nor the frequency vector is ever asserted as a factor equation.

## 7. Positive complete-`q2` factor certificate

The pair-only master with all 335 constraints (3.4), but without (3.5), has
an exact positive solution.  The retained files are

```text
scratch/k15_global_pair_cover_q2complete_raw_20260729.json
scratch/k15_global_pair_cover_q2complete_20260729.audit.json
```

with SHA-256 values

```text
raw   59fb88bd84180d16348e0b86f234362d0df490cefa160977fe939e1f837f5dc1
audit d49297b7f2af18d740186367eefd1f57f8bdcf732c07de23c46c89fa6e43e549
```

The stable compact-JSON encoding of the sorted selected edge-ID list has
SHA-256

```text
f1a5c676af5fadcf376bf2f3d5b7eec5298e47a825653896a84988225597ab61
```

and the independent replay status is `PASS`.  A second catalogue/physical
implementation then re-audited the same 858 selected IDs.  The exact result
is

```text
middle owners                  6435 / 6435, each once
rank-7 lower-q1 colours        6435 / 6435, each once
rank-6 q2 physical targets     5005 / 5005
rank-6 q2 orbits                335 / 335
q2 quotient loads              1^249 2^78 3^8
P_Psi, Xi_Q                     102, 8
rank-9 upper-q1 orbits          263 / 335  (72 holes)
rank-9 physical targets        3945 / 5005
quotient components               2
component rank-8 sizes          324, 105
component voltage classes     {2,13}, {1,14}
physical upper cycle lengths    4860, 1575
minimum residence run              2
residence bad runs              1215
residence total shortfall        1680
```

Both quotient component voltages are units, so each quotient component lifts
to exactly one physical cycle.  This proves, within the strict equivariant
factor fibre, that simultaneous squarefree middle/lower-`q1` and complete
lower `q2` are feasible.  It also isolates the collision-zero residue
sharply: the eight load-three colours account for exactly

\[
 \Xi_Q=102-94=8.                                  \tag{7.1}
\]

At any `Xi_Q=0` endpoint, every one of the eight current load-three colours
must have load at most two, and at least eight distinct current singleton
colours must be raised.  The minimum load-vector repair transfers exactly one
occurrence from each triple to eight distinct singleton colours.  A legal
factor path may make additional intermediate or endpoint changes.

The certificate does **not** prove a valid carrier for the compiler.  It has
72 upper-`q1` orbit holes, two physical components, and 1,215 short residence
runs.

### 7.1 Urgent grouped-sigma soundness reconciliation

After a report that the separate pair-cover lane had failed a stronger
physical verifier, the exact raw artifact above was replayed again by a new
no-import auditor:

```text
scratch/audit_k15_paircover_q2_claim_reconciliation_20260729.py
scratch/k15_paircover_q2_claim_reconciliation_20260729.audit.json
```

Their SHA-256 values are

```text
source 4addba9f5287c298cefb69719f59e172dad02eb89ce8494e0efb392009867435
audit  34df852f95c59c318e05ee8f4faea5910d07efd8b0d086083adfb72f04d12e1e
```

The fresh audit explicitly rebuilds all 3,432 voltage-labelled incidences,
including the 14 doubled endpoint pairs.  The selected artifact uses one
edge from three doubled pairs, no edge from eleven, and never selects both;
its explicit choices and selected-ID list have empty symmetric difference.
It then expands the literal physical cycles and returns
`PASS_CLAIM_SCOPE` with exactly the ledgers displayed above.  On each short
rank-six orbit, all five physical targets have load three, corresponding to
quotient-occurrence load one.

The grouped trusted `SigmaInstance.verify_factor` independently returns two
physical cycles of lengths 1,575 and 4,860, 6,435 unique middle states,
5,005 lower-`q2` targets, 3,945 upper-`q1` targets, and minimum run two.
Thus the q2-only claim passes.  The stronger
`audit_sigma_factor_candidate_20260729.py` correctly rejects this artifact
because that auditor requires complete upper `q1` and residence four.  Its
failure is a scope mismatch, not a doubled-edge, voltage, or short-orbit
encoding counterexample.  The full reconciliation is recorded in

```text
MATH_AUDIT_K15_PAIRCOVER_Q2_SOUNDNESS_RECONCILIATION_20260729.md.
```

## 8. Implementation and audit boundary

The new complete explicit-`x` implementation is

```text
scratch/search_k15_quotient_pair_cover_cpsat_20260729.py
SHA-256 f89e880f8265bd6066672ec0ef39b1ae54503b4f1c362acd53e57313906e5bf1
```

Its deterministic catalogue-only audit gives

```text
edge variables                         3432
pair variables                        24024
pair choices at every vertex             28
parallel endpoint multiplicities     1^3404 2^14
rank-6 candidate counts               12^2 36^333
rank-9 candidate counts               12^2 36^333
lower-pair table SHA  09016236c04d556bd282f28fe6879aa9da5ee355f0617e6da913be561b695bcb
upper-pair table SHA  5f5023d5daa13a856c36a26e223e8fe80c3621286f7def1cc7c9b6c159f57747
```

The model supports:

1. hard `q2` coverage;
2. hard upper-`q1` coverage;
3. the exact `n_C<=2` collision-zero refinement;
4. the optional complement-symmetric equations (3.8);
5. a complete strict-factor assignment hint (not a feasible assignment of
   the configured shadow-cover rows);
6. soft occurrence-frequency hints from the NAND trace;
7. literal component, voltage, physical-shadow, and residence audits on an
   emitted assignment.

Two separately implemented pair-only masters independently agree on all
3,432 incidence edge records and all 24,024 local pair colours.  The
complement-symmetric submaster then closed the simultaneous static pair-cover
gate positively.  Because Theorem 3.2 makes upper-`q1` coverage redundant
on this subface, the successful run imposed all lower-`q2` rows and
complement symmetry while omitting the duplicate upper rows.  A separate
physical replay checked every upper target directly.

The retained simultaneous certificate is

```text
scratch/k15_global_pair_cover_simultaneous_raw_20260729.json
SHA-256 38690ae7288da3f27e772af08e3022edfc3956903f29d4e311d50b3fb60e1783

scratch/k15_global_pair_cover_simultaneous_20260729.audit.json
SHA-256 dedac1b8d3ea409a86f812e66dd82a4de8a32027892a2c5a91c657fe09938545

scratch/k15_global_pair_cover_simultaneous_solver_20260729.stdout
SHA-256 906ec60d0d2a425aee75dd91df826dd712754b4c9596878644b11fb2272da9e6
```

The feasibility solve returned `OPTIMAL` after 39.367882828 seconds on four
H100 CPU workers, with 166,048 conflicts and 10,380,668 branches.  The
generator's selected-incidence semantic hash is

```text
6d848a1731c56e7a688f405d29e819124db259baa63f6e1c55d81fe5dd348f5a
```

and the independent replayer's sorted arc-ID serialization has hash

```text
68c7ab46cd2d0ab09b701acccf669147b05e00cca7b4fd137edb344c4fdd4b95.
```

The hash difference is a serialization difference, not a selected-edge
mismatch.

The exact status hierarchy is:

```text
PAIR_COVER_FEASIBLE:
  degree two on both shores + complete q2 + complete upper q1

PHYSICAL_CARRIER_PASS:
  PAIR_COVER_FEASIBLE + TOPOLOGY_RESIDENCE_PASS

TOPOLOGY_RESIDENCE_PASS:
  one physical cycle + residence, whether or not both pair covers pass

COMPILER:
  NOT_EVALUATED until the deeper shadows, safe cut, and literal common-word
  interface also pass
```

## 9. Simultaneous immediate-shadow certificate

The simultaneous certificate has the exact physical and quotient statistics

```text
selected quotient edge orbits          858
middle owners                         6435 / 6435, each once
rank-7 lower-q1 colours               6435 / 6435, each once
rank-6 lower-q2 targets               5005 / 5005
rank-9 upper-q1 targets               5005 / 5005
rank-6 quotient loads                 1^259 2^59 3^16 4^1
rank-9 quotient loads                 1^259 2^59 3^16 4^1
pair-collision sum, each deck          113
collision-floor excess, each deck       19
```

Indeed

\[
 59+16{3\choose2}+{4\choose2}=113=94+19.        \tag{9.1}
\]

The two short target orbits are covered, and all 5,005 physical targets on
both shores occur.  Complement symmetry is literal edge-by-edge.

The physical load histogram on each deck is

\[
 1^{3870}2^{870}3^{245}4^{15}6^5,
\]

with physical pair-collision sum 1,770.  One selected pair on each shore
uses the same quotient endpoints with two distinct voltages: pair IDs 11309
and 23463 select edge IDs 3229 and 3230.  Their lift is the physical
15-cycle below, not a physical loop.  Thus the 14 parallel-edge pair choices
omitted by the older 11,998-choice table are not merely formal: one is used
by this exact certificate.

The seven quotient components, written as
\((\text{rank-eight mass},\text{voltage})\), are

\[
 (195,2),(195,2),(17,3),(17,3),(2,4),(2,4),(1,11). \tag{9.2}
\]

They lift to 11 physical cycles of lengths

```text
2925, 2925,
85, 85, 85, 85, 85, 85,
30, 30,
15.
```

The chronology has minimum residence two, exactly 600 positive coordinate
runs of length two and 750 of length three.  Hence it has 1,350 bad runs and
residence shortfall

\[
 2\cdot600+750=1950.                            \tag{9.3}
\]

The deeper physical audit finds 303 missing lower-`q3` targets, 303
missing upper-`q2` targets, 75 missing upper-`q3` targets, and zero
missing upper targets at depths four through seven.  The compiler status is
`NOT_EVALUATED`.

Thus the exact positive boundary is

\[
 \boxed{\text{middle and lower q1 squarefree}
 +\text{complete lower q2}
 +\text{complete upper q1}}
\]

inside the complement-symmetric \(\mathbb Z_{15}\)-equivariant factor fibre.
The symmetry restriction is sufficient, not without loss of generality.

## 10. Sharp remaining boundary

The static simultaneous pair-cover gate is closed positively.  The exact
residual intersection problem is:

1. reduce both load vectors to the cap-at-two collision floor if that
   refinement is required;
2. obtain one quotient component of unit voltage, or prove an exactly
   pair-cover-preserving splice;
3. restore residence at least four;
4. repair lower `q3` and the deeper upper tower while preserving both
   immediate pair covers;
5. audit a safe opening and the literal common-`Q` compiler.

An alternating circuit in the bipartite factor fibre preserves middle
ownership and lower `q1` exactly, but it need not preserve (3.4), (3.5),
residence, or component voltage.  A feasible pair-cover point still does not
imply a resident Hamilton carrier, higher shadows, or a contiguous-OR word.
These quantifier and implication boundaries are not relaxed in this note.
