# Independent audit of protected resident facet extraction and cascade

Date: 2026-08-01  
Audited files:

* `MATH_THEOREM_RESIDENT_FACET_SOCKET_20260801.md`;
* `MATH_AUDIT_RESIDENT_FACET_SOCKET_BOUNDARY_AND_EXTRACTION_20260801.md`;
* `MATH_THEOREM_RESIDENT_FACET_SOCKET_PROTECTED_EXTRACTION_AND_CASCADE_20260801.md`.

Status: **PASS after scope corrections.**  This is a symbolic audit; no
finite search or numerical experiment is used.

## 1. Boundary and protected Hall

For the compact block \(F_j=U-v_j\), the \(v_j\)-trace is
\(1^j0\,1^{h-j}\).  Applying the exact initial/terminal-run lemma gives
the displayed ages

\[
\ell_{v_j}\ge h+1-j,\qquad \rho_{v_j}\ge j+1
\]

whenever the corresponding piece is nonempty, together with clean incoming
\(v_0\), outgoing \(v_h\), and both outside-\(U\) ages.  The clean rows
cannot be deleted; the \(h=1\) counterexample in the boundary audit is a
legal Johnson chronology.

For a fixed guard-retention state, let \(E_j\) encode physical eligibility
at position \(j\), including the two exterior Johnson joins, and let
\(B_{\mathcal P}\) be the facets forbidden on the facet-disjoint protected
face.  The exact position sets are

\[
                         C_j=(A_j\cap E_j)\setminus B_{\mathcal P}.
\]

Distinct socket facets are precisely an SDR of these sets, so Hall gives

\[
\left|\bigcup_{j\in J}C_j\right|\ge |J|\qquad(\forall J).
\]

This is exact on the stated face.  It is not claimed to be the one-shot
criterion when a protected edge may itself be retained as a guard; exact
general feasibility is the disjunction over the finite guard states.

Because \(U\) is missing, an old edge meets at most one facet of \(U\).
Thus \(p\) protected edges forbid at most \(p\) facets, proving the crude
pre-guard count \({r+1-p\choose h+1}\).

## 2. Extraction and the scalar cascade inequality

The facets selected for a missing \(U\) are independent.  Hence, if \(K\)
is the retained-guard edge set,

\[
q=\sum_{F\in X}\deg(F)-|K|.
\]

There is no hidden factor of two.  In a two-regular factor this is
\(2h+2-|K|\), giving the sharp two-old-guard value \(2h\).

For two linear forests \(F,F'\) on the same owner set, put

\[
D=E(F)-E(F'),\quad B=E(F')-E(F),\quad
\mu=c(F)-c(F')=|B|-|D|.
\]

If \(u(D)\) previously present upper colours lose their complete provider
sets and \(\rho=|D|-u(D)\), then at least

\[
|D|-\rho-(T-H_0)
\]

killed colours lie outside the \(T\) socket targets.  Only
\(|B|-hT=|D|+\mu-hT\) non-socket new edges and \(\kappa\) auxiliary
providers can restore them.  Subtraction gives exactly

\[
|\Gamma_{\rm out}|
\ge\bigl((h-1)T+H_0-\mu-\rho-\kappa\bigr)_+.
\]

Thus \(\kappa+\mu+\rho\ge(h-1)T+H_0\) is necessary for closure.
For one missing target in an upper-injective component-neutral forest the
right side is \(h\).  The raw socket is therefore supercritical for
\(h\ge2\).

The coordinate identity

\[
\mathbf1_{F_i}+\mathbf1_{F_{i+1}}-\mathbf1_{K_i}
=\mathbf1_U
\]

independently gives the collapsed excess \((h-1)\mathbf1_U\).
Compensation using only rank-\((r-1)\) lower holes needs

\[
\left\lceil{(h-1)(r+1)\over r-1}\right\rceil=h
\]

under \(r\ge2h+1\).  This is a lower bound, not a construction.

## 3. Min-max and weighted rows

After deleting unavailable backup objects and contracting frozen
independent choices, the single-matroid private face is exactly Rado's
problem.  Its maximum partial backup is

\[
\nu=\min_{Y\subseteq\Gamma}
\bigl(|\Gamma\setminus Y|+r_M(N(Y))\bigr),
\]

so full backup is equivalent to

\[
                         |Y|\le r_M(N(Y))\qquad(\forall Y).
\]

This does not encode signed palette equalities, exact edge count, or an
intersection of several physical matroids.  Those rows remain explicit in
the theorem.

The weighted cascade is also correctly stated as a state potential.  If
\(\Phi_t\) includes every active, reopened, or newly exposed nonterminal
defect and

\[
\Phi_{t+1}-\Phi_t\le-(1-\theta)w(R_t),
\]

then telescoping gives

\[
\sum_t w(R_t)\le{\Phi_0\over1-\theta}.
\]

A positive lower weight or another well-founded order is needed for a
finite event count, and the terminal family still needs a closing
absorber.

## 4. Prospective provider multiplicity

Let \(n\) allowed facets have total degree at most \(2n\), and suppose
every vulnerable upper colour has providers on at least \(a\) distinct
allowed facets.  There are at most \(\lfloor2n/a\rfloor\) such colours.
If every fixed \(a\)-set is contained in a random guard-legal socket with
probability at most \(\pi_a\), then

\[
\mathbb E|\Gamma_U|
\le\left\lfloor{2n\over a}\right\rfloor\pi_a.
\]

For the uniform \((h+1)\)-subset face,

\[
\pi_a={(h+1)_a\over(n)_a}.
\]

At \(a=2\), expectation is below one whenever

\[
                         h(h+1)<n-1.
\]

This proves a zero **raw upper-child** socket.  It does not close lower,
topology, residence-boundary, or endpoint-cocycle rows.

## 5. Fixed basis and two-stratum interface

For an \(M_0\)-supported socket, endpoint assignments contain no \(RL\)
pattern and are exactly \(L^pR^{h-p}\).  The facet graph
\(\Gamma_U(M_0)\) is simple, has indegree one at every vertex, and each
underlying component is unicyclic.  At \(h=3\), absence of a four-vertex
path is equivalent to a triangle factor, so \(3\nmid(r+1)\) forces a
supported socket.  The \(\Theta(h)\) statement is correctly limited to
abstract triangle-component joins; physical resource-safe joins are not
asserted.

For the paired Kneser bank,

\[
{C\over N}={4(2m-1)\over m(m+1)}.
\]

The raw load bounds prove avoidance of any \(o(N)\) typed footprint in the
even construction.  The present odd-seed relabelling proof needs
\(o(N/m)=o(C)\), unless the seed is planted first.  The balanced hole
normal form has exact maximum \(\operatorname{Sym}(G)\)-orbit density
\(8/(m+1)\), giving the stated \(<(m+1)/8\) lower-footprint avoidance.

Finally, differences of two \(C\)-hole degree vectors have total sum zero,
whereas a private socket contributes \((h-1)\mathbf1_U\).  Thus the
two-stratum bank supplies resource avoidance but not endpoint compensation.
The exact coordinate-layer composition condition is

\[
d_{\mathcal H_0}+(h-1)\mathbf1_U+\gamma
\in\mathfrak D_C(\mathcal A_L\setminus Z_L),
\]

and it forces

\[
                         \sum_x\gamma_x=-(h-1)(r+1).
\]

## 6. Audited scope

The frozen package proves a protected local extraction theorem, a sharp
supercriticality obstruction, a conditional min-max/weighted absorber,
and an \(o(W)\) coexistence interface.  It does not prove that the required
duplicate-provider factor, signed extraction boundary, common-\(M_0\)
completion, upper shadows, or compiler exist simultaneously.  Those are
the exact remaining regenerative rows.
