# Balanced subcube vortices realize the critical owner/root leave exactly

## Status

This note gives an unconditional structured replacement for the arbitrary
owner/root leave at the natural pull-ring cover-down scale.  If `a`
coordinates are frozen present and another `a` coordinates are frozen
absent, the surviving rank-`r` owners and rank-`(r-1)` roots induce a
smaller middle-levels graph.  They therefore have an exact one-component
owner/root factor.  Taking `a=(1/4+o(1))log_2 r` makes this balanced slice
have size `Theta(W/sqrt r)`, exactly the critical nibble scale.

The theorem does not force a packet cover-down to leave this slice, and it
does not decorate the smaller middle-levels cycle with the required upper
or lower-chain tickets.  It changes the integral target from absorption of
an arbitrary mesoscopic set to a prescribed-vortex cover-down theorem.

## 1. The balanced slice

Put

\[
 n=2r-1,\qquad
 \mathcal O=\binom{[n]}r,\qquad
 \mathcal Q=\binom{[n]}{r-1},\qquad
 W=|\mathcal O|=|\mathcal Q|.                            \tag{1.1}
\]

Choose disjoint sets `A,B subset [n]` with

\[
                         |A|=|B|=a\le r-2,                 \tag{1.2}
\]

and put

\[
 R=[n]-(A\cup B),\qquad q=r-a,
 \qquad |R|=2q-1.                                        \tag{1.3}
\]

Define the owner and root slices

\[
 \begin{aligned}
 \mathcal O_{A,B}
   &=\{A\cup X:X\in\tbinom{R}{q}\},\\
 \mathcal Q_{A,B}
   &=\{A\cup Y:Y\in\tbinom{R}{q-1}\}.
 \end{aligned}                                           \tag{1.4}
\]

Thus every member contains all of `A` and avoids all of `B`.

### Theorem 1.1 (exact balanced-subcube factor)

The containment graph induced by
`mathcal Q_(A,B) union mathcal O_(A,B)` is canonically the middle-levels
graph on `2q-1` coordinates.  In particular:

1. both shores have cardinality

   \[
                  W_a=\binom{2q-1}q;                     \tag{1.5}
   \]

2. the induced graph is `q`-regular; and
3. it has a Hamilton cycle.  Suppressing the root shore of that cycle
   gives one simple Johnson cycle which uses every owner in
   `mathcal O_(A,B)` and every lower colour in `mathcal Q_(A,B)` exactly
   once.

#### Proof

Deletion of the fixed set `A` is a shore-preserving graph isomorphism from
the induced containment graph to the graph between ranks `q-1` and `q` of
`B_R`, where `|R|=2q-1`.  The two ranks have the common size (1.5), and
every vertex has degree `q`.  The Middle Levels Theorem supplies a
Hamilton cycle.  Reinserting `A` and suppressing the alternating root
vertices proves the last assertion.  \(\square\)

The restriction `q>=2` in (1.2) avoids the degenerate graph `K_2` at
`q=1`, whose sole edge is not a Hamilton cycle under the usual simple-cycle
convention.  Nothing below uses that degenerate slice.

No Hall or absorber hypothesis occurs in Theorem 1.1.  Once the leave has
the form (1.4), central owner/root completion is exact.

## 2. Exact upper-current ledger inside the slice

Every suppressed Johnson edge in Theorem 1.1 has an upper colour in

\[
 \mathcal U_{A,B}
   =\{A\cup Z:Z\in\tbinom{R}{q+1}\}.                    \tag{2.1}
\]

The number of available upper colours is

\[
 U_a=\binom{2q-1}{q+1}
     ={q-1\over q+1}W_a.                                 \tag{2.2}
\]

### Proposition 2.1 (forced slice upper surplus)

Any upper-surjective owner/root factor on the balanced slice has exactly

\[
                         W_a-U_a={2W_a\over q+1}           \tag{2.3}
\]

upper occurrences beyond the first occurrence of every member of
`mathcal U_(A,B)`.

#### Proof

There is one upper occurrence for each of the `W_a` suppressed root
vertices.  If all `U_a` upper colours occur, the total multiplicity beyond
their first occurrences is `W_a-U_a`; substitute (2.2).  \(\square\)

Thus the vortex has exactly the same upper-current conservation law as the
ambient problem, with `r` replaced by `q`.  Theorem 1.1 by itself does not
assert upper surjectivity.

## 3. The critical square-root scale

For `a=o(r)` (and hence `q=r-a` tending to infinity), Stirling's formula
gives, uniformly,

\[
 {W_a\over W}
  =4^{-a}\sqrt{r\over r-a}\,(1+O((r-a)^{-1})).            \tag{3.1}
\]

### Corollary 3.1 (one critical vortex)

Let

\[
                         a=\left\lfloor{\log_2 r\over4}\right\rfloor.
                                                                    \tag{3.2}
\]

Then

\[
                         W_a=\Theta(W/\sqrt r).           \tag{3.3}
\]

#### Proof

Use

\[
 \binom{2s-1}s={4^s\over2\sqrt{\pi s}}(1+O(s^{-1}))      \tag{3.4}
\]

at `s=q` and `s=r`.  This proves (3.1).  Equation (3.2)
gives `4^a=Theta(sqrt r)`, while `sqrt(r/(r-a))=1+o(1)`.
\(\square\)

This is exactly the scale at which the unabsorbed growing-uniformity
packet nibble loses residual degree.

## 4. A disjoint bank of balanced vortices

Fix a `2a`-set `S`.  For every `A in binom(S,a)`, put `B=S-A`.  The
corresponding slices (1.4) are pairwise disjoint on each shore, because a
set in the slice recovers `A` as its intersection with `S`.  The internal
upper-colour families (2.1) are pairwise disjoint for the same reason.

### Corollary 4.1 (explicit vortex bank)

For fixed `S`, there are

\[
                         \binom{2a}a                       \tag{4.1}
\]

pairwise owner/root/inside-upper-disjoint balanced slices, each with an exact
one-component owner/root factor.  Their union occupies the exact fraction

\[
 {\binom{2a}aW_a\over W}
       ={1+o(1)\over\sqrt{\pi a}}                         \tag{4.2}
\]

of both central shores when `a=o(r)` and `a tends to infinity`.

#### Proof

Disjointness was observed above.  Multiply (3.1) by
`binom(2a,a)=4^a/(sqrt(pi a))(1+o(1))`.  \(\square\)

At (3.2), the bank contains `Theta(sqrt(r/log r))` disjoint critical-size
vortices.  Hence a proof may reserve one vortex, a slowly growing bank, or
the entire `Theta(1/sqrt(log r))` central sector without any owner/root
packing theorem inside the reserve.

## 5. Exact controlled-leave reduction

Let `H_ring` be any packet system whose edges use equal numbers of owner
and root resources.  Fix one balanced slice `V_(A,B)` as in (1.4).

### Theorem 5.1 (prescribed-vortex completion criterion)

Suppose a packet matching `M` covers every owner and root outside
`V_(A,B)` and uses no resource of `V_(A,B)`.  Then `M` extends, without
changing any of its packets, to an exact owner/root factor by adding the
Hamilton cycle of Theorem 1.1.

If the packet components and the vortex cycle carry compatible endpoint
states, the resulting components may subsequently be fused; no central
owner/root defect remains.

#### Proof

The two resource sets are disjoint.  Theorem 1.1 covers every resource in
the omitted slice exactly once.  Their union is therefore an exact factor.
The final sentence is only the usual component-gluing implication and is
stated conditionally on its literal endpoint hypotheses.  \(\square\)

The theorem replaces the arbitrary mesoscopic absorber condition by the
following more structured target:

> **Prescribed balanced-vortex cover-down.**  Find a decorated packet
> matching which covers the complement of one slice (1.4), avoids the
> slice, and exports upper, chain-ticket, and endpoint data compatible with
> a decorated middle-levels cycle inside the slice.

At the choice (3.2), this asks the main cover-down to stop at its natural
`W/sqrt r` scale, but removes the owner/root Hall problem at that scale
completely.

## 6. Exact remaining gates

The balanced-vortex theorem proves none of the following.

1. **Controlled cover-down.**  Existing packet matching theorems do not
   force the entire leave into a prescribed codimension-`2a` slice.
2. **Decorated vortex.**  The Middle Levels Theorem supplies central
   topology and the lower palette, but not upper surjectivity, depth-`d`
   residence, the residual named lower chains, or the terminal common cap.
3. **Length-neutral recursion.**  Iterating Theorem 1.1 on the smaller
   coordinate set `R` does not by itself preserve the *ambient* depth
   parameter or provide compatible splice ports.  A construction at the
   intrinsic smaller depth `d(2q-1)` is not automatically a depth-`d(2r-1)`
   factor.  Thus charging even one new physical position at every nested
   vortex is not an additive-constant argument; a regenerative,
   length-preserving decoration theorem is still required.

It does prove that an arbitrary `W/sqrt r` owner/root absorber is stronger
than necessary.  A controlled vortex leave of the same size already has an
exact, single-component central completion and an explicit upper-current
ledger.
