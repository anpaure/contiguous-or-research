# Independent K audit of the split-core literal two-sided collar

Date: 2026-08-01  
Audited theorem SHA-256:
`3d06d46731a54250bef9dad6d144d08b659fd3c640377c64282f79b89df694ad`  
Status: **GO for the local construction, with fixed-width transparency
explicitly excluded and all exterior conditions retained.**

## 1. Exact verdict

For

\[
 h\ge2,\qquad r-h\ge2,\qquad 2\le |X|\le r-h,
 \qquad |\Omega|\ge r+3h,
\]

the displayed `4h+1`-letter word has exactly the asserted `3h+1`
depth-`h` owners.  Those owners are distinct rank-`r` sets forming a
Johnson path; its `3h` lower colours and `3h` upper colours are separately
injective.  Every owner-coordinate run not meeting a local endpoint has
length at least `h+1`.

Deleting the central letter gives exactly the pre-insertion row

\[
 L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},R_0,\ldots,R_{h-1},
\]

where

\[
 U_j=M_j\cup M_{j+1}
 =B\cup\rho[1,j+1]\cup\lambda[j+1,h]
\]

has rank `r+1`.  No counterexample occurs at the sharp endpoint
`h=2`, `|X_L|=|X_R|=1`, including when `C` is empty.

## 2. Full source factorization

The final word consists of blocks of lengths

\[
                         h, h, 1, h, h.
\]

The first `h` length-`h+1` windows successively exchange
`d^-_(t+1)` for `lambda_(t+2)` and are `L_0,...,L_(h-1)`.
The next slide replaces `q^-` by `x_R`; the following `h` slides replace
`lambda_(j+1)` by `rho_(j+1)` and produce `M_0,...,M_h`.
The right seam replaces `x_L` by `q^+`, after which the last `h-1` slides
replace `rho_(t+1)` by `d^+_(t+1)`.  This is the literal `D^h`
factorization.

Johnson adjacency alone would not prove simplicity.  Simplicity follows
because the left block contains `q^-` and omits `x_R`, the middle block
contains `x_L,x_R` and neither seam label, and the right block contains
`q^+` and omits `x_L`; within a block the fresh prefix/suffix index changes
strictly.  This sentence has been added to the theorem.

## 3. Exact temporal and width ledger

Let the insertion cut in the old word be `a`.  The occurrence transport is

\[
 [i,j)\longmapsto
 \begin{cases}
 [i,j),&j\le a,\\
 [i+1,j+1),&i\ge a,\\
 [i,j+1),&i<a<j.
 \end{cases}
\]

The two adjacent old letters have union containing `X`, so every image has
exactly the old OR and the map is injective in every fixed exterior
context.  A crossing occurrence, however, gains one source position.
Thus the theorem proves arbitrary-width **OR-deck** containment, not
same-width-bucket containment.

The smallest literal witness to this distinction is `h=2` and
`B=X={x_L,x_R}`.  The old two-letter crossing interval has value

\[
                    M_1=B\cup\{\lambda_2,\rho_1\}.
\]

Its transported occurrence has length three, and no final length-two
interval has that value.  In general the exact expelled rows are:

* the `h-1` old length-`h` crossing cells, with values
  `M_1,...,M_(h-1)`, which move to length `h+1`;
* the `h` pre-insertion depth-`h` cells `U_0,...,U_(h-1)`, which move from
  source length `h+1` to `h+2`.

Their OR witnesses survive; their old source-length grades do not.  The
first family has rank `r`, and the second rank `r+1`.  This is precisely
why a strictly-lower reference matching loses no edge at the short-band
boundary, while an arbitrary width/address-sensitive guard still requires
literal replay.

## 4. Palette and residence audit

The lower and upper colours split into left-internal, left-seam, central,
right-seam, and right-internal classes.  Internal left/right classes carry
`q^-`/`q^+`; central classes contain the full `B` and no seam label.  A seam
lower colour omits `x_R` or `x_L`, and a seam upper colour contains the
corresponding seam label together with the omitted base coordinate.  Fresh
filler boundaries distinguish indices within every class.  Hence there are
exactly `3h` distinct colours on each shore.

Inside the displayed owner subpath, the exact nonclipped runs are

\[
 \lambda_j:L_{j-1},\ldots,L_{h-1},M_0,\ldots,M_{j-1},
\]

\[
 \rho_j:M_j,\ldots,M_h,R_0,\ldots,R_{j-1},
\]

each of length `h+1`.  The short flags are exactly

\[
 |q^-|=h,\quad |d^-_s|=s,
 \qquad |q^+|=h,\quad |d^+_s|=h-s,
\]

and every one meets the corresponding local endpoint.  At source level
these are not a further run-length choice.  The unique source occurrence of
`d^-_s` is at local position `s-1`, so after literal left concatenation the
length-`h+1` windows containing it have all start positions
`s-1-h,...,s-1`; the missing `h+1-s` starts are supplied automatically by
the exterior.  The same calculation supplies one predecessor start for
`q^-`, and symmetrically supplies the right flags of `d^+_s,q^+`.
Extra exterior occurrences can only merge or extend these runs.  Thus a
literal embedding automatically closes residence length; what remains is
to make the crossing windows valid distinct rank-`r` owners satisfying the
exterior palette and guard rows.  Merely embedding the set-valued owner
path, without its source antecedent, does not give that conclusion.

## 5. New lower cells and exact compiler scope

The final source intervals of length at most `h` outside the retained old
image are exactly the one-letter occurrence `[X]` and

\[
 B\cup\lambda[h-i+1,h],\qquad B\cup\rho[1,i],
 \qquad1\le i<h.
\]

They are `2h-1` distinct occurrences and the two nonsingleton banks are
strict nested rays.  Consequently zero residual local lower deficiency
follows only after the old ray-target occurrences are released, the
reference matching is strictly lower, and one common cap/guard word admits
all transported and new cells.  The source word does not itself establish
those ambient hypotheses.

The split condition `|X|>=2` is sharp for a one-letter monotone insertion
with distinct equal-rank seam moves.  If `X={x}`, a left equal-rank seam
entering `x` forces the old left adjacent letter to omit `x`; a right seam
deleting `x` forces the old right adjacent letter to omit `x`.  Their union
then omits `x`, contradicting zero-damage monotonicity.  This does not rule
out one-sided, nonmonotone, or multi-insertion singleton constructions.

## 6. Independent replay and remaining boundary

The dependency-free script
`scratch/audit_split_core_pivot_literal_two_sided_collar_20260801.py`
(SHA-256
`aef682c21bd2e3daf9d4503c641d41985dc2c232b1de5826cd36e56bdeb6745b`)
checks every old interval occurrence, both q1 palettes, the complete short
cell complement, and all internal runs in 297 symbolic instances with
`2<=h<=12`.  It reports `PASS`.

The audit does not infer a global source occurrence from protected
set-valued owner/incidence edges.  Exterior owner validity and histories,
upper witnesses, common-cap admissibility, and placement of the single
controlled nonowner in a global `W+1` depth row remain open.  Once a literal
source embedding with valid crossing owners exists, residence length itself
is automatic by the preceding convolution calculation.
