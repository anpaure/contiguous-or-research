# Polynomial protected forests extend from two sub-half exposure bounds

**Date:** 2026-08-05  
**Method:** exact protected Ore localization plus the two sharp
partial-shadow thresholds; no computation or search  
**Status:** unconditional factor-extension theorem.  It upgrades the
`m-2` small-protected-bank theorem to every polynomial-size protected path
forest whose two literal exposure parameters stay below half the owner
degree by a fixed linear margin.

## 0. Setting

Work in the balanced middle-level incidence graph on `[2r-1]`, with

\[
 \mathcal L={ [2r-1]\choose r-1},
 \qquad
 \mathcal U={ [2r-1]\choose r},
 \qquad
 W=|\mathcal L|=|\mathcal U|.
\tag{0.1}
\]

Let `P` be the incidence lift of a vertex-disjoint owner-path forest.  Thus
every protected lower vertex has degree two, every unprotected lower
vertex has degree zero, and every owner has protected degree at most two.
Put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},
 \qquad X=\mathcal L\setminus Z,
 \qquad e=|E(P)|=2|Z|.
\tag{0.2}
\]

Use the two exposure parameters

\[
 \alpha=
 \max_{x\in X}|\{U\supset x:d_P(U)>0\}|,
\tag{0.3}
\]

\[
 \beta=
 \max_{U\in\mathcal U}|N(U)\cap Z|.
\tag{0.4}
\]

Define

\[
 D_\alpha=r-\alpha-1,
 \qquad D_\beta=r-\beta-1,
 \qquad K(D)={2D-1\choose D},
\tag{0.5}
\]

and

\[
                         M_r(e)={r(r-1)\over2r-1}e.
\tag{0.6}
\]

## 1. Exact extension criterion

### Theorem 1.1

Assume `alpha,beta<=r-3`.  If

\[
 \boxed{
 M_r(e)\le\min\{K(D_\alpha),K(D_\beta)+1\},}
\tag{1.1}
\]

then `P` extends to a spanning two-factor of the middle-level incidence
graph.

#### Proof

Suppose `P` does not extend.  The capacitated Hall theorem gives a failed
residual shore `A subseteq X`.  The protected Ore near-shadow localization
gives

\[
 \min\{|A|,W-|A|\}<M_r(e).                              
\tag{1.2}
\]

If `|A|<=W/2`, the sharp small-shore theorem gives

\[
                         |A|\ge K(D_\alpha),              
\tag{1.3}
\]

contradicting (1.1)--(1.2).

Now suppose `|A|>W/2`.  Put

\[
                         B=X\setminus A.                  
\tag{1.4}
\]

Because `A subseteq X`, its full complement is the disjoint union

\[
                         \mathcal L\setminus A=Z\mathbin{\dot\cup}B.
\tag{1.5}
\]

The optional-complement identity says that failure of `A` is equivalent
to positivity of the optional bank `B`.  The sharp optional-core theorem
therefore gives

\[
                         |B|\ge K(D_\beta)+1.             
\tag{1.6}
\]

On the other hand, (1.2) and (1.5) give

\[
                         |B|\le W-|A|<M_r(e),             
\tag{1.7}
\]

again contradicting (1.1).  Both cases are impossible, so every residual
Hall cut is safe.  The capacitated Hall theorem completes `P` to a spanning
two-factor. \(\square\)

## 2. Polynomial corollary

### Corollary 2.1

Fix constants `C<infinity` and `epsilon>0`.  Suppose

\[
                         e\le r^C,                        
\tag{2.1}
\]

and

\[
                         \alpha,\beta
                         \le(1/2-\epsilon)r.              
\tag{2.2}
\]

Then, for all sufficiently large `r`, `P` extends to a spanning
two-factor.

#### Proof

Equation (2.2) gives

\[
 D_\alpha,D_\beta\ge(1/2+\epsilon)r-1.
\tag{2.3}
\]

Stirling's formula gives, uniformly for these two values,

\[
 K(D)=2^{2D-O(\log D)}
     \ge2^{(1+2\epsilon)r-O(\log r)}.                    
\tag{2.4}
\]

Meanwhile

\[
 M_r(e)=O(r^{C+1}).                                      
\tag{2.5}
\]

The exponential lower bound (2.4) eventually exceeds (2.5), so Theorem
1.1 applies. \(\square\)

### Corollary 2.2 (deadline-scale protected collars)

Any protected path bank with

\[
 e=O(r^{3/2}),
 \qquad
 \alpha,\beta=O(\sqrt r)
\tag{2.6}
\]

extends to a spanning two-factor for all sufficiently large `r`.

Thus the `O(Hr)` synchronized PBBS collar bank at
`H=O(d)=O(sqrt r)` has no residual owner/`q1` Hall obstruction once its
two exposure bounds (2.6) are established.  Component structure, upper
surjectivity, residence, and the typed cap are separate statements.

## 3. Why both exposures are needed

The edge count `e=poly(r)` alone localizes a failed cut to a polynomial
small or co-small shore, but it does not exclude either shore:

* `alpha` controls the sharp threshold for a small residual shore;
* `beta` controls the sharp threshold for the optional part of a co-small
  shore.

The theorem therefore does not silently replace a local exposure
hypothesis by aggregate sparsity.  A polynomial bank concentrated in one
owner star can still violate the required hypotheses.

## 4. Dependencies and scope

The proof combines, without strengthening their scopes:

* `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md`;
* `MATH_THEOREM_SUBLINEAR_EXPOSURE_PROTECTED_FACTOR_SMALL_CUT_AND_OPTIONAL_CORE_REDUCTION_20260805.md`.

No connectedness, Hamiltonicity, upper-palette exactness, residence, or
literal compiler conclusion is asserted.

