# Whole-row reverse law and successive conditioning for the log-gcd route

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No mathematical program was run. Verdict: the whole-row law, primitive
row exception, and tower-conditioning argument pass. The numerical
log-gcd estimate supplying the one-step pass probability is a separate
arithmetic audit, explicitly identified as an interface below.

## 1. Exact whole-row reverse product after marginalizing shallower levels

Work first under the auxiliary measure

    P*(D)=4^(-|D|)/2

on all finite rooted Dyck words. At pruning depth s the exact pushed-forward
law and its inverse-pruning fibres were proved in
`scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`
and
`scratch/PBBS_REVERSE_PROFILE_NB_TAILS_AND_EXISTENCE_ONLY_SMOOTHING_INDEPENDENT_AUDIT_20260908.md`.

Condition on the complete child word at depth s+1, or on the entire
deeper profile. Write

    b=a_(s+1), c=a_(s+2), p=2b+1,
    q=(s+2)^(-2), ell_s=a_s-2b+c.

The exact reverse size law is

    Pr(ell_s=t | deeper)
       =binom(t+p-1,p-1)(1-q)^p q^t,    t>=0.            (1)

Given that sum, the original row Z_s is uniform over the
`binom(t+p-1,p-1)` weak compositions of t into p parts. Consequently
the whole conditional row has the exact mass

    Pr(Z_s=z | deeper)=(1-q)^p q^(sum_j z_j),             (2)

so its p coordinates are independent Geom(q) variables.

This assertion already includes summation over EVERY shallower profile
and decoration: the marginal at depth s is the exact pushed-forward
Boltzmann law. Alternatively, for a fixed child word, each row vector
reconstructs one specified-root parent and its auxiliary weight is
proportional to q^(sum z), directly proving (2). Averaging over child
words of the given deeper profile leaves this same row law.

The indices are the canonical original persistent equality-particle
labels, with the initial-root origin fixed as in the inverse-pruning
encoding. No origin selected using the row's random values is substituted.
Nor does (2) assert independence across depths: their lengths and the
already exposed deeper states change during reverse conditioning.

The terminal child b=c=0 gives p=1 and the same geometric law. Thus
there is no hidden empty-core exception in (1)-(2).

## 2. Exact repetition probability and a uniform primitive-row bound

For a row of odd length p, let e>1 divide p and put d=p/e. The event
that it is e repetitions of a block of length d has exact probability

    [sum_(k>=0)((1-q)q^k)^e]^d
       =[(1-q)^e/(1-q^e)]^(p/e).                        (3)

Since p is odd, e>=3. Here q<=1/4, and

    log of (3)
       =p log(1-q)-(p/e)log(1-q^e)
       <=-pq+(p/e)q^e/(1-q^e)
       <=-pq+pq/24
       <=-2pq/3.                                        (4)

For the penultimate estimate use `q^e<=q/16`, `1-q^e>=1/2`, and e>=3.
A union over at most p possible repetition factors proves

    boxed: Pr(row nonprimitive | deeper)
       <=p exp(-2pq/3).                                 (5)

For p=1 the row is primitive by definition and its failure probability
is zero; no nontrivial repetition factor is included.

Unlike a fixed-sum composition estimate, (3)-(5) concern the ENTIRE
reverse row law. They must be used before imposing a fixed value of a_0
or a shallower regularity/pass event.

## 3. Exact finite interface to the one-step arithmetic bound

Fix a reference integer r>=1, an integer depth L>=1, and let A_j be

    A_j={ .99r/(j+1)<=a_j<=1.01r/(j+1) }.

The reference r remains fixed even though a_0 is random under P*.
Condition on the entire deeper profile at a step `0<=s<L`, and suppose
the exposed b=a_(s+1), c=a_(s+2) satisfy A_(s+1), A_(s+2).
The parent has the full law

    a_s=2b-c+NB(2b+1,q),    q=(s+2)^(-2).

The negative-binomial atom bound in section 3 of the Boltzmann audit is
`max atom<=1/sqrt(pq)`. On the indicated child ranges it gives

    max atom of (2a_s+1)
       <=sqrt((L+2)^3/r).                               (6)

Indeed `pq>=1.98r/(s+2)^3>=r/(L+2)^3`; multiplying the variable by two
and adding one does not change its individual atom masses.

Its ENTIRE support also satisfies

    a_s>=2b-c>=r/[2(s+2)],
    2a_s+1>=r/(L+2).                                    (7)

For the middle inequality, subtract r/[2(s+2)] from the lower estimate
for 2b-c. The numerator is `.47s+2.42`, strictly positive.

The separate log-gcd arithmetic lemma is applied to (6)-(7). Its needed
output, for each fixed integer `1<=v<=exp(L/16)`, is

    Pr(2a_s+1 divides v | entire deeper profile)<=1/2      (8)

uniformly over the indicated b,c ranges. The downstream application
sets `L=floor((r(log r)^2)^(1/5))` on its specified large-r domain.
This note proves the conditioning consequences of (8), not a half-pass
claim for arbitrary small r,L.

The completed arithmetic proof is
`scratch/PBBS_LOG_GCD_DIVISIBILITY_AND_FINITE_REVERSE_TEST_AUDIT_20260908.md`,
with the precise domain `loglog r>=2^20`, the displayed L, and
`1<=v<=exp(L/16)`. Its complete proof was subsequently read for this
audit: the infinite-support residue estimate, logarithmic-gcd argument,
constant 20, and numerical one-half comparison all pass. Thus (8) is
an established input on exactly that finite domain.

## 4. The tower argument: no independence or success-conditioned kernel

Write `F_(s+1)=sigma(a_(s+1),a_(s+2),...)`, and for a fixed candidate v
define

    E_s = intersection_(j=s)^(L+1) A_j
          intersect {2a_j+1 divides v for s<=j<L}.

Thus E_L is just A_L intersect A_(L+1), and

    E_s=E_(s+1) intersect A_s intersect {2a_s+1 divides v}.

The event E_(s+1) is F_(s+1)-measurable and supplies both child ranges
required by (8), including at the final step s=L-1. Therefore

    P*(E_s)
       =E*[1_(E_(s+1))
            P*(A_s and 2a_s+1 divides v | F_(s+1))]
       <=(1/2)P*(E_(s+1)).                              (9)

At each step the A_s restriction is dropped INSIDE the actual full
kernel before (8) is used. Iterating (9) from s=0 through L-1 gives

    boxed: P*(A and 2a_s+1 divides v for 0<=s<L)<=2^(-L),
    A=intersection_(j=0)^(L+1) A_j.                     (10)

No factorization of different tests is asserted. In particular the
reverse kernel is never conditioned on successful shallower tests;
those tests have already been bounded and removed in (9).

## 5. Fixed-size transfer and the primitive exception

Conditioning P* on a_0=r gives the uniform Dyck_r law. The elementary
normalizer bound is

    P*(a_0=r)>=1/Q_r,
    Q_r=2(r+1)(2r+1)<=12r^2.

For (10), first enlarge the numerator by dropping a_0=r and then divide.
This proves, for every fixed candidate v in the range of (8),

    Pr_r(A and all the tests in (10))<=Q_r 2^(-L).        (11)

It does not assert that the reverse NB kernel survives fixed-size
conditioning. The restriction a_0=r is removed before that kernel is
used, not imposed on it.

For a tested row s, the A-range of b alone gives

    pq>=r/(L+2)^3,    p<=3r+1.

Drop a_0=r and all A conditions except this deeper-measurable b-range,
apply (5), then divide by the same normalizer. Union over s gives

    boxed:
    Pr_r(A and some first-L row nonprimitive)
       <=Q_r L(3r+1) exp[-2r/(3(L+2)^3)].                (12)

The bound is finite as written; polynomial-prefactor absorption belongs
to the separate domain/charge audit.

## 6. Where period divisibility is used

For an actual physical PBBS g-period v, primitivity of the first L
original rows implies that each `n_s=2a_s+1`, `0<=s<=L`, divides v.
This is the proved synchronous invariant-row divisor theorem in
`scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`.

Use primitivity only for this deterministic implication. A short-period
event on the good set is then contained in the union of the profile tests
in (10). Drop primitivity when estimating that union under the auxiliary
reverse laws. In particular, no primitive-row conditioning is inserted
in (8) or (9).

There are at most exp(L/16) positive integer candidates in the short
period range. Thus (11) also gives the valid union-bound interface

    Pr_r(A, primitive tested rows, actual v<=exp(L/16))
       <=Q_r exp(L/16) 2^(-L).                          (13)

Only the L divisors at depths zero through L-1 are tested; the additional
depth-L divisor supplied by the theorem is harmless unused information.

## 7. Scope

This note certifies the exact whole-row law after summing shallower
levels, the role of persistent labels, the primitive probability,
the finite NB support/atom interface, all successive conditioning, and
the fixed-size normalization. The arithmetic proof of (8) and the final
explicit word-length rate are separate results. No independence across
depths or fixed-size geometric law has been assumed.
