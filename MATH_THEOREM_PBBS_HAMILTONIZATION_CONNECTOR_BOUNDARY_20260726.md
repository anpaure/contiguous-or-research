# Centered PBBS Hamiltonization: exact connector atlas, the \(C_8\) obstruction, and a linear parity bridge

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, or web input is
used.

## 0. Verdict

Put

\[
 n=2r+1,\qquad {\cal X}=\binom{[n]}r,\qquad
 W=\binom nr,\qquad N=\binom n{r-1},
\]

\[
 {\sf C}_r=\operatorname {Cat}_r=\frac Wn,\qquad r\ge2.
\tag{0.1}
\]

Let \(f\) be the canonical cyclic-parenthesis/PBBS permutation of
\({\cal X}\). At the upper Middle Levels vertex \(U_Z=[n]\setminus Z\),
use the two perfect matchings

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z).
\tag{0.2}
\]

The centered Johnson factor \(M_0\cup M_1\) has monodromy \(f^{-2}\), at
most \({\sf C}_r\) components, exact upper ownership, and raw opposite
triple-union defect

\[
 \beta_r^{\rm PBBS}=W-N=\frac{2W}{r+2}<4{\sf C}_r.
\tag{0.3}
\]

This note proves the following sharp connector package.

1. The natural exchange digraph has exactly

   \[
   N-n
   \tag{0.4}
   \]

   directed triangles. They are completely classified. Their physical
   support hypergraph is linear and has a vertex-disjoint reservoir of
   size

   \[
   \frac{N-n}{3r-2}
      =\left(\frac23+o(1)\right){\sf C}_r.
   \tag{0.5}
   \]

2. The natural exchange digraph has no directed \(4\)-cycle. Thus the
   previously proposed physically disjoint initial \(C_8\) parity bridge
   does not exist.

3. There is instead an explicit directed \(C_{2n}\). Its alternating
   Middle Levels lift changes \(2n=4r+2\) matching slots and reverses
   component parity. Its exact component derivative is

   \[
   \Delta c=
   \begin{cases}
   -1,&3\nmid n,\\
   +1,&3\mid n,
   \end{cases}
   \tag{0.6}
   \]

   with \(\Delta c=-1\) also at \(r=2\).

4. The bridge destroys at most \(2nr\) members of the triangle atlas, so
   the post-bridge state has a disjoint reservoir of size at least

   \[
   \frac{N-n-2nr}{3r-2}
      =\left(\frac23+o(1)\right){\sf C}_r.
   \]

5. A precise quotient representative lemma, stated in Section 6, would
   Hamiltonize the factor with at most

   \[
   2n+\frac32{\sf C}_r
   \tag{0.7}
   \]

   changed slots and would give

   \[
   \beta_r\le
   \frac{2W}{r+2}+2n+\frac32{\sf C}_r
   =O({\sf C}_r).
   \tag{0.8}
   \]

The quotient representative lemma is not proved. Consequently this note
does **not** prove an unconditional Hamiltonization, the GMM base theorem,
or coefficient one. What is closed is the entire local and parity part
of the connector problem. The surviving gate for the pairwise-disjoint,
monotone three-way \(C_6\)-fusion scheme is the phase/rigging-sensitive
component quotient Hall condition in Section 6.

## 1. The natural exchange digraph

For \(Z\in{\cal X}\), let \(p_+(Z)\) be the unique zero left by cyclic
forward \(10\)-matching. Then

\[
 f(Z)=Z^c\setminus\{p_+(Z)\},\qquad
 f(Z)^c=Z\cup\{p_+(Z)\}.
\tag{1.1}
\]

If the old \(M_1\)-edge at \(U_Z\) is moved to \(U_X\), incidence and
avoidance of \(M_0\) give the exact arrow test

\[
 Z\longrightarrow X
 \quad\Longleftrightarrow\quad
 f(Z)\cap X=\varnothing,\qquad X\notin\{Z,f^2(Z)\}.
\tag{1.2}
\]

Every nonloop candidate therefore has the form

\[
 X=Z-a+p_+(Z),\qquad a\in Z.
\tag{1.3}
\]

A directed \(t\)-cycle in (1.2) is an alternating Middle Levels
\(C_{2t}\). Switching it leaves \(M_0\) fixed, replaces \(M_1\) by
another perfect matching, and changes exactly \(t\) \(M_1\)-slots. If

\[
 \sigma=M_1^{-1}M_0,
\]

then the switch left-multiplies \(\sigma\) by the corresponding
\(t\)-cycle.

## 2. Complete directed-triangle classification

Three pairwise adjacent \(r\)-sets form either a star

\[
 C+x_0,\ C+x_1,\ C+x_2,\qquad |C|=r-1,
\tag{2.1}
\]

or a top

\[
 K+ab,\ K+bc,\ K+ca,\qquad |K|=r-2.
\tag{2.2}
\]

A directed top is impossible. Indeed, if \(Q\) is the common
\((r+1)\)-set and \(Z\to X\) is one side, (1.3) gives
\(Z\cup\{p_+(Z)\}=Q\), whence \(f(Z)=Q^c\). Two distinct sources would
have the same \(f\)-image.

Fix a core \(C\in\binom{[n]}{r-1}\). Its three forward-unmatched zeros
give the unique cyclic decomposition

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,
\tag{2.3}
\]

where the \(D_i\) are Dyck words and indices are modulo three. Put
\(Z_i=C+z_i\). Contracting the matched pairs in the \(D_i\)'s gives

\[
 p_+(Z_i)=z_{i+2}.
\tag{2.4}
\]

Thus the only possible orientation is

\[
 Z_0\longrightarrow Z_2\longrightarrow Z_1\longrightarrow Z_0.
\tag{2.5}
\]

Let \(p_-\) denote the reverse \(01\)-survivor. The side
\(Z_i\to Z_{i+2}\) collides with \(M_0\) exactly when

\[
 p_-(C+z_{i+2})=z_i.
\tag{2.6}
\]

The reverse rightmost-maximum rule applied to (2.3) gives the exact
criterion

\[
 p_-(C+z_j)=z_{j+1}
 \quad\Longleftrightarrow\quad
 D_j=D_{j+1}=\varnothing,\quad
 \operatorname {ht}(D_{j+2})\le1.
\tag{2.7}
\]

Indeed, rotate \(C+z_j\) to

\[
 1D_j\,0_{z_{j+1}}D_{j+1}\,0_{z_{j+2}}D_{j+2}.
\]

The reverse survivor is the zero following the rightmost global maximum.
For that maximum to occur immediately before \(z_{j+1}\), the first two
blocks must be empty and the last block must never rise two levels.
Conversely those conditions make the displayed maximum unique on its
right.

Since the total semilength of \(D_0,D_1,D_2\) is \(r-1\), (2.7) holds
for some side exactly when the core is a rotation of

\[
 000(10)^{r-1}.
\tag{2.8}
\]

This word has full period \(n\). Hence exactly \(n\) cores are illegal,
and the exact directed-triangle count is \(N-n\).

## 3. Physical supply and the component information it does—and does not—give

Let \({\cal H}_r\) be the \(3\)-graph on \({\cal X}\) formed by the legal
star triples. Two distinct triples share at most one center, since two
shared \(r\)-sets recover their common \((r-1)\)-core. A center \(Z\)
can occur only in a core \(Z-x\), \(x\in Z\). Therefore

\[
 {\cal H}_r\ \hbox{is linear},\qquad
 \Delta({\cal H}_r)\le r.
\tag{3.1}
\]

Greedy deletion after choosing one hyperedge removes at most
\(1+3(r-1)=3r-2\) hyperedges. This proves (0.5). Because \(Z\mapsto
U_Z\) and \(f\) are bijections, disjoint center triples give physically
vertex-disjoint alternating hexagons.

There are genuine three-component connectors. For a core (2.3), the
normalized Dyck roots of its three centers are

\[
 E_i=D_{i+2}\,1D_i0\,D_{i+1}.
\tag{3.2}
\]

Let \(\partial\) delete all current \(10\)-peaks and define the PBBS
action profile

\[
 {\bf a}(D)=
 \bigl(\operatorname {pk}(D),
       \operatorname {pk}(\partial D),
       \operatorname {pk}(\partial^2D),\ldots\bigr).
\tag{3.3}
\]

Peak-deletion semiconjugacy makes this profile constant on every PBBS
orbit. It is additive under Dyck concatenation, and

\[
 {\bf a}(1D0)={\bf a}(D)+{\bf e}_{\operatorname {ht}(D)+1}.
\tag{3.4}
\]

Consequently

\[
 {\bf a}(E_i)=
 \sum_{j=0}^2{\bf a}(D_j)
 +{\bf e}_{\operatorname {ht}(D_i)+1}.
\tag{3.5}
\]

Pairwise distinct block heights put the three centers in distinct
\(f\)-orbits and therefore in distinct \(f^{-2}\)-components. For every
\(r\ge4\), the legal choice

\[
 D_0=\varnothing,\qquad D_1=10,\qquad
 D_2=1^{r-2}0^{r-2}
\tag{3.6}
\]

has heights \(0,1,r-2\), proving existence.

For \(r\ge3\), the profile quotient is connected: wrapping a nonempty
Dyck block of
height \(h\) can be replaced, through a legal star, by wrapping the empty
block, changing

\[
 {\bf a}\longmapsto{\bf a}-{\bf e}_{h+1}+{\bf e}_1.
\tag{3.7}
\]

This strictly decreases

\[
 \Psi({\bf a})=\sum_{s\ge1}(s-1)a_s
\]

until the alternating profile \(r{\bf e}_1\) is reached. The sole
exceptional first move, from
\((r-1){\bf e}_1+{\bf e}_2\), is bypassed by splitting \(r-1\) into two
positive alternating blocks. Thus no obstruction measurable only by
the action profile exists.

Every \(f^{-2}\)-component also has some legal portal. If
\(D=F_1\cdots F_k\) is the primitive-factor decomposition, a center
\(0_pD\) lies in the star obtained by deleting \(x\) exactly when \(x\)
is the first up-step of some \(F_j=1A_j0\). The three blocks are the
prefix before \(F_j\), \(A_j\), and the suffix after \(F_j\). Applying
(2.7) shows that, for \(r\ge3\), the only center with no legal star is

\[
 D=1(10)^{r-1}0.
\tag{3.8}
\]

Its next step-two PBBS state is

\[
 1100(10)^{r-2},
\tag{3.9}
\]

which has a legal portal. Hence, for \(r\ge3\), no whole
\(f^{-2}\)-component is portal-free.

These conclusions do **not** prove component-quotient connectivity or a
loose spanning tree. Components inside one action profile retain
phase/rigging data, and quotienting the physically linear hypergraph can
create repeated component pairs.

## 4. Exact obstruction to a natural \(C_8\)

There is no directed \(4\)-cycle in the natural exchange digraph, even if
the collision exclusion \(X\ne f^2(Z)\) is dropped.

Suppose otherwise. Let \(A_0,A_1,A_2,A_3\) be the old lower endpoints
of the four \(M_1\)-edges in cyclic order. If \(p_-(A_i)\) is the reverse
survivor, alternation gives

\[
 A_i\cup\{p_-(A_i)\}=A_{i-1}\cup A_i,\qquad
 p_-(A_i)=A_{i-1}\setminus A_i.
\tag{4.1}
\]

The \(A_i\)'s form a Johnson \(4\)-cycle with four distinct consecutive
unions. Its only possible shapes are:

\[
 A_i=S+x_i
\tag{4.2}
\]

for a common \((r-1)\)-set \(S\), or, after relabeling,

\[
\begin{aligned}
 A_0&=C+ac,&A_1&=C+bc,\\
 A_2&=C+bd,&A_3&=C+ad
\end{aligned}
\tag{4.3}
\]

for a common \((r-2)\)-set \(C\).

In the star case, (4.1) requires four distinct reverse survivors after
changing one zero of a deficit-three word. Reverse clean-label
contraction says every survivor is one of the three old unmatched zeros,
a contradiction.

In the rectangle case, (4.1) requires

\[
 p_-(C+ac)=d,\quad p_-(C+bc)=a,\quad
 p_-(C+bd)=c,\quad p_-(C+ad)=b.
\tag{4.4}
\]

All four labels lie among the five reverse-unmatched zeros of \(C\).
Contract all reverse-matched pairs and label the five survivors cyclically
by \(0,1,2,3,4\). If a pair \(P\) is changed to ones, the unique survivor
is

\[
\begin{array}{c|cccccccccc}
P&01&12&23&34&40&02&13&24&30&41\\ \hline
s(P)&2&3&4&0&1&3&4&0&1&2.
\end{array}
\tag{4.5}
\]

Rotate \(a\) to \(0\). The equation \(s(bc)=0\) leaves only the ordered
possibilities

\[
 (b,c)=(3,4),(4,3),(2,4),(4,2).
\]

Inserting \(d=s(0c)\) into the remaining equations fails respectively at
\(s(0,1)\), \(s(4,1)\), \(s(2,1)\), and \(s(4,3)\). This contradiction
proves the claim.

Therefore a physically disjoint atlas consisting of initial natural
hexagons plus one initial natural \(C_8\) cannot exist. Any \(C_8\)
created later must meet the physical vertex support of an earlier switch.

## 5. An explicit linear parity bridge

All subscripts are modulo \(n\). Define

\[
 A_b=\{b-2,b-4,\ldots,b-2r\},
\qquad
 T_b=A_b-\{b-2\}+\{b\}.
\tag{5.1}
\]

Direct cyclic cancellation gives

\[
\begin{aligned}
 p_+(A_b)&=b,& f(A_b)&=A_{b+1},\\
 p_+(T_b)&=b-1,& f^3(T_b)&=T_{b+1},
\end{aligned}
\tag{5.2}
\]

and

\[
\begin{aligned}
 f^2(A_b)&=A_b-\{b+1\}+\{b\},\\
 f^2(T_b)&=T_b-\{b+1\}+\{b-1\}.
\end{aligned}
\tag{5.3}
\]

Thus

\[
 A_b\longrightarrow T_b\longrightarrow A_{b-2}
\tag{5.4}
\]

are legal arrows: the first removes \(b-2\), not the forbidden \(b+1\);
the second removes \(b\), again not \(b+1\). Since \(2\) generates the
additive cyclic group modulo odd \(n\), (5.4) is a simple directed
\(C_{2n}\).

For the component calculation, put \(b_j=b_0-2j\),

\[
 a_j=U_{A_{b_j}},\qquad t_j=U_{T_{b_j}},
\]

and

\[
 \tau=(a_0\,t_0\,a_1\,t_1\,\cdots\,a_{n-1}\,t_{n-1}).
\tag{5.5}
\]

The old monodromy is

\[
 \sigma(U_Z)=U_{f^{-2}(Z)}.
\]

The \(a_j\)'s form one complete \(\sigma\)-cycle with
\(\sigma(a_j)=a_{j+1}\). For \(r\ge3\), the \(T_b,f(T_b),f^2(T_b)\)
are three disjoint rotation families and form one \(f\)-cycle of length
\(3n\); hence the \(t_j\)'s lie in one \(\sigma\)-cycle with

\[
 \sigma^3(t_j)=t_{j+1}.
\tag{5.6}
\]

Cut the incoming \(\sigma\)-arcs at every \(a_j,t_j\). In
\(\tau\sigma\), the old \(T\)-segment beginning at \(t_j\) is followed
by \(a_{j+2}\) and then by the segment beginning at \(t_{j+3}\). The
return permutation of the \(n\) old \(T\)-segments is therefore

\[
 j\longmapsto j+3.
\tag{5.7}
\]

The two old components become \(\gcd(n,3)\) components, proving (0.6).
For \(r=2\), the return shift is \(j\mapsto j+4\pmod5\), so it also has
one cycle and \(\Delta c=-1\).

The multiplier (5.5) is an even-length cycle and hence odd. Thus its
parity reversal also follows abstractly, but (5.7) gives the exact
component count.

The bridge support has \(2n\) centers. By (3.1), deleting every natural
hexagon meeting it removes at most \(2nr\) atlas edges. Every remaining
hexagon is physically disjoint from the bridge and remains alternating.
Consequently the post-bridge atlas has at least

\[
 N-n-2nr
\tag{5.8}
\]

members and a physically disjoint subfamily of size at least

\[
 \frac{N-n-2nr}{3r-2}
   =\left(\frac23+o(1)\right){\sf C}_r.
\tag{5.9}
\]

## 6. Exact remaining static quotient theorem

If the initial component count \(c\) is odd, do not use the long bridge.
If \(c\) is even, use it once. In either case let \(F^\ast\) be the
resulting factor and \(c^\ast\) its odd number of components. From
(0.6),

\[
 c^\ast\le {\sf C}_r+1.
\tag{6.1}
\]

Let \({\cal A}^\ast\) be the natural legal hexagons which are physically
disjoint from the optional bridge, and project each member to the set of
components of \(F^\ast\) containing its three centers.

If \(c^\ast=1\), then \(F^\ast\) is already Hamiltonian and no hexagon is
needed. Assume henceforth that \(c^\ast\ge3\). The following is the exact
unproved representative statement needed by the pairwise-disjoint,
monotone three-way fusion route.

> **PBBS quotient representative loose-tree lemma \(({\rm QRL}_r)\).**
> There is a family \({\cal T}\subseteq{\cal A}^\ast\) such that:
>
> 1. its physical hexagons are pairwise vertex-disjoint;
> 2. every projected edge consists of three distinct \(F^\ast\)-components;
> 3. every \(F^\ast\)-component occurs in some projected edge;
> 4. \(|{\cal T}|=(c^\ast-1)/2\); and
> 5. for every nonempty \({\cal S}\subseteq{\cal T}\),
>
>    \[
>    \left|\bigcup_{e\in{\cal S}}e\right|
>       \ge 2|{\cal S}|+1.
>    \tag{6.2}
>    \]

### Theorem 6.1 (the quotient lemma implies Catalan-edit Hamiltonization)

If \(c^\ast=1\), or if \(c^\ast\ge3\) and \(({\rm QRL}_r)\) holds, the
centered PBBS factor can be changed to a Middle Levels Hamilton cycle
using at most

\[
 2n+\frac32{\sf C}_r
\tag{6.3}
\]

matching-slot changes, and the projected Johnson Hamilton cycle satisfies
(0.8).

#### Proof

If \(c^\ast=1\), the optional bridge has already produced a Hamilton
factor. It used at most \(2n\) slots, and the same Lipschitz argument below
gives the stated defect bound. Assume \(c^\ast\ge3\).

Condition (6.2) for two selected triples says that they meet in at most
one component. Thus the projected selected \(3\)-graph is linear.
Inside any connected selected subhypergraph with \(e\) edges, successive
connected edges show \(v\le2e+1\); (6.2) gives the reverse inequality.
Every connected block is therefore a loose tree. If there were \(k\)
blocks, their full union would have \(2|{\cal T}|+k\) vertices. Conditions
3 and 4 make this number

\[
 c^\ast=2|{\cal T}|+1,
\]

so \(k=1\). The projected family is a loose spanning tree.

Root this tree and order its edges outward. The first switch meets three
old components. Every later edge meets the already fused component once
and introduces two untouched components. Hence each directed
\(C_3\)-switch reduces the component count by two. Physical
vertex-disjointness ensures that every later hexagon is still alternating.
After \((c^\ast-1)/2\) switches, one component remains.

If the bridge was used, it changed \(2n\) slots. The hexagons change
\(3(c^\ast-1)/2\le3{\sf C}_r/2\) slots by (6.1). This proves (6.3).

Changing one matching slot changes at most one opposite triple-union
occurrence. The support deficit of a fixed-cardinality occurrence
multiset is \(1\)-Lipschitz under one replacement. Starting from (0.3)
therefore gives (0.8). \(\square\)

The scalar reservoir (5.9) is larger than the at most
\({\sf C}_r/2\) hexagons required in Theorem 6.1. It does not prove
\(({\rm QRL}_r)\): quotienting can collapse two physical centers into one
component label, and many quotient edges may reuse the same component
pair.

## 7. Strongest unconditional boundary

The following are unconditional.

1. The local \(C_6\) atlas is exactly classified and has the required
   Catalan-scale disjoint supply.
2. For \(r\ge3\), every PBBS component has a legal portal.
3. Three-component connectors exist in every rank \(r\ge4\).
4. For \(r\ge3\), the action-profile quotient is connected; no
   soliton-content cut can obstruct all connectors.
5. The natural \(C_8\) bridge is exactly impossible.
6. The explicit \(C_{2n}\) solves parity at \(O(r)\) slot cost and, as
   \(r\to\infty\), leaves a Catalan-scale \(C_6\) supply intact.

What remains unproved is \(({\rm QRL}_r)\), or a dynamic replacement for
it. More weakly, even ordinary connectivity of the labelled
\(f^{-2}\)-component quotient is not yet proved. Ordinary connectivity
would still not imply (6.2) or physical representative disjointness.

Thus the route neither proves nor refutes the existence of an
\(O({\sf C}_r)\)-edit Hamiltonization. It proves an exact obstruction to
the former \(C_8\)-based connector plan, supplies a valid parity
replacement, and isolates the remaining theorem for the
pairwise-disjoint monotone \(C_6\)-tree scheme at the phase/rigging
quotient.

## 8. Adversarial audit

1. **Local supply versus quotient Hall.** The count \(N-n\) and the
   packing (0.5) contain no component labels. Neither implies
   \(({\rm QRL}_r)\).
2. **Profiles versus physical components.** Distinct profiles separate
   components, but equal profiles can contain many PBBS cycles. Profile
   connectivity is only a coarse quotient statement.
3. **Portals versus three-way merges.** A legal portal may meet one or
   two components. Existence of one portal in every component does not
   imply a component-transversal edge.
4. **No \(C_8\) versus no parity bridge.** Only the natural directed
   \(4\)-cycle is impossible. Section 5 gives a valid longer even
   circuit.
5. **The \(3\mid n\) case.** The long bridge then increases the component
   count by one, but still reverses parity and changes only \(O(r)\)
   slots. The bound \(c^\ast\le{\sf C}_r+1\) includes this case.
6. **Physical disjointness after the bridge.** Avoiding its \(2n\)
   center indices also avoids its lower endpoints because \(f\) is a
   bijection. The remaining hexagons really are physically disjoint from
   it.
7. **Edit accounting.** A \(t\)-cycle switch changes \(t\), not \(2t\),
   matching slots. Its Middle Levels circuit has length \(2t\), but only
   the \(t\) movable matching edges are replaced.
8. **False isolation arguments.** Rotating a chosen occupied coordinate
   cannot simultaneously normalize the pre-existing double-zero seam.
   No alternating-component isolation claim is used here.
9. **Scope of the obstruction.** The no-\(C_8\) theorem refutes one
   static initial bridge. It is not an obstruction to a later
   dynamically created \(C_8\), to the long bridge, or to an unrelated
   Hamiltonization.

Independent audits of the two main ingredients are recorded in
MATH_AUDIT_PBBS_PAIRED_C6_CLASSIFICATION_AND_EXCHANGE_CUT_20260726.md
and MATH_AUDIT_PBBS_C6_C8_CONNECTOR_PACKAGE_20260726.md.
