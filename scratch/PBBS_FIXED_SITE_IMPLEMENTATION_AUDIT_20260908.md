# Fixed-site PBBS implementation: analytical and exhaustive audit

2026-09-08. Cover-selectors independent audit. All computation ran via
`ssh h100`, whose reported hostname was `arboghast`. Exhaustive scope:
every rank-r word for r=1,...,5, 636 words total. No sampling or larger
instance was run. Result: PASS, with the phase conventions below.

## Exact forward and inverse rules

Index a cyclic word w by 0,...,n-1, with n=2r+1 and r ones. Define

    S_i=sum_(j=0)^i (2w_j-1).

The omitted site is the FIRST index attaining min_i S_i. These are
AFTER-site prefix sums, and the final value -1 is included. If lambda
is that index, the cyclic sequence immediately AFTER lambda is a Dyck
word D. Indeed prefixes not crossing the array seam follow from global
minimality. A crossing prefix has value -1-S_lambda+S_i with i<lambda;
first attainment and integrality give S_i>=S_lambda+1, hence nonnegativity.
The total is zero. Repeated literal cyclic 10-pair deletion cancels D
and leaves exactly lambda, establishing the cancellation convention.

One PBBS step is

    f(w)_i = 0 if i=lambda, and 1-w_i otherwise.       (1)

It has r ones and is disjoint from w; their sole common zero is lambda.
This is exactly the source rooted-Dyck update 0D -> 0 complement(D).
If D=P 1 Q marks its first maximum-attaining up-step, rerooting (1)
gives

    lambda' = lambda+|P|+1 modulo n,
    D' = complement(Q) 0 complement(P),              (2)

the audited physical skew product of Section 8.1 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md.

For inversion define BEFORE-site sums

    B_i=sum_(j=0)^(i-1) (2w_j-1),  i=0,...,n-1.

The previous omitted site is the LAST index attaining max_i B_i.
It is equivalently the surviving zero under cyclic 01-pair deletion:
reversing the word changes the forward after-prefix sum at the mirrored
site to -1-B_i, so first minimum after reversal means last maximum
before the original site. Complementing at all other sites gives
f^(-1). Thus f is a permutation. The first/last tie conventions and
the distinction between before/after sums are essential.

## Top incoming zero-gap test

The canonical Dyck word ends in zero, so w_(lambda-1)=w_lambda=0.
Represent level-one equality particles by the END indices i of equal
edges (w_(i-1),w_i). The particle at lambda is a zero. Its predecessor
equality particle is also zero: otherwise the alternating suffix after
a last 11 equality would force a negative prefix of the canonical Dyck
word. The incoming distance is therefore 2Z_(0,0)+1. Consequently

    Z_(0,0)=0  iff  w_(lambda-2)=0.                  (3)

Equivalently Z_(0,0) is the number of terminal 10 factors in D. The
verifier extracts the incoming gap from the literal equality particles
and compares it with (3), rather than defining Z by the proposed test.

## Return and repair-edge phases

Let lambda_t be the omitted site BEFORE the update from w_t to w_(t+1).
If its next same-site selection is at time t+g, then g is odd: its bit
is held at zero at the first update, then alternates until it can again
be selected at zero. Define T=(g-1)/2, including the consuming update.
The accepted height-gap theorem gives g>=2height(D)+1, hence T>=height(D).

Use rank-(r+1) owners X_t=complement(w_t). At a birth at time t=2d,
the physical projected edge e has owners

    X_(2e-1) -> X_(2e+1).

The selected coordinate is inserted at e=d, present at the next T+1
owners, and removed at e=d+T+1. Thus the FULL repair trace is precisely

    e=d,d+1,...,d+T+1,                               (4)

with T+2 edges, including insertion and removal. A convention using
X_(2e) -> X_(2e+2) instead must shift the birth/edge phase accordingly.
There is no change to the update (1) itself.

The accepted full-label property says that every physical f-cycle of
length L visits every site, each L/n times. For each fixed site its
successive return gaps sum to L. Summing over sites therefore gives
mean g=n, hence mean newborn T=r exactly, under uniform physical births.
The small verifier checks this property separately on every complete
cycle and checks the exact mean by integer summation.

## Exhaustive evidence and reproducibility

All of the following pass on all 636 states:

- first-after-min versus independent simultaneous cyclic 10 cancellation;
- last-before-max versus independent cyclic 01 cancellation;
- inverse identities, bijectivity, rank, and the unique omitted site;
- agreement with the rooted first-maximum skew product and height invariance;
- incoming-gap extraction versus the two-site top-zero test;
- every same-site return's odd parity and height lower bound;
- full-label cycle census and exact mean T=r;
- all 636 repair traces' insertion, internal residence, and removal phases.

The state counts for r=1,...,5 were 3,10,35,126,462. Exact sums of T
were 3,20,105,504,2310. Python runtime on h100 was 0.0254639639 seconds.

Verifier:
`scratch/verify_pbbs_fixed_site_small_20260908_cover_selectors.py`.
Machine-readable copied output:
`scratch/PBBS_FIXED_SITE_SMALL_AUDIT_20260908.json`.
Remote files remain in `/tmp/pbbs_fixed_site_audit_20260908_cover_selectors/`.
The exact execution command was

    ssh h100 'timeout 60s python3 /tmp/pbbs_fixed_site_audit_20260908_cover_selectors/verify.py > /tmp/pbbs_fixed_site_audit_20260908_cover_selectors/report.json && cat /tmp/pbbs_fixed_site_audit_20260908_cover_selectors/report.json'

This validates the implementation and physical phase convention. It does
not establish any large-r abundance, congestion, or coefficient-one claim.
