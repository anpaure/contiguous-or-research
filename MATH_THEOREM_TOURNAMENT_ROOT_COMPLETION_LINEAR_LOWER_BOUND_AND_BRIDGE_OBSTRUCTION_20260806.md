# Tournament actuators: linear root-completion lower bound and the bridge obstruction

## Status

The regular-tournament biclique actuator has identical owners, exact
immediate-upper multiset, and an identical protected all-depth lower bank,
but its two immediate-lower root families are disjoint.  This note proves
that the missing q1 row cannot be supplied by a resource-disjoint bounded or
sublinear add-on.

Any additive completion which retains the authenticated base adjacencies
needs at least as many new owner occurrences as there are old roots.  More
locally, an owner incident to one old and one new root of a fixed biclique
is forced to be an already-used cross-grid owner.  Therefore the viable
repair is a macroscopic recoupling of a comparable owner bank, not a private
C6 attached outside the actuator.

## 1. Root inventories

Use the notation of the regular-tournament actuator.  Thus `g` is odd,
every group `G_i` has size `L=d+2`, and the base owner set has size

\[
                         N=\binom g2L^2.                     \tag{1.1}
\]

For an arc `i -> j`, the old and new roots are

\[
 \begin{aligned}
 Q^0_{ij;s,t}
   &=R-\{x_{i,s},x_{j,t},x_{j,t+1}\},\\
 Q^1_{ij;s,t}
   &=R-\{x_{j,s},x_{i,t},x_{i,t+1}\},
 \end{aligned}                                             \tag{1.2}
\]

with `s,t in Z_L`.  Let `mathcal Q_0,mathcal Q_1` be their multisets over
all tournament arcs.

The preceding root audit gives

\[
             |\mathcal Q_0|=|\mathcal Q_1|=N,
             \qquad \mathcal Q_0\cap\mathcal Q_1=\varnothing. \tag{1.3}
\]

Every multiplicity in either base family is one.

## 2. Additive completions need at least `N` new owners

Call a pair of phase extensions **base-retaining** when:

1. every old base q1 adjacency remains in phase zero;
2. every new base q1 adjacency remains in phase one; and
3. each phase adds `M` owner occurrences in cyclic state components, so it
   adds exactly `M` q1-root occurrences.

The added owner sets need not be equal, and their new root values may have
arbitrary multiplicity.

### Theorem 2.1 (sharp additive lower bound)

If a base-retaining extension has equal final q1-root multisets in its two
phases, then

\[
                              \boxed{M\ge N.}                \tag{2.1}
\]

More precisely, the phase-zero added multiset must contain every member of
`mathcal Q_1`, and the phase-one added multiset must contain every member of
`mathcal Q_0`.

#### Proof

Write the final root multisets as

\[
                \mathcal Q_0\uplus\mathcal A_0,
                \qquad
                \mathcal Q_1\uplus\mathcal A_1,             \tag{2.2}
\]

where `|mathcal A_0|=|mathcal A_1|=M`.  Fix
`Q in mathcal Q_1`.  By (1.3), its multiplicity in `mathcal Q_0` is zero,
whereas its multiplicity on the phase-one side of (2.2) is at least one.
Equality of the final multisets therefore forces `Q in mathcal A_0`.
All `N` members of `mathcal Q_1` are distinct, so `M>=N`.  The other shore
is symmetric. `square`

The bound is a counting identity, not a limitation of a particular C6
catalogue.  In particular no `O(1)`, `O(d)`, or `o(N)` resource-disjoint
completion can close this q1 row while retaining the base adjacencies.

For the largest odd tournament bank, `g=Theta(r/L)`, one has

\[
                              N=Theta(r^2).                  \tag{2.3}
\]

Even the smallest nontrivial choice `g=3` has

\[
                              N=3L^2=Theta(d^2).             \tag{2.4}
\]

## 3. No fresh owner directly bridges an old and a new root

It is convenient to encode an owner `R-{u,v}` by its omitted pair
`{u,v}`, and a root `R-Z` by its omitted triple `Z`.  The root is contained
in the owner exactly when

\[
                              \{u,v\}\subset Z.              \tag{3.1}
\]

### Theorem 3.1 (fixed-pair bridge obstruction)

Fix one group pair `G_i,G_j`.  If a rank-`r` owner is incident to both an
old root and a new root from (1.2) for this pair, then it is one of the
already-used cross-grid owners

\[
                         R-\{u,v\},qquad
                         u\in G_i, v\in G_j.                \tag{3.2}
\]

There is no owner outside the base grid which directly joins the two root
shores.

#### Proof

The omitted triple of an old root has group profile

\[
                              (1\text{ in }G_i, 2\text{ in }G_j), \tag{3.3}
\]

whereas a new root has profile

\[
                              (2\text{ in }G_i, 1\text{ in }G_j). \tag{3.4}
\]

Their intersection contains at most one element of each group.  If one
owner is incident to both roots, (3.1) says that its omitted pair lies in
this intersection.  The intersection must consequently have size two and
the pair must contain exactly one element of `G_i` and one of `G_j`.
This is precisely (3.2), which belongs to the base owner grid. `square`

### Corollary 3.2 (no private one-step splice)

A repair path which starts at an old root, enters only fresh owners, and
ends immediately at a new root cannot exist.  Any such path must either:

* reuse a base cross-grid owner;
* pass through additional intermediate root types and at least two fresh
  owner incidences; or
* globally rethread the base owner bank.

The first option destroys resource-disjointness, while the second remains
subject to the linear occurrence lower bound of Theorem 2.1 if the base
roots are retained.

## 4. Exact scope and viable repair

Theorem 2.1 assumes the base q1 adjacencies survive as submultisets.  It
does not rule out a length-preserving recoupling which deletes many old and
new base adjacencies and recomputes both root palettes on the same owners.
Indeed that is now the only plausible bounded-length route.

The next proof target is therefore not a local root-completion gadget.  It
is:

> **Macroscopic q1 recoupling lemma.**  On a tournament owner bank of size
> `N`, rethread a positive fraction of the existing cross-grid owners,
> without adding positions, so that the two phases acquire one common
> q1-lower multiset while retaining the exact q1-upper balance and the
> protected all-depth tickets.

Any theorem phrased as an external C6 completion must explicitly pay at
least `N` new q1 occurrences and therefore cannot yield an additive-constant
construction.
