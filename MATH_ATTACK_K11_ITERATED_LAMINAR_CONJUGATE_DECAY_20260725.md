# Lane K11: iterated laminar conjugates, exact persistence, and the shielding obstruction

Date: 2026-07-25

This report asks whether K10's literal \(1/16\)-density laminar packet cut
can be renewed under fresh coordinate conjugates until only \(o(W)\) owners
remain unresolved.

The exact outcome is as follows.

1. The native \(s=0\) packet atlas can be exhausted geometrically by an
   actual sequence of complete-component cuts. This processes all of that
   atlas with exact persistence, but the atlas contains only
   \((1/8+o(1))B\) rows and has only \(o(W)\) first-shadow repair capacity.
2. A hereditary fresh-clean-cover property would give literal global decay
   in \(\lceil17\log m\rceil\) renewal rounds, with at most \(B\) switched
   rows and \(O_A(W/\sqrt m)=o(W)\) certified multidepth tag charge.
3. Coordinate conjugation alone does not verify that property. It transports
   the factor, atlas, and residual set together and never leaves the original
   packet cube, modulo a final global relabelling.
4. Seam richness is antagonistic to persistence of the global
   resolved/unresolved bit. A frozen middle-root set \(Z\) can be kept fixed
   while \(Z^c\) is conjugated by \(\sigma\) if and only if
   \(\sigma Z=Z\). Every seam witnesses failure of this shielding condition.
5. For general packet route bits, the exact obstruction is a pathwise
   control-block loss. K10's \((11/128-o(1))W\) seams concern the old
   preparation bit, not the current route bit, and do not bound that loss.

Thus the present results do not produce the requested unconditional global
endpoint with total unbalanced mass \(o(W)\). They do give the strongest
literal iteration supported by the packet theorem, the exact conditional
geometric theorem, and a rigorous obstruction to renewal by fresh global
conjugation alone.

---

## 1. Native packets

Assume \(1\le H\le m-2\), and put

\[
 n=2m+1,\qquad B=C_m=\operatorname{Cat}_m,\qquad W=nB,\qquad M=m-2.
\tag{1.1}
\]

For every \(R\in\mathcal D_M\), the canonical MSW factor contains the
complete size-two component

\[
 K_R=\{1100R,1010R\}
\tag{1.2}
\]

for \(\tau=(2\ 3)\). Let \(U_R\) be the union of the middle roots owned by
the two rows of \(K_R\). Then

\[
 |U_R|=2n.
\tag{1.3}
\]

The \(U_R\) are pairwise disjoint and \(\tau\)-invariant. Precisely four
roots of \(U_R\) are fixed by \(\tau\), so switching \(K_R\) genuinely moves
\(2n-4\) middle roots.

For \(1\le q\le H\), define the suffix cylinders

\[
 \mathscr C(q,V)=\{UV:U\in\mathcal D_q\},
 \qquad V\in\mathcal D_{M-q}.
\tag{1.4}
\]

Together with \(\mathcal D_M\), these form a laminar family. Restriction to
an arbitrary subset of \(\mathcal D_M\) preserves laminarity. Its incidence
matrix is totally unimodular by the alternating-depth
Ghouila--Houri signing.

The exact Catalan ratio is

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 \longrightarrow\frac1{16}.
\tag{1.5}
\]

---

## 2. Unconditional geometric exhaustion of the native atlas

### Theorem 2.1

There is an actual sequence of complete-component cuts with active packet
sets \(Q_t\subseteq\mathcal D_M\) such that

\[
 Q_0=\mathcal D_M,\qquad
 |Q_t|\le\left\lceil\frac{C_{m-2}}{2^t}\right\rceil.
\tag{2.1}
\]

Every packet removed from \(Q_t\) is switched exactly once, every earlier
choice persists, and all native packets are switched after at most
\(\lceil\log_2 C_{m-2}\rceil+1\) rounds.

The cumulative exact ledgers are

\[
 \#\{\text{switched rows}\}
 =2C_{m-2}
 =\left(\frac18+o(1)\right)B,
\tag{2.2}
\]

\[
 \#\{\text{genuinely moved middle roots}\}
 =(2n-4)C_{m-2}
 =\left(\frac18+o(1)\right)W.
\tag{2.3}
\]

The complete certified private marked ledger through depth \(H\), including
the complementary upper copy, has size at most

\[
 2\sum_{q=1}^{H}C_qC_{m-q-2}
 \le 2C_{m-1}=o(W).
\tag{2.4}
\]

#### Proof

Suppose \(Q_t\) has been constructed. Restrict every cylinder (1.4) to
\(Q_t\), add \(Q_t\), and delete empty sets and repeated rows. The resulting
family is laminar and its incidence matrix remains totally unimodular. The
half-vector is feasible in \(x\in[0,1]^{Q_t}\) for

\[
 \left\lfloor\frac{|L|}{2}\right\rfloor
 \le x(L)\le
 \left\lceil\frac{|L|}{2}\right\rceil
\tag{2.5}
\]

on every restricted laminar set \(L\). Stacking the laminar incidence
matrix and its negative with \(I\) and \(-I\) preserves total
unimodularity, so this polytope has an integral \(0/1\) vertex. Choose its
orientation so that its one-set
\(S_t\subseteq Q_t\) obeys

\[
 |S_t|\ge\left\lfloor\frac{|Q_t|}{2}\right\rfloor.
\tag{2.6}
\]

Switch every \(K_R\) with \(R\in S_t\), and set
\(Q_{t+1}=Q_t\setminus S_t\). Then

\[
 |Q_{t+1}|\le\left\lceil\frac{|Q_t|}{2}\right\rceil,
\]

and repeated ceilings give (2.1). Switch a final singleton explicitly.

The root blocks \(U_R\) are pairwise disjoint and \(\tau\)-invariant.
Changing one cell therefore changes no row on either shore of another cell.
Every later cut is still a complete current component and every earlier
choice persists.

Every one of the \(C_{m-2}\) cells is eventually switched, which proves
(2.2)--(2.3). At depth \(q\), a marked lower packet is indexed by
\(R=UV\) with \(U\in\mathcal D_q\) and
\(V\in\mathcal D_{m-q-2}\), so there are
\(C_qC_{m-q-2}\) such marks. Complementation gives the upper copy, and
Catalan convolution proves (2.4). \(\square\)

### Scope

Every current residual cylinder is half-split in the round in which it is
processed. The terminal all-one vector is not a cumulative half-signing.
Equation (2.4), rather than terminal discrepancy one, is why this complete
tagged residue is harmless on the \(W\)-scale.

The native atlas cannot repair a macroscopic first-shadow defect. One native
two-for-two toggle has two positive first-shadow cells, so it fills at most
two old holes. Therefore

\[
 M_1(F_{\mathrm{terminal}})
 \ge M_1(F_{\mathrm{MSW}})-2C_{m-2}.
\tag{2.7}
\]

Since \(C_{m-2}=O(B)=o(W)\), the premise
\(M_1(F_{\mathrm{MSW}})\ge\delta W\), for fixed \(\delta>0\), gives

\[
 M_1(F_{\mathrm{terminal}})\ge(\delta-o(1))W.
\tag{2.8}
\]

Thus geometric decay inside the atlas is not global balancing.

### Theorem 2.2 (one unconditional fresh carrier bit)

Put

\[
 s=\left\lceil\frac{3H}{4}\right\rceil,\qquad
 M_s=m-s-2,\qquad
 \tau_s=(\beta_s\ \gamma_s),
\]

with \(\beta_s=2s+2\) and \(\gamma_s=2s+3\), as in K10. Assume \(m\) is
large enough that \(H\ge3\) and \(M_s\ge H\). The shifted cells are

\[
 K_{s,R}=\{P_s1100R,P_s1010R\},
 \qquad P_s=1^s0^s,\quad R\in\mathcal D_{M_s}.
\tag{2.9}
\]

After any \(s=0\) native laminar preparation, every \(K_{s,R}\) survives
verbatim as a complete current \(\tau_s\)-component. There is one literal
complete-component cut of these shifted cells such that, for every
\(q\le H\) and \(V\in\mathcal D_{M_s-q}\), the two certified tagged loads
on the shifted private pair are

\[
 \left\{
 \left\lfloor\frac{C_q}{2}\right\rfloor,
 \left\lceil\frac{C_q}{2}\right\rceil
 \right\}.
\tag{2.10}
\]

The cut switches \(C_{M_s}+O(1)\) shifted carrier rows. If the original
tagged pile of height \(C_q\) has pair-collision
\(\binom{C_q}{2}\), its post-cut self-collision is

\[
 \psi(C_q)
 =\left\lfloor\frac{(C_q-1)^2}{4}\right\rfloor
 \le\frac12\binom{C_q}{2}.
\tag{2.11}
\]

#### Proof

For \(s\ge3\), shifted packet indices begin with \(1^s\), while the native
\(s=0\) indices begin with \(1100\) or \(1010\). The two row families are
disjoint in the canonical exact factor, hence their invariant middle-root
blocks are disjoint. Switching native blocks therefore leaves every shifted
cell and both its shores untouched.

On \(\mathcal D_{M_s}\), use the suffix cylinders
\[
 \{UV:U\in\mathcal D_q\},
 \qquad q\le H,\quad V\in\mathcal D_{M_s-q}.
\]
They are laminar by the same proof as (1.4). The half-vector and total
unimodularity give one integral simultaneous half-selection. Each cylinder
has \(C_q\) cells, and the common-orientation marker identity moves its
tagged occurrences between the two private targets, proving (2.10).
The full-atlas constraint gives \(C_{M_s}+O(1)\) switched rows.

Finally, splitting an integer \(C\) into
\(\lfloor C/2\rfloor,\lceil C/2\rceil\) gives
\[
 \binom{\lfloor C/2\rfloor}{2}
 +\binom{\lceil C/2\rceil}{2}
 =\left\lfloor\frac{(C-1)^2}{4}\right\rfloor,
\]
and the displayed half-collision bound follows. \(\square\)

Theorem 2.2 realizes the first shifted packet-group bit physically, with
zero packet loss. It does not realize a second independent
noncommuting bit. That is exactly where the fresh control-block problem of
Section 6 begins.

---

## 3. The hereditary theorem that would give global decay

A legal clean packet cell in a current exact factor consists of two current
rows whose two shores form one complete ownership component for a current
transposition, whose invariant middle-root block has size \(2n\), and whose
two rows carry at most \(2H\) certified lower/upper route tags. A clean atlas
is a family of such cells with pairwise disjoint middle-root blocks. A clean
laminar atlas additionally carries a laminar family \(\mathscr L\) on its
cell indices, containing the full cell set \(\mathcal A\). A laminar
half-selection means \(x\in\{0,1\}^{\mathcal A}\) and
\[
 \left\lfloor |L|/2\right\rfloor
 \le x(L)\le
 \left\lceil |L|/2\right\rceil
 \qquad(L\in\mathscr L).
\]

### Definition 3.1

Fix a stopping threshold \(r_\star\). Property
\(\mathrm{HLC}_\eta(r_\star)\) says that for every admissibly reachable
pair \((F,R)\), obtained from the initial pair by any earlier sequence of
certified clean switches, where \(R\) is the surviving unresolved union and
\(|R|_{\mathrm{row}}>r_\star\), there is a clean current atlas wholly in
\(R\) and a laminar integral half-selection whose selected row set \(E\)
satisfies

\[
 |E|\ge\eta |R|_{\mathrm{row}}.
\tag{3.1}
\]

Every selected cell must be a complete component in the current \(F\), not
merely a transported certificate from an earlier factor.

### Theorem 3.2

Assume \(\mathrm{HLC}_\eta(r_\star)\) for a fixed \(\eta>0\). Then there is
an actual sequence of complete-component cuts, stopped on first reaching
\(|R_t|_{\mathrm{row}}\le r_\star\), such that

\[
 |R_t|_{\mathrm{row}}
 \le\max\{r_\star,(1-\eta)^tB\}.
\tag{3.2}
\]

The post-switch rows on every earlier selected block persist verbatim, and

\[
 \sum_t\#\{\text{switched rows at stage }t\}\le B,
\tag{3.3}
\]

\[
 \sum_t\#\{\text{certified marked tags at stage }t\}
 \le HB=\frac HnW.
\tag{3.4}
\]

For \(H\le A\sqrt m+1\), (3.4) is
\(O_A(W/\sqrt m)=o(W)\).

Define the canonical half-atlas row density

\[
 p_m:=\frac{2\lfloor C_{m-2}/2\rfloor}{C_m}
 \longrightarrow\frac1{16}.
\tag{3.5}
\]

For all sufficiently large \(m\), \(p_m\ge1/17\). Thus
\(\mathrm{HLC}_{p_m}(B/m)\) would give, for

\[
 T=\lceil17\log m\rceil,
\tag{3.6}
\]

\[
 |R_T|_{\mathrm{row}}\le B/m,\qquad
 |R_T|_{\mathrm{root}}\le W/m=o(W).
\tag{3.7}
\]

Here a process which stops early is extended by keeping \(R_t\) constant.

#### Proof

While \(|R_t|_{\mathrm{row}}>r_\star\), apply
\(\mathrm{HLC}_\eta(r_\star)\) to the current pair \((F_t,R_t)\). Switch
the selected complete cells and delete their row blocks from \(R_t\).
Because the atlas lies wholly in the unresolved union, its root blocks are
disjoint from all previously frozen blocks. Thus each step is literal and
persistent. Before stopping, (3.1) gives the multiplicative bound; after
stopping, the residual is at most \(r_\star\). This proves (3.2).

The selected invariant root blocks are disjoint, every block has \(2n\)
roots, and their union lies in the \(W=nB\) middle roots. Hence at most
\(B/2\) cells are ever selected. Each contributes two switched rows and at
most \(2H\) tags, proving (3.3)--(3.4). Equation (3.5) follows from (1.5),
including the negligible floor. Finally,

\[
 (1-1/17)^T\le e^{-T/17}\le m^{-1},
\]

which proves (3.7). \(\square\)

The theorem controls unresolved middle owners and the certified tagged
ledger. It implies the full multidepth objective only after the untagged and
collateral rows are also shown to satisfy the charged common-TU hypotheses
of K10.

---

## 4. Global conjugation does not renew the clean cover

Write \(\mathcal P_\sigma(F)\) for the complete ownership-component
partition of \(F\) against \(\sigma F\).

### Lemma 4.1

For every coordinate permutation \(g\),

\[
 \mathcal P_{g\sigma g^{-1}}(gF)=g\mathcal P_\sigma(F).
\tag{4.1}
\]

If \(\mathcal A\) is an atlas in \(F\) and \(R\) an unresolved set, then

\[
 \#\{K\in\mathcal A:K\subseteq R\}
 =
 \#\{gK\in g\mathcal A:gK\subseteq gR\}.
\tag{4.2}
\]

#### Proof

Relabelling sends every root \(X\) to \(gX\), every owner row to its
\(g\)-image, and every \(\sigma\)-owner edge to a
\(g\sigma g^{-1}\)-owner edge. It sends connected components bijectively,
which proves both assertions. \(\square\)

### Proposition 4.2

Begin with the canonical factor \(F_0\). Allow arbitrary whole-factor
coordinate relabellings and toggles only of the currently transported native
cells (1.2). Every reachable factor has the normal form

\[
 gF_\varepsilon,
\tag{4.3}
\]

where \(g\in S_n\) and \(F_\varepsilon\) is a vertex of the original native
packet cube. Modulo the final global relabelling, the actionable row union
is always the same
\[
 2C_{m-2}=(1/8+o(1))B
\]
native union.

#### Proof

The assertion holds initially. A global relabelling left-multiplies \(g\).
Toggling a currently transported native cell changes one coordinate of
\(\varepsilon\). Induction proves (4.3). \(\square\)

This does not cover a genuinely recomputed component atlas in a mixed
current factor. It proves exactly that a fresh coordinate conjugate is not
itself a regeneration theorem. Nor does large residual mass imply
whole-cell containment for one native atlas. Keep one of the two rows in
each native cell and every background row. This is an admissible union of
whole row-root blocks, contains no complete native cell, and retains
\[
 W-nC_{m-2}=\left(\frac{15}{16}+o(1)\right)W
\]
middle roots.

The phrase modulo global relabelling is harmless for coordinate-invariant
defect objectives. Exact labelled destinations co-move and must be tracked
separately.

Even the full static canonical contextual packet graph has audited maximum
matching

\[
 \nu(\mathfrak M_m)=\left(\frac{11}{72}+o(1)\right)B.
\tag{4.4}
\]

Hence a nonreusing schedule of transported static cells covers at most
\((11/36+o(1))B\) rows and leaves an independent residual set of
\((25/36+o(1))B\) rows. State-dependent recomputation is indispensable.

---

## 5. Shielding, seams, and component monochromaticity

Let the rows of an exact factor \(F\) own a partition of the middle layer.
For a union \(Z\) of complete row-root blocks and a transposition \(\sigma\),
let \(\Gamma_\sigma(F)\) be the owner graph: every moved orbit
\(\{X,\sigma X\}\) gives an edge between the owners of \(X\) and
\(\sigma X\). Its connected components are the complete ownership
components.

### Theorem 5.1 (shielding equivalence)

The following are equivalent.

1. Every component of \(\Gamma_\sigma(F)\) lies wholly in \(Z\) or in
   \(Z^c\).
2. The global indicator \(1_Z\) is component-monochromatic.
3. No owner edge crosses \(Z,Z^c\).
4. \(\sigma Z=Z\).
5. The rowwise prescription bit zero on \(Z\) and bit one on \(Z^c\) is
   constant on every ownership component and therefore defines a literal
   component cut which fixes every row in \(Z\) and applies \(\sigma\) to
   every row in \(Z^c\).

#### Proof

The first three statements are equivalent by connectedness. An edge crosses
exactly when some \(X\in Z\) has \(\sigma X\notin Z\), so (3) and (4) are
equivalent. Under (1), the rowwise prescription in (5) is constant on each
component, so its component cut is legal. Conversely, any componentwise
realization of that rowwise prescription makes the zero-side root union a
union of complete component root blocks, hence \(\sigma\)-invariant. Thus
(5) implies (4). \(\square\)

### Corollary 5.2

If \(X\in Z\) and \(\sigma X\notin Z\), then the fresh component containing
that seam contains both a bit-one \(Z\)-row and a bit-zero \(Z^c\)-row.
Therefore no complete-component cut realizes either nonconstant global
indicator orientation \(1_Z/0_{Z^c}\) or \(0_Z/1_{Z^c}\) for that colour.

For K10's selected root set \(\mathcal E\), the productive coordinate
matching supports

\[
 \left(\frac{11}{128}-o(1)\right)W
\tag{5.1}
\]

such genuine seams in total. The same statistic that certifies a nonlocal
commutator therefore certifies failure of exact shielding for the
preparation indicator. It does not count distinct fresh components: all
seams of one colour may coalesce.

This statement is deliberately scoped to the global preparation bit. If an
outside row is unlabelled, or if the current routed packet bit is unrelated
to \(1_{\mathcal E}\), a seam need not violate the weaker packet-only
monochromaticity condition.

### Corollary 5.3

Let \(\mathcal O\) be a coordinate-transposition menu generating \(S_n\),
in particular K10's connected degree-three menu. If a middle-root set \(Z\)
is shielded in the sense of Theorem 5.1 for every colour of \(\mathcal O\),
then

\[
 Z=\varnothing
 \quad\text{or}\quad
 Z=\binom{[n]}m.
\tag{5.2}
\]

#### Proof

Shielding makes \(Z\) invariant under every generator, hence under \(S_n\).
The \(S_n\)-action on the rank-\(m\) layer is transitive. \(\square\)

This corollary fixes one root union \(Z\) and requires verbatim persistence
through every menu generator. A dynamically changing \(Z\), a proper
subword, or setwise motion inside \(Z\) is outside its scope.

There is consequently a sharp trilemma.

* Globally conjugating both frozen and residual sets is literal, but
  preserves atlas coverage by Lemma 4.1.
* Partially conjugating all of the residual while fixing the frozen set is
  literal only for colours with zero boundary. With nonzero boundary one
  may still keep mixed components old and switch pure residual components,
  but this is only partial progress and needs its own coverage theorem.
* A seam-rich colour has mixed complete components, so persistence requires
  a new correlated routing theorem.

---

## 6. Exact pathwise control-block loss

At a route stage \(t\), let \(\mathcal C_t\) be the freshly recomputed
ownership components for the current colour \(\sigma_t\). Each active
logical packet \(P\) has two current row lineages and a prescribed bit
\(b_P(t)\in\{0,1\}\). Make a graph whose vertices are \(\mathcal C_t\) and
whose packet edge \(P\) joins the components containing its two rows; loops
are allowed. Mark every component containing a row which must persist
verbatim as forced zero. The connected pieces are the control blocks.

### Theorem 6.1 (block-uniform routing)

For a control block \(Q\), put

\[
 n_i(Q)=|\{P\in Q:b_P(t)=i\}|.
\tag{6.1}
\]

Use this conservative policy:

* on an unforced block, choose the majority bit and assign that side to
  every ownership component of the block;
* on a forced block, choose zero;
* discard every active packet whose prescribed bit disagrees with its
  block bit, and force its two current rows to zero for the rest of the
  route word.

The exact one-stage loss of this policy is

\[
 L_t=
 \sum_{Q\ {\rm unforced}}\min\{n_0(Q),n_1(Q)\}
 +\sum_{Q\ {\rm forced}}n_1(Q).
\tag{6.2}
\]

Every intermediate family is an integral exact factor. Every surviving
packet follows its prescribed bit, every discarded packet remains a
coherent two-row lineage at its freeze point, and every earlier frozen row
persists.

For a route word of length \(T\), recompute the fresh components, active
packets, and forced blocks after every actual cut. If \(N_t\) is the number
of still-successful active packets, then

\[
 N_t=N_{t-1}-L_t,\qquad
 N_T=N_0-\sum_{t=1}^{T}L_t.
\tag{6.3}
\]

If every renewal round on an unresolved packet set \(U\) has a coherent
route word satisfying the pathwise bound

\[
 \sum_{t=1}^{T}L_t\le(1-\eta)|U|,
\tag{6.4}
\]

then at least \(\eta|U|\) packets are successfully routed and frozen.
If the coherent failures are legal current candidates in the next renewal
round, with all accumulated forced rows included, then

\[
 |U_r|\le(1-\eta)^r|U_0|.
\tag{6.5}
\]

#### Proof

If every packet in a connected block is retained, a shared ownership
component forces all incident prescribed bits to agree, and connectedness
propagates the equality. The stated policy imposes this stronger
block-uniform condition even after minority packets are discarded. Thus both
rows of every packet receive the same identity/\(\sigma_t\) action.
Switching exactly the bit-one ownership components is a legal
complete-component cut. Forced-zero components keep all frozen rows fixed.

The policy discards exactly (6.2), proving (6.3). A packet discarded at one
stage is frozen for the remainder of the word, so its two lineages remain
coherent. At the end, the survivors are the successfully routed packets and
the failures number \(\sum_tL_t\), proving (6.4)--(6.5). \(\square\)

The policy is sufficient and preserves coherence of every failed packet.
If failed packets may instead be sacrificed permanently, it need not be
optimal: deleting a connector packet may split a block and permit a
nonconstant signing. For example, take components
\(A,B,C,D\), \(M\) bit-zero packets on \(A\!-\!B\), one bit-zero connector
on \(B\!-\!C\), and \(M\) bit-one packets on \(C\!-\!D\). A uniform
majority loses \(M\) packets, whereas
\[
 A=B=0,\qquad C=D=1
\]
loses only the connector, whose two row lineages are no longer required to
remain coherent.

### Lemma 6.2 (seam conflict under route-bit correlation)

Fix one colour. Suppose each of \(s\) distinct unordered moved-root seam
orbits joins two active two-row packet cells and crosses the current route
bit \(b_P(t)\). Then the block-uniform loss satisfies

\[
 L_t\ge\frac{s}{2n}.
\tag{6.6}
\]

#### Proof

Every such seam lies in a control block containing both bit values, so at
least one endpoint packet is discarded. A two-row packet owns \(2n\)
middle roots, and for a fixed colour each root has at most one seam
incidence. One discarded packet therefore covers at most \(2n\) seams.
\(\square\)

K10's seam theorem does not satisfy the hypotheses of Lemma 6.2. Its seams
cross the earlier preparation bit; an outside endpoint may be an unrouted
background row; and (5.1) is summed over separate fresh overlays whose seams
are not known to persist sequentially. Coordinate-menu degree three bounds
coordinate congestion, not ownership-component size or the losses (6.2).

The exact missing positive statement is (6.4), with all component
partitions and forced blocks quantified along the realized history.

### Corollary 6.3 (clean-cover plus routed survival)

Suppose renewal round \(r\) begins with \(R_{r-1}\) unresolved rows and
supplies a pairwise row-disjoint coherent candidate packet set
\(\mathcal E_r\), with both current rows of every candidate lying in
\(R_{r-1}\), satisfying

\[
 2|\mathcal E_r|\ge p|R_{r-1}|_{\mathrm{row}}.
\tag{6.7}
\]

Suppose its actual menu word, with every earlier frozen row forced zero,
has total block-uniform packet loss at most
\((1-\gamma)|\mathcal E_r|\).
Freeze the successful rows and retain the coherent failures as unresolved.
Then

\[
 |R_r|_{\mathrm{row}}
 \le(1-p\gamma)|R_{r-1}|_{\mathrm{row}},
\qquad
 |R_r|_{\mathrm{row}}
 \le(1-p\gamma)^rB.
\tag{6.8}
\]

If \(p\ge1/17\) and \(\gamma\ge1/16\), then
\[
 r=\lceil272\log m\rceil
\]
leaves at most \(B/m\) unresolved rows. If each newly frozen row is charged
at most \(H\) certified tags, their cumulative source ledger is at most
\(HB=o(W)\).

#### Proof

Theorem 6.1 routes at least a \(\gamma\)-fraction of the candidate packets
in (6.7), so at least
\(2\gamma|\mathcal E_r|\ge
p\gamma|R_{r-1}|_{\mathrm{row}}\) rows are newly frozen. This proves
(6.8). Since \(p\gamma\ge1/272\),
\[
 (1-p\gamma)^{272\log m}\le m^{-1}.
\]
Every row is newly frozen at most once, giving the tag bound. \(\square\)

This corollary controls the routed source tags, not the untagged action of
the complete components dragged along by the menu word.

---

## 7. Local-packet speed limit

### Theorem 7.1

Suppose round \(t\) switches \(r_t\) pairwise row-disjoint aligned
first-shadow packet trades, each having exactly two positive and two
negative first-shadow cells, even when the legal trades are freshly
recomputed after earlier rounds. Then

\[
 M_1(F_{t-1})-M_1(F_t)\le2r_t,
 \qquad r_t\le\lfloor B/2\rfloor.
\tag{7.1}
\]

Consequently,

\[
 M_1(F_0)-M_1(F_T)\le BT.
\tag{7.2}
\]

If \(M_1(F_0)\ge\delta W\) and \(M_1(F_T)=o(W)\), then

\[
 T\ge(\delta-o(1))n.
\tag{7.3}
\]

#### Proof

One two-for-two trade has only two positive first-shadow cells, so it fills
at most two holes. Its negative shore uses two distinct current rows, while
a simultaneous row-disjoint round has only \(B\) rows. This proves (7.1);
summing proves (7.2), and \(W=nB\) gives (7.3). \(\square\)

Therefore an \(O(\log m)\)-round global repair must leave this aligned
four-cell packet architecture. It may use nonlocal complete components or
genuinely high-footprint two-row components. The seam-rich menu locates
possible nonlocal components, but does not yet supply their correlated signs
or persistence.

---

## 8. Proved and conditional boundary

Unconditionally proved:

1. The native laminar atlas has a literal geometrically shrinking schedule
   and exact persistence, but covers only \((1/8+o(1))B\) rows and can
   repair only \(o(W)\) first-shadow holes.
2. Whole-factor conjugation preserves clean-atlas coverage and, together
   with transported native toggles, has normal form \(gF_\varepsilon\).
3. The partial conjugation fixing \(Z\) and conjugating all of \(Z^c\) is
   literal exactly under \(\sigma Z=Z\). Every productive seam violates
   that condition, and no nontrivial fixed \(Z\) is shielded through an
   \(S_n\)-generating menu.
4. Formula (6.2) is an exact pathwise sufficient ledger for block-uniform
   packet routing and frozen-row persistence.
5. Aligned two-for-two packets with two positive first-shadow cells need
   \(\Omega(n)\) rounds to remove a fixed positive first-shadow defect.

There are two exact conditional implications.

* If every reached factor and scheduled residual set satisfies the direct
  complete-cell property \(\mathrm{HLC}_{1/17}(B/m)\), Theorem 3.2 gives an
  actual sequence leaving \(W/m=o(W)\) unresolved middle roots after
  \(\lceil17\log m\rceil\) renewals, with certified tag charge
  \(O_A(W/\sqrt m)=o(W)\).
* If the clean cover first has to be routed through the degree-three menu,
  and the route retains a fraction \(\gamma\) of a \(p\)-fraction candidate
  set at every actual history, Corollary 6.3 gives decay rate
  \(1-p\gamma\). In particular \(p\ge1/17\) and \(\gamma\ge1/16\) give
  \(B/m\) unresolved rows after \(\lceil272\log m\rceil\) renewals.

In either case, if a final fresh overlay additionally satisfies K10's
charged common-TU hypotheses with \(o(W)\) charged residue, one further
literal complete-component signing gives \(J_A=o(W)\).
This last signing need not preserve the earlier routed rows unless its
common-TU system also includes the corresponding forced-zero constraints.

Neither the direct \(\mathrm{HLC}_{1/17}(B/m)\) property nor the routed
survival hypothesis follows from the seam-rich degree-three menu. The
requested unconditional global sequence is therefore not proved.

The precise missing positive theorem is a hereditary fresh-component
regeneration theorem: along the actual history, a \(p\ge1/17\) fraction of
the residual rows must admit current coherent packet routes, a fixed
\(\gamma>0\) fraction of those candidates must survive the forced
control-block losses, and the collateral multidepth charge must be \(o(W)\)
cumulatively. This is stronger than fresh-coordinate orbit capacity and is
exactly what is needed for geometric renewal of the verified
\(1/16\)-density reservoir. Constant one still additionally requires the
final charged common-TU/off-residue feasibility stated above, including
globally compatible tag destinations if earlier routes must persist.

---

## 9. Independent audit

Three independent audits checked the Catalan/TU constants, the shifted
first-bit theorem, covariance and shielding, control-block retries and
geometric constants, the aligned-packet speed limit, and the final
implication scope. All identified corrections were incorporated. The final
audit is recorded in
\[
\texttt{MATH\_ATTACK\_K11\_ITERATED\_LAMINAR\_CONJUGATE\_DECAY\_AUDIT\_20260725.md}.
\]
