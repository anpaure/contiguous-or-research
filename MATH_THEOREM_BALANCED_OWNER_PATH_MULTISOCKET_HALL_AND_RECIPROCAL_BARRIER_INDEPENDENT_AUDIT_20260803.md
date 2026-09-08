# Independent proof audit: balanced owner paths and multisocket Hall cuts

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_BALANCED_OWNER_PATH_MULTISOCKET_HALL_AND_RECIPROCAL_BARRIER_20260803.md`  
**Verdict:** the balanced path-cover theorem, the adaptive-boundary cut and
deficiency formula, the one-rank capture envelope, and the reciprocal
envelope barrier are correct.  The scope caveat is essential: the barrier
invalidates a rank-marginal proof, not the existence of a jointly
decorrelated path bank.  The residual nonadjacency law remains outside the
one-commodity flow theorem.  No computation is used in this audit.

## 1. Audit protocol and claims checked

The audit independently checks the following logical chain.

1. A symmetric fractional flow through the lower Boolean Hasse diagram can
   be rounded integrally while keeping every node flow between the floor
   and ceiling of its layer average.
2. For a fixed family of owner-rooted paths, adaptive selection of exactly
   \(C_s-b_s\) rank-\(s\) targets is an ordinary integral flow, and its cuts
   reduce exactly to

   \[
       \sum_s(e_s(Q)-b_s)_+\le d|Q|.
   \tag{1.1}
   \]

3. Floor/ceiling node balance determines the exact visitor-block size
   histogram at one rank and hence the exact one-rank capture function
   \(\Phi_s(q)\).
4. The sum of these independent rank envelopes exceeds the optimal depth
   on a fixed-density path family.
5. The preceding steps do not impose the no-adjacent-residual-rank law.

No claim about physical chronology, a fixed named boundary, or a complete
lower compiler is needed for any of these checks.

## 2. Balanced-path theorem

Let \(r\) satisfy \(C_s=\binom{k}{s}\le W=\binom{k}{r}\) for
\(0\le s\le r\), and write

\[
                       C_s=\binom{k}{s},\qquad
                       w_s=\frac W{C_s}.                 \tag{2.1}
\]

A rank-\(s\) set has \(s\) immediate subsets.  If it sends \(w_s/s\)
to each, then a fixed rank-\((s-1)\) set receives

\[
 (k-s+1)\frac{w_s}{s}
 =\frac{(k-s+1)W}{sC_s}
 =\frac W{C_{s-1}}=w_{s-1},                             \tag{2.2}
\]

using \(sC_s=(k-s+1)C_{s-1}\).  Thus the proposed fractional node flow
is conserved at every internal node.  At rank \(r\), \(w_r=1\), so it is
compatible with one unit from every distinct owner; at rank zero,
\(w_0=W\).

For every node, \(w_s\) lies between its integral floor and ceiling.  Node
splitting converts these bounds into ordinary integral lower and upper arc
capacities.  The remaining Hasse arcs can be capped at \(W\), which is at
least the total flow.  The feasible-flow polyhedron of this directed
network has integral vertices after the standard subtraction of lower
bounds.  Therefore the existence of the symmetric fractional witness
implies an integral feasible flow.

The graph is acyclic apart from the artificial source and sink, so the
integral value-\(W\) flow decomposes into \(W\) unit paths.  Every owner
source arc is fixed at one and hence starts exactly one decomposed path.
The flow on a split node arc is precisely its number of visiting paths.
This proves the stated floor/ceiling visit law.

There is no divisibility assumption hidden here.  When \(W/C_s\) is not
integral, different nodes of the same rank carry its floor and ceiling.
Also, because \(C_s\le C_r=W\) for \(s\le r\), every strict-lower node has
positive lower capacity and is visited.

No parity identity was used.  The argument therefore applies to either
widest rank in odd dimension as well as to the unique widest rank in even
dimension.  The sole required inequality is \(C_s\le W\) below the chosen
owner rank.

**Audit conclusion:** Theorem 1.1 is a valid integral network-flow theorem.

## 3. Independent derivation of the exact cuts

Fix a path bank and abbreviate \(N_s=C_s-b_s\).  Consider a network with
arcs

\[
 a\to s\to S\to T\to z,                                \tag{3.1}
\]

of capacities \(N_s,1,N+1,d\), respectively, where the
\(S\to T\) arc exists exactly when path \(T\) visits \(S\), and
\(N=\sum_sN_s\).  Capacity \(N+1\) merely represents infinity relative
to the requested flow value \(N\).

Fix a source-side rank set \(A\) and source-side path set \(Q\).  A target
of a rank in \(A\) can be put on the source side without crossing a large
arc exactly when every one of its visitors lies in \(Q\).  Including every
such target saves one unit; no other target inclusion can improve the cut.
The minimum cut with these fixed shores is consequently

\[
 \sum_{s\notin A}N_s+
 \sum_{s\in A}(C_s-e_s(Q))+d|Q|.                       \tag{3.2}
\]

Subtracting (3.2) from the desired value \(N\) gives

\[
 \sum_{s\in A}(e_s(Q)-b_s)-d|Q|.                       \tag{3.3}
\]

For fixed \(Q\), maximize over \(A\) by retaining precisely the positive
summands.  The maximum cut deficiency is therefore

\[
 \max_Q\left[
   \sum_s(e_s(Q)-b_s)_+-d|Q|
 \right]_+,                                             \tag{3.4}
\]

which is the formula in the theorem.  Integral max flow supplies distinct
selected targets and integral path assignments.

Two endpoint checks catch the usual sign errors.

* For \(Q=\varnothing\), (1.1) requires
  \(e_s(\varnothing)\le b_s\) at every rank: all unvisited targets can be
  placed inside the adaptive boundary.
* For \(Q\) equal to all \(W\) paths, \(e_s(Q)=C_s\), and (1.1) becomes
  \(\sum_s(C_s-b_s)\le dW\), the scalar capacity row.

For a fixed retained family, remove the rank-choice layer from (3.1).
The same cut proof gives the conjugate capacitated Hall condition counting
fixed targets whose whole visitor set lies in \(Q\).  This verifies the
fixed-boundary corollary as well.

Finally, targets assigned to one saturated path are nested.  Conversely,
any finite flag below an owner can be extended to a full saturated path by
inserting the missing ranks above, between, and below its members.  Paths
may meet, so these extensions do not interfere.  Hence the path-cut
formulation is exactly equivalent to the capacity-only owner-flag problem.

**Audit conclusion:** Theorem 2.1 and Corollaries 2.2--2.3 are exact; the
adaptive nature of the boundary is explicit and indispensable.

## 4. Exact one-rank envelope

At a fixed rank, the visitor sets of the \(C_s\) Boolean nodes partition
the \(W\) labelled paths.  Put \(m=\lfloor W/C_s\rfloor\).  If \(a\)
blocks have size \(m\) and \(c\) have size \(m+1\), then

\[
                         a+c=C_s,qquad ma+(m+1)c=W.     \tag{4.1}
\]

Solving gives

\[
                         a=(m+1)C_s-W,qquad c=W-mC_s.   \tag{4.2}
\]

To maximize the number of whole blocks contained in a \(q\)-element path
set, take size-\(m\) blocks first.  Before they are exhausted, the answer
is \(\lfloor q/m\rfloor\); afterward it is

\[
 a+\left\lfloor\frac{q-ma}{m+1}\right\rfloor,           \tag{4.3}
\]

capped at \(a+c\).  This is exactly the displayed formula for
\(\Phi_s(q)\).  It is attained for that one rank by taking the appropriate
whole blocks and filling unused positions of \(Q\) arbitrarily.

The tests \(\Phi_s(0)=0\) and \(\Phi_s(W)=C_s\) both hold.  Therefore the
substitution \(e_s(Q)\le\Phi_s(|Q|)\) into (1.1) is valid, proving the
balanced-marginal sufficient condition.

The word **rankwise** cannot be removed: the maximizing path set in (4.3)
depends on the rank partition.  Summing \(\Phi_s(q)\) aligns all these
possibly different maximizers adversarially.

The three extreme cut checks in Corollary 3.3 are also valid.  Balanced
visitation makes the empty visitor set absent.  The whole path bank gives
exactly the scalar inequality.  A singleton path family can capture only
multiplicity-one nodes, hence at most one target in each rank with
\(p_s>1/2\).  There are
\((\sqrt{\log2}+o(1))\sqrt r\) such ranks, strictly fewer than
\((\sqrt\pi/2+o(1))\sqrt r=d\), because
\(\log2<3/4<\pi/4\).  Thus these cuts do not hide the remaining gap.

**Audit conclusion:** Lemma 3.1 is exact at one rank, and Corollary 3.2 is
sufficient but not asserted necessary.

## 5. Reciprocal asymptotic barrier

This section, unlike Sections 2--4, specializes to \(k=2r\).

For \(s=r-j\) with \(j=O(\sqrt r)\),

\[
                         p_s=C_s/W=e^{-j^2/r+o(1)}       \tag{5.1}
\]

uniformly on every fixed scaled interval.  Thus the multiplicity-one zone
has asymptotic width \(\sqrt{\log2}\sqrt r\), while the next zone, of
multiplicity two, has width

\[
              (\sqrt{\log3}-\sqrt{\log2})\sqrt r.       \tag{5.2}
\]

Away from the lower endpoint of each zone, a sufficiently small fixed
density \(q/W=\theta\) can be filled entirely by the smaller visitor
blocks.  Each rank of the first zone then contributes \(q\) to its exact
envelope and each rank of the second contributes \(q/2+O(1)\).  Letting
the endpoint margin tend to zero gives the coefficient

\[
 \beta=\sqrt{\log2}+
 \frac12(\sqrt{\log3}-\sqrt{\log2})
 =\frac{\sqrt{\log2}+\sqrt{\log3}}2.                   \tag{5.3}
\]

The inequality \(\beta>\sqrt\pi/2\) is sound.  Indeed strict convex
midpoint estimates for \(1/x\) give \(\log2>2/3\) and \(\log3>1\), while
the classical elementary bound \(\pi<22/7\), together with

\[
                 (1+\sqrt{2/3})^2>22/7,                \tag{5.4}
\]

gives \(\sqrt{\log2}+\sqrt{\log3}>\sqrt\pi\).

Choosing a positive endpoint margin first and then a sufficiently small
fixed \(\theta\) makes the inequality uniform.  The loss from floors is
only \(O(\sqrt r)\), and the whole boundary subtraction is \(O(r)\).
Both are negligible beside \(q\sqrt r=\Theta(W\sqrt r)\).  Since
\(d=(\sqrt\pi/2+o(1))\sqrt r\), the independent-rank envelope exceeds
\(dq\) by a positive multiple of \(q\sqrt r\).

This calculation has one, and only one, negative consequence: no proof
which replaces the simultaneous quantities \(e_s(Q)\) by their separate
maxima \(\Phi_s(|Q|)\) can close the optimal-depth Hall cuts.  It does not
show that a common \(Q\) realizes those maxima, and it does not show that
Conjecture 6.1 is false.

**Audit conclusion:** Theorem 4.1 is correct with the stated scope.  Any
interpretation as a no-go theorem for all balanced Boolean path banks would
be an overclaim not made by the audited file.

## 6. Pattern-faithful system and final scope

The abstract balanced-socket proposition is correct.  At rank \(s\), fix
the floor/ceiling block sizes summing to \(W\).  Since the active row set
has size \(N_s\le C_s\), place its members in distinct blocks.  All blocks
have positive capacity, and the remaining capacity is exactly
\(W-N_s\), the number of inactive rows.  Filling it arbitrarily produces
the asserted balanced partition.  Repeating by rank preserves the given
anonymous row patterns.  These partitions need not be nested or carry
containment-compatible Boolean labels, so the proposition introduces no
unproved flag claim.

For a fixed saturated path, there is exactly one visited set at each rank.
Hence a binary mark \(x_{T,s}\) completely identifies the named target at
that path/rank occurrence.  The four constraint families in the audited
file have the following independent meanings:

\[
 \begin{array}{c|c}
 \text{constraint}&\text{property}\\ \hline
 \sum_Tx_{T,s}=N_s&\text{exact rank multiplicity}\\
 \sum_{T:P_T(s)=S}x_{T,s}\le1&\text{named-target uniqueness}\\
 x_{T,s}+x_{T,s+1}\le1&\text{residual nonadjacency}\\
 \sum_sx_{T,s}\le d&\text{owner depth}
 \end{array}                                             \tag{6.1}
\]

These conditions are plainly necessary, and marking the corresponding
visited sets proves they are sufficient.  Extending any realized flags to
saturated paths proves the converse quantifier over path banks.

After the residual nonadjacency rows are deleted, this is the
target--path max-flow problem already audited in Section 3.  With those
rows retained, the path-rank conflict and named-target capacity act on the
same occurrence variables.  Neither the balanced Boolean flow nor the
anonymous equitable rank decomposition proves integrality of that joint
system.

The final hierarchy is therefore accurate:

\[
 \begin{array}{c}
 \text{balanced integral path visitation: proved;}\\
 \text{capacity-only cuts for a fixed bank: proved exactly;}\\
 \text{existence of a bank satisfying all cuts: open in this note;}\\
 \text{the same with residual nonadjacency: strictly stronger and open.}
 \end{array}                                             \tag{6.2}
\]

The audited theorem does not claim a full optimal named inventory, does
not identify a literal triangular boundary, and does not infer any later
chronology or upper-side property.  No forbidden external chain theorem is
invoked.

## 7. Final audit verdict

The main note establishes three genuine, proof-safe advances:

1. an integral floor/ceiling cover of every lower Boolean node by distinct
   owner-rooted saturated paths;
2. the exact Hall/max-flow/deficiency criterion for using those paths as a
   serial multisocket bank with adaptive rank deficits; and
3. a rankwise-sharp reciprocal obstruction explaining why balanced node
   multiplicities alone fall short at depth \(d\).

The exact remaining conjecture is correctly isolated as a simultaneous
cross-rank expansion statement for one common path bank, followed by the
stronger residual-conflict lift.  The proofs support these conclusions and
no stronger one.
