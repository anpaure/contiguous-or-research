# Sharp positive-line isoperimetry and the paired broad seal

## 1. The sharp line-energy inequality

Let `nu_1,nu_2,nu_3` be finite measures on `[0,1]` with

\[
0\le \nu_i\le dt.
\]

Put

\[
A=\sum_i\|\nu_i\|
\]

and

\[
\mathcal E(\nu)=
\sum_i\int_0^1t\,d\nu_i(t)
+\sum_{i<j}\iint_{t+u\le1}d\nu_i(t)d\nu_j(u).
\tag{1.1}
\]

### Theorem 1.1

For `0<=A<=3`,

\[
\boxed{\mathcal E(\nu)\ge F(A)},
\tag{1.2}
\]

where

\[
F(A)=
\begin{cases}
A^2/2,&0\le A\le1,\\
A-1/2,&1\le A\le2,\\
A^2/2-A+3/2,&2\le A\le3.
\end{cases}
\tag{1.3}
\]

All three branches are sharp.

### Proof

Approximate the measures by rational step functions on an `N`-level mesh,
split fractional cells, and pass to the limit after solving the resulting
finite problem.  A selected cell `(i,r)` has vertex weight `r`; cells in two
different colours interact when `r+s<=N`.  Up to `O(N)` endpoint terms,
`N^2 E` is the total vertex weight plus the induced-edge count in this
three-colour Ferrers graph.

Two compressions do not increase this objective.

First, for any two colours replace their incidence sets by their union and
intersection.  Vertex moments and interactions with the third colour are
unchanged.  The mutual cross-colour edge count cannot increase: for each
pair of levels it is total occupancy product minus the same-colour dot
product, and sorting both two-vectors as `(union,intersection)` increases
that dot product by rearrangement.

Second, shift cells through the resulting nested Ferrers neighbourhoods.
At a minimum at most one colour is partially occupied:

1. If `K<=N`, put all `K` cells at the lowest levels of one colour.
2. If `N<=K<=2N`, fill one colour.  A cell of a second colour at level `r`
   has marginal cost `r+(N-r)=N`, independent of its level.
3. If `2N<=K<=3N`, fill two colours.  A third-colour cell at level `r` has
   marginal cost `r+2(N-r)=2N-r`, so the remaining cells move to the
   highest levels.

The standard Ferrers exchange proves these shifts: moving one cell through
a nested neighbourhood changes the edge count by the number of crossed
columns, exactly cancelling the vertex change in the middle phase and
having the displayed strict sign in the two outer phases.

After division by `N^2`, the three canonical configurations have energies
`A^2/2`, `A-1/2`, and `A^2/2-A+3/2`, respectively.  Rational approximation
and weak convergence give (1.2).  Equality is attained by

\[
\begin{array}{ll}
A\le1:&\nu_1=1_{[0,A]}dt,\\
1\le A\le2:&\nu_1=dt\text{ and any }A-1\text{ mass in one other direction},\\
2\le A\le3:&\nu_1=\nu_2=dt,\quad
\nu_3=1_{[1-(A-2),1]}dt.
\end{array}
\]

The exact duality

\[
\mathcal E(dt-\nu_1,dt-\nu_2,dt-\nu_3)
=\mathcal E(\nu)+3-2A
\]

also converts the first branch into the third and checks the constants.
QED.

## 2. Elimination of the paired broad survivor

For the nested alternating-pair process of
`MULTISCALE_DIRECTION_COUPLING_NEXT.md`, as `c downarrow 1`,

\[
f\to2,\qquad \ell\to3,
\]

and every absorbed reflected seam has the unique normalized level

\[
t=2-s\in[0,1].
\]

Let `nu_i` be the actual absorbed-successor level measures.  Same-line
uniqueness gives `nu_i<=dt`, while the absorbed-line theorem gives

\[
\mathcal E(\nu)\le1.
\]

The middle branch of Theorem 1.1 therefore forces

\[
A=\sum_i\|\nu_i\|\le3/2.                         \tag{2.1}
\]

The saving protected by an absorbed seam at level `t` is

\[
b(t)=(2-t)(1+t)=9/4-(t-1/2)^2.
\]

The total absorbed density is at most `2dt`.  By the bathtub principle, a
submeasure of mass at most `3/2` protects at most

\[
B\le2\int_{1/8}^{7/8}(2+t-t^2)dt={423\over128}.    \tag{2.2}
\]

If all reflected seams were nonabsorbed, their total saving would be

\[
2\int_0^1(2+t-t^2)dt={13\over3}.
\]

The scalar part tends to five and the contracted gap term tends to zero.
Consequently every arbitrary partial actual-line lift obeys

\[
\boxed{
\limsup_{c\downarrow1}U(c)
\le5-\left({13\over3}-{423\over128}\right)
={1525\over384}
=4-{11\over384}<4.}
\tag{2.3}
\]

The boundary `t+u=1` is null because every `nu_i` is dominated by Lebesgue
measure.  The disappearing nonreflected block has vanishing mass, the gap
moment tends to zero, and `b` is bounded and continuous.  Hence the strict
margin survives passage to one sufficiently small fixed threshold.

Thus the one known nested broad scalar survivor has no line-realizable lift,
even after arbitrary partial absorption.  This does not exclude every mixed
profile.

## 3. Common-weight dual for the remaining mixed-profile problem

For the exact seam saving

\[
\phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+,
\]

take nonnegative common threshold weights `w(c),q(c)` and define

\[
G_{w,q}(c)=\int
\min\{w(c)\phi(p,s,z),q(c)(p-1)\}\,d\rho_c.
\tag{3.1}
\]

Every nonabsorbed seam pays `w phi`; every absorbed seam has level
`t>=p-1` and therefore pays `qt`.  Thus

\[
wS+q\tau_A\ge G_{w,q}.                              \tag{3.2}
\]

Put

\[
R_A(c)=2f(c)-\ell(c)-\tau_A(c)-\iota_A(c)\ge0.
\]

Substitution into the exact modified-seam functional gives the pointwise
dual envelope

\[
\boxed{
\begin{aligned}
w(c)(U(c)-4)\le{}&
w(c)(3c+2e(c)+H(c)-4)-G_{w,q}(c)\\
&+q(c)(2f(c)-\ell(c))
-q(c)(\iota_A(c)+R_A(c)).
\end{aligned}}
\tag{3.3}
\]

Integrating (3.3) keeps the actual common edge lifetimes.  An all-profile
proof would follow from common nonnegative weights for which its integrated
right side is strictly negative for every coherent marked process.  The
remaining global term is the weighted actual intersection plus unused-line
slack

\[
\int q(c)(\iota_A(c)+R_A(c))dc.
\]

Scalar capacity cannot replace this term.

## 4. Status

Proved:

1. sharp positive-line isoperimetry (1.2)--(1.3);
2. the exact mass cap `A<=3/2` for the paired broad process;
3. the strict margin `11/384` under every partial absorption;
4. the common-weight dual reduction (3.3).

Open:

1. a universal choice of common weights for all coherent mixed profiles;
2. a physically realizable marked counterprocess defeating every choice;
3. the local three-box lemma and the original all-`k` contiguous-OR formula.
