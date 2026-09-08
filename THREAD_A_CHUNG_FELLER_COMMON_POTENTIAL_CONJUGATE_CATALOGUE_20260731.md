# Chung--Feller conjugate catalogues: exact averaging and a common-potential triangle

Date: 2026-07-31  
Lane: A, ordered four-transversal / common-potential catalogue  
Status: unconditional all-dimensional catalogue theorem and obstruction.
No ordered four-transversal existence theorem is claimed.

## 0. Result and scope

Fix \(m\ge2\), put \(\Omega=[2m]\), and let

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal X=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1}.
\]

Let \(F_m\) be the canonical MSW/Chung--Feller rooted complement-path
factor.  Consecutive middle states on its paths define oriented diamond
atoms.  This note proves four facts.

1. Every conjugate by the exact phase stabilizer

   \[
       H_m=\langle(2\ 3),(4\ 5),\ldots,(2m-2\ 2m-1)\rangle
   \]

   increases the same strict phase potential.  Thus this family genuinely
   meets the common-potential hypothesis of the bipartite-conflict rounding
   theorem; it is not merely a collection of separately acyclic parents.

2. For any subgroup \(G\le H_m\), the uniform orbit average has every
   upper load exactly one and every tail and head load at most one.  Its
   lower load is exactly the orbit average of the canonical lower-colour
   histogram.  Consequently it saturates the lower shore if and only if

   \[
              \sum_{L\in\mathcal O}\mu_m(L)=|\mathcal O|       \tag{0.1}
   \]

   for every \(G\)-orbit \(\mathcal O\subseteq\mathcal L\).  This is a
   necessary-and-sufficient fractional criterion, not a heuristic
   symmetry assertion.

3. Nevertheless, for every \(m\ge3\), the full \(H_m\)-conjugate
   catalogue contains three distinct atoms with one common lower resource
   and one common head resource.  Its resource-conflict graph therefore
   contains a triangle and is not bipartite.  Hence the positive rounding
   theorem from item 2165 cannot be applied to this natural catalogue.

4. The full coordinate-conjugate orbit under \(S_{2m}\) contains both
   orientations of every diamond.  It admits no strict common potential.
   Reorienting the underlying diamonds by an external coordinate order is
   a different construction; it restores a common potential but not the
   directed Chung--Feller parent structure, and its complete monotone
   catalogue still contains mixed resource triangles.

These statements do not exclude a carefully selected, nonsymmetric
subfamily of conjugates.  Such a subfamily must delete at least one member
of every explicit triangle below and must reprove fractional lower/upper
saturation after the deletion.

## 1. The directed Chung--Feller atom family

Let \(\mathcal D_m\) be the Dyck \(m\)-subsets of \([2m]\).  The canonical
factor has paths

\[
 X_0(P),X_1(P),\ldots,X_m(P),\qquad P\in\mathcal D_m,       \tag{1.1}
\]

where \(X_0(P)=P\), \(X_m(P)=\Omega\setminus P\), and consecutive states
are adjacent in \(J(2m,m)\).  The phase layers

\[
              \mathcal X_t=\{X_t(P):P\in\mathcal D_m\},
              \qquad 0\le t\le m,                         \tag{1.2}
\]

partition \(\mathcal X\).  Define

\[
                         \phi(X)=t\quad(X\in\mathcal X_t). \tag{1.3}
\]

For each transition put

\[
\begin{aligned}
 L_t(P)&=X_t(P)\cap X_{t+1}(P),\\
 U_t(P)&=X_t(P)\cup X_{t+1}(P).
\end{aligned}                                             \tag{1.4}
\]

If \(X_t(P)=L_t(P)+a\) and \(X_{t+1}(P)=L_t(P)+b\), denote the resulting
oriented atom by

\[
                         \alpha_t(P)=(L_t(P);a,b).          \tag{1.5}
\]

The catalogue \(F_m\) is the occurrence-labelled set of all atoms (1.5).
The rooted complement-path theorem gives:

* the upper resources \(U_t(P)\) enumerate \(\mathcal U\) exactly once;
* the tails \(X_t(P)\), \(0\le t<m\), are all distinct;
* the heads \(X_{t+1}(P)\), \(0\le t<m\), are all distinct; and
* every atom strictly increases \(\phi\).

Only the lower resources need not be a transversal.  Write their exact
histogram as

\[
                 \mu_m(L)=|\{(P,t):L_t(P)=L\}|.            \tag{1.6}
\]

## 2. Which coordinate conjugates share the phase potential

The exact coordinate stabilizer of all Chung--Feller layers is

\[
 H_m=\langle(2\ 3),(4\ 5),\ldots,(2m-2\ 2m-1)\rangle.     \tag{2.1}
\]

This is the maximality theorem proved in
`MATH_THEOREM_CHUNG_FELLER_AUTOMORPHISM_AND_PENTAGON_ESCAPE_20260726.md`.

### Theorem 2.1 (common phase potential)

For every \(g\in H_m\) and every atom \(\alpha=(L;a,b)\in F_m\), the
directed conjugate

\[
                         g\alpha=(gL;ga,gb)              \tag{2.2}
\]

satisfies

\[
                 \phi(g(L+a))<\phi(g(L+b)).             \tag{2.3}
\]

Thus every subcatalogue of \(H_mF_m\) has one common strict potential.

#### Proof

Every \(g\in H_m\) preserves each phase layer \(\mathcal X_t\).  If
\(L+a=X_t(P)\) and \(L+b=X_{t+1}(P)\), then their images remain in layers
\(t\) and \(t+1\), respectively.  Equation (1.3) gives (2.3). \(\square\)

The quantifier “one common” is essential.  Assigning a different potential
to each conjugate proves only that each parent separately is acyclic.  It
does not exclude a directed cycle assembled from atoms belonging to
different parents.

## 3. Exact fractional orbit criterion

Let \(G\le H_m\).  Keep occurrences labelled by \((g,P,t)\), and give
each occurrence of \(g\alpha_t(P)\) weight \(1/|G|\).  Equal physical
atoms may equivalently be collapsed by adding their weights.

### Theorem 3.1 (orbit-average ledger)

The resulting vector \(x^G\) has

\[
 \sum_{\upsilon(\alpha)=U}x^G_\alpha=1
                 \qquad(U\in\mathcal U),                \tag{3.1}
\]

and

\[
 \sum_{\tau(\alpha)=X}x^G_\alpha\le1,\qquad
 \sum_{\eta(\alpha)=X}x^G_\alpha\le1
                 \qquad(X\in\mathcal X).                \tag{3.2}
\]

For a lower resource \(L\), its exact load is

\[
 \ell_G(L)=\frac1{|G|}\sum_{g\in G}\mu_m(g^{-1}L).      \tag{3.3}
\]

If \(\mathcal O=GL\), then

\[
             \ell_G(L)=\frac1{|\mathcal O|}
                         \sum_{R\in\mathcal O}\mu_m(R). \tag{3.4}
\]

Consequently \(x^G\) is a fractionally saturating ordered-four-
transversal vector if and only if (0.1) holds for every lower orbit.

#### Proof

Every conjugate \(gF_m\) enumerates the upper shore once and uses each
tail and each head at most once.  Averaging proves (3.1)--(3.2).  A
conjugated occurrence has lower resource \(L\) precisely when the original
occurrence has lower resource \(g^{-1}L\), proving (3.3).

By orbit--stabilizer, as \(g\) runs over \(G\), every member of
\(\mathcal O\) occurs exactly \(|G|/|\mathcal O|\) times as \(g^{-1}L\).
This proves (3.4).  Lower saturation is exactly \(\ell_G(L)=1\) for every
orbit, which is (0.1). \(\square\)

The criterion can fail even though all point degrees balance.  For
example, at \(m=3\) the lower resource

\[
                              L=\{1,6\}                 \tag{3.5}
\]

is fixed by \(H_3=\langle(2\ 3),(4\ 5)\rangle\), while the phase-one
transitions of the Dyck roots \(111000\) and \(110100\) are

\[
 101001\longrightarrow100101,qquad
 110001\longrightarrow100011                         \tag{3.6}
\]

where strings are read in coordinate order from \(1\) to \(6\), both have
intersection \(\{1,6\}\).  Thus \(\mu_3(L)\ge2\), and the
uniform \(H_3\)-orbit average has lower load at least two at this singleton
orbit, not one.  This is an exact fractional obstruction for that symmetric
average only; nonuniform selected conjugates are not ruled out.

## 4. An explicit triangle in every phase-preserving orbit catalogue

For \(m\ge3\), define

\[
                  L=\{1,3,4,\ldots,m\},\qquad h=2m.     \tag{4.1}
\]

The following three atoms are distinct:

\[
 \alpha=(L;2,h),\qquad
 \beta=(L;2m-2,h),\qquad
 \gamma=(L;2m-1,h).                                  \tag{4.2}
\]

### Lemma 4.1 (literal Chung--Feller membership)

All three atoms in (4.2) belong to the conjugate catalogue \(H_mF_m\).

#### Proof

The first canonical transition from the Dyck root

\[
                              P_0=1^m0^m                 \tag{4.3}
\]

deletes coordinate \(2\) and inserts coordinate \(2m\).  Its atom is
\(\alpha\).

Now put

\[
       P_1=\{1,2,4,5,\ldots,m,2m-2\}.                  \tag{4.4}
\]

The interval \(\{4,5,\ldots,m\}\) is empty when \(m=3\).  The word of
\(P_1\) has height \(m-2\) after coordinate \(m\), then falls to height
one, rises at coordinate \(2m-2\), and ends with two down-steps.  Hence it
is Dyck.  Its first canonical transition deletes coordinate \(2m-2\) and
inserts coordinate \(2m\).

Both first-transition assertions follow directly from the MSW formulas
\(f=h\circ g\): on these two primitive Dyck words, \(g\) inserts the final
coordinate \(2m\).  Here is the complete height scan.  On \(P_0\), after
that insertion the up-steps starting at height one occur at coordinates
\(2\) and \(2m\); including the initial up-step from height zero, the
ordinal in the definition of \(h\) selects coordinate \(2\).  On \(P_1\),
the touching up-steps, in order, occur at coordinates

\[
                  1, 2, 4, 2m-2, 2m,               \tag{4.5}
\]

with the coincident entries \(4=2m-2\) identified when \(m=3\).  The
number of up-steps starting at height one is four when \(m\ge4\), and
three when \(m=3\); the corresponding ordinal in (4.5) is therefore
\(2m-2\) in both cases.  Hence the subsequent \(h\)-step deletes
respectively coordinate \(2\) or \(2m-2\), as asserted.

Let

\[
 \sigma=(2\ 3),\qquad
 \sigma'=(2\ 3)(2m-2\ 2m-1).                           \tag{4.6}
\]

Both lie in \(H_m\).  Conjugating the first transition of \(P_1\) by
\(\sigma\) gives \(\beta\), and conjugating it by \(\sigma'\) gives
\(\gamma\).  Indeed, both permutations send
\(P_1\setminus\{2m-2\}\) to \(L\); the first sends the deleted coordinate
to \(2m-2\), the second to \(2m-1\), and both fix \(2m\). \(\square\)

### Theorem 4.2 (phase-preserving conjugate triangle)

For every \(m\ge3\), the resource-conflict graph of \(H_mF_m\) is not
bipartite.

#### Proof

The atoms (4.2) have the same lower resource \(L\).  They also have the
same head resource \(L+\{2m\}\).  Hence they form a three-clique in the
resource-conflict graph.  A graph containing a triangle is not bipartite.
\(\square\)

This obstruction is stronger than merely observing a repeated lower
colour: it exhibits the exact mixed occurrence columns that must be
deleted or separated before bipartite-conflict rounding can apply.

## 5. Why unrestricted coordinate conjugacy loses the potential

### Theorem 5.1 (reverse-orientation obstruction)

Let \(\mathcal C\) contain the full \(S_{2m}\)-orbit of one directed atom.
Then no function \(\psi:\mathcal X\to\mathbb R\) strictly increases on
every atom of \(\mathcal C\).

#### Proof

Write the atom as \((L;a,b)\).  The coordinate transposition \((a\ b)\)
fixes \(L\) and sends it to the reverse atom \((L;b,a)\).  Thus
\(\mathcal C\) contains both directed arcs

\[
                         L+a\longrightarrow L+b,
 \qquad                  L+b\longrightarrow L+a.       \tag{5.1}
\]

A strict potential would have to increase in both directions, which is
impossible. \(\square\)

For \(m\ge3\), the same conclusion holds for the full alternating-group
orbit: compose \((a\ b)\) with a transposition inside \(L\), or inside the
unused coordinates, to obtain an even permutation inducing the same
reversal.  The small \(A_4\) orbit at \(m=2\) is exceptional and is not
used here.

One can instead forget the inherited directions and fix distinct
coordinate weights \(w_i\), orienting every diamond from \(L+a\) to
\(L+b\) when \(w_a<w_b\).  Then

\[
                         \psi(X)=\sum_{i\in X}w_i        \tag{5.2}
\]

is a common potential.  This is **not** a directed coordinate-conjugate
Chung--Feller catalogue: an individual conjugated path can acquire local
sources and sinks, so its tail/head-cap-one ledger no longer follows from
the path factor.

Moreover, the complete monotone catalogue is still not bipartite.  In the
mixed triangle of item 2165, choose the four relevant coordinates with

\[
                              w_\ell<w_q<w_p<w_r.        \tag{5.3}
\]

Then all three displayed atoms are oriented increasingly and remain a
resource-conflict triangle.  Thus external coordinate-order orientation
restores only the potential half of Theorem 3.1 of the ordered-four-
transversal note; fractional saturation and bipartite conflict remain
separate gates.

The coordinate-order model has now been frozen independently in
`THREAD_A_GLOBAL_COORDINATE_POTENTIAL_M3_EXACT_NOGO_20260731.md`.  Its
exact memoized recurrence has two solutions at \(m=2\) and none at \(m=3\).
This lane independently audited the recurrence: its state retains exactly
the remaining lower rows and the used upper, tail and head resources;
future feasibility depends on no other history, and at termination \(N\)
distinct upper resources among the \(N\) available ones are automatically
all upper resources.  All total coordinate orders are isomorphic by
relabelling.  The separately reported \(m=4\) count is not needed and is
not authenticated here.

## 6. The direct PBBS-cycle analogue

The centered PBBS construction is naturally a Johnson \(2\)-factor rather
than a rooted path factor.  Its cyclic chronology therefore behaves
differently from (1.1).

### Proposition 6.1 (cyclic-parent obstruction)

Let a directed candidate catalogue contain every directed edge of one
nonempty directed cycle.  It admits no strict common potential.  In
particular, orienting every component of the centered PBBS \(2\)-factor by
its PBBS step-two chronology does not meet the common-potential hypothesis.

#### Proof

Strict increase around the cycle would give

\[
 \psi(X_0)<\psi(X_1)<\cdots<\psi(X_{r-1})<\psi(X_0),
\]

an impossibility. \(\square\)

Breaking at least one directed edge in each PBBS component removes this
particular obstruction, but it also destroys the closed factor ledger and
requires an explicit replacement bank.  Alternatively, orienting the
underlying undirected edges by an external total order is acyclic, but at
a local minimum or maximum of an undirected factor cycle the resulting
parent has two equal-type tail or head uses.  Thus neither operation
inherits the fractional tail/head rows for free.  This is only a direct-
parent no-go; a symmetry-broken PBBS opening with compensated resources is
not excluded.

The centered PBBS factor is on the odd ground set \(2m+1\), whereas the
ordered four-transversal here is on \(2m\).  Proposition 6.1 is therefore
an obstruction to importing its cyclic directed-parent mechanism, not an
identification of the two atom systems.

## 7. Exact remaining catalogue gate

The natural conjugation attempts fail for two different, rigorously
separated reasons.

* Enlarging to all coordinate conjugates supplies reverse arcs and destroys
  every common strict potential.
* Restricting to the maximal phase-preserving group \(H_m\) retains a
  common strict potential, but its full orbit has the explicit triangle
  (4.2).  Its symmetric fractional lower shore must additionally pass the
  orbit equations (0.1), which already fail at \(m=3\).

The smallest surviving positive target is therefore:

> choose a nonsymmetric subfamily of phase-preserving conjugate atoms,
> deleting at least one atom from every resource odd circuit, and exhibit
> on the remaining catalogue a fractional vector saturating both outer
> shores with tail/head load at most one.

If the remaining conflict graph is bipartite, Theorem 3.1 of
`MATH_THEOREM_A_CATALAN_ORDERED_FOUR_TRANSVERSAL_ODD_CIRCUIT_ROUNDING_20260731.md`
then rounds it integrally and the phase potential proves acyclicity.  No
such all-dimensional deletion-and-rebalancing theorem is proved here.
