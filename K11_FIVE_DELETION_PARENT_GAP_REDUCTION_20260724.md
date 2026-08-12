# Parent-gap reduction from four deletions to five deletions

## Verdict

There is a sound transfer theorem from a four-deletion prefix to any of its
five-deletion children.  It does **not** say that a child must have a
width-15 parent.  Instead, it identifies exactly which parent-missing masks
can be healed by the extra deletion.

For a five-deletion set `D` and a restored position `e in D`, let

```text
P5       = the prefix after deleting D,
P4(e)    = the prefix after deleting D \ {e},
M5       = the masks missing from P5,
M4(e)    = the masks missing from P4(e),
G(e)     = OR values of P5 intervals crossing the gap created at e.
```

Then, exactly,

```text
M4(e) \ G(e)  subseteq  M5.                              (1)
```

Consequently, completion by sixteen appended entries requires

```text
width(M4(e) \ G(e)) <= 16                 for every e in D. (2)
```

This is a genuine pruning condition lying between the nonmonotone parent
widths and the full recency formula.

Its useful compact corollary is

```text
width(M4(e)) <= 27.                                        (3)
```

Thus every four-deletion set whose missing family has width at least 28
gives one sound four-literal blocking clause for the variable five-deletion
formula.  The completed four-deletion ledger proves that at least 62,265
such parent clauses exist.  Their identities were not archived by the
aggregate scan, so extracting and adding them requires a new rank-only
parent pass and a rebuilt CNF; the live formulas and solvers were not
modified.

The reduction is mathematically valid but quantitatively modest.  The
stronger exact condition (2) rejects none of the 2,727 known width-16
five-deletion branches obtained from the 790 four-deletion survivors.
Hence the 790 UNSAT certificates do not themselves provide a sound clause
blocking their five-deletion supersets.

## 1. Exact residue theorem

Fix `e in D`.  In `P4(e)`, the entry at original position `e` separates its
nearest retained predecessor and successor.  Deleting it compresses these
two sides together in `P5`.

Every interval of `P5` is of one of three kinds:

1. wholly to the left of the new gap;
2. wholly to the right of the new gap;
3. crossing the new gap.

An interval of the first two kinds is an unchanged physical interval of
`P4(e)`.  Therefore, if `T` is missing from `P4(e)` but covered in `P5`, every
`P5` witness for `T` must cross the gap.  Its OR belongs to `G(e)`.  This
proves (1).

Equivalently, every mask in `M4(e) \ G(e)` remains missing after the fifth
deletion.  Since the missing family of any prefix completable by `q`
appended entries is covered by the `q` suffix-OR chains at the new endpoints,
its width is at most `q`.  Taking `q=16` proves (2).

This theorem is exact about the only possible healing mechanism.  It does
not assume monotonicity of missing families, which is false.

## 2. Width of the cross-gap family

Let

```text
L1 subset ... subset La
R1 subset ... subset Rb
```

be the distinct nonempty suffix ORs to the left of the gap and prefix ORs to
the right.  Every cross-gap value has the form

```text
Li union Rj.
```

The map from the product of the two chains to `G(e)` is order preserving.
Preimages of pairwise incomparable image values are pairwise incomparable,
so

```text
width(G(e)) <= width(C_a x C_b) = min(a,b).
```

In a `k`-bit word, a strict suffix-OR or prefix-OR chain has at most `k`
nonempty values.  Hence

```text
width(G(e)) <= k.                                          (4)
```

For `k=11`, (1), subadditivity of width, and a completable child give

```text
width(M4(e))
 <= width(M5) + width(G(e))
 <= 16 + 11
 = 27,
```

which is (3).

The same argument can be applied rank by rank.  Since one rank is an
antichain, a parent with at least 28 missing masks in any one rank is
uniformly forbidden as a parent of a completable five-deletion branch.

## 3. Clauses for the variable-deletion CNF

The production map numbers the deletion variable for original zero-based
position `i` as `D_i = i+1`.  If the four-deletion set

```text
F = {a,b,c,d}
```

has missing width at least 28, every five-deletion superset of `F` is
impossible by (3).  Under the exact-five deletion counter, the sound clause
is simply

```text
(-D_a or -D_b or -D_c or -D_d).                            (5)
```

No append variable is needed.

The full four-deletion ledger contains two disjoint certified sources:

```text
maximum missing-rank count 28,29,30     56,525 + 5,420 + 226
rank-feasible branches of exact width 28                         94
total known width-at-least-28 parents                         62,265
```

Thus a future extraction pass can add at least 62,265 clauses of length
four.  Each forbidden parent has 461 possible fifth deletions.  Counting
parent-child incidences and using the fact that a five-set has five
four-subsets shows that these clauses exclude between

```text
ceil(62,265 * 461 / 5) = 5,740,833
```

and

```text
62,265 * 461 = 28,704,165
```

distinct five-deletion sets.  Relative to `C(465,5)`, this is between about
`0.00324%` and `0.0162%`.  It is a legitimate low-cost propagation layer,
not a transformative reduction of the 177-billion-branch universe.

The existing full scan retained only aggregate counts and width-15 survivor
rows, not the identities of the width-at-least-28 parents.  Producing (5)
therefore requires a new low-priority, rank-first extraction pass.  No such
pass was launched while the production solvers were live.

The checkpoint-friendly extractor

```text
scratch/extract_four_parent_rank28_clauses.cpp
```

accepts a half-open range of the smallest deleted index, so independent
shards can be run and resumed without another atomic all-branch job.  It
emits the four-literal DIMACS clauses directly and writes its tested/forbidden
inventory to standard error.  Its SHA-256 is

```text
0f1adf4a038ceabb0b250150877cb035a43d75f56521a9dcc8f0fc9f8c39d808.
```

A low-priority smoke shard on smallest indices `430<=i<462` checked all
`C(35,4)=52,360` quadruples in that tail and emitted no clause, as expected
for this low-impact tail.  The complete extraction was deliberately not run
alongside the live five-deletion solvers.

## 4. Exact audit on the 2,727 targeted five-deletion branches

The checker

```text
scratch/audit_five_deletion_parent_gap_reduction.cpp
```

independently reconstructs every parent prefix, every child prefix, and the
cross-gap family.  It asserts (1) mask by mask, computes all widths by exact
maximum matching, and asserts the universal `width(G)<=11` bound.

On

```text
scratch/k11_length476_joint_delete5_sa_20260724/
  all_790_extensions/width16_branches.txt
```

it checked all `2,727 * 5 = 13,635` parent-child incidences and returned

```text
tested five-deletion branches             2,727
child width 16                            2,727
rejected by parent residue                    0
worst residual width 16                   2,727

parent residual widths
13:11, 14:1000, 15:8556, 16:4068

per-branch widest cross-gap width
2:4, 3:29, 4:106, 5:2588

all individual parent cross-gap widths
0:1973, 1:124, 2:612, 3:2990, 4:4675, 5:3261
```

The residual inclusion assertion never failed.  The output and source
hashes are

```text
44def184179502814f3b87cf849a4d1e37da9084731ef37c518ad63508452f65  audit_five_deletion_parent_gap_reduction.cpp
f874ed45202c3b1cf003fe8bd0af12d432d66dc3f8aa1e58e90933d82f294300  parent_gap_audit.out
8a6b0fda926e944a2930e9177951f8a8ef8c05e53e833b5672cb624c1cc393a6  parent_gap_audit.time
```

This is an instructive tightness result.  Every targeted child saturates the
new condition at width 16 for at least one parent.  The parent-gap theorem
therefore supplies no additional rejection inside that already selected
family.

## 5. Why the 790 UNSAT certificates do not lift

The four-deletion certificates decide a different completion problem:

```text
four deleted prefix entries + 15 appended entries.
```

The five-deletion formula has both an additional deleted prefix entry and an
additional appended endpoint.  Neither formula is a restriction of the
other.  Restoring the fifth entry can destroy child witnesses crossing its
gap, and removing one appended endpoint can destroy an entire suffix chain.
There is no resolution-valid operation that turns a four-parent DRAT proof
into a clause blocking all its five-deletion supersets.

The failure already occurs in the two-bit toy problem.  The fixed prefix

```text
[3]
```

cannot be completed universally with one appended nonzero mask: appending
`1`, `2`, or `3` always misses one singleton.  After deleting the prefix
entry, however, the two appended masks

```text
[1,2]
```

form a universal word.  Thus parent `q`-append UNSAT does not imply child
`q+1`-append UNSAT even in the smallest relevant setting.

Nonmonotonicity under restoration is equally explicit.  In three bits,
deleting the middle entry from

```text
[1,4,2]
```

creates the compressed interval `[1,2]` with OR `3`; restoring `4` destroys
that witness.  This is exactly the cross-gap phenomenon isolated by (1).

Therefore it would be unsound to add the 790 clauses

```text
not(all four survivor positions are deleted).
```

Their 2,727 known width-16 supersets are not ruled out by the four-parent
proofs; they require their own exact completion formulas.

## 6. Practical conclusion

The sound reusable information from the four-deletion calculation is:

1. the exact parent-gap residue condition (2), useful for branch screening;
2. the uniform parent-width cap 27, yielding at least 62,265 short clauses;
3. saturated residual antichains of size 16, which may be useful as
   conditional endpoint-bijection propagation in fixed five-deletion
   formulas.

The first two are proved and implemented at the audit level.  The third is
a possible propagation refinement, not yet a compact global encoding.

The direct certificate-lifting strategy is closed: the 790 four-deletion
UNSAT proofs provide no sound deletion-superset clause for the five-deletion
formula.  Any stronger global reduction must either extract the parent-gap
clauses, encode child missing-family information directly, or use a genuine
joint recency argument involving all sixteen appended endpoints.
