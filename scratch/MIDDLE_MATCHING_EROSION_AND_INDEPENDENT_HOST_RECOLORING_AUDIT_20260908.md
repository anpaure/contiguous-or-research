# Middle-matching erosion and independent-position recoloring

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No word, matching data, or claimed verifier for the proposed 25,374-letter
construction was available during this audit. No dataset-dependent count
or full-cube coverage claim is certified here; no computation was run.

Verdict: both mechanisms are valid under the explicit hypotheses below.
For the matching mechanism, shared matching edges must be excluded:
otherwise a one-owner component is a counterexample to the stated ranks.

## 1. Exact hypotheses for a middle-matching component

Let an oriented alternating component be

    L_i subset U_i superset L_(i+1), indices modulo its period,

where |L_i|=r, |U_i|=r+1, and r>=3. Require consecutive lower owners
to be distinct and consecutive upper owners to be distinct. For two
perfect matchings on the complete middle-incidence graph, edge-disjointness
of the matchings supplies the needed nontrivial components; global unique
vertex ownership supplies the remaining distinctness.

Every lower step is then a Johnson exchange:

    L_(i+1)=(L_i\{d_i}) union {a_i},
    U_i=L_i union {a_i}=L_i union L_(i+1).

Assume the insertion residence condition CYCLICALLY, including the last
two transitions of every component:

    a_i belongs to L_(i+1), L_(i+2), and L_(i+3).       (1.1)

Equivalently, a newly inserted coordinate is not deleted on either of
the next two lower transitions. The cyclic qualification is essential.

## 2. Upper uniqueness supplies the omitted zero-run condition

Both U_(i-1) and U_i contain L_i. Since they are distinct (r+1)-sets,

    U_(i-1) intersect U_i = L_i.                       (2.1)

In particular a coordinate cannot be present in L_(i-1), absent in L_i,
and present in L_(i+1). Such a coordinate x would imply
U_(i-1)=L_i+x=U_i, contradicting upper distinctness. Thus every proper
zero run in the lower-owner binary coordinate sequence has at least
two positions.

Condition (1.1) gives every proper positive lower run length at least
three. Because U_i=L_i union L_(i+1), a lower positive run of length l
produces an upper positive run of length l+1. The intervening lower zero
runs have length at least two, so they keep these upper runs separated.
Every proper upper positive run consequently has length at least four.
Coordinates constant throughout a component are harmless.

## 3. Literal erosion and the exact ranks

Set

    E_i=U_(i-3) intersect U_(i-2) intersect U_(i-1) intersect U_i.

For any binary upper run occupying [a,b] with length at least four,
the corresponding E run occupies [a+3,b]. Unions of two, three, or four
consecutive E letters therefore recover respectively [a+2,b], [a+1,b],
and [a,b]. The same identities hold for constant coordinate sequences.
Coordinate by coordinate, this proves

    E_i union E_(i+1)
        =U_(i-2) intersect U_(i-1) intersect U_i,
    E_i union E_(i+1) union E_(i+2)=L_i,
    E_i union E_(i+1) union E_(i+2) union E_(i+3)=U_i.  (3.1)

The pair identity has rank r-1: its right side equals
L_(i-1) intersect L_i, and those distinct r-sets lie in U_(i-1).

Likewise E_i=L_(i-2) intersect L_(i-1) intersect L_i. The first of those
two lower steps deletes d_(i-2) from L_(i-2) and inserts a_(i-2).
The next deleted coordinate cannot be a_(i-2), by (1.1). It therefore
deletes a second, distinct coordinate originally in L_(i-2). Their
threefold intersection has rank r-2.

Thus at r=8 the E letters have rank six, their adjacent pair ORs have
rank seven, their triple ORs are exactly L_i, and their four-window ORs
are exactly U_i, with precisely the indices in (3.1).

This proves middle coverage when the supplied matchings cover all middle
vertices. It does not certify any other rank census or a full ordinary
word until the component openings, joins, and recolorings are supplied.

### Necessary exclusion of a degenerate matching component

Two perfect matchings may share an incidence edge. That shared edge is
a component with one lower owner L and one upper owner U. The lower
successor is L itself, so the insertion condition is vacuous, but E_i=U
has rank r+1 instead of r-2. Merely saying that each vertex appears once
in its component does not exclude this example.

The matching data must therefore verify edge-disjointness, or directly
verify that every lower successor differs from its source. On the
nontrivial components the proof above supplies the claimed implications.

## 4. Exact recoloring domain at an independent set of positions

Let E be a nonzero set word and let the current letters A_i satisfy

    A_i subset E_i,
    A_i union A_(i+1)=E_i union E_(i+1)

on every existing adjacent pair. Let I be an independent set of positions
in the path adjacency graph for a linear word, or the cycle adjacency
graph for a cyclic word. Hence the neighbors of each edited position
remain unchanged during a simultaneous recoloring.

For an internal position i, a permissible replacement S is exactly a
nonempty set satisfying

    E_i\(A_(i-1) intersect A_(i+1)) subset S subset E_i. (4.1)

Indeed the current pair equalities imply
A_(i-1) union E_i=E_(i-1) union E_i and similarly on the right.
The new left pair is correct exactly when E_i\A_(i-1) is contained in S;
the right pair is correct exactly when E_i\A_(i+1) is contained in S.
Their union is the lower bound in (4.1).

At a linear endpoint there is only one neighbor, so the lower bound is
E_i\A_neighbor. If there are no neighbors, no pair constraint is imposed.
These endpoint conventions cannot be silently replaced by two nonexistent
neighbors. Independence ensures that all the legal replacements can be
performed together. The sets may increase relative to the current A_i,
but remain contained in the fixed envelope E_i.

Every interval OR of length at least two is the union of its adjacent
pair ORs. Consequently all such interval ORs are preserved EXACTLY, for
every legal simultaneous recoloring. One-letter targets require the
separate bookkeeping below.

## 5. The maximum-matching objective and preservation of old targets

Fix a finite family F of nonempty targets. Let O be the targets IN F already covered
by the invariant intervals of length at least two or by the unchanged
letters outside I. Build a bipartite graph with left side F\O and right
side the positions in I. A target S is adjacent to i exactly when it is
a nonzero permissible replacement at i under Section 4.

If its maximum matching has size m, the maximum achievable number of
covered targets from F is exactly

    |O|+m.                                                 (5.1)

For the upper bound, every additionally covered target in F\O must be
the chosen one-letter value at some host in I. Choose one such host for
each target; these witnesses form a matching, since a single position
cannot carry two distinct letters. For attainment, assign each matched
host its matched target, and choose any permissible nonzero letter at each
unmatched host; E_i itself always qualifies. A nonempty current letter
may simply be retained. This covers O and every matched target. The upper bound
then gives equality.

All old targets of F can be preserved while achieving this maximum.
Initially match each old target of F\O to one position currently carrying
it. Distinct targets have distinct chosen hosts. Starting from this
matching, augment along alternating paths until a maximum matching is
reached. Previously matched LEFT vertices remain matched after each
augmentation, even though their host may change. Thus every old target
of F remains covered.

Preservation of ALL old targets needs F to include every old target
whose only witnesses are variable one-letter positions. Targets outside
F are not protected by the matching theorem merely because they were
present before recoloring. If O is instead defined as an unrestricted
set of fixed targets, formula (5.1) must use |F intersect O|, not |O|.

## 6. Verification boundary

This note verifies the symbolic implications only. The proposed length
25,374, complete target census, chosen independent host sets, actual
matching sizes, and all component-boundary checks require the literal
artifact or an accessible deterministic generator. None was inferred
from these lemmas or from the user's unavailable claimed checks.
