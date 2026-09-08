# Complete period-five Apéry extreme classification and Rayleigh positivity

**Date:** 2026-08-05  
**Method:** pure mathematics; exact polyhedral classification and comb/
Beatty decompositions; no computation, search, or solver  
**Status:** unconditional.  The period-five cyclic-superadditive increment
cone has, besides the arithmetic ray, exactly eight normalized extreme
rays.  Six are one-kink or mechanical.  The remaining two are genuinely
primitive and nonmechanical, but both have strictly positive complete
Rayleigh phase throughout the normalized period range.  Positivity on all
extreme rays does not by itself sign the nonlinear functional in the
interior of the cone.

## 1. The normalized period-five cone

Let `x=(x_1,...,x_5)` be the increment vector of a nonnegative cyclically
superadditive shift table.  Subtract the arithmetic ray
`x_1(1,1,1,1,1)` and scale the nonzero residual so that `x_5=1`.  Write

\[
 x=(0,a,b,c,1).
\tag{1.1}
\]

The cyclic-block minimum criterion gives exactly

\[
 \boxed{
 0\le a,b,c\le1,
 \qquad a\le b+c,
 \qquad a+b\le c+1.}
\tag{1.2}
\]

Indeed, length one says that the first increment is minimum, and length
four says that the fifth is maximum.  The only nonredundant length-two and
length-three inequalities are respectively

\[
 a\le b+c,
 \qquad a+b\le c+1.
\]

All remaining cyclic blocks follow from these and the box inequalities.

## 2. Exact vertex list

### Theorem 2.1

The polytope (1.2) has exactly the following eight vertices:

\[
\begin{array}{c|c|c}
(a,b,c)&x=(0,a,b,c,1)&\text{type}\\ \hline
(0,0,0)&(0,0,0,0,1)&\text{one-kink}\\
(0,0,1)&(0,0,0,1,1)&\text{one-kink}\\
(0,1,0)&(0,0,1,0,1)&\text{mechanical }h=2\\
(0,1,1)&(0,0,1,1,1)&\text{one-kink}\\
(1,0,1)&(0,1,0,1,1)&\text{mechanical }h=3\\
(1,1,1)&(0,1,1,1,1)&\text{one-kink}\\
(1/2,1/2,0)&\tfrac12(0,1,1,0,2)&\text{nonmechanical}\\
(1,1/2,1/2)&\tfrac12(0,2,1,1,2)&\text{nonmechanical}.
\end{array}
\tag{2.1}
\]

Together with the arithmetic vector `(1,1,1,1,1)`, these generate the
full homogeneous period-five cone.

#### Proof

Intersect the unit cube with the two halfspaces in (1.2).  A vertex lying
on neither oblique boundary is a cube vertex; precisely the first six
listed cube vertices survive.  A vertex lying on one oblique boundary but
not the other requires two independent cube facets, and its surviving
intersections are again among those six.

On both oblique boundaries,

\[
 a=b+c,
 \qquad
 a+b=c+1.
\]

Hence

\[
 b={1\over2},
 \qquad
 a=c+{1\over2},
 \qquad0\le c\le{1\over2}.
\]

The two endpoints are exactly the final two vertices in (2.1).  This
exhausts every possible set of three independent active facets.  Restoring
the subtracted minimum increment adds the arithmetic ray. \(\square\)

The two fractional vertices become the integral primitive tables

\[
 u=(0,1,1,0,2),
 \qquad
 v=(0,2,1,1,2).
\tag{2.2}
\]

Neither has a proper density tie, and neither is mechanical: a mechanical
increment word uses only two consecutive values, whereas each of (2.2)
uses `0,1,2`.

## 3. Exact positive decomposition of the first nonmechanical ray

Scale `u` by `eta>0`.  Its endpoint is `P=4eta`, and its five phases are

\[
 0,0,\eta,2\eta,2\eta.
\tag{3.1}
\]

Therefore

\[
\begin{aligned}
 \Phi_u(\eta)
 &=2F_P(0)+F_P(\eta)+2F_P(2\eta)\\
 &=\underbrace{\bigl(F_P(0)+F_P(2\eta)\bigr)}_{C(2\eta)}
 +\underbrace{\bigl(F_P(0)+F_P(\eta)+F_P(2\eta)\bigr)}_{R_{4,3}(\eta)}.
\end{aligned}
\tag{3.2}
\]

The second bracket is exactly the sparse Beatty rotor with phases

\[
 \left\lfloor{4\ell\over3}\right\rfloor\eta,
 \qquad \ell=0,1,2,
\]

modulo `4eta`.  Hence, if `P<=zeta`, the all-mechanical theorem gives

\[
 R_{4,3}(\eta)>0,
\]

while the all-mesh comb theorem gives

\[
 C(2\eta)>{377\over108000}.
\]

Thus

\[
 \boxed{
 \Phi_u(\eta)>{377\over108000}>0
 \qquad(4\eta\le\zeta).}
\tag{3.3}
\]

## 4. Exact positive decomposition of the second nonmechanical ray

Scale `v` by `eta>0`.  Its endpoint is `P=6eta`, and its phases are

\[
 0,0,2\eta,3\eta,4\eta.
\tag{4.1}
\]

The even and half-period residue systems give the termwise identity

\[
\begin{aligned}
 \Phi_v(\eta)
 &=2F_P(0)+F_P(2\eta)+F_P(3\eta)+F_P(4\eta)\\
 &=\underbrace{\bigl(F_P(0)+F_P(2\eta)+F_P(4\eta)\bigr)}_{C(2\eta)}
 +\underbrace{\bigl(F_P(0)+F_P(3\eta)\bigr)}_{C(3\eta)}.
\end{aligned}
\tag{4.2}
\]

Consequently

\[
 \boxed{
 \Phi_v(\eta)
 =C(2\eta)+C(3\eta)
 >{754\over108000}>0.}
\tag{4.3}
\]

This identity is valid for every `eta>0`; the normalized condition
`6eta<=zeta` is needed only to place the ray in the current Apéry period
range.

## 5. Complete extreme-ray consequence

Every normalized period-five extreme ray is now signed:

1. the one-kink rays by the exact arithmetic-comb decomposition;
2. the mechanical rays by the all-mechanical rotor theorem;
3. `u` by (3.2)--(3.3);
4. `v` by (4.2)--(4.3);
5. the arithmetic ray by the all-mesh comb theorem.

Thus no period-five cone extreme is a formal Rayleigh counterclock.

The phase functional

\[
 x\longmapsto\sum_{r=0}^{4}F_P(s_r(x))
\]

is nonlinear on a fixed-period cross-section.  Positivity on vertices
therefore does not imply positivity at every interior profile without an
additional concavity, exchange, or extremal-minimizer theorem.  No such
claim is made here.  The finite shoulder remains separate.

## 6. Dependencies

1. `MATH_THEOREM_RAYLEIGH_ALL_MECHANICAL_APERY_ROTORS_POSITIVE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_APERY_FUNDAMENTAL_PERIOD_COLLAPSE_AND_ONE_KINK_COMB_RESERVE_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_ARITHMETIC_COMB_CENTERED_PHASE_IDENTITY_20260805.md`.
