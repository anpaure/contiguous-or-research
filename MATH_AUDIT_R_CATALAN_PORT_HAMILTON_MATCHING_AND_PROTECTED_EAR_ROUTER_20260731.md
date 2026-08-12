# Audit of the Catalan port Hamilton-matching and protected-ear theorem

Date: 2026-07-31  
Status: independent hand audit, PASS after the two scope corrections recorded
in Section 8 of the theorem.  No finite search, SAT call or web source was
used.

Audited file:

MATH_THEOREM_R_CATALAN_PORT_HAMILTON_MATCHING_AND_PROTECTED_EAR_ROUTER_20260731.md

## 1. Exact port topology

Let the two port shores have \(2K\) occurrence tokens, paired into \(K\)
fragments on each shore.  A port perfect matching contracts to a degree-two
multigraph on the \(2K\) fragments.

For fragment sets \(I,J\), the selected cut of
\({\cal A}_I\sqcup{\cal B}_J\) has size

\[
 x({\cal A}_I,{\cal B}\setminus{\cal B}_J)
 +x({\cal A}\setminus{\cal A}_I,{\cal B}_J).
\]

The degree equations imply the lower bound

\[
                         2\bigl||I|-|J|\bigr|.
\]

Therefore only balanced fragment cuts can vanish.  A disconnected
degree-two factor supplies such a proper zero cut, and every such zero cut
is a union of components.  Theorem 2.1's balanced subtour inequalities are
thus necessary and sufficient.  The graphic-rank formulation is equivalent.

If the matching is a bijection \(f\), contracting its edges transports the
unmarked fragment involution to \(Q_f=f^{-1}P_{\cal B}f\).  On an alternating
\(2s\)-cycle, the product \(P_{\cal A}Q_f\) has exactly two \(s\)-cycles.
Corollary 2.2 is correct in both directions.

## 2. Block matching criteria

A disconnected perfect matching restricts to perfect matchings on one
proper balanced fragment block and its complement.  Conversely, two such
matchings unite to a disconnected global matching.  This proves Theorem
3.1.

The guard-pruned tight-shore obstruction is also exact.  If
\(N(A_{\cal S})\subseteq B_{\cal S}\) and the two shores have equal size,
every perfect matching saturates the two sets internally, leaving no
crossing seam.  This is a sufficient protected no-go, not a claimed
characterization of every topology obstruction.

## 3. Direct constructive certificates

For fixed orientations, the first seam family pairs each marked exit with
one unmarked entry.  The second seam family maps the corresponding unmarked
exit to the next marked entry.  Factor components are literally the cycles
of this second permutation, proving the oriented-ladder equivalence.

The three-seam insertion is exact.  Removing one selected seam \(ab\) opens
the current cycle, and the chain

\[
 a-b_*^--P_{\cal B}-b_*^+-a_*^-
 -P_{\cal A}-a_*^+-b
\]

uses every old boundary port and every new port once.  The three displayed
containments are precisely the new Johnson-seam tests.  Under EC3 the
physical edges are distinct.

## 4. Socket ears and hypertrees

For a current rung \(e=(a_e,b_e)\), the socket arc \(e\to f\) is exactly
the legality of the shifted edge \(a_fb_e\).  A directed socket cycle
therefore gives a matching exchange.  If it selects one old rung from each
of distinct current factor cycles, deleting those rungs opens the cycles
into paths and the cyclic shift concatenates them into one.  Theorem 6.1 is
valid.

For the static theorem, pairwise port-disjoint supports leave every future
old rung untouched.  Rooting the component--ear incidence tree makes each
ear meet the accumulated component once and otherwise meet untouched child
components.  Induction proves Theorem 6.3, and the tree edge count gives

\[
                         \sum_T(|S_T|-1)=c-1.
\]

The converse is correctly restricted to fresh old-supported sequences in
which every switch is clean relative to the current factor.  The
clean-C8 congruence is an arity ledger only and does not revive the false
universal circuit-parity law.

## 5. Boolean rank-gap-one audit

Both \(L_e\) and \(L_f\) are \(m\)-subsets of the \((m+1)\)-set \(U_e\).
When they are distinct,

\[
 |L_e\cap L_f|=m-1,\qquad U_e=L_e\cup L_f.
\]

Thus directed ears are occurrence-labelled Johnson necklaces.

If distinct \(m\)-sets \(L,L'\) were contained in distinct
\((m+1)\)-sets \(U,U'\), their union would have size at least \(m+1\) while
the intersection of \(U,U'\) has size at most \(m\), a contradiction.
Hence there is no nondegenerate physical C4.  Repeated tokens at one
physical \(U\) merely exchange the same physical cross edges.  Lemmas
7.1--7.2 are correct and explain why C6/C8/long ears, rather than rectangle
descent, are the relevant Boolean mechanisms.

## 6. Protection quantifiers

EC1--EC3 now explicitly state:

1. the exact marked internal tagged palette;
2. the distinct unmarked internal palette; and
3. pairwise-distinct marked endpoint labels equal to its complement.

These hypotheses prove exact lower q1 independently of the port matching.
Using each unmarked endpoint occurrence once fixes the complete
immediate-upper multiplicity vector.

Guard package A is now correctly restricted.  Every physical edge deleted
at every intermediate step must avoid the frozen support \(Q\); for a
one-shot construction this is \(Q\subseteq F(M_0)\cap F(M_{\rm final})\).
The package imports all seam and cyclic hypotheses of the cited
protected-residence theorem.  Package B instead performs literal final
witness and residence-DFA replay.  Neither package infers the common-cap
compiler.

## 7. Counterexample and general-scope audit

The \(m=2\) port graph is a chordless C8.  Every proper nonempty marked-side
set has at least one extra neighbour, and every graph edge belongs to a
perfect matching.  Both perfect matchings nevertheless give two factor
cycles.  The only socket cycle has component word \(ABAB\), so it is not
component-transversal.  The lower-palette equation forces both retained
host endpoints to be \(12\), so side choice cannot repair this fixed
hosting.

Finally, the paired-port blow-up of a balanced bipartite graph is exact.  A
Hamilton cycle gives a connected port matching.  Conversely a connected
degree-two contraction on at least four vertices cannot contain a parallel
two-cycle, and hence projects to a spanning alternating cycle.  This
supports the theorem's stated scope: the general port problem contains
bipartite Hamiltonicity, while the protected Boolean ear hypotheses are
genuine additional structure.

No unconditional Catalan/PBBS ear-bank existence, K17 equality or all-\(k\)
equality is asserted.
