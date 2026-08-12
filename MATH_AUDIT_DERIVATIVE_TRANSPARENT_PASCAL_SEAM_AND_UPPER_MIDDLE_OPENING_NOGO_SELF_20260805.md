# Self-audit: derivative-transparent Pascal seam and upper-middle opening no-go

**Date:** 2026-08-05  
**Method:** line-by-line pure-mathematical replay; no computation, search, or
solver  
**Audited theorem:**
`MATH_THEOREM_DERIVATIVE_TRANSPARENT_PASCAL_SEAM_AND_UPPER_MIDDLE_OPENING_NOGO_20260805.md`  
**Audited theorem SHA-256:**
`6f5a1d9e1ec94930c7f3d00fd1e7aa684768fc27d86295f28435101e7acf1fe7`  
**Verdict:** **SELF-GO**, pending independent audit.  The note proves an
exact conditional linear module and a sharp no-go for the stricter seam
state; it does not prove existence of its decorated lower-middle input.

## 1. Height-cycle row

A root of height `h(i)` uses owners at forward distances `0,...,h(i)`.
The cut immediately after a root at forward distance `t` is crossed exactly
when `h(i)>t`.  Hence a cut `c` is safe exactly when

\[
 h(c-1-t)\le t\qquad(0\le t\le d-2),
\]

or equivalently when it is uncovered by all deadline arcs
`{i+1,...,i+h(i)}`.  In particular its predecessor must have height zero.

For rank `q` on `2q-1` points, the root count equals the first-collar layer
size.  Surjectivity and exact bank size force `R_1` to be the full root set,
so every height is positive.  The triangular safe-opening no-go is exact.
It applies only to the strict no-crossing state; it does not prohibit a
transparent crossing seam.

## 2. Derivative identities

With `D_i=Q_i cap Q_(i+1)`, direct expansion gives

\[
 \bigcap_{u=0}^{j-1}D_{i+u}
 =\bigcap_{u=0}^{j}Q_{i+u}.
\]

Thus `I^Q_(i,j)=I^D_(i,j-1)` for every `j>=1`.  This identity is purely
set-theoretic and does not require residence.

At the opened seam, a root `Q_(-1-t)` crossing into

\[
 z+D_{-1},z+D_0,\ldots
\]

started in a `z`-free owner.  Therefore `z` disappears from its total
intersection.  Replacing each `D_v` by `Q_v cap Q_(v+1)` telescopes the
intersection to the original cyclic `Q` window.  A height-`d-1` root needs
at most `d-1` displayed derivative owners.  The claimed transparency and
prefix length are correct.

The asymmetry is real: a root starting in the lifted sector contains `z`,
and crossing into a `z`-free owner deletes it.  The proof does not claim a
reverse transparent seam.

## 3. Upper-rainbow lift

Consecutive lower-middle vertices `D_(i-1),D_i` are adjacent, so their
union `Q_i` has rank `q`.  If the `Q_i` are distinct, equal middle-layer
cardinalities on `2q-1` points make them the complete upper shore.  Both
`Q_i,Q_(i+1)` contain `D_i`; distinctness then forces their intersection to
be exactly `D_i`.  This proves both Johnson adjacency and the derivative
identity.

Conversely, deleting the upper vertices from an alternating middle-levels
Hamilton cycle leaves precisely this lower order and union list.  Thus the
Middle Levels Theorem supplies the upper-rainbow pair but no deeper-bank or
safe-cut decoration.

For residence, the binary incidence rule is

\[
 1_{x\in Q_i}=1_{x\in D_{i-1}\cup D_i}.
\]

Every positive `D` run expands by one position.  Expansions may merge over
a one-zero gap but cannot shorten.  Therefore `d`-residence of `D` implies
`(d+1)`-residence of `Q`.

## 4. Pascal layer ledger

The path

\[
 Q_0,\ldots,Q_{-1},z+D_{-1},z+D_0,\ldots,z+D_{-2}
\]

has `2N` distinct owners.  The first `N` are exactly the `z`-free rank-`q`
sets and the second `N` exactly the `z`-containing rank-`q` sets, so Pascal
gives the complete parent layer.  The unique sector seam is Johnson because
`D_(-1) subset Q_(-1)`.

At depth one, all `Q` roots supply the complete derivative layer `D_i`.  At
depth `j>=2`, the selected `Q` roots are `R^D_(j-1)` and their values are
`I^D_(i,j-1)`, giving every `z`-free target of rank `q-j`.  At depth `j`,
the lifted `D` roots `R^D_j` give `z+I^D_(i,j)`, every `z`-containing target
of that rank.  The sectors are value-disjoint.  This verifies every bank
size, colour, and nesting row.

The terminal path order ends at `D_-2`; the assumed safe cut is exactly
between `D_-2` and `D_-1`.  Hence the last `d-1` lifted roots obey the
required triangular caps.  All `Q` roots are at least `N>=d` positions from
the terminal.  The output inherits the safe terminal opening.

## 5. Linear residence row

Unsplit `Q` runs have length at least `d+1`; unsplit `D` runs have length at
least `d`.  At the sector seam:

* if `x in D_-1`, its `Q` tail joins its `D` initial fragment; when the
  cyclic `D` run is split into lengths `u,v`, the `Q` tail contains the
  terminal `v` positions plus one, so the joined run has length
  `u+v+1>=d+1`;
* if `x notin D_-1` but leaves at the seam, it lies in `D_-2`; the full
  preceding `D` run has length at least `d`, and its upper lift gives a
  `Q` tail at least one longer.

Thus no short internal run is created.  The proof explicitly leaves the
global initial `Q` fragment and terminal `D` fragment clipped and makes no
cyclic residence claim.

## 6. Scope

The theorem removes one exact obstruction: the recursively unavoidable
upper-middle sector does not need a triangularly safe cut if it is followed
by its derivative prefix.  It still assumes a lower-middle cycle on which
upper-rainbow order, supported banks, residence, and one safe cut coexist.
It also leaves arbitrary-width upper OR coverage, residual lower ranks,
literal endpoint closure, and cyclic parent closure open.  Therefore it
does not imply `nu(k)<=B(k)+O(1)` by itself.

