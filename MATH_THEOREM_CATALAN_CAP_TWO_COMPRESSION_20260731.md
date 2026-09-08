# Catalan compression at the integrality floor

Date: 2026-07-31  
Status: proved, conditional only on the published saturating-cycle theorem

## 0. Statement

For \(m\ge2\), put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

The existing Catalan-compression theorem constructs a Hamilton cycle of
\(J(2m,m)\) in which every rank-\((m+1)\) union colour occurs in one
contiguous block.  The unused middle facets were assigned to blocks with no
load control.

The assignment can always be made injective on the upper blocks.  Therefore
the union-colour load is exactly

\[
                             1^{N-K}2^K,                        \tag{0.1}
\]

the unique integrality-floor profile.  This also collapses the residual
two-sided problem from arbitrary paths inside blocks to one Catalan-sized
matching.

## 1. A small-family upper-shadow lemma

### Lemma 1.1

If \({\cal A}\subseteq\binom{[2m]}m\) and

\[
                         |{\cal A}|\le\operatorname{Cat}_m,
\]

then its upper shadow satisfies

\[
                         |\partial^+{\cal A}|\ge|{\cal A}|.    \tag{1.1}
\]

Consequently every family of at most \(\operatorname{Cat}_m\) middle sets
has a matching into distinct containing rank-\((m+1)\) sets.

#### Proof

Complementation turns \(\partial^+{\cal A}\) into the lower shadow of an
equally large family of \(m\)-sets.  Write
\(|{\cal A}|=\binom{x}{m}\) for real \(x\ge m\).  Since

\[
 |{\cal A}|\le {1\over m+1}\binom{2m}{m}
       \le {1\over2}\binom{2m}{m}
       =\binom{2m-1}{m},
\]

we have \(x\le2m-1\).  The continuous Kruskal--Katona shadow theorem gives

\[
 |\partial^+{\cal A}|
   \ge\binom{x}{m-1}
   =\binom{x}{m}\,{m\over x-m+1}
   \ge\binom{x}{m}=|{\cal A}|.
\]

Applying this inequality to every subfamily is Hall's condition and proves
the matching assertion. \(\square\)

## 2. Cap-two Catalan compression

Take a saturating cycle in the incidence graph of ranks \(m,m+1\) of
\(Q_{2m}\), written cyclically as

\[
 C_0,U_0,C_1,U_1,\ldots,C_{N-1},U_{N-1},C_0,                  \tag{2.1}
\]

where the \(U_i\) are all rank-\((m+1)\) sets and the \(C_i\) are distinct
rank-\(m\) sets, with

\[
                             C_i,C_{i+1}\subset U_i.            \tag{2.2}
\]

Let

\[
                  {\cal E}=\binom{[2m]}m\setminus\{C_i:i<N\}.
\]

Then \(|{\cal E}|=K\).  By Lemma 1.1 choose an injection

\[
                  \phi:{\cal E}\longrightarrow\binom{[2m]}{m+1},
                  \qquad X\subset\phi(X).                     \tag{2.3}
\]

### Theorem 2.1 (integrality-floor compression)

There is a Hamilton cycle \(P\) of \(J(2m,m)\) such that

1. every rank-\((m+1)\) union colour occurs in one contiguous block;
2. exactly \(K\) colours occur twice and every other colour occurs once;
3. compressing equal consecutive colours gives the Hamilton cycle
   \(U_0,U_1,\ldots,U_{N-1}\).

#### Proof

For each \(U_i\), use the block

\[
 C_i,C_{i+1}
\]

if \(U_i\notin\operatorname{im}\phi\), and use

\[
 C_i,X,C_{i+1}
\]

when \(\phi(X)=U_i\).  Every two consecutive vertices in a block are
distinct \(m\)-facets of the same \((m+1)\)-set \(U_i\), hence form a
Johnson edge with union \(U_i\).  Concatenating cyclically and identifying
the common seam vertices \(C_{i+1}\) visits every seam facet and every
member of \({\cal E}\) exactly once.  It is therefore a Hamilton cycle.

Injectivity of \(\phi\) puts at most one extra facet in a block.  The \(K\)
matched blocks have two edges and the remaining \(N-K\) blocks have one,
proving (0.1). \(\square\)

The profile (0.1) is forced by counting among all positive loads:
\(M\) cycle edges are distributed over \(N\) colours, and \(M-N=K\).
Thus the theorem attains the exact floor, not merely an \(O(1)\) or bounded
load.

## 3. The residual two-sided condition is one matching

For block \(U_i\), write

\[
 C_i=U_i\setminus\{p_i\},\qquad
 C_{i+1}=U_i\setminus\{q_i\}.                                 \tag{3.1}
\]

If \(\phi(X)=U_i\), write \(X=U_i\setminus\{c_i\}\).  Associate to an
edge between deletion labels \(a,b\in U_i\) the transfer head

\[
                         h_i(a,b)=U_i^c\cup\{a,b\}.             \tag{3.2}
\]

The complement of \(h_i(a,b)\) is the lower intersection colour of the
corresponding middle Johnson edge.

### Corollary 3.1 (Catalan split-repair normal form)

The cap-two cycle of Theorem 2.1 has complete lower adjacent colours if and
only if the matching \(\phi\) can be chosen so that the multiset

\[
 \begin{aligned}
 &\{h_i(p_i,q_i):U_i\notin\operatorname{im}\phi\}\\
 &\quad\cup
 \{h_i(p_i,c_i),h_i(c_i,q_i):\phi(U_i\setminus\{c_i\})=U_i\}
 \end{aligned}                                                \tag{3.3}
\]

covers all of \(\binom{[2m]}{m+1}\).

#### Proof

An unmatched block has the one deletion-label edge \(p_iq_i\).  A matched
block replaces it by the two-edge path \(p_ic_iq_i\).  Formula (3.2) is the
exact union/intersection transfer bijection, so lower-colour completeness is
equivalent to head coverage. \(\square\)

This is materially smaller than the unrestricted integral path-flow system:

* the only variables are a matching of the \(K\) unused facets;
* every selected host performs one local \(1\to2\) head split; and
* the load profile on the already-solved upper side remains at the exact
  integrality floor automatically.

The missing assertion is now a **Catalan split-repair matching theorem**:
choose \(\phi\) so (3.3) is surjective.  It is still a genuine global
condition and is not proved here.  But it is an exact direct target for a
two-sided OR--Pascal central row, rather than an arbitrary Hamilton search.
