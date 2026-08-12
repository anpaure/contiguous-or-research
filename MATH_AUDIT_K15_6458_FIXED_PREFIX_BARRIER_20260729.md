# The fixed `k=15` prefix has an exact width-20 completion barrier

Date: 2026-07-29

The verified word

```text
scratch/k15_h19_exact_compiler_union_suffix_6458.word
```

has length `6458`, and its first `6438` letters have third OR derivative
equal to the stored rank-eight carrier.  Direct exhaustive verification gives
the following residual family for that prefix:

```text
685 960 1103 2420 2575 2676 4469 5801 7267 7504 8250
9524 12825 13616 13620 17683 17738 19098 19568 21641 29776
```

The certificate and its previously stated upper bound are valid.  The lower
bound on a suffix can, however, be made both shorter and stronger than the
seam argument in
`MATH_CERTIFICATE_K15_EXPLICIT_6458_UPPER_BOUND_20260729.md`.

## Endpoint-antichain lemma

Let `P` be any fixed prefix, let `R(P)` be the masks not represented by an
interval of `P`, and append a suffix of length `s`.  If `A` is an antichain in
`R(P)`, then

\[
                              s\ge |A|.                 \tag{1}
\]

Indeed, every new witness for a mask in `A` must end in the appended suffix.
Two intervals with the same right endpoint are nested, so their ORs are
comparable by inclusion.  They therefore cannot witness two distinct members
of `A`.  The suffix supplies only `s` possible right endpoints, proving (1).

This proof allows intervals crossing the prefix/suffix seam.  In particular,
it does **not** require the last prefix letter to fail to be a subset of every
residual mask.

For the stored prefix, deleting `13620` from the 21 residual masks leaves an
antichain of size 20.  The only strict inclusions in the full residual family
are

\[
                    9524\subset13620,
             \qquad13616\subset13620.
\]

Thus its residual width is exactly 20.  The stored 20-letter suffix meets
(1), using

\[
                         9524\mathbin\lor13616=13620,
\]

so length 20 is optimal for this fixed prefix even if seam witnesses are
allowed without restriction.

## Exact audit of the last four compiler cells

The script

```text
scratch/audit_k15_tail_compiler_perturbations.py
```

enumerates every nonempty replacement of the last `t<=4` compiler cells
inside their maximal erosion envelopes, retains exactly the replacements
preserving `D^3 A=T`, and recomputes the full residual family and its poset
width.  For `t=4`, the exact output is

```text
scratch/k15_tail4_compiler_perturbation_audit.json
```

with:

```text
valid carrier-preserving tails       2,257,920
distinct residual families                   56
minimum residual size                        21
minimum residual width                       20
```

Consequently no perturbation confined to the final four compiler cells can
admit a suffix of length 19, regardless of seam effects.

The most tempting alternative tail is

```text
546 1601 3139 4128
```

instead of the stored final four letters.  Its last letter is contained in
four residual targets, but the resulting 22-mask residual still has width
20.  The endpoint-antichain lemma rules out a 19-letter completion.  This is
a useful warning: seam eligibility alone is not completion capacity.

## Exact one-incidence audit

The script

```text
scratch/audit_k15_single_bit_compiler_moves.py
```

uses the left-state/right-state factorization of intervals through one source
position to audit every carrier-preserving one-bit addition or deletion.  Its
output

```text
scratch/k15_single_bit_compiler_move_audit.json
```

reports

```text
legal additions                        4,104
legal deletions                       16,173
total legal one-bit moves             20,277
moves reducing residual size               0
moves reducing residual width              0
```

Exactly 21 moves cover a previously residual target, but each loses at least
one previously unique target.  The 14 best moves are one-for-one exchanges;
all retain residual width 20.  Hence a width-improving perturbation needs at
least two source incidences.

## Direct low-weight witness transformations

The additional diagnostic

```text
scratch/audit_k15_low_weight_compiler_perturbations.py
scratch/k15_low_weight10_compiler_perturbation_audit.json
```

enumerates every edit set of weight at most 10 in which all edits directly
turn one old interval into one of the 21 residual targets.  Among 13,167 such
necessary candidate sets, 113 preserve the carrier; none reduces residual
width below 20.

This last statement has deliberately limited scope.  It does not exclude a
move that uses additional incidences outside the target interval to repair a
carrier-breaking deletion.  Such compensation moves are exactly the next
neighbourhood to study; the JSON must not be cited as a global radius-10
UNSAT certificate.

## Precise next target

Let

\[
              \mathcal A=R(P)\setminus\{13620\}.
\]

It is the explicit 20-element antichain above.  Any improvement to a
19-letter suffix must change the prefix so that the new residual width is at
most 19.  Therefore it must newly cover an element of `A`, and any masks lost
as collateral damage must be absorbed into the remaining inclusion chains.

The local data say that isolated bit flips and final-boundary freedom cannot
do this.  The smallest still-live move is a **carrier-preserving relocation**:
delete a coordinate occurrence used by a unique old witness, reinsert the
same coordinate elsewhere in its residence run to keep `D^3 A=T`, and arrange
for the resulting lost mask to be comparable with an existing residual.  This
is a two-sided exchange condition, not a suffix-ordering problem.

