# Endpoint lower bounds, periodic-core lift, and set turnover at k19 and k20

2026-09-09. Independent pure-proof audit by `exact_b_induction` of the
latest user claims transcribed by root. No mathematical computation or
literal-word execution was performed by this author. The supplied nineteen-
and twenty-coordinate words have now passed the separately executed
independent forward checker recorded in Section8. Their coverage is not
assumed in the pure proofs below.

## 1. All-rank endpoint lower bound

For a universal word on k>=1 coordinates, fix 1<=s<=k and put

    M_s=binom(k,s),  Lambda_s=sum_(j=1)^(s-1) binom(k,j).

Select one ordinary interval for each rank-s target. Different selected
intervals cannot share a left or right endpoint, and cannot contain each
other: their unions would be comparable equal-rank sets, hence equal.
Thus N>=M_s. Order the intervals by their left endpoints as [l_i,r_i].
Their right endpoints have the same strict order. Writing N=M_s+t gives

    i<=l_i<=r_i<=i+t,       1<=i<=M_s.                 (1.1)

Consequently every valid (t+1)-letter window [i,i+t], i=1,...,M_s,
contains one selected witness. Its union has rank at least s. Every
longer interval contains such a window. Therefore each target of smaller
positive rank must be represented by an interval of length at most t.
Counting these intervals gives

    Lambda_s <= sum_(j=1)^t (N-j+1)
              =t M_s+t(t+1)/2.                        (1.2)

The t=0 sum is empty and equals zero. This handles rank s=1 as well,
where Lambda_s=0. The preliminary N<M_s case has already been excluded.
All valid windows, including both boundary windows, occur in (1.1).

Hence, with tau_s the smallest nonnegative integer satisfying (1.2),

    nu(k)>=max_(1<=s<=k) (M_s+tau_s)=B(k).             (1.3)

This is the existing endpoint theorem in MASTER_HANDOFF Section 2.1;
it does not depend on PBBS, an initialized state, or a cyclic construction.

For the current lower-bound comparisons the critical choices are s=10
in both dimensions. Their rank counts are

    M_19=binom(19,10)=92378,
    M_20=binom(20,10)=2 M_19=184756.

The smaller-rank totals are respectively

    Lambda_19=2^18-1,
    Lambda_20=(2^20-M_20)/2-1.

In each case 2 M_k+3<Lambda_k, excluding t<=2 and proving lower bounds
92381 and184759. These finite comparisons and the maximum over ALL ranks
are independently evaluated with integer arithmetic by the separate
literal checkers. A passing word of the stated length establishes exact
optimality from these lower bounds alone.

## 2. Cyclic width bound and finite periodic recency memory

Let C=(C_0,...,C_(M-1)) be a cyclic word of nonempty subsets of a nonempty
alphabet X, and suppose C is cyclic universal. Cyclic interval witnesses
can always be chosen to have length at most M: the full-period union is X,
and a longer interval has the same full union. At any one cyclic endpoint,
the unions of its last 1,...,M letters form a chain. Thus each endpoint
supplies at most one distinct target of any fixed rank, and

    M>=W(|X|).                                        (2.1)

For each integer t, define P_t to be the recency state after the finite
period window C_(t-M+1),...,C_t, with cyclic indexing. Its prefix deck
is exactly the cyclic suffix deck at phase t. The window contains all
coordinates, so it gives complete recency memory: earlier periods cannot
alter any coordinate's last occurrence or create another suffix union.
Consequently appending C_(t+1) updates P_t exactly to P_(t+1).

The M consecutive states P_t,...,P_(t+M-1) include every phase. Their
prefix decks together cover every nonempty old target. Therefore the
initialized update number satisfies

    lambda_X(P_t)<=M-1.                               (2.2)

The initial state is one of the M states and costs no update in lambda.
The general antichain lower bound gives lambda_X(P)>=W(|X|)-1 for every
complete state P. Hence if M=W(|X|),

    lambda_X(P_t)=M-1 for EVERY periodic phase t.       (2.3)

This is a direct corollary of the retained initialized-state definition
and bound; it is not a claim that every recency state has this optimal
lambda, nor that a width-sized cyclic universal word exists in every
dimension. The actual finite word must still supply that hypothesis.

## 3. Periodic-core lift and all ordinary witnesses

Assume in addition that the linear word

    A=C_0,...,C_(M-1),C_0,...,C_(d-1)                 (3.1)

is universal on X. Here d>=0 and the repeated prefix is understood
periodically if d>M. The existence of cyclic witnesses alone does NOT
imply that (3.1) is linear universal for an arbitrarily prescribed d.

Let z be a new coordinate. Append one singleton bridge and M-1 marked
continuation letters:

    A, {z},
    C_d+{z}, C_(d+1)+{z}, ..., C_(d+M-2)+{z}.          (3.2)

Its length is exactly

    (M+d)+1+(M-1)=2M+d.                               (3.3)

The final complete old state of A is P_(d-1), including when d=0. By
Section 2, this state followed by the M-1 displayed projected updates
covers all old targets as initialized suffix prefixes. Every such prefix
has an ordinary suffix witness in the finite projected history A and its
continuation, because A already contains a full period.

For an initial-state prefix, use its suffix of A followed by {z}. For a
later-state prefix, take its ordinary projected suffix at that later
endpoint and mark the continuation letters. If the suffix lies wholly
in the continuation it already contains z. If it starts in A, its actual
interval crosses the singleton bridge, which adds no old coordinate.
Thus every target T+{z} is represented by an ordinary, nonwrapping
interval in (3.2). The singleton target {z} has its explicit bridge;
all targets without z retain their witnesses inside A.

This proves universality of (3.2). It also explains exactly why replacing
an infinite periodic witness by a finite one is safe: its necessary
past is contained in the last full period already present in A.

For M=1, the marked continuation is empty; the argument still applies.
For d=0, (3.2) is the ordinary trimmed lift of a universal A=C. When
M=W, (2.3) and the existing identity

    Ext_z(A)=1+lambda_X(P_A)

show that the M appended positions are optimal among ALL appended
extensions in which every added letter contains z. They do not establish
optimality among arbitrary interleaved words in the next dimension.

### Prior-art boundary

For 0<=d<=M, (3.1) has literal prefix-suffix border d and length M+d.
The old bordered splice in MASTER_HANDOFF Section 2.2, equations
(2.1)--(2.2), gives length 2(M+d)-d=2M+d, with exactly the continuation
in (3.2). Therefore this finite lift formula is a specialization of the
already retained border-sensitive theorem. Section 2 isolates its useful
initialized consequence at every periodic phase; no new all-dimensional
induction should be credited merely for substituting M=W.

The current user specifies M=92378,d=3,z=524288 and the formula

    A=C+C[:3],
    A+[z]+[C[(3+j)%M] | z for j=0,...,M-2].            (3.4)

Its prescribed length is184759. That formula, its claimed initial masks,
and byte identity with the supplied twenty-coordinate file require the
separate structure/literal verification. They are not inferred from file
length or from this conditional proof.

## 4. Every equal-rank witness is short

Let an arbitrary N-letter word represent M_s distinct rank-s targets,
where M_s>=1. Fix ANY interval [a,b] representing one such target and
include this particular interval in a selection of one witness per
rank-s target. Order the M_s selected intervals by left endpoint. If
[a,b] is the i-th, the same antichain endpoint argument gives

    a>=i,       b<=i+N-M_s.

Thus

    b-a+1<=N-M_s+1.                                   (4.1)

The choice of [a,b] was arbitrary. This bounds every witness, not just a
shortest witness or a previously selected endpoint representative. If
M_s=0, the assertion about such witnesses is vacuous. The proof requires
ordinary linear intervals; cyclic witnesses need a different endpoint
ledger.

Equation (4.1) is an immediate strengthened phrasing of the old endpoint
antichain argument, valid for partial rank coverage as well as universal
words. It should not be conflated with a new target-allocation theorem.

## 5. Turnover for a set of coordinates Q

Fix a nonempty coordinate set Q. Call a position marked if its letter
meets Q. Let m_Q be the number of marked positions, R_Q the number of
marked-to-unmarked transitions, and D_(Q,s) the number of represented
rank-s targets meeting Q. Put t=N-M_s>=0.

Targets with a marked witnessing right endpoint number at most m_Q,
because each endpoint's suffix deck is a chain. For a target with an
unmarked endpoint, let p be the last marked position before that endpoint
j. Any witness meeting Q must contain p: its beginning is at or before
some marked position, hence at or before the last such position p.
By (4.1), its length is at least j-p+1 and at most t+1. Therefore j-p<=t.

For each exit run only its first t endpoints can serve such targets,
and each supplies at most one distinct rank-s target. Hence

    D_(Q,s)<=m_Q+t R_Q.                               (5.1)

The initial unmarked run serves no target meeting Q and is correctly not
counted. When t=0 there are no possible unmarked endpoints of this kind;
the inequality remains valid without division by zero. Reversing the
word gives the same assertion for unmarked-to-marked transitions.

If the word is universal on k coordinates and q=|Q|, deleting all marked
letters leaves a universal word on the k-q remaining coordinates. Indeed
an old witness disjoint from Q had no marked positions in its interval,
so deleting other positions preserves that contiguous witness. Thus

    N-m_Q>=nu(k-q),
    D_(Q,s)=binom(k,s)-binom(k-q,s).

With t=N-binom(k,s), (5.1) becomes the exact claimed set formula

    t R_Q>=nu(k-q)-binom(k-q,s)-t.                     (5.2)

Use binom(a,s)=0 when s>a and nu(0)=0. These conventions cover Q equal
to the full alphabet. Division to get a ceiling bound is permitted only
when t>0. A negative right-hand side imposes no positive run requirement.

## 6. Relation to the stronger paired-endpoint theorem

For singleton Q={z}, the earlier paired-endpoint theorem retained in
`PAIRED_ENDPOINT_CATALAN_RUN_BOUND_INDEPENDENT_AUDIT_20260909.md` gives

    R_z>=max(0,2 binom(k-1,s-1)-N)                    (6.1)

for universal k-coordinate words, by pairing old rank-(s-1) and marked
rank-s targets. It counts entrances equally by reversal.

At the proposed optimal19 length, this gives4859 exits and4859 entrances
per coordinate, stronger than the user's turnover consequence1621.
At a proposed optimal21 length B(21)=binom(21,11)+3, it gives

    R_z>=Cat_10-3,

stronger than the user's5599 consequence. The numerical Cat_10-3 value is
left to the separate exact arithmetic record rather than a new computation
in this audit. Neither inequality obstructs the existence of a suitable
highly interleaved word; each is a necessary transition budget.

For nonsingleton Q, (5.2) remains a valid useful statement in its own
scope. No assertion is made that the singleton paired proof transfers
unchanged to every collection of targets merely meeting Q.

## 7. Independent source review of the fixed literal checker

This author read the entire prepared
`verify_k19_k20_optimal_forward_first_occurrence_20260909.py` before
execution and reported PASS to root and its author `exact_b_finite_frontier`.

For each ordinary start, it orders the first future occurrence positions
of all coordinates and adds all bits arriving at the same position
simultaneously. Those events are exactly the distinct ordinary interval
ORs for that start. The target-indexed arrays are checked at every nonempty
mask. No cyclic extension, suffix recurrence, or imported verifier is used.

Its all-rank lower-bound routine uses integer square roots followed by an
upward correction and checks both the achieved capacity and failure at
the preceding integer. Thus each tau_s is minimal. Whole-run PASS requires
both words to cover their full cubes and to equal the maximum of these
all-rank lower bounds. Started/partial output is not a whole-run PASS.

This is a pre-execution logical review only. Coverage, input hashes,
executed event counts, structural periodicity, and file identity must be
attributed to the separate completed certificates when available.

## 8. Separately executed literal result

`exact_b_finite_frontier` subsequently ran the reviewed checker exactly
once on h100. Both words passed:92381 letters realize all524287 targets
at19, and184759 letters realize all1048575 targets at20. Their lengths
equal the independently evaluated maxima of the all-rank endpoint bounds;
rank10 is the unique maximizer in each dimension. Therefore

    nu(19)=B(19)=92381,  nu(20)=B(20)=184759.

The complete executed certificate is
`K19_K20_OPTIMAL_INDEPENDENT_FORWARD_CERTIFICATE_20260909.md`, and its
input words, reports and all ordinary witness arrays are under
`k19_k20_optimal_forward_20260909/`. Actual event counts were1200848
and2494149, with total measured CPU time1.804267801 seconds. This author
read the completed certificate but did not rerun it. No structural
decomposition claim is inferred solely from that full-cube coverage test.
The exact finite frontier is now through20; equality in every dimension
remains unproved.
