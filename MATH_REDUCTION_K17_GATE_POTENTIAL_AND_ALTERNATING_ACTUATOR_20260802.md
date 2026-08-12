# The `k=17` gate potential and alternating-actuator reduction

## Status

This note records an exact progress measure for the current equivariant
`k=17` carrier campaign.  It is a reduction and an authenticated finite
observation, not a proof of a resident upper-complete carrier and not a
`k=17` word.

## 1. Integer gate coordinates

On the current `Z_17`-equivariant connected factor, let

```text
P  = number of positive coordinate runs of length 1, 2, or 3,
H11 = number of missing rank-11 consecutive-owner unions,
H12 = number of missing rank-12 consecutive-owner unions.
```

Rank 10 is already complete by the cap gate, and ranks 13 through 17 are
complete in every promoted state below.  Literal orbit audits show that
`P`, `H11`, and `H12` are multiples of 17.  Define

```text
Psi = (P + H11 + H12) / 17.
```

Thus `Psi` is a nonnegative integer.  Moreover, on this fixed flat-carrier
face, `Psi=0` is exactly the conjunction of:

1. the depth-three positive-residence condition; and
2. the still-missing rank-11 and rank-12 upper-deck gates.

It does not include the source antecedent pins or the lower compiler.

The later packet search shows that `Psi` is **not** monotone under useful
residence moves: a packet may remove several residence orbits while exposing
more upper holes.  The correct well-founded coordinate is the lexicographic
pair

```text
Theta = (P/17, (H11+H12)/17).
```

A strict residence move lowers the first coordinate, regardless of its
bounded upper side effect.  An upper-repair move keeps the first coordinate
fixed and lowers the second.  Lexicographic order on `N^2` is therefore the
proof-safe progress order for the alternating programme.

## 2. Authenticated frontier sequence

The exact replayed states reached on 2026-08-02 are:

```text
state                         P/17   H11/17  H12/17   Theta
clean residence-1513           89      88      14     (89,102)
after connected C14            88      88      14     (88,102)
after connected C16            87      87      14     (87,101)
after balanced C18 pair         87      86      13     (87,99)
after serial C18                87      85      13     (87,98)
after joint C18                 86      84      12     (86,96)
after depth-four packet         82      87      10     (82,97)
after C18 repair                82      85      10     (82,95)
after depth-eight packet        78      90      12     (78,102)
after second C18 repair          78      88      12     (78,100)
```

The same non-`C18` catalogue also contained a connected cap-safe `C10` row
with gate vector

```text
(P/17,H11/17,H12/17) = (85,84,12),  Psi=181.
```

The provisional one-circuit row was superseded by a facet-disjoint
four-circuit packet.  Its additive transfer current predicted a four-orbit
residence improvement; literal topology replay retained one physical
component and realized the prediction exactly.  The following C18 step then
repaired two rank-11 orbits without giving back either the residence or
rank-12 gain.  Every row in the displayed table is now backed by a complete
model/factor replay.  The later depth-eight packet removes four further
residence orbits but raises the scalar `Psi` from `177` to `180`; it still
strictly decreases `Theta`, from `(82,95)` to `(78,102)`.  This is the exact
counterexample to treating the sum potential as the driver invariant.

The important structural observation is that the two search phases are
complementary rather than redundant:

- `C10/C14/C16` moves act directly on positive residence;
- serial `C18` rethreads expose upper witnesses and sometimes remove a
  residence orbit at the same time;
- an upper rethread changes the local endpoint geometry enough to expose a
  new shorter residence actuator.

This explains why a one-shot local census could appear stationary while the
alternating campaign continues to descend.

## 3. Exact conditional reduction

Let `G` be the graph whose vertices are connected cap-complete equivariant
factors with complete ranks 13--17, and whose edges are literally replayed
endpoint-retaining circuits or finite facet-disjoint packets preserving
those gates.

### Alternating lex-actuator lemma (missing)

Every vertex `F` in the prepared component with `Theta(F)!=(0,0)` has an
incident safe circuit or finite packet `F -> F'` satisfying

```text
Theta(F') <_lex Theta(F).
```

### Proposition

The alternating lex-actuator lemma implies that the prepared component contains
a depth-three resident factor with complete upper deck.

### Proof

The first coordinate of `Theta` can decrease only finitely many times.  At
each fixed value of the first coordinate, the second coordinate strictly
decreases and is nonnegative, so it too can decrease only finitely many
times.  Hence no infinite lex-decreasing sequence exists.  A terminal state
under the lemma must have `Theta=(0,0)`.  Every edge preserves connectivity,
cap coverage, and ranks 13--17; the definition of `Theta` supplies residence
and ranks 11--12 at the terminal state.  Hence the terminal factor has the
complete upper carrier gates. ∎

The proposition is length-neutral: circuit moves rethread the same factor
and add no word positions.

## 4. What remains after `Theta=(0,0)`

Even a proof of the alternating actuator lemma would settle only the carrier
side.  A `B(17)` word additionally needs:

- a literal depth-three antecedent with legal pins; and
- an integral lower-target compiler on those physical cells.

The finite `k=15` and `k=16` constructions show that this final coupling can
close, but no theorem currently derives it from `Theta=(0,0)`.

## 5. Proof target suggested by the data

The sharp next statement is not that every elementary circuit decreases a
scalar sum.  The catalogues contain many necessary neutral and temporarily
bad moves.  The data instead suggests a two-phase exchange assertion:

> From any prepared nonterminal state, either a non-`C18` safe packet lowers
> the residence coordinate, or a `C18` upper-Pareto rethread keeps residence
> fixed and lowers the upper-defect coordinate.  The accepted move strictly
> decreases `Theta`.

Proving this requires a cut condition on the circuit-transfer hypergraph,
including topology and cap side resources.  Aggregate counts alone are
insufficient.  The fail-closed alternating driver supplies exact finite
instances and immutable transfer signatures for testing that cut condition.
