# Chung--Feller fixed-layer factors and balanced first-layer completion

Date: 2026-07-26

Method: pure mathematics only. No enumeration, finite search, solver, or
web input is used.

## 0. Result

Let \(D=D_{2s}^0\) be the Dyck roots and let

\[
                         L_t=D_{2s}^t,\qquad0\le t\le s,              \tag{0.1}
\]

be the canonical Chung--Feller flaw layers. Write
\(i_t:D\to L_t\) for the canonical phase bijection.

Every exact rooted factor which uses precisely \(L_t\) at phase \(t\) is
equivalent to permutations

\[
                         p_0,p_1,\ldots,p_s\in\operatorname {Sym}(D),
\qquad p_0=p_s=1,                                      \tag{0.2}
\]

subject to exactly two conditions:

\[
 |i_t(p_tP)\mathbin\triangle i_{t+1}(p_{t+1}P)|=2       \tag{0.3}
\]

for every row and cut, and

\[
 \biguplus_{t=0}^{s-1}\biguplus_{P\in D}
 \{i_t(p_tP)\cup i_{t+1}(p_{t+1}P)\}
                         =\binom{[2s]}{s+1}.            \tag{0.4}
\]

In relative matchings

\[
                         \sigma_t=p_{t+1}p_t^{-1},       \tag{0.5}
\]

the endpoint condition is the zero-monodromy equation

\[
                         \sigma_{s-1}\cdots\sigma_1\sigma_0=1.      \tag{0.6}
\]

For a prescribed first layer \(p_1=\pi\), equations (2.4)--(2.7) below
give the exact residual completion problem. In particular, mere
permutation balance is insufficient: if the first cut repeats one
\((s+1)\)-color, no completion exists.

There is, however, a q-uniform positive completion theorem. Call \(\pi\)
**two-cut balanced** when every proposed phase-one state is adjacent to
both of its canonical outer states and the two incident \(Y\)-palettes
have exactly their canonical aggregate. Then

\[
                         p_0=1,\quad p_1=\pi,\quad
                         p_t=1\quad(2\le t\le s)         \tag{0.7}
\]

is an exact fixed-layer factor. This criterion is necessary and sufficient
for completion with a canonical tail beginning at phase two.

The theorem is not merely formal. For every \(s\ge2\), the
\(\operatorname {Cat}_{s-2}\) pairs

\[
                         1100R,\qquad1010R,
                         \qquad R\in D_{2s-4}^0          \tag{0.8}
\]

give disjoint balanced first-layer transpositions. Any subfamily may be
switched simultaneously. Hence the fixed-layer fibre contains a Boolean
cube of dimension \(\operatorname {Cat}_{s-2}\), acting on

\[
                         2\operatorname {Cat}_{s-2}
   =\left(\frac18+o(1)\right)\operatorname {Cat}_s      \tag{0.9}
\]

rows. This is a construction in every semilength, not a finite example.

More generally, at every phase index \(0\le q\le s-2\), the contextual
pairs

\[
 P1100R,\qquad P1010R,
 \quad P\in D_{2q}^0,\quad R\in D_{2(s-q-2)}^0
\]

give \(\operatorname {Cat}_q\operatorname {Cat}_{s-q-2}\) disjoint
two-cut rectangles. This is the q-uniform form of the construction.

The result does not prove coefficient one: the completed cube has a fixed
two-cut support and correlated deeper target action. It does settle the
algebraic first-layer completion gate exactly.

## 1. Exact fixed-layer normal form

Put

\[
 \mathcal X=\binom{[2s]}s,\qquad
 \mathcal Y=\binom{[2s]}{s+1},\qquad
 B=|D|=\operatorname {Cat}_s.                           \tag{1.1}
\]

The layers \(L_0,\ldots,L_s\) partition \(\mathcal X\), and every layer
has size \(B\). A phase-respecting row indexed by \(P\in D\) has states

\[
                         X_t(P)=i_t(p_tP).              \tag{1.2}
\]

### Theorem 1.1 (layer-permutation normal form)

The rows (1.2) form an exact \(D\)-port rooted complement-path factor if
and only if (0.2)--(0.4) hold.

#### Proof

Since \(p_t\) is a permutation, the phase-\(t\) states in (1.2) enumerate
\(L_t\) exactly once. Thus the complete \(X\)-ledger is automatic.

Condition (0.3) says that consecutive states form a Johnson edge. Its
union is an \((s+1)\)-set. Equation (0.4) says that these unions enumerate
the complete \(Y\)-rank exactly once, which is precisely the second
ownership ledger.

The canonical endpoint theorem is

\[
                         i_s(Q)=[2s]\setminus i_0(Q).    \tag{1.3}
\]

Hence the terminal state in row \(P\) is the complement of its initial
state exactly when \(p_sP=p_0P\). A common relabelling of all rows lets us
take \(p_0=p_s=1\). Conversely, the two exact ledgers, Johnson adjacency,
and (1.3) give the required rooted factor. \(\square\)

There is no additional hidden \(Y\)-condition: (0.4) is the full
adjacent-union ledger.

## 2. Relative matchings and a prescribed first layer

For \(u,v\in D\), define cut-\(t\) admissibility by

\[
 A_t(u,v)=
 \mathbf1_{\{|i_t(u)\triangle i_{t+1}(v)|=2\}},          \tag{2.1}
\]

When \(A_t(u,v)=1\), define its color by

\[
                         c_t(u,v)=i_t(u)\cup i_{t+1}(v)
                         \in\mathcal Y.                 \tag{2.2}
\]

If \(\sigma_t=p_{t+1}p_t^{-1}\), then cut \(t\) uses the perfect matching

\[
                         u\longmapsto\sigma_tu          \tag{2.3}
\]

between the root labels of \(L_t\) and \(L_{t+1}\).

### Theorem 2.1 (relative-matching equations)

A sequence \((\sigma_0,\ldots,\sigma_{s-1})\) gives an exact fixed-layer
factor if and only if

\[
                         A_t(u,\sigma_tu)=1
                         \quad(t,u),                    \tag{2.4}
\]

\[
 \boxed{
 \sum_{t=0}^{s-1}\sum_{u\in D}e_{c_t(u,\sigma_tu)}
                         =\mathbf1_{\mathcal Y},}        \tag{2.5}
\]

and

\[
 \boxed{\sigma_{s-1}\cdots\sigma_0=1.}                  \tag{2.6}
\]

#### Proof

Equation (2.4) is (0.3) after writing the layer-\(t\) owner as \(u\).
Equation (2.5) is the coefficient-vector form of (0.4). Finally
\(p_{t+1}=\sigma_tp_t\), so iteration from \(p_0=1\) gives

\[
                         p_s=\sigma_{s-1}\cdots\sigma_0.
\]

Thus \(p_s=1\) is exactly (2.6). \(\square\)

Now prescribe \(p_1=\pi\). Then \(\sigma_0=\pi\). Define its first-cut
color vector and residual palette by

\[
 C_0(\pi)=\sum_{u\in D}e_{c_0(u,\pi u)},\qquad
 R_\pi=\mathbf1_{\mathcal Y}-C_0(\pi).                  \tag{2.7}
\]

### Corollary 2.2 (exact residual completion problem)

The prescribed first layer \(\pi\) extends to an exact fixed-layer factor
if and only if there are permutations
\(\sigma_1,\ldots,\sigma_{s-1}\) satisfying (2.4) and

\[
 \sum_{t=1}^{s-1}\sum_{u\in D}e_{c_t(u,\sigma_tu)}
                         =R_\pi,                        \tag{2.8}
\]

\[
                         \sigma_{s-1}\cdots\sigma_1
                         =\pi^{-1}.                     \tag{2.9}
\]

This is an exact integral residual-palette problem plus endpoint
monodromy; it is not a fractional or asymptotic relaxation.

### Corollary 2.3 (immediate capacity obstruction)

If \(C_0(\pi)\) has a coefficient greater than one, then \(\pi\) has no
completion.

#### Proof

All later color vectors in (2.8) are nonnegative. A repeated first-cut
color makes the corresponding coefficient of \(R_\pi\) negative, which
is impossible. \(\square\)

Thus a permutation and Johnson adjacency at the first cut are not, by
themselves, a meaningful notion of balance.

## 3. Exact balanced first-layer completion

Assume \(s\ge2\). Join \(P\) to \(Q\) in a bipartite graph \(\Gamma_1\)
exactly when

\[
 |i_0(P)\triangle i_1(Q)|=2,
 \qquad
 |i_1(Q)\triangle i_2(P)|=2.                           \tag{3.2}
\]

Label every edge \(P\leftrightarrow Q\) of \(\Gamma_1\) by

\[
 \chi(P,Q)=
 e_{i_0(P)\cup i_1(Q)}
 +e_{i_1(Q)\cup i_2(P)}.                               \tag{3.1}
\]

The identity edges \(P\leftrightarrow P\) form one perfect matching.

### Definition 3.1

A permutation \(\pi\in\operatorname {Sym}(D)\) is **two-cut balanced** if

1. every edge \(P\leftrightarrow\pi P\) belongs to \(\Gamma_1\); and
2.

   \[
   \boxed{
   \sum_{P\in D}\chi(P,\pi P)
   =\sum_{P\in D}\chi(P,P).}                            \tag{3.3}
   \]

Condition (3.3) is labelled \(Y\)-balance. Equality only after taking
coordinate marginals is weaker and is not sufficient.

### Theorem 3.2 (balanced first-layer completion)

Every two-cut balanced \(\pi\) has the exact completion

\[
                         p_0=1,\quad p_1=\pi,\quad
                         p_t=1\quad(2\le t\le s).        \tag{3.4}
\]

Conversely, (3.2)--(3.3) are necessary for a completion of this form.

#### Proof

Only cuts zero and one change. Condition (3.2) proves both Johnson
adjacencies through every new phase-one state. Since \(\pi\) is a
permutation, the phase-one \(X\)-layer is still \(L_1\).

The old and new aggregate colors on the two changed cuts are the two sides
of (3.3). All later cuts are unchanged, so the full \(Y\)-palette remains
exact. Finally \(p_2=p_0=1\), and every subsequent \(p_t\) is one, so the
ports close with zero monodromy. This proves sufficiency. Each condition is
read directly from any completion (3.4), proving necessity. \(\square\)

In relative form this completion is

\[
                         \sigma_0=\pi,\qquad
                         \sigma_1=\pi^{-1},\qquad
                         \sigma_t=1\ (t\ge2).           \tag{3.5}
\]

Thus the monodromy cancellation is literal and uses no later absorption.

### Corollary 3.3 (zero-labelled alternating cycles)

Compare the perfect matching \(P\leftrightarrow\pi P\) in \(\Gamma_1\)
with the identity matching. Their symmetric difference is a disjoint union
of alternating cycles. The permutation \(\pi\) is two-cut balanced exactly
when the sum of the signed \(\chi\)-labels of those cycles is zero.

Hence every zero-labelled alternating-cycle system, including cycles with
arbitrarily many row vertices, completes by Theorem 3.2. Two-row cycles
are the octahedral rectangles; longer zero-labelled cycles are allowed and
need not be decomposed into rectangles for the completion theorem.

## 4. A uniform Catalan cube of balanced first layers

For \(R\in D_{2s-4}^0\), let \(S_R\subseteq\{5,\ldots,2s\}\) be the
shifted up-step set of \(R\). Consider the two roots

\[
                         x_R=1100R,\qquad y_R=1010R.    \tag{4.1}
\]

The first three canonical states are

\[
\begin{array}{c|ccc}
x_R&S_R\cup12&S_R\cup14&S_R\cup34\\
y_R&S_R\cup13&S_R\cup23&S_R\cup24.
\end{array}                                             \tag{4.2}
\]

Let \(\tau_R\) transpose \(x_R,y_R\) and fix every other root.

### Lemma 4.1 (one rectangle is balanced)

The permutation \(\tau_R\) is two-cut balanced.

#### Proof

After exchanging the two phase-one states, the two rows become

\[
                         S_R\cup(12,23,34),\qquad
                         S_R\cup(13,14,24).             \tag{4.3}
\]

All four new adjacencies are Johnson edges. Before and after the switch,
the four union colors are exactly

\[
                         S_R\cup\{123,124,134,234\}.    \tag{4.4}
\]

Thus (3.2)--(3.3) hold. \(\square\)

### Theorem 4.2 (uniform simultaneous completion)

For every subfamily \(\mathcal R\subseteq D_{2s-4}^0\), put

\[
                         \pi_{\mathcal R}
                         =\prod_{R\in\mathcal R}\tau_R. \tag{4.5}
\]

Then \(\pi_{\mathcal R}\) is two-cut balanced, and

\[
 p_0=1,\quad p_1=\pi_{\mathcal R},\quad
 p_t=1\quad(2\le t\le s)                               \tag{4.6}
\]

is an exact fixed-layer \(D\)-port factor.

#### Proof

Distinct \(R\)'s give disjoint root pairs in (4.1), so the transpositions
commute. Their old row supports are disjoint. Since the canonical factor is
exact and each rectangle preserves its own four-color set (4.4), the
\(X/Y\) ledgers of different rectangles are disjoint and their balance
equations add. Theorem 3.2 completes the product. \(\square\)

There are exactly \(\operatorname {Cat}_{s-2}\) independent bits, proving
the cube dimension. The acted-on row fraction is

\[
 {2\operatorname {Cat}_{s-2}\over\operatorname {Cat}_s}
 ={s(s+1)\over2(2s-1)(2s-3)}
                         \longrightarrow{1\over8}.       \tag{4.7}
\]

This is uniform in \(s\). It may be inserted in any aligned context by the
port-substitution theorem.

### Theorem 4.3 (uniformity at every phase \(q\))

Fix \(0\le q\le s-2\). For

\[
 P\in D_{2q}^0,\qquad R\in D_{2(s-q-2)}^0,
\]

consider the roots

\[
                         P1100R,\qquad P1010R.           \tag{4.8}
\]

Their canonical paths have, at phases \(q,q+1,q+2\), a common spectator
extension of the two rows in (4.2). Consequently the transposition of the
two phase-\((q+1)\) states is two-cut balanced on cuts \(q,q+1\).

For fixed \(q\), the

\[
                         \operatorname {Cat}_q
                         \operatorname {Cat}_{s-q-2}    \tag{4.9}
\]

root pairs are disjoint. Any subfamily may be switched simultaneously,
with every other phase permutation equal to the identity, giving an exact
fixed-layer factor.

#### Proof

The MSW concatenation law processes the complete prefix \(P\), then the
displayed four-letter block, then the suffix \(R\). During the two cuts of
the four-letter block, all coordinates belonging to the already processed
prefix and the untouched suffix form one common spectator set. Suppressing
that set gives exactly (4.2)--(4.4), so each transposition is two-cut
balanced.

For fixed \(q\), the factorization

\[
                         P\,\{1100,1010\}\,R             \tag{4.10}
\]

uniquely recovers \(P\), the middle choice, and \(R\). Hence the root
pairs are disjoint. Their canonical color supports are disjoint by exactness
of the original factor, so the balance equations add. The same proof as
Theorem 3.2 returns to the identity phase immediately after the changed
middle layer. \(\square\)

Rectangles belonging to different values of \(q\) may share roots. Theorem
4.3 asserts a product cube for each fixed \(q\), not simultaneous
independence across all phase indices.

## 5. Exact scope for constant one

The fixed-layer phase problem now has a precise hierarchy.

1. Equations (2.4)--(2.6) are the complete algebraic constraints.
2. A prescribed first layer has the exact residual problem
   (2.8)--(2.9).
3. Two-cut labelled balance has the explicit completion (3.4).
4. The Catalan cube (4.5) supplies a positive-density, all-scale family of
   such completions.
5. The contextual version (4.8) supplies
   \(\operatorname {Cat}_q\operatorname {Cat}_{s-q-2}\) exact atoms at
   every fixed phase \(q\).

What is not proved is that a first layer satisfying only a coarse
coordinate balance can be completed. Equation (3.3) shows the missing
information: every individual \((s+1)\)-color, not merely every coordinate
marginal, must balance if the tail is returned at phase two. With an
arbitrary later tail, (2.8)--(2.9) remain the exact completion gate.

For coefficient one, one would additionally need a q-uniform selection of
these or longer zero-labelled cycles whose full carrier-resolved
multidepth profiles fit the current residual capacities. The present cube
acts on only \((1/8+o(1))\) of the rows and has correlated effects at all
depths. It is an exact integral seed library, not yet a global cap theorem.

## 6. Final statement

\[
 \boxed{\text{Every exactly two-cut-balanced prescribed first layer has a
 q-uniform exact Chung--Feller completion.}}             \tag{6.1}
\]

The balance required is the labelled \(Y\)-palette equation (3.3), together
with the two Johnson adjacencies. Under this condition the completion is
\((1,\pi,1,\ldots,1)\); no asymptotic matching theorem or finite
verification is needed.
