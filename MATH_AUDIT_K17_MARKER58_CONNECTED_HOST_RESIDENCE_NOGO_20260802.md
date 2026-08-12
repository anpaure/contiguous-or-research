# `k=17` marker58 connected host: exact depth-three residence no-go

Date: 2026-08-02  
Status: unconditional finite audit of the connected marker58 q1/rank-ten
chronology.  The host is one physical Hamilton cycle, but no linear opening
admits a depth-three antecedent.  This is a no-go for this fixed chronology,
not for another q1/rank-ten host or a nonflat/variable-staircase construction.

## 1. Authenticated input

The factor

```text
scratch/k17_marker58_upper_q1_quotient_audit_20260802/c68b.double_fusion.factor.tsv
```

has 24,310 edges, every rank-eight facet exactly once, degree two at every
rank-nine owner, all 19,448 rank-ten caps, all 3,944 protected marker edges,
and one physical component.  Its quotient cycle has voltage four modulo 17.

The residence audit reconstructs the unique undirected physical owner cycle.
To make the exported order canonical, it starts at the least rank-nine mask
and chooses the smaller of its two neighbours.  Reversal or cyclic rotation
does not change any result below.

## 2. Exact cyclic run and gap census

Across the seventeen coordinate traces, the cycle has

```text
one-runs of length 1      0
one-runs of length 2   2873
one-runs of length 3   2499
all short one-runs     5372
```

Equivariance makes every coordinate statistic identical:

```text
one-runs per coordinate       1430
length-2 runs                  169
length-3 runs                  147
minimum / maximum one-run      2 / 71
minimum / maximum zero-gap     1 / 58
```

The absence of run length one is forced by the exact q1 palette, not an
accident of this witness.  If coordinate `x` enters at
`T_(i-1) -> T_i` and immediately leaves at `T_i -> T_(i+1)`, then both
adjacent rank-eight facets are

\[
T_{i-1}\cap T_i=T_i-\{x\}=T_i\cap T_{i+1},
\]

contradicting facet uniqueness.  Thus, inside the exact-q1 fibre, depth-three
residence debt consists precisely of length-two and length-three runs.

The complete one-run and zero-gap histograms are retained in the machine
audit rather than abbreviated here.

## 3. Every linear cut fails residence

For depth three, every internal positive carrier run must have length at
least four.  A cyclic short run can be boundary-truncated only when the cut
edge lies inside it or on one of its two flanking edges.

The audit applies this criterion to every one of the 24,310 physical cut
edges.  The exact result is

```text
legal depth-three cuts                         0
best cut edge                                 46
short internal runs remaining at best cut  5369
```

The distribution over all cuts is

| internal short runs | cut edges |
|---:|---:|
| 5369 | 272 |
| 5370 | 3417 |
| 5371 | 10965 |
| 5372 | 9656 |

Thus one cut can make at most three of the 5,372 short cyclic runs into
boundary runs.  This is not a marginal failure that can be repaired by a
better opening.

## 4. Maximal erosion at the best cut

For the canonical best cut, define the maximal source envelopes

\[
E_p=\bigcap_{\max(0,p-3)\le i\le\min(W-1,p)}T_i,
\qquad 0\le p<W+3.
\]

No envelope is empty, and their rank histogram is

```text
rank 6   21435
rank 7    2874
rank 8       2
rank 9       2
```

Nevertheless,

\[
E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}=T_i
\]

holds for only 12,670 of the 24,310 owner rows.  There are 11,640 literal
row mismatches.  Therefore `D^3 E != T`, exactly as the run audit predicts.

The exact maximal-envelope compiler graph is consequently undefined: some
required owner-coordinate occurrences have no legal envelope provider.  The
audit correctly records its raw lower census as `SKIPPED_NONRESIDENT` rather
than converting a relaxation into a compiler claim.

For diagnostics only, the envelope-only relaxation has

```text
short cells                                      72936
distinct allowed short-cell unions              40941
candidate incidences without provider guards  9702505
zero lower targets even in that relaxation       7542
```

This relaxation is already poor, but it is not the exact compiler graph and
is not used as a Hall certificate.

## 5. Mathematical consequence

The two successful cubic fusions close connectivity without worsening the
q1 or rank-ten palettes, but they do not address residence.  The connected
host therefore cannot be compiled by the flat identity

\[
D^3A=T.
\]

The next construction must do at least one of the following:

1. search the exact q1/rank-ten fibre with the short-run potential included;
2. rethread the same protected bank through a residence-aware quotient host;
3. use the variable-staircase/nonflat owner schedule rather than a flat
   depth-three carrier.

Because there are 5,372 short runs and a cut absorbs at most three, no
boundary-only repair of this cycle can work.

## 6. Frozen artifacts

```text
e885f32bab18d4f493f0cb4ed1738d5bfd71534c33c281a1859b7a6858a5c806
  scratch/audit_k17_marker58_connected_cycle_residence_compiler_20260802.cpp
a6d39ff89c9425a829eeb1b68b50dca0fbc0a4b928211ba407bce39ed33e718f
  scratch/k17_marker58_upper_q1_quotient_audit_20260802/c68b.double_fusion.residence.audit.json
02f48897bdaf6c10b134c108ec57a11b704e7736e94f9e39afeac2e03acfea47
  scratch/k17_marker58_upper_q1_quotient_audit_20260802/c68b.double_fusion.residence.cuts.tsv
6667e2e676a69ee2faf772dad2fd1a37a841fe0c0616aca43287517b843ec63c
  scratch/k17_marker58_upper_q1_quotient_audit_20260802/c68b.double_fusion.residence.cycle.tsv
```

An independently written compact run audit retained beside these artifacts
agrees on all decisive values: 5,372 cyclic short runs, best cut 46, 5,369
remaining internal short runs, no empty best-cut envelope, 11,640 `D^3`
mismatches, and the same envelope-rank histogram.

The H100 audit root is

```text
/home/amodo/or15/work/audit_quotient_k17_marker58_20260802
```

No source-state binding, lower-compiler feasibility, ranks 11--17, or
universal-word conclusion is claimed.
