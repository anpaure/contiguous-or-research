# Independent pre-execution review of the second19/20 verifier and19 reconstruction

2026-09-09. `exact_b_finite_frontier` read both complete sources below.
**PASS: no mathematical correction required.** This note is source review
only; I did not execute either program. It is separate from my already
completed forward first-occurrence check of the supplied words.

## 1. Suffix census, independent range queries, cyclic19 and exact20 lift

Reviewed source:
[verify_k19_k20_optimal_suffix_and_lift.py](../scripts/verify_k19_k20_optimal_suffix_and_lift.py).

At endpoint j, the recurrence keeps the current literal and extends
every previously distinct ending OR by the new literal. It therefore
enumerates exactly the ending OR set. When multiple intervals yield
the same OR, retaining their latest start loses no subsequent OR value
and minimizes the stored witness span for that endpoint. The at-most-k
bound follows from the strict inclusion chain of distinct nonempty
ending ORs. The code does not equate duplicate starts with duplicate
target coverage.

All target indices are checked after the census, and the observed rank
counts must equal every binomial coefficient. The additional middle
checks correctly require exactly the first three endpoints to lack a
middle target, no repeated middle label, and one event for every middle
label. They do not replace the full-cube coverage check.

The subsequent segment tree is built independently from the literal
input. Every saved inclusive ordinary interval is bounds-checked and
queried; its result must equal the named target. The output contains
all target witnesses, not a sample. Both raw input hashes and expected
lengths are checked before these operations.

For the cyclic19 deduction, A=C+C[:3] is verified as a literal identity.
Every independently range-checked witness has length at most |C|.
Reducing its start modulo |C| therefore yields an admissible cyclic
interval with identical letters and OR. All |C| cyclic triple/four
phases are additionally checked and give the complete rank9/rank10
bijections. Cyclic endpoint capacity gives the matching lower bound
|C|=binom(19,10); no unprovided quotient generator is required.

The20 reconstruction appends the pure new-coordinate letter and the
specified |C|-1 marked core letters to A. The program checks both the
resulting integer sequence and its serialized bytes against the supplied
20 file. It does not merely compare lengths or hashes of a proposed
formula. Full20 coverage is separately verified before reconstruction.

The all-rank endpoint computations for19 through22 use exact integer
binary search and check both sides of each minimal tau. The extra21
turnover/paired-run fields evaluate separately established formulas;
this source audit does not replace the mathematical proof of those
general formulas. The final report is written only after every asserted
coverage, range, cyclic and byte-reconstruction condition passes.

The one-run host and60 CPU/90 wall/2 GiB limits are explicit. An
exception or external resource interruption cannot produce FINAL_PASS.

## 2. Literal19 carrier and lower compiler reconstruction

Reviewed source:
[reconstruct_k19_optimal_literal_carrier_and_lower_compiler_20260909.py](reconstruct_k19_optimal_literal_carrier_and_lower_compiler_20260909.py),
including the final change making the ACTUAL fixed-Phi comparison a
diagnostic rather than an abort condition. The separately pinned native
canonical input is still checked against its own expected Phi convention.

The future-window definitions are consistent:

    R_i=OR(C_i,C_(i+1),C_(i+2)),
    U_i=OR(C_i,...,C_(i+3)),
    E_i=AND(U_(i-3),...,U_i).

Every original literal belongs to E at the same index. The source
explicitly checks both envelope-window equalities, the rank9/rank10
bijections, Johnson insertions/deletions, and the two stated delayed
deletion exclusions. The three terms of Pin_i are exactly the deficits
in the three native triple windows containing i. This is an individual
pin calculation; no unsupported assertion that arbitrary simultaneous
caps preserve the triples is added.

Every lower target of rank at most8 is required to have an actual
literal or pair witness. Such witnesses cover the entire period,
including its final wrapping pair; C+C[:3] contains that pair as an
ordinary interval. All stored half-open length1/2 witness intervals
are directly OR-replayed against the supplied linear word. Since
every triple has rank9, no longer interval could supply an omitted
rank-at-most8 target; the short inventory has the intended scope.

For the native comparison, the code checks the full named lower layer,
unique incoming upper matching and native outgoing Phi relation. The
map taking an actual incoming upper to its native lower owner is a
permutation. Its decomposed cycles give exactly the asserted cyclic
transport of old incoming labels. This remains true if the ACTUAL
outgoing matching has changed too: it compares one matching at a time.
The updated report separately counts outgoing changes instead of
assuming they vanish.

All19 rotations of each representative are explicitly enumerated and
must be distinct members of the complete lower layer. Each field is
tested for rotation equivariance. The report correctly says that a
single representative determines that field only if its own check has
zero violations; it also saves the entire named carrier and actual
orbit positions. A non-equivariant literal compiler is therefore not
silently replaced by a fictitious compact quotient.

The supplied literal SHA is required as a root-pinned command argument;
the canonical file has its own fixed SHA assertion. The host, resource
limits and fail-if-existing output directory are explicit. Any failed
structural condition is an architecture/input mismatch, not a rejection
of the separately proved literal optimum. This program does not claim
to recover or replay an unprovided search/generator.
