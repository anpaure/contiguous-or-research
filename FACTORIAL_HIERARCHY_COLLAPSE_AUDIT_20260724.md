# Audit: the normalized factorial hierarchy collapses to `r=2`

## Verdict

The factorial collision inequality is valid, but the proposed minimization
over orders `r` does not strengthen its quadratic member.  For every load
vector and every admissible `r>=2`, the normalized balanced factorial excess
is at least the normalized pair excess.  Consequently

\[
 \min_{2\le r\le c+1}
 \left\lfloor
 \frac{F_r-\Phi_r}{(r-1){c+1\choose r}}
 \right\rfloor
 =
 \left\lfloor
 \frac{F_2-\Phi_2}{{c+1\choose2}}
 \right\rfloor .
\]

The `r=2` expression is exactly the previously recorded floor-corrected
quadratic-energy hole bound.  The hybrid minimum with balanced overload can
still be strictly better than overload alone, but higher factorial moments
add no further improvement.

## 1. Pointwise comparison

Fix integers `c>=1` and `2<=r<=c+1`.  For an integer `x>=0`, put

\[
 g_r(x)={x\choose r}-{c\choose r}-(x-c){c\choose r-1}.
\]

If `T=cN+rho` and `x_1+...+x_N=T`, then the balanced-floor identity is

\[
 F_r-\Phi_r=\sum_{i=1}^N g_r(x_i).
\]

Moreover

\[
 g_r(0)=(r-1){c+1\choose r},
 \qquad
 g_2(0)={c+1\choose2}.
\]

The key inequality is

\[
 \boxed{
 \frac{g_r(x)}{(r-1){c+1\choose r}}
 \ge
 \frac{g_2(x)}{{c+1\choose2}}
 }
 \tag{1}
\]

for every integer `x>=0`.

### Proof for `x>=c`

Let

\[
 w(x)=
 \frac{g_r(x)}{(r-1){c+1\choose r}}
 -
 \frac{g_2(x)}{{c+1\choose2}}.
\]

The forward second difference is

\[
 \Delta^2w(x)=
 \frac{{x\choose r-2}}{(r-1){c+1\choose r}}
 -\frac{2}{c(c+1)}.
\]

At `x=c`, the first term is at least the second because

\[
 \frac{{c\choose r-2}}{(r-1){c+1\choose r}}
 =\frac{r}{(c+1)(c-r+2)}
 \ge\frac{2}{c(c+1)},
\]

the last inequality being equivalent to
`(r-2)(c+2)>=0`.  Since the binomial coefficient is nondecreasing in
`x`, `Delta^2 w(x)>=0` for all `x>=c`.  Finally `w(c)=w(c+1)=0`, so
discrete convexity gives `w(x)>=0` for all `x>=c`.

### Proof for `0<=x<=c`

Again `w(0)=w(c)=w(c+1)=0`.  Write

\[
 d_x=w(x+1)-w(x),\qquad 0\le x\le c.
\]

Because `Delta^2 w(x)` is nondecreasing in `x`, the finite sequence
`d_0,...,d_c` is convex.  Directly,

\[
 d_0=w(1)=
 \frac{2}{c+1}-\frac{r}{(r-1)(c+1)}
 =\frac{r-2}{(r-1)(c+1)}\ge0,
\]

while `d_c=0` and

\[
 \sum_{x=0}^{c-1}d_x=w(c)-w(0)=0.
\]

A convex finite sequence with `d_0>=0`, `d_c=0`, and zero sum over
`d_0,...,d_(c-1)` has a (possibly empty) nonnegative prefix followed by a
nonpositive suffix.  Indeed, after it becomes nonpositive it cannot become
positive before the terminal zero: once `d_j<=0`, convexity places every
later `d_k` below the chord from `(j,d_j)` to `(c,0)`, hence `d_k<=0`.
Its partial sums therefore
first increase and then decrease to zero, and are never negative.  Hence

\[
 w(x)=\sum_{j=0}^{x-1}d_j\ge0
 \qquad(0\le x\le c).
\]

This completes the proof of (1).

## 2. Consequences for load vectors

Summing (1) over the coordinates gives

\[
 \frac{F_r-\Phi_r}{(r-1){c+1\choose r}}
 \ge
 \frac{F_2-\Phi_2}{{c+1\choose2}}.
 \tag{2}
\]

Taking floors preserves the inequality.  Thus the best factorial bound is
always attained at `r=2`; there is no load profile for which `r>=3` gives a
smaller certified hole count.

Also

\[
 2(F_2-\Phi_2)
 =\sum_i(x_i-T/N)^2-\frac{\rho(N-\rho)}N,
\]

so (2) identifies the surviving factorial gate exactly with the earlier
floor-corrected quadratic gate.

For a wreath factor this means

\[
 K_q=K_{q,2}
 =\left\lfloor
 \frac{\Delta_{q,2}}{{c_q+1\choose2}}
 \right\rfloor,
\]

and the proposed hybrid statistic simplifies to

\[
 J_q=
 \min\left\{
 \left\lfloor\frac{O_q}{c_q}\right\rfloor,
 \left\lfloor
 \frac{\Delta_{q,2}}{{c_q+1\choose2}}
 \right\rfloor
 \right\}.
\]

The exact wreath/reservoir transfer remains valid with this simplified
quantity.  What remains open is still construction of a common exact factor
whose balanced overload or, equivalently for the moment lane, quadratic
excess is small through the mesoscopic depth range.

## 3. Finite check

As a regression check, (1) was evaluated exactly with integer arithmetic for
all `1<=c<=100`, all `2<=r<=c+1`, and all `0<=x<=300`; no counterexample
occurred.  The proof above is independent of this finite check.
