# A sharp local counterexample to absorbed-line control alone

## 1. Outcome

The absorbed positive-line energy, request widths, equal length marginals,
zero gaps, and direction stationarity do **not** by themselves force the
strict-sub-four seam bound.  The construction below is an exact
`c downarrow 1` single-threshold relaxation counterexample with

\[
U(1^+)={1029\over250}=4.116.
\]

It is not a physical all-threshold process: the full selected-line coarea
gate eliminates it.  Its purpose is to identify precisely which information
the general proof still needs.

## 2. Exact stationary marked coupling

Take

\[
f={11\over5},\qquad A={9\over5},
\]

and absorbed successor-level measures

\[
\nu_x=1_{[0,9/10]}dt,qquad
\nu_y=1_{[1/10,1]}dt,qquad
\nu_z=0.
\tag{2.1}
\]

Let

\[
h(t)=\min(t,1-t),\qquad w(t)={4\over7}h(t),
\]

and define

\[
p(t)=1+t-{w(t)\over2},qquad
s(t)=2-t-{w(t)\over2}.                                    \tag{2.2}
\]

Then

\[
[p(t)-1,2-s(t)]=[t-w(t)/2,t+w(t)/2],                       \tag{2.3}
\]

so absorption at level `t` is legal and the request width is exactly `w(t)`.

Use direction transitions `y->x` for `t in [0,9/10]` and `x->y` for
`t in [1/10,1]`; let `alpha` be their marked pushforward.  Since

\[
p(t)=s(1-t),                                                \tag{2.4}
\]

the absorbed flow is stationary jointly in length and direction.  Add the
nonabsorbed `z->z` block

\[
\beta={2\over5}\delta_{(11/10,11/10)},qquad
\rho=\alpha+\beta,                                         \tag{2.5}
\]

and give every seam zero gap.

## 3. Exact ledger

The absorbed mass is `A=9/5` and the total seam mass is `f=11/5`.  Also

\[
\int h(t)d(\nu_x+\nu_y)={49\over100},
\]

so

\[
W:=\int w\,d\alpha={7\over25}.                             \tag{3.1}
\]

Since `p+s=3-w` on `alpha`, symmetry gives the common absorbed marginal
moment

\[
{3A-W\over2}={64\over25}.
\]

The block `beta` adds `11/25` to each marginal.  Hence

\[
\|\rho\|={11\over5},qquad
\int p\,d\rho=\int s\,d\rho=3.                             \tag{3.2}
\]

Thus the edge-mass bound is saturated and the zero-gap budget is exact.

The actual absorbed-line level moment and cross-direction intersection are

\[
\tau=\int_0^{9/10}t\,dt+\int_{1/10}^1t\,dt={9\over10},
\]

\[
I=\int_{1/10}^1(1-u)du={81\over200}.
\]

Therefore

\[
E_A=\tau+I={261\over200}
<{7\over5}=2f-3.                                           \tag{3.3}
\]

The sharp positive-line lower bound is only

\[
F(9/5)=13/10=260/200,
\]

so no improvement depending only on absorbed mass can repair the gap.

On the other hand,

\[
2A-W={83\over25}>{80\over25}=1+f.                          \tag{3.4}
\]

Only `beta` pays nonabsorbed saving, namely

\[
\int_\beta ps={2\over5}\left({11\over10}\right)^2
={121\over250}.
\]

Since `e=ell-f=4/5` and `H=0`, the exact local seam value is

\[
U(1^+)=3+2e-\int_\beta ps
={23\over5}-{121\over250}
={1029\over250}>4.                                         \tag{3.5}
\]

## 4. The sharp count band left by local information

For any zero-gap local ledger put

\[
C=2A-W=\int_\alpha(p+s-1).
\]

Support and the common marginal moments give

\[
C\le\min\{2A,6-2f+A\}.                                    \tag{4.1}
\]

The sharp line-energy bound gives `F(A)<=2f-3`, hence

\[
A\le A_*(f)=
\begin{cases}
\sqrt{4f-6},&3/2\le f\le7/4,\\
2f-5/2,&7/4\le f\le9/4,\\
1+\sqrt{4f-8},&9/4\le f\le3.
\end{cases}                                                \tag{4.2}
\]

Substitution in (4.1) proves

\[
C\le1+f
\]

for `f<=2` and for `f>=22/9`.  In the last branch the crossing is

\[
\sqrt{4f-8}\le3(f-2),
\]

whose nontrivial root is `f=22/9`.  Thus absorbed-line information alone
leaves only the band

\[
2<f<{22\over9},                                            \tag{4.3}
\]

apart from equality analysis at its endpoints.  The construction above lies
strictly inside this band.

## 5. Why full line coarea kills the example

The nonabsorbed `z`-plateaux cannot be omitted from an actual selected-line
arrangement.  Against

\[
X=[0,9/10],\qquad Y=[1/10,1],
\]

a `z`-line at level `v in [-9/10,9/10]` adds

\[
|v|+P_X(v)+P_Y(v)-T_{XYZ}(v)
\]

to the full `T+I-J` line functional.  Direct interval calculation bounds
this quantity below by one throughout the allowed range.  Hence the beta
mass `2/5` adds at least `2/5` to the absorbed baseline `261/200`, producing

\[
{261\over200}+{2\over5}={341\over200}>{7\over5}.            \tag{5.1}
\]

So this marked extension violates the full selected-line gate.  It refutes
only a one-threshold theorem using absorbed lines alone; it does not refute
the full coarea program.

## 6. Repaired minimal target

Let

\[
R_\beta=\int_{\rho-\alpha}(p-1)(s-1).
\]

The exact zero-gap identity is

\[
U(1^+)=3-f+(2A-W)-R_\beta.                                 \tag{6.1}
\]

Therefore the sharp sufficient local statement, now explicitly under the
**full all-line coarea and common-lifetime constraints**, is

\[
\boxed{(2A-W)-R_\beta\le1+f.}                              \tag{6.2}
\]

For a universal strict exclusion one must also classify equality or recover
a fixed positive saving at some common continuity threshold.  Proving (6.2)
from the full line geometry, or producing a coherent all-threshold process
that violates it, is the next minimal problem.
