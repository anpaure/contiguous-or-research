# Exact short-target caps and a constructive capacitated-matching reduction

2026-09-08. Independent pure-proof note by exact_equality_structure.
No mathematical computation was run. The note gives exact local and
simultaneous cap criteria, then an integral flow whose saturation would
construct a complete target-covering bank on its existing W positions.
It does not assert that such a flow is saturated or that the bank has
been joined into a B(17)-word.

The retained source and pin identities are proved in
PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md,
which was read in full for this task.

## 1. Source, owners, pins, and coordinate runs

Fix one physical PBBS component, with distinct middle owners X_i of
rank r+1, indexed cyclically with period v. Fix 1<=H<=h, where h is
its height, and write

    D_i=intersection_(j=0)^H X_(i+j),
    W_t=[t-H,t] modulo v,
    union_(i in W_t)D_i=X_t.

Here v>=2r+1>2H, so all short intervals below are unambiguous proper
cyclic intervals. The letters D_i are nonempty. A positive coordinate
run [a,b] of the owner sequence has length at least H+1 and gives the
source run [a,b-H].

Let Pin_i contain the coordinate entering X_i from X_(i-1) and the
coordinate leaving X_(i+H) on the next transition. These are exactly
the coordinates for which i is the first or last position of a source
run. They may coincide, but Pin_i is always nonempty. Every cap E_i
subset D_i preserving all owner windows must contain Pin_i.

The exact general owner criterion is: for each coordinate, keep both
endpoints of every source run and leave gaps at most H+1 between
successive kept positions. A permanently positive coordinate instead
needs that gap bound around the whole cycle. These are sufficient as
well as necessary, since a kept source occurrence at i supplies that
coordinate to owner indices i,...,i+H.

## 2. One arbitrary interval: the exact deficit core

For any nonempty proper cyclic interval I define

    V_I=union_(i in I)D_i,

    K_I=union_t [X_t minus union_(j in W_t minus I)D_j].   (2.1)

Only owner windows meeting I contribute. Every coordinate in K_I
belongs to V_I, by the original owner identity. It is a coordinate
which at least one owner cannot obtain outside I.

For a target S, the following are equivalent:

1. Some nonempty caps on I, with all other letters full, preserve every
   owner and make the OR on I exactly S.
2. K_I subset S subset V_I.

When these conditions hold, the explicit maximal choice is

    E_i=D_i intersect S for i in I; E_i=D_i otherwise.   (2.2)

Necessity follows because S cannot gain coordinates outside V_I, while
every coordinate of K_I has to be supplied inside I. Conversely, if a
coordinate is retained in S, its appearances in I are unchanged. If it
is omitted from S, (2.1) ensures every owner requiring it has a full
source occurrence outside I. Thus all owners survive (2.2), and its
union on I is exactly S. Every Pin_i, i in I, belongs to K_I, so the
new letters are automatically nonempty.

This criterion includes entire-run deletions and endpoints. It is useful
even for intervals longer than the aperture; the simplified criterion
next is exactly equivalent only in the stated short range.

## 3. Exact pin criterion for every lower-target host

If 1<=|I|<=H, then

    K_I=union_(i in I)Pin_i.                             (3.1)

The inclusion from right to left follows from the indispensable source
run endpoints. For the reverse inclusion, omit a coordinate absent from
the right side. The interval I removes no endpoint of any of its source
runs. Any nonempty deletion is therefore an interior block of length
at most H, leaving its two retained neighbors at distance at most H+1.
Its owner contribution is preserved. A permanent coordinate loses at
most H consecutive positions and satisfies the same gap test. This
works around the cyclic cut as well: crossing a source-run boundary
would delete an endpoint and is already excluded by the pin condition.

Consequently the proposed criterion is exact:

    boxed: union_(i in I)Pin_i subset S subset V_I,
           1<=|I|<=H.                                   (3.2)

Its literal realization is (2.2). No additional nonzero-letter condition
is needed, since every resulting letter contains its original Pin_i.

Moreover this catalogues EVERY possible lower-target interval in ANY
owner-preserving cap of the bank. An interval of length H+1 or more
contains a prescribed middle window and so has rank at least r+1.
Thus a target of rank at most r must use length at most H. Such a
witness necessarily contains the pins at its positions and lies inside
V_I, while (3.2) proves individual realizability. This is a complete
local host catalogue, not merely a family of sufficient examples.

## 4. Simultaneous assigned intervals eliminate the letter search

Suppose targets S_alpha have assigned short cyclic intervals I_alpha,
possibly overlapping. Define their maximal common cap at every position:

    F_i=D_i intersect intersection_(alpha:i in I_alpha)S_alpha,
                                                               (4.1)

where an empty intersection means the full ground set. There exists
an owner-preserving nonempty cap realizing all assigned targets if and
only if F itself does so. Indeed every feasible E_i must lie in F_i.
Enlarging E_i to F_i cannot exceed an assigned target on its interval,
and cannot exceed any prescribed owner because F_i subset D_i. Thus
all equalities and nonemptiness of a feasible E persist in F.

This gives a direct coordinate-wise test with no remaining unknown letters.
For coordinate x let

    B_x=union_(alpha:x not in S_alpha) I_alpha,
    A_x={i:x in D_i} minus B_x.                          (4.2)

Then simultaneous feasibility is exactly:

* A_x retains both endpoints of each source x-run and has successive
  gaps at most H+1 (cyclically if x is permanent).
* For every alpha and every x in S_alpha, I_alpha intersects A_x.

The first condition preserves all owners and implies nonempty letters
through their pins; the second supplies every positive target coordinate.
Negative target coordinates are excluded by construction (4.2).
Thus fixed assignments can be checked by unions of ordinary intervals
inside coordinate runs and by interval intersection queries.

If each assigned pair is individually eligible under (3.2), all pins
survive automatically. The remaining owner obstructions are exactly
connected deleted blocks of H+1 or more positions inside a source run.
The remaining target obstructions are exactly positive coordinates whose
entire assigned availability is deleted by OTHER overlapping assignments.
Individual eligibility by itself therefore does not prove simultaneous
feasibility.

## 5. Preserving additional native rank decks

Fix 1<=p<=H+1. The p-consecutive-owner intersections are recovered by
source windows of width

    w=H+2-p,
    intersection_(j=0)^(p-1)X_(i+j)
       =union_(j=0)^(w-1)D_(i-j).                       (5.1)

Preserving this ENTIRE native deck is equivalent to retaining the same
source-run endpoints and tightening the gap bound from H+1 to w.
For a source run [a,b-H], kept occurrences now cover target indices
[i,i+w-1]; their union must be [a,b-p+1]. This proves both necessity
and sufficiency, including the shared first and last pins.

Preserving this stronger deck also preserves every longer source-window
OR, by taking unions of consecutive w-windows. In particular it preserves
middle owners and the complete upper deck. In this stronger setting,
the pin-only local criterion (3.2) holds for |I|<=w-1. At length w,
the native w-window itself is frozen; a smaller target cannot replace it.

At k=17, H=3:

* Owners of rank9 use w=4, allowing retained-coordinate gaps up to4.
* All native rank8 triples use w=3, requiring gaps at most3.
* All native rank7 pairs use w=2, requiring gaps at most2.
* Preserving every rank6 letter uses w=1 and allows no letter reduction.

These are occurrence-preservation requirements. Merely retaining coverage
of the named rank7 or rank8 layer is weaker and can permit repair at a
different occurrence. That distinction is explicit in the next reduction.

## 6. Full anchors give independent editable positions

Fix a desired preserved window width w. Choose anchor positions so that
every cyclic interval of length w contains an anchor, and keep the full
letter D_i at each anchor. At every other position permit ANY nonempty
letter between Pin_i and D_i. Then every native w-window is preserved.

Proof: source-run endpoints survive through their pins. No deleted block
of length w can occur inside a source run, because it would contain an
anchor carrying that coordinate. Thus the gap criterion of Section5
holds. All edits may be made simultaneously; no independent-trial or
single-edit assumption is involved.

For w=2, this means simply that the editable positions have no adjacent
pair on the cycle. For w=H+1, editable blocks may have length H between
successive anchors. The pins and anchors together are the reason full
owners survive even when an anchor in a particular owner window omits
one of that owner's coordinates: that coordinate then has an available
source-run endpoint in the window, which is pinned.

## 7. A literal capacitated-flow construction on the k=17 bank

Take the capped bank H=min(h,3). Leave all height-one and height-two
components full. On each H=3 component choose an editable set E with no
two consecutive cyclic positions. Its complement is a w=2 anchor set.
All letters on these components initially have rank6.

Let T run over all rank6 targets, and let

    n_T=#{i:D_i=T in the H=3 bank},
    e_T=#{i in E:D_i=T}.

Every n_T is positive: strict-height corridors already give the complete
rank6 literal palette in this bank. Set the allowed edit capacity

    c_T=e_T                  if n_T>e_T,
    c_T=e_T-1                if n_T=e_T.                 (7.1)

Thus at least one original literal occurrence of T is reserved. The
second case is nonnegative because n_T>=1. An already fixed anchor
with label T permits every editable T-position to be used.

Construct the following ordinary integral flow network:

1. A source sends capacity1 to each of the 9401 targets S of ranks1..5.
2. S connects to editable position i with capacity1 exactly when
   Pin_i subset S subset D_i.
3. Each position i sends capacity1 to the label group T=D_i.
4. Group T sends capacity c_T to the sink.

An integral flow of value9401 assigns each required target to one distinct
eligible position. Replace that position's letter by S; leave all other
letters full. This is an actual deterministic construction at the SAME
number of source positions, with the following complete coverage proof:

* Every rank1..5 target is one of the assigned literal letters.
* Every rank6 target retains a literal occurrence by (7.1).
* The H=3 native rank7 pairs remain unchanged by the anchors and pins.
  Together with the untouched H=2 letters these cover all rank7 targets.
* All native triples and middle windows on H=3 are unions of the retained
  pair windows; H<=2 components are untouched. Thus all rank8 and rank9
  targets remain.
* Every higher target remains via its original union of middle owners.

Conversely, within this SPECIFIED architecture (one assigned lower target
per edited position, fixed editable set, and at least one unchanged rank6
occurrence per label), such an assignment gives a flow of value9401.
So max-flow saturation is necessary and sufficient for this construction
scheme. Integrality follows from the ordinary integral-capacity max-flow
theorem; no fractional-to-literal compiler is missing.

This reduction is substantially smaller than searching over arbitrary
letter subsets. Once the editable set is fixed it is a single bipartite
matching with partition capacities. The resulting complete object is a
CYCLIC BANK, not a single cyclic word: opening or fusing its components
into a length24313 linear word remains a separate requirement.

## 8. An exact global capacity check, without execution

The number of semilength-r Dyck words of height at most two is 2^(r-1):
each primitive component is uniquely 1(10)^(m-1)0, so the concatenation
is encoded by a composition of r. At r=8 this gives128 normalized roots,
or 17*128=2176 physical middle states. Therefore the H=3 bank has

    24310-2176=22134

positions, all with rank6 letters. Reserving one full occurrence for each
of the binom(17,6)=12376 rank6 targets leaves at most

    22134-12376=9758

editable positions by this literal-reservation count. The rank1..5 demand
is9401, leaving a scalar margin of357.

This is only the unconstrained global capacity check. A fixed anchor set,
the pin/subset eligibility graph, and the individual label capacities
can create stricter obstructions. No saturating flow has been asserted
or computed. Nevertheless the scalar budget does not rule out the
explicit network, and any successful flow would materialize the claimed
coverage at exactly W existing bank positions.

## 9. Boundary of the result

The single-interval criterion and simultaneous maximal-cap criterion are
exact. The stronger native-deck gap rule is exact. The anchored network
is an explicit sufficient construction and is exact for its stated
restricted architecture. None supplies a free multi-cycle splice,
proves the required flow exists, or resolves exact equality. These
remaining boundaries are separate from the now fully specified local
and global lower-target assignment constraints.

## 10. Subsequent exact decision of the proposed flow route

The bounded calculation and independent certificate replay in
K17_CAPPED_LOW_TARGET_FLOW_HALL_OBSTRUCTION_20260908.md now settle
the proposed restricted flow route negatively. Even allowing EVERY H3
position to be editable, while reserving one occurrence per rank6 label,
the exact maximum assignment is8245 of9401. Its Hall certificate has
1768 small targets and only612 available group capacity, a deficit1156.
The fixed alternating anchor frame already fails its scalar capacity
test, with7013 permitted edits. These checks were performed by another
agent on h100 and were not rerun in this note.

The full obstruction note was read independently. Its stronger scope
corollary passes: with H1/H2 frozen, preserving every native H3 pair
forces every target of rank at most6 to have a literal H3 witness.
Each rank6 target then needs an unchanged occurrence of its own original
label; each smaller target needs a distinct pinned eligible position.
Any complete cap would therefore saturate the refuted unrestricted
network. Thus the fixed-bank route must change some native rank7 pair
occurrences (and recapture their labels), alter the low-height components,
or change another stated restriction. General short-interval caps are
not ruled out. Nor does this fixed-bank argument cover new witnesses
that might be created across later, independently justified seams.
