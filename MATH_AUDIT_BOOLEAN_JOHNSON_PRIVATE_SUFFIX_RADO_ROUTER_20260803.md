# Proof audit: Boolean--Johnson private suffix Rado router

**Date:** 2026-08-03
**Audited theorem:**
`MATH_THEOREM_BOOLEAN_JOHNSON_PRIVATE_SUFFIX_RADO_ROUTER_20260803.md`
**Method:** pure mathematics and theorem-scope audit.  No finite search,
solver, numerical construction, or computational experiment was used.
**Verdict:** **GO at the stated conditional scope.**

## 1. Exact conclusion audited

The theorem gives a negative and a positive conclusion.

* Negative: Boolean or Johnson expansion of set **values** does not imply a
  simultaneous physical suffix router.  Occurrence identities, terminal
  types, shared capacities, and the footprint of the frozen compensation
  linkage survive as independent data.
* Positive: after those data are fixed in one residual network, the weakest
  exact private-prefix condition is Rado's all-claim-subset inequality.  On
  an exact private occurrence lift it becomes a nested Hall theorem.  A
  literal `q1` factor-diamond lift is a transparent sufficient
  specialization.

The theorem therefore does not close the all-dimensional `B+1` host.  It
identifies the exact residual premise and proves that several more semantic
premises are insufficient.

## 2. Frozen compensation semantics

The residual network is formed only after one materialized state and one
fixed compensation linkage have been chosen:

\[
 D^{\rm res}=D^c-\operatorname{cap}(L_I),
 \qquad T^{\rm res}=T^c-T(L_I).
\]

This agrees with the frozen model in the terminal common-cap theorem and in
the private-router theorem.  It is not matroid contraction: the
compensation paths are not allowed to reroute after a gain subset is
selected.  Every theorem rank is therefore a residual rank after literal
capacity and sink deletion.

The order of operations is load-bearing:

1. fix the cap/guard/occurrence/type state;
2. fix and delete the compensation linkage;
3. reserve the claim-prefix interiors;
4. form the suffix gammoid; and only then
5. invoke Rado, Hall, or Boolean expansion.

Reversing steps 2 and 5 would silently certify routes through capacities
which the frozen background later removes.

## 3. Rado condition and rank formula

For each gain \(g\), the physical menu is \(A_g\subseteq P\), and the
suffix-linkable port sets are the independent sets of the strict gammoid
\(\Gamma\).  Under the stated private-prefix and complete-interface
hypotheses, a claim set is serviceable exactly when it has an independent
system of representatives in \(\Gamma\).

Rado's rank formula is

\[
 \rho(S)=\min_{X\subseteq S}
 \left(|S\setminus X|+r_\Gamma(A(X))\right).
\]

Consequently \(\rho(G)=|G|\) if and only if

\[
                       r_\Gamma(A(X))\ge|X|
                       \qquad(X\subseteq G).
\]

Both directions are exact.  Necessity follows by restricting a full
representative system to \(X\); sufficiency follows directly from the rank
formula.  The bounded-defect implication

\[
 r_\Gamma(A(X))\ge|X|-C
 \quad\Longrightarrow\quad
 \rho(S)\ge|S|-C
\]

is obtained by substituting the inequality into every term of the minimum.

The full-port condition \(r_\Gamma(P)=|P|\) is stronger.  If the
claim--port graph is left \(h\)-regular and right-at-most-\(h\), edge
counting gives \(|A(X)|\ge|X|\).  Full-port independence then implies the
Rado inequalities.  The converse need not hold because ports never needed
by an independent representative system may be suffix loops.

Thus the claimed weakening of the private-router premise is genuine and
proof-safe.

## 4. Nested Hall audit

When the suffix network is exactly a bipartite port--sink incidence graph
with private edge interiors, its port gammoid is the transversal matroid of
that graph.  Its rank is

\[
 r_\Gamma(Y)=
 \min_{Z\subseteq Y}
 \left(|Y\setminus Z|+|N_H(Z)|\right).
\]

Substitution in the Rado inequality gives

\[
 |A(X)\setminus Z|+|N_H(Z)|\ge|X|
 \qquad(X\subseteq G,\ Z\subseteq A(X)).
\]

No quantifier is missing: \(X\) ranges over claim subsets and \(Z\) over
port subsets of the associated union menu.  For the stronger task of
routing every port, Hall's deficiency theorem gives

\[
 |P|-r_\Gamma(P)
 =\max_{Z\subseteq P}\bigl(|Z|-|N_H(Z)|\bigr).
\]

If two edge bundles share an interior unit capacity, this transversal rank
is no longer valid.  The theorem correctly returns to the strict-gammoid
rank rather than duplicating that capacity.

## 5. Weighted Boolean-shadow audit

Let \(u(A)\) count active port occurrences of lower value \(A\), and let
\(w(B)\) count residual sink capacities of upper value \(B\).  In a complete
private occurrence lift, the neighborhood of any port-occurrence set
depends only on its lower-value support \({\cal F}\).  The largest demand
with that support takes all \(u(A)\) copies.  Hence occurrence Hall is
equivalent to

\[
 \sum_{B\in\nabla_b({\cal F})}w(B)
 \ge\sum_{A\in{\cal F}}u(A)
 \qquad({\cal F}\subseteq\tbinom{[n]}a).
\]

This equivalence explicitly counts physical occurrences rather than
distinct values.

For complete layers, every lower \(a\)-set has degree
\(d_L=\binom{n-a}{b-a}\), and every upper \(b\)-set has degree
\(d_R=\binom ba\).  Double counting yields

\[
 d_L|{\cal F}|\le d_R|\nabla_b({\cal F})|.
\]

Thus \(u(A)\le u_0\), \(w(B)\ge w_0\), and
\(w_0d_L\ge u_0d_R\) imply weighted Hall.  The identity

\[
 {d_L\over d_R}={\binom nb\over\binom na}
\]

verifies the equivalent layer-size form in the theorem.

On \([2r-1]\), ranks \(r-1\) and \(r\) have equal size and equal incidence
degrees, so one occurrence per value gives abstract Hall.  For ranks
\(r-1\) and \(r+1\), the layer ratio is

\[
 {\binom{2r-1}{r+1}\over\binom{2r-1}{r-1}}
 ={r-1\over r+1}<1.
\]

Therefore one occurrence per upper value fails already on the full-set
cut.  The theorem's uniform two-copy condition is sufficient, not claimed
necessary.

The surjective-multiplicity counterexample is also correct.  With
\(E=W-U\) extra upper occurrences concentrated on \(B_0\), take all lower
sets except the \(\binom{r+1}{2}\) lower subsets of \(B_0\).  At least
\(1+E\) terminal occurrences lie outside their neighborhood.  Whenever
\(1+E>\binom{r+1}{2}\), Hall fails.  Since

\[
 E={2W\over r+1},
 \qquad
 W=\binom{2r-1}{r-1}\ge2^{r-1},
\]

this holds for all sufficiently large \(r\).  The example attacks only
upper-value surjectivity.  A terminal bank with a bijective lower anchor
has an abstract matching; the theorem correctly distinguishes that stronger
ledger from its still-unproved physical lift.

## 6. `q1` factor-diamond audit

A spanning Middle-Levels two-factor is a disjoint union of even alternating
cycles.  Choosing one parity class on each component gives a perfect
matching from lower ports to owner occurrences.  If every chosen incidence
has the residual literal diamond

\[
                             p\leadsto o\leadsto q_p,
\]

then selected ports, owners, and the distinct \(q_p\) terminals are each
injective.  Private edge interiors account for every remaining physical
capacity.  The resulting suffix family is therefore a full linkage.

This is an unconditional theorem under the occurrence-lift hypotheses, but
not an unconditional lift theorem.  The diagonal-interval result proves the
native occurrence identities \(p_i-o_i-q_i\) and
\(p_i-o_{i+1}-q_i\).  Their survival after compensation deletion and prefix
reservation remains an explicit coexistence requirement.

Inside a single undeleted factor cycle, the only two perfect matchings are
the alternating parity classes.  After deleting incidence bundles while
retaining all vertices, a perfect matching remains exactly when one parity
class is untouched.  This verifies the residual-cycle statement.  Extra
physical suffixes can only improve rank, so failure of that canonical
subgraph is not claimed to obstruct the full gammoid.

## 7. Sharp obstruction audits

### One compensation path

The vertices \(v_1,\ldots,v_N\) support disjoint suffixes
\(p_i-v_i-q_i\).  A single compensation path may traverse all \(v_i\) in
series.  Freezing it deletes all \(v_i\), making every port a residual loop.
Thus one compensation claim can reduce rank by \(N\); a bound on the number
of compensation paths is not a damage bound.  This obstruction is exact
and keeps the deleted linkage explicit.

### Two occurrence coordinates

If both coordinates separately route into the same \(N\) unit sinks, each
marginal rank is \(N\), while the joint terminal cut has capacity \(N\)
against demand \(2N\).  Hence marginal Hall cannot replace capacity
separation, an allocated common state, or a proved legal coalescence of the
two roles.

### Terminal type

Untyped Hall permits illegal terminal permutations.  The theorem avoids
this by placing types in the network or in an exact type gadget before the
gammoid or Hall rank is taken.

## 8. Interface with the two-coordinate theorem

After removing the structural-zero set, for coordinate \(j\), Theorem 2.1
gives the Rado matroid induced by \(\Gamma_j\) and the menus \(A_{j,g}\).
Substituting those ranks into the exact two-matroid deficiency theorem gives

\[
 \delta=
 \max_{X_0\cap X_1=\varnothing}
 \left(
 |X_0|-r_{\Gamma_0}(A_0(X_0))
 +|X_1|-r_{\Gamma_1}(A_1(X_1))
 \right).
\]

This substitution is valid only after global product closure and all
cross-coordinate capacities have been resolved.  The deleted structural
zeros and background losses are then added separately exactly as in the
common-cap theorem.

The strongest proof-safe present conclusion is therefore:

> Boolean/Johnson expansion proves the required router if it is lifted to
> the residual typed occurrence graph and verifies the displayed Rado/Hall
> cuts.  The native diagonal factor diamonds close the occurrence geometry
> of one coordinate, subject to coexistence with the frozen background.  No
> theorem presently supplies the second residual coordinate lift or global
> product closure.

## 9. Dependency-scope check

The following inputs were used only at their proved scopes.

* `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`:
  frozen/adaptive separation, Rado rank, and exact two-coordinate
  deficiency.
* `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`:
  the full-active-port sufficient certificate and private prefix/suffix
  interface.
* `MATH_THEOREM_CROSS_SCD_SPARSE_TOP_COLLAR_ATTACHMENT_20260803.md`:
  uniform containment flow as an all-Hall-cut proof at the named value
  level.
* `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`:
  the abstract two-factor only; no physical router is imported.
* `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`
  and
  `MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md`:
  local literal pivot/ray and Johnson geometry only.
* `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`:
  the native one-coordinate occurrence diamonds and its explicit
  compensation/common-cap scope warning.
* `MATH_THEOREM_BOUNDED_DEPTH_RESCUE_CHAIN_ANCHORED_GAMMOID_CONTRACTION_20260803.md`:
  capacity-faithful interface requirements and fixed-compensation residual
  cuts.
* `MATH_THEOREM_BPLUS1_ONE_TOKEN_REGENERATIVE_OVERLAY_AND_FIXED_FIBRE_OBSTRUCTION_20260803.md`:
  one-coordinate closure and the remaining two-coordinate/common-cap reset
  premise.
* `MATH_THEOREM_BOOLEAN_INCIDENCE_OVERLOAD_SUFFIX_ROUTER_20260803.md`:
  a bounded-overload sufficient certificate, not an occurrence-lift
  existence theorem.

No cited result authenticates transported phase 1, constructs the missing
second occurrence coordinate, or proves an unconditional `B(k)+O(1)`
bound.  The audited theorem makes none of those claims.
