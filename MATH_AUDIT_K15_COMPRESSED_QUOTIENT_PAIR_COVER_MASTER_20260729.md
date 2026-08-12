# Exact audit of the compressed `C_15` quotient pair-cover master

Date: 2026-07-29

Status: theorem proved and independently replayed at catalogue level.  This
note proves that the `27,456`-Boolean master is exactly the
`C_15`-equivariant spanning-factor problem with complete lower `q2` and upper
`q1` support.  It does not assert that this master is feasible, resident,
connected, or compiler-ready.

## 1. The voltage-labelled quotient

Let `rho` cyclically permute `[15]`, and let `B` be the bipartite incidence
graph between ranks seven and eight of the Boolean lattice.  The action of
`<rho>` is free on both central ranks.  Indeed, a subset fixed by a nontrivial
rotation is a union of equal-length coordinate cycles, whereas neither seven
nor eight is divisible by `3`, `5`, or `15`.  Hence each central orbit has
size fifteen and the two quotient shores have

\[
 N={1\over15}{15\choose7}=429
\tag{1.1}
\]

vertices each.

Fix a canonical rank-seven representative `L`.  Every missing coordinate
`a` gives the physical incidence

\[
 L\subset L\cup\{a\}.
\]

Writing

\[
 L\cup\{a\}=\rho^{\lambda_e}U_e
\tag{1.2}
\]

with canonical rank-eight `U_e` defines one voltage-labelled quotient edge
`e=(L,a,U_e,lambda_e)`.  There are eight such edges at every lower vertex,
and, by the free action and incidence double count, eight at every upper
vertex.  Therefore

\[
 |E(Q)|=429\cdot8=3432.
\tag{1.3}
\]

The voltage labels are essential: the quotient has 3,404 endpoint pairs of
multiplicity one and fourteen endpoint pairs of multiplicity two.  The two
edges in a doubled pair have different voltages.

## 2. The exact local compression

Introduce one bit `x_e` for every voltage-labelled edge.  For every quotient
vertex `v` and every unordered pair `p` of its incident edges, introduce a
turn bit `y_(v,p)`.  Impose

\[
 \sum_{p\in{\delta(v)\choose2}}y_{v,p}=1,
\tag{2.1}
\]

and, for every `e in delta(v)`,

\[
 x_e=\sum_{\substack{p\in{\delta(v)\choose2}\\e\in p}}y_{v,p}.
\tag{2.2}
\]

Equation (2.2) is imposed at both endpoints of `e`, using the same global
edge bit.

### Theorem 2.1 (factor-compression equivalence)

The binary solutions of (2.1)--(2.2) are in bijection with the
`C_15`-invariant spanning physical two-factors of `B`.

At each vertex, the unique positive turn `y_(v,{e,f})` makes exactly `x_e`
and `x_f` positive and every other incident edge bit zero.  Thus exactly two
edges are selected.  The shared edge bit makes the choices at the two
endpoints consistent.  The resulting quotient multigraph is spanning and
two-regular, and its voltage lift is a spanning physical two-factor.

Conversely, a `C_15`-invariant physical two-factor descends, with voltage
labels retained, to a spanning degree-two quotient multigraph.  Its two
selected incident edges define the unique positive turn at every vertex,
and (2.1)--(2.2) follow.  This proves the bijection.  In particular, on this
face

\[
 y_{v,\{e,f\}}=x_e\mathbin{\wedge}x_f.
\tag{2.3}
\]

The advertised 56 incidences at a vertex are the `8*7` memberships of an
edge in a local two-edge choice.  Each unordered turn is counted twice, so
only

\[
 {8\choose2}=28
\tag{2.4}
\]

turn bits are needed there.  The exact global Boolean census is therefore

\[
 \underbrace{3432}_{x\text{ edge bits}}
 +\underbrace{429{8\choose2}}_{\text{lower turns}}
 +\underbrace{429{8\choose2}}_{\text{upper turns}}
 =3432+12012+12012
 =27456.
\tag{2.5}
\]

No direct pair-choice witness is duplicated across target rows.

## 3. Literal local colours

Let `U` be a canonical rank-eight quotient vertex.  Align each incident edge
to the `U` frame.  If the two selected lower neighbours delete coordinates
`a` and `b`, then their literal intersection is

\[
 (U\setminus\{a\})\cap(U\setminus\{b\})
 =U\setminus\{a,b\}.
\tag{3.1}
\]

Thus the upper-vertex turn has the exact lower-`q2` colour

\[
 \kappa_-(U;a,b)=\operatorname{can}(U\setminus\{a,b\}).
\tag{3.2}
\]

At a canonical rank-seven vertex `L`, if the selected upper neighbours add
coordinates `a` and `b`, their literal union is

\[
 (L\cup\{a\})\cup(L\cup\{b\})=L\cup\{a,b\}.
\tag{3.3}
\]

Hence the lower-vertex turn has the exact upper-`q1` colour

\[
 \kappa_+(L;a,b)=\operatorname{can}(L\cup\{a,b\}).
\tag{3.4}
\]

The voltage signs in (3.1) are fixed by (1.2): in the upper frame the
deleted coordinate of an edge is `a-lambda_e mod 15`.  The implementation
recomputes this coordinate from the aligned facet rather than assuming it.

### Theorem 3.1 (orbit OR rows are exact support rows)

Complete physical lower-`q2` support is equivalent to

\[
 \bigvee_{\kappa_-(U,p)=C}y_{U,p}=1
\tag{3.5}
\]

for every rank-six `C_15` orbit `C`.  Complete physical upper-`q1` support is
equivalent to

\[
 \bigvee_{\kappa_+(L,p)=D}y_{L,p}=1
\tag{3.6}
\]

for every rank-nine orbit `D`.

To prove the potentially delicate direction, a selected quotient turn lifts
to all fifteen of its translates.  If its target colour has orbit size `s`,
those translates hit each physical member of the target orbit exactly
`15/s` times.  Thus one selected turn covers the entire physical orbit,
including a short orbit.  If no turn in the row is selected, equivariance
leaves every member of that target orbit uncovered.  This proves both
directions.

There are 335 rows of each sign.  At rank six, the only nonfree masks are the
ten masks fixed by the order-three subgroup `<rho^5>`: choose two of its five
coordinate cycles.  They form two orbits of size five.  A rank-six mask
cannot be fixed by the order-five subgroup because six is not divisible by
five.  Hence the remaining

\[
 {5005-10\over15}=333
\]

orbits have size fifteen.  Complementation gives the same census at rank
nine.

For a fixed physical rank-six target, choosing the two added coordinates
gives `binom(9,2)=36` supporting physical turns.  Therefore a free target
orbit has 36 quotient turn candidates, while a size-five orbit has

\[
 {5\cdot36\over15}=12.
\]

The rank-nine count is identical by choosing a rank-seven subset of a fixed
rank-nine target.  Thus both exact candidate histograms are

\[
 36^{333}12^2.
\tag{3.7}
\]

This is support, not multiplicity control: a selected turn over a short
target orbit gives three physical occurrences of each target.  Any load,
collision, or weighted Hall objective must retain orbit weights five and
fifteen.

## 4. Independent executable audit

The second, fail-closed implementation is

```text
scratch/search_k15_quotient_paircover_factor_20260729.py
```

Its H100-only solve mode contains exactly the variables and rows above.  Its
local modes only rebuild and replay catalogues or emitted certificates.  The
independent cross-audit

```text
scratch/audit_k15_compressed_paircover_cross_20260729.py
```

compares this catalogue against the separately written
`search_k15_global_pair_cover_cpsat_20260729.py`.  It compares every
voltage-labelled edge and every local pair colour, rather than comparing only
aggregate counts.  The current replay is `PASS` and gives

```text
edges                              3432
lower turns                       12012
upper turns                       12012
meaningful Booleans               27456
endpoint multiplicities          1^3404 2^14
rank-6 candidate rows             36^333 12^2
rank-9 candidate rows             36^333 12^2
rank-6 orbit sizes                15^333 5^2
rank-9 orbit sizes                15^333 5^2
normalized edge SHA-256  a40fa20e104745704e43708c72b79636e3851691c9baac3d5019e267acfeb9fe
normalized pair SHA-256  73b6368c238c507bd47913729c7bfee9946780295033a063f4eab5d0433495f9
```

Frozen audit/source SHA-256 values are

```text
779380690eebb3e8c9a20698a44ef3b8b6bc921b8b486071e25dd7633b885644  search_k15_quotient_paircover_factor_20260729.py
1cda8b203aa7768d231a08569e3bf741e4249f96f87c81c1dbae5845a4746c42  audit_k15_compressed_paircover_cross_20260729.py
3d4af532837e6facab13555dfbdd736fcd31096141dca981331f1223a76d6b1d  k15_compressed_paircover_cross_20260729.audit.json
f2db06ae104cc253adc7590d47d8a3bbe7842724b13eab462a1f4e7742ae9d8d  frozen_search_k15_global_pair_cover_cpsat_f2db_20260729.py (H100 hybrid-run source)
a364a0e48e1f35dc9610436adf3e841f16290b883f12308de04dfce728fa8fda  graded_quotient_pipeline.py
```

The earlier source hash recorded in
`MATH_THEOREM_K15_Z15_QUOTIENT_PAIR_COVER_MASTER_AND_Q2_FACTOR_20260729.md`
belongs to an earlier implementation revision.  The normalized logical
digests above, not equality of source-file hashes, are the cross-catalogue
certificate.

The strict factor replay now checks exact JSON integer edge IDs, catalogue
hashes, degree two, both 335-row covers, structured requirements,
connectivity/unit-voltage/residence when claimed, the entire recorded audit,
and the exact repository-choice serialization when it exists.  Generator
provenance is reported separately when the frozen source paths remain
available.  This is an independent mathematical certificate replay; it does
not authenticate a solver transcript, round history, hostname, variable
count, or a frozen file whose recorded path is no longer available.

The exact H100 run used the two retained seeds only as branching hints.  The
resident factor owns all 3,432 edge hints and all 12,012 lower-turn hints.
The NAND `q2`-complete trace owns the upper-turn hints at the 367 upper
vertices it visits: 307 vertices have one observed turn, 58 have two, and two
have three, so sixty vertices require a deterministic tie break and 62 upper
vertices remain unhinted.  This gives 25,720 distinct hinted variables.  No
variable receives two hints.  The combined hint is deliberately not asserted
as a feasible assignment--only ten of the 367 chosen NAND upper turns agree
with the resident upper turn--and no NAND turn is fixed as a constraint.
The H100 processes were externally terminated after search startup and wrote
no solution or terminal solver response.  They therefore establish neither
feasibility nor infeasibility; the solver status of the full 670-row master
remains `NOT_EVALUATED` at theorem level.

## 5. Complement-equivariant row pairing

For a central representative `S`, write

\[
 S^c=\rho^{\epsilon(S)}\overline S,
 \qquad \overline S=\operatorname{can}(S^c).
\tag{5.1}
\]

The phase `epsilon(S)` is unique on ranks seven and eight.  If a quotient
edge is represented by

\[
 e=(L,U,\lambda),\qquad L\subset\rho^\lambda U,
\]

physical complementation sends it to the edge orbit

\[
 e^*=\bigl(\overline U,\overline L,
 \epsilon(L)-\epsilon(U)-\lambda\bigr),
\tag{5.2}
\]

because it reverses the incidence to
`(rho^lambda U)^c subset L^c`.  This is a shore-swapping involutive
automorphism of the voltage-labelled quotient multigraph.

For a local turn `p={e,f}`, put `p*={e*,f*}`.  Directly complementing
(3.1) or (3.3) gives

\[
 \kappa(p^*)=\operatorname{can}\bigl(\kappa(p)^c\bigr).
\tag{5.3}
\]

### Theorem 5.1 (complement-equivariant half-cover reduction)

Suppose the selected factor satisfies

\[
 x_e=x_{e^*}\qquad(e\in E(Q)).
\tag{5.4}
\]

Then its selected local turns satisfy `y_p=y_(p*)`.  Consequently, for every
rank-six orbit `C`, the lower-`q2` row for `C` and the upper-`q1` row for
`can(C^c)` have the same truth value.  Hence, inside the
complement-equivariant factor fibre,

\[
 \boxed{\text{all 335 lower-`q2` rows}
 \iff \text{all 335 upper-`q1` rows}.}
\tag{5.5}
\]

Indeed, (5.4) maps the unique selected pair at each vertex to the unique
selected pair at the complementary vertex, and (5.3) bijects the two cover
rows.  Thus a complement-equivariant `q2`-complete degree-two factor solves
all 670 pair-cover clauses.  Without (5.4), no such implication is valid.

The frozen audit gives 1,716 complement pairs of edge variables and 12,012
complement pairs of local turns, with no fixed edge or turn.  Its map hashes
are

```text
edge map  f4184edc714084ae1abfa36a222430a43a2b50a0936288af1101941e4a8fbb84
turn map  14bfa683a725e433c5f7e8388a547bed7413cd92366f509ed9a9213c4024db45
```

Among the fourteen doubled endpoint cells, four are self-complementary cells
whose two voltage-labelled edges swap, and the other ten form five
complementary cell pairs.  The two short target pairs are exactly

\[
 3171\leftrightarrow7399,
 \qquad
 5285\leftrightarrow11627.
\tag{5.6}
\]

Complement symmetry closes only the two first-shadow cover families.  It
still gives no connectivity, voltage, residence, deeper-shadow, or compiler
conclusion.

## 6. Parallel turns and compiler serialization

Exactly fourteen lower-shore turns select both voltage-distinct edges of a
doubled endpoint pair.  Such a choice saturates the same two quotient
vertices and forms an isolated quotient digon.  It is a valid component of a
disconnected equivariant bipartite two-factor, but it contracts to a loop and
is intentionally absent from the repository's 11,998-row Johnson `Choice`
table.

Consequently either of the following is sufficient for a complete 429-choice
compiler serialization:

1. forbid those fourteen lower turn variables; or
2. require the quotient factor to be connected.

A connected spanning factor cannot contain an isolated digon.  The verifier
therefore emits no fake choice list for a loop-containing factor and checks
all 429 choices exactly for a loop-free factor.

## 7. Exact implication boundary

A feasible point of (2.1)--(2.2), (3.5), and (3.6) proves all of the
following simultaneously:

1. every physical rank-eight middle owner occurs once;
2. every physical rank-seven vertex occurs once and hence supplies its
   lower-`q1` trace colour once as part of the spanning factor;
3. every physical rank-six lower-`q2` target occurs at least once;
4. every physical rank-nine upper-`q1` target occurs at least once.

It does not by itself prove:

1. one quotient component or unit lift voltage;
2. depth-three residence;
3. lower `q3` or any deeper upper shadow;
4. a safe linear opening;
5. a common one-core Hall matching or a literal contiguous-OR word.

Thus the compression is exact and removes the redundant witness layer, but
it does not weaken or close the remaining chronology/compiler gates.  A
running or timed-out CP-SAT process supplies no theorem in either direction;
only an independently replayed selected-edge certificate will be promoted to
a positive result.
