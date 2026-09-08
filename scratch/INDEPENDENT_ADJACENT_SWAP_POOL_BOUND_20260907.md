# The entire target pool of independent adjacent swaps

Date: 2026-09-07. Pure proof; no computation. This is a fixed-word
restriction, not an obstruction to changing the underlying routing.

## 1. Finite statement

Let A be a finite nonzero set-valued word. Choose J pairwise disjoint
adjacent two-letter blocks. Let B range over all words obtained by
independently either retaining or reversing each chosen pair. For a
rank s, let U_s(B) be its distinct rank-s interval unions. Then

    |(union_B U_s(B)) minus U_s(A)| <= 8J.                (1)

The statement holds both for linear intervals and for cyclic intervals
of length at most one full period, with disjoint chosen cyclic pairs.
It bounds the UNION over all 2^J choices, not merely each variant.
Letters may be arbitrary nonempty sets; singleton letters are not needed.

## 2. A two-choice boundary lemma

Consider an ordered sequence of blocks, each with fixed total union.
Blocks are either fixed single letters or unordered pairs {a,b} whose
two orders are permitted. Fix an initial set X and take unions starting
with X and then proceeding through this sequence, ending at any letter.
For any rank s, there are at most two distinct possible unions as all
pair orders and the ending position vary.

Indeed, let C_j be X together with the full unions of all blocks before
block j. The C_j form an inclusion chain independent of the choices.
Within a pair j, the possible proper partial unions are C_j union a
and C_j union b, and their union is C_(j+1). Within a singleton block
there is no ambiguity. If some C_j has rank s, every possible rank-s
partial union before or after that crossing equals this same set:
it is respectively a subset or a superset of C_j. Otherwise there is
at most one block j with |C_j|<s<|C_(j+1)|, and it offers at most two
partial unions. If s is not crossed at all, there are no such unions.
This proves the lemma. Reading the blocks backwards gives the same
assertion for intervals ending at a prescribed final set.

## 3. Charge genuinely new targets to internal cuts

Treat the chosen pairs as blocks and every other letter as a singleton
block. All block unions are fixed. An interval that neither starts
immediately after a chosen pair's internal cut nor ends immediately
before one has endpoints at block boundaries. It therefore corresponds
to an interval in A with the same union.

A genuinely new target consequently has an endpoint at one of these
J internal cuts. Fix such a cut as the left endpoint location. The
first letter of the interval is the pair's second letter, which has
at most two possible values. For each value X, the boundary lemma
gives at most two rank-s unions over all remaining choices of orders
and right endpoints. Thus this cut supplies at most four possible
rank-s targets. The backwards version gives at most four more when
the cut is charged as a right endpoint location. Summing proves (1).
Counting a target at two cuts only enlarges the bound.

For cyclic words, cut the cycle at the fixed endpoint and read one
period. A proper wrapping interval encounters fixed-union blocks in
that linear order; the last partial block, if any, has at most two
choices. The same boundary proof applies. The full-period union is
fixed and already belongs to A. Hence (1) also holds cyclically.

For a fixed bank of source cycles with a total of J disjoint chosen
pairs, the same bound holds for the union of their individual cyclic
target sets, by summing the bounds. No cross-cycle interval is meant.

## 4. Application boundary for coordinate-transposition reservations

In a fixed routed prefix network, a transposition of two consecutive
coordinates at a nonroot cut inside one coarse axis run swaps two
adjacent singleton entries of a source deletion or insertion list.
Its endpoint caps do not change, because their cuts are at coarse-root
residues. Disjoint coordinate pairs give disjoint source pairs.

Therefore, IF the total number of affected source pairs across a
fixed routed bank is J=o(W), every combination of these transpositions
adds only o(W) possible targets at each rank relative to that fixed
source bank. Exponentially many variants do not remove a Theta(W)
rank deficit in this regime.

When a compiler preserves exactly the cyclic source support at the
rank in question (as the guarded pure-band compilers do), the same
conclusion applies to its actual compiled rank support. A compiler
that uses different witnesses needs a separate argument.

For the proposed high-valence reservation family, the advertised
source-pair count is J=2K L t and principal M=2t(2Kh+1), so J/M=O(L/h).
Thus L/h->0 places its FIXED-ROUTING variants in this restriction,
provided that source-pair count and the nonroot-cut hypotheses hold.
Those geometric checks are separate from the abstract theorem above.

The theorem does not bound the union obtained by also varying root
permutations, adding new induced paths, changing caps or block unions,
or changing the word outside the disjoint pairs. In particular it
does not refute the high-valence routing programme. Its purpose is to
distinguish many cheap alternatives from a large new target pool.

Status: coordinator proof and independent root-agent audit passed. In the
cyclic argument, a proper interval beginning at a chosen pair's second
letter cannot reach that same pair's first letter at the end: that would
use the full period, whose union is fixed. No additional wrap factor is
needed.
