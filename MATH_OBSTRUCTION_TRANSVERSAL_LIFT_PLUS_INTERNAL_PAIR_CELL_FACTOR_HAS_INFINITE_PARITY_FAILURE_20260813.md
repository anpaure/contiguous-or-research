# The transversal lift plus internal pair-cell edges has an infinite parity obstruction

**Date:** 2026-08-13  
**Status:** unconditional exact obstruction and exact residual selection
formulation.  It applies even if the internal pair-cell edges are chosen
arbitrarily; Hamiltonicity, residence, and use of whole cells are not
assumed.

## 0. Outcome

Put

\[
 k=2p+1,\qquad R=p+1,\qquad
 \mathcal O={{[k]}\choose {p+1}},\qquad
 \mathcal L={{[k]}\choose p},\qquad
 W=|\mathcal O|=|\mathcal L|.                         \tag{0.1}
\]

Distinguish a sentinel `z` and partition the other `2p` coordinates into
pairs

\[
                         P_i=\{a_i,b_i\},\qquad i\in[p].          \tag{0.2}
\]

Let `H` be any cyclic Hamilton Gray code of `Q_p`, and let `P_H` be its
transversal edge-lift component.  It uses all `2^p` transversal lower
colours exactly once and saturates `2^p` owner vertices.

Suppose every remaining factor edge is internal to a cell of the same pair
structure; equivalently, it has the form

\[
             L\cup\{a_i\}\;--\;L\cup\{b_i\}                    \tag{0.3}
\]

for a lower set `L` empty on `P_i`.  Then an exact owner/lower factor can
exist only if

\[
                         W-2^p\quad\text{is even}.                \tag{0.4}
\]

But, whenever

\[
                         p=2^s-1,\qquad s\ge2,                    \tag{0.5}
\]

Lucas's theorem makes `W=binom(2p+1,p+1)` odd.  Since `2^p` is even,
`(0.4)` fails.

Thus for infinitely many middle layers:

\[
 \boxed{
 \text{transversal lift} + \text{arbitrary internal pair-cell edges}
 \text{ cannot be an exact lower factor}.}                         \tag{0.6}
\]

In particular, transversal lift plus good-cell Hamilton cycles cannot by
itself be the full resident carrier.  At least one genuinely cross-cell
edge or relative absorber is necessary.  The obstruction does not rule out
a bounded cross-cell correction.

## 1. Exact residual colour-choice system

For `L in mathcal L`, let

\[
 E(L)=\{i:L\cap P_i=\varnothing\}.                    \tag{1.1}
\]

### Lemma 1.1

The transversal lower sets are exactly those with `E(L)=varnothing`.  If
`E(L)\ne\varnothing`, the internal pair-cell edges having colour `L` are
exactly

\[
 e(L,i)=\{L\cup\{a_i\},L\cup\{b_i\}\},
                         \qquad i\in E(L).              \tag{1.2}
\]

#### Proof

This is the occupancy identity from the pair-cell lower theorem.  An
internal cell edge flips the chosen endpoint of one singleton pair, so its
intersection is empty on that pair.  Conversely `(1.2)` is a Johnson edge
inside the unique cell obtained by making `P_i` active and retaining every
other occupancy status of `L`.  If no pair is empty, the rank equation
forces `z notin L` and exactly one selected endpoint in every pair, which is
a transversal. \(\square\)

After fixing `P_H`, every nontransversal lower colour must therefore choose
one binary variable

\[
                         x_(L,i)\in\{0,1\},\qquad i\in E(L),       \tag{1.3}
\]

subject to

\[
                         \sum_(i\in E(L))x_(L,i)=1                 \tag{1.4}
\]

and the residual owner-degree equations

\[
 \sum_{(L,i):T\in e(L,i)}x_(L,i)
 =\begin{cases}
   0,&T\in V(P_H),\\
   2,&T\notin V(P_H).
  \end{cases}                                                    \tag{1.5}
\]

These equations are necessary and sufficient for an exact completion
whose nonlift edges are all internal: every variable is already a legal
edge of colour `L`, `(1.4)` uses every residual colour once, and `(1.5)`
gives every residual owner degree two.

This is a three-incidence exact-cover system: a column touches one lower
row and two owner rows.  It is not the ordinary bipartite-flow system used
by unrestricted protected-Ore completion.

## 2. Direction parity

Let

\[
                         N_i=\sum_{L:i\in E(L)}x_(L,i)             \tag{2.1}
\]

be the number of selected residual edges which flip pair `P_i`.

### Lemma 2.1

For every `i`,

\[
                              N_i\equiv0\pmod2.                   \tag{2.2}
\]

#### Proof

Sum the **residual** owner-degree equations `(1.5)` over all owners
containing coordinate `a_i`.  Every right-hand side is either zero or two,
so the sum is even.

An internal edge `(0.3)` contributes one modulo two to this sum exactly
when its direction is `i`: its two endpoints differ on `a_i`.  An internal
edge in any other direction has either zero or two endpoints containing
`a_i`.  The left-hand side of the summed residual equation is consequently
exactly `N_i` modulo two, proving `(2.2)`.  No direction-count property of
the Gray code is needed after the saturated lift has been subtracted and
encoded by the zero capacities in `(1.5)`. \(\square\)

### Corollary 2.2

An internal completion requires `W-2^p` even.

#### Proof

Every one of the `W-2^p` nontransversal lower colours is used once in
`(1.4)`, so

\[
                         \sum_{i=1}^pN_i=W-2^p.                   \tag{2.5}
\]

The left side is even by Lemma 2.1. \(\square\)

## 3. Infinite failure

### Theorem 3.1

If `p=2^s-1`, `s>=2`, the system `(1.4)--(1.5)` is infeasible.

#### Proof

Lucas's theorem says

\[
 {2p+1\choose p+1}\equiv1\pmod2
 \quad\Longleftrightarrow\quad
 (p+1)\mathbin{\&}p=0.                                  \tag{3.1}
\]

For consecutive positive integers, the bitwise condition on the right
holds exactly when `p=2^s-1`.  Hence `W` is odd under `(0.5)`.  Since
`2^p` is even, `W-2^p` is odd, contradicting Corollary 2.2. \(\square\)

The proof did not require the residual internal edges to form whole cell
cycles, Hamilton cycles, good cells, or resident components.  It rules out
the entire internal-edge closure of the pair structure.

## 4. Consequence for the replacement-carrier programme

The existing transversal-lift extension theorem remains correct: protected
Ore supplies an exact owner/lower completion because it allows arbitrary
Johnson edges.  Theorem 3.1 explains why that unrestricted completion is
not a cosmetic relaxation.  On the infinite sequence `(0.5)`, every exact
completion must contain a nonlift edge which exchanges coordinates from
different matched pairs or otherwise leaves the internal pair-cell graph.

Therefore the strongest currently certified pair-cell architecture is:

1. the transversal lift gives one exponentially large resident component
   and exactly repairs the inaccessible lower family;
2. unrestricted protected Ore completes the owner/lower incidence ledger;
3. a new cross-cell absorber/chronology theorem must replace the arbitrary
   completion if global residence is required.

Whole-good-cell selection cannot fill step 3, even after discarding the
whole-cell `2`-adic size obstruction: the finer direction parity above
survives arbitrary cutting inside cells.

The obstruction is only parity-one.  It does not prove that an extensive
cross-cell bank is necessary, and a bounded conformal absorber could in
principle remove it.  Such an absorber would still have to coexist with
the chronological transition-collar and upper/source rows.
