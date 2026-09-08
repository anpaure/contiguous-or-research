# Complete Boolean pair slices: target-exact fractional stationarity, parity obstruction, and linear leakage

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional integral-rounding no-go and sharp odd-order
positive theorem.  It shows that exact owner and named-target marginals,
connected regular fractional support, and literal stationarity do not imply
bounded-defect one-copy Euler rounding.  The construction is a complete
Boolean interval slice, not the full triangular middle-owner instance.

## 0. The complete pair slice

Fix a set `K` and a disjoint label set

\[
 U=\{1,\ldots,n\},\qquad n\ge3.
\]

Put

\[
 X_i=K\cup\{i\},
 \qquad
 T_{ij}=K\cup\{i,j\}\quad(i<j).                    \tag{0.1}
\]

The literal depth-one trace arcs of owner `T_(ij)` are

\[
 X_i\longrightarrow X_j,
 \qquad
 X_j\longrightarrow X_i.                            \tag{0.2}
\]

Each orientation has two occurrence variants: its head `X_j` or `X_i` may
be marked as the named proper-suffix target, or it may be left unmarked.
Thus the owner bank is the complete rank-two interval above `K`, and the
named target bank is the complete rank-one interval above `K`.

## 1. Exact fractional solution

### Theorem 1.1 (target-perfect stationary fractional point)

For every `n>=3`, the pair-slice system has a fractional selection satisfying

1. every owner `T_(ij)` has total mass one;
2. every named target `X_i` has marked mass one;
3. flow is balanced at every literal state `X_i`; and
4. the positive state support is connected.

#### Proof

For every unordered pair `{i,j}`, give each of the two **marked**
orientations weight

\[
 {1\over n-1},                                      \tag{1.1}
\]

and each of the two **unmarked** orientations weight

\[
 {n-3\over2(n-1)}.                                  \tag{1.2}
\]

The total mass of one orientation is `1/2`, so the two orientations of an
owner have total mass one.  At a state `X_i`, every one of the `n-1`
incident pair owners sends mass `1/2` into `X_i` and mass `1/2` out of
`X_i`; hence flow is balanced.  The marked incoming orientation from each
other state has weight `1/(n-1)`, so the total marked load of `X_i` is one.
Every directed edge has positive total mass, and the complete state graph is
connected. `square`

This point is already exact on the owner and named-target rows.  Its only
fractionality is in choosing the orientation and mark occurrence inside
each owner.

## 2. Owner and target integrality alone is easy

### Proposition 2.1

There is an integral selection using every owner once and every named target
once.

#### Proof

Choose a cyclic ordering of `U`.  Mark and orient the `n` owner edges of the
corresponding Hamilton cycle toward their next cyclic vertex.  Every
`X_i` is then the marked head exactly once.  Select an arbitrary unmarked
orientation for every remaining owner. `square`

Thus neither the owner partition nor the exact named-target bank causes the
obstruction below.

## 3. Even slices have unavoidable linear Euler defect

For an integral one-copy owner selection, write

\[
 b_i=\operatorname{out}(X_i)-\operatorname{in}(X_i). \tag{3.1}
\]

### Theorem 3.1 (complete-slice parity obstruction)

If `n` is even, every integral one-copy owner selection satisfies

\[
 \boxed{b_i\equiv1\pmod2\qquad(i\in U).}            \tag{3.2}
\]

Consequently:

1. no integral selection is stationary;
2. every directed-trail decomposition uses at least `n/2` trails;
3. at least `n/2` added arcs are required to obtain an Euler circuit; and
4. at least `n/2-1` added arcs are required to obtain one open Euler trail.

All four conclusions remain true after imposing exact use of every named
target.

#### Proof

The selected arcs orient the complete graph `K_n`.  Therefore

\[
 b_i=2\operatorname{out}(X_i)-(n-1).
\]

When `n` is even, `n-1` is odd, proving (3.2).  Hence every one of the `n`
states has nonzero odd imbalance.  Since the imbalances sum to zero,

\[
 \sum_i(b_i)_+={1\over2}\sum_i|b_i|\ge {n\over2}.   \tag{3.3}
\]

One directed trail accounts for at most one unit of positive endpoint
imbalance, proving item 2.  An added directed arc reduces the positive
imbalance by at most one.  A circuit has zero endpoint allowance and an
open trail has positive endpoint mass one, proving items 3 and 4.  Marking
an arc changes no endpoint, so the exact target rows do not affect the
argument. `square`

### Corollary 3.2 (no generic TU or regular-factor rounding)

The combined owner/target/state-balance constraint matrix for this family is
not totally unimodular.  More strongly, the following data do not imply
bounded-defect integral rounding:

* an integral right-hand side;
* exact fractional owner and target loads;
* connected positive support;
* complete regular state-transition support; and
* separate integral feasibility of the owner/target projection.

Indeed Theorem 1.1 supplies all the fractional hypotheses, Proposition 2.1
supplies the separate integral projection, and Theorem 3.1 gives an
unbounded `n/2-1` Euler repair cost.  In particular, no network-flow,
regular-bipartite-factorization, or denominator-clearing theorem using only
those hypotheses can prove the desired rotor rounding.

## 4. Orientation exchanges cannot repair parity

### Proposition 4.1 (exchange invariant)

Reversing any collection of selected pair-slice arcs changes each affected
imbalance by an even integer.  Changing marked/unmarked status changes no
imbalance.  Hence no sequence of length-preserving exchanges inside the
pair-slice menus can repair (3.2).

If owner deletions are allowed, at least `n/2-1` owners must be deleted
before the remaining oriented graph can have the boundary of one open Euler
trail.

#### Proof

Reversing `X_i->X_j` changes `b_i` by `-2` and `b_j` by `+2`.  Thus all
state parities are invariant.  Deleting one owner edge toggles degree parity
at only its two endpoints.  To reduce `n` odd states to at most two requires
at least `(n-2)/2` deletions. `square`

Thus a successful absorber for an even slice must use arcs outside the
frozen orientation menus; internal `C4`-style orientation switches cannot
help.

## 5. Exact leakage requirement inside a larger chronology

Suppose the complete even pair slice is embedded in a larger selected trace
system.  Call an incidence at a state `X_i` **external** if it belongs to an
arc not among the selected pair-slice orientations.  Count an arc twice if
both endpoints are pair-slice states.

### Theorem 5.1 (linear parity leakage)

If the final selected chronology is balanced at every `X_i`, then the total
number of external incidences at the slice states is at least `n`.  Hence at
least `n/2` external arcs meet the slice.

If the final chronology is allowed to be one open Euler trail whose two
endpoints may lie in the slice, the corresponding bounds are `n-2`
external incidences and `(n-2)/2` external arcs.

#### Proof

Modulo two, orientation is irrelevant: the divergence parity at a vertex is
its selected incident-degree parity.  The internal pair slice contributes
degree `n-1`, which is odd at every `X_i`.  Balance therefore requires an odd
number of external incidences at every one of the `n` states.  An external
arc contributes to at most two slice states.  For one open trail, at most
the two endpoint states may retain odd boundary. `square`

This is the exact quantified obstruction exported by an even complete pair
slice: any global owner/target rounding must provide linear cross-slice
parity leakage.  A bounded local portal bank cannot isolate and repair such
a slice.

## 6. Odd slices are exactly positive

### Theorem 6.1 (odd-order one-component selector)

If `n` is odd, there is an integral selection which

1. uses every owner exactly once;
2. uses every named target exactly once;
3. is balanced at every literal state; and
4. has one connected Euler component.

#### Proof

Identify `U` with `Z_n` and orient `{i,j}` from `i` to `j` exactly when

\[
 j-i\in\{1,2,\ldots,(n-1)/2\}\pmod n.              \tag{6.1}
\]

This cyclic tournament has indegree and outdegree `(n-1)/2` at every
state.  Mark precisely the arcs

\[
 i\longrightarrow i+1\pmod n.                       \tag{6.2}
\]

They form a directed Hamilton cycle, so every target is the marked head
once.  The whole selected tournament contains that spanning cycle, hence is
connected; balance and Euler's theorem give one Euler circuit. `square`

The even obstruction is therefore a sharp parity phenomenon on this
complete slice, not a failure of the local Boolean trace geometry.

## 7. Consequence for the triangular rotor programme

The theorem does not refute the special triangular middle-layer instance:
that global system has many cross-core transitions which may supply the
linear leakage required by Theorem 5.1.  It does prove that the newly closed
fractional stationary trace gate cannot be rounded by any theorem whose
input is only

\[
 \text{exact one-point marginals + regular connected support}.
\]

An all-`k` positive theorem must additionally prove one of the following.

1. the chosen Boolean support has no closed even pair slices;
2. every such slice receives the required linear cross-slice incidence
   bank; or
3. a global parity/Smith certificate vanishes after all owner and target
   choices are made jointly.

This parity row comes before arbitrary-width upper witnesses and the common
cap.  It is an integral chronology obstruction, not a fractional rank or
target-capacity obstruction.

## 8. Dependencies and scope

This theorem strengthens the reversible-menu parity warning in
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`
by simultaneously including

* a complete Boolean pair-owner interval;
* exact named-target marginals;
* a connected exact fractional circulation; and
* a sharp odd-order positive construction.

It does not claim that a closed even slice is forced in every triangular
carrier, nor that its linear leakage is expensive relative to the
exponential owner bank.  No OR-word upper or lower bound follows directly.
