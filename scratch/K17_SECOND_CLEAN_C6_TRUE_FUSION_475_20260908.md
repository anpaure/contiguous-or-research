# A genuine three-component clean C6 fusion in the current k17 GOOD sector

2026-09-08. Status: exact finite construction and complete computer-assisted
audit of one analytically prescribed move. All mathematical execution was
on h100, with one CPU process, 90 CPU seconds, 110 wall seconds, and 1 GiB
address space per phase. No random or broad candidate search was used.

## 1. Result

Start with the original canonical k17 PBBS factor, apply the previously
verified mountain C6, and keep the all-ports Johnson 306-owner prefix
unchanged. The explicit three-component clean C6 from the August 5 theorem
remains present and merges the following three GOOD components:

    mountain_135 + old_2(187) + old_8(153) -> one 475-cycle.

The labels old_i refer to the original canonical component numbering.
The current mountain_103 component is not changed. Every one of the 475
owners is retained once, and all source-factor degrees remain two.

The actual audited properties are:

* complete rank-eight adjacent-intersection multiset preserved;
* all 41,225 proper upper targets retained globally, using the actual
  306-owner linear prefix and the actual remaining cycles as backups;
* minimum positive coordinate run on the new upper-owner cycle is six;
* the 306-owner prefix is disjoint from the move and remains unchanged;
* a literal nonempty depth-three cyclic source has 475 letters, minimum
  letter rank six, and replays every owner and rank-eight facet exactly.

Thus the number of GOOD cycles decreases from 140 to 138. The current
stage consists of the same 306-owner path and 138 GOOD cycles. The path's
existing global rank-eight defects remain the same two missing labels
43857 and 46420, with one global duplicate, because this surgery's
rank-eight counter is unchanged.

This is a genuine component reduction with all requested guards, not just
an exchange of one two-cycle decomposition for another. It does not yet
give a single full-cube word or improve the recorded bound on nu(17).

## 2. Analytic specification and actual edges

Use the unrotated template of

    MATH_THEOREM_PBBS_EXPLICIT_THREE_COMPONENT_Q2_NEUTRAL_C6_20260805.md

at m=8. In lower rank-eight coordinates set

    K={3,12,13,14,15,16},
    (a_0,a_1,a_2)=(0,1,4), c=11,
    P_i=K+{a_i,a_(i+1)}, Q_i=K+{a_i,c}.

Delete the three undirected lower-owner edges

    (126987,129033), (127002,129034), (127001,129048)

and insert

    (126987,129034), (127002,129048), (127001,129033).

The verifier reconstructed the original f map by the unique cyclic Dyck
root, formed f^2, applied the first mountain surgery, and checked that all
three displayed old edges still exist. Their current component IDs are
exactly mountain_135, old_2, and old_8. No changed endpoint belongs to any
of the six bad cycles 115,116,118,122,129,138. Deleting one edge from each
of three distinct cycles leaves three paths; the cyclic reassignment joins
them into one cycle. The resulting 475-owner body was traversed literally.

## 3. Complete upper audit and the one outside backup

For every start on each affected old and new cyclic owner sequence, the
verifier repeatedly ORs the following owners until the full 17-set appears.
All intervening proper values of ranks 10 through 16 are retained with
literal witnesses. Repetitions are skipped only when their OR is unchanged.
Monotonicity makes stopping at the full set exact.

There is precisely one locally lost target and no locally gained target:

    131062.

Its outside backup is the unchanged mountain_103 cycle, cyclic start 25,
width seven, in the current recorded orientation. The full JSON includes
that literal witness, every common target's old/new witnesses, and the
complete lost/gained lists. Consequently the global proper upper support
remains exactly 41,225.

The outside calculation includes the **actual linear** prefix

    scratch/badsix_allports_johnson_306_owner_path.word

and excludes its six old intact cycles. Thus no discarded bad-cycle witness
is accidentally used as a backup. A future surgery on mountain_103 must
retain or replace the witness for 131062; the present result is not a
claim that this particular backup can subsequently be ignored.

## 4. Residence, lower palette, and literal source

The rank-eight adjacent-intersection counters of the affected upper-owner
cycles were compared exactly before and after the move. They are equal.
The positive-run histogram on the new 475-cycle is

    6:1, 7:289, 8:110, 9:15, 16:33, 18:2, 20:1,
    21:5, 22:1, 23:1, 29:15, 30:1, 32:1.

In particular there is no positive run of length below four. Define the
cyclic maximal depth-three source from the new upper owners T_i by

    E_p = T_p intersect T_(p-1) intersect T_(p-2) intersect T_(p-3).

Every E_p is nonempty. The verifier then checked every literal identity

    E_i union E_(i+1) union E_(i+2) union E_(i+3) = T_i,

and

    E_i union E_(i+1) union E_(i+2) = T_(i-1) intersect T_i.

This supplies an actual 475-letter cyclic source, not just a residence
certificate. Its source letters have minimum rank six. The source covers
the recorded component's owners and facets; it is not asserted to cover
the full Boolean cube or to survive an arbitrary linear opening.

## 5. Artifacts and reproduction

Local artifacts:

    scratch/audit_k17_second_clean_c6_20260908.py
    scratch/k17_second_clean_c6_topology_20260908.json
    scratch/k17_second_clean_c6_audit_20260908.json
    scratch/merged_475_upper_owner_cycle.word
    scratch/merged_475_depth3_source_cycle.word

The topology JSON contains all current component bodies before this move,
the actual prefix, the exact old/new edges, and the resulting cycle.
The audit JSON contains the complete target transport and outside-backup
certificate, the positive-run census, and the source verification record.

The remote directory is

    /home/amodo/exact-b-k17-second-c6-20260908/

The three bounded phases, with the source copied there as audit.py, are

    python3 audit.py topology
    python3 audit.py audit
    python3 audit.py source

They respectively verify current old-edge membership and 3-to-1 topology,
the complete requested support/palette/residence gates, and the literal
depth-three source. Each completed in under four seconds of its remote
execution call. Only the one published, unrotated candidate was tested.

## 6. Remaining construction boundary

The new cycle is compatible with the fixed shallow prefix and reduces the
GOOD component count by two. It does not join the remaining GOOD components,
supply a safe global opening, repair the missing rank-eight labels, or give a full lower
common-cap assignment. The all-dimensional equality objective remains open.
