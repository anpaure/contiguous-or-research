# K17 short-slot dual matroid and the exact socket-intersection gate

**Date:** 2026-08-02  
**Status:** proof-complete for the static outer matching and for a private
socket-ticket bank.  Whether the actual shared long-endpoint socket system is
matroidal is deliberately left open pending an occurrence-labelled exchange
audit.  This note is not a `1S-ROTS` certificate.

## 1. Static notation

Let `R` be the `18646` real bottom tokens.  On the right let `F` be the
`1748` singleton/free hosts and let `H` be the `18646` hard hosts.  A real
token is adjacent to a free host or hard host by the exact Boolean
containment rows in the augmented-matching theorem.  Let

\[
  M=M(G)
\]

be the transversal matroid on the ground set `F disjoint_union H`: a host set
is independent precisely when it can be matched injectively into `R`.
Every valid augmented static table matches every free host to a real token,
matches `16898` hard hosts to the remaining real tokens, and leaves the other
`1748` hard hosts to the dummy bank.

Assume first that `F` is independent; otherwise the static outer face is
empty.  Put

\[
  N=M/F\quad\hbox{on }H,
  \qquad M_{\rm short}=N^*.
\]

## 2. Exact short-set theorem

### Theorem 2.1

A set `S subset H` is the set of dummy/short slots of an augmented perfect
matching if and only if `S` is a basis of `M_short`.  In particular,

\[
 |S|=1748.
\]

#### Proof

The real-occupied hard set `I=H\S` extends the mandatory set `F` to a basis
`F union I` of `M` if and only if `I` is a basis of the contraction `N=M/F`.
By the definition of matroid duality, `I` is a basis of `N` if and only if
its complement `S=H\I` is a basis of `N^*=M_short`.  The rank is
`|H|-16898=1748`.  This correspondence is literal: a matching witnessing
`F union I` and arbitrary bijection from the dummy tokens to `S` materialize
the augmented table.  \(\square\)

### Corollary 2.2 (short-slot exchange)

For two feasible short sets `S,S'` and every `v in S\S'`, there is some
`w in S'\S` such that

\[
 (S-\{v\})\cup\{w\}
\]

is feasible.  Thus outer short-slot exchanges are matroidal even though a
particular real-token matching realizing the exchanged basis may require a
long alternating rematch.

### Proposition 2.3 (exact matching-rank oracle)

For every `S subset H`,

\[
 \boxed{
 r_{M_{\rm short}}(S)
   =|S|-18646+r_M\!\left(F\cup(H\setminus S)\right).}
 \tag{2.1}
\]

#### Proof

For `N=M/F`, dual rank gives

\[
 r_{N^*}(S)=|S|+r_N(H\setminus S)-r_N(H).
\]

Here `r_M(F)=1748`, `r_N(H)=16898`, and

\[
 r_N(H\setminus S)
 =r_M(F\cup(H\setminus S))-1748.
\]

Substitution gives (2.1).  \(\square\)

The rank on the right is the cardinality of an ordinary maximum matching
from the retained right-host set `F union (H\S)` into the real bottoms.  It
therefore supplies an exact rank oracle and an independently checkable
short-basis deficiency

\[
 |S|-r_{M_{\rm short}}(S)
 =18646-r_M(F\cup(H\setminus S)).                 \tag{2.2}
\]

Fundamental short-basis circuits and valid exchange cuts can be extracted
from the corresponding alternating reachability graph.  No literal socket
predicate belongs in this rank computation; sockets enter only through the
separate second matroid when a private-ticket representation is proved, or
through the nonmatroidal occurrence oracle otherwise.

### Corollary 2.4 (exact additive optimization)

For arbitrary slot costs `c_v`, minimizing

\[
  \sum_{v\in S}c_v
\]

over augmented static tables is weighted basis optimization in
`M_short`.  It is equivalently min-cost augmented matching, or the contracted
transversal greedy already proved on the complementary real-occupied basis.

This proves optimality only for a score additive in the identity of the
short slot.  A score depending on the chosen neighboring real-token
placements or on simultaneous socket activations is not covered.

### Proposition 2.5 (complete-matching path/cycle exchange normal form)

Let `P_0,P_1` be two complete real-bottom matchings: each saturates every
real token, every free host, and `16898` hard hosts.  Ignore dummy labels and
colour the edges of `P_0` old and those of `P_1` new.  In their symmetric
difference:

* every real token has degree zero or two;
* every free host has degree zero or two;
* every hard host has degree zero, one, or two; and
* the degree-one hard hosts are exactly
  `S_0 triangle S_1`, where `S_i` is the short set of `P_i`.

Hence every nontrivial component is an even alternating cycle or an
alternating path whose two endpoints are one member of `S_0-S_1` and one
member of `S_1-S_0`.

Flipping old/new edges on one cycle gives another complete real matching
with short set `S_0`.  Flipping one path gives another complete real
matching with short set

\[
 S_0-\{f\}+\{e\},
 \qquad f\in S_0-S_1,quad e\in S_1-S_0.             \tag{2.3}
\]

Thus path components are literal realizations of fundamental
`M_short`-basis exchanges; cycle components are same-basis bottom-placement
circuits.  Any union of vertex-disjoint components may be flipped
simultaneously and remains an exact static table.

#### Proof

Every real token is incident with one edge of each matching.  A right host
covered in both matchings also has one edge of each colour, while a hard
host covered in exactly one has degree one.  Free hosts are covered in both.
The standard degree-two decomposition gives alternating paths and cycles.
On a component, replacing all old edges by all new edges preserves degree
one at every internal vertex.  A cycle changes no covered host.  A path
interchanges which of its two hard endpoints is covered, giving (2.3).
All other edges stay fixed.  \(\square\)

This gives a finite exact first Pareto neighbourhood between any two outer
tables.  Projection perfection and literal socket counts are not invariant
under a component flip; each candidate must be rematerialized and replayed.

## 3. Admissible-bank Hall is a matroid minor test

Let `A subset H` be a declared bank in which all short slots must lie.  Then
`S subset A` is possible if and only if `H\A` is contained in some basis of
`N`, equivalently is independent in `N`.  Written in the original bipartite
graph, this is exactly the two Hall families

\[
 |N_F(X)|+|N_H(X)|\ge |X|,
\]

and

\[
 |N_F(X)|+|N_H(X)\cup A|\ge |X|+1748
 \qquad(X\subseteq R).
\]

The empty-set instance gives `|A|>=1748`.  Therefore the admissible-bank
maxflow is an exact fail-fast oracle for the declared restricted face.  It
becomes a necessary global `1S` no-go only when `A` is obtained from a
complete proof-safe global socket catalogue.  A fixed-table or soft-endpoint
bank has only its stated restricted scope.

## 4. When sockets give exact matroid intersection

Suppose there is a set `P` of **private socket tickets** and a bipartite graph
between hard slots and tickets such that:

1. slot `v` can be shortened using ticket `p` exactly when `vp` is an edge;
2. distinct selected tickets have disjoint physical long placements, flags,
   degree resources, and all other protected resources by construction; and
3. **pure-refinement/factorization:** for every slot set `S`, an outer
   matching witnessing `S in M_short` and a distinct-ticket matching
   witnessing `S` can be realized simultaneously.  In particular, any
   real-token/long-host placements carried by the tickets are in a reserved
   bank or have a proved extension theorem; and
4. no constraint remains except choosing distinct tickets.

Then the slot sets admitting distinct tickets form a transversal matroid
`M_sock` on `H`.

### Theorem 4.1 (private-ticket joint selector)

There is a statically feasible `1748`-slot short bank with private sockets if
and only if `M_short` and `M_sock` have a common independent set of size
`1748`.  Equivalently, by Edmonds' matroid-intersection min-max theorem,

\[
 \boxed{
 r_{M_{\rm short}}(X)+r_{M_{\rm sock}}(H\setminus X)\ge1748
 \quad\text{for every }X\subseteq H.}
\]

A common set of size `1748` is automatically a basis of `M_short`; its
ticket matching supplies one private socket per short slot.  Weighted common
basis optimization handles any additive slot/ticket objective.

This is stronger than admissible-bank Hall: the latter remembers only
whether a slot has at least one ticket, whereas matroid intersection retains
injective ticket ownership.

Condition 3 is load-bearing.  Pairwise-disjoint ticket labels do not by
themselves show that their prescribed real-token placements extend the same
outer matching.  Without pure refinement, membership in both projected
matroids is only necessary and the placement-labelled coupled oracle remains.

## 5. Why the actual shared socket system is not yet a matroid

An occurrence-labelled five-cell socket generally consumes a *pair* of
long boundary placements together with flag and directed-degree resources.
Different sockets may share one endpoint, and several selected sockets must
also satisfy global in/out-degree and chronology equations.  Hence their
feasible slot family is a hypergraph packing/projection, not automatically a
transversal matroid.

The minimal abstract exchange obstruction has three short slots `a,b,c` and
two endpoint resources `x,y`:

* the only ticket for `a` consumes `{x,y}`;
* `b` has a ticket consuming `{x}`;
* `c` has a ticket consuming `{y}`.

Then `{a}` and `{b,c}` are feasible, but neither `b` nor `c` augments
`{a}`.  Thus the hereditary feasible family violates the augmentation axiom.
This abstract pattern is not asserted to occur in K17; it is the exact
pattern the physical catalogue must exclude before `M_sock` may be invoked.

### Required exhaustive audit

The aggregate per-slot degree and flag mask are insufficient.  Preserve, for
every catalogue element,

```text
short_slot, short_address, pred_host, pred_token, pred_flag,
succ_host, succ_token, succ_flag, directed_role
```

plus any contracted degree/history resource.  Define a set of slots to be
socket-feasible only after selecting one occurrence ticket per slot and
replaying all shared-resource and degree rows.  Then either:

1. prove structurally that this family is a transversal matroid (for example
   by compiling every accepted socket to one genuinely private ticket); or
2. test augmentation and freeze the smallest literal pair `I,J` with
   `|I|<|J|` for which no member of `J\I` augments `I`.

Until one of these succeeds, matroid intersection is valid only on an
explicit private-ticket subbank.  The complete global menu may still be used
for proof-safe zero deletion, the admissible-bank Hall fail-fast, and
optimistic additive pricing.

## 6. Exact remaining row

The smallest strengthened outer theorem is therefore:

> Construct a rank-`1748` private socket-ticket transversal matroid on the
> hard slots whose common-basis Edmonds inequalities with `M_short` all hold,
> or exhibit a physical basis-exchange obstruction in the complete shared
> socket catalogue and retain the full placement-labelled hypergraph/Benders
> row.

Even a positive common basis closes only static payload plus one private
socket per short slot.  Literal chronology, residence, upper shadows,
topology, common-cap/compiler feasibility, and the final word remain outside
this theorem.
