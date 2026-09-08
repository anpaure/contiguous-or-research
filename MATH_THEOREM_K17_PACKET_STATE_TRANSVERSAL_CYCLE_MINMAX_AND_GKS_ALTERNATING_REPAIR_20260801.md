# `k=17`: packet-state transversals, exact cycle/Hamilton min--max, and alternating GKS repair

Date: 2026-08-01  
Scope: finite owner-attachment and changing-owner **support** optimization
over a static age-flag factor.  No owner chronology is preselected, no SAT
encoding is constructed, and voltage and upper-safe opening remain separate.

## 0. Verdict

The frozen static GKS flag factor has one packet rooted at every rank-eight
orbit.  A packet has exactly nine quotient-incidence attachment states when
parallel phases are retained: a state chooses a relative phase and one
rank-nine owner orbit containing the rotated packet root.  Choosing one
state per packet and one state per owner orbit is therefore a perfect
matching in a 9-regular packet/owner multigraph.

Changing-owner compatibility must be built between these **complete
states**, not between packet types.  For a selected state transversal `Z`,
split every state into a tail and a head copy and use the literal age-update
arcs.  If `delta(Z)` is the maximum Hall deficiency of this split graph,
then, provided at least one state transversal survives pruning,

\[
 \boxed{
 M_{\rm cc}=1430-
 \min_Z\max_{X\subseteq Z}
       \bigl(|X|-|N_Z^+(X)|\bigr)}                   \tag{0.1}
\]

is the maximum number of arcs in a directed path/cycle packing after the
owner attachments are optimized.  A full directed cycle cover exists
exactly when the minimum deficiency is zero.

Hamilton support has an equally exact ordered-Hall form.  Choose a closing
arc `q->r`, put `r` first and `q` last, and retain only arcs increasing a
total order.  The selected closing arc extends to a Hamilton cycle exactly
when the forward deficiency is one.  Minimizing that deficiency jointly
over the state transversal, closing arc, and order is an exact Hamilton
min--max, not a connectivity heuristic.

For computation, the same object has a compact state-expanded assignment
model with lazy Hall and directed subtour cuts.  Its oracles are bipartite
matching, residual min-cut, and directed cut separation; it does not
duplicate the owner-cycle SAT model.

If a fixed static factor has dead state rows, open the GKS rank-six/rank-eight
containment matching rather than changing packets independently.  Every
other valid controlled surgery differs from the frozen one by alternating
cycles and right-to-right alternating paths.  A shortest path in the GKS
exchange digraph is the exact minimum central-layer switch which inserts a
desired containment edge.  Such a switch is only a **candidate** chronology
repair: its affected low flags and complete age partitions must be
recertified before its new state and arc columns enter (0.1).

## 1. Complete attachment states

Let `mathcal K` be the 1430 packets of one literal static flag factor.  For
the frozen certificate this is

```text
scratch/threadA_k17_gks_full_static_flags_20260801.tsv
SHA256 5fc20be6e76a5ca0336ce9bc51e252d2d597f2ec2ea9ff96a54264eb050cf886
```

For `K in mathcal K`, write

\[
 F_K=(c_K;C_{K,0},C_{K,1},C_{K,2};Q_K),
 \qquad Q_K=C_{K,0}\mathbin{\dot\cup}C_{K,1}
                         \mathbin{\dot\cup}C_{K,2}, \tag{1.1}
\]

where `Q_K` is the fixed rank-eight root representative.  The `Q_K` run
through all 1430 rank-eight orbits once.

Let `mathcal O_9` be the 1430 rank-nine owner orbits and fix one
representative `T_O` of each.  An **attachment state** is a triple

\[
                         s=(K,O,a)                    \tag{1.2}
\]

with `a in Z_17` and

\[
                         \rho^aQ_K\subset T_O.        \tag{1.3}
\]

It carries the literal partition

\[
 C_i(s)=\rho^aC_{K,i}\quad(0\le i<3),
 \qquad C_3(s)=T_O-\rho^aQ_K.                        \tag{1.4}
\]

The last class is a singleton, so (1.4) has type `c_K`.  Write `kappa(s)=K`
and `omega(s)=O`.

Different alignments `a` between the same packet and owner remain distinct
states.  The free cyclic action and the nine physical rank-nine supersets of
a rank-eight set imply

\[
                 |\{(O,a):(K,O,a)\text{ satisfies (1.3)}\}|=9. \tag{1.5}
\]

Thus the complete fixed-factor state set has 12,870 elements.  Its
packet/owner incidence multigraph is 9-regular on both shores and therefore
has a perfect matching before changing-owner compatibility is imposed.
Write `Omega` for this state set.

A **state transversal** is a binary vector `z` satisfying

\[
 \sum_{s:\kappa(s)=K}z_s=1\quad(K\in\mathcal K),
 \qquad
 \sum_{s:\omega(s)=O}z_s=1\quad(O\in\mathcal O_9).  \tag{1.6}
\]

Let `mathfrak Z` be this family and `S_z={s:z_s=1}`.  Parallel states are
separate columns in (1.6).  If later guards delete states, the first exact
obstruction is ordinary packet/owner Hall:

\[
 |N_{\mathcal O_9}(R)|\ge |R|
 \qquad(R\subseteq\mathcal K).                       \tag{1.7}
\]

## 2. Literal changing-owner arcs

For states `s,t` and `v in Z_17`, rotate the whole target state by `v`.
There is a labelled changing-owner arc

\[
                         e=(s,t,v)                    \tag{2.1}
\]

when the following hold.

1. The two packet and owner colours are distinct.
2. With `alpha` the unique member of `C_3(s)`, there is a `beta` such that

   \[
        \rho^vT_{\omega(t)}=T_{\omega(s)}-\{\alpha\}+\{\beta\}. \tag{2.2}
   \]

3. The literal survivor inclusions hold:

   \[
             \rho^v C_{i+1}(t)\subseteq C_i(s)
             \qquad(0\le i<3).                       \tag{2.3}
   \]

Equations (2.2)--(2.3), together with the two complete partitions, force
the target age-zero class to be the new coordinate plus every refreshed
retained coordinate.  Hence they are necessary and sufficient for one
literal changing-owner update.  In particular the lower `q1` colour is

\[
 T_{\omega(s)}\cap\rho^vT_{\omega(t)}
       =C_0(s)\cup C_1(s)\cup C_2(s)=\rho^aQ_K.       \tag{2.4}
\]

Let `mathcal A` be the labelled arc multiset and let `D` be its directed
support after forgetting `v`.  Parallel voltages must be restored after a
support cycle is selected.  By item 1, `D` is the loop-free quotient support
used as a Hamilton relaxation.  A legal nonzero-voltage state self-loop can
lift to a physical 17-cycle; if arbitrary disconnected physical cycle
covers are the objective, include those loops and apply the same matching
theorem.  They are excluded here because they cannot belong to a
1430-vertex quotient Hamilton cycle and can mask its dead rows.

This construction fixes the crucial quantifier order:

\[
 \text{complete static flag} longrightarrow
 \text{owner attachment state} longrightarrow
 \text{literal arc}.                                 \tag{2.5}
\]

A fresh survivor partition chosen independently for each incident arc is
not composable and is excluded.

## 3. Exact optimized cycle-cover deficiency

For `z in mathfrak Z`, form the split bipartite graph

\[
 B_z=((S_z)_L,(S_z)_R;E_z),                          \tag{3.1}
\]

where `s_L t_R` is present exactly when `s->t` is in `D`.  Put

\[
 \delta(z)=\max_{X\subseteq S_z}
      \left(|X|-|N_{B_z}(X)|\right).                 \tag{3.2}
\]

### Theorem 3.1 (state-transversal cycle-cover min--max)

Assume `mathfrak Z` is nonempty.  The maximum number of changing-owner
support arcs which can be selected
with distinct tails and heads, jointly over all packet/owner state
transversals, is

\[
 \boxed{
 M_{\rm cc}=1430-\Delta_{\rm cc},
 \qquad
 \Delta_{\rm cc}=\min_{z\in\mathfrak Z}\delta(z).}   \tag{3.3}
\]

In particular a directed cycle cover of all packets and all owner orbits
exists if and only if `Delta_cc=0`.

#### Proof

For fixed `z`, a matching in (3.1) selects at most one outgoing and at most
one incoming arc at each selected state.  The bipartite deficiency form of
Hall's theorem says its maximum size is `1430-delta(z)`.  Maximizing over
the state transversals proves (3.3).  A matching of size 1430 gives every
selected state indegree and outdegree one, hence a disjoint union of
directed cycles.  Conversely every directed cycle cover is such a perfect
matching. `square`

The sharp fixed-factor failure alternative is:

* `mathfrak Z` is empty after state pruning; or
* for every `z in mathfrak Z` there is a selected state family `X` with

  \[
                   |N_{B_z}(X)|\le |X|-1.            \tag{3.4}
  \]

Local dead rows are the singleton shadows of (3.4).  They are useful early
cuts but are not the only obstruction.

## 4. Exact Hamilton-support min--max

Fix `z`, a support arc `e_*:q->r` with `q,r in S_z`, and a total order
`prec` of `S_z` whose first state is `r` and last state is `q`.  Keep only
support arcs increasing `prec`, split them as in (3.1), and write the result
as `B_(z,e_*,prec)^+`.  Define

\[
 \delta^+(z,e_*,\prec)=
 \max_{X\subseteq S_z}
 \bigl(|X|-|N_{B^+_{z,e_*,\prec}}(X)|\bigr).          \tag{4.1}
\]

### Theorem 4.1 (state-transversal ordered-Hall theorem)

There is a directed Hamilton support cycle on one state of every packet and
one state of every owner orbit if and only if

\[
 \boxed{
 \Delta_H=min_{\substack{z\in\mathfrak Z, e_*:q\to r\\
                           \prec:\ r\text{ first},q\text{ last}}}
             \delta^+(z,e_*,\prec)=1.}              \tag{4.2}
\]

#### Proof

For fixed data, all arcs in the split graph increase `prec`.  A matching of
size 1429 is therefore a spanning directed path forest with 1429 edges and
hence one Hamilton path.  Its order is necessarily `prec`; adding
`e_*:q->r` closes it.  Hall deficiency is one exactly when that matching
exists.  Conversely, delete any one arc from a Hamilton cycle and use the
resulting path order.  Its 1429 arcs form the required forward matching.
`square`

Theorem 4.1 concerns support only.  For a physical connected lift, choose
one voltage label on every selected support arc and require their sum to be
nonzero in `Z_17`.  A support Hamilton cycle may fail this modular gate.

## 5. Exact assignment model and structural cuts

The min--max has a direct finite optimization model.  Use binary variables
`z_s` for states and `y_(s,t)` for support arcs.  The state equations are
(1.6).  The maximum-support relaxation is

\[
 \begin{aligned}
 \sum_{t:s\to t}y_{s,t}&\le z_s,\\
 \sum_{u:u\to s}y_{u,s}&\le z_s,
 \end{aligned}
 \qquad(s\in\Omega),                                 \tag{5.1}
\]

with objective `max sum y_(s,t)`.  Its integer optimum is (3.3).  Replacing
both inequalities by equalities is the exact cycle-cover feasibility model.

To require one Hamilton cycle, add the directed subtour cuts

\[
 \sum_{\substack{s\to t:\ \kappa(s)\in R\\
                         \kappa(t)\notin R}}y_{s,t}\ge1
 \qquad(\varnothing\ne R\subsetneq\mathcal K).      \tag{5.2}
\]

Because exactly one state of every packet is selected, a proper directed
cycle component has a proper packet set and violates (5.2).  Conversely,
degree equalities plus all cuts (5.2) give one Hamilton cycle.

Useful exact or separating cuts are, in increasing strength:

1. packet/owner Hall cuts (1.7) after any state pruning;
2. local support cuts

   \[
      z_s\le\sum_{t\in N^+(s)}z_t,
      \qquad
      z_s\le\sum_{u\in N^-(s)}z_u;                  \tag{5.3}
   \]

3. selected-state Hall cuts (3.4), returned by a maximum-matching residual
   min-cut; and
4. Hamilton outgoing cuts (5.2), separated by directed min-cut or, at an
   integer cycle cover, by listing its proper cycles.

If the cycle-cover layer is Benders-separated from the state-transversal
master, a Hall witness `X subseteq S_z` has the exact conditional cut

\[
 \sum_{t\in\Gamma^+(X)}z_t
 +|X|\sum_{s\in X}(1-z_s)\ge |X|,                    \tag{5.4}
\]

where `Gamma^+(X)` is the set of **all** state columns reachable from `X`.
When every state of `X` remains selected, (5.4) imposes its Hall row; if any
tail state changes, the big term deactivates this particular witness.  The
joint `z,y` model (5.1) is usually stronger and needs no projected cut.

The natural exact algorithm is therefore:

1. enumerate the nine attachment states of each fixed packet and all literal
   labelled arcs (2.1);
2. prune locally dead states and run packet/owner matching;
3. solve either the joint state/arc master (5.1), or a state-transversal
   master with bipartite matching oracle and conditional cuts (5.4);
4. once deficiency zero is reached, add (5.2) lazily until one cycle remains;
5. finally solve the small parallel-label modular sum gate.

These are matching/min-cut/assignment oracles.  The formulation does not
re-encode the lower flag exact cover or the fixed type word at 1430 owner
positions.

## 6. Opening the GKS surgery by alternating switches

Let

\[
 G_{\rm GKS}=(H,L;E)                                 \tag{6.1}
\]

be the authenticated containment graph whose 286 left vertices are the
rank-eight-start roots and whose 728 right vertices are the GKS rank-six
elements.  The frozen surgery is a matching `M_0` saturating `H`.

All controlled surgeries in this class are exactly the integral points of

\[
 \sum_{\ell:h\ell\in E}g_{h\ell}=1\quad(h\in H),
 \qquad
 \sum_{h:h\ell\in E}g_{h\ell}\le1\quad(\ell\in L),
 \qquad g\ge0.                                      \tag{6.2}
\]

The bipartite matching matrix is totally unimodular, so every vertex of
(6.2) is another literal left-perfect GKS surgery.

### Lemma 6.1 (complete alternating-switch description)

For any two left-perfect matchings `M_0,M`, their symmetric difference is a
disjoint union of:

1. even alternating cycles; and
2. even alternating paths whose two endpoints lie in `L`, one endpoint
   matched only by `M_0` and the other matched only by `M`.

Flipping any such component preserves saturation of every `h in H` and
right injectivity.  Conversely every valid change from `M_0` to `M` is a
sequence of these flips.

#### Proof

Every left vertex has degree zero or two in the symmetric difference,
because both matchings saturate it.  Every right vertex has degree at most
two.  Components are therefore alternating cycles or paths; a path cannot
end on the left and has the stated right endpoints.  Flipping exchanges the
two alternating edge classes and preserves all matching degrees. `square`

For a current matching `M`, form its **right exchange digraph** `E_M` on
`L`: for `M(h)=ell`, put an arc

\[
                   \ell\longrightarrow\ell'
 \quad\text{for every }h\ell'\in E-M.               \tag{6.3}
\]

Thus trivial matched-edge self-loops are absent.  A directed cycle in
`E_M` is an alternating-cycle switch.  A directed path
from a currently matched right vertex to an `M`-unmatched right vertex is an
alternating-path switch: reassign each encountered left root to the next
right vertex.  Its first right vertex becomes unmatched and its last becomes
matched.

### Corollary 6.2 (minimum central repair)

Suppose a dead skip row rooted at `h` can become locally live only when its
rank-six base belongs to a declared set `L_good(h)`.  Ignoring downstream
low-flag conflicts, the minimum number of GKS root reassignments which puts
`h` on a good base is the shortest directed alternating path/cycle in
`E_M` whose first exchange arc is

\[
                  M(h)\longrightarrow\ell,
                  \qquad\ell\in L_{\rm good}(h),     \tag{6.4}
\]

and which either reaches an unmatched right vertex or closes at `M(h)`.
If no such walk exists, no controlled containment switch can repair that
row while all other GKS matching rules are retained.

If `M(h) in L_good(h)` already, the minimum repair cost is zero and no
exchange walk is required.  Corollary 6.2 concerns the remaining case
`M(h) notin L_good(h)`.

This is an exact central-layer theorem, but not yet a full packet theorem.
Changing the matched rank-six element simultaneously:

* changes the skip base at every left root on the alternating component;
* changes which native rank-six chains are broken pairs and which are intact
  triples at the two path endpoints; and
* may invalidate the lower-target/type assignment on every affected packet.

Therefore a switch column may enter the state master only after it supplies
a complete replacement static flag factor on its affected rows and preserves
all rank-`2,...,8` exact-cover and type-mass rows.

## 7. Switch-augmented exact master

Let `mathfrak F(M)` be the family of complete literal static flag factors
which extend GKS matching `M` and retain the certified target-orbit and type
counts.  For `F in mathfrak F(M)`, construct `Omega(F)` and `D(F)` by
Sections 1--2.  The exact switch-augmented deficiencies are

\[
 \Delta_{\rm cc}^{\rm GKS}
   =\min_{\substack{M\text{ satisfies (6.2)}\\F\in\mathfrak F(M)}}
      \min_{z\in\mathfrak Z(F)}\delta_F(z),           \tag{7.1}
\]

and

\[
 \Delta_H^{\rm GKS}
   =\min_{\substack{M,F,z,e_*,\prec}}
      \delta_F^+(z,e_*,\prec).                       \tag{7.2}
\]

Thus a switch-augmented cycle cover exists exactly when (7.1) is zero, and
Hamilton support exists exactly when (7.2) is one.

There is no need to enumerate `mathfrak F(M)`.  A column-generation/repair
algorithm can start at the frozen factor and:

1. obtain a dead-row, Hall-deficiency, or Hamilton-cut witness from Sections
   3--5;
2. mark GKS containment edges whose complete replacement packet options add
   an in-neighbour, out-neighbour, Hall neighbour, or cut-crossing arc;
3. price a minimum-cost alternating path/cycle in `E_M`;
4. re-solve the low-flag colored matching with unaffected rows frozen when
   possible, expanding to the global matching if the exchange propagates,
   and reject any switch which fails the literal exact rows; and
5. add the resulting complete packet-state columns to the master.

Lexicographically maximize selected support arcs and then minimize

\[
                         |M-M_0|                     \tag{7.3}
\]

to obtain a minimum-disruption repair.  If the pricing oracle proves that
no alternating component can add a column crossing the current exact cut,
that cut is an obstruction for the declared GKS-switch catalogue.

## 8. Quantifier and scope audit

The valid order is

\[
 \exists\ M\ \exists\text{ one complete static flag factor }F
 \ \exists\text{ one attachment state per packet and owner} \tag{8.1}
\]

followed by the universal Hall cuts and, for Hamilton support, the universal
proper-subtour cuts.  Literal changing-owner arcs are built only after the
complete state choices they join are defined.

It is invalid to:

* infer arcs from age types or suffix-rank marginals;
* choose a fresh age partition independently on each incident arc;
* switch one GKS skip base without updating the displaced native
  pair/triple row and the low-target exact cover; or
* identify a perfect directed matching with a Hamilton cycle without the
  ordered-Hall condition or cuts (5.2).

The model certifies owner-attachment support and its exact finite
obstructions.  Nonzero voltage, strict-upper witnesses, and an upper-safe
opening remain downstream gates.
