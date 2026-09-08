# Coordinate-necklace diagonal factors have a macroscopic GK top-weight cost

**Status (2026-08-21).**  This note gives an asymptotic obstruction to every
factor that is a union of whole coordinate-necklace diagonals from
Proposition 4.2 of
`MATH_THEOREM_GK_ORIENTATION_BIREGULARITY_AND_MAXWEIGHT_DFACTOR_GATE_20260821.md`.
In the DCC regime `H=Theta(sqrt(b log b))`, the aggregate extra cost is
`Omega(W_b)`.  The diagonal counts may be coupled arbitrarily across
necklace-pair blocks; requiring the same count in every block is not used.
Thus this cyclic-equivariant subclass does **not** prove `Gamma=o(W_b)`.

This is not an obstruction to an unrestricted maximum-weight `d_r`-factor.
It is also not a statement about phase diagonals in a genuine cyclic wreath
deck, nor about packing translated product atoms.  Those are separate levels.

Throughout, `b` is an odd prime,

\[
             W_b={2b\choose b},\qquad
             L_r={b\choose r}^2.                         \tag{0.1}
\]

## 1. Diagonal cost as the capped area of a circular bridge

Fix `1<=r<=b-1`.  Replace a column `(b-r)`-set `Y` by its complement
`Z`, an `r`-set.  Write

\[
        \xi_i={\bf1}_{i\in X},\qquad
        \zeta_i={\bf1}_{i\in Z}.                         \tag{1.1}
\]

For a relative shift `t`, define the zero-sum circular bridge

\[
 D^{(t)}_0=0,\qquad
 D^{(t)}_j=\sum_{i=1}^j(\xi_i-\zeta_{i+t}),
 \qquad 0\le j\le b,                                   \tag{1.2}
\]

where indices of `Z` are cyclic.  Put

\[
 h^{(t)}_s=D^{(t)}_s-\min_{0\le j<b}D^{(t)}_j,
 \qquad s\in\mathbb Z_b.                               \tag{1.3}
\]

The diagonal with relative shift `t` consists of the `b` sources obtained
by simultaneously rotating `X` and `Z`.  Let `k_(s,t)` be the GK top excess
of its source with simultaneous rotation `s`, and give the source weight
`min(k_(s,t),H)`.  Its total diagonal weight is

\[
                    C_t=\sum_{s\in\mathbb Z_b}
                         \min(k_{s,t},H).                \tag{1.4}
\]

### Lemma 1.1 (bridge-area lower bound)

For every `X,Z,s,t`,

\[
 k_{s,t}\ge 2h^{(t)}_s,
 \qquad
 C_t\ge 2\sum_s\min(h^{(t)}_s,H/2).                    \tag{1.5}
\]

#### Proof

At pair boundaries, the interleaved sign word has height
`2(D^(t)_(s+j)-D^(t)_s)`.  Its minimum over pair boundaries is therefore
`-2h^(t)_s`.  The full interleaved minimum also includes the odd boundaries
and can only be smaller.  Since GK top excess is the negative of that full
minimum, the first inequality follows.  Apply the increasing map
`u -> min(u,H)` and sum; `min(2h,H)=2min(h,H/2)`.  \(\square\)

Thus a cheap whole diagonal requires one circular difference bridge to
have abnormally small capped area through *all* of its rotations.  This is
the rigidity absent when individual source edges may be selected separately.

## 2. A discrete capped-area small-deviation lemma

We use the following elementary random-walk estimate.  Constants in this
section are absolute.

### Lemma 2.1 (capped bridge-area small deviation)

Let `(S_i)_(i=0)^n` be a uniformly random simple symmetric bridge of even
length `n`, and let

\[
 A_Q(S)=\sum_{i=0}^{n-1}\min\{S_i-\min_jS_j,Q\}.         \tag{2.1}
\]

There are constants `c,C>0` such that, whenever

\[
 n\ge 2,\qquad n\le T\le n^{3/2},\qquad
 Q\ge C T/n,                                          \tag{2.2}
\]

one has

\[
 \Pr\{A_Q(S)\le T\}
 \le Cn^C\exp\!\left(-c{n^3\over T^2}\right).         \tag{2.3}
\]

#### Proof

Cyclically rotate a bridge immediately after a minimum.  Its heights above
the minimum become a nonnegative excursion, and the multiset of those
heights, hence (2.1), is unchanged.  Allowing for the choice of the minimum
costs at most a factor `n`.

For `theta>0`, let `K_theta` be the symmetric transfer operator on
`ell^2(Z_(>=0))` whose nearest-neighbour entry from `i` to `j` is

\[
 \exp\{-\tfrac\theta2(\min(i,Q)+\min(j,Q))\}.           \tag{2.4}
\]

The standard one-dimensional uncertainty estimate gives

\[
 \|K_\theta\|\le
 2\exp(-c\theta^{2/3})                                \tag{2.5}
\]

provided `0<theta<=1` and `Q>=C theta^(-1/3)`.  For completeness, put
`V(i)=min(i,Q)` and subtract the quadratic form of `K_theta` from
`2||f||_2^2`.  Directly expanding the nearest-neighbour terms shows that
it dominates the saturated potential

\[
 \sum_{i\ge0}\min\{\theta V(i),1\}f_i^2,             \tag{2.6}
\]

and, on every edge with both endpoints at most `4R`, it also dominates a
constant multiple of `(f_(i+1)-f_i)^2`, where
`R=theta^(-1/3)`.  (On this range the exponential edge weights are bounded
below.)  If at least half the `ell^2` mass lies above `R`, (2.6) costs at
least `c theta R=c theta^(2/3)`, since `Q>=CR`.  Otherwise at least half
the mass lies in `[0,R]`; the one-ended discrete Poincare inequality

\[
 \sum_{i=0}^R f_i^2
 \le (R+1)^2\sum_{i=-1}^{R-1}(f_{i+1}-f_i)^2,
 \qquad f_{-1}=0,                                    \tag{2.6a}
\]

costs at least `c/R^2=c theta^(2/3)` in the locally unweighted gradient
term.  This proves (2.5).  The saturation in (2.6) is needed when
`theta Q` is large; in the application below one in fact has
`theta Q=o(1)`.

Exponential Markov and (2.5) bound the number of excursions of capped area
at most `T` by

\[
 2^n\exp\{\theta T-cn\theta^{2/3}\}.                  \tag{2.7}
\]

Take `theta=c_0(n/T)^3`, with `c_0` a sufficiently small absolute
constant.  Conditions (2.2) make (2.5) applicable, and (2.7) is at most
`2^n exp(-c n^3/T^2)`.  Finally divide by
`{n\choose n/2}>=c2^n/sqrt(n)` and absorb the Vervaat and endpoint factors
into `Cn^C`.  \(\square\)

The polynomial prefactor is harmless below: the constant multiplying
`b^(3/2)/sqrt(log b)` will be chosen small enough to make the right side
an arbitrarily large negative power of `b`.

## 3. A random diagonal is almost never cheap enough

Fix constants `0<c_1<=c_2<infinity` and assume

\[
        c_1\sqrt{b\log b}\le H\le c_2\sqrt{b\log b}.   \tag{3.1}
\]

Let `X,Z` be independent uniform `r`-subsets, with

\[
                       b/3\le r\le 2b/3.              \tag{3.2}
\]

For fixed `t`, erase the zero increments from (1.2).  If

\[
                  J=|X\setminus(Z+t)|,                \tag{3.3}
\]

the erased path is, conditional on `J=j`, a uniform simple bridge of
length `2j`.  Hypergeometric concentration gives

\[
                    \Pr\{J<b/10\}\le e^{-cb}.         \tag{3.4}
\]

The original capped area dominates the capped area at the nonzero-step
times.  Apply Lemma 2.1 conditionally on `J`, with

\[
              T_b=\varepsilon,{b^{3/2}\over\sqrt{\log b}},
              \qquad Q=H/2,                           \tag{3.5}
\]

where `epsilon>0` is a sufficiently small constant depending only on
`c_1,c_2`.  Since `2J=Theta(b)` off (3.4), (3.1) implies
`Q >= C T_b/(2J)`.  Choosing `epsilon` small in (2.3) gives, uniformly in
`r` satisfying (3.2) and in fixed `t`,

\[
 \Pr\left\{2\sum_s\min(h^{(t)}_s,H/2)<2T_b\right\}
 \le b^{-3}.                                         \tag{3.6}
\]

By Lemma 1.1,

\[
                         \Pr\{C_t<2T_b\}\le b^{-3}.   \tag{3.7}
\]

No independence among the `b` relative shifts is asserted or needed.

### Corollary 3.1 (order statistics of all relative shifts)

Let `C_(1)<=...<=C_(b)` be the ordered diagonal weights of one random
necklace-pair block.  Uniformly for `1<=p<=b`,

\[
 \mathbb E\sum_{j=1}^p C_{(j)}
 \ge 2T_b(p-b^{-1}).                                 \tag{3.8}
\]

#### Proof

Let `N_T=|{t:C_t<2T_b}|`.  Pointwise,

\[
             \sum_{j=1}^pC_{(j)}\ge2T_b(p-N_T).       \tag{3.9}
\]

By (3.7) and linearity, `E N_T<=b*b^(-3)<=b^(-2)`, which is even stronger
than the error displayed in (3.8).  \(\square\)

## 4. The aggregate diagonal obstruction

Recall the persistent count

\[
 n_r=\max\left\{0,
 \left\lfloor{b-|2r-b|-H+2\over2}\right\rfloor\right\}. \tag{4.1}
\]

There are `b-r` `A`-diagonals and `r` `B`-diagonals in every coordinate-
necklace block.  Put `S_r=N_r/b`, the number of necklaces on either shore.
The complement of a diagonal `d_r`-factor has degree
`(b-r-n_r)S_r` in orientation `A` and `(r-n_r)S_r` in orientation `B`.
Since one whole diagonal has `b` source edges, the complement therefore
uses exactly `p_r S_r^2` whole diagonals in total, where

\[
 p_r=(b-r-n_r)+(r-n_r)=b-2n_r
 \in\{|2r-b|+H-2,\ |2r-b|+H-1\}                    \tag{4.2}
\]

Orientation and row/column incidence restrictions can only increase the
cost relative to choosing the globally cheapest `p_r S_r^2` diagonals from
all necklace-pair blocks.

For every central split

\[
                        |2r-b|\le\sqrt b,             \tag{4.3}
\]

we have `p_r>=H/2` for all sufficiently large `b`.  Among all
`bS_r^2` diagonal units, the exact proportion having cost below `2T_b` is
the probability in (3.7): uniform subsets induce uniform necklace pairs,
and the relative shift is uniform.  Hence the *deterministic* number of
such cheap units is at most

\[
       bS_r^2\,b^{-3}=S_r^2/b^2.                     \tag{4.4}
\]

Consequently every admissible whole-diagonal complement, even one that
couples its diagonal counts arbitrarily across blocks, has deleted weight

\[
 \begin{aligned}
 R_{diag,r}
 &\ge 2T_b\left(p_rS_r^2-{S_r^2\over b^2}\right)\\
 &\ge cH{b^{3/2}\over\sqrt{\log b}}{N_r^2\over b^2}
 \ge c'L_r.                                          \tag{4.5}
 \end{aligned}
\]

Here primality ensures that every proper rank-`r` subset necklace has size
`b`; diagonal cost is representative-independent up to permuting relative
shifts.  Thus (4.4) is exact counting over the actual necklace blocks, not
a probabilistic construction.

Let `R_diag` denote this deleted weight, summed over both orientations and
all splits.  The squared-binomial law `L_r/W_b` has central fluctuations of
order `sqrt(b)`, so

\[
        \sum_{|2r-b|\le\sqrt b}L_r\ge cW_b.            \tag{4.6}
\]

Combining (4.5)--(4.6),

\[
                         R_{diag}\ge cW_b.             \tag{4.7}
\]

For comparison, let `R_un` be the cost of deleting the same number of
individually cheapest edges in every split and orientation.  The exact GK
survivor formulas imply

\[
 R_{un}\le {C\over b}\sum_r(|2r-b|+H+1)^{3/2}L_r
             +He^{-cb}W_b=o(W_b).                     \tag{4.8}
\]

Here is the finite argument behind (4.8).  Put
`Delta=|2r-b|+H+1`.  The number deleted in either orientation is at most
`Delta L_r/b`.  For `|2r-b|<=b/64` and all sufficiently large `b`, also
`H<=b/64`.  Take

\[
                       u=\lceil4\sqrt\Delta\rceil+8.   \tag{4.8a}
\]

Then `u<=sqrt(b)`.  The two survivor-drop inequalities (4.6) of the
alternating-GK theorem show that between top excess zero and top excess at
most `2u+1` there are at least `Delta L_r/b` edges of either orientation.
Consequently the individually cheapest deletion has cost at most

\[
             (2u+1){\Delta L_r\over b}
             \le {C\over b}\Delta^{3/2}L_r.           \tag{4.8b}
\]

The squared-hypergeometric tail `|2r-b|>b/64` is `e^(-cb)`; charge it the
trivial capped cost `H L_r`.  Finally the moment bound
`E|2R-b|^(3/2)=O(b^(3/4))` under `P(R=r)=L_r/W_b` gives (4.8).

If `U` is the unconstrained top-`K_r` weight and `F_diag` is the greatest
weight obtainable by whole necklace diagonals, then, writing `T_all` for
the weight of all orientation edges,

\[
 U-F_{diag}
 =(T_{all}-R_{un})-(T_{all}-R_{diag})
 =R_{diag}-R_{un}.                                   \tag{4.9}
\]

### Theorem 4.1 (macroscopic coordinate-necklace diagonal gap)

For odd primes `b` and `H=Theta(sqrt(b log b))`, every row/column-regular
selection that is a union of whole coordinate-necklace diagonals and has
the prescribed degree `d_r` in each orientation satisfies

\[
 \boxed{\displaystyle
       \sum_{r,c}\bigl(U_{r,c}-F^{diag}_{r,c}\bigr)
       \ge cW_b.}                                    \tag{4.10}
\]

In particular, the explicit necklace-diagonal route has
`Gamma not=o(W_b)`.  The failure is aggregate: rare deterministic bad
blocks alone are not the reason.  A marginal random block has only
polynomially few shifts, whereas making a whole diagonal cheap requires a
random bridge-area small deviation of polynomially small probability.

## 5. Exact scope

Theorem 4.1 rules out every whole-diagonal subclass of the coordinate-
necklace construction, including selections that move diagonal capacity
between different necklace-pair blocks.  It leaves open all of the following:

1. an unrestricted maximum-weight `d_r`-factor in the GK orientation graph;
2. phase-diagonal decompositions inside genuine cyclic wreath decks; and
3. collision-free packing of whole translated product atoms.

Thus it must not be cited as an obstruction to the exact biregularity/TU
theorem, nor as a fixed-order coinstantiation obstruction.
