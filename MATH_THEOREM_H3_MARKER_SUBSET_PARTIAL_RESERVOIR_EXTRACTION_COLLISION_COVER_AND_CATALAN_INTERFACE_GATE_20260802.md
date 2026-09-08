# Marker-subset partial reservoirs: exact collision cover and Catalan interface gate

**Date:** 2026-08-02  
**Lane:** H3, protected upper host / pure theorem  
**Status:** exact internal reservoir, exact `k=17` two-frame conflict
decomposition, exact `3--5`-frame extraction formulation, and all-`k`
owner/all-named-target packing scale.  No q1 SAT, host occurrence embedding,
connector realization, or compiler claim is made.

> **Finite-host supersession.**  The historical status passages below
> predate the connected rank-ten-complete first-58/open-3 factor.  That
> positive factor retains all 986 paths but is exactly nonresident: 5,372
> cyclic short runs, no legal depth-three opening, and 11,640 maximal-erosion
> mismatches at the best cut.  Its optimal three-particle monotone-staircase
> fibre also has loss at least 48,548 against budget 7,401.  Consequently the current target is not the
> source atlas over that fixed chronology.  It is a residence-aware factor
> reselection with a nonempty occurrence-labelled source fibre; see
> `MATH_THEOREM_H3_K17_MARKER58_RESIDENCE_AWARE_FACTOR_SOURCE_FIBRE_AND_DEEP_UPPER_RETHREAD_GATE_20260802.md`.
> The named-resource packing and collision-tensor theorems in this note
> remain valid.

## 1. Generalized marker-subset reservoir

Put

\[
 q=d+2,\qquad r=c+q-1.
\]

Assume \(q\ge4\), \(c\ge2\), and \(1\le a\le c-1\), the literal range of
the fixed-base buffered module theorem.

Fix disjoint sets `D,V,G` partitioning `[k]`, with

\[
 |D|=a\ge1,\qquad |V|=q,
 \qquad |G|=k-q-a,                                      \tag{1.1}
\]

and fix \(\beta\in D\), distinct \(w,h\in V\), and an oriented cyclic
order \(\sigma\) on `V`.  For every

\[
                  X\in{G\choose c-a},                    \tag{1.2}
\]

take the literal length-`q` primitive facet module with core

\[
                         C_X=D\cup X.                     \tag{1.3}
\]

Its complete named deck is

\[
\begin{array}{c|c}
\text{role}&\text{resource}\\ \hline
P&(D-\{\beta\})\cup X\cup\{w\},\\
H&D\cup X\cup\{h\},\\
I_{j,u}&D\cup X\cup I_{j,u}(\sigma),\quad
                   2\le j\le q-2,\ u\in\mathbb Z/q,\\
O_v&D\cup X\cup(V-\{v\}),\quad v\in V.
\end{array}                                                \tag{1.4}
\]

### Theorem 1.1 (exact marker-subset reservoir)

The family (1.2) has exactly

\[
                    N(k,q,c,a)={k-q-a\choose c-a}          \tag{1.5}
\]

literal modules.  All owners and all named targets in (1.4) are pairwise
distinct inside the family.  Each named resource determines its unique
module by intersection with `G`.

#### Proof

Every row in (1.4) is a disjoint union of its fixed part in `D union V`
and the variable set \(X\subseteq G\).  Equality of two same-rank resources
therefore forces equality of their selected tag role and of `X`.  The
literal primitive theorem supplies the source word, one primitive `P`, one
primitive `H`, and `d` short `H` buffers for every `X`. \(\square\)

This is a resource-simple **reservoir of modules**, not one connected host
packet.  Its per-module named-deck size is

\[
                         q^2-2q+2.                         \tag{1.6}
\]

## 2. The exact `k=17` reservoir

Take

\[
 k=17,\qquad q=c=5,\qquad a=1,
 \qquad d=3,\qquad r=9.                                  \tag{2.1}
\]

Then `D={beta}`, `|G|=11`, and

\[
                         N={11\choose4}=330.               \tag{2.2}
\]

One full reservoir consumes the following pairwise distinct resources:

\[
\begin{array}{c|ccccc}
\text{rank}&5&6&7&8&9\\ \hline
\text{count}&330&330&1650&1650&1650.
\end{array}                                                \tag{2.3}
\]

It also asks for `330` primitive-`P` occurrences, `1320` depth-two `H`
occurrences, and `990` units of short-loop slack.  These are exact demands,
not a proof that the frozen protected factor supplies the required literal
occurrences.

At the target `T_0=972`, the exact source demands are

\[
 (e_4,e_2,L-H)=(972,3888,2916),                           \tag{2.4}
\]

below the `k=17` scalar capacities `(3808,7072,7403)`.  Scalar source
capacity is therefore not the finite obstruction.

For the literal integer target

\[
              T_* = \left\lceil{W\over q^2}\right\rceil=973,       \tag{2.4a}
\]

the corresponding demands are `(973,3892,2919)`, still below the same
three scalar capacities.

For two frames write

\[
 F_i=\{\beta_i\}\mathbin{\dot\cup}V_i,\qquad |F_i|=6.     \tag{2.5}
\]

The fixed-base collision tensor proves that their owner decks are disjoint
exactly when \(F_1\cap F_2=\varnothing\).  In that case their common named
resources have counts

\[
\begin{array}{c|ccccc}
\text{rank}&5&6&7&8&9\\ \hline
\text{common}&10&10&125&25&0.
\end{array}                                                \tag{2.6}
\]

Each common resource belongs to one unique module in each frame, so it is
one occurrence-labelled conflict edge.

## 3. Exact two-frame conflict decomposition

Assume the owner-disjoint case in (2.6) and put

\[
                        L=[17]-(F_1\cup F_2),\qquad |L|=5. \tag{3.1}
\]

Let \(G_{12}\) be the bipartite module-conflict graph.  A vertex is one of
the `330` modules of a frame; two vertices are adjacent when their named
decks share a resource.

### Theorem 3.1 (six bicliques plus two matchings)

There is a canonical disjoint decomposition

\[
             G_{12}=10K_2\ \dot\cup\ 10K_2\ \dot\cup\
                     5K_{5,5}\ \dot\cup\ K_{5,5}\ \dot\cup\
                     560K_1.                              \tag{3.2}
\]

The four summands are respectively the rank-5 `P`, rank-6 `H`, rank-7,
and rank-8 collisions.  Consequently

\[
 |E(G_{12})|=170,\qquad
 \nu(G_{12})=\tau(G_{12})=50,\qquad
 \alpha(G_{12})=610.                                     \tag{3.3}
\]

In particular, all `170` conflicts can be killed by deleting the same `50`
modules from either chosen side, and fewer than `50` deletions cannot work.

#### Proof

For `P`, a common target is determined by a three-set \(Z\in{L\choose3}\):

\[
 X_1=\{w_2\}\cup Z,\qquad X_2=\{w_1\}\cup Z.
\]

This gives a ten-edge matching.  For `H`, a two-set
\(Z\in{L\choose2}\) gives

\[
 X_1=\{\beta_2,h_2\}\cup Z,\qquad
 X_2=\{\beta_1,h_1\}\cup Z,
\]

and a second ten-edge matching.

At rank seven, fix \(z\in L\).  The module on side one is indexed by
\(\{\beta_2\}\cup J_2\cup\{z\}\), where \(J_2\) is one of the five
cyclic two-intervals of \(V_2\).  It conflicts with all five modules
\(\{\beta_1\}\cup J_1\cup\{z\}\) on side two.  Thus each `z` gives one
\(K_{5,5}\).  At rank eight the same construction with cyclic
three-intervals and no `L` point gives the sixth \(K_{5,5}\).

The module patterns use respectively `(one tag,three L)`,
`(marker,one tag,two L)`, `(marker,two tags,one L)`, and
`(marker,three tags,no L)`, so the components are vertex-disjoint.  The
matching and Konig identities now give (3.3). \(\square\)

This sharpens the whole-frame no-go: the `170` common values are strongly
clustered, but their exact deletion cost is `50`, not `10` and not `170`.

## 4. Exact `3--5`-frame partial extraction

Fix `p in {3,4,5}` candidate frames.  Let \({\cal M}_i\) be their `330`
modules and let \({\cal D}(m)\) be the complete named deck of module `m`.
Let `B` be the already protected owner/q1 bank, and let \(e_m\in\{0,1\}\)
be an independently authenticated host-occurrence eligibility bit.  It is
`1` only when the fixed host contains the literal source/owner occurrences,
q1 roles and all protected local guards required by `m`.

The following `0--1` packing is the exact named-resource extraction:

\[
\begin{array}{ll}
\text{maximize}&\displaystyle\sum_m x_m\\[1mm]
\text{subject to}&x_m\le e_m,\\
&x_m=0\quad\text{if }{\cal D}(m)\cap B\ne\varnothing,\\
&\displaystyle\sum_{m:R\in{\cal D}(m)}x_m\le1
                  \quad\text{for every named resource }R,\\
&x_m\in\{0,1\}.
\end{array}                                                \tag{4.1}
\]

### Theorem 4.1 (collision-cover equivalence)

Let `G` be the occurrence-labelled conflict graph on the eligible,
unblocked modules, with an edge for every pair sharing a named resource.
Then (4.1) is maximum independent set in `G`.  Equivalently, if `F` is the
set of forced deletions from the original `pN` modules,

\[
 \operatorname{OPT}=|V(G)|-\tau(G)=pN-|F|-\tau(G).       \tag{4.2}
\]

All edges and their resource provenance are generated exactly by the
partial-assignment collision tensor; no q1 formula is needed.  A resource
occurring in three or more frames simply induces a clique, so pairwise
constraints remain exact.

#### Proof

Internal simplicity gives no edge inside a frame.  The resource inequalities
say precisely that no conflict edge has both endpoints selected.  Taking
the complement of a selected independent set gives a vertex cover and vice
versa, proving (4.2). \(\square\)

At `k=17`, the floor-scale target used in the prompt is

\[
 T_0=\left\lfloor{W\over q^2}\right\rfloor
     =\left\lfloor{24310\over25}\right\rfloor=972.        \tag{4.3}
\]

With no preblocked modules, (4.2) gives the exact thresholds

\[
\begin{array}{c|ccc}
p&3&4&5\\ \hline
pN-T_0&18&348&678.
\end{array}                                                \tag{4.4}
\]

For the literal integer target \(\lceil W/q^2\rceil=973\), replace these
budgets by `(17,347,677)`.  Every later 986-module orbit bank exceeds both
targets.

Thus a three-frame solution exists exactly when all collisions can be hit
by `18` module deletions.  Theorem 3.1 gives an immediate filter:

> If a three-frame candidate contains even one owner-disjoint frame pair,
> it cannot retain `972` modules.

Indeed that pair alone has matching number `50`.  Therefore any viable
three-frame design must use three overlapping six-coordinate supports and
every pair conflict graph must have matching number at most `18`.

For four and five frames, the exact residual budgets are `348` and `678`.
These cases are not proved feasible, but (4.1) is a small, fail-closed
packing problem with respectively `1320` and `1650` module variables, rather
than a q1 SAT instance.

### Theorem 4.2 (clustered pair-cover certificate)

For every pair `i<j`, choose any occurrence-labelled vertex cover
\(C_{ij}\) of its bipartite conflict graph.  Then

\[
 C=F\cup\bigcup_{i<j}C_{ij}                               \tag{4.5}
\]

covers the complete multi-frame conflict graph.  Hence at least

\[
                         pN-|C|                            \tag{4.6}
\]

modules survive.  In particular, deliberate collision clustering is
certified by the **union size** in (4.5), not by the number of common
resources.  Conversely the complement of every valid extraction is one
global vertex cover, so minimizing the clustered union is the exact target.

For an owner-disjoint pair, Theorem 3.1 supplies a canonical one-sided
`50`-module cover.  If several pair covers reuse the same module deletions,
their cost is paid once in (4.5).  This is the precise finite mechanism by
which four or five partial reservoirs could reach (4.3).

## 5. Protected-host and topology gate

Named-resource simplicity is necessary but does not embed a module into the
frozen protected owner/q1 factor.  Because that factor uses each owner once,
the five owner labels of a `k=17` module force its candidate host positions.
The eligibility bit \(e_m\) in (4.1) must replay at those occurrences:

1. the literal length-five source word and directed q1 atoms;
2. the intended rank-eight q1 colours and their occurrence footprints;
3. the local residence/age collars and protected-turn exclusions; and
4. avoidance of the frozen packet, banks and compiler reservations.

This replay makes (4.1) a unary host-eligibility prefilter only.  Two
individually eligible modules may still compete for source, guard or compiler
occurrences.  The complete joint footprint/capacity system is Theorem 8.3.

Each accepted primitive module is initially a separate component unless an
authenticated host path already contains it.  If a connector joins at most
`h` current components, component rank can drop by at most `h-1`; joining
`T` isolated modules to one component therefore needs at least

\[
                         \left\lceil{T-1\over h-1}\right\rceil \tag{5.1}
\]

connector events.  An exact joint formulation adds connector variables,
their owner/q1/upper footprints, socket capacities, and a rooted graphic
spanning-tree or flow certificate to (4.1).  This is a packing-plus-graphic
problem; the collision tensor alone supplies neither connectors nor
regeneration.

The induced owner-adjacency graph inside one frame is exactly

\[
                         J(k-q-a,c-a)\mathbin\square K_q. \tag{5.2}
\]

The `K_q` factor contains every horizontal Johnson adjacency within one
module; only the `q` edges of the cyclic order \(C_q\subset K_q\) are native
module edges.  A Johnson edge changes `X` by one exchange while retaining
the omitted tag.
These vertical edges have a different palette profile:

\[
\begin{array}{c|cc}
&|\text{lower}\cap G|&|\text{immediate upper}\cap G|\\ \hline
\text{horizontal}&c-a&c-a\\
\text{vertical}&c-a-1&c-a+1.
\end{array}                                                \tag{5.3}
\]

Thus Johnson connectivity is only an abstract topology scaffold.  Replacing
a native edge by a vertical edge does not preserve the immediate palettes;
an authenticated role converter or explicit lower/upper tickets are
necessary.

Assume the ambient factor has `W` native edges and is surjective on the `U`
immediate-upper targets.  If \(R_{\rm nat}\) module edges remain native and
\({\cal C}_{r+1}\) is their set of distinct active caps, their exact internal
repeat debt is

\[
                    D_{r+1}=R_{\rm nat}-|{\cal C}_{r+1}|.  \tag{5.3a}
\]

Every intact
length-`q` module has one rank-`(r+1)` cap repeated on all `q` native edges.
If caps of different modules collide, the repeat debt only increases.  Thus
`T` intact modules consume **at least** `(q-1)T` repeat units.  At `k=17`,

\[
 W-U={17\choose9}-{17\choose10}=4862.                    \tag{5.4}
\]

Consequently the floor-scale `972` intact modules consume at least `3888`
repeat units and leave at most `974` for the protected seed and exterior.
The literal target `T_*=973` consumes at least `3892` and leaves at most
`970`.  These are necessary scalar conditions, not chronology or connector
constructions.

## 6. Exterior language: bounded types, unbounded occurrences

For fixed `q`, the reservoir has \(q^2-2q+2\) named **role types** per module,
and the
collision tensor is a bounded partial-assignment grammar.  This is not a
dimension-uniform bounded exact exterior.  Every physical resource retains the module label
`X`, recovered by intersection with `G`; a fixed protected matching,
chronology or compiler may distinguish all of them.

For a selected set `S`, an exact common exterior is obtained by the total
occurrence partition and fibre-constancy criterion of the H3 common-exterior
theorem.  A quotient dropping `X` is sound only if an authenticated
automorphism of the **whole** host, protected bank, connector atlas and
compiler transports the corresponding occurrences.

There is a sharp conditional lower bound.  If each of `t` module sockets has
a private exterior capacity which can independently be free or occupied,
then any exact decomposition must absorb or expose all `t` capacities.
If `s` is the absorbed physical-support budget and `b` the number of distinct
native boundary coordinates, then

\[
                         s+b\ge t.                         \tag{6.1}
\]

Likewise, without internal connectors the topology requires a linear number
of physical socket uses by (5.1).  A protected internal packet which absorbs
the selected modules and exports `O(1)` standardized ports is one sufficient
route to a bounded exterior.  An authenticated whole-host symmetry or another
correlated interface theorem could also compress it.  Absent either kind of
certificate, bounded exterior remains open.

## 7. General Catalan-scale accounting

Let

\[
 s=k-r=k-c-q+1,\qquad W={k\choose r}.
\]

The exact reservoir-to-owner ratio is

\[
 {N(k,q,c,a)\over W}
 =s\,{r!\over(c-a)!}\,{(k-q-a)!\over k!}.                 \tag{7.1}
\]

If \(r/k\to1/2\) and \(q+a=o(k)\), then

\[
 {N(k,q,c,a)\over W}
 =2^{-(q+a)}\exp\!\left(O\!\left(
 (q+a)|r/k-1/2|+(q+a)^2/k\right)\right).                 \tag{7.1a}
\]

It is asymptotic to \(2^{-(q+a)}\) when both error terms tend to zero.  At
the canonical singleton-base scale the correction is
nontrivial: \(N/W\sim2^{-(q+1)}e^{-\pi/16}\).  In either case one full
reservoir is tiny, and obtaining \(T=\Theta(W/q^2)\) modules requires
\(2^{q+a+o(q+a)}/q^2\) partial frames in general.  This sharpens to
\(\Theta(2^{q+a}/q^2)\) when the exponent error in (7.1a) is `O(1)`, as in
the canonical singleton-base regime.  The whole-frame collision theorem
explains why those frames must be split.

The splitting is now proved at order scale for singleton bases.

### Theorem 7.1 (all-`k` clustered-pruning bank)

For every sufficiently large canonical parameter set, there is an
unconditional family of

\[
                         \Omega(W/q^2)                     \tag{7.2}
\]

completely labelled length-`q` modules whose owners and every named target
are pairwise disjoint.

#### Proof input

The fixed-base collision theorem samples
\(R=\Theta(2^q/q^2)\) singleton frames.  A second-frame resource cylinder
fixes one exact trace of the first module core on the other-only support;
there are only \(q^2-2q+2\) such traces, with no extra first-start factor.
Uniform hypergeometric trace probability is `O(2^-b)`, while the exponential
moment of two support intersections is `O(1)`.  Hence expected ordered-pair
damage is `O(M_1 q^2/2^q)`.  Deleting every cross-bad module leaves
`Omega(W/q^2)` modules.  This is Theorem 9.5 of the frozen collision-tensor
note. \(\square\)

It closes the asymptotic owner/all-named-target **scale**, not a prescribed
leading constant.  The independent audit gives the exact protected named-
resource extension.  For a forbidden bank \({\cal D}\), put

\[
 \Psi({\cal D})={|{\cal D}_c|\over{k\choose c}}
 +{|{\cal D}_{c+1}|\over{k\choose {c+1}}}
 +q\sum_{j=2}^{q-2}{|{\cal D}_{c+j}|\over{k\choose {c+j}}}
 +q{|{\cal D}_r|\over W}.                                \tag{7.2a}
\]

If \(\Psi({\cal D})\le\psi<1\), reducing the sampling constant leaves
\(\Omega(W/q^2)\) modules avoiding the bank.  This protects named resources,
not physical positions or compiler incidences.

The same audit closes aggregate occurrence **types** up to the conductor.
Let \(A=(A_0,\ldots,A_{r-1})\) be the canonical Ferrers age-signature
vector.  Assume
\(d\ge4\), \(d+1<r\), and
\(A_{d-3},A_{d-2}\ge{\cal Q}+1\), with the required finite conductor range
checked.  With \({\cal Q}=Q_{r,d}\), every integer

\[
 0\le t\le \min\left\{
 A_{d+1}-{\cal Q}-1,
 \left\lfloor{A_{d-1}-{\cal Q}-1\over q-1}\right\rfloor,
 \left\lfloor{L-H\over d}\right\rfloor\right\}          \tag{7.2b}
\]

can reserve \(t e_{d+1}+(q-1)t e_{d-1}\) while the residual age vector
remains integrally decomposable, subject to the stated neighboring-coordinate
conductor margins.  This is not a physical-position embedding.  In
particular, `L-H=o(W/q)` is a genuine scalar obstruction to this buffered
module family at scale `W/q^2`.  This conductor corollary does not apply to
the finite `k=17,d=3` bank; its scalar counts are checked directly in (2.4).

For `k=2m+1` at the central owner rank `r=m+1`, the SCD component count is

\[
 C_{\rm SCD}={2W\over m+2}.                               \tag{7.3}
\]

At the canonical buffered scale \(q^2/r\to\pi/4\), hence

\[
 {W/q^2\over C_{\rm SCD}}\longrightarrow {2\over\pi}.     \tag{7.4}
\]

So the desired partial-reservoir inventory is genuinely Catalan-scale in
component count, not an `O(1)` sidecar.  Its module owners total

\[
                         qT=\Theta(W/q)=o(W),              \tag{7.5}
\]

and a connector of `O(q)` protected support per component would also cost
`O(W/q)=o(W)`.  The scalar budget is therefore compatible with a Catalan
connector forest.  The live gate is joint selection: the collision cover,
host occurrence eligibility, connector graphic independence, residence and
upper sidecars must hold on the same modules.

The native immediate-upper row is more restrictive.  For an immediate-upper-
surjective `W`-edge factor at odd central `k=2r-1`,

\[
                         W-U=\operatorname{Cat}_r.         \tag{7.6}
\]

If all `q` native edges survive in every module, then

\[
                         (q-1)T\le W-U,                   \tag{7.7}
\]

which imposes `T=O(W/q^3)` at the canonical scale; its scalar ceiling is
`Theta(W/q^3)`.
More generally, if \(R_{\rm nat}\) native edges survive from `T` selected
modules, then

\[
                         R_{\rm nat}-T\le W-U.             \tag{7.8}
\]

Thus a `Theta(W/q^2)` construction must replace at least

\[
            \max\{0,(q-1)T-(W-U)\}                        \tag{7.9}
\]

native edges by new-cap edges; this lower bound is `Theta(W/q)` at that
construction scale.  The vertical Johnson edges cannot do this
palette-neutrally by (5.3), so the Catalan connector theorem must include
the role converter/ticket sidecar explicitly.

## 8. Frozen `Z_17` quotient bank

The finite quotient extraction is now solved at the complete named-resource
layer by
`MATH_THEOREM_K17_MARKER_RESERVOIR_Z17_ORBIT_PACKING_20260802.md`.
Identify the coordinates with \(\mathbb Z_{17}\) and let \(\rho\) be cyclic
translation.  For a base module `m`, let \(E(m)\) be the typed rotation-orbit
IDs of its `1,1,5,5,5` resources at ranks `5,...,9`.

### Theorem 8.1 (orbit lift)

If every `E(m)` has size `17` and the sets `E(m)` are pairwise disjoint for
base modules in `S`, then developing `S` by all powers of \(\rho\) gives
`17|S|` modules whose complete named decks are pairwise disjoint.  The
converse also holds.

#### Proof

The action of \(\mathbb Z_{17}\) is free on every nonempty proper subset of
`[17]`.  Thus one typed orbit contains exactly the 17 physical rotations of
one resource.  Internal orbit simplicity prevents collisions within one
developed module orbit, and disjoint `E(m)` prevent collisions between two
orbits.  Conversely, equality of orbit IDs produces an actual collision
after the unique aligning rotation. \(\square\)

The frozen orbit-conflict graph has

\[
 329\ \text{admissible base modules},\qquad
 1663\ \text{conflict edges},                             \tag{8.1}
\]

and the authenticated independent set has size `96`.  Its development has

\[
 1632\ \text{modules},\qquad 27744\ \text{pairwise distinct named resources},
                                                               \tag{8.2}
\]

with rank counts `(1632,1632,8160,8160,8160)`.  The independent replay also
checks every literal four-window owner identity.

The original `W/q^2` target follows without another search.

### Corollary 8.2 (the exact 58-orbit target)

Any `58` of the frozen `96` base modules develop to

\[
  58\cdot17=986>972                                      \tag{8.3}
\]

pairwise named-resource-disjoint literal modules.  Their rank-5 through
rank-9 counts are

\[
                         (986,986,4930,4930,4930).         \tag{8.4}
\]

On the quotient shores they consume `(58,58,290,290,290)` resource orbits,
well below the exact capacities `(364,728,1144,1430,1430)`.  The exact
quotient matching formulation was the 17-uniform hypergraph packing

\[
 \sum_m x_m\ge58,\qquad
 \sum_{m:o\in E(m)}x_m\le1\quad(o\text{ a typed resource orbit}), \tag{8.5}
\]

or, equivalently, independent set in the 329-vertex conflict graph.  The
frozen 96-set is a strict positive certificate for (8.5); no maximality is
claimed or needed.

Equation (8.5) is the unprotected bank.  With a protected named bank, replace
the right side by the residual orbit capacity \(b_o^{\rm res}\) and include
the orbit multiplicity \(a_{m,o}\):

\[
                         \sum_m a_{m,o}x_m\le b_o^{\rm res}. \tag{8.5a}
\]

The frozen 96-set does not by itself prove that 58 of its vertices survive a
particular protected bank; that is part of the joint host selection.

Orbit completion is not required for a nonsymmetric physical host.  Let

\[
             \widetilde{\cal M}={\cal I}_{96}\times\mathbb Z_{17}  \tag{8.5b}
\]

be the `1632` individually labelled developed modules.  The orbit theorem
proves that **every subfamily** of \(\widetilde{\cal M}\) is named-resource
simple.  Therefore the unrestricted physical target is to select any
`T_*=973` eligible labels from (8.5b), with named-deck counts

\[
                         (973,973,4865,4865,4865).          \tag{8.5c}
\]

Selecting `58` complete base orbits and obtaining `986` modules is a useful
quotient-symmetric sufficient route, not a necessary restriction on the
protected host.

The full 96-orbit bank is a reservoir, not an intact protected-host packet.
It needs `6528` occurrence-labelled source/buffer positions.  These have
zero local four-window failures but are not bound to physical host
occurrences.  A 58-orbit subbank needs `3944` such positions, while an
arbitrary `973`-module physical subbank needs `3892`.  These counts are the
four `H`/buffer roles only; add respectively `1632`, `986`, or `973`
primitive-`P` occurrences unless those are independently forced.

For each individually labelled physical module `u`, let \({\cal E}_u\) be
the complete atlas of **joint** host embeddings.  One entry places all four
`H`/buffer roles and also the primitive `P` occurrence unless an
independently replayed owner-forcing theorem fixes it.  It replays the
literal directed source word, fixed matching/root condition, q1 roles,
collar, protected bank and compiler reservations.  Let \(P(e)\) be its
complete physical or quotient-occurrence footprint.  Let \({\cal C}\) be
the exhaustive family of all minimal cross-module forbidden tuples of atlas
entries which are not already represented by a named-resource or
footprint-capacity row.

### Theorem 8.3 (exact physical-binding formulation)

A selected physical module bank has a collision-free physical source
binding if and only if

\[
 \sum_{e\in{\cal E}_u}z_{u,e}=x_u,\qquad
 \sum_{u,e}a_{e,p}z_{u,e}\le b_p,\qquad
 z_{u,e}\in\{0,1\},                                      \tag{8.6}
\]

for every module `u` and physical occurrence `p`, where
\(a_{e,p}\) is the exact footprint multiplicity, together with the residual
named protected-resource rows, written physically as

\[
                         \sum_u a_{u,R}x_u\le b_R^{\rm res}, \tag{8.6b}
\]

and the residual tuple rows

\[
                 \sum_{(u,e)\in C}z_{u,e}\le |C|-1
                         \qquad(C\in{\cal C}).             \tag{8.6e}
\]

#### Proof

Every physical binding selects one complete atlas entry per chosen module,
occurrence injectivity gives the capacity rows, and no forbidden tuple may
be wholly selected.  Conversely, the chosen joint entries already contain
every within-module chronology and local guard; the capacity, named and
tuple rows exclude every cross-module incompatibility, so their union is a
physical binding. \(\square\)

Suppose now that \({\cal C}=\varnothing\), equivalently that every
cross-module incompatibility is represented by a shared capacity token.
After cloning a capacity-`b_p` occurrence into `b_p` physical slots, replace
each atlas entry by all concrete assignments of its uses to token clones;
write \(\widehat{\cal E}_u\) for the resulting family and regard its
footprints as a hypergraph \({\cal H}_u\).  This
gives a concrete sufficient expansion theorem.  If all footprints have size
at most `g` and, for every nonempty module set `I`,

\[
 \nu\!\left(\bigcup_{u\in I}{\cal H}_u\right)>g(|I|-1),  \tag{8.6a}
\]

then the Aharoni--Haxell rainbow-matching theorem selects one disjoint joint
embedding for every module in the fixed candidate index set.  Condition
(8.6a) is sufficient, not necessary, and says nothing about the later
connector/voltage graph.

There is also a directly auditable bounded-codegree criterion.  For a fixed
candidate set `S`, put

\[
 L=\min_{u\in S}|\widehat{\cal E}_u|,
 \qquad
 \Delta=\max_{\substack{u\ne v\in S\\e\in\widehat{\cal E}_u}}
   |\{f\in\widehat{\cal E}_v:P(e)\cap P(f)\ne\varnothing\}|. \tag{8.6c}
\]

If

\[
                         L>(|S|-1)\Delta,                 \tag{8.6d}
\]

then (8.6) has a solution for all modules in `S`.  Indeed, after any `j`
entries have been chosen, each unembedded module has lost at most
`j Delta` entries, so greedy selection continues.  This criterion preserves
all local zero gates because they are already part of the definition of
\({\cal E}_u\).  It is sufficient only; failure of (8.6d) is not an
obstruction.

Only under \({\cal C}=\varnothing\) and a proved rectangularity hypothesis
\({\cal E}_u=\prod_r A_{u,r}\), with no cross-role factor beyond position
capacities, does (8.6) reduce to the bipartite group-transversal/Hall system

\[
 \sum_p y_{u,r,p}=x_u,\qquad
 \sum_{u,r}y_{u,r,p}\le b_p.                              \tag{8.7}
\]

Literal adjacency and collars generally make the atlas nonrectangular, so a
generic matching claim is not licensed.  If the host is genuinely
\(\mathbb Z_{17}\)-equivariant, the selection is orbit-complete, and every
used occurrence orbit is regular, (8.6) may instead be written on quotient
embeddings.  One quotient entry then represents all 17 translated modules,
equivalently `68` physical `H`/buffer roles and `17` primitive roles.  With
stabilizers, orbit-size weights remain in \(a_{e,p}\).  Without equivariance
the system uses the individually labelled modules (8.5b), and the literal
target has `3892` physical `H`/buffer demands plus `973` primitive demands
whenever the latter are not independently forced.

There is now one authenticated lower-q1 extension, but its address is fixed.
Take the **first 58** base masks in the frozen witness, develop all rotations,
and open native edge type `3` in every module.  The resulting 986 disjoint
four-edge paths extend to a rank-eight-rainbow two-factor on all 24,310
owners.  The independently replayed factor has 1,179 components, largest
component 16,643, and covers 13,307 of 19,448 rank-ten caps.  Thus this
fixed first-58/open-3 bank closes the owner/lower-q1 extension row but leaves
6,141 rank-ten holes.  No such extension is asserted for an arbitrary
58-orbit or arbitrary 973-module choice.  For those choices the b-flow or
the exact physical two-factor rows must be solved jointly with (8.6).

In the regular equivariant subclass for this fixed bank, a **new** residual
upper-aware factor has `1198*36=43128` raw binary pair options: one option
chooses the two owner endpoints and hence the rank-ten cap of a residual
facet orbit.  Owner filtering leaves `35713` primary variables in the live
solve.  Exact facet one-copy, owner degree two, and cap-cover rows are the
complete rank-eight/rank-ten quotient model.  A chronology additionally
needs quotient connectivity and a nonzero voltage.  The authenticated
1,179-component factor is non-equivariant, so this quotient system constructs
a different equivariant factor rather than upper-completing that witness.
No solve verdict is imported here.  This bounded model still does not
contain the source-state atlas (8.6), residence, ranks 11--17, or the compiler.

The immediate-upper scalar must distinguish an intact module cycle from an
opened module path.  Five native cycle edges with one common cap consume four
repeat units.  After deleting one native edge, the retained four-edge path
consumes only three repeat units.  Therefore an intact 96-orbit development
has repeat debt `4*1632=6528`, but an opened development has debt

\[
                         3\cdot1632=4896,                  \tag{8.8}
\]

only `34` beyond the global budget `4862`.  The fixed first-58/open-3
subbank has debt

\[
                         3\cdot986=2958,                   \tag{8.9}
\]

and leaves exactly `1904` repeat units for the residual factor.  The frozen
first-58/open-3 factor independently replays this equality: its 3,944
protected edges use 986 distinct caps, hence exactly 2,958 repeat units.
These are scalar identities, not an upper-complete connector construction.
They supersede the earlier unsound identification of the four `H`/buffer
source states with four repeat units.

For comparison, opening one edge in each member of an arbitrary
973-module physical subbank gives debt at least

\[
                         3\cdot973=2919,                  \tag{8.9a}
\]

and leaves at most `1943` repeat units.  Equality requires distinct caps and
neither the arbitrary lower-q1 extension nor its upper completion is
certified.

Finally, a quotient spanning tree on the 58 module orbits is not enough for
one physical component: its regular free \(\mathbb Z_{17}\)-lift has 17
copies.  For a connected quotient, a regular voltage lift is connected
exactly when the closed-walk voltages generate \(\mathbb Z_{17}\); since 17
is prime, one nonzero cycle voltage suffices.  An attachment to a host can
supply this generator only when the combined quotient is connected and the
attachment/action satisfies the same regular-cover hypotheses.  No
connector/voltage certificate is part of the frozen orbit bank.  For a
nonsymmetric 973-module selection, voltage compression is unavailable and
the literal rooted graphic/flow certificate of Section 5 must be supplied.

The authoritative hashes are:

* user-designated all-`k` collision/pruning snapshot
  `9eb1eafbf69d50ecbb324b4867057f477eac0318e046f7b2fd30994624ff9e6b`;
* current workspace theorem, including its appended proof-scope audit,
  `c5db41e006feba5f289d0264d6595b8e66be1700cb75369dea9f0790d6322c82`;
* theorem `bf072e7c74918ad729a14ba030e866de895444df85a5af02ecd2230357e40ee7`;
* witness `88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403`;
* independent orbit audit
  `28a4d4cd6e19c4c6b77a8140c85bd1fceac11421e5eea0dd8ae0e50ea8d119ab`;
* fixed first-58/open-3 q1/upper-core theorem
  `4401c1e021144b65f75a47f3e7164c38f3ea649053221f78cb95c081ba23aa08`;
* its factor
  `0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e`;
* independent factor audit
  `518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d`;
* independent upper-ledger audit
  `7afd27dc3489b20654216642b45ab84bbd0ce69ac95cee98fb4bed495db9786a`.

The weighted forbidden-bank and conductor statements use
`MATH_AUDIT_FACET_SINGLETON_RESERVOIR_CLUSTERED_PRUNING_EXTRACTION_20260802.md`;
its hash is
`f07202b2ea00e40762f994713cd74dd6bdcb2ff17b4f311af210008139104db0`.

No duplicate search is used in this note.

## 9. Exact verdict and handoff schema

At `k=17`, three to five **intact** reservoirs are impossible, and the raw
partial-frame formulation (4.1) remains exact at the named-resource layer.
The stronger cyclic quotient bank now closes named-resource extraction: a
58-orbit subbank gives 986 modules, while the full frozen bank gives 1,632.

There are two exact remaining formulations.  The unrestricted formulation
chooses any 973
eligible physical labels, solves (8.6), (8.6b), (8.6e), the physical lower-q1
two-factor/upper rows, and a literal rooted graphic/flow connector.  It has
no quotient-voltage shortcut.  The equivariant formulation fixes the
first-58/open-3 protected bank and asks a new equivariant factor to solve the
35,713-primary-variable upper quotient core together with source binding,
quotient connectivity and nonzero voltage.  The existing lower-q1 witness is
non-equivariant and therefore does not itself satisfy this formulation.
Choosing another 58 base orbits also reopens the lower-q1 extension row.

The active finite lane fixes the authenticated first-58/open-3 protected
bank.  Its lower-q1 embedding is closed, and the quotient core has one exact
connected rank-ten-complete solution.  That solution is depth-three
nonresident, so the next object is a residence-aware factor reselection with
a nonempty joint five-state source fibre, formalized in
`MATH_THEOREM_H3_K17_MARKER58_RESIDENCE_AWARE_FACTOR_SOURCE_FIBRE_AND_DEEP_UPPER_RETHREAD_GATE_20260802.md`.

A proof-grade handoff contains:

* `frames.tsv`: `(D,V,beta,sigma,w,h)` and source hashes;
* `modules.tsv`: immutable `X`, complete occurrence-labelled deck and host
  eligibility provenance;
* `collision_resources.tsv`: resource, all producing `(frame,X,role)` rows,
  tensor cell and rank;
* `conflict_graph.tsv`: deduplicated module pairs with all resource labels;
* `pair_covers.tsv`: pair matching/cover certificates and the clustered union;
* `extraction.tsv`: all `x_u`, literal objective `>=973`, protected-bank replay and
  complete resource capacities;
* `connector_atlas.tsv`: connector occurrences, footprints, sockets,
  graphic/flow certificate and quotient voltages; it may be `UNKNOWN` in a
  named-only handoff but is required for a protected-host/topology claim;
* `orbit_resources.tsv`: canonical typed orbit IDs, the frozen 96-set and
  either the selected physical 973-set or the fixed first-58/open-3 bank;
* `q1_extension.tsv`: exact physical b-flow/two-factor rows, or the frozen
  first-58 factor and the 35,713-primary-variable quotient upper core;
* `source_assignment.tsv`: the quotient or physical replay of (8.6); and
* independent replay hashes and explicit `UNKNOWN` rows.

The exact finite gain is stronger than a `3--5`-frame collision cover: cyclic
development already supplies more than the required named-resource bank.
The `6528` full-bank H/buffer occurrences are labelled but unplaced; the
literal 973-module target needs `3892`, plus 973 primitive occurrences unless
independently forced.  Even on the fixed first-58 bank, source binding,
one-component chronology, global residence, rank-ten completion, ranks
11--17 and the terminal compiler remain open.  The source and connector
atlases are necessary proof objects, not by themselves sufficient for those
later rows.
