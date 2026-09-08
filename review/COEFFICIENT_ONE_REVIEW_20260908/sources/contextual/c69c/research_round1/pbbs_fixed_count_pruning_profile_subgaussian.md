# Fixed-count pruning profiles without a conditioning prefactor

Date: 2026-09-08. Pure finite proof; no computation or original-project
edits. The worktree lead proposed the coupling and slice-exposure route;
the proof below passed an independent local derivation and complete-file
reviews by the worktree lead and the independent recency reader.

Let D be uniform among Dyck roots of semilength r>=1, let
r_s=|partial^s D|_up, and put n=2r+1. Uniformly over ALL integers s>=0,

    Pr(|r_s-r/(s+1)|>4sqrt(r)+x)
       <=2exp[-x^2/(6r)],               x>=0,          (1)

and

    E exp[t|r_s-r/(s+1)|/sqrt(r)]
       <=16exp(4t^2),                  t>=0.          (2)

These are original-root laws. The constants do not depend on s.
Equation (2) concerns each depth separately; it is not a moment bound
for the supremum over depths. No new short-incidence or overlap bound
is asserted here.

## 1. Two accepted finite inputs

For an arbitrary cyclic binary word w, let E(w) record the common bit
on each equality edge, and put N_s(w)=|E^s(w)|. On odd length n, every
iterate has positive odd length. For w=0D,

    N_s(0D)=2r_s+1.                                    (3)

The accepted depth-uniform edit bound says that changing one bit changes
N_s by at most two, for every s>=1. At s=0 the length is constant.
Thus changing k input bits changes every N_s by at most 2k.

For n iid fair input bits, the exact all-depth census and its Gaussian
sum bound give

    E_iid N_s=n/(s+1) sum_(j=0)^s
                    cos^(n-1)(pi j/(s+1)),
    0<=E_iid N_s-n/(s+1)<=2sqrt(n),       s>=0.         (4)

The s=0 case is exact. These inputs, including the uniform expectation
bound, are proved in the read-only root notes
PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md and
PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md.

## 2. Couple iid bits to the uniform fixed-count slice

Let W have iid fair bits and let K be its number of ones. Construct
W_bal with exactly r ones as follows. If K>r, choose K-r of its one
positions uniformly and flip them to zero. If K<r, choose r-K zero
positions uniformly and flip them to one. If K=r, make no change.

Conditional on each value of K, this construction is invariant under
every permutation of the n coordinates. Its output has exactly r ones,
so W_bal is uniform on that slice. The edit bound gives simultaneously
at all depths

    |N_s(W_bal)-N_s(W)|<=2|K-r|.

Since K has mean r+1/2 and variance n/4,

    2E|K-r|<=2sqrt(E(K-r)^2)=sqrt(n+1).

Taking expectations and using (4) proves

    |E_bal N_s-n/(s+1)|<=2sqrt(n)+sqrt(n+1),
                                               s>=0. (5)

No conditioning by the probability of the balanced slice is used.

## 3. Concentration directly on the slice

Fix s and expose the coordinates of a uniform r-ones word in order.
Consider a prefix after which m positions remain, with k ones still to
place. If both values of the next bit are possible, then 0<k<m.

The completion with next bit one has a uniform (k-1)-subset U of the
remaining m-1 positions. Choose a uniformly random position J outside U
and set V=U union {J}. Then V is a uniform k-subset: every V has exactly
k preimages (U,J), with the same weight. Pair the completions

    next bit 1, suffix U;
    next bit 0, suffix V.

They differ in exactly one swap, hence in two bits. Their N_s values
differ by at most four. Therefore the two conditional expectations at
this exposure differ by at most four. If only one next bit is possible,
the increment is zero.

The Doob martingale increments consequently have conditional range
length at most four. The bounded-range log-MGF inequality yields

    E_bal exp[lambda(N_s-E_bal N_s)]
       <=exp(2n lambda^2),              lambda in R.

Optimizing lambda gives

    Pr_bal(|N_s-E_bal N_s|>y)
       <=2exp[-y^2/(8n)],                y>=0.         (6)

This proof works separately for every s with the SAME constants. It
requires no independence between different pruning depths.

## 4. Transfer the slice law exactly to uniform Dyck roots

A cyclic word with r ones and r+1 zeros has a unique rotation of the form
0D with D Dyck, by the cycle lemma. All its n rotations are distinct:
a repetition by a factor greater than one would make that factor divide
the total zero-minus-one excess, which is one.

Thus every Dyck root has exactly n preimages in the fixed-count slice.
All N_s are rotation-invariant, so the ENTIRE pruning profile has the
same law under a uniform slice word and under uniform D via (3). There
is no probability cost or profile-dependent reweighting in this step.

Let b_s=E_D r_s. From (3) and (5),

    |b_s-r/(s+1)|
      <=sqrt(n)+(1/2)sqrt(n+1)+1/2
      <=4sqrt(r).                                    (7)

Also (6), after division by two, gives

    Pr_D(|r_s-b_s|>x)
       <=2exp[-x^2/(2n)]
       <=2exp[-x^2/(6r)].

Combining this with (7) proves (1).

For the moment bound set Y=(r_s-b_s)/sqrt(r). The centered log-MGF
above gives

    E exp(tY)<=exp[nt^2/(2r)]<=exp(3t^2/2),

and the same bound holds with -t. Therefore

    E exp[t|r_s-r/(s+1)|/sqrt(r)]
      <=e^(4t) E exp(t|Y|)
      <=2exp(4t+3t^2/2)
      <=16exp(4t^2).

The last inequality uses 4t<=2t^2+2 and 2e^2<16. This proves (2),
including t=0 and s=0.

## 5. Scope

The improvement is the absence of a polynomial prefactor from
conditioning iid bits to Dyck words. It supplies uniform one-depth
tails and moments directly under the original Dyck law. Weighted sums
or maxima across depths require their own argument; no across-depth
independence is supplied. In particular no O(1) short-incidence theorem
is a consequence stated in this note.
