# `k=17`: exact phase reduction, witness cores, and lazy rows for an upper-safe `Z_17` opening

Date: 2026-08-01  
Lane: AD, nonwrapping strict-upper linearization of a `Z_17`-equivariant owner cycle  
Status: unconditional opening theorem and exact finite certificates.  No upper-safe cycle is constructed.

## 0. Outcome

Let `rho` be coordinate rotation on `[17]`, and let `C` be a
`rho`-equivariant Hamilton cycle on all rank-nine owners.  Assume its
quotient has length

\[
                         N={1\over17}{17\choose9}=1430
\]

and primitive voltage `V in Z_17^*`.  A physical opening is one physical
copy of one quotient edge, not the whole edge orbit.

The exact conclusions are as follows.

1. For a fixed quotient edge index, all seventeen physical opening phases
   are equivalent under simultaneous coordinate rotation.  Thus one may
   normalize the physical phase to zero.  This does **not** identify the
   1430 quotient edge indices.
2. For every proper upper-target orbit and every quotient cut index there
   is an exact **lost-phase core**: the intersection of the crossing-phase
   sets of all normalized cyclic witness orbits.  The opening is safe
   exactly when every such intersection is empty.
3. A rank-`s` proper target witness contains at most `binom(s,9)` distinct
   owners.  Consequently one witness crosses a fixed quotient edge orbit
   in at most

   \[
   b_s=\left\lceil {\binom{s}{9}-1\over1430}\right\rceil
   \]

   phases.  For ranks `10,...,16`, these bounds are

   \[
                         1,1,1,1,2,4,8.              \tag{0.1}
   \]

   Hence a complete safe-opening certificate needs at most 4921 normalized
   quotient witness rows, rather than 41225 separate proper physical
   targets.
4. Rank ten has a sharper exact rule.  Cyclic rank-ten coverage is required
   first.  After that, cutting an edge is rank-ten safe iff the upper-colour
   orbit of that quotient edge occurs on at least two selected quotient
   edges.  This yields an exact presolve/lazy inequality.
5. A solver rooted at a quotient edge must still expand seventeen helical
   quotient laps.  Deleting the quotient edge orbit would delete seventeen
   physical edges and is an invalid strengthening.

The saved strict-spiral MMM cycle is a useful negative calibration, not the
desired decorated cycle.  It has voltage one and a perfect lower rank-eight
rainbow, but already has 2516 cyclic rank-ten holes, so no physical opening
of it can be upper-safe.

## 1. Voltage-gauged physical cycle

Choose quotient owner representatives `R_0,...,R_(N-1)` and labelled edge
voltages `delta_i`.  Put

\[
 p_0=0,\qquad p_i=\sum_{j<i}\delta_j,\qquad
 V=p_N\pmod {17}.                                    \tag{1.1}
\]

After a harmless gauge choice, the physical owner in quotient slot `i` on
lap `a` is

\[
                         T_{a,i}=\rho^{aV+p_i}R_i.    \tag{1.2}
\]

Because `V` is nonzero and 17 is prime, `(a,i)` for
`a in Z_17, 0<=i<N` traverses one cycle of length `17N=24310`.

Write `e_i^g` for the physical edge in quotient edge orbit `i` whose chosen
tail representative has phase `g`.  Coordinate rotation acts by

\[
                         \rho^t e_i^g=e_i^{g+t}.      \tag{1.3}
\]

### Theorem 1.1 (opening-phase symmetry)

For the target family consisting of all masks of ranks `10,...,17`, the cut
at `e_i^g` is upper-safe iff the cut at `e_i^0` is upper-safe.  More
precisely,

\[
  S\text{ is lost at }e_i^0
  \quad\Longleftrightarrow\quad
  \rho^g S\text{ is lost at }e_i^g.                 \tag{1.4}
\]

#### Proof

Rotation `rho^g` is an automorphism of the owner cycle, takes contiguous
owner intervals to contiguous owner intervals, commutes with union, and
takes the cut `e_i^0` to `e_i^g`.  It therefore bijects the surviving
witnesses on the two opened paths and rotates their targets.  The full
rank family is rotation-invariant.  This proves (1.4) and the safety
equivalence. `square`

The WLOG is exactly phasewise.  It is valid with labelled anchors only if
the anchors, boundary macro, forbidden resources, and compiler state are
rotated simultaneously.  A fixed distinguished coordinate can break it.

Reindexing an unrooted quotient cycle can name a *chosen* safe edge as the
last quotient edge.  It does not prove that a previously fixed edge is
safe, and it does not identify distinct quotient edge orbits in a rooted
model.

## 2. The physical witness core and a rejection certificate

Let `e` be a physical cycle edge.  For an upper target `S`, let
`W_C(S)` be the family of oriented cyclic owner intervals whose union is
`S`.  The interior of such an interval is the set of cycle edges traversed
between its first and last owner.  A full-cycle interval rooted at one
owner has `24309` interior edges and omits its rooted boundary edge.

Set

\[
 \mathfrak b_C(S)=
 \begin{cases}
 \displaystyle\bigcap_{I\in W_C(S)}\operatorname{int}(I),
       &W_C(S)\ne\varnothing,\\[1ex]
 E(C),&W_C(S)=\varnothing.
 \end{cases}                                         \tag{2.1}
\]

Then the cyclic-recut theorem gives

\[
 S\text{ survives cut }e
       \quad\Longleftrightarrow\quad e\notin\mathfrak b_C(S). \tag{2.2}
\]

There is an equivalent certificate which does not enumerate all
intervals.  Delete `e` and write the opened owner path as
`T_0,...,T_(W-1)`.  For a fixed `S`, split the positions satisfying
`T_i subseteq S` into maximal consecutive blocks `B`.

### Lemma 2.1 (maximal compatible blocks)

The target `S` survives iff some maximal `S`-compatible block satisfies

\[
                         \bigcup_{T\in B}T=S.         \tag{2.3}
\]

Thus a rejection certificate for `S` consists of the maximal compatible
blocks and, for every block `B`, one coordinate

\[
                    x_B\in S-\bigcup_{T\in B}T.      \tag{2.4}
\]

#### Proof

Every interval with union `S` consists only of owners contained in `S`, so
it lies in one maximal compatible block.  Conversely a block satisfying
(2.3) is itself an interval witness.  Formula (2.4) proves that no block
can be a witness. `square`

For a proper `S`, the compatible owners do not fill the whole Hamilton
cycle.  If there is exactly one cyclic compatible block `B=[a,b]` whose
union is `S`, put

\[
 \ell_S=\max\{\ell:\bigcup_{i=\ell}^{b}T_i=S\},
 \qquad
 r_S=\min\{r:\bigcup_{i=a}^{r}T_i=S\}.              \tag{2.5}
\]

Then

\[
        \mathfrak b_C(S)=\{e_t:\ell_S\le t<r_S\}.   \tag{2.6}
\]

If at least two cyclic compatible blocks have union `S`, their witness
interiors are disjoint and the core is empty.  If no block covers `S`, the
core is all edges by the convention in (2.1).

To prove (2.6), observe that `ell_S` is the largest possible left endpoint
of a witness and `r_S` is the smallest possible right endpoint.  An edge
belongs to every witness interior exactly when it is weakly to the right of
every left endpoint and strictly to the left of every right endpoint.

## 3. Quotient lost-phase cores

Fix one representative `U` of a proper target orbit.  Every witness orbit
under `rho` has a unique normalization `I` with

\[
                              \operatorname{OR}(I)=U, \tag{3.1}
\]

because a nonempty proper subset of `[17]` has trivial stabilizer.

For a normalized witness `I` and quotient edge orbit `i`, define

\[
 P_i(I)=\{-g:e_i^g\in\operatorname{int}(I)\}
                  \subseteq Z_{17}.                 \tag{3.2}
\]

Rotating `I` by phase `p` gives a witness for `rho^pU`; it crosses the
normalized physical cut `e_i^0` exactly when `p in P_i(I)`.  Define the
lost-phase core

\[
 L_i(U)=\bigcap_{I:\operatorname{OR}(I)=U}P_i(I),    \tag{3.3}
\]

with intersection of an empty witness family equal to all of `Z_17`.

### Theorem 3.1 (exact quotient opening test)

For every proper target orbit representative `U`,

\[
 \rho^pU\text{ is lost at }e_i^0
       \quad\Longleftrightarrow\quad p\in L_i(U).    \tag{3.4}
\]

Consequently `e_i^0` is upper-safe iff

\[
              L_i(U)=\varnothing
 \quad\text{for every target-orbit representative of ranks }10,...,16.
                                                               \tag{3.5}
\]

Rank seventeen needs no row: the entire opened Hamilton path has union
`[17]` and is a nonwrapping witness.

#### Proof

The witnesses of `rho^pU` are exactly the rotations `rho^pI` of the
normalized witnesses in (3.1).  Such a witness crosses `e_i^0` iff one of
its interior edges is `e_i^0`, equivalently iff an edge `e_i^{-p}` belongs
to `int(I)`, which is `p in P_i(I)`.  The target is lost precisely when
this holds for every normalized witness.  This is (3.3)--(3.4).  Intersect
over target phases and orbits to get (3.5).  The full target is witnessed
by the whole opened path. `square`

This theorem explains why checking one representative target per orbit is
wrong after opening.  Phase normalization fixes the cut; it leaves all
seventeen relative target phases to be checked.

## 4. Bounded crossing and the 4921-row certificate

### Lemma 4.1 (rank bound)

If `|U|=s<17`, every owner in a `U`-witness is one of the
`binom(s,9)` rank-nine subsets of `U`.  Since the Hamilton cycle has no
repeated owner, a witness contains at most `binom(s,9)` owners and at most
`binom(s,9)-1` interior edges.  Along the physical lift, quotient edge
indices repeat every `N=1430` edges.  Therefore

\[
                         |P_i(I)|\le b_s
   =\left\lceil{\binom{s}{9}-1\over1430}\right\rceil. \tag{4.1}
\]

For `s=10,...,16`, this gives the table

| rank `s` | target orbits | `binom(s,9)` | `b_s` | witnesses sufficient to certify `L_i(U)=empty` |
|---:|---:|---:|---:|---:|
| 10 | 1144 | 10 | 1 | 2 |
| 11 | 728 | 55 | 1 | 2 |
| 12 | 364 | 220 | 1 | 2 |
| 13 | 140 | 715 | 1 | 2 |
| 14 | 40 | 2002 | 2 | 3 |
| 15 | 8 | 5005 | 4 | 5 |
| 16 | 1 | 11440 | 8 | 9 |

Indeed, choose one normalized witness `I_0`.  If `P_i(I_0)` is empty, it
alone proves an empty intersection.  Otherwise, for every
`p in P_i(I_0)`, emptiness of the total intersection supplies a witness
`I_p` with `p notin P_i(I_p)`.  The bank

\[
                          \{I_0\}\cup\{I_p:p\in P_i(I_0)\} \tag{4.2}
\]

has at most `b_s+1` rows and already has empty phase intersection.

Summing the last column times the number of target orbits gives

\[
 2(1144+728+364+140)+3(40)+5(8)+9(1)=4921.          \tag{4.3}
\]

Thus one fixed opening of one fixed equivariant Hamilton cycle has a
machine-checkable all-ranks upper-safety certificate with at most 4921
normalized witness rows, plus the trivial whole-path rank-seventeen row.
Each row records target representative, start state, length, accumulated
voltage, and its set (3.2).  The verifier checks the literal owner union and
the empty intersections.  This is a certificate-size theorem, not an
existence theorem.

For ranks ten through thirteen, `P_i(I)` is empty or a singleton.  Hence a
target orbit is safe at a cut as soon as one witness avoids the edge orbit,
or two normalized witnesses cross it in different relative phases.

## 5. The exact rank-ten opening row

For a rank-ten target `U`, its rank-nine facets form the ten vertices of
`J(U,9)=K_10`.  Two consecutive distinct owners contained in `U` have union
`U`.  Hence the cyclic witnesses of rank ten are exactly the cycle edges
whose upper colour is `U`, up to harmless extension inside the same
`U`-compatible block.

### Corollary 5.1 (rank-ten presolve)

A physical cut edge `e` is safe at rank ten iff:

1. every rank-ten target occurs on at least one cyclic edge; and
2. the upper colour of `e` occurs on at least one other cycle edge.

In the `Z_17` quotient, write `c(a)` for the upper-colour orbit of a
selected labelled quotient edge occurrence `a`.  If `x_a` selects `a` and
`o_a` selects it as the opening edge orbit, the exact rank-ten rows are

\[
 \sum_{a:c(a)=U}x_a\ge1
       \quad\text{for every rank-ten orbit }U,        \tag{5.1}
\]

\[
 o_a\le \sum_{b\ne a:\ c(b)=c(a)}x_b.               \tag{5.2}
\]

Here `b` means a distinct selected quotient-edge occurrence.  Catalogue
alternatives at one quotient slot are not two providers unless both can
actually be selected, and parallel voltages must retain their literal
upper-colour labels.

There is also a small quantitative reserve.  A fixed physical rank-ten
target has only ten rank-nine facets, each of cycle degree two, so its edge
multiplicity is at most ten.  A complete quotient rank-ten palette uses
1144 colours on 1430 quotient edges and has excess 286.  If `d` colours are
duplicated, then `286<=9d`, so `d>=32`; the number of rank-ten-safe quotient
cut edges is

\[
             \sum_{U:\mu(U)\ge2}\mu(U)=286+d\ge318. \tag{5.3}
\]

This guarantees many rank-ten-safe candidates only.  Higher ranks can
still reject all of them.

## 6. Exact lazy clauses for ranks ten through seventeen

Suppose a variable-cycle model has:

* one-hot opening variables `o_a` on selected labelled quotient-edge
  occurrences;
* exact interval-orbit variables `w_I`, where `w_I=1` is channelled to the
  complete contiguous physical occurrence of normalized witness `I`; and
* a complete candidate family for each target orbit.

For every proper target representative `U`, phase `p in Z_17`, and opening
candidate `a`, the exact opening clause is

\[
 \boxed{
  \neg o_a\ \vee\!
  \bigvee_{I:\operatorname{OR}(I)=U,\ p\notin P_a(I)} w_I.}   \tag{6.1}
\]

If `o_a=1`, clause (6.1) chooses a literal noncrossing witness for
`rho^pU`.  Conversely every surviving witness appears in the complete
candidate family, so (6.1) is necessary.  The ranks have respectively

\[
 19448,12376,6188,2380,680,136,17,1                 \tag{6.2}
\]

physical targets.  Rank seventeen is automatic; the 41225 proper-target
rows can be generated lazily.

An equivalent exact implementation roots the physical lift at the proposed
cut and runs the accumulated-union automaton for each target.  For target
`U`, a scan state is inactive, done, or the nonempty set of coordinates of
`U` still missing from the current maximal suffix of owners contained in
`U`.  Acceptance is exactly existence of a compatible block satisfying
(2.3).

For a fixed physical path there is a linear-size exact oracle.  At each
owner start, record the first later occurrence of each of the at most eight
coordinates missing from that rank-nine owner.  The accumulated union can
change only at these first-arrival positions.  Sorting them therefore
enumerates every distinct prefix union from that start in at most eight
events, for at most

\[
                              8W=194480              \tag{6.3}
\]

events over the whole path.  The maximal-compatible-block scan in Lemma 2.1
then supplies an exact rejection trace; no quadratic witness enumeration is
needed.

For a fixed incumbent cycle and fixed cut, a missing-target oracle returns
the block certificate (2.4).  If the cycle remains variable, the unit clause
`not o_a` is generally invalid: another cycle using the same root arc may
create a witness.  Sound choices are either:

1. add the exact acceptance row (6.1) or its automaton encoding; or
2. guard the no-good by every labelled successor/voltage/order choice whose
   conjunction fixes the incumbent physical cycle.

## 7. The helical-root trap

Selecting quotient edge orbit `a_*` as the root and normalizing one physical
copy to phase zero does **not** remove the other sixteen copies.  The opened
physical path consists of seventeen quotient laps joined by sixteen rotated
copies of `a_*`; only the seventeenth copy is absent.  Sheet phases advance
by the primitive voltage `V`.

Therefore the following purported opening checks are unsound:

* delete `a_*` from every quotient lap and test seventeen disjoint paths;
* forbid every witness which uses the quotient edge orbit of `a_*`; or
* test only one target representative per target orbit.

The phase sets (3.2) retain exactly which physical copies a witness uses.
They are the smallest quotient correction to those three errors.

## 8. Scoped audit of the saved strict-spiral cycle

The lightweight independent checker

`scratch/audit_ad_k17_z17_opening_phase_core_20260801.py`

reads the physical middle-level cycle from
`scratch/k17_mmm_middle_cycle_source_20260801.zip` and the quotient from
`scratch/k17_mmm_quotient_cycle.tsv`.  It verifies 24310 distinct rank-nine
owners, 24310 distinct rank-eight intersections, quotient period 1430, and
voltage one.  Its cyclic upper-owner-interval deck is:

| rank | covered | total | holes | quotient holes |
|---:|---:|---:|---:|---:|
| 10 | 16932 | 19448 | 2516 | 148 |
| 11 | 9656 | 12376 | 2720 | 160 |
| 12 | 4811 | 6188 | 1377 | 81 |
| 13 | 2006 | 2380 | 374 | 22 |
| 14 | 629 | 680 | 51 | 3 |
| 15 | 136 | 136 | 0 | 0 |
| 16 | 17 | 17 | 0 | 0 |
| 17 | 1 | 1 | 0 | 0 |

At rank ten the quotient colour-load histogram is

\[
                         562\cdot1+434\cdot2=1430,   \tag{8.1}
\]

with 148 omitted colour orbits.  Thus 868 quotient edge occurrences have a
duplicate rank-ten provider, but **no** opening is upper-safe because cyclic
coverage itself already fails.  The smallest displayed missing physical
target is `0x07fd`.

Authenticated hashes at this audit are:

```text
scratch/k17_mmm_middle_cycle_source_20260801.zip
  5a63a50e207bc9b55724a94cc4716ae57e8aa467b5a13797f7ea144d642c9a4e
scratch/k17_mmm_quotient_cycle.tsv
  4439b89f56b513416a418cbe0f7e8d9fa9e1bff9538ff432c497aa8cb473145f
scratch/audit_ad_k17_z17_opening_phase_core_20260801.py
  c34053c5bdb776eb4fd01113514abc401209b6cafc5c4f70626a51e9efe477e6
scratch/ad_k17_z17_opening_phase_core_20260801.audit.json
  5c6bc274f22914196280a7a8a8c3a6274d29616f1d0350d890b0f1984a279f88
```

This negative result is scoped to the saved MMM strict spiral.  It is not a
counterexample to existence of another decorated `Z_17` quotient cycle.

## 9. Scope and remaining gate

For the depth-three age lift in this note, the theorem decides the complete
strict-upper literal source deck, not merely a sufficient owner subclass.
After cutting before `E_s`, the literal word is

```text
E_s,...,E_(s+W-1),E_s,E_(s+1),E_(s+2).
```

Every source interval of length at least four is exactly the union of its
nonwrapping four-letter owner windows, and conversely.  Every source interval
of length at most three is contained in a rank-nine owner and therefore has
rank at most nine.  The owner order begins at `T_(s+3)`; this offset is
essential.  Hence no cut-crossing strict-upper source exception survives
the three-letter tail.

It also assumes a fully labelled primitive-voltage Hamilton lift.  Support
arcs without voltage labels do not determine the phase sets.  For composite
group order, nonzero voltage would not imply one physical cycle.

The exact next finite gate is therefore clear.  Build a cyclically
upper-complete labelled quotient Hamilton cycle, impose (5.1)--(5.2), root
one selected quotient edge orbit, and lazily separate (6.1) on the full
seventeen-sheet helical lift.  If the oracle accepts, the at-most-4921-row
bank (4.2) is a compact independently replayable complete strict-upper
certificate for the literal `W+3` source.  Lower common-cap compilation,
boundary macros, and final universal-word verification remain separate
simultaneous rows.
