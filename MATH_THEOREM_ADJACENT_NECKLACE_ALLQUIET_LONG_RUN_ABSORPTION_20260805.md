# Adjacent necklaces: all-quiet long runs inject into the next-zero core

**Date:** 2026-08-05  
**Method:** the odd-group phase-fibre theorem followed by a marked terminal
transfer; no computation  
**Status:** unconditional receiver injection.  In a fresh zero stratum,
after every nonsingleton phase fibre is matched, all remaining sources
having a positive run of length at least three admit pairwise distinct
receivers with one additional zero.  Composing these receivers with
matchings in the next stratum requires a protected-deletion argument.  The
unabsorbed source core has only positive runs of lengths one and two.

## 0. Outcome

Fix an odd cyclic length `q`.  In each fixed zero-skeleton/key fibre, the
odd-group hypercube-quotient theorem perfectly matches every fibre with at
least one active pair phase.  A singleton fibre therefore has the following
rigid form:

* every standard adjacent pair has the form `(2z+1,1)`, `z>=0`;
* the unpaired first coordinate of an odd positive run is arbitrary.

Call such a necklace **all-quiet**.

Every all-quiet necklace with a positive run of length at least three has
an injective adjacent-transfer receiver in the stratum with one additional
zero.  On a selected long run, make the terminal move

\[
             \cdots,2z+1,1,0^g,\cdots
       \longmapsto
             \cdots,2z+2,0^{g+1},\cdots.             \tag{0.1}
\]

The receiver remembers the source uniquely: its unique positive run of
length at least two ending in an even value is the changed run.  Thus the remaining
all-quiet obstruction is confined to cyclic zero skeletons whose positive
runs all have length at most two.

## 1. Why singleton phase fibres are rigid

Fix a positive run and use the standard pair convention:

* in a run of even length, pair positions `(1,2),(3,4),...`;
* in a run of odd length, leave position one unpaired and pair
  `(2,3),(4,5),...`.

For one pair `(a,b)`, put

\[
                         u=a-1,\qquad w=b-1.          \tag{1.1}
\]

Under the quiet/nonquiet key partition, a pair has an active one-bit phase
unless it is the terminal quiet allocation

\[
                         u=2z,\qquad w=0              \tag{1.2}
\]

for some `z>=0`.  Equivalently every standard pair in a singleton fibre is
literally `(2z+1,1)`.  Only the unpaired first coordinate of an odd run and
the nonnegative values of the `z`'s remain unconstrained.

This is the exact `t=0` residue after applying the odd-group quotient
perfect matching to every `t>=1` phase fibre.

## 2. The terminal long-run transfer

Let `X` be all-quiet and let

\[
                         R=(a_1,\ldots,a_ell)         \tag{2.1}
\]

be a positive run of length `ell>=3`, followed cyclically by a zero run of
length `g>=1`.

Under either parity of `ell`, the last two positions of `R` are one standard
quiet pair.  Hence, for some `z>=0`,

\[
                         a_{ell-1}=2z+1,\qquad
                         a_ell=1.                    \tag{2.2}
\]

Move the unit in position `ell` to position `ell-1`.  Locally this is

\[
 (\ldots,a_{ell-2},2z+1,1,0^g,\ldots)
 \longmapsto
 (\ldots,a_{ell-2},2z+2,0^{g+1},\ldots).            \tag{2.3}
\]

It is one legal adjacent chip transfer.  It increases the number of zero
coordinates by exactly one and shortens the selected positive run from
`ell` to `ell-1>=2`.

If several long runs are present, choose one necklace-invariantly—for
example, take the first eligible run in the lexicographically least cyclic
representative, with ties identified under the stabilizer.  The injectivity
argument below is independent of which deterministic orbit of long runs is
chosen.

## 3. Unique marker and injectivity

### Theorem 3.1 (long-run receiver injection)

The map (2.3), with any deterministic necklace-invariant choice of the
long run, is injective on necklace classes.

#### Proof

In an unchanged all-quiet positive run of length at least two, the terminal
coordinate is the second member of a standard quiet pair and is therefore
one.  An unchanged run may end in an even value only when it has length one,
in which case that coordinate is the free unpaired first entry of an odd
run.

The changed run in (2.3) has length `ell-1>=2` and ends in the even value
`2z+2`.  It is
therefore the **unique** positive run of the receiver having both
properties

\[
                 \text{length at least two},\qquad
                 \text{terminal value even}.        \tag{3.1}
\]

Restore its terminal pattern

\[
                         2z+2,0\longmapsto2z+1,1.     \tag{3.2}
\]

This recovers the source necklace and the changed long-run orbit.  Hence a
receiver has at most one preimage.  The construction is injective.
\(\square\)

### Corollary 3.2 (one-stage codimension reduction)

After taking:

1. all perfect matchings inside the `t>=1` phase fibres; and
2. all long-run receiver edges from Theorem 3.1,

every unmatched **source in the current fresh stratum** lies in an
all-quiet singleton fibre and every one of its positive runs has length one
or two.

The phase-fibre edges in the current stratum and the receiver edges are
vertex-disjoint on their source shore, and the receiver endpoints are
pairwise distinct by Theorem 3.1.  A receiver endpoint lies in the next
zero stratum and may otherwise be used by that stratum's internal phase
matching.  Thus global iteration must reserve those endpoints and prove a
deletion-stable or monomer-routing matching in every affected next-stratum
fibre.  Edge-type disjointness alone does not provide that theorem.

## 4. Protected sockets

The construction can reserve any fixed list of receiver vertices by
removing their unique preimages from this stage and exporting those sources
as explicit boundary states.  It does not automatically preserve a
prescribed terminal long-run source itself.  For the radial shell programme
one should either:

1. choose the deterministic long-run orbit away from the named `AB/CD`
   socket bank; or
2. retain the finitely many conflicts in the shell's one-in/one-out socket
   state.

The protected-minor theorem for odd-group quotient phase fibres separately
handles phase-toggle socket edges.  The present injection handles only the
`t=0` singleton fibres, so the two tools do not compete for endpoints.

## 5. Exact remaining core

The unresolved all-quiet sources have a cyclic token description.  Every
positive run is one of

\[
                         [a]\quad(a>=1),
             \qquad     [2z+1,1]\quad(z>=0),        \tag{5.1}
\]

separated by nonempty zero runs.  Thus the only nontrivial pair parameter is
the odd first entry of a two-slot positive run.

The remaining matching theorem is consequently finite-state at the level
of run **types**, although the singleton values and zero-run lengths remain
unbounded:

> Match the cyclic token necklaces built from `[a]`, `[2z+1,1]`, and positive
> zero gaps, while transporting at most one radial monomer and avoiding the
> already used long-run receiver image.

This is strictly smaller than the original arbitrary-zero-pattern core.

## 6. Scope

Proved:

1. exact rigidity of every `t=0` phase fibre;
2. an explicit one-edge injection for every all-quiet source with a run of
   length at least three;
3. source-disjoint composition with the `t>=1` quotient-fibre matchings in
   one fresh stratum; and
4. reduction of that stratum's unabsorbed sources to positive runs of
   lengths at most two.

Not proved:

1. protected iteration after deleting receiver endpoints in the next
   stratum;
2. matching of the short-run token core (5.1);
3. the complete four-socket/radial-flexibility theorem;
4. attachment of the resulting necklace matching to the PBBS physical halo;
5. the all-dimensional universal-word upper bound.
