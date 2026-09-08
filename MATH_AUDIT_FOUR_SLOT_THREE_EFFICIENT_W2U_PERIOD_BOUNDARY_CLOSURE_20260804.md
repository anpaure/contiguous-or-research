# Audit: complete closure of the three-efficient `w=2u` face

**Date:** 2026-08-04  
**Verdict:** **PASS.**  
**Method:** exact Bellman normal forms and symbolic Gaussian derivative
arguments only; no search, solver, H100, or floating-point sign decision was
used.

## 1. Audited theorem inputs

The proof uses only the following frozen results.

| role | SHA-256 |
|---|---|
| exact three-efficient pulse normal form and period theorem | `b620128fdefd9063099a6e1032c1685d155ba9aa95bab96b0e49612c11987faf` |
| independent audit of that theorem | `d6c4448561ea344f48a8a53b171420047695e6d312f218371d51706102d47327` |
| endpoint-`A` threshold train theorem | `7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b` |
| independent endpoint audit | `090494f7180f211752635415294b4fd5f341cded2362de9c46aaf19eb6aea1c4` |
| four-efficient Apéry scalar closure | `2b334fc6670ec73d4eba0f9de7a211b5e64f38a77f205ee822bebc4f3a79e776` |
| independent scalar audit | `4dc1f99d6626cd23130f08f56e9cc94d1458c5b253901636ee9e508d938b2bd5` |
| all-grid first-crossing/Apéry theorem | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| independent all-grid audit | `d404632e3bd805f92333276c74d3a094991da224f22259f11ba24193c0842173` |

## 2. Feasible period interval

On `w=2u`, the exact inherited inequalities include

\[
 x\le u,qquad y\le2u,qquad u+y\le z,qquad u\le z/3.
\]

For a first-crossing endpoint, `z+u>=A`.  Hence the proposed lower period

\[
 z_0=\max\{3u,A-u\}
\]

is no larger than the original `z`.  If `z'` lies between `z_0` and `z`,
then

\[
 z'\ge3u\ge u+y,quad z'\ge x+y,quad
 z'+u\ge A,quad z'+u\ge4u\ge2y.
\]

Also

\[
 {z'\over3}\ge {y\over2},qquad
 {z'\over3}\ge {z'+u\over4}.
\]

Thus the table remains internally superadditive and three-efficient on the
entire interval, with the same fixed `x,y,u,v`.  Since

\[
 \min_u\max(3u,A-u)=3A/4,
\]

the whole interval lies in the normalized period range.  No hidden scalar
constraint is lost in the descent to `z_0`.

## 3. Full derivative, including the adverse pulse

The exact functional is

\[
 \Phi=\mathcal L_3(z;u,2u)
 +K(x)-K(u)+K(y)-K(2u)
 +K(z+v)-K(z+2u).
\]

The audited period theorem gives

\[
 {d\over dz}\mathcal L_3(z;u,2u)>0
\]

under precisely `z>=3A/4`, `u<=z/3`, `2u<=2z/3`, and `z+u>=A`.

For the final pulse, `u<=v<=2u`; hence both arguments are in the Gaussian
tail.  There

\[
 K'(t)=2(A+t)e^{-(A+t)^2}
\]

is strictly decreasing, because `1-2(A+t)^2<0` for `t>=A`.  Therefore

\[
 {d\over dz}\bigl(K(z+v)-K(z+2u)\bigr)
 =K'(z+v)-K'(z+2u)\ge0.
\]

The remaining two corrections are independent of `z`.  The total
functional is thus strictly increasing.  The adverse pulse is priced, not
discarded or assigned a false pointwise sign.

## 4. Boundary split

The two affine lower constraints meet at `u=A/4`, giving exactly

\[
 z_0=A-u\quad(u\le A/4),qquad
 z_0=3u\quad(u\ge A/4).
\]

Since `z<A` and `u<=z/3`, the second branch has `u<A/3`.  These are exactly
the parameter ranges required by the two boundary theorems.

### Endpoint `A`

When `z=A-u`, the endpoint is `T=A`.  The general endpoint-period Bellman
lower bound gives

\[
 \Phi\ge C(A)+F_A(x)+F_A(y)+F_A(A-u).
\]

Here `x<=u<=A/4` and `y<=2u<=A/2`.  The audited train bounds and reflection
therefore give

\[
 \Phi>{1\over25}+{1\over25}
       -{1593\over22000}-{1\over20000}
 ={1659\over220000}>0.
\]

This lower bound is on the actual Bellman clock and automatically includes
every finite transient.

### Density tie

When `z=3u`, the endpoint is `T=4u` and

\[
 z/3=T/4=u\ge y/2.
\]

Thus the same table is on the four-efficient Apéry boundary with
`alpha=u`.  Since `A/4<=u<A/3`, the exact reduction gives

\[
 \Phi\ge J(u)>{1117\over94500}>0.
\]

The delayed finite Apéry correction is part of this comparison.  Exact
cross-multiplication gives

\[
 {1117\over94500}>{1659\over220000},
\]

so the first boundary supplies a uniform lower margin for the whole
subcritical face.

## 5. First-crossing completion

For an arbitrary table on the `w=2u` face, the all-grid deletion theorem
reduces at the first displayed threshold crossing.  If that crossing is at
capacity at most three, the positive prefix functional is a lower bound for
the original functional.  If it is at capacity four, then `x,y,z<A` and the
subcritical theorem applies.  Hence the entire `w=2u` face is positive.

Combining this with the already closed two-efficient, four-efficient, and
`P+u=A` branches leaves only

\[
 w=y,\qquad P+u=2y,\qquad y>2u
\]

inside `n=4`.  The former large-residue `z>=A` row is an earlier-crossing
case, not an additional minimal counterexample face.

## 6. Scope

The proof closes the complete five-pulse `w=2u` face while preserving its
adverse tail term.  It does not sign the remaining `P+u=2y` surface, prove
the all-grid Bellman inequality, or imply `nu(k)<=B(k)+O(1)`.

**Final audit verdict: PASS.**
