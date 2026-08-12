# Exact contiguous transparent-donor census for K's `j3959` buffer

K's occurrence-conserving buffered chronology supplies the five named upper
targets but has three pre-flat donor gaps.  This census asks whether an intact
pre-flat segment can be moved into one gap while its old source gap closes
exactly, with every other old defect unchanged and all five upper service
tokens retained.

Every intact segment of length `1..64` in each of the four pre-flat pieces
was tested in both orientations.  The destination seam was first checked by
the exact depth-three endpoint replay; every survivor was then materialized
and checked by full variable-depth maximal-envelope replay, source-gap
closure and upper-token replay.

The exact census is

```text
raw oriented segments         806,144
destination-local survivors       381
full transparent donors              9
```

The nine donors all repair only the third gap `R2/R3`.  The distribution by
gap is

```text
R0/R1 (the released-Q gap): 0
R1/R2:                      0
R2/R3:                      9
```

Consequently there is no triple of independent contiguous donors in this
length range.  In particular, no intact same-parent segment of length at most
64 can replace forward `Q` at its source while preserving the five service
tokens and closing its own source gap.

This is a scoped no-go.  It does not cover noncontiguous/cross-reconnected
packets, cross-parent blocks, segments longer than 64, or a different
service chronology.  The exact next lane is a cross-parent/noncontiguous
donor for the first two gaps, using any of the nine certified third-gap
donors as the fixed final component.

Artifacts:

```text
scratch/search_k16_j3959_kbuffer_transparent_donors_20260730.cpp
SHA-256 627e77e503b2d45cc7070c61e350df46d61e3a4cca1340541a49b79456aca990

scratch/k16_rf_halo_j3959_upper_o5_20260730/kbuffer_singles.tsv
SHA-256 99ad7f28661ed42e46830ba567931ed2520edb26152d3874de9f4a2385e60842

scratch/k16_rf_halo_j3959_upper_o5_20260730/kbuffer_joins.tsv
SHA-256 47628d655148ebcce2e8dd05caa0293e96472825de6a623f345d52a4b83c9bde

scratch/k16_rf_halo_j3959_upper_o5_20260730/kbuffer_run.stdout
SHA-256 8dd9cc592ead72d6dac3062f8cb917e65a7a5d8ee3dde154825b63596a1e0548
```

