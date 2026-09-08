# Independent audit of subquadratic product-chain aggregation

## 1. Verdict

The core of Theorem A in
`fable_general_case/FABLE_GENERAL_CASE_WORK.md` is correct:

\[
 g_t(\boldsymbol\ell)
 \le w(\boldsymbol\ell)+K(1+\textstyle\sum_i\ell_i)^c
\]

uniformly for all `t`-chain boxes implies

\[
 \nu(k)
 \le W(k)+O_{t,c,K}\!
 \left(W(k)k^{(c-t+1)/2}\right),                     \tag{1.1}
\]

and hence `nu(k)=(1+o(1))W(k)` whenever `c<t-1`.

I independently checked the exact width identity, the SCD height tail and
all real moments, the product factorization, the balanced central-binomial
ratio, degenerate chain heights, and the local-zero bookkeeping.  The proof
does not assume balanced chain heights and does not lose an extra power of
`k` for noninteger `c`.

The clean, self-contained version is
`SUBQUADRATIC_PRODUCT_AGGREGATION.md`.

Three scope qualifications should be attached to Fable's statement.

1. The local estimate must hold uniformly for **every** height vector
   `bold ell in Z_{>=0}^t`, including unbalanced vectors and zero sides.  A
   bound only for the diagonal boxes `g_4(m,m,m,m)`, for example, is not
   enough.
2. If `g_t` omits the local zero target, boxes with nonempty common minimum
   need one additional entry.  The total is at most the number of product
   boxes and is absorbed by the `1` in the error term; it does not alter
   (1.1).
3. Constants depend on the fixed parameters `t,c,K`.  The threshold
   `c<t-1` is the threshold at which this aggregated upper bound becomes
   `o(W)`, not a necessity theorem for all conceivable constructions.

With those qualifications, no counterexample or missing factor remains.

## 2. Exact-width audit

Split `[k]` into blocks of sizes `k_i` and put an arbitrary SCD on each
block.  If a chain has minimum rank `a_i`, its edge-height is

\[
                             \ell_i=k_i-2a_i.         \tag{2.1}
\]

For a tuple of chains, let `A=sum_i a_i` and `L=sum_i ell_i`.  Then

\[
                             L=k-2A.                 \tag{2.2}
\]

The local rank corresponding to global rank `floor(k/2)` is

\[
 \lfloor k/2\rfloor-A
 =\lfloor(k-2A)/2\rfloor
 =\lfloor L/2\rfloor.                               \tag{2.3}
\]

Thus the local central coefficient of the product-chain rank polynomial
counts exactly the global-middle subsets in this product box.  Product
boxes partition the Boolean lattice, so summing these coefficients gives
exactly

\[
                              W(k).                   \tag{2.4}
\]

This verifies equation (3.2) and Theorem 1's imported main-term ledger in
`FIXED_DIMENSION_GRID_REDUCTION.md`.  Parity causes no offset because the
integer `A` may be moved through the floor in (2.3).

One logical detail in the older note should be made explicit.  Symmetry and
unimodality of the rank polynomial identify its largest rank, but those two
properties alone do not prove that no larger antichain exists.  The needed
conclusion is nevertheless correct because every finite product of chains
admits a symmetric-chain decomposition and is therefore Sperner.  The exact
sum (2.4) itself uses only the central coefficient, so even this terminology
does not affect the aggregation ledger.

## 3. SCD-tail audit

Let `s` be one block size, `m=floor(s/2)`, and `L(C)` the height of an SCD
chain.  For every integer `0<=d<=m`,

\[
 \#\{C:L(C)\ge2d\}=\binom{s}{m-d}.                  \tag{3.1}
\]

This is an equality, stronger than the `at most` used in
`FIXED_DIMENSION_GRID_REDUCTION.md`.  Indeed a qualifying symmetric chain
crosses rank `m-d` exactly once, and every point of that rank belongs to
one chain.  Conversely, a chain crossing that rank has height at least
`2d` (at least `2d+1` when `s` is odd).

Since the number of chains is `W(s)`, choosing a chain uniformly gives

\[
 \Pr(L\ge2d)=\frac{\binom{s}{m-d}}{W(s)}.            \tag{3.2}
\]

For even `s=2m`, the ratio is

\[
 \prod_{j=0}^{d-1}\frac{m-j}{m+j+1}
 \le e^{-d^2/s}.                                    \tag{3.3}
\]

For odd `s=2m+1`, the denominators become `m+j+2`, yielding
`exp(-d(d+1)/s)`, so (3.3) still holds.  This is an SCD-independent
sub-Gaussian tail on the scale `sqrt(s)`.

Discrete integration of the tail proves, for every fixed real `q>=0`,

\[
 \frac1{W(s)}\sum_C(1+L(C))^q
 =O_q((1+s)^{q/2}).                                 \tag{3.4}
\]

The replacement of `s` by `1+s` matters only for the literal all-small
statement: the original `O(s^{q/2})` cannot hold at `s=0` when `q>0`, since
the left side is one.  For balanced positive blocks in the asymptotic
argument there is no difference.

### Noninteger exponents

Fable proposed taking `r=ceil(c)` and using

\[
 \mathbb E X^c\le(\mathbb E X^r)^{c/r}.             \tag{3.5}
\]

This is the Lyapunov/power-mean inequality and is valid for the uniform
probability measure on chains.  Combining (3.5) with (3.4) at integer `r`
does give

\[
                         \mathbb E X^c=O(s^{c/2}).   \tag{3.6}
\]

There is no ceiling loss.  The standalone proof goes slightly further and
integrates (3.3) directly, proving (3.4) for real `q` without this detour.

## 4. Product-moment audit

For independent uniformly selected chains in the `t` block SCDs, write
`L_i` for their heights.  There are

\[
                         P=\prod_iW(k_i)             \tag{4.1}
\]

chain tuples.  For `c>=1`, convexity gives

\[
 (1+\textstyle\sum_iL_i)^c
 \le\left(\sum_i(1+L_i)\right)^c
 \le t^{c-1}\sum_i(1+L_i)^c.                        \tag{4.2}
\]

Fable used the weaker constant `t^c`, which is harmless.  For `0<c<1`,
the same conclusion follows from subadditivity with constant one.  Hence

\[
 \begin{aligned}
 \sum_{\boldsymbol C}(1+\textstyle\sum_i\ell_i)^c
 &=P\,\mathbb E(1+\textstyle\sum_iL_i)^c\\
 &\le O_{t,c}\!\left(P\sum_i(1+k_i)^{c/2}\right)\\
 &\le O_{t,c}\!\left(P(1+k)^{c/2}\right).          \tag{4.3}
 \end{aligned}
\]

This factorization is valid regardless of how unbalanced the realized
chain heights are.  In particular, no lower cutoff on `ell_i` is used.

## 5. Balanced-width ratio audit

Uniform Stirling/Wallis bounds say

\[
                         W(n)=\Theta\left(
                         \frac{2^n}{\sqrt{n+1}}
                         \right)                     \tag{5.1}
\]

for all `n>=0`.  Therefore, because `sum_i k_i=k`,

\[
 \frac{\prod_iW(k_i)}{W(k)}
 =\Theta_t\left(
   \frac{\sqrt{k+1}}{\prod_i\sqrt{k_i+1}}
   \right).                                         \tag{5.2}
\]

For a balanced fixed-`t` split, every `k_i+1=Theta_t(k+1)`, so

\[
 \frac{\prod_iW(k_i)}{W(k)}
 =\Theta_t((1+k)^{-(t-1)/2}).                        \tag{5.3}
\]

This independently verifies equation (4.5) of
`FIXED_DIMENSION_GRID_REDUCTION.md`.  The powers of two cancel exactly; the
remaining square-root factors give `t-1`, not `t`, powers of `sqrt(k)`.

For an arbitrary unbalanced block split the exact useful expression is
(5.2), not (5.3).  The proof deliberately chooses a balanced split.

## 6. Aggregated exponent

Multiplying (4.3) by (5.3) gives

\[
 \sum_{\boldsymbol C}(1+\textstyle\sum_i\ell_i)^c
 =O_{t,c}\left(
 W(k)(1+k)^{c/2-(t-1)/2}
 \right),                                           \tag{6.1}
\]

which is exactly

\[
 O_{t,c}\left(
 W(k)(1+k)^{(c-t+1)/2}
 \right).                                           \tag{6.2}
\]

The exponent is negative precisely when `c<t-1`.  In particular:

* `t=3`: every uniform local error `O((1+p+q+r)^c)` with `c<2` aggregates
  to `o(W(k))`;
* `t=4`: every uniform local error
  `O((1+ell_1+ell_2+ell_3+ell_4)^c)` with `c<3` aggregates to `o(W(k))`.

The second bullet cannot be weakened to a statement only about
`g_4(m,m,m,m)`.  Balanced Boolean coordinate blocks still yield SCD tuples
such as `(ell_1,ell_2,ell_3,ell_4)` with very different heights, including
zeros.  Those boxes constitute part of the partition and need local words
too.  This is the only materially misleading shorthand in Fable's ledger.

## 7. Zero and short-chain audit

The local quantity `g_t` in `FIXED_DIMENSION_GRID_REDUCTION.md` is described
as omitting the all-empty target "when appropriate."  The exact convention
needed by the Boolean aggregation is as follows.

For a chain tuple with common minimum

\[
                         B=\bigcup_iC^{(i)}_0,        \tag{7.1}
\]

the local origin maps to `B`.

* If `B=emptyset`, it is the globally omitted zero mask and needs no
  witness.
* If `B` is nonempty, prepend one local-zero entry.  After translation it
  is the legal nonzero array entry `B` and witnesses the box origin.

There is at most one extra entry per chain tuple.  Since
`(1+sum ell_i)^c>=1`, these entries are absorbed by increasing `K` by one.
All other translated entries are nonzero.  Height-zero chains and the
all-zero local box therefore cause no exception to (6.2).

This also explains why silently omitting every local origin would leave a
coverage gap, while demanding a literal global zero in every box would be
unnecessary.

## 8. Final certification

After the three scope repairs in Section 1, Theorem A is mathematically
sound.  The threshold and global exponent are exactly as claimed:

\[
 \boxed{
 c<t-1
 \quad\Longrightarrow\quad
 \nu(k)\le W(k)+o(W(k)).}
\]

What remains open is entirely local: proving a uniform subcritical error
bound for all fixed-dimensional chain boxes.  This audit does not provide
such a local construction.
