# Translation-invariant long cycle covers from quotient edge-colouring

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let \(p=2m+1\) be prime, let \(\rho:x\mapsto x+1\) act on
\(\mathbb F_p\), and let

\[
                 V=\binom{\mathbb F_p}{m},\qquad
                 \overline V=V/\langle\rho\rangle,\qquad
                 T=|\overline V|={1\over p}\binom pm .
\]

The action on \(V\) is free.  Start with any oriented cycle factor
\(F\) of the odd graph \(O_m=KG(p,m)\); for example, one may orient the
MSW shortest-cycle factor.  Project all its directed arcs to the two
necklace shores.  The result is a \(p\)-regular bipartite multigraph.
Consequently it decomposes into \(p\) perfect matchings.

Every one of those perfect matchings lifts, by translating each selected
arc through all \(p\) phases, to a \(\rho\)-invariant exact directed
owner permutation supported on odd-graph arcs.  It is a simple
odd-graph cycle factor provided the matching never selects the two
orientations of one undirected voltage orbit as a directed two-cycle.

Thus:

\[
\boxed{\text{a translation-invariant exact directed odd-edge owner
permutation always exists.}}
\]

This bypasses the Catalan congruence obstruction for invariant factors
whose cycles are required to have the shortest length \(p\).  It does
not by itself prove the constant-one theorem.  The lifted cycles need
not be shortest wreaths, need not be locally return-free, may have too
many components, and need not cover the lower shadow necklaces.  Those
three remaining requirements are stated exactly below.

## 1. The projected arc multigraph

Orient every component of \(F\), and write its successor as

\[
                 s:V\longrightarrow V,\qquad A\cap s(A)=\varnothing .
\tag{1.1}
\]

Form a bipartite multigraph \(B_F\) with a left and a right copy of
\(\overline V\).  For every physical owner \(A\in V\), insert one
tagged edge

\[
                 e_A:[A]_{\rm L}\longrightarrow[s(A)]_{\rm R}.
\tag{1.2}
\]

Parallel edges retain their physical tags.

### Theorem 1.1 (exact quotient regularity)

\(B_F\) is \(p\)-regular on both shores.

#### Proof

A necklace contains exactly \(p\) physical owners.  Every physical owner
is the tail of exactly one arc of \(F\), so every left necklace has
degree \(p\).  Since \(s\) is a permutation, every physical owner is
also the head of exactly one arc.  Hence every right necklace also has
degree \(p\). \(\square\)

By the integral perfect-matching theorem for regular bipartite
multigraphs,

\[
                 E(B_F)=M_1\mathbin{\dot\cup}\cdots
                         \mathbin{\dot\cup}M_p
\tag{1.3}
\]

for perfect matchings \(M_j\).

## 2. Lifting one quotient matching

Fix one \(M=M_j\).  For each selected tagged edge \(e_A\), include the
full translated arc orbit

\[
                 \mathcal O(e_A)=
 \{\,A+t\longrightarrow s(A)+t:t\in\mathbb F_p\,\}.
\tag{2.1}
\]

The chosen tag matters only as a representative of this orbit.

### Theorem 2.1 (invariant exact directed lift)

The union of the arc orbits in (2.1) is a
\(\rho\)-invariant directed owner permutation \(F_M\) on \(V\).
If it contains no directed two-cycle obtained from the two orientations
of one undirected voltage orbit, its underlying graph is a simple
odd-graph cycle factor.

#### Proof

Let \(X\in V\).  Its necklace occurs once on the left shore of \(M\), so
there is a unique selected edge \(e_A\) with \([A]=[X]\).  Freeness gives
a unique \(t\) with \(X=A+t\), and (2.1) gives exactly one outgoing arc
from \(X\).

The same argument on the right shore gives exactly one incoming arc at
every \(X\).  Translation preserves disjointness, so every selected arc
is an odd-graph edge.  The resulting directed graph has indegree and
outdegree one at every owner and is therefore a cycle factor.

If two selected quotient tags represented the same *directed* translated
arc orbit, they would have the same left and right necklace endpoints.
They are parallel edges of \(B_F\), and a matching cannot contain both.
Thus the physical lift has no repeated directed arc.  A matching may,
however, select an orbit \(O\to P\) and the reverse orbit \(P\to O\);
their lift is a directed backtrack on one undirected edge orbit.  Excluding
exactly those pairs gives the final simplicity assertion.  Equation
(2.1) makes \(\rho\)-invariance immediate. \(\square\)

### Corollary 2.2 (voltage and component count)

The matching \(M\) is a permutation of the \(T\) necklaces.  Let a
quotient cycle have length \(\ell\) and total translation voltage
\(v\in\mathbb F_p\).  Its lift consists of

\[
 \begin{cases}
 p\text{ cycles of length }\ell,&v=0,\\
 1\text{ cycle of length }p\ell,&v\ne0.
 \end{cases}
\tag{2.2}
\]

In particular, if \(c(M)\) is the number of quotient cycles, then

\[
                 c(F_M)\le p\,c(M).
\tag{2.3}
\]

Thus

\[
                 c(M)=o(T/H)
\tag{2.4}
\]

is sufficient for the usual \(o(W/H)\) physical component target.

The proof of (2.2) is the standard voltage lift: one circuit changes the
phase by \(v\); for prime \(p\), a nonzero \(v\) generates all phases.

## 3. Every-second Johnson traversal

Let

\[
 A_i\longrightarrow A_{i+1}\longrightarrow A_{i+2}
\tag{3.1}
\]

be two consecutive arcs of a lifted factor.  Define the omitted label

\[
                 u_i=\mathbb F_p\setminus(A_i\cup A_{i+1}).
\tag{3.2}
\]

Since \(A_i\) and \(A_{i+1}\) are disjoint \(m\)-sets, \(u_i\) is
unique.

### Lemma 3.1 (two-step swap identity)

If \(A_{i+2}\ne A_i\), then

\[
                 A_{i+2}
  =\bigl(A_i\setminus\{u_{i+1}\}\bigr)\cup\{u_i\}.
\tag{3.3}
\]

#### Proof

The complement of \(A_{i+1}\) is \(A_i\cup\{u_i\}\).  Hence
\(A_{i+2}\), an \(m\)-set disjoint from \(A_{i+1}\), is obtained by
deleting one element from \(A_i\cup\{u_i\}\).  The deleted element is
precisely the unique point outside \(A_{i+1}\cup A_{i+2}\), namely
\(u_{i+1}\).  If it were \(u_i\), then \(A_{i+2}=A_i\), contrary to the
hypothesis. \(\square\)

Thus the every-second successor \(J(A_i)=A_{i+2}\) is a Johnson move
away from immediate backtracks.  If the labels

\[
                 u_i,u_{i+1},\ldots,u_{i+2q-1}
\tag{3.4}
\]

are pairwise distinct, then the first \(q\) Johnson moves are
return-free and

\[
\begin{aligned}
 \bigcap_{t=0}^{q}J^t(A_i)
   &=A_i\setminus\{u_{i+1},u_{i+3},\ldots,u_{i+2q-1}\},\\
 \bigcup_{t=0}^{q}J^t(A_i)
   &=A_i\cup\{u_i,u_{i+2},\ldots,u_{i+2q-2}\}.
\end{aligned}
\tag{3.5}
\]

The two sets in (3.5) have ranks \(m-q\) and \(m+q\), respectively.
The first is the desired lower shadow.  The second is only the ordinary
union shadow of the every-second Johnson walk.  On the odd ground set,
the complement of a lower target has rank \(m+1+q\), so (3.5) does
**not** by itself supply the upper target furnished by a shortest
wreath.  Pairwise distinctness is a convenient sufficient condition for
the displayed Johnson geodesic; the exact two-queue residence criterion
is weaker.

## 4. Exact remaining long-cycle gate

For a selected quotient matching \(M\), let \(\mathcal B_H(M)\) be the
number of rooted signed windows through depth \(H\) for which the
every-second walk either backtracks or violates the exact two-queue
residence condition.  Let \(M_q^-(M)\) be the number of lower
rank-\((m-q)\) targets not realized by any valid rooted window.

The long-cycle quotient route would prove coefficient one only after an
additional transfer lemma replacing the shortest-wreath interval
interface.  The exact construction-side conditions to seek are a
matching \(M\) from an appropriate projected catalogue such that

\[
\boxed{
\begin{aligned}
 c(M)&=o(T/H),\\
 \mathcal B_H(M)&=o(W),\\
 \sum_{q\le H}M_q^-(M)&=o(W),
\end{aligned}}
\tag{4.1}
\]

for some \(H/\sqrt m\to\infty\), \(H=o(m)\).  In addition, one must prove
that the long odd-graph cycles can be linearized with \(o(W)\) overhead
while realizing either the complementary rank-\((m+1+q)\) targets or an
equivalent one-sided condition sufficient for the original OR transfer.
Translation invariance alone does not provide that statement.

The first line is a long-cycle condition on the quotient permutation,
the second is a local voltage/omitted-label condition, and the third is
the genuine one-sided necklace-cover condition.  Theorem 2.1 solves
exact invariant ownership without solving any of these three or the
long-cycle transfer interface.

## 5. Audited boundary

Proved here:

1. exact \(p\)-regularity of the projected directed arc multigraph;
2. its decomposition into \(p\) quotient perfect matchings;
3. the translation-invariant exact directed lift of every matching and
   the exact reverse-orbit condition for simplicity;
4. the voltage component formula; and
5. the two-step Johnson swap and literal shadow formulas.

Not proved:

1. a quotient matching satisfying any line of (4.1) for growing \(H\);
2. a simultaneous configuration-Hall theorem for the three lines;
3. that the projected MSW catalogue has sufficient long-cycle or
   local-voltage flexibility;
4. a valid odd long-cycle linearization/complement interface; or
5. coefficient one.

The gain over the shortest-cycle quotient formulation is exact:
translation-invariant ownership no longer requires two AP loops plus
zero-voltage \(p\)-cycles and has no Catalan congruence obstruction.
The price is that chronology, component count, and shadows must now be
controlled on a quotient perfect matching rather than being automatic
inside a shortest wreath.
