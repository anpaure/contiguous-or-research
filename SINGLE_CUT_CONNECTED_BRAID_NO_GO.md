# The proposed connected 93/369 single-cut braid is impossible

## Status

This note audits the proposed `k=11` schedule

\[
J_i=\begin{cases}[i,i+2],&i\le93,\\[i+1,i+2],&i\ge94,\end{cases}
\qquad
I_i=\begin{cases}[i,i+3],&i\le93,\\[i+1,i+3],&i\ge94.\end{cases}
\]

The numerical identity `93+369=462` is correct, and
`I_i=J_i union J_(i+1)` holds as a physical-interval identity for
`i<462`.  Nevertheless, no universal 465-entry word can realize the
claimed assignment.  The obstruction is a single containment at the width
switch.

All positions and interval endpoints below are one-based.

## 1. The fatal cell

At the switch,

\[
J_{94}=[95,96].
\]

The proposal requires its OR to be the rank-five mask `C_94`.  But the
purportedly free short cell

\[
K=[94,96]
\]

contains `J_94`.  Therefore

\[
U(K)\supseteq U(J_{94})=C_{94},
\]

and so `|U(K)|>=5`.

The proposal simultaneously lists `K` among the 561 free short cells that
must biject onto all masks of ranks one through four.  That is impossible.
This is not repairable by allowing a duplicate value: the 462 selected
rank-five cells, the 369 selected short rank-six cells, and the 561 lower
masks already account for all

\[
462+369+561=1392
\]

physical intervals of lengths at most three.  Distinct target values need
distinct physical witnesses, so every remaining short cell, including `K`,
must carry a different rank-at-most-four value.

Hence the hypotheses of the proposed Single-Cut Braid Theorem are mutually
inconsistent.

## 2. The correct maximal rank-five pool

In this orientation the 369 prescribed short rank-six cells are the triples
with starts `95,...,463`.  Delete them from the containment poset of all
short cells.  The maximal remaining cells are exactly

* the 94 triples with starts `1,...,94`; and
* the 369 pairs with starts `96,...,464`.

There are 463 such cells.  Every selected rank-five witness must occupy one
of them: a rank-five value in a nonmaximal residual cell would have a proper
residual supercell whose distinct OR has rank at most five, which is
impossible.  Thus the 462 rank-five masks occupy all but one of this pool.

The proposed list instead uses triples starting `1,...,93` and pairs starting
`95,...,463`.  In particular it uses the nonmaximal offending pair starting
95 and omits both boundary directions needed by the actual residual poset.

## 3. Why the width switch forces two components

The last long central window and first short central window are

\[
I_{93}=[93,96],\qquad I_{94}=[95,97].
\]

Their intersection is `[95,96]`.  A single alternating middle-level path
would need a rank-five witness in that intersection to connect the two
rank-six values.  The only possible physical cell is precisely `J_94`, but
it is contained in the residual triple `[94,96]`; the preceding argument
rules it out.

Using the correct maximal pool instead gives two physical containment
components:

* the 93 long rank-six quads interlaced with the 94 early rank-five triples;
* the 369 short rank-six triples interlaced with the 369 late rank-five
  pairs.

Deleting one of the 463 possible rank-five cells can split a component but
cannot join these two.  Therefore the exact q369 geometry necessarily has at
least two alternating components at this switch.  This is the structural
reason the current search uses a `369+93` two-path braid and permits the seam
to be a rank-eight upper portal.

There is also a schedule-independent endpoint count proving the same fact.
The rank-six left endpoints are

\[
\{1,\ldots,93\}\mathbin\cup\{95,\ldots,463\},
\]

whereas the 463 maximal rank-five cells have left endpoints

\[
\{1,\ldots,94\}\mathbin\cup\{96,\ldots,464\}.
\]

Before omitting one rank-five cell there are 461 possible same-left edges.
The rank-six right endpoints are `4,...,465`, while the maximal rank-five
right endpoints are `3,...,465`, giving 462 possible same-right edges.  The
only omission that preserves all 462 right edges is the cell ending at 3,
but that cell begins at 1 and reduces the left overlap from 461 to 460.
Conversely, either omission that preserves all 461 left edges has a right
endpoint in `4,...,465` and reduces the right overlap to 461.  Thus the
924-vertex middle endpoint forest has at most

\[
461+461=922
\]

edges.  A spanning linear forest on 924 vertices therefore has at least two
components.  This rules out a connected alternating Hamilton path for every
choice of the one omitted maximal cell, not just for the displayed `J_i`.

## 4. Scope

This no-go result refutes only the connected single-path schedule displayed
above.  It does not refute:

* `nu(11)=465`;
* the q369 mixed-width schedule with its correct two-component rank-five /
  rank-six forest;
* equality cases using fewer than 369 shortened rank-six witnesses.

The split itself is also not forced in an unrestricted equality word.  The
rank count proves **at most** 369 short rank-six witnesses and hence **at
least** 93 full-length witnesses.  Choosing exactly `369+93` is the
maximal-short, minimum-core branch; a word may in principle use more than 93
full-length witnesses.
