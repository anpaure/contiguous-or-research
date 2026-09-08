# The SCD short-triangle augmenter factorizes into one Hall row, one coloured three-partite SDR, and one graphic row

Date: 2026-08-01  
Lane: fixed-`M_0` SCD short bank / tight one-to-two ears  
Status: **exact typed algebra, resource and endpoint ledger, exact integral
selection formulation, and an all-dimensional Hall theorem in the
source-to-boundary capacity-two direction.  The reverse `I_m`-demand
capacity-two row is verified through `m=12` and left as the explicit
all-cut gate.  No all-dimensional square-SDR or graphic completion is
claimed.**

## 1. Fixed matching and the two rotations

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
\]

and let `S<L=S+x` be a short central chain in the standard
Greene--Kleitman SCD of `B_G`.  Put

\[
 A=aS,\qquad B=zS,\qquad C=L.                       \tag{1.1}
\]

For the frozen four-row matching,

\[
 M_0(A)=aL,\qquad M_0(B)=azS,\qquad M_0(C)=zL.      \tag{1.2}
\]

For a rank-`m` set `U subset G`, write

\[
 P(U)=M_0^{-1}(U),                                  \tag{1.3}
\]

and, for a rank-`(m-1)` set `V subset G`, write

\[
 Q(V)=M_0^{-1}(aV).                                 \tag{1.4}
\]

Choose independently

\[
 b_0,b_1\in G-L,
 \quad U=L+b_0,
 \quad W=L+b_1,
 \quad V=S+b_1=W-x.                                \tag{1.5}
\]

The two literal tight augmentations are

\[
 C\to A
 \longmapsto
 A\to B\; +\; C\to P(U),                          \tag{1.6}
\]

and then

\[
 A\to B
 \longmapsto
 B\to C\; +\; A\to Q(V).                          \tag{1.7}
\]

Thus their composite is

\[
 \boxed{C\to A
 \longmapsto
 B\to C\to P(U)\quad\sqcup\quad A\to Q(V).}       \tag{1.8}
\]

The three upper colours are

\[
 azL,\qquad zU,\qquad aW.                          \tag{1.9}
\]

The old colour `azL` is retained.  The two newly serviced targets may be
chosen independently.  The frequently used square subcatalogue is the
restriction `b_0=b_1`, hence `U=W` and `V=U-x`.

### Theorem 1.1 (necessary and sufficient serial fixed-`M_0` typing)

Equations (1.6)--(1.8) have a literal serial physical realization in the
frozen matching if and only if:

1. the three rows (1.2), together with (1.3)--(1.4), are the actual
   `M_0` rows;
2. `b_0,b_1` lie outside `L`;
3. the residual predecessor rows `(A,M_0(A))` and `(B,M_0(B))` are free;
4. for a literal serial realization, `C->A` is an unprotected isolated
   source-to-terminal component, `B` has both ports free, `P(U),Q(V)`
   have free incoming ports, and the new colours `zU,aW` are unused by the
   retained palette; and
5. the first intermediate exchange and the final three-edge exchange are
   both graphic-independent after contracting the retained background
   forest.

Condition 3 is the lower/tail ledger.  Condition 4 includes the free
incoming ticket at `B` used by the first rotation and the free incoming
ticket at `C` used by the second; saying only that `B` is a terminal is
insufficient.  For a simultaneous final replacement which need not exist
through the intermediate state, the temporary incoming ticket at `B` may
be dropped, but all final tail/head rows and condition 5 remain.  Merely
knowing the sets in (1.5) is not enough: a free colour is not a free rooted
occurrence.

The bare Boolean set identities and colour action use only conditions 1--2;
conditions 3--5 are precisely what upgrades them to the serial physical
move.

#### Proof

For the first augmentation substitute

\[
 \widehat L=L,\quad \widehat a=z,\quad
 \widehat b=b_0,\quad \widehat c=a,\quad \widehat x=x.
\]

For the second substitute

\[
 \widehat L=aS,\quad \widehat a=x,\quad
 \widehat b=b_1,\quad \widehat c=z,\quad \widehat x=a.
\]

The tight one-to-two identity gives (1.6) and (1.7) literally.  The first
move consumes the residual row at `A`; the second consumes the residual row
at `B`.  Conversely, their lower/tail/head roles force exactly the rows
(1.2)--(1.4) and the port conditions above, while serial forest feasibility
forces condition 5.  There is no
additional phase hidden in the set identity.  \(\square\)

## 2. Exact resource and rooted endpoint ledger

Let `P=P(U)` and `Q=Q(V)`.  The role ledger is

\[
\begin{array}{c|c|c|c}
\text{state}&\text{arcs}&\text{tails}&\text{heads}\\ \hline
0&C\to A&\{C\}&\{A\}\\
1&C\to P,\ A\to B&\{C,A\}&\{P,B\}\\
2&B\to C,\ C\to P,\ A\to Q&\{A,B,C\}&\{C,P,Q\}.
\end{array}                                         \tag{2.1}
\]

The physical edges in the final state are

\[
 azS-zL-U,
 \qquad aL-aV.                                      \tag{2.2}
\]

All tail classes are automatically distinct over distinct short chains.
After candidates meeting occupied background heads or colours have been
pruned, the remaining non-graphic collisions internal to a selected ear
family are exactly

\[
 U_i\ne U_j,qquad W_i\ne W_j,qquad V_i\ne V_j
 \quad(i\ne j).                                     \tag{2.3}
\]

Indeed, `U` injectivity is simultaneously `zU`-colour and `P(U)`-head
injectivity; `W` injectivity is `aW`-colour injectivity; and `V`
injectivity is `Q(V)`-head injectivity.  The signatures involving `a,z`
separate all cross-types.

In the clean rooted form, state 0 consists of the edge component `C->A`
and free endpoint components at `B,P,Q`.  State 2 has paths

\[
 B\to C\to P,
 \qquad A\to Q.                                     \tag{2.4}
\]

Thus the move consumes the terminal tickets at `A,B` and the source
tickets at `C,P,Q`, creates the new source ticket `A`, and leaves `B` as
the source of the first output path and `P,Q` as its two terminals.  This
is the endpoint transformation that a connector theorem must use; a
component-count-only ledger loses information.

## 3. Exact factorized selection problem

Let `mathcal S` be a family of short chains whose providers `C_S->A_S`
will be replaced.  Delete those providers first and contract the retained
background forest.

### 3.1 First rotation

Make the bipartite graph

\[
 S\sim U
 \iff U=L_S+b,quad b\in G-L_S,                    \tag{3.1}
\]

after deleting candidates whose `P(U)` ticket or target colour is
unavailable.  One first rotation for every source exists exactly when

\[
 \boxed{|N_0(X)|\ge |X|\quad(X\subseteq\mathcal S).} \tag{3.2}
\]

This is ordinary Hall.

For the full standard short bank, the total cut in (3.2) is

\[
 |N_0(\mathcal S)|-|\mathcal S|
 =I_m-c={m-5\over m+1}c.                            \tag{3.2a}
\]

Hence a full paired-ear selection is impossible at `m=3,4`, with exact
total deficiency one in each dimension; it is tight at `m=5`.  For
`m>=6` this scalar cut has slack, but the subset Hall cuts remain
load-bearing.

### 3.2 Second rotation

Make the bipartite graph with shores

\[
 \mathcal W=\{L+b\},\qquad
 \mathcal V=\{S+b\},                                \tag{3.3}
\]

and colour the edge

\[
 (W,V)=(L_S+b,S+b)                                  \tag{3.4}
\]

by its source short chain `S`.  One second rotation for every source is
exactly a rainbow matching containing one edge of every source colour.
Before forming this graph, delete every edge whose `Q(V)` ticket is occupied
by the retained background or whose `aW` colour is already retained; in
particular, if `V=L_T` for a short chain outside `mathcal S`, delete it
because the untouched provider ends at `A_T=Q(V)`.
Equivalently, it is the integral three-partite SDR

\[
 \sum_b x_{S,b}=1,
 \quad
 \sum_{S,b:L_S+b=W}x_{S,b}\le1,
 \quad
 \sum_{S,b:S+b=V}x_{S,b}\le1.                      \tag{3.5}
\]

The two projected Hall systems are necessary but not sufficient.  The
smallest abstract obstruction already has two source colours on a `2x2`
square:

\[
 E_1=\{(w_1,v_1),(w_2,v_2)\},\qquad
 E_2=\{(w_1,v_2),(w_2,v_1)\}.                       \tag{3.6}
\]

Both shore projections pass Hall, but no two edges of different colours
are disjoint.  Thus (3.5), not two marginal matchings, is the sharp
correlation row.

### Theorem 3.1 (non-graphic factorization)

When `b_0,b_1` are independent, the complete tail/head/colour selection
factorizes exactly into Hall (3.2) and the rainbow SDR (3.5).  No resource
is shared between these two systems.  The common-order restriction
`b_0=b_1` destroys this factorization and gives the square-SDR

\[
 U_S=L_S+b(S)\text{ distinct},\qquad
 V_S=S+b(S)\text{ distinct}.                        \tag{3.7}
\]

#### Proof

This is precisely the collision classification (2.3).  The first choice
controls only `U/P/z`; the second controls only `W/V/Q/a`.  In the common-
order subcatalogue the shared `b(S)` couples the two systems.  \(\square\)

### 3.3 The serial capacity-two projection

There is a useful intermediate problem in which the two typed target shores
`zU` and `aU` are identified with one unlabelled internal bank
`mathcal U_sh`.  Introduce binary variables

\[
 x^0_{S,U},x^1_{S,U}\qquad(L_S\subset U),           \tag{3.8}
\]

where phase 0 means that the first rotation services `zU`, and phase 1
means that the second rotation services `aU`.  If `x^1_{S,U}=1`, put

\[
                 V=U-x_S.                          \tag{3.9}
\]

The exact serial non-graphic refinement of a capacity-two assignment is

\[
\begin{aligned}
 &\sum_{S:L_S\subset U}(x^0_{S,U}+x^1_{S,U})=1
      &&(U\in\mathcal U_{\rm sh}),\\
 &\sum_Ux^0_{S,U}\le1,
   \qquad \sum_Ux^1_{S,U}\le1
      &&(S\in\mathcal L_{\rm sh}),\\
 &\sum_Ux^1_{S,U}\le\sum_Ux^0_{S,U}
      &&(S\in\mathcal L_{\rm sh}),\\
 &\sum_{S,U:\,U-x_S=V}x^1_{S,U}\le1
      &&(V\in {G\choose m-1}).                    \tag{3.10}
\end{aligned}
\]

The third line is precedence: a phase-1 service is available only after
some phase-0 service has created `A_S->B_S`.  The last line is precisely
the `Q(V)`-head SDR.  Candidates occupied by the retained background must
be removed before (3.10) is formed.  Moreover, if `V=L_T` for a short
chain, then `T` must itself be active so that the old provider into
`A_T=Q(V)` is deleted.  The rooted ticket and graphic rows of Sections 2
and 5 must still be imposed.

If phase, precedence, `V`, background, and topology data are erased from
(3.10), only

\[
                   |Y|\le2|N(Y)|                  \tag{3.11}
\]

remains.  Thus the reverse capacity-two theorem is an exact projection of
the serial model, but is not a lift of it.

## 4. The standard-GK phase-zero capacity-two row

Let `mathcal L_sh` be all standard-GK short tops and

\[
 \mathcal U_sh=\partial^+\mathcal L_sh.
\]

Then

\[
 |\mathcal L_sh|=c=\operatorname {Cat}_{m-1},
 \qquad
 |\mathcal U_sh|
 =I_m=\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}
 ={2(m-2)\over m+1}c.                               \tag{4.1}
\]

The anonymous phase-zero owner problem asks for one edge `L subset U`
for every `U in mathcal U_sh`, with capacity two at every `L`.  Its exact
max-flow/min-cut criterion is

\[
 \boxed{|Y|\le2|N(Y)|
        \quad\text{for every }Y\subseteq\mathcal U_sh.}       \tag{4.2}
\]

The total cut has the exact slack

\[
 2c-I_m={6\over m+1}c.                              \tag{4.3}
\]

By contrast, capacity one fails already by the total cut for every
`m>=6`.  Hence capacity two is a genuine row, not an inessential
relaxation.

There is also an unconditional Hall statement in the opposite direction.
Every short top has degree `m-2`, while every boundary target has degree at
most `m-1`.  Therefore, for every `X subseteq mathcal L_sh`, direct edge
counting gives

\[
 (m-2)|X|\le(m-1)|\partial^+X|.
\]

Consequently

\[
 2|\partial^+X|\ge |X|\qquad(m\ge3).                \tag{4.4}
\]

Thus every short source can be assigned a boundary target with target
capacity two in all dimensions.  Notice that
(4.4) is **not** (4.2); reversing a capacitated matching is invalid.

The deterministic audit described in Section 6 verifies (4.2) for
`3<=m<=12`, both in the full incidence graph and in the smaller graph
using only the two root-rotation parents of each boundary target.  This is
finite evidence, not an all-`m` proof.  It also shows why the most obvious
fractional proof does not close: assigning weight `1/mu(U)` to every
incident short top first exceeds load two at `m=12` (maximum
`2.019877344877`).

Finally, (4.2) is an anonymous owner-degree statement.  It permits two
edges at `zL`; the fixed-`M_0` paired ear has one outgoing and one incoming
ticket with prescribed roles.  Therefore (4.2) cannot be substituted for
(3.2), (3.5), or the rooted endpoint ledger.

## 5. Exact graphic row

Let `F^-` be the retained physical forest after deleting all selected
providers `C_S->A_S`, and contract every component of `F^-`.  A paired-ear
selection `J` adds the three projected edges

\[
 azS-zL,\qquad zL-U,qquad aL-aV                    \tag{5.1}
\]

for each `S in J`.  Its exact topology condition is

\[
 \boxed{\bigcup_{S\in J}E_S
        \text{ is independent in the contracted graphic matroid}.}       \tag{5.2}
\]

Equivalently, for every nonempty vertex set `Z` of the contracted
multigraph, counting parallel inserted edges with multiplicity,

\[
 \sum_{S\in J}|E_S\cap {Z\choose2}|\le |Z|-1.       \tag{5.3}
\]

Equivalently again, all three additions per source pass dynamic union--find
without closing a cycle.  Because the directed role rows already give
indegree and outdegree at most one, (5.2) makes the result a directed
linear forest.

This is the exact **final simultaneous-exchange** criterion.  It is not by
itself a serialization theorem: a literal sequence of the two rotations
must also keep each provider selected until its turn and pass the transient
`A->B` union--find tests.  In the isolated short-core model, if the
dependency digraph below is acyclic, processing it in reverse topological
order supplies such a serialization.

If `Q(V_S)=A_T`, equivalently `V_S=L_T`, then `T` must also be selected:
otherwise the untouched provider `C_T->A_T` already occupies that head.
For selected `T`, record the dependency arc `S->T`.  In an empty background
the only possible cross-ear cycle is a cycle in this dependency digraph.
In a nonempty background that shortcut is insufficient; the contracted
graphic inequality (5.3) is the exact condition.

## 6. Audit and surviving gate

`scratch/audit_threadD_scd_short_boundary_cap2_20260801.cpp` performs a
deterministic exact enumeration of the standard-GK boundary.  It checks:

* the literal short-top and boundary path predicates;
* all containment incidences;
* a capacity-two matching saturating every one of the `I_m` targets;
* the same matching restricted to the two canonical root-rotation parents;
  and
* the reciprocal-degree fractional load.

For `m=3,...,12`, its matching orders equal

\[
 1,4,14,48,165,572,2002,7072,25194,90440=I_m.       \tag{6.1}
\]

The exact remaining theorem is therefore not a menu count.  It is the
simultaneous integral system

\[
 \text{Hall (3.2)}
 \quad+\quad
 \text{rainbow SDR (3.5)}
 \quad+\quad
 \text{rooted tickets}
 \quad+\quad
 \text{graphic rank (5.2)},                         \tag{6.2}
\]

with the protected pivot and background availability deleted from the
candidate sets first.  The first unproved all-dimensional marginal is the
reverse capacity-two cut (4.2); even after it is proved, the coloured
square (3.6) and the graphic cuts remain genuine independent gates.
