# Audit of the `k=11` fourth-edge orbit split

## Verdict

The 60 fourth-edge representatives in `K11_FOURTH_EDGE_ORBITS.md` are an
exhaustive and irredundant residual-symmetry split under the stated canonical,
ordered, complete-graph, delay-three fixed-row assumptions.

The checker

```text
scratch/verify_k11_third_orbits.cpp
```

independently derives them as follows for every one of the fifteen certified
three-edge prefixes:

1. enumerate all thirty Johnson neighbours of `H`;
2. reject a repeated central vertex;
3. reject every edge whose rank-five intersection repeats one of the first
   three lower colours;
4. scan all eleven length-five prefix incidence words and reject every
   completed internal one-run shorter than four;
5. compute the five-mask coordinate signatures under `C,E,F,G,H`;
6. group legal transitions by the ordered removal/addition signature pair;
7. select the numerically least representative of each derived orbit; and
8. compare the entire derived set with a separately hard-coded copy of the
   source table.

Every prefix has exactly fifteen legal labelled fourth transitions.  The
derived orbit counts by second-edge block are

```text
q=0: 4+6+2+3                 = 15
q=1: 6+6+8+3+3+4             = 30
q=2: 2+3                     =  5
q=3: 3+3+4                   = 10
                                      --
                                      60
```

Compiling with

```text
g++ -O3 -std=c++20 scratch/verify_k11_third_orbits.cpp
```

and running the checker exits zero and ends with

```text
C0_moment crossing=11 endpoints=1 total=12
prefix_moment lower=55 crossing=9 endpoints=1 total=10
prefix_moment lower=115 crossing=10 endpoints=0 total=10
prefix_moment lower=611 crossing=10 endpoints=0 total=10
prefix_moment lower=1634 crossing=10 endpoints=0 total=10
PASS total_orbits=15
```

The historical final label refers to the fifteen third-edge prefixes; all 60
nested fourth-edge tables are checked before that line.
The four additional exact-10 lines independently exercise the prefix-moment
theorem on the first four lower colours of the reversed score-549 checkpoint.

## Source-scope audit

`RECOMBINE_FOURTH_ORBIT` is refused unless:

* `RECOMBINE_THIRD_ORBIT` and `RECOMBINE_SECOND_ORBIT` are both present;
* WLOG canonicalization is active;
* the graph is the complete Johnson graph;
* the encoding is ordered;
* `k=11`, `rank=6`; and
* `RECOMBINE_D=3` (or its default value three).
* the selected mode enforces coordinate-run factorability, either in the
  initial CNF or in its exact lazy refinement loop.

The selected edge and its direction are both forced.  Therefore a solver
cannot satisfy the branch using the representative edge elsewhere in the
path or in reverse orientation.

A stub initialization check confirmed that `allordbase` with a third-orbit
setting exits with guard code `9`, while `allordinc` accepts the nested
`q=t=u=0` branch and fixes the directed prefix masks

```text
63, 119, 126, 125, 221.
```
