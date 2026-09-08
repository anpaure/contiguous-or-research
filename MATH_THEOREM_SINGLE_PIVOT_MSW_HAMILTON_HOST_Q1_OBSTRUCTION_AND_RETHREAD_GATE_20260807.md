# The single-pivot MSW Hamilton host has a Catalan upper-q1 obstruction

**Date:** 2026-08-07  
**Method:** exact transfer of the canonical MSW upper-`q2` obstruction through
the endpoint-preserving MSW/MNW Hamiltonization; no computation or search  
**Status:** unconditional no-go theorem for the fixed-half MSW host.  It does
not rule out a rethreaded Hamilton host containing the same protected pivot.

## 0. Outcome

Let

\[
 H\subset ML_{m+1}
 =Q_{2m+1}\left[\binom{[2m+1]}m\cup
                    \binom{[2m+1]}{m+1}\right]
\tag{0.1}
\]

be the endpoint-preserving MSW/MNW Hamilton cycle with distinguished
coordinate `z` and

\[
                         F_z(H)=\mathcal P_m,          \tag{0.2}
\]

where `P_m` is the complete canonical MSW family of complementary
rank-`m` Johnson geodesics on

\[
                         \Omega=[2m+1]\setminus\{z\}.
\]

The protected-pivot theorem
`MATH_THEOREM_SINGLE_SHARP_PIVOT_MSW_PROTECTED_HAMILTON_HOST_20260807.md`
puts any one depth-`h` sharp pivot, with `3h<=m-1`, inside one chosen member
of this fixed half.

That closes the local topology gate, but the resulting Hamilton cycle is
not upper-complete.  For every `m>=6`, its consecutive rank-`(m+1)` owner
unions miss at least

\[
                         \boxed{\operatorname {Cat}_{m-6}}        \tag{0.3}
\]

rank-`(m+2)` targets avoiding `z`.  A global coordinate permutation only
relabels this missing family.  Moreover, any repair packet changing at
most `b` owner-turn values requires at least

\[
                         \operatorname {Cat}_{m-6}/b              \tag{0.4}
\]

applications.  Hence no bounded local repair of the fixed MSW half can
close even the immediate upper-`q1` row.

Global depth-`h` residence is also not automatic.  Across an MSW component
seam it is equivalent to two simultaneous core-membership conditions on
the exchanged labels.  The published MNW joining tree does not impose
those conditions, and coordinate relabelling cannot change whether they
hold.

Thus the weakest remaining host theorem is not another collar lemma.  It
is an **exterior-moving rethread** which changes the `z`-free owner-turn
map on Catalan scale while fixing the protected pivot segment and retaining
a Hamilton completion.

## 1. The exact turn map on the fixed half

One member of `P_m` has incidence form

\[
 X_0,Y_0,X_1,Y_1,\ldots,Y_{m-1},X_m,                 \tag{1.1}
\]

where

\[
 |X_j|=m,\qquad Y_j=X_j\cup X_{j+1},\qquad |Y_j|=m+1.
\tag{1.2}
\]

The `Y_j` are precisely the `z`-free owner vertices of `H` along this
component.  At every internal turn,

\[
 \boxed{
 Y_j\cup Y_{j+1}
   =X_j\cup X_{j+1}\cup X_{j+2}.}                    \tag{1.3}
\]

The right side is exactly the canonical MSW upper-`q2` value of the
complementary rank-`m` geodesic `X_0,...,X_m`.

Condition (0.2) is stronger than saying that these paths merely occur in
`H`: the `z`-free induced half is exactly `P_m`.  In particular, every
consecutive pair of `z`-free owners in `H` lies internally on one retained
MSW path.  Every owner pair crossing between retained paths passes through
the other half of `H` and therefore has union containing `z`.

## 2. Transfer of the canonical upper-`q2` obstruction

The theorem
`MATH_OBSTRUCTION_CANONICAL_MSW_Q2_SURJECTIVITY_INFINITE_FAMILY_20260805.md`
proves that for every `m>=6` the canonical turn map (1.3) misses at least
`Cat_(m-6)` rank-`(m+2)` targets.  An explicit missing family is obtained
from the endpoint-height-four word

\[
                         (1100)^2 1111 V,             \tag{2.1}
\]

where `V` ranges over all Dyck words of semilength `m-6`.

Every target in (2.1) is a subset of `Omega`, hence avoids `z`.  By Section
1 it has no witness from two consecutive `z`-free owners.  Any owner window
meeting the other half of `H` contains `z`, so it cannot have union equal
to a target in (2.1).  Therefore none of these targets occurs anywhere in
the full Hamilton cycle.  This proves (0.3).

This transfer is insensitive to which canonical component carries the
protected pivot.  The pivot theorem applies a coordinate permutation of
`Omega` to place the chosen geodesic; that same permutation carries the
missing family bijectively to another missing family of the same size.

### Corollary 2.1 (bounded-turn repair lower bound)

Starting from this fixed half, any family of moves in which one move
changes at most `b` values of the owner-turn map needs at least (0.4) moves
before upper-`q1` surjectivity is possible.

#### Proof

Each initially missing target must be created at some changed turn, and one
changed turn supplies at most one rank-`(m+2)` union value.  There are at
least `Cat_(m-6)` distinct missing targets. \(\square\)

This is a support-count statement.  It does not rule out one global move
whose support itself is Catalan-scale.

## 3. Why relabelling and endpoint-only Hamiltonization cannot help

A coordinate permutation preserves every interval-union incidence and
therefore preserves the cardinality of every missing palette.  It can
place the protected pivot wherever desired inside one MSW component, but
it cannot repair (0.3).

Likewise, the endpoint-preserving MNW flips leave the complete `z`-free
half fixed.  They change how its component endpoints are joined through
the `z`-present half, but introduce no new `z`-free owner adjacency.
Consequently they cannot change the map (1.3).

The first hard obstruction to the same-host route is therefore already the
immediate upper-`q1` deck.  It occurs before the deeper arbitrary-width
upper rows and before the global lower compiler.

## 4. The independent residence seam gate

Inside each complementary MSW geodesic, all exchanged coordinates have
long monotone runs; the protected pivot buffer has the local depth-`h`
residence proved in the single-pivot theorem.  What is not certified is
residence across the component joins.

The exact seam theorem in
`MATH_THEOREM_MSW_FREE_REPEAT_COLLAR_AND_ENDPOINT_GRAPH_20260805.md`
says that a forward seam

\[
                         y=x-q+p\longrightarrow x               \tag{4.1}
\]

has both clipped runs of length at least `h+1` if and only if

\[
                         q\in Q_h^+(x),\qquad p\in Q_h^+(y).     \tag{4.2}
\]

For a reverse seam the exact condition is

\[
                         q\in Q_h^-(x),\qquad p\in Q_h^-(y).     \tag{4.3}
\]

The published MNW joining tree is not selected in the alternating
bi-core-safe endpoint graph defined by (4.2)--(4.3).  No theorem currently
shows that all its seams pass these tests.  Coordinate relabelling preserves
deletion order and core membership, so it cannot turn an unsafe seam into a
safe one.

Thus upper incompleteness is a proved obstruction, while global residence
is a separate unclosed interface rather than an additional no-go theorem.

## 5. The weakest exterior-moving rethread

Any successful modification must create new `z`-free owner adjacencies;
changing only endpoint joins through the `z`-present half is insufficient.
The following is the weakest proof-safe target isolated by the preceding
theorem.

> **Protected `q2`-correcting exterior rethread lemma.**  For
> `h=d(2m+1)` and all sufficiently large `m`, there is a Hamilton cycle
> `H'` in `ML_(m+1)` with a distinguished coordinate `z` such that:
>
> 1. `H'` contains the prescribed buffered sharp-pivot incidence segment
>    verbatim;
> 2. outside that segment, its `z`-free incidence edges may be rethreaded,
>    and the unions of consecutive `z`-free rank-`(m+1)` owners cover every
>    rank-`(m+2)` subset of `Omega`;
> 3. the complementary `z`-present rethread reconnects the result into one
>    Hamilton cycle without altering the protected segment; and
> 4. every new component seam satisfies the appropriate two-sided
>    bi-core condition (4.2) or (4.3).

The lemma deliberately asks only for the first missing upper row.  Deeper
upper rows and the global literal antecedent/compiler remain subsequent
gates.  It also permits a Catalan-scale rethread, as Corollary 2.1 shows is
necessary for uniformly bounded-support moves.

Equivalently, before imposing the Hamilton completion, the central object
is a spanning `z`-free incidence path forest which contains the protected
pivot segment and whose owner-turn union map is rank-`(m+2)`-surjective.
The exterior half must then supply compatible endpoints and bi-core-safe
joins.  This is strictly weaker than preserving the canonical MSW path
factor and strictly stronger than ordinary protected Hamiltonicity.

### 5.1 Exact one-coordinate cut equivalence

The preceding description has a useful exact form.  Put

\[
 \mathcal I_0=inom\Omega m\longleftrightarrow
                  \binom\Omega{m+1},\qquad
 \mathcal I_1=inom\Omega{m-1}\longleftrightarrow
                  \binom\Omega m,                    \tag{5.1}
\]

and `C=Cat_m`.  A Hamilton cycle in `ML_(m+1)` is equivalent to a pair
`(F_0,F_1)` such that:

1. `F_i` is a spanning linear forest of `I_i` with exactly `C` path
   components;
2. all endpoints of both forests lie in `binom(Omega,m)`;
3. the two endpoint sets are the same set `E`, of order `2C`; and
4. after joining the two copies of every `X in E` by the vertical edge
   `X--(X+z)`, the union is connected.

#### Proof

Cut a Hamilton cycle at all edges changing membership of `z`.  The
`z`-free vertices induce `I_0`; deleting `z` from the `z`-present vertices
gives `I_1`.  A crossing edge is necessarily the vertical edge
`X--(X+z)` for one `X in binom(Omega,m)`.  Deleting all crossing edges
therefore leaves spanning path forests with the same endpoint set `E`.
No cycle component can remain, because it would already be a component of
the original Hamilton cycle.

Every path of `F_0` has both endpoints on its rank-`m` shore and therefore
contains one more rank-`m` than rank-`(m+1)` vertex.  Since

\[
 {2m\choose m}-{2m\choose m+1}=\operatorname {Cat}_m, \tag{5.2}
\]

`F_0` has exactly `C` components.  The same argument applies to `F_1`.
Thus `|E|=2C`.  Conversely, the vertical edges restore degree two at every
endpoint.  The resulting spanning graph is finite and 2-regular, so it is
a Hamilton cycle exactly when it is connected. \(\square\)

This equivalence permits both halves to move.  The fixed-half MSW theorem
is the special case in which `F_0=P_m` is prescribed in advance.

### 5.2 Suppressed doubly-coloured owner forest

Suppress the internal rank-`m` vertices of `F_0`.  The result is a linear
forest `J` on the complete owner set `binom(Omega,m+1)` with `C` components.
For every edge `AB` of `J` define

\[
             \ell(AB)=A\cap B\in\binom\Omega m,
 \qquad      u(AB)=A\cup B\in\binom\Omega{m+2}.       \tag{5.3}
\]

Lifting `J` back to a simple spanning incidence forest `F_0` is equivalent
to the following two requirements.

* The lower colours `ell(AB)` are pairwise distinct.
* The `2C` endpoint occurrences of `J` have a containment matching onto
  the `2C` unused rank-`m` sets, assigning a distinct subset of its endpoint
  owner to every occurrence.

Immediate upper completeness is exactly

\[
 \boxed{\{u(AB):AB\in E(J)\}=\binom\Omega{m+2}.}      \tag{5.4}
\]

Indeed, internal rank-`m` vertices of `F_0` are precisely the lower edge
colours in (5.3), while its two terminal rank-`m` vertices per component
are precisely the endpoint-matching values.  Together they must enumerate
the whole rank-`m` shore.

The marginal theorem
`MATH_THEOREM_Q2_SATURATING_CYCLE_CLIQUE_INSERTION_AND_CATALAN_PATH_FOREST_20260805.md`,
after complementation, already constructs a spanning `C`-component owner
forest satisfying (5.4).  What it does not control is lower-colour
injectivity, the endpoint containment matching, or compatibility with an
exterior forest `F_1`.  The protected pivot adds only the requirement that
one prescribed owner subpath of `J` be retained.

Consequently the first genuinely new rethreading theorem can be stated
without reference to the canonical MSW factor:

> Construct a protected spanning `C`-component Johnson forest `J` which is
> lower-colour injective and upper-colour surjective, complete its endpoint
> occurrences against the unused lower colours, and find a common-endpoint
> exterior forest `F_1` whose vertical union with `F_0` is connected and
> depth-`h` resident (equivalently bi-core-safe when the two forests retain
> the MSW-geodesic seam model).

This is the exact correlated strengthening of the already solved upper
marginal.  It is also the point at which the current proof stops.

## 6. Scope audit

The proved statements are exactly:

* one sharp pivot with `3h<=m-1` has a protected MSW Hamilton host;
* that particular fixed-half host has at least `Cat_(m-6)` immediate-upper
  holes for every `m>=6`;
* coordinate relabelling and endpoint-only MNW joining do not change the
  hole count;
* bounded-turn packets require Catalan-many applications; and
* global residence of the same host would additionally require all joins
  to satisfy (4.2)--(4.3).

This note does **not** prove that an upper-complete rethread exists or that
none exists.  It does not rule out a Catalan-scale global rethread, a
non-MSW owner factor, or a construction with a different distinguished
coordinate.  It also makes no claim that upper-`q1` surjectivity alone
implies the complete arbitrary-width upper deck.
