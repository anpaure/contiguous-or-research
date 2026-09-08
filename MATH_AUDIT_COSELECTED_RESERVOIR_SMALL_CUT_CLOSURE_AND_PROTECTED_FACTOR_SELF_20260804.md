# Self-audit: co-selected reservoir small-cut closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`  
**Method:** independent line-by-line algebra and scope replay; pure
mathematics; no computation, search, or solver  
**Verdict:** GO at the stated asymptotic protected-factor scope.

## 1. Residual Hall and minimality

After deleting the saturated lower palette `Z`, a remaining lower vertex
has demand two and owner `U` has capacity

\[
 c_U=2-d_P(U).
\]

Thus the exact Hall supply of `A subseteq X=L setminus Z` is

\[
 \kappa(A)=\sum_U\min(c_U,a_U).
\]

For `x in A`, the decrement on removing `x` is one exactly at owners with
`1<=a_U<=c_U`.  If `A` is inclusion-minimal deficient, then

\[
 \kappa(A)\le2|A|-1,
 \qquad
 \kappa(A-x)\ge2|A|-2,
\]

so the number of such owners is at most one.  The theorem's loose-owner
lemma is exact.

## 2. The `m-21` count

For `x notin Z`:

1. every internal owner over `x` contributes one to the singleton loss,
   so there are at most ten;
2. every nondeterministic endpoint owner over `x` exposes its protected
   neighbour away from `x`, so there are at most ten;
3. outside the union `H` of facets of the at most `2m` deterministic top
   endpoints, there is no deterministic top endpoint;
4. minimality leaves at most one loose owner.

These four classes are disjoint owner-degree/capacity classes, except that
the loose class may intersect the endpoint or unused class.  Subtracting
all four upper bounds therefore only overcounts exclusions and is safe:

\[
 m-10-10-0-1=m-21.
\]

Every owner left after those exclusions has protected degree zero and
occupancy at least three.  Calling their family `F`, each contributes two
to `kappa(A)`, so

\[
 2|F|\le\kappa(A)\le2|A|-1
 \quad\Longrightarrow\quad |F|\le|A|-1.
\]

The exceptional bank has

\[
 |H|\le(2m)m=2m^2.
\]

No forced-facet-load assumption is hidden in this small-side count.

## 3. Partial-shadow parameter replay

The abstract side-ratio lemma is stated for a nonempty upper family; this
is needed to write its size as `binom(y,D)`.  In the application the family
has size at least `2m^2`, so the condition is automatic.

Complementation changes

\[
 x\in\binom{[2m-1]}{m-1},\quad
 U\in\binom{[2m-1]}m,quad x\subset U
\]

into

\[
 U^c\in\binom{[2m-1]}{m-1},\quad
 x^c\in\binom{[2m-1]}m,quad U^c\subset x^c.
\]

Hence every member of `J=(A setminus H)^c` has at least `D=m-21`
selected facets from `C=F^c`.

If `|J|=binom(y,D)`, Chao--Yu gives

\[
 |C|\ge\binom y{D-1}.
\]

When `|A|>=4m^2`, one has `|J|>=2m^2` and

\[
 |C|\le|A|-1<2|J|.
\]

Therefore

\[
 {D\over y-D+1}<2,
 \qquad y>{3D\over2}-1.
\]

The non-strict version used in the theorem is consequently safe.  Stirling
gives

\[
 \log_2\binom{(3/2)D-1}{D}
 =\left({3\over2}H_2(2/3)+o(1)\right)D,
\]

and `(3/2)H_2(2/3)=1.377...>1`.  This contradicts the small-side cutoff
`2^(m+o(m))`.

The co-small theorem is applied with the exact complement convention:
if `B=X setminus A`, then

\[
 \mathcal L\setminus A=Z\mathbin{\dot\cup}B,
 \qquad
 \kappa(A)-2|A|=2|B|-\Omega_P(Z\cup B).
\]

Thus its optional co-small bank is exactly the complement of the residual
Hall shore, not a different cut.

## 4. Pair pricing of deterministic endpoints

The exact path-forest identity contains one unfavourable endpoint term.
Every counted private endpoint contains at least two selected facets and
is charged by `e_P^priv(x)` to each such facet.  Hence there are at most
`5|A|`.

For deterministic top endpoints, choose one unordered selected-facet pair
below each counted owner.  Two rank-`m-1` sets have at most one common
rank-`m` owner, namely their union when that union has rank `m`.  The map
from counted endpoint to chosen pair is injective.  Together with the
literal `2m` endpoint count this gives

\[
 E_{\rm top}\le\min\left(2m,\binom{|A|}{2}\right).
\]

Adding the singleton-load cap `10|A|` proves the loss estimate in the
theorem.

## 5. Kruskal--Katona and the finite polynomial split

For `a=|A|=binom(x,m)`, complementation identifies `N(A)` with the lower
shadow of an `a`-member rank-`m` family.  Kruskal--Katona gives

\[
 |N(A)|\ge\binom x{m-1}
 =a\,{m\over x-m+1}.
\]

Since `binom(m+3,m)>4m^2` for all sufficiently large `m`, the range
`a<4m^2` has `x<m+3` and therefore `|N(A)|/a>m/4`.  The exact
shadow-slack inequality yields

\[
 \sigma(A)>
 { (m-2)(m-4)\over4(m-1)}a=\beta_m a.
\]

For `2<=a<=8`, `(beta_m-15)a` eventually exceeds `binom(a,2)`.
For `a>=9`, `9(beta_m-15)>2m` eventually.  These two ranges cover every
non-singleton polynomial shore, while singleton safety follows directly
from `ell_P(x)<=10<m-2`.

## 6. Scope

The proof establishes only a spanning two-factor containing the protected
reservoir.  A two-factor may have many cycles.  No step proves:

- one Hamilton cycle or path;
- compatible physical endpoint collars;
- cyclic global residence;
- occurrence-level upper chronology; or
- a common-cap/lower compiler.

The forced-facet cap `z_U<=9` enters only through the separately audited
optional co-small theorem.  The small-side proof uses the two spread-ten
bounds and the deterministic endpoint count.  This separation is explicit
and prevents circular use of the desired residual factor.
