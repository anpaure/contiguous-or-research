# Audit of Claude's even-\(K\) runtime report

Snapshot: 2026-07-29 17:14--17:17 UTC.  Sources inspected directly in
`/Users/amir.nuriyev/Downloads/opusproblem/work` and on H100 host
`arboghast`; no solver was launched by this audit.

## 1. `tworail16` is not the lead lane and is not near a verdict

No `tworail16.py` process exists in the live H100 process table.  Its stale
log ends after q2 construction:

```text
/home/amodo/or15/work/tworail16.log
[tworail16] base built
  channeling (halved): 368082 x-vars (225s)
  q1 rows (1269s)
  q2 rows (3439436 sels, 318s)
```

There is no upper-row completion and no `SOLVE` line.  Claude's newest ledger
corrects the old status at lines 271--287: the suspended CP models are
"gone/killed -- superseded."

The active h=1 successor is instead

```text
PID 3780256: python3 cnf16.py 16 /dev/shm/ck16h1 --tfix t_h1_858.txt
```

At the snapshot it was still **emitting**, not solving.  Its log stopped at

```text
base: 2,410,458 clauses
mid: 179,090,676 clauses
q1: 316,508,720 clauses
q2: 508,893,448 clauses
```

and `/dev/shm/ck16h1.cnf.body.gz` grew from 3,775,624,617 to
3,794,859,174 bytes in five seconds while the Python emitter used one CPU.
No final DIMACS, map, Kissat process, SAT/UNSAT result, or verdict exists.

The actual live K16 solver lanes at this snapshot were the compact
canonical-ID CP-SAT process and the exact Waksman Kissat process, neither of
which belongs to the old `tworail16` claim.

## 2. `bre_k13` is genuinely live, but has no verdict

This part of the report is correct:

```text
PID 3757121
python3 breager.py 13 --workers 6 --rtimeout 28800 --prefix bre_k13
RSS about 55--58 GB; CPU about 544%; elapsed about 65 minutes
```

Its authoritative log is
`/home/amodo/or15/work/bre_k13b.log`:

```text
[breager k'=13] W=1716 N=132 r=7 runs/gaps >= 3
  mid channeling: 132x132 (8s)
  q1 channeling: 132x132 (12s)
  all-depth rows: 499 (854700 sels, 56s)
  solving...
```

There is no PASS, UNSAT, or output artifact yet.

## 3. The supposedly suspended jobs are gone

There is no live or stopped `be_k16b`, `bre_k15`, or `tworail16` process.
Only stale construction logs remain:

```text
be_k16b.log: channeling + q1 rows only
bre_k15.log: mid channeling + q1 channeling only
tworail16.log: base + q1 + q2 only
```

Python CP-SAT model state is not serialized in those logs, so these cannot be
"resumed instantly"; they would have to rebuild.  Claude's current
`LEDGER.md`, lines 271--287, now states the same correction.

## 4. The K8 and K10 equivariant constructions are real

This is the strongest correct part of the report.

The retained exact one-shot log
`/home/amodo/or15/work/be_k10.log` records

```text
SOLVE: OPTIMAL (534.1s)
audit: ham=0 jv=0 rv=0 miss=0 (mA=0 mB=0 q1=0 up=0)
CARRIER_PASS_CYCLIC
```

and `beloop_k8.log` records a compiling carrier at iteration 4.  Independent
literal enumeration during this audit gave

```text
k8_equivariant.word:  length 72,  255/255 nonempty ORs, PASS
k10_equivariant.word: length 254, 1023/1023 nonempty ORs, PASS
```

Thus the existence of equivariant optimal words at K8 and K10 is verified.
Calling them the "first" such constructions is a novelty claim about this
project, not a literature theorem checked here.

The broader statement that eager channeling has replaced lazy CEGAR is an
engineering conclusion, not a solved K16 result.  `bieager.py` did close K8
and K10 exactly; K12/K16 did not finish in that model.  The separate repaired
lazy engine's audit explicitly says it "does not claim a k10, k12, or k16
carrier" (`BIWORD_ENGINE_AUDIT_20260729.md`, lines 9--29).

## 5. Dual rail is validated only at its internal master gate

`/home/amodo/or15/work/dr_k10.log` genuinely records

```text
MASTER PASS: Hamilton path, residence clean
```

and `dr_k10_T.json` exists.  But this is not an end-to-end validation:
Claude's latest `LEDGER.md`, lines 320--334, records 16 missing
rank-7 `{z}` upper targets and a subsequent sandwich UNSAT.  This is why
`breager.py` was strengthened to all-depth double shadows.

The code confirms the limited scope.  `dualrail.py`, lines 76--104, audits
only the full middle layer, Johnson path, two q1 palettes, and residence at
output; it does not audit deeper upper shadows.  Therefore "dual-rail master
validated" is true, while "even pipeline validated end-to-end" is false.

The claimed 51-second theorem excluding an all-depth bi-resident single
spiral at k'=9 is stated in `LEDGER.md`, lines 329--333, but no corresponding
UNSAT log/proof artifact was found.  The retained `bre_k9_PASS.json` is the
earlier weaker factor that fails the newly discovered all-depth gate.  Treat
the census theorem as uncorroborated until its exact artifact is restored.

## 6. The braided-complement CSP does not exist, and the lane is refuted

`braidrecipe.py` is only a seam-density probe.  Its own docstring, lines
25--29, labels the file "Phase 1" and says a small CP model would be a future
step; the file imports no solver and builds no CSP.

Subsequent exact artifacts on H100 reverse the proposal:

```text
/dev/shm/braid_audit/k10_exact.json: status INFEASIBLE
/dev/shm/braid_audit/k12_exact.json: status INFEASIBLE
/dev/shm/braid_audit/k15_gapcut_result.json: status INFEASIBLE
```

Claude's latest `LEDGER.md`, lines 364--375, explicitly says the independent
audit kills the generalization and marks the lane closed.  The old claim that
the stitching problem is a small open CSP is therefore false/obsolete.

## Bottom line

Claude's durable contributions here are the K8/K10 equivariant certificates,
the even bilayer normal form, and a live all-depth `bre_k13` experiment.  The
runtime narrative overstates proximity: no `tworail16` verdict is pending,
the purported suspended models are gone, dual rail has not passed the full
compiler chain, and the braid recipe was refuted.  As of the snapshot the
next credible events are a K16 compact/Waksman solver result or a genuine
`bre_k13` result—not anything from the retired `tworail16` process.

