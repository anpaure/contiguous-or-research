# Exact stage-two orientation/capacity trade for the `j3959` buffered service

Starting from the six authenticated three-defect stage-two minima in the
depth-three donor descent, the exact component cross-pair census enumerates
all local destination-exact packets of length at most eight at the two
remaining residual cuts.  For every disjoint packet pair it removes the two
source packets and destination edges, installs both packets, pairs the four
exposed source endpoints in all three perfect matchings, and audits both
orientations of every connected path.

The exact census is

```text
disjoint packet pairs                 36
balanced component graphs             36
connected endpoint pairings           72
audited path orientations             144
capacity-sufficient exact carriers      0
five-token service carriers             0
```

Every one of the 144 candidates retains the five named upper-service tokens.
The failure is an exact orientation dichotomy:

```text
orientation 1 (72/72): flats [0,2,6447], capacity 6452,
                        empty 0, bad rows 0

orientation 0 (72/72): flats [6424,12869,12871], capacity 32167,
                        empty 0, bad rows 4..12
```

Thus the component pairing itself can solve the complete maximal-envelope
geometry, but only in the orientation that moves two terminal flats to the
front and destroys the lower-layer capacity.  Reversing the path restores
more than enough capacity and the authenticated tail-flat locations, but the
best such orientation has four replay-defective rows.  This is a sharp
orientation/capacity trade, not a generic failure of the donor descent.

The best structurally perfect representative has metadata

```text
minimum 0; packet options 2,1; pairing 0; orientation 1
cuts 895,3953
source packets (2138,8,reverse) and (3288,6,forward)
flats 0,2,6447; capacity 6452; empty 0; bad 0
upper holes 20; all five named tokens retained
```

The best capacity-rich representative has

```text
minimum 3; packet options 2,1; pairing 1; orientation 0
flats 6424,12869,12871; capacity 32167
empty 0; bad 4; first bad row 1356
upper holes 25; all five named tokens retained
```

Two strictly larger but still one-break families were then closed exactly on
the structurally perfect representative:

1. all 12,873 cyclic shifts in both orientations;
2. for every one of the 12,872 breakpoints, all eight orders obtained by
   reversing either side and optionally swapping the two sides.

For cyclic shifts, 3,898 candidates have capacity at least `LAMBDA`; none is
an exact carrier and the best has 11 replay-defective rows.  For the complete
one-break endpoint-rethread family, 77,234 orders are generated, 77,218 have
exactly three flats, and 21,042 have sufficient capacity.  None is an exact
carrier; the best has 10 replay-defective rows (`cut=9585`, `kind=5`).

Consequently a repair must rethread at least two occurrence components (or
split the flat-bearing endpoint component).  Mere rotation, global reversal,
or one endpoint-component move cannot reconcile the two orientations.

Artifacts:

```text
scratch/search_k16_j3959_stage2_component_crosspair_20260730.cpp
SHA-256 3e27683d82231077397c06d58d662075a8c5e2b05a1b5d5ae5d0b3fcb235e819

scratch/k16_j3959_stage2_component_crosspair_20260730.all_audited.tsv
SHA-256 b6e4c42b502e6dca681b64f4a477436df1dadfddffe2374488cf3990aeb3f1c6

scratch/k16_j3959_stage2_component_crosspair_20260730/struct_0_2_1_0_1.targets
SHA-256 c745c7d3cec2416de5ea91789a4df128826c176ae65557ac6ac4b54c6a98ad22

scratch/k16_j3959_stage2_component_crosspair_20260730/struct_0_2_1_0_1.nodes
SHA-256 621f5fef0e3cca73c1a2e0be5813dce8941f00057c0f22de0afbd4cacbfd5dbe

scratch/k16_j3959_stage2_component_crosspair_20260730/capnear_3_2_1_1_0.targets
SHA-256 09cea7a97a002e1d2f640b8ecf3e0132a43065f1ad0c042ad576c6a6725dd957

scratch/search_k16_rotate_structural_perfect_20260730.cpp
SHA-256 83f766feae38955d5bec32cdf87a7a0211ea8a017a3217de5e0608b900c3959c

scratch/search_k16_structural_endpoint_rethread_20260730.cpp
SHA-256 0c2e3620f35f6716b437df13ed7a0e8dd93b11ca3c8d54e7f72934cf73d0c5d4

scratch/k16_j3959_stage2_component_crosspair_20260730/endpoint_rethread.audit.tsv
SHA-256 e464b9bd292fb01ec086d8cab85831862f64553fa167f7f8761f6a52c0b5a121
```

Scope: this is an exact no-go only for the six stage-two minima, their
length-eight destination-exact packet choices, all source endpoint pairings,
and the two one-break rethread families above.  It does not exclude splitting
and independently rethreading the flat-bearing component, using a different
one of the 5,166 upper-service blocks, or arbitrary multi-component
cross-pairing.
