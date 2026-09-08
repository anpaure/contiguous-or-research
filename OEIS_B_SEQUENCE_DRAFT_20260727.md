# Draft OEIS entry: the rank-slack sequence (B(k))

This is a local draft only.  It has not been submitted.

## Name

Central binomial coefficient plus the minimum interval rank slack.

## Offset

1,2

## Data

```text
1, 2, 4, 7, 12, 21, 37, 72, 128, 254, 465, 926,
1719, 3434, 6438, 12873, 24313, 48623, 92381, 184759,
352719, 705435, 1352082, 2704159, 5200304, 10400603,
20058304, 40116603, 77558764, 155117523
```

## Formula

Put

\[
r=\lceil n/2\rceil,\quad W=\binom nr,\quad
L=\sum_{j=1}^{r-1}\binom nj.
\]

Then

\[
a(n)=W+\min\left\{d\ge0:L\le dW+\binom{d+1}{2}\right\}.
\]

Equivalently,

\[
d=\left\lceil
{\sqrt{(2W+1)^2+8L}-(2W+1)\over2}
\right\rceil,qquad a(n)=W+d.
\]

## Asymptotic

\[
a(n)=\binom n{\lfloor n/2\rfloor}+\sqrt{\pi n/8}+O(1).
\]

## Comments

The sequence is the central-rank form of the rank-count lower bound for the
minimum length \(\nu(n)\) of a nonzero set-valued word whose contiguous ORs
contain every nonempty subset of \([n]\).

It is conjectured that \(\nu(n)=a(n)\).  This equality is certified for
\(n\le10\) and for \(n=12\).  The value \(a(11)=465\) is conjectural as a
value of \(\nu(11)\), not certified.

The complete scalar endpoint-chain Hall hierarchy attains exactly this same
bound; stronger lower bounds must use two-sided compatibility or the internal
OR recurrence.

## Cross-references still needed before submission

* a public definition or preprint for the universal interval-OR problem;
* links to independently checkable construction certificates;
* an OEIS keyword choice and author attribution approved by the user.

