# Affine-balanced schedules do not average factor rows, and the SCD Ferrers rule is linearly non-diagonal

**Status (2026-08-21).**  Every assertion below is proved, conditional only
on the one-copy tight-cycle factors explicitly invoked.  There are two
independent conclusions.

1.  For an arbitrary nested type schedule, the row and column occurrence
    loads under independent factor conjugations have exact first- and
    second-moment formulas.  These formulas retain the full within-factor
    multiplicities of the longer and shorter interval decks; conjugating a
    factor merely randomly permutes that fixed multiplicity array.
2.  For the explicit affine schedule

    \[
      P_r=\{x\in\mathbb Z_b:((b-1)/2)x\pmod b<r\},
    \]

    an offset `q=Theta(sqrt b)` does **not** average over `q+1` substantial
    independent payload banks.  At a central split profile, one payload
    carries all but `O(q+|x|)` phases when `q` is even, and two payloads
    carry all but that many phases when `q` is odd.  Consequently the
    independently conjugated one-copy factor construction has
    `Omega_c(W_b)` expected missed labelled targets at every
    `q/sqrt(b)->c>0`; on the even subsequence the lower bound is
    deterministic.

There is also a separate exact obstruction to lifting the product-SCD
wider-side rule into such atoms.  Every physical type schedule makes its
side-choice matrix row-regular, whereas the SCD rule has a Ferrers row
degree determined by the SCD bottom rank.  Their aggregate Hamming distance
over the central payloads is at least `(1/4-o(1))W_b`, regardless of how the
factor orders are indexed.  Thus monotone/reverse-monotone indexing of SCD
bottom ranks cannot make the wider-side rule even `o(W_b)`-close to torus
diagonals.

Neither conclusion obstructs a correlated multirank factor bank, a
different atom geometry, or a linear-scale rerouting of the one-copy bank.

## 1. Exact row-load law, including repeated windows inside one bank

Let `b` be an odd prime, put

\[
 C_j={b\choose j},\qquad W_b={2b\choose b},
\]

and conditionally fix a tight-cycle factor `F_r` at every needed local rank
`r`.  Thus

\[
 |\mathcal F_r|=f_r={C_r\over b},
\]

and the rank-`r` cyclic windows of its orders partition the rank-`r`
subsets.

For any proper local rank `k`, define the full within-bank window
multiplicity

\[
 n_{r,k}(U)=
 \#\{(\alpha,i):\alpha\in\mathcal F_r,
                    i\in\mathbb Z_b,
                    I_\alpha(i,k)=U\},              \tag{1.1}
\]

where `|U|=k`.  No simplicity across different orders is assumed.  The
only universal identity is

\[
 \sum_{U\in{[b]\choose k}}n_{r,k}(U)=bf_r=C_r.      \tag{1.2}
\]

Independently conjugate every rank-and-side factor by a uniform permutation
of its labels.  For a fixed `k`-set `X`, let

\[
 D_{r,k}(X)=n_{r,k}(\pi_r^{-1}X).                   \tag{1.3}
\]

This is exactly the number of conjugated factor orders whose rank-`k`
window deck contains `X`, counted with the multiplicities in (1.1).  Put

\[
 \rho_{r,k}={C_r\over C_k},\qquad
 v_{r,k}={1\over C_k}\sum_U n_{r,k}(U)^2-\rho_{r,k}^2,
                                                                    \tag{1.4}
\]

and

\[
 \sigma_{r,k}={1\over C_k}
   \#\{U:n_{r,k}(U)>0\}.                            \tag{1.5}
\]

Fix an upper offset `q` and a split profile with both local coordinates
proper, namely `1<=t=s-q<=s<=b-1`:

\[
 s=|V\cap A|,\qquad t=s-q,qquad P_{q,s}=C_sC_t.    \tag{1.6}
\]

For an arbitrary nested schedule with `A`-phase sets `P_r`, let

\[
 m_r(q,s)=\#\{p\in\mathbb Z_b:
   r+|P_r\cap\{p+1,\ldots,p+q\}|=s\}.              \tag{1.7}
\]

Whenever the nested phase map is strictly increasing in `r`, each phase in
(1.7) belongs to at most one payload.  Let `L^A_{q,s}(X)` be the total
number of source occurrences in profile `(q,s)` whose `A` coordinate is the
fixed set `X`, and define `L^B_{q,s}(Y)` analogously for a fixed rank-`t`
complement coordinate `Y` on `B`.

### Theorem 1.1 (exact row and column moments)

For every fixed row `X` and column `Y`,

\[
 \boxed{
 L^A_{q,s}(X)=\sum_r m_r(q,s)f_rD^A_{r,s}(X),\qquad
 L^B_{q,s}(Y)=\sum_r m_r(q,s)f_rD^B_{r,t}(Y).}      \tag{1.8}
\]

Consequently,

\[
 \boxed{
 \begin{aligned}
 \mathbb E L^A_{q,s}(X)
   &={1\over bC_s}\sum_r m_r(q,s)C_r^2,\\
 \operatorname {Var}L^A_{q,s}(X)
   &=\sum_r\left({m_r(q,s)C_r\over b}\right)^2v_{r,s},
 \end{aligned}}                                                    \tag{1.9}
\]

and the analogous column formulas replace `C_s,v_(r,s)` by
`C_t,v_(r,t)`.  Moreover

\[
 \Pr(D_{r,k}(X)=0)=1-\sigma_{r,k}
   \ge(1-\rho_{r,k})_+,                           \tag{1.10}
\]

and, whenever `rho_(r,k)<=1`,

\[
 v_{r,k}\ge\rho_{r,k}(1-\rho_{r,k}).              \tag{1.11}
\]

#### Proof

Fix one occurrence `(alpha,i)` of `X` in the rank-`s` deck of the
rank-`r` factor.  For every `beta in F_r` and every one of the `m_r(q,s)`
contributing phase diagonals, there is exactly one counter point on that
diagonal with first coordinate `i`.  Hence this occurrence contributes
`m_r f_r` row occurrences.  Summing over all occurrences of `X` gives the
first identity in (1.8); the column identity is symmetric.

A uniform label conjugation acts transitively on the rank-`k` subsets, so
`D_(r,k)(X)` is exactly a uniformly sampled entry of the deterministic
array `(n_(r,k)(U))_U`.  Equations (1.2)--(1.5) give

\[
 \mathbb ED_{r,k}(X)=\rho_{r,k},\qquad
 \operatorname {Var}D_{r,k}(X)=v_{r,k}.            \tag{1.12}
\]

The rank variables are independent, so variances add in (1.9).
The support in (1.5) has size at most both `C_k` and the total multiplicity
`C_r`, proving (1.10).  Finally `D` is a nonnegative integer, so
`E D^2>=E D`; subtracting `(E D)^2` proves (1.11).  \(\square\)

Thus independent conjugation supplies no within-bank law of large numbers:
it only moves the zero rows and repeated rows of a fixed factor deck to
uniformly random labels.  Any concentration must come from many substantial
independent payload ranks, not from the exponentially many orders inside
one conjugated factor.

## 2. The inverse-step-two affine schedule has only one or two main ranks

Write

\[
 b=2h+1,qquad a=h=(b-1)/2\pmod b.
\]

Since `a^(-1)=-2 mod b`, the affine nested sets have the explicit form

\[
 P_r=\{-2y\pmod b:0\le y<r\}.                     \tag{2.1}
\]

Away from a cyclic interval around `0`, their indicator is the alternating
odd/even word whenever `r` is close to `h`.  More explicitly,

\[
 \begin{aligned}
 P_{h-k}&=\{0\}\cup\{2k+3,2k+5,\ldots,2h-1\},\\
 P_{h+1+k}&=\{0,1,3,\ldots,2h-1\}
             \cup\{2h,2h-2,\ldots,2h-2k+2\},      \tag{2.2}
 \end{aligned}
\]

with the evident empty-set conventions.
Here the first line is used for `0<=k<=h-1` (and `P_0` is empty), while
the second is used for `0<=k<=h`.

### Lemma 2.1 (one/two-main-rank phase law)

Suppose

\[
 q=O(\sqrt b),\qquad
 s={b+q\over2}+x,\qquad |x|=O(\sqrt b).            \tag{2.3}
\]

If `q=2ell` is even, put

\[
 r_0=s-\ell.
\]

Then

\[
 m_{r_0}(q,s)=b-O(q+|x|+1),\qquad
 \sum_{r\ne r_0}m_r(q,s)=O(q+|x|+1).              \tag{2.4}
\]

If `q=2ell+1` is odd, put

\[
 r_-=s-\ell-1,qquad r_+=s-\ell.
\]

Then

\[
 m_{r_-}(q,s)={b\over2}+O(q+|x|+1),\qquad
 m_{r_+}(q,s)={b\over2}+O(q+|x|+1),                \tag{2.5}
\]

and

\[
 \sum_{r\notin\{r_-,r_+\}}m_r(q,s)=O(q+|x|+1).   \tag{2.6}
\]

The estimates include any phase holes in their `O(q+|x|+1)` exceptional
set.

#### Proof

Every contributing rank is `r=s-z` with `0<=z<=q`, so (2.3) puts all of
them within `O(q+|x|+1)` of `h`.  Formula (2.2) shows that, simultaneously
for all those ranks, the word `1_(P_r)` differs from the alternating word
only on one cyclic interval of length `O(q+|x|+1)` about `0`.  At most
`O(q+|x|+1)` cyclic `q`-windows meet that interval.

On every remaining phase, an even-length window contains exactly `ell`
ones.  Hence the unique solution of `r+z=s` is `r_0`.  An odd-length window
contains `ell` or `ell+1` ones according to its parity, giving `r_+` or
`r_-`.  Outside the exceptional interval the two parities each occur
`b/2+O(q+|x|+1)` times.  Strict increase of the nested phase map rules out a
second rank at any phase and proves (2.4)--(2.6).  \(\square\)

Thus the nominal `q+1` payload sources are not `q+1` comparable random
summands.  For even `q` there is one summand of weight `(1-o(1))C_(r_0)`;
for odd `q` there are two summands of weight `(1/2+o(1))C_(r_\pm)`.

## 3. A linear labelled deficit despite scalar capacity

Let

\[
 {q\over\sqrt b}\longrightarrow c\in(0,\infty),
 \qquad {x\over\sqrt b}\longrightarrow d\in\mathbb R.          \tag{3.1}
\]

For either main rank in Lemma 2.1, the central binomial expansion gives

\[
 \alpha(c,d):={C_r\over C_s}
   =\exp\{c^2/2+2cd+o(1)\},                        \tag{3.2}
\]

and

\[
 \beta(c,d):={C_r\over C_t}
   =\exp\{c^2/2-2cd+o(1)\}.                        \tag{3.3}
\]

All nonmain ranks together have only

\[
 T_{\mathrm{minor}}={1\over b}
   \sum_{r\text{ nonmain}}m_r(q,s)C_r^2=o(P_{q,s})              \tag{3.4}
\]

source occurrences.  Indeed their total phase multiplicity is `O(sqrt b)`,
all relevant ranks are within `O(sqrt b)` of the middle, and
`C_sC_t=Theta_c(C_h^2)`.

Let `Z_(q,s)` denote the number of missed labelled targets in the split
profile `(q,s)`, and put

\[
 Z_q=\sum_s Z_{q,s}.                                \tag{3.4a}
\]

### Theorem 3.1 (affine balanced one-copy factor obstruction)

Under mutually independent rank-and-side conjugations of arbitrary
one-copy tight factors, the expected missed fraction in the fixed profile
obeys the following bounds.

If `q` is even, then in fact deterministically

\[
 \boxed{
 {Z_{q,s}\over P_{q,s}}
 \ge
 \begin{cases}
  1-\alpha(c,d)-o(1),&d<-c/4,\\
  1-\beta(c,d)-o(1),&d>c/4.
 \end{cases}}                                      \tag{3.5}
\]

If `q` is odd, then

\[
 \boxed{
 {\mathbb EZ_{q,s}\over P_{q,s}}
 \ge
 \begin{cases}
  (1-\alpha(c,d))^2-o(1),&d<-c/4,\\
  (1-\beta(c,d))^2-o(1),&d>c/4.
 \end{cases}}                                      \tag{3.6}
\]

In particular, for every fixed `c>0`, along either parity subsequence

\[
 \boxed{\mathbb EZ_q\ge(\Gamma_c^{\rm parity}-o(1))W_b}        \tag{3.7}
\]

for an explicit constant `Gamma_c^(parity)>0`.  One may take

\[
 \begin{aligned}
 \Gamma_c^{\rm even}
 &= {4e^{-c^2}\over\sqrt\pi}
    \int_{c/4}^{\infty}e^{-4d^2}
       \left(1-e^{c^2/2-2cd}\right)\,\mathrm d d,\\
 \Gamma_c^{\rm odd}
 &= {4e^{-c^2}\over\sqrt\pi}
    \int_{c/4}^{\infty}e^{-4d^2}
       \left(1-e^{c^2/2-2cd}\right)^2\,\mathrm d d.
                                                               \tag{3.8}
 \end{aligned}
\]

Moreover the failed concentration is visible directly in the exact
variance.  On the left-hand region `d<-c/4`, for a fixed row `X`,

\[
 \liminf {\operatorname {Var}L^A_{q,s}(X)\over C_t^2}
 \ge
 \begin{cases}
  \beta^2\alpha(1-\alpha),&q\text{ even},\\[2pt]
  \frac12\beta^2\alpha(1-\alpha),&q\text{ odd},
 \end{cases}                                       \tag{3.9}
\]

and the symmetric column statement holds on `d>c/4`.

#### Proof

Suppose first that `q` is even and `d<-c/4`.  By (3.2), the main rank has
`C_r<C_s` for all sufficiently large `b`.  Its rank-`s` window deck has
only `C_r` occurrences, so at least `C_s-C_r` rows are absent from that
deck, for every factor and every conjugation.  The main source covers no
target in any such row.  Those rows contain `(C_s-C_r)C_t` targets, and all
minor sources together can repair at most their total number of occurrences
(3.4).  This proves the first line of (3.5).  The column proof for
`d>c/4` uses `C_r<C_t` and is identical.

For odd `q`, the two main factor conjugations are independent.  A fixed row
is absent from main deck `r_i` with probability
`1-sigma_(r_i,s)>=1-C_(r_i)/C_s`.  Hence its probability of being absent
from both main decks is at least `(1-alpha+o(1))^2`.  Sum over all rows and
again subtract (3.4).  This proves (3.6).

Uniformly for bounded `d`, the profile local limit is

\[
 {P_{q,s}\over W_b}
 ={2+o(1)\over\sqrt{\pi b}}e^{-c^2-4d^2}.          \tag{3.10}
\]

Riemann summation of (3.5)--(3.6) over the two symmetric regions gives
(3.7)--(3.8), whose integrands are strictly positive.

Finally apply (1.11) to each main rank in the exact variance formula (1.9).
For even `q`, its coefficient divided by `C_t` tends to `beta`; for odd
`q`, each of the two coefficients tends to `beta/2`.  This gives (3.9).
\(\square\)

The scalar phase capacity can exceed `P_(q,s)` throughout this example.
The theorem shows why that does not imply a labelled lift: almost all that
capacity sits in one or two conjugated multiplicity arrays, and the missing
rows or columns of those arrays persist at constant density on the
off-central Gaussian shoulders.

## 4. The product-SCD wider-side matrix cannot be diagonalized

Fix symmetric-chain decompositions on `A` and `B`.  At rank `r`, let
`a(X)` and `c(Y)` be the bottom ranks of the chains containing `X` and `Y`.
Put

\[
 m=\min(r,b-r),\qquad C_{-1}=0.
\]

Every SCD has exactly

\[
 N_j=C_j-C_{j-1}                                   \tag{4.1}
\]

chains with bottom rank `j`.  Consequently the product-SCD wider-side rule

\[
 M^*(X,Y)=1_{\{a(X)\le c(Y)\}}                    \tag{4.2}
\]

has, in a row whose bottom is `a`, exactly

\[
 R_a=\sum_{c=a}^{m}N_c=C_r-C_{a-1}                 \tag{4.3}
\]

entries equal to one.

Now take arbitrary tight-cycle factors at rank `r`, pair every `A` order
with every `B` order, and allow an arbitrary relative origin and an
arbitrary cyclic type schedule in each atom, subject only to the necessary
middle count of exactly `r` letters of type `A`.  Let `M` be the resulting
choice matrix in which a middle source is marked one precisely when its
next emitted type is `A`.

### Theorem 4.1 (exact row-regularity and a quarter-distance barrier)

Every row of `M` has exactly

\[
 K_r=rf_r={r\over b}C_r                            \tag{4.4}
\]

ones.  Hence, for every choice and indexing of the factors, schedules, and
origins,

\[
 \boxed{
 \operatorname {dist}_{\rm Ham}(M,M^*)
 \ge
 \sum_{a=0}^{m}(C_a-C_{a-1})
 \left|C_r-C_{a-1}-{r\over b}C_r\right|.}          \tag{4.5}
\]

Uniformly for `|r-b/2|=O(sqrt(b log b))`, the right side is

\[
 (1/4-o(1))C_r^2.                                  \tag{4.6}
\]

Therefore, summed over those central payloads,

\[
 \boxed{
 \sum_r\operatorname {dist}_{\rm Ham}(M_r,M_r^*)
 \ge(1/4-o(1))W_b.}                                \tag{4.7}
\]

#### Proof

Fix `X` and its unique owner coordinate `(alpha,u)` in the rank-`r`
factor.  In one atom `(alpha,beta)`, as the `B` coordinate `v` runs through
`Z_b`, the counter-sum phase runs bijectively through `Z_b`.  Exactly `r`
of those cells see the next type `A`, independently of the relative origin
or the arrangement of the type word.  There are `f_r` choices of `beta`,
proving (4.4).

Two binary row vectors of weights `K_r` and `R_a` have Hamming distance at
least `|K_r-R_a|`.  There are `C_a-C_(a-1)` rank-`r` sets with SCD bottom
`a`; summing this row bound proves (4.5).

For the asymptotic evaluation, put

\[
 p_a={C_a-C_{a-1}\over C_m},\qquad
 u_a={C_{a-1}\over C_m},\qquad
 \kappa={r\over b}.                                \tag{4.8}
\]

The `p_a` are the successive mesh lengths of the partition
`0=C_(-1)/C_m<C_0/C_m<...<C_m/C_m=1`.  On the stated central range its
maximum mesh is `o(1)`.  Dividing (4.5) by `C_r^2=C_m^2` therefore gives
the left Riemann sum

\[
 \sum_ap_a|1-\kappa-u_a|
 =\int_0^1|1-\kappa-u|\,\mathrm du+o(1)
 ={(1-\kappa)^2+\kappa^2\over2}+o(1)
 ={1\over4}+o(1).                                  \tag{4.9}
\]

Finally Vandermonde gives `sum_r C_r^2=W_b`, and the window
`|r-b/2|=O(sqrt(b log b))` contains `1-o(1)` of this sum.  Summing (4.6)
proves (4.7).  \(\square\)

The obstruction is more basic than the proposed monotone/reverse-monotone
ordering of the bottom ranks.  A matrix constant on cyclic sum diagonals
has the same number of ones in every row.  The Ferrers matrix (4.2) has a
macroscopically varying row degree.  Reordering its rows and columns cannot
remove that discrepancy.

Nor can the Ferrers rule be substantially regularized while retaining the
same SCD trajectories.

### Proposition 4.2 (the wider-side rule is forced off equal-bottom blocks)

Consider assignments which, from a source `(X_r,Y_r)`, use the successor
of `X_r` in its fixed `A`-SCD chain when the source is marked `A`, and use
the predecessor of `Y_r` in its fixed `B`-SCD chain when it is marked `B`.
If every admissible offset-one target is covered, then on every product of
two SCD chains with unequal bottoms the marking is forced:

\[
 a<c\Longrightarrow\hbox{every common-rank source is marked `A`},
 \qquad
 a>c\Longrightarrow\hbox{every common-rank source is marked `B`}. \tag{4.10}
\]

Only an equal-bottom product can use a nonconstant threshold, with `A`
below the threshold and `B` above it.  At a central rank, the fraction of
sources lying in equal-bottom products is at most

\[
 {\sum_{a=0}^{m}(C_a-C_{a-1})^2\over C_r^2}
 \le\max_a{C_a-C_{a-1}\over C_r}=o(1).             \tag{4.11}
\]

If `M^(cov)` is the marking of any complete cover supported on the fixed
product-SCD trajectories, then centrally

\[
 \operatorname {dist}_{\rm Ham}(M^{\rm cov},M^*)
 \le\sum_{a=0}^{m}(C_a-C_{a-1})^2=o(C_r^2).         \tag{4.11a}
\]

Hence every physical row-regular torus marking `M` satisfies

\[
 \operatorname {dist}_{\rm Ham}(M,M^{\rm cov})
 \ge(1/4-o(1))C_r^2,                                \tag{4.11b}
\]

and this lower bound aggregates to `(1/4-o(1))W_b` over the central
payloads.  This is a side-marking/compilation distance, not a claim of
`Omega(W_b)` missed targets for a near-cover.

#### Proof

Along one product of chains, write `x_j=A` or `B` for its marking at common
rank `j`.  Coverage of the target between ranks `j` and `j+1` forbids the
pattern `(x_j,x_(j+1))=(B,A)`: neither chosen trajectory then reaches that
target.

Suppose `a<c`.  The `B` chain ends at rank `b-c`, whereas the wider `A`
chain continues at least through rank `b-c+1`.  The boundary target with
coordinates at `A`-rank `b-c+1` and `B`-rank `b-c` has no `B`-trajectory
predecessor, so the common-rank source at `b-c` is forced to be `A`.
Backward induction using the forbidden `(B,A)` pattern forces `A` at every
common rank.  If `a>c`, the `A` chain begins later.  The boundary target
with coordinates at `A`-rank `a` and `B`-rank `a-1` has no `A`-trajectory
predecessor, so its upper common-rank source is forced to be `B`; forward
induction forces `B` thereafter.  When `a=c` there is no unequal boundary,
and the only condition is the absence of a `B`-to-`A` rise, namely one
threshold.

The number of rank-`r` sources in equal-bottom products is the numerator of
(4.11).  Its normalized value is `sum_a p_a^2<=max_a p_a=o(1)` on the
central range used in (4.6).  Thus every complete marking differs from
`M^*` on at most those entries, proving (4.11a).  The triangle inequality
with (4.6), followed by the same central summation as in (4.7), proves
(4.11b) and its aggregate form.
\(\square\)

There is an even simpler reason that the exact central cover seen in an
unrestricted constant-side MILP cannot at the same time satisfy the
ordinary physical phase counts.  At `b=2h+1`, the balanced offset-one
profile has `s=h+1,t=h` and size `C_h^2`.  The payload-`h` bank has only
`hC_h^2/b` `A`-transition occurrences in that profile, while the
payload-`h+1` bank has only `hC_h^2/b` `B`-transition occurrences.  Thus
every row/column-regular one-copy realization misses at least

\[
 {1\over b}C_h^2                                   \tag{4.12}
\]

targets there, before collisions.  This is only `o(W_b)` and hence is not
an asymptotic no-go.  It does show that exact unrestricted MILP coverage and
exact physical regularity are different requirements.

## 5. Scope and audit

The affine result is a labelled one-copy factor obstruction, not a scalar
one: it is compatible with the exact inequality `T_(q,s)>=P_(q,s)` seen in
the phase-capacity ledger.  The SCD result obstructs only a literal or
`o(W_b)`-modified realization of a fixed product-SCD trajectory cover by
ordinary product-factor torus diagonals.  A row-regular cover built from
different containment trajectories might still cover all but `o(W_b)`
targets; (4.12) rules out exact coverage, not such an asymptotic result.

The H100 checker
`scratch/audit_affine_balanced_factor_row_load_and_scd_diagonal_20260821.py`
does the following.

- It exhaustively verifies (2.1)--(2.2) and the one/two-main-rank phase law
  for all odd primes `b<=101` and all central test profiles.
- It constructs Walecki rank-two factors at small odd `b`, retains every
  repeated longer/shorter window inside a bank, and exhaustively averages
  over label conjugations to verify (1.9)--(1.11).
- It checks the exact SCD bottom-rank census and row-degree formula (4.5),
  exhaustively checks the forced-switch statement in Proposition 4.2 at
  small odd `b`, and numerically verifies convergence of the normalized
  row-degree bound to `1/4` through large central ranks.
- It prints finite affine profile deficits and confirms that the minor
  occurrence fraction tends down on the predicted scale.

These computations audit the indexing and asymptotics; the proofs above do
not depend on them.
