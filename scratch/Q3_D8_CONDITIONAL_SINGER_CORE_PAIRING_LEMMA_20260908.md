# Conditional Singer core: forced triple types and fourteen Y skeletons

2026-09-08. Root's reduction, independently audited and written by
cover-selectors. Pure mathematics; no computation. The generic-bundle
coverage profile below is a hypothesis, not a consequence of selecting
arbitrary two Singer orbits.

## 1. Hypotheses and notation

Use the canonical critical target classes A,...,F and direction sets
from Q3_D8_TRANSLATION_CRITICAL_GEOMETRY_AND_PARITY_20260908.md.
In particular, A is a singleton, B has 21 vertices, and F is the
disjoint union of seven four-element sets F_d, indexed by nonzero
d in E=F_2^3. Set

    Y=A union B,       X=D union E.

Fix a Singer subgroup S of GL(3,2), cyclic of order seven. Assume
fourteen admissible generic six-edges, forming two S-orbits, are
pairwise disjoint and cover exactly

    C:28, B:14, D:28, F:14,

with no A or E vertices. The uncovered core then has the profile

    A:1, B:7, D:14, E:7, F:14,                       (1)

and has 43 vertices. The S-action on B is free, since a fixed B
vertex would fix its distinguished nonzero two-valued point. Thus
the seven remaining B vertices form one S-orbit.
Since the removed set is S-invariant, the
remaining F vertices meet every F_d equally: S acts transitively on
the seven directions. Hence precisely two vertices remain in each F_d.

We seek one of the existing self-complementary full four-edges plus
thirteen self-complementary short triples, with exact critical
coverage. Every selected edge must be wholly contained in the
currently uncovered core; otherwise this exact-cover budget already
fails.

The full four-edge has two F vertices in the same F_(d0), and two
X vertices. Its class multiset is F,F,E,E or F,F,D,E. These facts
hold for the two canonical full words 00223311 and 00232311 and
are preserved by coordinate transformations. The common direction
also follows directly from the self-complementary row identity.

## 2. Exactly six FFX, four YYX, and three XXX triples

Every self triple has a common direction and meets each F_d evenly.
It also meets Y evenly. These are the structural parity relations
proved in the preceding critical-geometry note.

After removing the full edge, the residual demands are

    F:12,        Y:8,        X:19.                  (2)

For F, the demand is zero in F_(d0) and exactly two in every other
F_d. Parity and triple size force every triple containing F to have
exactly two F vertices and one X vertex; its two F vertices lie in
the same F_d. Consequently there are exactly six FFX triples, one
for each d different from d0.

Similarly, each triple meeting Y contains exactly two Y vertices
and one X vertex. Thus there are exactly four YYX triples. These
ten triples use ten X vertices. The nine remaining X vertices
therefore require exactly three XXX triples. No other triple type
is compatible with the two parity rules.

This proves the forced decomposition

    6 FFX + 4 YYX + 3 XXX.                           (3)

It does not assert that suitable triples or disjoint X choices exist.

## 3. The remaining B direction-sharing graph is a seven-cycle

A canonical B vertex is specified by a Fano line L and its unique
two-valued point a in L; the other two points of L have value zero.
Its two directions are exactly L minus {a}. Indeed, a valid matching
must pair the two-valued point a with one of these zero-valued
points, giving precisely the other two line points as differences.

The remaining B orbit has seven vertices and fourteen direction
incidences. Singer symmetry makes the direction degrees equal, so
each direction occurs at exactly two B vertices. Form a graph on
these seven B vertices by joining the pair incident to each direction.

This graph has no parallel edges: an unordered pair of directions
{b,c} uniquely determines the B vertex with line {b,c,b+c} and
two-valued point b+c. Thus distinct B vertices cannot share both
directions. It has no loops, and every B vertex has degree two.

The graph is a simple 2-regular graph, and S acts transitively on
its seven vertices. Its cycle components must have equal size
dividing seven; every component has at least three vertices. Hence
the graph is a single seven-cycle.

## 4. Fourteen necessary Y pairing/direction skeletons

The four YYX triples pair the eight Y vertices. Since A occurs only
once, it is paired with one distinguished B vertex, called the root.
The six other B vertices must pair along direction-sharing edges:
each self triple needs a common direction.

Deleting the root from the seven-cycle leaves a path on six vertices.
That path has a unique perfect matching, obtained by repeatedly
matching its endpoint to its only neighbor. Thus the three B-B
pairs and their directions are forced by the root.

A has every direction. The A-root pair may therefore use either
of the root's two directions. There are exactly

    7 root choices * 2 root-direction choices = 14  (4)

possible pairing/direction skeletons under these necessary rules.
This count does not promise that each skeleton is realized by four
available self triples using distinct, compatible X vertices. The
six FFX triples and three XXX triples must also be supplied, and all
noncritical target constraints still need to be checked separately.

The lemma is conditional on (1) and the stated disjoint generic
coverage. It supplies an exact finite reduction after such a source
pair is certified; it does not certify any generic source pair or
construct a complete physical rectangle bank.
