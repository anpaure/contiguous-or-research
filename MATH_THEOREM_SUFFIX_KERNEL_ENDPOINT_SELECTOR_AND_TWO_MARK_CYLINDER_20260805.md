# The fresh suffix kernel gives an endpoint-changing two-mark selector

**Date:** 2026-08-05  
**Method:** exact fresh-FIFO inversion, conditional product sampling, and
monotone thinning; no computation or search  
**Status:** unconditional at the suffix-first owner level.  A fixed complete
endpoint fibre has no second-mark freedom, but a fixed fresh owner suffix
`T_2,...,T_d` has exactly `r-d+1` possible first insertion marks.  Independent
occurrence-local selection from those apertures upgrades any bank-conditioned
one-mark cylinder to the required two-mark cylinder, with multiplicative loss
`1+O(d/r)=1+o(1)`.  Subsequent collision deletion cannot spoil the cylinder.
The remaining physical quantifier is explicit: the lower-chain factor must be
chosen after this role selection, or must admit these endpoint-fibre changes.
The theorem does not claim that a lower-first fixed block packing has that
property.

## 1. A fresh owner suffix does not determine `b_1`

Let `d>=2` and `r>=2d`.  Consider a fresh FIFO owner suffix

\[
                         T_2,T_3,\ldots,T_d                 \tag{1.1}
\]

of rank `r`, so that for `3<=j<=d`

\[
                         T_j=T_{j-1}-x_j+b_j,               \tag{1.2}
\]

where all displayed `x_j,b_j` are pairwise distinct, every `x_j` is present
before its deletion, and every `b_j` is fresh when inserted.  Put

\[
 P=\bigcap_{j=2}^dT_j
   =T_2-\{x_3,\ldots,x_d\}.                                 \tag{1.3}
\]

Then

\[
                         |P|=r-d+2.                          \tag{1.4}
\]

Fix a legal one-mark choice `b_2 in P`.

### Theorem 1.1 (suffix-kernel endpoint aperture)

For every

\[
                         z\in P-\{b_2\},                    \tag{1.5}
\]

there is a fresh endpoint fibre whose first two insertion labels are

\[
                         b_1=z,\qquad b_2,                  \tag{1.6}
\]

and whose owner suffix is exactly (1.1).  More precisely, choose any
partition

\[
 P-\{z,b_2\}=C\mathbin{\dot\cup}A,
 \qquad |C|=r-2d,\quad |A|=d,                               \tag{1.7}
\]

and put

\[
 B=(z,b_2,b_3,\ldots,b_d).                                  \tag{1.8}
\]

There are exactly

\[
                         \binom{r-d}{d}                      \tag{1.9}
\]

choices of the unordered pair `(C,A)`, independently of `z`.  After choosing
an order of `A`, and two fresh queue labels `x_1,x_2`, the synchronized FIFO
formula reconstructs a complete depth-`d` block with the required suffix.

#### Proof

Freshness in (1.2) implies that the deleted labels
`x_3,...,x_d` lie in `T_2` and disappear one at a time, while the inserted
labels `b_3,...,b_d` are absent from `T_2` and enter one at a time.  Hence
(1.3) holds and removes exactly `d-2` labels from `T_2`, proving (1.4).

Choose `z` and (1.7).  The four role sets

\[
 C,\quad A,\quad X=\{x_1,x_2,x_3,\ldots,x_d\},
 \quad B=\{z,b_2,b_3,\ldots,b_d\}                           \tag{1.10}
\]

are pairwise disjoint once `x_1,x_2` are chosen outside
`\(T_2\cup\{b_3,\ldots,b_d\}\)`.  The synchronized-chain owner formula gives

\[
 \begin{aligned}
 \widehat T_2
  &=C\cup A\cup\{x_3,\ldots,x_d\}\cup\{z,b_2\}\\
  &=P\cup\{x_3,\ldots,x_d\}=T_2.                            \tag{1.11}
 \end{aligned}
\]

For `j>=3`, it then gives

\[
 \widehat T_j
 =P\cup\{x_{j+1},\ldots,x_d\}
      \cup\{b_3,\ldots,b_j\}=T_j                           \tag{1.12}
\]

by induction from (1.2).  Thus every `z` in (1.5) changes the endpoint fibre
but fixes the complete already-installed suffix.  After removing `z,b_2`,
the persistent set has size `r-d`, so (1.9) is immediate.  An arbitrary
ordering of `A` is owner-invisible, and the standard synchronized FIFO
recurrence completes the block.  \(\square\)

This is not a fixed-fibre switch.  Changing `z` changes the role set `B` and
usually changes the lower path.  It therefore crosses exactly the invariant
identified by the fixed-fibre rigidity theorem.

## 2. Exact size of the bottom fresh aperture

For a fixed choice of `z`, the labels available for `x_1,x_2` are

\[
 Y=[k]-\bigl(T_2\cup\{b_3,\ldots,b_d\}\bigr),               \tag{2.1}
\]

and hence

\[
 |Y|=k-r-(d-2)=q-d+1,\qquad q=k-r+1.                        \tag{2.2}
\]

Put

\[
                         L=T_2-\{b_2,z\}.                    \tag{2.3}
\]

For `a,b in Y`, the two bottom owner formulas are

\[
 T_1=L\cup\{z,a\},\qquad T_0=L\cup\{a,b\}.                 \tag{2.4}
\]

Thus the endpoint-changing choice (1.5) produces exactly the same `K_y`
resource geometry used in the pre-reserved bottom theorem:

\[
 v_a=L\cup\{z,a\},\qquad e_{ab}=L\cup\{a,b\}.              \tag{2.5}
\]

In particular, changing the second mark does not shrink the `y=q-d+1`
bottom option aperture.

## 3. Occurrence-local selection upgrades the cylinder

Let `B_0,B_1` be any already exposed bank pair.  Let `mathcal H` denote the
complete history which determines the banks and all selected fresh owner
suffixes, but not their first insertion marks.  For a selected suffix `i`,
write

\[
 s_i=(T_2^i,b_2^i),\qquad
 P_i=\bigcap_{j=2}^dT_j^i,
 \qquad A_i=P_i-\{b_2^i\}.                                  \tag{3.1}
\]

By (1.4), every aperture has the common size

\[
                         a:=|A_i|=r-d+1.                     \tag{3.2}
\]

Conditional on `mathcal H`, choose the marks `Z_i` independently and
uniformly from `A_i`.  The randomness is keyed by the **owner occurrence**
`i`, not by the coordinate value; hence two suffixes with overlapping
apertures do not share a latent random mark.

Let `Y_s` indicate selection of the one-mark suffix state `s=(T,b_2)`, and
let

\[
 \widetilde X_{(T,b_2,z)}
   =Y_{(T,b_2)}1_{\{Z_{(T,b_2)}=z\}}.                        \tag{3.3}
\]

Assume the selected suffix law has the bank-conditioned one-mark cylinder

\[
 \mathbb E\left[\prod_{i=1}^mY_{s_i}\mid B_0,B_1\right]
 \le \eta^m                                                     \tag{3.4}
\]

for compatible distinct owner occurrences and all `m<=M`, where

\[
                         \eta\le(1+\epsilon_1){H\over Wr}.   \tag{3.5}
\]

### Theorem 3.1 (suffix selector gives the two-mark cylinder)

For every compatible collection
`alpha_i=(T_i,b_2^i,z_i)` with distinct owners and `m<=M`, one has

\[
 \mathbb E\left[\prod_{i=1}^m\widetilde X_{\alpha_i}
          \mid B_0,B_1\right]
 \le \left({\eta\over r-d+1}\right)^m.                     \tag{3.6}
\]

Consequently

\[
 \boxed{
 \mathbb E\left[\prod_{i=1}^m\widetilde X_{\alpha_i}
          \mid B_0,B_1\right]
 \le
 \left((1+\epsilon_2){H\over W(r)_2}\right)^m,}            \tag{3.7}
\]

where

\[
 1+\epsilon_2
  =(1+\epsilon_1){r-1\over r-d+1}
  =1+\epsilon_1+O(d/r).                                     \tag{3.8}
\]

Thus, in the central regime `d=o(r)`, any `epsilon_1=o(1)` gives exactly
the required `(C2)` with `epsilon_2=o(1)`, uniformly through every order for
which the one-mark cylinder is available (in particular `M=O(d)`).

#### Proof

Condition further on `mathcal H`.  If some prescribed `z_i` is outside
`A_i`, the conditional probability is zero.  Otherwise occurrence-local
independence gives exactly `a^{-m}`.  Therefore

\[
 \begin{aligned}
 \mathbb E\left[\prod_i\widetilde X_{\alpha_i}\mid B_0,B_1\right]
 &\le a^{-m}
   \mathbb E\left[\prod_iY_{s_i}\mid B_0,B_1\right]\\
 &\le(\eta/a)^m,
 \end{aligned}                                               \tag{3.9}
\]

which proves (3.6).  Using `(r)_2=r(r-1)` gives

\[
 {\eta\over r-d+1}
 \le (1+\epsilon_1){r-1\over r-d+1}{H\over W(r)_2},        \tag{3.10}
\]

and hence (3.7)--(3.8).  \(\square\)

No conditioning on the persistent kernels is needed in (3.4).  The proof
conditions on the complete suffix history only inside the mark-selection
step and then averages it away.

## 4. Alteration is cylinder-safe

The suffix-first construction may later reject some marked occurrences in
order to remove lower-path conflicts, owner collisions, or failed terminal
hull constraints.  Let `X_alpha` be the indicator that marked state `alpha`
survives any such rule.  The rule may depend arbitrarily on all marks and on
the banks, but suppose it never changes a mark; equivalently,

\[
                         0\le X_\alpha\le\widetilde X_\alpha. \tag{4.1}
\]

### Corollary 4.1 (monotone thinning preserves `(C2)`)

Every bound (3.6)--(3.7) remains true with `X` in place of `widetilde X`.

#### Proof

Pointwise,

\[
                         \prod_iX_{\alpha_i}
                      \le\prod_i\widetilde X_{\alpha_i}.     \tag{4.2}
\]

Take the conditional expectation and apply Theorem 3.1.  \(\square\)

This is useful for a separator-funded alteration: proving that only
`O(H/d)` suffixes are rejected is a packing problem, but it cannot recreate
the two-mark concentration problem.

## 5. Exact interface with the bottom `K_y` theorem

Theorems 1.1 and 3.1 reduce the pre-reserved two-mark spread row to a single
quantifier-compatible extension statement.

> **Suffix-first endpoint extension.**  Select the fresh owner suffixes
> `T_2,...,T_d` with their bank-conditioned one-mark cylinder; expose the
> occurrence-local choices `b_1 in P-{b_2}`; then choose or alter the lower
> fresh-chain factor so that all retained suffix-role pairs are realized,
> losing at most the separator-funded `O(H/d)` occurrences.

If this statement holds, Corollary 4.1 supplies `(C2)` for the retained
occurrences.  The one-task option tail and both size-biased resource-load
tails then follow from
`MATH_THEOREM_PRE_RESERVED_KY_OPTION_TAIL_AND_TWO_MARK_CYLINDER_GATE_20260805.md`,
and the separator-amplified Haxell theorem completes the bottom two levels.

The probabilistic part of the former open theorem is therefore no longer a
multi-owner correlation problem.  It is supplied by independent
occurrence-local aperture choices.  The remaining issue is an integral
**quantifier swap** between the lower fresh-chain factor and the already
selected suffix roles.

## 6. Why this does not contradict fixed-fibre rigidity

For a fixed endpoint fibre `(C,A,X,B)`, the pair `(T_2,b_2)` determines
`b_1`; this is the rigidity theorem.  In Theorem 1.1, changing `z` replaces
the endpoint set `B`, repartitions the persistent kernel into `C,A`, and in
general changes the lower chain.  The owner suffix remains fixed, but the
endpoint fibre does not.

Thus the two statements have disjoint quantifiers:

\[
 \begin{array}{c|c}
 \text{fixed endpoint fibre}&b_1\text{ is rigid},\\
 \text{fixed fresh owner suffix}&r-d+1\text{ endpoint fibres are available}.
 \end{array}                                                 \tag{6.1}
\]

Global coordinate symmetrization is unnecessary and would be too weak:
the random choices here are indexed by occurrences, so the diagonal
two-owner obstruction disappears exactly.

## 7. Proof-safe conclusion

The endpoint-changing stochastic kernel itself is explicit and has the
right strength:

\[
 \boxed{
 (T_2,\ldots,T_d;b_2)
 \longmapsto
 b_1\text{ uniform on }
 \left(\bigcap_{j=2}^dT_j\right)-\{b_2\}.}
                                                               \tag{7.1}
\]

Its aperture has size `r-d+1`, so its loss relative to the ideal `r-1`
choices is only `1+O(d/r)`.  It is bank-conditioned, jointly product through
all required orders, compatible with the exact bottom `K_y` geometry, and
stable under arbitrary later deletion.

What remains unproved is not `(C2)` **given a suffix-first construction**.
It is the suffix-first endpoint-extension statement in Section 5.  In a
lower-first construction, the first insertion mark is already fixed and the
kernel cannot be applied.  Any all-dimensional use must therefore either
reverse that quantifier or prove an endpoint-changing exchange in the lower
chain factor.
