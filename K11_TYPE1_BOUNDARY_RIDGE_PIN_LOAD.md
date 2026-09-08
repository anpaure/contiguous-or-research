# Type-I boundary-ridge pin load

## 1. Result

Assume the exact Type-I `k=11,n=465` branch.  After deleting the fixed
literal rank-six endpoint `T=63`, the suffix has the exact inner peel

```text
P_5 || C_4 || Q_5,
```

where every entry of `C_4` has rank at most four and `C_4` represents every
nonempty mask of rank at most four.  For a four-set `Q`, define its **strict
core support**

```text
s_Q^C = #{i in C_4 : A[i] is a proper subset of Q}.
```

Then

```text
s_Q^C >= 10                         for every four-set Q.       (1.1)
```

In particular, the six facets of the fixed endpoint have fifteen pairwise
intersections

```text
Q_bc = T \ {b,c},                    0 <= b < c < 6,
```

and all fifteen obey (1.1).  These are the codimension-two, or **ridge**,
rows beneath the six already encoded facet rows.

The word "strict" matters.  If `m_Q^C=#{i in C_4:A[i]=Q}` and
`p_Q^C=#{i in C_4:A[i] subseteq Q}`, then (1.1) is equivalently

```text
p_Q^C >= 10 + m_Q^C.                                      (1.2)
```

Thus literal copies of the ridge do not pay any part of its ten-position
proper-pin demand.

## 2. Proof

Index `C_4` locally as a segment of length `q+2`, containing selected
witnesses `I_1,...,I_q` for distinct nonliteral rank-five masks.  Exact
rank-five endpoint slack gives

```text
I_i subseteq [i,i+2].                                     (2.1)
```

Consequently every interval of length at least three in `C_4` contains a
selected rank-five witness.  This is the same unrestricted inner-core fact
used in the boundary-facet theorem.

Fix a four-set `Q` and mark precisely the positions whose entries are proper
subsets of `Q`.  A marked run has length at most two: a marked interval of
length three would have OR contained in `Q`, but by (2.1) it would contain a
rank-five witness.

Every one of the fourteen nonempty proper subsets `S` of `Q` has a witness
wholly in `C_4`.  Every entry of such a witness is contained in `S`, hence is
a proper subset of `Q`, so the witness lies in one marked run.  It has length
at most two by the preceding paragraph.

If the strict support has `p` positions in `rho` runs, the number of
singleton and adjacent-pair cells available inside those runs is

```text
2p-rho.
```

All runs have length at most two, so `rho>=ceil(p/2)` and the capacity is at
most

```text
p + floor(p/2).                                           (2.2)
```

For `p<=9`, (2.2) is at most thirteen, less than the fourteen different
proper targets.  Therefore `p>=10`, proving (1.1).

The constant is sharp for this local argument.  Five separated two-position
runs with endpoint labels

```text
(1,2), (3,4), (5,8), (6,12), (9,10)
```

have pair unions `3,7,13,14,11`; their ten singleton cells and five pair
cells cover every mask `1,...,14`.  All endpoints are proper subsets of the
four-set `15`.  A second five-run gadget in the checker covers all fifteen
nonempty masks while still using ten strict entries, showing that absence of
a literal `Q` does not improve the threshold by this argument.

## 3. Second-order endpoint-pin form

Summing (1.1) over the fifteen ridges inside `T` gives

```text
sum_(i in C_4, A[i] proper-subset T, |A[i]|<=3)
    C(6-|A[i]|, 2) >= 150.                               (3.1)
```

A rank-`s` entry strictly contained in `T`, for `s<=3`, belongs to exactly
`C(6-s,2)` four-set ridges.  The pointwise fifteen rows are stronger than
(3.1): they demand ten pins for every *specified pair* of missing endpoint
coordinates rather than only 150 incidences in aggregate.

This is the next level of the boundary pin onion:

```text
six endpoint facets:          >=20 contained C_4 positions each;
fifteen endpoint ridges:      >=10 strictly contained C_4 positions each.
```

## 4. Compact SAT design

The deployed facet module already defines, for each `b<6` and suffix
position `i`,

```text
y[b,i] <-> [i in C_4 and A[i] subseteq T\{b}].
```

For each pair `b<c`, define

```text
z[b,c,i] <-> y[b,i] AND !A[i,c] AND !rank4[i].           (4.1)
```

The suffix rank cap and the exact rank flags make (4.1) precisely

```text
[i in C_4 and A[i] proper-subset T\{b,c}].
```

Indeed, `y[b,i]` supplies membership in `C_4` and containment in `T\{b}`;
removing `c` leaves a four-set, and `!rank4[i]` excludes the only
non-strict possibility.  Impose

```text
sum_i z[b,c,i] >= 10             for all 15 pairs b<c.   (4.2)
```

Using the production Wallace/ripple counter convention, the exact
incremental inventory over the existing facet variables is

| component | variables | clauses |
|---|---:|---:|
| `15*464` exact three-input conjunctions | 6,960 | 27,840 |
| fifteen exact 464-input counters | 13,800 | 96,600 |
| fifteen direct comparisons to 10 | 0 | 30 |
| **total** | **20,760** | **124,470** |

The natural guard should require

```text
K11_FOREST_TYPE1_FACET_PIN_LOAD=1
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_LOCAL_DENSITY_PB=1.
```

No new coordinate-support bank, endpoint selector, or target selector is
needed.  This note specifies and audits the design; it does not edit the
production solver.

## 5. Strictness against the present auxiliary ledger

The checker constructs a deterministic 465-entry multiset with the exact
Type-I rank architecture

```text
A[0]=63,
entry ranks (n1,...,n6)=(31,45,110,238,40,1),
twenty distinct rank-five entries on each side of one C_4 block.
```

It has one rank-at-most-four component, all forty literal five-sets are
distinct, and every coordinate singleton occurs.  More strongly, its actual
support minimum at each subcube rank `1,...,10` is

```text
1,2,5,9,18,33,61,108,187,297,
```

so it passes every pointwise nested-local-density row currently known.  Its
exact six-set support moment is 24,881, and all six fixed facet loads are at
least 20.  The usual selected-width summaries

```text
x=(1,42,284,135), y=(40,284,138), z7=(0,4,42,284)
```

pass the singleton-pool, joint-width, and Type-I truncated-rank-seven rows.
The outside coordinate columns can be relabelled into the residual lex
quotient, so its endpoint prefixes have the canonical six-value form.

Nevertheless, for `Q=T\{0,1}` its strict core support is exactly nine.  The
multiset is not claimed to satisfy the full interval-OR formula; it is a
separation from the currently exposed rank, support, width, onion, prefix,
and six-facet summaries.  The base CNF already implies (1.1); the proposed
module exposes that distributed consequence cheaply.

## 6. Verification and scope

Run

```text
python3 scratch/check_k11_type1_boundary_ridge_pin_load.py
```

The checker verifies the extremal capacity, two sharp gadgets, the exact
gate/comparator truth tables and inventory, and the deterministic strictness
certificate against the current auxiliary rows.

This theorem is globally WLOG inside Type I and is coordinate-sensitive.  It
does not prove SAT or UNSAT, change the bound on `nu(11)`, or assert that the
auxiliary strictness certificate is a universal word.
