# The `D_3` whole-factor native orbit escapes the fixed-slot matching, but no single leaking pair can be port-restored by a common re-opening

**Date:** 2026-08-06  
**Method:** pure mathematics; direct cyclic-word calculation  
**Status:** unconditional base-scale theorem.  It proves an explicit twelve-move
native path from the negative pentagon factor to the positive pentagon factor
and an exact no-go for repairing any one of the four leaking companion pairs by
merely changing to one common opening.  It does **not** prove that the twelve
moves admit a common suffix suspension, a bounded cut-slide realization, or a
terminal common-cap matching.

## 1. Conventions

Write `infinity` for the distinguished omitted coordinate.  A shortest
complement-geodesic row is represented by a cyclic order of the seven symbols.
If

\[
        w=(d_1,d_2,d_3,i_1,i_2,i_3,\infty),
\]

then its fixed-`infinity` path starts at \(\{d_1,d_2,d_3\}\) and successively
replaces \(d_j\) by \(i_j\).

Two cyclic rows form a native pair when rotations of them have the form

\[
 \begin{aligned}
 r_0&=(a,b,x,c,d,y_1,y_2),\\
 r_1&=(b,d,x,a,c,y_1,y_2).
 \end{aligned}                                      \tag{1.1}
\]

The native involution replaces them by

\[
 \begin{aligned}
 r'_0&=(b,a,x,d,c,y_1,y_2),\\
 r'_1&=(d,b,x,c,a,y_1,y_2).
 \end{aligned}                                      \tag{1.2}
\]

All equalities below are equalities of cyclic words; rotations are suppressed.

## 2. A common re-opening never repairs one leaking pair

For a cyclic row \(w\) and a proposed omitted coordinate \(z\), the root after
opening at \(z\) is the three-symbol cyclic window immediately following
\(z\).  Thus a desired root determines its opening whenever it occurs as a
cyclic three-window.

The four leaking native outputs are as follows.  The last column lists exactly
where the two old roots occur among the output cyclic windows.

\[
\begin{array}{c|c|c|c|c}
\text{edge}&r'_0&r'_1&\text{old roots}&\text{occurrences in the outputs}\\ \hline
-23&(5,6,3,4,\infty,2,1)&(4,5,3,\infty,6,2,1)
    &124,125&125\subset r'_0\ (z=\infty),\quad124\subset r'_1\ (z=6)\\
-25&(\infty,3,4,1,2,6,5)&(1,\infty,4,2,3,6,5)
    &124,134&124\subset r'_0\ (z=3),\quad134\subset r'_0\ (z=\infty)\\
+43&(\infty,2,5,1,3,6,4)&(1,\infty,5,3,2,6,4)
    &125,135&135\subset r'_0\ (z=2),\quad125\subset r'_0\ (z=\infty)\\
+45&(4,6,2,5,\infty,3,1)&(5,4,2,\infty,6,3,1)
    &134,135&134\subset r'_0\ (z=\infty),\quad135\subset r'_1\ (z=6).
\end{array}                                                   \tag{2.1}
\]

There are no other occurrences of the displayed old roots in the corresponding
output rows.

### Theorem 2.1 (single-pair re-opening no-go)

No leaking output pair in (2.1) can be re-opened at one common omitted
coordinate so as to recover its old root pair.

#### Proof

For edges \(-23\) and \(+45\), the two required roots occur on different rows,
but their forced omitted coordinates are respectively \(\infty\) and \(6\).
For edges \(-25\) and \(+43\), both required roots occur on the same output row
and neither occurs on the other row.  These exhaust the cyclic three-windows,
so no common opening exists.  \(\square\)

This is stronger than the fixed-`infinity` endpoint-current obstruction.  A
single leaking pair cannot be repaired by a mere common cut change.  Any escape
must coordinate several rows, or introduce a genuine junction which changes
the physical suffix/opening interface.

## 3. The whole five-row factor has a nontrivial native orbit

Let \(\mathcal P^-\) and \(\mathcal P^+\) be the two five-row pentagon factors,
with cyclic rows

\[
\begin{array}{c|c|c}
 &\mathcal P^-&\mathcal P^+\\ \hline
1&(2,3,1,6,4,5,\infty)&(3,2,1,6,5,4,\infty)\\
2&(4,2,1,6,5,3,\infty)&(1,2,4,3,5,6,\infty)\\
3&(2,1,5,4,3,6,\infty)&(1,5,2,3,6,4,\infty)\\
4&(1,3,5,2,4,6,\infty)&(5,3,1,6,4,2,\infty)\\
5&(1,4,3,2,6,5,\infty)&(3,1,4,5,2,6,\infty).
\end{array}                                                   \tag{3.1}
\]

Starting from \(\mathcal P^-\), perform the following twelve replacements in
the displayed order.  Every line is literally (1.1) on the left and (1.2) on
the right.

\[
\begin{array}{c|c|c|c|c}
 &r_0&r_1&r'_0&r'_1\\ \hline
1&(4,3,2,6,5,\infty,1)&(3,5,2,4,6,\infty,1)
 &(3,4,2,5,6,\infty,1)&(5,3,2,6,4,\infty,1)\\
2&(4,3,6,\infty,2,1,5)&(3,2,6,4,\infty,1,5)
 &(3,4,6,2,\infty,1,5)&(2,3,6,\infty,4,1,5)\\
3&(\infty,4,2,1,6,5,3)&(4,6,2,\infty,1,5,3)
 &(4,\infty,2,6,1,5,3)&(6,4,2,1,\infty,5,3)\\
4&(\infty,4,1,5,2,3,6)&(4,2,1,\infty,5,3,6)
 &(4,\infty,1,2,5,3,6)&(2,4,1,5,\infty,3,6)\\
5&(5,\infty,2,3,1,6,4)&(\infty,1,2,5,3,6,4)
 &(\infty,5,2,1,3,6,4)&(1,\infty,2,3,5,6,4)\\
6&(5,2,1,3,6,4,\infty)&(2,6,1,5,3,4,\infty)
 &(2,5,1,6,3,4,\infty)&(6,2,1,3,5,4,\infty)\\
7&(3,5,6,4,1,\infty,2)&(5,1,6,3,4,\infty,2)
 &(5,3,6,1,4,\infty,2)&(1,5,6,4,3,\infty,2)\\
8&(3,5,4,\infty,6,2,1)&(5,6,4,3,\infty,2,1)
 &(5,3,4,6,\infty,2,1)&(6,5,4,\infty,3,2,1)\\
9&(\infty,3,6,2,4,1,5)&(3,4,6,\infty,2,1,5)
 &(3,\infty,6,4,2,1,5)&(4,3,6,2,\infty,1,5)\\
10&(\infty,6,4,2,1,5,3)&(6,1,4,\infty,2,5,3)
 &(6,\infty,4,1,2,5,3)&(1,6,4,2,\infty,5,3)\\
11&(2,\infty,1,5,4,3,6)&(\infty,4,1,2,5,3,6)
 &(\infty,2,1,4,5,3,6)&(4,\infty,1,5,2,3,6)\\
12&(2,1,4,5,3,6,\infty)&(1,3,4,2,5,6,\infty)
 &(1,2,4,3,5,6,\infty)&(3,1,4,5,2,6,\infty).
\end{array}                                                   \tag{3.2}
\]

At every line, the two old rows occur in the current five-row factor produced
by the preceding lines.  Replacing them by the two new rows preserves the
complete middle-owner multiset, because it is a native pair trade.

### Theorem 3.1 (whole-factor native phase path)

The twelve native moves (3.2) transform \(\mathcal P^-\) exactly into
\(\mathcal P^+\).

#### Proof

Each line is checked by substituting its first row into
\((a,b,x,c,d,y_1,y_2)\): its second row is
\((b,d,x,a,c,y_1,y_2)\), and the two output rows are precisely (1.2).
Sequential cancellation of unchanged rows leaves after line 12 exactly the
five cyclic rows in the right column of (3.1).  \(\square\)

Thus the fixed-slot result saying that every individual native state component
is an isolated involution does **not** extend to the full five-row factor.  A
move changes which other row pairs are native, and the resulting dynamic
factor orbit contains a nontrivial phase transition.

## 4. Endpoint currents close only at the whole-factor scale

Opening every intermediate row at the original `infinity`, the old and new
root pairs in the twelve moves are

\[
\begin{array}{c|c|c}
 &\text{old roots}&\text{new roots}\\ \hline
1&135,134&135,134\\
2&135,125&145,135\\
3&135,124&356,126\\
4&145,356&125,236\\
5&125,123&235,125\\
6&125,126&125,126\\
7&125,235&125,235\\
8&126,125&125,123\\
9&125,236&145,246\\
10&235,246&135,124\\
11&124,145&125,124\\
12&134,124&134,124.
\end{array}                                                   \tag{4.1}
\]

The signed sum of the twelve endpoint currents is zero.  This follows either
by direct cancellation in (4.1), or because the initial and final factors have
the same fixed-`infinity` root multiset

\[
                   \{123,124,125,134,135\}.                  \tag{4.2}
\]

Hence there is no aggregate **base endpoint** obstruction to packaging the
twelve moves as one macro transition.

## 5. Exact remaining lift gate

The base theorem is not yet a suffix theorem.  Existing common-tail suspension
requires the fresh deletion and insertion banks to occupy compatible common
gaps of both rows.  Only the previously authenticated sealed alignments are
known to satisfy that condition automatically.  The path (3.2) deliberately
passes through alignments in which `infinity` moves among the active positions;
base endpoint cancellation therefore does not imply cancellation of every
proper suffix state or arbitrary-width interval current.

The remaining statement is now precise.

> **Bounded whole-factor cut-slide lemma.**  Lift the twelve base moves (3.2)
> through one common protected suffix, possibly using a bounded opening/pivot
> interface, so that all intermediate tail currents telescope and the final
> physical charge is bounded independently of the suffix depth.

A proof would supply the dynamic slot missing from the fixed-slot native
groupoid.  A no-go would have to exhibit a tail/current invariant of the entire
twelve-move word, not merely of one leaking edge.  The single-pair re-opening
theorem shows that a successful lift cannot be obtained by independently
re-cutting each leak.
