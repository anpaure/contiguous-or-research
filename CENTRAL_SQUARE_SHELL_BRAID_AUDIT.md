# Audit of the central-square shell braid

## Verdict

**PASS for the square decomposition and the two explicit shadow braids.**

The `Q_c` parameterization, the two-sector decomposition of the complete
four-box middle layer, the shell partition, the word length

\[
  (R+1)^2+R,
\]

and the interval witnesses for every target with `x>=u` are exact.  The
bottom chain and the displayed `Delta_u` grids also represent every target
in the complementary branch `x<u` when considered separately.

This is a shadow-level result.  It does **not** construct a common linked
factor band or prove the required core-pin conditions for the shell order.
Those remain separate obligations.  Also, at `c=0` the two coordinate-pair
orientations use the same square alphabet but generally demand different
rectangle families; one must either braid both families together or pay a
second `O(m^2)` copy.  The latter is asymptotically harmless relative to the
four-box width `Theta(m^3)`, but literal sharing of that overlap is not proved
by the shell theorem alone.  This is a real distinction: under the pair swap,
the `c=0` square coordinates transform as

\[
 (a,b)\longmapsto(R-b,R-a).
\]

Already at `R=2`, the transformed `Gamma_R` misses the target `(u,r,x)=(0,1,0)`.

## 1. Sector parameterization

For `R=m-c`,

\[
 Q_c(a,b)=(c+a,m-c-b,b,m-a),\qquad 0\le a,b\le R,
\]

lies in `[0,m]^4` and has coordinate sum `2m`.  Its inverse on the sector
`z_1+z_4>=m` is

\[
 c=z_1+z_4-m,\qquad a=m-z_4,\qquad b=z_3.
\]

The middle-layer identity gives `z_2=R-b`, so the representation is unique.
If `z_1+z_4<=m`, swapping the coordinate pairs `(1,4)` and `(2,3)` gives the
corresponding unique representation in the other sector.  The intersection
is exactly the `c=0` square.

Consequently

\[
 |M_m|=(m+1)^2+2\sum_{R=0}^{m-1}(R+1)^2
      ={2m^3+6m^2+7m+3\over3}.
\]

For any interval of square points, coordinatewise maximization gives

\[
 (c+\max a,\;m-c-\min b,\;\max b,\;m-\min a).
\]

Thus a bounding rectangle `[u,r]x[0,x]` has exactly the claimed target
value `(c+r,m-c,x,m-u)`.

## 2. Shell word

The sets

\[
 L_u=\{(a,u):u\le a\le R\}\cup\{(u,b):u<b\le R\}
\]

are exactly the fibres of `min(a,b)=u`; hence they partition the square and
have size `2(R-u)+1`.  The block `Gamma_0` lists `L_0` once.  For `u>=1`,
`Gamma_u` lists `L_u` once and inserts only the portal `(u,0)`, which already
belongs to `L_0`.  Therefore every square point occurs once except the `R`
portals, which occur twice, and

\[
 |Gamma_R|=(R+1)^2+R.
\]

For `0<=u<r<=R` and `u<=x<r`, the interval inside `Gamma_u` beginning at
`(r,u)`, passing through `(u,u)` and the portal `(u,0)`, and ending at
`(u,x)` has bounding box `[u,r]x[0,x]`.  For `u=0`, the analogous interval
uses the unique `(0,0)` in `Gamma_0`.  This covers exactly

\[
 \sum_{u=0}^{r-1}(r-u)={r(r+1)\over2}
\]

of the `r^2` targets at radius `r`.

All boundary cases are valid: `R=0` has one square point and no target;
`u=0` needs no repeated portal; and `u=R` contributes a shell block but no
target because every target has `u<r`.

If no sharing is assumed at the overlapping `c=0` sector, concatenating one
shell word for each sector in each of the two orientations gives the exact
shadow length

\[
 2\sum_{R=0}^{m}\bigl((R+1)^2+R\bigr)
 =|M_m|+(m+1)(2m+1).
\]

It contains every middle point and covers the `x>=u` branch in both
orientations.  Hence the claimed global overhead for this branch is indeed
only `O(m^2)=o(|M_m|)`, even without solving the `c=0` sharing issue.

## 3. Complementary portal grids

The missing targets are exactly `0<=x<u<r<=R`.  The bottom chain

\[
 (R,0),(R-1,0),\ldots,(0,0)
\]

supplies all `x=0` targets.  If `1<=x<u<r`, necessarily `u>=2`, and the
interval in

\[
 \Delta_u=(R,1),(R-1,1),\ldots,(u+1,1),(u,0),
           (u,1),\ldots,(u,u-1)
\]

from `(r,1)` through `(u,0)` to `(u,x)` has bounding box
`[u,r]x[0,x]`.  Thus the individual grids are exact.  What is not proved is
an ordering that superposes all these grids with subquadratic repetition.

## 4. Exhaustive check

`scratch/verify_central_square_shell_braid.py` verifies:

* the two-sector partition and exact middle-layer count through `m=10`;
* the square spanning and exact multiplicities of `Gamma_R`;
* all `x>=u` shell witnesses; and
* all `x<u` witnesses in the separate bottom/`Delta_u` grids,

through `R=12`.
