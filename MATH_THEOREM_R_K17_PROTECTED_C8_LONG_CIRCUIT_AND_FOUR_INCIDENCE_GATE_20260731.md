# Protected C8/long-circuit splices and the K17 four-incidence gate

Date: 2026-07-31  
Lane: R  
Status: unconditional circuit mathematics plus an independently replayed
K17 interface audit.  The exact max-retention optimum is used with its
reported `OPTIMAL` status; the lightweight replay below checks the primal
factor and every logical implication but does not reproduce a min-cost-flow
dual certificate.  No claim that \(\nu(17)=B(17)\) is made.

## 0. Verdict

There is a clean long-circuit primitive beyond incidence hexagons.

Let a balanced incidence factor contain the old shore of an alternating
\(C_{2\ell}\).  At each affected lower row retain its other owner.  If all
those retained owners use one common exterior coordinate, then toggling the
circuit preserves the complete immediate-upper multiplicity vector.  It
always preserves every lower-q1 colour.  If its deleted incidences avoid a
selected all-depth witness bank and its exact seam-DFA replay is resident,
then it is a literal zero-defect protected switch.  When its \(\ell\)
deleted Johnson edges lie on \(\ell\) distinct components, it merges them
to one.  In particular a protected \(C_8\) is the smallest possible
parity-changing component merger.

The frozen K17 Stage-2 service section does **not** satisfy the endpoint
hypothesis needed by any protected circuit theorem:

* its 1,838 advertised new witnesses repair all 1,838 old holes, but the
  3,336 forced cuts destroy the last witnesses of exactly 3,489 old targets;
* among the 1,838 prescribed service Johnson edges, 1,508 share exactly one
  source incidence and 330 share none;
* a simple alternating circuit can add only one incidence at any lower row,
  so each of those 330 zero-overlap service rows necessarily belongs to a
  compound two-passage circulation rather than one C8 (or one longer simple
  circuit);
* over **all** balanced incidence factors containing the 3,676 service
  incidences, the exact max-retention optimum contains only 13,596 of the
  13,600 frozen protected incidences.  Thus no C8 bank, no longer-circuit
  bank, and no arbitrary alternating-circuit composition can install this
  exact service section while preserving its exact frozen occurrence bank.

The four-incidence statement is an occurrence obstruction, not a target-name
no-go.  It leaves precisely the make-before-break escape: reselect at least
one occurrence section, or install alternate witnesses before releasing the
four unavoidable incidences.  It also leaves service-provider reselection
and a different compound circulation open.

## 1. Balanced incidence factors and contraction

Fix \(n=2r-1\), and put

\[
 \mathcal L=\binom{[n]}{r-1},\qquad
 \mathcal U=\binom{[n]}r.
\]

Let \(I(n,r-1)\) be the bipartite inclusion graph.  A **balanced factor** is
a simple edge set \(F\) satisfying

\[
                       d_F(v)=2
       \qquad(v\in\mathcal L\cup\mathcal U).       \tag{1.1}
\]

For \(L\in\mathcal L\), let its two selected neighbours be \(A,B\in
\mathcal U\).  Contracting \(L\) gives the Johnson edge \(AB\), labelled by
the lower colour \(L=A\cap B\).  Hence (1.1) uses every lower-q1 colour
exactly once.  Its immediate-upper colour at row \(L\) is

\[
                            A\cup B.                 \tag{1.2}
\]

A literal selected witness is represented by all incidence edges along its
contracted Johnson path.  Write \(P\subseteq F\) for the union of the
incidence supports of the selected all-target occurrences and any literal
residence corridors.

## 2. Exact projected action of an alternating circuit

Let

\[
 C=(U_0,L_0,U_1,L_1,\ldots,
       U_{\ell-1},L_{\ell-1},U_0)                  \tag{2.1}
\]

be a simple \(F\)-alternating circuit, with indices modulo \(\ell\), such
that

\[
 U_iL_i\in F,\qquad U_{i+1}L_i\notin F.             \tag{2.2}
\]

Let \(V_i\ne U_i\) be the other selected neighbour of \(L_i\) in \(F\).
Toggling \(C\) replaces, at row \(L_i\),

\[
       V_i-U_i \quad\hbox{by}\quad V_i-U_{i+1}.      \tag{2.3}
\]

All other contracted Johnson edges are unchanged.

### Lemma 2.1 (closed lower-colour packet)

The toggle (2.1) preserves every owner degree and every lower-q1 colour
exactly.  In the directed fragment ledger it is a closed packet: the new
seam at \(L_i\) reuses the label of the deleted edge at \(L_i\), so it
creates no tail, head, or lower-colour deficit outside the packet.

#### Proof

At every circuit vertex one selected incidence is deleted and one is added.
Thus all degrees remain two.  Every lower row \(L_i\) still has two selected
owners and is still contracted once with the same row label; rows outside
the circuit are untouched.  Formula (2.3) gives the literal fragment
interpretation. \(\square\)

### Lemma 2.2 (one-passage limitation)

A simple alternating circuit adds exactly one new incidence at every lower
vertex it visits.  Therefore, if a desired contracted Johnson edge \(AB\),
with \(L=A\cap B\), has neither \(AL\) nor \(BL\) in the source factor,
then no single simple alternating circuit can install \(AB\).  Any exact
symmetric-difference circulation installing it has blue degree two and red
degree two at \(L\), hence has at least two alternating passages through
\(L\) (two circuits, or one closed trail revisiting \(L\)).

#### Proof

The two circuit edges incident with a visited lower vertex have opposite
colours, one old and one new.  Thus one visit inserts one incidence.  If
both desired incidences are absent, both must be blue in the symmetric
difference.  Degree balance forces two red incidences there as well, so an
alternating decomposition has two passages through the row. \(\square\)

This is the first exact distinction between arbitrary Stage-2 seams and
simple C8/long-circuit columns.

## 3. Classification of simple incidence C8 supports

For \(\ell=4\), the upper vertices in (2.1) form a closed Johnson walk

\[
                  U_0U_1U_2U_3U_0.                  \tag{3.1}
\]

Simplicity of the incidence C8 says that the four vertices and the four
consecutive intersections are distinct.

### Theorem 3.1 (the two C8 geometries)

Up to cyclic order and relabelling, every simple incidence C8 has exactly
one of the following forms.

1. **Boolean square.**  There are \(|S|=r-2\) and distinct
   \(a,b,c,d\notin S\) such that

   \[
   \begin{split}
   U_0&=S+a+b,&U_1&=S+b+c,\\
   U_2&=S+c+d,&U_3&=S+d+a,
   \end{split}                                      \tag{3.2}
   \]

   and \((L_0,L_1,L_2,L_3)=(S+b,S+c,S+d,S+a)\).

2. **Top square.**  There is an \((r+1)\)-set \(T\) and four distinct
   \(a,b,c,d\in T\) such that the four \(U_i\) are

   \[
                  T-a,\quad T-b,\quad T-c,\quad T-d  \tag{3.3}
   \]

   in some cyclic order.  Consecutive lower rows are the corresponding
   \(T-\{a_i,a_{i+1}\}\).

Conversely, (3.2) and (3.3) give simple incidence C8 supports.

#### Proof

The Johnson distance between the opposite vertices \(U_0,U_2\) is at most
two and is nonzero.

If it is two, put \(S=U_0\cap U_2\).  A common Johnson neighbour of
\(U_0=S+a+b\) and \(U_2=S+c+d\) chooses one element of \(\{a,b\}\) and
one of \(\{c,d\}\).  The two common neighbours \(U_1,U_3\) must make
all four consecutive intersections distinct.  Choices sharing the same
element on either side repeat one consecutive lower row.  Hence the choices
are complementary, giving (3.2).

If the distance is one, write \(U_0=C+a\), \(U_2=C+b\), with
\(|C|=r-1\).  A common neighbour is either a star neighbour \(C+x\), or a
top neighbour \(C-c+a+b\).  A star neighbour has the same intersection
\(C\) with both opposite vertices and would repeat a lower row.  Therefore
both \(U_1,U_3\) are top neighbours, with two distinct deleted elements of
\(C\).  All four upper sets are consequently distinct \(r\)-subsets of
\(T=C+a+b\), proving (3.3).  The converses follow by direct intersection.
\(\square\)

Thus a physical C8 catalogue can be generated from two explicit local
geometries; an arbitrary four-tail permutation is not necessarily an
incidence C8.

## 4. Common-exterior long-circuit neutrality

The C6 common-exterior identity extends without change to every circuit
length.

### Theorem 4.1 (common-exterior protected \(C_{2\ell}\) splice)

In the setting of Section 2, suppose there is one coordinate \(x\) such
that

\[
                         V_i=L_i+x
                  \qquad(0\le i<\ell).               \tag{4.1}
\]

Assume additionally:

1. the deleted shore \(C^- =\{U_iL_i:i<\ell\}\) is disjoint from the
   selected literal witness/corridor support \(P\); and
2. after (2.3), the exact coordinate run-state automaton accepts every new
   cyclic component, including its closing seam.

Then toggling \(C\) preserves exactly:

* all middle owner degrees and the full lower-q1 palette;
* the complete immediate-upper multiplicity vector;
* every literal selected all-depth occurrence supported by \(P\); and
* the declared residence condition.

If the old projected edges \(V_iU_i\) lie on \(\ell\) distinct factor
components, the switch replaces those \(\ell\) components by one and hence
reduces the component count by \(\ell-1\).

#### Proof

Lemma 2.1 gives degree and lower-colour preservation.  Since \(V_i=L_i+x\)
and \(V_i\) is distinct from both circuit neighbours of \(L_i\), the old
and new immediate-upper colours in row \(L_i\) are respectively

\[
                 U_i+x,\qquad U_{i+1}+x.              \tag{4.2}
\]

As \(i\) runs cyclically, the second list is a cyclic permutation of the
first.  Hence the entire multiplicity vector is unchanged.

No incidence in \(P\) is removed.  At an internal vertex of any selected
witness path its two support incidences still saturate its degree, so the
same literal path survives.  Hypothesis 2 is exactly the necessary and
sufficient residence replay because all unchanged fragment interiors retain
their old coordinate words.

Finally, delete one old edge \(V_iU_i\) from each of \(\ell\) distinct
cycles.  This gives \(\ell\) paths with endpoint pairs \((U_i,V_i)\).  The
new edges \(V_iU_{i+1}\) concatenate these paths cyclically into one cycle.
\(\square\)

### Corollary 4.2 (protected C8 parity absorber)

For \(\ell=4\), Theorem 4.1 gives a zero-defect C8 switch.  When its four
old projected edges lie on four components it merges them to one, reducing
the count by three and reversing component parity.  Since consecutive
Boolean levels contain no C4, this is the smallest possible simple
parity-changing incidence circuit.

The theorem also has an exact two-component version.  After deleting the
four old projected edges, let \(M_P\) pair endpoints that lie on one retained
path, let \(M_R\) be the old-edge pairing, and let \(M_B\) be the new-edge
pairing.  The affected old and new component counts are respectively the
numbers of cycles of \(M_P\cup M_R\) and \(M_P\cup M_B\).  Thus a C8 merges
two affected components to one exactly when these numbers are two and one.
No informal “crossing” criterion is needed.

### Corollary 4.3 (length-four residence collar form)

For minimum positive-run length four, suppose every retained fragment
between switched edges has at least four owners.  For a coordinate \(z\),
let \(r_z(B)\) and \(l_z(B')\) be the terminal and initial positive-arm
lengths at a new seam, capped at four.  The residence hypothesis of Theorem
4.1 is equivalent to the pairwise conditions

\[
             r_z(B)+l_z(B')=0
       \quad\hbox{or}\quad
             r_z(B)+l_z(B')\ge4                     \tag{4.3}
\]

for every new seam and coordinate.  With a fragment of length at most three,
pairwise tests are not sufficient: the full multi-seam DFA product is
mandatory.

#### Proof

A forbidden run has word \(01^t0\), \(1\le t\le3\), and length at most
five.  A word crossing two seams contains the entire intervening fragment
and at least one vertex on either side, so a fragment of length at least four
excludes this.  The unique positive run meeting one seam has length exactly
the sum in (4.3), unless both arms vanish. \(\square\)

## 5. Exact K17 translation

Let \(F_0\) be the authenticated 11-component source factor

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
```

and let \(\mathcal S\) be the 1,838 service Johnson edges in

```text
scratch/k17_fragment_endpoint_matching_recycle_protected_20260731.result.json.
```

### Proposition 5.1 (330 rows require compound circulation)

Exactly 1,508 members of \(\mathcal S\) share one incidence with \(F_0\),
and exactly 330 share none.  No member shares two, since all are non-source
Johnson edges.  Consequently at least the latter 330 cannot be installed by
one simple alternating circuit per service row.  Each needs two alternating
passages through its lower row as in Lemma 2.2.

#### Proof

For a service edge \(AB\), compute \(L=A\cap B\) and count membership of
\(AL,BL\) in the source incidence factor reconstructed from the component
file.  The independent replay gives the histogram

\[
                             1^{1508},\qquad0^{330}.    \tag{5.1}
\]

Lemma 2.2 gives the structural conclusion. \(\square\)

This is why a catalogue containing only one C8 or one C6 per advertised
service seam is incomplete even before protection is imposed.

### Proposition 5.2 (Stage-2 is not monotone protected transport)

The 3,336 endpoint-forced source cuts plus the 1,838 service seams literally
cover all 1,838 previously missing targets and have no failure among their
advertised protected service spans.  They nevertheless destroy the last old
witnesses of exactly

\[
  3489=1864_{(10)}+1221_{(11)}+386_{(12)}+18_{(13)}  \tag{5.2}
\]

previously covered upper targets.

#### Proof

This is the exact old-target cut-kernel replay in
`scratch/k17_stage2_old_target_cut_kernel_20260731.audit.json`.  Its old-hole
and new-service counts are both 1,838, `protected_failures` is empty, and its
final holes equal its 3,489 lost-old list with rank histogram (5.2).
\(\square\)

Thus an arbitrary service transversal is not a plateau move.  A protected
long-circuit theorem must couple service gains to old-witness survival or to
literal replacements; counting only the 1,838 gains reverses the implication.

## 6. The exact four-incidence obstruction

Let \(S\) be the 3,676 distinct incidence edges of the 1,838 service
Johnson edges.  Let \(P_{\rm svc}\subseteq F_0\) be the union of all old
incidences in the selected protected suffix/prefix spans for those services.
The exact sizes are

\[
                      |S|=3676,\qquad |P_{\rm svc}|=13600.  \tag{6.1}
\]

The max-cost integral bipartite \(b\)-flow solves

\[
 R^*=\max\{|F\cap P_{\rm svc}|:
       F\text{ balanced},\ S\subseteq F\}.            \tag{6.2}
\]

The authenticated result is

\[
                              R^*=13596.               \tag{6.3}
\]

One optimal factor has eight components of lengths

\[
                   21322,2964,7,5,3,3,3,3              \tag{6.4}
\]

and loses the four incidences

\[
 (7847,7843),\ (79406,71214),\
 (96540,80156),\ (109506,109250).                      \tag{6.5}
\]

They occur in the advertised spans of provider rows
\(814,1024,1325,1352\) for this optimum.

That same maximum-incidence-retention factor has 6,499 upper target holes,
with rank histogram

\[
                    4066_{(10)}+2036_{(11)}+388_{(12)}+9_{(13)}. \tag{6.6}
\]

This is a primal counterexample to treating the unconstrained degree-two
\(b\)-flow objective as an all-target objective.  It does not prove that
every optimum has the histogram (6.6), or that no differently selected
service section can be upper-complete.

### Theorem 6.1 (frozen-section circuit no-go)

Assuming the exact `OPTIMAL` certificate (6.3), there is no balanced factor
containing \(S\cup P_{\rm svc}\).  Hence there is no sequence of C8 switches,
longer simple alternating-circuit switches, or arbitrary compound
alternating-circuit switches which installs every service incidence in
\(S\) while preserving the entire frozen occurrence section
\(P_{\rm svc}\).

This remains false even if component connectivity, residence, every old
target outside \(P_{\rm svc}\), the absolute staircase, and the compiler are
discarded.

#### Proof

Any endpoint of such a circuit sequence is a balanced factor containing
\(S\cup P_{\rm svc}\), and would have objective value 13,600 in (6.2),
contradicting (6.3).  Conversely, every balanced endpoint differs from
\(F_0\) by an Eulerian red/blue symmetric difference and therefore by an
alternating-circuit composition.  Thus the obstruction is to the endpoint,
not to a particular circuit decomposition. \(\square\)

The theorem does **not** say that four named targets must remain missing.
One incidence can support several occurrence records, and another occurrence
of the same target can replace a destroyed one.  Nor does (6.3) prove that
the four incidences in (6.5) are individually forced losses in every
optimum.  The exact conclusion is only that some four distinct incidences of
the frozen section must be released.

### Audit of the decisive implication

The max-flow construction has one rank-nine node of residual supply
\(2-d_S(U)\), one rank-eight node of residual demand \(2-d_S(L)\), and one
unit-capacity arc for each remaining inclusion.  Its integral flows are
therefore exactly the balanced factors containing \(S\).  Giving a remaining
arc cost \(-1\) exactly when it lies in \(P_{\rm svc}\) makes its objective
precisely (6.2); no chronology or target proxy enters.

The independent lightweight replay

```text
scratch/audit_r_k17_stage2_circuit_interface_20260731.py
scratch/r_k17_stage2_circuit_interface_20260731.audit.json
```

reconstructs both incidence factors from their physical component cycles,
checks degree two at all 24,310 vertices on each shore, checks containment of
all 3,676 service incidences, recounts 13,596 retained and four lost protected
incidences, identifies the four affected rows, replays (6.6), and
independently obtains (5.1)--(5.2).  It intentionally does not claim to be a second dual proof of
the min-cost optimum; the lower bound in (6.3) is inherited from the exact
`OPTIMAL` flow status.  The implication from (6.3) to Theorem 6.1 is purely
mathematical and decomposition-independent.

## 7. The corrected protected-circuit existence gate

The strongest usable replacement for the false frozen-section assertion is
a duplex circuit packet.

### Theorem 7.1 (duplex common-exterior circuit bank)

Let \(F\) be a balanced factor.  Let \(P_{\rm old}\subseteq F\) contain one
literal occurrence for every currently covered target.  Let
\(P_{\rm new}\) be a replacement section for the same target family together
with occurrences for the missing targets.  Suppose there is a balanced
factor \(F^*\) such that

\[
                     P_{\rm old}\cup P_{\rm new}\subseteq F^*, \tag{7.1}
\]

and the symmetric difference \(F\triangle F^*\) admits an order of
alternating circuits for which every intermediate exact residence-DFA replay
passes.  Then one can transport to \(F^*\) while protecting
\(P_{\rm old}\), declare \(P_{\rm new}\) protected there, and subsequently
release \(P_{\rm old}\).  No target is ever absent.

If the circuit decomposition consists of edge-disjoint common-exterior
circuits satisfying Theorem 4.1, its immediate-upper multiset and lower-q1
palette are also fixed at every step.  A C8 with the port-matching merger
condition of Corollary 4.2 supplies the required parity-changing topology.

#### Proof

Condition (7.1) is make-before-break: both occurrence sections coexist in
the handoff factor.  Until that state, no circuit removes the protected old
section.  At the handoff both sections certify every old target, so releasing
the old one loses none.  Theorem 4.1 gives the extra palette and residence
claims for the stated circuit bank. \(\square\)

For the K17 frozen service choice, Theorem 6.1 proves that one cannot take
\(P_{\rm new}=P_{\rm svc}\) while retaining it verbatim.  At least one of the
following must change:

1. the selected service seam set;
2. the occurrence chosen for one or more of the four affected service rows;
3. the old all-target witness section, via an earlier duplex replacement;
4. the circuit packet, using a compound two-passage column for each of the
   330 zero-overlap rows.

This is a precise finite target for the PBBS/fragment-braid CSP.  Circuit
columns should carry their complete red and blue incidence shores, their
old-witness damage set, their new-occurrence gain set, their lower-row labels,
their component port permutation, and their full coordinate-DFA transition.
Selecting arbitrary seam arcs and repairing only the degree equations drops
exactly the information exposed by (5.1), (5.2), and (6.3).

## 8. Proved boundary

Proved here:

1. the exact contracted action and lower-q1 neutrality of every alternating
   \(C_{2\ell}\);
2. the two possible simple C8 geometries;
3. common-exterior neutrality at every circuit length;
4. exact fixed-bank and residence conditions for a zero-defect long switch;
5. the clean component-merger theorem and the C8 parity absorber;
6. the 1,508/330 K17 one-/two-passage split;
7. the Stage-2 1,838-gain/3,489-loss scope; and
8. conditional on the authenticated exact max-retention optimum, the
   decomposition-independent four-incidence frozen-section no-go.

Not proved:

1. existence of a PBBS common-exterior C8 meeting the current K17 witness
   and residence predicates;
2. a replacement occurrence section closing the four-incidence gap;
3. a compound circuit bank servicing the 330 two-passage rows;
4. a connected resident K17 carrier satisfying all upper witnesses; or
5. a literal K17 compiler word of length \(B(17)\).

Accordingly this note supplies a rigorous protected C8/long-circuit theorem
and a sharp obstruction to applying it to the frozen Stage-2 section.  It
does not establish \(\nu(17)=B(17)\).
