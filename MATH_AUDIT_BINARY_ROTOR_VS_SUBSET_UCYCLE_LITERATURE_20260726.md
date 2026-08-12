# Audit: the binary-rotor component gate contains the linear-uniformity subset-Ucycle problem

Date: 2026-07-26

## 0. Identification

The Boolean circulation in
`MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`
is not merely analogous to a subset universal cycle.  If its support has
one component, its symbol word is an ordinary ((n,m))-Ucycle: every
(m)-subset of ([n]) occurs exactly once as (m) consecutive symbols.
With (C) components it is an exact factor into (C) disjoint subset
Ucycle packings.

Thus the component target

\[
 C=o(W/m)
\]

already asks for a substantial improvement over the known wreath factor
(C=W/n), even before the lower and upper prefix-cover inequalities are
imposed.

## 1. Literature boundary

The classical Chung--Diaconis--Graham conjecture asserts, for fixed (k)
and sufficiently large (n), the existence of a (k)-subset Ucycle under
the necessary divisibility condition.  It remains open in general, and
the published asymptotic packing theorems do not cover

\[
 k=m=(n-1)/2.
\]

Dȩbski--Lonc prove near-Ucycle packings for (k=o(n)), and explicitly
leave the regime (k\sim cn) as an open problem.  Their construction,
following Curtis--Hines--Hurlbert--Moyer, packs the subsets whose circular
gap composition has a unique part greater than one (the ``awesome''
subsets).  At density (k/n\to1/2), a random composition has geometric
part counts near its maximum, so the argument does not imply that the
awesome fraction tends to one.

Consequently no existing Ucycle theorem supplies the rotor rounding used
by the Gaussian-annulus compiler.

Primary sources:

- Curtis--Hines--Hurlbert--Moyer, *Near universal cycles for subsets
  exist*, arXiv:0809.3725.
- Dȩbski--Lonc, *Universal Cycle Packings and Coverings for k-Subsets of
  an n-Set*, Graphs and Combinatorics 32 (2016), 2323--2337.

## 2. A potentially weaker target than a single Ucycle

The compiler does not require one Ucycle.  It only requires

\[
 C=o(W/m),
\]

so average component length (omega(m)) suffices.  This is much weaker
than connectedness of the transition graph.  The form-transition method
decomposes every good circular-gap class into Eulerian base cycles; their
voltage lifts are subset-Ucycle components.  A viable intermediate theorem
would therefore be:

> Choose representatives for all circular-gap classes, including the
> non-good classes, so that the total number of voltage-Euler components is
> (o(W/m)).

This statement has not been found in the literature.  It is the correct
component-only predecessor to the two-sided prefix-cover rotor theorem.

## 3. Exact scope

Even a proof of the preceding component theorem would not finish the
constant-one problem.  The selected components must additionally satisfy
both prefix systems

\[
 \sum_{pi:\{\pi_1,\ldots,\pi_{m-q}\}=S}z_pi\ge1,
 \qquad
 \sum_{pi:\{\pi_1,\ldots,\pi_{m+1+q}\}=U}z_pi\ge1
\]

through the Gaussian cutoff.  The exact uniform fractional rotor
circulation satisfies all these inequalities simultaneously; correlated
integral rounding remains the new content.
