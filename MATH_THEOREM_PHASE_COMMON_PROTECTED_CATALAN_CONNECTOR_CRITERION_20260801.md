# Phase-common protected Catalan completion: the upper-tail row closes, the head/forest correlation remains

**Date:** 2026-08-01  
**Lane:** K, complete-reversal packet / upper-decorated rooted host  
**Status:** unconditional protected upper-tail extension and exact
Catalan-connector equivalence.  A common rooted Catalan forest and connector
tree are not constructed uniformly; their remaining occurrence-labelled
feasibility system is stated exactly.

## 0. Outcome

Open one edge of the `4d+2`-root complete-reversal packet and let

\[
 P=Z_0-I_0-Z_1-I_1-\cdots-I_{M-2}-Z_{M-1},
 \qquad M=4d+2.                                           \tag{0.1}
\]

Under `m>=8d+4`, the phase-common q1 theorem supplies a spanning
two-factor containing `P`.  Properly colour the protected path as

\[
 P_0=\{I_iZ_i\},\qquad P_1=\{I_iZ_{i+1}\}.                \tag{0.2}
\]

The new conclusions are:

1. `P_1` is already a graphic-independent rooted link path carrying
   `4d+1` distinct immediate-upper colours.
2. For any perfect matching `M_0` extending `P_0`, those protected
   upper-colour/tail tickets extend unconditionally to an assignment of
   **every** immediate-upper colour to a distinct rooted tail.
3. The only missing rows for a rooted Catalan forest are simultaneous head
   injectivity and graphic acyclicity of that assignment.
4. Once such a forest exists, the exact remaining topology is a free-port
   connector tree on its `Cat_m` components.  The packet is already
   contracted inside one component, and the same contracted instance
   serves both phases.

Thus phase synchronization adds no second Catalan problem.  The remaining
central obstruction is one occurrence-labelled matching-forest selector,
not a phase intersection.

## 1. Rooted coordinates

Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname{Cat}_m.                              \tag{1.1}
\]

Fix a perfect matching `M_0` of `ML_m` containing `P_0`.  For an incidence
edge `e=LV` outside `M_0`, define

\[
 \operatorname{up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).                 \tag{1.2}
\]

For the protected edge

\[
                         e_i=I_iZ_{i+1}\in P_1,            \tag{1.3}
\]

we have

\[
 M_0(I_i)=Z_i,qquad
 \operatorname{up}(e_i)=Z_i\cup Z_{i+1}=:U_i.             \tag{1.4}
\]

The `U_i` are pairwise distinct.

### Lemma 1.1 (protected link path)

Let `J=M_0^{-1}(Z_(M-1))`.  Then

\[
 \lambda(P_1)=I_0-I_1-\cdots-I_{M-2}-J.                  \tag{1.5}
\]

In particular, `lambda(P_1)` is graphic-independent and `J` is outside
the protected lower bank.

#### Proof

For `i<M-2`, the edge `I_(i+1)Z_(i+1)` belongs to `P_0`, so
`M_0^{-1}(Z_(i+1))=I_(i+1)`.  The final preimage is `J`.  Every protected
lower vertex is already matched in `P_0`, hence `J` is new. \(\square\)

This lemma is phase-common: reversing the directed root path does not
change `P_0,P_1`, the protected upper labels, or the rooted link path.

## 2. Every upper colour gets a distinct rooted tail

For a rank-`m+1` upper colour `R`, a **rooted tail ticket** is a rank-`m`
set `T subset R`.  Given `M_0`, put

\[
                         L=M_0^{-1}(T).                     \tag{2.1}
\]

Write `T=L+a` and `R=T+b`.  The unique other middle corner is

\[
                         V=L+b,                             \tag{2.2}
\]

and `e=LV` satisfies `up(e)=R`.

The one-step central shadow theorem says that any nonempty family `X` of
rank-`m+1` colours has

\[
                         |\partial X|\ge|X|+m.              \tag{2.3}
\]

Consequently any at most `m` prescribed distinct upper/tail tickets extend
to an injection of all upper colours into distinct rooted tails.

### Theorem 2.1 (phase-common upper-tail completion)

If `m>=8d+4`, there is an injection

\[
 \psi:{[2m-1]\choose m+1}\longrightarrow{[2m-1]\choose m},
 \qquad \psi(R)\subset R,                                 \tag{2.4}
\]

which retains every protected ticket

\[
                         \psi(U_i)=Z_i,qquad0\le i<M-1.    \tag{2.5}
\]

#### Proof

There are `M-1=4d+1` protected tickets.  Their upper colours `U_i` and
tails `Z_i` are separately distinct.  Since

\[
                         4d+1\le m,                         \tag{2.6}
\]

delete those upper vertices and tails from the containment graph between
ranks `m+1` and `m`.  For any remaining upper family `X`, (2.3) gives

\[
 |N(X)\setminus\{Z_0,\ldots,Z_{M-2}\}|
 \ge |X|+m-(4d+1)\ge|X|.
\]

Hall supplies the remaining tickets.  Adjoin (2.5). \(\square\)

The theorem closes the upper-colour and rooted-tail rows exactly.  It does
not yet say that the other middle corners `V` in (2.2) are distinct.

## 3. The exact rooted-Catalan system after contracting the packet

For every admissible pair `(R,T)` with `T subset R`, define

\[
\begin{aligned}
 L(R,T)&=M_0^{-1}(T),\\
 V(R,T)&=L(R,T)+(R-T),\\
 h(R,T)&=M_0^{-1}(V(R,T)),\\
 \ell(R,T)&=L(R,T)h(R,T).
\end{aligned}                                               \tag{3.1}
\]

Let `x_(R,T)` be a zero-one variable.  The following is an exact criterion.

### Theorem 3.1 (protected rooted Catalan criterion)

A rooted Catalan forest `Q_0` containing `P_1` exists relative to `M_0` if
and only if the following zero-one system is feasible:

\[
 \sum_{T\subset R,\ |T|=m}x_{R,T}=1
 \qquad\text{for every upper colour }R,                    \tag{3.2}
\]

\[
 \sum_Rx_{R,T}\le1
 \qquad\text{for every rooted tail }T,                     \tag{3.3}
\]

\[
 \sum_{R,T:\ V(R,T)=V}x_{R,T}\le1
 \qquad\text{for every middle head }V,                    \tag{3.4}
\]

\[
 \sum_{R,T:\ L(R,T),h(R,T)\in X}x_{R,T}\le |X|-1
 \qquad\text{for every }\varnothing\ne X\subseteq{[2m-1]\choose m-1},
\tag{3.5}
\]

and

\[
                         x_{U_i,Z_i}=1
 \qquad(0\le i<M-1).                                      \tag{3.6}
\]

#### Proof

Equation (3.2) chooses one occurrence of every upper colour.  Equations
(3.3)--(3.4) say that the resulting incidences have distinct lower tails
and distinct middle heads, so they form a matching.  Equation (3.5) is the
standard vertex-subset description of independence in the graphic matroid
of the labelled links `ell(R,T)`.  Finally (3.6) retains `P_1`.  These are
exactly the definition of a protected rooted Catalan forest. \(\square\)

The packet link path (1.5) may be contracted in (3.5).  It reduces the
graphic ground by `M-1` edges and `M-1` vertices but creates no loop and no
phase-dependent structural zero.  Both phases therefore induce the same
contracted system (3.2)--(3.6).

### Why Hall/Rado alone stops here

Equations (3.2)--(3.3) form the bipartite Hall system solved by Theorem 2.1.
Head injectivity (3.4) is a second partition constraint, while (3.5) is a
graphic-matroid constraint.  On occurrence atoms, the full problem is a
common independent transversal for two capacity partitions and one graphic
matroid.  A matching edge family is not itself a matroid, so ordinary
Rado or two-matroid intersection does not give a sufficient single rank
inequality.

If the head partition is fixed in advance, the remaining graphic Rado
condition is

\[
 r_{\rm gr}\!\left(\bigcup_{R\in\mathcal X}\mathcal A_R\right)
 \ge |\mathcal X|
 \qquad\text{for every upper-colour family }\mathcal X,    \tag{3.7}
\]

where `A_R` is the allowed link set for colour `R`.  Without the head/tail
capacity correlation, (3.7) is necessary but not sufficient for
(3.2)--(3.6).  This precisely locates the remaining non-Rado obstruction.

## 4. The connector tree after a Catalan forest

Assume `Q_0` exists.  Its `U=W-C` links form a forest with exactly `C`
components, including isolated lower vertices.  Matching injectivity makes
each component a coherently directed path.  Each component has one free
outgoing tail port and one free incoming head port.

Form the directed component graph `D_(Q0)`: an arc `A->B` exists when the
free outgoing port of component `A` and free incoming port of component `B`
lift to a legal unused incidence.

### Theorem 4.1 (exact connector criterion)

There is an upper-exact spanning alternating Hamilton path containing `P`
if and only if, for some `M_0,Q_0` satisfying Theorem 3.1, the graph
`D_(Q0)` contains a directed Hamilton path.  Equivalently, there are
`C-1` connector variables `y_(A,B)` satisfying

\[
 \sum_B y_{A,B}\le1,qquad \sum_Ay_{A,B}\le1,             \tag{4.1}
\]

\[
                         \sum_{A,B}y_{A,B}=C-1,             \tag{4.2}
\]

and the graphic inequalities

\[
 \sum_{A,B\in\mathcal S}y_{A,B}\le|\mathcal S|-1
 \qquad(\varnothing\ne\mathcal S\subseteq\operatorname{Comp}(Q_0)).
\tag{4.3}
\]

#### Proof

Conditions (4.1) make the selected arcs a directed partial permutation.
Conditions (4.2)--(4.3) make the underlying graph a spanning tree.  A tree
of maximum indegree and outdegree one is one directed Hamilton path.
Expanding the contracted `Q_0` paths gives a spanning rooted link path and
hence, after restoring `M_0`, a spanning alternating Hamilton path.
The converse follows by contracting `Q_0` inside any such path. \(\square\)

For an `s`-component upper-surjective factor, replace `C-1` by `C-s` and
require a perfect residual matching on the `s` unused tails and heads.  If
`s=O(1)`, that last condition is only an `O(1)` Hall instance.

The connector problem is again an intersection of outgoing partition,
incoming partition and graphic constraints.  In a general directed
component graph it is a Hamilton-path problem; no ordinary Hall condition
is sufficient.

## 5. Phase collapse

Every object above is selected only once.

* `P_0,P_1` are identical undirected incidence sets in the two phases.
* The protected tickets `(U_i,Z_i)` are identical.
* The contracted protected link path (1.5) is identical.
* Therefore `M_0`, a feasible `Q_0`, its component graph, and a connector
  tree are common to both phases.

Changing packet phase reverses the containing directed Hamilton path (or
factor component); it does not require a second common-basis intersection.
This is the main benefit of complete reversal over the earlier unrelated
old/new packet states.

## 6. Exact implication and remaining scope

If Theorems 3.1 and 4.1 have a solution, the result is one
phase-switchable owner/lower-q1/immediate-upper-exact Hamilton path.  For an
`O(1)`-component variant, the same statement holds with an `O(1)` residual
Hall completion and at most `O(1)` upper casualties on opening.

This closes only:

* central owner occurrence;
* immediate lower q1;
* immediate-upper surjectivity;
* owner-factor topology.

It does **not** by itself close:

* arbitrary-width upper targets outside the protected packet;
* residence on the selected unprotected bulk;
* source/antecedent factorability of that bulk;
* the occurrence-labelled lower compiler/common cap;
* safe linear openings and Pascal regeneration;
* `k=17`, all-`k`, or `B+O(1)`.

The strongest unconditional new row is Theorem 2.1.  The exact remaining
central theorem is now:

\[
 \boxed{
 \text{extend the phase-common protected upper-tail transversal}
 \text{ to a head-injective graphic forest, then connect its }C
 \text{ paths through free ports}.}
\]

