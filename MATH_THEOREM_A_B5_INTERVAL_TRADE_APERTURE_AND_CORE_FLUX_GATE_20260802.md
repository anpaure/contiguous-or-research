# The exact \(B_5\) interval-trade atlas, the one-aperture parity breaker,
# and the cross-core flux gate

**Date:** 2026-08-02  
**Lane:** A, central common-base/reset rounding  
**Status:** exact finite trade theorem and dimension-uniform core-flux
obstruction.  This note does not prove the complementary central bi-packing,
an all-\(m\) connected exchange theorem, residence, upper shadows, source
factorability, common cap, compiler, or a word construction.

## 0. Outcome

The frozen five-coordinate Dong--Mao bank is not circuitless.  Its saturated
rank-\(1/2/3\) fibres have one exact resource-neutral \(C_{10}\) switch.  In
fact, for a fixed outer and oriented middle resource signature, the fibre has
exactly two modes, and that switch is its complete Markov basis.

This positive result has two sharp limitations.

1. Every saturated switch is even: its two middle matchings differ by a
   5-cycle.  It preserves the determinant sign of the tail-to-head matching.
2. The first parity-breaking trade is a \(C_8\), but neither of its phases
   extends to a saturated five-diamond \(B_5\) bank.  It needs one missing
   interval, equivalently one externally supplied aperture/reset socket.

There is also a free, not torsion, obstruction to completing the whole
central palette while all diamonds remain in fixed \(B_5\) fibres.  For every
fixed-core pattern \(P\), the difference

\[
       \#\{\hbox{lower targets over }P\}
       -\#\{\hbox{upper targets over }P\}
\]

is invariant under every fibre-preserving circuit.  Its central demand is
nonzero.  Moreover, after all literal columns with the same ordered core
pair are aggregated, no nonzero palette-preserving simple-core circuit
using a cross-core pair can be supported on only one or two core states.
The first aggregate core circuit is the
three-state rectangle

\[
 [P,P+x]+[P+x,P+x+y]
 -[P,P+x+y]-[P+x,P+x].                              \tag{0.1}
\]

A literal lift of (0.1) leaves one middle Pluecker-square debt.  The
dimension-uniform hub-cycle \(C_6\) and \(C_8\) relations below are exact
ways to close all named resources; the \(C_8\) is also the smallest parity
breaker.  What remains unproved is a supply/connectedness theorem placing
these aperture circuits on one common nonnegative protected table.

## 1. Literal interval resources

Let \(K\) be a five-set.  A rank-\(1/2/3\) Boolean interval is

\[
 I(i;a,b)=[\{i\},\{i,a,b\}],                         \tag{1.1}
\]

with middle vertices \(\{i,a\}\) and \(\{i,b\}\).  A **phase** is a
family of intervals having pairwise distinct lower endpoints, upper
endpoints, and middle vertices.  Two phases form a **complete interval
trade** if their lower palettes, upper palettes, and middle palettes agree.

If the union of the two middle matchings is one even alternating cycle,
choose either bipartition class of that cycle as the tail palette and orient
both phases from that class to the other.  The trade then preserves the
lower, upper, tail, and head rows literally.  Thus every circuit below is a
four-resource circuit, not merely an unoriented interval identity.

Complementation in \(K\) gives the identical statements for the
rank-\(2/3/4\) fibre.

## 2. The saturated fibre is exactly one \(C_{10}\)

### Theorem 2.1 (regular-tournament classification)

There are exactly 24 saturated five-diamond phases between ranks 1 and 3 of
\(B_5\).  They split into 12 complete resource fibres of size two.  In each
fibre the two phases differ by one alternating \(C_{10}\); after a coherent
orientation they have identical lower, upper, tail, and head palettes.

Consequently the unique \(C_{10}\) toggle is a complete Markov basis on
each fixed saturated resource fibre.  Across independent fixed-core fibres,
the product of these toggles connects the complete frozen saturated face.

#### Proof

In a saturated phase, every two-set \(\{i,j\}\) is a middle vertex of
exactly one interval.  Direct the tournament edge \(ij\) from \(i\) to
\(j\) when that middle vertex belongs to the interval with lower endpoint
\(i\).  Every lower endpoint uses two middle vertices, so every tournament
vertex has outdegree two.  Conversely, a regular tournament on five
vertices gives the interval

\[
       [\{i\},\{i\}\cup N^+(i)]                     \tag{2.1}
\]

at each vertex.  Distinct lower vertices give distinct upper triples: if
the closed out-neighbourhood triples of \(i\) and \(j\) were equal, both
arcs \(i\to j\) and \(j\to i\) would be required.

Every regular tournament on five labeled vertices is a cyclic tournament.
Write its cyclic order as \(0,1,2,3,4\), so

\[
 M^+=\{A_iB_i:i\in\mathbb Z_5\},\qquad
 A_i=\{i,i+1\},\quad B_i=\{i,i+2\}.                \tag{2.2}
\]

The same unordered upper-triple palette has exactly the reverse cyclic
orientation.  Its middle matching is

\[
 M^-=\{A_iB_{i-1}:i\in\mathbb Z_5\}.               \tag{2.3}
\]

Thus \(M^+\cup M^-\) is

\[
 A_0B_0A_1B_1\cdots A_4B_4A_0,                    \tag{2.4}
\]

one alternating \(C_{10}\).  An unoriented cyclic order on five labeled
points has \((5-1)!/2=12\) choices, proving the counts.  The two
bipartition classes in (2.4) give the common tail/head orientations.
\(\square\)

### Corollary 2.2 (the saturated sign invariant)

Fix an ordering of the five tails and five heads in one saturated fibre.
Every frozen-fibre \(C_{10}\) toggle preserves the sign of the corresponding
tail-to-head bijection.  Any product of such toggles in one or two frozen
fibres preserves the sign in every fibre.

#### Proof

The relative permutation of (2.2) and (2.3) is a 5-cycle, whose sign is
\((-1)^{5-1}=+1\).  Signs multiply under composition. \(\square\)

This sign is asserted only on a fixed saturated resource fibre with fixed
tail and head sets.  It is not a global invariant after a move exchanges a
tail, head, or core fibre.

## 3. The complete primitive \(B_5\) trade atlas

### Theorem 3.1 (\(C_6/C_8/C_{10}\) classification)

After common unchanged intervals are cancelled, every nonzero complete
trade between pairwise-disjoint rank-\(1/2/3\) phases of \(B_5\) is one of:

\[
\begin{array}{c|c|c|c}
\text{phase size}&\text{alternating support}&
 \text{labeled trade pairs}&\text{relative sign}\\ \hline
3&C_6&20&+1\\
4&C_8&15&-1\\
5&C_{10}&12&+1.
\end{array}                                         \tag{3.1}
\]

There is no one-for-one or two-for-two complete trade.  Every \(C_6\) or
\(C_8\) phase fails to extend to a saturated five-diamond phase.  Every
\(C_6\) phase extends to size four, but no further.  Thus exactly one
fibre aperture is necessary before either the \(C_6\) or the parity-breaking
\(C_8\) can be used.

#### Proof

The union of two middle matchings with the same middle palette is a disjoint
union of even alternating cycles.  A nontrivial \(C_4\) is impossible.
Indeed, if two distinct lower singletons \(i,j\) can both be paired with two
distinct upper triples \(U,V\), then \(i,j\in U\cap V\).  Since \(U,V\)
are distinct triples, the only possible cross-pairing case has
\(U\cap V=\{i,j\}\).  But then the two intervals in either phase share the
middle vertex \(\{i,j\}\), contradicting that the phase is a bank.

There are only ten middle vertices, so after common edges are cancelled a
connected primitive support can only have length 6, 8, or 10.  Representatives
of the first two are the following hub-cycle identities.  For a common base
\(R\), a hub \(h\), and cyclically ordered distinct rim coordinates
\(a_0,\ldots,a_{r-1}\), put

\[
\begin{aligned}
 {cal P}^+_r&=\{[R+a_i,R+h+a_i+a_{i+1}]:i\in\mathbb Z_r\},\\
 {cal P}^-_r&=\{[R+a_i,R+h+a_{i-1}+a_i]:i\in\mathbb Z_r\}.
                                                               \tag{3.2}
\end{aligned}
\]

For \(r=3\) this is a \(C_6\), and for \(r=4\) it is a \(C_8\).  Both
phases use the same lower sets, upper sets, and the same middle sets

\[
       \{R+h+a_i:i\in\mathbb Z_r\}
       \mathbin{\dot\cup}
       \{R+a_i+a_{i+1}:i\in\mathbb Z_r\}.           \tag{3.3}
\]

Their relative permutation is an \(r\)-cycle, giving the signs in (3.1).
The \(C_{10}\) case is Theorem 2.1.

For a \(C_6\) inside \(B_5\), let \(w\) be the fifth coordinate outside
the hub and three rims.  The unused middle vertices are the four pairs
\(\{w,v\}\) with \(v\ne w\).  The two unused lower singletons are \(h,w\).
At most one more interval can be formed from those four middle vertices, so
the phase cannot reach size five.  For a \(C_8\), the omitted lower is the
hub and the two unused middle pairs do not contain the hub, so no fifth
interval exists at all.

The statements that there are exactly 20, 15, and 12 labeled pairs are a
finite \(B_5\) classification.  The independent exhaustive audit listed in
Section 7 checks all 30 intervals and all disjoint phases.  It also finds
120 size-four trades obtained by adjoining one common unchanged interval to
a \(C_6\); cancelling that interval recovers the primitive list above.
\(\square\)

### Corollary 3.2 (sharp scoped impossibility for the frozen bank)

The saturated five-fibre Dong--Mao bank admits the \(C_{10}\) atlas of
Theorem 2.1 but no \(C_6\) or \(C_8\) move wholly inside a saturated fibre.
Therefore its frozen-fibre exchange graph cannot change the selected outer
palettes or the saturated determinant sign.  Any parity-breaking absorber
must reserve at least one aperture and use a \(C_8\), or exchange a middle
role with another fibre.

This is a no-go only for the saturated frozen-fibre face.  It is not a
no-go for cross-fibre hub cycles or for a jointly selected two-bank table.

### Corollary 3.3 (the \(C_6+C_{10}\) parity no-go)

Fix any oriented named-resource fibre, so every phase is a bijection from
the same tail palette to the same head palette.  Every literal hub
\(C_6\) move and every saturated \(C_{10}\) move preserves the sign of this
bijection.  Hence an atlas containing only \(C_6\) and \(C_{10}\) circuits
is not circuit-complete whenever both signs occur.  The one-aperture
\(B_5\) \(C_8\) fibre is the smallest explicit obstruction: its two modes
have the same four named resource palettes and opposite signs, but no
sequence of \(C_6/C_{10}\) moves connects them.

#### Proof

On an alternating \(C_{2r}\), the relative tail-to-head permutation of the
two phases is an \(r\)-cycle and has sign \((-1)^{r-1}\).  Thus \(r=3\)
and \(r=5\) are even moves, whereas \(r=4\) is odd.  Sign is multiplicative
under overlapping as well as disjoint replacements, provided the named
tail and head palettes remain fixed.  Theorem 3.1 supplies a literal
\(C_8\) resource fibre and proves there is no smaller trade. \(\square\)

## 4. The free core-flux obstruction

Return to the central levels of \(B_{2m}\), and split

\[
                 [2m]=H\mathbin{\dot\cup}K,\qquad |K|=5.       \tag{4.1}
\]

For each \(P\subseteq H\), put

\[
 j(P)=m-1-|P|,qquad
 \lambda_P=\binom5{j(P)},\qquad
 \upsilon_P=\binom5{j(P)+2}.                       \tag{4.2}
\]

These are the numbers of rank-\((m-1)\) lower targets and rank-\((m+1)\)
upper targets whose intersection with \(H\) is exactly \(P\).

### Theorem 4.1 (Smith form of the frozen-fibre outer rows)

Modulo all fibre-preserving interval columns and all fibre-preserving
circuits, the outer-palette lattice has one free integer coordinate

\[
                   \kappa_P=L_P-U_P                  \tag{4.3}
\]

for every core pattern \(P\).  There is no torsion in this quotient.  The
full central target has

\[
 \kappa_P^{\rm target}=\lambda_P-\upsilon_P.         \tag{4.4}
\]

For \(j=-2,-1,0,1,2,3,4,5\), these values are

\[
                    -1,-5,-9,-5,5,9,5,1.            \tag{4.5}
\]

Hence no collection of frozen-fibre banks and frozen-fibre circuits can
complete both central outer palettes.

#### Proof

At the aggregate core level, every fibre-preserving interval contributes
the column \(e_P^L+e_P^U\).  The Smith form of the two-by-one block
\((1,1)^T\) is one nonzero diagonal entry 1 and one free cokernel generator
\(L_P-U_P\).  Blocks for distinct \(P\) are a direct sum.  This proves
(4.3) and the absence of torsion.  Substituting the exact binomial counts
gives (4.4)--(4.5). \(\square\)

The five-fibre bank uses loop intervals only and therefore has zero
\(\kappa\)-boundary.  Its residual palette has the same nonzero boundary
(4.5).  This is why its exact internal circuit atlas cannot by itself
complete the remaining quarter.

## 5. Three core states are necessary, but not yet sufficient

A general interval has lower core \(P=L\cap H\) and upper core
\(Q=U\cap H\), where

\[
                       P\subseteq Q,qquad |Q-P|\le2.             \tag{5.1}
\]

At the aggregate level it contributes \(e_P^L+e_Q^U\), and its core flux
is \(e_P-e_Q\).  Thus cross-fibre intervals turn (4.4) into an exact
transport boundary problem.

For a signed literal interval vector \(z\), define its **simple ordered-core
projection** by

\[
       \pi(z)_{P,Q}
       =\sum_{I:\,(L(I)\cap H,U(I)\cap H)=(P,Q)}z_I.            \tag{5.2}
\]

Thus all literal columns with the same ordered core pair are aggregated
before the core incidence kernel is considered.  In particular,
\(\pi(z)=0\) may conceal differences of parallel cross-core columns; the
core projection makes no assertion about such a literal circuit.

### Proposition 5.1 (three states for a nonzero simple-core circuit)

Let \(z\) preserve the aggregate lower- and upper-core palettes.  If
\(\pi(z)\ne0\) and its projection uses a cross-core pair, then the union of
the core states occurring in \(\pi(z)\) has size at least three.  This is
sharp: the first simple-core circuit is the three-state rectangle (0.1).

No claim is made when \(\pi(z)=0\).  Such a vector may be a nonzero literal
two-state circuit obtained by exchanging aggregate-parallel columns, and
must be tested on the full named-resource matrix.

#### Proof

Work in the simple bipartite graph with one edge for each allowed ordered
core pair.  For two incomparable states, its only edges are the two loops.
For comparable states
\(P\subsetneq Q\), the bipartite support on
lower copies and upper copies consists of

\[
                 P_LP_U,\quad P_LQ_U,\quad Q_LQ_U,              \tag{5.3}
\]

whenever the cross edge satisfies (5.1).  This support is a tree and its
signed incidence kernel is zero.  Because (5.2) has already summed every
family of aggregate-parallel literal columns, this proves the claim for
\(\pi(z)\ne0\).  On
\(P\subset P+x\subset P+x+y\), the four columns in (0.1) form the first
bipartite rectangle. \(\square\)

The core rectangle is only an aggregate circuit.  Its most economical
literal lift exposes the remaining nonlinear gate.  Let \(|R|=m-2\),
\(R\cap H=P\), choose distinct \(x,y\in H-R\), and choose distinct
\(k,a\in K-R\).  Put

\[
\begin{array}{ll}
 L_0=R+k,&L_1=R+x,\\
 U_0=R+k+x+a,&U_1=R+k+x+y.
\end{array}                                          \tag{5.4}
\]

All four intervals \([L_i,U_j]\) exist.  Formally replacing the diagonal
pair by the off-diagonal pair realizes (0.1), but each pair repeats the
common middle vertex \(R+k+x\), so this is not yet a two-interval bank
trade.  After that common occurrence is cancelled algebraically, its
remaining middle-resource debt is

\[
\begin{array}{c|c}
\text{interval}&\text{two middle vertices}\\ \hline
[L_0,U_0]&R+k+x,\ R+k+a\\
[L_1,U_1]&R+k+x,\ R+x+y\\
[L_0,U_1]&R+k+x,\ R+k+y\\
[L_1,U_0]&R+k+x,\ R+x+a.
\end{array}                                          \tag{5.5}
\]

Consequently the diagonal-minus-off-diagonal debt is

\[
 [R+k+a]+[R+x+y]-[R+k+y]-[R+x+a].                   \tag{5.6}
\]

This is one Boolean Pluecker square.  Therefore aggregate core Hall is not
enough: a complete circuit must cancel (5.6), or export it through an
explicit middle socket.

## 6. The exact replacement target

The hub-cycle identities (3.2) remain literal in every ambient Boolean
lattice.  If the active hub/rim coordinates meet both \(H\) and \(K\),
they are genuine cross-fibre circuits and automatically cancel the
Pluecker debt, all outer labels, and both oriented middle palettes.
Consequently:

* a cross-fibre \(C_6\) is the smallest complete signed interval circuit;
* a cross-fibre \(C_8\) is the smallest complete circuit which also breaks
  the saturated matching sign; and
* at least one aperture/reset socket is necessary to realize either circuit
  wholly inside a previously saturated \(B_5\) fibre.  A genuinely
  cross-fibre circuit may itself move that aperture; its joint nonnegative
  feasibility is a separate condition.

This yields the following proof-safe sufficient interface, but not its
supply theorem.

> **Aperture circuit interface.**  First choose one literal complementary
> two-bank table with a protected set of one-aperture fibres.  Require the
> available cross-fibre hub \(C_6/C_8\) circuits to (i) span the required
> core-flux corrections, (ii) contain an odd \(C_8\) generator in every
> saturated sign component which must change, and (iii) cancel every middle
> Pluecker debt on the same nonnegative table.  Then adjoin the internal
> \(C_{10}\) toggles.  On each resulting fixed named-resource fibre these
> circuits are exact legal moves; if their exchange graph is connected,
> they are a circuit-complete absorber.

The final clause--connectedness on one protected nonnegative table--is the
remaining theorem.  Signed span alone does not imply it, and separate
availability of the core, Pluecker, and parity generators does not imply a
common feasible phase.  The common-table Hoffman/reset checks from the
fixed-core theorem must be imposed after the aperture bank is fixed.

## 7. Independent finite audit

The exact \(B_5\) census is replayed by

```text
scratch/a_b5_interval_trade_aperture_20260802/
  audit_a_b5_interval_trade_aperture_20260802.py
  audit.json
```

It enumerates all 30 rank-\(1/2/3\) diamonds and every disjoint phase.  The
phase counts at sizes 1 through 5 are

\[
                       30,270,800,570,24.             \tag{7.1}
\]

There are no trades at sizes 1 or 2; there are 20 primitive \(C_6\), 15
primitive \(C_8\), and 12 \(C_{10}\) pairs.  All 24 maximum phases lie in
12 two-mode signatures.  The script also checks that no \(C_6\) or \(C_8\)
phase extends to size five and emits literal representatives of all three
circuits.
