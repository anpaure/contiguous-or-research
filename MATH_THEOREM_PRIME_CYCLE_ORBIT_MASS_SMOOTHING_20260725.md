# Prime-cycle orbit-mass smoothing

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The involution bridge can remove a hole only when its two-element target
orbit contains a duplicate.  A coordinate cycle of prime order has much
longer target orbits and therefore a more favorable relaxed mass ledger.

For an arbitrary finite-order permutation, every diagonal row replacement
preserves total load on each target orbit.  The unavoidable number of holes
on an orbit `O` of total load `t_O` is

\[
                         (|O|-t_O)_+.
\]

In the occurrence-token relaxation this floor is attainable after repeated
one-step transfers around the orbit.

Now let the dimension `n=2m+1` be prime and average over coordinate
`n`-cycles.  Every nontrivial rank target orbit has length `n`.  If

\[
 f_q=\mu_q-{W\over N_q}\mathbf1,
\]

then exact cyclic point margins put `f_q` in Johnson degrees at least two.
The average squared norm of its orbit projection is exactly

\[
 {1\over n}\|f_q\|_2^2.
\]

The relevant hypothesis `||f_q||_2^2=O(W)` is exactly the ordinary
Poisson/random variance scale at every bounded Gaussian depth.  This is
the central advantage of the prime-cycle layer: it asks the seed factor
to match random second moments, not to suppress holes beyond random.

Consequently some coordinate `n`-cycle has orbit-mass hole floor at most

\[
 \boxed{
 \mathfrak D_{\sigma,q}
 \le \sqrt{{N_q\over n}}\,\|f_q\|_2.}
\]

Thus ordinary `O(W)` quadratic load energy at one fixed depth already
makes the relaxed orbit floor `o(W)`.  The remaining difficulty is to lift
the token transports to exact/cancelling row operations simultaneously
over a growing band.  The theorem nevertheless identifies a genuine
advantage of long cycles over involutions: duplicate mass can be routed
collectively around length-`n` target orbits rather than being trapped in
two-cycles.

## 1. General orbit-mass conservation

Let `sigma` be any finite-order coordinate permutation and fix one rank.
For an exact factor `F`, write `mu(S)` for its target load.  If
`A subseteq F`, let `a_A(S)` count the occurrences of `S` belonging to rows
of `A`.  The diagonal replacement

\[
                   F_A=(F\setminus A)\sqcup\sigma A
\tag{1.1}
\]

has load

\[
 \boxed{
 \mu_A(S)=\mu(S)-a_A(S)+a_A(\sigma^{-1}S).}
\tag{1.2}
\]

Summing (1.2) around a target orbit `O` gives

\[
 \boxed{
 \sum_{S\in O}\mu_A(S)=\sum_{S\in O}\mu(S).}
\tag{1.3}
\]

The same identity persists under every sequence of diagonal replacements
using the same coordinate permutation.

### Theorem 1.1 (general orbit floor)

Put

\[
                         t_O=\sum_{S\in O}\mu(S).
\]

Every load vector reachable by such replacements has at least

\[
 \boxed{
 \mathfrak D_\sigma(\mu)
 =\sum_{O}(|O|-t_O)_+}
\tag{1.4}
\]

holes.

In the relaxation in which occurrence tokens may be moved independently
one step along their target orbit, (1.4) is the exact minimum after
sufficiently many rounds.

#### Proof

On an orbit of size `ell`, every positive integer load consumes at least
one of the `t_O` tokens.  Hence at most `min(ell,t_O)` coordinates can be
positive, proving the lower bound `max(0,ell-t_O)`.

For relaxed attainability, choose `min(ell,t_O)` desired target positions,
put one token at each, and put all remaining tokens arbitrarily.  On a
directed cycle every token can be routed from its initial position to its
assigned target by successive forward steps.  Moving the tokens one at a
time realizes this routing.  Summing over target orbits proves the claim.
\(\square\)

This attainability statement deliberately ignores row bundling: one wreath
row moves all its rank occurrences together.  It is a sharp load-level
benchmark, not an exact-factor construction.

## 2. Prime coordinate cycles

Assume now that `n` is prime and `sigma` is an `n`-cycle on coordinates.
For every rank `1<=r<=n-1`, no `r`-set is fixed by a nontrivial power of
`sigma`: an invariant set would be a union of coordinate orbits, and the
coordinate action has only one orbit.  Hence every target orbit has length
exactly `n`.

Let `P_tau` denote the permutation action of a coordinate permutation
`tau` on target functions, and let

\[
 \Pi_\sigma={1\over n}\sum_{t=0}^{n-1}P_{\sigma^t}
\tag{2.1}
\]

be the orthogonal projection onto functions constant on these target
orbits.  Put

\[
 \lambda_q={W\over N_q},\qquad
 f_q=\mu_q-\lambda_q\mathbf1.
\tag{2.2}
\]

The orbit containing `S` has total load `n(Pi_sigma mu_q)(S)`.  Therefore
the floor (1.4) can be written exactly as

\[
 \boxed{
 \mathfrak D_{\sigma,q}
 =\sum_S\bigl(1-(\Pi_\sigma\mu_q)(S)\bigr)_+.}
\tag{2.3}
\]

Since `lambda_q>=1`,

\[
 \mathfrak D_{\sigma,q}
 \le\|\Pi_\sigma f_q\|_1
 \le\sqrt{N_q}\,\|\Pi_\sigma f_q\|_2.
\tag{2.4}
\]

## 3. Exact class-average projection identity

Every wreath load has constant point marginals:

\[
 \sum_{S\ni x}\mu_q(S)=(m-q){W\over n}
\tag{3.1}
\]

for every coordinate `x`.  Centering by the uniform load gives

\[
                         f_q\in U_2\oplus U_3\oplus\cdots
\tag{3.2}
\]

in the Johnson decomposition.

The conjugacy-class average of coordinate `n`-cycles acts as zero on all
`U_j`, `j>=2`.  For prime `n`, every nonidentity power of a uniform
`n`-cycle is again uniformly distributed over the same conjugacy class.
Using that `Pi_sigma` is an orthogonal projection,

\[
\begin{aligned}
 \mathbb E_\sigma\|\Pi_\sigma f_q\|_2^2
 &=\mathbb E_\sigma\langle f_q,\Pi_\sigma f_q\rangle\\
 &={1\over n}\|f_q\|_2^2
   +{1\over n}\sum_{t=1}^{n-1}
      \mathbb E_\sigma\langle f_q,P_{\sigma^t}f_q\rangle\\
 &=\boxed{{1\over n}\|f_q\|_2^2.}
\end{aligned}
\tag{3.3}
\]

### Theorem 3.1 (prime-cycle smoothing)

For every exact factor and every depth `q`, some coordinate `n`-cycle
satisfies

\[
 \boxed{
 \mathfrak D_{\sigma,q}
 \le\sqrt{{N_q\over n}}\,\|f_q\|_2.}
\tag{3.4}
\]

More generally, for nonnegative weights `b_q`, one common `n`-cycle
satisfies

\[
 \boxed{
 \sum_q b_q\|\Pi_\sigma f_q\|_2^2
 \le {1\over n}\sum_qb_q\|f_q\|_2^2.}
\tag{3.5}
\]

#### Proof

Equation (3.3) and averaging give a cycle with the asserted squared-norm
bound.  Combine with (2.4) to get (3.4).  Summing (3.3) before choosing the
cycle proves (3.5). \(\square\)

### Representation-theoretic audit of the vanishing assertion

The permutation module on `r=m-q` subsets is multiplicity free:

\[
 \mathbb C\binom{[n]}r
 \cong\bigoplus_{j=0}^{r}S^{(n-j,j)}.                            \tag{3.6}
\]

Let `K_n` be the normalized class sum of all coordinate `n`-cycles.  By
Schur's lemma its scalar on `S^(n-j,j)` is

\[
 {\chi^{(n-j,j)}((n))\over\dim S^{(n-j,j)}}.                    \tag{3.7}
\]

Murnaghan--Nakayama says that the character of an `n`-cycle vanishes
unless the indexing partition is a hook.  Among the two-row partitions
`(n-j,j)`, this happens only for `j=0,1`; the corresponding character
values are `1,-1`.  Hence

\[
 \boxed{K_n=\Pi_0-{1\over n-1}\Pi_1.}                          \tag{3.8}
\]

It remains to justify that the centered wreath load has no degree-one
part.  Every cyclic order has exactly `r` cyclic `r`-intervals containing
any fixed coordinate `x`.  Therefore an exact factor of `T=W/n` rows
satisfies

\[
 \sum_{S\ni x}\mu_q(S)=rT={rW\over n}
 =\lambda_q\binom{n-1}{r-1}                                   \tag{3.9}
\]

for every `x`.  Thus all point-degree deviations of `f_q` vanish.  The
standard incidence realization of `U_1` gives `Pi_1 f_q=0`; also
`Pi_0 f_q=0` by total mass.  Equations (3.8)--(3.9) prove the vanishing
used in (3.3).

Equivalently, if target necklaces under `sigma` have masses `M_sigma(O)`,
then

\[
 \mathcal E_{\sigma,q}
 :=\sum_O(M_\sigma(O)-n\lambda_q)^2
 =\sum_{d\in\mathbb Z_n}\langle f_q,P_{\sigma^d}f_q\rangle.    \tag{3.10}
\]

For `d ne 0`, a nonzero power of a uniformly random prime `n`-cycle is
again uniform on the same conjugacy class.  Combining (3.8)--(3.10)
therefore gives the exact orbit-energy identity

\[
 \boxed{\mathbb E_\sigma\mathcal E_{\sigma,q}=\|f_q\|_2^2.}   \tag{3.11}
\]

This is the row-free form of (3.3).  Exceptional affine rows with
repeated target-necklace colors do not create a missing diagonal term:
their contribution is already included in the complete autocorrelation
(3.10).

### Theorem 3.2 (almost every row is necklace-transversal)

Fix any exact factor `F`.  There is a prime coordinate cycle `sigma` for
which all but at most `n(n-1)/2` rows of `F` have their `n` middle windows
in `n` distinct middle `sigma`-necklaces.

More exactly, if

\[
 a_{C,\sigma}(O)=
 \#\{X\in\mathcal W_m(C):X\in O\},
 \qquad
 I_\sigma(C)=\sum_O\binom{a_{C,\sigma}(O)}2,                   \tag{3.12}
\]

then

\[
 \boxed{
 \mathbb E_\sigma I_\sigma(C)
 ={n^2(n-1)\over2W},
 \qquad
 \mathbb E_\sigma\sum_{C\in F}I_\sigma(C)
 ={n(n-1)\over2}.}                                            \tag{3.13}
\]

#### Proof

Let `g_C` be the indicator of the `n` middle sets in row `C`.  Its total
mass is `n`, and every coordinate belongs to exactly `m` of those middle
sets.  Thus its centered vector

\[
                         g_C-{n\over W}\mathbf1
\]

has zero constant and degree-one Johnson components, exactly as in
(3.9).  Apply the orbit-energy identity (3.11) with total mean `n/W`.
There are `W/n` target necklaces, their masses are `a_(C,sigma)(O)`, and
their average mass is `n^2/W`.  Therefore

\[
 \begin{aligned}
 \mathbb E_\sigma
 \sum_O\left(a_{C,\sigma}(O)-{n^2\over W}\right)^2
 &=\left\|g_C-{n\over W}\mathbf1\right\|_2^2\\
 &=n-{n^2\over W}.
 \end{aligned}                                                 \tag{3.14}
\]

Expanding the left side yields

\[
 \mathbb E_\sigma\sum_Oa_{C,\sigma}(O)^2
 =n+{n^2(n-1)\over W}.
\]

Since `sum_O a_(C,sigma)(O)=n`, subtracting `n` and dividing by two proves
the first identity in (3.13).  The factor has `W/n` rows, so summing proves
the second.  Some cycle attains at most the expectation.  Every
nontransversal row contributes at least one to `I_sigma(C)`, completing
the proof. \(\square\)

Deleting the exceptional rows leaves at most `O(n^3)=o(W)` uncovered
middle sets.  Thus, at negligible middle cost, the row--necklace incidence
graph used by the phase lift may be assumed simple on its row side: every
surviving row meets `n` distinct middle necklaces once each.  This does
not solve the simultaneous complete-mapping constraints, but removes all
large row signatures from the main asymptotic gate.

This deletion produces a partial middle packing, not a smaller exact
factor: necklaces incident with a deleted row retain missing phases, and
one must impose noncollision rather than a full permutation constraint on
the surviving rows.  Closing under whole quotient components could enlarge
the leave drastically.  Thus transversality removes multiplicities but
does not by itself legalize independent row shifts.

By averaging a normalized sum of the nonnegative functional in (3.13)
and the multidepth orbit-energy functional, the same coordinate cycle can
be chosen both almost row-transversal and within a constant factor of all
the smoothing bounds used below.

### Corollary 3.3 (simultaneous multidepth transversality)

Fix `A<infinity` and `H=ceil(A sqrt(m))`.  One prime coordinate cycle has
at most

\[
 \boxed{
 {n(n-1)\over2}\sum_{q=0}^{H}\lambda_q
 =O_A(n^{5/2})}                                                 \tag{3.15}
\]

total pairs of equal target-necklace colors occurring inside individual
rows, summed over every depth `0<=q<=H`.  Consequently, after deleting
`O_A(n^(5/2))` rows, every remaining row has its `n` depth-`q` intervals
in `n` distinct target necklaces, simultaneously for every `q<=H`.  The
middle leave created by this deletion is `O_A(n^(7/2))=o(W)`.

#### Proof

At depth `q`, one row contains `n` distinct cyclic `(m-q)`-intervals and
every coordinate belongs to exactly `m-q` of them.  Repeat the proof of
Theorem 3.2 with target-space size `N_q` in place of `W`.  For one row,

\[
 \mathbb E_\sigma
 \sum_O\binom{a_{C,q,\sigma}(O)}2
 ={n^2(n-1)\over2N_q}.                                        \tag{3.16}
\]

There are `W/n` rows, so the expected total at depth `q` is

\[
 {W\over n}{n^2(n-1)\over2N_q}
 ={n(n-1)\over2}\lambda_q.                                   \tag{3.17}
\]

For `q<=A sqrt(m)`, the product formula gives
`lambda_q<=exp(A^2+o_A(1))`.  Sum (3.17) over `H+1=O_A(sqrt n)` depths and
choose a cycle attaining the expectation.  Every row which fails
transversality at any depth contributes at least one collision pair to
this total, proving (3.15) and the deletion claim. \(\square\)

Thus repeated row signatures are not the asymptotic lift obstruction.
On the surviving core, every row contributes at most one phase to any
fixed target necklace at every relevant depth.  The remaining problem is
the global compatibility of the row-phase variables across the many
middle exact-permutation and lower near-surjectivity constraints.

### Corollary 3.4 (abundant all-depth rainbow bundles)

If a row `C` is necklace-transversal at depth zero, then its full translate
orbit

\[
                         \{C,\sigma C,\ldots,\sigma^{n-1}C\}    \tag{3.18}
\]

is a middle packing of `n` rows.  If `C` is also transversal at depth
`q`, this bundle covers every phase of each depth-`q` necklace it touches,
with load exactly one.  Hence every row retained by Corollary 3.3 is a
simultaneously middle-disjoint, all-audited-depth rainbow bundle.

#### Proof

An intersection between `sigma^a C` and `sigma^b C` at the middle rank
would give two middle windows of `C` in one necklace, contradicting
depth-zero transversality.  At depth `q`, translating the row cycles the
phase of each of its `n` distinct necklace colors through all `n` values,
proving the rainbow assertion. \(\square\)

This proves existence of the desired local bundles in abundance.  It does
not select them globally.  The candidate bundles are the row-neighborhood
hyperedges in the `n`-regular row--middle-necklace incidence graph; one
still needs a matching of about `W/n^2` disjoint neighborhoods.  The
translation-quotient codegree theorem shows that the worst relative
pair codegree of the full catalogue remains `Theta(1/m)`, so this bundle
selection is a genuine growing-uniformity matching gate rather than a
free consequence of transversality.

## 4. Collision-energy corollary

Write `lambda_q=c_q+alpha_q`, `0<=alpha_q<1`, and let `Phi_q` be the
balanced pair-collision excess.  The exact Euclidean identity is

\[
 \|f_q\|_2^2
 =2\Phi_q+N_q\alpha_q(1-\alpha_q).
\tag{4.1}
\]

Consequently, at every fixed depth for which

\[
                         \Phi_q=O(W),
\tag{4.2}
\]

Theorem 3.1 gives

\[
                         \mathfrak D_{\sigma,q}=O(W/\sqrt n)=o(W).
\tag{4.3}
\]

This is substantially weaker than asking the original factor itself to
have `o(W)` holes or `o(W)` overload.  It says that ordinary bounded
collision energy is enough to make the *orbit-mass obstruction* vanish at
one depth after choosing a long coordinate cycle.

For a Gaussian window, applying Cauchy--Schwarz to (3.5) gives

\[
 \sum_{q\le H}b_q\mathfrak D_{\sigma,q}
 \le
 \left(\sum_{q\le H}b_qN_q\right)^{1/2}
 \left({1\over n}\sum_{q\le H}b_q\|f_q\|_2^2\right)^{1/2}.
\tag{4.4}
\]

If `H=Theta(sqrt(m))` and the energy is merely `O(W)` at each depth,
the raw Cauchy bound (4.4) is only `O(W)`.  The positive orbit surplus
`n(lambda_q-1)`, which (2.4) discarded, removes this loss.  The next theorem
does exactly that.

### Lemma 4.1 (surplus-sensitive orbit deficit)

For every prime coordinate cycle and every depth with `lambda_q>1`,

\[
 \boxed{
 \mathfrak D_{\sigma,q}
 \le {\|\Pi_\sigma f_q\|_2^2\over4(\lambda_q-1)}.}
\tag{4.5}
\]

#### Proof

For a target orbit `O`, put

\[
 d_O=\sum_{S\in O}\mu_q(S)-n\lambda_q,
 \qquad a_q=n(\lambda_q-1).
\tag{4.6}
\]

Its contribution to the orbit floor is `(-d_O-a_q)_+`.  For every real
`y` and every `a>0`,

\[
                         (y-a)_+\le {y^2\over4a},
\tag{4.7}
\]

because the maximum of `(y-a)/y^2` over `y>=a` is `1/(4a)`, attained at
`y=2a`.  Also

\[
 \sum_Od_O^2=n\|\Pi_\sigma f_q\|_2^2.
\tag{4.8}
\]

Apply (4.7) with `y=-d_O`, sum, and use (4.8):

\[
 \mathfrak D_{\sigma,q}
 \le {n\|\Pi_\sigma f_q\|_2^2
       \over4n(\lambda_q-1)}.
\]

This is (4.5). \(\square\)

### Theorem 4.2 (Poisson-energy band smoothing)

Fix `A<infinity` and put `H=ceil(A sqrt(m))`.  Suppose `n=2m+1` is
prime and one exact middle wreath factor satisfies

\[
 \boxed{
 \|f_q\|_2^2\le C_AW
 \qquad(1\le q\le H)}
\tag{4.9}
\]

for a constant `C_A` independent of `m`.  Then one coordinate `n`-cycle
`sigma` satisfies

\[
 \boxed{
 \sum_{q=1}^{H}\mathfrak D_{\sigma,q}
 =O_A(Wm^{-1/4})=o(W).}
\tag{4.10}

#### Proof

Put `Q=ceil(m^(1/4))` and define

\[
 T_1(\sigma)=\sum_{q\le Q}\|\Pi_\sigma f_q\|_2^2,
\qquad
 T_2(\sigma)=\sum_{Q<q\le H}
 {\|\Pi_\sigma f_q\|_2^2\over\lambda_q-1}.
\tag{4.11}
\]

The exact average identity (3.3) and (4.9) give

\[
 \mathbb ET_1\le {C_AQW\over n}.
\tag{4.12}
\]

Uniformly for `q<=A sqrt(m)`, the elementary product formula for
`lambda_q` gives

\[
 \lambda_q-1
 \ge {q(q+1)\over m+q+1}
 \ge {q^2\over2m}
\tag{4.13}
\]

for all sufficiently large `m`.  Therefore

\[
 \mathbb ET_2
 \le {C_AW\over n}\sum_{q>Q}{2m\over q^2}
 =O_A(W/Q).
\tag{4.14}
\]

Apply averaging to

\[
 {T_1\over\mathbb ET_1}+{T_2\over\mathbb ET_2}
\]

(omitting a zero denominator if necessary).  One common cycle has both
`T_1<=2 E T_1` and `T_2<=2 E T_2`.

For the shallow part, use (2.4) and Cauchy--Schwarz:

\[
\begin{aligned}
 \sum_{q\le Q}\mathfrak D_{\sigma,q}
 &\le
 \left(\sum_{q\le Q}N_q\right)^{1/2}T_1(\sigma)^{1/2}\\
 &\le O_A\left(
 (QW)^{1/2}(QW/n)^{1/2}\right)
 =O_A(QW/\sqrt n).
\end{aligned}
\tag{4.15}
\]

For the remaining depths, Lemma 4.1 gives

\[
 \sum_{Q<q\le H}\mathfrak D_{\sigma,q}
 \le {1\over4}T_2(\sigma)=O_A(W/Q).
\tag{4.16}
\]

With `Q=m^(1/4)` and `n asymp m`, both terms are
`O_A(Wm^(-1/4))`, proving (4.10). \(\square\)

Condition (4.9) is only a bounded-second-moment condition.  A
Poisson-like load profile with bounded mean throughout a fixed Gaussian
window has precisely this scale.  It is far weaker than MWB, which asks
for weighted distance `o(W)` from the balanced integer profiles.  Thus the
prime-cycle orbit transport converts ordinary pseudorandom energy into an
`o(W)` aggregate load-level hole floor.

### Theorem 4.2A (sublinear polynomial energy is sufficient)

Fix `A<infinity` and `0<=beta<1`, suppose `n=2m+1` is prime, and put
`H=ceil(A sqrt(m))`.  Suppose one exact middle wreath factor satisfies

\[
 \boxed{\|f_q\|_2^2\le C_AW(q+1)^\beta
        \qquad(1\le q\le H).}                                  \tag{4.16a}
\]

Then one prime coordinate cycle `sigma` satisfies

\[
 \boxed{\sum_{q=1}^{H}\mathfrak D_{\sigma,q}=o(W).}           \tag{4.16b}
\]

#### Proof

Choose a constant

\[
                         0<a<{1\over\beta+2}
\]

and put `Q=ceil(m^a)`.  Define `T_1,T_2` as in (4.11).  The exact cycle
average now gives

\[
 \mathbb ET_1
 \le {C_AW\over n}\sum_{q\le Q}(q+1)^\beta
 =O_A\left({WQ^{\beta+1}\over n}\right).                     \tag{4.16c}
\]

The shallow Cauchy bound is consequently

\[
 \mathbb E\sum_{q\le Q}\mathfrak D_{\sigma,q}
 \le O_A\left({WQ^{(\beta+2)/2}\over\sqrt n}\right)=o(W),    \tag{4.16d}
\]

by the choice of `a`.  For `q>Q`, use (4.13), Lemma 4.1, and the same
cycle average:

\[
 \begin{aligned}
 \mathbb E\sum_{Q<q\le H}\mathfrak D_{\sigma,q}
 &\le {C_AW\over4n}\sum_{q>Q}{2m(q+1)^\beta\over q^2}\\
 &=O_A(WQ^{\beta-1})=o(W),                                    \tag{4.16e}
 \end{aligned}
\]

because `beta<1`.  Average the normalized shallow and deep functionals,
as in Theorem 4.2, to choose one common cycle attaining both bounds.
\(\square\)

This weakening is relevant to the exact MSW ladder calculation.  A
critical nearest-neighbor counter transfer typically costs a factor of
order `sqrt(q)`, not a bounded factor.  Theorem 4.2A shows that an estimate

\[
                         \|f_q\|_2^2=O_A(W\sqrt{q+1})           \tag{4.16f}
\]

would still suffice.  Thus failure of a strictly subcritical scalar shell
sum does not by itself close the canonical-factor route; only linear or
superlinear growth in `q` is fatal to this particular smoothing argument.

### Theorem 4.2B (the growing MSW seam sectors may be discarded)

In the canonical MSW factor, let `nu_q` be the depth-`q` load obtained by
discarding the `2q` seam occurrences of every row and retaining only the
two intrinsic sectors.  Its total mass is

\[
 T_q=W-2q\operatorname {Cat}_m
    =W\left(1-{2q\over n}\right),\qquad
 \lambda_q'={T_q\over N_q}.                                   \tag{4.16g}
\]

Fix `A<infinity` and `0<=beta<1`.  If

\[
 \boxed{
 \|\nu_q-\lambda_q'\mathbf1\|_2^2
 \le C_AW(q+1)^\beta
 \qquad(1\le q\le A\sqrt m),}                                \tag{4.16h}
\]

then one prime coordinate cycle has aggregate orbit floor `o(W)` for the
**full** MSW depth loads through this window.

#### Proof

The full load dominates `nu_q` coordinatewise, so its orbit floor is no
larger.  Moreover `lambda_q'>=1` throughout the stated window for all
large `m`.  Indeed every factor in

\[
 \lambda_q=\prod_{i=0}^{q-1}{m+2+i\over m-i}
\]

is at least `1+2/m`, while, for `q<=A sqrt(m)`,

\[
 (1+2/m)^q\ge1+2q/m
 \ge {n\over n-2q}.
\]

Thus the ordinary orbit-floor Cauchy bound applies to the centered
intrinsic load.  For the deep part of the split, if `Q=o(sqrt(m))` tends
to infinity, then uniformly for `Q<q<=A sqrt(m)`,

\[
 \lambda_q'-1
 =\lambda_q\left(1-{2q\over n}\right)-1
 \ge c_A{q^2\over m}.                                         \tag{4.16i}
\]

This follows from (4.13), since the removed seam fraction is only
`O(q/m)`.  The prime-cycle class average for an arbitrary centered load is
at most `1/n` times its squared norm; constant point margins are not
needed.  Repeat the shallow/deep proof of Theorem 4.2A with
`nu_q,lambda_q'` and (4.16i).  It gives `o(W)` for the intrinsic orbit
floor, hence also for the full one. \(\square\)

Therefore no growing-`q` estimate for the seam-sector square energy is
needed.  The all-depth canonical problem is purely the coupled
`alpha_q/Gamma_q` ladder problem.

### Theorem 4.3 (a `W/sqrt(m)` middle leave is still admissible)

Fix `A<infinity`.  Let `P` be any middle-disjoint family of wreath rows,
not necessarily an exact factor.  Suppose it contains `R` rows and put

\[
 T=nR=W-L,\qquad 0\le L\le C_0{W\over\sqrt m}.
\tag{4.17}
\]

At every depth its total occurrence mass is `T`.  Put

\[
 \lambda'_q={T\over N_q},\qquad
 f'_q=\mu_q^P-\lambda'_q\mathbf1.
\tag{4.18}
\]

If

\[
 \|f'_q\|_2^2\le C_AW
 \qquad(1\le q\le\lceil A\sqrt m\rceil),
\tag{4.19}
\]

then, in prime dimension, one coordinate `n`-cycle satisfies

\[
 \boxed{
 \sum_{q\le A\sqrt m}
 \mathfrak D_{\sigma,q}(\mu^P)
 =O_{A,C_0,C_A}(Wm^{-1/4})=o(W).}
\tag{4.20}

Here the orbit floor is still computed against one desired occurrence per
target:

\[
 \mathfrak D_{\sigma,q}(\mu^P)
 =\sum_O(n-t_{O,q})_+.
\tag{4.21}
\]

#### Proof

The class-average subgroup projection has eigenvalue zero on `U_1` and
`1/n` on every Johnson degree at least two.  Therefore, without requiring
exact point margins,

\[
 \mathbb E_\sigma\|\Pi_\sigma f'_q\|_2^2
 \le {1\over n}\|f'_q\|_2^2.
\tag{4.22}
\]

Choose a sufficiently large constant `K=K(C_0)` and put
`Q=ceil(Km^(1/4))`.  Through depth `2Q`,

\[
\begin{aligned}
 \mathfrak D_{\sigma,q}
 &\le (N_q-T)_++\|\Pi_\sigma f'_q\|_1\\
 &\le (N_q-T)_++\sqrt{N_q}\|\Pi_\sigma f'_q\|_2.
\end{aligned}
\tag{4.23}
\]

The total deterministic deficit is at most

\[
 \sum_{q\le2Q}(N_q-T)_+
 \le2QL=O(Wm^{-1/4}).
\tag{4.24}
\]

Averaging one common cycle and applying Cauchy--Schwarz exactly as in
(4.15) bounds the projection term over these depths by

\[
                         O(QW/\sqrt n)=O(Wm^{-1/4}).
\tag{4.25}
\]

For `q>2Q`, the central-binomial ratio and the choice of `K` give

\[
 \lambda'_q-1
 ={W-L-N_q\over N_q}
 \ge c_{A,C_0}{q^2\over m}.
\tag{4.26}
\]

The surplus-sensitive proof of Lemma 4.1 applies verbatim with
`lambda'_q`.  Averaging the corresponding weighted projection energy gives

\[
 \sum_{q>2Q}\mathfrak D_{\sigma,q}
 =O\left({W\over Q}\right)=O(Wm^{-1/4}).
\tag{4.27}
\]

As before, normalize and add the shallow and deep projection functionals
before averaging, so the same cycle satisfies both bounds.  Combining
(4.24)--(4.27) proves (4.20). \(\square\)

Theorem 4.3 matches the natural `W/sqrt(m)` physical leave scale of several
near-perfect matching constructions.  It does **not** solve their exact
row phasing: independently shifting the selected rows would generally
create a linear middle defect.  Its force is that neither exact completion
nor hard lower-rank quotas are required before the cyclic transport step.

### Theorem 4.4 (subcubic energy is enough)

Fix `A<infinity`, let `H=ceil(A sqrt(m))`, and suppose first that `F` is an
exact factor in prime dimension.  Let `K=K(m)>=1` satisfy

\[
 \|f_q\|_2^2\le KW\qquad(1\le q\le H).
\tag{4.28}
\]

If `K=o(m^(1/3))`, then one coordinate `n`-cycle satisfies

\[
 \boxed{
 \sum_{q\le H}\mathfrak D_{\sigma,q}
 =O_A\!\left(WK^{3/4}m^{-1/4}\right)=o(W).}
\tag{4.29}
\]

More generally, let `P` be a middle-disjoint row family of mass `W-L`, put
`delta=L/W`, and center its depth loads at `(W-L)/N_q`.  If (4.28) holds
for those centered loads and

\[
 K=m^{o(1)},\qquad \delta\le m^{-1/2+o(1)},
\tag{4.30}
\]

then some coordinate cycle again has aggregate orbit floor `o(W)`.

#### Proof

For the exact case choose

\[
                         Q=\left\lceil(Km)^{1/4}\right\rceil.
\tag{4.31}
\]

The same class average as in (4.12) gives

\[
 \mathbb E\sum_{q\le Q}\|\Pi_\sigma f_q\|_2^2
 \le {QKW\over n}.
\tag{4.32}
\]

Consequently the shallow Cauchy bound is

\[
 O_A\!\left(QW\sqrt{K/n}\right).
\tag{4.33}
\]

For the deep depths, (4.13) and the surplus-sensitive inequality give the
average bound

\[
 O_A\!\left({KW\over Q}\right).
\tag{4.34}
\]

As before, average the normalized sum of the two functionals to select one
common cycle.  With (4.31), both (4.33) and (4.34) equal

\[
 O_A\!\left(WK^{3/4}m^{-1/4}\right).
\]

The hypothesis on `K` makes this `o(W)`.

For a near-factor, choose `Q=m^(1/4+o(1))` sufficiently large that

\[
 Q\ge (Km)^{1/4},\qquad
 Q\ge 2\sqrt{m\delta},
\tag{4.35}
\]

while still `Q=m^(1/4+o(1))`.  Such a choice exists under (4.30).  The
deterministic shallow deficit is at most

\[
                         QL=Q\delta W=o(W).
\tag{4.36}
\]

The shallow projection term is

\[
 O_A\!\left(QW\sqrt{K/m}\right)=o(W),
\tag{4.37}
\]

and (4.35) guarantees positive surplus of order `q^2/m` once `q` is beyond
a fixed constant multiple of `Q`.  The deep term is therefore

\[
 O_A(KW/Q)=o(W).
\tag{4.38}
\]

Combining (4.36)--(4.38) proves the near-factor assertion. \(\square\)

The practical consequence is important.  It is enough to build a
middle-disjoint near-factor with leave `Wm^(-1/2+o(1))` and, throughout
each fixed Gaussian window, either

\[
 \|f_q\|_2^2\le Wm^{o(1)}
\]

or even the pointwise cap `max_S mu_q(S)<=m^{o(1)}`.  The latter implies
the former from `sum_S mu_q(S)<=W`.  Thus the pre-smoothing matching step
does not need floor/ceiling quotas, constant variance, or near-rainbow
shadows; polylogarithmic shadow multiplicity already suffices.

### Theorem 4.5 (nonuniform energy ledger)

For an exact factor in prime dimension, put

\[
                         E_q=\|f_q\|_2^2.
\tag{4.39}
\]

For every `1<=Q<H`, one coordinate `n`-cycle satisfies

\[
 \boxed{
 \sum_{q\le H}\mathfrak D_{\sigma,q}
 \le C\left[
   \left({QW\over n}\sum_{q\le Q}E_q\right)^{1/2}
   +{1\over n}\sum_{Q<q\le H}{E_q\over\lambda_q-1}
             \right],}
\tag{4.40}
\]

where `C` is absolute.  Uniformly for `H<=A sqrt(m)`, the second term may
be replaced by

\[
                         C_A\sum_{q>Q}{E_q\over q^2}.
\tag{4.41}
\]

#### Proof

Let

\[
 A_\sigma=\sum_{q\le Q}\|\Pi_\sigma f_q\|_2^2,
 \qquad
 B_\sigma=\sum_{q>Q}
       {\|\Pi_\sigma f_q\|_2^2\over\lambda_q-1}.
\]

The class average gives

\[
 \mathbb EA_\sigma={1\over n}\sum_{q\le Q}E_q,
 \qquad
 \mathbb EB_\sigma={1\over n}\sum_{q>Q}{E_q\over\lambda_q-1}.
\]

Averaging the two normalized nonnegative functionals selects one cycle for
which each is at most twice its expectation.  Cauchy--Schwarz and (2.4)
give

\[
 \sum_{q\le Q}\mathfrak D_{\sigma,q}
 \le (QW)^{1/2}A_\sigma^{1/2},
\]

while Lemma 4.1 gives the deep contribution at most `B_sigma/4`.  This is
(4.40).  Finally (4.13) and `n asymp m` give (4.41). \(\square\)

The now-proved canonical-MSW first-shadow theorem gives the sharper

\[
                         E_1=O(W).                               \tag{4.42}
\]

The quantity which should remain `O(W)` at deeper ranks is this centered
energy (equivalently balanced pair-collision excess), not the raw pair
count.  Indeed

\[
 E_q=2P_q-(\lambda_q-1)W
    =2\Phi_q+N_q\alpha_q(1-\alpha_q).                           \tag{4.43}
\]

When `lambda_q` grows, the unavoidable baseline in `P_q` itself is of
order `lambda_q W`; a statement `P_q=O(W)` throughout the full band is
therefore false even for perfectly balanced loads.

There is also a sharp reason the prime-cycle step is useful rather than
cosmetic.  If `H_q` is the physical number of zero-load targets, then
Cauchy--Schwarz on the `N_q-H_q` nonzero coordinates gives

\[
 \boxed{
 H_q\le {W E_q\over
              \lambda_q(E_q+\lambda_qW)}.}                    \tag{4.43a}
\]

Indeed `sum mu_q^2>=W^2/(N_q-H_q)` and
`E_q=sum mu_q^2-W^2/N_q`; solving for `H_q` gives (4.43a).  In the
shallow regime `lambda_q=1+o(1)`, the condition `E_q=o(W)` already forces
near-perfection and is essentially the original target.  Generic-scale
energy `E_q=O(W)` gives only `H_q=O(W)`.  Prime-cycle averaging is exactly
what converts this cheaper generic-scale input into an `o(W)` **orbit
floor**; realizing that floor integrally is the price paid in the lift
step.

### Theorem 4.6 (one-cycle aggregate optimization)

For every split point `1<=Q<H`, one prime coordinate cycle satisfies

\[
 \boxed{
 \sum_{q\le H}\mathfrak D_{\sigma,q}
 \le C\left[
     \sum_{q\le Q}\sqrt{{N_qE_q\over n}}
     +\sum_{Q<q\le H}{E_q\over q^2}
           \right],}                                           \tag{4.44}
\]

uniformly for `H=o(m)`.  In particular, if

\[
                         \mathcal K W=\sum_{q\le H}E_q,          \tag{4.45}
\]

then, whenever `Q=(n\mathcal K)^{1/5}` lies in the allowed range, one may
choose `Q` so that

\[
 \boxed{
 \sum_{q\le H}\mathfrak D_{\sigma,q}
 \le C W\mathcal K^{3/5}n^{-2/5}.}                             \tag{4.46}
\]

Thus the coarse aggregate condition
`\mathcal K=o(n^{2/3})` is sufficient.
More finely, if

\[
                         E_q\le Cq^aW                            \tag{4.47}
\]

uniformly through the band for some fixed `a<1`, then the orbit-floor sum
is `o(W)`.

#### Proof

Using orbit energy (3.10), Cauchy--Schwarz on the `N_q/n` target
necklaces gives

\[
 \mathfrak D_{\sigma,q}
 \le\sqrt{{N_q\over n}\,\mathcal E_{\sigma,q}}.                \tag{4.48}
\]

For the deep range, the surplus argument behind Lemma 4.1 gives

\[
 \mathfrak D_{\sigma,q}
 \le {\mathcal E_{\sigma,q}\over4n(\lambda_q-1)}
 \le C{\mathcal E_{\sigma,q}\over q^2},                        \tag{4.49}
\]

where the last inequality uses
`n(lambda_q-1)>=c q^2` for `q=o(m)`.  Take expectations, use the exact
identity `\mathbb E\mathcal E_{\sigma,q}=E_q`, and apply Jensen to
(4.48).
Linearity of expectation then selects one common cycle satisfying (4.44).

Since `N_q<=W`, the shallow part is at most

\[
 W\sqrt{{Q\mathcal K\over n}},
\]

and the coarse deep part is at most `C\mathcal K W/Q^2`.  Balancing these
terms gives `Q\asymp(n\mathcal K)^{1/5}` and (4.46).

For (4.47), instead retain the depth-dependent denominator in (4.44).
Choose any `Q=Q(m)->infinity` with
`Q^{1+a/2}=o(\sqrt n)`.  The shallow sum is

\[
 O\left({W\over\sqrt n}\sum_{q\le Q}q^{a/2}\right)=o(W),
\]

whereas the deep sum is

\[
 O\left(W\sum_{q>Q}q^{a-2}\right)=O(WQ^{a-1})=o(W).
\]

This proves the final assertion. \(\square\)

### Corollary 4.7 (the `n^(1/4)` split)

The uniform constant-energy hypothesis need not be imposed throughout
the whole audited band.  Fix `C<infinity`, put

\[
                         Q_0=\lceil(Cn)^{1/4}\rceil,
\]

and suppose

\[
 E_q\le CW\quad(q\le Q_0),
 \qquad
 \sum_{Q_0<q\le H}{E_q\over q^2}=o(W).                       \tag{4.50}
\]

Then one prime cycle has

\[
                         \sum_{q\le H}\mathfrak D_{\sigma,q}=o(W).
                                                                    \tag{4.51}
\]

Indeed, the first branch of (4.44) is at most

\[
 Q_0W\sqrt{C/n}=O(C^{3/4}n^{-1/4}W)=o(W),
\]

and the second branch is precisely the second condition in (4.50).
If the stronger estimate `E_q<=CW` is available throughout the band,
then

\[
 \sum_{q>Q_0}{E_q\over q^2}
 \le {CW\over Q_0}=O(C^{3/4}n^{-1/4}W),                       \tag{4.52}
\]

so the same conclusion follows.  Thus constant-strength control is
needed only through the `n^(1/4)` crossover **provided** a weighted
deep-energy estimate is supplied separately.  This corollary is an
alternative to, not a replacement for, the fixed-Gaussian-window
diagonal route below.

### Scope of fixed-window diagonalization

There is no unaccounted range between a fixed Gaussian window and
`sqrt(m log m)` in the MWB implication.  The fixed-window theorem is used
diagonally: proving the required estimate for every fixed `A` produces a
sequence `A_m->infinity`, as slowly as necessary, and sets

\[
                         H_m=A_m\sqrt m.                        \tag{4.53}
\]

MWB asks for balancing only through `q<=H_m`.  The ranks beyond `H_m`
are not literalized.  They are handled by the previously proved
product-SCD outer-tail word, whose length is `o(W)` for every

\[
                         H_m/\sqrt m\longrightarrow\infty,
 \qquad                 H_m=o(m).                              \tag{4.54}
\]

The stronger cutoff `H>=sqrt(2m log m)` is needed only if one appends all
outer masks literally.  It is not a requirement of the current transfer
theorem.  Consequently

\[
 \boxed{
 \forall A<\infty\quad
 E_q\le C_AW\ (q\le A\sqrt m)
 }
\tag{4.55}
\]

remains a complete sufficient energy target, with arbitrary deterioration
of `C_A` absorbed into the diagonal choice.  The alternative condition
"constant energy to `m^(1/4)` plus a weighted deep-energy bound" is also
sufficient, but it is not weaker until that additional deep-energy bound
has actually been proved.

The interface is uniform under the later lift and leave operations.  The
product-SCD outer-tail word is an independently appended word depending
only on `(m,H_m)`; it does not inspect the chosen middle factor or any MSW
pointing.  Replacing `F` by a legally lifted exact factor therefore changes
none of its tail estimate.  If rows are deleted, their missing **band**
targets and middle owners must still be charged to the leave ledger, but
the outer-tail word itself is unchanged.  Thus no MSW-specific structure
is silently required after the lift.

The conceptual payoff is nevertheless correct: `E_q=O_A(W)` is the
Poisson/random variance scale.  Prime-cycle smoothing converts this
generic-strength input into an `o(W)` orbit floor, whereas direct coverage
would require a beyond-random zero suppression.

The benchmark can be stated exactly.  If `W` labelled occurrences are
placed independently and uniformly in `N_q` targets, then the multinomial
load vector satisfies

\[
 \mathbb E\sum_S(\mu(S)-\lambda_q)^2
 =\sum_S\operatorname {Var}\mu(S)
 =W\left(1-{1\over N_q}\right).                              \tag{4.56}
\]

Thus order-`W` centered energy is literally the independent-allocation
value at every depth, even when `lambda_q` grows.  This is only a
calibration--independent allocation is not an exact wreath factor--but it
shows that the energy hypothesis asks to match random second moments,
not to suppress holes beyond random scale.

## 5. Reduction to prime dimensions

Proving the coefficient-one theorem along odd prime dimensions is enough
for all dimensions.  Indeed, by the prime number theorem, every large `k`
has an odd prime `p<=k` with `p=(1-o(1))k`.  Repeated trimmed lifts give

\[
                         \nu(k)\le2^{k-p}\nu(p).
\tag{5.1}
\]

The central-binomial asymptotic gives

\[
 {2^{k-p}W(p)\over W(k)}
 =(1+o(1))\sqrt{k\over p}=1+o(1).
\tag{5.2}
\]

Thus `nu(p)<=(1+o(1))W(p)` for odd primes `p` implies the same statement
for arbitrary `k`.  Prime-order orbit smoothing is therefore not merely a
subsequence curiosity.

## 6. Exact remaining lift

The load-level result leaves three integral requirements:

1. find an exact factor satisfying the Poisson-scale bound (4.9) over each
   fixed Gaussian window;
2. lift the relaxed token redistribution around `sigma`-orbits to legal
   wreath-row operations;
3. keep exact middle ownership after each stage or prove cancellation of
   the total middle boundary.

The long-cycle orbit theorem removes the two-cycle duplicate trap at the
relaxed level.  Whether its collective transport can be lifted through the
MSW packet geometry is a new, sharply stated construction problem.

## 7. The exact prime-cycle packet quotient

For a prime coordinate cycle `sigma`, let `mathcal N_m(sigma)` be the set
of its orbits on the middle layer.  Every orbit has size `n`, so

\[
                         |\mathcal N_m(\sigma)|=W/n=B=|F|.
\tag{7.1}
\]

Define the bipartite multigraph `Q_sigma(F)` with left vertex set `F`,
right vertex set `mathcal N_m(sigma)`, and multiplicity

\[
 J_\sigma(C,O)=|\mathcal W_m(C)\cap O|.
\tag{7.2}
\]

Every left and right degree is exactly `n`: a wreath row owns `n` middle
sets, and a middle necklace contains `n` middle sets, each with one owner.
Thus `Q_sigma(F)` is an `n`-regular bipartite multigraph on two parts of
size `B`.

### Theorem 7.1 (cyclic packet-component theorem)

For `A subseteq F`, the following are equivalent:

1. replacing `A` by `sigma A` preserves exact middle ownership;
2. `U(A)=sigma U(A)`, where
   `U(A)=union_(C in A) W_m(C)`;
3. `U(A)` is a union of full middle `sigma`-orbits;
4. `A` is the left shore of a union of connected components of
   `Q_sigma(F)`.

Moreover, if `K` is one connected component with left row family `A_K`,
then for every phase `t in Z_n`,

\[
                         \sigma^tU(A_K)=U(A_K),
\tag{7.3}
\]

so its rows may be replaced by `sigma^t A_K`.  Choosing an independent
phase for every quotient component always produces another exact middle
wreath factor.

#### Proof

The old rows outside `A` cover `Omega_m setminus U(A)` once.  The new rows
cover `sigma U(A)`.  Their union is an exact partition precisely when
`sigma U(A)=U(A)`, proving `1 iff 2`.  A set is invariant under the cyclic
group generated by `sigma` precisely when it is a union of full target
orbits, proving `2 iff 3`.

Because the original row packets partition the middle layer, a necklace
`O` lies wholly in `U(A)` precisely when every row adjacent to `O` in the
quotient graph belongs to `A`; it lies wholly outside precisely when none
does.  Therefore no quotient edge can cross between the selected and
unselected component shores.  This is exactly the assertion that `A` is a
union of connected components, proving `3 iff 4`.

For one connected component, its middle union is a union of necklaces and
hence invariant under every power of `sigma`.  Different components have
disjoint invariant middle unions.  Replacing each component by an
independently chosen phase therefore preserves the partition component by
component. \(\square\)

This is the exact long-cycle analogue of a component-switching cube, with
`n` choices per component instead of two.

### Corollary 7.2 (exact random-phase covariance)

Let the quotient components be `K`, and let `u_(K,q)` be the depth-`q`
load contributed by the old rows of component `K`.  Choose independent
uniform phases `e_K in Z_n`.  The resulting object is an exact factor and

\[
 \mathbb E\mu'_q=\sum_K\Pi_\sigma u_{K,q}=\Pi_\sigma\mu_q,
\tag{7.4}
\]

\[
 \boxed{
 \mathbb E\|\mu'_q-\Pi_\sigma\mu_q\|_2^2
 =\sum_K\left(
   \|u_{K,q}\|_2^2-\|\Pi_\sigma u_{K,q}\|_2^2
   \right).}
\tag{7.5}
\]

#### Proof

Theorem 7.1 gives exactness for every phase vector.  A uniform cyclic shift
of one component load has mean `Pi_sigma u_(K,q)`.  The centered component
contributions are independent and have mean zero, so cross inner products
vanish.  Orthogonal projection gives

\[
 \mathbb E\|\sigma^{e_K}u_{K,q}
             -\Pi_\sigma u_{K,q}\|_2^2
 =\|u_{K,q}\|_2^2-\|\Pi_\sigma u_{K,q}\|_2^2.
\]

Summing proves (7.5). \(\square\)

Random phases need not cover the targets: the variance term in (7.5) can
retain Poisson-scale holes.  The exact row-lift gate has nevertheless been
reduced to a concrete `n`-ary phase choice whenever the quotient graph is
fragmented:

\[
 \boxed{
 \text{choose one phase per component of }Q_\sigma(F)
 \text{ so that the multidepth loads approach their orbit floors}.}
\tag{7.6}
\]

If `Q_sigma(F)` is connected, this component-phase mechanism has only the
`n` global relabellings and produces no balancing.  Thus a positive theorem
must prove either extensive quotient fragmentation or a more general
middle-admissible row-power trade not generated by these components.
