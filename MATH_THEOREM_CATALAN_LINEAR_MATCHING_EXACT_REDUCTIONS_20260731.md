# Exact reductions for the Catalan Linear Matching Theorem

Date: 2026-07-31  
Status: exact equivalences, a full fractional feasibility theorem, the
balanced-factorization ledger, and a cycle-switch criterion.  Integral
existence remains open.

## 1. The object

Fix \(m\ge2\), let \(|\Omega|=2m\), and put

\[
\mathcal L=\binom\Omega{m-1},\qquad
\mathcal X=\binom\Omega m,\qquad
\mathcal U=\binom\Omega{m+1}.
\]

Write

\[
K=\operatorname {Cat}_m,\qquad
N=|\mathcal L|=|\mathcal U|=mK,\qquad
M=|\mathcal X|=(m+1)K=N+K.                 \tag{1.1}
\]

The diamond graph \(B_m\) is the balanced bipartite containment graph on
\(\mathcal L\sqcup\mathcal U\).  Its degree is

\[
d=\binom{m+1}{2}.                              \tag{1.2}
\]

An edge \(e=(L,U)\), with \(U\setminus L=\{a,b\}\), lifts to the
Johnson edge

\[
\psi(e)=\{L+a,L+b\}\subset J(2m,m).            \tag{1.3}
\]

The Catalan Linear Matching assertion is that \(B_m\) has a perfect
matching \(P\) for which \(\Psi(P)\) has maximum degree at most two and is
acyclic.  Since \(|P|=N=M-K\), such a lift is automatically a spanning
forest of exactly \(K\) paths, with isolated vertices admitted as paths.

## 2. Ordered four-transversal normal form

### Theorem 2.1

The Catalan Linear Matching assertion is equivalent to choosing, for every
\(L\in\mathcal L\), an ordered pair of distinct elements

\[
(a_L,b_L)\in(\Omega\setminus L)^2                  \tag{2.1}
\]

such that the following three maps are injective:

\[
\begin{aligned}
U_L&=L\cup\{a_L,b_L\}\in\mathcal U,\\
T_L&=L\cup\{a_L\}\in\mathcal X,\\
H_L&=L\cup\{b_L\}\in\mathcal X,                  \tag{2.2}
\end{aligned}
\]

and the directed graph

\[
T_L\longrightarrow H_L\qquad(L\in\mathcal L)      \tag{2.3}
\]

has no directed cycle.

In this form \(U\) is actually a bijection, while the tail and head maps
each omit exactly \(K\) middle sets.

#### Proof

Given the desired matching, orient each component of its lifted path forest.
For the edge whose lower colour is \(L\), name its first and second middle
endpoints \(T_L=L+a_L\) and \(H_L=L+b_L\).  Perfect matching on the upper
shore makes \(U_L\) injective; path orientation makes tails and heads
injective; acyclicity gives the last condition.

Conversely, injectivity of \(U\), together with equal shore sizes, makes
the diamonds \((L,U_L)\) a perfect matching of \(B_m\).  Tail and head
injectivity give outdegree and indegree at most one in (2.3), hence
undirected degree at most two.  In a degree-two undirected cycle every
vertex would have one incoming and one outgoing edge, producing a directed
cycle.  Thus the last condition makes the lift a linear forest. \(\square\)

This is a four-transversal problem: lower colours are indexed, while upper
colours, tails, and heads must all be distinct.  The only non-matching
condition left is directed acyclicity.

### Corollary 2.2 (two-level path decomposition)

Subdivide every arc \(T_LH_L\) by its lower colour \(L=T_L\cap H_L\).
The assertion is equivalently a spanning \(K\)-path decomposition of the
two-level incidence graph on \(\mathcal L\cup\mathcal X\), in which every
lower vertex has degree two and the unions of its two middle neighbours
enumerate \(\mathcal U\).

## 3. There is no fractional obstruction, even after adding acyclicity

Use one variable \(x_e\) for every diamond.  Consider

\[
\begin{aligned}
\sum_{e\ni L}x_e&=1 &&(L\in\mathcal L),\\
\sum_{e\ni U}x_e&=1 &&(U\in\mathcal U),\\
\sum_{e:X\in\psi(e)}x_e&\le2 &&(X\in\mathcal X),\\
\sum_{e:\psi(e)\subseteq S}x_e&\le |S|-1
    &&(\varnothing\ne S\subseteq\mathcal X),\\
x_e&\ge0.                                             \tag{3.1}
\end{aligned}
\]

The fourth line is the complete graphic-forest system for the lifted
Johnson edges.

### Theorem 3.1 (uniform fractional linear matching)

The constant point

\[
x_e={1\over d}\qquad(e\in E(B_m))                    \tag{3.2}
\]

satisfies every constraint in (3.1).  Its total middle-capacity slack is
exactly \(2K\).

#### Proof

Regularity gives both matching equalities.  A middle set \(X\) is incident
with the \(m^2\) swaps \((a,b)\in X\times(\Omega\setminus X)\), so its
load is

\[
{m^2\over d}={2m\over m+1}<2.                         \tag{3.3}
\]

Summing the difference from two over all \(M=(m+1)K\) middle sets gives
\(2K\).

It remains to check the forest inequalities.  Let \(|S|=s\).  If
\(s\le m+1\), simplicity gives

\[
|E_{J}(S)|\le\binom s2\le d(s-1).
\]

If \(s\ge m+1\), the Johnson maximum degree \(m^2\) gives

\[
|E_J(S)|\le {m^2s\over2}\le d(s-1),                  \tag{3.4}
\]

where the last inequality is exactly \(s\ge m+1\).  Dividing by \(d\)
proves the fourth line of (3.1). \(\square\)

Thus even the natural LP containing perfect matching, middle capacity, and
all graphic inequalities is feasible.  The missing theorem is purely
integral.

There is no direct total-unimodularity shortcut.  Fix a rank-\((m-1)\) set
\(L\) and three distinct extensions \(L+a,L+b,L+c\).  The three middle
capacity rows and the three corresponding diamond columns contain the
unsigned triangle-incidence minor

\[
\begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
\]

whose determinant has magnitude two.

## 4. The balanced one-factorization route

Every proper \(d\)-edge-colouring of the \(d\)-regular bipartite graph
\(B_m\) is a one-factorization

\[
E(B_m)=P_1\sqcup\cdots\sqcup P_d.                      \tag{4.1}
\]

For a middle set \(X\), its incident diamonds form an \(m\)-by-\(m\)
grid: rows fix the deleted element of \(X\), and columns fix the inserted
element.  Properness in \(B_m\) implies that the edges of any one colour
form a matching inside this grid.

Put

\[
g_j(X)=|\{e\in P_j:X\in\psi(e)\}|.                    \tag{4.2}
\]

A **two-balanced one-factorization** is one satisfying

\[
g_j(X)\le2qquad(j\in[d],\ X\in\mathcal X).            \tag{4.3}
\]

### Proposition 4.1 (exact local and global ledgers)

If (4.3) holds, and \(n_i(X)=|\{j:g_j(X)=i\}|\), then

\[
2n_0(X)+n_1(X)=m.                                     \tag{4.4}
\]

For a fixed colour \(j\), let \(z_j,o_j\) be the number of degree-zero
and degree-one vertices in \(\Psi(P_j)\).  Then

\[
2z_j+o_j=2K.                                          \tag{4.5}
\]

Moreover, the number of isolated and nontrivial path components of
\(\Psi(P_j)\), excluding its cycle components, is exactly \(K\).

#### Proof

At \(X\), summing over colours gives \(m^2\), while
\(2d=m(m+1)\), proving (4.4).  A factor has \(N=M-K\) lifted edges, so its
degree sum is \(2N\).  Subtracting from the all-two degree sequence proves
(4.5).  Every nontrivial path has two degree-one endpoints, while an
isolated vertex contributes two deficit units; hence
\(z_j+o_j/2=K\). \(\square\)

Consequently a two-balanced one-factorization proves the cap-two half for
all \(d\) factors simultaneously.  The Catalan Linear Matching Theorem then
reduces to finding an acyclic colour, or to eliminating the cycles in one
colour without losing (4.3).  This factorization is stronger than the
original assertion and is not proved here.

## 5. An exact colour-preserving cycle switch

Let \(P\) be a perfect matching whose lift has maximum degree at most two,
and let

\[
C=X_0X_1\cdots X_{\ell-1}X_0
\]

be a cycle component.  Its edges correspond to matched diamonds

\[
L_i=X_i\cap X_{i+1},\qquad U_i=X_i\cup X_{i+1}
\quad(i\bmod\ell).                                    \tag{5.1}
\]

### Lemma 5.1 (forward cycle shift)

Replacing

\[
(L_i,U_i)\quad\hbox{by}\quad(L_i,U_{i+1})              \tag{5.2}
\]

for all \(i\) produces another perfect matching \(P^+\) of \(B_m\).  Its
new Johnson edge has endpoints

\[
X_{i+1},\qquad
Y_i=L_i\cup(U_{i+1}\setminus X_{i+1}).                 \tag{5.3}
\]

The analogous backward shift \((L_i,U_{i-1})\) is also valid.

#### Proof

We have \(L_i\subset X_{i+1}\subset U_{i+1}\), so every replacement is a
diamond.  The replacements use every old lower colour and every old upper
colour exactly once, only cyclically changing their partners.  They
therefore preserve perfect matching.  Formula (5.3) lists the two
intermediate rank-\(m\) sets of that diamond. \(\square\)

There is an exact safety test.  Delete the old cycle edges and call the
remaining graph \(F_0\).  Add the edges (5.3), and contract every connected
component of \(F_0\).  The shift preserves maximum degree two and creates
no new cycle iff

1. every physical vertex has its \(F_0\)-degree plus its multiplicity among
   the endpoints in (5.3) at most two; and
2. the resulting component multigraph has no loop and is acyclic (parallel
   edges count as a two-cycle).

Thus the two colour palettes do not freeze a cycle: each cycle has two
canonical colour-preserving candidate opening moves.  Either candidate can
still fail through collision with saturated vertices or through a cycle in
the contracted attachment graph.  If the chosen cycle was the only old
cycle, the two safety conditions are equivalent to the new lift being a
linear forest; otherwise they mean exactly that no additional cycle is
created, while the untouched old cycles remain.

## 6. The reduced theorem

Any one of the following would finish the Catalan Linear Matching gate.

1. Prove the ordered four-transversal system (2.1)--(2.3).
2. Construct a two-balanced one-factorization and prove that one factor is
   acyclic.
3. Construct a two-balanced one-factorization and prove that repeated safe
   shifts from Lemma 5.1 eliminate all cycles.

The uniform point proves that matching, cap-two, and graphic constraints
have simultaneous fractional slack.  The triangle minor proves that this
does not round by raw total unimodularity.  Hence the exact missing input is
an integral correlation theorem, not another Hall or capacity estimate.
