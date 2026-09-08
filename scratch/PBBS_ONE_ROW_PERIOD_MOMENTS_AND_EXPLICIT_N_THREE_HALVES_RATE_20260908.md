# One-row period gain: finite exception bound and explicit n^(-3/2) rate

2026-09-08. Independent pure-proof audit by exact_equality_structure.
No mathematical computation was run for this note. The period-divisibility
proof, the original finite composition law, the pruning census, and the
height-adaptive compiler sources below were read completely through their
relevant proofs. The resulting finite inequality passes.

For odd n=2r+1>=5 write W=binom(n,r), t=2^n/W, and

    beta_n = 4n(n+1)(242/243)^n + n(99/100)^n.

The SAME height-adaptive finite construction already proved satisfies

    nu(n) <= W + floor[(2^(n+2)+2W)/n^2 + W beta_n].        (1)

The floor in (1) encloses the whole sum. In particular,

    nu(n)/W <= 1+(4t+2)/n^2+beta_n
             =1+2sqrt(2pi)n^(-3/2)+O(n^(-2)).              (2)

The exact trimmed one-coordinate lift proves the same normalized bound
in the next even dimension. Thus, in all dimensions,

    nu(k)/W(k) <= 1+2sqrt(2pi)k^(-3/2)+O(k^(-2)).          (3)

This is a stronger analysis of a proved deterministic construction. It
does not prove exact equality with B(k).

## 1. Probability space, finite construction, and dynamical input

A uniform physical rank-r binary word on n=2r+1 sites corresponds to a
uniform Dyck word D of semilength r together with a uniform choice of the
physical unmatched-zero location. This is a bijection: the canonical
matching has exactly one unmatched zero, and rooting there recovers 0D.
In particular W=n Cat_r. Rotation-invariant quantities have precisely
the uniform-Dyck law. There is no weighting by a g-cycle length in the
Dyck probability measure.

Let h be the normalized Dyck height and v the physical period under g=f^2.
The finite word already proved in
PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md
has length W+sum_C(2h_C-1). Its relative collar charge is exactly

    (1/W) sum_C(2h_C-1) = E_state[(2h-1)/v].              (1.1)

The full proof of its all-rank literal coverage and its collars is
retained; this note changes only the estimate on (1.1).

Write N_s for the number of sites after s cyclic equality-pruning rounds,
so N_s=2r_s+1 on 0D. At the first row put

    p=N_1=2r_1+1,
    ell=r-2r_1+r_2=(n-2N_1+N_2)/2.

Its invariant incoming-gap vector Z is a weak composition of ell into p
parts. Conditional on the complete original pruning profile, it is uniform
over all

    D_count=binom(ell+p-1,p-1)                            (1.2)

such vectors. This is the ORIGINAL inverse-pruning fibre, not a reached
state, a short-clock conditioning, or an incidence-weighted fibre.
The exact encoding and its uniform law are proved in
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md,
Sections 1 and 2. That proof was read for this audit.

If d is the least cyclic period of Z, the independently proved dynamical
divisibility theorem gives

    nd divides v.                                        (1.3)

See PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md,
which was read in full. In particular v>=n always; if the row is
primitive, d=p and v>=np. The all-zero row with p>1 is nonprimitive and
is included in the exception below. No full-product divisibility across
multiple levels is assumed.

## 2. Uniformly small exceptional probability

For independent fair input bits on an odd n-cycle, the exact pruning
census gives

    E_iid N_1=n/2,
    E_iid N_2=n/3+4n/(3*2^n)>=n/3.                        (2.1)

Changing any one original bit changes either N_1 or N_2 by at most two.
The bounded-difference inequality therefore gives

    Pr_iid(|N_s-E_iid N_s|>a)<=2 exp(-a^2/(2n)),  s=1,2.  (2.2)

Both facts are proved in PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md,
Sections 2 and 4. Section 7 below also checks them by a direct two-level
argument, without using the deeper census formula.

The event that the iid word is exactly 0D for some Dyck_r word has
probability

    Cat_r/2^n >= 1/[n(n+1)].                              (2.3)

Indeed the largest of the 2r+1 binomial coefficients of order 2r is at
least their average, so binom(2r,r)>=2^(2r)/(2r+1).
On conditioning on the event in (2.3), D is uniform.

Call a profile regular if both deviations in (2.2) are at most n/11.
A union bound and (2.3) give

    Pr_D(nonregular)
      <=4n(n+1) exp(-n/242)
      <=4n(n+1)(242/243)^n.                              (2.4)

The last comparison follows from exp(1/242)>=243/242. No additional
conditioning on rank, a root orbit, or a cycle is required.

On every regular profile,

    p>=n/2-n/11=9n/22,

    ell=(n-2N_1+N_2)/2
        >=[n-2(n/2+n/11)+(n/3-n/11)]/2=n/33.             (2.5)

As n>=5, also p-1>=n/33: indeed 9n/22-1-n/33=25n/66-1>=0.
Consequently (1.2) obeys

    D_count>=2^(n/33).                                   (2.6)

For completeness, with q=ceil(n/33), both ell and p-1 are at least q;
therefore D_count>=binom(2q,q)>=2^q. The last inequality counts the
q-subsets obtained by choosing one member from each of q disjoint pairs.
This proof is also recorded by the finite-frontier audit in
PBBS_BETA_EXACT_THRESHOLDS_AND_COMPOSITION_COUNT_20260908.md.

Fix one regular full profile. Since p is odd, a nonprimitive length-p
row consists of j>=3 repetitions for some divisor j of p. If j does
not divide ell there are no such rows. Otherwise their number is

    D_j=binom(ell/j+p/j-1,p/j-1).

Concatenating j independently chosen compositions of ell/j into p/j
parts injects a set of size D_j^j into the full composition set of size
D_count. Hence D_j<=D_count^(1/j)<=D_count^(1/3). A union bound over
at most p possible divisors gives, still at that same fixed profile,

    Pr(nonprimitive | profile)
      <=p D_count^(-2/3)
      <=n 2^(-2n/99)
      <=n(99/100)^n.                                    (2.7)

To verify the last elementary comparison, (100/99)^99<e<4 implies
100/99<2^(2/99). The profile event in (2.5) depends only on the full
pruning profile, so retaining it does not change the conditional row law.
Averaging (2.7) over regular profiles and adding (2.4) proves

    Pr_D(nonregular OR nonprimitive)<=beta_n.             (2.8)

It is harmless that beta_n exceeds one in small dimensions. The finite
inequality is still valid there. Empty/pruned terminal cores introduce
no gap: on the regular event ell>0 and p>1, while excluded cases are
already charged through (2.4) or (2.7).

## 3. Exact first and second height moment bounds

For a uniform physical rank-r word, write the +/-1 linear walk from
0 to -1 as S_0,...,S_n, with maximum M and minimum m. The established
pointwise comparison is h<=M-m. Reflection gives

    Pr(M>=a)=binom(n,r-a)/W,
    Pr(-m>=a)=binom(n,r+1-a)/W,   a>=1.                  (3.1)

Summing the tails gives E(M-m)=t-1. Therefore

    E(2h-1)<=2t-3.                                      (3.2)

Summing with weights 2a-1 instead gives the EXACT formulas

    E M^2=r+2-t,
    E(-m)^2=r+1.                                        (3.3)

Here is a direct telescoping verification. For the first numerator,
substitute j=r-a in (3.1) and use

    (n-2j)binom(n,j)
      =n[binom(n-1,j)-binom(n-1,j-1)].

Then

    sum_(j=0)^(r-1)(2r-2j-1)binom(n,j)
      =rW-2(2^(n-1)-W)=(r+2)W-2^n.

For the second numerator, j=r+1-a gives

    sum_(j=0)^r(n-2j)binom(n,j)
      =n binom(n-1,r)=(r+1)W.

Consequently

    E h^2<=2E M^2+2E(-m)^2
           =2n+4-2t<=2n,                               (3.4)

because t>=2: the two equal middle binomial coefficients are disjoint
terms in the sum 2^n. These averages legitimately bound the same h used
in the uniform-Dyck calculation, since h is rotation invariant. No
independence between height and the pruning counts is asserted.

## 4. Exact peak moments and the denominator correction

Let K be the number of peaks of a uniform Dyck_r word. The Narayana
count is

    #{D:K=k}=(1/r)binom(r,k)binom(r,k-1).

After normalization, K-1 has the hypergeometric distribution obtained
by choosing r-1 elements from two classes each of size r and counting
one class. Indeed its mass at j is

    binom(r,j)binom(r,r-1-j)/binom(2r,r-1).

The elementary hypergeometric first and second moments yield

    E K=(r+1)/2,
    Var K=(r^2-1)/[4(2r-1)].

Since p=n-2K,

    E p=r,
    Var p=(r^2-1)/(2r-1),
    E(p-n/2)^2=(r^2-1)/(2r-1)+1/4<=n/3.                (4.1)

For the last inequality, multiply by 12(2r-1): the difference between
the right and left numerators is 4r^2-6r+11>0. The formulas are valid
already for r=1; the stated n>=5 domain has no exceptional denominator.

On p>=9n/22, an exact algebraic rearrangement gives

    1/p = 2/n - 2(p-n/2)/(np)
         <=2/n+[44/(9n^2)]|p-n/2|.                     (4.2)

Let G be the event that the profile is regular and its first row is
primitive. Because 2h-1 is positive, (3.2), (3.4), (4.1), and
Cauchy-Schwarz give

    E[(2h-1)/p;G]
      <=(2/n)E(2h-1)
        +[44/(9n^2)]sqrt(E(2h-1)^2 E(p-n/2)^2)
      <=(4t-6)/n + [88sqrt(2/3)/9]/n
      <=(4t+2)/n.                                      (4.3)

The last numerical step is strict: 88sqrt(2/3)/9<8 is equivalent to
2/3<81/121, or 242<243. In the preceding step E(2h-1)^2<=4E h^2<=8n.
There is no conditioning of the moments or unsupported decoupling.

## 5. Finite charge, rounding, parity, and asymptotics

On G, (1.3) gives v>=np. Everywhere v>=n and 2h-1<=2r-1<n.
Thus (1.1), (2.8), and (4.3) give

    (1/W)sum_C(2h_C-1)
       <=(1/n)E[(2h-1)/p;G]+Pr(G^c)
       <=(4t+2)/n^2+beta_n.                             (5.1)

The collar sum is an integer. Multiplying (5.1) by W and flooring the
whole right side proves (1). It would not justify flooring only the
main rational term while leaving W beta_n outside the floor.

Let F_n denote the integer floor in (1). The retained exact one-coordinate
lift gives

    nu(n+1)<=2W+2F_n,
    W(n+1)=2W.

Hence (5.1) is the normalized bound for both n and n+1. For a convenient
all-k formula take n=k when k is odd and n=k-1 when k is even.

Stirling's estimate t=sqrt(pi n/2)(1+O(1/n)) turns (5.1) into

    relative excess <=2sqrt(2pi)n^(-3/2)+2n^(-2)
                       +O(n^(-5/2))+beta_n.

The explicit beta_n decays exponentially and n=k+O(1), proving (2)-(3).
The finite construction and all-rank coverage are unchanged; no growing
parameter choice or asymptotic diagonalization enters this conclusion.

## 6. Monotonicity and the separately certified threshold comparisons

Put R(n)=(4t+2)/n^2+beta_n for odd n. The width ratio gives

    t_(n+2)=t_n(n+3)/(n+2).

Therefore t_n/n^2 strictly decreases under n to n+2, since

    (n+2)^3-n^2(n+3)=3n^2+12n+8>0.

The term 2/n^2 also decreases. For the first beta summand
B(n)=4n(n+1)(242/243)^n, its exact ONE-step ratio is

    B(n+1)/B(n)=(242/243)(n+2)/n<=1
       if and only if n>=484.

Equality occurs only at n=484, so this summand strictly decreases at
every integer step from n>=485. For the second summand
C(n)=n(99/100)^n, the exact one-step ratio is

    C(n+1)/C(n)=(99/100)(n+1)/n<=1
       if and only if n>=99,

with equality only at n=99. Hence both beta summands decrease strictly
along the odd dimensions n>=485. Combining this with the strict
two-step decrease of the main term proves that R(n) strictly decreases
on the odd dimensions n>=485. The exact
h100 rational comparisons, independently recorded in
PBBS_BETA_EXACT_THRESHOLDS_AND_COMPOSITION_COUNT_20260908.md, are

    R(5641)>0.01>R(5643),
    R(6253)>0.001>R(6255).

Combining those already executed finite checks with the pure monotonicity
proof and the exact parity lift yields

    nu(k)<1.01 W(k)   for every k>=5643,
    nu(k)<1.001 W(k)  for every k>=6255.                  (6.1)

These are thresholds for this explicit upper envelope, not a statement
about the first dimension at which the unknown optimal ratio crosses
either value. This audit ran no new threshold computation.

## 7. Direct checks of the two-level census inputs

The simple two-level inputs (2.1)-(2.2) can be checked without the full
Chebyshev calculation. The first equality count N_1 has mean n/2, since
each physical edge has equal endpoint bits with probability one half.

For N_2, root at a physical equal edge and locate the next equal edge.
If its clockwise distance is d<n, the recorded endpoint colors agree
exactly when d is odd. For d=1,3,...,n-2, the probability that these are
consecutive equal edges is 2^(-(d+1)); the intervening d-1 edges must
be unequal. If it is the only equal edge, the distance is n and the
probability is 2^(-(n-1)); it contributes an equal self-edge to N_2.
Summing over the n possible starting edges gives

    E N_2/n
      =sum_(j=0)^(r-1)2^(-(2j+2))+2^(-(n-1))
      =1/3+4/(3*2^n),

which is exactly (2.1), including the singleton-particle case.

For the Lipschitz bound, flipping one original bit has two possible
effects on the first equality-particle record. If its two neighbors
are equal, it inserts or deletes a consecutive pair of particles of
the same color. In the second equality count this changes at most two
equal adjacencies. If its neighbors differ, precisely one particle
moves and its recorded color flips; again at most two adjacencies change.
The one-particle self-edge is unchanged in the latter case. Thus
|Delta N_2|<=2 directly, and |Delta N_1|<=2 is immediate. Applying the
ordinary bounded-difference proof to the independent original bits
establishes (2.2), with the same constant as the cited source.

## 8. Scope of this independent audit

The deterministic nd divisibility is credited to the separately audited
invariant-gap-row theorem; the height-adaptive literal compiler is retained
from the earlier complete proof. This note verifies their probability-space
interface, every exceptional-probability normalizer, the exact moment
formulas, the denominator estimate, the finite floor, the odd/even passage,
and the displayed polynomial rate. Neither a complete product of period
factors nor a quantitative multilevel least-common-multiple estimate is
used or certified here. Such a stronger claim needs its own proof.
