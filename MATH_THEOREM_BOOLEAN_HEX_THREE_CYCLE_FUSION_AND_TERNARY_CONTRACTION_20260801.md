# Ternary Boolean hexes merge three directed cycles into one

Date: 2026-08-01  
Status: exact central four-resource and topology theorem.  It strengthens
the known one-cycle/two-path use of the ternary Boolean hex.  It does not
prove that a globally guarded factor contains a regenerating supply of the
required packets.

## 0. Outcome

Use the six ordered Boolean-diamond atoms from
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`.
Their old and new physical projections are

```text
O = {A->B, C->D, E->F},
N = {A->F, C->B, E->D}.
```

The old and new phases use exactly the same lower, upper, tail and head
resources.

In fact the head--upper attachment columns agree occurrencewise in the two
phases; the nontrivial `C_6` lies in the tail--head predecessor projection.
This stronger identity is harmless for cycle fusion but explains why the
packet cannot itself supply the opened rolling reset's attachment return.

If the three old edges lie on three distinct directed cycle components of
an exact four-resource factor, replacing `O` by `N` joins those three
cycles into one directed cycle.  Thus the cycle count falls by exactly two
without opening a component, consuming a path catalyst, changing a palette,
or changing the number of selected atoms.

Consequently, a component-disjoint bank of `s` such packets performs the
exact update

```text
c -> c-2s.
```

If a regenerating packet system can group all but at most two current
cycles into triples at every stage, then repeated ternary contraction leaves
one cycle when the initial cycle count is odd and two cycles when it is
even.  The former is already connected; the latter needs only one bounded
parity/opening sidecar.

## 1. Exact three-cycle fusion

Let `M` be a four-resource matching in the ordered Boolean-diamond host.
Its physical projection has indegree and outdegree at most one, so every
component is a directed path or a directed cycle.

Assume the old phase

\[
 O=\{A\mathbin{\to}B,\ C\mathbin{\to}D,\ E\mathbin{\to}F\}
 \tag{1.1}
\]

is contained in `M` and its three edges lie on three pairwise distinct
directed cycles `C_1,C_2,C_3`.

### Theorem 1.1 (three-cycle fusion)

Put

\[
 M'=(M-O)\cup
 \{A\mathbin{\to}F,\ C\mathbin{\to}B,\ E\mathbin{\to}D\}.
 \tag{1.2}
\]

Then:

1. `M'` is a four-resource matching with exactly the same complete lower,
   upper, tail and head inventories as `M`;
2. the three old cycle components are replaced by one directed cycle;
3. every other physical component is unchanged; and therefore
4. the number of directed cycles decreases by exactly two.

#### Proof

The four-resource assertion is the literal ternary-hex identity.  Delete
the three old edges.  The three cycles become directed paths

\[
 B\leadsto A,\qquad D\leadsto C,\qquad F\leadsto E.
 \tag{1.3}
\]

The new edges concatenate them in the order

\[
 B\leadsto A\to F\leadsto E\to D\leadsto C\to B.
 \tag{1.4}
\]

This is one directed cycle containing all vertices of the three old
cycles.  No new edge meets another component, so all remaining components
are unchanged.  Hence three cycles become one and the cycle count falls by
two.  \(\square\)

The conclusion is orientation-sensitive, but the displayed orientation is
exactly the orientation of the authenticated Boolean-hex atoms.  No
undirected reconnection choice is being assumed.

## 2. Parallel banks

Call two applicable packets **component-disjoint** if their three old cycle
components are disjoint.  In a four-resource matching this already makes
their old typed supports disjoint; each new phase uses exactly its old
typed support.

### Theorem 2.1 (parallel ternary contraction)

Let `I` be a component-disjoint family of `s` applicable three-cycle
packets.  Toggling every packet in `I`, in any order or simultaneously,
produces another exact four-resource matching and changes the physical
cycle count by

\[
                         c'=c-2s.                 \tag{2.1}
\]

#### Proof

The packet supports are disjoint, so their resource-preserving toggles
commute.  Theorem 1.1 applies independently on every three-component
footprint.  \(\square\)

Let `H_M` be the 3-uniform hypergraph whose vertices are the directed cycle
components of `M`, and whose hyperedges are the triples supporting at least
one applicable literal Boolean hex.  A matching of size `s` in `H_M` is
therefore exactly a parallel ternary contraction of size `s`.

### Corollary 2.2 (one-round bound)

If `H_M` has a matching covering all but `r` cycle vertices, then

\[
             c'={c-r\over3}+r={c+2r\over3}.          \tag{2.2}
\]

In particular, `r<=2` gives `c'<=ceil(c/3)+1`.

This is an exact matching reduction.  A fractional matching or an
uncoloured triple of components does not suffice; every chosen hyperedge
must contain one literal old hex phase already present in `M`.

## 3. Regenerative contraction and parity

### Theorem 3.1 (conditional ternary reset)

Suppose a class of exact four-resource factors has the following closure
property: whenever a member has `c>2` directed cycles, its applicable-hex
hypergraph has a matching covering all but at most two cycles, and after the
corresponding toggles the resulting factor remains in the class.

Then after `O(log c)` rounds the factor has at most two directed cycles.
More precisely, if `c_t` is the cycle count after round `t`, then

\[
                    c_{t+1}\le {c_t+4\over3}.        \tag{3.1}
\]

The parity of `c_t` is invariant.  Hence an odd initial count can terminate
at one cycle and an even initial count can terminate at two.

#### Proof

Equation (3.1) is Corollary 2.2.  Iterating its affine contraction reaches a
bounded value in `O(log c)` rounds, and the hypothesis continues to apply
until at most two cycles remain.  Every toggle changes the count by two, so
parity is invariant.  \(\square\)

The parity statement explains the division of labour with the existing
one-cycle/two-path actuator.  Ternary cycle fusion removes all Catalan-scale
cycle debt while preserving parity; one bounded opening/path sidecar can
handle the final even case.  There is no need to maintain two path
components as catalysts throughout the large contraction.

## 4. Relation to the rolling-reset three-return gate

The theorem proves that support three is already sufficient for the
**central topology and four immediate resources**.  This matches the
independent no-go saying that a nondegenerate owner-preserving `2 -> 2`
splice cannot cancel the rolling-reset boundary current.

It does not by itself give the reset's compatible three-return lift.  That
lift additionally requires:

1. the attachment return and both predecessor-parity returns to be
   projections of the same literal turn triples;
2. one common residual exterior for the two reset phases;
3. residence and arbitrary-width upper transparency; and
4. joint compiler safety of the three occurrence hazard sets.

A three-cycle hex whose old phase merely lies somewhere in the factor need
not have those prescribed endpoints.  Thus Theorem 1.1 is the central
support-three packet, while endpoint relocation/private-sink planting is a
separate gate.

More sharply, with owners

\[
 o_1=S+a+c+u,\quad o_2=S+b+c+u,\quad o_3=S+a+b+u,
\]

the complete attachment projections are

\[
 \{(B,o_1),(D,o_2),(F,o_3)\}
\]

in **both** phases.  Hence private corridors may transport the reset's
attachment boundary to the packet, but this complete hex toggle contributes
zero attachment boundary and cannot absorb it.  See
`MATH_THEOREM_PIVOT_CORRIDOR_HEX_RESET_COMPOSITION_GATE_20260801.md`.

## 5. Exact remaining supply theorem

The useful next statement is now narrower than a generic bounded-component
host theorem.

> **Guarded ternary-fusion supply.**  Choose the owner/target factor so that,
> after every bounded protected deletion, the hypergraph of literal,
> occurrence-labelled, guard-transparent Boolean hexes has a matching
> covering all but at most two current cycle components, and the same
> property regenerates after contraction.

Under this statement, Theorem 3.1 removes all but a bounded topological
sidecar while preserving the four central resources exactly.  The current
quadratic Cartesian fan gives many prospective labelings of a fixed target
atom, but no theorem yet forces the required three old edges to lie in
three different current cycles.  The known hex-free-cycle construction
shows that this supply cannot be inferred from near-perfectness or high
girth alone; it must be imposed during factor selection.
