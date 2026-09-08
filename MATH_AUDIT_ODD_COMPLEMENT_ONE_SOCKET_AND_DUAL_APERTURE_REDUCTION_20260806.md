# Audit: complement one-socket and dual-aperture reduction

**Date:** 2026-08-06  
**Primary theorem:**
`MATH_THEOREM_ODD_COMPLEMENT_ONE_SOCKET_AND_DUAL_APERTURE_REDUCTION_20260806.md`  
**Method:** symbolic replay of every endpoint, scan-row and
last-intersection identity; no computation or search  
**Verdict:** PASS as an exact reduction.  The bounded directed collar
remains explicitly unproved.

## 1. Complement orbit audit

The equation \(2-u=u\) in \(\{0,1,2\}^m\) forces every coordinate to
equal one.  Since complement is an involution, the remaining orbits are
two-cycles.  Therefore the odd-orbit count is exactly one without any
rotation.  Literal complement fixes the value one at coordinate zero, so
it preserves the aperture hyperplane.

## 2. Last-intersection splice audit

For one representative \(u\) of each nonfixed complement pair, retain
\(P_u\) and reroute the distinct path \(P_{\mathsf c u}\) to
\(b(u)\).  The used source indices are disjoint and exhaust all sources
except \(\mathbf1\).  Under the theorem's explicit avoidance hypotheses,
the splice has terminals

\[
 \{A(u),b(u):u\in I\}\dot\cup\{A(\mathbf1)\}.
\]

Thus there is exactly one socket.  No deterministic route in the opposite
orientation of the same complement pair is required.

## 3. Aperture boundary audit, including direct branches

The deterministic activation used in the proved aperture construction
chooses only internal pairs/connectors.  The subsequent zipper also uses
only internal pairs.  Hence coordinate \(2m\) retains the first entry of
the quiet boundary code:

\[
 q_0(0)_{2m}=0,\qquad q_0(1)_{2m}=2,
       \qquad q_0(2)_{2m}=2.
\]

The generic aperture move and both displayed direct \(p_1\) branches
change coordinate zero to one and never touch coordinate \(2m\).  Thus

\[
 A(u)_{(2m,0)}=(\beta(u_m),1)
\]

holds in every branch, not merely the generic one.

Applying reflected complement \((x,y)\mapsto(2-y,2-x)\) to the boundary
code of \(A(2-u)\) gives

\[
 A_*(u)_{(2m,0)}=(1,2-\beta(2-u_m)).
\]

The desired partner has boundary \((1,\beta(u_m))\).  The three rows are

\[
\begin{array}{c|c|c}
u_m&A_*(u)&b(u)\\ \hline
0&10&10\\
1&10&12\\
2&12&12.
\end{array}
\]

The claimed boundary-one discrepancy is exact.  The theorem correctly
does not infer equality of the remaining coordinates.

## 4. Scan-row conjugacy audit

On every internal pair, complement has the exact row action

\[
 (01-10)\leftrightarrow(12-21),\qquad
 (02-11)\mapsto(20-11).
\]

Thus phase zero maps to phase one at internal mass two, while the
mass-one and mass-three rows exchange.  On the boundary pair, the extra
swap gives

\[
 (01-10)\leftrightarrow(12-21),\qquad
 (02-11)\mapsto(02-11).
\]

This proves the matching-edge-set identity
\(\Gamma M_0\Gamma^{-1}=M_*\).  It does **not** prove an ambient digraph
automorphism: \(\tau\) does not preserve the nonwrap path.

The first-nonquiet boundary-current set is also not fixed.  A phase-zero
quiet internal `20` becomes phase-one quiet `02`, so

\[
                         \Gamma(P_0)=P_*\ne P_0
\]

in general.  The primary theorem records this correction explicitly and
retains avoidance of \(V(P_0)\) as an open collar condition.

The source identity is literal.  Internal codes transform as

\[
 q_0(2)\mapsto00,\quad q_0(1)\mapsto02,
       \quad q_0(0)\mapsto22,
\]

and the boundary swap keeps boundary code one equal to `20`.  Hence
\(\Gamma q_0(2-u)=q_*(u)\).

## 5. Reordering and collar audit

Under an honest ambient relabelling \(g\), a route last meeting
\(P_{\pi(u)}\) maps to one last meeting
\(P'_{\sigma\pi(u)}\), while its sink index maps to \(\sigma u\).
Therefore the new permutation is \(\sigma\pi\sigma^{-1}\).  The
identity cannot become complement.

Likewise, a collar starting at \(A(u)\) and avoiding the old linkage
thereafter last meets exactly \(P_u\).  Terminal labels cannot alter this
fact.  A complement counterflow must start on \(P_{2-u}\) (or meet that
path later).

## 6. Disjointness audit

Every vertex of the original promotion and aperture paths has the
unpaired root equal to one.  A counterflow interior with root flag zero or
two is therefore disjoint from the complete original linkage.  Within
the counterflow bank, the ternary zipper decoder recovers source and
stage at every majority vertex; a minority vertex is the unique scan mate
of its following majority vertex.  These facts prove disjointness up to
the terminal collar.

The primary theorem does not hide the last step: it requires the terminal
collar to retain either the root flag or an injective delimiter at every
nonterminal state and to avoid the old linkage.  Establishing that literal
collar in the fixed digraph

\[
                         D(M_0)-V(P_0)
\]

is the exact remaining predicate.

## 7. Scope verdict

Certified:

1. complement alone gives the optimal one-socket source matching;
2. the dual endpoint and its boundary discrepancy are exact;
3. the phase conjugacy is correct at matching-edge-set level;
4. scan reordering and terminal-only collars cannot fake the required
   last-intersection permutation; and
5. zipper decoding plus the root flag proves all macroscopic
   matching-faithfulness once the bounded collar is supplied.

Not certified:

1. an ambient path symmetry under \(\Gamma\);
2. avoidance of \(V(P_0)\) by the missing collar;
3. directed phase-one-to-phase-zero terminal restoration; or
4. existence of the complete complement counterflow bank.
