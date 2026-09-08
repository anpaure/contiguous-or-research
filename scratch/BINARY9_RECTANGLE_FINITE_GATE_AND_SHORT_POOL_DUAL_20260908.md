# Binary-nine rectangle gate and an exact short-pool obstruction

2026-09-08. Pure analytical deductions except the separately identified
h100 catalogue and bounded local-trade test. The short-pool dual below
has an independent direct-route audit PASS. No bank of charge below 280
is asserted here.
Section 8 also has a full direct-route audit PASS, conditional on the
complete six-source balance inventory. Sections 9–10 finish the stated
fixed-left mixed-sign trade by a complete necessary-source inventory and
literal missing-target certificates, rather than unresolved CP statuses.

## 1. Existing constructions and the finite gate

An axis-support rectangle chooses complementary nonempty coordinate
supports in the binary nine-cube, a nonempty strict chain C on one,
and a nonempty strict chain D on the other. Its designated family is
{c union d : c in C,d in D}; its charge is |C|+|D|. Covers and charges
retain every repeated occurrence. Full complementation is a bonus of
the later word compiler, not an alternative definition of coverage here.

The tube theorem in QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md,
Sections 2–3, already applies to this exact model, including nonsaturated
chains and changing support splits. The more recent
GRID_CHAIN_INFLATION_FOR_ASYMMETRIC_STAIRCASE_20260908.md gives the same
face-routing mechanism. A binary-nine macrobank of charge M inflates to
principal charge M*s^8 on [2s]^9, with lower-order assembly overhead.
Thus M<280 gives a strict equal-nine-axis local improvement on
280*s^8, or normalized local factor M/256<35/32. The outer accumulator
coefficient requires its own applicable length and probability ledger;
the general q-ary theorem's extra-accumulator formula is not silently
substituted for a nine-accumulator terminal rule.
The now-proved STRICT_EQUAL_PROTOTYPE_TO_UNCONDITIONAL_C9_GAIN_20260908.md
supplies precisely that transfer. The exact O(s^7) local overhead is also
checked in BINARY9_WEIGHTED_RECTANGLE_INFLATION_AND_INTEGRAL_GATES_20260908.md,
Section 1, by putting the smaller-dimensional shore on the right in A.24.

The following relevant existing artifacts were inspected:

- MASTER_HANDOFF.md A.7.1 and
  CATALAN_THRESHOLD_EIGHT_COVER_AND_TRANSFER_20260906_c58e2.md give the
  explicit fourteen full 4+4 prefix rows covering the eight-cube.
  The ranks 3,4,5 are each covered exactly once.
- The tube note gives exact finite gates on other alphabets, notably
  [4]^6, but supplies no binary-nine 26-rectangle bank.
- BALANCED_BINARY_FOUR_TUBE_EXACT_BARRIER_20260907.md proves the sharp
  binary-EIGHT independent-tube lower bound 140. It is not a binary-nine
  lower bound 280.
- MATH_CERTIFICATE_CYCLIC_MU9_WIDTH126_20260907.md proves an interval-OR
  CYCLIC word of length126. Its middle-level Hamilton cycle and all-rank
  interval coverage are not a decomposition into 26 axis-support
  rectangles. Such a decomposition needs additional geodesic and
  all-rank coverage conditions.

No explicit 26-rectangle binary-nine bank was found in these sources or
the targeted repository searches. That is a catalogue statement, not a
nonexistence theorem.

## 2. Exact critical-rank arithmetic

Call ranks4 and5 critical. For any rectangle C x D, form a bipartite
graph whose vertices are the members of C and D, and whose edges are
its critical cells. Distinct members of a strict set chain have distinct
ranks. Therefore this graph embeds in the rank graph with edges

    a+b=4 or a+b=5.

The latter is an alternating path: following two successive edges in a
fixed direction changes a by one. In particular every finite subgraph
is a forest of paths. If a rectangle has E critical cells and charge L,

    E <= L-1,                 E <= 10.                 (1)

The first inequality also holds for an empty critical graph because L>=2.
For the second, the smaller coordinate support has at most four axes,
so each of the two ranks has at most five cells. Since L<=11 in the
binary nine-cube, (1) also gives (11/10)E<=L.

A complete bank with t rectangles consequently satisfies

    t>=26,       M>=252+t,       M>=278.                (2)

Thus a strict improvement on 280 can only have M=278 or279, and at
most27 rectangles. At M=278 it has exactly26 rectangles, exactly252
critical occurrences, and each critical graph is a spanning path. At
M=279, a 27-rectangle bank has the same exact critical partition and
spanning-path condition. A 26-rectangle bank allows total critical
overlap plus critical-graph slack at most one. These conditions do not
prove all-rank coverage.

The fractional optimum is 1386/5=277.2. The lower certificate assigns
11/10 to every critical target and zero elsewhere. For attainment,
average all full ordered 4+5 prefix rows with total row weight126/5.
Each row has rank counts (1,2,3,4,5,5,4,3,2,1), so the two critical
ranks have coverage one and every other rank has coverage at least one.
The total charge is11*(126/5). This fractional bank is not an integral
macrobank or a word.

The proposed 26-full-row trimming arithmetic is therefore not immediately
contradictory. Full rows have cost286 and130 occurrences in each critical
rank. Deleting the bottom endpoint of a LONG, five-axis shore removes
one rank4 occurrence; deleting its top endpoint removes one rank5
occurrence. Four deletions of each kind would give cost278 and exact
critical counts126,126, provided actual coverage survives. Seven such
deletions give the cost279 arithmetic with at most one critical duplicate.
Actual target identities and all ranks remain essential.

## 3. The explicit 28-rectangle bank of charge280

Write an old row as left prefixes L_0,...,L_4 and right prefixes
R_0,...,R_4 on complementary four-axis supports. Let z be coordinate8.
Its packet is the full product of this row with {0,z}. It is covered
by either of these two exact chain partitions on the left five axes:

    short z=1:
       long  (L_0,L_1,L_2,L_3,L_4,L_4+z),
       short (L_0+z,L_1+z,L_2+z,L_3+z);

    short z=0:
       long  (L_0,L_0+z,L_1+z,L_2+z,L_3+z,L_4+z),
       short (L_1,L_2,L_3,L_4).

Pair both chains with the complete right chain. The long rectangle
has charge11 and ten critical cells; the short has charge9 and eight.
The two chains partition the 5-by-2 product exactly. Applying this
independently to all fourteen old rows gives28 rectangles, charge280,
and exactly one occurrence of every critical target. Its hook orientation
can be chosen separately for each owner without changing coverage.

## 4. Every short-only pool has an exact charge lower bound

Choose any m distinct old owners, and one short-hook orientation for each.
Let P be the union of their critical targets. It has8m distinct members.
Call a target in P hard if it has z=0 and rank5, or z=1 and rank4.
Each selected short has four hard and four other critical targets.

First, P never contains both B and B+z for an eight-coordinate rank4
set B. The old eight-bit template gives B a unique owner, and this
owner contributes at most one short, whose z value is constant.

Assign weight1 to every target in P and additional weight1/4 to each
hard target; all other nine-bit targets get zero weight. Then

    total target weight = 9m.                         (3)

For an arbitrary axis-support rectangle C x D, keep in its critical
graph only edges belonging to P. This is still a forest of paths.
Adjacent cells in one component share one chain member, while the other
two members have ranks differing by one. Since they are comparable,
their sets differ by exactly one coordinate. If that coordinate were z,
the two targets would be the forbidden pair B,B+z. Hence every component
has constant z.

Within a component with z=0 the hard targets project to rank5 on the
remaining eight coordinates; with z=1 they project to rank3. Any
axis-support chain rectangle on eight coordinates has at most four
targets of rank3 or rank5: for rank3 there are only four possible shore
rank pairs, and rank5 follows by complementation. This applies also to
a subset of such a rectangle, so each component has at most four hard
edges. A component with e edges therefore has weight at most

    e+4/4 = e+1 = its number of vertices.

Different components use disjoint chain members. Summing proves that
the entire target weight captured by C x D is at most |C|+|D|.
This is a genuine nonnegative covering dual. Consequently every
axis-support rectangle bank covering P has charge at least9m.

The original m shorts attain this bound. Thus no short-only trade can
lower the principal charge, for any mixture of hook orientations, any
number or shape of replacement rectangles, and even if replacements
also cover targets outside P. In particular five shorts cannot be
replaced by four full rows. The argument constrains designated Cartesian
products; it does not optimize an alternative ledger that also credits
their full complements as separate macro coverage.

## 5. Next finite trade and complete candidate catalogue

The next targeted trade frees one complete old packet (cost20) and
four other shorts (cost36), replacing them by five full rows (cost55).
It would give a27-rectangle bank of charge279. It must exactly partition
the50 freed critical targets and preserve coverage of every other rank.

Every full4+5 row contains the middle edge flipping z, so it contains
B and B+z for some rank4 base set B. The unique base owner of B must
be the fully freed packet owner i. For all other owners, each critical
target either specifies the one possible short orientation, or is an
endpoint omitted from both short choices and forces a second full owner.
Conflicting orientations within another owner also force that owner full.

The literal h100 catalogue enumerates all9!=362880 full ordered4+5 rows,
fixing z absorption into the displayed LEFT shore of every old row. It
retains rows with one forced full owner and at most four other compatible
short owners. Its exact result is98058 candidates, by full owner0..13:

    7456,6650,7190,7136,6656,6924,6616,
    7225,6868,6762,6944,6747,7349,7535.

The counts needing respectively0,1,2,3,4 short owners are

    140,1227,7635,31485,57571.

The run took1.6211 seconds on arboghast through ssh h100, with two-CPU
affinity,1GiB memory cap and20-second outer timeout. It ran no solver.
The source and durable outputs are:

- catalogue_binary9_one_packet_four_shorts_20260908.py
- BINARY9_ONE_PACKET_FOUR_SHORTS_CATALOGUE_SUMMARY_20260908.json
- BINARY9_ONE_PACKET_FOUR_SHORTS_CATALOGUE_20260908.json

For a fixed full owner i, use a Boolean x for each candidate row, and
y_(j,delta) for choosing owner j!=i and short sign delta. Require

    sum x=5,   sum y=4,   y_(j,0)+y_(j,1)<=1,

and the candidate's implied y values whenever x=1. If L_old(T) is the
literal full14-packet load, impose for EACH of all512 targets T:

    L_old(T) - 1{T in packet_i}
      - sum_(j,delta) y_(j,delta)1{T in short_(j,delta)}
      + sum_R x_R 1{T in R} >= 1.                    (4)

The critical counts force equality there automatically. The subsequent
authorized bounded test uses (4), not just the critical equations. Any
candidate witness must be independently replayed as actual complementary
support chains, with a full512 load census and literal total charge279.
UNKNOWN solver status is not an exclusion of this finite trade.

## 6. Bounded all-target trade test: no witness, twelve owners unresolved

The subsequent authorized model used the unchanged catalogue and all512
constraints (4). It ran sequentially for all fourteen full owners, with
two CP-SAT workers, two-CPU affinity, and a3GiB process memory cap on
h100. The first pass used1.25 seconds of solver allowance per owner and
completed in20.3708 seconds. Owner1 returned INFEASIBLE during presolve;
the other thirteen owners returned UNKNOWN before branching.

A final focused run on owner0, still within the authorized total30-second
computation limit, allowed6.5 solver seconds with a9-second outer timeout.
It completed in2.1116 seconds, returning INFEASIBLE during presolve after
1.2598 solver seconds. Thus the two runs used22.483 seconds altogether.
No witness was found, and no further search was launched.

The final finite statuses are:

- full owners0 and1: CP-SAT INFEASIBLE for the exact stated fixed-left
  packet/four-short model;
- full owners2,...,13: UNKNOWN, so their feasibility remains unresolved.

These are recorded solver outcomes with inspectable source, not an
independent proof-log certificate of global nonexistence. They do not
exclude other absorbed-shore choices, other local trades, or arbitrary
binary-nine banks. In particular the twelve UNKNOWN outcomes must not
be promoted to infeasibility.

The local solver source is solve_binary9_one_packet_four_shorts_20260908.py.
It builds (4) directly from literal target sets. An optional witness path
reconstructs all27 actual rectangles and independently checks their
complementary supports, strict chains, every target load, exact critical
decks, and principal cost279; this path was not reached because no witness
was returned. No unexecuted witness verifier is cited as verification
of a construction.

Durable status files are:

- BINARY9_ONE_PACKET_FOUR_SHORTS_TRADE_20260908.json
- BINARY9_ONE_PACKET_FOUR_SHORTS_TRADE_SUMMARY_20260908.json
- BINARY9_ONE_PACKET_FOUR_SHORTS_OWNER0_20260908.json
- BINARY9_ONE_PACKET_FOUR_SHORTS_OWNER0_SUMMARY_20260908.json

The input catalogue was
/tmp/binary9_one_packet_four_shorts_catalogue_20260908_cover_selectors.json
on h100. The exact two commands, with the local source sent on stdin, were:

    ssh h100 'timeout 30s python3 - /tmp/binary9_one_packet_four_shorts_catalogue_20260908_cover_selectors.json /tmp/binary9_one_packet_four_shorts_trade_20260908_cover_selectors.json' < scratch/solve_binary9_one_packet_four_shorts_20260908.py

    ssh h100 'timeout 9s python3 - /tmp/binary9_one_packet_four_shorts_catalogue_20260908_cover_selectors.json /tmp/binary9_one_packet_four_shorts_owner0_20260908_cover_selectors.json 0 6.5' < scratch/solve_binary9_one_packet_four_shorts_20260908.py

## 7. Uniform-z-one coordinate balance leaves six exact source choices

Section 5 of BINARY9_WEIGHTED_RECTANGLE_INFLATION_AND_INTEGRAL_GATES_20260908.md
proves a necessary coordinate balance when all four removed shorts have
z=1. For full owner i with displayed orders L,R, let

    B_j=prefix_j(L) union prefix_(4-j)(R),   0<=j<=4.

If root j is unmatched in the old packet's middle path and the four other
short owners are k_1,...,k_4, the necessary condition is

    sum_h 1_(right shore of owner k_h) = sum_(t!=j) 1_(B_t).       (5)

This section uses that analytical lemma; it does not infer (5) from
solver behavior. The exact inventory tests all fourteen full owners,
five roots, and715 distinct eligible owner quartets for each owner/root.
It first records the coordinate-sum signatures of the1001 quartets of
all fourteen right-shore masks, then excludes quartets containing i.
Every surviving signature is independently re-summed before export.

Exactly six choices survive (all indices are zero-based):

| Full owner i | Root j | Four removed short owners |
|---:|---:|:---|
|7|2|(5,10,11,12)|
|8|3|(0,3,12,13)|
|8|3|(2,5,11,13)|
|9|3|(3,4,6,10)|
|13|1|(0,7,8,10)|
|13|1|(5,6,8,10)|

Every other owner/root/quartet fails the necessary coordinate equation.
Thus ten full owners are excluded in this uniform-z-one fixed-left
subcase, and the other four reduce to the displayed six source choices.
This is not an exclusion of mixed hook orientations or a proof that any
of these six choices admits replacement rows or all-rank coverage.
No replacement row orders were searched.

The h100 inventory took0.004714 seconds, with two-CPU affinity,1GiB cap,
and a3-second outer timeout. The exact command was

    ssh h100 'timeout 3s python3 - /tmp/binary9_uniform_short_coordinate_balance_20260908_cover_selectors.json' < scratch/inventory_binary9_uniform_short_coordinate_balance_20260908.py

The durable source is inventory_binary9_uniform_short_coordinate_balance_20260908.py.
The complete70-case report, literal middle paths, target coordinate counts,
and survivor lists are in BINARY9_UNIFORM_SHORT_COORDINATE_BALANCE_20260908.json;
the compact count table is in
BINARY9_UNIFORM_SHORT_COORDINATE_BALANCE_SUMMARY_20260908.json.

## 8. Missing complements exclude all six uniform sources

The following complementary-endpoint filter was independently derived
by direct_route; cover_selectors supplied the literal finite replay.
Together with Section 7 it excludes the entire fixed-left, uniformly-z-one
one-packet/four-short to five-full-row trade. No new CP-SAT model was needed.

The freed no-z critical deck consists of five rank4 targets and four
rank5 targets, all from the one full packet. If z is at position p of
the five-axis shore of a full row, that row has p no-z rank4 cells and
p-1 no-z rank5 cells. If z is at position p of its four-axis shore,
the corresponding counts are p,p. Exact critical coverage by five new
full rows therefore forces exactly one row with z on its five-axis
shore, and forces p=1 in every row.

The four no-z rank5 targets U of the old packet must consequently be
the complete five-axis shores of the four new rows having z on their
four-axis shore. A full prefix rectangle contains BOTH complete shore
sets, by taking the other prefix empty. It therefore contains the
rank4 target

    E9 minus U = {z} union (E8 minus U).                (6)

Since all50 new critical cells must partition exactly the50 freed ones,
each complement (6) must belong to the freed source. For a uniform-z-one
short, every projected rank3 target belonging to its old owner is present:
its left prefix has length at most3, so the omitted length4 endpoint
does not affect rank3. The base template owns every rank3 target exactly
once. Thus the quartet must contain the old owner of E8 minus U, unless
that owner is the freed full packet itself; the latter never happens
for the four U of a full4+4 packet.

One missing complement suffices in each of the four surviving owner cases:

| Full owner | Required no-z U mask | E8 minus U | Required E9 complement | Absent old owner |
|---:|---:|:---:|---:|---:|
|7|220|{0,1,5}, mask35|291|4|
|8|186|{0,2,6}, mask69|325|1|
|9|62|{0,6,7}, mask193|449|2|
|13|171|{2,4,6}, mask84|340|4|

Each absent owner is missing from every quartet listed for its full owner
in Section 7. The owner identities are also directly visible in the
literal base rows: {0,1,5} is the first three left coordinates of owner4;
{0,2,6} is the first left coordinate plus the first two right coordinates
of owner1; {0,6,7} is the first three left coordinates of owner2; and
{2,4,6} is the first three right coordinates of owner4. Exact rank3
ownership makes these identities unique. Hence all six remaining sources
contradict the mandatory complementary endpoint (6).

The independent availability replay rebuilt every packet and short from
the literal base rows, compared them with the existing catalogue, formed
each50-target critical source, and checked all four U complements and
the root complement. It returned no surviving source. The four failures
in the table already suffice; the additional failures are saved in the
JSON but are not needed for the proof.

This h100 run took0.232729 seconds, including reading the existing
catalogue, with two-CPU affinity,1GiB cap and3-second outer timeout.
It used no solver and did not search row orders, mixed signs, or deeper
banks. The source is verify_binary9_six_uniform_sources_complements_20260908.py;
the literal certificate is
BINARY9_SIX_UNIFORM_SOURCES_COMPLEMENT_CERTIFICATE_20260908.json.

The exact command was

    ssh h100 'timeout 3s python3 - /tmp/binary9_one_packet_four_shorts_catalogue_20260908_cover_selectors.json /tmp/binary9_uniform_short_coordinate_balance_20260908_cover_selectors.json /tmp/binary9_six_uniform_sources_complements_20260908_cover_selectors.json' < scratch/verify_binary9_six_uniform_sources_complements_20260908.py

The conclusion is specific to the stated fixed-left, uniformly-z-one
trade. It is not a lower bound280 for arbitrary binary-nine rectangle
banks and does not replace the UNKNOWN statuses for the earlier mixed-sign
models by infeasibility.

## 9. Complete mixed-sign endpoint and anchor inventory

The support, endpoint, and anchor identities in Sections 6–7 of
BINARY9_WEIGHTED_RECTANGLE_INFLATION_AND_INTEGRAL_GATES_20260908.md
were independently audited by cover_selectors. They permit a small
necessary-condition inventory without enumerating new row orders.

Each owner supplies four rank5 targets U, with a directed edge to the
owner of E8 minus U. The resulting56-edge graph has indegree and
outdegree four and no loops. For a source consisting of packet o plus
four selected shorts, let S_0 contain o and zero-short owners, and S_1
contain o and one-short owners. The four new longer supports avoiding z
must be distinct edges U from S_0 to S_1. Their selection forces the
fifth longer support z+T by

    1_T = 1_E8 + sum_selected 1_J - sum_four 1_U.        (7)

The right side must be a zero-one vector; both z+T and E8 minus T must
be present in the literal critical source. The five old packet rank4
sets are the only possible vertical anchors. Assigning the five longer
supports to them forces each z-position: 5-|B intersect U| for a no-z
long support U, and1+|B intersect T| for z+T. Their sum must be5+4n_0.

The h100 inventory checked ALL160160 source choices: fourteen packet
owners,715 eligible quartets each, and16 short-sign vectors. Every owner
and source finished. Exactly25 sources pass some endpoint and incidence
certificate, and24 pass some anchor assignment. Their counts by owner
0 through13 are

    1,2,0,0,1,9,6,1,1,0,1,1,0,1.

Thus owners2,3,9,12 are excluded already by the necessary endpoint
structure. Neither uniform sign survives this complete inventory.
The source writes ONE witness per surviving source, stopping witness
enumeration after that success. It does not assert a unique longer-support
choice or anchor assignment. Its support_selections_passing_endpoints
field counts examined certificates, not all possible certificates of
a surviving source. The source-choice counts are nevertheless complete.

The run took0.480861 seconds on h100, with two-CPU affinity,1GiB cap,
and15-second outer timeout. The source is
inventory_binary9_mixed_endpoint_anchors_20260908.py. Durable output:

- BINARY9_MIXED_ENDPOINT_ANCHOR_INVENTORY_20260908.json
- BINARY9_MIXED_ENDPOINT_ANCHOR_SUMMARY_20260908.json

Direct-route independently read the full inventory source and JSON and
passed its exhaustive-source and one-witness scope. No row-order solver
was used in this step.

## 10. Every surviving fixed-left source has an unavailable critical target

The subsequent exact completion used the ENTIRE previously complete
98058-row catalogue, filtered only by full owner and the four fixed
short-owner/sign requirements. In particular it did NOT restrict any
source to the one example support selection or anchor assignment saved
by Section 9. Every retained candidate was expanded literally into all30
prefix targets. Its ten critical targets had to lie in the50-target
freed source. The model also retained every noncritical target whose
old coverage would vanish after the removal.

All24 sources fail before any branching: the union of ALL their compatible
new full rows misses a required critical target. The table gives the
complete source list, candidate count N, and one missing target mask.
Signs record the constant z value of the short, in quartet order.

| ID | Packet | Four short owners | Signs | N | Missing mask |
|---:|---:|:---|:---:|---:|---:|
|0|0|(4,8,10,11)|0110|76|29|
|1|1|(3,5,8,13)|0100|43|27|
|2|1|(3,5,10,13)|0100|44|27|
|3|4|(0,1,8,13)|1101|58|77|
|4|5|(0,9,10,13)|0110|42|116|
|5|5|(1,2,7,10)|1100|27|39|
|6|5|(1,7,10,13)|0110|51|153|
|7|5|(1,9,10,13)|0100|53|153|
|8|5|(1,9,10,13)|0110|51|153|
|9|5|(2,7,10,12)|1001|59|39|
|10|5|(2,7,10,13)|0110|55|116|
|11|5|(4,7,10,12)|1001|37|39|
|12|5|(6,9,10,13)|1100|33|61|
|13|6|(0,4,8,13)|1000|49|141|
|14|6|(0,4,9,13)|1000|104|163|
|15|6|(1,4,8,13)|1001|68|141|
|16|6|(1,4,9,13)|0001|86|85|
|17|6|(1,4,9,13)|1001|86|163|
|18|6|(2,4,9,13)|1001|98|163|
|19|7|(2,4,9,13)|1100|71|15|
|20|8|(3,4,9,11)|1100|37|30|
|21|10|(1,2,7,8)|1100|47|39|
|22|11|(3,4,6,9)|1010|27|15|
|23|13|(2,5,9,10)|1100|47|15|

Why the compatible catalogue is complete: each full new row contains a
vertical pair, whose unique base owner must be the fully freed packet.
Every other owner touched by its critical deck must supply those cells
in its one selected short. These are exactly the catalogue's filters.
Five full rows have50 critical occurrences, so a complete replacement
must use them only inside the50 missing critical targets, with no
duplicates. Thus a listed target absent from every compatible row rules
out the whole replacement, regardless of other-rank coverage.

The checker exported the complete compatible row-order list and a one-node
unavailable-target proof for each source. A separate proof-replay routine
checked the required target was missing initially and absent from every
available row; all24 replays passed. Although an exact-cover DFS was
implemented, every case finished at its initial availability test and no
branch was entered. This avoids relying on an opaque infeasibility status.

The run completed all24 cases in0.337683 seconds on h100, with two-CPU
affinity,1GiB cap and15-second outer timeout. Source:
complete_binary9_24_fixed_left_sources_20260908.py. Durable files:

- BINARY9_24_FIXED_LEFT_COMPLETIONS_20260908.json
- BINARY9_24_FIXED_LEFT_COMPLETION_SUMMARY_20260908.json

Combining Sections 9 and10 excludes the entire fixed-left one-packet plus
four shorts to five full4+5 rows trade, for all hook signs. The twelve
earlier UNKNOWN model statuses are superseded for THIS exact trade by
the complete necessary-source reduction and explicit missing-target
certificates. This does not exclude flexible absorbed shores, other
trades, truncated new rectangles, or arbitrary binary-nine banks.

## 11. Flexible absorbed shores with uniform z-one shorts are also excluded

This is a distinct variation: each of the four selected old owners may
absorb z into EITHER of its displayed four-axis shores. All four selected
shorts still have constant z=1. Its source families are not limited to
the fixed-left catalogue, so that catalogue was not used for completion.

The quartet must contain every owner of an eight-coordinate complement
of one of the packet's four no-z rank5 targets U. This condition is
independent of the absorbed shore: either one-hook short contains all
four base rank3 targets of its owner. For each eligible quartet the
inventory checked all16 choices of absorbed shore and the exact coordinate
balance (5). The coordinate sum determines at most one packet root.
The complementary root endpoint must also be present in the literal
critical source. These necessary tests were all exhaustive.

Exactly three sources survive. L or R below specifies the DISPLAYED
shore that absorbs z in each quartet owner, in quartet order:

| ID | Packet | Root | Short owners | Absorbed shores |
|---:|---:|---:|:---|:---:|
|0|2|1|(5,7,8,13)|RLRL|
|1|11|1|(0,3,7,8)|RLLR|
|2|11|2|(0,3,8,9)|RLRL|

For each source the new no-z path matching is forced away from its root.
For each of four path edges U, write B for its matched child anchor.
The new short-shore order is z followed by any order of E8 minus U;
the long-shore order is any order of B followed by the single element
of U minus B. This gives exactly3!*4!=144 rows per edge. The root row
has the two orders: any order of B_root, and z followed by any order
of E8 minus B_root. It gives exactly4!*4!=576 rows. These exhaust all
five-row possibilities for the forced matching; no9! enumeration is used.

All1152 orders were generated for EACH of the three sources. After
requiring every critical cell of a row to lie inside the50-target source,
the retained row counts in the four edge groups and root group were:

| Source ID | Five group counts | Critical target absent from their entire union |
|---:|:---:|---:|
|0|(5,6,2,2,16)|269|
|1|(4,4,2,4,9)|294|
|2|(1,2,2,2,10)|312|

Thus every source fails at initial critical-target availability. All three
one-node absence certificates were independently replayed; no DFS branch
was entered. The missing masks are z+13, z+38, and z+56, respectively,
and have rank four. The source reconstruction and optional literal witness
replay swap the displayed old shores whenever R absorbs z; the full old
packet itself stays unchanged. All512 final target requirements were
formed, although the critical failures already settle the cases.

The necessary-condition inventory took0.006113 seconds on h100 and the
complete order/coverage check took0.033566 seconds. Each had two-CPU
affinity and1GiB cap; the combined mathematical runtime is below the
authorized15-second total. No fixed-left row filter, mixed-sign extension,
or deeper trade was used.

Sources and durable data:

- inventory_binary9_flexible_uniform_shores_20260908.py
- BINARY9_FLEXIBLE_UNIFORM_SHORES_INVENTORY_20260908.json
- BINARY9_FLEXIBLE_UNIFORM_SHORES_SUMMARY_20260908.json
- complete_binary9_flexible_uniform_sources_20260908.py
- BINARY9_FLEXIBLE_UNIFORM_COMPLETIONS_20260908.json
- BINARY9_FLEXIBLE_UNIFORM_COMPLETION_SUMMARY_20260908.json

This excludes the one-packet plus four uniform-z-one shorts to five full
rows trade even with flexible absorbed shores. It does not exclude mixed
signs with flexible shores, or the uniform-zero case in the unchanged
literal bank: global complementation also reverses the old prefix orders,
so identifying these cases requires a separate symmetry argument.

## 12. General pure-charge trades and five-whole-packet availability

From five distinct old owners, free p whole packets and5-p shorts.
The source has

    18p+8(5-p)=10(p+4) critical targets,
    20p+9(5-p)=11p+45 charge.                         (8)

Replacing it by p+4 full4+5 rows would cost11p+44, a saving of one.
The critical deck must be exact. Taking rank5-minus-rank4 coordinate
incidence gives

    sum_new 1_(longer support) = p*1_E + sum_old shorts 1_J.

Exactly p of the new rows therefore have z on their five-axis shore,
and exactly four have it on their four-axis shore. If n_0 old shorts
have z=0, the sum of new z-positions is5p+4n_0. These conditions are
consistent at p=5: five z-long rows, four z-short rows, position sum25,
and coordinate incidence sum5*1_E.

For p=5 the source is five complete packets, with90 critical targets;
nine full rows would replace their old ten rectangles and lower charge
100 to99. There are2002 choices of five packet owners. Unlike the
one-packet case, the source has25 vertical pairs while the replacement
has only nine rows, so a bijection to every old anchor is unavailable.

A fresh complete9! row inventory assigned each full row the set of
old owners of its ten critical targets. It did not reuse the incomplete
fixed-left one-packet catalogue. For each exact owner mask it accumulated
the union of all its row targets, then a Boolean OR-zeta transform on
fourteen owners computed the union of ALL full rows supported inside
every owner set. Each five-owner set was compared with its90 required
critical targets. All2002 sets passed availability.

This has a direct constructive explanation and supplies no new source
restriction. For ANY individual packet, insert z first or last into
one of its old four-axis orders, retaining the other complete order.
The first full row covers all z-present packet cells; the second covers
all z-absent packet cells. Their union therefore covers the entire
packet. They cost22 instead of the old packet cost20. Consequently
unrestricted union availability automatically passes for every union
of whole packets, even though choosing only nine full rows remains an
unresolved integral restriction for five packets.

The row inventory was complete and took1.270717 seconds on h100, with
two-CPU affinity,1GiB cap and5-second outer timeout. Counts of full rows
by exact number of old owners touched, for sizes1 through9, were

    140,1731,14476,68820,134916,103652,34115,4813,217.

No row touches ten or more owners. All362880 ordered full4+5 rows were
processed, followed by all2002 sources. The exact owner-mask unions,
counts, representative orders and every source's availability result
are saved. No nine-row exact-cover or further selection search ran.

Sources and data:

- inventory_binary9_five_packet_availability_20260908.py
- BINARY9_FIVE_PACKET_AVAILABILITY_INVENTORY_20260908.json
- BINARY9_FIVE_PACKET_AVAILABILITY_SUMMARY_20260908.json

The remaining p=5 gate is to select nine rows whose90 critical targets
partition the source and whose other targets preserve full-cube coverage.
The availability pass neither solves nor excludes it.
