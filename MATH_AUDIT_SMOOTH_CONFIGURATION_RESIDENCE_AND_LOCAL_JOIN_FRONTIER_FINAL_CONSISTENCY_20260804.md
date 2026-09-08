# Final independent consistency audit: smooth-configuration synthesis

**Date:** 2026-08-04  
**Verdict:** **GO.**  The current synthesis correctly incorporates complete
Bellman positivity through grid size five, keeps every router conclusion
conditional on its literal physical hypotheses, and makes no unconditional
all-(k), exact-equality, or additive-constant claim.

No synthesis byte was edited during this audit.

## 1. Exact binding

| role | file | SHA-256 |
|---|---|---|
| audited synthesis | `MATH_SYNTHESIS_SMOOTH_CONFIGURATION_RESIDENCE_AND_LOCAL_JOIN_FRONTIER_20260804.md` | `75e586bc725e15a64f8942e841c0265ae6e103849243672d822d93138dff438b` |
| complete `n<=5` theorem | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| complete `n<=5` audit | `MATH_AUDIT_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_INDEPENDENT_20260804.md` | `8e853c0b47b177129a25a4a28741d42ca2f5df665775cd6cc074a604e2de8d9f` |
| factor-restricted router | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` | `09acd8673956a2e43ec97d1d67ff01d4e3ceb1ea230af0e796a762b84d142906` |
| factor-router audit, formatting-rebound | `MATH_AUDIT_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_INDEPENDENT_20260804.md` | `e9aed2a8806eaa47dcc3c6f01b207f656f0d6a0f7517a010a98172f54cf7525c` |
| private regular-factor router | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` | `2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0` |
| two-coordinate common-cap theorem | `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md` | `108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc` |
| common-cap/private-router freeze audit | `MATH_AUDIT_TERMINAL_COMMON_CAP_PRIVATE_ROUTER_FREEZE_20260803.md` | `18976c12ba4ad8111b17060865ed5b392722d67583b9041a5632725baeef5b90` |

The only repair made while preparing this audit was in the independent
factor-router audit: its reproduced inequality had plain text `le` instead
of `\le`.  Restoring that one formatting backslash changed no theorem byte
or mathematical statement.  The audit records its own former SHA and the
unchanged theorem binding explicitly.

## 2. Current five-slot verdict

The synthesis's current conclusion is unambiguous:

* every internally superadditive Bellman table with at most five active
  slots has strictly positive functional;
* a finite counterexample, if one exists, has grid size at least six; and
* grid six and larger remain open.

Earlier sentences saying that grid five was the first possible
counterexample, or that a counterexample had been reduced to selected
five-slot branches, are explicitly historical-stage statements appearing
before the subsequent branch closures.  They are not stated as the current
verdict.

The branch summary agrees with the authenticated `n<=5` theorem and audit:

1. `n<=4` is inherited from the complete four-slot theorem.
2. First-crossing deletion precedes endpoint saturation, and the least
   maximum-density split is then exhaustive over sizes `2,3,4,5`.
3. Size two is closed by the two-pulse wedge theorem.
4. Genuine size five lies on `c_5=A` and has endpoint margin `1/400`.
5. Size four consists of the active threshold face and exactly two inert
   composites, all closed by the cited train theorems.
6. Size three consists of the active endpoint plus the short train
   `mathcal R` and the retained-pulse/long-train exit.  The synthesis uses
   the current short-train derivative theorem and the current joint-convex
   tangent theorem for `mathcal P`, exactly as the complete theorem does.

The dependency hashes in the complete theorem and its independent audit
match the current workspace, including the current short-train theorem
`8f7e7cae...` and long-train theorem `19f8a5a2...`.

## 3. No overclaim of the general conjecture

The synthesis header says explicitly that neither
`nu(k)<=B(k)+O(1)` nor `nu(k)=B(k)` is proved.  Section 7 assumes one
compatible selected odd spine satisfying seven materialized gates before
deriving `nu(k)<=B(k)+C`; it immediately labels this an implication rather
than an existence theorem.  Section 8 again states that no `B+O(1)` theorem
has been proved and locates the remaining gap in the integral construction.

Thus complete finite Bellman positivity through five is not conflated with
the all-grid Bellman inequality, a resident carrier, the common-cap object,
or the desired OR-word theorem.

## 4. Router scope

The synthesis accurately distinguishes four levels.

1. On the one-step Boolean face, the displayed neighbourhood inequality
   gives a simultaneous suffix router under the stated typed-extension and
   forbidden-bank bounds.
2. For a general claim-to-port factor, exact feasibility is the
   factor-restricted Rado condition

   \[
   r_\Gamma(N_B(X))\ge |X|\qquad(X\subseteq G),
   \]

   equivalently the trapped-menu cuts; the degree-weighted flow is only a
   sufficient certificate.
3. A capacity-faithful typed bidirected Middle Levels corridor is a
   sufficient conditional realization at the required scalar scale.
4. The current protected factor supplies only the abstract incidence
   factor.  It does not supply the physical port map, private prefixes,
   typed suffix corridor, or compatible two-coordinate product state.

The synthesis explicitly includes the common unit-suffix bottleneck, so it
does not infer a router from a factor plus a parent/reference matching.
For two occurrence coordinates it retains the fixed-cap, product-closure,
shared-capacity, structural-zero, and transported-phase hypotheses of the
V2 common-cap theorem.  Transported phase 1 remains theorem input only.

## 5. Retraction and formatting audit

The retracted five-slot reverse-monotonicity theorem is not cited as a
positive dependency.  The synthesis describes the successful short-train
proof through its independently audited `q=1,2` derivative argument, not
through the retracted endpoint comparison.

Markdown display delimiters are balanced in the synthesis and in every
bound theorem/audit listed in Section 1.  Headings, tables, lists, tags,
boxed displays, inline code, and inequality directions are structurally
well formed.  The earlier formatting-failed unversioned common-cap draft is
mentioned only in the freeze audit as **DO NOT CITE**; the synthesis uses
the V2 theorem instead.

## 6. Final verdict

All requested consistency checks pass.  The current synthesis may be cited
as a proof-safe frontier document with these two principal conclusions:

* finite carry-aware Bellman positivity is complete through grid size five;
* the additive-constant construction remains open because the lower
  configuration, resident selector/splice, upper occurrence section, and
  literal common-cap/router hypotheses have not yet been co-instantiated.
