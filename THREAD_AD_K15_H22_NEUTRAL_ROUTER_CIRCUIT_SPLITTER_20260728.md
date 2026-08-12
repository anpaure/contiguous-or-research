# Lane AD: Hall-22 neutral router and local DM-circuit splitter

Date: 2026-07-28

Status: exact Hall \(23\to23\to22\) construction, exact
DM-circuit ear theorem, exact critical-shore common-controller regeneration,
and a conditional two-colour routing theorem for every positive H22 circuit.
Transitivity of the physical decorated router and creation at the seven
zero-degree components are not proved.

## 0. Main result

The authoritative route is

\[
H23
\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23_{\rm port}
\xrightarrow{\operatorname{FR}(740,4051,6137)}H22.
\tag{0.1}
\]

Its matching sizes and deficiencies are

\[
\begin{array}{c|ccc}
&H23&H23_{\rm port}&H22\\ \hline
\nu&16360&16360&16361\\
\delta&23&23&22.
\end{array}
\tag{0.2}
\]

Every state lists all \(6435\) middle owners once, is a Johnson path, is
depth-three resident, has every upper support through depth seven, and has
four immediate-lower holes.  The same seven zero-degree targets remain:

\[
2575,5801,13616,13620,17738,21641,29776.
\tag{0.3}
\]

The neutral first braid rotates a Boolean packet in the \(161/160\) DM
component rooted at 24610.  The improving second braid makes no cell-shore
change in that component.  Remotely, it replaces the sole shore

\[
\{4877,4909\}
\tag{0.4}
\]

of a \(2/1\) DM circuit by the singleton shores
\(\{4877\}\) and \(\{4909\}\).  Thus the exact architecture is

\[
\boxed{\text{neutral global legality router}
\quad+\quad\text{local deficient-circuit splitter}.}
\tag{0.5}
\]

Both final cells have singleton restricted shores and are native traces of
the same maximal erosion word.  They are not singleton letters: their depths
are one and two.  Together with all 983 native pins of the remaining H22 DM
shore they give 985 simultaneous literal pins on the former 1007-target H23
shore.  Hence its projected and native common-pin defects are both exactly
22.  This is a shore-local statement, not a common-word lift of an arbitrary
global maximum matching.

There is also an exact cumulative certificate across the preceding H24-to-H23
discharge.  One physical compiler under the final H22 controller realizes
1146 distinct pins on the old 1168-target H24 shore, missing exactly the 22
current roots.  It uses the 983 active native pins, all 161 pins of the
discharged 20516 component, and the two pins above; only position 6261 is
repinned, from 20517 to 20516.  Thus common-controller regeneration survives
both discharges, but remains critical-shore rather than global.

## 1. DM component theorem

Let \(G=(L,R;E)\) be bipartite and \(M\) a maximum matching.  Let
\(D_L\cup D_R\) be the alternating-reachable deficient shore and decompose
\(G[D_L,D_R]\) into connected components \((A_j,B_j)\).

### Theorem 1.1 (component additivity)

The matching \(M\) saturates every \(B_j\), and

\[
\operatorname{def}(G)
=|D_L|-|D_R|
=\sum_j\bigl(|A_j|-|B_j|\bigr).
\tag{1.1}
\]

The summand is the number of exposed left roots in that component.

#### Proof

Every reachable right vertex is matched, since otherwise an alternating
path from an unmatched left root would augment \(M\).  Its matched target is
in the same component.  Thus \(M\) saturates \(B_j\), leaving exactly
\(|A_j|-|B_j|\) exposed targets.  Summation gives (1.1).  \(\square\)

### Theorem 1.2 (gap-one components are transversal circuits)

If \(|A_j|=|B_j|+1\), then for every \(x\in A_j\),

\[
A_j\setminus\{x\}
\tag{1.2}
\]

matches bijectively to \(B_j\).

#### Proof

The component has one exposed root \(u\).  An alternating path from \(u\) to
\(x\) exists by canonical reachability.  Flipping it exposes \(x\) instead
of \(u\), so all other targets match \(B_j\).  \(\square\)

### Corollary 1.3 (circuit ear)

If a final graph retains a matching of \(A_j\setminus\{x\}\) and supplies a
new right-disjoint cell adjacent to \(x\), then it saturates \(A_j\).

The local statement lowers global deficiency only when the component
matching is right-disjoint from a retained exterior matching.  Equivalently,
if the new graph has a matching of size \(\nu(G)+1\) and retains a shore of
gap \(\operatorname{def}(G)-1\), its deficiency is exactly one smaller.

## 2. The H23 circuit and its neutral router

The H23 canonical shore is \(1007/984\).  It has 23 connected components,
all gap one.  Its 984 right cells have pairwise distinct native traces,
leaving exactly these component roots unmatched:

\[
\begin{gathered}
449,960,1103,1920,2420,2575,2676,4213,4877,5801,7504,8217,8218,\\
9524,13616,13620,17683,17738,18970,19568,21641,24610,29776.
\end{gathered}
\tag{2.1}
\]

The discharged component has targets \(\{4877,4909\}\) and one cell.  In
both H23 and its portal state this is cell 13614, depth two at start 739,
with

\[
(P_{739},P_{740},P_{741})=(809,301,4393),
\tag{2.2}
\]

native trace 4909, mandatory mask 4876, and restricted shore
\(\{4877,4909\}\).

The neutral router

\[
\rho=\operatorname{RF}(3799,4497,6039)
\tag{2.3}
\]

leaves this remote circuit unchanged.  In the 24610 component it replaces

\[
\begin{aligned}
&\{24610,24611,24674,24675,28707,28770,28771\},\\
&\{24614,24615,24678,24679\}
\end{aligned}
\tag{2.4}
\]

by

\[
\begin{aligned}
&\{24610,24611,24614,24615,24674,24675,24678,24679\},\\
&\{28707,28770,28771\}.
\end{aligned}
\tag{2.5}
\]

This \(7+4\to8+3\) packet rotation leaves that component at rank 160 and
leaves global Hall deficiency 23.  It has no lower- or upper-support loss
or gain and remains resident.  Its role is chronological: it routes legal
endpoints for the later remote split.

## 3. The local splitter and exact H22 audit

The splitter is

\[
\sigma=\operatorname{FR}(740,4051,6137).
\tag{3.1}
\]

It changes (0.4) into two singleton shores with exact cells

\[
\begin{array}{c|ccccc}
\text{target}&\text{cell}&\text{depth/start}&\text{allowed values}
 &\text{mandatory}&\text{native trace}\\ \hline
4877&7178&1/740&(781,4365)&4612&4877\\
4909&13614&2/739&(809,781,4365)&4652&4909.
\end{array}
\tag{3.2}
\]

The splitter makes no restricted-signature change in the 24610 component.
Its full-graph common-core rank is 16343 and its contracted boundary rank is

\[
17\longrightarrow18.
\tag{3.3}
\]

The final canonical shore is \(1005/983\).  It equals the portal shore with
exactly 4877 and 4909 removed and no target added.  The cross-gap matrix
(rows are graphs, columns are their canonical shores) is

\[
\begin{pmatrix}
23&23&22\\
23&23&22\\
22&22&22
\end{pmatrix}.
\tag{3.4}
\]

The recomputed full matching has size 16361, giving deficiency at most 22,
while the final shore in (3.4) has gap 22.  Hence the deficiency is exactly
22.  This numerical certificate does not by itself transport one prescribed
exterior matching or one prescribed global pin family.

The lower hole vectors are

\[
H23,H23_{\rm port}:(4,19,6,1,0,0,0),
\qquad
H22:(4,18,6,1,0,0,0).
\tag{3.5}
\]

The splitter gains lower depth-two target 4877, loses no lower support, and
leaves every upper support complete.

The direct compound cuts H23 at

\[
740,3799,4497,5788,6040,6138.
\tag{3.6}
\]

For consecutive blocks \(A,\ldots,G\), its final order is

\[
A,\overleftarrow D,C,F,E,\overleftarrow B,G.
\tag{3.7}
\]

The six final seam positions are
\(740,2031,2729,2827,3079,6138\), all Johnson edges.  Directly comparing
H23 with H22 gives a 19252-cell common full-signature core of rank 16333,
59-cell banks, and contracted ranks \(27\to28\).

## 4. Literal critical-shore compatibility

The H22 canonical shore has 1005 targets and 983 cells.  Its native traces
are distinct and simultaneously realized by its maximal erosion word.  Their
rank census is

\[
54\text{ of rank }5,\qquad259\text{ of rank }6,\qquad670\text{ of rank }7.
\tag{4.1}
\]

The splitter cells 7178 and 13614 lie outside the H22 DM-right shore, and
their targets lie outside the H22 DM-left shore.  Therefore they are
right- and target-disjoint from all 983 native H22 pins.  All 985 pins are
native in one word, so

\[
1007-985=22
\tag{4.2}
\]

is also the exact common-pin defect on the former H23 shore.

This does not lift an arbitrary global maximum matching or prove that the
length-6438 word covers every lower target.

### Theorem 4.1 (cumulative H24-shore regeneration)

Let \(S_{24}\) be the 1168-target canonical H24 DM shore, and let \(P\) be
the final H22 maximal controller.  There is one nonzero physical word
\(A_p\subseteq P_p\) realizing a target- and cell-injective family of 1146
pins on \(S_{24}\).  Its unresolved targets are exactly the 22 H22 roots, so
its common-controller defect on \(S_{24}\) is exactly 22.

#### Proof

Use the 983 native pins of the active H22 shore, the 161 target-distinct pins
of the previously discharged component rooted at 20516, and the two native
pins in (3.2).  The three target and cell families are pairwise disjoint.
Every selected pin is native under \(P\) except the root pin at the unused
depth-zero cell 6261.  There

\[
P_{6261}=20517=20516\cup\{0\}
\tag{4.3}
\]

in zero-based bit notation.  Set \(A_{6261}=20516\) and leave every other
letter equal to \(P\).  Coordinate 0 survives in every central four-window
through 6261.  Among the selected pin intervals, the only other interval
through 6261 is the depth-one cell starting at 6260, and its union remains
22565.  Hence Theorem 5.2 applies: every central owner and every selected pin
is unchanged except that the unused child cell now realizes root 20516.
All letters remain nonzero.  The count is

\[
983+161+2=1146.
\tag{4.4}
\]

The exact H22 root list has size 22 and is the complement of these targets
inside \(S_{24}\), proving exact defect 22.  \(\square\)

The single repin in (4.3) means \(A\ne P\); the physical compiler need not
itself be the maximal erosion controller.

## 5. Final-controller ear theorems

Fix one final depth-\(d\) resident controller \(P=(P_p)\), and write

\[
\tau_P(I)=\bigcup_{p\in I}P_p
\tag{5.1}
\]

for the native trace of a nonempty interval.  Nativeness in this section is
always relative to this one final controller.  A pin native at an
intermediate router state need not remain native after the splitter.

### Theorem 5.1 (simultaneous native ears)

Let the relevant target universe be \(L\), and let
\(D_j=(A_j,B_j)\), \(1\le j\le t\), be pairwise target- and right-disjoint
gap-one matching summands.  Choose \(x_j\in A_j\) such that
\(A_j\setminus\{x_j\}\) matches to \(B_j\).  Suppose a target- and
cell-injective pin family \(\mathcal M\) has size \(|L|-d_0\), where \(d_0\)
is the original matching deficiency, and:

1. is native under \(P\);
2. contains the chosen matchings of all
   \(A_j\setminus\{x_j\}\) and a cell-disjoint exterior matching; and
3. does not use any of the pairwise distinct targets \(x_j\); and
4. leaves distinct intervals \(J_j\) unused, with
   \(\tau_P(J_j)=x_j\).

Then

\[
\mathcal M\cup\{(x_j,J_j):1\le j\le t\}
\tag{5.2}
\]

is a target- and cell-injective matching realized simultaneously by the
single literal word \(P\).  It has \(t\) more edges than \(\mathcal M\).
If a retained Hall shore has gap \(d_0-t\), where \(d_0\) was the original
global deficiency, then the new global deficiency is exactly \(d_0-t\).

#### Proof

Theorem 1.2 supplies each component matching after exposing \(x_j\).
The exterior, component, and new ear cells are pairwise disjoint by
hypothesis, as are their targets.  Every pin in (5.2) is an exact interval
trace of the same word \(P\), so interval crossings create no compatibility
condition.  This gives a matching larger by \(t\).  The retained shore gives
the reverse deficiency inequality and hence equality.  \(\square\)

For the actual H22 controller,

\[
J_{4877}=[740,741],\qquad J_{4909}=[739,741],
\tag{5.3}
\]

and (3.2) gives their native traces.  Thus the construction uses nested
native pins and no exceptional letter shrink: one pins
\(A_j\setminus\{x_j\}\), and the other is the new ear in Theorem 5.1.
Concretely, take the 983 H22-shore pins together with the retained 4909 pin
as the 984-edge base and use \((4877,[740,741])\) as the new ear.

### Theorem 5.2 (one exceptional root-child shrink)

Let \(\mathcal M=\{(S_c,I_c)\}\) be the full target- and cell-injective
native pin family that is to be retained for \(P\).  Let \(R\ne\varnothing\),
\(Y=R\cup\{a\}\), where \(Y\) is already used by \(\mathcal M\) and \(R\)
is not.  Suppose an unused singleton cell \(c_*=\{s\}\) satisfies \(P_s=Y\).
Define

\[
A_s=R,\qquad A_p=P_p\quad(p\ne s).
\tag{5.4}
\]

Then \(A\) realizes the same central row, every pin of \(\mathcal M\), and
the new pin \((R,c_*)\) if and only if:

1. every central window through \(s\) contains \(a\) at another position;
2. every retained pin interval through \(s\) contains \(a\) at another
   position.

The first clause is equivalently \(M_s\subseteq R\), where

\[
M_s=\{x\in P_s:\text{some central window through }s
\text{ contains }x\text{ only at }s\}.
\tag{5.5}
\]

#### Proof

Only coordinate \(a\) is deleted, and only at position \(s\).  A central or
pinned interval changes exactly when it contains \(s\) and \(s\) was its
unique occurrence of \(a\).  The two clauses exclude precisely those cases;
all other coordinates are unchanged.  Nonzeroness of the new letter follows
from \(R\ne\varnothing\).  \(\square\)

Theorem 5.2 gives a common word only for the explicitly retained complete
pin family.  It does not make arbitrary exterior graph-matching edges
compatible, and unselected lower-support witnesses need not survive.

### Theorem 5.3 (exact final-controller common-\(Q\) criterion)

Let \(P_p\) be the maximal allowed mask at each position for prescribed
central targets \(T_i\), so \(P_p\subseteq T_i\) whenever position \(p\)
lies in the central window for \(T_i\).  For selected pins
\((I_c,S_c)\), put

\[
K_p=P_p\cap\bigcap_{c:p\in I_c}S_c,
\tag{5.6}
\]

where the empty intersection is the full coordinate set.  There exists one
nonempty word \(A_p\subseteq P_p\) realizing every central target and every
selected pin if and only if:

1. \(K_p\ne\varnothing\) for every position \(p\);
2. for every \(x\in T_i\), some position \(p\) in its central window has
   \(x\in K_p\);
3. for every \(x\in S_c\), some \(p\in I_c\) has \(x\in K_p\).

#### Proof

Any feasible \(A_p\) is contained in every selected pin target whose
interval contains \(p\), hence \(A_p\subseteq K_p\).  Nonemptiness and every
required positive coordinate hit give the three necessary conditions.
Conversely, choose \(A_p=K_p\).  The definition of \(P_p\) prevents excess
coordinates in central windows, and (5.6) prevents excess coordinates in
pin intervals.  Conditions 2 and 3 give all required positive hits, while
condition 1 keeps every letter nonempty.  \(\square\)

If every selected pin is native under the same \(P\), then
\(P_p\subseteq S_c=\tau_P(I_c)\) for every \(p\in I_c\); hence \(K_p=P_p\)
and Theorem 5.3 is automatic.  This is exactly why Theorem 5.1 composes
crossing native ears.  Separate feasibility of non-native pins does not
imply their simultaneous feasibility.

## 6. Neutral routing: weak groupoid and pin-decorated category

A three-cut permutation is invertible, but Johnson legality, residence,
shadow safety, Hall neutrality, and common-word compatibility depend on its
source state.  The correct object is a partial-action groupoid, not an
unconditional group on one carrier.

Let \(\mathcal I_0\) consist of the middle deck, Johnson legality, residence,
the protected lower and upper supports, exact Hall deficiency, and the
existence of the required exterior matching capacity or residual-shore
certificate; it does not name fixed matching edges.  The **weak carrier groupoid**
\(\mathfrak G_d^{\rm wk}(\mathcal I_0)\) has deficiency-\(d\) decorated
carriers as objects.  Its arrows are reversible braid macros whose endpoints
preserve \(\mathcal I_0\); every intermediate carrier must remain a legal
Johnson/resident source for the next braid, but a macro may make and restore
temporary Hall or support excursions.

The **pin-decorated transition category** \(\mathfrak C_d^{\rm pin}\)
further includes one explicit target/cell injection and one word realizing
all its pins.  An arrow here must certify the final interval of every
retained pin, or pass the full common-\(Q\) coordinate ledger.  It is a
groupoid only when the reverse macro also certifies inverse pin transport.
Existence of unrelated native matchings at the two endpoints is not
transport of a fixed pin family.

For discharged data \(D\) and a remaining component \(C\), let
\(\Sigma^{\rm wk}_{D,C}\) be the locus of carriers admitting one safe
component-specific ear while retaining an exterior matching.  Let
\(\Sigma^{\rm pin}_{D,C}\) impose in addition final-controller compatibility
for the complete selected matching.  A \(1/0\) component uses a first-cell
ear; a \(2/1\) component may use the splitter of Section 3; larger components
may require a different ear or diamond bank.

### Theorem 6.1 (exact routing-to-descent criterion)

In the weak groupoid, a component \(C\) is dischargeable by neutral routers
followed by one splitter if and only if

\[
\operatorname{Orb}_{\mathfrak G_D^{\rm wk}}(X)
\cap\Sigma^{\rm wk}_{D,C}\ne\varnothing.
\tag{6.1}
\]

In the pin-decorated category the exact condition is instead

\[
\operatorname{Reach}_{\mathfrak C_D^{\rm pin}}(X)
\cap\Sigma^{\rm pin}_{D,C}\ne\varnothing.
\tag{6.2}
\]

If the relevant condition holds hereditarily after every earlier discharge,
with a residual
shore certifying every claimed exact deficiency, the construction iterates.
In the pin-decorated version the final object at every stage has one literal
word for its complete selected matching.

#### Proof

An orbit or reachable-state hit gives a neutral macro to a legal splitter
source; compose it with the splitter and apply Corollary 1.3 or Theorem 5.1.
Conversely, any router-plus-one-splitter construction has, immediately before
its splitter, a reachable state in the stated locus; reversibility upgrades
reachability to a weak-groupoid orbit.  Hereditary iteration is induction on
the discharged set \(D\).  \(\square\)

### Theorem 6.2 (closed packet-chart routing)

Let \(H=(V,E)\) be a packet-host graph.  Assume a **closed decorated chart**:
for every reachable packet arrangement and every edge \(uv\in E\), there is
an exact reversible Hall-neutral macro which transposes the complete packets
at \(u,v\), changes no other packet, and transports every endpoint,
residence, shadow, compiler, matching, and final-pin decoration.  Then the
subgroup generated by these certified edge routers is

\[
G_H:=\langle g_{uv}:uv\in E\rangle
=\prod_{K\in\pi_0(H)}\operatorname{Sym}(K).
\tag{6.3}
\]

In particular, under \(G_H\), one packet reaches precisely the hosts in its
connected component; routing by these generators to an arbitrary fixed port
is transitive if and only if the relevant host component is connected.
Other legal neutral macros, if they exist, may enlarge \(G_H\) and connect
different components of \(H\).

#### Proof

Every generator is an edge transposition and therefore preserves connected
components.  Conversely, the edge transpositions of a spanning tree
generate the full symmetric group on its vertices: move either endpoint of
an arbitrary transposition along the unique tree path, perform the adjacent
transposition, and undo the preliminary moves.  Different connected
components have disjoint supports, giving the direct product.  Closure is
what makes every word in these generators a legal decorated macro.  \(\square\)

Thus a connected closed chart plus a portable splitter frame implies the
weak orbit hypothesis (6.1) and, because every decorated edge transport is
reversible, the pin reachability hypothesis (6.2).  The current construction
certifies only one router edge, not a closed chart.  Its inverse
\(\operatorname{FR}(3799,5342,6039)\) is certified only on the
H23-portal pair; it is not known to remain legal after the splitter.

Every splitter frame must record the ordered seam endpoints and orientations,
the full depth-three collars, every protected crossing trace through
\(q=7\), complete compiler neighbourhoods and mandatory masks, exterior
matching occupancy, and every final-controller pin trace.  Transitivity on
cut positions or endpoint pairs alone is insufficient.

### Theorem 6.3 (fixed-endpoint turn-colour holonomy)

Colour a Johnson edge \(UV\) by the two-coordinate set
\(\chi(UV)=U\triangle V\).  If Johnson paths \(T,T'\) have the same ordered
endpoints and

\[
\Delta_\chi(e)=\#\{\text{new edges of colour }e\}
-\#\{\text{old edges of colour }e\},
\tag{6.4}
\]

then for every coordinate \(j\),

\[
\sum_{e\ni j}\Delta_\chi(e)\equiv0\pmod2.
\tag{6.5}
\]

For a signed segment reassembly all internal colours cancel, including in
reversed blocks, so its seam current is Eulerian modulo two.

#### Proof

Along a Johnson path, membership of coordinate \(j\) toggles exactly on the
edges whose colour contains \(j\).  The parity of their number is therefore
\(\mathbf1_{j\in T_0\triangle T_{W-1}}\).  The two paths have the same
ordered endpoints, proving (6.5).  Reversal preserves each internal
unordered colour, proving seam localization.  \(\square\)

The certified neutral router has zero turn-colour current.  For the splitter,
after cancelling its common \(\{10,12\}\) colour, the current is

\[
+\{2,6\}+\{6,15\}-\{2,14\}-\{14,15\},
\tag{6.6}
\]

the alternating cycle \(2-6-15-14-2\).  Thus the local axis-6 polarization
is closed by a remote axis-6 return port; it cannot be installed as an
isolated fixed-endpoint one-port move.

The turn colours in (6.6)--(6.7) use coordinates \(1,\ldots,15\).  The
decimal-mask stabilizer calculation in Section 7 uses zero-based bit
positions \(0,\ldots,14\).

For the five surviving \(2/1\) circuits, the audited root/optional-axis list
is

\[
\begin{array}{c|ccccc}
\text{root}&2420&2676&9524&17683&19568\\ \hline
\text{axis}&10&14&7&13&14.
\end{array}
\tag{6.7}
\]

Only axis 14 repeats.  Hence those two circuits are the sole direct
same-axis two-local-port candidate; axes 10, 7, and 13 each require a remote
same-axis return or coupling to a larger component.  This is a necessary
holonomy condition, not a braid, residence, Hall, or common-\(Q\)
certificate.

### Theorem 6.4 (exact two-colour H22 root-port atlas)

The H22 canonical shore is the disjoint union of 22 excess-one transversal
circuits.  Every circuit has a target-distinct native atlas equal to the
circuit minus one root.  Exactly 15 circuits are nonloops, and each has a
component-restricted two-shore containing its root.  Their root ports have
only two colours:

\[
\begin{array}{c|c|c|l}
\text{root rank}&\text{cell depth}&\text{count}&\text{roots}\\ \hline
4&0&6&449,960,1920,8217,8218,24610\\
6&2&9&1103,2420,2676,4213,7504,9524,17683,18970,19568.
\end{array}
\tag{6.8}
\]

The seven loop circuits are

\[
2575,5801,13616,13620,17738,21641,29776.
\tag{6.9}
\]

#### Proof

The canonical alternating decomposition has 22 closed connected components,
each with one more target than cell.  Theorem 1.2 makes each target shore a
transversal circuit.  Taking the union of the final-controller letters in
every right cell gives 983 distinct native traces; componentwise these are
exactly every target except the displayed root.  The root-incidence audit
then gives the two-shore depths and lists in (6.8), while the seven roots in
(6.9) have no incident cell.  The counts are
\(6+9+7=22\).  \(\square\)

### Corollary 6.5 (regenerative two-colour reduction)

Suppose that after every prior nonloop discharge:

1. the unused ports of each colour in (6.8) form a connected closed
   decorated safe-swap chart;
2. that colour has a clean splitter station in the same reachable decorated
   class; and
3. the splitter regenerates the two-colour atlas, the exterior matching, and
   the complete common-controller pin face on the descendant.

Then all 15 nonloop circuits can be discharged in any prescribed order,
preserving the deck, residence, protected supports, and one physical pin
word.  Hall deficiency falls from 22 to the seven-loop floor 7.

#### Proof

For the chosen root, Theorem 6.2 routes its same-colour packet to the clean
station.  The splitter and the applicable final-controller criterion from
Section 5 discharge that circuit.  Hypothesis 3 returns a descendant
satisfying the same hypotheses.  Induction discharges all 15 nonloops.
\(\square\)

The previously discharged 20516 component is a rank-four prototype and the
4877 component is a rank-six prototype, but they were certified in earlier
orbits.  Neither supplies the required same-H22-class regenerative seed or
safe-swap connectivity.

### Proposition 6.6 (zero-incidence obstruction)

Let \(d_S\) be the number of physical compiler cells incident with target
\(S\).  Every router subgroupoid preserving the complete vector
\((d_S)_S\) preserves its zero set.  Consequently it cannot route an existing
positive root-edge splitter to any loop in (6.9).

#### Proof

The vector is invariant under every generator and hence every composition.
A root-edge splitter at \(S\) requires \(d_S>0\), whereas each target in
(6.9) starts with \(d_S=0\).  \(\square\)

Thus the literal claim that one occurrence-neutral braid group routes a
splitter to every remaining circuit is false.  A broader Hall-neutral macro
may route to a creator-ready context, but the creator must have positive
incidence derivative at that zero target.  The exact
\((22,7)\to(23,6)\to(22,6)\) creator/compensator macro in Section 7 is the
first example.

## 7. Sharp remaining boundary

Construction (0.1) proves one genuinely cross-component orbit hit in the
weak carrier groupoid: a neutral move supported in the 24610 component
routes a splitter for the remote 4877 circuit.  Separately, the final H22
controller has the shore-local 985-pin certificate of Section 4.  No audit
transports an arbitrary fixed exterior pin matching through the two moves,
so (0.1) is not yet a certified transition in the global pin-decorated
category.  It does not prove weak or strong transitivity to all 22 remaining
components.

Three obstructions are already exact.

1. Equal component sizes and rank profiles do not imply coordinate
   conjugacy.  The discharged \(161/160\) component rooted at 20516 had full
   target union; the remaining same-profile roots 960, 8217, and 24610 each
   omit a coordinate.  Bare relabeling cannot transport that whole gadget.
   Even within the \(2/1\) class, fix the discharged flag

   \[
   R_0=\{0,2,3,8,9,12\}\subset R_0\cup\{5\}.
   \tag{7.1}
   \]

   The stabilizer of this flag has four orbits on the five surviving flags,
   distinguished by
   \((|R\cap R_0|,\mathbf1_{5\in R},\text{class of the added bit})\):

   \[
   \begin{array}{c|c}
   2420&(2,1,R_0)\\
   2676,9524&(2,1,R_0^{\rm c}\setminus\{5\})\\
   17683&(2,0,R_0)\\
   19568&(0,1,R_0^{\rm c}\setminus\{5\}).
   \end{array}
   \tag{7.2}
   \]

   Coordinate symmetry can conjugate the entire carrier and route to
   discharge any one chosen \(2/1\) flag.  This is not routing inside the
   fixed carrier, and it is not hereditary after that flag is fixed.

   Indeed, the stabilizer of (7.1) is
   \(\operatorname{Sym}(R_0)\times\operatorname{Sym}(\{5\})
   \times\operatorname{Sym}([15]\setminus(R_0\cup\{5\}))\).  It preserves
   the displayed triple.  Conversely, within a fixed triple it can send the
   root coordinates and then the added coordinate to those of any other
   flag, so the triple is a complete orbit invariant.  Direct substitution
   of the five flags gives (7.2).
2. A local rank gain can steal an exterior cell, so the exterior matching
   clause cannot be dropped.
3. Seven remaining components are isolated zero-degree targets.  They need a
   first candidate cell rather than a split of an existing shore.  The move
   \(\operatorname{FF}(882,2606,3222)\) opens target 2575 but temporarily
   changes \((22,7)\) to \((23,6)\) and loses lower supports 8905, 713, and
   8777.  The second move \(\operatorname{RF}(1500,4943,6184)\) restores
   Hall 22 and all endpoint support sets while retaining six zeros.  Thus
   there is an exact net-neutral weak macro

   \[
   (22,7)\longrightarrow(23,6)\longrightarrow(22,6).
   \tag{7.3}
   \]

   Its final critical shore has 984 simultaneous native pins and defect 22,
   but that native atlas still omits 2575.  There is a separate exact
   common-controller rebasing which repins the depth-two cell at start 4467
   from native target 2607 to 2575.  It keeps 984 simultaneous pins but
   displaces 2607, so Hall remains 22.  This is useful reachability and a
   shore-local common-word certificate, not Hall descent or transport of an
   arbitrary exterior pin matching.

Literal repetition of only the present \(2/1\) polarization can discharge
the five surviving \(2/1\) components and reaches at best Hall 17.  The
stronger two-colour root-port atlas shows that a regenerative safe-swap
theorem would cover all 15 nonloops and reach Hall 7.  The seven loops still
need incidence-creating, compensated macros.

The exact next theorem is:

> Build hereditary connected safe-swap charts for both colours in (6.8), put
> one regenerative splitter station in each reachable decorated class, and
> transport the exterior common-controller face.  Separately, build
> rank-six and rank-seven zero creators with compensating Hall and shadow
> repair, or prove a stronger invariant excluding one creator orbit.

## 8. Artifacts and reproduction

Canonical SHA-256 values:

    scratch/k15_segment_braid_hall23.json
    8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d

    scratch/k15_segment_braid_hall23_portal.json
    9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6

    scratch/k15_segment_braid_hall22.json
    c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798

    scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json
    e0d591d6c0a7b9715bf4f6fc2007402a7e53215051390e50c01b3be3142070f6

Independent structural verifier:

    scratch/audit_k15_h22_router_splitter_structure.py
    ec0d79eacafa5cf06f906af28dea4e9d4ab7413a7b7e4a1eef77a0dbacaeb6f9

Native H22 certificate:

    scratch/k15_hall22_native_dm_pins_certificate.json
    3fecf4f57b6a253c00f8d97fd9bf83413ff214284c0565c9038d4ce5911823bc

Net-neutral six-zero endpoint:

    scratch/k15_segment_braid_hall23_zero6_from22.json
    9cfc942a60de988545cf0e19c38b57ed50879df92d5f56d3ad2be9862e818bfb

    scratch/k15_segment_braid_hall22_zero6.json
    bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778

Reproduction:

    python3 scratch/audit_k15_segment_braid_descent.py \
      --base scratch/k15_segment_braid_hall23.json \
      --step scratch/k15_segment_braid_hall23_portal.json \
      --step scratch/k15_segment_braid_hall22.json

    python3 scratch/audit_k15_h22_router_splitter_structure.py

    python3 scratch/audit_k15_h25_native_dm_pins.py \
      scratch/k15_segment_braid_hall22.json

    python3 scratch/audit_k15_segment_braid_descent.py \
      --base scratch/k15_segment_braid_hall22.json \
      --step scratch/k15_segment_braid_hall23_zero6_from22.json \
      --step scratch/k15_segment_braid_hall22_zero6.json

    python3 scratch/audit_k15_h25_native_dm_pins.py \
      scratch/k15_segment_braid_hall22_zero6.json

The H22 carrier is an exact finite certificate.  The all-circuit
orbit-transitivity statement remains explicitly conditional.

## 9. Independent proof-audit verdict

The algebraic and literal steps were audited independently after the exact
carrier reconstruction.  The final verdict is:

1. Theorems 1.1, 1.2, 5.2, and 5.3 pass as stated.
2. Theorem 5.1 is valid with its explicit unused-target and unused-cell
   hypotheses.  Omitting either hypothesis makes the claimed \(+t\) matching
   gain false.
3. Theorem 6.1 is an exact reachability criterion, not a proof that every
   locus is reached.  Pin transport is directed unless its inverse is also
   certified.
4. Theorem 6.2 identifies only the subgroup generated by the certified edge
   transpositions.  Other neutral macros may enlarge that group.
5. The H22 common-\(Q\) conclusion is exact for the 1007-target active shore:
   the final word realizes 985 target- and cell-distinct native pins, and the
   same shore has only 985 neighbours.  No global exterior matching is
   thereby literalized.

Thus the decisive finite descent and shore-local literalization pass; the
unproved statement is precisely hereditary decorated-chart reachability for
the residual components.
