# Independent audit: twisted three-run quotient `C6` dyadic pump

**Date:** 2026-08-02  
**Verdict:** `PASS` for the literal packet scope; the earlier blanket `C6`
no-go is corrected to its same-phase physical-triangle scope.

## 1. Independent reconstruction

The audit takes only `d` and a nonnegative slack.  It sets

\[
 h=d+1,qquad r=3h+1+s,qquad n=2r-1,
\]

constructs the three one-runs and three zero gaps, shifts the runs one at a
time, and checks `R_3=tau R_0`.  It then develops the quotient triangle
through all `n` phases.

The following are checked literally:

1. `3n` distinct rank-`r` owner occurrences;
2. Johnson adjacency at every edge, including the phase-advancing closure;
3. `3n` distinct rank-`(r-1)` intersections;
4. `3n` distinct rank-`(r+1)` unions;
5. exactly six trace changes for every coordinate;
6. minimum positive and zero cyclic run lengths at least `d+1`; and
7. equality of the complete physical lower/upper counters after reversal.

The voltage is not inferred from component total: the first two quotient
edges have gain zero and the closing lift ends at `tau R_0`, so its gain and
total are `+1`.  Reversal is `-1`.  The component formula then gives one
physical cycle because `gcd(n,1)=1`, for prime and composite odd `n` alike.

## 2. Replay

Run:

```text
python3 scratch/audit_k_twisted_three_run_c6_unit_pump_20260802.py
```

Frozen output:

```text
PASS_TWISTED_THREE_RUN_C6 cases= 64
formula n=6(d+1)+1+2*slack; voltage=+1 reverse=-1
last (16, 8, 119, 60, [50, 51])
```

The 64 cases are `1<=d<=16` crossed with slack `0,1,3,8`.  The last tuple
is `(d,slack,n,r,[minimum-zero-run,minimum-one-run])`.

A second implementation,
`scratch/audit_k_c6_three_run_unit_pump_independent_20260802.cpp`, was
written independently from the Python replay.  Its bit-vector construction
again checks `R_3=tau R_0`, all physical owner/lower/upper sets, and every
cyclic zero/one run for the same 64 cases.  Compiled with
`clang++ -std=c++20 -O3 -Wall -Wextra -pedantic`, it ends with

```text
d=16 slack=8 n=119 owners=357 lower=357 upper=357 min1=51 min0=50
PASS rotating-boundary C6 unit-pump independent audit
```

## 3. Scope correction and cap/history audit

The support-three orientation-flip no-go concerns a physical Johnson
triangle: the closing endpoint is the same physical root.  Here it is
`tau R_0`; the development is a `3n`-cycle.  Thus the positive result does
not contradict the common-neighbour dichotomy.

Forward and reverse use the same undirected physical edges, so their lower
and upper occurrences agree one-for-one.  Removing one physical edge and
its opposite removes the same lower/upper occurrence.  The remaining paths
have no short internal run; all cut runs are endpoint-clipped.  Hence the
branch tuple contains one cap-exact atomic exchange, one literal pair of
endpoint histories, one oriented private edge, and voltage `+1` (or the
fully reversed `-1` tuple).  No field is mixed across branches.

The audit does not supply an ambient factor reservation or prove that a
later fixed-`z` ticket's exterior history domain contains this endpoint
tuple.  Nor does it test source rows, deeper upper shadows, exterior
cross-windows, or compiler matching.
