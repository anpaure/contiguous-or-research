# PBBS uninterrupted lifetimes: exact suffix caps and record peeling

Date: 2026-09-07. Pure proof; no computation, enumeration, or original-source
modification. This note records the suffix-cap characterization and active-path
compression proposed by the uninterrupted-weight agent and independently
audited by the caps-audit agent.

For every exact height h, the complete class of roots with newborn lifetime
T=h admits a unique record-peeling encoding. The encoding yields the
coefficientwise bound

    G_(h,h)(x) <= x^h / F_h(x)^2,

where F_0=F_1=1 and F_h=F_(h-1)-x F_(h-2) for h>=2. In particular,

    G_(h,h)(1/4) <= 1/(h+1)^2.

This is a bound for the full uninterrupted class, not an identification with
a stable-spine cone. It does not supply a uniform exponential weight bound,
a growing-lifetime coefficient estimate, or a Gaussian-scale short-run
density estimate.

Follow-up: pbbs_uninterrupted_critical_weight.md strengthens the terminal
forest caps and the critical upper bound to O(h^(-3)). Its coefficient
transfer in pbbs_zero_budget_uniform_bound.md bounds the complete T=h
class, summed over all heights, by O(4^r/r^2). These later improvements
use the exact encoding proved here and do not cover positive budgets.

## 1. Exact map, conventions, and prior inputs

Use the exact first-maximum/first-return factorization

    D=P 1 R 0 S,              tau(D)=S 1_new P 0 R.       (1)

Here D is a nonempty rooted Dyck word of exact height h. The displayed old
up-step is the first step attaining h, and the displayed old down-step is
the first subsequent return to height zero. All letters in P,R,S retain
their identities. The displayed new up-step is newly planted. Height h is
invariant under tau.

Let D_0=D and D_j=tau^j(D). Plant the marked up-step in the update D_0 -> D_1.
Its newborn lifetime T(D) counts the subsequent updates beginning with
D_1 -> D_2 and ending with, and including, the update consuming that mark.
Thus T=h means the mark survives the h-1 updates out of D_1,...,D_(h-1)
and is consumed in the update out of D_h.

The exact map and height invariance are the inputs from
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Sections 8 and 9. The corrected
marked-height accounting, audited in pbbs_q6_independent_audit.md, is

    T=h+2 rho+sigma.                                      (2)

Here rho and sigma count the nonconsuming updates in which the marked
up-step lies in R and S, respectively. A mark in P rises by one height
unit; a mark in R falls by one; a mark in S keeps its height. In particular,
T=h holds exactly when all h-1 surviving updates put the mark in P.

For a possibly empty Dyck word W, ht(W) denotes its maximum height, with
ht(empty)=0. Maximum and minimum heights of paths include their endpoints.

## 2. Complete dynamic suffix-cap characterization

Let S_i be the canonical suffix S(D_i) in (1). Then

    T(D)=h  iff  ht(S_i)<=i for every 0<=i<h.              (3)

To prove this, suppose first that the mark has survived only in P before
state D_j. The word B_j preceding the mark in D_j is then exactly

    B_j=S_(j-1) 1 S_(j-2) 1 ... 1 S_0.                  (4)

There are j-1 ordinary up-steps between these suffixes. The formula starts
with B_1=S_0. A further P update sends this prefix to S_j 1 B_j, proving
the induction. Each S_i is a Dyck word, so B_j ends at height j-1 and

    maxheight(B_j)
      = max_(0<=i<j) [j-1-i+ht(S_i)].                    (5)

If every cap in (3) holds, (5) is at most j-1. For j<h, the mark itself
ends at height j<h, and no preceding up-step has reached h. Since D_j has
height h, its first maximum lies later, so the mark is in P. This proves
the induction through j=h. In D_h the mark reaches h and no earlier step
does; the next update consumes it, giving T=h.

Conversely, T=h and (2) force every surviving update to be P. Formula (4)
therefore holds at D_h. Consumption there requires maxheight(B_h)<=h-1.
Equation (5), with j=h, gives ht(S_i)<=i for every i<h.

Both endpoints matter: the i=0 cap says S_0 is empty, and the final
i=h-1 cap is required for consumption. Initial emptiness alone is not
sufficient. For example, the independently audited height-three family
D=1(1100)^q0 has S_0 empty but lifetime 3q; for q>=2 its suffix S_1 has
height two and violates the cap ht(S_1)<=1.

## 3. A formal active-path process for every initial root

Define a formal process independently of whether (3) holds. A_i is a
path starting at height i, ending at zero, staying in [0,h], and attaining
h. Set A_0=D. For 0<=i<h, since its initial height is less than h, A_i
has a first up-step attaining h. Factor

    A_i=L_i 1 R_i 0 U_i,                                (6)

at that up-step and the first later return to zero, and put

    A_(i+1)=L_i 0 R_i, read from initial height i+1.       (7)

The suffix is denoted U_i here to distinguish it from S(D_i) until the
connection to the actual marked dynamics has been established.

In (6), L_i runs from i to h-1, stays in [0,h-1], and has no visit to h.
The path R_i runs from h to 1 and stays in [1,h]. The suffix U_i is an
ordinary Dyck word of height at most h.

In (7), the heights along L_i are increased by one. Thus this prefix
stays in [1,h] and ends at h. The displayed down-step leads to h-1.
The heights along R_i are decreased by one, so this remainder stays in
[0,h-1] and ends at zero. This proves that the process exists inductively
through A_h, with A_(i+1) staying in [0,h] and attaining h.

At each step an up-step is changed to a down-step, the subsequent return
down-step is deleted, and the terminal suffix U_i is discarded. No other
letters are changed or reordered.

### Which up-steps are selected

In the original word D, let u_k be the first up-step attaining level k.
The successive selected up-steps in (6) are precisely

    u_h, u_(h-1), ..., u_1.                             (8)

The case i=0 is the definition of u_h. For the induction, when
1<=i<h, the original prefix strictly before u_(h-i+1) is still an
unchanged initial prefix of A_i; previous selections and deletions
occurred later. Reading that prefix from height i, its first visit to h
occurs at the original step u_(h-i). This step precedes u_(h-i+1), so
the same property holds at the next stage.

Because u_1 is the first letter of a nonempty Dyck word, the final selected
up-step is the first letter of A_(h-1), and L_(h-1) is empty. Consequently

    A_h starts at h, begins with a down-step,
    and thereafter stays in [0,h-1] until ending at zero. (9)

In particular, A_h has no visit to h after its initial vertex.

## 4. Connection to the actual marked dynamics

The formal suffixes satisfy the exact equivalent criterion

    T(D)=h  iff  ht(U_i)<=i for every 0<=i<h.             (10)

For sufficiency, after planting, the actual marked word is

    D_1=U_0 * A_1,

where * is the marked up-step. Suppose that up to D_i the caps have kept
the mark in P. Its actual word is then

    D_i=B_i * A_i,
    B_i=U_(i-1) 1 U_(i-2) 1 ... 1 U_0.                 (11)

The prefix-height computation (5) gives maxheight(B_i)<=i-1. For i<h,
the first maximum therefore lies in A_i, at the selected step of (6).
Applying (1) to (11) gives

    D_(i+1)=U_i 1 B_i * L_i 0 R_i
           =(U_i 1 B_i) * A_(i+1).                    (12)

This proves the induction and shows that the actual suffix S(D_i) equals
the formal suffix U_i at every stage used. At D_h, the prefix cap makes
the mark the first up-step attaining h, hence T=h.

For necessity, T=h forces all P updates. Applying (12) successively
identifies the actual active paths and suffixes with the formal ones;
then (3) gives all the caps in (10).

Thus (10) describes the entire height-h, lifetime-h class. It does not
assume that every active path has only one arch, that later suffixes are
empty, or that original side forests stay in a fixed spine position.

## 5. Unique inverse and its exact admissibility check

An encoding consists of the terminal path A_h and the ordered suffixes
(U_0,...,U_(h-1)). To reconstruct, work backwards for i=h-1,...,0.

Given A_(i+1), locate its last visit to height h. The next step must be
a down-step, since the path stays at most h and ends at zero. This uniquely
factors its word as

    A_(i+1)=L_i 0 R_i,                                  (13)

with the cut immediately after that last height-h vertex. The suffix R_i
then stays at most h-1. The one additional inverse admissibility check is

    every height along the prefix L_i is at least 1.     (14)

If (14) holds, set A_i=L_i 1 R_i 0 U_i, reading it from height i.
The heights along L_i are lowered by one, so they stay in [0,h-1]. The
inserted up-step first reaches h. The heights along R_i are raised by
one, so they stay in [1,h], ending at 1. The inserted down-step is
therefore the first subsequent return to zero. Appending a Dyck suffix
U_i of height at most i preserves the required range [0,h].

This proves that (14), together with the stated terminal-path and suffix
conditions, is sufficient as well as necessary. Necessity follows because
every forward prefix L_i was raised from a nonnegative path. The last
height-h visit in (13) is the correct cut: the forward prefix ends at h,
whereas the entire remainder after its next down-step stays at most h-1.

Starting from (9), and passing (14) at each inverse step, therefore
reconstructs a unique original Dyck word D whose formal suffixes are
exactly the prescribed U_i. By (10), this word has T=h. Conversely every
height-h root with T=h supplies such an admissible tuple. We have a
bijection with the tuples that pass all inverse checks, and an injection
into all tuples obeying only the terminal condition (9) and ht(U_i)<=i.

The inverse tests must not be silently omitted when asserting equality
of generating functions. Omitting them is legitimate for an upper bound.

## 6. The coefficientwise generating-function bound

Let C_j(x) count Dyck words of height at most j by their number of up-steps:

    C_0(x)=1,
    C_j(x)=1/(1-x C_(j-1)(x)) for j>=1.                 (15)

Let G_(h,h)(x) count original roots of exact height h and lifetime h by
semilength. The unrestricted suffix tuple contributes

    product_(i=0)^(h-1) C_i(x).                          (16)

The terminal paths in (9), weighted by their number of up-steps, have
the same generating function. For an explicit decomposition, the first
step is the compulsory descent from h to h-1. Before the first descent
from a later level j to j-1, the intervening segment is a Dyck excursion
above j with relative height at most h-1-j. After the first arrival at
zero, the remaining tail is a Dyck word of height at most h-1. These
unique pieces contribute C_0,C_1,...,C_(h-1), once each; all separating
down-steps have weight one.

At each forward step (7), the number of up-steps drops by
1 plus the number of up-steps in U_i. Hence

    semilength(D)=h+ups(A_h)+sum_(i=0)^(h-1) ups(U_i).    (17)

The injection at the end of Section 5 now gives, coefficientwise,

    G_(h,h)(x) <= x^h [product_(j=0)^(h-1) C_j(x)]^2.   (18)

For the continuant convention used here, define

    F_0(x)=F_1(x)=1,
    F_h(x)=F_(h-1)(x)-x F_(h-2)(x) for h>=2.            (19)

Equation (15) gives C_j=F_j/F_(j+1), so the product telescopes:

    product_(j=0)^(h-1) C_j(x)=1/F_h(x).

Therefore the promised upper bound is

    G_(h,h)(x) <= x^h/F_h(x)^2.                         (20)

No equality is claimed in general. Both sides have nonnegative power
series, and at x=1/4 every finite C_j is finite. Since

    C_j(1/4)=2(j+1)/(j+2),

equation (18) yields

    G_(h,h)(1/4) <= (1/4)^h [2^h/(h+1)]^2
                 =1/(h+1)^2.                           (21)

The critical-weight bound is polynomial in h. It is not a proof of
exponential suppression in h and does not by itself estimate the
coefficient at semilength r uniformly when h grows with r.

## 7. Previously verified small-height checks

For h=1, a root is (10)^r and its newborn lifetime is r. Thus

    G_(1,1)(x)=x,

which agrees with (20), since F_1=1. The suffix cap requires U_0 empty,
and the terminal path is the single down-step.

For h=2, the independently verified complete T=2 class at exact height
two is

    D=(10)^a 1(10)^b 0,  a>=0, b>=1.

There are r-1 such roots at semilength r>=2, giving

    G_(2,2)(x)=x^2/(1-x)^2.

This agrees with (20), since F_2=1-x. These are height-specific checks;
the additional height-one root 1010 also has lifetime two but is counted
in G_(1,2), not in G_(2,2). No complete height-three formula is asserted
or needed here.

## 8. Scope and the remaining gap

The suffix criterion (3) and the admissible inverse encoding describe
the full class T=h. A stable-spine family, if separately proved to obey
these caps, is only a subfamily. Its proposed product formula cannot be
substituted for the full-class count, and no earlier cone formula or
pole claim is used in this proof.

The present upper bound follows by forgetting inverse constraints, not
by enumerating them. It supplies neither a uniform exponential bound
on the critical weight nor control of classes with interruptions
T=h+2 rho+sigma>h. In particular, no estimate for the full event T<=H
at H of order sqrt(r), and no Gaussian-scale density or packing conclusion,
has been obtained. All independent upper bounds for the original covering
problem remain separate from this result.
