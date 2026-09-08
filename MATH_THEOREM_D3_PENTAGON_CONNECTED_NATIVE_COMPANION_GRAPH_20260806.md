# The anchored `D_3` pentagon has connected native companion graphs

**Date:** 2026-08-06  
**Method:** direct symbolic comparison of the two displayed five-path
factors; no computation or search  
**Status:** unconditional base and suffix companion-supply theorem.  At the
base scale both phase graphs contain connected spanning trees.  Not every
displayed base edge survives a common Dyck suffix, but two disjoint edges
survive in each phase, and the union of those two transported matchings is
connected in every larger dimension.  This closes the graph premise of the
phase-switched group theorem.  The note does **not** prove guarded
state-closure, cancellation of all-width currents, or a terminal common-cap
matching.

## 1. The two pentagon phases

Use the old and new path factors from
`MATH_ATTACK_E_D3_PORT_PENTAGON_CONVEYOR_AND_PCAP_AUDIT_20260726.md`.
Writing the omitted coordinate as `infinity`, their cyclic coordinate
orders, obtained from the deletion and insertion orders of each complement
geodesic, are

\[
\begin{array}{c|c|c}
 &\mathcal P^-&\mathcal P^+\\ \hline
1&(2,3,1,6,4,5,\infty)&(3,2,1,6,5,4,\infty)\\
2&(4,2,1,6,5,3,\infty)&(1,2,4,3,5,6,\infty)\\
3&(2,1,5,4,3,6,\infty)&(1,5,2,3,6,4,\infty)\\
4&(1,3,5,2,4,6,\infty)&(5,3,1,6,4,2,\infty)\\
5&(1,4,3,2,6,5,\infty)&(3,1,4,5,2,6,\infty).
\end{array}                                                    \tag{1.1}
\]

For semilength three, a native inverse pair has, after independent cyclic
rotation and possible reversal of the two rows, the normal form

\[
 r_0=(a,b,x,c,d,y_1,y_2),\qquad
 r_1=(b,d,x,a,c,y_1,y_2).                              \tag{1.2}
\]

The three common positions are therefore `x,y_1,y_2`; the other four
positions obey the displayed active-label permutation.

## 2. A connected companion tree in the negative phase

The following aligned pairs from the negative column of (1.1) have form
(1.2).  In each line the first row is `r_0` and the second is `r_1`.

\[
\begin{array}{c|c|c}
\text{edge}&r_0&r_1\\ \hline
12&(4,5,\infty,2,3,1,6)&(5,3,\infty,4,2,1,6)\\
23&(6,5,3,\infty,4,2,1)&(5,4,3,6,\infty,2,1)\\
25&(3,\infty,4,2,1,6,5)&(\infty,1,4,3,2,6,5)\\
54&(4,3,2,6,5,\infty,1)&(3,5,2,4,6,\infty,1).
\end{array}                                                    \tag{2.1}
\]

For example, the first line uses

\[
 (a,b,c,d,x,y_1,y_2)=(4,5,2,3,\infty,1,6),
\]

and the other three lines are read identically.  Hence the negative phase
contains the companion edges

\[
                         1-2,\quad2-3,\quad2-5,\quad5-4. \tag{2.2}
\]

They form a spanning tree on the five tracked rows.

### Theorem 2.1

The native companion graph of `mathcal P^-` is connected.

#### Proof

Every line of (2.1) is literally (1.2), so every edge in (2.2) is native.
The graph (2.2) is the path-with-branch tree

\[
                         1-2-5-4,\qquad2-3,
\]

and is connected.  \(\square\)

## 3. A connected companion tree in the positive phase

The following alignments from the positive column of (1.1) are again in
normal form (1.2):

\[
\begin{array}{c|c|c}
\text{edge}&r_0&r_1\\ \hline
14&(5,4,\infty,3,2,1,6)&(4,2,\infty,5,3,1,6)\\
32&(5,2,3,6,4,\infty,1)&(2,4,3,5,6,\infty,1)\\
43&(2,7,5,3,1,6,4)&(7,1,5,2,3,6,4)\\
45&(6,4,2,\infty,5,3,1)&(4,5,2,6,\infty,3,1).
\end{array}                                                    \tag{3.1}
\]

Here `7` denotes `infinity` in the third line; it is written numerically
only to keep the cyclic alignment compact.  The active four-tuples in the
two columns are respectively `[a,b,c,d]` and `[b,d,a,c]` in every line.
Thus the positive phase contains

\[
                         1-4,\quad3-2,
                         \quad4-3,\quad4-5.             \tag{3.2}
\]

This displayed spanning subgraph is connected and differs from the
displayed tree (2.2).  No claim is made here that the two **full** companion
graphs differ; that would require excluding additional pairwise alignments.

### Theorem 3.1

Both pentagon phases contain a connected native companion spanning
subgraph.

#### Proof

The explicit normal forms (3.1) prove every edge in (3.2).  They form the
spanning tree `1-4-3-2` with the additional branch `4-5`.
The negative and positive displayed spanning trees use different edge
sets.  \(\square\)

## 4. Suffix suspension leaves two phase-switched matchings

Both tables are complete anchored `D_3` path factors and fix the five
root/complement endpoint pairs row by row.  Appending one common Dyck
complement-geodesic tail to all five rows therefore transports the two
**factor phases**: the negative cylinder is canonical, and the positive
replacement is sealed with the ambient canonical completion untouched.

That statement is weaker than persistence of a native companion alignment.
For such persistence, the fresh deletion and insertion banks must enter the
same common gaps of the two aligned rows.

Write the common fresh deletion and insertion banks as

\[
                   U=(u_1,\ldots,u_s),\qquad
                   V=(v_1,\ldots,v_s).                 \tag{4.1}
\]

Four of the base alignments extend literally to the following native normal
forms.  In the negative phase,

\[
\begin{array}{c|c|c}
12&(4,5,V,\infty,2,3,1,U,6)
   &(5,3,V,\infty,4,2,1,U,6)\\
54&(4,3,U,2,6,5,V,\infty,1)
   &(3,5,U,2,4,6,V,\infty,1),
\end{array}                                             \tag{4.2}
\]

and in the positive phase,

\[
\begin{array}{c|c|c}
14&(5,4,V,\infty,3,2,1,U,6)
   &(4,2,V,\infty,5,3,1,U,6)\\
32&(5,2,U,3,6,4,V,\infty,1)
   &(2,4,U,3,5,6,V,\infty,1).
\end{array}                                             \tag{4.3}
\]

For example, edge `12` has

\[
 X=(V,\infty),\qquad Y=(1,U,6),
\]

while edge `54` has `X=(U,2)` and `Y=(V,infinity,1)`.
Each line of (4.2)--(4.3) is exactly

\[
       (a,b,X,c,d,Y),\qquad(b,d,X,a,c,Y),              \tag{4.4}
\]

with `|X|=s+1` and `|Y|=s+2`, the required lengths for semilength
`s+3`.

The other displayed positive edges do not persist under this common cut.
In edge `43`, the relevant gaps of row 4 are `d|Y` and `a|b`, whereas
those of row 3 are `c|d` and `Y|a`; edge `45` has the analogous mismatch.
Thus a valid base normal form need not be suffix-stable.

The factor statement uses the suffix formula

\[
 P(xR)=P(x)R\ \Vert\ \overline{x}(P(R)\setminus\{R\}),
\]

together with exact base state/union ledgers and rowwise fixed endpoints.
It does not repair the two failed gap alignments, but (4.2)--(4.3) already
supply the graph needed below.

### Corollary 4.1 (connected phase union in every dimension)

The two suffix-suspended phases expose the native companion matchings

\[
             M^- =\{12,54\},\qquad M^+=\{14,32\}.      \tag{4.5}
\]

Their union is the connected path

\[
                         5-4-1-2-3.                    \tag{4.6}
\]

Thus the anchored pentagon proves, in every larger semilength, the
**connected-union graph premise** of the phase-switched companion theorem.

#### Proof

The two edges in each line of (4.5) are disjoint, so each phase supplies a
matching.  Equations (4.2)--(4.3) prove that all four edges are literal
native inverse pairs after suffixing.  Their union is (4.6). \(\square\)

## 5. Exact remaining guard

This theorem closes the literal companion-edge creation and connected-union
premises, but it does not by itself satisfy the complete phase-switched
group theorem.  That theorem still needs, for each selected companion edge,
a reusable guarded fibre supporting the
whole diagonal `A_(2m+1)` action after every preceding excursion.  A native
inverse move has a nonzero q1/all-width current, so time-zero occurrence of
a connected graph does not prove such closure.

The remaining statement is now:

> **Pentagon guarded-reuse lemma.**  Promote the four persistent edges in
> (4.5) to reusable closed excursions based in one guarded reference fibre,
> while absorbing their finite nested-rail currents and retaining one
> marked generator.

Under that lemma, the corrected phase-switched companion theorem gives
full independent row-order control and the marked q1-square atlas.  The
terminal common-cap matching remains a separate final gate.
