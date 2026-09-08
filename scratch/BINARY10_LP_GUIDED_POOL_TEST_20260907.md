# Bounded LP-guided exact-cover test

No integral cover was found. The test below concerns a restricted candidate
pool, not nonexistence of a completion in the full catalogue.

## Chosen literal core and method

The input was regular-tournament matching index 7, last-label variant 1 from
the completed 24-phase screen. Its saved numerical primal is
`run-type6phases-jakiaL/matching-07-last-1.primal.json` under the remote parent
`/home/amodo/or-research-20260907-QiqXT3/` on h100. Input SHA256:

```
d55e892f13ff65693d5e28ffc6793236201989882ff855cd48cd70b46113acc6
```

The literal core has 26995 admissible nonfixed row-orbit columns. The residual
problem has 356 target orbits, including 256 tight orbits at ranks 4, 5, and 6.
All LPs require load exactly one on every tight orbit and at least one on every
other residual orbit. Each column covers 16 tight orbits, so every feasible
solution has total orbit mass 16 and physical row charge 32.

Starting with the input's 258 positive columns, eight LPs minimized independent
objectives `2 + 0.01 U_j`, with `U_j` uniform on `[-1,1]`. The numerical values
near 31.92 are these perturbed objectives, **not improved row charges**. Each LP
had a 30-second limit and one thread. All positive supports were united.

One integer model then selected sixteen columns from that pool, maintaining
all the original tight equalities and far-rank coverage constraints. It was
allowed sixteen workers and 900 seconds total. Hints were a compatible packing
only, not additional constraints. Any feasible result had to expand to 42
literal rows and independently cover all 1024 masks, with each tight target
covered exactly once.

## Recorded outcome

All eight LPs returned numerical optimality reports. Their supports plus the
baseline contained 999 distinct columns. This pool still had at least one
candidate for every required target orbit. Ten compatible rows supplied hints.

The integer solver reported `INFEASIBLE` for this restricted 999-column model
after 0.44224591 seconds. The complete run took 45.66257949685678 seconds and
exited normally. There was no literal integral witness. No conclusion about
the other 25996 catalogue columns follows from this result.

The durable run is `run-lppool-index7last1-jKz6XG/` under the remote parent above.
It contains the exact input/source identity, every randomized numerical
primal, `restricted_pool.json`, `integer_status.json`, and `output.log`.
All computation was explicitly run via `ssh h100`.

Reproduction sources:

- `binary10_lp_guided_pool_20260907.py` builds the literal catalogue, runs the
  bounded randomized LPs, saves the pool, and tests the restricted integer model.
- `binary10_durable_lp_pool_20260907.sh` records durable output and exit status.
- `binary10_verify_integral_rows_20260907.py` independently enumerates all
  target loads of any future proposed integral witness.

## A possible exact support reduction, not performed here

Given a pool `P`, maximize `sum_{j not in P} x_j` over the unchanged feasible
fractional-cover polytope. A positive optimum produces usable new columns.
An **exactly certified** zero optimum would prove that every omitted column
is forced zero in every fractional completion, justifying its removal before
integer search. Numerical near-zero output would not suffice. The randomized
support-union experiment above does not establish such a support-closure
certificate, and none is claimed here.
