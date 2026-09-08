# Thread A: the Hall-22 neutral router, remote circuit splitter, and the exact routing gate

Date: 2026-07-28

Status: exact \(H23\to H23\to H22\) certificate; proved DM-circuit,
overlapping-suffix splitter, native-pin, and decorated router--splitter
theorems; exact critical-shore common-word certificate. Universal neutral
routing, a common-\(Q_x\) maximum matching, and \(H22\to H21\) remain open.

## 0. Result and scope

The verified braid chain is

\[
 H23\xrightarrow{\rho=\operatorname{RF}(3799,4497,6039)}
 H23^{\rm port}
 \xrightarrow{\sigma=\operatorname{FR}(740,4051,6137)}H22.       \tag{0.1}
\]

The matching ranks and deficiencies are

\[
\begin{array}{c|ccc}
 &H23&H23^{\rm port}&H22\\ \hline
 \nu&16360&16360&16361\\
 \operatorname{def}&23&23&22.
\end{array}                                                       \tag{0.2}
\]

Each state contains every one of the \(6435\) rank-eight owners exactly once,
is a Johnson path, is depth-three resident, has nonempty maximal controller
and exact central reconstruction, and has complete upper support at every
depth \(1,\ldots,7\). The immediate lower layer has four holes and the same
seven degree-zero lower targets throughout. The complete lower vectors, which
are not all equal, appear in (6.10).

The two moves have cleanly separated functions.

* The neutral braid \(\rho\) rotates a two-column Boolean packet in the
  \(161/160\) DM component rooted at \(24610\), without changing that
  component's rank. It does not change the remote \(2/1\) component
  \(\{4877,4909\}\).
* The improving braid \(\sigma\) makes no cell-shore change incident with
  the \(24610\) component. Restricted to the old \(2/1\) component, it
  replaces its single common shore \(\{4877,4909\}\) by two separate shores
  \(\{4877\}\) and \(\{4909\}\), and removes this whole component from the
  final canonical DM shore.

Thus the proved architecture is

\[
 \boxed{\text{neutral chronology/legality router}
        \quad+\quad
        \text{remote DM-circuit basis ear}.}                       \tag{0.3}
\]

The word *router* is literal. Applying \(\sigma\) directly to \(H23\),
without \(\rho\), gives non-Johnson seams at final edges \(739\) and \(2826\),
both of symmetric-difference size \(8\), and five depth-three residence
violations

\[
 (2,737,739),\ (2,2826,2826),\ (6,740,742),\
 (6,2827,2828),\ (7,739,741).                         \tag{0.4}
\]

Here each triple is (coordinate, first position, last position). After
\(\rho\), the same nominal splitter is legal and resident.

This note proves the exact state-dependent groupoid theorem which turns an
orbit hit into a Hall descent. It does **not** prove that every remaining
circuit port lies in such an orbit. It also distinguishes three levels which
must not be conflated:

1. projected Hall matching;
2. a simultaneous literal matching on the critical DM shore;
3. one common-\(Q_x\) maximum matching on all matched targets.

Level 2 is proved for (0.1); level 3 is not.

## 1. Exact physical compiler

Let \(T=(T_0,\ldots,T_{W-1})\) be a rank-eight Johnson path, where
\(W=\binom{15}{8}=6435\), and let

\[
 P=(P_0,\ldots,P_{W+2})=E^3T                         \tag{1.1}
\]

be its maximal depth-three erosion. In every carrier considered here,

\[
 P_p\ne\varnothing\quad(0\le p<W+3),\qquad
 T_i=P_i\cup P_{i+1}\cup P_{i+2}\cup P_{i+3}.       \tag{1.2}
\]

For \(x\in T_i\), write

\[
 C(i,x)=\{p\in[i,i+3]:x\in P_p\}.                   \tag{1.3}
\]

Residence and (1.2) make this set nonempty. A physical lower cell is an
interval

\[
 c=(q,s),\qquad I_c=[s,s+q],\qquad q\in\{0,1,2\}.   \tag{1.4}
\]

Define its envelope and forced mask by

\[
 E_c=\bigcup_{p\in I_c}P_p,
 \qquad
 M_c=\{x:\ \exists\,0\le i<W,\ x\in T_i,\
                    C(i,x)\subseteq I_c\}.           \tag{1.5}
\]

Only nonempty carrier sets in (1.3) occur in the second definition. The
exact neighbourhood of \(c\) among the \(16383\) nonempty targets of ranks
at most seven is

\[
 \Gamma(c)=\left\{
 S:\ 1\le |S|\le7,\quad
 M_c\subseteq S\subseteq E_c,\quad
 S\cap P_p\ne\varnothing\ (p\in I_c)
 \right\}.                                             \tag{1.6}
\]

This is the full-cell predicate used below. In particular, all occurrences
of “shore” mean (1.6), with multiplicity, unless a restriction to a named DM
component is explicitly stated.

### Lemma 1.1 (the native cell edge)

For every cell \(c\), \(M_c\subseteq E_c\). If \(1\le |E_c|\le7\), then

\[
                         E_c\in\Gamma(c).             \tag{1.7}
\]

#### Proof

If \(x\in M_c\), then a nonempty carrier set \(C(i,x)\) is contained in
\(I_c\). Hence \(x\) occurs in some \(P_p\), \(p\in I_c\), and so
\(x\in E_c\). Each \(P_p\) is nonempty and is contained in \(E_c\), proving
all three conditions in (1.6) for \(S=E_c\). \(\square\)

Call \(\tau(c)=E_c\) the **native trace** of \(c\).

### Lemma 1.2 (native common-pin lemma)

Let \(\mathcal C_0\) be cells whose native traces have rank at most seven and
are pairwise distinct. Then

\[
                         c\longmapsto\tau(c)           \tag{1.8}
\]

is a target--cell matching, and all its pins are realized simultaneously by
the one word \(P\).

Equivalently, these pins pass the exact common-\(Q_x\) criterion without any
additional coordinate deletion.

#### Proof

Lemma 1.1 gives every edge in (1.8), and distinct traces give injectivity.
By definition,

\[
                         \bigcup_{p\in I_c}P_p=\tau(c) \tag{1.9}
\]

for every selected cell. Therefore \(P\) realizes all pins at once. More
explicitly, a negative pin for coordinate \(x\notin\tau(c)\) forbids \(x\)
on \(I_c\), but \(x\) is already absent from every \(P_p\), \(p\in I_c\).
Thus native pins do not shrink the maximal allowed sets \(Q_x\); all central
and pin-positive hits remain those of \(P\). \(\square\)

This lemma is strong enough for the critical-shore certificate in Section 6,
but says nothing about nonnative exterior matching edges.

## 2. DM circuits and exact component discharge

Let \(G=(L,R;E)\) be bipartite and \(M\) a maximum matching. Start alternating
reachability from every \(M\)-unmatched left vertex, and let
\((Z_L,Z_R)\) be the resulting canonical deficient region. Decompose the
induced graph into connected components

\[
                         D_j=(X_j,Y_j).                \tag{2.1}
\]

### Theorem 2.1 (DM component additivity)

Every \(y\in Y_j\) is \(M\)-matched to a vertex of \(X_j\), and

\[
 |X_j|-|Y_j|
 =\#\{\text{\(M\)-unmatched left roots in }X_j\}.      \tag{2.2}
\]

Consequently

\[
 \operatorname{def}(G)=|Z_L|-|Z_R|
 =\sum_j(|X_j|-|Y_j|).                                \tag{2.3}
\]

#### Proof

A reachable unmatched right vertex would terminate an augmenting path, so
every reachable right vertex is matched. Its mate is reached by the next
alternating step and lies in the same connected component. Thus \(M\)
matches all of \(Y_j\) internally, leaving exactly the difference in (2.2)
exposed. Summation gives (2.3). \(\square\)

### Theorem 2.2 (every unit DM component is a transversal circuit)

If \(|X|=|Y|+1\) for one component \(D=(X,Y)\), then for every \(x\in X\),

\[
                         X\setminus\{x\}\quad
 \text{matches bijectively to }Y.                    \tag{2.4}
\]

#### Proof

There is one exposed root \(r\) in \(X\). Every \(x\in X\) is reached from
\(r\) by an alternating path. Flipping that path moves the exposed vertex
from \(r\) to \(x\), while matching every other member of \(X\) to \(Y\).
\(\square\)

Thus “circuit” applies to all 23 H23 components, not only to its \(2/1\)
components.

### Theorem 2.3 (complement-safe circuit discharge)

Let \(G_0\) have deficiency \(h\), maximum matching \(M\), and a unit DM
component \(D=(X,Y)\). Suppose a final graph \(G_1\) has:

1. a matching \(M_{\rm out}\) of size \(|M|-|Y|\) on the old matched targets
   outside \(X\);
2. a matching \(M_D\) saturating \(X\); and
3. disjoint right endpoints for \(M_{\rm out}\) and \(M_D\).

Then

\[
 \nu(G_1)\ge\nu(G_0)+1,
 \qquad
 \operatorname{def}(G_1)\le h-1.                    \tag{2.5}
\]

If \(G_1\) has a target shore of gap \(h-1\), then equality holds in (2.5).

#### Proof

The disjoint union has size

\[
 (|M|-|Y|)+|X|=|M|+1,                               \tag{2.6}
\]

because \(|X|=|Y|+1\). The residual shore supplies the reverse Hall bound
when exact equality is asserted. \(\square\)

The size in item 1 is essential: the other \(h-1\) deficient components
still have exposed roots, so one must not demand saturation of all
\(L\setminus X\).

Without an explicit complement matching, the exact equivalent all-shore
condition for \(\operatorname{def}(G_1)\le h-1\) is

\[
 |N_{G_1}(A)|-|N_{G_0}(A)|
 \ge |A|-|N_{G_0}(A)|-(h-1)
 \qquad(A\subseteq L).                               \tag{2.7}
\]

Hence a local split is not, by itself, a global Hall proof.

## 3. The exact two-target suffix splitter

The successful remote ear has a useful controller-level normal form.

### Theorem 3.1 (overlapping-suffix splitter)

Let \(P_s,P_{s+1},P_{s+2}\) be three consecutive nonempty controller states.
Assume

\[
 S=P_{s+1}\cup P_{s+2},\qquad |S|=6,                 \tag{3.1}
\]

and

\[
 E=P_s\cup P_{s+1}\cup P_{s+2}=S\cup\{e\},\qquad |E|=7. \tag{3.2}
\]

Let \(c^-=(1,s+1)\) and \(c^+=(2,s)\). If

\[
                         e\in M_{c^+},                \tag{3.3}
\]

then, after restricting the full cell shores to the two targets
\(\{S,E\}\),

\[
 \Gamma(c^-)\cap\{S,E\}=\{S\},
 \qquad
 \Gamma(c^+)\cap\{S,E\}=\{E\}.                    \tag{3.4}
\]

#### Proof

The envelope of \(c^-\) is \(S\), and Lemma 1.1 gives \(M_{c^-}\subseteq S\).
Both controller states meet \(S\), so \(S\in\Gamma(c^-)\); \(E\) is not a
subset of its envelope. The envelope of \(c^+\) is \(E\), so
\(E\in\Gamma(c^+)\) by Lemma 1.1. Condition (3.3) excludes \(S\) from that
cell. This proves (3.4). \(\square\)

Condition (3.3) is itself physical, not a free label: by (1.5), it says that
some central occurrence of \(e\) has its complete carrier set contained in
\([s,s+2]\). The theorem therefore keeps the endpoint-conditioned mandatory
ledger exact.

There is no naked coordinate obstruction to (3.1)--(3.2). For any
\(S\in\binom{[15]}6\), \(e\notin S\), choose distinct \(u,v\in S\), choose
\(w\in S\setminus\{u\}\), and put

\[
 P_{s+1}=S\setminus\{u\},\quad
 P_{s+2}=S\setminus\{v\},\quad
 P_s=(S\setminus\{u,w\})\cup\{e\}.                 \tag{3.5}
\]

These are rank-five states; consecutive pairs are Johnson adjacent and they
satisfy (3.1)--(3.2). What remains nonlocal is to embed such a triple with
(3.3), legal seams, residence, exact middle ownership, protected support,
and a complement/common-\(Q_x\) certificate.

A \(1/0\) DM component is the boundary case of Theorem 2.3: it requires a
first cell adjacent to its one target. It cannot literally be discharged by
splitting an existing shared shore. Larger unit components likewise require
a new independent basis ear, not necessarily a binary shore split.

## 4. The decorated neutral-braid groupoid

A three-cut braid is invertible as a block permutation, but whether it is
legal depends on its source carrier. The correct algebra is therefore a
state-dependent groupoid.

Fix a protected package \(\mathcal I\). Its shadow part is a fixed baseline
list of targets or named occurrences which every state must retain; it does
not include accidental extra support. This distinction is necessary for
reversibility when a later directed splitter gains a new target. An object at
deficiency \(h\) consists of:

1. a middle deck, oriented Johnson path, and its exact maximal controller;
2. exact residence and protected lower/upper support witnesses;
3. the full cell graph (1.6), a maximum matching, and its DM decomposition;
4. an exterior matching service for any marked circuit port; and
5. when literal preservation is claimed, that same maximum matching, written
   as a target-to-cell injection \(\phi\), together with its common-\(Q_x\)
   witnesses.

When a particular component is to be discharged, the object is additionally
marked by that component, its current basis, and its exposed-root
identification. A neutral arrow must explicitly transport this marked port.
It is not enough that an unrelated component at the endpoint has the same
cardinalities.

For the last item, if \(I_{\phi(S)}\) is the assigned physical interval, set

\[
 Q_x(\phi)=\{p:x\in P_p\}
 \setminus
 \bigcup_{\substack{S\in\operatorname{dom}\phi\\x\notin S}}
 I_{\phi(S)}.                                       \tag{4.1}
\]

The injection is realized by one nonzero physical word if and only if

\[
\begin{aligned}
 Q_x(\phi)\cap[i,i+3]&\ne\varnothing &&(x\in T_i),\\
 Q_x(\phi)\cap I_{\phi(S)}&\ne\varnothing &&(x\in S),\\
 \{x:p\in Q_x(\phi)\}&\ne\varnothing &&(0\le p<W+3).
\end{aligned}                                                     \tag{4.2}
\]

When (4.2) holds, the maximal literal word is

\[
                         A_p=\{x:p\in Q_x(\phi)\}.    \tag{4.3}
\]

These conditions follow by separating, coordinate by coordinate, all pin
negative constraints from all central and pin-positive hits. They are both
necessary and sufficient.

Let \(\mathfrak N_h^{\rm proj}(\mathcal I)\) omit item 5, and let
\(\mathfrak N_h^Q(\mathcal I)\) require it. Safe Hall-neutral braid paths are
the arrows: every intermediate deficiency is exactly \(h\), every
intermediate state retains the protected package, and the marked circuit,
basis, exposed-root label, and exterior-service data are transported
invertibly. In \(\mathfrak N_h^Q\), each state must also carry an explicit
valid maximum-matching decoration (4.1)--(4.2), with invertible identification
along the arrow. Reversal traverses the same certified states and transported
data in reverse, with the inverse cuts. Hence each is a groupoid, not a
global group action on one fixed path.

For a unit component \(D\), let
\(\operatorname{Split}^{*}_{\mathcal I}(D)\), with
\(*\in\{\mathrm{proj},Q\}\), be the set of objects from which a directed safe
macro loses no protected support and certifies the Hall gain by either:

1. the two right-disjoint matchings of Theorem 2.3; or
2. the exact all-shore condition (2.7), together with the marked local
   circuit-ear identification.

In the \(Q\)-version, the endpoint must additionally exhibit a
common-\(Q_x\)-safe **maximum** final matching. If a gap-\((h-1)\) shore is
exhibited, a combined matching from option 1 is already maximum and must
itself pass (4.1)--(4.2). If the true deficiency drops by more than one, a
separate certified common-\(Q_x\) extension to a maximum matching is required;
the size-\(\nu(G_0)+1\) combined matching alone is only a partial injection.

### Theorem 4.1 (neutral-router/remote-splitter descent)

Let \(\Omega\) be a decorated state of deficiency \(h>0\), and let \(D\) be a
marked unit DM component. If

\[
 \operatorname{Orb}_{\mathfrak N_h^{*}(\mathcal I)}(\Omega)
 \cap \operatorname{Split}^{*}_{\mathcal I}(D)\ne\varnothing,
 \qquad *\in\{\mathrm{proj},Q\},                                  \tag{4.4}
\]

then a neutral router followed by the splitter gives a legal decorated state
of deficiency at most \(h-1\). If the final graph has a gap-\((h-1)\) shore,
the final deficiency is exactly \(h-1\).

#### Proof

Choose a neutral path to an object in the intersection (4.4), then append its
directed splitter. Every router state retains \(\mathcal I\) by the definition
of the groupoid, and the port transport identifies the endpoint circuit to
which the splitter applies. The splitter gives the rank gain either by
Theorem 2.3 or directly by (2.7). Its endpoint certificate supplies the
protected conclusion and, in the \(Q\)-version, the common-\(Q_x\)
conclusion. \(\square\)

No return route is needed. In particular, one may not write
\(g^{-1}\sigma g\) without an additional proof that \(g^{-1}\) lifts to the
new deficiency level after the splitter. State-dependent legality makes
ordinary group conjugation invalid in general.

### Corollary 4.2 (dynamic induction)

Suppose that for every reachable positive-deficiency decorated state there is
**some** unit component \(D\) satisfying (4.4), and that the resulting state
again belongs to the quantified class. Then repeated router--splitter macros
reach Hall zero while retaining \(\mathcal I\).

Routing to every named remaining circuit is stronger than is needed for this
induction. One orbit hit at each dynamically reached state suffices.

## 5. Exact audit of the H23 router

The H23 canonical DM shore has sizes \(1007/984\) and decomposes into 23
unit components. The neutral router changes 18 old and 18 new full cell
signatures. Sixteen on each side do not meet the canonical DM shore. The
two old and two new DM-touching signatures all lie in the \(161/160\)
component rooted at \(K=24610\).

Put \(K_I=K\cup I\), use the zero-based coordinate masks

\[
 x=2^0,\qquad c=2^2,\qquad d=2^6,\qquad b=2^{12},     \tag{5.1}
\]

and define

\[
 Q_s=\{K_s,K_{s+x},K_{s+d},K_{s+x+d}\},
 \qquad P_b=Q_b\setminus\{K_b\}.                    \tag{5.2}
\]

Restricted to this component, the exact old bank is

\[
                         \{Q_c,\ Q_\varnothing\cup P_b\},          \tag{5.3}
\]

and the new bank is

\[
                         \{P_b,\ Q_\varnothing\cup Q_c\}.         \tag{5.4}
\]

Numerically, this is

\[
\begin{aligned}
&\{24614,24615,24678,24679\},\\
&\{24610,24611,24674,24675,28707,28770,28771\}
\end{aligned}                                                     \tag{5.5}
\]

replaced by

\[
\begin{aligned}
&\{28707,28770,28771\},\\
&\{24610,24611,24614,24615,24674,24675,24678,24679\}.
\end{aligned}                                                     \tag{5.6}
\]

The component remains rank \(160\). In the complete graph, full-signature
cancellation leaves common-core rank \(16350\) and contracted boundary ranks

\[
                              10\longrightarrow10.    \tag{5.7}
\]

The remote component \(\{4877,4909\}\) is unchanged, including its sole
right-cell signature. The router preserves lower support at every depth and
keeps upper support complete. It does not preserve all shadow
multiplicities: several lower and upper multiplicity vectors change. Thus
the exact invariant is protected support, not a multiset identity.

## 6. Exact audit of the remote splitter

Before the splitter, the \(2/1\) component has targets

\[
                         S=4877,\qquad E=4909=S\cup\{2^5\}.          \tag{6.1}
\]

Its sole restricted right shore comes from

\[
 c_0=(q=2,s=739),\quad
 (P_{739},P_{740},P_{741})=(809,301,4393),            \tag{6.2}
\]

with envelope \(4909\), mandatory mask \(4876\), and **full** shore

\[
                         \{4876,4877,4908,4909\}.     \tag{6.3}
\]

After the splitter, the two componentwise singleton shores come from

\[
\begin{array}{c|c|c|c|c}
\text{cell}&(q,s)&\text{controller states}&M_c&
 \Gamma(c)\cap\{4877,4909\}\\ \hline
7178&(1,740)&(781,4365)&4612&\{4877\}\\
13614&(2,739)&(809,781,4365)&4652&\{4909\}.
\end{array}                                                       \tag{6.4}
\]

Their full shores are, respectively,

\[
 \{4612,4613,4620,4621,4868,4869,4876,4877\},         \tag{6.5}
\]

and

\[
                         \{4652,4653,4908,4909\}.     \tag{6.6}
\]

Thus “two singleton shores” is exact only after restriction to the old
two-target component. It is not a claim about the global cell
neighbourhoods.

The controller identities are

\[
 781\cup4365=4877,\qquad
 809\cup781\cup4365=4909,\qquad 2^5\in4652.           \tag{6.7}
\]

They are precisely Theorem 3.1. Full-signature cancellation for this move
leaves common-core rank \(16343\), with 41 old and 41 new boundary
signatures and contracted ranks

\[
                              17\longrightarrow18.    \tag{6.8}
\]

Only one old and two new changed signatures touch the old canonical DM
shore, all at the component (6.1). The entire full-neighbourhood multiset
incident with the \(24610\) component is unchanged by this second move.

The canonical DM shore changes from \(1007/984\) to \(1005/983\), removing
exactly \(4877,4909\) and adding no target. The exact cross-gap matrix (rows
are the three graphs and columns their canonical shores) is

\[
 \begin{pmatrix}
 23&23&22\\
 23&23&22\\
 22&22&22
 \end{pmatrix}.                                      \tag{6.9}
\]

This supplies both sides of the exact Hall equality.

The lower support-hole vectors are

\[
\begin{aligned}
 H23,H23^{\rm port}&:(4,19,6,1,0,0,0),\\
 H22&:(4,18,6,1,0,0,0).
\end{aligned}                                                       \tag{6.10}
\]

The splitter gains the depth-two target \(4877\) and loses no lower support.
Every upper support remains complete through depth seven. Again, support
does not mean multiplicity: both moves change shadow multiplicities.

### Theorem 6.1 (critical-shore common-word certificate)

In \(H23\) and \(H23^{\rm port}\), the 984 cells of the canonical DM right
shore have pairwise distinct native traces, all in the 1007-target DM left
shore. In \(H22\), the analogous 983 native traces are distinct in its
1005-target DM left shore.

Moreover, the two cells in (6.4) are outside the final DM right shore, their
targets are outside the final DM left shore, and their native traces are
\(4877\) and \(4909\). Consequently the final maximal controller realizes,
in one literal word, 985 distinct pins on the former 1007-target H23 shore.
Its exact critical-shore defect is \(1007-985=22\).

#### Proof

The distinctness, shore membership, and exact counts are the independently
reconstructed native-transversal certificate. Lemma 1.2 turns each such
transversal into one simultaneous literal pin family. Equation (6.7) gives
the two additional native traces, and their right- and target-disjointness
permits union of the matchings. Finally, the final-row/old-H23-shore entry of
(6.9) says that this 1007-target shore has exactly 985 neighbours in H22.
Thus no larger matching on that shore exists, and its defect is exactly 22.
\(\square\)

This is a genuine common-\(Q_x\) statement on the critical shore. It is not
a common-\(Q_x\) maximum matching of size \(16361\): the exterior matching
may use nonnative edges, and its combined negative-pin unions have not been
audited.

## 7. Remaining H22 circuits and the immediate routing problem

The H22 canonical DM shore has 22 unit components:

\[
\begin{array}{c|l}
\text{size}&\text{minimum/root masks}\\ \hline
169/168&1920\\
161/160&960,8217,24610\\
160/159&449,8218\\
5/4&4213,7504\\
3/2&1103,18970\\
2/1&2420,2676,9524,17683,19568\\
1/0&2575,5801,13616,13620,17738,21641,29776.
\end{array}                                                       \tag{7.1}
\]

The five remaining \(2/1\) circuits are

\[
\begin{array}{c|c|c}
S&E&S\triangle E\\ \hline
2420&2932&\{2^9\}\\
2676&10868&\{2^{13}\}\\
9524&9588&\{2^6\}\\
17683&21779&\{2^{12}\}\\
19568&27760&\{2^{13}\}.
\end{array}                                                       \tag{7.2}
\]

At the naked controller-triple level, every row of (7.2) is coordinate-
isomorphic to (6.1) by (3.5). Therefore there is no local rank or inclusion
obstruction to another suffix splitter. The exact unresolved problem is to
route one such triple with its mandatory condition and full decorated collar
into the fixed chronology.

The seven \(1/0\) components require first-cell ears instead. In particular,
\(13616\subset13620\) is the unique comparable pair among the seven zeros; a
new cell adjacent to both could merge two isolated components into one
\(2/1\) component and reduce both the Hall and zero counts after an exterior
rematch. No legal common-\(Q_x\) macro doing this is presently proved.

## 8. Minimum remaining theorem and adversarial audit

The strongest natural conjecture is the following.

> **Universal decorated port routing.** For every reachable decorated
> deficiency-\(h\) carrier and every unit DM component \(D\), the orbit of the
> carrier in \(\mathfrak N_h^Q(\mathcal I)\) meets
> \(\operatorname{Split}^Q_{\mathcal I}(D)\).

This would route a legal basis ear to every remaining circuit while retaining
deck, residence, protected support, exterior matching service, and one common
physical word. Theorem 4.1 would then discharge any chosen component.

It is unproved and is stronger than necessary. The **minimum** inductive
hypothesis is the adaptive version:

\[
 \boxed{
 \text{Every dynamically reachable positive-deficiency \(Q\)-decorated state
 has at least one unit component whose neutral orbit meets its \(Q\)-splitter
 locus.}}
                                                                  \tag{8.1}
\]

The audit exposes five invalid shortcuts.

1. **No global braid group.** Legality is state-dependent. Endpoint pairs,
   run-boundary states, mandatory masks, full cell signatures, support
   witnesses, exterior matching occupancy, and common-\(Q_x\) obligations
   must all belong to the port label.
2. **No same-component requirement.** The H23 router acts in the \(24610\)
   component and the splitter acts remotely on \(\{4877,4909\}\).
3. **No automatic conjugation.** A route \(g\) before a splitter does not
   imply that \(g^{-1}\) is legal after it.
4. **No local-to-global Hall inference.** A split component can steal an
   exterior right cell. Theorem 2.3 or the all-shore inequality (2.7) is
   indispensable.
5. **No projected-to-literal inference.** Theorem 6.1 closes common-\(Q_x\)
   only on the critical shore. A size-\(16361\) simultaneous injection is a
   separate, still-open certificate.

The one audited chain (0.1) proves a nontrivial orbit intersection in the
**projected** groupoid and shows that neutral routing can be
chronology-essential. Theorem 6.1 supplies a literal partial submatching but
does not promote this chain to the maximum-matching literal groupoid. There
is no transitivity theorem across the 22 remaining decorated component
ports, no \(H21\) carrier, and no length-6438 contiguous-OR word.

## 9. Exact artifacts

Canonical carriers:

    scratch/k15_segment_braid_hall23.json
    8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d

    scratch/k15_segment_braid_hall23_portal.json
    9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6

    scratch/k15_segment_braid_hall22.json
    c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798

Independent structural and native-pin audits:

    scratch/audit_k15_h22_router_splitter_structure.py
    ec0d79eacafa5cf06f906af28dea4e9d4ab7413a7b7e4a1eef77a0dbacaeb6f9

    scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json
    e0d591d6c0a7b9715bf4f6fc2007402a7e53215051390e50c01b3be3142070f6

    scratch/k15_hall22_native_dm_pins_certificate.json
    3fecf4f57b6a253c00f8d97fd9bf83413ff214284c0565c9038d4ce5911823bc

    scratch/k15_hall23_native_dm_pins_certificate.json
    9bcf9b3a1736282d7891a4d6f954a184b1e2ca8f7e23e6375f33b7fbd23d014d

    scratch/k15_hall23_portal_native_dm_pins_certificate.json
    330eed077e0c1c17611395919bbb47c1d8191cf96faca4b77fea5aaa9083e298

The general chain verifier is

    scratch/audit_k15_segment_braid_descent.py
    1e2ad82979d747853fcf0b2a2c4e87aa1101a144ee2201474e7688f7cc3ebfdf
