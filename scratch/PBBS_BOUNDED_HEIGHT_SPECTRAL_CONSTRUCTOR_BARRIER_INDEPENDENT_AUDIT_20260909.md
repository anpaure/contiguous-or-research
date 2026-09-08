# Bounded-height spectral lower bound for the native constructor's overhead

2026-09-09. Independent pure-proof audit by `exact_b_finite_frontier` of
the user's new constructor-barrier formulas, as relayed in this task.
No enumeration, numerical calculation, or mathematical program was run.
The claims below pass with the stated domain and constructor scope.

Write n=2r+1 with r>=1, W=binom(n,r)=n Cat_r, and let N_native be the
unchanged height-adaptive PBBS word with a collar of length 2h-1 at
every owner cycle of height h. Put C=N_native-W. The inherited exact
identity is

    C/W = E_states[(2h-1)/v].                           (1)

This is a claim about that specified constructor, not a lower bound on
the optimum nu(n). In particular, the independently verified exact17
and exact18 words do not lie under a claimed impossibility result here.

## 1. The height product is an upper bound on the actual period

Use the physical f-update and persistent labels from
[the exact translated-return proof](PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md).
At one parent level of length n_s, its child has p=n_(s+1) sites and
least physical period F_child. A physical return time of a nontrivial
level is a multiple of its circumference: equation(2.1) of that proof
with translation K=0 gives T=n_s m. Thus p divides F_child; for p=1
this also holds, with F_child=1.

Apply that same equivalence with

    T=n_s F_child, K=0, m=F_child.

The invariant row's period d divides p, hence divides m. The child
returns at T, and rotation by -m is the identity on its p sites.
All three requirements of the one-level equivalence therefore hold.
The parent's least period F_s divides this exhibited return time:

    F_s | n_s F_child.

Iterating from the one-site bottom proves

    v | product_(s=0)^(h-1) n_s,   v <= n^h.            (2)

All these periods are odd by the exact denominator formula, so the
owner map g=f^2 has the same period. No acceleration of the child clock,
row primitivity, or coprimality of different circumferences was used.

## 2. An explicit contribution from height two

There is one normalized root of height one and one physical cycle of
length n arising from it. Its collar contributes1.

A height-two profile is (m_0,m_1)=(r-b,b), with
1<=b<=floor(r/2). Its child circumference is p=2b+1; its top incoming
row has mass r-2b. The exact rooted inverse-pruning count is

    binom((r-2b)+(2b+1)-1,(2b+1)-1)=binom(r,2b).

The bottom row is unique. Thus this profile contains n binom(r,2b)
physical states. By (2), every cycle in it has period at most n(2b+1),
so its number of cycles is at least binom(r,2b)/(2b+1). Summing first,
then using that the total number of such cycles is an integer, yields

    #height-two cycles >= ceil(sum_(b>=1) binom(r,2b)/(2b+1))
                        = ceil(2^r/(r+1)-1).           (3)

For the identity, binom(r,2b)/(2b+1)=binom(r+1,2b+1)/(r+1), and the
sum of the odd binomial coefficients of r+1 is 2^r. The omitted b=0
term is1. Each height-two cycle contributes3, so

    C >= 1+3 ceil(2^r/(r+1)-1).                        (4)

The empty height-two sum at r=1 is0, and (4) remains correct. This
argument uses the varying child circumference in each profile; replacing
all of them by r+1 before summation would give a weaker estimate.

## 3. Spectral bounded-height count

Let D_(r,H) be the number of Dyck paths of semilength r with maximum
height at most the integer H>=1. These are walks of length2r from0
to0 on the path graph with vertices0,...,H. Diagonalizing its adjacency
matrix gives

    D_(r,H) = 2/(H+2) sum_(j=1)^(H+1)
        sin^2(pi*j/(H+2)) [2 cos(pi*j/(H+2))]^(2r).

Every summand is nonnegative. The distinct terms j=1 and j=H+1
have equal values. Retaining them proves, for r>=1,H>=1,

    D_(r,H) >= 4/(H+2) sin^2(pi/(H+2))
                       [4 cos^2(pi/(H+2))]^r.         (5)

The factor4 requires both extreme eigenvalues; the even walk length
makes their contributions have the same sign. Formula(5) is also valid
at H=1. No statement is needed at H=0 or r=0.

There are exactly n physical states per normalized root. On the states
counted by D_(r,H), one has h<=H, 2h-1>=1 and v<=n^H. Restricting
the nonnegative expectation in (1), and using Cat_r<=4^r, gives

    C/W >= D_(r,H)/(Cat_r n^H)
        >= 4/(H+2) sin^2(pi/(H+2))
                         cos^(2r)(pi/(H+2)) n^(-H).   (6)

## 4. Optimize the bound and check the additive conclusion

Take an integer H nearest (2*pi^2*r/log n)^(1/3). For all sufficiently
large r it is positive and tends to infinity. Taylor's formula for
log cos x at0, and the polynomial size of the prefactor in (6), give

    log(C/W) >= -H log n - pi^2*r/H^2
                + o((n(log n)^2)^(1/3)).

Replacing H+2 by H, or rounding H, affects only the displayed smaller
order term. Minimizing the two leading terms at the chosen H yields

    C/W >= exp[-(3*pi^(2/3)/2+o(1))
                         (n(log n)^2)^(1/3)].         (7)

Here n=2r+1, so the factor2 in the optimizing H cancels when the
leading constant is written in terms of n. This is the claimed
constant; the logarithm is natural.

For completeness, the notation N_native-B(n)=2^(n-o(n)) needs an upper
as well as a lower estimate. The lower estimate follows from (7),
log W=n log2-O(log n), and B(n)-W=O(sqrt(n)): the latter subtraction
is negligible beside C. For the upper estimate, n divides v and
h<=r imply

    (2h-1)/v <= (2r-1)/(2r+1) <1.

Thus C<W, N_native<2W<=2^n for odd n, the last inequality following
from the two disjoint central ranks. Consequently, for sufficiently
large odd n,

    log_2(N_native-B(n))=n-o(n),

which justifies the stated exponential notation. The literal even
doubling has twice the odd collar overhead and the same conclusion
after replacing n by n+1; its endpoint-bound excess is still only
O(sqrt(n)). The logarithm of a possibly nonpositive small-dimensional
difference is not asserted.

## 5. What is stronger, and what remains unchanged

The [earlier corner-period barrier](PBBS_CORNER_PERIOD_UPPER_BOUND_AND_EXPONENTIAL_COLLAR_BARRIER_AUDIT_20260908.md)
already proved the same leading exponential additive conclusion using
a penalty O(sqrt(n) log n). The present bounded-height argument improves
that penalty to an explicit leading constant times
(n(log n)^2)^(1/3), and (4) supplies a separate explicit height-two
lower bound. It does not newly show that the native constructor has an
exponential additive gap: that conclusion was already recorded.

The corner bound can still be stronger than n^h on individual profiles;
the improvement here comes from averaging the explicitly counted
bounded-height subfamily. None of (4), (7), or the additive conclusion
rules out collar trimming, changing the cycle source, capping, fusion,
initialized continuations, or an exact word from another constructor.
