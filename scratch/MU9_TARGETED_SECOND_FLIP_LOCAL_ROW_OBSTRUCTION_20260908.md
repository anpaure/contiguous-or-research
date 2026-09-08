# Targeted second flips remove the old guards but expose a local row obstruction

2026-09-08. Cover-selectors bounded experiment and exact finite follow-up.
All computation ran through ssh h100. Scope: second flips only from
the three full84 one-flip representatives0,1,4. No third-flip search
and no free row-order solver was run. Root full-note integration audit
passed, including the forced-block and two-stage propagation arguments.

## 1. Targeted enumeration and outcome

The inputs, canonical cycle extraction, row geometry, and two displayed
guards were revalidated against the saved one-flip files. The original
one-flip theorem now records both root and direct-route full audits PASS.

For each specified starting Hamilton cycle, enumerate its1680 hexagons.
Retain a matching flip only when all three removed edges are present
and all three inserted edges are absent. Exclude the undo to the untouched
source. Require all84 intrinsic V targets, invalidate BOTH displayed
guard proofs, and require the result to remain one252-vertex Hamilton
cycle. Compare full edge sets to remove coordinate-rotation duplicates.

A previous guard is conservatively retained whenever every CURRENT q
occurrence still has a valid old five-window of physical lower vertices,
with its four other V targets globally unique. This allows guard values
to change and redundant q occurrences to disappear, so a superficial
renumbering does not count as destroying a proof.

| Start representative | Legal matching flips | All84, excluding undo | Destroy both old guards | Of those, Hamilton | Of those, no new simple guard |
|---:|---:|---:|---:|---:|---:|
|0|160|46|3|2|1|
|1|162|49|3|2|1|
|4|165|51|5|3|0|

The seven Hamilton survivors are checked for ANY globally guarded
target, using every five-position window at every occurrence. Five
still have such a target. The two exceptions are candidates0 and2 below.
Here “no simple guard” means only this four-globally-unique-neighbors
test; it is not an absence of more general propagation obstructions.

Both orientations of these two candidates were tested for42 locally
realizable blocks, all84 retained V targets, and the cheap fixed-z
critical-target collision conditions. All four models were INFEASIBLE.
The diagnostic ablation and explicit proofs below locate the actual
obstructions without relying on those solver statuses.

## 2. Exact two-flip candidates

Use the original14-mask pair-envelope source from the earlier notes.
All masks below refer to its nine fixed coordinates.

Candidate0 starts from one-flip representative0:

    first core={0,1,3}, outside={5,7,8};
    second core={1,3,5}, outside={0,4,6}.

For its second step remove

    (43,107), (58,59), (106,122)

and insert

    (43,59), (58,122), (106,107).

Candidate2 starts from one-flip representative1:

    first core={0,1,4}, outside={2,5,8};
    second core={1,6,8}, outside={3,4,7}.

For its second step remove

    (330,458), (338,346), (450,466)

and insert

    (330,346), (338,466), (450,458).

Both results are single Hamilton cycles and have all84 V targets.
Their complete S,U,V sequences are saved in
MU9_TARGETED_SECOND_HEX_FLIP_20260908.json.

## 3. Candidate0 really passes the raw V boundary test

Let D be the following42 dropped V indices in candidate0's canonical
forward orientation:

    0,4,6,11,15,18,20,25,27,29,33,36,37,41,
    43,48,52,55,57,62,64,65,70,75,80,82,85,86,
    87,89,94,98,102,105,106,107,108,111,112,113,118,123.

Consecutive cyclic gaps are at most5, and the84 retained positions
contain every rank-six target EXACTLY once. Both facts were directly
replayed. Thus this is a genuine42-block boundary witness if local
row realizability is ignored. It is not a macro row bank.

Consecutive drops d,e determine the next block by

    start s=d+2 modulo126,  length p=e-d modulo126.

The displayed witness has seven invalid local blocks:

    (13,4), (35,3), (50,4), (67,5),
    (72,5), (91,5), (115,5).

Their existence alone would only disqualify this witness. The next
section proves that every all84 partition fails local row geometry.

## 4. Candidate0: a forced impossible block, in either orientation

Write x_i=1 if V_i is dropped. Every five consecutive positions
contain a drop. A globally unique target must be retained, and each
other required target must retain at least one occurrence.

### Forward orientation

The positions7,8,9,10 carry globally unique targets, so the five-window
6,...,10 forces x_6=1. Positions76,77,78,79 are also globally unique,
so76,...,80 forces x_80=1. The target438 occurs exactly at positions
6,71,80. Therefore x_71=0.

Positions72,73,74 are globally unique. Together with x_71=0, the
window70,...,74 forces x_70=1. Positions72,73,74,76 are globally
unique, so72,...,76 forces x_75=1. Hence70 and75 are consecutive
drops, with71,...,74 retained. They force the block(s,p)=(72,5).

Its rank-four targets are

    S_72,...,S_76 = (432,418,298,267,329),
    U_71=436.

The four entering coordinate masks are(2,8,1,64); the departing masks
are(16,128,32,2). Thus the first entering coordinate is later removed.
The common intersection is256, whereas a p=5 prefix row requires an
empty common intersection. This block cannot be realized by any row
order. No fixed-z or extreme-rank constraint is used in the contradiction.

### Reverse orientation

Use S'_i=S_(-i), U'_i=U_(-i-1). Positions2,3,4,5 in the resulting V'
sequence are globally unique, forcing x'_6=1. Positions7,8,9 are
globally unique. Window7,...,11 therefore forces a drop at10 or11.
The next drop after6 must be10 or11, forcing a block starting at8 of
length4 or5.

The first four/five lower targets are

    (202,106,75,77),  or  (202,106,75,77,92),
    with U'_7=218.

Already the first entering mask32 is removed at the next swap. The
four-target intersection is72 (two coordinates instead of the required
one); the five-target intersection is still72 (instead of empty).
Both forced block lengths are impossible.

Consequently candidate0 has an exact raw rank-six partition but has
NO all84 partition into the required locally realizable prefix rows,
in either orientation. This is a separate local-geodesicity obstruction.

## 5. Candidate2: a two-stage drop-spacing contradiction

No local row constraints are needed here. Positions104,105,107,108
carry globally unique targets359,119,407,411. Window104,...,108 forces
position106 to be dropped. Target183 occurs only at25 and106, so25
must be retained. The other positions26,27,28 are globally unique;
window24,...,28 now forces24 to be dropped.

Positions66,67,68,69 are globally unique, forcing70 to be dropped.
Positions79,80,81,82 are globally unique, forcing83 to be dropped.
But target438 occurs precisely at24,70,83. All its occurrences have
been dropped, a contradiction.

This implication uses a forced retained occurrence of a duplicated
target as an intermediate step. It explains why the simple global-unique
guard test did not detect candidate2. The argument involves only cyclic
five-windows and target multiplicities and therefore holds in the reverse
orientation as well.

## 6. Fixed-z collision conditions were valid but unnecessary here

For a valid block(s,p), its two fixed z-present rank-five path endpoints
are

    {z} union S_(s+p-1),
    {z} union ([9] minus U_(s-1)).

They coincide only at p=5, where they describe the same row cell.
Every selected row's fixed critical target must be different from every
other selected row's fixed target of that rank, because42 balanced rows
have exactly the full rank4/5/6 occurrence capacities.

More generally write K for the unordered right prefix of length5-p,
and C for the unordered left suffix of that same length. Their orders
vary independently on disjoint coordinate sets. A z-present prefix cell
is order-invariant precisely when its left prefix length is p or5 and
its right prefix length is0 or at least|K|. These exact fixed-cell rules
passed direct-route's independent algebra audit before the screen.

The boundary models also imposed n_1,n_5>=1,
2n_1+n_2>=9, and n_4+2n_5>=9 as cheap necessary full-cube capacities.
The ablation proves that none of these additional conditions causes
the failure: candidate0 already fails local row geometry alone, and
candidate2 already fails the raw rank-six drop-spacing condition.

## 7. Exact Boolean replay and next mathematical target

The three short arguments above were also extracted from independently
replayed unit-propagation proofs. The Boolean clause families were:

- at least one drop in each five-window;
- at least one retained occurrence of each target;
- at most one retained occurrence of each target when the84-slot ledger
  is imposed; and
- for an invalid block(s,p), the corresponding endpoint drops cannot
  be consecutive.

If the latter endpoints are d,e, its clause is

    not x_d OR not x_e OR x_(d+1) OR ... OR x_(e-1).

The extracted contradiction cores actually use no at-most-one clauses.
Every forced assignment and final contradiction was replayed without
importing CP-SAT. Clause metadata, dependency cores, and proof traces
are saved in MU9_SECOND_FLIP_BOOLEAN_CERTIFICATES_20260908.json.

The narrow next mathematical issue is now explicit. Candidate0 shows
that defeating the old guards and matching the complete rank-six drop
ledger is possible. An improvement must also avoid its forced backtracking
lower path, for example by changing the relevant local S path or the
target multiplicity/five-window implications forcing that block. A
different physical construction could also go beyond this consecutive
prefix-row model. The present result supplies no such construction,
and no further flip search was run.

## 8. Sources, caps, and saved reports

All files below are in this scratch directory:

- target_mu9_second_hex_flip_guards_20260908.py
- ablate_mu9_second_flip_partition_constraints_20260908.py
- certify_mu9_second_flip_block_failures_20260908.py
- MU9_TARGETED_SECOND_HEX_FLIP_20260908.json
- MU9_SECOND_FLIP_CONSTRAINT_ABLATION_20260908.json
- MU9_SECOND_FLIP_BOOLEAN_CERTIFICATES_20260908.json

The remote directory is
/tmp/mu9_targeted_second_flip_20260908_cover_selectors/.
The main run was pinned to two CPUs, capped at1GiB, and protected by
an18-second internal alarm and20-second outer timeout. Its measured
Python runtime was0.3851 seconds; the ablation took0.2716 seconds and
the Boolean certificate extraction/replay0.0064 seconds. All numerical
work, including the small diagnostic mask extraction, ran on h100.

No actual42-row binary-ten cover, coefficient improvement, or obstruction
to arbitrary row banks is claimed. The result is an exact diagnosis of
this tightly specified second-flip consecutive-block family.
