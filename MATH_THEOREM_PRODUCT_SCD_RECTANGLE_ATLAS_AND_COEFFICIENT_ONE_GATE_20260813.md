# Product-SCD semiperimeter rectangles: an exact deep atlas and the coefficient-one gate

**Date:** 2026-08-13  
**Method:** literal interval-union algebra, symmetric-chain counting, and an
exact finite dynamic programme.  The numerical table was evaluated on the
remote `h100` host; it is orientation, not an all-parameter proof.  
**Status:** unconditional standalone lower-payload atlas and exact reduction.
This note does **not** claim that the atlas is already an antecedent of a
simple rank-middle owner factor.  The remaining step is a joint chronology
compiler, not a marginal packing assertion.

## 1. Parameters and the physical budget

Put

\[
 r=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let `d=d(k)` be least with

\[
                    dW+{d+1\choose2}\geq\Lambda .       \tag{1.1}
\]

The final coefficient-one source budget is `W+d` **physical letters**.  The
quantity `dW` counts possible short interval addresses; it is not a physical
length budget.  In the PBBS notation put

\[
             t=r-d,
 \qquad
             \mathcal L_{\rm deep}
             =\{S:d<|S|<t\},
 \qquad
             L_{\rm deep}=|\mathcal L_{\rm deep}|.
                                                               \tag{1.2}
\]

Thus

\[
             L_{\rm deep}
             =\sum_{s=d+1}^{r-d-1}{k\choose s}.          \tag{1.3}
\]

The point of the construction below is that one source word of length
`A+B-1` carries all `AB` joins in an `A` by `B` product rectangle.  This is a
literal nonlinear compression of the deep lower deck.

## 2. The exact rectangle atom

Let the coordinate set be a disjoint union \(X\mathbin{\dot\cup}Y\).  Take two saturated
Boolean chains

\[
 C_0\subset C_1\subset\cdots\subset C_{a-1}\subseteq X,
 \qquad
 D_0\subset D_1\subset\cdots\subset D_{b-1}\subseteq Y . \tag{2.1}
\]

Write

\[
 x_i=C_i\setminus C_{i-1}\quad(i\geq1),
 \qquad
 y_j=D_j\setminus D_{j-1}\quad(j\geq1);                 \tag{2.2}
\]

these are singleton source letters.  Fix consecutive index intervals

\[
 I=[i_0,i_1],\qquad J=[j_0,j_1],
 \qquad A=|I|,\quad B=|J|,                               \tag{2.3}
\]

and put \(K=C_{i_0}\cup D_{j_0}\).

### Theorem 2.1 (product-chain rectangle atom)

Assume `K` is nonempty.  The word

\[
 x_{i_1},x_{i_1-1},\ldots,x_{i_0+1},
 K,
 y_{j_0+1},y_{j_0+2},\ldots,y_{j_1}                     \tag{2.4}
\]

has exactly

\[
                         A+B-1                           \tag{2.5}
\]

letters.  For every `(i,j) in I times J`, it contains a distinct interval of
length

\[
                    (i-i_0)+(j-j_0)+1                   \tag{2.6}
\]

whose union is exactly

\[
                           C_i\cup D_j.                  \tag{2.7}
\]

Consequently, if `A+B-1<=d`, all `AB` values in the rectangle are distinct
short-cell occurrences in one literal depth-`d` source atom.

#### Proof

For `i>i_0` start at the occurrence `x_i`, and for `i=i_0` start at `K`.
For `j>j_0` end at the occurrence `y_j`, and for `j=j_0` end at `K`.  The
interval union is

\[
 \left(\bigcup_{p=i_0+1}^{i}x_p\right)
 \cup K\cup
 \left(\bigcup_{q=j_0+1}^{j}y_q\right)
 =C_i\cup D_j.                                           \tag{2.8}
\]

Its endpoints recover `(i,j)`, so the occurrence intervals are distinct.
Counting their letters gives (2.6), and its maximum is (2.5). \(\square\)

### Corollary 2.2 (free hulls)

Any prescribed subset of an `A` by `B` rectangle, including an L-shape or a
disconnected collection of subrectangles, costs no more than `A+B-1`: use
the same atom and mark only the desired cell intervals.  The additional
hull values are harmless in a universal word.

This observation is already a genuine escape from the separated-block
laminar-star obstruction.  It must not be confused with a claim that an
arbitrary union of distant rectangles has one such atom.

## 3. Product SCDs partition the whole target band

Put `h=floor(k/2)` and split the coordinates as

\[
                         [k]=X\mathbin{\dot\cup}Y,
 \qquad |X|=h,\quad |Y|=k-h.                             \tag{3.1}
\]

Choose any symmetric-chain decomposition on each half cube.  In `B_h`, a
chain of minimum rank `u` has

\[
              \lambda_h(u)=h-2u+1                       \tag{3.2}
\]

vertices, and the number of such chains is

\[
              c_h(u)={h\choose u}-{h\choose {u-1}},      \tag{3.3}
\]

with the second binomial interpreted as zero at `u=0`.  Use the analogous
notation for `B_{k-h}`.

For a pair of chains of types `(u,v)`, number their vertices from zero.  The
product grid has dimensions

\[
             \lambda_h(u)\times\lambda_{k-h}(v),         \tag{3.4}
\]

and cell `(i,j)` is the unique target \(C_i\cup D_j\), of rank

\[
                            u+v+i+j.                      \tag{3.5}
\]

Define its active deep band

\[
 G_{uv}=\{(i,j):0\leq i<\lambda_h(u),\ 0\leq j<
 \lambda_{k-h}(v),\ d+1\leq u+v+i+j\leq r-d-1\}.        \tag{3.6}
\]

For a finite grid set `G`, let `rho_d(G)` be the minimum of

\[
                         \sum_Q(A_Q+B_Q-1)                \tag{3.7}
\]

over covers of `G` by consecutive axis rectangles `Q` of dimensions
`A_Q` by `B_Q` satisfying

\[
                         A_Q+B_Q-1\leq d.                 \tag{3.8}
\]

Rectangles may overlap and may cover inactive cells.

### Theorem 3.1 (exact standalone rectangle-atlas reduction)

There is one nonempty source word realizing every target in
\(\mathcal L_{\rm deep}\) on a distinct marked interval, of physical length

\[
 R_{k,d}:=
 \sum_{u=0}^{\lfloor h/2\rfloor}
 \sum_{v=0}^{\lfloor(k-h)/2\rfloor}
 c_h(u)c_{k-h}(v)\rho_d(G_{uv}).                          \tag{3.9}
\]

Moreover, (3.9) is the minimum physical length within the architecture that
concatenates independent atoms of Theorem 2.1 over this fixed product-SCD
partition.

#### Proof

Every subset of `[k]` has a unique restriction to `X` and `Y`, and each
restriction lies on a unique SCD chain.  Thus the product grids partition
the Boolean cube, and (3.5)--(3.6) partition the deep targets.

Choose an optimal rectangle cover in each grid and instantiate one atom per
rectangle.  Assign every active cell to one rectangle containing it and mark
the corresponding interval supplied by Theorem 2.1.  Occurrences in
different atoms use disjoint source positions.  A rectangle in (3.8) which
contains a deep cell has core rank at least

\[
 (d+1)-(A_Q+B_Q-2)\geq2,                                 \tag{3.10}
\]

so its core letter is nonempty.  Concatenation therefore gives a legal
nonempty word of length (3.9).  Conversely every independent atom has the
displayed cost, proving the architecture-relative minimum assertion.
\(\square\)

Theorem 3.1 is a literal source atlas.  Its concatenation need not have
rank-`r` length-`d+1` windows, simple owners, Johnson adjacency, or a
connected owner trace.  None of those properties follows from (3.9).

## 4. A finite exact row-guillotine upper bound

For fixed `(u,v)`, the active cells in row `i` form the interval

\[
 J_i=[\ell_i,r_i],
\quad
 \ell_i=\max\{0,d+1-u-v-i\},
\quad
 r_i=\min\{\lambda_{k-h}(v)-1,r-d-1-u-v-i\}.             \tag{4.1}
\]

Discard the empty rows; the remaining row indices are consecutive.  For a
slab `[a,b]` of active rows put

\[
 A=b-a+1,
 \quad L=\min_{a\leq i\leq b}\ell_i,
 \quad R=\max_{a\leq i\leq b}r_i,
 \quad w=R-L+1.                                          \tag{4.2}
\]

If `A<=d`, set

\[
 B_{\max}=d+1-A,
 \qquad q=\left\lceil{w\over B_{\max}}\right\rceil,
 \qquad
 \gamma(a,b)=w+q(A-1).                                  \tag{4.3}
\]

Indeed, split the column hull `[L,R]` into `q` consecutive pieces of widths
at most `B_max`.  The resulting `A` by `B` rectangles obey (3.8), and their
total cost is exactly (4.3).

Let the active rows run from `i_-` through `i_+`.  Define

\[
 F(i_--1)=0,
 \qquad
 F(j)=\min_{\substack{i_-\leq a\leq j\\j-a+1\leq d}}
       \{F(a-1)+\gamma(a,j)\}.                            \tag{4.4}
\]

Let `F^T` be the same dynamic programme after transposing the grid, and put

\[
             \rho_d^{\rm RG}(G_{uv})
             =\min\{F(i_+),F^T(j_+)\}.                   \tag{4.5}
\]

### Proposition 4.1

For every product grid,

\[
                 \rho_d(G_{uv})\leq\rho_d^{\rm RG}(G_{uv}). \tag{4.6}
\]

Hence replacing \(\rho_d\) by \(\rho_d^{\rm RG}\) in (3.9) is an explicit finite,
all-`k` constructive upper bound.

#### Proof

Equation (4.3) is the exact cost of the displayed hull cover for one slab.
The recurrence (4.4) minimizes over all consecutive row-slab partitions.
Transposition supplies the second family of covers. \(\square\)

The following exact-integer evaluations of (4.4) were made on `h100`.  They
are included only to orient the remaining theorem; oscillation with the
integer deadline is visible and the table is not an asymptotic proof.

\[
\begin{array}{c|c|c}
k&d&R^{\rm RG}_{k,d}/W\\ \hline
41&5&0.4066903\\
61&5&0.7843787\\
81&6&0.7482140\\
101&7&0.7003129\\
151&8&0.8908790\\
201&9&0.9989259\\
301&11&1.0498471\\
401&13&1.0238778\\
501&15&0.9638360
\end{array}                                               \tag{4.7}
\]

In particular, the present row-guillotine proof does not establish
`R_{k,d}<=W+O(d)` for every large `k`.

## 5. The sharp general area bound and budget normalization

If a rectangle has cost `c=A+B-1`, then

\[
 AB\leq\left\lfloor{(c+1)^2\over4}\right\rfloor
 \leq { (d+1)^2\over4d}\,c
 \qquad(1\leq c\leq d).                                  \tag{5.1}
\]

The second inequality follows because `(c+1)^2/c=c+2+1/c` is nondecreasing
for `c>=1`.

### Theorem 5.1 (rectangle-atlas lower bound)

Every cover in (3.7)--(3.8) satisfies

\[
 R_{k,d}\geq {4d\over(d+1)^2}L_{\rm deep}.               \tag{5.2}
\]

Under the standard central local-limit asymptotic for the deadline (1.1),

\[
 {L_{\rm deep}\over dW}
 \longrightarrow 2\Phi(-\sqrt{\pi/2}),                  \tag{5.3}
\]

and therefore

\[
 \liminf_{k\to\infty}{R_{k,d}\over W}
 \geq 8\Phi(-\sqrt{\pi/2})=0.84\ldots .                 \tag{5.4}
\]

#### Proof

The rectangles cover all `L_deep` active cells, counted with multiplicity at
least one.  Sum (5.1) and rearrange to obtain (5.2).  Equations (5.3)--(5.4)
then follow directly. \(\square\)

The old separated PBBS payload bank has only

\[
                    (1-e^{-\pi/4}+o(1))W=0.544\ldots W   \tag{5.5}
\]

free physical positions.  Thus **no standalone concatenation of these
rectangle atoms can be overlaid only in that old free bank**.  On the other
hand (5.4) is below the full coefficient-one budget `W+d`.  The product
atlas remains numerically viable only if most of its positions also serve
the rank-middle owner chronology.  Adding it after a separate `W+d` PBBS
word is impossible by definition.

## 6. What strong HC-SCP Type 1 pairing really shares

Let `C=(C_0,...,C_{m-1})` and
`C'=(C'_0,...,C'_{m+1})` be a Type 1 pair in the sense of
Streib--Trotter: the chains are disjoint,

\[
                    C'_0\subset C_0,
 \qquad |C_0\setminus C'_0|=1,                            \tag{6.1}
\]

and

\[
                    C_{m-1}\subset C'_{m+1},
 \qquad |C'_{m+1}\setminus C_{m-1}|=1.                   \tag{6.2}
\]

Fix a segment `D_0 subset ... subset D_{B-1}` on a disjoint coordinate set,
with increments `y_1,...,y_{B-1}`.

### Proposition 6.1 (exact paired boundary-row fan)

If `B+1<=d`, the word

\[
 C_0\cup D_0,\quad C'_0\cup D_0,\quad
 y_1,\ldots,y_{B-1}                                     \tag{6.3}
\]

of length `B+1` realizes both complete rows

\[
 \{C_0\cup D_j:0\leq j<B\},
 \qquad
 \{C'_0\cup D_j:0\leq j<B\}.                           \tag{6.4}
\]

The analogous word with the larger top core first,

\[
 C'_{m+1}\cup D_0,\quad C_{m-1}\cup D_0,\quad
 y_1,\ldots,y_{B-1},                                    \tag{6.5}
\]

shares the top two boundary rows.  Each fan saves `B-1` physical letters
relative to two independent `1` by `B` atoms.

#### Proof

In (6.3) the second core is contained in the first.  Thus an interval from
the first core through `y_j` has union \(C_0\cup D_j\), while the interval
starting at the second has union \(C'_0\cup D_j\).  The longest first-row
interval has `B+1` letters.  Equation (6.5) is identical using (6.2).
\(\square\)

The extra unit of deadline is real.  If both distinct core occurrences and
one common suffix of `B-1` increment occurrences are used, the interval for
the larger core and the last suffix value contains at least `B+1` letters.
Hence this literal sharing is unavailable at width `B=d`.

More generally, a descending chain of `s` cores can share one `B`-row arm
in `B+s-1` letters, provided `B+s-1<=d`.  The Type 1 axioms guarantee only
the two endpoint nestings (6.1)--(6.2), not a long nested family.

### Proposition 6.2 (no automatic full-rectangle sharing)

The Type 1 axioms alone do not allow either boundary fan in Proposition 6.1
to be thickened to height two on the longer chain while retaining the same
suffix arm.

#### Proof

The next longer-chain set `C'_1` has the same rank as `C_0`.  The two chains
in an SCD are disjoint, so \(C'_1\ne C_0\); consequently

\[
                            C'_1\not\subseteq C_0.         \tag{6.6}
\]

Fix the final occurrence on the purported common suffix arm.  Intervals
ending at that same occurrence are nested as intervals, so their unions are
linearly ordered by inclusion.  But adding the same disjoint `D`-prefix to
\(C_0\) and \(C'_1\) leaves them incomparable by (6.6) and equal rank.
Therefore those two rows cannot use the same suffix-arm endpoint.  Thus the
endpoint cover relation certifies exactly the one-row fan, not a shared
positive-height rectangle.  At the top, \(C'_m\) and \(C_{m-1}\) are the
analogous distinct equal-rank incomparable pair.
\(\square\)

This is the precise contribution of the two boundary cover edges.  The
Hamilton paths in the strong HC-SCP theorem are paths on target vertices;
they do not by themselves identify source positions or prove a smaller
semiperimeter atlas.  Proposition 6.1 is a genuine local saving, but a
global saving below coefficient one still requires a counted paired cover
or a new multi-seam chart.

There is a canonical safe way to count the guaranteed saving.  If `c_n(u)`
is (3.3), let `p_u` be the number of Type 1 pairs joining a long chain of
minimum rank `u-1` to a short chain of minimum rank `u`.  The block
partition forces

\[
 p_0=0,
 \qquad
 p_{u+1}=c_n(u)-p_u,                                     \tag{6.7}
\]

with the final residue consisting of the allowed Type 2 chains.  For every
paired chain pair whose shorter member has at least two vertices, and every
chain on the other axis, do the following:

1. delete the two endpoint rows from both product grids and apply the exact
   row-guillotine DP to the two interiors;
2. on each paired bottom or top row, fan-cover the intersection of the two
   active column intervals in chunks of width at most `d-1`;
3. cover the at most two unshared endpoint pieces by ordinary height-one
   atoms; and
4. take the cheaper of this cover and the two independent row-guillotine
   covers.

For a pair whose shorter chain is a singleton, use the independent covers;
its bottom and top row are the same row, so the two-fan accounting would
double count it.

This is an unconditional cover because every target is assigned either to
an interior grid, a paired fan, or an unshared endpoint piece.  Applying the
same construction on either half-axis and taking the better result gives the
following remote exact-integer census:

\[
\begin{array}{c|c|c|c}
k&d&R^{\rm RG}_{k,d}/W&R^{\rm pair}_{k,d}/W\\ \hline
41&5&0.4066903&0.4034144\\
61&5&0.7843787&0.7774386\\
81&6&0.7482140&0.7440392\\
101&7&0.7003129&0.7001721\\
151&8&0.8908790&0.8908790\\
201&9&0.9989259&0.9988055\\
301&11&1.0498471&1.0498471
\end{array}                                               \tag{6.8}
\]

Thus the two Type 1 cover edges do improve some finite covers, but their
guaranteed endpoint use is too small to close the first audited
above-coefficient-one case.  This does not rule out a more correlated
multi-seam word; it rules out treating the strong HC-SCP endpoint relations
alone as that missing compression theorem.

## 7. Positive residence versus biresidence

Let `T=(T_0,...,T_{W-1})` be a linear rank-`r` Johnson owner path and let
`A` be a nonempty depth-`d` antecedent,

\[
                         T_i=\bigcup_{p=i}^{i+d}A_p.       \tag{7.1}
\]

For every source interval `[a,b]` of length at least `d+1`, literal
associativity gives

\[
 \boxed{
 \bigcup_{p=a}^{b}A_p=\bigcup_{i=a}^{b-d}T_i .}          \tag{7.2}
\]

For a Johnson path, the maximal antecedent exists exactly when every
internal **positive** coordinate run has length at least `d+1` (with the
usual clipped boundary convention).  No lower bound on zero-run lengths is
used in either that criterion or (7.2).

### Corollary 7.1 (one-sided residence suffices for the flat compiler)

Suppose the chosen opening has positive residence and its nonwrapping
consecutive-owner union deck contains every designated proper-upper target.
Then its maximal antecedent rematerializes all those upper targets by (7.2),
even if the owner trace has short zero gaps.

Thus biresidence is not needed for:

1. existence of the flat maximal antecedent;
2. preservation of short lower cells inside that antecedent; or
3. read-only upper witnesses already present in the owner-union deck.

It can still be needed for complement-dual packets, flag-convex protected
connectors, cyclic cutting, and factor fusion.  Those are separate graph
and protection requirements.

The rectangle atlas of Sections 2--4 does **not** by itself prove the
hypothesis of Corollary 7.1.  Its arbitrary concatenated word need not induce
the desired owner path at all.  Nor does covering the deep lower band imply
that every upper set occurs as a source union: OR is not preserved by
complementation.  Upper coverage is automatic only after the same physical
letters have been compiled under an owner chronology whose consecutive
union deck is already upper-complete.

## 8. The exact remaining gate

The construction has moved the deep payload problem from an impossible
separated-block overlay to the following concrete coefficient-one question.

> Find a product-SCD rectangle/multi-seam cover of total cost at most
> `W+O(d)` and order those same physical letters so that their length-`d+1`
> windows form a simple positive-resident rank-`r` Johnson chronology with
> the required upper-union deck; or prove that no such joint compiler exists.

There are two independent unresolved parts:

1. **source cost:** the exact row-guillotine bound crosses above `W` at some
   audited deadlines, while the universal area lower bound is only
   `0.84...W`; the Type 1 endpoint fans give a real but not yet globally
   counted saving;
2. **joint chronology:** even a standalone atlas of length below `W` is not
   a PBBS factor until rank, Johnson adjacency, simplicity, positive
   residence, protected endpoints, and one connected opening hold on the
   same word.

What is now ruled out is the idea of inserting this atlas solely into the
old `0.544...W` free bank.  What remains open, and numerically plausible, is
a replacement chronology in which the product rectangles and the middle
owners are two readings of the same coefficient-one source.
