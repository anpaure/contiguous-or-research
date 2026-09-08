# Independent audit of the `k=17` marker-58 lower-rainbow two-factor

Date: 2026-08-02  
Status: **PASS**, with the exact finite scope stated below.  This audit does
not certify a chronology or an OR word.

## 1. Inputs and immutable hashes

The audit used these local artifacts:

| artifact | SHA-256 |
|---|---|
| `MATH_THEOREM_K17_MARKER_RESERVOIR_Z17_ORBIT_PACKING_20260802.md` | `bf072e7c74918ad729a14ba030e866de895444df85a5af02ecd2230357e40ee7` |
| `scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv` | `88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403` |
| `scratch/k17_marker_orbit_packing_20260802/independent.audit.json` | `28a4d4cd6e19c4c6b77a8140c85bd1fceac11421e5eea0dd8ae0e50ea8d119ab` |
| `scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv` | `0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e` |

The factor has one header and exactly `24,310` data rows.

There is one provenance qualification.  The task announcement named the
local verifier by a SHA beginning `4a729a...`, but the current checkout copy

`scratch/verify_k17_marker58_q1_extension_20260802.cpp`

hashes to

`9c79af0ea259b055c8defa443c872c170383907ff225cf4805114431514007c0`.

The latter compiles and returns the same substantive census, but it is not
the announced immutable source.  Therefore this note does not use that
source as its proof certificate.  It uses the separately written fail-closed
replay

`scratch/audit_ad_k17_marker58_q1_extension_20260802.cpp`.

## 2. Exact statement certified

### Proposition 2.1 (marker-58 lower-rainbow two-factor)

The factor file is a simple spanning two-factor of the Johnson graph
`J(17,9)` with the following properties.

1. It has exactly `24,310 = binom(17,9)` edges and uses every rank-8
   intersection colour exactly once.
2. Every one of the `24,310` rank-9 owners has degree exactly two.
3. Take the first 58 base masks in the frozen marker witness, develop each
   under all 17 cyclic shifts, and open every resulting five-cycle at type
   `3`.  The resulting `58*17=986` four-edge paths are pairwise
   vertex-disjoint.  They contain `4,930` distinct owners and `3,944`
   distinct lower-coloured edges.  The factor marks precisely these
   `3,944` edges as protected—no more and no fewer.
4. The two-factor has `1,179` connected components; its largest component
   has `16,643` vertices.
5. Its edge unions cover exactly `13,307` of the `19,448 = binom(17,10)`
   rank-10 targets.  Hence exactly `6,141` rank-10 targets are absent.  The
   rank-10 load has `11,003` repeat units and maximum load six.

The protected marker edges alone have exactly `986` distinct rank-10 unions,
`2,958` repeat units, and maximum load four.  Concretely, the four edges of
each opened marker path share its rank-10 support.  Thus protected-path
binding by itself is not an upper-q1 certificate.

## 3. Independent replay

For each row `(c,a,b,p)` the independent checker rejects unless

* `|c|=8`, `|a|=|b|=9`, and `a!=b`;
* `a intersect b=c` and `|a union b|=10`;
* `p` is literally `0` or `1`;
* the lower colour `c` has not appeared before.

It instantiates the complete rank-9 layer, accumulates endpoint degrees, and
uses a disjoint-set forest only for the final component census.  Exactly
`24,310` distinct rank-8 colours together with `24,310` rows proves the
complete lower palette; degree two at every element of the complete rank-9
layer proves spanning two-factorhood.

The protected-path check is reconstructed rather than trusted from the
factor flag.  For each of the first 58 witness bases `X` and each cyclic
shift, let

`U = D union X union V`

and form the five owners obtained by deleting, cyclically, one element of
`V`.  Opening type 3 orders them as cycle positions

`4,0,1,2,3`.

The checker builds the four literal Johnson edges along this path.  It first
proves that all 986 reconstructed paths have disjoint owner sets, then
requires equality—not merely containment—between the reconstructed edge set
and the rows carrying protected flag one.  It also compares the protected
degree map owner by owner.  This closes accidental edge omission, extra
protected rows, orientation differences, and collisions between developed
paths.

Finally, component sizes and upper-cap loads are recomputed directly from
the factor rows.  No builder state or flow certificate is imported.

The resulting machine-readable certificate is

`scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.independent_ad.audit.json`.

## 4. Exact boundary

The proposition proves an exact lower-rainbow, owner-spanning, degree-two
factor containing the 986 developed marker paths.  It does **not** prove:

* a connected component or a total owner chronology;
* physical binding of the marker theorem's occurrence-labelled source and
  buffer positions;
* residence at any depth;
* completeness at rank 10 (indeed, the exact deficit is 6,141);
* any statement at ranks 11 through 17;
* a compiler/common-cap matching;
* a universal contiguous-OR word.

Accordingly the correct status is a scope-safe positive extension theorem
for the owner/lower-q1 layer, together with a sharp negative rank-10 census.

## 5. Frozen independent artifacts

After the replay:

| artifact | SHA-256 |
|---|---|
| `scratch/audit_ad_k17_marker58_q1_extension_20260802.cpp` | `cbd643dac784fa309ba3b20a292ca426fff8eaad4f2752f8583a1ad7551a2297` |
| `scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.independent_ad.audit.json` | `518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d` |

Reproduction command:

```text
clang++ -std=c++20 -O2 -Wall -Wextra -pedantic \
  scratch/audit_ad_k17_marker58_q1_extension_20260802.cpp \
  -o /tmp/audit_ad_k17_marker58_q1_extension_20260802
/tmp/audit_ad_k17_marker58_q1_extension_20260802 \
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv \
  scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv \
  scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.independent_ad.audit.json
```

The observed terminal line is

```text
PASS edges=24310 lower=24310 protected_paths=986 protected_edges=3944 components=1179 largest=16643 rank10=13307 missing_rank10=6141
```
