# Same-particle multiplicity in short PBBS repair congestion

2026-09-07. Root pure-proof deduction; no computation.
The complete note passes independent root and task08 audits. It uses
the accepted physical clock and original-slot identities, not a new
law at a reached root. The bound is an UPPER multiplicity bound; it
does not assert the overlap lower bound needed for shared repair.

## 1. Conventions and the two clock inputs

Let D have semilength r, n=2r+1, and height at least two. In the
original level-one fixed-site process, lambda_1(t) is the omitted
particle label at every signed integer physical time t. For an original
level-zero particle label i let z=Z_(0,i), its invariant incoming-gap
coordinate. A projected birth at index d occurs at physical time2d
and has original particle label lambda_1(2d).

Retain any collection of births with lifetime T<=H, where H<r is an
integer. The consuming update is included in T. Its full repair trace
has edge indices

    d,d+1,...,d+T+1.

We use two already proved clock facts:

1. Selections of adjacent level-one labels i and i-1 strictly alternate.
   Consecutive selections of a fixed label have odd physical-time gaps.
   At a selection of i, the first later selection of i-1 is at an
   even relative time.
2. If lambda_1(2d)=i and T<=H<r, the original return at physical time
   2d+2T+1 is EXACTLY the (2z+2)-nd later selection of i-1.

These facts are in Section3 of task05's
pbbs_gaussian_clock_genealogy_structural_audit.md and Sections1-2 of
task08's pbbs_original_incidence_window_kernel.md. The second fact
uses the strict window2H+1<n, so a full spatial lap cannot win the
first-return race. No such assertion is made for a long birth.

## 2. The exact virtual endpoint bracket

Enumerate all EVEN physical selection times of label i as

    ...,2d_(-1),2d_0,2d_1,...,

with the d_k strictly increasing integers. The full-label property
and finite invertibility provide this bi-infinite enumeration.
Because consecutive selections of i are separated by odd gaps,
these even times are every second selection of i.

Starting from2d_k, let t_k^* be the physical time of the (2z+2)-nd
subsequent selection of i-1, whether or not the corresponding original
birth is short. Strict alternation of i and i-1 implies that t_k^*
falls between the (2z+1)-st and (2z+2)-nd subsequent selections of i.
In particular,

    2d_(k+z) < t_k^* < 2d_(k+z+1).

The first subsequent predecessor selection has even relative time;
its successive same-label gaps are odd. Therefore its even-numbered
selection t_k^* has odd physical time. The integer virtual right
endpoint r_k^*=(t_k^*+1)/2 consequently satisfies

    d_(k+z)+1 <= r_k^* <= d_(k+z+1).                  (1)

For a retained short birth, clock fact2 gives

    r_k^*=d_k+T+1,

its ACTUAL final repair-edge index. Long births are used only to
define the virtual endpoint bracket; their actual return need not
equal t_k^*.

## 3. Congestion contributed by one original particle

At a fixed edge index j, let k_i(z) count retained short births of
original label i whose full trace contains that edge. Then

    k_i(z)<=z+2.                                      (2)

If j is not itself one of the birth indices d_k, the stronger bound is

    k_i(z)<=z+1.                                      (3)

Proof. By (1), any contributing retained interval is contained in
[d_k,d_(k+z+1)]. If j=d_m, containment requires

    m-z-1<=k<=m,

giving at most z+2 indices. If d_m<j<d_(m+1), it requires

    m-z<=k<=m,

giving at most z+1. Lifetime floors or any other removal of births
can only reduce the count. No assumption on disjoint original labels
or independent lifetime tests is used. Square.

This is a bound on unwrapped PHYSICAL births. Repeated rooted shapes
are not identified, and signed-time histories are included. When
H<r, the finite window of births that can cover a given edge has
lengthH+2 below the physical cycle period, so it contains no duplicate
representatives of one physical birth.

## 4. A logarithmic uniform cap outside negligible occupied support

The accepted root profile-concentration theorem permits discarding
bad original profiles at short-support cost at most2W/(n+1)^9.
On every remaining profile, p/n tends uniformly to1/2 and ell/p
to1/3. Conditional on the complete profile, the p original level-zero
slots form a uniform weak composition of ell.

For any slot and integer m>=0, stars-and-bars gives

    Pr(Z_i>=m | profile)
      =binom(ell-m+p-1,p-1)/binom(ell+p-1,p-1)
      <=[ell/(ell+p-1)]^m,                            (4)

with probability zero if m>ell. On good profiles the bracket in
(4) is at most1/2 for all sufficiently large n. Let

    m_n=ceil(14 log_2(n+1)).

Since p<=n, a union bound gives

    Pr(max_i Z_i>=m_n AND profile good)
          <=n/(n+1)^14.

The short-trace support of those exceptional roots costs at most

    (H+2)W n/(n+1)^14 <= W n/[2(n+1)^13].

Together with the earlier bad-profile contribution this is o(W).
Outside it, (2) bounds EVERY original-label contribution by m_n+1.

The maximum of the persistent original slot values is invariant under
the dynamics (canonical rerooting only permutes those values).
This exceptional set therefore also consists of whole physical
components; discarding it leaves congestion unchanged on all retained
good components.

## 5. Scope

The result controls repeated-label multiplicity in the exact original
incidence kernel. It does not show that many DISTINCT labels actually
have an admissible lifetime window at the sampled edge. In particular
(2) is an UPPER bound, not the lower-overlap estimate needed to prove
that the total occupied short-repair support is o(W).

The maximum-slot restriction is used to discard components at directly
bounded cost. It is not silently added to a conditional composition
law or used as a claim that the remaining slots are independent.
