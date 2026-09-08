# Tagged-context fusion preserves every old cyclic width

2026-09-08. Derived in the exact-B investigation by root; independently
checked in `EXACT_B_TAGGED_CONTEXT_C6_FUSION_INDEPENDENT_AUDIT_20260908.md`.
This is a finite construction theorem. It is not an all-dimensional
partition theorem or a proof of nu(k)=B(k).

## 1. Construction

Fix p>=3, with indices taken modulo p. Let

    c, a_0,...,a_(p-1)

be distinct coordinates. Let C=(C_1,...,C_m) and D=(D_1,...,D_l) be two
finite words using coordinates disjoint from these active coordinates.
The base letters may be empty, and either base word may have length zero.
Put

    C_i = (C_t union {a_i})_(t=1)^m,
    D_i = (D_t union {a_i})_(t=1)^l,
    L_i = {c,a_i},
    R_i = {a_(i-1),a_i},
    N = m+l+2,
    U = union_t C_t union union_t D_t.

Consider the p cyclic words, each of length N,

    W_i = (L_i, C_i, R_(i+1), D_i).

Replace them by the one cyclic word of length pN obtained by traversing
indices in decreasing order:

    V = (..., L_i, C_i, R_i, D_(i-1),
              L_(i-1), C_(i-1), R_(i-1), D_(i-2), ...).

Each context block occurs once on either side of the replacement. All
letters of all words are nonempty, including tagged copies of empty base
letters. There is no added letter or uncharged bridge.

For a cyclic word Q, Deck(Q) means the distinct ORs of all nonempty cyclic
intervals of length at most its stated period. The multiset at width w
counts one occurrence for each cyclic start position.

## 2. Exact width theorem

For every 1<=w<=N, the multiset of width-w interval ORs in V is exactly
the multiset union of those in W_0,...,W_(p-1).

### Proof

Call the L and R letters screens. Their positions alternate in both the
old and new words, with successive distances m+1 and l+1. Any interval of
width at most N therefore contains at most two screens, with at most one
of each type. The following correspondence preserves the lengths of the
context fringes and is bijective within each screen case.

**No screen.** The interval lies wholly inside one C_i or D_i. That same
literal block remains in V, so copy the interval there.

**Only L_i.** Its left fringe is a suffix of D_i, and its right fringe is
a prefix of C_i. These blocks remain on the same sides of L_i in V.
The interval copies literally.

**Only R_(i+1).** The old fringes are a suffix of C_i and a prefix of D_i.
The new fringes are the equally long suffix of C_(i+1) and the same prefix
of D_i. The untagged base fringes are identical. Their possible tag
difference is contained in {a_i,a_(i+1)}, which R_(i+1) already supplies.
Thus their ORs agree.

**L_i followed by R_(i+1).** Map to L_(i+1) followed by R_(i+1) in V.
The full intervening contexts are C_i and C_(i+1), respectively. Before
the first screen, change the D_i suffix to the corresponding D_(i+1)
suffix; after the second screen keep the D_i prefix. The screen unions
in both intervals are

    {c,a_i,a_(i+1)}.

Every changed tag is in this set, while all untagged base letters and
fringe lengths agree. The ORs are equal.

**R_(i+1) followed by L_i.** The full intervening D_i remains the same.
The left C_i fringe changes to the corresponding C_(i+1) fringe, and
the right C_i fringe remains the same. The screen union again contains
both affected tags, so the ORs agree. This case is OR-preserving, not
necessarily a literal copy.

The cyclic index shifts in these rules are bijections, and the screen
cases partition all starts on both sides. This proves exact multiset
equality for each width. QED.

## 3. Complete cyclic support

Let a cyclic hub arc mean a nonempty set of consecutive vertices in the
cyclic order a_0,...,a_(p-1), without repetition. Then

    Deck(V) = union_i Deck(W_i)
              union {U union {c} union H:
                       H is a cyclic hub arc, 2<=|H|<=p}.

### Proof

The width theorem retains all old targets. Projecting V onto the base
coordinates gives repetitions of the period-N pattern (empty,C,empty,D).
Thus any interval of width greater than N contains all of U. It also
contains an L screen and hence c.

Along V the hub labels pass consecutively from a_i through L_i,C_i to
the transition R_i={a_i,a_(i-1)}, then to a_(i-1) through D_(i-1),
L_(i-1),C_(i-1). A consecutive interval therefore has a cyclic arc of
hub labels, or all of them. A one-hub stretch has length at most N-1,
so width greater than N supplies at least two hubs. This proves that
there are no other new targets.

Conversely, t consecutive complete blocks

    (L_i,C_i,R_i,D_(i-1)), ...

have length tN and OR equal to U union {c} union an arc of t+1 hubs.
Taking 1<=t<=p-1 and all cyclic starts supplies every displayed arc.
QED.

Old words use only two adjacent hubs. Consequently the genuinely new
targets are exactly those with hub arcs of sizes 3,...,p. There are
p(p-3)+1 of them. For p=3 this adds precisely the full union of all old
words. Disconnected hub subsets are not supplied by this construction.

## 4. Middle owners and a concrete k=17 module

If, for some h<=N, the h-window ORs across the old words are all distinct
and all have rank R, the same is true in V. This is an immediate
consequence of the exact multiset theorem. Here an owner is that actual
window OR; no prospective owner labels are introduced.

The identical-context fusion in
`EXACT_B_SHARED_CONTEXT_C6_FULL_CYCLIC_DECK_FUSION_20260908.md` cannot have
globally distinct width-(d+1) owners if a repeated common context has
length at least d+1: its initial window would repeat an owner. Tagged
contexts escape that restriction.

For an explicit example, choose four base coordinates K, nine further
distinct base coordinates x_1,...,x_9, and c,a_0,a_1,a_2. These are 17
coordinates in total. Use

    C = (K union {x_1},...,K union {x_5}),
    D = (K union {x_6},...,K union {x_9}),
    p=3, d=3, h=4, N=11.

In W_i, a_i is permanent. The nonhub symbols in order are

    c, x_1,...,x_5, a_(i+1), x_6,...,x_9.

They are all distinct. Every four-position window contains context
letters, hence contains K, and its OR consists of K, a_i, and four
consecutive symbols from this displayed 11-cycle. Its rank is nine.
Within one old cycle these owners are distinct because a proper cyclic
interval in a cycle of distinct symbols determines its start.

Across different old cycles, an owner with only one hub identifies its
permanent hub a_i. An owner with two hubs has exactly {a_i,a_(i+1)},
which also identifies the old cycle when p=3. Thus all 33 owners are
distinct. The fused 33-position word retains all of them and all old
cyclic targets, and additionally realizes the full 17-coordinate union.

This supplies a literal owner-once fusion module with old period
N=11>2d+2=8. It does not cover the full 17-cube.

## 5. What is and is not settled

The theorem provides a zero-cost cyclic fusion for a concrete family of
nonidentical contexts, preserving all old widths rather than only a
fixed set of lower shadows. It is a possible building block for a fresh
exact construction.

It does not partition an entire middle layer into compatible modules,
regenerate the required tagged structure after arbitrary fusions, solve
the lower-target compiler, or pay for a linear opening. Each old word has
a permanent hub, so it is not an intact canonical PBBS component. The
33-owner example does not solve the remaining 140-cycle PBBS fusion.

The all-dimensional objective nu(k)=B(k) remains open in this research
record. The theorem and example were proved symbolically; no numerical
experiment is used as a premise.
