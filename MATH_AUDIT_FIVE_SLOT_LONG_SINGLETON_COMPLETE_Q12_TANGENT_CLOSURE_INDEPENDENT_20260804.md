# Independent audit: complete `q=1,2` tangent closure of the five-slot long-singleton gate

**Date:** 2026-08-04  
**Verdict:** **GO**.  The theorem is correct as written.  Its domain map,
derivative reduction, joint-convexity argument, exact Taylor boxes, tangent
arithmetic, and boundary transport all pass an independent proof audit.
No numerical sampling, interval mesh, or search is used here.

## 1. Frozen inputs

This audit binds the following exact files.

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_FIVE_SLOT_LONG_SINGLETON_COMPLETE_Q12_TANGENT_CLOSURE_20260804.md` | `19f8a5a23cca1963e1914da28f609a56c9247f89422ee407e8e3aaa696654927` |
| `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_PURE_LATTICE_Q12_CONVEX_ONE_DIMENSIONAL_GATE_20260804.md` | `aabfd99e588999b4011a12b81565bc441446925bae16255adb0750b391c2559c` |
| `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |

## 2. Domain and derivative audit

Write

\[
 t=p/A,qquad \alpha=a/A,qquad r=1-t,qquad s=r-\alpha.
\]

Then

\[
 p<A-a\iff s>0,qquad
 p>A-2a\iff s<r/2,qquad
 p\ge 3a\iff s\ge(4r-1)/3.
\]

The last two inequalities imply `r<2/5`; conversely they imply
`alpha=r-s<1/4` (trivially for `r<=1/4`, and from
`r-s<=(1-r)/3<1/4` for `r>1/4`).  Thus the compact-coordinate domain in
the dependency is exact up to the harmless closure of a strict boundary,
and it lies inside

\[
                  0\le r\le2/5,qquad0\le s\le1/5.
\]

The three normalized `q=1` arguments are

\[
 1-r,qquad1-s,qquad1+r-2s,
\]

and the three `q=2` arguments are

\[
 2-2r,qquad2-r-s,qquad2-2s.
\]

Substitution in the two exact formulas for `K'(Au)/(2A)` reproduces
every term and coefficient in the displayed function `B(r,s)`.  Since
`p/A=1-r>3/5`, every omitted `q>=3` argument is larger than one, so every
omitted derivative term is strictly positive.  Hence the strict
derivative lower bound is correctly directed.

## 3. Joint convexity audit

The sign change of

\[
 h''(x)=2cx(2cx^2-3)e^{-cx^2}
\]

is exactly at `sqrt(6/pi)`.  The adverse arguments `r,s` lie below that
point, so `-h(r)` and `-h(s)` are convex.  Every positive argument is at
least `8/5`, and

\[
 (8/5)^2>6/\pi
\]

already follows from `pi>3`.  Therefore every positive affine composite
is convex.  Summing proves joint convexity of `B` on the whole ambient
rectangle; no monotonicity of the affine forms is needed.

## 4. Independent exact reconstruction of the Taylor table

Put

\[
 L={333\over106},\qquad U={355\over113},\qquad
 u={\pi x^2\over4}.
\]

For every one of the eight listed arguments, `0<u<6`; at the largest
argument this follows exactly from

\[
 {355\over113}{(19/7)^2\over4}
 ={128155\over22148}<6.
\]

For rational `z` define

\[
 S(z)=\sum_{j=0}^{24}{z^j\over j!},\qquad
 T(z)=S(z)+{z^{25}\over25!}{1\over1-z/26}.
\]

The positive exponential series and the ratio bound on its tail give
`S(z)<e^z<T(z)` for `0<z<6`.  Consequently, with

\[
 u_-={Lx^2\over4},\qquad u_+={Ux^2\over4},
\]

one has the dependency-safe enclosure

\[
 {1\over T(u_+)}<e^{-u}<{1\over S(u_-)}.                 \tag{4.1}
\]

For `h'(x)=e^{-u}(1-2u)`, I did **not** reuse a point estimate or assume
an unproved monotonic direction.  I combined (4.1) with

\[
 1-2u_+<1-2u<1-2u_-
\]

and took the minimum and maximum of all four endpoint products.  Thus
negative factors are automatically reversed correctly.

Clearing the positive rational denominators in `S`, `T`, and the four
endpoint products gives the following independent, strictly enclosing
rational boxes.  The entries are numerators in units of `10^-6`.

\[
\begin{array}{c|cc}
 x&10^6h(x)&10^6h'(x)\\ \hline
58/35 &(191722,191734)&(-383389,-383352)\\
12/35 &(312620,312622)&(743444,743452)\\
13/7  &(123713,123723)&(-294304,-294272)\\
1/7   &(140585,140586)&(952551,952554)\\
72/35 &(74098,74106)&(-203437,-203412)\\
81/35 &(34478,34483)&(-110453,-110436)\\
88/35 &(17544,17547)&(-62322,-62311)\\
19/7  &(8330,8333)&(-32456,-32449)
\end{array}
\]

These boxes are obtained solely by integer comparison after denominator
clearing.  Each is strictly contained in the corresponding `10^-4` box
in the theorem.  Hence all sixteen entries of the theorem's Taylor table
are independently certified, including every negative `h'` entry.

## 5. Value, gradient, and tangent arithmetic

At `(r_0,s_0)=(12/35,1/7)`, the eight affine arguments are exactly

\[
 58/35,\ 12/35,\ 13/7,\ 1/7,\ 72/35,\ 81/35,\ 88/35,\ 19/7.
\]

Using the audited boxes, the positive value numerator is

\[
 1917+1237+740+2(344)+2(175)+2(83)=5098,
\]

whereas the adverse upper numerator is `3127+1406=4533`.  Therefore

\[
 B(r_0,s_0)>565/10000>1/20.
\]

Differentiation independently reproduces

\[
\begin{aligned}
B_r={}&-h'(2-r)-h'(r)+h'(2+r-2s)
       -4h'(3-2r)-2h'(3-r-s),\\
B_s={}&-h'(2-s)-h'(s)-2h'(2+r-2s)
       -2h'(3-r-s)-4h'(3-2s).
\end{aligned}
\]

The exact interval sums are

\[
25<10^4B_r<34,
\qquad
26<10^4B_s<37.
\]

In particular both slopes are positive and less than `1/100`.  Joint
convexity makes the tangent plane a global lower support.  Its smallest
allowed correction over the ambient rectangle occurs at `(0,0)`, so

\[
 B(r,s)>{1\over20}-{1\over100}
   \left({12\over35}+{1\over7}\right)
 ={79\over1750}>0.
\]

The theorem's uniform positivity and strict period monotonicity follow.

## 6. Boundary transport

For fixed `a`, the lower endpoint is

\[
 p_-(a)=\max\{3a,A-2a\}.
\]

If `a>=A/5`, then `p_-=3a`, and the three residue classes in
`L_3(3a;a,2a)` partition the nonnegative integer multiples of `a`;
hence `P(3a,a)=C(a)>0`.  If `a<=A/5`, then `p_-=A-2a`; equivalently the
right offset satisfies `p+2a=A`, so the bound theorem's cited
threshold-endpoint result applies (also as the closed boundary of the
delayed-`b` theorem).  Continuity plus the strict positive period
derivative transports either positive boundary value through the whole
open interval `p_-<p<A-a`.

Finally, the audited delayed-`b` concavity theorem takes the minimum of
the already-positive threshold endpoint and this now-positive pure
lattice.  Therefore the claimed closure of the retained three-pulse
gate is also correctly inherited.

## 7. Scope verdict

**GO:** the bound theorem proves the complete long-singleton gate and,
through the cited concavity reduction, the retained three-pulse gate.
It does not close the separate repeated-gap/short-singleton gate and does
not by itself establish complete five-slot or all-grid Bellman
positivity.
