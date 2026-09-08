# Exact functional-attachment menus and the zero-margin random-\(\vartheta\) barrier

**Date:** 2026-08-06

**Method:** literal rail-shift algebra, Hall's theorem, and a Birkhoff
distribution on middle-level incidence bijections; no computation, search,
or solver

**Status:** unconditional exact characterization for a fixed resident
all-high flag table. It identifies every functional predecessor surviving
the literal age shift and gives the exact Hall system for an attachment
\(\vartheta\). It also proves that a random incidence bijection has expected
surviving degree at most one, so random attachment has no expansion margin.
The result does not construct the required exact mixed-length flag table.

## 1. Fixed flags and literal turns

Work on

\[
                         n=2m+1
\]

coordinates. Let

\[
                         {\cal Q}={[n]\choose m}.
\]

Fix \(d\ge2\). A flag table chooses at every root \(q\in{\cal Q}\) an
ordered deletion rail

\[
 {\bf z}(q)=(z_1(q),\ldots,z_{d-1}(q)),
 \qquad z_i(q)\in q
                                                               \tag{1.1}
\]

with distinct entries, and bottom

\[
 B(q)=q\setminus\{z_1(q),\ldots,z_{d-1}(q)\}.        \tag{1.2}
\]

A literal turn from a tail \(p\) to a head \(q\) has the form

\[
 q=p-\{z_1(p)\}+\{\beta\},
 \qquad \beta\notin p,                              \tag{1.3}
\]

and is legal exactly when

\[
 (z_1(q),\ldots,z_{d-1}(q))
 =
 (z_2(p),\ldots,z_{d-1}(p),\gamma)
                                                               \tag{1.4}
\]

for some \(\gamma\in B(p)\). Its owner is

\[
                         o=p\cup\{\beta\}
                          =q\cup\{z_1(p)\}.          \tag{1.5}
\]

These are the literal shift laws from the SCD flag chronology theorem.
The lower marks may use a mixed set of suffix widths; the transition rail
itself is still (1.1) whenever the central roots form a simple resident
Johnson chronology.

## 2. The exact incoming attachment menu

Let

\[
 \vartheta:{\cal Q}\longrightarrow {[n]\choose {m+1}},
 \qquad q\subset\vartheta(q),                       \tag{2.1}
\]

be an incidence bijection, and put

\[
                         \alpha_\vartheta(q)
 =\vartheta(q)\setminus q.                          \tag{2.2}
\]

For \(q\in{\cal Q}\) and \(\alpha\notin q\), define

\[
 \boxed{
 {\cal P}_F(q,\alpha)
 =
 \left\{
 q-\{\beta\}+\{\alpha\}:
 \begin{array}{l}
 \beta\in B(q),\\[1mm]
 {\bf z}(q-\beta+\alpha)
   =(\alpha,z_1(q),\ldots,z_{d-2}(q))
 \end{array}
 \right\}.}
                                                               \tag{2.3}
\]

### Theorem 2.1 (exact surviving-predecessor formula)

The predecessors of \(q\) in the functional flag-compatible graph
\(B_\vartheta(F)\) are exactly

\[
                         {\cal P}_F
 \bigl(q,\alpha_\vartheta(q)\bigr).                \tag{2.4}
\]

Equivalently, among the \(m\) unflagged functional predecessors of \(q\),
the survivor indexed by \(\beta\) exists precisely when the two conditions
inside (2.3) hold.

#### Proof

Suppose \(p\to q\) is a legal turn using owner \(\vartheta(q)\). From
(1.5),

\[
                         z_1(p)=\alpha_\vartheta(q).           \tag{2.5}
\]

Write \(q=p-z_1(p)+\beta\). Then

\[
                         p=q-\beta+\alpha_\vartheta(q).       \tag{2.6}
\]

The rail shift (1.4) forces

\[
 {\bf z}(p)
 =
 \bigl(\alpha_\vartheta(q),
       z_1(q),\ldots,z_{d-2}(q)\bigr).              \tag{2.7}
\]

Every entry on the right of (2.7) must belong to \(p\), while
\(z_{d-1}(q)\) must lie in \(B(p)\). Hence \(\beta\) can equal none of
\(z_1(q),\ldots,z_{d-1}(q)\), which is exactly

\[
                         \beta\in B(q).                       \tag{2.8}
\]

This proves necessity.

Conversely, let \(\beta\in B(q)\) satisfy (2.3), and put
\(p=q-\beta+\alpha\). Equation (2.3) gives the required shifted rail.
Because \(\beta\) lies in \(B(q)\), the final head label
\(z_{d-1}(q)\) remains in \(p\), is not a tail-rail entry, and therefore
lies in \(B(p)\). Equations (1.3)--(1.5) now give a legal turn with owner
\(q+\alpha=\vartheta(q)\). \(\square\)

### Corollary 2.2 (exact outgoing formula)

Let \(p\) have rail

\[
                         (u_1,\ldots,u_{d-1}).
\]

Its functional successors are exactly the roots

\[
                         q=p-\{u_1\}+\{\beta\},
 \qquad \beta\notin p,                              \tag{2.9}
\]

for which

\[
 \alpha_\vartheta(q)=u_1
                                                               \tag{2.10}
\]

and

\[
 {\bf z}(q)=(u_2,\ldots,u_{d-1},\gamma)
 \quad\text{for some }\gamma\in B(p).              \tag{2.11}
\]

## 3. Exact Hall/Rado form

### Theorem 3.1 (functional attachment criterion)

For a fixed flag table \(F\) and incidence bijection \(\vartheta\), an
owner-exact literal cycle cover exists if and only if

\[
 \boxed{
 \left|
 \bigcup_{q\in X}
 {\cal P}_F\bigl(q,\alpha_\vartheta(q)\bigr)
 \right|
 \ge |X|
 \qquad\text{for every }X\subseteq{\cal Q}.
 }                                                          \tag{3.1}
\]

#### Proof

By Theorem 2.1, the displayed union is exactly the predecessor
neighbourhood of \(X\) in \(B_\vartheta(F)\). Thus (3.1) is Hall's
condition. A perfect matching uses every head once and hence, through the
bijection \(\vartheta\), every owner once. Conversely every functional
owner-exact cycle cover is such a perfect matching. \(\square\)

The condition is exact rather than a new relaxation. Its value is that
all literal restrictions are compressed into the explicit local menus
(2.3); there is no separate hidden owner row after \(\vartheta\) is fixed.

## 4. A marginally uniform distribution on attachments

The middle inclusion graph between \({\cal Q}\) and
\(\binom{[n]}{m+1}\) is \((m+1)\)-regular. Giving every incidence edge
weight \(1/(m+1)\) is therefore a fractional perfect matching. By
bipartite integrality it is a convex combination of incidence bijections.
Hence there is a probability distribution on \(\vartheta\)'s satisfying

\[
 \Pr\{\alpha_\vartheta(q)=\alpha\}
 ={1\over m+1}
 \qquad(q\in{\cal Q},\ \alpha\notin q).             \tag{4.1}
\]

No independence between different heads is asserted or needed.

### Theorem 4.1 (exact random-attachment expectation)

Under any distribution with marginals (4.1),

\[
 \boxed{
 \mathbb E\,d^-_{B_\vartheta(F)}(q)
 =
 {1\over m+1}
 \sum_{\alpha\notin q}|{\cal P}_F(q,\alpha)|
 }                                                          \tag{4.2}
\]

for every head \(q\), and

\[
 \boxed{
 \mathbb E\,|E(B_\vartheta(F))|
 ={|\mathcal T(F)|\over m+1},
 }                                                          \tag{4.3}
\]

where \(\mathcal T(F)\) is the complete literal turn catalogue of the
fixed flag table.

#### Proof

Equation (4.2) follows by conditioning on
\(\alpha_\vartheta(q)\) and applying Theorem 2.1. Summing over \(q\)
gives (4.3), because every literal turn has one head-owner incidence and
is retained exactly when \(\vartheta\) chooses that incidence. \(\square\)

## 5. Random \(\vartheta\) has no expansion margin

### Theorem 5.1 (zero-margin expectation barrier)

For every fixed flag table,

\[
                         |\mathcal T(F)|\le(m+1)W,             \tag{5.1}
\]

and consequently

\[
 \boxed{
 \mathbb E\,|E(B_\vartheta(F))|\le W,
 \qquad
 \mathbb E\,\overline d(B_\vartheta(F))\le1.
 }                                                          \tag{5.2}
\]

Equality in (5.1) holds only when every tail flag has a legal successor
for every one of its \(m+1\) possible inserted coordinates.

#### Proof

Fix a tail root \(p\). Its first rail coordinate \(z_1(p)\) is fixed.
Every literal successor is determined by choosing the inserted coordinate

\[
                         \beta\in[n]\setminus p,               \tag{5.3}
\]

of which there are \(m+1\). Once \(\beta\) is chosen, the successor root
\(q=p-z_1(p)+\beta\) and its owner \(p+\beta\) are fixed; the selected
head flag either satisfies (1.4) or it does not. Thus the complete turn
catalogue has tail degree at most \(m+1\), proving (5.1).

Substitute (5.1) into (4.3). The average degree is the edge count divided
by the \(W\) heads, giving (5.2). The equality statement follows from the
tailwise count. \(\square\)

Every perfect matching in \(B_\vartheta(F)\) already uses \(W\) edges.
Therefore the random-attachment mean is at or below the bare feasibility
threshold, never above it. In particular:

* no Chernoff, expansion, or high-average-degree argument for random
  \(\vartheta\) can prove (3.1);
* a successful \(\vartheta\) must exploit correlation with the flag table,
  not merely uniform incidence marginals; and
* relative to the complete unflagged \(m\)-regular functional graph, a
  random attachment/flag combination deletes on average at least

  \[
                         (m-1)W                              \tag{5.4}
  \]

  functional incidences.

Thus the sharp \(<m\)-edge resilience theorem for an already complete
functional core is useful only after a correlated flag-compatible core has
been built. Random attachment is not a route to that core.

## 6. The remaining integral theorem

The clean functional route is now exactly:

1. construct a genuinely mixed-length, named-target-exact flag table
   \(F\);
2. choose \(\vartheta\) **correlated with \(F\)** so that the explicit
   menus (2.3) satisfy (3.1);
3. use bipartite integrality to obtain the owner-once cycle cover; and
4. fuse its cycles while preserving the PBBS, residence, and upper guards.

The maximal-width rotor cannot supply item 1 after bounded repair, by the
linear mixed-length necessity theorem. Equations (2.3) and (3.1) are the
exact local and global tests for item 2. The random-\(\vartheta\) calculation
shows that item 2 has zero probabilistic degree slack and must be designed,
not sampled independently.

## 7. Scope

This theorem does not prove the existence of \(F\) or \(\vartheta\).
It also does not prove connectedness, quotient voltage, residence,
arbitrary-width upper coverage, or an all-dimensional word bound.

Its exact contribution is to replace the vague phrase “choose a good
functional attachment” by the literal predecessor menus (2.3), the exact
Hall system (3.1), and a proof that independent random attachment has no
expansion margin.
