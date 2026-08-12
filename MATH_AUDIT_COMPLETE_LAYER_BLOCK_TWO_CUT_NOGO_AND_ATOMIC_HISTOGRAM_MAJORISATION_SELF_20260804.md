# Self-audit: complete-layer two-cut no-go and atomic histogram majorisation

**Date:** 2026-08-04  
**Method:** independent symbolic replay of every cut and asymptotic step;
no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_COMPLETE_LAYER_BLOCK_TWO_CUT_NOGO_AND_ATOMIC_HISTOGRAM_MAJORISATION_20260804.md`  
**Verdict:** **GO at the stated rank-histogram scope.**

## 1. Index and capacity replay

With `t_0=r-D`, a start at rank `t` has free residual capacity
`t-t_0`.  Summing the new-start counts from capacity `q` upward gives

\[
 \sum_{t=t_0+q}^{r}h_t
 =\sum_{t=t_0+q}^{r}(C_t-C_{t-1})
 =C_r-C_{t_0+q-1}=K_q.
\]

Thus the capacity multiset really has conjugate sequence `(K_q)`.  There
is no off-by-one error at `q=1` or `q=D`.

## 2. Two-cut replay

The highest residual block has top `t_0-1` and contributes
`C_(t_0-1)` flags to its own width cut.  Its width cut gives

\[
 C_{t_0-1}\le W-C_{t_0+\ell_1-1}.
\]

Under `ell_1/D -> alpha`, the three normalized distances from the central
rank are respectively `1`, `1-alpha`, and `1+alpha`.  Hence the limiting
inequality and second-block contribution are exactly those displayed in
the theorem.  The `q=1` capacity is `W-C_(t_0)`.  Subtraction gives

\[
 2e^{-\pi/4}+e^{-(\pi/4)(1+\alpha_*)^2}-1>0.
\]

The second block exists for all sufficiently large `k` because
`t_0/D -> infinity`.  Every complete-layer flag marks its own top, so
cardinality overload is a valid lower bound on omitted target weight.

## 3. Analytic Gaussian inequality

The Riemann integrand has the correct two displacements:

\[
 t_0-1-j=r-D-1-j,
 \qquad
 t_0+j=r-D+j.
\]

After division by `D`, these tend to `1+x` and `1-x`.  The normalization
`D^2(2/k)->pi/4` gives the exponent `a=pi/4`.

For

\[
 P(x)=e^{-a(1-x)^2}+e^{-a(1+x)^2},
\]

the sign of `P'` is the sign of `tanh(2ax)-x`.  Its derivative is strictly
decreasing, so there is one positive stationary point.  Since `P(0)<1`
and `P(1)>1`, the level one is crossed exactly once.  Therefore
`H'=1-P` changes from positive to negative once.  The endpoint calculation

\[
 \int_0^2 e^{-(\pi/4)u^2}\,du=\operatorname{erf}(\sqrt\pi)<1
\]

is exact.  Hence `H>0` away from zero and `H(x)/x` has a positive minimum.
This supplies the uniform margin used in the discrete cuts.

The compactness split covers both possible regimes: `p/D` bounded away
from zero gives a uniform Riemann sum, while `p/D ->0` gives
`2e^(-pi/4)<1`.  The uniform local central-binomial estimate is valid on
the entire `O(sqrt(k))` band.  No numerical experiment is used.

## 4. Gale--Ryser/max-flow replay

For a set of `p` rank columns, a socket of capacity `c_i` can receive at
most `min(c_i,p)` units, because the matrix is zero--one in each
row--column pair.  These are the complete max-flow cuts.  Sorting column
demands gives the worst `p`-set, and Ferrers double counting gives

\[
 \sum_i\min(c_i,p)=\sum_{q=1}^{\min(p,D)}K_q.
\]

For `p<=D`, the theorem's binomial pair inequality rearranges exactly to
the required cut.  For `p>D`, total mass is the only remaining cut.  Flow
integrality produces an exact zero--one matrix.

## 5. Scope audit

The positive result is deliberately only a rank-incidence theorem.  It
does not assert that targets placed in one row are nested, that they share
a containing owner, or that an arbitrary atomically split row family has
the complete-layer symmetry required by the joint-start orbit lift.
Therefore it does not prove `nu(k)<=B(k)+O(1)`.

The negative theorem is correspondingly narrow: it rules out unsplit
contiguous complete-layer block partitions, not cross-SCD rechainization
or within-layer splitting.  These exclusions and surviving requirements
are stated explicitly in the theorem.

