# Pre-reserved bottom owner banks: exact quantifier and shifted bottleneck

**Date:** 2026-08-05  
**Method:** literal FIFO inversion and the exact owner-count ledger; no
computation or search  
**Status:** unconditional structural theorem and obstruction.  A correlated
bottom bank is potentially preferable to independent sampling, but a literal
taskwise reservation fixes the whole future queue and destroys the large-star
freedom used by the backward SDRs.  Reserving an unassigned bank avoids that
collapse, but two reserved role banks move the unique balanced Hall problem
from level zero to level two rather than eliminating it.  Reserving one role
bank preserves twofold slack at level two and is the maximal reservation that
does not create a new balanced upper level.

## 1. Literal bottom algebra

For one punctured FIFO copy, use the notation

\[
 S_0\in{[k]\choose r-d},\qquad
 b_1,\ldots,b_{d-1},\qquad
 x_1,\ldots,x_d,u,                                          \tag{1.1}
\]

where all event coordinates have the required freshness.  Its owners are

\[
 T_j=S_0\cup\{b_1,\ldots,b_j\}
              \cup\{x_{j+1},\ldots,x_d\}quad(0\le j<d),   \tag{1.2}
\]

and `T_d=R+u`, where `R` is the rank-`r-1` hull.  In particular,

\[
 \begin{aligned}
 T_0&=S_0\cup\{x_1,x_2,\ldots,x_d\},\\
 T_1&=S_0\cup\{b_1,x_2,\ldots,x_d\}.
 \end{aligned}                                             \tag{1.3}
\]

### Theorem 1.1 (a bottom pair fixes the queue set)

Fix `S_0` and `b_1`.  A legal ordered bottom-owner pair `(T_0,T_1)` uniquely
determines

\[
 x_1=T_0\setminus T_1,
 \qquad
 \{x_2,\ldots,x_d\}
       =(T_0\setminus S_0)\setminus\{x_1\}.                 \tag{1.4}
\]

Conversely, a `d`-set `X subseteq[k]setminus R` and a distinguished
`x_1 in X` determine the pair by

\[
 T_0=S_0\cup X,qquad
 T_1=S_0\cup\{b_1\}\cup(X\setminus\{x_1\}).                \tag{1.5}
\]

#### Proof

The two rank-`r` owners in (1.3) differ by the single exchange
`x_1 -> b_1`.  This gives the first identity in (1.4), and subtracting the
known core `S_0` gives the second.  Formula (1.5) is the reverse
construction. \(\square\)

Thus a taskwise pre-reservation of the two literal bottom owners is not just
a reservation of two capacity units: it selects the complete unordered
future queue bank.

## 2. The remaining upper freedom after literal reservation

Once `(T_0,T_1)` is fixed, the only internal queue choice is an ordering of

\[
                         X'=\{x_2,\ldots,x_d\}.              \tag{2.1}
\]

There are `(d-1)!` such orders, followed by at most `q-d` choices of the
terminal coordinate `u`.

At upper level `j`, `2<=j<d`, the set of possible owners before earlier
choices are fixed is

\[
 \left\{
 S_0\cup\{b_1,\ldots,b_j\}\cup Y:
 Y\in{X'\choose d-j}
 \right\}.                                                  \tag{2.2}
\]

Hence its size is only

\[
                         {d-1\choose d-j},                  \tag{2.3}
\]

and, conditional on `T_(j-1)`, there are only `d-j+1` possible next
deletions.  By contrast, in the unrestricted backward SDR the raw menu at
the corresponding level has size

\[
                         q-(d-j)=\Theta(d^2).               \tag{2.4}
\]

The reservation therefore replaces the large upper-star SDRs by a coupled
permutation-packing problem.  No theorem about an independently reserved
bottom matching can ignore this loss of freedom.

## 3. Unassigned bank reservation and the exact slack shift

Let `H` be the number of copies and

\[
                         W=(d+1)H+O(W/d)                    \tag{3.1}
\]

be the scalar owner ledger.  Suppose an owner bank `B` of size `hH` is
reserved before installing upper levels, but its vertices are not yet
assigned to individual copies.  Install levels `j+1,...,d`, where `j>=2`.
They occupy `(d-j)H` owners.  The available right shore for level `j`, after
protecting `B`, has size

\[
 \begin{aligned}
 W-hH-(d-j)H
 &=(j+1-h)H+O(W/d).
 \end{aligned}                                             \tag{3.2}
\]

### Theorem 3.1 (reservation shifts the Hall bottleneck)

The right-to-left scalar ratio at upper level `j` is

\[
                         j+1-h+O(1).                        \tag{3.3}
\]

Consequently:

* reserving both bottom roles (`h=2`) makes level `j=2` balanced;
* reserving one bottom role (`h=1`) leaves ratio two at level `j=2` and
  ratio `j` at level `j`; and
* `h=1` is the largest whole-layer reservation which leaves every upper
  level `j>=2` with strict scalar slack.

#### Proof

Equation (3.2) is the full owner bank minus the reserved vertices and the
already installed later levels.  Divide by the `H` left tasks. \(\square\)

Before reservation the unique balanced graph was the final `G_0`.  A
two-role reservation does not remove a balanced matching theorem; it moves
that theorem to `G_2`, while bottom feasibility remains correlated with the
terminal state of `G_2`.

## 4. Why a deletion coupling cannot be frozen taskwise in advance

Let

\[
                         \phi:\mathcal L_{r-1}\longrightarrow
                         \mathcal L_r                       \tag{4.1}
\]

be any containment perfect matching, so `K subset phi(K)` for every
rank-`r-1` skeleton `K`.  If a bottom skeleton bank `Q` is chosen and
`phi(Q)` is reserved, then the edges `K--phi(K)` give a perfect bottom-owner
matching with uniform marginals.  This is the ideal deletion coupling.

For the actual final level, however, the skeleton is

\[
 K_i=T_1^i-\{b_1^i\}
    =S_0^i\cup\{x_2^i,\ldots,x_d^i\}.                      \tag{4.2}
\]

Thus `K_i` contains the whole unordered future queue set.  It is not known
before the upper choices are made.  If `K_i` is fixed early in order to
reserve `phi(K_i)`, Theorem 1.1 fixes that queue set and invokes the
permutation-packing problem of Section 2.  If it is fixed late, the upper
SDRs may already have consumed `phi(K_i)`.

This is the exact dependency loop:

\[
 \boxed{
 \text{reserve }\phi(K_i)
 \Longleftrightarrow
 \text{know }K_i
 \Longleftrightarrow
 \text{fix the future queue set.}}
 \tag{4.3}
\]

Marginal uniformity of `Q` and `phi(Q)` does not break (4.3).

## 5. One-role reservation is the viable correlated interface

Theorem 3.1 identifies the maximal proof-safe interface:

1. reserve one owner bank `B_0` of size `H`;
2. install upper levels `j>=2` in its complement, retaining at least
   twofold scalar slack at the lowest upper level;
3. choose the bottom skeletons only after the upper state is known; and
4. correlate their assignment into `B_0` with the choice of the second
   bottom role in the final residual bank.

This still leaves a fixed-rank coupled matching at the bottom, but the
upper SDRs have not been converted into a balanced problem.  Any successful
correlated theorem should therefore target this one-role interface, not a
fully taskwise pre-reserved pair.

The exact remaining matching has options

\[
 K_i=L_i\cup\{x_2\},\qquad
 T_1^i=K_i\cup\{b_1^i\},\qquad
 T_0^i=K_i\cup\{x_1\}\in B_0,                              \tag{5.1}
\]

where

\[
                         L_i=T_2^i-\{b_2^i,b_1^i\}.         \tag{5.2}
\]

It must make the `K_i`, `T_1^i`, and `T_0^i` occurrence resources
simultaneously injective.  This is a three-resource fixed-rank matching,
but only one role bank is prescribed and all upper levels retain slack.

## 6. Avoidance cost at the slack levels

Under the same product-residual hypothesis used for the level-SDR theorem,
a raw upper star of size `q-O(d)=Theta(d^2)` sees, after one role-bank
reservation, expected level-`j` degree

\[
 {j\over d+1}(q-O(d))=\Theta(jd),\qquad j\ge2.              \tag{6.1}
\]

Thus the reservation changes the former scale `Theta((j+1)d)` only by one
unit of `Theta(d)`.  In particular the minimum upper scale remains
`Theta(2d)`, so every exponential low-degree/right-load tail of the form

\[
                         \exp(-c(j+1)d)                     \tag{6.2}
\]

survives, with constants changed, as

\[
                         \exp(-c'jd).                       \tag{6.3}
\]

Summed over all `j>=2`, this still costs `O(H e^{-2c'd})=o(H/d)` discarded
copies.  This is conditional only on the same product-residual/cylinder
tracking needed before reservation; the scalar reservation itself creates
no new asymptotic loss at the slack levels.

## 7. Final verdict

There is no unconditional theorem saying that an exact taskwise bottom
matching can simply be reserved before the upper SDRs.  Literal reservation
fixes the whole queue set.  Reserving both unassigned role banks merely
moves the balanced Hall gate upward.

The strongest honest correlated reduction is

\[
 \boxed{
 \begin{array}{c}
 \text{reserve one bottom role bank}\;B_0,\\
 \text{run all upper levels with strict slack},\\
 \text{solve the final three-resource matching (5.1) jointly}. 
 \end{array}}
 \tag{7.1}

Closing (5.1) with `O(H/d)` discarded copies would already fit the global
separator budget.  It is a weaker target than the independent two-bank
random-Sperner estimate `O(H/d^2)`, and it avoids introducing a new balanced
upper SDR.

