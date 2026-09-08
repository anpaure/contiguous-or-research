# Fixed supplied21 structural reconstruction: review plan

Status: the single reviewed and authorized run **passed**; see the
[result and proof record](K21_SUPPLIED_THREE_CYCLE_CARRIER_LOWER_HOLES_AND_572_REPAIR_CERTIFICATE_20260909.md).
The text below records its pre-execution scope. This is the literal 353297-letter
submission with three periods, not the separate 357442-letter/12-cycle claim.
The finite-frontier agent independently read the complete source and this
plan and passed the phase, cyclic filtering, prefix/tail continuation, short
witnesses, range replay, and scope. Root then read the complete source, passed
it, and authorized exactly the one run that is now recorded.

Input: `answers/k21_upper353297.word`, SHA-256
`0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7`.
Source: [reconstruct_k21_supplied_three_cycle_carrier_and_572_repairs_20260909.py](reconstruct_k21_supplied_three_cycle_carrier_and_572_repairs_20260909.py).
Only one h100 run is proposed, after root review: 60 CPU seconds, 90 wall
seconds, 2 GiB address space, 512 MiB per output file. No search or alternative
cut, word edit, flow, or optimisation is performed.

## 1. Literal split and exact phase

The three periods have lengths 352548, 105, 63. Each is followed by its own
first three letters. Their period total is
`binom(21,10)=binom(21,11)=352716`; their opened concatenation has length
352725. The final 572 input letters are retained verbatim as the repair tail.

On each period define, with its own cyclic indexing,

\[
R_i=C_i\cup C_{i+1}\cup C_{i+2},\qquad
U_i=R_i\cup C_{i+3},\qquad
E_i=U_{i-3}\cap U_{i-2}\cap U_{i-1}\cap U_i.
\]

The checker verifies global bijections onto ranks 10 and 11, the two middle
incidence identities, and the causal, **same-index** cap relation `C_i⊆E_i`.
Each of `E_i,E_(i+1),E_(i+2)` lies in `U_(i-1)∩U_i=R_i`; the actual three
letters supply the reverse inclusion. Thus `OR3(E)_i=R_i`, and similarly
`OR4(E)_i=U_i`. Both identities are checked explicitly rather than inferred
from the user's indexing convention.

All singleton insertion/deletion steps and both delayed-deletion exclusions
are checked. Fixed canonical Phi uses the first strict global prefix minimum
in positive coordinate order. **Phi agreement is a diagnostic, not a required
premise**: violations are saved and the other checks continue. Literal pairs
are compared with envelope pairs, without assuming preservation.

## 2. Lower compiler and rotation quotient

Every period interval of length at least three contains a rank-10 triple.
Consequently every cyclic target of rank at most nine must be a literal or a
pair. The source enumerates their exact named sets, overlap, missing labels,
and ordinary witnesses in the actual three opened blocks. Every such witness
is replayed directly from one or two original letters. Missing lower labels
are reported; they are not silently excluded or assumed repaired by a flow.

Individual necessary triple-deficit pins are computed from the envelopes.
The actual caps must contain them. Simultaneous preservation is established
by the actual triple equalities, not by pins alone.

Every rank-10 mask has a 21-element coordinate orbit: a shorter rotational
period would require its weight to be divisible by a nontrivial divisor of
21, whereas `gcd(21,10)=1`. Thus there are 16796 named lower representatives.
The script independently tests equivariance of successor, incoming/outgoing
upper, envelope, pins, and actual literal cap. A representative reconstructs
only fields whose equivariance was verified. Full named rows are also saved.
This does not reconstruct an unprovided compact generation/search history.

## 3. Exact bank, opened-prefix, and repair comparison

Suffix ORs are maintained in decreasing order of their latest possible start.
Nested suffixes have nested ORs, so equal values are adjacent. Keeping the
first occurrence of each OR preserves its latest start, which suffices both
for ordinary coverage and for imposing a maximum cyclic interval length.

For each core separately the script scans two periods, retains states of
length at most that period, and marks targets only during the second period.
This enumerates exactly its cyclic targets, without counting inter-core joins.
The complete low part is independently compared with the literal/pair census.

The actual opened concatenation is then scanned once. Its hole set is compared
with the cyclic-bank hole set: this distinguishes opening losses from targets
gained at physical joins. The same actual suffix state is continued through
the 572 input repair letters. Every newly supplied target receives a concrete
ordinary interval; all these intervals are independently replayed in a segment
OR tree built from the literal word. The script also reports whether the set
of 572 repair letters equals the prefix hole set, without imposing that as a
premise.

Final coverage failure retains the diagnostics and prevents a PASS. Root's
separate full-cube witness audit remains the authoritative independent check
of all supplied-word witnesses; this structural run replays all short lower
witnesses and every target newly supplied by the repair tail.

## 4. Boundaries

No 462 weighted-Hall certificate is claimed. No new cycle bank, matching, cut,
literal modification, or candidate search is attempted. A resource stop or
runtime failure is inconclusive. The source pins the supplied file, saves
all diagnostics before final coverage assertion, records its own hash, and
exports a SHA-256 artifact manifest.
