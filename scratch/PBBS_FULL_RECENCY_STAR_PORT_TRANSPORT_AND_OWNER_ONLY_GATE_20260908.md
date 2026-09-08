# Full-recency star ports, maximal cap antecedents, and the exact owner-only gate

2026-09-08. Pure constructive proof by `exact_b_induction`, following
root's requested owner-only test. No mathematical execution was run.
This supplies a sufficient all-target fusion operation on changed
states, a precise antecedent interface, and an actual canonical example
showing that the owner-only gate is not vacuous. It does not claim a
new complete bank or optimal word.

The current exact checkpoint, tagged-context fusion, cap criteria,
capped-context port lemma, and canonical mountain-C6 transport note
were read for this task. In particular the fixed native rank5/rank5
context family has already been exhaustively refuted; strengthening
that same family is not proposed as a new search.

## 1. An explicit full-state reset identity

An ordered recency partition lists coordinate blocks from most recent
to oldest. Appending a nonempty letter R applies T_R: prepend R,
remove its coordinates from every old block, and delete empty blocks.
The prefix unions of this partition are exactly the distinct nonempty
suffix ORs at that endpoint.

Let K be a six-set. Fix a nonempty proper subset F of K, a coordinate
u outside K, distinct arms a_0,...,a_(p-1) outside K union {u}, and an
ordered partition C=(C_1,...,C_m) of the remaining coordinates
Omega minus (K union {u}). Thus C contains the arms. Assume

    C_1={w}, where w is outside K union {u,a_0,...,a_(p-1)}.

For each i define the complete cut state

    P_i=(F | K minus F | {u,a_i} |
                    C_1 minus {a_i} | ... | C_m minus {a_i}), (1.1)

omitting empty blocks. Choose S_i subset F with |S_i|=|F|-1 and set

    R_i=S_i union {a_i,a_(i+1)}.                         (1.2)

Then the exact identities are

    T_(R_i)(P_i)=T_(R_i)(P_(i+1))=Q_i,                  (1.3)

where

    Q_i=(R_i | F minus S_i | K minus F | {u} |
                  C_1 minus {a_i,a_(i+1)} | ... |
                  C_m minus {a_i,a_(i+1)}).             (1.4)

Proof: both arms are removed by R_i. Consequently the third old block
leaves exactly {u}, whether it originally contained a_i or a_(i+1).
Both ordered tails reduce to the same C blocks with both arms removed.
The two earlier blocks are identical in P_i and P_(i+1), so their
reductions agree as well. This proves equality of the entire recency
states, including every high-rank prefix, not just the first four
source-window ORs.

For |F|=4 the successive ranks at the two states begin

    P_i: 4,6,8,9,...,
    Q_i: 5,6,8,9,... .                                  (1.5)

Thus both have b_8=2 and b_9=3, using the number of distinct recency
prefixes below the indicated rank. The edge does not increase either
potential. At these ports the rank-eight labels are

    K union {u,a_i},   K union {a_i,a_(i+1)},

and the rank-nine labels are

    K union {u,a_i,w},   K union {u,a_i,a_(i+1)}.          (1.6)

For p>=3 they are distinct within each layer across all displayed
port states; the first family contains u (and, at rank nine, w),
while the second distinguishes the consecutive arm pair. This checks
the port-level middle/facet and potential budgets. It does not assert
uniqueness at all other positions of unspecified surrounding words.

The same identity works for 1<=|F|<=5. Choosing |F|=4 matters because
a last-two-letter context may then have unequal ranks5 and4, with
union K of rank6. This is outside the previously tested family that
only deletes one coordinate from each of two native rank6 letters
and consequently produces ranks5 and5.

## 2. A genuine all-target zero-extra fusion, given these states

Suppose p actual cyclic words use the full ground set Omega, with one
marked edge in each distinct component. Immediately before that edge
their ACTUAL periodic recency states are P_i, and the following letter
is R_i. Replace each marked successor by attaching the tail beginning
with R_i after the port whose cut state is P_(i+1).

Equation(1.3) makes the full state immediately after each entered R_i
equal its original state Q_i. Thereafter the unchanged letters of
that component propagate the original states, up to its next marked
cut. The routing is one cyclic permutation of the p components, so
they become one cyclic word with exactly the same total number of
letter occurrences.

All original full recency states are retained at their corresponding
physical letter occurrences. To justify that these consistent assigned
states are the actual periodic states of the new word, observe that
each coordinate appears in a full period: running through a complete
period fixes its last occurrence regardless of any initial state.
The resulting periodic recency assignment is unique. The assigned
states therefore coincide with it.

Every original cyclic interval target is a suffix OR at some endpoint,
and hence is a prefix union in one of these states. All named lower
and upper targets are therefore preserved by the fusion. This is
full-target transport, not merely preservation of rank8/9 labels or
of windows of length at most four.

The operation is conditional on ACTUAL states of the recoded source.
It does not permit replacing native states by formal P_i without a
literal antecedent. Unlike a permutation of the refuted native full
state inventory, these P_i can be different states; their construction
is governed by the next section.

## 3. Exact maximal-cap antecedent interface

Let a finite cyclic source have allowed letter envelopes D_j. Specify
the desired owner/facet windows after any proposed alternating
exchange, the named lower/upper witnesses that must remain, and any
port-state suffix windows. Each requirement has an actual physical
cyclic interval I_alpha and exact target T_alpha. Define

    E_j^max = D_j intersect
                 intersection_(alpha:j in I_alpha) T_alpha. (3.1)

An empty target intersection here means no restriction beyond D_j.
There exists a nonempty cap realizing ALL these interval requirements
if and only if the explicit maximal cap in (3.1) is nonempty at every
position and satisfies

    union_(j in I_alpha) E_j^max=T_alpha for every alpha. (3.2)

Necessity: every feasible cap is contained coordinatewise in E^max.
Enlarging it to E^max cannot exceed any required interval target by
the definition of (3.1), and cannot destroy any required positive
coordinate. It thus remains feasible. Sufficiency is the direct
construction E=E^max.

To impose a FULL state P_i rather than selected prefixes only, specify
an exact desired union for every suffix length ending at that port
through one period, using a nondecreasing schedule of the prefix
unions in P_i. Require every prefix in P_i to occur in that schedule.
Then (3.2) is exactly equality of the full recency state; it excludes
unintended intermediate suffix unions. Merely assigning one witness
for each desired prefix would not by itself exclude extra prefixes.

Thus the complete constructive operation is: provide concrete new
window locations, form (3.1), verify (3.2) and the full port states,
then apply Section2's deterministic successor reassignment. No
unverified fractional rounding, prospective owner label, or extra
join letter is concealed in that compiler.

This uses the general maximal-cap principle already proved in the
cap notes; the new application is to complete recoded port states and
all-target transport. It does not supply the required interval
assignment or show that a particular canonical envelope passes it.
If an owner/facet exchange changes the maximal source envelopes,
those changed envelopes must be explicitly constructed first.

## 4. The cheaper owner-only necessary test

In a triple-preserving H3 source, a port with state(1.1) and next
letter(1.2) must have consecutive native rank-nine owners

    V=K union {u,a,w} -> T=K union {u,a,b},              (4.1)

with their common rank-eight facet P=K union {u,a}. The next facet
must be Q=K union {a,b}, so the next owner transition removes u.
Group such actual transitions by (K,u,w), and record the directed
edge a -> b. Any star cycle must occur in this owner-only graph,
regardless of how its first two letters are capped.

Write G=K union {u}. In the canonical PBBS factor, the map on these
edges is necessarily

    b = unmatched_zero(G union {a}).                    (4.2)

Indeed the lower owner before the edge is A=Omega minus V. Its first
f-step must give facet P=G union {a}, which requires its unmatched
zero to be w. Its next f-step gives the complement of T by deleting
exactly the unmatched zero b of P. The additional next-facet condition
is that the unmatched zero of Omega minus T is u. All these conditions
are testable on the actual owner transitions without a cap search.

## 5. Every owner-only directed cycle has length exactly three

The rank-seven word G has three cyclic unmatched zeros. More generally,
on n=2r+1 sites any rank-(r-1) word has three such zeros after the
canonical noncrossing cancellation of matched10 pairs. Denote them
in cyclic order by c_0,c_1,c_2. The intervals between consecutive
unmatched zeros are Dyck words, giving the cyclic representation

    0_(c_0) D_0 0_(c_1) D_1 0_(c_2) D_2.

If a=c_j is flipped to one, its new one matches the next unmatched
zero c_(j+1); the sole remaining unmatched zero is c_(j-1). Hence

    root(G union {c_j})=c_(j-1).                        (5.1)

If a is a matched zero inside D_j, flipping it raises every later
prefix of that Dyck block by two and makes its final height two.
The modified block remains nonnegative. Traversing the next two
unmatched zeros reduces that height to zero; the intervening Dyck
blocks cannot introduce a negative excursion. The sole unmatched
zero of the full word is then c_j, the one preceding D_j. Thus

    root(G union {a}) is always one of c_0,c_1,c_2.       (5.2)

Any directed cycle of the map(4.2) must therefore lie among those
three vertices; there its action is exactly the three-cycle(5.1).
The extra root-w/root-u tests may delete edges but cannot create
another cycle. In particular every surviving owner-only cycle has
length three, and if w is itself one of the three unmatched zeros
the excluded vertex w prevents any such cycle in that group.

This is a classification, not a no-cycle theorem. The next section
gives a surviving actual canonical example.

## 6. The verified mountain C6 is an owner-only counterpattern

Use zero-based coordinates and set

    C={1,2,3,4,5,6},   K={10,11,12,13,14,15},
    w=0,   u=16,   arms={7,8,9}.

The three actual native lower-owner transitions of the retained
mountain-C6 certificate are

    510=C union {7,8} -> 255=C union {0,7},
    894=C union {8,9} -> 383=C union {0,8},
    766=C union {7,9} -> 639=C union {0,9}.

The unmatched zero of each left lower owner is0. The unmatched zero
of each right lower owner is16. These follow directly by reading
the corresponding Dyck cuts: after0 each left lower owner is Dyck,
and after16 each right lower owner is Dyck.

Complementing gives the owner-only edges

    9 -> 8,   7 -> 9,   8 -> 7

in the common group(K,u,w). Thus the owner-only graph contains the
directed cycle9->8->7->9. It cannot be ruled out by PBBS root signs
or middle/facet uniqueness.

These three ports belong to only two original components, of periods
17 and221. They are the analytically specified C6 in
`PBBS_CANONICAL_MOUNTAIN_C6_ALL_UPPER_TRANSPORT_20260908.md`, with exact
data in `k17_canonical_rigid_clean_c6_20260908.json` and verifier
`audit_k17_canonical_rigid_clean_c6_20260908.py`. Their previously
executed surgery gives two cycles135 and103; it does not reduce the
component count. This note did not rerun that certificate.

The exact verified source change retains every rank-nine owner, the
global rank-eight adjacent-facet multiset, and all1,343 local proper
upper owner targets. Rebuilding the two H3 envelopes is justified by
their positive owner runs of length at least seven, and preserves
global rank8 through17 coverage at the same W positions. The rank6
and rank7 source palettes were not certified by that old report.
No stronger lower-coverage conclusion is imported here.

## 7. What has and has not advanced

The all-target reset identity(1.3), the actual cyclic operation of
Section2, and the maximal antecedent test give a complete sufficient
compiler once recoded states and witness intervals are supplied.
The owner-only gate is classified and has an actual canonical
three-cycle, so it is not vacuous. However that example has only two
components and does not establish the needed full recency tails.

With |F|=5 and a common rank5/rank5 context, pin-preserving caps of
the unchanged native pair force the same removed coordinate at both
positions. This puts the construction back inside the already refuted
fixed-bank directed-port family. A full-state condition cannot rescue
that failed necessary gate. The |F|=4 form requires additional core
recoding and is not decided by that earlier census; it is still not
asserted to occur or to preserve a complete lower-target assignment.

No new bank-cover or optimal-word claim follows. A complete capped bank
would still need enough legal fusions, preservation of all assigned
targets under its antecedent, and a separately charged linear opening.
The all-dimensional objective nu(k)=B(k) remains open.
