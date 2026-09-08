# Triple-zero promoted ports obey an exact cyclic-moment velocity law

**Date:** 2026-08-05  
**Method:** cyclic weak-composition moment and PBBS action-angle velocity;
no search  
**Status:** unconditional.  The theorem gives a concrete obstruction to
deducing monotone physical port order from the positive triple-zero angle
rail alone.

## 1. Cyclic moment

Let a promoted hook torus have `Q` vacancy slots and `B` chips.  Write a
rooted angle as

\[
 z=(z_0,\ldots,z_{Q-1}),
 \qquad z_i\ge0,
 \qquad \sum_i z_i=B.
\tag{1.1}

Define its cyclic first moment

\[
                         M(z)=\sum_{i=0}^{Q-1}i z_i\pmod Q.
\tag{1.2}

The rooted PBBS factor step is

\[
 g(z_0,\ldots,z_{Q-1})=(z_{Q-1},z_0,\ldots,z_{Q-2}).
\tag{1.3}

Every old slot advances by one, so

\[
                         M(gz)-M(z)\equiv B\pmod Q.
\tag{1.4}

More generally,

\[
                         M(g^s z)-M(z)\equiv Bs\pmod Q.
\tag{1.5}

## 2. Moment of the triple-zero rail

Consecutive promoted ports on one cool-lex sibling rail differ locally by

\[
 A0001B\longrightarrow A0010B\longrightarrow
 A0100B\longrightarrow A1000B.
\tag{2.1}

In the weak-composition encoding, the complete three-step move carries
one chip from the vacancy bank after the displayed third zero to the bank
before the displayed first zero.  It therefore moves that chip backward by
three cyclic slots.  If the endpoint rooted compositions are `z,z'`, then

\[
                         M(z')-M(z)\equiv-3\pmod Q.
\tag{2.2}

The sign agrees with the convention (1.3): the chip in (2.1) moves left,
whereas positive PBBS time moves slot indices right.

### Theorem 2.1 (same-torus port velocity)

Suppose the two endpoint ports of (2.1) lie on the same unmarked promoted
PBBS torus.  If their directed factor-time separation is `s`, so that the
second rooted port is `g^s` of the first modulo its rotational stabilizer,
then

\[
                         \boxed{Bs\equiv-3\pmod Q.}
\tag{2.3}

For fixed rooted endpoints, `s` is unique modulo the rooted orbit length.

### Proof

Equations (1.5) and (2.2) compute the same moment difference.  Their
equality gives (2.3).  For the fixed pair of rooted endpoints, two time
shifts carrying the first to the second differ by a stabilizer period,
proving the last statement.  `square`

### Corollary 2.2

If `gcd(B,Q)=1`, then along any run of sibling ports which all lie on one
promoted torus, their directed PBBS times form an arithmetic progression
with the unique step

\[
                         s\equiv-3B^{-1}\pmod Q.
\tag{2.4}

In general, existence of a same-torus endpoint pair forces
`gcd(B,Q)` to divide three.  When the gcd is three, (2.3) has three residue
classes modulo `Q`; the actual rooted endpoints select one, and different
successive pairs are not proved to select the same class.  Thus the order
still requires occurrence data beyond the geometric rail.

For `B=1`, one has

\[
                         s\equiv-3\pmod Q.
\tag{2.5}

Thus even the unique one-chip promoted component encounters successive
triple-zero ports three vacancy phases in the negative PBBS direction, not
one phase in the positive direction.

## 3. Why an arbitrary cyclic order is insufficient

Let a child sibling path have odd length `E=2r+1`, and retain the child
contour permutation

\[
 \pi=\beta\alpha
 =(1,2,4,6,\ldots,2r,2r+1,2r-1,\ldots,3).
\tag{3.1}

If a third-shore cycle encounters edge labels by the two-step translation

\[
                         \gamma_2(j)=j+2\pmod E,
\tag{3.2}

then every odd label `3,5,...,2r+1` is fixed by

\[
                         \gamma_2\pi.
\tag{3.3}

Indeed, `pi(2k+1)=2k-1`, and `gamma_2(2k-1)=2k+1`.  Hence

\[
                         c(\gamma_2\pi)\ge r
                         ={E-1\over2}.
\tag{3.4}

So a generic arithmetic third-shore order can create linearly many return
contours.  The bounded return proved for `gamma=(1 2 ... E)` is genuinely
order-sensitive.

Equation (3.4) is an abstract permutation warning; it does not assert that
the exact translation (3.2) occurs for every PBBS parameter.  The physical
orders which do occur must be computed from (2.3) and the actual subset of
ports on each torus.

## 4. Revised recursive port invariant

A proof of the all-`b` contour theorem must carry more than the statement
that promoted ports are joined by positive angle-graph paths.  At minimum
it must retain, for every repeated parent torus:

1. the chip mass `B` and vacancy length `Q`;
2. the marked-port factor times determined by (2.3);
3. the cyclic interval order in which different parent tori are spliced;
   and
4. the orientation of every clean-C6 reconnection.

Equivalently, a successful **port-preserving splice invariant** must show
that the final physical third-shore permutation is monotone (or another
explicit bounded-return permutation) after these arithmetic native orders
are concatenated.  The local triple-zero rail and the sign `g=+1` do not
establish that statement by themselves.

This theorem is not a no-go for an actively reordering recursive splice.
It is a no-go for the inference

\[
 \text{positive angle rail}\Longrightarrow
 \text{monotone physical }\gamma.
\]

No q3, source-decoration, residence, upper, common-cap, or all-`k` claim is
included.
