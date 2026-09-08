# Higher-dimensional escapes from the four-box bottleneck

## 1. Outcome

Let

\[
 Q_t(\boldsymbol\ell)=\prod_{i=1}^t[0,\ell_i],\qquad
 S=\ell_1+\cdots+\ell_t,
\]

and let `g_t(bold ell)` be the shortest nonzero word whose contiguous
coordinatewise maxima cover every nonzero point of the box.  Write
`w_t(bold ell)` for the width of the box.

There are two rigorous aggregation escapes beyond the present four-box
program.

1. For one fixed dimension `t`, a power saving is not necessary.  The
   critical-degree estimate

   \[
   g_t(\boldsymbol\ell)-w_t(\boldsymbol\ell)
      =o((1+S)^{t-1})                              \tag{1.1}
   \]

   uniformly over all side vectors already implies
   `nu(k)=W(k)+o(W(k))`, provided the error is globally
   `O((1+S)^(t-1))`.  In particular, the weakest clean five-box target is

   \[
   \boxed{g_5(\boldsymbol\ell)
      \le w_5(\boldsymbol\ell)+o((1+S)^4)}.         \tag{1.2}
   \]

   The concrete bound `w_5+O(S^3)` is stronger than needed and would give
   the quantitative global error `O(W(k)/sqrt(k))`.

2. It is enough to have a family of local estimates

   \[
   g_t(\boldsymbol\ell)
      \le(1+\varepsilon_t)w_t(\boldsymbol\ell)
        +K_t(1+S)^{t-2},                            \tag{1.3}
   \]

   for arbitrarily large fixed `t`, where `epsilon_t -> 0`.  One takes
   `k -> infinity` first for each fixed `t`, and only then `t -> infinity`.
   No uniform-in-`t` constants and no explicit choice `t=t(k)` are required.

None of the presently proved slicing, hook, independent-SCD connector, or
two-factor Cartesian constructions meets either criterion.  Their excess
on an equal box has the full critical degree `t-1`.  The Boolean
complement-bridge construction is not a theorem about arbitrary chain boxes;
even an ideal half-cost chain-box analogue would tend to ratio `sqrt(2)`, not
one.

The most concrete new target is a **shared-initialization suspension lemma**
which replaces the fatal volume term in the existing SCD connector by one
universal word for the lower-dimensional box.  Its exact Boolean aggregation
constant would be `sqrt(t/(t-1))`, hence it would prove constant one as
`t -> infinity`.  This target is stated and calculated in Section 7; it is
open.

## 2. Critical little-o aggregation

Put

\[
 E_t(\boldsymbol\ell)=g_t(\boldsymbol\ell)-w_t(\boldsymbol\ell)\ge0.
\]

The nonnegativity follows from the endpoint-chain/Sperner lower bound in
the box.  The following is a critical-exponent extension of
`SUBQUADRATIC_PRODUCT_AGGREGATION.md`.

### Theorem 1 (critical little-o theorem)

Fix `t>=2`.  Suppose there is a constant `K_t` such that, for every side
vector,

\[
 E_t(\boldsymbol\ell)\le K_t(1+S)^{t-1},            \tag{2.1}
\]

and suppose

\[
 \eta_t(R):=
 \sup_{S\ge R}{E_t(\boldsymbol\ell)\over(1+S)^{t-1}}
 \longrightarrow0\qquad(R\longrightarrow\infty).  \tag{2.2}
\]

Then

\[
                         \nu(k)=W(k)+o(W(k)).        \tag{2.3}
\]

#### Proof

Split the Boolean coordinates into `t` balanced blocks and put an arbitrary
SCD on every block, exactly as in the audited aggregation theorem.  If
`L_i` are the heights of a chain tuple, there are

\[
 P=\prod_iW(k_i)=O_t(W(k)k^{-(t-1)/2})              \tag{2.4}
\]

tuples, their local widths sum exactly to `W(k)`, and the height-moment
lemma gives

\[
 \sum_{\rm tuples}(1+L_1+\cdots+L_t)^{t-1}=O_t(W(k)). \tag{2.5}
\]

Fix `R`.  On tuples with `sum L_i>=R`, (2.2) and (2.5) bound the total
excess by `O_t(eta_t(R)W(k))`.  There are only finitely many integer side
vectors with `sum L_i<R`; by (2.1), the excess of any such tuple is bounded
by a constant depending on `R` and `t`.  Their total contribution is at
most

\[
 O_{R,t}(P)=o(W(k)).                                \tag{2.6}
\]

First let `k -> infinity` and then `R -> infinity`.  The local-zero repair
cost is at most one per tuple and is also absorbed by (2.6).  Thus the
concatenated word has length `W(k)+o(W(k))`.  The reverse inequality is
Sperner's bound.  \(\square\)

For `t=5`, (2.1)--(2.2) allow, for example,

\[
 E_5(\boldsymbol\ell)=O\left({(1+S)^4\over
                                  \log(2+S)}\right),              \tag{2.7}
\]

which is strictly weaker than any fixed polynomial power saving.

## 3. A vanishing-ratio family theorem

### Theorem 2 (fixed-`t` diagonal theorem)

Suppose that for an unbounded set of fixed integers `t` there are constants
`K_t` and numbers `epsilon_t -> 0` for which (1.3) holds uniformly for all
side vectors, including zero and unbalanced sides.  Then

\[
                         \nu(k)=(1+o(1))W(k).        \tag{3.1}
\]

#### Proof

For one fixed `t`, exact width aggregation and the height-moment estimate at
exponent `t-2` give

\[
 \nu(k)\le(1+\varepsilon_t)W(k)
       +O_t(K_tW(k)k^{-1/2}).                       \tag{3.2}
\]

Consequently

\[
 \limsup_{k\to\infty}{\nu(k)\over W(k)}
       \le1+\varepsilon_t                            \tag{3.3}
\]

for every one of those fixed dimensions.  Letting `t -> infinity` proves
an upper limit at most one, while the width lower bound gives the reverse
inequality.  \(\square\)

### Optional slowly-growing diagonal

The fixed-`t` diagonal above is logically cleaner, but a quantitative
growing choice is also possible.  Uniform Wallis bounds give, for balanced
block sizes and `t<=k/2`,

\[
 {\prod_iW(k_i)\over W(k)}
 \le C^t t^{t/2}k^{-(t-1)/2}.                       \tag{3.4}
\]

The exact SCD height tail is sub-Gaussian.  Independence and the standard
sub-Gaussian moment inequality imply, for `q=t-2`,

\[
 \left\|1+\sum_iL_i\right\|_q
       \le C\sqrt{kt}.                              \tag{3.5}
\]

Thus the additive term in (1.3), divided by `W(k)`, is at most

\[
 {K_t(Ct)^t\over\sqrt{k}}.                          \tag{3.6}
\]

Hence a growing choice works whenever

\[
 \varepsilon_t\to0,
 \qquad K_t(Ct)^t=o(\sqrt{k}).                      \tag{3.7}
\]

For example, if `K_t=exp(O(t log t))`, then
`t=o(log k/log log k)` is sufficient.  This calculation is conditional on
a local theorem uniform in the growing dimension; Theorem 2 requires no
such uniformity.

## 4. Equal-box width constant

For fixed `t` and `m -> infinity`, inclusion--exclusion gives

\[
 w_t(m,\ldots,m)=\kappa_t m^{t-1}+O_t(m^{t-2}),     \tag{4.1}
\]

where

\[
 \kappa_t={1\over(t-1)!}
 \sum_{j=0}^{\lfloor t/2\rfloor}
 (-1)^j\binom tj(t/2-j)^{t-1}.                     \tag{4.2}
\]

This is the density at the mean of the sum of `t` independent uniform
`[0,1]` variables.  The local central limit/Edgeworth expansion is

\[
 \kappa_t=\sqrt{6\over\pi t}
       \left(1-{3\over20t}+O(t^{-2})\right).        \tag{4.3}
\]

In particular

\[
 \kappa_3={3\over4},\quad
 \kappa_4={2\over3},\quad
 \kappa_5={115\over192}.                           \tag{4.4}
\]

These constants make the architectural losses below explicit.

## 5. Exact failure constants of the known constructions

### 5.1 Iterated slicing and hooks

Sort the sides as `ell_1<=...<=ell_t`.  Slice the first `t-3` coordinates
and use the audited three-box hook word on the final three.  Exact zero
bookkeeping gives

\[
 g_t(\boldsymbol\ell)
 \le\left(\prod_{i=1}^{t-2}(\ell_i+1)\right)
       (\ell_{t-1}+\ell_t+1)-1.                    \tag{5.1}
\]

On the equal box this is

\[
 2m^{t-1}+O_t(m^{t-2}),                             \tag{5.2}
\]

so its ratio to width is

\[
 {2\over\kappa_t}
   \sim\sqrt{2\pi t\over3}.                        \tag{5.3}
\]

The excess has degree `t-1`, and the ratio diverges.

### 5.2 The independent-SCD connector

Apply the proved connector to a `(t-1)`-box `P` and the final chain of
height `m`.  Its exact length is

\[
 |P|+m\,w(P)-1.                                    \tag{5.4}
\]

For equal sides its leading coefficient is `1+kappa_(t-1)`, and hence the
ratio is

\[
 {1+\kappa_{t-1}\over\kappa_t}
       \sim\sqrt{\pi t\over6}.                      \tag{5.5}
\]

The fatal term is the initialization volume `|P|`, not the sweep term
`m w(P)`.

For `t=5`, (5.5) is exactly

\[
 {1+2/3\over115/192}={64\over23}=2.782608\ldots.   \tag{5.6}
\]

### 5.3 A two-factor Cartesian SCD split

Split the `t` coordinates into groups of sizes `a` and `b=t-a`.  Decompose
each group box into symmetric chains and use the shortest chain-rectangle
word on every pair.  If `V_a,V_b` and `w_a,w_b` denote the two volumes and
widths, this gives the exact upper bound

\[
 w_bV_a+w_aV_b-w_aw_b-1.                           \tag{5.7}
\]

For equal sides its leading ratio is

\[
 {\kappa_a+\kappa_b\over\kappa_t}.                 \tag{5.8}
\]

The best split is asymptotically balanced, for which

\[
 {2\kappa_{t/2}\over\kappa_t}\longrightarrow2\sqrt2. \tag{5.9}
\]

At `t=5`, the best split is `1+4`, again giving `64/23`.

### 5.4 Complement bridge

The proved complement-bridge Euler construction is a Boolean-cube
construction.  It has not been proved as a uniform construction for
arbitrary chain boxes, so it cannot be inserted into the product-chain
aggregation theorem.

Even granting an ideal chain-box analogue which halves the leading term in
(5.7), the best possible ratio within that calculation would be

\[
 {\kappa_a+\kappa_b\over2\kappa_t}
       \longrightarrow\sqrt2                       \tag{5.10}
\]

at a balanced split.  It therefore would not supply the
`1+O(1/t)` hypothesis of Theorem 2.  For `t=5`, the idealized best ratio is
`32/23=1.391304...`, still a fixed critical loss.

Thus none of these four architectures beats the aggregation threshold in
any fixed dimension `t>=5`.

## 6. The direct five-box target

The least conceptual change from the current program is:

> **Five-box critical-little-o theorem.** Uniformly for all
> `bold ell in Z_{>=0}^5`, including zero and arbitrarily unbalanced sides,
> \[
> g_5(\boldsymbol\ell)
> \le w_5(\boldsymbol\ell)+o((1+\sum_i\ell_i)^4),
> \]
> with a global `O((1+sum ell_i)^4)` majorant.

By Theorem 1 this alone proves `nu(k)=W(k)+o(W(k))`.  A proof with
`O(S^3)` error gives the stronger global rate `O(W/sqrt(k))`.

One useful formulation is a **five-box suspension theorem**: fuse all
levels of one coordinate against a four-box central growth diagram so that
the total seam/factor cost is `O(S^3)`.  This may use the fifth coordinate
as the pin/clock reservoir and therefore does not logically require a
near-width four-box word first.  Merely concatenating four-box slices or
applying the independent-SCD connector cannot work, by Section 5.

This theorem is open.

## 7. A more powerful shared-initialization target

The existing SCD connector for a ranked box `P` and a chain `[0,h]` costs

\[
                         |P|+h\,w(P)-1.             \tag{7.1}
\]

It initializes every symmetric chain of `P` separately.  The calculation
in Section 5.2 shows that `|P|` is exactly the term preventing a
higher-dimensional escape.

The concrete replacement is:

> **Shared-initialization suspension lemma.** For every fixed `d`, every
> `d`-chain box `P`, and every `h>=0`, there is a portal-compatible word for
> `P x [0,h]` of length
> \[
> g_d(P)+h\,w(P)+O_d((1+h+\operatorname{rank}P)^{d-1}). \tag{7.2}
> \]
> The word uses one universal initialization of `P`; each new height level
> then costs one portal per chain of a minimum SCD, with all target witnesses
> remaining uncontaminated.

The exponent `d-1` in (7.2) is one below the critical exponent of the
`(d+1)`-box.  The statement is exact for `d=1`, where it is just
`g_2(p,h)=p+h`.

### Theorem 3 (consequence of shared initialization)

If (7.2) holds for arbitrarily large fixed `d`, then

\[
                         \nu(k)=(1+o(1))W(k).        \tag{7.3}
\]

#### Proof

Take `t=d+1` balanced Boolean blocks, initially of equal size `s`; bounded
rounding changes nothing.  Sum (7.2) over all tuples of SCD chains.  The
height-sweep term factors exactly as

\[
 \begin{aligned}
 &\left(\sum_{C_t}\ell(C_t)\right)
   \left(\sum_{C_1,\ldots,C_{t-1}}
      w_{t-1}(\ell(C_1),\ldots,\ell(C_{t-1}))\right)\\
 &\qquad=(2^s-W(s))W((t-1)s).                       \tag{7.4}
 \end{aligned}
\]

Here `sum_C ell(C)=2^s-W(s)`, while exact product-box width aggregation on
the first `t-1` blocks gives the second factor.

The initialization terms contribute

\[
 W(s)\sum_{C_1,\ldots,C_{t-1}}g_{t-1}(\boldsymbol\ell). \tag{7.5}
\]

The proved slice--hook bound is critical-polynomial in fixed dimension, so
the sum in (7.5) is `O_t(W((t-1)s))`.  Since

\[
 {W(s)W((t-1)s)\over W(ts)}=O_t(s^{-1/2}),          \tag{7.6}
\]

(7.5) is `o(W(ts))`.  The last term of (7.2) aggregates to
`O_t(W(ts)/sqrt{s})` by the subcritical aggregation theorem.

Finally Stirling's formula gives

\[
 { (2^s-W(s))W((t-1)s)\over W(ts)}
       =\sqrt{t\over t-1}+o_s(1).                  \tag{7.7}
\]

Therefore, for every fixed such `t`,

\[
 \limsup_{k\to\infty}{\nu(k)\over W(k)}
       \le\sqrt{t\over t-1}.                       \tag{7.8}
\]

Letting `t -> infinity` proves (7.3).  \(\square\)

On an equal local `t`-box, the principal coefficient in (7.2) would be
`kappa_(t-1)`, so

\[
 {\kappa_{t-1}\over\kappa_t}
  =1+{1\over2t}+O(t^{-2}).                          \tag{7.9}
\]

This is precisely the vanishing multiplicative loss sought in Theorem 2.
It also identifies the required combinatorial operation: share the lower
word across distinct SCD chains.  Improving the within-chain connector alone
cannot remove the volume term.

## 8. Final ledger

Proved here:

* uniform critical little-o error in any one fixed dimension suffices;
* a fixed-`t` family with local ratio `1+epsilon_t`, `epsilon_t -> 0`, and
  degree-`t-2` error suffices;
* the optional condition for a slowly growing `t(k)`;
* the exact equal-box leading constants of slicing/hooks, the independent
  SCD connector, and Cartesian chain rectangles; and
* the exact global consequence `sqrt(t/(t-1))` of shared initialization.

Still open:

* the five-box critical-little-o theorem; and
* the shared-initialization suspension lemma.

The higher-dimensional escape is therefore real but sharply localized.  It
does not come from iterating the existing gadgets.  It requires either a
near-width five-box growth diagram or a connector that initializes all
lower-dimensional SCD chains with one shared universal word.
