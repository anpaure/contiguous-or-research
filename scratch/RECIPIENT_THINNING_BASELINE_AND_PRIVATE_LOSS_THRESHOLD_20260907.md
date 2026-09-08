# Recipient thinning: the exact baseline and the missing private-loss saving

2026-09-07. Pure finite calculation; no computation. Root synthesis of the
independently checked batching/net ledgers. A separate independent audit
passed after clarifying realization versus expectation and the small-p limit.

Input: the deterministic native-bundle theorem in
`/Users/amir.nuriyev/.codex/worktrees/3ca2/problem/research_round1/round10_native_bundle_greedy_recipient_selection.md`.
For at least m available variable recipient owners per target, d>=2 rails,
and J>=1 allowed cell separations, its guaranteed capture fraction is

    gamma(m)=ceil(m/J)/[J(ceil(m/J)+4d-1)].              (1)

This constructs coherent actual demand bundles at unchanged bank charge.
It does not protect old recipient-only targets. The following comparison
explains precisely why the guaranteed fraction alone gives no improved
constant when applied as an independent-recipient reset of the iid bank.

## 1. Deterministic net ledger and recipient-only old targets

Fix the marked bank and old phases. Account for all fixed and phase-invariant
coverage as guaranteed surviving support, without charging it as fresh gain.
For each remaining old target T let a_T>=1 be its number of current variable
owner frames. Select each frame independently as a recipient with probability
p. The target loses every frozen witness exactly when all a_T current owners
are recipients. Therefore its probability of needing recipient preservation
is p^(a_T), and the expected worst-case old-loss debit is exactly

    U(p)=sum_(old T) w_T p^(a_T).                       (2)

The weights and compared target domain are fixed when taking this expectation.
For any actual chosen new recipient words, the net gain is

    newly covered old-hole weight
       minus old weight with no final surviving witness. (3)

For a realized recipient set R, define D(R) as the total old weight whose
current owners all lie in R. The second term in (3) is bounded by D(R)
pointwise, and E D(R)=U(p). Thus only its EXPECTATION is bounded by (2).
Actual loss can be much smaller if old witnesses are coherently transferred
or resupplied. Treating the debit as fully lost is a sufficient-bound device,
not an assertion about the actual algorithm. All losses at other ranks must
also be charged or preserved.

## 2. Exact iid-phase comparison, without equal owner multiplicities

Now fix the marked bank BEFORE its independent uniform phase draws. Work on
targets with no invariant or fixed witness. Let K_T>=1 be the number of
distinct variable possible-owner frames of T, and write b_d=1-1/d. Across
different frames, T is independently captured with probability 1/d.
Recipient selection remains independent of these phase draws.

For each target the exact probabilities are

    Pr(old hole) = b_d^(K_T),
    Pr(old covered and no frozen witness)
       = [b_d+p/d]^(K_T)-b_d^(K_T).                    (4)

Indeed one possible owner supplies no frozen witness with probability
`p+(1-p)b_d=b_d+p/d`. Subtract the event of having no old witness at all.
Consequently private-old loss divided by old-hole probability is

    [1+p/(d-1)]^(K_T)-1 >= p K_T/(d-1).                (5)

No independence between different targets is needed: weighted expectations
sum these exact per-target identities. In particular if all K_T>=k, the
expected private-old debit is at least `pk/(d-1)` times expected old-hole
weight on that same fixed target family.

## 3. No thinning threshold repairs the coarse fresh-only certificate

An old hole with K possible owners has Binomial(K,p) possible recipients;
conditioning on it being an old hole does not change recipient selection.
For any integer threshold m>=1, (1) obeys

    gamma(m) <= m/(m+4d-1) <= m/(4d-1).

Therefore

    gamma(m) Pr(Binomial(K,p)>=m)
       <= pK/(4d-1),                                  (6)

using `m Pr(X>=m)<=E X`. The same inequality holds for the supremum over
m, even if one optimistically allowed a separate threshold for each target.
It also holds when a common lower bound k<=K is used in the binomial tail.

Compare (6) with (5). The certified fresh-only capture coefficient is smaller
than the full private-old debit coefficient by at least the factor

    (4d-1)/(d-1) > 4.                                 (7)

Thus no choice of independent thinning probability p>0 and threshold m can
make THIS coarse fresh-only guarantee exceed its iid private-old debit.
This does not upper-bound the greedy algorithm's actual gain, reject a
better capture theorem, or forbid coherent old-witness preservation.

## 4. Including old private targets among the new demands

Freeze the nonrecipient words and all invariant support, and optimize every
target absent from that exterior, not just old holes. Conditional on this
exterior and the selected recipient indices, the old recipient phases remain
independent uniform phases. If such a target has r>=m variable recipient
owners, its old capture probability is at least `1-b_d^m`.

But Bernoulli's inequality gives

    gamma(m) <= m/(m+4d-1)
             < m/(m+d-1)
             <= 1-(1-1/d)^m.                           (8)

The last inequality follows from
`(1+1/(d-1))^m >= 1+m/(d-1)`. Hence the same owner-count-only certificate
is weaker than the old iid contribution even when all private old targets
are allowed to be resupplied as part of the new demand family.

The exterior here is independent of the old recipient phase draws: it
contains only nonrecipient actual words and recipient invariants. An
exterior or demand family additionally selected from recipient phase
outcomes would need a new conditional law before using (8).

## 5. Quantitative target for a genuinely better exchange

Equation (7) implies that a uniform guarantee preserving a fraction r of
the otherwise-debited private-old weight would need at least

    r > 1-(d-1)/(4d-1) > 3/4                           (9)

before this coarse fresh-only certificate could possibly become positive
in the iid comparison. This is a necessary calibration for that method,
not a universal necessary condition for improving a word.

More specifically, in a homogeneous intensity regime K/d->lambda>0,
using a guaranteed owner lower bound k/d->kappa<=lambda and fixed J, take
p->0, pk->infinity, and m/(pk)->1 with the lower-tail failure tending to zero.
Then (1) gives
`gamma(m)~p kappa/(4J^2)`, whereas the private-old/hole ratio in (5) is
asymptotic to p lambda. A sufficient saved-loss guarantee must consequently
satisfy `r>1-kappa/(4J^2 lambda)` at this first-order comparison. Strict
slack, realized-debit control, and the actual tail errors are still needed
to turn such a condition into an improved word construction.

For a fixed nonzero p instead, the corresponding limits are
`gamma -> p kappa/[J(p kappa+4J)]` and private-old/hole ratio
`exp(p lambda)-1`; the small-p equivalents must not be used at that scale.

The useful positive batching theorem and this negative calibration are
consistent. The former solves some simultaneous fresh-demand constraints;
the latter shows why the cost of abandoning old coverage cannot be omitted.
