# Tight odd-diamond augmenters compose as alternating forests

Date: 2026-08-01  
Lane: protected odd owner-slot synchronization / exact cover-down  
Status: unconditional protected `U-o(W)` physical-forest start, independent
audit of the tight `1 -> 2` primitive, exact alternating-forest composition,
and exact packet-packing and boundary-cut criteria. Expansion of the actual
`o(W)` leave is not proved.

## 0. Outcome

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal M={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal M|,\qquad
 U=|\mathcal U|=W-\operatorname {Cat}_m.
\]

Clone every owner `T in M` into two literal slots `T^0,T^1`. An atom is

\[
       (R,L;T^i,H^j),\qquad L\subset T,H\subset R,              \tag{0.1}
\]

and uses one upper, one lower and two owner-slot resources.

This note closes three rows around the tight one-to-two augmenter.

1. The local primitive in
   `MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`
   is correct. Its exact target menu has order

   \[
      16(m+1)m(m-2)(m-1),                                      \tag{0.2}
   \]

   and its maximum non-target resource load is exactly

   \[
                         8m(m-1)(m-2).                          \tag{0.3}
   \]

2. The valid Delcourt--Postle short-cycle-conflict argument applies
   directly to the protected odd owner-slot host. After deleting one edge
   from every remaining long physical cycle, it gives a literal physical
   linear forest of size

   \[
                              U-o(W)                             \tag{0.4}
   \]

   containing any prescribed tight-pivot forest of order `O(sqrt(m))`.

3. Tight augmenters compose exactly as rooted alternating forests. If
   there are `t` augmenter nodes and `r` roots, their blocker ledger has
   exactly `t-r` old edges. Removing the `t` auxiliary edges and those
   `t-r` blockers, then installing the `2t` on-edges, increases the
   matching order by exactly `r` and covers exactly the `r` root upper
   colours.

Thus exact odd synchronization is reduced to one guarded expansion
statement on the genuine `o(W)` upper leave. The reduction is literal;
there is no remaining scalar or local-gadget ambiguity.

There is also a sharp obstruction. For a missing upper `R`, every atom
covering `R` uses two slots from its `2(m+1)`-slot facet boundary. A
protected matching omitting `R` can saturate that boundary only with at
least `2(m+1)` atoms, and an explicit matching of exactly that order does
so. Once frozen, it forbids **every** absorber for `R`, of arbitrary
support. Hence some boundary expansion hypothesis is logically necessary;
raw menu cardinality cannot replace it.

## 1. The odd owner-slot host and the protected forest start

Let `H_m` be the four-uniform hypergraph with vertex set

\[
 \mathcal U\mathbin{\dot\cup}\mathcal L
 \mathbin{\dot\cup}(\mathcal M\times\{0,1\}),                  \tag{1.1}
\]

and all atoms (0.1). The exact degree ledger is

\[
\begin{aligned}
 d(R)&=2m(m+1),&&R\in\mathcal U,\\
 d(L)&=2m(m-1),&&L\in\mathcal L,\\
 d(T^i)&=2m(m-1),&&T\in\mathcal M,
\end{aligned}                                                   \tag{1.2}
\]

and

\[
                         \Delta_2(\mathcal H_m)\le2m.           \tag{1.3}
\]

Put `D=2m(m+1)`. The physical projection of a host matching is a
simple graph of maximum degree two on `M`: two atoms with the same physical
owner pair have the same lower and upper resources and cannot coexist.

### Theorem 1.1 (protected `U-o(W)` odd physical forest)

Let `P_m` be a prescribed owner-slot matching whose physical projection is
a forest and whose order is `p_m=O(sqrt(m))`. Then, for all sufficiently
large `m`, there is an owner-slot matching `F_m` such that

1. `P_m subseteq F_m`;
2. the physical projection of `F_m` is a linear forest; and
3.

   \[
                              |F_m|=U-o(W).                      \tag{1.4}
   \]

#### Proof

Delete the four typed resources of every atom of `P_m` and all incident
host edges. At most `4p_mD=o(UD)` edges are removed, so the residual host
has

\[
                         |E|=UD-o(UD),\qquad \Delta\le D,        \tag{1.5}
\]

while (1.3) is unchanged.

Fix a cycle cutoff `g`. In the configuration hypergraph declare every
host matching whose physical projection is a simple cycle of length
`3,...,g` forbidden. If `ell` atoms of an `i`-cycle are fixed, their
projected edges form path segments. Completing them to one cycle has one
closing constraint, and therefore

\[
 \Delta_i=O_g(D^{i-2}),\qquad
 \Delta_{i,\ell}=O_g(D^{i-\ell-1}).                             \tag{1.6}
\]

With, for example, `beta=1/3`, equations (1.3) and (1.6) satisfy
Delcourt--Postle Corollary 1.17 for every fixed `g`. Hence the residual
host has a conflict-free proper edge-colouring with at most

\[
                         D(1+D^{-\alpha_g})                     \tag{1.7}
\]

colours. Its largest colour class `M_g` is a matching of order

\[
                         |M_g|=U-o_g(W),                         \tag{1.8}
\]

and has no physical cycle of length at most `g`.

The union `P_m union M_g` is still an owner-slot matching and has physical
maximum degree two. A cycle disjoint from `P_m` lies in `M_g` and has
length at least `g+1`. The cycles meeting `P_m` are edge-disjoint and
number at most `p_m`, because `P_m` itself is a forest. Delete one
`M_g`-edge from every cycle. This loses at most

\[
                         {|M_g|\over g+1}+p_m.                   \tag{1.9}
\]

Every cycle meeting `P_m` contains an `M_g`-edge, so no protected edge is
deleted. Take the standard slow diagonal `g=g(m) -> infinity`, only after
the fixed-`g` theorem thresholds have been passed. Equations (1.8)--(1.9)
give (1.4). The surviving projection is a linear forest. `square`

The external theorem and the fixed-cutoff/slow-diagonal quantifiers are
audited in

`MATH_AUDIT_CATALAN_FIXED_Q_DELCOURT_POSTLE_COROLLARY_117_20260731.md`.

The proof above is its direct specialization to the unpunctured odd host:
the host uniformity remains four, its codegree is (1.3), and the same
one-closing-constraint estimate gives (1.6). No approximate minimum-degree
hypothesis is being imported from Pippenger--Spencer.

This theorem is an unconditional starting object. It does not prescribe
the leave or supply its alternating expansion.

It is also important that Theorem 1.1 is an **anonymous two-slot physical
support** theorem. The labels `0,1` enforce capacity two, but they are not a
preassigned tail/head split and do not encode a fixed first incidence
matching `M_0`. Every resulting physical forest can be oriented
componentwise, but a lift respecting one already frozen `M_0`, rooted
endpoint tickets, or occurrence labels is an additional correlation row.
Corollary 3.3 gives one local rooted lift when those data are planted; it
does not promote the whole anonymous forest automatically.

## 2. Independent audit of the tight one-to-two primitive

Fix `R in U`. Choose ordered distinct `a,b in R`, put

\[
                         L=R-\{a,b\},                            \tag{2.1}
\]

choose `c notin R` and `x in L`, and define

\[
\begin{array}{lll}
 A=L+a,&B=L+b,&C=L+c,\\
 L'=(L-x)+c,&&D=(L-x)+a+c,\\
 S=L+a+c.&&
\end{array}                                                     \tag{2.2}
\]

For slots `i,j,p,q in {0,1}`, put

\[
\begin{aligned}
 f&=(S,L;A^i,C^j),\\
 e&=(R,L;A^i,B^p),\\
 g&=(S,L';C^j,D^q).                                             \tag{2.3}
\end{aligned}
\]

The containments are literal. In particular

\[
                         S-L'=\{a,x\},                           \tag{2.4}
\]

so the middle owners of `g` are `C=S-a` and `D=S-x`.
The four owners `A,B,C,D` are distinct: `A,B,C` add three different
external labels to `L`, while `D` omits `x` and contains both `a,c`.
Consequently `{e,g}` is a matching and

\[
 \operatorname {res}\{e,g\}
   =\operatorname {res}\{f\}\mathbin{\dot\cup}
     \{R,L',B^p,D^q\}.                                          \tag{2.5}
\]

This independently verifies the local theorem.

### Proposition 2.1 (exact count and exact maximum menu load)

For fixed `R`, the labelled menu has exactly

\[
                         N_R=16(m+1)m(m-2)(m-1)                 \tag{2.6}
\]

members. Among non-target typed resources its maximum load is

\[
                         \Lambda_R=8m(m-1)(m-2),                \tag{2.7}
\]

attained by fixing either an `A`-slot or a `B`-slot.

More precisely, the following are upper bounds, and the first four are
exact whenever the named resource has the displayed relative position:

\[
\begin{array}{c|c}
 \text{fixed object}&\text{number of menu members}\\ \hline
 A^i\text{ or }B^p&8m(m-1)(m-2)\\
 f&4(m-1)\\
 L'&96\\
 D^q&16(m-1)\\
 S&16m(m-1)\\
 L&32(m-1)(m-2)\\
 C^j&16(m-1).
\end{array}                                                     \tag{2.8}
\]

#### Proof

There are `(m+1)m` ordered choices of `(a,b)`, `m-2` choices of `c`,
`m-1` choices of `x`, and sixteen slot choices. The tuple is recovered
from the labelled configuration: `A=R-b` gives `b`, `B=R-a` gives
`a`, then `C-L` gives `c`, and `L-L'` gives `x`. This proves
(2.6).

For fixed `A^i`, `b` and `i` are fixed; the free data are

\[
 a:m,\quad c:m-2,\quad x:m-1,\quad (j,p,q):8,
\]

giving (2.7). The same calculation applies to `B^p`.

For fixed `f`, the sets `L,A,C` recover `a,b,c` and the slots `i,j`;
only `x,p,q` remain, giving `4(m-1)`. For fixed `L'`, its unique outside
coordinate is `c` and the triple `R-L'` is `{a,b,x}`; choosing which
member is `x` and ordering the other two gives `6*16=96`. For fixed
`D^q`, the outside coordinate is `c`, the pair `R-D` is `{b,x}`,
and `a` is any of the other `m-1` elements of `R`, giving
`2(m-1)*8=16(m-1)`. The remaining rows are obtained in the same way. All
are below (2.7). `square`

### Corollary 2.2 (protected local survival)

If `z` non-target typed resources are forbidden, at least

\[
                         N_R-z\Lambda_R                         \tag{2.9}
\]

menu members survive. In particular `z=o(m)` deletes only an `o(1)`
fraction of the menu, and every fixed tight-pivot bank of order
`O(sqrt(m))` is locally harmless.

The statement is local: current matching occupancy may still destroy every
**direct** augmenter by occupying all three increment resources.

## 3. Clean alternating augmenter forests

Let `M` be an owner-slot matching and `P subseteq M` a protected bank.
For a tight configuration `gamma=(f;e,g)` define its increment triple

\[
                         Q(\gamma)=\{L',B^p,D^q\}.               \tag{3.1}
\]

For a typed-resource set `Q`, let

\[
 N_M(Q)=\{h\in M:h\text{ uses a resource of }Q\}.                \tag{3.2}
\]

Let `Z` be a set of `r` upper colours omitted by `M`.

### Definition 3.1 (clean rooted expansion forest)

A clean expansion forest for `Z` consists of a finite rooted forest on a
node set `V`, with `|V|=t`, and the following data.

1. Its roots are labelled bijectively by `Z`. Every node `v` has a
   distinct target upper colour `R_v` and a tight configuration
   `gamma_v=(f_v;e_v,g_v)` with target `R_v` and

   \[
                              f_v\in M-P.                        \tag{3.3}
   \]

2. The auxiliary edges `f_v` are distinct. Every nonroot node `v` has a
   distinct blocker edge

   \[
                  h_v\in M-(P\cup\{f_w:w\in V\}),\qquad
                  \operatorname {upper}(h_v)=R_v.               \tag{3.4}
   \]

3. The triples `Q(gamma_v)` are pairwise resource-disjoint, and

   \[
       N_M\!\left(\bigcup_{v\in V}Q(\gamma_v)\right)
                    =\{h_v:v\text{ nonroot}\}.                  \tag{3.5}
   \]

   The blocker `h_v` belongs to the increment neighbourhood of its unique
   parent and to no other node's increment triple. It may occupy one or
   more of the three resources of that parent.

Condition (3.5) says exactly that every occupied increment resource is
released by one child blocker; all leaf increments are already free. It
also excludes hidden conflicts with the protected bank or an auxiliary
edge.

### Theorem 3.2 (exact alternating-forest augmentation)

Let a clean expansion forest for `Z` be given. Put

\[
 F=\{f_v:v\in V\},\qquad
 H=\{h_v:v\text{ nonroot}\},\qquad
 N=\{e_v,g_v:v\in V\}.                                         \tag{3.6}
\]

Then

\[
                         M^+=(M-(F\cup H))\cup N                 \tag{3.7}
\]

is an owner-slot matching, contains `P`, and

\[
                         |M^+|=|M|+r.                            \tag{3.8}
\]

Its upper palette is the old upper palette together with exactly `Z`.

If the physical projection of `M` is a forest, put

\[
                         G_0=\pi(M-(F\cup H)).                   \tag{3.9}
\]

Then `pi(M^+)` is a forest if and only if the `2t` projected on-edges are
loopless and graphic-independent after the components of `G_0` are
contracted. In that case the number of physical components falls by exactly
`r`.

#### Proof

For every node, (2.5) says that its two on-edges use the four resources of
`f_v`, the target upper `R_v`, and the increment triple `Q(gamma_v)`.
The `f_v` resources are pairwise disjoint because `F subseteq M` is a
matching. Equation (3.5) removes every old edge meeting an increment
resource, and the triples are mutually disjoint. The root upper colours
were unused; every nonroot target upper is the upper resource of its
deleted blocker. All target uppers are distinct. Hence no new edge meets
`M-(F union H)` or another new edge. This proves that (3.7) is a matching
and retains `P`.

There are `t` auxiliary edges and exactly `t-r` nonroot blockers, whereas
there are `2t` on-edges. Therefore

\[
             |M^+|-|M|=2t-t-(t-r)=r,                            \tag{3.10}
\]

proving (3.8). Each `g_v` retains the upper colour of `f_v`; each
nonroot `e_v` replaces the upper colour of `h_v`; and each root `e_v`
adds its missing upper. This proves the palette assertion.

Every edge of the physical forest `pi(M)` is a bridge. Deleting the
`2t-r` old edges raises its component count by that amount. Adding the
`2t` on-edges preserves acyclicity exactly when their quotient images are
graphic-independent, in which case they lower the component count by
`2t`. The net change is `-r`. `square`

The theorem permits genuine branching: one parent increment triple can be
blocked by up to three old edges. It also permits one blocker to occupy two
resources of its parent. What it forbids is a blocker shared by two parents,
because that destroys the rooted-tree accounting and can create a
cross-packet collision.

### Corollary 3.3 (rooted isolated tight augmenter)

Orient the off edge as `A -> C`. Suppose it is an isolated component of an
oriented physical path forest. Suppose further that `B` and `D` are the
initial endpoints of two other, distinct path components

\[
                 P_B:B\leadsto b_*,\qquad P_D:D\leadsto d_* .  \tag{3.11}
\]

Assume the endpoint convention assigns one unused lower ticket to every
terminal endpoint, that the isolated component's terminal ticket is
`L' subset C`, and that the other two components have terminal tickets
`Q_B subset b_*` and `Q_D subset d_*`.

Then the tight replacement, oriented as

\[
                         A\longrightarrow B,qquad
                         C\longrightarrow D,                    \tag{3.12}
\]

replaces the three old components by the two paths

\[
                 A\longrightarrow B\leadsto b_*,\qquad
                 C\longrightarrow D\leadsto d_* .              \tag{3.13}
\]

It preserves the two exterior terminal tickets `Q_B,Q_D`. The ticket `L'`
is consumed exactly as the lower colour of the new edge `C -> D`, and `C`
changes from a terminal to an initial endpoint. Thus the number of rooted
components and the number of unused terminal tickets both fall by one.

#### Proof

The three old components are disjoint by hypothesis. Each edge in (3.12)
joins the isolated component to a different one of the other two
components, so (3.13) is a pair of paths and no cycle is created. Their
terminal endpoints are still `b_*` and `d_*`, proving preservation of the
two exterior tickets. Finally

\[
                         C\cap D=(L-x)+c=L',                     \tag{3.14}
\]

so the new edge `C -> D` uses precisely the old free terminal ticket at
`C`. `square`

This corollary is stronger than the bare union--find test for a prepared
rooted host. It does not assert that every Delcourt--Postle component has
the required orientation or endpoint ticket; those are planting
hypotheses.

## 4. Packing bounded expansion witnesses

For one root `R`, let `mathscr T_R(T)` be a family of already certified
clean rooted expansion trees with at most `T` nodes. The witnesses are all
relative to the same starting matching `M` and protected bank `P`.

Give a witness with `t` nodes the compressed footprint

\[
 \Xi(\mathcal T)=
   \{\text{tokens of its }2t-1\text{ removed old edges}\}
       \mathbin{\dot\cup}
   \bigcup_{v\in V}Q(\gamma_v).                                 \tag{4.1}
\]

Thus

\[
                              |\Xi(\mathcal T)|\le5t-1\le b,
 \qquad b:=5T-1.                                                 \tag{4.2}
\]

The old-edge tokens are a new resource type. Formula (3.5) makes this
compression exact: if an increment resource of one witness lies on an old
edge of another, that old edge is a blocker token in the first witness as
well.

### Theorem 4.1 (alternating-expansion packet Hall)

Let `Z` be a set of missing uppers. If, for every nonempty `I subseteq Z`,

\[
 \boxed{
   \nu\!\left(\bigcup_{R\in I}
       \{\Xi(\mathcal T):\mathcal T\in\mathscr T_R(T)\}\right)
                    >(2b-3)(|I|-1),}                            \tag{4.3}
\]

then there is one clean expansion witness for every `R in Z` with all
compressed footprints disjoint. Their union is a clean expansion forest
with `|Z|` components, and Theorem 3.2 gives a matching of order

\[
                              |M|+|Z|.                           \tag{4.4}
\]

If the union of all selected on-edges satisfies the contracted graphic
test in Theorem 3.2, the resulting support is a physical forest.

#### Proof

Equation (4.3) is the Aharoni--Haxell rainbow-matching condition for
hypergraphs of rank at most `b`. It selects disjoint footprints, one from
each root family. Old-edge-token disjointness makes all auxiliary and
blocker edges distinct. Increment-resource disjointness and (3.5) exclude
every cross-witness resource conflict. The disjoint union is therefore a
clean expansion forest. Theorem 3.2 proves (4.4), and its last assertion is
exactly the graphic add-on. `square`

For direct one-node augmenters, the compressed footprint is simply

\[
                         \{f,L',B^p,D^q\},                       \tag{4.5}
\]

of rank four, so the coefficient in (4.3) is five.

### Corollary 4.2 (elementary deletion-resilient form)

Suppose that, for every `R in Z` and every set of at most `b(|Z|-1)`
compressed footprint resources, `mathscr T_R(T)` contains a witness avoiding
that set. Then the witnesses can be selected greedily and Theorem 4.1
applies.

This is the clean minimum-availability condition needed after the
Delcourt--Postle forest is fixed. The polynomial raw menu (2.6) does not
imply it, because membership of `f` in `M` and the blocker closure (3.5)
are matching-dependent.

## 5. The exact facet-slot cut

For `R in U`, define its literal facet-slot boundary

\[
 \Sigma(R)=\{(R-x)^i:x\in R,\ i\in\{0,1\}\},\qquad
                         |\Sigma(R)|=2(m+1).                     \tag{5.1}
\]

Every atom covering `R` uses two slots in `Sigma(R)`, at two distinct
physical facets.

### Theorem 5.1 (absolute protected-boundary obstruction)

Let `P` be a protected matching which omits the upper colour `R`.

1. Every atom of `P` uses at most one slot of `Sigma(R)`.
2. If `P` occupies all of `Sigma(R)`, no matching containing `P` can
   cover `R`; consequently no alternating absorber of any support can
   repair `R` while preserving `P`.
3. For every `m>=4`, there is such a blocking matching of the sharp order

   \[
                              2(m+1).                            \tag{5.2}
   \]

#### Proof

If one atom used two distinct facet owners of `R`, their union would be
`R`; that atom's upper colour would therefore be `R`, contrary to the
hypothesis that `P` omits `R`. This proves item 1. Item 2 follows because
every possible atom of upper colour `R` needs two occupied protected slots.
Item 1 also proves the lower bound (5.2).

For equality, write `n=m+1` and label the elements of `R` cyclically by
`Z_n`. Choose two different exterior coordinates `c_0,c_1`, possible
because `|Omega-R|=m-2>=2`. For every `x in Z_n` and `i in {0,1}`, put

\[
 y_{x,0}=x+1,\qquad y_{x,1}=x+2,                                \tag{5.3}
\]

and define

\[
\begin{aligned}
 T_x&=R-x,\\
 H_{x,i}&=R-\{x,y_{x,i}\}+c_i,\\
 L_{x,i}&=R-\{x,y_{x,i}\},\\
 S_{x,i}&=R-x+c_i.                                               \tag{5.4}
\end{aligned}
\]

Use the atom

\[
                     (S_{x,i},L_{x,i};T_x^i,H_{x,i}^0).          \tag{5.5}
\]

The directed pairs `(x,x+1)` and `(x,x+2)` are all different as unordered
pairs for `n>=5`; hence all lower colours in (5.5) are distinct. The upper
colours are determined by `(x,c_i)` and are distinct. Every auxiliary
owner contains an exterior `c_i`, and equality of two such owners would
force equality of the corresponding unordered pair and of `i`; hence the
auxiliary owner slots are distinct and are not facet slots of `R`.
Therefore (5.5) is a matching of order `2n`, it omits `R`, and it occupies
exactly `T_x^0,T_x^1` for every `x`. This proves item 3. `square`

The construction at `n=5` uses the cyclic tournament edges of steps one
and two; for larger `n`, no reverse of a step-one or step-two arc is again
a step-one or step-two arc except at `n=4`, which is outside the stated
range.

### Corollary 5.2 (the direct-augmenter Hall cut)

Let `M` be fixed and let `Z` be its missing upper shore. Let `S_free` be
the free owner-slot vertices. Form the bipartite graph

\[
 G_{\rm facet}\subseteq Z\times S_{\rm free},\qquad
 R\sim T^i\Longleftrightarrow T\subset R.                       \tag{5.6}
\]

A simultaneous family of direct tight one-to-two augmenters for every
`R in Z` requires

\[
                         |N_{G_{\rm facet}}(X)|\ge|X|
                         \qquad(X\subseteq Z),                   \tag{5.7}
\]

because every direct augmenter consumes its free `B^p` facet slot.

There are two further necessary marginal Hall cuts. Its free lower
increment satisfies

\[
             |R-L'|=3,\qquad |L'-R|=1,                          \tag{5.8}
\]

and its free `D`-slot satisfies

\[
             |R-D|=2,\qquad |D-R|=1.                            \tag{5.9}
\]

Thus the analogous graphs from `Z` to the free lower bank and to the free
`D`-slot bank must also satisfy Hall. These three marginal systems are not
sufficient: one tuple `(a,b,c,x)` and one selected auxiliary edge `f`
must realize them simultaneously. The exact joint sufficient condition is
Theorem 4.1.

## 6. Revised exact frontier

The unconditional chain now reads

\[
 \boxed{
 \begin{array}{c}
 \text{protected tight pivot}\\
 \Downarrow\\
 \text{odd owner-slot physical forest of size }U-o(W)\\
 \Downarrow\\
 \text{guarded clean alternating expansion of its missing uppers}\\
 \Downarrow\\
 \text{exact upper/lower/slot synchronization and physical forest.}
 \end{array}}                                                    \tag{6.1}
\]

The first arrow is Theorem 1.1. The local algebra and exact composition in
the second arrow are Theorem 2.1 of the tight-augmenter note and Theorem 3.2
here. What remains open is precisely the expansion/packing inequality (4.3),
or a stronger Boolean theorem implying it, for the actual Delcourt--Postle
leave.

The facet cut proves that some expansion premise is unavoidable. For the
actual protected pivot bank, whose order is `O(sqrt(m))`, the absolute
`2(m+1)` blocker cannot occur from the pivot alone. It can nevertheless
occur in the unprotected incumbent and must then be released by child nodes
of the alternating forest. This is exactly the role of branching in
Definition 3.1.

No statement here supplies residence, arbitrary-width upper witnesses, or
the terminal OR-word compiler. It solves the owner-slot absorption algebra
and identifies its exact remaining global Hall/graphic gate.
