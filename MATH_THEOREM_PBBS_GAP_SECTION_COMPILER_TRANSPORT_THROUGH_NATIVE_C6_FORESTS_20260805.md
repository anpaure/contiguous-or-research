# The PBBS gap-section compiler transports through native common-history C6 forests

**Date:** 2026-08-05  
**Method:** composition of the exact occurrence bijection with the new
fixed-factor section; no computation or search  
**Status:** unconditional under the stated prospective source-realization
hypothesis.  The lower compiler transports exactly through any serial
native clean-C6 ear forest.  The theorem deliberately does not assert
arbitrary-width upper transport or survival after a linear opening.

## 1. Inputs kept distinct

There are two different levels.

1. The gap-potential theorem gives, inside one uncut canonical PBBS owner
   factor, a selected occurrence cell for every strict-lower target.  At
   entrance depth `p` these cells are named `(X,p+d)`.
2. The common-history clean-C6 theorem gives, after a prospective
   depth-`D` source decoration, a value-, width-, and
   occurrence-preserving bijection on every strict-lower source interval
   cell.

The first statement does not automatically plant the source decoration.
The theorem below assumes that the chosen PBBS occurrence cells have been
realized as distinct strict-lower interval cells in the same decorated
antecedent.  This is the exact host/realization hypothesis; no abstract
owner edge is silently treated as a source cell.

## 2. One native move

Let a clean C6 have common core `K`, direct owners

\[
 P_i=K+a_i+a_{i+1},
 \qquad
 Q_i=K+a_i+c,
\]

and old/new shores

\[
                         P_iQ_i
 \quad\longleftrightarrow\quad
                         P_iQ_{i+1}.               \tag{2.1}
\]

Assume it is planted with the complete common-history fragments

\[
 X_i,\ C_1,\ldots,C_D,\ Y_i
\]

and that the complete right screen together with its right context moves
with the head, exactly as in the common-history theorem.

Let `Phi` be its occurrence bijection on strict-lower cells.

### Theorem 2.1 (root-cell transport)

If `M` is any occurrence-labelled matching from strict-lower targets to
distinct valid cells before the move, then

\[
                         \Phi(M)                   \tag{2.2}
\]

is a matching of the same targets to distinct valid cells after the move.
In particular, the image of the gap-section occurrence SDR has deletion
number zero.

#### Proof

The common-history bijection preserves the cell's interval value, width,
and occurrence identity.  Hence the target assigned to a cell is still
carried by its image.  Injectivity of `Phi` preserves distinctness.  Apply
this simultaneously to every edge of `M`. `square`

The cell map is more precise than support preservation:

* cells wholly in the common history or an untouched context are fixed;
* left-screen cells are fixed role by role;
* right-screen cells, together with their complete right contexts, are
  cyclically permuted among the three roles.

Thus a selected pair `(X,p+d)` need not remain the same PBBS root label
after rethreading, but it has one named transported successor of the same
depth/width and value.  Recomputing the gap-potential section in the new
factor is neither required nor justified.

## 3. Serial forests and double ears

### Theorem 3.1 (serial native-ear forest)

Consider any finite sequence of native clean-C6 moves.  Suppose each move
is literally common-history planted in the factor state in which it is
used, including its complete moved context.  Then the composite map

\[
                         \Phi_t\circ\cdots\circ\Phi_1       \tag{3.1}
\]

transports the initial gap-section compiler to a zero-defect terminal
compiler.

No pairwise disjointness or commutativity of the moves is needed.

#### Proof

Apply Theorem 2.1 inductively.  Every intermediate matching consists of
valid distinct cells, so the next occurrence bijection applies.  A
composition of bijections is a bijection. `square`

### Corollary 3.2 (aligned double ears and loose hyperstars)

An aligned double C6 ear, and hence any loose hyperstar or forest assembled
serially from such ears, preserves the gap-section lower compiler exactly
provided both constituent C6s satisfy the prospective planting hypothesis
at their time of use.

The usual q1/q2 halo-disjointness remains necessary for the PBBS palette
identities.  It is not needed merely for composition of the lower
occurrence bijections.

This separates two notions often conflated in the topology programme:
physical support disjointness certifies simultaneous q1/q2 legality,
whereas serial common-history transport certifies the lower compiler even
when moved contexts overlap at different times.

## 4. Cyclic versus opened cells

The preceding theorem is a cyclic/source-deck theorem.  Open a cyclic
source component at one cut.  Among all interval cells of one fixed width
`w`, exactly `w-1` cyclic cells cross that cut and disappear from the
linear word, provided `w` is smaller than the component length.  Therefore
among widths `1,...,D`, at most

\[
                         \sum_{w=1}^{D}(w-1)
                         ={D(D-1)\over2}            \tag{4.1}
\]

cells disappear per cut.

### Proposition 4.1 (sharp generic opening bound)

If a terminal factor is opened at `s` cuts, the transported compiler loses
at most

\[
                         s{D(D-1)\over2}            \tag{4.2}
\]

of its selected cells.  This is only an upper bound; a protected cut can
lose fewer or none.

The bare-cut count is not the correct final lower-word construction when
there is one terminal source cycle.  The deadline collar restores all of
these cells exactly.

#### Proof

For one cut and width `w`, the crossing cyclic intervals are exactly those
whose first position is one of the preceding `w-1` positions.  Sum over
widths and cuts.  The selected compiler is a subset of all cells, so its
loss is no larger. `square`

### Theorem 4.2 (the budgeted deadline collar preserves the whole lower deck)

Let a terminal cyclic source word be

\[
                         A_0,A_1,\ldots,A_{W-1}.
\]

Form the linear word

\[
 \boxed{
 A_0,A_1,\ldots,A_{W-1},A_0,A_1,\ldots,A_{D-1}.} \tag{4.3}
\]

It has length `W+D`.  Every cyclic source interval of width at most
`D+1` has an occurrence in (4.3) with the same start, width, and OR value.
Consequently all `W` cyclic owner windows of width `D+1`, every lower
derivative cell of widths `1,...,D`, and the transported gap-section
compiler survive in the linear word with zero deletion.

#### Proof

Represent a cyclic interval by its start `i in {0,...,W-1}` and width
`ell<=D+1`.  If `i+ell<=W`, it lies in the first copy.  Otherwise its
wrapped suffix uses at most `D` letters and is present in the appended
prefix.  Thus the linear interval beginning at `i` has exactly the cyclic
letter sequence.  Distinct `(i,ell)` remain distinct linear occurrence
addresses.  Taking `ell=D+1` gives every owner; smaller widths give every
lower cell. `square`

Thus for one terminal source cycle, the lower opening costs exactly the
deadline `D` already present in the target length `W+D`; it creates no
additional lower sidecar.  With several terminal source cycles one would
need one collar per cycle or a prior splice.  The theorem also says nothing
about upper intervals of the **owner chronology** which cross its linear
cut; those may have width much larger than `D+1`.

## 5. The upper bank does not follow

The native common-history move preserves:

* owner, lower q1, upper q1;
* selected q2 for a common-deletion PBBS occurrence;
* every strict-lower occurrence and the complete lower compiler.

It does not preserve the arbitrary-width upper deck in an arbitrary
exterior.  A private-prefix value can be lost first at width `D+3` and
rank `r+2`.  Consequently:

### Proposition 5.1 (exact integration dichotomy)

The fixed gap section plus native common-history ears closes the lower
compiler/topology interaction, but does not show that the **same modified
chronology** retains the complete PBBS upper deck.

An entirely separate, physically untouched complementary PBBS bank would
retain its old all-depth upper support tautologically.  If the alleged
"complementary bank" shares the rethreaded chronology or its exterior
contexts, no such conclusion follows.

The resident q=3 port lift supplies internal cyclic upper-support
monotonicity and residence, but its theorem does not transport the
gap-section lower occurrence SDR.  Therefore replacing every native ear
by a resident port ear merely exchanges the two proved local guarantees;
it does not combine them.

The exact remaining local integration lemma is a **hybrid lift** carrying
both:

1. the common-history lower occurrence bijection; and
2. the resident-port all-width upper witness bank,

with the same owner/q1 resources.  Alternatively, one may use native ears
and prove a protected exterior upper-witness bank globally.

## 6. Consequence

The newly closed common-section gate is stable under the native PBBS
topology mechanism in the strongest useful sense: its selected roots do
not have to remain canonical, because their literal compiler cells
transport exactly and telescope through the entire serial forest.

What remains is not lower Hall.  It is the coupling of that transported
compiler with upper protection, linear opening, zero-gap residence, and
the terminal common cap.
