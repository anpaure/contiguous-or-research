# Exact forced-head menus and two private Dyck banks

Date: 2026-09-09. Pure incidence proof; no execution, matching search or
word construction. This refines the freed-head interface in
[the all-root entrance obstruction](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md).

For every Dyck word D of semilength r-1, the forced upper is Z_D=111D,
with the new bits 00. The available root heads are obtained by deleting
a one other than the first two coordinates u,x. Write H for all old
strictly-positive rank-(r+1) words, equivalently 1 followed by a Dyck word
of semilength r. The question here is which heads can be freed and matched
injectively to the forced Z_D. Deletion age is a separate condition.

## 1. Complete menu and its unique prefix minimum

Let D^{down j} denote D with its up-step at position j changed to a
down-step. The COMPLETE head menu is

    H_(Z_D) = {110D} union {111 D^{down j} : D_j=1}.       (1)

These are all r permitted deletions. Every displayed head is in H, as
shown in the original obstruction proof. No new-coordinate deletion is
possible because Z_D has new bits 00.

Order words by pointwise prefix-walk height. In a fixed Z_D, deleting an
earlier one subtracts two from an earlier suffix, hence gives a smaller
word in this order. Thus (1) is totally ordered by the position deleted,
and 110D, obtained by deleting the third old coordinate y, is the UNIQUE
least member. If an up-step j of D is deleted instead, the sum of all old
prefix heights exceeds that of 110D by exactly 2j.

Consequently D->110D is also the unique minimum-total-prefix-area matching
among ALL full matchings into H. This is an incidence/order extremality
statement; it does not make that deletion age-legal.

## 2. The complete inverse menu

Every head in H begins with 11. There are two cases.

If it begins with 110, it is uniquely 110D for a Dyck D. Its only incident
forced upper is 111D: deleting an up-step inside another D would leave the
prefix 111. Thus all heads in

    H0={110D : D Dyck of semilength r-1}                  (2)

are PRIVATE, meaning they have degree one in this entire incidence graph.
Freeing exactly H0 therefore forces exactly the diagonal matching
Z_D->110D. There is no nontrivial permutation of these freed heads.

Otherwise the head is 111Q. The suffix Q has total height -2 and every
prefix has height at least -2. Its incident forced uppers are exactly
111D obtained by changing a zero of Q to one so that D is Dyck. Let j_0
be the first time Q visits height -1. A zero at position j is eligible
if and only if j<=j_0:

* For j>j_0, the earlier negative prefix survives, so D is not Dyck.
* For j<=j_0, earlier prefixes are nonnegative and every later prefix
  gains two, making it nonnegative because Q never falls below -2.

This describes EVERY preimage. In particular every such head has a
preimage, so the union of all menus (1) is the ENTIRE head family H.

There is an equivalent Dyck decomposition

    Q=A 0 B 0 C,                                       (3)

where the displayed zeros first reach heights -1 and -2, respectively,
and A,B,C are Dyck words. If A has semilength a, this head has exactly
a+1 incident forced uppers: one for every zero of A and the first displayed
zero. Equation (3), with one of these zeros marked and flipped, is an
explicit insertion/deletion parametrization of all noncanonical incidences.

The full matching choices can therefore be encoded by choosing, for each
D, either its private canonical head or a marked up-step in (1), subject
only to not using the same resulting head twice. The inverse classification
above gives the exact collisions; it is not an unspecified head menu.

## 3. A second private bank and independent binary choices

Assume r>=2. Every nonempty Dyck D begins with one; write D=1R. Its
canonical head and its head obtained by deleting this first D-one are

    h0(D)=1101R,       h1(D)=1110R.                     (4)

Both belong to the menu of Z_D=1111R. The second head is private too:
in Section2 its Q=0R first reaches -1 at its first position, so only that
zero can be flipped. Its sole source is the original D=1R.

Conversely, a head 111Q is private only if Q starts with zero. Otherwise
the nonempty initial Dyck word A in (3) has at least one down-step and
the inverse menu has size at least two. Hence the ENTIRE degree-one head
set is the disjoint union

    H0={1101R : 1R is Dyck},
    H1={1110R : 1R is Dyck}.                            (5)

Each source has exactly its two heads from (4) in this private set. All
these pairs are mutually disjoint: the fourth-prefix patterns 1101 and
1110 separate the two types, and R identifies D within each type.

It follows that ANY independent binary choice between h0(D) and h1(D)
for every D yields an injective head assignment. Its freed bank has
exactly Cat_(r-1) heads, the necessary minimum from the obstruction. There
are 2^{Cat_(r-1)} distinct such banks, and each forces its own matching.
Within the union of private heads, a minimum-size bank supports every
source if and only if it contains exactly one member of every pair (4).

For r=1, D is empty and the menu has only the canonical head 110. The
inverse classification still holds, while the two-choice assertion is
intentionally restricted to r>=2.

## 4. The stronger age gate selects a bank; incidence does not prove it

The binary-choice theorem above is INCIDENCE ONLY. In particular the
private, prefix-minimal choice 110D may still delete a coordinate too
young for residence three.

The [separate arrival-age analysis](Q3_ROOT_SOCKET_TWO_STEP_AGES_AND_CORRECTED_1110_HEADS_20260909.md)
proves the stronger conclusion that, in a residence-at-least-two history arriving
at U=011D00, the old coordinates x,y have ages exactly one and two,
while every D-one has age at least three. This statement is not proved
by the incidence analysis here. Its full inverse-matching proof was subsequently
read independently and passed: the ordinary inverse removes y, while the
unique z=b,w=u exception inserts and immediately deletes b, violating
residence at least two. The r=1 boundary and explicit conditional connector
were also checked. No mathematical execution was used in this review.

With that separately proved age lemma, freeing exactly H0 is insufficient for
residence three: its unique forced matching deletes y at age two. Every
head in (1) obtained by deleting a D-one passes this local age test. In
particular the explicit PRIVATE bank H1, with the forced assignment

    Z_(1R)=1111R -> 1110R,                              (6)

is a minimum-size, locally age-legal replacement. Among minimum-size
banks using only private heads, the age gate selects H1 uniquely.
Shared nonprivate heads can still offer other incidence choices.

Even after the local age lemma is established, (6) does not fill the
other incoming sockets, connect components, prove a spanning canonical-Phi
factor, or verify a complete interval-target family. Those global tasks
are outside this selectable head-bank result.
