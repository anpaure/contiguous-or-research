# Exact transport of generalized lower-provider cells under signed component moves

Fix a rank-eight source chronology `q`, a set `D` of removed source
occurrences, and a signed permutation of the maximal intervals of
`[0,n)\D`.  Each retained occurrence `x` has a unique destination `tau(x)`.
The inserted collar occurrences have no source preimage.

For a chronology `w`, let `d_i` be its forced depth and

`P_p = AND { w_i : i <= p <= i+d_i }`

be its maximal envelope.  A physical generalized lower-provider cell is a
proper-prefix interval `J=[s,s+l)`, where `1 <= l <= d_s`.

## Transport theorem

An old source cell `J=[s,s+l)` survives as an occurrence-labelled physical
right vertex if and only if

1. `J` is disjoint from `D`; and
2. its image is a legal destination prefix: if
   `K=[min tau(J), min tau(J)+l)`, then `l <= d'_min(K)`.

Condition 1 puts all occurrences of `J` in one maximal residual component.
Hence a forward or reversed component maps them bijectively onto one
contiguous interval, proving necessity and sufficiency of condition 2.
For a component `[a,b)` placed at destination `t`, the image start is

- `t+s-a` in forward orientation;
- `t+b-(s+l)` in reversed orientation.

Thus an old cell is lost exactly by deletion or by a destination phase too
small for its length.  Conversely, every resulting cell is exactly one of:

- an inherited source cell satisfying the two conditions;
- a phase-gained internal cell that was not a legal source prefix;
- a seam/collar cell whose positions do not have one consecutive source
  preimage inside one component.

## Provider-signature theorem

Physical survival does not imply unchanged lower-provider incidences.  For a
resulting cell `K`, define

- `A(K) = OR_{p in K} P'_p`;
- `M(K)` as the bits whose complete scheduled-row carrier is contained in
  `K`.

Its exact lower signature is

`Sigma(K)={S: 0<rank(S)<8, M(K) subset S subset A(K), and S intersects P'_p for every p in K}`.

Therefore a surviving old cell retains its provider incidences if and only
if this finite signature equals the signature computed at its source
interval.  This criterion is necessary and sufficient and automatically
accounts for reversal, changed phase, seam envelopes, mandatory carriers,
and source-cell losses.  Merely retaining the same row occurrences or the
same allowed OR is insufficient.

The accompanying auditor reconstructs both geometries, checks the transport
partition, and compares signatures exactly by allowed-submask enumeration.
Its scope is source-relative; it makes no unrestricted K16 claim.
