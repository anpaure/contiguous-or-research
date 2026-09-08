# Long-wrap Apéry clocks: Euclidean shifted-block collapse and the pure theta residual

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It closes the exact
first-carry long-wrap family for every period `4<=h<=1000` and reduces every
larger period to one explicit sufficient finite theta-block inequality.  It does not
prove that last theta inequality for arbitrary `h`, universal Bellman
positivity, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad
 F(w)=\sum_{q\ge0}K(qA+w),\qquad C=F(0),
\tag{0.1}
\]

and write

\[
 \rho(At)=-4\sum_{\ell\ge1}e^{-4\pi\ell^2}
                    \cos(2\pi\ell t).
\tag{0.2}
\]

The exact Jacobi reflection identity is

\[
                         F(w)+F(A-w)=\rho(w),
\tag{0.3}
\]

and the audited train estimates are

\[
 C>{43\over1000},\qquad
 0<F(w)<{61\over1000}\quad(0\le w\le A/2),
\tag{0.4}
\]

\[
                         |\rho(w)|<{1\over20000}.
\tag{0.5}
\]

We study the sole one-defect survivor from the cyclic-gap classification:

\[
 W_{qh+r}=q(A-a)+ra,\qquad q\ge0,\quad 0\le r<h,
\tag{0.6}
\]

where

\[
 h\ge4,\qquad {A\over2(h-1)}<a<{A\over h+1}.
\tag{0.7}
\]

Its exact endpoint-period lower sum is

\[
 S_h(a)=C+\sum_{i=1}^{h-1}F(ia)+F(A-a),
 \qquad \Phi(W)\ge S_h(a).
\tag{0.8}
\]

The point of the theorem is that every non-theta term in (0.8) admits one
uniform shifted-block estimate.  No growing collection of compact train
inequalities remains.

## Exact normalized functional and its uniform endpoint

With `x=a/A`, the literal long-wrap functional itself is the one-variable
series

\[
 \boxed{
 \Phi_h(x)=\sum_{q\ge0}\sum_{r=0}^{h-1}
 K\!\left(A\{q+(r-q)x\}\right).}
\tag{0.9}
\]

Termwise differentiation is justified on every closed subinterval of
the narrow band by a Gaussian summable majorant, and gives

\[
 \boxed{
 \Phi_h'(x)=A\sum_{q\ge0}\sum_{r=0}^{h-1}(r-q)
 K'\!\left(A\{q+(r-q)x\}\right).}
\tag{0.10}
\]

At the uniform endpoint `x=1/(h+1)`, the arguments in (0.9) are

\[
                         {A(qh+r)\over h+1}.
\]

As `(q,r)` ranges over `q>=0`, `0<=r<h`, the integer `qh+r` ranges over
all nonnegative integers exactly once.  Hence

\[
 \boxed{
 \Phi_h\!\left({1\over h+1}\right)
       =\sum_{N\ge0}K\!\left({AN\over h+1}\right)
       =:\mathcal C\!\left({A\over h+1}\right)>0.}
\tag{0.11}
\]

Here `\mathcal C(s)=\sum_{N\ge0}K(Ns)` is the arithmetic all-ceiling
train; its strict positivity is the proved reciprocal-ceiling theorem.
This notation is distinct from the scalar `C=F(0)` in (0.1).

The lower endpoint `x=1/[2(h-1)]` is covered by the earlier
endpoint-period argument because every displayed compact shift is at most
`A/2`.  Thus both endpoints are rigorously positive.  The proof below does
not assume a sign for (0.10); instead it obtains a uniform lower bound from
the endpoint-period minorant (0.8).

## 1. The normalized Euclidean chamber

Put

\[
 x={a\over A},\qquad {1\over x}=2m+\lambda,
 \qquad m=\left\lfloor{1\over2x}\right\rfloor,
 \qquad0\le\lambda<2,
\tag{1.1}
\]

and set

\[
 n=h-1-m,\qquad k=m-n.
\tag{1.2}
\]

The inequalities (0.7) give

\[
                         n\ge1,\qquad k+\lambda>2.
\tag{1.3}
\]

Indeed `1/x<2(h-1)` gives `m<=h-2`, hence `n>=1`; and, since
`h=m+n+1`, the inequality `1/x>h+1` is exactly

\[
                         2m+\lambda>m+n+2,
\]

which is (1.3).

In particular `m>=2`, `k>=1`, and `k<=m-1`.  Thus every block below is
nonempty on the open chamber.  The lower endpoint of (0.7), where `n=0`
can occur, was already closed before entering this chamber; it is not
silently included in the block argument.

Write

\[
                         f(t)=F(At),\qquad0\le t\le{1\over2}.
\tag{1.4}
\]

The terms with `i<=m` in (0.8) lie in the lower half, while those with
`i>=m+1` lie in the upper half.  Reflect the latter by (0.3).  Since

\[
 1-ix=(2m+\lambda-i)x,
\]

the complementary lower-half arguments, in increasing order, are

\[
 (k+\lambda)x,(k+1+\lambda)x,\ldots,(m-1+\lambda)x.
\tag{1.5}
\]

Also `F(A-a)+F(a)=rho(a)`.  Therefore (0.8) has the exact form

\[
\boxed{
\begin{aligned}
 S_h(a)={}&C+\sum_{i=2}^{m}f(ix)
       -\sum_{j=k}^{m-1}f((j+\lambda)x)+R_h(x),\\
 R_h(x)={}&\rho(Ax)+\sum_{j=k}^{m-1}
                         \rho(A(j+\lambda)x).
\end{aligned}}
\tag{1.6}
\]

This is the Euclidean shifted-block identity.

## 2. A one-mode translation lemma

### Lemma 2.1 (fractional translation of a unimodal grid block)

Let `g` be nonnegative on an interval, nondecreasing up to one mode and
nonincreasing after it.  Suppose

\[
                         g(0)=c,\qquad \sup g=M.
\]

For a consecutive grid block `J={r,...,s}` and `0<=theta<1`, with all
points involved in the interval,

\[
 \sum_{j\in J}g((j+\theta)d)-\sum_{j\in J}g(jd)
 \le M-c
\tag{2.1}
\]

provided the left endpoint `rd` is before the mode.  If it is at or after
the mode, the left side is nonpositive.

#### Proof

After the mode every summand can only decrease under a right translation.
Before the mode retain only the positive increments.  Their intervals

\[
                         [jd,(j+\theta)d]
\]

have disjoint interiors because `theta<1`.  On the nondecreasing part the
sum of the retained increments is at most the total rise from `g(rd)` to
the mode, namely `M-g(rd)`.  If `rd` is before the mode, monotonicity from
zero gives `g(rd)>=g(0)=c`.  This proves (2.1). \(\square\)

### Lemma 2.2 (the threshold train is one-mode)

The function `f` in (1.4) is nonnegative and one-mode on `[0,1/2]`.

#### Proof

Strict positivity is part of (0.4).  The authenticated compact-train
critical-point theorem says that every interior critical point of `F` on
`[0,A/2]` is a strict local maximum.  The train is real analytic in the
interior.  Two distinct critical maxima would force an interior minimum
between them, which would be another critical point and not a strict local
maximum.  Hence there is at most one critical point.  It follows that the
train is monotone or increases up to one mode and decreases thereafter.
\(\square\)

## 3. Collapse of every compact-train term

Write

\[
                         \lambda=s+\theta,
 \qquad s\in\{0,1\},\quad0\le\theta<1.
\tag{3.1}
\]

The integer comparison block

\[
                         k+s,k+s+1,\ldots,m-1+s
\tag{3.2}
\]

is contained in `{2,...,m}`.  If `s=0`, equation (1.3) and `lambda<1`
give `k>=2`; if `s=1`, its first index is at least two.  Its last index is
at most `m` in either case.

Apply Lemma 2.1 to (3.2), with `d=x`, and use (0.4).  The shifted block in
(1.6) can exceed its integer comparison block by less than

\[
                         {61\over1000}-{43\over1000}.
\tag{3.3}
\]

All integer terms outside the comparison block are nonnegative.  Thus
(1.6) gives the uniform bound

\[
\boxed{
 S_h(a)>2{43\over1000}-{61\over1000}+R_h(x)
       ={1\over40}+R_h(x).}
\tag{3.4}
\]

This is the main collapse: the complete compact part of the arbitrary
period problem has become one fixed `1/40` margin.

## 4. The pure theta gate

From (0.2) and (1.6), the residual is explicitly

\[
\boxed{
 R_h(x)=-4\sum_{\ell\ge1}e^{-4\pi\ell^2}
 \left[
  \cos(2\pi\ell x)
  +\sum_{j=k}^{m-1}\cos(2\pi\ell(j+\lambda)x)
 \right].}
\tag{4.1}
\]

Consequently the single inequality

\[
                         \boxed{R_h(x)\ge-{1\over40}}
\tag{4.2}

closes the long-wrap clock at `(h,x)`.  A strict inequality is sufficient
without any endpoint discussion.  This is a sufficient closure gate, not
an iff criterion for positivity, because (3.4) discarded nonnegative
integer-block terms and (0.8) is itself a lower comparison.

For clarity, the finite cosine block in (4.1) is the literal Dirichlet
block

\[
 \sum_{j=k}^{m-1}\cos\bigl(2\pi\ell(j+\lambda)x\bigr)
 ={
   \sin(\pi\ell n x)
  \over
   \sin(\pi\ell x)
  }
 \cos\!\left(2\pi\ell x
       \left(\lambda+{k+m-1\over2}\right)\right),
\tag{4.2a}
\]

where `n=m-k`; at `\sin(\pi\ell x)=0` the right side is interpreted by
continuous extension and equals the original finite sum.  Thus no finite
period census is hidden in the remaining gate.

There are exactly `n+1` theta terms in `R_h`.  Hence (0.5) gives

\[
                         R_h(x)>-{n+1\over20000}.
\tag{4.3}

The narrow-band lower bound in (0.7) also gives

\[
 {1\over2x}>{h+1\over2},\qquad
 n+1=h-m\le\left\lfloor{h\over2}\right\rfloor.
\tag{4.4}

For completeness, if `h=2s`, then `1/(2x)>s+1/2` gives `m>=s`;
if `h=2s+1`, then `1/(2x)>s+1` gives `m>=s+1`.  These are exactly
the two cases of (4.4).

Combining (3.4), (4.3), and (4.4), for every `4<=h<=1000`,

\[
 S_h(a)>{1\over40}
 -{\lfloor h/2\rfloor\over20000}\ge0.
\tag{4.5}

All inequalities used before the final weak comparison are strict, so the
value is strictly positive also at `h=1000`.  By (0.8),

\[
\boxed{
 \Phi(W)>0\qquad
 (4\le h\le1000,\quad
 A/[2(h-1)]<a<A/(h+1)).}
\tag{4.6}

Together with the earlier broad-subrange theorem, every exact-first-carry
one-defect clock of period at most one thousand is therefore positive.

For `h>=1001`, equations (3.4), (4.1), and the sufficient gate (4.2) are
the remaining proof-safe route supplied by this theorem.  In particular,
no compact Gaussian train, affine clock, or growing family of reflection
losses remains in that route: only the displayed finite Dirichlet block
under the superexponentially decaying theta weights.  Failure of (4.2)
would not prove that the original clock is nonpositive.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| one-defect classification, endpoint-period bound, and narrow band | `MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md` | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| full-half train bounds | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| compact-train critical-point theorem | `MATH_THEOREM_FIVE_SLOT_SHORT_SINGLETON_REPEATED_GAP_COMPLETE_CLOSURE_20260804.md` | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| exact Jacobi reflection identity | `MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_EXACT_THETA_ENDPOINT_DESCENT_20260804.md` | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |
| strict arithmetic all-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |
