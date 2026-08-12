# Independent audit: minimal common-guard linkage contraction

Date: 2026-07-31  
Audited note:
MATH_THEOREM_K_MINIMAL_COMMON_GUARD_LINKAGE_STATE_AND_EXPLICIT_CONTRACTION_20260731.md

## 1. Verdict

The strict-gammoid/Rado recurrence and its constants are correct under the
declared fixed-guard, fixed-orientation, literal-cell hypotheses.  The
sharp contraction summary is

\[
 \Gamma_\eta=\max_{A\subseteq B}(\eta|A|-r(A)),
\tag{1.1}
\]

and

\[
 |U|\le\lambda V+b_0,\quad \Gamma_\eta\le\gamma
 \quad\Longrightarrow\quad
 V'\le(1-\eta)\lambda V+(1-\eta)b_0+\gamma.
\tag{1.2}
\]

Thus

\[
 \rho=(1-\eta)\lambda,\qquad
 \beta=(1-\eta)b_0+\gamma.
\tag{1.3}
\]

The theorem is conditional.  It does not construct the required
Boolean/Pascal bank and does not apply to the replay-invalid K17 zipper.

## 2. Exact-state audit

For one fixed exposed set \(U\), one common guard \(Q\), one transported
matching \(M_0\), and one fixed free-cell bank \(F\), the only numerical
quantity needed for the final defect is \(r(U)\):

\[
                         V'=|U|-r(U).
\]

When a later context may expose arbitrary named subsets \(A\subseteq B\),
the whole rank function \(r(A)\) is necessary and sufficient.  This is a
coarsest-context statement, not a claim about the minimum number of encoded
bits.

If sinks vary, one must at least retain two-sided named linkability.  If
later gluing prescribes source--sink pairings or rejects directed cycles,
even all unpaired two-sided ranks can be insufficient; the full oriented
pairing-resolved relation is the proof-safe state.

The guard word, transported matching, alternating orientation, exposed
source set, and free sink bank must belong to the same final state.  Separate
minimizers cannot be combined.

## 3. Rado audit

Let each exposed source \(u\) have source-private entrance menu \(P_u\), and
let \(r_{\mathcal M}\) be the strict-gammoid rank on the port ground set.
Rado's partial-transversal formula is

\[
 q=\min_{X\subseteq U}
 \left(
 |U|-|X|+
 r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \right).
\tag{3.1}
\]

Therefore

\[
 |U|-q
 =\max_{X\subseteq U}
 \left(
 |X|-r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \right).
\tag{3.2}
\]

This verifies both the weakest residual-\(D\) cut condition and the
hereditary \((\eta,\gamma)\) sufficient condition.  The source-private menu
copies are necessary: two nominal menu entries which are the same physical
port cannot be treated as independent representatives.

## 4. Min-cut audit

In the node-split unit-capacity presentation, max-flow/min-cut gives

\[
 r(A)=\min_P\bigl(|A\setminus P|+\operatorname{cap}(P)\bigr).
\tag{4.1}
\]

For fixed \(P\), a selected source in \(P\) contributes \(\eta\) to
\(\eta|A|-r(A)\), while a source outside \(P\) contributes
\(\eta-1\le0\).  Hence

\[
 \Gamma_\eta
 =\max_P\bigl(\eta|B\cap P|-\operatorname{cap}(P)\bigr).
\tag{4.2}
\]

Deleting \(q\) unit resources reduces every cut capacity by at most \(q\),
so

\[
                         \Gamma'_\eta\le\Gamma_\eta+q.
\tag{4.3}
\]

This is stability, not contraction.  A bounded deletion/addition halo has
only additive effect on the pressure.

## 5. Constant audit

The theorem defines \(\lambda\) as the **total** pre-repair exposure
coefficient:

\[
                         |U|\le\lambda V+b_0.
\]

With this convention (1.3) is correct.  If instead one writes additional
exchange exposure as \(u_{\rm new}\le\alpha V+b_0\), then total exposure is
at most \((1+\alpha)V+b_0\), and the same formula becomes

\[
 \rho=(1-\eta)(1+\alpha),\qquad
 \beta=(1-\eta)b_0+\gamma.
\]

The typed refinement is also correct.  Exact healing of newly created
sources and \(\eta_0\)-fraction repair of inherited sources gives
\(\rho=1-\eta_0,\beta=\gamma\).

## 6. Sharp no-gos

### 6.1 Guard graphs cannot be united

Take targets \(a,b\), cells \(x,y\).  Under guard zero, only \(a\) is
adjacent to \(x,y\); under guard one, only \(b\) is.  The union of the two
graphs has a perfect matching, while every single guard has defect one.
Thus the correct quantifiers are

\[
                         \exists Q\ \forall X,
\]

not \(\forall X\,\exists Q\).

### 6.2 Bounded support cannot give a uniform fraction

If all changed incidences are covered by \(h\) right-cell identities, then

\[
                         |\nu(H')-\nu(H)|\le h.
\]

Thus \(V'\ge V-h\), and a fixed
\(V'\le\rho V+\beta\), \(\rho<1\), fails for
\(V>(h+\beta)/(1-\rho)\).  Likewise, if every augmenting path crosses a
boundary separator of size \(p\), then \(r(U)\le p\).  Positive-fraction
repair of unbounded defect needs \(\Omega(V)\) independent linkage capacity
or a global reset.

### 6.3 A fixed-sink rank does not remember pairings

Identity and crossed two-path networks can have the same unpaired rank for
every source subset against a common two-sink bank while realizing different
full pairings.  A later context which reserves one sink or closes one
pairing into a directed cycle distinguishes them.  This confirms the scope
split between the fixed-sink rank state and the general pairing-resolved
state.

## 7. Physical scope

Every graph right vertex must be a literal physical cell, and every path
must lie in one final common-guard graph.  Quotient providers are not
independent sinks unless their physical occurrences are disjoint.  Replay,
residence, upper shadows, sockets, and prepins are upstream gates.

The authenticated K17 OPTIMAL28 zipper fails those upstream tests:
2392 short-run defects, 3568 failed replay rows, and upper holes
1900/911/128.  No value of its common-cap \(V_*\), \(r\), or
\(\Gamma_\eta\) is asserted.

