# Full-anchor annular SCD routing: residual flow and the depth-two memory cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 H=\lceil A\sqrt m\rceil,\qquad
 h=o(\sqrt m),
\tag{0.1}
\]

where \(A>0\) is fixed, and put

\[
 r=m-H,\qquad
 N=\binom nr.
\tag{0.2}
\]

Every rank-\(r\) set belongs to a unique chain of an SCD, and that chain
continues to rank \(r+1\).  The SCD therefore induces an inclusion matching

\[
 \mu:\binom{[n]}r\longrightarrow\binom{[n]}{r+1},
 \qquad A\subset\mu(A).
\tag{0.3}
\]

This note analyzes the canonical **full-anchor** route: when the chain
rooted at its annular rank-\(r\) member \(A\) is visited, append the mask
\(A\).  The conclusions are exact.

1. **Depth-one flow.**  Delete from each upper set \(\mu(A)\) its owner
   edge \(A\subset\mu(A)\).  The resulting bipartite graph has a perfect
   matching if and only if its exact Hall inequalities

   \[
    \boxed{
    \left|
      \bigcup_{A\in X}
      \left(\binom{\mu(A)}r\setminus\{A\}\right)
    \right|\ge |X|
    \quad\text{for every }X\subseteq\binom{[n]}r}
   \tag{0.4}
   \]

   hold.  Such a matching is exactly a contaminant-free directed cycle
   factor of the rank-\(r\) chain roots at the first annular step.

2. **Exact switch.**  A residual \(2\times2\) rectangle swaps two
   predecessor assignments.  If the two assignments lie on distinct
   cycles, the switch merges those cycles and preserves every root and
   every first-child colour.  Thus vertex-disjoint rectangle forests give
   a literal component-fusion criterion.

3. **Higher-memory criterion.**  After anchors
   \(A_1,\ldots,A_t\), the inherited state begins with \(A_t\), followed
   by the nonempty backward novelty classes

   \[
    A_{t-j}\setminus\bigcup_{i=0}^{j-1}A_{t-i}.
   \tag{0.5}
   \]

   The lower annular flag of the chain visited at time \(t\) is exposed
   precisely when the first required novelty classes are the prescribed
   singleton increments.  Hence pairwise Hall expansion is not the full
   switching criterion; the true state graph has memory
   \(\Theta(H)\).

4. **Depth-two statewise obstruction.**  There is a four-root residual
   cycle whose four first-child colours are distinct, while every
   three-anchor union is the same rank-\((r+2)\) set.  Thus it is a
   perfect depth-one flow object but cannot be the first two levels of an
   SCD.  Ordinary Hall, a one-factor, or even one depth-one cycle is
   insufficient already at \(q=2\).

The result neither constructs nor refutes a fully noncanonical SCD with
\(o(W)\) annular contaminants.  It proves the exact flow theorem at the
first boundary and identifies a literal statewise obstruction to lifting
that flow independently through the Gaussian annulus.  Any positive
theorem must use a common history-state flow, not one Hall system per
depth.

## 1. The SCD first-child matching

Fix an SCD \(\mathscr C\) of \(2^{[n]}\).  Since \(r<m\), a chain
containing a rank-\(r\) set cannot end at rank \(r\).  Therefore, for
every \(A\in\binom{[n]}r\), its chain contains a unique successor

\[
 \mu(A)=A\cup\{f(A)\}.
\tag{1.1}
\]

Different rank-\(r\) sets lie in different SCD chains or at different
positions of one chain.  A single chain has only one rank-\(r\) member,
and different chains are disjoint.  Consequently the successors
\(\mu(A)\) are pairwise distinct, proving that (0.3) is an inclusion
matching.

The chains meeting rank \(r=m-H\) are precisely the chains whose radius is
at least \(H\).  There are \(N\) of them.  Since

\[
 \frac NW=e^{-A^2+o(1)},
\tag{1.2}
\]

they form a positive-density family for fixed \(A\).

## 2. Exact depth-one full-anchor flow

Suppose the previous full anchor was \(P\in\binom{[n]}r\), so the current
state has first block \(P\).  Append the next root \(A\).  The updated
state begins

\[
 (A,\ P\setminus A,\ldots).
\tag{2.1}
\]

The first lower-annular successor of \(A\) is \(\mu(A)=A\cup\{f(A)\}\).
It is exposed by (2.1) if and only if

\[
 P\setminus A=\{f(A)\}.
\tag{2.2}
\]

Because \(|P|=|A|=r\), condition (2.2) is equivalent to

\[
 P\ne A,\qquad P\subset\mu(A).
\tag{2.3}
\]

This proves the following exact local statement.

### Lemma 2.1 (residual-incidence switch test)

A full-anchor update \(P\to A\) exposes the first annular child of \(A\)
if and only if \(P\) is an alternative rank-\(r\) face of \(\mu(A)\), as
in (2.3).

Define the residual incidence graph

\[
 \mathcal R_\mu
 =\left(
   \binom{[n]}r_{\rm pred},
   \binom{[n]}r_{\rm targ};
   E_\mu\right)
\tag{2.4}
\]

by

\[
 P A\in E_\mu
 \quad\Longleftrightarrow\quad
 P\in\binom{\mu(A)}r\setminus\{A\}.
\tag{2.5}
\]

Every target has degree \(r\).

### Theorem 2.2 (exact residual Hall theorem)

The following are equivalent.

1. Every root has one distinct contaminant-free full-anchor predecessor.
2. The graph \(\mathcal R_\mu\) has a perfect matching.
3. The Hall inequalities (0.4) hold for every target family \(X\).

Every perfect matching defines a permutation \(p\) of
\(\binom{[n]}r\), where \(p(A)\) is the predecessor assigned to \(A\).
The directed edges

\[
 p(A)\longrightarrow A
\tag{2.6}
\]

form a vertex-disjoint directed cycle factor, and every internal
transition exposes the prescribed first SCD child.

#### Proof

The equivalence of the first two statements is Lemma 2.1 plus the
requirement that no root serve as predecessor twice.  The equivalence of
the second and third statements is Hall's theorem.  A perfect matching is
a bijection from targets to predecessors, so (2.6) gives indegree and
outdegree one at every root and therefore a directed cycle factor.
Lemma 2.1 certifies every transition. \(\square\)

The exact deficiency form is

\[
 \delta(\mu)
 =\max_X\left(
 |X|-
 \left|
  \bigcup_{A\in X}
  \left(\binom{\mu(A)}r\setminus\{A\}\right)
 \right|\right).
\tag{2.7}
\]

A maximum residual matching has size \(N-\delta(\mu)\).  Thus
\(\delta(\mu)=o(W)\) is necessary for an \(o(W)\)-contaminant
full-anchor route, but it controls neither cycle count nor deeper state
composition.

## 3. Exact component switches

Let \(p\) be a perfect residual predecessor assignment.  Suppose

\[
 p(A)=P,\qquad p(B)=Q.
\tag{3.1}
\]

Assume the crossed residual incidences also exist:

\[
 P\in\binom{\mu(B)}r\setminus\{B\},
 \qquad
 Q\in\binom{\mu(A)}r\setminus\{A\}.
\tag{3.2}
\]

Then replace (3.1) by

\[
 p'(A)=Q,\qquad p'(B)=P.
\tag{3.3}
\]

### Lemma 3.1 (residual rectangle switch)

The assignment \(p'\) is again a perfect residual matching.  If the
directed edges \(P\to A\) and \(Q\to B\) lie on distinct cycles of the
cycle factor of \(p\), then (3.3) merges those two cycles into one.

#### Proof

Condition (3.2) makes both new assignments legal, and swapping two values
preserves bijectivity.  Cutting one directed edge in each of two cycles
gives two directed paths.  Reconnecting their two tails to the opposite
heads, as in (3.3), joins the paths into one directed cycle. \(\square\)

This gives a static sufficient criterion.  Form the interaction graph on
the cycles of \(p\), joining two cycles when they admit a rectangle
(3.1)--(3.2).  Suppose a spanning forest of this interaction graph can be
witnessed by pairwise vertex-disjoint rectangles.  Performing its switches
in a leaf-to-root order does not alter any unused witness assignment.
Each forest edge merges two current cycles.  Consequently:

### Corollary 3.2 (vertex-disjoint switch forest)

If the cycle interaction graph has a vertex-disjoint rectangle forest with
\(k\) connected components, the depth-one cycle factor can be switched to
one having exactly \(k\) cycles.  Cutting those cycles and concatenating
the resulting paths uses \(k-1\) directed prefix-contaminant joins.

Thus \(k=o(W)\) is an exact sufficient switching certificate at depth one.
The theorem is integral throughout; no randomized cycle-merging claim is
being used.

## 4. The inherited state has backward-anchor memory

The depth-one flow forgets most of the state.  The complete inherited
state is still elementary to write.

Start from an arbitrary ordered partition \(\Pi_0\), and append full
anchors

\[
 A_1,A_2,\ldots,A_t.
\tag{4.1}
\]

For \(j=1,\ldots,t-1\), define

\[
 L_{t,j}
 =A_{t-j}\setminus\bigcup_{i=0}^{j-1}A_{t-i},
\qquad
 U_t=\bigcup_{i=1}^tA_i.
\tag{4.2}
\]

### Lemma 4.1 (backward novelty normal form)

After the update \(A_t\), the state is

\[
 \left(
 A_t,\ L_{t,1},L_{t,2},\ldots,L_{t,t-1},
 \Pi_0-U_t\right),
\tag{4.3}
\]

with empty blocks deleted and with the blocks of \(\Pi_0-U_t\) retaining
their original order.

#### Proof

This is the last-touch normal form.  The elements whose most recent anchor
is \(A_{t-j}\) are precisely those in \(A_{t-j}\) and in none of the more
recent anchors \(A_{t-j+1},\ldots,A_t\), which is (4.2). \(\square\)

Let

\[
 \Lambda_{t,1},\Lambda_{t,2},\ldots
\tag{4.4}
\]

be the nonempty \(L_{t,j}\)'s in increasing order of \(j\).  Suppose the
SCD chain rooted at \(A_t\) begins

\[
 A_t
 \subset A_t+\{f_{t,1}\}
 \subset\cdots\subset
 A_t+\{f_{t,1},\ldots,f_{t,\ell}\}.
\tag{4.5}
\]

### Theorem 4.2 (exact history switching criterion)

The full-anchor history exposes (4.5) at checkpoint \(t\) if and only if

\[
 \boxed{
 \Lambda_{t,q}=\{f_{t,q}\}
 \quad(1\le q\le\ell).}
\tag{4.6}
\]

More generally, the entire truncated annular target family is exposed if
and only if its successive difference blocks form an initial coarsening
of the ordered novelty list (4.4), followed if necessary by blocks from
\(\Pi_0-U_t\).

#### Proof

By (4.3), the prefix union immediately after \(A_t\) grows through the
nonempty novelty blocks in the order (4.4).  Consecutive target sets in
(4.5) differ by the singleton \(f_{t,q}\), so the intervening state block
must be exactly that singleton.  This proves (4.6) in both directions.
For a nonsaturated gap between prescribed annular ranks, the union of the
intervening state blocks must equal the corresponding target difference;
this is exactly the stated initial-coarsening condition. \(\square\)

Theorem 4.2 is the exact composable switching criterion for the
full-anchor architecture.  It has memory equal to the number of previous
anchors needed to supply the first \(\Theta(H)\) nonempty novelty classes.
The residual Hall graph \(\mathcal R_\mu\) records only
\(\Lambda_{t,1}\).

## 5. A depth-one cycle with a forced depth-two collision

The loss of information is genuine already on four coordinates.
Let \(K\) be any set of size \(r-2\), and choose distinct
\(a,b,c,d\notin K\).  Define four rank-\(r\) roots

\[
 \begin{array}{ll}
 A_0=K\cup\{a,b\},&
 A_1=K\cup\{b,c\},\\
 A_2=K\cup\{c,d\},&
 A_3=K\cup\{d,a\}.
 \end{array}
\tag{5.1}
\]

Read indices cyclically modulo four, and prescribe the first children

\[
 \mu(A_i)=A_{i-1}\cup A_i.
\tag{5.2}
\]

Explicitly these are

\[
 K\cup\{a,b,d\},\
 K\cup\{a,b,c\},\
 K\cup\{b,c,d\},\
 K\cup\{a,c,d\},
\tag{5.3}
\]

so they are four distinct rank-\((r+1)\) sets.  Thus (5.2) is a legitimate
partial inclusion matching, and the cyclic predecessor assignment

\[
 p(A_i)=A_{i-1}
\tag{5.4}
\]

is a perfect residual matching on these four roots.  Every transition is
depth-one contaminant-free by Lemma 2.1.

This interface occurs literally in a noncanonical SCD.  When \(r=2\),
\(K=\varnothing\), the six chains

\[
 \begin{array}{rcl}
 \varnothing&\subset&a\subset ab\subset abd\subset abcd,\\
 b&\subset&bc\subset abc,\\
 c&\subset&cd\subset bcd,\\
 d&\subset&da\subset acd,\\
 &&ac,\\
 &&bd
 \end{array}
\tag{5.5}
\]

partition \(B_4\) and are symmetric.  Their four rank-\(2\to3\) edges are
exactly (5.2).  Thus the residual four-cycle is genuine SCD interface
data, not merely a feasible quotient pattern.

At checkpoint \(A_i\), however, the first two novelty singletons come from
\(A_{i-1}\) and \(A_{i-2}\), and their cumulative rank-\((r+2)\) set is

\[
 A_{i-2}\cup A_{i-1}\cup A_i
 =K\cup\{a,b,c,d\},
\tag{5.6}
\]

independently of \(i\).

### Theorem 5.1 (four-root depth-two obstruction)

The depth-one residual cycle (5.1)--(5.4) cannot be the first two levels
of four distinct chains in any chain partition, and hence cannot occur as
four depth-two flags of an SCD.

#### Proof

The first-child sets (5.3) are distinct, so there is no depth-one
ownership collision.  If the full-anchor history exposed two saturated
steps at every \(A_i\), Theorem 4.2 would make the second child at every
checkpoint equal the cumulative set (5.6).  Four distinct chains would
then all contain the same rank-\((r+2)\) set, contradicting disjointness
of a chain partition. \(\square\)

The obstruction is not a parity or divisibility issue.  It is precisely a
failure of hereditary state composition: the quotient flow has forgotten
the second backward novelty layer.

## 6. The exact higher-memory object

For a proposed root order, define its depth-\(q\) chronological colour at
time \(t\) to be

\[
 C_q(t)
 =A_t\cup\Lambda_{t,1}\cup\cdots\cup\Lambda_{t,q},
\tag{6.1}
\]

whenever the first \(q\) novelty classes are singletons.  A full-anchor
SCD schedule through lower depth \(Q\) must satisfy simultaneously:

1. every root \(A_t\) occurs once;
2. \(\Lambda_{t,q}\) is the prescribed \(q\)-th SCD increment for every
   \(q\le Q\); and
3. for each \(q\), the colours \(C_q(t)\) are distinct across the roots
   whose chains reach that depth.

The upper annulus and the central collar impose the same condition on the
later novelty blocks, with the appropriate nonsingleton coarsenings from
Theorem 4.2.

Equivalently, one may lift from roots to history states consisting of an
ordered list of previous anchors together with their nonempty novelty
classes.  A legal transition shifts the history, appends one new root,
and consumes one unit of every chronological colour (6.1).  Selecting one
history state per root with indegree and outdegree at most one is an exact
coloured path-cover integer program.

Here is a finite exact formulation for the entire SCD, including the
shorter chains.  For every chain \(C\), let \(\alpha(C)\) be the least
nonempty member of its prescribed truncated central-and-annular family.
For a radius-at-least-\(H\) chain this is its rank-\(r\) root; for a
shorter chain it is the least target that the chain actually reaches.
Let \(\mathfrak H(C)\) be the ordered-partition states whose first block is
\(\alpha(C)\) and which expose the complete prescribed target family of
\(C\).  Put

\[
 \mathfrak H=\{(C,\Pi):\Pi\in\mathfrak H(C)\}.
\tag{6.2}
\]

Join \(v=(C,\Pi)\) to \(w=(D,\Pi')\) when

\[
 \Pi'=M_{\alpha(D)}(\Pi).
\tag{6.3}
\]

Thus every arc is one literal full-anchor update and already includes all
depths through \(H\).  Introduce binary variables \(y_v\) and \(x_{vw}\).
The exact state-transversal linear-forest system is

\[
 \sum_{v\in\mathfrak H(C)}y_v=1
 \qquad\text{for every SCD chain }C,
\tag{6.4}
\]

\[
 \sum_{w:vw\in E}x_{vw}\le y_v,
 \qquad
 \sum_{u:uv\in E}x_{uv}\le y_v
 \qquad\text{for every }v,
\tag{6.5}
\]

and, for every nonempty \(S\subseteq\mathfrak H\) and every
\(v_0\in S\),

\[
 \sum_{\substack{vw\in E\\v,w\in S}}x_{vw}
 \le \sum_{v\in S}y_v-y_{v_0}.
\tag{6.6}
\]

If \(v_0\) is selected, (6.6) says that the selected subgraph induced by
\(S\) has at most one fewer edge than vertices; if \(v_0\) is unselected,
the inequality is harmless.  Thus its sole purpose is to exclude directed
cycles without first knowing the support of \(y\).

### Theorem 6.1 (exact full-anchor Gaussian criterion)

Let

\[
 p_H^*
 =W-\max\left\{\sum_{vw\in E}x_{vw}:
 (x,y)\text{ satisfies (6.4)--(6.6)}\right\}.
\tag{6.7}
\]

Then \(p_H^*\) is exactly the minimum number of genuine one-update
full-anchor state paths which visit every SCD chain once and expose its
complete truncated central-and-annular target.  Consequently the complete
full-anchor SCD schedule has \(o(W)\) directed prefix-contaminant joins if
and only if

\[
 \boxed{p_H^*=o(W).}
\tag{6.8}
\]

#### Proof

A feasible integral solution selects one state of every chain by (6.4).
Constraints (6.5) give indegree and outdegree at most one, while (6.6)
excludes cycles.  The selected arcs therefore form a vertex-disjoint
directed path cover.  Every arc is a literal composable update by (6.3).
It has \(W\) selected vertices and \(\sum x_{vw}\) edges, hence
\(W-\sum x_{vw}\) paths.

Conversely, choose the actual state at every chain checkpoint of any
full-anchor state-path cover and set its path arcs to one.  All constraints
hold, and the same forest identity recovers its number of paths.  Joining
\(p_H^*\) paths requires \(p_H^*-1\) transitions outside the certified
one-update forest. \(\square\)

The system is an exact switching criterion, but it is not an ordinary
single-commodity flow: the colour equalities (6.4) couple alternative
states of one chain, and the subtour cuts (6.6) couple components.
Projecting away the state coordinate leaves the residual Hall graph of
Section 2 and loses the novelty colours.

This lifted object is not the ordinary bipartite flow of Section 2:
Theorem 5.1 gives four roots on which the depth-one flow is integral and
cyclic while the depth-two colour capacity is violated by a factor four.
Any claimed min-cut theorem for the Gaussian annulus must therefore place
the common history state and all rank-colour capacities in the network.
Separate Hall theorems at the individual depths are insufficient.

## 7. Status

Proved here:

1. the exact residual-incidence Hall theorem for depth-one full-anchor
   routing;
2. an exact component-merging rectangle switch and a vertex-disjoint
   switch-forest criterion for \(o(W)\) depth-one seams;
3. the exact backward-novelty state formula for a sequence of full anchors;
4. the necessary-and-sufficient history criterion for exposing every
   prescribed annular block; and
5. a four-root integral depth-one cycle which is formally impossible at
   depth two.

Not proved here:

1. an SCD whose residual Hall graph has a long-cycle factor;
2. an extension of a chosen depth-one inclusion matching to a full SCD;
3. an integral history-state path cover through
   \(H=A\sqrt m\); or
4. coefficient one.

The gain is a sharp separation.  At one annular step the problem is an
ordinary integral flow with exact rectangle switches.  At Gaussian depth
it is a common-history coloured path-cover problem.  The four-root
obstruction proves that no theorem based only on the depth-one quotient
flow can establish the required noncanonical SCD schedule.
