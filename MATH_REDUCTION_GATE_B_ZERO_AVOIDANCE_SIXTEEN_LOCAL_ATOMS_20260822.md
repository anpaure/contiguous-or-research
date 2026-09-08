# Gate B: zero avoidance reduces to sixteen local boundary atoms

**Date:** 2026-08-22

**Status.**  The two roots of the full-exposure boundary profile are at
distance three, not macroscopic distance, in the punctured boundary graph.
This rules out treating every term beyond `W_2` as a small error.  It also
leaves a finite leading object: after the standard linear relabelling, all
order-`D_M/r` boundary-profile mass comes from sixteen four-vertex local
atoms.  Ten are isolated two-edge matchings; six are a matching corrected
by the unique three-edge path on the same four vertices.

Uniformly in the harmonic level, shore, and boundary shift,

\[
 \boxed{
 \omega_{Z_s}(t)=L_{s,j}(t)+O(D_M/r^2),}                     \tag{0.1}
\]

where `L_(s,j)(t)` is the explicit signed profile of those sixteen atoms
after deleting any atom which uses one of the two punctured edges.  The
local term has scale at most `O(D_M/r)`.  Proving a polynomial avoidance
residual now reduces to a finite matrix-valued Venn--Hahn calculation for
this local atom bank, plus stability under the error in (0.1).

The local bank itself obeys the exact three-profile identity

\[
 \boxed{L_{s,j}(0)+L_{s,j}(\ell)=L_{s,j}(3)}                  \tag{0.2}
\]

for `r>=6`, both shores, and every `2<=j<=r-2`.  Hence its best constant
residual is at least `1/(3b)`.  The remote `O(D_M/r^2)` dressing is the
only part which breaks this identity.

## 1. Correct boundary-graph geometry

In the original cut coordinates a central target is an edge of cyclic
length `r` or `r-1`.  Multiplication by `-2` modulo `b=2r+1` sends

\[
                         r\longmapsto1,qquad r-1\longmapsto3. \tag{1.1}
\]

Thus the boundary graph becomes

\[
                         B_r=\operatorname {Cay}
 (\mathbb Z_b,\{\pm1,\pm3\}).                                \tag{1.2}
\]

The two event cuts are separated by `k=r-2` before relabelling, but

\[
                         -2(r-2)\equiv5\pmod{2r+1}.           \tag{1.3}
\]

Hence their images may be fixed as

\[
                         p=0,\qquad q=5.                     \tag{1.4}
\]

They have graph distance three: `5=3+3-1`, while no sum of two elements
of `{+/-1,+/-3}` is `5` once `r>=6`.  Therefore a three-blocker path can
join the two event roots with only four incident cuts.  Its boundary
codegree has the same `r^(2-4)` order as a two-blocker matching.  This is
the precise obstruction to an absolute `W_2` perturbation argument.

## 2. The sixteen four-vertex atoms

Work first in the full, unpunctured graph on the integer line with edges
of length one or three; for `r>=6` the radius-three neighbourhood below
does not wrap around the cycle.  A blocker set which covers `0,5` and has
exactly four incident vertices has one of the following sixteen vertex
sets:

\[
\begin{array}{rrrr}
(-3,0,2,5),&(-3,0,4,5),&(-3,0,5,6),&(-3,0,5,8),\\
(-1,0,2,5),&(-1,0,4,5),&(-1,0,5,6),&(-1,0,5,8),\\
(0,1,2,5),&(0,1,4,5),&(0,1,5,6),&(0,1,5,8),\\
(0,2,3,5),&(0,3,4,5),&(0,3,5,6),&(0,3,5,8).
\end{array}                                                   \tag{2.1}
\]

Ten induced graphs consist only of a two-edge matching, one edge incident
to each root.  The other six vertex sets are

\[
 (-1,0,2,5),\ (0,1,2,5),\ (0,1,4,5),
 \ (0,2,3,5),\ (0,3,4,5),\ (0,3,5,6),                       \tag{2.2}
\]

and their induced graph is a three-edge path.  On each such path there are
exactly two edge subsets with all four incident vertices: the endpoint
matching `M` and the full path `P`.  Inclusion--exclusion groups their
contribution as

\[
                         \deg(S,M)-\deg(S,P).                \tag{2.3}
\]

This coefficient is nonnegative: it counts configurations which contain
the two matching targets but not the connecting target.  Thus the local
bank consists of ten matching atoms and six positive
`matching-without-connector` atoms.  There are sixteen positive atoms but
twenty-two factorial blocker terms.

In the punctured graph, the same template is translated to the event
roots and any term using either omitted edge is deleted.  Only a bounded
set of translations sees the puncture.

### Lemma 2.1 (local three-profile identity)

For `r>=6`, (0.2) holds.

#### Proof

First restore the two omitted edges and form the complete local atom bank.
Translation invariance makes its signed profile independent of the event
shift; call it `Omega_s`.  In every one of the sixteen atoms, exactly one
edge supplies each event root.  This is immediate for a matching; in each
of the six paths the two event roots are the path endpoints and the third
edge is the connector.

Classify each atom by whether its two supplier edges use their start or end
boundary at the event roots, giving complete signed totals
`F_SS,F_SE,F_ES,F_EE`.  Reflection through the two event roots preserves
the complete local bank, the Venn degree, the blocker parity sign, and the
orientation-free harmonic product, while interchanging start and end at
both roots.  Thus `F_SS=F_EE`.

At event shift zero, the two omitted edges are exactly the two start
suppliers at the left root, so the puncture correction is
`C_s(0)=F_SS+F_SE`.  At shift `ell`, the same puncture is at the right root
and `C_s(ell)=F_SS+F_ES`.  No local atom contains both omitted edges:
every event root has a unique supplier.  At shift three, neither omitted
edge lies in a four-vertex atom covering the event roots, so
`L_s(3)=Omega_s`.  Consequently

\[
 C_s(0)+C_s(\ell)=2F_{SS}+F_{SE}+F_{ES}=\Omega_s,
\]

and `L=Omega-C` proves (0.2).  For prediction errors
`e_t=1-xL_(r,j)(t)-yL_(r-1,j)(t)`, one has
`e_0+e_ell-e_3=1`; Cauchy--Schwarz gives squared error at least `1/3` on
these three states, hence mean residual at least `1/(3b)`. `square`

## 3. Why every other blocker set loses one power

For a blocker set `J`, let `V(J)` be its incident boundary cuts.  The
signed root-set transposition at an event cut shows that its boundary
profile vanishes unless

\[
                         \{p,q\}\subseteq V(J).              \tag{3.1}
\]

The rooted-current sum is bounded by

\[
 \left|\sum_S\deg(S,J)H_{s,j}(S)\right|\le2r\deg(J),         \tag{3.2}
\]

because every configuration has `2r` targets on a fixed shore.  Use the
proved boundary-codegree inequality

\[
                         \deg(J)\le C_0^{|J|}D_M
 r^{2-|V(J)|}.                                               \tag{3.3}
\]

The sets in Section 2 have four incident cuts and contribute at most
`O(D_M/r)` to (3.2).  Every other component meeting both roots has at least
five incident cuts, hence pays one more factor `1/r`.  If the roots lie in
separate components, the same conclusion holds unless both components are
single edges; any enlargement adds a vertex.  Remote components have total
unrooted activity `O(1/r)` by the boundary-polymer estimate, so attaching
them to a four-vertex rooted atom also loses one factor.

The bounded-degree exploration and exponential-formula sum therefore give

\[
 \sum_{\substack{J:\{p,q\}\subseteq V(J)\\|V(J)|\ge5}}
 \deg(J)=O(D_M/r^3).                                         \tag{3.4}
\]

Multiplication by the `2r` in (3.2) proves the error `O(D_M/r^2)` in
(0.1).  The same calculation on the sixteen four-vertex atoms gives the
upper scale `O(D_M/r)` for `L`.

In particular, (0.1)--(0.2) give the approximate exact-exposure identity

\[
 |\omega_{Z_s}(0)+\omega_{Z_s}(\ell)-\omega_{Z_s}(3)|
 \le {C D_M\over r^2}.                                       \tag{3.5}
\]

## 4. Exact remaining local calculation

The expansion (0.1) explains both existing observations:

1. the `W_2` three-state identity need not survive full exposure, because
   the six path corrections are leading-order rather than perturbative;
2. the full-exposure residual can nevertheless remain of order `1/r`,
   because only a bounded local defect bank distinguishes the mostly
   translation-invariant boundary profile from a constant.

The next theorem needed is matrix-valued stability of the local affine gap
under the remote dressing in (0.1).  The scalar local gap itself is already
closed by Lemma 2.1, but absolute columnwise error is insufficient when the
two shore columns are ill-conditioned.  Each local atom and each first
remote decoration is evaluated by the same exact Venn factorial and signed
injection polynomial already used for `W_2`.  No growing family of blocker
topologies remains at leading order.
