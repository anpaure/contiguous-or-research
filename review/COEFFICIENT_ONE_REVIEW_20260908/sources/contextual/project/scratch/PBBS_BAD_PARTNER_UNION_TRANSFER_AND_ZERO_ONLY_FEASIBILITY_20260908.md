# Bad-partner union transfer and zero-only exposed feasibility

2026-09-08. Pure proof, no mathematical execution. Root proposed the
incidence-transfer argument and zero-only implication. Direct-route checked
the canonical shifted-triangle identification against the exact original
shift cocycle, the conditional realization, and the uniform growing-depth
raw bound. Root and appendix_a have independently read the complete note
and its two exact original source files: full-file audits PASS.

The main conclusion is that, with probability1-o(1) under actual base-c
incidence, no physical phase in the exposed E_2 environment admits a
feasible POSITIVE row-one sum. Thus the entire J test reduces to the
single physical word C_2^2 T_2. This does not establish abundance of such
phases.

## 1. A general raw-incidence to all-partners union lemma

Work on the full physical PBBS factor, with W=binom(2r+1,r) edges/births.
Fix base cutoff H_c=floor(c sqrt(r)) and the actual retained family

    F_c={GOOD,T<=H_c,Z_(0,0)=0},
    mu_c=(1/W)sum_(b in F_c)(T_b+2)=Theta_c(1).

For any family B_C of physical partner births, let U(B_C) be its occupied
edge union and define its normalized raw incidence by

    mu(B_C)=(1/W)sum_(b in B_C)(T_b+2).

For the canonical root-defined families below, the birth dictionary
identifies this with the corresponding uniform-Dyck-root expectation.
Let A(B_C) be the event that the sampled base-incidence edge meets at
least one trace from B_C. Then

    P_inc,c(A(B_C))
       <=(H_c+2) mu(B_C)/mu_c.                     (1)

Indeed the sampled edge has mass K_c(e)/(W mu_c), where K_c(e) is base
congestion. Its age can only be0,...,H_c+1, with at most one possible
birth per age on its physical cycle. Hence K_c(e)<=H_c+2. Also
|U(B_C)|/W<=mu(B_C). Summing this density over U(B_C) proves(1).
All relevant short traces lie below the physical cycle lengths for large
r; the age bound is the literal physical-incidence bound, not a quotient
or unweighted-root probability.

No independence between base and partner births is used. B_C may contain
arbitrarily many overlapping partners; the bound concerns their UNION.

## 2. Application to actual partners with nonzero triangles

Use the globally defined canonical triangle

    F_S(D)=sum_(s=0)^(S-1)sum_(u=0)^s Z_(s,-u),

with the bottom/repeated-slot conventions of the accepted source
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_uniform_early_triangle_incidence.md`.
For each fixed C, that source proves uniformly over deterministic
integers1<=S<=sqrt(r) that

    mu({T<=H_C,F_S>0})<=A_C S^2/r,
    H_C=floor(C sqrt(r)).                           (2)

Let B_(C,S) denote this full bad partner family. Formula(1) gives

    P_inc,c(A(B_(C,S)))<=A_(c,C) S^2/sqrt(r).        (3)

In particular, with probability1-o(1), EVERY actual C-short partner
covering the sampled edge has zero canonical triangle through any fixed
depth S. For S=2 the error in(3) is O_(c,C)(r^(-1/2)).

The source defines F_S on every root, even outside its distinct-coordinate
sector, and proves(2) globally. Thus(3) is uniform for the displayed
deterministic S range; it does not silently assume a safe genealogy.

The separate growing-depth actual-partner statement is therefore also
valid: if S=S(r)=o(r^(1/4)), then every actual C-short partner covering
the sampled edge has F_S=0 simultaneously with probability1-o(1).
For a literal distinct-slot interpretation impose the profile event
L_C>=max(S,2), where L_C=floor(kappa_C sqrt(r)/A). The accepted base-c
profile tail gives

    P_inc,c(L_C<max(S,2))
       <=A_c exp(-b_(c,C) r/S^2).                  (4)

This common profile is invariant along every physical partner, so the
safe-domain restriction holds simultaneously for all of them. The
statement here concerns ACTUAL partners. No growing-depth existential
fibre realization is inferred merely from(3).

## 3. Exact identity for a shifted partner's canonical triangle

Take the safe depth-two base incidence fibre, retaining its actual law.
Expose E_2=(full profile, all original rows s>=2, sampled offset j).
For each signed physical phase t=2d, put

    a_d=lambda_1(2d),       b_d=lambda_2(2d).

The exact source
`/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`,
Section1 equation(2), identifies the canonical arrays of phi^tD as

    Z^t_(s,u)=Z_(s,lambda_(s+1)(t)+u).              (5)

The same signed physical time is used at every depth. No extra spatial
+1 or time rescaling is inserted. The formula is valid after arbitrary
previous wraps; only the future short clock needs its safe horizon.

Consequently, for the actual physical birth tau^dD,

    F_2(tau^dD)
       =Z_(0,a_d)+Z_(1,b_d)+Z_(1,b_d-1).            (6)

This is an equality of the PARTNER'S CANONICAL triangle, not just an
arbitrary pair of entries in its chronological clock genealogy.
It is the identification needed to apply the original-root bad-sector
estimate to a partner produced by the two-query replay.

## 4. A feasible sum1 creates a bad partner with fixed probability

On the safe fibre, original row-one coordinates0,-1 are forced zero;
the P=p_1-2 remaining coordinates uniformly compose ell=ell_1. Use the
additional exposed regularity event

    P>=8,           1/16<=ell/P<=1/4.               (7)

Its actual-incidence complement is o(1), by the accepted fixed-depth
profile concentration. Bare original GOOD does not itself control r_3,
so(7) is stated separately.

Let W_1(E_2) be the event that some legal candidate phase
d in[j-H_C-1,j] admits row-one sum1 in the exact feasibility test.
If W_1 holds, choose one such phase and a prescribed assignment of
sum1 on its free pair slots using only E_2. The exact stars-and-bars
estimate in
`PBBS_ZERO_OR_ONE_FEASIBILITY_AND_DISTINCT_LABEL_RECIPROCAL_20260908.md`
gives conditional realization probability at least1/125.

After conditioning on the ENTIRE row-one realization, a_d=lambda_1(2d)
is determined. Original row zero is still its independent uniform free
composition, with coordinate0 forced zero. No bounded-query or fresh
reached-root assertion is needed to determine a_d: full row one may
determine it through long prefix sums, while row zero remains unexposed.

If a_d=0, its top gap is forced zero. Otherwise its zero probability is

    (p_0-2)/(ell_0+p_0-2)>=1/2                     (8)

for all sufficiently large original GOOD profiles, since ell_0/p_0->1/3.
Thus, on W_1 and(7), the conditional probability of realizing both
the chosen sum1 and the top gap0 is at least1/250.

The short two-row replay and safe reverse grouping now give an ACTUAL
C-short top-zero partner covering the sampled edge. Profile invariance
preserves GOOD. By(6) its canonical F_2 is exactly1, so it belongs to
B_(C,2). In particular

    P_inc,c(A(B_(C,2))|E_2,safe base)>=1/250

on W_1 intersect(7). If rho_r is the probability of the safe base event,
integration and(3) imply

    P_inc,c(W_1 intersect(7)|safe base)
       <=250 A_(c,C)/(rho_r sqrt(r)).              (9)

Here rho_r->1. Restoring the o(1) profile and safe exceptions proves

    P_inc,c(E_2 admits a feasible sum1)=o(1).        (10)

The selected partner's label can depend on row one, and different
candidate phases can share coordinates. Neither affects this argument:
one E_2-measurable witness is chosen, row one is realized exactly, and
then the still independent row zero is used. The underlying environment
law is never replaced.

## 5. Every positive feasible sum reduces to1

The birth-shift proof in the0/1 note has the following positive-sum
variant. Start with a feasible w>=1 at time t. While w>1 and T_2^2(t)
is at most2j, shift the birth to that later even selection of the same
original D_2 label and reduce w by1. Commutation preserves the endpoint:

    C_2^2 T_2^(2(w-1)+1)(T_2^2(t))
                       =C_2^2 T_2^(2w+1)(t).

Stop at w=1, or at the last even selection before2j. In the latter
case replace the remaining w>1 by1: the endpoint decreases but is
still strictly later than T_2^2(t)>2j. All new durations remain short,
the overlap persists, and the same row-one pair admits the smaller sum.
This proof works for signed births and the inclusive deletion boundary.

Thus existence of ANY feasible positive sum implies W_1. Combining
with(10), with probability1-o(1) EVERY feasible phase admits only sum0.
Consequently, on that event,

    J=J_0,

where J_0 counts exactly the physical phases for which C_2^2 T_2 finishes
within2H_C+1 and covers the sampled edge. Sum0 is feasible on the
composition domain, including the forced pair at the base.

The distinct-label count L from the0/1 note is likewise exactly the
number L_0 of original D_2 labels having such a sum0 physical phase.
Its height-free upper reciprocal estimate therefore applies to L_0
after an o(1) exceptional error. The subsequent note
`PBBS_HEIGHT_FREE_INTERVAL_STABBING_AND_RECIPROCAL_EQUIVALENCE_20260908.md`
proves J_0<=2L_0 by strict alternating-selection interval containment.
Thus J-divergence and L_0-divergence are equivalent without small-height
truncation. The same note proves the two-sided actual reciprocal
comparison 1/(2L_0)<=E[1/K_C|E_2,safe base]<=constant/L_0 on the regular
safe zero-only domain. Neither comparison establishes divergence.

## 6. A separately scoped growing-depth exposed-tail theorem

For deterministic S>=2, define the translated exposed tail at phase d by

    Theta_S(d)=sum_(s=2)^(S-1)sum_(u=0)^s
                    Z_(s,lambda_(s+1)(2d)-u).       (11)

Use the same global conventions as F_S: the height-one row has one
invariant coordinate, and rows beyond the height contribute zero. Thus
(11) is defined even outside the distinct-slot domain. At every nonempty
core the shift is the exact cocycle(5); the one-part conventions handle
the remaining rows.

All of(11) is E_2-measurable. Its original arrays have s>=2, and each
shift lambda_(s+1) is determined by still deeper original data. It has
no dependence on either free upper row. For every full completion,

    F_S(tau^dD)
       =Z_(0,a_d)+Z_(1,b_d)+Z_(1,b_d-1)+Theta_S(d). (12)

Let V_S(E_2) mean that some sum0 feasible physical phase has
Theta_S(d)>0. Choose such a phase from E_2. Realizing its at most two
row-one zeros has probability at least1/125 on(7); then realizing its
top-row zero has conditional probability at least1/2. These are the
ONLY coordinates that need to be assigned, regardless of S. The exposed
positive tail is unchanged by those assignments. Formula(12) therefore
produces a member of B_(C,S) covering the sampled edge with probability
at least1/250.

The argument of Section4 and the uniform bound(3) give, for every
deterministic integer2<=S<=sqrt(r),

    P_inc,c(V_S intersect(7)|safe base)
       <=250 A_(c,C) S^2/(rho_r sqrt(r)).           (13)

The constant is independent of S and of the height. There is no
growing-S free-fibre assignment, nor a fresh law at the shifted root.
Only the already exposed tail is tested, and the same fixed number
of upper coordinates is realized.

Consequently, for every deterministic S=o(r^(1/4)), after the o(1)
regular-profile and base-safe exceptions are restored, with probability
1-o(1) the following hold simultaneously:

* no physical phase admits a feasible positive row-one sum;
* every feasible phase has Theta_S(d)=0;
* every ACTUAL C-short partner covering the sampled edge has F_S=0.

The first two conclusions concern the exposed feasibility problem; the
third is the actual-partner union result(3). They must not be conflated:
an existentially feasible phase can have positive ACTUAL row-one marks
and then fail the short test. Its sampled full triangle need not be zero.
Rather, its exposed tail is zero, and a completion realizing its short
top-zero partner must use upper triangle values zero. In any such
realization, the entire shifted canonical triangle through S is zero.

If distinct slots and nonempty cores are needed for a later physical
genealogy, add the shared profile event from(4). Its complement is o(1)
in this S range. It changes none of the global identities or probability
bounds above.

## 7. Boundary of the result

The remaining exposed-environment question uses only the SINGLE fixed
word C_2^2 T_2 at actual even physical birth phases. The proof removes
positive row-one feasibility with high probability; it does not show
that many zero-sum phases exist.

The all-partner union lemma and the growing exposed-tail theorem retain
their separate quantifiers. Neither supplies a fresh law for the
original D_2 trajectory, turns canonical predecessor labels into physical
births, or proves coefficient one. The zero-only, translated-zero-tail
physical phase sector remains the unresolved abundance problem.
