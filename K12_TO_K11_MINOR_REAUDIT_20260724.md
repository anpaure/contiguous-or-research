# Re-audit of exact `k=12 -> k=11` minors against the length-477 bound

## Verdict

The authoritative exact source is `k12_optimal_nonzero.txt`, a verified
926-entry universal nonzero word on twelve coordinates.  Neither of the two
complete automatic families audited here—all surjective one-coordinate join
quotients and all coordinate-face restrictions—is competitive with the
verified 477-entry word `k11_completed_477.txt`.

The exhaustive normalized join-quotient family has best automatically
compressed length 774.  Literal coordinate restriction has best length 641.
Randomized deletion pruning previously reported and verified universal words
of lengths 585 and 583 respectively.  Those output artifacts are not retained
in the current workspace, and the outcomes are heuristic rather than
minimum-subsequence theorems.

Consequently the exact `k=12` certificate gives no improved complete
`k=11` word by the presently justified projection/minor operations.  A useful
inheritance remains the already retained 462-vertex avoiding-coordinate
central section, which is an upper-complete structural seed rather than a
complete OR word.  The complementary containing-coordinate section gives the
dual lower-side information, and the project also retains the combined
alternating-incidence-walk and sparse-hybrid viewpoints; none is currently a
complete word of length at most 477.

## 1. Authoritative source and benchmark

The exact source artifacts are:

```text
75754f3184c649d9d25b1705140d5627cf50c2b85e3a6dcabdd585dcf94a62da  k12_optimal_nonzero.txt
fc5238d201534f0bf0b0cf6ae084c185ccd90e8022d600ea74dcd5a759da3c9e  k12_optimal_verification.txt
7a3ee30962b99a91f87f516005b5e7cdeafd880e2d8c29bd7bc1107aa66bc162  k12_central_path_full.txt
```

The exhaustive verifier reports `length=926 covered=4095 required=4095`.
The central file consists of all 924 rank-six masks in a Johnson path, and
for the array `A` and path `Q` one has exactly

```text
Q[i] = A[i] | A[i+1] | A[i+2]    (0 <= i < 924).
```

The nearby files `k12_labelable_array_4083.txt`,
`k12_labelable_array_4087.txt`, and `k12_labelable_array_4088.txt` each have
926 entries but are not universal: their archived verifiers cover only 4083,
4087, and 4088 of the 4095 targets.  They are not valid sources for a theorem
that applies a quotient to a universal word.

The current comparison certificate is

```text
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
```

and both archived independent verifiers cover all 2047 nonzero masks.

## 2. Complete classification of one-coordinate join quotients

Let `phi:B_12 -> B_11` be a surjective join homomorphism with
`phi(empty)=empty`.  For every target atom `y`, surjectivity supplies a source
set whose image is `{y}`.  Since an image is the union of the images of its
source atoms, some source atom must itself map to `{y}`.  These eleven source
atoms are distinct.  Choose the remaining source atom `e`.  The singleton
images of the other eleven atoms define a bijection with the target atoms;
postcomposing by the inverse target-coordinate permutation makes those images
the natural singleton encodings.  This target relabelling changes neither
compressed length nor any coverage or pruning question for the fixed source
word.  The remaining source atom maps to an arbitrary mask `B`.

Thus, up to output-coordinate permutation, all such maps are exactly

```text
erased source coordinate e in {0,...,11};
arbitrary image B in {0,...,2047}.
```

The scanner evaluates `12*2^11=24576` normalized parameter pairs.  They cover
every map, with harmless duplicate representations when `B` is a singleton:
either source atom having that singleton image can be designated as `e`.
The family includes:

* coordinate erasure (`B=0`);
* identifying the extra coordinate with an existing coordinate (`B` a
  singleton);
* every higher-rank image of the extra coordinate.

Applying such a map entrywise preserves every interval-OR witness.  Deleting
zero images is safe, because zero does not change an OR and removal closes
only zero gaps.  Replacing a consecutive run of equal nonzero images by one
copy is safe for the same reason.  `scan_k12_join_quotients.cpp` exhausts this
complete family and performs both canonical simplifications.  The archived
exact census has global minimum 774, attained by sending source coordinate 11
to the full eleven-bit mask.

Target-coordinate permutations cannot change compressed length or the
existence of a deletion-pruned word, so the normalization loses no case.

## 3. Literal face restrictions

For source coordinate `e`, retain only entries not containing `e` and erase
that bit from their encoding.  A witness for a target avoiding `e` consists
entirely of entries avoiding `e`, so the retained subsequence is universal on
the eleven remaining coordinates.

For the exact 926-word, the twelve lengths, already after zero/equal-run
normalization, are

```text
671, 668, 675, 670, 673, 674, 672, 666, 661, 669, 664, 641.
```

The best face is coordinate 11.  Randomized exact-coverage deletion pruning
reached 583.  No face restriction is close to 477 before the extra heuristic
pruning stage.

## 4. What arbitrary deletion pruning does and does not prove

After either safe transformation, deleting an additional entry is valid only
when the resulting word is checked again for all 2047 targets.  The retained
order can create new cross-gap witnesses, so universality is not monotone in
the chosen subsequence.  In particular, an individually irredundant greedy
word is not a proof of minimum subsequence length.

The dedicated earlier audit records runs reaching 585 and 583, with the
program checking universality before accepting each improvement.  Their word
files and hashes are not retained here, so these are historical verified run
outcomes rather than archived certificates.  They do not certify that no
shorter subsequence of a particular quotient exists.  Conversely, the large
gaps

```text
774 -> 477   (best automatic join quotient),
641 -> 477   (best automatic restriction)
```

make a new large exact subsequence search unattractive: it would essentially
re-solve a constrained version of the hard `k=11` array problem and presently
has no structural indication of a 106-entry improvement over the best pruned
restriction.

Accordingly, the rigorous conclusion is that no **automatic** join quotient
or coordinate-face minor improves 477.  No claim is made that 583 is the exact
minimum among all subsequences of all transformed words.

## 5. Central-row section

Filtering `k12_central_path_full.txt` by coordinate 11 gives all 462 rank-six
masks on eleven coordinates.  Splitting at the 24 non-Johnson jumps and
reordering/reversing the 25 pieces gives the certified path
`k11_from_k12_upper_complete_path.txt` with:

```text
462/462 distinct central masks;
461/461 Johnson adjacencies;
complete union shadows in ranks 7,...,11;
missing lower shadows: 3 in rank 3, 18 in rank 4, 23 in rank 5;
delay-three internal-run deficit: 92.
```

Its SHA-256 is

```text
815d53fa427bc3a5b79bae5134fc2668480d98c739598ade3ceeafa249ed68fa.
```

This is useful as an upper-complete search seed, but it is neither a literal
OR factor nor a near-complete word.  Repairing its lower shadows, coordinate
runs, and labels is again the substantive `k=11` construction problem.

## 6. Reproduction policy

The existing exhaustive normalized-map scanner is
`scan_k12_join_quotients.cpp`; the restriction/pruning programs are
`project_and_prune_k12_to_k11.cpp` and `reduce_k12_to_k11.cpp`.  A guarded
launcher is supplied as `scratch/runpod_k12_to_k11_minor_audit.sh`.

The launcher refuses to run unless `RUNPOD_POD_ID` is present.  It verifies
the source and the 477 benchmark, performs the exact 24,576-map automatic
census, runs the optional heuristic pruning stages, and independently verifies
any emitted candidate.  The exhaustive part concerns the finite family of
join maps plus zero deletion/equal-run compression; the pruning restarts are
explicitly labelled heuristic.

No local compilation, CNF generation, SAT solving, or exhaustive projection
run was performed in preparing this re-audit.
