# K16 H1 all-29 conditioned-capacity independent audit

Date: 2026-07-30  
Status: **GO within the frozen joint13 fibre**

## Result

A structurally separate generic interval enumerator exactly reproduces the
primary all-29 census.  It eliminates the conditioned `H=0x2c6d` charts

```text
0,1,2,3,4,5,7,8,9,10,11,12,13,14,16,17,18,19,22,23,25,26.
```

The seven charts not eliminated by this capacity test are

```text
6,15,20,21,24,27,28.
```

This is not joint13 UNSAT.  A total capacity at least 55 is inconclusive.

## Independent construction

The preflight reads the authenticated JSON maps with a real JSON parser and
derives the 29 intervals afresh from block widths `2,4,3,4`.  It verifies
every witness row's flat and physical endpoints.  It also verifies:

- the explicit CNF has 1,790 variables and 55,852 clauses;
- `H` uses variables `465,...,493`, with its 29-literal at-least-one row and
  all 406 pairwise mutex rows present in the CNF;
- the composed model has 469 variables and 28,233 clauses;
- `H` uses LSB-first code bits `[81,82,83,84,85]`, codes `0,...,28` map
  one-to-one to the same old charts, and invalid codes 29--31 have their
  exclusion clauses in the CNF.

The C++ replay consumes only a 55-by-29 decimal ledger.  Unlike the primary
specialized loops, it decodes a generic canonical tuple, constructs all
intervals using nested `(left,right)` loops, and applies the exact test

```text
interval_OR subseteq target  and  need subseteq interval_OR.
```

It independently rebuilds the 216-state target meet closure and checks that
every state is nonzero and contains common coordinate 6.

## Capacity direction and Hall arithmetic

For a conditioned chart in block `b`, its local maximum counts `H`.  The
other three maxima explicitly delete `H`; otherwise the same target could be
charged more than once.  The generic all-target and without-`H` capacities
happen to agree here:

```text
block capacities = 7,23,14,12.
```

The conditioned capacities, in chart order, are

```text
5,5,5,
12,16,20,23,14,18,21,14,17,13,
9,12,14,9,12,8,
10,12,11,8,9,11,9,10,11,11.
```

Thus a chart in block `b` is excluded exactly when

```text
conditioned_capacity(b,H-chart)
  + sum(other block capacities excluding H) < 55.
```

The four other-block sums are respectively `49,33,42,44`.  Every learned
unit and its deficiency is recomputed row by row in the final audit JSON.

In the explicit CNF, excluded chart `c` gives unit `-(465+c)`.  In the
469-variable model its learned row is the assignment-blocking clause on
`[81,...,85]`: bit `i` is negated iff bit `i` of `c` is one.  All 22 unit and
five-literal mappings are listed in the audit.

## Completeness and scope

For any physical completion, replace each editable cell by the intersection
of labels of selected charts crossing that cell, using `0xffff` for an empty
family.  Every selected chart remains valid: an originally supplied need bit
cannot be removed by an intersected label omitting it, because the same
physical cell would then already violate that label.  Therefore all
canonical cells occur in the enumerated meet closure.

For a fixed tuple, the union of individually compatible targets is an upper
bound on how many targets can be assigned to that block.  Summing independent
block maxima can only overestimate physical capacity.  Consequently a sum
below the 55 one-chart target rows is a valid Hall contradiction.

The conclusion is exact only for arbitrary nonzero substitutions on the
frozen thirteen-cell joint13 support.  It does not normalize unrestricted
length-12,873 words into this fibre, exclude edits outside it, or change the
global K16 bracket.

## Authentication

```text
primary result
  1cf38f49743dce287d3151f60b88831e9bc8cbf8d8c74802a33edb4ad5a46e54
generic replay source
  0eab5f17fb7f0c571376a9408f39d72c2c7081471a63fba16f3429f126e6e5f8
generic replay result
  935fda6ca7d0ef5a19f87bcb6f98c851257a83fd4a918230900a13366ebe9df3
generic replay resource log
  84a5974f2f8250c2d1ffc60e91d4d94d4a7509c17b3b8c84d30b442e0f7d7903
preflight
  449087113cd574f2484bdb4b61cfafdcfd77ebd29d972dd2e6adcfc9c55acd19
final independent audit
  ed1215e3f908c22384b0402f021b0e4421274cc401f0054d20cc0b5f7f29d62e
```

The replay ran on H100 core 36 below the unique directory
`/home/amodo/or15/work/root_k16_h1_h29_capacity_independent_20260730_2b0efe`
with 600-second wall, 590-second CPU, and 1-GiB address-space caps.  It exited
zero after 304.58 seconds with 8,924 KiB maximum RSS and made no `/dev/shm`
writes.
