# K17 static recoupling as two-matroid common basis and weighted Hall oracle

**Date:** 2026-08-02  
**Status:** proof-complete for the compressed three-level static table.  A
literal K17 common-basis witness is audited on both raw warm47 and the
12-C6 materialization.  Occurrence sockets and all chronological layers are
outside the common-basis claim.

## 1. Correct ground sets and transversal wording

Put

\[
 L=\bigcup_{j=1}^{6}{[17]\choose j},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Then

\[
 |L|=21777,\qquad |M|=19448,\qquad |R|=24310.
\]

Let \(M_7\) be the transversal matroid on ground set \(R\), presented by
the containment graph from \(M\) to \(R\).  Thus a set \(I\subseteq R\)
is independent when a matching saturates the selected ground elements
\(I\) into distinct rank-seven witnesses.  At basis cardinality 19448 this
is equivalently a matching of all of \(M\) into the basis.  The literal
phrase “all rank-seven targets match into \(I\)” is not the definition for
arbitrary independent sets because it is not hereditary.

The incidence graph is \((10,8)\)-biregular.  For \(X\subseteq M\),

\[
 10|X|\le 8|N(X)|,
\]

so Hall's theorem matches all of \(M\) into \(R\).  Hence

\[
 r(M_7)=19448,\qquad r(M_7^*)=24310-19448=4862.
\]

Let \(M_L\) be the transversal matroid on
\(E=M\mathbin{\dot\cup}R\), presented by containment from \(L\) into
\(E\).  Again, independence means that the selected receiver set is
saturated by distinct low targets.  Saturation of all \(L\) follows only at
basis size.  Its rank is 21777; the literal table audit below supplies a
matching of this size, and no transversal presentation on left shore
\(L\) can have larger rank.

Finally put

\[
 N=M_7^*\oplus U_{16915,M}.
\]

Both \(M_L\) and \(N\) have rank 21777.

## 2. Load-bearing normal form

Here a *no-singleton compressed three-level table* means a partition into
chains of exactly the following forms:

\[
 \ell\subset m\subset r,\qquad
 \ell\subset r,\qquad
 m\subset r,
 \tag{2.1}
\]

with \(\ell\in L,m\in M,r\in R\).  In particular no chain contains two
comparable members of \(L\).

The histogram alone does not imply (2.1).  If a generic Boolean-chain table
has respectively \(a,b,c,d\) chains of types
`L-L-R`, `L-M-R`, `L-R`, `M-R`, the target counts and the histogram permit

\[
 (a,b,c,d)=(a,16915-a,4862-a,2533+a),
 \qquad0\le a\le4862.
\]

Thus the common-basis theorem is exact for (2.1), not for an unqualified
length histogram.

## 3. Exact common-basis equivalence

### Theorem 3.1

There exists an exact compressed table (2.1) with length histogram
\((0,7395,16915)\) if and only if \(M_L\) and \(N\) have a common basis.
More precisely, tables correspond to triples

\[
 (C,\mu_L,\mu_7),
\]

where \(C\) is a common basis, \(\mu_L\) is a perfect representing
matching between \(L\) and \(C\), and \(\mu_7\) is a perfect representing
matching between \(M\) and \(R-C_R\).  Forgetting the matchings is generally
many-to-one, so tables are not in bijection with common-basis element sets
alone.

#### Proof

Write \(C_M=C\cap M\) and \(C_R=C\cap R\).  Since \(C\) is a basis of the
direct sum \(N\),

\[
 |C_M|=16915,\qquad |C_R|=4862,
\]

and \(C_R\) is a basis of \(M_7^*\).  Therefore
\(B=R-C_R\) is a basis of \(M_7\), so \(\mu_7\) matches every member of
\(M\) to a distinct member of \(B\).  Since \(C\) is an \(M_L\) basis,
\(\mu_L\) matches every member of \(L\) to a distinct receiver in \(C\).

If \(\mu_L(\ell)=m\in C_M\), form
\(\ell\subset m\subset\mu_7(m)\).  If
\(m\in M-C_M\), form \(m\subset\mu_7(m)\).  If
\(\mu_L(\ell)=r\in C_R\), form \(\ell\subset r\).  These chains partition
all three levels.  Their counts are

\[
 16915,\qquad |M-C_M|+|C_R|=2533+4862=7395.
\]

Conversely, from a table (2.1), let \(C_M\) be its rank-seven middles with
low predecessors and let \(C_R\) be its roots with direct low predecessors.
The table edges give a perfect matching \(L\to C_M\dot\cup C_R\), and the
rank-seven-to-root edges give a perfect matching
\(M\to R-C_R\).  Hence \(C=C_M\dot\cup C_R\) is a basis of both
\(M_L\) and \(N\).  \(\square\)

Fixed rank-nine owners may be carried on the rank-eight roots throughout;
the theorem neither chooses nor changes them.

## 4. Exact Hall/Benders master

Let \(x_e=1\) mean \(e\in C\).  For a low-target shore \(A\subseteq L\)
and a rank-seven shore \(Q\subseteq M\), write \(\Gamma_L(A)\subseteq E\)
and \(\Gamma_7(Q)\subseteq R\) for their containment neighborhoods.  The
following binary system is exactly the common-basis master:

\[
\begin{aligned}
 \sum_{m\in M}x_m&=16915,\\
 \sum_{r\in R}x_r&=4862,\\
 \sum_{e\in\Gamma_L(A)}x_e&\ge |A| &&(A\subseteq L),\\
 \sum_{r\in\Gamma_7(Q)}(1-x_r)&\ge |Q| &&(Q\subseteq M),\\
 x&\in\{0,1\}^{E}.
\end{aligned}
\tag{4.1}
\]

The first Hall family matches \(L\) into the selected receivers \(C\); the
second matches \(M\) into the unselected roots \(B=R-C_R\).  Each family
has exact polynomial separation.  Give receiver nodes capacity \(x_e\) in
the low network and capacity \(1-x_r\) in the rank-seven network.  A
maximum flow below the required left-shore size returns an alternating
reachable shore and precisely the violated row in (4.1).  Normalize a cut
by its sorted receiver-neighborhood coefficient vector and right-hand side
before deduplication.

Equivalently, use the two matching-based independence oracles in Edmonds'
matroid-intersection algorithm.  For \(A\subseteq R\), the dual oracle is

\[
 r_{M_7^*}(A)=|A|-19448+r_{M_7}(R-A),
\]

so \(A\) is independent in \(M_7^*\) exactly when a maximum matching into
\(R-A\) has rank 19448.  The uniform summand only adds the test
\(|C_M|\le16915\).

Edmonds' min--max theorem gives

\[
 \max\{|I|:I\in\mathcal I(M_L)\cap\mathcal I(N)\}
 =\min_{X\subseteq E}\bigl(r_{M_L}(X)+r_N(E-X)\bigr).
\tag{4.2}
\]

A common basis exists exactly when the right side of (4.2) is at least
21777.

## 5. Weighted global optimization

For any element weight \(w:E\to\mathbb Z\), weighted matroid intersection
finds an exact minimum- or maximum-weight common basis in polynomial time.
The practical exchange graph uses fundamental circuits from the two
matching presentations; a negative reduced-cost alternating circuit is a
valid common-basis exchange, and the weighted algorithm continues until it
has a global optimum rather than a local C6 optimum.

This directly supports linear prices such as receiver reservation,
protected-host penalties, or a precomputed per-element socket score.  If a
cost belongs to the actual representing edge rather than to the selected
receiver, retain matching variables
\(y_{\ell e}\) and \(z_{mr}\) and price those edges explicitly.  The static
containment layer remains a bipartite-flow layer.

Occurrence socket compatibility is not, in general, an element weight or a
second matroid: tickets can share endpoint hosts, tokens, flags, or state
choices.  It must be handled by an occurrence-labelled subproblem and
proof-safe Benders cores, or by a separately proved private/Rado matroid
face.  Adding an arbitrary third matroid would not preserve the polynomial
two-matroid theorem.

## 6. Literal K17 audit and the C6 interface

The H100 package

```text
/home/amodo/or15/work/r2_k17_static_common_basis_20260802
```

independently decodes the raw-warm47 table and the materialized maximum
12-C6 table.  Both have:

```text
target deck                    65535/65535
length histogram               0,7395,16915
rank-seven matching            19448/19448
low matching                   21777/21777
|C_R|,|C_M|                    4862,16915
```

The two common-basis element sets differ by exactly 12 old and 12 new
members of \(M\), and by no member of \(R\).  Thus the row-disjoint C6
packet is literally a 12-element exchange in the uniform \(M\) summand
while retaining the same dual root basis.  Both endpoints remain common
bases.  Twelve shared \(M\) elements nevertheless change their representing
physical row and matched-low witness, so the element-set symmetric
difference does not encode the whole table rethread.  In particular it does
not make the selected socket occurrences compatible.

Load-bearing hashes are:

```text
auditor source                 aeb4a82486b35074ff65ae6e276bd3a0da0cca89b55abf2f79b40fab2dbc1658
raw-warm47 common basis        6a3bffc365ac35ee2cb601b071c878b09e8507c10ccee975a3af7e85627d7d53
12-C6 common basis             83cad2f17ebad3ff7abe07fd73bc0390e207c1bc1af961640f52ca5158f63656
basis symmetric difference    02046ae962ab321c5a1804cc03a7cc320b81bb774aacb898a2f3772e7aebfb64
package manifest               2b1e0019e3999d85e2b7f4f02e7d536bdc7fe455d15ada22b16444ecef354429
manifest replay                aece60c7e6796a8d46789a6a3e4d5f38d751a42ad57e4ac5a39eaa67b5f12f7e
```

## 7. Exact scope

The theorem closes global **static rank-graded recoupling** as weighted
two-matroid intersection and supplies exact matching/min-cut oracles.  It
does not close occurrence sockets, a common phase/state assignment,
topology, chronology, residence, deeper upper decks, source, opening,
compiler, or a word.
