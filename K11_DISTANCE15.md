# Exact distance-15 decomposition around the `k=11` score-549 row

## 1. Audit outcome

The old file `k11_integrated_allinc14.log` does **not** certify the global
claim that every colour-complete row is at edge distance at least 15 from
`k11_lower956_upper549.txt`.

The logged model used the full Johnson graph, but the corresponding source
enabled `canonicalize` in every `all...` mode.  It therefore fixed

```text
dummy--63
63--119
omitted rank-5 colour 31.
```

Those restrictions are WLOG for an unrestricted existence question: a bit
permutation and path reversal can normalize an omitted lower colour, an
endpoint containing it, and its first edge.  They are **not** WLOG inside a
Hamming ball around one fixed seed.  Applying the normalization to the
candidate also moves the fixed seed and need not preserve the number of seed
edges dropped.

Accordingly, the two-line log

```text
vertices=462 real_edges=6930 variables=43412
UNSAT round=0
```

proves at most UNSAT for that canonical endpoint/first-edge subclass, assuming
the logged binary matches the audited source.  It has no proof trace and does
not by itself independently certify even that narrower claim.

The source has now been corrected so that

```cpp
canonicalize = near_limit < 0 && ...;
```

Any mode with an edge-distance bound therefore leaves the omitted lower
colour and both endpoints free.  Corrected no-canonical runs at distances 14
and 15 are reported below; both return UNSAT, with distance 15 now undergoing
independent proof checking.

## 2. Exact upper-colour ledger

Let `E0` be the 461 real edges of the score-549 seed and let `E` be the 461
real edges of any candidate degree-two solution (a path after adding the
dummy edge, or even a relaxed cycle cover).  Put

```text
d = |E0 minus E| = |E minus E0|.
```

For a Johnson edge `e`, write

```text
u(e) = union of its two rank-6 endpoints,
```

which is a rank-7 colour.  For each rank-7 colour `U`, define

```text
s_U = number of seed edges of colour U,
x_U = number of those seed edges that are dropped,
y_U = number of non-seed candidate edges of colour U.
```

The seed has the exact multiplicity distribution

```text
seed multiplicity 0:  12 colours
seed multiplicity 1: 193 colours
seed multiplicity 2: 107 colours
seed multiplicity 3:  18 colours.
```

Thus it uses `318` of the `330` upper colours, and its multiplicity excess is

```text
107 + 2*18 = 143 = 461 - 318.
```

Let `M` be the set of twelve seed-missing upper colours.  Complete candidate
coverage is exactly

```text
s_U - x_U + y_U >= 1                 for every U.
```

In particular, `y_U >= 1` for every `U in M`.  Define the extra-edge count

```text
e_U = y_U - 1[U in M].
```

Since the seed and candidate have the same number of real edges,

```text
sum_U x_U = sum_U y_U = d,
sum_U e_U = d - 12.                  (1)
```

Therefore every completion with `d <= 15` has at most three extra new edges,
and those edges use at most three upper colours.

The multiplicity-sensitive loss constraint is

```text
x_U <= s_U - 1 + e_U                 (U not in M).    (2)
```

Consequences of (2) include:

* a seed colour of multiplicity one cannot lose its unique seed edge unless
  that same colour receives an extra non-seed edge;
* without an extra edge, a double colour can lose at most one occurrence and
  a triple colour at most two;
* at distance at most 15, at most three distinct singleton seed colours can
  lose their unique occurrence.

This is the exact accounting that a colour-only repair flow omits.

## 3. Sparse case decomposition

Let

```text
Z = {U : e_U > 0}.
```

Equations (1) give `|Z| <= 3`.  Every non-seed selected edge has colour in
`M union Z`; hence every distance-at-most-15 completion lies in

```text
E0 union {Johnson edges whose upper colour is in M union Z}       (3)
```

for some `Z subset rank7`, `|Z| <= 3`.

Conversely, every completion in the Hamming ball has such a `Z`, so (3) is an
exact case decomposition, not a heuristic neighborhood.  There are

```text
sum_(i=0)^3 binom(330,i) = 5,989,776
```

literal support cases.  A fixed support case exposes at most

```text
461 + (12+3)*21 = 776
```

real Johnson edges, because every rank-7 colour contains exactly 21 Johnson
edges of `J(11,6)`.

External enumeration of almost six million cases is unnecessary.  The same
union of cases has an exact compact selector encoding.

## 4. Selector encoding implemented

`recombine_paths_sat.cpp` now accepts

```text
RECOMBINE_EXTRA_SUPPORT=3
```

For each upper colour `U`, it creates a selector `z_U`.

* If `U` already occurs in the seed, every selected non-seed edge of colour
  `U` implies `z_U`.
* If `U` is seed-missing, every pair of selected edges of colour `U` implies
  `z_U`.  Its first edge is the mandatory one; a second edge is extra.
* A sequential counter enforces `sum_U z_U <= 3`.

Together with the existing distance-at-most-15 constraint and all-upper-colour
coverage, this has exactly the same feasible candidates as the original
model.  Given a candidate, set `z_U` precisely on the support of its extra
edges.  Conversely, if `z_U` is false, an existing seed colour admits no
non-seed selected edge, while a missing seed colour admits at most its one
mandatory selected edge.  Thus the selected non-seed edges have the form (3)
for the at-most-three true selectors.

To prevent accidental use as a heuristic restriction, the executable rejects
the option unless

```text
support_limit >= max(0, near_limit - seed_missing_upper_count).
```

For the present instance this is `3 >= 15-12`.  Repair phase hints do not
affect the accounting: the implementation keeps a separate immutable
`seed_edge` vector.

The patched source compiled successfully against CaDiCaL on the RunPod.  Its
distance-15 header is

```text
extra_colour_support=3 selectors=330
vertices=462 real_edges=6930 variables=45193
```

The selector encoding strengthens propagation but does not prove SAT or
UNSAT by itself.

Two corrected searches were launched in interactive remote `tmux` sessions,
replacing two obsolete canonical-restricted jobs and keeping the same CPU
footprint:

```text
k11d14_support   no canonicalization, support cap 2, seed 31414
k11d15_support   no canonicalization, support cap 3, seed 31515
```

Their initial headers are respectively

```text
extra_colour_support=2 selectors=330
vertices=462 real_edges=6930 variables=44402

extra_colour_support=3 selectors=330
vertices=462 real_edges=6930 variables=45193
```

Both corrected searches returned `UNSAT round=0`.  In particular, the
distance-15 instance excludes even a disconnected degree-two cycle cover
satisfying the lower-colour rainbow/endpoint conditions and all rank-7 upper
colours.  It does so before connectivity, factorability, or deeper shadows
are imposed.  Thus the exact-solver result strengthens the local statement to

```text
every fixed-row completion drops at least 16 seed edges.
```

A proof-producing rerun emitted

```text
corrected_allinc15.cnf    45193 variables, 161452 clauses
corrected_allinc15.drat   Kissat exit 20
```

on the RunPod.  An independent DIMACS scan confirmed exactly 45,193 as the
largest variable and exactly 161,452 terminated clauses.  `drat-trim` then
reported

```text
c 33293 of 161452 clauses in core
c 33440 of 146472 lemmas in core using 13430883 resolution steps
c 15750 RAT lemmas in core
s VERIFIED
```

The local proof bundle is in
`scratch/certificates/k11_distance15/`.  The hashes of the uncompressed
proof-critical files are

```text
f556064869e4454b38107bd8d26222639a52276e48f7b90681d2ae2f3ef5ceee  corrected_allinc15.cnf
73f772b06fe0bf2d67116b307d56d09011763143afb68c0eb332f9a158b9f34c  corrected_allinc15.drat
1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2  recombine_paths_sat_support.cpp
f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477  k11_lower956_upper549.txt
```

Thus the distance-at-least-16 statement is now proof-certified, conditional
only on the separately audited mathematical equivalence between the DIMACS
encoding and the relaxed edge-colour problem.

The successor support-cap-4 formula at distance at most 16 has also been
proof-certified.  It has 45,984 variables and 163,030 clauses; the frozen
source regenerated it byte-for-byte on a second RunPod, and `drat-trim`
independently returned `s VERIFIED`.  Hence the rigorously archived statement
is now the stronger one:

```text
every qualifying central candidate drops at least 17 seed edges.
```

The second bundle and exact scope audit are in
`scratch/certificates/k11_distance16/` and `K11_DISTANCE16_AUDIT.md`.

## 5. Precise proof scope

A SAT result from `allinc15` is initially a central-row candidate.  The lazy
solver must still establish, in order:

1. one connected dummy Hamilton cycle / real Hamilton path;
2. absence of internal coordinate runs of lengths 1, 2, or 3;
3. complete rank-4, rank-8, rank-3, and rank-9 shadows (and verification of
   the redundant outer shadows);
4. endpoint availability of the omitted rank-5 colour;
5. natural, then flexible, exact pin-surviving factor labeling;
6. independent enumeration of every interval OR in the resulting
   465-entry array.

Only step 6 plus the proved lower bound `B(11)=465` would establish
`nu(11)=465` and `N(11)=466`.

An UNSAT result for corrected no-canonical `allinc14` would prove only that no
colour-complete central row occurs within fourteen edge replacements of this
seed.  An UNSAT result for corrected `allinc15` after all lazy refinements
would exclude only the distance-15 ball in the fixed-row ansatz.  Neither
would exclude a more distant fixed row, nor the unrestricted monotone-band /
central-forest normal form.

## 6. Reproduction command

After compiling against CaDiCaL on a RunPod, the exact support-strengthened
distance-15 run is

```bash
RECOMBINE_EXTRA_SUPPORT=3 \
RECOMBINE_PHASE_REPAIRS=k11_rank7_flow_phase.txt \
./recombine_paths_sat 11 6 \
    k11_allbase_r7full.txt \
    k11_lower956_upper549.txt \
    allinc15:SEED
```

Heavy search should remain on the RunPods.  The local Mac is used only for
source audit and lightweight certificate checks.
