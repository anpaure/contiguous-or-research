# Bender--Knuth isometric cubes: exact carrier theorem and count audit

## 0. Verdict

Let a two-row standard tableau of size `2m` be identified, by binary RSK,
with its balanced middle word.  Retain the commuting odd Bender--Knuth
involutions

\[
 \tau _1,\tau _3,\ldots,\tau _{2m-1}.
\]

The newly observed local statement is true, in a stronger exact form.

* There is an explicit carrier description of every actual Johnson support.
* The twisted pairs have an exact characterization by a binary suffix rule.
* If `K` is the complement of **any** vertex cover of the twist graph at a
  tableau `Q`, then the `K`-subcube through `Q` is a genuine isometric
  coordinate-pair cube.  Every direction has one fixed support throughout
  that subcube, and the supports of distinct directions are disjoint.

The proposed counting explanation is false:

\[
 \#\{(Q,\hbox{ twisted pair at }Q)\}
 \not\le \exp((\log 3+o(1))m).
\]

In fact it is at least `Cat_(m-3)`, and therefore has exponential rate
`log 4`.

Nevertheless the intended large-cube conclusion survives.  All but `o(W)`
tableaux, where `W=binom(2m,m)`, lie in a radius-pure genuine coordinate-pair
subcube of dimension

\[
 (1/8-o(1))m.                                           \tag{0.1}
\]

Consequently, for every `ell=o(m)`, all but `o(W)` middle words lie in such
a cube of dimension at least `ell`.

This is a **local host-cube theorem**, not a cube partition.  The cubes
chosen through different tableaux may overlap.  Nothing here supplies a
vertex-disjoint tiling, a shadow bijection, a shift-compatible SCD, or a
universal OR word.

## 1. Ballot-path form of binary RSK

For a two-row standard tableau `Q`, write

\[
 q_t=U \quad\Longleftrightarrow\quad t\text{ is in the first row of }Q,
 \qquad
 q_t=D \quad\Longleftrightarrow\quad t\text{ is in the second row}. \tag{1.1}
\]

Then `q=q_1...q_(2m)` is a ballot path.  If its final height is `2d`, the
shape of `Q` is `(m+d,m-d)`.

There is a direct inverse-RSK description of the associated balanced binary
word `w(Q)`.  Match `U` and `D` steps by the usual stack rule.  Exactly `2d`
`U` steps remain unmatched.  In the bit convention used here:

* every matched `U` receives bit one;
* every `D` receives bit zero;
* the first `d` unmatched `U` steps receive bit zero and the last `d`
  receive bit one.

This gives exactly `m` ones.  It is the two-letter inverse row-insertion
algorithm: a matched `U,D` pair records the insertion and later reverse bump
of one letter, while the persistent `U` steps read the `2d` unpaired cells
of the first row of the unique semistandard insertion tableau.  Interchanging
the names zero and one only swaps the two halves of the last bullet and does
not change any support below.

Group the path into the odd label pairs

\[
 (q_{2j-1},q_{2j}),\qquad 1\le j\le m.                \tag{1.2}
\]

At every block boundary the path height is even.  Write `y_j` for half the
height after `j` blocks, with `y_0=0` and `y_m=d`.  A block is one of

\[
 UU:+1,\qquad DD:-1,\qquad UD:0,\qquad DU:0           \tag{1.3}
\]

in the `y`-path.

The involution `tau_(2j-1)` is active precisely when block `j` is mixed and
starts at a positive level `h=y_(j-1)>0`; it interchanges `UD` and `DU`.
Indeed, equal-row labels are comparable, and a `UD` block at level zero is
a vertical domino.  Every other mixed block consists of incomparable boxes.

## 2. The carrier support formula

Use the stack matching of Section 1.  At a mixed block at level `h`, call
the stack entry at depth `2h` the **carrier** of that level.

* An `UD` block matches internally and leaves the carrier unchanged.
* A `DU` block matches its odd `D` to the old carrier, then its even `U`
  becomes the new carrier.

Thus a `DU` block performs the carrier update

\[
 e\longmapsto 2j,                                     \tag{2.1}
\]

where `e` and `2j` are even ground coordinates.  The first carrier at a
level is also even: it is the second `U` of the `UU` block that most recently
entered that level.

There are only two circumstances in which this carrier identity can affect
the binary word.

1. The stack slot must survive to the end.  Equivalently, the block lies
   after the last block boundary below level `h`.
2. The persistent slot has rank `2h` among the final `2d` unmatched `U`
   steps, and it must lie in the first half.  Equivalently,

   \[
    2h\le d.                                           \tag{2.2}
   \]

Call the active mixed blocks satisfying these two conditions the **critical
sequence at level `h`**.  There is at most one such sequence for every
`1<=h<=floor(d/2)`.

All active blocks outside the critical sequences have the fixed local
support

\[
 S(Q,2j-1)=\{2j-1,2j\}.                               \tag{2.3}
\]

To describe a critical sequence, list its blocks from left to right as
`p_1<...<p_a`, where every `p_r` is the odd ground coordinate of its block,
and put

\[
 x_r=1\quad\Longleftrightarrow\quad\text{block }r\text{ is }DU. \tag{2.4}
\]

Let `e_0` be the initial carrier, and let

\[
 e_{r-1}=
 \begin{cases}
   p_t+1,&t=\max\{u<r:x_u=1\},\\
   e_0,&\text{if no such }u\text{ exists}.
 \end{cases}                                           \tag{2.5}
\]

### Theorem 1 (exact support formula)

For a generator in a critical sequence,

\[
 S(Q,p_r)=
 \begin{cases}
   \{p_r,p_r+1\},&\text{if some }x_t=1\text{ with }t>r,\\
   \{p_r,e_{r-1}\},&\text{otherwise}.
 \end{cases}                                           \tag{2.6}
\]

In particular every active odd generator has support `{odd,even}`.

### Proof

Compare the `UD` and `DU` versions of block `r`.  If a later `DU` occurs at
the same level, that later block consumes whichever of the two candidate
carriers was left by block `r`.  Both candidates are then matched `U` steps,
so the only changed bits are the two entries of block `r`.

If there is no later `DU`, the carrier left by block `r` persists.  In a
critical sequence it is one of the first `d` unmatched `U` steps.  Changing
`UD` to `DU` changes the odd matched `U` into a `D`, and changes the old
persistent carrier into a matched `U`; the two changed positions are
`p_r,e_(r-1)`.  The reverse change has the same support.  Conditions outside
the critical sequences either make both candidate carriers eventually
matched or put both in the same, second half of the persistent steps, giving
(2.3).  QED.

## 3. Exact twist graph and isometric subcubes

For two active odd generators `p_r,p_s`, call their commuting square
**twisted** at `Q` if an opposite pair of actual Johnson supports differs.
The other opposite pair then differs as well.

### Theorem 2 (twist criterion)

Twists occur only inside one critical sequence.  For `r<s` in that
sequence,

\[
 \{p_r,p_s\}\text{ is twisted}
 \quad\Longleftrightarrow\quad
 x_t=0\quad\text{for every }t>r\text{ with }t\ne s.   \tag{3.1}
\]

### Proof

Formula (2.6) depends on the suffix in exactly two ways: whether a later
`DU` exists, and, when none exists, the identity of the most recent earlier
`DU`.  Toggling block `s` changes the support at `r`, or toggling block `r`
changes the carrier used at `s`, exactly when `s` is the only possible `DU`
strictly after `r`.  This is (3.1).  Different levels use different stack
slots and cannot interact.  QED.

The graph in (3.1) need not be a clique or a disjoint union of cliques.  For
example the orientation string `001` gives a two-edge star on its three
vertices.

### Theorem 3 (vertex-cover isometry)

Let `G_Q` be the twist graph on the active odd generators at `Q`.  If `C` is
any vertex cover of `G_Q` and `K=V(G_Q)\C`, then the full `K`-orbit through
`Q` is a genuine isometric cube in `J(2m,m)`:

1. each generator in `K` has one fixed two-coordinate support throughout
   the orbit;
2. these supports are pairwise disjoint;
3. the orbit has exactly `2^|K|` middle words and remains in the RSK radius
   class of `Q`.

### Proof

It suffices to work in one critical sequence; all other supports are already
the disjoint native pairs (2.3).  Since `C` is a vertex cover, `K` is
independent in (3.1).

Look at the last `DU` whose generator is fixed, meaning it is not in `K`.
Every retained generator before it has a later fixed `DU`, so (2.6) gives
its native local support at every vertex of the `K`-subcube.

After that fixed carrier update, at most one generator can lie in `K`.  To
see this, if there are no retained `DU` blocks, any two retained `UD` blocks
form an edge by (3.1).  If there is one retained `DU`, it forms an edge with
every other retained block in the tail.  If there are at least two, the last
two retained `DU` blocks form an edge.  Each alternative contradicts
independence.

The possible single tail direction uses the fixed even carrier supplied by
the last deleted `DU`, or the fixed initial carrier if there is no such
block.  It is therefore fixed throughout the subcube.  It cannot meet a
retained native pair: a deleted `DU` carrier belongs to its deleted block,
and an initial carrier belongs to an inactive `UU` block.  Carriers at
different levels occupy different stack depths and hence different even
ground coordinates.  Thus all retained supports are disjoint.

The odd involutions commute and remain active throughout their abstract
orbit.  Fixed disjoint supports identify that orbit with the standard
coordinate-pair cube, proving injectivity and isometry.  Bender--Knuth moves
preserve tableau shape, hence radius.  QED.

## 4. The `3^m` incidence estimate is false

For every `m>=4`, construct ballot paths by the following block word:

\[
 UU,\ UD,\ UD,\ E,\ UU,                              \tag{4.1}
\]

where `E` is an arbitrary two-coloured Motzkin excursion of length `m-4`:
its up, down, and two horizontal steps are encoded respectively by
`UU,DD,UD,DU`.

After the first block the absolute block level is one.  The excursion never
drops below that level and returns to it; the final block raises the final
radius to `d=2`.  Therefore level `h=1` is critical.  It contains at least
the two displayed horizontal blocks.  The last two horizontal blocks in its
critical sequence satisfy (3.1), regardless of their orientations, so every
path (4.1) has a twist.

The number of two-coloured Motzkin excursions of length `n` is `Cat_(n+1)`.
Consequently

\[
 \#\{Q:G_Q\ne\varnothing\}\ge \operatorname {Cat}_{m-3}
   =\exp((\log4-o(1))m)=\Theta(W/m).                  \tag{4.2}
\]

The total number of twisted-pair occurrences is at least the same quantity.
Thus its exponential rate cannot be `log 3`.

This does not contradict the earlier `3^m` estimate for tableaux with few
**active** odd generators.  Twist incidence and active-direction deficiency
are different statistics.

## 5. Almost every tableau still has a linear genuine cube

Let `D(Q)` be the number of `DU` blocks in the ballot word of `Q`.  Every
such block is active.  Define a canonical retained set `K(Q)` as follows:

* retain every `DU` generator outside the critical sequences;
* in each critical sequence, retain all its `DU` generators except its last
  one.

The deleted last `DU` is a fixed carrier barrier.  Therefore every retained
direction has the native support

\[
 \{2j-1,2j\}                                           \tag{5.1}
\]

throughout the retained subcube.  There are at most `floor(d/2)` critical
levels, so

\[
 \dim K(Q)\ge D(Q)-\lfloor d/2\rfloor.                \tag{5.2}
\]

We now bound the two ways in which the right side can be small.

### Radius tail

The number of tableaux of radius exactly `d` is

\[
 f^{(m+d,m-d)}=\binom{2m}{m-d}-\binom{2m}{m-d-1}.
\]

Hence, for an integer `a<m`, the tail telescopes:

\[
 \#\{Q:d>a\}=\binom{2m}{m-a-1}.                       \tag{5.3}
\]

Relative to `W=binom(2m,m)`, the elementary product bound gives

\[
 \frac{\binom{2m}{m-a-1}}{W}
 \le \exp\!\left(-\frac{(a+1)^2}{m+a+1}\right).       \tag{5.4}
\]

Take `a=ceil(m^(2/3))`.  The radius exception is `o(W)`.

### `DU` lower tail

Ignore the ballot restriction and independently regard each two-step block
as one of `UU,DD,UD,DU`.  The number of block words with fewer than `m/8`
`DU` blocks is at most

\[
 \sum_{t<m/8}\binom mt3^{m-t}
 \le (m+1)\exp\left(m\left[H(1/8)+\frac78\log3\right]\right), \tag{5.5}
\]

where `H` is binary entropy.  Numerically,

\[
 H(1/8)+\frac78\log3=1.3380559138\ldots
   <\log4=1.3862943611\ldots.                         \tag{5.6}
\]

Since `W=exp((log4-o(1))m)`, (5.5) is `o(W)`.

Outside the two exceptional families, (5.2) yields

\[
 \dim K(Q)\ge \frac m8-\frac12\lceil m^{2/3}\rceil
             =(1/8-o(1))m.                            \tag{5.7}
\]

This proves (0.1).

## 6. Exhaustive checker

The self-contained checker

`scratch/verify_bk_isometric_cubes.py`

enumerates every two-row tableau through its ballot path.  It independently
computes the inverse-RSK binary word, every actual Johnson support, every
commuting-square twist, the predicted graph (3.1), and every state of the
canonical cube from Section 5.

Run:

```text
python3 scratch/verify_bk_isometric_cubes.py 8
```

The audited output is

```text
1 2 0 0
2 6 0 2
3 20 0 18
4 70 4 118
5 252 32 696
6 924 184 3908
7 3432 928 21336
8 12870 4372 114400
```

The columns are `m`, number of tableaux, number of twisted-pair
occurrences, and retained generator-state support checks.  In particular,
the twist counts `4,32,184,928,4372` agree with direct inverse-RSK square
enumeration.

## 7. Adversarial scope audit

1. **The false count is not used.**  The large-cube theorem uses a `DU`
   lower-tail estimate and the RSK radius tail, not a bound on twists.
2. **The theorem is per vertex.**  It constructs a large cube through almost
   every tableau.  It does not choose these cubes disjointly or consistently
   on overlaps.
3. **No shadows are certified.**  Fixed coordinate pairs make local faces
   transparent, but do not make their intersections or unions cover Boolean
   layers globally.
4. **Only the commuting odd generators are covered.**  No assertion is made
   for adjacent or arbitrary Bender--Knuth generators.
5. **Radius purity is not shift compatibility.**  Shape preservation keeps
   each cube inside one RSK radius class; it does not construct the downward
   and upward chain labels required by a shift-compatible SCD.
6. **The bit convention is harmless but explicit.**  Reversing binary
   letters changes which half of the persistent stack is called zero, not
   the support, carrier, twist, or cube statements.

The proved gain is therefore exact but limited: the state-dependent abstract
Bender--Knuth cubes contain linear-dimensional genuine coordinate-pair
subcubes almost everywhere.  Turning those overlapping local cubes into a
near-partition with globally complete typed shadows remains a separate
problem.
