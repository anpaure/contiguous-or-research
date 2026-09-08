# Multiblock optimization, a strict improvement, and a moving-center barrier

Date: 2026-09-06. Supplemental research note. The upper improvement is now
incorporated in `../MASTER_HANDOFF.md`, Appendix A.5B, using a shorter exact
finite-saving proof and five unequal blocks. The other results remain here.

Inputs read: `FULL_CUBE_CROSS_SPLIT_GROUPED_CHAIN_BOUND_20260905_d29f6.md`,
Master A.5, the subsequently located
`GENERAL_D_BLOCK_AND_RECURSIVE_SCD_LIMITS_20260905_f6b82.md`, and Master A.6.
The latter two already prove the one-step and centered-recursion barriers.
Those results are identified as existing below, not claimed as new.

## 1. Results and scope

Write `W(k)=binom(k,floor(k/2))`. Coefficient one remains unproved.

The exact block optimizations have the following behavior.

1. **Existing, audited:** optimizing a two-support split separately for each
   maximal signed product gives constants `C_m` with `C_m -> sqrt(2)`.
   Isolating only the longest factor is worse: its constant diverges.
2. **Existing, audited:** adaptive centered product-SCD reassociation has
   exact Bellman constants `R_m`, with
   `R_m -> R_* = inf_{m>=2} R_m` and `R_* >= 2/sqrt(e)`.
   Master A.6 supplies a finite policy-uniform barrier, so a slowly growing
   number of blocks does not evade it.
3. **New refinement:** `R_4=c_4`, and the five-factor Bellman integrals can
   all be evaluated by the explicit rational formula in Section 4.
   Merging the two shortest factors is not always optimal, even in the
   continuum: `(2,2,3,3,3)` gives `37/64` versus `61/108`.
4. **New upper improvement:** a literal eight-block construction gives

   \[
   \nu(k)\le(c_4-\Delta+o(1))W(k),\qquad
   \Delta={181781e^{-4}\over28800000\pi^2}
              >{11\over10^6}.                         \tag{1}
   \]

   In particular the certified upper endpoint from A.5 implies a coefficient
   strictly below `1.26946080564`. The improvement is small but rigorous;
   no new numerical quadrature is used.
5. **New broader obstruction:** allow arbitrary partitions into paired
   products of two saturated set chains, with arbitrary support splits and
   arbitrary rank centers, and charge `a+b` for a pair with lengths `a,b`.
   If `M` is the total charge, then

   \[
   {M\over W(k)}\ge {3\over2^{4/3}}-o(1)
                         =1.1905507889\ldots-o(1).    \tag{2}
   \]

   There is an exact finite inequality proving this, independent of the
   number of blocks or pieces. Moving centers alone therefore do not make
   this paired-rectangle partition ledger achieve coefficient one.

Neither (2) nor the stronger centered barrier is a lower bound for
unrestricted interval-union words. They charge designated paired rectangles,
not arbitrary extra targets from longer intervals or a new mechanism sharing
leading-order positions between rectangle occurrences. Saturation of the
terminal chains is an explicit hypothesis of (2).

## 2. Exact compilers and limiting objectives

### 2.1 Finite objects

Split `k=mh` coordinates into pivoted blocks. In each block minus its pivot,
take a Boolean SCD. Choose one chain per block and one of `2^{m-1}` sign
vectors, fixing the first sign. A negative factor means blockwise complement
in ascending order. Pair the resulting product with its full complement.
The pairs partition the Boolean cube: the first pivot determines the global
complement, the remaining pivots determine the signs, and the SCDs determine
the owners.

For a chain `E` of length `a` on support `U`, use the bridge

\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
     E_{a-1}\setminus E_{a-2},U\setminus E_{a-1}),       \tag{3}
\]

deleting empty letters. Its prefixes give the chain members, and its suffixes
give their complements. Its length is at most `a+1`. A terminal paired
rectangle `(C,D)` on complementary supports is represented by the two directed
edges between bridge vertices `(U,C)` and `(U^c,D^c)`. The two directions
realize the two complementary target families across literal boundaries.

Collect all these edges globally. Output the bridges along an Euler circuit
in each component, including one closing copy of the starting bridge. If
`E` is the number of terminal paired rectangles and `V_cat` bounds the number
of bridge vertices, the actual word length `N` satisfies

\[
 M\le N\le M+2E+(k+1)V_{\rm cat},\qquad
 M=\sum_{\rm terminal}(a+b).                           \tag{4}
\]

The lower inequality uses the fixed pivots: every chain fixes at least one
pivot in its support, so it cannot contain both the empty and full sets, and
`|beta(E)|>=a`. This is not the same as paying for a separately cut three-bridge
word at every rectangle. That latter procedure can lose a leading constant.

For lengths `a,b`, a complete product SCD has chain lengths

\[
 |a-b|+1,\ |a-b|+3,\ldots,a+b-1.                      \tag{5}
\]

Consequently the exact optimal centered recursive charge for one initial
tuple satisfies

\[
 P_2(a,b)=a+b,\qquad
 P_m(\mathbf a)=\min_{i<j}
   \sum_{r=|a_i-a_j|+1,\;\mathrm{step}\;2}^{a_i+a_j-1}
       P_{m-1}(r,\mathbf a_{\setminus\{i,j\}}).        \tag{6}
\]

Choices at different children may differ. The full-cube main charge is
`2^{m-1} sum P_m`, over all initial SCD tuples.

### 2.2 Size bias is essential

A uniformly chosen Boolean SCD chain, divided by `sqrt(h)`, converges to a
standard Rayleigh variable `X`. Its Gaussian tail bounds imply convergence
of every fixed polynomial moment. Weighting a tuple by its product volume
changes each input to

\[
 Z\sim\chi_3,\qquad
 g_Z(z)=\sqrt{2/\pi}\,z^2e^{-z^2/2},\quad z>0.        \tag{7}
\]

The normalized cost must be averaged under (7), not under the Rayleigh law.
The volume-weighted limit of (5) is the probability kernel

\[
 K(a,b;dr)={r\over2ab}\mathbf1_{|a-b|<r<a+b}\,dr.     \tag{8}
\]

Define

\[
 T_2(a,b)=a^{-1}+b^{-1},\qquad
 T_m(\mathbf x)=\min_{i<j}\int
       T_{m-1}(r,\mathbf x_{\setminus\{i,j\}})K(x_i,x_j;dr).
                                                               \tag{9}
\]

Then the exact limiting optimal centered-recursion coefficient is

\[
 R_m=\sqrt{\pi m/8}\,\mathbb E T_m(Z_1,\ldots,Z_m).  \tag{10}
\]

Indeed, the signed-tuple prefactor under the Rayleigh law is
`(sqrt(m)/2)(2/pi)^((m-1)/2)`. Multiplying by the mean tuple volume
`(pi/2)^(m/2)` gives `sqrt(pi*m/8)`. Dividing the finite recurrence by tuple
volume makes its summands have weights `r/(ab)`, whose mesh-two Riemann sum
is (8).

For fixed `m`, `T_m` is continuous on the positive orthant, homogeneous of
degree `-1`, and at most `sum_i 1/x_i`. The unweighted bound is

\[
 P_m(\mathbf a)\le\Bigl(\prod_i a_i\Bigr)\sum_i a_i^{-1}.
                                                               \tag{11}
\]

This polynomial bound gives the needed moment domination. At a merge with
nearly zero child length, use the unweighted integrand `r T_{m-1}` and first
remove `0<r<epsilon`; (11) bounds that piece by a polynomial times `epsilon`.
Ordinary Riemann convergence applies on the remaining compact interval.
Induction proves the fixed-`m` limit without assuming a rate uniform in `m`.

### 2.3 One-step support partitions

For a nonempty index set `I`, let `rho_I(x)` be the density at zero of the
sum of independent uniforms of lengths `x_i`, centered at zero. Put
`V_I=prod_{i in I} a_i`, and let `w_I` be the central coefficient of
`prod_{i in I}(1+z+...+z^(a_i-1))`.

Completing SCDs separately on supports `I,J` gives the exact principal charge

\[
                 V_Iw_J+w_IV_J.                      \tag{12}
\]

Optimizing this split separately for every initial tuple gives

\[
 C_m=\sqrt{\pi m/8}\,\mathbb E
       \min_{\varnothing\ne I\subsetneq[m]}
                    \{\rho_I(Z)+\rho_{I^c}(Z)\}.      \tag{13}
\]

For `r=|I|>=2`, its continuous width has the explicit formula

\[
 \Bigl(\prod_{i\in I}x_i\Bigr)\rho_I(x)
 ={1\over(r-1)!}\sum_{A\subseteq I}(-1)^{|A|}
       \left[\tfrac12\sum_{i\in I}x_i-\sum_{i\in A}x_i\right]_+^{r-1}.
                                                               \tag{14}
\]

For `r=1` the width is one. The finite inclusion-exclusion formula uses
binomial coefficients of degree `r-1`; replacing them by their leading
polynomials costs `O_r((1+sum a_i)^(r-2))`. Thus integer floors and parity
do not change (13).

Every one-step split is an admissible recursion, so `R_m<=C_m`. Equality
does not hold in general.

## 3. What growing the number of blocks actually does

### 3.1 All one-step partitions tend to sqrt(2)

This is the existing result, with the uniformity issue made explicit.
For deterministic lengths put `S_I=sum_{i in I}x_i^2`. A symmetric unimodal
density of peak `H` and variance `S_I/12` satisfies

\[
                         \rho_I(0)\ge S_I^{-1/2}.     \tag{15}
\]

To see this, any density bounded by `H` has
`Pr(|Y|>t)>=max(1-2Ht,0)`, hence variance at least `1/(12H^2)`.

For independent inputs (7), with probability tending to one,

\[
 S_{[m]}=(3+o(1))m,\qquad \max_i Z_i=o(\sqrt m).      \tag{16}
\]

Uniformly over every subset with `S_I>=m/16`, the triangular-array CLT and
unimodality give

\[
 \rho_I(0)\ge(1-o(1))\sqrt{6/(\pi S_I)}.             \tag{17}
\]

No union bound over `2^m` subsets is needed. If uniformity failed, a sequence
of offending arrays would still have maximum summand divided by standard
deviation tending to zero. Its CLT follows from the expansion of `sin(t)/t`.
The central height dominates the average density on any fixed standardized
interval around zero. First take the CLT limit, then shrink that interval.
This proves (17) for every such sequence, a contradiction.

If a shore has `S_I<m/16`, (15) already makes its contribution to (13)
at least `sqrt(2*pi)>sqrt(2)`. Otherwise (17) on both shores and convexity of
`s^(-1/2)` give a uniform lower bound `sqrt(2)-o(1)` for the normalized cost.

For the matching upper bound, `Z` times an independent uniform on
`[-1/2,1/2]` is `N(0,1/4)`: use a coordinate of an isotropic Gaussian vector.
For a fixed shore of size `q`, therefore,

\[
 \mathbb E\rho_I(0)=\sqrt{2/(\pi q)}.
\]

A fixed balanced partition in (13) has coefficient

\[
 {\sqrt m\over2}
 \left(\lfloor m/2\rfloor^{-1/2}+\lceil m/2\rceil^{-1/2}\right)
                    \longrightarrow\sqrt2.          \tag{18}
\]

Thus `C_m -> sqrt(2)`. If only the largest factor is isolated, the objective
contains `1/max_i Z_i`; its coefficient is at least a constant times
`sqrt(m/log(m))`, and diverges.

The same argument applies to unequal limiting block proportions
`lambda_i`, with sum one, whenever `max lambda_i -> 0`. Replace the inputs
by `sqrt(lambda_i) Z_i` and the prefactor by `sqrt(pi/8)`. Their total squared
length tends to three and their maximum squared length tends to zero.
A deterministic partition balances the sums of the `lambda_i` within
`max lambda_i`. Keeping a few macroscopic blocks is a different regime;
the number of named blocks alone does not imply (18).

### 3.2 Centered recursion has a different, but still nonunit, limit

Kernel (8) is the radius of the sum of independently oriented vectors in
three dimensions. If `phi_a(t)=sin(at/2)/(at/2)`, then

\[
                    \phi_a(t)\phi_b(t)=\int\phi_r(t)K(a,b;dr).
                                                               \tag{19}
\]

The product of the current `phi` factors is consequently a bounded
martingale under any adaptive merging policy. After reducing `m` independent
inputs (7) to terminal `A,B` and making one last kernel merge to `R`,
`R/sqrt(m)` has law `chi_3`, independently of the policy. One way to justify
uniqueness is to differentiate the density of the centered-uniform mixture
`E[R^(-1) 1_{R>2|x|}]`.

Set `L=(A-B)^2/m`, `U=(A+B)^2/m`. Conditional on `A,B`, `R^2/m` is uniform
on `[L,U]`. If `eta` is the law of `[L,U]` weighted by `1/(U-L)`, then

\[
 g(s)={\sqrt s\,e^{-s/2}\over\sqrt{2\pi}}
       =\int\mathbf1_{L<s<U}\,d\eta,\qquad
 C=\sqrt{2\pi}\int\sqrt U\,d\eta.                    \tag{20}
\]

For any threshold `t>0`,

\[
 \sqrt U\ge \sqrt t\,\mathbf1_{L<t<U}
    +\tfrac12\int_t^\infty{\mathbf1_{L<s<U}\over\sqrt s}\,ds.
\]

Integrating gives `C>=(t+1)e^(-t/2)` at every threshold where the density
identity holds. Such thresholds have full measure; taking them to one
proves `R_m>=2/sqrt(e)` without an endpoint-atom assumption.

This has a finite, policy-uniform version. Put `n=k-m` and

\[
 c_n(r)=\binom n{(n-r+1)/2}-\binom n{(n-r-1)/2},
 \quad r>0,\quad r\equiv n+1\pmod2.
\]

Every fully completed adaptive refinement has `2^{m-1}` copies of this
chain-length inventory. A terminal rectangle's interval `((a-b)^2/n,
(a+b)^2/n)` is exactly partitioned by the intervals
`((r-1)^2/n,(r+1)^2/n)` of its children (5). Hence the full squared-radius
mixture is exactly

\[
 g_n(s)={n\over4\,2^n}\sum_r c_n(r)
          \mathbf1_{(r-1)^2/n<s<(r+1)^2/n}.            \tag{21}
\]

It is independent of every adaptive choice. Adjacent-binomial estimates
give essentially locally uniform convergence away from zero to (20), and a weighted
tail above `S` is at most `S^(-1/2)`. The threshold inequality therefore gives,
uniformly over all policies,

\[
 {M\over W(k)}\ge\sqrt{k/n}\left(2/\sqrt e-o_n(1)\right).        \tag{22}
\]

This also works for unequal block sizes, since their nonpivot dimensions
still sum to `n`. It closes the possible interchange-of-limits loophole.

Finally, merge `m` initial inputs into `q` fixed groups of nearly equal
sizes. Their radii are independent scaled `chi_3` variables. Homogeneity,
continuity, and `T_q<=sum 1/x_i` show
`limsup_{m->infty} R_m<=R_q` for every fixed `q`. Thus

\[
                  R_m\longrightarrow R_*:=\inf_{q\ge2}R_q.     \tag{23}
\]

These are the existing recursion limit and obstruction, not a new proof of
an unrestricted lower bound for `nu`.

## 4. Exact four- and five-factor optimizations

For sorted positive lengths `a<=b<=c`,

\[
 T_3(a,b,c)=1/b+1/c,\qquad
 \rho(a,b,c)=1/c-{(a+b-c)_+^2\over4abc}.              \tag{24}
\]

The first follows directly from `integral r^(-1) K(a,b;dr)=1/max(a,b)`.

For four factors, after the first merge the two untouched factors have
lengths `p<=q`. The three-factor optimum gives

\[
 \mathbb E T_3(R,p,q)=1/q+\mathbb E[1/\max(R,p)]
                       =1/q+\rho(a,b,p).             \tag{25}
\]

Thus the decision is equivalent to choosing the isolated factor `q`.
For sorted `a<=b<=c<=d`, a largest factor is optimal, and

\[
 T_4(a,b,c,d)=1/d+\rho(a,b,c).                         \tag{26}
\]

Here is an exchange proof. Write `F_x=1/x+rho(the other three)`. Comparing
`F_c` and `F_d` reduces to the fact that `(a+b-t)_+^2/t` is decreasing in `t`.
For `F_b-F_c`, put
`H(t)=(a+t-d)_+^2/(4adt)`, `b<=t<=c<=d`. Where active,

\[
 H'(t)={t^2-(d-a)^2\over4adt^2}\le {1\over2t^2}.
\]

Hence `F_b-F_c>= (1/b-1/c)/2>=0`. The smallest factor cannot be the larger
untouched factor in (25) unless there is a tie. Alternatively `F_a>=F_b`
follows by bounding the derivative of `(t+c-d)_+^2/(4cdt)` by `1/(4cd)`.
This proves (26). Every `F_x` is coordinatewise nonincreasing, because
central densities of uniform sums decrease when a side length increases.
Consequently `T_4=min_x F_x` is coordinatewise nonincreasing as well.

Multiplying (26) by `abcd` gives precisely the A.5 polynomial. Therefore

\[
                            R_4=C_4=c_4.             \tag{27}
\]

For five factors, choose a first pair `a,b` and sort the remaining lengths
as `c<=d<=e`. Put `l=|a-b|`, `u=a+b`, and

\[
 Q(s)={s^2\over2e}+{s^2\over2d}
       -{(s-d+c)_+^3-(s-c-d)_+^3\over12cd}.
\]

The exact value of this first decision followed by optimal four-factor
continuation is

\[
 \begin{split}
 B(a,b;c,d,e)={1\over2ab}\bigg\{&Q(\min(u,e))-Q(\min(l,e))\\
 &+\max(u,e)-\max(l,e)\\
 &+{\rho(c,d,e)\over2}
       [\max(u,e)^2-\max(l,e)^2]\bigg\}.              \tag{28}
 \end{split}
\]

Thus `T_5` is the minimum of the ten expressions (28), not merely the one
that merges the two shortest inputs. To verify the primitive, for `r<=e`,

\[
 rT_4(r,c,d,e)=r/e+{r\over d}
       -{(r-d+c)_+^2-(r-c-d)_+^2\over4cd}=Q'(r).
\]

For `r>=e`, it equals `1+r rho(c,d,e)`. This proves (28), including every
breakpoint. It is a rational expression on rational input lengths.

At five equal lengths, (28) is `73/48`. At `(2,2,3,3,3)`,

\[
 B(2,2;3,3,3)=37/64,\qquad
 B(2,3;2,3,3)=61/108<37/64.                           \tag{29}
\]

Taking the minimum in (28) shows the latter is optimal. The difference is
`23/1728`, so this is not an integer-floor or seam artifact. It persists on
an open set of continuum inputs. Equation (28), together with (10), is an
exact five-dimensional expectation for `R_5`; no uncertified decimal for
that expectation is used here.

## 5. A strict eight-block improvement over c_4

Start with eight independent inputs of law (7). Merge three predetermined
disjoint pairs. The resulting state consists of

\[
 A,B,C\ \hbox{independent with law }\sqrt2\,\chi_3,
 \qquad D,E\ \hbox{independent with law }\chi_3.       \tag{30}
\]

Equivalently, the same limiting construction can start directly with five
unequal blocks of sizes `2h,2h,2h,h,h`. The eight-equal-block description
also places the improvement inside the constants `R_m` of (10).

If we always merge `D,E` next and then use (26), all four radii have law
`sqrt(2) chi_3`. Their coefficient, with the eight-block normalization
`sqrt(pi)`, is exactly `c_4`.

Instead, on the event

\[
                  A,B,C\le1,\qquad D,E\ge2,           \tag{31}
\]

isolate `E` and product-SCD the other four factors. Its normalized cost is
`1/E+rho(A,B,C,D)<=1/E+1/D`. This is a one-step admissible refinement.
Outside (31), keep the baseline policy.

We next bound the saving without simulation. The baseline conditional cost
is at least `E T_4(R,1,1,1)`, with `R` of kernel law `K(D,E)`, by coordinatewise
monotonicity. Put

\[
 g(r)=T_4(r,1,1,1)=
 \begin{cases}2-r/4,&0<r\le1,\\3/4+1/r,&r\ge1.\end{cases}
\]

Since

\[
 \int_0^1 r\{3/4+1/r-g(r)\}\,dr
       =\int_0^1(1-5r/4+r^2/4)\,dr=11/24,
\]

and `integral 1/r K(D,E;dr)=1/max(D,E)`, the baseline is at least

\[
 3/4+1/\max(D,E)-{11\over48DE}.
\]

Subtract the alternative bound. On (31) the saving is at least

\[
 3/4-1/\min(D,E)-{11\over48DE}\ge {37\over192}.       \tag{32}
\]

All decisions are deterministic functions of the current chain lengths.
The event boundaries have zero limiting measure, so the finite recurrence
and the seam estimates in Section 8 implement this policy literally.

For the probability of (31), elementary estimates suffice:

\[
 p:=\Pr(\sqrt2\chi_3\le1)
 ={1\over2\sqrt\pi}\int_0^1x^2e^{-x^2/4}\,dx
 \ge {17\over120\sqrt\pi}.                           \tag{33}
\]

Here `e^(-x^2/4)>=1-x^2/4`. Also, if
`I(x)=integral_x^infty e^(-u^2/2) du`, integration by parts gives
`I(x)>=x e^(-x^2/2)/(x^2+1)`. Therefore

\[
 q:=\Pr(\chi_3\ge2)
 =\sqrt{2/\pi}\{2e^{-2}+I(2)\}
 \ge {12\over5}\sqrt{2/\pi}\,e^{-2}.                 \tag{34}
\]

Combining the normalization, (32), and independence in (30), the coefficient
improves by at least

\[
 \sqrt\pi\,{37\over192}p^3q^2
 \ge {181781e^{-4}\over28800000\pi^2}=\Delta.          \tag{35}
\]

For a completely rational comparison, `e<87/32`, `(87/32)^4<55`, and
`pi<22/7` imply

\[
 \Delta>{181781\over15840000000}>{11\over10^6}.        \tag{36}
\]

One may prove the bound on `e` by summing through `1/5!` and bounding the
remaining tail by `7/4320`. The identity
`integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7-pi > 0`, obtained by polynomial
division, proves the bound on `pi`. The integer comparisons in (36) are
checked in the accompanying script. Equations (4), (10), and (35) prove (1), and

\[
                  2/\sqrt e\le R_*\le R_8\le c_4-\Delta<c_4.
                                                               \tag{37}
\]

## 6. Arbitrary moving-center rectangle partitions still have a barrier

Here the centered-SCD assumption is dropped completely. Suppose the Boolean
cube is partitioned into paired families

\[
 \{X\cup Y:X\in C,Y\in D\},\qquad
 \{(X\cup Y)^c:X\in C,Y\in D\},                       \tag{38}
\]

where `C,D` are saturated chains on complementary supports. Supports may
vary between pairs, as may the rank centers. Let `a=|C|`, `b=|D|`, and charge
`a+b` for (38). Include the empty target only as bookkeeping, not as a
required nonempty witness. Let `M` be the sum of the charges.

Define the linear interpolation of the binomial rank counts by

\[
 F_k(x)=\sum_{j=0}^k\binom kj(1-|x-j|)_+.
\]

**Finite theorem.** For every real `t>0`, independently of all partitions,

\[
                 M\ge2F_k(k/2+t)-F_k(k/2+2t).         \tag{39}
\]

### Proof

For a rank profile from one rectangle put
`u=(a+b)/2`, `v=|a-b|/2`, and let `c` be its rank center relative to `k/2`.
Convolving its integer rank counts with `(1-|x|)_+` gives exactly

\[
 H_{c,u,v}(x)=(u-|x-c|)_+-(v-|x-c|)_+.               \tag{40}
\]

For example, jitter the rank in each chain independently by a uniform on
`[-1/2,1/2]`. Its consecutive rank atoms become an interval of length `a` or
`b`; their convolution is (40). Saturation is used exactly here.

For fixed `t>0`, define the even continuous piecewise-linear function

\[
 q_t(x)=
 \begin{cases}
 0,&|x|\le t,\\
 2(|x|-t),&t\le|x|\le2t,\\
 |x|,&|x|\ge2t.
 \end{cases}                                         \tag{41}
\]

It satisfies `0<=q_t(x)<=|x|`; on the nonnegative axis it is nondecreasing
and 2-Lipschitz. For every real `c` and `0<=v<=u`,

\[
 q_t(c-u)+q_t(c+u)-q_t(c-v)-q_t(c+v)\le2u.            \tag{42}
\]

By symmetry take `c>=0`. If `c<=u`, the two outer terms are at most
`|c-u|+|c+u|=2u`, and the inner terms are nonnegative. If `c>=u`, monotonicity
makes `q_t(c-u)-q_t(c-v)<=0`, while the other difference is at most
`2(u-v)<=2u`. This proves (42).

The distributional second derivative of (40) is

\[
 H''=\delta_{c-u}+\delta_{c+u}-\delta_{c-v}-\delta_{c+v}.
\]

Thus (42) says `integral q_t H'' <= a+b`. Add this inequality for both
members of every pair (38). The partition property gives their total
smoothed rank profile exactly `F_k(k/2+x)`, not merely a pointwise cover.
Their total charge is `2M`. Since

\[
 q_t''=2\delta_{-t}+2\delta_t-\delta_{-2t}-\delta_{2t},
\]

two integrations by parts, or just finite sums for piecewise-linear
functions, give

\[
 2M\ge4F_k(k/2+t)-2F_k(k/2+2t).
\]

Here `F_k(k/2+x)=F_k(k/2-x)`. This proves (39), with no continuum
approximation and no assumption on the number of rectangles.

For fixed `s>0`, adjacent-binomial estimates give

\[
 {F_k(k/2+s\sqrt k)\over W(k)}\longrightarrow e^{-2s^2}.
\]

Taking `t=s sqrt(k)` in (39) yields

\[
 \liminf {M\over W(k)}\ge2e^{-2s^2}-e^{-8s^2}.
\]

The maximum occurs at `s^2=log(2)/6`, and equals `3/2^(4/3)`. This proves
(2) with a policy-uniform error depending only on `k`.

If a subpartition omits designated volume fraction `delta`, average (39)
over `t/sqrt(k)` in a small interval around the maximizing `s`. The loss
from the positive rank evaluations is `O(delta/epsilon)`, whereas the
averaged full bound loses `O(epsilon^2)`. Choosing `epsilon=delta^(1/3)`
gives `M/W(k)>=3/2^(4/3)-O(delta^(2/3))-o(1)`. The identical argument handles
a full rectangle cover with vanishing excess volume. No separate selector
or arbitrary-word repair claim is involved.

The barrier also survives empty-head/tail deletion when pivots are not
assumed. In the ordinary Euler compiler each nonempty-support bridge has
at least one letter and at least `a-1` letters for a chain of length `a`.
At least one support of each pair is nonempty, so even if empty supports
are admitted, `N>=E` and `M<=N+2E<=3N`. If `N=O(W(k))`, discard pairs with
`a+b<L=k^(1/8)`. Their total designated volume is at most `E L^2/2`, hence
an `O(k^(-1/4))` fraction of the cube. The retained pair count is at most
`M/L=o(W(k))`. The retained-volume bound just proved and
`N>=M_ret-2E_ret` imply `N/W(k)>=3/2^(4/3)-o(1)`. A sequence not of order
`W(k)` needs no such argument. This corollary concerns the ordinary bridge
occurrence compiler, not a new leading-order sharing mechanism.

## 7. The rank-only moving-center limiting optimization

This distinguishes a relaxation from an actual partition construction.
Scale terminal side lengths and rank-center offsets by `sqrt(k)`. The
limiting full-cube rank density is

\[
                         f(x)=\sqrt{2/\pi}e^{-2x^2}.
\]

For any terminal law admitting this scaling, its volume-weighted distribution
`mu(dc,da,db)` is a probability measure, symmetric in `c`, and its exact
rank-only relaxation is

\[
 \begin{split}
 C_{\rm mov}:=\inf_\mu\;&\sqrt{\pi/8}
                  \int(a^{-1}+b^{-1})\,d\mu,\\
 \text{subject to }&
 f(x)=\int {H_{c,(a+b)/2,|a-b|/2}(x)\over ab}\,d\mu
                   \quad\hbox{for almost every }x.    \tag{43}
 \end{split}
\]

It is only a relaxation: rank profiles do not guarantee realizability by
partitions of the actual sets. The finite proof (39) does not require the
existence of a limiting `mu`, and therefore also handles degenerating or
block-size-dependent partitions.

The test (41) is a feasible dual certificate for (43). In particular

\[
                 {3\over2^{4/3}}\le C_{\rm mov}\le {2\over\sqrt e}.
                                                               \tag{44}
\]

For completeness, the upper endpoint is genuinely feasible for the rank
relaxation, not asserted for words. On the positive axis, `f''` is negative
on `(0,1/2)` and positive on `(1/2,infinity)`. Couple the equal-mass measures
`-f''(v) dv` on the first interval and `f''(u) du` on the second by any
positive measure `eta(du,dv)`. Then

\[
 f(x)=\int\{(u-|x|)_+-(v-|x|)_+\}\,d\eta.
\]

This follows by taking second derivatives and using decay at infinity.
Set `a=u+v`, `b=u-v`, `c=0`, and `dmu=(u^2-v^2)deta`. Its mass is one by
integrating the displayed density. Its objective is

\[
 2\sqrt{\pi/8}\int_{1/2}^\infty u f''(u)\,du
 =2\sqrt{\pi/8}\{f(1/2)-\tfrac12f'(1/2)\}
 =2/\sqrt e.
\]

The exact value of (43) is not determined here. Even its lower bound in
(44) rules out coefficient one for moving-center saturated-rectangle
partitions with the stated charge. Arbitrary overlapping covers with
nonvanishing excess volume cannot be substituted for partitions in (39):
the dual has negative rank coefficients. This is a real distinction, not
an omitted error term.

## 8. Discretization, seams, and all dimensions

Fix `m`. Use a deterministic hook SCD at every binary merge. A chain on a
proper support consisting of `r` original blocks belongs to the catalogue
of some ordered binary-tree SCD on that support. There are at most
`r! 4^(r-1)` such trees. For each tree, the initial signed partitions give
at most `2^(rh)` chains. Including complements and all proper supports gives
the coarse sufficient bound

\[
 V_{\rm cat}\le B_m2^{(m-1)h},\qquad B_m=2m!8^m.      \tag{45}
\]

External adaptive decisions do not enlarge this catalogue: they select
chains from these trees rather than creating new chains inside a fixed
tree's decomposition.

For one tuple, put `L=sum a_i`. Every merge has at most `L` children, so
there are at most `L^(m-2)` leaves. The SCD moment bounds give

\[
 E\le2^{m-1}\sum_{\rm tuples}L^{m-2}
       =O_m(2^{mh}/h)=O_m(W(mh)/\sqrt h).              \tag{46}
\]

Equations (4)-(46) show that all bridge endpoint letters and closing Euler
cuts are `o(W(mh))`. Together with the Riemann justification after (11),
they prove that the stated limiting coefficients are actual word bounds.
In particular, (35) is a fixed eight-block construction with fully paid cuts.

For arbitrary `k`, take `h=floor(k/m)` and use fewer than `m` ordinary
top-bit splices. The multiplicative width correction is

\[
 {2^{k-mh}W(mh)\over W(k)}
   =\sqrt{k/(mh)}\{1+O((mh)^{-1})\}=1+O_m(h^{-1}).    \tag{47}
\]

To realize (23) as an all-dimension word upper bound, choose thresholds
`K_m` so large that all fixed-`m` approximation and seam errors are at most
`1/m` whenever `k>=K_m`, and also require `K_m>=m^2`. Let `m(k)` grow only
when the next threshold is reached. Then `m(k)->infinity`, `m(k)=o(k)`, the
rounding/splice error tends to zero, and the coefficient tends to `R_*`.
No explicit arbitrary growth rate is claimed from fixed-`m` estimates.
The finite barriers (22) and (39) apply independently of that diagonal.

## 9. Verification and exact remaining blocker

Run:

```text
python3 -B scratch/multiblock_partition_20260906_8b47c.py
```

The independent checker uses integer or rational arithmetic for every
assertion. It checks 79,056 translated-rectangle dual inequalities, 25
nonsymmetric full-cube partition/rank identities, 330 four-factor exchange
instances, the exact five-factor values (29), and the rational comparison
in (36). Its displayed decimal for (2) is only a diagnostic.

The extended checker also passes 6,930 exact finite conditional-saving
inequalities and four literal five-block full-cube words, in dimensions
7, 13, 14, and 16. The first three exercise the switching branch; the last
has the prescribed sizes `(4,4,4,2,2)` and exercises the baseline. All
interval unions and the global Euler cost are checked. The integrated
A.5B proof establishes the saving for every real scale, including
`sqrt(h)` when `h` is not a square, independently of these finite tests.

Independent proof audits checked the new optimization, switch, and
moving-center arguments. The supplemental text was corrected to use
essential uniform convergence for the open-bin density and to allow
empty supports in the endpoint-deletion corollary. The integrated
compiler explicitly includes complements in its bridge catalogue.

The existing recursive compiler checker was also rerun with `-B`. It passed
all six literal full-cube word checks, 1,600 exact merge identities, and
1,344 adaptive completed-rank inventories. These are checks, not premises
of the limiting proofs.

The best rigorous conclusions of this investigation are (1), (2), (28),
and (37). Centered reassociation does not approach one, and arbitrary
moving-center partitions into saturated paired rectangles still do not
approach one under the same charge. A coefficient-one construction must
change more than the block count, support split, or rank center: for
example, it must exploit leading-order occurrence sharing not charged by
`sum(a+b)`, extra multi-boundary targets, nonsaturated terminal chains, or
a genuinely different covering representation. None of those missing
mechanisms is constructed here.
