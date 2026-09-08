# Long-wrap train: outer-period closure and a compact theta core

**Date:** 2026-08-04
**Status:** unconditional pure-mathematical reduction.  It proves the sole
remaining chamber-II long-wrap train positive for

\[
 {A\over2}\le P\le {4A\over5}
 \qquad\text{and}\qquad
 {11A\over12}\le P<A.
\]

It reduces every possible counterexample to one normalized theta curve in
the fixed bounded band `4/5<P/A<11/12`, whose closure is compact.  It does
**not** sign that final
curve and therefore does not close chamber II, chamber I, six-slot
positivity, or an OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad h(x)=xe^{-\pi x^2/4},
 \qquad F_P(w)=\sum_{q\ge0}K(qP+w),
\tag{0.1}
\]

and

\[
 Q_P(a)=C(P)+F_P(a)+F_P(2a),
 \qquad C(P)=F_P(0).
\tag{0.2}
\]

The exact remaining domain is

\[
 {A\over2}<P<A,qquad
 0<a<m(P):=\min\left\{{P\over3},{A-P\over2}\right\}.
\tag{0.3}
\]

All four outer faces are already positive.  The frozen KKT reduction also
proves that an actual counterexample must satisfy

\[
 F_P'(a)\le0\le F_P'(2a),
 \qquad F_P'(a)+2F_P'(2a)=0,
\tag{0.4}
\]

and the period derivative must vanish.

Normalize

\[
                         \rho={P\over A},\qquad x={w\over A}.
\tag{0.5}
\]

On `0<=x<=1-rho`, the exact derivative is

\[
 {F_P'(Ax)\over2A}=T_\rho(x),
\tag{0.6}
\]

where

\[
 \boxed{
 T_\rho(x)=\sum_{q\ge0}h(1+x+q\rho)
              -h(1-x)-h(1-\rho-x).}
\tag{0.7}
\]

The frozen theorem proves that `x -> T_rho(x)` is strictly convex.

Every exponential estimate below is an exact rational certificate.  For
rational `t>=0`, put

\[
 S_N(t)=\sum_{k=0}^N{t^k\over k!},
 \qquad
 E_N(t)=S_N(t)+{t^{N+1}\over(N+1)!}
                    {1\over1-t/(N+2)}.
\tag{0.8}
\]

When `0<t<N+2`, the positive exponential series and its geometric tail give

\[
                         S_N(t)<e^t<E_N(t).
\tag{0.9}
\]

All comparisons involving `S_N,E_N` below are finite rational
inequalities; they may be checked by clearing positive denominators.  We
also use

\[
                         e>S_5(1)={163\over60}>{19\over7}.
\tag{0.10}
\]

## 1. The origin slope is negative through `rho=4/5`

At the origin,

\[
 T_\rho(0)=\sum_{q\ge1}h(1+q\rho)-h(1-\rho).
\tag{1.1}
\]

### Lemma 1.1

For

\[
                         {1\over2}\le\rho\le{4\over5},
\]

one has

\[
                         \boxed{T_\rho(0)<0.}
\tag{1.2}
\]

### Proof

The ratio of the first positive term in (1.1) to the adverse term is

\[
 R_0(\rho)={1+\rho\over1-\rho}e^{-\pi\rho}.
\tag{1.3}
\]

On `[1/2,3/5]`, its logarithmic derivative

\[
 {2\over1-\rho^2}-\pi
\]

is negative.  Hence

\[
 R_0(\rho)\le3e^{-\pi/2}<{5\over8}.
\tag{1.4}
\]

The last inequality is equivalent to `e^(pi/2)>24/5`; it follows from
`pi>157/50` and the exact comparison

\[
                         S_6(157/100)>{24\over5}.
\tag{1.4a}
\]

For successive positive terms, put `z=1+q*rho`.  Then

\[
 {h(z+\rho)\over h(z)}
 =\left(1+{\rho\over z}\right)
 e^{-(\pi/4)(2z\rho+\rho^2)}.
\tag{1.5}
\]

On `[1/2,3/5]` this is less than `3/8`: the prefactor is at most
`11/8`, while the exponential is at most `e^(-7pi/16)`, and the rational
Taylor inequality

\[
                         {11\over8}e^{-7\pi/16}<{3\over8}
\tag{1.6}
\]

follows from `pi>3`, `e>19/7`, and the positive degree-four series for
`e^(5/16)`.  Explicitly,

\[
 e^{7\pi/16}>e^{21/16}
 >{19\over7}S_4(5/16)>{11\over3}.
\tag{1.6a}
\]

Thus the whole positive tail is at most `8/5` times its
first term, and (1.4) proves (1.2) on this interval.

Now take `3/5<=rho<=4/5`.  The logarithm of (1.3) has increasing
derivative and therefore its maximum on this interval is at an endpoint.
Exact endpoint bounds give

\[
 4e^{-3\pi/5}<{3\over4},
 \qquad
 9e^{-4\pi/5}<{3\over4}.
\tag{1.7}
\]

They follow from the finite rational comparisons

\[
 S_6(9/5)>{16\over3},
 \qquad
 S_8(314/125)>12,
\tag{1.7a}
\]

using respectively `3pi/5>9/5` and
`4pi/5>314/125`.  In (1.5), the
prefactor is now at most `13/9`, while

\[
 2z\rho+\rho^2\ge {57\over25}.
\]

The exact comparison

\[
                         S_8(8949/5000)>{52\over9},
\tag{1.8a}
\]

together with `57pi/100>8949/5000`, gives

\[
 {13\over9}e^{-57\pi/100}<{1\over4}.
\tag{1.8}
\]

Hence the complete tail is at most `4/3` times its first term, and
(1.7) again makes it strictly smaller than `h(1-rho)`.  This proves
(1.2).  \(\square\)

## 2. Closure through `rho=3/5`

Suppose first that

\[
                         {1\over2}\le\rho\le{3\over5}.
\tag{2.1}
\]

Then `m(P)=P/3`.  Put

\[
                         G_P(a)=Q_P'(a)
 =F_P'(a)+2F_P'(2a).
\tag{2.2}
\]

The frozen reduction proves that `G_P` is strictly convex.  Lemma 1.1
gives

\[
                         G_P(0)=3F_P'(0)<0.
\tag{2.3}
\]

At the other endpoint, the shift-train theorem gives

\[
 F_P'(P/3)<0,
 \qquad F_P'(2P/3)<0,
\]

and hence

\[
                         G_P(P/3)<0.
\tag{2.4}
\]

A convex function lies below the chord between its endpoint values, so
`G_P<0` throughout.  Thus `Q_P` decreases to its arithmetic endpoint:

\[
 \boxed{Q_P(a)\ge Q_P(P/3)=C(P/3)>0.}
\tag{2.5}
\]

## 3. Closure from `rho=3/5` through `rho=4/5`

For

\[
                         {3\over5}\le\rho\le{3\over4},
\tag{3.1}
\]

put `r=1-rho`.  The point `w=Ar=A-P` obeys

\[
                         {P\over3}\le A-P\le{2P\over3}.
\]

The shift-train theorem therefore gives `F_P'(A-P)<0`, while Lemma 1.1
gives `F_P'(0)<0`.  Strict convexity of `F_P'` yields

\[
                         F_P'(w)<0\qquad(0\le w\le A-P).
\tag{3.2}
\]

It remains to extend the endpoint sign to `rho=4/5`.  Define

\[
 U(\rho):=T_\rho(1-\rho)
 =h(2-\rho)-h(\rho)+\sum_{n\ge0}h(2+n\rho).
\tag{3.3}
\]

### Lemma 3.1

On `[3/4,4/5]`,

\[
                         U(\rho)<0.
\tag{3.4}
\]

### Proof

Differentiate (3.3):

\[
 U'(\rho)=-h'(2-\rho)-h'(\rho)
              +\sum_{n\ge1}n h'(2+n\rho).
\tag{3.5}
\]

On this interval, exact one-variable bounds give

\[
 -h'(2-\rho)>{2\over5},qquad
 -h'(\rho)>-{1\over10},qquad
 \sum_{n\ge1}n h'(2+n\rho)>-{1\over20}.
\tag{3.6}
\]

For the first two, use the sign formula

\[
 h'(z)=e^{-\pi z^2/4}(1-\pi z^2/2)
\]

and its monotonicity on the displayed compact intervals.

For the first term, `-h'` is increasing on `[6/5,5/4]`.  At `6/5`,

\[
 -h'(6/5)=e^{-9\pi/25}\left({18\pi\over25}-1\right).
\]

The exact inequalities

\[
 E_8(198/175)<{25\over8},
 \qquad
 {18\pi\over25}-1>{5\over4}
\tag{3.6a}
\]

follow from `pi<22/7` and `pi>157/50`; hence
`-h'(6/5)>(8/25)(5/4)=2/5`.

For the second term, `-h'` is increasing on `[3/4,4/5]`.  At the left
endpoint,

\[
 h'(3/4)=e^{-9\pi/64}\left(1-{9\pi\over32}\right)
 <{64\over91}{1\over8}={8\over91}<{1\over10}.
\tag{3.6b}
\]

Here `pi>157/50>28/9` bounds the last factor by `1/8`, while
`pi>3` and `e^(27/64)>1+27/64=91/64` bound the exponential.

For the weighted tail, write

\[
 H(z)=-h'(z)=e^{-\pi z^2/4}\left({\pi z^2\over2}-1\right),
 \qquad a_n=nH(2+n\rho).
\]

Since `rho>=3/4` and `H` is decreasing for `z>=11/4`,

\[
 a_1\le H(11/4)<{1\over32}.
\tag{3.6c}
\]

Indeed the polynomial factor is smaller than `1219/112`, while
`121pi/64>95/16`; and

\[
 \left({19\over7}\right)^5S_4(15/16)>{2438\over7}
\]

proves `e^(95/16)>32(1219/112)`.  For `n>=1`, putting
`z=2+n rho` gives

\[
 {a_{n+1}\over a_n}
 <{20\over9}\left({71\over55}\right)^2e^{-75\pi/64}
 <{1\over10}.
\tag{3.6d}
\]

The polynomial ratio uses
`pi z^2/2>10`, `z>=11/4`, and `rho<=4/5`.  For the final exponential
comparison, `75pi/64>11/3` and

\[
 \left({19\over7}\right)^3S_4(2/3)
 >{200\over9}\left({71\over55}\right)^2.
\]

Consequently

\[
 -\sum_{n\ge1}n h'(2+n\rho)
 =\sum_{n\ge1}a_n
 <{1/32\over1-1/10}={5\over144}<{1\over20}.
\tag{3.6e}
\]

This proves all three inequalities in (3.6), and their strict sum gives
`U'>1/4`.  Notice that the formerly quoted sharper bound
`-h'(rho)>-39/1000` is false at `rho=3/4`; it is neither used nor needed.

At the right endpoint, use the exact rational bounds

\[
 \begin{aligned}
 h(6/5)&<{97\over250},&
 h(4/5)&>{2419\over5000},\\
 h(2)&<{173\over2000},&
 h(14/5)&<{3\over500}.
 \end{aligned}
\tag{3.7a}
\]

They follow respectively from

\[
 \begin{gathered}
 S_6(1413/1250)>{300\over97},
 \qquad E_6(88/175)<{4000\over2419},\\
 S_{12}(333/106)>{4000\over173},
 \qquad S_{14}(16317/2650)>{1400\over3}.
 \end{gathered}
\tag{3.7b}
\]

Here the four exponent comparisons use, in order,
`pi>157/50`, `pi<22/7`, and `pi>333/106` for the final two rows.

For the omitted positive tail, its first ratio from `14/5` is less than
`1/40`, and every subsequent ratio is less than `1/100`.  Indeed

\[
 S_7(4)>{360\over7},
 \qquad
 S_8(5)>{1100\over9},
\tag{3.7c}
\]

while the corresponding exponent gaps exceed `4` and `5`.  Therefore

\[
 \sum_{n\ge2}h(2+4n/5)
 <{3\over500}{1/40\over1-1/100}
 ={1\over6600}<{1\over6000}.
\tag{3.7d}
\]

It follows that

\[
\begin{aligned}
 U(4/5)
 &=h(6/5)-h(4/5)+h(2)+h(14/5)
      +\sum_{n\ge2}h(2+4n/5)\\
 &<-{1\over500}.
\end{aligned}
\tag{3.7}
\]

Indeed the displayed upper bound is exactly

\[
 {97\over250}-{2419\over5000}+{173\over2000}
       +{3\over500}+{1\over6000}
 =-{47\over15000}<-{1\over500}.
\tag{3.7e}
\]

Since `U` is increasing, (3.7) proves (3.4).  \(\square\)

Lemmas 1.1 and 3.1, together with strict convexity, prove (3.2) on the
larger interval `3/5<=rho<=4/5`.  In this range `m(P)=(A-P)/2`; hence

\[
 Q_P'(a)=F_P'(a)+2F_P'(2a)<0
 \qquad(0\le a\le m(P)).
\]

The train decreases to the already-positive threshold face:

\[
 \boxed{Q_P(a)\ge Q_P((A-P)/2)>0.}
\tag{3.8}
\]

Combining Sections 2--3 proves

\[
                         \boxed{Q_P(a)>0\quad(P\le4A/5).}
\tag{3.9}
\]

## 4. A positive upper-period region

### Lemma 4.1

If

\[
                         {11A\over12}\le P<A,
 \qquad0\le w\le A-P,
\]

then

\[
                         \boxed{F_P'(w)>0.}
\tag{4.1}
\]

### Proof

Put `rho=P/A`, `r=1-rho<=1/12`, and `x=w/A<=r`.  From (0.7), retain
only the `q=0,1` positive train terms:

\[
 T_\rho(x)
 >D(x)+h(2-r+x)-h(r-x),
\tag{4.2}
\]

where `D(x)=h(1+x)-h(1-x)`.

On `[1-r,1+r]`, one has `h'(z)>-1/2`.  Indeed `h'` decreases there, and

\[
 -h'(13/12)
 =e^{-169\pi/576}\left({169\pi\over288}-1\right)
 <{18\over49}<{1\over2};
\]

the first inequality follows from `pi<22/7`, `pi>3`, and the exact
rational comparison

\[
 S_3(169/192)>{851\over1008}{49\over18}.
\tag{4.2a}
\]

Indeed the polynomial factor is at most `851/1008`, while the Gaussian
exponent is larger than `169/192`.  Therefore

\[
                         D(x)\ge-x.
\tag{4.3}
\]

Also `h` is decreasing on `[2-r,2]`, so

\[
 h(2-r+x)\ge h(2)=2e^{-\pi},
 \qquad h(r-x)\le r-x.
\]

Consequently

\[
 T_\rho(x)>2e^{-\pi}-r>2e^{-\pi}-{1\over12}>0.
\tag{4.4}
\]

The last inequality is equivalent to `e^pi<24`.  It follows from
`pi<22/7` and the exact rational upper bounds

\[
 E_8(3)<{201\over10},
 \qquad
 E_3(1/7)<{7\over6}.
\tag{4.4a}
\]

Their product is `1407/60<24`.  This proves (4.1).  \(\square\)

It follows immediately that

\[
 Q_P'(a)=F_P'(a)+2F_P'(2a)>0
\]

on the complete admissible interval.  Therefore

\[
 \boxed{Q_P(a)\ge Q_P(0)=3C(P)>0
       \qquad(P\ge11A/12).}
\tag{4.5}
\]

## 5. The remaining normalized theta core

Every possible nonpositive long-wrap value is now confined to

\[
 \boxed{
 {4\over5}<\rho<{11\over12},qquad
 0<x<{1-\rho\over2}.}
\tag{5.1}
\]

For each fixed `rho`, strict convexity of `Q_P'` leaves at most one
interior local-minimum root `x_*(rho)`.  Whenever it exists, it necessarily
satisfies

\[
 \boxed{
 T_\rho(x_*)+2T_\rho(2x_*)=0,qquad
 T_\rho'(x_*)+4T_\rho'(2x_*)\ge0.}
\tag{5.2}
\]

The full KKT filters add

\[
 T_\rho(x_*)\le0\le T_\rho(2x_*),
\tag{5.3}
\]

and the normalized period equation

\[
\boxed{
 \mathcal R(\rho,x_*):=
 \sum_{q\ge1}q\bigl\{
  \kappa(q\rho)+\kappa(q\rho+x_*)
                   +\kappa(q\rho+2x_*)\bigr\}=0,}
\tag{5.4}
\]

where

\[
 \kappa(u)={K'(Au)\over2A}
 =\begin{cases}
 h(1+u)-h(1-u),&0\le u\le1,\\
 h(1+u),&u\ge1.
 \end{cases}
\tag{5.5}
\]

Thus the remaining sign problem is the single explicit normalized theta
function

\[
\boxed{
 \mathcal Z(\rho)=
 {Q_{A\rho}(Ax_*(\rho))},
 \qquad {4\over5}<\rho<{11\over12},}
\tag{5.6}
\]

only at those `rho` for which this local-minimum root exists and
(5.2)--(5.4) hold.  Positivity of
`mathcal Z` on this bounded KKT locus closes the long-wrap family and,
through the frozen reduction, all of chamber II.  This is strictly smaller
than the former curve: the intervals `[1/2,4/5]` and `[11/12,1)` have
been removed, and every surviving point carries both derivative signs plus
the period equation.

## 6. Exact scope and frozen dependencies

This theorem does not sign `mathcal Z`.  It proves no complete chamber,
six-slot, all-grid, integral-carrier, or OR-word result.

| role | file | SHA-256 |
|---|---|---|
| exact chamber-II KKT reduction | `MATH_THEOREM_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_ELIMINATION_AND_LONG_WRAP_CURVE_20260804.md` | `f5dbde2a817c6ab23ade7de5c0f0d691d80db4d4bb23865f9643959efa79c91b` |
| independent KKT audit | `MATH_AUDIT_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_AND_LONG_WRAP_CURVE_INDEPENDENT_20260804.md` | `3900b98672355272cf866659b4a5046f60b581604e18c91282e78e29d5f53d65` |
| density-tie shift theorem | `MATH_THEOREM_CHAMBER_I_SHIFT_TRAIN_BOUNDARIES_AND_SINGLE_PERIOD_STATIONARY_GATE_20260804.md` | `4a80c1bdf2e23d5b495799d41b7b30755d6500df509078cc2ec7bfdc8a134af9` |
| half-period train theorem | `MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md` | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
