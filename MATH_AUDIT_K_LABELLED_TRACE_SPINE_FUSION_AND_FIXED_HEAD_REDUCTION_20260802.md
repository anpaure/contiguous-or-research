# Independent audit: labelled trace spine fusion and the fixed-head reduction

**Date:** 2026-08-02  
**Verdict:** GO within the stated post-rounding scope.  The audit checks
`MATH_THEOREM_K_LABELLED_TRACE_SPINE_MATCHING_AND_ROOTED_EULER_FUSION_20260802.md`.
It does not audit or assert the missing common integral pull-clock rounding.

## 1. Literal de Bruijn switch

Write two order-`d` arcs as

\[
 e=(B_0,M,B_d),\qquad f=(C_0,N,C_d),                 \tag{1.1}
\]

where `M,N` are the internal `(d-1)`-letter words.  Their tails are
`(B_0,M),(C_0,N)` and their heads are `(M,B_d),(N,C_d)`.

The old tail `(B_0,M)` can point to the opposite head `(N,C_d)` exactly
when `M=N`; the other crossed arc gives the same condition.  Therefore the
spine-equality statement is both necessary and sufficient.  For `d=1`,
`M=N` is the equality of two empty words, so every literal pair passes the
geometry row, as it should.

Payload transparency is an independent condition.  Even when `M=N`, the
new terminal `C_d` must lie in the complete labelled terminal menu of the
first occurrence, and conversely.  This includes the owner cap and every
marked lower target.  Hence the theorem does not confuse a state rectangle
with an owner/target-transparent rectangle.

## 2. Hinge formula

For a chain

\[
 \varnothing=S_0<S_1<\cdots<S_\ell<T,\qquad\ell\le d-1,
\]

the displayed construction has the following suffix unions:

\[
 \bigcup_{p=d-j}^{d}B_p
 =(S_j\setminus S_{j-1})\cup\cdots\cup S_1\cup B_d
 =S_j                                                     \tag{2.1}
\]

for every `1<=j<=ell`, since `empty != B_d subseteq S_1`.
All earlier filler letters lie outside these suffixes.  The internal spine
is independent of the variable first and last letters, and

\[
 B_0\cup\cdots\cup B_d
 =(T\setminus S_\ell)\cup S_\ell=T.                    \tag{2.2}
\]

The endpoint cases are correct:

* `ell=1` leaves only the fixed penultimate letter `S_1` and the earlier
  singleton fillers;
* `ell=d-1` has no early filler positions; and
* `ell=d` is deliberately excluded, because a strict target at every proper
  suffix depth fixes all `d` head letters.

The full terminal pool is therefore exactly the nonempty subsets of `S_1`.
If further unmarked or exterior data are to be preserved, they must be
added to the occurrence menu; the lemma does not silently preserve them.

## 3. Matching factorization

Once tails are fixed, their multiplicity at every state fixes the required
head multiplicity through state balance.  Head occurrences must be treated
as tokens: two equal literal heads are two matching vertices.  A de Bruijn
arc can receive only a head token with the same spine by Section 1.  Thus a
tail-fixed balanced rerouting is precisely a bijection from the labels of
each spine to its old head tokens, restricted by labelled admissibility.
This is one bipartite perfect matching per spine.

Conversely, those perfect matchings preserve both the tail and head token
multisets, hence every state boundary coefficient.  They also preserve
every occurrence payload by the definition of their edges.  The direct
product and integrality statements therefore follow from ordinary
bipartite matching integrality.  No connectedness conclusion is hidden in
this step.

## 4. Fusion and root

In a weakly connected balanced directed component, every selected arc lies
on a directed cycle.  Deleting one selected arc leaves its underlying weak
support connected.  Therefore:

* cyclically permuting one head token among one selected arc from every
  component joins exactly the component cycle induced by that permutation;
* a one-cycle head permutation joins all components;
* a transparent `2x2` using arcs in two different current components merges
  those components; and
* a connected component--pool incidence graph stays connected after each
  such contraction.

The pool proof may reuse a complete pool: the labels remain in that pool and
its head tokens are merely permuted.  It never touches a protected label.
The final connected balanced support is Eulerian.  Since an Euler circuit
contains the untouched protected root occurrence, cyclic rotation roots it
there at zero extra length.

For the simultaneous fusion-tree version, deletion of several arcs from one
old component is not automatically safe; the theorem explicitly assumes
connected punctured support.  That qualification is necessary and correctly
stated.

## 5. Rigid full-depth indexing

If every chain has `d` strict marked targets, successive differences force

\[
 A_{i,d-j+1}=S_{i,j}\setminus S_{i,j-1}.              \tag{5.1}
\]

Thus trace `i` has fixed head

\[
                         h_i=(A_{i,1},\ldots,A_{i,d}). \tag{5.2}
\]

and variable first letter `B_(i,0)` satisfying

\[
 T_i\setminus S_{i,d}\subseteq B_{i,0}\subseteq T_i. \tag{5.3}
\]

For `h_j` to be the tail of trace `i`, literal state equality is exactly

\[
 (A_{j,2},\ldots,A_{j,d})
   =(A_{i,1},\ldots,A_{i,d-1}),\qquad B_{i,0}=A_{j,1}, \tag{5.4}
\]

and (5.3) is the displayed owner-cap condition.  Hence the arc definition
`j -> i` is correct.

Global distinctness of all marked targets implies the heads `h_i` are
distinct.  Balance then forces the tail multiset to be exactly the same
`W` states, one each.  A trace selection is consequently a directed cycle
cover of the explicit overlap graph.  Its Euler components are its
permutation cycles, so connected zero-sidecar support is exactly a Hamilton
cycle.  The crossed pair

\[
        j\to i,\ \ell\to m
          \quad\mapsto\quad
        j\to m,\ \ell\to i                              \tag{5.5}
\]

keeps the fixed heads, hence the owner-chain labels, and merges two distinct
cycles whenever all four arcs are legal.

For `d=1`, (5.4)'s word equality is empty and only the owner cap remains;
the reduction still holds.

## 6. Sidecar and obstruction scope

Switches inside a pool never cross a connected component of the original
component--pool incidence graph.  Conversely, the fusion theorem joins each
incidence block.  Therefore the exact minimum number of components under
that move class is the number `b` of incidence blocks.  This is not claimed
against tail-changing or larger alternating circuits.

At least `b-1` added edges are needed to connect `b` weak components.  The
upper bound must use the exact de Bruijn reset distance

\[
                         d-\operatorname{ov}(v,u),     \tag{6.1}
\]

so `b=O(1)` alone gives only `O(d)`, not `O(1)`.  The theorem correctly
requires total overlap deficit `O(1)` for a bounded sidecar.

## 7. Exact surviving lemma

The audit supports the theorem's final separation:

1. common one-copy owner/named-target rounding is still open;
2. after such a rounding, tail-fixed rerouting is integral;
3. exact fusion follows from a connected transparent spine-pool atlas, a
   connected head-permutation packet, or a protected fusion tree; and
4. proving that the triangular pull-clock support admits one of those
   correlated objects is the minimal remaining post-rounding lemma.

No residence, upper-shadow, compiler, or `nu(k)` claim follows from this
audit.
