# Exact audit of the composite-odd sigma quotient

Date: 2026-07-29

Status: proof, fail-closed source hardening, solver-free physical-orbit
regressions, and a fresh remote `k=9` calibration.  This note does **not**
claim a `k=15` carrier or word.

## 1. Verdict

Removing the prime guard from `scratch/sigma_sat_solver.py` is mathematically
sound for the central factor master at every odd `k`, provided three different
uses of orbit size are kept separate:

1. ranks `m` and `m+1` are free, so quotient edge degrees are ordinary
   weighted graph degrees (a loop counts twice);
2. shadow coverage is Boolean orbit coverage and remains exact even when the
   shadow orbit is short; and
3. a connected quotient cycle is one physical cycle only when its voltage is
   **coprime** to `k`, not merely nonzero.

The audit found and fixed two composite-specific acceptance hazards:

- the driver still accepted every nonzero voltage, which is false at
  `k=15`; and
- quotient `cap2` was reported as an upper physical load cap although a
  selected free edge orbit contributes load `k/s` to a target orbit of size
  `s`.  The code now fails closed and requires `--no-cap2` whenever the
  upper-q1 layer has a short orbit.

It also restores quotient loops to the build-only disconnected factor master
and independently validates the new grouped-neighbour lower-q2 compression.
Loops are legitimate weighted-degree-two components.  Explicit connectivity
modes forbid them immediately; the default lazy mode removes them by ordinary
component cuts.

The exact source/test artifacts are:

- `scratch/sigma_sat_solver.py`;
- `scratch/test_sigma_composite_quotient_soundness.py`; and
- `scratch/k13_q2_witness_portfolio.py` (grouped-turn consumer); and
- `scratch/k9_composite_quotient_audit_20260729.certificate.json`; and
- `scratch/k9_composite_quotient_factor_audit_20260729.certificate.json`.

## 2. Central freeness and exact weighted degree

Write `k=2m+1`.  If a nonidentity rotation fixes a set, the cycles of the
generated subgroup all have some common length `t>1` dividing `k`; a fixed set
is a union of those cycles, so `t` divides its cardinality.  But

\[
 \gcd(k,m)=\gcd(k,m+1)=1.
\]

Thus rotation is free on both central ranks.  At `k=15`, ranks seven and eight
have exactly

\[
 {1\over15}\binom{15}{7}={1\over15}\binom{15}{8}=429
\]

orbits, all of size 15.

A primary choice consists of a rank-seven lower colour `X` and two added
coordinates `{a,b}`.  Its physical translation orbit has 15 distinct edges,
because a stabilizer of the edge would stabilize its intersection `X`.  At a
quotient middle vertex it contributes one incidence at each endpoint; if the
two endpoints lie in the same orbit, it contributes two incidences there.
The CNF's repeated loop literal in the cardinality counter is therefore the
correct weighted coefficient.

Exactly one choice at each of 429 lower orbits selects 429 edge orbits, hence
858 quotient incidence units.  There are 429 middle vertices, each constrained
to degree at most two.  Equality of total demand and total capacity forces
degree exactly two at every middle orbit.  Central freeness then lifts this to
degree exactly two at every physical rank-eight vertex.

This proves both positive soundness and completeness of the factor core for
equivariant lower-q1-rainbow 2-factors.

## 3. Quotient loops

There are 14 loop choices at `k=15`.  Direct physical expansion gives the
following histogram by the loop voltage `v`:

```text
gcd(v,15) = 1 : 4 loops
gcd(v,15) = 3 : 4 loops
gcd(v,15) = 5 : 6 loops
```

Every such choice gives all 15 vertices of its central orbit physical degree
two.  Its lift consists of exactly `gcd(v,15)` cycles.  It is therefore a
valid component of a physical 2-factor, although it cannot belong to a
connected quotient factor with more than one quotient vertex.

The old unconditional `-loop` clauses made the advertised disconnected
factor CNF incomplete.  They are now present only when a direct/compact/
oriented connectivity encoding is requested.  In the default iterative
driver a selected loop appears as a singleton quotient component and is
eliminated by the usual lazy component cut.

## 4. Short upper-q1 orbits and why `--no-cap2` is sufficient

Rank nine at `k=15` has orbit profile

```text
333 orbits of size 15
  2 orbits of size  5
```

Each short orbit has 12 primary quotient choices pointing to it.  A selected
choice always represents 15 physical edges.  If its upper target orbit has
size `s`, those 15 occurrences are distributed uniformly, so every physical
target has multiplicity

\[
 {15\over s}.
\]

For a short rank-nine orbit this is three.  Consequently:

- the clause “at least one selected choice points to this representative” is
  exactly equivalent to covering every physical member of the orbit;
- no orbit-size weight is needed for zero/nonzero coverage; but
- unweighted quotient `at_most_2` is not physical load at most two.  In fact,
  covering a size-five orbit already forces physical load at least three.

Thus `--no-cap2` is sufficient for the exact upper-q1 **coverage** master and
is necessary at `k=15` if full coverage is requested.  The constructor now
rejects the misleading cap mode rather than silently accepting a physical
cap violation.

The same distinction applies to hole budgets: the existing option explicitly
counts missing quotient orbits.  It must not be read as missing physical mass
unless orbit sizes are applied afterwards.

## 5. Lower-q2 witnesses with short target orbits

Rank six has the same profile, `333 x 15 + 2 x 5`.  At a canonical middle
vertex `V`, the 56 possible choice incidences collapse to its eight literal
lower neighbours `V-{a}`.  All primary alternatives in one such group belong
to the same quotient lower orbit, so the exactly-one lower constraint makes
at most one of them selected.  Introduce the exact group bit

```text
e(V,a) <=> OR{primary incidences aligned with V-{a}}.
```

The exact weighted central degree is two.  A nonloop selected choice sets one
group bit at each endpoint; a selected quotient loop occurs in two different
groups at its sole quotient endpoint.  Hence exactly two distinct group bits
are true at every selected middle vertex.  For every pair define

```text
turn(V,a,b) <=> e(V,a) AND e(V,b).
```

Exactly one turn is true, and its physical lower-q2 colour is

\[
 (V-\{a\})\cap(V-\{b\})=V-\{a,b\}.
\]

The compressed CNF puts each turn literal into the clause for the canonical
orbit of this mask.  It is therefore equivalent to the expanded
pair-of-choice encoding on every feasible core assignment, including loops,
but needs only `429*C(8,2)=12,012` turn witnesses rather than 588,486 primary
pair witnesses.

With upper-q1 and lower-q2 coverage enabled, the resulting `k=15` factor CNF
has 36,465 variables and 243,913 clauses (3.9 MB), down from 670,511 variables
and about 2.07 million clauses in the expanded encoding.

For every turn witness, physical expansion produces all distinct
rotations of its target.  A target in a size-five orbit occurs three times at
each physical mask; a free target occurs once.  The two short target orbits
each have 12 exact turn witnesses.  Multiplicity is irrelevant to their
existential coverage clauses, so the lower-q2 encoding is sound despite the
short orbits.

Conversely, in a selected degree-two factor the two incident physical edges
at any middle vertex correspond to exactly one enumerated quotient incidence
pair (or the two sides of a loop).  Hence every genuine lower-q2 occurrence is
represented by a clause witness.  The encoding is complete for orbit
coverage, not merely positive-sound.

## 6. Composite voltage correction

Let a connected quotient cycle have net voltage `v`.  After one quotient lap,
the phase changes by `v`; translation by `v` on `Z_k` has `gcd(v,k)` orbits.
Therefore the physical lift has

\[
 \gcd(v,k)
\]

cycles and is one Hamilton cycle exactly when `gcd(v,k)=1`.

The old code checked only `v != 0`, inherited from the prime-only version.
At `k=15`, voltages 3, 5, 6, 9, 10, and 12 would therefore have been falsely
accepted; the old lift routine also emitted a length-6435 list containing
repeated physical vertices.  Both the lift routine and the iterative driver
now fail closed on every non-coprime voltage, and the verifier reports the
physical lift cycle count.

This correction is about a single Hamilton lift.  A non-coprime quotient
cycle still lifts to a perfectly valid disconnected 2-factor.

## 7. Fresh composite `k=9` calibration

The patched source was copied to the H100 host and run on CPU only:

```sh
KISSAT=/dev/shm/k15_sat/kissat/build/kissat \
python3 sigma_sat_solver.py \
  --k 9 --no-cap2 --lower-q2 \
  --max-rounds 20 --time-per-round 10 --seed 2907 \
  --prefix k9_composite_audit
```

It took two SAT rounds (one lazy subtour round) and 0.082 seconds of
reported total solve time.  Independent local replay of the retained explicit
choices gives:

```text
quotient components             [14]
voltage                          4 mod 9
physical lift cycles             1
physical lift length           126
unique middle                  126 / 126
unique lower q1                126 / 126
unique upper q1                 84 / 84
unique lower q2                 84 / 84
upper orbit sizes                9 x 9, 1 x 3
physical upper loads             54 at 1, 18 at 2, 12 at 3
```

The last line is a direct calibration of the cap fix: the quotient load
histogram is `7 at 1, 2 at 2, 1 at 3`; moreover the covered short orbit has
physical load three even when its own quotient load is only one.  Coverage is
exact; quotient cap-two semantics would not have been.

Certificate SHA-256:

```text
2f4040031a442b3234d4e0b92ef5b157058a293eaf38425ef99a88a9a290bb3c
```

A second run with `--allow-disconnected-factor` accepted its first exact
factor in 0.039 seconds.  Physical replay gives four cycles of lengths
`72,18,27,9`, all 126 middle masks, all 84 upper-q1 masks, all 84 lower-q2
masks, and one selected quotient loop.  This directly calibrates the loop
and arbitrary-voltage factor-lift code rather than merely inspecting it.
Certificate SHA-256:

```text
d73f1ed34c20b6fec57def086c7f7d12b07c597832e547a27d0c7ee91944802f
```

## 8. Regression command and exact boundary

```sh
python3 -m unittest -v \
  scratch/test_sigma_composite_quotient_soundness.py
```

The eight tests run without a solver.  They expand all 12,012 primary edge
orbits for the degree/upper checks, reconstruct all 12,012 grouped lower-q2
turn witnesses from physical incidences, verify both short target
multiplicities, audit all 14 loops, exercise the coprime-voltage guard, and
replay both retained connected/disconnected `k=9` certificates.  Runtime on
the local audit host is under one second.

The grouped representation initially invalidated two optional one-change
diagnostics which inverted an AND literal as though it contained primary
choice variables.  Both `--hint-q2-near-side lower` in the main driver and
`scratch/k13_q2_witness_portfolio.py --side lower` now expand only the
requested turn groups back to primary pairs.  A solver-free `k=13` replay at
target 405 finds 1,008 primary witness pairs and 92 compatible one-change
routes; a build-only hinted CNF reports the same 92 without error.

Proved/verified here:

- composite central factor degrees and loop weights;
- exact upper-q1 and lower-q2 orbit coverage at short targets;
- `--no-cap2` as the correct full-coverage mode;
- coprime voltage as the exact one-cycle criterion; and
- positive end-to-end composite `k=9` calibration.

Not proved here:

- loop-free connectedness, residence, a safe cut, Hall compilation, or a
  length-6438 word at `k=15`; and
- physical-load semantics for any future weighted shadow objective unless it
  explicitly uses actual orbit sizes.

Subsequent to this implementation audit,
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`
proved analytically that the full loop-allowing coverage-only `k=15` master
is satisfiable, and in fact supplied complete correct-window support at every
depth.  That PBBS point uses two quotient loops and is disconnected and
nonresident, so it does not settle any of the remaining joint conditions
listed above.

## 9. Exact overlap with Claude's new single-trace c-space normal form

The 13:05 snapshot of Claude's `LEDGER.md`/`cword.py` has SHA-256

```text
LEDGER.md  a548ed88f5249296a3a7e46483951cb76f9a33c7b93ce874c8bbc54d46282a84
cword.py   006fe8ef2600491518b82a075a5d9c27e751f73b0bc30af1c0c1dd611256b452
```

Its central single-trace theorem is mathematically compatible with this
factor master.  If a connected equivariant physical Hamilton cycle has unit
voltage (after multiplying coordinate labels by the inverse voltage), the
coordinate-zero trace `c` determines it by

\[
 T_i=\{t:c_{i-tN}=1\},\qquad W=kN.
\]

Class sum `r` gives the middle rank.  Exactly one run start and one run end in
every residue class modulo `N` gives one insertion and one deletion at every
seam, hence a Johnson step.  Pairwise rotation-inequivalent columns give all
central orbits.  Requiring every lower-q1 orbit then maps the trace bijectively
to a connected, oriented, coprime-voltage, loop-free solution of the sigma
factor core: its lower colour is `T_i intersect T_(i+1)` and its selected
upper colour is `T_i union T_(i+1)`.  Triple intersections are exactly the
same lower-q2 gate in both models.

Conversely, orienting any connected coprime-voltage sigma solution and gauging
its voltage to one produces this single trace.  Therefore c-space is not a
different factor theorem; it is an exact coordinate chart on the connected
coprime-voltage stratum of the sigma master.  It intentionally excludes
disconnected factors and quotient loops, which need multiple traces or a
later splice.

The composite short-orbit semantics are sound in `cword.py`: it enumerates
distinct canonical representatives and asks only for Boolean coverage.  Its
physical audit expands the whole trace.  Repeating `ph=0,...,k-1` creates
duplicate selectors on a short orbit but neither loses a target nor creates a
false witness.  It does not impose the invalid quotient cap-two constraint.

Three scope qualifications should remain explicit:

1. “voltage is pure gauge” requires `gcd(v,k)=1`.  The current
   `extract_cw` docstring says “ANY voltage” and does not validate this, which
   is false for nonunit composite voltage.  This cannot create a false final
   PASS because the reconstructed trace is audited independently, but it can
   misdescribe or badly seed a disconnected input.
2. `SEL_CAP=150`, radius filtering, and the short width list for upper-cover
   selectors make an UNSAT/failed CEGAR lane incomplete.  The source already
   acknowledges the selector cap.  Every reported positive selector remains
   sound, and final `audit` checks unrestricted physical coverage.
3. Start/end transversality gives Johnson rank, not q1 rainbow by itself.
   Middle-orbit and q1-orbit uniqueness remain the lazy collision/coverage
   gates exactly as the implementation states.

No composite-`k=15` short-orbit flaw was found in the c-space coverage logic.
The useful new relation is that the compact 36,465-variable factor CNF can
search all equivariant q1-rainbow 2-factors (including spliceable components),
whereas c-space searches the already connected voltage-one subfamily while
making residence a simple run constraint.
