# Fable task: resolve the global radius-typed wreath construction

Work mathematically on the general asymptotic OR problem, not on `k=11` and
not on another finite search.

## Goal

Prove, or make a proof-grade advance toward,

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

The cleanest current sufficient object is a near wreath-resolved symmetric
chain decomposition of the central Boolean band.

## Read first

Read these files completely and respect every scope qualification:

1. `PARTIAL_BLOCK_MULTISCALE.md`, especially Sections 8--12.
2. `MSW_ATOM_FLOW.md`, especially Sections 2, 6, and 7.
3. `ASYMPTOTIC_MATCHING.md`.
4. `TRUNCATED_IDEAL_PRODUCT.md` and its audit.
5. `GK_TWO_SIDED_RAINBOW_FOREST.md` and `GK_PROJECTION_COUNTS.md`.
6. `PORTAL_LINEAR_FACTOR_COUPLING_AUDIT.md` only for the warning that dense
   linked sharp turns cannot substitute for a genuine global factor.

## Exact target

Let `W=C(2m,m)`, choose

\[
H=\sqrt{m\,\omega(m)},\qquad \omega(m)\to\infty,
\]

arbitrarily slowly, and use long partial pair-flip blocks of half-length
`ell`, with `H=o(ell)=o(m)`.  The certification-depth probabilities

\[
p_0=1-\rho_1,\quad p_d=\rho_d-\rho_{d+1},\quad p_H=\rho_H
\]

give the exact typed fractional matching in Section 8 of
`PARTIAL_BLOCK_MULTISCALE.md`.  Round it so that the total number of uncovered
middle and central-band masks is `o(W)`, not merely an `o(1)` fraction of the
`Theta(W sqrt(m))` typed vertices.

Equivalently, construct an SCD whose middle projection is a radius-preserving
permutation and whose ordered removal/addition labels satisfy the shift law

\[
r_i(f(X))=r_{i+1}(X),\qquad
u_i(f(X))=u_{i+1}(X)
\]

through the assigned radius, apart from `o(W)` total band vertices.

Together with the proved tail word, this immediately gives the desired
asymptotic OR theorem.

## Allowed routes

Pursue whichever route actually closes:

1. an explicit algebraic/group-action construction of a shift-compatible
   SCD or pair-flip wreath factor;
2. a quantitative growing-uniformity nibble/absorption theorem, with every
   degree, codegree, uniformity, and error parameter substituted explicitly;
3. a multistage rounding that first builds the two-sided rainbow depth-one
   forest and then extends radii while proving total defect `o(W)`;
4. a rigorous obstruction that rules out the present typed block family and
   identifies a strictly weaker sufficient object still implying the OR
   theorem.

## Guardrails

- Fixed-depth or fixed-uniformity diagonalization is insufficient: `H` must
  exceed `sqrt(m)` by a diverging factor.
- A matching leaving `o(W sqrt(m))` typed vertices is insufficient; the
  required total defect is `o(W)`.
- Random/Poisson coverage fails in shallow ranks, whose mean is near one.
- The standard Greene--Kleitman projection is macroscopically nonbijective
  and cannot be repaired in `o(W)` changes.
- Cite a modern matching theorem only after checking its growing-uniformity,
  ambient-size, codegree, and quantitative-error hypotheses from the paper.
- Do not turn a fractional identity, capacity calculation, or LP feasibility
  check into an existence claim.
- Audit every claimed theorem adversarially before entering it in the handoff.

## Deliverable

Write early, in small safe edits, to

`fable_general_case/FABLE_WREATH_RESOLVED_SCD.md`.

If a theorem is obtained, also write

`fable_general_case/FABLE_WREATH_RESOLVED_SCD_AUDIT.md`.

State precisely what is proved, what remains conditional, and whether it
actually implies the all-`k` asymptotic OR theorem.

