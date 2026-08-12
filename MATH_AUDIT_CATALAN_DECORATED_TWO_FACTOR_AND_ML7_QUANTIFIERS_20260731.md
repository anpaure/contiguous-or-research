# Audit of the decorated 2-factor reduction and the `ML(7)` hexagon result

Date: 2026-07-31  
Status: independent implication/quantifier audit; two local wording corrections;
no all-dimension existence theorem

## 0. Verdict

The main implication in
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`
is correct:

> a spanning Middle Levels 2-factor carrying a componentwise Catalan
> decoration whose lift is acyclic on every factor component yields a
> perfect Boolean-diamond matching whose physical lift is a spanning
> `Cat_m`-path forest.

Hamiltonicity and component merging are genuinely unnecessary.  The proof
is componentwise because every turn edge and every residual cross edge uses
physical vertices belonging to one factor component.  The edge count then
forces exactly

\[
 \binom{2m}{m}-\binom{2m}{m-1}=\operatorname {Cat}_m
\]

path components.

The positive `ML(7)` theorem is also correct in its finite scope: one
explicit hexagon toggle repairs the displayed `m=4` obstruction, and the
transparent-hexagon criterion is an exact local preservation test for one
fixed decoration.  It does **not** prove, or nearly imply by itself, an
all-`m` recursion.  The missing quantifier is the existence, in every
dimension, of one globally correlated decoration and a compatible terminal
2-factor (or of a recursion whose full feasible-state relation has a
nonempty accepting root).

## 1. Exact weakest sufficient trace theorem

The cleanest formulation avoids conventions about marked and unmarked
components.

### Decorated 2-Factor Theorem, exact form

For every `m>=2`, there exist a spanning 2-factor `F` of `ML(2m-1)`, selected
occurrence sets `D_A,D_B`, and a perfect matching `R` of the unselected
occurrence graph such that:

1. the selected `A`-turn colours biject onto
   `binom([2m-1],m+1)`;
2. the selected `B`-turn colours biject onto
   `binom([2m-1],m-2)`; and
3. on every factor component, the physical graph formed by the selected
   turn shortcuts and the edges of `R` is acyclic.

On a component containing at least one mark, the residual perfect
matching exists exactly when consecutive selected occurrences have opposite
shores; it is then unique.  On an unmarked component either alternating
factor-edge phase is allowed.  The exact trace version of Item 3 is:

* an unmarked component is accepted;
* a wholly marked component is rejected; and
* a partially marked component is accepted unless every positive zero-run
  has length two and every one-run has odd length.

This is equivalent to the corrected theorem already recorded in the
decorated-2-factor note.  It is the weakest exact theorem presently isolated
inside the componentwise Middle-Levels support architecture.  It is only a
sufficient subclass of Catalan Linear Matching: an arbitrary linear diamond
matching need not extend to any Middle Levels 2-factor.

## 2. Audit of the factor-to-diamond implication

For a factor component

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
\]

a selected `A_i` uses the diamond

\[
 A_i\subset B_{i-1}\cup B_i,
\]

a selected `B_i` uses

\[
 \infty+(A_i\cap A_{i+1})\subset\infty+B_i,
\]

and a residual incidence edge `A_i B_j` uses

\[
 A_i\subset\infty+B_j.
\]

The two selected turn bijections use the two non-incidence palette banks
exactly once.  The residual perfect matching uses every remaining `A` and
`B` occurrence exactly once.  Therefore the resulting diamonds form a
perfect matching of the two Boolean shores.  The physical vertices used by
one factor component are its `B` occurrences together with its
`infinity+A` occurrences, so different factor components are vertex-disjoint
in the physical lift.  Acyclicity is consequently componentwise, not a
global coupling condition.

The all-marked correction is necessary and complete.  A wholly marked
component produces one rail cycle on its `B` vertices and one rail cycle on
its `infinity+A` vertices.  It cannot be accepted by applying the partial
trace face test vacuously.  The frozen `m=3` audit witnesses this literally.

The alternating-circuit statement is also correct, but is purely an
existential reconfiguration equivalence: the symmetric difference of two
2-factors decomposes into balanced red/blue closed trails, and toggling each
trail preserves degree two.  It supplies no reason that an accepting
terminal 2-factor exists.

## 3. Two wording corrections to the hexagon-transfer statement

### 3.1 Gap vertices are occurrence-labelled directed gaps

In Theorem 2.3 of the `ML(7)` note a gap vertex is said to be named by the
unordered pair of selected `A` endpoints.  That name is not always unique.
If a factor component has exactly two selected `A` occurrences, the two
opposite cyclic arcs have the same unordered endpoint pair but are distinct
gap occurrences and may have different colour neighbourhoods.  The exact
statement must use an occurrence-labelled oriented cyclic arc (or an
equivalent unique gap ID).  With that correction, the edge identity

\[
 \Gamma'=(\Gamma-D)+S
\]

and the contracted attachment-forest test remain valid.

### 3.2 A breaker is required on every output component

Corollary 2.2 is valid as written for a Hamilton-to-Hamilton toggle.  In the
componentwise 2-factor extension, one protected run somewhere in the old
factor is not sufficient if the toggle splits a component: the output
component not containing that run may land on the binary cycle face.  The
componentwise statement must require either

* a protected breaker on every output component, or
* the exact binary trace-face test separately on every output component.

This is already the stronger convention used in the later collar-state
note; it should be read back into the brief componentwise sentence of the
`ML(7)` note.

Neither correction affects the displayed `ML(7)` Hamilton-to-Hamilton
certificate or its finite census.

## 4. What the `ML(7)` result does and does not support

The finite result proves four useful facts:

1. the first `m=4` gap-Hall counterexample is a bad cycle, not a
   nonexistence theorem;
2. decorable `ML(7)` Hamilton cycles exist;
3. fixed-decoration transparency has an exact six-port test; and
4. leaf-peelability is not automatic under a transparent toggle.

It does not provide an inductive step.  In particular it does not prove:

* that every recursive dimension has an initially decorated factor;
* that the standard MMM gluing family contains a compatible spanning set;
* that pairwise transparent toggles share one common decoration;
* that the decoration interface has uniformly bounded adhesion; or
* that the correlated feasible-state relation has a nonempty root.

The explicit two-toggle `ML(7)` example with nonempty pairwise decoration
intersections but empty triple intersection rules out multiplying scalar
"this toggle is transparent for something" labels.  A recursion must carry
the correlated feasible-decoration relation, or prove a stronger private-
palette/leaf-peelable invariant whose nonemptiness is preserved.

After the decorated-2-factor quantifier drop, a transparent component-
spanning gluing tree is no longer the minimal target.  It remains a valid
strong construction route.  The sharper central question is simply whether
some terminal spanning 2-factor admits the exact decoration in Section 1;
its components need never be merged.

The feasible-decoration relation theorem also survives, but its root
acceptance sentence must be rebased.  In the Hamilton-restricted recursion
there is one terminal cyclic trace.  For the minimal 2-factor target, the
state must retain the component partition/order of its open trace fragments,
and at the root **every** resulting cyclic component is tested separately:
unmarked is accepted, wholly marked is rejected, and partially marked is
accepted exactly off the binary cycle face.  Matching degrees are still zero
on the empty boundary and the two turn palettes remain global.  Natural join
and existential projection remain exact; only the terminal topology predicate
changes.

## 5. Correct implication hierarchy

The honest hierarchy is

\[
\begin{array}{c}
\text{uniform repaired transparent Hamilton recursion}
\\ \Downarrow\\
\text{decorated Hamilton cycle}
\\ \Downarrow\\
\text{decorated spanning 2-factor}
\\ \Downarrow\\
\text{Catalan Linear Matching}.
\end{array}
\]

Only the final implication is presently proved for every dimension.  The
`m=4` transparent-hexagon theorem supplies one finite positive fixture and
an exact transition test, not either of the two all-dimension existence
statements above it.

Finally, Catalan Linear Matching is still only the central gate.  The full
identity `nu(k)=B(k)` additionally requires the residence, deeper-shadow,
seam/voltage, and integral lower-compiler conditions.  None follows from the
decorated-2-factor theorem.
