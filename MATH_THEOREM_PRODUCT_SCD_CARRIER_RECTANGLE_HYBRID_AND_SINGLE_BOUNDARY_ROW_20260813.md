# Product-SCD carrier rectangles lose only one global boundary row

**Date:** 2026-08-13  
**Method:** exact replacement of diagonal-fan words by singleton-increment
rectangle words and remote weighted census on `h100`.  
**Status:** unconditional standalone source theorem/reduction.  It makes
every atlas atom private-letter rigid at the same physical cost and isolates
all lost targets in the single rank `R-d` row.  This is not yet a proof of
one simple rank-`R` owner chronology.

## 1. The same-length carrier rectangle word

Use the product-chain notation

\[
 C_0\subset\cdots\subset C_{a-1},\qquad
 D_0\subset\cdots\subset D_{b-1}                                  \tag{1.1}
\]

on disjoint coordinate halves, with singleton increments

\[
                         c_i=C_i-C_{i-1},\qquad d_j=D_j-D_{j-1}.     \tag{1.2}
\]

At a base cell `(i_0,j_0)` put

\[
                         K=C_{i_0}\cup D_{j_0}.                     \tag{1.3}
\]

For effective dimensions `A,B`, replace the diagonal-fan word by

\[
 c_{i_0+A-1},\ldots,c_{i_0+1},K,
 d_{j_0+1},\ldots,d_{j_0+B-1}.                                    \tag{1.4}
\]

It has the same physical length `A+B-1` as the fan word.  The rectangle
identity gives a target cell `(i,j)` at width

\[
                         i+j+1,                                    \tag{1.5}
\]

where local coordinates are measured from the base.

### Lemma 1.1 (exact replacement ledger)

Suppose a diagonal fan of dimensions `A,B` was used on the truncated
downset

\[
                         0\le i<A,quad0\le j<B,quad i+j\le s.     \tag{1.6}
\]

The same-length word (1.4) preserves every assigned cell with

\[
                         i+j\le d-1.                               \tag{1.7}
\]

If `s=d`, the only cells which can be lost are those on the outer diagonal

\[
                         i+j=d.                                    \tag{1.8}
\]

This includes its two possible axis endpoints.  They were singleton
intervals in the diagonal-fan word but have width `d+1` in (1.4), so they
must not be silently retained.

#### Proof

Equation (1.5) is the literal rectangle-word interval width.  It is at
most `d` exactly under (1.7).  The fan recurrence never assigns a local
cell beyond radius `d`, proving the stated loss set.  \(\square\)

Every noncore letter of (1.4) is a singleton private increment.  Thus the
replacement removes the nested-letter private-coordinate defect of the
diagonal fan without changing physical cost.

## 2. Why every loss has global rank `R-d`

Use the corrected slab-fan recurrence in
`MATH_THEOREM_PRODUCT_SCD_DIAGONAL_FAN_ATOM_AND_RECURSIVE_SLAB_ATLAS_20260813.md`.
For a half-chain type `(u,v)`, its active downset radius is

\[
                         s_{uv}=R-d-1-u-v.                          \tag{2.1}
\]

Consider a terminal fan rooted at local grid cell `(x,y)`.  Its effective
local radius is

\[
                         z=s_{uv}-x-y.                              \tag{2.2}
\]

By Lemma 1.1, a loss occurs only if `z=d`, and each lost cell has local
rank

\[
                         x+y+d=s_{uv}.                              \tag{2.3}
\]

Therefore its global Boolean rank is

\[
                         u+v+s_{uv}=R-d-1.                          \tag{2.4}
\]

### Theorem 2.1 (single-row boundary theorem)

Replacing every terminal diagonal-fan word in the recursive slab atlas by
its same-length carrier rectangle word preserves all marked targets except
a family contained in the single global rank

\[
                         \boxed{R-d-1}.                             \tag{2.5}
\]

All retained atom words use nonempty letters, have the original total
physical charge, and every noncore letter is a private singleton.

#### Proof

The rank calculation is (2.1)--(2.4).  The empty rank-zero core
normalization is exactly the one already handled in the corrected fan
theorem: such an atom contains no assigned deep target and is omitted.
All other cores are nonempty.  \(\square\)

The row is `R-d-1`, not `R-d`, under the deep-band normalization used in
the product-SCD atlas.  This off-by-one is forced by (2.1).

## 3. Exact loss formula inside one fan

For dimensions `A,B`, the number of cells on local diagonal `d` is

\[
 \lambda_d(A,B)=
 \max\{0,\min(A-1,d)-\max(0,d-B+1)+1\}.                             \tag{3.1}
\]

The possible axial part is

\[
 \alpha_d(A,B)=\mathbf1_{d<A}+\mathbf1_{d<B},                       \tag{3.2}
\]

and the mixed part is

\[
                         \lambda_d(A,B)-\alpha_d(A,B).              \tag{3.3}
\]

Apply (3.1) to every terminal fan with effective radius exactly `d`, and
weight by the product-SCD chain multiplicities.  This gives the exact
global lost-target count `D_(k,d)` for the displayed hybrid.

### Corollary 3.1 (literal singleton repair)

Appending one nonempty singleton source letter equal to each lost target
repairs the atlas at physical length

\[
                         R^{SF}_{k,d}+D_{k,d}.                       \tag{3.4}

This is deliberately crude but unconditional.  The appended letters need
not be compatible with a rank-middle owner chronology; (3.4) is a
standalone universal-source statement.

## 4. Remote exact census

The accompanying verifier reproduces the corrected slab orientation,
chooses among minimum-cost orientations the one with minimum boundary
loss, and evaluates (3.1)--(3.4) using exact integers on `h100`.

| `k` | `d` | source / `W` | lost / `W` | mixed / `W` | axes / `W` | singleton-repaired / `W` |
|---:|---:|---:|---:|---:|---:|---:|
| 201 | 9  | 0.8660069177 | 0.0020683991 | 0.0017889572 | 0.0002794419 | 0.8680753168 |
| 301 | 11 | 0.9083389153 | 0.0019071882 | 0.0016927290 | 0.0002144592 | 0.9102461035 |
| 361 | 12 | 0.9310649027 | 0.0018501350 | 0.0016579350 | 0.0001922000 | 0.9329150377 |
| 401 | 13 | 0.8807843896 | 0.0015422267 | 0.0013945674 | 0.0001476594 | 0.8823266164 |
| 421 | 13 | 0.9372249057 | 0.0017463582 | 0.0015782832 | 0.0001680750 | 0.9389712639 |
| 481 | 14 | 0.9308045060 | 0.0016060255 | 0.0014620242 | 0.0001440013 | 0.9324105315 |
| 561 | 15 | 0.9603361153 | 0.0016008031 | 0.0014661848 | 0.0001346183 | 0.9619369185 |
| 641 | 16 | 0.9727518967 | 0.0015462895 | 0.0014238912 | 0.0001223982 | 0.9742981862 |
| 721 | 17 | 0.9782057674 | 0.0014728996 | 0.0013629399 | 0.0001099597 | 0.9796786670 |

In these instances the loss came from only `d-2` product chain-type pairs:
respectively 7 through 15 types in the table.  Every lost target was
independently checked to have rank (2.5).

These finite inequalities do not prove a uniform all-`k` coefficient-one
bound.  They do show that the carrier-compatible correction is a thin
single-row problem, not a rebuild of the deep atlas.

## 5. The local middle clock is still absent

Put

\[
                         q=d+1.                                      \tag{5.1}
\]

Consider one replacement word (1.4), of length `L=A+B-1`, whose core
`K` has global rank `beta`.  In every atom produced by the slab recurrence,
both arms have length at most `q-1`.  Hence every internal `q`-window of
the word contains `K`.  If it uses `a` left increments and `b` right
increments, then

\[
                         a+b=q-1                                   \tag{5.2}
\]

and its union is

\[
                         C_{i_0+a}\cup D_{j_0+b},                   \tag{5.3}
\]

of rank

\[
                         \beta+q-1.                                \tag{5.4}
\]

Consecutive internal windows delete one `C` increment and insert one `D`
increment, so they form a literal Johnson path at that rank.  There are

\[
                         (L-q+1)_+                                  \tag{5.5}
\]

such internal windows.

### Theorem 5.1 (no direct rank-`R` atom clocks)

An internal `q`-window of a replacement atom has rank `R` if and only if

\[
                         \beta=R-q+1=R-d.                           \tag{5.6}
\]

No atom in the deep slab atlas has such a base.  Indeed every atom is
rooted in the downset whose maximum global rank is

\[
                         R-q=R-d-1.                                \tag{5.7}
\]

Consequently the number of internal rank-`R` owner windows supplied by
the replacement atoms is exactly zero.

In particular, concatenating the intact atom words cannot be the final
owner chronology: every atom of length at least `q` leaves an internal
under-rank `q`-window which no choice of exterior seam can change.

#### Proof

Equations (5.2)--(5.4) prove the rank criterion.  Bound (5.7) is the
active-downset definition.  An internal window depends only on the
contiguous atom letters, so concatenating another word before or after it
does not change its union.  \(\square\)

The remote census found the following total numbers of internal
`q`-windows, normalized by `W`:

| `k` | `q` | internal atom `q`-windows / `W` | compatible rank-`R` / `W` |
|---:|---:|---:|---:|
| 201 | 10 | 0.1899235960 | 0 |
| 401 | 14 | 0.1953037376 | 0 |

Thus private singleton letters solve the local comparability defect but
not the middle-clock rank defect.  A successful compiler must split or
overlap the length-`q` atoms, interleave them by a new interval identity,
or add a rank-lifting schedule which does not alter any marked lower value.
Simple reordering of intact blocks is ruled out.

## 6. Relation to antidiagonal carrier positions

The rank-`R-d-1` product-SCD diagonals partition the whole Boolean row

\[
                         \binom{[k]}{R-d-1}.                         \tag{5.1}
\]

The lost family is a tiny named subset of that row in the tested census.
Antidiagonal words at base rank `R-d` produce rank-`R` owners in
`d+1`-letter windows, while base rank `R-d-1` would produce rank-`R-1`
windows.  Thus simply dropping the lost row into the previously proved
rank-`R-d` antidiagonal carrier is an off-by-one error.

A valid absorption must do one of the following:

1. use the lost sets as individually marked short cells inside a rank-
   `R-d` source chronology without changing its owner windows;
2. combine each lost set with one private increment inside a rectangle
   owner packet; or
3. charge them as a separately protected terminal row and prove a joint
   chronology compiler.

The census establishes the capacity scale for that final absorption but
does not infer it from unused marginal positions.

## 7. Verification artifact

`analyze_product_scd_fan_rectangle_hybrid_boundary.py` replays the exact
slab recurrence and prints the source, mixed, axial, total-loss, and
singleton-repaired charges, together with the global loss-rank histogram.
Substantial instances were run only on `h100`.
