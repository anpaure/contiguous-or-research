# Thread D: executable validation of the phase-free joint rail model

Date: 2026-07-30

Status: theorem/code cross-audit passed in the normalized one-block, unit-voltage
class.  Fresh `K=8` and `K=10` witnesses pass the exact q1, ownership,
Hamiltonicity, and positive-residence gates.  At `K=16` only the complete
model was built and sized; no `K=16` SAT, UNSAT, compiler, or word claim is
made.

## 1. Exact scope

Let `K=2R`, `n=K-1`, and

\[
 M=\binom nR/n=C_{R-1},\qquad N=2M,\qquad W=nN=\binom K R.
\]

The executable model in
`scratch/threadD_solve_joint_rail_phase_history_cegar_20260730.py` is sound
and complete for the following normalized class:

1. the carrier is `Z_n`-equivariant and uses every free A- and B-shore
   owner orbit once;
2. its quotient is one directed Hamilton cycle with exactly one A-to-B and
   one B-to-A transition, hence one contiguous block on each shore;
3. the quotient voltage is exactly `1 mod n`;
4. every old-coordinate positive run has length at least `d+1`, where `d`
   is the carrier depth;
5. all four lower/upper q1 target-orbit palettes are covered.

A physical equivariant Hamilton carrier can have any unit voltage.  The
usual coordinate-multiplier relabelling changes that unit to one and
preserves Johnson adjacency, residence, and target coverage.  Thus the
theorem is an iff **up to this relabelling**.  With fixed literal coordinate
labels, the executable searches only voltage one.  Likewise, one block per
shore is a genuine restriction, not a without-loss-of-generality claim.

The top coordinate needs no extra history: exactly two cross-shore edges
make its positive runs the A-blocks, each of length `M`; the constructor
checks `M>=d+1`.

## 2. The theorem and the encoding agree

The cross-audit of
`MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md`
against the executable gives the following exact correspondence.

- Every selectable Boolean is one literal option
  `(u,v;deleted,inserted,delta)`.  If the source is in phase `g`, the target
  is in phase `g+delta`; therefore accumulating selected deltas reconstructs
  all phases and no absolute phase variable is needed.
- Options with identical ordered endpoints are tied to one pair-arc Boolean.
  `AddCircuit` on the nonloop pair arcs forces one spanning directed quotient
  cycle, while the equality for each pair chooses exactly one literal option
  on every selected pair arc.  Omitting same-owner options is sound for a
  Hamilton cycle on `N>1` owners.
- The two cross-shore equalities impose one A-to-B and one B-to-A arc.
  Together with the single circuit, this is equivalent to one A block and
  one B block.
- `AddModuloEquality` plus `voltage==1` is exactly the normalized lift
  condition.  Decoding accumulates the option deltas, checks final voltage
  one, and verifies the last base state is Johnson-adjacent to the once-rotated
  first state.  The `n` revolutions then visit all `W` middle owners exactly
  once because both shore actions are free.
- At each owner the `d` history integers store the preceding insertion
  labels in that owner's frame.  The selected delta shifts each value by
  `-delta`, fixes the sentinel, and shifts the history queue.  A non-sentinel
  deletion is forbidden from equalling any of the `d` stored values.  This
  is exactly the directed forbidden-window condition: a deleted coordinate
  equals an insertion among the preceding `d` transitions iff its ending
  positive run has length at most `d`.
- Every q1 row is a Boolean OR over all transition options carrying its
  canonical palette label.  These are at-least-one coverage rows; duplicate
  witnesses are allowed.  Lifting one provider through all rotations covers
  its whole physical target orbit, including nonfree target orbits.

Conversely, canonicalizing any carrier in this class determines one selected
option at each quotient transition and the actual last-`d` insertion queue
satisfies every table row.  This proves completeness within the stated
class.  There is no hidden path-first gauge assumption.

## 3. Exact `K=16` size ledger

For `K=16`, `R=8`, `n=15`, `M=429`, `N=858`, and `d=3`.  The raw option
formula gives `2MR^2=54,912`; deleting the 56 same-owner internal options
leaves exactly `54,856` selectable options.  The four q1 palettes contain

\[
 335+429+429+335=1,528
\]

orbit rows, and the semantic insertion history has `Nd=2,574` domain-16
integers.

Writing `E` for selectable options, `P` for ordered-pair arcs, and `Q` for
q1 rows, the Thread-D implementation
`scratch/threadD_solve_joint_rail_phase_history_cegar_20260730.py` has
exactly

\[
 V=E+P+4N+2Nd+1,\qquad C=P+5+4N+3Nd+Q.
\]

Thus the exported `K=16` CP model has exactly 116,921 variables:

\[
54,856\ \text{options}+53,484\ \text{pair arcs}
+4N\ \text{selected attributes}+1\ \text{voltage}
+Nd\ \text{histories}+Nd\ \text{successor histories}.
\]

Its 66,171 constraints decompose as

\[
53,484+1+2+4N+2+3Nd+1,528=66,171,
\]

corresponding respectively to pair selection, one circuit, two crossing
counts, four selected-attribute equations per owner, voltage, the three
history/table families, and q1 coverage.  This exact ledger confirms that
the implementation has not reintroduced absolute phase variables.

The authoritative theorem now also records separate compact CP-SAT and
DIMACS implementations.  Their proto-variable/constraint counts differ
because they reify the same history recurrence and connectivity in different
ways.  The common semantic counts are `54,856` selectable options, `2,574`
history values, and `1,528` q1 rows; the `116,921/66,171` ledger here belongs
only to the named Thread-D executable and is not asserted for those other
encodings.

The build-only H100 run used Python 3.12.3 and OR-Tools 9.15.6755.  It took
14.97 seconds and 587,896 KiB peak RSS under a 1,536 MiB solver setting and
a 2 GiB OS limit.  It produced no solve round.
The exported model digest recorded by the build is
`e23ef2157635ccc94ae643aeac0d2c963ae51444c4c429712e78086e255fe6de`.
The exported pbtxt has 117,352,547 bytes and remains remote.  A separate
read-only SSH `sha256sum`/`stat` recheck reproduced that size and digest; the
local replay pins those values but does not pretend to have rehashed a local
copy of the large file.

## 4. Small-instance executable validation

Both solves used one H100 CPU worker and `--carrier-only`; each returned an
explicit decoded quotient tour and physical-cycle digest.

The solver-free replay
`scratch/audit_threadD_joint_rail_phasefree_results_20260730.py` rebuilds the
option catalogue, replays each selected literal transition, reconstructs the
unit-voltage physical cycle, checks ownership/connectivity/shore blocks and
positive runs, and applies literal q1, lower-q2, and all-width upper oracles.
It does not invoke OR-Tools or trust the producer's PASS field.

| instance | status | vars / constraints | solve wall | peak RSS | exact replay |
|---|---:|---:|---:|---:|---|
| `K=8` | `PASS_Q1_RESIDENT_HAMILTON_CARRIER` | 303 / 195 | 0.159 s | 105,420 KiB | 70 distinct middle owners; minimum positive run 3; no q1, lower-q2, or arbitrary-upper defect |
| `K=10` | `PASS_Q1_RESIDENT_HAMILTON_CARRIER` | 1,375 / 803 | 2.896 s | 130,308 KiB | 252 distinct middle owners; minimum positive run 3; all four q1 orbit palettes complete |

The witness files are `scratch/k8_phasefree_solve.json` and
`scratch/k10_phasefree_solve.json`.  Their selected-option / reconstructed
physical-cycle digests are respectively

```text
K8   99150c877f067996386e5daaf5972ad3fa11101f3c6bf1243f404cfd235aeae1
     892cc2ea65fa60ba226f198a6f8f3da9afedc19dc8a55316c3015764d85cceb9
K10  ed9eb660d826e4944dc4e216b46c0ff44f199394ba3562483e21308841c589ab
     24da6a22b6cabc52098322352794f41ca9f500800fdb419a75f7058aa47ddf07
```

The `K=10` witness is deliberately **not** compiler-ready.  Direct cyclic
replay finds the three lower-q2 holes

```text
73, 146, 292
```

and nine arbitrary-upper holes, all at rank seven,

```text
687, 701, 757, 855, 862, 890, 939, 981, 1002.
```

This is consistent with `--carrier-only`: the proved/modelled iff is the
q1-plus-residence carrier gate, not the deeper-shadow or compiler gate.
The deeper candidate no-goods in non-carrier mode are exact full-tour
no-goods, hence sound but not a complete generalized separator.

## 5. Frozen provenance and conclusion

The three result payload digests replay exactly after removing their
`payload_sha256` fields:

```text
K8   d4b175ff86619e9c565fffe5db2b15d67849f7e52f5142dc9635e249eb42c8fc
K10  15912e37402a56244bc6f07aeae74c0bcee4b635687dba8f2ddc96c15711d5f3
K16  0a732d1c48b243ff7035d94f096e1eb7d4d3c91ceea945ad7d31e0987c0e7295
```

Source/artifact file digests are:

```text
theorem       4542b5d1cd31d027e5bfcd1ae7d5d5fc3cc47c45a3155f3535c38f992431b002
solver        676694ea74fa8f52a141cf5a0c20ecac103a1f6a58595ce8334ccc7d14334c21
catalogue     7aad8237fc13723d53b0835be8af7bc8684573f92845a41e8a7c9044411f3f4f
K8 result     5bc4d118085da9efc3c6b74ad4efd4ef1f342581a1e943fb63db91d44fad605f
K10 result    10b6c4a98b49b42f951441d7af17df2cc3f69c5c2b2f4ced155d758ca3fc22a9
K16 build     7bcd08396b8682a6116723b3d24ad8a114ca500e80c7963bddf607e4275b2bf8
replay source bcde3e80b19f063d90f7c09edda41d858bbca834d9c439e3a4468219d5cd1c06
replay audit  aa7edc921873f4c176499991e285a5cc7f1406daef4dc3c033f58b1e86a3c694
```

The replay-audit payload digest is
`cd7c6c3180e8996aff510b8ca20c5314fcb376e4c4c21b89cefbf201d48b046c`;
its status is `PASS_INDEPENDENT_PHASEFREE_REPLAY_AND_K16_BUILD_AUDIT`.

Accordingly, the phase-free normal form and its executable realization are
validated for their precise normalized class.  Nothing here establishes
existence at `K=16`, settles carriers with more shore blocks, supplies deeper
shadows, runs `COMP_3`, or constructs a universal word.
