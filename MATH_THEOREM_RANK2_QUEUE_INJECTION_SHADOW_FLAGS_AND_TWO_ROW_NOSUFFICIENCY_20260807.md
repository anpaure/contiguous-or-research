# Injection-decorated queue targets are nested shadow flags, but the two endpoint rows do not determine the interior

**Date:** 2026-08-07  
**Method:** augment every target by its inactive bank singletons, then
read the decoration as a nested core-deletion flag  
**Status:** exact structural reduction and exact obstruction to a
singleton-plus-deepest-only matching argument. The all-depth packet has a
laminar flag form, but an intermediate target can collide while both
endpoint-row targets differ.

## 1. Shadow carriers

Fix one rank-two queue ring with core \(K\), bank \(B\), and an
all-switch injection decoration

\[
 \kappa:B\hookrightarrow K.
\tag{1.1}
\]

Let \(Q\) be a proper cyclic source interval of length

\[
 j=p-r,\qquad 1\le r\le p-1.
\tag{1.2}
\]

Write \(U_0(Q)\) for its canonical undecorated target and

\[
 X(Q)=\{x\in B:Q\subseteq I_x\}.
\tag{1.3}
\]

The exact relevant-bit lemma gives \(|X(Q)|=r\). Define the
**shadow carrier**

\[
 B(Q)=U_0(Q)\cup X(Q).
\tag{1.4}
\]

The canonical target has rank \(m-2r\), the added bank coordinates are
new, and therefore

\[
 |B(Q)|=m-r.
\tag{1.5}
\]

### Theorem 1.1 (exact shadow form)

The injection-decorated target at \(Q\) is

\[
 \boxed{
 U^\kappa(Q)=B(Q)\setminus\kappa(X(Q)).
 }
\tag{1.6}
\]

Thus every depth-\((p-r)\) target is an \(r\)-fold lower-shadow child of
a fixed rank-\((m-r)\) carrier, with its deleted \(r\)-set constrained to
be the image of the occurrence-labelled domain \(X(Q)\).

If two decorated targets at this depth are equal,

\[
 B(Q)\setminus\kappa(X(Q))
 =
 B'(Q')\setminus\kappa'(X'(Q')),
\tag{1.7}
\]

then

\[
 \boxed{d_J(B(Q),B'(Q'))\le r.}
\tag{1.8}
\]

#### Proof

The all-switch target formula removes exactly
\(\kappa(X(Q))\) from the core and adds exactly \(X(Q)\) to the
canonical target. This is (1.6). In (1.7), the common target has size
\(m-2r\) and is contained in both rank-\((m-r)\) carriers. Hence their
union has size at most \(m\), or equivalently their Johnson distance is
at most \(r\). \(\square\)

For \(r=1\), the carrier \(B(Q)\) is the rank-\((m-1)\) intersection
colour of the two adjacent owner states bracketing the unique inactive
phase. The deepest decorated target is that q1 lower colour with one
private core coordinate deleted.

## 2. The nested flag at one endpoint

Fix a source endpoint and take all suffix intervals ending there. Their
inactive-coordinate domains form a strict nested flag

\[
 X_1\subset X_2\subset\cdots\subset X_{p-1},
\qquad |X_r|=r,
\tag{2.1}
\]

where \(X_r\) belongs to depth \(p-r\). The shadow carriers form the
oppositely indexed strict flag

\[
 B_{p-1}\subset B_{p-2}\subset\cdots\subset B_1,
\qquad |B_r|=m-r,
\tag{2.2}
\]

because on passing from \(r\) to \(r-1\), one inactive singleton becomes
an active two-block, adding one bank coordinate.

More transparently, the decorated target chain itself satisfies

\[
 U^\kappa_{p-r}
 =B_r\setminus\kappa(X_r),
\tag{2.3}
\]

and extending the source interval by one phase restores one core
coordinate and adds one bank coordinate. Hence consecutive target ranks
differ by two and the target sets are nested.

The all-depth choice at one endpoint is therefore controlled by the
single ordered injection flag

\[
 \kappa(X_1)\subset\kappa(X_2)\subset\cdots
 \subset\kappa(X_{p-1}).
\tag{2.4}
\]

This is a genuine compression from \(p-1\) unrelated target choices to
one partial permutation flag. It does not, however, collapse to the first
and last members of the flag.

## 3. Exact failure of endpoint-row determination

Assume \(p\ge4\), and fix an intermediate value

\[
 2\le r\le p-2.
\tag{3.1}
\]

Choose

\[
 a\in X_1,\qquad
 b\in X_r\setminus X_1,\qquad
 z\in X_{p-1}\setminus X_r,\qquad
 y\in B\setminus X_{p-1}.
\tag{3.2}
\]

These four bank coordinates are distinct. Start with any injection
\(\kappa:B\hookrightarrow K\). Define \(\kappa'\) by exchanging the two
image pairs

\[
 \kappa(a)\leftrightarrow\kappa(b),
\qquad
 \kappa(z)\leftrightarrow\kappa(y),
\tag{3.3}
\]

and fixing every other image.

### Theorem 3.1 (same interior, different two endpoints)

For the suffix flag above,

\[
 \boxed{
 \kappa'(X_r)=\kappa(X_r),
 }
\tag{3.4}
\]

but

\[
 \boxed{
 \kappa'(X_1)\ne\kappa(X_1),
 \qquad
 \kappa'(X_{p-1})\ne\kappa(X_{p-1}).
 }
\tag{3.5}
\]

Consequently the two legal decorations have the same depth-\((p-r)\)
target at this endpoint, while both their deepest-row target
\((r=1)\) and singleton-row target \((r=p-1)\) are different.

#### Proof

Both \(a,b\) lie in \(X_r\), so their image exchange preserves the image
set of \(X_r\). Neither \(z\) nor \(y\) lies in \(X_r\), so the second
exchange also leaves that image set fixed. This proves (3.4).

The singleton \(X_1=\{a\}\) contains \(a\) but not \(b\), so its image
changes. The large set \(X_{p-1}\) contains \(z\) but not \(y\), so its
image set changes under the second exchange; the first exchange is
internal to \(X_{p-1}\) and does not cancel this change. Formula (2.3)
turns these image-set statements into the corresponding target
statements. \(\square\)

Thus there is no function

\[
 \text{intermediate target}
 =
 f(\text{singleton target},\text{deepest target})
\tag{3.6}
\]

or conversely which would make the two endpoint rows an exact substitute
for the interior rows. More importantly for matching, avoiding equality
on the singleton and deepest rows does not algebraically forbid equality
at an intermediate row.

## 4. A physical two-ring realization of the obstruction

The obstruction is not confined to comparing two decorations of one
private ring vertex. For sufficiently large \(n\), it can be realized by
two owner-disjoint coordinate-labelled queue rings.

Start with the two decorations in Theorem 3.1 and their common
intermediate target \(S\). Apply to the second decorated ring a coordinate
permutation from the stabilizer

\[
 \operatorname{Sym}(S)\times\operatorname{Sym}([n]\setminus S).
\tag{4.1}
\]

A generic such permutation:

1. keeps the intermediate target equal to \(S\);
2. avoids all \(O(p^2)\) equalities between the two singleton inventories;
3. avoids all \(O(p^2)\) equalities between the two deepest inventories;
4. avoids all \(O(p^2)\) equalities between their owner vertices.

To justify existence, every owner has at least

\[
 m-|S|=2r\ge4
\]

coordinates outside \(S\), so its orbit under (4.1) has polynomial size
at least order \(n^4\). The singleton and deepest targets have ranks
different from \(|S|\); their nontrivial inside/outside parts give orbits
of order at least \(n^2\). Each forbidden equality occupies one coset of
the corresponding stabilizer and hence an \(O(n^{-2})\) fraction at
worst. Since \(p^2=O(n)\), the union of all forbidden fractions is
strictly less than one for large \(n\) after choosing the inside and
outside permutations successively. Therefore an avoiding permutation
exists.

Coordinate relabelling preserves the queue equations, ranks, and gauge
legality. The two resulting rings are owner-disjoint and have disjoint
singleton and deepest target rows, but share \(S\) at the chosen
intermediate depth.

## 5. Exact remaining formulation

The nested-depth structure should be used as a **flag constraint**, not
discarded:

\[
 \boxed{
 \text{one endpoint contributes one nested carrier/deletion flag.}
 }
\tag{5.1}
\]

A proof may select injections by an ordered-flag matching or a laminar
flow rather than treating the \(p-1\) rows independently. But it must
still prevent equality at every internal flag node. Matching only the
singleton and deepest rows is not sufficient.

Together with the decoration-configuration theorem, the all-depth gate is
therefore:

> Select one injection flag per chosen owner ring so that no two of the
> \(3p\) endpoint flags share a node at any rank.

The shadow locality (1.8) and the nested domains (2.1) are the available
structure for that theorem. Its existence remains open.
