# PBBS prefix switching: socket obstruction, fault-tolerant banks, and the return gate

Date: 2026-07-30
Lane: R, pure-mathematics all-`k` compiler lane
Status: exact permanent-switching audit, sharp abstract socket obstruction,
and a deletion-stable sufficient switch-bank theorem.  No actual PBBS
reciprocal rectangle and no unconditional `B(k)+O(k)` theorem are claimed.

## 0. Outcome

The same-component permanent inequality in handoff item 1997 is valid.
For two disjoint residual candidate edges `e,f`, if `mathfrak B_H(e,f)` is
the weighted mass of pairs `(M_11,M_00)` in which `e,f` belong to the same
alternating component, then

\[
 Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).                 \tag{0.1}
\]

The proposed conclusion

\[
 \Pr(e,f)\le(1+\gamma/d)\Pr(e)\Pr(f)                            \tag{0.2}
\]

does not follow from unit closure, Hall feasibility, or the mandatory-core
candidate sandwiches.  The smallest obstruction is `K_(2,2)`: its two
saturating matchings are the two shores of one alternating cycle, and the
larger of the two shore-cylinder ratios is at least two.  There is no
separating switch.  The nondegenerate complete socket `K_(2,n)` has exact
uniform cylinder ratio

\[
                         {n\over n-1},                              \tag{0.3}
\]

so even the best symmetric two-row socket needs `n=Omega(d)` for (0.2).
For arbitrary two-row neighborhoods `A,B`, the exact cross-closed ratio is

\[
 1+{|A\cup B|-1\over(|A|-1)(|B|-1)}.                              \tag{0.4}
\]

In the raw PBBS mandatory-core envelope table, four reciprocal candidate edges
on targets `S,R` and columns `I,J` exist exactly when

\[
 F(I)\cup F(J)\subseteq S\cap R,
 \qquad S\cup R\subseteq P(I)\cap P(J).                           \tag{0.5}
\]

They expose the sharp `K_(2,2)` obstruction only when a residual prefix
also isolates those four vertices.  Current PBBS theorems neither prove nor
exclude such an isolated reciprocal sandwich; this report does not assert
one exists.

There is nevertheless an exact deletion-stable positive theorem.  Suppose
every exceptional input has a master bank of `Q` separating switches, every
graph vertex lies in at most `rho` switch supports, each surviving output
has product weight at least `eta` times its input, and output incidence
congestion is at most `b`.  For `gamma>0`, a prefix of at most `d-1`
matching edges kills
at most `2rho(d-1)` switches.  Hence

\[
 [Q-2\rho(d-1)]\eta\ge {bd\over\gamma}                            \tag{0.6}
\]

proves (0.2) in every required endpoint-deleted prefix.  This is the
correct fault-tolerant form of the external guard-bridge gate.

Finally, a distinct link between two PBBS interval columns contained in one
flat convex hull forces an actual erosion-coordinate return there.  A return-free flat
hull has no nontrivial interval links at all.  Thus local all-depth support
cannot supply the switches in (0.6): the bank must be built from PBBS
returns, ramps, or links leaving the hull, with bounded endpoint and output
congestion.  Under the protected common-extension hypotheses of Proposition
7.1, an unbraided parent bank transfers to its child interior.  The Pascal
identities alone preserve only candidates and event ports; they do not
control new promoted-collar inputs, return links, or component mergers.
Consequently they do not yet transfer an additive `O(k)` compiler theorem.

## 1. Residual matching notation

Let `H=(mathcal S,mathcal I;E)` be a finite bipartite graph with positive
edge weights.  Its left vertices are retained strict lower targets and its
right vertices are residual physical interval columns.  Every matching
under discussion saturates all of `mathcal S`; right vertices need not all
be used.

Fix two disjoint extendable edges `e,f`.  Let `Z_ab` be the total weight of
saturating matchings in which their status vector is `(a,b)`.  For an
ordered pair `(M_11,M_00)`, its symmetric difference is a disjoint union of
alternating cycles and right-to-right alternating paths.  Put

\[
 \mathfrak B_H(e,f)=
 \sum_{(M_{11},M_{00}):\ e,f\text{ in one component}}
       w(M_{11})w(M_{00}).                                         \tag{1.1}
\]

For a PBBS chronology, a physical interval column `I` has maximal envelope
`P(I)` and mandatory core `F(I)`.  A strict lower target `S` is a candidate
on `I` precisely when

\[
                         F(I)\subseteq S\subseteq P(I).             \tag{1.2}
\]

All prefix deletions below are endpoint deletions caused by conditioning a
partial matching.  Additional physical failed-literal pruning is not
silently identified with endpoint deletion.

## 2. The item-1997 permanent inequality is valid

### Theorem 2.1 (same-component error is exact)

For every positively weighted residual matching graph,

\[
 \boxed{Z_{11}Z_{00}\le Z_{10}Z_{01}+\mathfrak B_H(e,f).}         \tag{2.1}
\]

If `Z_10 Z_01>0` and

\[
 \mathfrak B_H(e,f)\le\beta Z_{10}Z_{01},                         \tag{2.2}
\]

then

\[
 \boxed{\Pr_H(e,f)\le(1+\beta)\Pr_H(e)\Pr_H(f).}                 \tag{2.3}
\]

#### Proof

For a pair `(M_11,M_00)` in which `e,f` lie in different alternating
components, swap between the two matchings the component containing `f`.
The result has statuses `10,01`, remains saturating, and has the same
product weight.  The operation is invertible on its image.  Only the pairs
counted by (1.1) escape, proving (2.1).

Writing `Z=Z_11+Z_10+Z_01+Z_00`, (2.1) is equivalent to

\[
 Z_{11}Z\le (Z_{11}+Z_{10})(Z_{11}+Z_{01})
                +\mathfrak B_H(e,f).                              \tag{2.4}
\]

The product on the right is at least `Z_10Z_01`; divide by `Z^2` and use
(2.2).  QED.

When `Z_10Z_01=0`, the ratio certificate (2.2) is unavailable.  A direct
pair estimate is then an additional hypothesis, not a consequence of
(2.1).  This zero-status case is exactly where the smallest socket below
lives.

## 3. Exact two-row socket obstructions

### Theorem 3.1 (minimal weighted `K_(2,2)` obstruction)

Let `H=K_(2,2)` with target rows `S,R`, interval columns `I,J`, and positive
edge weights.  Put

\[
 A=w(S,I)w(R,J),\qquad B=w(S,J)w(R,I),\qquad
 p={A\over A+B}.                                                   \tag{3.1}
\]

For the shore edges `e=(S,I),f=(R,J)`,

\[
 \Pr(e)=\Pr(f)=\Pr(e,f)=p,
 \qquad {\Pr(e,f)\over\Pr(e)\Pr(f)}={1\over p}.                  \tag{3.2}
\]

For the opposite shore the ratio is `1/(1-p)`.  Consequently

\[
 \boxed{\max\{1/p,1/(1-p)\}\ge2.}                                \tag{3.3}
\]

For either shore, `Z_10Z_01=0`; the unique opposite matching is in the
same alternating four-cycle, so there is no separating output and `q=0`.
Hence the all-pair factor `1+gamma/d` fails for every fixed `gamma` once
`d>gamma`.

This is the smallest simple bipartite example with no degree-one target
row and with two saturating matchings.

#### Proof

The only saturating matchings are the two shores, of product weights `A`
and `B`.  Equations (3.1)--(3.3) follow directly.  A disjoint pair requires
at least two target vertices and two interval vertices.  If all target
degrees are at least two on those four vertices, the graph is `K_(2,2)`.
QED.

### Proposition 3.1a (every isolated alternating cycle is an obstruction)

Let one residual connected component be an induced even cycle `C_(2s)`,
`s>=2`, with positive edge weights.  It has exactly two target-saturating
matching shores, of probabilities `p` and `1-p`.  Any two distinct edges
on one shore have joint probability and both marginals equal to that
shore probability.  Hence the larger of the two shore-cylinder ratios is
at least two, and no separating switch exists.

#### Proof

An even cycle has exactly its two alternating perfect matchings.  Apply the
calculation (3.2)--(3.3) verbatim.  QED.

Thus excluding isolated reciprocal `K_(2,2)` sockets is not sufficient:
longer isolated alternating-cycle faces have the same perfect-correlation
obstruction.  The two-row formulas below are sharp necessary diagnostics,
not a complete expansion criterion.

The `K_(2,2)` graph of Theorem 3.1 has no row-degree unit.  If both shores are additionally declared
physical pair conflicts, however, failed-literal or arc-consistency closure
detects the impossibility: conditioning any edge eliminates both choices
of the other target, one by column collision and one by the physical
conflict.  Thus the example is a sharp matching/permanent obstruction, but
it must not be advertised as surviving every stronger physical closure.

### Theorem 3.2 (complete socket `K_(2,n)`)

Give `K_(2,n)`, `n>=3`, unit edge weights and the uniform law on its
target-saturating matchings.  For two opposite-row edges `e,f` on distinct
columns,

\[
 \boxed{{\Pr(e,f)\over\Pr(e)\Pr(f)}={n\over n-1}.}                \tag{3.4}
\]

Moreover

\[
 Z_{11}=1,\quad Z_{10}=Z_{01}=n-2,
 \quad Z_{00}=n^2-3n+3,                                           \tag{3.5}
\]

and

\[
 \boxed{\mathfrak B_H(e,f)=2n-3.}                                \tag{3.6}
\]

Thus, for `gamma>0`, the direct estimate (0.2) requires

\[
                         n-1\ge d/\gamma,                          \tag{3.7}
\]

whereas the sufficient same-component ratio (2.2) requires the slightly
stronger exact inequality

\[
                         {2n-3\over(n-2)^2}\le{\gamma\over d}.    \tag{3.8}
\]

#### Proof

A saturating matching is an ordered pair of distinct columns, so there are
`n(n-1)` matchings.  A fixed row edge has probability `1/n`, while a fixed
disjoint pair has probability `1/[n(n-1)]`, proving (3.4) and (3.7).

After fixing the `11` matching, a `10` or `01` matching has `n-2` choices.
Subtraction from `n(n-1)` gives `Z_00` in (3.5).  An avoiding matching lies
in the same alternating component as both distinguished edges exactly when
it uses at least one of the two cross edges.  There are `n-1` choices using
the first cross edge, `n-1` using the second, and their intersection is the
single swapped matching.  This gives `2n-3`, and (3.8) follows from (2.2).
QED.

### Theorem 3.3 (arbitrary uniform two-row formula)

Suppose a residual connected component has exactly two target rows with
neighborhoods `A,B` in the interval shore.  Put

\[
 a=|A|,\qquad b=|B|,\qquad c=|A\cap B|.                            \tag{3.9}
\]

Under the uniform saturating-matching law there are `ab-c` matchings.  If
`i,j` are distinct columns in `A\cap B`, take
`e=(S,i),f=(R,j)`.  Then

\[
 \boxed{
 {\Pr(e,f)\over\Pr(e)\Pr(f)}
 ={ab-c\over(a-1)(b-1)}
 =1+{|A\cup B|-1\over(a-1)(b-1)}.}                               \tag{3.10}
\]

Consequently, for `gamma>0`, every terminal two-row prefix socket relevant to (0.2) must
satisfy the checkable reciprocal expansion inequality

\[
 \boxed{
 (a-1)(b-1)\ge {d\over\gamma}(|A\cup B|-1).}                      \tag{3.11}
\]

#### Proof

Choose one column from each row and exclude the `c` equal-column pairs.
This gives `ab-c`.  The number containing `e` is `b-1`, the number
containing `f` is `a-1`, and exactly one contains both.  Division gives
the first expression in (3.10).  Subtracting the denominator from its
numerator gives `a+b-c-1=|A\cup B|-1`.  Equation (3.11) is equivalent to
(0.2).  QED.

Equation (3.11) is necessary on an exposed two-row component.  It is not
claimed sufficient for permanent-minor control in an arbitrary larger
component.

## 4. Reciprocal sandwiches in the PBBS candidate graph

### Theorem 4.1 (exact raw four-edge criterion)

Let `S\ne R` be distinct strict lower targets and let `I\ne J` be distinct
interval columns in the unpruned mandatory-core envelope table.  All four
raw candidate edges

\[
 (S,I),(S,J),(R,I),(R,J)                                          \tag{4.1}
\]

exist if and only if

\[
 \boxed{
 F(I)\cup F(J)\subseteq S\cap R,
 \qquad S\cup R\subseteq P(I)\cap P(J).}                          \tag{4.2}
\]

#### Proof

The four lower sandwich inclusions combine to the first inclusion in
(4.2), and the four upper inclusions combine to the second.  Conversely,
(4.2) gives both `F(I),F(J)\subseteq S,R` and
`S,R\subseteq P(I),P(J)`, which are exactly the four copies of (1.2).
QED.

After unit closure or other candidate pruning, (4.2) remains necessary but
is sufficient only together with explicit survival of all four edges.

### Proposition 4.2 (exact isolation condition)

Let `Theta` be an extendable prefix partial matching disjoint from
`S,R,I,J`, and put `H_Theta=H\ominus Theta`.  The four vertices form an
isolated `K_(2,2)` component in `H_Theta` if and only if (4.2) holds in the
residual candidate table and

\[
 \boxed{
 N_{H_\Theta}(S)=N_{H_\Theta}(R)=\{I,J\},\qquad
 N_{H_\Theta}(I)=N_{H_\Theta}(J)=\{S,R\}.}                        \tag{4.3}
\]

In that event Theorem 3.1 applies with the residual edge weights.

#### Proof

The residual neighborhood equalities certify survival of the four internal
edges and say exactly that there is no edge from those vertices to the rest
of the residual graph.  The raw sandwich necessity is Theorem 4.1.  QED.

The sandwich condition alone does not imply isolation.  As an abstract
envelope table, take

\[
 K=\{1\},\quad Q=\{1,2,3\},\quad
 S=\{1,2\},\quad R=\{1,3\},                                      \tag{4.4}
\]

and set `F(I)=F(J)=K`, `P(I)=P(J)=Q`.  This satisfies (4.2) and realizes
the four-edge subgraph.  It does not certify that these `F/P` data arise
from one PBBS chronology and it says nothing about (4.3).  No actual PBBS
reciprocal rectangle is asserted here.

### Corollary 4.3 (dead reciprocal rectangle certificate)

Assume (4.2)--(4.3), and let `D_x^0` be the fixed negative background in
the contracted face.  If there are a middle row `t` and a coordinate
`x in T_t` such that, for

\[
 U=(E_x\cap[t,t+d])\setminus D_x^0,
\]

one has

\[
 x\notin S\cup R,\qquad U\subseteq I\cup J,\qquad
 U\nsubseteq I,\quad U\nsubseteq J,                              \tag{4.5}
\]

then both shores of the isolated rectangle are residual size-two parts of
contracted central-cover conflicts.  After adjoining an inclusion-minimal
subfamily of the deterministic negative background, every target-
saturating matching in that component contains a lifted physical conflict.
Within the fixed background face, compatibility therefore requires deleting
at least one target from the corresponding lifted conflict; this need not
be one of `S,R` if deletion of a forced background target is allowed.

#### Proof

The two residual intervals are both essential by (4.5).  Adjoin a minimal
subfamily of the fixed negative background which completes the cover.  The
exact run normal form gives a lifted conflict containing `(S,I),(R,J)`, and
applies unchanged to `(S,J),(R,I)` because the two residual labels and the
union of their intervals are the same.  The two shores are the only
saturating matchings of the isolated component.  QED.

This is a fail-closed symbolic PBBS obstruction, not an assertion that the
displayed data occur.  Moreover a strong failed-literal closure would
detect this dead rectangle; it is not a hidden post-closure obstruction.

## 5. A deletion-stable master switch bank

We now remove the repeated prefix quantifier from item 1997 under one
explicit fault-tolerance hypothesis.

Fix an integer `h>=0`.  A master switch certificate has a support containing
every graph vertex incident with an edge which the switch changes or
introduces.  For every exceptional ordered pair of full saturating matchings
`(widehat M_11,widehat M_00)` in `H`, choose its master catalogue before a
prefix is specified.

### Theorem 5.1 (fault-tolerant prefix switch supply)

Suppose every exceptional full pair has a master catalogue of at least `Q`
separating switch certificates with the following properties.

1. Within this catalogue, every graph vertex belongs to at most `rho`
   certificate supports.
2. For every common partial matching
   `Theta\subseteq widehat M_11\cap widehat M_00`, every certificate whose
   support avoids `V(Theta)` leaves `Theta` fixed and descends to a
   separating switch in `H\ominus Theta`.
3. Every descended output pair has product weight at least `eta>0` times
   its residual input product weight.
4. In every residual prefix graph, every output pair is the image of at
   most `b` surviving switch incidences, counted with multiplicity.

Then every common prefix with `|Theta|<=h` satisfies

\[
 \boxed{
 \mathfrak B_{H\ominus\Theta}(e,f)
 \le {b\over[Q-2\rho h]_+\eta}
       Z_{10}^{\Theta}Z_{01}^{\Theta},}                            \tag{5.1}
\]

whenever `Q>2\rho h`.  In particular, for `gamma>0` and `h=d-1`,

\[
 \boxed{
 [Q-2\rho(d-1)]\eta\ge {bd\over\gamma}}                         \tag{5.2}
\]

implies the pair factor `1+gamma/d` in every endpoint-deleted prefix.

#### Proof

The prefix `Theta` has `2|Theta|` endpoints.  By property 1, their union
meets the supports of at most `2\rho|Theta|` certificates.  Hence at least
`Q-2\rho h` certificates survive.  Property 2 makes all of them legitimate
residual separating switches.

Double-count weighted input--output switch incidences.  Each exceptional
input sends total output product weight at least
`[Q-2\rho h]\eta` times its input product weight.  Property 4 charges every
output at most `b` times.  This proves (5.1).  Equation (5.2), Theorem 2.1,
and `beta=gamma/d` prove the final assertion.  The common factor
`w(Theta)^2` in the extended input and output products cancels, so the
argument is genuinely prefix-stable.  QED.

For `gamma=0`, the required statement is instead
`mathfrak B=0`; division by `gamma` is not used.  The theorem covers only
endpoint deletion, which is exactly the conditioning operation in the
matching-cylinder chain rule.  If an application performs additional
candidate pruning at each prefix, it must reverify properties 1--4 in that
pruned graph.

For unit weights `eta=1`.  Thus a bank with bounded `rho,b` needs a linear
number of certificates with enough surplus to survive `2rho(d-1)` endpoint
faults.  The `K_(2,2)` obstruction has `Q=0`, while Theorem 3.2 shows that
even a complete two-row socket needs order `d` common columns.

## 6. Flat interval links require erosion returns

Let `P_p` be the maximal erosion states along the source line.  An index
interval `H=[u,v]` is a **flat hull** if every `P_p`, `p in H`, has the same
interior erosion rank and consecutive states are distinct Johnson
neighbors.  It is **return-free** if, for every coordinate `x`,

\[
                         \{p\in H:x\in P_p\}                       \tag{6.1}
\]

is an interval, possibly empty.

### Theorem 6.1 (return-free flat-hull rigidity)

Let `I=[a,b]` and `J=[c,e]` be interval columns contained in one
return-free flat hull.  If a retained target is a candidate on both, then

\[
                         \boxed{I=J.}                              \tag{6.2}
\]

#### Proof

Common candidacy gives

\[
 F(I)\cup F(J)\subseteq S\subseteq P(I)\cap P(J).                 \tag{6.3}
\]

Suppose `a<c`.  Flatness gives a coordinate
`x\in P_a\setminus P_{a+1}`.  This coordinate belongs to
`F_a\subseteq F(I)\subseteq P(J)`, so it occurs at some source position
`q in J`, with `q>=c>a`, although it is absent at `a+1`.  Its support in
the hull is not an interval, a contradiction.  Symmetry excludes `c<a`,
so `a=c`.

If `b<e`, flatness gives
`y\in P_e\setminus P_{e-1}`.  Now
`y\in F_e\subseteq F(J)\subseteq P(I)`, so it occurred at some `p<=b<e`
although it is absent at `e-1`.  This is another return.  Symmetry gives
`b=e`.  QED.

### Corollary 6.2 (actual PBBS return gate)

Every link between distinct interval columns whose convex hull is flat
certifies an erosion-coordinate return in that hull.  Hence every
nontrivial alternating component or external guard bridge must leave a
return-free hull, meet a clipped erosion ramp, or use such a return.

The theorem is deletion-stable because deleting candidate data cannot
create a common candidate.  It is not asserted across a ramp: one of the
endpoint differences used in the proof can be empty there.  Ramp-touching
interval columns must be charged separately, as in the `O(d^2)` endpoint
ledger of item 1997.

This proves that local stable-window abundance is not bridge abundance.
To establish (5.2) in PBBS one must count return-certified reciprocal links
for every exceptional input, bound how many are killed by each prefix
endpoint, control output preimages, and retain an `eta` weight ratio.  None
of those four conclusions follows from all-depth support alone.

## 7. Odd/even Pascal transfer

The proved Pascal facet/union identities transport envelope candidates and
mandatory event ports on unbraided interiors.  They do not, by themselves,
transport the four parameters in Theorem 5.1.

### Proposition 7.1 (protected component-faithful transfer)

Suppose an odd/even lift sends every parent candidate and every certificate
of a parent master bank injectively to one child shore and preserves
incidence and product-weight ratios.  Assume every child input pair under
consideration is a protected common extension

\[
 (\phi(M_{11})\cup N,\ \phi(M_{00})\cup N)
\]

by the same outside matching `N`, every lifted switch support is disjoint
from `V(N)`, and every lifted certificate is consequently a legitimate
child switch fixing all outside edges.  Suppose also that the lift creates
no additional preimages of a lifted switch output.  Then for these protected
inputs the parameters `Q,rho,b,eta` are unchanged.

If the child deadline `d'` satisfies `d'<=d`, every parent inequality

\[
 [Q-2\rho(d-1)]\eta\ge {bd\over\gamma}                            \tag{7.1}
\]

implies its child analogue with `d'`.

#### Proof

The injective protected lift carries the master catalogue and all switch
incidences without changing support load, congestion, or weight ratio.
Since `d'<=d`,

\[
 Q-2\rho(d'-1)\ge Q-2\rho(d-1),
 \qquad bd'/\gamma\le bd/\gamma.                                  \tag{7.2}
\]

Apply Theorem 5.1.  QED.

The proposition deliberately covers only lifted-parent inputs.  The
actual Pascal child also has new-shore candidates, cross-shore alternating
components, and promoted collars.  Those can attach to a parent reciprocal
socket, merge parent components, create new exceptional inputs, and change
switch preimage congestion.  The current Pascal theorems do not prove the
protection hypotheses or supply banks for those new inputs.  Conversely, a
parent isolated rectangle persists only when no new child edge attaches to
its four lifted vertices.  Thus neither obstruction nor expansion transfers
automatically.

## 8. Exact proved boundary

Proved unconditionally:

1. the item-1997 same-component permanent inequality;
2. the minimal weighted `K_(2,2)` obstruction and exact uniform
   `K_(2,n)` and arbitrary two-row socket formulas;
3. the reciprocal PBBS candidate-sandwich and isolation criteria;
4. the fault-tolerant `Q,rho,b,eta` prefix theorem;
5. return-free flat-hull link rigidity; and
6. protected component-faithful Pascal transfer.

Not proved:

1. no actual PBBS unit-closed face is proved here to contain an isolated
   reciprocal rectangle or dead rectangle;
2. no theorem excludes all such small sockets from the actual fully closed
   PBBS graph;
3. no PBBS theorem supplies the master return/guard bank (5.2) for every
   exceptional input;
4. the known Pascal lift does not control new/collar exceptional inputs or
   output congestion; and
5. therefore no unconditional `B(k)+O(k)` conclusion follows.

The exact remaining positive theorem is now checkable: after recursive
unit closure, prove the direct pair bound for every conflict-relevant pair
and prefix.  The two-row inequality (3.11) is a necessary terminal
diagnostic, while a fault-tolerant return/guard bank satisfying (5.2) for
every such pair is sufficient; excluding only small sockets is not enough
because Proposition 3.1a leaves longer alternating cycles.  One must then separately
bound the complete target-capped run/guard pressure from item 1997.  The
component-signature packet route is a valid alternative, but it must bound
its exact target repair pressure rather than component count alone.
