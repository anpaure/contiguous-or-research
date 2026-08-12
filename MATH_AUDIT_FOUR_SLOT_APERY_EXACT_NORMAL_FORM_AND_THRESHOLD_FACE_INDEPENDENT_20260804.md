# Independent audit of the four-slot Apéry normal form and threshold face

**Date:** 2026-08-04  
**Verdict:** **PASS after conservative scope repairs.**  The reduced-walk
census, the literal Bellman head through capacity nine, the three transient
corrections, period-face reduction, Gaussian-train estimates, and the strict
`47/10000` threshold-face margin are correct.  The reduction to the scalar
`J(alpha)` is exact.  This note does not count the inequality `J(alpha)>0`
as proved by the audited target.

No web search, H100 computation, numerical optimization, or finite parameter
search was used.  Rational inequalities were independently recomputed as
exact fraction comparisons.

## 1. Sources and repairs

| role | file | SHA-256 |
|---|---|---|
| target before audit | `MATH_THEOREM_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_20260804.md` | `ce122a435a0ba67a0c9af0551bcc0fa62d955c6ef04adc90db46e3d091efa748` |
| target after audit | same file | `8fc1405920daea3e597a105d04b9b63e42867a4db1cf9c9515f2a73cd6584cda` |
| supplied audit before audit | `MATH_AUDIT_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_20260804.md` | `306e83c506b313445a44e3f011a0f4b6ed5a20d3e56cf3439d7c5ef5b3bf2b68` |
| supplied audit after audit | same file | `f1037c63f6bed933ce8c58c6e7422ce8fc0e8b0e4f275fc062c7b6685814ba15` |

The independent-audit hash is reported outside this note.

Five proof-scope repairs were applied.

1. The table is now explicitly nonnegative.  This is inherited from the
   Bellman-clock setting and is needed for the kernel arguments and the
   bound `0<=x<=s_1`.
2. The inherited first-crossing assumption `T>=A` is now explicit in the
   target setup.  It is essential for Lemma 3.1: changed Bellman arguments
   then lie on the increasing tail of `K`.
3. The Apéry proof now says why it is enough to enumerate simple reduced
   walks.  All reduced step weights are nonpositive, so deleting a repeated
   residue's closed subwalk cannot decrease weight.
4. The generic ceiling train `C(a)=sum_(m>=0)K(ma)` is now defined before
   `C(alpha)` and `J(alpha)` are used.
5. The monotonicity proof on `[0,2A/3]` now includes the elementary exact
   justification `log 5<2<2pi/3`.

The supplied audit's phrase “four remaining contributions” was corrected to
“five retained contributions.”  Its arithmetic was already correct.

## 2. Reduced Apéry census

Put `alpha=T/4` and `d_j=c_j-j alpha`.  Four-slot efficiency and internal
superadditivity give

\[
 d_1,d_2,d_3\le0,
 \quad d_2\ge2d_1,
 \quad d_3\ge d_1+d_2,
 \quad d_1+d_3\le0.
\]

Because every step has nonpositive reduced weight, a maximal walk to a
given residue can be made simple by deleting closed subwalks.  A simple walk
from zero in `Z/4Z` has at most three edges.  Up to step order, the complete
list is

\[
\begin{array}{c|l}
1&d_1,\ d_2+d_3,\ d_1+2d_2,\ 3d_3,\\
2&d_2,\ 2d_1,\ 2d_3,\ d_1+d_2+d_3,\\
3&d_3,\ d_1+d_2,\ 3d_1,\ 2d_2+d_3.
\end{array}
\]

The dominance relations are exact:

\[
 d_1+2d_2\le d_1,
 \quad 2d_1\le d_2,
 \quad d_1+d_2+d_3\le d_2,
\]

and

\[
 d_1+d_2\le d_3,
 \quad3d_1\le d_1+d_2\le d_3,
 \quad2d_2+d_3\le d_3.
\]

Hence

\[
 \beta_1=\max(d_1,d_2+d_3,3d_3),
 \quad \beta_2=\max(d_2,2d_3),
 \quad \beta_3=d_3.
\]

Translating by the appropriate multiples of `alpha` gives exactly the
displayed `s_1`, `s_2`, and their bounds.  No reduced witness is missing.

## 3. Literal capacities and the transient correction

Direct partition comparison gives

\[
\begin{array}{c|ccccc}
m&5&6&7&8&9\\ \hline
V_m&T+\max(x,y+z-T)&T+\max(y,2z-T)&T+z&2T&2T+s_1.
\end{array}
\]

At capacity five the realizable residue-one witnesses are `4+1` and
`3+2`; the candidate `3+3+3` has capacity nine.  This is precisely why the
capacity-five shift is `b_1=max(x,y+z-T)` rather than `s_1`.  At capacity
six the witnesses `4+2` and `3+3` realize `s_2`; residue three is already
stable via `4+3`; and maximum efficiency bounds capacity eight by `2T`,
which is attained.

At capacity nine all three surviving residue-one witnesses fit:

\[
 2T+x,
 \qquad T+y+z,
 \qquad3z,
\]

whose maximum is `2T+s_1`.  Padding by size-four generators yields the
claimed periodic formulas.  Comparing the literal head with the four
shifted lattices gives, with no omitted term,

\[
 \Phi=\mathcal L_4(T;s_1,s_2,z)
 +K(x)-K(s_1)+K(y)-K(s_2)
 +K(T+b_1)-K(T+s_1).
\]

The signs and positions of all three corrections are correct.

## 4. Endpoint reduction in `T`

For fixed `x,y,z`, increasing `T` increases every Bellman maximum.  For
`m>=4`, the repaired hypothesis gives `V_m>=T>=A`; `K` is increasing on
`[A,infinity)`.  Termwise monotonicity therefore proves Lemma 3.1.

Also `z>=x+y>=3x`, so `x+z<=4z/3`.  Combining first crossing, internal
superadditivity, and four-slot efficiency gives the exact least endpoint

\[
 T_0=\max(A,2y,4z/3).
\]

The faces `T_0=A` and `T_0=2y` are exactly the threshold and two-efficient
faces.  The only remaining face is `T_0=4z/3>A`, including the harmless
tie conventions stated in the target.

## 5. Independent rational certificate replay

I used the exact rational bounds

\[
 {333\over106}<\pi<{355\over113}
\]

and the following two implications.  For `c,r>0`,

* `e^{-c pi}<r` follows once the positive Taylor partial sum at
  `c(333/106)` exceeds `1/r`;
* `e^{-c pi}>r` follows once the Taylor sum at `c(355/113)`, plus the
  geometric majorant of its positive remainder, is below `1/r`.

Independent exact cross-multiplication gives the following first sufficient
degrees; they agree with the supplied audit.

\[
\begin{array}{c|c}
\text{comparison}&\text{first sufficient degree}\\ \hline
e^{-\pi}<7/160&8\\
e^{-\pi}>1/24&4\\
e^{-9\pi/64}<129/200&3\\
e^{-25\pi/64}<47/160&5\\
e^{-81\pi/64}<19/1000&9\\
e^{-9\pi/64}>641/1000&1\\
e^{-25\pi/64}>7/24&2\\
e^{-81\pi/64}>37/2000&6\\
e^{-9\pi/4}<1/900&9\\
e^{-169\pi/64}<1/3000&10.
\end{array}
\]

The bound `M=1-2e^{-pi/4}>3/35` is also exact: the degree-four positive
Taylor sum at `333/424` is

\[
 {566333778491\over258555281408}>{35\over16},
\]

so `e^{-pi/4}<16/35`.

For the integer Gaussian tail, the first term is below `1/900` and all
successive ratios are below `e^{-7pi/4}<1/100`; hence the tail from `n=3`
is below `1/800`.  For the quarter-shift tail, the first term is below
`1/3000` and successive ratios are below `e^{-15pi/8}<1/100`; hence it is
below `1/1000`.

Substitution gives exactly

\[
 C(A)>{3\over35}-{7\over160}-{1\over800}
 ={57\over1400}>{1\over25},
\]

and

\[
 F(A/4)>
 1-{129\over200}-{47\over160}-{19\over1000}-{1\over1000}
 ={33\over800}>{1\over25},
\]

while

\[
 F(A/4)<1-{641\over1000}-{7\over24}-{37\over2000}
 ={293\over6000}<{1\over20}.
\]

All directions are correct.

## 6. Train monotonicity and reflection

With `h(t)=t exp(-(pi/4)t^2)`, direct differentiation gives

\[
 {F'(u)\over2A}
 =\sum_{n\ge1}h(n+u/A)-h(1-u/A).
\]

The function `h` increases on `[1/2,3/4]` and decreases on `[1,infinity)`.
On the two subintervals, the exact sign-safe estimates are

\[
 h(5/8)>{9\over20},
\]

and

\[
 h(5/4)+h(9/4)+{2\over\pi}e^{-81\pi/64}
 <{449719\over1065600}<{17\over40};
\]

then

\[
 h(1/2)>{2\over5},
\]

and

\[
 h(11/8)+h(19/8)+{2\over\pi}e^{-361\pi/256}
 <{619739\over1776000}<{7\over20}.
\]

These fractions independently reproduce the supplied audit.  Hence `F`
decreases on `[A/4,A/2]`.  Combined with the previously proved
critical-point fact—every interior critical point on `[0,A/2]` is a strict
maximum—this establishes all three bounds in Lemma 4.1.

For reflection, completing both half-trains to the full integer lattice and
applying Poisson summation gives exactly

\[
 F(At)+F(A(1-t))
 =-4\sum_{m\ge1}e^{-4\pi m^2}\cos(2\pi mt).
\]

Since `pi>3`, the absolute value is below

\[
 {4e^{-12}\over1-e^{-36}}<{1\over20000};
\]

the degree-eight positive Taylor sum gives `e^3>20`, which is already more
than enough.  For `1/2<=t<=3/4`, the reflected point lies in
`[A/4,A/2]`, where `F<1/20`; therefore

\[
 F(At)>-{1\over20000}-{1\over20}
 =-{1001\over20000}.
\]

Lemma 4.2 is correct.

## 7. Threshold-face margin

At `T=A`, one has

\[
 0\le s_1\le A/4,
 \quad0\le s_2\le A/2,
 \quad0\le z\le3A/4.
\]

Since `x<=s_1`, `y<=s_2`, and `K` decreases on `[0,A/2]`, the two compact
corrections are nonnegative.  Also `0<=b_1<=s_1<=A/4`, while `K` increases
on the Gaussian tail, so

\[
 K(A+b_1)-K(A+s_1)
 \ge K(A)-K(5A/4)
 =-e^{-\pi}+e^{-81\pi/64}
 >-{101\over4000}.
\]

The five retained lower bounds are therefore

\[
 {1\over25},\quad {1\over25},\quad0,
 \quad-{1001\over20000},\quad-{101\over4000}.
\]

Their exact sum is

\[
 {1\over25}+{1\over25}-{1001\over20000}-{101\over4000}
 ={47\over10000}>0.
\]

Thus Theorem 6.1 and its stated strict margin are verified.

## 8. Exact derivation and scope of `J(alpha)`

On the remaining face `T=4z/3`, put `alpha=z/3`.  First-crossing
truncation gives `alpha<A/3`, while `T>A` gives `alpha>A/4`.  The candidate
`3z-2T` equals `alpha`; the constraints `x<=alpha` and `y<=2alpha` make
the other residue-one candidates at most `alpha` and make `2z-T=2alpha`
dominate residue two.  Hence

\[
 s_1=\alpha,
 \qquad s_2=2\alpha,
 \qquad z=3\alpha.
\]

The four Apéry cosets interlace exactly into the arithmetic `alpha`-clock,
so formula (2.4) becomes

\[
 \Phi=C(\alpha)+K(x)-K(\alpha)+K(y)-K(2\alpha)
       +K(4\alpha+b_1)-K(5\alpha).
\]

For `0<t<=2/3`, the function

\[
 f(t)=\log{1+t\over1-t}-\pi t
\]

is strictly convex, so its maximum on `[0,2/3]` is at an endpoint.
Here `f(0)=0` and `f(2/3)=log 5-2pi/3<0`.  Thus `K` decreases on
`[0,2A/3]`, and the first two corrections are nonnegative.  Finally
`b_1>=0` and `4alpha>=A`, so tail monotonicity gives

\[
 K(4\alpha+b_1)\ge K(4\alpha).
\]

Therefore

\[
 \Phi\ge J(\alpha)
 :=C(\alpha)+K(4\alpha)-K(5\alpha).
\]

The physical interval is open, `(A/4,A/3)`.  Proving the inequality on the
closed interval `[A/4,A/3]` is a stronger, convenient sufficient statement
and includes all limiting faces.  Thus the scalar reduction is exact in
direction and scope.  The audited target itself does not prove the scalar
inequality, nor does it address the three-efficient branch or arbitrary
finite Bellman tables.
