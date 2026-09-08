# Audit of the integral two-coordinate Catalan braid and physical side gate

Date: 2026-07-31  
Lane: R, balanced-subcube integral recursion  
Audited theorem:
MATH_THEOREM_R_CATALAN_A1_INTEGRAL_FIVE_SECTOR_BRAID_AND_DIAGONAL_GATE_20260731.md  
Verdict: **PASS after the scope and notation corrections recorded below.**

The theorem proves an exact integral normal form, a positive literal base,
and sharp physical obstructions.  It does not prove the all-parameter
forest-compatible realization.

## 1. Strict five-sector arithmetic

With

\[
 K=\operatorname{Cat}_n,\quad
 M=\binom{2n}n,\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad C=M-P,\quad R=N-C=P-K,
\]

the row and column equations on the strict reserve-avoiding transitions
force

\[
                         (P,C,R,C,P).
\]

Also

\[
 {R\over M}={n^2-2n-2\over(n+1)(n+2)},
\]

so the strict integral form starts at \(n=3\).  The corrected scope is
essential: this singleton trace polytope applies only to trades supported
on the five allowed transitions.  Child-crossing atoms are outside it.

## 2. Marginal fibre and first circuit

The complement atoms have ranks

\[
 |L|=n,\qquad |T|=|H|=n+1,\qquad |U|=n+2.
\]

Occurrencewise freezing of \((L,U,T)\) forces
\(H=L\cup(U\setminus T)\).  If only the three marginal banks are frozen,
every trade has the permutation form

\[
 (L_i,U_i,T_i)\mapsto(L_i,U_{\sigma(i)},T_{\tau(i)}).
\]

The no-\(P_2\) proof is valid after the rank shift above.  The displayed
six-row \(P_3\) is a literal all-\(n\) marginal circuit after adjoining a
common \((n-2)\)-set and leaving another \((n-2)\)-set unused.  Its opposite
shore is obtained by full-ground-set complementation with lower/upper
reversal, followed by \(c\leftrightarrow z\); core complementation alone
would be wrong.

The guarded physical criterion is exact: new heads must remain injective,
and the three added edges must be independent after contracting the forest
left by deleting the old three edges.  This is catalogue supply only.

## 3. Prefix bank and automatic common basis

For every oriented child path forest, choosing prefixes of total edge
length \(C\) gives a common bank \(B\), a peeled set \(Q\), and a bijection
\(Q\to B\).  Deleting the forward prefix edges isolates \(B\), leaves
\(R\) central edges on its \(P\)-vertex complement, and simultaneously
satisfies both port containments.

This prefix theorem is correct but is no longer the weakest incidence
route.  For \(n\ge4\), the independent Kruskal--Katona/Edmonds common-basis
theorem chooses a deletion basis \(Q\) for which both diagonal containment
matchings exist.  Thus incidence Hall is closed.  The inherited ports

\[
                         p^-(U_q)=t_q,\qquad p^+(L_q)=h_q
\]

replace the deleted central incidences one-for-one.

## 4. Diagonal load min--max

For a fixed punctured bank, the stated fractional diagonal system is exact.
Its load-vector convex hull intersects the capacity down-set if and only if

\[
 \min_{\mu}\sum_{(d,V)\in\mu}\sum_{X\in I(d,V)}\gamma_X
 \le\sum_Xb_X\gamma_X\qquad(\gamma\ge0).
\]

This is ordinary finite-dimensional separation plus assignment duality.
The degree capacities are already in the LP.  Integrality and all graphic
inequalities remain additional gates; neither follows from bipartite
matching integrality.

## 5. Physical forest and topology criteria

Both physical interfaces in the theorem are valid.

1. In the common-prefix form, the two port edges for \(q\) are
   \[
   U(q)-(\{z\}\cup p(q))-(\{c,z\}\cup L(q)).
   \]
   The middle vertex is isolated on the retained central rail.  After
   contracting the two diagonal forests and suppressing these middle
   vertices, the socket graph \(J\) must be a path forest.
2. In the inherited-port form, contract the two side forests and
   \(F-Q\).  The seam edges \(U_qt_q,h_qL_q\) form a multigraph
   \(\Gamma_Q\).  The complete support is a linear forest exactly when the
   three rail supports are forests, all anchor degree caps hold, and
   \(\Gamma_Q\) is acyclic.

The component ledger is consistent.  In the prefix form each diagonal has
\(C-K\) components, the suffix has \(K\), and a forest \(J\) has
\(C-2K\), yielding \(C-K\) complement paths and \(C\) paths after the
\(K\)-component child is adjoined.

The separately audited side-anchor theorem further proves:

- \(c_2-c_0=K\) on each side;
- \(F-Q\) induces a partial left/right matching \(P_0\);
- if \(c_0=0\), any abstract left \(K\)-matching admits an abstract right
  \(K\)-matching making \(P_0\cup P_L\cup P_R\) a forest, because \(C>2K\);
- suppressing component vertices preserves exactly this cycle rank.

The word *abstract* cannot be dropped.

## 6. Positive \(n=3\to4\) integral braid

The producer and independent consumer both pass.  The literal construction
has:

\[
\begin{array}{c|c}
\text{sector sizes including child}&15,6,14,1,14,6\\
\text{lower/upper palettes}&56/56\text{ bijective}\\
\text{tail/head roles}&56/56\text{ injective}\\
\text{physical edges}&56\text{ distinct}\\
\text{degree histogram}&0^4\,1^{20}\,2^{46}\\
\text{cycle rank}&0\\
\text{component sizes}&1^4,2,3^2,4^5,12,26.
\end{array}
\]

The first two displayed child paths are oriented forward and the last three
backward, making the recorded bank a literal prefix union.  This proves one
positive \(\mathrm{PDFB}(3)\) instance, not \(\mathrm{PDFB}(3)\) for every
child.

## 7. Canonical and product obstructions

The all-\(n\) canonical-BTK degree proof is valid.  In scan order,

\[
                         X_n=1110(10)^{n-2}
\]

has \(n-2\) incident canonical diagonal edges from the displayed free-pair
swaps and one wrap edge, hence degree at least \(n-1\).  Therefore the
canonical upper diagonal fails the side degree row for every \(n\ge4\).
At \(n=3\), the complete canonical support has only 13 degree-at-most-one
sockets for 14 anchors.

The independent \(n=3,\ldots,7\) replay confirms:

\[
\begin{array}{c|ccccc}
n&3&4&5&6&7\\ \hline
\Delta_{\rm BTK}&2&3&4&5&6\\
\text{one-port sockets}&13&44&154&552&2013\\
\text{product head deficiency}&11&49&204&825&3289\\
\text{branched edge-components}&6&24&85&291&994.
\end{array}
\]

Product edge-component counts omit isolated ambient vertices, as stated.
These are canonical/product obstructions, not no-go theorems for
noncanonical side forests.

## 8. Literal physical cut after common-basis incidence

The turn-forest theorem gives the exact shore-local normal form: each side
is a spanning linear forest on child-edge occurrences, with both turn
colour streams bijective and every deleted occurrence at a path endpoint.
The equivalent oriented two-SDR form is also exact.

More strongly, a literal parameter-three child and a genuine two-sided
common deletion basis exhibit a physical failure after incidence has
already succeeded.  On the upper side,

\[
 D^-=\{\mathtt{07},\mathtt{0b},\mathtt{0d},
        \mathtt{0e},\mathtt{13},\mathtt{23}\},
\]

all rank-four vertices except \(\mathtt{0f}\) are anchors, and targets
\(\mathtt{3d},\mathtt{3e}\) force the first two rows.  Every remaining
candidate endpoint lies in

\[
 S=\{\mathtt{0f},\mathtt{17},\mathtt{1b},
      \mathtt{27},\mathtt{2b},\mathtt{33}\}.
\]

Its residual capacity is \(2+5=7\), while four physical edges demand
eight incidences.  The opposite incidence matching is also explicit.
Therefore a synchronized common basis and two incidence matchings do not
force even the side degree row.  Another common basis for this child
remains possible.

## 9. Prescribed-pair universality is false

If a side forest with \(P\) edges realizes a two-anchor pairing \(\Pi\),
then its component-disjoint paths give the exact necessary inequality

\[
                         \sum_{\{X,Y\}\in\Pi}d_J(X,Y)\le P.
\]

For every \(n\ge3\), a \(C\)-anchor bank can be chosen with a requested
\(K\)-matching of maximum-distance pairs.  Its cost \(K(n-1)\) is larger
than
\[
                    P=K\,{n(n-1)\over n+2}.
\]
At \(n=3\), every 14-anchor bank already admits a requested five-pair
matching of cost at least \(7>P=6\).  On the literal positive prefix
interface, the five explicit distance-two pairs recorded in the side-turn
theorem have cost \(10\).  Thus the abstract greedy topology theorem cannot
be lifted through an “every prescribed pairing” assertion.

The correct remaining positive statement is adaptive: one no-empty side
pairing and a physically feasible cross-component ear sequence on the
other shore, or equivalently

\[
 \exists\,P_-\in\mathcal R^-,\ P_+\in\mathcal R^+
 \quad P_0\cup P_-\cup P_+\text{ is a forest},
\]

where \(\mathcal R^\pm\) are the physically realizable pairing families.

## 10. Exact proved boundary

The following are proved:

- forced five-sector counts;
- prefix preparation and automatic synchronized incidence;
- exact turn-forest/two-SDR physical normal forms;
- exact collision and contracted-cycle cuts;
- one literal positive \(n=3\to4\) braid;
- a literal common-basis \(8>7\) side-capacity obstruction;
- an all-\(n\) canonical-BTK degree obstruction; and
- abstract topology decoupling plus the metric refutation of universal
  pairing prescription.

The following is unproved:

> choose a favorable automatic common basis whose two turn graphs admit
> rainbow anchor-capped side forests and whose realizable pairing families
> contain an acyclic compatible pair (equivalently, prove a physically
> serializable adaptive ear construction).

This is the exact surviving integral \(a=1\) gate.  No all-dimensional
Catalan linear matching, residence, deep-shadow, compiler, or
contiguous-OR theorem is inferred.

## 11. Artifact ledger

The stale GLOP file
scratch/balanced_subcube_trace_lp_m3_m8_20260731.STALE_BUGGY.json is
quarantined and is not evidence.

All retained scripts are lightweight exact replays.  Their final hashes
are recorded in the handoff item accompanying this audit.
