# Trapped-colour normal form for the union-rainbow rethread cut

**Date:** 2026-08-07  
**Method:** exact cycle incidence and partition-capacity algebra  
**Status:** unconditional reduction, assuming the doubly adequate cycle
from the companion rethread theorem.  It does not construct that cycle or
prove the resulting inequality.

## 1. Setup

Let \(|\Omega|=2m\), and put

\[
 \mathcal A={\Omega\choose m-2},\qquad
 \mathcal B={\Omega\choose m-1},\qquad
 \mathcal U={\Omega\choose m}.
\]

Let \(K\) be a Hamilton cycle on \(\mathcal B\).  For \(e=YZ\in E(K)\)
write

\[
 i(e)=Y\cap Z\in\mathcal A,
 \qquad q(e)=Y\cup Z\in\mathcal U.
\]

Assume that \(q\) is injective and that \(i(E(K))=\mathcal A\).  Let

\[
 \mathcal O=\mathcal U\setminus q(E(K)),
 \qquad E_a=\{e:i(e)=a\},\qquad \mu_a=|E_a|.
\]

Thus every \(\mu_a\ge1\).  For \(\mathcal X\subseteq\mathcal O\), let

\[
 S(\mathcal X)=\partial^-\mathcal X
 =\{Y\in\mathcal B:Y\subset U\text{ for some }U\in\mathcal X\}.
 \tag{1.1}
\]

Let \(N_K(\mathcal X)\) be the cycle edges with at least one endpoint in
\(S(\mathcal X)\).  Finally define

\[
 \kappa_K(S)=|S|-|E(K[S])|.                         \tag{1.2}
\]

If \(S\ne\mathcal B\), the induced subgraph \(K[S]\) is a union of paths
and isolated vertices, so \(\kappa_K(S)\) is exactly its number of
components.  If \(S=\mathcal B\), it is zero.

Call an intersection colour \(a\) **trapped by** \(S\) when every one of
its cycle occurrences touches \(S\):

\[
 E_a\subseteq N_K(\mathcal X).
\]

Write

\[
 \tau_K(\mathcal X)
 =|\{a\in\mathcal A:E_a\subseteq N_K(\mathcal X)\}|. \tag{1.3}
\]

## 2. Exact normal form

### Theorem 2.1 (incident-edge identity)

For every \(\mathcal X\subseteq\mathcal O\),

\[
 \boxed{|N_K(\mathcal X)|
       =|S(\mathcal X)|+\kappa_K(S(\mathcal X)).}   \tag{2.1}
\]

#### Proof

In the cycle, summing degrees over \(S\) gives

\[
 2|S|=2|E(K[S])|+|\delta_K(S)|.
\]

The edges touching \(S\) consist of the induced edges and the cut edges,
so

\[
 |N_K(\mathcal X)|
 =|E(K[S])|+|\delta_K(S)|
 =2|S|-|E(K[S])|
 =|S|+\kappa_K(S).
\]

This also covers \(S=\mathcal B\), when the last two quantities are
\(|E(K)|=|S|\). \(\square\)

### Theorem 2.2 (trapped-colour identity)

The deletion capacity available to \(\mathcal X\) is exactly

\[
 \boxed{
 \sum_{a\in\mathcal A}
   \min\bigl(\mu_a-1,\ |N_K(\mathcal X)\cap E_a|\bigr)
 =|N_K(\mathcal X)|-\tau_K(\mathcal X).}           \tag{2.2}
\]

#### Proof

Put \(n_a=|N_K(\mathcal X)\cap E_a|\).  Since \(0\le n_a\le\mu_a\),

\[
 \min(\mu_a-1,n_a)
 =n_a-\mathbf 1_{\{n_a=\mu_a\}}.
\]

Sum over \(a\).  The \(E_a\)'s partition \(E(K)\), hence
\(\sum_a n_a=|N_K(\mathcal X)|\); the indicator sum is precisely
\(\tau_K(\mathcal X)\). \(\square\)

### Corollary 2.3 (exact safe-endpoint criterion)

There is a palette-safe deletion edge assigned to every omitted colour,
with all deletion edges distinct, if and only if

\[
 \boxed{
 \tau_K(\mathcal X)
 \le |\partial^-\mathcal X|-|\mathcal X|
    +\kappa_K(\partial^-\mathcal X)
 \quad\text{for every }\mathcal X\subseteq\mathcal O.} \tag{2.3}
\]

#### Proof

The companion rethread theorem gives the exact capacitated Hall condition

\[
 \sum_a\min(\mu_a-1,|N_K(\mathcal X)\cap E_a|)
 \ge|\mathcal X|.
\]

Substitute (2.1)--(2.2) and rearrange. \(\square\)

Thus the cut has only three terms:

1. ordinary lower-shadow surplus \(|\partial^-\mathcal X|-|\mathcal X|\);
2. fragmentation of that shadow along the Hamilton cycle;
3. the number of intersection colours all of whose occurrences are trapped
   at that shadow.

All ordinary endpoint expansion has disappeared from the open problem.

There is an even shorter complementary form.  Put

\[
 R=|E(K)|-|\mathcal A|
\]

for the total intersection-colour repeat surplus, and for
\(T\subseteq\mathcal B\) define the repeat surplus retained inside \(T\) by

\[
 \operatorname {rep}_K(T)
 =|E(K[T])|-|i(E(K[T]))|.                            \tag{2.4}
\]

The second term counts distinct intersection colours, not occurrences.

### Corollary 2.4 (exterior repeat-surplus criterion)

For \(T(\mathcal X)=\mathcal B\setminus\partial^-\mathcal X\), the
safe-endpoint deletion exists if and only if

\[
 \boxed{
 \operatorname {rep}_K(T(\mathcal X))
 \le R-|\mathcal X|
 \quad\text{for every }\mathcal X\subseteq\mathcal O.} \tag{2.5}
\]

#### Proof

The edges not in \(N_K(\mathcal X)\) are exactly \(E(K[T])\).  Moreover,
an intersection colour is not trapped precisely when it appears on at
least one of these exterior edges.  Hence

\[
 \tau_K(\mathcal X)=|\mathcal A|-|i(E(K[T]))|.
\]

Using \(|N_K(\mathcal X)|=|E(K)|-|E(K[T])|\), the available capacity in
(2.2) becomes

\[
 |E(K)|-|E(K[T])|-|\mathcal A|+|i(E(K[T]))|
 =R-\operatorname {rep}_K(T).
\]

Requiring this to be at least \(|\mathcal X|\) gives (2.5). \(\square\)

Thus each omitted upper colour must be paid for by one unit of global
intersection-repeat surplus that is not sequestered wholly outside its
facet shadow.  Since

\[
 R=|\mathcal B|-|\mathcal A|={3m\over m+2}\operatorname {Cat}_m,
\]

while \(|\mathcal O|=\operatorname {Cat}_m\), the scalar reserve is almost
three units per omitted colour.  The open issue is solely the spatial
distribution of those units along the cycle.

## 3. Sharp singleton interpretation

For one omitted colour \(U\), its shadow consists of its \(m\) facets.
No two of those facets are adjacent on \(K\), because such an edge would
have union \(U\), contrary to \(U\in\mathcal O\).  Hence

\[
 |\partial^-\{U\}|=m,qquad
 \kappa_K(\partial^-\{U\})=m,qquad
 |N_K(U)|=2m.                                      \tag{3.1}
\]

Condition (2.3) becomes

\[
                         \boxed{\tau_K(U)\le2m-1.} \tag{3.2}
\]

Equivalently, among the \(2m\) cycle edges incident with facets of \(U\),
at least one has an intersection colour with another occurrence outside
that incident-edge bank, or two of the incident edges share one colour.

A same-deletion hinge at a facet of \(U\) supplies the second alternative:
its two incident edges share one intersection colour.  This explains
exactly why the private-hinge certificate closes every singleton cut.
Larger cuts additionally require the hinges not to collapse onto the same
colour capacity; that is the content of the full inequality (2.3).

## 4. Protected minor

Let \(P\subseteq E(K)\) be a protected edge set that may not be deleted,
and put \(E'=E(K)\setminus P\).  For each colour set

\[
 c_a=\min(\mu_a-1,|E_a\cap E'|),
 \qquad n'_a(\mathcal X)=|N_K(\mathcal X)\cap E_a\cap E'|.
\]

The exact protected criterion is

\[
 \boxed{\sum_a\min(c_a,n'_a(\mathcal X))\ge|\mathcal X|
 \quad(\mathcal X\subseteq\mathcal O).}            \tag{4.1}
\]

When \(P=\varnothing\), (4.1) reduces to (2.3).  For a nonempty protected
bank, the simple trapped-colour count need not by itself encode the lost
available occurrences; (4.1), rather than the unrestricted criterion, is
the proof-safe statement.

## 5. Remaining construction target

The first rethread gate can now be attacked by constructing a
union-rainbow Hamilton cycle for which

1. every intersection colour occurs;
2. the protected pivot segment survives; and
3. the trapped-colour inequality (2.3), or its protected form (4.1), holds.

Private omitted-colour hinges are a transparent sufficient design, but
they are stronger than necessary.  Any construction that spreads repeated
intersection colours so that no omitted-colour shadow traps too many whole
colour classes also closes the same gate.

This theorem does not construct the doubly adequate cycle, the exterior
forest, residence, or the all-width upper deck.
