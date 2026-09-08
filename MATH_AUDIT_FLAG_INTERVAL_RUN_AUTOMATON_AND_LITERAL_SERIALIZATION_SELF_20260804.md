# Self-audit: flag-interval run automata and literal serialization

**Date:** 2026-08-04  
**Method:** independent symbolic replay of definitions, implications, and
scope inside the proof; pure mathematics; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_FLAG_INTERVAL_RUN_AUTOMATON_AND_LITERAL_SERIALIZATION_20260804.md`  
**Verdict:** **SELF-GO at the stated fixed-factor, fixed-flag, fixed-address
scope.**

## 1. Address-to-age translation

For a flag

\[
 S_1\subsetneq\cdots\subsetneq S_m=Q
\]

at strict addresses

\[
 0\le\theta_1<\cdots<\theta_m=d-1,
\]

the threshold identity `F_(theta_j)=S_j` says exactly that a coordinate in
`S_j-S_(j-1)` has age in

\[
                         [\theta_{j-1}+1,\theta_j].
\]

The lower endpoint is strict because that coordinate is absent from the
preceding marked threshold; the upper endpoint is weak because it is
present at the current threshold. With `theta_0=-1`, the same formula
gives `[0,theta_1]` for the first block. Conversely, these intervals make
every marked threshold equal to its declared set. Thus (0.5) loses no
flag information.

The top address must be `d-1` on an oriented Johnson turn: its departing
coordinate has age `d-1` and belongs to `Q`. The theorem declares this
rather than deriving it from an arbitrary embedding.

## 2. Run recurrence

On a positive coordinate run:

- entry age is zero;
- a survivor either refreshes to zero or increments by one;
- age `d-1` cannot increment while remaining present; and
- departure age is `d-1`.

Therefore the forward image of a reachable set `R` is exactly

\[
                 \{0\}\cup\{a+1:a\in R, a<d-1\}.
\]

Intersecting with the next allowed-age interval proves the recurrence.
Requiring `d-1` at the final state is both necessary and sufficient, since
ordinary backtracking chooses one predecessor at every step. No condition
from another coordinate enters this recurrence.

The theorem assumes that no coordinate is present at every root, so every
cyclic positive run has an entry and a departure. Complete coatom-layer
factors satisfy this automatically. An arbitrary nonspanning Johnson cycle
with a coordinate present everywhere would instead need a cyclic, rather
than entry/departure, automaton; that case is deliberately outside scope.

## 3. Reconstruction audit

Choose one accepting age path independently on every positive run. At a
turn, the new source letter contains:

1. the unique newborn `beta_i`; and
2. every survivor assigned next age zero.

It is nonempty. Nonrefreshed survivors increment, refreshed survivors
reset, the oldest departing coordinate leaves, and the newborn enters.
Thus the next `d`-state is exactly `Q_(i+1)`, while the crossing
`d+1`-window is `Q_i union Q_(i+1)=T_(i+1)`. Since every present
coordinate belongs to exactly one positive run, independent choices do
not give conflicting age labels. This verifies the claimed absence of a
cross-coordinate product state.

## 4. Right-aligned specialization

For `c=d-m` and `theta_j=c+j-1`, the first age interval is `[0,c]` and
every later interval is the singleton `{c+j-1}`. Hence the theorem's
“forced tail, flexible bottom core” description is exact. Flexibility of
the bottom core is still constrained over time by the same run automaton;
the note does not treat its coordinates as freely reset at each root.

## 5. Waste implication

The lower-waste corollary assumes, rather than proves, that at least
`Lambda-C` distinct marked targets survive the linear opening and collar
replacement. Under the separately stated residence, halo, `W>2d`, and
`r>=2d` hypotheses, the existing desaturation theorem gives `R_A=0` and
the endpoint theorem gives

\[
 D_A=(\Lambda+\sigma)-|\operatorname{support}(A)|.
\]

Literal survival of `Lambda-C` pairwise distinct marks gives support at
least that large, hence `D_A<=sigma+C`. No cyclic-to-linear preservation
is inferred merely from automaton acceptance.

## 6. Counterexample audit

For `d=2`, in the turn

\[
 \{1,2,4\}\longrightarrow\{1,3,4\},
\]

the flags `{1} subset Q` and `{3} subset Q'` force coordinate `4` to age
one on both sides. A surviving age-one coordinate must reset to age zero;
the formal increment to two is forbidden at depth two. The departure `2`
is in the old
terminal block and the birth `3` is in the new bottom block, so both
endpoint tests pass. This verifies the claimed strict separation between
endpoint apertures and full run compatibility.

## 7. Exact exclusions

The theorem does not establish:

- feasibility of the joint-start type table;
- selection of flag addresses making all automata accept;
- a one-component protected factor;
- owner-palette-preserving component fusion;
- a collar-compatible opening retaining the marked bank;
- arbitrary-width upper coverage or common-cap compilation; or
- `nu(k)<=B(k)+O(1)`.

Its exact new content is the iff reduction and reconstruction after the
factor, named flags, and addresses have been fixed, plus the conditional
transfer from `Lambda-C` retained named marks to `D_A<=sigma+C`.
