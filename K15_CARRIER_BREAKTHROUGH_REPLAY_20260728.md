# k=15 carrier breakthrough: exact replay and reusable mechanism

## Frozen chain

The complete component reduction is independently replayable with
`scratch/replay_k15_breakthrough_chain.py`.  The script reconstructs every
recorded endpoint rotation and join directly from the preceding artifact and
checks exact ordered-path equality with the next artifact.  Its generated
manifest is `scratch/k15_breakthrough_chain.replay.json`.

| components | artifact | SHA-256 | q1 repeats / holes | q2 / q3 holes | path lengths |
|---:|---|---|---:|---:|---|
| 4 | `scratch/k15_lowerq_p4_q21q3_5_frontier.json` | `cee22b6e74ec1b765b3a65d0c9bfe231af0d1db156acfe412b38c350b09f8aec` | 0 / 4 | 21 / 5 | 170, 674, 828, 4763 |
| 3 | `scratch/k15_simple_p3_q21.json` | `8decd062f1d4319c486d7c61f995dc60882044355b58dc6c7f2d29b08743e341` | 0 / 3 | 21 / 5 | 180, 1769, 4486 |
| 2 | `scratch/k15_clean_p2_q24.json` | `f7cf0efa9d84b97b7f2731d6c4db4006e35f93ec84a392231bce5b7f307cf865` | 1 / 3 | 24 / 5 | 343, 6092 |
| 1 | `scratch/k15_targetpalette_p1_q28.json` | `ba96c6f81098ed73f09f861d9e55283d9374e3426604e05eab0e0c2cd5dabffe` | **1 / 2** | 28 / 5 | 6435 |

At every stage:

- depth-three residence defects are zero;
- every upper shadow at depths 1 through 7 has zero holes;
- all 6435 middle vertices occur exactly once.

## Exact move census

| transition | rotations | palette-neutral | palette-changing | join colour | colour load before join | seam type |
|---|---:|---:|---:|---:|---:|---|
| 4 -> 3 | 30 | 29 | 1 | 21809 | 0 | missing |
| 3 -> 2 | 27 | 27 | 0 | 12713 | 1 | **used bridge** |
| 2 -> 1 | 42 | 36 | 6 | 27210 | 0 | missing |

The exact seam pattern is therefore

```text
missing -> used -> missing.
```

The corresponding oriented seam endpoints and segment lengths are in the
JSON replay manifest.  In particular, the final safe join is

```text
27466 -- 27242, intersection 27210,
segment lengths 3668 + 2767 = 6435.
```

## What is structural rather than seed luck

For a path cover with `p` components, let `R` be the number of repeated
rank-seven edge-colour occurrences and `H` the number of missing rank-seven
colours.  There are exactly `W-p` internal edges and exactly `W` possible
colours, so identically

```text
H = p + R.
```

Consequently the four palette profiles above are forced by the seam types:

```text
(p,R,H): (4,0,4) -> (3,0,3) -> (2,1,3) -> (1,1,2).
```

A missing-colour join decreases both `p` and `H`.  A used-colour join
decreases `p` but increases `R`, leaving `H` unchanged.  The middle join is
therefore a one-unit **palette bridge**: allowing one repeat crosses an
endpoint obstruction without losing another colour, and the final missing
join lands exactly at the compiler-payable target `(R,H)=(1,2)`.

The rotations are not merely random reshufflings.  They preserve all upper
coverage and residence exactly while routing endpoints; 92 of 99 are also
q1-palette-neutral.  The few palette-changing rotations exchange one missing
colour for another without changing the global budget.  Across the complete
chain q3 stays at 4--5 and q2 rises only from 21 to 28.

This identifies the reusable mechanism:

1. maintain a small Pareto path cover rather than demand a Hamilton path
   immediately;
2. route endpoints with exact invariant-preserving Posa rotations;
3. allow a bounded used-colour bridge at an intermediate component count;
4. require the terminal join to use a missing colour;
5. reserve endpoint geometry and compiler Hall score as separate final
   objectives after the target palette is reached.

The remaining k=15 gap is not the carrier or palette: the frozen one-path
carrier already has the exact terminal palette.  Its two exposed compiler
cells cover neither missing q1 face, and its exact lower-compiler Hall
deficiency is 41 (40 after a strict Posa step).  Temporary palette relaxation
reaches both outer faces and Hall 38, so the live problem is coupling endpoint
repair back to the one-repeat palette and then closing Hall.
