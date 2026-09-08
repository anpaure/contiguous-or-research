# Serial coatom moves reduce `B+O(1)` to one final compiler reachability problem

Date: 2026-08-01  
Status: exact safe-search and terminal-compiler reduction.  No bounded final
compiler state is constructed here, so no unconditional additive-constant
theorem is claimed.

## 0. Outcome

The transparent-packet route was previously phrased as a simultaneous
selection problem: choose many disjoint packets while preserving one fixed
unused compiler basis through every phase.  That is a useful sufficient
interface, but it is stronger than existence of one final universal word.

The zero-defect mixed coatom tensor permits a weaker route.  Apply packets
**serially**, recomputing the next packet in the current chronology.  Packet
supports may overlap at different times.  Every intermediate chronology
retains

* the exact middle-owner permutation;
* simple Johnson-path topology;
* factor residence at depth `d`; and
* exactly the same complete interval-union coverage set.

The lower compiler need not exist at intermediate times.  It is solved once,
from scratch, on the terminal chronology.  Thus compiler U5 is no longer a
per-move invariant; it is one terminal potential

\[
                              \lambda_d(T).                       \tag{0.1}
\]

The additive-constant problem on this route becomes a reachability theorem:

> start with one resident upper-complete middle chronology and reach, by
> serial mixed-coatom moves, a chronology with `lambda_d(T)=O(1)`.

No simultaneous quadratic-menu packing, cross-packet token-load estimate,
or common intermediate compiler basis is needed for this weaker target.
One still needs an available planted move at every chosen step and a proof
that a bounded-compiler terminal state is reachable.

## 1. Safe carrier graph

Fix `k`, `r=ceil(k/2)` and `d=d(k)`.  A **safe carrier** is a word

\[
                         T=(T_0,\ldots,T_{W-1})                   \tag{1.1}
\]

with the following properties.

1. It is a permutation of the rank-`r` layer.
2. Consecutive owners form a simple Johnson path.
3. It is factor-resident at depth `d`, including the required boundary
   envelope state.

For a carrier `T`, let `Cov(T)` be the support of all nonempty contiguous
interval unions and let `u(T)` be its number of uncovered upper targets.

A **safe coatom move** replaces one contiguous fragment `X_d` by `Y_d`, or
conversely, from the mixed-screen theorem, under the following literal
embedding conditions.

* The fragment owners occur exactly once in the carrier.
* Its two boundary owners and exterior attachments are those in the planted
  tensor certificate.
* The replacement is made in the same positions and uses the same owner set.
* Its clipped residence boundary state agrees with the exterior state.

Let `Gamma_(k,d)` be the graph whose vertices are safe carriers and whose
edges are safe coatom moves.

## 2. One move is completely safe above the compiler

### Theorem 2.1

If `T,T'` are joined by one safe coatom move, then

\[
 \operatorname{owners}(T)=\operatorname{owners}(T'),\qquad
 operatorname{Cov}(T)=\operatorname{Cov}(T'),\qquad
 u(T)=u(T'),                                                     \tag{2.1}
\]

and `T'` is again a safe carrier.

#### Proof

The mixed-screen tensor phases are simple Johnson paths on the same distinct
owner set and have the same ordered endpoints.  Replacing the embedded
segment therefore preserves the global owner permutation, both exterior
Johnson edges, and simplicity of the global path.

The two phases have equal prefix-OR, suffix-OR and complete internal
interval-OR support decks.  The compressed-deck replacement theorem in both
directions gives

\[
                         \operatorname{Cov}(T)subseteq
                         \operatorname{Cov}(T')subseteq
                         \operatorname{Cov}(T).                   \tag{2.2}
\]

Their clipped positive-run boundary states agree and every new internal run
has length at least `d+1`.  Hence every exterior-crossing run remains legal,
so factor residence is preserved.  The boundary-envelope flags are part of
the planted certificate. \(\square\)

The theorem makes no statement about lower compiler assignments.  Indeed,
the canonical mixed-screen move exchanges two lower support chains across
depths `2,...,d`.

## 3. Overlapping serial composition

### Theorem 3.1 (safe serial search)

Let

\[
                          T^{(0)},T^{(1)},\ldots,T^{(s)}           \tag{3.1}
\]

be any walk in `Gamma_(k,d)`.  The packet supports used at different steps
may overlap.  Then every `T^(i)` is a safe carrier and

\[
                          \operatorname{Cov}(T^{(i)})
                          =\operatorname{Cov}(T^{(0)})            \tag{3.2}
\]

for every `i`.

#### Proof

Apply Theorem 2.1 inductively to the current chronology.  No commutativity or
simultaneous option interpretation is used. \(\square\)

Thus intermediate compiler defects, changed maximal erosions and changed
lower witness addresses are harmless.  They become relevant only at the
chosen terminal vertex of the safe-move graph.

## 4. Exact terminal reduction

For a factor-resident carrier `T`, let `lambda_d(T)` be its exact compiler
deletion number from the common-`Q` compiler theorem: the minimum number of
lower targets which must be omitted before some nonzero depth-`d` antecedent
realizes all remaining lower targets.  The exact terminal bound is

\[
                       \nu(k)\le B(k)+\lambda_d(T)+u(T).          \tag{4.1}
\]

### Theorem 4.1 (component reachability bound)

For every safe starting carrier `T_0`,

\[
 \boxed{
 \nu(k)\le B(k)+u(T_0)+
       \min_{T\in\operatorname{Comp}_{\Gamma_{k,d}}(T_0)}
                    \lambda_d(T).}                               \tag{4.2}
\]

#### Proof

Choose a reachable `T` minimizing `lambda_d`.  Theorem 3.1 gives
`u(T)=u(T_0)` and preserves factor residence.  Apply the exact compiler
deletion upper bound (4.1) to `T`. \(\square\)

### Corollary 4.2 (serial `B+O(1)` criterion)

Suppose that for every sufficiently large `k` there is an upper-complete
safe carrier `T_k` whose safe-move component contains `T'_k` with

\[
                             \lambda_{d(k)}(T'_k)\le C            \tag{4.3}
\]

for one absolute constant `C`.  Then

\[
                             \nu(k)\le B(k)+C.                    \tag{4.4}
\]

If `C=0`, the exact formula follows.

## 5. Relation to the fixed-basis packet theorem

The fixed-unused-basis theorem is still valuable when many packets must be
selected in parallel, or when a recursive proof insists on exporting a
compiler through every cube state.  It requires one common guarded matching
and packet deletion labels.

The serial theorem changes the quantifier order:

```text
parallel route:
  fix compiler -> choose compatible packets -> compiler survives;

serial route:
  choose one safe move -> recompute next move -> ... -> solve compiler once.
```

Accordingly, the current fail-closed packet list `A_tau=emptyset` is not an
obstruction to serial reachability.  It only says the packet cannot yet be
used inside the stronger common-basis composition theorem.

## 6. Exact missing theorem after the reduction

The remaining mathematical target is now one of the following equivalent-
strength constructive statements.

1. **Bounded terminal compiler:** every relevant safe-move component meets
   `{T:lambda_d(T)<=C}` for an absolute `C`.
2. **Regenerative reachability:** one same-parity Pascal lift produces a safe
   carrier and a serial coatom route to a bounded-`lambda` child, with the
   same interface regenerated.
3. **Hole-routing form:** the two nested lower-exposure chains of every move
   generate a routing graph in which all but `O(1)` compiler holes can be
   transported into a terminal repair bank.

The local planting theorem supplies an `O(d)`-support move with exact original
attachments and many labelled realizations.  What is not proved is that the
required successive moves exist in one safe component or that their lower
hole-routing action reaches bounded `lambda`.

This reduction is nevertheless strict: it removes simultaneous packet
disjointness, cross-list conflict bounds and an intermediate U5 invariant
from the weakest sufficient route to `B(k)+O(1)`.
