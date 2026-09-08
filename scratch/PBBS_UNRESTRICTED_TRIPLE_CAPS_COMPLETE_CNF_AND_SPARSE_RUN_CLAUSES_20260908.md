# Unrestricted overlapping H3 caps: complete CNF and sparse coordinate-run constraints

2026-09-08. Independent pure-proof note by `exact_equality_structure`.
No mathematical program or solver was run for this proof.

The equivalence below permits every H3 position to change. There are
no full anchors and no requirement to preserve individual rank-seven
pair occurrences. It freezes the H1/H2 components and preserves every
native rank-eight triple on H3. Under precisely these hypotheses,
the Boolean formula is satisfiable if and only if the capped cyclic
bank covers the complete nonempty cube.

The relevant source and endpoint facts are in
[the exact cap criterion](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md),
Sections 1–5, and
[the triple-preserving host certificate](K17_TRIPLE_PRESERVING_SHORT_HOSTS_AND_CANONICAL_ANCHOR_MENU_CERTIFICATE_20260908.md),
Sections 1–2. The latter directly recomputed all triple deficits and
all singleton/pair host cores. The previous
[anchor-menu CNF](PBBS_TRIPLE_PRESERVING_BLOCK_MENUS_AND_COMPACT_SAT_20260908.md)
does not itself cover this unrestricted problem: removing anchors
requires the explicit global preservation constraints proved here.

## 1. The exact unrestricted architecture

Use the original canonical k17 bank with aperture H=min(height,3).
Every H1/H2 component is unchanged. On each H3 component, indexed
cyclically with period v, the original source is

    D_i = X_i intersect X_(i+1) intersect X_(i+2) intersect X_(i+3).

Each D_i has rank six, each adjacent pair has rank seven, and each
native triple

    R_i = D_i union D_(i+1) union D_(i+2)                 (1.1)

has rank eight. The original four-letter windows are their prescribed
rank-nine owners. Every period is at least 17, so the three positions
in a cyclic triple are distinct.

Let P_i be the union of the single-position exclusion deficits over
all native triples containing i. The retained structural proof and
the direct finite census identify it with

    P_i = (X_i minus X_(i-1)) union
          (X_(i+3) minus X_(i+4)).                      (1.2)

Equivalently P_i contains exactly the coordinates whose positive
source run starts or ends at i. It is nonempty and has size one or
two. Since a triple that needs such a coordinate has no other
original source supplying it, every triple-preserving cap must keep
P_i at i, even when many other positions are capped simultaneously.

The allowed unknown letters are therefore

    P_i subset E_i subset D_i,                          (1.3)

at EVERY H3 position. No anchor is fixed. In addition, impose

    E_i union E_(i+1) union E_(i+2) = R_i                (1.4)

for every cyclic triple. The upper inclusion in (1.4) is automatic
from E_i subset D_i; only the coordinate-supply conditions remain.

All longer source-window ORs are preserved by (1.4), since they are
unions of consecutive triples. Thus all original rank-eight and
higher witnesses remain, including all rank-nine owners. The
remaining requirement is exactly coverage of ranks one through seven.

## 2. Complete singleton/pair host catalogue

For a cyclic interval I of length one or two write

    P_I = union_(i in I) P_i,
    V_I = union_(i in I) D_i.

A target S has a triple-preserving cap on I, with all other letters
left full, if and only if

    P_I subset S subset V_I.                            (2.1)

Necessity follows from (1.3) and E_i subset D_i. For sufficiency use

    E_i=D_i intersect S for i in I, and E_i=D_i outside I. (2.2)

Its interval union is exactly S. Every new letter contains its
nonempty pin. For a coordinate omitted from S, the edit removes no
endpoint of any of its source runs: such an endpoint would belong
to P_I. Any deletion is therefore inside a source run and removes
at most two consecutive occurrences. The neighboring retained
occurrences are at distance at most three. This is exactly the
coordinate-run condition for native triple preservation. Permanent
coordinates satisfy the same cyclic gap test. Hence (2.2) preserves
every native triple.

Equivalently, the exact triple deficit of I is

    G_I = union_t [R_t minus
                   union_(j in [t,t+2] minus I) D_j],

and the same argument proves G_I=P_I for |I|<=2. This includes
intervals crossing the canonical cyclic cut and cases where a
deletion would otherwise erase an entire short coordinate run.

This is also the complete catalogue of possible individual lower
witnesses in ANY solution of (1.3)–(1.4). A rank<=7 witness cannot
have length at least three because it would contain a fixed rank-eight
triple. It must be a literal or an adjacent pair, and its pins and
original source impose (2.1). Conversely each such host is individually
realizable by (2.2).

The word "individually" matters: (2.2) assumes other letters are full.
Different assigned hosts can overlap and can remove each other's
coordinate supply. Global conditions (1.4), not the local tests
alone, enforce their compatibility.

## 3. Exact sparse form of native triple preservation

Introduce a Boolean e_(i,x) for each x in D_i minus P_i. Interpret
e_(i,x)=1 as retaining that coordinate. Coordinates in P_i are
constant 1; coordinates outside D_i are constant 0.

The direct preservation clause for x in R_t is

    e_(t,x) OR e_(t+1,x) OR e_(t+2,x).                   (3.1)

Together over all t and x in R_t these clauses are equivalent to
(1.4). There is a substantially simpler but exactly equivalent way
to generate the nontrivial clauses:

* consider only x present in ALL THREE D_t,D_(t+1),D_(t+2);
* if x belongs to a pin at one of these positions, omit the clause;
* otherwise add the three-variable positive clause (3.1).

To prove equivalence, take a coordinate of an original triple that
is present at only one or two of its positions. Its three-bit
availability pattern is one of

    100, 010, 001, 110, 011, 101.

Each pattern exhibits a source-run start or end inside the triple.
That endpoint is pinned, so the original clause is already true.
If the availability pattern is 111, a pin again makes the clause
true; otherwise all three entries are actual optional variables
and (3.1) is necessary. Pattern 000 is not in R_t and supplies no
clause at all. This proves exact equality of the simplified and
full constraints, including across the cyclic cut.

In coordinate-run language, keep both original run endpoints and
forbid three consecutive deleted positions inside that run. This is
equivalent to distance at most three between consecutive retained
positions. A coordinate present around the entire cycle has no
endpoints and simply needs the cyclic no-three-zero condition.

Thus, AFTER pins are fixed, every remaining triple-preservation
clause has exactly three positive optional-coordinate literals.
No extra unit or two-variable preservation clauses are missing.
There are at most 6*22,134 such clauses before removing pin-satisfied
ones, because at most six coordinates are present in a source letter.
This is an analytic upper bound, not a newly executed clause census.

## 4. Exact complete formula with forward witness selectors

Let O be the lower targets already covered by the frozen H1/H2
components. For each nonempty rank<=7 target S outside O and each
eligible singleton/pair host I satisfying (2.1), introduce a selector
q_(S,I). The cap bits e_(i,x) are shared by ALL hosts containing i;
they are not copied independently for different targets.

If q_(S,I) is true, require exactly the following:

    for every i in I and x in D_i minus S:
        e_(i,x)=0;

    for every x in S:
        OR_(i in I) e_(i,x)=1.                          (4.1)

The implication clauses are respectively

    (-q_(S,I) OR -e_(i,x)),
    (-q_(S,I) OR OR_(i in I) e_(i,x)),                  (4.2)

with the constants from Section 3 simplified. Coordinates in P_I
belong to S by eligibility; selectors cannot delete mandatory pins.
Positive clauses with no available position cannot occur for an
eligible host because S subset V_I.

For every required target add its coverage clause

    OR_(eligible I for S) q_(S,I).                      (4.3)

An empty host list is an empty clause, certifying infeasibility.
Add either the full triple layer (3.1) or its proved sparse equivalent.
This completes the formula.

No reverse implication from an accidental target occurrence to its
selector is required. No per-position, per-pair, or per-channel
at-most-one restriction is required. If distinct targets selected
the same interval, their two exact union requirements in (4.1)
would already conflict. Distinct overlapping intervals may select
compatible targets and must remain allowed.

In particular, do NOT copy the old anchor-frame block domains,
rank-six reservation capacities, or fixed boundary-pair palette
into this formula. They are additional restrictions that are not
part of the present architecture. Every cyclic adjacent pair of an
H3 component is a candidate channel.

## 5. Proof of satisfiability equivalence

Suppose first the formula has a satisfying assignment. Decode all
cap bits to E_i. They satisfy (1.3), hence are nonempty. The global
triple layer gives (1.4), so the complete rank>=8 bank palette is
preserved. For each required lower target, (4.3) selects at least
one host and (4.1) makes its interval union exactly that target.
The frozen components supply O. Therefore the decoded cyclic bank
covers every nonempty target.

Conversely, suppose a bank in the stated architecture covers every
target. Assign its actual coordinate bits to e. Its prescribed
triple equalities satisfy the global triple layer. For each lower
target outside O, choose one actual witness. Section 2 proves that
the witness is a singleton or adjacent pair and is among the
eligible hosts. Set its selector true, and set all unchosen selectors
false. Every implication and coverage clause then holds.

This is an exact equivalence. It neither replaces simultaneous
feasibility by individual hosts nor demands that witnesses be
disjoint. It decides a complete CYCLIC BANK on its existing source
positions. Even a satisfying assignment would still need a separate
legal joining/opening argument to become a length-B(17) linear word.

## 6. Fixed host assignments have a canonical maximal cap

There is a useful equivalent description when a collection of target
hosts has already been selected. Let that collection be (S_alpha,I_alpha)
and set

    F_i=D_i intersect
        intersection_(alpha:i in I_alpha) S_alpha,      (6.1)

using the full ground set for an empty intersection. These are the
largest caps permitted by all selected negative requirements.
Every P_i remains, by local eligibility of each selected host.

Those selected hosts admit a triple-preserving realization if and
only if F itself preserves all triples and realizes every selected
target. For any feasible E, we have E_i subset F_i. Enlarging E to F
cannot exceed a prescribed target on its selected interval and
cannot exceed an original triple, because F_i subset D_i. It cannot
destroy a positive coordinate requirement. Hence a feasible E
implies that F works; the reverse implication is immediate.

Equivalently, for each coordinate x, remove the union of selected
intervals whose target omits x. The remaining available positions
must avoid a three-position deleted block inside an x-source run,
and every selected target containing x must retain an x-position
inside its own interval. This is a complete constructive verification
for fixed assignments. It is not an assertion that selecting such
assignments is a flow or that a fractional assignment can be rounded.

## 7. Implementation audit checklist and present boundary

The implementation should be checked against the exact mathematical
objects above:

1. Native H3 source letters and directly verified triple pins; H1/H2
   frozen; no anchor-derived restrictions.
2. One shared bit per optional physical coordinate at a cyclic H3
   position, with pins true and outside-source coordinates false.
3. Every native triple preserved, including wraparound. A sparse
   generator must use precisely the equivalent rule of Section 3.
4. Every singleton and cyclic adjacent pair host from (2.1), for
   every lower target not already fixed on a frozen component.
5. Forward exact-output implications and one coverage clause per
   required target, without artificial disjointness conditions.
6. A returned model independently decoded and replayed on literal
   capped cycles, checking all triples and all named target coverage.

These items are correctness interfaces, not a claim that a solver
has returned a model. An unsuccessful bounded run would not prove
infeasibility; an UNSAT claim needs independently checked evidence.
The canonical-anchor contradiction does not decide this unrestricted
formula, because its fixed full anchors were genuine restrictions.

This note itself has performed no new computation. A separate code
audit and any authorized single bounded solver run are to be recorded
with their own status and artifacts.
