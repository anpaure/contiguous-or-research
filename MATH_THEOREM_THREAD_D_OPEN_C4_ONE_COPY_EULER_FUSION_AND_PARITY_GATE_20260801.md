# Open Johnson-square reversals preserve the three palettes but cannot by themselves fuse one-copy Euler components

Date: 2026-08-01  
Lane: Thread D, post-TPC one-copy coloured-Euler rounding  
Status: exact literal resource ledger, exact state-boundary and parity
obstruction, exact cycle-factor boundary rigidity, an exact conditional
TU orientation theorem for a prospectively planted bank, and integration
of the exact all-depth reset--return complete-reversal packet.  The latter
closes every *internal cyclic* derivative and compiler-incidence row.  No
global planting, fixed-exterior cross-window, common-residual compiler, or
regeneration conclusion is made.

## 0. Outcome

Let `K` have rank `r-2` and let `x,y,z,w` be distinct and outside `K`.
Put

\[
\begin{aligned}
 V_0&=K+x+z,&V_1&=K+x+y,\\
 V_2&=K+y+w,&V_3&=K+z+w.
\end{aligned}                                                   \tag{0.1}
\]

The two open-square phases

\[
 P^+:V_1\to V_2\to V_3\to V_0,
 \qquad
 P^-:V_0\to V_3\to V_2\to V_1                         \tag{0.2}
\]

use exactly the same four middle owners and exactly the same three named
lower and upper edge colours.  They are therefore a valid reversible
**payload** pair.

They are not a zero-boundary Euler switch.  With
`partial(a->b)=e_b-e_a`,

\[
 \partial P^+=e_{V_0}-e_{V_1},\qquad
 \partial P^-=e_{V_1}-e_{V_0},\qquad
 \partial(P^--P^+)=2(e_{V_1}-e_{V_0}).                 \tag{0.3}
\]

Thus one reversal destroys state balance by two units at each endpoint;
modulo two it changes nothing.  A collection of reversals is balanced
exactly when its endpoint incidences form an integral circulation.  In
particular, pairwise owner-disjoint open squares have distinct endpoints
and admit no nonempty balanced reversal.

There is a stronger topology obstruction.  Reversal leaves the undirected
support of every square unchanged, so it cannot merge weak Euler
components.  If the square is completed to a legal block reversal inside a
directed owner cycle factor, exact preservation of the two boundary lower
and upper palettes forces the predecessor and successor outside the block
to be the same owner.  The move then merely reverses one closed component.
The completed local successor change is even, so every composition of such
blocks preserves the parity of the number of permutation cycles.  In
particular it cannot perform a two-components-to-one fusion.

A positive theorem survives only prospectively.  If many
occurrence-disjoint square packets are planted as unoriented macroedges,
their phase choice is an ordinary prescribed-orientation `b`-matching and
is totally unimodular.  Connectivity is determined by the undirected
packet bank and is independent of phase.  For a circuit over a balanced
backbone the literal endpoint multigraph must have even degree at every
state.  This requires endpoint reuse or another boundary actuator, and in
the one-copy owner setting that is exactly where the closed-doubleton gate
reappears.

Replacing the short square by the exact `4d+2`-root reset--return cycle
does close the all-depth payload side: the two phases are literal reversals
with identical cyclic derivative and compiler-incidence inventories.  It
does not change the Euler verdict.  The two phases still have identical
undirected support and differ by an even whole-cycle reversal, so internal
DM rank and component topology are invariant.  Only an external
support-changing portal can turn this stronger packet into a fusion move.

For an existential same-parity induction, simultaneous **global** reversal
is a gauge, not a local move.  One constructs a complete oriented child
(including its witnesses and compiler) and reflects the whole certificate
if the other representative is desired.  Hence no fixed-address
`G^+ cap G^-` compiler intersection is required unless a genuinely local
phase switch against a frozen exterior is part of the theorem.  Global
reversal still cannot change component count, target holes, or cut debt.

## 1. Exact owner, lower and upper ledger

For a Johnson edge `AB`, write

\[
                 \ell(AB)=A\cap B,\qquad u(AB)=A\cup B.    \tag{1.1}
\]

The four square edges have the following labels:

\[
\begin{array}{c|c|c}
\text{edge}&\ell&u\\ \hline
V_0V_1&K+x&K+x+y+z\\
V_1V_2&K+y&K+x+y+w\\
V_2V_3&K+w&K+y+z+w\\
V_3V_0&K+z&K+x+z+w.
\end{array}                                                   \tag{1.2}
\]

All four lower labels and all four upper labels are distinct.  Both phases
in (0.2) omit the first row and use the other three rows, once each.  They
also visit the same owner set

\[
                         \{V_0,V_1,V_2,V_3\}.             \tag{1.3}
\]

Consequently the phase difference is zero on every named owner, lower and
upper occurrence row.  This is an occurrence statement, not merely a
point-degree cancellation.  Equation (0.3) follows by telescoping the
three directed arcs.

For every state cut `X`, (0.3) gives

\[
 \langle {\bf1}_X,\partial(P^--P^+)\rangle
       =2({\bf1}_{V_1\in X}-{\bf1}_{V_0\in X}).          \tag{1.4}
\]

Hence every modulo-two state-cut character is invariant.  Open-square
reversals cannot repair the odd-state obstruction in the even-`k`
private-clock examples of the one-copy TPC theorem.

## 2. Exact balance criterion for several reversals

Let a balanced selected support contain pairwise edge-disjoint paths
`P_j^+:s_j->t_j` of the form (0.2), and replace the paths indexed by
`J` by their reverses.  Every payload row remains fixed.  The new support
is balanced if and only if

\[
                   \sum_{j\in J}(e_{t_j}-e_{s_j})=0.       \tag{2.1}
\]

Indeed the total boundary change is `-2` times the left side.  Thus the
chosen old-oriented macroedges form an integral directed circulation on
their literal endpoints.

If every endpoint is used by at most one packet, (2.1) forces `J` to be
empty: the coefficient at an endpoint of any chosen packet is `+1` or
`-1` and cannot cancel.  This applies in particular when packet supports
are disjoint in the rank-`r` owner palette, because every endpoint in
(0.2) is itself one of the four packet owners.

More generally, reversal changes no undirected edge.  Therefore

\[
 \operatorname{comp}_{\rm weak}(F)
  =\operatorname{comp}_{\rm weak}(F\triangle
       \{P_j^+,P_j^-:j\in J\})                         \tag{2.2}
\]

whenever the right side denotes literal replacement of orientations on
the same paths.  Balance may be repaired by a cyclic family of endpoint
currents, but weak components cannot be fused in this way.

### Theorem 2.2 (whole-cycle reversal theorem)

Let `F` be a directed one-factor: every vertex has indegree and outdegree
one, so its underlying undirected graph is a disjoint union of cycles.
Reverse any batch `S` of its arcs, without changing their unordered
endpoints.  The result is again a directed one-factor if and only if, on
each component of `F`, the batch contains either no arc or every arc.
Consequently every legal batch merely reverses a set of whole directed
cycles.  The number of components and the multiset of their lengths are
invariant.

#### Proof

On one underlying cycle, encode an arc by `+` when it retains the original
cyclic orientation and by `-` when it is reversed.  At a vertex incident
with consecutive cycle edges, indegree and outdegree are both one exactly
when the two signs agree.  Hence all signs on the connected cycle are
equal.  The all-`+` and all-`-` orientations are plainly valid.  Applying
this independently to every component proves the theorem.

For a bank of edge-disjoint open-square paths already contained in `F`, a
balanced phase flip must therefore tile every edge of each affected cycle;
otherwise it is impossible.  Even when such a tiling exists, it only
reverses those cycles.  This strengthens the endpoint-circulation condition
(2.1) on the one-factor face: (2.1) is necessary for a general Euler
multigraph, while Theorem 2.2 is the exact degree-one condition.

## 3. Completing one square inside a directed owner factor

Suppose a directed owner cycle factor contains the consecutive block

\[
       p\to V_1\to V_2\to V_3\to V_0\to q.              \tag{3.1}
\]

After reversing its four middle owners, the only degree-one completion
which leaves all other successors fixed is

\[
       p\to V_0\to V_3\to V_2\to V_1\to q.              \tag{3.2}
\]

Thus both `p` and `q` must be common Johnson neighbours of `V_0,V_1`.
Put

\[
                         L=K+x,\qquad U=K+x+y+z.          \tag{3.3}
\]

Every loopless common neighbour is exactly one of the following two
types:

\[
 \text{bottom: }B_a=L+a\quad(a\notin U),
 \qquad
 \text{top: }T_a=U-a\quad(a\in L).                       \tag{3.4}
\]

For a bottom neighbour,

\[
 \ell(B_aV_0)=\ell(B_aV_1)=L,\qquad
 u(B_aV_0)=L+a+z,\qquad u(B_aV_1)=L+a+y,               \tag{3.5}
\]

whereas for a top neighbour,

\[
 u(T_aV_0)=u(T_aV_1)=U,\qquad
 \ell(T_aV_0)=L-a+z,\qquad \ell(T_aV_1)=L-a+y.        \tag{3.6}
\]

### Theorem 3.1 (boundary-palette rigidity)

Assume all four boundary edges in (3.1)--(3.2) are loopless Johnson edges.
The replacement preserves separately the complete two-edge lower palette
and the complete two-edge upper palette if and only if

\[
                                  p=q.                    \tag{3.7}
\]

#### Proof

If `p=B_a,q=B_b`, the lower palette is automatic and the signed upper
change is

\[
 [L+a+z]-[L+a+y]+[L+b+y]-[L+b+z],                       \tag{3.8}
\]

which vanishes exactly when `a=b`.  If `p=T_a,q=T_b`, the upper palette is
automatic and the signed lower change is

\[
 [L-a+z]-[L-a+y]+[L-b+y]-[L-b+z],                       \tag{3.9}
\]

which again vanishes exactly when `a=b`.  In a mixed top/bottom pair, one
shore has one nonzero primitive difference and the other shore has another,
so neither can vanish.  The displayed masks are distinct because
`y,z` are distinct and the bottom and top parameters lie respectively
outside `U` and inside `L`.  This proves necessity.  If `p=q`, the two old
boundary edges are simply the two new boundary edges with their
orientations reversed, proving sufficiency.

When (3.7) holds, (3.1) is the directed five-cycle

\[
             p,V_1,V_2,V_3,V_0,p,                         \tag{3.10}
\]

and (3.2) is its reverse.  Thus exact local palette preservation gives no
component fusion.

There is also a topology-only parity obstruction.  On the five affected
tails `(p,V_1,V_2,V_3,V_0)`, the new head list is obtained from the old
head list by the permutation

\[
                         (4,5,1,2,3),                      \tag{3.11}
\]

which has six inversions and is even.  Hence the successor permutation has
unchanged sign.  Since a permutation on `N` owners with `c` cycles has sign
`(-1)^(N-c)`, any composition of completed open-square reversals preserves
`c mod 2`.  It cannot merge exactly two components into one.  This parity
statement remains valid for interacting completed blocks even when the
stronger fixed-undirected-support conclusion (2.2) no longer applies.

## 4. The exact positive face: orient a planted square bank

The preceding no-go concerns reversal of support already selected in a
one-copy factor.  There is a different, prospective use of the packet.

Let `G_0` be a fixed directed support with boundary `beta`.  Plant a bank
of occurrence- and payload-disjoint open-square packets.  Packet `j` has
literal endpoints `{s_j,t_j}` and offers either directed phase, with the
same complete owner/lower/upper/pin payload in both phases.  Its internal
vertices are private.  Let `H` be the undirected endpoint multigraph with
one edge `s_jt_j` per packet.  Let `h` be the boundary which the packet
bank must contribute, so that `beta+h` is the prescribed final circuit or
open-trail boundary.

Put

\[
                 a(v)={d_H(v)+h(v)\over2}.                 \tag{4.1}
\]

Here `a(v)` is the required number of packets oriented with head `v`, using
the convention `partial=e_head-e_tail`.

### Theorem 4.1 (square-bank orientation/Hall theorem)

There is an integral phase choice with boundary `h` if and only if every
`a(v)` is an integer and, for every endpoint set `X`,

\[
        |E_H(X)|\le \sum_{v\in X}a(v)
             \le |E_H(X)|+|\delta_H(X)|.                  \tag{4.2}
\]

Every such choice preserves all named packet payloads.  The selected
support is weakly connected if and only if the orientation-independent
undirected union of `G_0` and all packet paths is weakly connected.

#### Proof

Assign each packet edge to its chosen head.  It must be assigned to one of
its two endpoints, and vertex `v` must receive exactly `a(v)` assignments.
This is a bipartite `b`-matching from packet edges to endpoint vertices.
The compressed Hall inequalities are exactly (4.2), so they are necessary
and sufficient and the system is totally unimodular.  Phase-independent
payload equality was proved in Section 1.  Reorienting a path changes no
undirected edge, proving the final assertion.

For a circuit over a balanced backbone, `h=0`.  Theorem 4.1 reduces to the
condition that every literal endpoint degree in `H` is even; the cut rows
then hold automatically.  If the packet paths connect `c>1` old
components, their component quotient is a connected Eulerian multigraph
and hence uses at least `c` packet edges (two parallel edges when `c=2`).
For one final open trail, exactly the prescribed source and sink may have
odd endpoint degree, and a quotient path can attain `c-1` packets.

These quotient bounds are weaker than the literal endpoint rows.  In a
strict one-copy owner-disjoint bank, `d_H(v)<=1`, so the circuit condition
forces `H` to be empty.  Achieving degree two requires repeated interface
states supplied by distinct owner fibres, an owner-changing role converter,
or one larger overlapping atomic circuit.  Naively sharing the same
physical port between reflected packets is precisely the closed-doubleton
owner repetition in the Boolean q-gon theorem.

## 5. Exact surviving gate

The open support-four square is useful as a payload-transparent reversible
macroedge, but it is not a component switch of the kind

\[
       u\to v,\ x\to y\quad\longmapsto\quad
       u\to y,\ x\to v.                                  \tag{5.1}
\]

The latter changes undirected support and can merge two Euler components;
the square reversal does neither.  Moreover a genuine two-component merge
is an odd head transposition, while a completed square reversal is even.

Therefore one of the following additional objects is necessary:

1. a payload-transparent cross rectangle as in (5.1);
2. a jointly planted endpoint-Eulerian bank satisfying (4.2), with a
   literal one-copy realization of repeated interface states; or
3. a larger overlapping circuit which cancels the boundary Pluecker
   currents (3.8)--(3.9), changes undirected support, and is audited as one
   atomic owner selector rather than as simultaneous square copies.

The theorem settles only owner/immediate-lower/immediate-upper payload,
state balance, weak-component topology, and successor parity.  It does not
assert residence, deeper suffix rows, arbitrary-width upper coverage,
voltage, protected comparator chronology, or compiler feasibility.

## 6. The resident long-return rail: full reversal versus the Boolean-hex actuator

This section audits
`MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md` against
the one-copy Euler conclusions above.  It is essential to distinguish two
operations which use the same long rail.

### 6.1 Full reversal of the reset--return cycle is fixed-support

Let

\[
 \mathcal S:E=W_0\to W_1\to\cdots\to W_a=F            \tag{6.1}
\]

be any simple reset path, and let

\[
 \mathcal R:F=W_a\to W_{a+1}\to\cdots\to W_{n}=E     \tag{6.2}
\]

be a simple return path, internally disjoint from `S`.  Their union `C` is
one directed cycle.  Its full reversal is

\[
 C^{\rm rev}:E=W_n\to W_{n-1}\to\cdots\to W_0=E.       \tag{6.3}
\]

For edge `i`, put

\[
       L_i=W_i\cap W_{i+1},\qquad U_i=W_i\cup W_{i+1}. \tag{6.4}
\]

Then `C` and `C^rev` use exactly the same middle-owner occurrence set and
the same named lower and upper occurrence multisets

\[
                    \{L_i:0\le i<n\},\qquad
                    \{U_i:0\le i<n\}.                 \tag{6.5}
\]

Both have zero boundary, and they have identical undirected support.
Therefore full reversal merely replaces one cyclic successor permutation
by its inverse.  It preserves that component and its length.  Reversing any
batch of such cycles is exactly the whole-cycle operation in Theorem 2.2;
it cannot fuse Euler components.

The parity conclusion is equally exact.  An `n`-cycle and its inverse both
have sign `(-1)^(n-1)`, so their relative successor permutation is even.
Thus full long-cycle reversals preserve both the exact component inventory
and, a fortiori, component-count parity.

There is useful portal motion but no matching-rank gain.  If the `U_i` are
distinct, the head--upper attachment matchings are

\[
       M^+=\{U_iW_{i+1}^+:0\le i<n\},\qquad
       M^-=\{U_iW_i^+:0\le i<n\};                      \tag{6.6}
\]

their symmetric difference is one alternating cycle.  The two predecessor
matchings

\[
 \{W_i^-W_{i+1}^+\}_i,
 \qquad
 \{W_{i+1}^-W_i^+\}_i                                \tag{6.7}
\]

have `gcd(n,2)` alternating components, since their relative permutation
is the shift by two.  For the resident rail closed by its seam,
`n=2d+2`, so (6.7) has exactly two alternating cycles.  Opening the common
seam turns (6.6) into one attachment portal path and (6.7) into the two
signed predecessor portal paths.

Equations (6.6)--(6.7) are basis exchanges inside already saturated local
matching components.  They change which occurrence is attached to which
head, but do not augment matching cardinality or remove a Dulmage--Mendelsohn
deficiency by themselves.  After forced-edge contraction they may expose
useful portal endpoints; whether those endpoints reach a deficient shore is
an additional residual Hall statement.

For the literal rolling-reset construction these conclusions combine with
the stronger theorem
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`.
Let the depth be `d`, open the `2d+2`-root reset at
`E=T_0,F=T_(2d+1)`, choose the rail exchanges in the permanent reset core,
and choose the inserted rail coordinates outside the complete reset
support.  Under

\[
                         r\ge 2d+2,\qquad k-r\ge2d+1,       \tag{6.8a}
\]

the reset path and return rail form a simple cycle on

\[
                              M=4d+2                       \tag{6.8b}
\]

owners with globally simple lower and upper palettes.  Its nonconstant
positive-run lengths are `d+1`, `2d+1`, or `3d+1`.  Its maximal depth-`d`
antecedent is nonempty, and the antecedent in the opposite phase is its
literal reversal up to cyclic shift.  Consequently complete reversal
preserves, by a literal incidence isomorphism,

* every derivative-row inventory;
* every cyclic root interval-OR width;
* every cyclic antecedent interval-OR width; and
* the complete target--cell incidence graph for cells wholly internal to
  the closed packet.

Thus residence, internal upper transport, and internal compiler transport
are **not** remaining gates for this augmented packet.  They remain open
for the bare support-four path and for support-changing toggles which are
not the complete reversal.

### 6.2 The literal Boolean-hex toggle is support-changing

Now specialize to the long-collar theorem.  Its boundary atoms are

\[
 O=\{A\to B,C\to D,E\to F\},\qquad
 N=\{A\to F,C\to B,E\to D\},                         \tag{6.8}
\]

and the same directed return rail `R_d:F->...->E` is selected in both
phases.  Thus

\[
 G_d^-=O\cup E(R_d),\qquad G_d^+=N\cup E(R_d).         \tag{6.9}
\]

This is **not** the full reversal of the cycle `EF union R_d`.  The rail is
held fixed while the three boundary atoms undergo the alternating switch

\[
 A^- -B^+ -C^- -D^+ -E^- -F^+ -A^- .                 \tag{6.10}
\]

Both matchings in (6.8) saturate the same tail set `{A,C,E}` and the same
head set `{B,D,F}`.  Hence

\[
                       \partial O=\partial N,           \tag{6.11}
\]

and the toggle preserves the directed Euler boundary.  The Boolean-hex
identity, together with the common rail, proves equality of the complete
immediate lower, upper, tail and head occurrence vectors.  The disjointness
argument in the long-collar theorem makes this a literal one-copy statement
inside the packet, not merely a signed current cancellation.

Unlike full reversal, (6.10) changes unordered support.  Literally,

\[
\begin{array}{c|c}
G_d^-& (EF\cup R_d)\text{ one cycle},\ AB,\ CD\\
G_d^+& A-F-R_d-E-D\text{ one path},\ C-B\text{ one path}.
\end{array}                                               \tag{6.12}
\]

On this local vertex bank the weak-component count drops from three to two,
so the graphic rank rises by exactly one.  This is a genuine
support-changing component actuator.  It is simultaneously neutral in the
local matching rank: (6.10) is an alternating cycle between two perfect
matchings of the same three tails and heads.  In DM language it moves within
one balanced local component and creates no augmenting path.  Its value is
the graphic-rank change, not a local Hall gain.

The attachment permutation in tail order `(A,C,E)` changes the old head
list `(B,D,F)` to `(F,B,D)`, a three-cycle and therefore an even
permutation.  Consequently, if both local path covers are completed by the
same exterior source--sink matching to full successor permutations, the
two completed permutations have the same sign and hence the same parity of
cycle count.  The local `3 -> 2` path-component change in (6.12) must then
be accompanied by another parity change in the exterior closure.  It does
not, without a proved portal completion, certify a two-closed-cycles-to-one
fusion.

### 6.3 Exact all-depth, DM and exterior scope

For the reset--return complete reversal, the internal statement is now
finished: Section 6.1 records exact residence, all derivative rows, all
cyclic interval-OR widths, and an isomorphism of the internal compiler
incidence graph.  In particular the two internal Dulmage--Mendelsohn
decompositions are isomorphic and have the same matching rank and
deficiency.  The alternating cycles (6.6)--(6.7) are basis changes inside
that saturated graph, not augmenting paths.

This is still not fixed-exterior transparency.  Root both phases at `E`.
In the notation of the complete-reversal theorem, already their first
two-root prefix unions are

\[
       E\cup T_1=E+X_{d+1},\qquad
       E\cup Q_{d-1}=E+y_d,                              \tag{6.12a}
\]

and are different because `y_d` lies outside the complete reset support.
Reversal exchanges cyclic occurrences but does not fix their linear
addresses.  Thus an unchanged exterior sees different prefix/suffix
ladders unless its sockets are also reversed or a separate crossing-window
certificate is supplied.  Likewise, opening a common edge turns the
attachment and predecessor alternating cycles into portal paths, but those
paths augment only if an external deficient shore is reachable.

The frozen linearization theorem makes this quantitative.  For the
maximal depth-`d` antecedent of the reset--return packet, every cut destroys
at least

\[
                              d(2d-1)                       \tag{6.12c}
\]

distinct OR values which have no second witness anywhere inside the
cyclic packet.  Thus no cut has `O(1)` internal collateral.  A linear use
must reserve the explicit ambient duplicate bank, reflect a compatible
whole exterior component, or retain a nonlinear contraction.

Topologically, complete reversal remains powerless: it sends one successor
cycle to its inverse, changes no undirected edge, and has even relative
permutation.  If the closed packet is opened to a path, the two orientations
swap its source and sink and have boundary difference twice the endpoint
unit current.  A fixed exterior must therefore supply a complementary
portal current.  With only two Johnson boundary edges and exact preservation
of both q1 palettes, Theorem 3.1 forces the two exterior owners to coincide;
that closure merely reverses one component.  A genuine fusion still needs
an odd, support-changing exterior connector.

Separately, complete-reversal transparency does not transfer to the
support-changing Boolean-hex toggle (6.9).  Opening its seam destroys
exactly `q` local cyclic witnesses
at depth `q`, for `1<=q<=d`; these are pairwise distinct, giving the exact
local collateral bank

\[
                            \sum_{q=1}^d q={d(d+1)\over2}. \tag{6.13}
\]

Endpoint ladders through `A,D` or duplicate bulk occurrences may cover
some of (6.13), but this must be proved occurrence by occurrence.  Moreover,
linear embedding exposes prefix/suffix unions crossing the exterior joins;
cyclic internal-deck equality does not identify those contextual unions.

For the complete reversal, a phasewise compiler matching transports
literally by reversal.  One *fixed occurrence-labelled* residual matching
across an unchanged exterior is stronger: it requires reversal invariance,
a common-minor/Hall certificate, or declared phase decoupling.  The
phase-common q1-host theorem now embeds one opened packet path in a common
spanning q1 two-factor for `m>=8d+4` (or the closed packet as an isolated
component for `m>=8d+6`).  Hence root/lower-q1 planting is closed for that
single packet, though it does not automatically tensor to the full q-port
bank.  The exact remaining rows are an upper-surjective low-component
refinement, component opening and joining carrying the quadratic
duplicate/reflection payload, a common residual compiler, voltage if
required by the quotient lift, and regeneration.  Internal residence,
internal all-width upper transport, internal compiler transport, and the
single-packet q1 path host must not be listed among those remaining rows.

## 7. The q-port component semigroup and the open-path boundary actuator

The authoritative q-port theorem supplies a literal resident realization
of the abstract q-gon topology.  Keep its notation

\[
 A_i=S+z+a_i,\qquad B_i=S+a_i+a_{i+1}\qquad(i\bmod q), \tag{7.1}
\]

with direct phases

\[
 O=\{A_i\to B_i\}_i,\qquad
 N=\{A_i\to B_{i-1}\}_i.                                \tag{7.2}
\]

The old edge has lower/upper pair `(L_i,U_i)`, while the new edge
`A_i B_(i-1)` has lower `L_i` and upper `U_(i-1)`.  Hence (7.2) preserves
the complete named lower and upper palettes, as well as the tail and head
sets.  The common resident rails in
`MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md` are disjoint
from these direct palettes and make the following topology literal at
depth `d` on exactly

\[
                             q(2d+2)                         \tag{7.3}
\]

atoms.

A sufficient literal coordinate supply for this bank is

\[
                         m\ge d+3,qquad
                         k\ge m+q+d-1,                    \tag{7.3a}
\]

as in the q-port theorem.  These inequalities are local supply conditions,
not a global one-copy host theorem.

### Theorem 7.1 (literal q-gon fusion and sign)

Suppose the `q` old arcs `A_i->B_i` lie on `q` distinct directed cycle
components.  Replace them by all `q` arcs `A_i->B_(i-1)`.  Then the new
support has one directed cycle on the union of the old components.  Thus

\[
                              q\longmapsto1,
 \qquad \Delta c=-(q-1).                                  \tag{7.4}
\]

The relative head permutation is one q-cycle, so its sign is

\[
                              (-1)^{q-1}.                   \tag{7.5}
\]

The inverse switch splits one cycle into `q` cycles.

#### Proof

Deleting `A_i->B_i` opens component `i` into a directed fragment from
`B_i` to `A_i`.  The new arc from `A_i` enters fragment `i-1`.  Iterating
`i -> i-1` visits every residue modulo `q`, so all fragments form one
cycle.  On the head bank the replacement is exactly the cyclic shift
`B_i -> B_(i-1)`, proving (7.5).  The resource statement precedes the
theorem.

In the four-state q-port history, the component word is therefore

\[
             1\xrightarrow{\text{inverse q-gon}}q
              \xrightarrow{\text{whole reflections}}q
              \xrightarrow{\text{q-gon}}1.                \tag{7.6}
\]

The middle move reverses each of the `q` cycles and changes no component.
The two q-gon signs multiply to `+1`; the endpoint states are whole
reversals of one another, consistently with Theorem 2.2.

### Theorem 7.2 (component semigroup and parity)

Let `Q` be a set of available literal q-gon arities.  Any composition of
whole-component reflections and forward fusions has

\[
       c_{\rm final}=c_{\rm initial}
          -\sum_{q\in Q} n_q(q-1),\qquad n_q\in\mathbb Z_{\ge0}. \tag{7.7}
\]

Conversely, (7.7) is sufficient at the abstract component level whenever
the indicated moves can be ordered so that each step has a literal
resource-compatible q-port packet meeting `q` distinct current components.
Thus the only arithmetic obstruction to a closed Hamilton cycle is

\[
             c_{\rm initial}-1\notin
             \left\langle q-1:q\in Q\right\rangle_{\mathbb N}. \tag{7.8}
\]

If all available `q` are odd, component parity is invariant.  An even `q`
is an odd successor permutation and changes component parity.  The smallest
literal even-arity actuator is

\[
                               q=4,                         \tag{7.9}
\]

because the q-gon requires `q>=3`, while the formal `q=2` port identifies
the two `B` roots and is the closed-doubleton obstruction.  The resident
q=4 actuator has `8d+8` atoms and changes `4` cycles to one.

With q=3 and q=4 available, the numerical monoid is

\[
                \langle2,3\rangle_{\mathbb N}
                  =\{0,2,3,4,\ldots\}.                    \tag{7.10}
\]

Hence every component count except `2` is arithmetically reducible to one.
This is not a host theorem: (7.8) forgets packet occurrence supply,
residence at exterior joins, target witnesses and the common cap.

### Theorem 7.3 (open q-gon fusion)

Under the hypotheses of Theorem 7.1, delete the `q` old arcs but install
only the `q-1` new arcs

\[
                     A_i\to B_{i-1}\qquad(i\ne j).         \tag{7.11}
\]

The result is one directed Hamilton path on the union of the q fragments,
starting at `B_(j-1)` and ending at `A_j`.  Relative to the closed direct
palette, it omits exactly

\[
                \text{lower }L_j,\qquad
                \text{upper }U_{j-1},                     \tag{7.12}
\]

and its directed boundary is

\[
                         e_{A_j}-e_{B_{j-1}}.               \tag{7.13}
\]

#### Proof

The missing arc in (7.11) removes the unique entrance to fragment `j-1`
and the unique exit from fragment `j`.  The remaining shift edges visit
all q fragments in order, producing the asserted path.  New edge `i` has
lower `L_i` and upper `U_(i-1)`, so omitting `i=j` gives (7.12).
Telescoping the path gives (7.13).

Adding the omitted edge closes this path and recovers Theorem 7.1.  Thus
the open boundary stores exactly the missing closed-permutation parity; a
cycle sign is not defined until that edge is restored.  Component
arithmetic is unchanged: an open q-fusion still reduces the number of
components by `q-1`.  Consequently a construction may perform closed
fusions until its last q components and use Theorem 7.3 as the final
Hamilton-path step.  The exceptional two-component case is not repaired by
the q-gon bank: it needs a separate support-changing open two-component
join or an auxiliary third component, and the support-four fixed-path
reversal of Sections 1--3 supplies neither.

## 8. DM rank and the conditional ambient duplicate-bank criterion

The topology gain in Theorem 7.1 is not a matching-rank gain.  In the
bipartite tail--head graph, `O` and `N` are two perfect matchings whose
symmetric difference is one alternating `C_(2q)`.  Both saturate exactly
the same vertices, so the local DM deficiency is zero in both phases.
The toggle is a basis exchange inside one balanced DM component.  Its
graphic rank rises by `q-1` only because the old matched arcs lie on
distinct directed cycle components.

The open set (7.11) is a near-perfect matching with the single unmatched
tail `A_j` and unmatched head `B_(j-1)`.  The alternating `C_(2q)` is opened
to one alternating path.  This is exactly the allowed source/sink defect of
a Hamilton path, not a Hall augmentation.  Restoring the omitted edge
returns local matching deficiency zero.

Ambient Hall surplus can nevertheless change after fixed exterior
neighbours are contracted: an old packet neighbour may already be supplied
outside while a new one is genuinely new.  Such a gain is governed by the
distinct-neighbour cut formula of the complete-reversal theorem; it is not
an intrinsic rank of the q-gon circuit.

The all-depth obstruction to using the graphic gain is target survival.
The q-port theorem proves local one-copy roots, both immediate palettes and
residence, but the individual q-gon transitions generally change deeper
OR witnesses.  Linear opening also creates exterior prefix/suffix and
compiler cells.  The following criterion is exact after the ambient packet
placement is fixed.

There is one important one-sided improvement.  Corollary 6.3 of the q-port
theorem proves

\[
       \operatorname{Deck}_{\vee}(H_2)
          \subseteq \operatorname{Deck}_{\vee}(H_3),       \tag{8.0}
\]

where the deck is the ungraded set of internal root-interval unions.  Thus
the fusion direction deletes no last internal upper witness.  Its first
graded current is nevertheless nonzero at width `d+3`: one occurrence of
each saturated two-active-label value is replaced by a genuinely new
three-active-label value.  Formula (8.1) therefore has no demand from old
*internal upper support* in the closed fusion, but it may still have demand
from derivative/source rows, fixed occurrence multiplicities, exterior
cross-windows, an opening, or the common compiler.  The reverse split does
have genuine new-value casualties.

Let `lambda_new(T)` be the number of surviving or newly created packet
witnesses of required target `T`, and let `b(T)` be the number of common
surviving exterior witnesses not assigned to the reserve bank.  Put

\[
                    r(T)=\bigl(1-b(T)-\lambda_{\rm new}(T)\bigr)_+. \tag{8.1}
\]

Assume the reserve tickets have already been made resource-private: two
distinct tickets have no remaining mutual owner, palette, guard or cap
conflict.  Let `C_T` be the set of such exterior reserve tickets which
realize `T` and survive the complete q-gon toggle and chosen opening.  Form
the bipartite graph `T--C_T`, repeating target `T` according to demand
`r(T)`.

### Theorem 8.1 (conditional ambient duplicate-bank fusion)

Relative to the frozen exterior and this resource-private reserve
catalogue, the q-gon fusion has a target-complete occurrence-injective
realization if and only if

\[
             |N(\mathcal A)|\ge
                    \sum_{T\in\mathcal A}r(T)             \tag{8.2}
\]

for every target family `A`.  For the open fusion, (8.1) includes the
named immediate deficits `L_j,U_(j-1)` from (7.12), unless the terminal
boundary convention pays them directly.

#### Proof

All common internal witnesses are already retained.  Every remaining
deficit is one of the demand copies in (8.1), and a physical reserve cell
can be used at most once.  Therefore completion is precisely a bipartite
matching saturating the repeated demand shore.  Hall's theorem gives
(8.2).

Without resource privacy, (8.2) remains necessary but need not be
sufficient: the reserve selector is then a Rado/matroidal or more general
conflict problem, not an ordinary bipartite matching.

The adjective **conditional** also includes the choice of induction mode.
Theorem 8.1 is needed for a local switch whose exterior and literal
compiler addresses are frozen.  In the reversal-quotient existential mode,
one instead constructs a terminal matching for the selected oriented child;
global reversal transports that matching to the other representative.  In
that mode no intersection of the two phase graphs, and no phase-common
reserve assignment, is required.  Named one-sided sockets or independently
oriented packet components are not quotient gauges and still require the
local criterion.

For a literal component fusion, (8.2) must be combined with the following
independent hypotheses:

1. after contracting the unchanged ambient support, the q old packet arcs
   lie on q distinct components and the new port shift is one q-cycle;
2. the chosen oriented q-port root/lower/q1 bank has a one-copy host
   (phase-common support is needed only for a frozen local switch);
3. every exterior join passes the coordinate residence and Johnson tests;
4. the reserve graph includes every derivative/source, graded-occurrence,
   opening and crossing-window casualty, not only immediate colours
   (closed fusion needs no reserve for old internal root-OR support by
   (8.0)); and
5. the chosen terminal orientation has a residual compiler matching; if a
   local switch requires one matching common to both phases, then after
   contracting transported internal matches the intersection of the two
   residual target--cell graphs satisfies Hall; and
6. any quotient lift has the prescribed joined voltage and retains its
   named boundary/comparator pins.

The protected q1-host theorem proves the stronger phase-common form of item
2 for one opened complete-reversal packet at its stated threshold.  It does
not automatically tensor to an arbitrary q-port bank; even the one-oriented
larger host remains a hypothesis.  Likewise, endpoint/full-component reversal is
all-width transparent, whereas the individual q-gon fusion is not.

Under the applicable local-switch or quotient versions of these six
conditions, Theorem 7.1 gives a closed component reduction
of `q-1`, and Theorem 7.3 gives the final open Hamilton-path version.  No
chronology, arbitrary-upper, common-cap, or compiler conclusion is asserted
when any condition is omitted.

## 9. Reversal-quotient form of the nonlinear fusion

Let `[H]` denote simultaneous reversal of the complete source word,
endpoint interface, witness bank and compiler certificate.  The global
reversal theorem
`MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`
gives

\[
                         [H_0]=[H_3],\qquad [H_1]=[H_2].    \tag{9.1}
\]

Therefore the three-step q-port history is not an induction-state role
conversion.  Choose `H_2` as the convenient representative of the
q-component orbit and apply the support-changing q-gon fusion directly:

\[
                         [H_1]=[H_2]\longrightarrow
                         [H_3]=[H_0].                       \tag{9.2}
\]

This quotient transition reduces `q` components to one, has parity
`(-1)^(q-1)`, preserves the complete immediate palettes and residence, and
is internally upper-support monotone by (8.0).  A terminal compiler only
has to exist for the chosen `H_3` child; its reflected matching certifies
the `H_0` representative automatically.

The quotient does not erase any reversal-invariant obligation.  It leaves
unchanged the component arithmetic (7.7), the absolute opening debt
`d(2d-1)`, any lower derivative/source deficit of the q-gon fusion, quotient
voltage, and named one-sided sockets.  If reversal fixes the `c` component
labels setwise, it removes only the diagonal phase bit
`epsilon -> epsilon+1`; the remaining `c-1` relative phase bits still need
a connector/orientation theorem.  More generally it acts as
`epsilon -> 1+P epsilon` for an involutive component permutation `P` and
removes at most one binary choice.  Thus (9.2), rather than a phase-common
intersection model, is the weakest exact one-oriented-host formulation.

## 10. Frozen k=17 MMM calibration

The exact H100 audit

`scratch/threadD_k17_open_c4_reversal_20260801/`

expands the frozen 1,430-row MMM quotient cycle to its 24,310-owner physical
cycle (unit voltage), verifies 24,310 distinct lower colours, and tests all
24,310 consecutive four-root segments against the literal
`V_1,V_2,V_3,V_0` square normal form.  It finds

\[
  \#\{\text{quotient consecutive squares}\}=0,
  \qquad
  \#\{\text{physical consecutive squares}\}=0.           \tag{10.1}
\]

Thus the frozen MMM carrier contains no bare consecutive open-square
reversal at all.  Independently,

\[
                              24310\equiv1\pmod3,          \tag{10.2}
\]

so even a hypothetical resource-disjoint bank of three-edge square paths
could not tile that one cycle as required by Theorem 2.2.

The primary `-O3` run used one pinned H100 CPU, a 2-GiB address-space cap
and a 120-second CPU cap; it finished in 0.01 seconds at 5,632 KiB RSS.
An independent rank/distance replay reproduces (10.1).  This is only a
calibration of literal consecutive squares in the frozen MMM carrier.  It
does not obstruct prospectively planted reset--return or q-port packets,
nonconsecutive support-changing circuits, or any downstream chronology and
compiler construction.

## 11. The exact q=4-dominant fusion hierarchy

This section separates the unconditional component arithmetic from the
still-missing regenerative embedding.  All fusions are taken in the
one-oriented quotient direction

\[
                         H_2\longrightarrow H_3.          \tag{11.1}
\]

No phase-common compiler or intersection of two residual matching graphs is
assumed.

### 11.1 Optimal component arithmetic and parity

Let a directed factor initially have `c` cycle components.  If only q=4
fusions are used, the maximum possible number and the resulting minimum
component count at the abstract component level are

\[
 N_4^{\max}=\left\lfloor {c-1\over3}\right\rfloor,
 \qquad
 c_4^*=c-3\left\lfloor {c-1\over3}\right\rfloor
   =\begin{cases}
      1,&c\equiv1\pmod3,\\
      2,&c\equiv2\pmod3,\\
      3,&c\equiv0\pmod3.
    \end{cases}                                          \tag{11.2}
\]

Indeed every q=4 move reduces the current count by three and may be repeated
while at least four components remain.  Hence a pure q=4 hierarchy reaches
one component if and only if

\[
                              c\equiv1\pmod3.              \tag{11.3}
\]

Equivalently, a rooted full 4-ary fusion tree with `c` leaves exists exactly
when `c=3N_4+1`.

If q=3 packets are also available, the following q=4-dominant schedule is
optimal in the number of packets:

\[
\begin{array}{c|c|c|c}
c\pmod3 & N_4&N_3&N_4+N_3\\ \hline
1&(c-1)/3&0&(c-1)/3\\
0&(c-3)/3&1&c/3\\
2,\ c\ge5&(c-5)/3&2&(c+1)/3.
\end{array}                                               \tag{11.4}
\]

For the last row one must stop the q=4 descent at five components, not at
the q=4-only residue two, and then use `5 -> 3 -> 1`.  The other terminal
steps are `3 -> 1` and `4 -> 1`.  Every packet reduces the component count
by at most three, so (11.4) attains the lower bound

\[
                     N_3+N_4\ge
                     \left\lceil{c-1\over3}\right\rceil.  \tag{11.5}
\]

The exceptional count `c=2` cannot be reduced by either arity without an
auxiliary component or a different two-component actuator.

More invariantly, every rooted `{3,4}`-ary fusion tree satisfies, and at the
abstract component level is characterized by,

\[
                         c-1=2N_3+3N_4.                   \tag{11.6}
\]

There is no further successor-parity obstruction.  A q=3 fusion is even and
a q=4 fusion is odd, so a closed hierarchy changes successor sign by

\[
                              (-1)^{N_4}.                  \tag{11.7}
\]

But (11.6) gives `N_4 = c-1 (mod 2)`, exactly the sign change between a
`c`-cycle permutation and a one-cycle permutation on the same vertex set.

### 11.2 A sufficient regenerative certificate

Call a rooted `{3,4}`-ary fusion hierarchy **private and packet-closed at
depth d** if the following data are supplied.

1.  Every internal node of arity `q` has a literal oriented q-port
    occurrence in state `H_2`, one port component in each child component,
    and its rewrite to `H_3` contracts precisely those `q` child components
    to one.
2.  The packet atoms and their named owner, lower-q1, upper-q1, tail and head
    resources are disjoint across internal nodes and from the protected
    ambient resources, except for the old/new identifications internal to a
    single q-port trade.
3.  Substituting the already constructed child interiors for the q-port
    fragments is legal: it preserves the port endpoints and the stated
    immediate resource ledger.  Thus a child output is a legal input port
    for its parent.  This is the **regeneration** clause.
4.  At every new join, recomputing the coordinate traces creates no newly
    bounded positive run of length at most `d`.  Equivalently, every positive
    run touching a deleted or inserted port edge in the new cyclic order has
    length at least `d+1`.
5.  Every old arbitrary-width interval witness not wholly internal to the
    local `H_2` packet either survives the splice or has a protected witness
    outside the rewritten occurrence.  This is the exterior-sealing clause.
6.  The chosen terminal orientation, its named comparator pins and its
    voltage have one residual compiler/cap certificate.  No certificate for
    the globally reflected orientation is required.

These hypotheses are deliberately occurrence-level.  Pairwise disjoint
abstract target names without disjoint literal owners do not imply item 2,
and internal residence of each isolated q-port packet does not imply item 4
after child interiors are substituted.

### Theorem 11.1 (conditional monotone hierarchy theorem)

Given a private packet-closed hierarchy, applying its nodes bottom-up yields
the component count prescribed by (11.6), preserves every named owner and
both immediate palettes exactly once, and preserves depth-`d` residence.  In
addition, the set of internally witnessed upper interval unions is
monotone nondecreasing at every fusion.  In particular, a hierarchy with the
counts in (11.4) gives one resident cycle for every `c != 2`.

#### Proof

At one node, Theorem 7.1 gives the component contraction and preserves the
complete named immediate-resource sets.  Resource privacy therefore
preserves global one-copy use.  The local q-port theorem proves residence
inside the rewritten packet; item 4 is exactly the remaining check for runs
meeting a splice.  Corollary 6.3 gives

\[
                         \operatorname{Deck}(H_2)
                              \subseteq
                         \operatorname{Deck}(H_3)          \tag{11.8}
\]

for internal packet intervals, and item 5 protects all other old witnesses.
Thus target support cannot decrease.  Induction over the rooted hierarchy
proves the assertion.  The terminal compiler statement follows from the
global-reversal quotient theorem.  \(\square\)

The graded deck is not monotone.  Its exact first current at each node `v`
is

\[
 \Delta D_{d+3}^{(v)}
   =\sum_{i\bmod q_v}
       \left(e_{D_{v,i}}-e_{C_{v,i}}\right),              \tag{11.9}
\]

with the `C,D` values of the q-port theorem.  For q=4 the four `D_(v,i)`
are distinct within the node; for q=3 they are one value of multiplicity
three.  Every negative `C_(v,i)` retains another local occurrence, which is
why (11.8), but not a coefficientwise graded inequality, composes.

Under the resource-private sufficient condition, the exact number of packet
atoms reserved by a hierarchy is

\[
               R_d=(2d+2)(4N_4+3N_3).                    \tag{11.10}
\]

For the optimal schedules (11.4), this is also the minimum private-atom
census among abstract q=3/q=4 hierarchies:

\[
 {R_d^{\min}\over2d+2}=
 \begin{cases}
   (4c-4)/3,&c\equiv1\pmod3,\\
   (4c-3)/3,&c\equiv0\pmod3,\\
   (4c-2)/3,&c\equiv2\pmod3,\ c\ge5.
 \end{cases}                                             \tag{11.10a}
\]

To see minimality, replacing two q=4 reductions by three q=3 reductions
keeps the component decrement six but raises the atom coefficient from
eight to nine; the residue classes force exactly the terminal q=3 counts in
(11.4).

Consequently `R_d <= W` and the analogous lower/upper palette capacities
are necessary for this disjoint implementation.  Failure of (11.10) rules
out the private hierarchy, not an overlapping or recycling construction.

### 11.3 One terminal opening: the bare ledger and the protected payment

All internal nodes should remain cyclic.  At the terminal q-port node one
may omit one new edge and use Theorem 7.3.  This produces one Hamilton path
and exports exactly one lower and one upper immediate deficit,

\[
                             L_j,\quad U_{j-1},             \tag{11.11}
\]

together with boundary `e_(A_j)-e_(B_(j-1))`.  Thus the q=4/q=3 hierarchy
does not multiply the immediate boundary deficit: it is paid once at the
root.

There is a separate bare source-linearization ledger.  If the terminal opening
is made through an authenticated complete-reversal cyclic source packet of
depth `d`, and the first `ell` cyclic source cells are appended after the
cut, the exact forced short-family loss is

\[
 C_d(\ell)=\sum_{w=2}^{2d}\max(0,w-1-\ell)
           =\binom{2d-\ell}{2},
                 \qquad0\le\ell\le2d-1.                  \tag{11.12}
\]

In particular,

\[
 C_d(0)=d(2d-1),
 \qquad C_d(d)=\binom d2.                                 \tag{11.13}
\]

The second value is the residual forced debt of the canonical owner-exact
`d`-cell restitution tail.  Clearing this forced family by the one-sided
continuation `ell=2d-1` creates `d-1` extra depth-`d` owner occurrences.
Additional long-interval losses may remain in every case.

Equations (11.12)--(11.13) are not a theorem about an arbitrary q-port
cycle: they apply only when the final cut has the complete-reversal source
normal form.  For a general terminal realization the exact condition is the
occurrencewise ambient inequality

\[
                         N_+(T)\ge\mu_c(T)
                         \quad\hbox{for every target }T.   \tag{11.14}
\]

Here `mu_c(T)` is the cyclic multiplicity destroyed by the cut and `N_+(T)`
counts surviving nonpacket witnesses in the chosen oriented ambient word.
Global reversal transports a payment of (11.14); it does not pay it.

For the canonical `ell=d` complete-reversal opening, the newer protected
overlap theorem completely supersedes this ledger as a *remaining local
hole bound*, without changing (11.12) as a self-supply statement.  The full
local leave is exactly two upper Ferrers triangles, of total size
`d(d+1)`.  Two protected Johnson banks on `5d` raw owners cover every one
of those targets; after the two one-sided residence collars the bank uses at
most `7d` protected owners.  It appends no source letters beyond the
mandatory owner-exact `M+d` antecedent.  Thus `binom(d,2)` remains an exact
packet-self-supply loss, but the canonical protected terminal module has
zero uncompensated local leave.  What remains is its one-oriented
upper-complete ambient host, exterior deck preservation and terminal
compiler, all separate from the q-port hierarchy theorem.

Most importantly, (11.12) is paid once only if every nonroot fusion is a
closed cyclic substitution.  If construction of an internal hierarchy node
requires linearizing its packet, that node contributes its own
occurrence-labelled cut family.  Such families need not be disjoint as mask
sets, so their target-hole cardinalities cannot simply be added, but neither
may they be discarded.  A genuine regenerative theorem must therefore
provide closed child-to-parent packet substitution or explicit ambient
repayment at every internal cut.

### 11.4 The sharp remaining gate

The standalone q-port theorem proves the local states, immediate palettes,
residence and internal support inclusion.  It does **not** prove item 3:
the fused `H_3` component is not automatically a fresh `H_2` port component
for a parent node after arbitrary child interiors are inserted.  Nor does it
prove the exterior-sealing, terminal common-cap, voltage or named-pin rows.
Therefore (11.2)--(11.7) are unconditional component arithmetic, while
Theorem 11.1 is the strongest noncircular hierarchy statement currently
available.  The missing all-scale theorem is precisely a one-oriented,
packet-closed host satisfying items 2--6 with (11.10), not a phase-common
compiler theorem.
