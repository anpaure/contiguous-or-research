# A sparse-marking Turan theorem gives a spread Catalan pivot bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional owner-side theorem.  A single sparse random
marking of the complete pivot-geodesic hypergraph, followed by Turan's
independent-set bound in the marked intersection graph, produces the full
parity-appropriate Catalan number of pairwise owner-disjoint pivot bridges.
Simultaneously, the reserved owners occupy only `O(1/s)` of every lower
containment star, where `s=h+1`.  This replaces the proposed
growing-uniformity nibble by an elementary one-bite argument.  It does not
make the natural suffix decks of different bridges target-disjoint and does
not construct a protected trace factor on the complementary owners.

## 1. A general one-bite spread matching lemma

Let `H=(V,E)` be a simple `s`-uniform `Delta`-regular hypergraph on `N`
vertices.  Let `F subset V` be a forbidden set and write

\[
              H_F=H[V\setminus F].
\]

Let `A` be a family of test sets in `V`, and put

\[
              L=\min_{A\in\mathcal A}|A|.
\]

### Theorem 1.1 (sparse-marking Turan spread lemma)

Fix constants `gamma>0` and `0<epsilon<1`.  Suppose

\[
 {s|F|\over N}=o(1),
 \qquad
 {N\over s^2}\longrightarrow\infty,
 \qquad
 {L/s^2\over 1+\log |\mathcal A|}\longrightarrow +\infty.
\tag{1.1}
\]

Assume also that `s Delta >= gamma` for all sufficiently large parameters,
so that the marking probability below is at most one.  (This is automatic
in the pivot-hypergraph application, where `s -> infinity`.)

Then, for all sufficiently large parameters, `H_F` has a matching `M`
such that

\[
 |M|\ge
 \left(
 { (1-\epsilon)^2\gamma
  \over
   (1-\epsilon)+(1+\epsilon)\gamma}
 -o(1)
 \right){N\over s^2},
\tag{1.2}
\]

and, simultaneously for every `A in mathcal A`,

\[
       |V(M)\cap A|
       \le (1+\epsilon){\gamma\over s}|A|.
\tag{1.3}
\]

The `o(1)` in (1.2) is only the forbidden-set loss.  In particular, after
letting `epsilon` tend to zero through fixed values, the matching
coefficient can be made arbitrarily close to

\[
                         {\gamma\over1+\gamma}.
\tag{1.4}
\]

#### Proof

Independently mark every edge of `H_F` with probability

\[
                         q={\gamma\over s\Delta}.
\tag{1.5}
\]

Let `X` be the number of marked edges.  Since deleting all edges meeting
`F` removes at most `|F|Delta` edges and regularity gives

\[
                         |E|={N\Delta\over s},
\]

we have

\[
 \mu:=\mathbb EX
 =q|E(H_F)|
 \ge {\gamma N\over s^2}
       \left(1-{s|F|\over N}\right).
\tag{1.6}
\]

The variable `X` is binomial and `mu -> infinity` under (1.1) (indeed it is
exponential in the application below), so Chernoff gives

\[
             X\ge(1-\epsilon)\mu
\tag{1.7}
\]

with probability tending to one.

Make the **marked intersection graph** `G`: its vertices are the marked
hyperedges and two vertices are adjacent precisely when the corresponding
hyperedges intersect.  Let `Y=e(G)`.  The total number of intersecting
unordered pairs of hyperedges is at most

\[
 \sum_{v\in V}{d_H(v)\choose2}
 \le {N\Delta^2\over2}.
\]

This may overcount pairs meeting in more than one owner, which is harmless.
Consequently

\[
                  \mathbb EY
             \le {\gamma^2N\over2s^2}.
\tag{1.8}
\]

Markov's inequality shows that

\[
                  Y\le(1+\epsilon){\gamma^2N\over2s^2}
\tag{1.9}
\]

has probability at least `epsilon/(1+epsilon)`.

It remains to impose all spread tests.  For `A in mathcal A`, put

\[
 Z_A=\sum_{e\in E(H_F)}|e\cap A|\,\mathbf 1_{\{e\text{ marked}\}}.
\tag{1.10}
\]

Every owner in the union of the marked edges is counted at least once in
`Z_A`.  Moreover,

\[
 \sum_{e\in E(H_F)}|e\cap A|
 \le\Delta|A|,
 \qquad
 \sum_{e\in E(H_F)}|e\cap A|^2
 \le s\Delta|A|.
\tag{1.11}
\]

Hence

\[
 \mathbb EZ_A\le{\gamma\over s}|A|,
 \qquad
 \sum_e\operatorname{Var}
  \bigl(|e\cap A|\mathbf1_{\{e\text{ marked}\}}\bigr)
 \le\gamma|A|.
\tag{1.12}
\]

Bernstein's inequality, using the summand bound `s`, now gives an absolute
`c_(epsilon,gamma)>0` such that

\[
 \Pr\left\{Z_A>(1+\epsilon){\gamma\over s}|A|\right\}
 \le \exp\left(-c_{\epsilon,\gamma}{|A|\over s^2}\right).
\tag{1.13}
\]

Condition (1.1) and a union bound show that all inequalities in (1.13)
hold simultaneously with probability tending to one.  Intersecting this
event and (1.7) with the positive-probability event (1.9) leaves a valid
outcome for all sufficiently large parameters.

For that outcome, Turan--Caro--Wei and Cauchy--Schwarz give

\[
 \alpha(G)\ge\sum_{x\in V(G)}{1\over d_G(x)+1}
             \ge {X^2\over X+2Y}.
\tag{1.14}
\]

An independent set in `G` is a matching in `H_F`.  Substitution of
(1.6)--(1.9) into (1.14) proves (1.2).  Its owner union is contained in the
union of all marked edges, so (1.10)--(1.13) prove (1.3). `square`

### Remark 1.2 (why no nibble theorem is needed)

The argument uses neither pair codegrees nor fixed uniformity.  The marked
intersection graph may have arbitrary local clustering.  Turan's bound
prices its **total** collision count, and a fixed `gamma` leaves the
coefficient `gamma/(1+gamma)`.  Growing `s` helps the spread estimate because
the touched-owner density is `Theta(1/s)`.

## 2. Application to pivot geodesics

Fix owner rank `r` in dimension `k`, and let

\[
                         W={k\choose r},
 \qquad s=h+1.
\tag{2.1}
\]

Let `H_piv` be the simple `s`-uniform hypergraph on the rank-`r` layer whose
edges are the owner sets of length-`h` induced Johnson geodesics

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
       \qquad0\le j\le h,
\tag{2.2}
\]

where all displayed coordinates are disjoint and `|Q|=r-h`.  Coordinate
symmetry makes this hypergraph regular.  Its exact degree is

\[
 \Delta={s(r)_h(k-r)_h\over2},
\tag{2.3}
\]

although Theorem 1.1 needs only regularity.

For every lower set `S` with `|S|<=r-h-1`, let

\[
 \mathcal O(S)=\left\{T\in{k\choose r}:S\subseteq T\right\}
\tag{2.4}
\]

be its owner-containment star.  The smallest such star has size

\[
 L_*={k-r+h+1\choose h+1}.
\tag{2.5}
\]

When `k=2r+O(1)` and `h=Theta(sqrt r)`,

\[
 \log L_*=\Theta(\sqrt r\log r),
 \qquad
 {L_*\over s^2}\gg k,
\tag{2.6}
\]

whereas the number of tests is at most `2^k`.  Thus (1.1) holds for the
family of all stars (2.4).

### Theorem 2.1 (spread pivot-bank theorem)

Assume `k=2r+O(1)`, `h=Theta(sqrt r)`, and let `F` be any prescribed owner
bank with

\[
                         |F|=o(W/s).
\tag{2.7}
\]

For every fixed `gamma>0` and `epsilon>0`, the pivot hypergraph outside
`F` contains a matching `M` satisfying

\[
 |M|\ge
 \left(
 { (1-\epsilon)^2\gamma
  \over(1-\epsilon)+(1+\epsilon)\gamma}
 -o(1)
 \right){W\over s^2},
\tag{2.8}
\]

and

\[
 |V(M)\cap\mathcal O(S)|
 \le(1+\epsilon){\gamma\over s}|\mathcal O(S)|
\tag{2.9}
\]

for every `S` of rank at most `r-h-1`.

In particular, the complementary owner layer retains at least

\[
 \left(1-(1+\epsilon){\gamma\over s}\right)
 |\mathcal O(S)|-|F\cap\mathcal O(S)|
\tag{2.10}
\]

owners above every such `S`.

#### Proof

Apply Theorem 1.1 with `N=W` and the test family (2.4).  Equations
(2.5)--(2.7), together with (2.3), verify its hypotheses. `square`

## 3. The Catalan constants

Use the deadline depth of the pivot-gluing theorem:

\[
 h=d(k)+1,
 \qquad
 s=h+1=d(k)+2.
\tag{3.1}
\]

For `k=2r+O(1)`,

\[
                         {s^2\over r}\longrightarrow{\pi\over4}.
\tag{3.2}
\]

Choose, for example, `gamma=5` and then choose a sufficiently small fixed
`epsilon>0`.  Since

\[
                         {5\over6}>{\pi\over4},
\tag{3.3}
\]

Theorem 2.1 gives more than `W/(r+1)` bridges in the even case `k=2r`.
Taking an arbitrary submatching of the required size preserves (2.9).
Therefore it gives exactly

\[
                         {W\over r+1}-1
\tag{3.4}
\]

owner-disjoint bridges, the number needed to join the standard even
Catalan component count.

For `k=2r-1`, the odd component count is

\[
                \operatorname{Cat}_{r-1}={W\over2r-1},
\tag{3.5}
\]

and

\[
                         {s^2\over2r-1}\longrightarrow{\pi\over8}.
\tag{3.6}
\]

The same choice `gamma=5` gives much more than the required number, and a
submatching supplies exactly `Cat_(r-1)-1` bridges.

### Corollary 3.1 (unconditional spread Catalan bank)

In both parities, for all sufficiently large dimensions, the complete
middle layer minus any prescribed `o(W/s)` owner bank contains the exact
parity-appropriate number of pairwise owner-disjoint pivot geodesics.
Their owner union removes only `O(1/s)=O(r^(-1/2))` of every containment
star rooted at rank at most `r-h-1`.

For an independently prescribed polynomial-size bank `F`, equation (2.10)
therefore reads

\[
 |\mathcal O(S)\setminus(F\cup V(M))|
       =(1-O(r^{-1/2}))|\mathcal O(S)|
\tag{3.7}
\]

uniformly over all such lower `S`, because the minimum star (2.5) is
superpolynomial.

## 4. Interface with named lower chainization

After the random outcome is fixed, the bridge bank and its complement are
deterministic.  Equation (3.7) is exactly the static containment-star
reserve needed before running a later randomized named-chain/MLD
construction on the complementary owner bank: no lower target loses more
than an `O(r^(-1/2))` fraction of its possible middle hosts.

This statement must not be strengthened silently.  It does not prove that
conditioning an already sampled MLD law on avoiding the bridge bank
preserves MLD.  The proof-safe order is to fix the spread bridge bank first
and then sample or construct the lower object on its deterministic
complement.

## 5. Exact scope

This note proves:

1. a growing-uniformity-free one-bite spread matching lemma;
2. the exact even and odd Catalan-size owner-disjoint pivot bank;
3. avoidance of any prescribed `o(W/s)` owner bank; and
4. simultaneous `1-O(1/s)` retention of every low containment star.

It does **not** prove:

1. mutual disjointness of the overlapping-core bridges' natural lower
   suffix decks;
2. a protected trace factor on the complementary owners;
3. endpoint-state compatibility between that factor and the bridges;
4. internal arbitrary-width upper completeness; or
5. `nu(k)<=B(k)+1`, `B(k)+O(1)`, or exact equality for all `k`.

The previous growing-uniformity nibble hypothesis is therefore removed
from the **owner-side spread-bank** row, but the correlated protected-factor
row remains open.
