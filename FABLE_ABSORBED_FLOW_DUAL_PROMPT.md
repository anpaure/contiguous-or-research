# Fable task: close the all-k three-box bottleneck

Work on the general mathematics only. Do not work on `k=11`, finite SAT search, or certificate generation. Do not edit any existing project file. Put all of your work in new files whose names begin `fable_general_case/FABLE_ABSORBED_FLOW_`.

## Objective

The proved three-product-of-chains reduction would give

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}
\]

if the local three-chain box can be traversed with width plus subquadratic overhead. The remaining obstruction has been converted into a coupled marked-line/seam problem. Resolve that coupled problem, not a scalar relaxation of it.

Read these files in order and treat their status labels literally:

1. `PRODUCT_BOX_CONSTANT_ONE_REDUCTION.md`
2. `THREE_CHAIN_BOX_EXACT.md`
3. `MULTISCALE_DIRECTION_COUPLING_NEXT.md`
4. `MULTISCALE_DIRECTION_COUPLING_INDEPENDENT_AUDIT.md`
5. `MIXED_PROFILE_CROSSLINE.md`
6. `MIXED_PROFILE_CROSSLINE_AUDIT.md`
7. `ABSORBED_FLOW_COAREA.md`

First audit `ABSORBED_FLOW_COAREA.md` against the earlier definitions. Repair only in your own new file if needed. In particular, preserve physical predecessor-edge identities, seam identities, directions, line levels, gap lifetimes, successor identities, pairwise line intersections, and additive triple intersections. Never optimize different thresholds independently.

## Required mathematical target

Build one integrated multiscale variational formulation containing both:

- unabsorbed-seam savings from the exact contraction/gap argument; and
- absorbed-seam penalties from off-diagonal direction flow, positive-level line geometry, common edge lifetimes, pair intersections, and triple corrections.

Then obtain exactly one of the following two decisive outcomes.

### Outcome A: a rigorous dual certificate

Give an explicit nonnegative weight function or finite family of weights, all dual multipliers, and a fixed numerical `epsilon > 0`, and prove that every physically realizable broad marked process satisfies

\[
\inf_c U(c) \le 4-\epsilon.
\]

Every interchange of sums/integrals, boundary term, normalization, congestion bound, and equality case must be checked. A certificate that applies only to one atomic profile, only under `D=o(a^2)`, or only after forgetting directions/levels is not enough.

### Outcome B: a genuine physical survivor

Construct one coherent marked process, with common identities across all thresholds, satisfying all audited contraction, absorbed-flow, line-geometry, pair-intersection, additive-triple, and seam-service constraints while maintaining `U(c) >= 4` at every relevant threshold. It must be realizable by one marked line configuration, not merely a compatible collection of marginal profiles.

If neither outcome is reached, isolate the *single smallest missing lemma*: state it formally with constants, prove every reduction to it, and give either a credible proof route or an explicit near-extremizer showing why it is sharp. Do not branch into several vague future directions.

## Guardrails

- Do not claim the original OR problem is solved unless the implication through the product-box reduction is written in full and every hypothesis is proved.
- Do not use the earlier exact-atomic seal as if it handled mixed profiles or large defect; explicitly account for those cases.
- Do not replace common physical lifetimes by independent thresholdwise capacity bounds.
- Do not hide a factor proportional to the number of recursive seams.
- Aggressively adversarially audit your own proof. Separate proved lemmas, conditional deductions, counterexamples, and heuristics.
- You may use symbolic algebra or small numerical linear programs only to discover a certificate; the final certificate must be human-checkable and proved analytically.

## Deliverables

Write:

1. `fable_general_case/FABLE_ABSORBED_FLOW_RESOLUTION.md` — the complete argument or countermodel.
2. `fable_general_case/FABLE_ABSORBED_FLOW_AUDIT.md` — an independent line-by-line adversarial audit, including failed approaches and exact remaining gap if any.
3. `fable_general_case/FABLE_ABSORBED_FLOW_LEDGER.md` — a short theorem ledger listing inherited facts, new proved facts, conditional statements, and unresolved statements.

Continue until one decisive outcome is reached or the one minimal missing lemma is isolated and fully reduced. Use the enlarged response budget for sustained mathematical work, not for repeating the handoff.
