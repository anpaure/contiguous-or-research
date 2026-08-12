# Audit of the symmetric promotion-hinge orbit, AH countercut, and triangle scaffold

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_PBBS_PROMOTION_HINGE_SYMMETRIC_ORBIT_DEGREES_AH_COUNTERCUT_AND_CYCLE_SCAFFOLD_20260807.md`  
**Verdict:** the flat-hinge one-point degrees, the principal typed
pair-codegrees, the target-disjoint owner countercut, the q1-surplus
identity, and the far-core necessary condition all pass.  The triangle
scaffold counts pass after distinguishing the bare scaffold codegree from
the full flagged-triangle codegree.  Two scope corrections are essential:
the full pair codegree includes the choice of the third flag, and cycle
cancellation does not remove the duplicate lower-owner-edge-colour charge.

## 1. One-point degree table

Put

\[
 n=2m+1,\qquad a=m-d-2,\qquad
 c_0=\binom{m-2}{d},\qquad N=m+d+2.
\]

Choosing the base (R), its split (R=M\mathbin{\dot\cup}C), and the
ordered exterior labels ((u,x,y,v)) gives

\[
 E=\binom n{m-2}c_0(m+3)_4
  =\frac{n!}{a!d!(m-1)!}.
\]

For a fixed flag ((M,u)), choose (C\subseteq[n]\setminus(M+u)), then
choose ((x,y,v)) outside (M+C+u).  Hence

\[
 D_F=\binom Nd(m+2)_3.
\]

For one fixed value in one typed slot, direct reconstruction gives

\[
 D_O=c_0(m)_2(m+1)_2,
 \qquad
 D_L=c_0(m-1)(m+2)_3,
 \qquad
 D_U=D_O.
\]

The last equality follows, for example, from

\[
 D_{J_-}=c_0(m+1)_3m
          =c_0(m)_2(m+1)_2.
\]

Thus every formula in Theorem 2.1 passes.

## 2. Principal typed pair-codegrees

The displayed table also passes:

\[
\begin{array}{c|c}
(T_-,T_0),(T_0,T_+)&c_0(m)_2\\
(T_-,T_+)&4c_0\\
(I_-,Y)&c_0(m+1)_2\\
(J_-,J_+)&c_0(m)_2\\
(f,I_-)&(m+2)_3.
\end{array}
\]

For example, a nested typed lower--owner pair fixes the added owner label,
leaves (m-1) choices for the distinguished label in the lower set, the
(c_0) base split, and an ordered exterior pair.  Its codegree is therefore

\[
 \lambda_{max}=c_0(m-1)(m+1)_2.
\]

The next closest nested owner--upper pair has codegree

\[
 c_0(m)_2m<\lambda_{max},
\]

and all remaining typed pairs are smaller.  Consequently

\[
 \lambda_{max}/D_L=1/(m+2),\qquad
 \lambda_{max}/D_O=1/m.
\]

The (O(m^{-1})) worst normalized codegree and (O(m^{-2})) same-rank
codegree claims are correct.

## 3. Target-disjoint load and the Aharoni--Haxell countercut

For a fixed typed sidecar (I), target-disjointness permits at most

\[
 \binom{m-1}{d}
\]

distinct flag tops (U_f\subset I), and each has ((m+2)_3)
completions.  The proposed

\[
 \Delta_*=\binom{m-1}{d}(m+2)_3
\]

is therefore valid.  Checking the other slots directly gives no larger
load.  For instance a fixed typed owner containing (U_f) has total load
at most

\[
 \binom m{d+1}(d+1)(m+1)_2
 =\binom{m-1}{d}m(m+1)_2<\Delta_*.
\]

The ratio

\[
 \rho_H=\frac{\binom{m+d+2}{d}}{\binom{m-1}{d}}
 \longrightarrow e^{\pi/4}
\]

is correct for the optimal (d^2/m\to\pi/4).  The maximal-matching bound

\[
 \nu\ge \frac{\rho_H}{21}|\mathcal X|
\]

cannot imply the seven-uniform Aharoni--Haxell threshold
(7(|\mathcal X|-1)); the resulting crude sufficient ratio would indeed
be (\rho_H>147).

The large-bank countercut is exact.  The rank-(a)-to-rank-((a+1))
inclusion graph has a matching saturating the rank-(a) shore, yielding a
target-disjoint bank of size (inom na), while

\[
 \frac{\binom n{m-d-2}}{\binom nm}\longrightarrow e^{-\pi/4}>1/3.
\]

Every resource-disjoint flat hinge consumes three distinct rank-(m)
owners, so no bank larger than (W/3) embeds.  The associated
Aharoni--Haxell owner cut is also correct.

## 4. The q1-surplus identity and its scope

Since

\[
 \binom n{m-1}=\frac{m}{m+2}W,
\]

a linear (W)-owner path has exact excess

\[
 S_{q1}=(W-1)-\binom n{m-1}
       =\frac{2W}{m+2}-1,
\]

and a cyclic factor has (2W/(m+2)).  Thus independent payment of one
literal predecessor sidecar per member of a positive-density hinge bank is
impossible in a q1-exact architecture.

Cycle cancellation solves a different row: it supplies every exported
name (Q_i) at the successor occurrence of another hinge.  It does **not**
make the lower owner-edge palette injective.  In a cycle bank each (Q_i)
colours two owner edges, once as predecessor and once as successor.  Hence a
q1-exact owner factor still incurs one duplicate edge-colour occurrence per
hinge and must satisfy

\[
 |J|\le S_{q1}.
\]

Accordingly, the source's phrases “cycle cancellation removes that scalar
obstruction” and “smallest nonduplicating cancellation packet” are correct
only if “obstruction” means missing **literal named coverage** and
“nonduplicating” means the rank-(m) middle-owner unions.  They are false if
read as claims about the global lower-q1 owner-edge palette.  Either the
duplicate charge must be paid, or the displaced q1 targets must be compiled
in other short cells.

## 5. Triangle scaffold degrees

The bare oriented scaffold count and fixed-slot flag degree pass:

\[
 \binom n{m-2}(m+3)_3,
 \qquad
 D_\triangle=\binom{m+d+2}{d}(m+2)_2.
\]

If all three (M)-targets are required distinct, the full orbit and one
fixed flag degree are

\[
 E_\triangle=\binom n{m-2}(m+3)_3(c_0)_3,
\]

and

\[
 3\binom{m+d+2}{d}(m+2)_2(c_0-1)_2,
\]

respectively.

For two fixed flags assigned to two specified slots, let
(s=|M\cup M'|).  Provided (M\ne M'), both distinguished labels avoid
(M\cup M'), and (s\le m-2), the **bare scaffold** codegree is

\[
 \binom{n-s-2}{m-2-s}(m+1).
\]

This chooses the common (R) and the third exterior cycle label.  In the
full flagged-triangle orbit it must additionally choose the third
(M)-target.  For specified slots the codegree is therefore

\[
 \boxed{
 \binom{n-s-2}{m-2-s}(m+1)(c_0-2).}
\]

For two untyped flag vertices, multiply by the six ordered assignments to
two cycle slots.  At the worst compatible value (s=a+1), this is

\[
 \boxed{
 6\binom{m+d}{d-1}(m+1)(c_0-2).}
\]

Relative to the fixed-flag degree, the ratio is

\[
 \frac{2d}{(m+d+2)(m+d+1)(c_0-1)}.
\]

Thus formulas (6.9)--(6.10) must be labelled as **bare-scaffold**
codegrees; without that label they omit the third flag choice.  If
(M=M'), the full distinct-(M) orbit codegree is zero even when the two
flags differ through their distinguished labels.

## 6. Far-core arc obstruction

For an arc (i\to j), the set (Q_i-u_i) has rank (m-2), contains
(M_i), and has exactly (d) positions outside (M_i).  Since

\[
 Q_j=(Q_i-u_i)+b
\]

and (M_j\subset Q_j), necessarily

\[
 |M_j\setminus M_i|\le d+1.
\]

This proves the stated obstruction.  Three rank-(a) sets with all ordered
differences larger than (d+1), together with distinct external flag
labels, exist for all sufficiently large (m), so target-disjoint flag
banks with an empty flagged-coatom digraph do exist.  The near-diagonal
condition is therefore genuine and not implied by target-disjointness.

## 7. Final audited boundary

The following portions are exact:

1. all flat-hinge one-point degrees;
2. all displayed principal typed pair-codegrees and the worst-codegree
   bound;
3. the target-disjoint (W/3) owner countercut;
4. the q1-surplus formula;
5. the bare and full triangle degrees after the codegree distinction above;
6. the far-core necessary condition.

Neither the degree table nor cycle cancellation proves a positive-density
q1-exact hinge factor.  The remaining positive theorem must jointly price
the repeated lower edge colours, construct the near-diagonal triangle or
longer-cycle bank, and satisfy the literal endpoint/occurrence constraints.
