# Cyclic SCD promotion: the exact opposite-corner cocycle

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## Audit correction

Two scopes in the original formulation below were too strong.  The corrected
statements, with proofs, are in
`MATH_ATTACK_S_OUTER_CYCLIC_SCD_PROMOTION_20260726.md`.

1. If radius-zero middle owners may close/reset the forced paths, the exact
   depth-one condition is that

   \[
       G_1:\mathcal A_1\longrightarrow\binom{[2m]}m
   \]

   be injective and hence extendable to a permutation of the whole middle
   layer.  It need not map \(\mathcal A_1\) onto itself.  The complement
   extension uses exactly \(W-N_1=W/(m+1)\) abstract reset transitions.
   Consequently the ordered-potential acyclicity in Section 5 rules out a
   no-reset cyclic core, but does not alone rule out \(o(W)\) reset closure.
2. An unweighted one-step cocycle-defect count is not the aggregate rooted
   flag ledger asserted in (7.2).  A defect at offset \(j\) can propagate
   to \(H-j\) preceding roots.  One must use the actual rooted flag defect,
   or a safe weighted ledger such as

   \[
                         \sum_{j=1}^{H-1}(H-j)E_j.
   \]

Also, Proposition 3.1 is one unit weak: a shift-consistent cycle of length
\(L\) cannot contain an owner of radius at least \(L\), since
\(G_L(X)\ne X\).

## 0. Outcome

Let \(\mathscr S\) be an SCD of \(B_{2m}\).  For a middle owner \(X\) whose
chain has radius at least \(q\), write

\[
 D_q(X)\subset\cdots\subset D_1(X)\subset X
 \subset E_1(X)\subset\cdots\subset E_q(X),           \tag{0.1}
\]

and let \(\delta_j(X)\), \(\eta_j(X)\) be its ordered deletion and
insertion labels.  Define the depth-\(q\) opposite middle corner

\[
 \boxed{
 G_q(X)=D_q(X)\cup(E_q(X)\setminus X)
       =X-\{\delta_1,\ldots,\delta_q\}
          +\{\eta_1,\ldots,\eta_q\}.}                \tag{0.2}
\]

Put \(G_0(X)=X\).

The desired SCD promotion is completely forced at depth one:

\[
                         P(X)=G_1(X).                  \tag{0.3}
\]

There is therefore no separate rowmotion choice which can repair an
incompatible SCD.  The exact higher-depth condition is the partial semigroup
law

\[
 \boxed{
 G_1(G_t(X))=G_{t+1}(X)\qquad(0\le t<q),}             \tag{0.4}
\]

together with \(G_t(X)\) having residual radius at least \(q-t\).  Equivalently,

\[
 \delta_j(G_tX)=\delta_{t+j}(X),\qquad
 \eta_j(G_tX)=\eta_{t+j}(X)                           \tag{0.5}
\]

whenever \(t+j\le q\).  Thus the nested SCD flags are shift-consistent
through depth \(H\) if and only if the maps \(G_q\) are the first \(H\)
iterates of the single middle map \(G_1\), on their forced domains.

This gives the requested cocycle obstruction.  At depth two it is already

\[
 \boxed{
 G_1^2(X)=G_2(X),\quad\text{equivalently}\quad
 (\delta_1(G_1X),\eta_1(G_1X))
   =(\delta_2(X),\eta_2(X)).}                         \tag{0.6}
\]

The four-coordinate cyclic SCD satisfies (0.4) exactly.  The standard
BTK/Greene--Kleitman product SCD fails before (0.6): its map \(G_1\) strictly
increases a global potential and hence has no cyclic core.  Boolean
rowmotion and fixed-order toggle promotion are complementation, not Johnson
moves, and Schuetzenberger promotion likewise has explicit middle words on
which it is a macroscopic move.  None can be the forced operator (0.3).

For a product/quartet recursion, the cocycle has a concrete shuffle form.
If \(\sigma_X(j)\) records which child supplies the \(j\)-th lower and upper
flag labels, then every promotion edge must satisfy

\[
                         \sigma_{G_1X}(j)=\sigma_X(j+1).          \tag{0.7}
\]

The product of these tail-shift identifications around every middle-owner
cycle must have trivial holonomy.  A fixed nonconstant product shuffle
cannot satisfy (0.7); the \(B_4\) seed succeeds because its four local
shores form a zero-holonomy cycle.  The unresolved recursion theorem is
exactly a contextual quartet resolver whose seam transitions make this
shuffle cocycle trivial while preserving the global SCD radius census.

## 1. SCD flags and opposite corners

Let

\[
 \mathcal A_q=
 \{X\in\tbinom{[2m]}m:\rho(X)\ge q\}.                \tag{1.1}
\]

The SCD rank census gives

\[
                         |\mathcal A_q|=\binom{2m}{m-q}=N_q.     \tag{1.2}
\]

For \(X\in\mathcal A_q\), define labels by

\[
 \delta_j(X)=D_{j-1}(X)\setminus D_j(X),\qquad
 \eta_j(X)=E_j(X)\setminus E_{j-1}(X),                \tag{1.3}
\]

where \(D_0(X)=E_0(X)=X\).  The labels in each of the two words are
distinct, all \(\delta_j(X)\) belong to \(X\), and all \(\eta_j(X)\) lie
outside \(X\).

The interval \([D_q(X),E_q(X)]\) has \(2q\) free coordinates.  Its middle
rank contains the opposite corner (0.2).  In particular,

\[
 G_1(X)=X-\delta_1(X)+\eta_1(X)                       \tag{1.4}
\]

is the alternative middle corner of the first SCD diamond.

Suppose a middle permutation \(P\) realizes the SCD's first lower and upper
flags as its one-edge intersection and union.  Then

\[
 X\cap P(X)=D_1(X),\qquad X\cup P(X)=E_1(X).          \tag{1.5}
\]

The two equations uniquely determine \(P(X)\), and their solution is
\(G_1(X)\).  This proves (0.3): a promotion compatible with the given SCD
cannot be chosen independently of its diamond map.

## 2. Exact shift-consistency theorem

Call a partial middle permutation \(P\) **SCD-shift-consistent through
depth \(H\)** if, for every \(X\in\mathcal A_q\), \(q\le H\), and every
\(0\le t<q\),

\[
 \begin{aligned}
 \delta_j(P^tX)&=\delta_{t+j}(X),\\
 \eta_j(P^tX)&=\eta_{t+j}(X)
 \end{aligned}
 \qquad(1\le j\le q-t).                              \tag{2.1}
\]

The equations include the assertion \(P^tX\in\mathcal A_{q-t}\).

### Theorem 2.1 (opposite-corner semigroup criterion)

The following are equivalent.

1. The SCD admits an SCD-shift-consistent middle permutation through depth
   \(H\).
2. The map \(G_1\) is a permutation of \(\mathcal A_1\), and for every
   \(X\in\mathcal A_q\), \(q\le H\),

   \[
    G_t(X)\in\mathcal A_{q-t},\qquad
    G_1(G_t(X))=G_{t+1}(X)\quad(0\le t<q).            \tag{2.2}
   \]

3. On the same domains,

   \[
                              G_t(X)=G_1^t(X)          \tag{2.3}
   \]

   and the residual radius condition in (2.2) holds.

When these conditions hold, the permutation is uniquely \(P=G_1\) on
\(\mathcal A_1\).  It may be extended arbitrarily on the
\(W-N_1=o(W)\) radius-zero middle owners.

#### Proof

If \(P\) is shift-consistent, Section 1 gives \(P=G_1\).  Iterating (2.1)
shows

\[
 P^tX
 =X-\{\delta_1(X),\ldots,\delta_t(X)\}
    +\{\eta_1(X),\ldots,\eta_t(X)\}
 =G_t(X),                                             \tag{2.4}
\]

and proves (2.2)--(2.3).

Conversely, suppose (2.2) holds and put \(Y=G_t(X)\).  The two middle sets
\(Y\) and \(G_{t+1}(X)\) differ in exactly the directed Johnson swap

\[
                         \delta_{t+1}(X)\longmapsto\eta_{t+1}(X). \tag{2.5}
\]

Indeed the earlier \(t\) deletions and insertions occur in both.  But
\(G_1(Y)\) is obtained from \(Y\) by the unique directed swap
\(\delta_1(Y)\mapsto\eta_1(Y)\).  Equality in (2.2) therefore forces

\[
 \delta_1(G_tX)=\delta_{t+1}(X),\qquad
 \eta_1(G_tX)=\eta_{t+1}(X).                         \tag{2.6}
\]

Apply the same argument after replacing \(X\) by \(G_tX\), and induct on
the remaining depth.  This gives every equation in (2.1).  The equivalence
of (2.2) and (2.3) is ordinary induction. \(\square\)

Thus the exact obstruction is not a vague failure of nesting.  It is the
failure of a finite family of literal set identities (2.2).

## 3. The cocycle and its first obstruction

Define the partial semigroup defect

\[
 \mathfrak c_{s,t}(X)
 =G_s(G_t(X))\mathbin\triangle G_{s+t}(X),            \tag{3.1}
\]

whenever both terms are defined.  The SCD promotion cocycle vanishes through
depth \(H\) exactly when

\[
                         \mathfrak c_{s,t}(X)=\varnothing
                         \qquad(s+t\le H).            \tag{3.2}
\]

It is enough to check the generators \(\mathfrak c_{1,t}\), together with
the residual radius domains.  The first nontrivial one is

\[
 \mathfrak c_{1,1}(X)
 =G_1^2(X)\mathbin\triangle G_2(X).                  \tag{3.3}
\]

In flag labels, it vanishes precisely when (0.6) holds.  This is a finite
four-rank test involving only the SCD chains through \(X\) and \(G_1X\).

There is also a coordinate-valued one-cocycle on every orbit:

\[
 \omega(X)=e_{\eta_1(X)}-e_{\delta_1(X)}\in\mathbb Z^{[2m]},
 \qquad \mathbf1_{G_1X}-\mathbf1_X=\omega(X).         \tag{3.4}
\]

If \(X_0,\ldots,X_{L-1}\) is a \(G_1\)-cycle, telescoping gives

\[
                         \sum_{t=0}^{L-1}\omega(X_t)=0.          \tag{3.5}
\]

Thus the deletion and insertion labels have equal multisets around every
cycle.  This is only the zero-holonomy condition at depth one.  A physical
\(C_{2h}\)-strip requires the stronger ordered identities

\[
 L=2h,qquad
 \delta_1(X_t)=z_t,qquad
 \eta_1(X_t)=z_{t+h},                                 \tag{3.6}
\]

with all \(z_t\) distinct, while full SCD coherence requires

\[
 \delta_j(X_t)=z_{t+j-1},\qquad
 \eta_j(X_t)=z_{t+h+j-1}.                             \tag{3.7}
\]

Hence vanishing of the abelian sum (3.5) does not remove the ordered
cocycle (3.1).

### Proposition 3.1 (short-cycle holonomy obstruction)

If an SCD-shift-consistent \(G_1\)-cycle has length \(L\), then no owner on
it can have radius at least \(L+1\) within the certified range.

#### Proof

If \(X\in\mathcal A_{L+1}\), equation (2.1) and \(G_1^LX=X\) give

\[
                         \delta_1(X)=\delta_{L+1}(X),
\]

contradicting distinctness of the deletion labels in one SCD chain.
\(\square\)

Thus a promotion factor intended for depth \(H\) cannot place a
radius-\(H\) owner on a cycle shorter than \(H\).  The intended physical
cycle length \(2h\), with \(H<h\), automatically clears this obstruction.

## 4. Product-shuffle form of the cocycle

Suppose the SCD is assembled from child chain systems.  At a middle owner
\(X\), record which children supply its successive lower and upper labels:

\[
 \sigma_X(j)=
 \bigl(c^-(\delta_j(X)),c^+(\eta_j(X))\bigr).          \tag{4.1}
\]

This is the product-chain shuffle word, with a two-sided child label at each
depth.

### Proposition 4.1 (shuffle cocycle)

SCD shift consistency implies

\[
                         \sigma_{G_1X}(j)=\sigma_X(j+1)           \tag{4.2}
\]

for every certified \(j\).  Conversely, (4.2), together with the analogous
local child-label shifts inside the indicated children, is equivalent to
the flag equations (2.1).

#### Proof

Project the two label equalities in (2.1) to their child indices.  This
gives (4.2).  If both the child indices and the literal child labels agree,
the original labels agree, giving the converse. \(\square\)

Equation (4.2) is a groupoid cocycle: an edge \(X\to G_1X\) identifies the
protected flag word at its head with the one-letter tail of the word at its
tail.  Around a cycle, the composite identification must return the initial
word with trivial holonomy.

### Corollary 4.2 (fixed-shuffle obstruction)

Suppose a product rule assigns the same protected shuffle word \(\sigma\)
to every middle center in a proposed \(G_1\)-component.  If that component
is shift-consistent through depth \(H\), then

\[
                         \sigma(1)=\sigma(2)=\cdots=\sigma(H).   \tag{4.3}
\]

Thus a fixed product priority which uses two different child types in its
protected prefix cannot be shift-consistent.

#### Proof

Equation (4.2) becomes \(\sigma(j)=\sigma(j+1)\). \(\square\)

This isolates why an ordinary tensor SCD cannot be repaired merely by
calling its fixed factor order “promotion.”  A successful product theorem
must change the shuffle with the owner context so that each promotion step
literally shifts it, and the changes must close with zero holonomy around
every owner cycle.

## 5. Standard named dynamics

The exact equation (0.3) excludes the standard named operators before any
higher-depth test.

1. Regard \(B_{2m}\) as the order-ideal lattice of a \(2m\)-element
   antichain.  Rowmotion sends an ideal to the ideal generated by the
   minimal elements of its complement, hence sends \(X\) to \(X^c\).
   Fixed-order toggle promotion has the same effect.  For \(m>1\), this is
   not a Johnson neighbour of \(X\).
2. Schuetzenberger promotion on the two-row tableau encoding preserves SCD
   radius, but on the explicit rectangular family its induced middle words
   have Hamming distance \(2m-2\).  It is a macro move, not (1.4).
3. For the fixed-priority BTK/Greene--Kleitman SCD, the alternative-corner
   move replaces a lower-priority star coordinate by a higher-priority one.
   The sum of the selected coordinate priorities strictly increases.
   Therefore \(G_1\) is acyclic and cannot be a permutation on
   \(\mathcal A_1\).

The failure of item 3 affects \(1-o(1)\) middle owners: only the Catalan
many radius-zero centers avoid the positive-radius alternative-corner
dynamics.  Consequently no standard fixed-priority product SCD supplies an
approximate cyclic promotion by leaving only \(o(W)\) owners untreated.

## 6. The quartet seed is an exact local solution

On \([4]\), use the SCD

\[
\begin{array}{ccl}
 \varnothing&\subset&1\subset14\subset124\subset1234,\\
 2&\subset&12\subset123,\\
 3&\subset&23\subset234,\\
 4&\subset&34\subset134,\\
 &&13,\\
 &&24.
\end{array}                                           \tag{6.1}
\]

Its nontrivial middle centers form

\[
                         14\longrightarrow12\longrightarrow23
                         \longrightarrow34\longrightarrow14.   \tag{6.2}
\]

At the unique radius-two center,

\[
 \begin{aligned}
 (\delta_1(14),\eta_1(14))&=(4,2),\\
 (\delta_2(14),\eta_2(14))&=(1,3).
 \end{aligned}                                        \tag{6.3}
\]

At its successor \(12\),

\[
                         (\delta_1(12),\eta_1(12))=(1,3).        \tag{6.4}
\]

Thus \(G_1^2(14)=G_2(14)=23\), and the depth-two cocycle vanishes.  The
other three cycle centers have radius one, so there are no further local
conditions.  This proves the full semigroup criterion at every available
depth.  Moreover the deletion word \(4,1,2,3\) and insertion word
\(2,3,4,1\) satisfy the antipodal shift, so (6.2) is a physical \(C_4\).

The seed proves that the cocycle obstruction is not universal.  What it
does not supply is a product rule with zero seam holonomy on almost all
global owners.

## 7. Exact surviving recursion gate

For a contextual product/quartet SCD, define the sharp one-step flag defect

\[
 \begin{aligned}
 \mathcal E_H^{\rm shift}
 =\sum_{j=1}^{H-1}\big(&
 |\{X\in\mathcal A_{j+1}:
       G_1X\notin\mathcal A_j
       \text{ or }\delta_j(G_1X)\ne\delta_{j+1}(X)\}|\\
 &+
 |\{X\in\mathcal A_{j+1}:
       G_1X\notin\mathcal A_j
       \text{ or }\eta_j(G_1X)\ne\eta_{j+1}(X)\}|
 \big).                                               \tag{7.1}
 \end{aligned}
\]

The direct SCD-promotion route requires

\[
 \boxed{
 |\mathcal A_1\setminus\operatorname{Cyc}(G_1)|
 +\mathcal E_H^{\rm shift}=o(W),}                     \tag{7.2}
\]

followed by the physical antipodal label condition (3.6) on all but
\(o(W)\) owners.  Equation (7.1) counts the literal lower and upper rooted
one-step identities, with no triangular overcount from iterating one bad
edge.  Thus (7.2) is exactly the aggregate shift-cocycle gate; no
independent nested-flow rounding remains after it is proved.

The quartet seed supplies a zero-cocycle local chart.  A tensor construction
must now provide transition charts between different local quartet shores
such that

1. the shuffle identity (4.2) holds through \(H\) at all but \(o(W)\)
   rooted positions;
2. the product of transition charts around every retained owner component
   has trivial ordered holonomy;
3. the global SCD radius census \(|\mathcal A_q|=N_q\) is unchanged; and
4. the resulting \(G_1\)-cycles satisfy the physical antipodal ordering.

This is precisely the contextual four-child cyclic resolver, now expressed
as an explicit cocycle equation.  The existing bounded quartet associators
change local shores with exact owner support, but no theorem currently shows
that their transition cocycles can be chosen to make (7.2) hold.  That is
the remaining outer gate.
