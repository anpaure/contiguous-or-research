# Exact charge 140 for independent binary tube amplification on every split

Date: 2026-09-07. This is a lower bound for a specified local construction
model, not for unrestricted interval-OR words.

## 1. Model and theorem

Let a macro template cover `{0,1}^8` by indexed rectangles `C_j x D_j`.
Each row chooses any nonempty complementary coordinate split of sizes
`r,s`, with `r+s=8`; its two chains are nonempty strict binary chains and
may be nonsaturated. Different rows can use different splits and overlap.

For an integer `m>=1`, blow each macro point `v` on a `d`-coordinate
shore into the cell `mv+[m]^d`, where `[m]={0,...,m-1}`. For each macro
chain `C`, partition its complete tube

\[
T_m(C)=\bigcup_{v\in C}(mv+[m]^d)
\]

into arbitrary strict fine chains. Pair **every** left fine chain with
**every** right fine chain of that macro row. Do this independently for
all macro rows, retaining their full blown-up supports and charging all
occurrences, including overlaps between different rows.

Let `P_m` be the resulting principal charge, the sum of both fine-chain
lengths over all these paired rectangles. Then

\[
\boxed{P_m\ge140m^7.}                               \tag{1}
\]

The fourteen full-chain template displayed in Section 4 attains equality
for every `m`. Thus even optimal independent shore-chain partitions,
arbitrary nonsaturated binary macrochains, and **all nonempty support
splits** cannot improve the local constant 140 in this model. In particular,
unbalanced binary shore splits are not an escape from this bound.

## 2. Exact unit-cube smoothing and staircase antichains

Let `f_d` be the rank-density of Lebesgue measure on `[0,1)^d`: the
pushforward under summing the coordinates. Explicitly,

\[
f_1(x)=\mathbf1_{[0,1)}(x),\qquad
f_d(x)=\frac1{(d-1)!}\sum_{j=0}^d(-1)^j\binom dj(x-j)_+^{d-1}
\quad(d\ge2).
\]

The normalization is

\[
\boxed{\sum_{j\in\mathbb Z}f_d(z-j)=1
\quad\text{for every real }z.}                       \tag{2a}
\]

For `d=1`, the half-open unit intervals partition the line. Inductively,
`f_(d+1)(z)=integral_0^1 f_d(z-u) du`; summing its translates and
integrating (2a) proves the next dimension. The sums have locally finite
support, so the interchange is justified directly.

For a finite integer point set `S`, let `n_j` count its points of total
coordinate sum `j`. Thickening each point by `[0,1)^d` gives disjoint
unit cubes, whose rank-density is

\[
g(z)=\sum_j n_j f_d(z-j)\le\max_j n_j.                \tag{2b}
\]

Every layer counted by `n_j` is an antichain in coordinate order. Thus any
chain partition of `S` has at least `g(z)` chains for every `z`. This
inequality is exact for each integer dilation; it does not require
unimodality or a symmetric-chain decomposition.

Now suppose a binary macrochain has `a` consecutive unit-rank steps. Those
steps change `a` different coordinates. Their `a+1` cells, after a common
translation, have macro ranks `0,1,...,a`. Thickening their integer
`m`-dilates gives the union of the continuous cells `mv+[0,m)^d`.
Each such cell contributes rank-density
`m^(d-1) f_d(z/m-|v|)`: its volume is `m^d` and the rank variable scales
by `m`. The unit-cube and macro-cell density formulas agree pointwise:
for `d=1` this is the exact half-open interval partition; for `d>=2` it
also follows by convolving that identity, or by continuity of the two
density formulas. Therefore, at `z=(d+a)m/2`, (2b) gives

\[
\boxed{\#\text{partition chains}\ge
\lambda(d,a)m^{d-1},\qquad
\lambda(d,a)=\sum_{i=0}^a f_d\left(\frac{d+a}{2}-i\right).} \tag{2c}
\]

If the run starts at macro rank `r_0`, use
`z=mr_0+(d+a)m/2`; this translation changes nothing. For `d=1`, (2c)
is simply the bound one, for both possible run lengths. A run of length
zero means any one cell, so every nonempty chain is covered by the lemma.
The selected layers remain antichains when the other tube cells are added.

Write `a(C)` for the longest run of consecutive unit-rank steps of `C`
and put `L_d(C)=lambda(d,a(C))`. This is the lower bound used below.

### Four-coordinate specialization and direct checks

Write `r=(r_1<...<r_a)` for the ranks of a nonempty binary chain on four
coordinates. These are among the 31 nonempty subsets of `{0,1,2,3,4}`.
Put

\[
l(r)=\begin{cases}
1,&\text{two consecutive rank gaps are both one},\\
23/24,&\text{some rank gap is one, but not the first case},\\
2/3,&\text{otherwise}.
\end{cases}                                         \tag{2}
\]

Every partition of `T_m(C)` requires at least `l(r)m^3` chains. Only
antichains are needed for this assertion: each partition chain meets an
antichain in at most one point.

**One cell.** Every nonempty tube contains `[m]^4`. Its rank-`2m-2` layer
has size

\[
\binom{2m+1}{3}-4\binom{m+1}{3}
=\frac{2m^3+m}{3}\ge\frac23m^3.                     \tag{3}
\]

**A one-coordinate macro step.** Its two cells induce `[2m] x [m]^3`.
At rank `floor((5m-4)/2)`, inclusion--exclusion gives layer size

\[
\frac{23}{24}m^3+
\begin{cases}m/6,&m\text{ even},\\m/24,&m\text{ odd}.
\end{cases}                                         \tag{4}
\]

For verification, the rank polynomial is
`(1+z^m)(1+z+...+z^(m-1))^4`; expanding its coefficient at the displayed
rank gives (4). In particular the layer has at least `(23/24)m^3` points.

**Two consecutive one-coordinate macro steps.** The coordinates changed
are distinct, since macrochains are binary and increasing. After permuting
coordinates and translating fixed coordinates, the three cells are
`[m]^4`, `me_1+[m]^4`, `m(e_1+e_2)+[m]^4`. Their rank polynomial is

\[
(1+z^m+z^{2m})(1+z+\cdots+z^{m-1})^4.
\]

Its rank-`3m-2` layer has size exactly

\[
2\binom{m+1}{3}+\frac{2m^3+m}{3}=m^3.              \tag{5}
\]

The two outer cube-layer contributions are equal by rank reflection.
Equal-rank points are an antichain in the ambient coordinate order, so
adding the other macro cells cannot invalidate any of (3)--(5).
This proves (2) as an exact finite lower bound; no limiting error or
unproved symmetric-chain decomposition of the three-cell region is used.

## 3. Complete all-shore dual and stability

For two rank types `u,v`, let

\[
n_t(u,v)=\#\{(i,j)\in u\times v:i+j=t\}.
\]

Give every binary target weight `1/2` at ranks 3 and 5, weight `6/5`
at rank 4, and zero elsewhere. These weights sum to
`(binom(8,3)+binom(8,5))/2+(6/5)binom(8,4)=140`.

For shore dimensions `r+s=8` and rank types `u subset {0,...,r}`,
`v subset {0,...,s}`, the separating inequality is:

\[
\boxed{\frac12(n_3(u,v)+n_5(u,v))+\frac65n_4(u,v)
\le |u|L_s(v)+|v|L_r(u).}                          \tag{6}
\]

There are 3095 cases up to shore exchange: 765 for `1+7`, 889 for `2+6`,
945 for `3+5`, and 496 for `4+4`. Only `4+4` with both chains full is
tight; every other case has slack at least `2/15`. The following complete
rational certificate checks the full quantifier without external data:

```python
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial

def density(d, x):
    if d == 1:
        return F(0 <= x < 1)
    return sum(F((-1)**j * comb(d, j), factorial(d-1))
               * max(F(0), x-j)**(d-1) for j in range(d+1))

def tube_lower(d, ranks):
    longest = run = 0
    for x, y in zip(ranks, ranks[1:]):
        run = run + 1 if y-x == 1 else 0
        longest = max(longest, run)
    if d == 1:
        return F(1)
    return sum(density(d, F(d+longest, 2)-i)
               for i in range(longest+1))

count = tight = 0
for r in range(1, 5):
    s = 8-r
    left = [u for q in range(1, r+2)
            for u in combinations(range(r+1), q)]
    right = [v for q in range(1, s+2)
             for v in combinations(range(s+1), q)]
    pairs = (combinations_with_replacement(left, 2) if r == s
             else product(left, right))
    for u, v in pairs:
        n = [sum(i+j == t for i in u for j in v) for t in range(9)]
        slack = (len(u)*tube_lower(s, v) + len(v)*tube_lower(r, u)
                 - F(1, 2)*(n[3]+n[5]) - F(6, 5)*n[4])
        if r == s == 4 and u == v == tuple(range(5)):
            assert slack == 0
            tight += 1
        else:
            assert slack >= F(2, 15)
        count += 1
assert count == 3095 and tight == 1
```

For a fine partition of a row on dimensions `r,s`, the two memberships
are `|C|m^r` and `|D|m^s`. By (2c), full Cartesian pairing costs at least

\[
|C|m^r\,L_s(D)m^{s-1}+|D|m^s\,L_r(C)m^{r-1}
=\{|C|L_s(D)+|D|L_r(C)\}m^7.
\]

Sum (6) over the macro cover. Its nonnegative target weights total 140,
so this proves (1) for every nonempty split. The same slack argument now
shows that charge at most `(140+delta)m^7` allows total weight at most
`(15/2)delta` of rows that are not **full balanced 4+4** rows. Exact
equality therefore forces fourteen full balanced rows and minimal fine
partitions. This statement also allows fractional macro weights as a
weighted-ledger bound, without claiming any integral rounding.

## 4. Attainment and exact scope

The already established master template uses these fourteen pairs of
orders; each row's chains are all five prefixes of its two orders:

```
0461 | 5723     0473 | 2651     0674 | 3152     0726 | 1435
1507 | 4263     1605 | 7432     2104 | 6375     2150 | 7463
3206 | 7154     3210 | 4567     3617 | 5204     4302 | 6157
5034 | 6721     5426 | 7301
```

Their 350 prefix-pair occurrences cover all 256 binary targets. Every
rank-3, rank-4 and rank-5 target occurs exactly once. The companion checker
directly enumerates all targets from this displayed finite witness.

A full four-coordinate macrochain has a fine tube partition into exactly
`m^3` chains. For completeness, route chains through its five cells. In a
cell with the same incoming and outgoing axis, use parallel axis lines.
For different incoming/outgoing axes `a,b`, fix the other two local
coordinates and partition the `(a,b)` square into the `m` hooks

\[
(0,j),(1,j),\ldots,(m-1-j,j),
(m-1-j,j+1),\ldots,(m-1-j,m-1),\quad0\le j<m.
\]

These hooks join the incoming face to the outgoing face bijectively.
Use the first axis at both faces of the initial cell and the last axis at
both faces of the final cell. Matching equal remaining local coordinates
between successive cells gives `m^3` global chains, partitioning all five
cells. Their membership is `5m^4`. Each master row thus costs `10m^7`, and
the fourteen rows attain `140m^7`.

The template and face-routing mechanism are reused from master Appendix
A.7 and `CATALAN_THRESHOLD_EIGHT_COVER_AND_TRANSFER_20260906_c58e2.md`;
the lower certificates here are separate from the numerical upper-cost LPs
in `binary_four_tube_pricing_20260907.py` and
`binary_tube_all_split_pricing_20260907.py`.

The theorem does **not** constrain larger alphabets, coordinated fine
covers that discard redundant macro incidences, or global
joining/serialization with a different charge accounting. It is not a
lower bound on unrestricted `nu(k)`, nor a proof that the outer accumulator
construction is optimal. It rules out improving its binary-eight local
template merely by unbalanced support splits, nonsaturated macrochains,
or better independent shore partitions.
