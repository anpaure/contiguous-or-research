# K16 state2 buffered-star braid: two-gap no-go and closure-stabbing floor three

## Exact fibre

Start from either authenticated state2 root used in the frozen one-gap
closure theorem.  Choose an unordered set of three distinct cofacet-star
centers `p`.  Remove, unchanged, the 21 source rows in the three disjoint
radius-three collars

\[
C_p=[p-3,p+3],
\]

and preserve the order of every residual source row.  Call the resulting
core `R`; it has length

\[
M=12873-21=12852.
\]

Arbitrarily permute the 21 removed rows and cut that permutation once, at
one of positions 1 through 20, into two nonempty contiguous blocks `B1,B2`.
Choose two distinct canonical core gaps

\[
0\le g_1<g_2\le M
\]

and form the literal chronology

\[
R[:g_1]\,B_1\,R[g_1:g_2]\,B_2\,R[g_2:].
\]

This definition includes endpoint gaps, adjacent gaps `g2=g1+1`, and gaps
that split an original flat pair.

## Theorem

No chronology in this two-gap fibre has an exact middle carrier.  More
strongly, the three frozen collar-closure witnesses have insertion-gap
stabbing number exactly three.  Thus at least three distinct insertion gaps
are necessary to alter all three local failures; necessity is not a claim
that three gaps suffice.

This is a source-relative theorem for unchanged collar rows and an
order-preserving residual core.  It is not an unrestricted K16 no-go.

## Flat lemma, including splitting and adjacent gaps

Each root has exactly three adjacent source flat pairs.  The audit directly
checks all of the following:

1. Every selected collar is disjoint from every flat pair.
2. The 21 moved values in every collar triple are globally unique.
3. Every retained deletion closure has unequal endpoint values.

Therefore an arbitrary permutation of the moved rows has no internal flat;
neither a block/core join nor an adjacent-gap construction can create one;
and deletion closure itself creates none.  The only possible flats in the
new chronology are the original source flats that were not split by an
insertion.

For each collar triple, let `F` be its three canonical core gaps lying inside
the three source flat pairs.  If `g1` or `g2` belongs to `F`, at least one
source flat is destroyed and no replacement flat exists.  G0 then fails.
If neither gap belongs to `F`, all three flats survive, in their original
order.  Hence every untouched collar closure retains the actual depth phase
used by the frozen one-gap witness.

There are

\[
G=M+1=12853
\]

canonical gaps and

\[
\binom G2=82{,}593{,}378
\]

distinct ordered-by-position gap pairs.  Exactly

\[
\binom G2-\binom{G-3}2=38{,}553
\]

pairs split at least one flat; the remaining `82,554,825` pairs are
nonflat.

## Closure-port stabbing proof

For each selected center `p`, deleting `C_p` creates the directed core
closure

\[
Q_{p-4}\longrightarrow Q_{p+4}.
\]

The frozen actual-phase audit gives a literal reconstruction mismatch at
each of the 18 possible closures.  If its failing row is `r` and its local
depth is `d`, the complete dependency support lies in compressed-core rows

\[
[r-d,r+d].
\]

Let `P_p` be the internal canonical gaps of this support.  An inserted block
at a gap outside `P_p` only translates the support and leaves the exact loss
unchanged.  Thus changing this witness requires an insertion gap in `P_p`.

For selected centers in increasing order, if `m` selected collars lie below
`p`, its closure gap is

\[
g(p)=p-3-7m.
\]

The independent two-gap audit reconstructs all three translated port sets
for each of the `2*C(9,3)=168` collar triples and byte-compares them with the
frozen one-gap catalogue.  In every triple:

- each `P_p` is nonempty;
- the three `P_p` are pairwise disjoint;
- every `P_p` is disjoint from the three flat-splitting gaps.

Consequently

\[
\tau(P_{p_1},P_{p_2},P_{p_3})=3.
\]

Two distinct insertion gaps meet at most two port sets.  For every nonflat
pair, at least one untouched actual-phase reconstruction loss persists.
Together with the flat lemma, this closes every two-gap descriptor.

The audited separation and edge cases are:

| case | minimum compacted closure separation | minimum repair-port separation | max closures touched by arbitrary two gaps | minimum untouched failures | max closures touched by adjacent gaps |
|---:|---:|---:|---:|---:|---:|
| 0 | 59 | 56 | 2 | 1 | 1 |
| 1 | 374 | 371 | 2 | 1 | 1 |

For every triple there are 12,852 adjacent pairs, exactly six of which split
a flat.  Every nonflat adjacent pair touches at most one closure, leaving at
least two failures.  The two endpoint gaps are neutral: the 25,703 pairs
containing at least one endpoint include six flat-splitting pairs, and every
nonflat endpoint pair also touches at most one closure.

For an exact pair-count audit, write `s_i=|P_i|`, `S=sum s_i`, and
`z=G-3-S`.  Pairwise disjointness gives

\[
N_0=\binom z2,
\qquad
N_1=zS+\sum_i\binom{s_i}2,
\qquad
N_2=\sum_{i<j}s_i s_j,
\]

and the checker verifies

\[
N_0+N_1+N_2=\binom{G-3}2
\]

for each of all 168 triples.  Here `N_j` is the number of nonflat gap pairs
that can influence exactly `j` closure witnesses.

## Descriptor size

The arbitrary permutation and nonempty cut have

\[
21!\,20=1{,}021{,}818{,}843{,}434{,}188{,}800{,}000
\]

descriptors.  With the gap pair, this is

\[
84{,}395{,}469{,}983{,}282{,}773{,}681{,}766{,}400{,}000
\]

descriptors per unordered center triple.  There are 84 center triples per
root.  Ordered center labels add only a redundant factor of six once the 21
rows already have arbitrary permutation.

## Scope distinctions

- Lane A donor-value transfers are not in this theorem: they alter row
  values and may invalidate global uniqueness or a frozen closure witness.
- Long-segment 3-opt chronologies are not in this theorem: they change the
  residual core order and therefore its closure contexts.
- Three or more inserted blocks are not classified beyond the necessary
  three-gap stabbing bound.
- No unrestricted K16 lower bound follows from this source-relative class.

## Byte-stable independent audit

- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/audit_k16_state2_two_gap_closure_port_lower3_20260730.py`
  SHA-256 `c62fa80de149dd680e5ed4474f824251b5176b764f8c9ff2175bdf6aedce76cd`.
- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/independent.audit.json`
  SHA-256 `34512210a1a32412b6a4079120ff4dbdae062b6f20fce46317cd4da7c2ec73bf`,
  payload SHA-256 `0ffcf093c5cb884a36b8dadd14eee7065ef024db5b45642c8fbed99226b78582`.
- `scratch/k16_state2_two_gap_closure_port_lower3_20260730/two_gap_triple_catalogue.tsv`
  SHA-256 `a7abb3523197a6b3ffccc502834b2dbd764d38d2631fa9afd1e244af328009cc`.

The audit authenticates the frozen one-gap script/audit/catalogues with
SHA-256 hashes `fa9a0d2b...`, `332a9cb2...`, `b3c24ae4...`, `333e3208...`,
and `017e5f50...`; the frozen payload is `32d196d8...`.  It imports none of
their code and independently rebuilds every two-gap classification.
