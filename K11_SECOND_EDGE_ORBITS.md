# `k=11` full search split by the canonical second-edge orbits

## 1. Purpose

The proof-certified distance shells show that a successful fixed-row repair
must drop at least eighteen edges of the score-549 seed.  This makes another
local Hamming shell progressively less attractive.  The next search is the
complete Johnson graph, but it should use all exact symmetry available.

For an unrestricted ordered rank-six path, bit permutations and path reversal
allow the following canonical prefix without loss of generality.

* The omitted rank-five intersection colour is
  `C={0,1,2,3,4}`.
* The first endpoint is `E=C union {5}`.
* The first neighbour is
  `F=E setminus {3} union {6}`.

The existing full-graph canonicalization already imposes these choices.
This note proves that the next edge has exactly four stabilizer orbits.

## 2. Four-orbit lemma

### Lemma 1

After fixing `C,E,F`, every legal second neighbour of `F`, modulo the
setwise stabilizer of this prefix, is represented by exactly one of

\[
 \begin{array}{c|c|c|c}
 q&\text{removed from }F&\text{added to }F&\text{representative mask}\\ \hline
 0&0&3&126\\
 1&0&7&246\\
 2&5&3&95\\
 3&5&7&215.
 \end{array}                                      \tag{2.1}
\]

#### Proof

The stabilizer of `C,E,F` has the following orbits on coordinates:

\[
 \{0,1,2,4\},\quad\{3\},\quad\{5\},\quad\{6\},
 \quad\{7,8,9,10\}.
\]

Here `3` is the bit removed by the first edge, `5` is distinguished by the
endpoint, and `6` is the bit added by the first edge.  A Johnson neighbour of
`F` removes one bit of `F` and adds one bit outside `F`.

Removing bit `6` makes the new edge intersection equal to

\[
 F\setminus\{6\}=E\cap F,
\]

repeating the first rank-five edge colour.  The rainbow condition forbids
this entire removal orbit.  The remaining removal choices are the common
orbit `{0,1,2,4}` and the singleton `{5}`.  The addition choices are the
singleton `{3}` and the fresh outside orbit `{7,8,9,10}`.  Their Cartesian
product gives exactly the four cases in (2.1).  The stabilizer is transitive
within each displayed coordinate orbit, so each case has one representative.
\(\square\)

### Corollary 2

Running the four cases `q=0,1,2,3` is exhaustive for unrestricted fixed-row
existence.  No candidate is lost, and no distance-to-seed symmetry is being
used.

## 3. Implementation

`recombine_paths_sat.cpp` accepts

```text
RECOMBINE_SECOND_ORBIT=0|1|2|3
```

inside the WLOG canonical ordered branch.  It fixes the selected directed
arc from `F` to the corresponding representative in (2.1).  The option is
rejected unless the invocation is the complete `k=11`, rank-six, ordered
Johnson graph with the WLOG canonical branch active.  An independent audit
found that the first guard also admitted certain sparse seed-dependent
modes; the current source explicitly requires `all_edges`, `k=11`, and
`rank=6`, closing that scope bug.

For `k=11`, each full-graph initial formula has

```text
462 rank-six vertices
6930 Johnson edges
60142 variables
655251 clauses
```

before lazy factorability and deeper-shadow cuts.  Four remote searches are
running in modes

```text
RECOMBINE_SECOND_ORBIT=q
RECOMBINE_TARGETS=k11_initial_targets.txt
recombine_paths_sat_orbit ... allordinc
```

The base CNF already imposes a connected ordered Hamilton path, distinct
rank-five intersection colours, all rank-seven union colours, endpoint access
to the omitted lower colour, and a triple-union witness for rank-eight mask
`958`.  When a model appears, the lazy loop adds exact delay-three run cuts
and every missing rank-3, rank-4, rank-8, and rank-9 shadow constraint.  A
surviving path must subsequently pass the exact factor-label model; the orbit
split does not weaken any of these gates.

The implementation also accepts

```text
RECOMBINE_MIN_DISTANCE=18
```

as a redundant cardinality constraint: at most `443` of the seed's `461`
real edges may remain.  This is logically justified by the independently
verified distance-17 UNSAT theorem, which already holds in the weaker model
allowing disconnected cycle covers.  It therefore removes no candidate from
the stronger ordered search and prevents the global solver from repeatedly
reconstructing the now-certified radius-17 ball.

## 4. Scope

This is a genuine symmetry reduction of the full fixed-central-row search.
It is not a theorem about unrestricted monotone-band or central-forest
solutions, and an UNSAT result in all four branches would still rule out only
the fixed-row ansatz unless the stronger unrestricted reduction is supplied.
