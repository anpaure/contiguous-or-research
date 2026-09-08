# Greene--Kleitman root rotations give exact hinge C6s, but pair packing has a Catalan parity defect

**Date:** 2026-08-07  
**Status:** unconditional algebraic reduction and exact obstruction.  It
replaces the false private-hinge-transversal hope by a root-rotation circuit
problem.  It does not construct the required higher overlapping circuits.

## 1. The root-rotation graph

Let `D_m` be the Dyck words of semilength `m`.  Define a graph `R_m` on
`D_m` as follows.  For any four Dyck words `A,B,C,D` of total semilength
`m-2`, join

\[
 L=1A1B0C0D,
 \qquad
 R=1A0B1C0D.                                           \tag{1.1}
\]

Write the four displayed bits, in order, as positions

\[
                       \alpha<\beta<\gamma<\delta,
\]

and let `a` be the rank-`(m-2)` word obtained by setting all four of them
to zero.  Then

\[
 L=a+\alpha+\beta,
 \qquad
 R=a+\alpha+\gamma.                                    \tag{1.2}
\]

Conversely, a rank-`(m-2)` word with four unmatched zeros has the unique
factorization

\[
                         0A0B0C0D,
\]

and its two Dyck completions containing the first position are exactly
the two words in (1.1).  Thus the edges of `R_m` are in bijection with
such four-record words, and the edge colour is precisely `a`.

The number of edges is

\[
 |E(R_m)|=[z^{m-2}]C(z)^4
          ={2\over m}{2m\choose m-2}
          ={2(m-1)\over m+2}\operatorname {Cat}_m.     \tag{1.3}
\]

Here the coefficient formula is the standard Lagrange inversion identity
`[z^n]C(z)^k=k/(2n+k) binom(2n+k,n)`.

## 2. The two endpoint hinges

Use the fixed Greene--Kleitman successor matching `t` and the fixed root
facet `X_U=U-\alpha`.  The endpoint `L` has hinge data

\[
 u=\alpha,\quad b=\beta,\quad x=\gamma,\quad y=\delta,
\]

whereas `R` has hinge data

\[
 u=\alpha,\quad y=\beta,\quad b=\gamma,\quad x=\delta.
\]

These are exactly the two cases of the singleton-root hinge theorem.  Put

\[
 X_L=a+\beta,qquad X_R=a+\gamma,qquad Z=a+\delta.      \tag{2.1}
\]

Then the apparent cross-role collisions are identities:

\[
 B_{x,L}=X_R,quad B_{y,L}=Z,quad
 B_{x,R}=Z,quad B_{y,R}=X_L.                          \tag{2.2}
\]

The successor identities give

\[
\begin{aligned}
 t(X_L)&=a+\beta+\delta=:P,\\
 t(X_R)&=a+\beta+\gamma=:Q,\\
 t(Z)&=a+\gamma+\delta=:S.
\end{aligned}                                         \tag{2.3}
\]

## Theorem 2.1 (paired-root hinge circuit)

The two endpoint hinges in (1.1), after coincident edges are identified,
are exactly the alternating incidence six-cycle

\[
 X_L-P-Z-S-X_R-Q-X_L.                                  \tag{2.4}
\]

Its fixed-matching edges are

\[
 X_LP,qquad ZS,qquad X_RQ,
\]

and its cross edges are

\[
 ZP,qquad X_RS,qquad X_LQ.                           \tag{2.5}
\]

After suppression, all three Johnson edges have the same rank-`(m-2)`
intersection colour `a`, and their rank-`m` union colours `P,Q,S` are
distinct.  The two facets `X_L subset L` and `X_R subset R` ticket both
omitted roots.

### Proof

Equations (2.2)--(2.3) are direct substitutions in the two four-edge
hinges.  Removing repeated copies leaves exactly the six edges in
(2.4)--(2.5).  The three suppressed pairs are

\[
 (X_L,Z),\qquad(Z,X_R),\qquad(X_R,X_L),
\]

and every pair has intersection `a`.  Their unions are respectively
`P,S,Q`.  This proves every assertion.  \(\square\)

There is also exact privacy for edge-disjoint root pairs.  The `X` values
are fixed and injective in the roots.  The map `a -> Z` is injective:
in `Z`, the first three displayed zeros and the displayed final one are
the unmatched symbols, so changing that unique unmatched one back to zero
recovers `a`.  Moreover `Z` is not any root facet `X_U`, because adding the
first displayed position still leaves the path negative at the third
record.  Injectivity of `t` then gives privacy of `P,Q,S`.

Consequently, every matching in `R_m` lifts to a resource-disjoint bank of
paired-root alternating `C_6` circuits.

## 3. Exact parity obstruction

Let `inv(U)` be the number of `1`-before-`0` pairs in a Dyck word `U`.
The two endpoints in (1.1) differ by moving one displayed `1` past the
balanced word `B` and one displayed `0`.  Hence

\[
             inv(L)-inv(R)=|B|+1\pmod 2=1.             \tag{3.1}
\]

Thus `R_m` is bipartite by inversion parity.

Put

\[
 d_m=\sum_{U\in D_m}(-1)^{inv(U)}.
\]

The first-return decomposition `U=1A0B`, with `A` of semilength `i`, gives

\[
 d_m=\sum_{i=0}^{m-1}
 (-1)^{m+i(m-1)}d_i d_{m-1-i}.                         \tag{3.2}
\]

Starting from `d_0=1`, this recurrence yields

\[
 d_{2s}=0\quad(s\ge1),
 \qquad
 d_{2s+1}=-\operatorname {Cat}_s.                      \tag{3.3}
\]

Indeed the even assertion follows inductively by pairing the two end
terms and using the vanishing earlier even terms.  For odd index, only
odd--odd products survive after the base term, and `e_s=-d_{2s+1}` obeys

\[
 e_0=1,qquad e_s=\sum_{j=0}^{s-1}e_j e_{s-1-j},
\]

the Catalan recurrence.

## Corollary 3.1 (pair-circuit no-go)

When `m=2s+1`, every matching in `R_m` leaves at least

\[
                         \operatorname {Cat}_s         \tag{3.4}
\]

Dyck roots uncovered.  Therefore a construction using only mutually
resource-disjoint paired-root circuits (2.4) cannot have `O(1)` omission
defect on the odd-semilength subsequence.

### Proof

Any matching in a bipartite graph covers the same number of vertices in
the two shores.  Their size difference is `|d_m|`, which is (3.4) by
(3.3).  Apply Theorem 2.1.  \(\square\)

## 4. Exact remaining circuit lemma

The failed private-transversal target should therefore be replaced by:

> **Higher root-circuit lemma.**  In the fixed GK incidence host, select
> overlapping root-rotation hinges whose total symmetric difference is a
> degree-two alternating factor, tickets all but `O(1)` omitted roots,
> and preserves the required intersection colours.

The overlap must be genuine.  Pairwise disjoint `C_6` circuits cannot
cross the parity defect (3.4).  Equivalently, the next absorber must use a
higher alternating circuit, or a second omission/matching phase that
changes the root-parity balance.  This is an integral obstruction; it is
invisible in the already feasible fractional coloured two-factor.
