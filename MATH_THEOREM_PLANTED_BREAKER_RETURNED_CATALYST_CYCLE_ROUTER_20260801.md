# A returned catalyst atom routes every chordless occurrence cycle

Date: 2026-08-01  
Status: exact occurrence-level Markov theorem, with a scope-correct interface
to the planted adjacent-order coatom breakers

## 0. Outcome

The first nonnegative obstruction left by the occurrence-labelled Pluecker
theorem is an induced six-cycle.  It is removed by one exterior **matched
atom**, and the exterior atom is returned unchanged.

More generally, let the legal occurrence graph contain a chordless
`2 ell`-cycle on sources `s_1,...,s_ell` and endpoint labels
`t_1,...,t_ell`, together with one exterior pair `s_0t_0`.  Give `s_0` all
cycle labels and give one pivot source `s_ell` the exterior label `t_0`.
The two alternating matchings of the cycle become connected after adding
the catalyst atom `s_0t_0`.  There is a nonnegative route of exactly
`ell+1` quadratic switches, every switch uses `s_0`, and the catalyst
returns to `s_0t_0`.

For `ell=3`, this is the exact one-catalyst route through the induced `C6`
fibre.  Zero catalysts are impossible and four switches are optimal.

This theorem has a sharp boundary.  Quadratic switches, even with a returned
catalyst, preserve all source and endpoint marginals and preserve the used
physical basis.  They can remove an occurrence-level cycle obstruction, but
they cannot augment a deficient compiler matching.  A basis-changing
exterior ear remains necessary for that second task.

The planted adjacent-order coatom theorem supplies the required primitive
quadratic directions in projected reflection-odd pair currents.  To use the
router physically, one must still certify the `ell+1` rectangles as literal
occurrence-labelled packet switches with one common catalyst source and
common-cap address.  This is a finite local actuator condition, not a new
lattice condition.

## 1. The hub support

Fix `ell>=3`, with indices on the endpoint labels read modulo `ell`, so that
`t_(ell+1)=t_1`.  Let

\[
 S=\{s_0,s_1,\ldots,s_\ell\},\qquad
 T=\{t_0,t_1,\ldots,t_\ell\}.
\]

The legal incidence graph `G_ell` has edges

\[
 s_i t_i,\ s_i t_{i+1}\quad(1\le i\le\ell),
 \qquad s_0t_j\quad(0\le j\le\ell),
 \qquad s_\ell t_0.                                  \tag{1.1}
\]

On the nonexterior sources, put

\[
 M^0=\{s_it_i:1\le i\le\ell\},\qquad
 M^1=\{s_it_{i+1}:1\le i\le\ell\}.                \tag{1.2}
\]

Their union is the chordless `2 ell`-cycle.  The catalyst atom is

\[
                         c=s_0t_0.                   \tag{1.3}
\]

The tables `M^0+c` and `M^1+c` are genuine `0/1` matchings, with every
named source and endpoint marginal equal to one.  Introducing both `s_0`
and `t_0` is essential: merely adding `s_0t_1` would violate endpoint
capacity because `M^0` already uses `t_1`.

## 2. Exact returned-catalyst route

### Theorem 2.1 (star-catalyst triangulation)

In the fibre of `G_ell`, there is a nonnegative quadratic path

\[
                         M^0+c\longrightarrow M^1+c             \tag{2.1}
\]

of exactly `ell+1` switches.  First use

\[
             \{s_0,s_\ell\}\times\{t_0,t_\ell\}.              \tag{2.2}
\]

Then, in the order `i=ell-1,ell-2,...,1`, use

\[
                       \{s_0,s_i\}\times\{t_i,t_{i+1}\}.       \tag{2.3}
\]

Finally use

\[
             \{s_0,s_\ell\}\times\{t_0,t_1\}.                 \tag{2.4}
\]

Every intermediate table is a matching and the final catalyst is again
`s_0t_0`.

#### Proof

The first switch replaces

\[
                s_0t_0+s_\ell t_\ell
                   \quad\hbox{by}\quad
                s_0t_\ell+s_\ell t_0.                         \tag{2.5}
\]

Before each subsequent step `i`, the exterior source carries `t_(i+1)`.
The two donor incidences are

\[
                         s_it_i,\qquad s_0t_{i+1}.
\]

Switching (2.3) replaces them by

\[
                         s_it_{i+1},\qquad s_0t_i.               \tag{2.6}
\]

Thus row `s_i` reaches its target state while the exterior endpoint moves
one place backward.  The successive middle steps move it through
`t_ell,t_(ell-1),...,t_2,t_1`.  At that point `s_ell` carries `t_0`.
The last rectangle replaces

\[
                    s_0t_1+s_\ell t_0
                       \quad\hbox{by}\quad
                    s_0t_0+s_\ell t_1.                         \tag{2.7}
\]

Thus the catalyst is returned and every nonexterior row carries
`t_(i+1)`.  All intermediate coefficients are zero or one.  \(\square\)

For the induced six-cycle, the route is explicitly

\[
\begin{aligned}
 &\{s_1t_1,s_2t_2,s_3t_3,s_0t_0\}\\
 \to{}&\{s_1t_1,s_2t_2,s_3t_0,s_0t_3\}\\
 \to{}&\{s_1t_1,s_2t_3,s_3t_0,s_0t_2\}\\
 \to{}&\{s_1t_2,s_2t_3,s_3t_0,s_0t_1\}\\
 \to{}&\{s_1t_2,s_2t_3,s_3t_1,s_0t_0\}.             \tag{2.8}
\end{aligned}
\]

### Theorem 2.2 (sharpness)

For the pair `M^0,M^1`:

1. with no catalyst, neither endpoint admits a quadratic move;
2. one catalyst atom suffices by Theorem 2.1; and
3. every quadratic path from `M^0+c` to `M^1+c` has length at least
   `ell+1`.

Hence the catalyst number is exactly one and the route in Theorem 2.1 is
switch-optimal.

#### Proof

The subgraph induced by `s_1,...,s_ell,t_1,...,t_ell` is a chordless cycle
of length at least six, so it contains no four-cycle.  Thus no quadratic
move is available without the exterior atom.

In `G_ell`, any two nonexterior sources have at most one common neighbour.
Consequently every four-cycle uses `s_0` and exactly one nonexterior source.
One switch changes the assignment of at most one row `s_i`.  All `ell` rows
differ between `M^0` and `M^1`.

If only `ell` switches were used, every nonexterior row would be switched
once.  The exterior source starts at `t_0`; after its first switch, `t_0`
is carried by that nonexterior row.  Returning `t_0` to `s_0` requires
switching that row a second time.  Therefore at least `ell+1` switches are
necessary.  Theorem 2.1 attains the bound.  \(\square\)

## 3. Exact interface to planted adjacent-order breakers

Call a rectangle in (2.2)--(2.4) **physically certified** when its two
diagonal occurrence states are the old/new states of one literal packet
that preserves the owner set, simple topology, immediate palettes, complete
interval-OR support, residence, and the named common-cap address.

### Corollary 3.1 (serial physical lift)

Suppose all `ell+1` rectangles are physically certified and use the same
exterior occurrence `s_0`.  Suppose also that each packet leaves the guards
needed by the next packet unchanged.  Then (2.1) is a literal serial route;
no simultaneous disjointness of catalyst copies is needed because the one
catalyst atom is returned and reused.

#### Proof

Apply the certified packets in the order in Theorem 2.1.  Equations
(2.5)--(2.7) show that every packet's donors are present.  Certification
preserves the ambient guards, and the last packet returns the exterior atom.
\(\square\)

The planted adjacent-order theorem

```text
MATH_THEOREM_PLANTED_COATOM_ADJACENT_ORDER_QUADRATIC_BREAKER_BASIS_20260801.md
```

proves that the safe planted catalogue spans every primitive pair-square
direction, integrally, in each reflection-odd depth coordinate.  It does
**not** by itself prove Corollary 3.1's common occurrence address or the
nonnegative serial order.  The exact remaining local row is therefore:

> construct one trace-guarded exterior matched atom around each induced
> `C6`, and certify the four hub rectangles on one common-cap bank.

For a longer induced cycle, four becomes `ell+1`.  The star router then
supplies the nonnegative serial order automatically.  This is stronger than
projected quadratic span and weaker than a global physical Markov theorem.

## 4. Why this does not augment a deficient compiler

### Theorem 4.1 (cycle/ear boundary)

Every sequence of quadratic switches preserves:

1. every source marginal;
2. every endpoint marginal;
3. the cardinality of the matching; and
4. the set of used physical source cells.

The same is true for a returned-catalyst route after the common catalyst row
and column are deleted from the comparison.  Consequently such a route
cannot lower the Hall deficiency of a fixed physical basis and cannot
implement an alternating augmenting path whose endpoint is a new cell.

#### Proof

A rectangle switch deletes and inserts one incidence at each of the same two
sources and the same two endpoints.  Thus all row and column marginals are
unchanged, as is the used source set.  Composition preserves these
quantities.  In Theorem 2.1 the catalyst atom occurs at both endpoints, so
deleting its common row and column changes none of the conclusions for the
original table.  A matching augmentation changes cardinality or its used
basis and is therefore impossible.  \(\square\)

Thus the occurrence-level `O(1)` programme has two logically distinct
actuators:

* a **returned catalyst atom** for induced-cycle connectivity; and
* an **exterior open ear** for basis change / Hall augmentation.

One exterior atom can play both roles only if the physical macro includes a
certified attach/detach endpoint operation in addition to its quadratic hub
switches.  That unary endpoint operation is not supplied by the quadratic
breaker basis.

## 5. Consequence for the additive-constant route

The signed lattice and reflected-pair obstruction are no longer the active
issue.  At the first nonnegative cycle obstruction, one recyclable atom is
enough.  The remaining proof burden is precisely physical:

1. plant a common-address hub for the four `C6` rectangles;
2. preserve higher-depth companion currents and common-cap tickets through
   the four-step route; and
3. separately supply boundedly many exterior open ears for residual basis
   deficiency.

The theorem supports a bounded-state strategy: one catalyst can be
serialized across arbitrarily many induced cycles, provided each cycle has
a certified hub interface.  It does not claim that one catalyst repairs an
unbounded number of Hall endpoints without an exterior ear bank.

## 6. Independent replay

Run

```text
python3 scratch/audit_planted_breaker_returned_catalyst_cycle_router_20260801.py
```

The dependency-free audit checks `ell=3,...,12`.  It verifies every donor
and inserted incidence, matching marginals, catalyst return, absence of
uncatalysed four-cycles, and the optimal distance `ell+1` by breadth-first
search.

