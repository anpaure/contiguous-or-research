# Supplied21: exact three-cycle carrier and the 572-letter repair

Date: 2026-09-09. Status: **PASS**, one reviewed and authorized h100 run.
This is the supplied 353297-letter word. It is not the separate
357442-letter, 12-cycle report.

## 1. Input, execution, and reproducibility

Input: [k21_upper353297.word](../answers/k21_upper353297.word), SHA-256
`0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7`.

Reviewed source:
[reconstruct_k21_supplied_three_cycle_carrier_and_572_repairs_20260909.py](reconstruct_k21_supplied_three_cycle_carrier_and_572_repairs_20260909.py),
SHA-256 `8d4ec0ff311fe22ef177118bfa8135af54b8361755c57e1beab518299c15c8ca`.
The [review plan](K21_SUPPLIED_THREE_CYCLE_STRUCTURAL_RECONSTRUCTION_REVIEW_PLAN_20260909.md)
contains the phase and enumeration proofs. Root and finite-frontier both read
the complete source and passed it before execution.

Exactly one run on `h100`/`arboghast`, with 60 CPU seconds, 90 wall seconds,
2 GiB address space and 512 MiB per-file bounds, completed successfully in
8.92601687181741 seconds. No search, alternative cut, decomposition trial,
word edit, or retry was performed.

Complete artifact bundle:
[k21_literal_structure_20260909](k21_literal_structure_20260909/).
Primary report:
[k21_three_cycle_structure_and_repairs_certificate.json](k21_literal_structure_20260909/k21_three_cycle_structure_and_repairs_certificate.json).
Remote original: `/home/amodo/exact-b-k21-k22-upper-20260909/literal21_structure/`.
The certificate SHA-256 is
`7b2230f8a92fc6e7d8498d7dd632ca3dda0a6418894d0084dcc19b677887c829`.
All ten primary artifacts were copied locally and passed the remote-generated
SHA-256 manifest. Source snapshot, run log, provenance, and hash-replay output
are included in the local bundle.

## 2. Exact skeleton, middle carrier, and envelope phase

The periods have lengths **352548, 105, 63**. Their sum is
`W(21)=binom(21,10)=binom(21,11)=352716`. Each is followed by its own first
three letters. The physical opened prefix therefore has length352725, and
the last572 letters are exactly the supplied repair tail.

Using each period's cyclic indices, define

\[
R_i=C_i\cup C_{i+1}\cup C_{i+2},\quad
U_i=R_i\cup C_{i+3},\quad
E_i=U_{i-3}\cap U_{i-2}\cap U_{i-1}\cap U_i.
\]

Every triple has rank10 and every four-window rank11. Across the three
cycles, both rows are bijections onto the entire corresponding middle
layer. The actual outgoing upper is canonical Phi at **all352716** lower
states. Both delayed-deletion exclusions hold at every transition.

All envelopes have rank8. The literal relation is `C_i⊆E_i` at the **same
index**, with

\[
E_i\cup E_{i+1}\cup E_{i+2}=R_i,\qquad
E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}=U_i.
\]

The phase follows because every one of the first three envelopes lies in
`U_(i−1)∩U_i=R_i`, and the corresponding actual letters supply the reverse
inclusion. The checker also verifies both equalities literally.

All envelope pairs have rank9. The actual caps change **53717, 21, 63**
pair occurrences on the three cycles respectively. These changed pairs
shrink to ranks6,7,8. Thus the construction uses pair changes; preserving
every native pair is not part of its compiler.

## 3. Exact lower palette of the cyclic bank

Since every three-letter interval has rank10, every cyclic target of rank
at most9 must be a literal or a pair. The complete named short-interval
census is:

|Rank|Possible|Distinct literals|Distinct pairs|Overlap|Covered|Missing|
|---:|---:|---:|---:|---:|---:|---:|
|1|21|21|0|0|21|0|
|2|210|210|0|0|210|0|
|3|1330|1330|0|0|1330|0|
|4|5985|5985|0|0|5985|0|
|5|20349|20349|0|0|20349|0|
|6|54264|53951|314|1|54264|0|
|7|116280|112871|3297|60|116108|172|
|8|203490|153472|50124|408|203188|302|
|9|293930|0|293835|0|293835|95|

Every listed covered target has a saved one- or two-letter ordinary witness
in the actual opened blocks, and every such witness was directly replayed.
The complete cyclic suffix-OR enumeration independently agrees with this
low-rank census.

The cyclic bank covers **2096582** nonempty targets and misses exactly
**569**:172 of rank7,302 of rank8,95 of rank9. In particular **every target
of rank10 through21 is covered cyclically**. The actual low compiler is
not complete before repair.

## 4. Opening losses and the exact repair

Scanning the supplied opened concatenation, including its two physical
inter-cycle joins, gives **2096572** targets and **579** holes. The569 cyclic
lower holes remain. Opening adds exactly ten losses:

|Rank|Additional opening holes|
|---:|---:|
|12|1|
|13|2|
|14|3|
|15|3|
|16|1|

There are no gains from the physical joins relative to the cyclic bank.
The ten named opening losses are
`1082367,1098751,1102847,1606655,1623039,1627135,1868799,1885183,1999871,2016255`.
The exact named holes and both kinds of difference are saved in
[cyclic_bank_opened_prefix_and_repair_holes.json](k21_literal_structure_20260909/cyclic_bank_opened_prefix_and_repair_holes.json).

The final572 letters are pairwise distinct, and their literal set is **not**
the579-element prefix hole set. Continuing the actual suffix-OR state through
this tail supplies all579 holes. Every newly supplied target has a saved
ordinary interval ending in the tail, and all579 witnesses were independently
checked in a segment OR tree built from the supplied full word. Thus the
finished word covers all **2097151** nonempty21-coordinate targets.

The statement above verifies the actual repair word. It does not reconstruct
an unavailable original repair forest or its search history. Because579
targets are supplied by572 letters, at least seven newly supplied targets
require nonliteral intervals in this tail-based repair accounting.

## 5. What the rotation quotient does and does not encode

Every middle lower mask has a full21-element coordinate-rotation orbit,
giving **16796** representative rows. The following named fields are exactly
rotation-equivariant: successor, outgoing upper, incoming upper, envelope,
and individual triple-deficit pins.

The actual literal-cap field is **not** equivariant: the one-step test fails
at6520 named lower states. Therefore the quotient reconstructs the carrier,
envelopes, and pins; it does **not** by itself reconstruct all actual capped
letters. Both the full named rows and all literal-cap violations are exported.
This distinction matters when using the compact carrier as input to another
compiler.

## 6. Scope of the resulting construction evidence

This supplies a literal-derived carrier with complete middle and cyclic
upper coverage, together with an explicit pair-changing compiler that has
569 lower holes and an explicit572-letter repair after the stated openings.
It does not prove the all-dimension induction or an optimal21 bound.

No462 weighted-Hall certificate, original generator, or unavailable search
certificate is asserted by this run. A separate fixed candidate-graph audit
may study that claim using the same envelopes, with its own reviewed source
and authorization. Root's independently executed full-cube witness check is
separate from this structural reconstruction.
