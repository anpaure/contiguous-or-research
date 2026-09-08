# Common pull-clock/SCD rounding: portal reduction and a one-copy lattice warning

**Date:** 2026-08-01  
**Status:** proof-safe synthesis, one conditional exact rounding theorem, and
two finite/lattice audits.  This note does **not** prove a common integral
rounding, an Euler chronology, or an upper bound for `nu(k)`.

## 0. Outcome

The corrected stationary pull-clock theorem and the protected SCD selector
solve two different projections of the lower chronology problem:

* the pull clock gives an exact **fractional stationary literal circulation**
  with the optimal triangular rank marginals;
* an SCD gives an exact **integral named-target chain selector**, even after
  quarantining any at-most-`m+1` prescribed root flags.

Their common integral point is still open.  It is not an ordinary network
flow consequence.  Once a literal flag table is frozen, the remaining turn
problem is a tripartite tail/head/owner matching problem.  Physical strong
triangles are impossible, but physical clean strong `C5`s occur; hence the
first possible balanced-matrix obstruction is exactly an odd pentagon.

The useful positive consequence is that a bounded bank of prepared pentagon
portals no longer pays any named-target sidecar: the protected SCD theorem
can quarantine all of its flags while covering every named target exactly.
If the residual turn core is balanced and fractionally perfect, exact
owner/root rounding follows.

There is also a sharp warning against rounding the particular symmetric pull
clock type by type.  At `k=10`, its type-`(1,1)` density is

\[
 x_{1,1}={605\over7308},\qquad
 W x_{1,1}=\binom{10}{5}{605\over7308}={605\over29}\notin\mathbb Z.
 \tag{0.1}
\]

Thus no `W`-position one-copy schedule can preserve that exact block-start
histogram.  This is a lattice obstruction to **that canonical fractional
point**, not to the full construction: `k=10` itself has a verified exact
optimal word.

The shortest remaining theorem is therefore not “round every pull-block
coefficient independently.”  It is one of:

1. choose a functional owner attachment whose predecessor graph has Hall;
2. choose a fractionally light odd-cycle transversal in one correlated
   positive support; or
3. prepare resource-disjoint odd-cycle portals and leave a balanced,
   fractionally perfect residual core.

All three choices must be made simultaneously with the exact named-target
flag table.

## 1. Audit of the corrected pull clock

Use the notation of
`MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md`.
The pull coefficients are

\[
 x_{\delta,j}=A_\delta\Delta_j-A_{\delta+1}\Delta_{j+1}.
 \tag{1.1}
\]

The corrected ratio directions are

\[
 {A_\delta\over A_{\delta+1}}\ge
 \rho={k-c+1\over c},
 \qquad
 {\Delta_{j+1}\over\Delta_j}\le\rho,
 \tag{1.2}
\]

and therefore every `x_(delta,j)` is nonnegative.  With

\[
 \theta={1\over\rho}={c\over k-c+1},
 \tag{1.3}
\]

the packing calculation uses

\[
 {P-\alpha\over H}\le {P-\alpha\over P}\le\theta,
 \tag{1.4}
\]

and

\[
 {\gamma-\beta\over\beta-\alpha}\le\rho.
 \tag{1.5}
\]

These imply total block-plus-separator cost at most one.  The staircase
telescoping, literal cyclic realization, stabilizer averaging, and final
rankwise thinning then give exactly the claimed triangular residual loads.

The audit found no mathematical defect in this corrected proof.  Equation
(1.4) was missing its first comparison sign in the file and has been fixed.
The theorem remains explicitly fractional.

## 2. The exact common master after the two marginal theorems

Let `F` be a one-copy literal flag table, one flag rooted at every rank-`m`
set.  Marked suffixes of `F` must cover every required named lower target
exactly once.  For each overlap state `w`, form the legal turn graph

\[
 G_w=(L_w,R_w;E_w),
 \tag{2.1}
\]

where a turn from

\[
 f=(p;z_1,\ldots,z_{d-1})
\]

to `g` is legal precisely when

\[
 q=p-\{z_1\}+\{\beta\},\qquad
 \operatorname{rail}(g)=(z_2,\ldots,z_{d-1},\gamma),
 \quad \gamma\in B(f),
 \tag{2.2}
\]

and its owner colour is `p+beta`.

For a fixed table `F`, the exact chronology rows are:

1. `|L_w|=|R_w|` for every state `w`;
2. every `G_w` has a perfect matching;
3. the statewise matchings can be selected with every owner colour exactly
   once.

The SCD theorem solves the named-target marginal but can fail already at
row 1 and can contain dead rows at row 2.  The pull clock solves the
stationary fractional analogue, but repeats labelled owners and does not
select one integral table `F`.  Their common problem is therefore a
correlated integral colouring problem, not a missing rank count.

## 3. The exact flow face: functional owner attachment

Suppose an owner is attached functionally to every head root by a bijection

\[
 \vartheta:Q\longrightarrow O,
 \qquad q\subset\vartheta(q).
 \tag{3.1}
\]

Keep only legal turns `(p,q,o)` with `o=vartheta(q)`.  The head row and its
owner row are then identical.  Suppressing the duplicate owner rows leaves
the bipartite predecessor graph

\[
 B_\vartheta=(P,Q;\{pq:(p,q,\vartheta(q))\text{ is legal}\}).
 \tag{3.2}
\]

Its incidence matrix is totally unimodular after orienting one shore.
Consequently:

### Theorem 3.1 (functional common-rounding criterion)

If an exact named-target flag table `F` and an attachment `vartheta` can be
chosen so that `B_vartheta` satisfies Hall, then `F` has an owner-exact
literal directed cycle cover.

This is the maximal presently proved ordinary-flow face.  The unsolved
choice is joint: a frozen exact SCD table need not admit any suitable
attachment, while choosing `vartheta` first need not leave an exact
named-target flag table.

## 4. Why a generic TU or bipartite-flow proof stops at `C5`

In the full physical Boolean turn hypergraph an atom is

\[
 (p,q,o),\qquad o=p\cup q,
 \tag{4.1}
\]

with `p,q` distinct middle roots.  A clean strong `C3` cannot occur: its
three shared rows would have types tail, head, owner; the two roots inside
the shared owner already force the third atom to contain all three shared
rows.

Clean physical strong `C5`s do occur.  The authenticated connected `k=17`
type-inventory face contains a zero-holonomy `C5`, so neither quotient gauge
nor aggregate type balance removes it.  Its odd-cycle incidence minor has
determinant two.  Therefore the unrestricted common master is not a network
matrix or a balanced packing matrix.

The same authenticated `C5` has a one-row portal: one portal atom together
with two alternating cycle atoms is a matching saturating all five cycle
rows.  Thus the pentagon is a real non-TU witness but not a local
impossibility.  It identifies the minimal absorber that a general rounding
proof must organize globally.

## 5. Protected portals cost zero named-target sidecar

The protected SCD selector theorem permits arbitrary prescribed flags at
any `h<=m+1` distinct roots and covers every named high target exactly once
while marking none of the prescribed flag suffixes.  Combine it with the
prepared portal-core theorem.

### Theorem 5.1 (protected-portal common-rounding criterion)

Let `P` be a matching of prepared portal atoms whose incident root flags use
at most `m+1` distinct protected roots.  Suppose there is a completion `F`
of those prescribed flags such that:

1. `F` is an exact named-target selector;
2. after deleting every resource used by `P`, the residual literal turn
   hypergraph `H'` has a balanced incidence matrix; and
3. `H'` has a fractional perfect matching.

Then the same construction has both an exact named-target selector and an
owner-exact literal cycle cover containing `P`.

#### Proof

The protected SCD theorem removes the named-target cost of prescribing the
portal flags: all protected suffixes may be unmarked and all targets route
through unprotected roots.  By balanced-packing integrality, the fractional
perfect matching of `H'` rounds to an integral perfect matching.  Its union
with the resource-disjoint portal matching `P` saturates every tail, head,
and owner resource.  `square`

The theorem is conditional only in the common completion: it does not claim
that an arbitrary protected SCD completion preserves residual balancedness
or fractional Hall.  Its gain is the exact quantifier separation:
**bounded portals themselves cause no lower-target deficit.**

The same statement holds with bounded deficiency `C` if the residual
fractional matching number is at least the residual shore size minus `C`.

## 6. A complete finite census at the first nontrivial depth

At `(k,m,d)=(5,2,2)`, a flag consists of a rank-two root and one deleted
coordinate.  The audit enumerated all `2^10` rooted flag tables, retained
the `704` tables in which every singleton target has a provider, built the
full physical tail/head/owner turn hypergraph, and compared fractional
perfect matching with integral exact cover.

An exact-rational two-phase tableau gives

```text
NO_EXACT_GAP support_ok=704 fractional_ok=24 integral_ok=24
```

Thus every fractionally feasible table in this complete finite census is
integrally feasible.  This does not prove an all-`k` theorem, but it shows
that the first actual common-turn face has no hidden fractional/integral
gap.

Artifacts:

```text
scratch/search_d2_flag_fractional_integral_gap_exact_20260801.cpp
scratch/search_d2_flag_fractional_integral_gap_20260801.cpp
scratch/d2_flag_fractional_integral_gap_20260801.audit.txt
```

## 7. The first canonical pull-clock histogram misses the one-copy lattice

For `k=10`, the corrected exact pull-clock audit gives

\[
\begin{aligned}
 x_{1,1}&={605\over7308},&x_{1,2}&={5\over116},\\
 x_{2,1}&={25\over1218},&x_{2,2}&={5\over522}.
\end{aligned}
\tag{7.1}
\]

In the literal block construction, `x_(delta,j)` is the normalized number
of starts of a type-`(delta,j)` pull block.  A period using exactly the `W`
middle owners once and preserving this precise block histogram would require
every `W x_(delta,j)` to be integral.  But

\[
 W x_{1,1}=252{\cdot605\over7308}={605\over29}.
 \tag{7.2}
\]

### Proposition 7.1 (fixed-histogram one-copy obstruction)

The canonical symmetric pull-block decomposition at `k=10` cannot be
realized on a `W`-position one-copy owner period with exactly its displayed
block-start histogram.

This is deliberately scoped.  It does not show that the stationary
circulation has no other decomposition, that the full common polytope has no
integral point, or that `k=10` is impossible.  On the contrary, the known
exact `k=10` word proves that another integral architecture exists.  The
proposition rules out only the naïve proof strategy “multiply the canonical
pull densities by `W` and assign those block types ownerwise.”

It also explains why denominator clearing is harmless for fractional
stationarity but insufficient for one-copy chronology: clearing the
denominator repeats the labelled owner inventory.

## 8. The exact remaining theorem

The evidence now separates the common integral gate as follows.

| row | status |
|---|---|
| triangular rank marginals | exact |
| stationary literal pull circulation | exact fractional |
| unrestricted/protected named-target chain selector | exact integral |
| generic one-copy rounding of the canonical pull histogram | false |
| common exact flag table with rail balance/statewise Hall | open |
| owner-rainbow selection | open |
| component joining, upper deck, residence, compiler | later/open |

A sufficient next theorem is:

> **Protected portal common-rounding theorem.**  Jointly choose an exact
> protected named-target flag table, a bounded resource-disjoint portal
> matching meeting every odd block of the positive fractional support, and
> a residual support which is balanced and fractionally perfect.

Alternatively it is enough to jointly choose a functional attachment
`vartheta` for which the predecessor graph has Hall.

The bounded portal flags can now be treated as free on the lower-target
side.  The canonical pull-clock denominator shows that the residual support
must be allowed to change by integral trades; it cannot be frozen to the
specific symmetric block histogram.  The all-depth cubic flag absorber is a
natural target-side trade, while the one-row `C5` portal is the minimal
turn-side parity repair.  What is still missing is a physical construction
in which those two absorber systems coexist and leave one residual
fractionally perfect balanced core.

## 9. Scope

Nothing in this note proves connectedness of the cycle cover, quotient
voltage, residence, arbitrary-width upper coverage, or terminal compiler
feasibility.  It also does not prove `B(k)+O(1)` or exact equality.  Its
proved gains are:

1. the corrected pull-clock theorem survives audit;
2. the exact common problem has a clean functional/TU face;
3. `C5`, not `C3`, is the first physical balancedness obstruction;
4. bounded prepared portal flags cost zero named-target sidecar;
5. the complete `k=5,d=2` common-turn census has no fractional/integral gap;
6. the `k=10` canonical pull histogram has an explicit one-copy denominator
   obstruction, proving that a successful rounding theorem must permit
   integral trades or another fractional decomposition.
