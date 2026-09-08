# The relative-identity PBBS fusion route is a mod-three period obstruction

**Date:** 2026-08-05  
**Method:** directed-period and cochain calculus on complete fan states; no
computation or search  
**Status:** unconditional sufficient reduction after quotienting the
unavoidable strand-tag monodromy.  It characterizes exactly when a family
of positive aligned clean-`C6` transitions can return the complete fan
**state** up to its canonical occurrence bijection while changing the
three-cycle topology.  Zero fan current can more generally occur through a
nonidentity element of the deck stabilizer; that weaker route is recorded
in Section 4 and is not characterized by the period test alone.

## 1. The literal transition digraph

Fix a prospective PBBS host.  A raw cut state is an ordered triple of
occurrence-labelled states

\[
 \Omega=(R,(A(u))_{u\geq 0},(B(v))_{v\geq 0},
              \hbox{source and occurrence tags}),                 \tag{1.1}
\]

one on each of the three directed factor cycles.  Let `tau` cyclically
rename the three strand-occurrence tags, carrying the entire record
attached to a tag but not relabelling any ground-set coordinate.

One positive aligned site necessarily advances the strand tag by `tau`.
Thus a raw `k`-site holonomy has tag projection `tau^k`; raw pointwise
identity would itself force `3|k` and is the wrong comparison for a fusion.

At site number `j`, gauge-normalize the raw state by `tau^{-j}`.  If its raw
site-plus-forward-transport map is `A_j=E_jS_j`, its normalized map is

\[
                  \bar A_j=\tau^{-(j+1)}A_j\tau^j.              \tag{1.2}
\]

The **relative complete-state transition digraph** `G` has these
gauge-normalized states as vertices and the physically admissible maps
`bar A_j` as edges.  In raw notation, a directed relative cycle of length
`k` says exactly

\[
                          H=\tau^k                               \tag{1.3}
\]

on the complete visible state.  This is equality through the canonical
old-to-new occurrence bijection, not pointwise equality of immutable old
strand names.

An edge

\[
                         \bar\Omega\longrightarrow\bar\Omega'     \tag{1.4}
\]

is one normalized positive clean-`C6` site followed by the declared literal
forward transport to the next aligned site.  Actual owner labels,
both complete history chains, source occurrences, and all protected halo
data are part of the vertex.  Equality in `G` is literal equality of this
data, not equality only of ranks or unlabelled target sets.

A directed cycle in `G` is called **physically simple** when its site
supports, owners, and required halo resources are pairwise disjoint and
its transitions occur in the same cyclic order on each of the three old
factor cycles.  These are precisely the extra hypotheses needed to read
the abstract cycle as an aligned multi-site replacement.

## 2. State return versus topology

### Theorem 2.1 (relative cycle criterion)

Let a physically simple directed cycle in the relative graph `G` have
length `k`.  Equivalently, let its raw holonomy satisfy (1.3).  Then its
complete fan current is zero at every depth, through the occurrence
bijection `tau^k`.  On the union of the three old factor cycles, its
positive reconnections produce exactly

\[
                              \gcd(3,k)                         \tag{2.1}
\]

new cycles.  Hence it is a state-returning fusion macro if and only if

\[
                              k\not\equiv0\pmod3.               \tag{2.2}
\]

#### Proof

The directed relative cycle returns the gauge-normalized state (1.1).  In
raw labels its endpoint is `tau^k` of its start.  Pair each initial
occurrence with the terminal occurrence bearing its transported tag.
Successive triangular fan currents then telescope occurrence by occurrence,
and the final deck is the initial deck under this bijection.  The
complete-state coboundary theorem gives zero lower fan current, and
complementation gives zero current on the paired upper witnesses.

For the topology, cut the `k` aligned edges on each old cycle.  After one
old path segment a positive reconnection advances the old-cycle index by
one and the site index by one.  After a tour of all site positions, the
return action on the old-cycle index is translation by `k` in `Z_3`.
Its number of orbits is `gcd(3,k)`. `square`

Thus, for the relative-identity route, the topology and fan constraints are
no longer two unrelated global conditions.  They ask for one directed
state cycle whose length is nonzero modulo three.

## 3. Exact phase-lock alternatives

Let `C` be a strongly connected component of the relative graph `G`.  Write `1` for the
constant `Z_3`-valued function on its directed edges.

### Theorem 3.1 (phase-potential equivalence)

The following are equivalent.

1. Every directed closed walk in `C` has length divisible by three.
2. There is a function

   \[
                        \phi:V(C)\longrightarrow\mathbb Z_3       \tag{3.1}
   \]

   such that every edge `x->y` satisfies

   \[
                              \phi(y)=\phi(x)+1.                  \tag{3.2}
   \]
3. Any two directed paths in `C` with the same initial and terminal
   vertices have congruent lengths modulo three.
4. The period of `C`, namely the greatest common divisor of its directed
   closed-walk lengths, is divisible by three.

Equivalently, the constant edge cochain `1` is exact precisely when every
relative-identity positive word is topology-neutral.

#### Proof

`(2)->(1)` follows by summing (3.2) around a closed walk.  It also gives
`(3)` by summing along two paths with common endpoints.

Assume `(1)`.  Fix a root `o`.  For a vertex `v`, choose any directed path
from `o` to `v` and define `phi(v)` to be its length modulo three.  This is
well defined: if `P,Q:o->v` are two choices, strong connectivity supplies
a directed path `R:v->o`; both `PR` and `QR` are closed, so their lengths
are zero modulo three and `|P|=|Q| (mod 3)`.  Extending a path by one edge
gives (3.2).  Thus `(1)->(2)`.

Condition `(3)` implies `(1)` by comparing an arbitrary closed walk at
`o` with the length-zero path.  Finally, every closed-walk length is
divisible by three exactly when their gcd is divisible by three, proving
the equivalence with `(4)`. `square`

### Corollary 3.2 (sharp dichotomy)

In every strongly connected state component exactly one of the following
happens.

* **Phase lock:** the potential (3.1) exists, and no positive
  relative-identity aligned word can fuse the three old cycles.
* **Phase break:** there is a directed closed walk of length nonzero modulo
  three.  Decomposing it into simple directed cycles shows that there is a
  simple directed cycle of length nonzero modulo three.

If that simple cycle has a physically simple realization, it is the exact
state-returning fusion macro of Theorem 2.1.

### Corollary 3.3 (two-path certificate)

It is enough to find two directed paths `P,Q:x->y` in one state component
such that

\[
                              |P|\not\equiv |Q|\pmod3.             \tag{3.3}
\]

Indeed, append one common directed return path `R:y->x`.  The two closed
walks `PR,QR` have different residues, so at least one has nonzero residue.

This is often easier than constructing a closed macro directly: one may
build two literal transports with the same complete input and output state
but different numbers of positive sites.

## 4. The exact deck-stabilizer boundary

Relative identity is stronger than zero target current.  For a fixed
initial state `Omega`, let `mathcal D(Omega)` be its complete
occurrence-summed triangular target deck, including every depth and every
named compiler-relevant class.  Define

\[
 \operatorname{Stab}_{\cal D}(\Omega)
   =\{g:{\cal D}(g\Omega)={\cal D}(\Omega)\}.                  \tag{4.1}
\]

For a raw `k`-site holonomy `H`, put

\[
                              \bar H=\tau^{-k}H.                \tag{4.2}
\]

The exact terminal current condition for this fixed routed word is

\[
                 \boxed{\bar H\in\operatorname{Stab}_{\cal D}(\Omega).}
                                                                    \tag{4.3}
\]

The relative-cycle theorem uses the sufficient special case `bar H=I`.
A nonidentity stabilizer element may preserve the target multiset while
permuting histories or occurrence providers.  Therefore a phase potential
on the full-state graph rules out relative-identity macros only; it does
not rule out all zero-current macros unless one additionally proves that
the relevant deck stabilizer is trivial, or that deck equivalence is a
transition congruence to which the same period theorem descends.

This distinction is essential.  Raw tag identity is too strong because it
forces `3|k`; relative state identity is proof-safe but may still be
unnecessarily strong; (4.3) is exact.

## 5. Boundedness and the exact local target

The period theorem alone does not give an additive bound.  A useful PBBS
application needs a **uniform bounded phase breaker**: a constant `K`,
independent of the dimension, and for every sufficiently large dimension a
physically simple state cycle of length at most `K` and nonzero modulo
three.  A two-site or four-site cycle is the preferred instance.

Conversely, a uniform proof that every admissible complete-state component
has a phase potential (3.1) is an exact no-go for all positive aligned
clean-`C6` macros using relative identity.  To turn it into a no-go for all
zero-current macros one must also control the deck stabilizer (4.1).

The remaining local problem can therefore be stated without reference to
a particular proposed word:

> **Bounded phase-break lemma.**  Exhibit two physically plantable literal
> complete-state transports with common endpoints and lengths differing
> modulo three, using a uniformly bounded number of pairwise disjoint PBBS
> resources.

Together with the existing lower occurrence transport, residence packet,
and all-depth fan coboundary theorem, this lemma supplies a topology-changing
zero-fan-current local macro.  Global packing, regeneration, common-cap
compatibility, and the final linear opening remain separate requirements.

## 6. Scope

Proved here:

1. the exact directed-cycle formulation of relative-identity fusion;
2. the mod-three phase-potential obstruction;
3. the equivalence between phase breaking, unequal-length same-endpoint
   transports, and a non-three-periodic state component; and
4. reduction to one uniformly bounded physical phase breaker.

Not proved here:

1. that the PBBS complete-state transition graph contains a phase breaker;
2. that an abstract state cycle has disjoint physical owners and halos;
3. whether a useful nonidentity deck stabilizer element is physically
   realizable;
4. a global packing or regenerative induction; or
5. `nu(k)<=B(k)+O(1)`.
