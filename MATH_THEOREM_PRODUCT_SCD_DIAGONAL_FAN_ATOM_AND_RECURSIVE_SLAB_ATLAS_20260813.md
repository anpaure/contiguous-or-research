# Product-SCD diagonal fans: a multi-seam atom and recursive slab atlas

**Date:** 2026-08-13  
**Method:** literal interval-union algebra and a finite exact product-grid
recurrence.  The orientation table was evaluated on `h100`; it is not an
asymptotic proof.  
**Status:** unconditional standalone deep-atlas theorem and a strict
improvement over rectangle-only charts.  The displayed recursive family
comes within a small coefficient gap of one but does not prove a uniform
`W+O(d)` bound.  It also does not compile the atlas into a rank-middle
owner chronology.

## 1. Product-chain notation

Let `X dotcup Y` be a disjoint coordinate split.  Take saturated Boolean
chains

\[
 C_0\subset C_1\subset\cdots\subset C_{p-1}\subseteq X,
 \qquad
 D_0\subset D_1\subset\cdots\subset D_{q-1}\subseteq Y. \tag{1.1}
\]

For a base cell `(i_0,j_0)` and positive integers `A,B`, put

\[
 K=C_{i_0}\cup D_{j_0},
 \qquad
 X_i=C_{i_0+i}\cup D_{j_0}\quad(1\leq i<A),              \tag{1.2}
\]

\[
 Y_j=C_{i_0}\cup D_{j_0+j}\quad(1\leq j<B).              \tag{1.3}
\]

Except in the unique rank-zero base case normalized in Section 4, every
displayed letter that is physically retained is a legal nonempty source
letter.  This is the key relaxation beyond the singleton-increment
rectangle atom.

The interval-union identities below hold even if `K` is empty.  To read
Theorem 2.1 as a standalone literal source word, assume `K` is nonempty;
Section 4 removes the only empty-core atom arising in the global atlas.

## 2. The exact diagonal-fan atom

For an integer `s>=0`, define the truncated downset

\[
 H(A,B;s)=\{(i,j):0\leq i<A,\ 0\leq j<B,\ i+j\leq s\}.  \tag{2.1}
\]

### Theorem 2.1 (diagonal fan)

The word

\[
 K, X_{A-1},X_{A-2},\ldots,X_1,
 Y_1,Y_2,\ldots,Y_{B-1}                                  \tag{2.2}
\]

has physical length

\[
                         A+B-1.                            \tag{2.3}
\]

For every `(i,j) in H(A,B;s)`, it has a distinct interval of value

\[
                         C_{i_0+i}\cup D_{j_0+j}           \tag{2.4}
\]

and width

\[
 w(i,j)=
 \begin{cases}
  1,&ij=0,\\
  i+j,&i,j>0.
 \end{cases}                                              \tag{2.5}
\]

Consequently, if

\[
                         \min\{s,A+B-2\}\leq d,           \tag{2.6}
\]

the entire truncated product downset is realized by legal source intervals
of width at most `d`.

#### Proof

The base cell uses the singleton interval `K`.  If `i>0,j=0`, use the
singleton interval `X_i`; if `i=0,j>0`, use the singleton `Y_j`.
For `i,j>0`, take the interval from `X_i` through `X_1,Y_1,...,Y_j`.
The `X` letters in that interval are nested and their union is `X_i`; the
`Y` letters are nested and have union `Y_j`.  Because the coordinate
halves are disjoint,

\[
                         X_i\cup Y_j
                         =C_{i_0+i}\cup D_{j_0+j}.        \tag{2.7}
\]

There are `i` `X` letters and `j` `Y` letters in the interval, giving the
second branch of (2.5); the base and both axes use singleton intervals.
Its endpoints recover `(i,j)`, so the marked interval occurrences are
distinct.  Equation (2.6), together with `d>=1`, is precisely the deadline
condition.
\(\square\)

The fan can therefore have physical length `d+1` even when it realizes a
full product rectangle at deadline `d`, and a truncated fan can be much
longer than `d` when its two arms do not attain their maxima
simultaneously.  Rectangle semiperimeter is no longer the physical-cost
constraint.

## 3. One product grid is a diagonal band

Use the product-SCD setup of
`MATH_THEOREM_PRODUCT_SCD_RECTANGLE_ATLAS_AND_COEFFICIENT_ONE_GATE_20260813.md`.
For a half-chain type pair `(u,v)`, let

\[
 a=\lambda_h(u),\qquad b=\lambda_{k-h}(v),                \tag{3.1}
\]

and put

\[
 \ell=d+1-u-v,
 \qquad
 s=r-d-1-u-v.                                             \tag{3.2}
\]

The active deep cells in its product grid are

\[
 G(a,b;\ell,s)=
 \{(i,j):0\leq i<a,\ 0\leq j<b,\ \ell\leq i+j\leq s\}. \tag{3.3}
\]

Covering the larger downset

\[
                         \{(i,j):i+j\leq s\}              \tag{3.4}
\]

is allowed: extra shallow target values in a universal word are harmless.
This removes the lower diagonal boundary from the construction.

## 4. The recursive slab cover

Fix a row-slab height

\[
                         1\leq A\leq d+1,                  \tag{4.1}
\]

and put

\[
                         B=d+2-A.                          \tag{4.2}
\]

Thus an `A` by `B` rectangle has exact atom cost and maximum interval width

\[
                         A+B-2=d,                          \tag{4.3}
\]

while its physical cost is `A+B-1=d+1`.

Process row-slab origins

\[
                         x=0,A,2A,\ldots<a.                \tag{4.4}
\]

At origin `x`, let

\[
                         a_x=\min\{A,a-x\}.                \tag{4.5}
\]

Starting at column `y=0`, place full `a_x` by `B` rectangles while

\[
 y+B\leq b,
 \qquad
                         x+y+a_x+B-2\leq s.               \tag{4.6}
\]

Each costs `a_x+B-1` and is realized by the rectangle atom.

When (4.6) first fails, put

\[
                         z=s-x-y.                           \tag{4.7}
\]

If `z>=0`, use one diagonal fan rooted at `(x,y)` with effective dimensions

\[
 A_x'=\min\{a_x,z+1\},
 \qquad
 B_x'=\min\{b-y,z+1\}.                                   \tag{4.8}
\]

It costs

\[
                         A_x'+B_x'-1.                      \tag{4.9}
\]

and covers every remaining active cell in this slab.

There is one useful recursive stop.  If no full rectangle was placed in
the slab and

\[
 \min\{s-x,(a-x-1)+(b-1)\}\leq d,                        \tag{4.10}
\]

then a single fan rooted at `(x,0)`, with dimensions

\[
 \min\{a-x,s-x+1\}\quad\hbox{by}\quad
 \min\{b,s-x+1\},                                        \tag{4.11}
\]

covers the entire residual downset, including every later slab.  Stop the
recursion.

### Theorem 4.1 (slab-fan grid cover)

The procedure in (4.1)--(4.11) gives a literal source atlas for every cell
of `G(a,b;ell,s)`.  All marked intervals have width at most `d`.  Different
atoms occupy disjoint physical word positions.

#### Proof

Every full rectangle lies below the diagonal by (4.6).  The rectangles are
column-disjoint inside a slab.  After the last one, the remaining cells in
that slab have local coordinates satisfying `i+j<=z`, and the effective
fan in (4.8) covers exactly that truncated tail by Theorem 2.1.  Distinct
slabs are row-disjoint.

In the stopping case, (4.10) says that the maximum possible local sum in
the whole residual grid is at most `d`; Theorem 2.1 therefore covers all
of it in one fan.  Extra cells below rank `ell` cause no conflict.  Finally,
concatenate the atom words and mark only the assigned active cells.

There is one literal nonemptiness normalization.  A core letter can be
empty only at global base rank zero.  Every value supplied by a
deadline-`d` rectangle or fan rooted there has global rank at most `d`,
whereas every assigned deep target has rank at least `d+1`.  Consequently
no such atom contains an assigned target; omit it.  This can only decrease
the physical length charged by the recurrence.  If exact charged length
rather than an upper bound is desired, pad the final concatenation with
arbitrary nonempty letters.
\(\square\)

## 5. Exact recurrence and weighted global sum

For implementation and independent auditing, define `Phi` recursively.
Let

\[
 \Phi(a,b,s,d;A)=0\quad\hbox{if }a\leq0\hbox{ or }b\leq0
 \hbox{ or }s<0.                                          \tag{5.1}
\]

Otherwise put `a_0=min(A,a)`, `B=d+2-A`, and

\[
 q=\max\{q'\geq0:q'B\leq b,
 \ a_0+B-2+(q'-1)B\leq s\},                              \tag{5.2}
\]

where the second inequality is omitted at `q'=0`.  Let

\[
                         y=qB,
 \qquad                  z=s-y.                           \tag{5.3}
\]

The current-slab cost is

\[
 q(a_0+B-1)+
 \begin{cases}
  \min\{a_0,z+1\}+\min\{b-y,z+1\}-1,&z\geq0, y<b,\\
  0,&\text{otherwise}.
 \end{cases}                                              \tag{5.4}
\]

If `q=0` and

\[
                         \min\{s,(a-1)+(b-1)\}\leq d,    \tag{5.5}
\]

replace (5.4) and all later costs by the single stopping-fan cost

\[
                         \min\{a,s+1\}+\min\{b,s+1\}-1.  \tag{5.6}
\]

Otherwise add

\[
                         \Phi(a-a_0,b,s-a_0,d;A).          \tag{5.7}
\]

Define the orientation-optimized grid cost

\[
 \phi_d(a,b;s)=
 \min_{1\leq A\leq d+1}
 \{\Phi(a,b,s,d;A),\Phi(b,a,s,d;A)\}.                    \tag{5.8}
\]

Finally put

\[
 R^{\rm SF}_{k,d}=
 \sum_{u=0}^{\lfloor h/2\rfloor}
 \sum_{v=0}^{\lfloor(k-h)/2\rfloor}
 c_h(u)c_{k-h}(v)
 \phi_d\bigl(\lambda_h(u),\lambda_{k-h}(v);
              r-d-1-u-v\bigr).                           \tag{5.9}
\]

### Corollary 5.1

There is a standalone nonempty-letter depth-`d` source word of physical
length at most `R^SF_(k,d)` realizing every deep target on a distinct
marked interval.  It may be padded to physical length exactly
`R^SF_(k,d)`.

This is the precise finite quantity whose coefficient-one inequality
remains to be proved or refuted.

## 6. Remote exact-integer orientation

The recurrence (5.1)--(5.9) gives:

\[
\begin{array}{c|c|c}
k&d&R^{\rm SF}_{k,d}/W\\ \hline
201&9&0.8660069\\
301&11&0.9083389\\
361&12&0.9310649\\
401&13&0.8807844\\
421&13&0.9372249\\
481&14&0.9308045\\
561&15&0.9603361\\
641&16&0.9727519
\end{array}                                               \tag{6.1}
\]

The table is not an eventual upper bound.  It shows two rigorous design
facts:

1. diagonal fans remove most of the rectangle-only overhead; and
2. every corrected audited value in (6.1) is below coefficient one, with
   a still-unproved all-parameter margin.

The next exact source-cost target is therefore an analytic proof that
(5.9) is at most `W+O(d)` for every sufficiently large parameter, or a
shared-boundary/variable-slab improvement which gives a uniform margin.
Any such source saving must still be compiled jointly with the
rank-middle owner chronology; a standalone atlas is not yet a PBBS factor.
