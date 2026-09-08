# Fixed-bank triple caps: independently checked UNSAT certificate

2026-09-08. The complete fixed-bank formula now has an accepted independent
DRAT proof. This result is restricted to the original canonical 146-cycle
bank, H1/H2 frozen, all H3 native triples preserved, and all lower targets
required inside those cyclic components. It is not an obstruction to
arbitrary words. The subsequently supplied optimal 24,313-letter word uses
a different chronology and has been verified independently.

The [encoding and original run](K17_UNRESTRICTED_TRIPLE_CAPS_CNF_SINGLE_SOLVER_RUN_20260908.md)
retain the complete scope and variable/host proof. The unchanged formula
has 720,885 variables and 3,023,399 clauses, SHA-256

    673d26f3dc605da62cdfa335953c1637eb1375f0fee82e85822b68ab4b8747ab.

## Proof-export failure and repair

The first solver call reported UNSAT, but the original binary proof was
truncated at 1,448,580 bytes, with an incomplete final operation and no
empty-clause addition. The independent checker rejected it. Appending an
empty-clause addition to its complete prefix was also rejected; that
candidate is not a valid proof and was never promoted.

A tiny contradictory two-variable regression showed that deleting the
solver before reading a retained duplicate file descriptor did not by
itself flush the proof: its captured proof was empty and rejected.
No cap-formula solve occurred in that failed regression attempt.

The corrected capture explicitly calls the C runtime's fflush(NULL) while
the native streams and their descriptors are alive, before seeking or
reading the Python file object. Its tiny regression produced a complete
eight-byte proof and passed DRAT checking. The same corrected capture was
then used for **one additional replay of the identical immutable formula,
with the same CaDiCaL195 seed zero**. This was certificate reproduction,
not an alternate cap instance, seed or construction search.

Thus there were two total cap-formula decision calls: the original run
and this one replay. The replay also returned UNSAT, with identical reported
statistics (1,130 conflicts, 1,565,640 decisions, 45,446,192 propagations).
The original failed artifacts remain unchanged.

## Accepted independent check

The complete proof has 1,450,630 bytes, 112,032 operations, and one
empty-clause addition. Its SHA-256 is

    acfb05ad0054a4824fb3529865b12b7b35ae7c7f76741959ba786e3af6d477ea.

The separately built [official drat-trim checker](https://github.com/marijnheule/drat-trim)
was pinned at commit2e3b2dc0ecf938addbd779d42877b6ed69d9a985. Its result was

    420 of 3023399 original clauses in core
    215 lemmas in core using720resolution steps
    0 RAT lemmas in core
    s VERIFIED

Checking took about1.55seconds; wrapper elapsed1.74seconds. The recovered
proof is therefore an accepted UNSAT certificate for the reviewed finite
encoding. The generated LRAT file is retained, but no separate LRAT checker
was run. The core has420original clauses; no further semantic core analysis
is claimed here.

## Artifacts and limits

- [Proof-export repair script](recover_k17_triple_caps_proof_20260908.py).
- [Independent checking wrapper](check_k17_triple_caps_complete_drat_20260908.py).
- [Replay report](k17_unrestricted_triple_caps_20260908/certificate_export_replay_flushed/replay_report.json).
- [Complete proof](k17_unrestricted_triple_caps_20260908/certificate_export_replay_flushed/complete_solver_proof.drat.bin).
- [Checker report](k17_unrestricted_triple_caps_20260908/certificate_export_replay_flushed/independent_drat_check_report.json).
- [Checker log](k17_unrestricted_triple_caps_20260908/certificate_export_replay_flushed/independent_drat_check.log).
- [Extracted original core](k17_unrestricted_triple_caps_20260908/certificate_export_replay_flushed/verified_original_core.cnf).

The replay allowed60CPU/90wall seconds and4GiB, and completed in7.55seconds.
The independent checker allowed120CPU/150wall seconds and4GiB. All execution
was onh100/arboghast. No limit was reached and no process remains running.
This computational proof does not constitute an external review or a
proof-assistant certification of the broader PBBS mathematics.
