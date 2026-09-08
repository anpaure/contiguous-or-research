# `k=17`: marker-58 five-state source atlas and the unbuffered `PH` fusion gate

**Date:** 2026-08-02  
**Lane:** H3, protected upper host / pure theorem  
**Status:** exact source-atlas formulation and exact ordinary-fusion no-go.
No source atlas is enumerated, no q1 or upper solve is duplicated, and no
chronology, residence, deeper-upper, or compiler claim is made.

> **Finite-host supersession.**  Sections 1--3 below freeze the atlas over
> the earlier 1,179-component lower-q1 witness.  A later theorem constructs a
> connected rank-ten-complete equivariant factor containing the same 986
> paths, but the exact residence audit rejects that chronology before atlas
> binding: it has 5,372 cyclic short runs and no legal depth-three cut.  The
> deadline-particle audit also rejects every optimal three-particle monotone
> staircase on the same chronology (`G_2=36`, loss at least 48,548 versus
> budget 7,401).  The
> current atlas is therefore `E_u(m)`, conditioned on a residence-aware
> factor/orientation/seam master `m`, as formalized in
> `MATH_THEOREM_H3_K17_MARKER58_RESIDENCE_AWARE_FACTOR_SOURCE_FIBRE_AND_DEEP_UPPER_RETHREAD_GATE_20260802.md`.
> The unbuffered-packet and ordinary-fusion results in Sections 4--5 are not
> withdrawn.

## 1. Frozen rebase

The named-resource and lower-q1 rows are no longer the finite target.

1. The frozen marker orbit bank contains 96 base modules whose full
   `Z_17` development gives 1,632 pairwise owner/all-named-target-disjoint
   modules.
2. Fix the **first 58** base rows in the witness, develop all 17 rotations,
   and open native edge type `3`.  This gives 986 pairwise vertex-disjoint
   protected paths on 4,930 owners with 3,944 distinct rank-eight colours.
3. The b-flow theorem first extended this protected bank to a
   rank-eight-rainbow two-factor on all 24,310 owners.  That historical
   witness has 1,179 components and is not upper complete.
4. A later 35,713-primary-variable quotient model produced a connected,
   nonzero-voltage, rank-ten-complete factor retaining the same paths.  Its
   chronology is exactly depth-three nonresident, so it is a positive
   palette/topology witness but not an atlas host.

The frozen inputs are

```text
MATH_THEOREM_K17_MARKER_RESERVOIR_Z17_ORBIT_PACKING_20260802.md
  bf072e7c74918ad729a14ba030e866de895444df85a5af02ecd2230357e40ee7
scratch/k17_marker_orbit_packing_20260802/k17_marker_orbit.witness.tsv
  88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
MATH_THEOREM_K17_MARKER58_Q1_BFLOW_AND_UPPER_QUOTIENT_CORE_20260802.md
  4401c1e021144b65f75a47f3e7164c38f3ea649053221f78cb95c081ba23aa08
scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv
  0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e
scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.independent_ad.audit.json
  518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d
```

Thus rank-eight q1 extension and existence of one connected rank-ten factor
are inputs, but a usable factor is again a variable: it must be reselected
with residence active and then have a nonempty joint five-state source fibre.

## 2. The exact five-state atlas

Let

\[
                  {\cal U}={\cal I}_{58}\times\mathbb Z_{17},
                  \qquad |{\cal U}|=986.                 \tag{2.1}
\]

For each \(u\in{\cal U}\), let
\(\mathbf R_u=(\rho_{u,0},\ldots,\rho_{u,4})\) be its frozen ordered
source-role word.  Its role multiset is

\[
                \{\rho_{u,0},\ldots,\rho_{u,4}\}
                         =\{P,H,B_1,B_2,B_3\}.            \tag{2.2}
\]

The literal order, masks, roots and marked cells are those of the frozen
marker module translated by `u`.

An **atlas entry** `e in E_u` is one complete occurrence-labelled embedding
of `R_u` into the physical host.  It must replay simultaneously:

1. all five literal source states, in their frozen directed order;
2. the attachment of their owner word to the fixed open-type-3 protected
   path of the lower-q1 factor;
3. every marked lower and named target cell of the module;
4. the fixed-`M_0` root/head legality and occurrence identity;
5. the complete local predecessor/successor collar and every frozen
   protected reservation touching the five states; and
6. every physical position, capacity token, and local clause changed or
   consumed by that embedding.

Missing data gives no entry.  A rolewise list without the joint directed
word and collar is not an atlas entry.

Let `P(e)` be the complete multiplicity-labelled footprint of `e`.  Let
`b_p` be the residual capacity of physical token `p`, and let `a_(e,p)` be
the multiplicity of `p` in `e`.  Finally let `C` be the exhaustive family of
all minimal cross-entry forbidden tuples not already represented by a shared
capacity token.

### Theorem 2.1 (exact marker-58 source-binding system)

The 986 protected paths have a simultaneous five-state source binding if
and only if the following finite system has a solution:

\[
 \sum_{e\in{\cal E}_u}z_{u,e}=1
                         \qquad(u\in{\cal U}),            \tag{2.3}
\]

\[
 \sum_{u,e}a_{e,p}z_{u,e}\le b_p
                         \qquad(p\text{ a physical token}), \tag{2.4}
\]

\[
 \sum_{(u,e)\in C}z_{u,e}\le |C|-1
                         \qquad(C\in{\cal C}),            \tag{2.5}
\]

with `z_(u,e) in {0,1}`.

#### Proof

A physical binding chooses exactly one complete entry for every protected
path, respects every token capacity, and cannot contain a forbidden tuple;
this gives (2.3)--(2.5).  Conversely, each selected entry already contains
the complete within-module source word and local guards.  Equations (2.4)
and (2.5) exclude every cross-module incompatibility, so the union of the
selected entries is precisely a simultaneous source binding. \(\square\)

This is an exact formulation, not an existence proof.  In particular,
`E_u` may be empty and the tuple family may be nonempty.

The aggregate source ledger is slack.  The fixed 986 modules demand

\[
        (e_4,e_2,L-H)=(986,3944,2958)                    \tag{2.5a}
\]

against the authenticated scalar capacities `(3808,7072,7403)`, leaving
`(2822,3128,4445)`.  Hence a failure of (2.3)--(2.5) is positional or
correlational, not this three-row scalar shortage.

### Corollary 2.2 (two sufficient expansion tests)

Assume every cross-entry incompatibility is represented by a shared
capacity token, so \({\cal C}=\varnothing\), and clone capacities into
physical slots.  Replace each atlas entry by all of its concrete assignments
to the required token clones; call the resulting family
\(\widehat{\cal E}_u\), and regard every concrete footprint as a hyperedge
of rank at most `g` in \({\cal H}_u\).  Either of the following conditions
suffices for (2.3)--(2.4).

1. For every nonempty \(I\subseteq{\cal U}\),

   \[
       \nu\!\left(\bigcup_{u\in I}{\cal H}_u\right)
                           >g(|I|-1).                    \tag{2.6}
   \]

2. With

   \[
   L=\min_u|\widehat{\cal E}_u|,
   \qquad
   \Delta=\max_{\substack{u\ne v\\e\in\widehat{\cal E}_u}}
      |\{f\in\widehat{\cal E}_v:P(e)\cap P(f)\ne\varnothing\}|, \tag{2.7}
   \]

   one has

   \[
                              L>985\Delta.                \tag{2.8}
   \]

Condition (2.6) is the Aharoni--Haxell rainbow-matching hypothesis.
For (2.8), after `j` choices each remaining module has lost at most
`j Delta` entries, so a greedy choice remains.  Neither condition is
necessary.

Only under a separately proved rectangularity

\[
                    {\cal E}_u=\prod_{r\in\mathbf R_u}A_{u,r} \tag{2.9}
\]

with no tuple constraints does this reduce to one capacitated bipartite
matching on the demand nodes `(u,r)`.  It separates into five independent
rolewise Hall systems only if the five role token shores are also disjoint.
Literal adjacency, the fixed root, shared H/buffer capacities and collars
are exactly why these hypotheses are not automatic.

## 3. Physical versus quotient scope

The protected marker paths are `Z_17`-equivariant, but the authenticated
1,179-component lower-q1 factor is not.  Therefore its five-state source
atlas is a physical 986-path object.  Dividing the five roles by 17 merely
because their names lie in coordinate orbits is unsound.

A quotient atlas is valid only after proving that the complete source
occurrence universe, fixed matching, local collars, protected exclusions,
and every tuple constraint are transported by the same free `Z_17` action.
One quotient entry must then lift to all 17 translated five-state words, so
its multiplicities in (2.4) carry the orbit weights.  The live upper quotient
solve does not by itself prove this source symmetry.

The exact finite output language is therefore:

* `ELIGIBLE(u,e)` only after complete replay of the six requirements above;
* `NO_ENTRY_CERTIFIED(u)` only after an exhaustive, epoch-bound atlas for
  `u` is checked;
* `BOUND` only after (2.3)--(2.5) has a positive certificate; and
* `UNKNOWN` for every missing role, collar, tuple, or completeness manifest.

## 4. The unbuffered packet at `k=17`

For the unbuffered alternating rotor put

\[
 k=17,\quad r=9,\quad q=5,\quad d=3,\quad c=5,
 \quad m=3,\quad L=6,\quad Q=7.                          \tag{4.1}
\]

One support has `A={beta} dotcup V`, `|V|=6`, and its module indices are

\[
                         X\in\binom{[17]-A}{4},
                         \qquad\binom{10}{4}=210.         \tag{4.2}
\]

The literal cycle `(PH)^3` has six primitive source states, three of each
type, no short buffers, and the exact named-deck counts

\[
\begin{array}{c|rrrrrr}
\text{rank}&5&6&7&8&9&10\\ \hline
\text{count}&3&3&6&6&6&6.
\end{array}                                               \tag{4.3}
\]

Thus it has 30 named resources and six source states per cycle.  A buffered
marker module has deck counts `(1,1,5,5,5)` at ranks 5--9 and five source
states: one `P`, one `H`, and three short buffers.

### Proposition 4.1 (no finite drop-in replacement)

The unbuffered packet does not replace the frozen marker-58 bank or its
lower-q1 factor without rebuilding both the named packing and the protected
factor.

#### Proof

Its support has seven fixed coordinates rather than six, its module
reservoir has 210 rather than 330 members, its protected component has six
owners rather than the marker path's five, and its named deck includes six
rank-ten caps.  The frozen orbit conflict graph and the first-58 b-flow
factor authenticate the marker deck and its four-edge open paths only.
None of their resource or incidence certificates transports to (4.3).
Hence literal substitution changes both protected vertices and protected
edges of the fixed factor. \(\square\)

At equal protected-owner coverage there is no physical-slot saving.  The
986 marker paths request

\[
                   986(1P+1H+3B)=4930                 \tag{4.4}
\]

source states.  The same number of unbuffered cycles requests
`986*6=5916` primitive states.  Matching the marker bank's 4,930 protected
owners instead needs at least `ceil(4930/6)=822` alternating cycles and
`822*6=4932` primitive states.  The benefit is therefore removal of the
**short-buffer type and its low-minus-high scalar charge**, not a reduction
in total source positions at this owner metric.

At equal primitive-signature demand the comparison reverses.  Each
alternating cycle realizes three inseparable copies of `g_(2,4)`, so 329
cycles realize 987 signatures using only `329*6=1974` source states and the
same number of owners.  This is a genuine aggregate compression relative to
986 one-signature marker modules.  It does not map those signatures to the
986 fixed occurrence-labelled protected paths, and the three signatures
cannot be split from their common six-cycle or immediate-upper deck.

There is one finite local positive statement.  The 210 modules of a single
support (4.2) are mutually named-deck-disjoint, giving 1,260 distinct owners,
1,260 distinct rank-eight facets, 1,260 distinct rank-ten caps and 630
primitive signatures.  Reaching 329 cycles already requires a cross-support
extraction, for which the sufficiently-large clustered-pruning theorem gives
no `k=17` constant.

The asymptotic clustered-pruning theorem does prove an
`Omega(W/q^2)` named-deck-disjoint unbuffered bank and includes the immediate-
upper deck.  Its aggregate reservation theorem assumes `d>=4`; it gives no
finite `k=17,d=3` physical occurrence allocation.  No finite `Z_17` orbit
packing, protected q1 extension, or six-state source atlas has been proved
for (4.3).

### Proposition 4.2 (exact replacement b-flow)

Let `P` be any finite protected unbuffered cycle bank.  In the bipartite
incidence graph between rank-eight facets `F` and rank-nine owners `O`, count
both incidences of every protected edge and put

\[
 b_F(f)=2-\deg_P(f),\qquad b_O(o)=2-\deg_P(o).            \tag{4.5}
\]

Assume these residual demands are nonnegative.  Then `P` extends to a
spanning lower-rainbow two-factor if and only if the network

\[
 s\longrightarrow f\longrightarrow o\longrightarrow t             \tag{4.6}
\]

with capacities `b_F(f),1,b_O(o)` has flow
\(\sum_f b_F(f)=\sum_o b_O(o)\).  Equivalently, for every residual facet
set `A`,

\[
 \sum_{f\in A}b_F(f)
       \le\sum_{o\in O}\min\{b_O(o),\deg_A(o)\}.          \tag{4.7}
\]

The proof is the same incidence-flow bijection as for marker-58: a unit
`f -> o` selects owner `o` as one endpoint of the unique edge of lower colour
`f`.  In particular, an intact `(PH)^3` cycle has zero residual demand on
all six of its facets and owners.  Any containing two-factor therefore
leaves it as an isolated component.  No positive finite `k=17` flow
certificate is known for an opened unbuffered bank.

## 5. Sharp ordinary-fusion obstruction

The complete deck in (4.3) is lower-rainbow and immediate-upper-rainbow.
That strength prevents an ordinary transparent two-cycle splice.

### Theorem 5.1 (no ordinary transparent `PH` port)

Take one edge from each of two vertex-disjoint selected `(PH)^3` cycles in
a globally lower- and immediate-upper-rainbow bank.  Thus the removed lower
colours satisfy `S!=T` and the removed upper colours satisfy `U_1!=U_2`.
Delete the edges and reconnect their four owner endpoints crosswise.  No
nondegenerate reconnection preserves the two deleted lower colours.  It also
cannot preserve the two deleted immediate-upper colours.  Consequently a
fully protected unbuffered cycle exports no palette-transparent ordinary
two-edge fusion port.

#### Proof

Write the old lower colours as distinct rank-eight sets `S,T`.  If a cross
edge has colour `S`, its two rank-nine endpoints both contain `S`; one of
them was an endpoint of the old `T`-edge and also contains `T`.  Applying
the same argument to the other cross edge gives two distinct rank-nine
endpoints containing `S union T`.  Since distinct rank-eight sets have union
of size at least nine, both endpoints must equal that union, a contradiction.

The upper proof is dual.  If the distinct old rank-ten unions are `U_1,U_2`
and the cross edges reuse them, the old and new containments force two
distinct rank-nine endpoints to be rank-nine subsets of `U_1 intersect U_2`.
Two distinct rank-ten sets have at most one common rank-nine subset, so the
switch is degenerate. \(\square\)

Thus the affected marked-chain equality in the unbuffered theorem's
component-joining boundary is an exact compatibility test, but on the fully
protected two-edge face it has no nondegenerate solution.  At `k=17` the
weaker core-rank condition

\[
                         |X\setminus Y|\le q              \tag{5.1}
\]

is vacuous because `|X|=|Y|=4<5`; it cannot detect the palette obstruction.
Moreover, every edge of a selected unbuffered cycle has a private rank-ten
cap.  Merely opening one edge removes that cap's last internal witness.  Any
nontransparent opening must therefore predeclare its rank-ten repayment as
well as its lower-colour and boundary-chain debt.

### Corollary 5.2 (what a fusion theorem must add)

Joining a protected unbuffered bank requires at least one of:

1. a support-three-or-larger zero-palette circuit;
2. an all-at-once coloured port transversal with an explicit leave and
   repayment sidecar;
3. an authenticated `q`-port role converter whose whole affected marked
   chain, immediate-upper deck, residence collars and exterior crossings are
   replayed; or
4. a larger globally compensated trade.

Random clustered pruning proves none of these.  It controls resource
collisions but does not force connectivity of a guarded multi-edge seam
graph.  Hence `(PH)^m` is an asymptotic buffer-free packet family, not yet a
transparent Catalan fusion reservoir.

### Theorem 5.3 (exact all-at-once lower-port criterion and cap deficit)

Fix `n` selected cycles.  Choose one oriented cut state

\[
                    s_i=(e_i,a_i,b_i)                    \tag{5.2}
\]

on each, with removed lower colour \(\lambda_i\) and removed upper cap
\(\mu_i\).  Let \({\cal A}(s)\) contain every directed connector
`i -> j` represented by the legal Johnson edge `b_i a_j`, after deleting
every arc failing the local collar and marked-chain guards, and require its
lower colour to lie in \(\Lambda=\{\lambda_1,\ldots,\lambda_n\}\).

For these fixed states, there is one spanning directed path using `n-1`
connectors and recycling `n-1` distinct cut lower colours if and only if
\({\cal A}(s)\) has a size-`n-1` set common-independent in:

1. the graphic matroid on the component indices;
2. the out-degree partition matroid;
3. the in-degree partition matroid; and
4. the cut-colour partition matroid.

Indeed, a graphic-independent set of size `n-1` is a spanning tree; the two
degree bounds make it one directed path, and the colour matroid gives the
declared recycling.  On the child-pays face
\(\kappa_-(b_i a_j)=\lambda_j\), this is exactly a directed Hamilton path
in the compatibility digraph.  If cuts are variable, the incoming and
outgoing arc of one component must use the same state `s_i`; choosing those
states independently is a relaxation.

This lower-port condition is not full transparency.  For every protected
target `Z` at every retained width/row `h`, the exact load after joining is

\[
 L'_h(Z)=L_h(Z)-\sum_iD_{i,h}(Z)
              +\sum_{f\in J}G_{f,h}(Z)+E_h(Z),           \tag{5.3}
\]

where `D` records deleted cut occurrences, `G` the connector occurrences,
and `E` authenticated ambient providers.  Coverage requires
\(L'_h(Z)\ge1\); a frozen occurrence inventory requires its exact prescribed
multiplicity.  The relevant marked windows are shorter than a six-state
segment, so each new window meets at most one seam and (5.3) is the literal
local ledger.  Residence and compiler boundary guards remain additional
rows.

The cap row already forces an obstruction.  The `n` cuts delete `n`
distinct private caps \(\mu_i\), while a spanning path has only `n-1`
connector edges and hence at most `n-1` new cap values.  With `E=0`, at
least one deleted protected cap remains uncovered.  Thus even a positive
four-matroid port transversal is not upper-transparent.

On the fully protected factor face, an actuator must instead be an
alternating circuit of the residual facet/owner incidence graph.  There is
no `C4`.  A later literal retained-path calculation shows that a simple
incidence `C6` can perform a binary component merge; `C8` is therefore a
larger move class, not the first binary one.  Such circuits must be
occurrence-labelled, postorder-active, socket-disjoint or regenerated, and
jointly cap/chain/residence safe.  Static component connectivity alone is
insufficient.

## 6. Exact verdict

For the current `k=17` host, continue with the fixed first-58/open-3 marker
bank.  Its owner/lower-q1 embedding is closed, and one connected rank-ten
factor exists, but that factor fails residence before (2.3)--(2.5).  The live
finite row is the residence-aware factor/source master in the superseding H3
note, not an atlas solve on the rejected chronology.

The unbuffered `(PH)^m` construction is valuable asymptotically because it
removes short-buffer-type and low-minus-high slack, and because its named
deck already includes distinct immediate-upper targets.  At `k=17` it is
not a drop-in replacement, does not reduce total source positions at equal
owner coverage, and has an exact ordinary two-edge fusion no-go.  It does
compress equal primitive-signature demand, but only in inseparable triples
inside a new six-cycle deck.  Its live route is therefore a new finite
orbit/q1/source construction or a genuine support-at-least-three fusion
theorem, neither of which is claimed here.

## 7. Dependencies

The marker packing and fixed q1 extension are the two frozen theorems in
Section 1.  The unbuffered packet is
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`.
The ordinary lower-colour and upper-colour splice rigidities are respectively
`MATH_THEOREM_K_COLOURED_CYCLE_OPENING_PORT_TRANSVERSAL_AND_SEAM_CAPACITY_20260729.md`
and Lemma 3.3 of
`MATH_THEOREM_K_RESET_RETURN_RAIL_CATALAN_Q1_PACKING_AND_COMPLETE_REVERSAL_HOST_GATE_20260801.md`.
