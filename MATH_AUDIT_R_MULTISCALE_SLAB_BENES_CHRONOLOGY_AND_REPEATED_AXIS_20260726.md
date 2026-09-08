# Multiscale slab routing: exact chronology, repeated-axis, and holonomy audit

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or web
input is used.

## 0. Outcome

The abstract Beneš theorem does not lift formally to the certified
rank-twisted cross-parent slab.

There are two exact reasons.

1. A slab switch is a change of codimension-one foliation.  If the old
   packets are the two \(e\)-facets and the new packets are the two
   \(i\)-facets, every old packet meets every new packet in exactly half of
   its owners.  Thus the switch bisects packet-attached flag tables; it is
   not either permutation matrix on two indivisible wires.
2. Even when the four half-packet flag restrictions happen to glue, an
   isometric (C_{2R})-compiler imposes an **ordered port condition**, not
   just an endpoint or support condition.  Deleting the two occurrences of
   the removed direction from each doubled-permutation cycle produces two
   ordered geodesic paths.  The paths on opposite shores may be rejoined by
   the new direction if and only if their endpoint-swapped ordered words
   agree exactly.

A multistage route consequently has three independent closure requirements:

* active-axis legality at every step;
* perfect-matching and frozen-orientation closure; and
* trivial ordered-port holonomy on every transported compiler fragment.

Aggregate direction cancellation implies none of these.

There is also an exact collar count.  Opening one compiler direction exposes
exactly \(2q\) starts per \(C_{2R}\) cycle at signed depth \(q<R\).  For a
two-packet \(Q_{R+1}\) slab this is \(2q\,2^R/R\) starts per sign.  Summed over
both signs and \(q\le H\), one genuine \(i\mapsto e\) splice, under the
edge-preserving transport analyzed below, changes

\[
                 2{2^R\over R}H(H+1)                 \tag{0.1}
\]

owner-resolved flag entries, namely the normalized signed-depth
entry multiplicity per slab owner

\[
                         {H(H+1)\over R}              \tag{0.2}
\]

when multiplicity over signed depths is counted.  This normalized
multiplicity may exceed one.
For the CPCR regime

\[
 H=\sqrt m\,\omega(m),\qquad R=o(m),
\]

the ratio \(H^2/R\) tends to infinity.  Therefore a positive-owner-density
bank of owner-disjoint, one-splice monotone transports cannot carry a
preassigned balanced nested flag table with only (o(W)) entry changes.  A
successful multiscale construction
would have to use correlated axis reactivation and exact ordered-port
cancellation.  Freshly reinstalling a compiler after every slab avoids the
transport requirement, but then the construction is an atlas-option
selection and does not convert the given abstract nested flow.

This is a no-go for the proposed **literal flag-transport lift**.  It is not
a no-go for CPCR itself: a final state chosen with fresh compiler contexts
could still satisfy CPCR without preserving any preassigned intermediate
flag table.

## 1. One slab is a foliation switch

Write the abstract orientation bits of one physical slab as

\[
                         D\mathbin{\dot\cup}\{e\},
                 \qquad |D|=R,
\]

and fix \(i\in D\).  Its old and new packetizations are

\[
 P_\alpha=\{x_e=\alpha\},\qquad
 Q_\beta=\{x_i=\beta\},\qquad \alpha,\beta\in\{0,1\}.
                                                               \tag{1.1}
\]

Then

\[
 P_\alpha\cap Q_\beta
   =\{x_e=\alpha,x_i=\beta\}\cong Q_{R-1},
 \qquad |P_\alpha\cap Q_\beta|=2^{R-1}.             \tag{1.2}
\]

Hence the normalized owner-incidence matrix is

\[
                         {1\over2}
             \begin{pmatrix}1&1\\1&1\end{pmatrix}.             \tag{1.3}
\]

In particular, an ownerwise label which is constant with value (A) on
(P_0) and (B\ne A) on (P_1) is half (A), half (B) on each new
packet.  This proves that a physical slab is not an ideal straight/cross
switch on arbitrary indivisible packet bundles.

The following fixed-frame endpoint formula quantifies the same fact over
many coordinate-foliation changes.

### Theorem 1.1 (fixed-frame endpoint transfer)

Let (V=Q_n).  Let ({\cal P}_0) and ({\cal P}_1) be partitions of (V)
into coordinate (Q_R)'s obtained by freezing coordinate sets (K_0,K_1),
where

\[
                         |K_0|=|K_1|=n-R.
\]

Put

\[
 d=|K_0\setminus K_1|=|K_1\setminus K_0|.
\]

For cells

\[
 P_a=\{x:x|_{K_0}=a\},\qquad Q_b=\{x:x|_{K_1}=b\},
\]

one has

\[
 |P_a\cap Q_b|=
 \begin{cases}
  0,&a,b\text{ disagree on }K_0\cap K_1,\\
  2^{R-d},&a,b\text{ agree on }K_0\cap K_1.
 \end{cases}                                             \tag{1.4}
\]

Consequently every final cell receives equal (2^{-d})-fractions from
exactly (2^d) initial cells, and every initial cell is split equally among
exactly (2^d) final cells.  This depends only on the endpoint frozen sets,
not on the intervening sequence of foliation changes.

#### Proof

The combined restrictions fix exactly

\[
 |K_0\cup K_1|=(n-R)+d
\]

coordinates.  If the common restrictions disagree the intersection is
empty.  Otherwise the remaining number of free coordinates is

\[
 n-|K_0\cup K_1|=R-d,
\]

which proves (1.4).  For fixed (b), the (d) values on
(K_0\setminus K_1) index the (2^d) compatible initial cells; the reverse
statement is symmetric. \(\square\)

### Corollary 1.2 (fixed-frame indivisible-bundle no-go)

In the setting of Theorem 1.1, a final packet is the owner set of one whole
initial packet if and only if (d=0).  In that case (K_0=K_1) and the two
physical packet partitions are identical.  Thus coordinate-foliation
changes alone realize no nontrivial permutation of arbitrary
owner-attached packet bundles.

Theorem 1.1 also isolates the owner-fragment version of the exponential
fibre obstruction.  If an endpoint frame has replaced \(d\) independent
frozen coordinates, every final packet contains \(2^d\) equal old-packet
fragments.  In particular \(d\ge q\) gives at least \(2^q\) fragments.
Closing the endpoint frame removes this multiplicity only by taking
\(d=0\), when the physical packet partition has returned exactly.  This is
an owner-fragment statement, not by itself a lower bound on literal target
load.

The same purity statement does not require a fixed frame: if two partitions
have equal cell size and an output cell is label-pure for arbitrary labels
which are constant and distinct on the input cells, then that output cell
is contained in one input cell and hence equals it.  A moving frame can
therefore evade Corollary 1.2 only by opening the bundles and later gluing
their restrictions; it cannot turn a foliation change into an indivisible
wire switch.

## 2. Exact moving-frame state and repeated-axis law

The activated cross-parent pair is deliberately not an edge of the old
rank-(k) matching.  To iterate the construction while returning to the
standard rank-twisted packet class, the matching frame itself must be
updated.

Write the old perfect matching as a bijection

\[
                         \mu:A\longrightarrow C.
\]

Choose distinct (a,b\in A), put

\[
 f=\{a,\mu(a)\},\qquad g=\{b,\mu(b)\},
\]

and activate

\[
 e=\{a,\mu(b)\}.
\]

The complementary cross edge is

\[
 e^*=\{b,\mu(a)\}.
\]

### Lemma 2.1 (matching-frame update)

The unique perfect matching which keeps all old edges outside (f\cup g)
and contains (e) is

\[
 M'=M-\{f,g\}+\{e,e^*\}.                           \tag{2.1}
\]

Equivalently, its matching bijection is

\[
                         \mu'=\mu\circ(a\ b).       \tag{2.2}
\]

Thus every cross-parent slab contributes one transposition to the matching
frame holonomy.

#### Proof

After (a) is matched to (mu(b)), the only unmatched vertices among the
four affected coordinates are (b) and (mu(a)), so they must form
(e^*).  Formula (2.2) is immediate. \(\square\)

### Corollary 2.2 (one-step re-atlasing)

In the explicit slab construction, the two endpoints of \(e^*\) are both
frozen absent.  On each new packet, \(e\) is split and active, \(e^*\) has
status zero, the removed old active edge \(i\) has status one with a frozen
orientation, and all other statuses are unchanged.  Hence, relative to
\(M'\), each new packet is again an ordinary physical rank-twisted
\(Q_R\)-fibre.

Thus the geometric packet class is closed under one switch **provided**
the atlas is allowed to update its matching from \(M\) to \(M'\).  If the
certified atlas permits only a prescribed cyclic family of matchings, this
closure is not automatic: one must prove that the local transposition frame
is an admissible new atlas state.  In either case, successive switches must
track the transposition holonomy rather than continue to use the old
matching labels.

A packet strand through a sequence of slabs therefore has state

\[
                         (M_t,D_t,\zeta_t),          \tag{2.3}
\]

where (M_t) is its current matching frame, (D_t\subseteq M_t) is its
active (R)-set, and (zeta_t) is its frozen status/orientation word.  A
legal exchange has

\[
 D_{t+1}=D_t-\{i_t\}+\{e_t\},
 \qquad i_t\in D_t,quad e_t\notin D_t,             \tag{2.4}
\]

with (e_t) produced from two inactive edges of (M_t) as in Lemma 2.1.
In particular:

* an axis cannot be removed while inactive;
* an axis cannot be activated while active;
* every removed axis which belongs to the prescribed output frame must be
  reactivated later; and
* every transient activated axis absent from the output frame must later be
  removed.

For a closed frame route, the activation and removal counts of every
physical axis agree.  In addition, the product of the transpositions in
(2.2) must stabilize the prescribed output matching, and the transported
frozen word (zeta_t) must return to the prescribed orientation.  The
coarser vector identity

\[
                 \sum_t(e_{e_t}-e_{i_t})=0          \tag{2.5}
\]

does not imply either matching or orientation closure.  This is the first
pathwise holonomy obstruction.

The isolated cross-parent slab theorem proves one step of (2.4).  A
branchwise recursive network additionally needs the two inactive matching
edges with the required (10/01) statuses to exist after every preceding
switch choice.  No such all-branches availability theorem follows from
single-step reachability.

## 3. Cutting an isometric compiler at one direction

Let (F) be an exact factor of a physical (Q_R) into isometric
(C_{2R})'s, each canonically oriented.  The direction word of every cycle
is

\[
                         \pi\pi                    \tag{3.1}
\]

for a permutation (pi) of its (R) active directions.

Fix one active direction (i).  Its two occurrences on each cycle are
separated by (R) edges.  Delete all (i)-edges.  Every cycle splits into
two paths, one in each (i)-facet.  Each path:

* has (R) vertices and (R-1) edges;
* is geodesic;
* uses every direction in (D\setminus\{i\}) exactly once; and
* inherits an ordered direction word (w\) of length (R-1).

For one canonically oriented path write its directed ordered port record as

\[
                         (a,b;w),                  \tag{3.2}
\]

meaning that it runs from (a) to (b) with word (w).  If orientation is
forgotten, the underlying undirected path may be represented by either

\[
                         (a,b;w)\sim(b,a;w^{\rm rev}).           \tag{3.3}
\]

For transport of a prescribed canonically oriented flag table, however,
the two representatives in (3.3) are not interchangeable: reversing one
retained path changes all of its directed interior chronology.

Now let (F_0,F_1) be compiler factors on the old packets (P_0,P_1) of
(1.1).  Fix \(\beta\in\{0,1\}\), so that the prospective new packet (Q_\beta)
contains the (i=\beta) half of each old packet.

### Theorem 3.1 (directed ordered half-cube gluing criterion)

Keep all old edges in directions (D\setminus\{i\}) inside the two chosen
half-packets, delete the old (i)-edges, and permit only (e)-edges between
the halves.  These path factors glue to an exact canonically oriented
isometric (C_{2R})-factor while preserving every retained directed path
if and only if their actual directed path records admit a bijection such
that

\[
            (a,b;w)\quad\longleftrightarrow\quad
            (b+e,a+e;w).                           \tag{3.4}
\]

No independent use of the reversal equivalence (3.3) is permitted in this
directed statement.  The criterion must hold separately for
\(\beta=0,1\).

#### Proof

Suppose a path on the (e=0) shore runs (a\to b) with word (w).  The
only (e)-neighbour of (b) on the other shore is (b+e), and the only
vertex there which can return by an (e)-edge to (a) is (a+e).  Hence a
cycle using the retained path edges must have the form

\[
 a\mathrel{\xrightarrow{w}}b
 \mathrel{\xrightarrow{e}}b+e
 \mathrel{\xrightarrow{w'}}a+e
 \mathrel{\xrightarrow{e}}a.                       \tag{3.5}
\]

Its direction word is (w,e,w',e).  An isometric (C_{2R}) direction
word is periodic with period (R), so necessarily and sufficiently
(w'=w).  This is exactly (3.4).

If all directed records pair in this way, (3.5) gives disjoint cycles covering every
path and hence every owner of (Q_\beta).  Each cycle has word
((w,e)(w,e)), so it is isometric.  Conversely every retained-edge
isometric gluing must use the unique (e)-edges at the two path endpoints,
and period (R) forces (3.4). \(\square\)

Endpoint equality alone is therefore insufficient.  Support equality is
also insufficient.  The complete directed ordered word is part of the
compiler port.  If only undirected factorhood is sought, one may weaken the
test by choosing an orientation of each proposed new cycle.  That weaker
test does not transport the prescribed canonical flag table and does not
justify the collar identity in Section 4.

### Corollary 3.2 (compiler-conjugation holonomy)

At every valid slab splice, (3.4) induces a bijection of ordered path
records.  Along a sequence of splices, a transported fragment is acted on
by the composition of these bijections.  If the active set, matching frame,
and frozen word return to their initial values, verbatim transport of the
initial owner-resolved compiler bundle still requires the composite port
bijection to be the identity, up to one globally allowed compiler
automorphism which fixes the requested literal flag table.

A nonidentity composite is ordered chronology holonomy.  It can remain
nontrivial even when (2.5) vanishes and the matching transposition product
is the identity.

Fresh compiler reinstallation proves neither (3.4) nor triviality of this
holonomy.  It constructs a legal new factor, but it discards the proposed
transported flag table.

There is, however, one exact matched-context solution of the local gluing
condition.

Let \(\tau_i\) denote translation of an old \(Q_R\)-packet by its
orientation bit \(i\), and let \(\tau_e:P_0\to P_1\) be translation across
the slab bit \(e\).

### Theorem 3.3 (twisted-twin compiler splice)

Let \(F_0\) be any canonically oriented isometric \(C_{2R}\)-factor on
\(P_0\), and install on \(P_1\) the affine-conjugate factor

\[
                         F_1=\tau_e\tau_iF_0.        \tag{3.6}
\]

Then the ordered gluing condition (3.4) holds simultaneously for
\(\beta=0,1\).  Keeping all \(D\setminus\{i\}\)-edges and replacing the
\(i\)-seams by \(e\)-seams therefore gives exact isometric
\(C_{2R}\)-factors on both new packets.  Their cycle words are obtained
from those of \(F_0\) by replacing \(i\) with \(e\), up to cyclic phase.
In particular they are physical affine/context conjugates of the same
abstract compiler and retain its within-packet trace injectivity.

#### Proof

Take a path record \((a,b;w)\) in the \(i=\beta\) facet of \(F_0\).
Because the parent cycle has doubled word \(\pi\pi\), its other \(i\)-facet
contains the companion path

\[
                         (b+i,a+i;w).               \tag{3.7}
\]

Translation by \(i\) moves (3.7) back into the \(i=\beta\) facet and gives
\((b,a;w)\).  Translation by \(e\) then gives the record
\((b+e,a+e;w)\) in \(P_1\), exactly as required by (3.4).  This works for
both values of \(\beta\) and pairs every path.

The glued cycle has word \(w,e,w,e\).  The old cycle, phased immediately
after an \(i\)-edge, has word \(w,i,w,i\).  Thus the new factor is the
same abstract doubled-permutation compiler after the axis substitution
\(i\mapsto e\).  Physical affine conjugation preserves literal trace
injectivity. \(\square\)

### Proposition 3.4 (the twisted relation survives the shore change)

Let \(G_0,G_1\) be the two new packet factors constructed in Theorem 3.3,
indexed by their frozen value of \(i\).  Then

\[
                         G_1=\tau_i\tau_eG_0.        \tag{3.8}
\]

Here \(\tau_e\) toggles the now-active orientation bit \(e\), while
\(\tau_i\) moves between the two frozen \(i\)-facets.  Thus both shores of
the exact slab trade carry the same twisted-twin context relation.

#### Proof

A cycle of \(G_0\) consists of an \(i=0\) path of \(F_0\), an \(e\)-edge,
the matched \(i=0\) path of \(\tau_e\tau_iF_0\), and the second \(e\)-edge.
Applying \(\tau_i\tau_e\) swaps the two \(e\)-halves and sends these paths
respectively to the \(i=1\) companion paths used in the corresponding
cycle of \(G_1\).  It preserves their ordered words and the canonical
cycle orientation.  Hence it sends the whole factor \(G_0\) to \(G_1\).
\(\square\)

### Corollary 3.5 (context cocycle for a fixed switch graph)

Suppose a fixed graph of packet slots is to support twisted-twin splices.
Orient every switch edge \(a=vw\), and let

\[
                         \theta_a=\tau_{e_a}\tau_{i_a}           \tag{3.9}
\]

be its required context transition, transported into one common frame.
Compiler contexts \(h_vF\) satisfying

\[
                         h_wF=\theta_a h_vF          \tag{3.10}
\]

on every switch edge exist if and only if the ordered product of the
\(\theta_a\)'s around every graph cycle lies in the stabilizer of \(F\).
For pure commuting orientation translations and a compiler with trivial
translation stabilizer, this reduces to

\[
                         \bigoplus_{a\in C}(e_a+i_a)=0            \tag{3.11}
\]

for every cycle \(C\).

#### Proof

Necessity follows by composing (3.9) around a cycle.  For sufficiency,
choose one context in each connected component and define every other
context by multiplying transitions along a path from the root.  The cycle
condition makes this path-independent. \(\square\)

In a moving matching frame, the transitions in (3.9) must first be
conjugated into a common coordinate frame.  They need not commute, and the
ordered cycle product, not merely the xor (3.11), is the relevant
holonomy.  Theorem 3.3 closes one literal switch; Corollary 3.5 shows
exactly what a recursive bank must additionally solve.

## 4. Exact collar and repeated-cut count

The doubled-permutation chronology gives an exact count of the entries
which a splice must expose.

### Lemma 4.1 (one-direction collar)

On one oriented (C_{2R}), for \(1\le q<R\), exactly \(2q\) directed
(q)-windows contain the fixed direction (i).

#### Proof

There are two occurrences of (i), separated by (R) edges.  Exactly
(q) directed starts have a given occurrence in their next (q) edges.
The two start sets are disjoint because their two edge occurrences have
cyclic separation \(R\) and \(q<R\). \(\square\)

Put (s=2^R) and (g_R=s/R).  The old shore of a (Q_{R+1}) slab has
two (Q_R)-packets and hence

\[
                         {2s\over2R}=g_R             \tag{4.1}
\]

compiler cycles.  Lemma 4.1 gives exactly

\[
                         2qg_R                      \tag{4.2}
\]

old starts per sign whose (q)-window crosses an (i)-seam.  The new
shore has the same number crossing an (e)-seam.

For the genuine rank-twisted exchange, (i) and (e) are distinct
coordinate-disjoint physical axes.  Under the **directed** retained-edge
transport of Theorem 3.1, every old window counted by (4.2) changes its
literal target:
the old lower target varies (i) and keeps one frozen endpoint of (e),
whereas the new lower target varies (e) and keeps one frozen endpoint of
(i); the upper statement is analogous.  Hence the number of changed
owner-resolved entries of a transported prescribed flag table, summed over
both signs and all \(q\le H<R\), is exactly

\[
 2\sum_{q=1}^H2qg_R
   =2g_RH(H+1).                                    \tag{4.3}
\]

Since the slab has (2s=2Rg_R) owners, (4.3) divided by owner mass is the
normalized signed-depth entry multiplicity

\[
                         {H(H+1)\over R}.            \tag{4.4}
\]

The corresponding union of old and new collars is at most twice (4.3).
Without directed compatibility, a reversal of one retained path can alter
\(\Theta(R)\) successor arcs, and (4.3) is not a valid total-change count.

There is a useful multicut form.  On one cycle let (S) be a nonempty set
of (k) distinct directions whose seam edges are opened.  In one copy of
the permutation word, let

\[
                         g_1,\ldots,g_k\ge0,
 \qquad                 \sum_jg_j=R-k               \tag{4.5}
\]

be the cyclic gaps of unopened directions between consecutive members of
(S).

### Lemma 4.2 (exact multicut survival count)

The number of directed (q)-windows on the full (C_{2R}) which avoid all
opened seams is exactly

\[
                         2\sum_{j=1}^k(g_j-q+1)_+.   \tag{4.6}
\]

In particular it is at most

\[
                         2(R-k-q+1)_+,              \tag{4.7}
\]

so at least

\[
                         2\min\{R,k+q-1\}           \tag{4.8}
\]

starts have their (q)-chronology exposed.

#### Proof

A window avoids the cuts precisely when all its (q) consecutive letters
lie inside one unopened gap.  A gap of length (g_j) contains
((g_j-q+1)_+) such starts.  The word has two identical copies, proving
(4.6).

For (q\ge1), the function (x\mapsto(x-q+1)_+) is superadditive in the
sense

\[
 (a-q+1)_+ +(b-q+1)_+\le(a+b-q+1)_+.
\]

Iterating and using (4.5) proves (4.7), and subtraction from (2R) gives
(4.8). \(\square\)

Formula (4.8) is an exposure count.  It becomes a literal mismatch lower
bound when the opened directions are replaced monotonically by distinct
new axes and are not later restored.  In a nonmonotone moving-frame route,
reactivation may cancel a seam; then the exact ordered-port holonomy of
Corollary 3.2, rather than the number of historical cuts, decides whether
the final flag returns.

## 5. Consequence in the CPCR scale

Suppose a positive fraction (eta W) of owners is subjected to one
monotone rank-twisted (i\mapsto e) splice and the purpose is to transport
a previously prescribed balanced owner-resolved nested flag table.  By
(4.3)--(4.4), the transported table differs in

\[
                 \eta W,{H(H+1)\over R}            \tag{5.1}
\]

signed-depth entries.

In the authoritative CPCR regime,

\[
 H=\sqrt m\,\omega(m),\qquad \omega(m)\to\infty,
 \qquad R=o(m),
\]

and therefore

\[
                         {H^2\over R}
  ={m\over R}\omega(m)^2\longrightarrow\infty.     \tag{5.2}
\]

Thus (5.1) is not (o(W)) for any fixed (eta>0).  A standard recursive
router which monotonically opens new switch axes cannot be used as an
(o(W))-error transport of an already balanced common all-depth flow.

This does not say that every changed flag creates floor energy: a globally
correlated final reassembly could land on a different balanced table.  It
does say that the abstract balanced table cannot be treated as immutable
traffic and then carried through the literal slab network with a negligible
collar budget.

The only two possible escapes are therefore:

1. **Exact correlated return.** Reactivate axes and choose ordered port
   bijections so that matching, orientation, and compiler holonomy all
   close, while the final nontrivial home assignment survives.
2. **Fresh final selection.** Discard intermediate flags, install fresh
   legal compiler contexts on the final packets, and prove CPCR directly
   for that final legal state.

The first is an unproved nonlocal gluing theorem.  The second is precisely
CPCR and gains nothing merely from the Beneš diagram.

## 6. Exact sufficient conditions for a literal recursive lift

A recursive slab network does give a literal owner-exact approximate flag
router if all of the following are proved.

1. **Branchwise availability.** At each stage and under every preceding
   setting used by the route, the two packets are opposite facets of a
   legal rank-preserving (Q_{R+1}) slab; slabs in one stage are
   owner-disjoint.
2. **State legality.** Every path satisfies (2.4), every matching update is
   (2.1), and the terminal matching, active set, and frozen orientation are
   the prescribed ones.
3. **Ordered gluing.** Both (i)-facets at every active switch satisfy
   Theorem 3.1 for one common choice through all depths and both signs.
4. **Port holonomy.** The composite ordered-port bijection on every routed
   fragment realizes the prescribed output compiler bundle.
5. **Collar ledger.** The literal entries exposed by the final effective
   seams, counted by Lemma 4.2, either equal their prescribed output entries
   or have aggregate discrepancy (o(W)).

Under Conditions 1--4, induction over the stages gives an exact middle-owner
factor at every stage and a legal isometric compiler factor at the end.
Condition 5 gives the declared common all-depth approximation.  This is a
sufficient theorem, not a construction.  Theorem 3.3 supplies Condition 3
for one twisted-twin local context.  The isolated slab reachability theorem
does not supply Condition 1, a branchwise global assignment of those
contexts satisfying Condition 4, or Condition 5.

## 7. Audited boundary

Proved here:

* the exact fixed-frame endpoint transfer formula (1.4);
* the indivisible-bundle no-go;
* the exact matching transposition associated with one cross-parent frame
  update;
* the pathwise active-axis and frame-holonomy requirements;
* the necessary and sufficient ordered half-cube compiler-gluing criterion;
* the explicit twisted-twin local compiler splice and its context-cocycle
  criterion;
* the exact one-direction and multicut collar counts; and
* the positive-density monotone transport obstruction in the CPCR scale.

Not proved:

* a branchwise dense recursive bank of compatible rank-twisted slabs;
* a global moving-frame assignment of twisted-twin contexts on such a bank;
* a nontrivial closed port-holonomy family realizing prescribed homes;
* a final correlated reassembly whose collar changes form another balanced
  table; or
* CPCR.

Therefore the ordinary Beneš analogy is exhausted at the literal
chronology level.  Abstract rearrangeability is positive, but a physical
slab is a half-packet foliation switch.  The remaining positive object is
not a binary packet switch network; it is a correlated ordered-port
reassembly with exact matching and compiler holonomy.
