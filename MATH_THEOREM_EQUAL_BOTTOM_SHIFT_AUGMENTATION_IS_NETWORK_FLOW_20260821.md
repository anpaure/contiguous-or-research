# Equal-bottom product-SCD shift augmentation is an exact integral network flow

**Status (2026-08-21).** Every statement below is proved.  After the
unequal-bottom endpoint matching is fixed, the remaining adaptive
constant-shift problem on equal-bottom product-SCD rectangles is not a new
rounding obstruction.  For every fixed offset `q`, every set of retained
source ranks, and every integral residual phase-color ledger, its exact
maximum-weight augmentation is a one-commodity min-cost flow and therefore
has an integral optimum.

This theorem does **not** prove that the residual capacities are large enough
to recover all equal-bottom rectangles.  It also does not couple choices
across different offsets and does not realize tokenwise containments by
common cyclic orders.  It removes only the fixed-`q`, equal-bottom
integrality gate.

## 1. Equal-bottom rectangles and constant shifts

Let `A,B` be disjoint `b`-sets, let `b=2h+1`, and fix symmetric chain
decompositions of their Boolean lattices.  There are

\[
 m_d=c_d^2,
 \qquad
 c_d={b\choose d}-{b\choose d-1},                  \tag{1.1}
\]

ordered pairs of chains whose two bottom ranks both equal `d`.

Fix an upper offset `q`.  In one such equal-bottom chain rectangle, the
rank-`(b+q)` target diagonal has local `A`-ranks

\[
 s=d+q,d+q+1,\ldots,b-d.                            \tag{1.2}
\]

For every `z in {0,...,q}`, the constant-shift map

\[
 s\longmapsto r=s-z                                 \tag{1.3}
\]

is a target-saturating containment matching in that rectangle; all its
edges have phase color `z`.

Let `J subseteq {0,...,b}` be the source ranks retained by the application.
If a level-`d` chain pair is assigned shift `z`, retain from (1.3) exactly
the edges whose source rank lies in

\[
 I_{d,z}=J\cap[d+q-z,b-d-z].                        \tag{1.4}
\]

Their number, and hence their arbitrary nonnegative objective weight in the
coverage problem, is

\[
 w_{d,z}=|I_{d,z}|.                                 \tag{1.5}
\]

More general integer weights may be substituted below without changing the
integrality statement.

## 2. Exact prefix formulation

Suppose an already chosen matching leaves a nonnegative integral residual
capacity `R_(r,z)` at every retained source rank `r in J` and color
`0<=z<=q`.  Let `x_(d,z)` be the number of the `m_d` equal-bottom chain
pairs assigned shift `z`.  We omit a variable when `I_(d,z)` is empty.

The supply constraints are

\[
 \sum_zx_{d,z}\le m_d.                              \tag{2.1}
\]

At a fixed source rank and color, a level-`d` assignment contributes one
edge exactly when

\[
 d\le t_z(r):=\min(r-q+z,b-r-z).                   \tag{2.2}
\]

Thus the residual color constraints are the prefix inequalities

\[
 \sum_{0\le d\le\min(h,t_z(r))}x_{d,z}
 \le R_{r,z}
 \qquad(r\in J, 0\le z\le q),                    \tag{2.3}
\]

with an empty left side when `t_z(r)<0`.  Conversely, (2.1)--(2.3) are
sufficient: choose any `x_(d,z)` labelled chain pairs at every level and
use (1.3).  Different chain pairs have disjoint sources and targets, and
one shift is used per pair.

Consequently the exact constant-shift augmentation problem is

\[
 \max\sum_{d,z}w_{d,z}x_{d,z}
 \quad\hbox{subject to (2.1)--(2.3),}\quad x\ge0.    \tag{2.4}
\]

## 3. Network representation and integrality

Put `M=sum_d m_d`; it will serve as a finite infinity.  For every color
`z` and `0<=k<=h`, define

\[
 B_{z,k}=\min\Bigl(
  \{R_{r,z}:r\in J,\ \min(h,t_z(r))=k\}\cup\{M\}
 \Bigr).                                            \tag{3.1}
\]

Ranks with `t_z(r)<0` impose no constraint because no equal-bottom variable
contributes there.

### Theorem 3.1 (exact integral flow)

The feasible vectors in (2.1)--(2.3) are in weight-preserving
correspondence with flows in the following acyclic network.

* Send exactly `M` units from a source `s` to a sink `t`.
* For every level `d`, add `s -> D_d` with capacity `m_d`.  Add
  `D_d -> t` with capacity `m_d` and cost zero; this carries unused supply.
* For every color `z`, create a chain

  \[
   Z_{z,0}\longrightarrow Z_{z,1}\longrightarrow\cdots
   \longrightarrow Z_{z,h+1}\longrightarrow t.    \tag{3.2}
  \]

  Give `Z_(z,k) -> Z_(z,k+1)` capacity `B_(z,k)` for `0<=k<=h`,
  and give the last edge to `t` capacity `M`.
* Whenever `I_(d,z)` is nonempty, add
  `D_d -> Z_(z,d)` with capacity `m_d` and cost `-w_(d,z)`.

The flow on `D_d -> Z_(z,d)` is exactly `x_(d,z)`.  Hence (2.4) has an
integral optimum whenever `m_d,R_(r,z)`, and the weights are integral.

#### Proof

Because the total capacity of the edges `s -> D_d` is exactly `M`, every
one is saturated.  Conservation at `D_d` says that its assigned flow plus
its unused flow is `m_d`, which is (2.1).

At the edge `Z_(z,k) -> Z_(z,k+1)`, conservation gives the exact flow

\[
 \sum_{d=0}^k x_{d,z}.                              \tag{3.3}
\]

Its capacity `B_(z,k)` is precisely the minimum of all residual bounds in
(2.3) having prefix index `k`; if there is no such bound, capacity `M` is
vacuous.  Therefore the chain capacities are equivalent to every inequality
in (2.3).  This constructs a flow from every feasible `x`, and reading the
choice-edge flows reverses the construction.  The only nonzero costs are
the choice-edge costs, so the objective is preserved.

All network capacities and demands are integral.  The integral-flow theorem
therefore supplies an integral optimum.  \(\square\)

### Corollary 3.2 (no equal-bottom rounding loss)

For a fixed `q`, any fractional constant-shift augmentation of value `V`
against an integral residual color ledger can be replaced by an integral
augmentation of value at least `V`.  In particular, any loss at this stage
comes from an actual residual-capacity cut, not from non-total-unimodularity
of the larger all-rectangle shift matrix.

## 4. Exact residual-capacity gate

The preceding theorem turns the equal-bottom question into an ordinary
min-cut problem.  To prove `o(W_b)` aggregate loss in the full DCC band, it
would now suffice at the tokenwise level to construct the unequal-bottom
matching and residual ledgers so that the network (3.2) sends all but
`o(W_b)` weighted equal-bottom supply after summing over the offsets.

That cut estimate is not proved here.  Nor does a fixed-`q` flow choose one
coherent cyclic order and counter origin per physical atom.  The independently
proved common-origin diagonal obstruction shows that even the `q=1`
product-SCD edges require `Omega(W_b/b)` switches or deletions before such a
physical lift.  Thus the remaining gates, in order, are:

1. a quantitative residual-capacity/min-cut bound, preferably simultaneous
   over the DCC offsets;
2. cross-offset coinstantiation of the token choices; and
3. an `o(W_b)` labelled-order/common-origin switch or absorption theorem.

Theorem 3.1 proves that fractional-to-integral rounding inside the adaptive
equal-bottom constant-shift core is no longer one of those gates.

