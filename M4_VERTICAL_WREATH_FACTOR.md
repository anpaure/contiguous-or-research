# A fully vertical exact wreath factor on nine coordinates

## Status

There is an exact factor of the middle layer of `Q_9` into fourteen wreaths
whose cyclic intervals collectively cover **every nonempty proper subset** of
`[9]`.  In particular, every rank-three first-shadow target occurs.  This is
the first dimension where the published Mütze--Standke--Wiechert factor is
not vertically complete, so the certificate proves that its four missing
rank-three colours are a defect of that particular factor rather than an
obstruction to all exact wreath factors.

The certificate is `m4_fully_vertical_wreath_factor.txt`; an independent
verifier is `scratch/verify_m4_vertical_wreath_factor.py`.

## 1. Definitions

For a cyclic order

\[
 \pi=(x_0,\ldots,x_8)
\]

and `1<=r<=8`, put

\[
 I_\pi(j,r)=\{x_j,x_{j+1},\ldots,x_{j+r-1}\},
 \qquad j\in\mathbb Z_9.
\tag{1.1}
\]

A family of fourteen orders is an exact middle wreath factor when its
`14*9=126` length-four intervals are precisely the members of
`binom([9],4)`, each once.

## 2. Explicit certificate

The fourteen cyclic orders are

```text
1 2 3 4 5 6 7 8 9
1 2 3 7 4 5 9 6 8
1 2 4 7 6 9 3 8 5
1 2 4 8 3 5 6 7 9
1 2 5 7 3 9 8 4 6
1 2 6 3 4 9 5 8 7
1 3 4 6 8 2 9 7 5
1 3 6 8 7 4 9 2 5
1 3 8 7 5 2 4 6 9
1 4 3 7 6 2 9 5 8
1 4 8 7 2 6 5 3 9
1 5 4 7 8 3 2 6 9
1 6 5 4 8 2 9 3 7
1 6 8 5 2 3 9 4 7
```

### Theorem 2.1 (full vertical coverage)

For the displayed family `F`,

\[
 \bigcup_{\pi\in F}\{I_\pi(j,r):j\in\mathbb Z_9\}
   =\binom{[9]}r
 \qquad(1\le r\le8).
\tag{2.1}
\]

At rank four every target occurs exactly once.  The multiplicity histograms
at ranks one through four are

\[
\begin{array}{c|l}
r&\#\{S:\operatorname{mult}(S)=t\}\text{ by }t\\ \hline
1&9\text{ at }t=14,\\
2&1,7,8,15,3,2\text{ at }t=1,2,3,4,5,6,\\
3&44,38,2\text{ at }t=1,2,3,\\
4&126\text{ at }t=1.
\end{array}
\tag{2.2}
\]

Ranks five through eight have the reversed histograms.

#### Proof

Direct enumeration of the cyclic intervals gives (2.2), whose support sizes
are respectively `9,36,84,126`, exactly the binomial rank sizes.  This proves
(2.1) through rank four.  In one cyclic order the complement of a length-`r`
interval is the opposite cyclic interval of length `9-r`.  Complementation
therefore proves ranks five through eight.  The independent verifier performs
these set comparisons literally and checks uniqueness at rank four.  QED.

## 3. Consequence for contiguous OR

For each order emit its nine singleton masks followed by its first seven
singleton masks.  Every cyclic interval of lengths one through eight is then
a physical linear interval; the first nine entries also have full union
`[9]`.  Concatenating the fourteen blocks gives a verified nonzero universal
word of length

\[
 14(9+7)=224.
\tag{3.1}
\]

The explicit word is `m4_vertical_wreath_word_224.txt`.  It is not competitive
with the known optimum `nu(9)=128`; its value is structural.  It proves that
an exact middle factor and perfect vertical coverage are compatible in the
first dimension where the standard exact factor fails.

## 4. Search provenance

`scratch/search_m4_vertical_wreath_factor.py` enumerates the
`(9-1)!/2=20,160` cyclic orders modulo rotation and reversal.  Coordinate
symmetry fixes the first displayed wreath.  Removing candidates that meet it
in a rank-four interval leaves `12,741` candidates.  The CNF uses exact-one
constraints for all 126 middle targets and coverage clauses for ranks one,
two, and three.  Its final inventory is

```text
127284 variables
343768 clauses
```

Kissat returns SAT.  Solver output is not needed to trust the result: the
fourteen-row certificate and the independent enumerator prove every claim.

## 5. Mathematical significance and limit

For `m=4`, the weak vertical wreath defect is exactly zero at every depth:

\[
 M_1=M_2=M_3=0.
\tag{5.1}
\]

This is positive evidence for the lossless multiscale wreath-factor route.
It is not an induction and does not prove that such factors exist for all
`m`.  The next mathematical target is to identify switches or a recursion
that preserves middle exactness and vertical coverage, starting from this
factor rather than the vertically defective MSW representative.

## 6. Frozen hashes

```text
043b69d3d36932925a066238fe7f8f7f692cb1a462b98ba334770f6d2caf7f4a  m4_fully_vertical_wreath_factor.txt
4fbae6ec6984336cfa09342bfd640b3d3d053b6430c10e06818162a89ed93c05  m4_vertical_wreath_word_224.txt
d78a021607a108922d57751703be1ccee79cb942a4c7e7d82755c8b6b933d928  scratch/search_m4_vertical_wreath_factor.py
76dac611a30ee5dc8cc764d97d1e0329ef488da5896539e9650ee5cff9e55a64  scratch/verify_m4_vertical_wreath_factor.py
```

## 7. Stronger follow-up certificates

Two later certificates strengthen the discovery.

First, adding the condition that no rank-three shadow colour occur more than
twice is SAT.  Since there are 126 slots and 84 colours, complete coverage
then forces the optimally balanced histogram

\[
 1^{42}2^{42}.
\]

The resulting factor and word are
`m4_balanced_vertical_wreath_factor.txt` and
`m4_balanced_vertical_wreath_word_224.txt`.

Second, `WREATH_SHADOW_SWITCH_AUDIT.md` gives a six-switch nonincreasing path
from the published MSW factor to an independently found fully vertical
factor `m4_switch_fully_vertical_wreath_factor.txt`.  Hence full verticality
is not merely present somewhere in the exact-cover space: it is reachable
from the canonical factor using the shortest exact-factor-preserving local
move, a balanced alternating eight-cycle.

The original certificate remains useful because it additionally contains the
nested fully vertical Catalan flag described in
`NESTED_VERTICAL_WREATH_FLAG.md`.
