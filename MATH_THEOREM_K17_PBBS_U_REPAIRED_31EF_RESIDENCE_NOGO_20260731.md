# Fixed repaired PBBS U-atlas: the `0x31ef` residence obstruction

## Statement

Let `scratch/k17_pbbs_u_repaired.fragments` be the audited 763-fragment
partition of the 5005 rank-nine masks on `[15]`.  No ordering and orientation
of these fixed fragments simultaneously

1. covers every upper mask by a contiguous union, and
2. has every internal positive coordinate run of length at least three.

This is a statement only about this fixed fragment atlas.  It does not rule
out a different duplicate-occurrence selection or a further re-cutting of the
PBBS streams.

## Proof

The unions of intervals lying wholly inside fragments miss 29 masks, all of
rank ten.  One is

```text
U = 0x31ef.
```

Suppose an interval in a rethreading realizes `U`.  Because `U` is not
internally realized, the interval crosses a fragment boundary.  Every
rank-nine word in that interval is a subset of `U`.  At any crossed boundary,
the adjacent words are distinct rank-nine subsets of the rank-ten set `U`, so
their union is exactly `U`.  Thus a fragment-endpoint seam with union `U` is
necessary.

There is exactly one unoriented endpoint pair with that union:

```text
0x31cf | 0x30ef = 0x31ef.
```

It yields two ordered/oriented seams, one the reversal of the other.  In both
directions, the concatenated two fragments contain the bit-7 pattern `0110`
strictly inside their concatenation.  Hence bit 7 has an internal positive run
of length two.  Adding fragments before or after cannot change that bounded
run.  The seam required for upper coverage therefore violates residence.

## Replay

```bash
python3 scratch/audit_k17_pbbs_u_repaired_31ef_residence_nogo_20260731.py \
  --output scratch/k17_pbbs_u_repaired_31ef_residence_nogo_20260731.audit.json
```

The replay exhausts all oriented endpoint pairs and asserts that there are two
ordered candidates and zero residence-safe candidates.

