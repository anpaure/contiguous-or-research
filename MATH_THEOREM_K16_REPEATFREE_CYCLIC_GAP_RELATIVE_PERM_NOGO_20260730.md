# Exact no-go for every cyclic four-cell gap and every relative permutation

## 1. Scope

Let `B` be any of the six authenticated optimal `k=15`, length-`6438`
parents

```text
scratch/k15_repeatfree_parents_20260730/k15seed_0.word
...
scratch/k15_repeatfree_parents_20260730/k15seed_5.word.
```

Seeds `1` and `5` are the two parents whose depth-two middle trace is
repeat-free.  The other four have one repeat and are included as a stronger
secondary census.

Choose either orientation of `B`, choose any of its `6438` cyclic positions,
delete the four consecutive cells starting there, and linearize the remaining
cyclic segment as a word `B'` of length `6434`.  Consider a boundary lift

```text
A | {z} | (z + pi(B')),
```

where `A` is any unmarked prefix word and `pi` is an arbitrary permutation of
the fifteen old coordinates.  The following result is exact.

> **Theorem.** None of the `6 * 2 * 6438 = 77,256` oriented cyclic-gap
> configurations admits a relative coordinate permutation `pi` that covers
> all marked masks.  In particular, none of the
> `2 * 2 * 6438 = 25,752` configurations from the two repeat-free parents
> works.  Every configuration has an explicit two-cycle precedence
> obstruction, so the theorem is independent of the choice of `A`.

This rules out only this single-boundary architecture.  It does **not** rule
out multi-sector interleavings, rethreading either parent, two separated gaps,
or edits of physical cells.

## 2. Exact precedence reduction

Let `S` be the suffix-OR change chain of `A`, let `P` be the prefix-OR change
chain of `B'`, and let `H` be the old masks not realized by intervals internal
to `B'`.  The marked masks missed internally are exactly `pi(H)`.  Cross-seam
intervals have old-coordinate projection

```text
s OR pi(p),    s in S, p in P.
```

For `h in H`, let `p_h` be the largest member of the nested chain `P` which is
contained in `h`, and put `q_h = h \ p_h`.  Smaller contained prefixes can
only enlarge `q_h`, so using `p_h` loses nothing.

For an old target coordinate `y`, let `tau(y)` be its first entry time in the
suffix chain `S`.  Then

```text
s OR pi(p_h) = pi(h)
```

for some `s in S` if and only if

```text
max {tau(pi(x)) : x in q_h}
    <
min {tau(pi(y)) : y notin h}.                         (1)
```

Indeed, equality is equivalent to

```text
pi(q_h) subseteq s subseteq pi(h),
```

and a suffix-chain value lies between those two masks exactly under (1).

Thus every `h` generates the strict precedence arcs

```text
x -> y    for x in q_h and y outside h.
```

A relative permutation merely assigns the source vertices of this graph to
the suffix-entry times of `A`.  Any directed cycle is therefore impossible.
Conversely, when the graph is acyclic, a `2^15` ideal dynamic program with the
exact suffix-time group capacities decides and reconstructs `pi`.  Hence the
reduction covers all `15!` relative permutations; it is not an AGL or
annealing screen.

## 3. Census result

The optimized scanner evaluated every configuration on the H100 CPU.  The
full six-parent result is

```text
UNSAT_IN_SCOPE configs=77256 acyclic=0
```

and the primary repeat-free subfamily is recorded separately as

```text
requested_repeatfree_configurations=25752
requested_repeatfree_acyclic=0
```

The internal-hole counts range from `10` to `36`.  More strongly, the
shortest directed cycle has length exactly `2` in every one of the `77,256`
rows.  Each TSV row records the two coordinates and the two absent masks
which witness the opposite arcs.

An independent program then reconstructed every oriented cyclic segment
directly from the parent word.  For each recorded edge it independently:

1. proved that the witness mask is absent from every internal interval;
2. recomputed the largest contained prefix directly from the physical cells;
3. checked the required `x in q_h` and `y outside h` memberships.

It checked `154,512` edge witnesses and returned

```text
rows=77256 edge_witnesses=154512 failures=0
PASS_INDEPENDENT_ALL_TWO_CYCLES
```

This second audit does not call the scanner's hole-enumeration or graph
construction routines.

## 4. Interpretation

The repeat-free discovery removes the inherited middle ghost, but does not by
itself solve the even lift.  A single `A | z | B'` boundary has only one
suffix chain and one prefix chain.  The holes of every cyclicly opened parent
force contradictory ordering requirements on two old coordinates.  No
relative relabelling can repair that contradiction.

Consequently the live construction must use a genuine phase braid or another
multi-sector chronology.  This is consistent with the verified length-12874
word, whose `z`-bit pattern has many alternating runs rather than one marked
rail.

## 5. Artifacts and hashes

```text
e2e7a7a9f11ac5f69df69296a6a2579e0eb5ffa933db7997cea594ce5f289976  scratch/search_k16_repeatfree_cyclic_gap_relative_perm_exact_20260730.cpp
73bdc5cafa5b2e51a45de4fcb14efc380d8696d7c9b20142615a905c885e9670  scratch/audit_k16_repeatfree_cyclic_gap_precedence_cycles_20260730.cpp
8fe39182d40ca19e0c25f15f1d7126b46e8230323ebed4247896357176f38f48  scratch/k16_repeatfree_relative_perm_exact_20260730/cyclic_gap_all6_rows.tsv
4923d2c50764c94427757731c11091c0e7d84d396eaa96f0c171f377ea78e10e  scratch/k16_repeatfree_relative_perm_exact_20260730/cyclic_gap_all6_summary.txt
27b41a01a9b4425d8db38be7d7b245b0df8e856c1fd9ade585a9721525f605c7  scratch/k16_repeatfree_relative_perm_exact_20260730/cyclic_gap_all6_independent.stdout
6281a334dcbbee2938c2fd62d9897f5d07e12a8dbc6198a8b88e301fa83cd2ff  scratch/k16_repeatfree_relative_perm_exact_20260730/cyclic_gap_all6_independent.stderr

018fa0a98239950ddd1a2a7a23c0666d96da91429dec77330524e0317c92f7ef  scratch/k15_repeatfree_parents_20260730/k15seed_0.word
93484c945194c628b761f5b9a67111365d00fc1727d7e19839f07b74fee96d49  scratch/k15_repeatfree_parents_20260730/k15seed_1.word
ba9e83cced86e0b3d40890c10e30ad59cb703a50529b7830fa83f4fd28f01c49  scratch/k15_repeatfree_parents_20260730/k15seed_2.word
38ef44eaceb7c0ff3edcb694bc260ff020824c73d0fa0d23bd1e6fd5ecd135cf  scratch/k15_repeatfree_parents_20260730/k15seed_3.word
57a8370c1df54e2f79eb3af269f57b3b9840546cbb6c4862d6cf2adbcd94b2ae  scratch/k15_repeatfree_parents_20260730/k15seed_4.word
4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6  scratch/k15_repeatfree_parents_20260730/k15seed_5.word
```

