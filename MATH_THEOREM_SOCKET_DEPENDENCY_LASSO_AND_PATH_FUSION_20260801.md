# Socket-dependency lassos and native path fusion

## Status and scope

This note isolates a proof-safe mechanism suggested by the corrected
`k=17` rich-socket selector.  It is a theorem about a prepared socket bank;
it is **not** a proof that the required bank exists in every dimension, and
it is not a proof of `nu(17)=B(17)`.

The finite motivation is exact.  The corrected selector can cover target
`75749`, but its optimum still has one omitted target, now `69605`.  These
two colours are consecutive unions on one native owner component:

\[
  4069\cup67557=69605,
  \qquad
  67557\cup74725=75749.
\]

The owners occur consecutively on component `1209`, at positions
`3,4,5`.  Two separately encoded sockets duplicate the common facet owner
`67557`; the native two-edge path uses it once.  Thus at least part of the
one-hole obstruction is an augmenting-path phenomenon hidden by the
row-wise owner AMO encoding.

## 1. Abstract gain--debt packets

Let `U` be a finite set of unsupported palette targets and let `S_0` be the
palette already supported by the background chronology.  For each
`x in U`, let `P_x` be a menu of packets.  A packet `p in P_x` has:

* a gain `g(p)=x`;
* a debt `d(p) in U union {bottom}`;
* a physical resource footprint `R(p)`.

The value `d(p)=bottom` means that every child colour created by the packet
is already in `S_0` or is supplied internally by the packet.  Otherwise
`d(p)=y` means that, after removing all background-supported and self-served
children, the packet has the single remaining obligation `y`.

For a packet family `A`, write

\[
  G(A)=\{g(p):p\in A\},
  \qquad
  D(A)=\{d(p):p\in A,\ d(p)\ne\bot\}.
\]

The family is palette-closed when

\[
  D(A)\subseteq S_0\cup G(A).                 \tag{1.1}
\]

This is a set-support condition, not a multiplicity equation.  If several
packets ask for the same child colour, one supplied occurrence suffices.

## 2. The dependency-lasso theorem

Perform every certified native path fusion of Section 3 first, and regard
the resulting macros as the packet candidates.  Call two packets
incompatible when their remaining physical fragments cannot coexist.  Let
`C` be the corresponding graph.  In the graph-form statements below we
assume that `C` is complete: every independent set in `C` is jointly
physically feasible.  This holds for one-capacity typed resources after
fusion.  If topology or another higher-order constraint is not captured by
pairwise conflicts, it must instead be included in the exact packet
feasibility relation; the degree corollaries then do not apply.

### Theorem 2.1 (compatible dependency lasso)

Assume that one can choose a pairwise compatible representative

\[
  p_x\in P_x \qquad (x\in U).                 \tag{2.1}
\]

Then every initially missing target `h in U` has a pairwise compatible,
palette-closed repair family.

More precisely, start with `x_0=h`.  Having chosen `x_i`, stop if
`d(p_{x_i})=bottom`; otherwise put

\[
  x_{i+1}=d(p_{x_i}).                          \tag{2.2}
\]

Because `U` is finite, this process either reaches `bottom` or first repeats
a target.  The packets on the resulting directed path or directed lasso
form the required repair family.

#### Proof

Before the first repeat, the targets `x_i` are distinct, so their chosen
packets are pairwise compatible by (2.1).  In the terminating case the debt
set is contained in

\[
  \{x_1,\ldots,x_t\}\subseteq
  \{x_0,\ldots,x_t\}=G(A).
\]

In the repeating case, the last debt is one of the earlier `x_j`, and all
other debts are the next targets on the walk.  Again `D(A) subseteq G(A)`.
Thus (1.1) holds in both cases, and `h=x_0` is supplied.  Compatibility is
inherited by taking a subset of (2.1).  QED

The theorem explains why a directed cycle is useful here.  The arcs encode
new **obligations**, not deletion of already selected packets.  Every debt
on the cycle is paid by the gain of the next packet.

### Corollary 2.2 (degree criterion)

Let `Delta` be the maximum degree of the incompatibility graph `C`.  If

\[
  |P_x|\ge 2\Delta \qquad\text{for every }x\in U,               \tag{2.3}
\]

then the conclusion of Theorem 2.1 holds.

#### Proof

Haxell's independent-transversal theorem gives an independent set meeting
every part `P_x` once under (2.3).  Apply Theorem 2.1.  QED

### Corollary 2.3 (typed-resource criterion)

Suppose every packet uses at most `s` nonfusible typed resources, and every
such resource occurs in at most `mu` packet candidates.  Then

\[
  \Delta\le s(\mu-1).                          \tag{2.4}
\]

Consequently it is sufficient that

\[
  |P_x|\ge 2s(\mu-1) \qquad(x\in U).           \tag{2.5}
\]

The resources in (2.4) must include every actual source of interaction:
owner capacity, nonfusible facet use, guard interiors, protected upper
witnesses, cut incompatibility, and endpoint state.  Omitting one of these
types invalidates the conclusion.

For asymptotic packet atlases with

\[
  |P_x|\ge \alpha r^2,
  \qquad
  s\mu\le \beta r d,
\]

condition (2.5) holds for all sufficiently large `r`, since
`d=Theta(sqrt(r))` and hence `r/d -> infinity`.

## 3. Native path fusion

The incompatibility graph must not classify a legal shared path endpoint as
a collision.

### Lemma 3.1 (two-socket path fusion)

Let

\[
  P=(u_0,u_1,\ldots,u_a),
  \qquad
  Q=(u_a,u_{a+1},\ldots,u_{a+b})
\]

be simple directed owner paths which otherwise have disjoint owner sets.
Assume:

1. the right trace of `P` and the left trace of `Q` agree at `u_a`;
2. the two inner guard states are inverse copies of the same native state,
   so deleting them restores the old chronology through `u_a`;
3. all immediate lower and upper colours on the concatenated path are
   allowed, with repeated providers accounted for only once;
4. the two outer guard intervals are legal and residence-clean.

Then the concatenation

\[
  P*Q=(u_0,u_1,\ldots,u_{a+b})                 \tag{3.1}
\]

is one legal socket packet.  It preserves every target carried by an edge
of either `P` or `Q`, uses the common owner `u_a` once, and requires only the
two outer guards.

Relative to treating the paths as separate packets, fusion saves one owner
occurrence, two inner guard interfaces, and the corresponding inner
boundary cuts.

#### Proof

The owner sequence in (3.1) is simple because the paths meet only at their
common endpoint.  Every old edge of `P` and `Q` remains an edge of the
concatenation, so its intersection and union colours remain.  Conditions 1
and 2 make `u_a` an ordinary internal owner rather than a seam.  Hence no
inner guard or boundary cut is needed.  Conditions 3 and 4 verify the
remaining palette and residence gates.  QED

The same argument iterates along a chain.  Fusing `ell` one-edge sockets
arranged as one simple native path uses `ell+1`, rather than `2ell`, owner
occurrences and only two outer guards.

### Theorem 3.2 (alternating socket-chain replacement)

Let `F` be a background owner path forest with supported immediate palettes
`S_0^-` and `S_0^+`.  Suppose a source replacement deletes a set `C^+` of
upper providers and `C^-` of lower providers.  Let

\[
  P=(v_0,v_1,\ldots,v_t)
\]

be a clipped owner path which can be inserted at the replacement site.
Write

\[
  u_i=v_{i-1}\cup v_i,
  \qquad
  \ell_i=v_{i-1}\cap v_i
  \qquad(1\le i\le t).
\]

Assume:

1. the owners `v_i` are distinct and the clipped piece is residence-clean;
2. the `u_i` are distinct and the `ell_i` are distinct;
3. every source casualty is either retained elsewhere or recreated on the
   new path:

   \[
     C^+\subseteq S_0^+\cup\{u_1,\ldots,u_t\},
     \qquad
     C^-\subseteq S_0^-\cup\{\ell_1,\ldots,\ell_t\};            \tag{3.2}
   \]

4. every new externally required child colour of the replacement belongs
   to the same two sets on the right of (3.2);
5. the two outer traces and cuts are legal.

Then replacing the source by `P` creates no immediate-palette defect.  In
particular, every missing target among the `u_i` is repaired without a new
q1 hole.

#### Proof

All retained providers survive by definition of `S_0^+` and `S_0^-`.
Every nonretained casualty is recreated by (3.2).  Conditions 2 and 4 show
that the new path introduces no collision or unpaid child obligation.
Conditions 1 and 5 establish physical legality and residence.  Hence the
new immediate palettes contain the old palettes together with every newly
requested `u_i`.  QED

This is an alternating augment: a new edge may create or expose the target
needed by the next edge, while a later edge may pay an earlier source-cut
casualty.  Only the closed set condition (3.2) matters; individual one-edge
sockets need not be feasible in isolation.

### Proposition 3.3 (the `G-A-F-B` adjacent-socket augment)

Let `G,A,F,B` be four distinct middle owners.  Put

\[
  C=G\cup A,
  \qquad U=A\cup F,
  \qquad V=F\cup B.
\]

Suppose the separate candidate sockets for `U` and `V` are blocked only
because both insist on the same forced facet owner `F`.  Suppose further
that:

1. `G-A-F-B` is a simple, residence-clean clipped Johnson path;
2. its three lower colours are distinct and legal;
3. the source replacement casualties are retained in the background except
   possibly `C`;
4. `C` is recreated by the predecessor edge `G-A`;
5. the two outer traces and cuts are legal.

Then the one joint macro `G-A-F-B` realizes both target sockets `U` and `V`,
uses `F` once, recreates `C`, and creates no immediate-palette defect.
Consequently it reduces the socket-bank target deficiency by one whenever
one of `U,V` was the unique omitted target and the other was already the
routed replacement target.

#### Proof

Apply Theorem 3.2 to the path `G-A-F-B`.  Its upper colours are exactly
`C,U,V`.  The shared facet `F` is one internal owner, not two competing
owner occurrences.  By assumptions 3 and 4 every source casualty is
retained or appears on the path.  The lower, residence, and attachment
conditions are assumptions 1, 2, and 5.  Hence both sockets coexist in one
legal macro and no new q1 debt remains.  QED

In the bipartite target--facet incidence graph this macro is the alternating
path

\[
  G-C-A-U-F-V-B.
\]

Longer socket augments have the same form

\[
  v_0-t_1-v_1-t_2-\cdots-t_s-v_s,
  \qquad t_i=v_{i-1}\cup v_i,
\]

and are certified by Theorem 3.2 whenever their source casualties lie in
the retained palette plus the displayed `t_i`.

### Corollary 3.4 (the finite `8165/69605/75749` augment)

The native clipped owner path

\[
  8101\;--\;4069\;--\;67557\;--\;74725                    \tag{3.3}
\]

has upper colours

\[
  8101\cup4069=8165,
  \quad
  4069\cup67557=69605,
  \quad
  67557\cup74725=75749,                                    \tag{3.4}
\]

and lower colours

\[
  8101\cap4069=4005,
  \quad
  4069\cap67557=2021,
  \quad
  67557\cap74725=66533.                                    \tag{3.5}
\]

Both triples are pairwise distinct.  The four-owner piece is
residence-clean in its audited clipped context.  Every source-cut casualty
is present in the pre-atlas support list except `8165`, and the first edge
of (3.3) recreates `8165`.  Thus the same piece supplies both `69605` and
`75749` and pays its only local source casualty.  Applying Theorem 3.2 to a
global bank additionally requires every cited background provider to
survive the other selected cuts.  The first literal postbank replay shows
that this extra condition is not automatic.

The shorter component-`1209` segment

\[
  4069\;--\;67557\;--\;74725
\]

is the fusion core.  In particular, the shared use of owner `67557` must
not be treated as an unconditional owner conflict.

## 4. Hall form of the physical condition

Theorem 2.1 separates the palette argument from the physical selection
argument.  The latter may be certified in either of two ways.

1. **Independent-transversal form.**  Build the full incompatibility graph
   after path fusion and verify (2.3) or (2.5).

2. **Exact packet-Hall form.**  For every `X subseteq U`, the candidate
   packets in `union_{x in X} P_x` must contain `|X|` pairwise compatible
   representatives.  This is exactly the statement that the packet family
   admits an independent transversal; it is stronger than ordinary facet
   Hall when guards or upper tickets introduce extra conflicts.

Facet Hall alone is insufficient: all facet allocations can be distinct
while every packet uses the same one-capacity guard port.  Conversely, once
guards are included in the resource footprint, a typed-resource load bound
such as (2.5) is a checkable sufficient condition.

If the selected outer guard intervals have pairwise disjoint interiors,
the guard-interval transversal theorem supplies a global residence cut set:
force every selected outer endpoint, forbid every selected guard interior,
and choose one remaining cut in each still-unhit short-run defect interval.
Thus no additional global cut obstruction remains in that prepared face.

## 5. Consequence for the current finite model

The macro test has now been performed.

* The corrected row-only model has optimum omission count one: activating
  `75749` routes the omission to `69605`.
* Replacing the two separate target groups by the four-owner macro (3.3)
  makes the remaining 137 target groups simultaneously SAT.
* Independent clause replay verifies all `14,200,174` clauses of the
  `2,799,659`-variable model under the returned complete assignment.
* Independent semantic replay verifies 137 distinct nonmacro target rows,
  no owner overlap, no macro collision, every guard endpoint, no guard
  interior cut, every facet-run boundary, every residence-defect interval,
  and all four forced macro cuts.
* Minimizing the otherwise free cut variables gives 2013 distinct cuts,
  within the exact scalar allowance 2539.

These facts close the **abstract owner/guard/cut selector** obstruction and
prove that the former one-hole row conflict was caused by separating two
sockets which share a native facet path.  They do not close literal q1.

Exact replay of the materialized piece bank finds 19 raw-zero and 342
residence-extendable-zero q1 colours.  The reason is precise: the selector
treated membership in the pre-atlas provider list as permanent support,
while other selected cuts can delete every literal provider of such a
colour.  The next selector must carry explicit surviving-provider witness
variables (Section 7), or add them by CEGAR.  No `k=17` upper bound follows
from the present SAT witness.

## 6. General target

The general theorem still missing is now narrow:

> Construct, for every unsupported target, a large menu of one-debt socket
> packets such that legal native endpoint sharing is fused before conflicts
> are counted, and the resulting incompatibility graph satisfies the
> independent-transversal bound (2.3), or the exact packet-Hall condition.

Under that statement, the dependency-lasso theorem closes every initial
palette hole.  The palette side needs no monotone descent and no acyclic
dependency graph; directed cycles are the absorbers.

## 7. Exact literal-provider preservation

The postbank replay exposes a missing condition in the abstract selector.
Membership in a precomputed support list is not a persistent property: a
later cut or packet may delete every provider in that list.

Fix a colour `y`.  Let `M_y` be the internally delivering macros for `y`,
and let `W_y` be the exhaustive catalogue of literal external witnesses for
`y`.  A witness `w` has a finite survival condition

\[
  A_w=\bigwedge_{\ell\in L_w}\ell,             \tag{7.1}
\]

where the literals may require boundary cuts, forbid internal cuts, forbid
owner consumption by selected facets or guards, prescribe endpoint state,
and select the seam which actually joins the two endpoint states.  A macro
delivery may similarly have a conjunction `A_m`.

### Lemma 7.1 (literal-provider preservation)

Assume the catalogues `M_y` and `W_y` are exhaustive for the chosen physical
construction class.  Then a selected boundary cut whose child obligation
is `y` is sound if and only if

\[
  \bigvee_{m\in M_y}A_m
  \quad\vee\quad
  \bigvee_{w\in W_y}A_w.                       \tag{7.2}
\]

If a cut variable `z_e` is what creates the obligation, its exact conditional
form is

\[
  z_e\Longrightarrow
  \left(
    \bigvee_{m\in M_y}A_m\vee
    \bigvee_{w\in W_y}A_w
  \right).                                     \tag{7.3}
\]

#### Proof

Every occurrence of `y` in the final chronology is, by exhaustiveness,
either an internal edge of one selected macro or an external seam/retained
edge represented by one witness in `W_y`.  Such an occurrence exists
exactly when its complete survival conjunction holds.  Therefore `y` is
present exactly when (7.2) holds, and conditioning on the cut gives (7.3).
QED

### CNF encoding

Introduce one atom `a_w` for each witness and add

\[
  \neg a_w\vee\ell
  \qquad(\ell\in L_w).                         \tag{7.4}
\]

Do the same for conjunctive macro deliveries.  Then add the monotone
provider clause

\[
  \neg z_e
  \vee
  \bigvee_{m\in M_y}a_m
  \vee
  \bigvee_{w\in W_y}a_w.                       \tag{7.5}
\]

Only the forward implications (7.4) are needed: a satisfying assignment
may decline to certify a witness which happens to survive, but every
certified witness is real.  The size of this encoding is

\[
  O\!\left(\sum_y\sum_{w\in W_y}|L_w|\right).
\]

It is an OR-of-ANDs in the physical literals and a monotone OR in the
introduced witness atoms.

The witness menu must be joined to the **entire contemporaneous candidate
bank**, not only to the incumbent solution.  If `O(w)` is the owner-position
set reserved by witness `w`, then every socket, guard, or macro candidate
`p` added to the selector requires

\[
  \neg a_w\vee\neg x_p                              \tag{7.6}
\]

whenever `p` consumes a position in `O(w)`, unless their overlap is an
explicitly certified native fusion.  Likewise, if `B(w)` and `I(w)` are the
required boundary cuts and forbidden internal cuts, add

\[
  \neg a_w\vee z_b \quad(b\in B(w)),
  \qquad
  \neg a_w\vee\neg z_i \quad(i\in I(w)).             \tag{7.7}
\]

Thus newly introduced raw-hole sockets, second-generation (`J2`) macros,
and later CEGAR candidates are automatically covered by the same rule.
Using a witness table against a later candidate bank without regenerating
(7.6)--(7.7) is unsound.

### Exact CEGAR form

One need not add all provider clauses eagerly.

1. Solve the owner/guard/cut selector.
2. Materialize and replay the literal palette.
3. For every newly missing colour `y`, enumerate its exhaustive witness
   menu and add (7.4)--(7.5).
4. Repeat.

Once the clause for `y` has been installed, `y` cannot reappear as a literal
hole in a later model.  Hence q1 CEGAR terminates after at most the number of
q1 colours, provided each witness catalogue is exhaustive.  If `W_y` and
`M_y` are both empty while `z_e` is forced, (7.5) immediately certifies
UNSAT for that construction class.

Theorem 2.1 must therefore be read with `S_0` equal to the **literally
retained** background palette certified by (7.2), not the union of colours
which appeared somewhere in the pre-atlas.  With this correction, the
dependency-lasso proof is unchanged.
