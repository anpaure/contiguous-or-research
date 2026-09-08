# Anchored-window measures: exact atomic blocks, dense superadditive clocks, and extreme rays

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional cone theorem.  It proves that scaled counting
measures of superadditive clocks are pairing-dense in the complete
anchored-window cone, gives an exact atomic criterion, and identifies a
large family of extreme rays.  It does **not** prove Rayleigh positivity on
those rays.

## 0. Setup

Let `C_AW` be the cone of locally finite nonnegative Borel measures `rho`
on `[0,infinity)` satisfying

\[
 \rho((x,x+t])\le \rho([0,t])
 \qquad(x>0,t>0).                                  \tag{0.1}
\]

These are exactly the Stieltjes measures of nonnegative nondecreasing
subadditive prices, with the initial jump represented by an atom at zero.
Endpoint conventions at the positive atoms can be chosen consistently and
do not affect any pairing with the absolutely continuous Rayleigh measures.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A
 \end{cases}                                       \tag{0.2}
\]

be the Rayleigh signed-tail kernel.

## 1. Closed-interval and atomic-block characterizations

### Theorem 1.1 (closed-interval normal form)

A locally finite nonnegative measure belongs to `C_AW` if and only if

\[
 \boxed{
 \rho([u,v])\le \rho([0,v-u])
 \qquad(0<u\le v).
 }                                                   \tag{1.1}
\]

#### Proof

Assume (0.1).  Fix `0<u<=v` and take `0<epsilon<u`.  Applying (0.1) to

\[
 x=u-\epsilon,
 \qquad
 t=v-u+\epsilon
\]

gives

\[
 \rho([u,v])
 \le \rho((u-\epsilon,v])
 \le \rho([0,v-u+\epsilon]).
\]

Let `epsilon` decrease to zero.  Local finiteness and continuity from above
give (1.1).

Conversely, fix `x,t>0`.  For `0<epsilon<t`, equation (1.1) gives

\[
 \rho([x+\epsilon,x+t])
 \le \rho([0,t-\epsilon])
 \le \rho([0,t]).
\]

Let `epsilon` decrease to zero and use continuity from below on the left.
This recovers (0.1). `square`

### Corollary 1.2 (exact locally discrete atomic criterion)

Let

\[
 \rho=\sum_{i\ge0}w_i\delta_{y_i},
 \qquad
 0=y_0<y_1<y_2<\cdots,
 \qquad
 y_i\longrightarrow\infty,
 \qquad
 w_i>0.                                             \tag{1.2}
\]

Then `rho in C_AW` if and only if, for every `1<=p<=q`,

\[
 \boxed{
 \sum_{i=p}^{q}w_i
 \le
 \sum_{i:\ y_i\le y_q-y_p}w_i.
 }                                                   \tag{1.3}
\]

#### Proof

Necessity is (1.1) with `u=y_p` and `v=y_q`.  Conversely, the atoms in any
nonempty interval `[u,v]` form a consecutive block `y_p,...,y_q`.  Since

\[
 y_q-y_p\le v-u,
\]

equation (1.3) bounds the mass of that block by `rho([0,v-u])`.  Theorem
1.1 applies. `square`

The singleton case `p=q` already shows that every positive atom has mass
at most the atom at zero.  In particular, a nonzero purely atomic
anchored-window measure must have positive mass at zero.

## 2. Unit atoms are exactly superadditive clocks

### Theorem 2.1 (counting-clock equivalence)

Let

\[
 0=x_0<x_1<x_2<\cdots,
 \qquad x_n\longrightarrow\infty,                  \tag{2.1}
\]

and put

\[
 \eta_x=\sum_{n\ge0}\delta_{x_n}.                  \tag{2.2}
\]

Then

\[
 \boxed{
 \eta_x\in C_{AW}
 \quad\Longleftrightarrow\quad
 x_{m+n}\ge x_m+x_n\quad(m,n\ge0).
 }                                                   \tag{2.3}
\]

#### Proof

For unit weights, (1.3) says that the interval block

\[
 x_p,x_{p+1},\ldots,x_{p+m}
\]

of `m+1` atoms must fit under a prefix containing at least `m+1` atoms.
Because the sequence is strictly increasing, this is equivalent to

\[
 x_m\le x_{p+m}-x_p.
\]

This is exactly (2.3), with `n=p`. `square`

Nondecreasing clocks with repeated positions are handled by retaining the
corresponding integer multiplicities at their atoms.  Equivalently, they
are the jump trains of integer-valued nondecreasing subadditive prices.

## 3. Counting clocks are dense in the whole cone

Let `rho in C_AW`, and let `f` be its nonnegative nondecreasing
subadditive cumulative price, with the standard initial-jump convention.
For every positive integer `N`, define

\[
 g_N(x)=\lceil Nf(x)\rceil,
 \qquad
 f_N(x)={g_N(x)\over N}.                            \tag{3.1}
\]

At the origin set `g_N(0)=0`, as for every covering price.

### Theorem 3.1 (single-clock quantization)

For every `N`:

1. `g_N` is integer-valued, nonnegative, nondecreasing and subadditive;
2. its Stieltjes measure is a counting measure

   \[
   \eta_N=\sum_j\delta_{a_j^{(N)}}                 \tag{3.2}
   \]

   whose atom sequence is nondecreasing and superadditive;
3. the scaled counting measure

   \[
   \rho_N={1\over N}\eta_N                         \tag{3.3}
   \]

   converges vaguely to `rho`; and
4. for the Rayleigh pairing,

   \[
   \boxed{
   \int K\,d\rho_N\longrightarrow\int K\,d\rho.
   }                                                 \tag{3.4}
   \]

If `rho` is purely atomic, every `rho_N` may be taken on the same atomic
support as `rho`.

#### Proof

The elementary ceiling inequality

\[
 \lceil a+b\rceil\le\lceil a\rceil+\lceil b\rceil
\]

and subadditivity of `f` give

\[
 g_N(x+y)
 \le \lceil Nf(x)+Nf(y)\rceil
 \le g_N(x)+g_N(y).
\]

Thus assertion 1 holds.

Every jump of an integer-valued monotone function is an integer.  Split a
jump of size `r` into `r` unit atoms at the same position.  If

\[
 a_j^{(N)}=\sup\{x:g_N(x)\le j\}                   \tag{3.5}
\]

with a consistent one-sided convention, then for `x<a_i^(N)` and
`y<a_j^(N)` one has

\[
 g_N(x+y)\le g_N(x)+g_N(y)\le i+j.
\]

Letting `x` and `y` increase to their suprema gives

\[
 a_{i+j}^{(N)}\ge a_i^{(N)}+a_j^{(N)}.             \tag{3.6}
\]

This proves assertion 2.  A bounded price simply gives a finite train, or
equivalently a train that is eventually at the cemetery point `infinity`,
where `K(infinity)=0`.

Uniformly on the nonnegative line,

\[
 0\le f_N-f<{1\over N}.                            \tag{3.7}
\]

The convergence of the cumulative functions implies vague convergence of
their Stieltjes measures.  More explicitly, interval masses converge at
every common continuity endpoint, and compactly supported continuous test
functions follow by the standard monotone-class approximation.  When `f`
is a step function, `g_N` can jump only where `f` jumps, proving the final
support statement.

Finally, let `mu-nu` denote the finite signed Rayleigh job/socket measure
whose signed tail is `K`.  Stieltjes summation by parts gives

\[
 \int K\,d\rho_N-\int K\,d\rho
 =\int(f_N-f)\,d(\mu-\nu).
\]

Therefore (3.7) yields

\[
 \left|\int K\,d\rho_N-\int K\,d\rho\right|
 \le {\|\mu-\nu\|_{TV}\over N},                  \tag{3.8}
\]

which proves (3.4). `square`

### Corollary 3.2 (discrete rays are an exact positivity test)

The following statements are equivalent:

1. `int K d rho>=0` for every anchored-window measure for which the
   Rayleigh pairing is defined;
2. for every locally finite nondecreasing superadditive sequence
   `0=a_0<=a_1<=...`,

   \[
   \boxed{\sum_{j\ge0}K(a_j)\ge0;}                 \tag{3.9}
   \]

3. the same inequality holds for every integer-valued nondecreasing
   subadditive price.

#### Proof

Every counting clock is in `C_AW` by Theorem 2.1 (or by the inverse-clock
theorem when positions repeat), proving necessity.  Conversely, apply
(3.9) to every `eta_N` in Theorem 3.1, divide by `N`, and pass to the limit
using (3.4). `square`

Thus the phrase “mixture or limit of clock measures” can be strengthened:
no mixture is required.  Every anchored-window measure is a pairing-limit
of **single scaled counting clocks**.

## 4. Extreme rays and the role of arithmetic grids

### Theorem 4.1 (every strict counting clock is extreme)

For every sequence (2.1) satisfying (2.3), the ray generated by `eta_x` is
an extreme ray of `C_AW`.

#### Proof

Suppose

\[
 \eta_x=\rho_1+\rho_2,
 \qquad \rho_1,\rho_2\in C_{AW}.                   \tag{4.1}
\]

Positivity implies that both summands are supported on the set
`{x_0,x_1,...}`.  Write

\[
 \rho_1(\{x_n\})=c_n,
 \qquad
 \rho_2(\{x_n\})=1-c_n.
\]

The singleton case of (1.1) applied to `rho_1` gives

\[
 c_n\le c_0.
\]

Applied to `rho_2`, it gives

\[
 1-c_n\le1-c_0.
\]

Hence `c_n=c_0` for every `n`, so

\[
 \rho_1=c_0\eta_x,
 \qquad
 \rho_2=(1-c_0)\eta_x.
\]

This is extremality. `square`

### Corollary 4.2 (arithmetic grids are extreme but not exhaustive)

For every `h>0`, the arithmetic comb

\[
 \sum_{n\ge0}\delta_{nh}                            \tag{4.2}
\]

is an extreme ray.  It is very far from being the only one: for example,

\[
 \sum_{n\ge0}\delta_{hn^2}                         \tag{4.3}
\]

is another extreme ray, because `(m+n)^2>=m^2+n^2`.

Consequently, arithmetic grids do not exhaust the extreme-ray tests for
the anchored-window cone.  No claim about the closed conic hull of the
arithmetic rays is needed here.

There are also two distinct notions of Rayleigh extremality.

1. If the first positive atom `x_1` lies at or beyond the unique minimum
   `zeta` of `K`, then superadditivity gives `x_n>=n x_1`, and monotonicity
   of `K` on `[zeta,infinity)` gives

   \[
   \sum_{n\ge0}K(x_n)
   \ge
   \sum_{n\ge0}K(nx_1)>0.                           \tag{4.4}
   \]

   Thus on this postminimum face the arithmetic grid with the same first
   atom is the termwise Rayleigh minimizer.  The strict positivity on the
   right is the proved all-ceiling-ray theorem.

2. Arithmetic grids are not global Rayleigh minimizers at fixed asymptotic
   slope.  Define

   \[
   b_{2q}=2qA,
   \qquad
   b_{2q+1}=2qA+{15A\over16}.                       \tag{4.5}
   \]

   This sequence is superadditive: parity-even sums are equalities, while
   an odd-plus-odd sum has slack `A/8`.  Its asymptotic slope is `A`.  The
   even terms agree with the arithmetic grid `nA`, while

   \[
   K\left(2qA+{15A\over16}\right)<K((2q+1)A)
   \qquad(q\ge0).                                   \tag{4.6}
   \]

   For `q=0`, this is the proved strict increase of `K` on
   `[15A/16,A]`; for `q>=1`, both arguments are above `A`, where `K` is
   strictly increasing.  Hence

   \[
   \sum_{n\ge0}K(b_n)
   <
   \sum_{n\ge0}K(nA).                              \tag{4.7}
   \]

   Both sums are nevertheless positive by the already-proved two-slot
   Bellman theorem.  Thus (4.7) is not a Rayleigh counterexample; it only
   refutes arithmetic-grid optimality under an asymptotic-slope
   normalization.

## 5. Exact remaining boundary

The density theorem removes a possible continuum obstruction: there is no
anchored-window separator that is invisible to all discrete
superadditive clocks.

It does **not** prove (3.9).  By Corollary 3.2, proving (3.9) for all
superadditive atom sequences is exactly the complete all-grid
Bellman/anchored-window problem, not a smaller residual lemma.  Arithmetic
grids alone cannot suffice because Theorem 4.1 supplies infinitely many
nonarithmetic extreme rays and (4.7) shows that even objective comparison
with the arithmetic grid can fail.

## 6. Dependencies

1. `MATH_THEOREM_SUBADDITIVE_PRICE_MEASURE_AND_SUPERADDITIVE_CLOCK_REDUCTION_20260804.md`;
2. `MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md`;
3. `MATH_OBSTRUCTION_MAXIMUM_DENSITY_CEILING_LOWER_BOUND_20260804.md`.
