# Forced coherent ports reduce joint decoration to residual gap Hall

Date: 2026-07-31  
Status: exact fixed-cycle theorem; exhaustive finite replay on every
alternating incidence hexagon of the frozen `m=3,4` positive fixtures; no
all-`m` cycle or coherent spanning-tree existence claim

## 0. Verdict

Fix a middle-levels cycle

\[
 C=A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
\]

with upper turn word `u_i` at the `A` positions and lower turn word `ell_j`
at the `B` positions.  Let

\[
                   P_A\subseteq\mathbb Z_Q,qquad
                   P_B\subseteq\mathbb Z_Q             \tag{0.1}
\]

be positions which a proposed recursive construction requires marked.  For
example, `P_A union P_B` may be the six ports of every coherent hexagon in a
component-spanning catalogue.

There is a joint alternating Catalan decoration containing every forced
port if and only if the following conditions hold.

1. The colours `{u_i:i in P_A}` are distinct and the colours
   `{ell_j:j in P_B}` are distinct.
2. There is an upper-turn transversal `I superseteq P_A` such that every
   cyclic `I`-gap contains at most one position of `P_B`, and after deleting
   each gap containing a forced `B`-port together with that port's forced
   lower colour, the residual gap--lower-colour graph has a perfect matching.

Thus coherent-hex transparency and common-decoration selection separate
cleanly: coherence removes all local palette-transfer equations, while one
ordinary residual Hall test decides whether the union of required ports can
belong to a common joint decoration.

## 1. Exact residual graph

Write the selected upper positions cyclically as

\[
                       I=\{i_0,\ldots,i_{P-1}\}.
\]

Their `B`-position gaps are

\[
               G_t=[i_t,i_{t+1})_{\mathbb Z_Q}.       \tag{1.1}
\]

Every `B` position lies in exactly one gap.  Let `F` be the gaps which
contain a point of `P_B`.  The at-most-one condition assigns to each
`G in F` one forced lower colour `ell_j`.  Delete `F` and delete those
colours.  On the remaining gaps and remaining lower colours put an edge

\[
       G\sim L\quad\Longleftrightarrow\quad
       \ell_j=L\text{ for some }j\in G.               \tag{1.2}
\]

This is the residual gap graph.

## 2. Proof

Suppose a decoration containing the forced ports exists.  Its selected
`A` positions form an upper-turn transversal `I` containing `P_A`, so the
forced upper colours are distinct.  Alternation places exactly one selected
`B` occurrence in every cyclic `I`-gap.  Hence two forced `B` ports cannot
occupy one gap, their lower colours are distinct, and the unforced selected
`B` positions give a perfect matching of the residual graph.

Conversely, choose `I` and a residual perfect matching as in the statement.
Select the forced `B` occurrence in every deleted gap.  In every remaining
gap select an occurrence of its matched residual colour.  There is now
exactly one selected `B` position between consecutive selected `A`
positions, so the selected shore types alternate.  The forced and residual
lower colours together enumerate the whole lower alphabet once, while `I`
enumerates the upper alphabet once.  The result is the required joint
decoration.  \(\square\)

## 3. Consequence for the coherent-hex route

On a fixed factor, a proposed all-six coherent component tree may be tested
in this order:

1. take the union of its lower and upper port positions as `(P_A,P_B)`;
2. pass the forced-port theorem above;
3. use coherence to obtain palette-transparent transfer at every selected
   hexagon;
4. impose the separate gap-forest attachment, router-resilience, physical
   trace, socket/voltage and downstream compiler rows.

No per-hex SDR search remains.  The still-open constructive question is to
choose the coherent tree and the containing upper transversal together so
that the residual Hall graph and all later rows pass.

