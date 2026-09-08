# Near-universal subset packings are simple resident owner cycles, but almost all of their q1 facets must repeat

**Date:** 2026-08-13  
**Primary input:** M. Dębski and Z. Lonc, *Universal Cycle Packings and
Coverings for k-Subsets of an n-Set*, Graphs and Combinatorics 32 (2016),
2323--2337, DOI `10.1007/s00373-016-1727-6`.  
**Status:** unconditional transfer theorem and exact non-transfer barrier.
The near-Ucycle theorem yields legal generalized closed rails with simple
owner decks and one-sided residence.  It cannot supply the ordered-two-SDR
or immediate-lower-palette row: when (q=o(M)), all but an (o(1)) fraction
of its q1 facet occurrences are necessarily repeats.

## 1. From a Ucycle packing to a generalized rail

Let

\[
 a=(a_0,a_1,\ldots,a_{L-1})
\]

be a cyclic ((M,q))-Ucycle packing.  Thus every cyclic block of (q)
consecutive symbols consists of (q) distinct elements of ([M]), and its
underlying (q)-set occurs at most once.  Let (C) be a disjoint (c)-set
and put (R=c+q).  Define

\[
 O_i=C\cup\{a_i,a_{i+1},\ldots,a_{i+q-1}\},
 \qquad i\in\mathbb Z_L.
\tag{1.1}
\]

### Theorem 1.1 (generalized-rail transfer)

If (L>1), the sequence ((O_i)_{i\in\mathbb Z_L}) is a simple closed
Johnson cycle of rank-(R) owners.  Every nonconstant positive coordinate
run has length at least (q).  The whole source trace is closed, hence has
zero integral state boundary.

#### Proof

The (q)-window sets are distinct, so the owners (1.1) are distinct.  In
passing from (O_i) to (O_{i+1}), the symbol (a_i) leaves and
(a_{i+q}) enters.  The entering symbol is not one of
(a_{i+1},\ldots,a_{i+q-1}), because the new (q)-block has distinct
symbols.  It also cannot equal (a_i), because then the two consecutive
(q)-window sets would agree.  Thus every transition is one Johnson swap.

Two cyclic occurrences of one symbol have separation at least (q), since
otherwise some (q)-block would contain that symbol twice.  One occurrence
belongs to exactly (q) consecutive owner windows.  Occurrences separated
by exactly (q) produce adjacent such intervals and merge; larger gaps keep
them separate.  Hence every positive run has length a positive multiple of
(q).  Finally, cyclicity of (a) makes the source state close exactly.

This proves the theorem. \(\square\)

The construction is a genuine generalization of a pure rail: symbols may
repeat around the long cycle, but not within one owner window.

## 2. Exact immediate shadows

For every edge put

\[
 I_i=O_i\cap O_{i+1},\qquad U_i=O_i\cup O_{i+1}.
\]

The proof above gives the literal identities

\[
 I_i=C\cup\{a_{i+1},\ldots,a_{i+q-1}\},
\tag{2.1}
\]

and

\[
 U_i=C\cup\{a_i,\ldots,a_{i+q}\}.
\tag{2.2}
\]

Thus the lower q1 colours are exactly the cyclic ((q-1))-window sets of
the source word.  The upper q1 colours are its cyclic ((q+1))-window sets.
The packing hypothesis controls neither family for equality or surjectivity.

### Theorem 2.1 (sharp lower-facet density barrier)

If the lower facets (I_i) are all distinct, then

\[
 \boxed{L\le {M\choose q-1}.}
\tag{2.3}
\]

More generally, at least

\[
 \boxed{L-{M\choose q-1}}
\tag{2.4}
\]

lower-facet occurrences repeat a previously occurring named facet.

#### Proof

After removing the common core (C), every (I_i) is one of the
(\binom M{q-1}) possible ((q-1))-subsets.  Equation (2.3) is the
pigeonhole principle.  If (D) distinct facets occur, exactly (L-D)
occurrences remain after retaining one representative of each; since
(D\le\binom M{q-1}), (2.4) follows. \(\square\)

Dębski--Lonc prove that for (q=o(M)) there is a packing of length

\[
 L=(1-o(1)){M\choose q}.
\tag{2.5}
\]

But

\[
 \frac{{M\choose q-1}}{{M\choose q}}
 =\frac{q}{M-q+1}=o(1).
\tag{2.6}
\]

Combining (2.4)--(2.6), a near-universal packing has at least

\[
 (1-o(1)){M\choose q}
\tag{2.7}
\]

repeated lower-facet occurrences.  Equivalently, only an (o(1)) fraction
of its edges can be retained in any globally lower-q1-simple subbank on one
fixed core.

This applies directly in the central rail range (q=\Theta(\sqrt M)).

## 3. Further exact ledgers

### 3.1 Point incidence and fixed-core divisibility

If symbol (x) occurs (n_x) times in the cyclic source, then (x) lies
in exactly

\[
 qn_x
\tag{3.1}
\]

owners.  Thus every noncore point degree is divisible by (q).  Repeated
symbols do not remove the fixed-core divisibility obstruction; overlapping
core allocation remains necessary.

### 3.2 Residence is only one-sided

If two successive occurrences of a symbol are at cyclic distance (g\ge q),
the zero gap between their owner intervals has length (g-q).  This can be
any nonnegative integer.  Consequently Ucycle packing gives the required
positive-run lower bound (q=d+1), but does not give a matching lower bound
on zero gaps.  Any two-sided resident application needs an additional gap
condition or a complementary return construction.

### 3.3 Upper colours and wider windows

Equation (2.2) shows that immediate upper colours are well-defined
rank-((R+1)) sets.  They need not be distinct.  A fixed upper set has at
most (q+1) occurrences: it has only (q+1) constituent (q)-subsets,
and every occurrence uses two consecutive members of that finite family.
This bounded multiplicity is weaker than the required upper palette.

For a window of (w) consecutive owners, the union is

\[
 C\cup\{a_i,a_{i+1},\ldots,a_{i+q+w-2}\}.
\tag{3.2}
\]

The Ucycle condition excludes repetitions only at separation below (q).
For (w\ge3), (3.2) may therefore have repeated symbols, variable rank,
and repeated values.  No arbitrary-width upper witness theorem follows.

### 3.4 Literal lower chains

Every owner occurrence does carry the nested suffix chain

\[
 \{a_{i+q-1}\}\subset
 \{a_{i+q-2},a_{i+q-1}\}\subset\cdots\subset
 \{a_{i+1},\ldots,a_{i+q-1}\}.
\tag{3.3}
\]

Hence the word supplies literal candidate lower marks.  It does not make
their named target loads exact.  At depth one, Theorem 2.1 proves that the
physical facet repetitions are already overwhelming; optional marking
cannot remove a repeated incidence vertex from an ordered two-SDR.

## 4. Exact non-transfer conclusion

The Dębski--Lonc theorem does give three useful physical properties at once:

\[
 \boxed{\text{simple owner cycle}+
        \text{positive }q\text{-residence}+
        \text{closed trace state}.}
\tag{4.1}
\]

Its component length is

\[
 {M\choose q}(1-o(1))=2^{o(M)}
\]

when (q=\Theta(\sqrt M)), so a bounded protected bank would meet a
subexponential-size hypothesis.

However, it fails the immediate physical incidence row by the asymptotically
sharp factor

\[
 \frac{{M\choose q}}{{M\choose q-1}}
 =\frac{M-q+1}{q}=\Theta(\sqrt M).
\tag{4.2}

A near-full fixed-core Ucycle cannot be a component of an ordered two-SDR,
because its repeated rank-((R-1)) intersections would give repeated lower
vertices and degree exceeding two.  Splitting or thinning it to a
lower-simple family discards a (1-o(1)) fraction of its owner edges.

Therefore the near-Ucycle result is not an integral rail-queue rounding
theorem.  The precise possible use is narrower: its cycles may serve as a
one-sided-resident owner reservoir before a global overlapping-core
selection.  To enter the full Shadow--Braid construction, one would still
need a correlated selector which takes only (O(q/M)) of any one core
fibre, gives every lower q1 colour once globally across different cores,
installs the missing upper/all-width tickets, and exports the prescribed
phase/socket and cap state.  Those are exactly the current positive-semigroup
and coinstantiation gates.
