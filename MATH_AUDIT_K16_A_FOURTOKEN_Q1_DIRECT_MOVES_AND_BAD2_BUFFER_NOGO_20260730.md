# The `6a3b` direct-move quotient and the upper-complete two-defect carrier

Date: 2026-07-30

Status: **PASS exact direct-move census; one upper-complete carrier with two
adjacent replay defects; PASS scoped single-buffer no-go.  No length-12873
word is claimed.**

The authenticated input is Lane A's middle-exact four-token carrier

```text
scratch/threadA_k16_j3959_bdr_fourtoken_commutator_20260730/
  j3959.fourtoken_6a39_6b29_69a9_68e9.middle_exact.targets
```

It has capacity `32063`, no empty maximal-envelope cell, and exactly one
upper hole, the rank-nine mask `6a3b`.

## 1. The direct edge quotient is finite

Every rank-eight subset of `6a3b` occurs exactly once in the carrier.  Their
positions and omitted singleton bits are

```text
156:6a1b/0020, 463:6a2b/0010, 3196:683b/0200,
3367:6a33/0008, 3431:6a3a/0001, 3846:6a39/0002,
4401:4a3b/2000, 5075:623b/0800, 5792:2a3b/4000.
```

An interval witnessing the rank-nine target must contain an adjacent pair
of two different facets.  Therefore:

* a one-segment reversal which directly installs such an edge is one of the
  two reversals determined by a facet pair; and
* a one-row relocation which directly installs such an edge is determined
  by the moved facet, the stationary facet, and the side of insertion.

After deduplication this gives exactly `216` carrier words.  Independent
maximal-envelope and all-upper replay gives

```text
upper-complete:                 13
middle-exact:                    0
simultaneously complete:         0
```

Thus a direct installation of the missing q1 edge does not by itself close
the carrier.

## 2. The sharp bad-two carrier

The unique best upper-complete direct move reverses the segment
`[3846,4400]`, making the facets `6a39,4a3b` adjacent.  Its frozen file is

```text
scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/
  best_upper_complete_bad2.targets
SHA-256 dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d.
```

It retains the original three flat positions

```text
6320, 12869, 12871,
```

has capacity `32063`, has no empty envelope, and covers **every** upper mask.
Its complete middle error list is

```text
row 3844: target 287d, replay 286d, missing 0010;
row 3845: target 6879, replay 6869, missing 0010.
```

The defect is one binary phenomenon: the `0010` trace has the length-two run
on rows `3844,3845`, bracketed by zeroes on rows `3843,3846`.  At depth three
the run must be extended to length at least four.

## 3. No one-row swap and no single contiguous buffer

An independent occurrence swap census checks every one-row swap at row
`3846` whose incoming value contains `0010`; none is middle-exact.  The
stronger frozen C++ census moves every same-phase contiguous source block of
length `2..64`, in either orientation, immediately before row `3846`, while
protecting the `6a39--4a3b` delivery edge.

The three new joins are checked by the exact binary run law.  For every
coordinate, a new equal-bit join must have combined boundary-run length at
least four; a changed-bit join must have both terminal runs of length at
least four.  This condition is necessary and sufficient because every
internal run of each retained or reversed component is unchanged.

The exact result is

```text
oriented block placements tested: 781830
three-join survivors:                  0
```

Therefore the bad-two carrier cannot be repaired by a single contiguous
buffer block of length at most 64 within its depth-three phase.  A repair
must use at least two detached components/tokens, move a protected endpoint,
or leave this direct-move basin.

## Frozen artifacts

```text
scratch/search_root_k16_a_fourtoken_q1hole_direct_moves_20260730.py
  SHA-256 2d2de168c81a10bdf7e1f7934102480b876087500c6b1a88171384aedc1194af
scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/audit.json
  SHA-256 6f1d6bb2d5fb54b189bc3d8ac6690e971f068f795a31cde91c0453393c445644
  payload 1ed5cff60bc7e8e34ee2b6c2546225128d35916060691de1e9c317c220cb724e
scratch/search_root_k16_a_bad2_buffer_block_20260730.cpp
  SHA-256 fb95cd03d6e2ef63253f2aa9b946c177bfb86b5b5728cf20e8e76fd20d8b9106
scratch/root_k16_a_bad2_buffer_block_20260730/run.stdout
  SHA-256 8df7adeb6910f790549ff6af98013901a23e78f2641385dfb05b5e54c5b0bfed
```

Scope is exactly the declared direct reversals, direct one-row relocations,
one-row swaps at the defective seam, and same-phase single contiguous buffer
blocks of length at most 64.  It is not a global K16 no-go.
