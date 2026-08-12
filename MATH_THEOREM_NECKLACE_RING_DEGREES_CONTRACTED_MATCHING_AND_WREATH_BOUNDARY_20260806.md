# Exact necklace-ring degrees, incidence contraction, and the wreath boundary

## Status

This note computes the complete degree and pair-codegree ledger for the
near-maximal masked antipodal rings used in
`MATH_THEOREM_NEAR_MAX_RING_UNIFORM_COORDINATE_MARGINALS_20260806.md`.
It also gives an exact contraction of the simultaneous owner/root resolution
through one perfect matching of the quotient middle-incidence graph.

The conclusions are sharp.

* On either literal shore separately, the maximum nontrivial pair-codegree is
  only

  \[
             {2D\over q(q-1)}.
  \]

  Thus one-shore ring selection has genuinely favourable local overlap.
* An incident owner/root pair has codegree

  \[
             {2D\over q},
  \]

  because the root can be the left or right boundary of the owner.  Hence the
  combined `2 ell`-uniform host is at the critical scale

  \[
        2\ell\,{\Delta_2\over D}=4+o(1).
  \]
* After quotienting by coordinate translation, the exact codegree is a sum
  over all relative translations.  It depends on the cyclic autocorrelation
  of the two necklaces.  The quotient-simple subhost is therefore not proved
  regular by symmetry; symmetry proves regularity only for the
  occurrence-counted multihost.
* Fixing a perfect matching of the quotient owner/root incidence multigraph is
  an exact reduction, not a relaxation.  Contracting that matching produces a
  `(q-1)`-regular directed multigraph.  The desired rings are a very special
  family of directed cycles in it.  Ordinary directed cycle covers do not
  impose the common-core and delayed-insertion law.

No currently cited perfect-matching, design-decomposition, or wreath theorem
closes the resulting exact cycle resolution.  In particular the construction
must not be delegated to the still-open general Baranyai--Katona wreath
conjecture.

No computation or search is used.

## 1. The ring universe

Put

\[
 n=2q-1,\qquad s=q-h,
 \qquad \ell=q+h-1-u,\qquad u\in\{1,2\}.               \tag{1.1}
\]

Thus a ring has an invariant core `K`, a cyclically ordered moving set `F`,
and an unused set `U` of sizes

\[
                    |K|=s,\qquad |F|=\ell,
                    \qquad |U|=u.                       \tag{1.2}
\]

For a cyclic order `F=(f_t)`, its owners and roots are

\[
 \begin{aligned}
 O_t&=K\cup\{f_t,\ldots,f_{t+h-1}\},\\
 Q_t&=K\cup\{f_{t+1},\ldots,f_{t+h-1}\}.
 \end{aligned}                                          \tag{1.3}
\]

The ring is oriented, but its phase is cyclic: cyclic rotations of the word
`F` describe the same oriented ring.  Reversal is kept as the other
orientation.  Every ring has `ell` distinct owners and `ell` distinct roots.

For falling factorials write

\[
                        (x)_d=x(x-1)\cdots(x-d+1).       \tag{1.4}
\]

## 2. Exact degrees

### Theorem 2.1 (both shore degrees)

The number of oriented rings containing a fixed rank-`q` owner, and the
number containing a fixed rank-`(q-1)` root, are both

\[
              \boxed{D={q!(q-1)!\over s!u!}}.           \tag{2.1}
\]

#### Proof

Fix an owner `T`.  Choose

* the core `K subset T`, in `binom(q,s)` ways;
* the unused set `U subset [n]-T`, in `binom(q-1,u)` ways;
* the order of the `h` moving elements in `T-K`;
* the order of the remaining `ell-h` moving elements.

Anchoring `T` at phase zero removes cyclic rotation and gives

\[
 \binom qs\binom{q-1}u h!(\ell-h)!
       ={q!(q-1)!\over s!u!}.                           \tag{2.2}
\]

For a fixed root `Q`, choose `K subset Q`, choose the unused set in the
`q`-element complement of `Q`, and order the `h-1` moving elements in `Q-K`
and the remaining `ell-h+1` moving elements.  This gives

\[
 \binom{q-1}s\binom qu (h-1)!(\ell-h+1)!
       ={q!(q-1)!\over s!u!}.                           \tag{2.3}
\]

This proves the claim. \(\square\)

## 3. Exact same-shore codegrees

For two sets on the same uniform shore, their Johnson distance is the number
of elements in either one-sided difference.

### Theorem 3.1 (owner pairs)

Let two rank-`q` owners have Johnson distance `d`.

For `1<=d<h`, their codegree is

\[
 \boxed{
 \lambda^{OO}_d=
 2\binom{q-d}s\binom{q-1-d}u
 (d!)^2(h-d)!(\ell-h-d)! }
                                                               \tag{3.1}
\]

and hence

\[
 \boxed{{\lambda^{OO}_d\over D}
       ={2(d!)^2\over(q)_d(q-1)_d}.}                    \tag{3.2}
\]

At the disjoint-window endpoint `d=h`,

\[
 \boxed{{\lambda^{OO}_h\over D}
   ={s-u\over\binom qh\binom{q-1}h}.}                  \tag{3.3}
\]

For `d>h` the codegree is zero.

#### Proof

When `d<h`, the two moving `h`-windows overlap in `h-d` elements.  Their
relative cyclic displacement is either `+d` or `-d`.  Their common core is
chosen in `binom(q-d,s)` ways, and the unused set is chosen outside their
union in `binom(q-1-d,u)` ways.  The two one-sided differences, the overlap,
and the unused part of the cyclic order contribute respectively

\[
                  d!,\quad d!,\quad(h-d)!,
                  \quad(\ell-h-d)!.
\]

This proves (3.1), and cancellation against (2.2) gives (3.2).

At `d=h`, the core is forced to be the complete intersection.  The two
moving windows are disjoint.  There are `ell-2h+1=s-u` possible relative
displacements.  Ordering the two windows and the remaining moving labels
gives

\[
 \lambda^{OO}_h
   =\binom{s-1}u(s-u)(h!)^2(s-1-u)!.
\]

Dividing by `D` gives (3.3).  Every two owners in one ring contain the common
`s`-set `K`, so distance greater than `h` is impossible. \(\square\)

### Theorem 3.2 (root pairs)

Let two rank-`(q-1)` roots have Johnson distance `d`.  For `1<=d<h-1`,

\[
 \boxed{
 \lambda^{RR}_d=
 2\binom{q-1-d}s\binom{q-d}u
 (d!)^2(h-1-d)!(\ell-h+1-d)! }
                                                               \tag{3.4}
\]

and

\[
 \boxed{{\lambda^{RR}_d\over D}
       ={2(d!)^2\over(q-1)_d(q)_d}.}                    \tag{3.5}
\]

At `d=h-1`,

\[
 \boxed{{\lambda^{RR}_{h-1}\over D}
 = {s+2-u\over\binom q{h-1}\binom{q-1}{h-1}}.}        \tag{3.6}
\]

For `d>h-1` the codegree is zero.

#### Proof

The proof is the preceding proof with moving-window size `h-1`.  At the
endpoint, the number of disjoint relative positions is
`ell-2(h-1)+1=s+2-u`; the complement of the union has size `s+1`.  Thus

\[
 \lambda^{RR}_{h-1}
  =\binom{s+1}u(s+2-u)((h-1)!)^2(s+1-u)!,
\]

which simplifies to (3.6). \(\square\)

### Corollary 3.3 (the same-shore maximum)

In the near-maximal regime `h=o(q)`, for all sufficiently large `q`,

\[
       \max_{T\ne T'}\lambda^{OO}(T,T')
       =\max_{Q\ne Q'}\lambda^{RR}(Q,Q')
       ={2D\over q(q-1)}.                               \tag{3.7}
\]

Indeed the ratio of successive normalized values in (3.2) or (3.5) is

\[
        {(d+1)^2\over(q-d)(q-1-d)}<1,                  \tag{3.8}
\]

and the disjoint-window endpoints (3.3), (3.6) are exponentially smaller.
Consequently

\[
                  \ell\,{\Delta^{\rm same}_2\over D}
                         =O(q^{-1}).                    \tag{3.9}
\]

## 4. Exact cross-shore codegrees

For an owner `T` and a root `Q`, put

\[
                         c=|T-Q|.                       \tag{4.1}
\]

Since `|T|=q` and `|Q|=q-1`, the opposite difference has size `c-1`.

### Theorem 4.1 (owner/root pair)

For `1<=c<h`,

\[
 \boxed{
 \lambda^{OR}_c=
 2\binom{q-c}s\binom{q-c}u
 c!(c-1)!(h-c)!(\ell-h-c+1)! }
                                                               \tag{4.2}
\]

and therefore

\[
 \boxed{{\lambda^{OR}_c\over D}
   ={2c!(c-1)!\over(q)_c(q-1)_{c-1}}.}                 \tag{4.3}
\]

At `c=h`,

\[
 \boxed{{\lambda^{OR}_h\over D}
 = {s+1-u\over\binom qh\binom{q-1}{h-1}}.}            \tag{4.4}
\]

For `c>h` the codegree is zero.  In particular, when `Q subset T`,

\[
              \boxed{\lambda^{OR}_1={2D\over q}.}      \tag{4.5}
\]

If one prescribes which side of `T` the root occupies, the factor two is
removed and the codegree is `D/q`.

#### Proof

For `c<h`, the moving windows overlap in `h-c` elements and have two cyclic
relative positions.  Choose the core in their intersection and the unused
set outside their union.  The owner-only part has size `c`, the root-only
part size `c-1`, and the remaining moving part outside the union has size
`ell-h-c+1`.  This gives (4.2).  Cancelling the core, unused, and order
factors against `D` gives (4.3).

At `c=h`, the moving windows are disjoint.  There are `s+1-u` relative
positions, giving

\[
 \lambda^{OR}_h
 =\binom su(s+1-u)h!(h-1)!(s-u)!,
\]

which is (4.4).  Formula (4.5) is (4.3) with `c=1`: a contained root is
necessarily one of the two endpoint roots of the owner. \(\square\)

### Corollary 4.2 (the critical two-shore scale)

For `h=o(q)`, the values (4.3) decrease with `c`, since

\[
 {\lambda^{OR}_{c+1}\over\lambda^{OR}_c}
        ={c(c+1)\over(q-c)^2}<1.                       \tag{4.6}
\]

Thus the combined owner/root ring hypergraph has

\[
                {\Delta_2\over D}={2\over q},
 \qquad
       2\ell\,{\Delta_2\over D}=4+o(1).               \tag{4.7}

The root shore is therefore not a harmless decoration of an owner-only
nibble.  It is the unique critical pair correlation.

## 5. What translation quotienting does to the ledger

Let `Z_n` act by coordinate translation.  Both central shores are free and
have `C=W/n` necklaces.  Let `X=[T]`, `Y=[T']` be owner necklaces.  In the
occurrence-counted quotient multihypergraph the exact owner codegree is

\[
 \boxed{
 \overline\lambda^{OO}(X,Y)
   =\sum_{a\in\mathbb Z_n}
        \lambda^{OO}_{|T-(T'+a)|}.}                    \tag{5.1}
\]

The root formula is identical with (3.4)--(3.6).  For an owner necklace
`X=[T]` and a root necklace `Z=[Q]`,

\[
 \boxed{
 \overline\lambda^{OR}(X,Z)
   =\sum_{a\in\mathbb Z_n}
        \lambda^{OR}_{|T-(Q+a)|}.}                     \tag{5.2}
\]

These expressions are independent of the chosen representatives, but not
of the necklace pair.

Every ring orbit used here also has full size `n`.  Indeed, if a nonzero
translation stabilized a ring, it would stabilize its unused set `U`.
Every nontrivial translation orbit on `Z_n` has odd size at least three,
whereas `|U|` is one or two.  Thus `U` cannot be a union of nontrivial
translation orbits.  This rules out a hidden stabilizer factor in
(5.1)--(5.2).

In particular, define the literal incidence multiplicity

\[
 m(X,Z)=\#\{a\in\mathbb Z_n:Q+a\subset T\}.            \tag{5.3}
\]

The `c=1` contribution alone is

\[
                     {2D\over q}\,m(X,Z).              \tag{5.4}
\]

The multiplicities `m(X,Z)` are the entries of the quotient middle-incidence
multigraph and need not all be zero or one.

### Proposition 5.1 (regular multihost, irregular simple host)

Counting necklace occurrences with multiplicity, every owner and root
necklace has degree exactly `D`.  Equations (5.1)--(5.2) are its exact
pair multicodegrees.

After restricting to quotient-simple rings, the degree of a necklace `X`
is

\[
 D_X^{\rm simple}
   =D-\#\{\text{rings through a fixed }T\in X
            \text{ with a repeated owner or root necklace}\}. \tag{5.5}
\]

The subtracted quantity depends on cyclic autocorrelations of `X` and of
the other phases.  Translation symmetry alone does not make (5.5)
independent of `X`.

#### Proof

Fix `T` in `X`.  In a full translation orbit of a ring, every occurrence of
`X` has exactly one translate equal to `T`.  Therefore the incidence degree,
with repeated necklace occurrences retained, is the literal degree `D`.
Two prescribed necklace occurrences may have any relative translation,
and summing the literal codegree over that relative translation gives
(5.1) or (5.2).

If a ring uses one necklace twice, the occurrence multihost retains both
copies but the quotient-simple host deletes the ring.  Whether this happens
is exactly an autocorrelation property of the displayed sets. \(\square\)

For example, the cyclic interval

\[
                         T=\{0,1,\ldots,q-1\}
\]

has `T+1` as a Johnson-distance-one member of its own necklace.  Any ring
containing this pair is non-simple after quotienting, and Theorem 3.1 counts
exactly `2D/[q(q-1)]` such oriented rings through the pair.  A necklace with
no distance-one translate has no loss of this type.  This is a literal
source of the nonuniformity in (5.5), not merely a limitation of the proof.

Thus the favourable literal same-shore estimate (3.9) cannot simply be
quoted after quotienting: a quotient pair aggregates up to `n` relative
translations, and the cross pair additionally sees the incidence
multiplicity (5.3).

The immediate uniform bounds illustrate the loss:

\[
 \overline\lambda^{OO}(X,Y)
       \le {2nD\over q(q-1)}=(4+o(1)){D\over q},        \tag{5.6}
\]

whereas the corresponding coarse cross bound is

\[
 \overline\lambda^{OR}(X,Z)
       \le {2nD\over q}=(4+o(1))D.                     \tag{5.7}
\]

Equation (5.7) is a multicodegree bound and may exceed the degree because a
single orbit edge can contain repeated necklace occurrences.  Restricting
to quotient-simple edges restores the tautological codegree-at-most-degree
bound, but loses exact regularity through (5.5).

### Theorem 5.2 (autocorrelation-exceptional necklaces are exponentially sparse)

For `k in {q-1,q}`, let

\[
 \mathcal E_k(h)=\left\{T\in\binom{[n]}k:
       |T-(T+a)|\le h\text{ for some }a\ne0\right\}.   \tag{5.8}
\]

If `h=o(n/log n)` (in particular for the critical `h=Theta(sqrt n)`), then

\[
 { |\mathcal E_k(h)|\over\binom nk}=\exp(-\Omega(n)). \tag{5.9}
\]

Consequently the proportion of all oriented rings which fail owner- or
root-quotient-simplicity is `exp(-Omega(n))`.  Moreover, after deleting an
`exp(-Omega(n))` fraction of necklace vertices, every remaining vertex loses
only an `exp(-Omega(n))` fraction of its incident rings.

#### Proof

Fix a nonzero translation `a`, put `g=gcd(a,n)` and `L=n/g`.  Its coordinate
permutation consists of `g` cycles of length `L`.  Record membership in `T`
as a binary cyclic word on each cycle.  The Johnson distance

\[
                         |T-(T+a)|
\]

is half the total number of binary transitions on those cycles.  A word with
at most `2h` transitions is specified by its transition edges and one
initial bit on every coordinate cycle.  Hence, without even imposing the
rank condition, the number of such `T` is at most

\[
                    2^g\sum_{j=0}^{2h}\binom nj.       \tag{5.10}
\]

Because `n` is odd, a nontrivial proper divisor satisfies `g<=n/3`.  Also

\[
       \log\left(\sum_{j=0}^{2h}\binom nj\right)
                    =O(h\log(n/h))=o(n).               \tag{5.11}
\]

Summing (5.10) over the fewer than `n` nonzero translations gives

\[
             |\mathcal E_k(h)|
                 \le \exp((\log2)n/3+o(n)).            \tag{5.12}
\]

Both relevant binomial layers have size
`exp((log 2)n-o(n))`, proving (5.9).

If two owners in one ring lie in the same necklace, then they are translates
at Johnson distance at most `h`; if two roots do, their distance is at most
`h-1`.  Thus every nonsimple ring contains an occurrence from one of the two
exceptional families.  The exact degree `D` bounds the number of such ring
occurrences by

\[
          D\bigl(|\mathcal E_q(h)|
                 +|\mathcal E_{q-1}(h-1)|\bigr).       \tag{5.13}
\]

There are `WD/ell` oriented rings in total.  Dividing (5.13) by this number
and using (5.9) proves the global assertion.  Applying Markov's inequality
to the lost-degree sum proves the final vertexwise assertion after changing
the implicit exponential constant. \(\square\)

At distance one there is even an exact count.  For a fixed nonzero `a`,
with `g,L` as above, a rank-`q` set satisfies `|T-(T+a)|=1` exactly when one
of the `g` coordinate cycles has one `1`-block of length `(L+1)/2`, exactly
`(g-1)/2` other cycles are full, and all remaining cycles are empty.  Hence

\[
 \#\left\{T\in\binom{[n]}q:|T-(T+a)|=1\right\}
       =n\binom{g-1}{(g-1)/2}.                          \tag{5.14}
\]

For rank `q-1`, replace the nonconstant block length by `(L-1)/2`; the same
count results.  Thus the worst explicit autocorrelation types are a
negligible exceptional bank, even though they prevent an exact global
regularity claim for the quotient-simple host.

## 6. Exact contraction through one quotient matching

Let `Gbar` be the bipartite multigraph whose shores are the owner and root
necklaces and whose edges are translation orbits of literal incidences
`Q subset T`.

### Lemma 6.1 (the quotient incidence graph)

`Gbar` is `q`-regular on two `C`-vertex shores.  Hence it has a perfect
matching and, indeed, a decomposition into `q` perfect matchings.

#### Proof

Every literal owner contains `q` roots and every literal root has `q`
owner supersets.  Since both actions are free, quotienting preserves these
degrees with edge multiplicity.  Bipartite regular multigraphs have a
one-factorization. \(\square\)

Fix a perfect matching `M` of `Gbar`.  Contract every matched root-owner
edge.  For a root `Qbar` matched to owner `X`, and every other incidence
edge from `Qbar` to an owner `Y`, create an arc `X -> Y`.  Call the resulting
directed multigraph `D_M`.

### Lemma 6.2 (regular contracted digraph)

`D_M` has indegree and outdegree `q-1` at every vertex.

#### Proof

The root matched to `X` has `q-1` other incident edges, giving the outgoing
arcs.  Of the `q` root incidences at an owner `Y`, exactly one is its matched
edge; the other `q-1` give the incoming arcs. \(\square\)

An oriented quotient ring has two alternating perfect matchings on its own
owner/root incidence cycle: pair every `Q_t` with `O_t`, or pair every
`Q_t` with `O_{t+1}`.

### Theorem 6.3 (contracted-incidence equivalence)

A quotient-simple simultaneous owner/root ring resolution with the required
numbers of periods `ell=p,p+1` exists if and only if there are

1. a perfect matching `M` of `Gbar`; and
2. a partition of the owner necklaces into quotient-simple rings of those
   periods,

such that one alternating incidence matching of every selected ring is
contained in `M`.

Equivalently, after orienting each ring, its owners form a directed cycle in
`D_M`.  Not every directed cycle is allowed: it must have a literal lift

\[
 O_t=K\cup\{f_t,\ldots,f_{t+h-1}\},\qquad
 Q_t=O_t-\{f_t\},                                      \tag{6.1}
\]

with a common core, distinct moving labels, the required voltage, and the
delayed insertion law

\[
                         b_t=f_{t+h}.                   \tag{6.2}
\]

#### Proof

Given a resolution, choose either of the two alternating incidence
matchings independently on every ring.  The ring blocks partition both
shores, so their union is a perfect matching `M` of `Gbar`.

Conversely, suppose the owner blocks partition and one alternating matching
of each lies in `M`.  Every owner is matched once by `M`, and therefore the
roots used by those alternating matchings are also all distinct and exhaust
the root shore.  Hence the same rings resolve both shores.

Contracting `M` turns the unchosen incidence edge at every ring root into
the next directed arc, giving the cycle in `D_M`.  Formulae (6.1)--(6.2) are
exactly the antipodal-ring recognition law and are additional to being a
directed cycle. \(\square\)

This theorem isolates the root correlation, but it does not make it free.
An arbitrary cycle factor of the regular digraph `D_M` need not have either
allowed period and almost never has one common core per cycle.

### Corollary 6.4 (two colours of one factorization)

The same resolution is equivalent to two edge-disjoint perfect matchings
`M_0,M_1` of `Gbar` whose union has the required quotient-simple antipodal
cycles.  Moreover `M_0,M_1` can always be extended to a complete
`q`-edge-colouring of `Gbar`.

Equivalently, the permutation of the owner shore obtained by following an
`M_0` edge backwards to a root and then the `M_1` edge forwards to an owner
has exactly `A` cycles of length `p` and `B` cycles of length `p+1`, and every
cycle satisfies the literal recognition law (6.1)--(6.2).

#### Proof

In a resolution, take the two alternating incidence matchings on every ring
and union like parities over all rings.  They are two edge-disjoint perfect
matchings `M_0,M_1`.  Conversely their bicoloured cycles resolve both shores
whenever those cycles are recognized rings.  Removing them leaves a
`(q-2)`-regular bipartite multigraph, which has a one-factorization.  The
permutation description is the usual contraction of `M_0`. \(\square\)

Thus the reference to a `q`-edge-colouring can be made exact, but only in the
following form: **find two globally coordinated colours whose union already
has the desired special cycles**.  Permuting the names of the colours in an
arbitrary factorization creates no new bicoloured subgraph.

## 7. Why averaging over incidence matchings is not a solution

For one oriented ring `R`, let `P_R^+` and `P_R^-` denote its two
`ell`-edge alternating partial matchings.  Exactly

\[
 R\text{ is compatible with }M
 \quad\Longleftrightarrow\quad
 P_R^+\subseteq M\ \text{ or }\ P_R^-\subseteq M.       \tag{7.1}
\]

Thus matching compatibility is an `ell`-edge correlation, not a one-edge
marginal.

There is an exact fractional fact: orient every ring both ways with equal
weight.  Its incidence-edge projection is the barycentre

\[
                         x_e={1\over q}\qquad(e\in E(Gbar)), \tag{7.2}
\]

because a prescribed side of a fixed owner/root incidence occurs in `D/q`
rings.  By bipartite matching integrality, (7.2) is a convex combination of
perfect matchings.

But this decomposition does not preserve the ring variables.  It controls
each edge separately and gives no perfect matching containing all `ell`
edges of either `P_R^+` or `P_R^-` for a useful family of rings.

The independent benchmark shows the size of the lost correlation.  If each
owner chose one of its `q` incidences independently, an oriented ring would
respect all choices with probability `q^{-ell}`.  Its expected compatible
degree through a fixed owner would be

\[
 {D\over q^\ell}
 ={q!(q-1)!\over s!u!\,q^{q+h-1-u}}
 \le { (q-1)!\over u!\,q^{q-1-u}}
 =\exp(-q+O(\log q)).                                  \tag{7.3}
\]

This is not a theorem about a specially correlated perfect matching, but it
proves that independent deletion choices and first-moment averaging are the
wrong mechanism.  A successful `M` must itself be generated coherently with
the ring resolution.

Likewise, choosing one colour from a fixed `q`-edge-colouring of `Gbar`
keeps a ring only when all edges of one `P_R^\pm` are monochromatic.  An
edge-colouring theorem supplies no such monochromatic cyclic blocks.

## 8. Boundary of the standard theorems

The degree ledger identifies exactly what standard results do and do not
give.

1. **Bipartite matching and flow.**  These give `M` and the regular digraph
   `D_M`.  They do not impose (6.1)--(6.2) or the prescribed cycle lengths.
2. **Fixed-rank nibble/list-colouring theorems.**  On one literal shore the
   ratio (3.9) is promising for an approximate packing.  The combined host
   has the critical cross scale (4.7), and after quotienting even the
   maximum codegree is necklace-dependent.  Moreover the available
   fixed-rank hierarchies do not permit rank `ell=Theta(q)` to grow with
   `log C=Theta(q)`.  This is the same quantifier failure audited in
   `MATH_AUDIT_GOULD_KELLY_VORTEX_PACKET_CHROMATIC_GATE_20260806.md`.
3. **Dense hypergraph perfect-matching and design-decomposition theorems.**
   Their minimum-degree or fixed-template supercomplex hypotheses do not
   hold: the ring host is sparse and its template size grows with `q`.
4. **Cycle covers of regular digraphs.**  A cycle cover in `D_M` is only a
   Johnson/inclusion chronology.  The common core and delayed insertion are
   nonlinear recognition constraints.

Thus no invoked theorem proves even the exact undecorated necklace
resolution of Theorem 3.2 in the near-maximal-ring note.

## 9. Exact comparison with the Baranyai--Katona wreath conjecture

The Baranyai--Katona conjecture asks, for every pair `(N,k)`, for a
decomposition of the complete `k`-uniform layer into cyclic-interval
wreaths.  When `gcd(N,k)=1`, these are tight Hamilton cycles.

Two qualifications are essential here.

1. The central case `(N,k)=(2m+1,m)` is already known: the
   Mütze--Standke--Wiechert cycle factor in the odd graph gives `Cat_m`
   cycles of length `2m+1`, and each such minimum odd cycle is a wreath.
   Therefore the present argument must not describe that special central
   case as open.
2. The general conjecture remains open.  Petr--Turek's 2025 Dyck-labelled
   statements are stronger conjectures, not available decomposition
   theorems.

For one fixed pair `(K,U)`, our moving layer is the complete `h`-uniform
layer on the `ell`-set `F=[n]-(K union U)`.  When `gcd(ell,h)=1`, our
one-step cyclic `h`-windows are precisely a Baranyai--Katona wreath (a tight
Hamilton cycle), and the general conjecture for `(ell,h)` would decompose
that *whole fibre*.  Even then our resolution does not contain a whole
fibre: it must choose correlated pieces from many `(K,U)` fibres so that
every rank-`q` owner necklace and every rank-`(q-1)` root necklace occurs
once.  The conjecture alone would not supply that cross-fibre allocation.

When `gcd(ell,h)>1`, the distinction is sharper.  A Katona wreath has
`ell/gcd(ell,h)` sets, obtained from the appropriate stepped starts, whereas
our antipodal ring uses all `ell` one-step windows.  In that case the local
atom itself is not a Katona wreath in the standard noncoprime convention.

Conversely, the present resolution is one specialized two-shore design and
does not imply the general wreath conjecture.  The two problems share the
same cyclic-window atom, but neither may be cited as a theorem proving the
other.

There is a second caution about equivariance.  The necklace resolution is a
translation-invariant sufficient subclass; a literal exact ring factor need
not be translation-invariant.  In the limiting central parameters
`h=q,s=u=0,ell=2q-1`, its analogue becomes the problem of a
translation-invariant exact central wreath factor.  Even though an
unrestricted central wreath factor is known, the invariant version has an
additional voltage/difference-family gate (and, for prime
`2q-1` congruent to `1` modulo `4`, exceptional AP loops).  This is the classification
in
`MATH_THEOREM_O_PRIME_INVARIANT_QUOTIENT_FACTOR_AND_ONE_SIDED_NECKLACE_GATE_20260726.md`;
the general invariant existence statement is not presently a theorem.

Our `u=1,2` rings have free translation orbits and avoid those AP fixed
loops, but the comparison shows why passing to necklaces is a substantive
equivariant design demand, not a routine quotient of the known literal
central factor.  A non-invariant literal near-maximal ring construction
would bypass Theorem 3.2 entirely and remains a legitimate alternative.

Primary references for this scope distinction are:

* T. Mütze, C. Standke, V. Wiechert, *A minimum-change version of the
  Chung--Feller theorem for Dyck paths*, arXiv:1603.02525;
* J. Petr, P. Turek, *Intervals in Dyck paths and the wreath conjecture*,
  arXiv:2501.07277.

## 10. The sharpened remaining theorem

The exact central gate may now be stated without hidden marginal claims.

> **Matched necklace-ring resolution.**  Choose a perfect matching `M` of
> the `q`-regular quotient incidence multigraph such that the special cycle
> catalogue in `D_M` satisfying (6.1)--(6.2) has a spanning cycle factor
> with exactly `A` cycles of length `p` and `B` cycles of length `p+1`, while
> every selected cycle is quotient-simple.

The uniform coordinate ledger proves a fractional solution before `M` is
chosen.  Theorems 3.1--4.1 prove that same-shore overlap is not the barrier.
Theorem 6.3 shows that the only central integral correlation is the coherent
choice of `M` together with its special directed cycle factor.

This is the strongest proof-safe reduction presently available.  It is not
closed by a standard matching theorem and should be attacked as a
structured deletion-matching/cycle-factor construction, potentially with a
small exceptional necklace absorber, rather than as a generic
`2 ell`-uniform hypergraph matching.
