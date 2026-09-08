# The atomic--alpha parity lock in the punctured Johnson prism

## 1. Verdict

The atomic rank-transfer square and the ordinary three-strand alpha switch
do not form a sufficient neutral-switch alphabet.

There are two independent obstructions.

1. Both moves are alternating circuits.  They preserve the degree of every
   physical vertex and therefore cannot repair a non-complement-invariant
   endpoint set.
2. Even after the endpoint set has been repaired separately, atomic squares
   and three-strand alpha switches satisfy an exact parity lock:

   \[
      \operatorname{sgn}(\pi)=(-1)^\tau,
   \]

   where `pi` is the induced endpoint-ownership permutation and `tau` is the
   signed number of units of tag transfer

   \[
      (-1,+2,-1).
   \]

   Consequently a ledger-neutral word has even endpoint monodromy, while a
   one-unit rank-transfer word has odd endpoint monodromy.  In particular,
   no such word is a pure endpoint transposition.

The smallest extension at the signature level is one move outside this
diagonal parity class.  The three-boundary ear braid has the required
signature, but the geodesic outer paths exclude it.  The four-boundary
segment exchange of `PRISM_RANK_TRANSFER_FLOW.md` is therefore the smallest
currently available prism move which breaks the lock.  It has one unit of
tag transfer and trivial endpoint monodromy.

This identifies a necessary local alphabet.  It does not construct a
dynamically closed switch system: composing the four-boundary exchange with
an inverse atomic square has the signature of a pure endpoint transposition,
but the two physical moves have not been proved successively flippable on one
evolving Catalan parent chart.

## 2. Endpoint ownership and transfer number

Fix a path factor with distinct oriented strand endpoints

\[
        P_i:s_i\leadsto t_i,\qquad 1\le i\le r.
\]

Every degree-preserving switch retains the physical endpoint sets.  Label the
new strands by their initial endpoints.  There is then a unique permutation
`pi` such that the new strand beginning at `s_i` ends at `t_(pi(i))`.
Call `pi` the endpoint-ownership monodromy.

Let

\[
                         v=(-1,+2,-1).
\]

For a switch word whose net change in the zero-, one-, and two-tag sector
ledger is an integer multiple of `v`, write

\[
                         \Delta N=\tau v.
\]

The integer `tau` is the signed transfer number.  A forward atomic square has
`tau=1`, and its reverse has `tau=-1`.

## 3. Signatures of the local moves

Record only

\[
        (\tau\bmod2,\;\epsilon),\qquad
        \epsilon=0\text{ for even monodromy},\quad
        \epsilon=1\text{ for odd monodromy}.
\]

### Lemma 3.1 (atomic signature)

An atomic rank-transfer square used between two distinct **rooted** path
strands, with the invariant that every resulting strand contains exactly one
old lower root, has
signature

\[
                              (1,1).
\]

### Proof

The square removes one zero-tag and one two-tag edge and inserts two one-tag
edges, so its transfer number is `+1`; reversing it gives `-1`, which is
still odd modulo two.

Deleting one internal edge from each of two rooted paths creates two
root-containing prefixes and two root-free suffixes.  Of the two nontrivial
pairings of the four loose pieces, the prefix--prefix/suffix--suffix pairing
would create one strand containing two lower roots and one containing none.
It is therefore inadmissible under root preservation.  The only admissible
cross reconnection attaches each prefix to the other path's suffix.  Thus the
two terminal owners are exchanged, and the endpoint monodromy is a
transposition.  Its sign is odd.  \(\square\)

The statement is scoped to the rank-transfer use of the square, where its
opposite removed edges belong to distinct strands and the old lower-root
ownership is retained.  This is precisely the admissibility condition needed
by the proposed neutral-switch lemma.  If root ownership is allowed to fail
at intermediate states, the other reconnection is possible, but it leaves the
claimed state space and cannot be used as a state-closed generator without a
separate root-repair theorem.  Toggling a square whose two old edges lie in
one component is likewise not the two-strand factor move used here.

### Lemma 3.2 (alpha signature)

An ordinary three-strand, tag-ledger-neutral alpha switch has signature

\[
                              (0,0).
\]

### Proof

Ledger neutrality gives transfer number zero.  The three path tails are
cyclically reattached, so the endpoint action is a 3-cycle, which is even.
The inverse orientation is also a 3-cycle and is also even.  \(\square\)

This lemma concerns the parameterized three-member alpha tuple.  A separate
verified even-support alpha chart could act by an odd cycle and would itself
be a parity-breaking generator.  The published connectivity theorem for the
full family of flipping tuples does not identify such a dynamically usable,
ledger-neutral chart, so it cannot be silently included in the present
alphabet.

## 4. The parity-lock theorem

### Theorem 4.1 (atomic--alpha parity lock)

Let a dynamically legal switch word be composed of forward or reverse atomic
rank-transfer squares and ordinary three-strand ledger-neutral alpha
switches.  If its transfer number is `tau` and its endpoint monodromy is
`pi`, then

\[
                    \boxed{\operatorname{sgn}(\pi)=(-1)^\tau.}
\]

### Proof

Suppose the word contains `q` atomic squares.  Every alpha factor is even,
and every atomic factor is odd, so

\[
                    \operatorname{sgn}(\pi)=(-1)^q.
\]

Write the orientations of the atomic squares as signs
`sigma_i in {+1,-1}`.  Alpha moves contribute zero to the tag ledger, hence

\[
                         \tau=\sum_{i=1}^q\sigma_i.
\]

Modulo two, `sigma_i=1` for either sign.  Therefore `tau=q (mod 2)`, proving
the formula.  \(\square\)

The proof uses only the signatures of moves that actually occur.  It does
not assume that all formal alpha generators remain available.  Dynamic
non-flippability can only shrink the reachable set and cannot evade the
invariant.

### Corollary 4.2 (no pure transposition)

No ledger-neutral atomic--alpha word induces an odd endpoint permutation.
In particular it cannot implement one pure endpoint transposition.

### Corollary 4.3 (no endpoint-neutral atomic transfer)

No atomic--alpha word with one net unit of tag transfer has even endpoint
monodromy.  Hence it cannot replace the endpoint-safe ear or four-boundary
rank-transfer braid.

More generally, if `D` units of prism imbalance are corrected using only this
alphabet, the final endpoint permutation is forced to have sign `(-1)^D`.
Agreement of this forced sign with the desired ownership permutation is a
necessary condition, not a sufficient one.

### Corollary 4.4 (neutral state graph is disconnected)

Fix the tag ledger and lower-root set, and form the reconfiguration graph
whose vertices are admissible rooted path factors and whose edges are
arbitrary dynamically legal atomic--alpha words returning to that same
ledger.  Endpoint-permutation parity is constant on every connected
component.  In particular, no component contains both a factor and the
factor obtained from it by one pure endpoint transposition.

### Proof

Every graph edge has transfer number zero, so Theorem 4.1 gives even relative
monodromy.  Parity therefore cannot change along a path in the state graph.
\(\square\)

This remains true if an edge of the reconfiguration graph is allowed to pass
through intermediate nonzero transfer ledgers.  Only its net transfer enters
Theorem 4.1.

## 5. Minimal parity-breaking extension

The signature quotient is the vector space

\[
                         \mathbb F_2^2.
\]

Atomic squares generate the diagonal vector `(1,1)`; ordinary alpha switches
generate zero.  Their span is only

\[
                         \{(0,0),(1,1)\}.
\]

### Theorem 5.1 (minimal signature alphabet)

To control transfer parity and endpoint parity independently, at least one
move with an off-diagonal signature is necessary.  Either of the following
is sufficient at the abstract signature level:

1. an endpoint-neutral transfer move with signature `(1,0)`; or
2. a ledger-neutral odd endpoint move with signature `(0,1)`.

Together with the atomic square, either move generates all of
`F_2^2`.  No smaller extension does.

### Proof

The diagonal subgroup has index two, so a generator outside it is necessary
and one such generator is sufficient.  Moreover

\[
                      (1,1)+(1,0)=(0,1),
\]

and symmetrically `(1,1)+(0,1)=(1,0)`.  \(\square\)

The known endpoint-safe transfer braids have exactly the first signature:

| move | transfer parity | endpoint parity | boundaries |
|---|---:|---:|---:|
| atomic rank square | 1 | 1 | two path cuts |
| three-boundary ear | 1 | 0 | three |
| four-boundary segment exchange | 1 | 0 | four |
| ordinary alpha switch | 0 | 0 | alternating 6-cycle |

The three-boundary ear is the abstract endpoint-safe minimum.  Lemma 3.3 of
`PRISM_RANK_TRANSFER_FLOW.md` proves that a nontrivial ear cannot use an
explicit geodesic `O_0(P)` outer path.  For that geometry, the four-boundary
segment exchange is therefore the smallest established off-diagonal move.

Formally, a four-boundary transfer followed by an inverse atomic transfer
has total signature

\[
                         (1,0)+(1,1)=(0,1),
\]

the signature of a pure endpoint transposition.  This is a quotient
calculation, not yet a physical two-move construction.  The atomic square
cross-pairs two path tails, while the four-boundary theorem is stated for
complementary input paths.  A new common-support or conjugation lemma is
needed to show that the second move remains available after the first.

## 6. The separate endpoint-boundary invariant

There is a stronger obstruction before endpoint ownership is considered.

### Theorem 6.1 (circuit alphabets cannot repair endpoint sets)

Any switch alphabet consisting only of alternating circuits preserves the
degree of every physical vertex.  Therefore it preserves the physical path
endpoint set.  Atomic squares, alpha switches, and four-boundary segment
exchanges all have this property.

Consequently no word in these moves can turn the published
Mütze--Weber endpoint set into a complement-invariant endpoint set.

### Proof

At every vertex of an alternating circuit, one factor edge is removed and
one nonfactor edge is inserted.  All degrees are unchanged.  Path endpoints
are exactly the degree-one vertices, so their set is unchanged.  The
Mütze--Weber endpoint set is not complement-invariant, as recorded in
`ALPHA_ENDPOINT_MONODROMY.md`.  \(\square\)

Thus a complete recursion needs an endpoint-moving signed `T`-join or open
alternating-trail move in addition to the local circuit alphabet.  Once such
a move has produced a complement-invariant endpoint set, Theorem 4.1 still
governs the residual pairing monodromy unless that endpoint-moving move also
breaks the parity lock.

## 7. Consequence for the Catalan neutralization proposal

Connectedness of the three-strand alpha support proves at most generation of
an alternating group.  Adding atomic squares does not automatically upgrade
this to a state-closed symmetric-group action at fixed tag ledger: every
ledger-neutral word remains even by Corollary 4.2.

Therefore a dynamically closed neutralization theorem must explicitly
supply at least one of:

1. a state-stable four-boundary/atomic composite realizing a neutral odd
   transposition;
2. a directly verified ledger-neutral odd switch, such as a dynamically
   usable even-support flipping tuple; or
3. an endpoint-moving trail whose residual action has off-diagonal signature.

It must additionally prove that these moves remain available after previous
overlapping switches and preserve targetwise one-tag colours, lower roots,
factor provenance, and pins.  Abstract connectedness and the Catalan moment
bound do not provide those properties.

The rigorous conclusion is therefore

\[
 \boxed{
 \text{atomic squares plus ordinary alpha switches are parity-locked and
 cannot supply connected ledger-neutral endpoint transpositions.}
 }
\]
