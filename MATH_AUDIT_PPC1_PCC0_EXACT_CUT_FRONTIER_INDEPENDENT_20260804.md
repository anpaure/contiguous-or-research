# Independent scope audit of the `PPC(1)` / `PCC(0)` cut frontier

**Date:** 2026-08-04
**Audited synthesis:**
`MATH_SYNTHESIS_PPC1_PCC0_EXACT_CUT_FRONTIER_20260804.md`
**Frozen synthesis SHA-256:**
`704a81661b39593adcfdcb9c21f9cd2e76e0db9c6860d52c1ff35a4340dd4c0e`
**Method:** independent symbolic implication, quantifier, and scope check;
no computation or search evidence is used as mathematical evidence.

## 0. Audit verdict

**PASS as a conditional synthesis.**

The synthesis preserves the exact finite status `nu(k)=B(k)` for
`0<=k<=16` and makes no new claim at `k=17` or in all dimensions.  Its
three named missing statements have the correct strength:

* `PPC(1)` is a zero-omission theorem on the odd one-pivot scaffold and a
  charge-at-most-one theorem on separate even taps;
* `PPC(C)` for one absolute finite `C` is sufficient only for `B+O(1)`;
* `PCC(0)` is an architecture-relative exact-`B` co-instantiation theorem,
  not a necessary condition on every conceivable exact construction.

No exact cut equivalence is promoted to simultaneous existence of its
witnesses.

## 1. Terminal charge and sharp constants

For a fixed literal terminal word `Z`, appending a shortest repair word for
the complete omitted family preserves every old witness and supplies every
omitted target.  The final length is exactly

\[
 |Z|+R({\cal H}(Z))=B(k)+c(Z)+R({\cal H}(Z)).          \tag{1.1}
\]

Therefore the synthesis's three implications from `tau=0`, `tau<=1`, and
uniformly bounded `tau` are valid.  Exact `B` also uses the independent
general lower bound.

On the odd pivot route, the inserted letter gives `c=1`.  Under the
nonnegative integer charge convention, `tau<=1` forces `R(H)=0`, and a
zero-length repair is possible only for `H=emptyset`.  The synthesis
correctly does not apply that conclusion to an arbitrary even tap.  There
the three charge-at-most-one possibilities are

\[
                 (c,R)=(1,0),(0,0),(0,1).             \tag{1.2}
\]

A sharp all-`k` `B+1` statement must verify every finite dimension before
the spine begins at the same sharp constant.  Only an unspecified additive
constant can absorb a worse finite prefix.  This caveat is present in both
`PPC(1)` and `PCC(0)` formulations.

## 2. Lower-side audit

### 2.1 Balanced path cover

The floor/ceiling owner-path theorem is an integral lower-bounded-flow
argument.  The symmetric fractional flow sends `W/C_s` through each
rank-`s` Boolean node; Boolean degree identities give conservation, and
network integrality gives one unit path from every owner.  Since
`C_s<=W` below a widest rank, every lower target is visited.  This proof is
parity-free at the stated widest-rank scope.

It controls each rank marginal, not the alignment of visitor partitions at
different ranks.  The synthesis preserves this distinction.

### 2.2 Exact multisocket cuts

For a fixed path bank, the target-assignment network has rank demands
`N_s`, unit target capacities, visitor incidences, and path capacity `d`.
Fixing a source-side rank set and path set `Q` and minimizing over target
placements yields the deficiency

\[
 \max_Q\left[
  \sum_s(e_s(Q)-b_s)_+-d|Q|
 \right]_+.                                           \tag{2.1}
\]

Thus the synthesis states an if-and-only-if only for the adaptive-boundary,
capacity-only named-flag problem on a fixed path bank.  It does not claim
that every balanced bank, or any known balanced bank, passes these cuts.

For `R=P-Q`, full visitation gives `e_s(Q)=C_s-u_s(R)`.  Substitution of
`N_s=C_s-b_s` and `L=dW-sum_sN_s` gives exactly

\[
 \sum_s\min\{u_s(R),N_s\}\ge d|R|-L.                 \tag{2.2}
\]

The signs and cap are correct.  Residual rank nonadjacency acts on the same
path/rank variables as named-target uniqueness and is absent from this
one-commodity flow.  The synthesis correctly records the stronger coupled
zero--one system as still open.

### 2.3 Fixed versus variable slots

For fixed complete-layer banks, normalized containment weights give a
fractional bipartite matching whenever the scalar rank transport is
feasible; bipartite integrality gives the named matching.  Independent
interface matchings form a ladder because bank indices strictly decrease.

Choosing the slot of each named target adds partition rows across time
copies.  The companion audit exhibits determinant-`2` minors and a literal
bounded-chain integrality gap.  Hence the synthesis is correct to cite the
fixed-bank theorem but reject variable-slot TU rounding.

### 2.4 Random and container scope

The abstract balanced-partition expectation and factorial MGF are exact in
that abstract model.  Boolean visitor blocks instead satisfy
`V_s(S) subseteq U_s(S)`.  Coordinate stars therefore refute global
exchangeability without furnishing a bad Hall cut.

The later Boolean-local theorem adds only the following unconditional
items:

1. one-rank deterministic eligible-density upper and lower bounds;
2. shift monotonicity of the local hypergeometric **first moment**;
3. a Johnson-local boundary lower bound for its linear-incidence gap;
4. the coordinate-halfspace classification at rank `r-1`, half density;
5. safety of fixed-width principal-star forced cores and strict safety of
   the coordinate-halfspace local benchmark.

Discrete convexity does not apply to the realized block count or to the
log-MGF.  The synthesis therefore leaves exactly the needed uniform
multi-rank leakage/switching-container theorem open and does not infer the
all-subset family (2.1).

## 3. Upper retained-old and topology audit

Fixing the occurrence-labelled factor is essential.  Exact upper
representation leaves one occurrence of each colour, so the deletion
complement uses quota `b_R=mu_R-1`.  A subset of a cycle cover is a forest
exactly when the deletion meets every old cycle.  A target survives exactly
when some witness interval avoids the deletion.  Therefore the synthesis's
four deletion conditions are jointly necessary and sufficient on this
fixed retained-old face.

The failure sets of one target are the transversals of its witness family.
Singleton transversals are exactly forced-cut cores, but a forest makes many
deletions; the complete minimal-transversal clutter is necessary.  The
occurrence-section natural join retains shared occurrences and is exactly
equivalent to the deletion formulation.  No running-intersection property
is asserted for the Boolean instance.

After a rainbow selector is fixed, component omission is a capacitated
Hall problem: each component demands one deletion and colour `R` supplies
`b_R` deletions.  Its exact deficiency is

\[
 \max_{Y\subseteq{\cal K}}
 \left(|Y|-\sum_{R:N_R^\sigma\cap Y\ne\varnothing}b_R\right). \tag{3.1}
\]

This agrees with partition--graphic matroid intersection after contracting
the protected bank.  The outer minimization over selectors remains
unevaluated, and compatible witness-token sets fail matroid augmentation.

For later connector topology, ordinary component-port Hall gives one path
plus cycles exactly when its deficiency is at most one.  A Hamilton path
needs an ordered endpoint Hall system, or else a separate serial
cycle-accessibility theorem.  The synthesis retains both qualifications.

## 4. Physical suffix and common-cap audit

The residual suffix graph is formed only after one materialized state, one
frozen compensation linkage, terminal types, prefix interiors, and shared
capacities are fixed.  Under the private-prefix interface, Rado's theorem
gives the exact all-claim condition

\[
 r_\Gamma(A(X))\ge|X|\qquad(X\subseteq G).             \tag{4.1}
\]

When suffix bundles form an exact private incidence lift, substituting the
transversal-matroid rank formula gives the nested Hall family

\[
 |A(X)\setminus Y|+|N(Y)|\ge|X|
 \quad(X\subseteq G,\ Y\subseteq A(X)).               \tag{4.2}
\]

These are occurrence-capacity statements, not consequences of Boolean
value expansion.  The factor-diamond theorem is unconditional only after
the complete residual physical diamonds are supplied.

For two coordinates, the displayed disjoint-subset maximum is the exact
two-Rado deficiency only after structural zeros are removed and global
product closure/shared-capacity allocation is proved.  The synthesis
states those as additional premises.  It does not infer a joint router from
two marginal Hall systems.

## 5. `PPC(C)` and `PCC(0)` quantifiers

`PPC(C)` requires one entire compatible odd sequence, not one independently
good child in each dimension.  Its schematic outer order is

\[
 \exists C,m_0\ \exists(g_m,O_m,E_m)_{m\ge m_0}\
 \forall m\ge m_0,                                    \tag{5.1}
\]

with the `g_m` forming one path and every listed lower, upper, topology,
router, replay, and export row witnessed in the same materialized state.
This is a single co-instantiation theorem even though its exact projections
are expressed by several cut families.

The even certificate is terminal-only.  It may have its own chronology,
cap, compiler, and repair, and different even taps need not be compatible.
If an even choice changes the exported odd child, it is no longer
terminal-only and must be co-instantiated with the odd transition.  The
all-parity constant is therefore `max(q_o,q_e)`, not their sum.

`PCC(0)` adds the architecture-specific cap-two selector, growing-depth
folded conversion, zero structural and Rado deficiencies, product closure,
and zero terminal charge.  None of the fixed-face selector or router
theorems supplies this intersection.  The synthesis correctly permits a
different exact architecture to bypass the folded converter.

## 6. Parity-toll audit

For even `K`, the closed top-bit splice of an odd word of excess `q` has
length excess

\[
 2q+\chi_K,
 \qquad \chi_K=2d_{K-1}-d_K\in\{d_K,d_K+2\}.          \tag{6.1}
\]

Since `d_K=Theta(sqrt(K))`, this does not turn an odd constant-charge spine
into all-dimensional constant charge.  If a new even word saves `s`
literal positions from that splice and its replay omits `H`, direct length
subtraction gives

\[
                  s-R(H)\ge2q+\chi_K-Q                \tag{6.2}
\]

exactly for a `B(K)+Q` conclusion.  Conditional bilayer dummy counts or
router slack are not a value of `s`.  The synthesis makes no such
promotion.

## 7. Claim-status ledger

| Statement | Audited status |
|---|---|
| balanced floor/ceiling path visitation | proved |
| fixed-bank adaptive multisocket deficiency | proved exactly |
| one bank satisfying all multisocket cuts | open |
| residual-nonadjacency named lift | open |
| fixed complete-layer ladder | proved |
| adaptive target-to-slot TU rounding | false as a generic inference |
| local first-moment compression and Johnson energy | proved |
| realized multi-rank switching/container bound | open |
| fixed-factor blocker/CSP equivalence | proved exactly |
| fixed-selector component omission min--max | proved exactly |
| full Boolean rainbow selector/forest | open |
| residual one-coordinate Rado/Hall criterion | proved exactly |
| missing occurrence lift and two-coordinate product closure | open |
| bounded-charge even taps | open |
| `PPC(1)` / finite-charge `PPC(C)` | open |
| architecture-relative `PCC(0)` | open |
| all-dimensional `B+O(1)`, `B+1`, or exact `B` | open |

## 8. Digest and file-scope check

All sixteen source digests in Section 7 of the synthesis were recomputed
against the workspace bytes and match the frozen theorem/audit files,
including the corrected final wave-7 and wave-8 hashes.  The synthesis
does not cite an interim wave hash as final.

No index, handoff, source theorem, or source audit is modified by this
audit.  Subject to the frozen synthesis hash at the top, the synthesis is
proof-safe and confidence-neutral.
