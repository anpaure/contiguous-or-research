# Product boxes: a two-dimensional no-go and a three-dimensional constant-one reduction

## 1. Outcome

Split the coordinates into blocks and take an ordinary symmetric-chain
decomposition in each block.  Tuples of component chains partition the full
Boolean cube into rank-symmetric products of chains, called **boxes**.

This architecture has an exact width ledger:

\[
              \sum_{\text{boxes }P}\operatorname{width}(P)
                 =\binom{k}{\lfloor k/2\rfloor}=W(k).             \tag{1.1}
\]

It therefore gives a genuine constant-one reduction: if every box admits a
local contiguous-OR word of length its width plus a sufficiently small local
error, concatenating the local words covers the whole cube.

There is a sharp dimensional distinction.

* With two balanced coordinate blocks, refining the standard SCD in each
  two-dimensional grid into one side of an orthogonal pair requires a
  positive fraction of the grid width in extra chains.  Summed over the
  typical grids this is `Omega(W(k))`.  Thus the natural two-block local-SCD
  route merely recreates a constant-factor construction.
* With three balanced coordinate blocks, a typical box has height
  `Theta(sqrt(k))` but width `Theta(k)`.  The preceding obstruction vanishes.
  A uniform local theorem with additive error `O(height(P))` would sum to

  \[
                           W(k)+O(W(k)/\sqrt{k}),                  \tag{1.2}
  \]

  and hence prove `nu(k)=(1+o(1))W(k)`.

This does not prove the local three-box theorem.  It reduces the global
asymptotic problem to a fixed-dimensional, polynomial-sized family of join
posets, and proves that the most obvious two-dimensional version cannot work.

## 2. Exact box decomposition

Partition the coordinate set into fixed blocks

\[
                  [k]=X_1\sqcup\cdots\sqcup X_t,
                  \qquad |X_j|=k_j.                              \tag{2.1}
\]

Choose a saturated SCD `D_j` of the Boolean cube on `X_j`.  A chain
`C in D_j` has a minimum of rank `r(C)` and step length

\[
                         p(C)=k_j-2r(C).                          \tag{2.2}
\]

Thus its rank generating polynomial is

\[
                         x^{r(C)}(1+x+\cdots+x^{p(C)}).
\]

For a tuple `C=(C_1,...,C_t)`, the Cartesian product

\[
                         P_C=C_1\times\cdots\times C_t           \tag{2.3}
\]

is a box isomorphic to

\[
                         [0,p_1]\times\cdots\times[0,p_t],       \tag{2.4}
\]

ordered coordinatewise.  The boxes partition the Boolean cube.

Put `P=p_1+...+p_t`.  The box rank polynomial, after removing its absolute
minimum rank, is

\[
                         F_C(x)=\prod_{j=1}^t(1+x+\cdots+x^{p_j}).\tag{2.5}
\]

Products of chains are rank-symmetric, rank-unimodal, and admit SCDs.
Therefore their width is the central coefficient

\[
               w(C)=[x^{\lfloor P/2\rfloor}]F_C(x).              \tag{2.6}
\]

### Theorem 1 (exact width aggregation)

The box widths satisfy (1.1).

### Proof

For every coordinate block,

\[
 (1+x)^{k_j}=\sum_{C\in D_j}
       x^{r(C)}(1+x+\cdots+x^{p(C)}).                             \tag{2.7}
\]

Multiplying (2.7) over the blocks gives

\[
 (1+x)^k=\sum_{\mathbf C}
       x^{R(\mathbf C)}F_{\mathbf C}(x),
 \qquad R(\mathbf C)=\sum_jr(C_j)={k-P\over2}.                   \tag{2.8}
\]

The coefficient needed from this summand at global rank `floor(k/2)` is

\[
 \left\lfloor{k\over2}\right\rfloor-R(\mathbf C)
     =\left\lfloor{P\over2}\right\rfloor,                       \tag{2.9}
\]

because `P` and `k` have the same parity.  Taking the middle coefficient of
(2.8) and applying (2.6) proves (1.1).  \(\square\)

## 3. Exact OR aggregation

Embed a box in the original cube in the natural way.  Its coordinates are
the fixed minimum masks of its factor chains together with the ordered
singleton increments along those chains.  Join in the box is ordinary set
union.

### Theorem 2 (local words concatenate)

Suppose every nonempty box `P_C` has a word `A_C` whose contiguous unions
contain every nonempty mask in that box.  Then

\[
                 A=\mathop{\Vert}_{\mathbf C} A_C                \tag{3.1}
\]

is universal on the whole cube and

\[
                         |A|=\sum_C|A_C|.                         \tag{3.2}
\]

In particular, if

\[
                         |A_C|\leq w(C)+e(C),                     \tag{3.3}
\]

then

\[
                         \nu(k)\leq W(k)+\sum_Ce(C).              \tag{3.4}
\]

### Proof

The boxes partition all masks.  A witness internal to one concatenated block
remains contiguous after (3.1), so every local target is still represented.
Equation (3.2) is immediate and (3.4) follows from Theorem 1.  The unique box
containing the empty mask is interpreted in the punctured-cube convention;
this changes no nonzero target and at most a constant boundary term.
\(\square\)

No compatibility is required between different boxes.  All ordering and
pinning work is local.

## 4. Why the standard two-dimensional refinement cannot work

Consider the grid

\[
                              P=[0,p]\times[0,q],\qquad p\leq q.  \tag{4.1}
\]

Its width is

\[
                              w=p+1.                              \tag{4.2}
\]

The standard product SCD has chains `K_0,...,K_p` of lengths

\[
                              \ell_i=p+q-2i+1,
                              \qquad0\leq i\leq p.                \tag{4.3}
\]

Explicitly, `K_i` starts at `(0,i)`, runs horizontally to `(p-i,i)`,
then vertically to `(p-i,q)`.

Suppose this SCD is refined by splitting its chains into a chain partition
`L`.  Let `R` be any chain partition orthogonal to `L`.  If both partitions
have at most `w+c` chains, orthogonality forces every member of `L` to have
length at most `w+c`, since its elements must lie in distinct `R`-chains.

### Theorem 3 (two-grid splitting lower bound)

Under the preceding hypotheses,

\[
 c\geq
   \min\left\{p+1,\left\lceil{q-c\over2}\right\rceil_+\right\}. \tag{4.4}
\]

In particular, for the square grid `p=q=d`,

\[
                              c\geq\left\lceil{d\over3}\right\rceil,
                                                                        \tag{4.5}
\]

so both sides cannot have `w+o(w)` chains.

### Proof

Every original chain with `ell_i>w+c` must be split at least once.  Each
such split increases the number of `L`-chains by one, while `L` has at most
`w+c`; hence there can be at most `c` such original chains.  By (4.2)--(4.3),

\[
 \ell_i>w+c
 \quad\Longleftrightarrow\quad
 p+q-2i+1>p+1+c
 \quad\Longleftrightarrow\quad
 2i<q-c.                                                         \tag{4.6}
\]

The number of indices `0<=i<=p` satisfying (4.6) is the right side of
(4.4).  This proves (4.4).  For `p=q=d`, it gives

\[
                         c\geq\left\lceil{d-c\over2}\right\rceil,
\]

which is equivalent to `3c>=d`, proving (4.5).  \(\square\)

Thus even allowing arbitrary splitting and an arbitrary orthogonal second
partition, a constant number of repairs per growing square grid is
impossible.  The obstruction precedes the within-chain precedence and
pinning conditions.

## 5. The two-block loss aggregates to width order

For one block of dimension `h`, let `c_h(p)` be the number of chains of step
length `p` in an SCD.  It is independent of the chosen SCD and equals

\[
 c_h(p)=\binom h{(h-p)/2}-\binom h{(h-p)/2-1}
       ={2(p+1)\over h+p+2}\binom h{(h-p)/2}.                    \tag{5.1}

For any constants `0<a<b`, uniformly for

\[
                              a\sqrt h\leq p\leq b\sqrt h,       \tag{5.2}
\]

of the correct parity,

\[
                              c_h(p)=\Theta(W(h)/\sqrt h).        \tag{5.3}

There are `Theta(sqrt(h))` such values.

Now split `2h` coordinates into two `h`-blocks.  A positive fraction of the
exact width sum (1.1) comes from grids with both side lengths in (5.2): there
are `Theta(W(h)^2)` such grids, and each has width `Theta(sqrt h)`.  Since

\[
                              W(2h)=\Theta(W(h)^2\sqrt h),        \tag{5.4}


their total width is `Theta(W(2h))`.  Restrict further to `p/q` in a fixed
compact interval around one.  Theorem 3 then forces `Omega(sqrt h)` splits
per grid whenever both local chain counts are within `o(width)` of the grid
width.  Summing gives

\[
                              \Omega(W(2h))                        \tag{5.5}

extra chains.

Therefore the balanced two-block strategy

> ordinary half-cube SCDs -> two-dimensional chain grids -> refine one local
> SCD by `o(width)` splits -> orthogonal local endpoint chains

cannot prove `nu(k)=(1+o(1))W(k)`.  Its loss is of width order, consistent
with the known square-root-two scale of two-block chain-product methods.

## 6. Why three blocks are qualitatively different

For fixed `t`, split the coordinates into balanced blocks

\[
                              k_j=k/t+O(1).                        \tag{6.1}
\]

The number of boxes is

\[
 \prod_{j=1}^tW(k_j)
       =\Theta\left({W(k)\over k^{(t-1)/2}}\right).               \tag{6.2}

A typical factor-chain step length is `Theta(sqrt(k))`.  Hence a typical
`t`-box has height

\[
                              H(P)=1+\sum_jp_j=\Theta(\sqrt k),    \tag{6.3}


while its width is

\[
                              w(P)=\Theta(k^{(t-1)/2}).            \tag{6.4}

For `t=2`, height and width have the same order, exactly as in Theorem 3.
For every fixed `t>=3`,

\[
                              H(P)=o(w(P))                         \tag{6.5}

on typical boxes.  In particular, the longest-chain orthogonality bound
`number of opposite chains >= H(P)` is vacuous relative to width once
`t>=3`.

There is also an exact aggregate height ledger.  Let `B` be the number of
boxes.  Since

\[
        \sum_{C\in D_j}(p(C)+1)=2^{k_j},
\]

one has

\[
 \sum_{\mathbf C}\left(1+\sum_jp(C_j)\right)
  =B+\sum_j\bigl(2^{k_j}-W(k_j)\bigr)
                 \prod_{i\ne j}W(k_i).                           \tag{6.6}

For balanced fixed `t`, equations (6.2) and (6.6) give

\[
                         \sum_{\mathbf C}H(P_C)
                         =O\left({W(k)\over k^{(t-2)/2}}\right).  \tag{6.7}

In particular, for three blocks this is `O(W(k)/sqrt(k))`.

### Theorem 4 (three-box constant-one reduction)

Suppose there is a uniform construction which, for every rank-symmetric
three-chain box

\[
                         [0,p]\times[0,q]\times[0,r],             \tag{6.8}

embedded by disjoint singleton increments and an arbitrary fixed base mask,
produces a contiguous-OR word covering the box with length

\[
                         w(p,q,r)+O(p+q+r+1).                     \tag{6.9}

Then

\[
                         \boxed{\nu(k)=W(k)+O(W(k)/\sqrt k)}      \tag{6.10}

up to the already proved lower-order rank-slack term.  In particular,

\[
                         \nu(k)=(1+o(1))W(k).                     \tag{6.11}

### Proof

Use three balanced coordinate blocks and their SCD box partition.  Apply the
local construction to every box and concatenate, as in Theorem 2.  The width
terms sum to `W(k)` by Theorem 1, and the error terms sum to
`O(W(k)/sqrt(k))` by (6.7).  The lower bound `nu(k)>=W(k)` completes
(6.11).  \(\square\)

The same argument with `t>3` permits the aggregate error in (6.7), but the
three-block statement is already sufficient and is the smallest dimension
where the two-grid height obstruction disappears.

## 7. Exact remaining local theorem

The global constant-one problem has therefore been reduced to the following
fixed-dimensional statement.

> **Three-box OR lemma.**  A rank-symmetric product of three chains, with
> arbitrary disjoint singleton increment labels and an arbitrary fixed base
> mask, has a contiguous-union word of length its width plus
> `O(p+q+r+1)`.

An equivalent stronger route is to construct inside every three-box two
orthogonal chain covers with width plus `O(height)` chains, together with:

1. the two forced within-chain endpoint precedence orders;
2. triangular support with only `O(height)` padding; and
3. a coordinatewise pin-surviving Boolean join growth diagram.

This is no longer an exponentially large all-dimensional object.  For a
typical box it asks for a word of length `Theta(k)` on a poset of
`Theta(k^{3/2})` masks, with additive allowance `Theta(sqrt(k))`.  The local
parameters `p,q,r` remain arbitrary, so the theorem is still mathematical,
not a finite computation.

The two-dimensional no-go shows why the third factor is essential.  No
analogous height/orthogonality count currently rules out the three-box
lemma.
