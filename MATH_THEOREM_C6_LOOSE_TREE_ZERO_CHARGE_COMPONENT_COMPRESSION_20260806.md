# Prepared Boolean C6 ports compress arbitrarily many factor cycles at zero length

## Status

The symmetric vortex halo is now known to have a simple spanning
owner/root `2`-factor, but its number of cycles is uncontrolled.  This note
shows that an `O(1)`-cycle theorem is not necessary.  If the factor contains
an edge-disjoint loose tree of prepared Boolean-C6 ports, the exact
three-way splice merges its cycles three at a time without inserting a
source letter.  An arbitrary number of initial cycles is reduced to one or
two.

The result is an exact topological reduction.  It uses the literal OR,
ticket, and capped-age C6 tensor proved in
`MATH_THEOREM_THREE_WAY_C6_VORTEX_STATE_SPLICE_20260806.md`.  It does not
prove that a coloured halo factor contains the required loose connector
tree.  That protected planting statement replaces the former Hamilton-halo
gate.

## 1. Prepared portals and their auxiliary hypergraph

Let `F` be a cyclic source factor with cycle components

\[
                         \mathcal C=\{C_1,\ldots,C_s\}.  \tag{1.1}
\]

A **prepared C6 port** consists of one cut in each of three distinct
components, together with the common-core, three-label collar, occurrence
tickets, and capped-age data of the exact three-way C6 splice theorem.
Applying the port cyclically reassigns the three right tails.  It preserves
all protected local OR occurrences and joins the three components into one.

For a serial family, require in addition that every nonconstant one-sided
run or gap used by a later port reaches the required cap inside that port's
private collar (and retain the constant-coordinate flags separately), and
that every protected crossing ticket is local to the collar or has a named
witness disjoint from all other cuts.  Call such a port **serially sealed**.
This condition prevents a remote earlier rethread from changing a later
port's capped-age or ticket input even though its literal collar is
untouched.

Assume different prepared ports use disjoint source collars.  Define the
auxiliary `3`-uniform hypergraph `A` on vertex set `mathcal C` by putting
`{C_i,C_j,C_k}` in `E(A)` for every prepared port on those components.

A sequence `e_1,...,e_m` of hyperedges is a **loose connector tree** if,
after a suitable ordering,

\[
 |e_1|=3,
 \qquad
 \left|e_t\cap\bigcup_{u<t}e_u\right|=1
       \quad(2\le t\le m).                              \tag{1.2}
\]

It spans exactly `2m+1` component vertices.

## 2. Zero-charge component compression

### Theorem 2.1 (loose-tree fusion)

Let `e_1,...,e_m` be a loose connector tree of pairwise collar-disjoint,
serially sealed prepared C6 ports.  Applying the ports in the order (1.2)
merges all
`2m+1` original factor cycles indexed by their vertex union into one cyclic
source component.  Throughout the sequence:

1. no source position is inserted or deleted;
2. every protected boundary OR occurrence and its ticket is transported
   bijectively;
3. the owner and immediate-lower resource multisets are unchanged; and
4. every required positive run and zero gap remains legal.

#### Proof

The first port acts on three distinct cycles and its tail permutation is a
three-cycle, so it merges them into one.  Suppose the first `t-1` ports
have merged all components in their vertex union into one cycle.  By
(1.2), port `e_t` has one cut in that merged cycle and its other two cuts
in two untouched cycles.  The three cuts therefore again lie in distinct
current cycles, and the C6 tail three-cycle merges them into one.

Disjointness of the physical collars means an earlier splice changes
neither the literal letters nor the boundary tensor at a later port; it
only changes the global cycle containing that port.  Serial sealing ensures
that the same is true of the capped-age inputs and every nonlocal protected
ticket.  The four preservation claims therefore follow at every induction
step from the exact C6 splice theorem. \(\square\)

### Corollary 2.2 (one-or-two component target)

If the auxiliary port hypergraph contains

* a loose spanning tree when `s` is odd, or
* a loose tree spanning `s-1` vertices when `s` is even,

then the factor can be rethreaded at zero length to have respectively one
or two components, with no loss of any protected local ticket.

Thus a bounded terminal component charge is enough to handle parity; it
does not grow with the original number of cycles.

#### Proof

A `3`-uniform loose tree has an odd number `2m+1` of vertices.  Apply
Theorem 2.1.  In the even case the one unspanned cycle remains as the second
component. \(\square\)

## 3. Exact parity boundary

Every three-way C6 tail reassignment is a `3`-cycle and hence an even
permutation.  Consequently the parity of the number of cyclic components
is unchanged by a sequence of C6 splices.  In particular, C6 ports alone
cannot turn an even number of components into one.

Indeed, on the fixed set of source positions a successor permutation with
`c` cycles has sign `(-1)^(N-c)`.  Composing it with an even tail
three-cycle preserves this sign and hence preserves `c modulo 2`.

This is harmless for an additive-constant theorem: Corollary 2.2 leaves at
most two components.  Exact coefficient-one equality would additionally
need either an odd tail trade (the first candidate is a prepared four-way
port), an initially odd factor, or a terminal operation which pays the
single parity charge elsewhere.

## 3.1 The unavoidable collar-volume bound

The loose-tree theorem is not a license to start from an arbitrary
`Theta(N)`-cycle factor when the protected source width grows.  If the
owner width is `h` and the full owner/root boundary tensor is protected,
one cut needs `h-1` source positions on each side.  A three-cut port
therefore occupies at least

\[
                              3(2h-2)=6h-6               \tag{3.1}
\]

private collar positions.  If the factor has `N` source positions and the
loose tree has `m` pairwise collar-disjoint ports, then

\[
                         m\le {N\over6h-6}.               \tag{3.2}
\]

A spanning loose tree has `s=2m+1` component vertices, so necessarily

\[
                         s\le {N\over3h-3}+1.             \tag{3.3}
\]

Thus the theorem replaces an `O(1)`-component hypothesis by the weaker but
still substantive target `s=O(N/h)`, together with a well-distributed
sealed port bank.  It cannot by itself compress a worst-case two-factor
with `Theta(N)` constant-length cycles.  Beating (3.3) would require
overlapping/regenerative collars or a shorter tensor, neither of which is
proved here.

## 4. The revised global topology gate

The old sufficient target was:

> choose the coloured halo factor with `O(1)` cycles.

The strictly weaker sufficient target is now:

> choose any coloured halo `2`-factor together with pairwise
> collar-disjoint, serially sealed prepared C6 ports whose component
> hypergraph contains a
> loose tree spanning all but at most one component.

The second formulation is compatible with a nibble-plus-reservoir proof:
the factor may initially have as many as `O(N/h)` cycles, and the connector
bank can be selected after the factor provided its collars and tickets were
protected.
The remaining mathematical task is therefore a protected C6-port
planting/linkage theorem, not Hamiltonicity of the product halo itself.
