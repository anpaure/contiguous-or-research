# Disjoint OR bundles give a coupled integral host criterion

2026-09-09. Pure-proof continuation by `exact_b_finite_frontier`.
No solver, program, numerical census, or mathematical execution was run.

The result is a restricted sufficient construction: fix disjoint target
bundles and rank-eight witness backbones, then use ONE ordinary bipartite
matching to place all proper-pair bundles and residual literal bundles
together. A whole-bundle edge already contains one compatible pair of
literal caps. This avoids committing to an arbitrary proper-pair flow
before the residual literal allocation is considered.

There is an explicit disjoint target-bundle template in every dimension.
For ranks six/seven at k19 it contains11,088 OR triples. That is a static
target packing, not a host matching or a complete k19 construction. The
fixed palette must be removed before any of these triples receives credit.

## 1. Prior results and the exact restriction that restores integrality

The existing [K17 three-level chainization theorem](../MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md)
already supplies a complete named lower-target partition using normalized
Boolean containment and Dilworth. The
[compressed-normal recoupling theorem](../MATH_THEOREM_K17_GLOBAL_COMPRESSED_NORMAL_CHAIN_RECOUPLING_AND_SOCKET_BENDERS_GATE_20260802.md)
also proves integrality of a particular static containment assignment.
It records that a successful static table can fail its physical socket
tests. Thus static rank-splitting or normality alone is not a new solution
to the common-cap problem.

Here the three-target pieces have the different form

    {E,F,E union F},   E,F incomparable,

and are intended as the two literal outputs and the pair output of one
physical two-position block. They are not inclusion chains. The useful
additional condition below is their simultaneous literal host test.

The [actual two-letter menu counterexample](PBBS_TWO_LETTER_MENU_COMPATIBILITY_AND_NONMATROID_OBSTRUCTION_20260908.md)
shows why three individually eligible channels cannot be matched
independently. Its eligible literal labels A,B and pair label C fail
A union B=C; the associated demand system even fails matroid exchange.
The older
[configuration counterexample](../MATH_THEOREM_NAMED_UPPER_DUPLICATE_CONFIGURATION_HYPERGRAPH_AND_COUNTERCUT_20260807.md)
also rules out deducing integral physical choices merely from fractional
configuration feasibility or nested-chain containment.

The present restriction is explicit: the demand family is partitioned
into disjoint bundles BEFORE host matching; each bundle uses one block;
each edge certifies the entire bundle with one cap pair. Once this is
done, the only remaining conflicts are two bundles using the same block.
Those are exactly bipartite matching conflicts. Allowing alternative
overlapping bundle decompositions is outside this integral formulation.

## 2. Fixed physical data and simultaneous preservation

Take a supplied finite source bank and an independent two-position frame
as in the [proper-pair lemma](K19_GENUINE_PAIR_RESERVATION_LEMMA_AND_NEXT_FINITE_GATE_20260909.md).
At k19 the editable native letters have rank seven, native pairs rank
eight, and native triples rank nine. Full anchors separate the editable
blocks; unchanged one-position gaps are included in the frozen part.
Every block b has left/right available letters D_b,E_b and nonempty
mandatory pins P_b,Q_b. The frame must certify that ALL simultaneous
choices between pins and available letters preserve every native triple
and every pair touching the frozen part. The minimum-cap replay described
in that earlier lemma is one sufficient finite certificate.

Also require explicit source coverage: the native triples and longer
intervals, together with the frozen components, cover every target of
rank at least nine. All rank-eight targets must have an original internal
pair witness or an already invariant/frozen witness. These are input
hypotheses, not consequences of the dimension or of calling the source
PBBS. No single length-B19 carrier is asserted here.

For every rank-eight target V lacking an invariant/frozen witness,
designate one original internal block with D_b union E_b=V. Choose
backbones

    P_b subseteq B_b subseteq D_b,
    Q_b subseteq C_b subseteq E_b,
    B_b union C_b=V.                                  (2.1)

At other blocks take B_b=P_b,C_b=Q_b, or any explicitly chosen larger
backbones. One block has only one original pair label, so different V
obligations do not require the same block. All subsequent cap pairs
(A_b,F_b) must obey

    B_b subseteq A_b subseteq D_b,
    C_b subseteq F_b subseteq E_b.                     (2.2)

Equation(2.1) then preserves that named rank-eight pair for every such
choice, including choices used to realize low literal bundles. The
source frame preserves the triple deck and hence all longer intervals.
In particular a block whose protected backbone union has rank eight
cannot host a rank-seven OR triple. This conflict is present in the
actual host graph; no capacity is silently counted twice.

Let O be an explicitly witnessed, invariant palette of targets of ranks
one through seven. A conservative choice is the distinct literal labels
at the frozen H3 positions. Any larger O must have witnesses invariant
under ALL allowed choices(2.2). Define the remaining demands exactly as

    R={S subseteq[19]:1<=|S|<=7} minus O.               (2.3)

Original variable literal labels are not included in O merely because
they existed before editing. Unless independently protected, they remain
demands in R and must be supplied by the construction.

## 3. Whole-bundle host graph and constructive Hall theorem

Partition R into a family G of disjoint nonempty bundles of these types:

* OR triple: {U,V,S}, with U,V distinct proper subsets of S and
  U union V=S. It must be realized by the literals U,V in either order.
* Literal pair: {U,V}, with U!=V. It must be realized by the two
  literals U,V in either order; its pair output is extra uncredited cover.
* Literal singleton: {U}. It is realized by one literal; the other
  can be any allowed nonempty cap.

For each bundle g and block b, put an edge g~b precisely when there is
one cap pair obeying(2.2) and the specified realization rule for g.
Keep a literal representative with each edge. These tests need no
independent-channel approximation:

* For a triple or literal pair, test the two orientations of the two
  prescribed literals directly against(2.2).
* For a singleton, test its containment between one shore's backbone
  and availability. The other original available letter is a valid
  companion. Test either shore.

For the fixed source, backbones and bundle partition, the following are
equivalent:

    (i) Each bundle can be assigned to a distinct compatible block.
    (ii) For every A subseteq G, |A|<=|N(A)|.           (3.1)

This is ordinary bipartite Hall. Equivalently, a rational nonnegative
edge weighting with bundle sum1 and block sum at most1 can be rounded
integrally by the bipartite matching theorem. This integrality comes
from the graph in(3.1), not from an unproved matroid property of menus.

Given a saturating matching, use the stored two-letter representative
at every matched block and the original available letters at every
unmatched block. The blocks are disjoint. Every final letter satisfies
(2.2), so every native triple, upper interval, invariant witness and
designated rank-eight backbone witness survives simultaneously. Every
target in O keeps its invariant witness; every target in R belongs to
exactly one assigned bundle and has its prescribed literal or pair
witness. Thus every rank is covered by one actual capped bank.

This matches proper-pair reservations AND all residual literal jobs
together. It does not first freeze the outputs of a maximum reservation
flow. An edge for a triple fixes both required literal subtargets along
with its pair target, so its three credited labels cannot disappear
during a separate allocation stage.

The theorem is sufficient for the full bank and exact for the specified
one-bundle-per-block architecture. It is not necessary for every possible
cap: a general solution could spread a chosen bundle across blocks or
use another partition. Backbones are also part of the supplied instance;
their existence alone does not establish any useful Hall inequalities.

## 4. Explicit disjoint OR triples in every dimension

Fix n>=h+1 and h>=1, order the coordinates1,...,n, and pair the first
coordinates as (1,2),(3,4),... . For every

    1<=j<=floor((n-h+1)/2)

and every (h-1)-subset T of {2j+1,...,n}, form

    U_(j,T)=T union {2j-1},
    V_(j,T)=T union {2j},
    S_(j,T)=T union {2j-1,2j}.                         (4.1)

The ranks are h,h,h+1. Both lower sets are nonempty proper subsets of
S, and their union is S. These named triples are pairwise disjoint:
the first occupied coordinate pair of U or V has exactly one member,
and identifies j; at that fixed j the member and T determine the set.
The first occupied pair of S has both members and likewise identifies j
and T. The different ranks prevent a lower label from coinciding with
an upper label of any triple. This includes h=1, when T is empty.

The exact number of triples is

    q(n,h)=sum_(j=1)^floor((n-h+1)/2) binom(n-2j,h-1). (4.2)

Equivalently q(n,h)=binom(n-2,h-1)+q(n-2,h), with zero when n<h+1.
This is an explicit target construction valid in all dimensions; it
does not claim maximum possible packing or any prescribed physical host.

For n=19,h=6, equation(4.2) is

    6188+3003+1287+462+126+21+1 =11,088.

It names22,176 distinct rank-six labels and11,088 distinct rank-seven
labels. Out of all94,183 targets of ranks one through seven, the other
60,919 labels are not in these triples. On a free formal tape, placing
each triple's two facets consecutively and every other target literally
uses

    2*11,088+60,919=83,095 positions.                  (4.3)

This is only a lower-family formal word, not an available cap of the
19-coordinate source. In particular its length cannot be compared with
all87,514 H3 positions while forgetting the frozen anchors among them.
The next section gives the correctly charged frame version.

## 5. Remove fixed labels first; the exact frame count

Intersect the template(4.1) with the actual remaining demand family R.
Retain a template triple as a three-target bundle ONLY when all three
of its labels lie in R. Call this retained subfamily T_clean and let
q_clean be its size. Drop the other templates completely as templates;
any of their still-missing labels returns to the residual demand pool.
This explicitly avoids giving three units of credit to a triple whose
pair target or literal facet was already supplied by a frozen anchor.

Let M=|R|. There are M-3q_clean residual named targets. In any fixed
ordering, pair consecutive residual labels into literal-pair bundles,
with one literal singleton if their number is odd. Along with T_clean
this is an explicit disjoint partition of all R. The number of jobs is

    J=q_clean+ceil((M-3q_clean)/2)
     =ceil((M-q_clean)/2).                             (5.1)

The host theorem applies to exactly this partition. A different ordering
of residual pairs might have different eligibility; the formula is not
a claim that every ordering satisfies Hall. The theorem also permits
any other supplied disjoint residual pairing, with its actual host graph.

For the canonical k19 H3 frame, let P=87,514, let F be all frozen H3
positions outside the editable two-position blocks, and let L_F be the
set of their distinct literal labels. With O=L_F there are

    b=(P-|F|)/2 blocks,   M=94,183-|L_F| demands.

The weakest necessary consequence of bundle Hall, J<=b, is exactly

    q_clean >=6,669+(|F|-|L_F|).                       (5.2)

Thus repeated frozen labels are charged, and proper-pair labels already
in L_F earn zero credit. The earlier raw count11,088 cannot replace the
actual q_clean or the right side of(5.2). Choosing backbones can eliminate
further edges without changing this scalar inequality; all such local
losses remain in Hall(3.1).

After a matching succeeds, the literal facets of the selected triples
and the prescribed residual literal labels are distinct named demands
by construction. This removes the earlier risk of accidentally spending
several positions on the same newly fixed subletter. Extra pair outputs,
the unused companion of a singleton, and unmatched blocks are allowed
to duplicate labels, but receive no credit toward satisfying R.

## 6. Concrete next gate, and present status

A meaningful future finite proposal has four finite inputs: an actual
source/frame/palette certificate; explicit rank-eight backbones; the
disjoint bundle partition of the nonfixed demands; and its whole-bundle
host graph with literal edge representatives. A saturating matching
then is a complete integral lower-allocation certificate, followed by
one direct literal replay. A Hall-deficient subset refutes that fixed
choice. No separate raw-q flow is needed or justified first.

The current progress is this coupled sufficient theorem and the explicit
all-dimensional disjoint target template. Neither a k19 host graph nor
a saturation certificate has been constructed here. Static normality
from the earlier K17 chainization does not imply this graph's Hall
conditions: full named literal compatibility and protected rank-eight
backbones are additional restrictions. Even a successful capped-bank
certificate still needs a separate witness-preserving fusion/opening
argument before it is an optimal-length single word. No exact19 or
all-dimensional equality claim is made.
