# A sharp finite Gaussian estimate for the existing product-SCD exterior

Date: 2026-09-08. Independent audit by `exact_b_induction` of the user's
new exterior estimate. The general proof is pure mathematics. The single
specified numerical instance was certified by bounded exact arithmetic
through ssh h100; no floating-point estimate or broad search was used.

Status: all displayed finite inequalities and the rational comparison pass.
The literal exterior construction is the existing one; this note improves
its estimate and preserves its coverage and aperture conventions.

## 1. The exact length being bounded

Use the product-SCD construction in
`MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`,
Theorem 1.1, equations (1.3), (1.8), and Lemma 1.2.

For r>=1 and 0<=a<=floor(r/2), write

\[
 A_r(a)=\binom ra-\binom r{a-1},\qquad
 w_r(a)=\begin{cases}r,&a=0,\\r-2a+1,&a>0.\end{cases}
\]

For 1<=H<=r, the exact even-dimensional constructed length is

\[
 L_r(r-H)=\sum_{a+b\le r-H}
       A_r(a)A_r(b)(w_r(a)+w_r(b)),                     \tag{1.1}
\]

where both a,b range from zero through floor(r/2). The trimmed odd lift
has exactly twice this length. It covers every odd-dimensional target
of rank at most r-H or at least r+H+1. It can be concatenated with the
central word without additional joining letters.

Put W_r=binom(2r+1,r). This note bounds 2L_r(r-H)/W_r, not a different
cutoff such as L_r(r-H-1).

## 2. A finite chain-pair inequality and Vandermonde

For one pair set

\[
 q=r-a-b,\qquad x=r-2a+1,\qquad y=r-2b+1.
\]

Then x,y are positive, x+y=2(q+1), and

\[
 A_r(a)=\binom ra\frac{x}{r-a+1},\qquad w_r(a)\le x.
\]

The inequality for w includes a=0, where w=r=x-1. Also
r-a+1,r-b+1>=(r+2)/2. Therefore

\[
\begin{aligned}
 A_r(a)A_r(b)(w_r(a)+w_r(b))
 &\le\binom ra\binom rb
       \frac{xy(x+y)}{(r-a+1)(r-b+1)}\\
 &\le\frac{8(q+1)^3}{(r+2)^2}\binom ra\binom rb.       \tag{2.1}
\end{aligned}
\]

The last line uses xy<=(x+y)^2/4=(q+1)^2. Summing first over q and
enlarging the permitted nonnegative a,b to the full Vandermonde range
gives, with b_q=binom(2r,r-q),

\[
 \boxed{L_r(r-H)\le\frac8{(r+2)^2}
                    \sum_{q=H}^{r}(q+1)^3 b_q.}         \tag{2.2}
\]

Every term is nonnegative, so this enlargement requires no parity or
endpoint approximation.

## 3. The exact cubic telescoping identity

Define b_(r+1)=0 and

\[
                 F_r(q)=\frac{(r+q)(q^2-q+r)}2.
\]

Since b_(q+1)/b_q=(r-q)/(r+q+1), direct cancellation gives

\[
\begin{aligned}
 F_r(q)b_q-F_r(q+1)b_{q+1}
 &=\frac{b_q}{2}\big[(r+q)(q^2-q+r)
                     -(r-q)(q^2+q+r)\big]\\
 &=q^3b_q.                                             \tag{3.1}
\end{aligned}
\]

This holds also at q=r, where the second term vanishes. Consequently

\[
                 \sum_{q=H}^{r}q^3b_q=F_r(H)b_H.
\]

For q>=H>=1, (q+1)^3<=(1+1/H)^3q^3. Substitute into (2.2), and use
W_r=(2r+1)b_0/(r+1). This proves the exact finite bound

\[
 \boxed{\frac{2L_r(r-H)}{W_r}
       \le\Theta(r,H)\frac{b_H}{b_0},}                 \tag{3.2}
\]

where

\[
 \Theta(r,H)=
 \frac{8(r+1)(r+H)(H^2-H+r)}{(2r+1)(r+2)^2}
                   \left(1+\frac1H\right)^3.           \tag{3.3}
\]

## 4. The factor 32, including H=1 and r=1

For H>=2,

\[
 \frac{(r+1)(r+H)}{(2r+1)(r+2)}\le1,
 \qquad \frac{H^2-H+r}{r+2}\le1+\frac{H^2}{r},
 \qquad (1+1/H)^3\le27/8.
\]

The first inequality follows from H<=r and
(2r+1)(r+2)-2r(r+1)=3r+2>0. Thus
Theta(r,H)<=27(1+H^2/r) in this case.

For H=1, (3.3) simplifies to

\[
 \Theta(r,1)=\frac{64r(r+1)^2}{(2r+1)(r+2)^2}<32.
\]

Indeed
(2r+1)(r+2)^2-2r(r+1)^2=5r^2+10r+4>0. This includes r=1.
Hence for the entire finite domain,

\[
             \boxed{\Theta(r,H)\le32(1+H^2/r).}          \tag{4.1}
\]

There is no excluded small-r or one-step case.

## 5. The centered binomial ratio has the claimed exponent

Write N=r+1/2. For 1<=j<=H<=r,

\[
 \frac{r-j+1}{r+j}
     =\frac{1-z_j}{1+z_j},\qquad
 z_j=\frac{j-1/2}{r+1/2}\in(0,1).
\]

The elementary inequality log((1-z)/(1+z))<=-2z follows by
differentiation or by its convergent odd-power series. Since
sum_(j=1)^H(j-1/2)=H^2/2, the exact ratio product implies

\[
 \boxed{\frac{b_H}{b_0}\le
                   \exp\left(-\frac{H^2}{r+1/2}\right).} \tag{5.1}
\]

Combining (3.2), (4.1), and (5.1) gives

\[
 \boxed{\frac{2L_r(r-H)}{W_r}
      \le32\left(1+\frac{H^2}{r}\right)
                 \exp\left(-\frac{H^2}{r+1/2}\right),
             \quad r\ge1, 1\le H\le r.}               \tag{5.2}
\]

## 6. The prescribed aperture and a numerical uniform constant

Let r>=16, c>=0, c^2<=log log r, and set

\[
                         H=\lfloor c\sqrt r\rfloor+1.
\]

Then H>c sqrt(r) and H<=c sqrt(r)+1. Since
log log r<=log r<=r/4 on r>=16, this H lies in [1,r]. The prefactor obeys

\[
 1+H^2/r\le(1+c^2)(1+r^{-1/2}+r^{-1})
                        \le(21/16)(1+c^2).
\]

Here 2c<=1+c^2 was used before taking r>=16. The exponential obeys

\[
 \exp\left(-\frac{H^2}{r+1/2}\right)
 \le e^{-c^2}\exp\left(\frac{c^2}{2r+1}\right)
 \le e^{-c^2}e^{1/8}\le(8/7)e^{-c^2}.
\]

The last elementary bound follows from e^x<=1/(1-x), 0<=x<1.
Thus (5.2) yields the explicit uniform statement

\[
 \boxed{\frac{2L_r(r-H)}{W_r}
                   \le48(1+c^2)e^{-c^2}.}              \tag{6.1}
\]

In particular C=64 is also valid if a power-of-two constant is preferred.
The exponent is -c^2 at the actual aperture floor(c sqrt(r))+1; no
unrecorded cutoff shift or moderate-deviation approximation is used.

## 7. Exact rational certificate at r=1000, H=120

The bound (3.2), before replacing its ratio by an exponential, was
checked by exact rational arithmetic on h100. The result is

\[
 \Theta(1000,120)=\frac{4741891268114}{67804155135},
\]

and

\[
 \frac{37923376245}{10^{15}}
 \le\Theta(1000,120)
          \frac{\binom{2000}{880}}{\binom{2000}{1000}}
 <\frac{37923376246}{10^{15}}
 <\frac1{25000}.                                      \tag{7.1}
\]

Thus the normalized cost of this existing exterior word is strictly
less than 1/25000 at the specified parameters. The enclosed rational
quantity is an upper bound on that cost, not a claim of its exact value.

Artifacts:

* `scratch/verify_sharp_exterior_r1000_h120_20260908.py`;
* `scratch/sharp_exterior_r1000_h120_certificate_20260908.json`.

The captured run used integer binomial coefficients and `Fraction`,
with 10 CPU seconds, 15 wall seconds, and 256 MiB as explicit resource
caps. It finished successfully. No theorem in Sections 1-6 depends on
this numerical check.
