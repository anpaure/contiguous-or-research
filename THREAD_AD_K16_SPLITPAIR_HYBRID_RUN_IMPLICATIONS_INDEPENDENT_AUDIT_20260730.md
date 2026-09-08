# Independent audit: K16 split-pair hybrid run implications

Date: 2026-07-30  
Status: **PASS; polynomial certificate closes the five unenumerated canonical
lattices, and the canonical lattice is WLOG for frozen-catalogue pointwise
`A/B` multiset-preserving hybrids**

## 1. Frozen artifacts

```text
MATH_THEOREM_AD_K16_SPLITPAIR_HYBRID_RUN_IMPLICATION_COLLAPSE_20260730.md
SHA256 24b75cfb241a7688c09fa26a219f30db6745780cd3c07cc0c0a52d7a8eaddaf0

scratch/audit_ad_k16_splitpair_hybrid_run_implications_20260730.py
SHA256 56ae3c146c41d43de65c0b65ddf8ae67ab99b3f7f7b28a787994e0445c6fdac1

scratch/ad_k16_splitpair_hybrid_run_implications_20260730.audit.json
SHA256 111ae02e333d410a52b72ac0ce56a88c99fe4947bf79dbb091cdddbf8e8c747e
payload 8cd03159e511893e26468e09c4219b59ae7eb1f12db2f29a00ef4999f87b40d8
```

The payload digest was independently recomputed after removing its own
`payload_sha256` field.  All eight endpoint hashes match the authenticated
inputs.

## 2. Independently checked logic

### 2.1 Literal encoding

At a position owned by assignment cycle `C`, the bit in the hybrid is

```text
0 or 1                         if A and B agree,
x_C                            if (A_bit,B_bit)=(0,1),
1-x_C                          if (A_bit,B_bit)=(1,0).
```

The generator's string traces `xC` and `~xC` implement exactly this rule.
Every stored selected witness was replayed directly from the two physical
endpoint rows; its affine trace, hexadecimal row values, variable list,
bad assignment, coordinate, and resulting `0,1^ell,0` trace all agree.

### 2.2 Short-run implication orientation

All selected windows lie in positions 1986 through 5938, before the first
depth drop at 6320.  For a positive run `[s,t]` of length at most three,
bounded by zeros, every four-row intersection supporting a positive target
row crosses one of those zeros.  Hence no maximal-envelope cell contains
that coordinate, and exact middle reconstruction fails.

A witness which becomes `0,1^ell,0` at `(x_C,x_D)=(1,0)` therefore forbids
that assignment and proves

\[
x_C\le x_D,
\]

that is, the directed implication `C -> D`.  The stored orientation is
correct in every selected row.  Its windows are robust because only the two
listed cycle variables occur in them.

### 2.3 SCC conclusion

The independent replay rebuilt *all* robust two-variable arcs by the same
declared polynomial window definition, then recomputed SCCs without using
the target's SCC routine.  It also verified that the **selected** inward and
outward arborescence edges alone recover the stored SCC partition.

| pair | cycles | robust arcs | SCC sizes | selected tree windows | result |
|---|---:|---:|---|---:|---|
| 151/282 | 26 | 153 | 26 | 50 | all switches equal |
| 155/282 | 23 | 133 | 23 | 44 | all switches equal |
| 178/282 | 24 | 143 | 24 | 46 | all switches equal |
| 231/282 | 26 | 157 | 19,7 | 48 | quotient bridge closes |
| 233/282 | 21 | 98 | 21 | 40 | all switches equal |

In a strongly connected implication graph, a `1` switch reaches every
switch, so no `0` switch can coexist with it.  Thus only all zero and all one
remain.

For 231/282 the SCCs are exactly `0..18` and `19..25`.  The stored robust
arc `2 -> 19` has coordinate `0008`, half-open window `[3844,3847)`, and
trace `~x2,1,x19`; it excludes quotient assignment `(1,0)`.  The remaining
mixed assignment `(0,1)` gives coordinate `0400` trace

```text
x4,1,1,~x1,~x19 = 0,1,1,1,0
```

on `[3842,3847)`, because cycles 1 and 4 lie in the first SCC and cycle 19
in the second.  This is a genuine length-three positive run and excludes the
last mixed quotient state.

## 3. Cycle census, flat schedule, and WLOG scope

An independent occurrence parser reproduced all 28 cycle counts, including
the five large counts `26,23,24,26,21`.  Every nontrivial cycle position is
strictly before 6320.  Every endpoint has exactly the same three adjacent
repeat pairs

```text
6320/6321 = 4e71,
12869/12870 = cc63,
12871/12872 = ce61,
```

and exact maximal-envelope replay.  A hybrid retains those flats; any new
adjacent equality creates a fourth depth decrement and is already invalid.

The target theorem and JSON state a narrower ordered-pairing scope than is
necessary for these particular inputs.  Here only `4e71`, `cc63`, and
`ce61` are duplicated, and both copies occur at the same fixed positions in
every endpoint.  Every other mask `v` is unique.  For any pointwise choice
`H_p in {A_p,B_p}`, let `s_p` say that `B_p` was chosen.  Preserving the
unique mask `v` gives

\[
1-s_{p_A(v)}+s_{p_B(v)}=1,
\]

so `s_(p_A(v))=s_(p_B(v))`.  These are exactly the equalities along the
canonical ordered-occurrence permutation; hence `s` is constant on every
canonical cycle.  Re-pairing either copy of a duplicated mask can introduce
only value-inert position cycles because `A_p=B_p` at all six such positions.

Therefore, for the frozen eight endpoints, the canonical cycle model is WLOG
among all pointwise `A/B` hybrids which preserve the complete target
multiset.  Generic repeated-value counterexamples remain relevant only when
duplicates move between endpoint positions.  The result still says nothing
about a third row value, a non-multiset-preserving braid, or another carrier.

Combining this polynomial closure of the five large pairs with the stored
endpoint-only exhaustive results for the 23 pairs with at most 16 cycles
closes all 28 frozen endpoint pairs in the stated pointwise/multiset class.

## 4. Independent replay artifacts

```text
scratch/audit_ad2_k16_splitpair_hybrid_run_implications_independent_20260730.py
SHA256 ecdb35522100e00abf5ed08a65d8b973e0b4fab1eb22295518b7703c4142e968

scratch/ad_k16_splitpair_hybrid_run_implications_20260730.independent.audit.json
SHA256 6da22a496350bdf046509760e435e7a7e5735385356f3e61fe9043ad48135da0
payload ab8116d8ed7515eaf217d1c774ab4d1fd72ce84c6786af24cd02051bd4f252af
```

The independent run took under one second, used the polynomial local-window
scan only, and did not enumerate any `2^c` assignment lattice.
