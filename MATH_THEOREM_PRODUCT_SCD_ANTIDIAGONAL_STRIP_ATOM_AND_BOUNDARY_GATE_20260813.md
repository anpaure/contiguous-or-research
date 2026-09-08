# Product-SCD antidiagonal strips: an exact carrier-compatible atom and its boundary gate

**Date:** 2026-08-13  
**Method:** literal interval-union algebra, followed by an exact weighted
product-SCD census run on `h100`.  
**Status:** unconditional local theorem and unconditional global atlas
reduction.  The most direct boundary completion has coefficient larger than
one, so it is not by itself the desired all-width compiler.  The rank
`R-d` specialization is a literal Johnson owner-path source, but only a
partial one.

## 1. Product-chain notation

Let `X dotcup Y` be a disjoint coordinate split, and let

\[
 C_0\subset C_1\subset\cdots\subset C_{a-1}\subseteq X,
 \qquad
 D_0\subset D_1\subset\cdots\subset D_{b-1}\subseteq Y               \tag{1.1}
\]

be saturated Boolean chains.  Write

\[
 |C_i|=u+i,\qquad |D_j|=v+j.                                        \tag{1.2}
\]

For every allowed index put

\[
 c_i=C_i\setminus C_{i-1},\qquad d_j=D_j\setminus D_{j-1};           \tag{1.3}
\]

these are singleton increments.  The two increment alphabets are disjoint.

## 2. The exact antidiagonal word

Fix an integer `s` and an interval of indices

\[
 I=[p,r]\subseteq\mathbb Z                                           \tag{2.1}
\]

such that

\[
 0\le p\le r<a,qquad 0\le s-r\le s-p<b.                            \tag{2.2}
\]

For literal nonempty-source applications assume also `u+v+s>0`.  The only
excluded set-algebra case is the single rank-zero letter; every deep PBBS
strip below automatically has positive source rank.

For `t in I`, define

\[
                         Z_t=C_t\cup D_{s-t}.                         \tag{2.3}
\]

### Theorem 2.1 (antidiagonal interval-union atom)

In the word

\[
                         Z_p,Z_{p+1},\ldots,Z_r,                      \tag{2.4}
\]

every interval `[x,y] subseteq [p,r]` has value

\[
 \bigcup_{t=x}^{y} Z_t=C_y\cup D_{s-x}.                              \tag{2.5}
\]

It has width `y-x+1` and rank

\[
                         u+v+s+(y-x).                                \tag{2.6}
\]

Distinct index intervals have distinct values.  Consecutive source letters
are incomparable Johnson neighbours.  More precisely,

\[
 Z_{t+1}=(Z_t\setminus d_{s-t})\cup c_{t+1}.                          \tag{2.7}
\]

#### Proof

The `C_t` increase with `t`, while the `D_{s-t}` decrease.  Their two
coordinate alphabets are disjoint.  Hence the largest `C` contribution in
`[x,y]` is `C_y`, and the largest `D` contribution is `D_{s-x}`, proving
(2.5).  Equation (1.2) gives (2.6).  The two endpoint indices are recovered
from the two product-chain coordinates of the value, so no two intervals
have the same value.  Finally, one step gains `c_{t+1}` and loses
`d_{s-t}`, proving (2.7).  \(\square\)

The atom has literal private-letter rigidity: extending an interval one
step left adds exactly one new `D` increment, and extending it one step
right adds exactly one new `C` increment.  In particular, every interval
of width at most `d` is a legal width-`d` lower occurrence with no rank
slack.

## 3. The triangle inside one diagonal strip

For a product grid `[0,a) times [0,b)`, the maximal local-rank-`q`
antidiagonal has index interval

\[
 l_q=\max\{0,q-b+1\},\qquad r_q=\min\{a-1,q\},                        \tag{3.1}
\]

and length

\[
 L_q(a,b)=\max\{0,r_q-l_q+1\}.                                      \tag{3.2}
\]

The corresponding word is

\[
 W_q=(C_t\cup D_{q-t}:l_q\le t\le r_q).                             \tag{3.3}
\]

### Lemma 3.1 (exact covered triangle)

For `1<=tau<=d`, the subintervals of `W_q` of width at most `tau` realize
exactly the cells

\[
 \begin{split}
 T_q(\tau)=\{(i,j):{}&q\le i+j\le q+\tau-1,\\
                    &i\le r_q,\ j\le q-l_q\}.
 \end{split}                                                         \tag{3.4}
\]

Every cell of the full strip block

\[
 B_q(\tau)=\{(i,j)\in[0,a)\times[0,b):
                     q\le i+j\le q+\tau-1\}                         \tag{3.5}
\]

outside `T_q(tau)` lies in at least one of the two boundary wedges

\[
 i\ge q+1,qquad j\ge q+1.                                          \tag{3.6}
\]

#### Proof

By Theorem 2.1, an interval `[x,y]` in `W_q` represents the cell

\[
                         (i,j)=(y,q-x),                               \tag{3.7}
\]

and has width `i+j-q+1`.  The endpoint constraints are exactly the two
coordinate bounds in (3.4).  If the first bound fails then necessarily
`q<a-1` and `i>=q+1`; the second is symmetric.  \(\square\)

Thus one long antidiagonal word simultaneously supplies all sliding
intervals in its triangle.  Charging a separate length-`d` word for every
top cell would be an erroneous factor-`d` overcount.

## 4. A literal boundary-complete strip cover

Let

\[
 \Gamma(A,B)=
 \begin{cases}
 A+B-1,&A,B>0,\\
 0,&\text{otherwise}.
 \end{cases}                                                         \tag{4.1}
\]

The right wedge in (3.6), translated by `(q+1,0)`, is a truncated product
downset of radius at most `tau-2`.  The diagonal-fan atom therefore covers
it with dimensions

\[
 A_R=\min\{\max(a-q-1,0),\tau-1\},\qquad
 B_R=\min\{b,\tau-1\}.                                               \tag{4.2}
\]

The upper wedge is symmetric, with

\[
 A_T=\min\{a,\tau-1\},\qquad
 B_T=\min\{\max(b-q-1,0),\tau-1\}.                                  \tag{4.3}
\]

### Theorem 4.1 (boundary-complete strip)

The central word `W_q` and the two boundary fans cover every cell of
`B_q(tau)` by a distinct assigned interval of width at most `d`.  Their
total charged physical length is

\[
 \kappa_d(a,b;q,\tau)
 =L_q(a,b)+\Gamma(A_R,B_R)+\Gamma(A_T,B_T).                           \tag{4.4}
\]

Overlap between the two fans is harmless: assign an overlapping target to
one fan and leave the other occurrence unmarked.

#### Proof

Lemma 3.1 handles the central triangle.  If `i>=q+1`, put
`i'=i-q-1`.  Every cell of the strip then satisfies

\[
                         i'+j\le\tau-2,                               \tag{4.5}
\]

so the translated right fan covers it.  The upper case is identical.
The central interval widths are at most `tau<=d`; both fans have local
radius at most `tau-2`.  \(\square\)

## 5. Product-SCD global cost

Use the product-SCD notation of
`MATH_THEOREM_PRODUCT_SCD_RECTANGLE_ATLAS_AND_COEFFICIENT_ONE_GATE_20260813.md`.
For a half-chain type pair `(u,v)`, put

\[
 a=\lambda_h(u),\quad b=\lambda_{k-h}(v),\quad
 \ell=d+1-u-v,\quad s=r-d-1-u-v.                                    \tag{5.1}
\]

The active grid is

\[
 \{(i,j):0\le i<a, 0\le j<b, \ell\le i+j\le s\}.                 \tag{5.2}
\]

Set `q_0=max(0,ell)` and, while `q_j=q_0+jd<=s`, set

\[
 \tau_j=\min\{d,s-q_j+1\}.                                          \tag{5.3}
\]

Theorem 4.1 on these consecutive blocks gives the exact grid charge

\[
 \psi_d(a,b;\ell,s)
 =\sum_{j:q_j\le s}
       \kappa_d(a,b;q_j,\tau_j).                                     \tag{5.4}
\]

One may instead start at any

\[
 \max\{0,q_0-d+1\}\le q'_0\le q_0                                 \tag{5.5}
\]

and overcover cells below `ell`; minimizing over these phases is still a
literal atlas.  The tested instances happened to choose `q'_0=q_0`.

If `c_h(u)` denotes the number of chains of type `u`, the global cost is

\[
 R_{\rm ADS}(k,d)
 =\sum_{u,v}c_h(u)c_{k-h}(v)
       \min_{q'_0}\psi_d^{q'_0}
       (\lambda_h(u),\lambda_{k-h}(v);\ell,s).                        \tag{5.6}
\]

This is a theorem, not a marginal packing estimate: the product grids
partition the Boolean targets, the strip blocks partition the active rank
band within each grid, and all atom words are put in disjoint physical
positions.

### Exact remote census

The accompanying verifier evaluated (5.6) with exact integers on `h100`.
`W=binom(k,r)` and `d` is the PBBS deadline parameter.

| `k` | `d` | `R_ADS/W` | central words only / `W` |
|---:|---:|---:|---:|
| 201 | 9  | 1.3411192633 | 0.1852519862 |
| 301 | 11 | 1.4400331185 | 0.1775866430 |
| 401 | 13 | 1.4307390321 | 0.1574334068 |
| 481 | 14 | 1.5147970614 | 0.1648957688 |
| 561 | 15 | 1.5664044411 | 0.1675976265 |
| 641 | 16 | 1.5956645490 | 0.1670127554 |

Therefore this particular per-grid boundary completion does **not** prove
the coefficient-one inequality.  The numerical failure is concentrated in
the separately restarted boundary fans, not in the antidiagonal cores.
This table is not a lower bound against cross-grid boundary stitching or a
different triangular atlas.

## 6. Rank-`R-d` source specialization

Now fix a desired owner rank `R` and put

\[
                         m=R-d.                                      \tag{6.1}
\]

In a product grid of type `(u,v)`, take

\[
                         q=m-u-v.                                    \tag{6.2}
\]

whenever the local rank-`q` diagonal is nonempty.

### Theorem 6.1 (literal central owner path)

Every letter of `W_q` has rank `m`.  Every `d+1` consecutive letters
`Z_x,...,Z_{x+d}` have union

\[
 O_x=C_{x+d}\cup D_{q-x},\qquad |O_x|=R.                             \tag{6.3}
\]

Consecutive owners are Johnson neighbours:

\[
 O_{x+1}=(O_x\setminus d_{q-x})\cup c_{x+d+1}.                        \tag{6.4}
\]

Every shorter window has exact rank `m+w-1`, where `w` is its width.
Within the word, every coordinate has only a prefix run, a suffix run, the
full run, or the empty run; in particular, there is no internally bounded
positive run.

Across all product-SCD grids, the total number of rank-`m` letters in
these maximal words is exactly

\[
 \sum_{u,v}c_h(u)c_{k-h}(v)L_{m-u-v}
                         =\binom{k}{m}.                               \tag{6.5}
\]

The number of literal internal rank-`R` owner windows is exactly

\[
 \sum_{u,v}c_h(u)c_{k-h}(v)
       \max\{L_{m-u-v}-d,0\}.                                        \tag{6.6}
\]

#### Proof

Equations (6.3)--(6.4) are Theorem 2.1 with interval width `d+1`.
The run statement follows from the fact that `C` increments only enter
and `D` increments only leave as `t` increases.  Finally, the product-SCD
grids partition the Boolean lattice, so their local rank-`m-u-v`
diagonals partition the global rank-`m` layer, proving (6.5).  Counting
length-`d+1` windows in each word gives (6.6).  \(\square\)

For the same remote instances, with `R=r`:

| `k` | `d` | `binom(k,R-d)/W` | internal owner windows / `W` |
|---:|---:|---:|---:|
| 201 | 9  | 0.4898224811 | 0.0434606847 |
| 301 | 11 | 0.4823604190 | 0.0424143126 |
| 401 | 13 | 0.4599582088 | 0.0358673306 |
| 481 | 14 | 0.4697373271 | 0.0394880432 |
| 561 | 15 | 0.4734719667 | 0.0411357022 |
| 641 | 16 | 0.4733339753 | 0.0413997383 |

Thus the antidiagonal words are genuinely carrier-compatible, but one copy
of the rank-`R-d` layer cannot be a full rank-`R` owner chronology: even
after perfect stitching it has only `binom(k,R-d)<W` source positions.
The displayed internal windows are smaller still because every separate
product diagonal loses `d` endpoint positions.  Coordinate-conjugate
copies or a joint multi-rank chronology are therefore necessary.

## 7. The exact next gate

The atom removes the earlier semiperimeter obstruction and exposes a much
sharper problem:

> Stitch the endpoint wedges of product diagonals across strong-HC-SCP
> chain blocks so that boundary targets become crossing intervals, while
> preserving the private-letter rank growth and the rank-`R` owner-window
> path.

The Type-1 endpoint cover relations are plausible ports for such a
stitching, but separate endpoint adjacency does not prove the required
multi-letter interval unions.  Until those crossing identities are
written down, the proof-safe conclusion is (5.6), its coefficient-greater-
than-one census, and the partial owner theorem (6.1)--(6.6).

## 8. Verification artifact

`verify_product_scd_antidiagonal_strip_atlas.py` replays the exact weighted
census.  Its `--self-test` option enumerates every strip block for
`a,b<=14` and `d<=8` and checks literal target containment; this test was
run on `h100` and returned

```text
PASS_SMALL_STRIP_COVER
```
