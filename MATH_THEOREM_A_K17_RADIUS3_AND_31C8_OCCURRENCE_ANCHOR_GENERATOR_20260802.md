# `k=17`: the exact radius-three / `3+1`-`C8` occurrence-anchor generator

**Date:** 2026-08-02  
**Status:** pure q1 theorem.  This is a finite generator and proof-system
separator for the first move shells beyond the frozen one-for-one
Hamming-two face.  It performs no q1 solve and makes no rank-ten, residence,
topology, or compiler claim.

## 1. Scope

Let `B0` be the authenticated round-02 bank.  Let \(\mathscr R\) be the
finite catalogue of one-for-one primitive recuts, identified by immutable
base/cut data.  For every compatible \(S\subseteq\mathscr R\), including a
locally dirty `S`, let `B[S]` denote the *formal* occurrence-labelled bank
obtained after applying all members of `S`.  The word formal means that the
complete owner, orientation, endpoint, selected-colour and q1-atom data are
defined before the zero-265 rows are imposed.  This convention is necessary:
a dirty singleton may be repaired by a second or third recut.

Partition the authenticated library into two typed parts.
\(\mathcal L_0\) consists of unconditional q1 contradictions, eligible for
trace-persistence rejection before any pivot choice.
\(\mathcal L_{\rm succ}\) consists of certificates whose hypotheses arise
only after a specified pivot-footprint contraction.  A conditional
successor certificate must not be used in the unconditional anchor test.
The exact Hamming-two portfolio is treated as an input.  If it closes, the
next one-for-one recut shell is radius three.  This assertion says nothing
about move classes, such as a correlated `C8`, which are not subsets of
\(\mathscr R\).

## 2. Complete ternary occurrence delta

A native q1 atom is the triple

\[
 e=(\tau(e),\eta(e),\gamma(e)),                         \tag{2.1}
\]

where the first two entries are immutable oriented socket occurrences and
the third is the selected lower colour.  Its complete resource footprint is
recorded, including any genuine protected q1 unit-capacity resource.  In the
one-for-one face, endpoint geometry is determined at the endpoint base and
colour availability is the selected-colour predicate.  Thus the legality
predicate has the typed form

\[
 {\bf 1}_{e\in E(B[S])}
   =G^{\rm tail}_e(S)G^{\rm head}_e(S)P_{\gamma(e)}(S). \tag{2.2}
\]

For a compatible nonempty \(T\subseteq\mathscr R\), define its genuinely
new atom residue by

\[
 J_T=E(B[T])\setminus\bigcup_{A\subsetneq T}E(B[A]).     \tag{2.3}
\]

The occurrence labels and complete footprints, rather than masks, are part
of (2.3).  Deleted atoms, changed positive rows, changed capacities,
complement pairs, and invalidated blockers are recorded by exact
subset-to-final comparison; they are not assumed unary.  A row whose
physical role is relocated is a changed row, not an atom residue on the old
row.

### Lemma 2.1 (radius-three causal completeness)

Let \(S\subseteq\mathscr R\) have size at most three.  Every new q1 atom in
`B[S]` has an inclusion-minimal activation witness \(T\subseteq S\), and
hence every genuinely joint q1 atom of this bank is contained in

\[
  \bigcup_{1\le |T|\le3}J_T.                            \tag{2.4}
\]

For a radius-three bank `B[{g,h,k}]`, its native q1 atlas is reconstructed
exactly from the baseline data, the exact destruction/role deltas on every
nonempty subset, the three pair residues, and `J_{\{g,h,k\}}`.

#### Proof

Among the subsets of `S` in whose formal bank `e` is legal, choose an
inclusion-minimal one `T`.  Since \(|S|\le3\), also \(|T|\le3\), and (2.3)
places `e` in `J_T`.  The final atom set is therefore recovered from the
baseline atoms and the residues of all nonempty subsets of `S`.  Removed
atoms and changed rows/resources are recovered by literal comparison with
the final joint atlas. \(\square\)

Factorization (2.2) explains the possible ternary interaction as
tail--head--colour activation, but the proof does not assume that the colour
predicate is independent or single-supplier.  A joint palette compensation
is included automatically because all proper subsets of `S` occur in
(2.3).  The lemma makes no arity-three claim for a move with more than three
primitive edits.

## 3. Critical resources and anchors

For a library entry `K`, let \(D(K)\) be its complete load-bearing native
dependency cone.  It contains

1. every demanded occurrence/resource row;
2. every effective provider of those rows and its complete footprint;
3. every capacity, conflict, orientation or complementation datum used by
   the certificate; and
4. every guard and blocker on which an omitted provider depends.

For resource-saturation entries, all final seams meeting the demanded
support and all resources in their footprints are included.  For a guarded
minor or bicycle, every entailed leaf used by the proof is included.

For an integer \(p\), define the critical anchor hypergraph

\[
 \mathfrak A_p(K)=\{A\subseteq\mathscr R:
   1\le |A|\le p,\ A\text{ is inclusion-minimal and }B[A]
   \text{ changes a datum of }D(K)\}.                    \tag{3.1}
\]

All changes in (3.1) are evaluated on the complete formal joint atlas.
Thus \(\mathfrak A_p(K)\) includes geometry--colour joins,
two-endpoint activation, the ternary tail--head--colour residue, dirty
compensation, blocker invalidation and genuine role relocation.

### Theorem 3.1 (finite anchor bound)

Let \(S\subseteq\mathscr R\), \(|S|\le p\).  If the occurrence-labelled
trace of `K` does not persist in `B[S]`, then

\[
       \exists A\in\mathfrak A_p(K)\quad A\subseteq S.   \tag{3.2}
\]

In particular, fix any authenticated unconditional reference entry
\(K_*\in\mathcal L_0\).  Every
support-\(p\) bank which escapes every stored trace belongs to the finite
anchored family

\[
 \mathscr G_p(K_*)=
 \bigcup_{A\in\mathfrak A_p(K_*)}
   \{S\in {\mathscr R\choose\le p}:A\subseteq S\}.       \tag{3.3}
\]

The stronger necessary generator is

\[
 \mathscr G_p(\mathcal L_0)=
 \{S\in {\mathscr R\choose\le p}:
   \forall K\in\mathcal L_0\ \exists A\in\mathfrak A_p(K),\ A\subseteq S\}.
                                                               \tag{3.4}
\]

For the first recut shell after exact Hamming-two closure, put \(p=3\).
Then (3.3) requires at most three primitive anchors, and after an anchor
\(A\) is chosen only \(3-|A|\) free recuts remain.  Thus a complete
radius-three search need not start from all triples: it starts from the
finite critical tuples of one reference core and retains only triples which
also satisfy (3.4).

If \(N=|\mathscr R|\) and
\(a_i=|\mathfrak A_3(K_*)\cap{\mathscr R\choose i}|\), the number of
anchored triples before deduplication is at most

\[
       a_1{N-1\choose2}+a_2(N-2)+a_3.                  \tag{3.5}
\]

Intersecting the upward-closed anchor conditions for the other library
entries can only reduce this number.  Formula (3.5) is an enumeration bound,
not a bound on the number of library-open survivors.

#### Proof

Some datum of `D(K)` differs between `B[S]` and `B0`.  Among subsets of `S`
which already change a load-bearing datum, choose an inclusion-minimal one
`A`.  It belongs to (3.1), proving (3.2).  A bank escaping every stored trace
escapes `K_*` and every `K` separately, giving (3.3) and (3.4).  The
radius-three bound is immediate. \(\square\)

The condition (3.4) applies only to unconditional cores and is necessary,
not sufficient.  A changed datum may be irrelevant after exact contraction,
or a moved copy of the same obstruction may remain.  Entries of
\(\mathcal L_{\rm succ}\) are tested only after a pivot footprint is chosen
in Section 5.

### Corollary 3.2 (exact round-02 root-fan anchor)

Let \(A_{21}\) be the frozen twelve selected noncore socket escapes together
with the nine recuts in the two central bases.  In the one-for-one bank the
selected-colour multiplicity has the additive update law

\[
 m_{B[S]}(c)=m_{B_0}(c)+
 \sum_{g\in S}\bigl({\bf1}_{\mathrm{new}(g)=c}
                 -{\bf1}_{\mathrm{old}(g)=c}\bigr).     \tag{3.6}
\]

Together with the frozen empty nonanchor creator--supplier join, (3.6)
implies that every radius-three recut packet which destroys the original
`114930` dual fan contains a member of \(A_{21}\).  Hence its first
proof-complete radius-three generator has at most

\[
                  21{N-1\choose2}                       \tag{3.7}
\]

anchor completions before compatibility filtering and deduplication.

#### Proof

If a central role changes or the direct root seam changes, the packet uses
one of the nine central recuts.  Otherwise the central endpoint of a
noncore arm is fixed and its outside endpoint is unchanged or is created by
one mover `g`.  If the arm colour is already selected in the relevant
singleton child, that recut is one of the twelve escapes.  Otherwise
\(m_{B[g]}(c)=0\), while final selection gives
\(m_{B[\{g,h,k\}]}(c)=1\).  By (3.6), at least one of `h,k`, say `h`, is a
positive contributor, and then \(m_{B[\{g,h\}]}(c)=1\).  Thus `{g,h}` is
exactly a frozen creator--supplier pair.  The empty nonanchor join forces
one member of the pair into \(A_{21}\).  The remaining recut may repair
other rows but cannot remove this containment.  Choosing the anchor and the
other two recuts gives (3.7). \(\square\)

This corollary is root-core-specific.  Ternary residues remain necessary for
successor cores and other q1 rows.  In a move language without the additive
one-for-one law (3.6), a three-way palette compensation could evade the
Hamming-two latent join, and the generic hypergraph
\(\mathfrak A_3(K_*)\), not \(A_{21}\), is the safe anchor.

## 4. The finite support kernel

Let `B` be a final bank and let `P` be one exact footprint signature at the
chosen pivot support \(U_0\).  Define

\[
 \operatorname{Ker}_{\mathcal L_0,\mathcal L_{\rm succ}}(B,P) \tag{4.1}
\]

to contain

* \(\partial P\), every seam meeting \(U_0\), and every resource in the
  footprint of such a seam;
* for every unconditional or successor resource support \(U(K)\), the
  residual demanded resources
  \(U(K)\setminus\partial P\), every final seam meeting one of them, and
  every resource in the footprint of such a seam; and
* the complete dependency cones of every unconditional entry and every
  guarded-minor or bicycle successor entry after `P` is contracted.

This is a finite occurrence-labelled object.  It deliberately contains the
outside resources of a seam: two providers meeting different demanded rows
may conflict only on such an outside resource.

### Theorem 4.1 (kernel sufficiency)

For fixed `P`, every unconditional rejection and whether any member of
\(\mathcal L_{\rm succ}\) closes `P` are determined entirely by
\(\operatorname{Ker}_{\mathcal L_0,\mathcal L_{\rm succ}}(B,P)\).

#### Proof

For a support entry, the saturation maximum uses only seams meeting its
demanded support.  Compatibility among those seams is determined by their
complete footprints, all of which occur in (4.1).  For guarded minors and
bicycles, closure is determined by their recorded clauses, guards and
entailed leaves, which are included by definition.  No other atom can cover
a demanded row or alter a recorded implication. \(\square\)

Thus D may serialize and compare only this kernel when applying the
successor library.  This is not a small-interface theorem: the kernel is
finite at `k=17`, but its size is not claimed to be bounded independently of
dimension.

## 5. Exact radius-three survivor specification

For a compatible triple \(S=\{g,h,k\}\) retained by (3.4), materialize the
complete final bank using Lemma 2.1.  It is a **library-open zero-265
radius-three packet** exactly when

1. every frozen zero-265 row holds in the joint bank `B[S]`;
2. no member of \(\mathcal L_0\) is entailed in the complete final atlas;
3. \(\Sigma_{B[S]}(U_0)\) is reconstructed from the complete final atlas;
   and
4. there is a footprint `P` such that no conditional successor entry closes
   the contracted residual:

\[
 \exists P\in\Sigma_{B[S]}(U_0)\quad
 \forall K\in\mathcal L_{\rm succ}\quad
 K\text{ does not close }P.                              \tag{5.1}
\]

### Theorem 5.1 (complete radius-three generator relative to the library)

The following procedure emits every support-three bank satisfying (5.1):

1. enumerate the finite anchored triples (3.3), or equivalently the smaller
   unconditional hitting family (3.4);
2. reconstruct all unary, pair and ternary occurrence-labelled deltas;
3. retain exactly the joint zero-265 banks; and
4. apply every unconditional semantic core in \(\mathcal L_0\); and
5. split on every exact footprint and retain the banks satisfying (5.1).

No q1 SAT call is used.  A bank not emitted is either outside the declared
radius-three move class, fails zero-265, or is refuted by the exact
footprint-plus-successor-core proof system.

#### Proof

Every library-open bank must disturb every unconditional core, so Theorem
3.1 enumerates it.  Lemma 2.1 makes the reconstructed atlas complete,
including the genuinely ternary atoms.  The unconditional semantic scan is
exact relative to \(\mathcal L_0\).  The negation of the conditional
successor-cover condition
\(\forall P\,\exists K\in\mathcal L_{\rm succ}\,
K\text{ closes }P\) is precisely (5.1).  Hence the last filter is exact
relative to that proof system. \(\square\)

Passing (5.1) has no positive q1 meaning: a new core, a larger Hall shore, or
a functional-Hall cylinder may still refute the bank.

### Corollary 5.2 (the three genuinely new radius-three mechanisms)

After final replay, every radius-three packet satisfying (5.1) belongs to
the first applicable one of the following classes.

1. **Clean pair extension.**  Some proper two-recut subpacket already
   satisfies the zero-265 and library-open conditions.
2. **Local-debt completion.**  No proper pair passes both predicates, but
   some proper pair is library-open and locally dirty; the remaining recut
   repairs its zero-265 debt in the full triple.
3. **Distributed core cover.**  No proper pair is library-open and every
   changed q1 datum has a unary or binary activation witness, but the three
   recuts jointly disturb the last surviving certificates of different
   stored cores.
4. **Primitive ternary constructor.**  Some load-bearing final atom or
   boundary datum has inclusion-minimal activation support of size three,
   recorded in `J_{\{g,h,k\}}`.

Consequently, appending one recut only to the `3664` Hamming-two portfolio is
not a complete radius-three generator: it can omit both classes 2 and 3.

#### Proof

If a proper pair passes the two final predicates, class 1 holds.  If none
does but a locally dirty proper pair is library-open, class 2 holds.  In the
remaining case no proper pair is library-open.  Inspect the exact subset
truth table of every changed load-bearing datum.  If every change has unary
or binary support, the three proper-subset effects must jointly remove the
last stored closures, which is class 3.  Otherwise a datum has minimal
support three, giving class 4.  These cases are exhaustive.
\(\square\)

## 6. The incomparable `3+1`-`C8` shell

The exact simple Boolean incidence-`C8` classification has two families.

* In the **star** family,
  `C_i=S union {a_i}` with `|S|=7`.
* In the **octahedral** family,
  `C_i=S union {a_i,a_(i+1)}` with `|S|=6`, cyclically in `i`.

For each four-petal set there are three cyclic orders modulo reversal and
two toggle phases.  At `k=17` each family therefore has `24504480`
canonical oriented keys, for the raw proof-complete bound

\[
                         49008960.                       \tag{6.1}
\]

The star family alone is not a complete simple-`C8` catalogue.

Let \(\mathscr C_{31}\) be the subcatalogue of these literal alternating
`C8` packets whose four removed owner adjacencies have the aligned `3+1`
component-role pattern.  A packet is represented by its four removed and
four added occurrence-labelled q1 incidences, not by its owner masks.  Its
physical `C8` equations, orientation, selected-colour and endpoint roles are
part of the object.  For the role-relocation subface, final replay must also
show that a demanded forced-row occurrence is changed or internalized;
touching or renumbering its old component is not role relocation.

For `K in \mathcal L_0`, let \(\operatorname{Anc}_{31}(K)\) be the finite set of changed
`C8` slots whose reverse dependency cone meets `D(K)`.  This includes a slot
which relocates a demanded role even when none of its added seams lies in an
old provider row.  The reverse cone is the hypergraph cone of the *joint*
packet: a slot belongs to it when it participates, possibly with one or more
other changed slots, in a new endpoint--endpoint, endpoint--colour or
tail--head--colour atom incident with `D(K)`.  It is not the union of four
singleton deltas.

### Theorem 6.1 (`3+1`-`C8` anchor theorem)

If a packet \(Q\in\mathscr C_{31}\) escapes the trace of `K`, at least one
of its four changed adjacency slots belongs to
\(\operatorname{Anc}_{31}(K)\).  Consequently every `3+1`-`C8` packet which
escapes all stored cores is generated by

1. anchoring one of its four slots in
   \(\operatorname{Anc}_{31}(K_*)\) for any fixed unconditional reference
   core `K_*`;
2. completing the other three slots by the literal alternating-`C8`
   equations and the `3+1` role pattern;
3. replaying the joint zero-265 rows; and
4. applying the footprint-open test (5.1).

#### Proof

If no changed slot lies in the reverse dependency cone, every occurrence,
provider, resource incidence, capacity and guard in `D(K)` is unchanged, so
the stored trace persists.  The contrapositive gives the anchor.  The four
listed stages then enumerate every packet in the declared physical class
and apply the same exact relative separator as Theorem 5.1. \(\square\)

A `3+1` `C8` changes four owner adjacencies but is one correlated packet; it
is not a radius-four member of the independent-recut metric.  Conversely,
a radius-three packet need not have an alternating-`C8` realization.  The
two generators must be retained as separate faces.

## 7. Completeness and failure boundaries

The generators have no false omission **within their declared move classes**
provided that

1. the primitive recut and `C8` catalogues are physically complete;
2. all banks are reconstructed on immutable occurrence labels;
3. dirty intermediate subsets are retained when forming joint residues;
4. tail--head--colour ternary atoms, role relocation, blocker invalidation,
   capacities and every outside footprint resource are included;
5. zero-265 is replayed on the complete joint bank;
6. anchor/persistence rejection is applied only to unconditional cores; and
7. every footprint and conditional successor closure is tested on the
   kernel (4.1).

It is proof-safe to enlarge any anchor family: this emits extra candidates.
Shrinking it without a reverse-dependency proof can omit a genuine survivor.

The theorem does not cover four-or-more independent recuts, overlapping
same-base edits, segment rethreads, nonliteral `C8` packets, or a move whose
endpoint/colour predicates do not satisfy the declared primitive contract.
It does not show that a radius-three or `3+1`-`C8` survivor exists.  It does
not turn a library-open footprint into q1 feasibility.  Finally, a move may
destroy every old trace yet remain refuted by the successor cover; this is
why (5.1), not trace disturbance alone, is the final survivor condition.
