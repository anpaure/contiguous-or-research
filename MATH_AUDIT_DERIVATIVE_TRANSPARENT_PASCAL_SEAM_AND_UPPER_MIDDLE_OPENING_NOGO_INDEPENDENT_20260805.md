# Independent audit: derivative-transparent Pascal seams and the upper-middle opening obstruction

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_DERIVATIVE_TRANSPARENT_PASCAL_SEAM_AND_UPPER_MIDDLE_OPENING_NOGO_20260805.md`  
**Method:** independent pure-mathematical replay; no computation, search, or
solver  
**Verdict:** `GO` after one wording-only distance correction in Lemma 1.1.

## 0. Executive verdict

All substantive claims audit correctly:

* the height-cycle safe-cut criterion and upper-middle no-go;
* the complete derivative-flag identity;
* literal transparency of the one-way derivative seam;
* the upper-rainbow lower/upper middle pair and residence expansion;
* exact enumeration of the full parent rank-`q` layer;
* every depth-by-depth Pascal bank count and nesting relation;
* inheritance of one safe terminal opening from the lower derivative child;
* internal residence and the precise linear-endpoint scope.

The source formerly called `t` the forward distance from `Q_(c-1-t)` to
the cut.  The transition distance is `t+1`; `t` is the number of intervening
roots.  Its inequality `h(c-1-t)<=t` and forbidden-arc formula were already
correct.  The source prose and proof have been repaired accordingly.  No
theorem statement or downstream implication changed.

The result is a genuine recursive advance, not the final construction.  It
removes the impossible demand for a triangularly safe opening of the
upper-middle sector.  It still assumes one lower-middle cycle carrying an
upper-rainbow lift, all supported banks, and one safe cut; it does not supply
that correlated object.

## 1. Height-cycle criterion

A root `i` of height `h(i)` uses exactly

\[
                         Q_i,Q_{i+1},\ldots,Q_{i+h(i)}.
 \tag{1.1}
\]

For the cut between `c-1` and `c`, put `i=c-1-t`.  The flag crosses the cut
exactly when

\[
                         i+h(i)\ge c
 \iff h(i)\ge t+1
 \iff h(i)>t.
 \tag{1.2}
\]

Thus noncrossing is `h(c-1-t)<=t`.  Roots farther than `d-2` places back
cannot cross because `h<=d-1`.  Equivalently, root `i` forbids precisely
the cuts

\[
                         i+1,i+2,\ldots,i+h(i).
 \tag{1.3}
\]

This proves both forms of Lemma 1.1 and shows immediately that the root
preceding a safe cut has height zero.

On a `(2q-1)`-point rank-`q` factor,

\[
 {2q-1\choose q}={2q-1\choose q-1}.
 \tag{1.4}
\]

Surjectivity of the first collar bank therefore forces its size to equal the
entire root count.  Every root has positive height, contradicting the
height-zero predecessor required by (1.2).  Corollary 1.2 is exact; it uses
neither a probabilistic assumption nor a scalar estimate.

## 2. Derivative row and flag identity

With `D_i=Q_i cap Q_(i+1)`, direct reassociation gives

\[
 \begin{aligned}
 I^D_{i,j-1}
 &=\bigcap_{u=0}^{j-1}(Q_{i+u}\cap Q_{i+u+1})\\
 &=\bigcap_{u=0}^{j}Q_{i+u}
 =I^Q_{i,j}.
 \end{aligned}
 \tag{2.1}
\]

No residence assumption is needed for this equality.  If consecutive
`D` values are distinct, both are rank-`q-1` subsets of `Q_(i+1)`, so they
are Johnson adjacent.  The source states this conditional scope correctly.

Consequently one selected derivative occurrence at depth `j-1` supplies
the identical named `Q` occurrence at depth `j`; there is no additional
matching or relabelling step.

## 3. Seam-transparency indexing

Open `Q` between `Q_(-1)` and `Q_0`.  A flag starting at `Q_(-1-t)` and
having height `j>t` uses

\[
                         s=j-t
 \tag{3.1}
\]

lifted derivative owners after the seam, namely

\[
                         z+D_{-1},z+D_0,\ldots,z+D_{s-2}.
 \tag{3.2}
\]

There are exactly `s` terms in (3.2).  Since the earlier `Q` owners omit
`z`, it disappears from the total intersection.  The remaining factors are

\[
 \begin{aligned}
 &\left(\bigcap_{v=-1-t}^{-1}Q_v\right)
 \cap\left(\bigcap_{v=-1}^{s-2}(Q_v\cap Q_{v+1})\right)\\
 &\hspace{30mm}=\bigcap_{v=-1-t}^{s-1}Q_v.
 \end{aligned}
 \tag{3.3}
\]

The old cyclic flag ends at

\[
                         (-1-t)+j=s-1,
 \tag{3.4}
\]

so (3.3) is exactly its old value.  When `j<=t`, the flag never crosses the
seam and nothing changes.  A derivative prefix of `d-1` owners is sufficient:
the worst case is `t=0,j=d-1`, which needs exactly `D_(-1),...,D_(d-3)`.

The asymmetry is real.  A root starting in the lifted sector contains `z`;
crossing into a `z`-free sector deletes it from the intersection.  The
source uses transparency only in the valid direction.

## 4. Upper-rainbow derivative lift

Let `D` be a Hamilton cycle on all rank-`q-1` subsets of a `(2q-1)`-set and
put `Q_i=D_(i-1) union D_i`.  Consecutive `D` sets are adjacent, so every
`Q_i` has rank `q`.  If the `Q_i` are pairwise distinct, their number is

\[
 N={2q-1\choose q-1}={2q-1\choose q},
 \tag{4.1}
\]

and they enumerate the complete upper-middle layer.  Both `Q_i` and
`Q_(i+1)` contain `D_i`; distinct rank-`q` supersets of a rank-`q-1` set
intersect exactly in that set.  Hence

\[
                         Q_i\cap Q_{i+1}=D_i,
 \tag{4.2}
\]

and `Q` is a Hamilton Johnson cycle.

Conversely, in an alternating Middle Levels Hamilton cycle, each intervening
upper vertex is the union of its two adjacent lower vertices.  Reading the
lower shore gives precisely this construction.  Thus the identification of
upper-rainbow factors is exact, and the Middle Levels Theorem supplies this
unlabelled pair only.

Coordinatewise,

\[
                         1_{x\in Q_i}=1_{x\in D_{i-1}\cup D_i}.
 \tag{4.3}
\]

A cyclic positive `D` run of length `ell` becomes a `Q` run of length
`ell+1`; expansions separated by a one-zero gap may merge.  No run becomes
shorter.  Proposition 4.2 therefore correctly upgrades `d`-residence to
`d+1`-residence.

## 5. Full parent-layer enumeration

The path in Theorem 5.1 contains

\[
                         Q_0,Q_1,\ldots,Q_{-1}
 \tag{5.1}
\]

once each, hence every `z`-free rank-`q` subset of `K`.  Its second sector
contains

\[
                         z+D_{-1},z+D_0,\ldots,z+D_{-2}
 \tag{5.2}
\]

once each, hence every `z`-containing rank-`q` subset of `K+z`.  The sectors
are disjoint and

\[
 2N=2{2q-1\choose q}={2q\choose q},
 \tag{5.3}
\]

so this is exactly the full parent layer.

The seam from `Q_(-1)` to `z+D_(-1)` is Johnson because
`D_(-1) subset Q_(-1)` and each set adds one different point to that common
coatom.  Internal adjacency in each sector is already established.  No
unmentioned cyclic closure is asserted.

## 6. Depth-by-depth bank replay

Adopt `R^D_0=Z_N` only as a notational convenience.  From

\[
                         h_Q(i)=\min(d-1,1+h_D(i)),
 \tag{6.1}
\]

the roots selected at depth `j` are

\[
 \begin{array}{c|c|c}
 &Q\text{ sector}&z+D\text{ sector}\\ \hline
 j=1&\mathbb Z_N&R^D_1\\
 2\le j<d&R^D_{j-1}&R^D_j.
 \end{array}
 \tag{6.2}
\]

Their values are

\[
 \begin{array}{c|c|c}
 &Q\text{ sector}&z+D\text{ sector}\\ \hline
 j=1&D_i&z+I^D_{i,1}\\
 2\le j<d&I^D_{i,j-1}&z+I^D_{i,j}.
 \end{array}
 \tag{6.3}
\]

The first row uses (4.2); the later rows use the derivative identity.  The
supported `D` banks make the left values in (6.3) bijective onto

\[
                         {K\choose q-j},
 \tag{6.4}
\]

and the right values bijective onto

\[
                         \{z\}\star {K\choose q-j-1}.
 \tag{6.5}
\]

These are disjoint and Pascal gives

\[
 {K+z\choose q-j}
 ={K\choose q-j}\mathbin{\dot\cup}
  \left(\{z\}\star {K\choose q-j-1}\right).
 \tag{6.6}
\]

Thus every parent target appears exactly once at every declared depth.
Both columns of (6.2) are nested as `j` increases, so the combined banks are
nested.  The cap in (6.1) causes no off-by-one at `j=d-1`:
`h_Q>=d-1` is equivalent to `h_D>=d-2`, exactly `R^D_(d-2)`.

All `Q` flags that cross the sector seam retain their old values by Theorem
3.1.  Lifted `D` flags near the terminal remain wholly inside their sector by
the safe-cut inequalities.  Therefore (6.3) uses actual linear-path future
intersections, not merely cyclic labels.

## 7. Inherited terminal opening

The terminal order of the lifted sector is `D_(-1),D_0,...,D_(-2)`.  Its
terminal cut is the original cyclic cut between `D_(-2)` and `D_(-1)`.
Only the last `d-1` lifted roots could cross it.  For the root `D_(-2-t)`,
the required inequality is

\[
                         h_D(-2-t)\le t,
 \qquad 0\le t\le d-2,
 \tag{7.1}
\]

which is exactly the assumed safe-cut row.  Every `Q` root is separated from
the terminal by all `N` lifted roots, and `N>d-1` under `2<=d<=q-1`.
The inherited terminal opening is therefore safe.

This does not make the parent path cyclically safe at its left boundary; the
module deliberately produces a linear factor with the usual two endpoint
states.

## 8. Residence and endpoint scope

For `x in K`, an unsplit `Q`-sector run has length at least `d+1`, and an
unsplit lifted-`D` run has length at least `d`.

If a cyclic `D` run is split by the chosen cut into terminal and initial
fragments of lengths `v` and `u`, then `x in D_(-1)` and the terminal `Q`
fragment has length `v+1`.  It joins the initial lifted fragment across the
sector seam, giving

\[
                         (v+1)+u\ge d+1.
 \tag{8.1}
\]

If a `D` run begins at `D_(-1)` but does not wrap the cut, its complete
initial fragment already has length at least `d` and joins at least the
single terminal owner `Q_(-1)`.  If `x` is absent from `D_(-1)` but present
in `Q_(-1)`, then it lies in `D_(-2)`; its complete `D` run ends there, has
length at least `d`, and its corresponding `Q` tail is one position longer.

All remaining possibly short pieces are precisely the `Q` fragment clipped
by the global left endpoint and the lifted-`D` fragment clipped by the global
right endpoint.  The new coordinate `z` has one second-sector run of length
`N>=d`.  This proves Proposition 5.2 with exactly its stated linear scope and
does not infer cyclic residence closure.

## 9. Scope and implication

The audited implication is

\[
 \boxed{
 \begin{array}{c}
 \text{one upper-rainbow, resident lower-middle cycle }D\\
 +\ \text{supported banks through depth }d-1\\
 +\ \text{one safe cut}
 \end{array}
 \Longrightarrow
 \begin{array}{c}
 \text{one complete linear parent middle layer}\\
 +\ \text{exact parent nested banks}\\
 +\ \text{one safe terminal opening}.
 \end{array}}
 \tag{9.1}
\]

It does not prove existence of the correlated child `D`, arbitrary-width
upper OR coverage, the residual lower renewal deck, terminal compiler
feasibility, closure of the two endpoint states, or a cyclic parent factor.
No additive-constant conclusion follows yet.  Within those explicit limits,
the source theorem is correct.

