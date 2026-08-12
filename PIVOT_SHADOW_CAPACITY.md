# Capacity audit for the nonlocal-pivot Bender--Knuth partition

## 0. Verdict

The proposed nonlocal-pivot partition is valid and is strictly richer than
the native last-`DU` partition: every critical sequence contributes one
fixed nonlocal free direction.  Nevertheless it still cannot supply the
full growing shadow band by itself.

The obstruction survives for a different reason than the literal
fixed-matching theorem.  A radius-`d` cell has at most `d/2` pivot
directions.  In any cyclic transition word which is geodesic through depth
`H`, one fixed direction occurs at most once in every `H` consecutive
transitions.  Thus a uniformly counted depth-`q` window contains on average
at most

\[
                         qd/(2H)                    \tag{0.1}
\]

pivots.  In the asymptotic construction one needs

\[
 q=c\sqrt m,\qquad
 H=\sqrt m\,g(m),\qquad
 d\le D=\sqrt{m g(m)}=o(H),                         \tag{0.2}
\]

where `g(m)->infinity` sufficiently slowly and `H=o(m)`.

Thus all but `o(W)` windows use `o(q)` pivots.  Relative to the native
matching, one pivot changes the lower full-pair type by at most one.  An
`o(q)` displacement cannot bridge the `Theta(q)` separation between the
typical source-middle type and the typical rank-`m-q` target type.

The main theorem below makes this quantitative: for a sufficiently large
fixed `c`, every `H`-geodesic cyclic factor made from these pivot cells
misses `Omega(W)` lower targets at depth `q=floor(c sqrt(m))`, and likewise
above.  This remains a scoped obstruction.  It does not exclude a reservoir
mixing coordinate-conjugated BK partitions, nor a new dynamics which uses a
positive density of nonnative supports rather than only `O(d)` pivot
directions.

## 1. The pivot cells are genuine isometric cubes

Fix one critical final low-level sequence, with active horizontal blocks

\[
 p_1<\cdots<p_a
\]

and orientation bits `x_j=1` for `DU`, `x_j=0` for `UD`.  Ignore the final
bit temporarily and put

\[
 b=\max\{j<a:x_j=1\},
\]

with `b=0` when the set is empty.  Define

\[
 \begin{aligned}
 S_0&=\{x:x_1=\cdots=x_{a-1}=0\},\\
 S_b&=\{x:x_b=1,\ x_{b+1}=\cdots=x_{a-1}=0\}
          \quad(1\le b<a).
 \end{aligned}                                       \tag{1.1}
\]

In every cell the final bit `x_a` is free.  In `S_b`, `b>0`, the bits before
`b` are also free; in `S_0` there are no other free bits.

### Proposition 1 (nonlocal-pivot cell theorem)

The cells (1.1) partition the orientation cube.  Each is a genuine
fixed-disjoint-support Bender--Knuth cube.  Its free directions are:

* the native prefix directions `u<b`, with supports `{p_u,p_u+1}`; and
* one final nonlocal pivot, with support

  \[
  \{p_a,p_b+1\}\quad(b>0),
  \qquad
  \{p_a,e_h^0\}\quad(b=0),                         \tag{1.2}
  \]

  where `e_h^0` is the fixed initial carrier of the final level epoch.

Taking products over critical levels and leaving all noncritical active
directions free partitions every odd-BK orbit into radius-pure isometric
cubes.  Every cell has exactly one pivot for each nonempty critical sequence;
the number `R` of pivots is orbit-invariant and satisfies

\[
 R\le\lfloor d/2\rfloor                              \tag{1.3}
\]

nonlocal pivot directions.

#### Proof

Every prefix `x_1...x_(a-1)` either has no `1` or has one uniquely defined
last `1`, so (1.1) is disjoint and exhaustive.

If `u<b`, the fixed `DU` at `b` is a permanent later carrier reset.  The
support formula in `BK_SUPPORT_FORMULA.md` therefore fixes direction `u` at
its native pair throughout the cell.  For the final generator there is no
later `DU`.  When `b>0`, the most recent earlier carrier is always the fixed
even coordinate `p_b+1`, regardless of the free prefix.  When `b=0`, every
earlier orientation is fixed `UD`, so the carrier is the fixed initial
coordinate `e_h^0`.  This proves (1.2) and support constancy.

The coordinate `p_b+1` belongs to the fixed, nonfree block `b`; `e_h^0`
belongs to the inactive block entering the level.  Hence the pivot support
is disjoint from every free native prefix pair.  Critical sequences at
different levels use different blocks and stack carriers, so their product
supports remain disjoint.  Odd BK moves preserve tableau shape, proving
radius purity.  There is at most one pivot for each of the at most `d/2`
critical levels, proving (1.3).  QED.

For a sequence of length `a`, the cell dimension is `1` when `b=0` and `b`
when `b>0`.  Its codimension in the full active sequence has expectation

\[
 \sum_{t=1}^{a-1}t2^{-t}+(a-1)2^{1-a}
 =2-2^{2-a}<2.                                      \tag{1.4}
\]

Thus the same orbit-weighted Markov argument as in
`BENDER_KNUTH_SHADOW_BRIDGE.md` shows that all but `o(W)` vertices lie in
pivot cells of dimension `(1/8-o(1))m`.

## 2. Exact native pair-type counts

Use the native matching

\[
 \mathcal P_0=\{\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\}.
\tag{2.1}
\]

For a set `S`, let `F(S)` be the number of pairs in `P_0` wholly contained
in `S`.

The number of middle sets with `F(X)=g` is exactly

\[
 V_g=\frac{m!}{g!^2(m-2g)!},2^{m-2g}.              \tag{2.2}
\]

The number of rank-`m-q` targets with `F(L)=f` is exactly

\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!},2^{m-2f-q}.         \tag{2.3}
\]

Indeed, a middle set has `g` full pairs, `g` empty pairs, and `m-2g`
oriented split pairs.  A lower target has `f` full pairs, `f+q` empty pairs,
and `m-2f-q` oriented split pairs.  Consequently

\[
 \sum_gV_g=\binom{2m}{m}=W,
 \qquad
 \sum_fT_{f,q}=\binom{2m}{m-q}=N_q.                \tag{2.4}
\]

For a uniformly random `k`-set, the mean number of full native pairs is

\[
 \mu_k=\frac{k(k-1)}{2(2m-1)},                     \tag{2.5}
\]

and its variance is

\[
 m p_2(1-p_2)+m(m-1)(p_4-p_2^2),
 \quad
 p_j=\frac{(k)_{\underline j}}{(2m)_{\underline j}}.
\tag{2.6}
\]

Uniformly for `q=O(sqrt(m))`, (2.6) is `(1/16+o(1))m`.  Stirling's formula
applied to (2.2)--(2.3) gives the common local limit

\[
 \begin{aligned}
 \frac{V_{\lfloor\mu_m+x\sqrt m\rfloor}}W
  &=\frac4{\sqrt{2\pi m}}e^{-8x^2}(1+o(1)),\\
 \frac{T_{\lfloor\mu_{m-q}+x\sqrt m\rfloor,q}}{N_q}
  &=\frac4{\sqrt{2\pi m}}e^{-8x^2}(1+o(1))
 \end{aligned}                                      \tag{2.7}
\]

for every fixed bounded `x`.  Finally, if `q=c sqrt(m)` with fixed `c`,

\[
 \frac{\mu_m-\mu_{m-q}}{\sqrt m}\longrightarrow\frac c2,
 \qquad
 \frac{N_q}{W}\longrightarrow e^{-c^2}.            \tag{2.8}
\]

Thus the typical lower target has `c sqrt(m)/2+O(1)` fewer full native
pairs than the typical middle start.

## 3. One pivot moves the type by at most one

Consider a geodesic depth-`q` window beginning at `X`, and let `L` be its
intersection.  Suppose `r` of its `q` transition directions are nonlocal
pivots.

### Lemma 2 (type Lipschitz bound)

\[
             F(L)\le F(X)\le F(L)+r.               \tag{3.1}
\]

#### Proof

The intersection is obtained from `X` by deleting the selected endpoint of
each of the `q` flipped supports.  A native support is one native pair and
`X` contains exactly one member of it, so deleting that member changes a
split pair to an empty pair and does not change `F`.

A pivot support joins coordinates from two different native pairs.  Its
deleted selected endpoint belongs to only one of those native pairs and can
destroy at most one full pair.  Deletion never creates a full pair.  Summing
over the `r` pivots proves (3.1).  QED.

This bound is independent of how the pivot pairs cross the native matching.

## 4. Pivot incidence in an arbitrary `H`-geodesic factor

Let a simple cyclic factor inside one fixed-coordinate cell have transition word
of length `L>=H`.  Assume every `H` consecutive transitions use distinct cube
directions.  Write `R` for the number of pivot directions available in the
cell, and for every cyclic depth-`q` window, `q<=H`, let `r_t` count its
pivot transitions.

### Lemma 3 (pivot-density bound)

The total number `M_piv` of pivot transitions in the cyclic word satisfies

\[
 M_{\rm piv}\le \frac{RL}{H}+R.                     \tag{4.1}
\]

Consequently,

\[
 \frac1L\sum_{t=0}^{L-1}r_t
 \le \frac{qR}{H}+\frac{qR}{L},                    \tag{4.2}
\]

and for every fixed `epsilon>0`, apart from an endpoint term `O(qR/L)`,

\[
 \frac1L\#\{t:r_t>\epsilon q\}
 \le \frac{R}{\epsilon H}+O\!\left(\frac R{\epsilon L}\right).
\tag{4.3}
\]

For a standard `2ell` pair-flip cycle the sharper identity is
`sum_t r_t=2hq`, where `h<=R` is the number of selected pivot directions.

#### Proof

Partition the cyclic transition positions into consecutive arcs of length
`H`, with one final shorter arc.  A fixed direction occurs at most once in
each full arc by `H`-geodesicity, giving (4.1).  Every transition belongs to
exactly `q` cyclic depth-`q` windows, so

\[
 \sum_t r_t=qM_{\rm piv}.
\]

Substitute (4.1) and apply Markov to obtain (4.2)--(4.3).  In the standard
pair-flip cycle every selected direction occurs exactly twice, giving the
stated equality.  QED.

Choose a function `g(m)->infinity` sufficiently slowly that

\[
 H=\sqrt m\,g(m)=o(m),\qquad
 D=\sqrt{m g(m)}=o(H).                              \tag{4.4}
\]

The exact RSK radius tail above `D` is

\[
 O\!\left(e^{-D^2/m+o(1)}W\right)
 =O(e^{-g(m)+o(1)}W)=o(W).                          \tag{4.5}
\]

In every remaining pivot cell, `R<=D/2`.  Summing (4.3) over any
`H`-geodesic cyclic factor shows that, outside `o(W)` starts,

\[
                         r_t\le\epsilon q             \tag{4.6}
\]

at every fixed `q=c sqrt(m)`.  Indeed, the main omitted fraction is at most
`D/(2 epsilon H)=o(1)`.  Since every cycle has length at least `H`, there
are at most `W/H` cycles; the endpoint term in (4.3) contributes only
`O(DW/H)=o(W)`.  Linearization creates at most `O(qW/H)=o(W)` additional
seam-crossing depth-`q` windows.

## 5. The remaining macroscopic capacity obstruction

### Theorem 4 (sparse pivots do not repair the shadow capacity)

There are fixed constants `c,eta>0` such that the following holds.  Let

\[
 q=\lfloor c\sqrt m\rfloor,
\]

and factor the large cells of the nonlocal-pivot BK partition into cyclic
transition words which are geodesic through depth `H` in (4.4).  Permit
arbitrary active directions, orders, cycle lengths at least `H`, and
couplings between cells.  Then the resulting depth-`q` windows miss at least

\[
                         \eta W                         \tag{5.1}
\]

rank-`m-q` targets.  The same conclusion holds at rank `m+q`.

#### Proof

Fix `epsilon=1/32`.  Choose a fixed `C>0` and let `B_q` be the target type
band

\[
 |f-\mu_{m-q}|\le C\sqrt m.                         \tag{5.2}
\]

By (2.7), its size is

\[
 |B_q|=(\beta_C+o(1))N_q                         \tag{5.3}
\]

for a constant `beta_C>0`.

A low-pivot window satisfying (4.6) and landing in (5.2) must, by Lemma 2,
start at a middle set whose type obeys

\[
 g\le \mu_{m-q}+(C+\epsilon c)\sqrt m
   =\mu_m-a_c\sqrt m+o(\sqrt m),                    \tag{5.4}
\]

where

\[
 a_c=c(1/2-\epsilon)-C.                             \tag{5.5}
\]

The number of all middle starts satisfying (5.4), whether or not they occur
in retained cells, is at most

\[
 \left(\Phi(-4a_c)+o(1)\right)W,                   \tag{5.6}
\]

by (2.7), where `Phi` is the standard normal distribution function.

As `c` tends through fixed constants,

\[
 \log\Phi(-4a_c)
 =-8(1/2-\epsilon)^2c^2+O(c),                       \tag{5.7}
\]

while `N_q/W=e^{-c^2+o(1)}`.  Since

\[
 8(1/2-1/32)^2>1,
\]

choose one sufficiently large fixed `c` so that (5.6) is at most
`(beta_C/4)N_q` for all large `m`.

By Section 4, high-pivot starts, high-radius cells, small partition cells,
and seam windows contribute only `o(W)=o(N_q)` further candidates.  Thus
fewer than `(beta_C/3)N_q` physical windows can hit the target band (5.2),
whereas that band contains `(beta_C+o(1))N_q` distinct targets.  At least a
fixed positive fraction of `N_q` is missed.  Since
`N_q=(e^{-c^2}+o(1))W`, this is (5.1).

Complement every mask and reverse the selected/unselected convention to get
the upper statement.  QED.

The theorem is a deterministic capacity obstruction.  Randomness or
independent cube choices are not assumed.

## 6. What the pivots do buy

The negative theorem should not obscure the exact gain.

* The pivot partition is a genuine radius-pure cube partition.
* It inserts one controlled cross-pair direction at every nonempty critical
  level without reducing the asymptotic cell dimension.
* Those cross pairs vary with the tableau carrier and therefore break the
  literal one-fixed-matching model locally.

What fails is their **density in long windows**.  There are only `O(d)`
pivot directions in a cell, and an `H`-geodesic long cycle exposes only an
`O(d/H)=o(1)` transition fraction through them.  A
successful escape must therefore do at least one of the following:

1. mix coordinate-conjugated BK partitions at the block level;
2. construct long locally geodesic cycles with a positive density of
   nonnative directions, rather than one pivot per critical level; or
3. introduce a global re-pairing whose nonlocal shadow effect is not bounded
   by the number of nonnative transitions in the window.

No positive integral or fractional shadow-cover theorem is claimed here.

## 7. Finite checker

The checker

```text
scratch/check_pivot_shadow_capacity.py
```

independently:

* constructs the cells (1.1) in every odd-BK orbit;
* verifies support constancy and disjointness at every cell state;
* verifies that every nonpivot free support is native;
* checks `R<=floor(d/2)`; and
* exhausts all direction subsets through depth three to check (3.1); and
* checks the exact sums (2.4).

Through `m=8` it reports

```text
m  vertices  pivot cells  pivot/vertex incidence
6       924          289                     276
7      3432          834                    1218
8     12870         2427                    5244
```

The finite computation audits the support and counting definitions.  The
asymptotic obstruction is proved by the incidence and local-limit arguments,
not extrapolated from these values.

## 8. Scope audit

1. The theorem allows arbitrary cyclic transition words, but assumes they
   form a vertex-disjoint middle factor, are geodesic through depth `H`, and
   satisfy `D/H->0`.  Standard partial pair-flip cycles are only one special
   case.
2. It permits arbitrary choices, orders, repetitions beyond distance `H`,
   and couplings between cycles; the earlier common-direction-catalog
   obstruction is not used.
3. It counts every high-pivot window as potentially successful.  No
   independence or genericity assumption is hidden in the proof.
4. A pivot changes `F` by at most one because the intersection deletes one
   selected coordinate, not two.  This is the critical Lipschitz constant.
5. Exceptional high-radius vertices, small cells, and all seam windows total
   `o(W)` under (4.4) and the stated low-seam assumption; they cannot repair
   the constant `eta W` deficit.
6. The result does not apply after mixing many coordinate-conjugated
   partitions, because then there is no single native type statistic `F`
   controlling every block.
