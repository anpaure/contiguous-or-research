# General block splits and recursive SCD regrouping: exact compilers and limits

Date: 2026-09-05. The compact policy-uniform finite ledger barrier is
incorporated in `MASTER_HANDOFF.md`, Appendix A.6. This note is supplemental.

## 1. Results and scope

There is no coefficient-one construction in this note. The two proposed
extensions of the cross-split construction can now be analyzed rigorously:

\[
 \boxed{C_d^{\mathrm{one}}\longrightarrow\sqrt2.}       \tag{1}
\]

Here `C_d^{one}` optimizes over **every nontrivial two-support partition
for every length tuple**, not just an isolated longest factor.

For recursive adaptive product-SCD regrouping, with global Euler assembly
of the terminal paired rectangles, let `R_d` be the optimal limiting
coefficient. Then

\[
 \boxed{R_d\longrightarrow R_*:=\inf_{q\ge2}R_q,
 \qquad {2\over\sqrt e}\le R_*\le c_4<1.27.}           \tag{2}
\]

The lower bound is `2/sqrt(e)=1.2130613194...`, not one. The upper bound
`c_4` is the four-block construction in the preceding scratch note;
the new limit and lower-bound proofs do not use its numerical certificate.
That upper endpoint can instead be replaced by the closed-form
three-block constant `1.3010622654...` without any certified quadrature.

The exact value of `R_*` within this interval is not determined. In
particular, (2) is not a claim that the lower endpoint is achievable.

Positive results included here are:

- A global Euler compiler that makes recursive regrouping literal without
  paying a whole extra bridge at every terminal rectangle.
- An exact integer dynamic programme for the optimum recursive main cost.
- A rigorous five-factor improvement: near five equal lengths, recursive
  regrouping improves the main cost from `5/3` to at most `73/48` after
  homogeneous normalization. Consequently `R_5<C_5^{one}`.
- A sharp relaxed rank-profile lower bound, and an exact nonnegative
  formula for the gap above `2/sqrt(e)`.

All block constants mean: first fix `d`, let the common block size tend
to infinity, and then study `d->infinity`. A controlled diagonal can
realize the limiting upper coefficient; arbitrary simultaneous growth
is not inferred from a fixed-d error term.

The recursion class refines products of ascending chains by complete
product SCDs on selected groups of factors, keeping the common rank
center, and finally pays two bridge lengths per paired rectangle.
It permits grouping decisions to change at every child tuple. It does
not include nonsymmetric refinements with moving centers or a new
compression that shares leading-order positions across terminal
rectangles. Those are genuine ways to leave the obstruction's scope.

## 2. Signed families and the exact global compiler

Split `k=dh` coordinates into `d` blocks of size `h`, with a pivot in
each. On each block minus its pivot take a Boolean SCD, with
`A_h=W(h-1)` chains. For each tuple choose one of `2^{d-1}` sign patterns
with first sign positive. A positive factor is its original chain;
a negative factor is its complemented chain, reversed into ascending
order. Pair the product of these desired chains with its full complement.

These paired families partition the cube. The first pivot decides
whether to complement a target globally; the other pivots determine
the signs; SCD ownership determines the chain tuple. This is the same
literal partition mechanism as in the preceding four-block construction.

At any node, merge two factors by the standard product SCD. For lengths
`a,b`, its child chain lengths are

\[
              |a-b|+1,\ |a-b|+3,\ldots,a+b-1.        \tag{3}
\]

The child products partition the parent product; their full complements
partition its complementary family. Repeat adaptively until two factors
remain. This preserves a partition at every stage, irrespective of the
later choices at different children.

For a terminal pair of desired chains `C` on `U` and `D` on `V=U^c`,
create an edge between the bridge vertices

\[
          (U,C),\qquad (V,D^c).
\]

Use both directed arcs. The edge's two boundary orientations realize all
nonempty targets in `C x D` and its full complement: a suffix of `beta_V(D^c)` followed by
a prefix of `beta_U(C)`, and the reverse boundary, respectively.
These are ordinary literal interval unions, not abstract chain labels.

Globally collect **all** terminal edges from all signed initial tuples.
Each connected component has an Euler circuit. Output the bridge of
every arc tail, then one extra starting bridge. Concatenate the component
words. No asserted witness crosses a component join.

Let `E` be the number of terminal edges, `M` the sum of their two chain
lengths, and `V_cat` the number of distinct bridge vertices used. Since
`|beta(C)|=|C|+O(1)`, with absolute error at most one,

\[
 \boxed{|N-M|\le2E+(k+1)V_{\rm cat}.}                \tag{4}
\]

In contrast, separately linearizing each two-bridge cycle could cost
`Theta(sqrt(h))` per leaf and lose a leading constant. Global assembly
is essential here.

### Why the cuts really are negligible

Use one deterministic hook SCD at every binary merge. Any chain arising
under an adaptive history is a chain from one of the fixed ordered
binary-tree product SCDs on its support. For a support consisting of
`m` original blocks, there are at most `m! 4^{m-1}` such trees.
For each tree, multiplying the initial signed chain partitions gives a
chain partition of that support cube, with at most `2^{mh}` chains.
Include their complements as well.

Only proper supports occur at terminal vertices. Thus the explicit
coarse bound

\[
 V_{\rm cat}\le B_d2^{(d-1)h},\qquad B_d=2d!8^d,    \tag{5}
\]

is sufficient. It allows histories depending on outside lengths: every
resulting chain is still in this finite union of tree catalogues.

For one initial tuple put `L=sum_i a_i`. Every intermediate chain has
length at most `L`, and a binary merge has at most `L` children. Hence
there are at most `L^{d-2}` terminal rectangles. Uniform SCD length
moments therefore give

\[
 E\le2^{d-1}\sum_{\rm tuples}(\sum_i a_i)^{d-2}
                  =O_d(2^{dh}/h)=o(W(dh)).           \tag{6}
\]

Also `(dh+1) B_d 2^{(d-1)h}=o(W(dh))` for fixed `d`. Equations (4)--(6)
prove that the actual word and its recursive main-cost ledger have the
same asymptotic coefficient.

## 3. Exact discrete optimization

Let `P_d(a_1,...,a_d)` be the least sum of terminal two-chain lengths
over binary product-SCD refinements. Then

\[
 P_2(a,b)=a+b,
\]

\[
 \boxed{P_d(\mathbf a)=
 \min_{i<j}\sum_{r=|a_i-a_j|+1,\,\mathrm{step}\,2}^{a_i+a_j-1}
       P_{d-1}(r,\mathbf a_{\setminus\{i,j\}}).}      \tag{7}
\]

The minimum is finite and attained. Choosing a minimizing pair and then
optimizing every child is a deterministic literal refinement algorithm.
The complete full-cube main cost is

\[
                   2^{d-1}\sum_{\rm SCD\ tuples}P_d(\mathbf a).   \tag{8}
\]

A simultaneous multi-factor SCD merge offers no different length law:
the chain-length multiset of a symmetric product is determined by its
rank polynomial. A fixed binary-tree SCD produces the same multiset,
and (7) can simulate that tree before allowing further decisions.

A one-step support split `I,J` has main cost

\[
 V_I w_J+w_I V_J,\qquad V_I=\prod_{i\in I}a_i,
\]

where `w_I` is the central coefficient of
`prod_{i in I}(1+z+...+z^{a_i-1})`. It is an admissible recursion: finish
all merges inside `I` and `J`, then stop. Thus the recursive optimum is
pointwise no worse than the optimum over all one-step partitions.

## 4. The correct size-biased limit

Uniformly selected initial SCD chain lengths divided by `sqrt(h)`
converge to independent Rayleigh variables `X_i`. The Gaussian tail
bound from their central-binomial tail ratios gives all needed moment
convergence.

After weighting a tuple by its volume `prod_i X_i`, each coordinate
instead has density

\[
             g(x)=\sqrt{2/\pi}\,x^2e^{-x^2/2},\quad x>0.         \tag{9}
\]

This is the norm of a three-dimensional standard Gaussian, denoted `Z`.
Using the unweighted Rayleigh law for the normalized cost would give
the wrong optimization problem.

For positive lengths define `f_I(0)` to be the density at zero of the
sum of independent uniforms `[-x_i/2,x_i/2]`, `i in I`. Then

\[
 \boxed{C_d^{\rm one}={1\over2}\sqrt{\pi d/2}\,
 \mathbb E\min_{\varnothing\ne I\subsetneq[d]}
       \{f_I(0)+f_{I^c}(0)\},}                      \tag{10}
\]

with independent inputs of law (9).

To check the normalization, the width of an `m`-factor grid, divided by
`h^{(m-1)/2}`, tends to `prod_{i in I}x_i f_I(0)`. This is the elementary
Riemann sum for its central section. The signed-tuple prefactor is
`(sqrt(d)/2)(2/pi)^{(d-1)/2}` under the Rayleigh measure. Multiplication
by `prod_i x_i` changes that measure by `E[X]^d=(pi/2)^{d/2}`, giving
exactly `(1/2)sqrt(pi d/2)` in (10). The same calculation applies to
(12). Polynomial SCD moment bounds justify these finite-d limits.

For recursion, the volume-weighted limit of (3) is the probability kernel

\[
 \boxed{K(a,b;dr)={r\over2ab}
             \mathbf1_{|a-b|<r<a+b}\,dr.}           \tag{11}
\]

Let `T_d` be the optimal expected terminal sum of reciprocals under
adaptive applications of this kernel. Its exact Bellman recursion is

\[
 T_2(a,b)=a^{-1}+b^{-1},
\]

\[
 T_d(\mathbf x)=\min_{i<j}
 \int_{|x_i-x_j|}^{x_i+x_j}
 {r\over2x_ix_j}T_{d-1}(r,\mathbf x_{\setminus\{i,j\}})\,dr,
\]

\[
 \boxed{R_d={1\over2}\sqrt{\pi d/2}\,
                     \mathbb E T_d(Z_1,\ldots,Z_d).}             \tag{12}
\]

The functions `T_d` are homogeneous of degree `-1`, continuous on the
positive orthant, and bounded above by `sum_i 1/x_i`. These facts follow
inductively from (11); the apparent singularity at `r=0` is integrable
because the kernel contains `r`. In fact
`integral r^{-1} K(a,b;dr)=1/max(a,b)`.

For fixed `d`, dividing (7) by the tuple volume gives Riemann sums for
(11)--(12), locally uniformly for positive initial lengths. To justify
the induction near a zero child length, first truncate `r<epsilon`;
the unweighted cost is bounded by a polynomial of degree `d-2`, so that
piece tends uniformly to zero with `epsilon`. The remaining compact
interval is an ordinary Riemann sum. The bound
`P_d(a)<=prod_i a_i sum_i 1/a_i` supplies polynomial domination for
the initial SCD average. This proves (12) for actual words via (4).

## 5. All one-step partitions return to sqrt(2)

For deterministic lengths put `S_I=sum_{i in I}x_i^2`.
The uniform sum is symmetric unimodal and has variance `S_I/12`.
If its peak is `m=f_I(0)`, the elementary density-height variance bound
`Var>=1/(12m^2)` gives

\[
                         f_I(0)\ge S_I^{-1/2}.      \tag{13}
\]

For example, integrate
`Pr(|Y|>t)>=max(1-2mt,0)` to prove that variance bound.

Under (9), with probability tending to one,

\[
 \sum_i Z_i^2=(3+o(1))d,\qquad
                   \max_i Z_i/\sqrt d=o(1).         \tag{14}
\]

Uniformly over **all** subsets with `S_I>=d/16`, the triangular-array
CLT and unimodality imply

\[
                 f_I(0)\ge(1-o(1))\sqrt{6/(\pi S_I)}.            \tag{15}
\]

Here is why there is no invalid union bound over `2^d` subsets. On (14),
every possible such array has maximum summand divided by its standard
deviation tending to zero. The characteristic-function expansion of
`sin(t)/t` proves the CLT for any sequence of these arrays. For a fixed
`epsilon>0`, peak times `2 epsilon sigma` dominates the probability
inside that interval. The CLT bounds that probability by the normal
limit; then let `epsilon` decrease to zero. If (15) were not uniform,
a bad subsequence of arrays would contradict this same argument.

If a partition has one shore with `S_I<d/16`, (13) makes its normalized
cost in (10) at least `sqrt(2 pi)>sqrt(2)`. Otherwise apply (15) on both
shores and minimize `s^{-1/2}+(S-s)^{-1/2}` at `s=S/2`. Equations
(14)--(15) then give normalized cost at least `sqrt(2)-o(1)`, uniformly
over every partition. Taking expectations proves the required liminf.

For the matching upper bound, note the exact Gaussian mixture identity:
if `Z` has law (9), then `Z` times an independent uniform on `[-1/2,1/2]`
is `N(0,1/4)`. This is one coordinate of an isotropic Gaussian of radius
`Z`, divided by two. Hence for a fixed subset of size `m`,

\[
                         \mathbb E f_I(0)=\sqrt{2/(\pi m)}.
\]

A fixed balanced partition in (10) therefore gives

\[
 C_d^{\rm one}\le{\sqrt d\over2}
       \{\lfloor d/2\rfloor^{-1/2}+\lceil d/2\rceil^{-1/2}\}
                    \longrightarrow\sqrt2.          \tag{16}
\]

This proves (1). Isolating the largest factor alone is worse: its
coefficient is at least a constant times `sqrt(d/log d)`, since
`E max_i Z_i^2=O(log d)` and Jensen bounds `E[1/max_i Z_i]` below.

## 6. A sharp rank-law obstruction for all recursive policies

The kernel (11) is the radius law of the sum of two independent uniformly
oriented three-dimensional vectors of lengths `a,b`. Define

\[
                        \phi_a(t)={\sin(at/2)\over at/2}.
\]

Direct integration gives

\[
                  \phi_a(t)\phi_b(t)=\int\phi_r(t)K(a,b;dr).     \tag{17}
\]

Thus the product of these characteristic functions over the current
factors is a bounded martingale, even when the next merge depends on
the entire current tuple.

Start with `d` independent inputs (9), follow any adaptive policy to two
terminal radii `A,B`, and make one final kernel merge into `R`.
Equation (17) and the Gaussian mixture identity give

\[
               \mathbb E\phi_R(t)=e^{-dt^2/8}.
\]

The mixture of centered uniforms of lengths `R` is therefore Gaussian.
This determines the mixing radius uniquely: its density follows by
differentiating `E[R^{-1} 1_{R>2|x|}]`. Consequently

\[
 R/\sqrt d\sim\chi_3,\qquad
 R^2/d\text{ has density }
                 g(s)={\sqrt s e^{-s/2}\over\sqrt{2\pi}}.        \tag{18}
\]

No independence between `A,B` is claimed or needed.

Put

\[
 L={(A-B)^2\over d},\quad U={(A+B)^2\over d}.
\]

Conditionally on `A,B`, `R^2/d` is uniform on `[L,U]`. Define the
measure `eta` on intervals by weighting their probability law by
`1/(U-L)`. Then

\[
 g(s)=\int\mathbf1_{L<s<U}\,d\eta,
 \qquad
 C={1\over2}\sqrt{\pi d/2}\,\mathbb E(A^{-1}+B^{-1})
       =\sqrt{2\pi}\int\sqrt U\,d\eta.              \tag{19}
\]

For every threshold `r>0` and every interval `[L,U]`,

\[
 \sqrt U\ge\sqrt r\,\mathbf1_{L<r<U}
            +{1\over2}\int_r^\infty
                   {\mathbf1_{L<s<U}\over\sqrt s}\,ds.
\]

Integrating this inequality and using (18)--(19) gives

\[
                  C\ge(r+1)e^{-r/2}.
\]

One can first take thresholds without endpoint atoms and pass to a limit;
the density (18) is continuous. Maximizing at `r=1` proves

\[
                    \boxed{R_d\ge2/\sqrt e\quad(d\ge2).}        \tag{20}
\]

For the present continuous inputs, there are no endpoint atoms at any
positive threshold. Indeed there are finitely many possible merge
histories. Before restricting to the event that a history is selected,
its terminal sums and differences are homogeneous functions of the
initial radii and independent angle variables. Scaling all initial
radii shows that any positive level set has probability zero. Selecting
a subset of that null set cannot give it positive mass.

Thus there is the exact gap identity

\[
 C-{2\over\sqrt e}=
 \sqrt{2\pi}\int
 \{\sqrt U\,\mathbf1_{U<1}+\sqrt L\,\mathbf1_{L>1}\}\,d\eta.
                                                               \tag{21}
\]

Thus approaching even `2/sqrt(e)` requires a policy whose terminal
intervals straddle one up to vanishing **weighted** error. It does
not suffice that an unweighted exceptional probability tends to zero.

### Vanishing-volume omissions do not remove the barrier

Suppose a subfamily of terminal rectangles is retained, losing a fraction
`delta` of the target volume. Its auxiliary radius-square density is a
subdensity `g_ret<=g`, with `integral(g-g_ret)=delta`. Apply the interval
inequality above to the retained family and average thresholds over
`[1-epsilon,1+epsilon]`, for `0<epsilon<1/2`. The lost first term is at
most `sqrt(1+epsilon) delta/(2 epsilon)`; the lost integral term is at
most `delta/(2 sqrt(1-epsilon))`. The full averaged lower bound differs
from `2/sqrt(e)` by `O(epsilon^2)`. Taking `epsilon=delta^{1/3}` for
small positive `delta` gives

\[
 C_{\rm retained}\ge {2\over\sqrt e}
                -O(\epsilon^2+\delta/\epsilon+\delta)
           \ge {2\over\sqrt e}-O(\delta^{2/3}).       \tag{21a}
\]

Thus deleting only a vanishing density of designated terminal families
does not produce a near-width density-one input either. This statement
does not count extra targets obtained from new intervals crossing
several terminal boundaries; exploiting those would leave the present
paired-rectangle coverage ledger.

For arbitrary block-size-dependent policies and retained families, the
finite-transfer justification is the exact rank-inventory and squared-interval
mixture proof in the master's Appendix A.6. The preceding fixed-policy
continuum approximation alone is not a uniform transfer argument.

### Sharpness of the relaxed bound, not a construction

Let `alpha(du)=g'(u)du` on `(0,1)` and
`beta(dv)=-g'(v)dv` on `(1,infinity)`. Both have mass `g(1)`.
Any coupling `eta` of these measures satisfies
`g(s)=integral 1_{u<s<v} d eta`. Moreover
`(v-u)d eta` is a probability measure, and all its intervals straddle
one. Set `A=sqrt(d)*(sqrt(v)+sqrt(u))/2`,
`B=sqrt(d)*(sqrt(v)-sqrt(u))/2`.
This realizes equality in the relaxed rank-law problem.

It is not a proof that this interval coupling comes from recursive SCD
regrouping of the actual signed chain tuples. That realizability problem
is an additional open constraint. In particular it supplies no
`2/sqrt(e)` full-cube upper bound, much less coefficient one.

## 7. The optimal recursive constants have a limit

Merge fixed disjoint groups of `m` initial inputs into single factors.
The radius kernel and Gaussian closure make the resulting radii
independent `sqrt(m) chi_3` variables. Follow an optimal `q`-factor
policy on `q` such groups. Homogeneity gives

\[
                         R_{mq}\le R_q.              \tag{22}
\]

More generally, divide `d` inputs into `q` groups of sizes `n_i` differing
by at most one. Their radii are independent `sqrt(n_i)Z_i`. Therefore

\[
 R_d\le{1\over2}\sqrt{\pi/2}\,
       \mathbb E T_q(\sqrt{n_1/d}Z_1,\ldots,\sqrt{n_q/d}Z_q).
\]

For fixed `q`, continuity, homogeneity and
`T_q<=sum_i 1/x_i` justify dominated convergence as `d->infinity`.
The right side tends to `R_q`. Thus
`limsup_d R_d<=inf_q R_q`, while the reverse liminf inequality is
tautological. This proves the limit assertion in (2).

Every one-step strategy is a recursive strategy, so `R_4<=c_4` from
the preceding construction. Together with (20), this proves both bounds
in (2). The exact value of the infimum is not evaluated here.

For completeness, the limiting coefficient is an actual asymptotic
compiler upper bound, not just a collection of unrelated fixed-d limits.
For each fixed `d`, take `h` sufficiently large to control (4)--(6) and
the fixed-d SCD/Riemann-sum approximation. Choose `d=d(k)` increasing
slowly enough that all these errors tend to zero and `h=floor(k/d)`
tends to infinity. Fewer than `d=o(k)` top-bit lifts interpolate from
`dh` to `k`, costing a relative `1+o(1)`. This yields
`nu(k)<=(R_*+o(1))W(k)`, but (20) prevents this route from reaching one.

## 8. A proved benefit of adaptive reassociation

For five equal continuum lengths equal to one, the best one-step split
is `1+4`, with main cost `1+2/3=5/3`. The `2+3` split costs `1+3/4=7/4`.

Instead merge the first two factors and let the child length be `r`.
Among the remaining four factors, isolate the longest and product-SCD
the other three. The terminal expected reciprocal cost for that state is

\[
 T^{\rm policy}_4(r,1,1,1)=
 \begin{cases}2-r/4,&0<r\le1,\\1/r+3/4,&1\le r<2.\end{cases}
\]

Integrating against `K(1,1;dr)=r dr/2` gives

\[
 {1\over2}\int_0^1r(2-r/4)\,dr+
 {1\over2}\int_1^2r(1/r+3/4)\,dr
              ={73\over48}<{5\over3}.              \tag{23}
\]

For actual chain lengths all equal to `L`, the corresponding principal
costs divided by `L^4` converge to these two values. All required leaf
cycles can be globally Euler-assembled by Section 2, so this is a
literal constructive saving, not an uncharged cut comparison.

The functions involved are continuous on positive length tuples.
Consequently the saving remains strict on an open neighborhood of the
equal-length tuple. The initial Rayleigh law gives that neighborhood
positive measure. Since recursion is nowhere worse than a one-step
split, this proves the strict averaged inequality

\[
                            R_5<C_5^{\rm one}.       \tag{24}
\]

No uncertified decimal for either side is claimed.

## 9. Reproducible finite checks

Run `python3 scratch/recursive_scd_coalescent_20260905_f6b82.py`.
It verifies:

- Six globally Euler-assembled recursive full-cube words, through 12
  coordinates, including every literal interval union.
- Disjointness and completeness of the terminal signed-family partition.
- Equality of the dynamic-programming main cost and the actual sum of
  leaf chain lengths, plus every primary and cut position in (4).
- 1,600 exact volume and energy identities for the merge lengths (3).
- 1,344 adaptive final-chain histograms against complete rank polynomials.
- The five-equal-chain improvement at `L=2,4,8,16,32,64`.

The finite histograms corroborate the adaptive rank-law invariant. The
large-d assertions (1), (2), and (20) are proved analytically above;
none is inferred from simulation or these finite examples.

The remaining coefficient-one gap is structural: further progress must
leave the centered paired-rectangle bridge ledger, rather than merely
optimize its partitions or its SCD reassociation tree.
