# The screened folded-C8 common cut has an exact cap-labelled address bijection

Date: 2026-08-01  
Lane: R, folded-C8 addressed occurrence / compiler boundary  
Status: unconditional finite address theorem for the explicit folded family
through `2<=d<=12`, and dimension-free abstract transport and screen-recycling
lemmas.  The result is exact on the unguarded one-core common-cap face.  It
does not manufacture an owner-legal host, a `q1` sidecar, or a protected
trace guard.

## 0. Verdict

The common-cut calculation can be lifted from signed values to literal
physical interval occurrences, with one essential qualification.

For the explicit screened old/new words, not only the counters

\[
                 (\text{width},\text{OR core})
\]

but the stronger counters

\[
        (\text{width},\text{OR core},\text{interval common cap})       \tag{0.1}
\]

agree exactly for every audited `2<=d<=12`.  Ordering the physical
`(start,end)` addresses lexicographically inside each fibre of (0.1) gives
an explicit bijection.  On the unguarded one-core compiler face, a cell with
core `C` and cap `P` has neighbourhood

\[
                         [C,P]=\{Q:C\subseteq Q\subseteq P\}.           \tag{0.2}
\]

The address bijection therefore is an isomorphism of the two literal local
compiler graphs.  It transports every packet matching and every packet
transversal-matroid basis.  If the background is fixed and compatible with
this same complete cap state, extending the bijection by the identity
transports the whole matching.

This does **not** follow from signed-value equality alone.  Address-specific
trace guards, forced `q1` occurrences, and cap-state compatibility must be
included in the fibre label or checked separately.

The common left screen also need not cost a new source position.  If the
actual immediate-left ambient letter already contains the screen, it masks
every left-crossing prefix discrepancy and can be used in place of the
prepended screen.  This has source charge `chi=0`.  For compiler use, any
target served by a crossing cell must still contain the whole actual ambient
letter, not merely the abstract screen.

## 1. Physical address fibres

Let

\[
                 W^\epsilon=(w^\epsilon_0,\ldots,w^\epsilon_{n-1}),
                 \qquad \epsilon\in\{0,1\},                         \tag{1.1}
\]

be two words of the same length.  Their physical interval-address set is

\[
                 \mathcal A_n=\{(i,j):0\le i\le j<n\}.              \tag{1.2}
\]

At `a=(i,j)` put

\[
 \ell(a)=j-i+1,\qquad
 C_\epsilon(a)=\bigcup_{p=i}^j w^\epsilon_p.                       \tag{1.3}
\]

Let `hat W=(hat w_0,...,hat w_(n-1))` be one actual pointwise common cap,
so `w^epsilon_p subseteq hat w_p`, and put

\[
                         P(a)=\bigcup_{p=i}^j\widehat w_p.            \tag{1.4}
\]

If there is an occurrence guard, let `g_epsilon(a)` be its complete guard
type: two cells have the same type exactly when they have the same allowed
target neighbourhood after all guard deletions.  On the unguarded face this
coordinate is omitted.

Define the enriched address key

\[
             k_\epsilon(a)=(\ell(a),C_\epsilon(a),P(a),g_\epsilon(a)).
                                                                         \tag{1.5}
\]

### Theorem 1.1 (canonical addressed-occurrence lifting)

There is a bijection `Phi:A_n->A_n` satisfying

\[
                         k_0(a)=k_1(\Phi(a))                           \tag{1.6}
\]

for every address `a` if and only if the two words have the same number of
addresses in every key fibre.

When the fibre counts agree, one canonical `Phi` is obtained by sorting the
addresses in each fibre lexicographically and pairing equal ranks.

#### Proof

Necessity follows by restricting any bijection satisfying (1.6) to one
fibre.  Conversely, equal finite fibre cardinalities allow a bijection in
each fibre; their disjoint union is the desired `Phi`.  Lexicographic
rank-pairing makes the choice explicit and deterministic.  \(\square\)

The theorem is elementary, but it supplies the occurrence data which a
signed counter forgets: every right-hand matching vertex is a literal
`(start,end)` address, and every such address occurs exactly once in `Phi`.

### Corollary 1.2 (exact local common-`Q` transport)

Fix one complete cap state.  Suppose a target `Q` is adjacent to an
occurrence `a` precisely when

\[
                 C_\epsilon(a)\subseteq Q\subseteq P(a)               \tag{1.7}
\]

and its guard type permits `Q`.  Then `id_Q x Phi` is an isomorphism between
the two occurrence-labelled target--cell graphs.  In particular it
transports every matching, every packet-independent target set, and the
entire packet transversal matroid.

If a background cell bank and all of its incidences are phase-common in the
same cap state, extend `Phi` by the identity on the background.  Every old
complete matching then transports to a new complete matching.  Equivalently,
the packet/background common-`Q` state is matching-closed.

#### Proof

Equation (1.6) preserves the core, cap and complete guard-deletion type, so
(1.7) holds for `(Q,a)` exactly when it holds for `(Q,Phi(a))`.  This is a
bipartite-graph isomorphism fixing the target shore.  Matchings and
transversal-matroid independent sets are invariant under graph isomorphism.
Adding a fixed disjoint background and extending by the identity proves the
last assertion.  \(\square\)

The existence of a common cap word is not by itself enough: if `Phi` sends an
address to one with a different interval cap, the Boolean intervals in
(1.7) can differ.  Nor may legal incidences from incompatible complete cap
states be unioned.

## 2. Application to the frozen common-cut pair

Use the canonical aligned folded source pair `S_0,S_1` and the opposite
two-host ray pair `G_1,G_0`.  In source--ray order put

\[
                     V_0=\rho_1(S_0G_1),\qquad
                     V_1=\rho_1(S_1G_0),                         \tag{2.1}
\]

where `rho_1` is the unique common cancelling cut.  Let either

\[
                  E=\{a_1,a_3\}
             \quad\text{or}\quad
                  E=\{z,a_1,a_3\},                              \tag{2.2}
\]

and define the screened words

\[
                         W_0=E V_0,\qquad W_1=E V_1.             \tag{2.3}
\]

At each position take the minimal pointwise common **containment-cap
candidate**

\[
                         \widehat w_p=w^0_p\cup w^1_p.           \tag{2.4}
\]

### Theorem 2.1 (exact finite cap-labelled address theorem)

For both choices in (2.2), and every `2<=d<=12`, the two words (2.3) have
identical counters of the triples

\[
                       (\ell(a),C_\epsilon(a),P(a)).             \tag{2.5}
\]

Consequently the canonical map of Theorem 1.1 is a literal bijection of all
`n(n+1)/2` physical interval addresses preserving width, actual OR value,
and interval containment cap.  If (2.4) is admitted by one legal complete
unguarded one-core cap state, Corollary 1.2 applies in that state.  The fibre
audit alone does not prove that (2.4) satisfies owner erosions, pins or other
global cap rows.

#### Proof

The equality and the bijection are checked directly from the explicit words:
enumerate all addresses, group them by (2.5), sort each group, and pair equal
ranks.  The replay checks equality of key sets and fibre cardinalities,
then checks each paired address against the original letters and the cap
word.  Finally it checks that both address projections of the resulting list
are all of `A_n`, without repetition.  This is exhaustive for the stated
finite range.  \(\square\)

This strengthens the earlier graded equality on exactly the datum used by
the unguarded common-`Q` graph after cap legality is supplied.  It remains a
finite theorem through depth twelve; no symbolic all-`d` cap-fibre identity
or complete-cap existence is claimed.

## 3. The ray shore and the antidiagonal semantic correction

The local two-host rail in phase `epsilon`, indexed from zero, is

\[
  G_\epsilon=(X_L,L_\epsilon,f_2,\ldots,f_{d-1},R_\epsilon,X_R),
                                                                  \tag{3.1}
\]

with positions `0,1,...,d,d+1`.  Thus, for `1<=j<d`, the literal ray
occurrences are

\[
\begin{array}{c|c}
\text{target}&\text{physical interval address in }G_\epsilon\\ \hline
P_\epsilon(j)&[1,j],\\
S_\epsilon(j+1)&[j+1,d].
\end{array}                                                     \tag{3.2}
\]

In particular

\[
\begin{array}{c|c}
P_0(j)&[1,j]\text{ in }G_0\\
S_1(j+1)&[j+1,d]\text{ in }G_1\\
P_1(j)&[1,j]\text{ in }G_1\\
S_0(j+1)&[j+1,d]\text{ in }G_0.
\end{array}                                                     \tag{3.3}
\]

Let `m=|S_epsilon|`.  After the source--ray concatenation, cut (2.1), and
screen insertion, these local addresses become

\[
                         [m+1,m+j],\qquad[m+j+1,m+d].            \tag{3.4}
\]

The two intervals in (3.2) are disjoint adjacent physical cells.  Their
union spans `[1,d]`, but that spanning interval contains both active labels
`a_1,a_3` and is not either one-label ray target.  Therefore an abstract
antidiagonal comparator edge such as

\[
                         (P_0(j),S_1(j+1))                       \tag{3.5}
\]

is a **paired two-cell ticket**, and in (3.5) its two entries even belong to
opposite phase words.  It is not one physical compiler cell of capacity one.
Likewise `(P_1(j),S_0(j+1))` is a cross-phase two-cell ticket.

This is a load-bearing semantic correction to the antitone birail theorem.
The scalar antitone pairing proves that the two marginal threshold profiles
have zero corner deficiency.  A physical use must additionally provide
either:

1. two disjoint cell banks in one complete endpoint state realizing the two
   coordinates of every selected ticket; or
2. a matching-closed phase transport, such as Corollary 1.2, together with
   a matching in one endpoint.

Treating (3.5) as a single right-hand matching vertex undercounts capacity by
a factor of two and mixes incompatible phase states.  The current address
bijection transports fixed endpoint matchings; it does not by itself realize
an arbitrary permutation of these paired tickets.

## 4. Zero-charge screen recycling

The following statement is dimension free.

### Theorem 4.1 (immediate-left screen recycling)

Let `U,V` have the same length.  Suppose:

1. their internal width-graded decks have a physical address bijection;
2. their suffix ORs agree pointwise by length; and
3. a set `E` satisfies

\[
             E\cup\operatorname{Pre}_t(U)
              =E\cup\operatorname{Pre}_t(V)\qquad(0\le t\le |U|).
                                                                  \tag{4.1}
\]

Let `H` be the actual final letter of a fixed left exterior word and assume
`E subseteq H`.  Then `H` itself replaces a freshly inserted copy of `E`:
for every fixed right exterior word, the two complete words have a literal
width-and-value preserving interval-address bijection.  No new source
position is used, so the packet length charge is

\[
                                  \chi=0.                       \tag{4.2}
\]

If, moreover, the internal bijection and the pointwise crossing
correspondence preserve interval cap and guard types, the conclusion lifts
to a compiler-graph isomorphism as in Corollary 1.2.

#### Proof

Partition intervals into five classes.  Intervals wholly in a fixed exterior
are fixed.  Internal intervals use the assumed bijection.  A left-crossing
interval contains `H`, hence contains `E`; (4.1) gives equality at the same
relative address.  A right-crossing interval is equal at the same relative
address by suffix equality.  An interval crossing both boundaries contains
`H` and all of `U` or `V`, so (4.1) with `t=|U|` applies.  These classes are
disjoint and exhaustive and preserve widths.  Because `H` was already in
the ambient word, no position was inserted.  Adding cap and guard equality
to the same classwise map proves the final sentence.  \(\square\)

Immediate adjacency is essential.  If a letter between `H` and the packet
does not contain `E`, an interval beginning after `H` may see an unscreened
prefix discrepancy.  More generally it suffices that every intervening
suffix met by such an interval contains `E`.

### Compiler caveat

Recycling is free in length, not automatically free in target incidence.
Every target assigned to a left-crossing cell must contain the whole actual
core contributed by `H`.  If `H` has an extra coordinate outside that target,
the address is not a provider even though the OR-language equality remains
true.  It is sufficient that the transported matching use only internal
packet cells and fixed background cells, or that every crossing assignment
passes this containment test.

## 5. What is and is not closed

Closed exactly:

1. a literal physical address bijection preserving `(width,core,cap)` for
   the explicit screened pair through `d=12`;
2. packet-local common-`Q` graph isomorphism on the unguarded one-core face;
3. transport of any already existing compatible packet/background matching;
4. the literal ray-address ledger (3.2)--(3.4); and
5. zero-charge reuse of an actual immediate-left screen under Theorem 4.1.

Still separate:

1. owner legality and Johnson adjacency of the clipped boundary rail;
2. the lost lower-`q1` cut colour and any upper sidecar occurrence;
3. address-specific residence, deadline, protected-witness or trace guards;
4. existence of the first complete matching if it is not supplied by the
   ray diagonal plus a compatible transported background matching;
5. compatibility between different complete cap states; and
6. regenerative return of the same background boundary signature.

For a `q1` sidecar to be included in this theorem, its occurrence label must
be added to the key (1.5), or a distinguished sidecar address must be fixed
by the transport.  Equality of OR cores alone does not preserve a palette
owner.

## 6. Replay and independent audit

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_r_folded_c8_address_bijection_and_screen_recycling_20260801.py \
  --write
```

The replay checks both screens and every `2<=d<=12`.  Besides the freshly
screened pair, it checks an ambient immediate-left letter strictly containing
the screen and a nontrivial fixed two-sided context.  For each case it
constructs and hashes the complete canonical address bijection and verifies
both projections, every width, every OR core and every interval common cap.

The proof audit independently checks the five interval classes in Theorem
4.1, the exact local indices (3.2), the global offset (3.4), and the
graph-isomorphism quantifiers in Corollary 1.2.  It rejects three stronger
but invalid implications: plain signed-value equality does not imply cap
transport; one antidiagonal comparator edge is not one physical cell; and
screen containment does not preserve target incidence when the ambient
letter overshoots the assigned target.
