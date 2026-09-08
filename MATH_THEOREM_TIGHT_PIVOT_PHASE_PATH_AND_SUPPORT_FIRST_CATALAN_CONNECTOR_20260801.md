# A tight pivot has a correlated protected phase, and the remaining Catalan
# gate admits a support-first reduction

Date: 2026-08-01  
Lane: tight pivot / protected owner phase / Catalan connector  
Status: exact protected specialization and exact sufficient reduction.
Existence of the global upper-surjective forest support remains open.

## 0. Outcome

The fixed-`M_0` counterexample for arbitrary protected tickets does **not**
apply to the native tight-pivot owner path when its matching phase is chosen
in correlation with that path.

For any simple Johnson path

\[
                  V_0,V_1,\ldots,V_\ell              \tag{0.1}
\]

with distinct lower intersections

\[
                  L_i=V_i\cap V_{i+1},qquad0\le i<\ell, \tag{0.2}
\]

put every predecessor incidence `L_i V_i` into the perfect class `M_0`.
After extending this small matching to a perfect matching, the successor
incidences `L_i V_(i+1)` contract to one directed path

\[
                L_0\longrightarrow L_1\longrightarrow\cdots
                     \longrightarrow L_\ell.          \tag{0.3}
\]

Thus their tails and heads are automatically distinct and their rooted
links are acyclic.  If the Johnson path has injective upper transition
colours, those protected colours are distinct as well.  The reverse phase
gives the reverse directed path.

For the tight split-pivot collar, `ell=3h`.  Hence the correlated phase
exists whenever `3Hh<=m-1` for `H` resource-disjoint copies; the established
`6Hh<=m-2` planting range implies this inequality.  The generic `m=3`
three-ticket obstruction is therefore a warning against selecting `M_0`
after the tickets, not an obstruction to the prospective pivot phase.

After this phase choice, the remaining owner theorem has a clean
support-first sufficient form:

1. build an upper-surjective directed linear forest support containing the
   protected pivot path(s);
2. select one occurrence of every upper colour inside that support, keeping
   every protected occurrence;
3. connect the resulting `C=Cat_m` path components through an acyclic
   free-port reservoir satisfying one-defect Hall.

Steps 2--3 are exact and integral.  Only Step 1 and construction of its
Hall-expanding connector reservoir remain open.

The four native lower-`q1` deficits of the older sparse split source are not
used as owner-layer structure here.  They may be carried only as additional
protected incidence tickets, subject to the same phase/matching count.  The
newer native-q1 repair removes them entirely at the local source level.

## 1. Correlated phase theorem

Work in the middle-levels incidence graph `ML_m` between ranks `m-1` and
`m` of `[2m-1]`.

### Theorem 1.1 (predecessor phase makes the successor shore one path)

Let (0.1) be a simple rank-`m` Johnson path and suppose the sets (0.2) are
distinct.  Define

\[
 P_0=\{L_iV_i:0\le i<\ell\},\qquad
 P_1=\{L_iV_{i+1}:0\le i<\ell\}.                       \tag{1.1}
\]

If `ell<=m-1`, then there is a perfect matching `M_0` containing `P_0`.
For every such extension, put

\[
                         L_\ell=M_0^{-1}(V_\ell).       \tag{1.2}
\]

Then

\[
 \lambda_{M_0}(P_1)
      =\{L_i\to L_{i+1}:0\le i<\ell\}.                \tag{1.3}
\]

In particular, `P_1` has distinct tails and heads and is a directed path.
Its upper labels are exactly

\[
                         V_i\cup V_{i+1}.               \tag{1.4}
\]

#### Proof

The owner vertices `V_0,...,V_(ell-1)` are distinct, and the lower vertices
`L_0,...,L_(ell-1)` are distinct, so `P_0` is a matching of size `ell`.
The protected small-matching extension theorem supplies `M_0` when
`ell<=m-1`.

For `0<=i<ell-1`, the matching contains

\[
                         M_0(L_{i+1})=V_{i+1}.          \tag{1.5}
\]

The contracted head of `L_i V_(i+1)` is consequently `L_(i+1)`.  For the
last successor incidence it is the vertex (1.2).  This proves (1.3).

The new vertex `L_ell` is distinct from every earlier `L_i`: otherwise the
perfect matching would send one lower vertex to both `V_i` and the distinct
owner `V_ell`.  Hence (1.3) is a simple directed path.  Finally, at its
`i`th lower turn the two owners are `V_i,V_(i+1)`, so its upper label is
their union.  \(\square\)

### Corollary 1.2 (tight pivot bank)

The tight split-pivot collar has `ell=3h`, distinct owners, distinct lower
transition colours, and distinct upper transition colours.  Choosing the
predecessor phase and extending it to `M_0` therefore turns its successor
shore into one protected directed path with `3h` globally distinct upper
labels.

For `H` owner/lower-resource-disjoint collars whose upper transition
colours are also distinct across copies, the same proof gives `H`
vertex-disjoint directed protected paths whenever

\[
                              3Hh\le m-1.              \tag{1.6}
\]

The previously used hypothesis `6Hh<=m-2` implies (1.6).  If extra
protected incidence tickets are added—for example, external hosts for the
four deficits of the sparse source—the exact predecessor-phase size,
matching, and cross-colour conditions must include them.  They are not
hidden in `3Hh`.

The native lower-`q1` repair enlarges existing source letters without
changing this owner path, and hence leaves Theorem 1.1 unchanged while
removing those four external tickets.

## 2. Support-first upper representative theorem

Fix the correlated `M_0`, and let `D_(M_0)` be its rooted-link digraph.  A
directed linear forest means an arc set with indegree and outdegree at most
one and no undirected cycle.

### Theorem 2.1 (upper-surjective support contains a protected Catalan forest)

Let `R subseteq D_(M_0)` be a directed linear forest whose upper labels
cover every rank-`m+1` set.  Let `P` be a directed subforest of `R` whose
upper labels are distinct.  Then `R` contains an upper-exact rooted Catalan
forest `Q_0` with

\[
                         P\subseteq Q_0,qquad |Q_0|=U. \tag{2.1}
\]

Its number of components on the full `W`-vertex rooted ground set is

\[
                         W-U=C=\operatorname {Cat}_m. \tag{2.2}
\]

#### Proof

For every upper colour carried by `P`, choose its prescribed edge of `P`.
For every other upper colour, choose any carrying edge of `R`.  Different
upper colours select different arcs, and the labels on `P` are distinct, so
this gives exactly one edge per upper colour and contains all of `P`.

The selected set is a subset of the directed linear forest `R`; hence its
tails and heads are injective and its rooted links are acyclic.  It has `U`
edges on `W` spanning vertices, including isolates, and therefore has
`W-U=C` components.  \(\square\)

This is the exact support-first analogue of the earlier physical-forest
Rado reduction.  Once the redundant support is already a directed linear
forest, representative selection has no residual head or graphic
correlation: one edge of each colour may be chosen independently.

### Theorem 2.2 (exact four-matroid contraction form)

On the arc ground set of `D_(M_0)`, let

* `M_L` be the tail partition matroid;
* `M_H` be the head partition matroid;
* `M_G` be the rooted graphic matroid; and
* `M_U` be the upper-colour partition matroid.

Let `P` be the correlated protected pivot path from Theorem 1.1, of size
`ell`.  Then a protected upper-exact rooted Catalan forest exists if and
only if the four contractions

\[
             M_L/P,\qquad M_H/P,\qquad M_G/P,\qquad M_U/P       \tag{2.3}
\]

have a common independent set of size `U-ell`.

Every contracted matroid separately has enough rank:

\[
 \begin{array}{c|c}
 \text{matroid}&\text{rank on the full residual ground}\\ \hline
 M_L/P&W-\ell\\
 M_H/P&W-\ell\\
 M_G/P&W-1-\ell\\
 M_U/P&U-\ell.
 \end{array}                                                   \tag{2.4}
\]

Thus the remaining obstruction is purely common correlation, not an
individual rank shortage.

#### Proof

The protected path has distinct tails, heads and upper colours and is
graphic-independent, so it is independent in all four matroids.  A set
`X` of residual arcs extends it to `Q_0=P union X` with tail/head
injectivity, acyclicity and at most one edge of each upper colour exactly
when `X` is independent in all four contractions.  If `|Q_0|=U`, upper
independence uses every one of the `U` colour parts exactly once.  This
proves the equivalence.

The two partition ranks lose precisely the `ell` ports consumed by `P`.
The connected rooted graph has graphic rank `W-1`, and contracting the
`ell`-edge forest lowers it by `ell`.  The colour partition has rank `U`
and the protected colours are distinct, giving the last row.  \(\square\)

This is an exact common-basis formulation, but it is a **four**-matroid
intersection.  Edmonds' two-matroid min--max theorem does not apply, and
the generic protected counterexample shows that separate extendibility in
the four rows would not suffice.

## 3. Connector completion after the pivot path is contracted

Let `Q_0` be supplied by Theorem 2.1.  Its components are directed paths,
one of which contains each protected pivot path.  Contract the protected
subpaths only for bookkeeping; every component still has one free outgoing
and one free incoming port.

Choose a collection `mathcal A` of admissible free-port connector arcs
between distinct components, and suppose its component digraph is acyclic.
Let `H_mathcalA` be the bipartite graph on outgoing and incoming copies of
the `C` components.

### Theorem 3.1 (protected one-defect Hall completion)

There are `C-1` compatible connectors in `mathcal A` which join `Q_0` into
one directed Hamilton path if and only if

\[
 |N_{H_\mathcal A}(X)|\ge |X|-1
       \qquad(X\subseteq\operatorname {Comp}(Q_0)).   \tag{3.1}
\]

If some connector paths are protected in advance, contract them first and
apply (3.1) to the residual acyclic reservoir.

#### Proof

Hall deficiency gives a connector matching of size at least `C-1` exactly
under (3.1).  Acyclicity prevents a perfect connector matching, since such
a matching would be a disjoint union of directed cycles.  Thus the matching
has size exactly `C-1`.

Its indegrees and outdegrees are at most one.  An undirected cycle under
these degree bounds would be coherently directed, contradicting the
acyclicity of `mathcal A`.  Hence the selected connector graph is a forest
on `C` vertices with `C-1` edges, and therefore one directed Hamilton path.
The converse is immediate.  \(\square\)

## 4. Exact protected Catalan--pivot certificate

Combining the preceding results gives the following sufficient theorem.

### Theorem 4.1

For the tight pivot bank, suppose one can choose:

1. the predecessor phase `P_0` and a perfect extension `M_0` as in
   Theorem 1.1;
2. an upper-surjective directed linear forest support `R subseteq D_(M_0)`
   containing the successor pivot path `P_1`; and
3. after selecting `Q_0` by Theorem 2.1, an acyclic free-port connector
   reservoir satisfying (3.1).

Then `M_0` together with `Q_0` and the selected `C-1` connectors is an
upper-surjective alternating Hamilton path containing the whole protected
pivot owner path.

#### Proof

Theorem 1.1 gives the correctly phased protected path.  Theorem 2.1 gives
an upper-exact rooted Catalan forest containing it.  Theorem 3.1 joins the
`C` components through unused incoming and outgoing ports into one rooted
Hamilton path.  Expanding `M_0` gives the desired alternating incidence
path, and `Q_0` already supplies every upper colour.  \(\square\)

This theorem accounts jointly for owner incidence, upper colours, tail and
head injectivity, and graphic topology.  It does not assert the existence
of `R` or `mathcal A`, and it does not address exterior residence,
arbitrary-width upper witnesses, the common lower cap, or regeneration.

## 5. Revised frontier

The protected ticket problem now separates cleanly.

* **Solved for the native pivot phase:** the protected successor incidences
  form one directed path, so the generic fixed-`M_0` head/topology
  counterexample is avoided.
* **Solved after support selection:** any upper-surjective directed linear
  forest support contains the required protected upper-exact Catalan forest.
* **Solved after an acyclic connector reservoir is exposed:** the exact
  remaining condition is one-defect Hall.

The owner-layer existence problem has therefore narrowed to the prospective
joint construction

\[
 \boxed{\text{correlated }M_0
        +\text{ protected upper-surjective linear-forest support}
        +\text{ acyclic one-defect-Hall connector reservoir}.}
\]

This is strictly stronger information than the rooted-tail semimatching,
but it remains a conditional certificate rather than an all-`m`
construction.
