# Re-rooting K2 cycles: an exponential projected packing and the exact FIFO obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 n=2m,\qquad k=m-H,\qquad \ell=m+H,
 \qquad W=\binom{2m}{m},\qquad N_H=\binom{2m}{k},
\tag{0.1}
\]

and assume throughout the reduced-scale range

\[
 H=\left\lfloor\sqrt{m\log\log m}\right\rfloor,
 \qquad 1\le r<H,
\tag{0.2}
\]

unless a statement is explicitly made for general parameters.  The
following conclusions are proved.

1.  At root-set level, two successive re-root exchanges

    \[
       A\xrightarrow{e\to p}B\xrightarrow{f\to q}C
    \]

    are locally compatible with the ordered \(O/S\) atlas exactly when

    \[
                         f\ne p,\qquad q\ne e.               \tag{0.3}
    \]

    The directed-arc transition graph is exactly

    \[
       (J_k-I_k)\otimes(J_\ell-I_\ell)
    \]

    over each intermediate root.  It has degree

    \[
                         (k-1)(\ell-1),                       \tag{0.4}
    \]

    and its exact common-neighbour numbers are given in Section 2.

2.  This projected graph has an explicit all-\(m\) long-cycle packing.
    Pair the \(2m\) coordinates.  The mixed-coordinate orientations in
    every fixed pair signature form a cube, and a cyclic Gray code gives
    a locally compatible root cycle.  Keeping only cubes of dimension at
    least \(\lfloor m/4\rfloor\) covers

    \[
                         (1-e^{-\Omega(m)})N_H                \tag{0.5}
    \]

    roots by vertex-disjoint cycles, each of length at least

    \[
                         2^{\lfloor m/4\rfloor}.              \tag{0.6}
    \]

3.  Every one of those projected cycles is a genuine **static**
    collar-neutral re-root trade after collars are assigned.  In
    complements, it is a cycle of rank-\((\ell-1)\) seam facets; the
    endpoint flags telescope exactly at every protected signed rank.
    Fixed-root boundary rectangles may be placed immediately before and
    after the re-root at a top, so the move really joins different
    \(K_2\) boundary-option components.  It is not merely an abstract
    arc circulation.

4.  The same cycles are almost never seamless physical fusions.  In an
    ordered trajectory the root queue is FIFO:

    \[
       (e_0,\ldots,e_{k-1})
       \longmapsto
       (e_1,\ldots,e_{k-1},p).
    \]

    Thus, if the \(j\)-th root exchange is \(e_j\to p_j\), every cyclic
    lift obeys

    \[
                         \boxed{e_{j+k}=p_j}.                 \tag{0.7}
    \]

    Inside a fixed pair cube this forces every direction to recur
    exactly \(k\) events later.  Hence the cube dimension must equal
    \(k\), so the root has no full coordinate pair.  Such roots number

    \[
                         \binom mH2^{m-H}
       =e^{-m\log2+o(m)}N_H.                                 \tag{0.8}
    \]

    Therefore the explicit packing in (0.5) is overwhelmingly a
    set-level \(K_2\) packing and cannot be used as a literal fused word.

5.  Full monodromy of the fixed short macro is classified exactly.  For

    \[
                         F_r=S\circ O^{r-1},
    \]

    put \(g=\gcd(\ell,r)\) and \(s_0=\ell/g\).  Its permutation of the
    \(2m\) ordered slots has cycles of lengths

    \[
                         s_0+k\quad\hbox{once},
       \qquad s_0\quad\hbox{\(g-1\) times}.                  \tag{0.9}
    \]

    The root returns after \(s_0+k\) blocks.  The complete ordered state
    returns then if and only if

    \[
                         g=1\quad\hbox{or}\quad s_0\mid k.   \tag{0.10}
    \]

    In the reduced range the second alternative is impossible.  Hence

    \[
                 \boxed{\gcd(m+H,r)=1}                       \tag{0.11}
    \]

    is necessary and sufficient for the standard fixed macro to give a
    one-pass root-simple ordered cycle.  Then the slot permutation is one
    \(2m\)-cycle and its roots are the \(2m\) cyclic consecutive
    \(k\)-windows of a coordinate order.

6.  The catalogue of these genuine interval-wreath root cycles is
    regular with root degree

    \[
                         D_R=k!\ell!,                         \tag{0.12}
    \]

    maximum relative root-pair codegree

    \[
                         {2\over k\ell}={2+o(1)\over m^2}.    \tag{0.13}
    \]

    It therefore has the correct fractional geometry.  A near-perfect
    integral matching would use \((1+o(1))N_H/(2m)\) cycles and would
    reduce the opening-collar allowance to

    \[
                         O\!\left({HN_H\over m}\right)=o(W). \tag{0.14}
    \]

    No such integral matching with simultaneous middle-owner completion
    is proved.  Prebundling raises the physical rank to order \(m r\),
    outside the authorized growing-rank matching theorem; postbundling
    through the Gray bank is invalid by (0.7).

This gives a sharp answer to the proposed re-root route.  Orbit mobility
and exact collar-neutral static trades are abundant.  The missing gate
is not root-graph expansion; it is an integral matching in the genuine
ordered interval-wreath catalogue, with middle-owner capacity included.

## 1. The exact ordered atlas

An ordered state is a partition of \([2m]\) into three ordered queues

\[
 \Sigma=(Q;P;E)
\tag{1.1}
\]

with

\[
 \begin{aligned}
 Q&=(q_0,\ldots,q_{H-1}),\\
 P&=(p_0,\ldots,p_{m-1}),\\
 E&=(e_0,\ldots,e_{k-1}).
 \end{aligned}                                               \tag{1.2}
\]

The middle owner is the set \(P\), the top is \(P\cup Q\), and its
complementary root is the set \(E\).  Define

\[
 \begin{aligned}
 O\Sigma={}&
 (q_1,\ldots,q_{H-1},p_0;\ 
  p_1,\ldots,p_{m-1},q_0;\ E),\\
 S\Sigma={}&
 (q_1,\ldots,q_{H-1},e_0;\
  p_1,\ldots,p_{m-1},q_0;\
  e_1,\ldots,e_{k-1},p_0).
 \end{aligned}                                               \tag{1.3}
\]

Both maps are bijections and both make the same owner transition

\[
                         P\longmapsto P-p_0+q_0.              \tag{1.4}
\]

The map \(O\) fixes the top and root.  The map \(S\) makes

\[
 \begin{aligned}
 P\cup Q&\longmapsto(P\cup Q)-p_0+e_0,\\
 E&\longmapsto E-e_0+p_0. 
 \end{aligned}                                               \tag{1.5}
\]

For \(1\le r<H\), put

\[
                         F_r=S\circ O^{r-1}.                  \tag{1.6}
\]

A direct substitution gives

\[
 \begin{aligned}
 Q'={}&(q_r,\ldots,q_{H-1},p_0,\ldots,p_{r-2},e_0),\\
 P'={}&(p_r,\ldots,p_{m-1},q_0,\ldots,q_{r-1}),\\
 E'={}&(e_1,\ldots,e_{k-1},p_{r-1}).
 \end{aligned}                                               \tag{1.7}
\]

Thus one block has \(r\) literal owner transitions and one root
exchange

\[
                         e_0\longrightarrow p_{r-1}.          \tag{1.8}
\]

The order on \(E\) is physical.  Only an unexposed suffix of an open
path may be permuted when choosing its initial representation; once a
label has been appended, it cannot be moved to the head by a change of
gauge.

## 2. Local K2 compatibility and exact graph parameters

Write a directed root arc as

\[
 \alpha=(A;e,p):A\longrightarrow B=A-e+p,                   \tag{2.1}
\]

where \(e\in A\), \(p\notin A\).  A prospective successor is

\[
 \beta=(B;f,q):B\longrightarrow C=B-f+q.                    \tag{2.2}
\]

### Theorem 2.1 (two-seam compatibility)

The two arcs (2.1)--(2.2) can occur as two consecutive \(S\)-seams of
an ordered \(O/S\) trajectory only if

\[
                         f\ne p,\qquad q\ne e.                \tag{2.3}
\]

Conversely, these two inequalities are sufficient for a two-seam local
ordered representation, with the still-unexposed queue suffix chosen
arbitrarily.

#### Proof

At the first seam, \(p\) is appended at the tail of \(E\).  It cannot be
the next removed head, so \(f\ne p\).  The label \(e\) is appended at
the tail of \(Q\).  Since \(r<H\), it cannot be the next \(P\)-head
which enters the root, so \(q\ne e\).

Conversely, order the first root with head \(e\), put \(p\) in the
required \(P\)-slot, and put \(f\) next in the root queue.  The two
inequalities leave all four designated slots distinct where required.
The other slots can be filled bijectively by the unused coordinates.
This gives the two local seams.  It does not assert a third seam or a
closed lift. \(\square\)

Let \(\mathcal L\) be the directed transition graph whose vertices are
directed root arcs and whose arcs are the compatible consecutive pairs.
It has

\[
                         N_Hk\ell                            \tag{2.4}
\]

vertices.

### Theorem 2.2 (degree and codegrees)

Every vertex of \(\mathcal L\) has exact indegree and outdegree

\[
                         D=(k-1)(\ell-1).                     \tag{2.5}
\]

Fix an intermediate root \(B\).  Index its incoming arcs by

\[
                         (p,e)\in B\times B^c                \tag{2.6}
\]

and its outgoing arcs by \((f,q)\in B\times B^c\).  The local matrix is

\[
                         (J_k-I_k)\otimes(J_\ell-I_\ell).     \tag{2.7}
\]

For two incoming arcs \((p,e),(p',e')\), the exact number of common
successors is

\[
       \bigl(k-|\{p,p'\}|\bigr)
       \bigl(\ell-|\{e,e'\}|\bigr).                          \tag{2.8}
\]

Thus, for distinct rows, the three possibilities are

\[
 (k-1)(\ell-2),\qquad (k-2)(\ell-1),\qquad
 (k-2)(\ell-2).                                              \tag{2.9}
\]

Incoming arcs with different heads have no common successor.  The
common-predecessor formulas are dual.

#### Proof

Given \((p,e)\), one may choose any

\[
                         f\in B\setminus\{p\},
       \qquad q\in B^c\setminus\{e\},                        \tag{2.10}
\]

which proves (2.5)--(2.7).  A common successor must avoid both forbidden
first coordinates and both forbidden second coordinates, giving (2.8)
and (2.9).  An outgoing arc has a unique tail, proving the last claim.
\(\square\)

Compatible two-step root walks end exactly at Johnson distance two.  A
fixed distance-two endpoint is obtained in exactly four ways, by ordering
the two departures and the two arrivals independently.

The codegrees in (2.9) are almost the full degree.  Hence ordinary
small-codegree matching theory is not available on the arc-transition
graph itself.  This large codegree is nevertheless not the decisive
obstruction: the next section gives an explicit long-cycle packing.

## 3. An explicit projected packing by pair cubes

Fix a partition of \([2m]\) into coordinate pairs

\[
                         \Pi_1,\ldots,\Pi_m.                  \tag{3.1}
\]

For a root \(A\in\binom{[2m]}k\), let

* \(a\) be the number of pairs contained in \(A\);
* \(b\) the number disjoint from \(A\); and
* \(d\) the number meeting \(A\) in one coordinate.

Then

\[
                         2a+d=k,qquad a+b+d=m,               \tag{3.2}
\]

so

\[
                         b=a+H,qquad d=k-2a.                 \tag{3.3}
\]

Fix which pairs are full, empty, and mixed.  The roots with that
signature are indexed by the choice of one of two coordinates in every
mixed pair, hence form a cube \(Q_d\).  A cube edge flips one mixed pair
and is a root Johnson edge.

### Lemma 3.1 (cube cycles are locally compatible)

For \(d\ge2\), a cyclic binary-reflected Gray Hamilton cycle in \(Q_d\)
satisfies (2.3) at every vertex.

#### Proof

Two consecutive edges of a simple cube cycle cannot have the same
direction, since two successive flips of one bit backtrack.  Edges in
different pair directions use four coordinates from two disjoint pairs.
Thus the next departure is not the previous arrival and the next arrival
is not the previous departure. \(\square\)

Take

\[
                         d_0=\lfloor m/4\rfloor.              \tag{3.4}
\]

Use one Gray Hamilton cycle in every signature cube with \(d\ge d_0\).
These cycles are root-disjoint and every one has length at least
\(2^{d_0}\).

### Theorem 3.2 (exponentially long projected near-factor)

The exact number of omitted roots is

\[
 N_{\rm bad}=
 \sum_{\substack{d<d_0\\d\equiv k\ ({\rm mod}\ 2)}}
 {m!\,2^d\over
  ((k-d)/2)!\,((k-d)/2+H)!\,d!}.                             \tag{3.5}
\]

Moreover

\[
                         {N_{\rm bad}\over N_H}=e^{-\Omega(m)}.\tag{3.6}
\]

#### Proof

For fixed \(d\), choose the mixed pairs, the full pairs among the
remainder, and one coordinate in every mixed pair.  This gives (3.5).
Crude summation gives

\[
 \begin{aligned}
 N_{\rm bad}
 &\le2^m\sum_{d\le m/4}\binom md\\
 &\le2^m\,3^{m/4}(4/3)^m
   =\left({8\over3^{3/4}}\right)^m.                           \tag{3.7}
 \end{aligned}
\]

The second inequality follows by multiplying the \(d\)-th summand by
\(3^{m/4-d}\ge1\) and summing the binomial expansion of \((1+1/3)^m\).

For \(H=o(m)\), comparison with the middle binomial coefficient gives

\[
 N_H\ge {4^m\over2m+1}
       \exp\!\left(-{3H^2\over m}\right)                    \tag{3.8}
\]

for all sufficiently large \(m\).  One direct proof writes the ratio to
\(\binom{2m}m\) as a product and uses
\(\log(1-x)\ge-x-x^2\) for \(0\le x\le1/2\).  At (0.2), the exponential
factor in (3.8) is at least \((\log m)^{-3}\).  Therefore

\[
 {N_{\rm bad}\over N_H}
 \le(2m+1)(\log m)^3
       \left({2\over3^{3/4}}\right)^m=o(1).                  \tag{3.9}
\]

This proves the theorem. \(\square\)

In particular, the number of projected components is at most

\[
                         {N_H\over2^{\lfloor m/4\rfloor}}.    \tag{3.10}
\]

If these cycles were seamless physical components, their collar cost
would be far below coefficient-one scale.  Section 5 proves that they
are not.

## 4. What the Gray cycles do prove physically: static collar-neutral trades

Let

\[
 A_0,A_1,\ldots,A_{L-1},A_L=A_0                           \tag{4.1}
\]

be any simple root Johnson cycle.  Put \(U_i=A_i^c\), and let

\[
                         B_i=U_{i-1}\cap U_i                 \tag{4.2}
\]

be its rank-\((\ell-1)\) seam facet.  Then

\[
                         U_i=B_i\cup B_{i+1}.                 \tag{4.3}
\]

Thus the root cycle is dual to a cyclic sequence of adjacent seam
facets.  The already proved two-seam trace formula says that a one-step
re-root on \(U_i\) has one negative flag based at \(B_i\) and one
positive flag based at \(B_{i+1}\).  Matching ordered collars makes
these flags literally equal, so they telescope around the cycle.

For completeness, the required collars always exist at the present
scale.  At a seam vertex choose an ordered set of size \(2H-1\).  It
must avoid the two exchanged labels and the collar at each adjacent
vertex.  Choose all but the final collar greedily, avoiding one previous
collar; at least

\[
                         \ell-1-(2H-1)-2=m-H-2               \tag{4.4}
\]

labels remain.  For the last collar avoid both neighbouring collars and
the two seam labels; at least

\[
                         \ell-1-2(2H-1)-2=m-3H-1             \tag{4.5}
\]

remain.  Under \(m\ge6H+4\), both quantities are at least \(2H-1\).

### Theorem 4.1 (static cycle lift)

Every root cycle satisfying the local inequalities (2.3) at every
vertex admits rooted top words
such that the simultaneous one-step re-root at its tops has aggregate
signed derivative zero at every protected depth \(-H\le q\le H\).

In particular every Gray cycle in Section 3 is an exact static
collar-neutral factor substitution.  At each top, a fixed-root boundary
rectangle can enter the old rooted word and another can leave the shifted
word.  The two focal \(K_2\) edges use successive boundary pairs

\[
                         \{p_1,p_2\},\qquad\{p_2,p_3\}.       \tag{4.6}
\]

Hence the cycle genuinely joins distinct fixed-root \(K_2\) components.

This theorem is an endpoint-table trade.  Its different tops are changed
simultaneously.  It does not say that the top words concatenate in one
ordered queue trajectory.  That distinction is decisive.

## 5. FIFO obstruction to seamless fusion

Consider any consecutive sequence of \(S\)-seams, allowing arbitrary
numbers of \(O\)-steps between them.  Write the ordered root before seam
\(j\) as \(E_j\), and write its exchange as \(e_j\to p_j\).

### Theorem 5.1 (exact root FIFO law)

For every open trajectory,

\[
 E_{j+1}=\operatorname{shift}(E_j)\mathbin\Vert p_j.         \tag{5.1}
\]

Consequently, in every cyclic lift,

\[
                         e_{j+k}=p_j                         \tag{5.2}
\]

with indices read cyclically.

#### Proof

Every \(O\)-step fixes \(E\), while (1.3) shifts it left and appends the
departing owner coordinate.  Iterating gives (5.1).  An appended label
reaches the head after exactly \(k\) further \(S\)-events, proving
(5.2). \(\square\)

### Theorem 5.2 (pair-cube lift obstruction)

A simple cycle contained in a fixed pair-signature cube can lift through
the ordered root queue only if

\[
                         a=0,qquad d=k.                      \tag{5.3}
\]

Every such lifted simple cycle has length exactly \(2k\).

#### Proof

Suppose seam \(j\) flips one mixed pair from \(e_j\) to its mate \(p_j\).
The next use of that pair direction must remove \(p_j\).  By (5.1), this
cannot happen in the following \(k-1\) seams, and by (5.2) it must happen
at seam \(j+k\).  Therefore no direction repeats among any \(k\)
consecutive seams.  The cube has only \(d\) directions, so \(d\ge k\).
But (3.3) gives \(d=k-2a\le k\), proving (5.3).

Now all \(k\) directions occur exactly once in each block of \(k\)
seams, and the direction word is \(k\)-periodic.  After one period every
bit is complemented; after two periods the root returns.  A simple cycle
therefore has length exactly \(2k\). \(\square\)

The number of roots satisfying (5.3) is

\[
                         N_{\rm lift}=\binom mH2^{m-H}.        \tag{5.4}
\]

Indeed, choose the \(H\) empty pairs and one coordinate from every other
pair.  Since \(H=o(m)\),

\[
 \log N_{\rm lift}=m\log2+o(m),\qquad
 \log N_H=2m\log2-o(m),                                    \tag{5.5}
\]

which proves (0.8).

The standard Gray direction word already displays the obstruction
locally: it contains the pattern \(1,2,1\).  When \(r\ll H\), the first
flipped-in root label is still near the tail of \(E\), and the first
flipped-out label is still near the tail of \(Q\), two blocks later.
Neither can occupy the required head.  The nominal two-block collar
certificates overlap inside a radius-\(H\) window and do not define one
literal concatenation.

## 6. Exact monodromy of the fixed macro

We now classify \(F_r\) as a permutation of the ordered slots.  On the
top positions choose the cyclic indexing

\[
 \begin{aligned}
 u_0&=Q_0,\\
 u_1,\ldots,u_m&=P_{m-1},P_{m-2},\ldots,P_0,\\
 u_{m+1},\ldots,u_{\ell-1}&=Q_{H-1},Q_{H-2},\ldots,Q_1.
 \end{aligned}                                               \tag{6.1}
\]

Then \(O\) is the \(\ell\)-cycle

\[
                         u_i\longmapsto u_{i+1}.              \tag{6.2}
\]

The map \(S\) replaces the one arrow

\[
                         u_m\longrightarrow u_{m+1}           \tag{6.3}
\]

by the path

\[
 u_m\longrightarrow E_{k-1}\longrightarrow E_{k-2}
 \longrightarrow\cdots\longrightarrow E_0
 \longrightarrow u_{m+1}.                                  \tag{6.4}
\]

Thus \(F_r\) is top rotation by \(r\), with the \(E\)-chain spliced
into the rotation orbit containing (6.3).

### Theorem 6.1 (slot-cycle classification)

Let

\[
                         g=\gcd(\ell,r),\qquad s_0=\ell/g.   \tag{6.5}
\]

The slot cycles of \(F_r\) have lengths

\[
                         s_0+k,quad
       \underbrace{s_0,\ldots,s_0}_{g-1\text{ times}}.       \tag{6.6}
\]

The root-set orbit has length \(s_0+k\).  The full ordered state closes
at its first root return if and only if (0.10) holds.

#### Proof

Rotation by \(r\) on \(\mathbb Z/\ell\mathbb Z\) has \(g\) cycles,
all of length \(s_0\).  Replacing one arrow on one cycle by the path
(6.4) adds its \(k\) slots to that cycle and leaves the other cycles
unchanged.  This proves (6.6).

All root slots lie on the long cycle, consecutively.  Their set returns
after its length \(s_0+k\).  At that time every short slot cycle has
also returned exactly when \(s_0\mid(s_0+k)\), equivalently \(s_0\mid k\).
If there are no short cycles, i.e. \(g=1\), closure is automatic.
\(\square\)

At the reduced scale, \(g\le r\), so

\[
                         s_0\ge{\ell\over r}>2H              \tag{6.7}
\]

for all sufficiently large \(m\).  If \(s_0\mid\ell\) and
\(s_0\mid k\), then \(s_0\mid(\ell-k)=2H\), contradicting (6.7).
This proves (0.11).

When \(g=1\), the ordered slots form one \(2m\)-cycle.  The root positions
are a consecutive \(k\)-block on it.  Hence, as the macro is iterated,
its root sets are precisely the \(2m\) cyclic consecutive \(k\)-windows
of one coordinate order.  This is a genuine zero-monodromy interval
wreath, not merely a projected root cycle.

For \(r=1\), the middle-owner positions are also a consecutive
\(m\)-block on the same slot cycle.  Therefore the same orbit consists
of the \(2m\) cyclic middle windows.  This is an exact physical packet,
but it need not factor the even middle layer: in general
\(2m\nmid\binom{2m}{m}\).  The frozen exact middle-wreath theorem is on
the odd ground set \([2m+1]\) and cannot be invoked after the infinity
cut without an additional completion argument.

## 6A. Mixed block lengths do not remove monodromy by gcd

It is tempting to mix lengths \(r\) and \(r+1\), since
\(\gcd(\ell,r,r+1)=1\).  That gcd is vacuous.  The variable macros do
not commute, and there is a sharp one-lap obstruction.

Let \(R=O\) be the \(\ell\)-cycle on the top slots, fixing \(E\), and
put

\[
                         T=SR^{-1}.                           \tag{6A.1}
\]

In the indexing (6.1), \(T\) is the cycle supported on

\[
                         u_{m+1},E_{k-1},\ldots,E_0.          \tag{6A.2}
\]

Thus

\[
                         F_a=TR^a.                            \tag{6A.3}
\]

For a chronological word of positive block lengths
\(a_0,\ldots,a_{K-1}\), put \(A=\sum_i a_i\) and

\[
                         T_x=R^xTR^{-x}.                      \tag{6A.4}
\]

### Theorem 6A.1 (anchored-cycle closure equation)

The exact slot permutation of the word is

\[
\begin{aligned}
 P(\mathbf a)
 &:=F_{a_{K-1}}\cdots F_{a_0}\\
 &=T_0T_{a_{K-1}}
   T_{a_{K-1}+a_{K-2}}\cdots
   T_{a_{K-1}+\cdots+a_1}R^A.                               \tag{6A.5}
\end{aligned}
\]

Full closure is equivalent to \(P(\mathbf a)=1\); root-set closure is
equivalent to \(P(\mathbf a)E=E\), and ordered-root closure requires
pointwise return of the ordered \(E\)-slots.

#### Proof

Substitute (6A.3) and move each power of \(R\) rightward across the next
copy of \(T\).  Conjugation produces the successive suffix sums in
(6A.5).  The three closure statements are then definitions of full,
setwise-root, and ordered-root return. \(\square\)

### Theorem 6A.2 (one-lap mixed-length obstruction)

If every \(a_i>0\), \(K>0\), and

\[
                         \sum_i a_i=\ell,                    \tag{6A.6}
\]

then

\[
                         P(\mathbf a)\ne1,\qquad
                         P(\mathbf a)E\ne E.                 \tag{6A.7}
\]

#### Proof

The suffix anchors in (6A.5) are distinct modulo \(\ell\), because their
integer representatives form a strictly increasing sequence between
zero and \(\ell-1\).  Also \(R^A=1\).  Write the corresponding distinct
top slots as \(X_1,\ldots,X_K\).  Multiplying the anchored cycles in
(6A.5), or inducting on \(K\), shows that their product is the left
rotation by \(K\) on the ordered list

\[
                         (E_0,\ldots,E_{k-1},X_1,\ldots,X_K)  \tag{6A.8}
\]

and fixes every other top slot.  Its active cycle structure is

\[
 \gcd(k,K)\text{ cycles of length }{k+K\over\gcd(k,K)}.      \tag{6A.9}
\]

It is nonidentity.  The \(E\)-slots form a nonempty proper cyclic
interval in (6A.8), so a nonzero rotation does not preserve their set.
This proves (6A.7).  When \(K<k\), the image contains exactly \(K\) of
the \(X_i\)'s and \(k-K\) old root slots. \(\square\)

This obstruction has positive mixed \(r/(r+1)\) instances at every
sufficiently large reduced parameter.  Write

\[
                         \ell=qr+s,\qquad0\le s<r.            \tag{6A.10}
\]

If \(s>0\), take \(K=q\), with \(s\) blocks of length \(r+1\) and
\(q-s\) of length \(r\).  If \(s=0\), take \(K=q-1\), with \(r\)
blocks of length \(r+1\) and \(q-1-r\) of length \(r\).  For
\(\ell\gg r^2\), both counts are positive and their total stride is
exactly \(\ell\).  At the reduced scale,

\[
                         K\sim{\ell\over r}<k,                \tag{6A.11}
\]

so every ordering fails even root-set closure by Theorem 6A.2.

Thus mixing adjacent block lengths can tune the scalar owner count but
does not remove the ordered obstruction.  Longer multi-lap schedules
are not ruled out here; they must solve the full noncommutative equation
(6A.5) together with FIFO and owner capacity.  No gcd condition replaces
those equations.

One further count-only necessary condition follows from parity.  Since
\(T\) has sign \((-1)^k\) and \(R\) has sign \((-1)^{\ell-1}\), closure
requires

\[
                         Kk+A(\ell-1)\equiv0\pmod2.           \tag{6A.12}
\]

This condition, like the total stride, is far weaker than (6A.5).

## 7. Degree and codegree of the genuine root-wreath catalogue

Let one catalogue edge be the \(2m\) cyclic \(k\)-windows of an oriented
cyclic coordinate order, modulo rotation.  There are \((2m-1)!\) such
orders.

### Theorem 7.1 (exact incidences)

A fixed root belongs to

\[
                         D_R=k!\ell!                          \tag{7.1}
\]

catalogue cycles.  Two roots at Johnson distance \(d\), where
\(1\le d<k\), belong together to

\[
                         C_d=2(k-d)!(d!)^2(\ell-d)!           \tag{7.2}
\]

cycles, and hence

\[
                         {C_d\over D_R}
       ={2\over\binom kd\binom\ell d}.                       \tag{7.3}
\]

Two disjoint roots belong together to

\[
                         C_k=(2H+1)(k!)^2(2H)!               \tag{7.4}
\]

cycles, with relative ratio

\[
                         {2H+1\over\binom\ell k}.             \tag{7.5}
\]

The maximum distinct-root relative codegree is

\[
                         {2\over k\ell}.                     \tag{7.6}
\]

A fixed directed root arc occurs in

\[
                         (k-1)!(\ell-1)!                     \tag{7.7}
\]

cycles, and a fixed compatible consecutive arc pair occurs in

\[
                         (k-2)!(\ell-2)!                     \tag{7.8}
\]

cycles.

#### Proof

Rotate a cyclic order so a prescribed root begins at position zero.
Order its \(k\) labels and the \(\ell\) complementary labels, proving
(7.1).

For \(d<k\), the second root can overlap the first from the left or the
right.  In either orientation, order the four consecutive regions of
sizes \(d,k-d,d,\ell-d\).  This gives (7.2), and division proves (7.3).

For disjoint roots, the second interval can begin at any of the
\(\ell-k+1=2H+1\) positions which keep the two intervals disjoint.
Order the two root blocks and the remaining \(2H\) coordinates, giving
(7.4).  Formula (7.5) follows.  The maximum in (7.6) is at \(d=1\).

For a directed arc, the first departure and first arrival have fixed
positions; order the remaining root and complement labels.  For a
compatible consecutive pair, two departures and two arrivals have fixed
positions.  This proves (7.7)--(7.8). \(\square\)

Thus this physical catalogue has excellent pair geometry and an exact
uniform fractional root factor.  Its edge rank is \(2m\).  The authorized
growing-rank matching hypothesis contains an exponential factor in the
rank; already on the root catalogue the expression

\[
                         e^{4m}{2\over k\ell}\log D_R         \tag{7.9}
\]

diverges.  Hence the available theorem does not round the fractional
point.

## 8. Middle-owner completion and the exact remaining gate

There are two natural ways to combine the root cycles with reduced-scale
owner completion, and the preceding theorems separate both precisely.

### 8.1 Prebundle

A full \(F_r\)-cycle with \(g=1\) has \(2m\) root blocks and
\(2mr\) principal owner positions.  Treating it as one literal master
column therefore has physical rank

\[
                         2m(r+1).                             \tag{8.1}
\]

before the all-depth colour rows are counted.  A matching of such columns
could simultaneously complete owners and create mesoscopic components,
but the exponential rank loss is stronger than in (7.9).  Low root
pair codegree by itself does not imply integral packing.

The scalar owner count is already exact up to the unavoidable floor
remainder.  Put

\[
                         \lambda_H={W\over N_H},
       \qquad r=\lfloor\lambda_H\rfloor.                     \tag{8.2}
\]

If genuine cycles cover \(N_H-z\) roots, their declared principal-owner
occurrence count is

\[
 r(N_H-z)
 =W-N_H(\lambda_H-r)-rz.                                    \tag{8.3}
\]

Thus \(z=o(N_H)\) gives \(W-o(W)\) occurrences.  This is a count, not
owner completion: the occurrences must still be proved distinct and
must satisfy all target capacities.  If \(\gcd(\ell,r)>1\), taking
\(r=1\) with \(\lfloor\lambda_H\rfloor\) root-clone colours gives the
same scalar baseline, but again leaves the joint owner/root cycle
matching open.

Conditionally, suppose a multiset of coordinate cycles covers every
even middle owner exactly once (or covers the declared multiframe owner
resource with its prescribed constant multiplicity).  Each selected
cycle contributes its \(2m\) induced roots.  In the multiplicity-one
case the induced root ledger has total mass \(W\) and exact singleton
marginals

\[
                         {kW\over2m}.                         \tag{8.4}
\]

Indeed every coordinate occurs in exactly \(k\) root windows of each
coordinate cycle.  Therefore differences of induced root ledgers from
two such owner-complete coordinate-cycle systems lie in the
zero-singleton-marginal rectangle lattice.  The exact rectangle
relations give full **formal** algebraic mobility of that ledger.  They
do not supply either the hypothesized even owner factor or a nonnegative,
owner-preserving sequence whose intermediate root loads respect capacity.

### 8.2 Pack microchunks first

The dummy-completed, sparsified microchunk theorem gives an unconditional
owner near-packing at block length

\[
 r\asymp {\log m\over\log\log m}\ll H.                       \tag{8.5}
\]

Trying to fuse its selected blocks afterwards using only (2.3) admits
the projected Gray cycles of Section 3, but Theorem 5.2 proves that those
cycles have no ordered lift on all but an exponentially small root set.
The hidden queue suffix is selectable only before it is exposed; it
cannot be reordered at every seam to repair the violation.

Independent opening collars would cost, in the one-block-per-root
calibration \(r\sim\lambda_H\),

\[
                         2HN_H
       =\left({2H\over\log m}+o(1)\right)W,                   \tag{8.6}
\]

which is fatal.  A genuine interval-wreath near-factor would instead
have

\[
                         C=(1+o(1)){N_H\over2m}               \tag{8.7}
\]

components and collar allowance

\[
                         2HC=(1+o(1)){HN_H\over m}=o(W).      \tag{8.8}
\]

With cloned shorter microchunks, the same comparison is
\(2H\) times the number of microchunks versus \(2H\) times that number
divided by \(2m\); the latter is still \(o(W)\).

## 9. Exact proved/conditional boundary

Proved:

1. the local two-seam criterion and all degree/codegree formulas;
2. an explicit projected packing by exponentially long cycles covering
   \(1-e^{-\Omega(m)}\) of the roots;
3. a literal static collar-neutral re-root trade on every such cycle,
   which really connects successive fixed-root \(K_2\) option components;
4. the exact FIFO law and the exponentially strong obstruction to lifting
   the Gray bank;
5. the complete positional monodromy classification of
   \(F_r=S O^{r-1}\);
6. the exact genuine interval-wreath catalogue degrees and codegrees;
7. the favorable conditional collar ledger; and
8. formal rectangle-lattice mobility of induced root ledgers from exact
   middle-wreath factors.

Not proved:

1. a near-perfect integral matching of genuine interval-wreath root
   cycles;
2. simultaneous middle-owner completion and root capacity in that
   matching;
3. a nonnegative sequence of rectangle/re-root trades maintaining exact
   owner capacity at every prefix; or
4. coefficient one.

The projected root graph expands extremely well and has abundant long
cycles.  That avenue is exhausted: its cycles are spurious for literal
fusion because they ignore the ordered \(E/Q/P\) queues.  The surviving
positive problem is the integral owner-and-root packing of genuine
zero-monodromy interval wreaths.
