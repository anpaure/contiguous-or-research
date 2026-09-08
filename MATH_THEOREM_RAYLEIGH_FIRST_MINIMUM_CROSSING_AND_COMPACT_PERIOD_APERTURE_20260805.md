# Rayleigh clocks: first-minimum normalization and a compact period aperture

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional all-clock reduction and exact no-go.  Every negative
superadditive-clock certificate can be replaced by a finite Bellman clock
whose first crossing is the unique global minimum of the Rayleigh kernel,
whose saturated crossing value lies in a fixed compact interval, and whose
complete infinite tail is bounded below by one finite periodized residue
functional.  That crude residue functional is explicitly negative on an
infinite family of valid first-crossing prefixes.  A proof must therefore
retain the shorter maximum-density Apéry tail and its finite shoulder.

## 0. Setup

Put

\[
 A={\sqrt\pi\over2}
\]

and

\[
 K(x)=
 \begin{cases}
  1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
  -e^{-(A+x)^2},&x>A.
 \end{cases}                                      \tag{0.1}
\]

Let `zeta` be the unique global minimum of `K`.  Thus

\[
 0<\zeta<A,
 \qquad K\text{ is strictly decreasing on }[0,\zeta],
 \qquad K\text{ is strictly increasing on }[\zeta,\infty).
                                                        \tag{0.2}
\]

Let (with `K(infinity)=0`)

\[
 0=a_0\le a_1\le a_2\le\cdots,
 \qquad a_{i+j}\ge a_i+a_j                       \tag{0.3}
\]

be a nondecreasing superadditive counting clock with values in
`[0,infinity]`.  Repeated positions are
allowed.  Its Rayleigh functional is

\[
 \Phi(a)=\sum_{m\ge0}K(a_m).                      \tag{0.4}
\]

Once one finite positive clock value occurs, (0.3) makes the finite part
unbounded unless the clock reaches the cemetery value `infinity`; in both
cases the Gaussian tail makes (0.4) absolutely convergent after a finite head.
The identically-zero clock has value `+infinity` and is irrelevant to a
negative certificate.

## 1. Cut at the first visit to the global minimum

Assume the clock is not identically zero and define

\[
 N=\min\{m\ge1:a_m\ge\zeta\}.                    \tag{1.1}
\]

Use the finite prefix as denominations.  Namely, let

\[
 V_0=0,
 \qquad
 V_m=\max\left\{
       \sum_{j=1}^s a_{i_j}:
       s\ge0,\ 1\le i_j\le N,\ \sum_j i_j=m
             \right\}.                            \tag{1.2}
\]

### Theorem 1.1 (first-minimum Bellman reduction)

One has

\[
 V_m=a_m\quad(0\le m\le N),                      \tag{1.3}
\]

and

\[
 \zeta\le V_m\le a_m\quad(m\ge N).              \tag{1.4}
\]

Consequently

\[
 \boxed{\Phi(V)\le\Phi(a).}                      \tag{1.5}
\]

In particular, every negative superadditive clock has a negative finite
Bellman minorant whose endpoint is its first crossing of the **global
minimum** `zeta`, rather than merely its first crossing of the support
threshold `A`.

#### Proof

For `m<=N`, the one-part representation in (1.2) gives `V_m>=a_m`.
Conversely, repeated use of (0.3) bounds every partition value by `a_m`,
which proves (1.3).

Every representation used in (1.2) is also bounded by `a_m`, again by
superadditivity, so `V_m<=a_m` for all `m`.  For `m>=N`, use one
size-`N` denomination and any exact fill of `m-N` (zero-valued size-one
fills are allowed if `a_1=0`) to obtain

\[
 V_m\ge a_N+V_{m-N}\ge a_N\ge\zeta.
\]

Thus (1.4) holds.  The two arguments `V_m` and `a_m` lie in the increasing
branch of `K` for every `m>=N`, so

\[
 K(V_m)\le K(a_m).
\]

The terms before `N` agree by (1.3).  Summation proves (1.5). `square`

The proof uses only monotonicity after the true minimum.  It therefore
strictly sharpens the earlier first-`A` deletion: the interval
`[zeta,A)` is also a safe deletion tail.

## 2. Saturation forces a universal overshoot window

Let

\[
 P_N=\max\left\{
       \sum_{j=1}^s a_{i_j}:
       s\ge2,\ 1\le i_j<N,\ \sum_j i_j=N
             \right\},                            \tag{2.1}
\]

with `P_N=0` if no such partition exists, and put

\[
 T=\max\{\zeta,P_N\}.                             \tag{2.2}
\]

Replace the endpoint denomination `a_N` by `T`, retain
`a_1,...,a_(N-1)`, and call the new Bellman clock `W`.

### Theorem 2.1 (minimum-crossing saturation)

The saturated table is internally superadditive and

\[
 W_m=V_m=a_m\quad(m<N),                           \tag{2.3}
\]

\[
 \zeta\le W_m\le V_m\quad(m\ge N).              \tag{2.4}
\]

Moreover the endpoint obeys the **dimension-free strict aperture**

\[
 \boxed{\zeta\le T<2\zeta,}                     \tag{2.5}
\]

and

\[
 \boxed{\Phi(W)\le\Phi(V)\le\Phi(a).}           \tag{2.6}
\]

If `P_N>=zeta`, the endpoint denomination is Bellman-inert; if
`P_N<zeta`, the endpoint is exactly `zeta`.

#### Proof

Every lower-index partition of `N` has value at most `P_N`, so (2.2)
preserves all internal superadditivity inequalities ending at `N`.
All earlier inequalities are unchanged.  Since `a_N>=zeta` and
`a_N>=P_N`, one has `T<=a_N`.  Lowering one denomination can only lower
the Bellman clock, while capacities below `N` cannot use it.  This proves
the equality in (2.3) and the upper inequality in (2.4).  The lower
inequality follows by using one endpoint denomination.

It remains to prove the strict upper bound in (2.5).  Take any partition
of `N` into at least two proper positive parts and separate one part of
capacity `j` from all the others.  Its value is at most

\[
 a_j+V_{N-j}=a_j+a_{N-j}.
\]

Both indices are strictly below `N`; by the definition of the first
crossing, both displayed values are strictly below `zeta`.  Hence every
proper partition has value strictly below `2zeta`, and therefore
`P_N<2zeta`.  Equation (2.5) follows.

For `m>=N`, both clocks in (2.4) lie on the increasing branch of `K`, so
`K(W_m)<=K(V_m)`; before `N` they agree.  This gives (2.6).

Finally, when `P_N>=zeta`, an attaining lower-index partition replaces
every endpoint occurrence without lowering its value, so the endpoint is
inert.  The other case is immediate from (2.2). `square`

## 3. The complete infinite tail collapses to one compact period

For `T>=zeta` define the periodized Rayleigh kernel

\[
 F_T(x)=\sum_{q=0}^{\infty}K(qT+x),
 \qquad 0\le x<T.                                \tag{3.1}
\]

The series is absolutely convergent: all terms after the first lie on the
Gaussian increasing tail and decay quadratically exponentially.

### Theorem 3.1 (compact period aperture)

The saturated clock of Theorem 2.1 satisfies

\[
 \boxed{
 \Phi(W)\ge
 \mathcal A_N(a_1,\ldots,a_{N-1};T)
 :=\sum_{r=0}^{N-1}F_T(a_r).
 }                                                  \tag{3.2}
\]

Its finite data obey

\[
 0=a_0\le a_1\le\cdots\le a_{N-1}<\zeta,        \tag{3.3}
\]

\[
 a_{i+j}\ge a_i+a_j\quad(i+j<N),                \tag{3.4}
\]

\[
 a_i+a_{N-i}\le T\quad(1\le i<N),               \tag{3.5}
\]

and `T=max(zeta,P_N) in [zeta,2zeta)`.

Consequently:

> **Finite minimum-crossing aperture.**  If
> \[
>   \sum_{r=0}^{N-1}F_T(a_r)\ge0                 \tag{3.6}
> \]
> for every finite system (3.3)--(3.5) with the saturated endpoint rule,
> then
> \[
>   \sum_{m\ge0}K(a_m)\ge0
> \]
> for every nondecreasing superadditive clock.

Conversely, every negative clock produces finite saturated data satisfying
(3.3)--(3.5) for which the compact aperture in (3.6) is negative.

#### Proof

Superadditivity of the Bellman clock and `W_N=T` give

\[
 W_{qN+r}\ge qT+W_r=qT+a_r
 \qquad(q\ge0,\ 0\le r<N).                       \tag{3.7}
\]

For `q>=1`, both sides of (3.7) are at least `T>=zeta`; monotonicity of
`K` on `[zeta,infinity)` gives

\[
 K(W_{qN+r})\ge K(qT+a_r).                       \tag{3.8}
\]

At `q=0` equality holds.  Sum (3.8) over all residues and quotients to
obtain (3.2).

Conditions (3.3)--(3.4) are inherited from the first-crossing prefix.
Condition (3.5) is the internal superadditivity inequality ending at `N`
after endpoint saturation.  Theorems 1.1 and 2.1 prove all remaining
claims.

If (3.6) holds universally, then (3.2), (2.6), and (1.5) rule out a
negative clock.  Conversely, if the original clock is negative, the two
normalizations remain negative.  Equation (3.2) then implies

\[
 \mathcal A_N\le\Phi(W)<0,
\]

which is the asserted finite negative aperture. `square`

## 4. Why this is sharper, and why it is not yet the proof

The previous carry-aware reduction normalized at the physical socket
endpoint `A`.  The present theorem uses the only monotonicity actually
needed: monotonicity of `K` after its global minimum.  It therefore gains
three exact facts simultaneously:

1. the first crossing occurs at `zeta`, not `A`;
2. saturation confines its overshoot to the fixed compact interval
   `[zeta,2zeta)`; and
3. every possible infinite tail is replaced by the explicit finite
   functional (3.2).

The remaining inequality (3.6) is strictly finite-dimensional for each
`N`, but `N` is unbounded.  It still retains all carry information through
(3.4), (3.5), and the endpoint saturation rule.  Those rows cannot be
discarded.  For example, a crude period lower envelope can be negative on
a fake half-zero/half-near-`zeta` prefix even though its true Bellman clock
uses the near-`zeta` denomination at a shorter, higher-density period.  The
maximum-density Apéry correction is exactly what the fake prefix omits.

The next section shows that the universal statement `mathcal A_N>=0` is
false.  Thus the all-price problem is not solved, and the exact
maximum-density Apéry tail is mandatory rather than optional.

## 5. Exact no-go for crude first-crossing periodization

Extend (3.1) continuously to `x=T` by

\[
 F_T(T)=\sum_{q\ge1}K(qT).
\]

The authenticated rational Rayleigh bounds give

\[
 K(0)<{9\over100},
 \qquad
 K(\zeta)<-{1\over20}.                            \tag{5.1}
\]

Every `K(qzeta)` with `q>=2` is strictly negative.  Therefore

\[
\begin{aligned}
 F_\zeta(0)+F_\zeta(\zeta)
 &=K(0)+2\sum_{q\ge1}K(q\zeta)\\
 &< {9\over100}-2{1\over20}<0.                   \tag{5.2}
\end{aligned}
\]

By continuity, choose `epsilon>0` so small that

\[
 F_\zeta(0)+F_\zeta(\zeta-\epsilon)<0.           \tag{5.3}
\]

For an integer `M>=1`, put `N=2M+1` and define

\[
 a_i=
 \begin{cases}
  0,&0\le i\le M,\\
  \zeta-\epsilon,&M+1\le i<N,\\
  \zeta,&i=N.
 \end{cases}                                      \tag{5.4}
\]

### Theorem 5.1 (half-step aperture no-go)

The table (5.4) is nondecreasing and internally superadditive, `N` is its
first `zeta` crossing, and its saturated endpoint is `T=zeta`.
Nevertheless

\[
 \boxed{
 \mathcal A_N
 =(M+1)F_\zeta(0)+M F_\zeta(\zeta-\epsilon)<0
 }                                                  \tag{5.5}
\]

for every sufficiently large `M`.

#### Proof

If two indices in the positive proper block both exceed `M`, their sum is
at least `2M+2>N`, so no internal inequality sees two positive proper
values.  Every remaining sum has one zero-valued input and is bounded by
monotonicity.  Hence the table is internally superadditive.

No partition of `N` contains two positive proper parts for the same index
reason.  Therefore `P_N=zeta-epsilon<zeta`, and saturation gives
`T=zeta`.

The right side of (5.5) equals

\[
 M\bigl(F_\zeta(0)+F_\zeta(\zeta-\epsilon)\bigr)
 +F_\zeta(0),
\]

which is negative for all sufficiently large `M` by (5.3). `square`

This is not a counterexample to Rayleigh clock positivity.  The proper
denomination of capacity `M+1` and value `zeta-epsilon` has almost twice
the density of the endpoint.  Its repetitions raise the true Bellman tail
far above the crude period-`N` train.  The no-go proves exactly that this
higher-density carry cannot be discarded.

## 6. Corrected scalar frontier: the minimum-threshold Apéry shoulder

For the saturated first-`zeta` table, let

\[
 \lambda=\max_{1\le j\le N}{a_j\over j},
 \qquad
 g=\gcd\{j:a_j=j\lambda\},                       \tag{6.1}
\]

where in this section the endpoint symbol is reset to `a_N=T`,

and let `U` be its formal maximum-density Apéry clock.  The exact residue
theorem gives

\[
 W_m\le U_m\quad(m\ge0),
 \qquad
 W_m=U_m\quad(m\ge N(N-1)).                      \tag{6.2}
\]

Consequently

\[
 \boxed{
 \Phi(W)=\Phi(U)+
 \sum_{m=0}^{N(N-1)-1}\bigl(K(W_m)-K(U_m)\bigr)
 }                                                  \tag{6.3}
\]

is an identity.  Since `K` decreases before `zeta`, every summand with
`U_m<=zeta` is nonnegative.  The only adverse terms lie in

\[
 \mathcal D_\zeta=
 \{m<N(N-1):U_m>\zeta\}.                          \tag{6.4}
\]

Combining Theorems 1.1--2.1 with (6.3) gives the proof-safe remaining
statement:

> **Minimum-threshold Apéry-shoulder lemma.**  For every saturated
> first-`zeta` table with endpoint `T in [zeta,2zeta)`, its formal Apéry
> functional plus the exact finite shoulder in (6.3) is nonnegative.

This lemma is equivalent to excluding all finite Bellman counterclocks
after the unconditional normalization above.  It is strictly sharper than
the former first-`A` trichotomy because both the crossing threshold and the
endpoint overshoot are confined by the actual one-well geometry of `K`.
It is not proved here.

## 7. Relation to the binomial configuration gate

The authoritative configuration dual closes the physical prices to the
full cone of nonnegative nondecreasing subadditive covering prices.
Single-clock quantization is pairing-dense in that cone.  Hence there is no
smaller `binomial-only` price class available without adding a new physical
reserve hypothesis.  The half-step no-go shows that even crude endpoint
periodization is too weak.  The proof-safe target is the exact
minimum-threshold Apéry shoulder (6.3).

## 8. No uniform dual margin is available

Even a successful proof of nonnegativity cannot pay for a rounding bank by
a dimension-free normalized dual gap.  For `h>0`, put

\[
 \rho_h=h\sum_{n\ge0}\delta_{nh}.                 \tag{8.1}
\]

This is an anchored-window measure (a scaled arithmetic clock), and

\[
 1\le \rho_h([0,1])\le1+h.                       \tag{8.2}
\]

Since `K` is continuous and integrable,

\[
 \int K\,d\rho_h
 =h\sum_{n\ge0}K(nh)
 \longrightarrow\int_0^\infty K(x)dx=0          \tag{8.3}
\]

by ordinary Riemann-sum convergence.  Hence

\[
 \boxed{
 \inf_{\rho\ne0}
 {\int K\,d\rho\over\rho([0,1])}=0
 }                                                  \tag{8.4}
\]

if universal positivity holds (and in any event the infimum is at most
zero).  Thus a polynomial exceptional bank must be reserved by a separate
finite-size or adjacent-depth argument; it cannot be extracted from a
uniform positive continuum price margin.

This does **not** mean that the arithmetic comb face lacks enough
finite-size margin.  Since `K'` is absolutely continuous by pieces and
`K''` is integrable (with only a finite matching-point jump), the
trapezoidal Euler--Maclaurin estimate gives

\[
 h\left({K(0)\over2}+\sum_{n\ge1}K(nh)\right)
 =\int_0^\infty K(x)dx+O(h^2)=O(h^2).             \tag{8.5}
\]

Therefore

\[
 \boxed{
 h\sum_{n\ge0}K(nh)={K(0)\over2}h+O(h^2).
 }                                                  \tag{8.6}
\]

At the reciprocal meshes `h=A/q` one has the sharper exact identity

\[
 \sum_{n\ge0}K(nA/q)
 ={1\over2}-e^{-\pi/4}
 -2q\sum_{m\ge1}e^{-4\pi q^2m^2}>0.              \tag{8.7}
\]

Thus a mesh `h asymp k^(-1/2)` has normalized positive margin
`Theta(k^(-1/2))`.  After multiplying by the Boolean scale `W`, this is
`Theta(W/sqrt(k))`, which dominates every polynomial in `k`.  Exact combs
therefore have ample room for a polynomial root-lattice bank.  What (8.4)
rules out is only a **dimension-free** normalized margin; a proof for
general nonarithmetic clocks must still quantify how close they can come
to the zero-work Lebesgue limit.

## 9. Dependencies

1. `MATH_THEOREM_SUBADDITIVE_PRICE_MEASURE_AND_SUPERADDITIVE_CLOCK_REDUCTION_20260804.md`;
2. `MATH_THEOREM_ANCHORED_WINDOW_ATOMIC_BLOCK_CLOCK_DENSITY_AND_EXTREME_RAYS_20260805.md`;
3. `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` (for comparison only; not used in the proof);
4. `MATH_THEOREM_ALL_GRID_MINIMAL_COUNTEREXAMPLE_APERY_DESCENT_TRICHOTOMY_20260804.md` (for the surviving Apéry-tail interpretation).
