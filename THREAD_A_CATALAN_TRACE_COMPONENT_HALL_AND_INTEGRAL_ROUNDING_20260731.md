# Exact component Hall cuts for Catalan trace decoration

Date: 2026-07-31  
Status: proved fixed-cycle integral rounding theorem and exact Hall
compression; this is a sufficient middle-levels-resolvable subclass, not a
normal form for arbitrary Catalan linear matchings

## 1. Scope and notation

Fix \(m\geq 2\), put

\[
 \Omega=[2m-1],\qquad
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P=\operatorname {Cat}_m.
\tag{1.1}
\]

Let

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0
\tag{1.2}
\]

be a fixed Hamilton cycle of \({\rm ML}(2m-1)\), with

\[
 A_i\subset B_i\supset A_{i+1}.
\]

Its upper and lower turn colours are

\[
 u_i=B_{i-1}\cup B_i\in\binom\Omega{m+1},\qquad
 \ell_i=A_i\cap A_{i+1}\in\binom\Omega{m-2}.
\tag{1.3}
\]

All subscripts are read modulo \(Q\).  The results below concern only diamond
matchings supported on this one cycle.  Proposition 5.1 of
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
shows that an arbitrary Catalan linear matching need not have such a
representation.

## 2. The augmented trace graph

Let

\[
 {\cal U}_0=\binom\Omega{m+1},\qquad
 {\cal L}_0=\binom\Omega{m-2}.
\]

Define a bipartite graph \({\cal G}_C\) with shores

\[
 \bigl(\{A_i:i\in\mathbb Z_Q\}\sqcup{\cal L}_0\bigr)
 \quad\hbox{and}\quad
 \bigl(\{B_i:i\in\mathbb Z_Q\}\sqcup{\cal U}_0\bigr).
\tag{2.1}
\]

It has the following edges and no others:

\[
 A_i u_i,\qquad \ell_iB_i,\qquad A_iB_{i-1},\qquad A_iB_i.
\tag{2.2}
\]

Thus a turn edge chooses an occurrence of a required outer colour, while a
cycle edge retains one residual cross incidence.

### Theorem 2.1 (integral trace-rounding theorem)

Perfect matchings of \({\cal G}_C\) are in bijection with pairs of turn
representative sets \(I,J\subseteq\mathbb Z_Q\) satisfying

1. \(i\mapsto u_i\) is a bijection
   \(I\to{\cal U}_0\);
2. \(j\mapsto\ell_j\) is a bijection
   \(J\to{\cal L}_0\); and
3. the selected \(A_i\)'s and \(B_j\)'s alternate in the cyclic order
   (1.2).

For a perfect matching, the residual cross matching is exactly its set of
edges between the \(A\)- and \(B\)-positions.  In particular, once a
fractional perfect matching of \({\cal G}_C\) has been proved, bipartite
integrality gives an integral Catalan decoration; no further rounding lemma
is needed on this fixed cycle.

#### Proof

In a perfect matching, each vertex of \({\cal U}_0\) is matched to exactly
one occurrence \(A_i\) of its colour \(u_i\), and each vertex of
\({\cal L}_0\) is matched to exactly one occurrence \(B_j\) of its colour
\(\ell_j\).  Call the corresponding index sets \(I,J\).  Every remaining
position vertex must be covered by an \(A\)--\(B\) cycle edge.  Hence the
unselected vertices of (1.2) have a perfect matching in their induced
cycle subgraph.  This happens exactly when each nonempty residual path has
even order, equivalently when consecutive selected positions have opposite
shore types.  This proves the forward implication.

Conversely, the two bijective turn selections match all colour vertices.
Alternation makes every residual component an even path, whose perfect
matching covers all remaining position vertices.  The union is therefore
a perfect matching of \({\cal G}_C\).  The last assertion is the integral
perfect-matching theorem for bipartite graphs. \(\square\)

## 3. Exact compression of every Hall cut

For \(S\subseteq\mathbb Z_Q\), regarded as a set of \(A\)-positions, put

\[
 \Gamma(S)=\{B_{i-1},B_i:i\in S\},
 \qquad
 U(S)=\{u_i:i\in S\}.
\tag{3.1}
\]

For a lower colour \(L\in{\cal L}_0\), let

\[
 O_L=\{B_j:\ell_j=L\},
\]

and define the number of lower occurrence classes trapped in the collar of
\(S\) by

\[
 \lambda(S)=|\{L\in{\cal L}_0:O_L\subseteq\Gamma(S)\}|.
\tag{3.2}
\]

The empty occurrence set is allowed in (3.2); consequently the case
\(S=\varnothing\) detects failure of lower-turn surjectivity.

### Theorem 3.1 (component-Hall criterion)

The graph \({\cal G}_C\) has a perfect matching if and only if, for every
\(S\subseteq\mathbb Z_Q\),

\[
 |U(S)|+|\Gamma(S)|-\lambda(S)\ \geq\ |S|.
\tag{3.3}
\]

If \(S\) is nonempty and proper and has \(c(S)\) cyclic components, then

\[
 |\Gamma(S)|=|S|+c(S),
\]

so (3.3) becomes the particularly transparent cut

\[
 \boxed{\ \lambda(S)-|U(S)|\leq c(S).\ }
\tag{3.4}
\]

For one cyclic interval \(S\), this is

\[
 \lambda(S)\leq |U(S)|+1.
\tag{3.5}
\]

Thus the exact obstruction is not a marginal shortage on either turn word:
it is excess opposite-colour occurrence classes trapped behind too few
turn-colour classes and too few boundary components.

#### Proof

An arbitrary subset of the left shore of \({\cal G}_C\) has the form
\(S\sqcup D\), where \(S\) is a set of \(A\)-positions and
\(D\subseteq{\cal L}_0\).  Its neighbourhood has disjoint position- and
colour-parts and hence size

\[
 |N(S\sqcup D)|=|U(S)|+|\Gamma(S)\cup O(D)|,
\tag{3.6}
\]

where \(O(D)=\bigcup_{L\in D}O_L\).  The occurrence sets \(O_L\) are
pairwise disjoint.  For fixed \(S\), adding a lower colour \(L\) to \(D\)
changes

\[
 |\Gamma(S)\cup O(D)|-|D|
\]

by \(|O_L\setminus\Gamma(S)|-1\).  This is negative exactly when
\(O_L\subseteq\Gamma(S)\), zero when precisely one occurrence lies outside,
and positive otherwise.  Therefore the minimum over all \(D\) is

\[
 |\Gamma(S)|-\lambda(S).
\tag{3.7}
\]

Hall's inequality for every \(S\sqcup D\) is consequently equivalent to
(3.3) for every \(S\).  The two shores have equal size \(Q+P\), so Hall's
theorem finishes the proof.  Finally, each proper cyclic component of
\(S\) contributes exactly one more \(B\)-neighbour than \(A\)-vertices,
which gives (3.4). \(\square\)

### Corollary 3.2 (the first local obstruction)

For two consecutive \(A\)-positions \(A_i,A_{i+1}\) carrying the same
upper turn colour, their three-position collar

\[
 \{B_{i-1},B_i,B_{i+1}\}
\]

cannot contain the complete occurrence classes of three distinct lower
turn colours.  This is the smallest connected support on which (3.4) can
fail once the lower turn word is surjective: a one-position \(S\) has a
two-position collar, so distinct nonempty occurrence classes give
\(\lambda(S)\leq2=|U(S)|+1\).

The symmetric statement, obtained by interchanging the two shores and the
two turn words, is equally valid.

All subsets \(S\), rather than only connected intervals, occur in the exact
criterion.  A colour occurrence class can meet several components, so no
claim is made that the connected cuts alone imply all disconnected cuts.

## 4. Occurrence-variable interval cuts

The same obstruction has an exact projected form.  Let
\(0\leq\alpha_i,\beta_i\leq1\) denote the amounts of selected \(A_i\)- and
\(B_i\)-turns.  Let \(p_i\) be the residual amount on \(A_iB_i\), and
\(q_i\) that on \(B_iA_{i+1}\).  The position equations are

\[
 p_i+q_{i-1}=1-\alpha_i,
 \qquad
 p_i+q_i=1-\beta_i.
\tag{4.1}
\]

### Theorem 4.1 (exact circular-interval projection)

There exist nonnegative \(p_i,q_i\) satisfying (4.1) if and only if

\[
 \sum_i\alpha_i=\sum_i\beta_i
\tag{4.2}
\]

and, for every cyclic interval of indices from \(r\) through \(s\),

\[
 \sum_{i=r}^{s}\alpha_i-
 \sum_{i=r}^{s-1}\beta_i\leq1.
\tag{4.3}
\]

Equation (4.3) is the odd-vertex arc inequality for

\[
 A_r,B_r,A_{r+1},\ldots,B_{s-1},A_s.
\]

Its complementary arc gives the symmetric inequality with \(A,B\)
interchanged.  For zero-one \(\alpha,\beta\), (4.2)--(4.3) hold exactly
when the selected marks alternate by shore.

#### Proof

Subtract the two equations in (4.1):

\[
 q_i-q_{i-1}=\alpha_i-\beta_i.
\tag{4.4}
\]

Cyclic consistency is exactly (4.2).  On a lifted indexing of the circle,
put

\[
 D_i=\sum_{k=0}^{i}(\alpha_k-\beta_k).
\]

Every solution of (4.4) has \(q_i=t+D_i\).  Since
\(p_i=1-\beta_i-q_i\), nonnegativity is equivalent to

\[
 \max_i(-D_i)\leq t\leq
 \min_j(1-\beta_j-D_j).
\tag{4.5}
\]

Such a \(t\) exists exactly when, for every ordered pair \(i,j\),

\[
 D_j-D_i\leq1-\beta_j.
\]

Reading the indices cyclically from \(i+1\) through \(j\), this is (4.3).
For zero-one marks, a failure of alternation gives an arc whose same-shore
endpoints are consecutive selected marks and hence violates (4.3).
Conversely, every subarc of an alternating sequence has shore discrepancy
at most one. \(\square\)

Theorem 4.1 identifies the exact missing interval cuts if one keeps only
the two turn-occurrence partition rows.  Theorem 3.1 is their colour-level
Hall compression.  In the full augmented graph these are ordinary
bipartite matching cuts, so they introduce no new fractional-to-integral
gap.

## 5. A literal abstract obstruction with the \(m=3\) cardinalities

The two turn-surjections alone do not imply (3.4).  Take \(Q=10,P=5\), and
write five upper colours \(U_1,\ldots,U_5\) and five lower colours
\(L_1,\ldots,L_5).  Consider the occurrence words

\[
 (u_0,\ldots,u_9)=
 (U_1,U_1,U_2,U_3,U_4,U_5,U_2,U_3,U_4,U_5),
\tag{5.1}
\]

\[
 (\ell_0,\ldots,\ell_9)=
 (L_2,L_3,L_4,L_5,L_4,L_5,L_4,L_5,L_4,L_1).
\tag{5.2}
\]

Both words are surjective.  But for \(S=\{0,1\}\),

\[
 U(S)=\{U_1\},\qquad
 \Gamma(S)=\{B_9,B_0,B_1\},\qquad
 \lambda(S)=3.
\]

Thus (3.4) reads \(3-1\leq1\), which is false.  Equivalently, the three
lower representatives \(B_9,B_0,B_1\) are forced, whereas the only upper
colour occurring at \(A_0,A_1\) contributes only one representative.  The
five-position arc

\[
 B_9,A_0,B_0,A_1,B_1
\]

has selected-shore discrepancy at least two.

This is an abstract occurrence-table counterexample whose cardinalities
match \(m=3\).  It is not asserted to be the turn table of an actual
middle-levels Hamilton cycle.  Its purpose is only to prove that two
separate rainbow/surjection statements do not contain the common
alternating-SDR theorem.

## 6. Escaping the sole binary-trace cycle face

Once Theorem 3.1 gives a decoration, the physical lift has maximum degree
two.  By the exact trace criterion in the source note, it is a forest
unless every maximal unmarked run has length two and every maximal marked
run has odd length.

Two useful exact consequences are as follows.

### Proposition 6.1 (odd Catalan automatic forest)

If \(K=\operatorname {Cat}_m\) is odd, every Catalan decoration of \(C\)
has a linear-forest lift.

#### Proof

On the exceptional cycle face, the \(2K\) unmarked positions form exactly
\(K\) runs, all of length two.  There are therefore also \(K\) marked runs,
all of odd length.  Their total length has parity \(K\), but their total
length is \(2P\), which is even.  Hence the exceptional face requires \(K\)
even. \(\square\)

### Proposition 6.2 (four-zero forced-block criterion)

Fix \(i\).  If \({\cal G}_C\) has a perfect matching containing the two
cycle edges

\[
 A_iB_i\quad\hbox{and}\quad A_{i+1}B_{i+1},
\tag{6.1}
\]

then the associated physical lift is a linear forest.  Equivalently, it is
enough that the balanced graph obtained from \({\cal G}_C\) by deleting the
four position vertices

\[
 A_i,B_i,A_{i+1},B_{i+1}
\]

have a perfect matching.  This last assertion has an ordinary Hall
certificate.

#### Proof

The two forced matching edges make four consecutive cycle positions
unmarked.  Their maximal unmarked run therefore has length at least four,
which is outside the exceptional face.  Forcing the two disjoint edges and
deleting their endpoints is the standard perfect-matching reduction.
\(\square\)

Consequently, for odd \(K\), (3.3) alone is a complete fixed-cycle
sufficient theorem for the ordered four-transversal.  For even \(K\), the
forced-block Hall test is one explicit sufficient escape from the single
bad trace face.

## 7. Relation to the global Catalan linear-matching LP

The cuts (3.3)--(3.4) are exact for the **chosen middle-levels support**.
They must not be advertised as inequalities valid for every arbitrary
Catalan linear matching: the \(m=3\) example in the source note proves that
some linear diamond matchings are not middle-levels-resolvable at all.

Likewise, the uniform fractional point satisfying the global diamond
matching, cap-two and all graphic inequalities does not by itself select a
Hamilton support cycle or satisfy (3.3) for a prescribed one.  What has
been proved here is the precise fixed-cycle rounding statement:

* all simultaneous upper-turn, lower-turn and alternating-occurrence
  correlation is exactly one bipartite Hall problem;
* its complete Hall family compresses to (3.3), or to the component cuts
  (3.4); and
* after Hall, only the explicitly described binary-trace cycle face remains
  before obtaining an ordered four-transversal.

Thus the smallest additional correlation obstruction in the one-cycle
architecture is the connected cut (3.5), with the first possible failure
given by Corollary 3.2.  The still-open global theorem is to construct a
cycle satisfying these cuts (and escaping the cycle face), or to round the
unrestricted ordered four-transversal directly.  No equivalence between
those two routes is claimed.

## 8. Adversarial audit

1. The two shores of \({\cal G}_C\) both have size \(Q+P\).  Thus the
   one-shore Hall test used in Theorem 3.1 really does imply a perfect
   matching covering both shores.
2. Formula (3.7) uses the fact that the sets \(O_L\) partition the
   \(B\)-positions.  It would be false for overlapping occurrence
   resources; no such generalization is claimed.
3. Connected cuts are displayed because they expose the first local
   obstruction, not because they form a complete test.  The exact theorem
   retains every disconnected \(S\).
4. The table (5.1)--(5.2) is not asserted to arise from a Boolean
   middle-levels Hamilton cycle.  It certifies only the logical
   independence of separate turn-surjectivity and common alternation.
5. Neither Theorem 3.1 nor Theorem 4.1 is an inequality valid for every
   unrestricted diamond matching.  Both are projections of the additional
   choice to support the matching on the fixed cycle \(C\).
6. The Hall theorem settles occurrence correlation and the middle degree
   cap in this subclass, but it does not automatically settle topology when
   \(K\) is even.  Proposition 6.2 is sufficient, not necessary, for
   escaping the exceptional binary-trace face.
