# Fable task: resolve the general three-box gate, not another finite case

Work mathematically on the general contiguous-OR problem. Do **not** work on
`k=11`, `k=14`, any finite SAT instance, or another local repair of q369.
The purpose of this turn is to obtain a theorem that changes the all-`k`
picture.

## Global objective

Let `g_3(p,q,r)` be the minimum length of a word of points of

\[
[0,p]\times[0,q]\times[0,r]
\]

such that every point of the box is the coordinatewise maximum of a nonempty
contiguous subword. Let

\[
w_3(p,q,r)=[z^{\lfloor(p+q+r)/2\rfloor}]
 (1+z+\cdots+z^p)(1+z+\cdots+z^q)(1+z+\cdots+z^r)
\]

be the width of the box.

The proved product-box reduction says that a **uniform** estimate

\[
g_3(p,q,r)\le w_3(p,q,r)+O((1+p+q+r)^c),\qquad c<2,
\]

with suitable uniformity for all aspect ratios (or a proved typical-box
version plus a negligible-tail estimate), would imply

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

Conversely, a uniform balanced-box theorem

\[
g_3(a,a,a)\ge w_3(a,a,a)+\Omega(a^2)
\]

would rule out this entire constant-one architecture. Resolve this dichotomy,
or prove the strongest rigorous result that genuinely crosses the existing
mixed-profile barrier.

## Required starting record

Read these files completely before acting:

1. `PRODUCT_BOX_CONSTANT_ONE_REDUCTION.md`
2. `MIXED_PROFILE_SEAM_NEXT.md`
3. `MIXED_PROFILE_CROSSLINE.md`
4. `MIXED_PROFILE_CROSSLINE_AUDIT.md`
5. `EXACT_ATOMIC_SEAM_ENVELOPE.md`
6. `EXACT_ATOMIC_SEAM_ENVELOPE_INDEPENDENT_AUDIT.md`
7. `MATHEMATICAL_HANDOFF.md`, especially Sections 107--139 and 162, 165,
   168, 172, and 178.

Treat audited results as black boxes only within their stated hypotheses.
The exact atomic seal exhausts the one-atom, one-threshold optimization. Do
not spend this turn improving its scalar constant.

## The unresolved mathematical gate

The broad profile

\[
\mu(dx)=2\mathbf 1_{[1,2]}(x)\,dx
\]

and similar non-atomic profiles admit feasible ledgers **separately at every
threshold**. Those ledgers are not known to arise from one ordering. The
missing information is simultaneous:

- all threshold tails come from one direction-labelled length/level measure;
- predecessor/successor couplings come from one cyclic order;
- absorption uses the same physical coordinate lines at every threshold;
- gaps are shared across scales rather than reallocated independently;
- additive triple intersections and cross-line deserts come from the same
  three nested level sets.

Build the correct nested-threshold object explicitly. A natural form is one
global marked measure on `(length, direction, level)` together with one
stationary successor/gap coupling and shared line-capacity variables. Derive
every marginal, nesting, transport, and additive constraint that follows from
an actual word.

Then do one of the following:

### Route A: construction

Give an explicit family of three-box words with uniform subquadratic error.
Prove coverage, length, and uniformity. Carry the result through the exact
product-box aggregation and state the resulting asymptotic theorem for
`nu(k)`.

### Route B: no-go

Prove that the simultaneous multiscale constraints force
`D_a >= c a^2-o(a^2)` for some absolute `c>0` in every balanced three-box
word. Translate this into a rigorous `Omega(a^2)` excess for `g_3(a,a,a)` and
therefore a no-go theorem for the three-block constant-one reduction.

### Route C: strictly decisive intermediate theorem

If neither full route closes, prove a theorem that eliminates the broad
mixed-profile survivor or gives a realizable counterexample satisfying the
**simultaneous** constraints. Merely writing another thresholdwise LP,
optimizing a cutoff, or restating the remaining gate is not a deliverable.

## Guardrails

- No finite-`k` work and no heavy brute-force search.
- Do not assume atomicity, concentration, vanishing seam defect, direction
  balance, or independent thresholds.
- Do not infer realizability of independently feasible threshold ledgers.
- Keep direction labels, level locations, gap ownership, and additive triple
  terms until a proved inequality permits eliminating them.
- Test every exchange of limits, weak-convergence step, matching claim, and
  congestion charge adversarially.
- If a proposed lemma is false, construct a concrete counterexample and pivot;
  do not bury the failure under a weaker heuristic statement.
- Do not modify shared search code or the main handoff while working. Put the
  result in `FABLE_THREE_BOX_GLOBAL_RESOLUTION.md` and put an independent
  adversarial audit in `FABLE_THREE_BOX_GLOBAL_RESOLUTION_AUDIT.md`.

## Required final ledger

Your final response and files must distinguish:

1. fully proved new theorems;
2. inherited audited facts;
3. conditional consequences;
4. explicit counterexamples to failed subclaims;
5. the exact unresolved statement, if anything remains;
6. the implication for the global bracket
   \(W(k)\le\nu(k)\le(\sqrt2+o(1))W(k)\).

Success means materially changing the all-dimensional theorem ledger. It does
not mean accumulating another finite-case score or another scalar necessary
condition that the known broad profile already satisfies.
