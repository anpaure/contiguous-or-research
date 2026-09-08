# Independent audit: long-wrap Euclidean shift and theta residual

**Date:** 2026-08-04  
**Target:** `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md`  
**Target SHA-256 after proof-hygiene corrections:**
`7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738`  
**Verdict:** **PASS / GO in its corrected stated scope.**

The theorem proves positivity of every exact-first-carry long-wrap clock in
the open narrow band for `4<=h<=1000`.  For `h>=1001` it supplies one
explicit sufficient theta/Dirichlet closure inequality; it does not claim
that failure of that inequality proves nonpositivity.  No enumeration,
solver, numerical search, or H100 computation is used.

## 1. Frozen inputs checked

The four original dependency hashes agree byte-for-byte with the theorem:

| dependency | SHA-256 |
|---|---|
| one-defect classification and endpoint-period comparison | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| full-half compact-train estimates | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
| compact-train critical-point theorem | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| exact Jacobi reflection identity | `0bed69bf36b52abb5eab3022f2a06f3eabe7f05cdd299d232d9fd0a7b90094ff` |

The corrected theorem also names the arithmetic all-ceiling input explicitly:

`MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md`,
SHA-256
`c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d`.

The audit treats the following already-proved analytic estimates as frozen
inputs:

\[
C=F(0)>43/1000,
\qquad 0<F(w)<61/1000\quad(0\le w\le A/2),
\]

\[
F(w)+F(A-w)=\rho(w),
\qquad |\rho(w)|<1/20000.
\]

## 2. Normalization and literal clock

At exact first carry, the long wrap has period increment

\[
P=A-a,
\qquad
W_{qh+r}=q(A-a)+ra
\quad(q\ge0,\ 0\le r<h).
\]

Writing `x=a/A` gives exactly

\[
W_{qh+r}=A\{q+(r-q)x\},
\]

so equation (0.9) is the literal Bellman series, with no missing residue or
endpoint term.  On a compact subinterval of the open narrow band,
`1-x` is bounded away from zero; the factor `|r-q|` in the derivative is
therefore dominated by a Gaussian-summable `O(q^2 e^{-c q^2})` majorant.
Termwise differentiation in (0.10) is valid, although the sign of that
derivative is not used later.

At `x=1/(h+1)`,

\[
q+(r-q)x={qh+r\over h+1}.
\]

The map `(q,r) -> qh+r` is a bijection from
`Z_{>=0} x {0,...,h-1}` to `Z_{>=0}`.  The corrected equation (0.11) is
therefore the arithmetic all-ceiling train
`mathcal C(A/(h+1))>0`.  The former notation `C(A/(h+1))` was locally
undefined because `C` had already been fixed as the scalar `F(0)`; this was
a notation defect only.

The other endpoint `x=1/[2(h-1)]` satisfies `(h-1)a=A/2` and is included in
the previously proved endpoint-period subrange.  Neither endpoint is used
inside the open Euclidean chamber.

## 3. Integer Euclidean chamber and empty-block audit

The open band is equivalent to

\[
h+1<{1\over x}<2(h-1).
\]

With

\[
{1\over x}=2m+\lambda,
\quad m=\left\lfloor{1\over2x}\right\rfloor,
\quad0\le\lambda<2,
\]

and `n=h-1-m`, `k=m-n=2m-h+1`, one obtains

\[
m\ge2,
\qquad m\le h-2,
\qquad n\ge1,
\qquad k+\lambda={1\over x}-h+1>2.
\]

Since `lambda<2`, `k>=1`; since `n>=1`, `k<=m-1`.  Hence the reflected
block `j=k,...,m-1` is nonempty and has exactly

\[
m-k=n
\]

terms.  The positive integer block `i=2,...,m` is also nonempty.  Thus no
empty sum is being assigned a positive length in the proof.

The endpoint at which `n=0` can occur is the excluded lower endpoint and
has already been closed separately.  The cases `lambda=0` and `lambda=1`
are harmless: in the decomposition `lambda=s+theta`, they have `theta=0`,
so the translation intervals degenerate and Lemma 2.1 holds with zero
translation loss.

## 4. Exact reflected-block identity

For `i<=m`, `ix<=1/2`.  For `i=m+1,...,h-1`, reflection gives

\[
F(Aix)=\rho(Aix)-F(A(1-ix)),
\]

and

\[
1-ix=(2m+\lambda-i)x.
\]

As `i` decreases from `h-1` to `m+1`, the new integer index
`j=2m-i` increases from

\[
2m-h+1=k
\quad\hbox{to}\quad
m-1.
\]

Thus the reflected compact arguments are exactly
`(j+lambda)x`, `j=k,...,m-1`.  Pairing the original `F(Ax)` with
`F(A-Ax)` contributes `rho(Ax)`.  This proves (1.6), including all signs,
indices, and the exact count `n+1` of rho terms.

Every argument used in the translation step lies in `[0,1/2]`:

* `mx<=1/2` by the definition of `m`;
* `(m-1+lambda)x<1/2` because `lambda<2` and
  `2m+lambda=1/x`;
* the lower indices are positive because `k>=1` and `k+lambda>2`.

## 5. One-mode translation lemma

The compact-train theorem says every interior critical point of `f` on
`[0,1/2]` is a strict local maximum.  Analyticity rules out an interval of
critical points.  Two distinct critical maxima would force a critical
minimum between them.  Hence there is at most one critical point, and `f`
is monotone or rises to one mode and then falls.

For a right translation by `0<=theta<1`, the intervals

\[
[jd,(j+\theta)d]
\]

have disjoint interiors.  Terms beginning at or after the mode do not
increase.  Before the mode, the sum of all positive increments, including
the possible unique interval crossing the mode, is at most the total rise
from the first grid point to the mode.  If that first point is before the
mode, monotonicity from zero gives `g(rd)>=g(0)`.  This proves the exact
bound `M-g(0)` in Lemma 2.1.  No convexity or unproved monotonicity of `F`
is being assumed.

Now write `lambda=s+theta`, with `s` in `{0,1}`.  The comparison block is

\[
k+s,\ldots,m-1+s.
\]

If `s=0`, `k+lambda>2` and `lambda<1` imply `k>=2`; if `s=1`, `k>=1`
implies `k+1>=2`.  Its final index is at most `m`.  Hence it is a literal
subblock of `{2,...,m}` in both cases.

The translated sum exceeds this comparison block by at most `M-C`, where
`M=sup f`.  Therefore

\[
S_h(a)\ge 2C-M+R_h(x)
       >2(43/1000)-61/1000+R_h(x)
       ={1\over40}+R_h(x).
\]

The strict `1/40` margin and its sign are correct.

## 6. Theta estimate and the cutoff 1000

There are `n` reflected rho terms plus `rho(Ax)`, hence exactly `n+1`
terms.  The strict theta estimate gives

\[
R_h(x)>-{n+1\over20000}.
\]

The upper inequality `x<1/(h+1)` gives

\[
{1\over2x}>{h+1\over2}.
\]

If `h=2s`, then `m>=s`; if `h=2s+1`, strictness over the integer `s+1`
gives `m>=s+1`.  Since `n+1=h-m`, both cases give

\[
n+1\le\lfloor h/2\rfloor.
\]

Consequently

\[
S_h(a)>{1\over40}-{\lfloor h/2\rfloor\over20000}.
\]

For `h<1000` the right side is positive.  At `h=1000` it is zero, but
both preceding inequalities are strict, so `S_h(a)>0` there as well.
Together with `Phi(W)>=S_h(a)`, this proves the claimed strict positivity
uniformly for `4<=h<=1000`.  This is one symbolic estimate, not a census of
the 997 periods.

## 7. Exact finite Dirichlet block and large-period scope

The phase block has the standard exact form

\[
\sum_{j=k}^{m-1}\cos(2\pi\ell(j+\lambda)x)
=
{\sin(\pi\ell n x)\over\sin(\pi\ell x)}
\cos\left(2\pi\ell x
\left(\lambda+{k+m-1\over2}\right)\right),
\]

with continuous interpretation when the denominator vanishes.  This
verifies that (4.1) is one finite Dirichlet block for each theta mode; the
outer theta series remains infinite but superexponentially weighted.

The condition

\[
R_h(x)\ge-1/40
\]

is sufficient to close a given large-period clock.  It is not necessary:
the shifted-block estimate discarded nonnegative terms and the
endpoint-period expression is only a lower comparison to `Phi(W)`.  The
theorem was patched to say this explicitly.  Therefore it makes no
nonpositivity claim when the sufficient gate fails.

## 8. Corrections made during this audit

1. Replaced the undefined/overloaded endpoint notation
   `C(A/(h+1))` by the explicitly defined arithmetic train
   `mathcal C(A/(h+1))`.
2. Added the arithmetic all-ceiling dependency and its frozen hash.
3. Recorded that the Euclidean blocks are nonempty only on the open
   chamber and that the lower endpoint is handled separately.
4. Added the exact finite Dirichlet-kernel expression, including its
   removable denominator-zero case.
5. Narrowed the large-period wording from an implicit exact frontier to a
   sufficient proof route; failure of the gate is not a negative result.

None of these corrections changes the proof or conclusion for
`4<=h<=1000`.

## Final audit verdict

After these corrections, every algebraic identity, integer range,
translation estimate, strict constant margin, and endpoint case checks.
The theorem is safe to cite for:

\[
\Phi(W)>0
\quad
(4\le h\le1000,
\ A/[2(h-1)]<a<A/(h+1)),
\]

and for the displayed sufficient theta/Dirichlet gate at larger periods.
It is not an all-period closure and does not imply Bellman positivity or an
OR-word upper bound.
