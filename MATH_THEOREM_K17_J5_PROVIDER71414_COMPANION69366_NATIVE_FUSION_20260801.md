# K17 J5 native fusion for provider 71414 and companion 69366

Date: 2026-08-01

## Exact local repair

After hard-installing J4, unit propagation produced a DRAT-verified six-clause
core: all four remaining witnesses for provider target `71414` force cut
`(450,3)`, while that cut is prohibited because its child colour `69366` is
not otherwise priced.

The exact native repair is

```text
5878(c178,p0) -> 67318(c450,p3) -> 69238(c450,p2).
```

It is a simple rank-9 Johnson path with

```text
upper colours: 71414, 69366
lower colours: 1782, 67190.
```

The installation has the exact cut interface

```text
force: 178:1, 450:2, 450:4
forbid: 450:3.
```

The three exposed boundary children are

```text
6134, 73334, 83702,
```

with respectively `116`, `8`, and `10` authenticated rows in the
extendable-provider atlas.  The three-owner path is clipped-resident and its
two immediate palettes are collision-free.

Therefore the next joint model should remove target `71414` from the external
provider bank, should not add `69366` as a separate socket, and should install
this macro with the displayed cut pattern.

## Independent replay

The fail-closed C++ audit reads the frozen SCD component table and provider
atlas and independently verifies the source owners, ranks, Johnson edges,
palettes, clipped residence, exact cut interface, and literal support counts:

```text
scratch/audit_k17_j5_provider71414_companion69366_20260801.cpp
scratch/k17_j5_provider71414_companion69366_20260801.audit.json
```

Status:

```text
PASS_SCOPED_J5_NATIVE_FUSION
```

## Scope

This closes only the local owner/q1 propagation core.  It does not prove a
simultaneous socket/provider selection, dynamic-fragment orientation,
global path chronology, ranks 11 and above, the common-Q compiler, or a
length-24313 `k=17` word.
