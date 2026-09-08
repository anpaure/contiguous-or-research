# Audited fifth-edge orbit census for `k=11`

This census determines whether extending the explicit canonical-prefix split
past the 60 fourth-edge branches is worthwhile.

For every certified prefix `C,E,F,G,H,I`, the checker enumerates all thirty
Johnson neighbours `J` of `I`, rejects repeated vertices and lower colours,
checks every completed coordinate run in `E,F,G,H,I,J`, and groups survivors
by removal/addition membership signatures under all six fixed masks.

The exact aggregate result is

```text
legal labelled fifth transitions: 896
residual stabilizer orbits:        464
```

Among the 60 prefixes, 56 have fifteen labelled continuations and four have
fourteen.  The orbit-count distribution is

| fifth orbits in a prefix | number of prefixes |
|---:|---:|
|3|3|
|5|1|
|6|21|
|8|18|
|9|7|
|10|3|
|12|6|
|15|1|

The weighted total is 464.  Thus a fifth split is exact and nearly halves the
remaining labelled prefix space, but would expand the portfolio from 60 to
464 explicit jobs.  It has not been added to `recombine_paths_sat.cpp` because
the global exact flag-moment cuts offer a better propagation-to-portfolio-cost
tradeoff.  The independently reproducible census remains in

```text
scratch/verify_k11_third_orbits.cpp
```

and is reported by

```text
fifth_summary raw=896 orbits=464.
```

No existence claim or branch exclusion relies on this unimplemented census.
