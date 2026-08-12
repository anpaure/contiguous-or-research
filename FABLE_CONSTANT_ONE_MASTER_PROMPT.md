# Master prompt: replace the global `sqrt(2)` constant by `1+o(1)`

You are working on the universal contiguous-OR problem.  Do **not** spend this
run on `k=11`, finite SAT search, another scalar lower bound, or another
unfactorable middle-row construction.

## Primary objective

Prove

```text
nu(k) <= (1+o(1)) W(k),
W(k)=C(k,floor(k/2)).
```

Equivalently, replace the current unconditional upper coefficient
`sqrt(2)+o(1)` by `1+o(1)`, so the relative excess `nu(k)/W(k)-1` tends to
zero.

The cleanest sufficient local theorem is:

```text
For some fixed delta>0, uniformly for every four-chain box
Q(ell_1,...,ell_4),

g_4(ell) <= width(Q(ell)) + O((1+sum ell_i)^(3-delta)).
```

By `SUBQUADRATIC_PRODUCT_AGGREGATION.md`, this implies the primary objective.
Uniformity includes zero, short, and highly unequal sides.

## Authoritative inputs

Read completely before acting:

1. `SUBQUADRATIC_PRODUCT_AGGREGATION.md` and its audit;
2. `CONSTRUCTIVE_CONSTANT_ONE_NEXT.md` and its audit trail;
3. `FOUR_BOX_POSITIVE_ROUTE_AUDIT.md`;
4. `VARIABLE_BAND_FOUR_BOX_FACTOR.md` and its audit;
5. `ALL_RADIUS_TRIANGULAR_PORTAL_BRAID_AUDIT.md`;
6. `TRIANGULAR_MIN_REPEATS.md` and its audit;
7. `FOUR_BOX_INTACT_BLOCK_BARRIER.md`;
8. `MATHEMATICAL_HANDOFF.md`, especially the four-box, triangular, factor,
   and pin sections.

The new audited triangular theorem may be used as a black box:

```text
g_triangle(R) <= 7R^2/8+O(R),
rho(R) <= 3R^2/8+O(R).
```

Its selective lift is valid.  The remaining linear loss per two-level lift
comes from duplicating the diagonal ladder and adding parity supplements.

## Exact missing target

Attack **one** of the following two routes, in this order of preference.

### Route A: subquadratic factorable triangular braid

Construct an invariant family with, for some fixed `epsilon>0`,

```text
rho(R) <= rho(R-2)+O(R^(1-epsilon)),
```

or directly `rho(R)=O(R^(2-epsilon))`.

This requires sharing or absorbing **both** the repeated diagonal ladder and
the parity-supplement peaks.  Removing only the ladder leaves a linear
increment and is not enough.

Crucially, the output must be a **factorable** triangular braid, not merely a
word covering abstract upper joins.  It must simultaneously provide:

1. every residual upper target as a contiguous join;
2. replacement/preservation of all central-square intervals;
3. one monotone linked interval band `I_i=[i+alpha_i,i+beta_i]`;
4. every reflected lower meet with a nonempty core
   `J_(u,v)=[v+alpha_v,u+beta_u]`;
5. coordinate pin survival for all central intervals and all lower cores.

The sufficient factor/pin criterion in `FOUR_BOX_POSITIVE_ROUTE_AUDIT.md`
must be checked literally.  A triangular trail, meet word, or list of abstract
providers without these five properties does not imply an OR word.

### Route B: global repetition absorption

Keep the audited `rho(R)=3R^2/8+O(R)` local braid, but prove that its repeated
ladder/supplement occurrences can be shared across the SCD four-box
decomposition so their **total** contribution is `o(W(k))`.

This must be a physical-word sharing theorem: identify the same occurrences,
show which boxes use them, prove that all assigned intervals remain
contiguous and uncontaminated, and verify the common coordinate pins.  Merely
dividing a local count by an expected multiplicity is not a proof.

## Closed or low-value directions

Do not return any of the following as progress:

* an improvement only for equal four-cubes;
* a bound that excludes zero or highly unequal chain heights;
* another concatenation of independently solved fixed-depth bands;
* a triangular word whose reflected half supplies meets but no common factor;
* a recurrence with `Theta(R)` new repetitions per level;
* an unproved claim that central-square targets can be restored later;
* a target count, average-capacity calculation, or scalar blocker inequality
  with no ordered/pin realization;
* finite evidence at `R=6` without an all-radius invariant.

The endpoint-blocker theorem in
`BLOCKER_BARRIER_AND_CONTAINMENT_SPECTRUM.md` has passed independent audit;
see `BLOCKER_BARRIER_AND_CONTAINMENT_SPECTRUM_AUDIT.md`.  Treat every
single-family endpoint-chain, antichain, bounded-height, fractional, and
nested containment-Hall refinement as a closed lower-bound strategy: their
optimal containment spectrum collapses exactly to `B(k)`.  Keep this run
constructive unless you prove a genuinely non-nested named-cell or pin
coupling.

## Required working standard

1. State the invariant and recurrence before doing asymptotics.
2. For every proposed splice, list the target classes and give their exact
   witnessing intervals.
3. Prove no inserted/shared cell contaminates those intervals.
4. Track the interval-band endpoints and legal pin sets explicitly.
5. Give an executable constructor and exhaustive checker for at least
   `R=0,...,50` whenever the claim is finite/combinatorial.
6. Derive the local error exponent and then substitute it into the aggregation
   theorem; do not claim a global constant from analogy.
7. If the desired lemma is false, isolate the first unavoidable linear-cost
   family and prove a lower bound for that precise invariant.  A rigorous
   obstruction is preferable to speculative prose.

## Deliverable

Produce one paper-style note with exactly one of these verdicts:

```text
PROVED: a uniform four-box error O(S^(3-delta));
PROVED: a factorable triangular recurrence with sublinear increment;
PROVED: a global repetition-absorption theorem;
or
NO-GO: a rigorous obstruction to the chosen invariant, with the next
minimal escape stated precisely.
```

Separate every theorem from every conjecture.  End with the exact implication
for `limsup nu(k)/W(k)`.  Do not claim the `1+o(1)` result unless the full
factor/pin and uniform aggregation chain is complete.
