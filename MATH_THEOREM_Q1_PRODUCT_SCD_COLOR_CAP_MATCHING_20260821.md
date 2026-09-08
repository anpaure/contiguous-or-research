# A product-SCD matching solves the clustered `q=1` color-cap relaxation up to `O(W_b/sqrt b)`

**Status (2026-08-21).** Every statement below is proved.  At upper offset
`q=1`, the full tokenwise Boolean-containment relaxation has a matching of
size

\[
 {2b\choose b+1}-O\left({W_b\over\sqrt b}\right)
 =(1-o(1))W_b,
 \qquad W_b={2b\choose b},
\]

which respects every clustered phase-color capacity.  The construction uses
arbitrary symmetric chain decompositions on the two local `b`-sets, discards
only pairs of chains with the same bottom rank, and perfectly matches every
remaining chain rectangle.

This is a theorem only in the **tokenwise orbit relaxation**.  It does not
make independently selected containment edges arise from common cyclic
orders, and it says nothing about offsets `q>=2`.  Those are still open.

## 1. The `q=1` color-cap problem

Let `A,B` be disjoint `b`-sets, with `b` odd, and put

\[
 \mathcal U_r=\{(X,Y):X\subseteq A,\ |X|=r,
                         Y\subseteq B,\ |Y|=b-r\},
 \qquad L_r=|\mathcal U_r|={b\choose r}^2.          \tag{1.1}
\]

At rank `b+1`, a containment edge from `(X,Y)` either adds one `A`-letter
or one `B`-letter.  Give these two edge colors the clustered capacities

\[
 Q_r^A={r\over b}L_r,
 \qquad
 Q_r^B={b-r\over b}L_r.                             \tag{1.2}
\]

For odd prime `b` and `1<=r<=b-1`, these are the exact integer token counts
from the clustered schedules: the `A^rB^(b-r)` phase word has `r` next-`A`
phases and `b-r` next-`B` phases, and each phase contributes
`L_r/b` occurrence tokens.  At `r=0,b`, (1.2) remains the natural algebraic
endpoint convention.  A graph matching with at most `Q_r^A,Q_r^B` edges of
the two colors lifts tautologically to the tokenwise relaxation by assigning
its edges injectively to distinct tokens of their colors.

## 2. Product symmetric-chain rectangles

Fix arbitrary symmetric chain decompositions of the Boolean lattices on
`A` and `B`.  Put

\[
 c_d={b\choose d}-{b\choose d-1},
 \qquad 0\le d\le h={b-1\over2},                    \tag{2.1}
\]

with `binom(b,-1)=0`.  Every symmetric chain decomposition has exactly
`c_d` chains whose bottom rank is `d`; such a chain contains one set at
each rank from `d` through `b-d`.

Pair an `A`-chain with bottom rank `a` and a `B`-chain with bottom rank
`c`.  Their rank-`b` vertices are

\[
 (X_r,Y_{b-r}),
 \qquad \max(a,c)\le r\le b-\max(a,c).              \tag{2.2}
\]

Their rank-`(b+1)` vertices and the chosen matching are as follows.

* If `a<c`, the target ranks are `s=c+1,...,b-c+1`.  Match every source
  of local `A`-rank `r=c,...,b-c` to `(X_(r+1),Y_(b-r))`.  This is the
  unique perfect matching of the rectangle diagonal and every edge adds
  `A`.
* If `a>c`, the target ranks are `s=a,...,b-a`.  Match every source of
  local `A`-rank `r=a,...,b-a` to `(X_r,Y_(b-r+1))`.  This is the unique
  perfect matching and every edge adds `B`.
* If `a=c`, use no edge from this chain pair.

Different chain pairs have disjoint source and target vertices.  Hence the
union just defined is a labelled containment matching.

## 3. Exact color ledger

For `0<=t<=h`, write

\[
 S_t=\sum_{d=0}^t c_d={b\choose t},
 \qquad E_t=\sum_{d=0}^t c_d^2,
 \qquad F_t={S_t^2-E_t\over2}.                      \tag{3.1}
\]

### Lemma 3.1 (the off-diagonal chain-pair bound)

For every `0<=t<=h`,

\[
 E_t\ge {b-2t\over b}S_t^2,
 \qquad\hbox{and consequently}\qquad
 F_t\le {t\over b}S_t^2.                           \tag{3.2}
\]

#### Proof

The claim is equality at `t=0`.  For `t>=1`, put

\[
 x={S_{t-1}\over S_t}={t\over b-t+1},
 \qquad \delta_t={b-2t\over b}.
\]

If the first inequality holds at `t-1`, then

\[
 {E_t\over S_t^2}
 ={E_{t-1}+(S_t-S_{t-1})^2\over S_t^2}
 \ge \delta_{t-1}x^2+(1-x)^2
 =\delta_t+{2t\over b(b-t+1)}
 \ge\delta_t.
\]

This proves the first inequality by induction.  The second is its
rearrangement.  \(\square\)

### Theorem 3.2 (all clustered `q=1` color capacities are respected)

At every source split `r`, the matching of Section 2 uses exactly

\[
 F_{\min(r,b-r)}                                    \tag{3.3}
\]

next-`A` edges and the same number of next-`B` edges.  In particular these
counts are at most `Q_r^A` and `Q_r^B` from (1.2).

#### Proof

Put `t=min(r,b-r)`.  A chain pair contains a source of split `r` exactly
when both bottom ranks are at most `t`.  The next-`A` edges are precisely
the ordered pairs `a<c<=t`, and the next-`B` edges are precisely the ordered
pairs `c<a<=t`.  Each count is

\[
 \sum_{0\le a<c\le t}c_ac_c
 ={(\sum_{d\le t}c_d)^2-\sum_{d\le t}c_d^2\over2}=F_t.
\]

If `r<=h`, Lemma 3.1 gives `F_r<=rL_r/b=Q_r^A`, while
`F_r<=L_r/2<=(b-r)L_r/b=Q_r^B`.  If `r>=h+1`, apply the same argument with
`t=b-r`; the smaller capacity is now `Q_r^B`.  \(\square\)

## 4. The discarded mass is `O(W_b/sqrt b)`

An equal-bottom chain pair with bottom rank `d` has exactly `b-2d`
rank-`(b+1)` vertices.  Therefore the exact number of targets omitted by
the matching is

\[
 D_b=\sum_{d=0}^h c_d^2(b-2d).                     \tag{4.1}
\]

### Lemma 4.1 (Gaussian bound for the equal-bottom rectangles)

\[
 D_b=O\left({W_b\over\sqrt b}\right).              \tag{4.2}
\]

#### Proof

Write `b=2h+1` and `d=h-k`.  Then

\[
 c_{h-k}={b\choose h-k}{2k+2\over h+k+2}.          \tag{4.3}
\]

Moreover

\[
 {{b\choose h-k}\over {b\choose h}}
 =\prod_{j=0}^{k-1}{h-j\over h+j+2}
 \le \exp\left(-{k(k+1)\over b}\right),           \tag{4.4}
\]

because the `j`th factor is
`1-(2j+2)/(h+j+2)` and `h+j+2<=b`.  Equations
(4.3)--(4.4) give

\[
 c_{h-k}
 \le {4(k+1)\over b}{b\choose h}
       e^{-k(k+1)/b}.                               \tag{4.5}
\]

Since `b-2d=2k+1`, comparison with the Gaussian integral gives

\[
 D_b
 \le {16{b\choose h}^2\over b^2}
       \sum_{k=0}^h(2k+1)(k+1)^2e^{-2k(k+1)/b}
 =O\left({b\choose h}^2\right).                    \tag{4.6}
\]

The standard central-binomial estimates give
`binom(b,h)^2=O(W_b/sqrt b)`, proving (4.2).  \(\square\)

### Theorem 4.2 (near-perfect `q=1` tokenwise matching)

The color-capacitated rank-`b` to rank-`(b+1)` containment graph has a
matching of exact size

\[
 {2b\choose b+1}-D_b
 ={2b\choose b+1}
  -O\left({W_b\over\sqrt b}\right)
 =(1-o(1))W_b.                                      \tag{4.7}
\]

If the product construction retains only payload ranks

\[
 I=[H+2,b-H-2],\qquad H=o(b),                       \tag{4.8}
\]

deleting matching edges whose source rank lies outside `I` loses at most

\[
 \sum_{r\notin I}{b\choose r}^2=e^{-\Omega(b)}W_b. \tag{4.9}
\]

Thus (4.7) remains valid for the genuine central payload interval.

#### Proof

Every unequal-bottom chain rectangle is perfectly matched, while every
equal-bottom rectangle is discarded.  This proves the first equality in
(4.7); Lemma 4.1 proves the estimate.  Deleting one edge can be charged to
its unique source, giving (4.9).  Finally, when `H=o(b)`, the omitted local
binomial layers have entropy `o(b)`, whereas `W_b=\exp((2\log2+o(1))b)`,
which proves the displayed exponential bound.  \(\square\)

## 5. Exact scope and next gate

This theorem eliminates the first color-capacitated matching gate at
`q=1`, with `O(W_b/sqrt b)=o(W_b)` loss.  It is stronger than a fractional
transport statement and uses actual labelled source and target sets.

It does **not** solve either remaining coinstantiation problem:

1. for `q>=2`, product chain rectangles become two-dimensional distance-`q`
   containment systems and the analogous color-cap matching is unproved;
2. even at `q=1`, the token assigned to an edge is abstractly
   interchangeable with every token of its color.  One must still realize
   the selected edges by the actual cyclic-order/phase occurrences of a
   coherent tight-cycle bank.

Accordingly this is positive progress at the exact tokenwise gate, not a
coefficient-one proof and not an unconditional use of the growing-rank
Baranyai--Katona conjecture.

