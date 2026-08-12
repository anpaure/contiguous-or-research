# Subcritical product-chain aggregation

## 1. Statement

For `s>=0`, write

\[
                  W(s)=\binom{s}{\lfloor s/2\rfloor}.
\]

Let

\[
 Q(\boldsymbol\ell)=
 [0,\ell_1]\times\cdots\times[0,\ell_t]
\]

with coordinatewise join.  Let `g_t(bold ell)` be the minimum length of a
word of nonzero points of this box whose nonempty contiguous joins contain
every nonzero point of the box.  Put

\[
 w(\boldsymbol\ell)=
 [z^{\lfloor(\ell_1+\cdots+\ell_t)/2\rfloor}]
 \prod_{i=1}^t(1+z+\cdots+z^{\ell_i}).                 \tag{1.1}
\]

The zero-dimensional box is allowed: if all `ell_i=0`, then `g_t=0` and
`w=1`.

Allowing arbitrary subsets of the disjoint chain increments gives the same
`g_t`: close each entry to the least tuple of coordinate prefixes containing
it.  Every interval whose old join was a box point keeps exactly that join,
and zero entries may then be deleted.  Thus the range-maximum formulation
used here loses no local freedom.

### Theorem 1 (subcritical aggregation)

Fix an integer `t>=2`, a real `c>=0`, and a constant `K>=0`.  Suppose that,
**uniformly for every** `bold ell in Z_{>=0}^t`,

\[
 g_t(\boldsymbol\ell)
 \le w(\boldsymbol\ell)
      +K(1+\ell_1+\cdots+\ell_t)^c.                  \tag{1.2}
\]

Then the minimum nonzero universal-OR length satisfies

\[
 \nu(k)
 \le W(k)+O_{t,c,K}\!\left(
       W(k)(1+k)^{(c-t+1)/2}\right).                 \tag{1.3}
\]

Consequently, if

\[
                              c<t-1,                 \tag{1.4}
\]

then

\[
                         \nu(k)=(1+o(1))W(k).         \tag{1.5}
\]

The lower bound in (1.5) is the usual endpoint-chain/Sperner bound
`nu(k)>=W(k)`.

The theorem is a reduction.  It does not assert the local estimate (1.2).
For `t=3`, any uniform exponent `c<2` suffices.  For `t=4`, any uniform
exponent `c<3` suffices.

The word **uniform** is essential.  Even after the Boolean coordinates have
been split into equal blocks, the symmetric-chain heights occurring inside
one block are highly unequal.  A bound only for cubes
`ell_1=...=ell_t`, or only for positive side lengths, is not enough for this
aggregation theorem.

## 2. Boolean-lattice decomposition

Choose a balanced partition

\[
 [k]=X_1\sqcup\cdots\sqcup X_t,
 \qquad k_i=|X_i|,
 \qquad |k_i-k_j|\le1.                               \tag{2.1}
\]

Fix an arbitrary symmetric-chain decomposition `D_i` of `2^(X_i)`.  Write
one of its chains as

\[
 C_0\subset C_1\subset\cdots\subset C_{\ell(C)}.
\]

If the minimum has rank `a(C)`, symmetry and saturation give

\[
                       \ell(C)=k_i-2a(C).             \tag{2.2}
\]

For a tuple `bold C=(C^(1),...,C^(t))`, define

\[
 P_{\boldsymbol C}
 =\left\{C^{(1)}_{x_1}\cup\cdots\cup C^{(t)}_{x_t}:
          0\le x_i\le\ell(C^{(i)})\right\}.          \tag{2.3}
\]

The sets `P_bold C` partition `2^[k]`.  Each is a join-isomorphic copy of
`Q(bold ell)`, where `ell_i=ell(C^(i))`.

Let

\[
 A=\sum_i a(C^{(i)}),
 \qquad L=\sum_i\ell(C^{(i)})=k-2A.                 \tag{2.4}
\]

A point of local rank `q` has global rank `A+q`.  Since

\[
 \left\lfloor\frac L2\right\rfloor
 =\left\lfloor\frac k2\right\rfloor-A,             \tag{2.5}
\]

the global-middle elements in `P_bold C` are exactly its local-middle
elements.  A finite product of chains admits a symmetric-chain
decomposition (equivalently here, it has the Sperner property); hence its
width is its largest rank, the central coefficient `w(bold ell)`.  As the boxes
partition the Boolean lattice,

\[
 \boxed{
 \sum_{\boldsymbol C\in\mathcal D_1\times\cdots\times\mathcal D_t}
 w(\ell(C^{(1)}),\ldots,\ell(C^{(t)}))=W(k).}        \tag{2.6}
\]

This identity is exact and does not depend on which symmetric-chain
decompositions were chosen.

## 3. A uniform moment bound for SCD heights

The required estimate includes highly unbalanced, zero, and short chains.

### Lemma 2 (height moments)

Let `D_s` be any symmetric-chain decomposition of the `s`-cube, and let
`L(C)` be the edge-height of `C`.  For every fixed real `q>=0`,

\[
 \frac1{W(s)}\sum_{C\in\mathcal D_s}(1+L(C))^q
 \le C_q(1+s)^{q/2}                                 \tag{3.1}
\]

for all `s>=0`.  The constant is independent of the chosen SCD.

#### Proof

Put `m=floor(s/2)`.  For every integer `0<=d<=m`, a symmetric chain has
height at least `2d` exactly when it crosses rank `m-d`.  Each such chain
crosses that rank once, so

\[
 \#\{C:L(C)\ge2d\}=\binom{s}{m-d}.                  \tag{3.2}
\]

After choosing a chain uniformly from `D_s`, (3.2) gives

\[
 \Pr(L\ge2d)=\frac{\binom{s}{m-d}}{\binom{s}{m}}.   \tag{3.3}
\]

For `s>=2`, the quotient of binomial coefficients, written as a product of
successive ratios, satisfies

\[
 \frac{\binom{s}{m-d}}{\binom{s}{m}}
 \le \exp(-d^2/s).                                  \tag{3.4}
\]

For completeness, if `s=2m`, its factors are

\[
 \frac{m-j}{m+j+1}\quad(0\le j<d).
\]

Using `log(1-x)<=-x`, their logarithms sum to at most
`-d^2/(m+d)<=-d^2/s`.  If `s=2m+1`, the factors are
`(m-j)/(m+j+2)` and give the still stronger exponent
`-d(d+1)/s`.

Let `D=floor(L/2)`.  Then `1+L<=2(D+1)`, while (3.4) says
`Pr(D>=d)<=exp(-d^2/s)`.  Discrete summation by parts gives, for every real
`q>0`,

\[
 \begin{aligned}
 \mathbb E(D+1)^q
 &=1+\sum_{d\ge1}\big((d+1)^q-d^q\big)\Pr(D\ge d)\\
 &\le 1+C_q\sum_{d\ge1}(d+1)^{q-1}e^{-d^2/s}
 =O_q((1+s)^{q/2}).                                  \tag{3.5}
 \end{aligned}
\]

The cases `q=0` and `s=0,1` are immediate after enlarging the constant.
This proves (3.1).  Notice that the proof works directly for noninteger
moments.  Equivalently, one may prove the next integer moment and apply
Lyapunov's power-mean inequality.  \(\square\)

## 4. Summing the local errors

Let `C_i` be a uniformly selected chain from `D_i`, independently for the
different blocks, and put `L_i=ell(C_i)`.  The number of tuples is

\[
                         P=\prod_{i=1}^t W(k_i).      \tag{4.1}
\]

For nonnegative `x_i` and fixed real `c>=0`,

\[
 \left(\sum_{i=1}^t x_i\right)^c
 \le t^{\max(c-1,0)}\sum_{i=1}^t x_i^c.             \tag{4.2}
\]

Since `1+sum_i L_i <= sum_i(1+L_i)`, Lemma 2 yields

\[
 \begin{aligned}
 &\sum_{\boldsymbol C}
    (1+\ell(C^{(1)})+\cdots+\ell(C^{(t)}))^c\\
 &\qquad=P\,\mathbb E(1+L_1+\cdots+L_t)^c\\
 &\qquad\le C_{t,c}P\sum_{i=1}^t(1+k_i)^{c/2}
 \le C'_{t,c}P(1+k)^{c/2}.                          \tag{4.3}
\end{aligned}
\]

No balance assumption on the random chain heights was made.  In
particular, (4.3) includes every tuple having one or more height-zero
chains.

## 5. The balanced-width ratio

Uniform central-binomial estimates give constants `0<a<b<infinity` such
that

\[
 a\frac{2^s}{\sqrt{s+1}}
 \le W(s)\le
 b\frac{2^s}{\sqrt{s+1}}                             \tag{5.1}
\]

for every `s>=0`.  Hence, for any split,

\[
 \frac{\prod_iW(k_i)}{W(k)}
 =\Theta_t\!\left(
   \frac{\sqrt{k+1}}{\prod_i\sqrt{k_i+1}}
   \right),                                         \tag{5.2}
\]

where the powers of two cancel because `sum_i k_i=k`.  Under the balanced
split (2.1), every `k_i+1=Theta_t(k+1)`, and therefore

\[
 \boxed{
 \frac{\prod_iW(k_i)}{W(k)}
 =\Theta_t((1+k)^{-(t-1)/2}).}                       \tag{5.3}
\]

This remains valid, after changing only the `t`-dependent constants, for
the finitely many small `k` for which some `k_i` is zero.

Combining (4.3) and (5.3), the sum of all local error terms is

\[
 O_{t,c}\!\left(
 W(k)(1+k)^{(c-t+1)/2}\right).                       \tag{5.4}
\]

## 6. Zero targets and concatenation

There is one small bookkeeping point when `g_t` is defined only for the
nonzero local points.

For a box tuple `bold C`, let

\[
                    B_{\boldsymbol C}=\bigcup_iC^{(i)}_0. \tag{6.1}
\]

The map from a local vector `x` to the corresponding member of
`P_bold C` is a join homomorphism and sends local zero to `B_bold C`.

* If `B_bold C` is empty, use a nonzero local covering word.  Its images are
  nonzero, and the omitted local zero is exactly the globally omitted empty
  mask.
* If `B_bold C` is nonempty, prepend one local zero to the local word.  Its
  image is the nonzero target `B_bold C`; every other target keeps its old
  internal witness.

Thus at most one entry per product box is added.  As each summand in (4.3)
is at least one, this extra `P` is absorbed by replacing `K` with `K+1`.
After mapping, every emitted Boolean mask is nonzero.  Concatenating the
blocks cannot destroy any witness lying inside a block.

Equation (2.6) supplies the total main term, (5.4) supplies the total error,
and this one-entry bookkeeping is already absorbed in that error.  This
proves Theorem 1.

## 7. Exact scope of the exponent threshold

The ratio of the aggregated error bound to `W(k)` is

\[
                         O(k^{(c-t+1)/2}).            \tag{7.1}
\]

Therefore this **aggregation estimate** is `o(1)` exactly in the range
`c<t-1`.  At `c=t-1`, it gives only `O(W(k))`; it does not prove that a
more refined argument or a particular local family cannot still have
smaller total error.  Thus `t-1` is the threshold of this uniform
moment-bound reduction, not a lower bound on every possible construction.
