# PBBS/GKS flat carriers: the fixed-atlas interval-TU theorem, laminar corridor splices, and the global fragmentation obstruction

Date: 2026-07-28

Status: pure-mathematical theorem note.  The fixed-atlas compiler theorem,
the single-run all-depth compiler, the PBBS corridor and two-corridor
carrier splice, the global laminar/interval obstruction, and the canonical
PBBS cut obstruction are unconditional.  The final PBBS atlas statement is
explicitly conditional.  No `k=15` word and no coefficient-one theorem is
claimed.

## 0. Verdict

Let

\[
 k=2m+1,
 \qquad W=\binom{k}{m},
 \qquad B=\frac{W}{k}=\operatorname {Cat}_m.
 \tag{0.1}
\]

There are two meanings of “interval-TU common `Q_x` compiler,” and they
have opposite answers.

1. **Fixed-atlas meaning.**  Once a resident flat carrier and the actual
   cut-aware flag intervals are fixed, the common compiler is always a
   direct sum of interval-TU coordinate blocks.  In fact no rounding is
   needed: the maximal allowed word is feasible if and only if every
   positive pin is hit and every physical position is allowed for some
   coordinate.
2. **Global consecutive-neighbourhood meaning.**  Requiring every physical
   allowed set `Q_x` itself to be one interval, or requiring the family
   `{Q_x}` to be laminar, is impossible for a complete middle carrier in
   the central regime.  More sharply, if `c_x` is the number of components
   of `Q_x`, then every `N`-vertex Johnson carrier satisfies

   \[
                         \sum_x c_x\ge N-1.
   \tag{0.2}
   \]

   A complete carrier therefore needs aggregate `Q`-fragmentation at least
   `W-1`.

The useful positive theorem is local and compositional.  Every resident
Johnson arc in which each coordinate has one owner run has one common
all-depth compiler whose `Q_x` are physical intervals.  Every canonical
PBBS target corridor is of this type; its `Q_x` are even laminar prefixes,
suffixes, and one spanning core.  Two corridors also splice exactly when
the outgoing bank of the first is the reversed incoming bank of the second
and their cores differ by one Johnson exchange.  This gives a genuine
flat, resident, cross-seam all-depth carrier module.

The corresponding global bypass is exact:

> If the PBBS flag factor can be cut or braided into `R=O(B)` resident
> single-run carrier paths, covering every middle owner once, and if every
> required flag target has one concrete final occurrence internal to one
> of those paths, then concatenating their maximal erosion words has length
> 
> \[
>                         W+dR=W+o(W)
> \]
> 
> for `d=O(sqrt(m))`.

The hypotheses, not the compiler, are the unresolved PBBS content.  They
include exact middle ownership and a cut-aware occurrence cover.  Scalar
connectivity is irrelevant.

Two exact obstructions delimit this positive route.

* The canonical three-root PBBS component contains a five-owner
  `0 1 1 1 0` coordinate pattern, so at every depth `d>=3` that unmodified
  arc has no flat preimage at all.  Its cyclic translates give an odd-cycle
  cut matrix of determinant two.
* The natural parent-first GKS middle-member preorder already fails the
  resident Johnson screen on an embedded `B_4` or `B_5` sector.  Local GKS
  chain laminarity does not repair its chronology.

Thus connectivity and fixed-skeleton integrality are both secondary.  The
live object is a cut-aware PBBS occurrence selection together with a
residence-producing braid.

## 1. Fixed carrier and fixed atlas: the common compiler is already interval-TU

Let

\[
 T=(T_0,\ldots,T_{N-1}),
 \qquad T_i\in\binom{[k]}r,
 \tag{1.1}
\]

be a depth-`d` resident Johnson path, with `r>d`.  Its maximal erosion
controller is

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,N-1)}T_i,
 \qquad 0\le p<N+d.
 \tag{1.2}
\]

The usual one-sided boundary ranks are understood.  Let

\[
                         \Pi=\{(I_\alpha,S_\alpha)\}_\alpha
 \tag{1.3}
\]

be a fixed cut-aware family of exact interval pins.  It may contain lower,
upper, protected, seam, endpoint, or fallback pins.  The central pins
`([i,i+d],T_i)` are already encoded by (1.2).  Define the maximal allowed
positions of coordinate `x` by

\[
 Q_x={p:x\in P_p\}\setminus
      \bigcup_{\alpha:x\notin S_\alpha}I_\alpha.
 \tag{1.4}
\]

### Theorem 1.1 (fixed-atlas maximal-`Q` criterion)

There is a common nonzero word

\[
                         A=(A_0,\ldots,A_{N+d-1})
 \tag{1.5}
\]

such that `D^d A=T` and

\[
                         \bigcup_{p\in I_\alpha}A_p=S_\alpha
 \tag{1.6}
\]

for every pin if and only if

\[
 I_\alpha\cap Q_x\ne\varnothing
 \qquad(\alpha,\ x\in S_\alpha)
 \tag{1.7}
\]

and

\[
                         \bigcup_{x=1}^{k}Q_x=[0,N+d-1].
 \tag{1.8}
\]

When these conditions hold, the coordinatewise maximal word

\[
                         \widehat A_p=\{x:p\in Q_x\}
 \tag{1.9}
\]

realizes all pins simultaneously.

#### Proof

Every central equality forces `A_p subseteq P_p`.  If `x` is absent from a
pin label `S_alpha`, it must be absent throughout `I_alpha`; hence every
realizing support of `x` is contained in (1.4).  A positive coordinate in
`S_alpha` must occur at least once in that interval, giving (1.7), and a
nonzero physical letter gives (1.8).

Conversely, (1.9) contains no coordinate forbidden by a central or extra
pin.  Condition (1.7) supplies every positive coordinate of every extra
pin, while the central positive-hit conditions are exactly the
erosion-controller endpoint/gap conditions and hold because (1.2) is the
maximal erosion of the resident path.  Condition (1.8) makes every letter
nonempty.  Thus all central and extra equalities hold.  \(\square\)

### Theorem 1.2 (coordinatewise interval-TU)

For a fixed `T` and fixed `Pi`, the binary positive-hit system is a direct
sum of totally unimodular interval matrices.

#### Proof

Fix `x` and order the variables

\[
                         z_{p,x}\qquad(p\in Q_x)
\]

by increasing physical position.  The row for a positive pin
`(I_alpha,S_alpha)`, `x in S_alpha`, has support

\[
                         I_\alpha\cap Q_x.
 \tag{1.10}
\]

This is consecutive in the induced order on `Q_x`, even when `Q_x` has
several physical components: if two allowed positions lie in the line
interval `I_alpha`, every allowed position between them also lies in it.
Therefore the coordinate block has the consecutive-ones property and is
totally unimodular.  Different coordinates have disjoint variable sets, so
their direct sum is TU.

The nonzero-position requirement need not be appended as a coupling row:
after taking every allowed variable, it is exactly the deterministic cover
test (1.8).  \(\square\)

Theorem 1.2 is the sharp scope of the positive TU statement.  Rank caps,
trace-two owner caps, target-to-cell injections, or simultaneous chronology
selection couple different coordinate blocks and need not preserve TU.
In particular, making the fixed compiler TU does not repair the frozen
Hall-29 carrier: it leaves unchanged the choice of carrier, occurrence
atlas, and eligible physical cells.

## 2. Single-run resident paths have one common all-depth interval compiler

For `0<=a<=b<N` with `b-a<=d`, put

\[
 L_{a,b}=\bigcap_{i=a}^{b}T_i,
 \qquad
 U_{a,b}=\bigcup_{i=a}^{b}T_i.
 \tag{2.1}
\]

Use the fixed physical frames

\[
 J_a^0=[a,a+d],
 \qquad
 J^-_{a,b}=[b,a+d],
 \qquad
 J^+_{a,b}=[a,b+d].
 \tag{2.2}
\]

Call `T` **single-run** if, for every coordinate `x`, the owner support

\[
                         R_x=\{i:x\in T_i\}
 \tag{2.3}
\]

is empty or one integer interval.

### Theorem 2.1 (single-run all-depth interval-`Q` compiler)

If `T` is resident and single-run, then its maximal erosion word `P` in
(1.2) is nonzero and simultaneously realizes

\[
 \bigcup_{p\in J_a^0}P_p=T_a,
 \qquad
 \bigcup_{p\in J^-_{a,b}}P_p=L_{a,b},
 \qquad
 \bigcup_{p\in J^+_{a,b}}P_p=U_{a,b}
 \tag{2.4}
\]

for every displayed `a,b`.  For the pin system consisting of all these
rows,

\[
                         Q_x=\{p:x\in P_p\}.
 \tag{2.5}
\]

Every nonempty `Q_x` is one physical interval.  Hence the common
coordinate-position matrix has the consecutive-ones property in the
single physical order and is TU.

#### Proof

Coordinatewise erosion--dilation of a positive run of length at least
`d+1` gives

\[
                         \bigcup_{p=i}^{i+d}P_p=T_i.
 \tag{2.6}
\]

For a coordinate with owner run `[u,v]`, its controller support is

\[
 \{p:x\in P_p\}=
 \begin{cases}
 [0,N+d-1],&u=0, v=N-1,\\
 [0,v],&u=0, v<N-1,\\
 [u+d,N+d-1],&u>0, v=N-1,\\
 [u+d,v],&0<u\le v<N-1.
 \end{cases}
 \tag{2.7}
\]

The last interval is nonempty by residence.  Since `r>d`, every controller
state has the positive flat/boundary rank prescribed by erosion--Johnson
duality, so `P_p` is nonempty.

Now `x` belongs to every owner in `[a,b]` if and only if the interval in
(2.7) meets `[b,a+d]`; equivalently, every central window
`[i,i+d]`, `a<=i<=b`, is hit by the same eroded run.  This proves the lower
identity.  Likewise `x` belongs to at least one owner in `[a,b]` if and
only if its eroded run meets the union

\[
                         \bigcup_{i=a}^{b}[i,i+d]=[a,b+d],
\]

which proves the upper identity.

Central negative pins alone restrict the allowed set of `x` to exactly
(2.7).  None of the natural flag pins shrinks it: if `x` is absent from a
lower or upper label, the corresponding interval in (2.2) is already
disjoint from (2.7), by the just-proved exact equality.  Hence (2.5)
holds.  Formula (2.7) proves the interval and TU assertions.  \(\square\)

The theorem is stronger than a rankwise Hall statement.  It installs both
shores, every depth through `d`, and all central owners in one maximal
word.  It also shows exactly what a PBBS braid would gain by producing a
single-run carrier: the common compiler becomes automatic.

## 3. Exact PBBS corridor module

Fix `1<=q<=m-1` and a target

\[
                         K\in\binom{[2m+1]}{m-q}.
 \tag{3.1}
\]

The audited PBBS global-maximum corridor gives one directed `q`-edge path.
After reversing and renaming its pairwise distinct marks if necessary, its
rank-`m` states are

\[
 X_t=K\cup\{a_t,\ldots,a_{q-1}\}
       \cup\{c_{q-t},\ldots,c_{q-1}\},
 \qquad0\le t\le q.
 \tag{3.2}
\]

An index range with lower endpoint larger than its upper endpoint is empty.
Cut the two PBBS adjacencies external to this path and define the sparse
word on positions `0,...,2q` by

\[
 V_p=
 \begin{cases}
 K\cup\{a_p\},&0\le p<q,\\
 K,&p=q,\\
 K\cup\{c_{2q-p}\},&q<p\le2q.
 \end{cases}
 \tag{3.3}
\]

### Theorem 3.1 (laminar PBBS corridor compiler)

The cut corridor is a depth-`q` resident flat carrier and

\[
                         D^qV=(X_0,\ldots,X_q).
 \tag{3.4}
\]

For every `0<=a<=b<=q`,

\[
 \begin{aligned}
 L_{a,b}
 &=K\cup\{a_b,\ldots,a_{q-1}\}
      \cup\{c_{q-a},\ldots,c_{q-1}\},\\
 U_{a,b}
 &=K\cup\{a_a,\ldots,a_{q-1}\}
      \cup\{c_{q-b},\ldots,c_{q-1}\},
 \end{aligned}
 \tag{3.5}
\]

and the same word realizes them on

\[
 J^-_{a,b}=[b,q+a],
 \qquad J_a^0=[a,a+q],
 \qquad J^+_{a,b}=[a,q+b].
 \tag{3.6}
\]

For the complete two-sided pin tower, the exact maximal allowed sets are

\[
 \boxed{
 \begin{aligned}
 Q_x&=[0,2q]&& (x\in K),\\
 Q_{a_j}&=[0,j]&& (0\le j<q),\\
 Q_{c_j}&=[2q-j,2q]&& (0\le j<q),\\
 Q_x&=\varnothing&&\text{for all other coordinates.}
 \end{aligned}}
 \tag{3.7}
\]

The nonempty sets in (3.7) are laminar.  Their incidence matrix is TU, and
both the sparse word `V` and the maximal word

\[
                         \widehat V_p=\{x:p\in Q_x\}
 \tag{3.8}
\]

realize the whole tower.

#### Proof

The window `[t,t+q]` in (3.3) contains precisely the `a`-marks with index
at least `t`, the `c`-marks with index at least `q-t`, and `K`, proving
(3.4).  Intersecting or uniting (3.2) gives (3.5), and a direct inspection
of (3.3) gives (3.6).

Every `a_j` owner run is the left-boundary interval `[0,j]`; every `c_j`
owner run is the right-boundary interval `[q-j,q]`; every core coordinate
spans the packet.  There are no internal variable-coordinate runs, so the
path is resident at depth `q`.

Theorem 2.1 already gives (3.7).  Directly, every negative pin for `a_j`
begins after physical position `j`, and the negative upper pin rooted at
`[j+1,q]` excludes it from all of `[j+1,2q]`.  Dually, the negative upper
pin rooted at `[0,q-j-1]` excludes `c_j` from
`[0,2q-j-1]`.  Thus the allowed sets are exactly those displayed.

The left prefixes are nested, the right suffixes are nested, the two banks
are disjoint, and the core interval contains them all.  This is laminarity.
The common-pin conclusion follows from Theorem 1.1.  \(\square\)

Every selected source interval in (3.6) lies inside the opened PBBS path,
so both external cuts preserve it as an old occurrence; no seam-created
flag is being credited.  Since the PBBS all-depth theorem supplies (3.2)
for every `K` and every `q<=m-1`, every lower target has a **targetwise**
resident laminar compiler carrying its complete paired local tower.  This
does not assert that all these packets can be chosen simultaneously with
low overlap.

## 4. A two-corridor resident splice

The corridor module has one exact nontrivial composition interface.  Work
at arbitrary rank `r`.  Take two depth-`q` corridors.  Write their cores as

\[
 K^+=K^-\setminus\{u\}\cup\{v\},
 \tag{4.1}
\]

and let `L=(ell_0,...,ell_(q-1))`, `C=(c_0,...,c_(q-1))`, and
`R=(r_0,...,r_(q-1))` be disjoint banks, also disjoint from the private core
letters.  The first corridor has incoming bank `L` and outgoing bank `C`.
Give the second corridor incoming order

\[
                         a'_h=c_{q-1-h}
 \qquad(0\le h<q)
 \tag{4.2}
\]

and outgoing bank `R`.  Concatenate all `q+1` owners of the first packet
and all `q+1` owners of the second, without identifying the endpoint.

### Theorem 4.1 (reverse-bank/core-swap splice)

The seam

\[
                         K^-\cup C\longrightarrow K^+\cup C
 \tag{4.3}
\]

is a Johnson edge.  The combined `2q+2`-owner path is depth-`q` resident
and single-run.  Its maximal erosion word has `3q+2` positions and realizes
every lower and upper window of depth at most `q`, including windows crossing
the seam.

On physical positions `0,...,3q+1`, its nonempty allowed sets are

\[
 \begin{array}{c|c}
 \text{coordinate type}&Q_x\\ \hline
 \ell_j &[0,j]\\
 u &[0,q]\\
 c_j &\{2q-j\}\\
 v &[2q+1,3q+1]\\
 r_j &[3q+1-j,3q+1]\\
 x\in K^-\cap K^+ &[0,3q+1].
 \end{array}
 \tag{4.4}
\]

They form a laminar family.

#### Proof

The endpoint states in (4.3) differ only by `u -> v`.  A bank coordinate
`c_j` appears in the first packet from owner `q-j` to owner `q`; by (4.2)
it persists in the second packet through its local owner `q-1-j`.  Its
combined owner run is therefore

\[
                         [q-j,2q-j],
 \tag{4.5}
\]

of exact length `q+1`.  The coordinate `u` has the left-boundary run
`[0,q]`, `v` has the right-boundary run `[q+1,2q+1]`, the `L` and `R`
banks have boundary runs, and the common core spans the path.  Thus every
coordinate has one run and every internal run has length `q+1`.

Theorem 2.1 gives the all-depth word.  Eroding the runs just listed gives
(4.4): in particular (4.5) erodes to the singleton `2q-j`.  The left and
right banks nest under the two private-core intervals, the interface
singletons are pairwise disjoint and lie between them, and the common core
contains everything.  Hence the family is laminar.  \(\square\)

This theorem is an exact Johnson-carrier splice.  To use it as a literal
PBBS factor trade one must still prove that the two canonical packets occur
with interface (4.1)--(4.2), that the projected seam lifts without
duplicating an odd-graph middle owner, and that many such splices are
owner-disjoint.  Those are not consequences of the displayed label
algebra.

The reverse-bank condition is not cosmetic.  If two corridors with
disjoint noncore banks are merely butt-concatenated, `c_0` of the first
packet occurs only in its final owner and in neither neighbouring owner.
It becomes an internal positive run of length one, so no depth-`q` flat
preimage exists for `q>=1`.

## 5. Global laminarity and low fragmentation are impossible

Let a common pin system include all central pins of a flat carrier, and let
`Q_x` be its maximal allowed sets.  Then

\[
 T_i=\{x:[i,i+d]\cap Q_x\ne\varnothing\}.
 \tag{5.1}
\]

### Theorem 5.1 (global laminar-`Q` no-go)

Suppose `T` contains every rank-`r` subset of `[k]`, where
`1<=r<=k-1`.  If the nonempty family `{Q_x}` is laminar, then

\[
                         r\le d+1.
 \tag{5.2}
\]

Consequently no complete central PBBS or `k=15` carrier has laminar
`Q_x` in the relevant regime `r>d+1`.

#### Proof

If `Q_x subseteq Q_y`, then (5.1) implies that every middle owner containing
`x` also contains `y`.  But the complete rank-`r` layer contains a set with
`x` and without `y`.  Thus no two distinct nonempty allowed sets are nested
or equal.  Laminarity forces them to be pairwise disjoint.

The maximal letter at one physical position then contains at most one
coordinate.  A central interval has only `d+1` positions, so its union has
rank at most `d+1`.  Since its rank is `r`, (5.2) follows.  \(\square\)

### Theorem 5.2 (fragmentation lower bound)

Let `T_0,...,T_(N-1)` be a path of distinct rank-`r` sets with consecutive
states Johnson-adjacent.  Let `c_x` be the number of interval components of
`Q_x`.  Then

\[
                         \boxed{\sum_{x=1}^{k}c_x\ge N-1.}
 \tag{5.3}
\]

For a cyclic Johnson carrier the corresponding cyclic-component bound is
`sum_x c_x>=N`.

#### Proof

Dilating one component of `Q_x` by the length-`d+1` central windows gives
one interval of owner indices.  Different dilated components may merge but
cannot split.  Hence the binary owner-incidence word of coordinate `x` has
at most `c_x` positive components and therefore at most `2c_x` membership
toggles.

Every Johnson transition toggles exactly two coordinates.  The path has
`2(N-1)` toggles in total, so

\[
                         2(N-1)\le2\sum_xc_x.
\]

On a cycle, every positive component has two cyclic boundary toggles and
there are `2N` toggles.  \(\square\)

### Corollary 5.3 (one-interval charts have Catalan scale)

If every nonempty `Q_x` is one physical interval, then

\[
                         N\le k-r+1.
 \tag{5.4}
\]

Consequently an atlas of such charts covering all `W` middle owners needs
at least

\[
                         \left\lceil\frac{W}{k-r+1}\right\rceil
 \tag{5.5}
\]

charts.

#### Proof

By (5.1), each coordinate also has one owner run.  At every Johnson
transition the inserted coordinate was absent at time zero; otherwise it
would be re-entering after an earlier run.  Distinct transitions insert
distinct coordinates.  Only `k-r` coordinates are absent from `T_0`, so
`N-1<=k-r`.  Summing chart capacities proves (5.5).  \(\square\)

At the middle levels, (5.5) is `Theta(B)`.  Thus a Catalan number of
interval-`Q` charts is order-necessary but asymptotically affordable:
their depth-`d` collar cost is `Theta(dB)=o(W)` for `d=o(m)`.  The no-go is
against one global laminar or low-fragmentation carrier, not against a
Catalan-scale cut atlas.

## 6. Canonical PBBS counterexample and its non-TU cut matrix

The canonical three-root PBBS component contains, after relabelling, the
six consecutive rank-`m+1` owners

\[
 \begin{aligned}
 X_0&=K\cup0124,&X_1&=K\cup014z,&X_2&=K\cup034z,\\
 X_3&=K\cup234z,&X_4&=K\cup123z,&X_5&=K\cup125z,
 \end{aligned}
 \tag{6.1}
\]

where `z=2m` and `K={6,8,...,2m-2}`.

### Proposition 6.1 (flat and laminar failures in the PBBS motif)

1. For every `d>=3`, the subpath `X_1,...,X_5` has no depth-`d` flat
   preimage, even with arbitrary bundled letters and arbitrary extra pins.
2. At `d=1`, the resident subpath `X_0,...,X_3` has crossing allowed sets
   `Q_0,Q_z`; moreover `Q_2` is disconnected.
3. At `d=2`, the resident subpath `X_0,...,X_4` has crossing allowed sets
   `Q_4,Q_z`; moreover `Q_1` is disconnected on `X_1,...,X_4`.

#### Proof

On `X_1,...,X_5`, coordinate `3` has owner pattern

\[
                         0,1,1,1,0.
 \tag{6.2}
\]

For `d>=3`, the positive central interval at the first `1` is covered by
the two central intervals at the flanking zeros.  Those negative pins delete
every allowed position for `3` in the positive interval, violating (1.7).
This proves item 1.

For `d=1`, coordinate `2` has pattern `1,0,0,1`, so its two required
central hits lie on opposite sides of the forbidden middle intervals;
`Q_2` is disconnected.  Coordinate `z` is absent from `X_0`, so its first
positive window forces position `2`; coordinate `0` is absent from `X_3`,
so its last positive window also forces position `2`.  The positive window
at `X_0` contains a `Q_0` point forbidden to `z`, and the one at `X_3`
contains a `Q_z` point forbidden to `0`.  Thus the two allowed sets cross.

For `d=2`, coordinate `4` has the left-boundary owner run `X_0,...,X_3`,
so its maximal allowed interval is `[0,3]`; coordinate `z` has the
right-boundary run `X_1,...,X_4`, so its interval is `[3,6]`.  They cross
at position `3`.  Coordinate `1` has pattern `1,0,0,1` on
`X_1,...,X_4`, giving the disconnected-set assertion.

All positive runs in the displayed `d=1,2` subpaths either have the
required length or meet a boundary, so those failures are genuinely about
laminarity/one-interval structure rather than hidden nonresidence.
\(\square\)

The motif repeats in one physical PBBS component of length
`3N`, `N=2m+1`.  Let `e_t` denote its projected transition at position `t`
and put

\[
                         B_j=\{e_{3j+1},e_{3j+2},e_{3j+3},e_{3j+4}\},
 \qquad j\in\mathbb Z_N.
 \tag{6.3}
\]

Each intact `B_j` carries a translate of (6.2).  Consecutive sets share
exactly one transition and nonconsecutive sets are disjoint:

\[
 B_j\cap B_{j+1}=\{c_j\},
 \qquad c_j=e_{3j+4}.
 \tag{6.4}
\]

### Proposition 6.2 (exact PBBS cut obstruction)

Every cut-only or piece-reversal linearization into depth-`d` resident
pieces, `d>=3`, must delete at least

\[
                         \left\lceil\frac N2\right\rceil=m+1
 \tag{6.5}
\]

of the canonical transitions in this component merely to hit the
witnesses (6.3).  This bound is exact for that witness cover.  Moreover the
witness-versus-shared-cut submatrix is

\[
                         I+P_{C_N}
 \tag{6.6}
\]

and has determinant of absolute value `2`.

#### Proof

An intact `B_j` contains the forbidden five-owner pattern, so every row
must be hit.  Each transition lies in at most two rows; the shared
transitions `c_j` form the vertex-cover incidence of the odd cycle.  Thus
at least `ceil(N/2)` cuts are needed, and alternating shared transitions
attain the bound.

Restricted to row `B_j` and columns `c_j`, the two ones occur at
`c_(j-1),c_j`, giving (6.6).  If

\[
                         (I+P)v=0,
\]

then consecutive entries alternate.  Around an odd cycle this forces the
usual determinant magnitude `2`; equivalently the eigenvalue product of
`I+P` is `2`.  Hence the joint cut-selection matrix is not TU.  \(\square\)

At `k=15`, (6.5) is eight cuts on this `45`-owner component.  The component
has only polynomial size, so the proposition is not an asymptotic no-go.
Its role is exact: fixed-atlas compilation is interval-TU, whereas even the
first PBBS-specific choice of which chronology edges to cut already has a
determinant-two obstruction.  A nonlocal braid which replaces the paired
diamond occurrences is outside the proposition.

## 7. GKS does not supply the missing chronology

At one fixed GKS chain endpoint, the chain members are prefix unions of one
ordered star state.  Their witness intervals are nested suffixes, so the
local endpoint packet is laminar.  By Theorem 1.2, any fixed collection of
such endpoint pins is also coordinatewise interval-TU.  This local fact
does not make the endpoint order resident.

The exact obstruction is already present on a constant-size embedded
sector.  For even `k`, the embedded `B_4` GKS subtree has local middle
members

\[
                         12;quad (23,24),\ (13,34),\ (14).
 \tag{7.1}
\]

Every sibling order either makes a non-Johnson jump or creates an internal
singleton positive coordinate run.  For odd `k=2h+5`, prefixing the
embedded `B_5` sector by `(01)^h` gives root and child blocks

\[
 \begin{aligned}
 R&=(123),\\
 A^+&=(234,245,235),&A^-&=(234,235,245),\\
 B^+&=(134,345,135),&B^-&=(134,135,345),\\
 C&=(124,145),&D&=(125).
 \end{aligned}
 \tag{7.2}
\]

The only safe block continuations are

\[
 A^+\to\varnothing,quad A^-\to C,quad
 B^+\to D,quad B^-\to A,quad C\to D,quad D\to C,
 \tag{7.3}
\]

with the entry from `R` excluding `A^-`, `B^-`, and `D`.  Starting with
`A^+` stops immediately; `B^+` forces `D,C` and then cannot enter `A`;
starting with `C` forces `D` and stops.  Hence no parent-first sibling order
is both Johnson and free of an internal singleton run.

By erosion--Johnson duality, neither (7.1) nor (7.2) is the window union of
any positive-depth resident controller.  Thus the natural parent-first GKS
preorder is closed before the common `Q_x` question is reached.  Arbitrary
non-tree endpoint orders and nonlocal PBBS braids are not covered by this
constant-sector obstruction.

There is also no generic TU theorem for choosing the chronology.  At
`(k,r,d)=(15,8,3)`, take the cyclic label word

\[
 Z=a_0\cdots a_7c_1c_2c_3a_0\cdots a_7f_1f_2f_3f_4
 \tag{7.4}
\]

and let `T_i` be its eight consecutive labels.  Every trace through depth
three has the correct rank and every turn is erosion-safe.  The safe-state
arcs form a directed cycle, while the owner `{a_0,...,a_7}` occurs exactly
twice.  Delete one state-incidence row and append this owner row.  The
resulting square minor has determinant `+-2`: the reduced directed-cycle
incidence has one-dimensional all-ones kernel, and the appended row sums to
two on it.  Thus full chronology/owner selection is not TU even though each
fixed chronology fibre has Theorem 1.2.

## 8. Exact bypass theorem and remaining PBBS gate

### Theorem 8.1 (Catalan-chart interval-`Q` bypass)

Fix a depth `d<r`.  Suppose a final cut/braided PBBS atlas consists of
resident single-run Johnson paths

\[
                         T^{(1)},\ldots,T^{(R)}
 \tag{8.1}
\]

with the following properties.

1. Their credited central owners are disjoint and together contain all `W`
   middle owners exactly once.
2. Every required lower and upper target through depth `d` is assigned one
   concrete final occurrence lying wholly inside one path.
3. Every assigned occurrence is retained with its complete two-sided depth
   prefix; all seam and endpoint constraints are among the fixed pins used
   in the common `Q_x` test.

Then one nonzero literal word covers all middle owners and all assigned
targets and has length

\[
                         \boxed{L\le W+dR.}
 \tag{8.2}
\]

Every chart has a common interval-`Q` compiler; no rankwise matching or
rounding is needed.

#### Proof

If path `j` contains `N_j` credited owners, Theorem 2.1 gives its maximal
erosion word of length `N_j+d`, with all assigned internal flags realized.
Concatenate these `R` words.  Witness intervals remain internal to their
charts.  Since `sum_j N_j=W`, the total length is (8.2).  \(\square\)

For `d=O(sqrt(m))` and `R=O(B)`,

\[
                         dR=O(B\sqrt m)=O(W/\sqrt m)=o(W).
 \tag{8.3}
\]

This is a genuine structural route around the frozen `k=15` carrier: it
constructs a different carrier for which the common compiler is automatic.
It is not yet a PBBS theorem.  The sole unresolved PBBS content of this
route is the following simultaneous assertion:

> **PBBS single-run occurrence-atlas gate.**  At the required depth, choose
> a cut/braid of the canonical PBBS all-depth factor into `O(B)` resident
> single-run paths, preserve exact middle ownership, and assign every
> required target one final internal two-sided flag occurrence.

The targetwise corridor theorem proves the local packet part.  The
reverse-bank theorem proves one exact carrier splice.  Proposition 6.1
shows that arbitrary PBBS arcs do not satisfy the condition, and
Proposition 6.2 shows that even cut selection is not generically TU.
Neither component connectivity nor scalar occurrence load proves the gate.

## 9. Proved boundary

The unconditional conclusions are:

1. fixed resident chronology plus fixed cut-aware pins has an exact maximal
   common compiler and a coordinatewise interval-TU positive-hit matrix;
2. resident single-run paths carry the complete natural two-sided flag
   tower in one physical word and have physical interval `Q_x`;
3. every canonical PBBS target corridor is a resident laminar instance;
4. reversed-bank/core-swap corridor pairs compose at the Johnson-carrier
   level, including all cross-seam flags;
5. a complete middle carrier cannot have globally laminar `Q_x` when
   `r>d+1`, and must have aggregate fragmentation at least `W-1`;
6. the canonical PBBS three-root component contains both a flat-residence
   obstruction and a determinant-two cut-selection obstruction; and
7. the natural parent-first GKS preorder fails before compiler integrality,
   while general chronology selection is not TU.

The note makes no claim that the PBBS single-run occurrence-atlas gate is
true.  It isolates exactly what would make the interval-TU special case a
coefficient-one bypass and exactly why local laminarity or connectivity
alone does not do so.
