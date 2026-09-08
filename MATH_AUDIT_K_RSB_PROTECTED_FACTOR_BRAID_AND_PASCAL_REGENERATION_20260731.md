# Independent audit of the protected-factor RSB/Pascal regeneration theorem

Date: 2026-07-31  
Verdict: PASS after the scope corrections recorded below  
Scope: proof audit and lightweight replay only; no search or solver run

## 1. Audited theorem

This note audits

MATH_THEOREM_K_RSB_PROTECTED_FACTOR_BRAID_AND_PASCAL_REGENERATION_20260731.md.

The load-bearing conclusion is conditional:

* an accepting protected-factor root relation is necessary and sufficient
  inside one declared sealed segmentation;
* left-total odd-to-even and odd-to-odd Pascal relations would propagate
  optimal words;
* no such all-dimension left-total relation is proved.

The theorem does not claim that central decorated-factor existence implies
RSB, or that the authenticated \(k=13,\ldots,16\) transitions form an
inductive chain.

## 2. Central-input audit

The corrected componentwise decorated-2-factor theorem is sufficient for
the central path forest.  Its hypotheses include:

1. globally bijective selected upper and lower turn representatives;
2. componentwise alternating selected shore types;
3. at least one unmarked occurrence on every marked component; and
4. exclusion of the binary cycle face on every marked component.

The wholly-marked exclusion is necessary: the audited \(m=3\) example has
both palettes and alternation but lifts to two rail cycles.  The RSB theorem
retains this correction.

The symmetric difference of two spanning 2-factors decomposes into
alternating circuits, but that is only a terminal regeneration statement.
It supplies no preservation of residence, upper witnesses or compiler
variables through the packet.  Treating the packet as a regeneration node
and recomputing the terminal protected state is therefore the correct
quantifier.

The positive \(ML(7)\) hex theorem is also used with the right strength:
31 alternating hexes, 16 Hamilton outputs, 10 decorable outputs, and 6
fixed-decoration-transparent outputs.  The minimal factor-level route needs
a terminal joint decoration, not the strongest transparent subclass.

## 3. General staircase versus flatness

The master C1--C3 criterion uses arbitrary chain-aligned row intervals.  It
does not require \(D^dA=T\).  Direct replay of the retained words gives:

\[
\begin{array}{c|c|c}
k&d&\text{ordinary }D^d\text{ rank histogram}\\ \hline
13&3&7^{1716}\\
14&2&7^{3432}\\
15&3&8^{6435}\\
16&3&8^{6484}9^{6386}.
\end{array}
\]

All four derivative rows are injective.  Thus the first three endpoints
are flat in this sense, while \(k=16\) is not.  This derivative replay proves
nonflatness only; acceptance comes independently from the frozen schedule,
envelope, pin and common-cap certificate.  The frozen \(k=16\) carrier is
the mixed-depth chronology

\[
 D^2A[0,6386)\ \Vert\ D^3A[6386,12870).
\]

This is byte-identical to the endpoint-rerooted rank-eight target file.
The theorem therefore correctly makes the general staircase state primary
and the flat run state only a subclass.

## 4. Protected-state proof audit

### 4.1 Short-run events

For a fixed depth \(d\), only internal positive runs of length at most
\(d\) can enter the adjusted-frontier inequalities.  Exact concatenation
must handle both two-sided merges and one-sided closures: in \(011|0\), for
example, the old terminal arm becomes a new internal short run.  The
corrected theorem concatenates the two truncated run decompositions,
coalesces one-arms only across a \(1|1\) boundary, and reclassifies any arm
closed by a boundary zero.  Once a run exceeds \(d\), future positive
extensions cannot make it short.  Hence the corrected short-event record,
capped arms and all-one flag form an exact associative monoid.

For arbitrary omitted starts \(\alpha\), the record reconstructs every run
appearing in

\[
 \rho_j^\alpha=\max\{a:(b-a+1)+g_{b+1}\le j\}.
\]

For a legal schedule, the condition \(\tau\ge\rho^\alpha\) gives
coordinatewise row recovery.  Chain alignment is separately required for
the nested upper-row transfer.  Nonempty envelopes and cap/pin survival
remain separately present in the compiler relation.  No minimum-run scalar
is substituted for those rows.

### 4.2 Upper service

The total/prefix/suffix/deck formulas are exact: every interval is internal
to one child or uniquely crosses the join.  A distinct prefix or suffix OR
chain has at most \(k-r+1\) values because it starts at rank \(r\) and can
strictly gain at most \(k-r\) coordinates.

For a fixed-window-complete cycle factor, deleting cuts and adding joins
gives targetwise

\[
 \mu'_q(U)=\mu_q(U)-\delta_q^C(U)+\eta_q^J(U).
\]

Here the vulnerable family is restricted to required rank-\((r+q)\)
targets with positive source load; this avoids the irrelevant equality
\(0=0\).  If every fragment is longer than \(q\), the old and new boundary
occurrence counts are \(cq\) and \((c-1)q\).  Without that separation the
identity remains exact but the literal union size must replace the count.
The theorem states this qualification.

For arbitrary-width service, with invariant internal bank \(K\), final
coverage is exactly \(V\subseteq X_{\rm new}\), where
\(V={\cal U}_{>r}\setminus K\).  The bound

\[
 |V|\le |H_0|+\binom c2(k-r+1)^2
\]

follows from the two monotone boundary chains for every first/last block
pair.  This is a protected sealed-block theorem, not a permission to reopen
internal witnesses later.

### 4.3 Compiler relation

The common-cap boundary relation is the projection of the complete Boolean
compiler formula onto variables meeting the current cut.  Natural join is
conjunction and projection is existential quantification, so composition is
associative.

The coarseness proof is correct against arbitrary logical future joins:
pin a valuation in the symmetric difference of two unequal relations.  It
does not claim that every pin is a member of a restricted physical Pascal
catalogue.  Consequently a smaller physical state requires an additional
locality theorem.

Bounded conflict rank \(d+1\) does not bound boundary adhesion.  A
block-aligned Boolean path decomposition of width \(b\) would give an exact
table with at most \(2^b\) assignments, but acceptance additionally requires
a nonempty accepting root relation.  No such width-and-acceptance theorem is
extracted from the \(k=14\) or \(k=16\) certificates.

## 5. Facet-bridge audit

The one-jump schedule with

\[
 I_i=[i,i+d-1]\quad(i<a),\qquad I_i=[i,i+d]\quad(i\ge a)
\]

has mixed owner row

\[
 C_i=(D^{d-1}A)_i\quad(i<a),\qquad C_i=(D^dA)_i\quad(i\ge a).
\]

Away from the single hinge,

\[
 (D^dA)_i=C_i\cup C_{i+1}\quad(i<a-1),\qquad
 (D^dA)_i=C_i\quad(i\ge a).
\]

The hinge needs the stated literal supply test.  This qualification prevents
the schedule identity from being overgeneralized.

For a lower-rainbow directed Johnson factor, consecutive incoming/outgoing
facets at one owner are distinct and their union is that owner.  Therefore
a complete secondary cycle and a rooted primary path admit a slot-preserving
facet substitution.  The uncontracted facet maps to its successor owner,
giving the canonical containment SDR.

The \(k=16\) arithmetic is exact:

\[
 W=6435,\quad (\ell,s)=(6390,45),\quad d=3,\quad
 a=\ell-(d+1)=6386.
\]

Hence

\[
 |B|=s+d+1=49,\qquad y_d=a+d-1=W-s-2=6388.
\]

The two marked parent shifts 5113 and 5158 differ by \(s=45\), because this
literal rotated arc wraps inside the 6390-cycle while indices are written
modulo the full \(6390+45\) deck.  In the general theorem a nonwrapping arc
has only one shift piece.  The bridge is exactly the four incoming facets of
the deleted primary collar plus all 45 facets of the secondary cycle.

Light replay verifies:

* top-bit trace \(1^{6390}0^{6435}1^{45}\);
* plain chunks of lengths \(1278,5112,9,36\);
* marked owner chunks of lengths \(1277,5109\);
* 49 distinct facets and 49 missing owners;
* 128 containment edges and matching number 49; and
* 96 literal one-step socket edges and matching number 49.

The facet-ray identity \(D(e_a,\ldots,e_b,v_b)=(v_a,\ldots,v_b)\)
inherits every deeper flag wholly internal to a recovered string.  Flags
crossing a bridge end, residence, and the common-cap compiler remain in the
protected state.  The theorem does not promote the containment SDR to those
independent rows.

## 6. Finite-case reconciliation

The exact upper-debt sizes in the authenticated carriers are

\[
                0,\ 4,\ 2,\ 6\qquad(k=13,14,15,16).
\]

At \(k=14\), the four masks are \(\mathtt{0x29ce},\mathtt{0x29de},
\mathtt{0x352e},\mathtt{0x3b64}\), served by three seam rays.  At \(k=15\),
\(\mathtt{0x4e79},\mathtt{0x6f79}\) lie on one nested ray.  At \(k=16\),
the two endpoint ladders supply \(\mathtt{0xb3cc},\mathtt{0xd3cc},
\mathtt{0xd3ce},\mathtt{0xf3cc},\mathtt{0xdbce},\mathtt{0xfbce}\).

The lower boundary debts are respectively \(1,0,2,0\).  The odd cases use
global endpoint cells rather than a universal seam-recycling law.

The compiler mechanisms are not one finite local template:

* \(k=13\) uses the full \(\mathrm{COMP}_3\) fibre and is not in the
  \(DA=DP\) one-core;
* \(k=15\) uses the one-core compiler;
* \(k=16\) uses a global, asymmetric maximal-common-cap assignment.

Thus these dimensions validate the joint state but do not prove bounded
compiler adhesion or Pascal preservation.

## 7. Recursive scope

The left-total odd-spine theorem is a formal induction on exact
lower-bound-length relations.  Its odd state deliberately exports an
auxiliary facet/diamond package.  An optimal word without that occurrence
and cycle-closure data is not known to be left-total.  A weaker witness
sequence would still need one accepting even child at every odd node; an
infinite odd path alone is insufficient.

The current direct \(k=15\to17\) four-sector family fails before the
compiler: minimum positive run two, 4,045 arbitrary-width upper holes, and
60 disjoint upper-\(q=1\) conflicts.  Any complete rethread in that formula
class needs at least 60 new rank-ten edges and at least 61 old-edge
deletions.  It therefore excludes rethreads deleting at most 60 old edges
inside that direct-formula factor, not global regeneration or another
factor.

Accordingly, the exact missing theorem is uniform production of a
left-total child relation carrying simultaneously:

1. the mixed-depth/facet owner row;
2. schedule-aware residence;
3. the protected upper debt;
4. legal pins and envelopes;
5. a noncircular common-cap compiler certificate; and
6. the next auxiliary regenerative export.

No all-\(k\) conclusion is claimed.
