# Exact ordered three-layer packing at `k=11`

## 1. Result

Let

```text
F5 = C([11],5),  F6 = C([11],6),  F7 = C([11],7),
V  = 462+462+330 = 1254.
```

For the three-antichain endpoint packing number defined in
`THREE_ANTICHAIN_ENDPOINT_PACKING.md`, one has the exact value

```text
Lambda_3(F5,F6,F7) = 1583.                         (1.1)
```

More strongly, the value `1583` is attained by selected witnesses in an
actual 463-entry contiguous-OR word.  Thus neither simultaneous endpoint
ordering, chain orientation, nor coordinate realization restricted to these
three central layers lowers the computable relaxation.

Consequently the three central ranks yield only

```text
n >= 1254-floor(1583/2) = 463,                     (1.2)
```

not `465` or `466`.  Any improvement at `k=11` must couple these ranks to
additional targets or impose global pin constraints coming from targets
outside the central three-layer factor.

## 2. Frozen rank-six path

Use the 462-term rank-six path

```text
scratch/certificates/k11_distance19/k11_allbase_r7full.txt
```

whose SHA-256 is

```text
71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f.
```

Write it as

```text
B_0,B_1,...,B_461.
```

Direct exhaustive checking gives:

1. the `B_i` are all 462 rank-six subsets of `[11]`;
2. consecutive vertices are Johnson adjacent;
3. the 461 intersections `B_i intersect B_(i+1)` are pairwise distinct
   rank-five sets;
4. the unique omitted rank-five set is `535`, and `535 subset B_0`;
5. the 461 unions `B_i union B_(i+1)` cover all 330 rank-seven sets.

These properties were already checked as input facts in the distance-19
certificate audit.  The checker accompanying this note reconstructs them
directly from the frozen path rather than trusting that earlier report.

## 3. The 463-entry central factor

Let

```text
A_0 = 535,
A_(i+1) = B_i intersect B_(i+1)       (0<=i<461),
X = B_461 setminus A_461.
```

The `A_i` are a permutation of all 462 rank-five sets.  Moreover, for
`0<=i<461`, the two sets `A_i,A_(i+1)` are distinct rank-five subsets of the
same six-set `B_i`.  Hence

```text
A_i union A_(i+1) = B_i.                            (3.1)
```

Also `X` is the one-element set encoded by the mask `4`, and

```text
A_461 union X = B_461.                              (3.2)
```

Define the word

```text
W = (A_0,A_1,...,A_461,X).                          (3.3)
```

Its explicit 463 masks are frozen in
`scratch/certificates/k11_central_567_factor.txt`, with SHA-256

```text
2f71437d1c9294a3dd886f28cdba85b2c8992696d201d569a943f37681db88a8.
```

It has length 463.  Its singleton windows contain every rank-five set.
Equations (3.1)--(3.2) say that its 462 pair windows are exactly the `B_i`,
so they contain every rank-six set exactly once.  Finally, its triple window
starting at `i` has value

```text
B_i union B_(i+1)                                   (0<=i<461),
```

where the last equality also uses (3.2).  Property 5 of the frozen path
therefore says that the triple row covers every rank-seven set.

Thus (3.3) is an actual OR realization of the complete ranks 5, 6, and 7.

## 4. Endpoint weight

Select:

* the singleton occurrence `[i,i]` for each rank-five target `A_i`;
* the pair occurrence `[i,i+1]` for each rank-six target `B_i`;
* one triple occurrence `[i,i+2]` for each of the 330 rank-seven targets.

Different rank-seven targets use different triple positions because one
physical triple has only one OR value.

The selected left endpoints occupy exactly positions `0,...,461`, so

```text
e_L = 462.
```

The selected right endpoints occupy exactly positions `0,...,462`, so

```text
e_R = 463.
```

The two-sided endpoint saving is therefore

```text
(V-e_L)+(V-e_R) = 792+791 = 1583.                  (4.1)
```

All shared-endpoint blocks are genuine inclusion chains because they arise
from nested physical intervals with the stated OR labels.  Within each rank,
the chosen intervals are noncontaining: they have common physical length
one, two, or three respectively.  Hence (4.1) is an admissible ordered
three-antichain packing and proves `Lambda_3>=1583`.

## 5. Matching upper bound

For any admissible three-family packing, let `P` be the total number of
projected edges in its three bichromatic linear forests.  The rank-five to
rank-six projection has at most

```text
462+462-1 = 923
```

edges.  Each projection involving rank seven has at most `2*330=660` edges,
because every vertex on its 330-vertex side has degree at most two.  Thus

```text
P <= 923+660+660 = 2243.                            (5.1)
```

If `S` is the endpoint saving and `D` the number of nontrivial block
incidences, the exact identity from the three-antichain theorem is

```text
D = 3S-P,
```

and `D<=2V`.  Combining this with (5.1) gives

```text
S <= floor((2V+P)/3)
  <= floor((2508+2243)/3)
   = 1583.                                          (5.2)
```

Equations (4.1) and (5.2) prove (1.1).

## 6. Reproducibility

Run

```text
python3 scratch/check_k11_central_three_layer_exact_packing.py
```

The checker independently reconstructs the word, verifies every interval OR,
checks the endpoint chain system and all bichromatic forests, and reproduces
both sides of the exact `1583` equality.
