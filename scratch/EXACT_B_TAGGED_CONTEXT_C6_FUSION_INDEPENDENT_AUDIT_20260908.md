# Independent audit: tagged common contexts preserve the full old cyclic deck

Date: 2026-09-08. Reviewer: Codex subagent exact_equality_structure.

Verdict: the root's proposed tagged-context strengthening is valid. The
OR occurrence multiset is preserved at every old width. Tagging also
removes the previous long-identical-context obstruction to middle-owner
uniqueness. A concrete rank-nine, depth-three, 33-owner example is given
below. No canonical PBBS fit or full-cube attaining construction is claimed.

This audit is purely combinatorial; no program was executed.

Final primary-record check: read
`EXACT_B_TAGGED_CONTEXT_FUSION_20260908.md` in full after it was written.
Its general-p per-width proof, complete hub-arc support identity, exact
new-target count, 33-owner rank-nine example, and construction boundaries
agree with the independent derivations below. No material issue was found.

## 1. Statement audited

Let C,D be base words using coordinates disjoint from c,a_0,a_1,a_2.
Read subscripts modulo three, and form the entrywise tagged copies

\[
C_i=(C_t\cup\{a_i\})_t,\qquad
D_i=(D_t\cup\{a_i\})_t.
\]

Set L_i={c,a_i}, R_i={a_(i-1),a_i}, and N=|C|+|D|+2. The three old
cyclic source words are

\[
W_i=(L_i,C_i,R_{i+1},D_i).
\]

The successor rethread produces one cyclic word

\[
V=(L_0,C_0,R_0,D_2,L_2,C_2,R_2,D_1,L_1,C_1,R_1,D_0).
\]

For every 1<=w<=N, its width-w OR multiset equals the disjoint multiset
union of the three old width-w rows. No source occurrence is added or
removed. Either base word may be empty, provided the final source-letter
convention is respected; the added tags make even an empty base set at a
context position into a nonempty source letter.

## 2. Complete interval check

Screen gaps alternate between |C|+1 and |D|+1. An interval of width at
most N contains at most two screen occurrences. In every case below,
retain its exact offsets within the two base contexts.

**No screen.** It lies in a particular C_i or D_i copy. That same tagged
copy occurs once in the new word, so copy the interval literally.

**One L_i screen.** Its neighboring contexts are D_i and C_i in both
words. Thus suffix(D_i),L_i,prefix(C_i) is literal in both.

**One R_(i+1) screen.** The old neighborhood is

    suffix(C_i), R_(i+1), prefix(D_i),

whereas the new one is

    suffix(C_(i+1)), R_(i+1), prefix(D_i).

The base portions are identical, and the only possible change is the tag
a_i versus a_(i+1) in the left fringe. Both coordinates are already in
R_(i+1). The OR is therefore unchanged, including when either fringe is
empty.

**Two screens, R-to-L orientation.** The old interval has form

    suffix(C_i), R_(i+1), D_i, L_i, prefix(C_i).

The corresponding new interval is

    suffix(C_(i+1)), R_(i+1), D_i, L_i, prefix(C_i).

Only the left fringe changes its tag, and that change is absorbed by the
R screen exactly as above. The arc is not wholly literal after tagging;
it is OR-preserving.

**Two screens, L-to-R orientation.** Map

    suffix(D_i), L_i, C_i, R_(i+1), prefix(D_i)

to

    suffix(D_(i+1)), L_(i+1), C_(i+1), R_(i+1), prefix(D_i).

The union of the two old screens and of the two new screens is in both
cases {c,a_i,a_(i+1)}. Every changed context tag lies in this common set.
The base portions and offsets are identical. Thus the OR is equal.

Each matching is bijective within its interval type. The five types are
disjoint and exhaustive, proving exact multiset equality at every w<=N.

## 3. Longer intervals

Let B be the union of all base letters and put

    Omega=B union {c,a_0,a_1,a_2}.

Every new interval longer than N contains every base position type, since
the base background and screen positions repeat with spacing N. Its base
union is therefore B. It contains at least two consecutive screens.

The union of two consecutive screens contains c and two of the three a
labels. A longer consecutive screen block has either those same labels or
all four active labels. Tags in the context fringes do not introduce a
fourth label unless a neighboring screen block already reaches that label:
for an L_i,R_i arc the fringe tags are a_i,a_(i-1); for an R_i,L_(i-1)
arc they are again a_i,a_(i-1). These are already in the respective screen
unions. The same remains true for the three-screen L_i,R_i,L_(i-1) block;
any other larger block already contains all active labels.

Consequently a long interval's value is either Omega or
B union {c,a_i,a_(i+1)} for some i. The latter is the full-period union
of old cycle W_i. Thus

    Deck(V)=Deck(W_0) union Deck(W_1) union Deck(W_2) union {Omega}.

The full-period interval of V supplies Omega, and the per-width bijection
supplies every old target, so this is equality of supports.

## 4. Why the earlier owner-uniqueness obstruction does not apply

The identical-context lemma forced |C|,|D|<=d for a globally unique
rank-r owner row, because a width-(d+1) interval lying entirely in C or D
had the same label in all three ports. Here the corresponding intervals
have different permanent tags a_i, so that proof fails for a valid reason.
Middle-owner uniqueness is in fact possible with N>2d+2, as the following
explicit example shows.

Take d=3 and owner rank r=9. Use exactly 17 coordinates:

* a common four-set K;
* nine distinct coordinates x_1,...,x_9 disjoint from K; and
* the four active coordinates c,a_0,a_1,a_2.

Let

    C=(K+x_1,...,K+x_5),
    D=(K+x_6,...,K+x_9),

and use the tagged construction above. Each old source cycle has N=11
positions, exceeding 2d+2=8.

Every source position contains its port's permanent tag a_i. Apart from
that tag and K, the eleven positions supply eleven distinct symbols in
cyclic order:

    c, x_1,...,x_5, a_(i+1), x_6,...,x_9.

Every window of four source positions contains at least one context
position, so it contains K. In fact, the screen gaps are six and five,
so it contains at most one screen. Its union is exactly K, the permanent
tag a_i, and the four distinct positional symbols it meets. It therefore
has rank 4+1+4=9.

Different starts within a port give different proper cyclic four-subsets
of eleven distinct symbols. Across ports, the active part is one of
{a_i}, {c,a_i}, or {a_i,a_(i+1)}. These possibilities identify the port,
so no two ports share an owner. The old bank thus consists of exactly 33
distinct rank-nine owners. The per-width theorem at w=4 transfers precisely
that owner multiset to V, giving a single 33-owner cyclic chronology with
no repeated owner.

This is a literal finite module. It does not cover the entire rank-nine
layer or Boolean cube. Its permanent port tags also exclude identifying
the old cycles with canonical PBBS components, whose coordinate homomesy
does not permit one coordinate to be permanently present. No PBBS
51-cycle or 17-cycle fusion is asserted.

## 5. Boundaries retained

The full old components must have exactly the tagged-context form. The
proof does not apply to unrelated exterior bodies appended to the ports.
Its output does not automatically regenerate three components of the same
form. It also does not protect arbitrary long cyclic witnesses after a
final linear cut with only a depth-d collar.

The positive conclusion is therefore a stronger exact fusion rule and a
genuine escape from the identical-context owner-duplication obstruction.
Partitioning the entire middle layer into compatible modules, supplying
the full lower deck, and opening a final cyclic source remain unproved.

## 6. Arbitrary cycle count p>=3

The same theorem holds with distinct hubs a_i indexed modulo any p>=3,
the same definitions L_i={c,a_i}, R_i={a_(i-1),a_i}, and the p old
cycles W_i=(L_i,C_i,R_(i+1),D_i). The new cyclic word concatenates

    B_i=(L_i,C_i,R_i,D_(i-1))

in descending i order. The port successor i -> i-1 is one p-cycle.
Every case in Section 2 is unchanged; no step used p=3. Thus all old
widths w<=N preserve the exact OR occurrence multiset.

Let Arc_p be the collection of vertex sets of consecutive arcs of the
cyclically ordered hub set, with sizes from two through p inclusive. Then

    Deck(V)=union_i Deck(W_i)
             union {B union {c} union H : H in Arc_p}.

To prove the only-new-values direction, an interval longer than N sees
all base position types and hence their union B, and it sees an L screen
and hence c. Its hub support moves monotonically around the hub cycle:
L_i,C_i carry a_i; R_i carries a_i and a_(i-1); D_(i-1),L_(i-1),C_(i-1)
carry a_(i-1); and the next R screen makes the next adjacent transition.
The union of a consecutive source interval is consequently a connected
cyclic hub arc, possibly the full hub cycle. A one-hub stretch lies
strictly between consecutive R screens and has length at most N-1, so an
interval longer than N has at least two hubs.

Conversely, concatenate t consecutive complete blocks B_i, for
1<=t<=p-1. Their union is B, c, and the t+1 consecutive hubs
a_i,a_(i-1),...,a_(i-t). This gives every cyclic arc of sizes two through
p as a literal interval within the new cycle. All old targets survive by
the per-width theorem, proving the equality.

Because the base coordinates and c are disjoint from the hubs, an old
target has at most two hubs. Therefore the genuinely new values are
exactly the arcs of sizes three through p. Their count is

    p(p-3)+1:

there are p arcs of each size 3,...,p-1 and one full hub set. For p=3
this reduces to the single full-union addition in Section 3. The formula
does not assert that all subsets of the hub set are covered; disconnected
hub subsets can still be absent.
