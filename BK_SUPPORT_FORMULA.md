# Exact physical supports in the odd Bender--Knuth cubes

## 1. Outcome

This note resolves the local-isometry question left open in Section 5 of
`TABLEAU_CRYSTAL_AUDIT.md`.

Let a balanced binary word of length `2m` be encoded by its two-row binary
RSK recording tableau `Q`, and retain the commuting moves

\[
             \tau _1,\tau _3,\ldots,\tau _{2m-1}.        \tag{1.1}
\]

For every active odd move there is an exact closed formula for the two word
positions which it changes.  If the move is `tau_i`, one changed position is
always the odd position `i`; the other is an even position `e_i`.  Usually
`e_i=i+1`.  The exceptional case is one explicitly described final excursion
of the recording path.

This formula has three consequences.

1. Two commuting moves form a twisted square exactly under the path criterion
   in Theorem 3 below.  The twist graph is a disjoint union of elementary
   clique-with-leaves graphs, one for each low path level.
2. The nonlocal generators form an explicit vertex cover.  Its mean size over
   all `W=binom(2m,m)` tableaux is `O(sqrt(m))`.
3. Partitioning every critical orientation sequence by its last `DU`
   partitions **every odd-BK orbit** into physical, radius-pure, isometric
   pair-flip cubes.  All but `o(W)` tableaux belong to cells of dimension at
   least

   \[
                         m/8-m^{5/6}.                 \tag{1.2}
   \]

   In particular, for every `ell=o(m)`, all but `o(W)` tableaux belong to an
   isometric Bender--Knuth cell of dimension at least `ell`.

Thus these cubes are not merely overlapping pointwise charts: they give an
exact middle-layer cube partition, with only `o(W)` vertices in small cells.
This still does not prove the required lower/upper shadow bijections.  All
free directions use the one native coordinate matching
`{1,2},{3,4},...`; the deep fixed-pair capacity obstruction therefore still
applies.

## 2. Binary inverse RSK as a ballot-path rule

Use the alphabet `0<1`, and let

\[
 w=w_1\cdots w_{2m},\qquad |w|_1=m.                  \tag{2.1}
\]

Write `U` when a recording label is in the first row of `Q` and `D` when it
is in the second.  Put

\[
 \epsilon_t=\begin{cases}+1,&U,\\-1,&D,\end{cases}
 \qquad H_t=\sum_{a=1}^t\epsilon_a,qquad H_0=0.     \tag{2.2}
\]

The standard-tableau condition says that `H_t>=0`.  If the RSK shape is

\[
                    (m+d,m-d),                       \tag{2.3}
\]

then `H_(2m)=2d`.

Match every `D` with the most recent unmatched `U`, as in the usual
parenthesis matching.  There are `2d` unmatched `U` steps.  Binary inverse
RSK gives the following exact rule.

### Lemma 1 (inverse word rule)

* every `D` position has word letter `0`;
* every matched `U` position has word letter `1`;
* reading the `2d` unmatched `U` positions from left to right, the first `d`
  have letter `0` and the final `d` have letter `1`.

Equivalently, for a `U` step at `t`,

\[
 w_t=0
 \quad\Longleftrightarrow\quad
 \min_{s\ge t}H_s=H_t\ \hbox{ and }\ H_t\le d.       \tag{2.4}
\]

#### Proof

In binary row insertion, an inserted `1` terminates in the first row.  An
inserted `0` either terminates in the first row or bumps a `1` to the second
row.  The bump pairs are exactly the noncrossing `U-D` pairs above.  Thus a
matched `U` records a `1`, and its matched `D` records the `0` which bumps it.

The insertion tableau of shape `(m+d,m-d)` and content `(m,m)` is unique.
Its `m-d` height-two columns are forced to be `0/1`, and its remaining
`2d` first-row cells are `d` zeros followed by `d` ones.  Reverse insertion
therefore assigns `0` to the first `d` unmatched `U` steps and `1` to the
last `d`.  An unmatched `U` is characterized by the path never subsequently
falling below its post-step height.  The unmatched post-step heights are
`1,2,...,2d`, which gives (2.4).  QED.

## 3. The exact support formula

For odd `i`, the move `tau_i` swaps the recording labels `i,i+1` when their
boxes are incomparable.  In path language an active move interchanges

\[
                      UD\longleftrightarrow DU       \tag{3.1}
\]

at positions `i,i+1`, with

\[
              H_{i-1}=H_{i+1}=2h,qquad h\ge1.       \tag{3.2}
\]

The case `UD` at height zero is the comparable vertical domino and is fixed.
Orient the active edge so that its source has `UD` at `i,i+1`; call this the
peak representative.  The heights outside time `i` are the same at the two
ends of the edge.

### Theorem 2 (physical support formula)

For every active odd move `tau_i`,

\[
             w_Q\mathbin\triangle w_{\tau_iQ}=\{i,e_i\},       \tag{3.3}
\]

where `e_i` is even.  More precisely:

\[
 e_i=\begin{cases}
 i+1,
   &2h>d\ \hbox{or}\ \min_{t\ge i+1}H_t<2h,\\[2mm]
 \displaystyle
 \max\{t<i:H_{t-1}=2h-1,\ H_t=2h\},
   &2h\le d\ \hbox{and}\ \min_{t\ge i+1}H_t\ge2h.
 \end{cases}                                                \tag{3.4}
\]

The second line is well-defined and gives `e_i<i`.

#### Proof

At the peak representative, the `U` at `i` is matched immediately by the
`D` at `i+1`; its word letter is therefore `1`.  At the valley representative
position `i` is a `D`, hence has letter `0`.  Thus position `i` always
changes.

At the valley representative, `i+1` is a `U` whose post-step height is
`2h`.  Lemma 1 says that its letter is `1` if the later path falls below
`2h`, or if `2h>d`.  These are exactly the two alternatives in the first
line of (3.4).  The peak representative has a `D`, hence letter `0`, at
`i+1`; in this case `i+1` is the compensating changed position.

It remains to consider

\[
             2h\le d,\qquad \min_{t\ge i+1}H_t\ge2h.           \tag{3.5}
\]

Let `e` be the final up-step into height `2h` before `i`.  The path never
falls below `2h` after `e` in the peak representative, so this `U` is
unmatched.  Its height is at most `d`, hence Lemma 1 gives `w_e=0`.  Replacing
the peak by the valley inserts a dip to `2h-1` at time `i`, matching precisely
this last up-step, so its letter becomes `1`.  Position `i+1` is now an
unmatched `U` at height at most `d` and remains `0`.

No later position changes, because its step and suffix are unchanged.  No
earlier position other than `e` changes: the only new suffix minimum is the
single dip from `2h` to `2h-1`, and `e` is the unique formerly unmatched
up-step into height `2h`.  This proves (3.3)--(3.4).  Finally, every path has
`H_t congruent t (mod 2)`.  Since `H_e=2h`, the position `e` is even.  QED.

Call the move **local** when `e_i=i+1`, and **nonlocal** otherwise.

## 4. Motzkin form and the complete twist classification

Group the recording steps into the odd pairs from (1.1), and put

\[
                         Y_a={H_{2a}\over2},\qquad 0\le a\le m. \tag{4.1}
\]

The pair types `UU,DD,UD,DU` respectively give an up-step, a down-step, and
two colours of horizontal step in a Motzkin meander `Y`.  At every positive
height both horizontal colours are active Bender--Knuth generators.  A
ground-level `UD` is inactive.

Fix a height `h>=1`.  Look only at horizontal blocks at height `h` belonging
to the final `h`-epoch, meaning that after their left boundary the Motzkin
path never again falls below `h`.  List them as

\[
                       a_1<a_2<\cdots<a_s,             \tag{4.2}
\]

and give `a_u` colour

\[
 \eta_u=\begin{cases}0,&UD,\\1,&DU.\end{cases}         \tag{4.3}
\]

Theorem 2 immediately gives:

\[
 \boxed{\ a_u\hbox{ is nonlocal}
 \ \Longleftrightarrow\ h\le d/2\ \hbox{ and }
                 \eta_v=0\text{ for every }v>u.\ }     \tag{4.4}
\]

All horizontal generators outside these final low epochs are local.

For two active odd generators, call their commuting tableau square
**stable** when each pair of opposite edges has the same physical support,
and **twisted** otherwise.

### Theorem 3 (twisted-square criterion)

Let `a_u<a_v` be two active horizontal blocks.  Their square is twisted if
and only if they occur in the same list (4.2), that list has `h<=d/2`, and

\[
                     \eta_t=0\qquad(t>u,\ t\ne v).     \tag{4.5}

All other commuting odd squares are stable.

In a twisted square there are four distinct physical coordinates.  At a
suitable choice of its base vertex they have the order

\[
                         e<i<i+1<j,                    \tag{4.6}

\]

and the four edge supports are

\[
 \{i,i+1\},\quad\{e,j\},\quad\{e,i\},\quad\{i+1,j\}. \tag{4.7}

Thus the support systems are the two alternating matchings of one physical
four-cycle.

#### Proof

Changing the colour of the later block `a_v` can affect the support of the
earlier block only if it toggles the existence of a later `DU` dip at the
same height.  Formula (4.4) shows that this happens exactly when the level is
at most `d/2`, no later boundary falls below it, and every other horizontal
block after `a_u` is `UD`.  This is (4.5).

A change in one pair of opposite supports forces a change in the other pair:
the xor of the four word-edge supports around a commuting square is zero.
Applying (3.4) before and after the two toggles gives (4.6)--(4.7).  If the
two blocks have different heights, lie before the final epoch, or have a
second surviving later `DU`, neither suffix test in (3.4) changes, and the
square is stable.  QED.

## 5. Exact structure of the twist graph

Let `T(Q)` be the graph whose vertices are the active odd generators at `Q`
and whose edges are the twisted squares.  Theorem 3 decomposes `T(Q)` by the
levels `1<=h<=floor(d/2)`.

For one list (4.2), let

\[
                  p_1<\cdots<p_r                    \tag{5.1}
\]

be the positions coloured `DU`.

* If `r=0`, the level graph is the complete graph `K_s`.
* If `r>=1`, put `p=p_r`.  The vertices

  \[
                         \{p,p+1,\ldots,s\}           \tag{5.2}
  \]

  form a clique.  In addition, `p` is joined to every position from
  `p_(r-1)` through `p-1` when `r>=2`, and to every position from `1`
  through `p-1` when `r=1`.  There are no other edges.

This is a clique with extra leaves attached to its first vertex.  In
particular its exact minimum vertex-cover number is

\[
 \kappa_h=\begin{cases}
 \max(0,s-1),&r=0,\\
 s-1,&r\ge1,\ p=1,\\
 \max(1,s-p),&r\ge1,\ p>1.
 \end{cases}                                          \tag{5.3}
\]

For the asymptotic application an even simpler cover is more useful.  Define

\[
 N_h=\{u:\eta_v=0\text{ for every }v>u\}.             \tag{5.4}
\]

Thus `N_h` is the whole list when there is no `DU`, and otherwise it is the
suffix beginning at the last `DU`.  Equations (4.4)--(4.5) show that `N_h`
is both the set of nonlocal generators at this level and a vertex cover of
the level twist graph.  Put

\[
                           N(Q)=\bigcup_h N_h.         \tag{5.5}
\]

Then

\[
                      \tau(T(Q))\le |N(Q)|,           \tag{5.6}
\]

where `tau(G)` denotes the minimum vertex-cover number.

## 6. The local generators give a genuine isometric cube

Let

\[
 L(Q)=\{i:\tau_iQ\ne Q,\ e_i=i+1\}.                  \tag{6.1}
\]

### Theorem 4 (local-cube theorem)

The orbit of `Q` under the generators in `L(Q)` is a physical isometric
pair-flip cube of dimension `|L(Q)|`.  Throughout the entire subcube, the
support of generator `tau_i` is the fixed pair

\[
                             \{i,i+1\}.               \tag{6.2}

\]

The pairs (6.2) are mutually disjoint.

#### Proof

The odd Bender--Knuth moves commute, preserve the Motzkin skeleton `Y`, and
only toggle colours of their own horizontal blocks.  At a low final epoch,
(4.4) says that the local blocks are precisely those strictly before the
last `DU`.  That last `DU` is itself nonlocal, so it is not toggled by the
subgroup generated by `L(Q)`.  It remains a permanent later dip certifying
that every selected earlier block is local.  At high levels and before final
epochs, locality follows from the unchanged skeleton and is likewise
permanent.

Therefore Theorem 2 gives the same support (6.2) at every subcube vertex.
Distinct odd indices give disjoint adjacent pairs.  Toggling any set of the
generators consequently toggles exactly the corresponding disjoint word
pairs, proving both injectivity and isometry.  QED.

This is stronger than merely taking an independent set in `T(Q)`: it gives
an explicit support-constant independent set and proves constancy on every
higher-dimensional face, not only on the base squares.

The local cubes in Theorem 4 have an exact global compatibility which is
worth making explicit.  Fix one odd-BK orbit; equivalently, fix the
uncoloured Motzkin skeleton and the set of active horizontal blocks.  For a
critical sequence of length `s`, partition its orientation cube as

\[
 \begin{aligned}
 R_0&=\{0^s\},\\
 R_p&=\{\eta:\eta_p=1,\ \eta_{p+1}=\cdots=\eta_s=0\}
       \qquad(1\le p\le s).
 \end{aligned}                                         \tag{6.3}
\]

Here the first `p-1` bits of `R_p` are free.  Formula (4.4) says that their
generators are local throughout `R_p`, because the fixed last `DU` at `p`
is a permanent later dip.  The cell `R_0` has no free direction from this
sequence.  Leave every noncritical active direction free and take the
product of (6.3) over the critical levels.

### Corollary 5 (exact orbitwise cube partition)

The cells just defined partition every odd-BK orbit into pairwise disjoint,
radius-pure, physical isometric cubes.  Every free support is one native
pair `{2j-1,2j}`.

#### Proof

Every binary orientation string has either no `DU` or one uniquely defined
last `DU`, so (6.3) is a partition.  The product cells therefore partition
the whole orbit.  Theorem 4 proves isometry; Bender--Knuth moves preserve
tableau shape, hence radius.  QED.

## 7. Average cover size

Condition on the uncoloured Motzkin skeleton `Y`.  Every positive-height
horizontal block may independently be `UD` or `DU`; all `2^s` colourings are
valid and equiprobable.  (At height zero only `UD` is valid, and it is
inactive.)

For a fixed final low-level list of length `s`, a position `u` belongs to
`N_h` precisely when all `s-u` later colours are `UD`.  Hence

\[
 \mathbb E(|N_h|\mid Y)
   =\sum_{u=1}^s2^{-(s-u)}
   =2(1-2^{-s})<2.                                   \tag{7.1}

There are at most `floor(d/2)` relevant levels, so

\[
                      \mathbb E(|N(Q)|\mid Y)\le d.  \tag{7.2}

In the orbitwise partition of Corollary 5, `|N(Q)|` is exactly the
codimension `Delta(Q)` of the cell containing `Q` inside its full abstract
odd-BK orbit: it consists of the last `DU` and the fixed trailing bits in
each critical sequence.  Thus (7.2) is also the exact estimate needed for
the partition, not only for a pointwise vertex cover.

The number of two-row tableaux of radius `d` is

\[
 V_d=\binom{2m}{m-d}-\binom{2m}{m-d-1}.              \tag{7.3}

Summation by parts gives the exact radius moment

\[
 \sum_{d=0}^m dV_d
   =\sum_{d=1}^m\binom{2m}{m-d}
   ={4^m-\binom{2m}m\over2}.                         \tag{7.4}

Combining (5.6), (7.2), and (7.4), with
`W=binom(2m,m)`, proves

\[
 \boxed{
 {1\over W}\sum_Q\tau(T(Q))
 \le {1\over W}\sum_Q|N(Q)|
 \le {4^m-W\over2W}
 =\left({\sqrt{\pi m}\over2}+o(\sqrt m)\right).
 }                                                       \tag{7.5}

In particular, for every function `omega(m)->infinity`, all but `o(W)`
tableaux have a twist-graph vertex cover of size at most
`omega(m)sqrt(m)`; and, more crudely,

\[
 \#\{Q:|N(Q)|>m/40\}=O(W/\sqrt m)=o(W).              \tag{7.6}

## 8. Almost every partition cell has linear dimension

Let `A(Q)` be the number of active odd generators.  It is constant on an
odd-BK orbit.  Let `D(Q)` be the number of `DU` blocks in the recording
path.  Every `DU` block is active (a `DU` at ground level would violate the
ballot condition), so

\[
                              A(Q)\ge D(Q).           \tag{8.1}
\]

Discarding ballot legality only enlarges the family having few `DU` blocks.
Choose their locations and give every other block one of the other three
types.  Therefore

\[
 \#\{Q:D(Q)<m/8\}
 \le\sum_{t<m/8}\binom mt3^{m-t}
 \le(m+1)\exp\{m[H(1/8)+(7/8)\log3]\}.               \tag{8.2}
\]

Numerically,

\[
 H(1/8)+(7/8)\log3=1.3380559138\ldots<\log4,         \tag{8.3}
\]

so (8.2) is `o(W)`.  If an orbit had `A<m/8`, every one of its vertices
would satisfy `D<m/8`; hence the union of all such small-active orbits is
also `o(W)`.

The radius tail is independently negligible.  From (7.3), for every
integer `a<m`,

\[
 \#\{Q:d>a\}=\binom{2m}{m-a-1},                      \tag{8.4}
\]

and the elementary product estimate gives

\[
 {\binom{2m}{m-a-1}\over W}
 \le\exp\left(-{(a+1)^2\over m+a+1}\right).          \tag{8.5}
\]

Take `a=ceil(m^(2/3))`.  Outside `o(W)` vertices, therefore, the whole
containing orbit has

\[
                         A\ge m/8,\qquad d\le m^{2/3}+1. \tag{8.6}
\]

On each such orbit, choose a uniformly random vertex, equivalently its cell
with probability proportional to cell size.  By (7.2) and Markov,

\[
 \Pr\{\Delta>m^{5/6}\mid Y\}
 \le {d\over m^{5/6}}=O(m^{-1/6}).                   \tag{8.7}
\]

Summing (8.7) with orbit-size weights discards only `o(W)` more vertices.
The cell dimension is exactly `A-Delta`.  We have proved:

### Theorem 6 (large-cell middle partition)

The partition of Corollary 5 is an exact partition of all `W` middle words
into radius-pure physical pair-flip cubes, and all but `o(W)` words belong
to cells of dimension at least

\[
                         m/8-m^{5/6}.                 \tag{8.8}
\]

Consequently, for every integer function `ell(m)=o(m)`, all but `o(W)`
tableaux belong to an isometric partition cell of dimension at least
`ell(m)`.

### Audit of the orbitwise upgrade

Four possible quantifier failures were checked explicitly.

1. `R_p` in (6.3) really is a subcube: the prefix bits are free, while the
   last `DU` and every trailing bit are fixed.  Different `p`, including
   `p=0`, are disjoint and exhaustive.
2. Critical sequences use disjoint generator coordinates.  Their Cartesian
   product, together with all noncritical directions, therefore partitions
   an entire odd-BK orbit rather than merely covering it.
3. `D(Q)`, the number of `DU` blocks, is **not** orbit-invariant.  The proof
   does not assume it is.  It uses `D(Q)<=A` to show that every orbit with
   `A<m/8` is contained in the `DU` lower-tail exception; `A` itself is
   invariant.
4. Markov's inequality is applied separately with the uniform measure on
   each remaining orbit and then summed with orbit-size weights.  Hence
   (8.7) bounds a fraction of vertices, not an unweighted fraction of
   orbits.

These checks accept both the exact partition and the bound (8.8).

## 9. Independent finite audit

The checker

`scratch/verify_bk_support_formula.py`

is frozen at SHA-256

```
f0eed41e447d2fcf3379af28b3bc148ad722af0ecb5cdef6dde4d5fc8d7611ee
```

does not use inverse RSK to predict supports.  It enumerates balanced words,
computes their recording paths by row insertion, and checks:

1. formula (3.4) for every active odd edge;
2. criterion (4.5) for every commuting odd square;
3. support constancy (6.2) on every vertex of every local/partition cell.

Exhaustion through `m=9` gives:

```
m=7 tableaux=3432  supports=9504   squares=11400  cube_edges=101960: PASS
m=8 tableaux=12870 supports=42042  squares=60588  cube_edges=644992: PASS
m=9 tableaux=48620 supports=183040 squares=308308 cube_edges=4034540: PASS
```

These computations are an audit, not an input to the proofs.

## 10. What this does and does not solve

The state-dependent-support obstruction in `TABLEAU_CRYSTAL_AUDIT.md` is now
resolved positively at the correct scale: the entire middle layer has an
explicit radius-pure physical cube partition, and almost every vertex lies
in a cell with far more than `ell=o(m)` mutually disjoint,
support-constant directions.  Thus `LINEAR_CYCLE_TILING.md` may be applied
inside the large cells to solve the middle-only block-factor step.

Two genuinely global problems remain.

1. Isometry does not make the depth-`q` lower and upper face labels
   globally injective across different cubes.
2. Every free direction is drawn from the single global adjacent matching
   `{1,2},{3,4},...`.  The fixed-pair residual-capacity theorem shows that
   this unmixed partition cannot reach depths `q` with
   `q/sqrt(m)->infinity`.  Conjugate matchings, controlled nonlocal carrier
   directions, or a typed global re-pairing are still required.

Accordingly, Theorem 6 completes a genuine middle-layer Stage A and removes
one major obstruction, but it is not yet the shadow-resolved SCD or the final
universal-OR construction.
