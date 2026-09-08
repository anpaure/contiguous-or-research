# `k=17` marker58: protected diamond exchange, exact cap delta, and component fusion

Date: 2026-08-02  
Lane: A, pure mathematics and frozen-ledger audit  
Status: exact exchange calculus and complete conditional simple-`C6`/`C8`
generators.  This note does **not** prove that a profitable circuit exists in
the frozen factor; it gives the proof-safe object on which that finite
question must be asked.

## 0. Outcome

Let

\[
 \mathcal C={ [17]\choose 8},\qquad
 \mathcal T={ [17]\choose 9},\qquad
 \mathcal U={ [17]\choose 10}.
\]

The authenticated marker58 file is most naturally viewed as a spanning
two-factor of the bipartite containment graph between \(\mathcal C\) and
\(\mathcal T\).  Its 3,944 protected Johnson edges are 7,888 fixed incidence
edges.  After contracting them, all palette-preserving completions are
exactly the common bases of two capacity partition matroids.  Their complete
elementary exchange graph is the directed residual containment graph:

* a mutable selected incidence is directed `owner -> colour`;
* an unselected incidence is directed `colour -> owner`.

Directed circuits are precisely the protected palette-preserving switches.
For every such circuit this note gives:

1. the exact rank-ten cap multiplicity delta;
2. an orientation-free endpoint-matching formula for the component delta;
3. a reachability/min-cut criterion for installing one prescribed missing
   cap by a one-incidence exchange; and
4. complete finite `C6` and `C8` sufficient theorems which simultaneously
   increase distinct cap coverage and merge factor components.

For the last item, a protected-disjoint active aligned `3+1` `C8` works
exactly when its cap support gain is positive.  Every such simple `C8` is in
the star/octahedral transition join, whose dimension-17 upper bound is

\[
                         1,750,320.                         \tag{0.1}
\]

Thus the previously frozen active-`C8` face is directly relevant to the
marker58 carrier.  It is a complete candidate class for simple octagonal
two-component fusion, but it does not guarantee that a profitable candidate
exists.  In the incidence-factor model, unlike the separate directed
successor-permutation model, a `C6` is **not** parity-forbidden from a
two-to-one fusion; Section 5 gives the exact correction and the smaller
`C6` candidate bound.

The distinct-cap objective is not an additive weight on incidence elements,
so ordinary weighted matroid intersection does not solve the coupled upper
problem.  The exact atom lift is recorded in Section 8.

## 1. Frozen factor and protected residual ledger

Let \(G\) be the bipartite graph with vertex set
\(\mathcal C\mathbin{\dot\cup}\mathcal T\) and incidence \(C--T\) when
\(C\subset T\).  Let \(F\subset E(G)\) be the factor in

```text
scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv
```

For each colour `C`, its two neighbours in `F` are denoted
`T_C^0,T_C^1`.  Suppressing `C` gives the Johnson edge

\[
       e_C=T_C^0T_C^1,\qquad
       T_C^0\cap T_C^1=C,\qquad
       \upsilon_F(C)=T_C^0\cup T_C^1\in\mathcal U.          \tag{1.1}
\]

The frozen replay proves

\[
 d_F(C)=d_F(T)=2\quad(C\in\mathcal C,T\in\mathcal T),       \tag{1.2}
\]

so suppression preserves the 1,179 factor components.

There are 986 pairwise owner-disjoint protected paths, each with five
rank-nine owners and four coloured Johnson edges.  Write `P_J` for these
3,944 Johnson edges and `P` for their 7,888 incidence halves.  Fixing a path
edge means fixing **both** incidences at its colour.

### Lemma 1.1 (exact residual capacities)

The protected bank has:

\[
\begin{array}{c|r|r}
\text{object}&\text{count}&\text{residual incidence capacity}\hline
\text{protected colours}&3944&0\\
\text{internal protected-path owners}&2958&0\\
\text{protected-path endpoint owners}&1972&1\\
\text{owners outside the protected paths}&19380&2.
\end{array}                                                  \tag{1.3}
\]

Consequently there are 20,366 residual colours and total residual incidence
demand

\[
             1972+2(19380)=40732=2(20366).                  \tag{1.4}
\]

#### Proof

The paths are owner-disjoint by the marker packing audit.  Every five-owner
path has three internal owners and two endpoints.  Internal owners already
have two protected incidences, endpoints one, and all other owners zero.
There is one protected colour per protected path edge and all those colours
are distinct.  Subtracting from 24,310 gives (1.3), and summing the residual
capacities gives (1.4).  \(\square\)

Each protected path lies among the five rank-nine facets of one protected
rank-ten cap.  Hence its four edges give four fixed occurrences of that cap.
The 986 protected caps are distinct.  This explains the independently
replayed protected contribution `4^986`, or 2,958 unavoidable protected
repeat units.  It does not say that an unprotected edge cannot give a fifth
occurrence of one of these caps.

### Lemma 1.2 (exact complete-cap excess marginal)

For every rank-eight-rainbow owner two-factor on `[17]`, its rank-ten cap
multiset has point degree 14,300 at every coordinate.  If every rank-ten cap
is covered, the nonnegative excess multiset over one copy of every cap has

\[
             |E|=4862,\qquad \deg_E(x)=2860\quad(x\in[17]). \tag{1.5}
\]

In the marker58 protected face, three of the four mandatory copies of each
of the 986 protected caps belong to this excess.  They contribute

\[
             |E_P|=2958,\qquad \deg_{E_P}(x)=1740.          \tag{1.6}
\]

Consequently any upper-complete protected extension has a residual excess
multiset satisfying

\[
             |E_R|=1904,\qquad \deg_{E_R}(x)=1120.          \tag{1.7}
\]

These conditions are necessary, not sufficient.

#### Proof

Fix a coordinate `x`.  Since every rank-nine owner has factor degree two,
the sum of its endpoint incidences over all factor edges is

\[
                  2{16\choose8}=25740.                     \tag{1.8}
\]

For an edge with lower colour `C` and cap `U`, pointwise membership obeys

\[
 {\bf1}_{x\in T^0}+{\bf1}_{x\in T^1}
       ={\bf1}_{x\in C}+{\bf1}_{x\in U}.                 \tag{1.9}
\]

Every rank-eight colour occurs once, contributing
`binom(16,7)=11440` at `x`.  Subtracting from (1.8) gives cap degree 14,300.
One copy of every rank-ten cap has size 19,448 and point degree
`binom(16,9)=11440`.  Subtraction proves (1.5), including
`24310-19448=4862`.

By the frozen marker-orbit packing theorem, the 986 protected caps are 58
complete free `Z_17` orbits.  A rank-ten orbit
contains each coordinate ten times.  Three mandatory excess copies therefore
have size `3*986=2958` and point degree `3*58*10=1740`, proving (1.6).
Subtracting (1.6) from (1.5) proves (1.7).  Marginals alone neither pair
facets nor satisfy owner degrees, so sufficiency does not follow.  \(\square\)

## 2. Exact common-base model

For every vertex `v` of `G`, put

\[
                         b(v)=2-d_P(v).                      \tag{2.1}
\]

On the residual incidence ground set, let `M_C` be the direct sum, over
colours `C`, of uniform matroids of rank `b(C)`, and let `M_T` be the
analogous direct sum over owners `T` with rank `b(T)`.

### Theorem 2.1 (protected factors are common bases)

The map \(F'\mapsto F'\setminus P\) is a bijection between

1. spanning incidence two-factors `F'` containing every protected path
   edge; and
2. common bases of `M_C` and `M_T` of size 40,732.

Every such `F'` suppresses to a rank-eight-rainbow rank-nine owner
two-factor containing all 3,944 protected Johnson edges.

#### Proof

At every vertex, contraction of `P` leaves exactly the demand (2.1).
Independence in the two partition matroids imposes the two sets of upper
bounds.  A common independent set of total size
\(\sum_C b(C)=\sum_T b(T)=40732\) saturates every bound, and conversely every
protected two-factor has exactly these residual degrees.  Suppression is the
incidence-factor bijection.  \(\square\)

This is the exact matroid-intersection layer.  Cap coverage and connectivity
are additional correlated rows, not consequences of the common-base
description.

## 3. The protected residual exchange digraph

Relative to the frozen factor \(F\), form a directed graph \(\mathcal R_P(F)\)
on \(\mathcal C\mathbin{\dot\cup}\mathcal T\) as follows:

\[
\begin{array}{ll}
 T\longrightarrow C,& CT\in F\setminus P,\\
 C\longrightarrow T,& CT\notin F.
\end{array}                                                  \tag{3.1}
\]

Selected protected incidences have no removable arc.  Unselected arcs at a
fully saturated protected vertex are harmless: that vertex has no removable
arc and hence lies on no directed circuit.

Let a directed simple circuit be written

\[
 T_0\to C_0\to T_1\to C_1\to\cdots\to
 T_{q-1}\to C_{q-1}\to T_0.                                \tag{3.2}
\]

It removes `(C_i,T_i)` and adds `(C_i,T_(i+1))`, with indices modulo `q`.
Write

\[
 F^Q=F-\{C_iT_i:i\in\mathbb Z_q\}
       +\{C_iT_{i+1}:i\in\mathbb Z_q\}.                    \tag{3.3}
\]

### Theorem 3.1 (exact circuit correspondence)

Every directed simple circuit of `R_P(F)` gives a protected
palette-preserving incidence two-factor `F^Q`.  Conversely, for any other
protected incidence two-factor `F'`, the symmetric difference
\(F\mathbin{\triangle}F'\) decomposes into directed alternating circuits of
\(\mathcal R_P(F)\).

#### Proof

At each visited colour and owner, (3.3) deletes and adds one incidence.
Every other degree is unchanged, and no protected incidence is deleted.
This proves the forward statement.

For the converse, colour \(F\setminus F'\) negative and
\(F'\setminus F\) positive.
At every incidence vertex the negative and positive degrees agree because
both factors have degree two and contain `P`.  Pair opposite signs locally
and follow the pairings.  This decomposes the balanced signed graph into
closed alternating trails, and then into directed simple circuits.  \(\square\)

Thus `R_P(F)` is the exact palette-preserving exchange graph.  There is no
separate rank-eight palette check after a circuit toggle.

## 4. Exact cap delta

At a circuit colour `C_i`, let `R_i` be its selected neighbour different
from `T_i`.  It is retained by (3.3).  Define

\[
 U_i^-=R_i\cup T_i,\qquad U_i^+=R_i\cup T_{i+1}.             \tag{4.1}
\]

Both are rank-ten sets.  Put

\[
 m_F(U)=|\{C:\upsilon_F(C)=U\}|,
\quad r_Q(U)=|\{i:U_i^-=U\}|,
\quad a_Q(U)=|\{i:U_i^+=U\}|.                              \tag{4.2}
\]

### Theorem 4.1 (cap multiplicity and support identity)

For every \(U\in\mathcal U\),

\[
                 m_{F^Q}(U)=m_F(U)-r_Q(U)+a_Q(U).            \tag{4.3}
\]

If `d_10(F)=|{U:m_F(U)>0}|`, then

\[
\begin{split}
 d_{10}(F^Q)-d_{10}(F)
   ={}&|\{U:m_F(U)=0,\ a_Q(U)>0\}|\\
     &-|\{U:m_F(U)>0,\ m_F(U)-r_Q(U)+a_Q(U)=0\}|.          \tag{4.4}
\end{split}
\]

#### Proof

Only the pair at a touched colour changes, from `(R_i,T_i)` to
`(R_i,T_(i+1))`, proving (4.3) after summing equal cap values.  A support
value is gained exactly in the first set of (4.4), and lost exactly in the
second.  \(\square\)

Call `Q` cap-monotone when

\[
        m_F(U)-r_Q(U)+a_Q(U)\ge1
        \quad\text{for every }U\text{ with }m_F(U)>0.        \tag{4.5}
\]

### Corollary 4.2 (strict cap gain)

A cap-monotone circuit which creates at least one currently missing cap
strictly increases `d_10`.  More generally it increases `d_10` if and only
if the first cardinality in (4.4) exceeds the second.

The aggregate condition (4.5), rather than the unsafe rule “every deleted
cap has load at least two”, is necessary when a circuit removes several
occurrences of the same cap or recreates an old cap elsewhere.

For the frozen marker58 factor,

\[
 d_{10}(F)=13307,\qquad
 |\mathcal U|-d_{10}(F)=6141,\qquad
 \sum_U(m_F(U)-1)_+=11003.                                  \tag{4.6}
\]

Equation (4.4) is therefore the exact score needed by a local circuit
catalogue; no degree or scalar-repeat proxy is sufficient.

## 5. Orientation-free component delta

Let `Z_Q` be the `2q` endpoints of the removed incidence edges in (3.2).
After deleting those edges from `F`, every retained path pairs two members
of `Z_Q`.  Let `alpha_Q` be this fixed-point-free path-pairing involution.
Let

\[
 \rho_Q=\prod_i(T_i\ C_i),\qquad
 \beta_Q=\prod_i(C_i\ T_{i+1})                              \tag{5.1}
\]

be respectively the deleted-edge and new-edge matchings on `Z_Q`.

### Theorem 5.1 (endpoint-matching component formula)

The numbers of old and new touched components are

\[
 k_{\rm old}(Q)={c(\alpha_Q\rho_Q)\over2},\qquad
 k_{\rm new}(Q)={c(\alpha_Q\beta_Q)\over2},                \tag{5.2}
\]

where `c(pi)` is the number of permutation cycles.  Hence

\[
       \operatorname{comp}(F^Q)-\operatorname{comp}(F)
       ={c(\alpha_Q\beta_Q)-c(\alpha_Q\rho_Q)\over2}.       \tag{5.3}
\]

#### Proof

The union of two perfect matchings is a disjoint union of even cycles.  If
the matchings are involutions `a,b`, every union cycle gives two cycles of
the permutation `ab`; hence the number of union cycles is `c(ab)/2`.
Joining the retained-path matching `alpha_Q` first with the deleted matching
`rho_Q` reconstructs the old touched components.  Joining it with the new
matching `beta_Q` constructs the new ones.  Untouched components cancel,
giving (5.3).  \(\square\)

This formula needs no arbitrary orientation of the old components.  It also
handles repeated cuts on one component without replacing physical
occurrences by dense component ids.

For a simple `C8`, three cuts on one component and one on another give
`2 -> 1` exactly in the aligned cyclic order; the opposite order gives three
touched components.  This is an evaluation of (5.2).

### Proposition 5.2 (no incidence-factor `C6` parity obstruction)

A simple alternating `C6` can algebraically change two touched components
into one.  Thus the two-to-one `C6` obstruction for a directed successor
permutation must not be imported into the present incidence-factor model.

#### Proof

Write the removed matching and the forward added matching as

\[
 \rho=(t_0c_0)(t_1c_1)(t_2c_2),\qquad
 \beta=(c_0t_1)(c_1t_2)(c_2t_0).
\]

Take the retained-path pairing

\[
             \alpha=(t_0c_0)(t_1t_2)(c_1c_2).              \tag{5.4}
\]

Then `c(alpha rho)=4`, so the old support has two components, whereas
`c(alpha beta)=2`, so the new support has one.  The pairs in (5.4) have the
correct bipartite path parities.  Here is a literal Boolean-incidence
realization of the three retained paths.  Choose distinct `s_0,s_1 in S`
and distinct `a,b,c,d,e` outside the rank-seven set `S`, and put

\[
 c_0=S+a,\quad c_1=S+b,\quad c_2=S+c,
 \qquad
 t_0=S+a+c,\quad t_1=S+a+b,\quad t_2=S+b+c.
\]

Using `+` for adjoining elements and `\sim` for incidence adjacency, take

\[
\begin{aligned}
 P_0: &t_0\sim((S\setminus\{s_0\})+a+c)
       \sim((S\setminus\{s_0\})+a+c+d)\\
      &\sim((S\setminus\{s_0\})+a+d)\sim(S+a+d)\sim c_0,\\
 P_t: &t_1\sim((S\setminus\{s_1\})+a+b)
       \sim((S\setminus\{s_1\})+a+b+c)\\
      &\sim((S\setminus\{s_1\})+b+c)\sim t_2,\\
 P_c: &c_1\sim(S+b+e)\sim(S+e)\sim(S+c+e)\sim c_2.
\end{aligned}                                             \tag{5.4a}
\]

Successive ranks alternate between eight and nine, the internal vertices
are distinct, and the endpoint pairing is exactly (5.4).  Adding `rho`
closes `P_0` as one cycle and joins `P_t,P_c` as a second; adding `beta`
instead joins all three paths into one cycle.  Thus bipartiteness and the
Boolean incidence geometry impose no local two-to-one parity obstruction.
The two removed edges on the second old component have opposite parity in
that component.  An extra rule forcing every removed edge into one
predesignated constituent one-factor would exclude this pattern, but no
such rule is present in the marker58 degree-two factor fibre.  Whether the
frozen marker58 factor supplies these paths remains a literal catalogue
question.  \(\square\)

Every Boolean-incidence `C6` has a rank-seven core `S` and three distinct
petals, with

\[
             C_i=S+a_i,\qquad T_i=S+a_i+a_{i+1}.            \tag{5.5}
\]

Indeed, its three lower vertices are pairwise Johnson-adjacent.  A triangle
of rank-eight sets is either a star over a common rank-seven set or a top
inside one rank-nine set.  In the top case all three pairwise unions are the
same owner, whereas a simple `C6` has three distinct owner vertices.  Only
the star case remains.

The same degree-two transition join gives at most

\[
 \left\lfloor { {17\choose7}\,10\,2^2\over3}\right\rfloor
                         =259306                            \tag{5.6}
\]

canonical active directed `C6`s before protection, component, and cap
filters.  Hence (5.6), scored by (4.4) and (5.2), is the smallest complete
simple-circuit face for marker58.  The `C8` face remains the exact next face
and supplies the aligned `3+1` actuator when no suitable hexagon exists.

Protection gives a sharper input bound.  A profitable circuit cannot root
at any of the 3,944 protected lower colours, because both incidences there
are fixed.  Rooting instead at one of the 20,366 mutable colours, choosing
one of its eight rank-seven cores, and then using the same two degree-two
continuations gives at most

\[
 \left\lfloor {20366\cdot8\cdot2^2\over3}\right\rfloor
                         =217237                            \tag{5.7}
\]

canonical active directed `C6`s before the remaining protection, component,
and cap filters.  This is an upper bound on a complete proof-safe catalogue,
not an existence assertion.

### Theorem 5.3 (complete protected simple-`C6` improvement face)

Generate the star triples (5.5) from the selected degree-two transition
table, reject every triple whose removed incidence is protected, and score
the surviving toggle by (4.4) and (5.2).  This emits, exactly once, every
simple alternating incidence `C6` which fixes all 3,944 protected marker
edges, strictly increases distinct rank-ten cap coverage, and decreases the
number of owner-factor components.  The input has at most 217,237 canonical
keys by (5.7).

#### Proof

The rank-seven-core classification preceding (5.6) is exhaustive, and the
least cyclic root removes exactly the three presentations of a directed
triple.  Avoiding the removed protected incidences is necessary and
sufficient for fixing the protected rows.  The exact cap and topology
conclusions are respectively (4.4) and (5.2); hence neither a valid key nor
an invalid key is lost by the declared filters.  \(\square\)

## 6. A one-cap service reachability criterion

Fix a currently missing cap \(U\) and a colour \(C\subset U\).  Suppose the
current pair at `C` is `{R,T^-}` and exactly one member, say `R`, is a
rank-nine facet of `U`.  Let `T^+` be the other rank-nine facet of `U`
containing `C`.  Then

\[
                 R\cup T^+=U.                              \tag{6.1}
\]

If `C` is unprotected and `CT^+` is unselected, the residual graph contains
the directed service path

\[
                         T^-\to C\to T^+.                   \tag{6.2}
\]

### Theorem 6.1 (service path extension)

The one-incidence replacement (6.2) extends to a protected
palette-preserving alternating circuit if and only if

\[
 T^-\text{ is reachable from }T^+
 \text{ in }\mathcal R_P(F)-C.                              \tag{6.3}
\]

Equivalently, there is no directed cut separating `T^+` from `T^-` in that
deleted graph.  Every resulting circuit creates an occurrence of `U` at
`C`; its net cap and component effects are exactly (4.4) and (5.3).

#### Proof

A directed path from `T^+` back to `T^-`, chosen simple, closes (6.2) into a
directed simple circuit.  Theorem 3.1 applies and (6.1) gives the advertised
cap.  Conversely, deleting (6.2) from any containing directed circuit leaves
such a path.  Directed reachability is equivalent to the stated cut
condition.  \(\square\)

If neither current neighbour of `C` is a facet of `U`, no circuit visiting
`C` only once can install `U` there: one old neighbour remains after the
switch.  Such a service needs a repeated-colour/compound exchange.  This is
the first exact boundary between simple circuits and higher-support moves.

Theorem 6.1 is only a palette/protection criterion.  A service circuit can
still exhaust another cap or split components, which is why (4.4) and (5.3)
must be checked on the closed circuit.

## 7. The complete profitable simple-`C8` theorem

Every simple `C8` in the rank-eight/rank-nine Boolean incidence graph is of
one of the following two forms.

* **Star:** for a rank-seven core `S` and distinct petals
  `a_0,...,a_3`,
  \[
    C_i=S+a_i,\qquad T_i=S+a_i+a_{i+1}.
  \]
* **Octahedral:** for a rank-six core `S` and distinct petals
  `a_0,...,a_3`,
  \[
    C_i=S+a_i+a_{i+1},\qquad
    T_i=S+a_i+a_{i+1}+a_{i+2}.
  \]

Indices are modulo four.  In either case one phase removes `(C_i,T_i)` and
adds `(C_i,T_(i-1))`.  The reverse phase reverses this directed word.

At each `C_i`, let `R_i` be its other selected owner.  The literal cap
change is

\[
 U_i^-=R_i\cup T_i,\qquad U_i^+=R_i\cup T_{i-1}.            \tag{7.1}
\]

The identities (7.1) prove directly that owner and colour degrees are
unchanged: `T_i` is removed at `C_i` and reinserted at `C_(i+1)`, while
`C_i` loses and gains one incidence.

### Theorem 7.1 (protected cap-improving two-component fusion)

Let `Q` be an active simple `C8` of either family in the marker58 factor.
Assume:

1. none of its four removed incidences belongs to `P`;
2. the endpoint-matching test gives
   `k_old(Q)=2` and `k_new(Q)=1` (equivalently, on the `3+1` face, the
   three cuts on the repeated component occur in the aligned cyclic order);
3. the exact cap score (4.4) is positive.

Then `F^Q` is another exact rank-eight-rainbow rank-nine owner two-factor,
contains all 3,944 protected marker edges, has one fewer component, and has
strictly more distinct rank-ten caps.

Conversely, every simple-`C8` switch with these four conclusions satisfies
conditions 1--3.

#### Proof

Theorem 3.1 proves factor and protection preservation.  Theorem 5.1 and
condition 2 give the one-component decrease.  Theorem 4.1 and condition 3
give strict cap gain.  Conversely, protection forces condition 1, the
claimed component change is exactly condition 2 by (5.2), and strict cap
gain is exactly condition 3 by (4.4).  \(\square\)

### Corollary 7.2 (clean sufficient test)

It suffices in Theorem 7.1 to replace condition 3 by:

* every old cap remains positive under (4.3); and
* at least one value among the four `U_i^+` is currently missing.

Then the cap gain equals the number of distinct currently missing values
among the `U_i^+`.

### Theorem 7.3 (complete finite `C8` candidate face)

For any dimension-17 incidence two-factor, all active directed simple
`C8`s are generated exactly once by the star and octahedral transition
joins.  Before protection, component, and cap filtering, their canonical
count is at most

\[
 388960+1361360=1750320.                                    \tag{7.2}
\]

Therefore filtering that join by the literal protected-incidence test,
(5.2), and (4.4) emits every marker58 simple-`C8` satisfying Theorem 7.1,
with no false rejection.

#### Proof

At every colour there are two selected owner transitions.  The star join
has at most
`binom(17,7)*10*2^3/4=388960` directed rotation classes.  The octahedral
join has at most
`binom(17,6)*11*10*2^2/4=1361360`.  The star/octahedral classification is
disjoint and complete, and the directed least-rotation key removes exactly
the four rootings without identifying the reverse phase.  The remaining
tests are literal conclusions of Theorems 3.1, 4.1, and 5.1.  \(\square\)

The bound (7.2) is reused from the active-`C8` transition theorem, but no
round-02 factor count or verdict is transported to marker58.  A new literal
join against the marker58 incidence table is required for any finite
existence or no-go claim.

Only the star/octahedral transition classification and count are imported.
Any “`C8` is the smallest two-component actuator” conclusion based on the
directed-successor cut permutation is outside the present incidence-factor
scope and is superseded here by Proposition 5.2.

## 8. Why weighted matroid intersection is not the upper solver

Theorem 2.1 may suggest assigning weights to incidences and solving one
weighted common-base problem.  This cannot represent even one prescribed
cap reward.

Fix a colour `C` and four containing owners `C+a,C+b,C+c,C+d`.  Suppose a
reward is one exactly for the selected pair `{C+a,C+b}` and zero for the
other five pairs.  If incidence weights `w_a,w_b,w_c,w_d` represented it,
then

\[
 w_a+w_b=1,\qquad w_i+w_j=0
 \quad\text{for every other pair }\{i,j\}.                  \tag{8.1}
\]

From `w_a+w_c=w_a+w_d=w_c+w_d=0` one gets
`w_a=w_c=w_d=0`, and then `w_b+w_c=0`, contradicting
`w_a+w_b=1`.  Thus the pair-at-a-colour cap statistic is genuinely
quadratic on incidence variables.

An exact lift uses atom variables

\[
 p_{C;T,T'}\in\{0,1\}
 \quad(C\subset T,T',\ T\ne T')                            \tag{8.2}
\]

and cap indicators `y_U`.  The complete protected owner/palette/upper model
is

\[
\begin{array}{rl}
 \sum_{\{T,T'\}}p_{C;T,T'}&=1 \quad(C\in\mathcal C),\\
 \sum_{(C;A,B):\,T\in\{A,B\}}p_{C;A,B}&=2
                                      \quad(T\in\mathcal T),\\
 p_{C;T,T'}&=1 \quad\text{for every protected Johnson edge},\\
 y_U&\le\sum_{C,\,T\cup T'=U}p_{C;T,T'} \quad(U\in\mathcal U).
\end{array}                                                  \tag{8.3}
\]

Maximizing `sum_U y_U` gives exact distinct-cap coverage.  If a connected
owner factor is required, add the exact subtour rows

\[
 \sum_{C,\,|\{T,T'\}\cap S|=1}p_{C;T,T'}\ge2
 \quad(\varnothing\ne S\subsetneq\mathcal T).               \tag{8.4}
\]

For a degree-two owner graph, (8.4) is equivalent to connectivity.  This is
the exact upper-aware atom model; it is not a two-matroid intersection.
The separate running Boolean-diamond CNF is one finite realization of this
correlated layer and is not duplicated here.

## 9. Scope and frozen evidence

The conclusions proved here are:

* exact protected palette-preserving exchange graph;
* exact cap and component deltas for every closed circuit;
* exact one-cap service reachability/min-cut;
* complete conditional simple-`C6` and simple-`C8` simultaneous cap/fusion
  theorems; and
* the marker58-applicable `217,237` protected-`C6` and `1,750,320`
  universal-`C8` prefilter bounds.

They do **not** prove:

* that a circuit satisfying Theorem 7.1 exists;
* that repeated profitable circuits can reach cap completeness or one
  component;
* that an individually profitable circuit remains profitable after another
  circuit;
* source/buffer occurrence binding, chronology, residence, ranks 11--17,
  all-width interval support, common-cap compilation, or a `k=17` word.

Frozen inputs used at exactly this scope:

* factor SHA-256
  `0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e`;
* factor audit SHA-256
  `6e1598c481ff41cde4fc99159acf0737bd30ba9585c4261fe213fff2b29060c6`;
* independent replay SHA-256
  `518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d`;
* marker-reservoir theorem SHA-256
  `bf072e7c74918ad729a14ba030e866de895444df85a5af02ecd2230357e40ee7`;
* active-`C8` transition theorem SHA-256
  `c2ee92ef642f16b3be0061d8ca7ae9bd3cac51292115fe067eb3b050791f52b5`.

No SAT call, exhaustive circuit enumeration, or heavy local computation was
used for this note.
