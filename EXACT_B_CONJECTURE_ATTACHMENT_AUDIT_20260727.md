# Audit of the exact rank-slack conjecture attachment

Date: 2026-07-27

## 1. Verified arithmetic

Let

\[
r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad
\Lambda=\sum_{j=1}^{r-1}\binom kj,
\]

and let (d) be the least nonnegative integer satisfying

\[
\Lambda\le dW+\binom{d+1}{2}.
\]

Then (B(k)=W+d).  The displayed values

\[
1,2,4,7,12,21,37,72,128,254,465,926
\]

are correct values of (B(1),\ldots,B(12)).  The value 465 at (k=11)
is **not** a certified value of \(\nu(11)\); it is the conjectural value
\(B(11)\).  Equality \(\nu(k)=B(k)\) is certified for (k\le10) and
(k=12).

The identity

\[
dW+\binom{d+1}{2}
=dB(k)-\binom d2
=\sum_{i=1}^{B(k)}\min\{d,B(k)-i+1\}
\]

is exact.  Its chains are physical endpoint chains of short intervals, not
the chains of an arbitrary SCD.

The asymptotic statement is

\[
d\sim\sqrt{\pi k/8}
\sim {1\over2}{2^k\over W}.
\]

Thus (d) is asymptotically, not exactly, half the mean Boolean-chain
length.

## 2. Correct zero-slack conclusions

### (k=6)

Here (W=20,d=1,B=21,\Lambda=21).  Equality in the lower-rank count forces
the 21 singleton intervals (the array entries) to enumerate all nonempty
sets of ranks one and two.

The further conclusion that every adjacent union has rank three uses a
second fact: every rank-three witness has length at most (d+1=2).  No
rank-three target is an entry, and there are exactly 20 adjacent intervals
for the 20 rank-three targets.  Hence the adjacent unions enumerate the
rank-three layer exactly.  Zero lower slack alone is not the whole proof.

### (k=9)

Here (W=126,d=2,B=128,\Lambda=255).  Equality forces all 255 intervals of
length one or two to enumerate every target of ranks one through four.
The central witness cap then forces the 126 length-three intervals to
enumerate rank five.

This does not by itself force 127 endpoint chains of one common
``(2 low,2 high)`` profile.  Upper witnesses can be distributed unevenly.
The verified shortest-witness distribution of the stored optimum is the
stronger safe datum: ranks one and two have respectively 9 and 36 witnesses
of length one; rank three has 83 of length one and one of length two; ranks
four through nine have respectively 126, 126, 84, 36, 9, and 1 witnesses of
lengths two through seven.

## 3. Correct (k=11) endpoint forcing

At (k=11), (W=462,d=3,B=465,\Lambda=1023).  Every lower witness has
length at most three.  Therefore:

* at least \(\lceil1023/3\rceil=341\) endpoints carry a lower witness;
* at least 94 endpoints carry three lower witnesses.

The second number follows because, respecting the first endpoint's capacity
one and the second endpoint's capacity two, a profile with no load-three
endpoint carries at most (1+2\cdot464=929) targets.  Each load-three
endpoint adds at most one beyond this baseline.  The attachment's claim that
at least 341 endpoints carry exactly three confuses the support lower bound
with the saturation lower bound.

These constraints are useful exact-search cuts, but they do not determine a
length-465 word.

## 4. The proposed recursion check

Literal two-coordinate filtering of the stored certified optima does not
recover a smaller optimum:

| source | target | minimum surviving entries | target optimum |
|---|---:|---:|---:|
| (k=9) | (k=7) | 62 | 37 |
| (k=10) | (k=8) | 130 | 72 |
| (k=12) | (k=10) | 441 | 254 |

Thus the stored constructions do not implement the simplest
(k\mapsto k+2) recursion supplied by literal coordinate deletion.  More
subtle refinement or relabeling recursions remain possible.

Canonical shortest-witness endpoint-chain profiles also differ markedly
from the punctured SCD multiplicity profile.  This rules out the naive claim
that the known optima are simply an SCD written as a word; it does not rule
out a different witness selection with SCD-like structure.

## 5. Strategic conclusion

The exact conjecture and the wreath/MWB asymptotic programme should be kept
separate.  Direct linearization of (C_m) wreaths has overhead vastly larger
than (B(k)-W(k)=\Theta(\sqrt k)).  This shows that the current direct
necklace compiler cannot attain the exact formula.  It does not prove that
every future construction using cyclic pieces must be abandoned.

The zero-slack cases are genuine positive evidence for \(\nu(k)=B(k)\), but
the corrected deductions support a modest rather than decisive confidence
increase.
