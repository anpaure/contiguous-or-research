# Nonlocal-pivot Bender--Knuth partition

## 1. Result and scope

The last-`DU` partition in `BK_SUPPORT_FORMULA.md` can be strengthened.
Instead of fixing the final active block of each critical sequence, one may
leave that block free and use the last earlier `DU` as a fixed carrier
barrier.  The final generator then has one fixed **nonlocal** physical
support throughout the cell.

The resulting cells still form an exact partition of every odd
Bender--Knuth orbit into radius-pure, physical, isometric cubes.  In every
cell the number of retained nonlocal directions is exactly the number of
nonempty critical levels.  For a critical orientation sequence of length
`a`, the exact size-biased mean codimension improves from

\[
                 2-2^{1-a}
       \quad\hbox{to}\quad
                 2-2^{2-a}<2.                       \tag{1.1}
\]

Consequently all but `o(W)` of the

\[
                         W=\binom{2m}{m}
\]

middle-layer vertices lie in partition cells of dimension at least

\[
                         \frac m8-m^{5/6}.           \tag{1.2}
\]

The quantifier in this last sentence concerns `W-o(W)` **vertices**, not
`W-o(W)` distinct cells.

This theorem does not prove any lower- or upper-shadow coverage.  In
particular, retaining a controlled nonlocal direction at each critical
level is not by itself a shift-compatible SCD.

## 2. The carrier input

Fix one odd-BK orbit.  Its uncoloured Motzkin skeleton, active mixed blocks,
RSK radius `d`, and critical sequences are fixed.  In one nonempty critical
sequence, list the active mixed blocks from left to right as

\[
                         p_1<\cdots<p_a              \tag{2.1}
\]

and write

\[
 x_r=\begin{cases}
 0,&p_r\text{ is }UD,\\
 1,&p_r\text{ is }DU.
 \end{cases}                                         \tag{2.2}
\]

Here `p_r` is the odd ground coordinate of its two-position block.  Let
`e_0` be the even initial carrier at this stack level.  The exact support
formula from `BK_SUPPORT_FORMULA.md` says

\[
 S(x,p_r)=
 \begin{cases}
  \{p_r,p_r+1\},
       &\text{if some }x_t=1\text{ with }t>r,\\[1mm]
  \{p_r,p_s+1\},
       &s=\max\{t<r:x_t=1\},\\[1mm]
  \{p_r,e_0\},
       &x_t=0\text{ for every }t<r,
 \end{cases}                                         \tag{2.3}
\]

where the second and third lines apply when there is no later `1`.
All active generators outside critical sequences have their fixed native
support `{p,p+1}`.

## 3. The one-sequence partition

For `x in {0,1}^a`, define

\[
 b(x)=\max\{r<a:x_r=1\},                             \tag{3.1}
\]

with `b(x)=0` if this set is empty.  Notice that the last bit `x_a` is
deliberately ignored.

Define `P_0,P_1,...,P_(a-1)` by

\[
\begin{aligned}
 P_0&=\{x:x_1=\cdots=x_{a-1}=0\},\\
 P_b&=\{x:x_b=1,\ x_{b+1}=\cdots=x_{a-1}=0\}
          \qquad(1\le b<a).
\end{aligned}                                        \tag{3.2}
\]

In `P_b`, all unmentioned bits are free.  Thus `x_a` is free in every cell;
when `b>0`, the prefix `x_1,...,x_(b-1)` is also free.

### Theorem 1 (disjoint exhaustive subcubes)

The cells in (3.2) are pairwise disjoint and exhaust `{0,1}^a`.  Their
dimensions and codimensions are

\[
\begin{array}{c|c|c}
\text{cell}&\dim&\operatorname{codim}\\ \hline
P_0&1&a-1\\
P_b\ (1\le b<a)&b&a-b.
\end{array}                                          \tag{3.3}
\]

This includes the boundary case `a=1`: then `P_0={0,1}`, its dimension is
one, and its codimension is zero.

#### Proof

Every orientation word has a unique last `1` among its first `a-1`
positions, or has none.  This gives exactly one value of `b`.  Formula
(3.2) fixes `a-1` bits when `b=0`; for `b>0` it fixes `x_b` and the
`a-1-b` following bits before `x_a`, a total of `a-b` bits.  QED.

## 4. Fixed physical supports, including the nonlocal pivot

### Theorem 2 (one retained nonlocal direction)

Every `P_b` is a fixed-support physical isometric cube.  More precisely:

* if `b>0`, the free prefix generators `p_1,...,p_(b-1)` have their native
  supports `{p_r,p_r+1}`;
* the final generator `p_a` is free and has the fixed nonlocal support

  \[
                    \{p_a,p_b+1\};                   \tag{4.1}
  \]

* in `P_0`, the only free generator from this critical sequence is `p_a`,
  and its fixed support is

  \[
                    \{p_a,e_0\}.                    \tag{4.2}
  \]

Thus every cell retains exactly one nonlocal direction from this critical
sequence.

#### Proof

For `r<b`, the fixed bit `x_b=1` is later than `r`.  It remains fixed while
all free bits, including `x_a`, are toggled.  The first line of (2.3)
therefore gives the native support `{p_r,p_r+1}` everywhere in the cell.

There is no index after `a`.  If `b>0`, the fixed `1` at `b` is the most
recent earlier carrier overwrite seen by `p_a`: every position from `b+1`
through `a-1` is fixed to zero.  Hence (2.3) gives (4.1), independently of
all free prefix bits and of the orientation of `p_a` itself.  If `b=0`, all
earlier orientations are fixed to zero, so the inherited carrier is `e_0`
and (4.2) follows.

The native prefix pairs are mutually disjoint.  The coordinate `p_b+1`
belongs to the fixed barrier block `p_b`, not to a free prefix block, while
`e_0` belongs to the inactive `UU` block which introduced this stack slot.
The odd coordinate `p_a` belongs only to the final block.  Consequently the
listed supports are pairwise disjoint.  Toggling any subset of their
generators therefore flips exactly the associated disjoint pairs in the
inverse-RSK middle word.  This proves physical injectivity and isometry.
QED.

## 5. Products over all critical levels

Apply (3.2) independently to every nonempty critical sequence and leave all
noncritical active generators free.

### Theorem 3 (orbitwise nonlocal-pivot partition)

The Cartesian products of the cells `P_b` partition the complete odd-BK
orbit into disjoint, radius-pure, physical isometric cubes.  Within each
product cell all retained physical supports are pairwise disjoint, including
supports coming from different critical levels.

If the orbit has `c` nonempty critical sequences, then every cell has
exactly

\[
                              c                     \tag{5.1}
\]

retained nonlocal directions.  In particular,

\[
                        0\le c\le\lfloor d/2\rfloor. \tag{5.2}
\]

#### Proof

Disjointness and exhaustion follow by taking products of Theorem 1.  Odd
Bender--Knuth moves at distinct active blocks commute and preserve the RSK
shape, so it remains only to audit physical support collisions.

At one critical level, Theorem 2 handles all collisions.  At distinct
levels, the persistent carriers occupy distinct stack depths and therefore
distinct even ground coordinates.  A carrier of the form `p_b+1` belongs to
a fixed mixed block, while an initial carrier belongs to an inactive `UU`
block; neither block supplies a retained native direction.  The odd endpoint
`p_a` is the unique odd coordinate of its own final block.  Native supports
from all remaining free blocks are disjoint block pairs.  These observations
exclude every native--native, native--carrier, and carrier--carrier
collision.

Each nonempty critical sequence contributes precisely its final generator
as a nonlocal free direction; all of its other free generators are native.
This proves (5.1).  Critical levels can occur only for
`1<=h<=floor(d/2)`, proving (5.2).  QED.

## 6. Exact codimension law

Condition on one odd-BK orbit.  Its active orientation bits are independent
and uniform under the uniform measure on the orbit.  For a critical sequence
of length `a`,

\[
 \Pr(b=0)=2^{1-a},\qquad
 \Pr(b=j)=2^{j-a}\quad(1\le j<a).                    \tag{6.1}
\]

Using (3.3), its size-biased mean cell codimension is

\[
\begin{aligned}
 \mathbb E\Delta_a
 &= (a-1)2^{1-a}+\sum_{j=1}^{a-1}(a-j)2^{j-a}\\
 &= (a-1)2^{1-a}+\sum_{t=1}^{a-1}t2^{-t}\\
 &=2-2^{2-a}<2.                                     \tag{6.2}
\end{aligned}

The formula also gives zero at `a=1`.  For comparison, the old last-`DU`
partition had mean `2-2^(1-a)`, so the improvement is exactly
`2^(1-a)` per sequence.

If the critical lengths are `a_1,...,a_c`, the total cell codimension
`Delta` inside the full active orbit satisfies the exact identity

\[
       \mathbb E(\Delta\mid\text{orbit})
       =\sum_{j=1}^c(2-2^{2-a_j})<2c\le d.           \tag{6.3}
\]

No independence between different critical sequences is needed for the
last estimate, although the orbit product in fact supplies it.

## 7. Large-cell consequence

Let `A` be the number of active odd generators in an orbit.  It is constant
on that orbit, and every cell has dimension

\[
                              A-\Delta.              \tag{7.1}
\]

The two tail estimates already proved in `BK_SUPPORT_FORMULA.md` are:

1. the union of the orbits with `A<m/8` contains `o(W)` vertices, because
   every `DU` block is active and the binomial bound for fewer than `m/8`
   `DU` blocks has exponential rate below `log 4`;
2. the number of tableaux with radius
   `d>ceil(m^(2/3))` is `o(W)`, by the telescoping two-row hook count and its
   Gaussian product bound.

On every remaining orbit, (6.3) and Markov's inequality give

\[
 \Pr\{\Delta>m^{5/6}\mid\text{orbit}\}
 \le {d\over m^{5/6}}=O(m^{-1/6}).                  \tag{7.2}
\]

Sum (7.2) with orbit-size weights and add the two tail families.  Only
`o(W)` middle vertices are discarded.  Every surviving vertex belongs to a
partition cell with

\[
 \dim\ge {m\over8}-m^{5/6}.                          \tag{7.3}
\]

This proves (1.2).

## 8. What the extra directions do not prove

The strengthening is exact but limited:

* it contributes exactly one nonlocal support per nonempty critical level,
  hence at most `floor(d/2)` per cell;
* the remaining free directions still use the one native adjacent matching;
* neither a cube's lower faces nor its upper faces have been shown globally
  injective across cells;
* no cycle factor, shadow permutation, pinning theorem, or universal-OR word
  follows from the partition alone.

The result supplies a rigorously controlled nonlocal reservoir inside the
existing radius-pure partition.  Whether conjugates of this reservoir can
be mixed to resolve growing-depth shadows remains open.

## 9. Finite checker

`scratch/verify_nonlocal_pivot_bk_partition.py` independently:

1. enumerates balanced binary words;
2. computes recording tableaux by ordinary row insertion;
3. constructs every nonlocal-pivot cell;
4. checks disjointness and exhaustion of every orbit;
5. compares actual inverse words on every cell edge;
6. checks support constancy, global pairwise disjointness, the explicit
   carrier coordinate, exactly one nonlocal direction per critical
   sequence, and the rational expectation (6.3).

It passes exhaustively through `m=9`:

```
m=7 tableaux=3432  cells=834  cell_edges=8764   carriers=276:  PASS
m=8 tableaux=12870 cells=2427 cell_edges=38638  carriers=943:  PASS
m=9 tableaux=48620 cells=7101 cell_edges=167908 carriers=3155: PASS
```

The computation is an audit of the proof, not an input to it.
