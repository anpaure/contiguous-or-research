# K17 rooted flags: exact exchange-column/global-optimizer interface

Date: 2026-08-01  
Lane: H2 independent architecture/audit support  
Status: exact column semantics and reduced-model formulation; no global solve

## 1. Frozen inputs and the exact local domain

The baseline is the authenticated rooted factor

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

For a row `r`, put

\[
 \theta_r=(\operatorname {type}_r,[C_{0,r}],
                         [C_{0,r}\cup C_{1,r}]).       \tag{1.1}
\]

The exact two-row catalogue independently keeps or swaps each of the three
coordinates of `theta_q,theta_r`, then enumerates every literal partition of
the two fixed roots which realizes the resulting tickets.  It contains

```text
raw rooted flags                       2,722,720
root pairs with a feasible exchange       26,867
distinct feasible ticket patterns          26,961
literal realization pairs                 213,670.
```

Every realization pair preserves the two-row multiset in the type ledger and
both suffix ledgers.  Hence every **root-disjoint** set of such columns
preserves the complete static factor.  This statement is exact; allowing two
selected columns to write the same root is not legal composition.

The frozen per-owner witness file is only a projection: it stores one
individually successful realization for each of the 782 baseline incoming-
dead owners.  It is not the complete column table and it is not a simultaneous
assignment.

## 2. Why isolated repair masks cannot be used as cover clauses

An incoming turn at owner `o` depends on an ordered pair of the nine aligned
root incidences at `o`.  If a column changes roots `q,r`, only owners incident
with `q` or `r` can change status, at most 18 owners.  It is therefore useful
to record, for each column, the affected-owner list and the baseline versus
isolated-column live masks.

Those masks are **not monotone**.  A second, root-disjoint exchange may still
touch another root incident with the same owner and destroy the ordered pair
which witnessed the first column's gain.  Consequently the clause

\[
       \bigvee_{c:\ o\text{ is an isolated gain of }c}x_c       \tag{2.1}
\]

is not proof-safe.  Isolated gains and losses may be used for branching or an
objective only.  Exact owner support must be reconstructed from the final row
options.

The O3 materializer

```text
scratch/build_h2_k17_rooted_flag_exchange_column_master_20260801.cpp
```

emits all 213,670 columns, a deduplicated row-option table, the nine aligned
incidences of each owner, and the isolated gain/loss masks with this caveat in
the output scope.  Its source is syntax-checked but the full materialization
was deliberately not launched in this lane.

## 3. Exact compact column-matching model

This first model is the exact root-disjoint two-row-exchange subclass.  Let
`e_c` select exchange column `c`, and let `b_r` mean that root `r` retains its
baseline flag.  Impose

\[
 b_r+\sum_{c\ni r}e_c=1\qquad(r\in\mathcal R).       \tag{3.1}
\]

For each distinct flag option `a` available at root `r`, introduce `x_{r,a}`
and channel it to (3.1): the baseline option equals `b_r`, while a nonbaseline
option is the sum of selected incident columns assigning that option.  Root
disjointness makes these sums Boolean.  No separate static ledger rows are
needed in this subclass because every selected column is ledger-neutral.

For owner `o`, aligned incidence positions `i != j`, and final options `a,b`
on their two distinct root packets, precompute the literal recurrence

\[
 b\in C^i_2,\qquad C^j_2\subseteq C^i_1,
                 \qquad C^j_1\subseteq C^i_0.        \tag{3.2}
\]

For every compatible tuple create a support atom `y_(o,i,a,j,b)` and add

\[
 y\le x_{r_i,a},\qquad y\le x_{r_j,b},qquad
 \sum_{(i,a,j,b)\text{ compatible}}y_{o,i,a,j,b}\ge1. \tag{3.3}
\]

The reverse Tseitin implication is unnecessary: (3.3) merely chooses one
true compatible pair.  Equations (3.1)--(3.3) are necessary and sufficient
for a root-disjoint exchange packing whose final table gives every owner at
least one loop-free incoming turn.

This remains only a singleton-support relaxation.  It does not enforce a
root/owner state transversal, a directed cycle cover, connectedness, voltage,
or upper/source/compiler rows.

## 4. Stronger recommended row-option model

The column-matching face omits ticket permutations on cycles of length three
or more and all overlapping sequences of two-row exchanges.  A stronger but
still compact reduced model retains the unique row options appearing in the
213,670 columns, adds the baseline option and the option from certificate
28401 at every root, and chooses directly

\[
             \sum_{a\in A_r}x_{r,a}=1.              \tag{4.1}
\]

Because columns are no longer selected, exact static rows must be restored:

\[
 \sum_{r,a:\operatorname {type}(a)=t}x_{r,a}=m_t,  \tag{4.2}
\]

and, for every rank-two-through-seven necklace ticket `S`,

\[
 \sum_{r,a:\,[C_0(a)]=S\text{ or }[C_0(a)\cup C_1(a)]=S}
 x_{r,a}=1.                                         \tag{4.3}
\]

The two alternatives in (4.3) have different ranks in the certified type
list, so its coefficients are zero or one.  Rank eight is automatic from one
option per root.  Equations (3.2)--(3.3) then give exact final-table owner
support.  This model is exact within its explicitly exported option domain;
it is not the unrestricted 2,722,720-flag factor model.

## 5. Correct use of the two proposed seeds

The greedy incidence cover has 173 roots.  It is only a necessary touch
cover.  In the disjoint-column face the number of changed-ticket roots is
even, so those 173 roots cannot themselves be the exact support of a column
matching.  Use the cover for variable activity or a soft objective, not as a
hard pin; ledger partners outside the cover must remain available.

The alternate static certificate is

```text
scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/certificate_28401.tsv
SHA256 e973061f57d1e4c141dc42489da289a0b454d4b9fd27369d887561fdea29299e
```

An independent local replay gives:

```text
static rooted verifier                      PASS
literal state arcs                         7,688
zero-in / zero-out packet roots          822 / 739
zero-in / zero-out owner orbits           703 / 7
flags changed from baseline                 1,426
complete tickets changed                    1,419.
```

It cannot be represented by a root-disjoint selection of the 213,670
columns: every nontrivial column changes the complete tickets of exactly two
roots, whereas 1,419 is odd.  It is therefore a valid full-factor hint for
the direct row-option model (4.1)--(4.3), but not an incumbent for the
column-matching model (3.1).

A proof-safe CP-SAT strategy is:

1. include every column-derived option plus all 1,430 alternate-certificate
   options;
2. add (4.1)--(4.3) and exact support rows (3.2)--(3.3);
3. use certificate 28401 only as `AddHint` values;
4. give the 173 cover roots preferred branching/low change cost, while
   retaining all partner roots;
5. on any SAT assignment, ignore solver-side cached masks and replay the
   literal table from scratch.

## 6. Required independent decoder

For a selected table the decoder must fail closed unless it verifies:

1. one literal partition of the declared root at every one of 1,430 rows;
2. the nine exact type masses;
3. every rank-two-through-seven suffix orbit exactly once;
4. all nine aligned incidences of every owner reconstructed independently;
5. at least one literal ordered pair satisfying (3.2) at every owner;
6. in column mode, root-disjoint selected columns and exact agreement between
   their endpoint flags and the decoded row options.

Passing these checks proves only a zero-singleton-defect static/owner-support
table.  The complete nine-state transition graph and its state-transversal
matching must then be rebuilt.  A local incoming witness per owner does not
imply packet-support Hall, much less one nonzero-voltage cycle.

## 7. Scope

No solve was launched and no repaired K17 factor is claimed.  The theorem is
the exact optimizer interface and the two non-composition warnings: isolated
gain masks are not cover columns, and certificate 28401 lies outside the
root-disjoint two-row-exchange face.
