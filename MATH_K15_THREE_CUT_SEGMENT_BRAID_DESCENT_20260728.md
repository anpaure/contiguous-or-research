# `k=15`: exact three-cut segment-braid descent

## 1. Move theorem

Let

\[
T=A\,B\,C\,D,
\qquad B=T[a:u],\quad C=T[u:v+1]
\]

be a middle-layer Johnson path, with `0<=a<u<=v<|T|`.  Consider the four
three-cut braids

\[
 ACB D,\qquad A\overleftarrow C B D,\qquad
 AC\overleftarrow B D,\qquad A\overleftarrow{BC}D.
\]

They are denoted `FF`, `RF`, `FR`, and `RR`.  Reversal transports every
internal adjacency and every internal union/intersection window without
changing its label.  Consequently:

1. the middle deck is unchanged;
2. Johnson legality needs to be checked only at the three new seams;
3. for depth `q`, the exact shadow-count delta is the multiset of new
   length-`q+1` windows crossing a new seam minus the old windows crossing an
   old cut; at most `q` starts per seam occur on either side;
4. depth-`d` residence can change only in radius-`d` seam collars.

Thus each braid has an exact `O(d+H^2)` local legality audit for residence and
protected shadows through depth `H` (or the equivalent incrementally cached
audit), while its lower compiler Hall score may
change globally because the physical erosion positions have been reordered.
This is a genuine large-neighbourhood move: it may relocate thousands of
middle vertices while changing only three seams.

The native exhaustive enumerator is
`scratch/search_k15_segment_braid_native.cpp`.  Its independent verifier is
`scratch/audit_k15_segment_braid_descent.py`.

## 2. Exact descent

Starting from the authoritative frozen Hall-29 carrier, the following chained
moves are exact:

\[
\begin{aligned}
H29&\xrightarrow{\operatorname{RF}(471,2327,5456)}H28\\
   &\xrightarrow{\operatorname{FF}(322,556,3940)}H27\\
   &\xrightarrow{\operatorname{FF}(784,1712,6357)}H26\\
   &\xrightarrow{\operatorname{FR}(3259,3823,5264)}H25.
\end{aligned}
\]

At every state:

* all `6435` rank-eight sets occur exactly once;
* every consecutive pair is Johnson-adjacent;
* depth-three residence is exact, and maximal erosion satisfies `D^3 A=T`;
* the fixed-depth upper shadows `q=1,...,7` have zero holes;
* the global upper support is all `16384` masks of ranks `8,...,15`;
* the immediate-lower support has exactly four holes;
* the seven zero-candidate lower targets remain

  \[
  2575,5801,13616,13620,17738,21641,29776.
  \]

The unmatched-rank profiles along the descent are

| Hall | unmatched rank 6 | unmatched rank 7 |
|---:|---:|---:|
| 28 | 5 | 23 |
| 27 | 5 | 22 |
| 26 | 5 | 21 |
| 25 | 5 | 20 |

The verifier reconstructs the whole chain from the frozen carrier, rather
than trusting stored aggregate statistics.

The canonical compact Hall-25 step file is
`scratch/k15_segment_braid_hall25.json`; its middle-path digest (the SHA-256
of the comma-separated decimal masks) is
`0ddee21c54e6034e91f3e5b06d6ea2cef3c3a52a55539787d91d3fe2c9287df3`.

## 3. Exact local-minimum result

Exhaustive native enumeration from the Hall-26 endpoint over every resident,
upper-safe `FF/RF/FR/RR` three-cut braid, with no immediate-lower-hole cap,
finds the Hall-25 move above.  Repeating the complete enumeration from Hall 25
gives

```text
SUMMARY johnson=551986 resident=12029 upper_safe=9233
        target=9233 best_hall=25 best_zero=7
```

Thus no single resident, upper-safe `FF/RF/FR/RR` move improves Hall
deficiency below `25`.  The minimum is not strict: the genuine nonidentity
move

```text
RF(2612,3222,3766)
```

also has deficiency `25`, zero-candidate count `7`, and the same seven-zero
set.  It loses the two lower-depth-three support targets `1801,5000`.
Accordingly H25 is a **weak** one-move minimum in this catalogue, not a
unique or strict minimum.  The native score minimizes the number of zero
candidates; it does not lexicographically compare their target masks.

The exhaustive scan is reproduced by

```sh
clang++ -O3 -DNDEBUG -std=c++20 \
  scratch/search_k15_segment_braid_native.cpp \
  -o /tmp/search_k15_segment_braid_native
/tmp/search_k15_segment_braid_native \
  scratch/k15_segment_braid_hall25.json 0 hall 6435
```

This is a catalogue-local no-go, not an obstruction to the conjecture.  A
successful next move must use at least one of:

* four or more independently movable segments;
* a composition whose intermediate state is not Hall-improving;
* a deck-changing compensated circuit;
* simultaneous movement of the carrier and physical compiler pins.

The first alternative succeeds: a neutral braid followed by an improving
braid escapes this local minimum and reaches Hall 24.  See
`MATH_K15_TWO_BRAID_DM_PORTAL_ESCAPE_20260728.md`.

## 4. What this proves and what it does not

The descent proves that shadow-safe global chronology moves can pay genuine
lower Hall deficit without damaging the already solved middle, residence, or
upper conditions.  It is the first exact monotone descent of the frozen
carrier under a large segment braid.

It does **not** give a length-6438 word.  Hall `25` is still positive.  Even a
future outer Hall score of zero would remain only a target/cell matching for
the maximal erosion unless the chosen pins satisfy the one-common-word
coordinate criterion.  The missing general Shadow--Braid theorem must therefore
construct one physical word, not merely a carrier with separate abstract
shadow matchings.

The complete H25 lower-hole vector is

\[
                         (4,19,4,1,0,0,0).
\]

Hence any coefficient-one endpoint must also enter the necessary prefix
corridor `h_1<=2`, `h_2<=h_1+3<=5`.  The exact integral continuation is now
formulated in
`THREAD_D_H25_MULTI_COLLAR_CROSS_STRATUM_CIRCULATION_20260728.md`: retained
segments are reconnected by an alternating-cycle port circulation, all H25
maximum shores are separated by one residual-DM min-cut, and the final
target assignment is tested against one common physical word.  The certified
two-braid portal `H25 -> H25 -> H24` is the first positive Hall-layer
multi-collar; its one-common-word completion remains open.
