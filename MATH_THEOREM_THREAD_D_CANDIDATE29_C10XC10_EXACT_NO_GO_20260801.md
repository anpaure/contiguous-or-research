# Candidate29 `H-C10 x D-C10`: exact palette-current no-go

Date: 2026-08-01  
Status: **proved, exhaustively and independently replayed**

## 1. Scope and frozen input

The input is the candidate29 literal factor

```text
scratch/threadD_k17_connected_debt2_repair_20260801/
  second_final.minimum_debt_second_B.factor.tsv
SHA256 aed64bc32992d65f77c4a0bcbcf9189f88d3d835295df517e8ca29f46595fb8a
```

It has one quotient cycle of length `1430`, voltage `3 mod 17`, one missing
upper rank-10 orbit `0x0355f`, and one missing lower rank-7 orbit `0x0062f`.
This theorem concerns only a simultaneous simple `H` assignment 5-cycle and
simple `D` assignment 5-cycle: a bipartite `C10 x C10` terminal move.  It
makes no claim about deeper shadows, residence, opening, source words, or the
compiler.

The exact algebraic domain, pair-rescue theorem, projected cross-square
current, overlap-rank bound, and provider clauses are proved in

```text
MATH_THEOREM_THREAD_D_CANDIDATE29_C10XC10_CURRENT_AND_OVERLAP_GATE_20260801.md
```

In particular, provisional isolated turns are formed on all masks and then
projected to the required rank.  This is essential for pair-rescued atoms,
whose isolated opposite-base trace can have rank 8 or 9.

## 2. Complete finite domain

On each side, retain every nonloop literal assignment arc, including an arc
equal to the opposite base incidence.  Enumerate every simple directed
5-cycle and identify two histories only if their complete literal terminal
maps agree.  The resulting banks have sizes

\[
                 |\mathcal B_{H,5}|=8045,
                 \qquad |\mathcal B_{D,5}|=8068.          \tag{2.1}
\]

Every simultaneous terminal state in this shell occurs exactly once in

\[
 \mathcal B_{H,5}\times\mathcal B_{D,5},
 \qquad 8045\cdot8068=64{,}907{,}060.                     \tag{2.2}
\]

For every pair, the primary checker:

1. applies the exact isolated-conflict containment test;
2. forms both final literal matchings and rejects every remaining D/H
   incidence collision;
3. recomputes the affected owner and facet turns from the simultaneous final
   state, including all overlap rectangles;
4. evaluates the exact pointwise palette-current inequalities;
5. contracts the base Hamilton cycle and computes every component and its
   literal voltage; and
6. performs a full 1430-row replay on every one-palette-safe row and every
   strict running minimum.

The containment test rejects `47,823,562` pairs.  Of the remaining
`17,083,498`, exactly `42,995` acquire a final overlap collision, leaving

\[
                         17{,}040{,}503                  \tag{2.3}
\]

terminal-valid pairs.  Exactly `100,388` of these are pair-rescued: at least
one raw side atom is invalid against the unchanged opposite side, but their
simultaneous terminal state is legal.

## 3. Exact no-go

### Theorem 3.1

No terminal-valid `H-C10 x D-C10` pair covers both immediate palettes of
candidate29.  Hence this complete simple two-circuit shell contains no
immediate palette-exact physical repair.

#### Proof

The exhaustive pointwise terminal census over (2.3) is

| property | pairs |
|---|---:|
| upper palette complete | 122 |
| lower palette complete | 114 |
| both palettes complete | **0** |

The two safe sets are therefore disjoint even before connectedness or voltage
is imposed.  Every row in their union was independently rebuilt from all
1430 literal turns.  This proves the claim.  \(\square\)

Topology is not the obstruction: `3,254,775` terminal rows are connected and
`3,088,600` are connected with nonzero voltage.  The minimum total palette
debt among connected nonzero rows is `2`, attained first at atom IDs
`(H,D)=(651,1481)`.

## 4. Current anatomy

The exact disjoint-support provider test eliminates `64,485,211` Cartesian
pairs, leaving `421,849` pairs in which both named holes are not already
excluded without a mixed owner or facet turn.  This is a sound cut, not the
no-go by itself.

Among terminal-valid pairs, classify by the terminal loads of the two
original holes:

| original holes filled | pairs |
|---|---:|
| neither | 16,711,874 |
| lower only | 188,530 |
| upper only | 135,244 |
| both | 4,855 |

Every one of the `4,855` joint-provider rows ejects other targets.  Its
minimum total terminal debt is `4`, attained twice.  Thus the obstruction is
the full palette current, not lack of raw providers.

Both assignment 5-cycles are even.  Consequently the terminal permutation
has the sign of the base 1430-cycle and its component count is odd.  The
observed component counts are exactly `1,3,5,7,9`.  This parity invariant is
valid but does not rule out connected rows.

## 5. Independent replay and resources

The independent checker does not include the primary evaluator.  It
regenerates both raw banks, forms complete terminal literal maps, directly
recounts both palette currents, verifies

\[
                  P'=\alpha_H^{-1}P\alpha_D,              \tag{5.1}
\]

contracts its own affected-tail set, and fully replays the first row of every
current/overlap profile, every running minimum, and all `236` one-palette-safe
rows.  It performs `739` full replays in total.

The independent output agrees with the primary output on all headline
counts, the complete component-count and connected-voltage histograms, all
134 joint hole-count cells, the minimum atom IDs, and the empty intersection
of the two palette-safe sets.

Both O3 executions ran on one H100 CPU process under a 2-GiB address-space
cap:

| checker | wall time | maximum RSS | exit |
|---|---:|---:|---:|
| primary | 134.33 s | 8,704 KiB | 0 |
| independent | 78.24 s | 9,216 KiB | 0 |

The first independent preflight exited before enumeration because an
optional diagnostic tried to evaluate an off-rank isolated opposite-base
turn.  It made no mathematical inference.  The frozen independent source
skips such arcs in that optional unmixed-provider counter; its terminal
enumeration always retained them and is complete.

## 6. Frozen artifacts and surviving shell

```text
scratch/threadD_k17_candidate29_c10_c10_20260801/
  audit_candidate29_c10_c10.cpp
    SHA256 93edcfe893d3ffcbe3e26e0664f565cb82b895754219f7a84c56ad2674543f7a
  primary.audit.json
    SHA256 3ad1197b5c2f6bd4418e958a0667e2248a7348a6ebd5ad9476c6dcee1635ee88
  audit_candidate29_c10_c10_independent.cpp
    SHA256 7c8f991d453f1e06d78f35d5cb65e56943b1cfbbe4ee4a192eee92dd5d187f3a
  independent.audit.json
    SHA256 c8e6189d1bfa724c82c07fe6703201dde07625edc2168d287c1cab0ad1161c59
  INDEPENDENT_RESULT.md
    SHA256 4cbb53dfad1cd44cd09629f44a4526d096af6562be8ee7d8681d3d93cc2dd134
```

The Boolean owner--facet incidence graph has no simple `C4`, so a nonphase
assignment circuit has support at least three.  At total owner support ten,
two simple two-circuit partitions therefore remain:
`C8 x C12` (assignment supports `4+6`) and `C6 x C14` (supports `3+7`), in
both H/D orientations.  The former is parity-legal because both assignment
cycles are odd permutations, so their product preserves the base sign.  In
the balanced-outward ordering after `5+5`, `C8 x C12` is therefore the next
shell; `C6 x C14` is only the next **odd-by-odd** shell.  Both must use the
same projected cross-square discipline: isolated columns are not proof-safe
at pair-rescued overlaps.
