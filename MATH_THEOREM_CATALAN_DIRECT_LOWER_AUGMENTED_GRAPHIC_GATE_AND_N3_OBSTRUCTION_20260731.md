# Direct lower shores after a rooted upper shore: the augmented graphic gate and a strict \(n=3\) obstruction

Date: 2026-07-31  
Status: exact all-parameter lower-shore reformulation; exact serializable-ear
criterion; independently replayed smallest fixed-basis obstruction.  No
all-parameter side-forest existence theorem is claimed.

## 0. Result

Fix an oriented child Catalan path forest \(F\), a direct common deletion
basis \(Q\), and one physically realized upper side forest.  Suppose the
upper forest is anchor-capped and has no anchor-free component.  Its
double-anchor components give a \(\operatorname {Cat}_n\)-matching
\(\Pi^-\).  Together with the partial matching \(P_0\) supplied by the
retained child segments, this gives a fixed forest \(F_0=P_0\cup\Pi^-\)
on two copies of \(Q\).

The lower alternating-cycle condition is not intrinsically nonlinear.
Attach every lower physical anchor to the component of \(F_0\) containing
its lower label.  The fixed attachment edges form a forest \(A_0\).  A
selected direct lower support \(S^+\) is compatible with the fixed upper
shore if and only if

\[
                         A_0\cup S^+\quad\hbox{is a forest}.       \tag{0.1}
\]

Thus, after the upper shore is fixed, the complete lower topology row is
one ordinary graphic-matroid independence condition on the direct lower
occurrences.  Palette exactness still contributes two partition bases and
the physical degree caps still contribute a \(b\)-matching row.  These
extra rows do not disappear into the graphic matroid.

This distinction is already sharp at the smallest physical parameter.
For the authenticated child \(n=3\) forest, the strict direct common bases
are exactly those whose retained edge has id

\[
                              0,1,5,11.                         \tag{0.2}
\]

At retained edge \(1\), there are two distinct no-empty upper rooted
supports and one distinct no-empty lower support.  Neither upper support
is compatible with the lower support: the two contracted unions have
cycle ranks \(1\) and \(4\).  Therefore

```text
upper no-empty rooted tree
+ marginally realizable lower no-empty side forest
+ strict direct common basis
```

does not imply a compatible lower shore for that fixed basis.  Retained
edges \(5\) and \(11\) do have compatible pairs, so this is a basis-choice
obstruction, not a refutation of the strict recursion.

## 1. Explicit fixed upper state

Write a child edge as

\[
 q=(L_q,U_q,t_q,h_q),\qquad
 L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.              \tag{1.1}
\]

Let \(Q\subseteq E(F)\) have order

\[
 C=\operatorname {Cat}_{n+1},\qquad
 K=\operatorname {Cat}_n.                            \tag{1.2}
\]

Use two formally disjoint copies

\[
 Q_T=\{q_T:q\in Q\},\qquad Q_H=\{q_H:q\in Q\}.      \tag{1.3}
\]

The copy \(q_T\) records the upper seam at the component of \(F-Q\)
containing \(t_q\); the copy \(q_H\) records the lower seam at the
component containing \(h_q\).  Define the central partial matching by

\[
 q_Tq'_H\in P_0
 \quad\Longleftrightarrow\quad
 [t_q]_{F-Q}=[h_{q'}]_{F-Q}.                          \tag{1.4}
\]

The tail and head component maps are injective, so (1.4) really is a
partial matching.  It includes the length-zero retained segments between
two consecutive deleted child edges.

Let the fixed upper side forest induce

\[
 q_Tq'_T\in\Pi^-
 \quad\Longleftrightarrow\quad
 U_q,U_{q'}\text{ lie in the same upper side component}. \tag{1.5}
\]

The no-empty hypothesis and the Catalan charge give
\(|\Pi^-|=K\).  Put

\[
 F_0=(Q_T\sqcup Q_H,\;P_0\sqcup\Pi^-).               \tag{1.6}
\]

This is always a forest.  Indeed, every \(Q_H\)-vertex has degree at most
one and all noncentral edges lie inside \(Q_T\), where they form a
matching.  Hence no cycle is possible.  If \(p_0=|P_0|\), then

\[
                 |\operatorname {comp}(F_0)|=2C-p_0-K. \tag{1.7}
\]

The formula does not assume that \(Q\) meets every child path.
More explicitly, if \(r_Q\) is the number of child paths containing at
least one edge of \(Q\), then a path containing \(s\ge1\) selected edges
contributes exactly \(s-1\) relations to (1.4).  Consequently

\[
                 p_0=C-r_Q,\qquad
                 |\operatorname {comp}(F_0)|=C+r_Q-K. \tag{1.8}
\]

## 2. The augmented lower graph

The lower physical vertex bank is

\[
                         V^+=\binom{\Omega}{n-1}.      \tag{2.1}
\]

For \(q\in Q\), its lower seam anchor is

\[
                         b^+(q)=L_q\in V^+.           \tag{2.2}
\]

The anchors (2.2) are distinct.  Let \(\kappa(q)\) be the component of
\(F_0\) containing \(q_H\), and introduce one auxiliary vertex
\(r_D\) for every \(D\in\operatorname {comp}(F_0)\).  Define the fixed
spoke forest

\[
 A_0=\{b^+(q)r_{\kappa(q)}:q\in Q\}.               \tag{2.3}
\]

It has \(C\) edges on distinct physical endpoints and is therefore a
forest, even when several spokes have the same auxiliary endpoint.

A direct lower occurrence is a pair \(e=(q,x)\), \(x\in L_q\), with

\[
\begin{aligned}
 \lambda(e)&=L_q-x\in\binom\Omega{n-2},\\
 \upsilon(e)&=U_q-x\in\binom\Omega n,\\
 \partial(e)&=\{t_q-x,h_q-x\}\subseteq V^+.          \tag{2.4}
\end{aligned}
\]

The physical edge \(\partial(e)\) is undirected.  Nothing here asserts
that the child ordering \(t_q\to h_q\) survives literally after projection;
once the complete support is a linear forest, its paths may be oriented
consistently at the output.

For the fixed basis \(Q\), retain only occurrences with

\[
                 \upsilon(e)\in
 D_Q:=\binom\Omega n\setminus\{h_q:q\in Q\}.         \tag{2.5}
\]

Parallel occurrences are kept as parallel elements, although two
occurrences with the same pair \((\lambda,\upsilon)\) have the same
physical edge.  Let \({\cal M}_{F_0}^+\) be the graphic matroid of the
augmented graph (2.1)--(2.3), contracted by \(A_0\), and pulled back to
the occurrence set through \(e\mapsto\partial(e)\).  Equivalently,

\[
 S\text{ is independent in }{\cal M}_{F_0}^+
 \quad\Longleftrightarrow\quad
 A_0\cup\partial(S)\text{ is a forest}.              \tag{2.6}
\]

### Theorem 2.1 (augmented-graphic equivalence)

Let \(S\) be a direct lower occurrence set such that the physical graph
\(G(S)=(V^+,\partial(S))\) is a linear forest and every lower anchor has
degree at most one.  Let \(\Pi^+(S)\) pair the two labels whose anchors
belong to the same two-anchor component of \(G(S)\).  Then

\[
 \boxed{\quad
 \beta(A_0\cup\partial(S))
   =\beta(P_0\cup\Pi^-\cup\Pi^+(S)).
 \quad}                                               \tag{2.7}
\]

In particular, the selected lower side has no alternating cycle against
\(P_0\cup\Pi^-\) if and only if it is independent in
\({\cal M}_{F_0}^+\).

#### Proof

Contract every path component of \(G(S)\).  This preserves cycle rank.
An anchor-free component becomes an isolated vertex.  A one-anchor
component and its spoke become a leaf at the appropriate auxiliary
vertex.  A two-anchor component and its two spokes become a length-two
path between the two auxiliary vertices prescribed by \(\kappa\); after
suppressing its middle vertex this is exactly the corresponding edge of
\(\Pi^+(S)\) after the components of \(F_0\) have been contracted.

Deleting isolated vertices, deleting leaves and suppressing degree-two
subdivision vertices preserve cycle rank.  Contracting the fixed forest
\(F_0\) also preserves cycle rank.  The resulting graph is precisely the
contraction of \(P_0\cup\Pi^-\cup\Pi^+(S)\), proving (2.7). \(\square\)

The construction has explicit size.  If
\(N=\binom{2n}{n-1}\), \(P=\binom{2n}{n-2}\) and
\(g_0=2C-p_0-K\), then the augmented graph has

\[
                  N+g_0\text{ vertices},\qquad C+P
                  \text{ edges}                      \tag{2.8}
\]

for a complete lower selection.  On the acyclic face its number of
components is

\[
 \begin{aligned}
 N+g_0-(C+P)
   &=N-P+C-p_0-K\\
   &=H+r_Q-K.
 \end{aligned}                                       \tag{2.9}
\]

### Corollary 2.2 (exact fixed-upper lower normal form)

A compatible strict direct lower shore exists if and only if there is a
set \(S\) of \(P\) retained occurrences satisfying all four rows:

1. \(\lambda:S\to\binom\Omega{n-2}\) is a bijection;
2. \(\upsilon:S\to D_Q\) is a bijection;
3. every physical vertex has degree at most two and every lower anchor
   has degree at most one; and
4. \(S\) is independent in \({\cal M}_{F_0}^+\).

No separate side-cycle or alternating-cycle row is needed: row 4 implies
that \(G(S)\) is a forest and Theorem 2.1 supplies the coupling condition.

If the lower shore is also required to have no anchor-free component, put

\[
 H=N-P=C-K                                                   \tag{2.10}
\]

and adjoin a new vertex \(\rho\) with all root edges
\(\rho b^+(q)\), \(q\in Q\).  The additional requirement is exactly that
there be a set \(R\) of \(H\) root edges for which

\[
                         \partial(S)\cup R             \tag{2.11}
\]

is a spanning tree on \(V^+\cup\{\rho\}\).  Thus the no-empty fixed-upper
problem is exactly

```text
two palette-partition bases
+ one rooted graphic base
+ one augmented graphic independence row
+ the physical degree caps.
```

This is an exact characterization, not a claim that the displayed
intersection is an ordinary two-matroid intersection.

## 3. What Rado does and does not prove

For either palette coordinate
\(\chi\in\{\lambda,\upsilon\}\), let \({\cal E}_c\) be the menu of
retained occurrences having color \(c\).  Rado's theorem applied to the
graphic matroid \({\cal M}_{F_0}^+\) gives the exact one-coordinate
statement:

### Proposition 3.1 (one-rainbow graphic Rado criterion)

There is a choice of one occurrence from every \(\chi\)-color menu whose
physical edges satisfy the augmented graphic row if and only if

\[
 r_{{\cal M}_{F_0}^+}
       \left(\bigcup_{c\in I}{\cal E}_c\right)
       \ge |I|
 \qquad\text{for every set }I\text{ of }\chi\text{-colors}.    \tag{3.1}
\]

Any selected Rado transversal is edgewise serializable: palette
injectivity and graphic independence are hereditary, so its edges may be
installed in any order.  The same is true of the physical degree caps if
the final transversal satisfies them.

Condition (3.1) controls only one palette coordinate.  Applying it once
to \(\lambda\) and once to \(\upsilon\) does not synchronize the two
transversals.  The full problem remains two partition bases plus the
graphic and degree rows.

There is nevertheless an exact Rado theorem when the recursion supplies
private complete path ears.

### Theorem 3.2 (private-ear graphic Rado theorem)

Fix a lower scaffold whose already suppressed links form a forest.  Let
\(I\) be a set of remaining ear slots.  For every \(i\in I\), let
\({\cal P}_i\) be a nonempty menu of complete direct lower path ears.  Assume
the following **serializability certificate**.

1. Every ear has exactly two unused lower anchors as endpoints, has no
   other anchor, and is locally palette-injective and degree-valid.
2. Physical vertices, lower and upper palette colors, and anchor endpoints
   used by different slots lie in disjoint private resource banks.
3. For every choice of one ear per slot, the chosen ears together with the
   scaffold cover exactly the prescribed remaining physical and palette
   resources.  No installed atom is later removed.

Contract the current scaffold and \(F_0\).  Map an ear \(P\) with anchor
labels \(q,q'\) to the quotient edge

\[
                       \sigma(P)=\kappa(q)\kappa(q').  \tag{3.2}
\]

Regard different ears with the same image as parallel elements of the
quotient graphic matroid \({\cal G}\).  There is a choice
\(P_i\in{\cal P}_i\) for every \(i\in I\) whose suppressed links are
acyclic if and only if

\[
 r_{\cal G}\!\left(
       \bigcup_{i\in J}\sigma({\cal P}_i)\right)
       \ge |J|
 \qquad(J\subseteq I).                                \tag{3.3}
\]

Every choice certified by (3.3) is physically serializable in an arbitrary
slot order.

#### Proof

Rado's theorem gives one independent quotient edge from every menu exactly
under (3.3).  Resource privacy makes the corresponding physical ears
disjoint and makes all palette and degree checks commute.  Every prefix of
an independent graphic set is independent, so every installation order
preserves the contracted-forest invariant. \(\square\)

The privacy assumptions are load-bearing.  Without them, two ears can
compete for a palette color, physical socket or anchor even when their
quotient edges are graphically independent.  The strict \(n=3\) example
below shows that even the two separate occurrence-level Rado systems can
both pass while the synchronized two-rainbow graphic selection is empty.

### Proposition 3.3 (exact component-ear serialization)

A complete compatible no-empty lower shore exists if and only if its
\(H=C-K\) path components can be installed as pairwise resource-disjoint
direct ears such that

1. their union is bijective on both palette banks and covers the side
   vertex bank;
2. every component has one or two anchors, with exactly \(K\) two-anchor
   ears; and
3. whenever a two-anchor ear is installed, its two \(\kappa\)-vertices
   lie in different components of the quotient formed by the previously
   installed two-anchor ears.

For a supplied final shore, every ordering of its two-anchor components
satisfies condition 3.

#### Proof

Conditions 1 and 2 are exactly palette saturation, the rooted no-empty
tree condition and the Catalan charge.  Condition 3 is the graphic
union-find rule.  It makes every prefix acyclic and hence the final shore
compatible by Theorem 2.1.  Conversely, the suppressed links of a
compatible shore form a forest.  Every subset of a forest is a forest, so
adding its edges in any order always joins two previously distinct
components. \(\square\)

This proposition makes serializability exact, but it does not by itself
supply the ears.  The remaining recursive theorem must provide either the
private menus of Theorem 3.2 or an adaptive way to construct the complete
resource-disjoint ear decomposition of Proposition 3.3.

## 4. Exact strict \(n=3\) obstruction

Use the authenticated parameter-three child in

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

and index its fifteen child edges in path order as in that witness.  A
retained id \(r\) means

\[
                         Q=E(F)\setminus\{r\}.         \tag{4.1}
\]

Exhaustive direct incidence matching gives exactly the four common bases
in (0.2).  Take \(r=1\).  Then

\[
 P_0=\{q_T(q-1)_H:3\le q\le14\}.                   \tag{4.2}
\]

It has twelve edges.  The two distinct no-empty upper rooted supports have
pairings

\[
\begin{aligned}
 \Pi^-_A={}&\{(0,12),(2,4),(3,8),(5,7),(10,13)\},\\
 \Pi^-_B={}&\{(0,12),(3,14),(4,6),(7,9),(10,13)\}.   \tag{4.3}
\end{aligned}
\]

The unique distinct no-empty lower support has pairing

\[
 \Pi^+=\{(0,10),(2,13),(3,5),(6,8),(9,12)\}.         \tag{4.4}
\]

For \(\Pi^-_A\), the union contains the four-cycle

\[
 10_T-9_H-12_H-13_T-10_T.                            \tag{4.5}
\]

For \(\Pi^-_B\), it contains four disjoint four-cycles:

\[
\begin{aligned}
 &3_T-2_H-13_H-14_T-3_T,\\
 &4_T-3_H-5_H-6_T-4_T,\\
 &7_T-6_H-8_H-9_T-7_T,\\
 &10_T-9_H-12_H-13_T-10_T.                           \tag{4.6}
\end{aligned}
\]

Thus the augmented graphic ranks fail by one and four respectively on the
only synchronized lower support.

The first fixed upper pairing gives a sharper warning about Rado.  On its
complete direct lower occurrence bank, all \(63\) nonempty inequalities
(3.1) pass for the six lower colors, and all \(63\) pass separately for
the six upper colors.  Nevertheless, there is only one distinct selection
bijective on both color banks, and it is the cyclic support (4.4).
Separate Rado transversals therefore cannot be synchronized by a formal
intersection argument.

For comparison, retained ids \(5\) and \(11\) each admit a compatible
no-empty upper/lower pair.  Retained id \(0\) has no physically legal
no-empty lower support.  The obstruction at id \(1\) is consequently the
smallest fixed-basis example that passes both marginal physical shores but
fails only at their coupling.

## 5. Reproducible audit

The standard-library audit

```text
scratch/audit_catalan_direct_lower_augmented_graphic_n3_20260731.py
```

reconstructs the child atoms and all direct occurrences, enumerates all
strict common bases at \(n=3\), checks both rooted side forests, rebuilds
\(P_0\), verifies the augmented-graphic identity and the literal cycles
(4.5)--(4.6), and exhausts both sets of Rado inequalities.  It writes

```text
scratch/catalan_direct_lower_augmented_graphic_n3_20260731.audit.json
```

No solver output, claimed component labels or claimed pairings are trusted.
