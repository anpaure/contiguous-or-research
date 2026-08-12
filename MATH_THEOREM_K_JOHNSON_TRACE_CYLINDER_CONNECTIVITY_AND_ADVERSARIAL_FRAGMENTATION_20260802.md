# Johnson trace cylinders: local resilience and the adversarial fragmentation barrier

Date: 2026-08-02  
Status: exact deterministic quotient and obstruction theorem.  The
multi-support random giant remains open.

## 0. Scope and conclusion

Let

\[
        \mathcal J=J(n,a),\qquad
        \varepsilon n\le a\le (1-\varepsilon)n,
\]

and let `E subseteq [n]`, `|E|=b`, with every trace size `0,...,b`
feasible.  An **exact trace cylinder** is

\[
        \mathcal C(E,T)=\{X\in\tbinom{[n]}a:X\cap E=T\},
        \qquad T\subseteq E.                              \tag{0.1}
\]

This note proves four facts relevant to the clustered-pruning reservoir.

1. The exact trace quotient is an augmented Boolean graph.  Deleting only
   `s=O(q^2)` traces on one `b=Theta(q)` support leaves a component containing
   a `1-O(bs/2^b)` fraction of the reservoir.
2. No theorem based only on the **total number** or **total density** of
   deleted cylinders can give a giant, or even an `O(1)`-component linear
   remainder.  With `O(2^b/b^(1/4))` cylinders and deleted density
   `O(b^(-1/4))`, an adversary fragments the reservoir into cardinality bands,
   each of mass `O(b^(-1/4))`.
3. Independently sampled frame supports avoid this particular obstruction:
   with high probability their outside supports are distinct and have pairwise
   intersection `O(q/log q)`.  This is not a proof of a random-support giant.
   The missing statement is a transverse-cylinder switching theorem.
4. Common-base conditioning does not repair connectivity by itself.  There is
   an actual facet-frame family, with one common base point and a complete
   support-intersection graph, which deletes only `o(1)` of one reservoir but
   leaves `2^{Theta(q)}` components.  These extra components may have tiny
   total mass, so this is a connectivity/component-count obstruction rather
   than a no-giant theorem.

Thus clustered pruning supplies enough surviving **vertices**, but physical
fusion needs genuine information about the distribution of cylinder supports.
Sections 1--4.1 apply to arbitrary exact cylinders on a central Johnson
slice.  Theorem 4.2 additionally invokes the authenticated fixed-base facet
deck and its exact trace-necessity formula.

## 1. Exact trace quotient

Define `Lambda_b` on `2^E` by joining `T,T'` when either

\[
 |T\triangle T'|=1,
 \quad\hbox{or}\quad
 |T|=|T'|\ \hbox{ and }\ |T\triangle T'|=2.               \tag{1.1}
\]

Thus `Lambda_b` contains the Boolean cube `Q_b`; in addition, each level is
the Johnson graph `J(b,t)`.

### Lemma 1.1 (quotient-component identity)

For `D subseteq 2^E`, delete

\[
             \bigcup_{T\in D}\mathcal C(E,T)              \tag{1.2}
\]

from `J(n,a)`.  The connected components of the remaining graph are exactly
the inverse images of the connected components of `Lambda_b-D` under
`X mapsto X cap E`.

### Proof

For fixed `T`, its fibre is `J(n-b,a-|T|)` and is connected.  A Johnson edge
either swaps two points outside `E`, swaps two points inside `E`, or swaps one
point across the boundary of `E`.  Its two traces are therefore equal or are
adjacent by (1.1).

Conversely, a same-level edge in (1.1) lifts by keeping the outside part
fixed.  An inclusion edge `T -> T+e` lifts by deleting one chosen outside
point; the reverse edge lifts by inserting one unchosen outside point.  The
feasibility assumption guarantees these choices.  Hence connected trace
components lift to connected unions of fibres, and no edge joins two distinct
trace components. \(\square\)

### Corollary 1.2 (sharp first disconnection)

Exactly `b` trace cylinders are necessary and sufficient to disconnect a
single fixed-support reservoir.

### Proof

The cube `Q_b` has vertex connectivity `b`.  Since it is a spanning subgraph
of `Lambda_b`, adding the level-Johnson edges cannot lower vertex
connectivity.  On the other hand, the empty trace has degree `b` in
`Lambda_b`.  Deleting the `b` singleton traces isolates it. \(\square\)

This sharp cut isolates only an exponentially small trace fibre.  It is not a
balanced obstruction.

### Proposition 1.3 (exact lifted socket multiplicities)

Put `N=n-b`, and let `T,T'` be feasible traces.  The number of physical
Johnson edges between their fibres is

\[
 e(T,T')=
 \begin{cases}
 \displaystyle\binom N{a-|T|},
   &|T|=|T'|,\ |T\triangle T'|=2,\\[3mm]
 \displaystyle(a-|T|)\binom N{a-|T|},
   &T'=T+u,\\[3mm]
 \displaystyle(a-|T'|)\binom N{a-|T'|},
   &T=T'+u.
 \end{cases}                                               \tag{1.3}
\]

The number of edges internal to the fibre of `T` is

\[
 {1\over2}\binom N{a-|T|}(a-|T|)(N-a+|T|).                \tag{1.4}
\]

Consequently a connected surviving trace quotient does not merely lift to
one connected core family: every quotient tree edge has the full socket bank
in (1.3).

### Proof

For a same-level trace exchange, the outside part is unchanged, giving one
edge for each of its `binom(N,a-|T|)` choices.  If `T'=T+u`, a lower-fibre
vertex has `a-|T|` outside points, and deleting any one of them while inserting
`u` gives a different crossing edge.  The reverse formula is the same count
with the smaller trace named first.  The last display is the ordinary edge
count of `J(N,a-|T|)`. \(\square\)

## 2. One frame cannot destroy its reservoir giant

### Theorem 2.1 (fixed-support trace resilience)

If `D subseteq 2^E`, `|D|=s`, then `Lambda_b-D` has a component containing at
least

\[
                         2^b-(b+1)s                       \tag{2.1}
\]

trace vertices.

If in addition

\[
 a=n/2+O(b),\qquad b=O(\sqrt n),                           \tag{2.2}
\]

then its lifted component in `J(n,a)` contains a fraction

\[
                         1-O(bs/2^b)                      \tag{2.3}
\]

of all cores.

### Proof

At most one component of `Lambda_b-D` has more than `2^(b-1)` vertices.
For every other component `K`, its cube edge boundary obeys

\[
 |partial_Q K|\ge |K|.                                    \tag{2.4}
\]

Indeed the cube edge-isoperimetric inequality gives
`|partial_Q K| >= |K|(b-log_2|K|)`.  Every such boundary edge ends in `D`,
because a cube edge is also an edge of `Lambda_b`.  Summing over the small
components gives total size at most `bs`, since the deleted trace vertices
have only `bs` incident cube edges in total.  Adding the `s` deleted traces
proves (2.1).

Under (2.2), for every `T subseteq E`,

\[
 { |\mathcal C(E,T)|\over\binom na}
 ={(a)_{|T|}(n-a)_{b-|T|}\over(n)_b}
 =\Theta(2^{-b})                                           \tag{2.5}
\]

uniformly in `T`; the implicit constants depend only on the constants in
(2.2).  Therefore the omitted `(b+1)s` fibres have total mass
`O(bs2^(-b))`, proving (2.3). \(\square\)

For the unbuffered packet, one opposing frame contributes only
`s=O(q^2)` traces on its one outside support and `b=Theta(q)`.  The loss in
(2.3) is exponentially small.  Thus the obstruction cannot come from one
opponent in isolation.

### Corollary 2.1a (explicit Johnson connector tree)

Every component in Lemma 1.1 has an explicit spanning tree of
Johnson-adjacent cores.  In particular, the giant in Theorem 2.1 can be
equipped with such a tree, and every connector satisfies
`|X\setminus Y|=|Y\setminus X|=1`.

### Proof

Choose a spanning tree of the corresponding component of `Lambda_b-D`.
Inside every trace fibre choose a spanning tree of
`J(n-b,a-|T|)`.  For each trace-tree edge, use the literal lift constructed
in Lemma 1.1 to join the two fibre trees.  Their union is the required
spanning tree. \(\square\)

These are explicit **rank-legal** connectors.  Whether their packet collars
have equal affected marked-chain inventories is an additional transparency
condition not encoded by the cylinder deletion model.

### Proposition 2.2 (a cylinder-count lower bound for fragmentation)

Suppose every component of `Lambda_b-D` has at most `eta 2^b` trace vertices,
where `eta<=1/2`, and put `s=|D|`.  Then

\[
 s\ge {2^b\log_2(1/\eta)\over b+\log_2(1/\eta)}.           \tag{2.6}
\]

### Proof

Apply the cube edge-isoperimetric inequality to every surviving component.
All cube boundary edges end in `D`, so

\[
 (2^b-s)\log_2(1/\eta)
 \le \sum_K |partial_QK|\le bs.                            \tag{2.7}
\]

Rearrangement is (2.6). \(\square\)

### Theorem 2.3 (disjoint-support product giant)

Let `E_1,...,E_t` be pairwise disjoint, put `b_i=|E_i|` and
`B=sum_i b_i`, and suppose

\[
                         B<\min(a,n-a).                   \tag{2.8}
\]

On `E_i` delete `s_i` exact traces, and let `G_i` be the giant trace
component supplied by Theorem 2.1.  The cores satisfying

\[
                         X\cap E_i\in G_i\quad(1\le i\le t) \tag{2.9}
\]

induce one connected Johnson subgraph.  Under the central assumptions
(2.2), its relative size is at least

\[
                 1-O\!\left(\sum_i b_i s_i2^{-b_i}\right). \tag{2.10}
\]

#### Proof

Fix a tuple of allowed traces.  Its remaining outside fibre is a Johnson
graph on `[n]-union_iE_i` and is connected.  Condition (2.8) guarantees
that this fibre has both a selected and an unselected outside coordinate
for every trace tuple.  Hence every inclusion/deletion edge in a tree of
some `G_i` lifts by exchanging the changed `E_i` coordinate with an outside
coordinate; same-level edges lift without changing the outside part.
Taking the product of the trace trees and the outside fibre trees proves
connectivity.

For each `i`, Theorem 2.1 and the uniform marginal trace estimate omit
`O(b_i s_i2^{-b_i})` of the central slice.  A union bound over `i` gives
(2.10). \(\square\)

This theorem is genuinely transverse but applies to at most `O(n/q)`
supports of size `Theta(q)`.  The clustered extraction has exponentially
many overlapping supports; small pairwise intersections do not turn them
into the disjoint product in (2.9).

## 3. Adversarial periodic-layer fragmentation

The fixed-support resilience threshold is eventually reached by the complete
clustered budget.

Assume (2.2), and let `2<=ell<=sqrt(b)`.  For a residue `r mod ell`, put

\[
 D_r=\{T\subseteq E: |T|\equiv r\pmod\ell\}.              \tag{3.1}
\]

### Theorem 3.1 (vanishing-density, many-component obstruction)

There is a residue `r` such that deletion of the cylinders indexed by `D_r`
has all of the following properties:

\[
 |D_r|\le {2^{b+1}\over\ell},                              \tag{3.2}
\]

\[
 {1\over\binom na}
 \left|\bigcup_{T\in D_r}\mathcal C(E,T)\right|
 \le {2\over\ell},                                       \tag{3.3}
\]

and every remaining component has core mass at most

\[
                         O(\ell/\sqrt b).                  \tag{3.4}
\]

There are `Theta(b/ell)` nonempty components.  Consequently any fixed number
of components has mass `O(ell/sqrt(b))`.

### Proof

For each residue define

\[
 A_r=2^{-b}\sum_{t\equiv r(\ell)}\binom bt,
\qquad
 B_r={1\over\binom na}\sum_{t\equiv r(\ell)}
       \binom bt\binom{n-b}{a-t}.                          \tag{3.5}
\]

Both `(A_r)` and `(B_r)` are probability vectors.  Hence some residue has
`A_r+B_r<=2/ell`.  This gives (3.2) and (3.3).

Every edge of `Lambda_b` changes trace cardinality by at most one.  The
forbidden cardinality levels therefore separate the surviving graph into
the maximal bands of fewer than `ell` consecutive allowed levels.  Each band
is connected: individual levels are Johnson-connected, and consecutive
levels have inclusion edges.

The hypergeometric variable `H=|X cap E|` has variance `Theta(b)` under
(2.2), and its maximal atom is `O(b^(-1/2))` by the standard unimodality and
Stirling bound.  A band contains fewer than `ell` atoms, proving (3.4).
All trace levels are feasible, so the number of bands is `Theta(b/ell)`.
\(\square\)

Taking

\[
                         \ell=\lfloor b^{1/4}\rfloor       \tag{3.6}
\]

deletes only `O(b^(-1/4))` of the cores using
`O(2^b/b^(1/4))` exact cylinders, but the largest component and every fixed
union of components have mass `O(b^(-1/4))`.  For `b=q+O(1)` this cylinder
count lies below the `Theta(2^q)` total cross-cylinder budget in the
clustered-pruning extraction.

This is an obstruction to any theorem whose hypotheses mention only total
cylinder count, total deleted density, or the one-opponent estimate.  It is
not yet a claim that the structured packet menus can realize (3.1).

## 4. Independent supports avoid the exhibited obstruction

The periodic construction uses exponentially many traces concentrated on
one coordinate support.  Independent random supports do not have this
geometry.

### Theorem 4.1 (random outside-support dispersion)

Let `n=Theta(q^2)`, let `R<=exp(C_R q)`, and independently sample supports
whose outside parts `E_i`, conditional on their sizes, are uniform subsets
of `[n]`.  Suppose their sizes arise as `Q-|A_i cap A_0|`, where
`Q=Theta(q)` and `A_i,A_0` are independent `Q`-subsets of a
`Theta(q^2)`-set.  Then, with probability tending to one,

1. `|E_i|=(1-o(1))Q` for every `i`;
2. all `E_i` are distinct;
3. `max_(i!=j)|E_i cap E_j|=O(q/log q)`.

### Proof

For `t>=1`, a hypergeometric tail estimate gives

\[
 \Pr(|A_i\cap A_0|\ge t)
 \le \left({C\over t}\right)^t.                           \tag{4.1}
\]

Take `t=Kq/log q`, with `K` larger than the constant hidden in
`log R=O(q)`.  Then the logarithm of the right side is
`-Kq+o(q)`.  The union over all sampled supports tends to zero.  Hence
`|E_i|=Q-O(q/log q)=(1-o(1))Q` simultaneously.

Conditional on sizes at least `Q-O(q/log q)`, two equal outside supports have
probability at most

\[
 {1\over\binom n{Q-O(q/\log q)}}
 =\exp(-(1-o(1))q\log q).                                 \tag{4.2}
\]

After a union bound over `R^2` pairs and the `O(q)` possible sizes, this is
`o(1)`.

Finally, for two independent outside supports of sizes at most `Cq`,

\[
 \Pr(|E_i\cap E_j|\ge t)
 \le \left({C'\over t}\right)^t,                          \tag{4.3}
\]

because `|E_i||E_j|/n=O(1)`.  Taking
`t=C''q/log q` with `C''` sufficiently large absorbs the `R^2=exp(O(q))`
union bound. \(\square\)

Theorem 4.1 rules out the common-support periodic separator (3.1) in the
actual random sampling argument.  It does **not** imply that the survivor is
connected.  A family of transverse exact cylinders is a high-arity
constraint system, and pairwise support dispersion alone does not provide a
Johnson path between arbitrary surviving cores.

### Proposition 4.1a (exact local random calibration)

Let `b=q+O(1)`, `n=Theta(q^2)`, and let each of `R` independent frames
delete at most `s=O(q^2)` traces on its random `b`-support.  Assume the
support and its typed trace menu are relabelled independently of the fixed
core or edge being tested, so that the uniform central trace bound remains
valid after conditioning that the support meets either exchanged coordinate.
This is the symmetry used in the packet sampling.  If

\[
                         R=\alpha {2^q\over q^2},         \tag{4.3a}
\]

then a fixed core is deleted with probability at most `O(alpha)`.  For a
fixed Johnson edge, the probability that exactly one endpoint is deleted is
at most

\[
                         O(\alpha/q).                     \tag{4.3b}
\]

These estimates do not imply a giant component.

#### Proof

The central trace estimate bounds the one-frame deletion probability of a
fixed core by `Cs2^(-b)`.  Summing over (4.3a) gives `O(alpha)`.

The restrictions of adjacent cores differ only if the random support meets
one of the two exchanged coordinates, an event of probability `O(b/n)`.
Conditioned on this event, the same trace estimate, with a changed absolute
constant, bounds a one-sided deletion by `Cs2^(-b)`.  Thus one frame cuts a
fixed Johnson edge with probability

\[
 O((b/n)s2^{-b})=O(q2^{-q}).
\]

Summing over (4.3a) proves (4.3b).  The periodic construction in Section 3,
with a fixed modulus, has constant deleted density and only `Theta(1/q)` of
Johnson edges crossing the deleted set, yet has no linear component.
Therefore neither estimate has the strength of a separator theorem.
\(\square\)

For a deletion set `D`, a union `S` of survivor components satisfies

\[
                         N_{\mathcal J}(S)-S\subseteq D.   \tag{4.3c}
\]

Conversely, every survivor set satisfying (4.3c) is a union of components.
Consequently, once a positive survivor density is known, the exact random
statement needed for a giant is a **separator anti-cover** theorem: with
high probability no survivor set of middle-slice measure in a fixed
interval `[epsilon,1/2]` has its entire external Johnson boundary covered
by the sampled cylinder union.  Proposition 4.1a is only a first-moment
edge calibration and does not prove this anti-cover statement.

### Theorem 4.2 (actual common-base facet fragmentation)

Common-base conditioning and even a complete support-intersection graph do
not imply connectivity.  More precisely, take a singleton-base reservoir

\[
 A_0=\{\beta\}\mathbin{\dot\cup}V_0,\qquad |V_0|=q,
\]

whose core ground `G_0=[k]-A_0` has size `n`, and whose core indices are
`X in binom(G_0,a)`.  Assume

\[
 a=n/2+O(q),\qquad n=\Theta(q^2).                         \tag{4.4}
\]

Choose pairwise disjoint `q`-sets `E_1,...,E_t subset G_0`, where

\[
 t=\left\lfloor{\min(a,n-a)\over2q}\right\rfloor
   =\Theta(q),                                             \tag{4.5}
\]

and for every `j` take one genuine opposing singleton-base facet frame with
support

\[
                         A_j=\{\beta\}\dot\cup E_j.        \tag{4.6}
\]

Delete from the base reservoir every core whose module shares a named
resource with one of these `t` opposing frames.  Then

\[
 {\#\{\hbox{deleted base cores}\}\over\binom na}
      =O(tq^2 2^{-q})=O(q^3 2^{-q})=o(1),                 \tag{4.7}
\]

but the survivor induced in `J(n,a)` has at least

\[
                         2^t=2^{\Theta(q)}                 \tag{4.8}
\]

connected components.  All `t+1` frame supports contain `beta`, so their
support-intersection graph is a clique.

### Proof

The complete trace list of the `j`-th opposing frame on `E_j` consists of
two singleton traces, cyclic intervals of sizes `2,...,q-2`, and the `q`
co-singletons

\[
                         E_j-\{v\},\qquad v\in E_j.        \tag{4.9}
\]

It contains neither the empty trace nor the full trace `E_j`.  The trace
necessity lemma from clustered pruning therefore says that every base core
whose trace on every `E_j` is either empty or full survives all `t` opposing
frames.

Every co-singleton trace in (4.9) is not merely a necessary pattern; its
whole cylinder is genuinely deleted.  Indeed, let

\[
 X\cap E_j=E_j-\{v\}
\]

and choose any `u in V_0`.  The base owner

\[
             \{\beta\}\cup X\cup(V_0-\{u\})              \tag{4.10}
\]

equals the `v`-omitting owner of the opposing module whose core is

\[
       Y=(X-(E_j-\{v\}))\cup(V_0-\{u\}).                  \tag{4.11}
\]

The set `Y` has size `a` and is disjoint from `A_j`, so it is a valid module
index.

For a surviving core define

\[
 \eta_j(X)={\bf1}_{\{X\cap E_j=E_j\}}.                    \tag{4.12}
\]

A Johnson edge can change a full trace on `E_j` only to a co-singleton, and
can enter the full trace only from a co-singleton.  Those intermediate
vertices were deleted by (4.9)--(4.11).  Hence the vector
`eta(X) in {0,1}^t` is constant on every survivor component.

Every binary vector occurs.  For `S subseteq[t]`, include all of `E_j` when
`j in S`, include none of it otherwise, and choose the remaining
`a-q|S|` points from

\[
                         K=G_0-\bigcup_jE_j.
\]

The inequalities in (4.5) guarantee
`0<=a-q|S|<=|K|` for every `S`.  This proves (4.8).

Finally one opposing frame has `q^2-2q+2=O(q^2)` occurrence traces.  The
uniform trace estimate (2.5), or Lemma 9.2 of the fixed-base collision note,
bounds every one of their cylinders by `O(2^-q)binom(n,a)`.  A union bound
over the `t` frames proves (4.7). \(\square\)

Theorem 4.2 is stronger than the abstract statement that a malicious cylinder
family may disconnect the graph: it uses the literal owner row of the actual
facet menu.  It also shows that pairwise support dispersion is not, by itself,
a component-count theorem--the outside supports here are disjoint.  It does
not contradict the possibility of a `1-o(1)` giant, because the components
distinguished by a full `q`-trace can have exponentially small mass.

## 5. Exact remaining fusion lemma

The proof-safe positive target is now the following.

> **Transverse-cylinder resilience.**  Let `R=Theta(2^q/q^2)` supports of
> size `Theta(q)` be sampled in a `Theta(q^2)` coordinate set.  On each
> support delete at most `Cq^2` exact traces, using the packet footprint
> menus.  Condition on a positive surviving density.  Prove that the induced
> survivor in `J(n,a)` has a linear component, preferably `O(1)` components,
> and export Johnson-adjacent edges carrying the required transparent socket
> labels.

Theorem 2.1 proves this for one support.  Theorem 3.1 shows that it is false
for adversarially concentrated supports, even at vanishing deletion density.
Theorem 4.1 verifies that independent sampling removes that explicit
concentration.  Passing from dispersion to a connected transparent socket
bank is the remaining nontrivial step; it cannot be replaced by generic
density or Johnson isoperimetry alone.

## 6. Relation to the unbuffered packet theorem

The vertices here are precisely the common cores of one singleton-support
reservoir in
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`.
Conditional on the footprint formulas in that note, Johnson adjacency gives
its necessary mixed-owner rank bound.
The present theorem supplies many literal adjacent cores before cross-frame
pruning and proves that each individual opponent leaves an overwhelming
connected core bank.  It does not prove that the final pruned adjacency edges
are chain-transparent, nor does it address exterior upper windows, residence,
topology, or the terminal compiler.
