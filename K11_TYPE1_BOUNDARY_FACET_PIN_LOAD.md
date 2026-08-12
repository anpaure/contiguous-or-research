# Type-I boundary-facet pin load

## 1. Result

Assume the exact Type-I `k=11,n=465` branch.  Thus

```text
A[0]=T=63={0,1,2,3,4,5}
```

is the unique literal six-set, and the 464-position suffix has the exact
rank-five boundary--core decomposition

```text
P_5 || C_4 || Q_5.                                    (1.1)
```

The entries of `P_5,Q_5` are distinct literal five-sets.  Every entry of
`C_4` has rank at most four, and `C_4` represents all 561 nonempty masks of
ranks at most four.

For a five-set `R`, put

```text
p_R^C = #{i in C_4 : A[i] subseteq R}.
```

Then the following pointwise pin-load law holds:

```text
p_R^C >= 20                         for every five-set R. (1.2)
```

In particular, for each of the six facets `R_b=T\{b}`, `b=0,...,5`,

```text
#{i in C_4 : A[i] subseteq T\{b}} >= 20.               (1.3)
```

These six rows are a compact, coordinate-sensitive consequence of the inner
rank-five peel.  They are not a new scalar rank count and are not implied by
the current rank-profile, selected-width, rank-seven-width, or six-subcube
support-count ledgers.

The outer rank-six complement rectangle contributes no further target-name
restriction: with one boundary cell it degenerates to the endpoint prefix
chain already encoded by `K11_FOREST_TYPE1_PREFIX_CHAIN`.

## 2. The support-run theorem

Fix a five-set `R`.  Let

```text
P_R={i in C_4:A[i] subseteq R}
```

and decompose `P_R` into maximal consecutive runs.

The core has length `q+2`, where `q` selected witnesses for distinct
nonliteral rank-five masks live wholly in the core.  The ordered-antichain
segment lemma consequently says:

* every core interval of length at least three contains a selected
  rank-five witness;
* a core interval of length four contains at least two distinct selected
  rank-five witnesses.

It follows that every `P_R`-run has length at most three.  Indeed, two
distinct selected rank-five masks contained in a length-four support interval
would both be rank-five subsets of `R`, and hence would both equal `R`.

There is at most one length-three `P_R`-run.  Every such run contains a
selected rank-five witness; its value is a rank-five subset of `R`, hence is
`R`.  The one selected witness for `R` cannot lie in two disjoint support
runs.  If `R` is a literal boundary value, its aligned selected witness is
the boundary singleton, so in that case there is no length-three support run
at all.  Only the weaker universal statement "at most one" is needed below.

Every one of the 30 nonempty proper subsets of `R` has a witness in `C_4`.
Such a witness has physical length at most two, because every core interval
of length at least three contains a rank-five witness.  A support run of
length `g` contains exactly `2g-1` singleton and adjacent-pair cells.  If
`p=p_R^C` and `rho` is the number of support runs, the total candidate-cell
capacity is therefore

```text
2p-rho.                                               (2.1)
```

Since all runs have length at most two except possibly one run of length
three,

```text
p <= 2rho+1,
rho >= ceil((p-1)/2).                                (2.2)
```

For `p<=19`, equations (2.1)--(2.2) give at most

```text
2*19-ceil(18/2)=29
```

candidate cells, fewer than the 30 distinct proper targets.  This proves
(1.2).

The constant 20 is sharp for this local argument.  The 30 masks in
`B_5\{empty,[5]}` admit a partition into ten triples

```text
X, Y, X union Y,
```

so ten separated two-cell support runs have exactly the required 30 labels.
The finite checker below records one explicit partition.

## 3. Aggregate endpoint-facet form

Summing (1.3) over `b in T` gives

```text
sum_(i in C_4, A[i] subseteq T) (6-|A[i]|) >= 120.     (3.1)
```

Indeed a rank-`s` entry contained in `T` belongs to exactly `6-s` of the six
facets.  The six pointwise rows are stronger than (3.1), but the aggregate
identity explains their boundary-pin meaning: the low core must supply at
least 120 missing-coordinate incidences inside the fixed endpoint six-set.

## 4. Exact SAT design

The current full Type-I portfolio already enables the exact six-subcube
support bank.  Retain the 464 support literals

```text
support_T[i] <-> A[i] subseteq T,  1<=i<=464,
```

for `T=63`, and reuse the exact rank-five flags.  For each `b=0,...,5` and
suffix position `i`, define

```text
y[b,i] <-> support_T[i] AND !A[i,b] AND !rank5[i].      (4.1)
```

Because every suffix entry has rank at most five and the rank-at-most-four
positions are exactly `C_4`, `y[b,i]` is precisely
`[i in C_4 and A[i] subseteq T\{b}]`.  Impose the six exact comparisons

```text
sum_i y[b,i] >= 20.                                    (4.2)
```

No endpoint selector, target bank, or new coordinate-support bank is needed.
The exact incremental inventory is

| component | variables | clauses |
|---|---:|---:|
| `6*464` three-input conjunctions | 2,784 | 11,136 |
| six exact 464-input counters | 5,520 | 38,640 |
| six direct comparisons to 20 | 0 | 12 |
| **total** | **8,304** | **49,788** |

The count assumes reuse of the existing true constant and `support_T`
literals.  If the support vector is not retained as a member of the current
subcube plan, doing so changes no CNF inventory.  A direct seven-literal
definition from array bits is also possible but costs 11,136 additional
clauses.

The natural production guard should require

```text
K11_FOREST_RANK_FILTRATION_TYPE1=1
K11_FOREST_SUBCUBE_DEFICIENCY=1.
```

The named-cell guard is not logically required: the length-two localization
used in the proof follows already from the exact inner rank-five endpoint
geometry.  Enabling it remains useful for propagation.

## 5. Strictness against the current scalar ledger

The following abstract ledger passes the currently encoded scalar rows:

```text
entry ranks (n1,...,n6) = (11,45,110,258,40,1),
rank-5 widths y          = (40,284,138),
rank-6 widths x          = (1,42,284,135),
rank-7 widths z          = (0,4,42,284).
```

It has `y2=138>=96+40`, satisfies all five joint rank-five/rank-six
generating rows, and has truncated rank-seven moment exactly 940.  Its
rank-five and rank-six entry moments are respectively 11,016 and 20,261,
above the encoded thresholds 7,392 and 14,322.

At the six-subcube level, take `p_T=32`, take 406 other six-subcube counts
equal to 44 and 55 equal to 43.  Their total is 20,261, matching the rank-six
entry moment, and every run-credit charge is zero.  The Type-I correction at
`T` contributes only one unit and also passes.

These scalar data do not control the intersection with a facet.  They permit
all 32 positions supported by `T` to contain one fixed coordinate `b`, so
that the abstract support of `T\{b}` is zero.  Equation (1.3) forbids this.
Thus the new row is strictly outside the present scalar ledger.  It remains,
of course, a consequence of the full universal interval-OR formula; its role
is to expose that consequence cheaply to the solver.

## 6. Verification

The independent finite checker is

```text
python3 scratch/check_k11_type1_boundary_facet_pin_load.py
```

It verifies the extremal run-capacity calculation, the explicit sharp
30-mask partition, every scalar-ledger row quoted above, and the exact CNF
inventory.  This theorem and design do not assert SAT, UNSAT, or a changed
bound for `nu(11)`.
