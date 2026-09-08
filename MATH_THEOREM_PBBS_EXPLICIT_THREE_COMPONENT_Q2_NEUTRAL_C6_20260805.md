# An explicit three-component q2-neutral PBBS clean C6

**Date:** 2026-08-05  
**Method:** pure forward/reverse parenthesis matching; no computation or
search  
**Status:** unconditional for `m>=6`.  This is a literal selected clean C6
whose three old edges lie on three distinct PBBS components and whose q2
effect is zero.  It proves that the common-pivot three-component atlas is
nonempty, but not that its component hypergraph contains the required
spanning loose forest.

## 1. Literal data

Work on the cyclic ground set `{0,1,...,2m}`.  Put

\[
\begin{aligned}
 H&=\{2\}\cup\{5,6,\ldots,m+2\},\\
 (a_0,a_1,a_2)&=(0,1,4),\\
 c&=m+3,\\
 K&=\{3\}\cup\{m+4,m+5,\ldots,2m\},\\
 d&=m+4.
\end{aligned}
\tag{1.1}
\]

Then `|H|=m-1`, `|K|=m-2`, and the ground set is the disjoint union

\[
 H\mathbin{\dot\cup}K\mathbin{\dot\cup}
 \{a_0,a_1,a_2,c\}.
\tag{1.2}
\]

Define

\[
 R_i=K+a_i,qquad
 P_i=K+a_i+a_{i+1},qquad
 Q_i=K+a_i+c,qquad
 L_i=P_i-d.
\tag{1.3}
\]

## 2. The old shore is literal PBBS

The deficit-three word of `H`, cut at its forward-unmatched zeros, is

\[
 0_{a_0}\,D_0\,0_{a_1}\,D_1\,0_{a_2}\,D_2,
\tag{2.1}
\]

where

\[
 D_0=\varnothing,qquad D_1=10,qquad
 D_2=1^{m-2}0^{m-2}.
\tag{2.2}
\]

Thus the forward-unmatched zeros are exactly `a_0,a_1,a_2`.  If
`Z_i=H+a_i`, the forward-survivor rule gives

\[
 f(Z_i)=K+c+a_{i+1}=Q_{i+1}.
\tag{2.3}
\]

The block heights in (2.2) are `(0,1,m-2)`.  In each of the three rotated
words obtained by flipping one `a_i`, the rightmost global maximum lies in
`D_2`; its following down-step is `c=m+3`.  More explicitly the three
regional maximum triples are

\[
 (1,1,m-3),\qquad (2,m-2,-1),\qquad(m-1,0,0).
\tag{2.4}
\]

For `m>=6` the indicated winner is strict.  Hence

\[
 r_-(Z_i)=c,qquad
 f^{-1}(Z_i)=K+a_{i+1}+a_{i+2}=P_{i+1}.
\tag{2.5}
\]

Equations (2.3)--(2.5) show that the centered PBBS factor contains all
three directed old edges

\[
                         P_i\longrightarrow Q_i.
\tag{2.6}
\]

## 3. Common companion deletion

For a middle state `P`, write `s(P)=r_-(P)`.  Since

\[
 f^{-2}(P)=P+s(P)-r_-(f^{-1}(P)),
\]

the coordinate deleted by the incoming companion row is
`r_-(f^(-1)(P))`.  Direct reverse cancellation gives the complete table

\[
\begin{array}{c|c|c|c}
i&s(P_i)&f^{-1}(P_i)&r_-(f^{-1}(P_i))\\ \hline
0&4&\{2,5,\ldots,m+3\}&m+4\\
1&5&\{0,2,6,\ldots,m+3\}&m+4\\
2&5&\{1,2,6,\ldots,m+3\}&m+4.
\end{array}
\tag{3.1}
\]

Therefore the unchanged companion q1 row at every `P_i` is exactly

\[
                         L_i=P_i-d,qquad d=m+4\in K.
\tag{3.2}
\]

## 4. All six required q1 occurrences are selected

For the old rows `R_i`, cut the deficit-three word at `c`.  The current
max-height down-steps are respectively

\[
                         a_1=1,qquad a_2=4,qquad a_0=0.
\tag{4.1}
\]

For `R_0`, the first cyclic one-run has length `m-2` and dominates all
later heights.  For `R_1`, the rightmost maximum is after the one at
coordinate `3`, hence is followed by `4`.  For `R_2`, the initial cyclic
one-run has height `m-3`, while the later two-step rise reaches only
`m-4`; it is followed cyclically by `0`.  The last strict comparison uses
`m>=6`.  Thus the max-height rule selects `P_iQ_i` for all `i`.

For the companion rows, cut at `d=m+4`.  Their rightmost maxima are followed
by

\[
                         4,qquad5,qquad5,
\tag{4.2}
\]

which are exactly the three values `s(P_i)` in (3.1).  Adjoining `d` and
the corresponding value in (4.2) gives the incoming factor edge at `P_i`.
Hence all three `L_i` occurrences are also selected.

## 5. q2 neutrality and component separation

The common-deletion criterion applies to (3.2).  Therefore replacing

\[
                         P_iQ_i\quad\hbox{by}\quad P_iQ_{i+1}
\tag{5.1}
\]

cycles the three affected q2 targets

\[
 K-d+a_0,quad K-d+a_1,quad K-d+a_2
\]

and changes no other selected q2 turn.  The switch is q1- and q2-exact.

The peak-pruning profile of the normalized center above `Z_i` is

\[
 \mathbf b+\mathbf e_{h_i+1},qquad
 \mathbf b=(2,1,\ldots,1),qquad
 (h_0,h_1,h_2)=(0,1,m-2).
\tag{5.2}
\]

These are pairwise different.  Equivalently their soliton partitions are

\[
 (m-2,1,1),qquad(m-2,2),qquad(m-1,1).
\tag{5.3}
\]

Peak-pruning profile is constant on PBBS components, so the three old
edges in (2.6) lie on three distinct factor cycles.  The clean C6 therefore
merges those three cycles into one, while preserving the selected q2
multiset exactly.

## 6. Reachability scope

Cyclic coordinate rotation gives `2m+1` literal translates of this
connector, all with the same three action profiles (5.3).  This proves a
nonempty rotation orbit of genuine three-component common-pivot
connectors.

It does **not** prove that these translates hit different component triples:
rotation can stabilize or permute PBBS components within a fixed action
sector.  Nor does it connect directly to the single-soliton sector
`(m)`.  Consequently this theorem supplies a real edge of the common-pivot
component hypergraph, but not the loose-forest expansion or the straddling
connector required to repair the rigid cycle.

