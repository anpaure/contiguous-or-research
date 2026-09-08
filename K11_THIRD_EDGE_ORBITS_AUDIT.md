# Audit of the `k=11` third-edge orbit split

## Result

The split in `K11_THIRD_EDGE_ORBITS.md` is sound, complete, and irredundant
under its stated scope: canonical complete ordered `J(11,6)` search with
delay three and one of the four certified second-edge representatives fixed.

An independent finite checker is retained as

```text
scratch/verify_k11_third_orbits.cpp
```

It does not trust the prose classification.  For each second-edge case it:

1. enumerates all thirty Johnson transitions out of `G`;
2. deletes repeated vertices and repeated previous lower colours;
3. directly scans the four-vertex coordinate words for a forbidden completed
   internal run of length below four;
4. computes the coordinate membership signatures under `C,E,F,G`;
5. forms the exact orbit key `(signature(removed), signature(added))`; and
6. compares the resulting key set with the hard-coded representatives used
   by `recombine_paths_sat.cpp`.

Compiled with `g++ -O3 -std=c++20` and given the score-549 path as an
additional audit input, it prints

```text
q=0 legal_raw=20 stabilizer_orbits=4 reps=125 252 95 222
q=1 legal_raw=20 stabilizer_orbits=6 reps=245 252 500 215 222 470
q=2 legal_raw=20 stabilizer_orbits=2 reps=126 222
q=3 legal_raw=20 stabilizer_orbits=3 reps=222 246 470
C0_moment crossing=11 endpoints=1 total=12
PASS total_orbits=15
```

The raw counts sum to 80 legal labelled continuations; the residual
stabilizers reduce these exactly to 15 branches.
The last line before `PASS` also verifies the exact omitted-colour moment on
the current checkpoint, whose noncanonical endpoint `504` demonstrates why
one must not assume both endpoints contain `C0`.

## Source integration check

The modified `recombine_paths_sat.cpp` passed a C++20 syntax check against a
minimal CaDiCaL interface stub.  A lightweight initialization run of branch
`(q,t)=(0,0)` with both new exact cuts enabled printed

```text
canonical_second_orbit=0 second_mask=126
canonical_third_orbit=0 third_mask=125
ordered_connectivity=1 variables=59134
c0_flag_moment=12 support=156
vertices=462 real_edges=6930 variables=62812
```

The 156-literal support independently agrees with the flag-moment proof:
150 real edges cross the six rank-six supersets of `C0`, and six dummy edges
can mark endpoints there.

No SAT search was run locally; the initialization used a no-op solver stub
whose `solve()` immediately returned UNSAT after formula construction.
