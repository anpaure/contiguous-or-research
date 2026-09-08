# Audit of the Catalan two-rail port theorem and its C8 obstruction

Date: 2026-07-31

Status: independent hand audit.  The fixed-fragment port theorem, the
literal \(m=2\) counterexample, and the correction of the circuit-length
parity claim are valid with the occurrence qualifications recorded below.
No all-dimensional equality statement follows.

## 1. Audited source and verdict

The audited theorem is

MATH_THEOREM_R_CATALAN_TWO_RAIL_PORT_MATCHING_AND_C8_CONNECTIVITY_OBSTRUCTION_20260731.md.

Its main mathematical assertions pass:

1. a fixed collection of two-rail fragments is parameterized exactly by
   perfect matchings of the occurrence-labelled containment port graph;
2. every such matching preserves the exact lower-q1 multiset and the entire
   immediate-upper multiplicity vector;
3. connectivity is exactly the cycle count of the fragment involution
   superposed with the port matching;
4. a simple four-rung exchange is a common-\(z\) alternating incidence
   \(C_8\), but its effect on component count is determined by the retained
   occurrence strands, not by its length; and
5. the displayed \(m=2\) split-switch instance is valid and has no
   component-merging alternating \(C_8\), even if internal-rail \(C_8\)'s
   are allowed.

Four wording or typesetting qualifications are required.

* When two unmarked cut ports represent the same physical owner, a
  symmetric-difference component is initially an occurrence-labelled
  alternating closed trail, not necessarily a simple incidence circuit.
  It is a simple \(C_{2\ell}\) when its physical upper owners are distinct.
* In the definition of the port graph, the intended symbol is
  \({\cal G}_{\rm port}\).
* In the socket-digraph display, the intended separator after \(L'\) is
  \(\quad\).
* In the \(m=2\) port graph, a cross label lies in exactly two **unmarked**
  rank-three endpoint owners.  It also lies in the marked owner \(z+L\),
  which is not on the unmarked side of that port graph.

These are scope or transcription corrections; they do not change the
proofs.

## 2. Quantifier audit of the fixed-fragment theorem

Let \(m\geq 2\), and assume all hypotheses of the Catalan two-rail rainbow
switch theorem.  Put

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname {Cat}_m .
\]

The \(K\) marked cuts are vertex-disjoint.  Indeed every cut has endpoints
\(X\in{\cal E}\) and \(J_X\) in the used parent set; the \(X\)'s are
distinct, the \(J_X\)'s are distinct, and the two classes are disjoint.
The \(K\) unmarked cuts are distinct, although adjacent cuts may share a
physical owner.  Thus:

* the marked cross ports are indexed by the \(2K\) distinct labels

  \[
       {\cal Q}={\cal E}\sqcup\{J_X:X\in{\cal E}\};
  \]

* the unmarked side consists of \(2K\) occurrence tokens, not necessarily
  \(2K\) distinct physical owners; and
* deleting all cross edges leaves exactly \(K\) path fragments on each
  rail, hence a perfect fragment-end involution \(P\) on \(4K\) tokens.

For a marked port \(p_L\) and an unmarked occurrence \(q\), the physical
cross edge exists exactly when \(L\subset U(q)\).  If a perfect matching
\(R\) selects \(p_Lq\), that edge has

\[
 (z+L)\cap U(q)=L,\qquad (z+L)\cup U(q)=z+U(q).       \tag{2.1}
\]

Every \(p_L\) is used once, so the cross lower multiset is the fixed set
\({\cal Q}\), once each.  Every occurrence \(q\) is used once, so the cross
upper multiset is the fixed occurrence multiset
\(\{z+U(q):q\in{\cal P}_0\}\).  All internal fragment edges remain fixed.
This proves independence of both complete adjacent multisets, not only
their supports.

Repeated unmarked owner values do not create a multiple physical edge.
Two matching edges incident with two tokens of the same unmarked owner have
different marked endpoints because the labels \(L\) are distinct.  A
singleton unmarked fragment therefore receives two distinct cross edges and
has physical degree two.  All other fragment endpoints receive one internal
and one cross edge.  This closes the only occurrence-to-physical
quantifier.

After contraction of retained fragments, \(P\cup R\) is literally the
degree-two token graph.  Contraction preserves component count.  Hence the
factor is Hamiltonian if and only if \(P\cup R\) is one alternating token
cycle.  Ordinary Hall only supplies some \(R\); it does not supply this
one-cycle condition.

The restriction \(m\geq2\) is appropriate.  The example below is the first
nondegenerate case.  The \(m=1\) source would require treating a one-vertex
rail cycle and its loop conventions separately and is not used.

## 3. Exact circuit and topology ledger

Let \(R,R'\) be two port perfect matchings.  A symmetric-difference
component can be written on occurrence tokens as

\[
 (z+L_i)-U_i-(z+L_{i+1})
 \qquad(0\leq i<\ell),
\]

with both \(L_i\) and \(L_{i+1}\) contained in \(U_i\).  Its toggle replaces

\[
       (z+L_i)-U_i\quad\hbox{by}\quad(z+L_{i+1})-U_i.  \tag{3.1}
\]

Equation (2.1) proves rowwise lower preservation and, more strongly,
pointwise preservation of the marked upper target \(z+U_i\).  If the
physical \(U_i\)'s are distinct, (3.1) is a simple common-\(z\) incidence
\(C_{2\ell}\).  With repeats it is an occurrence trail; its balanced
physical edge set may be decomposed into simple incidence circuits, without
asserting that the simple pieces are separately legal intermediate states.

For one exchange component, delete its old matching edges and let \(A\)
pair the exposed tokens along retained factor strands.  Let \(R_0,R_1\)
denote its old and new cross pairings.  Then the exact affected component
counts are

\[
                 c(A\cup R_0),\qquad c(A\cup R_1).     \tag{3.2}
\]

This proves the source theorem's topology criterion.  In the clean case,
one edge is deleted from each of \(\ell\) distinct cycles; the new circuit
joins the \(\ell\) resulting paths into one, giving
\(\ell\longrightarrow1\).  Without cleanliness there is no
length-only parity law.  Section 6 supplies a literal \(C_8\) with
\(2\longrightarrow2\).

## 4. Reproduction of the \(m=2\) rainbow instance

Take the old ground set \([4]\), and put

\[
\begin{aligned}
 (U_0,U_1,U_2,U_3)&=(123,124,134,234),\\
 (C_0,C_1,C_2,C_3)&=(23,12,14,34).
\end{aligned}                                         \tag{4.1}
\]

Each \(U_i\) contains \(C_i,C_{i+1}\), cyclically.  The unused middle sets
are \(13,24\).  Host \(13\) in \(U_0\), host \(24\) in \(U_1\), and retain
\(12\) in both blocks.  Thus

\[
 J_{13}=23,\qquad J_{24}=14,
\]

which are distinct.  The retained marked lower colours are

\[
 13\cap12=1,\quad24\cap12=2,\quad
 14\cap34=4,\quad34\cap23=3.
\]

They are exactly all four rank-one colours.  Hence every split-switch
rainbow hypothesis holds.

The marked parent rail is

\[
 z23,z13,z12,z24,z14,z34,z23.
\]

The two switches delete

\[
 U_3U_0,\ z23\,z13,\qquad U_1U_2,\ z24\,z14
\]

and insert

\[
 U_3z23,\ U_0z13,\qquad U_1z24,\ U_2z14.
\]

The resulting factor is

\[
\begin{aligned}
 {\cal C}_1&=(123,124,z24,z12,z13),\\
 {\cal C}_2&=(134,234,z23,z34,z14).                    \tag{4.2}
\end{aligned}
\]

Its ten lower colours, in cyclic order on the two components, are

\[
 (12,24,z2,z1,13),\qquad(34,23,z3,z4,14),
\]

so the lower palette is exact.

The four marked upper targets are \(z123,z124,z134,z234\).  Each occurs
once on a cross edge and once on an internal marked edge, hence has
multiplicity two.

Deleting the four cross edges leaves the fragment pairs

\[
 (U_0,U_1),\quad(U_2,U_3),\quad
 (p_{13},p_{24}),\quad(p_{14},p_{23}).                 \tag{4.3}
\]

The containment neighbours are

\[
\begin{array}{c|c}
p_{23}&U_0,U_3\\
p_{13}&U_0,U_2\\
p_{14}&U_1,U_2\\
p_{24}&U_1,U_3 .
\end{array}                                            \tag{4.4}
\]

Therefore the port graph is exactly the chordless cycle

\[
 p_{23}-U_0-p_{13}-U_2-p_{14}-U_1-p_{24}-U_3-p_{23}.  \tag{4.5}
\]

It has exactly its two alternating perfect matchings.  Superposition with
(4.3) gives two token cycles for either matching.  Thus no fixed-fragment
port matching, and hence no bank of fixed-fragment common-\(z\) circuits,
Hamiltonizes this factor.

## 5. Hand-exhaustive catalogue of all initial C8s

The preceding port argument excludes every fixed-fragment rematching.  The
following finite hand table is stronger: it proves that even an internal
rail \(C_8\) cannot merge the two initial cycles.

At a lower row \(L\), choose one of its two selected owners \(T\).  The
factor uses two of the three rank-two facets of \(T\); let \(D\) be the
third, unselected facet.  An alternating circuit can continue from the
selected incidence \(L-T\) only through \(T-D\).  The complete successor
table is:

\[
\begin{array}{c|cc}
L&\multicolumn{2}{c}{T\longmapsto D}\\ \hline
12&123\mapsto23&124\mapsto14\\
13&z13\mapsto z3&123\mapsto23\\
14&z14\mapsto z1&134\mapsto13\\
23&234\mapsto24&z23\mapsto z2\\
24&124\mapsto14&z24\mapsto z4\\
34&134\mapsto13&234\mapsto24\\
z1&z12\mapsto12&z13\mapsto z3\\
z2&z24\mapsto z4&z12\mapsto12\\
z3&z23\mapsto z2&z34\mapsto34\\
z4&z34\mapsto34&z14\mapsto z1
\end{array}                                            \tag{5.1}
\]

A simple alternating incidence \(C_8\) is exactly a directed four-cycle in
(5.1) with four distinct rows and four distinct chosen owners.  Reading
the table gives, up to cyclic rotation, exactly two:

\[
\begin{aligned}
 23&\xrightarrow{234}24\xrightarrow{124}14
     \xrightarrow{134}13\xrightarrow{123}23,\\
 z4&\xrightarrow{z14}z1\xrightarrow{z13}z3
     \xrightarrow{z23}z2\xrightarrow{z24}z4.          \tag{5.2}
\end{aligned}
\]

This is an exhaustive proof: every one of the twenty possible selected
incidences appears once as a labelled outgoing option in (5.1), and every
alternating continuation is forced to use the displayed target row.

## 6. Both C8s fail to merge

The first circuit in (5.2) is the common-\(z\), octahedral cross-rung C8.
It changes

\[
\begin{aligned}
 &U_3z23,\ U_1z24,\ U_2z14,\ U_0z13\\
 \longmapsto\quad&
 U_3z24,\ U_1z14,\ U_2z13,\ U_0z23 .
\end{aligned}                                         \tag{6.1}
\]

The new cycles are

\[
 (123,124,z14,z34,z23),\qquad
 (134,234,z24,z12,z13).                               \tag{6.2}
\]

It therefore has topology \(2\to2\).  At every unmarked endpoint \(U_i\),
the new cross edge still has union \(z+U_i\), so marked upper q1 is
preserved pointwise.

The second circuit is the marked star/antipodal C8.  Its toggle produces

\[
 (123,124,z24,z34,z13),\qquad
 (134,234,z23,z12,z14).                               \tag{6.3}
\]

Its four changed internal marked edges have unions

\[
 z123,\ z124,\ z134,\ z234
\]

once each before and once each after.  Thus it too preserves the complete
marked upper-q1 multiset and has topology \(2\to2\).

Equations (5.1)--(6.3) prove the stronger scoped statement:

> In this exact rainbow two-rail factor, neither of the only two initially
> alternating incidence C8s merges its components, and both preserve the
> exact lower palette and marked upper-q1 multiplicities.

Consequently the split-switch matching cannot imply a C8 connectivity
theorem even at the weakest adjacent-palette level.  The counterexample
does not exclude a longer mixed internal/cross circuit after changing the
fragment involution, nor does it obstruct choosing different source rails,
hosts, or split sides.

## 7. Protected-witness scope

For any fixed-fragment port rematching, immediate upper q1 is automatic.
There is no marked-q1 Hall obstruction in this class.  The obstruction in
the example is occurrence-port interlacing and the absence of a
Hamilton-compatible port matching.

Deeper targets are different.  A witness internal to one retained fragment
survives.  A seam-spanning target survives only if an old witness avoids all
changed seams or the new oriented fragment order supplies a literal
suffix/full-fragment/prefix replacement.  Residence requires the exact
cyclic product of the oriented fragment transition states.  These are joint
conditions and are not consequences of the lower rainbow identity or of
marked-q1 preservation.

Thus the correct reusable sufficient condition is:

*a Hamilton-compatible port matching in the component of the starting
matching under the allowed circuit exchanges, together with the literal
blocker-clutter and residence-DFA conditions.*

The source theorem supplies an initial perfect matching only.  The
\(m=2\) example proves that this weaker datum does not imply the sufficient
condition.  No conclusion about \(\nu(k)=B(k)\) is asserted.
