# Exact pentagon returns for the PBBS height ladder

**Date:** 2026-08-05  
**Method:** literal cyclic-parenthesis cancellation only; no search or
computation  
**Status:** unconditional for `r >= 4`.  Every forced `M_1` exchange on the
monotone `A_h` height ladder has an explicit directed pentagon return.  For
distinct heights these pentagons are physically vertex-disjoint.  Hence the
entire height-`2` through height-`H` connector can be installed with `M_0`
fixed and with `O(H)=O(d)` changed matching-pair units.

## 1. Setup

Put

\[
                 n=2r+1,
 \qquad A_h=0\,1^h0^h(10)^{r-h},
 \qquad U_h=A_h^c .                                      \tag{1.1}
\]

For \(2\le h<r\), the desired Johnson edge between \(U_h\) and
\(U_{h+1}\)
has common lower facet

\[
 I_h=U_h\cap U_{h+1}.
\]

With the two natural PBBS matchings

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z),                 \tag{1.2}
\]

the tail edge \(U_hI_h\) already belongs to \(M_0\).  The head edge
\(I_hU_{h+1}\) forces in the contracted \(M_1\) exchange digraph the arc

\[
                  B_h\longrightarrow A_{h+1},
 \qquad B_h=A_h-\{1\}+\{h+1\}.                            \tag{1.3}
\]

The earlier survivor calculation shows that (1.3) lies in no directed
triangle, and the general PBBS theorem excludes every directed
four-cycle.  We now attain the sharp next possibility: a directed
pentagon.

## 2. The five-survivor core

Let

\[
 K_h=B_h\cap A_{h+1}
     =A_h+\{h+1\}-\{1,2h+1\}
\]

and remove the coordinate `2`:

\[
 L_h:=K_h-\{2\}
     =000\,1^{h-1}0^{h+1}(10)^{r-h-1}.                   \tag{2.1}
\]

Write

\[
 z_0=0,\qquad z_1=1,\qquad c=2,\qquad
 a=2h+1,\qquad z_2=2h+2.                                \tag{2.2}
\]

Then `L_h` has the cyclic decomposition

\[
 0_{z_0}\,0_{z_1}\,0_c\,
 (1^{h-1}0^{h-1})\,0_a\,0_{z_2}\,(10)^{r-h-1}.           \tag{2.3}
\]

Both parenthesized words are forward Dyck words.  Consequently the five
displayed zeros are exactly the five forward survivors of `L_h`.

Define five rank-`r` states

\[
\begin{aligned}
 Z_h^0&=L_h+\{c,a\}=B_h,\\
 Z_h^1&=L_h+\{z_1,c\}=A_{h+1},\\
 Z_h^2&=L_h+\{z_0,z_1\},\\
 Z_h^3&=L_h+\{z_1,z_2\},\\
 Z_h^4&=L_h+\{a,z_2\}.
\end{aligned}                                             \tag{2.4}
\]

### Lemma 2.1 (the forward survivor cycle)

The forward survivors of the five states are respectively

\[
 p_+(Z_h^0)=z_1,\quad
 p_+(Z_h^1)=z_0,\quad
 p_+(Z_h^2)=z_2,\quad
 p_+(Z_h^3)=a,\quad
 p_+(Z_h^4)=c.                                             \tag{2.5}
\]

#### Proof

Cancel the two Dyck blocks in (2.3).  On the remaining cyclic five-set,
the selected pairs in (2.4) are

\[
             23,\quad12,\quad01,\quad14,\quad34.
\]

Their reduced binary words and unique forward survivors are

\[
\begin{array}{c|ccccc}
\text{pair}&23&12&01&14&34\\ \hline
\text{word}&00110&01100&11000&01001&00011\\
\text{survivor}&1&0&4&3&2.
\end{array}
\]

Re-expanding the cancelled Dyck blocks gives (2.5). \(\square\)

It follows immediately from (2.4)--(2.5) that all five arrows

\[
 Z_h^0\longrightarrow Z_h^1\longrightarrow Z_h^2
 \longrightarrow Z_h^3\longrightarrow Z_h^4
 \longrightarrow Z_h^0                                      \tag{2.6}
\]

satisfy the incidence part of the PBBS exchange test.  The first arrow is
exactly (1.3).

## 3. Every arrow avoids `M_0`

For a candidate exchange arrow

\[
 X=Z-\{x\}+\{p_+(Z)\},                                    \tag{3.1}
\]

the new incidence collides with `M_0` exactly when

\[
                         p_-(X)=x.                         \tag{3.2}
\]

Indeed, the new lower endpoint is `f(Z)=Z^c-p_+(Z)`, whereas

\[
 f^{-1}(X)=X^c-p_-(X)
          =Z^c-p_+(Z)+\{x\}-\{p_-(X)\}.
\]

The two are equal precisely under (3.2).

The deleted labels around (2.6) are

\[
                    a,\quad c,\quad z_0,\quad z_1,\quad z_2.       \tag{3.3}
\]

The literal words of the five targets are

\[
\begin{array}{c|l}
Z_h^1&0\,1^{h+1}0^{h+1}(10)^{r-h-1}\\
Z_h^2&110\,1^{h-1}0^{h+1}(10)^{r-h-1}\\
Z_h^3&010\,1^{h-1}0^h1(10)^{r-h-1}\\
Z_h^4&000\,1^{h-1}0^{h-1}11(10)^{r-h-1}\\
Z_h^0&00\,1^h0^{h-1}(10)^{r-h}.
\end{array}                                                 \tag{3.4}
\]

Reading the zero immediately following the rightmost global prefix
maximum gives the following exact table.  Put `t=r-h-1`.

\[
\begin{array}{c|c|c}
\text{target}&p_-(\text{target})&\text{deleted label}\\ \hline
Z_h^1&h+2&a=2h+1\\
Z_h^2&h+2&c=2\\
Z_h^3&h+2\ (h\ge3\text{ or }(h,r)=(2,3));\quad
       2r\ (h=2,r\ge4)&z_0=0\\
Z_h^4&h+2\ (h\ge5\text{ or }(h,r)=(4,5));\quad
       2r\ (h=4,r\ge6);\quad
       2r\ (h\in\{2,3\},t\ge1);\quad
       0\ (h\in\{2,3\},t=0)&z_1=1\\
Z_h^0&h+2\ (h\ge3);\quad 2r\ (h=2)&z_2=2h+2.
\end{array}                                                 \tag{3.5}
\]

For completeness, these cases follow directly from the peak heights in
(3.4).  For `Z_h^3`, the central peak has height `h-2`, while the
alternating tail has peak zero.  For `Z_h^4`, the central peak has height
`h-4`; a nonempty alternating tail again has peak zero, and when both are
negative the initial cut is the rightmost maximum.  For `Z_h^0`, the
central peak has height `h-2`; at `h=2` the last alternating tooth is the
rightmost maximizing position.  In every case the reverse survivor is
the zero immediately after the stated rightmost peak.

Every entry in the middle column differs from its deleted label for
`r >= 4`.  In the last row with `h=2`, equality can occur only at the
isolated small pair `(r,h)=(3,2)`.  Hence:

### Theorem 3.1 (legal pentagon return)

For every \(r\ge4\) and \(2\le h<r\), (2.6) is a legal directed
pentagon in the natural PBBS \(M_1\) exchange digraph.  It contains the
forced ladder arc \(B_h\longrightarrow A_{h+1}\).

## 4. Simultaneous disjoint returns

The five state families in (2.4) have distinct three-bit prefixes:

\[
\begin{array}{c|ccccc}
\text{family}&Z_h^0&Z_h^1&Z_h^2&Z_h^3&Z_h^4\\ \hline
\text{prefix}&001&011&110&010&000.
\end{array}                                                 \tag{4.1}
\]

So states in different families never coincide.  Within any one family,
the lengths of the displayed initial one- and zero-runs in (3.4) recover
`h`; hence states belonging to distinct heights never coincide either.
Therefore the pentagons (2.6) are pairwise vertex-disjoint as `h` varies.

Since \(Z\mapsto U_Z\) and \(Z\mapsto f(Z)\) are bijections, disjoint exchange
vertices give disjoint physical upper and lower vertices in the lifted
alternating Middle Levels circuits.  The switches may consequently be
performed simultaneously.

### Theorem 4.1 (the complete ladder return)

Let

\[
                    3\le H\le r.
\]

Switch the pentagons (2.6) for every `h=2,...,H-1`.  Then:

1. `M_0` is unchanged;
2. the new \(M_1\) contains every head edge \(I_hU_{h+1}\);
3. the union \(M_0\cup M_1\) contains the full alternating connector
   path
   \[
       U_2-I_2-U_3-I_3-\cdots-I_{H-1}-U_H;
   \]
4. exactly `5(H-2)` old `M_1` slots are switched;
5. relative to the `H-2` forced arcs, the completion uses exactly
   `3(H-2)` auxiliary exchange vertices and `4(H-2)` additional arcs.

In particular, taking \(H\le2d+1\) gives an \(O(d)\)-support relative PBBS
return.

#### Proof

Theorem 3.1 gives every pentagon, and (4.1) gives their disjointness.
In the pentagon for height `h`, its first arrow moves the old lower
endpoint \(f(B_h)=I_h\) to the upper endpoint \(U_{h+1}\).  This is exactly
the desired `M_1` head edge.  The `M_0` tail edge `U_h I_h` was never
changed.  Concatenating these alternating pairs gives the displayed
path.  The counts follow directly from one five-cycle per height.
\(\square\)

## 5. Consequence and exact boundary

This closes the displaced-survivor return lemma for the explicit
monotone PBBS height ladder.  The earlier lower bound of five exchange
vertices per forced arc is sharp: the bipartite-incidence girth excludes
directed two-cycles, triangles are excluded for these arcs, and the PBBS
exchange digraph has no directed four-cycle, while the pentagon above
always exists.

What this theorem supplies is the previously missing **two-colour factor
lift** of the explicit `A_h` Johnson ladder:

* the `M_0` colour is retained verbatim;
* the `M_1` colour is repaired by pairwise disjoint directed pentagons;
* the entire named connector has only `O(d)` physical support.

It does not by itself prove that the switched global factor has the
desired final component count, that every new local upper occurrence is
backed up, or that the resulting protected factor extends through all
later compiler gates.  Those global occurrence and topology statements
remain separate.  The local relative cycle-cover obstruction, however,
is completely removed.

## 6. Dependencies

The forced arc and its no-triangle calculation are in
`MATH_OBSTRUCTION_PBBS_AH_LADDER_NATURAL_MATCHING_RETURN_20260805.md`.

The PBBS exchange criterion, reverse-survivor collision test, triangle
classification, and no-directed-four-cycle theorem are developed in
`MATH_THEOREM_PBBS_HAMILTONIZATION_CONNECTOR_BOUNDARY_20260726.md` and
`MATH_THEOREM_PBBS_NO_C8_AND_LONG_PARITY_BRIDGE_20260726.md`.

The height-ladder body co-selection theorem is in
`MATH_THEOREM_PBBS_HEIGHT_LADDER_BODY_COSELECTION_20260805.md`.
