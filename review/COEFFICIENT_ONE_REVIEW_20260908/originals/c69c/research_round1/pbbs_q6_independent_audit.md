# Independent PBBS Q6 audit: primitive height-three words with unbounded exit time

Date: 2026-09-07. Pure proof, with no computation, enumeration, or source
modification.

**Verdict: Theorem Q6 is false.** For every integer q>=1, the primitive
Dyck word

    D_q = 1(1100)^q0

has height 3 and empty canonical terminal suffix S(D_q), but the letter
planted at its next tau-step has exact lifetime 3q. Thus neither the stated
height-plus-O(1) bound nor a uniform O(height) repair holds for all such
words. This disproves the asserted pointwise mechanism. It does not by
itself determine the density or packing of short runs in the canonical
cover.

## 1. Sources and prior overlap

The exact maps used below are proved in
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Lemma 8.1 and Theorem 9.1.
For the first-maximum/first-return factorization

    D=P 1 R 0 S,

the exact two-step map is

    tau(D)=S 1_new P 0 R.                                (1)

Here the displayed old first-maximum up-step is consumed, the new divider
is the freshly planted coordinate, and all letters in P,R,S retain their
identities. This is also the necklace interpretation in Q1 of
MATH_THEOREM_PBBS_QUEUE_FLUSH_DYNAMICS_AND_RUN_CONSERVATION_20260820.md.

Prior overlap is significant. Section 23 of the residence-reduction file
and PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md already retract a
different primitive height-time converse. Their first counterexample is
D_2=1110011000, exactly the q=2 case below, and they record its three-word
tau orbit. The present proof explicitly tracks the planted letter and
extends that example to a fixed-height family with arbitrarily long
lifetimes. No novelty claim is made for the individual q=2 word or its
orbit.

## 2. A fixed lifetime convention and the Q4 endpoint issue

Let T be the number of subsequent tau updates from the state immediately
after planting through the update that consumes the planted letter.
Equivalently, T counts the consecutive owner states in which that newly
entered coordinate is present. This is the convention under which planting
in 111000 gives T=3, as in the source's sanity check.

Before the final consuming update, let p,rho,sigma count the updates at
which the marked letter lies in P,R,S respectively. Its height starts at
1; a P update raises it by 1, an R update lowers it by 1, and an S update
leaves it unchanged. It is consumed at height h. Therefore

    p-rho=h-1,
    T-1=p+rho+sigma,
    T=h+2rho+sigma.                                      (2)

The height changes in Q3 are valid. The displayed Q4 identity with h-1
instead of h is valid only when its T excludes the final consuming update;
it does not use the same convention as the source's T=3 sanity check for
111000. This is an endpoint discrepancy of one, separate from the
unbounded error in Q6 established below.

## 3. Exact three-word orbit of the counterfamily

Put

    A=111000,    B=1100,
    D_q=1 B^q 0,
    E_q=A B^(q-1),
    F_q=B^(q-1) A.

D_q is primitive: after the initial 1, each B is read above baseline
height 1, and only the last 0 returns to height zero. Its height is 3.
Its first maximum is in the first B, and its first subsequent return to
zero is the last letter. Thus S(D_q) is empty.

The first-maximum factorizations are explicitly

    D_q = (11) 1 (00 B^(q-1)) 0,
    E_q = (11) 1 (00) 0 B^(q-1),
    F_q = (B^(q-1) 11) 1 (00) 0.

Applying (1) gives

    D_q -> E_q -> F_q -> D_q.                            (3)

For q=1 these three words coincide with A; otherwise they are three
distinct words. This harmless degeneracy does not affect the argument.

In particular, already at the planting step from the primitive D_q the
new word E_q consists of a height-three arch followed by q-1 complete
height-two arches. For q>=2 it is not a single arch, and its canonical
suffix S is nonempty. This directly contradicts the starting structural
assertion and the induction used in Q6.

## 4. Marked-letter evolution and exact lifetime

Mark the letter planted at D_q -> E_q. It is the first up-step of A in
E_q, at height 1.

The first subsequent update E_q -> F_q retains the mark in P. In F_q
it is the second up-step of the final A, at height 2. The next update
F_q -> D_q again retains it in P. It becomes the second up-step, hence
the peak, of the LAST B copy in D_q, at height 3.

Number the B copies in D_q from left to right by 1,...,q. Suppose the
mark is the peak of B_j with j>1. Under the three subsequent updates:

1. D_q -> E_q: the first maximum is in B_1, so the mark lies in R.
   It is moved to the peak of B_(j-1) in the trailing B forest, and its
   height drops from 3 to 2.
2. E_q -> F_q: the mark lies in S. That forest moves to the front,
   and the mark stays at height 2.
3. F_q -> D_q: the mark lies in P. The newly planted outer divider
   raises it to height 3, at the peak of B_(j-1) in D_q.

Thus one R,S,P round takes exactly three updates and moves the marked
peak one B copy to the left. When it reaches B_1, it is the first
maximum-attaining up-step and is consumed on the very next update.

There are two initial climbing updates, q-1 such three-update rounds,
and one consuming update. Therefore

    T(D_q)=2+3(q-1)+1=3q.                               (4)

The nonconsuming counts are p=q+1, rho=q-1, sigma=q-1, consistent
with (2): 3+2(q-1)+(q-1)=3q.

This calculation tracks physical letter identities through (1); it does
not merely compare unmarked binary strings that happen to coincide.
The semilength is r=2q+1, so these primitive height-three words have
T=3(r-1)/2, linear in semilength despite constant height.

### Fully explicit q=2 check

For q=2 the unmarked orbit is

    1110011000 -> 1110001100 -> 1100111000 -> 1110011000.

Starting immediately after the first arrow, the marked letter's successive
positions within the currently rooted Dyck word are

    1 -> 6 -> 7 -> 8 -> 2 -> 3 -> consumed.

Its nonconsuming locations are P,P,R,S,P, followed by consumption.
Thus T=6 although h=3. The family (4), rather than this single finite
example alone, disproves the claimed uniform additive constant.

## 5. Exact unsupported statement and downstream scope

The failing assertion is not just an omitted justification. The implication

    S(D)=empty => the planted word and all its successors are single arches

is false. In (3), the first successor of D_q has q-1 suffix arches. Their
later transport puts first-maximum material ahead of the mark and creates
the R,S interruptions recorded in Section 4. The no-interruption claim
and the claimed T=h+O(1) bound are both false.

Q1's exact necklace update and Q3's height changes survive this audit.
With a consistent endpoint convention, the conservation law survives as
(2). The uninterrupted-climber statement in Q5 does not prevent the
interruptions here: the marked letter is explicitly swept and rested, and
transported old material becomes positioned before it.

Corollaries Q6.1 and Q6.2 and any status conclusion whose sole run-density
input is Q6 therefore lack that claimed proof. The present family has
only one specified word at each semilength 2q+1. It does not prove that
long-lived primitive roots have positive Catalan density, does not
disprove a positive-density short-run statement by another mechanism,
and gives no asymptotic estimate for the edge-disjoint packing nu_H.
Any independent proof of the canonical PBBS obstruction must be audited
separately; this note makes no assertion about proofs outside the stated
Q6 dependency.

A repair cannot uniformly bound all primitive/S-empty roots by a constant
multiple of their height. To recover a positive-density fast-exit theorem,
one needs a further structural restriction on the transported suffix
forests, together with a justified count of that restricted family.
