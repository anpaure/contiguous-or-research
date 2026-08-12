# Decorated Middle Levels 2-factors: global gap Hall and the exact cycle budget

Date: 2026-07-31  
Status: exact corrected factor-level reduction; exact smallest obstruction;
exact fixed-factor matching and preliminary flow criteria; no all-dimension
decorated 2-factor or contiguous-OR theorem

## 0. Rebased verdict

Hamiltonicity is unnecessary for the central Catalan Linear Matching
construction.  The correct weakest target in the current
middle-levels-supported architecture is a spanning 2-factor carrying one
global occurrence matching whose restriction to every factor component is
forest-safe.

There is one boundary condition missing from the first draft of
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`:
a fully marked component is never forest-safe.  Its turn edges form two
same-rail cycles.  The exact local cycle ledger is

\[
                   \mu=2f+g,                         \tag{0.1}
\]

where `f` is the number of fully marked factor components and `g` is the
number of partially marked components on the usual mixed binary cycle face.
Consequently the physical lift has

\[
             \operatorname{Cat}_m+2f+g               \tag{0.2}
\]

connected components, and it is a `Cat_m`-path forest exactly when
`f=g=0`.

After this correction, component merging, Hamilton voltage, and an ECO
incidence hypertree disappear from the minimal central target.  They remain
useful only for stronger recursive or downstream constructions.

## 1. Componentwise turn data

Fix `m>=2`, put `Omega=[2m-1]`, and let `F` be a spanning 2-factor of
`ML(2m-1)`.  Write a component `C` as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.               \tag{1.1}
\]

Its lower and upper turn colours are

\[
 \ell_i=A_i\cap A_{i+1},\qquad
 u_i=B_{i-1}\cup B_i.                                \tag{1.2}
\]

Select `A`- and `B`-occurrences over all components so that the selected
`u_i` enumerate every rank-`m+1` colour once, the selected `ell_i` enumerate
every rank-`m-2` colour once, and selected shore types alternate cyclically
on every component which contains a mark.

Call a component:

* **unmarked** if it has no selected occurrence;
* **fully marked** if every occurrence is selected; and
* **partially marked** otherwise.

On a partially marked component write the cyclic mark trace as

\[
                 1^{a_1}0^{b_1}\cdots1^{a_s}0^{b_s}. \tag{1.3}
\]

Alternation makes every `b_i` positive and even.  Call the partial component
**exceptional** when

\[
                        b_i=2\ \forall i,
             \qquad a_i\text{ odd}\ \forall i.       \tag{1.4}
\]

## 2. Exact local and global topology

### Theorem 2.1 (component cycle classification)

For the physical diamond lift induced by the selected turns and residual
factor edges, one factor component contributes the following cyclomatic
number:

\[
\begin{array}{c|c}
\text{component trace}&\text{cyclomatic contribution}\cr \hline
\text{unmarked}&0\cr
\text{fully marked}&2\cr
\text{partially marked and exceptional}&1\cr
\text{partially marked and nonexceptional}&0.
\end{array}                                           \tag{2.1}
\]

An unmarked `2q`-cycle has exactly two residual phases; either phase gives
`q` disjoint cross edges.  For `u` unmarked components these choices are
independent, giving exactly `2^u` residual phase assignments.

#### Proof

On an unmarked component, an alternating perfect matching of the factor
cycle covers every `A` and `B` occurrence once.  Every chosen factor edge
becomes one cross-rail physical edge, so the lift is `qK_2`.  The two phases
use no turn-colour vertex and hence do not couple across components.

On a partially marked component, deleting marked positions leaves even
paths with unique residual matchings.  The cyclic binary-trace proof is
component-local: a physical route closes around the component exactly when
every zero-run and every one-run transmits, which is precisely (1.4).  In
that event there is one physical cycle; otherwise every physical component
is a path.

On a fully marked component there are no residual cross edges.  The selected
`A_i`-turns join `B_{i-1}` to `B_i` and form one cycle on the `B` rail.  The
selected `B_i`-turns join `infinity+A_i` to `infinity+A_{i+1}` and form a
second disjoint cycle.  Thus the contribution is two.  (A four-cycle factor
component cannot occur in this consecutive-level incidence graph: two
distinct rank-`m` vertices containing the same two adjacent rank-`m-1`
vertices would both equal their unique union.)  \(\square\)

### Theorem 2.2 (exact global cycle budget)

Every componentwise decoration gives a perfect Boolean-diamond matching and
a spanning physical graph of maximum degree two.  If `f,g` have the meaning
in (0.1), its cyclomatic number is `2f+g` and its number of connected
components is (0.2).  Hence it is a `Cat_m`-path forest if and only if

\[
                              f=g=0.                 \tag{2.2}
\]

#### Proof

Global turn-colour bijectivity uses every noncross diamond-shore colour once.
On a marked component the residual even paths cover every unselected
occurrence once; on an unmarked component either residual phase does so.
Thus every lower and upper diamond-shore vertex is matched exactly once.

The physical vertex sets contributed by different factor components are
disjoint.  Theorem 2.1 therefore makes cyclomatic number additive and gives
`2f+g`.  Put

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2}.
\]

The physical graph has `2Q` vertices and the perfect diamond matching has
`P+Q` edges.  Since `2Q-(P+Q)=Q-P=Cat_m`, Euler's identity gives

\[
 \#\text{components}=|V|-|E|+\mu
 =\operatorname{Cat}_m+2f+g.
\]

Maximum degree two and `f=g=0` make every component a path.  \(\square\)

## 3. The smallest missing-boundary counterexample

### Proposition 3.1

The all-one trace must be excluded already for `m=3`.

#### Proof

Let `Omega=Z_5`, with subscripts modulo five.  The two cycles

\[
 A_i=\{i,i+1\},\qquad B_i=\{i,i+1,i+2\},             \tag{3.1}
\]

and, using successor `i -> i+2`,

\[
 A'_i=\{i,i+2\},\qquad B'_i=\{i,i+2,i+4\}            \tag{3.2}
\]

partition `ML(5)`.  Mark every occurrence of the first cycle and no
occurrence of the second.  On the first cycle

\[
 \ell_i=\{i+1\},\qquad
 u_i=\Omega\setminus\{i+3\},                         \tag{3.3}
\]

so both selected turn maps are global bijections and the marks alternate by
shore.  The original mixed-face wording declared the all-one trace safe,
because it has no positive zero-run and its single one-run has even length.
But its physical lift is two five-cycles, one per rail.  The unmarked second
component contributes five cross edges.  Thus the lift is

\[
                         C_5\sqcup C_5\sqcup5K_2,     \tag{3.4}
\]

with seven components and cyclomatic number two, rather than a
`Cat_3=5`-path forest.  \(\square\)

This is the smallest failure: at `m=2` the single upper and lower colour
cannot fully mark a factor component.

## 4. One global matching is the exact fixed-factor gate

Build the turn-augmentation graph `H_F`.  Its shores are

\[
 \mathscr A=\{\text{all }A\text{-occurrences of }F\}
       \sqcup\binom\Omega{m-2},
\]

\[
 \mathscr B=\{\text{all }B\text{-occurrences of }F\}
       \sqcup\binom\Omega{m+1}.                      \tag{4.1}
\]

For every factor edge add the corresponding `A--B` incidence edge.  For
every `A` occurrence add its upper-turn edge to `u_i`; for every `B`
occurrence add the lower-turn edge from `ell_i`.

### Theorem 4.1 (factor augmentation equivalence)

Perfect matchings of `H_F` are in bijection with componentwise Catalan
decorations, including one of the two cross phases on every wholly unmarked
component.  A perfect matching gives a Catalan path forest exactly when its
component traces satisfy `f=g=0`.

#### Proof

Every upper-colour vertex must match one `A` occurrence and every lower-
colour vertex one `B` occurrence, giving the two global turn transversals.
Every remaining occurrence is matched through a factor edge.  On each
factor component these residual edges form a perfect matching of the cycle
with the marked vertices deleted.  If the component is marked, this is
equivalent to even residual gaps, hence alternating mark types; if it is
unmarked, it is one of the two alternating cycle phases.  This construction
is reversible.  The last statement is Theorem 2.2.  \(\square\)

There is an equivalent gap-Hall form.  Choose one `A` occurrence for every
upper turn colour.  On each component with at least one chosen `A`, make one
cyclic gap between every consecutive pair of chosen `A` occurrences.  Form
the occurrence-labelled bipartite multigraph `Gamma_F(I)` from these gaps to
the lower colours, with one edge `(G,L;j)` for each `B` occurrence `j` of
colour `L` lying in gap `G`.

### Corollary 4.2 (global componentwise gap Hall)

The chosen upper transversal `I` extends to a componentwise Catalan
decoration if and only if `Gamma_F(I)` has a perfect matching.  The matched
edge occurrence `j`, not merely its colour `L`, determines the trace.  The
lift is a Catalan path forest if and only if some such perfect matching has
`f=g=0`.

Indeed, alternation requires exactly one selected `B` occurrence in every
`I`-gap; components with no selected `A` receive no selected `B` and remain
unmarked.

## 5. A polynomial preliminary component-balance obstruction

Before solving cyclic gap Hall, forget occurrence order and ask only whether
the two colour palettes can be assigned to components with equal mark counts.
Make the unit-capacity network

\[
 s\longrightarrow\mathcal U\longrightarrow\mathcal C
  \longrightarrow\mathcal L\longrightarrow t,       \tag{5.1}
\]

where `U` and `L` are the upper and lower turn-colour sets, `C` is the factor
component set, an arc `U--C` exists when colour `U` occurs as an upper turn on
`C`, and `C--L` exists when `L` occurs as a lower turn on `C`.  Colour arcs
at `s` and `t` have capacity one; internal arcs and component throughput have
capacity at least `P`.

### Proposition 5.1 (component-balance flow)

The network has flow value `P` if and only if all upper and lower colours can
be assigned to factor components, at occurring turns, so that every
component receives equally many colours from the two shores.

#### Proof

An integral unit of flow `U--C--L` pairs one upper and one lower colour on
component `C`.  A value-`P` flow saturates every colour vertex and therefore
gives the required assignments and equal component counts.  Conversely,
pair the upper and lower colours assigned to each component arbitrarily and
route the resulting units.  Integrality is ordinary network-flow
integrality.  \(\square\)

Failure of this flow is a literal obstruction.  Success is only necessary:
the cyclic gap-Hall condition and the local cycle budget `f=g=0` remain.

## 6. Constructive consequence and exact remaining target

Within the middle-levels-supported architecture, the weakest all-dimension
central target is

\[
 \boxed{\exists F\ \exists M\in\operatorname{PM}(H_F):
                   f(M)=g(M)=0.}                    \tag{6.1}
\]

Equivalently, find `F,I` and a perfect occurrence matching of
`Gamma_F(I)` with no fully marked or exceptional partial component.

This strictly weakens every Hamilton target:

* the raw canonical factor may be decorated directly;
* terminal ECO/circuit moves need repair only colour incidence, gap Hall, or
  trace parity, not component count;
* selected ECO atoms need not form a connected incidence hypertree; and
* wholly unmarked components simply contribute independent cross phases.

Any two spanning 2-factors are connected through unrestricted alternating
circuits, so the choice of starting factor creates no existential gate.
This does not imply connectivity through strict ECO atoms, bounded circuits,
transparent moves, residence-safe moves, or protected moves.

The exact fixed-factor failure hierarchy is:

1. a globally absent turn colour;
2. component-balance flow smaller than `P`;
3. gap-Hall failure for every upper transversal;
4. perfect gap matchings exist but all force `f+g>0`.

Separate upper/lower turn surjectivity remains insufficient; the audited
`ML(7)` example is already a one-component instance of Item 3.

The target (6.1) proves only central Catalan Linear Matching.  Residence,
deeper shadows, seam chronology, RSB, sockets/voltage and the common lower
compiler remain independent downstream gates for `nu(k)=B(k)`.
