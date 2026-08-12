# Independent audit: connected 93/369 single-cut braid

## Verdict

**FAIL.**  The displayed connected schedule is inconsistent with short-cell
saturation, and every schedule with those rank-six endpoints has at least two
middle endpoint-forest components.

## Local contradiction

The proposed rank-five witness

\[
J_{94}=[95,96]
\]

is contained in the residual triple `[94,96]`.  If `J_94` has rank five, the
containing triple has rank at least five.  The 369 short rank-six witnesses
and 1023 lower masks saturate all 1392 short cells, so this residual triple
must be a distinct lower value.  It therefore cannot be one of the claimed
rank-at-most-four cells; if its rank were five it would have to equal the
contained five-set, producing a forbidden duplicate.

## Correct residual maxima

After deleting the rank-six triples starting `95,...,463`, the residual short
poset consists of all singletons, all pairs, and the 94 triples starting
`1,...,94`.  Its maximal cells are exactly:

* triples starting `1,...,94` (94 cells);
* pairs starting `96,...,464` (369 cells).

The 462 rank-five masks occupy all but one of these 463 cells.  The proposed
schedule instead uses triples `1,...,93` and pairs `95,...,463`, including a
nonmaximal cell and omitting the wrong boundary cells.

## Component lower bound

The rank-six left endpoints are
`{1,...,93} union {95,...,463}` and their right endpoints are `4,...,465`.
The 463 maximal rank-five cells have left endpoints
`{1,...,94} union {96,...,464}` and right endpoints `3,...,465`.

There are initially 461 possible same-left and 462 possible same-right
incidences.  Omitting the unique cell ending at 3 preserves the right count
but lowers the left count to 460.  Either omission preserving all 461 left
incidences has a right endpoint at least 4 and lowers the right count to 461.
Thus after any omission the 924-vertex endpoint forest has at most 922 edges,
and hence at least two components.

## Scope

The `93+369` split is the extremal maximum-short/minimum-core branch, not a
forced property of every equality word.  This audit refutes the connected
single-path schedule only.  It does not refute `nu(11)=465` or the correct
two-component q369 braid.
