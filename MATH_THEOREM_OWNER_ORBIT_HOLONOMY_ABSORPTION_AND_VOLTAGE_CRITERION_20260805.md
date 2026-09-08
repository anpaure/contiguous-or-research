# Owner-orbit absorption of packet holonomy: the exact voltage criterion

**Date:** 2026-08-05  
**Method:** finite groupoids and permutation factorizations; no computation  
**Status:** unconditional complete-state theorem.  A nonflat packet may close
after being transported through distinct owners, but only under the exact
voltage equation below.  The theorem supplies a one-copy lift whenever a
suitable owner Hamilton cycle and its literal transports already exist.  It
does not construct that Hamilton cycle, the packet copies, or their physical
resource packing.

## 0. Outcome

Let

\[
 v_0,v_1,\ldots,v_{W-1},v_W=v_0
\]

be a one-copy Hamilton cycle of named owners.  Let

\[
 E_i:\Omega_i\longrightarrow\Omega_{i+1}
\]

be the complete-state transport on its \(i\)-th owner transition, and let

\[
 S_i:\Omega_i\longrightarrow\Omega_i
\]

be the holonomy of the local packet inserted at owner \(v_i\).  All maps are
assumed to be total bijections of the complete continuation fibres.

Transport every local packet back to the initial fibre.  If

\[
 P_0=I,\qquad P_i=E_{i-1}\cdots E_0,\qquad
 \widehat S_i=P_i^{-1}S_iP_i,\qquad \gamma=P_W,
\]

then the complete one-tour holonomy is

\[
 \boxed{
 H=\gamma\widehat S_{W-1}\widehat S_{W-2}\cdots
                  \widehat S_0.}                    \tag{0.1}
\]

Consequently the owner tour absorbs the packet holonomies exactly when

\[
 \boxed{
 \widehat S_{W-1}\cdots\widehat S_0=\gamma^{-1}.}   \tag{0.2}
\]

In the coherent case

\[
                         S_i=P_i\sigma P_i^{-1},     \tag{0.3}
\]

equation (0.2) becomes

\[
                         \boxed{\gamma\sigma^W=I.}  \tag{0.4}
\]

Thus a flat owner cycle does not require the individual packet to be flat.
It requires only

\[
                         \operatorname{ord}(\sigma)\mid W. \tag{0.5}
\]

If the owner cycle has selectable continuation voltage, the required value
is instead

\[
                         \boxed{\gamma=\sigma^{-W}.} \tag{0.6}
\]

This is the precise positive escape from same-owner flatness.  It is also
the precise obstruction: vertexwise gauge conjugation alone cannot change
(0.1) from nonidentity to identity.

## 1. The owner-cycle product formula

### Theorem 1.1 (interleaved owner and packet holonomy)

With the notation above,

\[
 E_{W-1}S_{W-1}\cdots E_1S_1E_0S_0
 =P_W\widehat S_{W-1}\cdots\widehat S_0.            \tag{1.1}
\]

Hence the concatenated one-copy tour closes its complete continuation state
if and only if (0.2) holds.

#### Proof

By definition,

\[
                         E_i=P_{i+1}P_i^{-1}.
\]

Substitute this into the left side of (1.1), beginning at the last edge:

\[
\begin{aligned}
 E_{W-1}S_{W-1}\cdots E_0S_0
 &=P_W(P_{W-1}^{-1}S_{W-1}P_{W-1})\cdots
       (P_0^{-1}S_0P_0)\\
 &=P_W\widehat S_{W-1}\cdots\widehat S_0.
\end{aligned}
\]

Both sides map the initial fibre to itself because \(v_W=v_0\).  Identity
of this map is exactly (0.2). \(\square\)

The convention here is “local packet, then owner edge.”  Reversing that
convention merely shifts the conjugating prefixes; the resulting closed
product is conjugate and has the same identity criterion.

### Corollary 1.2 (coherent one-copy orbit lift)

Assume every local block consumes the owner \(v_i\) exactly once, preserves
its declared named payload, and has the coherent transport form (0.3).  If
(0.4) holds, concatenating the blocks along the owner Hamilton cycle is one
connected owner-once complete-state tour.  In particular, when the owner
edge transport is flat, (0.5) is sufficient.

#### Proof

Equation (0.3) gives \(\widehat S_i=\sigma\) for every \(i\), so Theorem
1.1 gives \(H=\gamma\sigma^W\).  Under (0.4) the state closes.  The owner
cycle is connected and visits every owner once; inserting a closed local
block at each visited owner does not change that owner order.  Rolewise
payload exactness is preserved by hypothesis. \(\square\)

This corollary is deliberately conditional on literal role blocks.  It does
not turn a type occurrence into a one-copy named owner occurrence.

### Corollary 1.3 (a closed type circuit may be spread across owners)

Let a closed age-type circuit have \(p\) literal transitions and endpoint
continuation permutation \(\sigma\), not necessarily the identity.  Suppose
\(p\mid W\), and suppose one can lay each copy of the circuit across \(p\)
consecutive *distinct* named owners, so that the \(b=W/p\) copies partition
the owner Hamilton cycle.

At the \(b\) block boundaries, factor the complete block map as a pure
block-to-block owner transport followed by a self-map of the continuation
fibre.  If the self-maps are coherent copies of \(\sigma\), and the product
of the pure block transports has voltage \(\gamma\), then the complete tour
closes if and only if

\[
                         \boxed{\gamma\sigma^b=I,
                         \qquad b=W/p.}               \tag{1.2}
\]

In particular, a flat block transport absorbs the nonzero type-circuit
holonomy whenever

\[
                         \operatorname{ord}(\sigma)\mid W/p. \tag{1.3}
\]

#### Proof

Contract each \(p\)-owner segment to one super-vertex.  The resulting cycle
has \(b\) super-vertices, its owner voltage is \(\gamma\), and its rooted
local maps are all \(\sigma\).  Theorem 1.1 applied to that cycle gives
\(H=\gamma\sigma^b\). \(\square\)

This is the literal one-copy use of the mechanism: the \(p\) transitions of
a type circuit are paid by \(p\) different owners, rather than by repeating
one owner until its labelled state returns.  Different circuit lengths
\(p_j\) may likewise be packed when \(\sum_jp_j=W\); the exact closure row is
then the ordered product of their rooted endpoint permutations, together
with the owner voltage.  What remains physical is to coinstantiate this
owner partition, the literal circuit copies, and their named-target
payloads.

### Theorem 1.4 (exact voltage of the positive-composition rotor)

Put \(n=d+1\).  In the core-free positive-composition rotor, or in the
positive mobile part of a rotor with a permanent current core, write the
ordered nonempty mobile blocks as

\[
                         (C_0,C_1,\ldots,C_{n-1}).
\]

The unique literal successor over the rotated type is

\[
 R(C_0,C_1,\ldots,C_{n-1})
   =(C_{n-1},C_0,\ldots,C_{n-2}).                    \tag{1.4}
\]

If the size composition has least cyclic period \(p\mid n\), then its
closed type circuit has \(p\) transitions, endpoint holonomy \(R^p\), and

\[
                         \operatorname{ord}(R^p)=n/p. \tag{1.5}
\]

Consequently, if \(W/p\) coherently transported copies of that circuit use
every owner once, their total packet holonomy is

\[
                         (R^p)^{W/p}=R^W.             \tag{1.6}
\]

It closes over flat owner transport if and only if

\[
                         \boxed{d+1\mid W.}           \tag{1.7}
\]

For arbitrary owner voltage the exact requirement is

\[
                         \boxed{\gamma=R^{-W}.}       \tag{1.8}
\]

#### Proof

At a positive-composition transition, every new age-\((i+1)\) block has the
same positive size as the old age-\(i\) block and is contained in it.
Therefore it equals that old block.  The new age-zero block is the remaining
old age-\((n-1)\) block, proving (1.4).  A type returns after \(p\) rotations,
so its labelled endpoint map is \(R^p\).  Since \(R\) has order \(n\) and
\(p\mid n\), (1.5) follows.  Equations (1.6)--(1.8) now follow from
Corollary 1.3. \(\square\)

Thus the forced-rotation necklace obstruction has an exact one-copy voltage:
it is the residue \(W\bmod(d+1)\), not an unspecified failure of integral
rounding.  Changing the cyclic type orbit does not change this residue.
To beat it one must use nonrotation transitions, reverse-oriented circuits,
or a physical owner transport whose action on the mobile-age fibre is
\(R^{-W}\).

### Theorem 1.5 (a short hub cycle kills the rotation residue)

Let

\[
 H=(r-d,1,\ldots,1)
\]

be the hub age composition, and identify a labelled hub state with the
ordered \(d\)-tuple

\[
                         (x_1,\ldots,x_d)
\]

of its singleton age-\(1,\ldots,d\) coordinates.  Its literal successor
digraph has the arcs

\[
 (x_1,\ldots,x_d)\longrightarrow
 (y,x_1,\ldots,x_{d-1})
 \quad\Longleftrightarrow\quad
 y\notin\{x_1,\ldots,x_d\}.                          \tag{1.9}
\]

For every integer

\[
                         d+1\le L\le r,               \tag{1.10}
\]

this digraph contains a simple directed cycle of length \(L\).

#### Proof

Choose \(L\) distinct owner coordinates
\(z_0,\ldots,z_{L-1}\), with indices read modulo \(L\), and use the states

\[
 X_t=(z_t,z_{t-1},\ldots,z_{t-d+1})
 \qquad(0\le t<L).
\]

Since \(L\ge d+1\), the new symbol \(z_{t+1}\) is absent from \(X_t\), so
\(X_t\to X_{t+1}\) is an arc of (1.9).  The states are distinct because
their first coordinates are distinct, and \(X_L=X_0\). \(\square\)

Put \(n=d+1\), and assume \(r\ge2d+1\).  If \(s=W\bmod n\), choose

\[
 L=
 \begin{cases}
 n,&s=0,\\
 n+s,&1\le s<n.
 \end{cases}                                         \tag{1.11}
\]

Then \(n\le L\le2n-1\le r\), and \(W-L\) is divisible by \(n\).  Therefore
one identity-holonomy hub circuit of length \(L\), together with
\(W-L\) coherently rotating transitions, has flat total age-state
holonomy.

The hub circuit uses no extra owner occurrences: it replaces \(L\) of the
\(W\) transitions.  It also has the same *rank* suffix profile at every
occurrence of \(H\).  Hence the residue obstruction of Theorem 1.4 can be
removed without owner voltage whenever an exact owner--payload table exposes
\(L\) hub roles whose named incidences admit the cycle (1.9).  The theorem
does not prove that last coloured embedding; it isolates it as a
size-\(O(d)\) functional rainbow subproblem rather than a global holonomy
problem.

## 2. Gauge conjugation versus physical voltage

Change the fibre identification at owner \(v_i\) by a bijection \(g_i\).
Then

\[
 E_i\mapsto g_{i+1}E_ig_i^{-1},\qquad
 S_i\mapsto g_iS_ig_i^{-1}.                         \tag{2.1}
\]

The complete product changes by

\[
                         H\mapsto g_0Hg_0^{-1}.      \tag{2.2}
\]

Therefore a vertex gauge only conjugates the closed holonomy.  It cannot
make a nonidentity \(H\) equal to the identity.  Absorption requires either
the arithmetic cancellation in (0.5), a genuinely nontrivial physical owner
voltage (0.6), or noncoherent local copies whose root-conjugated products
cancel.

Suppose all complete-state maps lie in a group \(G\), and the local packet
may be installed with any root-conjugate of one element \(\sigma\in G\).
Let

\[
                         {\cal C}(\sigma)
 =\{c\sigma c^{-1}:c\in G\}.                       \tag{2.3}
\]

### Theorem 2.1 (exact conjugacy-flexible voltage gate)

For a fixed owner-cycle voltage \(\gamma\), a group-level one-copy closure
using \(W\) conjugate copies of \(\sigma\) exists if and only if

\[
                         \boxed{
 \gamma^{-1}\in {\cal C}(\sigma)^W.}                \tag{2.4}
\]

Here the right side is the set of ordered products of \(W\) elements of the
conjugacy class.  In every abelian quotient \(A\) of \(G\), (2.4) forces

\[
                         \boxed{[\gamma]+W[\sigma]=0\quad\text{in }A.}
                                                               \tag{2.5}
\]

#### Proof

After root transport, the \(i\)-th local copy is one element of
\({\cal C}(\sigma)\).  Equation (0.2) is therefore exactly membership
(2.4).  Conversely, any factorization in (2.4), when its conjugate copies
are physically available at the corresponding owners, satisfies (0.2).
Conjugate elements have the same image in every abelian quotient, so
abelianizing (0.2) gives (2.5). \(\square\)

Condition (2.4) is an exact algebraic criterion, not a physical lifting
theorem.  If only a restricted set of conjugates is plantable at owner
\(v_i\), replace the common class in (2.4) by the ordered product of those
owner-specific allowed sets.

### Corollary 2.2 (even owner count cancels every permutation holonomy)

Let \(G=S_n\), let \(\gamma=I\), and assume every conjugate of
\(\sigma\in S_n\) is physically available at every owner.  If \(W\) is even,
then

\[
                         I\in{\cal C}(\sigma)^W.       \tag{2.6}
\]

#### Proof

Every permutation is conjugate to its inverse, since they have the same
cycle type.  Hence both \(\sigma\) and \(\sigma^{-1}\) lie in
\({\cal C}(\sigma)\).  Use \(W/2\) consecutive pairs
\(\sigma\sigma^{-1}\). \(\square\)

For the central owner count this disposes of the abstract group obstruction
in almost every dimension.

### Proposition 2.3 (parity of the central owner count)

For

\[
                         W={k\choose\lceil k/2\rceil},
\]

\(W\) is odd if and only if

\[
                         k=2^a-1                       \tag{2.7}
\]

for some \(a\ge1\).

#### Proof

By Lucas's theorem, \({k\choose r}\) is odd exactly when
\(r\mathbin{\&}(k-r)=0\).  If \(k=2m\), the two arguments are both \(m\),
so this fails for \(m>0\).  If \(k=2m+1\), they are \(m+1\) and \(m\).
Consecutive integers have disjoint binary support exactly when
\(m=2^{a-1}-1\), which is equivalent to (2.7). \(\square\)

Consequently, outside the odd Mersenne dimensions, Corollary 2.2 says that
*every* finite permutation holonomy is algebraically absorbable by a flat
owner cycle, provided inverse-conjugate packet copies are literally
plantable.  In a Mersenne dimension \(W\) is odd, and the sign quotient gives
the sharp first obstruction

\[
                         \operatorname{sgn}(\gamma)
                         \operatorname{sgn}(\sigma)=1. \tag{2.8}
\]

For example, an odd packet permutation cannot close over a flat owner cycle
in those dimensions.  A selectable odd owner voltage would remove that
particular obstruction.

### Proposition 2.4 (literal reversal realizes inverse holonomy)

Let

\[
                         A=(A_1,\ldots,A_\ell)
\]

be a literal packet word, and let

\[
                         A^{\rm rev}=(A_\ell,\ldots,A_1).
\]

Then:

1. \(A\) and \(A^{\rm rev}\) have exactly the same multiset of contiguous
   union values, at every width;
2. their coordinate-run and gap lengths agree after exchanging left and
   right boundary flags;
3. every Johnson owner path, lower palette, and upper palette carried by
   \(A\) is traversed in reverse by \(A^{\rm rev}\); and
4. if the packet transition is reversible and has complete-state map
   \(S\), then the reversed packet has map

\[
                         J S^{-1}J^{-1},               \tag{2.9}
\]

where \(J\) is the boundary-state reversal identification.

#### Proof

The interval \([i,j]\) of \(A\) corresponds to
\([\ell+1-j,\ell+1-i]\) of \(A^{\rm rev}\), with the same union.  This
proves the first assertion.  Reversal preserves every internal run and gap
length and swaps the two clipped boundary pieces, proving the second.
Adjacent intersections and unions are symmetric in their two arguments, so
the owner and immediate-palette claims follow.  Finally, begin the reversed
packet in the reversal of a forward terminal state.  It traverses the
reversible local transitions in inverse order and finishes in the reversal
of the corresponding forward initial state, which is exactly (2.9).
\(\square\)

Hence the even-\(W\) cancellation does not require a large menu of unrelated
packet designs.  It is enough that one literal packet and its reversal can be
installed with compatible boundary orientations, so that the adjacent owner
transports absorb \(J\) and root the two holonomies as
\(\sigma,\sigma^{-1}\).  Alternating those two orientations then gives flat
complete-state holonomy.  The remaining qualification is real: if the
global chronology fixes one boundary orientation and does not permit the
reversal identification \(J\), the algebraic inverse pair need not be
physically composable.

### Corollary 2.5 (holonomy defect localizes to one owner)

Under the compatible-orientation hypothesis of Proposition 2.4, \(W\)
copies can be rooted so that

\[
 \widehat S_{W-1}\cdots\widehat S_0
 =
 \begin{cases}
 I,&W\ \text{even},\\
 \sigma,&W\ \text{odd},
 \end{cases}                                           \tag{2.10}
\]

after choosing the unpaired odd copy to be last.

Thus reversal pairing reduces the complete-state closure equation to no
local packet at all when \(W\) is even, and to one exceptional local packet
when \(W\) is odd.  In particular, for the central owner layer, continuation
holonomy is a bounded exceptional-state problem confined to the Mersenne
dimensions \(k=2^a-1\); it is not an extensive \(W\)-packet defect.

This is only a defect-localization statement.  Closing the odd case still
requires owner voltage \(\gamma=\sigma^{-1}\), an exceptional flat packet,
or one bounded correction block with the required residual holonomy.
It applies as stated to one-owner packets.  If one closed rotor block
consumes \(p>1\) owners as in Corollary 1.3, the number to pair is
\(b=W/p\), not \(W\); the same localization holds with \(b\bmod2\), but
the Mersenne classification of \(W\)'s parity alone no longer decides it.

## 3. The transposition case is completely soluble

Let the reference fibre have \(n\ge2\) points, let \(G=S_n\), and suppose
the packet holonomy is a transposition.  Its conjugacy class is the set of
all transpositions.  For \(\pi\in S_n\), write \(c(\pi)\) for its number of
cycles, including fixed points.

### Theorem 3.1 (exact transposition absorption)

A fixed owner voltage \(\gamma\) can be cancelled by \(W\) conjugate
transposition packets if and only if

\[
 \boxed{
 W\ge n-c(\gamma)
 \quad\text{and}\quad
 W\equiv n-c(\gamma)\pmod2.}                        \tag{3.1}
\]

For a flat owner cycle this reduces simply to

\[
                         \boxed{W\text{ is even}.}   \tag{3.2}
\]

#### Proof

The minimum number of transpositions whose product is a permutation
\(\pi\) is \(n-c(\pi)\): splitting each nontrivial cycle gives a
factorization of that length, while multiplying by one transposition changes
the cycle count by exactly one, proving the lower bound.  Every
transposition factorization has parity congruent to \(n-c(\pi)\).  Conversely
one may enlarge a minimum factorization by two at a time by inserting
\(\tau\tau=I\).  Apply this characterization to
\(\pi=\gamma^{-1}\), noting that \(c(\gamma^{-1})=c(\gamma)\), and use
Theorem 2.1. \(\square\)

Thus varying the conjugate copy can be much more flexible than coherent
repetition.  But the parity row is unavoidable.  In \(S_n^{\rm ab}\cong
C_2\), it is exactly (2.5).

## 4. Quotient voltage and strict spirals

Let a cyclic group \(\langle\rho\rangle\) of order \(m\) act freely on the
owner set.  Suppose a quotient circuit visits each of the \(N=W/m\) owner
orbits once and has owner voltage \(\rho^v\).

### Theorem 4.1 (derived owner-cycle count)

The lifted quotient circuit has exactly

\[
                         \gcd(v,m)                  \tag{4.1}
\]

owner cycles.  It is one Hamilton cycle on all \(W\) owners exactly when

\[
                         \gcd(v,m)=1.                \tag{4.2}
\]

After this topological lift, its complete-state closure is still governed
by Theorem 1.1.  In particular, if the full lifted owner-edge transport is
flat and the owner-local blocks are coherent copies of \(\sigma\), the
additional and exact condition is

\[
                         \operatorname{ord}(\sigma)\mid W.   \tag{4.3}
\]

#### Proof

After one quotient lap, the phase in the cyclic owner orbit increases by
\(v\) modulo \(m\).  Addition by \(v\) on \(\mathbb Z_m\) has
\(\gcd(v,m)\) cycles, each of length \(m/\gcd(v,m)\).  Since the quotient
lap visits every owner orbit once, these are exactly the cycles of the
derived owner lift.  This proves (4.1)--(4.2).  Under (4.2) the derived lift
is a full Hamilton cycle of length \(W\), so Corollary 1.2 gives (4.3).
\(\square\)

Topology voltage and continuation voltage are therefore two separate rows:
coprime owner voltage joins the owner orbits, while (0.2) closes the enlarged
continuation state.

## 5. A single coordinate permutation cannot replace the quotient circuit

One might try to let one global coordinate permutation \(g\in S_k\) carry a
single owner through the complete central layer.  This fails for all
sufficiently large central layers, for a simple order reason.

### Proposition 5.1 (coordinate-orbit obstruction)

For \(k\ge6\) and \(r=\lceil k/2\rceil\), no cyclic group generated by one
coordinate permutation acts transitively on \({[k]\choose r}\).

#### Proof

If the cycle lengths of \(g\) are \(\ell_1,\ldots,\ell_t\), then

\[
 \operatorname{ord}(g)=\operatorname{lcm}(\ell_1,\ldots,\ell_t)
 \le\prod_i\ell_i\le3^{k/3}.                         \tag{5.1}
\]

The last inequality is the standard integer-partition product bound,
obtained by replacing every part at least five by \(3\) and its remainder,
and replacing three twos by two threes.  On the other hand,

\[
 {k\choose\lceil k/2\rceil}\ge {2^k\over k+1}>3^{k/3}
 \qquad(k\ge6).                                      \tag{5.2}
\]

The final inequality holds at \(k=6\), and its left-to-right ratio increases
thereafter.  Every orbit of \(\langle g\rangle\) has length at most
\(\operatorname{ord}(g)\), so it is shorter than the owner layer. \(\square\)

Thus the useful positive mechanism is not “let one permutation enumerate
all owners.”  It is a quotient circuit visiting many owner orbits, with a
coprime voltage joining its lift, followed by the independent continuation
voltage test (0.2).

## 6. Consequence for integral rotor fusion

The same-owner flatness target is stronger than necessary.  A proof may
instead build:

1. one owner-once Hamilton cycle, directly or by a coprime-voltage quotient
   lift;
2. one literal packet block at every owner, all with the same declared
   owner/target resources;
3. complete bijective owner-edge transports with voltage \(\gamma\); and
4. local packet holonomies satisfying (0.2).

On the coherent face the entire nonadditive continuation row is the single
group equation \(\gamma\sigma^W=I\).  On the conjugacy-flexible face it is
the product-class condition (2.4), with the abelian obstruction (2.5).

This does not solve the lower named-target or owner-Hamilton construction.
It does prove that nonidentity one-tour packet holonomy is not itself a
fatal obstruction: it can be amortized across distinct owners exactly when
the owner voltage equation permits it.  Conversely, a construction which
checks only additive current and owner connectivity but fails (2.5) cannot
be repaired by changing vertex gauges.
