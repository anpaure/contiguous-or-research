# Original PBBS peeling forests: universal caps and an exact product law

Date: 2026-09-07. Pure proof; no computation or original-source edits.
The universal caps, graded bijection, exact zero-budget product, and
shifted-cap algebra were independently audited by the recency-gate agent
and reviewed by the root task. The subsequent first-packet majorant in
pbbs_growing_budget_first_packet_majorant.md yields the uniform growing-
budget estimate in pbbs_growing_budget_uniform_bound.md without using
the unproved maximum-excess coupling discussed below.

The terminal half-height caps previously used for T=h are universal for
the original formal peeling of every height-h Dyck root. The suffixes
have complementary universal caps. Together these give an exact product
encoding of all height-h roots, before any statement about their newborn
lifetime. In particular, terminal-cap violations cannot measure the
interruption budget: there are no such violations.

The budget-dependent condition for T=h is instead ht(U_i)<=i. In the
exact original-root product law, these are independent forest events at
critical Boltzmann weight. This does not make subsequently reached marked
states independent, and no growing-budget coupling is asserted here.

## 1. Original formal peeling and universal prefix clearance

For an original height-h Dyck word D=A_0, define its full formal peeling

    A_i=L_i 1 R_i 0 U_i,
    A_(i+1)=L_i 0 R_i, read from height i+1,             (1)

for i=0,...,h-1. The selected up-step first reaches h and the selected
down-step first returns to zero afterward. Each A_i starts at i, ends
at zero, stays in [0,h], and attains h. The selected up-steps are the
original first-hitting steps of levels h,h-1,...,1. Thus the terminal
A_h starts at h and never revisits h after its first down-step.

For every i, the prefix through the last visit to h in A_i stays at
height at least i. This is a property of every original root, not only
of roots with T=h. To prove it forward, start with nonnegativity of A_0.
The prefix L_i before the first maximum lies in the protected prefix.
In A_(i+1) it is raised by one and ends at h, whereas the entire remainder
after the following down-step has height at most h-1. This proves the
induction.

Equivalently, in the inverse of (1), the cut at the last visit to h must
occur before any visit below the starting height. One can also prove this
by inverse persistence: an old prefix before a cut remains before every
later inverse cut and is lowered at each remaining inverse step. A vertex
below the current starting height would become negative in A_0.

No suffix cap ht(U_i)<=i is used in either argument.

## 2. Both universal forest caps

Decompose the terminal path by successive first descents:

    A_h=0 V_0 0 V_1 ... 0 V_(h-1).                     (2)

The original unrestricted cap of V_j is j, and its initial baseline is
h-1-j. The universal prefix clearance sharpens this to

    ht(V_j)<=ceil(j/2).                                (3)

Indeed, after k inverse operations, while the cut has remained before
this block, its baseline is h-1-j+k in the path starting at h-k. If
2k<j+1, that baseline is below the starting height, so the cut must stay
before the block and the block cannot attain h. Apply this at
k=floor(j/2), obtaining ht(V_j)<=j-k=ceil(j/2).

There is a complementary universal cap for the original suffixes:

    ht(U_i)<=h-ceil(i/2),       0<=i<h.                  (4)

For i=0 this is the ordinary height cap h. For i>=1, the suffix U_i starts
at baseline zero in A_i. After q inverse operations whose cuts stayed
before it, its baseline is q in the path starting at i-q. If 2q<i, the
baseline lies below the starting height. Universal prefix clearance
therefore keeps the next cut before U_i and forbids any height-h visit
inside it. The block remains unchanged and its baseline rises by one at
the next inverse operation. At q=floor((i-1)/2), absence of height h gives

    q+ht(U_i)<=h-1,
    ht(U_i)<=h-1-floor((i-1)/2)=h-ceil(i/2).

Both proofs permit later cuts to split or transport the forest once its
baseline is no longer below the current start. They do not assume that
the forest remains intact throughout the complete inverse.

## 3. The caps characterize the full original-root encoding

Let C_j(x) count Dyck words of height at most j, with C_0=1 and
C_j=1/(1-x C_(j-1)). Let F_0=F_1=1 and F_m=F_(m-1)-x F_(m-2), so
C_j=F_j/F_(j+1).

Consider all tuples of independent forest choices satisfying exactly

    ht(V_j)<=ceil(j/2),
    ht(U_i)<=h-ceil(i/2),              0<=i,j<h.         (5)

Assign degree h+sum ups(V_j)+sum ups(U_i). The original formal peeling
maps height-h roots injectively into these tuples: the terminal is (2),
and the canonical last-height-h inverse recovers the original word
uniquely whenever its admissibility checks pass.

The unrestricted generating function for the tuples in (5) is

    x^h product_(j=0)^(h-1) C_ceil(j/2)
        product_(i=0)^(h-1) C_(h-ceil(i/2)).             (6)

The combined multiset of caps contains h once, each of 1,...,h-1 twice,
and zero once. Consequently (6) equals

    x^h C_h [product_(j=0)^(h-1) C_j]^2
      = x^h/(F_h F_(h+1))
      = C_h-C_(h-1).                                   (7)

The last expression is exactly the generating function for all roots
of height h. Each degree contains finitely many tuples and finitely many
roots. The injection and coefficient equality therefore prove surjectivity.

Thus every tuple obeying the two universal caps (5) passes all canonical
inverse admissibility checks, and the encoding is a bijection. This
conclusion follows from a graded counting argument; the checks have not
been silently discarded during an attempted reconstruction.

## 4. Exact critical product law

At x=1/4, give a forest W with cap m the normalized law

    P_m(W)=4^(-ups(W))/C_m(1/4),
    C_m(1/4)=2(m+1)/(m+2).                              (8)

Choose all V_j and U_i independently with their caps in (5), and reconstruct
the unique original root. By (7), its law is precisely

    P(D)=4^(-semilength(D)) / [C_h(1/4)-C_(h-1)(1/4)],
    C_h(1/4)-C_(h-1)(1/4)=2/[(h+1)(h+2)].              (9)

This is a law on original rooted words with varying semilength. Conditional
on semilength r, it is uniform on roots of height h, but the forest choices
are then coupled by their total size. No product-law assertion is made
for a subsequently reached marked state or for fixed semilength without
that conditioning.

## 5. Exact uninterrupted counting function

The exact suffix characterization already established by record peeling is

    T(D)=h  iff  ht(U_i)<=i for every 0<=i<h.            (10)

Combining (10) with the bijection in Section 3 gives the exact identity

    G_(h,h)(x)
      = x^h product_(j=0)^(h-1) C_ceil(j/2)
          product_(i=0)^(h-1) C_min(i,h-ceil(i/2)).      (11)

This also resolves the inverse indicators in the earlier zero-budget
upper bound: once both universal caps are retained, no further inverse
restriction remains. The earlier upper bounds are still valid.

There is a compact form. Let a,b,c be the three integers differing by
at most one whose sum is 2h+1. Then

    G_(h,h)(x)=x^h/[F_a(x) F_b(x) F_c(x)].               (12)

To check the cap multiset, for j>=1 the number of factors in (11) whose
cap is at least j is

    max(0,h-2j+1)
      + max(0,min(h-1,2h-2j)-j+1)
      = max(0,2h+1-3j).                                (13)

Writing 2h+1=3q+r with r in {0,1,2}, the exponent of C_j is therefore
three for 1<=j<q, r for j=q, and zero above q. Telescoping gives
F_q^(3-r) F_(q+1)^r in the denominator, proving (12).

At critical weight,

    G_(h,h)(1/4)=2/[(a+1)(b+1)(c+1)]
                 ~ 27/(4h^3).                         (14)

This is an equality for the full uninterrupted class; it does not identify
that class with a previously proposed stable-spine cone.

## 6. Where growing-budget defects must be measured

Terminal caps (3) have no defects for any original root, so counting their
violations cannot distinguish B=T-h=0 from B>0. In contrast, the stricter
suffix conditions (10) can fail.

Under the exact product law (8), put M_i=h-ceil(i/2). The indicators
1{ht(U_i)>i} are independent, with probabilities

    q_i=0                                      if M_i<=i,
    q_i=(M_i-i)/[(i+2)(M_i+1)]                  if M_i>i. (15)

This follows by dividing C_i(1/4) by C_(M_i)(1/4). Their joint absence
has the exact probability

    P(T=h)=(h+1)(h+2)/[(a+1)(b+1)(c+1)].                (16)

For a growing-budget argument, a new structural result would have to
relate the actual interruption budget to these original suffix defects,
their excess heights, or another function of the exact independent
original forests. No bound of the form B>=number of defects, no bound
on their total height excess, and no analogous coupling is proved here.
The availability of the product law alone does not establish such a
coupling or a growing-budget density estimate.

## 7. Exact shifted-cap partition, without a budget assertion

For 0<=J<=h, let K_(h,J)(x) count original roots satisfying

    ht(U_i)<=i+J for every 0<=i<h.                       (17)

This is a precisely defined positive family, whether or not it contains
every root with interruption budget at most J. By the product bijection,

    K_(h,J)(x)
      = x^h product_(j=0)^(h-1) C_ceil(j/2)
          product_(i=0)^(h-1) C_min(i+J,h-ceil(i/2)).    (18)

Let a,b,c be balanced integers with sum 2h+1+J. Then

    K_(h,J)(x)=x^h F_J(x)/[F_a(x) F_b(x) F_c(x)].        (19)

For an explicit check, the number N_j of factors in (18) with cap at
least j is

    N_j=2h+1-2j                         for 1<=j<=J,
    N_j=max(0,2h+1+J-3j)                for j>J.         (20)

Thus the cap exponents are two below J and three from J up to the final
balanced truncation. Telescoping produces F_J in the numerator of (19).
Equation (18), rather than the alternating-coefficient numerator alone,
is the positive partition underlying this identity.

At critical weight the formula is particularly simple:

    K_(h,J)(1/4)=2(J+1)/[(a+1)(b+1)(c+1)]
                 =O((J+1)/(h+1)^3), uniformly 0<=J<=h. (21)

The cases J=0 and J=h recover respectively the exact uninterrupted
count and the full height-h count. No statement

    T-h<=J  implies  ht(U_i)<=i+J

has been proved here. Establishing that implication, a weakened version
with a controlled multiple of J, or a counterexample is the remaining
structural step before using (18)-(21) as a growing-budget majorant.
