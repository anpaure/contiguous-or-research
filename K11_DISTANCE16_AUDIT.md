# Independent audit of the corrected `k=11` distance-16 certificate

## 1. Verdict

The distance-16 bundle is valid for the exact local theorem in Section 2.
The frozen source regenerates its archived CNF byte for byte, and the
archived DRAT proof was independently accepted on a RunPod different from
the proof-producing machine.

The proof-critical values are

```text
CNF variables       45984
CNF clauses         163030
CNF SHA-256          d39ed5022cd464cc5c1c124702cc213d8afe8c19267a1d2baad3c9cb76eb85a4
DRAT SHA-256         3aff03f9f2be1f27084b6e19d06c9091e249114f0aa95fb7f72c87dbe8590717
source SHA-256       1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2
seed SHA-256         f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477
```

## 2. Exact theorem certified

Let `V` be the 462 rank-six subsets of `[11]`, let `J=J(11,6)`, and let
`E_0` be the 461 unoriented consecutive edges of
`k11_lower956_upper549.txt`.

There is no real-edge set `E subseteq E(J)` with distinct vertices
`p,q in V` satisfying all five conditions below.

1. In `(V,E)`, the vertices `p,q` have degree one and every other vertex
   has degree two.  Disconnected cycle components are allowed.
2. At most sixteen seed edges are absent:

   \[
                         |E_0\setminus E|\le16.
   \]

3. The 461 rank-five intersection colours `A intersect B`, `AB in E`, are
   pairwise distinct.
4. Every rank-seven set occurs as `A union B` for at least one `AB in E`.
5. The unique omitted rank-five intersection colour is contained in `p` or
   `q`.

The degree equations force `|E|=|E_0|=461`, so

\[
 |E_0\setminus E|=|E\setminus E_0|.
\]

Consequently any connected Hamilton-path candidate having the same central
colour properties must drop at least seventeen seed edges.  Its ordinary
edge-set symmetric difference from the seed is therefore at least 34.

## 3. Exact regeneration

The audited invocation is

```text
RECOMBINE_EXTRA_SUPPORT=4
recombine_paths_sat 11 6 \
    k11_allbase_r7full.txt \
    k11_lower956_upper549.txt \
    allinc16:31616
```

with `RECOMBINE_DUMP_CNF` and `RECOMBINE_DUMP_ONLY=1` for regeneration.
The source snapshot in the bundle is byte-identical to the current audited
source.  Compiling it against CaDiCaL on the independent pod produced

```text
extra_colour_support=4 selectors=330
vertices=462 real_edges=6930 variables=45984
dumped clauses=163030
```

and the resulting file had exactly the archived CNF hash above.

The first input contains every rank-six mask exactly once, so its 6,930
real edges are precisely the complete Johnson graph.  The preferred input
is another permutation of the same layer and has 461 distinct consecutive
Johnson edges.

## 4. Clause-level equivalence

Mode parsing gives

```text
all_edges       = true
core_mode       = inc16
near_limit      = 16
incremental     = true
ordered         = false
use_pair        = false
use_quad        = false
use_runs        = false
canonicalize    = false
```

Thus the dumped round-zero CNF contains exactly the following substantive
constraints.

### Exact degree two with a dummy vertex

For every real vertex and the dummy, omission clauses enforce degree at
least two and sequential counters enforce degree at most two.  The selected
augmented graph has 463 edges.  Exactly two are dummy edges to distinct real
vertices `p,q`, leaving 461 real edges.  Removing the dummy gives one
`p`--`q` path component and any number of real cycle components.

### Distance at most sixteen

The distance counter receives `not e` for each of the 461 preferred edges
and has upper bound sixteen.  The counter is sound and complete for these
negative literals: selected literals force the corresponding prefix-count
states, while any assignment containing at most sixteen true literals has a
minimal extension to the auxiliary states.

### Lower-colour rainbow and endpoint access

Every Johnson edge has a rank-five intersection.  Pairwise negative clauses
within every colour bucket make the 461 selected real colours distinct.
Exactly one of the 462 possible colours is therefore omitted.

For every rank-five `C`, the formula requires either a selected real edge of
colour `C` or a selected dummy edge at a rank-six vertex containing `C`.
This is equivalent to requiring that the one omitted colour be contained in
at least one endpoint.

### Complete upper colours

For each of the 330 rank-seven sets, one clause contains exactly the 21
Johnson edges having that union.  These clauses are precisely condition 4.

### Exact four-colour support strengthening

The seed misses twelve upper colours.  A candidate dropping `d<=16` seed
edges selects exactly `d` nonseed edges.  Complete upper coverage consumes
at least twelve of them, one for each missing colour, leaving at most

\[
                         d-12\le4
\]

extra nonseed edges.

For an upper colour already present in the seed, any selected nonseed edge
forces that colour's selector.  For a seed-missing colour, any selected pair
forces its selector; its first edge is the mandatory baseline edge and its
second is extra.  Hence every candidate covered by the theorem activates at
most four selectors.  Conversely, setting selectors on exactly the colours
carrying an extra edge extends every such candidate to the support clauses.
The cap is therefore equisatisfiable with the unstrengthened distance-16
model, not a heuristic restriction.

## 5. Canonicalization audit

The corrected source enables canonicalization only when

```cpp
near_limit < 0
```

but this invocation has `near_limit=16`.  Neither canonicalization block is
executed.  The formula fixes none of the following:

```text
omitted rank-five colour
first or second endpoint
first real edge
path orientation
bit permutation
```

The two input paths determine vertex numbering, the fixed seed used in the
distance counter, and solver phases.  Vertex numbering is only a bijective
renaming.  Phases do not enter the dumped clauses.  The optional repair file
also changes only the mutable phase vector, while distance and support use
the separate immutable `seed_edge` vector.  Regeneration without phase hints
still produced the identical CNF hash.

## 6. Independent proof check

The original Kissat log identifies its machine as

```text
70b635274a4a
```

The independent audit ran on

```text
f93817d72edc
```

after separately decompressing and hashing both archived artifacts.  The
independent `drat-trim` run ended in `s VERIFIED`.  Its retained log is

```text
scratch/certificates/k11_distance16/corrected_allinc16_independent_dratcheck.log
SHA-256 5ee96e05433078db7efb25a0ae24521a29217caca5ffefe7b4beb75bb4093e8b
s VERIFIED
verification time: 197.202 seconds
```

## 7. Exact exclusions from the theorem

This certificate does **not** do any of the following.

* It does not determine `nu(11)` or `N(11)`.
* It does not exclude candidates dropping seventeen or more seed edges.
* It does not exclude a more distant fixed rank-six row.
* It does not impose connectivity, delay-three factorability, rank-3,
  rank-4, rank-8, or rank-9 shadows, longer upper shadows, or factor labels.
* It does not exclude unrestricted monotone-band or central-forest optima.

The certified result is exactly a radius-16 exclusion around one fixed seed,
already proved in the relaxation that permits disconnected cycle covers.
