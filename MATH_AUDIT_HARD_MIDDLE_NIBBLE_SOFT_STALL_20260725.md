# Hard-middle packet nibble versus the soft-greedy stall

Date: 2026-07-25

Method: exact counting and a conditional multi-bite calculation; no
computation and no matching black box.

## 0. Verdict

The soft-greedy product-survival obstruction does **not** rule out the
hard-middle-only wreath nibble at the leave scale needed for prime-cycle
smoothing.

For the full packet catalogue, an independently thinned middle residual of
density `u` has expected live-packet count

\[
 { (2m)!\over2}u^{2m+1}.
\]

Its first-moment stall occurs only at `u=(e+o(1))/(2m)`.  At the desired
stopping density `u=m^{-1/2+o(1)}`, the logarithm of the expected catalogue
size is `(1+o(1))m log m`, and the expected degree of every surviving
middle owner has the same exponential order.  Thus the old augmented-edge
stall, whose edge contains `Theta(m^{3/2})` protected resources, is outside
the scope of the hard-middle nibble, whose edge contains only `2m+1`
resources.

What remains missing is not first-moment availability.  It is a hereditary
statement saying that the **endogenous matching residual** retains local
link flatness and two-time anti-clustering.  The final theorem below states
exactly enough typicality to propagate both a long nibble and the required
pair-spread bound.

## 1. Exact product-residual scales

Put

\[
 n=2m+1,
 \qquad W=\binom nm,
 \qquad B={W\over n},
 \qquad D={m!(m+1)!\over2}.
\]

The number of unoriented wreath packets is

\[
 M=BD={(2m)!\over2}.
\tag{1.1}
\]

Retain every middle set independently with probability `u`.  A fixed
packet survives precisely when all its `n` middle owners survive, so

\[
 \boxed{\mathbb E M_{\rm live}=Mu^n.}
\tag{1.2}
\]

The first-moment threshold is therefore

\[
 u_*=M^{-1/n}
 ={e+o(1)\over2m},
\tag{1.3}
\]

because Stirling's formula gives

\[
 {1\over n}\log M=\log(2m)-1+o(1).
\]

At `u=m^{-1/2+o(1)}` instead,

\[
 \log(Mu^n)=(1+o(1))m\log m.
\tag{1.4}
\]

Condition on a fixed middle owner `X` surviving.  Its expected residual
packet degree is

\[
 \boxed{d(u)=Du^{n-1},}
\tag{1.5}
\]

and again

\[
 \log d(u)=(1+o(1))m\log m
 \qquad\bigl(u=m^{-1/2+o(1)}\bigr).
\tag{1.6}
\]

If `X,Y` have Johnson distance `s`, their original packet codegree is

\[
 d(X,Y)=D{2\over\binom ms\binom{m+1}s}.
\tag{1.7}
\]

Conditioning on both owners surviving, the expected residual codegree is
`d(X,Y)u^{n-2}`.  Relative to (1.5), it is

\[
 {2\over\binom ms\binom{m+1}s\,u}.
\tag{1.8}
\]

For the antipodal/disjoint backbone (`s=m`) this is

\[
 {2\over(m+1)u}=m^{-1/2+o(1)},
\tag{1.9}
\]

at the target density.  Off that backbone it is at most

\[
 {2\over m(m+1)u}=m^{-3/2+o(1)}.
\tag{1.10}
\]

Thus even the largest product-residual pair link is still `o(d(u))` at
the proposed stopping time.

The edgewise overlap mass is also on the correct scale.  For every packet
`E`, the exact packet calculation gives

\[
 {1\over D}\sum_{\{X,Y\}\subseteq E}d(X,Y)=O(1).
\tag{1.11}
\]

After product thinning, the expected left side with residual codegrees,
divided by `d(u)`, is `O(1/u)`.  Since one packet has `n` owners, its
relative Bonferroni correction is only

\[
 O\left({1\over nu}\right)=m^{-1/2+o(1)}.
\tag{1.12}
\]

Equations (1.4), (1.6), and (1.9)--(1.12) are favorable.  They are exact
product-model calculations, not claims about a matching-generated
residual.

## 2. One deterministic flat-residual bite

The precise local hypotheses needed by one bite can be stated without any
independence assumption.

Let `H` be the packet hypergraph induced on some residual middle vertex
set.  Suppose there is a number `d` such that

\[
 d_H(X)=(1\pm\varepsilon)d
 \qquad(X\in V(H)),
\tag{2.1}
\]

and, for every available packet `E`,

\[
 \sum_{\{X,Y\}\subseteq E}d_H(X,Y)
 \le \eta nd.
\tag{2.2}
\]

Sample every available packet independently with probability

\[
 p={\theta\over nd},
\tag{2.3}
\]

where `theta>0` is fixed, and retain a sampled packet only when no other
sampled packet meets it.

### Proposition 2.1 (one flat bite)

If `epsilon+eta=o(1)` and `nd tends to infinity`, then, uniformly over
available packets and vertices,

\[
 \Pr(E\text{ is retained})
 ={\theta e^{-\theta+o(1)}\over nd},
\tag{2.4}
\]

\[
 \Pr(X\text{ is covered})
 ={\theta e^{-\theta}+o(1)\over n},
\tag{2.5}
\]

and, for two distinct packets,

\[
 \Pr(E,F\text{ are both retained})
 \le p^2,
\tag{2.6}
\]

with the left side zero when `E` and `F` overlap.

#### Proof

Let `N_H(E)` be the packets meeting `E`, including `E`.  The union bound
and the first two Bonferroni terms give

\[
 \sum_{X\in E}d_H(X)
 -\sum_{\{X,Y\}\subseteq E}d_H(X,Y)
 \le |N_H(E)|
 \le\sum_{X\in E}d_H(X).
\]

Thus (2.1)--(2.2) imply

\[
 |N_H(E)|=nd(1+O(\varepsilon+\eta)).
\]

Therefore

\[
 p(1-p)^{|N_H(E)|-1}
 ={\theta e^{-\theta+o(1)}\over nd},
\]

which proves (2.4).  Retained packets through one vertex are mutually
exclusive, so summing (2.4) over its `(1+o(1))d` incident packets proves
(2.5).  Finally, simultaneous retention implies simultaneous independent
sampling, giving (2.6). \(\square\)

For a product residual at density `u=m^{-1/2+o(1)}`, equations
(1.11)--(1.12) predict (2.2) with `eta=m^{-1/2+o(1)`.  The unproved step is
that an actual residual produced by all preceding bites satisfies (2.1)
and (2.2) uniformly.

## 3. Exact two-time hypothesis that yields cumulative spread

One-round pair spread does not by itself imply spread for the union of
`Theta(n log m)` bites.  The needed longitudinal assumption can be stated
cleanly.

Let `R_t` be the random residual before round `t`, and let `u_t` be its
target density.  Suppose

\[
 u_{t+1}=u_t\left(1-{a+o(1)\over n}\right),
 \qquad a=\theta e^{-\theta},
\tag{3.1}
\]

and use

\[
 d_t=Du_t^{n-1},\qquad p_t={\theta\over nd_t}.
\tag{3.2}
\]

Assume the flat-link hypotheses (2.1)--(2.2) hold in every round with
uniform `o(1)` error.  In addition assume that, for all two disjoint
original packets `E,F` and all rounds `s,t`,

\[
 \boxed{
 \Pr(E\subseteq R_s,\ F\subseteq R_t)
 \le K_m u_s^n u_t^n,}
\tag{3.3}
\]

where `K_m=m^{o(1)}`.  This is the required **two-time hereditary
anti-clustering**.  It is stronger than degree regularity and is not a
consequence of (2.1)--(2.2).

### Theorem 3.1 (conditional multi-bite spread)

Under (3.1)--(3.3), stop at any time with
`u_T>=m^{-1/2+o(1)}`.  For the union `P` of all retained packets,

\[
 \boxed{
 \Pr(E,F\in P)\le {C_\theta K_m\over D^2}
 \qquad(E\ne F).}
\tag{3.4}
\]

Moreover the residual density is `m^{-1/2+o(1)}` after
`Theta(n log m)` rounds.

#### Proof

Overlapping packets can never both be retained.  For disjoint packets,
use a union bound over their two selection rounds.  Acceptance only lowers
probability, the round-sampling coins are independent, and (3.3) gives

\[
 \Pr(E,F\in P)
 \le K_m\left(\sum_{t<T}u_t^np_t\right)^2.
\]

But (3.2) gives

\[
 u_t^np_t={\theta u_t\over nD}.
\]

The geometric decay (3.1) implies

\[
 \sum_{t<T}{u_t\over n}=O_\theta(1).
\]

This proves (3.4).  Taking logarithms in (3.1) shows that reducing density
from one to `m^{-1/2+o(1)}` uses `Theta(n log m)` rounds. \(\square\)

Together with concentration of the residual size around `u_TW`, Theorem
3.1 would give exactly the spread near-matching required by prime-cycle
smoothing.

## 4. Scope correction for the stall claim

The statement

\[
 \mathbb E|\mathcal O_{\rm live}|=M u^K
\]

is exact only for exogenous independent survival of the `K` resources of
each catalogue edge (or its fixed-size hypergeometric analogue).  It has
two distinct limitations.

1. It is not a theorem about an endogenous residual produced by a matching
   algorithm.  Such a residual may preserve or destroy complete packets at
   rates very different from `u^K`.
2. Even in the product model, the relevant `K` must be the number of hard
   resources actually consumed.  The augmented multidepth template has
   `K=Theta(m^{3/2})` and stalls near density one.  A hard-middle wreath row
   has `K=n=Theta(m)` and its product catalogue survives down to density
   `Theta(1/m)`.

Hence the corrected conclusion is

\[
 \boxed{
 \begin{gathered}
 \text{the augmented hard-quota trajectory is product-stalled, but the}\\
 \text{hard-middle-only spread nibble is not stalled at }u=m^{-1/2+o(1)};
 \end{gathered}}
\]

the latter remains conditional on hereditary link-flatness (2.1)--(2.2),
two-time anti-clustering (3.3), and residual-size concentration.  These are
the exact probabilistic assumptions that heuristic product-survival
language had previously hidden.

## 5. A finite overlap polynomial controlling product-degree variance

There is a useful exact static form of the anti-clustering problem.  Fix a
middle owner `X` and a packet `E` containing it.  The stabilizer of `X` is
transitive on the `D` packets through `X`.  Define

\[
 G_m(z)={1\over D}\sum_{F\ni X}z^{|E\cap F|-1}.
\tag{5.1}
\]

Thus `G_m` is independent of the choices of `X` and `E`.

Condition on `X` surviving an independent vertex thinning of density `u`,
and let `Z_X` be its residual packet degree.  Expanding the second moment
over two packets through `X` gives the exact identity

\[
 \boxed{
 {\operatorname {Var}(Z_X\mid X\text{ survives})
  \over D^2u^{2n-2}}
 =G_m(1/u)-1.}
\tag{5.2}
\]

Indeed, two packets `E,F` through `X` require
`2(n-1)-(|E cap F|-1)` other vertices to survive.  Transitivity makes the
inner sum over `F` equal to (5.1), and
`E Z_X=Du^{n-1}`.

The first derivative of the overlap polynomial is already determined by
the exact packet codegrees.  A fixed packet has two other middle windows
at every Johnson distance `1<=s<=m` from `X`, so

\[
 \boxed{
 G_m'(1)
 =4\sum_{s=1}^{m}{1\over\binom ms\binom{m+1}s}
 ={4\over m+1}+O(m^{-2}).}
\tag{5.3}
\]

Thus two random packets conditioned to contain `X` have only `O(1/m)`
additional common owners on average.  The mean alone is insufficient at
`z=sqrt(m)`: rare large intersections receive exponential weight.

For the admissible stopping density
`u=omega(m)/sqrt(m)`, where `omega(m) tends to infinity` arbitrarily
slowly, the exact finite combinatorial gate for product-degree
concentration is

\[
 \boxed{G_m(\sqrt m/\omega(m))=1+o(1).}
\tag{5.4}
\]

By (5.2), (5.4) is equivalent to vanishing relative degree variance for a
fixed surviving owner.  A stronger estimate with high moments and a
summable tail would yield simultaneous degree flatness.

Packets through `X` have an explicit two-chain description.  Relative to
a fixed packet, a second packet is specified by an ordering of the `m`
elements of `X` and an ordering of its `m+1` complementary elements.  Its
windows away from `X` form two chains of equal-size prefix replacements.
For one prescribed pair of chain orientations, common windows are common
setwise cut points of those two random orders.  If
`d_1<...<d_k` are prescribed cut points and
`r_i=d_i-d_(i-1)`, their exact probability is

\[
 { (m-d_k)!(m+1-d_k)!\prod_{i=1}^k(r_i!)^2
  \over m!(m+1)!}.
\tag{5.5}
\]

The elementary factorial-convolution estimate

\[
 \sum_{s_1+\cdots+s_t=N\atop s_i\ge1}
       \prod_i(s_i!)^2
 \le C^{t-1}(N-t+1)!^2
\tag{5.6}
\]

follows by induction on `t`.  After applying the inductive bound, the
remaining convolution is, with `M=N-t+1`,

\[
 \sum_{s=1}^{M}s!^2(M-s+1)!^2
 =(M+1)!^2\sum_{s=1}^{M}\binom{M+1}s^{-2}
 \le C M!^2.
\]

The two endpoint summands in the last normalized sum are
`1/(M+1)^2`, and the interior summands are smaller.  Enlarging the
absolute constant closes the induction.

Applying (5.6) to (5.5) shows that the `k`-th cut-point factorial moment
for one fixed orientation pair is at most

\[
 C^k m^{-(2k-1)}.
\tag{5.7}
\]

Consequently one orientation pair alone has exponential moment
`1+O(z/m)` uniformly for `z=o(m^2)`.

The four comparisons are not arbitrary.  Call the two directional chains
of each packet `+` and `-`, and let `K_(epsilon,delta)` be the number of
common noncentral windows between direction `epsilon` of `F` and direction
`delta` of `E`.

### Lemma 5.1 (directional compatibility)

The nonzero entries of the two-by-two matrix
`(K_(epsilon,delta))` form a partial matching.  In particular, at most one
of

\[
 K_{+,+}+K_{-,-},\qquad K_{+,-}+K_{-,+}
\tag{5.8}
\]

is positive.

#### Proof

Along one direction of `F`, its removed sets and its inserted sets are
nested.  If this chain met both opposite directional chains of `E`, at
depths `d<=e`, a fixed prefix end-set of size `d` would have to be
contained in a fixed suffix end-set of size `e`.  In the removed universe
of size `m` this is possible only at `e=m`; in the inserted universe of
size `m+1`, where `e<=m`, it is still impossible.  Thus one row of the
comparison matrix has at most one nonzero entry.

If both directions of `F` met the same direction of `E`, at depths `d,e`,
the two domain end-sets have intersection size
`max(0,d+e-m)` in the removed universe, whereas their two equal target
end-sets have intersection size `min(d,e)`.  Equality forces
`max(d,e)=m`.  In the inserted universe of size `m+1`, the corresponding
domain intersection then has size `min(d,e)-1`, a contradiction.  Hence
one column also has at most one nonzero entry. \(\square\)

### Theorem 5.2 (two-sided overlap moment)

Uniformly for `1<=z=o(m)`,

\[
 \boxed{G_m(z)=1+O(z^2/m).}
\tag{5.9}
\]

In particular, (5.4) holds for every slowly diverging `omega(m)`.

#### Proof

Put

\[
 K_{\rm d}=K_{+,+}+K_{-,-},\qquad
 K_{\rm a}=K_{+,-}+K_{-,+}.
\]

Lemma 5.1 says that at most one is positive.  Therefore, pointwise,

\[
 z^{|E\cap F|-1}-1
 =(z^{K_{\rm d}}-1)+(z^{K_{\rm a}}-1).
\tag{5.10}
\]

For the diagonal term, Cauchy--Schwarz gives

\[
 \mathbb E z^{K_{+,+}+K_{-,-}}
 \le
 \left(\mathbb E z^{2K_{+,+}}
       \mathbb E z^{2K_{-,-}}\right)^{1/2}.
\]

Each factor is the one-orientation cut-point moment above evaluated at
`z^2`, hence is `1+O(z^2/m)` by (5.7).  The same argument applies to the
anti-diagonal term.  Taking expectations in (5.10) proves (5.9).
Substituting `z=sqrt(m)/omega(m)` gives an error `O(omega(m)^(-2))`.
\(\square\)

Combining (5.2) and (5.9) proves an unconditional static statement:
under independent thinning to density `omega(m)/sqrt(m)`, the residual
degree of any fixed surviving middle owner has relative variance
`O(omega(m)^(-2))`.  This is the first anti-clustering estimate needed by
the packet nibble.  Uniform simultaneous concentration and, more
importantly, the longitudinal two-time condition (3.3) remain open.

## 6. Exponential lower tail by Janson

The overlap estimate yields more than Chebyshev on the lower side.  Keep
the independent residual density

\[
 u={\omega\over\sqrt m},\qquad \omega\longrightarrow\infty,
 \qquad \omega=m^{o(1)},
\tag{6.1}
\]

and condition on `X` surviving.  For each packet `F` through `X`, let
`I_F` indicate that all other owners of `F` survive, so
`Z_X=sum_(F ni X)I_F` and `mu=E Z_X=Du^{n-1}`.

Two indicators have a dependency only when their packets share an owner
besides `X`.  For a fixed `F`, the number of such `G` is at most

\[
 \sum_{Y\in F\setminus\{X\}}d(X,Y)
 =D G_m'(1)=O(D/m).
\tag{6.2}
\]

Let `Delta` be the Janson dependency sum of joint expectations over
dependent pairs (either convention changes only an absolute factor).
All covariances are nonnegative.  Using (5.2), (5.9), and (6.2),

\[
 \begin{aligned}
 \Delta
 &\le O(\operatorname {Var}Z_X)
      +O(D^2u^{2n-2}/m)+O(\mu)\\
 &\le O\left({\mu^2\over\omega^2}\right),
 \end{aligned}
\tag{6.3}
\]

because `mu` is superpolynomially large by (1.6).

### Theorem 6.1 (fixed-owner lower tail)

For every fixed `0<epsilon<1`,

\[
 \boxed{
 \Pr\left(Z_X\le(1-\varepsilon)Du^{n-1}
       \mid X\text{ survives}\right)
 \le \exp(-c_\varepsilon\omega^2).}
\tag{6.4}
\]

#### Proof

The standard Janson lower-tail inequality for a sum of increasing
all-present events gives

\[
 \Pr(Z_X\le(1-\varepsilon)\mu)
 \le\exp\left(-{\varepsilon^2\mu^2
                    \over2(\mu+\Delta)}\right).
\]

Insert (6.3). \(\square\)

Consequently the expected number of surviving owners with degree below
`(1-epsilon)d(u)` is at most

\[
 uW\exp(-c_\varepsilon\omega^2).
\tag{6.5}
\]

Taking, for example, `omega=log m` makes this smaller than `uW/m^A` for
every fixed `A`.  Hence a quarantine of **low-degree** owners is negligible
even after the `n`-fold edge-incidence amplification.  This is stronger
than the variance-only estimate and avoids any union bound over all `W`
owners.

The corresponding upper tail, simultaneous control of the edgewise
codegree sum (2.2), and preservation under endogenous bites are not
provided by Janson's lower-tail inequality.  These are now the precise
remaining probabilistic pieces; the static low-degree tail is closed.

## 7. Global live-packet mass is sharply concentrated

Although the fixed-owner upper tail remains open, the **total** packet
mass has an immediate strong second-moment bound.  Let `Y` be the number
of packets wholly contained in the independent residual.  Then

\[
 \mathbb EY=Mu^n.
\]

For `z=1/u`, expanding the second moment gives

\[
 {\operatorname {Var}Y\over(\mathbb EY)^2}
 ={1\over M^2}\sum_{E,F}\bigl(z^{|E\cap F|}-1\bigr).
\tag{7.1}
\]

Only intersecting pairs contribute.  Since
`z^s-1<=z^s<=s z^s` for `s>=1`, double-counting a shared owner and using
the star polynomial (5.1) yields

\[
 \begin{aligned}
 \sum_{E,F}\bigl(z^{|E\cap F|}-1\bigr)
 &\le\sum_X\sum_{E,F\ni X}z^{|E\cap F|}\\
 &=W D^2 zG_m(z).
 \end{aligned}
\tag{7.2}
\]

Because `M=WD/n`,

\[
 \boxed{
 {\operatorname {Var}Y\over(\mathbb EY)^2}
 \le {n^2zG_m(z)\over W}.}
\tag{7.3}
\]

At `u=omega/sqrt(m)`, Theorem 5.2 makes the right side exponentially
small in `m`.  Together with ordinary binomial concentration of the
residual vertex count, this proves that the average residual packet degree
is `(1+o(1))d(u)` with overwhelmingly high probability.

Thus the remaining upper-tail issue is genuinely local: the total degree
mass is correct, and low-degree owners are exponentially rare, but one
still needs to prevent a small set of high-degree owners from concentrating
too much of that mass or to design bite weights which tolerate them.

## 8. Trimming removes the fixed-owner upper-tail requirement

For one bite, the last local upper-tail problem can in fact be avoided.
The point is to trim **edges with a large degree sum**, rather than trying
to prove a simultaneous upper bound for every vertex degree.

Take, for definiteness,

\[
 u={\log m\over\sqrt m},\qquad d=Du^{n-1},
\tag{8.1}
\]

and let `R` be the independent product residual.  Write `d_R(X)` for the
degree of a surviving owner and `Y` for the number of live packets.

### Proposition 8.1 (a typical trimmable product residual)

With probability tending to one, all of the following hold (and the
relative `o(1)` errors in (8.2) may be taken to be `o(epsilon)`):

\[
 |R|=(1+o(1))uW,qquad
 Y=(1+o(1))Mu^n,
\tag{8.2}
\]

\[
 \sum_{X\in R}(d_R(X)-d)^2
 \le { |R|d^2\over\log m},
\tag{8.3}
\]

and, with

\[
 \varepsilon=(\log m)^{-1/4},
\tag{8.4}
\]

the number of owners satisfying
`d_R(X)<(1-epsilon)d` is at most

\[
 |R|\exp\bigl(-c(\log m)^{3/2}\bigr).
\tag{8.5}
\]

#### Proof

The two assertions in (8.2) are ordinary binomial concentration and
(7.3), respectively.  By transitivity and (5.2),

\[
 \mathbb E\sum_{X\in R}(d_R(X)-d)^2
 =uWd^2\bigl(G_m(1/u)-1\bigr)
 =O\left({uWd^2\over(\log m)^2}\right).
\]

Markov's inequality proves (8.3) with failure probability `O(1/log m)`.
Finally the proof of Theorem 6.1, with a varying lower-tail parameter,
gives

\[
 \Pr(d_R(X)<(1-\varepsilon)d\mid X\in R)
 \le \exp(-c\varepsilon^2(\log m)^2)
 =\exp\bigl(-c(\log m)^{3/2}\bigr).
\]

Markov's inequality, enlarging the right side by (say) the square root of
its exponential factor, proves (8.5) after changing `c`.  The four events
therefore hold simultaneously with probability tending to one. \(\square\)

Fix a realization satisfying Proposition 8.1.  Call an owner **low** if
its degree is below `(1-epsilon)d`, and delete every packet containing a
low owner.  Since a low owner has degree at most `d`, the proportion of
live packets deleted is at most

\[
 {d\,|R|e^{-c(\log m)^{3/2}}\over Y}
 \le n e^{-c(\log m)^{3/2}}=o(m^{-A})
\tag{8.6}
\]

for every fixed `A`.

For a remaining packet `E`, define its **original degree sum**

\[
 A_E=\sum_{X\in E}d_R(X).
\tag{8.7}
\]

Every remaining packet satisfies

\[
 A_E\ge(1-\varepsilon)nd.
\tag{8.8}
\]

On the other hand, double counting and (8.3) give

\[
 \sum_{E\text{ live}}A_E
 =\sum_{X\in R}d_R(X)^2
 \le(1+o(\varepsilon))ndY.
\tag{8.9}
\]

Here one expands `d_R(X)^2` around `d`, uses
`sum_X d_R(X)=nY`, and invokes (8.2)--(8.3).

Put

\[
 \delta=\sqrt\varepsilon=(\log m)^{-1/8}.
\tag{8.10}
\]

Equations (8.8)--(8.9) imply that the proportion `beta` of the remaining
packets with `A_E>(1+delta)nd` satisfies

\[
 \beta=O(\varepsilon/\delta)+o(1)=O(\sqrt\varepsilon)=o(1).
\tag{8.11}
\]

Delete these high-degree-sum packets as well.  The total number of lost
edge--owner incidences is at most `(beta+o(1))nY`.  Hence, if

\[
 \gamma=\sqrt\beta,
\tag{8.12}
\]

all but `O(sqrt(beta))|R|=o(|R|)` nonlow owners lose at most `gamma d`
incident packets.  Let `R_good` be the set of those undamaged nonlow
owners, and let `H_good` be the packet family left after the two edge
deletions.

### Theorem 8.2 (trimmed product-residual bite)

There is a product-residual realization and a subhypergraph `H_good` such
that

\[
 |R_{\rm good}|=(1-o(1))uW,
\tag{8.13}
\]

every `X in R_good` has

\[
 d_{H_{\rm good}}(X)\ge(1-o(1))d,
\tag{8.14}
\]

and every `E in H_good` satisfies

\[
 |N_{H_{\rm good}}(E)|\le(1+o(1))nd.
\tag{8.15}
\]

Consequently, if every edge of `H_good` is sampled independently with

\[
 p={\theta\over nd}
\]

and only isolated sampled edges are retained, then for every
`X in R_good`,

\[
 \boxed{
 \Pr(X\text{ is covered})
 \ge {\theta e^{-\theta}-o(1)\over n}.}
\tag{8.16}

For two distinct original packets `E,F`,

\[
 \boxed{\Pr(E,F\text{ are both retained})\le p^2,}
\tag{8.17}
\]

with probability zero when they overlap.

#### Proof

The preceding trimming argument proves (8.13)--(8.14).  For a retained
edge,

\[
 |N_{H_{\rm good}}(E)|
 \le\sum_{X\in E}d_{H_{\rm good}}(X)
 \le\sum_{X\in E}d_R(X)=A_E
 \le(1+\delta)nd,
\]

which is (8.15).  Thus every retained-catalogue edge is isolated after
sampling with probability at least

\[
 p(1-p)^{(1+o(1))nd}
 ={\theta e^{-\theta}-o(1)\over nd}.
\]

Retained edges through a fixed owner are mutually exclusive.  Summing
the last display over the `(1-o(1))d` available edges through a good
owner gives (8.16).  Simultaneous retention requires simultaneous
independent sampling, proving (8.17). \(\square\)

There is also a deterministic global consequence of the same random
bite.  Let `A` be the number of retained edges and let `D_Y` be the number
of live catalogue edges destroyed by deleting their owners.

### Corollary 8.3 (one bite preserves global packet mass)

There are absolute constants `c,C>0` such that, for every sufficiently
small fixed `theta>0`, some outcome of the bite in
Theorem 8.2 satisfies

\[
 A\ge c\theta {|R|\over n^2},
 \qquad
 D_Y\le C\theta Y.                                             \tag{8.18}
\]

Thus the bite covers `Omega(theta|R|/n)` owners while destroying only an
`O(theta)` fraction of the live packet catalogue.

#### Proof

Summing the edge-retention lower bound in Theorem 8.2 gives

\[
 \mathbb EA\ge(\theta e^{-\theta}-o(1)){Y\over nd}
 =(\theta e^{-\theta}-o(1)){|R|\over n^2}.                     \tag{8.19}
\]

For distinct edges, simultaneous retention has probability at most
`p^2`, so

\[
 \mathbb E[A(A-1)]\le Y^2p^2=O_\theta((\mathbb EA)^2).          \tag{8.20}
\]

For `theta` in a fixed sufficiently small interval, Paley--Zygmund gives
an absolute constant lower bound for `A` to exceed half its mean.  On the
other hand, a fixed live
edge is destroyed only if some retained edge in its neighborhood was
sampled.  By (8.15),

\[
 \mathbb E D_Y
 \le\sum_Ep|N(E)|
 \le(1+o(1))\theta Y.                                         \tag{8.21}
\]

Choose the absolute `C` so large that Markov's upper bound for failure of the
second event is smaller than the Paley--Zygmund lower bound for the first.
The two events then intersect with positive probability, proving
(8.18). \(\square\)

Theorem 8.2 closes the static one-bite problem without any uniform
fixed-owner upper-tail theorem and without the edgewise codegree
hypothesis (2.2).  It does **not** yet iterate: after the first bite the
residual is endogenous, and neither (8.3) nor the two-time condition
(3.3) is currently known to persist.  The remaining packet-nibble gate
is therefore longitudinal, not static.

## 9. The edgewise link sum can be trimmed simultaneously

Although Theorem 8.2 does not need (2.2), the product residual also has
enough average link control to impose it at negligible extra cost.  This
is useful for any attempted longitudinal propagation theorem.

For a live packet `E`, put

\[
 B_E=\sum_{\{X,Y\}\subseteq E}d_R(X,Y).
\tag{9.1}
\]

Let

\[
 H_E(z)=\sum_F z^{|E\cap F|},
\]

where `F` ranges over all packets.  Double counting a marked common owner
and using (5.1) gives the exact derivative identity

\[
                         H_E'(z)=nD G_m(z).                     \tag{9.2}
\]

Conditioning on `E` being live and then summing over the second packet
gives

\[
 \begin{aligned}
 \mathbb E(B_E\mid E\text{ live})
 &=\sum_F\binom{|E\cap F|}{2}u^{n-|E\cap F|}\\
 &={nD\over2}u^{n-2}G_m'(1/u).
 \end{aligned}                                                  \tag{9.3}
\]

The positivity of the nonconstant coefficients gives, for `z>=1`,

\[
 G_m'(z)
 \le {G_m(2z)-G_m(0)\over z},                                  \tag{9.4}
\]

because `k<=2^k` for every `k>=1`.  Theorem 5.2 applied at `2z=o(m)`
and `1-G_m(0)<=G_m'(1)=O(1/m)` from (5.3) therefore yield

\[
                         G_m'(z)=O(z/m).                         \tag{9.5}
\]

At `u=omega/sqrt(m)`, equations (9.3)--(9.5) imply

\[
 {\mathbb E(B_E\mid E\text{ live})\over nd(u)}
 ={G_m'(1/u)\over2u}
 =O(\omega^{-2}).                                               \tag{9.6}
\]

For `omega=log m`, sum (9.6) over `E`, use Markov once for the total
link mass, and combine it with the typical realization of Proposition
8.1.  With probability tending to one after a harmless weakening of the
constant,

\[
                         \sum_{E\text{ live}}B_E
 \le {ndY\over\log m}.                                         \tag{9.7}
\]

Delete all edges with

\[
                         B_E>(\log m)^{-1/4}nd.                  \tag{9.8}
\]

Their proportion is `O((log m)^(-3/4))`.  Repeating the incidence-loss
argument from (8.11)--(8.14) shows that, after discarding only `o(|R|)`
additional damaged owners, every remaining good owner still has
`(1-o(1))d` available edges.  The final trimmed catalogue therefore has,
simultaneously,

\[
 \begin{gathered}
 d_H(X)\ge(1-o(1))d\quad\text{for }(1-o(1))|R|\text{ owners},\\
 |N_H(E)|\le(1+o(1))nd,\\
 \sum_{\{X,Y\}\subseteq E}d_H(X,Y)
 \le(\log m)^{-1/4}nd\quad(E\in H).
 \end{gathered}                                                  \tag{9.9}
\]

Thus all deterministic local hypotheses of a standard one-bite nibble
can be recovered from the product model by trimming.  The sole unproved
step is to recover an analogue of (9.7)--(9.9) after the residual has
been generated by earlier matching bites rather than by independent
vertex thinning.

## 10. Every matching residual is exactly point-balanced

The endogenous residual is not arbitrary.  It retains one exact design
constraint at every time, which removes the most obvious hereditary
counterexamples.

### Lemma 10.1 (residual one-design)

Let `P` be any packet matching of size `t`, and let

\[
                         R=\binom{[n]}m\setminus\bigcup_{E\in P}E.
\]

Then

\[
                         |R|=W-nt,                              \tag{10.1}
\]

and, for every coordinate `x`,

\[
 \boxed{
 \#\{X\in R:x\in X\}={m\over n}|R|.}                          \tag{10.2}
\]

Equivalently, the centered indicator of `R` has no constant or
degree-one Johnson harmonic.

#### Proof

One cyclic wreath packet has `n` middle windows.  A fixed coordinate
belongs to exactly `m` of them, namely the windows whose `m` possible
starts precede that coordinate.  Since packets in `P` are disjoint on
middle owners, deleting `t` packets removes `nt` owners and exactly `mt`
owners containing each fixed coordinate.  The full middle layer contains
`mW/n` owners through each coordinate, proving (10.1)--(10.2). \(\square\)

Thus the star residual which kills every packet is impossible along a
legal matching trajectory.  Point balance alone is unlikely to force
packet abundance--pair and higher correlations remain uncontrolled--but
any longitudinal counterexample or propagation theorem must begin in
Johnson harmonic degree at least two.  This is the exact deterministic
state constraint available for the next step.

Point balance by itself is definitely insufficient.  At `m=3,n=7`, take
the seven triples of the Fano plane.  Every coordinate lies in exactly
three triples, so this seven-owner set is point-balanced.  Any two Fano
lines intersect, however, whereas consecutive owners in a wreath packet
are disjoint.  The induced packet catalogue is therefore empty.  Thus a
longitudinal theorem must use the fact that the residual was generated by
a particular random packing trajectory, not merely the one-design
identity (10.2).

## 11. Equivalent shortest-odd-cycle formulation

There is a graph-theoretic restatement of the longitudinal gate.  Let

\[
                         O_n=KG(2m+1,m)
\]

be the odd graph on the middle layer.  Its odd girth is `n=2m+1`, and its
shortest odd cycles are exactly the wreath packets.  Hence, for every
residual owner set `R`,

\[
 \begin{array}{c}
 \text{live packets in the packet hypergraph}\[1mm]
 \text{are exactly the copies of `C_n` in the induced graph `O_n[R]`.}
 \end{array}                                                     \tag{11.1}
\]

A packet matching is equivalently a vertex-disjoint packing of shortest
odd cycles.  Lemma 10.1 says that after deleting any such packing, the
remaining vertex set is an exact one-design in the Boolean coordinates.
The product calculations of Sections 5--9 are therefore a sharp
supersaturation statement for `C_n` in a random induced subgraph of the
odd graph, including overlap control between cycles through a fixed
vertex.

This equivalence has an exact matrix form.  Let `A_R` be the adjacency
matrix of `O_n[R]`.  Since `O_n` has odd girth `n`, every closed walk of
length `n` is a simple shortest odd cycle: deleting a backtrack from any
other closed odd walk would produce an odd closed walk of length below
`n`.  Therefore

\[
 \boxed{
 Y_R={1\over2n}\operatorname {tr}(A_R^n),\qquad
 d_R(X)={1\over2}(A_R^n)_{X,X}.}                                \tag{11.2}
\]

The factors `2n` and `2` are the two orientations and the choices of a
starting vertex.  Thus global packet mass and local packet degree are
respectively the trace and diagonal of one high odd power of the induced
odd-graph adjacency matrix.  A longitudinal theorem may equivalently be
stated as preservation of the trace and most diagonal entries in (11.2).

In this language the remaining theorem is:

> prove that a suitably chosen random greedy packing of vertex-disjoint
> shortest odd cycles keeps `O_n[R_t]` cycle-supersaturated and
> overlap-flat until `|R_t|=m^{-1/2+o(1)}W`, with the required two-time
> spread.

This is not supplied by ordinary edge expansion of `O_n`: counting an
`n`-cycle is a high-order condition, and exact point balance removes only
the first Johnson harmonic.  It does, however, identify the longitudinal
problem as a structured odd-cycle supersaturation/packing theorem rather
than an arbitrary growing-uniformity hypergraph assertion.

## 12. The overlap error has a summable trajectory budget

There is one favorable quantitative fact for a perturbative longitudinal
proof.  The static overlap errors do not accumulate by a factor equal to
the number of bites, provided the one-step error is proportional to the
fraction removed in that bite.

For `u>=omega/sqrt(m)`, Theorem 5.2 and (9.5) give

\[
 \kappa(u):=G_m(1/u)-1=O\left({1\over mu^2}\right),             \tag{12.1}
\]

\[
 \ell(u):={G_m'(1/u)\over2u}
 =O\left({1\over mu^2}\right).                                 \tag{12.2}
\]

Suppose an ideal small-bite trajectory satisfies

\[
 \log u_{t+1}-\log u_t=-{a_t\over n}+o(a_t/n),
 \qquad \max_t a_t=o(1).                                       \tag{12.3}
\]

Then the Riemann-sum comparison gives

\[
 \boxed{
 \sum_t{a_t\over n}\kappa(u_t)
 +\sum_t{a_t\over n}\ell(u_t)
 =O\left({1\over m u_T^2}\right).}                             \tag{12.4}
\]

Indeed,

\[
 \int_{u_T}^{1}{1\over mu^2}\,{du\over u}
 ={1\over2m}(u_T^{-2}-1).                                      \tag{12.5}
\]

At the admissible stopping density `u_T=omega/sqrt(m)`, the right side of
(12.4) is `O(omega^{-2})=o(1)`.

Thus the `Theta(n log m)` number of rounds is not itself an accumulation
obstruction.  What is needed is a one-step propagation estimate in which
the deviation from the product trajectory is

\[
 O\left({a_t\over n}
 [\kappa(u_t)+\ell(u_t)]\right)                                 \tag{12.6}
\]

rather than an unweighted `O(kappa+ell)` error.  Equations
(12.1)--(12.5) would then sum that deviation to `o(1)` all the way to the
target leave.  This is a sharper longitudinal gate than simply demanding
uniform product-likeness after every bite.

## 13. A rigorous first endogenous propagation step

The first bite, starting from the full catalogue, already has the desired
bite-weighted **variance** error.  This does not yet give induction, but it
shows that this part of the target scale in (12.6) is attainable rather
than merely formal.  The aggressive lower coupling below has an additional
`O(theta^2)` drift bias relative to the isolated-bite density; over a long
iteration it can be made negligible by taking, for example,
`theta=o(1/(n log m))`.

Sample every packet of the full packet hypergraph with probability

\[
                         p={\theta\over nD},                     \tag{13.1}
\]

where `theta>0` is sufficiently small (and may tend to zero).  The actual bite
retains only isolated sampled packets.  Couple it to the more aggressive
process which deletes every owner lying in **any** sampled packet,
including nonisolated ones.  The aggressive residual is contained in the
actual residual, so its packet degrees are lower bounds for the actual
ones.

Fix an owner `X`.  For a packet `F` through `X`, let `I_F` be the
indicator that no sampled packet meets `F`, and put

\[
                         Z_X=\sum_{F\ni X}I_F.                  \tag{13.2}
\]

Thus `Z_X` is the aggressive residual degree of `X`, with value zero when
`X` itself is aggressively deleted.

### Theorem 13.1 (first-bite lower-degree propagation)

Uniformly in `X`,

\[
 \mathbb EZ_X=D\left(e^{-\theta}+O(\theta/n)\right),            \tag{13.3}
\]

\[
 \boxed{
 \operatorname {Var}Z_X=O\left({\theta\over n}D^2\right).}     \tag{13.4}
\]

Consequently there is an isolated-edge bite for which all but
`O((theta/n)^(1/2)+theta^(1/2))W` owners of the actual residual have
degree

\[
 \boxed{
 d_{\rm new}(X)
 =\left(e^{-\theta}
 \pm O((\theta/n)^{1/4}+\theta^{3/2})\right)D.}                 \tag{13.5}
\]

The same outcome may be chosen to cover `Omega(theta W/n)` owners.
In particular, the exceptional fraction is `o(1)` whenever
`theta=theta_m` tends to zero.

#### Proof

By transitivity, every packet has the same conflict-neighborhood size
`L`.  The first two union terms and (1.11) give

\[
                         nD-O(D)\le L\le nD.                    \tag{13.6}
\]

Hence, with `q=(1-p)^L`,

\[
                         q=e^{-\theta}+O(\theta/n),
 \qquad \mathbb EZ_X=Dq,                                      \tag{13.7}
\]

which proves (13.3).

For two packets `F,G` through `X`, put

\[
                         C(F,G)=|N(F)\cap N(G)|.
\]

Then

\[
 \operatorname {Cov}(I_F,I_G)
 =q^2\left((1-p)^{-C(F,G)}-1\right)
 \le C_\theta q^2pC(F,G),                                     \tag{13.8}
\]

because `pC(F,G)<=pL<=theta`.

For a packet `E`, let

\[
 c_X(E)=\#\{F:F\ni X,\ F\cap E\ne\varnothing\}.
\]

Double counting a common conflict packet gives

\[
 \sum_{F,G\ni X}C(F,G)=\sum_Ec_X(E)^2.                         \tag{13.9}
\]

The `D` packets containing `X` contribute exactly `D^3` to the last
sum.  If `E` does not contain `X`, then

\[
 c_X(E)\le\sum_{Y\in E}d(X,Y),
 \qquad
 c_X(E)^2\le n\sum_{Y\in E}d(X,Y)^2.                           \tag{13.10}
\]

The exact codegree formula (1.7) gives

\[
 \sum_{Y\ne X}d(X,Y)^2
 =4D^2\sum_{s=1}^m{1\over\binom ms\binom{m+1}s}
 =O(D^2/m).                                                     \tag{13.11}
\]

Summing (13.10) first over `E` and then over `Y`, using that every `Y`
lies in `D` packets, yields

\[
                         \sum_Ec_X(E)^2=O(D^3),                 \tag{13.12}
\]

because `n/m=O(1)`.  Equations (13.8)--(13.12), together with the
individual variances `O(D)`, prove

\[
 \operatorname {Var}Z_X
 \le O(D)+O(pD^3)
 =O((\theta/n)D^2),
\]

as `D` is superpolynomial.  This is (13.4).

Take `epsilon=(theta/n)^(1/4)`.  Chebyshev and (13.4) show that the
expected fraction of owners with
`|Z_X-e^{-theta}D|>O(epsilon D)` is
`O((theta/n)^(1/2))`.  Markov gives an outcome with the asserted number
of exceptional owners for the aggressive residual.

It remains to compare the actual and aggressive residual degrees.  If a
packet `F` survives the actual bite but not the aggressive deletion, then
some sampled packet `E` meeting `F` was nonisolated, so a second packet in
`N(E)` was also sampled.  A union bound using (13.6) gives

\[
 \Pr(F\text{ is rescued})
 \le L^2p^2=O(\theta^2).                                       \tag{13.13a}
\]

Hence the expected rescued degree at a fixed owner is `O(theta^2D)`.
After averaging over owners, Markov shows that all but
`O(theta^(1/2))W` owners receive at most `O(theta^(3/2)D)` rescued
packets.  This proves the two-sided estimate (13.5).

Finally, the isolated-edge count has expectation
`Theta(theta W/n^2)` and second factorial moment at most its independent
sampling bound, exactly as in Corollary 8.3.  Paley--Zygmund and a weighted
choice of the two good events give the same outcome with
`Omega(theta W/n^2)` retained packets, covering
`Omega(theta W/n)` owners. \(\square\)

The new missing step is now sharply hereditary: reproduce (13.12), with
the correct current normalization, after previous bites.  The first
endogenous step itself has the desired `theta/n` variance scale.

The proof isolates a reusable deterministic condition.  For an arbitrary
residual packet hypergraph `H`, define

\[
 c_X(E)=\#\{F\in H:X\in F,\ F\cap E\ne\varnothing\},
 \qquad
 T_X(H)=\sum_{E\in H}c_X(E)^2.                                 \tag{13.13}
\]

### Proposition 13.2 (hereditary one-step criterion)

Suppose, for some current degree scale `d`, that

\[
 d_H(X)=(1+o(1))d,qquad
 |N_H(F)|=(1+o(1))nd,                                          \tag{13.14}
\]

and

\[
 \boxed{T_X(H)=O(d^3)}                                         \tag{13.15}
\]

for all but `o(|V(H)|)` owners `X`.  If `theta=theta_m` tends to zero
slowly enough that the expected bite size tends to infinity, then one
isolated-edge bite at sampling rate `p=theta/(nd)` has an outcome covering
`Omega(theta|V(H)|/n)` owners such that, apart from `o(|V(H)|)` owners,
the new degrees are at least

\[
                         (e^{-\theta}-o(1))d.                  \tag{13.16}
\]

More quantitatively, the aggressive coupling degree at every owner
satisfying (13.15) has relative variance `O(theta/n)+o(1)`, and the mean
rescued degree in passing to the actual bite is `O(theta^2d)`.

#### Proof

Repeat (13.7)--(13.9) inside `H`.  Condition (13.14) gives the mean in
(13.16), while (13.15) gives

\[
 \operatorname {Var}Z_X
 \le O(d)+O(pT_X(H))
 =O((\theta/n)d^2)+o(d^2).
\]

Chebyshev, averaging over owners, and the same Paley--Zygmund intersection
argument as in Theorem 13.1 prove the assertion. \(\square\)

Thus the longitudinal problem no longer asks for full product
distribution at each time.  It asks for propagation of the single local
third-overlap moment (13.15), together with first-order degree and
neighborhood flatness.  The exact full-catalogue calculation proves its
initial value; its hereditary drift remains open.

## 14. Exact drift of the third-overlap moment

The one-step drift of `T_X` can also be written exactly enough to expose
the next obstruction.  For packets `A,B`, write

\[
                         C(A,B)=|N_H(A)\cap N_H(B)|.             \tag{14.1}
\]

Let `Q_X` be the set of ordered triples `(E,F,G)` such that
`F,G` contain `X` and `E` meets both `F` and `G`.  Then

\[
                         |Q_X|=T_X(H).                          \tag{14.2}
\]

Define the fourth-overlap sum

\[
 U_X(H)=\sum_{(E,F,G)\in Q_X}
 [C(E,F)+C(E,G)+C(F,G)].                                       \tag{14.3}
\]

### Proposition 14.1 (third-moment drift inequality)

Assume every packet neighborhood has size `(1+O(epsilon))nd`, and take
the sampling rate `p=theta/(nd)`.  If `T_X^{ag}` denotes the new
third-overlap moment in the aggressive sampled-edge deletion, then

\[
 \boxed{
 \mathbb E T_X^{ag}
 \le e^{-3\theta+O(\theta\varepsilon)}
 \left[T_X(H)+{C\theta\over nd}U_X(H)\right].}                 \tag{14.4}
\]

For the actual isolated-edge bite,

\[
 \boxed{
 \mathbb E T_X^{act}
 \le e^{-3\theta+O(\theta\varepsilon)}
 \left[T_X(H)+{C\theta\over nd}U_X(H)\right]
 +O(\theta^2T_X(H)).}                                         \tag{14.5}
\]

#### Proof

Expand `T_X^{ag}` over `Q_X`.  A fixed triple survives precisely when no
sampled packet belongs to

\[
                         N(E)\cup N(F)\cup N(G).
\]

The first two union terms give

\[
 |N(E)\cup N(F)\cup N(G)|
 \ge3(1-O(\varepsilon))nd
   -C(E,F)-C(E,G)-C(F,G).                                      \tag{14.6}
\]

Since the last sum is at most `3(1+O(epsilon))nd`, and `theta` is small,
the elementary bound `exp(x)<=1+C_theta x` on the relevant compact
interval gives (14.4) after summing over `Q_X`.

For (14.5), a packet which survives the actual bite but not aggressive
deletion must be rescued by a nonisolated sampled neighbor.  The argument
of (13.13a) bounds this probability by `O(theta^2)` for each of the three
packets in a candidate triple.  A union bound over the triple and then
over `Q_X` gives the final term. \(\square\)

In particular, the natural next hereditary estimate is

\[
 \boxed{U_X(H)=O(dT_X(H)).}                                    \tag{14.7}
\]

Under (14.7), (14.4) has only an `O(theta/n)` relative overlap error;
the isolation correction is `O(theta^2)` and can be made summable by the
infinitesimal-bite choice already noted in Section 13.  The crude bound
`U_X<=O(ndT_X)` loses exactly the factor `n` and gives no useful drift.
Thus (13.15) alone does not close under the present argument: propagation
reduces to the packet-specific fourth-overlap estimate (14.7), or to a
self-correcting substitute which controls the same size-biased common
neighborhoods.

The full catalogue satisfies (14.7) as well; this is another exact
starting-scale calculation.

### Lemma 14.2 (full-catalogue fourth overlap)

For the full wreath-packet hypergraph and every owner `X`,

\[
                         \boxed{U_X=O(D^4)=O(DT_X).}             \tag{14.8}
\]

#### Proof

First observe that for any two packets `A,B`,

\[
                         C(A,B)\le D(|A\cap B|+C_0)             \tag{14.9}
\]

for an absolute constant `C_0`.  Indeed, upper-bound a common conflict
packet by choosing one of its owners in `A` and one in `B`, and sum the
corresponding packet codegrees.  Equal owner pairs contribute
`D|A cap B|`.  A fixed owner of `A` is disjoint from at most two owners of
`B`: the latter owners are cyclic `m`-intervals, and at most two such
intervals fit inside one fixed `(m+1)`-set.  These disjoint pairs therefore
contribute `O(D)`.  Every remaining distinct pair has Johnson distance in
`1,...,m-1`, hence codegree at most `2D/[m(m+1)]` by (1.7); all `n^2` of
them again contribute `O(D)`.  This proves (14.9).

For packets `F,G` chosen uniformly through `X`, put
`K=|F cap G|-1`.  Theorem 5.2 at the fixed value `z=2` gives

\[
                         \mathbb E 2^K=1+O(1/m).
\]

Since `K^2<=C2^K` for nonnegative integral `K`,

\[
                         \mathbb E(|F\cap G|+1)^2=O(1).         \tag{14.10}
\]

Equations (14.9)--(14.10) imply

\[
 \sum_{F,G\ni X}C(F,G)^2=O(D^4),                               \tag{14.11}
\]

which controls the `C(F,G)` part of (14.3).

For the `C(E,F)` part, set

\[
                         a_X(E)=\sum_{Y\in E}d(X,Y).
\]

If `E` does not contain `X`, then `c_X(E)<=a_X(E)`, and (14.9) gives

\[
 \sum_{F\ni X,\,F\cap E\ne\varnothing}C(E,F)
 \le C D a_X(E).                                                \tag{14.12}
\]

The calculation in (13.10)--(13.12) gives

\[
                         \sum_{E\not\ni X}a_X(E)^2=O(D^3).     \tag{14.13}
\]

Thus the contribution of all such `E` to (14.3) is `O(D^4)`.  If
`E` contains `X`, then `c_X(E)=D`; (14.9) and (14.10), now only at first
moment, give

\[
 \sum_{F\ni X}C(E,F)=O(D^2).
\]

There are `D` choices of `E`, so these contribute another `O(D^4)`.
The `C(E,G)` term is identical.  Summing the three parts proves
(14.8). \(\square\)

Therefore both the third- and fourth-overlap conditions needed by the
drift argument hold at time zero with absolute constants.  The remaining
issue is genuinely their **renormalized hereditary propagation**, not a
missing initial moment estimate.

## 15. Drift of the fourth-overlap moment

Write a term of `U_X` as a tagged ordered quadruple

\[
                         (E,F,G;A,ij),                           \tag{15.1}
\]

where `(E,F,G) in Q_X`, the tag `ij` is one of `EF,EG,FG`, and `A` is a
packet in the common conflict neighborhood of the tagged pair.  Let
`R_X` be this multiset of tagged quadruples, so `|R_X|=U_X`.
For `r=(E,F,G;A,ij)`, let `P(r)` be its four packet slots and put

\[
 V_X(H)=\sum_{r\in R_X}\sum_{B<C\in P(r)}C(B,C),                \tag{15.2}
\]

with repeated slots retained according to their multiplicity.

Exactly the same union-neighborhood expansion as in Proposition 14.1
gives the next drift formula.

### Proposition 15.1 (fourth-moment drift inequality)

Under the hypotheses and notation of Proposition 14.1,

\[
 \boxed{
 \mathbb E U_X^{ag}
 \le e^{-4\theta+O(\theta\varepsilon)}
 \left[U_X(H)+{C\theta\over nd}V_X(H)\right],}                 \tag{15.3}
\]

and

\[
 \boxed{
 \mathbb E U_X^{act}
 \le e^{-4\theta+O(\theta\varepsilon)}
 \left[U_X(H)+{C\theta\over nd}V_X(H)\right]
 +O(\theta^2U_X(H)).}                                         \tag{15.4}
\]

#### Proof

Expand the new `U_X` over the current tagged quadruples.  In the
aggressive process a term survives only if no sampled packet lies in the
union of the four packet neighborhoods.  The first two union terms give

\[
 \left|\bigcup_{B\in P(r)}N(B)\right|
 \ge4(1-O(\varepsilon))nd-
   \sum_{B<C\in P(r)}C(B,C).
\]

Linearizing the bounded exponential correction and summing proves
(15.3).  If a tagged quadruple survives the actual but not the aggressive
process, at least one of its four slots is rescued by a nonisolated
sampled neighbor.  Equation (13.13a) and a four-term union bound give the
last term in (15.4). \(\square\)

Thus a finite two-moment induction would close if one had the
self-bounding estimate

\[
                         \boxed{V_X(H)=O(dU_X(H)).}              \tag{15.5}
\]

Equations (14.7) and (15.5) would propagate `(T_X,U_X)` with relative
overlap error `O(theta/n)` per bite, while the `O(theta^2)` isolation bias
is summable for infinitesimal bites.  Proposition 15.1 does not by itself
close a two-component induction: one must either prove that (15.5) is
self-preserving, or control the next size-biased common-neighborhood
moment generated when (15.5) is propagated.

The corresponding time-zero fifth-overlap estimate can be proved by one
additional quadratic link calculation.  This avoids iterating a
first-moment estimate after a size-biased common-neighbor choice.

### Lemma 15.2 (full-catalogue fifth overlap)

For the full packet catalogue,

\[
                         \boxed{V_X=O(D^5)=O(DU_X).}             \tag{15.6}
\]

#### Proof

We first record the owner-to-packet link sum.  If `Y` is an owner not
lying in a packet `P`, then

\[
                         \sum_{Z\in P}d(Y,Z)=O(D/m).            \tag{15.7}
\]

Indeed at most two cyclic `m`-windows of `P` are disjoint from `Y`; they
contribute `O(D/m)` by (1.7).  Every other distinct window has codegree at
most `2D/[m(m+1)]`, and there are `n` of them.  If `Y in P`, the same sum
is `D+O(D/m)`.

For packets `P,Q,R`, this gives both

\[
 |N(P)\cap N(Q)|\le D(|P\cap Q|+C)                             \tag{15.8}
\]

and the uniform first weighted-link estimate

\[
 \sum_{A\in N(P)\cap N(Q)}|A\cap R|
 \le D(|P\cap Q\cap R|+C)
 \le D(|P\cap Q|+C).                                           \tag{15.9}
\]

For (15.8), mark an owner in each of the two intersections and sum the
corresponding owner codegrees.  For (15.9), fix `Y in R`.  The number of
packets through `Y` which meet both `P` and `Q` is at most

\[
 \min\left\{\sum_{Z\in P}d(Y,Z),
             \sum_{Z\in Q}d(Y,Z)\right\}.
\]

This is `D+O(D/m)` when `Y in P cap Q`, and `O(D/m)` otherwise.
Summing over the `n` choices of `Y` proves (15.9).

The only further input is a quadratic version for the root triangle.
Fix packets `F,G`, put `s=|F cap G|`, and sum over
`E in N(F) cap N(G)`.  Then

\[
 \begin{aligned}
 \sum_E1&=O(D(s+1)),\\
 \sum_E |E\cap F|\,|E\cap G|&=O(D(s+1)),\\
 \sum_E |E\cap F|^2+
 \sum_E |E\cap G|^2&=O(D(s+1)).
 \end{aligned}                                                 \tag{15.10}
\]

The middle identity follows simply by dropping the now redundant common-
neighbor restriction and expanding:

\[
 \sum_E |E\cap F|\,|E\cap G|
 =\sum_{Y\in F,Z\in G}d(Y,Z)=O(D(s+1))
\]

by (15.7).  For the square term, use `|E cap G|>=1` and expand

\[
 \sum_{E\in N(F)\cap N(G)}|E\cap F|^2
 \le\sum_{Y,Z\in F,T\in G}d(Y,Z,T),                            \tag{15.11}
\]

where `d(Y,Z,T)` is the number of packets through the displayed owners.
The diagonal `Y=Z` contributes
`sum_(Y in F,T in G)d(Y,T)=O(D(s+1))`.  For `Y ne Z`,

\[
 \sum_{T\in G}d(Y,Z,T)
 \le\min\left\{n d(Y,Z),\sum_{T\in G}d(Y,T)\right\}.          \tag{15.12}
\]

If `Y in F cap G`, summing (15.12) over `Z in F-Y` is `O(D)`.
If `Y in F-G`, it is `O(D/m)`.  To verify the latter two assertions,
the other owners `Z` of the packet `F` occur twice at every Johnson
distance `1,...,m` from `Y`, and (1.7) gives

\[
 \sum_{Z\in F-Y}n d(Y,Z)=O(D),
 \qquad
 \sum_{Z\in F-Y}\min\{n d(Y,Z),D/m\}=O(D/m).                  \tag{15.13}
\]

For the second estimate the distances `1` and `m` contribute `O(D/m)`;
the distances `2,...,m-1` contribute less.  Summing over `Y` proves the
first square estimate in (15.10), and the other is symmetric.

We now count (15.2).  Fix roots `F,G` through `X` and a packet
`E in N(F) cap N(G)`.  Choose one of the three tag pairs `P,Q` among
`E,F,G`.  If a pair `B,C` in (15.2) does not contain the new slot `A`,
then (14.9) and (15.8) give

\[
 \sum_{A\in N(P)\cap N(Q)}C(B,C)
 \le C D^2(|P\cap Q|+C)(|B\cap C|+C).                          \tag{15.14}
\]

If the pair is `A,R`, then (14.9), (15.8), and (15.9) give

\[
 \sum_{A\in N(P)\cap N(Q)}C(A,R)
 \le C D^2(|P\cap Q|+C).                                      \tag{15.15}
\]

There are only three tag choices and six packet-pair choices.  Every
factor on the right of (15.14)--(15.15) is one of
`|E cap F|+C`, `|E cap G|+C`, or `s+C`.  The quadratic estimates (15.10)
therefore show that the total contribution for the fixed root pair is at
most

\[
                         C D^3(s+C)^3.                          \tag{15.16}
\]

Finally Theorem 5.2 at `z=2` bounds every fixed polynomial moment of
`s-1`; in particular,

\[
 {1\over D^2}\sum_{F,G\ni X}(s+C)^3=O(1).                     \tag{15.17}
\]

Summing (15.16) over the `D^2` root pairs proves `V_X=O(D^5)`.  Also
`U_X=Omega(D^4)`: in the `C(F,G)` tag, the choice `E in
N(F) cap N(G)` gives `sum_(F,G) C(F,G)^2`, and every root pair has the
`D` packets through `X` as common conflict neighbors.  Hence (15.6)
follows. \(\square\)

Thus the hierarchy is rigorously normalized through `V_X` at time zero.
Its hereditary propagation remains open: monotonicity alone does not
preserve the normalization as the current degree `d` decreases.

## 16. Exact-factor pair spread is the correct integration target

The longitudinal target must retain row-pair spread, not merely cover
almost all middle owners.  The exact counting statement is short.

Let `mathfrak F` be a coordinate-invariant distribution on exact wreath
factors.  Since every factor contains `B=W/n` of the `M=BD` packets,
coordinate transitivity gives, for every packet `E`,

\[
                         \boxed{\Pr(E\in\mathfrak F)=1/D.}      \tag{16.1}
\]

For depth `q`, let `I_q(E)` be the `n` depth-`q` targets of packet `E`.
Suppose that

\[
 \Pr(E,E'\in\mathfrak F)\le {K_A\over D^2}                    \tag{16.2}
\]

whenever `E ne E'` share a depth-`q` target, uniformly for
`q<=A sqrt(m)`.  Then

\[
 \begin{aligned}
 \mathbb E P_q(\mathfrak F)
 &=\sum_{E<E'}|I_q(E)\cap I_q(E')|
                  \Pr(E,E'\in\mathfrak F)\\
 &\le {K_A\over D^2}N_q\binom{\lambda_qD}{2}
 \le {K_A\lambda_q W\over2}.                                  \tag{16.3}
 \end{aligned}
\]

Here every fixed target belongs to exactly `lambda_qD` catalogue
packets.  Since an exact factor has total depth mass `W`, its centered
energy is

\[
 E_q=2P_q-(\lambda_q-1)W.
\]

Consequently

\[
 \boxed{
 \mathbb E E_q
 \le K_A\lambda_qW-(\lambda_q-1)W=O_A(W).}                    \tag{16.4}
\]

Any distribution on exact factors may first be conjugated by an
independent uniform coordinate permutation, which enforces (16.1)
without changing depth or target-sharing relations.  Thus the genuinely
missing part is (16.2), or the weaker aggregate inequality (16.3).

The multi-bite condition (3.3) was designed precisely to propagate this
pair spread for a near matching.  It does **not** supply an exact factor:
an arbitrary packet matching leave need not admit a wreath completion.
Accordingly, a complete longitudinal theorem must include either

1. an exact-factor-valued dynamics with (16.2), or
2. an extendibility theorem which completes the spread near matching
   while adding only an `o(W)` aggregate contribution to (16.3).

Coverage alone, even with the moment bounds of Sections 13--15, does not
provide this integration step.
