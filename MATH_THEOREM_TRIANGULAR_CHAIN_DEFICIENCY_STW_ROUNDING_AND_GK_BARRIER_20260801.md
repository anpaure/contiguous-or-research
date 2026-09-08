# Triangular chain deficiency, asymptotic integral rounding, and the Greene--Kleitman barrier

Date: 2026-08-01  
Status: exact formulation and unconditional asymptotic integral theorem.  The
exact zero-defect triangular factor and endpoint serialization remain open.

## 0. Summary

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,\qquad
 W=\binom{k}{r},\qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
\]

\[
 \Lambda=|\mathcal L|,qquad
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\},
 \qquad D=\left\lceil\frac\Lambda W\right\rceil,
\]

and

\[
                         h=(\Lambda-dW)_+.
\]

The exact fractional triangular theorem in
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`
is correct.  It gives zero fractional deficiency using `W` anchored
depth-`d` chains and boundary capacities `1,2,...,d`.

This note proves three further facts.

1. The correct integral quantity is one **triangular chain-atom
   deficiency** `Gamma_d^triangle`, not solely the stronger anchored
   deficiencies `gamma_D` or `gamma_d`.
2. The upper-half construction of Sudakov--Tomon--Wagner gives

   \[
   \boxed{
   \gamma_q\le(\Lambda-qW)_+
       +O(\Lambda k^{-1/16})
   }
   \qquad(q\in\{d,D\}).                              \tag{0.1}
   \]

   Consequently

   \[
   \gamma_D=O(\Lambda k^{-1/16})=o(\Lambda),         \tag{0.2}
   \]

   and

   \[
   \Gamma_d^\triangle
       \le h+O(\Lambda k^{-1/16})=o(\Lambda).        \tag{0.3}
   \]

   Thus the sharp fractional factor does have a sublinear-defect integral
   rounding.  The unresolved jump is from `o(Lambda)` to zero or `O(1)`.
3. Greene--Kleitman saturation does not make this jump.  Its `q`-norm is a
   **minimum** theorem, whereas a maximum chain-length cap requires the
   `q`-norm to attain its largest possible value.  Cardinality-restricted
   chain covering is a different, generally NP-complete problem.

## 1. The exact triangular integral object

For an owner `T in binom([k],r)`, let `A_T(d)` be the family of inclusion
chains of nonempty strict subsets of `T` having at most `d` members.

For `1<=i<=d`, introduce one unanchored boundary address `partial_i`, and let
`A_(partial_i)` be the family of arbitrary inclusion chains in `mathcal L`
having at most `i` members.  Empty chains are allowed at every address.

An **integral triangular selection** chooses

\[
 C_T\in\mathcal A_T(d)
 \quad(T\in\tbinom{[k]}r),
 \qquad
 C_{\partial_i}\in\mathcal A_{\partial_i}
 \quad(1\le i\le d),                                \tag{1.1}
\]

with all chosen target sets pairwise disjoint.

### Definition 1.1 (triangular chain deficiency)

Define

\[
 \boxed{
 \Gamma_d^\triangle
   =\Lambda-
      \max\left|
        \bigcup_T C_T\ \cup\
        \bigcup_{i=1}^d C_{\partial_i}
      \right|.}                                     \tag{1.2}
\]

Then `Gamma_d^triangle=0` if and only if the complete lower ideal has the
exact static chain decomposition required by the `B(k)=W+d` triangular
endpoint profile.

The hypergraph form is literal.  Its vertex set is

\[
 \mathcal L\ \dot\cup\ \binom{[k]}r
 \ \dot\cup\ \{\partial_1,\ldots,\partial_d\},
\]

and an atom consists of one address vertex together with the members of one
legal chain at that address.  A triangular selection is a matching using
every address exactly once; its uncovered lower vertices are counted by
(1.2).

The theorem
`MATH_THEOREM_OPTIMAL_TRIANGULAR_FRACTIONAL_CHAIN_FACTOR_20260801.md`
proves that the LP relaxation of this hypergraph has deficiency zero.

For comparison, let

\[
 \gamma_q=\Lambda-max\left\{
   \left|\bigcup_T C_T\right|:
   C_T\text{ are target-disjoint anchored chains of length }\le q
                         \right\}.                   \tag{1.3}
\]

The elementary relations are

\[
 \boxed{
  (\gamma_d-\tbinom{d+1}{2})_+
       \le \Gamma_d^\triangle\le\gamma_d.}          \tag{1.4}
\]

Indeed, deleting the boundary atoms gives the upper bound.  Conversely the
boundary atoms contain at most `binom(d+1,2)` targets in total, proving the
lower bound.

Thus `gamma_D=0` is a convenient sufficient theorem, but it gives one
extra row at every owner and is stronger than the exact physical target.
The exact coefficient-one static question is `Gamma_d^triangle=0`.

For additive slack `C`, define `Gamma_(d+C)^triangle` in the same way with
owner capacity `d+C` and boundary capacities `1,...,d+C`.  A bounded value
of this deficiency gives a bounded static casualty set, but a word still
requires the sliding-OR cocycle and all upper/residence rows.

## 2. An asymptotic integral rounding theorem

The required input is an explicit intermediate conclusion in the proof of
Sudakov--Tomon--Wagner's uniform-chain theorem.

Let

\[
                         s_k=\frac{2^k}{W},
 \qquad K=\left\lceil\frac{s_k}{2}\right\rceil,
 \qquad \lambda=k^{-1/16}.                          \tag{2.1}
\]

They partition the upper Boolean half

\[
                         \mathcal B^+
       =\{S\subseteq[k]:|S|\ge r\}                  \tag{2.2}
\]

into exactly `W` chains so that all but

\[
                         O(Wk^{-1/8})                \tag{2.3}
\]

chains have size between

\[
                         K-3\lambda K
             \quad\text{and}\quad
                         K+3\lambda K.              \tag{2.4}
\]

This is the upper-half statement proved in their Section 2.7 before the
complementary lower shore is attached.

### Theorem 2.1 (sublinear-defect sharp-depth factor)

For `q=d` and for `q=D`,

\[
 \gamma_q\le(\Lambda-qW)_+
            +O(\Lambda k^{-1/16}).                  \tag{2.5}
\]

#### Proof: odd `k=2m+1`

Here `r=m+1`.  Complement the chain partition (2.2).  It becomes a
partition of the sets of ranks at most `m` into `W` chains.  Remove the
empty set.  Every chain has one rank-`m` maximum because the upper chain had
one rank-`r` minimum.

In every chain retain its top `q` members (or the whole chain if it is
shorter).  The retained families are target-disjoint chains of length at
most `q`.  Match their distinct rank-`m` maxima to distinct rank-`r` owners;
the regular containment graph between the two central layers has a perfect
matching.  This makes all retained chains anchored.

For `q in {d,D}` we have

\[
                         q=K+O(1),                  \tag{2.6}
\]

because `d<=D<=d+1`, `D=ceil(Lambda/W)`, and in odd dimension
`Lambda=2^(k-1)-1`.

Every typical chain in (2.4) therefore retains at least

\[
                         q-O(\lambda K)-O(1)         \tag{2.7}
\]

lower targets.  Multiplying by the `W-O(Wk^(-1/8))` typical chains gives

\[
 \text{covered}
 \ge qW-O(W\lambda K)-O(Wk^{-1/8}K)-O(W).           \tag{2.8}
\]

Since `WK=Theta(Lambda)` and `lambda=k^(-1/16)`, the error in (2.8) is
`O(Lambda k^(-1/16))`.  Comparing with the total `Lambda` gives (2.5).

#### Proof: even `k=2m`

Now `r=m`.  Complementing (2.2) partitions all sets of rank at most `m`
into `W` chains, each with one rank-`m` maximum.  Remove the empty set.

For each owner chain retain its maximum together with its top `q` strict-
lower members.  Thus its total retained length is at most `q+1`; after the
rank-`m` maximum is removed it is an anchored strict-lower chain of length
at most `q`.

Again

\[
                         q+1=K+O(1),                 \tag{2.9}
\]

because

\[
                         \Lambda=\frac{2^k-W}{2}-1.
\]

The same multiplication as in (2.8), followed by deletion of the `W`
owner maxima, gives

\[
 \text{strict-lower covered}
 \ge qW-O(\Lambda k^{-1/16}).                        \tag{2.10}
\]

Comparison with `Lambda` proves (2.5).  \(\square\)

### Corollary 2.2 (the three present integral scales)

Since `DW>=Lambda`, Theorem 2.1 gives

\[
                         \gamma_D
       =O(\Lambda k^{-1/16})=o(\Lambda).             \tag{2.11}
\]

At the true owner depth,

\[
                         \gamma_d
       \le h+O(\Lambda k^{-1/16}).                   \tag{2.12}
\]

Finally (1.4) gives

\[
 \boxed{
                         \Gamma_d^\triangle
       \le h+O(\Lambda k^{-1/16})=o(\Lambda).}       \tag{2.13}
\]

The scalar `h<=binom(d+1,2)=O(k)` is negligible compared with `Lambda`.
The new fractional theorem removes it exactly, but the present integral
rounding does not yet correlate the discarded targets into the `d`
boundary chains.

Primary source: B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain
decompositions and applications*, Random Structures & Algorithms 60
(2022), 261--286, arXiv:1911.09533; see especially Sections 2.2 and 2.7.

## 3. Why Greene--Kleitman saturation points the other way

For a chain partition `mathscr C` of a finite poset `P`, define its
`t`-norm by

\[
                         \|\mathscr C\|_t
       =\sum_{C\in\mathscr C}\min(t,|C|).            \tag{3.1}
\]

Let `alpha_t(P)` be the maximum number of elements in a union of `t`
antichains.  Greene--Kleitman proves

\[
                         \alpha_t(P)
       =\min_{\mathscr C}\|\mathscr C\|_t.          \tag{3.2}
\]

A partition attaining this minimum is called `t`-saturated, and their
simultaneous theorem supplies a partition which is both `t`- and
`(t+1)`-saturated.

This does not imply a deadline-bounded partition.

### Proposition 3.1 (norm-direction obstruction)

A chain partition has maximum chain size at most `t` if and only if

\[
                         \|\mathscr C\|_t=|P|,       \tag{3.3}
\]

which is the **largest** possible `t`-norm.  If the height of `P` exceeds
`t`, then

\[
                         \alpha_t(P)<|P|,            \tag{3.4}
\]

so every `t`-saturated partition has a chain longer than `t`.

#### Proof

Each summand in (3.1) equals `|C|` exactly when `|C|<=t`; summing proves
(3.3).  If `P` contains a chain of `t+1` elements, no union of `t`
antichains contains that whole chain, so `alpha_t(P)<|P|`.  Equations
(3.2)--(3.3) finish the proof.  \(\square\)

At `t=d=Theta(sqrt(k))`, the Boolean lower half has height
`r-1=Theta(k)>d`.  Hence a Greene--Kleitman `d`-saturated partition is
forced to contain chains longer than the deadline.  Saturation makes the
chain-size vector as concentrated into long chains as the `d`-norm permits;
the OR problem asks for the opposite balancing operation.

There is a second mismatch.  The triangular target prescribes one common
partition satisfying the complete heterogeneous capacity vector

\[
                         (\underbrace{d,\ldots,d}_{W},d,d-1,\ldots,1).
                                                               \tag{3.5}
\]

Strong-Sperner inequalities verify every separate antichain-capacity row
for (3.5), but Greene--Kleitman only minimizes one norm (or two adjacent
norms) at a time.  It does not manufacture one partition dominated by the
whole vector (3.5), and it contains no owner labels.

This is not merely a missing manipulation of Dilworth's proof.  The minimum
chain-cover problem with a prescribed maximum chain cardinality is
NP-complete for general posets (H. Shum and L. E. Trotter, *Cardinality-
restricted chains and antichains in partially ordered sets*, Discrete
Appl. Math. 65 (1996), 421--439).  A sharp positive theorem must exploit
special Boolean exchange structure.

## 4. Exact frontier

The static lower compiler now has four rigorously separated levels:

\[
\begin{array}{c}
\text{optimal triangular fractional factor}\quad\text{(zero defect)}\\
\Downarrow\\
\text{optimal triangular integral factor}
 \quad\text{(defect }O(\Lambda k^{-1/16})\text{ proved; zero open)}\\
\Downarrow\\
\text{two-endpoint/sliding-OR serialization}\quad\text{(open)}\\
\Downarrow\\
\text{upper, residence and common-cap compatible word}.
\end{array}                                             \tag{4.1}
\]

The shortest sharp static theorem is

\[
                         \boxed{\Gamma_d^\triangle=0.} \tag{4.2}
\]

For an additive theorem it would suffice statically to prove, for one
absolute `C`, either

\[
                         \Gamma_{d+C}^\triangle=0
 \quad\text{or}\quad
                         \Gamma_{d+C}^\triangle=O(1), \tag{4.3}
\]

with the bounded casualties appended only at the terminal dimension.
Neither (4.2) nor (4.3) follows from Greene--Kleitman saturation or the
present asymptotic uniform-chain theorem.

