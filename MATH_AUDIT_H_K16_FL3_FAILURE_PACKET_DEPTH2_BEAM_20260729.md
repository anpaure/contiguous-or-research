# Lane H: exact FL3 failure-packet depth-two beam

Date: 2026-07-29  
Status: theorem/code/plan/size package complete; no heavy local enumeration
and no H100 launch under the active headroom freeze.

## 1. Frozen endpoint and the three libraries

The input endpoint is

```text
scratch/k16_q1_endpoint_resume1_failedlit3_20260729.json
SHA-256 430fa828587fd793a908cb5c379be6c5686dc5bb473657fe2b5af10ca037481a.
```

It is a physical Johnson 2-factor with three components of lengths
`12084,773,13`, zero lower or upper q1 holes, and `2222` short runs.  Its
complete scoped failed-literal bank is

```text
scratch/k16_failedlit3_fullbank_20260729.audit.json
SHA-256 e292d250dbfca0331fb74b12d8cc7e69770ea101c8a9f9b890289e5d1db2bd94.
```

All `956` candidate variables were probed.  Exactly three have contradictory
zero and one branches.  They are current blue variables on the three edges

```text
v=23456: (52419,54467)
v=21759: (43339,47427)
v=23195: (51358,59422).
```

These are the three initial failure-specific packet libraries.  They are not
chosen by a proof-incidence ranking.

## 2. Exact beam definition

For a state `Q`, reconstruct its exact fixed-resident overlay constraints,
run deterministic unit propagation to the complete fixpoint, and probe every
variable occurring in an unhit two-live-variable short-motif row.  Let
`Phi(Q)` be the number of variables whose two assumptions both contradict.
For every such variable, use its actual current blue physical edge as a focus
edge.

For each focus edge and each radius `r=2,3,4`, enumerate every connected,
edge-simple alternating closed-trail switch with `r` deleted factor edges and
`r` added Johnson edges.  The alternating-trail recursion is complete for
this family: orient the distinguished deleted edge in either direction,
enumerate each new-Johnson/old-factor pair, and close by the final new edge.
Incidence balance preserves degree two.  Simple `C4,C6,C8` switches are
included; repeated-vertex closed trails are also permitted.  Disconnected
packet unions and packets missing every current failure edge are outside the
library.

Every candidate must retain every lower and every upper q1 colour.  This is
a hard, independently replayed zero-hole condition, not an objective.
Colour multiplicities may change.

At depth one, retain **every** live neutral-or-improving state

```text
Phi <= 3.
```

No topology or component condition enters retention or ordering.  The
reported Pareto coordinates are only `(Phi,residence)`.  Expand every
retained state once, using the newly recomputed current double-failure edges.
The exact target is `Phi=0`.  A zero result would close this detector only;
it would not prove the full overlay feasible.

The driver is

```text
scratch/search_k16_fl3_depth2_failure_packet_beam_20260729.py
SHA-256 92c9ce716cabbc5344966c8d5c2f570c468b86d9da37cf7a7441fb3a9aef716a.
```

The locally replayed, enumeration-free plan is

```text
scratch/k16_fl3_depth2_failure_packet_beam_20260729.plan.json
SHA-256 23ad61d1b921950e13048cd0b54b25e91499a0017490dc06c22e03f461a06551.
```

It binds the FL3 endpoint, fullbank, resident selection and all resident
reconstruction inputs, edge catalogue, direct helper code, exact three
failed-variable identities, deterministic branch-core digest, and the three
named failure edges.  A full run recomputes all of those before expansion.

## 3. Enumeration-free size audit

The Johnson degree on rank-eight masks is `8*8=64`.  After choosing one of
two orientations of a distinguished deleted edge, every remaining
alternating pair has at most `64` choices for the new Johnson edge and two
choices for the following old factor edge.  Hence the terminal-walk upper
bound per focus edge is

```text
r=2:       2*128       =       256
r=3:       2*128^2     =    32,768
r=4:       2*128^3     = 4,194,304.
```

With three initial focus edges, the per-parent upper bound is therefore

```text
12,681,984 terminal walks.
```

This deliberately precedes final Johnson closure, q1 filtering and
deduplication.  If `N1` neutral-or-improving first states survive, the same
crude depth-two bound is `N1*12,681,984`.  A materialized 12,870-edge factor
has a deterministic conservative allowance of `3,313,696` bytes (tuple and
integer objects, 64 bytes of hash slack per edge, and one MiB fixed
overhead), but intermediate trail states and constraint systems can dominate
it.

The audit used no packet enumeration:

```text
scratch/audit_k16_fl3_depth2_beam_static_size_20260729.py
SHA-256 613f3ed32e90777df8cadb0a2010f97d2512d862ce49960bd365c38df137c81e
scratch/k16_fl3_depth2_failure_packet_beam_20260729.size.json
SHA-256 cd2723b79d04cb902bde4e9736be82c4f698521297ede7c7298c8720cb9469bb.
```

## 4. H100-only capped package

The self-contained package is

```text
scratch/k16_fl3_depth2_beam_h100_package_20260729/
```

Its manifest is

```text
SHA256SUMS
SHA-256 fb2f11d51b6e7d8c104a30f1c4b2fcd61bb361374b78490cf5170542e0ae1846,
```

and every listed file passes `shasum -a 256 -c SHA256SUMS`.

The launcher has four independent safety barriers:

1. host short name must be `arboghast`;
2. `H100_HEADROOM_CONFIRMED=YES` must be explicitly supplied;
3. scoring is single-process (`--workers 1`), with GPU visibility empty; and
4. `RLIMIT_AS=24 GiB`, CPU time six hours, and core dumps disabled.

Because scoring is single-process, the address-space limit is a job-level
hard cap rather than a per-worker cap multiplied over a process pool.  The
cap is a fail-safe, not a completion guarantee.  The package README preserves
the transfer and launch commands, but none was executed.

## 5. Proved/unknown boundary

Proved: the exact FL3 input, the three failure-specific focus edges, the
connected radius-2/3/4 library definition, hard q1 preservation, neutral
first-layer retention, detector-zero success rule, static size bound, and
capped H100 package.

Unknown: whether any permitted one- or two-packet composition has `Phi=0`.
A negative completed run would exclude only this adaptive connected-packet
beam.  It would not exclude a first step with `Phi>3`, a disconnected packet,
a radius above four, or a packet avoiding all current double-failure edges.
