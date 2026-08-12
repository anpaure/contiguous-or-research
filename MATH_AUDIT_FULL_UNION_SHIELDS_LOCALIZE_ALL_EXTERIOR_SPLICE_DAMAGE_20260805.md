# Audit of full-union exterior shields

**Date:** 2026-08-05  
**Method:** independent interval, rank, and owner/source-scope replay; no
computation or search  
**Audited theorem:**
`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`

## 0. Verdict

**PASS after two corrections.**  The two-sided arc-reassembly theorem and
the sharp owner-level Johnson shield are exact.  The original one-sided
paragraph incorrectly inferred a quadratic address bound from orientation
alone, and the first draft undercounted the generic four-arc interface as
four rather than eight oriented shield occurrences.  Both statements are
corrected in the theorem.

## 1. Arc-reassembly replay

An interval wholly inside one directed arc is copied literally.  An interval
crossing at least two cuts contains the complete intervening arc and hence
contains one of its full-union terminal shields.  Its value is therefore the
full ground set, which every shield still witnesses after reassembly.

An interval crossing exactly one cut and using at least `H` incoming letters
contains the incoming arc's suffix shield.  The analogous statement holds
on the outgoing side.  Thus a non-full casualty has between one and `H-1`
letters on each side, giving fewer than `H^2` addresses per cut.  This proves
Theorem 1.1.

With only an outgoing shield, the outgoing endpoint is localized but the
incoming endpoint is not.  An incoming arc of length `M` can contribute
`Theta(MH)` crossing addresses.  Hence orientation alone cannot imply
`qH^2`; a separate incoming endpoint bound is necessary.

Four cut arcs have four prefixes and four suffixes.  Unless the two shield
blocks on an arc overlap by construction, these are eight physical
occurrences.

## 2. Sharp Johnson shield replay

With `h=n-r`, `|K|=2r-n`, and disjoint `h`-sets `X,Y`, every displayed owner
has size

\[
                         (2r-n)+(n-r)=r.
\]

Each step removes one `x` and adds one `y`.  The complete path union is
`K union X union Y=Omega`, and the path has `n-r+1` owners.  Any Johnson
path on fewer owners has union rank at most `r+(ell-1)<n`, proving sharpness.

The lower colours are the distinct prefix/suffix sets

\[
 K+Y[1,j]+X[j+2,h],
\]

and the upper colours are obtained by adjoining the indexed pair
`x_(j+1),y_(j+1)`.  Both palettes are simple.

## 3. Owner/source scope

The common-history crossover is a reassembly of directed **owner** arcs:
the four old hinge edges are deleted and the unchanged owner continuations
are reconnected.  Theorem 1.1 therefore localizes owner-interval unions,
which are upper targets.

The owner geodesic does not itself provide a depth-`d` source antecedent.
It also does not transport source intervals, strict-lower cells, residence,
or typed common-cap routes.  The theorem now records this boundary.

## 4. Remaining planting gate

In the odd middle-level host, one shortest shield has `m` owners and
`2(m-1)` lifted incidence edges.  Thus even one such prescribed path lies
outside the current small protected-factor theorem's `m-2` edge allowance;
eight shields are farther outside it.  This is a failure of the available
planting theorem, not a proof that no containing factor exists.

