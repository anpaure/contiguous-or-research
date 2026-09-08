# Thread K: an exact Catalan-leave semilength lift, functorial no-go, and seam/port budget

Date: 2026-07-29

## 0. Verdict

There is an exact semilength-raising construction at the degree-two level,
but there is no literal functorial/ECO inheritance theorem of the form sought.

The positive construction starts with an oriented lower-rainbow Johnson
factor on `2r-1` coordinates.  It chooses one occurrence of every upper
first-shadow target, leaving exactly

\[
             b=\operatorname {Cat}_r
\]

parent positions, and uses a cap-two incidence factor on the remaining
positions.  Four explicit edge formulas then give a literal lower-rainbow
Johnson 2-factor on `2r+1` coordinates.  No edge completion or fractional
rounding is hidden in the proof.

What is not automatic is precisely what matters for a passing carrier:

* old-coordinate residence on the new cycles;
* the lower `q=2,3` and upper flag supports;
* cyclic phase/voltage;
* a child one-core with the required Hall ports.

The forced Catalan leave has an exact chronology ledger.  At lower or upper
depth `q`, it cuts at most `qb` pure occurrences in each of the `X` and `Y`
families separately, and at most `(q+1)b` pure `U` occurrences.  The new `A`
cycles, pure-`U` lower windows, and cross-leave mixed windows are the
non-parent-consecutive coverage sources after surviving inherited duplicates
are retained.  Thus the construction is a theorem, while the
simultaneous choice of the leave, its cap-two factor, protected flag
witnesses, and residual one-core ports is the exact remaining lemma.

There are four independent obstructions to strengthening this theorem to a
literal inherited recursion.

1. A locally bijective edge-functorial selector lift is a graph covering.
   For a connected parent it would force `Cat_(m+1)/Cat_m` to be an integer,
   which is false for every `m>=5`.
2. The raw boundary has

   \[
        \Gamma_5=C_{42},\qquad
        \Gamma_6=C_{119}\sqcup C_{13}.
   \]

   Both child components need an odd parity-breaking correction.
3. Across all `462` plane-tree leaf insertions from the frozen `k=11`
   selector, only `17/132` raw `k=13` rows can inherit both marks from any
   parent.  At least `115` quotient rows and `133` individual marks must
   change.
4. The canonical raw one-core ports do not inject across the boundary:
   every old singleton has six ports, while every child singleton has one.

The result is therefore neither a claimed all-odd recursion nor merely a
finite negative fit.  It supplies an exact non-ECO degree-two lift, proves a
universal covering obstruction, and identifies the single simultaneous
chronology/port gate which a successful induction must discharge.

Only lightweight exact parsing of the frozen `42`- and `132`-row atlases was
used.  No SAT solver, exhaustive carrier search, or long local job was run.

## 1. Parent notation and the forced Catalan leave

Let

\[
 r\ge2,\qquad |\Omega|=2r-1,\qquad
 W=\binom{2r-1}{r},
\]

and let

\[
 F=(T_i)
\]

be an oriented spanning Johnson 2-factor on \(\binom{\Omega}{r}\).  Indices are
cyclic on each component.  Put

\[
 C_i=T_i\cap T_{i+1},\qquad
 V_i=T_i\cup T_{i+1}.                       \tag{1.1}
\]

Assume that `F` is lower-rainbow, so the `C_i` enumerate
\(\binom{\Omega}{r-1}\), and that its upper first shadow is complete, so the
`V_i` cover \(\binom{\Omega}{r+1}\).

Choose an occurrence transversal `I`: the map

\[
 i\longmapsto V_i
\]

is a bijection from `I` onto \(\binom{\Omega}{r+1}\).  Let `J=I^c`.  Then

\[
 |I|=\binom{2r-1}{r+1},
\]

and hence

\[
 \begin{aligned}
 |J|
 &=\binom{2r-1}{r}-\binom{2r-1}{r+1}\\
 &=\frac{2}{r+1}\binom{2r-1}{r}
  =\frac1{r+1}\binom{2r}{r}
  =\operatorname {Cat}_r.
 \end{aligned}                                      \tag{1.2}
\]

Thus the Catalan leave is not a loss estimate: its size is forced by the
four-sector layer cardinalities.

## 2. The exact Catalan-leave lift

Define the bipartite graph

\[
 \mathcal P_I=
 \left(\binom{\Omega}{r-2},I;E\right),
 \qquad Z\sim i\quad\Longleftrightarrow\quad Z\subset C_i.       \tag{2.1}
\]

Both shores have size

\[
 \binom{2r-1}{r-2}=\binom{2r-1}{r+1}=W-\operatorname {Cat}_r.
\]

### Theorem 2.1 (literal four-sector factor)

If `P_I` has a simple bipartite 2-factor `K`, then adjoining two coordinates
`x,y` produces an explicit lower-rainbow spanning Johnson 2-factor on
\(\binom{\Omega\cup\{x,y\}}{r+1}\).

#### Construction

The child upper owners are

\[
 \begin{array}{ll}
 A_i=C_i\cup\{x,y\},& i\text{ arbitrary},\\
 X_i=T_i\cup\{x\},& i\text{ arbitrary},\\
 Y_i=T_i\cup\{y\},& i\text{ arbitrary},\\
 U_i=V_i,&i\in I.
 \end{array}                                           \tag{2.2}
\]

For every child lower color choose exactly the following edge.

If the two `K`-neighbors of
\(Z\in\binom{\Omega}{r-2}\) are `i,j`, use

\[
       Z\cup\{x,y\}:\qquad A_iA_j.                     \tag{2.3}
\]

For every `i`, use

\[
 C_i\cup\{x\}:\qquad
 \begin{cases}
 X_iX_{i+1},&i\in I,\\
 X_iA_i,&i\in J,
 \end{cases}                                           \tag{2.4}
\]

and

\[
 C_i\cup\{y\}:\qquad
 \begin{cases}
 Y_iY_{i+1},&i\in I,\\
 A_iY_{i+1},&i\in J.
 \end{cases}                                           \tag{2.5}
\]

Finally put

\[
 L_i=
 \begin{cases}
 U_{i-1},&i-1\in I,\\
 X_i,&i-1\in J,
 \end{cases}
 \qquad
 R_i=
 \begin{cases}
 U_i,&i\in I,\\
 Y_i,&i\in J,
 \end{cases}                                           \tag{2.6}
\]

and use

\[
                 T_i:\qquad L_iR_i.                   \tag{2.7}
\]

#### Proof

The owners in (2.2) enumerate the complete child upper layer.  The `A_i`
are distinct because the lower-rainbow colors `C_i` are distinct.  The
`X_i` and `Y_i` give two copies of the complete old middle layer with
different new-coordinate signatures.  The occurrence transversal makes the
`U_i` one copy of every old rank-`r+1` set.  These four families are disjoint.

Every displayed pair has the named intersection.  For (2.3), distinct
`C_i,C_j` both contain `Z`, so their intersection is exactly the
rank-`r-2` set `Z`.  Equations (2.4) and (2.5) follow from
\(T_i\cap T_{i+1}=C_i\).  In (2.7), the only case needing comment is
`i-1,i in I`.  Then `U_(i-1)` and `U_i` are distinct: equality would give
two selected occurrences of the same `V`, contrary to transversality.
Both contain `T_i`, so their intersection is exactly `T_i`.

The four color families

\[
 \begin{split}
 &\{Z\cup\{x,y\}:|Z|=r-2\},\\
 &\{C\cup\{x\}:|C|=r-1\},\\
 &\{C\cup\{y\}:|C|=r-1\},\\
 &\{T:|T|=r\}
 \end{split}
\]

partition the complete rank-`r` child layer.  Each is used once.

It remains to check degrees.

* If `i in I`, `A_i` has its two `K`-edges.  If `i in J`, it has
  `X_iA_i` and `A_iY_(i+1)`.
* `X_i` always has the edge of color `C_i+x`.  Its second edge is
  `X_(i-1)X_i` when `i-1 in I`, and the `T_i` edge when `i-1 in J`.
* `Y_i` always has the edge of color `C_(i-1)+y`.  Its second edge is
  `Y_iY_(i+1)` when `i in I`, and the `T_i` edge when `i in J`.
* For `i in I`, `U_i` occurs exactly on the edges of colors `T_i` and
  `T_(i+1)`.

Every child upper owner therefore has degree two.  This proves the theorem.
\(\square\)

The theorem does not assert connectedness or translation invariance.  Those
properties are not needed for exactness of the factor, but a later compiler
must account for its components and phases.

### Theorem 2.2 (exact cap-two Hall criterion)

The required `K` exists if and only if, for every

\[
             \mathcal A\subseteq\binom{\Omega}{r-2},
\]

one has

\[
 \boxed{
 \sum_{i\in I}
 \min\left(2,\left|\{Z\in\mathcal A:Z\subset C_i\}\right|\right)
 \ge 2|\mathcal A|.}                                  \tag{2.8}
\]

#### Proof

Use the integral network

\[
 s\longrightarrow Z\ [2],\qquad
 Z\longrightarrow i\ [1],\qquad
 i\longrightarrow t\ [2].                            \tag{2.9}
\]

For a fixed set `A` on the left, minimizing a cut independently at each
right vertex yields capacity

\[
 \sum_i\min(2,\deg_{\mathcal A}(i)).
\]

Thus max-flow/min-cut gives (2.8).  The two shores have the same size, so a
flow saturating every left capacity also saturates every right capacity.
Unit middle-edge capacities make the selected graph simple.  Integrality
gives a literal 2-factor. \(\square\)

This is the first exact algebraic gate.  It is stronger than ordinary
positive degree and weaker than the chronology conditions below.

## 3. Residence: exact for the two new labels, open for the old labels

Write `s_i=1_I(i)`.  The `K`-cycles consist only of `A` owners, so `x` and
`y` are constant on them.

### Theorem 3.1 (leave-gap criterion)

Let `j,k` be consecutive positions of `J` on one parent component, with
cyclic distance `g=k-j`.  The mixed child cycles contain exactly the
following maximal nonconstant runs:

\[
 X_{j+1},X_{j+2},\ldots,X_k,A_k                 \tag{3.1}
\]

for coordinate `x`, and

\[
 A_j,Y_{j+1},Y_{j+2},\ldots,Y_k                 \tag{3.2}
\]

for coordinate `y`.  Both have length `g+1`.

Consequently `x,y` satisfy depth-`d` residence if and only if every cyclic
`J`-gap on every component meeting `J` is at least `d`.

#### Proof

Between consecutive leave positions, (2.4) joins all successive `X`
owners.  At the right leave position it joins `X_k` to `A_k`; the next edge
leaves `A_k` for a `Y` owner, which omits `x`.  At the left boundary, the
`T_(j+1)` edge enters `X_(j+1)` from an owner omitting `x`.  This gives
(3.1).  Equation (3.2) is the reflected argument using (2.5).  The all-`A`
cycles create no finite boundary run. \(\square\)

On a single Hamilton parent component the scalar spacing condition is

\[
                    W\ge d\operatorname {Cat}_r,       \tag{3.3}
\]

and is sharp if the leave positions are otherwise free.  It is only a
capacity condition: the occurrence-transversal requirement may forbid the
desired spacing.

For `k=11 -> 13`, `r=6`, and depth `d=3`,

\[
 (W,b,d)=(462,132,3),\qquad W-db=66.                    \tag{3.4}
\]

Thus the two new coordinates have scalar spacing slack.  This does not
settle the constrained transversal.

For an old coordinate `z`, put
\(t_i(z)=\mathbf 1_{\{z\in T_i\}}\).  Its traces on the
four owner types are exactly

\[
 X_i,Y_i:t_i,\qquad
 A_i:t_it_{i+1},\qquad
 U_i:t_i\lor t_{i+1}.                                  \tag{3.5}
\]

The `K` edges couple the `A_i` in an order unrelated to the parent cycles.
Therefore old-coordinate residence is not inherited from residence of
`T`.  Equation (3.5), read on every actual `K` and mixed cycle, is the exact
statewise residence test.  This is the first unresolved condition in the
positive lift.

## 4. Exact lower/upper signature ledger

For a child factor cycle `S`, define

\[
 L_q^S(a)=\bigcap_{h=0}^{q}S_{a+h},\qquad
 U_q^S(a)=\bigcup_{h=0}^{q}S_{a+h}.                    \tag{4.1}
\]

Let `B` be the subset of `{x,y}` in the resulting target and put `s=|B|`.
Call a lower window expected-rank when
\(|L_q^S(a)|=r+1-q\), and an upper window expected-rank when
\(|U_q^S(a)|=r+1+q\).  Only such windows can witness the corresponding
rank layer.  For expected-rank windows, deleting `x,y` gives the exact old
ranks

\[
 \begin{aligned}
 |L_q^S(a)\setminus\{x,y\}|&=r+1-q-s,\\
 |U_q^S(a)\setminus\{x,y\}|&=r+1+q-s.
 \end{aligned}                                        \tag{4.2}
\]

Relative to an old rank-`r` chronology, these are lower depth `q+s-1` and
upper depth `q+1-s`.  For `q=2,3` the rank ledger is

\[
\begin{array}{c|ccc}
 &s=0&s=1&s=2\\ \hline
\text{child lower }q=2&L_1&L_2&L_3\\
\text{child lower }q=3&L_2&L_3&L_4\\
\text{child upper }q=2&U_3&U_2&U_1\\
\text{child upper }q=3&U_4&U_3&U_2.
\end{array}                                           \tag{4.3}
\]

This table is a rank/signature identity, not an occurrence identity.  On a
pure `X` or `Y` run, both towers are literal old consecutive windows.  On a
pure `U` run only the upper tower has the simple formula

\[
 \bigcup_{h=0}^{q}U_{i+h}
 =\bigcup_{h=0}^{q+1}T_{i+h}.                         \tag{4.3a}
\]

The corresponding lower expression

\[
 \bigcap_{h=0}^{q}(T_{i+h}\cup T_{i+h+1})             \tag{4.3b}
\]

need not be an old consecutive intersection.  On `A/K` and mixed windows
even the ordering is new.

### Proposition 4.1 (exact support equations)

The child has complete lower depth `q` if and only if, for every
\(B\subseteq\{x,y\}\),

\[
 \left\{
 L_q^S(a)\setminus\{x,y\}:
 L_q^S(a)\cap\{x,y\}=B,
 \ |L_q^S(a)|=r+1-q
 \right\}
 =\binom{\Omega}{r+1-q-|B|}.                           \tag{4.4}
\]

It has complete upper depth `q` if and only if

\[
 \left\{
 U_q^S(a)\setminus\{x,y\}:
 U_q^S(a)\cap\{x,y\}=B,
 \ |U_q^S(a)|=r+1+q
 \right\}
 =\binom{\Omega}{r+1+q-|B|}.                           \tag{4.5}
\]

These are set-support equalities; multiplicity is irrelevant to coverage.

#### Proof

Every expected-rank child target has a unique new-coordinate signature `B`,
and deleting that signature is a bijection to the old layer on the right of
(4.4) or (4.5).  Equations (4.2) give the ranks.  Turnaround windows of the
wrong rank are excluded and cannot witness that layer. \(\square\)

In particular, old carrier information only through depths two and three
cannot by itself imply the child `q=3` claims.  The both-new lower signature
projects to the old `L_4` rank and must be proved directly on the `A/K`
chronology (or supplied by protected old depth-four data).  The no-new upper
signature on a pure `U` run is literally old `U_4`.  A valid recursion must
carry or replace these depth-four witnesses.

### Proposition 4.2 (Catalan halo of the four-sector lift)

Put

\[
 \mathcal H_q(J)=
 \{i:\{i,i+1,\ldots,i+q-1\}\cap J\ne\varnothing\}.    \tag{4.6}
\]

A pure `X` or pure `Y` depth-`q` window survives exactly when its `q`
internal indices avoid `J`.  A pure `U` depth-`q` window needs `q+1`
consecutive indices in `I`.  Hence

\[
 |\mathcal H_q(J)|\le q b,                             \tag{4.7}
\]

and the inherited occurrence losses are bounded by

\[
\begin{array}{c|cc}
 &X/Y\text{ separately}&U\\ \hline
q=2&2b&3b\\
q=3&3b&4b.
\end{array}                                           \tag{4.8}
\]

If the cyclic leave gaps exceed the relevant halo length, the occurrence
loss bounds are equalities.  A target may still retain another surviving
pure duplicate.  After all such surviving pure occurrences are retained,
the non-parent-consecutive coverage sources are the pure-`U` lower windows
of (4.3b), `A/K` windows, and windows crossing a leave position.

#### Proof

One leave position belongs to at most `q` intervals in (4.6), proving
(4.7).  The `X/Y` statement follows directly from (2.4)--(2.5).  A run of
`q+1` successive `U` owners is destroyed by a leave in any of its `q+1`
positions.  Disjoint halos give equality. \(\square\)

Thus the unavoidable correction supply in this construction is extensive:
`b=Cat_r` marked positions, not `O(1)` seams.  The exact question is whether
their new windows satisfy (4.4)--(4.5), not whether the scalar layer counts
balance.

## 5. Degree two as an integral correction problem

Return to the marked-Dyck quotient at semilength `m+1`.  Let
`B_(m+1)` be its bipartite incidence multigraph: a lower Dyck row `P` is
incident through token `t` to the upper Dyck vertex `psi(P,t)`.

Every left and right vertex has degree `m+2`.  A selector is exactly an
arc-simple `(2,2)`-biregular spanning subgraph of this incidence multigraph;
parallel quotient endpoints are allowed when their token arcs differ.

### Theorem 5.1 (exact correction circulation)

Let \(x^0_{P,t}\in\{0,1\}\) be any baseline choosing two tokens in every child
row, for example the two marks inherited from its unique ECO parent.  Put

\[
 d^0(Q)=\sum_{(P,t):\psi(P,t)=Q}x^0_{P,t}.
\]

A corrected degree-two selector is exactly `x=x^0+z`, where `z` is integral
and

\[
 -x^0_{P,t}\le z_{P,t}\le1-x^0_{P,t},                 \tag{5.1}
\]

\[
 \sum_tz_{P,t}=0\quad\text{for every }P,              \tag{5.2}
\]

\[
 \sum_{(P,t):\psi(P,t)=Q}z_{P,t}=2-d^0(Q)
 \quad\text{for every }Q.                             \tag{5.3}
\]

These equations are always feasible if no chronology restriction is added.

#### Proof

Equations (5.1)--(5.3) are respectively simplicity, left degree two, and
right degree two, so they are necessary and sufficient.  The regular
bipartite graph `B_(m+1)` has a perfect matching; deleting one leaves a
regular bipartite graph with another perfect matching.  Their union is
arc-simple and `(2,2)`-biregular.  Taking this incidence vector for `x`
proves feasibility. \(\square\)

More generally, if only a prescribed safe incidence set `E_safe` may be
used, the same cap-two flow proof as Theorem 2.2 says that a selector exists
if and only if, for every child-row family `A`,

\[
 \sum_Q\min(2,\deg_{\mathcal A}^{\rm safe}(Q))
 \ge2|\mathcal A|.                                    \tag{5.4}
\]

This completely solves the algebraic degree layer.  Residence, shadows,
and one-core Hall are properties of alternating walks and common owner
intervals after the 2-factor is selected; they are not consequences of total
unimodularity.

## 6. Why strict ECO cloning cannot work

Use the unique ECO parent obtained by deleting the rightmost peak.  For a
Dyck word `R`, let

\[
                 f(R)=1+\ell(R),                      \tag{6.1}
\]

where `ell(R)` is its final descent length.  This is the number of ECO
children of `R`.

Let `Gamma(pi_m)` be a parent selector graph.  Its edge labels and vertex
labels are both the complete set `D_m`.  At a parent vertex `Q`, let the two
incident edge rows be `P_-` and `P_+`.

### Theorem 6.1 (ECO fibre-balance and rigidity)

A strict parent-respecting clone lift can have degree two only if

\[
             f(P_-)+f(P_+)=2f(Q)                      \tag{6.2}
\]

at every parent vertex.  Moreover, (6.2) holds everywhere if and only if
`f` is constant on every connected component of the full vertex-edge
incidence graph of `Gamma(pi_m)`.

#### Proof

The two old incident rows contribute `f(P_-)+f(P_+)` inherited child
incidences above `Q`.  The `f(Q)` child upper vertices demand total degree
`2f(Q)`, proving necessity.

Assume equality.  Then

\[
 f(Q)^2\le\frac{f(P_-)^2+f(P_+)^2}{2}.                \tag{6.3}
\]

The edge labels and vertex labels are both `D_m`, so their multisets of
`f`-values agree.  Summing (6.3) over all vertices gives equality on the two
sides.  Strict convexity forces

\[
 f(P_-)=f(P_+)=f(Q)
\]

at every vertex, and hence constancy on components.  The converse is
immediate. \(\square\)

For a nonzero deficit

\[
 \delta_Q=2f(Q)-f(P_-)-f(P_+),                         \tag{6.4}
\]

the exact endpoint-transport relaxation needs

\[
 B(\pi_m)=\sum_Q\delta_Q^+
          =\frac12\sum_Q|\delta_Q|                    \tag{6.5}
\]

moved incidences.  This is exact when an incidence may be transported from
any surplus vertex to any deficit vertex; legal marked-Dyck adjacency can
only raise the cost.

For the frozen `k=11` selector, only `6/42` vertices satisfy (6.2), and

\[
                  B(\pi_5)=42.                        \tag{6.6}
\]

The raw `k=13` selector, projected through the same ECO parent maps, moves
`225` endpoints: only three child rows move none, `33` move one, and `96`
move both.  Its legal correction is therefore far from the unconstrained
lower bound.  This endpoint-parent comparison is distinct from natural
token-mark inheritance in Section 8.

## 7. Universal functorial and parity obstructions

Let an edge-functorial lift have maps

\[
 p_-:\mathcal D_{m+1}^{\rm low}\to\mathcal D_m^{\rm low},
 \qquad
 p_+:\mathcal D_{m+1}^{\rm up}\to\mathcal D_m^{\rm up},             \tag{7.1}
\]

such that each selected child edge maps to the selected parent edge indexed
by `p_-`.

### Theorem 7.1 (covering obstruction)

If the two child incidences at every upper vertex map to the two distinct
parent incidences, then `p_+` is a graph covering.  If the parent selector is
connected, this forces

\[
             \frac{\operatorname {Cat}_{m+1}}
                  {\operatorname {Cat}_m}
\]

to be an integer.  Since

\[
 \frac{\operatorname {Cat}_{m+1}}{\operatorname {Cat}_m}
 =4-\frac6{m+2},                                      \tag{7.2}
\]

no such lift exists for any `m>=5`.

#### Proof

The local condition is precisely local bijectivity onto a 2-regular parent
graph.  A finite cover of a connected graph has a constant integer sheet
number on each child component; summing the sheets is still an integer.
Equation (7.2) is nonintegral for `m>=5`. \(\square\)

For a disconnected parent the divisibility conclusion applies separately
over its components and cannot be replaced by one global ratio.

There is also no nontrivial physical lift commuting with old and new cyclic
translations.  Any homomorphism between `Z_(2m+1)` and `Z_(2m+3)` is trivial
because the two orders are coprime.  A valid recursion must root the two
Catalan quotients separately and reconstruct phase/voltage globally.

### Corollary 7.2 (raw odd-cycle parity)

At the audited boundary,

\[
 \Gamma_5=C_{42},\qquad
 \Gamma_6=C_{119}\sqcup C_{13}.                       \tag{7.3}
\]

Pull back the bipartition of `C_42`.  Every inherited edge flips shore, so
each odd child component must contain an odd number of parity-breaking
edges.  At least two quotient selected edges, one in each component, are
therefore non-inherited.  Translation lifting gives at least

\[
 2\cdot13=26
\]

physical changed middle edges.  They touch at least four quotient upper
vertices, hence at least `52` physical upper vertices.  This lower bound is
sharp only in the abstract graph-homomorphism category; it is not a claim
that two legal marked-Dyck trades realize the raw factor.

For a construction made of `d` complete parent-cover sheets plus row
insertions or deletions, the arithmetic edit lower bound is

\[
 E_m=\min_{d\in\mathbb Z_{\ge0}}
 |\operatorname {Cat}_{m+1}-d\operatorname {Cat}_m|
 =\frac{\operatorname {Cat}_m}{m+2}\min(m-4,6),
 \qquad m\ge5.                                        \tag{7.4}
\]

At `m=5`, three sheets plus six rows is closest.  For `m>=10`, four sheets
with `6 Cat_m/(m+2)` deletions is closest.  This does not constrain
nonuniform ECO fibres or the four-sector construction.

## 8. Exact `k=11 -> 13` leaf-grafting audit

Inserting a plane-tree leaf is inserting a Dyck peak `UD`.  The frozen atlas
contains all `462` parent/child/insertion relations between `D_5` and
`D_6`.  For each relation the old two marks have a unique natural injection
into the seven child token labels `0,...,6`.

### Theorem 8.1 (all-leaf mark obstruction)

Among the `132` raw child rows, the best overlap over every possible deleted
leaf has distribution

\[
 \begin{array}{c|ccc}
 \text{number of inherited marks}&0&1&2\\ \hline
 \text{child rows}&18&97&17.
 \end{array}                                           \tag{8.1}
\]

Thus any leaf-parent rule with natural mark injection needs at least

\[
 132-17=115                                             \tag{8.2}
\]

quotient row replacements and at least

\[
 2\cdot18+97=133                                       \tag{8.3}
\]

individual mark replacements.  The 18 rows with zero overlap for every leaf
parent are

```text
UDUUDUDUDUDD
UDUUUDUDUDDD
UUDDUUDUDDUD
UUDDUUUDUDDD
UUDUDDUUDUDD
UUDUDUDDUDUD
UUDUDUDDUUDD
UUDUDUDUDUDD
UUUDDUDUDUDD
UUUDDUDUUDDD
UUUDDUUDDDUD
UUUDDUUDUDDD
UUUDDUUUDDDD
UUUDUDDDUUDD
UUUDUUUDDDDD
UUUUDUUDDDDD
UUUUUDUDDDDD
UUUUUUDDDDDD
```

#### Proof

Delete each peak of each child word, inject labels by their left-to-right
up-step order, and compare the resulting two-mark set with the raw child
marks.  This is a complete enumeration of the `462` mathematical relations,
not a search over carriers.  Taking the maximum overlap for each child gives
(8.1); (8.2)--(8.3) follow.  Every relation and the 18 witnesses are frozen
in the audit artifact of Section 11. \(\square\)

A quotient segment braid changing `R` selected row edges can repair at most
`R` such row disagreements.  Consequently, **if** a naturally inherited
row assignment itself forms a legal factor on the same child owner set, and
the only correction is an `R`-cut/`R`-join segment braid preserving every
other selected edge, then reaching the raw child requires

\[
                         R\ge115.                     \tag{8.4}
\]

The natural inherited assignment generally already fails degree two, so
(8.4) is not an unconditional seam lower bound.  It is also not an
asymptotic unbounded-seam theorem.  It does not rule out a different globally
corrected child.

### Proposition 8.2 (four canonical upper-parent capacity no-gos)

Order the parent upper vertices around `C_42`, and for a fixed peak-deletion
map put

\[
 a_j=|p_+^{-1}(j)|.
\]

If all child edges lie above parent edges and `b_j` counts edges above
`j(j+1)`, degree two forces

\[
                     b_{j-1}+b_j=2a_j.                \tag{8.5}
\]

The alternating sum of (8.5) vanishes.  For leftmost, rightmost, and first
deepest deletion, the audited absolute alternating sums are respectively

\[
                         2,4,6,                       \tag{8.6}
\]

so (8.5) is impossible.  Last-deepest deletion has alternating sum zero, but
with `z=b_41` the exact recurrence in the frozen cycle order requires
simultaneously `z>=6` and `z<=2`; it too is impossible.

In the relaxed inequalities

\[
                     b_{j-1}+b_j\le2a_j,              \tag{8.7}
\]

the maximum inherited-edge counts are

\[
 \begin{array}{c|rrrr}
 &\text{left}&\text{right}&\text{first deepest}&\text{last deepest}\\ \hline
 \max\sum b_j&130&124&124&128\\
 \text{nonparent lower bound}&2&8&8&4.
 \end{array}                                           \tag{8.8}
\]

These lower bounds are sharp in the aggregate integer `b`-matching
relaxation.  They are not asserted to be attainable by simple legal
marked-Dyck rows.

#### Proof

Equation (8.5) is the degree equation on every parent fibre.  Alternating it
around an even cycle proves (8.6).  For (8.7), maximum bipartite
`b`-matching equals minimum vertex cover with weights `2a_j`; the exact
42-cycle dynamic programme in Section 11 gives (8.8). \(\square\)

## 9. The raw one-core port boundary is not inherited

For a depth envelope `P` and one-core `C`, a position `i` offers target `S`
exactly when

\[
                         C_i\subseteq S\subseteq P_i.  \tag{9.1}
\]

The canonical raw one-cores at both `k=11` and `k=13` pass their complete
physical Hall tests.  Their port distributions nevertheless differ sharply.

At `k=11`, the `11` singleton targets each have candidate degree `6`.  At
`k=13`, the `13` singleton targets each have candidate degree `1`.  Hence no
fixed coordinate injection and injective transport of old port positions can
carry the canonical old port graph into the canonical raw child port graph.
At least

\[
                    11(6-1)=55                         \tag{9.2}
\]

old singleton-port incidences must disappear, while the two new singleton
targets contribute two new incidences.

This is scoped to the canonical cores and a literal port-position injection.
A new child one-core may reorganize all ports.  If the only allowed port
loss is promotion of a seam endpoint core cell to its full envelope, at most
two columns change per seam.  The raw cores have no empty cell, so one column
can be a candidate for at most one singleton.  Equation (9.2) would therefore
force at least `28` physical seams.  That conclusion does not apply to a
globally rebuilt core.

## 10. Exact seam and one-core correction budgets

The Catalan leave of Theorem 2.1 is a cross-dimensional bulk feature.  A
separate same-dimensional rethreading may still be needed.  Its budget is as
follows.

### Theorem 10.1 (window seam ledger)

Let two legal factors on the same upper layer share all segment-interior
edges and differ by `R` old cuts and `R` new joins.  Segments may be reversed.
Let `lambda_q,lambda'_q` be their target-multiplicity vectors at depth `q`
on either one of the lower or upper towers.  Then

\[
 \begin{aligned}
 \#\text{old occurrences removed}&\le qR,\\
 \#\text{new occurrences created}&\le qR,\\
 \|\lambda'_q-\lambda_q\|_1&\le2qR,\\
 |\operatorname{supp}(\lambda_q)\setminus
   \operatorname{supp}(\lambda'_q)|&\le qR.
 \end{aligned}                                        \tag{10.1}
\]

In particular, if the old depth-`q` support is complete, the new support has
at most `qR` holes.  The first two bounds are equalities when all relevant
seam collars are disjoint.  Every new depth-`d` residence failure meets a new seam; there are
at most `dR` crossing depth-`d` windows, contained in inward halos of total
size at most `2dR` positions.

#### Proof

A window wholly inside a common segment has the same set of vertices after
transport; reversal does not change its intersection or union.  For one
seam exactly `q` possible starts of a `q+1`-vertex window cross it, unless
collars overlap.  Summing old losses and new gains proves (10.1).  A short
run disjoint from every new seam would be an unchanged internal run, proving
the residence localization. \(\square\)

If one quotient seam represents a full orbit at child order `n'`, replace
`R` by `n'R` in (10.1).

### Theorem 10.2 (one-core gluing budget)

There are two useful scopes.

1. If the envelope/core sequence itself is cut into common segments, carry
   `C` with each segment and set `C'_i=P'_i` at the two endpoints of every
   new seam.  Then

   \[
                       C'\subseteq P',\qquad DC'=DP',  \tag{10.2}
   \]

   and at most `2R` Hall columns change.
2. If the central factor is changed specifically by an `R`-cut segment
   braid and `P'` is its recomputed maximal depth-`d` erosion, transport the
   old core on the common safe interiors.  There are at most `dR` new
   seam-crossing erosion cells.  On their halo, enlarged by one unchanged
   envelope position at each outer boundary, set `C'_i=P'_i`.  The promoted
   set has size at most

   \[
                              (d+2)R.                 \tag{10.3}
   \]

   Again (10.2) holds.  This claim is not for an arbitrary central-factor
   modification with no common segment structure.

In the first scope an old saturating Hall matching loses at most `2R`
assigned targets; in the second it loses at most `(d+2)R`.  After reserving
all safe transported matches, exact preservation is equivalent to the
ordinary residual Hall inequalities for the lost targets against the new
halo ports and any freed safe ports.

#### Proof

On a common core edge the old identity holds.  At a genuinely new envelope
adjacency both endpoints are promoted, so the union is the full envelope
union.  At an outer promoted/unpromoted boundary, the two envelope cells are
an unchanged old adjacent pair.  Replacing one old core cell by its larger
envelope cannot destroy the old OR equality.  This proves (10.2).  Only the
promoted columns of (9.1) change, so deleting their previously matched
targets leaves all other matches valid. \(\square\)

The parity theorem by itself does not construct a legal inherited baseline
or a two-orbit rethreading.  **Conditionally**, if such a legal baseline and
two-quotient-seam correction exist at `k=13`, then there are
`R=2*13=26` physical seams and, per lower or upper tower,

\[
 \begin{array}{c|cc}
 &q=2&q=3\\ \hline
 \text{removed occurrences}&52&78\\
 \text{created occurrences}&52&78\\
 L^1\text{ change}&104&156.
 \end{array}                                           \tag{10.4}
\]

At depth `d=3`, residence auditing is confined to `78` crossing windows or
at most `156` halo positions.  Direct envelope-level core gluing changes at
most `52` Hall columns; recomputing the erosion and using the unconditional
halo construction changes at most `130`.  These are budgets, not a proof
that a two-seam legal marked-Dyck correction exists.

## 11. Frozen audit artifacts

The input atlas and source words are

```text
b77f40e1b60a6329e1c193f5f0ed9271b3e04945cb8e4d9d050cd9ce5ab6db06  scratch/k11_k13_k14_dyck_choice_atlas_20260729.json
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850  answers/k11.word
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0  answers/k13.word
```

The strict ECO fibre/endpoint audit is

```text
0001ce959e112aa26a2255e6b578df0f6068be10d769129632931cf9a6ca9679  scratch/analyze_k11_k13_eco_selector_lift.py
a754edd3be47d0a4fa34151b7df947e47d9fcb63d31e7da776c75bfac91ed787  scratch/k11_k13_eco_selector_lift_20260729.json
```

The all-leaf inheritance audit added for this theorem is

```text
0365e0e70815ef86bb28875cc0fb98dd446e48c8bbdb1d0f139061b4c71d468e  scratch/analyze_k11_k13_any_leaf_inheritance.py
1aa140732fdc5d61ee0a15cbd8dadb73569c735d3e7abdcb0fe16249dcff7486  scratch/k11_k13_any_leaf_inheritance_20260729.json
```

The four canonical upper-parent capacity audit is

```text
6b3d2186c6b744d8fac55c809e7e8f080c4363368c66b7b9b61a6dfbca89f981  scratch/audit_k11_k13_peak_parent_capacity.py
a6ab50460e0665f6fb12f997abe06bffb6255fe78c482e310bd4289e5a9d0501  scratch/k11_k13_peak_parent_capacity_20260729.json
```

The canonical one-core port census is

```text
dbb158455a9ca37bd50491d3fb416e78d37c251cf74c800aaef75925f8fab478  scratch/analyze_k11_k13_raw_onecore_ports.py
246bd77aa94625c4c46d14d43e2b2944ec6f26e57c7ec4c632115291c2796d48  scratch/k11_k13_raw_onecore_ports_20260729.json
```

Reproduction commands are lightweight:

```text
python3 scratch/analyze_k11_k13_eco_selector_lift.py
python3 scratch/analyze_k11_k13_any_leaf_inheritance.py
python3 scratch/audit_k11_k13_peak_parent_capacity.py
python3 scratch/analyze_k11_k13_raw_onecore_ports.py
```

The last command reconstructs the two frozen words and runs a small exact
Hopcroft--Karp audit on `231` and `1092` targets; it is not a search for a new
carrier.

## 12. Exact remaining theorem

The degree-two part is closed by either Theorem 2.1 or Theorem 5.1.  The
locally bijective edge-functorial, strict ECO-clone, translation-natural, and
natural mark-inheritance routes are closed by Sections 6--8.  Folded or
globally corrected lifts are not.  What remains is the following simultaneous
statement.

> **Catalan-leave chronology/port lemma.**  Given a passing parent flag
> factor, choose an upper-occurrence transversal `I` and a cap-two factor
> `K`, and perform any required cycle cuts/joins and rerooting, so that the
> **final** child satisfies all of the following simultaneously:
>
> 1. the leave `J` is componentwise depth-`d` spaced;
> 2. all coordinate traces are depth-`d` resident on every final cycle,
>    including the traces (3.5) and every later join halo;
> 3. the support equations (4.4)--(4.5) hold for lower `q=2,3` and every
>    additional lower or upper depth required by the intended passing-carrier
>    definition, with protected witnesses surviving the Catalan halos (4.8)
>    and the later join halos (10.1);
> 4. the child admits a one-core whose residual Hall system passes after the
>    exact sacrifice in Theorem 10.2;
> 5. if a translation quotient is required, global rerooting realizes the
>    prescribed voltage on every quotient component; unit voltage is needed
>    only on components intended to lift to one physical cycle.

No rankwise marginal theorem can replace this lemma: degree two is already
integrally feasible, and both raw factors already pass their separate
one-core Hall tests.  The obstruction is the common chronology coupling the
leave, old-coordinate runs, all flag signatures, and the same owner ports.

Conversely, with every depth required by the passing-carrier definition in
item 3, the lemma plus Theorem 2.1 is a literal semilength-raising recursion.
Restricted to the requested lower `q=2,3` interface, it gives only that
interface recursion.  This is the precise proved/conditional boundary; no
coefficient-one or all-odd claim is made here.

## 13. Independent proof-audit record

Two independent theorem audits were run against this note.

The construction audit checked every owner family, every intersection color,
the degree-two count, the cap-two min-cut, the new-label run formula, the
signature table, and all seam constants.  It caught the need to filter
turnaround windows by expected rank and the fact that pure-`U` lower windows
are not old consecutive intersections.  Sections 4 and 12 incorporate both
corrections.

The obstruction audit independently checked the covering and parity scopes,
the `115/133` leaf census, the four canonical fibre-capacity bounds, the
`55` singleton-port loss, and the `2R` versus `(d+2)R` one-core scopes.  It
required the legal-baseline hypotheses in Sections 8 and 10 and the narrower
list of closed functorial classes in Section 12.

After those corrections, both audits returned `PASS`.  All four lightweight
artifact generators were then rerun and reproduced the hashes in Section 11.
