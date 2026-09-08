# Endpoint permutation group of the MNW alpha switches

## 1. Outcome

There are two sharply different facts.

1. **Abstractly, connected alpha supports have maximal even permutation
   power.**  On every connected component of the 3-uniform alpha-support
   hypergraph, the endpoint 3-cycles generate the full alternating group.
2. **They cannot perform endpoint antipodalization by themselves.**  Every
   alpha switch is an alternating circuit and therefore preserves the
   degree, and hence endpoint status, of every physical vertex.  The
   published Mütze--Weber endpoint set is not complement-invariant.  Thus
   no word in alpha switches—of Catalan length or any length—can map it to a
   complementary path factor.

The alpha group is consequently a possible *cycle-control* mechanism only
after an endpoint-moving signed `T`-join has been supplied.  The Catalan
long-trail decomposition in `MW_MSW_CATALAN_BRAID.md` supplies such a
candidate.  Static alpha cycles alone do not.

## 2. The formal permutation group

Let `V` label oriented path strands.  Let `mathcal H` be the 3-uniform
support hypergraph of available flipping tuples.  For every hyperedge

\[
                         e=\{a,b,c\},                 \tag{2.1}
\]

choose the orientation induced by its alternating 6-cycle and write

\[
                         \pi_e=(a\ b\ c).             \tag{2.2}
\]

### Theorem 1 (connected 3-cycle generation)

If the support hypergraph induced on `U subseteq V` is connected, then

\[
             \langle\pi_e:e\subseteq U\rangle=A(U).  \tag{2.3}
\]

For an arbitrary support hypergraph, the generated group is the direct
product of the alternating groups on its connected components.

### Proof

Every generator is even, so the generated group is contained in `A(U)`.
Order the edges of a connected spanning subhypergraph so that every new
edge meets the union of its predecessors.  The first 3-cycle generates
`A_3` on its support.

Inductively suppose `A(S)` has been generated.  Let a new triple meet `S`
and add one or two vertices.  Conjugating its 3-cycle by `A(S)` replaces
the old point or old pair in its support by any point or ordered pair of
`S`.  Products of two such conjugates give every 3-cycle involving a new
vertex and two old vertices; conjugating again gives all 3-cycles on the
enlarged set.  Since 3-cycles generate the alternating group, the enlarged
group is `A(S union e)`.  Induction proves (2.3).  Different connected
components have disjoint supports and commute.  \(\square\)

Consequently, if the available **3-cycle** charts have connected support on
all `Cat_m` strands, their formal group is `A_(Cat_m)`.  This connectivity
hypothesis must not be silently replaced by MNW's published spanning-tree
theorem for the complete family `Psi_m`: that family also uses the constant
base patterns, including supports of a different size.  Those generators
may enlarge the formal group (an even-size support induces an odd cycle),
but their exact strand action must be included before claiming either
`A_(Cat_m)` or `S_(Cat_m)` globally.

In all cases, the statement is algebraic.  It does not assert that an
arbitrary word in the formal generators is dynamically flippable in the
evolving factor.

## 3. The degree-boundary obstruction

Let `H` be the current factor and let `Z` be an alternating 6-cycle.  A
switch replaces `H` by

\[
                         H'=H\triangle Z.             \tag{3.1}
\]

At every vertex of `Z`, one old incident edge is deleted and one new edge
is inserted.  Hence

\[
                         \deg_{H'}(v)=\deg_H(v)        \tag{3.2}
\]

for every physical vertex `v`.  In particular, the endpoint set is fixed.

In signed-`T`-join notation, every alpha switch vector `z` satisfies

\[
                         \partial z=0.                 \tag{3.3}
\]

Thus every integral combination or dynamically valid sequence of alpha
switches remains in the cycle space `ker(partial)`.

For the published MW central induction, with

\[
 C=C_m,
 \qquad D=C_{m+1}-2C_m,
\]

the four endpoint-sector counts are

\[
                 (2D+C,\ 2C,\ C,\ 0).                \tag{3.4}
\]

Complementation exchanges sectors `00<->11` and `10<->01`, so this endpoint
set is not complement-invariant.  Reaching a complement-invariant set has
nonzero boundary demand.  Equations (3.3)--(3.4) prove:

### Theorem 2 (alpha-only antipodalization no-go)

No sequence of MNW/MW alternating-cycle switches can turn the published MW
dangling system into complementary paths.  This remains true with dynamic
chart selection, repeated generators, mirrored generators, and unlimited
word length.

The obstruction is endpoint status, not lack of permutation power.

## 4. Pairing monodromy after endpoint repair

Suppose a separate signed `T`-join has produced a complement-invariant
endpoint set.  Orient its `N` path strands as

\[
                         P_i:s_i\leadsto t_i.          \tag{4.1}
\]

Let `kappa` be the unique permutation satisfying

\[
                         t_{\kappa(i)}=\bar s_i.       \tag{4.2}
\]

A switch schedule with endpoint monodromy `pi` changes the path pairing to

\[
                         s_i\leadsto t_{\pi(i)}.       \tag{4.3}
\]

Add the artificial antipodal matching.  Starting at `s_i`, one augmented
step consisting of a path followed by an antipodal edge sends the strand
index to

\[
                         \kappa^{-1}\pi(i).            \tag{4.4}
\]

Therefore an augmented component corresponding to an `ell`-cycle of
`kappa^{-1}pi` contains exactly `ell` antipodal edges.  We obtain the exact
criterion

\[
 \boxed{
 \text{one antipodal edge in every augmented cycle}
 \iff \pi=\kappa.
 }                                                       \tag{4.5}
\]

Combining (2.3) and (4.5), on a connected alpha-support component the
*formal* alpha group can finish the pairing exactly when the required
restriction of `kappa` is even and preserves that component.  If it is odd,
parity is an additional obstruction: 3-cycles alone cannot realize it.  If
it is even, group generation proves algebraic reachability but not a
dynamically valid `O(N)` word.  A verified odd generator from a non-alpha
base pattern would remove parity, but not the endpoint-boundary obstruction.

## 5. Why the known loose tree is insufficient

A spanning loose tree proves group generation, but using each tree
generator once leaves every leaf strand with nontrivial monodromy.  Pairing
each generator with its natural antipodal copy applies the same 3-cycle
twice, not a cycle and its inverse.  This is the leaf obstruction from
`PAIRED_ALPHA_BRAID_OBSTRUCTION.md`.

Theorem 1 explains the apparent tension: the tree generators *generate*
the desired alternating group only after repetitions and nontrivial words.
The product of the generators used once is not identity and need not have
any endpoint-safe interpretation.  Connectivity is a group-generation
statement, not an endpoint-balanced schedule.

Dynamic validity is an additional restriction.  A geometric 6-cycle is an
involution on factor edge sets.  After it is toggled, an overlapping chart
may cease to be alternating.  Hence the actually reachable monodromies form
a subset of the formal group in (2.4).  This can only strengthen Theorem 2.

## 6. Constant-distance endpoint matching does not persist

Every last endpoint of the all-zero MW factor is a balanced path that moves
below zero exactly once.  It therefore has a unique form

\[
                         L=A\,01\,B,                  \tag{6.1}
\]

with `A,B` Dyck.  The canonical first-return bijection sends it to the
complement-Dyck endpoint

\[
                         \tau(L)=\overline{1A0B}.      \tag{6.2}
\]

This is an explicit all-dimensional bijection from the old unmatched last
endpoints to the new canonical endpoints.

Small dimensions suggest that a perfect matching of these two endpoint
families may exist at Johnson distance at most three.  That cannot be an
all-dimensional theorem.  Take

\[
 L_n=1^{n-1}0^{n-1}01.                                \tag{6.3}
\]

It belongs to `D_(2n)^-`.  In its first `n-1` positions all bits are one.
Any complement of a Dyck word is nonpositive, so among its first `n-1`
positions at most `floor((n-1)/2)` bits are one.  Consequently

\[
 d_J(L_n,\overline{\mathcal D_n})
 \ge \left\lceil {n-1\over2}\right\rceil.             \tag{6.4}
\]

Thus distance three must fail from semilength eight onward.  The finite
distance-three observation through cube dimension fourteen is real but
cannot drive the all-`k` proof.

This does not obstruct a Catalan number of *long* endpoint-moving trails.
The bijection (6.2) gives exactly one target endpoint per old last endpoint;
the remaining problem is to realize those pairs by edge-disjoint or
provenance-compatible alternating trails.

## 7. Correct hybrid target

The mathematical roles are now separated.

1. Use endpoint-moving alternating trails to leave the zero-boundary cycle
   space and reach a complement-invariant endpoint set.  The exact
   `H_0 triangle H_CF` decomposition provides at most `4 Cat_n` candidate
   long trails/circuits.
2. Use alpha-type alternating circuits only for component splitting and
   pairing monodromy.  Their formal group is alternating, and the exact
   target is `pi=kappa`.
3. Prove a dynamically valid word with controlled provenance.  Neither the
   loose spanning tree nor abstract group generation supplies this step.

This hybrid formulation avoids asking a cycle-space generator to solve a
nonzero endpoint boundary, which is algebraically impossible.
