# Audit of the leaf--run--socket boundary-state theorem

Date: 2026-07-31  
Status: independent theorem audit PASS after corrections; exact provenance
scope recorded; no new finite search (the frozen item-2172 census is imported)

Audited theorem:

    MATH_THEOREM_AD_CATALAN_LEAF_RUN_SOCKET_BOUNDARY_STATE_AND_ROUTING_OBSTRUCTION_20260731.md

Audited SHA-256:

    9d02aaf58dda58092a059dd8351beabc825218472cb41fdf6cdc5bbdcbc5e7ac

## 1. Verdict

The final theorem is correct in its stated normalized finite-interface and
residual-host scope.

It proves an exact **complete** correlated state, not a unique globally
smallest encoding.  Its only Myhill-minimal claims are explicitly relative
to declared exterior contexts:

1. the gap connectivity partition after the planned deletions; and
2. the abstract labelled permutation-routing lower bound.

The 44-state run representation is correctly stated only as an exact upper
bound.  The physical kernel is correctly stated only as a sufficient
labelled cut-open skeleton.  The unrestricted socket profile is exact, but
has variable width.

No claim that decoration alone supplies sockets, no arbitrary-CLMT
normalization and no all-\(m\) accepting-state theorem remains.

## 2. Decoration and common-core linkage

The state coordinate is correctly a pair:

1. the current selected-occurrence decoration interface, including local
   palettes and fragment boundary types; and
2. when representatives change, the chosen common-core maximum matching
   and its pairing-resolved augmenting-linkage signature.

These are not alternatives.  A representative-changing step must export
the resulting decoration interface for later toggles.

For an alternating \(2t\)-circuit, at most \(t\) physical-incidence,
\(t\) upper-turn and \(t\) lower-turn augmented edges disappear.  If the
old deficiency is \(d\), restriction of an old maximum matching to the
common graph proves

\[
                         r\le d+3t.
\]

For a chosen maximum common matching \(M\), a new perfect matching exists
exactly when \(r\) vertex-disjoint \(M\)-augmenting paths cover its \(2r\)
exposed vertices.

If the tree adhesion has \(b\) additional named vertices, the theorem now
uses

\[
                         p=b+2r
\]

and the safe bound

\[
                         4^p p!=2^{O(p\log p)}.
\]

This matches the exact item-2169 finite linkage state.  The theorem also
correctly warns that the paths can traverse globally; bounded terminal
width is not automatic locality.

## 3. Gap-forest state

For a fixed transparent decoration, the selected lower occurrences already
give a perfect matching.  Therefore the exact update from

\[
 \Gamma'=(\Gamma-D)+S
\]

needs only the labelled component partition of the endpoints of \(S\) in
\(\Gamma-D\).  The inserted attachment multigraph must be loopless and
acyclic.

The minimality proof remains inside the balanced bipartite category.  If
two states disagree on whether \(u,v\) are connected, add one fresh matched
pair \(z,w\):

1. for opposite shores, insert the length-three path \(u-w-z-v\);
2. for the same shore, make \(z\) a leaf at \(w\) and add \(uw,vw,zw\).

The old matching plus \(zw\) is perfect in both completions, while a cycle
appears exactly when \(u,v\) were already connected.

For an open bottom-up node, the additional matching-exposure mask is
necessary.  The theorem correctly scopes this compression to a
no-hidden-reopening order; otherwise the deletion response or full boundary
forest must be retained.

## 4. Strict-run state

After shore alternation is carried by the decoration coordinate, every
complete zero-run is even.  The run coordinate therefore needs:

1. zero boundary length in \(1,2,3,4+\);
2. one boundary parity;
3. first/last typed descriptors;
4. the one-run/homogeneous flag; and
5. one absorbing internal-failure flag.

The displayed count is correct as an upper bound:

\[
 4+2+(16+8+8+4)+1+1=44.
\]

Reversal, concatenation and cyclic root closure are exact.  The theorem no
longer calls 44 coarsest: producting with the decoration coordinate permits
further quotients.

## 5. Physical residual phase

An unmarked retained subfragment has two possible residual-matching boundary
phases unless both bounding marks already lie inside the protected node.
Even an even-length subfragment is not phase-free.

The corrected physical state is a labelled cut-open path skeleton.  It
retains the incidence and order of every exposed halo and residual host,
degree deficits, open residual phases and a permanent-cycle failure flag.
It suppresses only inert nonhost degree-two subdivisions.

A finalized path is removed from the active skeleton and emits one record

\[
                         (t_C,h_C,U_C)
\]

into the socket coordinate.  The theorem makes no minimality claim for this
concrete encoding.

## 6. Socket chain-cover equivalence

Every recorded chain is required to be internally lower-injective before
its lower-label set \(\Lambda\) is formed.  Thus a repeated internal label
cannot disappear under set notation.

For two disjoint chains, the product is defined exactly by:

\[
 h\cup t'=U',\qquad
 \Lambda\cap\Lambda'=\varnothing,\qquad
 h\cap t'\notin\Lambda\cup\Lambda'.
\]

The product keeps the first entrance, last exit and union of used lower
labels.  It is associative.  After pruning socket-empty branches, every
proper socket node represents a strict subset of the final components, so
restriction of a Hamilton cycle gives only directed chains and never a
closed internal cycle.

At the root, one chain closes exactly when its last exit and first entrance
give the required first upper label and a fresh lower label.  This proves
the unrestricted iff.  The one-chain state is exact only under the stated
tree-contiguity hypothesis.

## 7. Literal permutation construction

For the uniform construction set \(m=3n-1\).  The ground count is

\[
 (m-2)+3n+1=2m.
\]

Every displayed vertex is an \(m\)-set and consecutive vertices differ by
one exchange.  The \(y_i\) tags separate all first three vertices of
different paths; the \(P,Q,d\) labels separate the last two.  Directly,

\[
 h_a\cup t_i=U_i\iff a=\pi(i),
\]

and the selected lower labels are

\[
                         C+q_{\pi(i)},
\]

so both upper and lower socket rows are exact.

The independently supplied smaller \(J(6,3)\) calibration was checked
edge-by-edge:

\[
\begin{split}
 P_1&:012-013-014-024-023,\\
 P_2&:015-025-035-135-125
\end{split}
\]

has only its two loops, while

\[
\begin{split}
 Q_1&:012-013-014-015-025,\\
 Q_2&:023-035-034-134-123
\end{split}
\]

has only its two cross-arcs.  Their selected lower labels are respectively
\(\{02,15\}\) and \(\{02,12\}\).  Each system uses ten distinct vertices.
Since \(J(4,2)\) has only six vertices, \(m=3\) is minimal under the
two-path/four-edge specification.

The \(n!\) Myhill lower bound is exact only in the abstract labelled-routing
algebra.  For \(\delta=\pi^{-1}\pi'\), choose moved \(a\), an \(n\)-cycle
\(c\) with \(c(\delta(a))=a\), and \(\rho=c\pi^{-1}\).  Then
\(\rho\pi=c\) is Hamiltonian, while \(\rho\pi'=c\delta\) fixes \(a\).
The theorem correctly does not claim that all these contexts are
transparent, leaf-peelable Catalan traces.

## 8. Separation witnesses

The three examples prove successive strict non-implications:

1. item 2158's transparent \(m=4\) toggle creates the smallest possible
   bipartite cycle \(K_{2,2}\), so transparency need not preserve the gap
   forest;
2. the \(m=2\) trace \(100100\) has leaf graph \(K_{1,1}\) but fails the
   strict run condition;
3. the \(m=2\) trace \(110000\) is leaf-peelable and strict but has no
   uniformly outgoing residual-host socket cycle.

Only the graph-cycle size, and the two explicitly stated \(m=2\)
dimension claims, are minimal.  No dimension-minimal claim is made for the
first witness.

## 9. Proven boundary

The final result is:

\[
\boxed{
\text{decoration/linkage}
+\text{gap connectivity}
+\text{strict-run transfer}
+\text{phase-indexed physical paths}
+\text{socket chain covers}.}
\]

This is necessary and sufficient under the theorem's normalized
finite-interface residual-host semantics.  It is a correlated relation,
not five independently feasible marginals.

The socket coordinate becomes bounded only under an additional routing
restriction such as tree contiguity.  Otherwise the literal permutation
family forces variable-width routing state in the abstract socket category.

## 10. Item-2172 recursion boundary

The post-audit integration of item 2172 is scope-correct.  The complete
unmodified standard \(m=5\) family has exactly two Hamilton outputs; both
have \(81/84\) turn colours on each shore and both miss the lower orbit

\[
                  \{73,146,292\}.
\]

One output is nevertheless locally all-six transparent at both glues and
uses disjoint lower triples \(\{82,84,88\}\) and \(\{50,52,56\}\).  Therefore
the standard recursion can fail in the decoration coordinate despite
passing the local private-attachment test.  This neither changes the
finite-state composition theorem nor proves a no-go for nonstandard
switches, different representatives, a different base factor, or arbitrary
decorable \(ML(9)\) cycles.

## 11. Provenance

Authoritative imported hashes:

    94bd265bce22854386cf49510fb79a18d1aec4d23389be3fd80d01eb9c4772cc
      MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md
    b9a43ef8abf3e2e9f883516411d4997c5b5cc2f5d7c7cb8d2abdc3f7a55f4088
      MATH_THEOREM_AD_CATALAN_TRACE_RESIDUAL_SOCKET_GATE_AND_M2_COUNTEREXAMPLE_20260731.md
    8081278116521aeff8875bf6b8d4d9213d8b83c7c32f3979686d1b0cbdba7cfb
      MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md
      (handoff-frozen item 2169)
    d584b5ec42177318db24d1fb2b55ba736cd8f9e6d4c6e893904f6610408595f1
      MATH_THEOREM_CATALAN_TRACE_LONG_SWITCH_AUGMENTING_LINKAGE_20260731.md
    ec31038667001e9e587ed0e9f0d81ef2c739d82c5014d47087781a10bf92cc92
      MATH_THEOREM_CATALAN_SUPPLIED_FOREST_OCCURRENCE_CONNECTOR_VOLTAGE_20260731.md
    39315e57c998c0733036ea804c3683a65188c579e07422d724410568f0782c3b
      MATH_THEOREM_CATALAN_PRIVATE_TRIPLE_STANDARD_M5_REFUTATION_20260731.md
    3bd41be38af3ddbf7a96e20adc31934c591aad1c5790984b64eea8a58e81080d
      scratch/audit_catalan_private_triple_standard_m5_refutation_20260731.py
    cb283fdfac243b1724f1eab9a7e7bddcc9fee24c450743b74b1855b7f7e1ad3c
      scratch/catalan_private_triple_standard_m5_refutation_20260731.audit.json

Provenance warning: after item 2169 was frozen, the live workspace copy of
its theorem acquired additional exposition and hashed

    f2d24f9ae051b41c884fa630ff915e372ab4b1a9cec54ea36970f4f6659ac9a3

at this audit.  The present theorem imports and reproves only the common
matching-gain, \(d+3t\), and bounded-adhesion linkage statements frozen in
item 2169; it does not rely on the post-freeze drift.

No web search, SAT solve or new finite theorem search was used.  The
item-2172 finite census is imported only through its frozen theorem and
audit.  Three independent proof audits were reconciled before this PASS.
