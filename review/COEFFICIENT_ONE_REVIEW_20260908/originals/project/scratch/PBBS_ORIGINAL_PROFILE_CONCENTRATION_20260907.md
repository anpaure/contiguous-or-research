# Quantitative regularity of the original PBBS pruning profile

2026-09-07. Root pure-proof deduction; no computation.
The complete proof passed independent root, task05 and task08 audits.
It addresses the first two ORIGINAL pruning counts, not the law of a
reached root or the short-return trajectory.

## 1. Cyclic equality-edge pruning

For a cyclic binary word w of odd length n>=3, let E(w) be the cyclic
word formed by recording the common bit on each edge whose two bits
are equal, in cyclic edge order. Define

    N_1(w)=|E(w)|,    N_2(w)=|E(E(w))|.

Every cyclic binary word has an even number of unequal edges. Hence
E(w) has positive odd length, and these definitions are unambiguous.
For a one-letter cyclic word its unique self-edge counts as equal.

For a rooted Dyck word D of semilength r, put n=2r+1 and w=0D.
The accepted equality-particle/pruning identity identifies the recorded
word E(0D), up to its root, with 0(partial D), where partial removes
all peaks simultaneously. Applying it twice gives

    N_1=2r_1+1,    N_2=2r_2+1,

where r_j is the semilength after j pruning rounds. This is the sole
PBBS-specific input. It is explicitly proved in Section1 of the
accepted source
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md.

The level-zero composition parameters are therefore

    p=N_1,    ell=(n-2N_1+N_2)/2.                     (1)

## 2. Exact expectations before conditioning

Now take the n bits of w independently and uniformly. Then

    E N_1=n/2,
    E N_2=n/3+epsilon_n,
    epsilon_n=(n/6)4^(-(n-3)/2).                       (2)

The first identity is immediate from the n edges. For the second,
let V be the number of unequal consecutive bits in E(w). Then
N_2=N_1-V.

For a fixed original equality edge at i, suppose the next equality
edge is at i+m, in the forward direction. Their recorded bits differ
exactly when m is even: the m-1 intervening edges are all unequal.
For 1<=m<=n-2 the required two equality edges and intervening unequal
edges prescribe m+2 consecutive bits, up to one free initial bit.
Their probability is 2^(-(m+1)). Only

    m=2,4,...,n-3

contribute to V. The remaining distinct-edge distance m=n-1 would
leave n-2 unequal edges around the original cycle, an odd number,
and is impossible. If there is only one equality edge, its return
to itself gives no unequal adjacency in E(w).

Every unequal adjacency of E(w) is counted exactly once in this way.
Thus

    E V=n sum_(j=1)^((n-3)/2) 2^(-(2j+1))
       =(n/6)(1-4^(-(n-3)/2)),

with the empty sum at n=3. Subtraction proves (2).

## 3. Bounded changes and elementary concentration

Changing a single original bit toggles equality on exactly its two
incident original edges. All other recorded edge bits are unchanged.
Thus E(w) changes by at most two cyclic insertions/deletions.

One insertion or deletion in a cyclic binary word changes its number
of equal adjacencies by at most one. Indeed inserting x between a,b
changes that count by

    1_{a=x}+1_{x=b}-1_{a=b},

which is +1 or -1 for binary symbols. The same bound holds for the
empty and one-letter intermediates: the empty edit-intermediate has
equal-adjacency count zero, and a one-letter cycle has count one.
Therefore changing one original bit changes EACH of N_1,N_2 by at
most two.

For completeness, exposing independent input bits successively gives
a martingale for either statistic. Each conditional martingale increment
has mean zero and range of length at most two. For a mean-zero variable
of range length c, the log moment generating function has second
derivative equal to a tilted variance, at most c^2/4. Integrating twice
from zero gives log E exp(lambda X)<=lambda^2 c^2/8. Iterating this
bound over the n martingale increments and optimizing lambda gives

    Pr(|N_j-E N_j|>a)<=2 exp(-a^2/(2n)).

A union bound for j=1,2 yields

    Pr(max_j |N_j-E N_j|>a)<=4 exp(-a^2/(2n)).          (3)

No independence between N_1 and N_2 is used.

## 4. Conditioning to the uniform Dyck root

The event that w is exactly 0D for some Dyck_r word has probability

    Cat_r/2^n >= 1/[2(r+1)n].

Indeed Cat_r=binom(2r,r)/(r+1), and the largest of the n binomial
coefficients in the sum4^r is at least4^r/n. Conditional on this
event, D is uniform. Thus (3) gives the finite bound

    Pr_D(max(|N_1-n/2|,|N_2-n/3-epsilon_n|)>a)
        <=8(r+1)n exp(-a^2/(2n)).                     (4)

Let

    a_n=sqrt(24n log(n+1))

and let BAD denote the event in (4) with a=a_n. Since r+1=(n+1)/2,

    Pr_D(BAD)<=4n/(n+1)^11<=4/(n+1)^10.               (5)

On the complement,

    |p-n/2|<=a_n,
    |ell-n/6|<=(3/2)a_n+epsilon_n/2.

In particular, uniformly on these good profiles as n tends to infinity,

    p/n=1/2+O(sqrt(log n/n)),
    ell/p=1/3+O(sqrt(log n/n)).                       (6)

The centering epsilon_n in the finite statement is retained; it
decays exponentially and causes no asymptotic loss.

## 5. Discarding bad profiles without an unknown normalizer

Use the physical PBBS convention in which a retained repair trace
has T+2 edges, and the full physical factor has W=n Cat_r births.
Fix ANY integer cutoff H<r and retain any specified subclass of
births with T<=H. Let U_BAD be the union of its traces whose ORIGINAL
root profile is BAD. Counting trace incidences gives

    |U_BAD|/W
       <= E_D[(T+2)1_{T<=H}1_BAD]
       <= (H+2)Pr_D(BAD)
       <= 4(r+1)/(n+1)^10
       = 2/(n+1)^9.                                 (7)

This bound holds before normalizing an incidence probability law,
and regardless of how rare the retained subclass is. Additional
restrictions on the birth event only make the bound smaller.

Hence the occupied-support problem for Gaussian-short repairs,
including the residual B>J_r sector, may discard BAD original
profiles at o(W) cost. On all remaining profiles p is linear in r,
ell/p tends uniformly to1/3, and every H=o(r) satisfies H=o(p).
These are exactly the profile assumptions of the original-slot
geometric limit in the finite incidence kernel.

If the full retained raw-incidence normalizer mu tends to zero,
its occupied support is already o(W). Otherwise, on subsequences
where mu>=epsilon>0, (7) also makes BAD incidence probability o(1).
There is no need to claim that normalized incidence profiles are
typical uniformly when mu is arbitrarily small.

This does NOT make the deeper arrays typical under their incidence
weight, control the predecessor-visit intervals, prove growing-lag
independence, or bound the remaining product mu E_inc[1/K].
It removes the first-level profile-conditioning issue only.

## 6. Restriction preserves congestion on good components

The accepted original pruning profile is invariant under the physical
PBBS dynamics, including the root shift tau. Thus GOOD and BAD profiles
occupy disjoint physical components. For any retained birth family A,
its edge congestion satisfies the exact identity

    K_(A intersect GOOD)(e)=1_GOOD(e) K_A(e).

In particular discarding BAD components does not change the congestion
of any retained good incidence. This is stronger than merely bounding
the difference of the occupied unions.

For the following slot-limit conclusion, SPECIALIZE the retained family
to A={m(profile)<=T<=H}, where m>=height is profile-measurable. All-short
births use m=height; the residual B>J_r family uses m=height+J_r+1.
Additional restrictions may inspect the conditioned environment below,
but not extra level-zero slot values. The slot conclusion is not claimed
for an arbitrary subclass A from the preceding paragraph.

For H=o(r), the uniform conditional original-slot lemma in task08's
finite incidence kernel now applies throughout GOOD for this family. It gives joint
total-variation convergence to independent geometric variables with
Pr(G=a)=(3/4)(1/4)^a for any FIXED number of distinct nonzero original
level-zero slots selected using only the profile, deeper arrays and
sampled offset j. On subsequences with mu bounded below, (7) shows
that mixing over the actual incidence law preserves this conclusion.
If mu tends to zero, occupied support is already negligible instead.

This statement concerns the selected slot VALUES only. The distribution
of the environment selecting their labels and lifetime-test intervals
is still uncharacterized. It gives no growing-number independence,
fresh reached-root law, or solution of the weighted reciprocal problem.
