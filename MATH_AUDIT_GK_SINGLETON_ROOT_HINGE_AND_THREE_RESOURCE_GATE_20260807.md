# Audit: Greene--Kleitman singleton-root hinge

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_GK_SINGLETON_ROOT_HINGE_AND_THREE_RESOURCE_GATE_20260807.md`  
**Verdict:** **GO after one scope correction.**

## 1. Local construction

For a Dyck root `U`, the displayed sets have the required ranks:

* `a` has rank `m-2`;
* `X,B_x,B_y` have rank `m-1`;
* `Q_x,Q_y,U` have rank `m`.

The four incidences in

\[
B_x-Q_x-X-Q_y-B_y
\]

are literal.  Suppressing the two rank-`m` vertices gives two Johnson
edges with common intersection `a`, and `X subset U` is the required
ticket to the omitted root.

## 2. Greene--Kleitman successor identities

For `X=U-u`, the modified height has its last new record low at the close
`y` of the first primitive component.  Hence the rightmost unmatched zero
is `y`, and `t(X)=X+y=Q_y`.

In Case I, `B_x=U-u-b+x` has new record lows at `u` and `b`.  The matched
`b`-excursion never drives the modified height below the level reached at
`b`, and after `x` the displacement returns from `-4` to `-2`.  Thus `b`
is the rightmost unmatched zero and `t(B_x)=B_x+b=Q_x`.

In Case II, the successive record lows occur at `u`, `y`, and `b`; changing
the closing step `x` upward prevents a later lower record.  Again the
rightmost unmatched zero is `b`, giving `t(B_x)=Q_x`.

These arguments also show that `Q_x,Q_y` are in the image of the fixed SCD
matching and hence outside its singleton-root omission bank.

## 3. Automatic privacy and the corrected residual gate

All Dyck roots begin with coordinate `1`, so `U -> X_U=U-{1}` is
injective.  Since `t` is injective, `U -> Q_{y,U}=t(X_U)` is injective as
well.

The original draft incorrectly required separate injectivity of the maps
`U -> B_x` and `U -> B_y`.  That would not exclude a cross-role collision
`B_{x,U}=B_{y,V}`, nor a collision with a fixed `X_V`.  The theorem has
been corrected.  The exact residual privacy condition is:

1. all selected `B_x` and `B_y` values are jointly distinct;
2. none belongs to the fixed `X` bank;
3. the selected intersection colours `a` are distinct.

Then injectivity of `t` makes the `Q_x=t(B_x)` values jointly distinct and
disjoint from all `Q_y=t(X)` values.  These conditions are also necessary,
so the remaining gate really is a three-resource list-transversal in which
each root claims `(B_x,B_y,a)` while avoiding the fixed `X` bank.

## 4. Scope

The theorem proves one fixed-matching-compatible hinge at every omitted
Greene--Kleitman singleton root.  It does **not** prove:

* the global three-resource transversal;
* extension of the prospective cross edges to the second perfect matching;
* surjectivity on every rank-`(m-2)` intersection colour;
* bounded component count or Hamiltonicity;
* residence, deeper upper palettes, or the terminal compiler.

No such conclusion should be cited from this local theorem.
