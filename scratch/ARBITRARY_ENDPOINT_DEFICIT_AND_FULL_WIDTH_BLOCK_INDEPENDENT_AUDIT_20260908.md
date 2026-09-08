# Independent audit: arbitrary endpoints, deficit, and the full-width block

Date: 2026-09-08.

Source: the user's supplied text at `/Users/amir.nuriyev/.codex/attachments/5e90e3f1-a1a5-496b-ade2-60dbb47bc2ce/pasted-text.txt`, together with the subsequent user strengthening relayed by the root agent concerning offset blocks and upper-target support. The subsequent strengthening is not present in that attachment.

Status: the endpoint-deficit identity and full-width block theorem pass independent pure-proof review for arbitrary starts and deadlines. The follow-up strengthening also passes, with the explicit hypotheses and per-rank scope below. This audit does not establish an attaining word or nu(k)=B(k).

The attachment links to a sandbox proof/checker package that is not included in the supplied files. Its claimed 82,488-family and 21-word computations were not independently replayed here. The proofs below do not depend on those computations. No mathematical program was executed for this audit.

## 1. General endpoint setup

Let a universal linear word of nonempty set letters have n=W+t positions, where W=binomial(k,s). Choose one interval I_i=[ell_i,r_i] for each rank-s target, ordered by left endpoint.

Distinct same-rank targets cannot have nested witnessing intervals: inclusion of intervals implies inclusion of their unions, and two different sets of equal rank are incomparable. Thus both endpoint sequences are strictly increasing. Consequently

    ell_i=i+alpha_i,    r_i=i+beta_i,
    0 <= alpha_i <= beta_i <= t,

with alpha and beta nondecreasing. These conclusions do not require prescribed or consecutive starts.

Every interval [a,b] of length at least t+1 contains I_a, because a<=W and

    a <= ell_a <= r_a <= a+t <= b.

In particular, all lower-rank witnesses have length at most t. Put

    Lambda = sum(j=1,...,s-1) binomial(k,j),
    sigma = tW+t(t+1)/2-Lambda.

Universality implies sigma>=0. Every selected interval has length at most t+1.

## 2. Exact endpoint deficit

Let C count the nonempty position intervals containing none of the selected I_i, and set ell_0=alpha_0=0. If ell_(i-1)<a<=ell_i, the earliest-ending selected interval starting at or after a is I_i. The avoiding intervals starting at a are exactly [a,b] with a<=b<r_i, numbering r_i-a. If a>ell_W, all intervals starting at a avoid the selected family. Summation gives

    C = sum(i=1,...,W) (ell_i-ell_(i-1))r_i
        +(n-ell_W)(n+1)-n(n+1)/2.

Subtract this expression from its value at alpha_i=0,beta_i=t. The difference is

    sum_i(t-beta_i)
      +sum_i(alpha_i-alpha_(i-1))(n+1-i-beta_i).

Using n=W+t and

    sum_i(alpha_i-alpha_(i-1))(W+1-i)=sum_i alpha_i

proves the exact identity

    C=tW+t(t+1)/2-D,
    D=sum_i(t+alpha_i-beta_i)
       +sum_i(alpha_i-alpha_(i-1))(t-beta_i).

Both sums in D are nonnegative. Each lower-rank target has a distinct witness counted by C, so C>=Lambda and therefore D<=sigma. In particular,

    sum_i(t+1-|I_i|) <= sigma.

No loss or unstated endpoint regularity enters this identity.

## 3. All rank-s full-width windows form one block

Consider every length-(t+1) window V_a, with 1<=a<=W. The containment argument above gives |V_a|>=s.

First, no two such windows can have the same rank-s union. Otherwise take those two intervals and one witness for each of the other W-1 rank-s targets. They form W+1 pairwise nonnested intervals: different equal-rank targets cannot nest, and the two equal-target windows have equal lengths and different starts.

In an antichain of M position intervals in [n], the i-th left endpoint is at least i and the i-th right endpoint is at most n-M+i. Every interval therefore has length at most n-M+1. Applying this with M=W+1 gives maximum length t, contradicting the two chosen windows' length t+1.

All rank-s full-width windows can thus be included simultaneously in the selected representative family. For that family,

    |I_i|=t+1  if and only if  alpha_i=0 and beta_i=t.

The beta condition is a suffix of the index sequence and the alpha condition is a prefix. Their intersection is a single consecutive block, possibly empty. On that intersection ell_i=i, so ordinal indices equal actual source starting positions. Because all rank-s full-width windows were included, this is precisely the full set of their starting positions, not merely a selected subset.

Every other representative consumes at least one unit in sum_i(t+1-|I_i|). Hence the block has at least [W-sigma]_+ windows. This proves the user's theorem for arbitrary endpoint geometries and validly removes the consecutive-start premise of the earlier restricted 16,909-window deduction.

At k=17, s=9, W=24,310, n=B(17)=24,313, t=3 and sigma=7,401. An attaining word therefore has a block of at least 16,909 consecutive rank-nine four-letter windows, all with distinct unions. Their source segment has at least 16,912 positions. Every four-letter window outside the complete rank-nine block has rank at least ten.

This is a necessary condition on an unknown attaining word, not its construction.

## 4. Offset blocks and the shape forced by one full-width witness

For any selected representative family, the total increase of alpha plus beta between successive indices is at most 2t. Each change of the ordered pair (alpha_i,beta_i) uses at least one unit. Thus there are at most 2t+1 maximal constant-offset blocks.

Now suppose at least one selected witness I_h has full length t+1. This holds, in particular, under the preceding theorem whenever W>sigma. Since alpha_h=0 and beta_h=t, monotonicity forces

    alpha_i=0 for i<=h,
    beta_i=t for i>=h.

Before the full-width block the selected lengths are beta_i+1, hence nondecreasing; after it they are t+1-alpha_i, hence nonincreasing. After merging equal neighboring values, their order is a subsequence of

    1,2,...,t,t+1,t,...,2,1,

with missing blocks allowed. There is exactly one nonempty block of length t+1.

Moreover ell_1=1 and r_W=n. Every adjacent selected pair touches or overlaps:

- For i<h, consecutive starts give ell_(i+1)=ell_i+1<=r_i+1.
- For i>=h, consecutive deadlines give ell_(i+1)<=r_(i+1)=r_i+1.

Therefore the intervals fill the entire word without gaps. More precisely, every consecutive subfamily I_i,...,I_j fills exactly [ell_i,r_j]. This stronger subfamily statement is the one needed in the next argument.

Without a full-width selected witness, neither this unimodal length conclusion nor the gapless covering conclusion is asserted by this audit. The bound of 2t+1 constant-offset blocks remains valid without that additional premise.

## 5. Upper support of the consecutive-owner union family

Retain the full-width-witness hypothesis, and write T_i for the rank-s union on I_i. Consider the family

    U = {T_i union T_(i+1) union ... union T_j : 1<=i<=j<=W}.

Fix a rank q>s. If a witnessing interval [a,b] for a rank-q target has a selected start a=ell_i and a selected deadline b=r_j, then i<=j. Indeed, i>j would make [a,b] a subinterval of I_j and force its rank to be at most s. The gapless subfamily statement now gives

    union(A_a,...,A_b) = T_i union ... union T_j.

So any rank-q target absent from U must have an unselected start or an unselected deadline in every witness. There are exactly t unselected starts and t unselected deadlines in [n]. For one fixed start, interval unions are nested as the right endpoint increases and therefore yield at most one distinct target of rank q. The same statement holds for one fixed deadline as the start varies.

Charging each target absent from U to one unselected endpoint of one witness gives

    number of rank-q targets absent from U <= 2t, for each fixed q>s.

At k=17 exact length this is at most six exceptions in each upper rank. It is not a bound of six on the union of all upper-rank exception sets. This proof concerns consecutive unions of any number of selected owners, not only adjacent-owner unions.

## 6. Review conclusion

The supplied endpoint-deficit identity, rank-s full-width uniqueness, single-block theorem, and its 16,909-window specialization are valid under their stated universal-word assumptions. The follow-up offset and upper-support conclusions are valid with the explicit full-width-witness hypothesis and per-fixed-rank interpretation given above. All of these are structural necessities; they do not supply compatible source letters, the missing Q construction, a word of length 24,313, or exact attainment in every dimension.
