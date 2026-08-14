# An exact owner-targeted q4 k17 reflection-pair generator exposes millions of missing columns and drives certified descent

**Date:** 2026-08-14
**Status:** exact symbolic generator theorem, complete H100 censuses on eleven
target rows, and exact one-pair-swap scoring certificates.  This is an
owner-only quotient result; lower-ticket simplicity and a completed owner
factor are separate gates.

## 0. Result

Put the ground on `Z_17`, quotient rank-nine owners by translation, and
pair nonfixed owner necklaces under reflection `[A] -> [-A]`.  There are
680 reduced nonfixed rows.  Given any such row `r`, orient each reflected
pair so its base deck contains the chosen representative `A` rather than
`rho(A)`.  The generator in this note enumerates **every** quotient-simple
period-ten q4 reflected pair that is owner-disjoint and contains `r`.  An
optional free-row set `F`
retains exactly the configurations whose ten reduced rows lie in `F`.

The raw anchored parameter space has the exact size

```text
                 C(9,5) * 4! * P(8,6) = 60,963,840.             (0.1)
```

Configurations are deduplicated by their ten-row reduced mask, while a
literal `(core,cyclic order)` witness is retained.  Against the frozen
27,008-pair sample-zero pool, each of the three hardest E86 holes has

```text
15,486,081 valid reflected-pair masks,
       327 masks already in the frozen pool,
15,485,754 genuinely new masks.                                (0.2)
```

Thus the frozen pool sampled only about two parts in one hundred thousand
of the available target-local masks.

The generator also has a bounded streaming scorer.  For every new mask it
computes the exact best exchange against all 54 selected pair
configurations of an incumbent, retains a deterministic top `K`, and keeps
a per-hole coverage reservoir.  It found and independently replayed the
following descent steps:

```text
E86 --target row595--> E80   (best delta -6, hole change -3),
E78 --target row516--> E76   (best delta -2, hole change -1),
E76 --target row395--> E74   (best delta -2, hole change -1),
E74 --target row399--> E72   (best delta -2, hole change -1),
E70 --target row459--> E68   (best delta -2, hole change -1),
E66 --target row605--> E64   (best delta -2, hole change -1).   (0.3)
```

Every displayed insertion was incorporated into an augmented instance.
Exact pair/self descent supplied additional moves E72-to-E70 and E68-to-E66.
At E64 the complete row348 and row664 oracles had no negative one-swap, but
the appended neutral row348 bank enabled a zero pivot followed by a self
ejection, reaching the certified E62 state.  Each pre-step state in this
chain was independently certified one-exchange locally optimal over its
then-current pair pool and all 3,749 group-preserving self alternatives.

## 1. Quotient and reduced-row conventions

Let `A` be a rank-nine subset.  Translation acts freely on rank-nine
subsets of `Z_17`: a set invariant under a nonzero translation would be a
union of orbits of the prime-order translation, hence empty or all of
`Z_17`.  Every owner necklace therefore has a unique canonical translate,
and there are

```text
                         C(17,9)/17 = 1,430                      (1.1)
```

owner necklaces.

Reflection acts on canonical necklaces by `[A] -> [-A]`.  Exactly 70 are
fixed and the remaining 1,360 form 680 pairs.  Order the representatives
`v` satisfying `v < reflection(v)` by owner-orbit index.  Reduced row `r`
is the `r`-th such representative, and both `v` and `reflection(v)` map to
`r`.  This is exactly the row convention of the frozen reflection-master
instance.

## 2. Complete anchored parameterization

Fix a nonfixed reduced row and let `A` be the canonical rank-nine
representative of its chosen owner necklace.  An anchored raw rail is
specified by:

1. a five-core `C subset A`, giving `C(9,5)` choices;
2. an ordering `(s0,s1,s2,s3)` of `A-C`, giving `4!` choices; and
3. an ordered six-tuple `(s4,...,s9)` of distinct labels in `Z_17-A`,
   giving `P(8,6)` choices.

Set

```text
O_i = C union {s_i,s_(i+1),s_(i+2),s_(i+3)},       i mod 10.    (2.1)
```

Then `O_0=A`, the core and support are disjoint, and the support labels are
distinct.  The two labels of `Z_17-A` absent from the six-tuple are unused.
The implementation enumerates permutations of all eight outside labels
and requires the last two to be increasing.  Every ordered six-tuple has
exactly one such completion, proving the `P(8,6)` factor without duplicate
raw parameters.

### Theorem 2.1 (completeness)

Every quotient-simple period-ten q4 rail containing the chosen owner
necklace occurs in the anchored parameterization `(2.1)`.

#### Proof

In a quotient-simple rail the target necklace has a unique owner
occurrence.  Translate that physical occurrence to the canonical
representative `A` and rotate the ten cyclic starts so it is `O_0`.
Translation is unique because the rank-nine action is free.  The rail core
is then a unique five-subset of `A`; the four support labels in the target
window are exactly `A-C` in their cyclic order; and the remaining six
ordered support labels are distinct elements of `Z_17-A`.  These are
precisely the parameters above.  Conversely every raw parameter constructs
`O_0=A`; the subsequent filters test all remaining requirements literally.
\(\square\)

If an unordered reflected pair is initially presented with `rho(A)` in its
base deck, reflect the whole rail first.  Its mate then contains `A`, so
Theorem 2.1 applies.  Thus the anchored enumeration is complete for
unordered ten-row reflection-pair masks, not only for one preselected
orientation.

## 3. Exact reflection-pair filter and deduplication

For every raw rail, canonically translate the ten owners and reject it
unless their 1,430-row orbit IDs are distinct.  Let `E` be this owner deck
and `rho(E)` its literal reflected deck.  Retain exactly when

```text
                             E intersect rho(E) = empty.         (3.1)
```

Condition `(3.1)` simultaneously excludes fixed owner rows and collisions
between the two columns.  Each member of `E` then lies in a different
reflection pair, so the ten reduced row IDs are distinct.  They contain the
target row.  If an allowed set `F` is supplied, the implementation retains
the mask exactly when all ten row IDs lie in `F`.

The catalogue key is the sorted ten-row mask.  The stored witness is the
lexicographically least `(core,order,owner-ID sequence)` seen for that key.
The literal reflected witness is obtained by negating every core and order
label; reflected owner IDs are recorded explicitly in scored artifacts.
An optional TSV mode persists all masks and witnesses.  It was deliberately
not used for the 15--17 million-mask unfiltered runs.

As a strong completeness check, every frozen pair mask containing the
target row must reappear.  The code asserts equality, not mere inclusion,
between the regenerated frozen overlap and the independently parsed frozen
target degree.

## 4. Exact finite censuses

For the E86 incumbent, rank its 43 holes by:

1. ascending number of inclusion-minimal blocker menus;
2. descending minimum blocker cardinality;
3. ascending frozen pair degree; and
4. row ID.

The first three are

```text
row595: 330 menus, minimum blocker size3, pair degree327,
row484: 340 menus, minimum blocker size3, pair degree327,
row631: 340 menus, minimum blocker size2, pair degree327.        (4.1)
```

They lie in one multiplier orbit, but all three were enumerated
independently.  Their exact counts agree:

```text
raw anchored                                      60,963,840
quotient-simple raw                               59,564,920
reflection-disjoint raw                           30,978,490
unique pair masks                                 15,486,081
frozen target masks, all regenerated                     327
genuinely new masks                               15,485,754. (4.2)
```

For later descent, speed is more useful than recomputing the full blocker
antichain.  The next target is the hole of minimum current pair degree,
with row ID breaking ties.  This gives the following additional complete
censuses:

```text
incumbent/target                    E78/row516             E76/row395
current pair pool                      127,008                132,008
target pair degree                         942                    733
raw anchored                         60,963,840             60,963,840
quotient-simple raw                  59,974,574             59,932,504
reflection-disjoint raw              33,166,418             34,684,548
unique pair masks                    16,578,457             17,337,095
current masks regenerated                   942                    733
genuinely new masks                  16,577,515             17,336,362. (4.3)
```

Here row516 and row395 are incumbent-specific hard holes, not generic
symbolic representatives.  Counts from different target rows are not
summed: their catalogue union was not materialized or deduplicated.

For each of rows595, 484, and 631, every one of the 43 E86 holes occurs in
the new target-local catalogue.  For row595 the least non-target E86-hole
coverage is 116,401 masks; the corresponding minima for rows484 and631 are
126,787 and115,778.

## 5. Exact one-pair-swap score

Let an incumbent have reduced row loads `ell_x` and energy

```text
                         Phi = sum_x (ell_x-1)^2.                (5.1)
```

For a candidate incoming mask `N`, the add-only energy increment at a row
of load `0,1,2` is respectively

```text
                              a_ell = -1,+1,+3.                  (5.2)
```

For a selected outgoing pair mask `P`, the remove-only increments are
`b_ell=+3,+1,-1`.  A row in `N intersect P` is actually unchanged.  Since

```text
                              a_ell+b_ell=2                     (5.3)
```

for every load, the exact exchange delta is

```text
Delta(N,P) = sum_(x in N) a_(ell_x)
           + sum_(x in P) b_(ell_x)
           - 2 |N intersect P|.                                (5.4)
```

Selected outgoing rows never have load zero, but the general formula is
used and independently replayed.  If `H` is the incumbent hole set, the
exact change in the number of holes is

```text
-|N intersect H|
+ |{x in P-N : ell_x=1}|.                                     (5.5)
```

The scorer checks all 54 outgoing selected pairs for every generated new
mask and minimizes `(Delta,hole change,outgoing pair index)`.

### Proposition 5.1 (bounded-shard top-K is exact)

Retaining the best `K` distinct masks separately in every worker shard and
then taking the best `K` of their union gives the global best `K`.

Indeed, a mask discarded from one shard has at least `K` strictly better
distinct masks in that same shard, hence cannot belong to the global best
`K`.  The row mask is the final deterministic tie-breaker.  Duplicate masks
have the same score; witness merging retains their least physical witness.

In parallel, the scorer keeps the best `h` masks containing each incumbent
hole.  Merging the per-shard per-hole banks and deduplicating their union
gives the coverage reservoir.

## 6. Certified score outputs

### 6.1 E86, target row595

The top-100,000 score histogram is

```text
Delta -6:      2
Delta -4:     54
Delta -2:   1379
Delta  0:  20881
Delta +2:  77684.                                             (6.1)
```

The best exchange removes frozen pair index `10590`, inserts reduced mask

```text
[36,63,78,149,273,595,631,633,642,654],                       (6.2)
```

fills eight old holes, changes the hole count by `-3`, and has
`Delta=-6`, taking E86 to E80.  The 4,725-mask union of 256-per-hole
reservoirs covers all 43 holes with minimum reservoir degree 256.

An independent Python verifier reconstructed all 104,725 emitted physical
witnesses, their reflected mates, all 54 outgoing scores per witness, both
histograms, strict top order, and the literal E80 load vector.

### 6.2 E78, target row516

Among the top 5,000 masks there are six with `Delta=-2`.  The best removes
pair index `13581`, inserts

```text
[10,34,130,176,202,283,502,516,594,670],                       (6.3)
```

fills seven holes, changes the hole count by `-1`, and takes E78 to E76.
The 2,338-mask union of 128-per-hole reservoirs covers all 39 incumbent
holes.  All 7,338 emitted records and all outgoing swaps were independently
replayed.

### 6.3 E76, target row395

Among the top 5,000 masks there are four with `Delta=-2`.  The best removes
pair index `19587`, inserts

```text
[51,53,107,117,188,226,310,319,327,395],                       (6.4)
```

fills six holes, changes the hole count by `-1`, and takes E76 to E74.  The
2,368-mask coverage reservoir uses 128 candidates per incumbent hole before
union deduplication.  Full-record replay is bound separately.

### 6.4 Continued descent and the first exhausted targets

The next complete oracles are:

```text
state target  unique masks  current overlap  best Delta  direct result
E74   row399    18,520,527       1,176            -2      E72
E70   row459    18,100,072         898            -2      E68
E66   row605    16,459,048       1,089            -2      E64
E64   row348    18,248,848       1,617             0      exhausted
E64   row664    17,933,605       1,796             0      exhausted
E62   row624    14,517,701         937             0      exhausted. (6.5)
```

The direct improving masks are respectively

```text
row399: [115,150,252,274,322,399,408,420,446,634],
row459: [102,192,459,495,501,509,606,610,646,673],
row605: [4,99,117,310,344,352,386,556,599,605].      (6.6)
```

Each has hole change `-1`.  Exact augmented-pool descent after row399 and
row459 supplied the additional moves mentioned above.  The three zero rows
in `(6.5)` are complete **one-swap** exhaustions at their stated incumbent;
they do not rule out a neutral pivot, a self ejection, or a two-swap move.
Indeed row348's neutral bank is precisely what unlocked E62.

## 7. Artifact interface

Scored TSVs have one header and the fields

```text
rows
core
order
reflected_core
reflected_order
owner_ids
reflected_owner_ids
best_outgoing_pair_index
delta
new_energy
hole_change
holes_filled
add_base
covered_incumbent_holes
target_row
tier.                                                          (7.1)
```

The `rows` field alone appends directly to the compact fixed-face instance.
All remaining fields are decode metadata.  Every emitted mask is new
relative to the instance against which it was scored.  The top and
reservoir files may overlap; consumers deduplicate by `rows`.

The intended exact descent loop is:

1. certify a one-exchange local optimum over the current instance;
2. rank its holes, cheaply by current pair degree if desired;
3. completely enumerate one target row;
4. retain all negative masks (top 5,000 is ample in the observed steps)
   plus a 128-per-hole reservoir;
5. append/deduplicate and rerun exact pair/self steepest descent; and
6. mark a target exhausted at that state if its complete oracle has no
   negative mask.

This loop stops only at E0 or when every current hole has been exhausted.

## 8. Scope

Proved here:

* completeness of the anchored raw parameterization for any nonfixed owner
  row;
* exact quotient simplicity, literal reflection disjointness, optional
  free-row filtering, row-mask deduplication, and witness retention;
* exact target-local censuses and complete regeneration of current-pool
  overlaps;
* exact one-pair-swap energy and hole-count formulas;
* exact bounded top-K and per-hole reservoir merging; and
* literal descent witnesses through E64 and complete one-swap exhaustions
  at rows348,664,624, together with the independently certified E62 state.

Not proved here:

* lower-q1 or lower-q2 simplicity of these owner-only columns;
* resource-disjoint simultaneous actuator compilation;
* feasibility of the full owner factor;
* distinctness of catalogues from different target rows after union; or
* that top 5,000 remains sufficient at every future state if more than
  5,000 negative masks occur.

All substantive compilation, enumeration, scoring, replay, compression,
and hashing run through SSH on H100.  The Mac is used only for reading,
editing, transfer, and Git.
