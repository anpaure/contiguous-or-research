# Exact q=1 rainbow Johnson cycle from the saturating-cycle theorem

Date: 2026-07-26

## 0. Verdict

For (m\ge2), the requested rainbow Hamilton cycle is not an open
expansion problem.  It is exactly the two-level case of the
saturating-cycle theorem for the
Boolean cube.  In the odd-ground notation relevant to the wreath problem,
put

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 N_1=\binom{n}{m-1}=\frac{m}{m+2}W.
\]

There is a simple cycle

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N_1-1},X_{N_1-1},R_0
 \tag{0.1}
\]

in the incidence graph between ranks (m-1) and (m), where the (R_i)
are all the ((m-1))-sets and the (X_i) are (N_1) distinct (m)-sets.
Consequently:

1. (R_0,\ldots,R_{N_1-1}) is a Hamilton cycle of
   (J(n,m-1)) whose union colours (R_i\cup R_{i+1}) are all distinct;
2. (X_0,\ldots,X_{N_1-1}) is a simple cycle of (J(n,m)) whose
   intersection colours are exactly all ((m-1))-sets, once each;
3. the unused middle-owner leave has the exact size
   \[
   W-N_1=\frac{2W}{m+2};                              \tag{0.2}
   \]
4. adjoining every unused owner as a singleton gives exactly
   \[
   1+(W-N_1)                                           \tag{0.3}
   \]
   components.  This is (o(W/H)) whenever (H=o(m)).

For the even-ground formulation in the prompt, replace (n=2m+1) by
(n=2m).  Then

\[
 N_1=\binom{2m}{m-1}=\frac{m}{m+1}W,
 \qquad W-N_1=\frac{W}{m+1}.                          \tag{0.4}
\]

The downstream literal compiler accepts this long cycle at depth one; it
does not require a length-(n) wreath.  The general depth-(H) compiler
accepts arbitrary cycle lengths only under the additional physical
(H)-safety hypothesis.  The saturating-cycle theorem certifies depth one,
not that multidepth hypothesis.

## 1. Published existence theorem

Gregor--Mička--Mütze, *On the central levels problem*, Corollary 2, proves
that the subgraph of (Q_n) induced by any sequence of consecutive levels
has a saturating cycle.  Apply it to levels (m-1,m).  Since

\[
 \binom{n}{m-1}<\binom{n}{m}
\]

for (n=2m) or (n=2m+1), the smaller bipartition class is rank (m-1).
Thus a saturating cycle visits every rank-((m-1)) vertex.  A simple
bipartite cycle alternates, so it also visits the same number (N_1) of
pairwise distinct rank-(m) vertices.  This gives (0.1).

Primary source:

P. Gregor, O. Mička, T. Mütze, *On the central levels problem*, Corollary 2,
<https://tmuetze.de/papers/gmlc2.pdf>.

## 2. Exact equivalence with the rainbow Johnson cycle

Index (0.1) so that

\[
 R_i\subset X_i\supset R_{i+1}.
 \tag{2.1}
\]

The two lower sets in (2.1) are distinct ((m-1))-subsets of the same
(m)-set.  Therefore

\[
 |R_i\cap R_{i+1}|=m-2,
 \qquad
 X_i=R_i\cup R_{i+1}.                                 \tag{2.2}
\]

Hence consecutive (R_i)'s are adjacent in (J(n,m-1)).  They exhaust
that Johnson graph's vertices, so they form a Hamilton cycle.  Its edge
colour at (R_iR_{i+1}) is (X_i), and the (X_i)'s are distinct because
the saturating cycle is simple.  Thus it is rainbow.

Conversely, any Hamilton cycle of (J(n,m-1)) with pairwise distinct union
colours produces (0.1) by inserting the colour (X_i=R_i\cup R_{i+1})
between each adjacent pair.  Thus the two formulations are exactly
equivalent, not merely implications.

## 3. The projected owner cycle and its load

At the lower vertex (R_i), the two incident owners are (X_{i-1}) and
(X_i).  They are distinct (m)-sets containing (R_i), hence

\[
 X_{i-1}\cap X_i=R_i.                                 \tag{3.1}
\]

It follows that

\[
 X_0,X_1,\ldots,X_{N_1-1},X_0                        \tag{3.2}
\]

is a simple cycle in (J(n,m)), and its edge-intersection colours are
precisely the (R_i)'s.  If the core depth-one load is defined by these
intersection colours, then

\[
 \mu_1^{\rm core}(R)=1
 \qquad\text{for every }R\in\binom{[n]}{m-1}.         \tag{3.3}
\]

The leave is exactly the set of rank-(m) vertices not among the (X_i),
so (0.2) and (0.4) follow from the elementary binomial ratios.

There is a further exact abstract depth-one completion on odd ground.  Each
lower set (R) has (m+2) middle supersets, exactly two of which are its
cycle neighbours.  Hence its degree into the omitted-owner family is at
most (m), while every omitted owner has exactly (m) lower facets.  For
every omitted subfamily ({\cal A}), incidence counting gives

\[
 m|{\cal A}|\le m|\partial{\cal A}|.
\]

Hall therefore assigns the omitted owners to distinct lower facets.
Adding those assignments to (3.3) gives the perfectly balanced full load

\[
 \mu_1(R)\in\{1,2\},
 \qquad
 \#\{R:\mu_1(R)=2\}=W-N_1.                           \tag{3.4}
\]

Thus the abstract q=1 balanced-overload is exactly zero.  This Hall
completion has a stronger owner-cycle form.  If an omitted owner (Y) is
assigned to (R_i=X_{i-1}\cap X_i), replace the edge
(X_{i-1}X_i) by

\[
 X_{i-1},Y,X_i.                                       \tag{3.5}
\]

All three middle sets contain (R_i), so both new pairs are Johnson
adjacent and have intersection (R_i).  Since the assignments use distinct
(R_i)'s, performing all subdivisions produces one Hamilton cycle on all
(W) middle owners.  Its intersection-colour multiplicities are exactly
(1) and (2), with value (2) precisely on the assigned colours.

This Hamilton-cycle completion is an abstract q=1 owner object.  At an
inserted vertex (Y), the two consecutive intersection colours are both
(R_i); hence their union is (R_i), not (Y).  Thus the completed cycle
fails the no-return identity used by the standard delay-atom literal
compiler at those vertices.  The original core cycle plus literal appending
of the omitted owners is the cleaner physical q=1 word.

## 4. Exact component and scale ledger

The used-owner cycle is one component.  Treating each omitted owner as an
isolated component partitions all (W) middle owners into

\[
 K=1+(W-N_1)                                           \tag{4.1}
\]

components.  If a path rather than a closed cycle is required, cut one
cycle edge; the nontrivial core is still one path component, so (4.1) is
unchanged.

For odd ground,

\[
 \frac{K}{W/H}
 =\frac{2H}{m+2}+\frac{H}{W}\longrightarrow0
 \qquad(H=o(m)).                                      \tag{4.2}
\]

For even ground the leading term is (H/(m+1)).  In particular the
mesoscopic regime (H=\sqrt m\,\omega(m)) with
\(\omega(m)=o(\sqrt m)\) passes the component/leave scale exactly.

The words "leave" and "component count" should not be conflated:
the uncovered-owner leave is (W-N_1), whereas the completed partition has
(1+(W-N_1)) components.

If only an abstract Johnson owner factor is required, the edge subdivisions
in (3.5) instead give one component and zero owner leave.  This stronger
abstract statement does not remove the literal no-return caveat just noted.

## 5. Literal compiler interface

Let

\[
 B_i:=X_{i-1}\cap X_i=R_i.
\]

Because (B_i) and (B_{i+1}) are distinct facets of (X_i),

\[
 X_i=B_i\cup B_{i+1}.                                 \tag{5.1}
\]

Therefore the cyclic word (B_0,B_1,\ldots,B_{N_1-1}), with the necessary
initial prefix repeated when linearized, literally realizes every lower
target (B_i) and every used middle owner (X_i).  Appending each omitted
middle owner literally costs (W-N_1).  Thus arbitrary cycle length causes
no q=1 obstruction; no length-(n) wreath structure is used in (5.1).

For the two-sided depth-one compiler, the upper transition colours are

\[
 U_i:=X_{i-1}\cup X_i\in\binom{[n]}{m+1}.             \tag{5.2}
\]

The saturating theorem does **not** say that the (U_i)'s are distinct or
cover the whole upper layer.  Likewise, for (q\ge2), a general Johnson
cycle need not satisfy

\[
 \left|\bigcap_{j=0}^{q}X_{i+j}\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^{q}X_{i+j}\right|=m+q.          \tag{5.3}
\]

Those are the physical (H)-safety/geodesicity conditions required by the
factor-blind multidepth compiler.  Consequently the exact interface verdict
is:

* **yes** for the q=1 lower-shadow owner-cycle and its (o(W/H)) leave;
* **yes** for arbitrary cycle lengths once physical (H)-safety is supplied;
* **no automatic implication** from the saturating theorem to the upper
  q=1 ledger, deeper flags, a length-(n) wreath decomposition, or the
  constant-one theorem.
