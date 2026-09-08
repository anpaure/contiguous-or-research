# K16 RF495 tri-window: exact active kernel and the support-three collateral no-go

Date: 2026-07-30  
Status: **proved solver-independent, source-relative theorem; the unrestricted 18-site fibre remains open**

## 1. Frozen source and scope

The authenticated repeat-free parent is

```text
scratch/k15_repeatfree_parents_20260730/K15_REPEATFREE_SEED.word
SHA-256 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

and the frozen RF495 18-cell ledger is

```text
scratch/k16_rf495_score3_20260730.cells
SHA-256 6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

with layout

```text
cells[0:4]
+ parent[6:6436]
+ cells[4:13]
+ (0x8000 | parent[7:6432])
+ cells[13:18].
```

The canonical newline serialization of the reconstructed length-12,873 word
has SHA-256

```text
9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6.
```

Its exact holes are

```text
h0 = 0x18e7,   h1 = 0x3de7,   h2 = 0x9e20.
```

The allowed tri-window positions are

```text
A = [0,3] union [6434,6442] union [12868,12872],       |A|=18.
```

This note studies words obtained by substituting positions of `A` while all
other positions remain equal to the RF495 source.  It proves a no-go only
when at most three positions of `A` change.  It does not settle arbitrary
values on all 18 positions, arbitrary edits outside `A`, or unrestricted
length-12,873 words.

## 2. Exact active-kernel reduction

For a changed support `P subseteq A` and a nonzero target `t`, let

```text
W_x(t) = {source intervals I : OR_x(I)=t},
K(P)   = {t : every I in W_x(t) meets P}.
```

The empty-family convention puts every source hole in `K(P)`.

### Theorem 2.1 (source-kernel equivalence)

If a word `y` differs from the RF495 source `x` only on `P`, then

```text
y is universal  iff  y covers every target in K(P).                 (2.1)
```

#### Proof

Every `t` outside `K(P)` has a source witness avoiding `P`.  The same literal
interval is unchanged in `y`, so it still witnesses `t`.  Thus only `K(P)`
can require new service, and covering all of it is also sufficient.  
\(\square\)

For the full 18-site set `A`, the exact kernel contains 70 targets.  In other
words, 65,465 targets already have a source witness wholly in the fixed
complement.  Deduplicating every interval that meets `A` by

```text
(F_I,Q_I),
F_I = OR of the fixed cells of I,
Q_I = I intersect A,
```

leaves exactly 227 relevant forms.  The enumeration has no collar-width
cutoff: each endpoint scan stops only after its fixed OR saturates.

For supports of cardinality one, two, and three, the exact kernel sizes lie
respectively in

```text
6..17,   8..28,   11..37.
```

The audit contains the complete histogram and target list for every one of
the `18+153+816=987` supports.

## 3. Exact form-selection lemma

Fix one support `P={p_1,...,p_k}`.  A form `(F,Q)` can witness target `t`
only when

```text
F subseteq t,     m=Q intersect P is nonempty.                      (3.1)
```

Cells of `Q-P` retain their source values and are included in `F` before
(3.1) is tested.

Select one eligible form `(F_t,m_t)` for every `t in K(P)`.  Define

```text
U_i = intersection of all t whose m_t contains p_i,
      with empty intersection equal to 0xffff,

R_m = OR of (t minus F_t) over all t with m_t=m.                    (3.2)
```

### Lemma 3.1 (U/R criterion)

The selected forms are simultaneously realizable by nonzero values on `P`
if and only if

```text
U_i != 0                                      for every i,
R_m subseteq OR_{p_i in m} U_i                for every nonempty m. (3.3)
```

#### Proof

For necessity, a physical value `v_i` used in every selected target
containing `p_i` must satisfy `0<v_i subseteq U_i`.  Each required bit in
`R_m` must be supplied by some site of `m`, giving (3.3).

Conversely, assign `v_i=U_i`.  No selected interval overshoots its target,
because `U_i` is a submask of every target using that site.  The second row
of (3.3) supplies every bit of `t-F_t`; together with `F_t` this makes the
selected interval OR exactly `t`.  Sites unused by all selected forms may be
assigned any nonzero value.  
\(\square\)

Both sides of (3.3) are monotone during target insertion: intersections can
only shrink and required unions can only grow.  Therefore a dynamic program
may discard a failed partial state permanently.  Its state is precisely

```text
(U_1,...,U_k ; R_1,...,R_{2^k-1}),
```

so the computation is an explicit finite proof of the displayed Boolean
conditions, not an invocation of SAT, CP-SAT, MILP, or an LP oracle.

## 4. Hole service needs three tri-window sites

The independent provider audit tests every deduplicated witness-form triple
for the three holes.

```text
support size 1:   18 supports, 111 form triples, zero feasible;
support size 2:  153 supports, 7,702 form triples, zero feasible.
```

Thus the three holes cannot be serviced by at most two changed tri-window
sites.  This is already a literal OR-equation contradiction, before any
collateral target is imposed.

The bound is sharp for hole service.  On any three distinct sites, place
`h0,h1,h2` in any order; the three singleton intervals are witnesses.  Hence

```text
minimum tri-window hole-service support = 3,
unordered viable supports               = C(18,3) = 816,
ordered singleton-provider tuples       = 18*17*16 = 4,896.        (4.1)
```

The complete 4,896-row singleton-provider normal-form catalogue is frozen
below.  It is a canonical catalogue of all ordered pairwise-distinct site
tuples, not an assertion that every non-singleton interval realization has
been given a separate row.

Outside this tri-window the service-only minimum is two, as proved by
`MATH_THEOREM_K16_RF495_SOURCE_PROVIDER_SUPPORT_20260730.md`.  Therefore the
number three in (4.1) must not be promoted to an unrestricted support bound.

## 5. Every support-three service face dies on its active kernel

The exact `U/R` dynamic program was run for all supports of sizes one through
three.  The results are

| support size | supports | largest live state set | terminal states | completions |
|---:|---:|---:|---:|---:|
| 1 | 18 | 2 | 0 | 0 |
| 2 | 153 | 5 | 0 | 0 |
| 3 | 816 | 34 | 0 | 0 |

In particular, the 816 sharp hole-service faces from Section 4 all fail once
their complete active kernels are imposed.

### Theorem 5.1 (RF495 tri-window support-three no-go)

No universal word differs from the RF495 source at at most three positions
of `A`.  Consequently any universal completion inside the RF495 tri-window
substitution fibre must change at least four of its 18 sites.

#### Proof

For every proposed support `P` of size at most three, Theorem 2.1 reduces
universality exactly to covering `K(P)`.  Every possible new witness for a
kernel target has one of the enumerated forms.  Selecting one witness per
target is therefore necessary and sufficient.  Lemma 3.1 is an exact test
for simultaneous physical values.  The exhaustive monotone state recurrence
has no terminal state for any of the 987 supports, proving the claim.  
\(\square\)

This strengthens the service-only gate: three edited cells can always create
the holes, but cannot simultaneously repair the source targets whose old
witness families they destroy.

## 6. Exact normalized full-fibre Boolean model

The 70-target, 227-form catalogue also emits an exact normalized Boolean
model for arbitrary nonzero values on all 18 tri-window sites.  Use cell-bit
variables `x[p,b]` and a selector `y[t,f]` for every target/form incidence.
The clauses are

```text
OR_b x[p,b]                                                    for every p,
OR_f y[t,f]                                                    for every t,
not y[t,f] OR not x[p,b]          for p in Q_f and b notin t,
not y[t,f] OR OR_{p in Q_f}x[p,b] for b in t-F_f.              (6.1)
```

There are exactly

```text
288 cell-bit variables,
6,081 witness selectors,
6,369 variables total,
205,557 clauses.
```

Formula (6.1) is satisfiable if and only if some arbitrary nonzero assignment
on the 18 sites covers the 70 active targets; all other targets then retain
their fixed-complement witnesses.  No solver verdict for this full formula
is used here.  The present theorem closes only its change-support-at-most-
three faces.

## 7. Authenticated artifacts and replay

```text
scratch/audit_k16_rf495_triwindow_provider_kernel_20260730.py
  SHA-256 9311bccd2f0a456328de28494bf05d7c711e35d119123bf930471fd5ce1a8049

scratch/k16_rf495_triwindow_provider_kernel_20260730.audit.json
  SHA-256 9977f324091c662e50c88e98122421ca1d28c819c3045fcf5588359419447486
  payload 1fc89efdc39ea6e67cb32514dd43b7506c3f6d2d024003cbb65afbfdc7d3bf5d

scratch/k16_rf495_minimal_singleton_provider_tuples_20260730.catalogue.json
  SHA-256 84e770cc3fc0850f8c71ccfc1ab33446e0d8a35b0d25c892cfbe658a039be274
  payload 584492034249249dfd5c2966d03e92853f85e0789243959ec837ac193de7af24

scratch/k16_rf495_triwindow_exact_form_quotient_20260730.catalogue.json
  SHA-256 63bac356c732a6097d8472445cfeb01bcedae6d13098eaf39d6ced8df3862943
  payload c1cebc33cc3e45a2fa8c7b6ff524b2e4d3971b7a4ea4c0eff52e6fff498c1085
```

The heavy replay was run twice on H100 CPU from the unique directory

```text
/home/amodo/or15/work/rf495_triwindow_kernel_9311bccd
```

with a 600-second wall cap, 3-GiB address-space cap, one Python process,
single-thread numerical-library environment, and `nice -n 19`.  Both runs
returned `RC=0` and reproduced all three file hashes byte for byte.  All
three JSON payload hashes also match independent canonical recomputation
after reload.  No stochastic search, DIMACS solver, SAT solver, CP solver,
or MILP solver was launched by this lane.

The exact K16 bracket remains

```text
12873 <= nu(16) <= 12874.
```
