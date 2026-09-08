# Growing adaptive gap exposure under actual short incidence

2026-09-08. Pure proof; no computation. Root and independent cover-selectors
read the complete note and passed the entropy, decoding, parameter replacement,
actual-incidence, and adaptive-query quantifier checks.

For a fixed number S of original rows, the finite-query freshness theorem
extends to any deterministic fresh-query budget M_r=o(r/log r). In
particular it permits O(sqrt(r)) individual original-gap queries. The
environment keeps its actual incidence law and repeated labels keep their
previous values. No new law is assigned to reached roots.

## 1. A quantitative uniform-composition lemma

Fix 0<a<b<infinity. Let Z=(Z_1,...,Z_P) be a uniform weak composition of
ell into P labelled parts, with a<=ell/P<=b. Put

    q=ell/(ell+P).

There is a constant C_(a,b) such that, whenever P is sufficiently large
and 1<=m<P with ceil(K_(a,b)(m+log P))<= (ell+P-1)/2,

    TV(Law(Z_1,...,Z_m), Geom(q)^m)
       <= C_(a,b)(m+log P)/P + P^(-2).              (1)

Here Geom(q){j}=(1-q)q^j, j>=0. Thus m=o(P) suffices for convergence
to the exact mean-matched independent law. For m>=log P, (1) has rate
O_(a,b)(m/P).

### 1.1. Uniform words and an entropy estimate

Encode the composition by a word with ell stars and P-1 bars, all such
words equally likely. Put N=ell+P-1, B=P-1, and p=B/N. Its first m
gaps are the numbers of stars before each of its first m bars.

Compare its first L symbols, sampled without replacement, with L iid
Bernoulli(p) symbols, where one denotes a bar. Under the without-
replacement law, let S_j count bars among the first j symbols. The next
conditional bar probability is p_j=(B-S_j)/(N-j). Direct pair counting
gives

    E S_j=jp,
    Var(S_j)=j p(1-p)(N-j)/(N-1).

For completeness, distinct symbol indicators have covariance
-p(1-p)/(N-1), because their joint bar probability is B(B-1)/(N(N-1)).
Summing their variances and covariances proves the displayed formula.
Consequently

    E(p_j-p)^2 = j p(1-p)/[(N-1)(N-j)].

For Bernoulli distributions, log x<=x-1 proves

    D(Bern(u) || Bern(p)) <= (u-p)^2/[p(1-p)].

The entropy chain rule therefore yields

    D(prefix_without_replacement || Bern(p)^L)
      <= sum_(j=0)^(L-1) j/[(N-1)(N-j)]
      <= L(L-1)/[2(N-1)(N-L+1)].                   (2)

Pinsker's inequality makes the prefix total variation O(L/N) when
L<=N/2. One elementary proof of the inequality suffices here: coarsen
to the set where the first density exceeds the second, use the log-sum
inequality, and note that binary relative entropy has second derivative
1/u+1/(1-u)>=4 in its first argument. This gives D>=2 TV^2.

### 1.2. Decode gaps without paying an additional actual tail

For ell/P in [a,b], the bar probability p is bounded below by a positive
constant p_* depending only on b. Choose

    L=ceil(K(m+log P))

with K large enough that Lp>=2m and Lp>=16log P. The elementary iid
Bernoulli Chernoff estimate gives

    Pr_iid(S_L<m) <= Pr_iid(S_L<Lp/2)
                   <= exp(-Lp/8) <= P^(-2).          (3)

For example, apply exponential Markov with exponent -1/2 and use
e^(-1/2)<5/8 to obtain the middle bound.

Maximally couple the two length-L prefixes. If they agree and the iid
prefix contains m bars, their first m decoded gaps agree. Thus their
gap-vector TV is at most the prefix TV plus (3). No tail assertion for
the actual without-replacement stopping time is needed.

The iid decoded gaps have parameter

    q'=ell/(ell+P-1),    |q'-q|=O_(a,b)(1/P).

Both parameters stay in a compact subinterval of (0,1). The exact formula

    D(Geom(u) || Geom(v))
      =log((1-u)/(1-v)) + [u/(1-u)]log(u/v)

has a uniform quadratic bound C(u-v)^2 there. This follows by Taylor
expansion in v around v=u: the first derivative is zero and the second
derivative is uniformly bounded on that compact interval. Additivity
and Pinsker give a product-TV error O_(a,b)(sqrt(m)/P), which is absorbed
by O_(a,b)(m/P). Combining this with (2)-(3) proves (1).

## 2. Exact adaptive implementation by fresh-reply sequences

Fix the safe base event B_(r,S) and actual environment E_r from
`PBBS_FINITE_ADAPTIVE_GAP_QUERY_FRESHNESS_20260908.md`:

    E_r=(entire profile, all original rows s>=S, sampled offset j).

The accepted finite-layer incidence fibre says that, conditional on every
feasible E_r and B_(r,S), rows 0<=s<S are independent uniform compositions
of ell_s into P_s=p_s-s-1 free slots, with their base coordinates zero.

In each row, pre-generate a uniform-composition reply sequence of length
P_s, independently across rows. When an exploration requests a previously
unseen free label in that row, assign the next unused reply to that label.
Store it and reuse it at subsequent requests. Return zero at base labels.

This generates exactly the original adaptive transcript law. Indeed,
conditional on any previous replies, the unseen labelled coordinates
still uniformly compose the residual total; their exchangeability makes
every history-measurable choice of a new label equivalent to the next
entry of the pre-generated sequence. The choice of label imposes no extra
condition on unused values. Repeated labels are not new draws.

An exploration making at most M_r fresh requests in total is therefore a
measurable function of E_r, its independent seed, and the first M_r reply
entries of each of the S rows. Pre-generating S*M_r entries is harmless;
many may never be used. Joint TV contracts under this measurable map.
Thus summing the S row bounds (1) controls EVERY such adaptive exploration,
without a sequential M_r^2/r coupling loss or a separate selection penalty.

The legal-input restriction is unchanged: every query and stopping decision
must use only E_r, the seed, and previously returned individual values.
An unrevealed aggregate or a reached-root oracle is not supplied for free.

## 3. The exact finite parameters under actual incidence

Define the environment-dependent parameters

    q_(s,r)=ell_s/(ell_s+P_s),  0<=s<S.

For every fixed S and every deterministic M_r=o(r), the preceding argument
gives mean conditional TV convergence of all legal M_r-query transcripts
to an oracle returning independent Geom(q_(s,r)) values at each new free
slot in row s, while preserving E_r and repeated replies.

Here are sufficient quantitative profile bounds, also needed below. The
accepted original one-depth concentration is

    Pr_D(|r_s-r/(s+1)|>(4+x)sqrt(r))<=2exp(-x^2/6).

The marginal F0-incidence density is at most (H+2)/mu_0=O_c(sqrt(r)).
Conditioning on B_(r,S), whose probability tends to one, costs at most a
further factor two for sufficiently large r. A union bound over depths
0,...,S+1, with x a sufficiently large multiple of sqrt(log r), therefore
shows the following for every fixed D>0: outside an actual incidence set
of probability O_(c,S,D)(r^(-D)),

    |r_s-r/(s+1)| <= C_(c,S,D) sqrt(r log r)
                                  for 0<=s<=S+1.   (4)

Since S is fixed, these estimates imply P_s is comparable to r and
ell_s/P_s stays in a compact positive interval, uniformly on this set.
The exact composition-to-finite-parameter transcript error is therefore

    O_(c,S,D)((M_r+log r)/r) + O_(c,S,D)(r^(-D)),   (5)

whenever M_r=o(r). The finite-population estimate itself needs no logarithm
in the admissible exposure fraction.

## 4. Replacement by the fixed limiting geometric parameters

Using p_s=2r_(s+1)+1 and
ell_s=r_s-2r_(s+1)+r_(s+2), the profile estimate (4) gives

    |q_(s,r)-q_s| <= C_(c,S,D) sqrt(log r/r),
    q_s=1/(s+2)^2.                                 (6)

All these parameters lie in a common compact subinterval of (0,1) for
fixed S on the typical set. The geometric entropy estimate used in
Section 1, additivity over S*M_r fresh replies, and Pinsker give

    TV(product finite-parameter replies,
       product fixed-parameter replies)
        <= C_(c,S,D) sqrt(M_r log r/r).              (7)

Combine (5)-(7) and contract through the adaptive algorithm. Uniformly
over every legal exploration with at most M_r fresh queries,

    E_[E_r | B_(r,S)] TV(actual transcript | E_r,
                         fixed-parameter oracle transcript | E_r)
      <= C_(c,S,D)[(M_r+log r)/r
                         +sqrt(M_r log r/r)]
                           +O_(c,S,D)(r^(-D)).      (8)

In particular M_r=o(r/log r) implies convergence. At M_r=O(sqrt(r)),
the displayed bound is O_(c,S)(r^(-1/4)sqrt(log r)), after choosing D
large enough. Assigning a common exceptional output outside B_(r,S)
adds only its O_(c,S)(1/r)+exp(-Omega_(c,S)(r)) probability and yields
the corresponding unconditional actual-incidence statement.

The comparison keeps exactly the same actual environment marginal on
both sides, so (8) is also joint total-variation control of environment
and transcript. It does not replace that marginal by an unweighted law.

## 5. Physical use and remaining boundary

The result now permits O(sqrt(r)) legal individual-gap exposures in a
fixed number of rows; tightness of a fixed query budget is unnecessary
for such a task. For example, a two-row virtual-clock construction that
selects at most two row-one labels for each of H+2 physical phases using
only the exposed depth-two trajectory fits the budget, once its exact
clock and phase interface is established separately.

The theorem does not itself establish many eligible virtual clocks,
physical renewal, a growing-S law, or the cross-cutoff gate. Whole-row
aggregate exposure still needs a separate conditional-fibre argument
unless reconstructed within the permitted individual-query budget.
