# A fixed-dimensional chain-box route to constant one

## 1. Outcome

There is a direct way to separate the exponential Boolean-lattice scale from
the remaining local geometry.

Split the coordinates into a fixed number `t` of blocks and put an arbitrary
symmetric-chain decomposition on each block cube.  A tuple of chains, one
from every block, is a product of `t` chains.  These chain boxes partition
the Boolean lattice, and the sum of their individual widths is **exactly**

\[
                         W(k)={k\choose\lfloor k/2\rfloor}.
\]

Consequently, a surface-error construction for fixed-dimensional boxes would
prove the asymptotically sharp constant for the original problem.  In
particular, the following purely three-dimensional lemma is sufficient:

> Every product of three finite chains has a contiguous-union word covering
> all its points whose length is its width plus
> `O(1 + p + q + r)`, where `p,q,r` are the three chain heights.

If this lemma holds uniformly, then

\[
          \nu(k)\le W(k)+O\!\left({W(k)\over\sqrt{k}}\right).
\]

This is a reduction, not yet a proof of the three-dimensional lemma.  It is
mathematically different from the two-block Cartesian construction: two
dimensions have an exact linear obstruction, while three dimensions are the
first dimension in which a boundary-size error is compatible with global
constant one.

## 2. Chain boxes

Partition

\[
                   [k]=X_1\sqcup\cdots\sqcup X_t,
                   \qquad |X_i|=k_i,
\]

where `t` is fixed and the `k_i` differ by at most one.  On every
`2^(X_i)` choose an SCD `D_i`.

Write a chain `C in D_i` as

\[
 C_0\subset C_1\subset\cdots\subset C_{\ell(C)}.
\]

If its minimum rank is `a(C)`, symmetry and saturation give

\[
               \ell(C)=k_i-2a(C).                         \tag{2.1}
\]

For a tuple `bold C=(C^(1),...,C^(t))`, put

\[
 P_{\boldsymbol C}
   =\{C^{(1)}_{x_1}\cup\cdots\cup C^{(t)}_{x_t}:
                  0\le x_i\le\ell(C^{(i)})\}.             \tag{2.2}
\]

The coordinate blocks are disjoint, so (2.2) is a copy of the box

\[
            [0,\ell_1]\times\cdots\times[0,\ell_t]
\]

ordered coordinatewise.  The boxes `P_bold C` partition `2^[k]`.

The common minimum

\[
                    B_{\boldsymbol C}=\bigcup_i C^{(i)}_0
\]

causes no encoding difficulty.  A local word may be written in the disjoint
increment coordinates and `B_bold C` added to every emitted entry.  Every
nonempty interval union then acquires precisely the common minimum.

## 3. Exact width additivity

Let

\[
 w(\ell_1,\ldots,\ell_t)
   =[z^{\lfloor(\ell_1+\cdots+\ell_t)/2\rfloor}]
       \prod_{i=1}^t(1+z+\cdots+z^{\ell_i}).          \tag{3.1}
\]

The coefficient in (3.1) is the width of the product of chains.  Indeed the
rank polynomial is symmetric and unimodal.

Put `A=sum_i a(C^(i))`.  By (2.1),

\[
     \sum_i\ell_i=k-2A.
\]

Therefore the members of `P_bold C` in the global middle rank are exactly
the central-rank members of the box, and their number is (3.1).  Since the
boxes partition the Boolean lattice,

\[
 \boxed{
   \sum_{\boldsymbol C\in D_1\times\cdots\times D_t}
          w(\ell(C^{(1)}),\ldots,\ell(C^{(t)}))=W(k).}    \tag{3.2}
\]

This identity is exact and independent of which SCDs were chosen.

## 4. Aggregation theorem

For a chain box with heights `bold ell`, let `g_t(bold ell)` be the least
length of a word in its disjoint increment sets whose contiguous unions
contain every box point except the all-empty target when appropriate.

### Theorem 1 (surface-error aggregation)

Fix `t>=3`.  Suppose that for an absolute constant `K_t`, every `t`-box
satisfies

\[
 g_t(\ell_1,\ldots,\ell_t)
 \le w(\ell_1,\ldots,\ell_t)
      +K_t(1+\ell_1+\cdots+\ell_t)^{t-2}.             \tag{4.1}
\]

Then

\[
             \nu(k)\le W(k)+O_t(W(k)k^{-1/2}).        \tag{4.2}
\]

### Proof

Use the local word for every box and concatenate all of them.  Every Boolean
mask is represented inside its own box word, so crossings between box words
are irrelevant.  By (3.2), the sum of the main terms in (4.1) is exactly
`W(k)`.

It remains to sum the error terms.  For an SCD of an `s`-cube, the number of
chains of height at least `2d` is at most `binom(s,floor(s/2)-d)`.  The usual
central-binomial tail estimate therefore gives, for every fixed integer
`r>=0`,

\[
 {1\over W(s)}\sum_{C\in D_s}(1+\ell(C))^r=O_r(s^{r/2}). \tag{4.3}
\]

Using `(x_1+...+x_t)^(t-2)<=O_t(sum_i x_i^(t-2))` and factorizing the sums
over chain tuples, (4.3) bounds the total error in (4.1) by

\[
 O_t\!\left(prod_i W(k_i)\;k^{(t-2)/2}\right).       \tag{4.4}
\]

For a balanced fixed split, Stirling's formula gives

\[
 {\prod_i W(k_i)\over W(k)}=\Theta_t(k^{-(t-1)/2}).   \tag{4.5}
\]

Combining (4.4) and (4.5) gives `O_t(W(k)/sqrt(k))`, proving (4.2).
\(\square\)

For `t=3`, hypothesis (4.1) is simply

\[
             g_3(p,q,r)\le w(p,q,r)+O(p+q+r+1).       \tag{4.6}
\]

Thus one fixed three-dimensional theorem would settle the leading constant
for all Boolean dimensions.

## 5. Why two dimensions do not suffice

The analogous boundary-error claim is false for a rectangle.  Consider two
strict chains of heights `p,q` on disjoint coordinates.  To represent all
targets on the first coordinate axis, an entry of each of the `p` new chain
heights is forced which contains no increment from the second coordinate.
The second axis similarly forces `q` disjoint entries.  Hence

\[
                         g_2(p,q)\ge p+q.             \tag{5.1}
\]

The standard suffix--prefix gadget attains `p+q`, so this is exact.  For a
balanced square its width is only `p+1`; the excess is linear in the side
length, not a zero-dimensional boundary term.

The same obstruction appears in the orthogonal-chain formulation.  Any SCD
of the rectangle contains the saturated chain from its minimum to its
maximum, of length `p+q+1`.  A chain partition orthogonal to it must have at
least `p+q+1` chains, one for each intersection.  Thus a width-sized local
orthogonal pair is impossible.

This explains structurally why repeated refinements of the two-block
Cartesian construction do not reach constant one.  Dimension three is the
first local geometry for which the proposed surface term has the right
global order.

## 6. Exact remaining local problem

The next mathematical target is no longer an exponential Boolean-lattice
construction.  It is the following polynomial-size fixed-dimensional
problem.

### Three-chain interval-join conjecture

Let three disjoint increment chains have heights `p,q,r`.  There exists a
word of subsets of their increments, of length

\[
 [z^{\lfloor(p+q+r)/2\rfloor}]
      (1+\cdots+z^p)(1+\cdots+z^q)(1+\cdots+z^r)
      +O(p+q+r),                                      \tag{6.1}
\]

whose contiguous unions are every triple of chain prefixes.

The entries may mix increments from all three chains; forbidding mixed
entries would reintroduce the two-dimensional obstruction.  A proof should
probably be phrased as one of:

1. an explicit diagonal/lozenge traversal of the box;
2. two ordered orthogonal chain covers plus a Boolean join growth diagram;
3. a bounded-boundary recursion on one side length; or
4. a flow decomposition of the central hexagonal slice.

A counterexample showing an unavoidable `Omega(width)` excess for cubic
boxes would also be decisive: it would close this entire product route.

