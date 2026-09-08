# Dense Ferrers rounding contains a unit-scale upper-half chain-deletion problem

**Date:** 2026-08-03  
**Status:** unconditional static reduction for every even dimension and every
fixed complete cyclic depth-`d` carrier.  The final section compares its scale
with a published asymptotic chain-decomposition theorem.  No computation is
used.  This note does **not** construct the required chain partition or a
physical factor.

## 0. Outcome

Let `k=2m`, put

\[
 r=m,\qquad W={k\choose r},\qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},\qquad
 \Lambda=|\mathcal L|,
\]

and let

\[
 d=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\}.
 \tag{0.1}
\]

Define the static anchored-chain deletion number

\[
 \gamma_d(k)=\min |D|,                                      \tag{0.2}
\]

where the minimum is over `D subseteq mathcal L` for which
`mathcal L setminus D` can be partitioned into `W` (possibly empty)
inclusion chains `C_T`, indexed by the rank-`r` owners, such that

\[
 |C_T|\le d,\qquad S\subseteq T\quad(S\in C_T).             \tag{0.3}
\]

Let

\[
 \mathcal U^- =\{S\subseteq[k]:r\le |S|\le k-1\}.          \tag{0.4}
\]

Then `gamma_d(k)` is **exactly** the minimum number of elements which must
be deleted from `mathcal U^-` so that the remainder has a partition into
`W` chains, each of size at most `d+1`, with the `W` middle sets occurring
one per chain.

Now fix any complete cyclic rank-`r` carrier and any depth-`d` factor on it.
Suppose distinct cyclic lower cells represent all but `c` named lower
targets after a separate boundary bank represents at most `b_partial`
targets.  Then

\[
 \boxed{\gamma_d(k)\le c+b_{\partial}.}                     \tag{0.5}
\]

In particular, for the optimal triangular boundary bank

\[
 b_{\partial}\le {d+1\choose2}=O(k)=o(W),                  \tag{0.6}
\]

an `o(W)` integral named-target rounding on the dense punctured-Ferrers
face would imply

\[
 \boxed{\gamma_d(k)=o(W).}                                  \tag{0.7}
\]

This is a unit-scale upper-half uniform-chain deletion statement.  It is
strictly before simultaneous interval closure, Euler serialization, upper
coverage, or regeneration.  Thus neither the ideal containment SDR nor the
fractional pull-clock circulation can be rounded to `o(W)` named-target
defect by a generic discrepancy argument unless that argument also proves
(0.7).

The scale is much sharper than the presently published asymptotic uniform
chain theorem.  The explicit estimates of Sudakov--Tomon--Wagner certify
the upper bound

\[
 2^k k^{-1/8+o(1)}=Wk^{3/8+o(1)},                           \tag{0.8}
\]

and additive good-chain length fluctuations of order `k^(7/16)`.  These
are valuable `o(Lambda)` estimates, but neither is `o(W)`.  Therefore that
theorem cannot be cited as the missing dense named-target rounding.

## 1. The static chain parameter

The owner labels in (0.2)--(0.3) are not decorative.  A chain `C_T` must
lie below its named owner `T`; empty chains are allowed so that there are
always exactly `W` indexed chains.

Define independently

\[
 \Gamma_d(k)=\min |D'|,                                    \tag{1.1}
\]

where `D' subseteq mathcal U^-` and `mathcal U^- setminus D'`
admits a partition into `W` chains of size at most `d+1`, each containing
exactly one member of `binom([k],r)`.

### Theorem 1.1 (exact complement equivalence)

For every even `k`,

\[
 \boxed{\gamma_d(k)=\Gamma_d(k).}                           \tag{1.2}
\]

### Proof

Suppose first that `(C_T:T in binom([k],r))` witnesses (0.2).  Adjoin its
owner to every chain:

\[
                         \widehat C_T=C_T\cup\{T\}.          \tag{1.3}
\]

This remains a chain by (0.3), has size at most `d+1`, and the family of
all `widehat C_T` partitions

\[
       \{S:1\le |S|\le r\}\setminus D.                       \tag{1.4}
\]

Complementation reverses inclusion and, because `k=2r`, preserves the
middle rank.  Hence

\[
 \overline{\widehat C_T}
   =\{[k]\setminus S:S\in\widehat C_T\}                    \tag{1.5}
\]

is a chain in `mathcal U^-`, contains the unique middle set
`[k] setminus T`, and the `W` complemented chains partition
`mathcal U^- setminus overline D`.  Their sizes are unchanged.  Therefore
`Gamma_d(k)<=gamma_d(k)`.

Conversely, every chain counted by `Gamma_d(k)` contains one middle set,
because the `W` chains partition the `W` middle sets and no chain contains
two distinct equal-rank sets.  Complement all chains and remove their
distinct middle members.  What remains is a family of `W` chains of size at
most `d`, indexed by their containing middle members, partitioning the
strict lower ideal apart from the complemented deletion set.  This proves
the reverse inequality. `square`

The scalar lower bound on either parameter is

\[
 \gamma_d(k)=\Gamma_d(k)\ge (\Lambda-dW)_+.                 \tag{1.6}
\]

Indeed, after the middle owner is removed, the `W` chains have only `dW`
lower positions.  By (0.1), the right side of (1.6) is at most
`binom(d+1,2)`; the scalar deficit is therefore small, while the integral
chain-deletion problem is not thereby solved.

There is an exact fractional comparison.  Let `gamma_d^*(k)` be the
deficiency of the fractional owner-chain atom hypergraph: an atom consists
of one owner together with one chain of at most `d` strict-lower targets
below it; atom weights give every owner total load one (empty chains are
allowed), give every target load at most one, and the objective is total
target load.

### Theorem 1.2 (exact fractional deletion value)

For every even `k` in the notation of this note (and, with
`r=ceil(k/2)` and the same definitions of `Lambda` and `d`, by the
identical proof in either parity),

\[
 \boxed{\gamma_d^*(k)=(\Lambda-dW)_+.}                       \tag{1.7}
\]

Consequently the entire static rounding question on even dimensions is the
integrality gap

\[
 \gamma_d(k)-\gamma_d^*(k).                                 \tag{1.8}
\]

### Proof

No fractional selection can carry more than `d` targets per unit owner
mass, proving the lower bound in (1.7).

For the reverse bound put

\[
 p_s={{k\choose s}\over W},\qquad1\le s<r.                  \tag{1.9}
\]

Choose numbers `0<=q_s<=p_s` with

\[
 \sum_s q_s=\min\left(d,{\Lambda\over W}\right).            \tag{1.10}
\]

Because `p_s<=1` and the sum in (1.10) is at most `d`, the vector `q` lies
in the independence polytope of the uniform matroid of rank `d` on the
rank indices.  Hence there is a random set
`R subseteq {1,...,r-1}` of size at most `d` with

\[
                         \Pr(s\in R)=q_s.                    \tag{1.11}
\]

For every owner `T`, choose a uniform ordering of its `r` coordinates and
retain, as one owner-chain atom, the initial subsets at the ranks in `R`.
Average this construction over all owners, orderings, and sets `R`, giving
each owner total atom mass one.

A fixed rank-`s` target `S` is contained in
`binom(k-s,r-s)` owners.  In one such owner it is the initial `s`-set with
probability `q_s/binom(r,s)`.  Its total fractional load is therefore

\[
 { {k-s\choose r-s}q_s\over {r\choose s}}
      ={Wq_s\over {k\choose s}}
      ={q_s\over p_s}\le1.                                  \tag{1.12}
\]

The total target load is

\[
 \sum_{s=1}^{r-1}{k\choose s}{q_s\over p_s}
      =W\sum_s q_s=\min(\Lambda,dW).                         \tag{1.13}
\]

This attains the capacity upper bound and proves (1.7). `square`

Theorem 1.2 is deliberately static.  It neither balances literal trace
states nor selects one integral atom per owner.  It shows exactly why
fractional rank marginals have no remaining separator while the named
integral deletion parameter can still be positive.

## 2. Every dense factor projects to the static problem

Let

\[
 T_j=\bigcup_{h=j-d}^{j}A_h\in{[k]\choose r},
 \qquad j\in\mathbb Z_W,                                  \tag{2.1}
\]

be a complete cyclic carrier factor: the `T_j` are all the rank-`r` sets,
once each.  A cyclic lower cell ending at `j` has the form

\[
 Q_{j,q}=\bigcup_{h=j-q+1}^{j}A_h,
 \qquad 1\le q\le d.                                      \tag{2.2}
\]

For one fixed endpoint,

\[
 Q_{j,1}\subseteq Q_{j,2}\subseteq\cdots\subseteq Q_{j,d}
 \subseteq T_j.                                            \tag{2.3}
\]

The inclusions need not be strict, but distinct named targets assigned to
these cells form a strict subchain.

### Theorem 2.1 (factor-to-chain deletion inequality)

Suppose a set `B subseteq mathcal L` of at most `b_partial` targets is
assigned to external boundary cells, and all but `c` other lower targets
are assigned injectively to cyclic cells (2.2) having the same literal
value.  Then (0.5) holds.

### Proof

Group the cyclically assigned targets by the right endpoint of their
assigned cell.  Equation (2.3) makes every group an inclusion chain of
size at most `d`, contained in its owner `T_j`.  Injectivity of the cell
assignment and distinctness of named Boolean targets make the groups
disjoint.  The complete carrier labels the `W` groups by all middle owners.
They cover every target outside the `c` omissions and the boundary set
`B`.  Thus they witness

\[
                         \gamma_d(k)\le c+|B|\le c+b_\partial.
\]

`square`

The converse is false without additional hypotheses.  A static chain
partition need not satisfy the sliding suffix cocycle

\[
 Q_{j,q}=Q_{j-1,q-1}\cup Q_{j,1},                           \tag{2.4}
\]

and a target-to-cell assignment on one carrier must additionally satisfy
the simultaneous interval-closure criterion coordinate by coordinate.
Thus `gamma_d` is a necessary projection of dense Ferrers rounding, not a
replacement for the physical theorem.

## 3. Why the fractional theorems stop before this parameter

The ideal owner SDR and the symmetric fractional owner-chain theorem prove
respectively:

1. every lower target has a distinct containing labelled owner slot at
   depth at most `d+1`; and
2. the owner-chain atom hypergraph has the scalar-optimal fractional point.

Neither theorem proves an integral matching of chain atoms.  Equivalently,
both forget `gamma_d`.  The corrected pull-clock theorem adds a stationary
fractional literal trace law, but its convex combination may repeat owners
and named targets.  It also leaves (0.2) unresolved.

Consequently the proposed implication

\[
 \text{fractional pull clock + equitable ideal SDR}
 \Longrightarrow o(W)\text{ named-target defect}             \tag{3.1}
\]

already contains the new static assertion `gamma_d(k)=o(W)` for every even
`k`, before chronology or interval closure is tested.

The required precision is easy to quantify.  Since

\[
 |\mathcal U^-|=\Lambda+W=\Theta(\sqrt{k}\,W),              \tag{3.2}
\]

deleting `o(W)` elements means a relative exceptional mass

\[
                         o(k^{-1/2}).                         \tag{3.3}
\]

This is a **unit-chain-scale** statement: one lost target on a positive
fraction of the `W` endpoint chains is already too expensive.

## 4. Quantitative comparison with the literature

Sudakov, Tomon and Wagner prove that `B_k` has a minimum chain
decomposition in which all but a

\[
                         k^{-1/8+o(1)}                         \tag{4.1}
\]

proportion of the chains have size

\[
 s\bigl(1+O(k^{-1/16})\bigr),
 \qquad s={2^k\over W}=\Theta(\sqrt k),                      \tag{4.2}
\]

and their good chains cover a
`1-k^(-1/8+o(1))` proportion of the lattice.  The proof first constructs
the corresponding upper-half chains and then reflects them, so this is the
relevant published comparison.

Equations (4.1)--(4.2) certify an exceptional element scale

\[
 2^k k^{-1/8+o(1)}
   =Wk^{3/8+o(1)},                                      \tag{4.3}
\]

and an additive good-chain length window

\[
 s\,O(k^{-1/16})=O(k^{7/16}).                         \tag{4.4}
\]

Both are `o` of their natural `Theta(sqrt(k))`-relative scales, but both
are much larger than one.  In particular, (4.3) is not `o(W)`, and trimming
the chains using only (4.4) does not improve it to that scale.

This is a scope statement, not a lower bound against possible future
improvements of their method.  It says only that the published theorem does
not imply (0.7).

**Reference.** B. Sudakov, I. Tomon, A. Z. Wagner, *Uniform chain
decompositions and applications*, Random Structures & Algorithms 60
(2022), 261--286, Theorem 1.2 and Corollary 1.3,
DOI `10.1002/rsa.21034`, arXiv `1911.09533`.

## 5. Sharpened target

The dense named-target programme has two successive integral gates, not one:

\[
\boxed{
\begin{array}{c}
\textbf{static unit-scale chain deletion:}
      \quad\gamma_d(k)=o(W)\ \text{(or the scalar-optimal }O(k)\text{)},\\[1mm]
\textbf{physical lift:}
      \quad\text{realize those chains by Ferrers holes satisfying}\
      \text{the sliding cocycle and simultaneous interval closure.}
\end{array}}
\tag{5.1}
\]

The first row is already beyond the currently published asymptotic
uniform-chain estimates.  The second is strictly stronger.  Therefore the
next positive theorem cannot be merely a generic rounding of rank marginals,
an ideal containment SDR, or a stationary age circulation.  It must exploit
Boolean-specific adjacent containment exchanges at unit-chain precision;
only after that does dense Ferrers path-flow rounding become the correct
physical question.
