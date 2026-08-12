# Face-aligned modular cuts: an exact common-basis rounding criterion and its sharp gap

Date: 2026-07-31  
Status: complete polyhedral theorem, exact two-element obstruction, and an
authenticated Boolean row showing that the sufficient condition is not
automatic.  The criterion is testable cut-by-cut by weighted matroid
intersection, but already fails for one literal parameter-three parent.

## 0. Result

Let `P_cb` be the strict common-base polytope and let the two physical
fractional marginals be imposed by the upper and lower Farkas systems in
Theorem 3.1 of
`MATH_THEOREM_CATALAN_FIXED_Q_DUMMY_DUAL_AND_MULTICOLOUR_LOCKING_20260731.md`.
Every one of their rows restricts to an affine function `ell` on `P_cb`.

There is one exact condition under which fractional feasibility already
rounds to a strict common basis:

> **No-straddling condition.**  For every upper and lower physical Farkas
> row,
> 
> ```text
> min_(q in P_cb) ell(q) < 0 < max_(q in P_cb) ell(q)             (0.1)
> ```
> 
> is false.

Under (0.1), if the joint fractional gate is nonempty, then it is a face of
`P_cb`, and hence contains an integral strict common basis `Q` with

```text
rho^+(Q)=rho^-(Q)=0.                                      (0.2)
```

For a returned Farkas row, the two extrema in (0.1) are ordinary weighted
matroid-intersection problems.  Thus (0.1) is a concrete structural target
for the actual Boolean maps, rather than an appeal to generic rounding.

The condition is also sharp at the level of this information.  A
two-element rank-one common-base polytope and two contracted physical
marginals have a feasible fractional midpoint but no feasible common basis.
Its two rows straddle with opposite signs.  Therefore integrality of the
matroid-intersection polytope plus a separation oracle does not by itself
solve the new gate.

## 1. The strict common-base polytope

Let `M_+` and `M_-` be the two strict pulled-back matroids on the child-edge
ground set `E`, both of rank `C`, and put

```text
P_cb = B(M_+) intersect B(M_-).                         (1.1)
```

Edmonds' matroid-intersection theorem says that (1.1) is integral:

```text
P_cb = conv{1_Q : Q is a strict common basis}.          (1.2)
```

For an upper dual-feasible triple `(a,b,z)`, its physical cut is

```text
ell_(a,b,z)^+(q)
 = sum_D a_D + sum_V b_V - 2 sum_x z_x
   + sum_(e in E) q_e (z_(upsilon(e))-a_(tau(e))) <= 0. (1.3)
```

The lower shore has the complemented formula.  The important point is
that, after the dual triple is fixed, (1.3) is affine in `q`.  Its modular
edge cost is exactly

```text
c_e = z_(upsilon(e))-a_(tau(e)).                        (1.4)
```

## 2. Face-aligned rounding

### Theorem 2.1 (no straddling implies integral physical bank)

Let `P` be any integral polytope and let

```text
C = {x : ell_j(x)<=0 for every j in J}                 (2.1)
```

be an arbitrary intersection of affine halfspaces.  Suppose `P intersect C`
is nonempty and, for every `j`,

```text
not(min_P ell_j < 0 < max_P ell_j).                    (2.2)
```

Then `P intersect C` is a nonempty face of `P`.  In particular, it contains
an integral vertex of `P`.

#### Proof

Fix `j`.  If `max_P ell_j<=0`, its halfspace contains all of `P` and is
redundant.  Otherwise `max_P ell_j>0`.  Nonemptiness of `P intersect C`
implies `min_P ell_j<=0`; condition (2.2) then forces
`min_P ell_j=0`.  Consequently

```text
P intersect {ell_j<=0} = argmin_(x in P) ell_j(x),      (2.3)
```

which is an exposed face of `P`.

Thus every row is either redundant on `P` or cuts out a face.  An arbitrary
nonempty intersection of faces of a polytope is a face.  Since `P` is
integral, every nonempty face contains an integral vertex. `square`

### Corollary 2.2 (strict common-basis version)

If the upper and lower Boolean physical Farkas systems are nonstraddling on
`P_cb`, then feasibility of their joint fractional separation-oracle LP
implies a strict common basis satisfying (0.2).

For any one returned row, both extrema are computable by weighted matroid
intersection with weights (1.4).  A finite complete facet list therefore
gives a finite certificate of the hypothesis.  The theorem does not assert
that finding such a complete list, or proving nonstraddling uniformly in
`n`, is automatic.

### Corollary 2.3 (the more intrinsic face criterion)

It is enough that each shore's fractionally physical region, after
restriction to `P_cb`, is a face of `P_cb`.  If the two restricted regions
have nonempty intersection, their intersection is a nonempty integral face.

The no-straddling condition is a row-by-row sufficient certificate for this
intrinsic statement.  It is not necessary: several straddling rows may be
jointly redundant or may describe the same face after other rows are imposed.

## 3. Exact two-element integrality gap

Take both strict matroids to be `U_(1,2)` on `E={1,2}`.  Their common-base
polytope is

```text
P_cb = {(q_1,q_2)>=0 : q_1+q_2=1}.                    (3.1)
```

The following are contracted one-owner physical marginal systems with the
same affine demand/capacity pattern as (3.1) of the fixed-`Q` theorem.

On the upper shore, let one forced atom load an owner once and let a flexible
atom have weight `w_+`.  Require

```text
w_+ = 1-q_2,
1+w_+ <= 2-q_1.                                       (3.2)
```

This is feasible exactly when

```text
q_1-q_2 <= 0.                                         (3.3)
```

On the lower shore interchange `1` and `2`:

```text
w_- = 1-q_1,
1+w_- <= 2-q_2,
```

which is feasible exactly when

```text
q_2-q_1 <= 0.                                         (3.4)
```

The two rows intersect (3.1) only at

```text
q=(1/2,1/2).                                           (3.5)
```

Neither common basis is feasible on both shores: `(1,0)` violates (3.3)
and `(0,1)` violates (3.4).  Both rows straddle `P_cb`, with extrema
`(-1,+1)`.

This template is a minor obtained after contracting a forced physical load;
it deliberately does **not** claim to be a complete Boolean-diamond shore.
Its role is exact and limited: it proves that no theorem based only on

```text
integral common-base polytope + affine physical Farkas cuts
```

can guarantee an integral bank.  A positive all-parameter theorem must use
additional Boolean geometry, such as face alignment, a submodular-flow
representation, or a correlated exchange property of `tau/upsilon`.

## 4. Relation to generalized polymatroids and exchange

Theorem 2.1 identifies the weakest clean polyhedral route.  Two stronger
but more structured sufficient routes are:

1. prove directly that the joint physical restriction of `P_cb` is a face;
   or
2. represent the complete joint restriction as one integral generalized
   polymatroid (or one integral submodular-flow projection).

The second route works because a nonempty integral generalized-polymatroid
face has an integral point.  Merely representing the two shores separately
as additional matroid or generalized-polymatroid constraints is insufficient:
that creates a three-or-more-system intersection, for which generic
integrality is false.  Likewise, basis-exchange connectedness alone does
not prevent the midpoint obstruction in Section 3.

For the actual Boolean maps the concrete next test is therefore:

```text
For every extreme physical dual row returned by separation, optimize the
cost c_e=z_(upsilon(e))-a_(tau(e)) over strict common bases.  Prove that
the row is redundant or extremal, never genuinely straddling.            (4.1)
```

If (4.1) holds, the new fractional gate rounds exactly.  If one authentic
Boolean row straddles, it identifies the precise exchange direction on
which an integrality gap can occur and rules out face rounding for that
parent.

## 5. The authenticated Boolean system already has a straddling row

The no-straddling theorem is not a hidden all-parameter solution.  Consider
the literal oriented parameter-three forest used in the fixed-`Q`
deficiency-one obstruction.  In this orientation every co-singleton
deletion bank is a strict common basis, so `P_cb` is the full simplex on its
fifteen possible retained edges.

On the upper shore set

```text
a_07=a_13=a_23=1,       a_34=-1,
b_37=1,
z_17=z_27=z_33=1,
```

and set every other `a,b,z` to zero.  Direct replay on every Boolean
diamond gives

```text
a_D+b_V <= z_x+z_y.                                    (5.1)
```

The constant part of (1.3) is `-3`.  In the child-edge order by increasing
rank-two colour, its modular cost vector (1.4) is

```text
(-1,1,0,0,0,0,0,0,1,0,1,0,0,0,1).                   (5.2)
```

Since a co-singleton deletion vector is `q=1-e_r`, the row values on the
fifteen integral common bases are

```text
(1,-1,0,0,0,0,0,0,-1,0,-1,0,0,0,-1).                (5.3)
```

Thus this genuine Boolean physical row has minimum `-1` and maximum `1`.
It cuts through the interior of `P_cb`, rather than exposing a common-base
face.  This does not exhibit a joint two-shore integrality gap: several
integral bases satisfy this row, and other physical rows still matter.  It
does prove that a uniform theorem based solely on rowwise face alignment is
false even at the first physical parameter.

Equivalently, if `p_r` is the retained-edge distribution (`q=1-p`), this
particular physical cut is the signed donor inequality

```text
p_0 <= p_1+p_8+p_10+p_14.                              (5.4)
```

This is a more useful reading than its raw dual weights.  Exact rounding
must route the mass of a bad bank to one of several compensating banks; it
cannot merely choose a minimum face independently on each shore.  The
two-shore problem is therefore naturally a coupled donor-flow or
submodular-flow question on common-basis exchanges.

The remaining plausible exact rounding structures are therefore narrower:

1. the **complete** upper/lower systems may define a common integral face
   even though individual rows straddle;
2. their joint projection may be one integral submodular-flow or generalized
   polymatroid despite non-face facets; or
3. Boolean basis exchanges may couple opposite straddling rows so that an
   integral zero-deficiency basis survives.

The exact arithmetic in Section 3 is replayed by

```text
scratch/audit_catalan_modular_cut_face_rounding_gap_20260731.py
scratch/audit_catalan_n3_boolean_farkas_straddling_20260731.py
```
