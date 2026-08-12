# `C8` host placement: the all-depth interior obstruction and boundary-recut gate

Date: 2026-08-01  
Lane: folded `C8` physical lift / coherent chainization actuator  
Status: all-`d` interior no-go; exact scoped boundary census for `2<=d<=12`;
connector/rethread embedding remains open.

## 0. Verdict

The two folded `C8` ray hosts cannot be planted as independent internal
letters of a flat resident depth-`d` carrier.  This is not a failure of the
particular folded word: it follows from a general `d`-deletions-versus-`d-1`
link obstruction.

The obvious escape is to make the two typed hosts the clipped ends of one
cyclic boundary rail.  Exhaustively recutting the authenticated
upper-complete folded Hamilton cycles does **not** do this: among all common
cuts and both orientations which retain the exact two-ray support, the four
phase-labelled bases remain at distance `Theta(d)` from the path boundary.
Thus the existing cycles need a genuine connector/rethread (or the already
proved one-deadline-jump nonflat interface); rotation alone is insufficient.

In the current general reduction, the desired object should be viewed as a
**chainization actuator**: an owner-legal recyclable boundary rail which
performs one adjacent antitone comparator while preserving the nested
endpoint-chain realization.  Abstract comparator Hall is no longer the
obstruction.  Physical boundary regeneration is.

## 1. General flat-host obstruction

Let

\[
 A=(A_0,\ldots,A_{N+d-1}),\qquad
 T_i=\bigcup_{j=i}^{i+d}A_j\quad(0\le i<N),             \tag{1.1}
\]

and suppose every `T_i` has rank `r` and consecutive distinct owners form a
Johnson path.  Say the owner path is **depth-`d` resident** if every internal
coordinate run in `T` has length at least `d+1`.

### Theorem 1.1 (interior host/link obstruction)

Suppose `d>=1`, `d<=p<=N-1`, and

\[
                         |A_p|=r-d+1.                  \tag{1.2}
\]

If the complete owner block

\[
                  T_{p-d},T_{p-d+1},\ldots,T_p          \tag{1.3}
\]

is internal in the linear owner path, then (1.1) cannot be a depth-`d`
resident Johnson path.

#### Proof

Put `X=A_p`.  Every one of the `d+1` owners in (1.3) contains `X`.  Hence

\[
                 B_i=T_{p-d+i}\setminus X
                 \quad(0\le i\le d)                    \tag{1.4}
\]

has size `d-1`.  There are `d` Johnson transitions in (1.3).  At each
transition one coordinate outside `X` is deleted.

No coordinate inserted during these `d` transitions can be deleted again
before the end of the block.  Such an insertion and deletion would delimit
an internal owner run of length at most `d-1`, contradicting residence.
Consequently every deleted coordinate was already in `B_0`.  The deleted
coordinates are distinct: deleting one twice would require reinserting it
between the two deletions, which is the same forbidden short run.

Thus the `d` transitions require `d` distinct deleted coordinates from the
`(d-1)`-set `B_0`, a contradiction.  \(\square\)

### Corollary 1.2 (where a sharp host may live)

A source host of rank `r-d+1` in a flat resident carrier must satisfy at
least one of the following:

1. its owner block is clipped by a global path boundary;
2. the owner chronology is rethreaded so that the recycled short run crosses
   the global cut and is therefore a clipped boundary run;
3. one allows the proved nonflat width-`d+2` full-block lift, i.e. a one-step
   deadline jump; or
4. the entire erosion is recomputed in a different owner chronology.

In particular, two independent internal typed hosts cannot realize the
folded prefix/suffix rays inside an otherwise fixed flat carrier.

The theorem is only a necessity statement.  A boundary cut removes the
contradiction by permitting a recycled coordinate run to be clipped; it does
not by itself prove the palettes, upper witnesses, topology or compiler.

## 2. Exact folded base geometry

For the authenticated owner-value quotient, the owner path has `8d+24`
vertices and its maximal linear erosion has length

\[
                              n=9d+24.                  \tag{2.1}
\]

Write `p^-_L,p^+_L` for the old/new prefix-base positions and
`p^-_R,p^+_R` for the old/new suffix-base positions.

The three useful cut faces are distinct:

* minimum graded discrepancy: `L1=6d+4`, upper support fifteen, with
  \[
  (p^-_L,p^+_L)=(3d+6,7d+18),\qquad
  (p^-_R,p^+_R)=(2d+6,6d+18);                           \tag{2.2}
  \]
* aligned bases: `L1=10d+12`, upper support fifteen, with
  \[
  p^-_L=p^+_L=4d+12,\qquad p^-_R=p^+_R=5d+12;           \tag{2.3}
  \]
* upper-safe: upper support sixteen and minimum `L1=10d+20`, but without
  a fixed pair of aligned source slots.

All three have the same two directed distinct-support rays.  Equations
(2.2)--(2.3) concern full graded occurrence multiplicity and physical
addresses, so they cannot be interchanged merely because the support rays
agree.

There is a second distinction which is equally load-bearing.  Here
**upper-complete means support-complete**: all sixteen local upper `q1`
values occur, and the complete old/new cycles have the same upper
multiplicity counter.  It does not mean that every upper colour occurs once.
The folded cycle has `8d+24` edges, so it is not an exact upper-colour
transversal of the sixteen-value local bank.

Consequently there are two possible uses of the actuator:

* in the universal-support route, phase-common repeated upper witnesses are
  allowed and the folded upper row is already sufficient;
* in a strict Catalan-selector route, a separate occurrence allocation must
  choose one physical representative per upper colour and preserve the side
  forest.  Support completeness alone does not supply that exact selector.

Nothing below silently upgrades support completeness to outer-palette
exactness.

## 3. Boundary-recut census

For four base positions `(p^-_L,p^+_L,p^-_R,p^+_R)` in a source word of
length `n`, define the paired boundary radius

\[
\begin{split}
 b=\min\{&\max(p^-_L,p^+_L,n-1-p^-_R,n-1-p^+_R),\\
          &\max(n-1-p^-_L,n-1-p^+_L,p^-_R,p^+_R)\}.    \tag{3.1}
\end{split}
\]

This is the smallest collar radius which puts both phase-prefix bases at
one end and both phase-suffix bases at the other.  A literal endpoint host
is the radius-zero/one ideal; an `O(1)` recyclable boundary interface
requires `b=O(1)`.

### Theorem 3.1 (no boundary host by common recut, audited range)

For every `2<=d<=12`, first take the two upper-complete folded Hamilton
cycles in each phase.  Among every old/new pair, every common-edge cut, and
both path orientations whose maximal inverses have exactly the two
prescribed ray support differences,

\[
                         \min b=4d+12.                  \tag{3.2}
\]

Restricting further to cuts which retain all sixteen upper `q1` values gives

\[
                         \min b=4d+13.                  \tag{3.3}
\]

Hence no such recut puts the bases in even the first/last `d` erosion
positions.  The best support-fifteen cut is exactly the aligned-base face
(2.3).

The stronger all-cycle census gives the same answer.  It ranges over all
sixteen lower-rainbow degree-two Hamilton cycles in each phase, every common
cut and both orientations for which all four typed bases occur as literal
source singletons.  Again the minimum is `4d+12`; moreover the minimizer is
already upper-complete and has the exact two-ray support.  Thus relaxing the
upper palette inside this complete quotient degree-two class does not move
the hosts toward the boundary.

Even the same-endpoint requirement is not responsible.  Cutting each phase
cycle independently, and minimizing the two-base boundary radius in that
phase over all sixteen cycles, all edges and both orientations, still gives
`4d+12` in both phases.  Therefore an independent opening followed by a
passive connector does not expose the native bases either.  The connector
must first change the owner/source threading, or the construction must use
the nonflat deadline-jump interface.

#### Scope

This is an exhaustive finite theorem for the authenticated folded cycles in
the stated depth range.  It excludes rotation/reorientation of the existing
upper-complete cycle pair as the missing physicalization.  It does **not**
exclude:

* a connector which actively rethreads the quotient owner/source rail;
* leaving the complete quotient degree-two class during a connector move;
* a bounded-palette-sidecar rethread;
* a nonflat one-deadline-jump packet; or
* a different Catalan owner factor selected jointly with the actuator.

The replay was run on the remote CPU host.  Files:

```text
scratch/explore_c8_folded_boundary_base_census_20260801.py
  SHA-256 7f7bd1e0de93b0ca0d8e649a71926febe78d4930c79c343df8e5cb85b5748884
scratch/c8_folded_boundary_base_census_d2_d12.json
  SHA-256 ba5c2cc1ebe9e58a08bbc38b02379af82ee42ca49586e568d10b4c3e044eb230
scratch/explore_c8_folded_allcycle_boundary_singletons_20260801.py
  SHA-256 11c620d13bd0b35f6c13f5bbcce981383bf69f1ab17aa167c848aebb201f23e3
scratch/c8_folded_allcycle_boundary_singletons_d2_d12.json
  SHA-256 54d2b8279d317dbf8a91bc6f5a714a76247486df11d97046c092f4cfa85bbfae
scratch/explore_c8_folded_independent_boundary_singletons_20260801.py
  SHA-256 98f310dbdb5cd318f95820142c0947396c82c81202cfd9b36f050785e7f20052
scratch/c8_folded_independent_boundary_singletons_d2_d12.json
  SHA-256 b9ac790469cca3a9c55fdc5c80cb4ed1caaf112567e2502c52236de4200c1a8d
```

### Theorem 3.2 (one clean socket exists, but carries no ray rail)

Put

\[
                         X=K\cup\{z,a_1,a_3\}.          \tag{3.4}
\]

This is the smaller one-host value of the nonflat construction.  For every
audited `2<=d<=12` and for both phases, an upper-complete resident quotient
Hamilton path has a maximal-erosion endpoint whose replacement by `X`
leaves the owner path exactly unchanged.  For `d>=3` the complete census has
eight such phase-path records, and the best occurrence is at source position
zero.

This positive fact is one-sided:

1. no audited quotient path permits owner-preserving replacement of **both**
   source endpoints by `X` simultaneously;
2. splitting the one legal endpoint into
   `({z,a_3},{z,a_1})` in either order loses no old interval-OR support and
   adds exactly three values per phase; but
3. no common old/new endpoint split supplies either complete opposite
   prefix ray or complete opposite suffix ray.  The best remaining support
   difference is `6d-5` values in each direction.

Thus the native physical socket is present; the nested filler rail is not.
The missing connector should be described as **transporting a ray rail to an
existing boundary socket**, rather than manufacturing the host value itself.
The current one-end shrink/split is support-safe but is not yet an adjacent
antitone comparator.

Remote replay files:

```text
scratch/explore_c8_onehost_source_availability_20260801.py
  SHA-256 e164410dbd9de482bacf87e0db029c132d0bdfd42581fde5a1bf0ee395f3414d
scratch/c8_onehost_source_availability_d2_d12.json
  SHA-256 7bfdfcfaf1783b2a2812520f403705d4f6da9aa00247a5893201562fa29c92d5
scratch/explore_c8_onehost_boundary_pair_20260801.py
  SHA-256 ca5c0e054b4b1e3746f983922aa76c81f7b43205e670e4e2a3a7a7a1317248dd
scratch/c8_onehost_boundary_pair_d2_d12.json
  SHA-256 dee71a3d6592b95fcb5901cc0f00737370f8f20451c3559e5ca7b1f7564252d2
scratch/explore_c8_onehost_common_endpoint_ray_20260801.py
  SHA-256 d02e2445bc0bb673dc6a9733fd464f00f72e9c8d60b1aae6caf38fdafa70cd65
scratch/c8_onehost_common_endpoint_ray_d2_d12.json
  SHA-256 a9e5021183570d1527b5be2feb2b51ae5099812e51648644d8c2ce32f20a7e84
```

## 4. Exact remaining chainization actuator

The shortest positive target is now the following.

> **Folded boundary-comparator lemma.**  There is an owner-legal rethread of
> the quotient-folded `C8` pair which transports the two nested filler rays
> to one or two clean boundary sockets (including the native socket (3.4)),
> places the opposite phase bases beside the appropriate socket endpoints,
> and has the following properties:
>
> 1. all owners retain rank `r`, are simple, and have cap-two physical degree;
> 2. the lower and upper immediate palettes are preserved up to `O(1)` named
>    sidecars in the universal-support sense; if used inside a strict Catalan
>    selector, the selected upper occurrences remain injective as well;
> 3. every internal coordinate run remains at least `d+1`, with the one
>    necessary recycled link coordinate crossing the global cut;
> 4. contraction restores the old rail and its protected witnesses;
> 5. the two nested endpoint chains are transported by the adjacent
>    antitone comparator; and
> 6. the protected background matching loses only the named sidecar cells.

The local algebra after such a rail exists is already closed: the two-host
module gives the exact ray cells and pointwise cap, and the antitone-birail
theorem gives zero abstract terminal Hall deficiency.  What remains is the
physical connector in this lemma.

The all-depth obstruction above explains why the connector must be genuinely
boundary-stateful.  The finite census explains why it cannot be obtained by
merely choosing a better cut of the present upper-complete cycles.
