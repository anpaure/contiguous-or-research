# Independent audit of the corrected `k=11` distance-15 certificate

## 1. Verdict

The archived round-zero certificate is sound for the exact local theorem
stated below.  It has no endpoint, omitted-colour, first-edge, bit-permutation,
or path-reversal canonicalization.

The frozen source regenerates the archived CNF byte for byte:

```text
variables  45193
clauses    161452
SHA-256    f556064869e4454b38107bd8d26222639a52276e48f7b90681d2ae2f3ef5ceee
```

The archived proof has uncompressed SHA-256

```text
73f772b06fe0bf2d67116b307d56d09011763143afb68c0eb332f9a158b9f34c
```

and was independently accepted by `drat-trim` on a RunPod different from
the machine recorded in the original Kissat log.

The retained second-machine log is

```text
scratch/certificates/k11_distance15/corrected_allinc15_independent_dratcheck.log
SHA-256 233ebd0fff8211b5aef534adb0e99f8b71139437584a056c469ac659e8479e37
```

## 2. Exact theorem certified

Let `V` be the 462 rank-six subsets of `[11]`, and let `J=J(11,6)`.  Let
`E_0` be the 461 unoriented edges of
`k11_lower956_upper549.txt`.

There do not exist a real-edge set `E subseteq E(J)` and two distinct
vertices `p,q in V` satisfying all of the following.

1. In the real graph `(V,E)`, `p` and `q` have degree one and every other
   vertex has degree two.  The graph is allowed to be a disjoint union of
   one `p`--`q` path and any number of cycles.
2. At most fifteen seed edges are dropped:

   \[
                         |E_0\setminus E|\le15.
   \]

3. The rank-five intersection colours `A intersect B`, for `AB in E`, are
   pairwise distinct.
4. Every rank-seven set occurs as an upper colour `A union B` of some edge
   `AB in E`.
5. The unique rank-five colour not used by an edge of `E` is contained in
   at least one of `p,q`.

Because both `E_0` and `E` have 461 real edges, condition 2 is equivalently

\[
 |E_0\setminus E|=|E\setminus E_0|\le15.
\]

Thus every connected Hamilton-path candidate satisfying conditions 3--5
must drop at least sixteen seed edges.  In symmetric-difference language,
its edge set is at distance at least 32.

## 3. Formula audit

The proof-producing mode is

```text
allinc15
```

with `RECOMBINE_EXTRA_SUPPORT=3`.  Parsing the mode gives

```text
all_edges       = true
core_mode       = inc15
near_limit      = 15
incremental     = true
ordered         = false
use_pair        = false
use_quad        = false
use_runs        = false
canonicalize    = false
```

The two input files each contain 462 masks.  The first contains every
rank-six mask exactly once; the preferred file is also a permutation of
that layer and its consecutive pairs are 461 distinct Johnson edges.
Consequently the generated 6,930 real variables are exactly all edges of
`J(11,6)`.

### Degree clauses

For each vertex, the clauses obtained by omitting one incident literal at a
time enforce degree at least two.  The sequential counter enforces degree at
most two.  The dummy vertex receives the same exact-degree-two condition.
Removing the dummy therefore leaves precisely two distinct real vertices of
degree one and all others of degree two.  Connectivity is not imposed in
round zero.

The selected augmented graph has 463 edges in total.  Two are dummy edges,
so exactly 461 real Johnson edges are selected.

### Distance clauses

For each of the 461 preferred edges the counter receives the literal
`not edge`.  Its upper bound is fifteen.  The counter is sound for arbitrary
literals, including negative edge literals, and every assignment obeying the
bound has an extension to its auxiliary variables.

### Lower colours and endpoints

Every Johnson edge between rank-six masks has a rank-five intersection.
Pairwise negative clauses inside each colour bucket make these 461 selected
real colours distinct.  There are 462 possible rank-five colours, hence
exactly one is omitted.

For every rank-five target `C`, the endpoint clause is

```text
(an edge of intersection colour C)
or
(a selected dummy edge at a rank-six vertex containing C).
```

All clauses except the one for the omitted colour are already satisfied by
a real edge.  The remaining clause is exactly condition 5.

### Upper colours

For every one of the 330 rank-seven sets, one clause contains all Johnson
edges having that union.  These are exactly the complete-upper-colour
constraints in condition 4.

### The support cap is equisatisfiable

The preferred path misses exactly twelve upper colours and has multiplicity
distribution

```text
missing 12, singleton 193, double 107, triple 18.
```

If `d<=15` preferred edges are dropped, exactly `d` nonpreferred edges are
selected.  Complete upper coverage uses at least one of these for each of
the twelve missing colours.  After reserving those twelve mandatory edges,
there are at most `d-12<=3` extra nonpreferred edges.

For a colour present in the seed, every selected nonseed edge forces its
selector.  For a seed-missing colour, a second selected edge forces its
selector.  Hence at most three selectors suffice for every candidate in the
distance ball.  Conversely the clauses do nothing beyond enforcing that
at-most-three support statement.  Setting selectors exactly on colours
carrying an extra edge extends every candidate satisfying conditions 1--5.
The selector counter therefore strengthens propagation without deleting a
candidate covered by the theorem.

### No invalid canonicalization

The corrected condition is

```cpp
canonicalize = near_limit < 0 && ...;
```

and `near_limit=15`, so both canonicalization blocks are unreachable.  In
particular, the CNF does not fix

```text
the omitted rank-five colour,
either endpoint,
the first real edge,
an orientation,
or a bit permutation.
```

The initial path changes variable numbering and solver phases only.  The
optional repair file changes phases only; it does not modify the immutable
`seed_edge` vector or any clause.  Regeneration without phase hints produced
the identical CNF hash, independently confirming this point.

## 4. Artifact reproduction

The source snapshot

```text
scratch/certificates/k11_distance15/recombine_paths_sat_support.cpp
```

has SHA-256

```text
1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2
```

and is byte-identical to the audited current source.  Compiling that snapshot
on the second RunPod and dumping the formula from the two supplied paths
gave the same CNF hash as the archive.  Decompressing the proof on that pod
gave the manifest hash above.  The independent proof-check output ended in

```text
s VERIFIED
c verification time: 119.205 seconds
```

## 5. Scope exclusions

The certificate does **not** prove any of the following.

* It does not prove `nu(11)>465`, `nu(11)=465`, or `N(11)=466`.
* It does not exclude a candidate dropping sixteen or more seed edges.
* It does not exclude a more distant fixed central row.
* It does not exclude the unrestricted monotone-band or central-forest
  normal forms.
* It does not certify connectivity, delay-three run factorability, ranks
  3, 4, 8, or 9, longer upper shadows, or factor labeling.  Those conditions
  are absent because the certified formula is UNSAT before lazy refinement.
* The unarchived trusted-solver observations at distance sixteen are not part
  of this theorem.

The rigorously certified advance is exactly a radius-15 exclusion around one
fixed rank-six seed, already in a relaxation allowing disconnected cycle
covers.
