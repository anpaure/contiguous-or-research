# Genuine wreath orders can have all but two GK-monochromatic phases

**Status (2026-08-21).**  An explicit pair of genuine cyclic orders has
exactly `b-2` GK-orientation-monochromatic physical phase antidiagonals.
Thus `b-o(b)` monochromaticity alone is possible and cannot be the premise
of a compiler no-go.  The monochromatic colors in this example still form
two long constant runs, so only `b/2+O(1)` of them can agree with the
persistent almost-alternating half-step word.

This is a construction for one order pair.  It neither supplies the desired
correctly alternating phases nor proves a stability theorem for all order
pairs.

## 1. The two orders

Let `b=2r+1>=5`, label both blocks by `Z_b`, and take the cyclic order

\[
 \alpha=(0,1,2,\ldots,b-3,b-1,b-2).                    \tag{1.1}
\]

Pair it with its reverse

\[
 \beta=(0,b-2,b-1,b-3,b-4,\ldots,1).                  \tag{1.2}
\]

Let `X_i` be the rank-`r` window of `alpha` ending at counter `i`, and let
`Y_j` be the rank-`r+1` window of `beta` ending at counter `j`.  Physical
phase `p` is

\[
                    \{(X_i,Y_{p-i}):i\in\mathbb Z_b\}. \tag{1.3}
\]

Write `Z_j=B\setminus Y_j`, viewed on the common coordinate labels when
computing GK orientation.  Since `beta` is the reverse of `alpha`,

\[
                         Z_j=X_{-j-1}.                 \tag{1.4}
\]

Hence phase `p` compares

\[
                         (X_i,X_{i-p-1}),qquad i\in\mathbb Z_b. \tag{1.5}
\]

## 2. Only two phases lose monochromaticity

Let `I_i={i-r+1,...,i}` be the ordinary numerical rank-`r` circular
interval.  Swapping the last two entries of the standard order changes
only two windows.  With

\[
                         e=r-2,\qquad f=2r-1,          \tag{2.1}
\]

one has

\[
 \begin{aligned}
 X_e&=I_e-\{2r\}+\{2r-1\},\\
 X_f&=I_f-\{2r-1\}+\{2r\},\\
 X_i&=I_i\quad(i\notin\{e,f\}).                      \tag{2.2}
 \end{aligned}
\]

For a source `(X,Z)`, put

\[
 D_q=|X\cap\{0,\ldots,q-1\}|-|Z\cap\{0,\ldots,q-1\}|. \tag{2.3}
\]

The even interleaved prefix heights are `2D_q`; the odd height immediately
after `A_q` is `2D_q+2 1_(q in X)-1`.  Therefore its GK top excess is odd
(`A`-first) exactly when a minimum of `D` occurs immediately before a
coordinate outside both `X` and `Z`.                         \(\tag{2.4}\)

If neither set in (1.5) is exceptional, they are simultaneous translates
of two numerical intervals.  Translation rotates the interleaved word by
an even number of coordinates and preserves the minimum parity.  The
standard/reverse calculation therefore gives color `B` for `0<=p<r` and
color `A` for `r<=p<=2r`.

It remains only to inspect rows

\[
             i\in\{e,f,e+p+1,f+p+1\},                \tag{2.5}
\]

the rows in which at least one set in (1.5) is exceptional.  Substituting
(2.2) into the prefix criterion (2.3)--(2.4) gives the following parity
table; repeated row indices are listed only once.

\[
\begin{array}{c|c|c}
p&\text{ordinary rows}&\text{exceptional-row colors}\ \\ \hline
0&B&B,A,A,B\\
1\le p\le r-1&B&B,B,B,B\\
r&A&B,A,B\\
r+1\le p\le2r&A&A,A,A,A
\end{array}                                             \tag{2.6}
\]

For completeness, (2.6) can be checked without GK terminology: scan the
two endpoint-swapped intervals in increasing coordinate order.  Away from
their four endpoints the difference prefix (2.3) is constant; its minimum
is attained before a `00` coordinate in exactly the entries marked `A`.
At `p=0` the two exceptional odd minima occur in rows `f` and `e+1`; at
`p=r` the exceptional even minima occur in rows `e` and `e+1`.  In the two
open ranges every exceptional row has the standard parity.

### Theorem 2.1 (exact near-monochromatic phase word)

For the genuine wreath-order pair (1.1)--(1.2), phases `0` and `r` are
nonmonochromatic, and every other phase is monochromatic.  More precisely,

\[
 \boxed{\displaystyle
       (*),\ B^{r-1},\ (*),\ A^r}                     \tag{2.7}
\]

is its cyclic phase word, where `*` denotes a nonmonochromatic
antidiagonal.  Thus exactly

\[
                              b-2                       \tag{2.8}
\]

of the `b` physical phases are GK-orientation monochromatic.

## 3. Why this does not compile the persistent word

Let `tau` be any odd cyclic binary word with exactly one equal-letter edge;
the persistent central half-step word has this form.  On a constant run of
length `ell`, `tau` agrees with a prescribed constant letter at most
`ceil(ell/2)` times, apart from a possible improvement of one at its unique
equal edge.  Hence, under every relative cyclic shift, the number of
correctly colored monochromatic phases in (2.7) is at most

\[
 \left\lceil{r-1\over2}\right\rceil
 +\left\lceil{r\over2}\right\rceil+1
 \le r+1={b+1\over2}.                                \tag{3.1}
\]

The integral alternating-GK retirement uses `b-O(H)` correctly colored
phase diagonals when `H=o(b)`.  Construction (1.1)--(1.2) therefore answers
the plain monochromaticity question positively but still has a linear
correct-color shortfall.

## 4. Scope of the remaining stability gate

Any decisive arbitrary-order obstruction must use the colors, not merely
the number, of the monochromatic phases.  The still-open statement is of
the following form:

> no pair of genuine cyclic orders has `b-o(b)` phase antidiagonals that
> are both GK-monochromatic and correctly colored by the persistent
> almost-alternating word.

Theorem 2.1 shows that replacing "correctly colored" by "monochromatic"
makes that statement false, even with only two exceptional phases.
