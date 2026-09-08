# Protected two-extension fibres and the literal PBBS fragment-braid interface

Date: 2026-07-31.

Status: unconditional interface and guarded-connectivity theorems.  The
existence of a dimension-uniform PBBS guard/absorber satisfying the final
connected colored-DFA conditions is not proved.

## 1. Incidence and physical forms

Put \(n=2r-1\), and set

\[
 {\cal C}=\binom{[n]}{r-1},\qquad {\cal V}=\binom{[n]}r,
\]

and let \(I\) be their inclusion graph.  A balanced two-extension factor is
a simple incidence set \(M\subseteq E(I)\) with

\[
                 d_M(C)=d_M(V)=2
       \quad(C\in{\cal C},\ V\in{\cal V}).               \tag{1.1}
\]

The two selected owners over \(C\) are \(C+a,C+b\); contracting \(C\)
therefore gives the Johnson edge

\[
             e_M(C)=\{C+a,C+b\},\qquad L(e_M(C))=C.       \tag{1.2}
\]

Write \(J(M)\) for this contracted physical graph.

Thus an incidence factor and a lower-rainbow Johnson 2-factor are the same
object.  An incidence hexagon changes one selected incidence at each of
three colour rows.  In the physical graph it deletes at most three Johnson
edges and installs at most three Johnson edges, row by row with exactly the
same lower colours.

This last phrase is important.  A hexagon is not merely an unlabelled
three-edge switch: its three row labels are the literal lower compiler
colours of its three replacement seams.

## 2. Paired guards

A **paired incidence guard** is a set \(K\subseteq M\) which is a union of
complete incidence pairs: whenever it contains an incidence of the physical
edge \(e_M(C)\), it contains both incidences joining \(C\) to the endpoints
of that edge.  Write

\[
 {\cal F}(K)=\{N\subseteq E(I):d_N\equiv2,\ K\subseteq N\}. \tag{2.1}
\]

The following are two sufficient literal meanings of protection.

* For each required upper target \(Z\), choose one interval witness in the
  contracted factor and put both incidences of every physical edge in its
  span into \(K\).  Every factor in \({\cal F}(K)\) retains this interval.
* For a desired minimum positive-run length \(h\), suppose that, for every
  coordinate \(x\) and every owner \(V\ni x\), the component of the guarded
  physical graph on \(x\)-containing owners which contains \(V\) has at
  least \(h\) vertices.  Then every factor in \({\cal F}(K)\) has all
  positive \(x\)-runs of length at least \(h\).

The second condition is a sufficient corridor certificate, not a claim that
every resident PBBS factor possesses a sparse guard of this form.  The exact
endpoint-DFA test in Section 4 can be strictly weaker, but it is a condition
on a completed order and is not hereditary throughout \({\cal F}(K)\).
Indeed, if \(N\in{\cal F}(K)\), then the positive-run component of
\(J(N)\) containing \(V\ni x\) contains the entire guarded
\(x\)-component containing \(V\), and hence has at least \(h\) vertices.
This is the complete quantifier justification for the corridor claim.

### Theorem 2.1 (fixed-guard protected fibre connectivity)

If \({\cal F}(K)\ne\varnothing\), then any two factors in \({\cal F}(K)\)
are connected by a sequence of alternating-circuit toggles, every one of
which remains in \({\cal F}(K)\).  Consequently every upper witness and
every residence corridor certified by \(K\) survives at every intermediate
factor.

#### Proof

Let \(M,N\in{\cal F}(K)\), colour \(M\setminus N\) red and
\(N\setminus M\) blue.  At each incidence vertex the red and blue degrees
are equal, because both full degrees are two.  Pair red and blue half-edges
locally.  Following the pairings decomposes the symmetric difference into
edge-disjoint alternating circuits.  No circuit contains an edge of \(K\),
since \(K\subseteq M\cap N\).  Toggling the circuits one at a time preserves
all degrees, simplicity, and \(K\).  The two guard conclusions follow from
their definitions. \(\square\)

This is a genuine neutral-switch theorem: once one fixed literal guard is
declared, no additional monotone-connectivity lemma is needed inside its
fibre.  It does not say that the component count is monotone along the
route, and it does not replace the alternating circuits by primitive
hexagons.

### Proposition 2.2 (exact residual Hall inequalities)

Put

\[
 b_C=2-d_K(C),\qquad b_V=2-d_K(V),\qquad H=I\setminus K.
\]

For a vertex family \(S\), write \(b(S)\) for the sum of its displayed
demands; subscripts only indicate the shore.

Then \({\cal F}(K)\ne\varnothing\) if and only if

\[
 b_{\cal C}(A)\le b_{\cal V}(B)+e_H(A,{\cal V}\setminus B) \tag{2.2}
\]

for every \(A\subseteq{\cal C}\), \(B\subseteq{\cal V}\), together with
\(\sum_Cb_C=\sum_Vb_V\).  The quantifiers are over all two-shore subset
pairs, not merely one-shore Hall sets.  For a proposed union of guards,
degree feasibility \(d_K\le2\) is checked first; if it fails, its fibre is
empty before (2.2) is invoked.

#### Proof

Use the network with capacities \(b_C\) from the source to \(C\), unit
capacity on every residual incidence, and capacity \(b_V\) from \(V\) to
the sink.  The cut whose source shore contains \(A\) and \(B\) has capacity

\[
 b_{\cal C}({\cal C}\setminus A)+e_H(A,{\cal V}\setminus B)+b_{\cal V}(B).
\]

The max-flow/min-cut theorem gives (2.2), and integrality gives a simple
residual incidence selection. \(\square\)

These are the correct guarded Hall inequalities.  An uncoloured or
untyped endpoint matching, or the binary cycle-space theorem, does not imply
them after guard incidences have been removed.

### Proposition 2.3 (exact fixed-guard mobility test)

For \(M\in{\cal F}(K)\), the fibre \({\cal F}(K)\) contains a factor other
than \(M\) if and only if \(I\setminus K\) contains a nonempty
\(M\)-alternating circuit.

#### Proof

Toggling such a circuit gives another factor containing \(K\).  Conversely,
if \(N\ne M\) also contains \(K\), the red--blue decomposition in the proof
of Theorem 2.1 supplies a nonempty alternating circuit in
\(M\triangle N\subseteq I\setminus K\). \(\square\)

Thus a selected all-depth guard can fail for the sharpest possible reason:
it may hit every alternating circuit.  In that case binary generation by
hexagons is irrelevant; the literal protected fibre is a singleton.

## 3. From a factor switch to a literal fragment braid

Let \(M,N\) be two balanced factors.  In the contracted physical graphs,
retain precisely the physical edges common to both factors.  Their
noncyclic components are the maximal path fragments.  A cyclic common
component is already a sealed component of both factors and has no port.
Every edge in \(M\setminus N\) is a cut and every edge in
\(N\setminus M\) is a seam.

### Theorem 3.1 (exact factor-to-braid transfer)

The preceding construction has the following properties.

1. Every new seam is Johnson.  If it is indexed by row \(C\), its
   intersection colour is literally \(C\).
2. For every changed row, the old and new physical edges have the same
   lower colour.  Hence lower-rainbow restitution is rowwise, not merely a
   global count.
3. The common physical path fragments, joined by the new seams, together
   with any sealed common cycles, are exactly the components of the
   contracted graph of \(N\).  Thus connectivity of the abstract endpoint
   is exactly connectivity of the literal macro braid; in particular a
   nontrivial connected endpoint has no sealed common cycle.
4. Any selected old interval whose complete edge span is common to both
   factors remains a contiguous interval (possibly reversed) in \(N\).
5. All other new interval values are exactly those given by the complete
   suffix--full-fragment--prefix formula of the fragment-braid theorem.

For one incidence hexagon the braid has at most three cuts and three seams.
For an alternating circuit meeting \(s\) distinct colour rows it has at
most \(s\) cuts and \(s\) seams.

#### Proof

At a row \(C\), every selected owner has the form \(C+a\).  Two distinct
selected owners therefore differ in exactly two coordinates, have
intersection \(C\), and form a Johnson edge.  Changing either or both
selected incidences at that row changes the physical edge but not its row
label, proving 1--2.

Every owner has degree two in \(N\).  Removing its new edges leaves the
maximal common paths; reinstalling those edges joins exactly the ports which
are adjacent in \(N\).  This proves 3.  If every edge of an old witness is
common, its internal degree-two vertices retain their two witness edges, so
the witness remains a path segment.  Finally every interval crossing one or
more new seams has a unique first and last fragment and hence is a suffix,
all intervening fragments in full, and a prefix.  This proves 4--5. \(\square\)

Theorem 3.1 is the exact dictionary sought in the PBBS lane.  It also shows
why an abstract balanced switch can be installed literally without a
fixed-exterior monodromy claim: the endpoint is itself a new physical
factor.  What is not automatic is that the endpoint retains the chosen
upper witnesses, residence, or one-component topology.

## 4. The endpoint form of the fragment CSP

Suppose a paired guard contracts to a spanning linear forest
\(P_1,\ldots,P_c\).  Its degree-deficient owner occurrences are its **port
tokens**; a singleton fragment has two port tokens at the same owner.  The
unused colour rows have residual demand two.  A literal seam assignment is
therefore the integral residual incidence problem of Proposition 2.2:
each unused colour chooses two distinct compatible port owners, and each
port token is used once.

In the seam-arc projection, this becomes all of the following, not just an
endpoint matching.

1. **Ports:** every nonexternal port token is used exactly once.
2. **Colours:** each seam is labelled by the intersection of its endpoints,
   and the required unused rows are used with their prescribed
   multiplicities.  Suppressing row vertices turns this into a partition-
   matroid constraint.
3. **Upper witnesses:** every target has a retained guarded span or one
   explicitly selected suffix--prefix (or multi-fragment) provider.
4. **Residence:** the product endpoint automaton accepts the complete
   oriented component order.
5. **Connectivity:** the selected macro graph is one cycle, or, after the
   deliberate one-colour opening, one path.  Degree feasibility alone may
   leave subtours.

For the current `010/0110` guard, use states

\[
                 \epsilon,0,01,011,\bot
\]

tracking the longest suffix which is a prefix of a forbidden word.  The
nonfailure transitions are

\[
\begin{array}{c|cc}
 &0&1\\ \hline
\epsilon&0&\epsilon\\
0&0&01\\
01&\bot&011\\
011&\bot&\epsilon.
\end{array}                                             \tag{4.1}
\]

An oriented fragment induces one partial transformation of these states for
each coordinate.  The whole braid is residence-safe exactly when the
corresponding transformations compose without reaching \(\bot\).

Pairwise seam safety is not this condition.  A one-vertex middle fragment
can make `0|1|0`, and a two-one middle fragment can make `0|11|0`, although
neither adjacent pair alone contains a forbidden word.  This explains the
observed PBBS phenomenon in which pure Johnson endpoint matching is
feasible while the run-state-restricted endpoint problem is infeasible: the
lost object is a matching in the product of the port graph with (4.1), not
global Hamiltonicity.

That negative conclusion is catalogue-scoped.  It excludes the frozen
ports, cuts, and orientations used to build that endpoint graph; a reroot,
a larger alternating circuit, or a net-protected guard change can create a
different product graph.

### Corollary 4.1 (component-neutral linear ledger)

If the guarded physical forest spans \(W\) owners and has \(c\) components,
then it contains \(W-c\) internal lower colours.  Joining it into one path
uses \(c-1\) pairwise-distinct seam colours, for a total of

\[
                         (W-c)+(c-1)=W-1.               \tag{4.2}
\]

Thus component subdivision is exactly neutral and leaves the single forced
linear lower-colour hole.  In the odd-to-odd Pascal U insertion this is the
Catalan identity

\[
 (N-c)+2c+(J-1-c)=N+J-1,
       \qquad W=N+J,\quad J=W-N=\operatorname{Cat}_r.   \tag{4.3}
\]

Equation (4.2) is only a slot identity until the colour-row constraints in
item 2 above are satisfied.

## 5. Hexagons versus protected circuits

The binary cycle space of \(I\) is generated by incidence hexagons.  This
does not imply that a given alternating circuit admits an ordering of
hexagons such that every intermediate hexagon is alternating in the current
factor.  It implies even less after deleting a guard.

Call the residual fibre **conformally hexagonal** if, for every
\(M\in{\cal F}(K)\) and every \(M\)-alternating circuit \(Q\subseteq
I\setminus K\), there is a sequence of currently alternating,
guard-disjoint incidence hexagons carrying \(M\) to \(M\triangle Q\).
Under this extra hypothesis, Theorem 2.1 can be strengthened from
alternating circuits to literal three-seam hexagon braids.  Without it,
Theorem 2.1 is still exact with compound circuits, and binary hexagon
generation supplies no monotone proof.

This is the first precise obstruction: algebraic generation is not
nonnegative protected generation.

## 6. Guard changing and the absorber nerve

One fixed guard may freeze too much of PBBS to permit a connected or
resident endpoint.  An exact sufficient way to change guards, without ever
relying on destruction and simultaneous recreation of a certificate, is an
absorber.

Let \({\mathscr K}\) be any catalogue of paired guards, each certifying its
declared upper witnesses and, when residence is declared protected at that
stage, a hereditary corridor certificate.  Discard guards with empty
fibres.  Form the **absorber graph** \(\Gamma\) on \({\mathscr K}\) by

\[
 K\sim K'\quad\Longleftrightarrow\quad
             {\cal F}(K\cup K')\ne\varnothing.          \tag{6.1}
\]

Call a circuit step **catalogue-guard-preserving** if both of its endpoints
belong to one common fibre \({\cal F}(K)\) and its support avoids that
\(K\).

### Theorem 6.1 (guard-nerve connectivity)

The protected union

\[
                    \bigcup_{K\in{\mathscr K}}{\cal F}(K) \tag{6.2}
\]

is connected by catalogue-guard-preserving alternating circuits on every
connected component of \(\Gamma\).  In the graph containing only
catalogue-guard-preserving steps, its connected components are exactly the
unions indexed by the connected components of \(\Gamma\).

#### Proof

Each individual fibre is connected by Theorem 2.1.  If \(K\sim K'\), a
factor containing \(K\cup K'\) lies in both fibres and is a literal absorber
which simultaneously carries the old and new certificates.  Concatenating
within-fibre circuit paths along a path of \(\Gamma\) proves the first
claim.  Conversely, each allowed step has both endpoints in one guard fibre.
Changing the witnessing fibre along a route requires a factor lying in both
successive fibres, hence an edge of \(\Gamma\). \(\square\)

This graph-connectivity statement preserves one common target predicate
along a guard-chain only when every guard on that chain certifies that same
predicate.  If guards certify different target families, Theorem 6.1 still
connects the degree fibres but does not assert target monotonicity at the
handoff.

A compound switch may instead destroy the last old witness and create a new
one in the same toggle.  Such a net-protected transfer need not pass through
a common-guard absorber and is outside Theorem 6.1.  Thus disconnectedness
of \(\Gamma\) obstructs the absorber architecture, not every possible
protected compound circuit.  In particular, Theorem 6.1 makes no converse
claim about the full graph whose vertices are merely protected at their
endpoints; an H-certificate to E-certificate switch with no common
certificate fibre is allowed in that larger graph.

### Proposition 6.2 (the broader converse is false on one \(C_{12}\))

In \(I(5,2)\), let \(H\) be the incidence cycle

\[
\begin{split}
12-123-13-134-34-345-35-135-15-125-25-235\\
-23-234-24-245-45-145-14-124-12,
\end{split}                                             \tag{6.3}
\]

and let \(E=E_1\cup E_2\), where

\[
\begin{aligned}
E_1={}&12-123-13-135-35-345-45-245-24-124-12,\\
E_2={}&14-145-15-125-25-235-23-234-34-134-14.
\end{aligned}                                           \tag{6.4}
\]

Both are balanced factors, and every rank-four physical union colour has
load two in each.  Their symmetric difference is the single alternating
circuit

\[
13-134-14-124-24-234-34-345-45-145-15-135-13,           \tag{6.5}
\]

with the edges alternating between \(H\) and \(E\).
Nevertheless, if

\[
 K_H=\{13\!-\!123,13\!-\!134\},\qquad
 K_E=\{13\!-\!123,13\!-\!135\},                         \tag{6.6}
\]

then \({\cal F}(K_H\cup K_E)=\varnothing\), because the union has degree
three at row \(13\).  Thus the net-protected \(C_{12}\) takes \(H\) to
\(E\), while the two displayed certificate fibres have no common absorber.

For a full common-predicate version, extend \(K_H\) by the complete
physical incidence pairs at rows

\[
                         15,\ 14,\ 35,\ 23,
\]

and extend \(K_E\) by those at rows

\[
                         34,\ 15,\ 14,\ 45.             \tag{6.7}
\]

The resulting guards \(\widehat K_H,\widehat K_E\) each retain one physical
provider for every rank-four target, while their union is still infeasible
because it contains \(K_H\cup K_E\).

#### Proof

The displayed lists directly give degree two on both shores.  Contracting
the ten rank-two rows in (6.3) gives the five rank-four unions
\(1234,1235,1245,1345,2345\), each twice; the same check on (6.4) gives the
same loads.  Cancelling their common incidences leaves exactly (6.5).
Finally (6.6) has the three distinct incidences from row \(13\) to
\(123,134,135\), which no degree-two factor can contain.  In \(H\), rows
\(13,15,14,35,23\) supply respectively
\(1234,1235,1245,1345,2345\); in \(E\), rows
\(34,13,15,14,45\) supply those same five targets in that order.
This verifies the full guards in (6.7). \(\square\)

Proposition 6.2 is not a PBBS counterexample.  It audits the logical scope:
the absorber nerve is an exact theorem for catalogue-guard-preserving
transport, while net witness replacement can cross between its components.

Proposition 2.2 applied to \(K\cup K'\) gives exact, checkable Hall
inequalities for every proposed absorber.  Thus, within the fixed-guard/
absorber architecture, failure is localized more sharply than “PBBS has
many components.”  It occurs through at least one of:

* a residual Hall cut (2.2) for every candidate common guard;
* failure of the colored endpoint rows after contracting the guard;
* failure of the protected seam-provider/span rows for an unguarded target;
* a product-DFA cut for patterns 010 and 0110;
* a subtour/connectivity obstruction among otherwise feasible seams; or
* disconnection of the absorber graph (6.1), within the guard-preserving
  absorber architecture.

## 7. Conditional PBBS zero-defect transfer theorem

The preceding results package one exact sufficient PBBS statement.

### Theorem 7.1 (conditional protected PBBS transfer)

Fix an odd dimension and a PBBS all-depth factor \(M_0\).  Suppose there is
a chain of paired guards

\[
                         K_0,K_1,\ldots,K_t             \tag{7.1}
\]

such that:

1. the selected target family is the **entire required lower and upper
   shadow universe**, and every \(K_i\) carries one literal witness for
   every member of that common family; for some \(j\le t\), every \(K_i\)
   with \(i\ge j\) also carries a
   hereditary residence-corridor certificate (take \(j=0\) when residence
   is required throughout);
2. \({\cal F}(K_0)\) contains \(M_0\), and
   \({\cal F}(K_i\cup K_{i+1})\ne\varnothing\) for every \(i\);
3. \({\cal F}(K_t)\) contains an endpoint whose contracted graph, after the
   declared opening of one unguarded residual edge/colour, is one path;
4. the endpoint's unused-row/port assignment is colour-exact, every upper
   target not guarded internally has a selected protected seam provider, and
   the full residence-DFA and staircase replay accepts;
5. its boundary hole and remaining lower targets satisfy an independently
   proved exact common-cap compiler Hall theorem, and the resulting literal
   post-opening word passes complete replay.

Then the endpoint is a literal zero-defect carrier/compiler certificate and
gives \(\nu(k)=B(k)\).  Moreover the carrier can be reached from PBBS by a
sequence of protected compound alternating-circuit switches.  If every
residual fibre in (7.1) is conformally hexagonal, the compound switches may
be replaced by protected incidence-hexagon switches.

#### Proof

Theorems 2.1 and 6.1 transport through the guard chain without losing a
selected upper witness, and without losing residence from stage \(j\)
onward.  Theorem 3.1 turns the endpoint into the literal fragment braid
described in 4.  Hypotheses 3--4 give one
physical protected chronology with exact owner and lower-colour ledgers;
hypothesis 5 imports exactly the remaining integral compiler theorem and
literal replay; no common-\(Q\) integrality is proved in this note.  The
deadline lower bound then forces equality. \(\square\)

The theorem is conditional only in the explicitly listed existence clauses.
In particular it does not infer a connected protected endpoint from binary
hexagon generation, marginal upper completeness, or pairwise-safe endpoint
matching.

## 8. A sharp sufficient remaining PBBS lemma

PBBS already supplies the all-depth starting factor.  The fragment-braid
CSP already supplies the exact suffix/prefix witness and residence labels.
The genuinely new all-dimensional statement needed for a zero-defect proof
can therefore be stated without ambiguity:

> **Protected absorber-and-routing lemma.**  The PBBS guard catalogue has a
> connected absorber subgraph leading to a guard whose residual incidence
> b-matching contains a colour-exact, product-DFA-accepted, one-path
> endpoint, and whose protected seam services and common-cap lists satisfy
> their simultaneous Hall inequalities.

The local K17 endpoint-matching failure shows why “degree-two fibres are
connected” is not this lemma.  The exact factor correspondence shows equally
why global Hamiltonicity is not the first obstruction.  The first missing
object is a compatible guarded residual factor; only after it exists do
subtour elimination and compiler Hall become relevant.

No unconditional PBBS absorber theorem is claimed here.
