# Strict-extremal side forests and the contracted Gamma gate at `n=3,4`

## Scope

This note classifies one deliberately strong normal form in the two-coordinate
Catalan collar.  The child path forests, orientations, and retained edge sets
`Q` are exactly those in
`scratch/catalan_two_coordinate_integral_collar_n3_n4_20260731.audit.json`.
The classification is exhaustive for these two fixed faces only.  It is not
an all-`n` construction and does not prove or refute an unrestricted
protected-corner SCD/CLM theorem.

## 1. Strict side normal form

Fix one shore.  Its physical side graph is a linear forest on the appropriate
rank-`n-1` or rank-`n+1` middle layer.  The `C` inherited seam vertices are
called anchors.  A side is **strict extremal** when

1. every anchor has physical degree at most one; and
2. every nonanchor has physical degree exactly two.

Write `c_i` for the number of side components containing exactly `i` anchors.
The usual charge identity is

```text
c_2 - c_0 = K,                 K = Cat_n.
```

The strict row is stronger than `c_0=0`.

### Lemma 1 (strict normal form)

Every strict side has

```text
c_0 = 0,   c_2 = K,   c_1 = C - 2K.
```

Moreover, every `c_1` component is an isolated anchor and every `c_2`
component is a path whose two endpoints are anchors.

### Proof

A finite path component has either one isolated vertex or two degree-one
endpoints.  A nonanchor cannot be isolated or an endpoint because its degree
is exactly two.  Hence every component contains one or two anchors, proving
`c_0=0`; a one-anchor component must be an isolated anchor.  Substitution in
`c_2-c_0=K` gives `c_2=K`, and counting the `C` anchors gives
`c_1+2c_2=C`.  This proves the formula.  QED.

The converse is false.  In the frozen `n=3` positive collar the minus shore
has `c_0=0`, but its sole nonanchor has degree one.  In the frozen `n=4`
minus shore two nonanchors have degree one.  Thus charge extremality alone
does not imply the strict degree row.

## 2. Contracted attachment criterion

Let `F_-`, `F_z`, and `F_+` be the minus-side forest, the retained child
forest, and the plus-side forest.  Contract every component of these three
forests and retain the two cross edges contributed by every moved child edge.
Call the resulting layered multigraph `Gamma`.

### Lemma 2 (forest contraction)

Assume the literal physical endpoint caps hold.  The expanded complement is
a linear forest if and only if `Gamma` has maximum degree at most two and is
acyclic.

### Proof

Before cross edges are added, every contracted object is a tree component.
Adding a cross edge creates a cycle in the expanded graph exactly when its
two endpoints were already connected; the same union-find event occurs after
component contraction.  Thus cycle rank is preserved.  Physical endpoint
caps are exactly the local maximum-degree-two condition.  QED.

This is the proof-safe topology gate.  Neither a product-SCD alignment nor a
prescribed abstract anchor pairing is needed once the three internal forests
and `Gamma` are known.

## 3. Complete frozen-face census

The audit enumerates every outer-colour matching satisfying exact palette
bijection, side acyclicity, anchor cap one, and the strict nonanchor degree-two
row.  “Signature” below means a literal outer-colour matching; no symmetry
quotient was taken.

| child `n` | strict minus signatures | strict plus signatures | pairs | `Gamma` cycle-rank histogram | acyclic pairs |
|---:|---:|---:|---:|---|---:|
| 3 | 1 | 1 | 1 | `4:1` | 0 |
| 4 | 270 | 2 | 540 | `0:116, 1:32, 2:210, 4:98, 6:84` | 116 |

For `n=3`, every strict shore has

```text
(c_0,c_1,c_2) = (0,4,5).
```

The two strict sides are individually valid and unique, but their only joint
`Gamma` has cycle rank four.  Therefore this fixed `n=3` face has no joint
strict-extremal lift.  Its already known positive lift necessarily leaves the
strict row on the minus shore.

For `n=4`, every strict shore has

```text
(c_0,c_1,c_2) = (0,14,14).
```

There are 116 acyclic pairs.  The first canonical pair, at catalogue indices
`(98,0)`, was materialized as all 210 ambient Boolean diamonds.  Literal
replay gives exact lower and upper palettes, maximum physical degree two,
cycle rank zero, 42 path components, and exact central `z`-degree
inheritance.  Thus the strict normal form is genuinely feasible on this
fixed `n=4` face after reselecting both shores.

The originally published `n=4` sides are not members of this strict
catalogue: the frozen minus nonanchor degree histogram is `1^2 2^12`, and
the frozen plus histogram is `0^1 1^6 2^7`.

## 4. Consequence for the protected-balanced-corner route

The smallest exact invariant is not “`A` is isolated on each shore.”  It is
the correlated three-forest condition

```text
side palette exactness
+ physical endpoint caps
+ acyclic contracted Gamma.
```

The `n=3` census shows that forcing both shores into the stronger isolated-
anchor/nonanchor-degree-two form can destroy the only topology, even though
each side separately exists.  The `n=4` census shows that the same form can
work after correlated side selection.  Therefore a viable all-parameter
theorem, if true, must choose the two shores jointly (or permit controlled
non-strict endpoints); charge alone and independent-boundary absorber packing
do not settle the topology.

## 5. Audit artifacts

- `scratch/audit_h2_catalan_n3_n4_strict_extremal_normal_form_20260731.py`
- `scratch/h2_catalan_n3_n4_strict_extremal_normal_form_20260731.audit.json`
- enumeration/replay kernel:
  `scratch/audit_h2_catalan_n4_extremal_side_gamma_20260731.py`
- auxiliary `n=4` report:
  `scratch/h2_catalan_n4_extremal_side_gamma_20260731.audit.json`

Exact SHA-256 values are recorded in the handoff entry accompanying this
note.  All searches are deterministic finite rollback enumerations; no SAT,
CP-SAT, or remote computation is used.
