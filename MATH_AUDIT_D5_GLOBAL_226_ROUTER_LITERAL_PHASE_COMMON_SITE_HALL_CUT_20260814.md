# Hostile audit of the D5 global-router literal phase-common site obstruction

**Date:** 2026-08-14  
**Verdict:** **PASS in the stated literal head-shore scope.**  The frozen
flat 226-word is algebraically correct and the selected 41-circuit factor
really has the advertised lifted `372 -> 1` action, but a direct compiler
which may cut only projected rank-12 Johnson edges already common to both
frozen phases is impossible.  A singleton moved token has site supply zero.
The result does not obstruct an added cable/dilation carrier or a different
cut-open substitution functor.

Audited source:

```text
MATH_OBSTRUCTION_D5_GLOBAL_226_ROUTER_LITERAL_PHASE_COMMON_SITE_HALL_CUT_20260814.md
```

## 1. Projection and interface convention

The source uses the correct shore for the algebraic word.  Its 477 logical
tokens are rank-12 head colours.  If a rank-11 incidence owner has two head
neighbours `C0,C1`, suppressing that owner gives the rank-12 Johnson edge
`C0--C1`.  Such an edge is phase-common exactly when the unordered pair at
that same rank-11 owner agrees before and after the D5 switch.

Two tempting weaker objects are correctly excluded.

1. A single incidence `O--C` retained in both factors is not by itself a
   projected Johnson cut site; an edge on the head-owner chronology needs
   both rank-12 endpoints.
2. A degree-one rank-11 factor endpoint also supplies no projected edge.

This is precisely why the independent audit requires a common pair of
length two.  An earlier diagnostic version which counted a common
degree-one incidence would have undercounted the obstruction by three; the
frozen replay and theorem use the corrected `20`, not `17`.

## 2. Reproduction of the zero-site cut

The constructor and the independent replay agree exactly:

```text
moved head tokens                                  477
phase-common projected degree 0                     20
phase-common projected degree 1                    457

isolated because retained incidence is at
  another changed tail owner                        17
  a degree-one canonical endpoint                    3

flat-word demand on isolated tokens
  demand one:                                       14
  demand two:                                        6
  total port tickets:                               26.
```

The complete isolated-token lists agree, not merely the aggregate counts.
The independent replay rebuilds the canonical `m=11` factor rather than
reading a site list from the constructor.

## 3. Literal witness check

For

```text
c = 0010010101011111101100
```

the replay finds three projected rank-11 edge owners in the union of the two
phase neighbourhoods.  Their pre/post head pairs are exactly the three rows
displayed in the source note, and all three pairs change.  The middle owner
retains the incidence to `c` but changes its other head; hence it is not a
phase-common projected edge.  The other two owners carry the old-only and
new-only head roles.  Therefore `deg_H(c)=0` literally.

The target sends `c` to

```text
0010010101011101101101,
```

so `c` is not fixed.  The flat word happens to use it once, at factor 63,
port 1 with zero-based indices, but the proof does not depend on that word:
any product which omits `c` fixes it.  Thus every realizing factorization
has demand at least one at `c`, while the admissible direct-site supply is
zero.  The singleton Hall cut is valid and inclusion-minimal.

## 4. Algebra and topology independence

The standalone hostile replay imports neither the flat constructor nor the
site analyzer.  It independently checks the rightmost-first product on all
477 tokens and obtains

```text
226 factors, 678 appearances, maximum exposure 3.
```

It also constructs the complete lifted factor on both shores using a
separate dense union-find traversal.  On the 477 changed owner occurrences
it obtains

```text
touched components before   372
touched components after      1
reduction                   371.
```

This separates the physical failure cleanly: neither the algebraic word nor
the desired frozen topology is wrong.

## 5. Resource and collar claims

The source makes no invalid downstream inference.  Since no literal
678-site schedule exists, it does not claim a simultaneous owner/q1/q2
palette, legal crossing Johnson pairs, or residence collars at scheduled
sites.  The obstruction occurs before those rows.  The internal
36-owner/18-owner router theorems are unaffected.

The repair statement is also correctly scoped.  The fixed flat word has 26
port demands on zero-supply tokens, so a direct repair needs 26 distinct new
port tickets there; a valid cable or dilation must then satisfy ordering,
resource simplicity, q2 equality/support, and residence.  The theorem does
not claim that adding 26 arbitrary edges is sufficient.

## 6. Bound artifacts

```text
audited obstruction note
  MATH_OBSTRUCTION_D5_GLOBAL_226_ROUTER_LITERAL_PHASE_COMMON_SITE_HALL_CUT_20260814.md
  fa90e4cab1a9ad40844e90df8c505136262d708191f903b9a7de03ca4fc8607f

site analyzer
  scratch/analyze_d5_flat226_phase_common_site_schedule_20260814.py
  bcb5c472d71117f44236e517e6179874c78e04c678ec0b5695464673ef69dfac

site output
  scratch/analyze_d5_flat226_phase_common_site_schedule_20260814.h100.out
  0c6439d236637fb2c713abe847ac3c96fc0db44ccaa85c498b7df8f684d1f333

independent replay
  scratch/audit_d5_flat226_phase_common_zero_site_obstruction_independent_20260814.py
  649799c044ce897b2937c9bb732bfe2c41d9dfd1c4d1c2e6301872a7acf18740

independent output
  scratch/audit_d5_flat226_phase_common_zero_site_obstruction_independent_20260814.h100.out
  f92bf19a0c6fbc0312817543f757d662b3b572bb7c198e956f99ecc94ce17f21
```

All substantive replay and hashing were performed via SSH on H100.
