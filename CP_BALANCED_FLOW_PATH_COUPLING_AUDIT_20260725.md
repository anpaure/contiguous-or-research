# Covering-prefix balance versus bridge-one chronology

Date: 2026-07-25

This note audits and sharpens the covering-prefix gate \((\mathrm{CP}_A)\)
from `ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md`.  It uses no SCD
constraint.

## 0. Verdict

The balanced-full-flag theorem and the ordered-Hall path-cover theorem in
that note are correct.  Before chronology is imposed, the lower and upper
flags can be constructed independently by two integral lower-bounded flows
and combined owner by owner into valid radius-\(H\) useful states.

They do not combine with the bridge-one path cover as one ordinary network
flow or one matroid-base selection.  A bridge-one transition couples the
two flags by an exact queue law: the lower deletion queue shifts, and the
coordinate leaving its front becomes the first upper addition at the next
owner.  Consequently every \(p\)-path solution satisfies the new necessary
stationarity bounds

\[
 \boxed{
 \|A_i-A_{i+1}\|_1\le2p\quad(1\le i<H),
 \qquad
 \|A_1-B_1\|_1\le2p.}
 \tag{0.1}
\]

Here \(A_i(a)\) counts owners whose \(i\)-th lower deletion is coordinate
\(a\), and \(B_i(a)\) is the analogous upper-addition count.  These
constraints are absent from the two independent balanced-flow polytopes.

There is an exact mixed integer formulation: choose one full state in every
middle-owner fibre, impose lower and upper target capacities, and choose a
split-copy matching of bridge-one arcs in one total order.  Its optimum is
the covering-prefix path count.  The formulation is a list-constrained
matching with flow side constraints, rather than a network matrix.

Thus the surviving constructive problem is not target balance or path
cover separately.  It is an integral **queue-aligned two-flow theorem**:
choose the two balanced nested flows so that their ownerwise pairing obeys
the shift laws on all but \(o(W/H)\) path boundaries.

## 1. Audit of the balanced-flow construction

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
 \qquad \lambda_q={W\over N_q}.
\]

In the lower inclusion network, a depth-\(q\) set has size \(m-q\) and
splits its incoming flow equally among its \(m-q\) facets.  A fixed
depth-\((q+1)\) set has \(m+q+1\) parents.  Hence its throughput is

\[
 \lambda_q{m+q+1\over m-q}
 ={W\over N_{q+1}}=\lambda_{q+1}.
 \tag{1.1}
\]

The node-capacity intervals

\[
 [\lfloor\lambda_q\rfloor,\lceil\lambda_q\rceil]
 \tag{1.2}
\]

are integral and contain this fractional throughput.  The ordinary
lower-bounded-circulation reduction therefore gives an integral flow, and
its acyclic decomposition gives one nested deletion path from every middle
owner.  The same construction on complements gives one nested upper path
from every owner.

Write their ordered labels as

\[
 \alpha(X)=(\alpha_1(X),\ldots,\alpha_H(X)),
 \qquad
 \beta(X)=(\beta_1(X),\ldots,\beta_H(X)),
 \tag{1.3}
\]

where \(\alpha_i(X)\in X\) are distinct and
\(\beta_i(X)\in X^c\) are distinct.  The combined useful state is

\[
 \omega_X=
 \bigl(
 X-\{\alpha_1,\ldots,\alpha_H\};
 \alpha_H,\ldots,\alpha_1,
 \beta_1,\ldots,\beta_H;
 [2m]-(X\cup\{\beta_1,\ldots,\beta_H\})
 \bigr).
 \tag{1.4}
\]

Its rank-\((m-q)\) prefix is

\[
 X-\{\alpha_1,\ldots,\alpha_q\},
\]

and its rank-\((m+q)\) prefix is

\[
 X\cup\{\beta_1,\ldots,\beta_q\}.
\]

Thus independent lower and upper flows really do combine into a valid
state.  Since \(\lambda_q\ge1\), every target receives at least one unit;
the construction has zero holes.  This verifies Theorem 4.8.

## 2. Exact queue law for a bridge-one edge

Abbreviate

\[
 a_i=\alpha_i(X),\qquad b_i=\beta_i(X),
\]

and put

\[
 L=X-\{a_1,ldots,a_H\},qquad
 R=[2m]-(X\cup\{b_1,ldots,b_H\}).
\]

Let \(\omega_X\to\omega_Y\) be a bridge-one edge between distinct
owners.  The complete bridge classification gives exactly two cases.

### Rotor case

For some \(x\in L\) and \(y\in R\),

\[
 \begin{aligned}
 Y&=X-a_1+y,\\
 \alpha(Y)&=(a_2,a_3,\ldots,a_H,x),\\
 \beta(Y)&=(a_1,b_1,b_2,\ldots,b_{H-1}).
 \end{aligned}
 \tag{2.1}
\]

### Promotion case

For some \(x\in L\) and \(1\le t\le H\),

\[
 \begin{aligned}
 Y&=X-a_1+b_t,\\
 \alpha(Y)&=(a_2,a_3,\ldots,a_H,x),\\
 \beta(Y)&=(a_1,b_1,\ldots,b_{t-1},b_{t+1},\ldots,b_H).
 \end{aligned}
 \tag{2.2}
\]

The promotion alternatives using one of the first \(H\) singleton blocks
leave the middle owner unchanged and therefore do not give an edge between
distinct owner fibres.

Equations (2.1)--(2.2) are obtained simply by substituting (1.4) into the
three bridge-one forms.  In both cases the universal identities are

\[
 \boxed{
 \alpha_i(Y)=\alpha_{i+1}(X)\quad(1\le i<H),
 \qquad
 \beta_1(Y)=\alpha_1(X).}
 \tag{2.3}
\]

This is the exact coupling absent from the independent flows.

There is also a triangular flag recurrence.  For \(q<H\),

\[
 L_q(Y)=L_{q+1}(X)\cup\{Y\setminus X\}.
 \tag{2.4}
\]

In the rotor case,

\[
 U_q(Y)=U_{q-1}(X)\cup\{Y\setminus X\}
 \quad(q\ge1),
 \tag{2.5}
\]

while promotion deletes one selected member of the old upper queue.  Thus
even though the lower and upper target loads can be balanced separately,
their chronological refinements cannot be selected separately.

## 3. Positional stationarity forced by a short path cover

For a selected covering-prefix transversal define coordinate histograms

\[
 A_i(a)=\#\{X:\alpha_i(X)=a\},
 \qquad
 B_i(a)=\#\{X:\beta_i(X)=a\}.
 \tag{3.1}
\]

### Theorem 3.1 (queue-stationarity obstruction)

If the selected useful states have a directed bridge-one path cover with
\(p\) paths, then (0.1) holds.  More generally,

\[
 \|A_i-A_j\|_1\le2p|i-j|
 \qquad(1\le i,j\le H).
 \tag{3.2}
\]

#### Proof

There are \(W-p\) internal path arcs.  Along every such arc, (2.3) pairs
the value of \(\alpha_{i+1}\) at its source with the value of
\(\alpha_i\) at its target.  Delete the \(p\) terminal owners from the
first multiset and the \(p\) initial owners from the second.  The remaining
coordinate multisets are identical.  Two histograms which become equal
after deleting at most \(p\) entries from each have \(\ell^1\)-distance at
most \(2p\).  This proves the first family in (0.1).  The same argument
with \(\alpha_1\) at the source and \(\beta_1\) at the target proves the
second.  Summing adjacent inequalities gives (3.2). \(\square\)

The histograms are visible directly in the balanced target loads.  If
\(\mu_q^-(T)\) and \(\mu_q^+(U)\) are the lower and upper loads, then for
every coordinate \(a\),

\[
 \sum_{i=1}^qA_i(a)
 ={W\over2}-
 \sum_{\substack{T\in\binom{[2m]}{m-q}\\a\in T}}
 \mu_q^-(T),
 \tag{3.3}
\]

\[
 \sum_{i=1}^qB_i(a)
 =
 \sum_{\substack{U\in\binom{[2m]}{m+q}\\a\in U}}
 \mu_q^+(U)-{W\over2}.
 \tag{3.4}
\]

Indeed, the left side of (3.3) counts the owners which contain \(a\) but
whose depth-\(q\) lower flag does not; (3.4) is the dual statement.

Floor/ceiling balance controls every individual target load, but it does
not prescribe the point marginals on the right of (3.3)--(3.4).  Therefore
Theorem 4.8 does not imply (0.1).  A proof of \((\mathrm{CP}_A)\) must
choose the balanced quotas and their nested realizations with these
positional correlations built in.

For the desired scale \(p=o(W/H)\), (0.1) requires

\[
 \|A_i-A_{i+1}\|_1=o(W/H),
 \qquad
 \|A_1-B_1\|_1=o(W/H),
 \tag{3.5}
\]

simultaneously through a Gaussian number of queue positions.  These are
strictly stronger than rankwise floor/ceiling balance.

## 4. The exact combined integer program

Let \(\Omega_H(X)\) be the set of full useful states centred at \(X\), and
let

\[
 c_q=\left\lfloor{W\over N_q}\right\rfloor.
\]

Fix a total order \(\prec\) on the middle owners.  Let
\({\cal A}_\prec\) be the bridge-one arcs \(\omega\to\omega'\) whose
owners satisfy \(X(\omega)\prec X(\omega')\).  Use binary variables
\(x_\omega\) and \(y_{\omega\omega'}\).  The exact balanced version of the
covering-prefix optimization is

\[
 \sum_{\omega\in\Omega_H(X)}x_\omega=1
 \quad(X\in\tbinom{[2m]}m),
 \tag{4.1}
\]

\[
 c_q\le
 \sum_{\omega:L_q(\omega)=T}x_\omega
 \le c_q+1,
 \tag{4.2}
\]

with the analogous upper inequalities, and

\[
 \sum_{\omega':\omega\omega'\in{\cal A}_\prec}
 y_{\omega\omega'}\le x_\omega,
 \qquad
 \sum_{\omega':\omega'\omega\in{\cal A}_\prec}
 y_{\omega'\omega}\le x_\omega.
 \tag{4.3}
\]

The objective is

\[
 \boxed{p=W-\sum_{\omega\omega'}y_{\omega\omega'}.}
 \tag{4.4}
\]

Because the owner order makes the selected arc graph acyclic, (4.3) is a
split matching and (4.4) is exactly its path count.  Minimizing (4.4) over
all orders gives the exact balanced subclass of \((\mathrm{CP}_A)\).
Dropping the upper bounds in (4.2), and retaining only load at least one,
gives the full covering-prefix gate.

For fixed \(x\), (4.3) is an ordinary integral bipartite matching.  With
the path variables removed, (4.1)--(4.2) have an integral feasible point by
the two independent flow constructions.  Their union is not thereby one
network matrix: the same \(x_\omega\) must support both its incoming and
outgoing arc and simultaneously encodes two entire nested paths.

## 5. Why the separate flow bases are not one matroid

Even one Boolean inclusion layer already rules out the inference that its
integral matching choices are bases of a single matroid on the chosen
incidence edges.  Inside a three-coordinate Boolean interval, the incidence
graph between

\[
 \{1\},\{2\},\{3\}
 \quad\hbox{and}\quad
 \{1,2\},\{2,3\},\{1,3\}
\]

is a six-cycle.  It has the two perfect matchings

\[
 M_0=\{1\!-!12,,2\!-!23,,3\!-!13\},
\]

\[
 M_1=\{1\!-!13,,2\!-!12,,3\!-!23\}.
\]

For an edge \(e\in M_0\setminus M_1\), no single
\(f\in M_1\setminus M_0\) makes \(M_0-e+f\) a perfect matching.  Hence
the base-exchange axiom fails.  This gadget embeds at consecutive ranks of
every sufficiently large Boolean lattice by fixing the other coordinates.

Perfect matchings are, of course, intersections of two partition matroids
and have an integral bipartite-matching polytope.  The point is narrower
but decisive: the lower balanced-flow choices cannot be treated as bases of
one matroid and then combined with the upper choices and bridge arcs by one
more routine matroid intersection.  The bridge queue equalities (2.3) add a
third, ownerwise consistency relation.

This does not rule out a more elaborate extended formulation.  It rules
out the currently tempting deduction

\[
 \text{integral lower flow}+\text{integral upper flow}
 +\text{integral path matching}
 \Longrightarrow\text{one integral combined network}.
\]

## 6. A quantitative first-band consequence

At depth one, a balanced lower load takes values one or two, with total
duplicate excess

\[
 W-N_1={W\over m+1}.
 \tag{6.1}
\]

The same holds above.  From a bridge-one path forest with \(W-p\) arcs,
delete at most \(W-N_1\) arcs to make all lower intersection colours
distinct and at most another \(W-N_1\) arcs to make all upper union colours
distinct.  The remaining graph is a two-sided-rainbow Johnson linear
forest with at least

\[
 \boxed{
 W-p-{2W\over m+1}}
 \tag{6.2}
\]

edges.

#### Proof

For every bridge-one arc \(X\to Y\), (2.3) at the first position gives

\[
 L_1(X)=X\cap Y,
 \qquad U_1(Y)=X\cup Y.
\]

At a fixed lower colour, keep at most one outgoing arc among all sources
having that colour.  The number removed is at most the total lower load
excess \(W-N_1\).  Do the same for upper colours.  Deletion preserves a
linear forest and proves (6.2). \(\square\)

Thus \((\mathrm{CP}_A)\) in its balanced form would imply a quantitative
two-sided-rainbow forest with deficit \(o(W/H)+O(W/m)\).  At
\(H=\Theta(\sqrt m)\), this is \(o(W/\sqrt m)\), stronger than the
currently recorded unquantified \(o(W)\) forest error.  This is a necessary
first-band milestone, not a sufficient higher-depth theorem.

## 7. Exact remaining theorem

The clean combined target is now:

> **Queue-aligned balanced-flow theorem.**  For every fixed \(A>0\), with
> \(H=\lceil A\sqrt m\rceil\), choose one integral lower balanced flow and
> one integral upper balanced flow, pair their paths at each common middle
> owner as in (1.4), and obtain useful states whose bridge-one graph has a
> path cover with \(o_A(W/H)\) components.

Theorem 4.8 proves both integral flows exist.  The ordered-Hall formula
proves the path cover exists once the states are fixed, but with no useful
component bound.  Theorem 3.1 gives a new family of compulsory cut
inequalities for any attempted coupling.  No network-flow or matroid theorem
currently proves their simultaneous satisfaction, and no contradiction to
their Boolean-specific feasibility is proved here.

