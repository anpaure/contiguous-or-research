# Audit of the shielded opposed-hinge macro rectangles

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_ROOT_SHIELDED_OPPOSED_HINGE_MACRO_RECTANGLES_20260802.md`  
**Theorem SHA-256:**
`931e5be7a548b8548f4a73a523811443a501e42bac6e7db832c3e2ff1dd9e2ff`

## 0. Verdict

PASS in the stated bounded-exception supply scope.

The two-cell formula is a genuine two-sided literal Cartesian macro, not a
projection of a correlated relation.  Convex contiguous-interval filtering
really does factor into independent left and right predicates.  The
Middle-Levels pairing proof also has the corrected endpoint aperture and a
single common predecessor phase: the transition through the omitted root is
deleted before the owner path is paired.

The scope restrictions are essential.

* The arbitrary-width factorization applies to contiguous intervals in one
  fixed global placement and quotient.  It does not apply to arbitrary
  nonconvex address sets or an extra automaton with a genuinely joint
  endpoint action.
* The owner factor makes paired immediate-lower roots distinct, but it does
  not assign the full strict-lower target table or make the immediate-upper
  colours complete.
* The connected Middle-Levels projection is not a literal full-`d` source
  skeleton.  The persistence cut in Proposition 6.1 can kill linearly many
  interpair ports.
* Neither the PCPS factorization nor the local rectangles proves the shifted
  macro-Hoffman inequalities, a global address/history section, a protected
  complete-state spanning skeleton, `B+O(1)`, or regeneration.

## 1. Independent check of the literal formula

For adjacent owners

\[
             T^-=R\cup\{a\},\qquad T^+=R\cup\{b\},
\]

and an ordered partition `R=D_1 dotcup ... dotcup D_d`, the proposed word is

\[
  (\{a\}\cup A,D_d,D_{d-1},\ldots,D_1,\{b\}\cup A'). \tag{1.1}
\]

Its first and second length-`d+1` unions are visibly `T^-` and `T^+`.
The initial state omits `D_1-A` and hence the guard `y`; the terminal state
omits `D_d-A'` and hence `z`; and the unique middle state has union `R`.
Thus none of the three states is saturated in an adjacent rank-`r` owner.

Only the first letter contains `A` and only the last contains `A'`.  Hence
the map from the two Boolean choices to the two endpoint tuples is injective
on each shore, and every cross-pair is the displayed physical word.  This
checks Cartesianity directly.

The left half is precisely the full-depth unsaturated hinge for layer order
`D_1,...,D_d`.  The forward right hinge for the reversed target chain is

\[
                  (\{b\}\cup A',D_1,D_2,\ldots,D_d).
\]

Reversing its whole trace gives the right half of (1.1).  Thus the proof does
not selectively reverse one state against a frozen exterior; it reverses
the complete second hinge before fusing at the common state.

## 2. Decisive convex-row audit

Let the variable positions of (1.1) be `u<v`.  For any contiguous global
interval `I` there are exactly four cases.

1. `I` contains neither endpoint: its value is fixed.
2. `I` contains `u` only: its value is a function of `A` only.
3. `I` contains `v` only: its value is a function of `A'` only.
4. `I` contains both: convexity puts the whole fixed middle block in `I`.
   That block has union `R`, while `A,A' subseteq R`, so the value is fixed.

Every exact interval-value row is therefore left-only, right-only, or
constant.  Point caps and pins have the same separation, and physical
address inequalities are fixed by the global placement.  An arbitrary
conjunction of these rows has feasible endpoint relation
`mathcal A times mathcal H`, or is empty.  This independently verifies the
load-bearing step of Theorem 3.1.

Nonconvex prescribed address sets would invalidate Case 4: such a set could
contain both variable endpoints while omitting a fixed core letter.  The
theorem correctly restricts its automatic factorization to contiguous
interval rows.  Likewise the global placement must be fixed first; pairwise
ports alone do not resolve identifications through a short intervening
component.

## 3. PCPS and history scope

With the fixed middle letters pinned and capped to equality, and the two
endpoint caps restricted as in (3.3), the PCPS Boolean closure theorem is
an exact nonemptiness test for words of the form (1.1).  Section 2 then
upgrades nonemptiness to a product of the two endpoint projections.

The owner chronology, transition root, immediate-upper colour, incidence
support and forced graphic forest are the same for every cross-pair.
Consequently the contracted Rado choice has no shared endpoint variable and
may be chosen independently, exactly as claimed.

For the owner-history automaton, initialize every coordinate with its bit in
`T^-` and clipped age `d+1`.  Reading `T^-` and then `T^+` accepts both the
`a:1->0` and `b:0->1` changes and gives one fixed output state.  This proves
that a nonempty signed-history slice exists locally and is independent of
`A,A'`.  It does not prove that these input/output states match around the
global macro order.  The theorem explicitly leaves that global history
section open.

## 4. Root-distinct pairing and endpoint phase

Take a Middle Levels Hamilton cycle containing the prescribed incidence
`o subset T_*`; incidence transitivity under coordinate permutations makes
this possible.  Index it

\[
 o=L_0,T_0=T_*,L_1,T_1,\ldots,L_{W-1},T_{W-1},L_0.
                                                               \tag{4.1}
\]

The parity matching `M_0(L_i)=T_i` is perfect.  Delete the owner transition
through `L_0=o` and orient the remaining owner path as

\[
                         T_{W-1},T_{W-2},\ldots,T_0.    \tag{4.2}
\]

For its transition `T_i -> T_(i-1)`, the intersection is `L_i`,
`M_0(L_i)=T_i`, and the supporting incidence `L_iT_(i-1)` is outside
`M_0`.  This is exactly the corrected terminal phase: the one omitted lower
root `o` is matched to and contained in the terminal owner `T_0=T_*`.

Pairing consecutive vertices of (4.2) covers every owner when `W` is even.
When `W` is odd it leaves exactly `T_0`.  The pair roots have distinct
indices, and the supporting incidences have distinct lower and owner
endpoints.  Thus the claimed incidence matching and one-exception count are
exact.  Contracting paired subpaths preserves the order and connectedness of
(4.2); it does not prove that the contracted joins have literal source-rail
overlap.

## 5. Rank range

The Cauchy--Schwarz calculation is sound:

\[
 {2r\choose r}=\sum_j{r\choose j}^2\ge {4^r\over r+1},
 \qquad W={1\over2}{2r\choose r}.
\]

Hence `Lambda/W<(r+1)/2<=r-3` for `r>=7`; the direct values at `r=5,6`
close the two remaining ranks.  The actual triangular depth therefore has
enough room to make both endpoint layers have size at least two for every
`r>=5`.

## 6. Persistence obstruction

The fixed letter at source position `d+1` contains the entering coordinate
`b`.  It lies in every depth window starting at `1,2,...,d+1`.  Therefore
`b` belongs to `T^+` and the next `d` owners of any literal continuation.
This proves Proposition 6.1 without a history approximation.  It is an
exact source-factor obstruction, and explains why the projected
Middle-Levels connector path is not yet a protected literal skeleton.

## 7. Finite replay

The independent script

`scratch/audit_root_shielded_opposed_hinge_macro_20260802.py`

has SHA-256

`bb4c52c6035cdc23223fddfb12700226da04d9be80cfa94beceb5225af64139d`

and returns

```text
PASS
literal_instances=2484
literal_cross_pairs=18336
interval_classifications=859
triangular_depth_ranks=96 max_depth=9
symbolic_terminal_phase_pairs=4392
```

The replay exhausts all ordered endpoint-wide partitions and all guards in
the tested ranks/depths, checks every endpoint cross-pair, the exact two
owner windows, all three unsaturated states, both target-ray formulas, and
the forward/reversed-hinge identity.  It then checks every interval in
padded representative blocks, one accepted signed-history slice, the
terminal-phase pairing indices, and the triangular depth inequality through
rank 100.

The finite replay is a regression for the formulas, not evidence for the
unproved global Hoffman, upper-completeness, compiler, or regeneration rows.

