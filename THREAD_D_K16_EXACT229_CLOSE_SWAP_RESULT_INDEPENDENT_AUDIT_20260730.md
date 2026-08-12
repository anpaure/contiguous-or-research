# Lane D: independent result audit of exact229 dynamic close swaps

Date: 2026-07-30.

## Theorem

For the authenticated exact229 chronology, no genuinely changed old-token
swap `p<->q` with `1<=q-p<=6` preserves the exact dynamic three-flat compiler
geometry.  Therefore none can repair the frozen Hall shore, irrespective of
upper coverage.

This is a complete statement for the 77,217 unordered distance-1-through-6
support-two swaps.  It is not a statement about support at least three,
non-token substitutions, or far-separated swaps whose two individually
illegal flat relocations might compensate globally.

## Authenticated production bundle

Bundle:

```text
scratch/threadD_k16_exact229_joint_close_swap_dynamic_20260730
```

The expected-input and staged-output manifests both verify completely.
Principal hashes are:

- engine source:
  `024668a446f7d24eafc3e7ba54ea544d94a63612a16d422fa0a0117440b85cd7`;
- production binary:
  `795ceb35dfecec4b18de1669f912e73af404e416ce0b385c60ffeb98fdeb4f80`;
- exact229 chronology:
  `cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974`;
- Hall audit:
  `85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0`;
- result JSON:
  `810b4af95013e415632ce301af0b14a1a7a0142cdf95d41f29b6f69ecd8d017d`.

The run completed RC0 under one H100 CPU and a 512 MiB address-space cap in
0.16 seconds, using 6,196 KiB maximum RSS.  Compilation was clean.  Its exact
ledger is

```text
spatial pairs                         77,217
equal-value unchanged pairs                3
wrong total flat count                    41
joint exact swaps                          0
fixed-flat joint exact                     0
relocated-flat joint exact                 0
```

Since no swap reaches exact geometry, `swaps.tsv` correctly contains only its
header, no Hall current is defined, and no candidate is emitted.

## Independent full replay

The independent checker does not include or call the production close-swap
engine.  For every unordered pair it swaps the two old values, then derives
from scratch over all 12,873 rows:

1. every literal adjacent equality and the total flat count;
2. the entire depth vector `3-(number of preceding flats)`;
3. every erosion envelope;
4. every linear endpoint condition;
5. every nonzero-envelope condition; and
6. every exact reconstruction equation.

It then restores the two values and checks restoration before the next pair.
Its exhaustive result is

```text
all spatial pairs                     77,217
equal-value trivial                         3
nontrivial flat-count histogram:
    one flat                                 2
    two flats                               39
    three flats                         77,173
three-flat candidates fully replayed    77,173
endpoint failures                            0
zero-envelope failures                     180
row-equation failures                   77,173
fully exact swaps                            0
```

The 180 zero-envelope failures overlap the universal row-equation failure;
they are not added to it.  The explicit first-bad-row histogram has 12,208
keys and total mass 77,173, independently confirming that every valid-flat
candidate has a concrete failed row.

Independent source SHA-256:
`ff8a718bac4b562886576ee8ef95cf6f0c4af2d485ad78c56fbc13150818102e`.
Remote audit binary SHA-256:
`c0a11b4b5f23fe2dedb43b79abd216a037d0c08e597673dc29ae0103ec95732b`.
Independent result SHA-256:
`33e2459edf29020e85883923e401ba2eb7f4af5a087861ff047ef77c65ec829b`.

This separate H100 replay completed RC0 in 10.12 seconds on one CPU under a
512 MiB cap, with maximum RSS 4,608 KiB.  Its immutable local bundle is

```text
scratch/threadD_k16_exact229_joint_close_swap_dynamic_20260730/
  independent_full_replay/
```

and its manifest is
`independent_close_swap_fullreplay.sha256`.

## Proof of the scoped no-pass

There are `sum_{d=1}^6(12873-d)=77217` unordered pairs.  The three equal-value
pairs make no change and cannot repair anything.  The independent replay
partitions every remaining pair into 41 candidates with the wrong number of
flats and 77,173 candidates with exactly three flats.  Every member of the
latter class fails an explicit reconstruction row under its literal dynamic
depth.  Thus no genuinely changed pair is compiler-exact.

The Hall shore has deficiency 25, but that gate is never reached: exact
geometry already excludes the entire class.  This result is consequently
stronger than a fixed-shore-current no-pass for the same quantified swaps.

## Exact surviving scope

Still open are mechanisms outside this census, including:

- swaps at distance at least seven whose flat changes are not separately
  legal and might compensate jointly;
- one token cycle on at least three positions with close interactions;
- several simultaneous token cycles;
- non-token substitutions, rethreads, or topology changes.

The earlier pair-cross no-pass covers the frozen-flat/individually-local-legal
minimum-separation-seven class; it should not be conflated with a dynamic-flat
no-go for every far-separated two-swap.
