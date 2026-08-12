# Exact cross-parent transparent-donor no-go for K's `j3959` buffer

This census extends the same-parent contiguous-donor audit to every
authenticated optimal K15 parent chronology.  Candidate packets are every
contiguous carrier block of length `1..64`, in both orientations, from the
canonical parent and six repeat-free parents.  Each block is mapped by mask
value to its unique physical K16 occurrences, so it may be noncontiguous in
the current chronology while occurrence conservation remains exact.

For each of the two empty donor gaps `R0/R1` (the released-`Q` gap) and
`R1/R2`, a candidate must:

1. pass the exact depth-three destination endpoint signature;
2. close every scattered source gap created by removing its occurrence
   labels;
3. delete exactly the assigned old replay defects and introduce none;
4. retain nonempty maximal envelopes and all five named upper tokens.

The exact result is

```text
authenticated parents                         7
raw oriented parent blocks             5,737,536
unique occurrence-labelled candidates  1,647,284
destination-signature survivors              232
full transparent donors                         0
```

The 232 endpoint-compatible candidates split as

```text
R0/R1 candidates: 144
R1/R2 candidates:  88
```

Thus none of the four-reflection K15 parent blocks of length at most 64 is a
transparent absorber for either empty gap.  More strongly, every disjoint
pair of those endpoint-compatible packets was combined with each of the nine
known exact `R2/R3` donors.  This gives exactly 104,328 occurrence-conserving
joint candidates.  Full variable-depth replay finds **zero exact carriers**.
Hence the two nontransparent source-defect sets cannot cancel inside this
entire fixed parent-block family.

This does not exclude longer parent blocks, arbitrary cross-reconnection of
the exposed occurrence components, or a different one of the 5,166 upper-
service blocks.  Those are now the live finite families.

Artifacts:

```text
scratch/search_k16_j3959_crossparent_transparent_donors_20260730.cpp
SHA-256 251614bcc9a8ce5f8175b787b61b7bceacab7562f9ef9b3bb1ac0d1fb17f154d

scratch/k16_j3959_crossparent_donors_20260730/run.stdout
SHA-256 4d8120dd756d4e0535ce44e81448f4a50d7ea85da8b3fa828837e6cdf0078296

scratch/k16_j3959_crossparent_donors_20260730/singles.tsv
SHA-256 af44c69d71076d48e8ff0d5dc282c53c98cc0c50b15d26e78b4bbc81d839eab2

scratch/k16_j3959_crossparent_donors_20260730/joins.tsv
SHA-256 eb653a942d9edc0ce26b3ba1b34ea7334953c4c471d8b0a2174158a712c4b67c
```

The authenticated H100 executable had SHA-256
`a550887f8b769e91d45914805a4c993c72de62b8cb0574357ac4c9302a09477b`.
