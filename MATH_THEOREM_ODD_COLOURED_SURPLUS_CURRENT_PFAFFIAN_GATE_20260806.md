# Odd current: one coloured cotransversal Pfaffian is the exact direct gate

**Date:** 2026-08-06  
**Method:** generic transversal representation, exterior two-forms, and
square-zero hub-colour variables; no computation  
**Status:** unconditional exact reduction.  After the stabilizer-root cut,
the existence of a majority-only, hub-rainbow **boundary-current bank**
whose endpoints form a surplus basis is equivalent to nonvanishing of one
explicit Pfaffian.  The theorem also includes one prescribed terminal
socket.  It does not prove that this Pfaffian is nonzero for every sector.
It prices hub colours on the boundary-current bank, not on the
complementary nonwrap matching; repeated colours there still belong to the
fan/receiver route.

## 1. Input from the stabilizer-root theorem

Let

\[
                         B=(L,R;E_B)
\tag{1.1}
\]

be the bipartite nonwrap quotient graph supplied by the stabilizer-root
cut.  It has a matching saturating \(R\), and

\[
                         \delta=|L|-|R|>0.
\tag{1.2}
\]

Let \(S\) be the rank-\(\delta\) cotransversal surplus matroid on \(L\):
a \(\delta\)-set \(U\subseteq L\) is a basis of \(S\) exactly when
\(B-U\) has a perfect matching.

Let \(W\) be the same-shore physical boundary graph on \(L\).  A simple
quotient edge \(uv\) can have several legal pointed occurrences.  Write

\[
                         {\cal O}(uv)
\tag{1.3}
\]

for those occurrences, after all protected vertices and forbidden reset
colours have been removed.  Every occurrence \(o\) has an unpointed
deleted-cut hub colour \(c(o)\).

The direct current problem asks for:

1. a basis \(U\) of \(S\);
2. a perfect matching of \(W[U]\), when \(\delta\) is even; or a matching
   of \(U-\{s\}\) for one allowed socket \(s\), when \(\delta\) is odd;
3. one pointed occurrence for every selected quotient edge; and
4. distinct hub colours on the selected occurrences.

## 2. A generic representation of the surplus matroid

The transversal matroid presented by \(B\) is represented over a rational
function field as follows.  Give every incidence \(lr\in E_B\) an
independent variable \(z_{rl}\), and form the \(|R|\)-by-\(|L|\) matrix

\[
 X_{r l}=
 \begin{cases}
 z_{rl},&lr\in E_B,\\
 0,&lr\notin E_B.
 \end{cases}
\tag{2.1}
\]

A square minor of \(X\) is nonzero exactly when its row and column sets
have a perfect incidence matching: every matching contributes a distinct
monomial.  Thus \(X\) represents the transversal matroid.  Its dual
surplus matroid \(S\) is representable over the same field.  Fix any
full-row-rank matrix

\[
                         A=(a_v)_{v\in L}
\tag{2.2}
\]

of size \(\delta\)-by-\(|L|\) representing \(S\).  Therefore

\[
 \det A[U]\ne0
 \quad\Longleftrightarrow\quad
 U\text{ is a surplus basis}.
\tag{2.3}
\]

No canonical choice of \(A\) is needed.

## 3. The occurrence and colour algebra

For every legal pointed occurrence \(o\), introduce an independent
commuting variable \(x_o\).  For every unpointed hub colour \(c\),
introduce a commuting square-zero variable

\[
                         \epsilon_c^2=0.
\tag{3.1}
\]

Work over the commutative algebra

\[
 {\cal R}
 =K[x_o:o]\,[\epsilon_c:c]/(\epsilon_c^2:c),
\tag{3.2}
\]

where \(K\) is the representation field of Section 2.  Its squarefree
hub monomials are linearly independent over \(K[x_o:o]\).

Define the skew occurrence matrix \(\Theta\), indexed by \(L\), by

\[
 \Theta_{uv}
 =\sum_{o\in{\cal O}(uv)}\epsilon_{c(o)}x_o
 \quad(u<v),
 \qquad
 \Theta_{vu}=-\Theta_{uv}.
\tag{3.3}
\]

Finally put

\[
                         \Omega=A\Theta A^{\mathsf T}.
\tag{3.4}
\]

It is a \(\delta\)-by-\(\delta\) skew matrix over \({\cal R}\).

## 4. Even surplus rank

### Theorem 4.1 (coloured surplus-current Pfaffian)

Suppose \(\delta\) is even.  Then

\[
                         \operatorname{Pf}(\Omega)\ne0
\tag{4.1}
\]

if and only if there are:

* a surplus basis \(U\subseteq L\);
* a perfect matching \(P\) of \(W[U]\); and
* one occurrence \(o_e\in{\cal O}(e)\) for every \(e\in P\),

such that all hub colours \(c(o_e)\) are distinct.

Consequently (4.1) is equivalent to a perfect matching of the simple
capacity-two sector whose majority-current bank is hub-rainbow.  It is not
yet a globally hub-rainbow ambient lift, because the complementary
nonwrap matching can repeat an unpointed hub colour.

#### Proof

Let \(a_v\) be the columns in (2.2), and form the exterior two-form

\[
 \omega=\sum_{\{u,v\}\in W}
          \Theta_{uv}\,a_u\wedge a_v
 \in\Lambda^2 K^\delta\otimes{\cal R}.
\tag{4.2}
\]

The coefficient of a fixed volume form in
\(\omega^{\delta/2}/(\delta/2)!\) is
\(\operatorname{Pf}(\Omega)\).  Expanding first by the set of used
columns gives the Pfaffian minor-summation identity

\[
 \operatorname{Pf}(\Omega)
 =\sum_{\substack{U\subseteq L\\|U|=\delta}}
    \pm\det A[U]\operatorname{Pf}\Theta[U].
\tag{4.3}
\]

Expand \(\operatorname{Pf}\Theta[U]\).  A term chooses a perfect matching
of \(W[U]\), one pointed occurrence of every selected quotient edge, and
has coefficient

\[
 \pm
 \left(\prod_e x_{o_e}\right)
 \left(\prod_e\epsilon_{c(o_e)}\right).
\tag{4.4}
\]

If one hub colour repeats, (4.4) is zero by (3.1).  If all colours are
distinct, it is a nonzero squarefree colour monomial.  Different pointed
matching choices have different products of the independent variables
\(x_o\), so two surviving terms cannot cancel.

Finally, the coefficient \(\det A[U]\) is nonzero exactly for a surplus
basis by (2.3).  Therefore the whole sum (4.3) is nonzero exactly when one
of the displayed hub-rainbow basis matchings exists.

Adjoin the perfect matching of \(B-U\), supplied by the surplus-basis
property, to the selected boundary matching.  This gives the final simple
sector matching.  The square-zero variables certify distinct hub colours
only among the selected boundary occurrences. \(\square\)

## 5. Odd surplus rank and one typed socket

Now suppose \(\delta\) is odd, and let \(O\subseteq L\) be the allowable
terminal socket set after all type and protected-bank restrictions.
Add one dummy vertex \(\star\).  Extend the surplus representation to
rank \(\delta+1\) by

\[
 \widetilde a_v=(a_v,0)\quad(v\in L),
 \qquad
 \widetilde a_\star=(0,\ldots,0,1).
\tag{5.1}
\]

Let \(\widetilde A\) be the resulting matrix.  Extend the occurrence graph
by the edges

\[
                         \star s\qquad(s\in O),
\tag{5.2}
\]

giving each such edge an independent variable \(y_s\) and no hub-colour
factor.  Let \(\widetilde\Theta\) be the corresponding skew matrix and put

\[
 \widetilde\Omega
 =\widetilde A\widetilde\Theta\widetilde A^{\mathsf T}.
\tag{5.3}
\]

### Theorem 5.1 (one-socket Pfaffian)

\[
                         \operatorname{Pf}(\widetilde\Omega)\ne0
\tag{5.4}
\]

if and only if there are:

* a surplus basis \(U\);
* one allowed socket \(s\in U\cap O\);
* a perfect matching of \(W[U-\{s\}]\); and
* a hub-rainbow pointed occurrence choice for that matching.

This is equivalent to a direct majority-only simple-sector matching which
misses exactly the typed socket \(s\), with a hub-rainbow boundary-current
bank.

#### Proof

Apply Theorem 4.1 to the extended rank-\((\delta+1)\) system.  Every basis
of the represented extension has the form \(U\cup\{\star\}\), with \(U\)
a basis of \(S\).  In every perfect matching of the extended occurrence
graph, \(\star\) is matched to exactly one \(s\in O\), and the remaining
vertices \(U-\{s\}\) are matched by physical boundary edges.  The
independent variable \(y_s\) prevents cancellation between different
socket choices. \(\square\)

## 6. Why this is not the failed free-fermion argument

The audited free-fermion matrix used one translation-invariant
one-particle current and therefore had a forced bank of inverse-momentum
zero modes.  The present matrix is different in all load-bearing ways:

1. \(A\) is a generic representation of the complete nonwrap incidence
   system, so it already contains every Hall correlation of the cut-open
   many-particle sector;
2. \(\Theta\) uses configuration- and occurrence-dependent variables on
   the actual boundary transfers;
3. the product \(A\Theta A^{\mathsf T}\) is the exterior projection of a
   cotransversal basis-matching problem, not an additive one-particle
   operator; and
4. square-zero colour variables impose the unpointed hub partition on the
   boundary-current bank.

Thus Fourier nullity neither proves nor disproves (4.1).  Nonvanishing of
this interacting Pfaffian is exactly the remaining direct coloured
**boundary-current** theorem.  Ambient completion still has to make the
chosen nonwrap matching hub-safe or pass its repeated colours through the
paired fan/receiver construction.

## 7. Protected-minor form

If a finite receiver bank or compensation linkage has already consumed
vertices, delete those vertices from \(B,W\) before constructing the
transversal representation.  If the residual \(B\) still saturates its
minority shore, Sections 2--5 apply verbatim to its residual surplus
matroid.  Forbidden hub colours are removed by deleting their occurrences
from (3.3), and allowed socket types are imposed by the set \(O\).

Therefore every protected direct-current instance has one exact
certificate:

\[
\boxed{\text{the corresponding coloured surplus Pfaffian is nonzero}.}
\tag{7.1}
\]

This is a genuine protected-minor statement.  It does not assert that
arbitrary protected deletions preserve minority saturation.

## 8. Scope

Proved:

1. generic representability of the exact surplus cotransversal matroid;
2. a single Pfaffian whose nonvanishing is equivalent to a physical
   nearest-neighbour surplus-basis matching;
3. exact occurrence choice and unpointed hub-rainbow enforcement on its
   boundary-current edges;
4. an exact one-typed-socket extension; and
5. the protected residual version after any independently certified
   minority-saturating deletion.

Not proved:

1. nonvanishing of the Pfaffian in every odd sector;
2. a useful factorization or leading monomial proving nonvanishing;
3. hub safety of the complementary nonwrap matching, and the repeated-hub
   fan/receiver architecture when no direct rainbow current exists;
4. PBBS halo/cap compatibility; or
5. the all-\(k\) upper bound.
