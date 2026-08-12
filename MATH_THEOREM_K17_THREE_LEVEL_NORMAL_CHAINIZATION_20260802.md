# K17 exact three-level chainization of the strict lower ideal

**Date:** 2026-08-02  
**Status:** unconditional static chain-partition theorem.  It closes the
named-target chainization row for `k=17`, but it does not construct a literal
source chronology, residence, upper shadows, a common cap, or a universal
word.

## 1. Statement

Put

\[
  \mathcal L=\{S\subseteq[17]:1\le |S|\le 8\}.
\]

### Theorem 1 (exact depth-three chainization)

The family `\(\mathcal L\)` has a partition into exactly

\[
                         {17\choose8}=24\,310
\]

inclusion chains, every chain has at most three members, and every chain
contains exactly one rank-eight set.

Equivalently, all `65,535` nonempty targets below the selected middle rank
nine admit one exact static depth-three payload table indexed by the rank-eight
sets.

### Corollary 2 (attachment to an owner phase)

Let `\(G\)` be any incidence graph between the rank-eight and rank-nine
layers which has a perfect matching.  Then the chains in Theorem 1 can be
assigned bijectively to the rank-nine owners so that every target in an
owner's chain is a proper subset of that owner.

In particular this applies to a two-factor, by alternating its cycles.  It
also applies to the authenticated K17 lollipop factor: its rank-eight leaf
forces the tail matching, after which the remaining even cycle alternates.

## 2. Rank compression

Make a three-level poset `\(P\)` as follows:

\[
\begin{aligned}
 P_0&=\bigcup_{s=1}^{6}{[17]\choose s},\\
 P_1&={[17]\choose7},\\
 P_2&={[17]\choose8}.
\end{aligned}
\]

Elements inside one `\(P_i\)` are declared incomparable, and elements in
different levels are ordered by ordinary set containment.  Thus every chain
of `\(P\)` is a genuine Boolean-lattice inclusion chain, and it has at most
three members.

The level sizes are

\[
\begin{aligned}
 n_0&=\sum_{s=1}^{6}{17\choose s}
     =17+136+680+2380+6188+12376=21\,777,\\
 n_1&={17\choose7}=19\,448,\\
 n_2&={17\choose8}=24\,310.
\end{aligned}                                                    \tag{2.1}
\]

The key point is that this rank compression remains normal even though
`\(P_0\)` contains six original Boolean ranks.

## 3. Uniform adjacent-level couplings

For `\(S\in P_0\)` of original rank `\(s\)` and `\(T\in P_1\)` with
`\(S\subset T\)`, put

\[
 \mu_{01}(S,T)=
 {1\over n_0{17-s\choose7-s}}.                         \tag{3.1}
\]

The first marginal is uniform, since `\(S\)` has
`\({17-s\choose7-s}\)` rank-seven supersets.  For a fixed `\(T\in P_1\)`,

\[
\begin{aligned}
 \sum_{S\subset T}\mu_{01}(S,T)
 &= {1\over n_0}
    \sum_{s=1}^{6}{{7\choose s}\over{17-s\choose7-s}}\\
 &= {1\over n_0}
    \sum_{s=1}^{6}{{17\choose s}\over{17\choose7}}\\
 &= {1\over n_1}.                                      \tag{3.2}
\end{aligned}
\]

Here the middle identity is the elementary double-counting identity

\[
 {{7\choose s}\over{17-s\choose7-s}}
       ={{17\choose s}\over{17\choose7}}.
\]

Hence `\(\mu_{01}\)` is a containment-supported coupling with uniform
marginals on `\(P_0\)` and `\(P_1\)`.

Likewise put

\[
 \mu_{12}(T,U)={1\over 10n_1}
 \quad(T\in P_1, U\in P_2, T\subset U).             \tag{3.3}
\]

Every rank-seven set has ten rank-eight supersets and every rank-eight set
has eight rank-seven subsets.  Since `\(10n_1=8n_2\)`, this coupling also
has uniform marginals.

Couple the two steps conditionally through their common uniform
`\(P_1\)` marginal.  This gives a probability distribution on triples

\[
                         S\subset T\subset U             \tag{3.4}
\]

whose marginal on `\(P_i\)` is uniform for each `\(i=0,1,2\)`.

## 4. Width and Dilworth

Let `\(A\)` be any antichain of `\(P\)`, and write
`\(A_i=A\cap P_i\)`.  A random chain (3.4) meets `\(A\)` at most once.
Taking expectations gives the LYM inequality

\[
 { |A_0|\over n_0}+{ |A_1|\over n_1}+{ |A_2|\over n_2}\le1.       \tag{4.1}
\]

By (2.1), `\(n_i\le n_2\)` for all `\(i\)`, so

\[
             {|A|\over n_2}
 \le { |A_0|\over n_0}+{ |A_1|\over n_1}+{ |A_2|\over n_2}
 \le1.                                                          \tag{4.2}
\]

Thus every antichain has size at most `\(n_2\)`.  Since `\(P_2\)` itself is
an antichain of size `\(n_2\)`, the width of `\(P\)` is exactly `\(n_2\)`.

Dilworth's theorem partitions `\(P\)` into `\(n_2=24,310\)` chains.  The
poset has only three levels, so every chain has size at most three.  There
are `\(n_2\)` rank-eight elements and no chain contains two of them;
therefore every chain contains exactly one rank-eight element.  This proves
Theorem 1.

For Corollary 2, match the rank-eight top `\(U\)` of each chain to a
rank-nine owner `\(R\supset U\)`.  Every earlier chain member is contained
in `\(U\)` and hence in `\(R\)`.  Distinct matched owners receive distinct
chains, proving the claim.

## 5. Constructive realization on the authenticated factor

The companion O3 C++ builder constructs the Dilworth path cover by
Hopcroft--Karp on the transitive three-level comparability graph, then finds
a perfect rank8--rank9 matching inside the selected incidence factor.  On the
independently frozen full-q1 residence-2018 model it reports

```text
PASS chains=24310 links=41225 phase=24310 lengths=1748,3899,18663
```

The exact replay census is

```text
compressed nodes                    65535
comparability edges               8625188
matched chain links                 41225
chain lengths 1,2,3           1748,3899,18663
selected factor incidences          48620
perfect owner phase                 24310
targets by ranks 1,...,8
  17,136,680,2380,6188,12376,19448,24310
```

The frozen constructive artifacts are:

* `scratch/build_k17_exact_depth3_owner_payload_table_20260802.cpp`, SHA
  `410a617e3e724e005b8cce73bee50067ee8256363ae723621e18910748c929b1`;
* `scratch/k17_exact_depth3_owner_payload_table_20260802/k17_depth3_owner_payload.tsv`,
  SHA `029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1`;
* its audit JSON, SHA
  `6e508cb8521e2c263c32b3f08e546693d50e90f858b8f6157a3f55e7ef7c758c`.

The builder's replay is intentionally redundant with the proof: it checks
every target exactly once, every chain containment, every root and owner
exactly once, and every assigned root--owner edge selected in the input
factor.  A separately implemented strict parser has now replayed the complete
table, SAT assignment and 218,790-row incidence map without reusing the
producer.  It passes with report SHA
`bb2fc1f7eb54e0379af2797b179efdb25b7eb677a826bb0732198134b4cf001f`;
the independent source SHA is
`e198b4870f6832a5168aae596686478de38ceed525f7555eca157df0ac6a9aeb`.

## 6. What this removes, and what it does not

For K17 the triangular depth is `\(d(17)=3\)`.  The theorem therefore gives
an exact owner-labelled static payload table with no unmatched named lower
target and no fourth payload position.  In particular, a future K17 source
construction need not solve a separate equitable-chain conjecture.

The result is deliberately static.  It does **not** show that the selected
chains can be realized simultaneously as proper suffix unions of one
balanced literal de Bruijn circulation.  After attaching chains to owners,
the remaining lower-side gate is the fixed-table state-balance/rooted-Euler
problem, together with the actual residence and upper guards.  Those are the
Hoffman/fusion rows isolated in the current hinge-rectangle and labelled
trace-spine theorems.

The argument is also dimension-specific in an important way.  It uses

\[
 \sum_{s=1}^{6}{17\choose s}<{17\choose8}.
\]

At the next analogous odd case with depth three, the corresponding compressed
bottom may exceed the top level; then some chains must contain two targets
from the compressed bottom bank, and this three-level proof no longer
applies unchanged.
