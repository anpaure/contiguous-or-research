# Complementary exact portfolio for the reduced direct-span CNF

## Formula

Both runs solve the same independently audited full formula:

```text
scratch/k11_length476_five_deletion_span_20260724/delete5_append16_span.cnf
```

with SHA-256

```text
42d64edb00f1a8cb0367b3071b2bb6a8d1cdce75e1f09f9df34d509743d6334f
```

No assumptions, deletion branches, or heuristic restrictions are added.
Thus either solver returning SAT gives a global model for this entire
delete-five/append-sixteen neighborhood, and either returning UNSAT gives a
global solver verdict for the neighborhood.  An UNSAT verdict is not yet a
certificate because these exploratory runs do not write proofs.

## Existing SAT-targeted run

The existing run is left untouched:

```sh
nice -n 15 kissat \
  --sat --walkinitially --seed=20260724 \
  scratch/k11_length476_five_deletion_span_20260724/delete5_append16_span.cnf
```

Its nondefault search settings are:

```text
target=2
restart interval=50
initial local walk enabled
initial phase=true
stable mode=1
```

The durable log is

```text
scratch/k11_length476_five_deletion_span_20260724/kissat.sat.log
```

and the tmux session is `k11_delete5_span_solve`.

## Complementary focused/phase-zero run

The complementary run uses the opposite search bias:

```sh
nice -n 19 kissat \
  --unsat --phase=false --seed=271828 \
  scratch/k11_length476_five_deletion_span_20260724/delete5_append16_span.cnf
```

The `--unsat` preset sets `stable=0`, so this run remains in focused search
instead of switching between focused and stable modes.  It also begins from
the opposite phase and has an independent random seed.  These differences
alter restarts, decision phases, learned-clause trajectories, and
preprocessing choices while retaining exact full-formula semantics.

The process is deliberately resource-conscious: one process, one core,
`nice 19`, no proof stream, and no copy of the CNF.  It was launched as

```sh
tmux new-session -d -s k11_delete5_span_unsat \
  'cd /Users/amir.nuriyev/Documents/problem && \
   /usr/bin/time -l nice -n 19 kissat \
     --unsat --phase=false --seed=271828 \
     scratch/k11_length476_five_deletion_span_20260724/delete5_append16_span.cnf \
     > scratch/k11_length476_five_deletion_span_20260724/kissat.unsat_phase0.log \
     2> scratch/k11_length476_five_deletion_span_20260724/kissat.unsat_phase0.time; \
   rc=$?; echo $rc > \
     scratch/k11_length476_five_deletion_span_20260724/kissat.unsat_phase0.status'
```

At the initial audit snapshot it had completed preprocessing and entered
search without a terminal `s` line.  Its early trace is visibly distinct:
focused search remains at switch level zero, whereas the SAT-targeted run
alternates modes and starts with the phase/walk configuration above.

## Terminal handling

For SAT, decode and independently verify with

```sh
python3 scratch/decode_delete_append_span_model.py \
  k11_upper549_natural_array.txt \
  scratch/k11_length476_five_deletion_span_20260724/delete5_append16_span.map \
  SOLVER_LOG \
  VERIFIED_WORD.txt
```

The decoder compares two independent contiguous-OR implementations before
accepting the model.

For UNSAT, preserve the exploratory log but make no certified claim.  Rerun
the same audited CNF with a binary proof path, then verify the proof
independently before updating the mathematical status.

## Later status correction

Both monolithic processes were externally terminated with status 143 and no
terminal SAT/UNSAT line.  The SAT-oriented run accumulated about 3,841 CPU
seconds; the focused phase-zero run accumulated about 3,322 CPU seconds.
Neither result is mathematical evidence for satisfiability or
unsatisfiability.

An attempted 792-cube follow-up using `delete_count_b8.jsonl` was also found
invalid: it inferred counter-row stride six although the CNF allocates five
AMO auxiliaries after every six-state row, making the true stride eleven.
Every result from that malformed cube file is quarantined.  Corrected
explicit-row decompositions and their current UNKNOWN status are documented
in `K11_DELETE5_CORRECTED_CUBE_FRONTIER_20260724.md`.
