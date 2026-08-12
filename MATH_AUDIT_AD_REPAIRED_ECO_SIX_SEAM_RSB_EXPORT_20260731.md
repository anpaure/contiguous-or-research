# Audit of the repaired-ECO six-seam RSB export

Date: 2026-07-31  
Audited theorem:
`MATH_THEOREM_AD_REPAIRED_ECO_SIX_SEAM_RSB_EXPORT_AND_CUBE_GUARDS_20260731.md`  
Verdict: **PASS**, with all common-connector, common-core, fixed-skeleton,
and halo-separation hypotheses load-bearing

## 1. Six-edge physical lift

Use the old incidence matching

\[
 L_aU_{ca},\quad L_bU_{ab},\quad L_cU_{bc}
\]

and the new matching

\[
 L_aU_{ab},\quad L_bU_{bc},\quad L_cU_{ca}.
\]

At a marked `L_x`, the physical turn edge joins its fixed external
rank-`m` neighbour `H+x+d` to its current hexagon `U`-neighbour.  This gives
exactly the three `B`-rail rows (1.6), (1.8).  At a marked `U_xy`, the
physical turn edge joins `infinity+(H-e+x+y)` to the current
`infinity+L` neighbour, giving (1.7), (1.9).

All six incidence ports are marked.  Therefore none belongs to a residual
unmarked path, so the residual cross matching is literally unchanged.
Every other marked turn has the same two neighbours.  This proves that no
physical edge outside the displayed six-edge block changes.

The old and new `B` blocks pair the common vertex set

\[
 \{H+a+d,H+b+d,H+c+d,U_{ab},U_{bc},U_{ca}\},
\]

and the old and new `A` blocks pair the common vertex set

\[
 \{\infty+H-e+a+b,\infty+H-e+b+c,\infty+H-e+c+a,
   \infty+L_a,\infty+L_b,\infty+L_c\}.
\]

The two rails are disjoint.  Distinctness of `a,b,c,d` and `e in H`
prevents any identification inside a rail.  Thus both blocks are matchings
on the same twelve vertices.  Direct intersection/union gives exactly

\[
 \begin{array}{c|c|c}
 &\text{lower colours}&\text{upper colours}\\ \hline
 {\cal B}&
 \{H+a,H+b,H+c\}&
 \{H+d+a+b,H+d+b+c,H+d+c+a\}\\
 {\cal A}&
 \{\infty+H-e+a,\infty+H-e+b,\infty+H-e+c\}&
 \{\infty+H+a+b,\infty+H+b+c,\infty+H+c+a\}.
 \end{array}
\]

Hence the exact count `six old/six new`, degree-vector invariance, endpoint
invariance, and rank-one neutrality all pass.

## 2. Trace obstruction

For `m=2`, the middle-levels order

\[
 0,01,1,12,2,02
\]

with marks at `0` and `12` has upper turn `012`, lower turn `empty`, and
alternating marked shore types.  Its trace is `100100`.  The marked turns
give physical edges

\[
                         02-01,qquad \infty1-\infty2,
\]

and the residual paths give

\[
                         01-\infty1,qquad02-\infty2.
\]

They form the four-cycle stated in the theorem.  Thus a joint alternating
SDR plus residual matching does not imply a linear physical lift.  The
additional exact row is exclusion of the binary cycle face.  A retained
literal `0^4` is sufficient because it forces one zero-run to have length
at least four.

The protected-breaker induction is correctly scoped to strict
component-faithful merges.  It would be false for an operation allowed to
split a component or delete a breaker edge.

## 3. Connector and collar constants

If the connector set is common, it is disjoint from both physical forests.
The final Hamilton cycles therefore differ in exactly the six forest edges.
With connector sets `C_0,C_1`, every old-only edge lies in the six-edge
forest block or `C_0 minus C_1`, proving the upper bound `6+c`.  Equality is
asserted only for a common connector, as required.

Deleting six pairwise vertex-disjoint edges from a Hamilton cycle gives six
common path fragments, each of order at least two.  Therefore

\[
 b_q=\sum_{i=1}^6\min(q,n_i)\le6q,qquad b_2=12.
\]

The reversal-invariant internal-window cancellation proves the signed
intersection and union formulas.  It does not apply without change to an
orientation-sensitive compiler skeleton; the theorem separately requires
the occurrence-exact transport map there.

At erosion depth `delta`, an erosion letter uses `delta` owner seams, a
wall uses `delta+1`, and a width-`h` cell uses `delta+h-1`.  Multiplying by
the exact ECO seam count gives exposed dependency-boundary banks of size at
most

\[
 6\delta,\qquad6(\delta+1),\qquad6(\delta+h-1),
\]

as valid sharp-support upper bounds.  Actual signatures can agree on some
exposed starts, so these count possibly changed right vertices, not
necessarily strict changes and not changed target incidences.

## 4. Depth-two data separator

With common predecessor `R=H+d+p`, replacing

\[
 (H+a+d,H+a+b)\quad\hbox{by}\quad(H+a+d,H+a+c)
\]

changes the union of the crossing triple from `H+a+b+d+p` to
`H+a+c+d+p`.  The atom ports, common labels, owner data, and complete
rank-one palette ledger are unchanged.  Varying `p` varies the depth-two
delta.  Hence external rays or an equivalent window-value quotient are
genuinely additional data.  The theorem correctly scopes this as a local
data separator, not a globally unique-hole construction.

## 5. Negative-part cube formulas

Under `R`-separation, every affected flag window and every changed named
cell belongs to exactly one atom bank.  Consequently

\[
 \mu_{\cal U}=\mu_\varnothing+\sum_{t\in\cal U}\Delta_t
\]

target by target.  The minimum over all subsets selects exactly the
negative `Delta_t`, proving (6.6).

For compiler Hall, disjoint right-vertex banks give

\[
 |N_{\cal U}(X)|-|X|
 =\sigma_0(X)+\sum_{t\in\cal U}\delta_t(X).
\]

Again the minimum over all subsets selects exactly the negative terms.
Taking this minimum independently for every Hall shore `X` is legitimate
because the assertion quantifies over **all** pairs `(X,U)`.  This proves
the necessity and sufficiency of (6.9).

Neither formula survives a dependency window meeting two atom blocks: a
mixed Boolean coefficient can occur.  The common-core/halo hypothesis is
therefore substantive, not cosmetic.

## 6. Terminal theorem cross-audit

Sections 2 and 6 of
`MATH_THEOREM_CATALAN_TERMINAL_DECORATION_AND_RSB_JOINT_TRANSITION_20260731.md`
are consistent with this theorem.

* The residence collar monoid is exact when

  \[
  \omega_x(P)=1\Longleftrightarrow x\in P_i\text{ for every owner }P_i.
  \]

  The source has been clarified to state this explicitly.  If `omega`
  meant merely “occurs somewhere,” its concatenation formulas would be
  false.
* The arbitrary-interval `Tot/Pre/Suf/Deck` formulas partition intervals
  into left-internal, right-internal, and seam-crossing classes and are
  exact.
* A terminal trace truth bit is not compositional; the named protected span
  or exact trace automaton is required.
* The depth-two transparent-hex separator in Section 6.1 is the one-rail
  projection of the exact six-edge block above.

## 7. Scope boundary

The theorem proves a downstream transition calculus.  It does not prove:

1. an all-dimension controlled repair;
2. a collision-free owner-aligned ECO bank;
3. a common connector Hamiltonizing every cube state;
4. `R`-separated boundary rays;
5. residence-safe interior rethreading; or
6. an integral common-cap compiler.

At repaired project `m=5`, the central singleton is positive, while its
intact-path physical lift has exactly 32 internal length-two positive runs.
Thus the central result and the downstream RSB obstruction are consistent.

No computation, SAT solve, or web result is used in this audit.
