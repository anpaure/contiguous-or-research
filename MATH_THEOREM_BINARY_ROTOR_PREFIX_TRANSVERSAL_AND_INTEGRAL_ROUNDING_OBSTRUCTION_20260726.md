# Binary-rotor prefix transversals and the exact integral-rounding obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,
\]

and let \(A\) rotate the first \(n-1=2m\) positions of a permutation
state and \(B\) rotate all \(n\) positions.  This note audits the integral
rounding gate in
`MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md`.

There are four exact conclusions.

1.  **The two prefix systems have no integral Hall obstruction by
    themselves.**  Any symmetric-chain decomposition of the Boolean
    lattice gives one permutation state over every middle owner and covers
    every lower and upper prefix target, simultaneously at every rank.

2.  For a fixed owner-prefix transversal \(P\subset S_n\), the missing
    rotor condition is exactly one ordinary bipartite Hall system:

    \[
      \boxed{|N^+_P(Q)|\ge |Q|\quad(Q\subseteq P),}
      \tag{0.1}
    \]

    where

    \[
      N^+_P(Q)=P\cap\{A\pi,B\pi:\pi\in Q\}.
    \]

    Thus (0.1), after the state transversal has been chosen, is the
    smallest exact integral coupling inequality.

3.  The simultaneous owner-flow matrix is not totally unimodular in the
    actual rotor graph.  It contains an explicit determinant-two minor on
    a directed \(4m\)-cycle.  Hence network-flow integrality does not
    survive the owner-fibre rows.

4.  The failure is not merely a bad matrix presentation.  On the
    \(A\)-only face, the uniform all-prefix fractional circulation exists
    for every \(H\le m-1\), whereas an integral circulation requires

    \[
                         2m\mid W.                 \tag{0.2}
    \]

    If \(m\) is an odd prime, Lucas' congruence gives

    \[
                         W\equiv2\pmod m,           \tag{0.3}
    \]

    so there is no integral point on this face.  In particular, at every
    Gaussian depth \(H=\lceil A_0\sqrt m\rceil\le m-1\), the feasible
    fractional point is outside the convex hull of all integral rotor
    circulations.

This is an exact obstruction to a universal LP, total-unimodularity,
Birkhoff, or face-preserving decomposition proof.  It is **not** an
obstruction to a genuinely mixed \(A/B\) circulation.  Any mixed solution
with \(o(W/m)\) support cycles must, however, contain at least

\[
              \left(\frac12-o(1)\right)\frac Wm
\]

\(B\)-arcs.  The surviving statement is therefore precise: construct an
all-prefix owner transversal satisfying (0.1) and using a macroscopic
number on the Catalan scale of genuine rotor changes.  No coefficient-one
claim is made here.

## 1. The exact extended formulation

For \(\pi=(\pi_1,\ldots,\pi_n)\in S_n\), write

\[
 \rho(\pi)=\{\pi_1,\ldots,\pi_m\}
 \tag{1.1}
\]

for its middle owner, and write

\[
 p_r(\pi)=\{\pi_1,\ldots,\pi_r\}
 \qquad(0\le r\le n)
 \tag{1.2}
\]

for its prefix sets.  Let \(z_{\pi,A},z_{\pi,B}\ge0\), and put

\[
 y_\pi=z_{\pi,A}+z_{\pi,B}.
 \tag{1.3}
\]

The fractional rotor system is

\[
 \sum_{\rho(\pi)=X}y_\pi=1
 \qquad\left(X\in\binom{[n]}m\right),              \tag{1.4}
\]

\[
 y_\pi=z_{A^{-1}\pi,A}+z_{B^{-1}\pi,B}
 \qquad(\pi\in S_n),                              \tag{1.5}
\]

and, through depth \(H\),

\[
 \sum_{p_{m-q}(\pi)=S}y_\pi\ge1
 \quad\left(S\in\binom{[n]}{m-q},\ 0\le q\le H\right),
 \tag{1.6}
\]

\[
 \sum_{p_{m+1+q}(\pi)=U}y_\pi\ge1
 \quad\left(U\in\binom{[n]}{m+1+q},\ 0\le q\le H\right).
 \tag{1.7}
\]

For a Boolean solution, (1.4) selects one state over every owner and
(1.5) makes the selected arcs a disjoint union of directed cycles.

The uniform point

\[
 z_{\pi,A}=\frac{t}{D},\qquad
 z_{\pi,B}=\frac{1-t}{D},\qquad
 D=m!(m+1)!,                                      \tag{1.8}
\]

is feasible for every \(0\le t\le1\) and every \(H\le m-1\).  Indeed,
each owner fibre has \(D\) states, both \(A\) and \(B\) are permutations
of \(S_n\), and the mass on any prescribed rank-\(r\) prefix is

\[
 \frac{r!(n-r)!}{D}
 =\frac{W}{\binom n r}\ge1                       \tag{1.9}
\]

for \(m-H\le r\le m+1+H\).  The last inequality holds because the
middle two ranks have the maximum binomial coefficient.

## 2. The smallest integral coupling inequality

Let \(P\subset S_n\) contain exactly one state from every owner fibre.
Form a bipartite graph \(G_P\) with a left and a right copy of \(P\), and
put edges

\[
 \pi_L(A\pi)_R\quad\hbox{if }A\pi\in P,
 \qquad
 \pi_L(B\pi)_R\quad\hbox{if }B\pi\in P.           \tag{2.1}
\]

### Theorem 2.1 (fixed-transversal rotor Hall theorem)

There is a Boolean rotor circulation whose selected state set is exactly
\(P\) if and only if

\[
 |N^+_P(Q)|\ge |Q|\qquad(Q\subseteq P).            \tag{2.2}
\]

When it exists, any perfect matching in \(G_P\) supplies the rotor arcs,
and its directed support is a disjoint cycle cover of \(P\).

#### Proof

A Boolean circulation gives every selected state one outgoing selected
arc and one incoming selected arc.  Sending its left copy to the head of
that arc is therefore a perfect matching of \(G_P\).

Conversely, a perfect matching chooses for every \(\pi\in P\) exactly one
of its legal heads \(A\pi,B\pi\), and every state in the right copy is
chosen exactly once.  Thus selected outdegree and indegree are both one.
The resulting finite directed graph is a disjoint union of cycles.
Hall's marriage theorem says that this perfect matching exists exactly
when (2.2) holds. \(\square\)

All prefix conditions depend only on \(P\), not on which of the two arcs
is subsequently chosen.  Thus the integral problem separates exactly as
follows:

* choose one state in every owner fibre satisfying (1.6)--(1.7);
* make that same state set satisfy the single Hall family (2.2).

The next theorem proves that the first bullet has an exact solution at
all depths.

## 3. An exact all-rank integral prefix transversal

### Lemma 3.1 (existence of symmetric-chain decompositions)

For every \(n\), the Boolean lattice \(2^{[n]}\) is a disjoint union of
chains

\[
 C_r\subset C_{r+1}\subset\cdots\subset C_{n-r},
 \qquad |C_j|=j.                                  \tag{3.1}
\]

#### Proof

Induct on \(n\).  From a symmetric chain

\[
 A_r\subset\cdots\subset A_{n-1-r}
\]

in \(2^{[n-1]}\), form

\[
 A_r\subset\cdots\subset A_{n-1-r}
       \subset A_{n-1-r}\cup\{n\},                \tag{3.2}
\]

and, when nonempty,

\[
 A_r\cup\{n\}\subset\cdots\subset
 A_{n-2-r}\cup\{n\}.                             \tag{3.3}
\]

Their endpoint ranks sum to \(n\), and together they partition the two
copies, without and with \(n\), of the old chain.  Applying this to every
old chain proves the induction. \(\square\)

### Theorem 3.2 (all-prefix SCD transversal)

There is a set \(P_{\mathcal C}\subset S_n\) with exactly one state over
every middle owner such that, for every \(0\le r\le n\) and every
\(R\in\binom{[n]}r\),

\[
              p_r(\pi)=R
\quad\hbox{for at least one }\pi\in P_{\mathcal C}.       \tag{3.4}
\]

At ranks \(m\) and \(m+1\), the occurrence in (3.4) is unique.
Consequently (1.4), (1.6), and (1.7) have a common Boolean solution for
every \(H\le m\), before flow conservation is imposed.

#### Proof

Fix a symmetric-chain decomposition \(\mathcal C\).  Since \(n=2m+1\),
every symmetric chain crosses ranks \(m\) and \(m+1\), exactly once at
each rank.  Hence \(\mathcal C\) has exactly \(W\) chains and their
rank-\(m\) members enumerate all middle owners.

For a chain (3.1), choose a permutation

\[
 \pi_C=(a_1,\ldots,a_n)                            \tag{3.5}
\]

as follows.  Order the elements of \(C_r\) arbitrarily in the first
\(r\) positions; then put in positions \(r+1,\ldots,n-r\), in order, the
unique successive elements of
\(C_{r+1}\setminus C_r,\ldots,C_{n-r}\setminus C_{n-r-1}\); finally
order the elements outside \(C_{n-r}\) arbitrarily.  It follows that

\[
 p_j(\pi_C)=C_j\qquad(r\le j\le n-r).              \tag{3.6}
\]

Put \(P_{\mathcal C}=\{\pi_C:C\in\mathcal C\}\).  Every set \(R\) is
an element of one and only one decomposition chain, say \(R=C_r\), so
(3.6) gives (3.4).  At ranks \(m,m+1\), every one of the \(W\) chains
crosses the rank, so there are exactly \(W\) prefix occurrences for
exactly \(W\) targets; uniqueness follows.  The middle-prefix statement
also says that \(P_{\mathcal C}\) has one state in every owner fibre.
\(\square\)

Theorem 3.2 rules out a prefix-side or Gaussian-annulus Hall deficit.
The unresolved requirement is to choose the within-chain orders and,
possibly, the symmetric-chain decomposition itself so that (2.2) also
holds.  Fractional averaging cannot make that choice automatically.

### Proposition 3.3 (whole-transversal averaging does not improve rotor Hall)

Let (P\subset S_n) be any owner transversal, and let (R(P)) denote
entrywise relabelling by (R\in S_n).  Averaging the incidence vectors
of (R(P)) over all (R\in S_n) gives

\[
                 \frac1{D}\mathbf 1_{S_n}.        \tag{3.7}
\]

If (P) covers a collection of prefix ranks, every (R(P)) covers the
same ranks.  Moreover all the bipartite rotor graphs
(G_{R(P)}) are isomorphic.  In particular, the Hall deficiency

\[
 \operatorname{def}(P)
   :=\max_{Q\subseteq P}\bigl(|Q|-|N^+_P(Q)|\bigr) \tag{3.8}
\]

is constant throughout the relabelling orbit.

#### Proof

Fix a target state \(\sigma\in S_n\).  For each \(\pi\in P\), there is
exactly one entrywise coordinate relabelling (R) with
(R(\pi)=\sigma).  Thus \(\sigma\) occurs in exactly \(|P|=W\) of the
\(n!\) relabelled transversals.  Since (n!=WD), its average incidence
is (1/D), proving (3.7).

Relabelling maps a prefix target to its relabelled target, so it preserves
coverage rank by rank.  It acts on coordinate values while (A,B) act on
positions; hence

\[
                       R(A\pi)=A(R\pi),\qquad
                       R(B\pi)=B(R\pi).            \tag{3.9}
\]

Therefore (R) is an isomorphism from (G_P) to (G_{R(P)}), and
(3.8) is invariant. \(\square\)

Applied to (P_{\mathcal C}), Proposition 3.3 expresses the uniform
fractional root vector as an average of **integral transversals which
already cover every prefix rank**.  Thus neither marginal averaging nor
whole-transversal averaging addresses flow: a relabelling orbit cannot
turn a Hall-deficient seed into a rotor-closed one.

## 4. Exact cycle-column form

Let \(\mathfrak C\) denote the directed simple cycles of the full
two-rotor graph.  For \(C\in\mathfrak C\), define

\[
 a_X(C)=|V(C)\cap\rho^{-1}(X)|,                    \tag{4.1}
\]

and, for every prefix target \((r,R)\),

\[
 b_{r,R}(C)=|\{\pi\in V(C):p_r(\pi)=R\}|.          \tag{4.2}
\]

Every nonnegative circulation decomposes into directed cycles.  Hence
the fractional feasibility problem is equivalently

\[
 \sum_{C\in\mathfrak C}a_X(C)\lambda_C=1
 \quad(X\in\tbinom{[n]}m),                         \tag{4.3}
\]

\[
 \sum_{C\in\mathfrak C}b_{r,R}(C)\lambda_C\ge1
 \quad\hbox{for all protected prefix targets},    \tag{4.4}
\]

with \(\lambda_C\ge0\).

An integral solution is an exact cover by cycles for which every used
cycle is owner-simple:

\[
                         a_X(C)\le1.               \tag{4.5}
\]

Indeed, a used cycle with \(a_X(C)\ge2\), or two used cycles meeting the
same owner fibre, violates (4.3).  Conversely, an integral exact cover in
(4.3) is automatically vertex-disjoint, because two selected states in
one vertex also lie in one owner fibre.  Thus ordinary circulation
decomposition has converted the problem into a coloured-cycle exact-cover
problem; it has not rounded it.

## 5. An explicit determinant-two minor in the rotor graph

Let

\[
 \pi^0=(1,2,\ldots,2m,2m+1).
\]

With the tuple-action convention, \(A\) left-rotates the first \(2m\)
entries and \(B\) left-rotates all \(2m+1\) entries.  Therefore

\[
 T:=BA^{-1}
\]

swaps the final two positions and fixes the first \(2m-1\).  Since
\(A^{-1}=A^{2m-1}\), the following is a positive directed rotor cycle:

\[
 \begin{split}
 \pi^0,A\pi^0,\ldots,A^{2m-1}\pi^0,
 T\pi^0,AT\pi^0,\ldots,A^{2m-1}T\pi^0,\pi^0.
 \end{split}                                       \tag{5.1}
\]

The two closing transitions displayed in (5.1) are \(B\)-transitions;
all other transitions are \(A\)-transitions.

### Lemma 5.1

For \(m\ge2\), (5.1) is a simple directed cycle of length \(4m\), and
the owner \(X_0=[m]\) occurs on it exactly twice, at \(\pi^0\) and
\(T\pi^0\).

#### Proof

Each of the two displayed \(A\)-strings has \(2m\) distinct states,
because \(A\) acts freely on a permutation and has order \(2m\).  If a
state from the two strings coincided, then a power of \(A\) would equal
\(T\) as a position permutation.  This is impossible: every power of
\(A\) fixes the final position, whereas \(T\) moves it.  Hence the cycle
is simple.

Along the first string, the middle owners are the \(m\)-term cyclic
intervals in the cyclic order

\[
                         1,2,\ldots,2m.
\]

Only the interval beginning at \(1\) equals \([m]\).  Along the second
string, the first \(2m\) entries have cyclic order

\[
                         1,2,\ldots,2m-1,2m+1.
\]

Again only the interval beginning at \(1\) equals \([m]\).  These are
the states \(\pi^0\) and \(T\pi^0\). \(\square\)

Let \(M\) be the matrix whose columns are rotor arcs, whose state rows
are flow-incidence rows, and whose owner row \(X\) has entry one on arcs
whose tail lies in \(\rho^{-1}(X)\).  Restrict to the \(4m\) arc columns
of (5.1), take any \(4m-1\) of its vertex-incidence rows, and append the
owner row \(X_0\).

### Theorem 5.2 (exact non-TU minor)

The resulting square minor has determinant \(\pm2\).  In particular,
the owner-flow matrix is not totally unimodular for any \(m\ge2\).

#### Proof

For an oriented \(\ell\)-cycle, delete one row of its vertex-arc
incidence matrix.  Every maximal minor of the remaining
\((\ell-1)\times\ell\) matrix is \(\pm1\), with the signs arranged so
that appending a row \(r=(r_1,\ldots,r_\ell)\) gives determinant

\[
                         \pm\sum_{i=1}^{\ell}r_i.   \tag{5.2}
\]

This also follows directly by successively eliminating along the cycle.
For the owner row \(X_0\), Lemma 5.1 says that the sum in (5.2) is two.
\(\square\)

Thus adding only one owner-fibre equation already destroys the network
matrix.  Adding the prefix-cover rows cannot restore total
unimodularity.

## 6. A genuine integer-hull gap on the \(A\)-only face

### Theorem 6.1 (A-face divisibility obstruction)

Suppose a Boolean solution of (1.4)--(1.5) has
\(z_{\pi,B}=0\) for every \(\pi\).  Then

\[
                         2m\mid W.                 \tag{6.1}
\]

#### Proof

Let \(P=\{\pi:y_\pi=1\}\).  With only \(A\)-arcs, flow conservation
says

\[
                         A(P)=P.
\]

The action of \(A\) on permutation states is free and every orbit has
length \(2m\).  Hence \(|P|\) is a multiple of \(2m\).  The owner
equalities select one state for each of the \(W\) owners, so \(|P|=W\).
\(\square\)

### Corollary 6.2 (infinitely many exact fractional/integral gaps)

If \(m=p\) is an odd prime, the uniform \(A\)-only point

\[
 z_{\pi,A}=1/D,\qquad z_{\pi,B}=0                 \tag{6.2}
\]

satisfies the owner equations, flow, and both prefix-cover systems for
every \(H\le m-1\), but it is not in the convex hull of the Boolean
solutions.

#### Proof

Fractional feasibility is (1.8)--(1.9) with \(t=1\).  Lucas' theorem in
base \(p\) gives

\[
 \binom{2p+1}{p}
 \equiv \binom21\binom10
 \equiv2\pmod p.                                  \tag{6.3}
\]

Thus \(p\nmid W\), and Theorem 6.1 excludes a Boolean point on the
\(A\)-only face.

If (6.2) were a convex combination of arbitrary Boolean mixed
circulations, every circulation in the combination would have to use no
\(B\)-arc: all \(B\)-coordinates are nonnegative and their average is
zero.  This is impossible by the preceding paragraph. \(\square\)

For every fixed \(A_0>0\), the Gaussian value
\(H=\lceil A_0\sqrt p\rceil\) is at most \(p-1\) for all sufficiently
large primes.  Therefore Corollary 6.2 is an obstruction at exactly the
scale in the question, not at an irrelevant depth.

One elementary integer-hull cut exposed by the proof is

\[
                 \sum_{\pi\in S_n}z_{\pi,B}\ge1   \tag{6.4}
\]

whenever \(2m\nmid W\).  It separates (6.2).  The cut is small in
absolute size and does not obstruct a genuinely mixed construction.

## 7. How much mixing a few-cycle solution must contain

Let \(b(z)\) be the number of selected \(B\)-arcs in a Boolean
circulation, and let \(c_A(z)\) be the number of support cycles containing
only \(A\)-arcs.

### Proposition 7.1 (exact run ledger)

Every Boolean rotor circulation satisfies

\[
                 W\le 2m\bigl(c_A(z)+b(z)\bigr).   \tag{7.1}
\]

Consequently, if \(C(z)\) is its total number of support cycles, then

\[
                 b(z)\ge \frac{W}{2m}-C(z).        \tag{7.2}
\]

In particular,

\[
 C(z)=o(W/m)\quad\Longrightarrow\quad
 b(z)\ge\left(\frac12-o(1)\right)\frac Wm.         \tag{7.3}
\]

#### Proof

A pure \(A\)-cycle has exactly \(2m\) states.  On any support cycle
containing a \(B\)-arc, delete its \(B\)-arcs.  This leaves one directed
\(A\)-run for each \(B\)-arc, allowing empty runs when two \(B\)-arcs are
consecutive.  No such run has \(2m\) or more \(A\)-arcs, because
\(A^{2m}=1\) would repeat a state before the support cycle closed.
Therefore a mixed support cycle containing \(b_C\) \(B\)-arcs has at
most

\[
                    b_C(2m-1)+b_C=2m b_C
\]

states.  Summing over pure and mixed cycles proves (7.1).  Since
\(c_A(z)\le C(z)\), (7.2)--(7.3) follow. \(\square\)

Thus the component target rules out an almost-\(A\)-only repair.  The
required \(B\)-arc count is on the Catalan scale \(W/m\), even though its
density among all \(W\) selected arcs is only \(\Theta(1/m)\).

## 8. Precise proved/conditional boundary

The following statements are proved here.

1. Owner transversality and both prefix-cover systems have a common
   Boolean solution at every depth, by Theorem 3.2.
2. For any such selected state set, rotor closure is equivalent to the
   exact Hall inequalities (2.2).
3. The direct owner-flow matrix has an actual determinant-two minor.
4. Uniform fractional feasibility does not imply membership in the
   integer hull, even with all prefix systems present: Corollary 6.2 gives
   infinitely many Gaussian-scale instances.
5. Any integral few-cycle solution must use the quantitative amount of
   genuine \(A/B\) mixing in (7.3).

What is not proved is an obstruction to every mixed solution of
(1.4)--(1.7), or a construction of one.  The exact remaining constructive
lemma is:

> Choose a symmetric-chain-type all-prefix owner transversal
> \(P\subset S_n\) for which (2.2) holds and whose resulting perfect
> matching has \(o(W/m)\) directed cycles.

The determinant and prime divisibility cuts show why this cannot follow
from generic circulation rounding, two-matroid intersection, or a convex
decomposition of the uniform fractional point.  A successful proof must
correlate the state choice with the rotor matching and must cross the
\(A\)-orbit faces on the scale forced by (7.3).
