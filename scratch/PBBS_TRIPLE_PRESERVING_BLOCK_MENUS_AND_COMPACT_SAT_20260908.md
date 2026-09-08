# Triple-preserving cap blocks: exact menus and a compact complete Boolean encoding

2026-09-08. Pure-proof note by `exact_equality_structure`. No mathematical
code or SAT solver was run for this note.

The local menu and encoding below are exact. The particular canonical
anchor frame to which they were first applied has now been disproved by
finite forced-support propagation: see Section 8. Consequently no SAT
script or run is needed for that frame. The formulation remains usable
for a separately justified changed frame or source. It does not produce
a complete capped bank or a length-B(17) linear word.

The source identities are from
[the capped-aperture interface](PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md)
and [the exact cap criterion](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md),
especially Sections 1, 5, and 6 of the latter. The actual canonical data
and counts are from
[the executed triple-preserving catalogue](K17_TRIPLE_PRESERVING_SHORT_HOSTS_AND_CANONICAL_ANCHOR_MENU_CERTIFICATE_20260908.md).
These sources were read for this proof. Numerical census and propagation
claims below are attributed to those certificates, not to a new run.

## 1. Fixed hypotheses and simultaneous preservation

Use the k=17 capped PBBS bank with H=min(height,3), on its original
cyclic owner chronology. Freeze all H=1 and H=2 components. On an H=3
component write

    D_i = X_i intersect X_(i+1) intersect X_(i+2) intersect X_(i+3),
    P_i = (X_i minus X_(i-1)) union (X_(i+3) minus X_(i+4)).

The retained source lemmas give:

* each D_i has rank six;
* each adjacent pair union has rank seven;
* each three-letter union has rank eight;
* each four-letter union is its prescribed rank-nine owner;
* P_i is the nonempty set of source-coordinate run endpoints at i.

The source-run criterion for preserving every native triple is exactly
to retain those endpoints and to leave distance at most three between
consecutive retained occurrences of every coordinate. Permanent
coordinates have the analogous cyclic gap condition. The finite
catalogue also recomputed the triple-window exclusion deficits and
verified that their union is this same P_i at every H=3 position.

Choose full anchor positions whose successive cyclic distances are at
most three. Thus every cyclic interval of three positions contains an
anchor, and the nonempty editable blocks between anchors have length
one or two. At every editable position allow exactly

    P_i subset E_i subset D_i.                              (1.1)

Every simultaneous choice in (1.1) preserves every native triple.
Indeed a deleted block of three consecutive occurrences inside a
coordinate's source run would contain a full anchor. Source-run
endpoints are retained by P_i, so the exact gap criterion applies.
This argument includes the cyclic cut and does not suppose that only
one block is edited.

Every longer native window is a union of consecutive native triples,
so all of its ORs are preserved as well. In particular all middle
owners and the original upper deck survive. The frozen components
remain unchanged. The problem left to the cap choices is exactly the
named lower palette, not an additional upper or middle preservation
condition.

## 2. Boundary pairs are fixed; all variable lower witnesses are local

An adjacent source pair has two private coordinates: if

    D_i = K union {a},   D_(i+1) = K union {b},

then |K|=5 and a,b are distinct and outside K. A coordinate of
D_i minus D_(i+1) is at the last position of its source run, hence
belongs to P_i. Similarly D_i minus D_(i-1) belongs to P_i.
Consequently

    E_i union D_(i+1) = D_i union D_(i+1),
    D_(i-1) union E_i = D_(i-1) union D_i                 (2.1)

whenever the neighbor is a full anchor. All anchor-touching pairs
therefore remain their original rank-seven labels.

Let O be the fixed lower palette consisting of:

1. targets covered on the frozen H<=2 components;
2. full anchor letters;
3. pairs touching an anchor.

The only additional targets of rank at most seven are the literal
letters in editable blocks and the internal pair of a two-position
block. This list is exhaustive. A window of length at least three
contains a preserved rank-eight triple. A pair not internal to an
editable block touches an anchor and is already in O. No variable
lower witness crossing two blocks has been omitted.

This exhaustiveness is a statement about the separate cyclic bank.
An eventual surgery or join can create new cross-component witnesses;
such changes are not part of this fixed-frame decision.

## 3. Exact two-position menus and forced rank-seven unions

For one two-position block write its original letters and pins as

    D = K union {a},   F = K union {b},   |K|=5,
    P = {a} union P_0, Q = {b} union Q_0,
    P_0,Q_0 subset K.

The private coordinates a and b are pinned by the run-endpoint
argument in Section 2. In this bank each P_0,Q_0 has size at most one.
Every legal option is therefore exactly

    E={a} union U,   G={b} union V,
    P_0 subset U subset K,   Q_0 subset V subset K.        (3.1)

Its three output channels are E, G, and E union G. They are always
distinct: E contains a and omits b, G contains b and omits a, while
their union contains both. A named target has at most one possible
channel in this block.

The exact individual channel tests are

    left S:  P subset S subset D,
    right S: Q subset S subset F,
    pair S:  P union Q subset S subset D union F.         (3.2)

The pair test is sufficient by the literal realization
E=D intersect S, G=F intersect S. These tests concern one output at
a time; the simultaneous menu still obeys E union G=S.

For a prescribed pair output S, put T=S minus {a,b}. If (3.2) holds,
the exact number of cap pairs giving that union is

    2^|P_0 symmetric_difference Q_0|
       * 3^|T minus (P_0 union Q_0)|.                    (3.3)

Proof: each coordinate pinned on both sides has one state; one pinned
on exactly one side has two states; an unpinned coordinate of T has
three states (left only, right only, both); coordinates outside T must
be absent on both sides. These choices are independent coordinatewise.

In particular a rank-seven internal output must equal the original
pair label D union F. Requiring that label is equivalent to

    for every x in K:  [x in E] OR [x in G].             (3.4)

Pins simplify these positive clauses. The requirement permits many
proper literal caps; it does not force either whole letter to stay
full. However the pair channel can no longer supply any smaller
target. This is the exact local cost of forcing a missing rank-seven
label to its unique provider block.

For simultaneous left target A and pair target S, the full criterion
is the respective tests in (3.2) plus A subset S; choose
E=A, G=F intersect S. For three prescribed outputs A,B,S, the extra
condition is exactly A union B=S. These companion rules and the
actual canonical nonmatroid example are independently proved in
[the two-letter compatibility note](PBBS_TWO_LETTER_MENU_COMPATIBILITY_AND_NONMATROID_OBSTRUCTION_20260908.md).

## 4. Exact global configuration-cover problem

Let T be the set of all nonempty rank<=7 targets outside O. For each
editable block b let M_b be its complete one- or two-letter menu and
let out(m) be its one or three output labels. The cap construction
exists exactly when

    choose one m_b in M_b for every b,
    T subset union_b out(m_b).                           (4.1)

Necessity follows from the exhaustive witness list in Section 2.
Sufficiency follows because Section 1 supplies simultaneous triple
and longer-window preservation for every menu combination, while
(4.1) supplies precisely the missing lower targets. There is no
unpaid compatibility condition between distinct anchor-separated
blocks. Nor does this equivalence pay for opening or fusing the
separate cyclic components into one linear word.

The formulation is an exact finite choice problem. It is not an
ordinary target-to-position or target-to-channel flow. Inside a
two-position block the third output is the union of the first two,
so three individually feasible channel requirements can conflict.
The cited compatibility note gives a concrete counterexample in
positions 1,2 of the actual canonical frame, and shows that the local
feasible-demand family is not a matroid.

## 5. A compact complete CNF without Cartesian option variables

The following encoding is equisatisfiable with (4.1). It uses the
coordinate structure of the caps rather than one Boolean for every
Cartesian block option.

For every editable position i and x in D_i minus P_i introduce a
Boolean e_(i,x). Let the expression e_(i,x) be constant 1 for x in
P_i and constant 0 for x outside D_i. Its truth values specify the
literal cap E_i exactly. No nonemptiness clause is needed because
P_i is nonempty.

For each unfixed target S and each eligible channel c from (3.2),
introduce a witness selector q_(S,c). Eligibility is exact and can
be enumerated directly as a Boolean interval of masks. Add the
following forward implications.

For a literal channel at i:

    q_(S,i) implies e_(i,x)=1 for x in S,
    q_(S,i) implies e_(i,x)=0 for x in D_i minus S.       (5.1)

The first family is the clauses (-q OR e); the second is (-q OR -e).
Simplify constants in the ordinary way.

For the internal pair channel (i,j):

    q_(S,ij) implies (e_(i,x) OR e_(j,x))  for x in S,
    q_(S,ij) implies e_(i,x)=0             for x in D_i minus S,
    q_(S,ij) implies e_(j,x)=0             for x in D_j minus S.
                                                               (5.2)

The positive clauses are (-q OR e_i OR e_j). Again constants are
simplified. Coordinates outside D_i union D_j need no clause.

Finally require a witness for each unfixed target:

    OR_(eligible channels c for S) q_(S,c),  for every S in T.
                                                               (5.3)

An empty eligible list produces the empty clause.

No reverse implication from a true output equality to q is needed.
No at-most-one clause for the selectors of one channel is needed:
if two different targets selected the same channel, their distinct
output equalities in (5.1) or (5.2) would already be incompatible.
Selectors at different channels may witness a repeated target,
which is harmless for coverage.

Proof of equivalence: a satisfying assignment specifies legal caps.
Each true selector certifies literal equality to its target through
(5.1) or (5.2), and (5.3) covers every member of T. Section 4 then
gives the full bank. Conversely, a complete menu selection gives the
cap bits; for each S choose one actual witnessing channel and set
its selector true, leaving the others false. All clauses hold.

Thus the CNF retains the complete joint dependence of E, G, E union G
and avoids the invalid independent-channel relaxation. It is also
complete for the exact specified anchor frame: it neither fixes an
unrequested output nor silently admits a cap outside the menu.

## 6. Size and useful deterministic simplifications

The executed canonical catalogue has 14,720 editable positions:
13,011 with four optional coordinates and 1,709 with five. Thus the
cap layer has exactly

    4*13,011 + 5*1,709 = 60,589 Boolean variables.

It has 7,343 internal pair channels. A literal contributes at most
32 eligible targets, while a pair contributes at most 32: its source
union has seven coordinates and its two private coordinates are
mandatory. More precisely the number of eligible literal incidences
before removing fixed targets is

    16*13,011 + 32*1,709 = 262,864.

Hence the selector count is at most

    262,864 + 32*7,343 = 497,840.                         (6.1)

This upper bound uses only the stored per-position census and the
proved pair interval; it is not a fresh selector census. There are
20,282 coverage clauses in the canonical frame. Each literal selector
requires at most five nontrivial cap-bit clauses. Each pair selector
requires at most ten: only the five shared coordinates can vary,
and each costs at most two clauses. Constants often remove more.
There is no need to materialize the 2,346,272 Cartesian options to
form these clauses.

If a target has exactly one eligible channel, (5.3) is a unit clause.
For a unique-provider rank-seven target it enforces precisely (3.4).
One can also propagate exact per-block requirements using the local
compatibility tests before generating a CNF. These are deductions,
not choices of a heuristic subdomain: every complete selection must
obey them.

Removing a target already in O is valid because its permanent witness
survives every assignment. More aggressive removal would need its
own proof. In particular merely being individually possible in some
other block does not make a target redundant.

## 7. What a decision certificate would establish

For a different explicitly fixed frame, a SAT model can be decoded
directly into physical nonempty caps. Independently replaying its
clauses, original-subset/pin conditions, anchor positions, preserved
triple windows, and required lower witnesses certifies a complete
cyclic bank. It still would not certify a linear length-B(17) word
without a legal additional splice.

A solver's unverified UNSAT response is not itself the intended
mathematical certificate. A separately checked proof or an exact
implication trace terminating in contradiction is sufficient. A
resource-limited unanswered run would be inconclusive. In the
canonical case the next section already provides the latter exact
trace, so no solver was prepared or run for this note.

## 8. The canonical frame is now refuted by exact propagation

The separately executed certificate
[anchor_support_propagation_certificate.json](k17_anchor_propagation_20260908/anchor_support_propagation_certificate.json)
uses the same menu SHA-256

    bf55d2ef90e32f7eac6148e1e889d87a4a0214e651adb62df543c2e7af04c642.

It first applies all 4,441 unique-provider rank-seven requirements.
It then obtains eight further forced (target mask, block) pairs:

    (63,2), (95,37), (119,32), (125,27),
    (126,2), (175,106), (183,168), (55,425).

After the last restriction, required target mask 2103 has no surviving
provider. The propagation logic is exact: if a target has just one
provider block in the current domains, every complete selection must
choose an option of that block containing it. Intersecting the block
domain with this requirement therefore preserves every potential
solution. A target with no provider is a contradiction.

The [producer and replay script](propagate_k17_canonical_w3_anchor_menus_20260908.py)
independently regenerates each domain from the original menus and
accumulated required targets, verifies every claimed sole provider,
and verifies the final absence. It also independently reconstructs
all 14,720 position menus from source D_i and pins P_i. The saved
report records a successful independent trace/domain replay in about
2.93 seconds on h100, under 120 CPU seconds, 150 wall seconds, and
2 GiB address space. This note read the producer/replay code and
certificate; it did not rerun them.

Therefore the exact canonical anchor choice 0,3,6,... on these original
cycles cannot cover every lower target, even though every target has
an individual host. This excludes (4.1) and its equivalent CNF for
that frame. It does not exclude changed anchors, changed source
chronology, non-anchor cap patterns, or later surgery creating new
lower witnesses. No such extension is asserted to work here.

The new reusable result is the exact coordinatewise menu and complete
compact encoding. The finite canonical feasibility question has
already received a negative answer, so the next construction must
change an actual constraint of that frame rather than search its
remaining nonexistent solutions.
