# Common-intersection packets lift with aggregate immediate-upper support monotonicity

**Date:** 2026-08-13  
**Status:** unconditional local source theorem; simultaneous use requires the
stated cut-separation hypothesis  
**Scope:** owners, the strict-lower source deck, and the owner-edge
immediate-upper source row (source width `d+2`).  No claim is made about
wider upper rows, global port planting, or the terminal cap.  In
particular, this theorem does **not** by itself transport the MSW selected
`q2` turn ledger `E union Q`: that ledger is the union of two consecutive
q1 colours, equivalently a source interval of width `d+3`.

## 1. Setup

Fix owner rank `R` and source depth `d`.  For each packet index
`a in A`, let

\[
 (A_{a,i},B_{a,i})\qquad(i\in I_a)                 \tag{1.1}
\]

be the selected old Johnson edges of an owner-edge head rethread, and
let `pi_a` be the permutation for which the new edges are

\[
 (A_{a,i},B_{a,\pi_a(i)}).                        \tag{1.2}
\]

Assume all owners occurring in the packet bank are distinct.  For every
`a`, suppose that

\[
 H_a\subseteq\bigcap_{i\in I_a}
       (A_{a,i}\cap B_{a,i}),\qquad |H_a|\ge d,    \tag{1.3}
\]

and choose a nonempty ordered partition

\[
 H_a=C_{a,1}\mathbin{\dot\cup}\cdots
             \mathbin{\dot\cup}C_{a,d}.           \tag{1.4}
\]

Put

\[
 X_{a,i}=A_{a,i}\setminus H_a,qquad
 Y_{a,i}=B_{a,i}\setminus H_a.                    \tag{1.5}
\]

Plant the old fragments

\[
 W_{a,i}=(X_{a,i},C_{a,1},\ldots,C_{a,d},Y_{a,i}) \tag{1.6}
\]

as occurrence-labelled subwords.  Cut just before each tagged `Y`
occurrence and transport its complete residual source path according to
`pi_a`.  Require the entire bank to be **cut-separated**: no tagged cut is
strictly inside any other displayed left block

\[
 X_{b,j},C_{b,1},\ldots,C_{b,d}.                   \tag{1.7}
\]

Occurrence-disjoint fragments with disjoint collars are sufficient.

Assume the ambient source is a disjoint union of cyclic source words, each
of length at least `d+1`.  Cutting all tagged occurrences is understood at
the occurrence level, so the resulting residual paths are disjoint even
when several cuts lie on one old cyclic component.

The old and new owner-edge immediate-upper multisets of packet `a` are

\[
 \mathcal U_a^-=
   \{\!\{A_{a,i}\cup B_{a,i}:i\in I_a\}\!\},
 \qquad
 \mathcal U_a^+=
   \{\!\{A_{a,i}\cup B_{a,\pi_a(i)}:i\in I_a\}\!\}.
                                                               \tag{1.8}
\]

Write

\[
 \Delta(T)=\sum_a
  \bigl(m_{\mathcal U_a^+}(T)-m_{\mathcal U_a^-}(T)\bigr).     \tag{1.9}
\]

Let `lambda_0(T)` be the number of width-`d+2` occurrences of `T` in the
old ambient source.

## 2. Packet lift

### Theorem 2.1

Under `(1.1)--(1.7)`, simultaneously transporting all tagged residual
paths has the following exact effects.

1. The owner multiset is unchanged, and the selected old edges `(1.1)`
   are replaced by the new edges `(1.2)`.
2. If the alternating trades preserve the immediate-lower colour
   multiset, then that colour multiset remains exact.
3. Every source interval of value-rank strictly below `R` has a literal
   occurrence-, width-, and value-preserving mate after the rethread, and
   conversely.
4. The width-`d+1` source row (the owner row) is exact.
5. The complete signed change in the width-`d+2` source row is exactly
   `Delta` from `(1.9)`.
6. Every nonempty positive run in the new owner chronology has length at
   least `d+1`.
7. The source-length charge is zero.

Consequently, if

\[
 \lambda_0(T)+\Delta(T)\ge1
       \quad\hbox{for every }T\hbox{ with }\lambda_0(T)\ge1,    \tag{2.1}
\]

then the rethread loses no previously covered first-upper target.  Every
old hole `T` with `Delta(T)>0` is newly covered.  Condition `(2.1)` is an
**aggregate packet condition**: an individual constituent circuit may
temporarily delete the last old occurrence, provided another constituent
restores it in the final packet.

### Proof

The two consecutive length-`d+1` windows of `(1.6)` have values

\[
 H_a\cup X_{a,i}=A_{a,i},\qquad
 H_a\cup Y_{a,i}=B_{a,i}.                         \tag{2.2}
\]

After transporting the tagged `Y` residuals they instead realize
`A_{a,i},B_{a,\pi_a(i)}`.  The `A` roles are fixed and the `B` roles are
permuted, so the owner multiset is exact.  Immediate-lower exactness is the
assumed incidence-colour ledger.

Cut-separation makes all tagged residual paths literal disjoint objects.
Consider a strict-lower interval crossing a new seam.  If it reaches the
left screen `X_{a,i}`, it contains the whole displayed history and hence
contains `A_{a,i}`, of rank `R`, a contradiction.  It therefore consists
of a suffix of the common history followed by a prefix of one transported
tagged residual.  Map it to the old seam preceding that same residual.
The letters, width, and OR-value are identical.  A strict-lower interval
cannot cross a second cut, since it would then contain a complete displayed
left owner block.  Intervals avoiding cuts remain literal.  Reversing the
transport proves bijectivity.

A width-`d+2` interval changes only when it contains a changed owner
transition.  At transition `A_{a,i}B_{a,i}` its old value is their union;
at the replacement transition it is
`A_{a,i}\cup B_{a,\pi_a(i)}`.  Every other transition lies inside one
transported residual path and is literal.  Hence the signed occurrence
change is exactly `(1.9)`, proving items 4 and 5 and implication `(2.1)`.

Finally, each occurrence of a coordinate in a cyclic source letter belongs
to `d+1` consecutive owner windows.  Positive runs are unions of such
length-`d+1` cyclic intervals, so no nonempty positive component is
shorter.  Only existing blocks were permuted, giving zero length charge.
\(\square\)

## 3. Alternating owner-edge `C6/C8` packet corollary

### Corollary 3.1

Let a bank consist of owner-disjoint alternating circuits on the
owner--owner Johnson-edge row of arbitrary even lengths (in particular a
mixture of `C6` and `C8` circuits), represented by the head permutations
in `(1.1)--(1.2)`.  Suppose:

* each circuit's changed owners have a common intersection of size at
  least `d`;
* their source occurrences satisfy simultaneous cut-separation;
* the bank is exact on owner degrees and immediate-lower colours; and
* its computed first-upper load ledger satisfies `(2.1)`.

Then the complete mixed packet has a zero-charge positively
`(d+1)`-resident source lift that preserves every strict-lower occurrence
and every previously supported first-upper target, while creating every
positive-ledger old hole.

The conclusion depends only on the **final** load ledger.  It does not
require the circuits to be individually support-monotone or to be toggled
through intermediate factors that retain upper support.

### Proof

The head permutation preserves the owner bank, and the assumed colour row
is exact.  Apply Theorem 2.1 simultaneously to its final symmetric
difference.  Intermediate switch states are irrelevant to the source word
defined by the final rethread.  \(\square\)

## 4. Exact boundary of the result

This theorem removes two unnecessary restrictions from the exact-palette
common-intersection lift:

* first-upper **multiplicity equality** is replaced by the necessary
  support inequality `(2.1)`; and
* all circuits are assessed as one aggregate packet, so relay debts may be
  closed by later circuits.

It does not prove that a desired packet is present in the canonical MSW
factor, that its ports can be planted simultaneously, or that source rows
of width at least `d+3` survive.  Those remain the global host and
all-width-current gates.

There is a particularly important bookkeeping boundary here.  In the
canonical MSW owner--q1 incidence factor, an alternating `C6` or `C8`
toggles an incidence `OQ` while the other selected mate `E` at `O` stays
fixed.  Its counter-carry current is

\[
                         E\cup Q^-\longmapsto E\cup Q^+,
\]

which is a **turn** current at source width `d+3`, not the edge current
`A_i union B_i` in `(1.8)`.  Applying the present theorem to such a packet
proves positive residence and strict-lower transport once a common-history
realization exists, but proves no support statement for that selected MSW
`q2` row.  A turn-faithful extension must retain `E` (or the corresponding
third owner occurrence) and audit the complete width-`d+3` cut current.
