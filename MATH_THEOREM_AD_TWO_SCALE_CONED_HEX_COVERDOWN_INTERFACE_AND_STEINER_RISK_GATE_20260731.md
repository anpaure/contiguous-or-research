# Two-scale coned-hex cover-down: exact interface and the first global gates

Date: 2026-07-31  
Lane: AD  
Status: exact native constant absorber, exact conditional two-scale
composition theorem, and sharp interface obstructions.  No prescribed
positive-density matching extension, fixed-`Q` long-ear bank, AGCF-to-side
realization, or all-parameter completion theorem is claimed.

## 0. Verdict

The proposed two scales are numerically compatible, and the constant scale
has a particularly clean native gadget.

* A standard Boolean incidence hexagon becomes a literal atom of the
  fixed-`Q` side host after adjoining one fresh coordinate only on its upper
  shore.  Its two alternating three-edge phases use the same three lower
  resources, the same three upper resources, and the same six physical
  owner slots.  Deleting one edge from one phase turns the remaining
  `2 -> 3` switch into a gain-one absorber for that designated legal side
  atom.  Every legal side atom lies in such a coned hex for `n>=3`.
* The full unpunctured host contains a pairwise resource-disjoint bank of at
  least `ceil(N/72)` such supports.  Raw puncture risk is at most three per
  support, so uniform common-basis marginals leave at most `C/24` uncertified
  gadgets after retaining exactly `floor(N/72)` of them.  If the complete
  exterior guard has risk at most nine, the corresponding bound is `C/8`.
* For `n>=5`, `C/8` worst-length native gain-one ears fit the scalar one-shore
  storage budget.  Thus the metric order and constants do not obstruct the
  two-scale architecture.

What is **not** supplied by these facts is the global interface.

1. The surviving old halves of `Theta(N)` coned hexes must extend jointly
   to one fixed-`Q` matching whose leave is exactly their designated target
   atoms.  Individual survival and pairwise support disjointness do not imply
   this common off state.  The protected Delcourt--Postle theorem permits an
   `o(P)` reserve, whereas this bank has positive density.
2. Constant literal support does not imply constant puncture risk once the
   packet's exterior graphic signature is protected.  In a forest, the exact
   additional risk is the minimal Steiner subtree joining its ports; that
   subtree can have length `Theta(n)` or larger.
3. Every bad constant gadget must export **one native gain-one boundary**.
   A balanced alternating circuit has boundary zero and cannot reduce a
   cover-down deficiency.  The AGCF all-candidate absorber has the right
   nonzero-boundary logic but lives in a different resource hypergraph; a
   fixed-`Q` side realization or positive-semigroup grouping is still needed.
4. Stage-two ears must be tested in the graphic matroid after the actual
   stage-one choice is contracted.  Separate graphic tests at the two scales
   do not compose.

Theorem 5.1 below is the exact positive implication once these four rows are
assumed.  Sections 6--8 prove that none may be omitted from a black-box
composition of the current theorems.

## 1. Parameters and typed side atoms

Use the side-forest notation

\[
 K=\operatorname {Cat}_n,\qquad
 N=\binom{2n}{n-1}=nK,\qquad
 P=\binom{2n}{n-2}={n(n-1)\over n+2}K,
\]

\[
 C=\operatorname {Cat}_{n+1},\qquad
 \alpha={C\over N}={2(2n+1)\over n(n+2)}< {4\over n}.       \tag{1.1}
\]

After choosing a common basis `Q` and deleting the forced slot baseline, a
side atom has four typed resources

\[
             e=(D,V;x,y),                                      \tag{1.2}
\]

where `D` is a surviving rank-`n` outer resource, `V` is a rank-`n+2`
outer resource containing `D`, and `x,y` are the two rank-`n+1`
intermediates between them, with their actual capacity-slot labels.  Its
physical image is the Johnson edge `xy`.

For a packet with old atom set `R` and new atom set `A`, write

\[
              \partial(R,A)={\bf a}(A)-{\bf a}(R)               \tag{1.3}
\]

for its signed four-resource incidence vector.  A circuit has boundary
zero.  A gain-one cover-down ear for target atom `e` has boundary
`a(e)`.

This distinction is invariant under every sequence of balanced switches.

## 2. The native one-point-coned hex absorber

Let `Omega` have order `2n`.  Choose

\[
 H\in\binom\Omega{n-1},\qquad
 z\notin H,\qquad
 \{a,b,c\}\subseteq\Omega\setminus(H\cup\{z\})                 \tag{2.1}
\]

with `a,b,c` distinct.  Put

\[
 D_a=H+a,\quad D_b=H+b,\quad D_c=H+c,                            \tag{2.2}
\]

\[
 V_a=H+b+c+z,\quad V_b=H+c+a+z,\quad V_c=H+a+b+z.               \tag{2.3}
\]

There are two alternating side matchings

\[
 \begin{aligned}
 {\cal P}&=\{(D_a,V_c),(D_b,V_a),(D_c,V_b)\},\\
 {\cal N}&=\{(D_a,V_b),(D_b,V_c),(D_c,V_a)\}.                   \tag{2.4}
 \end{aligned}
\]

### Theorem 2.1 (coned-hex four-resource transparency)

The two phases in (2.4) use exactly the same twelve typed host resources:
the three `D` resources, the three `V` resources, and once each the six
physical owners

\[
 X_{ab}=H+a+b,\quad X_{bc}=H+b+c,\quad X_{ca}=H+c+a,
\]

\[
 Z_a=H+a+z,\quad Z_b=H+b+z,\quad Z_c=H+c+z.                     \tag{2.5}
\]

The same slot copy may therefore be used at every owner in both phases.
Consequently, for any designated edge `e in P`,

\[
              {\cal P}\setminus\{e\}\ \longrightarrow\ {\cal N} \tag{2.6}
\]

is a native gain-one absorber with

\[
       \partial({\cal P}\setminus\{e\},{\cal N})={\bf a}(e).   \tag{2.7}
\]

Every legal unpunctured side atom belongs to a coned hex of this form when
`n>=3`.

#### Proof

For an incidence `(D_x,V_y)` in (2.4), the two intermediates are one plain
upper hex port `X_ij` and the coned lower port `Z_x`.  Reading the six edges
in (2.4) shows that each of the six vertices in (2.5) occurs once in either
phase.  Both phases also match the same three `D` and the same three `V`
resources, proving four-resource transparency.  Subtracting the two equal
full incidence vectors after removing `e` gives (2.7).

Conversely let `e=(D,V)` be any legal atom.  Order the two elements of
`V-D` as `b,z`, choose `a in D`, put `H=D-a`, and choose

\[
                  c\in\Omega\setminus V.                         \tag{2.8}
\]

There are `n-2>=1` choices for `c`.  Then `D=D_a` and `V=V_c`, so `e` is
the first edge of `P`.  `square`

The theorem is stronger than a bare outer alternating cycle: the owner-slot
multiset also agrees.  It is weaker than exterior transparency.  Re-pairing
the six ports can merge, split, or rethread components of the retained
physical graph, and that effect is not determined by (2.1)--(2.5).
Likewise, if a central alternating decoration must be retained, the known
coherent-external-label test on the two shores remains an additional local
guard.  Four-resource side transparency neither implies nor requires that
decoration condition.

### Theorem 2.2 (positive-density full-host bank)

For `n>=4`, the unpunctured side host contains at least

\[
                         \left\lceil {N\over72}\right\rceil       \tag{2.9}
\]

pairwise disjoint coned-hex supports, where disjointness includes all three
lower resources, all three upper resources, and all six physical owners.
If a predeclared protected resource set has order `z_0`, one retains at
least

\[
                         {N\over72}-{z_0\over12}                   \tag{2.10}
\]

supports before integer rounding.

#### Proof

The number of distinct supports is

\[
              G=N(n+1)\binom n3:                                 \tag{2.11}
\]

choose `H`, then `z`, then the unordered triple `{a,b,c}`.  The support is
recovered from the intersection of its three `D` resources, their three
new letters, and the common extra `z` in the `V` resources, so there is no
overcount.

By transitivity, the degrees of a lower resource, upper resource and
physical owner in this twelve-uniform support hypergraph are respectively

\[
 d_D={3G\over\binom{2n}n},\qquad
 d_V={3G\over P},\qquad
 d_X={6G\over N}=n(n-1)(n-2)(n+1).                              \tag{2.12}
\]

For `n>=4`, `d_X` is the maximum.  A maximal disjoint family of `t`
supports meets every support.  Charging an intersecting support to one of
the twelve resources in a selected support gives

\[
                 G\le12t d_X,\qquad t\ge {G\over12d_X}={N\over72}. \tag{2.13}
\]

Deleting supports meeting a protected set removes at most `d_X z_0`
supports before the same argument, proving (2.10). `square`

This is a prospective support bank.  The theorem does **not** place the two
old edges of every absorber into one matching.

## 3. Common-basis survival and exterior closure

The uniform common-basis law has

\[
                      \Pr(q\in Q)=\alpha                         \tag{3.1}
\]

for every child atom.  For one precomputed packet let `R_i` be the complete
set of child atoms whose puncture can invalidate its declared semantics.
The common-basis puncture-survival theorem gives a `Q` for which

\[
               |B|\le\alpha\sum_{i\in I}|R_i|,                   \tag{3.2}
\]

where `B` is the set of uncertified single-option packets.  Hence, for
exactly `floor(N/72)` coned hexes,

\[
 \begin{array}{c|c}
 |R_i|\le3& |B|\le C/24,\\
 |R_i|\le9& |B|\le C/8,
 \end{array}                                                     \tag{3.3}
\]

up to the harmless floor improvement.

The first row is only the raw local puncture risk.  The second row is useful
only if all exterior state has truly been closed by six additional child
atoms.  The next lemma shows why that is a substantive hypothesis.

### Lemma 3.1 (exact port-Steiner closure)

Let `F` be a forest and `S` a finite set of declared packet ports.  In each
component of `F`, let `T_F(S)` be the minimal subtree spanning the ports in
that component, with all nonport leaves pruned.  For an edge-deletion set
`Q_F`, the partition of `S` into components of `F-Q_F` is the same as its
partition in `F` if and only if

\[
                          Q_F\cap E(T_F(S))=\varnothing.           \tag{3.4}
\]

In particular, two relevant ports at distance `d` on a path contribute
exactly `d` edges to the exterior risk.

#### Proof

An edge outside `T_F(S)` lies on no path between two ports and hence cannot
change the port partition.  Every edge of the pruned Steiner subtree
separates two nonempty port sets; deleting it separates a pair of ports that
were connected in `F`.  This proves both directions. `square`

When child punctures delete physical forest edges or the occurrences that
support them, their preimages must be added to `R_i`.  Thus a twelve-resource
hex can have `Theta(n)` or larger **exterior-closed** risk.  If
`|R_i|=lambda n`, then

\[
                       \alpha|R_i|\longrightarrow4\lambda,       \tag{3.5}
\]

and the one-point theorem no longer gives an `o(1)` bad fraction.  A valid
Stage 1 therefore needs bounded-diameter or laminar port closure, or a
different `Q`-independent graphic labelling theorem.

Call a packet **exterior-transparent** when its risk set includes:

1. every local atom needed in both phases;
2. the entire port-Steiner closure needed to keep its contracted component
   signature fixed;
3. every protected anchor/root witness on which its legality depends; and
4. every cap guard not already protected by literal owner-slot equality.

Only exterior-transparent packets may be charged by (3.2) while retaining a
predeclared graphic link.

## 4. The common-off-state and gain interfaces

Let `A_Q` be the incidence matrix of the balanced fixed-`Q` side host,
including actual owner slots.  A Stage-1 packet for target atom `e_i` has an
off set `O_i` and an on set `N_i` satisfying

\[
                       A_Q({\bf1}_{N_i}-{\bf1}_{O_i})=A_Q{\bf1}_{e_i}. \tag{4.1}
\]

For the coned hex, `|O_i|=2` and `|N_i|=3`.

A family has an **installed common off state** if there is one current
matching `M_Q^-` and one `Q`-legal installed off block `O_i(Q)` for every
packet such that all `O_i(Q)` are disjoint subsets of `M_Q^-`, every option
used for packet `i` starts from that same block, and, after the affine slot
baseline is removed,

\[
           {\bf1}_{\rm host}-A_Q{\bf1}_{M_Q^-}
                  =\sum_{i\in I}{\bf f}_i(Q).                     \tag{4.2}
\]

Here `f_i(Q)` is the legal fixed-`Q` four-resource boundary vector
exported by that installed block: one lower resource, one upper resource,
and two available owner slots.  It need not itself be the column of a direct
host atom.  For a good coned hex it equals `A_Q e_i`.  For a packet whose
local target or off phase was punctured, `f_i(Q)` must instead be an
explicitly authenticated fallback boundary; it is not defined to be the
now-illegal original atom.

Equation (4.2), not individual packet existence, is the exact edge-aligned
cover-down state.  Switching a good set `G` leaves precisely

\[
                          \sum_{i\in I\setminus G}{\bf f}_i(Q).     \tag{4.3}
\]

If puncturing invalidates an off state, a fallback must replace it in
`M_Q^-`; merely deleting the invalid old atom need not preserve (4.2).

There are two possible Stage-2 types.

* A **zero-boundary circuit** has `A_Q(N-R)=0`.  It can repair physical
  degree, anchor or topology defects inside a fixed matching, but (4.3) is
  unchanged.
* A **gain-one ear for a legal boundary `f_i(Q)`** has

  \[
                         A_Q({\bf1}_N-{\bf1}_R)={\bf f}_i(Q).      \tag{4.4}
  \]

  Only this type reduces the remaining cover-down leave by one native side
  atom.

The AGCF all-candidate absorber has an analogous nonzero-boundary identity,
but its target column has `(n+1,n,n)` resources in the AGCF path host, not
four resources in `G_Q`.  To use it here one must prove a native map or a
grouping such that the residual vector in (4.3) lies in the positive
semigroup of resource-disjoint realized AGCF candidate boundaries.  A
cardinality bound on `I-G` and the AGCF flux lattice do not imply that
grouping; the parameter-three semigroup-hole theorem from item `2301AD`
already rules out that inference.

## 5. Exact conditional two-scale completion

### Theorem 5.1 (two-scale exterior-transparent cover-down)

Fix `n`, a synchronized common basis `Q`, its affine slot baseline, and a
protected physical scaffold.  Let `I` be a Stage-1 target set.  Assume:

1. **Installed edge-aligned Stage 1.**  Equation (4.2) holds for one
   fixed-`Q` matching `M_Q^-`.  For a good packet, `M_Q^-` contains its
   standard coned-hex off state.  For a bad packet whose standard off state
   was punctured, it instead contains an explicitly declared fixed-`Q`
   fallback off state exporting one legal boundary `f_i(Q)`.
   Equation (4.2) uses `f_i(Q)=A_Qe_i` for good packets and these
   fallback boundaries for bad packets.  The installed packet supports are pairwise
   resource-disjoint, and every good packet is exterior-transparent.  The
   common basis was chosen so the bad set `B` satisfies (3.2).
2. **Stage-1 cap and graphic guards.**  Switching every packet in
   `I-B` preserves every ordinary cap-two owner and cap-one protected
   anchor.  After deleting the switched old states, all selected new edges
   are independent in the contracted graphic matroid.  The retained good
   packet resources are then closed against Stage 2, except for explicitly
   declared attachment ports with recorded residual capacity.
3. **One native fallback per bad packet.**  After the Stage-1 switches, the
   residual leave is exactly the disjoint union of the legal columns
   `f_i(Q)`, `i in B`; no bad packet creates a second outer or slot deficit.
   For every `i in B` there is a fixed-`Q` gain-one Stage-2 option family
   satisfying (4.4), all with one installed common off state `R_i`
   contained in the current matching.
4. **Cross-scale privacy and caps.**  The sets `R_i` are pairwise disjoint
   and avoid every closed Stage-1/scaffold resource.  Different Stage-2
   options may meet the retained graph only at declared, slot-distinct
   attachment ports.  After deleting all `R_i`, the remaining physical
   graph `F_0` is a forest, and every option is internally a forest and
   obeys

   \[
             d_{F_0}(v)+d_{\rm option}(v)\le b(v),                 \tag{5.1}
   \]

   with `b(v)=1` at protected anchors and `b(v)=2` otherwise.
5. **Joint graphic/root row.**  Suppress the private internal vertices of
   every Stage-2 option.  Its remaining links form a packet in the graphic
   matroid on the components of `F_0`.  There is one option per `i in B`
   whose union is independent in that matroid.  This is already a joint
   cross-scale test because `F_0` contains and contracts the actual retained
   Stage-1 edges.  If exactly one root per final component is required,
   first require every component of `F_0` to contain at most one root; then
   add a root-star edge at every root-bearing component and require the union to
   satisfy the following exact condition: the fixed root-star edges together
   with the selected links form a spanning tree.  Equivalently, the selected
   links form a tree after contracting the fixed root-star edges.

Then all fixed-`Q` required boundaries are absorbed.  The resulting atom set covers every
nonbaseline host resource exactly once, obeys every physical cap and
protected anchor, and its physical projection is a forest with the stated
root condition.

#### Proof

By (4.1)--(4.3), switching the good Stage-1 packets leaves exactly the bad
fallback columns.  Hypothesis 3 and (4.4) cover each of those columns exactly
once while preserving all resources already covered.  Common off states and
cross-scale privacy make all atom replacements simultaneous matchings.
Hypothesis 4 proves the local degree and anchor rows.  After deleting every
old state, adding the selected private option forests creates a physical
cycle exactly when their suppressed links are dependent in the contracted
graphic matroid.  Hypothesis 5 excludes this.  The standard root-star
criterion gives at most and at least one root simultaneously. `square`

The theorem is deliberately sequential only in its proof.  Its graphic row
is joint: the actual Stage-1 links are already present when Stage 2 is
tested.

### Corollary 5.2 (calibrated scalar compatibility)

Take exactly `floor(N/72)` Stage-1 coned hexes with exterior risk at most
nine.  Then some common basis has

\[
                            |B|\le C/8.                            \tag{5.2}
\]

Suppose every bad packet satisfies the one-native-fallback clause and has a
private gain-one ear whose old state has order at most `n+1`.  The raw
one-shore storage inequality is

\[
                           |B|(n+2)\le P.                          \tag{5.3}
\]

For (5.2), its left/right ratio is

\[
 { (n+2)C\over8P}
       ={(n+2)(2n+1)\over4n(n-1)}\le1\qquad(n\ge5).               \tag{5.4}
\]

Thus scalar storage is sufficient for every `n>=5`.  With raw risk three,
the same ratio is divided by three.  This proves only capacity.  The
installed common off states, native fallback, private packing, and joint
graphic/root row remain the hypotheses of Theorem 5.1.

If each bad gadget exports `g` gain-one tokens rather than one, multiply
the left side of (5.4) by `g`.  For risk nine, `g=2` would require

\[
              (n+2)(2n+1)\le2n(n-1),                              \tag{5.5}
\]

whose left side exceeds the right by `7n+2`.  Therefore the one-native-
fallback clause is quantitatively load-bearing, not cosmetic.

## 6. Common-off extension is not a marginal statement

### Proposition 6.1 (smallest forced-edge extension obstruction)

Let a bipartite graph have left vertices `a,b,c`, right vertices `1,2,3`,
and edges

\[
              a1,a2,b1,b3,c2,c3.                                  \tag{6.1}
\]

The vertex-disjoint edges `a1` and `c3` are each contained in a perfect
matching, but no perfect matching contains both.

#### Proof

The perfect matchings

\[
                 \{a1,b3,c2\},\qquad \{a2,b1,c3\}                 \tag{6.2}
\]

prove the two individual extensions.  After forcing `a1,c3`, the unmatched
left vertex `b` has only the already occupied neighbours `1,3`. `square`

Thus even individual extendability plus resource disjointness does not give
the common off state (4.2).  In the four-resource host the corresponding
forced-edge problem also includes slot and graphic rows.

There is a separate quantitative issue.  A bank of `Theta(N)` coned hexes
contains `Theta(N)=Theta(P)` old atoms.  The protected Delcourt--Postle
theorem loses `O(|Z|)` when their closed supports are reserved, and hence
only proves coexistence for `|Z|=o(P)`.  The positive-density bank must be
chosen jointly with the bulk or handled by a new Delcourt--Postle theorem
conditioned on a prescribed positive-density partial matching.

## 7. Separate graphic tests do not compose

### Proposition 7.1 (three-component cross-scale obstruction)

Let the contracted base forest have three components `A,B,C`.  Suppose
Stage 1 selects the independent links `AB,BC`, while the only Stage-2 link
is `CA`.  Stage 1 is graphically valid, and `CA` is independently valid
against the original base forest, but their union is a triangle.

After contracting the actual Stage-1 forest, `CA` is a loop.  Hence testing
the two stages in separate copies of the original graphic matroid is
unsound.  Hypothesis 5 of Theorem 5.1 is the weakest ordinary-graphic repair
of this issue.

The same point applies to cap guards.  Internal corridor disjointness is
not enough if two scales use the same attachment slot.  Either the ports are
cross-scale private or the selection problem has an additional partition-
capacity matroid; ordinary graphic Rado alone then no longer suffices.

## 8. Exact first false conditions

The proposed two-scale implication is valid neither from local absorber
existence nor from order notation alone.  Reading it in construction order,
the first unsupported condition is:

> **Positive-density common-off extension.**  After choosing the synchronized
> common basis, the surviving coned-hex old halves and the bulk side atoms
> extend to one capacity-safe physical forest whose exact leave consists of
> the designated target columns.

Theorem 2.1 proves each local packet.  Theorem 2.2 packs prospective supports.
The common-basis theorem bounds how many declarations are punctured.  None
of them proves the displayed extension, and the current protected-reserve
theorem is quantitatively outside its range.

Even if that row is added, the next two independent gates are:

1. **bounded exterior risk:** the relevant port-Steiner/guard closure must
   be `O(1)` (nine in the calibrated row), not merely the literal gadget;
2. **native installed fallback:** every bad gadget must become one fixed-`Q`
   gain-one ear with a common off state, not a zero-boundary circuit or an
   untyped AGCF candidate.

Finally the ears must pass the joint contracted graphic/root and cap rows.
These statements are strictly stronger than local hex transparency and
strictly weaker than a global all-at-once circuit: they are the exact
two-scale interface now left to prove.

## 9. Dependencies and scope

The marginal estimate uses Theorem 4.2 of
`MATH_THEOREM_K_COMMON_BASIS_PRIVATE_CIRCUIT_ALTERATION_20260731.md`.
The detailed coned-hex catalogue and puncture audit is independently frozen
in
`MATH_THEOREM_AD_TWO_SCALE_STAGE1_ALPHA_HEX_PACKING_AND_PUNCTURE_GATE_20260731.md`.
The gain-one capacity arithmetic is independently audited in
`MATH_AUDIT_AD_TWO_SCALE_STAGE2_PRIVATE_CIRCUIT_CAPACITY_20260731.md`.
The AGCF semigroup warning is the exact parameter-three obstruction in
`MATH_OBSTRUCTION_CATALAN_EDGE_ALIGNED_COVERDOWN_N3_SEMIGROUP_HOLE_20260731.md`.

Nothing here proves the positive-density common-off extension, bounded
Steiner closure, a `Q`-punctured long-ear bank, the AGCF-to-side realization,
residence, deeper shadows, a literal compiler, or `nu(k)=B(k)`.
