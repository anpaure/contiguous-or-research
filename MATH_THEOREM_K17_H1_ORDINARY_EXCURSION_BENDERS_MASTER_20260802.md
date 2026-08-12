# K17 `h=1`: ordinary-excursion Benders master

**Date:** 2026-08-02  
**Status:** exact reductions, a sufficient outer-selector subclass, and an
implemented fail-closed master.  Feasibility of the strengthened master is
not asserted here.  This note does not solve the source flags, lower
compiler, or `nu(17)`.

## 1. Ordinary-coatom contraction

Use the fixed-boundary augmented-incidence lollipop with missing coatom
`M`, duplicated coatom `D`, and all owners of rank nine.  For every ordinary
coatom

\[
                         q\notin\{M,D\},
\]

its degree is exactly two.  Contract its two selected incidences to an
unordered owner edge.  Call the resulting graph on the 24,310 owners `P`.

### Lemma 1.1

If the augmented incidence graph is connected, then `P` is the disjoint
union of two linear paths and has exactly 24,308 edges.

#### Proof

The lollipop Euler trail lists all owners linearly.  Its 24,309 internal
owner adjacencies consist of one adjacency through the internal occurrence
of `D` and one through every ordinary coatom.  Removing the single `D`
adjacency from a linear path leaves two linear paths.  The endpoint `M` and
terminal occurrence of `D` are not internal owner adjacencies.  \(\square\)

This contraction removes the only topology-dependent provider.  Every edge
of `P` is a literal owner adjacency in both Euler orientations.

## 2. Exact pair channel

For an ordinary rank-eight coatom `q` and distinct labels `a,b` outside
`q`, introduce

\[
 p_{q;a,b}\ \Longleftrightarrow\
 y_{q,q+a}\wedge y_{q,q+b}.                         \tag{2.1}
\]

The degree-two row at `q` makes exactly one of its 36 pair variables true.
There are

\[
                 (24310-2){9\choose2}=875088          \tag{2.2}
\]

such variables.  Three Tseitin clauses per pair give an exact channel.

### Lemma 2.1 (rank ten)

A rank-ten target `U` has an ordinary immediate provider exactly when

\[
 \bigvee_{\substack{q\in{U\choose8}\\q\notin\{M,D\}}}
 p_{q;U\setminus q}                                  \tag{2.3}
\]

is true.

#### Proof

For `U-q={a,b}`, the selected owner pair is `q+a,q+b`, whose union is
exactly `U`.  Conversely every ordinary adjacent owner pair has this unique
intersection and union.  \(\square\)

### Lemma 2.2 (rank eleven)

Fix a rank-eleven target `U` and a centre owner `T in {U choose 9}`.  Put
`U-T={a,b}`.  Let `A(T,a)` be the ordinary pair variables joining `T` to
an owner obtained by adding `a`, and define `A(T,b)` analogously.  If

\[
            \left(\bigvee A(T,a)\right)\wedge
            \left(\bigvee A(T,b)\right)              \tag{2.4}
\]

holds, then `P` contains a three-owner path with centre `T` and union `U`.
Conversely every length-two ordinary excursion with union `U` has this
form.

#### Proof

An edge in `A(T,a)` replaces one member of `T` by `a`; an edge in
`A(T,b)` does the same with `b`.  The two groups are disjoint.  Since an
owner has only two selected incidences, selected edges from the two groups
meet at `T` and form the claimed path.  The converse reads the two newly
introduced coordinates of any such path.  \(\square\)

One witness variable for each `(U,T)` gives 680,680 witness variables and
two implication rows per witness.  Requiring one witness for every `U`
is an exact rank-eleven row inside the ordinary-excursion subclass.

## 3. Residence without chronology variables

For a coordinate `x`, let `P_x` be the subgraph of `P` induced by owners
containing `x`.

### Retired overstrong criterion and corrected seam rule

It is formally true that if every component of every `P_x` has order at
least four, then either Euler orientation is resident: adding the one `D`
adjacency can only join components.  But this condition is structurally
impossible at the fixed linear boundary and must not be used as the search
criterion.  If the second incidence of `B` is `(B-{c})B`, then the ordinary
neighbour of `B` through that coatom omits `c`.  Hence `B` is a singleton
component of `P_c`, harmless only because `B` is a clipped endpoint.

The corrected seam rule is exact.  The graph `P` has four degree-one owners:
`B` and the three selected neighbours of `D`.  Ordinary floor-four cuts are
valid only for coordinate components disjoint from this four-owner seam
bank.  If the two path components pair their endpoints as

```text
(B,d1) and (d2,d3),
```

then `d1` cannot be terminal, since joining `d2,d3` closes the other path
into a cycle.  The two valid physical choices join `d1` to `d2` or `d3` and
leave the other as terminal.  Residence at the seam components must be
checked on those two literal augmented-coatom chronologies, with `B` and
the chosen terminal clipped.  The implementation performs exactly this
replay; if all structural rows pass but both seam choices fail, it emits a
complete selected-incidence no-good.

Let `C` be a current component of `P_x` of order at most three.  Let
`E(C)` be a spanning set of its currently selected internal pair edges and
let `delta_x(C)` be all legal ordinary pair variables joining `C` to an
`x`-owner outside `C`.  Whenever `C` is disjoint from the four seam owners,
every acceptable master solution obeys

\[
       \bigvee_{e\in E(C)}\neg p_e\quad\vee\quad
       \bigvee_{f\in\delta_x(C)}p_f\quad\vee\quad
       \bigvee_{\substack{T\in C\\D\subset T}}y_{D,T}. \tag{3.1}
\]

Indeed, retaining the internal spanning edges and choosing no crossing
edge leaves the same short component **provided it also remains disjoint
from the selected seam bank**.  Because the three `D` neighbours may change,
the implemented row additionally contains every incidence literal `y_(D,T)`
with `T in C`.  Selecting one such literal legitimately moves `C` into the
exact seam audit.  With those activation literals, (3.1) is a globally valid
partition cut rather than an incumbent no-good.

## 4. All-upper ordinary excursions

For an upper target `U`, let `P[U]` be the subgraph induced by owners below
`U`.

### Lemma 4.1

If a component `C` of `P[U]` satisfies

\[
                         \bigcup_{T\in C}T=U,          \tag{4.1}
\]

then `U` is a contiguous-owner union in both lollipop orientations.

#### Proof

Each component of `P` is a linear subpath of either Euler orientation, up
to reversal.  A component of the induced subgraph is therefore a contiguous
owner interval.  Equation (4.1) is its interval union.  \(\square\)

This is sufficient, not necessary: a valid witness may cross the one
exceptional `D` adjacency.

Suppose the current components of `P[U]` are `C_1,...,C_t` and none has
union `U`.  Retain a spanning forest inside every `C_i`.  Any future
ordinary-excursion solution for `U` must either delete one retained forest
edge or select an ordinary pair joining two current components.  Hence the
valid Benders row is

\[
 \bigvee_{e\in\bigcup_i E(C_i)}\neg p_e\quad\vee\quad
 \bigvee_{\substack{f=vw\\v\in C_i,w\in C_j,i\ne j\\v,w\subset U}}p_f.
                                                               \tag{4.2}
\]

If neither event occurs, every current `C_i` stays connected and distinct,
so all component unions remain proper subsets of `U`.

## 5. Implemented master

Before giving the implementation counts, there is a complete two-case
symmetry split at the fixed boundary owner.  The owner `B` already uses the
fixed incidence `MB`; its other selected coatom is either `D`, or is obtained
by deleting one of the seven coordinates in `M cap D`.  The stabilizer of
the ordered pair `(M,D)` is transitive on those seven coordinates.  Hence
the two clauses

```text
DB selected
(B-{0})B selected
```

give two disjoint cases exhausting the master up to the remaining symmetry.
They are useful solver branches, not additional assumptions.  Neither may
be discarded by an ordinary-component argument, because the short component
at `B` is boundary-exempt.  The builder leaves the split free; a branch file
may add either unit row.

The artifacts are

```text
scratch/build_k17_h1_global_outer_cnf_20260802.cpp
scratch/decode_k17_h1_global_outer_model_20260802.cpp
```

They were compiled with `g++ -O3` and the base master was built on the H100
CPU under

```text
/home/amodo/or15/work/root_k17_h1_global_outer_20260802/
```

The authenticated build reports

```text
variables  1,774,558
clauses    8,540,093
rank-10 rows 19,448
rank-11 rows 12,376
CNF size   275 MB
build      1.87 s, 55 MB RSS
```

The decoder first emits exact incidence connectivity cuts.  On a connected
lollipop it independently replays both Euler orientations, emits (3.1) for
every short ordinary component, and emits (4.2) for every missing upper
ordinary excursion.  Acceptance of these rows proves the connected central,
positive-residence, and complete-upper gates.  It does not prove the source
refresh flags or ranks-one-through-seven compiler.

The builder also has a `lazy11` mode.  It retains every rank-ten row but
omits the minimal three-owner restriction at rank eleven; the decoder then
uses the general excursion cut (4.2) starting at rank eleven.  This larger
class permits long rank-eleven excursions and has 1,093,878 variables and
7,166,357 base clauses.  The eager and lazy modes are complementary search
lanes, not different acceptance criteria: both require the same complete
ordinary-excursion replay before acceptance.

A still looser `lazy10` mode retains the exact pair channel but introduces
both rank-ten and higher rows only through (4.2).  It is intended for staged
CEGAR: the first model is inexpensive, while every emitted target row is a
sound ordinary-excursion partition cut and all targets are still literally
replayed at acceptance.

The proof-exact lead is the separate `exacth1` mode.  It imposes ordinary
rank-ten provider rows for exactly the 19,412 targets not containing `D`.
Those rows are necessary, because such a target cannot use the exceptional
`D` adjacency.  The 36 rank-ten targets containing `D`, all higher targets,
and all seam residence cases are checked only on the two materialized
augmented paths `Q_0,...,Q_W`.  The exact decoder uses interior residence
partition cuts disjoint from the four seam owners and otherwise emits a
complete 48,620-incidence chronology no-good.  It does not reuse the
ordinary `P[U]` upper cuts, since a valid exact witness may cross `D`.

The CNF and replay verdicts have different scopes.  A SAT verdict for one
`exacth1` CNF is only a **q1 scaffold**: it proves the degree factor and all
19,412 necessary non-`D` rank-ten rows, but says nothing yet about the 36
`D`-containing rank-ten targets, higher upper targets, or exact residence.
Only successful materialization of one augmented path together with the
literal two-orientation replay is an unconditional outer-carrier witness.

Conversely, the two normalized boundary branches (core branch and shared
`DB` branch) exhaust the h=1 boundary choice.  A DRAT-verified UNSAT result
for **both** clean `exacth1` branch CNFs would therefore prove that no h=1
factor can satisfy even the necessary rank-ten gate, and would rule out the
global h=1 outer architecture.  UNSAT for just one branch is scoped to that
branch.  This statement does not apply to the retired ordinary-component
formula of Section 7, whose extra residence restriction was only a
sufficient and in fact overstrong subclass condition.

## 6. Guarded C6 topology completion

The component patcher

```text
scratch/patch_k17_h1_components_by_c6_20260802.cpp
```

now has a guarded mode.  It loads the exact accumulated clauses over both
incidence variables and channelled ordinary-pair variables.  Before accepting
an alternating incidence hexagon it updates the six incidence literals and
the affected pair literals, and rejects the toggle if any guarded clause
would become false.  It also protects `MB` and the selected normalized
`DB`/core boundary-branch incidence.  Every accepted toggle therefore preserves:

* all incidence degree equations, by the alternating-C6 identity;
* the fixed boundary rows;
* every named accumulated residence/upper/connectivity clause; and
* strict descent of the literal component count.

On the first staged outer master it connected a 28-component factor in 24
toggles while preserving all 15,833 accumulated clauses.  On the next staged
factor it connected 128 components in 103 toggles while preserving all
15,918 prior clauses.  These are positive topology-completion witnesses for
those exact clause fibres; they do not imply that the terminal factors pass
the still-unadded residence or upper rows.

The independently replayed second connected factor has 5,753 literal short
augmented-coatom runs and upper holes

```text
rank 10..17: 4196, 2353, 450, 7, 0, 0, 0, 0
```

on its better Euler orientation.  Its ordinary sufficient graph has 5,763
short components and 7,008 upper excursion holes, producing 12,771 further
exact partition cuts.  Thus guarded C6 completion closes the topology row
for these iterations, but substantial residence and palette routing remains.

## 7. Exact audit of the retired all-component face

The core-normalized `lazy10` round 3 formula returned `UNSAT` and its DRAT
proof was independently checked after normalizing the zero-padded DIMACS
header:

```text
variables 1,093,878
clauses   7,175,740
core      57 clauses, 1 lemma, 57 resolution steps
verdict   s VERIFIED
check     5.366 s, 625 MB RSS
```

This is **not** evidence against `h=1`.  The complete 57-clause core consists
of the units `MB` and `(B-{0})B`, owner-degree clauses at `B`, their pair
channels, and one all-component residence row for coordinate zero.  That row
demands an ordinary zero-preserving neighbour of `B`, although its only
ordinary selected coatom is `B-{0}` and every owner paired through it omits
zero.  The core therefore proves only the intentionally overstrong and now
retired statement

```text
every ordinary coordinate component, including the clipped boundary B,
has order at least four.
```

The corrected decoder never emits that boundary row.  No global K17,
`h=1`, upper, or residence impossibility follows from this proof.

## 8. Round-one provenance correction

On 2026-08-02 an auxiliary driver with an obsolete hard-coded stage name
overwrote the raw `round1.kissat.out` and zeroed its DRAT file.  Those two raw
artifacts are unavailable and must not be cited or assigned their former
hashes.  The incident did not alter the frozen connected model or the two
untouched ingredients from which the original round-one formula is
deterministically reconstructed:

```text
cumulative0 cuts                         86503cb37daf4018d54d19dc0c05154f7f85c72715982b076e8cdb7e307bcd8f
preserved 3,680-row round0 q1 cut         77b26de6b1a76a90eeff203a4f40d11625bb318dfb2c3c711ad86dbdeeb9c524
reconstructed cumulative1                45156e7311bb50e15e1bd55013e65ed015f05c08c00241650dbc50dcb0e188a4
reconstructed original round1 CNF        771b91134e6e4d91bdd153bf878d566c7c6110c298f6645a37bc5da5a89337cd
frozen guarded complete round1 model      e15fec8ffa3cd93cf183d54d93c9a5965e350fac9bd574d66b44e0dcd31fd97a
strict replay audit                       ea627cbb618c151b0ef1a29b7d93cc51f6dcafba9823836b47bc5ef94a078d31
```

The reconstructed CNF and cumulative bank match their pre-incident hashes
byte for byte.  The independent complete-model replay checks all 1,093,878
variables, 7,155,100 clauses, and 22,247,152 literal occurrences and returns
`PASS_K17_H1_COMPLETE_DIMACS_MODEL_REPLAY`.  The repair bundle is frozen at

```text
/home/amodo/or15/work/root_k17_h1_global_outer_20260802/
  provenance_round1_reconstructed_20260802/
```

The hardened driver has SHA-256
`2fe1f84cd08fd684c9825d2f88b5c42084edfcf3330cd8da60d9e45a36d48daa`.
It requires the absolute stage directory as a positional argument, locks that
directory, verifies the live solver's `/proc` working directory, and refuses
every pre-existing round output.  This correction restores model provenance;
it does not recreate or authenticate the overwritten original solver log or
DRAT stream.

## 9. Guarded q1 optimization and passive downstream audit

The guarded C6 patcher now has an optional heuristic phase.  It keeps every
accumulated clause, the normalized boundary, and augmented connectivity hard,
while scoring all 19,412 necessary non-`D` rank-ten targets incrementally.
Only a strict best model is saved, and every promoted model is subsequently
extended and replayed by the exact q1 checker.  This is a search accelerator,
not a new proof rule.

The best authenticated q1 counts obtained so far are:

```text
core branch, staged CEGAR round 4          18,325 / 19,412
core branch, guarded 10M C6 walk           18,985 / 19,412
core branch, chained guarded 20M C6 walk   19,175 / 19,412
core branch, chained guarded 50M C6 walk   19,341 / 19,412
core branch, loss-safe C6/C8 pair chain    19,386 / 19,412
core branch, loss-safe residual circuits   19,407 / 19,412
shared branch, guarded 10M C6 walk         19,016 / 19,412
```

The 50M incumbent is connected and was independently extended to all
1,093,878 channelled variables before the exact q1 replay.  The replay reports
exactly 71 missing necessary non-`D` rank-ten targets and 3,195 literals in
the corresponding exact cut.  Its authenticated artifacts are rooted at

```text
/home/amodo/or15/work/root_k17_h1_global_outer_20260802/
  exact_q1_anneal71_stage_20260802/
```

with hashes

```text
connected factor model       24296cdf3b600c4018c109d8de9d352b05913e2cd08b5c7074675fdfc9c63df4
extended complete model      0debc7f6aabfb30b9f69e13da39e3ca355f29206d7dec3e5592cc5544f7c4f63
exact 71-target q1 cut       5c4b9a9a3cb6fe2a0d4a17b02475a6aa092456dc356db8ab1edab085a1825b0f
round-zero cumulative bank   431ebb3a8d7643ff6a95ea5c148f3337862aa8c3d1af449052c7b4c6bd2b5ba3
round-zero CNF               ec791a6654575f45ba5ef5480d1a2f565a4caa7f6f5388353cb29b0e9eed6499
round-zero map               d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63
round-zero build audit       4f0989dd1652b26c7d67cf28b0fe1969ea860b06feb8b99c0414da66813baaf3
```

This remains a q1-local incumbent.  The 71 rows were used to seed a fresh
proof-safe exact CEGAR stage; neither satisfiability of all accumulated q1
rows nor any residence/deeper-upper conclusion is asserted by the seed.

### 9.1 Complete current-state C6/star-C8 pair descent

A separate deterministic catalogue enumerates, at each incumbent, every
alternating incidence C6 and every four-petal star C8 on a rank-seven core.
It retains only moves which replay all 16,261 frozen clauses, computes their
exact signed effect on all 19,412 q1 multiplicities, and tests connectivity.
It then tests every root-disjoint pair among the gainful connected moves and
accepts only a strict loss-safe improvement.  Repeating this complete
current-state calculation gives the monotone chain

```text
71,69,67,65,63,61,59,57,55,53,51,49,47,45,43,41,39,37,35,33,31,29,28,26
```

holes, after which no single retained C6/star-C8 or root-disjoint retained
pair improves the q1 score.  The terminal factor is independently replayed
and remains connected:

```text
root       /home/amodo/or15/work/root_k17_q1_targeted_static_20260802
model      census22.independent.model
model SHA  645de2d68cb0b012bbea2d7f7027b7f62f86e9d4e43b9b70fceb22c60dc00a4a
audit SHA  80af20fb0c5ae04a0335f7eee3e4da55efb166a5072152d24eafc2e40d0877da
extended   08c8794960d02c8c1b091206c551b80d1a6e0f07ec21dbc32d5e6d3a6efe9bf2
q1 cut     70ed7ac6cd23f5830639cc898224e34887982057e7614372d037ac2363897dbc
```

Exact replay reports `19,386/19,412`, hence 26 necessary non-`D` holes.
The plateau excludes only the stated single-move and root-disjoint
two-move catalogue at this incumbent.  Longer alternating circuits,
overlapping compound packets and unrestricted factor reselection remain
open; no q1 impossibility follows.

### 9.2 Long alternating-circulation descent

The five-line owner-degree constraint has a larger exact move space than
C6/star-C8.  Relative to a selected factor, any degree-preserving exchange
is an alternating circulation in the rank-eight/rank-nine incidence graph.
The targeted residual search forces one candidate provider of a missing
rank-ten target and enumerates diversified shortest alternating return paths
of length at most 20.  A candidate is accepted only after literal replay of
all frozen clauses, connectivity, degree equations and every q1
multiplicity; in the loss-safe lane it may remove providers only from
colours of multiplicity at least two.

Starting from the 26-hole static plateau, these longer circuits give

```text
26,25,24,23,22,21,20,19,18,17,15,14,13,12,11,10,9,8,7,6,5
```

holes and then plateau for the searched path budget.  Every accepted step
has zero displaced colours; the two-unit step at 17 holes installs two new
colours.  The terminal factor passes an independent replay:

```text
root       /home/amodo/or15/work/root_k17_q1_targeted_static_20260802
model      residual5.independent.model
model SHA  de100adac19a65893b8d9b873634e5159a5d11adefc86264932c2588ad67ffa2
extended   93065d0e73fa9aea7abc5ba4c95161bde318def83cab720184ecc757888b8036
q1 cut     e0c7c6812af4f41132fc5ecceb7268e2350dbc3a9e98029b5c3aa4b81778b54c
source     85500a3101ba3ea718c61701623adcce1b84677a68f85ade78cbd0a7f0df4143
```

Exact q1 replay is `19,407/19,412`, leaving five necessary non-`D`
targets.  This is not a proof that five is unavoidable: longer paths,
additional diversified returns, and compound circuits with a temporary
one-unit debt are outside the completed catalogue.

Passive literal Euler replay was run without feeding any emitted residence or
upper cut back to SAT.  It shows that q1 optimization strongly reduces the
rank-ten upper holes but does not yet solve residence or deeper ranks:

```text
factor                         short runs   upper holes at ranks 10,11,12,13
core round 1                      5,649       4,292, 2,438, 485, 15
core round 3                      5,745       1,558, 1,878, 357, 11
core round 3, 2M anneal           5,729       1,065, 1,724, 334,  8
core round 4, 10M anneal          5,608         436, 1,604, 305,  2
core round 4, chained 20M         5,592         249, 1,652, 342,  7
core round 4, chained 50M         5,576          93, 1,547, 288,  7
core loss-safe C6/C8 chain        5,574          48, 1,534, 288,  7
core residual-circulation chain   5,572          27, 1,534, 291,  7
shared round 5, 10M anneal        5,649         408, 1,581, 269,  4
```

All holes at ranks 14 through 17 vanish in the last five displayed factors.
The residence count remains about 5,600, so q1 completion is only the first
outer gate.  The passive cut files are explicitly named
`*.cuts.DO_NOT_ADD.cnfpart`; they are diagnostic artifacts and were not added
to any live cumulative stage.

The exact passive 50M replay has audit SHA-256
`ae9d9d7771dd1f11bdaf905bc5af96d4104d178333c6ab2cc9d2f084c3dae6e3`.
It has 5,574 short ordinary cyclic components before opening and 5,576
short literal runs in either best linear orientation; the table records the
literal linear quantity.
Its 93 linear rank-ten holes include the topology-dependent `D` targets and
opening effects omitted from the 19,412-row necessary q1 score; hence the
figures 71 and 93 are consistent and must not be conflated.

The terminal 26-hole factor has 5,572 short ordinary cyclic components and
5,574 short literal runs in its best linear orientation.  Its passive audit
has SHA-256
`32edaf0fa9b8d771c4f6a71f96825192e31cbcc859248310102d50fe885cf36d`.
Again these diagnostic cuts were not fed to the q1 search.

The terminal five-hole factor has 5,570 short ordinary cyclic components
and 5,572 short literal runs in its best linear orientation.  Its passive
audit has SHA-256
`5c142c123efd7f671d9c6e51dbae791bedf42c3c88b7a0b4a27ffe31e71f8719`.
The 27 literal rank-ten holes include the five necessary non-`D` holes plus
the excluded `D`/opening effects; the two counts answer different gates.
