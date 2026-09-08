# Full-cube cross-split constructions below sqrt(2)

Date: 2026-09-05. The compact self-contained proof and rational certificate
are incorporated in `MASTER_HANDOFF.md`, Appendix A.5. This note is supplemental.

## 1. Verified results

Let `W(k)=binom(k,floor(k/2))`. There is an explicit deterministic
construction of nonzero set-valued words covering every nonempty subset,
in every dimension, such that

\[
 \boxed{\nu(k)\le(c_4+o(1))W(k),\qquad c_4<1.27.}       \tag{1}
\]

The constant has the exact probabilistic definition

\[
 c_4=\left({2\over\pi}\right)^{3/2}
 \mathbb E\left[AB(C+D)-{D\over4}(A+B-C)_+^2\right],   \tag{2}
\]

where `A<=B<=C<=D` are the order statistics of four independent standard
Rayleigh variables, of density `x exp(-x^2/2)` on `x>0`.

An exact-rational midpoint certificate, including a proved integration
error bound, establishes

\[
             1.26521705312<c_4<1.26947180564<1.27.    \tag{3}
\]

Uncertified higher-resolution midpoint diagnostics suggest
`c_4=1.26734...`; the upper theorem uses (3), not this approximation.

A simpler three-block construction has the closed-form coefficient

\[
 \boxed{c_3={\sqrt3\over\pi}
  \left({1\over3}+{3\over\sqrt2}\arctan\sqrt2\right)
  =1.30106226544951\ldots<\sqrt2.}                   \tag{4}
\]

The route began as repair of whole omitted rectangles of the earlier
`0.841485...` density word. The grouped repair is in fact advantageous for
all rectangles, so the final full-cube constructions do not first build
and lift that density word. They use chain-dependent support splits and
charge every resulting physical position. They are not concatenations
of several full-cube words.

Coefficient one, or density amplification to one at the same width,
is not proved here. All factor dimensions tend to infinity; no inference
from a fixed finite seed is used.

## 2. A paired-family bridge compiler

Let disjoint nonempty coordinate sets `U,V` partition the active universe.
Let `D=(D_0<...<D_{d-1})` be an ascending saturated chain on `V`.
Let a family `F` of subsets of `U` have a partition into ascending
saturated chains `E_1,...,E_r`. Write `v=|F|=sum_j |E_j|`.

For an ascending chain `E` on `U`, define

\[
 \beta_U(E)=(E_0,E_1\setminus E_0,\ldots,
 E_{a-1}\setminus E_{a-2},U\setminus E_{a-1}),        \tag{5}
\]

deleting empty letters. Its length is at most `a+1`. Its prefixes
include every chain member, and its suffixes include their complements
in `U`. Empty prefixes/suffixes are permissible parts of a witness,
not nonempty witnesses of the empty target.

Write `D^c=(V\D_{d-1},...,V\D_0)` in ascending order, and output

\[
 \beta_V(D^c),\beta_U(E_1),\beta_V(D^c),\ldots,
              \beta_U(E_r),\beta_V(D^c).             \tag{6}
\]

This covers both families

\[
 \{X\cup Y:X\in F,Y\in D\},\qquad
 \{(U\setminus X)\cup(V\setminus Y):X\in F,Y\in D\}.              \tag{7}
\]

For the first target, use the suffix `Y` of the fixed bridge followed
immediately by the prefix `X` of its owning `E_j` bridge. For the second,
use the suffix `U\X` of that same `E_j` bridge followed by the prefix
`V\Y` of the next fixed bridge. These are literal contiguous intervals.
Every nonempty target has at least one nonempty part. Omitting empty
letters preserves the contiguity and union.

The exact upper length ledger is

\[
 \boxed{|(6)|\le v+(d+2)r+d+1.}                     \tag{8}
\]

Indeed the moving bridges cost at most `v+r`, and the `r+1` fixed
bridges cost at most `(r+1)(d+1)`. The final fixed bridge, often an
unaccounted cut cost in an informal product argument, is included.

The families in (7) need not partition their support cube. Extra interval
unions are harmless. Later uses concatenate many instances of (6), but
all witnesses asserted here remain inside their own instance.

## 3. Exact product-chain decompositions

For two chains with `a<=b` members, the product grid has a saturated SCD
with `a` chains. In index notation its chain `i`, `0<=i<a`, is

\[
 (0,i),(1,i),\ldots,(a-1-i,i),
          (a-1-i,i+1),\ldots,(a-1-i,b-1).            \tag{9}
\]

Its bottom and top ranks sum to `a+b-2`; the chains partition the grid.
Interchange the two factors if necessary. Applying this construction to
every pair of chains recursively gives an SCD of any finite product of
saturated chains. It works for set chains on disjoint supports because
the map from index tuples to unions is injective and preserves covers.

For three chains of lengths `a<=b<=c`, the number of SCD chains is

\[
 \boxed{w_3(a,b,c)=ab-
                 \left\lfloor{(a+b-c)_+^2\over4}\right\rfloor.}  \tag{10}
\]

Here is an exact middle-layer count. Put
`s=floor((a+b+c-3)/2)`. The middle coefficient counts pairs
`0<=i<a,0<=j<b` for which `s-c+1<=i+j<=s`. If `delta=a+b-c<=1`,
all `ab` pairs qualify. Otherwise the excluded lower and upper corners
are triangles. If `delta=2q`, their sizes are `q(q-1)/2` and
`q(q+1)/2`; if `delta=2q+1`, both have size `q(q+1)/2`.
The total exclusion is respectively `q^2` or `q(q+1)`, which is
`floor(delta^2/4)`. Since `c>=b`, these triangles fit within both side
lengths. Every symmetric chain meets the middle layer once, proving
(10).

The total membership of the product SCD is exactly `abc`.

## 4. A genuine four-block cross-split word

Fix `h>=2`. Split `4h` coordinates into four disjoint blocks
`U_1,...,U_4`, each of size `h`, and choose a pivot `z_i` in each block.
In each `2^{U_i\{z_i}}`, take the elementary Boolean SCD obtained by
repeated one-coordinate extension. Any SCD would give the same estimates.
Let

\[
                         L_h=W(h-1).
\]

For a tuple of chains `(C_1,...,C_4)`, consider eight sign vectors
`epsilon in {0,1}^4` with `epsilon_1=0`. Define the ascending chain

\[
 F_i=\begin{cases}
 C_i,&\epsilon_i=0,\\
 (U_i\setminus C_{i,\mathrm{top}},\ldots,
       U_i\setminus C_{i,\mathrm{bottom}}),&\epsilon_i=1.
 \end{cases}                                         \tag{11}
\]

The paired target families for this signed tuple are

\[
 \mathcal P=\{X_1\cup\cdots\cup X_4:X_i\in F_i\},
                         \qquad \mathcal P^c.       \tag{12}
\]

These paired families partition the entire Boolean cube. To check this,
replace a target by its full complement if necessary so that it omits
`z_1`. For each other block, its pivot determines whether that part is
an ordinary SCD member or the complement of one. Unique SCD ownership
then determines every `C_i` and every sign. Complementing back supplies
the other member of the paired family. Thus there are no missing target
classes hidden in the sign choice.

Sort the four chain lengths as `a<=b<=c<=d`. Choose a block of length `d`,
using the smallest block index in a tie, as the fixed support `V` in
Section 2. The other three blocks form `U`; take the product SCD of
their three chains from (11) as the family `F`. Equations (8)--(10)
give a literal word for (12) of length at most

\[
 abc+(d+2)w_3(a,b,c)+d+1.                             \tag{13}
\]

Concatenate these words over all chain tuples and all eight sign
vectors. The output is nonzero and full-cube universal, with the exact
finite upper bound

\[
 \boxed{\nu(4h)\le
 8\sum_{(C_1,C_2,C_3,C_4)}
 \{abc+(d+2)w_3(a,b,c)+d+1\}.}                       \tag{14}
\]

The support partition in (6) is chosen anew for each tuple: the block
whose chain is longest is isolated, and the other three supports are
merged. Moving bridges therefore contain mixed-support set-valued
letters relative to the original blocks. There is no global two-half
full-block decomposition to which the earlier `sqrt(2)` barrier applies.

This is cross-box position sharing inside a three-chain product SCD,
not three independently concatenated chain words. Each moving chain
bridge serves all `d` values of the fixed chain in each orientation.

## 5. Asymptotic accounting and all dimensions

If a chain is sampled uniformly from an SCD of the `n`-cube, its length
`L_n` obeys

\[
 \Pr(L_n\ge u)=
 {\binom n{\lfloor(n+1-u)/2\rfloor}\over W(n)}
 \quad(u\ge1),                                      \tag{15}
\]

with the usual zero convention outside the rank range. This follows
by telescoping the count `binom(n,i)-binom(n,i-1)` of chains starting
at rank `i`. Adjacent-binomial products give
`L_n/sqrt(n) -> X`, where `Pr(X>x)=exp(-x^2/2)`, and uniform Gaussian
tails. Consequently all fixed polynomial moments converge.

Applied independently to the four chain choices, the sorted lengths
divided by `sqrt(h)` converge to the variables in (2). By (10),

\[
 abc+d w_3(a,b,c)
 =ab(c+d)-{d\over4}(a+b-c)_+^2+O(d).                 \tag{16}
\]

The remaining terms in (14) are `O((1+a+b+c+d)^2)`, uniformly, so their
expectation is `O(h)`. The principal term has scale `h^{3/2}` and is
continuous in the scaled lengths; the Gaussian moment bounds justify
convergence of its expectation.

Finally,

\[
 L_h\sim {2^h\over\sqrt{2\pi h}},\qquad
 W(4h)\sim {2^{4h}\over\sqrt{2\pi h}},
 \qquad {8L_h^4h^{3/2}\over W(4h)}
                   \longrightarrow(2/\pi)^{3/2}.   \tag{17}
\]

The complete error from all bridge cuts, initial/final letters, and
integer floors is `O(W(4h)/sqrt(h))`. Equations (14)--(17) establish
`nu(4h)<=(c_4+o(1))W(4h)` with (2).

For any large `k`, let `4h<=k<4h+4`. At most three ordinary top-bit
splices give a universal word of length at most `2^{k-4h}nu(4h)`.
The exact binomial ratios give
`2^{k-4h}W(4h)/W(k)=1+O(1/h)`. This proves the all-dimension statement
(1), without any sparse-subsequence or fixed-seed extrapolation.

## 6. Exact integral for the four-block constant

For the order statistics in (2), the joint density is
`24abcd exp(-(a^2+b^2+c^2+d^2)/2)` on `0<a<b<c<d`.
Integrate out `d`, then put `a=ru`, `b=rv`, `c=r` with
`0<u<v<1`. The needed tail integrals are

\[
 \int_r^\infty d e^{-d^2/2}\,dd=e^{-r^2/2},\qquad
 \int_r^\infty d^2e^{-d^2/2}\,dd=
 r e^{-r^2/2}+\sqrt{\pi/2}\operatorname{erfc}(r/\sqrt2).
\]

The remaining radial integrals are

\[
 \int_0^\infty r^8e^{-(q+1)r^2/2}\,dr
       ={105\sqrt{\pi/2}\over(q+1)^{9/2}},
\]

\[
 J(q):=\int_0^\infty r^7e^{-qr^2/2}
                       \operatorname{erfc}(r/\sqrt2)\,dr
 ={48-(105q^3+210q^2+168q+48)/(q+1)^{7/2}\over q^4}.  \tag{18}
\]

Formula (18) follows by one integration by parts using the antiderivative
`-exp(-qr^2/2)(r^6/q+6r^4/q^2+24r^2/q^3+48/q^4)`.

Now put `u=xv`, mapping to the unit square, and define

\[
 q=1+v^2(1+x^2),\quad p=xv^2,\quad
 s={1\over4}(v(x+1)-1)_+^2,\quad
 G(q)={105\over(q+1)^{9/2}},
\]

\[
 H(x,v)=xv^3\{(2p-s)G(q)+(p-s)J(q)\}.
\]

Then the exact formula to be certified is

\[
 \boxed{c_4={48\over\pi}\int_0^1\int_0^1H(x,v)\,dx\,dv.}         \tag{19}
\]

All integrands are nonnegative. In particular
`(v(x+1)-1)_+<=xv`, so `s<=p/4`.

## 7. A rigorous numerical upper certificate

The certificate uses exact rational arithmetic, not floating-point error
estimates. Only the final decimal display is rounded.

On the unit square `1<=q<=3`. The elementary inequality
`erfc(z)<=exp(-z^2)` gives, by differentiating its integral in (18),

\[
 0\le J\le3,\quad |J'|\le6,\quad |J''|\le15.
\]

Direct differentiation gives

\[
 0<G<5,\quad |G'|<11,\quad |G''|<29.
\]

For transparency, put `N=xv^3`, `A=N(2p-s)`, `B=N(p-s)`. The following
uniform bounds follow by the product rule; second derivatives of `s`
are interpreted almost everywhere:

| quantity | value | absolute x derivative | absolute v derivative | absolute xx derivative | absolute vv derivative |
|---|---:|---:|---:|---:|---:|
| A | 2 | 9/2 | 11 | 11/2 | 48 |
| B | 1 | 5/2 | 6 | 7/2 | 28 |
| q | 3 | 2 | 4 | 2 | 4 |

For example `0<=s<=1/4`, `|s_x|<=1/2`, `|s_v|<=1`,
`|s_xx|<=1/2`, and `|s_vv|<=2`, which imply the table immediately.
For `H=A G(q)+B J(q)`, a second product/chain rule gives

\[
                    |H_{xx}|\le644,\qquad
                    |H_{vv}|\le2860.                \tag{20}
\]

For instance the two contributions to the first bound are
`(11/2)*5+2*(9/2)*11*2+2*(29*4+11*2)=501.5` and
`(7/2)*3+2*(5/2)*6*2+(15*4+6*2)=142.5`.
For the second they are `2224` and `636`.

The function is `C^1` across `v(x+1)=1`; its first derivatives are
absolutely continuous on coordinate lines. Thus the standard elementary
one-dimensional midpoint bound applies successively in the two variables.
If `M_n` is the average of `H` over the `n^2` cell midpoints, then

\[
 \left|\int H-M_n\right|
 \le{644+2860\over24n^2}={146\over n^2}.             \tag{21}
\]

Here is the exact arithmetic used to enclose each midpoint value:

1. The midpoint `x,v` and the resulting `q,p,s` are rational.
2. For rational `z>0` and `S=10^20`, compute
   `j=isqrt(floor(z S^2))`. Then `j/S<=sqrt(z)<(j+1)/S`.
3. Use these bounds for `sqrt(q+1)`. In (18), `J` increases with this
   square root when all rational powers of `q,q+1` are held fixed;
   `G` decreases with it. This gives rational lower/upper bounds for `H`.
4. Round each bound outward to denominator `10^16` and sum the resulting
   integers. This prevents large common-denominator growth and remains exact.
5. Bound pi using `pi=16 atan(1/5)-4 atan(1/239)` and the alternating
   arctangent series with 40 terms, whose next term bounds the remainder.
   The identity follows from the tangent addition formula and the angle range.
6. Add/subtract (21), then multiply by `48/pi` with the appropriate
   rational endpoints.

At `n=1024`, the resulting exact rational upper bound is strictly below
`127/100`. Its decimal display and the corresponding lower bound are
those in (3). The full certificate is the function `certify_four_block`
in `four_block_cross_split_20260905_d29f6.py`.

This proves the strict improvement in (1) with a certified error margin
of more than `0.0005` below `1.27`.

## 8. Grouped repair of a whole omitted rectangle

Here is the exact repair lemma that initiated the construction. It is
stronger than paying separately for each target fiber, and is not a
restatement of the individual-fiber cylinder lemma.

Use the earlier split `P=P_0 union {z}`, `|P_0|=b-1`, `|Q|=b`.
Let `C,D` be old SCD chains of lengths `a,c`, and adjoin a fresh `t`-set
`R`. The paired old rectangles are

\[
 \{X\cup(Q\setminus Y):X\in C,Y\in D\},\quad
 \{(P\setminus X)\cup Y:X\in C,Y\in D\}.             \tag{22}
\]

Put `m=min(a,c)`, `M=max(a,c)`, and

\[
 w_m(t)=\sum_{j=0}^{m-1}
 \binom t{\lfloor(t+m-1)/2\rfloor-j}.               \tag{23}
\]

The entire pair (22), times all subsets of `R`, has a nonzero covering
word of length at most

\[
 \boxed{2^t m+(M+2)w_m(t)+M+1.}                     \tag{24}
\]

If `a<=c`, decompose `C x 2^R` into a product SCD, with total membership
`a2^t` and `w_a(t)` chains, and alternate its bridges on `P union R`
with the fixed bridge `beta_Q(D)`. The two boundaries give respectively
`X union Z union (Q\Y)` and
`(P\X) union (R\Z) union Y`. As `Z` ranges through `2^R`, this covers
both complete cylinders. If `c<a`, enlarge the `D` side instead.
The witness and cost proof is exactly the two-boundary proof of Section 2.

The product SCD can be obtained by adjoining one new bit at a time:
from `E_0<...<E_l`, take the long chain
`E_0<...<E_l<E_l union {z}` and the short chain
`E_0 union {z}<...<E_{l-1} union {z}` when nonempty.
Its common center gives precisely the coefficient (23).

Since `w_m(t)<=2^t`, the principal cost in (24) is no greater than
`2^t(a+c)`. At leading order in the regime `t=b->infinity`, it is
therefore beneficial to use grouped repair on every rectangle, not just
the omitted ones; all secondary terms in (24) are still charged.
Crucially, the new support
is placed on `P` for some pairs and on `Q` for others.

For `t=b`, write `m=min(a,c)`, `M=max(a,c)` and decompose `2^R` itself
into SCD chains of lengths `e`. Equation (9) gives

\[
 w_m(b)=\sum_E\min(m,e),\qquad
 2^b m+M w_m(b)=\sum_E\{me+M\min(m,e)\}.
\]

For the three numbers `a,c,e`, the expression inside braces is exactly
their smallest member times the sum of the other two. The same Rayleigh
limit therefore yields the three-block coefficient

\[
 c_3={\sqrt3\over\pi}\mathbb E[A(B+C)],              \tag{25}
\]

for three ordered independent Rayleigh variables. With
`kappa=sqrt(pi/2)`, the expectation is

\[
 6\int_0^\infty x^2e^{-x^2}
      \{x e^{-x^2/2}+\kappa\operatorname{erfc}(x/\sqrt2)\}\,dx
 ={1\over3}+{3\over\sqrt2}\arctan\sqrt2.            \tag{26}
\]

For example, evaluate the first integral as `4/3` and use
`integral exp(-q x^2) erfc(alpha x) dx
=atan(sqrt(q)/alpha)/sqrt(pi q)` and its q derivative for the second.
This proves (4). A separate exact-rational arctangent/root certificate
in the checker encloses its displayed numerical value.

The four-block refinement improves (25): isolating the longest chain
and taking the full SCD of the other three saves the triangle term in
(10), rather than only making two-chain rectangles.

## 9. Verification and limits

Run:

```
python3 scratch/grouped_chain_cylinder_20260905_d29f6.py
python3 scratch/four_block_cross_split_20260905_d29f6.py --certify 1024
```

The first checker verifies 430 grouped paired cylinders and 20 assembled
full-cube words through dimension 14, including every actual interval
union and every position in (24). Its floating-point ledger values through
`b=2048` are diagnostics, not exact numerical certificates.

The second checks 816 signed paired-box words and four complete
four-block words through dimension 16. It verifies (10) for all 512
triples of lengths from 1 through 8, checks the closed-form three-block
constant, and executes the exact-rational certificate (18)--(21).

These finite words are checks of the literal compiler, not finite-optimal
certificates. The all-dimension asymptotic proof is Sections 2--7.

There is no claimed coefficient-one construction. Reset-tail deletion,
cross-split residual targeting at width one, and an iteration reaching
coefficient one are not consequences of (1). The proved progress is the
full-cube upper constant below `1.27`, with a fully paid cross-split word.
