# Clocked singleton arms compile product cells into legal middle rails

**Date:** 2026-08-13  
**Status:** unconditional local compiler and a decisive no-go for its naive
application to the recursive slab atlas.  A singleton-increment
product-chain arm of length at most `q-2` can be planted unchanged inside
one period-`q+2` owner rail while preserving a simple
immediate-lower/owner/upper triple.  However many optimized slab-fan atoms
have longer arms, and the fully legal short-atom sharing graph is empty in
the first audited large instance.  Thus this local atom does not compile
that atlas at coefficient one.

## 1. The clocked arm

Let `q>=4`, let the owner rank be `R`, and assume `R+2<=k`.  Put

\[
                         N=q+2.                              \tag{1.1}
\]

Choose disjoint sets

\[
 K,E,X=\{x_1,\ldots,x_L\},Y=\{z_1,\ldots,z_{N-L}\},        \tag{1.2}
\]

with

\[
 |K|=\beta,\qquad |E|=R-q-\beta,qquad 0\le L\le q-2.     \tag{1.3}
\]

Thus `F=K dotcup E` has rank `R-q`.  Use the cyclic source word

\[
 A_i=
 \begin{cases}
  K\cup\{x_i\},&1\le i\le L,\\
  F\cup\{z_{i-L}\},&L<i\le N.
 \end{cases}                                               \tag{1.4}
\]

The first `L` positions are the **payload arm** and the remaining positions
are guards.

### Theorem 1.1 (clocked singleton arm)

The length-`q` cyclic source windows of (1.4) are `N` distinct rank-`R`
sets forming a simple Johnson cycle.  The width-`q-1` and width-`q+1`
rows are separately simple of ranks `R-1` and `R+1`.  Every toggle
coordinate has a positive owner run of exactly `q`, so the owner trace is
positive-resident at depth `q-1`.

Every source interval contained wholly in the payload arm has literal
union

\[
                         K\cup\{x_i,x_{i+1},\ldots,x_j\}.   \tag{1.5}
\]

#### Proof

Because `L<=q-2`, every cyclic interval of `q-1` source positions contains
a guard.  Hence every interval of width at least `q-1` emits every
coordinate of `F`.  It also contains precisely the corresponding cyclic
interval of the `N` unique toggle labels.  At widths `q-1,q,q+1` its
union is therefore `F` plus respectively `q-1,q,q+1` toggles, proving the
ranks and simplicity.  Shifting a `q`-window deletes its oldest toggle and
inserts the next toggle, while `F` stays fixed, so the owners form a simple
Johnson cycle.  A toggle occurs in exactly the next `q` owner windows,
proving positive residence.  Inside the payload arm no guard occurs, so
only `K` and the displayed consecutive toggles are emitted; this is (1.5).
\(\square\)

The zero gaps of the toggles have length two, so no two-sided residence is
claimed.

## 2. Product-cell compilation

Let

\[
 C_0\subset\cdots\subset C_{a-1},\qquad
 D_0\subset\cdots\subset D_{b-1}                       \tag{2.1}
\]

be saturated Boolean chains on disjoint coordinate halves, with singleton
increments `c_i=C_i-C_(i-1)` and `d_j=D_j-D_(j-1)`.  Fix a base

\[
                         K=C_{i_0}\cup D_{j_0}.             \tag{2.2}
\]

For dimensions `A,B`, use the singleton arm

\[
 c_{i_0+A-1},\ldots,c_{i_0+1},
 d_{j_0+1},\ldots,d_{j_0+B-1}.                             \tag{2.3}
\]

It has length

\[
                         L=A+B-2.                           \tag{2.4}
\]

Assume the base rank obeys

\[
                         |K|\leq R-q.                       \tag{2.5}
\]

Choose `E` and all guard toggles from the complement of `K` and the arm
increments.  The total packet support then has rank `R+2`, so the standing
hypothesis `R+2<=k` is exactly the required supply condition.

### Corollary 2.1 (clocked product rectangle)

If `A+B-2<=q-2`, the arm (2.3) may be used as `X` in Theorem 1.1.  For
every local cell `(i,j)` with `0<=i<A`, `0<=j<B` and `(i,j)!=(0,0)`, one
payload interval has union exactly

\[
                         C_{i_0+i}\cup D_{j_0+j}.           \tag{2.6}
\]

Its width is `i+j`, except that axis cells use their corresponding nested
subarm interval.  The base cell `K` itself is not supplied unless it is
marked at an allowed singleton source position by a separate decoration.

#### Proof

Order the left increments in decreasing index and the right increments in
increasing index.  The interval starting at `c_(i_0+i)` and ending at
`d_(j_0+j)` contains exactly the increments needed to enlarge the base to
(2.5).  Pure axis cells use the appropriate subinterval on their arm.
Equation (1.5) gives the value.  The base has no toggle and hence no
position in the arm.  \(\square\)

The useful feature is separation of roles: `K` is the immutable payload
base, `E` lifts every owner window to rank `R` but never contaminates an
arm cell, and the toggles provide both the product increments and the
owner clock.

## 3. Exact atom-count gate

Take any product-SCD atlas which partitions its assigned target cells into
clockable atoms of the form in Corollary 2.1.  Let `A_atlas` be the number
of nonempty atoms, counted with the multiplicities of their product-chain
types, and let `B_base` be the family of assigned base cells not supplied
elsewhere.  Replacing every atom by its clocked rail uses exactly

\[
                         (q+2)A_{\rm atlas}                  \tag{3.1}
\]

source positions and produces the same number of rank-middle owner
occurrences.  All nonbase assigned targets remain literal lower cells.

Consequently the first coefficient-one condition for this compiler is

\[
                         (q+2)A_{\rm atlas}+|B_{\rm base}|
                         \le W+O(q),                        \tag{3.2}
\]

together with an owner-disjoint selection of the resulting rails.  Equation
(3.2) is only a necessary physical charge when bases are paid by singleton
letters; sharing or programming bases can lower the second term.

For the recursive diagonal-fan slab atlas, truncated terminal fans may have
arm length as large as `2d-1`, not merely `q-1`.  Hence many are outside
Corollary 2.1.  Short boundary cases have two exact repairs:

1. split off one outer-diagonal increment/cell so every residual arm has
   length at most `q-2`; or
2. use a `q1`-preserving schedule whose sole in-arm emission is at the
   terminal arm phase, and assign only intervals avoiding that phase to the
   guard-free payload.

Either repair charges a named subset of the already isolated outer global
boundary row.  Long fans require an actual multi-atom split or a different
clock; an exterior seam cannot repair an internal overlong arm.

## 4. Scope

The theorem is packet-local.  It proves neither (3.2), nor global
owner/lower/upper disjointness, nor an integral packet factor, nor fusion
into one linear word.  It does, however, remove the rank obstruction from
`MATH_THEOREM_PRODUCT_SCD_CARRIER_RECTANGLE_HYBRID_AND_SINGLE_BOUNDARY_ROW_20260813.md`:
the old intact atoms had no rank-`R` internal `q`-windows, whereas every
position of the clocked replacement belongs to a legal rank-`R` owner
window.

## 5. Exact remote atom-count census

The script
`analyze_clocked_product_scd_atom_count.py` replays the exact optimized
slab recurrence and charges one period-`q+2` rail to every atom.  Substantial
instances were evaluated only on `h100`.

\[
\begin{array}{c|c|c|c|c|c}
k&q&R^{\rm SF}/W&A_{\rm atlas}/W&(q+2)A_{\rm atlas}/W\\ \hline
201&10&0.8660069&0.1006979&1.2083748\\
301&12&0.9083389&0.0852026&1.1928369\\
401&14&0.8807844&0.0710612&1.1369791\\
561&16&0.9603361&0.0650121&1.1702174\\
641&17&0.9727519&0.0613168&1.1650192\\
721&18&0.9782058&0.0581337&1.1626746
\end{array}                                                \tag{5.1}
\]

Thus the local compiler is not by itself a coefficient-one construction:
the one-rail-per-atom charge exceeds `W` in every tested case.  The result
is nevertheless quantitatively sharp enough to identify the required
sharing.  At scale `q=Theta(sqrt k)`, approximately one atlas arm must be
assigned to each endpoint ticket of a shared rail, rather than allocating
a private rail to every arm.

The exact next combinatorial object is therefore a cyclic arm-packing
problem governed by Proposition 3.3 of
`MATH_THEOREM_PERIOD_Q_PLUS_2_COMPLETE_NESTED_TICKET_PORTAL_AND_EQUITABLE_CHAIN_GATE_20260813.md`:
the endpoint thresholds of all arms sharing a packet must be translates of
one common capped-age word for every core coordinate.

## 6. Exact shared-rail obstruction at `k=201`

An H100 replay of the optimized recurrence at `k=201` (`q=10,N=12`) gives

\[
 A_{\rm atlas}/W=0.100693,qquad
 A_{\rm long}/W=0.033282,                                 \tag{6.1}
\]

where `A_long` counts arms longer than `q-1`; the maximum arm length is
`17=2d-1`.  These atoms cannot be contiguous payload arcs of a period-12
clock.

On the remaining short atoms, successively imposing the true pair
conditions gives maximum-matching sizes

\[
\begin{array}{c|c}
\text{condition}&\text{matching size}/W\\ \hline
\text{cyclic superstring only}&0.005094\\
\text{plus shared-core rank feasibility}&0.004869\\
\text{plus exact shared-core equality}&0.002735\\
\text{plus arm-toggle/shared-core disjointness}&0\\
\text{plus per-coordinate `(q-1)` hit/avoid feasibility}&0.
\end{array}                                                \tag{6.2}
\]

The decisive zero occurs one row earlier than the schedule test: every
cyclic, exact-core candidate pair has at least one proposed arm-toggle
coordinate already lying in the other atom's base and hence in the shared
core.  Such a coordinate cannot be a private toggle of the rank-`R` clock.
The final hit/avoid row is an additional physical condition but is vacuous
on this empty graph.  In a nonempty instance it would require every core
coordinate omitted by an assigned target to avoid that target's whole
payload arc while still hitting every `(q-1)` window.

In addition, `0.012871W` atoms are already
singleton-infeasible, and weighted grid copies totalling `0.010292W` admit
no exact packet cover in this architecture.

Thus the unsplit shared-clock compiler is ruled out before owner-factor or
fusion questions.  The local Theorem 1.1 remains valid and may be reused
in another atlas, but the product-SCD slab route must be split/rebuilt or
abandoned.

The durable replay is
`analyze_slab_atom_arm_lengths_and_pairing.py`.  It chooses, among
minimum-source-cost slab orientations, the one with minimum atom count;
extracts the literal directed arm labels; and runs exact NetworkX maximum
matching separately in every product-grid type before weighting by the
product-SCD multiplicities.  The substantial run was performed only on
`h100`.
