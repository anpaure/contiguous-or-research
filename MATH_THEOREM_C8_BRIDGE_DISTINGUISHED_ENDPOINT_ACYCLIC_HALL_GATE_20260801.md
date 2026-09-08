# Acyclic Hall with the double-crossrail bridge as a prescribed path endpoint

Date: 2026-08-01  
Lane: bridge-only Catalan connector  
Status: exact distinguished-endpoint Hall theorem and exact joint selector
target.  No all-dimensional acyclic-reservoir construction is claimed.

## 0. Outcome

The bridge-only reduction in
`MATH_THEOREM_C8_DOUBLE_CROSSRAIL_PROTECTED_HAMILTON_EXTENSION_GATE_20260801.md`
leaves

\[
                         q=C-2d+1                       \tag{0.1}
\]

rooted-link components after the upper representatives and the `2d-1`
forced repeated-upper connector occurrences are installed.  All protected
bridge links lie in one distinguished component `K_*`.

The generic acyclic connector theorem asks only for a matching of size
`q-1`, equivalently one-defect Hall.  That is not quite enough for the
literal bridge source.  Its left clipping is real: to retain the displayed
source without a new left factorization, the bridge component must be the
**first** component of the final Hamilton path.  Thus the unique unmatched
incoming port has to be the incoming port of `K_*`.

On an acyclic reservoir the exact condition is ordinary Hall after deleting
that one incoming port:

\[
 \boxed{
 |N^-_{\mathcal A}(Y)|\ge |Y|
 \quad\text{for every }Y\subseteq
       \operatorname {Comp}(F)\setminus\{K_*\}.}       \tag{0.2}
\]

Here `N^-` is the set of available outgoing component ports which enter a
member of `Y`.  Equation (0.2), not unrooted one-defect Hall, is the exact
bridge-compatible connector cut.

## 1. Distinguished-source acyclic Hall

Let `mathcal C` be a set of `q` directed path components.  Every component
has one free outgoing port and one free incoming port.  Let `mathcal A` be
an admissible connector reservoir whose component digraph is acyclic, and
fix `K_* in mathcal C`.

Make the connector bipartite graph with one outgoing and one incoming copy
of each component.  Delete the incoming copy of `K_*`.

### Theorem 1.1 (rooted one-defect Hall)

The reservoir contains a directed Hamilton path starting at `K_*` if and
only if (0.2) holds.

#### Proof

After deleting the incoming copy of `K_*`, the right shore has `q-1`
vertices.  Hall's theorem says that (0.2) is exactly the existence of a
matching saturating those `q-1` incoming ports.

The selected arcs have indegree and outdegree at most one.  They have no
directed cycle because the whole reservoir is acyclic; under the degree
bounds an undirected cycle would be coherently directed, so there is no
undirected cycle either.  Thus the selected graph is a directed path forest.
It has `q` vertices and `q-1` edges, hence one component.  Every component
other than `K_*` has its incoming port matched, while `K_*` does not, so the
unique path starts at `K_*`.

Conversely, the arcs of a Hamilton path starting at `K_*` match every other
incoming port and give (0.2). \(\square\)

### Terminal version

Deleting the **outgoing** copy of `K_*` instead gives the dual criterion

\[
 |N^+_{\mathcal A}(X)|\ge |X|
 \qquad(X\subseteq\mathcal C\setminus\{K_*\}),         \tag{1.1}
\]

which is equivalent to a Hamilton path ending at `K_*`.

### Why generic one-defect Hall is weaker

The inequalities

\[
 |N(X)|\ge|X|-1
\]

produce some source and some terminal.  They do not prescribe where the
one missing incoming or outgoing port lies.  A directed path reservoir whose
source is not `K_*` is the immediate counterexample.  Therefore the source
condition cannot be omitted merely because the total connector deficiency
is already one.

## 2. Application to the bridge-only bank

There are two proof-safe protected versions.  For the bare bridge put

\[
 (p_\star,s_\star)=(2d+3,4),
\]

and for the right-continued bridge of Section 5 put

\[
 (p_\star,s_\star)=(3d+3,d+4).
\]

In both cases

\[
                         p_\star-s_\star=2d-1.         \tag{2.0}
\]

Fix a componentwise alternating phase, a compatible perfect shore `M0`, a
representative subbank `A0` of the `s_star` protected upper values, and a
set `X` satisfying the contracted common-independence condition

\[
 X\in
 \mathsf M_L/P_1\cap\mathsf M_O/P_1
 \cap\mathsf M_G/P_1\cap\mathsf M_U/A_0,
 \qquad |X|=U-s_\star.                                \tag{2.1}
\]

Put

\[
                         F=P_1\cup X.                  \tag{2.2}
\]

The full protected path `P1` is one directed path, so it lies in one
component `K_*` of `F`.  The edge count gives exactly `q=C-2d+1`
components.  Therefore:

### Corollary 2.1 (bridge-rooted protected connector)

If there is a guard-admissible acyclic connector reservoir `mathcal A` on
the components of `F` satisfying (0.2), then selecting the Hall matching
gives exactly `C-2d` new connector incidences.  Together with `M0`, it forms
an upper-exact alternating Hamilton path containing the complete protected
bridge, with the bridge component first.

The connector count is

\[
 q-1=C-2d,                                             \tag{2.3}
\]

as required by the repeated-upper occurrence ledger.

This corollary is owner-layer exact.  It assumes (2.1); it does not infer
the other-head/graphic common extension from the rooted-tail Hall theorem.

### Theorem 2.2 (support-first form absorbs the repeated occurrences)

Fix the correlated predecessor `M0`.  Suppose instead that one directly
constructs an upper-surjective directed linear forest

\[
                         R\subseteq D_{M_0}             \tag{2.4}
\]

containing the whole protected bridge shore `P1`.  Let `q_R` be its number
of spanning components and let `K_*` be the component containing `P1`.
If an admissible acyclic reservoir on these components satisfies the rooted
Hall cuts (0.2), then `R` extends to an upper-surjective directed Hamilton
path starting with `K_*`.

#### Proof

The forest has `W-q_R` edges.  Theorem 1.1 selects `q_R-1` compatible
connectors forming one path from `K_*`; their union with `R` has `W-1`
edges and remains a directed linear forest, hence is a Hamilton path.  Since
no edge of `R` is deleted, every upper value and every protected occurrence
survives. \(\square\)

Selecting one occurrence of each upper colour inside `R`, choosing one
protected occurrence for each protected value, gives an upper-exact rooted
Catalan forest `Q0 subseteq R`.  The remaining edges `R-Q0` are already
acyclic connector occurrences.  Thus Theorem 2.2 is exactly the
support-first version of the contracted criterion: it replaces the
four-matroid common-extension step by the single constructive target

\[
 \boxed{\text{upper-surjective directed linear-forest support containing
 the repeated bridge path.}}                           \tag{2.5}

For a minimum-size support containing only the forced `2d-1` duplicate
occurrences, `q_R=C-2d+1`, recovering Corollary 2.1.  Extra support edges
reduce the residual component count one-for-one as long as acyclicity and
port injectivity are retained.

## 3. A concrete acyclic-reservoir target

For any injective potential

\[
                         \omega:\mathcal C\to\mathbb R
\]

with `omega(K_*)` minimum, retain only admissible connector arcs

\[
 \mathcal A_\omega={K\to K':\omega(K)<\omega(K')\}.  \tag{3.1}
\]

This reservoir is acyclic and has no incoming arc to `K_*`.  Thus the full
connector theorem for this face is reduced to the explicit cut family

\[
 \boxed{
 |N^-_{\mathcal A_\omega}(Y)|\ge|Y|
 \quad(Y\subseteq\mathcal C\setminus\{K_*\}).}         \tag{3.2}
\]

A convenient Boolean choice is a generic coordinate-weight potential on
the free incoming root of each component.  No claim is made that this or an
arbitrary potential satisfies (3.2); equation (3.2) is the exact expansion
statement to prove while choosing `M0,Q0` and the bridge phase jointly.

The average free-port degree is only constant order in a Catalan forest, so
a generic density argument is not enough.  The required expansion must be
built into the correlated selector.

## 4. Exact quantifier order

The `m=3` protected counterexample in
`MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md`
shows that an arbitrary fixed `M0` can fail even for three clean protected
arcs.  The small protected-factor theorem supplies some compatible `M0`,
but gives no reason for its free-port cuts to satisfy (3.2).

For the native bridge one can at least choose the protected phase
prospectively.  Orient the bridge as displayed, put every predecessor
incidence in `P0`, and extend that matching to a perfect `M0`.  The sharp
middle-shadow Hall surplus guarantees the extension for the bare and
right-continued bridges under

\[
                         2d+3\le m-1,
 \qquad                  3d+3\le m-1,                 \tag{4.0}
\]

respectively.  For every such extension the successor incidences contract
to one directed path in the required orientation.  Hence the arbitrary
fixed-ticket obstruction is absent from the protected bridge itself.  What
remains joint is the upper-surjective support/common extension and the
rooted Hall reservoir.

The proof-safe all-dimensional target is therefore the one joint
existential statement

\[
 \boxed{
 \begin{gathered}
 \exists\text{ bridge phase},\ M_0\supseteq P_0,\ A_0,\ X,\omega:\\
 X\text{ satisfies (2.1)},\quad
 \mathcal A_\omega\text{ is guard-admissible},\quad
 \text{and (3.2) holds.}
 \end{gathered}}                                      \tag{4.1}
\]

Theorem 1.1 then supplies the Hamilton connector automatically.  Choosing
`M0` first by an arbitrary extension and attempting to repair its port graph
afterward is not justified.

## 5. Residence and source-address scope

The literal right continuation from the protected-extension note replaces
the bridge's terminal maximal source letter by `{f_(d+1)}` and appends the
owner collar

\[
 C_t=E-\{f_1,\ldots,f_t\}+\{x_1,\ldots,x_t\}.
\]

It preserves `D^d`, both cross banks, and all old filler residence inside
the protected component.  Its fresh `x_s` runs are clipped at the far end.

There are therefore two different endpoint conventions.

1. Put the original bridge at the global source.  Its left clipping is
   literal, and Theorem 1.1 must make `K_*` the first contracted component.
   The right continuation exports a nested fresh-coordinate guard into the
   next component.
2. Put the continued bridge at the global terminal.  The fresh-coordinate
   runs are globally clipped, but the original left maximal-source bank is
   no longer an internal cap automatically; it needs a new incoming source
   factorization.

The first convention is the current proof-safe one, because it preserves
the authenticated left source literally.  Accordingly (0.2) is the relevant
connector cut.  Connector admissibility out of `K_*` must include the
exported fresh-coordinate guard and every source/cap condition; an ordinary
owner incidence is not enough.

Neither convention transports the exterior lower compiler.  That remains a
separate background/common-cap row after the owner connector is selected.

## 6. Current frontier

The bridge-specific Catalan connector is now reduced to two exact statements:

1. the common extension (2.1), whose upper/tail projection is already
   solved but whose other-head/graphic correlation is open;
2. the distinguished-source acyclic Hall cuts (3.2), with the outgoing
   bridge guard included among the structural zeros.

No arbitrary-ticket extension theorem can replace these rows.  A successful
construction must choose the perfect phase, upper representatives, component
potential and guard-compatible port reservoir together.
