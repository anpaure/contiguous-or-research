# The parity-tail endpoint trade has a forced positive two-run

**Date:** 2026-08-13  
**Status:** unconditional residence obstruction for the audited first-seam
relative trade.  It also gives an exact necessary condition on any
superposed repair.  It does not rule out a new overlapping multi-seam
trade which changes the displayed boundary facets.

Let `m>=10`, and apply the relative trade of
`MATH_THEOREM_PARITY_TAIL_ENDPOINT_ROTATION_INSTALLS_FIRST_COMPOUND_SEAM_20260813.md`
inside the complete offset-zero first-aligned MSW factor.  Define the
rank-`m-1` set

\[
 K_m=\{0,6,9,10,2m-3\}
       \mathbin{\dot\cup}\{12,14,\ldots,2m-2\}.
\tag{1.1}
\]

The union is disjoint, and `|K_m|=m-1`.

## The exact four-owner witness

### Proposition 1 (forced word `0110`)

In the resulting owner two-factor, the following four owners occur
consecutively, up to reversing the cyclic orientation:

\[
\begin{aligned}
 D_0&=K_m\cup\{3,4\},\\
 D_1&=K_m\cup\{2,3\},\\
 D_2&=K_m\cup\{2,2m-1\},\\
 D_3&=K_m\cup\{1,2m-1\}.
\end{aligned}
\tag{1.2}
\]

The three intervening facet colours are

\[
 D_0\cap D_1=K_m\cup\{3\},\qquad
 D_1\cap D_2=K_m\cup\{2\},\qquad
 D_2\cap D_3=K_m\cup\{2m-1\}.
\tag{1.3}
\]

The first and third edges in `(1.3)` are unchanged MSW row edges.  The
middle edge is exactly edge `4` of the six-edge repair circuit.  Hence the
coordinate-`2` word on `(D_0,D_1,D_2,D_3)` is

\[
                            0,1,1,0.                 \tag{1.4}
\]

#### Proof

The repair hosts for steps `4` and `5` are the canonical MSW rows with
Dyck roots

\[
 111001011001(01)^{m-8}0010,
 \qquad
 110111011001(01)^{m-8}0000.                           \tag{1.5}
\]

Apply the MSW concatenation rule to the common `(01)^(m-8)` tail.  The
two owner windows adjacent to the step-`4` endpoint in the first row are
`D_0,D_1`; those adjacent to the step-`5` endpoint in the second row are
`D_2,D_3`.  The common tail contributes precisely the set in `(1.1)`.
The repair rotation replaces the old step-`4` edge by `D_1D_2`, while it
does not change `D_0D_1` or `D_2D_3`.  This gives `(1.2)-(1.3)`, and
membership of coordinate `2` gives `(1.4)`. \(\square\)

### Corollary 2 (positive-residence failure)

The final occurrence chronology has a positive run of coordinate `2` of
length exactly two.  It is therefore not positive `q`-resident for any
`q>=3`.

This is a statement about the full factor chronology, not merely a word
formed from selected owners: both flanking zeroes are joined to the run by
literal factor edges.

## What another seam copy would have to change

### Corollary 3 (boundary-touch necessity)

Any further relative trade which leaves the coloured edges (that is, the
two endpoints assigned at each of the three facet colours) in `(1.3)`
unchanged retains the positive two-run.  Consequently any successful
resident supertrade must do at least one of the following:

1. replace one of the two explicit boundary edges with colours
   `K_m+3` or `K_m+(2m-1)`; or
2. replace the repair edge of colour `K_m+2` by a different splice.

In particular, owner/lower-disjoint or row-disjoint height copies do not
dilate this run.  Cancellation can occur only through an *overlapping*
multi-terminal trade which deliberately absorbs this repair interface.

More formally, a coordinate conjugate by `gamma` carries `(1.2)` to the
same four-owner word with `K_m` and coordinate `2` replaced by
`gamma(K_m)` and `gamma(2)`.  Therefore any family of conjugate packets
whose changed interfaces are mutually disjoint has one literal positive
two-run in every packet.  Subsequent fusions away from the three displayed
facets do not alter those local words.  Such a family is never positive
`q`-resident for `q>=3`, regardless of how many packets are used.

This complements the separate height-shift obstruction: conjugating the
one-seam theorem does not by itself produce legal copies in one fixed MSW
factor, while copies that remain disjoint from the displayed interface do
not cure residence.  A shared construction must therefore be both a
fixed-host multi-seam incidence trade and a chronology repair at these
interfaces.

## Exact replay

The verifier

* `scratch/verify_endpoint_ladder_forced_two_run_20260813.py`

reconstructs only the explicit `O(m)` touched rows, applies every relative
rotation, and asserts `(1.1)-(1.4)` together with the changed/unchanged
edge labels.  H100 replay passed every `m=10,...,40` and
`m=41,64,65,100,101`.  This replay audits the displayed symbolic identity;
the proof above is the all-`m` argument.
