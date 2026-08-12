# Anchor-pair contraction for the two-coordinate physical row

Date: 2026-07-31  
Status: exact contraction and solver-free sufficient/obstruction criteria;
independent replay of the \(n=3,4\) fixtures; no all-\(n\) punctured-side
existence theorem

## 0. Verdict

The common-basis gate is closed by
MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md.
It is not an open hypothesis here.

Fix an oriented child Catalan path forest \(F\) and an automatically
available common basis \(Q\). Suppose the two diagonal incidence matchings
have been physically realized as side forests \(G^-,G^+\), with side degree
at most two and seam-anchor degree at most one. Every side component then
has at most two anchors, and:

1. every double-anchor minus component induces one matching edge between
   tail components of \(F-Q\);
2. every double-anchor plus component induces one matching edge between
   head components of \(F-Q\); and
3. the contracted attachment graph \(\Gamma_Q\) is a forest if and only if
   the union of these two matchings has no alternating cycle.

The exact component charge

\[
 c_2^\pm-c_0^\pm=\operatorname{Cat}_n=:K
 \tag{0.1}
\]

therefore fixes the number of contraction links:

\[
 |E(H)|=2K+c_0^-+c_0^+.
 \tag{0.2}
\]

This yields a proof-safe induction state: the two shore matchings, their
signed charges, and a union-find/leaf-peeling state for their union. Adding
each new double-anchor component between two currently distinct contraction
components preserves acyclicity.

There is also a sharp local obstruction. Two consecutive moved child edges
cannot be paired by their direct side Johnson edge: on the minus shore its
intersection label is a selected tail deleted from \(D^-\), and on the plus
shore its union label is a selected head deleted from \(D^+\). A local
zipper must therefore use a longer nonanchor cap or a nonconsecutive/cross-
path pair.

The exact \(n=3,4\) fixtures satisfy the pairing-forest criterion. At
\(n=3\) the contracted union has 10 edges on 14 used vertices; at \(n=4\)
it has 29 edges on 39 used vertices. Both have maximum degree two and admit
a complete leaf peeling. This validates the state but does not construct
the side forests for all \(n\).

## 1. Setup after the automatic common basis

Let \(F\) be an oriented \(K\)-path forest on the rank-\(n\) middle layer,
where

\[
 |E(F)|=N,\qquad |V(F)|=M,\qquad M-N=K.
 \tag{1.1}
\]

Let \(Q\subseteq E(F)\) be a common basis of order
\(C=\operatorname{Cat}_{n+1}\), supplied automatically for \(n\ge4\).
Write

\[
 R=N-C,\qquad Z=F-Q.
 \tag{1.2}
\]

For \(q=t_qh_q\in Q\), let

\[
 a(q)=[t_q]_Z,\qquad b(q)=[h_q]_Z
 \tag{1.3}
\]

be the components of the punctured central forest containing its tail and
head.

### Lemma 1.1 (punctured child quotient)

The maps \(a,b:Q\to\operatorname{comp}(Z)\) are injective. The graph with
vertices \(\operatorname{comp}(Z)\) and edges

\[
 a(q)b(q),\qquad q\in Q,
 \tag{1.4}
\]

is a disjoint union of \(K\) paths.

### Proof

On one oriented child path, list the removed edges in path order as
\(q_1,\ldots,q_s\). Deleting them cuts that path into components
\(Z_0,\ldots,Z_s\), with

\[
 a(q_i)=Z_{i-1},\qquad b(q_i)=Z_i.
 \tag{1.5}
\]

This proves injectivity on each path, and different child paths are
disjoint. Restoring the removed edges gives the quotient path
\(Z_0-\cdots-Z_s\). \(\square\)

The inherited seam anchors are

\[
 B^-=\{U_q=t_q\cup h_q:q\in Q\},\qquad
 B^+=\{L_q=t_q\cap h_q:q\in Q\}.
 \tag{1.6}
\]

Let \(G^-\) be a punctured side forest on the rank-\(n+1\) bank, and
\(G^+\) its rank-\(n-1\) dual. The exact side degree rows are

\[
 \Delta(G^\pm)\le2,\qquad d_{G^\pm}(x)\le1\quad(x\in B^\pm).
 \tag{1.7}
\]

For a side, let \(c_j^\pm\) count components containing exactly \(j\)
anchors.

## 2. Charge and unavoidable double-anchor components

### Lemma 2.1 (anchor cap two is automatic)

Under (1.7), every component of either side forest contains at most two
anchors.

### Proof

Every component is a path or an isolate. A nontrivial path has exactly two
vertices of degree at most one, and every anchor must be one of them. An
isolated component contains one vertex. \(\square\)

### Proposition 2.2 (Catalan charge)

Every side forest has \(N\) vertices, \(P\) edges, \(N-P\) components and
\(C\) anchors. Therefore

\[
 \sum_{j\ge0}(j-1)c_j^\pm=C-(N-P)=K.
 \tag{2.1}
\]

Under anchor cap two this becomes (0.1).

### Proof

Sum \(j-1\) over all side components. The sum of the \(j\)'s is \(C\), and
the number of summands is \(N-P\). The binomial identity
\(C-(N-P)=M-N=K\) gives (2.1). \(\square\)

Thus at least \(K\) components on each shore contain two anchors. An
anchor-free component costs one additional double-anchor component. This
is a signed global charge, not a canonical assignment of one double
component to each child path; the \(n=3,4\) fixtures explicitly violate
that stronger assignment.

## 3. Star contraction

For a minus component \(D\), let

\[
 Q(D)=\{q\in Q:U_q\in D\}.
 \tag{3.1}
\]

In \(\Gamma_Q\), the contracted vertex \(D\) is adjacent to
\(\{a(q):q\in Q(D)\}\). Define plus blocks dually with \(L_q\) and \(b(q)\).
Lemma 1.1 makes the neighbors within each block distinct.

For each nonempty minus block, choose one root \(q_0\in Q(D)\) and replace
its star by the edges

\[
 a(q_0)a(q),\qquad q\in Q(D)-\{q_0\}.
 \tag{3.2}
\]

Do the same on the plus shore using \(b\). Let \(H_Q\) be the resulting
graph on the central components.

### Theorem 3.1 (star-contraction identity)

\[
 \boxed{\beta(\Gamma_Q)=\beta(H_Q).}
 \tag{3.3}
\]

In particular, \(\Gamma_Q\) is a forest if and only if \(H_Q\) is a forest.
The statement is independent of the spanning tree selected inside each
anchor block.

### Proof

A side block with \(j\) distinct central neighbors is a star with one new
vertex and \(j\) edges. Replacing it by a tree on its \(j\) neighbors
removes one vertex and one edge, preserves the connected partition of all
other vertices, and hence preserves

\[
 \beta=|E|-|V|+\#\operatorname{components}.
 \tag{3.4}
\]

Apply this independently to every nonempty side block. Empty side
components are isolated vertices of \(\Gamma_Q\) and contribute no cycle.
\(\square\)

### Corollary 3.2 (two shore matchings)

Under the exact side degree rows (1.7):

1. the minus links in \(H_Q\) form a matching;
2. the plus links form a matching;
3. \(\Delta(H_Q)\le2\); and
4. every cycle in \(H_Q\) is an even cycle alternating between the two
   shores.

Moreover,

\[
 |E(H_Q)|=c_2^-+c_2^+=2K+c_0^-+c_0^+.
 \tag{3.5}
\]

### Proof

Each anchor belongs to one side component, and \(a\) and \(b\) are
injective. Hence no center component is used twice by one shore matching.
A center component can be used once by each shore, proving maximum degree
two and alternation. Formula (3.5) is (0.1) on both shores. \(\square\)

This is the smallest exact topology state: the side forests matter to
\(\Gamma_Q\) only through two partial matchings on the components of
\(F-Q\).

### Corollary 3.3 (global edge budget; redundant under the shore rows)

If \(\Gamma_Q\) is a forest, then

\[
 c_0^-+c_0^+\le C-K-1=N-P-1.
 \tag{3.6}
\]

### Proof

The punctured center \(F-Q\) has \(K+C\) components. A forest on these
vertices has at most \(K+C-1\) links. Combine this with (3.5):

\[
 2K+c_0^-+c_0^+\le K+C-1.
\]

Rearrangement and \(C-K=N-P\) give (3.6). \(\square\)

The inequality is valid, but it is not an additional topology obstruction
once both shore histograms are valid. Indeed

\[
 c_1^\pm=C-2c_2^\pm=C-2K-2c_0^\pm\ge0
\]

already gives

\[
 c_0^-+c_0^+\le C-2K\le C-K-1
\]

for \(K\ge1\). The genuine remaining topology row is the absence of an
alternating cycle, not this scalar edge count.

### Corollary 3.4 (partial-involution form)

Let \(\mu_-,\mu_+\) be the fixed-point-free partial involutions on
\(\operatorname{comp}(F-Q)\) defined by the minus and plus link matchings.
Then

\[
 \Gamma_Q\text{ is a forest}
 \quad\Longleftrightarrow\quad
 \mu_+\mu_-\text{ has no periodic orbit on its iterated domain}.
 \tag{3.7}
\]

### Proof

An alternating \(2r\)-cycle in the union of the two matchings becomes an
\(r\)-periodic orbit after taking one minus and one plus step. Conversely
every such periodic orbit expands to an alternating cycle. A parallel
minus/plus pair is the case \(r=1\). Apply Theorem 3.1. \(\square\)

This gives a compact symbolic boundary state: two partial involutions and
the absence of a closed alternating orbit.

### Corollary 3.5 (component ledger)

If \(\Gamma_Q\) is a forest, then it has exactly \(N-P\) components. After
adjoining the \(K\) reserved child paths, the ambient forest has

\[
 (N-P)+K=C=\operatorname{Cat}_{n+1}
 \tag{3.8}
\]

components, as required.

### Proof

The graph \(H_Q\) has \(K+C\) center vertices and
\(2K+c_0^-+c_0^+\) edges. If it is a forest, it has

\[
 C-K-c_0^--c_0^+
\]

components. The \(c_0^-+c_0^+\) anchor-free side components are isolated
vertices of \(\Gamma_Q\), so Theorem 3.1 gives \(C-K=N-P\) components in
total. Adding the disjoint child trace and using \(N-P+K=C\) proves (3.8).
\(\square\)

## 4. A solver-free inductive sufficient condition

### Theorem 4.1 (union-find construction)

Suppose anchor-capped side forests are constructed component by component.
Whenever a double-anchor component is completed, add its induced link to
the current graph \(H\). If its two center endpoints are in different
current components, then after all side components are installed,
\(\Gamma_Q\) is a forest.

Equivalently, it is sufficient that the double-anchor links admit a reverse
ordering in which every link has an endpoint of degree at most one among
the links not yet removed.

### Proof

Adding an edge between different components of a forest preserves
acyclicity. Induction proves that the final \(H\) is a forest, and Theorem
3.1 transfers this to \(\Gamma_Q\). The reverse formulation is ordinary
leaf peeling of a forest. \(\square\)

### Corollary 4.2 (tree composition law)

Consider disjoint recursively supplied side states, each carrying:

1. its two shore matchings on punctured-center components;
2. its signed charges \(c_2^\pm-c_0^\pm\); and
3. its current union-find partition.

Gluing the states by any list of new double-anchor links which join
different current components preserves \(\Gamma\)-acyclicity. Charges add,
and the target closes exactly when each shore has total charge \(K\).

Thus an induction need not preserve literal child-path ownership of the
double components. It need preserve only charge and forest-safe attachment
of their two center endpoints.

### Corollary 4.3 (product/SCD sufficient certificate)

Let the guaranteed \(Q\) be fixed. Suppose there are two SCDs of
\(B_{2n}\) whose deep rank-\(n\) banks are respectively

\[
 D^-=\binom{[2n]}n-\{t_q:q\in Q\},\qquad
 D^+=\binom{[2n]}n-\{h_q:q\in Q\}.
 \tag{4.1}
\]

Use the rank \(n\to n+2\) two-step turns of the first SCD and the dual
rank \(n-2\to n\) turns of the second. If these two turn graphs satisfy
(1.7), have anchor cap two, and their induced links obey Theorem 4.1, then
the five-sector construction is a Catalan path forest at parameter
\(n+1\).

### Proof

The SCD turns give the two saturating diagonal incidence matchings. Their
hypotheses give the side degree rows. Port inheritance handles the central
trace, Theorem 4.1 handles \(\Gamma_Q\), and the exact two-coordinate
reduction then gives the ambient path forest. \(\square\)

Corollary 4.3 is a genuine product/SCD sufficient condition. It does not
assert that every transversal basis \(D^\pm\) is the deep bank of an SCD.

## 5. A local obstruction to the naive zipper

### Proposition 5.1 (direct consecutive caps are punctured out)

Let

\[
 q=x_{i-1}x_i,\qquad r=x_ix_{i+1}
 \tag{5.1}
\]

be consecutive oriented child edges, both in \(Q\). Their minus anchors and
plus anchors satisfy

\[
 U_q\cap U_r=x_i,\qquad L_q\cup L_r=x_i.
 \tag{5.2}
\]

The direct Johnson edge \(U_qU_r\) is unavailable in \(G^-\), and the
direct edge \(L_qL_r\) is unavailable in \(G^+\).

### Proof

The child forest has distinct upper and lower edge colours. Thus the
coordinate removed by \(q\) is not the coordinate added by \(r\), and the
coordinate added by \(q\) is not the coordinate removed by \(r\); otherwise
the consecutive edges would repeat an upper or lower colour. This proves
(5.2).

The lower label of \(U_qU_r\) is \(x_i=t_r\). Since \(r\in Q\), this set is
deleted from

\[
 D^-=\binom{[2n]}n-\{t_s:s\in Q\}.
 \]

The upper label of \(L_qL_r\) is \(x_i=h_q\), deleted from \(D^+\).
Therefore neither edge belongs to its punctured diagonal incidence
catalogue. \(\square\)

Consequently the appealing construction which pairs consecutive moved
edges by one direct side edge is false before topology is considered. A
same-path local actuator must use at least one nonanchor internal side
vertex, or the side component must pair nonconsecutive/cross-path anchors.
Both behaviors occur in the exact fixtures.

## 6. A solver-free obstruction template

For the minus shore, form the allowed graph \({\cal J}^-\) on rank-\(n+1\)
sets whose Johnson edge \(XY\) is retained exactly when

\[
 X\cap Y\in D^-.
 \tag{6.1}
\]

Define the anchor compatibility graph \({\cal K}^-\) on \(B^-\): two
anchors are adjacent when \({\cal J}^-\) has a path between them whose
internal vertices contain no anchor. Define \({\cal K}^+\) dually, using
\(X\cup Y\in D^+\).

### Proposition 6.1 (Tutte matching obstruction)

Any anchor-capped side-forest solution satisfies

\[
 \nu({\cal K}^-)\ge K,\qquad \nu({\cal K}^+)\ge K.
 \tag{6.2}
\]

### Proof

Each double-anchor side component contains a path between its two anchors
with no third anchor internally, and distinct double components use
disjoint anchors. Thus the double components give a matching of order
\(c_2^\pm\) in \({\cal K}^\pm\). Proposition 2.2 gives
\(c_2^\pm=K+c_0^\pm\ge K\). \(\square\)

Failure of either inequality, certifiable by Tutte's theorem, is therefore
a solver-free physical no-go. Passing it is not sufficient because it
ignores outer-label uniqueness and the alternating-cycle condition.

## 7. Exact \(n=3,4\) replay

The independent audit

    scratch/audit_h2_catalan_sideforest_anchor_pairing_contraction_20260731.py

reconstructs the two frozen integral collars and verifies the contraction
without importing their materializer.

At \(n=3\):

\[
\begin{array}{c|cc}
&c_0&c_2\\ \hline
-&0&5\\
+&0&5
\end{array}
\qquad |E(H)|=10,\quad
 |V(H)|=K+C=19,\quad |\operatorname{supp}V(H)|=14.
\tag{7.1}
\]

At \(n=4\):

\[
\begin{array}{c|cc}
&c_0&c_2\\ \hline
-&0&14\\
+&1&15
\end{array}
\qquad |E(H)|=29,\quad
 |V(H)|=K+C=56,\quad |\operatorname{supp}V(H)|=39.
\tag{7.2}
\]

In both cases \(H\) has maximum degree two, no alternating cycle, and a
literal complete leaf-peeling order. The audit also checks (5.2) for every
consecutive moved pair. Although the selected \(Q\)'s have enough
combinatorial adjacent-pair capacity (\(6\ge5\) and \(14=14\)), those
direct pairs are physically punctured out, explaining why the successful
fixture components are nonlocal.

## 8. Exact remaining theorem

The common basis is automatic. A sufficient all-\(n\) physical theorem is:

> choose a guaranteed common basis \(Q\), realize its two diagonal
> complements by anchor-capped side forests, and install their
> double-anchor links in the union-find-safe
> order of Theorem 4.1.

The unresolved existence is the simultaneous realization of the two
label-saturating side forests with that link state. No claim is made that
an arbitrary common basis, an arbitrary SCD, or every child Catalan forest
has such a realization.
