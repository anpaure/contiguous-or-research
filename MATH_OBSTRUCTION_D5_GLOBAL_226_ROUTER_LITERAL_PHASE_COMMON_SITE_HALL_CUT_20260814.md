# Twenty moved D5 heads have no literal phase-common site for the global C6-router atlas

**Date:** 2026-08-14  
**Status:** exact obstruction to compiling the certified flat 226-router word
directly into the frozen D5 pre/post factors using only already-present
phase-common head-shore Johnson cuts.  The algebraic 226-word and the frozen
`372 -> 1` component action both replay correctly.  Added cable/dilation
owners, a non-phase-common interface, or a different physical carrier remain
open escapes.

## 0. Outcome

The flat minimum factorization of the frozen D5 head permutation is valid:

```text
three-cycle factors                         226
logical port appearances                   678
moved logical head tokens                  477
maximum appearances of one token             3
appearance histogram              1:292, 2:169, 3:16.
```

It nevertheless cannot be planted by cutting only head-shore Johnson edges
which already occur in both frozen phases.  In the literal intersection
chronology, the 477 moved tokens have phase-common degree histogram

```text
degree 0: 20 tokens
degree 1: 457 tokens.
```

The fixed flat word asks for 26 port appearances on the 20 isolated tokens:
14 of them occur once and six occur twice.  Their available literal site
supply is zero.

More sharply, one isolated moved token already gives the one-element Hall
cut

\[
              \text{port demand}\ge 1,
              \qquad \text{phase-common site supply}=0.       \tag{0.1}
\]

This does not depend on flatness or minimality: every permutation word which
realizes the frozen target must mention every moved token at least once.
Thus no longer three-cycle word fixes the direct-site architecture.

## 1. Literal phase-common head chronology

Let `F-` be the frozen post-`T2`, pre-actuator incidence factor at `m=11`,
and let `F+` be the factor after the selected 41 alternating circuits.  A
rank-11 owner `O` of incidence degree two projects to the Johnson edge

\[
                    \{C_0,C_1\},                 \tag{1.1}
\]

on its two incident rank-12 head colours.  Call this projected edge
**phase-common** when the same unordered pair occurs through `O` in both
`F-` and `F+`.  Retain exactly those edges and call the resulting rank-12
graph `H`.

This is the literal shore on which the C6 ports for the algebraic head
three-cycles live.  Cutting an edge of `H` consumes its two rank-12 owner
occurrences.  Consequently distinct serial port sites must be distinct
edges with no reused endpoint occurrence.  In particular a logical token
which is isolated in `H` has no admissible direct cut site, before any
Johnson cross-pair, palette, q2, or residence condition is imposed.

The definition deliberately does not count a phase-common *incidence* at a
rank-11 endpoint as a site.  A C6 port splice cuts a projected Johnson edge,
which requires two rank-12 endpoint owners.  Likewise, if a rank-11 owner
keeps one incidence but changes its other head, its projected Johnson edge
is not phase-common.

## 2. A one-token certificate

Use the bit order of the frozen certificates.  One canonical witness selected
by the replay is

```text
c = 0010010101011111101100.
```

Its frozen target predecessor and image are

```text
target predecessor  1010010101011111101000
target image        0010010101011101101101.
```

Thus `c` is moved.  In the flat word it occurs once, at zero-based factor 63,
port 1.  The complete pre/post projected-edge neighbourhood is

```text
edge owner                  pre head pair
                            post head pair

0010010101011111101000      1010010101011111101000,
                            0010010101011111101001
                            --------------------------------
                            0010010101011111101100,
                            0010010101011111101001

0010010101011110101100      1010010101011110101100,
                            0010010101011111101100
                            --------------------------------
                            0010010101011111101100,
                            0010010101011110101101

0010010101011101101100      0010010101011111101100,
                            0010010101011101111100
                            --------------------------------
                            0010010101011101111100,
                            0010010101011101101101.
```

Every incident projected edge changes.  The middle rank-11 owner is a
selected owner at which `c` is the retained tail incidence while the other
head changes; the other two owners carry the old and new head roles of `c`.
Hence

\[
                         \deg_H(c)=0.              \tag{2.1}
\]

### Theorem 2.1 (minimal site Hall cut)

No product of local three-cycle routers supported on literal phase-common
strands of `H` realizes the frozen D5 head permutation.

#### Proof

If no factor of a permutation product contains `c`, then every factor fixes
`c`, so their product fixes `c`.  The frozen target does not fix `c` by the
displayed predecessor/image pair.  Therefore every realizing product has at
least one port demand at `c`.

But `(2.1)` leaves no edge of `H` on which to place even the first port for
`c`.  The singleton demand set `{c}` therefore has demand at least one and
site supply zero.  This is `(0.1)`. `square`

The obstruction is inclusion-minimal: the empty demand set is feasible,
while the singleton `{c}` is not.

## 3. Exact census and the fixed flat word

The H100 constructor rebuilds the complete canonical `m=11` factor, applies
all 42 suffix copies of `T2`, applies the selected 41 circuits, and compares
every degree-two rank-11 projected edge in the two phases.  Exactly 20 moved
heads are isolated in `H`.

Their causes split as follows:

```text
stable incidence lies at another changed tail owner    17
stable incidence lies at a degree-one factor endpoint   3.
```

For the certified flat word their demand histogram is

```text
demand 1: 14 isolated tokens
demand 2:  6 isolated tokens
total:    26 unavailable port tickets.
```

The obstruction is local, not a shortage in aggregate factor size.  The
common projected graph has hundreds of thousands of edges, but none is
incident with these isolated tokens.  For the canonical flat word, even the
weaker pathwise edge-matching relaxation has 60 deficient common paths and
total deficit 72.  The theorem uses only the stronger and smaller singleton
witness of Section 2.

## 4. Independent algebra and topology replay

The independent audit imports neither the flat-word constructor nor the site
analyzer.  It separately verifies:

```text
flat product agrees with the target on all 477 tokens     yes
phase-common degree histogram                       0:20, 1:457
touched lifted components before                           372
touched lifted components after                              1
component reduction                                        371.
```

Thus the desired topology is genuinely present in the frozen 41-circuit
factor, and the flat 226-word genuinely has its advertised algebraic action.
What fails is the proposed direct occurrence compilation into already
present phase-common head-shore cuts.

## 5. Resource and residence scope

There is no 678-site occurrence schedule in this architecture.  Therefore
no assertion about simultaneous router relabellings, crossing q1/q2 decks,
or graft residence can be inferred from the failed direct schedule.  The
zero-site Hall cut precedes all of those tests; it neither contradicts nor
uses the certified internal zero-q2 and `(3,3;4,2)` residence properties of
one marked C6 router.

The exact escape is to create strand capacity before installing the router
word.  For this fixed flat certificate, the isolated tokens alone require
26 distinct new port tickets.  A valid repair must expose those tickets by
new phase-common cable/dilation occurrences (or prove a different cut-open
substitution functor), preserve their required per-token order, and only
then pass owner/q1/q2 simplicity and collar residence.  Merely refactoring
the target permutation cannot remove the universal demand in `(0.1)`.

## 6. H100 provenance

```text
site analyzer
  scratch/analyze_d5_flat226_phase_common_site_schedule_20260814.py
  SHA256 bcb5c472d71117f44236e517e6179874c78e04c678ec0b5695464673ef69dfac

site certificate
  scratch/analyze_d5_flat226_phase_common_site_schedule_20260814.h100.out
  SHA256 0c6439d236637fb2c713abe847ac3c96fc0db44ccaa85c498b7df8f684d1f333

independent replay
  scratch/audit_d5_flat226_phase_common_zero_site_obstruction_independent_20260814.py
  SHA256 649799c044ce897b2937c9bb732bfe2c41d9dfd1c4d1c2e6301872a7acf18740

independent certificate
  scratch/audit_d5_flat226_phase_common_zero_site_obstruction_independent_20260814.h100.out
  SHA256 f92bf19a0c6fbc0312817543f757d662b3b572bb7c198e956f99ecc94ce17f21

frozen flat-word certificate
  scratch/build_t2_suffix_d5_flat_minimum_c6_atlas_20260814.h100.out
  SHA256 2b7bc68cb4559696c0dcf6bc0f7464c8dbe0d7d398dfab2b0996282a7f419dcc

frozen D5 selection
  scratch/solve_t2_suffix_d5_topology_cegar_20260814.h100.out
  SHA256 94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32
```

All construction, replay, enumeration, and hashing are run via SSH on H100;
the local Mac is used only for reading, editing, transfer, and Git.
