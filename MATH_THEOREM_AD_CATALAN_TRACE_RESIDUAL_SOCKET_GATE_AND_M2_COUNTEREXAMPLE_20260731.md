# Alternating trace decorations: literal ports, residual socket gate, and the smallest counterexample

Date: 2026-07-31  
Status: exact physical translation, exact residual-socket criterion, and
transparent-gluing composition; explicit \(m=2\) counterexample to automatic
residual-socket closure; no all-dimension decoration theorem

## 0. Result

For a Catalan decoration of one middle-levels Hamilton cycle, the binary
mark trace determines every selected physical Johnson occurrence, every
middle degree, and every formal path port.  The forced residual cross
matching has \(K=\operatorname{Cat}_m\) edges, exactly the number of path
components in the forest case, but this numerical equality does not make it
a connector bank.

There are two separate facts.

1. The residual matching itself is part of the common-transversal forest,
   so its edges are not closure edges.
2. It can serve as the matching-side **host bank** for uniformly outgoing
   upper-coherent connector sockets only on the strict run face
   \[
    \boxed{
      \text{every unmarked run has length at least four, and every marked
      run has even length}.}                            \tag{0.1}
   \]
   Even on this face, connector existence is an additional directed
   Hamilton-cycle condition in a literal endpoint/upper-colour socket graph.

The additional condition is not automatic.  The unique middle-levels cycle
at \(m=2\), with one adjacent \(A\)-mark and \(B\)-mark, is a genuine
Catalan decoration with trace \(110000\).  Its lift is a spanning two-path
forest and satisfies (0.1), but its residual-host socket digraph has only one
of the two required directions.  Both possible endpoint connector cycles
exist, yet each attaches both doubled upper blocks to the same path
component, so neither is uniformly outgoing.

Thus the alternating SDR makes topology and endpoint ports explicit; it
does not supply safe connector sockets for free.

The phrase "alternating SDR" is essential.  For a fixed upper turn
transversal \(I\), its existence is exactly Hall in the induced
gap--lower-colour graph from
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`.
Separate surjectivity of the upper and lower turn words is insufficient:
the authoritative \(m=4\) cycle has both surjections but fails that Hall
condition for every one of its \(12{,}288\) upper SDRs.  Every result below
therefore starts only **after** the gap--Hall/interlacing gate has passed.

This note uses neither the retracted `GK_PROJECTION_COUNTS`/`GK_TWO`
\(W/2\)-retention assertion nor any claim that an arbitrary Catalan Linear
Matching is middle-levels-resolvable.

## 1. Literal physical trace model

Let

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0            \tag{1.1}
\]

be a Hamilton cycle of \({\rm ML}(2m-1)\), where

Throughout this note \(m\ge2\).

\[
 A_i\in\binom{\Omega}{m-1},\qquad
 B_i\in\binom{\Omega}{m},\qquad
 A_i\subset B_i\supset A_{i+1}.                        \tag{1.2}
\]

Adjoin a new coordinate \(\infty\), and write the physical middle vertices
in cyclic order as

\[
 v_{2i}=\widehat A_i:=\{\infty\}\cup A_i,\qquad
 v_{2i+1}=B_i.                                         \tag{1.3}
\]

Let \(I\) mark \(A\)-turns and \(J\) mark \(B\)-turns, and define

\[
 \varepsilon_{2i}=1_{i\in I},\qquad
 \varepsilon_{2i+1}=1_{i\in J}.                       \tag{1.4}
\]

Assume \(I\) is an upper turn transversal and \(J\) is a lower turn
transversal selected by a perfect matching of the gap--lower-colour graph.
Thus consecutive marks have opposite rail types.  Equivalently, every
cyclic zero-run of \(\varepsilon\) has even length.  Merely assuming that
the two complete turn words are separately surjective would not justify
this step.

### Theorem 1.1 (literal edge formula)

The perfect diamond matching determined by the decoration lifts to the
following physical edge set:

\[
 F_\varepsilon=
 \bigl\{v_{r-1}v_{r+1}:\varepsilon_r=1\bigr\}
 \ \dot\cup\ R_\varepsilon,                            \tag{1.5}
\]

where, for every cyclic block

\[
 v_p,\underbrace{v_{p+1},\ldots,v_{p+2b}}_{\text{unmarked}},
 v_{p+2b+1}                                             \tag{1.6}
\]

whose endpoints are marked, the forced residual matching contributes

\[
 v_{p+1}v_{p+2},\quad v_{p+3}v_{p+4},\quad\ldots,\quad
 v_{p+2b-1}v_{p+2b}.                                   \tag{1.7}
\]

Every edge in (1.5)--(1.7) is a literal Johnson edge.  Its lower and upper
outer colours are:

\[
\begin{array}{c|c|c}
\text{selected occurrence}&\text{lower colour}&\text{upper colour}\\ \hline
B_{i-1}B_i&A_i&B_{i-1}\cup B_i\\
\widehat A_i\widehat A_{i+1}&\{\infty\}\cup(A_i\cap A_{i+1})
  &\{\infty\}\cup B_i\\
\widehat A_iB_i&A_i&\{\infty\}\cup B_i\\
B_{i-1}\widehat A_i&A_i&\{\infty\}\cup B_{i-1}.
\end{array}                                             \tag{1.8}
\]

The first row is selected when \(A_i\) is marked, the second when \(B_i\)
is marked, and the last two are the two possible residual cross
occurrences.  The two turn bijections plus the forced residual matching make
the lower and upper columns in (1.8) exact bijections on the complete outer
palettes.

#### Proof

A marked position is suppressed in the middle-levels cycle, so its two
physical neighbours are joined by the unique same-rail Johnson turn edge.
After deleting all marked positions, every residual component of (1.1) is
an even path; its perfect matching is uniquely (1.7).  This proves (1.5).
Intersections and unions give (1.8) directly.  Exact outer coverage is the
decorated-cycle matching theorem. \(\square\)

### Corollary 1.2 (literal degree and port formula)

For every physical position,

\[
 \deg_{F_\varepsilon}(v_r)
   =(1-\varepsilon_r)+\varepsilon_{r-1}+\varepsilon_{r+1}. \tag{1.9}
\]

Thus a degree-one vertex is one endpoint port, while a degree-zero vertex is
a trivial component with two formal ports.

#### Proof

An unmarked vertex lies in exactly one edge of the residual matching.  A
turn chord is incident with \(v_r\) precisely when it is centred at one of
the two neighbouring marked positions.  A marked vertex has no residual
edge. \(\square\)

Once the binary-trace criterion certifies that \(F_\varepsilon\) is a
forest, orient its paths.  For a physical edge \(XY\), put

\[
 L=X\cap Y,\qquad U=X\cup Y.
\]

If the path orientation is \(X\to Y\), the ordered four-transversal record
is

\[
 (L,\ a=X\setminus L,\ b=Y\setminus L,\ U,\ T=X,\ H=Y). \tag{1.10}
\]

The lower and upper entries are bijective by (1.8); tails and heads are
injective because oriented paths have indegree and outdegree at most one;
and directed acyclicity is literal.  Hence (1.10) is the promised
occurrence-level translation to the ordered four-transversal theorem.

It is a sufficient middle-levels-resolvable subclass only.  It does not
normalize an arbitrary ordered four-transversal or arbitrary Catalan Linear
Matching.

## 2. Where the residual edges sit

Write the cyclic trace as

\[
 1^{a_1}0^{2b_1}1^{a_2}0^{2b_2}\cdots1^{a_s}0^{2b_s},
 \qquad a_t,b_t\ge1.                                   \tag{2.1}
\]

In the \(t\)-th zero-run denote its residual edges by

\[
 r_{t,j}=v_{p+2j-1}v_{p+2j},\qquad 1\le j\le b_t.      \tag{2.2}
\]

There are

\[
 |R_\varepsilon|=\sum_tb_t
   ={\#\{r:\varepsilon_r=0\}\over2}=K                \tag{2.3}
\]

such edges.

### Proposition 2.0 (residual matching is an internal assembly bank)

Let

\[
 T_\varepsilon=\{v_{r-1}v_{r+1}:\varepsilon_r=1\}
\]

be the turn-chord graph before adding \(R_\varepsilon\).  Then
\(T_\varepsilon\) is a forest with exactly \(2K\) components.  Every
residual edge uses free endpoint capacity in this forest.  If
\(F_\varepsilon=T_\varepsilon\cup R_\varepsilon\) is a forest, all \(K\)
residual edges are bridges and reduce the component count to \(K\).  In the
cyclic trace face, they instead collectively create the one cycle.

In particular, \(R_\varepsilon\) is not the missing closure bank of
\(F_\varepsilon\): it is already inside the outer-palette perfect matching.
Deleting one of its edges deletes that edge's unique lower and upper
services; re-adding it only restores the same internal assembly edge.

#### Proof

Within every marked run, turn chords split by position parity into paths;
the intervening zero positions prevent a cyclic parity component.  Hence
\(T_\varepsilon\) is a forest.  It has \(2Q\) vertices and one distinct edge
for each of the \(2P\) marks, so it has

\[
 2Q-2P=2(Q-P)=2K
\]

components.  A zero at the boundary of a zero-run has turn degree one and
an internal zero has turn degree zero.  Thus every edge in (1.7) respects
the degree-two capacity.  The component claims follow from adding \(K\)
edges to a forest and from the exact binary-trace cyclerank, which is either
zero or one.  Palette essentiality follows from the perfect-matching
bijections in (1.8). \(\square\)

### Lemma 2.1 (terminal residual edges)

Call a residual edge **terminal** when it is incident with at least one
degree-one endpoint of its final \(F_\varepsilon\)-component.  An isolated
two-vertex residual component is terminal at both ends.

Every residual edge in the \(t\)-th zero-run is terminal in its
\(F_\varepsilon\)-component if and only if \(b_t\ge2\), equivalently the
zero-run has length at least four.

#### Proof

The first and last zeroes of the run are each incident with one boundary
turn chord and therefore have degree two.  Every interior zero has degree
one.  If \(b_t=1\), the sole residual edge joins the two boundary zeroes and
is internal at both ends.  If \(b_t\ge2\), every residual pair contains at
least one interior zero; the intermediate pairs contain two. \(\square\)

### Theorem 2.2 (one residual host per path)

Assume \(F_\varepsilon\) is a forest.  The following are equivalent.

1. Every path component contains exactly one edge of \(R_\varepsilon\), and
   that edge is terminal in the component.
2. Every zero-run has length at least four and every marked run has even
   length:
   \[
      b_t\ge2\quad\text{and}\quad a_t\equiv0\pmod2
      \qquad(1\le t\le s).                             \tag{2.4}
   \]

#### Proof

Lemma 2.1 gives the necessity of \(b_t\ge2\).  Under this hypothesis, an
intermediate residual pair strictly inside a zero-run is an isolated
two-vertex path, so it already contains exactly one residual edge.

Consider the chord graph across a marked run, including the boundary zero
on each side.  Chords join positions two apart, so it splits by parity.  If
\(a_t\) is odd, one parity path joins the two boundary zeroes and hence the
two boundary residual edges, while the other parity path contains no
residual edge.  Thus one component contains two residual edges and another
contains none.  If \(a_t\) is even, the two parity paths each contain one
boundary zero and terminate at opposite marked endpoints.  Each therefore
contains exactly one boundary residual edge.  This proves both necessity
and sufficiency. \(\square\)

Condition (2.4) is strictly stronger than the forest alternative.  A forest
needs only one run defect: some zero-run of length at least four **or** some
marked run of even length.  The residual-host bank needs both statements at
every run.

## 2A. The unique closure supported by the original middle-levels cycle

Let \(C_0\) be the physical cross-edge cycle with cyclic vertices
\(v_0,\ldots,v_{2Q-1}\).  We now ask for closure edges only from the unused
base occurrences

\[
 S\subseteq E(C_0)\setminus R_\varepsilon.             \tag{2.5}
\]

This is a genuine restriction: arbitrary Johnson edges between path ports
are not required to lie in \(C_0\).

### Theorem 2.3 (canonical base-cycle closure)

Assume \(F_\varepsilon\) is a forest.  There is a set \(S\) satisfying
(2.5) for which \(F_\varepsilon\cup S\) is two-regular if and only if
every maximal marked run has length exactly two.

When it exists, \(S\) is unique.  It consists of:

1. the base edge joining the two marks in every `11` run; and
2. for every zero-run \(z_1,\ldots,z_{2b}\), the gap edges
   \[
    z_2z_3,\ z_4z_5,\ldots,z_{2b-2}z_{2b-1}.           \tag{2.6}
   \]

It has \(|S|=K\), and \(F_\varepsilon\cup S\) is one literal Hamilton
cycle, not merely a cycle cover.

#### Proof

A boundary zero of every zero-run already has degree two in
\(F_\varepsilon\), so no mark--zero base edge can be selected.  The internal
zero ports must therefore be paired successively by exactly the gap edges
(2.6).

In a marked run, only its first and last positions are ports; a one-mark run
has two formal ports at its sole vertex.  If the run has length one, both
neighbouring base edges meet saturated boundary zeroes.  If its length is at
least three, every base edge incident with a terminal mark has its other
endpoint at an internal marked vertex of degree two.  The only possible case
is therefore a two-mark run, where the edge between the two marks uses both
ports.  This proves necessity and uniqueness.

Conversely, (2.6) turns every residual matching on a zero-run into the path

\[
 z_1-z_2-\cdots-z_{2b}.
\]

Across a marked pair \(p_1,p_2\), the two turn chords and the added pair
edge traverse the block from its left boundary to its right boundary in the
order

\[
 \lambda-p_2-p_1-\rho.
\]

Thus every zero block is traversed forward and every marked pair in reverse.
The blocks concatenate in their original cyclic order, yielding one
Hamilton cycle.  The degree equations also give
\(|S|=|V|-|F|=K\). \(\square\)

### Corollary 2.4 (sharp dimensional obstruction)

The canonical base-cycle closure face is empty for every \(m\ge4\).

#### Proof

There are \(2P\) marks.  If every marked run has length two, there are
exactly \(P\) marked runs and hence \(P\) nonempty zero-runs.  Since the
total zero length is \(2K\), necessarily \(P\le K\).  But

\[
 {P\over K}={m-1\over2}.                               \tag{2.7}
\]

Therefore \(P\le K\) exactly when \(m\le3\). \(\square\)

At \(m=3\), equality \(P=K\) forces every zero-run also to have length two,
so the only possible trace shape is \((1100)^K\), up to rotation.  This is
only a trace consequence; an actual turn choice passing the exact
gap--Hall/interlacing criterion on one physical middle-levels cycle still
has to be constructed.

### Theorem 2.5 (palette ledger and direction sign)

For the unique set \(S\) in Theorem 2.3, both maps

\[
 s\longmapsto\ell(s),\qquad s\longmapsto u(s)          \tag{2.8}
\]

are injective.  Every connector colour is already supplied by an adjacent
selected forest occurrence:

* a marked-pair connector takes its lower colour from the \(A\)-turn and
  its upper colour from the \(B\)-turn;
* a zero-gap connector takes its lower and upper colours from its two
  adjacent residual edges.

Hence adding \(S\) gives both outer profiles \(1^{N-K}2^K\), and every
connector is locally coherent with one same-upper and one same-lower forest
edge.

However, in the canonical Hamilton orientation, marked-pair connectors and
zero-gap connectors have opposite upper-provider signs: for one kind the
same-upper forest edge follows the connector, and for the other it precedes
it.  Global reversal flips both signs simultaneously.  Therefore, relative
to the two orientations of this fixed canonical Hamilton cycle, the closure
is uniformly outgoing exactly when there are no zero-gap connectors.  In the
nontrivial dimensions allowed by Corollary 2.4, this is
the rigid \(m=3\) face; the \(m=2\) face has both signs and is not uniformly
outgoing.

#### Proof

The colour identities follow by taking intersections and unions in the two
local block types.  The canonical set \(S\) is a matching on physical
middle-levels positions: every connector uses a distinct \(A\)-position and
a distinct \(B\)-position.  Since the cycle lists every \(A_i\) and \(B_i\)
once, the lower labels \(A_i\) and upper labels
\(\{\infty\}\cup B_i\) are injective.  The marked/zero split shows that the
two connector classes cannot collide.

When every marked run is `11` and every intervening zero-run is even, all
marked pairs begin on the same rail.  Along the Hamilton traversal in the
proof of Theorem 2.3, every marked pair is traversed in reverse while every
zero block is traversed forward.  Therefore all marked-pair connectors have
one common upper-provider sign and all zero-gap connectors have the opposite
sign.  There are \(K-P\) zero-gap connectors.  Thus none occur exactly when
\(K=P\), which by (2.7) is \(m=3\). \(\square\)

Theorem 2.3 is a positive literal socket theorem and Corollary 2.4 is a
sharp obstruction to extending it as an all-dimension normal form.  Neither
statement restricts arbitrary non-base Johnson connectors.

## 3. The exact residual-host socket graph

Assume (2.4).  For every path component \(C\), let \(q_C\) be its unique
residual edge and let

\[
 U_C=u(q_C).                                            \tag{3.1}
\]

If \(q_C\) has only one degree-one endpoint, call it \(t_C\), the proposed
entrance; let \(h_C\) be the other endpoint of the whole path.  If
\(C=q_C\) is an isolated residual edge, either endpoint may be chosen as
\(t_C\), and the other is \(h_C\).

For a fixed choice at every isolated residual component, define the directed
socket graph \(D_R\) on the path components by

\[
 C\longrightarrow C'
 \quad\Longleftrightarrow\quad
 h_C\cup t_{C'}=U_{C'}.                                \tag{3.2}
\]

The equality in (3.2) says literally that \(h_Ct_{C'}\) is a Johnson
connector with the same upper colour as \(q_{C'}\), sharing the entrance
endpoint \(t_{C'}\).

### Theorem 3.1 (residual-host connector equivalence)

There is a uniformly outgoing, upper-block-coherent endpoint connector
cycle which uses precisely the residual edges \(q_C\) as its matching-side
terminal hosts if and only if some choice of orientations for the isolated
residual components makes \(D_R\) contain a directed Hamilton cycle.

For a selected arc \(C\to C'\), the connector is forced to be

\[
 d_{C,C'}=h_Ct_{C'}.                                   \tag{3.3}
\]

These connectors are pairwise distinct, disjoint from
\(F_\varepsilon\), and have pairwise-distinct upper colours.  If the
intermediate lower floor is also required, one must additionally impose

\[
 h_C\cap t_{C'}\quad\text{pairwise distinct over the selected arcs}. \tag{3.4}
\]

Because the forest already uses every lower colour once and the closure has
\(K\) edges, (3.4) is exactly the connector condition for the intermediate
lower profile \(1^{N-K}2^K\).  It does not ask connector colours to avoid the
forest palette; each selected connector repeats one existing colour.

Any packet, collar, guard, residence, or compiler resource needs its own
literal privacy constraint.

#### Proof

An incoming connector immediately followed by \(q_{C'}\) must meet the
component at \(t_{C'}\), leave the preceding component at \(h_C\), and have
upper colour \(U_{C'}\).  This is exactly (3.2), so a coherent connector
cycle gives a directed Hamilton cycle in \(D_R\).

Conversely, a directed Hamilton cycle selects one incoming and one outgoing
port at every path component.  Equations (3.2)--(3.3) make every selected
edge Johnson and give it the upper colour of the following terminal host.
The colours \(U_C\) are distinct because the original diamond matching is
exact on the upper shore.  Hence the connectors are distinct.  No selected
connector is in \(F_\varepsilon\): its upper colour occurs in the forest
only on \(q_{C'}\), and the connector is a different edge with that colour.
Contracting the paths gives the selected directed Hamilton cycle, so the
physical union is one Hamilton cycle.  Lower connector colours obey the
usual floor exactly when (3.4) holds. \(\square\)

The theorem is a literal stateful Hall object: ordinary reachability or an
uncoloured Hamilton cycle on the components is insufficient.  At clean
quotient scale, one must further require primitive total voltage.  A linear
carrier deletes one physical connector occurrence, not an entire orbit.

If (2.4) fails, a safe closure may still exist by choosing terminal host
edges among the selected **turn** edges or by using a different component
orientation.  Therefore (2.4) is exact for the residual-only host normal
form, not necessary for all connector constructions.

## 4. Smallest physical counterexample

Take \(m=2\), old ground set \(\Omega=\{0,1,2\}\), and adjoin
\(\infty\).  The middle-levels graph has the cycle

\[
 A_0=0, B_0=01, A_1=1, B_1=12, A_2=2, B_2=02, A_0. \tag{4.1}
\]

Choose

\[
 I=\{0\},\qquad J=\{0\}.                              \tag{4.2}
\]

The unique upper turn colour is

\[
 u_0=B_2\cup B_0=012,
\]

and the unique lower turn colour is

\[
 \ell_0=A_0\cap A_1=\varnothing.
\]

Thus both turn maps are surjective, and the two adjacent marks have opposite
rail types.  More exactly, the fixed upper transversal has one gap, that
gap sees the unique lower colour, and its gap--colour graph is \(K_{1,1}\).
Hence the authoritative gap--Hall antecedent holds.  The physical trace is

\[
 \begin{array}{c|cccccc}
 \text{position}&0&1&2&3&4&5\\ \hline
 v_r&\infty0&01&\infty1&12&\infty2&02\\
 \varepsilon_r&1&1&0&0&0&0.
 \end{array}                                            \tag{4.3}
\]

The lifted perfect diamond matching is

\[
 F=\{02-01,\ \infty0-\infty1,\ \infty1-12,\
       \infty2-02\}.                                   \tag{4.4}
\]

It is the two-path forest

\[
 C_1:\ \infty0-\infty1-12,
 \qquad
 C_2:\ 01-02-\infty2.                                 \tag{4.5}
\]

The residual hosts are

\[
\begin{array}{c|c|c|c|c}
 C& q_C&t_C&h_C&U_C\\ \hline
 C_1&\infty1-12&12&\infty0&\infty12\\
 C_2&02-\infty2&\infty2&01&\infty02.
\end{array}                                             \tag{4.6}
\]

Condition (2.4) holds: the marked run has length two and the zero-run has
length four.  Nevertheless,

\[
 h_{C_1}\cup t_{C_2}=\infty02=U_{C_2},
\]

whereas

\[
 h_{C_2}\cup t_{C_1}=012\ne\infty12=U_{C_1}.          \tag{4.7}
\]

Thus \(D_R\) contains \(C_1\to C_2\) but not
\(C_2\to C_1\); no residual-host directed connector cycle exists.

This is not a topology obstruction.  There are exactly two endpoint
connector cycles:

\[
\begin{aligned}
 D_0&=\{\infty0-\infty2,\ 12-01\},\\
 D_1&=\{\infty0-01,\ 12-\infty2\}.
\end{aligned}                                           \tag{4.8}
\]

Each makes \(F\cup D_i\) a physical Hamilton cycle.  Each connector also
has a unique same-upper-colour terminal matching edge, but the attachment
map is constant:

* both connectors of \(D_0\) attach, through their same-upper forest edge,
  to \(C_2\);
* both connectors of \(D_1\) attach to \(C_1\).

Hence neither closure is uniformly outgoing.  The example separates three
levels exactly:

1. alternating SDR and physical path forest: **yes**;
2. endpoint-private Hamilton closure: **yes**;
3. residual-host or even unrestricted uniformly outgoing upper-coherent
   closure: **no**.

It is therefore a scoped counterexample to automatic safe sockets, not to
the decorated-cycle theorem, the Catalan Linear Matching assertion, or
ordinary Hamilton closure.

## 5. Correct reduced target

Within the decorated-middle-levels architecture the construction problem is
now the following ordered sequence.

1. Choose one middle-levels Hamilton cycle whose two turn maps admit the
   exact gap--Hall matching: some upper transversal \(I\) must have a
   perfect matching in its gap--lower-colour graph.  Two separate turn
   surjections do not suffice.
2. Require the trace to be in the forest face of the binary criterion.
3. If the forced residual edges are to be the terminal socket hosts, impose
   the strict run condition (2.4).
4. Solve the literal directed socket cycle (3.2), with lower-colour
   injectivity (3.4), primitive voltage when quotienting, and all physical
   private-resource rows.
5. Only then impose residence, deeper shadows, boundary chronology, and the
   asymmetric common-cap compiler.

Steps 3--4 are not consequences of the alternating SDR.  Conversely, they
are only a sufficient residual-host face; a valid construction may use turn
edges as some terminal hosts, exactly as the \(m=2\) closures demonstrate.

### 5.1 Transparent gluing is the correct decoration interface, not a socket theorem

The fixed-cycle obstruction from the authoritative \(m=4\) gap--Hall note
is not an existence obstruction in that dimension.  By
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`, one
standard incidence-hexagon toggle repairs it and gives an explicit decorable
Hamilton cycle of \({\rm ML}(7)\) whose lift is a spanning
\(\operatorname {Cat}_4=14\)-path forest.

That theorem also supplies the exact recursion interface.  A fixed
decoration survives a hexagon toggle if and only if

1. the selected local turn-colour multisets agree before and after the
   toggle, separately on the two shores; and
2. after the three retained fragments are reconnected, discard any fragment
   whose selected subsequence is empty; in the cyclic order of the remaining
   nonempty subsequences, the last selected shore type of each and the first
   selected shore type of the next are opposite.

Call such a toggle **transparent**.

### Proposition 5.1 (exact composition with the physical socket gate)

Suppose a middle-levels factor starts with globally bijective selected turn
palettes and selected shore types alternating on every factor cycle.  Suppose
it is joined into a Hamilton cycle by a tree of hexagon toggles, each
dynamically valid on the current factor and transparent for those same
selected vertex sets.  Let \(\varepsilon\) be the final cyclic mark trace.

1. The final physical diamond lift is literally the graph
   \(F_\varepsilon\) of (1.5)--(1.7), with degree and ports given by (1.9).
2. It is a forest exactly under the binary trace criterion of the parent
   trace theorem.
3. On the final forest, if the residual matching is required to be the
   terminal host bank, then it has exactly one terminal host per path
   exactly under (2.4), and the desired uniformly outgoing upper-coherent
   closure exists exactly under Theorem 3.1.

Thus a joint alternating SDR plus transparent gluing tree is sufficient for
the final decoration.  Together with a protected trace breaker, or an exact
post-gluing pass of item 2, it is sufficient for the decorated forest.  It
does **not** by itself imply either linearity or safe residual-host sockets.

Here a protected breaker must remain disjoint from every later toggle port;
otherwise only the final exact trace test supplies item 2.

#### Proof

Transparency preserves the two selected turn palettes and cyclic
alternation at every toggle, so induction gives a decoration on the final
cycle.  Theorem 1.1 and Corollary 1.2 then give the literal lift and ports.
The binary trace theorem gives item 2, while Theorems 2.2 and 3.1 give item
3.  No implication has been inserted between those independent conditions.
Indeed, the \(m=2\) example of Section 4 is already a decorated one-node
gluing tree (no toggle is needed), lies on the strict run face, and still
fails the residual socket cycle. \(\square\)

The trace-run part can be propagated through a gluing tree by a finite exact
boundary state: on each retained fragment record the first and last bit,
the two boundary-run summaries (zero length clipped at four together with
its parity, and one length modulo two), whether the whole fragment is one
run, and whether every completed internal run already satisfies (2.4).
Reversal swaps the two boundary summaries, and concatenation merges them
when their bits agree.
At the root, the same rule merges and tests the final and initial cyclic
boundary runs; the whole-fragment flag prevents counting one run twice.
This is an exact finite automaton for (2.4).  The transparent decoration
state separately records whether each selected subsequence is empty and,
when nonempty, its first and last selected shore types.  In contrast, the
socket gate must additionally carry the literal path endpoints, the chosen
terminal host and its upper colour for each component, or an equivalent
occurrence-labelled socket relation.  The transparent-hexagon palette and
selected-shore boundary bits alone do not determine that relation.

Consequently the recursive target is:

\[
 \boxed{\text{joint alternating SDR + transparent gluing tree
 + exact trace-run state + endpoint-labelled socket state}.}
\]

Freezing an arbitrary SDR before a published gluing tree is too strong, and
choosing an arbitrary published gluing tree before solving the SDR is too
weak.  Even after the two are co-designed, endpoint/socket feasibility and
the later compiler constraints remain separate.

## 6. Sources and scope

The exact parent reductions are:

* `MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`;
* `MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`;
* `MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`;
* `MATH_THEOREM_CATALAN_PATH_FOREST_CONNECTOR_AND_SMOOTHING_LEDGER_20260731.md`;
* `MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`.

No arbitrary Catalan Linear Matching is asserted to admit the trace form.
No all-\(m\) socket cycle, residence theorem, or contiguous-OR compiler is
claimed.

## 7. Independent audit and source freeze

Independent symbolic audits checked:

* all four colour rows in (1.8) and the degree formula (1.9);
* the component-parity proof of Theorem 2.2;
* uniqueness and connectedness in Theorem 2.3;
* the ratio \(P/K=(m-1)/2\), palette injectivity, and provider-sign ledger;
* both directions of the residual-host socket equivalence; and
* the complete \(m=2\) endpoint pairing census, including the two
  nonisomorphic Hamilton closures and their constant attachment maps;
* the gap--Hall and componentwise hypotheses in Proposition 5.1, including
  empty selected fragments and dynamic transparency on the current factor;
  and
* the exact finite trace-run boundary state, cyclic wrap, and the separation
  between transparent decoration data and endpoint-labelled socket data.

The decisive proofs are combinatorial and do not rely on finite search.
The authoritative input hashes at audit time were:

```text
aac430e2b2aaece12c42fafe3c84df4ffa57e0837814f4ff623458e08f322d1c  MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md
a9779950d781b1914fca6eafca6212da2b21e1560c8b68bfb2cfaae85759d1a8  MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md
c19f5e7a5bef20a16ca6fc0f475cb6084f7d3ed4a07b5c657611231c9ab5aec0  MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md
94bd265bce22854386cf49510fb79a18d1aec4d23389be3fd80d01eb9c4772cc  MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
e2ca586397a21275439ab86253bf5a8893b8072f220c7c9341cfe162b7435c69  MATH_THEOREM_CATALAN_PATH_FOREST_CONNECTOR_AND_SMOOTHING_LEDGER_20260731.md
a88042f078f76c369d20a353281dfc950abf634b624ce2bf80d2704c7e176d33  MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md
```
