# A full SCD funnel is a matching but not a locally invisible Catalan reservoir

Date: 2026-08-01  
Lane: four SCD funnels / owner-slot nibble / protected Catalan reservoir  
Status: exact star-load identities and a sharp near-full regularity no-go for
the natural unused owner clones.  A contracted-halo or nonnested correlated
reservoir is not excluded.

## 0. Outcome

Let

\[
 c=\operatorname {Cat}_{m-1},\qquad C=\operatorname {Cat}_m,
 \qquad 4c-C={6\over m+1}c.                         \tag{0.1}
\]

Four full SCD funnels have the correct scalar order: retaining
`C=4c-O(c/m)` of their `4c` providers would give a Catalan-size isolated
reservoir.  Two independent obstructions prevent promoting the current
product construction to that theorem.

1. The nested product already forces `Cat_(m-2)=Theta(c)` endpoint
   deletions, so it retains fewer than `C` resource-disjoint sockets for
   every `m>=22`.  The allowed loss in (0.1) is only `O(c/m)`.

2. More fundamentally, even one full funnel is not locally invisible to
   the owner-slot host.  Although its selected providers form a matching,
   the unused clone of one of its physical owner vertices has residual
   degree zero.  For every near-full subfunnel of size `c-O(c/m)`, some
   unused owner clone loses at least

   \[
                              m^2-O(m)               \tag{0.2}
   \]

   of its native `2m(m-1)` incident diamonds.  Thus its relative degree
   loss is at least `1/2-o(1)`, not `o(1)`.

Consequently the proposed reservoir cannot simply be frozen while all
unused owner clones remain in an asymptotically regular host.  A positive
Delcourt--Postle/nibble implementation must at least contract or delete a
Catalan owner halo and reanalyse the resulting irregular host.  The result
does not exclude such a contracted-halo argument, nor a nonnested
correlated four-funnel construction.

## 1. One full funnel and its four resource banks

Use

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
\]

and the four-row Greene--Kleitman matching.  For every short central chain

\[
                         S<L
\]

the funnel provider is the diamond

\[
 e_S=\bigl(azL,\ aS,\ aL,\ azS\bigr).              \tag{1.1}
\]

Thus the four reserved resource banks are

\[
\begin{aligned}
 \mathcal R&=\{azL:L\text{ a short top}\},\\
 \mathcal K&=\{aS:S\text{ a short bottom}\},\\
 \mathcal T&=\{aL:L\text{ a short top}\},\\
 \mathcal H&=\{azS:S\text{ a short bottom}\}.
\end{aligned}                                       \tag{1.2}
\]

Every bank has order `c`, and each is injective.  Hence (1.1) is indeed a
resource matching after one slot is chosen at each physical owner.

The complete owner-slot diamond host has exact native degrees

\[
 d(R)=2m(m+1),\qquad
 d(K)=2m(m-1),\qquad
 d(T^i)=2m(m-1).                                    \tag{1.3}
\]

The first identity chooses the omitted pair from an upper set and then two
owner slots.  The second chooses two exterior coordinates and two slots.
For the third, remove one of the `m` owner coordinates, add one of the
`m-1` exterior coordinates, and choose the other owner's slot.

## 2. Exact local-load functions

For an arbitrary host resource, its co-incidence with the frozen funnel is
given without approximation by

\[
\begin{array}{c|l}
\text{surviving resource}&\text{funnel resources capable of sharing a diamond}\\ \hline
R\in{[2m-1]\choose m+1}
 &\{aS\in\mathcal K:aS\subset R\},\quad
   \{T\in\mathcal T\cup\mathcal H:T\subset R\},\\[2mm]
K\in{[2m-1]\choose m-1}
 &\{azL\in\mathcal R:K\subset azL\},\quad
   \{T\in\mathcal T\cup\mathcal H:K\subset T\},\\[2mm]
T^i,\ |T|=m
 &\{azL\in\mathcal R:T\subset azL\},\quad
   \{aS\in\mathcal K:aS\subset T\},\\
 &\{H^j:H\in\mathcal T\cup\mathcal H, |T\triangle H|=2\}.
\end{array}                                         \tag{2.1}
\]

These are the exact star loads.  Multiplying one fixed compatible upper
neighbour of an owner slot by `2m` gives its exact contribution to deleted
incident diamonds: there are `m` possible lower facets and two slots for
the other owner.  The analogous factors are four for one fixed upper/lower
pair and two for one fixed lower/owner pair.  Overlaps must be handled by
literal inclusion--exclusion; raw matching load one does not control the
star damage.

## 3. The short-bottom/short-top incidence mass

Let `mathcal S` and `mathcal L` be the standard short bottoms and tops, and
form the bipartite containment graph

\[
                         S\sim L\iff S\subset L.     \tag{3.1}
\]

### Theorem 3.1 (exact incidence mass)

The graph (3.1) has

\[
 \boxed{
 |E(\mathcal S,\mathcal L)|
 ={m\over2}\operatorname {Cat}_{m-1}
 ={2m-3\choose m-2}. }                              \tag{3.2}
\]

Both shore degrees are at most `m-1`.

#### Proof

Prepend an absent step to a short top `L`.  This gives a Dyck path of
semilength `n=m-1`.  Write its first-return decomposition as

\[
                         0\,A\,1\,B,
 \qquad |A|=2i.                                      \tag{3.3}
\]

Deleting a present coordinate of `L` gives a short bottom exactly for one
of the `i+1` down-steps up to and including this first return.  There are
`Cat_i Cat_(n-1-i)` paths with the displayed value of `i`.  Therefore

\[
 |E|=\sum_{i=0}^{n-1}(i+1)\operatorname {Cat}_i
                         \operatorname {Cat}_{n-1-i}. \tag{3.4}
\]

Pair the summand indexed by `i` with the one indexed by `n-1-i`.  Their
weights add to `n+1=m`; the unweighted Catalan convolution is `Cat_n`.
This proves `|E|=(m/2)Cat_(m-1)`, and direct Catalan arithmetic gives the
binomial form.  The degree bound is immediate from the set ranks. \(\square\)

Thus one full funnel creates a **linear**, not bounded, mean star load:

\[
 {1\over c}\sum_{S\in\mathcal S}
       |\{L\in\mathcal L:S\subset L\}|={m\over2}.   \tag{3.5}
\]

## 4. A literal zero-degree surviving clone

Take the ordered binary word

\[
                         S_\star=0(01)^{m-2},        \tag{4.1}
\]

where `0` means absent and `1` present.  It is a short bottom.  Every
one-element extension `S_star+y`, `y notin S_star`, is a short top: changing
the first zero gives `1(01)^(m-2)`, while changing any later zero gives a
walk of minimum exactly `-1` and final value `-1`.

Let

                         T_\star=azS_\star.          \tag{4.2}

One clone of `T_star` is occupied by the provider (1.1); consider the other
clone.  Every host edge incident to that clone has upper resource

\[
                         T_\star+y=az(S_\star+y)    \tag{4.3}

for some `y notin S_star`.  By (4.1), every set in (4.3) belongs to the
reserved upper bank `mathcal R`.  Hence every one of the

\[
                         2m(m-1)                    \tag{4.4}

incident host edges is deleted.

### Corollary 4.1 (full-funnel regularity no-go)

Freezing one full funnel and retaining the unused clone of each physical
owner leaves a surviving owner-slot vertex of degree zero.  In particular,
the remaining host is not `(1-o(1))`-regular.

This is not a slot-assignment artefact: whichever clone is used by the
provider, the other clone has the zero star.

## 5. Near-full funnels still have constant relative damage

Retain an index set `J` of `c-q` short-chain providers.  It reserves both
the upper vertices `azL`, `L in J`, and one clone of the owner vertices
`azS`, `S in J`.

Deleting `q` vertices from each shore of (3.1) removes at most
`2q(m-1)` incidences.  Hence the induced incidence graph on `J` has at
least

\[
                         {m\over2}c-2q(m-1)          \tag{5.1}
\]

edges.  Some retained bottom `S in J` is therefore contained in at least

\[
 \rho_J\ge
 {\frac m2c-2q(m-1)\over c-q}                      \tag{5.2}
\]

retained short tops.

For the unused clone of `azS`, each such top `L` supplies exactly `2m`
distinct incident host edges whose upper resource is the reserved `azL`.
Consequently its degree loss is at least

\[
 \boxed{
 2m\,{\frac m2c-2q(m-1)\over c-q}. }                \tag{5.3}

If `q=O(c/m)`, (5.3) is

\[
                         m^2-O(m),                  \tag{5.4}

\]

whereas its native degree is `2m(m-1)`.  This proves the claimed
`1/2-o(1)` relative-loss lower bound.

### Corollary 5.1 (four-funnel natural-clone no-go)

Any putative selection of `4c-O(c/m)` providers from four full funnels
retains `c-O(c/m)` providers in each funnel.  If the unused clone of every
retained physical endpoint remains in the nibble host, at least one such
clone suffers constant relative degree loss.  Therefore the four-funnel
bank cannot be preplanted *naively* as an invisible Catalan reservoir.

The qualification is load-bearing.  One may delete or contract both clones
of every reservoir owner and then prune a larger halo.  That changes the
host and requires a new edge-count/degree theorem; (5.3) does not rule it
out.

## 6. Resource-disjoint size `C` in the current product construction

The allowed deletion from four scalar funnels is

\[
                         4c-C={6\over m+1}c=O(c/m).  \tag{6.1}
\]

The nested product theorem exhibits `Cat_(m-2)` disjoint forced tail
conflicts and proves

\[
 \nu_{\rm resource}(\text{four nested funnels})
 \le4c-\operatorname {Cat}_{m-2}<C
 \qquad(m\ge22).                                    \tag{6.2}

Since

\[
 {\operatorname {Cat}_{m-2}\over c}
 ={m\over2(2m-3)}=\Theta(1),                        \tag{6.3}

the gap in (6.2) is much larger than (6.1).  Thus the existing canonical
nested product cannot supply the proposed size-`C` isolated reservoir.

A nonnested common matching could have a different conflict graph; no
general four-funnel matching-number upper bound is proved here.  The exact
positive target would have to establish both:

1. a resource matching of order `C` across a nonnested correlated funnel
   family; and
2. a contracted-halo theorem for the owner-slot host, rather than the false
   claim that the natural unused clones retain degree `D-o(D)`.

## 7. Deterministic audit

`scratch/audit_scd_funnel_owner_slot_degree_loss_20260801.cpp` enumerates
the complete owner-slot host and removes one standard full funnel.  With
one owner clone per provider reserved, it reports for `m=3,...,8` the exact
maximum losses

\[
\begin{array}{c|rrrrrr}
m&3&4&5&6&7&8\\ \hline
\text{upper loss}&14/24&28/40&46/60&68/84&94/112&124/144\\
\text{lower loss}&10/12&22/24&38/40&58/60&82/84&110/112\\
\text{slot loss}&12/12&24/24&40/40&60/60&84/84&112/112.
\end{array}                                         \tag{7.1}

The slot row is proved for all `m` by Section 4.  The upper/lower rows are
included as an independent finite audit only; no extrapolation of their
displayed formulas is used in the theorem.
