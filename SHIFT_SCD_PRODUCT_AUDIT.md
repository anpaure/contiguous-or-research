# Shift-compatible SCDs: product attempts and the syndrome-tiling obstruction

This note audits whether the explicit kernel-translate cycle tiling in
`LINEAR_CYCLE_TILING.md` can itself be decorated into the wreath-resolved
symmetric-chain decomposition proposed in Sections 9--10 of
`PARTIAL_BLOCK_MULTISCALE.md`.

The answer is no beyond logarithmic certification depth.  The middle-layer
tiling remains correct and useful, but its translates have unavoidable
collisions after a coordinate window longer than the syndrome redundancy is
erased.  This is an algebraic obstruction, independent of the enumeration
used to define the syndrome map.

## 1. Flags of a partial pair-flip cycle

Work first in one orientation cube `Q_ell=F_2^ell`.  Let

\[
 P=(p_0,p_1,\ldots,p_{2\ell-1})
\]

be the standard pair-flip cycle, so the coordinate flipped on successive
edges is

\[
 1,2,\ldots,\ell,1,2,\ldots,\ell.
\]

For a start `t` and a depth `q<ell`, let `Q_t(q)` be the set of the `q`
coordinates flipped on the next `q` edges.  These coordinates are distinct.
In the original paired ground set, the depth-`q` lower flag of the middle
vertex at start `t` is obtained by making the pairs in `Q_t(q)` empty and
retaining the orientations of every other split pair.  The upper flag makes
those same pairs full and likewise retains every other orientation.

Consequently, if two translated cycles differ by an orientation vector `z`,
then their depth-`q` lower flags at the same start coincide exactly when

\[
 \operatorname{supp}(z)\subseteq Q_t(q).             \tag{1.1}
\]

The identical criterion holds for the upper flags.

## 2. Kernel translates collide after the redundancy

Let

\[
 \phi:\mathbb F_2^\ell\longrightarrow\mathbb F_2^r,
 \qquad r=\log_2(2\ell),
\]

be any syndrome map for which `P` is a transversal, and put
`K=ker(phi)`.  Thus the blocks `P+k`, `k in K`, tile the orientation cube.

### Theorem 1 (erasure collision theorem)

Fix a start `t` and a depth `q`.  Every depth-`q` lower flag arising from the
kernel translates at that start has multiplicity at least

\[
 2^{\max(0,q-r)}.                                    \tag{2.1}
\]

The same is true of the upper flags.  In particular, among the `|K|`
translated starts with this fixed `t`, a family with pairwise-distinct
depth-`q` flags has size at most

\[
 |K|\,2^{-\max(0,q-r)}.                              \tag{2.2}
\]

#### Proof

Let `V_t(q)` be the coordinate subspace supported on `Q_t(q)`.  Since

\[
 \dim K=\ell-r,
 \qquad \dim V_t(q)=q,
\]

the dimension formula gives

\[
 \dim(K\cap V_t(q))
 \ge (\ell-r)+q-\ell=q-r.                            \tag{2.3}
\]

For every `z in K cap V_t(q)`, the two translated starts indexed by `k` and
`k+z` have the same erased flag by (1.1).  Hence every fibre contains the
coset `k+(K cap V_t(q))`, proving (2.1) and (2.2).  QED.

This is just the elementary coding-theoretic statement that `r` check bits
cannot uniquely recover more than `r` erased coordinates.  It does not
depend on how the syndrome values `u_i` were enumerated.

## 3. Incompatibility with the SCD radius law

The bound survives Cartesian fibres, fixed full/empty pairs, and summation
over every orientation stratum.  Group all middle starts by

* their pair-type stratum;
* the inactive orientation fibre;
* their relative start `t` in the standard cycle.

Within every group Theorem 1 applies.  Therefore, from all `W` tiled middle
vertices, at most

\[
 2^{r-q}W                                             \tag{3.1}
\]

can be assigned radius at least `q` while retaining pairwise-distinct
depth-`q` lower flags, whenever `q>r`.  Allowing collisions between different
groups can only decrease this upper bound.

By contrast, an SCD of the `2m`-cube has exactly

\[
 N_q=\binom{2m}{m-q}=\rho_q W                        \tag{3.2}
\]

chains of radius at least `q`, and their depth-`q` lower members must be all
distinct.  Hence a necessary condition for the kernel tiling to support the
SCD flags is

\[
 \rho_q\le 2^{r-q}.                                  \tag{3.3}
\]

For the prescribed-scale construction, `ell=m^(3/4+o(1))`, so
`r=(3/4+o(1))log_2 m`.  Take, for example, `q=2r`.  Then

\[
 \rho_q=\exp(-q^2/m+o(1))=1-o(1),
 \qquad 2^{r-q}=2^{-r}=o(1).                         \tag{3.4}
\]

Thus (3.3) fails by a factor tending to infinity.  In fact the construction
cannot resolve even an `o(W)`-defect SCD at this logarithmic depth, long
before the desired depth `Theta(sqrt(m log m))`.

### Corollary 2

No choice of the syndrome enumeration in `LINEAR_CYCLE_TILING.md`, and no
fixed Cartesian extension of that kernel tiling, turns its consecutive
intersection/union flags into a near wreath-resolved SCD through the required
depth.

This does **not** invalidate the Stage-A row theorem: the cycles still tile
the middle vertices and preserve whichever individual windows are later
selected.  It says that Stage B cannot certify the required fraction of
those windows by simply assigning radii to the existing kernel translates.

## 4. Consequences for product and recursion attempts

The obstruction identifies what a successful direct construction must add.

1. **One low-redundancy coset tiling is insufficient.**  A depth-`q` flag
   needs enough variation in its erased coordinate set to compensate for the
   `q-r` invisible kernel directions.

2. **Independent Cartesian fibres do not help.**  The collision occurs
   inside every fibre before fibres are combined.

3. **A multiscale mixture remains possible.**  Different block systems may
   give the same middle vertex different flip windows.  Selecting chains
   across many such resolutions can avoid the fixed-window kernel fibres;
   this is exactly the typed matching problem rather than a single tiling.

4. **A product SCD needs a non-Cartesian shuffle.**  Tensoring paired
   coordinate diamonds while retaining one fixed active-coordinate order
   inherits the same erasure fibres.  Any viable product theorem must change
   the active shuffle from block to block (or use a global promotion action)
   while keeping all ranks disjoint.

### The standard diamond-product recursion fails on almost every centre

There is an even more elementary obstruction to the most literal product
attempt.  Give each paired coordinate square its usual decomposition

\[
 \varnothing\subset\{a_i\}\subset\{a_i,b_i\},
 \qquad \{b_i\},                                      \tag{4.1}
\]

and combine the factors using the standard BTK product recursion.  Up to the
chosen ordering and orientation of the coordinates, this is the
Greene--Kleitman SCD.

Let a Greene--Kleitman chain of radius `d>0` have star positions

\[
 e_1<\cdots<e_{2d}.
\]

Its middle member has star pattern `1^d 0^d`; its first downward and upward
labels are `e_d` and `e_(d+1)`.  The projected middle move therefore changes
the star pattern to

\[
 1^{d-1},0,1,0^{d-1}.                             \tag{4.2}
\]

The central `01` is now a matched parenthesis pair, so the new middle member
belongs to a Greene--Kleitman chain with only `2d-2` stars, namely radius
`d-1`.

Hence the projected move of the standard product SCD strictly decreases the
chain radius at **every** positive-radius centre.  It cannot be a
radius-preserving permutation on even one such class.  Since the number of
radius-zero chains is only

\[
 \binom{2m}{m}-\binom{2m}{m-1}
 =\frac{1}{m+1}\binom{2m}{m}=o(W),                   \tag{4.3}
\]

the untouched standard product recursion fails the shift-compatible
condition on `1-o(1)` of all middle centres.  Local treatment of only its
Catalan many roots cannot repair this; a successful product construction
must globally rewire the chain memberships or use a genuinely different
tensor shuffle.

## 5. Necklace/Dyck-path route: precise status

### Why lifting a necklace SCD by coordinate rotations is not enough

The known theorem that the necklace quotient `B_(2m)/C_(2m)` is a symmetric
chain order does not directly give the required middle cycles.  In the most
literal lift, all rotations of one quotient chain are used as parallel
chains.  For their middle projections to form one shift orbit, a middle set
`X` would have to satisfy

\[
 |X\mathbin\triangle \sigma^a X|=2                 \tag{5.1}
\]

for some nontrivial coordinate rotation `sigma^a`.

Almost no middle sets have this property.  Put `n=2m` and
`g=gcd(n,a)`.  The permutation `sigma^a` has `g` coordinate cycles, each of
length `L=n/g`.  Hamming distance two means that exactly one such cycle has
two binary transitions and every other cycle is constant.  Even without
imposing weight `m`, the number of such binary strings is at most

\[
 g\binom L2 2^g.                                      \tag{5.2}
\]

For `a not congruent 0`, one has `g<=m`; summing (5.2) over all rotations
gives only

\[
 O(m^4 2^m)=o\!\left(\binom{2m}{m}\right).           \tag{5.3}
\]

Thus a rotation-lifted quotient chain can provide the required Johnson move
for only an exponentially small fraction of the middle layer.  A useful
necklace construction must use the necklace merely as an index and assign a
new ground-set permutation to each index; it cannot use coordinate rotation
itself as the projected shift.

There is a closely related, but currently conjectural, way to obtain the
needed varying windows.  The identity

\[
 (m+1)\operatorname{Cat}_m=\binom{2m}{m}
\]

identifies middle `m`-sets with the correct number of pairs consisting of a
Dyck `m`-path and one of its `m+1` linear windows of length `m`.  Petr and
Turek proved the finer count

\[
 \iota_m(m,l)=\binom ml^2,
\]

and conjectured compatible labelings of the Dyck paths that resolve the
corresponding Katona wreaths on `2m+1` points.  Restricting their conjectured
wreaths to the windows avoiding the distinguished point would already give
an exact, non-coset partition of the middle layer of `B_(2m)` into these
`m+1`-window paths.

This is attractive because the Dyck path supplies a non-Cartesian shuffle,
but the compatible labeling is itself open (verified in that work only for
small parameters), and middle-layer resolution alone still does not prove
the all-depth SCD flag partition.  It should therefore be treated as a
specific conjectural replacement for the failed fixed-kernel route, not as
an available theorem.

## 6. Revised direct target

The most concrete successor is a **multi-resolution SCD theorem**:

> Choose almost all middle vertices from a superposition of pair-flip
> resolutions so that, at every depth `q`, the selected erased windows meet
> every kernel/projection fibre at most once and occur with the forced density
> `rho_q`, nested in `q`.

Theorem 1 shows why the word “superposition” is essential.  A single
translation tiling, however explicit, cannot satisfy this statement.

The fixed-pair construction can be sharpened in a different direction.  For
every oriented split core `(S,eta)`, an SCD of the residual Boolean lattice
on `[m]\S` simultaneously pairs all lower and upper pair-type targets.  The
complete theorem, the proof that every prescribed residual central matching
extends to an SCD, and an unconditional `W-o(W)` fixed-pair depth-one
linearization are in `FIXED_PAIR_RESIDUAL_SCD.md`.  That note also proves
that choosing the residual SCD independently of `eta` forces disjoint
four-cycles on almost all middle vertices, so orientation dependence is the
minimum viable form of the required superposition.
