# A typed one-cell star has a triangular crossing-collar gate

Date: 2026-08-01  
Lane: K, basis-changing exterior ear for the additive-constant compiler  
Status: exact local theorem and sharp scoped obstruction.  The conditional
one-credit matching ledger is correct, but a one-cell insertion also changes
every selected shorter crossing pin which does not contain the star target.
For the natural star-coordinate code making the destroyed depth-`d` targets
distinct, the entire shorter crossing triangle must be returned.  No
unconditional `B(k)+1` conclusion is claimed.

## 0. Result

Put a new source position at an internal cut and call it `0`.  The exact
fan/crossing identity

\[
 Z\cup C_i=L_{i+1}\cup R_{d-i+1},\qquad Z=A_0,              \tag{0.1}
\]

characterizes the `d-1` old length-`d` cells destroyed by the insertion.
There is a second, load-bearing family: every old crossing cell of length at
most `d-1` survives as its convex hull, and that hull contains the star.

For `u,v>=1`, write

\[
 I_{u,v}=\{-u,\ldots,-1,1,\ldots,v\},\qquad
 C_{u,v}=\bigcup_{p\in I_{u,v}}A_p.                         \tag{0.2}
\]

If `u+v<=d-1`, its transported short cell is

\[
 \widehat I_{u,v}=I_{u,v}\cup\{0\},
 \qquad
 \bigcup_{p\in\widehat I_{u,v}}A_p=C_{u,v}\cup Z.          \tag{0.3}
\]

Consequently a selected old pin on `I_(u,v)` transports with the same target
if and only if that target contains `Z`.  This is the **triangular collar
condition**.  It is independent of marginal Hall and is part of the exact
common-`Q` test.

The condition is costly for star-hidden coding.  If `z in Z` has first side
occurrences at distances `lambda_z,rho_z`, then precisely the shorter cells

\[
 u<\lambda_z,\qquad v<\rho_z,qquad u+v\le d-1              \tag{0.4}
\]

omit `z` and hence cannot retain their old pins.  If `z` is programmed to be
absent from the single destroyed crossing `I_(i,d-i)`, then at least

\[
                         i(d-i)-1                            \tag{0.5}
\]

shorter crossing cells are incompatible.  If `d-1` star coordinates are
used to make the destroyed targets the distinct coatom bank

\[
                         N_i=U-\{z_i\},                      \tag{0.6}
\]

then **every** one of the

\[
                         \binom{d-1}{2}                      \tag{0.7}
\]

shorter crossing cells is incompatible with at least one `z_i`.  Thus a
selector using that triangle needs a separate triangular return; the
`d-1` destroyed cells and the `2d-1` fans are not the complete affected pin
ledger.

There is an exact conditional positive conclusion.  If

1. the two old chains are literally carved on the non-singleton fans;
2. the `d-1` destroyed targets have distinct post-switch native providers;
3. every incompatible selected shorter crossing pin has a distinct return;
4. the diagonal star-spanning owner windows form the declared valid carrier;
5. the singleton target passes the exact star cap below; and
6. all of these incidences coexist in one nonzero common-`Q` state,

then the seam has `alpha_loc=ell+1` on the declared affected fibre (and
`alpha>=ell+1` globally).  Its gross short-band gain is `d`; typing
the singleton consumes one credit and increases the unused-address count by
exactly `d-1` relative to the old basis.

The canonical opposite-orientation coatom fans do not meet these hypotheses.
They force every diagonal owner to the same set and every destroyed crossing
to contain both active labels and the complete filler flag outside `Z`.
Hence they neither repay the canonical NEW chain nor give an owner-complete
`W+1` chronology for growing `d`.

## 1. The full crossing triangle

Fix `d>=2`.  The old line has positions

\[
 -(d-1),\ldots,-1\mid1,\ldots,d-1,
\]

and the new line inserts position `0`.  The side source values are unchanged
in this section; the new value is the nonempty set `Z=A_0`.

For `u,v>=1` with `u+v<=d`, define `I_(u,v)` and `C_(u,v)` by (0.2).
When `u+v=d`, the convex hull has length `d+1`, so the cell leaves the
strict-lower band.  These are exactly the `d-1` destroyed cells

\[
 I_i=I_{i,d-i},\qquad 1\le i\le d-1.                        \tag{1.1}
\]

When `u+v<=d-1`, the convex hull has length at most `d` and is the transported
old cell.

### Theorem 1.1 (exact triangular transport criterion)

For every `u,v>=1` with `u+v<=d-1`, the transported cell has value

\[
                         C_{u,v}\cup Z.                       \tag{1.2}
\]

Therefore an old pin assigning target `C_(u,v)` to `I_(u,v)` transports
unchanged if and only if

\[
                              Z\subseteq C_{u,v}.             \tag{1.3}
\]

More generally, if the old target is `S_(u,v)` and the unchanged side
letters already union to `S_(u,v)`, exact transport is again equivalent to
`Z subseteq S_(u,v)`.

#### Proof

The new convex hull differs from the old crossing cell by the single source
position `0`.  OR is idempotent, so its value is exactly `C_(u,v) union Z`.
This equals `C_(u,v)` precisely when (1.3) holds.  The last statement is the
same identity with the old union named `S_(u,v)`.  \(\square\)

This theorem concerns a literal transported pin.  A compiler may instead
move that target to another cell.  Such a move is a **return edge**, not
transport, and must be counted in `ell` and `alpha`.
If a braid also changes the side source letters, (1.2)--(1.3) must be
recomputed from those terminal letters; the side-fixed criterion cannot be
imported unchanged.

## 2. Threshold rectangles and an exact rerouting count

For a coordinate `z in Z`, let

\[
 \lambda_z=\min\{t\ge1:z\in A_{-t}\},\qquad
 \rho_z=\min\{t\ge1:z\in A_t\},                             \tag{2.1}
\]

where a missing minimum is infinity.  Since the star itself is not in an
old crossing cell,

\[
 z\in C_{u,v}
 \quad\Longleftrightarrow\quad
 u\ge\lambda_z\ \text{or}\ v\ge\rho_z.                    \tag{2.2}
\]

### Theorem 2.1 (rectangular incompatibility ideal)

The selected shorter crossing pins incompatible with retaining `z` at the
star are exactly

\[
 \mathcal R_z={(u,v):u,v\ge1,\ u+v\le d-1,
                         u<\lambda_z,\ v<\rho_z\}.            \tag{2.3}
\]

If the zero set of `z` on the destroyed cells is the nonempty interval
`[a,b] subseteq[1,d-1]`, one may take

\[
 \lambda_z=b+1,qquad \rho_z=d-a+1,                           \tag{2.4}
\]

with the usual omission of a side occurrence at a boundary.  Then

\[
 \mathcal R_z={(u,v):1\le u\le b,\ 1\le v\le d-a,
                                      u+v\le d-1\}.           \tag{2.5}
\]

For the singleton zero set `{i}`,

\[
                            |\mathcal R_z|=i(d-i)-1.          \tag{2.6}
\]

#### Proof

Equation (2.2) proves (2.3).  On a destroyed cell `I_(i,d-i)`, absence is
the pair of inequalities

\[
                         i<\lambda_z,qquad d-i<\rho_z.
\]

Their integer solution set is `[d-rho_z+1,lambda_z-1]`, which gives (2.4)
and (2.5).  If `a=b=i`, the rectangle before the band restriction has
`i(d-i)` pairs.  Its unique pair with sum `d` is `(i,d-i)`; every other pair
has sum at most `d-1`.  Removing that one pair proves (2.6).  \(\square\)

### Corollary 2.2 (the singleton-omission code disturbs the whole triangle)

Let `z_1,...,z_(d-1)` be star coordinates and program `z_i` to be absent
from exactly `I_(i,d-i)`.  Then

\[
 \bigcup_{i=1}^{d-1}\mathcal R_{z_i}
   =\{(u,v):u,v\ge1,\ u+v\le d-1\}.                         \tag{2.7}
\]

The right side has cardinality `binom(d-1,2)`.

#### Proof

Take any `(u,v)` on the right.  The interval

\[
                              [u,d-v]
\]

is nonempty because `u+v<=d-1`.  Choose `i` in it.  Then `u<=i` and
`v<=d-i`, so `(u,v) in R_(z_i)` by (2.5).  The reverse inclusion is part
of the definition.  Finally

\[
 \sum_{s=2}^{d-1}(s-1)=\binom{d-1}{2}
\]

counts crossing intervals by their old length `s=u+v`.  \(\square\)

An especially short consequence is useful.  If the selected old pin on
`I_(1,1)` must transport, then every star coordinate belongs to its target.
It consequently belongs to every destroyed crossing cell.  Thus no star
coordinate can distinguish the destroyed bank.  Conversely, any nonconstant
star-coordinate trace forces at least that adjacent pin to move.

## 3. The closest compatible coatom bank

The preceding obstruction is not a claim that distinct destroyed values are
algebraically impossible.  It identifies their exact price.

Let `F={f_1,...,f_d}` and let `a,b` be outside `Z union F`.  Put

\[
                              U=Z\cup\{a,b\}\cup F.          \tag{3.1}
\]

Assume `z_1,...,z_(d-1)` are distinct elements of `Z`.  The two fan chains

\[
\begin{aligned}
 L_{h+1}&=Z\cup\{b,f_1,\ldots,f_h\},\\
 R_{h+1}&=Z\cup\{a,f_{d-h+1},\ldots,f_d\},
             \qquad1\le h\le d-1,                           \tag{3.2}
\end{aligned}
\]

can coexist with the distinct destroyed bank

\[
                              N_i=U-\{z_i\}.                 \tag{3.3}
\]

Indeed, retain every element of `Z-{z_1,...,z_(d-1)}` on one nearest side
source.  For `z_i`, put a copy at left distance `i+1` when `i<=d-2` and at
right distance `d-i+1` when `i>=2`.  The missing boundary occurrence is
simply omitted.  Then `z_i` has crossing trace one except at `i`, while the
extra copies do not alter either fan because all of `Z` is already at the
star.  Coordinates outside `Z` are forced by (3.2), and their union on every
destroyed cell is `{a,b} union F`.  This proves (3.3).

If `|U|=r`, the `N_i` are distinct rank-`r-1` targets.  This is the natural
q1-shaped crossing bank.  Corollary 2.2 shows that it changes the complete
shorter crossing triangle.  Moreover the new star-spanning owner at split
`i` is

\[
 T_i=Z\cup N_i=U,                                           \tag{3.4}
\]

so all `d-1` diagonal owners coincide.  An owner-complete chronology of
length `W+1` has total multiplicity excess one.  The plateau (3.4) alone has
excess `d-2`; hence it is impossible in that chronology for every `d>=4`.
For `d=3` it consumes the sole allowed duplicate, and for `d=2` there is no
plateau repetition; neither small case supplies the remaining carrier and
compiler rows automatically.

Thus star-coordinate coding can repair target distinctness or carrier
simplicity, but not both on the canonical complementary fans.  A viable
growing-depth seam must change the fan diagonals outside `Z`.

## 4. Exact carrier and singleton conditions

For arbitrary nested fan chains with common first value `Z`, define

\[
                         T_i=L_{i+1}\cup R_{d-i+1}.           \tag{4.1}
\]

By the star identity, these are exactly the new depth-`d` owner windows
which contain old positions on both sides of the inserted source.  There are
also two one-sided star windows, involving the next source at distance `d`,
and unaffected windows outside this local display.  Full carrier replay
must verify all of them.

For the internal mixed windows, a Johnson walk requires

\[
 |T_i|=r,qquad |T_i\cap T_{i+1}|=r-1                       \tag{4.2}
\]

at every internal join.  A simple Johnson segment additionally requires the
`T_i` to be pairwise distinct.  These conditions do not replace the two
one-sided owner and endpoint-join tests.  Marginal fan coverage implies none
of them.

Now freeze the nonstar source letters and all protected pins meeting the
star.  Assume their nonstar unions are already subsets of the corresponding
declared carrier owners and pin targets; otherwise no choice at the star can
repair the excess coordinate.  Let `P_*` be the maximal star envelope, and
define

\[
 M_*=\bigcup_{i:\,*\in[i,i+d]}
 \left(T_i-\bigcup_{p\in[i,i+d]-\{*\}}A_p\right),           \tag{4.3}
\]

\[
 M_{\rm pin}=\bigcup_{(I,S):*\in I}
 \left(S-\bigcup_{p\in I-\{*\}}A_p\right).                 \tag{4.4}
\]

### Theorem 4.1 (exact typed-star cap)

The singleton source may be set to the nonempty typed target `S_tau`, while
preserving every star-containing carrier window and protected pin, if and
only if

\[
 \boxed{
 M_*\cup M_{\rm pin}\subseteq S_\tau\subseteq
 P_*\cap\bigcap_{(I,S):*\in I}S,qquad S_\tau\ne\varnothing.}
                                                                    \tag{4.5}
\]

When the two fan chains have common minimum `Z` and the singleton is their
shared source, a literal typed fan socket has `S_tau=Z`.  Every selected
transported shorter crossing pin is included in the upper intersection in
(4.5), so Theorem 1.1 is exactly its triangular part.

#### Proof

For a star-containing carrier window, the nonstar sources supply the second
term in (4.3).  Equality with `T_i` holds exactly when the missing coordinates
are in `S_tau` and no coordinate outside `T_i` is introduced.  Intersecting
over the windows gives the carrier portion of (4.5).  A protected pin
`(I,S)` is identical: its nonstar union must be completed by `S_tau` to
exactly `S`, giving

\[
 S-\bigcup_{p\in I-\{*\}}A_p\subseteq S_\tau\subseteq S.
\]

Intersect over the pins and impose nonzeroness.  Conversely the displayed
inclusions verify every affected union directly.  \(\square\)

Pins not meeting the star still have their ordinary source-position and
positive-hit common-`Q` conditions.  Thus (4.5) is the complete star row,
not a replacement for the global common-`Q` replay.

## 5. Conditional one-credit theorem with the missing row restored

Let `O` be the `2(d-1)` old-chain targets assigned to the non-singleton
fans, let `N` be the `d-1` targets on the destroyed length-`d` cells, and
let `tau` be one exposed typed target.  Fix one terminal common-`Q` state.
Restrict first to the declared affected target/cell fibre, and write
`alpha_loc` for its augmenting number.  A return in this fibre is called
**basis-neutral** when it replaces one deleted old cell by one terminal cell
and exposes no additional target or sink.
The fibre is **closed** when its only unmatched target beyond the endpoints
of the `ell` deleted matching edges is `tau`, and its displayed terminal
cells contain no additional augmenting endpoint.

### Theorem 5.1 (literal one-credit criterion)

Suppose all of the following hold in that one state.

1. `O` is matched bijectively to `L_2,...,L_d,R_2,...,R_d`.
2. `N` is matched to distinct post-switch native cells.
3. Every selected shorter crossing pin violating (1.3), and every other
   pin displaced by the carrier switch, belongs to a family of pairwise
   vertex-disjoint basis-neutral alternating returns that restore their
   targets; this family is vertex-disjoint from all assignments in items 1,
   2, and 5.
4. The mixed diagonal owners (4.1), both one-sided star owners, all
   unaffected windows, endpoint joins, residence, and protected upper
   witnesses give the declared physical carrier.
5. The singleton realizes `tau` under (4.5), and all named target and cell
   occurrences are distinct.
6. The complete source word passes the ordinary nonzero/common-`Q` positive
   rows.
7. The declared affected fibre is closed in the preceding sense.

Then, relative to the retained old compiler matching,

\[
                         \alpha_{\rm loc}=\ell+1.             \tag{5.1}
\]

In the unrestricted terminal compiler graph this gives
`alpha>=ell+1`; equality there additionally requires that no further
exterior augmentation exists.

The one-cell insertion contributes exactly `d` net short cells.  The typed
singleton uses one, so the unused-address count rises by exactly `d-1`
relative to the old basis after the new target is covered.

#### Proof

Delete the old matching edges on `O`, on `N`, and on every additionally
displaced pin, obtaining the retained matching `M_0`.  Items 1--3 give a
terminal matching which restores every old matched target, and item 5 adds
the exposed target at the previously nonexistent star cell.  Thus this
terminal matching has size `|M_0|+ell+1`.  Items 4 and 6 say that all its
edges coexist in one legal terminal graph rather than only in its marginal
union.  Basis neutrality, closedness, and the fact that `tau` is the sole
added target give the matching-number upper bound `|M_0|+ell+1` in the
declared fibre.
The augmenting-linkage identity therefore gives
`alpha_loc=ell+1`.  The same matching is present in the unrestricted graph,
so its augmenting number is at least this large.

The short-band identity is

\[
                       (2d-1)-(d-1)=d.
\]

The target at the singleton consumes one of those `d` new address credits;
the unused-address count therefore increases by `d-1` relative to the old
basis.  \(\square\)

Without item 3, the scalar count using only `O,N` is incomplete.  Without
item 4, the canonical complementary fan word has a constant owner plateau.
Without item 5, the fan bank merely restores the deleted matching and gives
`alpha_loc=ell`.  Without item 6, separate marginal incidences can belong to
incompatible cap states.

## 6. Consequence for the canonical coatom proposal

For the corrected opposite native/boundary orientation, the canonical OLD
fans have the form (3.2).  Equation (0.1) forces every destroyed crossing to
contain `{a,b} union F` outside `Z`.  A canonical NEW prefix target omits
`b` and a canonical NEW suffix target omits `a`; each also contains only a
proper filler prefix or suffix.  Therefore no destroyed crossing is a
canonical NEW target, already for `d=2`.

For `d>=3`, the diagonal owners are all the same set `U`, and for `d>=4`
the multiplicity argument following (3.4) rules out an owner-complete
`W+1` carrier.  The fresh-q1 endpoint transporter supplies a separate
endpoint-contained q1 occurrence, but it neither changes (0.1) nor returns
the triangular collar.  It cannot be counted as the missing star credit.

The exact live construction target is therefore a **noncanonical diagonal
fan braid** satisfying (4.2), together with

* a compatible rank-`r-1` destroyed bank and post-switch native injection;
* a return for the selected triangular crossing pins described by (2.3);
* the typed-star cap (4.5); and
* one terminal common-`Q`, residence, upper-shadow and q1-sidecar replay.

This is a finite, occurrence-labelled exterior-ear condition.  It is
strictly stronger than the marginal assertion that the fan has one excess
cell, and it is the precise proved/conditional boundary for the proposed
`B(k)+1` macro.

## 7. Independent proof audit

Three independent proof passes checked the seam equations, the canonical
coatom orientation, the singleton cap, and the matching ledger.  They agreed
on the following points.

1. The fan carving and gross count are exact.
2. Canonical OLD fans cannot self-repay canonical NEW targets.
3. The star-coordinate trace has interval zero sets, but every selected
   shorter crossing pin imposes the additional triangular condition (1.3).
4. The fresh-q1 transporter is a separate endpoint occurrence and does not
   remove the triangular or diagonal-owner gates.
5. `alpha_loc=ell+1` is valid exactly under the seven simultaneous hypotheses
   of Theorem 5.1; it is not an unconditional consequence of cardinality.

The dependency-free replay

```text
scratch/audit_k_one_cell_typed_star_triangular_collar_20260801.py
```

checks the fan/crossing source word, every singleton rectangle, their union
with the full shorter crossing triangle, and the constant diagonal owner for
every `2<=d<=40`.  It reports

```text
PASS_K_ONE_CELL_TYPED_STAR_TRIANGULAR_COLLAR d=2..40
payload_sha256=5345f99c9ca570fdae8b4b1b4fba229b1e5d881c2867db2d13ec6c69ffad7ba5
```

The script SHA-256 is
`67c2c86d0282363ec48df5e299c23c8979c2097757c4d71e8fa117eee09aed9d`.

Dependencies:

* `MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`;
* `MATH_THEOREM_COATOM_TWO_PHASE_BOUNDARY_CHAIN_CARVING_20260801.md`;
* `MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`;
* `MATH_THEOREM_AD_ONE_CELL_TWO_FAN_EXACT_EAR_HALL_CUT_20260801.md`;
* `MATH_AUDIT_AD_ONE_CELL_TWO_FAN_COMMONQ_STAR_GATE_20260801.md`; and
* `MATH_THEOREM_COATOM_BOUNDARY_STAR_FAN_COMBINATION_NOGO_20260801.md`;
* `MATH_THEOREM_A_ONE_CELL_STAR_HIDDEN_TWO_FAN_COMMONQ_20260801.md`.
