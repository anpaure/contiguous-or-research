# The fixed 106-component endpoint face is closed; the corrected master starts with 122 pieces

Date: 2026-07-31  
Status: exact source-relative audit and exact optimization reduction; no `K17`
word, common-cap compiler, or unrestricted no-go is claimed

## 0. Result

Let `P` be the fixed rank-eight macro-port forest in
`scratch/k17_parent_induced_macro_port_cycle_20260731.flow.json`.  The 108
macros meeting the forced nonflat A bank have the advertised strong local
properties:

* their 3436 owner occurrences are distinct;
* every whole macro is internally `D2 >= 3` and `D3 >= 4` clean;
* the two-orientation direct-concatenation graph has 3146 arcs and minimum
  oriented outdegree 5; and
* their closure in `P` consists of 106 components, 190 macros, and 3970
  distinct owners.

The closure does **not**, however, turn those 106 forest components into 106
clean atomic paths.  Six components have 32 strict internal length-two
`D2` runs, all on the two new coordinates.  The exact minimum number of
existing macro seams meeting those runs is 16.  Thus a clean chronology which
opens only existing macro seams has at least

\[
                         106+16=122                         \tag{0.1}
\]

marked pieces before it starts to join them.

There is an independent endpoint obstruction.  Keep every fixed macro-port
incidence and orient each of the 106 components.  A one-cell old-`U` connector
between exposed rank-eight ports `T,T'` exists exactly when

\[
 |T\mathbin\triangle T'|=2,\qquad U=T\cup T',\qquad |U|=9. \tag{0.2}
\]

The owner `U` is unique.  Of 414 oriented geometric arcs, only 310 pass the
literal `D2/D3` join test.  Eleven components have no incident clean arc in
either orientation.  Therefore the fixed 106-component endpoint-only face
has no Hamilton path, even before all-different `U`, lower-palette, residual
flow, connectivity, upper service, or common-cap constraints are imposed.

The next exact model must expose and restitute internal incidences.  Treating
the 16 cuts as free ports would be unsound: each cut opens a saturated
rank-eight lower-colour interface.

## 1. Exact objects

The old ground set is `[15]`.  Let

\[
 {cal T}=\binom{[15]}8,\qquad {cal U}=\binom{[15]}9.
\]

The fixed macro forest is `P=({\cal T},E_P)`, with 1430 macro edges.  A macro
edge `e=(a_e,b_e)` expands to a literal rank-nine owner path `W_e`.  Its first
owner contains `a_e`, its last owner contains `b_e`, and every internal owner
adjacency is Johnson.  The graph `P` is a linear forest with 5005 components,
including 4021 isolated members of `T`.

Let `M` be the 108 forced-bank macros and let `C` be the set of components of
`P` meeting `M`.  Literal traversal gives

\[
 |M|=108,\quad |C|=106,\quad
 \left|\bigcup_{C\in{cal C}}E(C)\right|=190.          \tag{1.1}
\]

The two nontrivial component-size tails have 13 and 17 macro edges; the full
size histogram is

\[
                    1^{71}2^{17}3^9 4^7 13^1 17^1.    \tag{1.2}
\]

## 2. The 16-seam certificate

For a component word `W`, write a strict bad `D2` run as the half-open owner
interval `[s,s+l)`, with `l<3`.  A cut between owner positions `c-1,c` can
make that run terminal only if

\[
                         s\le c\le s+l.               \tag{2.1}
\]

Restrict `c` to existing boundaries between consecutive macros.  This gives
an interval stabbing instance on each component.  Exhaustive subset replay
gives optima

\[
                       1+1+1+6+1+6=16.                \tag{2.2}
\]

The JSON audit records every bad run, every available seam, and every chosen
minimum seam as `(left_macro,right_macro,shared_port,token_cut)`.  All other
100 components have optimum zero.  Reversal cannot help: a strict internal
run remains strict internal under reversal.

Equation (2.2) is a necessary topology statement, not a physical
construction.  At an internal forest vertex `T`, the two incident macro
endpoint incidences already give lower-vertex degree two.  Separating the two
owner paths requires changing at least one incidence and later restoring the
complete lower palette.  Accordingly, `122` is the smallest piece count in
the existing-seam topology, not a claim that 121 arbitrary `U` cells finish
the marked bank.

## 3. Exact fixed-endpoint connector semantics

For a clean oriented component `C^epsilon`, let

* `h(C^epsilon)` be its exposed head port;
* `t(C^epsilon)` be its exposed tail port; and
* `W(C^epsilon)` be its literal owner word.

For distinct components define a candidate labelled arc

\[
 a=(C^\epsilon,U,D^\delta)                            \tag{3.1}
\]

if and only if

\[
 U=t(C^\epsilon)\cup h(D^\delta),\quad |U|=9,
 \quad |t(C^\epsilon)\triangle h(D^\delta)|=2,        \tag{3.2}
\]

and the literal concatenation

\[
             W(C^\epsilon),\ U,\ W(D^\delta)          \tag{3.3}
\]

has no strict internal owner run below three and its adjacent-OR derivative
has no strict internal run below four.  These conditions are purely local,
because both component interiors have already been replayed.

There are 414 arcs satisfying (3.2), 310 satisfying (3.2)-(3.3), and only 128
distinct `U` labels among the latter.  Eleven component vertices have zero
incoming and zero outgoing arcs across both orientations.  This proves the
scoped no-go.

Notice that (3.2) is stronger than mere trace compatibility.  The 3146-arc
whole-macro compatibility graph ignores physical port incidence and therefore
cannot by itself materialize a lower-rainbow chronology.

## 4. Compact exact marked-path master

This section records the reusable model for any repaired piece catalogue.
Let `R` be a set of internally clean literal pieces.  Every piece `i` has two
orientations.  Precompute the exact connector catalogue `A` by (3.2)-(3.3),
or by the incidence-changing semantics of Section 5 when a seam is opened.
Each connector `a` stores

\[
       \operatorname{tail}(a),\operatorname{head}(a),
       \operatorname{ori}_{t}(a),\operatorname{ori}_{h}(a),
       u(a),\lambda(a),\mu(a).                        \tag{4.1}
\]

Here `u(a)` is the inserted owner and `lambda,mu` are its two rank-eight
incidence colours.

Use Booleans `x_a`, orientation Booleans `z_(i,epsilon)`, and dummy start/end
arcs.  The exact path constraints are

\[
 \sum_{\epsilon}z_{i,\epsilon}=1,                     \tag{4.2}
\]

\[
 \sum_{a:\operatorname{head}(a)=i}x_a+s_i=1,
 \qquad
 \sum_{a:\operatorname{tail}(a)=i}x_a+t_i=1,          \tag{4.3}
\]

\[
                   \sum_i s_i=\sum_i t_i=1,           \tag{4.4}
\]

with implications from every `x_a` to its two endpoint orientations, and

\[
                    \sum_{a:u(a)=u}x_a\le1            \tag{4.5}
\]

for each owner label.  Subtours must be excluded.  The leanest proof-safe
encoding is one dummy vertex `*` and a circuit constraint on `R union {*}:
`* -> start`, the chosen labelled arcs, and `end -> *`.  In DIMACS, lazy
directed-cycle clauses or an order/flow encoding are equivalent.

Constraints (4.2)-(4.5) alone are only a labelled path-cover formulation.
They are not a Hamilton-path theorem without the circuit/subtour condition.

## 5. Corrected 122-piece incidence master

Let `S` contain the 16 certified seam cuts, giving at least 122 marked pieces.
At every new piece endpoint retain the literal endpoint owner `v`, but do not
pretend that its old port is free.  The exact choice is an incidence

\[
                         (v,L),\qquad L\subset v,\ |L|=8.            \tag{5.1}
\]

If a connector inserts `u`, its two colours are forced:

\[
                    \lambda=v_{\rm left}\cap u,qquad
                    \mu=u\cap v_{\rm right}.          \tag{5.2}
\]

The tuple is admissible only when both have rank eight, are the intended
free incidences of their endpoint owners, do not overfill a colour already
used internally, and the literal three-block join passes residence.  Thus a
candidate generator should enumerate `(piece,orientation,u,piece,orientation)`
and derive (5.2); it should not enumerate abstract unlabeled seams.

Let `F_int` be all incidences fixed strictly inside the pieces, and let
`F(x)` add the incidences chosen by marked connectors.  Exact palette and
owner degrees are

\[
 \deg_{F(x)\cup Y}(v)=2\quad\hbox{for every rank-nine owner }v,
 \qquad
 \deg_{F(x)\cup Y}(L)=2\quad\hbox{for every rank-eight colour }L.   \tag{5.3}
\]

The residual variables `Y` range only over literal containments `L subset v`.
This single incidence system correctly restitutes every opened seam.  It also
makes clear why cutting a saturated old port is not free.

## 6. Residual `U`-to-port flow and exact Hall cuts

On the fixed-port face, once marked connectors `x` are fixed, put

\[
 d_x(T)=2-\deg_P(T)-a_x(T),                            \tag{6.1}
\]

where `a_x(T)` is the number of marked connector incidences using `T`.  An
unused old owner `U` has supply two and every containment arc `U superset T`
has capacity one.  The residual network

\[
             s\longrightarrow U\longrightarrow T\longrightarrow t          \tag{6.2}
\]

is integral.  Its feasibility is equivalent to the generalized Hall family

\[
 \sum_{T\in Q}d_x(T)
 \ \le\ 
 \sum_{U\notin u(x)}\min\bigl(2,\,|\{T\in Q:T\subset U\}|\bigr)
 \qquad(Q\subseteq{\cal T}).                           \tag{6.3}
\]

Thus a path-master candidate should be screened by one exact max flow.  A
failed min cut supplies a proof-safe Benders row; no monolithic SAT expansion
of the residual incidence network is needed.

For the incidence-changing 122-piece master, use the same construction with
residual owner demands `2-deg_F(v)` and residual lower demands
`2-deg_F(L)`.  The standard cut form for source-side sets `A` of owners and
`B` of lower colours is

\[
 \sum_{v\in A}(2-\deg_F(v))
 \le
 \sum_{L\in B}(2-\deg_F(L))
 +e_{\rm free}(A,{\cal L}\setminus B).                 \tag{6.4}
\]

This is exactly checkable and linearizes to the fixed-incidence Benders rows
already used elsewhere in the project.

## 7. Why residual flow is not yet complementary contiguity

A feasible solution of (6.2) only makes a degree-two factor.  Pair the two
selected facets of each unused `U` to obtain a quotient edge between macro
forest components.  To make the complementary bank one path, contract the
marked path to one supervertex and require the quotient factor to be
connected.  Since every quotient vertex then has degree two, connectivity is
equivalent to one cycle; deleting the marked supervertex leaves one path
through all unmarked components.

One exact pair formulation uses

\[
 z_{U,\{T,T'\}}\in\{0,1\},\qquad T,T'\subset U,quad T\ne T',      \tag{7.1}
\]

with one pair per unused `U`, port-degree equations, and lazy cuts

\[
 \sum_{e\in\delta(Q)}z_e\ge2
 \qquad(\varnothing\ne Q\subsetneq\hbox{contracted components}). \tag{7.2}
\]

There are at most 36 pairs per old `U`.  Equation (7.2) is necessary in
addition to Hall.  Residence is another independent gate: if residual joins
are not orientation-blind clean, the pair variables must be refined to
oriented component arcs and checked literally.

Consequently the marked-path and residual-flow problems may be solved in
sequence only under all three conditions:

1. the selected marked incidences and owner labels are subtracted exactly
   from residual capacities;
2. every residual selected pair is residence-safe in its induced component
   orientation (or residence is encoded jointly); and
3. the quotient connectivity cuts (7.2) pass.

Marginal Hall feasibility alone does not prove either bank contiguous.

## 8. Reproduction and scope

Run

```text
python3 scratch/audit_k17_marked_component_endpoint_gate_20260731.py
python3 -m py_compile scratch/audit_k17_marked_component_endpoint_gate_20260731.py
```

The audit is fail-closed on all headline counts and independently reconstructs
the selected macros from the forced-pattern map.  It does not import the
phase-path producer.  The frozen phase JSON is replayed only in its actual
A-subblock scope; it is not used as a whole-macro physical witness.

This note closes only the fixed whole-component, fixed-port, one-old-`U`
endpoint face.  It leaves open the exact 122-piece incidence-restitution
master, alternative macro closure, changed owner values, deeper lower/upper
service, the maximal envelopes, and the common-cap compiler.
