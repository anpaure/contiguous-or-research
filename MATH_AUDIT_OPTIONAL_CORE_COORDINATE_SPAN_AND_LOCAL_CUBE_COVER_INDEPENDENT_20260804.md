# Independent audit: optional-core coordinate span and local-cube cover

**Date:** 2026-08-04  
**Method:** pure mathematics; line-by-line independent replay  
**Audited source:**
`MATH_COROLLARY_OPTIONAL_CORE_COORDINATE_SPAN_AND_LOCAL_CUBE_COVER_20260804.md`

## Verdict

The mathematical implications are correct.  There is one presentational
correction in the outcome paragraph: equation (0.6) is a **lower bound**
on the number of covering apertures, not an equality.  It should read

\[
 t\ge 2^{d-C+O(1)}
\]

for fixed `C`.  Nothing in the proof supplies a matching upper cover.

## 1. Fixed-rank interval bound

If every member of a rank-`r` family lies between `X` and `Y`, then
deleting `X` maps the family injectively into one fixed layer of the
`h=|Y-X|` cube.  Thus

\[
 |F|\le {h\choose r-|X|}
       \le {h\choose\lfloor h/2\rfloor}.
\]

No assumption about disjointness of different covering intervals is
used later; the union bound is therefore valid for arbitrary overlaps.

## 2. Strict monotonicity replay

For `h=2a`,

\[
 {2a+1\choose a}/{2a\choose a}={2a+1\over a+1}>1,
\]

and for `h=2a+1`,

\[
 {2a+2\choose a+1}/{2a+1\choose a}=2.
\]

Hence the central binomial coefficient is strictly increasing in the
cube dimension.  A family larger than
`binom(2D-1,D-1)` cannot fit in a Boolean interval of dimension at most
`2D-1`, proving free-coordinate span at least `2D`.

The strict `+1` is necessary: the `(D-1)`-layer of a `(2D-1)`-cube has
exactly `binom(2D-1,D-1)` members and span `2D-1`.

## 3. Cover-number replay

Every interval of free dimension at most `h` contributes at most
`binom(h,floor(h/2))` members of the fixed-rank family.  Consequently

\[
 t\ge
 \left\lceil
 {\binom{2D-1}{D-1}+1\over
  \binom h{\lfloor h/2\rfloor}}
 \right\rceil.
\]

For `h=D+C` with fixed `C`, the central-binomial estimates give

\[
 {\binom{2D-1}{D-1}\over
  \binom{D+C}{\lfloor(D+C)/2\rfloor}}
 =2^{D-C+O(1)}.
\]

Substitution `D=d-3` changes the exponent only by an additive constant,
so the correct conclusion is

\[
 t\ge2^{d-C+O(1)}.
\]

## 4. Scope

The source correctly does not infer that the present protected reservoir
admits such a bounded aperture cover.  The theorem is an exclusion
criterion: a separately proved bounded local cover would eliminate the
optional core.  Coordinate span by itself does not provide that cover.

