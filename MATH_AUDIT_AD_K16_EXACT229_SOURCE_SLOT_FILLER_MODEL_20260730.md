# Exact229 component-level source-slot filler model

Date: 2026-07-30  
Lane: AD  
Status: **complete H100 census; two exact/upper outputs, neither improves Hall 25**.

## 1. Frozen source

```text
scratch/search_ad_k16_exact229_source_slot_filler_20260730.cpp
SHA-256 f099372408694f671cf5ae0075857b628594bf252636eb084f40f299ef74d6a3
```

The source compiles cleanly under

```text
clang++ -std=c++20 -O0 -Wall -Wextra -Wpedantic -fsyntax-only
```

The required input chronology is externally pinned to

```text
scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/
    best_upper_complete_bad2.targets
SHA-256 dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d
```

The C++ source checks a strong structural fingerprint and independently
replays its exact229 antecedent, but it does not compute SHA-256 internally.
Any run must check the input hash before launching.

## 2. Exact normal form

In original bad2 coordinates set

\[
 A=[2186,2217)\quad\hbox{forward},\qquad
 B=[1266,1295)\quad\hbox{reverse}.
\]

For every admitted filler interval `F=[lo,hi)` and orientation, the program
performs the literal row permutation

1. delete `A`, `B`, and the source copy of `F`;
2. insert oriented `F` at the vacated `A` slot, between old source rows 2185
   and 2217;
3. insert `A` followed by reverse(`B`) immediately before old source row
   3846.

Origin labels are transported with the rows.  This proves the output length
and rank-eight row multiset are unchanged.  A direct audit checked all four
relative placements

```text
F < B,     B < F < A,     A < F < DEST,     DEST < F.
```

Every origin is inserted or retained exactly once in each case.

## 3. Literal checks

For a materialized inserted interval `[begin,end)`, the function
`literal_d3_interval` checks the seven-row windows starting at exactly

\[
 begin-6,begin-5,\ldots,end-1.
\]

For a deletion gap `begin=end`, these are precisely its six crossing
windows.  The program checks:

* the literal surviving deletion gap of `F`;
* the fixed `B` source gap;
* the complete filler interval at the vacated `A` slot;
* the complete fixed `A+reverse(B)` destination interval.

It then recomputes the full variable-depth middle geometry.  A local-pass
candidate that fails this full replay is rejected and counted; it does not
abort the census.  Finally, `upper_holes` performs unrestricted contiguous-OR
replay for every upper mask, with no width cutoff.

Thus every emitted word is middle-exact, has no zero maximal envelope, and is
arbitrary-upper-complete.  This model does **not** solve the lower compiler or
Hall problem; the ear fields below are candidate incidences only.

## 4. The five source-slot ear tests

Let `s` and `t` be the first positions before and after the inserted filler.
The program tests the exact generalized-compiler candidate predicate at

| target | cell |
|---:|---|
| `091d` | `(s,2)` |
| `291d` | `(s,3)` |
| `291c` | `(s+1,2)` |
| `2e28` | `(t,2)` |
| `2f28` | `(t,3)` |

For each cell it reconstructs maximal envelopes and mandatory carrier bits,
then checks exactly

\[
 M_C\subseteq T\subseteq \bigcup_{p\in C}P_p,qquad
 T\cap P_p\ne\varnothing\quad(p\in C).
\]

The carrier scan `start-3,...,end-1` is sufficient and necessary because all
depths are at most three.

The summary distinguishes the number of hit target incidences from the
number of distinct right cells.  This matters when `|F|=1`, since cells
`(s+1,2)` and `(t,2)` coincide.  No ear count is labelled as a simultaneous
matching improvement.  Every output still requires the full generalized
Hall audit.

Equal materialized value words can arise from different filler-origin
witnesses.  The program deduplicates by the complete value word, merges the
union of ear targets over all witnesses, and separately records the single
witness with the best `(ear-target count, distinct-cell count)`.  It therefore
does not discard a stronger boundary-labelled witness.

## 5. Exact completeness boundary

The enumeration covers every `F` satisfying all of the following.

* `1 <= |F| <= 64`; both orientations are included, with the duplicate
  reversal of a singleton omitted.
* The full six-row source context of `F` precedes the first flat:
  `F.hi+6 <= 6320`.
* `F` is halo-disjoint from `A` and `B` under the inherited strict test.  This
  means at least seven untouched rows separate the packet intervals; the
  equality boundary with six untouched rows is outside scope.
* `F` does not contain the fixed destination cut and does not end exactly at
  it.  In the latter case `A+reverse(B)` occupies the cut, so there is no
  surviving literal `F` deletion adjacency.
* The actual materialized `F` gap passes all six literal D3 windows.

When the `F` gap is at least six rows from the destination, the equivalent
old-word gap test is used as a safe prefilter.  Within five rows, that
prefilter is deliberately disabled and the materialized context is tested;
this avoids the earlier incompleteness in which destination interaction
could be rejected before construction.

No protected-row `4400/4401` filter is imposed.

The model says nothing about interacting `A/B/F` source halos, a filler whose
context meets a flat, `|F|>64`, multiple fillers, coincident destination/gap
cuts, or a moved fixed destination.

## 6. Operational fail-closed behavior

The output directory is rejected if it already contains `pass_*.targets`, so
stale candidates cannot be mixed into a new run.  Candidate-word and summary
writes are checked.  Exact word deduplication uses the full vector, not a
probabilistic hash.

At most 4096 unique upper-complete words are retained in memory.  Exceeding
that cap aborts with an explicit `UNKNOWN` message; it is not an UNSAT or
no-survivor result.  The completed run below stayed below this cap.

## 7. Authenticated H100 census and Hall result

The final source above was compiled and run on one H100 CPU core under a
600-second timeout and 2 GiB address-space cap in

```text
/home/amodo/or15/work/ad_exact229_sourcefiller_27ca0c68_20260730
```

The externally checked source/input hashes and remote binary hash were

```text
dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d  best_upper_complete_bad2.targets
65abf0532b0bbfced9041cbc3d22b48a66ffc7044525e412c37890a62c36d655  included base source
f099372408694f671cf5ae0075857b628594bf252636eb084f40f299ef74d6a3  filler source
095dd4fc39827ebc61e140e30959cbfb46610e38614dbd065df4cd11686f6a38  remote binary
```

The exact census returned

```text
oriented_blocks=19620
old_gap_prefilter_pass=10900
materialized_source_gap_pass=18383
literal_component_pass=7
full_middle_reject=0
full_exact=7
upper_complete_rows=2
unique_upper_complete=2
```

It did not hit the 4096-word cap.  The two unique outputs are:

| filler | best source-slot ears | word SHA-256 | incidences | matching | deficiency | shore |
|---|---|---|---:|---:|---:|---:|
| `[6253,6263)` reverse | `2e28,2f28`, distinct cells | `0c19e3c73616a4d771f29f8031aebd946131f4eeb20a571f59852458ec0f0760` | 347799 | 26305 | 27 | 212/185 |
| `[1225,1226)` | none | `7e708f542daa88e821a4b1748115d0250a9faf77e2e7dffd71fb66b62e367f35` | 347817 | 26305 | 27 | 216/189 |

Both outputs preserve the complete middle chronology and unrestricted upper
coverage.  Their independently rebuilt generalized compiler graphs have
deficiency 27, two worse than exact229's 25.  In particular, the first word
is a literal positive source-return construction for two desired endpoint
ears, but it is not a Hall descent: other changed source-slot incidences move
additional deficiency units into the new canonical shore.

Therefore the one-filler source-slot normal form is exactly closed as a Hall
improvement.  This is not a no-go for two fillers, touching halos, a longer
filler, or a simultaneous correction at the filler's own source collar.
