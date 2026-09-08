# The repo-owned graded quotient pipeline: exact gates and calibration

Date: 2026-07-29

Status: implementation and `k=11` calibration complete; `k=15` search in
progress.  This note does **not** claim a `k=15` word.

## 1. What is now implemented

The self-contained implementation is

```text
scratch/graded_quotient_pipeline.py
```

It does not import any file from the changing
`~/Downloads/opusproblem/work` directory.  Its stable quotient catalogue:

* works for every odd `k`, not only primes;
* excludes quotient self-loops from the Hamilton-circuit table;
* stores explicit `(lower representative,a,b)` triples and a table digest;
* accepts bare numeric choice IDs only when they agree with those explicit
  triples;
* requires voltage coprime to `k`, not merely nonzero;
* uses actual target-orbit sizes in the compiler quotient.

At `k=15` the central quotient has `429` vertices per shore.  There are
`12012` raw extension choices, of which `14` are quotient self-loops, leaving
`11998` circuit-legal choices.

The prime guard in the older `scratch/sigma_sat_solver.py` cannot safely be
removed by itself.  That model rejects only voltage zero; at composite
`k=15`, every nonunit voltage (for example `3` or `5`) produces multiple
physical lift cycles.  It also counts upper-orbit incidences as unit weight in
its optional load caps.  This is false on the periodic rank-nine orbits: the
rank-nine target represented by `7399` has orbit size `5`, and the choice
`(lower=1255, a=11, b=12)` contributes physical load `3` to each orbit member
although the old quotient constraint counts it as `1`.  The repo-owned model
therefore requires `gcd(voltage,k)=1`, uses Boolean coverage only where that is
sound, and postpones multiplicity-sensitive claims to actual-orbit weighted
flow plus the final physical matching.

The carrier model has exact eager constraints for the quotient circuit,
perfect lower-q1 rainbow, unit voltage, residence, and upper-q1.  CEGAR
checks lower-q2, the lower-q3/rank-five Hall-positive gate, and all upper
shadows.

## 2. The exact lower-q3 boundary

Let `P` be the maximal depth-three erosion of a resident rank-eight carrier.
The graded Hall graph assigns every target `S` of rank at most five literally
to a position satisfying

```text
C_i <= S <= P_i.
```

For rank five, `|S|=|P_i|=5`, so the last containment is equivalent to
`S=P_i`.  Therefore

```text
missing lower-q3 target
  <=> missing rank-five value of P
  <=> zero-degree Hall target.
```

It is not an additional frozen derivative row, but it is a necessary
positive-degree gate before any one-core can work.  The pipeline checks it
before the expensive Hall search and feeds failures back to carrier CEGAR.

The exploratory lower-q2 builder had also omitted motifs in which the two
outside insertions coincide.  That omission was false: the inserted
coordinate is absent from the middle set and hence cannot enlarge the
three-way intersection.  The corrected builder has `515` groups for the
`k=11` target orbit represented by `201`, including the selected witness
`[394,503]`.  This is now a permanent regression test.  No future run should
reuse the unpatched `equi3.py` builder.

The old upper-q2 DNF has the exact dual defect: it forbids the left and right
neighbors from deleting the same middle coordinate.  That deletion is legal,
because the middle state itself retains the coordinate and the three-way
union is unchanged.  At `k=11`, upper target orbit `255` has `979` compact
state-path witness pairs but only `817` in the old DNF; all `162` additional
pairs are valid.  The production compact encoding includes them.  An old
DNF-based UNSAT result is therefore not authoritative on either side.

The lower-q3 CEGAR itself now has a compact exact encoding.  For a fixed
rank-`r-3` target `S`, its states are the `C(k-|S|,3)` central supersets of
`S`; three allowed Johnson transitions are linked to the selected directed
quotient arc variables, and every coordinate outside `S` is required to be
absent from at least one of the four states.  At `k=15` this uses `120`
states per missing orbit instead of about `122000` DNF witness triples.

The independent exhaustive audit

```text
scratch/audit_compact_q3_equivalence.py
```

compares the compact state paths with the full DNF oracle for all `15`
rank-three target orbits at `k=11`.  The two witness sets agree exactly for
every orbit (`20261` or `20517` choice triples, depending on orbit type).

The construction is a generic exact shadow encoding.  For lower depth `q`
and target `S` of rank `r-q`, take `q+1` states from the central supersets of
`S`, link consecutive states by selected directed quotient arcs, and require
each coordinate outside `S` to be absent from at least one state.  This is
equivalent to intersection exactly `S`.  Dually, for an upper target `U` of
rank `r+q`, take central subsets of `U` and require every coordinate of `U`
to occur in at least one state; this is equivalent to union exactly `U`.

The implementation now uses this generic primitive for lower and upper q2
and q3.  On the residence-perfect `k=15` seed, all `86` missing constraints
(`47` lower-q2, `11` lower-q3, `27` upper-q2, `1` upper-q3) build in `6.38s`
with `46,930` variables and `457,330` constraints.  The large DNF builders
remain small-instance correctness oracles, not production encodings.

## 3. The compiler is an exact matching, not greedy punching

For an equivariant one-core `C<=P` with `DC=DP`, form the physical graph

```text
target S -- position i  iff  C_i <= S <= P_i.
```

The weighted quotient max flow is checked first, with actual orbit sizes;
then an independent physical Hopcroft--Karp matching is required.  A matched
word satisfies

```text
C <= A <= P  =>  DP=DC <= DA <= DP  =>  DA=DP.
```

This identity is why adjacent changed letters are harmless.  The older
`punch.py` imposed pairwise nonadjacency and used a greedy conflict-removal
loop; its five-of-six result on `k=11` measured that extra restriction, not
compiler feasibility.  The exact graded compiler passes `231/231` on the
same instance.

At composite `k`, the final physical matching is allowed to break rotation
symmetry.  At `k=15` its target-orbit profile is

```text
rank 1: 15^1
rank 2: 15^7
rank 3: 15^30 + 5^1
rank 4: 15^91
rank 5: 15^200 + 3^1.
```

## 4. Independent deterministic calibration

The immutable explicit source carrier is

```text
scratch/fixtures/k11_equivariant_carrier_explicit_v1.json
```

and its normalized stable selector is

```text
scratch/fixtures/k11_equivariant_carrier_repo_v1.json.
```

The pipeline constructs a canonical equivariant one-core, obtains weighted
quotient flow `231/231`, confirms a physical matching `231/231`, chooses an
upper-safe cut, appends the three-letter prefix, and emits

```text
scratch/k11_graded_pipeline_repo.word.txt.
```

An independent verifier reports

```text
length                 465 = B(11)
nonempty masks         2047 / 2047
D^3 middle row         462 distinct rank-six masks
status                 VERIFIED_OPTIMAL
SHA-256                 b90eebd0f9f4eb50084ec3f70f333f19cadb4b0138b8cc695502e6e5b6654862
```

The build and verification were repeated on the remote CPU host and produced
the identical hash.

## 5. The first `k=15` exact seeds

The residence-only quotient ablation found a strict voltage-one cycle in
`626.05s` on eight remote CPU workers.  It is serialized with explicit stable
choices as

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json.
```

Its exact defects are

```text
residence violations                0
lower-q2 missing orbits             47
rank-five positive missing orbits   11
upper missing by rank               67 at rank 9, 27 at rank 10, 1 at rank 11
```

Two controlled 1,800-second ablations did not return a model:

```text
upper-q1 + strict circuit, no residence       UNKNOWN  1801.43s
residence + upper-q1 cycle cover,
  no one-cycle/voltage constraint             UNKNOWN  1805.12s
```

These are timeouts, not UNSAT results.  They show that the eager
upper-q1/degree-orientation conjunction is already the computationally hard
part; quotient connectivity alone does not explain the stall.

The `11` rank-five orbits give exactly `165` zero-degree physical Hall
targets.  The canonical core has quotient and physical matching size
`4778/4943`; two hundred different minimum equivariant one-cores cannot
change that `165` deficit, as the rank argument predicts.

An exact flow repair covers the `67` missing upper-q1 orbits with exactly
`67` changed lower-orbit choices, meeting the trivial hard lower bound.  The
stable choice-level scaffold is

```text
scratch/fixtures/k15_upper_q1_repair_scaffold_hint_v1.json.
```

It is not a carrier: only `283/429` quotient vertices have degree two after
the independent q1 repair.  It is nevertheless a useful CP-SAT choice hint.
Its degree histogram is

```text
0^3, 1^72, 2^283, 3^65, 4^5, 5^1.
```

There are `78` deficit and `78` surplus incidence units.  Replacing one
choice changes at most four endpoint incidences, so every degree-two selector
must differ from this scaffold in at least `156/4=39` choices.  Consequently
radius below `39` around the scaffold is rigorously infeasible, independently
of circuit connectivity and residence.

The q1 scaffold already supplies selected witness triples for eight of the
eleven seed-missing rank-five/q3 orbits.  The exact two-action extension

```text
5380 -> 5389
9314 -> 9299
```

supplies the remaining representatives `1349,1585,2329`.  Therefore

```text
scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json
```

is only `69` choices from the residence-perfect seed and simultaneously has
zero upper-q1 and zero lower-q3-positive misses at choice level.  It is not a
carrier yet; its exact degree-shortage count puts it at least `40` choices
from degree two.  This yields a sharper LNS schedule around the joint hint:
`R=48,64,96`.

The solver supports an exact large-neighborhood radius

```text
overlap(current,hint) >= 429-R
```

through `--max-choice-changes R`.  Relative to the resident seed, any
upper-q1-complete carrier needs `R>=67`; the first useful radii are `80`,
`120`, and `180`.

The exact radius implementation was checked with the `k=11` carrier on the
remote CPU host.  At radius zero it returned the identical 42-choice
selector in `0.186s` and passed residence, lower-q2, lower-q3-positive, and
all upper gates.  The normalized result is

```text
scratch/k11_graded_pipeline_radius0.remote.json.
```

## 6. Completion standard

A quotient selector is not a solution.  A valid `k=15` claim requires all of:

1. one physical strict-spiral carrier cycle of length `6435`;
2. residence, lower-q2, rank-five positive degree, and every upper shadow;
3. an equivariant one-core passing weighted quotient Hall;
4. an independent physical matching of all `4943` lower targets;
5. an upper-safe cut and three-letter prefix closure;
6. a direct word of length `6438` whose exhaustive verifier covers all
   `32767` nonempty masks and whose third derivative is the exact middle
   layer.

No current artifact satisfies this complete list.

## 7. Exact arithmetic scope of the one-core route

Put `h=r-d` and

```text
R0(k) = sum_{j=1}^h C(k,j).
```

In the graded subclass `DA=DP`, every derivative row above `A` has rank at
least `h+1`.  Hence all `R0(k)` targets of ranks at most `h` must occur as
literal source letters.  A length-`W+d` word therefore necessarily satisfies

```text
R0(k) <= W+d.                                            (7.1)
```

This is an arithmetic viability condition, not a Hall or existence theorem:
even when (7.1) holds, a fixed carrier/core may have zero-degree targets or a
larger deficient shore.  The cyclic-prefix implementation has only `W`
independently chosen letters (the final `d` repeat a prefix), so its matching
uses the slightly stronger capacity `R0(k)<=W`.

The exact first failures of the general linear inequality are

```text
k     d     h       W+d-R0
9     2     3          -1
14    2     5         -38
19    3     7       -1802
21    3     8      -49210.
```

At `k=15`, by contrast, `R0=4943` and `W+d=6438`, leaving scalar slack
`1495` (`1492` within the cyclic `W` positions).  Thus the graded one-core
route is fully viable for the present case, but it cannot be the all-`k`
proof.  The known optimal `k=9` and `k=14` words already demonstrate what a
general recursion must add: controlled deeper punches that let some low
targets occur in derivative rows while changing the otherwise frozen tower.
