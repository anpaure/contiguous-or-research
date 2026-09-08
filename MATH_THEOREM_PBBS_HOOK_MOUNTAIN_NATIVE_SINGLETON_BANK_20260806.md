# A native PBBS hook component contains a complete singleton bank

**Date:** 2026-08-06  
**Method:** exact mountain inverse-fibre renewal, hook action--angle
arithmetic, and mandatory-core localization; no computation or search  
**Status:** unconditional for `2<=h<m`, subject only to the standard exact
PBBS action--angle and predecessor-return formulae already used in the
component census.  Taking `h=d+1` gives, inside one untouched canonical
PBBS component, one occurrence-disjoint literal singleton cell for every
ground coordinate.  This closes the native singleton-supply row.  It does
not prove residence or compilation on the other PBBS components.

## 1. The one-pile mountain angle

Put

\[
                         n=2m+1,
 \qquad 2\le h<m,
 \qquad p=2h-1,
 \qquad b=m-h.
\tag{1.1}
\]

Consider the hook action

\[
                         \lambda=(h,1^b).
\tag{1.2}
\]

The mountain inverse-fibre coordinates identify its angles with cyclic
weak-composition necklaces of `b` chips on `p` slots.  Choose the
one-pile angle represented by

\[
                         \eta=(0,b,0,\ldots,0).
\tag{1.3}
\]

Because `b>0`, this composition has exact rotational period `p`; in the
action--angle notation its internal symmetry is `gamma=1`.

The hook period matrix and PBBS translation are

\[
 F=
 \begin{pmatrix}
  n-2&2\\
  2b&2h+1
 \end{pmatrix},
 \qquad
 v=\binom1h.
\tag{1.4}
\]

The determinant is

\[
                         \det F=np,
\tag{1.5}
\]

and replacing the first column by `v` has determinant one.  Hence this
whole torus is one canonical PBBS component, of length `np`, for the
step-two middle-owner map `tau`.

There is also a direct rooted-coordinate identity.  If `z_t` is the
terminal leaf-slot occupancy at phase `t` and `r_t` its physical root,
substitution in the rooted hook update gives

\[
                         r_{t+1}=r_t-(2z_t+1)\pmod n.
\tag{1.6}
\]

During one complete `p`-slot rotation the occupancies sum to `b`.  Hence

\[
 r_p-r_0=-(2b+p)=-(2m-1)\equiv2\pmod n.
\]

Thus the literal centered identity is

\[
                         \boxed{\tau^p=\rho^2.}
\tag{1.7}
\]

Since `n=2m+1` is odd, `rho^2` still generates every coordinate rotation.
Hence all `n` coordinate rotates of a rooted phase lie on this **same**
PBBS factor component, at factor-time spacing exactly `p`.

## 2. Exact minimum return and component residence

For the mountain inverse fibre the literal parent transport rotates the
composition slots.  Its distinguished predecessor is selected at times

\[
                         2,\ 2+p,\ 2+2p,\ldots.
\tag{2.1}
\]

Consequently a phase with terminal occupancy zero has first omitted-label
return gap

\[
                         p+2=2h+1.
\tag{2.2}
\]

This is the exact zero-winding return from the additive-renewal theorem.
The primality assumption used there for a bulk census is unnecessary
here: (1.3) itself has exact period `p` for every `p`.

More generally, terminal occupancy `z>=0` can only delay the relevant
predecessor selection.  Thus no phase in this one-pile component has a
first omitted-label return gap smaller than `2h+1`.  This also follows
directly before the outer circumference: the first possible predecessor
selection is the one in (2.2), and `2h+1<n` because `h<m`.

Recall the centered residence dictionary.  If the omitted-label word has
consecutive occurrences

\[
                         g_s=g_{s+2L+1}=x
\tag{2.3}
\]

and no intervening occurrence of `x`, then in the step-two rank-`m`
owner row the coordinate `x` is inserted after the first occurrence and
deleted at the second; its positive owner run has exactly `L` states.
Equations (2.2)--(2.3) therefore give:

### Theorem 2.1 (native minimum-run component)

Every positive coordinate run on the component through (1.3) has length
at least `h`.  At every phase whose terminal occupancy is zero, the
current omitted coordinate has a positive run of length exactly `h`.

In particular, with

\[
                         h=d+1,
\tag{2.4}
\]

this component is cyclically depth-`d` resident and has an exact
minimum-length run.

## 3. One exact run for every coordinate, in one component

Choose one zero-terminal phase of (1.3), and call its omitted coordinate
`x_0`.  Equation (1.7) says that the phases

\[
                         \tau^{jp}D=\rho^{2j}D,
 \qquad 0\le j<n,
\tag{3.1}
\]

have the same one-pile angle and the same zero terminal occupancy.  Their
omitted coordinates are

\[
                         x_j=\rho^{2j} x_0.
\tag{3.2}
\]

These are all `n` ground coordinates.  By Theorem 2.1, each `x_j` has an
exact length-`h` owner run beginning at the corresponding rotated phase.

When `h<=m-2`, this is literally an untouched component of the standard
full rigid-rotation rethread.  That rethread cuts only the single-soliton
and two-soliton edge orbits, whereas (1.2) then has at least three
solitons.  In the eventual regime `h=d+1=Theta(sqrt(m))`, the inequality
`h<=m-2` is automatic.

The phases in (3.1) are distinct.  Indeed, no rank-`m` subset of an
`n=2m+1` cycle is fixed by a nonidentity rotation: invariance under a
rotation with orbit length `ell>1` would force `ell` to divide `m`, while
`ell` also divides `n` and `gcd(m,n)=1`.

The selected run starts are therefore pairwise distinct factor edges,
and their cyclic factor-time spacing is exactly

\[
                         p=2h-1.
\tag{3.3}
\]

This proves a point which is easy to misstate: coordinate rotation does
not produce `n` alternative PBBS factors.  All rotated tickets coexist as
distinct occurrences on one component of the one fixed canonical factor.

## 4. Literal singleton cells without changing the owner factor

Now set `h=d+1` and let

\[
                         P_t=\bigcap_{a=0}^{d}T_{t-a}
\tag{4.1}
\]

be the maximal depth-`d` antecedent on this component.  For a simple
Johnson owner trace, the mandatory core at a source position is

\[
                         F_t=\{\iota_t,\delta_t\},
\tag{4.2}
\]

where `iota_t` is the run which begins at the corresponding owner
transition and `delta_t` is the run which ends after erosion.  At the
eroded position of an exact length-`d+1` run these two labels coincide.
Thus the `j`-th selected position `t_j` has

\[
                         F_{t_j}=\{x_j\}.
\tag{4.3}
\]

Define a nonmaximal antecedent by

\[
 A_t=
 \begin{cases}
  \{x_j\},&t=t_j\text{ for some }j,\\
  P_t,&\text{otherwise}.
 \end{cases}
\tag{4.4}
\]

The positions `t_j` inherit the spacing (3.3).  In particular they are
distinct and form a union of singleton free intervals.  Every such free
interval has length one, at most `d`, and (4.3) retains its complete
mandatory core.  The short-gap localization theorem therefore gives

\[
                         \boxed{D^dA=T.}
\tag{4.5}
\]

All unmodified envelope letters are nonempty: on a simple resident
Johnson trace the intersection of `d+1` consecutive owners has rank
`m-d>=1`.  The modified letters are singletons.  Thus `A` is an ordinary
nonempty source word, not merely a set-valued factor with empty cells.

Every `A_(t_j)` is literally the width-one target `{x_j}`.  We have proved:

### Theorem 4.1 (complete native singleton bank)

For every `2<=d+1<m`, the untouched canonical PBBS factor contains one
hook component which admits a depth-`d` antecedent carrying all `n=2m+1`
singleton targets on pairwise distinct source cells.  The owner chronology,
its component decomposition, and every immediate lower/upper owner colour
are unchanged.

Moreover every old owner-interval union remains a literal source-interval
union: from (4.5),

\[
 \bigcup_{i=a}^{b}T_i
 =\bigcup_{t=a}^{b+d}A_t.
\tag{4.6}
\]

Thus the singleton installation creates no loss in the upper interval-OR
deck inherited from this component.

## 5. Consequence and exact scope

The singleton compiler row no longer requires a PBBS-relative collar or a
conjugate double-rail rethread.  Its tickets already occur natively and
simultaneously on one untouched hook component.  In particular:

* no owner is replaced or duplicated;
* no q1 edge is punctured;
* no component is split or joined;
* all coordinate rotations coexist in the same factor, rather than being
  mutually exclusive choices; and
* shrinking the `n` isolated antecedent cells preserves `D^dA=T` exactly.

This theorem does **not** say that every component of the canonical PBBS
factor is depth-`d` resident.  Other components can contain shorter runs,
and the global construction still needs its established residence repair,
upper-component gluing, and terminal common-cap/low-target compilation.
It also does not supply targets of ranks `2,...,d`; the separate literal
collar atlas remains relevant for those rows.

## 6. Dependencies

The only imported statements are:

1. the mountain inverse-fibre weak-composition transport and exact first
   return formula from
   `MATH_THEOREM_PBBS_ST_EXACT_ADDITIVE_RENEWAL_AND_TWO_TIME_CENSUS_20260726.md`;
2. the exact hook period matrix and one-cycle torus theorem from
   `MATH_THEOREM_PBBS_SOLITON_GAP_FORCES_EXPONENTIALLY_MANY_SELECTED_CYCLES_20260805.md`;
3. the standard spatial-rotation action vector used throughout the PBBS
   action--angle ledger; and
4. mandatory-core short-gap localization from
   `MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md`.

The assertion that the component is untouched by the full rigid orbit
uses the exact cut ledger in
`MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_ALL_DEPTH_INTERVAL_FAN_TRANSPORT_20260805.md`.

No finite search, solver, asymptotic probability estimate, or unproved
packet-regeneration hypothesis is used.
