# Independent audit of the decorated Middle Levels 2-factor reduction

Date: 2026-07-31  
Verdict: **correct after one necessary all-one-trace correction**; exact
factor-level weakening of the Hamilton target; no all-dimension existence or
`nu=B` theorem

## 1. Decisive correction

The first version of
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`
declared a marked component linear whenever it was off the mixed binary
cycle face

\[
 \text{all positive zero-runs have length two and all one-runs are odd}.
\]

That wording is false for an all-one trace.  A fully marked factor cycle has
no residual cross edges.  Its `A`-turn edges form one cycle on the `B` rail,
and its `B`-turn edges form a second cycle on the `infinity+A` rail.  It must
therefore be declared nonlinear.

The corrected source theorem now requires every marked component to contain
at least one unmarked occurrence before applying the mixed trace test.

## 2. Exact smallest counterexample

At `m=3`, put `Omega=Z_5`.  The cycles

\[
 A_i=\{i,i+1\},\quad B_i=\{i,i+1,i+2\},
\]

and, with successor `i -> i+2`,

\[
 A'_i=\{i,i+2\},\quad B'_i=\{i,i+2,i+4\}
\]

partition `ML(5)`.  Mark the first cycle completely and leave the second
unmarked.  On the marked cycle

\[
 \ell_i=\{i+1\},\qquad u_i=\Omega\setminus\{i+3\},
\]

so the two selected turn maps are global bijections and shore types
alternate.  Nevertheless the lift is

\[
                         C_5\sqcup C_5\sqcup5K_2.
\]

It has cyclomatic number two and seven components, not a
`Cat_3=5`-path forest.  This refutes only the omitted fully marked boundary
case; the unmarked-component construction is valid.

## 3. Complete local audit

For one factor component the exact physical cycle contribution is:

\[
\begin{array}{c|c}
\text{trace class}&\text{cycle rank}\cr \hline
\text{unmarked}&0\cr
\text{fully marked}&2\cr
\text{partially marked, mixed exceptional face}&1\cr
\text{partially marked, off face}&0.
\end{array}
\]

Thus, if `f` components are fully marked and `g` partial components are
exceptional, the global lift has cycle rank `2f+g` and

\[
                  \operatorname{Cat}_m+2f+g
\]

connected components.  It is a Catalan path forest exactly when `f=g=0`.

An unmarked `2q`-cycle has exactly two alternating residual phases.  Either
phase supplies `q` cross diamonds and lifts to `qK_2`.  Choices on `u`
unmarked components are independent (`2^u` choices) and consume no selected
turn-colour vertex, so there is no hidden global parity coupling.

## 4. Claims which pass unchanged

After the correction:

1. global upper/lower turn bijectivity plus componentwise alternating marks
   gives a perfect Boolean-diamond matching;
2. physical supports of distinct factor components are disjoint;
3. the lift has maximum degree at most two and, when acyclic,
   `2Q-(P+Q)=Q-P=Cat_m` path components;
4. any two spanning 2-factors are joined through a packet of unrestricted
   alternating circuits, with intermediate states only required to remain
   2-factors; and
5. Hamiltonicity and component merging are unnecessary for this central
   implication.

The circuit packet need not be bounded, ECO, transparent, residence-safe or
protected.  The factor-level target remains only the weakest currently known
**middle-levels-supported** trace architecture; arbitrary Catalan linear
diamond matchings need not admit such a representation.

## 5. Rebased constructive target

For a fixed factor, one global turn-augmentation perfect matching is exactly
a componentwise decoration, including the phase of each unmarked component.
Equivalently, after choosing an upper occurrence transversal, one solves the
global occurrence-labelled gap--lower-colour matching across all marked
components and rejects matchings with `f+g>0`.

This permits terminal ECO or other circuit moves to repair palette support,
gap Hall and trace parity without merging factor components.  It does not
settle residence, deeper shadows, RSB, seam chronology, voltage or the
common lower compiler, so no implication to `nu(k)=B(k)` is asserted.
