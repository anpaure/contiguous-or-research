# Adjacent necklaces: every monomer has an active unique-zero radial lift

**Date:** 2026-08-05  
**Method:** the exact shell translation and the odd-group phase-fibre
matching; no computation  
**Status:** unconditional.  Radial monomer transport does not require the
fixed `AB/CD` square: every inner-shell monomer lifts to a prescribed
unique-zero vertex in the next outer shell, and one orientation always
places that vertex in a nontrivial phase fibre.  That fibre passes exactly
one monomer onward.

## 0. Outcome

Let `q>=3` be odd.  Suppose `y` is any boundary necklace of residual mass
`t`, so `y` has at least one zero coordinate.  The next outer shell has
residual mass

\[
                         s=t+q.                      \tag{0.1}
\]

Choose a zero coordinate `i` of `y`, and let `j=i-1` be its cyclic
predecessor.  Define

\[
                         x=\mathbf1+y-e_i+e_j.       \tag{0.2}
\]

Then:

1. `x` has mass `s` and exactly one zero, at `i`;
2. the actual points in consecutive minimum shells are adjacent by one
   chip transfer;
3. rooted at its unique zero, `x` has an active final pair phase; and
4. deleting `x` from its phase fibre leaves a perfect matching except for
   exactly one opposite-parity unique-zero companion.

Thus one incoming radial monomer produces at most—and in the parity state,
exactly—one outgoing radial monomer.  It never branches.

## 1. Exact radial lift

Work with labelled representatives first.  Let `y_i=0`, and define `x` by
(0.2).  Coordinatewise,

\[
 x_i=0,\qquad x_j=y_j+2,\qquad
 x_h=y_h+1\quad(h\ne i,j).                           \tag{1.1}
\]

### Lemma 1.1

The vector `x` is a weak composition of `t+q`, has a unique zero, and
satisfies

\[
                         \mathbf1+y-x=e_i-e_j.       \tag{1.2}

Consequently, if `y` is in minimum shell `m+1` and `x` is in minimum shell
`m`, their physical representatives differ by the one-unit transfer
`j -> i`.

#### Proof

Equation (1.1) gives nonnegativity and shows that only coordinate `i` is
zero.  Also

\[
 |x|=|y|+q-1+1=t+q.
\]

Equation (1.2) is a rearrangement of (0.2).  Hence

\[
 (m+1)\mathbf1+y
   =m\mathbf1+x+e_i-e_j,
\]

which is exactly one adjacent chip transfer because `i,j` are cyclically
adjacent.  \(\square\)

Changing the labelled root rotates both representatives and therefore
gives a well-defined edge of necklace classes.

## 2. The lifted socket is automatically active

Root `x` at its unique zero `i`.  Its remaining `q-1` positive coordinates
form one even-length run.  Under the standard phase pairing they are paired
from the first coordinate after `i`, so the coordinate immediately before
`i` is the **second** member of the final pair.

That coordinate is `j`, and (1.1) gives

\[
                         x_j=y_j+2\ge2.              \tag{2.1}

An all-quiet terminal pair has form `(2z+1,1)` and hence second member one.
Therefore the final pair of `x` is nonquiet.  Its fixed skeleton/key fibre
has at least one active phase coordinate.

### Theorem 2.1 (active radial lift)

Every inner-shell boundary vertex has a radial neighbour `x` in the next
outer shell which:

1. has a unique zero;
2. belongs to a `t_phase>=1` odd-group hypercube quotient fibre; and
3. is not an all-quiet singleton residue.

The construction is the predecessor-donor orientation (0.2).

#### Proof

Lemma 1.1 proves the radial edge and unique-zero claims.  Equation (2.1)
proves that the final standard pair is active.  \(\square\)

## 3. One-in/one-out phase routing

Let `R_x=Q_h/H` be the active phase fibre containing `x`, where `h>=1`
and `H` is the odd cyclic stabilizer of its fixed skeleton/key data.  The
odd-group Clifford theorem gives a perfect matching `M` of `R_x`.

Let `x'` be the mate of `x` under `M`.  Then

\[
                         M-\{xx'\}                   \tag{3.1}

is a perfect matching of `R_x-{x,x'}`.  Every vertex of this fibre has the
same unique-zero skeleton.  Hence `x'` is another unique-zero outer-shell
vertex.

### Corollary 3.1 (adaptive radial monomer propagation)

Consume an arbitrary inner monomer `y` by the radial edge `yx` from
Theorem 2.1.  Match the rest of `x`'s phase fibre by (3.1).  Exactly one
outer monomer `x'` remains, and `x'` is a legal input to the next radial
lift.

Iterating across any number of minimum shells transports one monomer
without branching or accumulation.  At a chosen shell one may replace the
arbitrary perfect matching by the protected-minor criterion whenever a
specific outgoing phase socket is required.

#### Proof

The incoming edge saturates `x`; (3.1) saturates every other fibre vertex
except `x'`.  Theorem 2.1 applies again to any boundary vertex, including
`x'`.  Induction gives the assertion.  \(\square\)

## 4. What radial transport no longer requires

The propagation theorem does not require:

* a fixed outgoing socket in every shell;
* arbitrary prescribed-edge extendability of `Q_h/H`;
* a separate radial square at every step; or
* a canonical root for a periodic zero skeleton.

The socket is selected adaptively as the matching mate of the incoming
active lift.  Odd cyclic symmetry is already absorbed by the quotient
matching theorem.

## 5. Exact remaining shell theorem

The adaptive lift solves the **transport** part of radial flexibility.  To
obtain a near-perfect matching of the complete adjacent-necklace graph, one
still needs a baseline shell matching with the following property:

> after removing the one active unique-zero socket used by the incoming
> radial edge, every other shell vertex is matched except possibly the one
> active unique-zero companion exported by Section 3.

All `t_phase>=1` fibres satisfy this property automatically.  The remaining
content is the collision-free matching/absorption of the all-quiet
singleton fibres and their next-zero receivers.  The long-run receiver
theorem reduces those sources further to the short-run token core
`[a]` and `[2z+1,1]`.

## 6. Scope

Proved:

1. a radial lift for every inner boundary vertex;
2. an orientation that always lands in an active phase fibre;
3. exact one-in/one-out monomer propagation through arbitrarily many
   shells; and
4. compatibility with odd cyclic stabilizers.

Not proved:

1. baseline matching of every all-quiet zero-core fibre;
2. terminal absorption of the final globally forced parity monomer;
3. PBBS q2-halo/owner placement; or
4. any universal-word upper bound.
