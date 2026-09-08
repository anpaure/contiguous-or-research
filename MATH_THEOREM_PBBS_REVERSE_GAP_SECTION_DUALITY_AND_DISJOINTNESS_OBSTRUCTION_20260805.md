# Reverse PBBS gap sections are forward-consecutive, but cannot be disjoint from the forward section

**Date:** 2026-08-05  
**Method:** six-mark signed-walk duality and the exact q1 edge criterion;
no computation or search  
**Status:** unconditional.  Reflection and the unmatched-role swap produce
two sign changes, so the reverse gap potential is the reflected forward
walk, not its negative and not a minimum rule on the old `C` marks.  More decisively,
some q1 colours have one corrected physical occurrence, forcing every
forward and reverse section to share that edge.

## 1. Corrected q1 occurrences are nonempty-gap boundaries

Fix

\[
                         K\in{[2m+1]\choose m-1}.
\]

In its expanded deficit-three word, write `A` on the three
forward-unmatched zeros and `C` on the three reverse-unmatched zeros, with
the fixed shared-coordinate order `C_x,A_x`.  Number the `C` marks
cyclically and let

\[
 z_i=\#\{A\text{ marks strictly between }C_i,C_{i+1}\}.    \tag{1.1}
\]

Let `A_i^last` be the last `A` in this gap when `z_i>0`.

### Lemma 1.1 (exact occurrence list)

The physical corrected occurrences of q1 colour `K` are exactly

\[
       K+C_{i+1}\longrightarrow K+A_i^{last}
       \qquad(z_i>0)                                \tag{1.2}
\]

in the forward `g` orientation, and the reversals of the same edges in the
`g^{-1}` orientation.

#### Proof

The deficit-three one-edge criterion says

\[
 g(K+x)=K+y
 \iff
 y=\operatorname{pv}_{A}(x),
 \quad x=\operatorname{nx}_{C}(y).                 \tag{1.3}
\]

For `x=C_(i+1)`, the first equation chooses the final `A` preceding it.
The second equation holds precisely when that `A` lies after `C_i`, i.e.
when `z_i>0`.  Reversing (1.3) gives the `g^{-1}` statement. `square`

In particular, the number of corrected occurrences of `K` is the number
of nonempty `C`-gaps, not always three.

## 2. Exact reverse-potential transformation

Put a signed walk `H` on the complete expanded six-mark circle: crossing
an `A` raises `H` by one and crossing a `C` lowers it by one.  At the `C`
marks its increments are

\[
             H(C_{i+1})-H(C_i)=z_i-1,             \tag{2.1}
\]

so, up to an additive constant, this restriction is the forward gap
potential `h`.

Let `rho` reverse the physical circle.  Conjugating PBBS by `rho` swaps
forward and reverse unmatched marks.  Under this operation an old `A`
becomes a new `C^-` and an old `C` becomes a new `A^-`.  The reversal also
turns the old local order `C,A` at a shared coordinate into `A,C`; after
the role swap this is again the required new order `C^-,A^-`.

### Theorem 2.1 (reverse potential is the reflected full walk)

If `H^-` is the signed walk used by the gap rule for `g^{-1}`, then

\[
                         H^-(t)=H(\rho t)+\text{constant}.  \tag{2.2}
\]

Consequently a reverse maximum corresponds to a forward maximum of the
**full expanded walk at the reflected old `A` cuts**.  It does not, in
general, correspond either to a maximum or to a minimum of `h` sampled
only at old `C` marks.

#### Proof

Reversal changes the sign of every directed walk increment.  The role swap
changes old `A,+1` into new `C^-,-1` and old `C,-1` into new `A^-,+1`,
which changes the sign a second time.  Thus the two signs cancel and the
transformed cumulative walk is `H circ rho`, up to its arbitrary base
value.  New potential samples occur at new `C^-` marks, which are reflected
old `A` marks. `square`

Thus “take a forward minimum `C`” is not a valid definition of the reverse
section.  Nor is “take a forward maximum `C`”: the sampling shore has
changed from old `C` to old `A`.  The shared-coordinate convention is automatically correct only
after performing both reflection and the role swap.

## 3. Tie rules cannot make the two sections disjoint

### Theorem 3.1 (unique-occurrence obstruction)

Suppose, after cyclic reindexing,

\[
                         (z_0,z_1,z_2)=(3,0,0).     \tag{3.1}
\]

Then q1 colour `K` has exactly one corrected physical edge.  Every forward
q1 section and every reverse q1 section must select that same undirected
edge.  No choice of maximum/minimum tie rules can make the two sections
edge-disjoint for every `K`.

#### Proof

By Lemma 1.1, corrected occurrences are in bijection with nonempty gaps.
Under (3.1) there is exactly one.  A section must select a corrected
occurrence of every q1 colour, so both orientations are forced to use it.
`square`

This obstruction occurs inside the canonical PBBS factor.  On the rooted
all-unit/single-soliton component, the exact gap calculation gives
`(0,0,3)` for `m>=3`, which is (3.1) after rotation.  Hence the failure is
not an artificial six-mark word.

If directed arcs are distinguished, the two sections orient the forced
edge oppositely.  For factor protection and puncturing they still use the
same physical Johnson edge, so this distinction gives no disjoint reserve.

## 4. Reverse whole fans are forward-consecutive

### Theorem 4.1 (orientation is not the obstruction)

A reverse fan

\[
             A,g^{-1}A,\ldots,g^{-q}A              \tag{4.1}
\]

is the same owner path as

\[
             g^{-q}A,g^{-(q-1)}A,\ldots,A          \tag{4.2}
\]

read in the forward `g` orientation.  Its intersection and union are
unchanged by this reversal.  Therefore every reverse-section whole fan is
a literal forward-consecutive path after swapping its two endpoints.

#### Proof

Applying `g` to the `t`-th owner of (4.2) gives the next owner.  Reversal of
a finite list does not change either its set intersection or its set
union. `square`

Thus reverse fans are legitimate protected paths in a forward-oriented
factor.  The obstruction is solely physical edge overlap from Theorem 3.1,
not chronology orientation.

## 5. Consequence for selected-edge puncturing

A second reverse gap section may provide alternate witnesses for colours
with at least two corrected occurrences.  It cannot be a universal
edge-disjoint backup bank: every unique-occurrence q1 colour forces
overlap, beginning on the wholly selected single-soliton component.

Therefore a puncture theorem still needs a local rerouting of the forced
q1 target itself (for example the q1 row rotation of a clean `C6`) and an
all-depth repair of its inverse fan.  Reverse-section tie rules alone do
not remove the puncture gate.
