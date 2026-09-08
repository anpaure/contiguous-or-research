# Thread D: K16 AAAB collar colour--order flow theorem

**Date:** 2026-07-30  
**Scope:** source-independent one-A-block/one-B-block K16 quotient catalogue;
finite exact enumeration and integral network flow only.  No SAT result,
source carrier, edit radius, or timed branch inference is used.

## 1. Statement

Fix one of

\[
  \operatorname{AAAB}_{380},\quad \operatorname{AAAB}_{384},\quad
  \operatorname{AAAB}_{395},\quad \operatorname{AAAB}_{406}.
\]

Let a selected terminal fragment be

\[
 A_0\xrightarrow e A_1\xrightarrow f A_2
       \xrightarrow s B_0,
\]

where \(p_{ef}=x_e\wedge x_f\) is one of the 80 exact subgroup-q2
prefix variables and \(s\) is the selected A-to-B seam.  Let
\(g:B_0\to B_1\) be the first B-to-B option.  Write \(c(a)\) for the
tight lower-q1 colour carried by an option \(a\).

### Theorem 1 (five-state colour collar)

For each of the 640 choices of \((e,f,s)\):

1. the 35 residence-safe choices for \(g\) split into five sets of seven,
   according to the shifted q3 label of
   \(A_1\cap A_2\cap B_0\cap B_1\);
2. every seven-set has one fixed colour \(c(g)\);
3. the five fixed colours are pairwise distinct and none equals \(c(s)\).

Thus the shifted-q3 class, the first-B tight colour, its target, and its
newest history value are one coupled option-level object.  The five q3
labels are

\[
\begin{array}{c|c}
380,395&587,601,713,1609,2341\\
384,406&589,617,841,1171,2633.
\end{array}
\]

### Theorem 2 (one-more-edge collar)

After fixing \((e,f,s,g)\), update the three-entry insertion history into
the canonical frame of \(B_1\).  Let \({\cal A}_{efsg}\) be the B-to-B
options \(h:B_1\to B_2\) which

* do not delete any of those three history coordinates, and
* do not return to the already used quotient vertex \(B_0\).

Across each parent AAAB branch there are 22,400 such fixed collars, and

\[
 |{\cal A}_{efsg}|=
 \begin{cases}
 34&\text{for 200 collars},\\
 35&\text{for 22,200 collars}.
 \end{cases}
\tag{1.1}
\]

Every one of the 783,800 legal extensions satisfies

\[
 c(h)\notin\{c(s),c(g)\}.
\tag{1.2}
\]

In particular, the first two B steps do not spend the unique repeat token
of the tight lower-q1 palette.

The exact common propagation row is

\[
 \boxed{
 \neg p_{ef}\ \vee\ \neg x_s\ \vee\ \neg x_g\ \vee
       \bigvee_{h\in{\cal A}_{efsg}}x_h .}
\tag{1.3}
\]

There are 200 rows of length 37 and 22,200 rows of length 38 per parent
branch.  These rows are valid simultaneously for all five shifted-q3
classes.  They are already entailed by outgoing degree, insertion history,
and binary rail order/incoming degree, so (1.3) is a propagation
strengthening, not a branch-closing theorem.

The executable now installs this family in
`scratch/solve_even_two_rail_joint_history_kissat_20260730.py`.  To avoid
depending on the private numbering of the exact prefix variable, it expands
\(\neg p_{ef}\) as \(\neg x_e\vee\neg x_f\).  Thus the emitted CNF rows
have lengths 38 and 39, while remaining logically identical to (1.3) under
the already installed equivalence
\(p_{ef}\leftrightarrow(x_e\wedge x_f)\).  The production ledger records
both logical and expanded length histograms.

### Theorem 3 (exact guarded assignment-capacity inequality)

Fix \((e,f,s,g)\).  Let

\[
 S=V_B\setminus\{B_0\},\qquad
 T=(V_B\setminus\{B_0,B_1\})\cup\{\star_{BA}\}.
\]

Both sets have 428 elements.  Form the allowed directed option multigraph
\(G_{efsg}\) from \(S\) to \(T\):

* at source \(B_1\), retain precisely the history-safe B-to-B options not
  entering \(B_0\) (the loop at \(B_1\) is absent from the catalogue);
* at every other source, retain B-to-B options not entering
  \(B_0,B_1\), and collapse every B-to-A option to the capacity-one target
  \(\star_{BA}\).

Every option retains its exact lower colour.  The two already covered
colours \(c(s),c(g)\) are distinct, so the uncovered set

\[
 C_0={\cal C}_{q1}\setminus\{c(s),c(g)\}
\]

has size 427.  For every \(C\subseteq C_0\), define

\[
 \mu_{efsg}(C)=
 \max_M\sum_{a\in M}{\bf1}_{c(a)\in C},
\tag{1.4}
\]

where \(M\) ranges over perfect source--target option matchings of
\(G_{efsg}\).  Parallel options are retained in (1.4), because two options
with the same endpoints may carry different colours.  If the unweighted
graph has no perfect matching, the collar is immediately impossible and no
value of (1.4) is needed.

Any lower-q1-complete continuation must satisfy the exact necessary
inequality

\[
 \boxed{\mu_{efsg}(C)\ge |C|\qquad(C\subseteq C_0).}
\tag{1.5}
\]

The value in (1.4) is an integral max-cost flow: source-to-\(S\),
\(S\)-to-\(T\) option arcs, and \(T\)-to-sink all have unit capacity, while
an option arc has profit \({\bf1}_{c(a)\in C}\).  Hence there is no rounding
qualification in (1.5).  If a set \(C\) violates (1.5), the guarded clause

\[
 \neg p_{ef}\vee\neg x_s\vee\neg x_g
\tag{1.6}
\]

is valid for that semantic collar.

For the critical full set \(C=C_0\), exact replay gives

\[
 \boxed{\mu_{efsg}(C_0)=428=|C_0|+1}
\tag{1.7}
\]

for all \(4\cdot640\cdot35=89,600\) collars.  Thus the full-set
assignment-capacity cut has exactly one unit of positive slack everywhere;
it does not eliminate a branch.

No claim is made that every proper subset \(C\subsetneq C_0\) was tested.
Equation (1.5), rather than a purported all-subset verdict, is the reusable
separator delivered by this note.

## 2. Separate Hall projections

For comparison, project \(G_{efsg}\) separately onto colours--sources and
colours--targets.  On the target side \(\star_{BA}\) is one ordinary
capacity-one vertex.  Each graph has 427 uncovered colours and 428 slots.

The 22,400 collars of one branch collapse to 1,925 semantic profiles, with
profile multiplicities

\[
 10^{490},\qquad 12^{1400},\qquad 20^{35}.
\]

Every profile has matching number 427 in both projections.  Expanded back
to collars, in every one of the four branches:

\[
 \nu(H_S)=\nu(H_T)=427\quad\text{in all 22,400 cases}.
\tag{2.1}
\]

The exact minimum-degree census is

\[
\begin{array}{c|c}
\text{quantity}&\text{collar histogram per branch}\\ \hline
\min_{c\in C_0}d_{H_S}(c)&6^{18900},7^{3500}\\
\min_{c\in C_0}d_{H_T}(c)&7^{19180},8^{3220}\\
\min_{u\in S}d_{H_S}(u)&5^{22400}\\
\min_{v\in T}d_{H_T}(v)&6^{5600},7^{16800}.
\end{array}
\tag{2.2}
\]

For the endpoint-coupled graph restricted to colours in \(C_0\), the
minimum source degree is

\[
 31^{2288},\quad32^{400},\quad35^{19712},
\tag{2.3}
\]

and every graph has a perfect matching of size 428, which is the explicit
witness for (1.7).

The quotient incidence counts used in the projection reduction are not
silently assumed to be eight-regular.  Composite \(15\) produces 14
degree-seven vertices/colours:

\[
 d=7^{14},8^{415}.
\]

For a fixed colour--B-target incidence, the number of quotient source
providers is \(6^{98},7^{3320}\); for a BA colour it is
\(7^{14},8^{415}\).  Consequently deleting the two ordered source nodes
cannot erase a target incidence.  The exceptional source \(B_1\) is handled
by literal history enumeration, which leaves exactly five deletion colours.

## 3. Unit-voltage covariance and the 21-case reduction

Multiplication by a unit of \(\mathbb Z_{15}\), followed by canonical
rotation, maps transition options, colours, order endpoints, and history
coordinates bijectively.  The exact transports from the audited reference
middle 380 are

\[
 380\xrightarrow{11}384,qquad
 380\xrightarrow{7}395,qquad
 380\xrightarrow{2}406.
\tag{3.1}
\]

After including the canonical-frame phase correction on history, the full
1,925-profile multiset transports exactly in all three cases.  Therefore
(1.1)--(2.3) were computed once on the reference and replayed under an
audited option-level isomorphism, not inferred from matching histograms
alone.

The ten next-collar q3 labels form two unit-group orbits:

\[
 \{587,601,617,841,1171,1609,2341,2633\},
 \qquad\{589,713\}.
\tag{3.2}
\]

At the parent q2 level, the exceptional middles have three unit orbits:

\[
 \{380,384,395,406\},\qquad
 \{378,381,383,405\},\qquad
 \{396\}.
\tag{3.3}
\]

Thus allowing any unit quotient voltage preserves every option-level
collar propagation proved here and reduces the old nine-middle by
seven-pattern portfolio from 63 to \(3\cdot7=21\) orbit cases.  This is a
symmetry reduction of formulas, not an existence proof.

The five-state and 22,400-collar counts in Theorems 1--3 are proved for the
four middles in \(\mathcal O_{80}\).  The reduction of the other two middle
orbits to representatives 378 and 396 is supplied by the separate global
unit-symmetry theorem; these collar counts are not silently asserted for
those different 120-prefix formulas.

The production successor-clause constructor is nevertheless generic over an
AAAB terminal family.  Lightweight regression on representatives 378 and
396 gives 960 terminal paths, 33,600 rows, successor histogram
\(34^{640}35^{32960}\), and 1,175,360 fresh-colour extensions with zero local
repeats in each case.  This tests the one-step propagation hook in all three
AAAB middle-orbit representatives used by the 21-case interface.  It does
not extend the Hall/flow verdict of Theorem 3 beyond \(\mathcal O_{80}\), and
the 18 non-AAAB orbit formulas do not satisfy this AAAB collar hypothesis.

## 4. Proof audit and sharp surviving gate

The five-by-seven partition is obtained by literal substitution in the
54,856-option catalogue.  The q3 intersection depends on which of the five
history-safe coordinates is deleted, while the inserted coordinate gives
the seven options in that class.  The lower colour also depends only on the
deleted coordinate.  The finite audit separately verifies distinctness of
the five canonical colours for all 2,560 terminal fragments.

For the next edge, deleting any of the three updated history coordinates
removes 21 of the 56 raw B-to-B options.  Of the 35 history-safe options,
the binary order removes one immediate return in exactly 200 collars per
branch.  Direct colour replay gives (1.2) in all remaining 783,800 cases.

The two projection matchings and the endpoint-coupled matching are ordinary
integral bipartite matchings.  The exact profile transport (3.1) supplies
the other three formulas.  The scan includes the ten terminal fragments per
parent branch
already excluded by the strengthened terminal q1 excess clauses; proving
positive slack on this larger set automatically proves it on each actual
strengthened formula.

The conclusion is negative but sharp: no one-collar colour/source Hall,
colour/target Hall, one-extra-edge Hall, or full-uncovered endpoint-coupled
capacity cut closes any of the four AAAB formulas.  A genuine obstruction
must use a proper colour subset in (1.5), several collars simultaneously,
or longer Hamilton/history structure.  More timed branch solves are not
justified by this local audit.

## 5. Reproducibility

* audit source:
  `scratch/audit_threadD_k16_aaab_collar_colour_order_history_20260730.py`
* source SHA-256:
  `d5c23ad37f8bba5d325bc56d93e94ac55cccde17c564174aa0cdaff054889491`
* audit JSON:
  `scratch/threadD_k16_aaab_collar_colour_order_history_20260730.audit.json`
* file SHA-256:
  `62a97203a8c1ded50a2613cff008620b3b4db2c3bb5eb68977f501e066ff5413`
* stable payload SHA-256:
  `732b06c5b7d3268510a602e3c04bedf3a13fc700695650bfb6938c4148749dce`
* current catalogue-constructor dependency:
  `scratch/audit_joint_rail_quotient_history_model_20260730.py`, SHA-256
  `415891be220e7fb18ac51eaf23a2d2eef7fd5a8e0cf170f879b6ac4f591feec2`

The lightweight production regression
`scratch/test_threadD_k16_q23_disjoint_portfolio_20260730.py` checks the
emitted 22,400-row family and independently replays the four branch summaries
from this audit.  It does not treat either the propagation rows or the
positive Hall slack as a feasibility certificate.

The audit uses only the Python standard library and the frozen exact
catalogue constructors.  Its recorded wall time is 16.67 seconds.  It does
not invoke a solver.
