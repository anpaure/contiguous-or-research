# The one-collar all-dimensional target: exact matching gate, insured opening, and finite bases

Date: 2026-08-01  
Lane: additive-constant rooted q1 / adjacent-upper interface  
Status: exact necessary-and-sufficient finite certificate, exact conditional
insurance theorem, and complete finite calibration through owner rank five.
The all-dimensional upper-surjective Hamilton extension remains unproved and
unrefuted.

## 0. Verdict

Let the odd Middle Levels host have ground size \(2m-1\), owner rank \(m\),
and let the shortest rotating-hole collar have residence depth \(h\).

The new protected-factor theorem applies to the bare all-plus collar in all
sufficiently large dimensions:

\[
 |E_J(P_h^+)|=h+5,\qquad
 |E_{\rm ML}(\widehat P_h^+)|=2h+10,
 \qquad 2h+10\le m-2.                                    \tag{0.1}
\]

For \(h=\Theta(\sqrt m)\), the last inequality eventually holds.  It gives a
spanning q1-rainbow two-factor containing the collar.  It does not give the
requested theorem.  Three correlated rows are absent:

1. the planted incidences must receive the prescribed tail/head colouring;
2. the resulting owner permutation must be one Hamilton cycle; and
3. the paired owner unions must cover every rank-\((m+1)\) colour.

For a bare aligned collar there is a fourth row: one upper-safe common cut
must exist on each of the two residual cycles produced by reversal.  This
row is not automatic.  A literal \(m=4\) upper-surjective Hamilton target
has a residual five-cycle all of whose common edges are unique upper
providers.

A two-edge insurance connector removes the fourth row and also turns the
two protected plus paths into one directed path.  Conditional on an
upper-surjective Hamilton completion containing that connected path, two
upper-safe common cuts then exist for every \(m\ge4\) and
\(1\le h\le m-3\).

No counterexample to the remaining completion theorem appears in the first
two feasible owner ranks.  Exact finite search is positive for every
feasible bare depth at \(m=4,5\), and for every connector-legal insured
depth there.  The independently frozen recursive-depth census additionally
gives bare completions at \((m,h)=(6,3),(7,3)\).  This is finite evidence
only.

## 1. What the protected two-factor theorem actually plants

Write

\[
 {\cal Q}={ [2m-1]\choose m-1},\qquad
 {\cal O}={ [2m-1]\choose m},\qquad
 W=|{\cal Q}|=|{\cal O}|.                                \tag{1.1}
\]

The shortest collar consists of the rotating return rail of \(h+2\)
Johnson edges and the three all-plus ternary edges.  Hence it has \(h+5\)
Johnson edges.  Its incidence lift is a disjoint union of two alternating
paths, has maximum degree two, and has \(2h+10\) incidence edges.

The small protected-factor theorem therefore proves:

### Proposition 1.1 (unconditional q1 factor planting)

If

\[
                             2h+10\le m-2,                \tag{1.2}
\]

then the all-plus shortest collar is contained in a spanning q1-rainbow
two-factor of the Middle Levels graph.

This conclusion is unoriented.  The two protected paths may lie on the same
factor component with incompatible relative directions, the factor may
have a bulk number of components, and its paired upper unions may omit
rank-\((m+1)\) colours.

The connector of Section 4 changes the protected support into one path.
Its incidence lift has \(2h+14\) edges, so the same theorem gives a spanning
q1 factor containing it when

\[
                             2h+14\le m-2.                \tag{1.3}
\]

Because the protected support is then connected, its factor component may
be oriented to agree with the complete planted direction.  Hamiltonity and
upper surjectivity still do not follow.

## 2. Exact directed matching certificate

For every \(q\in{\cal Q}\), a directed q1 occurrence chooses two distinct
owners containing \(q\): a tail \(t(q)\) and a head \(s(q)\).

### Theorem 2.1 (exact rooted upper-decorated Hamilton certificate)

A directed q1-rainbow Hamilton cycle containing a specified directed
protected path \(P\) and covering every adjacent-upper colour exists if and
only if there are maps

\[
                         t,s:{\cal Q}\longrightarrow{\cal O}             \tag{2.1}
\]

such that:

1. \(q\subset t(q),s(q)\) and \(t(q)\ne s(q)\) for every \(q\);
2. both \(t\) and \(s\) are bijections;
3. for every planted arc \(u\to v\) of colour \(q=u\cap v\),
   \(t(q)=u\) and \(s(q)=v\);
4. the owner permutation
   \[
                              \pi=s\circ t^{-1}            \tag{2.2}
   \]
   is one \(W\)-cycle; and
5. the paired unions are surjective:
   \[
       \{\,t(q)\cup s(q):q\in{\cal Q}\,\}
                    ={ [2m-1]\choose m+1}.                \tag{2.3}
   \]

#### Proof

In a directed q1-rainbow factor, each lower colour occurs on one directed
Johnson edge, every owner occurs once as a tail and once as a head, and
therefore the two incidence shores are exactly the bijections \(t,s\).
The arc from owner \(u\) ends at
\(s(t^{-1}(u))=\pi(u)\), so factor components are precisely the cycles of
\(\pi\).  Thus the factor is Hamiltonian exactly when \(\pi\) is one cycle.
The upper colour of the \(q\)-edge is \(t(q)\cup s(q)\), giving (2.3).
Fixing the path arcs is exactly row 3.  The reverse construction is
immediate from the same statements. \(\square\)

The protected-factor theorem controls only the unordered union of the two
incidence matchings.  It supplies neither the prescribed \(t/s\) colouring,
the one-cycle row (2.2), nor the nonlinear paired cover (2.3).

## 3. Bare reversal and the exact safe-cut row

Let an adjacent-upper-surjective Hamilton target contain the bare aligned
plus collar.  In its cyclic orientation the two protected components occur
as

\[
 A\longrightarrow{\cal R}\longrightarrow D
 \longrightarrow Q_D\longrightarrow C\longrightarrow B
 \longrightarrow Q_A\longrightarrow A,                 \tag{3.1}
\]

where \(Q_D,Q_A\) are the two complementary common paths.

Reversing the ternary triple produces exactly:

1. the resident rotating-hole sidecar;
2. the residual cycle \(CD+Q_D\); and
3. the residual cycle \(AB+Q_A\).

The reverse preserves the complete adjacent-upper multiplicity vector,
because the old and plus ternary triples have equal upper multisets and the
rail is common.

For an upper colour \(R\), let \(\mu(R)\) be its multiplicity in the target
cycle.  Build a bipartite graph whose left nodes are the two residual
cycles and whose right nodes are upper colours.  Join residual cycle \(i\)
to \(R\) when it has a common \(R\)-edge, and give \(R\) capacity

\[
                                b(R)=\mu(R)-1.             \tag{3.2}
\]

### Proposition 3.1 (two-cycle upper-safe opening)

One common edge can be cut from each residual cycle while preserving
adjacent-upper surjectivity if and only if this capacitated bipartite graph
has a matching covering both left nodes.  Equivalently, for every subset
\(I\) of the two residual cycles,

\[
                       |I|\le\sum_{R\in N(I)}b(R).         \tag{3.3}
\]

#### Proof

Cutting \(k_R\) occurrences of colour \(R\) preserves that colour exactly
when \(k_R\le\mu(R)-1\).  Each residual cycle needs one cut and one edge
cannot serve two cycles.  These are precisely the stated capacitated
matching constraints; capacitated Hall gives (3.3). \(\square\)

Global upper surjectivity does not imply (3.3).  The authenticated
\(m=4,h=1\) warning fixture is a directed q1-rainbow Hamilton target,
contains the aligned collar, and covers all 21 rank-five upper colours.
After reversal its components have sizes

\[
                                  4+5+26.                 \tag{3.4}
\]

Every common edge on the residual five-cycle is the unique provider of its
upper colour.  Thus the one-node instance of (3.3) already fails.

## 4. The insured connected path

Use the shortest-collar notation

\[
 E=L+d,\quad F=L+a,\quad C=L-b+c+d,\quad D=L+c,          \tag{4.1}
\]

with rotating labels \(x_0,\ldots,x_{h-1}\).  If
\(1\le h\le m-3\), choose

\[
 r\in L\setminus\{b,x_0,\ldots,x_{h-1}\},\qquad
 R=L+c+d,\qquad T=R-r.                                  \tag{4.2}
\]

Then

\[
                           D\longrightarrow T\longrightarrow C           \tag{4.3}
\]

is a Johnson two-path.  Its lower colours are new, while both connector
upper colours equal \(R\), which is also the upper colour of \(ED\) in the
plus phase and \(CD\) in the old phase.  The protected plus support becomes
one directed path

\[
       A\longrightarrow F\longrightarrow{\cal R}\longrightarrow E
        \longrightarrow D\longrightarrow T\longrightarrow C
        \longrightarrow B                                      \tag{4.4}
\]

with \(h+7\) Johnson edges.

### Theorem 4.1 (upper insurance)

Let \(m\ge4\), \(1\le h\le m-3\), and suppose an adjacent-upper-surjective
directed q1-rainbow Hamilton cycle contains (4.4).  Reverse the ternary
triple.  Then two edges common to both phases can be cut so that:

1. the old phase consists of the resident sidecar, an opened
   \(DTC\)-triangle, and an opened bulk path;
2. the plus Hamilton cycle is opened into two paths;
3. both phases lose the same two distinct lower-q1 colours; and
4. both phases remain adjacent-upper surjective.

#### Proof

Reversal creates the resident rail cycle, the triangle
\(D-T-C-D\), and one bulk cycle.  Cut either connector edge.  The upper
colour \(R\) retains two local providers in both phases.

Put

\[
 W={2m-1\choose m},\qquad M={2m-1\choose m+1},\qquad
 \Delta=W-M={2W\over m+1}.                              \tag{4.5}
\]

In any upper-surjective \(W\)-edge factor, the number of edge occurrences
whose upper colour has multiplicity at least two is at least
\(\Delta+1\).  Indeed, if \(t\ge1\) upper colours repeat, those occurrences
number \(\Delta+t\).

For the stated range,

\[
                               \Delta+1>h+7.              \tag{4.6}
\]

Therefore one repeated-colour edge lies outside the protected path (4.4),
on the unique bulk segment.  It is common to both phases: every edge of the
plus Hamilton cycle outside (4.4) is unchanged by the ternary reversal.
Cut it.  If its colour is not \(R\), its other provider survives.  If its
colour is \(R\), then the three protected \(R\)-occurrences plus this bulk
occurrence leave at least two providers after both cuts.  Reversal preserves
the complete upper multiplicity vector, so the same conclusion holds in
both phases.  Lower q1 injectivity makes the two cut colours distinct.
\(\square\)

This theorem removes orientation ambiguity and the bare safe-cut Hall row.
It does not construct the upper-surjective Hamilton completion in its
hypothesis.

## 5. Complete finite calibration

The first nominal owner rank \(m=3\) is structurally infeasible: outside
\(U\) there is only one label, whereas the ternary exterior \(c\) and rail
exterior \(y\) must be distinct.  Hence \(m=4\) is the first legal host.

### Theorem 5.1 (all feasible bare depths at \(m=4,5\))

For every feasible pair

\[
                 (m,h)\in\{(4,1),(4,2),(5,1),(5,2),(5,3)\},              \tag{5.1}
\]

there is an explicit directed q1-rainbow Hamilton target containing the
canonical aligned shortest rotating-hole collar, covering every adjacent
upper colour, and admitting a two-edge common cut which preserves that
coverage after reversal.

The reverse component sizes and numbers of upper-safe cut tuples are:

\[
\begin{array}{c|c|c}
(m,h)&\text{reverse component sizes}&\text{safe cut tuples}\\ \hline
(4,1)&4+6+25&80\\
(4,2)&5+13+17&97\\
(5,1)&4+4+118&146\\
(5,2)&5+24+97&864\\
(5,3)&6+17+103&447.
\end{array}                                               \tag{5.2}
\]

### Theorem 5.2 (all connector-legal depths at \(m=4,5\))

For

\[
                         (m,h)\in\{(4,1),(5,1),(5,2)\},   \tag{5.3}
\]

there is an explicit upper-surjective directed q1 Hamilton cycle containing
the insured connected path (4.4).  Reverse component sizes are respectively

\[
                         3+4+28,\qquad3+4+119,\qquad3+5+118.              \tag{5.4}
\]

The independent replay applies one connector cut and one upper-safe bulk
cut, verifies two distinct q1 debts, and verifies complete upper
surjectivity in both phases.

For fixed \((m,h)\), the full coordinate group is transitive on all legal
bare collar tuples, and also on all legal insured tuples.  The ordered role
labels map coordinatewise, while unused core and exterior labels map
arbitrarily.  Hence each canonical witness proves existence for every
individual legal single-collar choice at the same finite \((m,h)\).

These are exhaustive depth rows only at \(m=4,5\); they are not an
induction.  Together with
`MATH_THEOREM_ROTATING_HOLE_H1_UPPER_HAMILTON_FINITE_CENSUS_20260801.md`,
they also show that the recursive-depth bare target is positive through
owner rank seven.  The insured finite search was not extended to those two
ranks because Theorem 4.1 has already made the connector's cut row
solver-free; the still-relevant question there is the completion itself.

## 6. Exact all-dimensional residue

The requested all-dimensional statement implies, after forgetting the
protected path, the existence for all sufficiently large \(m\) of a
q1-rainbow Middle Levels Hamilton cycle whose paired upper turns cover every
rank-\((m+1)\) colour.  That upper-turn-surjective Hamilton statement is not
proved by the ordinary Middle Levels theorem or by the protected
two-factor theorem.

The new Catalan-connector normal form makes this residue more explicit.
For every planted directed arc \(u\to v\) of lower colour \(q=u\cap v\),
put its tail incidence \(qu\) in \(P_0\) and its head incidence \(qv\) in
\(P_1\).  Thus the directed incidence lift is properly two-edge-coloured as

\[
                              P=P_0\mathbin{\dot\cup}P_1.  \tag{6.1}
\]

Each colour class has \(h+7\) edges.  Whenever \(h+7\le m-1\), the
matching \(P_0\) extends to a perfect incidence matching \(M_0\): after
deleting the \(p=h+7\) matched endpoints, every remaining lower family
\(A\) has at least

\[
 |N(A)|-p\ge |A|+\min\{m-1,W-|A|\}-p\ge |A|             \tag{6.2}
\]

remaining upper neighbours, so Hall applies.

Put

\[
 K={2m-1\choose m+1},\qquad
 C_m=W-K={2W\over m+1}=\operatorname{Cat}_m.             \tag{6.3}
\]

Relative to \(M_0\), every second-matching edge has one paired upper label
and one link edge on the lower shore.  Specializing the exact
Catalan-connector decomposition to one component gives the following.

### Proposition 6.1 (protected Catalan-connector form of the remaining gate)

Fix a perfect matching \(M_0\supseteq P_0\).  An upper-surjective Hamilton
completion containing the insured path, **whose first incidence matching is
this \(M_0\)**, and admitting an upper-transparent bulk opening exists if
and only if one can choose \(Q_0,Q_1\subseteq ML_m-M_0\) and an incidence
edge \(e_*\) such that:

1. \(Q_0\cup Q_1\) is a matching and
   \(P_1\subseteq Q_0\cup Q_1\);
2. \(Q_0\) has \(K=W-C_m\) edges, carries every rank-\((m+1)\) upper
   colour exactly once, and its labelled links form a forest with \(C_m\)
   components;
3. \(Q_1\) has \(C_m-1\) edges and its links form a loopless forest after
   those \(C_m\) components are contracted; and
4. \(e_*\notin M_0\) joins the one unmatched vertex on each incidence
   shore, and \(e_*\) avoids the protected support.

Without fixing the first matching in advance, the same statement holds
with \(M_0\supseteq P_0\) existentially quantified together with
\(Q_0,Q_1,e_*\).

#### Proof

The union \(Q_0\cup Q_1\) is a matching of size \(W-1\).  Its link graph
is a spanning tree: \(Q_0\) begins with \(C_m\) components and \(Q_1\)
supplies exactly \(C_m-1\) acyclic component joins.  Because a matching's
link graph has indegree and outdegree at most one, this spanning tree is a
directed Hamilton path.  The residual edge \(e_*\notin M_0\) completes the
second perfect matching and closes that path rather than creating a rooted
loop.  Hence the two matchings form one alternating Hamilton cycle.
Meanwhile \(Q_0\) gives the full upper palette and
the protected-edge conditions retain the insured path.

Conversely, delete one upper-transparent, unprotected second-matching edge
from a rooted upper-surjective Hamilton factor whose first matching is
\(M_0\).  The remaining \(W-1\) link edges form a spanning path.  Choose
one retained occurrence of every upper colour for \(Q_0\); the other
\(C_m-1\) path edges form \(Q_1\), and the deleted edge is \(e_*\).
It lies outside \(M_0\), since the two perfect matchings in a simple
alternating Hamilton cycle are disjoint.  This is exactly the
Catalan-connector decomposition. \(\square\)

The insurance theorem guarantees that, once the desired Hamilton target
exists, its bulk supplies the required upper-transparent unprotected edge.
Thus Proposition 6.1 is not adding another safe-cut hypothesis; it is the
exact two-scale integral content of the remaining Hamilton/upper gate.

The insured reduction leaves exactly the following statement:

> For every sufficiently large \(m\), with the recursive residence depth
> \(h=\Theta(\sqrt m)\), the connected protected path (4.4) extends to an
> adjacent-upper-surjective directed q1-rainbow Hamilton cycle.

If this statement holds, Theorem 4.1 supplies the two common upper-safe
cuts automatically.  If it fails, any counterexample must occur after the
owner/q1 factor extension and before the insured opening: it is a failure
of the rooted Catalan forest, its (C_m-1) component connectors, the
one-cycle permutation row (2.2), or their integral correlation.

The existing exact theorems therefore neither prove nor refute the all-\(m\)
claim.  They reduce it to one explicit two-perfect-matching problem with a
one-cycle and paired-union constraint, and remove the independent safe-cut
obstruction.

## 7. Audited artifacts

Finite bare search and replay:

* `scratch/search_o1_rooted_rotating_hole_upper_finite_20260801.py`,
  SHA `36f6d22d03091618de00502c4635797d6191dd3d5f611b46a7ff4ee293aa301c`;
* `scratch/o1_rooted_rotating_hole_upper_finite_20260801.search.json`,
  SHA `441b04ff4ca20c6b6759a7784c566da80e52301277a48fcc7b985cabaa7b7b34`,
  payload `2c2535555eb64d461bef6259848d262ac8b4e21f3d1ac2f3592ee191325b3fe4`;
* `scratch/audit_o1_rooted_rotating_hole_upper_finite_20260801.py`,
  SHA `891302e9986c4fbe3e8a5509f085215dd509ff26af189a172b697fa0f2fce9dd`;
* `scratch/o1_rooted_rotating_hole_upper_finite_20260801.audit.json`,
  SHA `d80c51fc692c2b8e67de267bef37d6eaeb1d5511d51f451b54b6ce639c2fb469`,
  payload `43d932505e2d835c09ae7c3df61f6aff1a7a2604520d55fc0922b0910cf8ea43`.

Finite insured search and replay:

* `scratch/search_o1_insured_rotating_hole_upper_finite_20260801.py`,
  SHA `30b23f35c31d194add8662f5660b6f102f44cd2eb33d82ce9849590b48defb0b`;
* `scratch/o1_insured_rotating_hole_upper_finite_20260801.search.json`,
  SHA `a51819d3b83004a50b3f22c477f2b3812730f5cdfb19c877b688fe7340c9bc74`,
  payload `65422494512f18145516088ee68a7986b3a963b2fd923064c47e94c2a6138798`;
* `scratch/audit_o1_insured_rotating_hole_upper_finite_20260801.py`,
  SHA `489cf3a0033b63b46e0e3a2c02918aff3a2c1ba89454ac3a4b6a251979640ed1`;
* `scratch/o1_insured_rotating_hole_upper_finite_20260801.audit.json`,
  SHA `2c7c6901aaa13724cb670407a5e3d32adbf81cf1570c18fe77e51104d1a1fd4d`,
  payload `66c07a1bbb2748394568d7922c4711d76490845f20c88a00b090dbfd2407afe1`.

Insurance formulas and unsafe-cut warning:

* `MATH_THEOREM_O1_SHORTEST_COLLAR_UPPER_INSURANCE_CONNECTOR_20260801.md`,
  SHA `e354a0b52e0a33b2f01c4ad47b4acef09b1e79f92dfaca0b4d1c21878f907452`;
* `scratch/audit_o1_shortest_collar_upper_insurance_connector_20260801.py`,
  SHA `ea983d358e26d4913e69b52f1038253a2aa30a7fc99e9c8c681193582bcf4b19`;
* `scratch/o1_shortest_collar_upper_insurance_connector_20260801.audit.json`,
  SHA `1d043ee31bedfa7bda40a9f0be8fa0a675af6448d6f4c4e3cc7136bb4ebbcda0`,
  payload `ab2ee14d5ccb34109efe666b378d0a004e0b9e79c1bd25b68b80342ec4a0512d`;
* `scratch/search_o1_ml7_collar_upper_unsafe_cut_20260801.py`,
  SHA `a010f9114be5c8c39f4a87e9c755f9a6c42d927352a800cfdf49f98d6a03711c`;
* `scratch/audit_o1_ml7_collar_upper_unsafe_cut_20260801.py`,
  SHA `61aac2525b471af2bfd534273fecc78c6732e8146c180237f6f594a53a2738b0`;
* `scratch/o1_ml7_collar_upper_unsafe_cut_20260801.audit.json`,
  SHA `0334cb247cad7d61f161cb2b70343e477fe7a51483e307135f40d265d5bdabca`,
  payload `bafd0e21af3b6c06f01022976c388b94fed7dcdee4cdb5ca70b1866e963a4f85`.
