# Asymptotically sharp anchored chain factor from the STW upper-half construction

Date: 2026-08-01  
Status: **independently audited PASS, with the source and parity scope made
explicit below**.  Sudakov--Tomon--Wagner (STW) state their main theorem for
the full Boolean lattice, but Section 2.7 of their proof first constructs the
approximately uniform upper-half partition needed here.  Their later
Conjecture 3 concerns arbitrary prescribed half-chain lengths and does not
retract or make conditional this special uniform construction.

## 0. Statement

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom{k}{r},
 \qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|,
\]

and let

\[
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\}.
\]

For all sufficiently large `k`, there are pairwise target-disjoint chains

\[
 C_T\subseteq 2^T\setminus\{\varnothing,T\},
 \qquad |C_T|\le d,
 \qquad T\in\binom{[k]}r,
\]

such that

\[
 \boxed{
 \Lambda-\left|\bigcup_T C_T\right|
   =O\!\left(\Lambda k^{-1/16+o(1)}\right).}
 \tag{0.1}
\]

Equivalently, the anchored cap-`d` deficiency satisfies

\[
 \gamma_d=O\!\left(\Lambda k^{-1/16+o(1)}\right)=o(\Lambda).
 \tag{0.2}
\]

The `o(1)` in the exponent is harmless and may be omitted from the dominant
STW truncation term; it is retained here to absorb their atypical-chain
count uniformly.

## 1. The exact STW input

Let

\[
 s_k=\frac{2^k}{W},\qquad
 K=\left\lceil\frac{s_k}{2}\right\rceil,
 \qquad \lambda=k^{-1/16}.
 \tag{1.1}
\]

In Section 2.7, STW partition

\[
 \mathcal B^+=\{S\subseteq[k]:|S|\ge r\}
 \tag{1.2}
\]

into exactly `W` chains.  Their final estimates imply that all but

\[
 O\!\left(Wk^{-1/8+o(1)}\right)
 \tag{1.3}
\]

of those chains have length

\[
 K+O(1)+O(\lambda K).
 \tag{1.4}
\]

More literally, their construction gives a lower endpoint
`K+1-3 lambda K` and an upper endpoint `K+1+lambda K`, up to the harmless
integer convention in `K`.  Formula (1.4) is the only form used below.

This upper-half conclusion is not merely inferred from the stated
full-lattice Theorem 1.  It is the intermediate partition denoted
`D*` in the proof: STW first partition the upper half and only afterwards
join it to the complementary shore to prove their full-lattice theorem.

STW's Conjecture 3 has different quantifiers.  It asks for an upper-half
decomposition approximating an *arbitrary prescribed dominated sequence*
of chain lengths.  The special nearly uniform upper-half partition (1.2)--
(1.4) is already proved and is sufficient here.

Primary source: B. Sudakov, I. Tomon and A. Z. Wagner,
*Uniform chain decompositions and applications*, Random Structures &
Algorithms 60 (2022), 261--286, arXiv:1911.09533.  See especially Section
2.7, including the construction and final count of the partition `D*`.

## 2. Scalar comparison with the sharp depth

Let

\[
 D=\left\lceil\frac{\Lambda}{W}\right\rceil.
\]

Since `K=Theta(sqrt(k))`, while `W` is exponential in `k`, the triangular
term is negligible compared with one owner row.  Hence, for all sufficiently
large `k`,

\[
 d\in\{D-1,D\},\qquad d=K+O(1),\qquad D=K+O(1).
 \tag{2.1}
\]

The parity-specific identities behind (2.1) are

\[
 \Lambda=2^{k-1}-1
 \quad(k\text{ odd}),
 \tag{2.2}
\]

and

\[
 \Lambda=2^{k-1}-\frac W2-1
 \quad(k\text{ even}).
 \tag{2.3}
\]

Thus a typical STW half-chain has enough members to contribute
`d-O(lambda K)-O(1)` strict-lower targets after the parity-specific central
rank is handled.

## 3. Odd anchoring

Let `k=2m+1`, so `r=m+1` and the two middle ranks both have size `W`.
Complement every STW upper-half chain.  This partitions the sets of ranks at
most `m` into `W` chains.  Each complemented chain has a distinct rank-`m`
maximum: the original upper-half partition has `W` chains and covers the
`W` rank-`m+1` sets, while a chain contains at most one such set.

Delete the empty set globally; it occurs in only one chain.  In each
remaining chain retain its top `d` nonempty members, or all its members if
fewer remain.

The bipartite containment graph between ranks `m` and `m+1` is regular:
every vertex on either shore has degree `m+1`.  It therefore has a perfect
matching.  Match the distinct rank-`m` maxima to distinct rank-`m+1` owners
and assign each retained chain to the matched owner.  Every retained member
is a strict subset of that owner.

No owner is deleted in odd dimension: the owners lie at rank `m+1`, outside
the complemented lower half.  The perfect matching is the entire odd
anchoring step.

## 4. Even anchoring

Let `k=2m`, so `r=m`.  Complementation partitions all sets of ranks at most
`m` into `W` chains with distinct rank-`m` maxima.  Those maxima themselves
are the `W` owners.

Delete the rank-`m` maximum from every chain and delete the empty set
globally.  In each resulting strict-lower chain retain its top `d` members,
or all its members if fewer remain.  The retained chain is automatically
contained in its deleted rank-`m` owner.

This is the parity row that must not be conflated with Section 3: even
dimension deletes one owner element per chain, whereas odd dimension uses a
middle-layer perfect matching and deletes no owner element.

## 5. Coverage calculation

Let `G` be the typical STW chains.  From (1.3),

\[
 |G|=W-O\!\left(Wk^{-1/8+o(1)}\right).
\]

Sections 2--4 and (1.4) show that every chain in `G` contributes at least

\[
 d-O(\lambda K)-O(1)
\]

strict-lower targets.  Ignoring all contributions from atypical chains
therefore gives

\[
 \begin{aligned}
 \left|\bigcup_T C_T\right|
 &\ge dW
   -O(W\lambda K)
   -O\!\left(Wk^{-1/8+o(1)}K\right)
   -O(W)\\
 &=dW-O\!\left(\Lambda k^{-1/16+o(1)}\right),
 \end{aligned}
 \tag{5.1}
\]

because `WK=Theta(Lambda)`.  Consequently

\[
 \gamma_d
 \le (\Lambda-dW)_+
      +O\!\left(\Lambda k^{-1/16+o(1)}\right).
 \tag{5.2}
\]

The definition of `d` gives

\[
 (\Lambda-dW)_+\le\binom{d+1}{2}=O(k),
 \tag{5.3}
\]

which is swallowed by the error term in (5.2).  This proves (0.1)--(0.2).

The source controls the *number* of atypical chains, not their total mass.
Equation (5.1) deliberately avoids a bad-chain mass assertion: it lower
bounds coverage solely by the retained contribution of the typical chains.

## 6. Exact scope

The theorem is unconditional and proves an asymptotically sharp static
anchored cap-`d` chain packing.  It does **not** prove any of the following:

1. exact or `O(1)` uncovered deficiency;
2. an integral realization of the triangular boundary chains of capacities
   `1,2,...,d`;
3. the sliding suffix-OR cocycle or a serial endpoint chronology;
4. residence, protected upper shadows, topology, or a common compiler cap.

Thus STW closes the coefficient-one static problem up to a sublinear leave,
but the Boolean absorber and physical serialization gates remain open.

