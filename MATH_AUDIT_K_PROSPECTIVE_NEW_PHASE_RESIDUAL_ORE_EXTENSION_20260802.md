# Independent audit of the prospective new-phase residual Ore extension

**Date:** 2026-08-02  
**Audited theorem:**
`MATH_THEOREM_K_PROSPECTIVE_NEW_PHASE_RESIDUAL_ORE_EXTENSION_20260802.md`  
**Verdict:** PASS for the owner/lower-`q1` factor row, subject to the explicit
arithmetic inequalities.  No two-corridor, history, charge, deeper-upper or
compiler conclusion follows.

## 1. Phase count and common-host check

The developed pump has `3k` projected edges and `6k` middle-level
incidences.  Removing one pump edge leaves `6k-2` incidences.  The direct
new phase contains three projected edges, hence six incidences, so its local
total is

\[
                         6k+4.                        \tag{1.1}
\]

The equivalent old presentation retains the closed pump and adds the two
old partner edges, hence also `6k+4`.  Therefore the residual increment over
the closed-pump Ore theorem is exactly four, and

\[
                         q_*=52d+62+4=52d+66.          \tag{1.2}
\]

The opposite phase cannot be selected accidentally after fixing one phase:
both phases use the same three lower facets, and the selected phase gives
degree two at each of them.  Thus those facets have zero residual demand.
This validates the common owner/lower host needed for the swap.  The argument
does not identify seam-specific sidecars or histories.

## 2. Literal residual-safe pair

The three-run signature audit proves internal pump incidence degree at most
three and external cross-degree one on both shores.  For one pump edge,
discard at most six `b` labels whose two relevant facets are internal pump
facets.  Then all three `b`-dependent partner owners and the first partner
facet are external.  Discard at most one `c` producing the third pump owner
through the target facet.  If the second partner facet were internal after
that discard, the remaining external owner would contain two pump facets,
contradicting cross-degree one.  This independently gives at least

\[
                         (m-7)(m-3)                   \tag{2.1}
\]

owner/lower-safe pairs for `m>=8`.

The replay

```text
scratch/audit_k_direct_new_phase_residual_ore_20260802.cpp
```

reconstructs every target edge for `1<=d<=8` and slack `0,1,3`.  It checks
the stronger owner/lower and immediate-upper exclusions literally.  The
minimum owner/lower-safe counts start

```text
d=1 slack=0 m=7  min_owner_lower=15
d=1 slack=1 m=8  min_owner_lower=35
d=2 slack=0 m=10 min_owner_lower=48
d=3 slack=0 m=13 min_owner_lower=99
```

and are positive in all tested cases.  This finite upper-`q1` check is
calibration only; the theorem uses only the all-`m` owner/lower proof.

The direct partner lies one additional Johnson step outside the original
local bank.  Replacing the 2648K radius `2d+4` by `2d+5` therefore suffices
for literal owner/lower disjointness.  Its ball volume remains
`exp(O(sqrt(m) log m))` when `d=O(sqrt(m))`, so the strengthened packing
condition is eventually automatic.

## 3. Ore cut audit

For every residual lower shore `S`, let

\[
 T=(L-F_P)-S,
 \qquad A=F_P\dot\cup T,
 \qquad c_A(Y)=(j_A(Y)-m+2)_+.
\]

Direct cancellation of protected incidences gives the exact equivalence

\[
 \operatorname{Ore}(S)
 \quad\Longleftrightarrow\quad
 \kappa(A)+\rho_{O_P}(A)
 \ge2|F_P|+\omega_{Q^\circ}(A).                       \tag{3.1}
\]

The protected term is nonnegative waste.  It is bounded by `q_*`, and an
edge-minimal failed extension has size at most both `q_*` and `2|T|`.

The underlying residual-curvature theorem was independently audited in

* `MATH_AUDIT_K_TWISTED_C6_RESIDUAL_ORE_CURVATURE_20260802.md`, and
* `MATH_AUDIT_K_TWISTED_C6_THEOREM5_POLYNOMIAL_CORE_20260802.md`.

Its proof checks all shores, not merely a sampled atlas:

1. degree `m-1` and codegree one close the small-shore and small-complement
   ranges;
2. Tanner's bound localizes a hypothetical failure to one polynomial-size
   full shore;
3. the small-`S` Lovasz--Kruskal--Katona branch gives coefficient
   `a_m`; and
4. the small-complement branch gives coefficient `c_m`.

Substitution of `q_*` into the same inequalities therefore proves every
Ore shore and invokes integrality only through the standard bipartite
`b`-factor theorem.

## 4. Independent arithmetic replay

The audit program evaluates the exact Ore inequalities through `m=300000`
and independently checks the logarithmic Johnson-ball separation inequality
at each reported threshold and at `m=300000`, for

\[
                         d=\lfloor C\sqrt m\rfloor.
\]

With state-encoded histories (`q=q_*`) it reports persistent passing from

```text
C=1: m=2825
C=2: m=10937
C=3: m=24457
```

through the audited range.  If four disjoint depth-`d` collar sides are
frozen literally (`q=60d+66`), it reports

```text
C=1: m=3729
C=2: m=14529
C=3: m=32529.
```

All twelve logged separation checks pass.  The thresholds are Ore-arithmetic
finite checks, not the asymptotic proof.  The proof
uses only `q=O(sqrt(m))`, while the three left margins in the arithmetic
conditions have orders `m`, `m^3`, and `m^2` against the corresponding
`O(sqrt(m))` or `O(m)` demands.

## 5. Scope and the minimal remaining family

The family of violating owner/lower Ore shores is empty under the displayed
hypotheses.  The
minimal remaining obstruction is therefore not an Ore shore.  It is one of:

* a failed role-separated two-corridor Hall shore after histories and
  capacity states are imposed;
* a nonzero frozen integer charge on that matching fibre; or
* a deeper-upper/source/compiler failure.

Unweighted degree and codegree cannot rule out the charge obstruction.  A
regular codegree-one bipartite graph with weight one on all edges incident
to one fixed left vertex has charge one in every perfect matching.  Hence
the additive-coboundary or charge-reversing-pair condition in the theorem is
genuinely extra and must remain in the two-corridor state.
