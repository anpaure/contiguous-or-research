# A resident long return rail for the Boolean-hex square collar

Date: 2026-08-01  
Status: exact local construction.  It closes residence for the collared
cycle sidecar at any prescribed depth `s<=m-2`.  It does not make the
collar transparent to arbitrary-width upper witnesses or to the terminal
common-cap compiler.

## 1. Setup

Work on a `2m`-element ground set.  Let `L` have rank `m-1`, and choose
distinct coordinates

\[
 \alpha,\delta\notin L,
 \qquad b\in L,
 \qquad c\notin U:=L+\alpha+\delta .                 \tag{1.1}
\]

The target ordered diamond is

\[
 e=(L,U,E,F),\qquad E=L+\delta,\quad F=L+\alpha.     \tag{1.2}
\]

Use `(b,c)` in the ternary Boolean-hex packet.  With the notation of the
square-collar theorem, its old and new phases are

\[
 O=\{AB,CD,EF\},\qquad N=\{AF,CB,ED\},              \tag{1.3}
\]

where

\[
 A=U-b,\quad B=L-b+\alpha+c,
 \quad C=L-b+c+\delta,\quad D=L+c.                  \tag{1.4}
\]

Fix `1<=s<=m-2`.  Choose ordered, pairwise-distinct lists

\[
 x_1,\ldots,x_s\in L\setminus\{b\},
 \qquad
 y_1,\ldots,y_s\in \overline U\setminus\{c\}.       \tag{1.5}
\]

Put `X_j={x_1,...,x_j}` and `Y_j={y_1,...,y_j}`.  Define

\[
 P_j=L-X_j+Y_j+\alpha\qquad(0\le j\le s),           \tag{1.6}
\]

so `P_0=F`, and

\[
 Q_0=L-X_s+Y_s+\delta,                               \tag{1.7}
\]

\[
 Q_j=L-\{x_{j+1},\ldots,x_s\}
       +\{y_{j+1},\ldots,y_s\}+\delta
       \qquad(1\le j\le s),                         \tag{1.8}
\]

so `Q_s=E`.  The long return rail is the directed Johnson path

\[
 R_s=P_0P_1\cdots P_sQ_0Q_1\cdots Q_s.              \tag{1.9}
\]

It has `2s+1` edges and `2s+2` vertices.

## 2. Exact resource statement

### Theorem 2.1 (resident square-collar actuator)

The two atom sets

\[
                   G_s^-=O\cup E(R_s),
       \qquad      G_s^+=N\cup E(R_s)               \tag{2.1}
\]

are four-resource matchings with identical complete lower, upper, tail and
head signatures.

The physical graph of `G_s^-` is the disjoint union of

* the directed cycle
  \[
       E,F=P_0,P_1,\ldots,P_s,Q_0,\ldots,Q_s=E,
  \]
  of length `2s+2`; and
* the isolated directed edges `AB` and `CD`.

The physical graph of `G_s^+` is the disjoint union of the two directed
paths

\[
 A,F=P_0,P_1,\ldots,P_s,Q_0,\ldots,Q_s=E,D,
 \qquad C,B.                                         \tag{2.2}
\]

Thus `G_s^- -> G_s^+` removes exactly one cycle, creates no cycle and
changes no immediate typed resource.

There are exactly

\[
                         ((m-2)_s)^2                 \tag{2.3}
\]

ordered rails for one fixed `(e,b,c)`, where `(q)_s` is the falling
factorial.

#### Proof

Every successive pair in (1.9) differs by one swap.  The first `s` edges
swap `x_j` for `y_j`; the central edge swaps `alpha` for `delta`; and the
last `s` edges swap `y_j` back for `x_j` in the **same** order.

The rail vertices are distinct: every `P_j` contains `alpha` and not
`delta`, every `Q_j` contains `delta` and not `alpha`, and each half is a
strict prefix walk in the distinct `x` and `y` lists.  Its lower colours
are

\[
 L-X_j+Y_{j-1}+\alpha\quad(1\le j\le s),             \tag{2.4}
\]

\[
 L-X_s+Y_s,                                          \tag{2.5}
\]

and

\[
 L-\{x_j,\ldots,x_s\}
   +\{y_{j+1},\ldots,y_s\}+\delta
       \quad(1\le j\le s).                          \tag{2.6}
\]

Its upper colours are

\[
 L-X_{j-1}+Y_j+\alpha\quad(1\le j\le s),            \tag{2.7}
\]

\[
 L-X_s+Y_s+\alpha+\delta,                            \tag{2.8}
\]

and

\[
 L-\{x_{j+1},\ldots,x_s\}
   +\{y_j,\ldots,y_s\}+\delta
       \quad(1\le j\le s).                          \tag{2.9}
\]

The prefix indices make the colours within each displayed family distinct.
The occurrence of `alpha`, neither, or `delta` separates (2.4)--(2.6), and
the occurrence of `alpha` only, both, or `delta` only separates
(2.7)--(2.9).

The packet lower palette is

\[
              L-b+\alpha,\quad L-b+c,\quad L,        \tag{2.10}
\]

and its upper palette is

\[
       L-b+\alpha+c+\delta,\quad L+c+\delta,
       \quad U.                                      \tag{2.11}
\]

Because every rail state retains `b` and omits `c`, (2.4)--(2.9) are
disjoint from (2.10)--(2.11).  The same membership patterns separate the
rail vertices from `A,B,C,D`.  Hence both sides of (2.1) are typed
matchings.  The ternary-hex identity gives `res(O)=res(N)`, and the entire
rail is common, so their complete signatures agree.  The component shapes
are read directly from (1.3) and (1.9).  Finally both available ordered
lists in (1.5) have size `m-2`, proving (2.3).  \(\square\)

## 3. Exact residence statement

For a directed cycle, call a coordinate `s`-resident when its positive
trace is all one or every cyclic positive run has length at least `s+1`.
For a directed path, impose the same lower bound only on positive runs
which meet neither path endpoint; endpoint runs are clipped boundary runs.

### Theorem 3.1 (all affected runs are exact)

Every coordinate trace on the cycle component of `G_s^-` is either constant
or has one positive run of length exactly `s+1`.

Every internal positive run on either path component of `G_s^+` has length
at least `s+1`.  More precisely:

* `alpha` occupies `P_0,...,P_s` on the old cycle;
* `delta` occupies `Q_0,...,Q_s`;
* `y_j` occupies
  `P_j,...,P_s,Q_0,...,Q_(j-1)`; and
* the complementary cyclic run of `x_j` is
  `Q_j,...,Q_s,P_0,...,P_(j-1)`.

Each listed run has exactly `s+1` vertices.  On the new long path, the
`y_j` run and the terminal `delta` run remain the only nonboundary affected
positive runs, again of length `s+1`; every split `x_j` run and the
`alpha` run meets an endpoint.  The two-vertex path `CB` has no internal
run.

#### Proof

The four trace descriptions follow immediately from (1.6)--(1.8).  Their
lengths are respectively

\[
 s+1,quad s+1,quad(s-j+1)+j,quad(s-j+1)+j.
\]

Coordinates in `L-{b,x_1,...,x_s}` occur everywhere on the old cycle;
`b` also occurs everywhere because it is never exchanged.  All other
coordinates are absent.  This proves the cyclic statement.

After the phase toggle, `A` precedes `F` and `D` follows `E`.  The split
positive pieces of each `x_j` therefore meet the two path boundaries;
the `alpha` run meets `A`; and the isolated occurrence of `delta` in `A`
is also a boundary run.  The runs of `y_j` and the later run of `delta`
are unchanged internally.  Direct inspection of `CB` finishes the proof.
\(\square\)

### Corollary 3.2 (depth-safe central sidecar)

Taking `s=d(k)` makes both phases legal for the flat depth-`d(k)` residence
test, componentwise, whenever `d(k)<=m-2`.  Since `d(k)=Theta(sqrt(m))`,
this holds in every sufficiently large dimension.

The support has size `2d(k)+6=O(d(k))`; it adds no physical word length if
it replaces an equal-size prepared owner segment.  This is a support-width
statement, not a proof that the prepared segment exists.

## 4. The hidden wreath and the exact upper cut triangle

The long cycle is not merely resident.  It is a literal wreath on its
active coordinates.

Put

\[
 K=L\setminus\{x_1,\ldots,x_s\},
 \qquad
 \pi=(\delta,x_1,\ldots,x_s,\alpha,y_1,\ldots,y_s), \tag{4.1}
\]

read cyclically, and let `n=2s+2`.  Enumerate the main old cycle without
repeating its initial vertex as

\[
 V_0=E, V_1=P_0,ldots,V_{s+1}=P_s,
 V_{s+2}=Q_0,ldots,V_{2s+1}=Q_{s-1}.                \tag{4.2}
\]

### Theorem 4.1 (wreath normal form)

For every `i mod n`,

\[
                  V_i=K\cup\{\pi_i,\pi_{i+1},ldots,
                                  \pi_{i+s}\}.        \tag{4.3}
\]

Consequently the cyclic source word

\[
                         W_i=K\cup\{\pi_i\}          \tag{4.4}
\]

satisfies `D^s W=V` exactly.  Every source position has one private active
coordinate over the common core `K`.

For `0<=q<=s`, every block of `q+1` consecutive owners has union

\[
 \bigcup_{t=0}^{q}V_{i+t}
   =K\cup\{\pi_i,\pi_{i+1},\ldots,\pi_{i+s+q}\}.     \tag{4.5}
\]

For `q>=s+1` the union is the complete active owner
`K union {pi_0,...,pi_(n-1)}`.

#### Proof

At the successive old-cycle transitions the deleted coordinates are

\[
 \delta,x_1,ldots,x_s,\alpha,y_1,ldots,y_s,
\]

while the inserted coordinates are the same list shifted cyclically by
`s+1`.  The initial active set at `E` is
`{delta,x_1,...,x_s}`.  This proves (4.3).  Equations (4.4)--(4.5) are the
union of consecutive singleton letters and the union of overlapping cyclic
windows.  Once the window length reaches `n`, the active set is complete.
\(\square\)

### Corollary 4.2 (exact cut collateral)

The common return path in the plus phase reads

\[
                         V_1,V_2,\ldots,V_{n-1},V_0. \tag{4.6}
\]

Hence every old wreath witness avoiding the cut edge `V_0V_1=EF` survives
literally.  At depth `q`, `1<=q<=s`, exactly `q` cyclic blocks of `q+1`
owners cross that cut.  Their targets are pairwise distinct, both within a
depth and between depths.  The complete local upper collateral before using
the new endpoints `A,D` is therefore the explicit triangle

\[
                             \sum_{q=1}^{s}q
                              ={s(s+1)\over2}.         \tag{4.7}
\]

This is a classification, not a hole count in the global carrier.  A lost
local witness may have another protected occurrence in the bulk, and the
new endpoint ladders through `A` or `D` may recreate part of the triangle.

## 5. Exact remaining boundary

The old and new phases have equal immediate palettes and now have compatible
residence.  Two rows are still not automatic.

1. The two component routings order the same vertices differently.  Their
   interval unions of width at least two need not agree.  A full OR-word
   use needs protected witnesses disjoint from the collar or an exact
   recreated-ladder/cut-transversal proof.
2. Equal outer palettes do not imply that the same occurrence-labelled
   lower assignments survive in one maximal common-cap state.  The cap
   rows must be replayed on the long rail.

Thus the resident rail closes one of the three guards in the collared-cycle
regenerative theorem; it does not by itself prove guarded collar export or
`nu(k)<=B(k)+O(1)`.

## 6. Replay

Run

```text
python3 scratch/audit_boolean_hex_resident_long_square_collar_20260801.py
```

The replay exhausts every ordered `(x,y)` rail for `3<=m<=7` and every
`1<=s<=m-2`.  It checks both typed signatures, all component shapes, formula
(2.3), every cyclic/path residence assertion, the wreath identity (4.3),
all upper unions (4.5), and the triangular cut count (4.7).

## 7. Exact insertion at the two-queue reset seam

The rail has a particularly clean specialization inside the two-queue
reset.  This specialization strengthens the local cyclic statement, but it
also gives a literal counterexample to pointwise boundary transparency.

Put

\[
 n=d+1,\qquad N=2n,
\]

let `C` have rank `m-d-1`, and choose private coordinates
`xi_0,...,xi_(N-1)` disjoint from `C`.  The two-queue owner cycle is

\[
 T_a=C\cup\{\xi_a,\xi_{a+1},\ldots,\xi_{a+d}\},
 \qquad a\in\mathbb Z_N.                              \tag{7.1}
\]

At the seam put

\[
 E=T_0,\qquad F=T_{N-1},\qquad
 L=E\cap F=C\cup\{\xi_0,\ldots,\xi_{d-1}\},          \tag{7.2}
\]

so that `delta=xi_d` and `alpha=xi_(N-1)` in Section 1.  Assume

\[
                              m\ge 2d+1.              \tag{7.3}
\]

Choose distinct `x_1,...,x_d` in `C`, and choose distinct
`y_1,...,y_d` outside the complete reset support

\[
                       C\cup\{\xi_0,\ldots,\xi_{N-1}\}.
                                                               \tag{7.4}
\]

Both choices are possible under (7.3) on the `2m`-point ground.  Use these
lists in `R_d`, and replace the seam `F E` by that rail.  The resulting
cycle, with repeated endpoints suppressed, is

\[
 \mathcal C_d=(T_0,T_1,\ldots,T_{N-1}=P_0,
                P_1,\ldots,P_d,Q_0,\ldots,Q_{d-1}). \tag{7.5}
\]

It has `4d+2` vertices.

### Theorem 7.1 (two-queue long-seam cycle)

The cycle (7.5) is a simple rank-`m` Johnson cycle with pairwise-distinct
lower and upper edge colours.  Every nonconstant coordinate has one cyclic
positive run of length at least `d+1`.  More precisely, its run lengths are

\[
\begin{array}{c|c}
\text{coordinate class}&\text{positive-run length}\\ \hline
C-\{x_1,\ldots,x_d\}&\text{constant}\\
x_j&3d+1\\
y_j&d+1\\
\xi_0,\ldots,\xi_{d-1}&3d+1\\
\xi_d,\xi_{N-1}&2d+1\\
\xi_{d+1},\ldots,\xi_{N-2}&d+1.
\end{array}                                                \tag{7.6}
\]

The reverse orientation of (7.5) has the same owner, lower and upper
palettes and the same cyclic contiguous-union multiset at every width.

#### Proof

The original open reset path is simple and rainbow.  Every lower colour on
that path contains the whole core `C`.  By (2.4)--(2.6), every rail lower
colour omits at least one selected `x_j`; hence the two lower banks are
disjoint.  Every rail upper colour in (2.7)--(2.9) contains at least one
fresh `y_j`, while no reset upper colour does; hence the upper banks are
disjoint.  Every internal rail vertex likewise contains a fresh `y_j` and
omits a selected `x_j`, so it is not an old reset vertex.  Simplicity
inside each bank was proved in Theorem 2.1.

An `x_j` is absent on the `d+1` consecutive rail vertices

\[
                  P_j,\ldots,P_d,Q_0,\ldots,Q_{j-1},
\]

and present everywhere else, giving `3d+1`.  A `y_j` is present on exactly
that same displayed interval, giving `d+1`.  Each
`xi_0,...,xi_(d-1)` had an old run of length `d+1` crossing the replaced
seam and is present on all `2d` new internal rail vertices.  Each of
`xi_d,xi_(N-1)` gains the `d` internal vertices on its corresponding rail
half.  The remaining private-coordinate runs avoid the seam and are
unchanged.  This proves (7.6).

Reversing a cycle does not change its vertices or undirected edges.
Reversal bijects its cyclic intervals, proving the last assertion. \(\square\)

The residence assertion also gives a canonical source-word form.  If
`Z_i` are the vertices of (7.5), put

\[
                         A_i=\bigcap_{t=0}^{d}Z_{i-t}. \tag{7.7}
\]

Erosion followed by dilation reconstructs every cyclic coordinate interval
whose length is at least `d+1`; hence `D^d A=Z`.  Each `A_i` is nonempty,
because the coordinate deleted on the edge leaving `Z_i` ends a run of
length at least `d+1`.  Reversal commutes with (7.7), up to cyclic
reindexing.  Thus the two canonical source words also have identical
cyclic contiguous-OR multisets at every width.

### Proposition 7.2 (occurrence currents and exterior limitation)

Enumerate (7.5) as `Z_0,...,Z_(M-1)`, where `M=4d+2`, and put

\[
 I_i=Z_i\cap Z_{i+1},\qquad U_i=Z_i\cup Z_{i+1}.
\]

Scalar owner, lower and upper currents vanish under full reversal.  The
occurrence-labelled attachment currents do not.  Upper `U_i` is attached
to head `Z_(i+1)` in the forward phase and to head `Z_i` in the reverse
phase; the symmetric difference is one alternating cycle

\[
 Z_0-U_0-Z_1-U_1-\cdots-Z_{M-1}-U_{M-1}-Z_0.        \tag{7.8}
\]

The lower--tail projection has the analogous cycle with the `I_i`.
The predecessor permutations are `sigma` and `sigma^{-1}`.  Their
symmetric difference has two alternating components, because `M` is even
and alternation advances the vertex index by two.

The two phases have exactly the same undirected `M`-cycle and therefore the
same weak-component partition.  Full reversal is not a component-fusion
move.  Selecting both orientations would create one closed doubleton on
every edge and repeat every lower and upper colour.

Finally, cyclic OR equality is not fixed-exterior transparency.  Open both
orientations at `E=T_0`.  Their second prefix unions are

\[
 E\cup T_1=E\cup\{\xi_{d+1}\},\qquad
 E\cup Q_{d-1}=E\cup\{y_d\},                       \tag{7.9}
\]

which are different by (7.4).  Hence the rooted prefix/suffix current is
generally nonzero.  Reversal transports an internal compiler matching to
an isomorphic phasewise matching, but it does not produce one fixed
occurrence-labelled common cap.  A fixed exterior or common cap still
requires cancellation of that prefix/suffix current, reversal invariance,
or a separate joint
Hall/common-minor theorem.

Proposition 7.2 concerns full reversal of the enlarged reset cycle.  It
must not be conflated with the Boolean-hex switch `O -> N` in Theorem 2.1:
that switch changes three undirected edges and can change components, while
full reversal changes none.
