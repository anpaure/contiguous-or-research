# Missing-poset width theorem for fixed-prefix append completion

## Result

Let `P` be a fixed nonzero prefix and append `q` new entries.  Let
`M(P)` be the family of nonempty masks not represented by an interval wholly
inside `P`, ordered by inclusion.

Every successful append satisfies

\[
 \boxed{\operatorname{width}(M(P))\le q.}
\]

This strictly strengthens the earlier fixed-rank endpoint cap.  Applied to
all 465 single deletions of `k11_upper549_natural_array.txt`, it leaves only
deletion 102.  That sole survivor already has an independently verified DRAT
refutation.  Therefore the complete fixed-prefix

```text
delete one of 465 entries, then append 12 entries
```

length-476 neighborhood is now rigorously eliminated.

This is a result about that restricted neighborhood, not a proof that an
arbitrary 476-entry universal word is impossible.

## 1. Endpoint-chain proof

Every target `T` absent from `P` must use a witness whose right endpoint is
one of the `q` appended positions.  Otherwise its witness lies wholly in the
fixed prefix and `T` was not missing.

Fix one appended right endpoint `e`.  The ORs of all intervals ending at
`e` form an inclusion chain:

\[
 U([e,e])\subseteq U([e-1,e])\subseteq\cdots.
\]

Choose one completed-word witness for every target in `M(P)` and group the
targets by their chosen right endpoint.  Each group is a subchain of the
suffix-OR chain at that endpoint.  Thus `M(P)` is covered by `q` chains.
By Dilworth's theorem its width is at most `q`.

Equivalently, every antichain of masks missing from the fixed prefix has
size at most the number of appended positions.  The earlier theorem

\[
 \#\{T\in M(P):|T|=r\}\le q
\]

is the special case in which the antichain is one rank layer.

The proof includes append-only and seam-crossing witnesses and assumes
neither singleton append entries nor a fixed witness length.

## 2. Exact width computation

For a finite missing family `M`, construct the bipartite strict-inclusion
graph with a left and right copy of every mask and an edge

\[
 X_LY_R\quad\Longleftrightarrow\quad X\subsetneq Y.
\]

If `mu` is the size of a maximum matching, Dilworth's theorem gives

\[
 \operatorname{width}(M)=|M|-\mu.
\]

The independent checker

```text
scratch/audit_append_missing_poset_width.cpp
```

uses a simple augmenting-path matcher, recovers a maximum antichain from the
dual minimum vertex cover, and verifies every reported pair is incomparable.
Its SHA-256 is

```text
a1e55a8227ee83963b8932d9f90404e36b8a4041dc39c06ade37d24d5fc29c2b
```

Run it with

```sh
g++ -O3 -std=c++20 scratch/audit_append_missing_poset_width.cpp \
    -o /tmp/audit_append_missing_poset_width
/tmp/audit_append_missing_poset_width \
    11 12 k11_upper549_natural_array.txt
```

## 3. Complete 465-branch distribution

The exact output is

```text
missing-poset width    deletion branches
12                       1
13                      24
14                     115
15                     185
16                     138
17                       2
```

Hence 464 branches violate the necessary width bound `width<=12`.  The only
survivor is

```text
deleted index 102
deleted value 24
missing targets 17
maximum matching 5
missing-poset width 12
```

The three branches that survived the old rank-layer screen are now rejected
structurally:

```text
skip 7      missing 21    matching 8    width 13
skip 89     missing 19    matching 5    width 14
skip 196    missing 19    matching 4    width 15
```

Explicit maximum-antichain certificates include:

```text
skip 7:
251 493 607 941 956 1267 1694 1763 1820 1929 1937 1944 1990

skip 89:
251 493 500 607 941 956 1267 1508 1694 1748 1763 1884 1946 1990

skip 196:
246 251 493 607 941 956 1079 1141 1268 1468 1694 1763 1884 1946 1990
```

The checker verifies pairwise incomparability and matching optimality.

## 4. The sole abstract survivor is certified UNSAT

Deletion 102 is the only branch not eliminated by the theorem.  Its exact
CNF and binary DRAT proof have hashes

```text
2270fd363c941db026ca38cd5b71acbeb2266a2bf9d9aaf20f2290639612b443  CNF
00fed3a7ed55e474f83abba0403090c6b8f328edad1781dd12b008c1318c1b45  DRATB
2a27fd4b0ae8185f72cdfdb0aa701892a82dfff813682fa0c9a87291589762e8  verifier log
```

The independent `drat-trim` log ends in `s VERIFIED` after 25,858,633
resolution steps.  Combining this certificate with the width theorem closes
all 465 branches without relying on any uncertified solver conclusion.

## 5. Production implementation

`append_completion_sat.cpp` now computes the exact missing-poset width for
repair families of at most 4,096 masks, after the cheaper rank-layer screen.
It exits structurally UNSAT whenever the width exceeds `q`.  The explicit
size guard changes no logical behavior on larger formulas; it merely skips
this optional quadratic preprocessing.

For every formula that is built, the source also exposes the complete
endpoint-chain law: endpoint flags belonging to incomparable missing masks
receive at-most-one clauses even when their ranks differ.  If the width is
exactly `q`, one recovered maximum antichain is saturated across all `q`
endpoints, so every endpoint receives exactly one of its members.  These are
logically redundant consequences of the exact OR model and lose no
completion.

The source SHA-256 is

```text
7e49ea13cd92b42a9a7c2bc7c3116e3b9dd6ca80719111b62d9163fef60368e3
```

Independent source inspection confirmed the strict-inclusion predicate and
the layered maximum matcher.  A separately written checker reproduced the
complete width distribution.  The compiled production binary rejected
deletions 7, 89, and 196 with widths 13, 14, and 15.

The original no-deletion branch remains SAT.  Its strengthened inventory is
`1338/71164`, comprising the old formula plus 132 cross-rank incomparability
clauses and twelve saturated-antichain endpoint supports.  A fresh
completion

```text
243 1249 579 542 956 1468 941 1990 1946 493 1884 1694
```

produced a 477-entry word accepted by both independent OR verifiers.
