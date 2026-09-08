# Independent audit of the K16 D3 two-shift and 49-facet bridge

Date: 2026-07-31  
Lane: AD  
Status: **exact finite identity and a conditional incoming-facet lemma; no all-dimension recurrence claim**

## 1. Inputs and conventions

The frozen inputs are:

```text
answers/k15.word
SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

answers/k16.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

All indices are zero based and spans are half-open. For a word `A`, define

```text
D3(A)[i] = A[i] OR A[i+1] OR A[i+2] OR A[i+3].
```

Put `W=6435`, `z=0x8000`, `T=D3(k15.word)`, and `U=D3(k16.word)`.
Direct replay gives `len(T)=6435`, `len(U)=12870`, and `T` is a
permutation of all rank-8 old-coordinate masks.

Read the `z`-marked and unmarked entries of `U` in their original order:

```text
M = [U[i] without z : z is in U[i]],
N = [U[i]           : z is not in U[i]].
```

Both have length 6435. Indices of `M,N` below are compressed occurrence
indices, not physical starts in `U`.

## 2. Exact decompositions

### Theorem 2.1 (marked row)

The first 6386 marked projections are parent owners:

```text
M[j] = T[(j+5113) mod W],   0 <= j < 1277;
M[j] = T[(j+5158) mod W],   1277 <= j < 6386.
```

Their source order is therefore

```text
5113,5114,...,6389, 0,1,...,5108.
```

The remaining 49 marked projections `M[6386:6435]` are distinct rank-7
facets. The marked physical starts in `U` are exactly

```text
[0,6390) union [12825,12870).
```

The first 6386 starts carry the rank-8 owner projections; the facets have
physical starts

```text
[6386,6390) union [12825,12870).
```

### Theorem 2.2 (unmarked row)

The unmarked row is a permutation of all of `T`:

```text
N[j] = T[(j+5112) mod W],   0 <= j < 1278;
N[j] = T[(j+5157) mod W],   1278 <= j < 6390;
N[j] = T[(j+36)   mod W],   6390 <= j < 6399;
N[j] = T[(j+6426) mod W],   6399 <= j < 6435.
```

Its source order is

```text
[5112,6390), [0,5112), [6426,6435), [6390,6426).
```

Its physical starts in `U` are `[6390,12825)`.

Every equality above is replayed entry by entry, not inferred from a
multiset. The exact rank histograms are:

```text
M projected: rank7 49,   rank8 6386
N:           rank8 6435
U:           rank8 6484, rank9 6386
```

`D3` is only the uniform four-letter diagnostic here. The optimal K16
middle schedule has variable depth, so the last histogram does not assert
that every `U[i]` is a rank-8 scheduled middle owner.

## 3. Exact meaning of 45

The parent row has the exact lower-rainbow two-cycle factor

```text
C_L = (T[0],...,T[6389]),       length 6390 = 15*426;
C_S = (T[6390],...,T[6434]),    length   45 = 15*3.
```

Every consecutive pair, including the separate closures
`T[6389]->T[0]` and `T[6434]->T[6390]`, is a Johnson edge. The 6435
cycle-edge intersections are distinct rank-7 masks, hence the complete
rank-7 palette. The short component consists of three full Z15 orbits.

There is also a direct indexing explanation. When the global output index
advances while the source traversal wraps `6389->0`, the shift in a formula
`T[(j+s) mod W]` must increase by

```text
W - len(C_L) = 6435 - 6390 = 45.
```

Indeed,

```text
5158-5113 = 45,     5157-5112 = 45.
```

The short-component wrap has the complementary shift change 6390. Thus 45
is precisely the short parent component size, not an unexplained phase
offset. What is not proved in general is why an analogous parent should
have a three-orbit short component.

## 4. Exact meaning of 49

The first 6386 marked owners use source indices

```text
[5113,6390) union [0,5109).
```

The missing parent owners are exactly

```text
S = {T[5109],T[5110],T[5111],T[5112]}
    union {T[6390],...,T[6434]}.
```

Thus `|S|=4+45=49`. Write `F[r]=M[6386+r]`.

The first four facets are the directed incoming edge colours

```text
F[r] = T[5108+r] intersect T[5109+r],   0 <= r < 4.
```

They form the four-edge path

```text
T[5108] -> T[5109] -> T[5110] -> T[5111] -> T[5112].
```

Physical position 6389 is exactly the singleton `z`. The four length-4
windows containing it start at 6386,6387,6388,6389; after deleting `z`
they are exactly these four facets. Therefore the fixture identity is

```text
49 = 45 + 4 = short-component size + D3 window arity.
```

For the other 45 facets, let

```text
p_r = 6390 + ((35+r) mod 45),
q_r = 6390 + ((36+r) mod 45),      0 <= r < 45.
```

Then

```text
F[4+r] = T[p_r] intersect T[q_r].
```

Thus the suffix facet order begins at `T[6425]->T[6426]` and traverses
every directed incoming edge of the short cycle exactly once. The 49-bank
is one four-edge path plus the complete directed lower-colour cycle of the
short component.

## 5. Canonical containment matching

Form the bipartite graph with left side the 49 facets, right side `S`, and
edge `F~T` exactly when `F` is a subset of `T`.

### Theorem 5.1

The graph has exactly 128 edges and the following solver-free perfect
matching:

```text
F[r]   -> T[5109+r],   0 <= r < 4;
F[4+r] -> T[q_r],      0 <= r < 45.
```

Containment follows from the intersection formulas. The first four images
are the four omitted long owners, while the `q_r` traverse all 45 short
owners exactly once.

The exact degree histograms are

```text
left:  degree1^1 degree2^17 degree3^31
right: degree1^1 degree2^18 degree3^29 degree4^1.
```

The incidence blocks are

```text
                              four long owners   45 short owners
four path facets                       7                 1
45 cycle facets                        0               120
```

The extra containments are unnecessary for existence; the displayed
incoming-edge assignment already proves a perfect matching.

## 6. Reusable conditional lemma

### Lemma 6.1 (incoming-facet SDR)

Let a directed Johnson 2-factor on rank-r owners have globally distinct
incoming edge intersections. For any selected owner set `S`, assign

```text
f(v) = predecessor(v) intersect v.
```

Then the `f(v)` are distinct and `f(v)` is a facet of `v`, so
`f(v)->v` is a canonical containment matching.

This is immediate from containment and the assumed global injectivity. A
lower-rainbow factor supplies the injectivity automatically. The present
fixture selects a whole 45-cycle and four consecutive owners of the long
cycle.

## 7. Scope and obstruction to generalization

The following statements are not consequences of this audit.

1. **No all-m short component.** The parent has a three-orbit component,
   but no theorem yet produces an analogous O(m)-size component in every
   dimension.
2. **No automatic literal Dd bridge.** Lemma 6.1 constructs an abstract
   facet SDR. One physical word must still realize those facets in the
   required chronology. The four singleton windows and 45 suffix windows
   are extra identities of this solved word.
3. **The form `component size + d+1` is conditional.** An interior cell is
   in `d+1` uniform `D^d` windows, but their ranks can be wrong, boundary
   truncation can intervene, and other marked cells can change the bank.
4. **No downstream conclusion.** The owner/facet matching alone does not
   preserve residence, deep upper shadows, endpoint voltage, or integral
   compiler chronology, and does not prove a new exact optimum.
5. **No uniform cut rule.** The opening indices 5112, 5113, 6426 and the
   four-owner gap are authenticated but not dimension-uniformly selected.

The reusable target exposed here is narrower: construct a lower-rainbow
parent factor with a controlled short component, then realize its
incoming-facet SDR by one literal Dd bridge while preserving downstream
rows.

## 8. Reproducible audit

```text
scratch/audit_ad_k16_d3_two_shift_49_facet_bridge_20260731.py
SHA-256 d7ebb313ca57c4a379ecbf85e829d9bd242341ea0c877812eb7c917f11d95a5a

scratch/ad_k16_d3_two_shift_49_facet_bridge_20260731.audit.json
SHA-256 e0326a3f70c8cce2ac90b1ebba4efca47ea5619a09c6d77931f5d71ca5ba26ed
payload SHA-256 40e755e5fa2a0c8c2f03564e6df378443660086afb2a8af1b8f007122dca9370
```

The script performs linear scans of the two words and one 49-by-49
containment census. It contains no search or solver.
