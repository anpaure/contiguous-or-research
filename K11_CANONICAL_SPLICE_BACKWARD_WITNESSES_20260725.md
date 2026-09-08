# Canonical K=11 backward-splice witness metadata

This supplements
`K11_CANONICAL_CYCLIC4_SUPPORT_CLASSIFICATION_20260725.md`.
Indices are zero-based in \(\pi=(0,R,I)\), (t) is the sixth coordinate
after the tail five-window, and the candidate head is
\(S'_h=B^*\cup\{t\}\).

```text
hole     row  i   beta  t   head S'_h
0147     A9   9   10    5   01457
0169     A2   8   10    3   01369
0237     D4   9   10    5   02357
0247     D5   9   10    3   02347
0256     E9   0    4    1   01256
0257     E10  0    3    1   01257
0258     E3   0    4    1   01258
0347     A6   0    1    9   03479
0369     A5  10    1    7   03679
0469     A2   7   10    1   01469
0478     A11 10    1    5   04578
0479     A4   7   10    1   01479
047(10)  A3   7    8    1   0147(10)
0489     A5   7   10    1   01489
0569     A7   7   10    1   01569
1269     D2   1    3    8   12689
127(10)  E6   2    4    8   1278(10)
1369     A5  10    0    7   13679
136(10)  A3  10    0    5   1356(10)
1459     A13 10    0    7   14579
1469     A14 10    0    5   14569
1478     A7   1    3    2   12478
1479     A6   1    3    2   12479
2369     A3   2    5    4   23469
247(10)  A3   6    8    0   0247(10)
257(10)  A7   5    6    9   2579(10)
2589     A6   5    6   10   2589(10)
258(10)  A5   5    4    9   2589(10)
259(10)  A4   5    4    7   2579(10)
267(10)  A2   5    4    9   2679(10)
```

The two canonical holes with no backward-physical witness are

\[
\{0,2,5,10\},\qquad \{1,5,8,10\}.
\]

This last statement concerns the fixed-forward tail orientation only.
Both exceptions have genuine reverse-tail witnesses.  On a canonical
six-window \((t_0,\ldots,t_5)\), the reverse formula is

\[
B_{\rm rev}=U\setminus\{t_0,\beta\},
\qquad \beta\in\{t_3,t_4\}.
\]

- In the D4 order, the six-window
  \((7,10,0,2,3,5)\), with \(\beta=3=t_4\), gives
  \[
  B_{\rm rev}=\{0,2,5,10\},
  \qquad S'_h=\{0,2,5,7,10\}.
  \]

- In the E11 order, the six-window
  \((6,5,1,10,4,8)\), with \(\beta=4=t_4\), gives
  \[
  B_{\rm rev}=\{1,5,8,10\},
  \qquad S'_h=\{1,5,6,8,10\}.
  \]

Hence the union of forward-tail and reverse-tail backward candidates
contains all 32 canonical holes.  Forward head admissibility is a
separate test.
