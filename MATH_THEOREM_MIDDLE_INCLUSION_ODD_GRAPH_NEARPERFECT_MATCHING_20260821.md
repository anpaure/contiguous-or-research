# A middle-inclusion permutation gives a near-perfect odd-graph matching

## 1. The construction

Let
\[
        b=2r+1,\qquad N=\binom br,
\]
and write \({\cal L}_k=\binom{[b]}k\).  Let
\[
        \phi:{\cal L}_r\longrightarrow{cal L}_{r+1}          \tag{1.1}
\]
be a bijection satisfying \(X\subsetphi(X)\) for every \(X\).  Such a
bijection exists because the consecutive-level inclusion graph is
\((r+1)\)-regular bipartite; alternatively, the middle successors in any
symmetric chain decomposition give one explicitly.

Define
\[
        f(X)=[b]\setminusphi(X).                             \tag{1.2}
\]
Complementation is a bijection from \({\cal L}_{r+1}\) to
\({\cal L}_r\), so \(f\) is a permutation of \({\cal L}_r\).  Moreover
\(X\cap f(X)=\varnothing\).  Thus every arrow \(X\to f(X)\) is an edge
of the odd graph
\[
        G=KG(2r+1,r).                                         \tag{1.3}
\]

On every even cycle of the permutation \(f\), take alternate graph
edges.  On every odd cycle, expose one vertex and take alternate edges
on the remaining path.  Denote the union of the chosen edges by \(P).

**Theorem 1.1 (deterministic near-perfect Kneser matching).**  The set
\(P\) is a matching in \(G\), and
\[
        |V(G)\setminus V(P)|\le {N\over b},
        \qquad
        |P|\ge {N\over2}\left(1-{1\over b}\right).           \tag{1.4}
\]
The construction is explicit once an inclusion matching (1.1), an
origin on each odd \(f\)-cycle, and a parity on each even cycle are
fixed.

This removes the need to start the paired-wreath compression from a
random maximum matching.  It does **not** yet prove that the induced
compressed hypergraph \({\cal J}_r[P]\) has an almost-perfect matching;
that is a separate gate.

## 2. Odd girth of the odd graph

We use the following elementary form of the odd-girth theorem.

**Lemma 2.1.**  Every simple odd cycle in \(KG(2r+1,r)\) has length at
least \(2r+1\).

**Proof.**  Let
\(X_0,X_1,\ldots,X_{2s},X_0\) be an odd cycle.  Since both \(X_i\) and
\(X_{i+2}\) are \(r\)-subsets of the \((r+1)\)-set
\([b]\setminus X_{i+1}\), they differ by at most one exchange:
\[
        |X_i\setminus X_{i+2}|\le1.                           \tag{2.1}
\]
The even-index walk
\(X_0,X_2,\ldots,X_{2s}\) has \(s\) such steps.  But
\(X_{2s}\cap X_0=\varnothing\), so all \(r\) elements of \(X_0\) must
have been removed along it.  Hence \(s\ge r\), and the original cycle
has length \(2s+1\ge2r+1\).  ∎

## 3. Proof of Theorem 1.1

The cycle decomposition of a permutation partitions \({\cal L}_r\).
Every chosen alternate pair is an edge of \(G\) by (1.2), and different
pairs have disjoint endpoints.  Thus \(P\) is a matching.

An even \(f\)-cycle leaves no vertex exposed.  An odd \(f\)-cycle has
length at least \(b\) by Lemma 2.1 and leaves exactly one vertex exposed.
The odd cycles are vertex-disjoint, so their number is at most \(N/b\).
This proves the first inequality in (1.4); the second follows by dividing
the number of covered vertices by two.  ∎

Notice that no randomness or asymptotic matching theorem enters this
argument.  It applies to every middle inclusion matching \(\phi\).

## 4. The canonical Greene--Kleitman instance

For a concrete deterministic choice, encode \(X\) as a binary word,
recursively pair a `1` with the next available `0` to its right, and flip
the rightmost unpaired `0`.  This is the usual middle successor in the
Greene--Kleitman/de Bruijn--Tengbergen--Kruyswijk symmetric chain
decomposition and supplies (1.1).

The exact finite cycle profiles for this choice begin as follows:
\[
\begin{array}{c|c|c|c}
b&N&\text{cycle lengths of }f&\text{exposed vertices}\\ \hline
5&10&5^2&2\\
7&35&7^2,21&3\\
9&126&9^3,27^2,45&6\\
11&462&11^3,33^4,55^4,77&12.
\end{array}                                                    \tag{4.1}
\]
These data are evidence about the later compressed-hypergraph gate, not
inputs to Theorem 1.1.

For the alternating origins used by the finite checker, the induced
paired-wreath hypergraph \({\cal J}_r[P]\) has respectively
\(5,47,472,5064\) hyperedges for \(b=5,7,9,11\).  At \(b=7\), its maximum
matching has five hyperedges and leaves one of the sixteen pair vertices;
at \(b=9\), it has a perfect matching of fifteen hyperedges on all sixty
pair vertices.  At \(b=11\), finite optimization currently gives 43
hyperedges against the upper bound 45.  None of these last finite facts is
promoted here to an asymptotic claim.

## 5. Exact scope in the wreath compiler

Every edge of \(P\) pairs two disjoint middle targets.  If a matching in
\({\cal J}_r[P]\) leaves \(L_P\) pair vertices unused, its selected
punctured wreaths have mutually disjoint clean targets and cover
\[
        2|P|-2L_P                                             \tag{5.1}
\]
middle targets.  By (1.4), their target deficit is at most
\[
        {N\over b}+2L_P.                                      \tag{5.2}
\]
In addition, exactly one source window is discarded per selected wreath,
which is \(O(N/b)\) sources when the pair matching is near-complete.
Therefore \(L_P=o(N)\) would already give unconditional \(o(N)\)
central source/target loss.  Aligning the resulting wreaths with the
upper Boolean band remains separate.
