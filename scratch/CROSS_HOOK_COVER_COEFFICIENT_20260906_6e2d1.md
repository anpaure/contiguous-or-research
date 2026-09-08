# An Overlapping Cross-Hook Cover With Coefficient Below 1.245

Date: 2026-09-06. New scratch work only; no master or existing research files
were changed.

## 1. Theorem

Write `W(k)=binom(k,floor(k/2))`. There is a deterministic construction of
nonempty set-valued words realizing every nonempty subset such that

\[
 \boxed{\nu(k)\le(c_4-\Delta_H+o(1))W(k)
                  <(1.245+o(1))W(k),}                 \tag{1}
\]

where the exact-arithmetic certificate below gives

\[
 \boxed{\Delta_H={453819283540955815\over18446744073709551616}
             >{49\over2000}=0.0245.}                 \tag{2}
\]

Here `c_4` is the four-block constant in `../MASTER_HANDOFF.md`, Appendix A.5.
Using its **certified** bound `c_4<1.26947180564`, not the informal
approximation `1.26734...`, the upper endpoint in (1) is in fact below

\[
                         1.244870213.                \tag{3}
\]

The word construction and its limiting integral are proved analytically.
The numerical inequality (2) is computer-assisted, using an integer-only
finite certificate with proved lower bounds on each integration cell.

The mechanism is **overlapping covers rather than partitions**. Two products
of L-shaped chain families cover a four-chain box. Their overlap is confined
to its all-low and all-high threshold subboxes. Each L-shaped family has an
explicit minimum chain cover, so both product families compile into literal
interval-union words with fully charged joins.

For four equal chain lengths `2m`, the new principal charge is `12m^3`, versus
the existing four-block charge `14m^3`. Thus the local saving is leading-order,
not a saved endpoint letter. Optimizing the cuts adapts this benefit to the
nonuniform chain lengths occurring in the Boolean cube.

Coefficient one is **not** proved. These are universal words of a smaller
constant multiple of width, not width-length words with vanishing hole density.

## 2. A Minimum Chain Cover of a Hook

For integers `a,b>=1`, `0<=u<=a`, and `0<=v<=b`, define

\[
 H(a,b;u,v)=\{(x,y):0\le x<a,\ 0\le y<b,
                         \ x\ge u\ \hbox{or}\ y<v\}.
\]

Its volume and width are exactly

\[
 V(a,b;u,v)=ab-u(b-v),\qquad
 w(a,b;u,v)=\max\{\min(a,v),\min(a-u,b)\}.             \tag{4}
\]

**Width proof.** The hook is the union of the bottom strip
`[0,a) x [0,v)` and the right strip `[u,a) x [0,b)`. A point in the bottom
strip but not the right strip is strictly below every point in the right
strip but not the bottom strip. Therefore an antichain lies entirely in one
of the two strips. Their widths are `min(a,v)` and `min(a-u,b)`, and each
width is attained within its strip. This proves (4), including empty strips.

There is an elementary deterministic chain-cover algorithm attaining this
width. Process the points in increasing `x`, and then increasing `y` within
each column. Append a point to a chain whose last `y` is the largest value
not exceeding its `y`; create a chain if none is eligible. Break ties by
earliest chain creation.

For completeness, the chains' last `y` values stay in nonincreasing order of
creation. A point assigned to chain number `j>1` has a preceding last point
on chain `j-1` with strictly greater `y`. Induction records a decreasing-`y`
subsequence of length `j` ending at this point. Its `x` values are strictly
increasing: two points of the same column were processed in increasing `y`.
It is consequently an antichain. Opening `r` chains certifies an antichain of
size `r`, proving optimality without invoking an unproved matching claim.

If the two coordinate axes are actual ascending set chains on disjoint
supports, send `(x,y)` to the union of their indexed members. This is an
injective order embedding. The algorithm therefore supplies exactly `w`
actual set chains, with total membership `V`. Saturation of the resulting
chains is not needed anywhere below.

## 3. Two Cross-Split Products Cover the Whole Box

Take four ascending set chains `C_i` on disjoint supports `U_i`, with lengths
`a_i`. Choose integer cuts `u_i` between `0` and `a_i`. For a point of the
product box, let

\[
                  b_i=\mathbf1_{\{x_i\ge u_i\}}.
\]

Choose a cyclic ordering of the four factors and, for notation, call it
`0,1,2,3`. The following two families cover the entire product:

\[
 \begin{split}
 \mathcal F_0&=H(a_0,a_1;u_0,u_1)\times
                         H(a_2,a_3;u_2,u_3),\\
 \mathcal F_1&=H(a_1,a_2;u_1,u_2)\times
                         H(a_3,a_0;u_3,u_0).
 \end{split}                                                     \tag{5}
\]

Indeed the first condition is `b_0>=b_1` and `b_2>=b_3`; the second is
`b_1>=b_2` and `b_3>=b_0`. Failure of both would require a strict binary
increase on an edge from each of the two perfect matchings of the four-cycle.
Those two edges are adjacent, which would require three strictly increasing
binary values. This is impossible.

Both conditions hold precisely when all four bits agree. Thus the overlap
has the exact size

\[
               |\mathcal F_0\cap\mathcal F_1|
                 =\prod_i u_i+\prod_i(a_i-u_i).         \tag{6}
\]

This proves coverage of the **actual set supports**, not just of their ranks.
It holds for every choice of cuts, including boundary cuts.

For the four directed edges of the chosen cycle, abbreviate

\[
 V_i=a_i a_{i+1}-u_i(a_{i+1}-u_{i+1}),\qquad
 w_i=\max\{\min(a_i,u_{i+1}),\min(a_i-u_i,a_{i+1})\},   \tag{7}
\]

with cyclic indices. The principal paired-cover charge is

\[
 \boxed{Q(\mathbf a,\mathbf u)
        =V_0w_2+V_2w_0+V_1w_3+V_3w_1.}               \tag{8}
\]

The next section proves that this is a genuine word charge up to lower-order
terms. No partition claim is made for (5).

Only three cyclic orders need to be searched. Rotation leaves (8) unchanged;
reversing a cycle and replacing every cut `u_i` by `a_i-u_i` also preserves
its four volumes and widths, with their edge directions reversed.

## 4. Literal Compilation and Every Join

For any strict ascending set chain `E=(E_0,...,E_{r-1})` on support `U`, use

\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
            E_{r-1}\setminus E_{r-2},U\setminus E_{r-1}),           \tag{9}
\]

deleting empty letters. Every `E_i` is a prefix union and `U\E_i` is a suffix
union. Its length is at most `r+1`, even for nonsaturated chains.

Suppose a family on `U` has a chain partition `C_1,...,C_r`, with total
membership `V`, and a family on the disjoint support `U^c` has a chain
partition `D_1,...,D_s`, with total membership `Z`. For each `C`, output

\[
 \beta_U(C),\beta_{U^c}(D_1^c),\beta_U(C),\ldots,
                  \beta_{U^c}(D_s^c),\beta_U(C),        \tag{10}
\]

where `D_j^c` is the reversed complemented chain, in ascending order.

A suffix of a `D_j^c` bridge followed by a prefix of the next `C` bridge
realizes every `X union Y`, `X in C`, `Y in D_j`. The preceding boundary
realizes its full complement. These are contiguous intervals. An empty
prefix or suffix is allowed as one part of a witness; a nonempty target has
at least one nonempty part. Deleting empty letters preserves that interval.

Summing the lengths of the row words (10) gives the exact upper ledger

\[
             |A|\le Vs+Zr+V+2rs+r.                  \tag{11}
\]

In particular the closing `C` bridge is charged once per row. We do **not**
separately cut and close every terminal two-bridge rectangle.

Apply (11) to the two products in (5), and concatenate the resulting words.
With `L=sum_i a_i`, their total length is at most

\[
                   Q(\mathbf a,\mathbf u)+L^2+L+1.   \tag{12}
\]

For example, each `w_i<=min(a_i,a_{i+1})`; hence
`w_0w_2,w_1w_3<=L^2/16`, while
`V_0+V_1<=a_1(a_0+a_2)<=L^2/4` and `w_0+w_1<=L`.
These bounds already give the smaller overhead `L^2/2+L` in this orientation.
Formula (12) is a convenient common bound including the old construction.

Every asserted witness stays in its own row. Arbitrary additional intervals
across row or family joins can only help.

For `a_i=2m,u_i=m`, each hook has volume `3m^2` and width `m`. Thus

\[
 Q=12m^3,\qquad |A|\le12m^3+10m^2+2m.              \tag{13}
\]

The old isolated-longest-factor charge is exactly `14m^3`. Equation (13) is
an unconditional, scalable local improvement with literal witnesses.

## 5. Boolean-Cube Assembly and Limit

Use the same initial ownership partition as Master A.5: split `4h`
coordinates into four `h`-sets, choose one pivot in each, and take a Boolean
SCD on each block minus its pivot. For each tuple of SCD chains, take the
eight sign vectors with first sign positive. A negative factor is its
reversed blockwise complement. Pair each signed product with its full
complement.

These paired products partition the Boolean cube. The first pivot chooses
the global complement, the remaining pivots choose the signs, and unique
SCD ownership chooses the four chains. Inside each paired product replace
the partition compiler by the overlapping cover (5) when beneficial.

Here is an exact finite decision rule. For sorted lengths `a<=b<=c<=d`, put

\[
 B_4(a,b,c,d)=ab(c+d)-d\left\lfloor{(a+b-c)_+^2\over4}\right\rfloor.
                                                               \tag{14}
\]

Let `H_Z(a)` be the minimum of (8) over all integer cuts and cyclic orders,
and put `J(a)=min(B_4(a),H_Z(a))`. The old word has length at most
`B_4+2w_3+d+1`, where `w_3=ab-floor((a+b-c)_+^2/4)`; this also obeys the
overhead in (12). Finite enumeration with lexicographic ties, followed by
the greedy hook chain cover, is a deterministic construction. It gives

\[
 \boxed{\nu(4h)\le
    8\sum_{\text{four SCD chains}}\{J(\mathbf a)+L^2+L+1\}.}       \tag{15}
\]

The standard SCD inventory used in Master A.5 is
`binom(n,i)-binom(n,i-1)` chains starting at rank `i`. Consequently a uniformly
sampled chain length, divided by `sqrt(h)`, converges to a standard Rayleigh
variable of density `x exp(-x^2/2)`, with uniform Gaussian tails and convergence
of every fixed polynomial moment.

Extend (7)-(8) to real lengths and real cuts. Let `H(x)` minimize `Q` over
the compact parameter set `u_i=theta_i x_i`, `0<=theta_i<=1`, and cyclic
orders. Define

\[
 P_4(a,b,c,d)=ab(c+d)-{d\over4}(a+b-c)_+^2
       \quad(a\le b\le c\le d),\qquad
 P_H(\mathbf x)=\min\{P_4(\mathbf x),H(\mathbf x)\}.                \tag{16}
\]

These are continuous, homogeneous degree-three functions. Integer rounding
of four cuts changes the charge by `O(L^2)`, uniformly: volumes change by
`O(L)`, widths by `O(1)`, and (8) contains only four terms. Thus the finite
minimum in (15), scaled by `h^(3/2)`, converges to (16). The bound
`0<=J<=B_4<=L^3` and the SCD moment bounds justify expectation convergence.

The tuple prefactor is

\[
 {8W(h-1)^4h^{3/2}\over W(4h)}\longrightarrow(2/\pi)^{3/2}.
\]

The entire overhead in (15) is `O(W(4h)/sqrt(h))`. Therefore, for four
independent standard Rayleigh variables,

\[
 \nu(4h)\le(c_H+o(1))W(4h),\qquad
 c_H=(2/\pi)^{3/2}\mathbb E P_H(X_1,X_2,X_3,X_4).                  \tag{17}
\]

At most three ordinary top-bit splices handle every dimension. Their width
correction `2^(k-4h)W(4h)/W(k)` tends to one, so (17) holds for all `k`.

This proves the construction without any packet selection, Bellman recursion,
unproved chain packing, or inference from a fixed finite optimal word.

## 6. Exact Certificate for the Saving

Let `Delta_*=c_4-c_H`. Integrate the largest Rayleigh length radially and write
the other three as its ratios `0<x<y<z<1`. Since
`integral_0^infinity r^10 exp(-q r^2/2) dr=945 sqrt(pi/2) q^(-11/2)`,

\[
 \Delta_*={45360\over\pi}\int_{0<x<y<z<1}
 {xyz\,[P_4(x,y,z,1)-H(x,y,z,1)]_+
       \over(1+x^2+y^2+z^2)^{11/2}}\,dx\,dy\,dz.                  \tag{18}
\]

The certificate lower-bounds (18), not a sampled average. It need not find
the global optimal thresholds: any validated feasible cuts provide a lower
bound for the saving after taking the positive part.

### 6.1 An Explicit Candidate Menu

In a chosen cyclic order write the lengths as `a,b,c,d`, and put

\[
 p=b-a,\quad q=c-b+a,\quad \delta=d-q,\quad\eta=\delta_+.
\]

Use cuts

\[
             (u_0,u_1,u_2,u_3)=(t,a-t,p+t,q-t).       \tag{19}
\]

For

\[
 \max(0,a-b,-\delta)\le t\le
    \min\{a,q,(\delta\ge0\ ?\ a:d)-\eta\},           \tag{20}
\]

these are feasible and the four widths are
`a-t,p+t,q-t,t+eta`. Thus three successive widths are balanced exactly.
Substitution in (8) makes its dependence on `t` quadratic, with coefficients

\[
 A=\min(a+c,b+d),\qquad
 B=(b-d)(c-a)+(p-a)\delta-2aq+(a+q)\eta.              \tag{21}
\]

The unconstrained minimizer is `-B/(2A)`. The certificate clamps it to (20)
at the cell midpoint, rounds `K*t/a` to its nearest integer, and tests that
multiple of `a/K` and its two neighbors. It also tests the six affine boundary
choices in (20). It tries the four rotations of each of
`(0,1,2,3)`, `(0,1,3,2)`, `(0,2,1,3)`.

All midpoint choices, comparisons, and tie decisions are made with integers.
Every selected `t` is a rational affine function of the four lengths. Its
feasibility and the sign of `delta` are checked at all eight corners of the
cell. Since these conditions are affine, they then hold throughout the cell.

### 6.2 A Cell Lower Bound

Use the disjoint cells

\[
 x={i+s\over N},\quad y={j+t\over N},\quad z={l+v\over N},
 \qquad0\le s,t,v\le1,\qquad0\le i<j<l<N.             \tag{22}
\]

The omitted diagonal slabs have nonnegative saving. For one validated
candidate, expand an integer polynomial `R(s,t,v)` of total degree at most
three such that

\[
 0\le {R\over4K^3N^3}\le[P_4-H]_+.                 \tag{23}
\]

Here `4K^3` clears the denominators of (19) and (8). For the baseline's
positive part, if `x+y-z` is nonpositive throughout the cell, use zero;
otherwise subtract its full square. This only decreases the baseline, even
when the cell crosses the breakpoint. Write `R=sum_alpha c_alpha s^alpha`.
The certificate accepts the cell only if

\[
                   c_0+\sum_{\alpha\ne0}\min(c_\alpha,0)\ge0.     \tag{24}
\]

This proves the first inequality in (23) everywhere, because all local
monomials lie in `[0,1]`. The second follows from the feasible literal cover.

Define the integer

\[
 T=\sum_\alpha c_\alpha\,2160
       \prod_{r=1}^3
       {i_r(\alpha_r+2)+\alpha_r+1
                 \over(\alpha_r+1)(\alpha_r+2)},\quad(i_1,i_2,i_3)=(i,j,l).
                                                               \tag{25}
\]

The denominator product divides `2160` whenever `sum alpha_r<=3`. Equation
(25) integrates `(i+s)(j+t)(l+v)R` exactly and multiplies the result by 2160.
In particular `T>=0` on an accepted cell.

Put

\[
 S=N^2+(i+1)^2+(j+1)^2+(l+1)^2,\qquad R_S=\lceil\sqrt S\rceil.
\]

Using `pi<22/7` and the maximum denominator on the cell, its contribution
to (18) is at least

\[
 {45360\cdot7\,T N^2
   \over22\cdot4K^3\cdot2160\,S^5 R_S}.              \tag{26}
\]

This includes all Jacobians and the radial normalization. The square-root
rounding is checked by integer comparisons. Round (26) downward to a multiple
of `2^(-64)` by binary integer division, and add the results. Rejected cells
contribute zero. There is no quadrature-error estimate or floating-point
rounding assumption in this lower certificate.

### 6.3 Verified Output

For `N=192,K=16`, the checker visits exactly 1,161,280 cells. It finds 864,880
with a feasible candidate, and 745,125 pass (24). The integer sum is

\[
                    453819283540955815.
\]

Thus (18) is at least (2). The program asserts the rational inequality
`2000*sum > 49*2^64`. Smaller runs independently give lower bounds
`0.0214413917177...` at `N=64,K=32` and `0.0239054608386...` at `N=128,K=32`.

All polynomial coefficients and moments use signed 128-bit integers. For
the stated parameter range, crude coefficient and moment bounds are below
`10^33`, well inside their range. Every multiplication used to form (26) is
explicitly overflow-checked in unsigned 128-bit arithmetic. The division also
checks that doubling its remainder is safe. Assertions are enabled.

Equations (17)-(18), this finite certificate, and the retained certified upper
bound for `c_4` prove (1)-(3).

## 7. Reproduction and Independent Checks

Run from the repository root, choosing an executable path in the temporary
directory. No solver or third-party Python package is needed for these checks.

```sh
python3 -B scratch/cross_hook_cover_20260906_6e2d1.py
clang++ -std=c++17 -O2 -Wall -Wextra -pedantic \
  scratch/cross_hook_certificate_20260906_6e2d1.cpp \
  -o /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/cross_hook_certificate_20260906_6e2d1
/var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/cross_hook_certificate_20260906_6e2d1 192 16
python3 -B scratch/cross_hook_independent_check_20260906_6e2d1.py \
  /var/folders/sw/_lc6g7h504j22_c4pzb7ccd80000gp/T/opencode/cross_hook_certificate_20260906_6e2d1 \
  --samples 240
```

Observed checks:

- 1,936 exact hook chain covers, including degenerate cuts.
- 297 literal paired-box words with every required set checked by actual
  interval unions.
- Equal-side words at side lengths 2, 4, 6, and 10, with principal charges
  12, 96, 324, and 1500, respectively.
- Full-cube assembly in dimensions 8, 12, and 16, covering exactly 255, 4095,
  and 65535 nonempty targets. These are compiler regressions, not finite
  optimum improvements.
- The complete integer certificate at `N=192,K=16`.
- 143 independently integrated certificate cells, using Python `Fraction`
  arithmetic and tensor Boole quadrature. This entails 17,875 exact comparisons
  between the displayed polynomial and the independently evaluated hook cost.
  Boole quadrature is exact here because each separate variable has degree at
  most four after multiplication by `xyz`. All cell moments and downward
  rounding quotients agreed.
- An undefined-behavior-sanitized certificate run at `N=48,K=16` passed.

The optional `--samples ... --balanced` mode of the word checker samples the
twelve balanced-cut policies. It is **not** part of the certificate. A
500,000-sample diagnostic found a paired mean saving about `0.02663` over the
old construction, suggesting an attainable coefficient near `1.241`. Neither
this decimal nor optimality of that menu is asserted by the theorem.

## 8. Why the Existing Obstructions Do Not Apply

The following cautions were checked before pursuing the construction:

- Master 3.5A and the density-bridge note: fixed full-half words cannot gain
  a leading density of targets from intervals crossing two bridge boundaries.
- Master A.6 and `MULTIBLOCK_PARTITION_BARRIER_20260906_8b47c.md`: centered
  partitions and arbitrary moving-center saturated partitions have positive
  ledger gaps above one.
- The moving-center note's explicit warning: its signed dual cannot be applied
  to covers with nonvanishing excess volume.
- The three-box endpoint/precedence notes: unordered chain partitions or
  rank-profile feasibility are not by themselves interval realizations.

The new cover intentionally uses the third distinction. At equal cuts, (6)
is one eighth of the product's volume. This is a leading excess volume, not
an error term that may be discarded. The two families also use different
support splits. All promised targets are realized by the explicit boundaries
in (10), so no multi-boundary or endpoint-pinning hypothesis is being assumed.

The initial attempt to find a better **partition** of a three-chain grid did
not produce an improvement. Its exploratory LP/MILP driver is preserved as
`ribbon_grid_experiment_20260906_6e2d1.py`; its fractional values and solver
nonexistence diagnostics are not premises of this theorem. The successful
four-chain mechanism instead permits overlap from the outset.

The remaining target is still to lower the coefficient to one. Nothing in
this note proves that iterating the four-hook cover does so, or supplies
near-width words with `o(2^k)` holes. What is established is the unconditional
full-cube constant improvement (1), with a concrete new covering mechanism.

## 9. Side Result: Nonsaturation Alone Does Not Fix Partitions

This result was obtained before finding the overlapping cover and is separate
from its upper-bound proof. It strengthens the scope of the previous cautions.

Suppose a Boolean-cube partition consists of paired products of two arbitrary
strict set chains on complementary supports. Rank gaps, support splits, and
rank centers may all vary. Charge `a+b` for a pair of chain lengths `a,b`, and
let `M` be the total. Then, for every integer rank `r`,

\[
 \boxed{2M\ge3\binom{k}{r}-\binom{k}{3r-k},\qquad
        {M\over W(k)}\ge {4\over3^{9/8}}-o(1)
                         =1.1622473904\ldots-o(1).}   \tag{27}
\]

Binomial coefficients outside ranks `0,...,k` are interpreted as zero.

To prove it, for one pair let
`A={2|X|:X in C}` and `B={k-2|Y|:Y in D}`. Put

\[
 G(t)=|A\cap(B+t)|+|B\cap(A+t)|,\qquad
 D(t)=|A\triangle(B+t)|+|B\triangle(A+t)|.
\]

With `m=|A|+|B|`, one has `D(t)=2m-2G(t)`. Three applications of the
symmetric-difference triangle inequality, along
`A,B+t,A+2t,B+3t` and its exchanged version, give `D(3t)<=3D(t)`. Hence
`3G(t)-G(3t)<=2m`. At `t=2r-k`, `G(t)` is exactly the pair's rank-`r`
profile, and `G(3t)` is its rank-`3r-k` profile. Summing the partition identity
proves the finite inequality in (27), for both parities of `k`.

Take `r=k/2+s sqrt(k)+O(1)` and maximize
`(3 exp(-2s^2)-exp(-18s^2))/2`. Its maximum occurs at
`s^2=log(3)/16` and is `4/3^(9/8)`. This proves the asymptotic assertion.

Equation (27) is not a lower bound for unrestricted words. In particular it
does not apply to the overlapping construction in Sections 2-6: the partition
identity used in its proof fails by precisely the excess volume (6).
