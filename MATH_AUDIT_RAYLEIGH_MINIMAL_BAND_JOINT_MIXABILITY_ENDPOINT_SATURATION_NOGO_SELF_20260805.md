# Self-audit: Rayleigh minimal-band joint-mixability endpoint no-go

**Date:** 2026-08-05  
**Method:** independent line-by-line mathematical replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_MINIMAL_BAND_JOINT_MIXABILITY_ENDPOINT_SATURATION_NOGO_20260805.md`  
**Verdict:** **GO.**  The result is a scoped no-go for the whole-band,
exact-minimum-piece Wang--Wang construction.  It is not a no-go for the
Rayleigh coagulation, a finer job disintegration, or the `n+1`-piece route.

## 1. Crossing and monotonicity

The crossing equation is

\[
 {\operatorname {arctanh}\theta\over\theta}={\pi\over2}.
\]

The ratio on the left is strictly increasing.  At `theta=1/2` it is
`log 3`, and `log 3<pi/2`; hence `theta>1/2` and `2c>A`.
Consequently every `I_n=((n-1)c,nc)` with `n>=3` lies in `(A,infinity)`.
There the residual job density is `j`, and

\[
 j'(x)=2e^{-(A+x)^2}(1-2(A+x)^2)<0
\]

because `A^2=pi/4>1/2`.  Thus its reflection is genuinely increasing, as
required by the chosen direction of the Wang--Wang theorem.

## 2. Support inequality

For the tuple `(Y_1,...,Y_m,-X_n)`, the negative job support is
`[-nc,-(n-1)c]`; its length is `c`.  Every socket support lies in `[0,c]`
and also has length at most `c`, so the maximum support length in the
Wang--Wang row is exactly `c`.  With center zero, the two sides become

\[
 \sum_i a_i-nc+c\le0,
 \qquad
 0\le\sum_i b_i-(n-1)c-c.
\]

These are precisely

\[
 \sum_i a_i\le(n-1)c,
 \qquad
 \sum_i b_i\ge nc.
\]

No mean term was dropped: constant sum zero separately forces
`sum_i E Y_i=E X_n`.

## 3. Endpoint contradiction

For `m=n`, `sum_i b_i>=nc` and `b_i<=c` force every `b_i=c`.
If a probability density is nondecreasing on `[a,c]`, the mean density on
its final `epsilon` interval is at least its mean density on the whole
support, so its final mass is at least `epsilon/(c-a)>=epsilon/c`.  This
also holds trivially if the support begins inside that final interval.

The band mass `w_n` is strictly positive.  Hence its `n` socket roles force
at least `n w_n epsilon/c` socket mass in `(c-epsilon,c)`.
The actual density `s-j` is continuous and equals zero at `c`, so its mass
there is `o(epsilon)`.  The two bounds are incompatible.  Domination by the
global residual socket measure is already impossible, so no interaction
with other bands can repair this particular decomposition.

## 4. Extra-piece row

For `m=n+1`, the same support algebra gives

\[
 \sum_i(c-b_i)\le c.
\]

Taking all upper endpoints `beta_n=nc/(n+1)` meets it with equality.  A
strictly decreasing law on `((n-1)c,nc)` has mean strictly below the
interval midpoint and above its lower endpoint.  Dividing by `n+1` places
the required socket mean strictly between `beta_n/2` and `beta_n`, so an
increasing density with this mean exists.  Thus the theorem correctly says
that the *local* Wang--Wang obstruction disappears with one extra role.

## 5. Scope check

The proof does not establish the global barycentric socket identity.  It
also does not treat the first residual band as one monotone job law, since
that density rises on `(c,A)` and falls after `A`.  No claim is made that
the Rayleigh count slack pays every forced extra role; the previously proved
strict ceiling inequalities are consistent with this no-go.  The theorem
therefore isolates, without overstating, the failure of the most direct
minimal-band mixability construction.

