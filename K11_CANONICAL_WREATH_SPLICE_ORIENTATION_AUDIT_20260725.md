# Independent audit of the canonical (K=11) wreath splice criterion

Date: 2026-07-25

## 1. Verdict

The five displayed seam inequalities in Theorem 2.1 of
`K11_CANONICAL_WREATH_SPLICE_CRITERION_20260725.md` are necessary and
sufficient for the intended splice of two vertex-disjoint physical paths.
The two-candidate corollary is also correct for the fixed orientation used
there.

The source as first audited was missing one mathematical hypothesis: the
two old paths must be vertex-disjoint, in particular

\[
 S'_h\ne S_i,\qquad D'_h\ne D_i.
\tag{1.1}
\]

Without (1.1), disjointness \(S'_h\cap D_i=\varnothing\) alone allows
\(S'_h=S_i\), in which case \(\beta=a_i\) and the first exchange identity in
(2.1) is not a five-set exchange.  The phrase "a second physical path" is
apparently intended to include (1.1).  The current working copy now states
this hypothesis explicitly.

Reversing a canonical wreath gives genuinely new local choices.  At a fixed
target (D_i), the forward orientation makes the omissions
(z_{i-4},z_{i-3}) backward-safe, while the reverse orientation makes the
complementary omissions (z_{i-2},z_{i-1}) backward-safe.  Thus every one of
the four off-cycle facets is backward-safe in exactly one of the two tail
orientations.

This does not prove physical cycle fusion.  Reversing the head can still fail
in both orientations, and there is an exact four-case obstruction below.
What reversal does prove unconditionally is a degree statement for the graph
before the head tests: the orientation-expanded backward-safe quotient of
the forty-two wreaths has simple in-degree and out-degree at least four.
No positive minimum degree for the fully physical seam graph, and no
six-path fusion, follows from this argument.

## 2. Audit of the five inequalities

Assume that the two old paths are physical and vertex-disjoint and that all
displayed indices exist.  Before the splice, the relevant port words are

\[
 \ldots,a_{i-2},b_{i-2},a_{i-1},b_{i-1},a_i,b_i,\ldots
\]

and

\[
 a'_h,b'_h,a'_{h+1},b'_{h+1},\ldots.
\]

After replacing the old transition after (D_i) by the cross transition to
(S'_h), the word is

\[
 \ldots,a_{i-2},b_{i-2},a_{i-1},b_{i-1},a_i,
 \beta,a'_h,b'_h,a'_{h+1},b'_{h+1},\ldots.
\tag{2.1}
\]

The physical port rule is

\[
 a_j\ne b_{j+1},\qquad a_j\ne b_{j+2}
\tag{2.2}
\]

whenever those future deletion ports exist.  The only three changed
two-port tests are therefore

\[
 (a_{i-2};b_{i-1},\beta),\qquad
 (a_{i-1};\beta,b'_h),\qquad
 (a_i;b'_h,b'_{h+1}).
\tag{2.3}
\]

The old path already gives (a_{i-2}\ne b_{i-1}).  Removing that inherited
inequality from (2.3) leaves exactly

\[
 \boxed{
 \beta\notin\{a_{i-2},a_{i-1}\},\qquad
 b'_h\notin\{a_{i-1},a_i\},\qquad
 b'_{h+1}\ne a_i.}
\tag{2.4}
\]

Starting at (a'_h), both future deletion ports are those of the old second
path.  The immediate incidence inequalities (a_i\ne\beta) and
(a'_h\ne\beta) follow from vertex-disjointness: equality would give,
respectively, (S'_h=S_i) or (D'_h=D_i).  All earlier tests are inherited.
This proves both necessity and sufficiency; there is no missing sixth seam
inequality.

The exchange identities themselves are also correct under the same
nondegeneracy hypothesis.  Both \(S_i\) and \(S'_h\) are distinct facets of
\(U_i=\Omega\setminus D_i\), and both \(D_i\) and \(D'_h\) are distinct
facets of \(\Omega\setminus S'_h\), giving

\[
 S'_h=S_i-\beta+a_i,qquad
 D'_h=D_i-a'_h+\beta.
\tag{2.5}
\]

## 3. Audit of the fixed-orientation corollary

Put

\[
 q_0=z_{i-5},\ q_1=z_{i-4},\ q_2=z_{i-3},\
 q_3=z_{i-2},\ q_4=z_{i-1},\ q_5=z_i.
\tag{3.1}
\]

Then (U_i=\{q_0,\ldots,q_5\}).  The facets omitted by (q_5) and (q_0)
are \(S_i\) and \(S_{i+1}\), respectively.  In an exact wreath factor, the
other four facets lie in four distinct wreaths, all different from the tail
wreath.  This is the cross-edge matching fact proved as Lemma 6.1 below.

For the forward tail, the last three insertion ports are

\[
 a_{i-2}=q_3,\qquad a_{i-1}=q_4,\qquad a_i=q_5.
\]

Thus an off-cycle omission passes the two backward tests precisely when

\[
 \beta\in\{q_1,q_2\}=\{z_{i-4},z_{i-3}\}.
\tag{3.2}
\]

For either surviving facet, the remaining tests are exactly

\[
 b'_h\notin\{q_4,q_5\},\qquad b'_{h+1}\ne q_5,
\tag{3.3}
\]

which is (3.2) of the source note.  Hence Corollary 3.1 is correct for a
fixed forward orientation.  Its phrase "two physically eligible cases"
should read "two backward-eligible cases," since either one can still fail
(3.3).

The shadow identities are also correct in this orientation:

\[
 B^*=S_i\cap S'_h=U_i\setminus\{q_5,\beta\},
 \qquad
 Y^*=D_i\cap D'_h=D_i\setminus\{a'_h\}.
\tag{3.4}
\]

## 4. Exact effect of reversing the tail

Traverse the same alternating wreath in the reverse direction.  Around the
same target (D_i), the path now has

\[
 \ldots,S_{i+2},D_{i+1},S_{i+1},D_i,
\]

and its last three insertion ports are

\[
 q_2=z_{i-3},\qquad q_1=z_{i-4},\qquad q_0=z_{i-5}.
\tag{4.1}
\]

Applying (2.4) in this orientation excludes \(\beta=q_2,q_1\).  Therefore:

### Theorem 4.1 (orientation-complete tail facets)

For the four off-cycle facets (U_i-\beta):

\[
\begin{array}{c|c|c}
\beta & \text{unique backward-safe tail orientation}
      & (c,d):=(a_{\rm prev},a_{\rm tail})\\ \hline
q_1,q_2 & \text{forward} & (q_4,q_5)\\
q_3,q_4 & \text{reverse} & (q_1,q_0).
\end{array}
\tag{4.2}
\]

Thus allowing both orientations does not produce eight backward-safe
facet-orientation pairs.  It produces exactly four: every off-cycle facet,
with a unique tail orientation.

For a reverse-tail splice, the remaining head tests and new lower color are

\[
 b'_0\notin\{q_1,q_0\},\qquad b'_1\ne q_0,
\tag{4.3}
\]

\[
 B^*_{\rm rev}=S_{i+1}\cap S'_h
               =U_i\setminus\{q_0,\beta\}.
\tag{4.4}
\]

The new upper color is always \(D_i\setminus\{\alpha\}\), where \(\alpha\)
is the first insertion port of the chosen head orientation.  In particular,
head reversal can change the new upper color.

## 5. Exact effect of reversing the head

Write the five coordinates of a head source in its forward cyclic order as

\[
 S'_h=\{p_1,p_2,p_3,p_4,p_5\},
 \qquad
 (p_1,\ldots,p_5)=(x_{h-5},\ldots,x_{h-1}).
\tag{5.1}
\]

The first two outgoing deletion ports are

\[
 (p_1,p_2)\quad\text{in the forward orientation},
 \qquad
 (p_5,p_4)\quad\text{in the reverse orientation}.
\tag{5.2}
\]

Let ((c,d)=(a_{\rm prev},a_{\rm tail})) be the ordered forbidden pair
from the chosen tail orientation.  Both (c,d) lie in (S'_h).  The two
head orientations pass exactly as follows:

\[
\begin{aligned}
\text{forward head passes}
 &\Longleftrightarrow p_1\notin\{c,d\}\ \text{and}\ p_2\ne d,\\
\text{reverse head passes}
 &\Longleftrightarrow p_5\notin\{c,d\}\ \text{and}\ p_4\ne d.
\end{aligned}
\tag{5.3}
\]

### Proposition 5.1 (the two-orientation head obstruction)

Both head orientations fail if and only if

\[
 \boxed{
 (c,d)\in
 \{(p_5,p_1),(p_5,p_2),(p_1,p_4),(p_1,p_5)\}.}
\tag{5.4}
\]

Indeed, inspect the position of (d).  If (d=p_1) or (p_2), the
forward head fails, while the reverse head also fails exactly when
(c=p_5).  If (d=p_4) or (p_5), the reverse head fails, while the
forward head also fails exactly when (c=p_1).  If (d=p_3), the two
heads could both fail only if (c=p_1=p_5), which is impossible.

This proposition is the precise amount of extra freedom supplied by head
reversal.  It often rescues a seam, but it does not always do so.

### Example 5.2 (a cross edge dead in both directions)

Take the tail cyclic order

\[
 z=(2,6,3,4,5,1,11,7,8,9,10)
\]

and (i=5).  Then

\[
 D_i=\{7,8,9,10,11\},\quad U_i=\{1,2,3,4,5,6\},
 \quad\beta=6=z_{i-4}.
\]

The forward tail is backward-safe, its cross source is
(S'=\{1,2,3,4,5\}), and its forbidden pair is

\[
 (c,d)=(z_{i-1},z_i)=(5,1).
\]

Put \(S'\) in the second canonical order

\[
 x=(1,2,3,4,5,7,6,8,9,10,11).
\]

At this head, the forward deletion pair is ((1,2)), so it fails because
(1=d); the reverse deletion pair is ((5,4)), so it fails because
\(5=c\).

The reverse directed incidence is blocked as well.  In the second order,
\(\Omega\setminus S'=\{6,7,8,9,10,11\}\) occurs in the order
\[
 (7,6,8,9,10,11).
\]
The same missing coordinate \(\beta=6\) selects its forward tail
orientation and gives protected pair \((r,t)=(10,11)\).  In the first
order, the reverse head source \(\{7,8,9,10,11\}\) occurs in the order
\[
 (11,7,8,9,10).
\]
Its forward head fails at \(p_1=t=11\), and its reverse head fails at
\(p_5=r=10\).

The two cyclic length-five interval families in this example are disjoint.
For the first order they are
\[
\begin{gathered}
23456,\ 13456,\ 1345\,11,\ 1457\,11,\ 1578\,11,\ 1789\,11,\\
78910\,11,\ 278910,\ 268910,\ 236910,\ 234610,
\end{gathered}
\]
and none is among the eleven windows of the second order
\[
\begin{gathered}
12345,\ 23457,\ 34567,\ 45678,\ 56789,\ 678910,\\
68910\,11,\ 18910\,11,\ 12910\,11,\ 12310\,11,\ 1234\,11.
\end{gathered}
\]
Here juxtaposition is only compact set notation and the symbol \(11\) is
one coordinate, not two digits to be separated.

Thus even an external edge between two disjoint canonical wreaths may
disappear in both directed orientations of the fully physical port graph.
This example is not asserted to extend to a complete exact factor; it
disproves the local claim that one of the two directions or one of the two
head orientations must always work.

More generally, the seam rules alone permit all four facets at one target
to be blocked: for each facet, place its ordered pair ((c,d)) at
((p_5,p_1)) in the chosen head order.  Whether a named exact factor rules
out such a simultaneous configuration is a separate global question.

## 6. A sound minimum-degree theorem before the head tests

Let (O_6=KG(11,5)) be the odd graph.  The eleven length-five intervals of
one canonical coordinate order induce an eleven-cycle in (O_6).  Each of
its vertices has two neighbors within its own wreath and four external
neighbors.

### Lemma 6.1 (cross edges between two wreaths form a matching)

Let (C,C') be two distinct wreaths in an exact factor.  A vertex of (C')
has at most one neighbor in (C), and conversely.  Hence the cross edges
between (C) and (C') form a matching and there are at most eleven of
them.

To prove this, suppose a five-set (X\in C') were disjoint from two
five-intervals (I,J\in C).  Both (I,J) lie in the six-set
(\Omega\setminus X).  Two distinct cyclic five-intervals whose union has
size at most six must be consecutive; their union is a cyclic six-interval.
Its complementary five-set is itself a five-interval of (C), and that
complement is (X).  This contradicts the fact that the exact factor gives
distinct wreaths disjoint vertex sets.

### Theorem 6.2 (orientation-expanded backward degree)

Contract the forty-two wreath cycles, retain all cross incidences which pass
the backward seam tests in at least one tail orientation, and ignore the
head tests.  The resulting directed multigraph has weighted in-degree and
out-degree (44) at every wreath, and its underlying simple directed graph
has in-degree and out-degree at least four.

Indeed, a wreath has (11\cdot4=44) external odd-graph edges.  Theorem 4.1
makes every directed external incidence backward-safe in exactly one tail
orientation.  Lemma 6.1 permits at most eleven of these incidences to go to
one other wreath, so at least (44/11=4) other wreaths occur.  The statement
for incoming arcs follows by reversing the directed incidence.  The
underlying undirected quotient is connected because (O_6) is connected.

Equivalently, before directions are doubled, the external-incidence
quotient is a connected loopless \(44\)-regular multigraph with edge
multiplicity at most eleven.  It is therefore Eulerian and has no bridge:
for every vertex subset, the size of its edge cut has the same parity as
the sum of the even vertex degrees.  This is additional ordinary quotient
structure, but it still forgets the selected cut port at each wreath.

There is an exact uncontracted version.  Form the \(924\)-vertex port graph
but impose only cross incidence and the backward tests, ignoring both head
tests.  This digraph is \(4\)-in/\(4\)-out regular.  A fixed tail port has
two safe off facets and each facet has two possible head ports.  Conversely,
a fixed head port has four off-factor rank-six supersets, and Theorem 4.1
selects exactly one tail port over each.  Thus every wreath group has
weighted port-arc in-degree and out-degree \(22\cdot4=88\).  The fully
physical port graph is obtained by retaining zero, one, or two head ports
for each directed external incidence according to Proposition 5.1.

For comparison, one fixed tail orientation retains twenty-two incidences
per wreath and therefore guarantees only simple out-degree at least two by
the same argument.  Tail reversal genuinely doubles this unconditional
backward-degree guarantee.

Theorem 6.2 is not a minimum-degree theorem for fully physical seams.
Proposition 5.1 may delete every head orientation of a given incidence, and
the seam criterion alone gives no bound on how many such endpoint
obstructions occur in an exact factor.

## 7. Why no cycle-fusion conclusion follows

There are three independent couplings which the degree theorem omits.

First, if an intact canonical cycle is entered at (S_h), then its exit is
not arbitrary: the forward traversal exits after (D_{h-1}), while the
reverse traversal exits after (D_h).  Thus the head choice, tail choice,
and orientation of one cycle are a single state.  Orientations cannot be
chosen independently for every incident arc of a proposed quotient forest.

Second, the outgoing arc must avoid the four endpoint obstructions in
(5.4), not merely pass the backward tests.

Third, each selected arc fixes its new lower and upper shadow colors.  The
same selected set of arcs must retain support at least (319) in both
ledgers.

Consequently connectedness, the degree-four quotient bound, or an ordinary
spanning forest in the cycle quotient does not prove a physical six-path
fusion.  A valid next theorem would have to be a path-cover theorem in the
two-orientation endpoint-state graph, with the head tests and both shadow
colors attached to every arc.

## 8. Audit of the companion port-forest equivalence

Theorem 6.1 of K11_MSW_PHYSICAL_CYCLE_SPLICE_GATE_20260725.md is sound for
its stated one-cut-per-wreath model.  Deleting one selected incidence edge
from a wreath gives a unique oriented path from its rank-five endpoint to
its rank-six endpoint.  An incoming selected arc can use only the head and
an outgoing selected arc can use only the tail.  Hence indegree and
outdegree at most one use every endpoint at most once.  A directed acyclic
selection on forty-two ports with thirty-six arcs is a union of six
directed paths.

There is also no hidden interaction between the incoming and outgoing seam
tests of an internal wreath: the remaining long side of the cut
eleven-cycle contains ten old source transitions, whereas physicality has
radius two.  Thus filtering every selected arc by the five seam tests is
sufficient for physicality of the concatenation.

One formula later in that companion note needs an orientation qualifier,
but this does not affect Theorem 6.1.  Relative to the originally fixed
order \(z\), its equation (8.1)
\[
 B^*=U_i\setminus\{z_i,\beta\}
\]
is the forward-tail formula.  At the reverse tail it is instead
\[
 B^*=U_i\setminus\{z_{i-5},\beta\}.
\]
The displayed equation is valid for all ports only if the coordinate order
is silently reoriented along with the port, so that its newly named current
insertion is again denoted \(z_i\).

## 9. Line-level editorial findings in the source note

* Lines 13--40: the canonical definitions and port identities are correct.
* Lines 44--70: the explicit vertex-disjointness/nondegeneracy hypothesis
  is necessary before asserting the two exchanges in (2.1); it has now
  been added to the working copy.
* Lines 72--116: the five inequalities and proof are correct once that
  hypothesis and existence of the displayed indices are understood.
* Lines 118--170: the two-candidate result is correct only for the fixed
  forward orientation.  Change "physically eligible" to
  "backward-eligible."
* Lines 172--194: the two shadow formulas and the two displayed lower colors
  are correct for that orientation.  The display opened at line 181 lacks a
  closing `\]` after tag (4.2).
* Lines 196--207: the count (42\cdot11=462) is correct for fixed oriented
  tails.  If reversal is admitted, there are four backward-safe facets per
  target in the union of orientations, not two.  The warning that quotient
  connectivity alone does not settle fusion is correct.
* Lines 74 and 162 contain a control character in place of `\beta`, and the
  proof endings contain literal `(square)` instead of `\(\square\)`.
