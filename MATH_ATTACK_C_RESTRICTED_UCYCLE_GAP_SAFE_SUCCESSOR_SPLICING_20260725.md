# Restricted central Ucycle route: exact gap-safe successor splicing

Date: 2026-07-25

Scope: pure mathematics.  No computation or search is used.

## 0. Outcome and boundary

Assume \(m\ge2\), and put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m.
\]

Start with an oriented exact odd-graph wreath factor.  Its rows give (B)
directed circuits in the injective ordered-((m-1))-tuple de Bruijn graph,
and its (W) selected arcs are in bijection with the middle layer.

This note proves the following exact facts.

1. Ignoring recurrence constraints, successor switches can reduce the
   (B) row circuits to exactly the number of weak components of the
   selected de Bruijn subgraph.  Thus `few components' is an incidence
   theorem about **ordered** states, not a formal consequence of exact
   middle ownership.
2. If two current circuits are cut at a common ordered state, there is an
   exact coordinate-by-coordinate formula for every new recurrence gap.
   For two untouched wreath rows it reduces to

   \[
    \rho(R\# S)=n-\max_{x\in[n]}|p_R(x)-p_S(x)|.             \tag{0.1}
   \]

   Hence a splice preserves minimum gap (m+H) exactly when

   \[
    |p_R(x)-p_S(x)|\le m+1-H\quad(x\in[n]).                 \tag{0.2}
   \]
3. The general formula yields a rigorous iterative sufficient theorem:
   matching rounds of dynamically collar-compatible circuit pairs preserve
   gap (m+H), and the final number of circuits is exactly the initial
   number minus the number of merges.
4. A final system of (C) circuits has a literal singleton realization of
   length

   \[
                 W+C(m+H-1).                               \tag{0.3}
   \]

   The lower windows are unchanged by all successor switches.  At upper
   depth (q), one switch changes at most (2q) flags.
5. Correct recurrence gaps imply that the new upper flags have the correct
   rank.  They do **not** imply that those flags cover the rank.  The exact
   support-loss ledger is given below.  At \(H=A\sqrt m\), a schedule with
   \(B-o(B)\) switches has a generic all-depth exposure count of order
   \(H^2B=\Theta_A(W)\), not \(o(W)\), so coverage cannot be inferred from
   injectivity.  Nevertheless, all flags crossing one altered successor
   share an \((m+1)\)-core and admit a literal repair word of length
   \(2H-1\).  Thus all \(B-o(B)\) switches cost only
   \(O(HB)=o(W)\) to repair.

The resulting conditional theorem is useful and coefficient-sharp.  If
the selected ordered-state graph has \(o(B)\) weak components and the
initial exact factor has \(o(W)\) total lower shallow-shadow holes, then
arbitrary legal component-merging successor switches, with every physical
seam charged, give a central-band word of length \(W+o(W)\).  A wholly
singleton final spine still requires the stricter gap-safe packet theorem.

This is a theorem about a restricted sufficient architecture.  It does not
assert that singleton ordered-partition states are without loss of
generality for arbitrary contiguous-OR words.

## 1. The selected injective de Bruijn graph

Let \(\mathcal D_{n,m}\) be the directed graph whose vertices are injective
words of length (m-1) on ([n]).  An injective word

\[
                  a_1a_2\cdots a_m
\]

is an arc from (a_1\cdots a_{m-1}) to
(a_2\cdots a_m).

An oriented wreath row is a cyclic permutation

\[
                  R=(r_i)_{i\in\mathbb Z_n}.
\]

It gives the directed (n)-circuit

\[
 e_i^R=(r_i,r_{i+1},\ldots,r_{i+m-1}),\qquad
 v_i^R=(r_i,r_{i+1},\ldots,r_{i+m-2}).             \tag{1.1}
\]

For an exact wreath factor \(\mathcal F\), the underlying sets of the arcs
in all rows are every member of \(\binom{[n]}m\) exactly once.  Let
(D_{\mathcal F}) be the directed subgraph consisting of these (W) arcs.
It is balanced, because it is initially decomposed into the (B) row
circuits.

At an ordered state (v), suppose the current transition system pairs
incoming arcs (a,c) with outgoing arcs (b,d), respectively.  The
**successor switch** replaces

\[
                    a\mapsto b,\quad c\mapsto d
\]

by

\[
                    a\mapsto d,\quad c\mapsto b.           \tag{1.2}
\]

If (a,b) lie on one current circuit and (c,d) on another, (1.2)
merges those two circuits.  It neither inserts nor deletes an arc.

### Theorem 1.1 (exact unrestricted component number)

Let (c(D_{\mathcal F})) be the number of weak components of the selected
de Bruijn subgraph after isolated vertices are discarded.  Among all
transition systems obtained from the row system by successor switches, the
minimum possible number of Eulerian circuits is exactly

\[
                         c(D_{\mathcal F}).                 \tag{1.3}
\]

#### Proof

A successor switch never moves an arc between weak graph components, so
every transition system has at least one circuit in each weak component.

Conversely, fix one weak component.  Its initial row circuits have a
connected intersection graph: two circuits are adjacent when they meet at
an ordered state.  Choose a spanning tree of this intersection graph.
Process its edges in an order which always joins two different current
parts.  At their common state, choose one transition belonging to each
current circuit and apply (1.2).  The standard two-cycle tracing shows that
the switch merges the two circuits into one.  After one switch for every
tree edge, the whole weak component is one Eulerian circuit.  Treat the
weak components independently.  This proves (1.3).  ∎

Thus unrestricted reduction to (o(B)) circuits is equivalent to

\[
                        c(D_{\mathcal F})=o(B).              \tag{1.4}
\]

Exact middle ownership alone does not state (1.4), because equality of
underlying ((m-1))-sets is weaker than equality of their orderings.

### Proposition 1.2 (ordered-state collision obstruction)

Let (d(v)) be the number of initial row circuits which visit the ordered
state (v), and put

\[
                  E_{\rm ord}:=\sum_v(d(v)-1)_+.
\]

Then

\[
 B-c(D_{\mathcal F})\le E_{\rm ord},                       \tag{1.5}
\]

and, for every (v),

\[
                         d(v)\le\left\lfloor\frac{m+2}{2}\right\rfloor.
                                                                    \tag{1.6}
\]

In particular, (o(B)) final circuits require

\[
                         E_{\rm ord}\ge(1-o(1))B.           \tag{1.7}
\]

If \(\mu(S)\) is the ordinary depth-one wreath multiplicity of an
\((m-1)\)-set \(S\), and \(M_1=\#\{S:\mu(S)=0\}\), then also

\[
 E_{\rm ord}
 \le\sum_S(\mu(S)-1)_+
 =W-\binom n{m-1}+M_1
 =\frac{2W}{m+2}+M_1.                                    \tag{1.8}
\]

#### Proof

Begin with the (B) row vertices as isolated objects.  For each ordered
state (v), joining all (d(v)) rows that visit (v) can lower the number
of connected components by at most (d(v)-1).  Summing gives (1.5).

For (1.6), let \(S\) be the underlying \((m-1)\)-set of \(v\).  At each row
visit to (v), the incoming and outgoing middle arcs have underlying sets

\[
                         S\cup\{a\},\qquad S\cup\{b\},
\]

with (a\ne b).  Across different visits all these middle sets are
different, by exact middle ownership.  Hence the (2d(v)) extension
coordinates are distinct members of the ((m+2))-set ([n]\setminus S).
This proves (1.6).  Equation (1.7) follows from (1.5).

For (1.8), split the \(\mu(S)\) occurrences according to their ordered
state \(v\).  Replacing equality of the underlying set by equality of the
whole ordering can only reduce collision excess, so

\[
 \sum_{\operatorname{supp}(v)=S}(d(v)-1)_+
 \le(\mu(S)-1)_+.
\]

Summing proves the first inequality.  The remaining equalities are the
exact slot ledger

\[
 W=\left(\binom n{m-1}-M_1\right)+\sum_S(\mu(S)-1)_+,
\qquad
 W-\binom n{m-1}=\frac{2W}{m+2}.
\]

Thus even a perfect first shadow supplies only an ambient collision budget
\(2W/(m+2)=(4+o(1))B\); reaching \(o(B)\) ordered components requires at
least a \((1/4-o(1))\)-fraction of that unavoidable **underlying** excess
to agree in full order.  Perfect set-valued first-shadow coverage does not
by itself provide this alignment.  ∎

The proposition is an obstruction, not a construction of a collision-free
exact factor.  It identifies the precise ordered incidence which must be
proved for any proposed factor.

## 2. Exact two-circuit recurrence formula

For a cyclic coordinate word, measure a recurrence gap by the positive
cyclic difference between consecutive occurrences of the same coordinate.
The following elementary equivalence fixes the endpoint convention:

\[
\min_x\rho(x)\ge g
\quad\Longleftrightarrow\quad
\text{every coordinate window of length at most \(g\) is injective}.       \tag{2.0}
\]

Indeed, two equal letters in a length-\(g\) window have distance at most
\(g-1\); conversely, a recurrence gap \(d<g\) puts its two endpoints in a
window of length \(d+1\le g\).  In particular, equality \(\rho(x)=g\) is
safe.

Let (C) be a current directed circuit of length (L_C), and choose one
visit to an ordered state (v).  Start at (v), traverse all arcs of (C),
and record the coordinate appended by each arc.  This gives a linear word

\[
                  \omega_C=(c_0,c_1,\ldots,c_{L_C-1}).      \tag{2.1}
\]

The final (m-1) letters of (2.1) are exactly (v).  Every coordinate is
present, because every current component contains at least one original
wreath row.

For (x\in[n]), define

\[
 f_C(x)=\min\{i:c_i=x\},\qquad
 \ell_C(x)=\max\{i:c_i=x\},                                \tag{2.2}
\]

and let (\rho_C^{\rm int}(x)) be the minimum difference between two
consecutive occurrences of (x) inside the linear word (2.1), with value
(+\infty) if (x) occurs only once.

Suppose a second circuit (D) is cut at the same ordered state (v), and
apply the successor switch there.  Up to cyclic rotation, the merged
coordinate period is

\[
                           \omega_C\omega_D.                \tag{2.3}
\]

### Theorem 2.1 (exact splice gap formula)

For every coordinate (x), its minimum cyclic recurrence gap in the
merged circuit is

\[
\boxed{
 \rho_{C\#D}(x)=\min\left\{
 \begin{array}{l}
 \rho_C^{\rm int}(x),\ \rho_D^{\rm int}(x),\\[2mm]
 L_C-\ell_C(x)+f_D(x),\\
 L_D-\ell_D(x)+f_C(x)
 \end{array}\right\}.}                                    \tag{2.4}
\]

Consequently, if both current circuits already have recurrence gap at
least (g), the splice preserves that bound if and only if

\[
 \begin{aligned}
 L_C-\ell_C(x)+f_D(x)&\ge g,\\
 L_D-\ell_D(x)+f_C(x)&\ge g
 \end{aligned}
 \qquad(x\in[n]).                                          \tag{2.5}

#### Proof

Inside each linear block, the order and distances between successive
occurrences are unchanged.  The old wrap pair in each circuit is deleted.
The only new consecutive occurrence pairs are the last occurrence in
(C) followed by the first in (D), and the last in (D) followed
cyclically by the first in (C).  Their distances are the last two terms
of (2.4).  This list is exhaustive, proving both assertions.  ∎

### Corollary 2.2 (two untouched wreath rows)

Let (R,S) be two original rows meeting at (v).  In their cut words each
coordinate occurs once.  Write (p_R(x),p_S(x)\in\{0,\ldots,n-1\}) for
its positions.  Then the two new gaps of (x) are

\[
                n+p_S(x)-p_R(x),\qquad
                n+p_R(x)-p_S(x),                           \tag{2.6}
\]

and hence

\[
                \rho(R\#S)=n-\max_x|p_R(x)-p_S(x)|.        \tag{2.7}
\]

For (g=m+H), (2.7) is at least (g) exactly when (0.2) holds.

#### Proof

Substitute (L_R=L_S=n) and
(f_R=\ell_R=p_R, f_S=\ell_S=p_S) in (2.4).  ∎

The common state itself causes no hidden loss: its (m-1) coordinates are
the final (m-1) letters of both cut words, so their phase differences in
(2.7) are zero.

### Corollary 2.3 (triangular actual-collar test)

Assume \(H\le(m+2)/2\).  At the chosen visit to
\(v=v_1\cdots v_{m-1}\), let

\[
 p_i^C=\text{the \(i\)-th coordinate immediately before \(v_1\) on \(C\)},
 \qquad
 q_j^C=\text{the \(j\)-th coordinate immediately after \(v_{m-1}\) on \(C\)}
                                                                    \tag{2.8}
\]

for \(C\in\{R,S\}\) and \(1\le i,j\le H\).  Suppose the two old circuits
already have recurrence gap at least \(m+H\).  Their switch at \(v\)
preserves this gap if and only if

\[
\boxed{
\begin{aligned}
 p_i^R&\ne q_j^S,\\
 p_i^S&\ne q_j^R
\end{aligned}
\qquad\text{whenever }i,j\ge1,\ i+j\le H+1.}               \tag{2.9}
\]

#### Proof

All old recurrence pairs remain safe.  A new cross-seam repetition can
only pair a left-collar coordinate with a right-collar coordinate.  The
distance from \(p_i^R\) through the common state to \(q_j^S\) is exactly

\[
                         m-2+i+j.                          \tag{2.10}
\]

It is forbidden precisely when this is less than \(m+H\), equivalently
\(i+j\le H+1\).  The reverse seam gives the second line of (2.9).
Pairs outside the displayed triangle have distance at least \(m+H\).
This proves necessity and sufficiency.  ∎

For \(H=1\), every legal shared-state merge is automatically safe:
(2.9) asks only that the incoming extension at one visit differ from the
outgoing extension at the other, in both directions, and these four
extensions are distinct by exact middle ownership.  This automatic safety
does not extend to mesoscopic \(H\); the whole triangular collar then
matters.

## 3. A rigorous iterative packet theorem

Fix

\[
                         g=m+H\le n.                        \tag{3.1}
\]

Call two pointed current circuits **(g)-compatible** if they meet at the
pointed ordered state and satisfy (2.5).

### Theorem 3.1 (matching-round gap-safe fusion)

Start with the (B) original row circuits.  At stage (j), choose a
matching \(\mathcal M_j\) of the current circuit set such that every matched
pair has chosen (g)-compatible visits to one common ordered state.  Apply
the corresponding successor switches simultaneously.  Then:

1. every circuit after every stage has coordinate recurrence gap at least
   (g);
2. the number of final circuits is exactly

   \[
                 C=B-\sum_j|\mathcal M_j|;                  \tag{3.2}
   \]
3. the selected arc set, and hence exact middle ownership, is unchanged.

In particular, if the rounds satisfy

\[
                  \sum_j|\mathcal M_j|=B-o(B),              \tag{3.3}
\]

they give (o(B)) (g)-safe Eulerian components.

#### Proof

An original row is a permutation of ([n]), so its recurrence gap is (n),
which is at least (g).  Within one matching, no current circuit is touched
twice.  Theorem 2.1 therefore applies independently to every matched pair
and proves the inductive gap assertion.  Every switch merges two different
current circuits, so it lowers the circuit count by exactly one.  This
proves (3.2).  A successor switch changes only the transition pairing and
not the arcs, proving the last assertion.  ∎

The theorem is deliberately dynamic.  Connectivity of the static graph of
two-row-compatible ports is not enough: after a merge, the relevant first
and last occurrences in (2.5) belong to the whole new component.

There is also a sharp limitation on a one-round local-separation argument.
If selected switch ports on an original length-(n) row are required to
have cyclic distance at least (g>n/2) in both directions, that row can
carry at most one port.  Thus one such round is only a matching and leaves
at least (B/2) components.  Iteration on the longer merged components, or
a genuinely joint multi-seam certificate, is necessary for (o(B)).

### Theorem 3.2 (exact simultaneous forest packet criterion)

There is a second, genuinely simultaneous sufficient theorem.  Let
\(\mathcal C\) be any current circuit decomposition.  Choose a family
\(\mathcal P\) of successor switches with the following properties.

1. Every switch joins two members of \(\mathcal C\) at a common ordered
   state.
2. No pointed incoming--outgoing transition of a member of \(\mathcal C\)
   is used by two switches.
3. The interaction multigraph \(G_{\mathcal P}\), whose vertices are the
   circuits and whose edges are the chosen switches, is a forest.

Then simultaneous reassignment at all ports in \(\mathcal P\) produces
exactly one Eulerian circuit for every nontrivial tree of
\(G_{\mathcal P}\), and leaves every isolated circuit alone.  Hence the
new circuit count is

\[
                         |\mathcal C|-|\mathcal P|.         \tag{3.4}
\]

Cut every input circuit at all of its selected ports.  This gives directed
segments \(Q\).  The successor reassignment determines an unambiguous
cyclic ordering

\[
                         Q_1,Q_2,\ldots,Q_t                \tag{3.5}
\]

of the segments in each output circuit.  For a segment \(Q\) of length
\(L_Q\) and a coordinate \(x\) which occurs in it, let

\[
 f_Q(x)=\hbox{first position of \(x\)},\qquad
 \ell_Q(x)=\hbox{last position of \(x\)},                  \tag{3.6}
\]

and let \(\rho_Q^{\rm int}(x)\) be its least internal recurrence gap.
Call

\[
 \mathfrak b_Q(x)=
 \bigl(L_Q,f_Q(x),\ell_Q(x),\rho_Q^{\rm int}(x)\bigr)       \tag{3.7}
\]

the cut boundary profile.

For a fixed \(x\), retain from (3.5) only the segments containing \(x\).
If \(Q_i\) and \(Q_j\) are consecutive retained segments in the cyclic
order, their cross-segment recurrence gap is

\[
 d_x(Q_i,Q_j)=
 L_{Q_i}-\ell_{Q_i}(x)
 +\sum_{i<k<j}^{\rm cyclic}L_{Q_k}
 +f_{Q_j}(x).                                             \tag{3.8}
\]

The simultaneous packet has minimum coordinate recurrence gap at least
\(g\) if and only if

\[
 \rho_Q^{\rm int}(x)\ge g
 \quad\hbox{and}\quad
 d_x(Q_i,Q_j)\ge g                                       \tag{3.9}
\]

for every applicable \(Q,x,i,j\).

#### Proof

Order the forest edges arbitrarily.  Before an edge is processed, its two
endpoint circuits lie in different components of the already processed
subforest; otherwise that edge would close a forest cycle.  Port
disjointness says that its two designated transition pairs have not been
altered earlier.  Its successor transposition therefore merges two
different current Eulerian circuits.  Induction proves (3.4), and also
shows that the simultaneous and sequential final reassignments coincide.

After all cuts, every output occurrence of \(x\) is either followed by
another occurrence inside the same segment or by the first occurrence in
the next segment of (3.5) which contains \(x\).  The former gaps are
exactly those measured by \(\rho_Q^{\rm int}(x)\); direct position counting
gives (3.8) for the latter.  These are all consecutive occurrence pairs,
so (3.9) is necessary and sufficient.  ∎

The cyclic order (3.5), not just the abstract forest, is part of the gap
certificate.  Theorem 3.2 certifies the **final** transition reassignment.
Its individual successor transpositions are always legal de Bruijn
switches, but an arbitrary intermediate order need not have gap \(g\).
If every intermediate transition system must also be \(g\)-safe, use the
dynamic collar inequalities (2.5) and the matching-round theorem 3.1.
Thus the final-safe packet statement and the stepwise-safe statement are
distinct and have both been quantified exactly.

## 4. Exact literal word length

Let a final Eulerian component have (L) arcs and coordinate period

\[
                         x_0x_1\cdots x_{L-1}.
\]

Write one period and then repeat its first (g-1) letters.  Every cyclic
coordinate window of length at most (g) is now a literal interval in the
resulting linear singleton word, whose length is (L+g-1).

Summing over all (C) components proves:

### Proposition 4.1 (component overhead)

The final transition system has a literal singleton realization of length

\[
                         W+C(g-1).                          \tag{4.1}
\]

Every selected middle arc appears, so every middle (m)-set appears
exactly once as an (m)-window.  If (C=o(B)) and (H=O(\sqrt m)), then

\[
 C(g-1)=o(Bm)=o(W).                                        \tag{4.2}
\]

Concatenating the component words may create extra crossing intervals;
they are harmless.  Formula (4.1) uses only the within-component windows
whose existence has just been proved.

## 5. What switches preserve below the middle

For (0\le q<m), the length-((m-q)) word beginning at an arc is the
prefix of that selected ordered (m)-arc.  Since successor switches do not
change arcs, they do not change any such word.

### Proposition 5.1 (exact lower-shadow invariance)

At every lower depth (q), the multiset of ordered length-((m-q))
windows, and therefore the multiset and support of their underlying sets,
is exactly invariant under arbitrary successor switches.                \(
\square\)

Thus this route cannot repair lower-shadow holes of the initial exact
wreath factor, but it also cannot create new ones.

There is an exact initial upper--lower duality which removes a separate
upper-shadow hypothesis.  Write

\[
 \delta_q^-=
 \left|\binom{[n]}{m-q}\setminus\mathcal L_q(\mathcal F)\right|
 \quad(0\le q\le H),
\]

where \(\delta_0^-=0\) by exact middle ownership, and write
\(\delta_q^+(T_0)=\Delta_q(T_0)\).

### Proposition 5.2 (exact initial complement identity)

For every \(1\le q\le H\),

\[
\boxed{\delta_q^+(T_0)=\delta_{q-1}^-.}                    \tag{5.1}
\]

Consequently,

\[
\boxed{
\Delta_H^-+\Delta_H^+(T_0)
=2\sum_{q=1}^{H-1}\delta_q^-+\delta_H^-
\le2\Delta_H^-.}                                          \tag{5.2}
\]

#### Proof

Inside one wreath permutation, the complement of a cyclic interval of
length \(m+q\) is the opposite cyclic interval of length

\[
 n-(m+q)=m+1-q=m-(q-1).                                   \tag{5.3}
\]

Taking the opposite interval is a bijection on the \(n\) cyclic starts,
and set complementation is a bijection between the two ambient ranks.
After taking the union over all wreath rows, an upper target is covered
exactly when its complement belongs to the initial lower support at depth
\(q-1\).  Missing targets therefore correspond bijectively, proving
(5.1).  Summing (5.1) for \(1\le q\le H\), using
\(\delta_0^-=0\), and adding
\(\Delta_H^-=\sum_{q=1}^H\delta_q^-\) gives (5.2).  ∎

## 6. Upper flags: rank is not coverage

For a transition system (T), an arc (e), and (1\le q\le H), let
(U_q^T(e)) be the underlying union of the length-((m+q)) coordinate word
which starts with (e).  It is obtained from the ordered (m)-arc by
following (q) successor transitions.

If the recurrence gap is at least (m+H), every (U_q^T(e)) has size
(m+q).  This is only a rank assertion.

### Lemma 6.1 (exact changed-start bound)

One successor switch changes (U_q^T(e)) for at most (2q) starting arcs
(e).

#### Proof

The switch changes the successor of exactly two incoming arcs.  A
length-((m+q)) flag depends on the next (q) successor applications.  For
one altered incoming arc, only that arc and its (q-1) predecessors in the
old transition circuit can be affected.  There are at most (q) such
starts.  The two altered arcs therefore affect at most (2q) starts.  ∎

Let

\[
 \Delta_q(T)=\left|\binom{[n]}{m+q}
     \setminus\{U_q^T(e):e\in E(D_{\mathcal F}),\ |U_q^T(e)|=m+q\}
              \right|                                    \tag{6.1}
\]

be the upper support defect.

Call a switch **(q)-cover-safe** if every rank-((m+q)) target present
before the switch is still present after it.  It is **(H)-cover-safe** if
this holds for every (q\le H).

### Proposition 6.2 (support-loss ledger)

For a sequence of (J) switches,

\[
                 \Delta_q(T_{\rm fin})
                 \le\Delta_q(T_0)+2qJ.                    \tag{6.2}
\]

If all but (S) switches are (H)-cover-safe, then the sharper simultaneous
bound is

\[
 \sum_{q=1}^H\Delta_q(T_{\rm fin})
 \le
 \sum_{q=1}^H\Delta_q(T_0)+S H(H+1).                       \tag{6.3}
\]

#### Proof

At depth (q), a switch can delete from the support no more targets than
the number of changed old starts, at most (2q) by Lemma 6.1.  This proves
(6.2) by iteration.  A cover-safe switch deletes no target.  Summing the
same bound over the (S) exceptional switches and using
(2\sum_{q=1}^Hq=H(H+1)) proves (6.3).  ∎

A useful static sufficient condition is also exact.  Let
\(A_q\) be the set of initial starting arcs whose depth-\(q\) continuation
is ever changed.  If every initially covered target (Y) has an occurrence
outside (A_q), then no initial depth-(q) target is lost.  This is a
predecessor-conditional coverage condition, not a consequence of the
cardinality of the new flags.

For a near-spanning fusion (J=B-o(B)), the generic sum of the right sides
of (6.2) over all (q\le H) is

\[
             JH(H+1)=\Theta_A(Bm)=\Theta_A(W)              \tag{6.4}
\]

when (H=A\sqrt m+O(1)).  Therefore injectivity, correct rank, and
(o(B)) components do not by themselves give coefficient-one shallow
coverage.

The preceding bound counts missing targets one at a time.  Literal OR
repair has a much sharper common-core compression.

### Lemma 6.3 (one-transition shallow fan compression)

Fix one successor transition in a current coordinate circuit.  Index the
local cyclic word so that its incoming \(m\)-arc is

\[
                       x_0x_1\cdots x_{m-1}
\]

and its old successor appends \(x_m\).  Put

\[
                         K=\{x_0,x_1,\ldots,x_m\}.          \tag{6.5}
\]

The set-valued word

\[
\boxed{
 \mathcal R_H=
 \bigl(
 \{x_{-H+1}\},\ldots,\{x_{-1}\},
 K,
 \{x_{m+1}\},\ldots,\{x_{m+H-1}\}
 \bigr)}                                                  \tag{6.6}
\]

has length \(2H-1\) and contains, as literal contiguous ORs, every old
upper flag through depth \(H\) whose continuation uses this successor
transition.

#### Proof

At depth \(q\), the affected starts are indexed by
\(t=0,1,\ldots,q-1\), where \(t\) is the number of start shifts before
the incoming arc.  The corresponding old flag is exactly

\[
 Y_{q,t}=\{x_{-t},x_{-t+1},\ldots,x_{m+q-t-1}\}.           \tag{6.7}
\]

In (6.6), take the interval consisting of the last \(t\) left singleton
letters, the core \(K\), and the first \(q-1-t\) right singleton letters.
Its OR is (6.7).  This works for every \(q\le H\) and every \(t<q\).
No disjointness assumption is needed: both sides are unions of exactly the
same indexed coordinates, even if the local circuit has repetitions.  ∎

### Theorem 6.4 (all switch losses repair in \(O(H)\) per switch)

Consider any sequential schedule of \(J\) successor switches.  At each
switch, form the gadget (6.6) for each of its two old successor
transitions, using the transition system immediately before that switch.
Then the final component words together with these \(2J\) gadgets cover
every upper target through depth \(H\) which was covered by the initial
row circuits.  Their total repair length is exactly at most

\[
                         2J(2H-1).                         \tag{6.8}
\]

#### Proof

At one step, every old flag which changes uses one of the two altered
successor transitions, by the proof of Lemma 6.1.  Lemma 6.3 places all
such old flags in the two repair gadgets.  Every unchanged old flag remains
in the new transition system.  Therefore the union of the new support and
the accumulated gadget support contains the old support after every step.
Induction over the \(J\) switches proves the coverage assertion.  The
length is \(2J\) times \(2H-1\).  ∎

Thus the \(\Theta(W)\) exposure count in (6.4) is a real warning against
the false implication “rank-correct implies covered”, but it is **not** a
word-length obstruction.  The triangular family has a common core and
costs only \(O(H)\), rather than \(O(H^2)\), to restore.

## 7. Charged recurrence seams

It is sometimes unnecessary to demand a globally (g)-safe schedule.
Mark selected successor transitions as **charged**.  Assume the final
coordinate circuits satisfy the local certificate

> every coordinate segment of length (g) which crosses no charged
> transition has pairwise distinct letters.                              \(\tag{7.1}\)

If there are (M) charged transitions, then at upper depth (q) at most
(qM) starting flags can have the wrong rank: every wrong-rank flag contains
a repeated coordinate, hence crosses a charge by (7.1), and one transition
lies among the (q) continuation steps of exactly (q) starts, counted
with multiplicity.  In particular, charging both redirected transitions of
(S) exceptional switches gives at most (2qS) rank-defective flags.

This is an exact localization theorem.  It does not say that the remaining
rank-correct flags cover their rank; that issue is still governed by
Proposition 6.2.

For a merge-only schedule starting from the wreath rows, one may mark every
final successor transition at which the final pairing differs from the
initial row pairing.  There are at most \(2J\) such transitions after
\(J\) switches.  A segment which avoids all marks follows one untouched
row, and hence is injective through every length \(g<n\).  Thus (7.1)
holds automatically with all physical splice seams charged.  Theorem 6.4
then restores their complete old shallow support at the smaller cost
\(2J(2H-1)\).

## 8. Conditional coefficient-sharp band theorem

For the initial factor, let

\[
 \Delta_H^-=
 \sum_{q=1}^H\left|\binom{[n]}{m-q}\setminus\mathcal L_q(\mathcal F)\right|,
 \qquad
 \Delta_H^+(T_0)=\sum_{q=1}^H\Delta_q(T_0),                \tag{8.1}
\]

where \(\mathcal L_q(\mathcal F)\) is the invariant lower support from
Proposition 5.1.

### Theorem 8.1 (gap-and-cover-safe splice criterion)

Let (H=\lceil A\sqrt m\rceil\), with fixed (A>0).  Suppose a successor
switch schedule on one exact oriented wreath factor has the following
properties.

1. Its final transition system has (C=o(B)) Eulerian components.
2. All but (S=o(B)) switches are locally (g=m+H) recurrence-safe and
   (H)-cover-safe; after marking the two transitions of every exceptional
   switch, certificate (7.1) holds.
3. The initial shallow deficits satisfy

   \[
                    \Delta_H^-+\Delta_H^+(T_0)=o(W).        \tag{8.2}
   \]

Then there is a literal set-valued contiguous-OR word covering every set in
the ranks

\[
                  m-H,m-H+1,\ldots,m+H
\]

whose length is at most

\[
 W+C(m+H-1)+\Delta_H^-+\Delta_H^+(T_0)+S H(H+1).           \tag{8.3}
\]

In particular, (8.3) is (W+o(W)).

#### Proof

Use Proposition 4.1 for the main singleton word.  It covers the middle
rank exactly.  Proposition 5.1 identifies its lower holes with the initial
ones.  Proposition 6.2 bounds its final upper holes by

\[
                  \Delta_H^+(T_0)+SH(H+1).
\]

Append every missing target set as one literal set-valued letter.  A
one-letter interval then covers that target.  This gives (8.3).

Since (W=(2m+1)B), (C=o(B)), (S=o(B)), and
(H^2=O_A(m)), both the component overhead and the charged support loss
are (o(W)).  Equation (8.2) handles the remaining terms.  ∎

The use of set-valued repair letters is legitimate for the original
contiguous-OR problem.  The main spine remains singleton; the theorem does
not claim that a completely singleton universal cycle exists.

The common-core repair removes the cover-safe hypothesis altogether:

### Theorem 8.2 (unrestricted legal splicing with compressed seam repair)

Let

\[
                         C=c(D_{\mathcal F}).
\]

Use Theorem 1.1 to merge the initial rows to \(C\) circuits with exactly

\[
                         J=B-C                             \tag{8.4}
\]

legal successor switches.  Then, for every \(H\le(m+2)/2\), there is a
literal set-valued word covering every initially covered lower, middle,
and upper target through depth \(H\), of length at most

\[
\boxed{
 W+C(m+H-1)+2(B-C)(2H-1).}                                \tag{8.5}
\]

After appending the initially missing shallow targets, the length is at
most

\[
 W+C(m+H-1)+2(B-C)(2H-1)
   +2\Delta_H^-.                                           \tag{8.6}
\]

Consequently, if

\[
 c(D_{\mathcal F})=o(B),\qquad
 \Delta_H^-=o(W),\qquad H=o(m),                            \tag{8.7}
\]

then (8.6) is \(W+o(W)\).  In particular this holds at every fixed Gaussian
window \(H=\lceil A\sqrt m\rceil\).

#### Proof

Theorem 1.1 supplies (8.4).  Linearize the \(C\) final components using
Proposition 4.1, at cost \(W+C(m+H-1)\).  Lower windows and the exact
middle arc set are invariant by Proposition 5.1.  Apply Theorem 6.4 to the
\(J\) switches, giving the last term of (8.5) and restoring every initial
upper flag.  This proves (8.5); literal one-letter repairs of the initial
holes, together with the complement bound (5.2), prove (8.6).

Finally \(W=(2m+1)B\).  Under (8.7),

\[
 C(m+H-1)=o(Bm)=o(W),
\]

while

\[
 2(B-C)(2H-1)\le4BH
 =\frac{4H}{2m+1}W=o(W).
\]

The deficit term is \(o(W)\) by hypothesis.  ∎

Theorem 8.2 does not assert that the final singleton spine has gap
\(m+H\).  It says something more directly relevant to literal OR output:
all gap failures are confined to charged successor seams, and the complete
triangular shallow family destroyed there is restored at \(o(W)\) total
cost.  If an entirely gap-safe final singleton spine is itself required,
Theorems 3.1--3.2 remain the exact additional conditions.

## 9. The exact surviving gates

The repaired restricted cycle-splicing route has two necessary positive
inputs about one chosen exact factor, plus one optional stricter input for
an all-singleton conclusion.

1. **Ordered-state incidence:** prove (c(D_{\mathcal F})=o(B)), or the
   stronger dynamic compatible-matching condition (3.3).
2. **Dynamic gap compatibility (optional all-singleton gate):** find common-state ports satisfying the
   exact collar inequalities (2.5) through enough matching rounds.  Static
   two-row compatibility is not enough.
3. **Initial lower-shadow quality:** for the coefficient-one repaired-band theorem, prove

   \[
                         \Delta_H^-=o(W).                   \tag{9.1}
   \]

   Proposition 5.2 then gives the initial upper condition automatically.
   No cover-safety of the switches is needed, because Theorem 6.4 repairs
   every switched shallow fan at cost \(O(HB)=o(W)\).  If one insists on
   using the final singleton spine without set-valued seam repair, then one
   must instead prove the aggregate final-support bound

   \[
                    \sum_{q=1}^H\Delta_q(T_{\rm fin})=o(W). \tag{9.2}
   \]

Neither exact middle ownership nor recurrence injectivity supplies initial
shadow quality.  Conversely, Theorem 8.2 shows that ordered-state
connectivity plus initial shadow quality is sufficient with exact
coefficient-one accounting; dynamic gap compatibility is needed only for
the stricter all-singleton, un-repaired conclusion.

No assertion here promotes singleton states to a normal form for general
OR words.
