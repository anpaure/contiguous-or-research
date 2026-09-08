# A protected common-exterior C8 odd socket and the collapse of the forward selector

**Date:** 2026-08-03  
**Status:** unconditional owner/immediate-palette theorem.  It constructs a
prospectively plantable odd actuator compatible with any fixed small
pivot-incidence bank, and gives exact normal forms for the residual
colour--tail--head selector.  It does not prove that an upper-exact global
completion containing the socket exists, nor does it carry residence,
deeper interval witnesses, or the lower compiler.

## 0. Outcome

Two separate issues should no longer be conflated.

1. The parity bit can be prepared explicitly.  Four private incidence
   hexagons support one common-exterior star `C8`.  Its off phase consists
   of four saturated factor cycles; toggling the octagon merges them into
   one.  The predecessor matching is fixed, the successor matching changes
   by a `4`-cycle, and the complete immediate-upper multiplicity vector is
   merely permuted.  This socket coexists with a fixed depth-`d` pivot bank
   whenever the combined protected incidence count is at most `m-2`.
2. The remaining forward colour--tail--head gate is not a matroid/flow
   problem plus that parity bit.  With no order fixed it is exactly a
   three-partite perfect matching followed by subtour elimination.  Once a
   strict forward order is fixed, the endpoint rows force the unique chain
   of consecutive vertices, so there is no residual matching choice at all.

Thus the odd actuator is available at the abstract q1 layer.  The genuine
open problem is still a correlated upper-surjective Hamilton ordering.

Throughout, put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

\[
 W=|\mathcal L|=|\mathcal O|,qquad
 U=|\mathcal U|,qquad C=W-U=\operatorname {Cat}_m.    \tag{0.1}
\]

## 1. No C4, so C8 is the first odd circuit

Let

\[
 G=ML(2m-1)
\]

be the incidence graph between ranks `m-1` and `m`.

### Lemma 1.1 (Boolean anti-rectangle)

The graph `G` contains no simple `C4`.

#### Proof

Two distinct rank-`(m-1)` sets have at most one common rank-`m` superset.
If their union has rank `m`, that union is the unique common neighbour; if
their union has larger rank, there is none.  A `C4` would give two common
neighbours.  \(\square\)

An alternating `C_(2s)` matching toggle composes the factor permutation by
an `s`-cycle and changes component parity by `s-1`.  A `C6` has even
endpoint action.  Lemma 1.1 excludes the only smaller odd action, so a
`C8` is the first possible simple incidence-circuit parity actuator.

## 2. The private common-exterior socket

Assume `m>=6`.  Choose

* a set `S` of rank `m-2`;
* distinct petals `a_0,a_1,a_2,a_3` outside `S`;
* a further exterior point `e`; and
* distinct points `z_0,z_1,z_2,z_3` in `S`.

Indices are cyclic modulo four.  Put

\[
 \begin{aligned}
 C_i&=S+a_i,\\
 T_i&=S+a_i+a_{i+1},\\
 R_i&=S+a_i+e,\\
 B_i&=S+a_i+a_{i+1}+e,\\
 Q_i&=B_i-z_i,\\
 A_i&=(S-z_i)+a_i+a_{i+1},\\
 D_i&=(S-z_i)+a_i+e.
 \end{aligned}                                                \tag{2.1}
\]

Here `C_i,A_i,D_i` have rank `m-1`, while `T_i,R_i,Q_i` have
rank `m`; `B_i` has rank `m+1`.

### Lemma 2.1 (four private off cycles)

For each `i`,

\[
 T_i-C_i-R_i-D_i-Q_i-A_i-T_i                         \tag{2.2}
\]

is a simple incidence `C6`.  The four cycles in (2.2) are pairwise
vertex-disjoint.

#### Proof

Every consecutive containment follows directly from (2.1).  The six
vertices in one row are distinct: the three lower vertices have respective
`S`-intersections `S`, `S-z_i`, `S-z_i` and different exterior parts, and
the same argument applies to the owners.

Across different indices, the `S`-intersection of every auxiliary vertex
records the distinct missing point `z_i`; the unpunctured vertices are
distinguished by their petal sets.  A punctured vertex cannot equal an
unpunctured one because it omits `z_i in S` and replaces it by an exterior
point.  Hence all four cycles are disjoint.  \(\square\)

Let `Z` be their `24`-edge union.  At the four lower vertices `C_i`, call

\[
                         C_iT_i                         \tag{2.3}
\]

the old octagon phase.  The opposite phase is

\[
                         C_iT_{i-1}.                    \tag{2.4}
\]

### Theorem 2.2 (zero-q1-defect odd socket)

The toggle (2.3) to (2.4):

1. replaces the four components (2.2) by one component;
2. preserves every lower and owner degree;
3. fixes one predecessor perfect matching `M_0` and changes only the other
   matching `M_1`;
4. preserves the complete immediate-upper multiplicity vector.

#### Proof

Deleting \(C_iT_i\) opens the \(i\)-th private cycle into the path

\[
 C_i-R_i-D_i-Q_i-A_i-T_i.
\]

The new edge \(C_iT_{i-1}\) joins the \(C_i\)-end of this path to the
\(T_{i-1}\)-end of the preceding path.  Since \(i\mapsto i-1\) is one
four-cycle, the four opened paths close into one cycle, not two or four.

Alternately colour each private `C6` so that `C_iR_i` lies in `M_0` and
`C_iT_i` lies in `M_1`.  The four new incidences rematch exactly the same
four lower vertices to the same four owners `T_i`, so `M_1` remains a
perfect matching and `M_0` is unchanged.

Explicitly, on the `i`-th off cycle,

\[
\begin{aligned}
 M_0&:\quad C_iR_i,\ D_iQ_i,\ A_iT_i,\\
 M_1&:\quad C_iT_i,\ R_iD_i,\ Q_iA_i.
\end{aligned}                                             \tag{2.4a}
\]

The on phase replaces only the first displayed `M_1`-edge by
`C_iT_{i-1}`.  The new `M_1`-edges are again a bijection between the four
`C_i`'s and the four `T_i`'s.

The old upper value at `C_i` is

\[
        R_i\cup T_i=S+e+a_i+a_{i+1},                  \tag{2.5}
\]

whereas the new value is

\[
        R_i\cup T_{i-1}=S+e+a_{i-1}+a_i.              \tag{2.6}
\]

The latter is the old value with index `i-1`.  Thus the four values are
permuted.  Every lower vertex other than the four `C_i`'s keeps both of
its matching neighbours, so every other immediate-upper turn is literally
unchanged.  \(\square\)

In particular, the off/on states differ in component count by three and
therefore supply exactly one controllable parity bit without changing the
colour, tail, or head resources.

The socket has an exact constant upper-nullity charge.  At its other two
lower vertices,

\[
 R_i\cup Q_i=B_i,
 \qquad Q_i\cup T_i=B_i,                               \tag{2.7}
\]

and (2.5) is also `B_i`.  Thus the twelve socket turns use the four
distinct colours `B_0,...,B_3`, each with multiplicity three.  Their repeat
excess is exactly

\[
                              12-4=8.                  \tag{2.8}
\]

After the toggle the colour at `C_i` becomes `B_(i-1)`, so the same
`3,3,3,3` multiplicity vector remains.  Any upper-surjective global factor
containing this saturated socket therefore needs Catalan duplicate budget
`C>=8`.  An upper-surjective Hamilton **path** retaining all twelve turns
has total duplicate budget `C-1` and therefore needs `C>=9`.  Both are
automatic in the planting range `m>=6`.

### Corollary 2.3 (both signs in one exact resource fibre)

Relative to the fixed `M_0`, the old and new successor matchings have
opposite permutation signs, but identical tail, head, and upper-colour
multisets.  Hence any completion of the off state by a disjoint exterior
matching is also a completion of the on state with exactly the same three
resource marginals and the opposite topology parity.

Thus there is no intrinsic index-two/parity obstruction in a prospective
Boolean colour--tail--head fibre which contains this socket.

### Proposition 2.4 (sharp saturated-private size)

The `24`-edge support is minimum among constructions which force the four
old octagon incidences to lie in four distinct components by placing each
inside a vertex-disjoint saturated protected cycle.

#### Proof

The Boolean incidence graph is bipartite and has no `C4` by Lemma 1.1, so
its girth is at least six.  Each of four disjoint saturated components must
therefore contain at least six edges.  Lemma 2.1 attains the resulting lower
bound `4*6=24`.  \(\square\)

## 3. Coexistence with a protected pivot bank

Let `P` be a 2-bounded protected incidence bank in `G`, with `p` edges.
Write `b_-` and `b_0` for its numbers of occupied lower and owner vertices,
and put

\[
                         W={2m-1\choose m-1}.
\]

### Lemma 3.1 (private placement)

If

\[
                         12(b_-+b_0)<W,                \tag{3.1}
\]

some relabelled copy of the socket `Z` is vertex-disjoint from `P`.

#### Proof

Apply a uniformly random permutation of the ground coordinates to one
fixed socket.  Each of its twelve lower vertices is uniform on the lower
shore and each of its twelve owner vertices is uniform on the owner shore;
both shores have size `W`.  The union bound makes the probability of any
collision at most `12(b_-+b_0)/W`, which is less than one.  \(\square\)

### Theorem 3.2 (protected odd-socket planting)

Assume (3.1) and

\[
                         p+24\le m-2.                  \tag{3.2}
\]

Then there is a spanning two-factor containing `P` and the complete off
socket `Z`.  The four private cycles remain separate components, and the
toggle of Theorem 2.2 gives another spanning two-factor containing `P`,
with identical immediate palettes and component count smaller by three.

#### Proof

Choose the disjoint socket by Lemma 3.1.  The union `P union Z` is
2-bounded and has at most `m-2` edges.  Apply the protected Middle-Levels
two-factor extension theorem.  Every socket vertex already has protected
degree two, so no completion edge can leave one of its four cycles; they
remain four distinct factor components.  Theorem 2.2 now applies and does
not touch `P`.  \(\square\)

For `H` protected depth-`d` pivot collars, the concrete sufficient bound is

\[
                         6Hd+24\le m-2.                \tag{3.3}
\]

Together with (3.1), this holds for every fixed `H` and
`d=Theta(sqrt(m))` once `m` is sufficiently large.  Phase-labelled pivot
rails must still satisfy their ordinary component parity pins.  For the
fixed-predecessor interpretation of Theorem 2.2, the four socket cycles
must be phased **coherently** so that all four old edges `C_iT_i` belong
to the same matching.  Before the predecessor is named there are two
global coherent choices, obtained by swapping `M_0,M_1` on all four cycles
simultaneously.  Once a particular predecessor is fixed, only the coherent
choice putting all `C_iT_i` in the successor matching realizes Theorem 2.2;
the four phases are not independent.

Theorem 3.2 closes the **abstract odd-actuator availability** row.  It does
not say that the arbitrary two-factor completion is upper-surjective.
Rather, it says that whenever an upper-surjective completion containing
this prepared socket is obtained, either socket phase is upper-surjective
with exactly the same multiplicities.

## 4. Exact three-partite normal form of the residual selector

Fix a predecessor matching `M_0`, an allowed rooted occurrence ground `E`,
and distinct desired source and terminal vertices `s,t`.  Use `M_0` to
identify the owner shore with \(\mathcal L\), so an allowed occurrence is a
labelled arc `e:x->y` on \(\mathcal L\), with immediate-upper colour

\[
                         u(e)=M_0(x)\cup M_0(y)\in\mathcal U.
                                                               \tag{4.0a}
\]

Put

\[
 T={\cal L}-\{t\},\qquad H={\cal L}-\{s\},
 \qquad |T|=|H|=W-1.
\]

Let `D` be a dummy set of size `C-1=W-1-|mathcal U|`, and put

\[
                         K=\mathcal U\mathbin{\dot\cup}D.       \tag{4.0}
\]

Construct a three-partite occurrence-labelled three-uniform multihypergraph
on `T,H,K`.  For every allowed occurrence `e:x->y`, include

\[
                         (x,y,u(e);e)                  \tag{4.1}
\]

and, for every dummy `d in D`, include the occurrence-labelled copy

\[
                         (x,y,d;e).                    \tag{4.2}
\]

The entry after the semicolon is an edge label, not a fourth hypergraph
vertex.  It prevents distinct literal occurrences with identical resource
triples from being silently identified.

On the **full unrooted shores**, before deleting the terminal tail, source
head, or any protected/structural occurrence, the real-colour part has an
exact biregular fractional point.  Every tail has `m-1` nonbase incidences,
every head has `m-1` incoming nonbase incidences, and every upper colour has
exactly `m+1` occurrences.  For the last assertion, index the occurrences
of `R in mathcal U` by its middle facets `V`: put

\[
 L=M_0^{-1}(V),\qquad a=V-L,qquad V'=R-a.
\]

Then `L` is the tail, `y=M_0^{-1}(V')` is the head, and `L->y` is the
unique colour-`R` occurrence indexed by `V`.
Consequently, assigning weight `1/(m+1)` to every real occurrence gives

\[
 \sum_{e:u(e)=R}x_e=1,\qquad
 \sum_{e:t(e)=L}x_e=\sum_{e:h(e)=L}x_e
     ={m-1\over m+1}={U\over W}.                      \tag{4.2a}
\]

Thus all upper colours are fractionally saturated and the total unused
tail/head mass on each full shore is exactly `W-U=C`.  This removes the
unprotected real-colour rank-count separator.  It does **not** by itself
fill the dummy connector slots, give a fractional perfect matching after
the rooted endpoint deletions, or survive arbitrary protected structural
zeros; those restrictions can destroy biregularity and remain part of
Theorem 4.1's actual selector.

There is nevertheless an exact fractional completion on the **full
unrooted cycle selector**.  In that version take a dummy set `D_cyc` of
size `C` rather than `C-1`, and include a dummy-labelled copy `(x,y,d;e)`
of every nonbase occurrence for every `d in D_cyc`.

### Proposition 4.0 (exact fractional cycle selector)

The complete unprotected, unrooted three-partite cycle-selector
hypergraph has a fractional perfect matching.

#### Proof

Give every real-colour occurrence weight `1/(m+1)`.  Equation (4.2a)
saturates every real upper colour and gives load

\[
                         {U\over W}={m-1\over m+1}
                                                               \tag{4.2b}
\]

at every tail and head.  For each dummy `d`, give every one of the
`W(m-1)` occurrence-labelled dummy copies weight

\[
                         {1\over W(m-1)}.              \tag{4.2c}
\]

This gives load one at `d` and load `1/W` at each tail and head.  Summing
over the `C` dummies contributes `C/W` to every endpoint.  Since
`U+C=W`, the total endpoint load is

\[
                         {U\over W}+{C\over W}=1.
\]

Thus all three shores are saturated exactly. \(\square\)

This proposition is deliberately scoped to the full unrooted cycle
selector.  A rooted Hamilton path deletes one tail and one head and has
only `C-1` dummy slots; protected incidences introduce further structural
zeros.  Nor does a fractional perfect matching impose any subtour cut.

### Theorem 4.1 (colour--tail--head matching equivalence)

There is a set of `W-1` allowed occurrences with distinct tails, distinct
heads, and complete upper-colour support if and only if the hypergraph
(4.1)--(4.2) has a perfect matching.

#### Proof

Given the occurrence set, assign one occurrence of each real upper colour
to its real slot and biject the remaining `C-1` occurrences with the dummy
slots.  Endpoint injectivity makes the resulting triples disjoint.

Conversely, every real slot in a hypergraph perfect matching is covered by
an occurrence of that colour, while the dummy triples merely absorb the
extra occurrences.  The tail and head shores enforce their two endpoint
capacities.  \(\square\)

Thus the unfixed-order selector is exactly a three-dimensional matching,
or an intersection of three partition systems—not ordinary bipartite flow
or two-matroid intersection.  Contracting protected occurrences just
contracts forced triples after designating which protected repetitions use
dummy slots.

The selected arcs form one `s`-to-`t` path together with directed cycles.
Hamiltonicity is the additional subtour family

\[
      x(\delta^+(X))\ge1
      \qquad(\varnothing\ne X\subseteq\mathcal L-\{t\}). 
                                                               \tag{4.3}
\]

The prepared C8 toggles the parity of the number of these components, but
one parity bit cannot replace (4.3): a cover with three cycle components
has the same component parity as a one-cycle cover.

There is already a minimal abstract integrality obstruction even when the
tail--head support is `C4`-free.  Take tails `x_0,x_1,x_2`, heads
`y_0,y_1,y_2`, and colours `A,B,C`, with triples

\[
 \begin{array}{lll}
 (x_0,y_0,A),&(x_1,y_1,A),&(x_2,y_2,B),\\
 (x_0,y_1,B),&(x_1,y_2,C),&(x_2,y_0,C).
 \end{array}                                                \tag{4.4}
\]

The tail--head graph is one simple `C6`.  Weighting all six triples by
`1/2` saturates every tail, head, and colour exactly once.  Its only two
tail--head perfect matchings are the two displayed rows; the first repeats
`A` and misses `C`, while the second repeats `C` and misses `A`.  Thus the
integer colour--tail--head system is empty although its natural fractional
point is perfect.

This example is an abstract `C4`-free structural-zero warning, not a claim
that these six colour labels occur on one Boolean socket.  It proves that
anti-rectangular tail--head geometry and one parity bit alone cannot yield
integrality; a positive theorem must use the stronger Boolean colour
identities or a prepared absorber such as Section 2.

## 5. A fixed forward order leaves no matching choice

Let

\[
                         v_1<_{\phi}v_2<_{\phi}\cdots
                              <_{\phi}v_W                 \tag{5.1}
\]

be a strict total order, and retain only forward arcs.

### Theorem 5.1 (forward-order rigidity)

If a forward arc set `Q` has `W-1` distinct tails and `W-1` distinct heads,
then necessarily

\[
                         Q=\{v_i\to v_{i+1}:1\le i<W\}.  \tag{5.2}
\]

Consequently such `Q` exists exactly when every consecutive arc in (5.2)
is allowed, and it is upper-surjective exactly when the colours of those
consecutive arcs cover `mathcal U`.  If source `s` and terminal `t` are
prescribed, necessarily `v_1=s` and `v_W=t`.

#### Proof

The maximum vertex cannot be a forward tail, and the minimum vertex cannot
be a forward head.  Since only one tail and one head are omitted, these are
the omitted endpoints.  The head `v_2` can be supplied only by `v_1`, so
`v_1->v_2` is forced.  Delete those used endpoint copies and repeat: the
only still-unused possible tail for head `v_(i+1)` is `v_i`.  Induction
gives (5.2).  \(\square\)

### Corollary 5.2 (exact forward-route reformulation)

For fixed `M_0` and a protected bank `P` of rooted occurrence arcs, the
following are equivalent.

1. Some order `phi` extending `P` admits a forward set satisfying all
   colour, tail, and head rows **and containing every arc of `P`**.
2. The rooted occurrence graph has an upper-surjective directed Hamilton
   path containing every edge of `P`.

The order is uniquely the vertex order of that path.  In particular, every
protected path in `P` must occur as a contiguous block, not merely as a
comparable suborder.

This corrects the tempting interpretation of the forward atlas as a large
post-order matching menu.  Every upper colour may have a forward occurrence
while the unique consecutive chain misses it.  For example, on
`v_1<v_2<v_3`, arcs

\[
 v_1\to v_2\ (B),\qquad v_2\to v_3\ (B),\qquad
 v_1\to v_3\ (A)                                      \tag{5.3}
\]

make both colours available, but the only endpoint-complete forward path
has colour sequence `B,B`.

## 6. Exact remaining gate

At the owner/immediate-upper layer, the new division is proof-safe.

* A fixed small protected bank plus one odd common-exterior socket embeds
  in a spanning two-factor unconditionally under (3.1)--(3.2).
* The socket gives two q1-identical phases whose component counts differ by
  three.  Therefore Catalan parity is not an intrinsic obstruction once the
  host is chosen prospectively.
* The residual one-copy construction is the perfect matching of Theorem 4.1
  plus all subtour cuts (4.3), or equivalently the upper-surjective
  Hamilton ordering of Corollary 5.2.

What remains is not one matroid/flow theorem plus a parity bit.  It is one
correlated three-resource selector with connectivity.  Tractable faces
remain the known ones: private tails or heads reduce Theorem 4.1 to Hall;
fixing an upper-exact forest reduces the connectors to free-port Hall; and
fixing the Hamilton order makes colour coverage a deterministic audit.
