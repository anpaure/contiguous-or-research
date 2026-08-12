# Fixed-`M_0` ledger for the two-stage SCD short-chain ear

Date: 2026-08-01  
Lane: Thread D / SCD short-chain tight augmentation  
Status: exact local algebra, exact typed-resource and endpoint ledger, and
an exact global SDR/graphic formulation.  No all-dimensional Hall theorem
for the standard Greene--Kleitman boundary is asserted here.

## 0. Verdict

The two rotations are legal in the frozen four-row matching.  The second
label `b'` is independent of the first label `b`; imposing `b'=b` gives a
useful square subcatalogue but is not forced by the augmenter.

For a family of short chains, the unrestricted two-stage catalogue is
therefore governed by three images, not two:

1. the first target/head image `U=L+b`;
2. the second target-colour image `U'=L+b'`; and
3. the second rooted-head image `V=S+b'=U'-x`.

All three relevant images must be injective on their respective selected
domains.  In addition, a second-stage head which lands at the `A`-root of
an untouched short chain is illegal, and the surviving dependency arcs
must be graphic-independent.  These are genuine typed conditions; raw
menu counts do not imply them.

There is a useful projection.  If the internal Catalan bank is treated as
an unlabelled demand bank and every short triangle has its two serial
service positions available, the projection is a capacity-two bipartite
matching.  Its exact Hall inequalities are

\[
 |Y|\le 2|N(Y)|\qquad(Y\subseteq\mathcal U_{\rm sh}).       \tag{0.1}
\]

The demand shore has exact size

\[
 |\mathcal U_{\rm sh}|=I_m
 =\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}.          \tag{0.2}
\]

This projection is necessary but is not the full paired-ear theorem: one
must orient the two loads as first/second service, enforce the `V`-head
SDR, and impose the rooted graphic rows below.

## 1. Frozen matching and notation

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3.
\]

Let `S<L=S+x` be a short central chain in the standard SCD on `G`, with
`|S|=m-2`.  Its three rank-`m-1` roots are

\[
 C=L,\qquad A=aS,\qquad B=zS.                        \tag{1.1}
\]

The frozen four-row incidence matching satisfies

\[
 M_0(C)=zL,\qquad M_0(A)=aL,\qquad M_0(B)=azS.       \tag{1.2}
\]

Thus the rooted arc `C\to A` is the physical Johnson edge

\[
 zL-aL
\]

with lower intersection `L=C` and upper union `azL`.

Choose independently

\[
 b_0,b_1\in G-L.                                     \tag{1.3}
\]

Put

\[
 U_0=L+b_0,\qquad U_1=L+b_1,\qquad
 V_1=S+b_1=U_1-x,                                    \tag{1.4}
\]

and define the rooted heads

\[
 P_0=P(U_0)=M_0^{-1}(U_0),\qquad
 Q_1=Q(V_1)=M_0^{-1}(aV_1).                          \tag{1.5}
\]

For the four-row SCD matching one may also write
`Q(V)=a p(V)`, where `p(V)` is the predecessor below `V` in its central
SCD segment.

## 2. Exact two-stage identity

### Lemma 2.1 (first rotation)

The fixed-`M_0` replacement

\[
 \boxed{
 C\to A
 \quad\longmapsto\quad
 A\to B\; +\; C\to P_0 }
                                                               \tag{2.1}
\]

is a legal tight one-to-two augmentation.  Its physical form is

\[
 zL-aL
 \quad\longmapsto\quad
 aL-azS\; +\;zL-U_0,                                 \tag{2.2}
\]

and its upper-colour action is

\[
 \{azL\}\longmapsto\{azL,zU_0\}.                    \tag{2.3}
\]

#### Proof

The edge `A\to B` has physical intersection `aS=A` and union `azL`.
The edge `C\to P_0` has physical intersection `L=C` and union `zU_0`,
because `M_0(P_0)=U_0`.  These are exactly the two diamonds supplied by
the tight augmenter with

\[
 \widehat L=L,quad \widehat a=z,quad
 \widehat b=b_0,quad \widehat c=a,quad \widehat x=x.
\]
\(\square\)

### Lemma 2.2 (independent second rotation)

Starting from the auxiliary edge `A\to B`, independently of `b_0`, one
may apply

\[
 \boxed{
 A\to B
 \quad\longmapsto\quad
 B\to C\; +\; A\to Q_1 . }
                                                               \tag{2.4}
\]

Its physical form is

\[
 aL-azS
 \quad\longmapsto\quad
 azS-zL\; +\;aL-aV_1,                                \tag{2.5}
\]

and its upper-colour action is

\[
 \{azL\}\longmapsto\{azL,aU_1\}.                    \tag{2.6}
\]

#### Proof

Since `L=S+x`, `V_1=S+b_1`, and `b_1\notin L`, one has

\[
 L\cap V_1=S,qquad L\cup V_1=U_1.
\]

Consequently `aL-aV_1` has intersection `aS=A` and union `aU_1`.
The edge `azS-zL` has intersection `zS=B` and union `azL`.  This is the
tight augmenter with

\[
 \widehat L=aS,quad \widehat a=x,quad
 \widehat b=b_1,quad \widehat c=z,quad \widehat x=a.
\]
\(\square\)

### Corollary 2.3 (general paired ear)

The composite replacement is

\[
 \boxed{
 \{C\to A\}
 \longmapsto
 \{B\to C\to P(U_0),\ A\to Q(V_1)\}, }
                                                               \tag{2.7}
\]

with upper colours

\[
 azL,qquad zU_0,qquad aU_1.                        \tag{2.8}
\]

The specialization `b_0=b_1` gives `U_0=U_1` and is the Boolean-square
subcatalogue.  Equality of the two labels is not needed for (2.7).

## 3. Exact typed-resource ledger

Write only the selected rooted arcs; isolated tickets are implicit.  The
three states have the following exact ledger:

\[
\begin{array}{c|c|c|c|c}
\text{state}&\text{selected arcs}&\text{lower/tails}&\text{heads}
 &\text{upper colours}\\ \hline
0&C\to A&\{C\}&\{A\}&\{azL\}\\
1&C\to P_0,\ A\to B&\{C,A\}&\{P_0,B\}
 &\{azL,zU_0\}\\
2&B\to C,\ C\to P_0,\ A\to Q_1&\{C,A,B\}
 &\{C,P_0,Q_1\}&\{azL,zU_0,aU_1\}.
\end{array}                                                   \tag{3.1}
\]

Thus the first rotation adds tail/lower ticket `A`, releases head ticket
`A`, and consumes head tickets `B,P_0`.  The second adds tail/lower ticket
`B`, releases head ticket `B`, and consumes head tickets `C,Q_1`.
Overall, all three short roots become tails; the old head `A` is released;
and the final heads are `C,P_0,Q_1`.

The literal path endpoints are

\[
\begin{array}{c|c|c}
\text{state}&\text{sources}&\text{terminals}\\ \hline
0&\{C\}&\{A\}\\
1&\{C,A\}&\{P_0,B\}\\
2&\{B,A\}&\{P_0,Q_1\}.
\end{array}                                                   \tag{3.2}
\]

In particular the move is not endpoint-neutral.  Any rooted connector
argument which records only the component decrement loses essential
information.

## 4. Exact family-level resource conditions

Let each short chain be assigned a state `r_S\in\{0,1,2\}`.  Put

\[
 \mathcal A=\{S:r_S\ge1\},\qquad
 \mathcal D=\{S:r_S=2\}.                              \tag{4.1}
\]

For `S\in\mathcal A` choose `b_0(S)`; for `S\in\mathcal D` choose
`b_1(S)`.  Apart from interaction with a background forest, the exact
palette/head conditions are:

\[
\begin{aligned}
 &U_0(S)=L_S+b_0(S) &&(S\in\mathcal A)
       &&\text{are pairwise distinct},\\
 &U_1(S)=L_S+b_1(S) &&(S\in\mathcal D)
       &&\text{are pairwise distinct},\\
 &V_1(S)=S+b_1(S)   &&(S\in\mathcal D)
       &&\text{are pairwise distinct}.                \tag{4.2}
\end{aligned}
\]

The first row simultaneously makes the `zU_0` colours and `P(U_0)` heads
injective.  The second makes the `aU_1` colours injective.  The third makes
the `Q(V_1)` heads injective.  Coordinate signatures separate all other
head classes, except for the following deliberate short-chain linkage.

If

\[
 V_1(S)=L_T                                             \tag{4.3}
\]

is itself a short top, then `Q(V_1(S))=A_T`.  Therefore (4.3) is legal
only when `T\in\mathcal A`, so that the old incoming use of `A_T` has been
released.  It then gives the literal continuation into the tail `A_T`.
Landing at an untouched `T\notin\mathcal A` is a head collision, not an
exit to the long core.

The first heads `P(U_0)` are never short roots `C_T`: their `M_0` images
lie wholly in `G`, whereas `M_0(C_T)=zL_T` contains `z`.  Other collisions
with a previously selected background are still genuine free-head rows
and must be imposed explicitly.

## 5. SDR and capacity-two projections

### 5.1 The unrestricted rectangular SDR

For a prescribed active set `\mathcal A` and doubled set
`\mathcal D\subseteq\mathcal A`, the non-graphic selection problem is:

* choose one edge `S\mapsto U_0=L_S+b_0` for every
  `S\in\mathcal A`, injectively in `U_0`;
* choose one hyperedge
  `S\mapsto(U_1=L_S+b_1,V_1=S+b_1)` for every
  `S\in\mathcal D`, injectively in both `U_1` and `V_1`;
* impose the closure implication (4.3).

The first bullet is an ordinary transversal.  The second is a coloured
matching in a three-partite 3-uniform hypergraph.  The separate Hall
conditions on its two projections are necessary but not sufficient.
Calling the full problem a single ordinary Hall matching is therefore
incorrect.

### 5.2 Servicing the internal Catalan demand bank

Let

\[
 \mathcal L_{\rm sh}=\{L:\ L\text{ is a standard-GK short top}\},
 \qquad
 \mathcal U_{\rm sh}=\partial^+\mathcal L_{\rm sh}.     \tag{5.1}
\]

The exact ballot count is

\[
 |\mathcal L_{\rm sh}|=\operatorname {Cat}_{m-1},
 \qquad
 |\mathcal U_{\rm sh}|=I_m
 =\operatorname {Cat}_m-2\operatorname {Cat}_{m-1}.    \tag{5.2}
\]

Project away the phase, head and graphic data, and permit each short
provider to service at most two demands.  The resulting bipartite
`b`-matching saturates all of `\mathcal U_{\rm sh}` if and only if

\[
 \boxed{|Y|\le2|N(Y)|\quad
        \text{for every }Y\subseteq\mathcal U_{\rm sh}.} \tag{5.3}
\]

The total cut has strict scalar room

\[
 2|\mathcal L_{\rm sh}|-|\mathcal U_{\rm sh}|
 ={6\over m+1}\operatorname {Cat}_{m-1}.             \tag{5.4}
\]

Equation (5.4) does not prove the subset cuts (5.3).

An exact integral refinement uses variables `x^0_{S,U},x^1_{S,U}` for
`L_S\subset U`.  For an unlabelled demand bank, the serial constraints are

\[
\begin{aligned}
 &\sum_{S:L_S\subset U}(x^0_{S,U}+x^1_{S,U})=1
       &&(U\in\mathcal U_{\rm sh}),\\
 &\sum_Ux^0_{S,U}\le1,qquad \sum_Ux^1_{S,U}\le1
       &&(S\in\mathcal L_{\rm sh}),\\
 &\sum_Ux^1_{S,U}\le\sum_Ux^0_{S,U}
       &&(S\in\mathcal L_{\rm sh}),                 \tag{5.5}\\
 &\sum_{S,U:\ U-x_S=V}x^1_{S,U}\le1
       &&\left(V\in{G\choose m-1}\right).
\end{aligned}
\]

The third row is the serial-precedence condition: a second rotation is
unavailable unless the first rotation has created `A_S\to B_S`.  The last
row is the missing `Q(V)` head-SDR.  The closure implication (4.3), fixed
target shores if any, protected tickets and the graphic rows must then be
added.  Therefore a proof of the projected capacity-two Hall system (5.3)
would be useful, but would not alone prove a paired-ear forest.

## 6. Exact graphic condition

Delete every rotated provider edge `C_SA_S` from the current physical
forest.  Insert the physical edges dictated by state 1 or 2.  The family
is legal exactly when

1. all directed tail/head capacities from Sections 3--4 hold; and
2. the inserted physical edges are independent in the graphic matroid
   after the untouched background components are contracted.

In the clean local bank, with all `P(U_0)` roots and all nonshort `Q(V_1)`
roots isolated, the only possible continuing dependencies are (4.3).
The inserted support is a linear forest exactly when the directed graph

\[
 S\longrightarrow T
 \quad\Longleftrightarrow\quad
 S\in\mathcal D, V_1(S)=L_T                         \tag{6.1}
\]

has no directed cycle and every target `T` lies in `\mathcal A`.
An arc landing at a state-1 block terminates there; only state-2 blocks
can continue a dependency cycle.

With a nontrivial background, (6.1) is no longer the full test.  The exact
criterion is the contracted graphic-matroid independence in the preceding
paragraph, together with the rooted endpoint ledger (3.2).

## 7. Sharp surviving gate

The two-stage SCD algebra is unconditional.  What remains is not a menu
count but the following coupled integral statement:

> choose a serial capacity-two assignment satisfying (5.5), the short-top
> closure implications, all fixed-background free-head rows, and the
> contracted graphic inequalities.

The projected standard-GK capacity-two cut system (5.3) is the first
testable layer.  Even if it is proved in all dimensions, the `V`-head SDR
and graphic/rooted endpoint conditions remain load-bearing.
