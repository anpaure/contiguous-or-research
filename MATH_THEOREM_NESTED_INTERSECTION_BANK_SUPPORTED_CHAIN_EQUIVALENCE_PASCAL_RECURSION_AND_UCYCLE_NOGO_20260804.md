# Nested intersection banks: supported-chain equivalence, a Pascal recursion, and the natural-Ucycle boundary

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reformulation of the forced collar selector,
an unconditional flag-matroid sufficient condition, an exact conditional
Pascal splice, and an infinite-family obstruction to the natural singleton-
window Ucycle route.  This note does **not** construct the required resident
factor and does not prove `nu(k)<=B(k)+O(1)`.

## 0. Outcome

Let

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},\qquad |Q_i|=q,
 \tag{0.1}
\]

be a cyclic oriented Johnson factor on the complete rank-`q` layer, and
assume every positive coordinate run has length at least `d`.  Put

\[
 I_{i,j}=\bigcap_{u=0}^{j}Q_{i+u},
 \qquad 1\le j<d.
 \tag{0.2}
\]

Then `|I_(i,j)|=q-j`.  The forced-departure theorem in
`MATH_THEOREM_RENEWAL_BLOCKS_FORCED_DEPARTURE_COLLARS_AND_ATOMIC_SEPARATION_20260804.md`
says that a right-aligned consecutive top collar at root `i` must use this
flag.

This note proves five facts.

1. The desired nested banks are **exactly** a partition of the Boolean band

   \[
   \mathcal B=\bigcup_{j=1}^{d-1}{[k]\choose q-j}
   \tag{0.3}
   \]

   into saturated chains ending in rank `q-1`, with the chain ending at
   `S` required to be a prefix of one actual forced flag from the fibre
   `I_(i,1)=S`.

   Once the chain partition is fixed there is no remaining root-SDR: fibres
   belonging to different top sets are disjoint.

2. Equivalently, the banks are nested bases of the partition matroids whose
   parts are the colour fibres of `i -> I_(i,j)`.  A genuine flag-matroid
   sufficient condition is that these partition matroids form a quotient
   chain.  Abstract Boolean deletion maps satisfying this quotient condition
   always exist by normalized matching.

3. A transition-independent quotient atlas is impossible.  The pull identity

   \[
   p_s(T+\beta)=p_{s-1}(T)+\beta
   \tag{0.4}
   \]

   cannot hold for every incidence `T subset T+beta`.  Thus the deletion
   maps and the allowed factor transitions must be co-selected; one cannot
   first choose globally pull-equivariant Boolean parent maps and then invoke
   an arbitrary Johnson factor.

4. The collar selector has an exact Pascal recursion.  A `z`-free rank-`q`
   child and a `z`-containing lift of a rank-`q-1` child combine without any
   colour loss whenever their openings are triangularly seam-safe.  Pascal's
   identity then gives every collar target exactly once.

5. A standard singleton-window Ucycle would turn (0.2) into ordinary shorter
   suffix windows, so it is genuinely relevant.  But it leaves the new
   **multi-radius suffix-chain exact cover** completely open.  Moreover it
   cannot be an all-dimensional route: for

   \[
   k=2m,\qquad q=m-1,\qquad m=2^a-1,
   \tag{0.5}
   \]

   every cyclic singleton-window packing by distinct rank-`q` sets omits at
   least `m=k/2` rank-`q` sets.  Hence this architecture cannot give an
   `O(1)`-omission owner factor in infinitely many even dimensions.

The exact remaining collar problem is therefore:

\[
 \boxed{
 \text{construct one resident oriented factor whose actual forced
 flag-prefix hypergraph exactly covers }\mathcal B.}
 \tag{0.6}
\]

This is narrower than arbitrary named flag Hall, but stronger than an atomic
rank histogram or ordinary Ucycle existence.

## 1. The forced flag-prefix hypergraph

Let `E=Z_N` be the root-index set.  For `1<=j<d`, write

\[
 \mathcal X_j={[k]\choose q-j},\qquad
 \phi_j:E\longrightarrow\mathcal X_j,
 \quad \phi_j(i)=I_{i,j}.
 \tag{1.1}
\]

For `0<=h<d`, define the flag prefix

\[
 C(i,h)=\{I_{i,1},I_{i,2},\ldots,I_{i,h}\},
 \qquad C(i,0)=\varnothing.
 \tag{1.2}
\]

For positive `h` this is a saturated descending Boolean chain.  Let
`H_Q` be the hypergraph on vertex set `mathcal B` whose columns are all
`C(i,h)`, with their root labels retained.

### Theorem 1.1 (supported band-chain equivalence)

The following are equivalent.

1. There are nested banks

   \[
   R_{d-1}\subseteq\cdots\subseteq R_1\subseteq E
   \tag{1.3}
   \]

   such that `phi_j` maps `R_j` bijectively onto `mathcal X_j` for every
   `j`.

2. There is a height function

   \[
                         h:E\longrightarrow\{0,1,\ldots,d-1\}
   \tag{1.4}
   \]

   for which the nonempty columns `C(i,h(i))` partition `mathcal B`.

3. The band `mathcal B` has a partition into saturated chains, all ending
   in rank `q-1`, such that the chain ending at each
   `S in mathcal X_1` is a prefix of an actual forced root flag

   \[
   I_{i,1}=S\supset I_{i,2}\supset\cdots\supset I_{i,h}
   \tag{1.5}
   \]

   for some root `i`.

Equivalently, the zero-one incidence system

\[
 \sum_{(i,h):\,X\in C(i,h)}x_{i,h}=1
 \qquad(X\in\mathcal B)
 \tag{1.6}
\]

has an integral solution.  No separate at-most-one-root row is needed in
(1.6): two positive columns belonging to the same root both contain
`I_(i,1)` and therefore cannot both be selected.

#### Proof

Assume item 1 and put

\[
 h(i)=\max\{j:i\in R_j\},
 \tag{1.7}
\]

with maximum zero when `i notin R_1`.  At layer `j`, precisely the columns
with `h(i)>=j` contribute `I_(i,j)`.  Their root set is `R_j`, and the
bijection hypothesis says that these values partition `mathcal X_j`.
Different ranks are disjoint, so all columns together partition
`mathcal B`.  This proves item 2.

Every positive column in item 2 is a saturated chain ending at rank `q-1`.
Since the rank-`q-1` layer is covered exactly once, there is exactly one
column ending at each `S in mathcal X_1`.  This is item 3.

Conversely, choose for each chain in item 3 one witnessing root.  Witnesses
for chains with different tops are automatically different, because the
fibres `phi_1^(-1)(S)` are disjoint.  Give a witness the height of its chain
and all unused roots height zero.  At every depth `j` the chains meeting
`mathcal X_j` give exactly one occurrence of every member of that layer.
Thus `R_j={i:h(i)>=j}` satisfies item 1.

Finally, (1.6) is exactly the assertion that the selected columns partition
the vertex set.  The shared top vertex proves the stated automatic root
capacity. `square`

### Corollary 1.2 (the target chains themselves are not the obstruction)

If `q-1<=floor(k/2)`, the abstract band `mathcal B` always has a partition
into saturated chains ending at rank `q-1`.

#### Proof

For each consecutive pair of ranks `s,s+1` in the band, normalized matching
in the Boolean lattice supplies a matching from the complete rank-`s` layer
into the complete rank-`s+1` layer, because the layer sizes are
nondecreasing.  Choose these matchings independently at every interface.
Their union has indegree and outdegree at most one, and every vertex below
the top layer has an upward edge.  Its components are therefore saturated
chains ending in the top layer and partitioning the band. `square`

Thus the new content is not ordinary Boolean chainization.  It is support of
one such chainization by the forced flags of the **same** resident factor.

### Proposition 1.2A (linear protected-top reserve)

Let `s<(k-1)/2`, put

\[
 a=k-s,\qquad b=s+1,
 \tag{1.8}
\]

and define

\[
 \eta_s=\left\lfloor
 \min\left\{a-1,
 { (a-b)(a(a-2)+1)\over b}
 \right\}\right\rfloor.
 \tag{1.9}
\]

For every prescribed family

\[
                         Z\subseteq {[k]\choose s+1},
 \qquad |Z|\le\eta_s,
 \tag{1.10}
\]

there is an inclusion matching from the complete rank-`s` layer into
`binom([k],s+1)\setminus Z`.  Consequently, in any lower Boolean band ending
at rank `s+1`, there is a saturated-chain partition in which every member of
`Z` is a singleton top chain.

At the top collar interface in both central parities, `eta_s=m+2`:

\[
 \begin{array}{c|c}
 k=2m+1,\ q=m & s=q-2=m-2,\\
 k=2m,\ q=m-1 & s=q-2=m-3.
 \end{array}
 \tag{1.11}
\]

Thus the **value-side** chain partition can reserve any `O(d)` named top
targets as short chains.  This does not yet exclude prescribed seam *roots*:
their top colours still need alternate compatible occurrences.

#### Proof

Let `G` be the inclusion graph from rank `s` to rank `s+1`, and take
`X` on its lower shore with `x=|X|`.  Every lower vertex has degree `a`, and
two distinct lower vertices have at most one common upper neighbour.  If
`d_Y` counts members of `X` below the upper vertex `Y`, then

\[
 \sum_Yd_Y=ax,
 \qquad
 \sum_Y{d_Y\choose2}\le{x\choose2}.
 \tag{1.12}
\]

Cauchy--Schwarz gives

\[
 |N(X)|\ge {a^2x\over a+x-1}.
 \tag{1.13}
\]

For `1<=x<=a(a-2)+1`, subtracting `x+(a-1)` from the right side of
(1.13), over the positive denominator, leaves

\[
 a^2x-(a+x-1)^2
 =(x-1)(a(a-2)-(x-1))\ge0.
 \tag{1.14}
\]

Hence `|N(X)|-x>=a-1` in this range.  For larger `x`, ordinary edge
counting, using upper degree `b`, gives

\[
 |N(X)|-x\ge {a-b\over b}x
 \ge{(a-b)(a(a-2)+1)\over b}.
 \tag{1.15}
\]

Therefore every lower family has at least `eta_s` surplus neighbours.
Deleting `Z` preserves Hall, proving the matching.  Choose arbitrary
matchings at the lower interfaces as in Corollary 1.2; together with this
top matching they form the claimed chains, while vertices of `Z` receive no
incoming edge and are singleton chains.

For odd central parameters, `(a,b)=(m+3,m-1)`; for even parameters,
`(a,b)=(m+3,m-2)`.  In both cases the second term in (1.9) exceeds `m+2`
and the first equals `m+2`, proving (1.11). `square`

### Corollary 1.3 (a fixed chain partition has only local support tests)

Fix a saturated-chain partition `mathscr C` of `mathcal B` ending in rank
`q-1`.  For the unique chain `C_S in mathscr C` ending at
`S in mathcal X_1`, put

\[
 \mathcal F_Q(C_S)=
 \{i:\ I_{i,1}=S\text{ and }C(i,|C_S|)=C_S\}.
 \tag{1.16}
\]

Then `mathscr C` is supported by nested banks if and only if

\[
                         \mathcal F_Q(C_S)\ne\varnothing
 \qquad(S\in\mathcal X_1).
 \tag{1.17}
\]

No Hall inequalities couple different `S`: the sets in (1.16) lie in the
pairwise disjoint fibres `phi_1^(-1)(S)`.

#### Proof

Necessity follows from Theorem 1.1.  Conversely, choose one root from every
nonempty set in (1.16).  The choices are automatically distinct, and the
chosen flag prefixes are precisely the chains of `mathscr C`; apply Theorem
1.1. `square`

### Corollary 1.3A (exact capacitated/seam-safe support test)

Give every root an allowed height cap

\[
                         c:E\longrightarrow\{0,1,\ldots,d-1\}.
 \tag{1.17A}
\]

There are nested banks with height `h(i)<=c(i)` if and only if the Boolean
band has a saturated-chain partition such that, for every chain `C_S`
ending at `S`,

\[
 \{i:\ I_{i,1}=S,\ C(i,|C_S|)=C_S,\ c(i)\ge|C_S|\}
 \ne\varnothing.
 \tag{1.17B}
\]

In particular, after a factor and a candidate chain partition are fixed,
triangular seam safety creates only these independent top-fibre tests; it
does not create a new cross-top Hall matching.

#### Proof

Restrict the prefix-column hypergraph of Theorem 1.1 to columns `C(i,h)`
with `h<=c(i)`.  The supported-chain proof and the disjointness of distinct
top fibres are unchanged. `square`

There is nevertheless very little local choice at the top of the collar.

### Proposition 1.4 (forced-top-fibre rigidity)

Assume `phi_1` is surjective, put

\[
 N=|E|,\qquad n_j=|\mathcal X_j|,
 \tag{1.18}
\]

and let `U subseteq E` be the roots whose `phi_1` colour has a singleton
fibre.  Then

\[
                         |U|\ge 2n_1-N.
 \tag{1.19}
\]

If nested banks exist, then for every `A subseteq U` and every `j`,

\[
                         |\phi_j(A)|
 \ge |A|-(n_1-n_j).
 \tag{1.20}
\]

In particular,

\[
                         |\phi_j(U)|
 \ge |U|-(n_1-n_j).
 \tag{1.21}
\]

For the central coatom ranks these singleton-root lower bounds are

\[
 \begin{array}{c|c}
 k=2m+1,\ q=m & |U|\ge {m-2\over m+2}N,\\[1mm]
 k=2m,\ q=m-1 & |U|\ge {m-4\over m+2}N.
 \end{array}
 \tag{1.22}
\]

Thus all but `O(N/k)` top colours have a forced root occurrence.  A
successful construction cannot expect to choose a favourable flag from a
large fibre at most tops.

#### Proof

If `u=|U|`, the other `n_1-u` nonempty fibres have size at least two.  Hence

\[
                         N\ge u+2(n_1-u)=2n_1-u,
\]

which is (1.19).

Every root in `U` is forced into `R_1`, because it is the only provider of
its top colour.  The complement `R_1\setminus R_j` has size `n_1-n_j`, so
at least `|A|-(n_1-n_j)` members of `A` lie in `R_j`.  The map `phi_j` is
injective on `R_j`; therefore their images are distinct and all lie in
`phi_j(A)`.  This proves (1.20)--(1.21).

For odd `k`,

\[
 {n_1\over N}={{2m+1\choose m-1}\over{2m+1\choose m}}
 ={m\over m+2};
\]

for even `k`,

\[
 {n_1\over N}={{2m\choose m-2}\over{2m\choose m-1}}
 ={m-1\over m+2}.
\]

Substitution in (1.19) gives (1.22). `square`

## 2. Exact partition-matroid and flag-matroid formulations

For each `j`, let `M_j` be the partition matroid on `E` whose parts are

\[
                     \phi_j^{-1}(S),\qquad S\in\mathcal X_j,
 \tag{2.1}
\]

each with capacity one.  Empty fibres may be deleted; in the intended exact
case every `phi_j` is surjective and

\[
                         r(M_j)=|\mathcal X_j|.
 \tag{2.2}
\]

### Proposition 2.1 (nested-base formulation)

The banks in Theorem 1.1 exist if and only if there are nested sets (1.3)
such that `R_j` is a base of `M_j` for every `j`.

#### Proof

A set is independent in `M_j` exactly when `phi_j` is injective on it.  A
set of size `|mathcal X_j|` is a base exactly when `phi_j` is bijective onto
`mathcal X_j`. `square`

This is the exact flag-transversal formulation.  For unrelated partition
matroids it is not ordinary two-matroid intersection.  There is, however, a
clean genuine flag-matroid face.

### Theorem 2.2 (quotient-chain sufficient condition)

Assume every `phi_j` is surjective and

\[
                         M_{j+1}\text{ is a quotient of }M_j
 \qquad(1\le j<d-1).
 \tag{2.3}
\]

Then the nested banks exist.

For these capacity-one partition matroids, (2.3) is equivalent to the
existence of surjective maps

\[
 p_j:\mathcal X_j\longrightarrow\mathcal X_{j+1}
 \quad\text{such that}\quad
 \phi_{j+1}=p_j\circ\phi_j.
 \tag{2.4}
\]

Because actual intersection flags are nested, every such `p_j` is a Boolean
deletion map:

\[
                         p_j(S)\subset S,qquad |p_j(S)|=|S|-1.
 \tag{2.5}
\]

#### Proof

Choose any base of `M_(d-1)`.  A base of a quotient is independent in the
larger matroid and therefore extends to a base of that larger matroid.
Extend successively through

\[
 M_{d-1},M_{d-2},\ldots,M_1.
 \tag{2.6}
\]

The resulting bases are nested, so Proposition 2.1 applies.

The flats of a capacity-one partition matroid are precisely unions of its
parts.  Thus `M_(j+1)` is a quotient of `M_j` exactly when each
`M_(j+1)`-part is a union of `M_j`-parts.  Equivalently, equality of two
`phi_j` colours forces equality of their `phi_(j+1)` colours, which is
exactly the factorization in (2.4).  Surjectivity of `p_j` follows from
surjectivity of `phi_(j+1)`, and (2.5) follows from
`I_(i,j+1) subset I_(i,j)`. `square`

### Proposition 2.3 (the abstract Boolean quotient scaffold always exists)

For every consecutive pair of Boolean ranks below the middle there is a
surjective deletion map

\[
 p_s:{[k]\choose s}\longrightarrow {[k]\choose s-1},
 \qquad p_s(S)\subset S.
 \tag{2.7}
\]

Hence maps of the abstract form required in Theorem 2.2 exist through the
whole collar band.

#### Proof

Normalized matching supplies an injection

\[
 u_s:{[k]\choose s-1}\hookrightarrow {[k]\choose s},
 \qquad T\subset u_s(T).
 \tag{2.8}
\]

Set `p_s(u_s(T))=T`.  On every upper set outside the image of `u_s`, delete
an arbitrary element.  The resulting map has containment (2.7) and is
surjective because every `T` has its designated preimage `u_s(T)`. `square`

Proposition 2.3 closes the static flag-matroid count.  It does not provide a
factor for which the actual future intersections obey those maps.

## 3. Pull compatibility and a sharp no-go

The missing factor condition has an exact queue identity.

### Lemma 3.1 (forced-flag shift)

For every `1<=j<d-1`,

\[
                         I_{i+1,j}=I_{i,j+1}\cup\{\beta_i\}.
 \tag{3.1}
\]

#### Proof

The entering coordinate `beta_i` is absent from `Q_i`, belongs to
`Q_(i+1)`, and, by residence, survives through `Q_(i+j+1)`.  It therefore
belongs to the right side of (3.1) and to `I_(i+1,j)`.

Any other coordinate in `I_(i+1,j)` already belongs to `Q_i`: the Johnson
step from `Q_i` to `Q_(i+1)` introduces only `beta_i`.  Hence it belongs to
all `Q_i,...,Q_(i+j+1)`, which is `I_(i,j+1)`.  The reverse inclusion is
immediate. `square`

Suppose the quotient identities (2.4) hold.  For `1<=j<d-2`, combining
them with (3.1) forces, on every transition actually used by the factor,

\[
 p_j(T\cup\{\beta_i\})
   =p_{j+1}(T)\cup\{\beta_i\},
 \qquad T=I_{i,j+1}.
 \tag{3.2}
\]

Thus the new point is transported unchanged while the old flag is pulled
one level down.

### Theorem 3.2 (no complete pull-equivariant Boolean quotient atlas)

Let `2<=s<=k-1`.  There do not exist deletion maps

\[
 p_s:{[k]\choose s}\to {[k]\choose s-1},qquad
 p_{s-1}:{[k]\choose s-1}\to {[k]\choose s-2}
 \tag{3.3}
\]

such that

\[
 p_s(T\cup\{\beta\})=p_{s-1}(T)\cup\{\beta\}
 \tag{3.4}
\]

for **every** `T in binom([k],s-1)` and every `beta notin T`.

#### Proof

Choose any `S in binom([k],s)` and let

\[
                         \delta\text{ be the unique element of }
                         S\setminus p_s(S).
 \tag{3.5}
\]

Put `T=p_s(S)=S-{delta}` and `beta=delta`.  Equation (3.4) would give

\[
 p_s(S)=p_{s-1}(p_s(S))\cup\{\delta\}.
 \tag{3.6}
\]

The right side contains `delta`, whereas the left side does not.  This is a
contradiction. `square`

Therefore the quotient-chain face is a **sparse physical** target: the
factor must select only pull-compatible transitions of the chosen deletion
maps.  Abstract parent maps and an arbitrary resident factor cannot be
constructed independently.

The most obvious sparse choice is also impossible cyclically.

### Proposition 3.3 (extreme-deletion quotient maps are gradient no-gos)

Linearly order the ground set and define

\[
 p_s^{\min}(S)=S-\{\min S\}
 \tag{3.7}
\]

at every rank.  Every pull-compatible transition between coherent flags
strictly increases the sum of the elements in its rank-`s` member.  Hence
these maps support no cyclic coherent factor.  With `min` replaced by `max`,
the sum strictly decreases and the same conclusion holds.

#### Proof

Write the old rank-`s` member as

\[
 S=T\cup\{\delta\},\qquad \delta=\min S,qquad
 T=p_s^{\min}(S).
 \tag{3.8}
\]

A pull introduces some `beta notin S` and makes the new rank-`s` member
`T+beta`.  Coherence one level lower requires

\[
 p_s^{\min}(T+\beta)=p_{s-1}^{\min}(T)+\beta.
 \tag{3.9}
\]

The right side retains `beta`; therefore `beta` is not the minimum of
`T+beta`, so

\[
                         \beta>\min T>\delta.
 \tag{3.10}
\]

Consequently

\[
                         \sum(T+\beta)-\sum S=\beta-\delta>0.
 \tag{3.11}
\]

A strict potential forbids a directed cycle.  The maximum-deletion case is
the order-dual argument. `square`

Thus a viable quotient scaffold must be non-gradient and co-designed with
its cyclic transition support; the canonical minimum/maximum parent rules
cannot be repaired merely by discarding their incompatible pulls.

## 4. Exact Pascal sector recursion

Let `[k]=K dotcup {z}`.  Consider two linear oriented resident factors:

* `A` lists every member of `binom(K,q)` once;
* `B` lists every member of `binom(K,q-1)` once, and is lifted to the
  rank-`q` path `z+B`.

Suppose their two end pairs are joined by legal Johnson seams so that

\[
                         Q=A\,\cdot\,(z+B)
 \tag{4.1}
\]

is a cyclic resident factor on `binom([k],q)`.

Give every child root a supported height as in Theorem 1.1.  For a root in
a linear sector, let `dist(i)` be the number of transitions remaining before
the next seam.

### Theorem 4.1 (triangularly safe Pascal splice)

If

\[
                         h(i)\le \operatorname{dist}(i)
 \tag{4.2}
\]

for every positive-height root in both sectors, then the union of the two
child prefix covers is a nested-intersection bank for `Q`.

#### Proof

Condition (4.2) says that every selected future intersection stays wholly
inside its child sector.  In the first sector its values therefore form the
child layers

\[
                         {[k-1]\choose q-j}.
 \tag{4.3}
\]

In the second sector, `z` is present throughout every selected window, so
stripping it leaves the child intersections and its values form

\[
                         \{z\}\star {[k-1]\choose q-j-1}.
 \tag{4.4}
\]

The two families are disjoint and Pascal's identity gives

\[
 {[k]\choose q-j}
 = {[k-1]\choose q-j}
   \mathbin{\dot\cup}
   \bigl(\{z\}\star {[k-1]\choose q-j-1}\bigr)
 \tag{4.5}
\]

at every `j`.  The union of the child banks is nested because the child
banks are nested, and (4.5) proves bijectivity at every depth. `square`

The condition is triangular: the root immediately before a seam must have
height zero, the preceding root may have height at most one, and so on.
This is the exact seam state a Pascal induction must regenerate.  The scalar
height inventory has ample zero/short rows near the central layer; what is
not automatic is placing them consecutively at two legal factor openings
without losing one of the forced named top colours.

## 5. Natural singleton-window Ucycles

Let `w=(w_i)_(i in Z_L)` be a cyclic word on `[k]` such that every length-`q`
window has `q` distinct symbols and the resulting `q`-sets are pairwise
distinct.  Put

\[
                         Q_i=\{w_i,w_{i+1},\ldots,w_{i+q-1}\}.
 \tag{5.1}
\]

### Proposition 5.1 (the exact help supplied by a natural Ucycle)

The sets `Q_i` form a resident oriented Johnson cycle, every positive
coordinate run has length exactly `q`, and for `0<=j<q`,

\[
                         I_{i,j}
 =\{w_{i+j},w_{i+j+1},\ldots,w_{i+q-1}\}.
 \tag{5.2}

Consequently the nested-bank condition is exactly a choice of suffix-window
chains from `w` which partitions the Boolean band in Theorem 1.1.

#### Proof

Consecutive windows drop `w_i` and add `w_(i+q)`.  These symbols cannot be
equal, for then consecutive `q`-sets would coincide.  The new symbol is
different from the other `q-1` symbols because the new window is a set.
Thus every step is Johnson.

An occurrence of a symbol belongs to exactly the `q` consecutive windows
whose position interval contains it.  Two occurrences cannot be at distance
less than `q`, and distance exactly `q` would make one Johnson step drop and
add the same symbol.  Hence the positive incidence runs have length exactly
`q`.

The positional overlap of `Q_i,...,Q_(i+j)` is the window on the right side
of (5.2).  A symbol outside that positional overlap cannot remain in every
set: to replace its exiting occurrence without an absent step would require
a repeat at distance exactly `q`, which was just excluded.  This proves
(5.2), and Theorem 1.1 gives the final statement. `square`

Thus a natural Ucycle solves owner chronology and residence and turns the
collar into a transparent shorter-window problem.  It does **not** solve that
problem: ordinary Ucycle existence controls only the length-`q` windows,
whereas (5.2) asks for one jointly nested exact cover at every length
`q-1,...,q-d+1`.

There is also an unavoidable arithmetic boundary.

### Theorem 5.2 (infinite even-central omission lower bound)

Let

\[
 k=2m,qquad q=m-1,qquad m=2^a-1\ge3.
 \tag{5.3}
\]

If a cyclic word has a family `mathcal F` of pairwise distinct rank-`q`
sets as all of its length-`q` windows, then

\[
 \left|{[k]\choose q}\setminus\mathcal F\right|\ge m.
 \tag{5.4}
\]

In particular a natural Ucycle of the complete rank-`q` layer does not
exist in these infinitely many dimensions.

#### Proof

Let

\[
                         C_m={1\over m+1}{2m\choose m}
 \tag{5.5}
\]

be the Catalan number.  Kummer's carry theorem gives

\[
 v_2\binom{2m}{m}=a=v_2(m+1)
 \tag{5.6}
\]

when `m=2^a-1`; hence `C_m` is odd.

The complete rank-`q` layer has

\[
 N={2m\choose m-1}=mC_m
 \tag{5.7}
\]

members.  The number containing one fixed coordinate is, by incidence
counting,

\[
 D={qN\over k}={qC_m\over2}
   \equiv {q\over2}\pmod q,
 \tag{5.8}
\]

where `q=m-1` is even.

For a coordinate `x`, let `t_x` be its number of occurrences in the cyclic
word.  Each occurrence lies in exactly `q` length-`q` windows, and no such
window contains two occurrences of `x`.  Therefore

\[
                         \deg_{\mathcal F}(x)=qt_x.
 \tag{5.9}
\]

If `h_x` is the number of omitted complete-layer sets containing `x`, then

\[
                         h_x=D-qt_x\equiv q/2\pmod q,
 \tag{5.10}
\]

so `h_x>=q/2`.  Summing over all `k=2m` coordinates and writing `H` for the
number of omitted sets gives

\[
                         qH=\sum_x h_x
                         \ge 2m\,{q\over2}=mq.
 \tag{5.11}
\]

Hence `H>=m`. `square`

For odd central parameters `k=2m+1,q=m`, the divisibility obstruction does
vanish:

\[
                         {2m+1\choose m}=(2m+1)C_m.
 \tag{5.12}
\]

This still does not invoke a known all-central Ucycle theorem.  The
Glock--Joos--Kuehn--Osthus tight-Euler theorem states that for each **fixed**
uniformity `q` there is a threshold `n_0(q)`; it does not imply its hypothesis
at `n=2q+1`.  More importantly, even a natural Ucycle would still need the
multi-radius suffix-chain exact cover from Proposition 5.1.

Universal cycles obtained from shorthand binary strings, difference words,
or labelled-graph representations use different substrings; they do not make
the ground-set elements themselves the singleton symbols in (5.1), and hence
do not yield the Johnson/intersection identities (5.1)--(5.2).

## 6. Revised frontier

The forced collar gate now has three exact levels.

\[
 \begin{array}{c}
 \text{Boolean band chain partition}\quad\text{(always exists)}\\
 \Downarrow\\
 \text{support every chain by one forced factor flag}
 \quad\text{(open exact-cover row)}\\
 \Downarrow\\
 \text{co-select legal pulls, resident factor seams, and upper/owner gates}
 \quad\text{(open physical row).}
 \end{array}
 \tag{6.1}
\]

The quotient-chain condition gives one recognizable sufficient
flag-matroid face, but Theorem 3.2 proves that this face cannot be made
transition-independent.  The Pascal splice gives an exact recursive route,
but it requires triangularly safe openings.  Natural Ucycles give the
cleanest possible flags when they exist, but ordinary Ucycle theorems neither
produce the multi-radius exact cover nor cover all central parameters.

The next positive lemma should therefore be one of the following.

1. **Supported-chain factor lemma.**  Construct a resident oriented factor
   whose flag-prefix hypergraph `H_Q` has the exact cover (1.6).
2. **Sparse quotient pull lemma.**  Choose Boolean deletion maps and a
   connected balanced set of only their pull-compatible Johnson transitions
   which uses every rank-`q` root once.
3. **Pascal safe-opening lemma.**  Regenerate two triangularly safe child
   cuts while preserving the supported chain covers and the protected
   upper/owner interface.

Any of these closes the named consecutive-collar row.  Residual ranks below
`r-d`, safe opening of the final word, and the upper-complete connected host
remain separate requirements.

## 7. Primary literature boundary

* S. Glock, F. Joos, D. Kuehn, and D. Osthus,
  *Euler tours in hypergraphs*, arXiv:1808.07720.  Theorem 2 has the
  quantifier `for every fixed uniformity k` and proves natural subset
  Ucycles under the divisibility condition only beyond a threshold depending
  on that uniformity.
* C. Campbell, L. Janik-Jones, and J. Sawada,
  *Universal cycle constructions for k-subsets and k-multisets*,
  arXiv:2603.11954.  Its all-parameter constructions use shorthand or
  difference representations, not the natural singleton-window
  representation (5.1).

## 8. Dependencies

* `MATH_THEOREM_RENEWAL_BLOCKS_FORCED_DEPARTURE_COLLARS_AND_ATOMIC_SEPARATION_20260804.md`;
* `MATH_THEOREM_K_MOVING_CORE_PULL_CLOCK_DEPTH_ONE_HAMILTON_RAIL_AND_DEPTH_TWO_BOUNDARY_20260802.md`;
* Boolean normalized matching / Hall's theorem;
* the elementary partition-matroid quotient criterion;
* Kummer's theorem for the Catalan parity calculation.
