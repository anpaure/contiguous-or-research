# What radius-pure Bender--Knuth cubes buy for the shadow problem

## 0. Verdict

The fixed-coordinate refinement of the odd Bender--Knuth cubes is a real
advance, but it does **not** by itself produce a wreath-resolved symmetric
chain decomposition.

There are four logically separate levels.

1. A genuine fixed-coordinate cube supplies many locally geodesic
   pair-flip cycles inside one RSK radius class.  Thus it solves the local
   Johnson-support problem that remained open in `TABLEAU_CRYSTAL_AUDIT.md`.
2. The per-vertex host theorem in `BENDER_KNUTH_ISOMETRIC_CUBES.md` can in
   fact be upgraded: partition every critical orientation sequence by its
   last `DU`.  This partitions every odd-BK orbit into genuine isometric
   subcubes, and all but `o(W)` vertices lie in cells of dimension
   `(1/8-o(1))m`.  Thus the middle-only Stage A is solved.
3. The resulting free supports are all native pairs
   `{1,2},{3,4},...`.  Hence this particular partition is trapped inside
   one global coordinate matching.  The deterministic capacity theorem in
   `FIXED_PAIR_RESIDUAL_SCD.md`, Section 8, says that it misses `1-o(1)` of
   the targets when `q/sqrt(m)->infinity`, regardless of how its cycle
   tilings are coordinated.  It cannot by itself reach the literal-tail
   depth.
4. Even before that deep capacity barrier, orbitwise pair-flip cycle factors
   do not automatically have globally unique shadows.  Independent
   orbitwise choices leave at least an `e^(-1)-o(1)` expected fraction of
   both first-shadow layers missing.
   At larger depth, using one fixed cyclic direction order in each cube
   creates a deterministic macroscopic collision once

   \[
        2^q>\ell,
   \]

   where `2 ell` is the cycle length.

The positive conclusion is an exact bridge theorem.  Radius-pure isometric
cubes reduce the remaining all-rank problem to making two explicit
inverse-RSK shadow maps into near permutations.  They remove local
geodesicity, radius accounting, and middle-only block construction from the
list of unknowns.  They do **not** remove the global rainbow matching, and
the native-pair partition must be mixed with conjugate pairings (or with
nonlocal carrier supports) before it can cover the full useful band.

Throughout,

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\]

and

\[
 a_d=f^{(m+d,m-d)}=N_d-N_{d+1}
\tag{0.1}
\]

is the number of middle words of RSK radius `d`.

## 1. The exact local object

A fixed-coordinate `s`-cube in the middle layer has the form

\[
 \mathcal Q(C;P_1,\ldots,P_s)
 =\left\{C\cup\{x_1,\ldots,x_s\}:x_i\in P_i\right\},
\tag{1.1}
\]

where the `P_i={a_i,b_i}` are pairwise disjoint, `C` is disjoint from all
of them, and `|C|+s=m`.  It is **radius-pure** when all its vertices have the
same binary-RSK shape `lambda_d=(m+d,m-d)`.

Inside such a cube, any standard pair-flip cycle is an actual isometric
Johnson cycle.  A window which flips `q` different directions spans an
axis-parallel `q`-face.  Its intersection deletes both members of the `q`
free pairs and its union includes both members.  Hence its two shadows have
ranks `m-q` and `m+q`.

For a single cycle, distinct cyclic starts give distinct lower shadows and
distinct upper shadows for every `q<ell`; this is the local theorem in
`FIXED_DEPTH_SHADOWS.md`.  Radius purity says that a cube of radius `d` may
certify exactly the depths `q<=d`, as required by the SCD radius ledger.

The fixed-coordinate Bender--Knuth analysis gives, for all but `o(W)`
middle tableaux, a cube of dimension `(1/8-o(1))m` through the tableau: one
keeps every native `DU` pair except the last `DU` at each critical level.
This is enough local dimension for every

\[
 H=o(m),\qquad \ell=o(m),\qquad H<\ell.
\tag{1.2}
\]

The host cubes in that theorem depend on the tableau and overlap.  The
following last-`DU` resolution upgrades them to an actual near-partition.

### Theorem 1 (orbitwise isometric cube partition)

Every orbit of the commuting odd Bender--Knuth generators partitions into
radius-pure genuine fixed-coordinate subcubes.  Moreover, all but `o(W)`
middle tableaux belong to cells of dimension

\[
 \frac m8-m^{5/6}=(1/8-o(1))m.
\tag{1.3}
\]

Every free direction in this partition has its native support
`{2j-1,2j}`.

#### Proof

The block-level height path, the active mixed blocks, and the critical
sequences are constant on one odd-BK orbit.  Consider one critical sequence
of length `a`, with orientation word `x_1...x_a`, where `x_i=1` means `DU`.
Partition its orientation cube into

\[
 \begin{aligned}
 R_0&=\{0^a\},\\
 R_l&=\{x:x_l=1,\ x_{l+1}=\cdots=x_a=0\}
       \qquad(1\le l\le a).
 \end{aligned}
\tag{1.4}
\]

In `R_l`, the first `l-1` bits are free.  Every corresponding generator has
the fixed later `DU` at position `l`, so the support formula in
`BENDER_KNUTH_ISOMETRIC_CUBES.md`, Theorem 1, gives its native support
`{2j-1,2j}` throughout the cell.  The later directions and direction `l`
are fixed.  The cell `R_0` has no free direction from this sequence.
All noncritical active directions remain free and already have native
support.  Taking the product over the critical sequences therefore
partitions the whole odd-BK orbit into genuine fixed-disjoint-support cubes.
Bender--Knuth moves preserve shape, so every cell is radius-pure.

Let `A` be the number of active directions in the orbit and let `Delta` be
the number lost in the cell containing a uniformly random orbit vertex.  A
critical sequence of length `a` contributes

\[
 \delta=
 \begin{cases}
   a,&x=0^a,\\
   a-l+1,&l\text{ is the last }1,
 \end{cases}
\]

and hence

\[
 \mathbb E\delta
 =a2^{-a}+\sum_{t=1}^a t2^{-t}
 =2-2^{1-a}<2.
\tag{1.5}
\]

There are at most `floor(d/2)` critical sequences at radius `d`, so

\[
 \mathbb E\Delta<d.
\tag{1.6}
\]

The radius-tail estimate in the cited note shows that all but `o(W)`
vertices have `d<=m^(2/3)`.  Its `DU` lower-tail estimate shows that all but
`o(W)` vertices have at least `m/8` `DU` blocks.  Since every `DU` block is
active, every orbit containing such a vertex has `A>=m/8`; indeed an orbit
with `A<m/8` consists entirely of lower-tail exceptions.

On every remaining orbit, Markov's inequality and (1.6) give

\[
 \Pr(\Delta>m^{5/6})\le m^{-1/6}.
\tag{1.7}
\]

Summing (1.7) with orbit-size weights discards only `o(W)` further vertices.
Every retained vertex lies in a cell of dimension
`A-Delta>=m/8-m^(5/6)`, proving (1.3).  QED.

Thus the Bender--Knuth route now has an explicit middle-only Stage-A
partition.  The price is equally explicit: every free direction belongs to
the one global native coordinate matching

\[
 \{\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\}.
\tag{1.8}
\]

## 2. The inverse-RSK shadow coordinates

For every `q`, binary RSK gives canonical bijections

\[
 \begin{aligned}
 \kappa_q^-:
   \bigsqcup_{d=q}^m\operatorname{SYT}(\lambda_d)
       &\longrightarrow \binom{[2m]}{m-q},\\
 \kappa_q^+:
   \bigsqcup_{d=q}^m\operatorname{SYT}(\lambda_d)
       &\longrightarrow \binom{[2m]}{m+q},
 \end{aligned}
\tag{2.1}
\]

where

\[
 \kappa_q^\pm(Q)=\operatorname{invRSK}(P_{d,q}^\pm,Q)
 \quad(Q\in\operatorname{SYT}(\lambda_d)).
\tag{2.2}
\]

The domain size is

\[
 \sum_{d=q}^m a_d=N_q,
\tag{2.3}
\]

exactly the size of either target layer.

Now suppose the radius-`d` middle words have been put into directed
pair-flip cycles.  For a start tableau `Q`, let `X_j(Q)` be the `j`th middle
word along its cycle and set

\[
 L_q(Q)=\bigcap_{j=0}^qX_j(Q),\qquad
 U_q(Q)=\bigcup_{j=0}^qX_j(Q).
\tag{2.4}
\]

Define the **RSK shadow-index maps**

\[
 \Theta_q^-=(\kappa_q^-)^{-1}\circ L_q,
 \qquad
 \Theta_q^+=(\kappa_q^+)^{-1}\circ U_q.
\tag{2.5}
\]

Both maps have the same finite set

\[
 \mathcal T_{\ge q}=\bigsqcup_{d=q}^m\operatorname{SYT}(\lambda_d)
\tag{2.6}
\]

as domain and codomain.

### Theorem 2 (exact RSK permutation criterion)

Assume every middle word of radius at least `q` occurs once in the chosen
cycle factor and every relevant `q`-window is geodesic.  Then the depth-`q`
lower shadows are all distinct if and only if `Theta_q^-` is a permutation
of `mathcal T_(>=q)`.  The analogous statement holds above.  In either case,
injectivity alone implies complete coverage.

#### Proof

The maps `kappa_q^pm` are bijections.  The domain and target layer both have
size `N_q` by (2.3).  Therefore distinct physical shadows are equivalent to
injectivity of (2.5), and injectivity is equivalent to bijectivity.  QED.

This is the exact payoff of the inverse-RSK vectors `P_(d,q)`: they turn
global shadow coverage into an ordinary permutation problem on recording
tableaux.  They do not identify the physical face map automatically.

## 3. The canonical RSK flags cannot be retained

The most tempting strengthening of Theorem 2 is false already at depth one.

### Proposition 3 (no identity on both sides)

Let `Q` have positive radius `d`, let `X=kappa_0(Q)` be its middle word, and
let `Y` be a radius-`d` Johnson neighbour of `X`.  It is impossible to have
simultaneously

\[
 X\cap Y=\kappa_1^-(Q),\qquad
 X\cup Y=\kappa_1^+(Q).
\tag{3.1}
\]

In particular, no nontrivial Bender--Knuth edge makes both maps in (2.5)
the identity at `Q`.

#### Proof

In the canonical crystal chain through `Q`, write

\[
 \kappa_1^-(Q)=X-\{r_0(Q)\},\qquad
 \kappa_1^+(Q)=X\cup\{u_0(Q)\}.
\]

Equations (3.1) determine the other endpoint uniquely:

\[
 Y=X-\{r_0(Q)\}+\{u_0(Q)\}.
\]

The canonical-radius-drop theorem in `TABLEAU_CRYSTAL_AUDIT.md` says that
this word has RSK radius `d-1`, contradicting the assumed radius `d`.  QED.

Thus a successful Bender--Knuth construction must globally re-pair the
canonical lower and upper vectors.  Radius purity is compatible with a
wreath-resolved SCD only after this re-pairing; it cannot preserve the
standard crystal chains.

## 4. What is automatic at depth one inside one cube

Fix one cube (1.1).  A cube edge is determined by

* its flipped pair `P_i`; and
* one chosen member of every other active pair.

Its lower shadow contains neither member of `P_i`, while its upper shadow
contains both.  Therefore distinct edges of one fixed cube have distinct
lower shadows and distinct upper shadows.

Consequently **every** cycle factor of one cube is shadow-simple at depth
one.  All depth-one collisions in a disjoint cube partition are necessarily
cross-cube collisions.

Radius purity does not prevent such a collision.  On eight coordinates,
the following two radius-one Bender--Knuth edges lie in different odd-BK
orbits:

\[
 \{2,3,4,5\}\longleftrightarrow\{2,3,4,6\},
 \qquad
 \{2,3,4,7\}\longleftrightarrow\{2,3,4,8\}.
\tag{4.1}
\]

Both have lower shadow `{2,3,4}`.  The first uses the fixed coordinate pair
`{5,6}` and the second uses `{7,8}`.  Thus even genuine radius-pure
fixed-coordinate cube edges do not have globally unique first shadows.

## 5. Independent orbitwise rounding has an `e^(-1)` barrier

The preceding example is finite.  There is also a general macroscopic
obstruction to the most obvious randomized use of a hypothetical cube
partition.

### Theorem 4 (Poisson barrier for independent cube factors)

Assume, as an extra hypothesis, that all positive-radius middle words are
partitioned into radius-pure fixed-coordinate cubes `Q_alpha` of dimensions
`s_alpha`, where

\[
 s_{\min}:=\min_\alpha s_\alpha\longrightarrow\infty.
\tag{5.1}
\]

In each cube independently choose a random cycle factor from a distribution
invariant under translations and permutations of its `s_alpha` directions.
Then the expected number of missing rank-`m-1` lower shadows is at least

\[
 (e^{-1}-o(1))N_1.
\tag{5.2}
\]

The same lower bound holds for upper shadows.  Since the number of physical
depth-one slots is `N_1`, the expected collision excess is the same as the
expected missing count.

#### Proof

A cycle factor of `Q_s` has `2^s` edges, whereas the cube has
`s2^(s-1)` edges.  Symmetry therefore makes each cube edge present with
probability

\[
 p_s=2/s.
\tag{5.3}
\]

Fix a lower target `S`.  By Section 4, at most one cube edge in any fixed
cube has lower shadow `S`.  Let `A(S)` be the cubes containing such a
candidate edge and put

\[
 \lambda_S=\sum_{\alpha\in A(S)}2/s_\alpha.
\tag{5.4}

Independence gives

\[
 \Pr(S\text{ is missed})
 =\prod_{\alpha\in A(S)}(1-2/s_\alpha).
\tag{5.5}

For `epsilon=2/s_min=o(1)`,

\[
 \log(1-p)\ge -p/(1-p)\ge-(1+2\epsilon)p,
\]

so (5.5) is at least

\[
 \exp(-(1+2\epsilon)\lambda_S).
\tag{5.6}

Every selected cube factor contributes one first-shadow slot per cube
vertex.  The number of positive-radius middle vertices is

\[
 \sum_{d\ge1}a_d=N_1.
\]

Double counting candidate-edge probabilities therefore gives

\[
 \sum_{S\in\binom{[2m]}{m-1}}\lambda_S=N_1.
\tag{5.7}

Average (5.6) over the `N_1` targets and use convexity of the exponential.
Equations (5.6)--(5.7) give (5.2).  The upper proof is identical.  Finally,
with exactly `N_1` slots, missing targets and repeated occurrences have the
same total excess.  QED.

The theorem does **not** say that a coordinated choice is impossible.  It
says that the cubes do not make Stage B an independent local decision.  A
global matching, switching, or absorption theorem is mandatory even at
depth one.

## 6. A fixed direction order fails at logarithmic depth

There is a second obstruction inside one cube.  It applies to the explicit
linear-code tiling when every translated cycle uses one common cyclic order
of `ell` directions.

### Theorem 5 (direction-catalog bound)

Let an `s`-cube be factored into partial `2ell` pair-flip cycles.  Suppose
the set of `q` directions used by a `q`-window belongs to a catalog of at
most `K_q` subsets of the `s` cube directions.  Then the number of distinct
depth-`q` lower shadows, and likewise upper shadows, is at most

\[
 K_q2^{s-q}.
\tag{6.1}

Since the factor has `2^s` depth-`q` starts, its collision excess is at
least

\[
 \left(2^s-K_q2^{s-q}\right)_+.
\tag{6.2}

For one common cyclic direction order, `K_q<=ell`.  Hence

\[
 c_q^\pm\ge
 \left(1-\frac{\ell}{2^q}\right)_+2^s.
\tag{6.3}

#### Proof

A `q`-shadow is the Boolean label of a `q`-face.  Once its free direction
set is fixed, at most `2^(s-q)` orientations of the other directions are
available.  Summing over the catalog gives (6.1).  Subtract from the `2^s`
physical starts to obtain (6.2).  A cyclic order has only `ell` cyclic
intervals of length `q`, proving (6.3).  QED.

In the intended regime `ell=m^(3/4+o(1))` and
`H=sqrt(m omega(m))`, choose, for example,

\[
 q=\lceil\log_2\ell\rceil+2.
\tag{6.4}

Then `q=o(sqrt m)`, so `N_q=(1-o(1))W`, but (6.3) loses at least
`(3/4-o(1))` of the slots in every same-order cube factor.  Thus simply
applying the fixed linear translate tiling to every Bender--Knuth cube gives
a macroscopic shallow-shadow defect.  The direction order must vary between
cycles.  More quantitatively, a shadow-injective factor needs at least

\[
 2^q
\tag{6.5}

different `q`-direction sets across its cycles.

This is consistent with `CUBE_SHADOW_TILING.md`: its finite-field translate
tiling is face-simple through `q<=log_2 ell`, and the quotient-rank barrier
appears immediately after that range.

### Proposition 6 (the native partition has a fixed-pair capacity defect)

There are absolute constants `c,eta>0` such that, at

\[
 q=\lfloor c\sqrt m\rfloor,
\tag{6.6}
\]

every block factor confined to the native-pair partition of Theorem 1 misses
at least `eta W` lower targets and at least `eta W` upper targets.  This is
independent of direction orders, switches, or coupling between cells.

#### Proof

Relative to the native matching (1.8), a rank-`m-q` target of pair type `f`
has count

\[
 T_{f,q}=\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q},
\]

whereas every native-pair construction has only

\[
 V_f=\frac{m!}{f!f!(m-2f)!}2^{m-2f}
\]

physical starts of its required source type.  Thus it misses at least
`sum_f(T_(f,q)-V_f)_+`; this is the exact capacity theorem in
`FIXED_PAIR_RESIDUAL_SCD.md`, Section 8.

For a uniformly random target, the type `F` has variance `O(m)` and saddle

\[
 f_*=(m-q)^2/(4m).
\]

Moreover, uniformly in the central type range,

\[
 \log\frac{V_f}{T_{f,q}}
 =-\frac{q^2}{m}
   +O\!\left(\frac qm+\frac{q^3}{m^2}
       +\frac q m|f-f_*|\right).
\tag{6.7}
\]

Choose a fixed `C` so that `|F-f_*|<=C sqrt(m)` contains, say, at least
half of the target mass; Chebyshev's inequality permits this.  Then choose
the fixed constant `c` in (6.6) sufficiently large compared with the
absolute constant in (6.7).  Throughout that positive-mass type band,

\[
 V_f/T_{f,q}\le e^{-c^2/2}<1/2.
\]

Hence a fixed positive fraction of the entire rank-`m-q` layer is missed.
Finally,

\[
 \frac{N_q}{W}=e^{-c^2+o(1)},
\]

which is a positive constant for fixed `c`.  The missing count is therefore
at least `eta W` for some constant `eta>0`.  Complementation gives the upper
statement.  Linearizing partial cycles creates only `O(qW/ell)=o(W)` new
depth-`q` seam windows when `ell>>sqrt(m)`, so the same `Omega(W)` conclusion
holds for the resulting row.  QED.

This proposition is stronger than the direction-catalog obstruction for
the specific native partition: even perfect direction diversity cannot
repair the wrong source-type capacities.  Its scope is also narrower.  An
arbitrary vertex-cover subcube from
`BENDER_KNUTH_ISOMETRIC_CUBES.md` may retain one nonlocal carrier direction
in a critical tail, and conjugating the whole construction changes the
global coordinate matching.  Proposition 6 does not exclude a reservoir
that deliberately mixes those different pair systems.

## 7. The conditional positive bridge

The preceding obstructions leave a precise sufficient theorem.

### Theorem 6 (Bender--Knuth shadow bridge)

Let `H<ell` tend to infinity with `H/ell->0`.  Suppose:

1. all but `E` middle tableaux lie in a vertex-disjoint family of
   radius-pure fixed-coordinate cubes of dimension at least `ell`;
2. each cube is tiled by pair-flip cycles, and a radius-`d` cube certifies
   the starts through depth `min(d,H)`;
3. if

   \[
    c_q^-=|D_q|-|\{L_q(Q):Q\in D_q\}|,
    \qquad
    c_q^+=|D_q|-|\{U_q(Q):Q\in D_q\}|,
   \tag{7.1}
   \]

   where `D_q` is the covered radius-at-least-`q` domain, then

   \[
    HE+\sum_{q=1}^H(c_q^-+c_q^+)=o(W).
   \tag{7.2}
   \]

Then these blocks form a near wreath-resolved SCD of the central band with
total defect `o(W)`.  Equivalently, the RSK maps `Theta_q^pm` in (2.5) are
near permutations with total defect `o(W)`.

If, in addition, `H=sqrt(m omega(m))` for some `omega(m)->infinity` slow
enough for the block hypotheses, the tail construction of
`TRUNCATED_IDEAL_PRODUCT.md` gives

\[
 \nu(2m)=W+o(W).
\tag{7.3}
\]

#### Proof

For a complete radius partition, (0.1) telescopes to exactly `N_q` certified
starts at depth `q`.  Omitting `E` middle vertices removes at most `E` starts
at each depth.  Local pair-flip geodesicity makes every remaining start a
valid rank-`m-q` and rank-`m+q` shadow.  Therefore the number of missing
targets at depth `q` is at most

\[
 E+c_q^-\quad\text{and}\quad E+c_q^+.
\]

Summing through `H` and using (7.2) gives `o(W)` literal repairs.  Cycle
linearization costs `O(HW/ell)=o(W)`, and omitted middle vertices cost
`O(HE)=o(W)`.  This is precisely the near wreath-resolved SCD criterion in
`PARTIAL_BLOCK_MULTISCALE.md`.  The cited tail theorem then proves (7.3).
QED.

Theorem 1 supplies the cube-partition hypothesis with `E=o(W)`, and ordinary
linear-code tilings supply the middle cycle factor.  Thus the entire
remaining construction is the simultaneous near-permutation problem (2.5).
Proposition 6 says that this problem has no solution inside the one native
pairing; Theorem 6 becomes useful only after mixing conjugated or nonlocal
BK cube systems.

## 8. Exhaustive checker

The script

```text
scratch/check_bk_shadow_bridge.py
```

independently performs the following small-case checks.

* It computes binary RSK and the odd Bender--Knuth orbits.
* It checks which natural odd-BK orbits are genuine fixed-disjoint-coordinate
  cubes.
* It enumerates all first-shadow face collisions between distinct
  radius-pure cubes.
* It computes the inverse-RSK vectors `P_(d,1)` on both sides and verifies
  that no radius-preserving BK edge realizes both canonical flags at one
  endpoint.
* It constructs the linear-code cycle tiling and counts its `q`-face
  multiplicities.

The separate checker

```text
scratch/verify_bk_orbit_partition.py
```

constructs every last-`DU` cell through `m=8`, verifies that the cells are
disjoint and cover all `W` tableaux, and checks every free support at every
cell vertex is exactly its native pair.  It also verifies the orbitwise
expectation bound `E Delta<=d` used in (1.6).

Its final lines are

```text
m  vertices  odd-BK orbits  partition cells  mean cell dimension
6       924            267              346             1.89177
7      3432            750             1032             2.30653
8     12870           2123             3096             2.72696
```

For example,

```bash
python3 scratch/check_bk_shadow_bridge.py --max-m 8 --max-ell 16
```

finds the explicit collision (4.1).  For the deterministic natural tiling
of the isometric odd-BK cubes, the depth-one lower collision excess among
the tiled vertices is already

```text
m=6:   85 / 468
m=7:  483 / 1956
m=8: 2152 / 7716
```

and every repeated first face is cross-orbit, as predicted by Section 4.
These finite figures are diagnostics, not an asymptotic lower bound for all
possible coordinated tilings.

For the same-order linear tiling, the checker also verifies zero face
collisions at depths one and two, followed by the rapid higher-depth
collapse predicted by Theorem 5.  The simple default enumeration is not the
finite-field enumeration from `CUBE_SHADOW_TILING.md`, so it is not intended
to attain the optimal logarithmic face-simple range.

## 9. Exact next theorem

The right use of the Bender--Knuth result is not to apply one standard tiling
independently in every native cell.  Proposition 6 rules out that entire
single-pairing architecture.  The viable object is instead a mixed, colored
block reservoir built from conjugated BK partitions and/or admissible
nonlocal-carrier cubes.  Its vertices are

\[
 \text{middle tableaux}
 \quad\dot\cup\quad
 \{(q,-,R),(q,+,R):R\in\mathcal T_{\ge q},\ 1\le q\le H\},
\]

and whose hyperedges are pair-flip cycles cut from the corresponding BK
cubes, decorated by their maps (2.5).

The missing result has two simultaneous parts:

1. choose vertex-disjoint cycles covering `W-o(W)` middle tableaux while
   mixing the different cube systems (a single native system already has
   such a factor, but has the wrong deep-shadow capacities); and
2. make every `Theta_q^-` and `Theta_q^+` a near permutation, with total
   collision excess `o(W)`.

The native pairs in Theorem 1 do **not** vary: they are the fixed matching
(1.8).  Nonlocal carrier supports and coordinate-conjugated copies do vary,
and only those enlarged reservoirs can escape the fixed-matching bias in
`CUBE_SHADOW_TILING.md`.  Theorem 4 shows that independent rounding cannot
exploit that advantage.  Theorem 5 shows that a common direction order
cannot exploit it either.  A proof must use globally coordinated direction
catalogs plus matching or absorption.

That is the honest mathematical boundary: Bender--Knuth cubes solve the
local colored-geometry problem, but the global wreath resolution remains a
correlated rainbow factor theorem.
