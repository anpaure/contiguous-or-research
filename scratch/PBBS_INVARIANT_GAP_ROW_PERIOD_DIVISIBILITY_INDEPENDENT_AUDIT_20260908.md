# Invariant gap rows force physical PBBS period divisibility

2026-09-08. Independent pure-proof audit by `exact_b_induction` of the
period-divisibility mechanism in the user's new claims. No mathematical
program was run. Verdict: the finite mechanism passes, including the
synchronous descent through primitive rows. The number-theoretic and
probabilistic estimates using it are separate audits.

## 1. Exact retained inputs and conventions

At pruning level s put

    r_s = semilength after s peak-deletions,
    n_s = 2r_s+1,
    p_s = n_(s+1),
    ell_s = r_s-2r_(s+1)+r_(s+2).

The actual physical one-step map is f, and the original middle-owner
cycle map is g=f^2. All periods here are periods of labelled physical
states, not periods modulo rotation.

The exact one-step equality-particle theorem is
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md:1175`, Theorem 14.1,
with persistent positions and their skew update at line 1224. In one
physical f-update, precisely one equality particle advances one physical
edge, no particle passes another, and its recorded bit stays zero while
all other recorded bits are complemented. Thus the recorded word on the
p persistent particle labels receives precisely ONE reduced f-update.
There is no time rescaling in this statement.

The original invariant coordinates and their finite law are in
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`,
sections 1 and 2 (lines 22 and 66). For incoming distance L_j from particle
j-1 to j and differing-recorded-bit indicator epsilon_j, they are

    Z_j=(L_j-1-epsilon_j)/2,
    L_j=2Z_j+1+epsilon_j,
    sum_j Z_j=ell_s.

The labels here are persistent cyclic labels, anchored at the initial
root. They are not renumbered at a later current root.

When p>=3, the selected particle a has recorded neighbors 0,0,1.
Its move increases L_a and epsilon_a by one and decreases L_(a+1)
and epsilon_(a+1) by one. Other entries do not change. Therefore every
Z_j stays exactly fixed with its persistent index.

For p=1, the single incoming distance is n and its recorded bit is zero;
Z_0=(n-1)/2 is constant. This terminal case is handled directly, since
the two incident-gap updates then refer to the same coordinate.

## 2. A physical return has a uniform cyclic shift of particle labels

Fix one level, writing its circumference as n and particle count as p.
Choose ordered integer lifts at time zero and extend them by

    x_(j+p)(0)=x_j(0)+n.

Lift every later one-edge move positively, preserving this convention.
Suppose the physical binary word returns to itself after t>0 updates.
Its set of equality edges then returns to its old set. Since particles
never overtake, there is one integer m such that, simultaneously for all j,

    x_j(t)=x_(j+m)(0).

The integer m includes complete turns and is not merely a residue modulo
p. To justify its uniformity, list the periodically extended particle
positions in increasing order on the line. At a return they are the same
periodic set; any order-preserving bijection of these indexed lists is
one translation of the indices.

Exactly one particle moves one edge at each update, so

    t=sum_(j=0)^(p-1) [x_j(t)-x_j(0)]
      =sum_(j=0)^(p-1) [x_(j+m)(0)-x_j(0)]
      =n m.

The last identity follows by shifting the index once: the difference
between the sums for m+1 and m is `x_(p+m)-x_m=n`; at m=0 the sum is
zero. Thus m>0 and n divides every physical return time.

## 3. A row's rotational period supplies the additional divisor

At the physical return, the recorded bit on persistent particle j is
the original bit on particle j+m, because the underlying physical word
has returned and their physical edges agree. Likewise its incoming
distance is the original incoming distance at j+m. Hence

    Z_j(t)=Z_(j+m)(0).

Persistent row invariance makes the left side Z_j(0). Let d be the least
positive cyclic shift fixing the row. Its fixing shifts form a subgroup
of the cyclic group of order p, so d divides p and every fixing shift
is a multiple of d. Consequently d divides m. Together with t=nm,

    boxed: n d divides t.

In particular, if the original g-cycle has length v, take t=2v.
Both n and d are odd, so

    boxed: n d divides v.

No primitivity hypothesis is needed for this one-row conclusion. The
row with p=1 has d=1 and gives the same conclusion.

## 4. Why a primitive row permits descent at the SAME time t

If the row is primitive, then d=p. Thus m is a multiple of p. The return
identity strengthens to

    x_j(t)=x_j(0)+(m/p)n.

Every persistent particle has returned to its own physical edge modulo
n. Since the original word also returned, every recorded bit has
returned to its original value on the SAME persistent label j. Therefore
the entire reduced physical word returns at time t.

By Theorem 14.1, this is a return after exactly t reduced f-updates.
It is not a return after t/n or t/p updates. The reduced word need not
have minimal period t; only that t is a genuine return time is used.

The argument can now be applied at the next pruning level with its own
physical circumference, persistent particles, and invariant row.
If the first L original rows are primitive, then for each
`0<=s<L` the same original return time t satisfies

    n_s n_(s+1) divides t,

and the state at level L also returns at that same time. In particular
the original g-cycle period v satisfies

    boxed: lcm_{0<=s<L}(n_s n_(s+1)) divides v.

All these divisors are odd, so passing from t=2v to v loses no factor.
One may NOT replace this least common multiple by the full product
without an additional number-theoretic argument.

## 5. Original finite row law and the meaning of primitive

For a fixed full original pruning profile, row s is a uniform weak
composition of ell_s into p_s parts, and different original rows are
independent. The cited structural source proves this using the exact
inverse-pruning encoding: fixed core bits and the distances L_j uniquely
reconstruct the original cyclic word and its specified root. The number
of such fibres is exactly `binom(ell_s+p_s-1,p_s-1)`, independent of the
particular deeper core once the profile is fixed. Reconstructing from
the bottom upward gives the product law.

This is the ORIGINAL law. No conditioning on a short clock, sampled
edge, reached state, or zero triangle is needed here. Whether a row has
least period d, and in particular whether it is primitive (d=p), is
unchanged by rotating its indices. Thus use of canonical roots for
counting does not alter this event.

When p=1 its only row is primitive with d=1. One may stop descent at
the empty core; extending its one-site zero state adds only trivial
factors one. If ell=0 and p>1, the zero row has d=1 and is not primitive;
it must be included in the exceptional event, rather than silently
treated as having a primitive row.

## 6. Scope and a direct finite interface

For the proved height-adaptive word, its normalized collar overhead is
exactly the state average of `(2h-1)/v`. The one-row result permits the
pointwise upper bound `(2h-1)/(n d)`; on a primitive row this is
`(2h-1)/(n p)`. The iterated least-common-multiple divisor is equally
pointwise. These are legitimate inputs to the proposed moment and
exceptional-profile estimates.

This note certifies the dynamical divisor and finite probability space.
It does not itself certify the claimed polynomial or superpolynomial
error bounds, their constants, or the number-theoretic lower bound for
the least common multiple. Those require their separately reviewed
estimates. Exact equality remains outside this period argument.
