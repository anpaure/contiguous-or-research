# Sharp one-sided Boolean threshold shadows via the partial-shadow theorem

**Date:** 2026-08-04  
**Method:** pure mathematics; exact application of the Chao--Yu theorem
resolving the Bollobas--Eccles partial-shadow conjecture  
**Status:** unconditional, subject only to the cited published/preprint
theorem.  No computation, finite search, or solver is used.

## 0. Result

Let

\[
 \mathcal A\subseteq\binom{[N]}k,
 \qquad \varnothing\ne
 \mathcal C\subseteq\binom{[N]}{k+1},
\tag{0.1}
\]

let `D>=2`, and assume that

\[
 d_{\mathcal A}(C)
 :=|\{A\in\mathcal A:A\subset C\}|
 \ge D
 \qquad(C\in\mathcal C).
\tag{0.2}
\]

Then the following sharp implication holds:

\[
 \boxed{
 |\mathcal C|\ge|\mathcal A|
 \quad\Longrightarrow\quad
 |\mathcal A|\ge\binom{2D-1}{D-1}.}
\tag{0.3}
\]

If equality holds in (0.3), then necessarily

\[
 |\mathcal A|=|\mathcal C|
 =\binom{2D-1}{D-1}
 =\binom{2D-1}{D},
\tag{0.4}
\]

and, after deleting unused coordinates, there are disjoint sets `X,Y`
with

\[
 |X|=2D-1,
 \qquad |Y|=k+1-D,
\tag{0.5}
\]

such that

\[
 \boxed{
 \begin{aligned}
  \mathcal A&=\{Y\cup S:S\in\tbinom X{D-1}\},\\
  \mathcal C&=\{Y\cup T:T\in\tbinom X D\}.
 \end{aligned}}
\tag{0.6}
\]

Thus the lifted consecutive middle pair of the `(2D-1)`-cube is not
merely an example: it is the unique equality shape, up to relabelling and
irrelevant ambient coordinates.

If the side imbalance is strict, then integrality and the equality
classification give the strict strengthening

\[
 \boxed{
 |\mathcal C|>|\mathcal A|
 \quad\Longrightarrow\quad
 |\mathcal A|\ge\binom{2D-1}{D-1}+1.}
\tag{0.7}
\]

## 1. External theorem used

For completeness, here is exactly the form of the partial-shadow theorem
that is used.

### Chao--Yu partial-shadow theorem

Let `r,m` be positive integers, let `0<=s<=r`, and let `x>=r-s` be real
with

\[
                         m=\binom{x}{r-s}.
\tag{1.1}
\]

Suppose `mathcal J` is an `m`-element family of `r`-sets and `mathcal F`
is a family of `(r-1)`-sets such that every member of `mathcal J` has at
most `s` facets missing from `mathcal F`.  Then

\[
                         |\mathcal F|
 \ge\binom{x}{r-s-1}.
\tag{1.2}
\]

Moreover, equality in (1.2) forces disjoint sets `X,Y`, with
`|X|=x` and `|Y|=s`, for which

\[
 \mathcal J=\{Y\cup S:S\in\tbinom X{r-s}\},
 \qquad
 \mathcal F=\{Y\cup T:T\in\tbinom X{r-s-1}\}.
\tag{1.3}
\]

This is Theorem 1.7 (source label `theorem:PartialShadow`) in the primary
source:

> Ting-Wei Chao and Hung-Hsun Hans Yu, *Tight Bound and Structural
> Theorem for Joints*, arXiv:2307.15380v3 (2023),
> <https://arxiv.org/abs/2307.15380>.

It resolves the conjecture of Bollobas and Eccles on partial shadows.  A
later paper by the same authors restates the numerical assertion as the
partial-shadow phenomenon: *When Joints Meet Extremal Graph Theory:
Hypergraph Joints*, arXiv:2410.06498.

The proof of that input theorem is deep (it passes through the sharp
joints theorem and the polynomial method).  No compression-only proof of
the full partial-shadow theorem is asserted here.

## 2. Exact parameter translation

Put

\[
                        r=k+1,
 \qquad                 s=r-D=k+1-D.
\tag{2.1}
\]

Every `C in mathcal C` has exactly `r` facets.  Condition (0.2) says that
at most `r-D=s` of those facets are missing from `mathcal A`.  Therefore
the pair

\[
                         (\mathcal J,\mathcal F)
                         =(\mathcal C,\mathcal A)
\tag{2.2}
\]

is an admissible partial-shadow pair with

\[
                         r-s=D.
\tag{2.3}
\]

Let

\[
                         M=|\mathcal C|.
\tag{2.4}
\]

The hypotheses make `M>=1`.  There is a unique real `x>=D` satisfying

\[
                         M=\binom{x}{D},
\tag{2.5}
\]

because the generalized binomial coefficient is continuous and strictly
increasing on `[D,infinity)`, beginning with `binom(D,D)=1`.

The partial-shadow theorem gives

\[
                         |\mathcal A|
                         \ge\binom{x}{D-1}.
\tag{2.6}
\]

This is already an exact rank-free threshold-shadow inequality: the
ambient ranks `k,k+1` occur only through the number `s` of allowed missing
facets and disappear from the numerical answer.

## 3. Balance forces `x>=2D-1`

By the assumed side balance and (2.5)--(2.6),

\[
 \binom{x}{D}
 =|\mathcal C|
 \ge|\mathcal A|
 \ge\binom{x}{D-1}.
\tag{3.1}
\]

For real `x>=D`, both binomial coefficients are positive and

\[
 {\binom{x}{D}\over\binom{x}{D-1}}
 ={x-D+1\over D}.
\tag{3.2}
\]

Consequently (3.1) implies

\[
                         x-D+1\ge D,
 \qquad\text{hence}\qquad
                         x\ge2D-1.
\tag{3.3}
\]

The function `binom(x,D-1)` is increasing on this range, so (2.6) gives

\[
 |\mathcal A|
 \ge\binom{x}{D-1}
 \ge\binom{2D-1}{D-1},
\tag{3.4}
\]

which proves (0.3).

If equality holds in (3.4), strict monotonicity forces `x=2D-1`.
Equations (2.5) and (3.1) then force (0.4), and equality holds in the
partial-shadow theorem itself.  Its equality classification gives
(0.5)--(0.6).

Finally, if `|mathcal C|>|mathcal A|`, equality in (0.3) is impossible by
(0.4).  Since `|mathcal A|` is integral, (0.7) follows.

## 4. Optional-bootstrap specialization

For the optional bootstrap core, use

\[
 \mathcal A=B^-,
 \qquad
 \mathcal C=Q,
 \qquad
 D=d-3.
\tag{4.1}
\]

The previously proved bootstrap ledger gives

\[
 |Q|\ge|B^-|+1,
 \qquad
 |B^-\cap\tbinom U{m-1}|\ge d-3
 \quad(U\in Q).
\tag{4.2}
\]

Thus (0.7), not merely (0.3), applies and yields the sharp strict-balance
obstruction

\[
 \boxed{
 |B^-|\ge
 \binom{2d-7}{d-4}+1.}
\tag{4.3}
\]

Writing `D=d-3`, Stirling's formula gives

\[
 \binom{2D-1}{D-1}
 ={1\over2}\binom{2D}{D}
 \sim {4^D\over2\sqrt{\pi D}}.
\tag{4.4}
\]

Hence the old central-`D` obstruction of order `2^D/sqrt(D)` improves to
order `4^D/sqrt(D)`.  Since `d=Theta(sqrt(m))` in the ambient application,
this remains `2^{Theta(sqrt(m))}`, but doubles the leading exponential
constant in the natural `d` scale.

## 5. Exact scope

The sharp one-sided threshold-shadow conjecture isolated in
`MATH_THEOREM_OPTIONAL_BOOTSTRAP_BALANCED_CORE_AND_CENTRAL_D_BINOMIAL_20260804.md`
is therefore **proved**, not open.

This theorem does **not** by itself eliminate the optional core.  The
ambient Boolean middle layer is much larger than (4.3), and no previously
proved upper bound on `|B^-|` contradicts (4.3).  What it does prove is
that every surviving optional obstruction is exponentially larger than
previously known and that the only non-strict extremal shape is a lifted
middle pair of a `(2D-1)`-cube.  Any final exclusion still needs a
trace-, chronology-, or capacity-specific upper/localization argument.
