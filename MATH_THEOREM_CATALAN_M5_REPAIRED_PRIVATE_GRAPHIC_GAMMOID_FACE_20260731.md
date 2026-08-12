# The repaired `m=5` state enters the private graphic--gammoid face

Date: 2026-07-31  
Status: exact finite `m=5` theorem and interface audit; no minimum-three-
`C10` theorem and no all-`m` repair, nontrivial-voltage, deeper-shadow,
residence or compiler theorem

## 0. Verdict

Let `g0,g1` be the two standard transparent glues

```text
g0 = (11001010,10101010),
g1 = (11001100,10101100).
```

Start with the standard Hamilton output using both labels and apply the
three frozen, pairwise vertex-disjoint `C10` switches `C1,C2,C3`.  Their
palette and augmented-matching deficiencies form the exact staircase

\[
 (3,3,3)\longrightarrow(2,2,2)\longrightarrow(1,1,1)
 \longrightarrow(0,0,0).                             \tag{0.1}
\]

The `C10` supports are disjoint from the two standard collars, so commute
the fixed repair packet before `g0,g1`.  The resulting repaired preglue
factor has two components, of orders `120` and `132`.  Either `g0` or `g1`
alone produces one `252`-cycle, and the same forced-port `84+84`
decoration is valid and leaf-peelable at every point of the full two-label
cube.

Consequently the complete surviving gluing bank

\[
                         T=\{g0,g1\}                  \tag{0.2}
\]

lies on the private-gap graphic--gammoid face.  Its two component edges are
parallel, its gap row is free on this literal restriction, and after the
fixed repair linkage has been contracted its residual linkage matroid is
free.  With component target `q-1=1`, Edmonds' four rank inequalities have
left sides

\[
                         2,2,2,1.                    \tag{0.3}
\]

There is no violating `X`; both singletons are accepted component-spanning
sets.  The end-to-end audited choice is `{g1}`, which also has a literal
two-shore-injective socket closure.  It is a smallest accepted subcatalogue:
the empty set leaves two factor components.

This does **not** prove that three `C10` switches are a smallest repair
packet.  It proves that the displayed three-switch prefix works and that,
after this fixed prefix, the smallest component-spanning gluing selection
has one label.

## 1. Exact repaired cube

Write `F` for the canonical MMM two-factor, `H_i` for the physical hexagon
of `g_i`, and

\[
                  P=C_1\mathbin\triangle C_2
                       \mathbin\triangle C_3.         \tag{1.1}
\]

The repaired preglue state and its four descendants are

\[
 F_S=F\mathbin\triangle P
       \mathbin\triangle\!\bigtriangleup_{g_i\in S}H_i,
       \qquad S\subseteq T.                          \tag{1.2}
\]

The literal component and gap-forest replay is

\[
\begin{array}{c|c|c|c}
S&\text{factor component orders}&|E(\Gamma_S)|&
  \kappa(\Gamma_S)\\ \hline
\varnothing&120,132&107&61\\
\{g0\}&252&109&59\\
\{g1\}&252&109&59\\
\{g0,g1\}&252&111&57.
\end{array}                                           \tag{1.3}
\]

Every `Gamma_S` is a forest on the same `168` occurrence-labelled
vertices, has the selected perfect matching, and is therefore uniquely
leaf-peelable.  Each binary trace induced by the common marked sets is on
the linear-forest side.

The two private lower-owner transitions are

\[
\begin{array}{c|c|c}
 &\text{old neighbourhoods}&\text{new neighbourhoods}\\ \hline
g0&\{82\},\{84\},\{88\}&\{82,84\},\{84,88\},\{88\}\\
g1&\{50\},\{52\},\{56\}&\{50,52\},\{52,56\},\{56\}.
\end{array}                                           \tag{1.4}
\]

Thus their attachment paths are

\[
 [82]-g-[84]-g-[88],\qquad[50]-g-[52]-g-[56],        \tag{1.5}
\]

and the two owner triples are disjoint.  Equation (1.3), rather than an
unproved locality heuristic, is what makes the gap row free on the complete
two-element restriction.

## 2. The fixed repair linkage and the residual selectable linkage

The original standard Hamilton state has augmented matching rank `207`.
The three switches raise this rank successively to

\[
                         208,209,210.                 \tag{2.1}
\]

The intersection of the original and final augmented occurrence graphs has
matching rank `197`.  Relative to a maximum common-core matching and the
forced-port final perfect matching, their symmetric difference consists of
thirteen vertex-disjoint augmenting paths, with edge lengths

```text
3,3,3,3,3,3,3,3,3,3,3,5,15
```

and four harmless alternating four-cycles.  Hence the preliminary repair
prefix passes the exact bounded common-core linkage gate; this is not being
inferred from turn-palette counts.

After that fixed prefix is contracted, the *same* marked sets certify all
four states in (1.3).  The glues do change state-specific occurrence edges,
but every one of the four transfers has already been accepted under that
common decoration.  Thus there is no **unresolved residual** linkage demand
on this prepared two-label restriction.  After quotienting by the certified
finite transfer relation, its residual selectable linkage matroid is

\[
                         M_L=U_{2,2}.                 \tag{2.2}
\]

This distinction is important: the fixed prefix has a nontrivial
thirteen-path linkage certificate, while the post-repair label bank has a
free residual linkage row.

## 3. The concrete Edmonds inequalities

Let the two vertices of the restricted component graph be the `120`- and
`132`-cycles.  Both `g0` and `g1` join these vertices.  For the target-one
spanning-tree selection problem, therefore,

\[
 M_C=U_{1,2},\qquad
 r_C(X)=\min(1,|X|),\qquad r_L(Y)=|Y|.                \tag{3.1}
\]

Edmonds' criterion for a common independent set of size `q-1=1` is

\[
              r_C(X)+r_L(T\setminus X)\ge1
              \qquad(X\subseteq T).                 \tag{3.2}
\]

The complete rank table is

\[
\begin{array}{c|c|c|c|c}
X&r_C(X)&r_L(T\setminus X)&\text{sum}&\text{slack}\\ \hline
\varnothing&0&2&2&1\\
\{g0\}&1&1&2&1\\
\{g1\}&1&1&2&1\\
T&1&0&1&0.
\end{array}                                           \tag{3.3}
\]

The unique tight partition is `X=T`; no `X` violates (3.2).  Both `{g0}`
and `{g1}` are common bases.  Select `T'={g1}` to retain the audited socket
closure.  On this literally smallest restriction the two inequalities are
both tight:

\[
 0+r_L(T')=1,
 \qquad r_C(T')+0=1.                                 \tag{3.4}
\]

The state `{g0,g1}` is also a valid Hamilton state by direct replay, even
though it is dependent in this restricted `M_C`.  Consequently
`I(U_{1,2})` is not a characterization of every Hamilton-safe cube subset;
it is an exact conservative restriction for the rank-one existence question.
The bonus dependent state is not needed by the graphic--gammoid proof.

## 4. Physical socket and recursive-interface audit

The current physical-lift companion is positive through literal topology
and outer-load cap two for the final `{g0,g1}` state.  Its `210` selected
Johnson edges on
`J(10,5)` use every rank-four intersection and every rank-six union exactly
once and form a spanning forest of `42` paths.  The endpoint catalogue has

```text
84 formal ports,
297 legal formal port pairs,
273 distinct physical connector edges,
0 zero-degree ports,
connected 42-component projection.
```

A frozen set of `42` legal connectors uses every formal port once, is
injective on both outer-colour shores, and turns that forest into one literal
`252`-vertex Hamilton cycle.  The resulting lower and upper load profiles
are both exactly

\[
                         1^{168}2^{42}.               \tag{4.1}
\]

The deterministic MRV search takes `1,285` nodes and retains `33` edges of
the first topology-only closure.  At the literal `h=1` level the voltage
condition is vacuous, so this closes the topological,
connector-colour-injective and multiplicity-cap-two socket gates for that
displayed final state.

That bonus-state certificate is not being silently attached to an Edmonds
basis.  The singleton `{g1}` has been replayed separately under the same
common marks.  It again gives a `210`-edge exact-palette forest with `42`
paths, `84` formal ports, `297` legal pairs, `273` distinct connector edges,
no zero port and connected component projection.  A frozen `42`-connector
matching is injective on both shores and produces one `252`-cycle.  Its
connector and Hamilton-cycle hashes begin respectively

```text
2681868a51352f26
62b168c3875225dd
```

Thus the component basis, fixed decoration, private gap row, literal
topological socket and multiplicity-cap-two `42/42` connector gate all pass
on the same selected singleton `{g1}`.  This is not block coherence: among
the `42` doubled colours, only `15` lower and `11` upper connector/forest
pairs share a middle vertex.  No uniform-outgoing or block-coherent compiler
claim follows.

No frozen artifact here tests deeper shadows, a nontrivial quotient voltage,
proper-prefix residence, staircase deadlines, or a common literal compiler
for the selected singleton `{g1}`.  A separate audit of the bonus full
`{g0,g1}` closure proves all-depth flag support, but also proves that every
intact-path opening fails depth-two residence because of `31` immutable
length-two one-runs.  That full-state result does not automatically transfer
to `{g1}`.  The recursive compiler interface therefore remains open.

## 5. Minimality scope of the repair prefix

The following negative statements are exact at the displayed transparent
standard Hamilton root:

* no single incidence `C6` improves either palette;
* no Hamilton-safe incidence-hex sequence of depth at most three completes
  the repair;
* among all single simple alternating `C8` and `C10` switches, the best
  deficits are respectively `(2,3,3)` and `(2,2,2)`, so no single
  `C6/C8/C10` completes the repair.

The longer exploratory census uses a recorded `281`-circuit common-exterior
pool.  It checks `22,832` edge-disjoint two-switch pairs, finds no
palette-perfect pair and has `182` states at deficit `(1,1)`.  The complete
`C6/C8/C10` third-switch census from those `182` sources gives `585`
distinct palette-perfect Hamilton outputs, of which `452` have augmented
deficiency zero.

Those two- and three-switch counts are exact **inside that recorded pool**.
They do not exhaust arbitrary sequential pairs of long alternating circuits.
Accordingly the displayed three-`C10` packet is an explicit synchronized
positive packet, not a theorem that every repair needs three `C10`s.

## 6. The repair prefix is a defect-router catalogue

The three `C10`s belong before, not inside, the private
graphic--gammoid selection.  The following formulation makes the interface
exact.

Let `L` and `U` be the missing lower and upper colour sets at a fixed root
factor, and let `P_L,P_U` be the already covered colours which must remain
covered.  A **unit router macro** `a` has labels

\[
                         (\ell_a,u_a)\in L\times U    \tag{6.1}
\]

when its physical symmetric difference creates `ell_a` and `u_a`.  A macro
catalogue `A` is support-monotone if its effects commute and, for every
subset `S` under consideration,

\[
\begin{aligned}
 \operatorname {miss}_L(F_S)
   &=L\setminus\{\ell_a:a\in S\},\\
 \operatorname {miss}_U(F_S)
   &=U\setminus\{u_a:a\in S\},                       \tag{6.2}
\end{aligned}
\]

while `P_L,P_U` stay covered.  This definition is at support level: a macro
may change a protected colour's multiplicity, but may not make that colour
absent.

Equivalently, for binary macro variables `x_a`, the exact static system is

\[
 \sum_{a:\ell_a=\ell}x_a=1\quad(\ell\in L),\qquad
 \sum_{a:u_a=u}x_a=1\quad(u\in U),                  \tag{6.2a}
\]

together with the protected rows

\[
 \mu_s(c)+\sum_a\Delta_a^s(c)x_a\ge1
 \quad(s\in\{L,U\},\ c\in P_s).                    \tag{6.2b}
\]

Plain Hall is exact only after (6.2b) is redundant or has been compiled into
the macro catalogue.  A sufficient private-reserve condition is that every
negative derivative is `-1` on an initial multiplicity-two colour, the
negative banks of selected macros are pairwise disjoint on each shore, and
no macro consumes another macro's defect gain.  The frozen packet satisfies
this condition literally.

Make the bipartite router multigraph `R_A` with shores `L,U` and one
labelled edge `ell_a u_a` for each macro.  Equivalently, use the integral
network

```text
source -> lower deficit -> macro -> upper deficit -> sink,
```

with unit capacities.  Under (6.2), a macro set repairs every deficit
exactly once if and only if it is a perfect matching of `R_A`.  Hence the
exact palette condition is

\[
 |L|=|U|,
 \qquad |N_{R_A}(X)|\ge |X|
       \quad\text{for every }X\subseteq L,            \tag{6.3}
\]

or, equivalently, maximum flow `|L|`.  This is ordinary Hall with parallel
macro identities retained.  Protected-colour monotonicity is a hypothesis
of the router graph, not an inference from (6.3).

The exact static rank is the min-cut formula

\[
 \nu(R_A)=\min_{X\subseteq L}
   \bigl(|L\setminus X|+|N_{R_A}(X)|\bigr).          \tag{6.3a}
\]

Hall does not decide physical chronology.  For a selected perfect matching
`M`, form the state-expanded directed graph `D(M)`.  Its vertices are the
subsets `S subseteq M` for which the current physical factor passes the
declared topology and protected-support tests.  Store at each vertex the
exact linkage-debt signature

\[
                 \Sigma_S=(d_S,{\cal R}_S),
 \qquad d_S=N-\nu({\cal A}_S),                        \tag{6.4}
\]

where `A_S` is the augmented occurrence graph, `d_S` is its scalar
deficiency and `R_S` is the correlated unmatched-terminal/linkage relation.
There is an arc `S -> S+a` precisely when `a` is alternating in the current
factor and the exact boundary relation composes to `Sigma_(S+a)`.

The selected router packet is physically accepted if and only if `D(M)`
has a directed path from the root to `M` and the terminal signature has
`d_M=0` with the required forced-port decoration.  Equivalently, the
unit-capacity state network has source--sink flow one, or every directed
source--sink cut has an outgoing arc.  This state flow is finite and exact;
unlike (6.3), it need not have a polynomial-size uncompressed description.
The relation `R_S`, not the scalar `d_S` alone, is required in general.

There is one useful exact simplification at a prefix.  Suppose the only
unmatched obstruction consists of isolated defect banks
`D_S^L,D_S^R`, both of size `d_S`, in a balanced augmented graph on `N+N`
vertices.  Delete those banks and call the result `Ahat_S`.  The prefix has
no hidden occurrence debt if and only if any of the following equivalent
conditions holds:

\[
 \widehat{\cal A}_S\text{ has a perfect matching}
 \iff \nu({\cal A}_S)=N-d_S
 \iff
 |N_{{\cal A}_S}(X)\setminus D_S^R|\ge |X|           \tag{6.4a}
\]

for every `X` outside `D_S^L`; equivalently its matching-flow value is
`N-d_S`, or every corresponding cut has capacity at least `N-d_S`.
These are independent layerwise flows.  Requiring the chosen matchings to
nest across time would add an unsupported recourse constraint.

At the transparent standard `m=5` root, the complete Hamilton-safe
optimum-`C10` static catalogue has `31` labelled macros.  With rows
`73,146,292` and columns `219,365,438`, its multiplicity matrix is

\[
 \begin{pmatrix}
 1&10&0\\
 12&0&0\\
 0&0&8
 \end{pmatrix}.                                      \tag{6.4b}
\]

Its matching rank is three.  The tight rows force the unique endpoint
matching

\[
 73\mapsto365,\qquad146\mapsto219,\qquad292\mapsto438,\tag{6.4c}
\]

with `10*12*8=960` labelled static realizations.  The extra signature
`73->219` belongs to no perfect matching.  These are assignments, not yet
ordered physical packets.

For the frozen `m=5` packet,

\[
 L=\{73,146,292\},\qquad U=\{219,365,438\},           \tag{6.5}
\]

and the router edges are

\[
 C_1:73\mapsto365,qquad
 C_2:146\mapsto219,qquad
 C_3:292\mapsto438.                                  \tag{6.6}
\]

Their negative protected banks are

\[
\begin{array}{c|c|c}
 &B_L^-&B_U^-\\ \hline
C_1&11,104,321&125,335,489\\
C_2&26,131,208&159,249,467\\
C_3&13,416&175,500.
\end{array}                                           \tag{6.6a}
\]

Every displayed colour has root multiplicity two and the banks are
pairwise disjoint on each shore.  Hence the protected rows (6.2b) are
redundant for this selected packet, while every desired defect gain remains
private.

Thus the **frozen three-macro subcatalogue** itself is a perfect matching:
every Hall inequality on that restriction is tight and its unique router
flow uses all three macros.  Its relay `C3` is root-unsafe and is not being
certified by the root-safe `31`-macro catalogue (6.4b).  The complete frozen
subset audit is

\[
\begin{array}{c|c|c|c|c}
S&\text{Hamilton}&d_S&\operatorname {miss}_L&
                         \operatorname {miss}_U\\ \hline
000&\text{yes}&3&73,146,292&219,365,438\\
001&\text{yes}&2&146,292&219,438\\
010&\text{yes}&2&73,292&365,438\\
011&\text{yes}&1&292&438\\
100&\text{no}&2&73,146&219,365\\
101&\text{no}&1&146&219\\
110&\text{no}&1&73&365\\
111&\text{yes}&0&\varnothing&\varnothing.
\end{array}                                           \tag{6.7}
\]

Here the bits index `C1,C2,C3` from least to most significant.  The exact
topology-flow graph is therefore

```text
000 -> 001 -> 011 -> 111
  \      ^
   -> 010
```

with the second path `000 -> 010 -> 011 -> 111`.  In particular `C3` is the
unique final relay; palette Hall alone would not reveal that it is unusable
before both direct filters.  Along either legal route the temporary linkage
debt is `3 -> 2 -> 1 -> 0`.  The ranks `208` and `209` are not decorations.
Only the terminal rank `210`, together with the exact `197`-core and
thirteen augmenting paths of Section 2, discharges the router linkage debt.

### Transparent collars and debt-carrying routers are different species

The exact fixed-decoration criterion is the transparent-hexagon theorem of
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.
For a decorated factor `(C,D)` and a Hamilton-safe incidence-hex toggle
`C -> C'`, the same `D` survives if and only if

1. the selected local turn-colour **multisets** agree before and after the
   toggle, separately on the lower and upper shores; and
2. after the old matching is deleted, the selected boundary mark types on
   the retained fragments alternate under the new reconnection.

If leaf peelability is part of the state, one must additionally delete the
old seam-crossing gap edges, contract the retained gap-forest components,
and require the new attachment multigraph to be loopless and acyclic.

This criterion applies only when a fixed decoration already exists on the
input.  The finite `ML(7)` calibration makes the distinction literal: among
`31` alternating incidence hexagons, `16` outputs are Hamilton, `10` are
decorable, but only `6` admit a common fixed decoration across the toggle.
Thus “the output can be redecorated” is not the transparent relation needed
by a recursive gluing tree.

Accordingly the recursive object is a **joint alternating SDR together with
a transparent gluing tree**.  An arbitrary frozen SDR may fail a chosen
glue, while an arbitrary published gluing tree may have no decoration which
survives all of its edges.

The `m=5` `C10`s are not transparent collars in this sense.  The router
root has debt three and the two nonterminal legal layers have debts two and
one, so no decoration exists there to freeze.  Their correct state is
`(ell_a,u_a,Sigma_S)` in the router network.  By contrast, after terminal
debt zero is reached, `g0,g1` are literal fixed-decoration transparent moves:
the same `84+84` marked sets pass every state of their cube, and the exact
gap-attachment replay is acyclic.

### The router-to-Edmonds interface

Let `M` be an accepted router matching and let `F_M` be its terminal factor.
It may feed a downstream collar ground `T` only after all of the following
hold:

1. the terminal debt is zero and one guarded decoration `D` exists;
2. the fixed router packet commutes with the downstream collars, or the
   complete repaired collar cube is replayed literally;
3. the same `D` prepares every permitted downstream choice;
4. every selectable downstream move satisfies the fixed-decoration palette
   and retained-fragment boundary test above; and
5. the downstream gap row is private or aligned (with the exact
   delete--contract--insert test when leaf peelability is carried).

Only then are the ranks `r_C^{M,D}` and `r_L^{M,D}` defined on the prepared
label ground, and the next exact gate is

\[
 r_C^{M,D}(X)+r_L^{M,D}(T\setminus X)
      \ge q(M)-1\qquad(X\subseteq T).                \tag{6.8}
\]

Temporary macro linkage debt must not be mixed marginally into (6.8).  It
is discharged and contracted at the router boundary; otherwise the
downstream gammoid is being asked to start from a decoration which does not
exist.

In the literal `m=5` fixture, (6.6)--(6.7) accept the unique router packet,
the forced-port terminal decoration prepares the full `g0,g1` cube, and
(6.8) becomes exactly the four inequalities (3.3).

### Uniform target after the Pascal obstruction

The finite packet should not be extrapolated as a bounded-number-of-switches
lemma.  The exact target from
`MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md`
is a **controlled-debt packet of bounded-port circuits** whose total length
may grow with `m`; what must stay controlled at a cut is the live boundary
and linkage debt.  After that packet terminates, an ordered list of
fixed-decoration transparent, leaf-peelable glues performs the component
braid.

This state is forced algebraically.  The Pascal-sector determinant theorem
shows that two full embedded parent solutions plus the forced cross rails
already contain a cycle, so scalar two-full-parent recursion is impossible.
Exact atom contraction requires both residual acyclicity and absence of an
`H -> T` path.  Hence boundary-deficient rails and endpoint/reachability
state are necessary, not optional implementation detail.

The synchronized `m=5` full-state closure already covers the entire lower
and upper flag tower and has `46` all-depth-safe cuts.  Its remaining failure
is residence: every intact-path opening retains `31` internal coordinate
one-runs of length two, while `d=2` requires length at least three.  Path
permutation, reversal and socket choice cannot alter those runs.  Therefore
the next packet operation must include an **interior rethread** which
preserves the accepted decoration/flag tower while changing path bodies;
another endpoint-only closure cannot solve the compiler gate.

## 7. Audit artifacts

The independent replay

```text
scratch/audit_catalan_standard_m5_three_c10_private_repair_independent_20260731.py
```

contains no project-module imports.  It independently reconstructs the MMM
factor, the two standard labels and the three authoritative `C10`s; checks
the staircase, the `197+13` common-core certificate, all four gap/trace
states, both private paths, and the rank tables (3.3)--(3.4).  It emits

```text
scratch/catalan_standard_m5_three_c10_private_repair_independent_20260731.audit.json
```

The separate endpoint audit is

```text
scratch/audit_catalan_m5_three_c10_endpoint_socket_20260731.py
scratch/catalan_m5_three_c10_endpoint_socket_20260731.audit.json
```

and checks the displayed physical forest and literal `42/42` Hamilton
connector witness.  Its no-import independent replay is

```text
scratch/audit_catalan_m5_three_c10_endpoint_socket_independent_20260731.py
scratch/catalan_m5_three_c10_endpoint_socket_independent_20260731.audit.json
```

These are companion finite certificates, not an all-`m` socket or compiler
theorem.

The complete root-safe static router census and protected-bank theorem are

```text
MATH_THEOREM_CATALAN_M5_DEFECT_ROUTER_HALL_GATE_20260731.md
scratch/audit_catalan_m5_defect_router_hall_20260731.py
scratch/catalan_m5_defect_router_hall_20260731.audit.json
```

The independent full eight-state router/debt replay is

```text
scratch/audit_catalan_m5_three_c10_defect_router_independent_20260731.py
scratch/catalan_m5_three_c10_defect_router_independent_20260731.audit.json
```

The exact rank-one catalogue and singleton-`g1` socket composition are
replayed by

```text
scratch/audit_catalan_m5_repaired_parallel_catalogue_20260731.py
scratch/catalan_m5_repaired_parallel_catalogue_20260731.audit.json
```

Finally, the fixed-decoration transfer criterion used at the router boundary
is the independently frozen

```text
MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
```

whose finite calibration is `31/16/10/6` for alternating, Hamilton,
decorable and common-fixed-decoration hexagons respectively.

The dimension-uniform target and its algebraic necessity are recorded in

```text
MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md
MATH_THEOREM_CATALAN_PASCAL_SECTOR_DETERMINANT_AND_TWO_COPY_NOGO_20260731.md
THREAD_A_M5_THREE_C10_DOWNSTREAM_COMPATIBILITY_AUDIT_20260731.md
```
