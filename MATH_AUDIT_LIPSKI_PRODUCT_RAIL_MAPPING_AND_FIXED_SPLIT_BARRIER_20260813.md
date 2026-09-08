# Independent source audit of the Lipski product-to-rail mapping

**Date:** 2026-08-13  
**Verdict:** **PASS**.  
**Audited note:**
`MATH_THEOREM_LIPSKI_PRODUCT_RAIL_MAPPING_AND_FIXED_SPLIT_BARRIER_20260813.md`  
**Audited note SHA-256:**
`6e9bc683ca9705c30044bd0e06aed01e7e6eba851b2150ce849eaf24a235c977`  
**Primary source:** W. Lipski, Jr., *On strings containing all subsets as
substrings*, Discrete Mathematics 21 (1978), 253--259, local scan
`/Users/amir.nuriyev/Downloads/1-s2.0-0012365X78901577-main.pdf`.

No correction to the audited note is required.

## 1. Source-level checks

I rendered and read source pages 254--258, including the displayed proof of
Lemma 1.1 and the complete definitions of (A_i,B_i,L_{2k},A_i^*,B_i^*),
and (L_{2k+1}).

Lipski defines a special collection of permutations by the property that
every subset is an initial or final segment.  Lemma 1.1 gives exactly

\[
 r=\frac12{h\choose h/2}
 \quad(h\text{ even}),
\]

and

\[
 r=\frac12\left(1+\frac1h\right)
 {h\choose\lfloor h/2\rfloor}
 \quad(h\text{ odd}).
\]

For even (h), the source proof starts with one complete-chain extension
through every middle set, pairs complementary middle sets, takes the first
half of one permutation and the reverse of the first half of its complement,
and obtains the claimed initial/final coverage.  For odd (h), adjoining the
new label at the two opposite ends doubles the even-((h-1)) collection and
gives the displayed formula.  This is represented accurately in Section 1
of the audited note.

For two disjoint (h)-sets, Lipski's (A_i) cyclically shift the pairing of
the two special collections, so as (i) varies every pair
((\phi_s,\psi_t)) occurs at a block boundary.  The (B_i) replace every
(\psi_t) by its reversal.  The proof of (P_{2h}) is exactly the four-way
prefix/suffix boundary argument stated in the note.  The odd construction
inserts the new singleton between every two blocks in the second copy; it is
a doubling construction for Lipski's singleton-letter model and is not a
new rail factorization.

## 2. Theorem 2.1

Set (q=h-1) and (N=2h=2q+2).  For a target
(Q\in\binom{U\dot\cup V}q), put (P=Q\cap U) and (S=Q\cap V).
Specialness supplies a permutation in which each is a prefix or suffix.
Opposite endpoint types meet across one boundary of (\phi\psi); equal
endpoint types become opposite after reversing (\psi).  Empty pieces are
allowed endpoints, and neither piece can be the whole (h)-set because
(|Q|=h-1).  Thus the crossing interval has exactly (q) distinct labels.

This proves the claimed cover by the literal cyclic orders

\[
 \{\phi_i\psi_j,\phi_i\overline\psi_j\}_{i,j}.
\]

Each is a legal shortest-period pure rail after adjoining a disjoint core.
The total number of owner occurrences for even (h) is

\[
 (2h)(2r^2)=h{h\choose h/2}^2.
\]

Dividing by (\binom{2h}{h-1}) and applying the central-binomial estimate
gives

\[
 \left(\frac2{\sqrt\pi}+o(1)\right)\sqrt h,
\]

as stated.

## 3. Split ledger and fractional obstruction

In a cyclic two-block order on (U\dot\cup V), every mixed split
(1\le a\le q-1) occurs in exactly the two boundary-crossing windows.  At
(a=0,q), a block of length (h=q+1) has exactly two internal windows of
length (q).  These (2(q+1)=2h=N) windows exhaust the deck.  Hence every
two-block rail gives exactly two owners in every split layer.

For a nonnegative weighted catalogue, every split layer therefore has the
same total weighted load (2Z), whereas exact unit owner load would require
the layer totals

\[
 \binom ha\binom h{q-a}.
\]

The (a=0) and (a=1) totals are respectively

\[
 h,\qquad \frac{h^2(h-1)}2,
\]

so no fixed-split fractional factor exists for (h\ge3).  Intersecting the
two allowed load intervals gives the note's robust lower bound

\[
 \varepsilon\ge
 \frac{|\mathcal Q_1|-|\mathcal Q_0|}
      {|\mathcal Q_1|+|\mathcal Q_0|}
 =1-O(h^{-2}).
\]

This obstruction applies to the full Lipski boundary catalogue, not merely
to one chosen order.

## 4. Model comparison and scope

A Lipski word uses singleton letters and represents a set (Y) in exactly
(|Y|) consecutive positions.  It is therefore a special case of a
set-valued contiguous-OR word, so the direction

\[
 s_k\ge\nu(k)
\]

is correct.  Lipski's lower bound cannot be transferred as a lower bound for
(\nu(k)), and his (\Theta(2^k)) upper construction is weaker than the
existing (o(2^k)) set-valued upper bound.

Uniform relabelling of one fixed labeled two-block cycle is uniform on all
labeled cyclic orders.  Consequently symmetrizing the split returns the
ordinary carousel orbit; it does not preserve a new Lipski-specific
transversal.  Before symmetrization the split ledger forbids even fractional
owner balance.

The audited note therefore draws the strongest source-supported conclusion:
Lipski supplies a small explicit order cover and a useful local order bank,
but not owner-disjoint rounding, exact lower flags, prescribed recursive
states, or a new positive rail factor.
