# Sparse Boolean cycles give physical `ell <-> ell` switches

Date: 2026-07-31  
Status: exact all-parameter construction.  For every `ell>=5` and
`n>=2ell-2`, both phases
preserve the two outer palettes, respect every capacity-one owner, and
project to linear forests.  The switch is incidence-balanced and therefore
does not absorb a nonzero leave by itself.

## 1. Construction

Work in the rank-`n` / rank-`n+2` Boolean diamond host on `[2n]`.  Choose

* a background `B` of size `n-2`;
* `ell>=5` active points `a_0,...,a_(ell-1)`; and
* `ell` distinct spectator points `z_0,...,z_(ell-1)`,

all disjoint.  This is possible exactly under the displayed sufficient
range `n>=2ell-2`.  Read active indices modulo `ell` and put

\[
 D_i=B\cup\{a_i,a_{i+1}\},                              \tag{1.1}
\]

\[
 V_i=B\cup\{a_i,a_{i+1},a_{i+2},z_i\}.                 \tag{1.2}
\]

Then `|D_i|=n`, `|V_i|=n+2`, and both `D_i subset V_i` and
`D_(i+1) subset V_i`.  Hence the two families

\[
 M_0=\{(D_i,V_i):i\in\mathbb Z_\ell\},\qquad
 M_1=\{(D_{i+1},V_i):i\in\mathbb Z_\ell\}            \tag{1.3}
\]

are alternating perfect matchings of the same `ell` lower and `ell` upper
outer colours.

Moreover this lower--upper support is an induced `2ell`-cycle.  Indeed,
the active pair `{a_j,a_(j+1)}` of `D_j` is contained in the active triple
`{a_i,a_(i+1),a_(i+2)}` of `V_i` exactly for `j=i` or `j=i+1` when
`ell>=5`; the spectator `z_i` is not active.  Hence the restricted support
has exactly the two phases in (1.3).  In particular these switches provide
irreducible protected rerouters of every fixed length `ell>=5`, not merely
one five-colour example.

## 2. Physical owners

Define rank-`n+1` sets

\[
\begin{aligned}
 H_i&=B\cup\{a_i,a_{i+1},a_{i+2}\},\\
 P_i&=B\cup\{a_i,a_{i+1},z_i\},\\
 Q_i&=B\cup\{a_{i+1},a_{i+2},z_i\}.
\end{aligned}                                           \tag{2.1}
\]

The two intermediate owners of `(D_i,V_i)` are `{H_i,P_i}`, while those
of `(D_(i+1),V_i)` are `{H_i,Q_i}`.  All `3ell` sets in (2.1) are distinct:

* no `H_i` contains a spectator;
* sets carrying different spectators `z_i` are distinct;
* for fixed `i`, `P_i ne Q_i`; and
* the `ell` consecutive active triples `H_i` are distinct because
  `ell>=5`.

Therefore each phase in (1.3) is a matching in the occurrence-labelled
capacity-slot host whenever its `ell` lower colours survive the chosen
puncture.  Every used owner occurs only once in a phase, so even a seam
anchor of capacity one suffices.  The physical projections are

\[
              \phi(M_0)=\{H_iP_i:i\in\mathbb Z_\ell\},
 \qquad       \phi(M_1)=\{H_iQ_i:i\in\mathbb Z_\ell\}.         \tag{2.2}
\]

Each is a matching of `ell` ordinary graph edges, hence a linear forest.

### Theorem 2.1 (sparse cycle switch)

Under the availability condition on the `ell` sets `D_i`, replacing `M_0` by
`M_1`, or conversely,

1. preserves every lower and upper outer colour exactly;
2. preserves matching and all owner-capacity constraints internally;
3. replaces one `ell`-edge physical linear forest by another; and
4. has zero incidence boundary on the two outer palettes.

For fixed `ell`, the construction uses a constant number of resource
vertices independent of `n`.  At `ell=5` it is the first sparse Boolean
switch beyond the abstract two--four-colour locking threshold, unlike the
complete 25-atom affine five-colour refactorization.  Allowing `ell` to grow
also supplies protected global rerouters of increasing size.

#### Proof

Equations (1.1)--(1.3) prove palette preservation and containment.  The
owner calculation and distinctness proof above show host matching and
capacity safety.  Equation (2.2) proves internal physical acyclicity.
`square`

## 3. Exact guards and limitations

This is a **kernel** switch: it replaces `ell` atoms by `ell` atoms and
preserves the covered lower and upper palettes.  It does not increase
matching size and cannot by itself fill an unmatched resource bank.  Its
use is to rethread physical owners, alter the slot leave, split a locked
multi-colour exchange core, or prepare an edge-aligned boundary for a
separate gain-one actuator.

When the phase is embedded beside a retained physical forest `F`, internal
acyclicity is not enough.  Delete the old `ell` edges, contract the components
of the retained forest, and require the `ell` new edges in (2.2) to be
loopless and independent in the quotient graphic matroid.  Protected seam,
root, residence, and downstream compiler-cap constraints are likewise not
automatic.

The `ell` lower colours `D_i` must all remain in the punctured lower palette.
Because this risk set has constant size, the uniform common-basis marginal
theorem can preserve almost all members of any precomputed disjoint bank of
such switches by the additive-risk argument.  It does not make their
quotient links private or prove an aligned-color theorem.

Finally, the switch is sparse: its lower--upper incidence support is the
`2ell`-cycle

\[
 D_0,V_0,D_1,V_1,\ldots,D_(\ell-1),V_(\ell-1),D_0.
\]

It therefore avoids the complete-biclique owner collapse proved in
`MATH_THEOREM_CATALAN_FIVE_COLOUR_BICLIQUE_SLOT_COLLAPSE_20260731.md`.
